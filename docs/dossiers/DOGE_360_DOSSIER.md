# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 01:29:56 IST` (`2026-10-29 19:59:56 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0783` | **Live Ask Quote**: `0.0804` | **Mid Price**: `0.0794`
- **Spread Points**: `21.00` | **Spread BPS**: `264.65 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0778` | VWAP Z-Score: `+0.49` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000407` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.96` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0804` | Lower -3.00σ Band: `0.0751`
  * Upper +2.51σ Band: `0.0800` | Lower -2.51σ Band: `0.0755`
  * Upper +2.01σ Band: `0.0795` | Lower -2.01σ Band: `0.0760`
  * Upper +2.00σ Band: `0.0795` | Lower -2.00σ Band: `0.0760`
  * Upper +1.28σ Band: `0.0789` | Lower -1.28σ Band: `0.0766`
  * Upper +1.00σ Band: `0.0787` | Lower -1.00σ Band: `0.0769`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0782` | EMA-20=`0.0784` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0781` (Slope: `+0.0000`) | EMA-100=`0.0780`
  * Institutional Anchors: EMA-144=`0.0779` | EMA-200=`0.0777` (Slope: `+0.1137`) | EMA-233=`0.0776`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0763` | Weekly High=`0.0803` | Weekly Low=`0.0755`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0786` (Distance: `+0.95%`)
  * Point of Control (POC) = `0.0767` (Distance: `+3.47%`)
  * Value Area Low (VAL) = `0.0764` (Distance: `+3.87%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `0.0790` - `0.0797`
  * Optimal Trade Entry (OTE 0.705): `0.0795`
  * Structural Invalidation Anchor (0.786): `0.0800`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0791` | `0.0794` | `0.0791` | `0.0794` | `9,582,874` | 760,106.77 USD | 169,893.00 USD | `+22.35%` | -8,913,931.19 USD | `+0.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0794` | `0.0794` | `0.0793` | `0.0793` | `7,873,701` | 624,833.06 USD | 200,773.46 USD | `+32.13%` | -8,713,157.73 USD | `+0.65` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.0793` | `0.0795` | `0.0793` | `0.0794` | `8,194,422` | 650,808.99 USD | 371,685.54 USD | `+57.11%` | -8,341,472.19 USD | `+1.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0793` | `0.0793` | `0.0791` | `0.0791` | `27,310,868` | 2,162,354.33 USD | -538,046.61 USD | `-24.88%` | -8,882,131.14 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.0791` | `0.0792` | `0.0790` | `0.0791` | `20,524,754` | 1,623,560.28 USD | -201,693.05 USD | `-12.42%` | -9,083,824.19 USD | `-0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0791` | `0.0795` | `0.0791` | `0.0794` | `25,832,285` | 2,050,137.64 USD | 756,740.83 USD | `+36.91%` | -8,327,083.36 USD | `+1.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0801` | `0.0802` | `0.0792` | `0.0796` | `261,755,492` | 20,864,959.87 USD | -2,385,280.59 USD | `-11.43%` | -9,433,626.40 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0796` | `0.0797` | `0.0789` | `0.0793` | `184,672,867` | 14,645,934.56 USD | 790,590.21 USD | `+5.40%` | -8,643,036.19 USD | `+0.90` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.0793` | `0.0795` | `0.0790` | `0.0794` | `73,486,619` | 5,821,663.42 USD | 2,612.34 USD | `+0.04%` | -8,640,423.85 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0794` | `1,008,269,009` | 80,689,360.24 USD | -2,771,578.68 USD | `-3.43%` | -8,626,035.02 USD | `-0.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0797` | `0.0799` | `0.0774` | `0.0778` | `998,970,852` | 78,232,937.14 USD | -7,024,064.25 USD | `-8.98%` | -3,060,763.89 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -7,420,203.26 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0794` | `1,008,269,009` | 80,689,360.24 USD | -2,771,578.68 USD | `-3.43%` | -8,626,035.02 USD | `-0.31` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.0794`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0793` | `46668.0000` | 3,703.06 USD | 52,735.64 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `9212.0000` | 730.95 USD | 53,466.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `389838.0000` | 30,932.09 USD | 84,398.68 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `464714.0000` | 36,872.73 USD | 121,271.41 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `66261.0000` | 5,257.41 USD | 126,528.82 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `143730.0000` | 11,403.97 USD | 137,932.79 USD | `2 orders` | `-0.04%` | `-` |
| `ASK` | `0.0794` | `78808.0000` | 6,257.75 USD | 149,913.26 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `429959.0000` | 34,140.03 USD | 143,655.51 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `6072.0000` | 482.13 USD | 109,515.48 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `50458.0000` | 4,006.37 USD | 109,033.35 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `5748.0000` | 456.39 USD | 105,026.98 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `39937.0000` | 3,170.92 USD | 104,570.60 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `18891.0000` | 1,499.89 USD | 101,399.68 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `31174.0000` | 2,475.09 USD | 99,899.79 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `18891.0000` | 1,499.85 USD | 97,424.70 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `116293.0000` | 9,232.97 USD | 95,924.85 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `154604.0000` | 12,274.48 USD | 86,691.88 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `18891.0000` | 1,499.79 USD | 74,417.41 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `408564.0000` | 32,436.30 USD | 72,917.61 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `31177.0000` | 2,475.14 USD | 40,481.31 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0794` | `20841.0000` | 1,654.55 USD | 38,006.16 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `0.0794` | `179173.0000` | 14,224.01 USD | 36,351.62 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0794` | `236192.0000` | 18,749.87 USD | 22,127.61 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0794` | `5039.0000` | 400.01 USD | 3,377.75 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0794` | `32473.0000` | 2,577.74 USD | 2,977.74 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `0.0794` | `5039.0000` | 400.00 USD | 400.00 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0794` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0794` | `15850.0000` | 1,258.13 USD | 1,258.13 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0794` | `5040.0000` | 400.02 USD | 1,658.15 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0794` | `8040.0000` | 638.11 USD | 2,296.26 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0794` | `39643.0000` | 3,146.31 USD | 5,442.56 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0794` | `88198.0000` | 6,999.75 USD | 12,442.31 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0794` | `12284.0000` | 974.90 USD | 13,417.20 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0794` | `120414.0000` | 9,556.30 USD | 22,973.50 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0794` | `1034.0000` | 82.06 USD | 23,055.56 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0794` | `5040.0000` | 399.97 USD | 23,455.53 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0794` | `129048.0000` | 10,240.99 USD | 33,696.52 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0794` | `51083.0000` | 4,053.79 USD | 37,750.31 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0794` | `12283.0000` | 974.73 USD | 38,725.04 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0794` | `12283.0000` | 974.71 USD | 39,699.75 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0794` | `117616.0000` | 9,332.83 USD | 49,032.58 USD | `1 orders` | `-0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `302` | `0xb83d...6e36` | `SHORT` | 8,144,132.98 USD | `102,645,925.00` | `0.0946` | `0.0793` | `1.30` | 1,563,208.67 USD | `+19.19%` | `3X Cross` |
| `312` | `0xc63a...a3cd` | `LONG` | 7,933,300.00 USD | `100,000,000.00` | `0.0856` | `0.0793` | `0.000000` | -631,521.96 USD | `-7.96%` | `10X Cross` |
| `317` | `0x610b...b613` | `LONG` | 7,828,490.08 USD | `98,666,424.00` | `0.0872` | `0.0793` | `0.0585` | -771,691.82 USD | `-9.86%` | `5X Cross` |
| `593` | `0x5b5d...c060` | `SHORT` | 3,924,819.15 USD | `49,478,955.00` | `0.0946` | `0.0793` | `3.11` | 756,697.46 USD | `+19.28%` | `3X Cross` |
| `632` | `0xca49...53c8` | `SHORT` | 3,692,274.89 USD | `46,542,649.00` | `0.0929` | `0.0793` | `0.3490` | 633,769.79 USD | `+17.16%` | `10X Cross` |
| `644` | `0x45d2...4029` | `SHORT` | 3,603,417.45 USD | `45,426,000.00` | `0.0954` | `0.0793` | `0.8561` | 732,211.77 USD | `+20.32%` | `10X Cross` |
| `797` | `0xecb6...2b00` | `SHORT` | 2,946,998.84 USD | `37,152,820.00` | `0.0796` | `0.0793` | `0.7882` | 9,961.00 USD | `+0.34%` | `10X Cross` |
| `1187` | `0x458d...ab3b` | `LONG` | 1,941,041.25 USD | `24,454,063.00` | `0.1002` | `0.0793` | `0.0714` | -509,880.65 USD | `-26.27%` | `3X Isolated` |
| `1190` | `0xeadc...9d55` | `LONG` | 1,928,907.98 USD | `24,317,440.00` | `0.0926` | `0.0793` | `0.000000` | -322,686.60 USD | `-16.73%` | `10X Cross` |
| `1238` | `0x9aa5...58af` | `SHORT` | 1,864,083.16 USD | `23,500,500.00` | `0.0907` | `0.0793` | `0.3971` | 266,671.79 USD | `+14.31%` | `10X Cross` |
| `1330` | `0xf48f...10fe` | `LONG` | 1,699,905.29 USD | `21,424,497.00` | `0.0968` | `0.0793` | `0.0344` | -374,399.32 USD | `-22.02%` | `4X Cross` |
| `1371` | `0x9946...0852` | `SHORT` | 1,658,781.21 USD | `20,910,149.00` | `0.0871` | `0.0793` | `0.1317` | 161,774.18 USD | `+9.75%` | `10X Cross` |
| `1553` | `0xcac1...26b3` | `SHORT` | 1,438,237.47 USD | `18,126,835.00` | `0.0943` | `0.0793` | `0.5082` | 271,221.73 USD | `+18.86%` | `10X Cross` |
| `1596` | `0x0d6a...ca57` | `LONG` | 1,398,588.70 USD | `17,626,455.00` | `0.0875` | `0.0793` | `0.0626` | -143,516.26 USD | `-10.26%` | `3X Isolated` |
| `1643` | `0x4808...a82c` | `LONG` | 1,334,858.79 USD | `16,828,143.00` | `0.0883` | `0.0793` | `0.0632` | -151,614.19 USD | `-11.36%` | `3X Cross` |
| `1775` | `0x31ef...f715` | `LONG` | 1,208,401.98 USD | `15,230,102.00` | `0.0936` | `0.0793` | `0.0668` | -217,293.95 USD | `-17.98%` | `3X Isolated` |
| `1793` | `0xbfc7...80b4` | `SHORT` | 1,191,401.42 USD | `15,020,000.00` | `0.0920` | `0.0793` | `0.3741` | 190,997.87 USD | `+16.03%` | `10X Cross` |

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
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0174` | 198.71 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0184` | 1,110.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0186` | 320.23 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0191` | 16,770.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0203` | 125.67 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0210` | 295.48 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0217` | 435.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 345.98 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0238` | 615.03 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0240` | 481.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0246` | 12,100.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0249` | 4,670.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0260` | 391.04 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0267` | 3,500.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0268` | 6,030.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 1,080.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0280` | 149.90 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0283` | 486.58 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0285` | 2,320.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0289` | 769.46 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0296` | 574.59 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0301` | 2,460.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 4,240.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0328` | 2,630.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0333` | 150.12 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0335` | 1,590.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 1,690.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 16,930.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 33,300.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 210.51 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0357` | 4,370.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0362` | 774,500.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 195.51 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0372` | 3,350.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0376` | 77,600.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 3,810.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0379` | 1,030.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 246.45 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 1,000.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 1,050.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 221.10 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0398` | 103,180.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0403` | 30,260.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0411` | 2,800.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 59,100.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 2,090.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,740.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 2,080.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 7,270.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0428` | 2,150.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 6,430.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 3,810.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 14,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 2,000.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0469` | 15,210.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,010.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 593.13 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0478` | 298.34 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,500.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 18,690.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 826.08 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 1,710.00 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 980.43 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 1,200.00 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 4,290.00 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 395.09 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 181,950.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,770.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 315,090.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 53,680.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 13,510.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 1,810.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 2,510.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 1,420.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0549` | 298.32 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 772.30 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 101.07 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 772.62 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 1,010.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 747.06 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 1,040.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 644.99 USD | 13,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,590.00 USD | 13,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 5,730,000.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 4,160.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 392.08 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 9,120.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 889.30 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,660.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,650.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 4,560.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 380.38 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 18,120.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 548.46 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 23,320.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,830.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,220.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 1,490.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,220.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 913.21 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,400.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 13,460.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 528.46 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 1,820.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 3,470.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 168.28 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,750.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,080.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 1,470.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 32,500.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 8,670.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,360.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 633.29 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 2,170.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 23,050.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 3,520.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 87,470.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 9,910.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 7,430.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 5,340.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 20,790.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 71,100.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 11,990.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 23,130.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 27,600.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,030.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 66,550.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 1,490.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,020,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 389.18 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,630.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 899.27 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 196.64 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 96,360.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 2,070.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 5,100.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0679` | 20,030.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0682` | 1,680.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0684` | 6,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 7,740.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0687` | 1,410.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 69,020.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 517.48 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 3,670.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 52,390.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,840.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0696` | 15,100.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,420.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0699` | 9,500.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 2,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 93,740.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0707` | 93,520.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0711` | 24,090,000.00 USD | 24,090,000.00 USD | 33,080.00 USD | 20,050.00 USD | 85,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0712` | 23,950,000.00 USD | 23,950,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 23,890,000.00 USD | 23,890,000.00 USD | 34,400.00 USD | 58,130.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 23,730,000.00 USD | 23,730,000.00 USD | 32,300.00 USD | 33,120.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,220.00 USD | 843,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 23,660,000.00 USD | 23,660,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,230.00 USD | 840,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 23,590,000.00 USD | 23,590,000.00 USD | 30,130.00 USD | 31,610.00 USD | 270.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 2,780.00 USD | 832,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 23,530,000.00 USD | 23,530,000.00 USD | 15,510.00 USD | 7,710.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,520.00 USD | 829,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 23,490,000.00 USD | 23,490,000.00 USD | 63,040.00 USD | 36,880.00 USD | 50,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 10,850.00 USD | 828,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 23,340,000.00 USD | 23,340,000.00 USD | 15,840.00 USD | 3,820.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 817,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 23,310,000.00 USD | 23,310,000.00 USD | 48,000.00 USD | 15,600.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 23,870.00 USD | 816,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 23,210,000.00 USD | 23,210,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0722` | 23,150,000.00 USD | 23,150,000.00 USD | 29,680.00 USD | 15,630.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 10,450.00 USD | 792,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 23,070,000.00 USD | 23,070,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 163.73 USD | 782,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 22,960,000.00 USD | 22,960,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 87,670.00 USD | 782,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 22,830,000.00 USD | 22,830,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 694,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 22,670,000.00 USD | 22,670,000.00 USD | 31,660.00 USD | 0.00 USD | 175.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 694,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 22,640,000.00 USD | 22,640,000.00 USD | 20,420.00 USD | 0.00 USD | 285.35 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 3,170.00 USD | 693,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 22,620,000.00 USD | 22,620,000.00 USD | 15,580.00 USD | 802.30 USD | 261.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 646.11 USD | 690,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 22,600,000.00 USD | 22,600,000.00 USD | 17,820.00 USD | 0.00 USD | 18,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 76,420.00 USD | 689,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 22,570,000.00 USD | 22,570,000.00 USD | 14,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,300.00 USD | 613,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 22,550,000.00 USD | 22,550,000.00 USD | 42,980.00 USD | 0.00 USD | 187.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 602,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 22,510,000.00 USD | 22,510,000.00 USD | 42,110.00 USD | 0.00 USD | 41.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 5,410.00 USD | 600,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 22,470,000.00 USD | 22,470,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 22,450,000.00 USD | 22,450,000.00 USD | 4,580.00 USD | 0.00 USD | 258.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,000.00 USD | 595,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 22,450,000.00 USD | 22,450,000.00 USD | 24,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 588,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 22,430,000.00 USD | 22,430,000.00 USD | 8,600.00 USD | 0.00 USD | 1.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 584,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 22,420,000.00 USD | 22,420,000.00 USD | 48,230.00 USD | 0.00 USD | 154.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,390.00 USD | 578,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 22,370,000.00 USD | 22,370,000.00 USD | 31,820.00 USD | 0.00 USD | 162.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 5,430.00 USD | 568,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 22,340,000.00 USD | 22,340,000.00 USD | 32,610.00 USD | 0.00 USD | 107.41 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 15,010.00 USD | 563,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 22,300,000.00 USD | 22,300,000.00 USD | 33,740.00 USD | 0.00 USD | 380.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 463,970.00 USD | 548,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 22,270,000.00 USD | 22,270,000.00 USD | 31,820.00 USD | 0.00 USD | 348.56 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 777.39 USD | 84,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 22,240,000.00 USD | 22,240,000.00 USD | 25,930.00 USD | 0.00 USD | 596.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 83,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 22,210,000.00 USD | 22,210,000.00 USD | 28,250.00 USD | 27,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 2,140.00 USD | 82,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 22,160,000.00 USD | 22,160,000.00 USD | 41,210.00 USD | 1,840.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,040.00 USD | 79,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 22,100,000.00 USD | 22,100,000.00 USD | 106,370.00 USD | 57,220.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,420.00 USD | 77,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 21,910,000.00 USD | 21,910,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,050.00 USD | 76,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0747` | 21,370,000.00 USD | 21,370,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0747` | 359.77 USD | 75,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 20,910,000.00 USD | 20,910,000.00 USD | 169,810.00 USD | 65,720.00 USD | 99,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 20,580,000.00 USD | 20,580,000.00 USD | 194,160.00 USD | 144,960.00 USD | 8,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0750` | 1,370.00 USD | 74,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0750` | 20,230,000.00 USD | 20,230,000.00 USD | 233,830.00 USD | 83,730.00 USD | 120,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 451.13 USD | 73,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0751` | 19,790,000.00 USD | 19,790,000.00 USD | 268,200.00 USD | 82,120.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 1,480.00 USD | 73,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0752` | 19,370,000.00 USD | 19,370,000.00 USD | 117,830.00 USD | 19,450.00 USD | 85,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0752` | 3,910.00 USD | 71,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0753` | 19,150,000.00 USD | 19,150,000.00 USD | 133,330.00 USD | 72,710.00 USD | 28,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0754` | 208.64 USD | 67,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0754` | 18,920,000.00 USD | 18,920,000.00 USD | 87,330.00 USD | 62,330.00 USD | 19,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0755` | 4,060.00 USD | 67,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0755` | 18,750,000.00 USD | 18,750,000.00 USD | 109,960.00 USD | 15,650.00 USD | 69,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 977.84 USD | 63,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0756` | 18,550,000.00 USD | 18,550,000.00 USD | 164,890.00 USD | 147,310.00 USD | 112,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 516.61 USD | 62,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0757` | 18,130,000.00 USD | 18,130,000.00 USD | 88,960.00 USD | 44,210.00 USD | 103,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0757` | 3,270.00 USD | 62,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0758` | 17,890,000.00 USD | 17,890,000.00 USD | 70,320.00 USD | 31,960.00 USD | 91,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0759` | 5,070.00 USD | 58,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0759` | 17,700,000.00 USD | 17,700,000.00 USD | 195,880.00 USD | 130,420.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0760` | 32,080.00 USD | 53,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0760` | 17,360,000.00 USD | 17,360,000.00 USD | 235,330.00 USD | 313,670.00 USD | 277,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,690.00 USD | 21,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0761` | 16,540,000.00 USD | 16,540,000.00 USD | 500,630.00 USD | 440,880.00 USD | 277,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 190.38 USD | 19,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0762` | 15,320,000.00 USD | 15,320,000.00 USD | 579,620.00 USD | 303,280.00 USD | 223,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0762` | 181.93 USD | 19,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0763` | 14,210,000.00 USD | 14,210,000.00 USD | 305,000.00 USD | 179,660.00 USD | 197,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0764` | 11,510.00 USD | 19,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0764` | 13,530,000.00 USD | 13,530,000.00 USD | 356,430.00 USD | 327,090.00 USD | 23,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0765` | 12,820,000.00 USD | 12,820,000.00 USD | 497,560.00 USD | 213,120.00 USD | 313,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0766` | 11,800,000.00 USD | 11,800,000.00 USD | 621,080.00 USD | 262,670.00 USD | 279,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0767` | 10,630,000.00 USD | 10,630,000.00 USD | 229,810.00 USD | 78,490.00 USD | 214,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0768` | 10,110,000.00 USD | 10,110,000.00 USD | 426,850.00 USD | 236,860.00 USD | 142,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0769` | 9,300,000.00 USD | 9,300,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0770` | 8,810,000.00 USD | 8,810,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0771` | 8,150,000.00 USD | 8,150,000.00 USD | 231,550.00 USD | 266,030.00 USD | 189,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0772` | 7,470,000.00 USD | 7,470,000.00 USD | 169,730.00 USD | 297,590.00 USD | 333,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0773` | 6,670,000.00 USD | 6,670,000.00 USD | 272,980.00 USD | 149,960.00 USD | 241,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0774` | 6,000,000.00 USD | 6,000,000.00 USD | 143,850.00 USD | 97,350.00 USD | 230,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0775` | 5,530,000.00 USD | 5,530,000.00 USD | 359,420.00 USD | 150,850.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0776` | 5,000,000.00 USD | 5,000,000.00 USD | 137,380.00 USD | 345,400.00 USD | 381,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0777` | 4,140,000.00 USD | 4,140,000.00 USD | 74,870.00 USD | 182,120.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0778` | 3,870,000.00 USD | 3,870,000.00 USD | 148,860.00 USD | 120,190.00 USD | 200,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0779` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 85,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0780` | 3,310,000.00 USD | 3,310,000.00 USD | 217,760.00 USD | 88,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0781` | 3,010,000.00 USD | 3,010,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0782` | 2,960,000.00 USD | 2,960,000.00 USD | 44,780.00 USD | 75,640.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0783` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0784` | 2,700,000.00 USD | 2,700,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0785` | 2,150,000.00 USD | 2,150,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0786` | 1,810,000.00 USD | 1,810,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0787` | 1,280,000.00 USD | 1,280,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0788` | 689,800.00 USD | 689,800.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0789` | 267,030.00 USD | 267,030.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0790` | 36,980.00 USD | 36,980.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0791` | 33,720.00 USD | 33,720.00 USD | 0.00 USD | 3,690.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0791` | 8,030.00 USD | 8,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 16,260.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 414,540.00 USD | 414,540.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 569,220.00 USD | 569,220.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 912,240.00 USD | 912,240.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 917,850.00 USD | 917,850.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 928,750.00 USD | 928,750.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 1,100,000.00 USD | 1,100,000.00 USD | 3,520.00 USD | 0.00 USD | 162,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 1,540,000.00 USD | 1,540,000.00 USD | 200,420.00 USD | 208,070.00 USD | 40,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 2,610,000.00 USD | 2,610,000.00 USD | 411,890.00 USD | 131,030.00 USD | 522,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 3,360,000.00 USD | 3,360,000.00 USD | 445,800.00 USD | 291,790.00 USD | 12,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 3,970,000.00 USD | 3,970,000.00 USD | 293,220.00 USD | 180,540.00 USD | 132,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 241,410.00 USD | 233.41 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 4,510,000.00 USD | 4,510,000.00 USD | 93,910.00 USD | 75,260.00 USD | 135,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 4,770,000.00 USD | 4,770,000.00 USD | 27,080.00 USD | 18,240.00 USD | 208,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 5,190,000.00 USD | 5,190,000.00 USD | 22,430.00 USD | 10,710.00 USD | 386,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 5,680,000.00 USD | 5,680,000.00 USD | 232,650.00 USD | 151,890.00 USD | 112,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 6,560,000.00 USD | 6,560,000.00 USD | 441,880.00 USD | 245,220.00 USD | 189,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 7,200,000.00 USD | 7,200,000.00 USD | 361,650.00 USD | 152,470.00 USD | 130,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 710.08 USD | 710.08 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 7,990,000.00 USD | 7,990,000.00 USD | 298,910.00 USD | 161,880.00 USD | 322,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 8,680,000.00 USD | 8,680,000.00 USD | 171,350.00 USD | 368,950.00 USD | 156,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 9,680,000.00 USD | 9,680,000.00 USD | 215,860.00 USD | 275,570.00 USD | 499,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 10,400,000.00 USD | 10,400,000.00 USD | 383,530.00 USD | 167,310.00 USD | 170,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 11,030,000.00 USD | 11,030,000.00 USD | 260,030.00 USD | 184,710.00 USD | 187,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 11,380,000.00 USD | 11,380,000.00 USD | 264,720.00 USD | 75,420.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 11,950,000.00 USD | 11,950,000.00 USD | 147,030.00 USD | 226,510.00 USD | 198,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 12,200,000.00 USD | 12,200,000.00 USD | 124,920.00 USD | 94,070.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 12,550,000.00 USD | 12,550,000.00 USD | 102,880.00 USD | 60,100.00 USD | 190,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 12,650,000.00 USD | 12,650,000.00 USD | 52,670.00 USD | 48,230.00 USD | 675.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 12,920,000.00 USD | 12,920,000.00 USD | 224,210.00 USD | 37,180.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 13,280,000.00 USD | 13,280,000.00 USD | 206,610.00 USD | 79,000.00 USD | 72,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 13,790,000.00 USD | 13,790,000.00 USD | 262,060.00 USD | 98,430.00 USD | 150,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 13,970,000.00 USD | 13,970,000.00 USD | 97,970.00 USD | 39,590.00 USD | 42,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 11,330.00 USD | 12,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 14,380,000.00 USD | 14,380,000.00 USD | 233,350.00 USD | 91,440.00 USD | 86,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 14,640,000.00 USD | 14,640,000.00 USD | 159,920.00 USD | 68,410.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 150.95 USD | 12,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0834` | 14,980,000.00 USD | 14,980,000.00 USD | 146,880.00 USD | 60,550.00 USD | 133,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 15,360,000.00 USD | 15,360,000.00 USD | 110,610.00 USD | 184,470.00 USD | 78,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 15,730,000.00 USD | 15,730,000.00 USD | 71,510.00 USD | 84,520.00 USD | 221,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 12,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 16,020,000.00 USD | 16,020,000.00 USD | 189,060.00 USD | 61,550.00 USD | 34,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 14,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 16,290,000.00 USD | 16,290,000.00 USD | 145,530.00 USD | 76,380.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 16,360,000.00 USD | 16,360,000.00 USD | 67,620.00 USD | 0.00 USD | 855.10 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 104.69 USD | 14,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0840` | 16,410,000.00 USD | 16,410,000.00 USD | 35,250.00 USD | 15,480.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0840` | 17,690.00 USD | 31,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0841` | 16,440,000.00 USD | 16,440,000.00 USD | 32,120.00 USD | 2,010.00 USD | 458.39 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 16,520,000.00 USD | 16,520,000.00 USD | 30,040.00 USD | 0.00 USD | 47,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 31,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0843` | 16,560,000.00 USD | 16,560,000.00 USD | 37,310.00 USD | 0.00 USD | 140.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 16,640,000.00 USD | 16,640,000.00 USD | 81,010.00 USD | 0.00 USD | 168.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 16,660,000.00 USD | 16,660,000.00 USD | 15,700.00 USD | 0.00 USD | 575.75 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 16,740,000.00 USD | 16,740,000.00 USD | 72,340.00 USD | 16,670.00 USD | 0.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 213.74 USD | 32,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 16,760,000.00 USD | 16,760,000.00 USD | 12,740.00 USD | 0.00 USD | 304.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 16,770,000.00 USD | 16,770,000.00 USD | 11,540.00 USD | 0.00 USD | 404.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0849` | 16,780,000.00 USD | 16,780,000.00 USD | 6,070.00 USD | 0.00 USD | 292.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 16,800,000.00 USD | 16,800,000.00 USD | 20,730.00 USD | 0.00 USD | 11.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0851` | 214.75 USD | 32,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0851` | 16,830,000.00 USD | 16,830,000.00 USD | 26,040.00 USD | 11,000.00 USD | 469.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0853` | 16,850,000.00 USD | 16,850,000.00 USD | 12,910.00 USD | 737.47 USD | 450.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 16,910,000.00 USD | 16,910,000.00 USD | 35,960.00 USD | 13,190.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0855` | 17,050,000.00 USD | 17,050,000.00 USD | 64,150.00 USD | 45,460.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 17,200,000.00 USD | 17,200,000.00 USD | 92,490.00 USD | 32,810.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0857` | 17,300,000.00 USD | 17,300,000.00 USD | 50,540.00 USD | 18,030.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 17,380,000.00 USD | 17,380,000.00 USD | 48,130.00 USD | 36,780.00 USD | 185.71 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 32,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0859` | 17,510,000.00 USD | 17,510,000.00 USD | 72,260.00 USD | 20,870.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0859` | 135.37 USD | 32,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0860` | 17,600,000.00 USD | 17,600,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0861` | 17,650,000.00 USD | 17,650,000.00 USD | 20,430.00 USD | 0.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 216.58 USD | 32,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0862` | 17,730,000.00 USD | 17,730,000.00 USD | 33,780.00 USD | 29,080.00 USD | 11,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 35,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0863` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 219.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0864` | 17,780,000.00 USD | 17,780,000.00 USD | 22,510.00 USD | 20,050.00 USD | 5,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0865` | 17,830,000.00 USD | 17,830,000.00 USD | 31,770.00 USD | 1,280.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 17,890,000.00 USD | 17,890,000.00 USD | 25,410.00 USD | 16,310.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0867` | 17,960,000.00 USD | 17,960,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 18,020,000.00 USD | 18,020,000.00 USD | 8,080.00 USD | 9,300.00 USD | 34,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0869` | 18,080,000.00 USD | 18,080,000.00 USD | 16,230.00 USD | 8,560.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 18,140,000.00 USD | 18,140,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0871` | 18,300,000.00 USD | 18,300,000.00 USD | 34,400.00 USD | 58,130.00 USD | 62,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 18,370,000.00 USD | 18,370,000.00 USD | 32,300.00 USD | 33,120.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0873` | 18,430,000.00 USD | 18,430,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0875` | 18,460,000.00 USD | 18,460,000.00 USD | 9,700.00 USD | 17,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0876` | 9,620.00 USD | 44,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0876` | 18,500,000.00 USD | 18,500,000.00 USD | 20,430.00 USD | 14,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0877` | 18,530,000.00 USD | 18,530,000.00 USD | 8,360.00 USD | 5,020.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 45,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0882` | 104.90 USD | 45,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 45,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 46,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 46,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0896` | 6,050.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0900` | 226.85 USD | 52,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0907` | 7,590.00 USD | 60,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0909` | 884.52 USD | 61,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0910` | 114.23 USD | 61,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 743.15 USD | 62,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0912` | 4,040.00 USD | 66,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0914` | 171.19 USD | 66,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0917` | 344.43 USD | 66,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 66,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0925` | 188.14 USD | 67,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0935` | 3,300.00 USD | 70,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0949` | 573.84 USD | 70,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 13,800.00 USD | 84,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0951` | 114,180.00 USD | 198,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 747.55 USD | 199,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 200,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0964` | 48,230.00 USD | 248,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 39,190.00 USD | 287,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 288,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 10,510.00 USD | 298,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1004` | 1,290.00 USD | 299,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1007` | 1,010.00 USD | 300,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1013` | 177.90 USD | 301,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 308,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 311,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 312,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1047` | 1,030.00 USD | 313,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 319,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1075` | 3,220.00 USD | 322,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,370.00 USD | 325,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1121` | 2,290.00 USD | 328,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 328,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 1,660.00 USD | 330,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1187` | 106.19 USD | 330,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1221` | 355.95 USD | 330,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 331,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1250` | 375.15 USD | 331,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 331,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1288` | 1,560.00 USD | 333,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1293` | 2,350.00 USD | 335,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 335,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 338,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 338,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1320` | 2,760,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1381` | 997.30 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1391` | 22,550.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 1,800.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1459` | 2,340.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,320.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1484` | 701.13 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1487` | 393.33 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1512` | 1,870.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 2,010.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1519` | 56,850.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 267.55 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 195.39 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 194.45 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1568` | 341.15 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 4,830.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 980.15 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0160` | 15,950,000.00 USD | 0.00 USD | 3,930.00 USD | `-79.77%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 15,950,000.00 USD | 0.00 USD | 407.02 USD | `-79.26%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 15,950,000.00 USD | 0.00 USD | 5,290.00 USD | `-79.14%` | `319,394.00` |
| `Live` | `Long` | `0.0174` | 15,940,000.00 USD | 0.00 USD | 198.71 USD | `-78.13%` | `11,453.00` |
| `Live` | `Long` | `0.0184` | 15,940,000.00 USD | 0.00 USD | 1,110.00 USD | `-76.87%` | `60,320.00` |
| `Live` | `Long` | `0.0186` | 15,940,000.00 USD | 0.00 USD | 320.23 USD | `-76.62%` | `17,263.00` |
| `Live` | `Long` | `0.0191` | 15,940,000.00 USD | 0.00 USD | 16,770.00 USD | `-75.98%` | `880,408.00` |
| `Live` | `Long` | `0.0203` | 15,920,000.00 USD | 0.00 USD | 125.67 USD | `-74.47%` | `6,206.00` |
| `Live` | `Long` | `0.0210` | 15,920,000.00 USD | 0.00 USD | 295.48 USD | `-73.46%` | `14,037.00` |
| `Live` | `Long` | `0.0217` | 15,920,000.00 USD | 0.00 USD | 435.00 USD | `-72.58%` | `20,000.00` |
| `Live` | `Long` | `0.0232` | 15,920,000.00 USD | 0.00 USD | 345.98 USD | `-70.69%` | `14,881.00` |
| `Live` | `Long` | `0.0238` | 15,920,000.00 USD | 0.00 USD | 615.03 USD | `-70.06%` | `25,896.00` |
| `Live` | `Long` | `0.0240` | 15,920,000.00 USD | 0.00 USD | 481.00 USD | `-69.68%` | `20,000.00` |
| `Live` | `Long` | `0.0246` | 15,920,000.00 USD | 0.00 USD | 12,100.00 USD | `-68.93%` | `491,018.00` |
| `Live` | `Long` | `0.0249` | 15,910,000.00 USD | 0.00 USD | 4,670.00 USD | `-68.67%` | `187,979.00` |
| `Live` | `Long` | `0.0260` | 15,900,000.00 USD | 0.00 USD | 391.04 USD | `-67.29%` | `15,069.00` |
| `Live` | `Long` | `0.0267` | 15,900,000.00 USD | 0.00 USD | 3,500.00 USD | `-66.28%` | `130,804.00` |
| `Live` | `Long` | `0.0268` | 15,900,000.00 USD | 0.00 USD | 6,030.00 USD | `-66.15%` | `224,650.00` |
| `Live` | `Long` | `0.0276` | 15,890,000.00 USD | 0.00 USD | 1,080.00 USD | `-65.27%` | `39,049.00` |
| `Live` | `Long` | `0.0279` | 15,890,000.00 USD | 0.00 USD | 1,730.00 USD | `-64.77%` | `61,775.00` |
| `Live` | `Long` | `0.0280` | 15,890,000.00 USD | 0.00 USD | 149.90 USD | `-64.64%` | `5,344.00` |
| `Live` | `Long` | `0.0283` | 15,890,000.00 USD | 0.00 USD | 486.58 USD | `-64.39%` | `17,224.00` |
| `Live` | `Long` | `0.0285` | 15,890,000.00 USD | 0.00 USD | 2,320.00 USD | `-64.01%` | `81,125.00` |
| `Live` | `Long` | `0.0289` | 15,890,000.00 USD | 0.00 USD | 769.46 USD | `-63.63%` | `26,671.00` |
| `Live` | `Long` | `0.0296` | 15,890,000.00 USD | 0.00 USD | 574.59 USD | `-62.62%` | `19,379.00` |
| `Live` | `Long` | `0.0301` | 15,890,000.00 USD | 0.00 USD | 2,460.00 USD | `-61.99%` | `81,743.00` |
| `Live` | `Long` | `0.0306` | 15,880,000.00 USD | 0.00 USD | 4,240.00 USD | `-61.49%` | `138,941.00` |
| `Live` | `Long` | `0.0328` | 15,880,000.00 USD | 0.00 USD | 2,630.00 USD | `-58.59%` | `80,000.00` |
| `Live` | `Long` | `0.0333` | 15,880,000.00 USD | 0.00 USD | 150.12 USD | `-58.08%` | `4,515.00` |
| `Live` | `Long` | `0.0335` | 15,880,000.00 USD | 0.00 USD | 1,590.00 USD | `-57.83%` | `47,501.00` |
| `Live` | `Long` | `0.0338` | 15,870,000.00 USD | 0.00 USD | 1,690.00 USD | `-57.45%` | `50,000.00` |
| `Live` | `Long` | `0.0338` | 15,870,000.00 USD | 0.00 USD | 16,930.00 USD | `-57.33%` | `500,000.00` |
| `Live` | `Long` | `0.0350` | 15,860,000.00 USD | 0.00 USD | 33,300.00 USD | `-55.81%` | `950,000.00` |
| `Live` | `Long` | `0.0352` | 15,820,000.00 USD | 0.00 USD | 210.51 USD | `-55.69%` | `5,989.00` |
| `Live` | `Long` | `0.0357` | 15,820,000.00 USD | 0.00 USD | 4,370.00 USD | `-54.93%` | `122,306.00` |
| `Live` | `Long` | `0.0358` | 15,820,000.00 USD | 0.00 USD | 214.53 USD | `-54.81%` | `5,984.00` |
| `Live` | `Long` | `0.0362` | 15,820,000.00 USD | 0.00 USD | 774,500.00 USD | `-54.43%` | `21,424,497.00` |
| `Live` | `Long` | `0.0365` | 15,040,000.00 USD | 0.00 USD | 195.51 USD | `-53.92%` | `5,349.00` |
| `Live` | `Long` | `0.0372` | 15,040,000.00 USD | 0.00 USD | 3,350.00 USD | `-53.04%` | `90,000.00` |
| `Live` | `Long` | `0.0376` | 15,040,000.00 USD | 0.00 USD | 77,600.00 USD | `-52.66%` | `2,066,606.00` |
| `Live` | `Long` | `0.0377` | 14,960,000.00 USD | 0.00 USD | 3,810.00 USD | `-52.54%` | `101,126.00` |
| `Live` | `Long` | `0.0379` | 14,960,000.00 USD | 0.00 USD | 1,030.00 USD | `-52.16%` | `27,061.00` |
| `Live` | `Long` | `0.0381` | 14,960,000.00 USD | 0.00 USD | 246.45 USD | `-52.03%` | `6,477.00` |
| `Live` | `Long` | `0.0386` | 14,960,000.00 USD | 0.00 USD | 121.74 USD | `-51.40%` | `3,158.00` |
| `Live` | `Long` | `0.0391` | 14,960,000.00 USD | 0.00 USD | 1,000.00 USD | `-50.77%` | `25,729.00` |
| `Live` | `Long` | `0.0391` | 14,960,000.00 USD | 0.00 USD | 1,050.00 USD | `-50.65%` | `26,900.00` |
| `Live` | `Long` | `0.0393` | 14,960,000.00 USD | 0.00 USD | 221.10 USD | `-50.52%` | `5,633.00` |
| `Live` | `Long` | `0.0398` | 14,960,000.00 USD | 0.00 USD | 103,180.00 USD | `-49.76%` | `2,589,112.00` |
| `Live` | `Long` | `0.0403` | 14,850,000.00 USD | 0.00 USD | 30,260.00 USD | `-49.13%` | `750,000.00` |
| `Live` | `Long` | `0.0404` | 14,820,000.00 USD | 0.00 USD | 115.12 USD | `-49.01%` | `2,846.00` |
| `Live` | `Long` | `0.0408` | 14,820,000.00 USD | 0.00 USD | 419.28 USD | `-48.63%` | `10,289.00` |
| `Live` | `Long` | `0.0411` | 14,820,000.00 USD | 0.00 USD | 2,800.00 USD | `-48.25%` | `68,212.00` |
| `Live` | `Long` | `0.0415` | 14,820,000.00 USD | 0.00 USD | 1,030.00 USD | `-47.62%` | `24,809.00` |
| `Live` | `Long` | `0.0420` | 14,820,000.00 USD | 0.00 USD | 266.05 USD | `-47.12%` | `6,342.00` |
| `Live` | `Long` | `0.0420` | 14,820,000.00 USD | 0.00 USD | 59,100.00 USD | `-46.99%` | `1,405,488.00` |
| `Live` | `Long` | `0.0423` | 14,760,000.00 USD | 0.00 USD | 2,090.00 USD | `-46.74%` | `49,468.00` |
| `Live` | `Long` | `0.0423` | 14,760,000.00 USD | 0.00 USD | 267.52 USD | `-46.61%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 14,760,000.00 USD | 0.00 USD | 1,740.00 USD | `-46.49%` | `40,941.00` |
| `Live` | `Long` | `0.0425` | 14,750,000.00 USD | 0.00 USD | 2,080.00 USD | `-46.36%` | `48,797.00` |
| `Live` | `Long` | `0.0427` | 14,750,000.00 USD | 0.00 USD | 7,270.00 USD | `-46.23%` | `170,531.00` |
| `Live` | `Long` | `0.0428` | 14,740,000.00 USD | 0.00 USD | 2,150.00 USD | `-45.98%` | `50,080.00` |
| `Live` | `Long` | `0.0430` | 14,740,000.00 USD | 0.00 USD | 859.00 USD | `-45.86%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 14,740,000.00 USD | 0.00 USD | 6,430.00 USD | `-45.48%` | `148,704.00` |
| `Live` | `Long` | `0.0433` | 14,740,000.00 USD | 0.00 USD | 2,450.00 USD | `-45.35%` | `56,456.00` |
| `Live` | `Long` | `0.0439` | 14,730,000.00 USD | 0.00 USD | 3,810.00 USD | `-44.72%` | `86,807.00` |
| `Live` | `Long` | `0.0440` | 14,730,000.00 USD | 0.00 USD | 750.58 USD | `-44.60%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 14,730,000.00 USD | 0.00 USD | 1,060.00 USD | `-44.47%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 14,730,000.00 USD | 0.00 USD | 101,440.00 USD | `-44.09%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 14,630,000.00 USD | 0.00 USD | 444.76 USD | `-43.71%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 14,630,000.00 USD | 0.00 USD | 248.63 USD | `-43.59%` | `5,556.00` |
| `Live` | `Long` | `0.0454` | 14,620,000.00 USD | 0.00 USD | 2,170.00 USD | `-42.70%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,620,000.00 USD | 0.00 USD | 32,650.00 USD | `-42.58%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,590,000.00 USD | 0.00 USD | 5,470.00 USD | `-42.33%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 14,580,000.00 USD | 0.00 USD | 4,500.00 USD | `-41.95%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 14,580,000.00 USD | 0.00 USD | 114.36 USD | `-41.82%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 14,580,000.00 USD | 0.00 USD | 362.87 USD | `-41.57%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 14,580,000.00 USD | 0.00 USD | 16,780.00 USD | `-41.44%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,560,000.00 USD | 0.00 USD | 2,000.00 USD | `-41.32%` | `43,069.00` |
| `Live` | `Long` | `0.0466` | 14,560,000.00 USD | 0.00 USD | 109.49 USD | `-41.19%` | `2,347.00` |
| `Live` | `Long` | `0.0469` | 14,560,000.00 USD | 0.00 USD | 15,210.00 USD | `-40.94%` | `324,759.00` |
| `Live` | `Long` | `0.0473` | 14,550,000.00 USD | 0.00 USD | 3,010.00 USD | `-40.43%` | `63,783.00` |
| `Live` | `Long` | `0.0474` | 14,540,000.00 USD | 0.00 USD | 593.13 USD | `-40.18%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 14,540,000.00 USD | 0.00 USD | 105.02 USD | `-39.93%` | `2,204.00` |
| `Live` | `Long` | `0.0478` | 14,540,000.00 USD | 0.00 USD | 298.34 USD | `-39.80%` | `6,248.00` |
| `Live` | `Long` | `0.0481` | 14,540,000.00 USD | 0.00 USD | 56,440.00 USD | `-39.43%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,480,000.00 USD | 0.00 USD | 2,500.00 USD | `-39.30%` | `51,918.00` |
| `Live` | `Long` | `0.0483` | 14,480,000.00 USD | 0.00 USD | 2,280.00 USD | `-39.05%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 14,480,000.00 USD | 0.00 USD | 1,480.00 USD | `-38.92%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 14,480,000.00 USD | 0.00 USD | 1,280.00 USD | `-38.42%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,480,000.00 USD | 0.00 USD | 5,470.00 USD | `-38.29%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,470,000.00 USD | 0.00 USD | 1,080.00 USD | `-38.17%` | `21,989.00` |
| `Live` | `Long` | `0.0495` | 14,470,000.00 USD | 0.00 USD | 18,690.00 USD | `-37.54%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,450,000.00 USD | 0.00 USD | 253.82 USD | `-37.28%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,450,000.00 USD | 0.00 USD | 826.08 USD | `-36.91%` | `16,505.00` |
| `Live` | `Long` | `0.0503` | 14,450,000.00 USD | 0.00 USD | 5,410.00 USD | `-36.65%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,450,000.00 USD | 0.00 USD | 1,710.00 USD | `-36.53%` | `34,056.00` |
| `Live` | `Long` | `0.0505` | 14,440,000.00 USD | 0.00 USD | 334.89 USD | `-36.40%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,440,000.00 USD | 0.00 USD | 1,040.00 USD | `-36.15%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,440,000.00 USD | 0.00 USD | 5,350.00 USD | `-36.02%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,440,000.00 USD | 0.00 USD | 535.43 USD | `-35.77%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,440,000.00 USD | 0.00 USD | 566.65 USD | `-35.64%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,440,000.00 USD | 0.00 USD | 11,000.00 USD | `-35.52%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,430,000.00 USD | 0.00 USD | 1,490.00 USD | `-35.39%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,420,000.00 USD | 0.00 USD | 385.13 USD | `-35.27%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,420,000.00 USD | 0.00 USD | 980.43 USD | `-35.14%` | `19,056.00` |
| `Live` | `Long` | `0.0517` | 14,420,000.00 USD | 0.00 USD | 1,200.00 USD | `-34.76%` | `23,207.00` |
| `Live` | `Long` | `0.0520` | 14,420,000.00 USD | 0.00 USD | 277.72 USD | `-34.51%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,420,000.00 USD | 0.00 USD | 4,290.00 USD | `-34.38%` | `82,410.00` |
| `Live` | `Long` | `0.0522` | 14,420,000.00 USD | 0.00 USD | 275,090.00 USD | `-34.13%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,140,000.00 USD | 0.00 USD | 1,170.00 USD | `-33.88%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,140,000.00 USD | 0.00 USD | 5,640.00 USD | `-33.75%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,130,000.00 USD | 0.00 USD | 395.09 USD | `-33.63%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,130,000.00 USD | 0.00 USD | 2,110.00 USD | `-33.50%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,130,000.00 USD | 0.00 USD | 673.52 USD | `-33.38%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,130,000.00 USD | 0.00 USD | 181,950.00 USD | `-33.25%` | `3,436,227.00` |
| `Live` | `Long` | `0.0532` | 13,950,000.00 USD | 0.00 USD | 8,770.00 USD | `-33.00%` | `165,000.00` |
| `Live` | `Long` | `0.0534` | 13,940,000.00 USD | 0.00 USD | 315,090.00 USD | `-32.62%` | `5,894,979.00` |
| `Live` | `Long` | `0.0536` | 13,630,000.00 USD | 0.00 USD | 942.48 USD | `-32.49%` | `17,600.00` |
| `Live` | `Long` | `0.0539` | 13,620,000.00 USD | 0.00 USD | 53,680.00 USD | `-32.11%` | `996,821.00` |
| `Live` | `Long` | `0.0539` | 13,570,000.00 USD | 0.00 USD | 5,290.00 USD | `-31.99%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,570,000.00 USD | 0.00 USD | 2,290.00 USD | `-31.86%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,560,000.00 USD | 0.00 USD | 13,510.00 USD | `-31.74%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 13,550,000.00 USD | 0.00 USD | 96,530.00 USD | `-31.61%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 13,450,000.00 USD | 0.00 USD | 1,810.00 USD | `-31.36%` | `33,224.00` |
| `Live` | `Long` | `0.0546` | 13,450,000.00 USD | 0.00 USD | 2,510.00 USD | `-31.23%` | `46,004.00` |
| `Live` | `Long` | `0.0546` | 13,450,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.11%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 13,450,000.00 USD | 0.00 USD | 188.07 USD | `-30.98%` | `3,435.00` |
| `Live` | `Long` | `0.0549` | 13,450,000.00 USD | 0.00 USD | 298.32 USD | `-30.73%` | `5,429.00` |
| `Live` | `Long` | `0.0551` | 13,450,000.00 USD | 0.00 USD | 772.30 USD | `-30.60%` | `14,029.00` |
| `Live` | `Long` | `0.0556` | 13,450,000.00 USD | 0.00 USD | 907.02 USD | `-29.97%` | `16,328.00` |
| `Live` | `Long` | `0.0558` | 13,450,000.00 USD | 0.00 USD | 101.07 USD | `-29.72%` | `1,813.00` |
| `Live` | `Long` | `0.0561` | 13,450,000.00 USD | 0.00 USD | 772.62 USD | `-29.22%` | `13,760.00` |
| `Live` | `Long` | `0.0563` | 13,440,000.00 USD | 0.00 USD | 40,620.00 USD | `-29.09%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,400,000.00 USD | 0.00 USD | 351.85 USD | `-28.96%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,400,000.00 USD | 0.00 USD | 131.48 USD | `-28.71%` | `2,325.00` |
| `Live` | `Long` | `0.0566` | 13,400,000.00 USD | 0.00 USD | 1,010.00 USD | `-28.58%` | `17,849.00` |
| `Live` | `Long` | `0.0568` | 13,400,000.00 USD | 0.00 USD | 747.06 USD | `-28.46%` | `13,164.00` |
| `Live` | `Long` | `0.0570` | 13,400,000.00 USD | 0.00 USD | 1,040.00 USD | `-28.21%` | `18,175.00` |
| `Live` | `Long` | `0.0570` | 13,400,000.00 USD | 0.00 USD | 8,350.00 USD | `-28.08%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,390,000.00 USD | 0.00 USD | 644.99 USD | `-27.95%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,390,000.00 USD | 0.00 USD | 3,910.00 USD | `-27.70%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,390,000.00 USD | 0.00 USD | 3,590.00 USD | `-27.45%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 13,380,000.00 USD | 0.00 USD | 10,600.00 USD | `-27.32%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,370,000.00 USD | 0.00 USD | 14,210.00 USD | `-27.20%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,360,000.00 USD | 0.00 USD | 3,940.00 USD | `-27.07%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,360,000.00 USD | 0.00 USD | 5,730,000.00 USD | `-26.82%` | `98,673,851.00` |
| `Live` | `Long` | `0.0582` | 7,630,000.00 USD | 0.00 USD | 4,160.00 USD | `-26.69%` | `71,463.00` |
| `Live` | `Long` | `0.0583` | 7,620,000.00 USD | 0.00 USD | 116.82 USD | `-26.44%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 7,620,000.00 USD | 0.00 USD | 392.08 USD | `-26.32%` | `6,708.00` |
| `Live` | `Long` | `0.0585` | 7,620,000.00 USD | 0.00 USD | 172.78 USD | `-26.19%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 7,620,000.00 USD | 0.00 USD | 9,120.00 USD | `-25.94%` | `155,271.00` |
| `Live` | `Long` | `0.0590` | 7,610,000.00 USD | 0.00 USD | 212.22 USD | `-25.69%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 7,610,000.00 USD | 0.00 USD | 26,980.00 USD | `-25.43%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 7,590,000.00 USD | 0.00 USD | 889.30 USD | `-25.18%` | `14,984.00` |
| `Live` | `Long` | `0.0595` | 7,590,000.00 USD | 0.00 USD | 3,660.00 USD | `-25.06%` | `61,626.00` |
| `Live` | `Long` | `0.0595` | 7,580,000.00 USD | 0.00 USD | 2,650.00 USD | `-24.93%` | `44,458.00` |
| `Live` | `Long` | `0.0599` | 7,580,000.00 USD | 0.00 USD | 4,560.00 USD | `-24.55%` | `76,220.00` |
| `Live` | `Long` | `0.0600` | 7,570,000.00 USD | 0.00 USD | 380.38 USD | `-24.42%` | `6,345.00` |
| `Live` | `Long` | `0.0600` | 7,570,000.00 USD | 0.00 USD | 18,120.00 USD | `-24.30%` | `301,826.00` |
| `Live` | `Long` | `0.0602` | 7,560,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.17%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 7,550,000.00 USD | 0.00 USD | 548.46 USD | `-23.92%` | `9,088.00` |
| `Live` | `Long` | `0.0604` | 7,550,000.00 USD | 0.00 USD | 23,320.00 USD | `-23.79%` | `385,716.00` |
| `Live` | `Long` | `0.0605` | 7,520,000.00 USD | 0.00 USD | 32,830.00 USD | `-23.67%` | `542,170.00` |
| `Live` | `Long` | `0.0607` | 7,490,000.00 USD | 0.00 USD | 1,220.00 USD | `-23.42%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,490,000.00 USD | 0.00 USD | 1,490.00 USD | `-23.29%` | `24,429.00` |
| `Live` | `Long` | `0.0609` | 7,490,000.00 USD | 0.00 USD | 2,220.00 USD | `-23.16%` | `36,478.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 913.21 USD | `-22.91%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 298.17 USD | `-22.79%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,480,000.00 USD | 0.00 USD | 655.16 USD | `-22.66%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,480,000.00 USD | 0.00 USD | 1,400.00 USD | `-22.41%` | `22,725.00` |
| `Live` | `Long` | `0.0617` | 7,480,000.00 USD | 0.00 USD | 13,460.00 USD | `-22.28%` | `218,374.00` |
| `Live` | `Long` | `0.0617` | 7,470,000.00 USD | 0.00 USD | 528.46 USD | `-22.16%` | `8,558.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 26,790.00 USD | `-21.78%` | `431,787.00` |
| `Live` | `Long` | `0.0622` | 7,440,000.00 USD | 0.00 USD | 1,820.00 USD | `-21.53%` | `29,227.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 1,900.00 USD | `-21.40%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 3,470.00 USD | `-21.27%` | `55,505.00` |
| `Live` | `Long` | `0.0625` | 7,430,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-21.15%` | `17,645,727.00` |
| `Live` | `Long` | `0.0626` | 6,330,000.00 USD | 0.00 USD | 168.28 USD | `-21.02%` | `2,686.00` |
| `Live` | `Long` | `0.0628` | 6,330,000.00 USD | 0.00 USD | 461.78 USD | `-20.90%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,330,000.00 USD | 0.00 USD | 6,400.00 USD | `-20.77%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 3,750.00 USD | `-20.64%` | `59,614.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 3,080.00 USD | `-20.52%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,320,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-20.39%` | `16,854,659.00` |
| `Live` | `Long` | `0.0633` | 5,250,000.00 USD | 0.00 USD | 1,470.00 USD | `-20.26%` | `23,227.00` |
| `Live` | `Long` | `0.0634` | 5,250,000.00 USD | 0.00 USD | 12,660.00 USD | `-20.14%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 5,240,000.00 USD | 0.00 USD | 1,690.00 USD | `-20.01%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,240,000.00 USD | 0.00 USD | 280.95 USD | `-19.89%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,240,000.00 USD | 0.00 USD | 32,500.00 USD | `-19.76%` | `510,677.00` |
| `Live` | `Long` | `0.0638` | 5,200,000.00 USD | 0.00 USD | 8,670.00 USD | `-19.63%` | `136,018.00` |
| `Live` | `Long` | `0.0639` | 5,200,000.00 USD | 0.00 USD | 23,220.00 USD | `-19.51%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,170,000.00 USD | 0.00 USD | 1,360.00 USD | `-19.38%` | `21,194.00` |
| `Live` | `Long` | `0.0641` | 5,170,000.00 USD | 0.00 USD | 633.29 USD | `-19.13%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,170,000.00 USD | 0.00 USD | 9,150.00 USD | `-19.00%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,160,000.00 USD | 0.00 USD | 2,170.00 USD | `-18.88%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,160,000.00 USD | 0.00 USD | 23,050.00 USD | `-18.75%` | `357,682.00` |
| `Live` | `Long` | `0.0646` | 5,140,000.00 USD | 0.00 USD | 3,520.00 USD | `-18.50%` | `54,442.00` |
| `Live` | `Long` | `0.0648` | 5,130,000.00 USD | 0.00 USD | 87,470.00 USD | `-18.37%` | `1,350,935.00` |
| `Live` | `Long` | `0.0649` | 5,040,000.00 USD | 0.00 USD | 9,910.00 USD | `-18.25%` | `152,854.00` |
| `Live` | `Long` | `0.0649` | 5,040,000.00 USD | 0.00 USD | 21,910.00 USD | `-18.12%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 5,010,000.00 USD | 0.00 USD | 2,380.00 USD | `-17.87%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 5,010,000.00 USD | 0.00 USD | 13,770.00 USD | `-17.74%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 5,000,000.00 USD | 0.00 USD | 7,430.00 USD | `-17.62%` | `113,620.00` |
| `Live` | `Long` | `0.0655` | 4,990,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.37%` | `81,453.00` |
| `Live` | `Long` | `0.0657` | 4,980,000.00 USD | 0.00 USD | 20,790.00 USD | `-17.24%` | `316,670.00` |
| `Live` | `Long` | `0.0658` | 4,960,000.00 USD | 0.00 USD | 71,100.00 USD | `-17.11%` | `1,081,348.00` |
| `Live` | `Long` | `0.0659` | 4,890,000.00 USD | 0.00 USD | 14,600.00 USD | `-16.99%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,880,000.00 USD | 0.00 USD | 11,990.00 USD | `-16.86%` | `181,801.00` |
| `Live` | `Long` | `0.0662` | 4,870,000.00 USD | 0.00 USD | 23,130.00 USD | `-16.61%` | `349,643.00` |
| `Live` | `Long` | `0.0663` | 4,840,000.00 USD | 0.00 USD | 1,630.00 USD | `-16.48%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,840,000.00 USD | 0.00 USD | 27,600.00 USD | `-16.36%` | `415,904.00` |
| `Live` | `Long` | `0.0664` | 4,810,000.00 USD | 0.00 USD | 1,030.00 USD | `-16.23%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,810,000.00 USD | 0.00 USD | 66,550.00 USD | `-16.10%` | `1,000,000.00` |
| `Live` | `Long` | `0.0667` | 4,750,000.00 USD | 0.00 USD | 34,860.00 USD | `-15.98%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,710,000.00 USD | 0.00 USD | 1,490.00 USD | `-15.85%` | `22,334.00` |
| `Live` | `Long` | `0.0669` | 4,710,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-15.73%` | `15,230,102.00` |
| `Live` | `Long` | `0.0669` | 3,690,000.00 USD | 0.00 USD | 389.18 USD | `-15.60%` | `5,813.00` |
| `Live` | `Long` | `0.0670` | 3,690,000.00 USD | 0.00 USD | 9,630.00 USD | `-15.47%` | `143,575.00` |
| `Live` | `Long` | `0.0672` | 3,680,000.00 USD | 0.00 USD | 899.27 USD | `-15.35%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 196.64 USD | `-15.22%` | `2,924.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 96,360.00 USD | `-15.10%` | `1,430,733.00` |
| `Live` | `Long` | `0.0674` | 3,580,000.00 USD | 0.00 USD | 2,070.00 USD | `-14.97%` | `30,756.00` |
| `Live` | `Long` | `0.0675` | 3,580,000.00 USD | 0.00 USD | 310.73 USD | `-14.84%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,580,000.00 USD | 0.00 USD | 8,210.00 USD | `-14.72%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,570,000.00 USD | 0.00 USD | 5,100.00 USD | `-14.59%` | `75,221.00` |
| `Live` | `Long` | `0.0678` | 3,570,000.00 USD | 0.00 USD | 55,180.00 USD | `-14.47%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,510,000.00 USD | 0.00 USD | 20,030.00 USD | `-14.34%` | `294,729.00` |
| `Live` | `Long` | `0.0680` | 3,490,000.00 USD | 0.00 USD | 212.72 USD | `-14.21%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,490,000.00 USD | 0.00 USD | 1,680.00 USD | `-14.09%` | `24,721.00` |
| `Live` | `Long` | `0.0683` | 3,490,000.00 USD | 0.00 USD | 6,220.00 USD | `-13.96%` | `91,110.00` |
| `Live` | `Long` | `0.0683` | 3,480,000.00 USD | 0.00 USD | 1,290.00 USD | `-13.84%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,480,000.00 USD | 0.00 USD | 6,000.00 USD | `-13.71%` | `87,593.00` |
| `Live` | `Long` | `0.0685` | 3,480,000.00 USD | 0.00 USD | 7,740.00 USD | `-13.58%` | `112,887.00` |
| `Live` | `Long` | `0.0687` | 3,470,000.00 USD | 0.00 USD | 1,410.00 USD | `-13.46%` | `20,568.00` |
| `Live` | `Long` | `0.0688` | 3,470,000.00 USD | 0.00 USD | 69,020.00 USD | `-13.33%` | `1,003,929.00` |
| `Live` | `Long` | `0.0688` | 3,400,000.00 USD | 0.00 USD | 517.48 USD | `-13.21%` | `7,516.00` |
| `Live` | `Long` | `0.0689` | 3,400,000.00 USD | 0.00 USD | 507,660.00 USD | `-13.08%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,890,000.00 USD | 0.00 USD | 3,670.00 USD | `-12.95%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,890,000.00 USD | 0.00 USD | 8,350.00 USD | `-12.83%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,880,000.00 USD | 0.00 USD | 52,390.00 USD | `-12.57%` | `755,504.00` |
| `Live` | `Long` | `0.0694` | 2,830,000.00 USD | 0.00 USD | 4,840.00 USD | `-12.45%` | `69,669.00` |
| `Live` | `Long` | `0.0696` | 2,820,000.00 USD | 0.00 USD | 15,100.00 USD | `-12.32%` | `217,157.00` |
| `Live` | `Long` | `0.0697` | 2,810,000.00 USD | 0.00 USD | 5,240.00 USD | `-12.20%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,800,000.00 USD | 0.00 USD | 3,420.00 USD | `-12.07%` | `49,047.00` |
| `Live` | `Long` | `0.0698` | 2,800,000.00 USD | 0.00 USD | 3,630.00 USD | `-11.94%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,790,000.00 USD | 0.00 USD | 9,500.00 USD | `-11.82%` | `135,877.00` |
| `Live` | `Long` | `0.0701` | 2,790,000.00 USD | 0.00 USD | 264.58 USD | `-11.69%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,780,000.00 USD | 0.00 USD | 1,590.00 USD | `-11.57%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,780,000.00 USD | 0.00 USD | 2,000.00 USD | `-11.44%` | `28,486.00` |
| `Live` | `Long` | `0.0703` | 2,780,000.00 USD | 0.00 USD | 5,060.00 USD | `-11.31%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,780,000.00 USD | 0.00 USD | 216.56 USD | `-11.19%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,780,000.00 USD | 0.00 USD | 93,740.00 USD | `-10.94%` | `1,326,872.00` |
| `Live` | `Long` | `0.0707` | 2,680,000.00 USD | 0.00 USD | 93,520.00 USD | `-10.81%` | `1,321,767.00` |
| `Live` | `Long` | `0.0712` | 2,590,000.00 USD | 0.00 USD | 389.38 USD | `-10.18%` | `5,465.00` |
| `Live` | `Long` | `0.0713` | 2,590,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-10.05%` | `24,460,119.00` |
| `Live` | `Long` | `0.0714` | 843,020.00 USD | 0.00 USD | 2,220.00 USD | `-9.93%` | `31,003.00` |
| `Live` | `Long` | `0.0716` | 840,810.00 USD | 0.00 USD | 8,230.00 USD | `-9.80%` | `114,992.00` |
| `Live` | `Long` | `0.0717` | 832,580.00 USD | 0.00 USD | 2,780.00 USD | `-9.68%` | `38,828.00` |
| `Live` | `Long` | `0.0717` | 829,800.00 USD | 0.00 USD | 1,520.00 USD | `-9.55%` | `21,127.00` |
| `Live` | `Long` | `0.0718` | 828,280.00 USD | 0.00 USD | 10,850.00 USD | `-9.42%` | `151,060.00` |
| `Live` | `Long` | `0.0720` | 817,430.00 USD | 0.00 USD | 778.93 USD | `-9.30%` | `10,826.00` |
| `Live` | `Long` | `0.0721` | 816,650.00 USD | 0.00 USD | 23,870.00 USD | `-9.17%` | `331,347.00` |
| `Live` | `Long` | `0.0722` | 792,770.00 USD | 0.00 USD | 10,450.00 USD | `-8.92%` | `144,576.00` |
| `Live` | `Long` | `0.0723` | 782,330.00 USD | 0.00 USD | 163.73 USD | `-8.79%` | `2,263.00` |
| `Live` | `Long` | `0.0725` | 782,170.00 USD | 0.00 USD | 87,670.00 USD | `-8.67%` | `1,210,106.00` |
| `Live` | `Long` | `0.0726` | 694,490.00 USD | 0.00 USD | 260.74 USD | `-8.54%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 694,230.00 USD | 0.00 USD | 948.37 USD | `-8.41%` | `13,054.00` |
| `Live` | `Long` | `0.0727` | 693,280.00 USD | 0.00 USD | 3,170.00 USD | `-8.29%` | `43,539.00` |
| `Live` | `Long` | `0.0728` | 690,120.00 USD | 0.00 USD | 646.11 USD | `-8.16%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 689,470.00 USD | 0.00 USD | 76,420.00 USD | `-8.04%` | `1,047,551.00` |
| `Live` | `Long` | `0.0731` | 613,050.00 USD | 0.00 USD | 10,300.00 USD | `-7.91%` | `141,047.00` |
| `Live` | `Long` | `0.0732` | 602,750.00 USD | 0.00 USD | 1,930.00 USD | `-7.78%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 600,820.00 USD | 0.00 USD | 5,410.00 USD | `-7.66%` | `73,796.00` |
| `Live` | `Long` | `0.0735` | 595,420.00 USD | 0.00 USD | 7,000.00 USD | `-7.41%` | `95,360.00` |
| `Live` | `Long` | `0.0736` | 588,410.00 USD | 0.00 USD | 4,060.00 USD | `-7.28%` | `55,170.00` |
| `Live` | `Long` | `0.0736` | 584,350.00 USD | 0.00 USD | 5,490.00 USD | `-7.15%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 578,860.00 USD | 0.00 USD | 10,390.00 USD | `-7.03%` | `140,949.00` |
| `Live` | `Long` | `0.0738` | 568,470.00 USD | 0.00 USD | 5,430.00 USD | `-6.90%` | `73,561.00` |
| `Live` | `Long` | `0.0740` | 563,030.00 USD | 0.00 USD | 15,010.00 USD | `-6.78%` | `202,965.00` |
| `Live` | `Long` | `0.0741` | 548,020.00 USD | 0.00 USD | 463,970.00 USD | `-6.65%` | `6,265,674.00` |
| `Live` | `Long` | `0.0741` | 84,050.00 USD | 0.00 USD | 777.39 USD | `-6.52%` | `10,484.00` |
| `Live` | `Long` | `0.0742` | 83,270.00 USD | 0.00 USD | 1,280.00 USD | `-6.40%` | `17,202.00` |
| `Live` | `Long` | `0.0743` | 82,000.00 USD | 0.00 USD | 2,140.00 USD | `-6.27%` | `28,845.00` |
| `Live` | `Long` | `0.0745` | 79,850.00 USD | 0.00 USD | 2,040.00 USD | `-6.15%` | `27,364.00` |
| `Live` | `Long` | `0.0746` | 77,810.00 USD | 0.00 USD | 1,420.00 USD | `-6.02%` | `19,020.00` |
| `Live` | `Long` | `0.0746` | 76,400.00 USD | 0.00 USD | 1,050.00 USD | `-5.89%` | `14,085.00` |
| `Live` | `Long` | `0.0747` | 75,340.00 USD | 0.00 USD | 359.77 USD | `-5.77%` | `4,813.00` |
| `Live` | `Long` | `0.0750` | 74,980.00 USD | 0.00 USD | 1,370.00 USD | `-5.52%` | `18,241.00` |
| `Live` | `Long` | `0.0751` | 73,620.00 USD | 0.00 USD | 451.13 USD | `-5.39%` | `6,011.00` |
| `Live` | `Long` | `0.0751` | 73,170.00 USD | 0.00 USD | 1,480.00 USD | `-5.26%` | `19,691.00` |
| `Live` | `Long` | `0.0752` | 71,690.00 USD | 0.00 USD | 3,910.00 USD | `-5.14%` | `51,995.00` |
| `Live` | `Long` | `0.0754` | 67,770.00 USD | 0.00 USD | 208.64 USD | `-5.01%` | `2,769.00` |
| `Live` | `Long` | `0.0755` | 67,570.00 USD | 0.00 USD | 4,060.00 USD | `-4.88%` | `53,747.00` |
| `Live` | `Long` | `0.0756` | 63,510.00 USD | 0.00 USD | 977.84 USD | `-4.76%` | `12,943.00` |
| `Live` | `Long` | `0.0756` | 62,530.00 USD | 0.00 USD | 516.61 USD | `-4.63%` | `6,829.00` |
| `Live` | `Long` | `0.0757` | 62,020.00 USD | 0.00 USD | 3,270.00 USD | `-4.51%` | `43,197.00` |
| `Live` | `Long` | `0.0759` | 58,740.00 USD | 0.00 USD | 5,070.00 USD | `-4.38%` | `66,803.00` |
| `Live` | `Long` | `0.0760` | 53,680.00 USD | 0.00 USD | 32,080.00 USD | `-4.25%` | `422,343.00` |
| `Live` | `Long` | `0.0761` | 21,600.00 USD | 0.00 USD | 1,690.00 USD | `-4.13%` | `22,243.00` |
| `Live` | `Long` | `0.0761` | 19,910.00 USD | 0.00 USD | 190.38 USD | `-4.00%` | `2,500.00` |
| `Live` | `Long` | `0.0762` | 19,720.00 USD | 0.00 USD | 181.93 USD | `-3.88%` | `2,386.00` |
| `Live` | `Long` | `0.0764` | 19,540.00 USD | 0.00 USD | 11,510.00 USD | `-3.75%` | `150,696.00` |
| `Live` | `Long` | `0.0791` | 8,030.00 USD | 0.00 USD | 8,030.00 USD | `-0.22%` | `101,457.00` |
| `Live` | `Short` | `0.0818` | 710.08 USD | 710.08 USD | 0.00 USD | `+3.06%` | `8,686.00` |
| `Live` | `Short` | `0.0832` | 12,040.00 USD | 11,330.00 USD | 0.00 USD | `+4.82%` | `136,223.00` |
| `Live` | `Short` | `0.0833` | 12,190.00 USD | 150.95 USD | 0.00 USD | `+5.07%` | `1,811.00` |
| `Live` | `Short` | `0.0837` | 12,480.00 USD | 293.44 USD | 0.00 USD | `+5.45%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 14,050.00 USD | 1,570.00 USD | 0.00 USD | `+5.58%` | `18,767.00` |
| `Live` | `Short` | `0.0839` | 14,160.00 USD | 104.69 USD | 0.00 USD | `+5.83%` | `1,247.00` |
| `Live` | `Short` | `0.0840` | 31,850.00 USD | 17,690.00 USD | 0.00 USD | `+5.96%` | `210,521.00` |
| `Live` | `Short` | `0.0843` | 31,960.00 USD | 104.72 USD | 0.00 USD | `+6.21%` | `1,243.00` |
| `Live` | `Short` | `0.0847` | 32,170.00 USD | 213.74 USD | 0.00 USD | `+6.71%` | `2,525.00` |
| `Live` | `Short` | `0.0851` | 32,390.00 USD | 214.75 USD | 0.00 USD | `+7.22%` | `2,525.00` |
| `Live` | `Short` | `0.0858` | 32,500.00 USD | 115.30 USD | 0.00 USD | `+8.23%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 32,640.00 USD | 135.37 USD | 0.00 USD | `+8.35%` | `1,575.00` |
| `Live` | `Short` | `0.0862` | 32,850.00 USD | 216.58 USD | 0.00 USD | `+8.60%` | `2,514.00` |
| `Live` | `Short` | `0.0862` | 35,200.00 USD | 2,340.00 USD | 0.00 USD | `+8.73%` | `27,165.00` |
| `Live` | `Short` | `0.0876` | 44,820.00 USD | 9,620.00 USD | 0.00 USD | `+10.37%` | `109,908.00` |
| `Live` | `Short` | `0.0881` | 45,280.00 USD | 465.17 USD | 0.00 USD | `+11.00%` | `5,283.00` |
| `Live` | `Short` | `0.0882` | 45,390.00 USD | 104.90 USD | 0.00 USD | `+11.13%` | `1,190.00` |
| `Live` | `Short` | `0.0887` | 45,800.00 USD | 411.53 USD | 0.00 USD | `+11.88%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 46,220.00 USD | 418.80 USD | 0.00 USD | `+12.26%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 46,500.00 USD | 285.70 USD | 0.00 USD | `+12.76%` | `3,194.00` |
| `Live` | `Short` | `0.0896` | 52,560.00 USD | 6,050.00 USD | 0.00 USD | `+13.02%` | `67,505.00` |
| `Live` | `Short` | `0.0900` | 52,780.00 USD | 226.85 USD | 0.00 USD | `+13.39%` | `2,522.00` |
| `Live` | `Short` | `0.0907` | 60,380.00 USD | 7,590.00 USD | 0.00 USD | `+14.40%` | `83,669.00` |
| `Live` | `Short` | `0.0909` | 61,260.00 USD | 884.52 USD | 0.00 USD | `+14.53%` | `9,736.00` |
| `Live` | `Short` | `0.0910` | 61,370.00 USD | 114.23 USD | 0.00 USD | `+14.65%` | `1,256.00` |
| `Live` | `Short` | `0.0911` | 62,120.00 USD | 743.15 USD | 0.00 USD | `+14.91%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 66,160.00 USD | 4,040.00 USD | 0.00 USD | `+15.03%` | `44,324.00` |
| `Live` | `Short` | `0.0914` | 66,330.00 USD | 171.19 USD | 0.00 USD | `+15.16%` | `1,874.00` |
| `Live` | `Short` | `0.0917` | 66,680.00 USD | 344.43 USD | 0.00 USD | `+15.66%` | `3,754.00` |
| `Live` | `Short` | `0.0921` | 66,850.00 USD | 171.49 USD | 0.00 USD | `+16.04%` | `1,863.00` |
| `Live` | `Short` | `0.0925` | 67,040.00 USD | 188.14 USD | 0.00 USD | `+16.55%` | `2,035.00` |
| `Live` | `Short` | `0.0935` | 70,340.00 USD | 3,300.00 USD | 0.00 USD | `+17.81%` | `35,291.00` |
| `Live` | `Short` | `0.0949` | 70,910.00 USD | 573.84 USD | 0.00 USD | `+19.57%` | `6,050.00` |
| `Live` | `Short` | `0.0950` | 84,710.00 USD | 13,800.00 USD | 0.00 USD | `+19.70%` | `145,305.00` |
| `Live` | `Short` | `0.0951` | 198,890.00 USD | 114,180.00 USD | 0.00 USD | `+19.95%` | `1,200,000.00` |
| `Live` | `Short` | `0.0959` | 199,630.00 USD | 747.55 USD | 0.00 USD | `+20.96%` | `7,791.00` |
| `Live` | `Short` | `0.0961` | 200,240.00 USD | 609.59 USD | 0.00 USD | `+21.21%` | `6,340.00` |
| `Live` | `Short` | `0.0964` | 248,470.00 USD | 48,230.00 USD | 0.00 USD | `+21.59%` | `500,000.00` |
| `Live` | `Short` | `0.0979` | 287,660.00 USD | 39,190.00 USD | 0.00 USD | `+23.35%` | `400,522.00` |
| `Live` | `Short` | `0.0983` | 288,140.00 USD | 477.50 USD | 0.00 USD | `+23.86%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 298,650.00 USD | 10,510.00 USD | 0.00 USD | `+24.11%` | `106,785.00` |
| `Live` | `Short` | `0.1004` | 299,940.00 USD | 1,290.00 USD | 0.00 USD | `+26.63%` | `12,841.00` |
| `Live` | `Short` | `0.1007` | 300,950.00 USD | 1,010.00 USD | 0.00 USD | `+26.88%` | `10,000.00` |
| `Live` | `Short` | `0.1013` | 301,120.00 USD | 177.90 USD | 0.00 USD | `+27.64%` | `1,757.00` |
| `Live` | `Short` | `0.1014` | 308,750.00 USD | 7,630.00 USD | 0.00 USD | `+27.89%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 311,720.00 USD | 2,970.00 USD | 0.00 USD | `+28.14%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 312,210.00 USD | 492.85 USD | 0.00 USD | `+28.40%` | `4,839.00` |
| `Live` | `Short` | `0.1047` | 313,240.00 USD | 1,030.00 USD | 0.00 USD | `+32.05%` | `9,849.00` |
| `Live` | `Short` | `0.1061` | 319,350.00 USD | 6,110.00 USD | 0.00 USD | `+33.82%` | `57,554.00` |
| `Live` | `Short` | `0.1075` | 322,570.00 USD | 3,220.00 USD | 0.00 USD | `+35.46%` | `29,960.00` |
| `Live` | `Short` | `0.1085` | 325,940.00 USD | 3,370.00 USD | 0.00 USD | `+36.84%` | `31,000.00` |
| `Live` | `Short` | `0.1121` | 328,230.00 USD | 2,290.00 USD | 0.00 USD | `+41.38%` | `20,406.00` |
| `Live` | `Short` | `0.1127` | 328,440.00 USD | 214.15 USD | 0.00 USD | `+42.01%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 330,100.00 USD | 1,660.00 USD | 0.00 USD | `+42.39%` | `14,696.00` |
| `Live` | `Short` | `0.1187` | 330,210.00 USD | 106.19 USD | 0.00 USD | `+49.57%` | `895.00` |
| `Live` | `Short` | `0.1221` | 330,560.00 USD | 355.95 USD | 0.00 USD | `+53.99%` | `2,914.00` |
| `Live` | `Short` | `0.1222` | 331,360.00 USD | 796.83 USD | 0.00 USD | `+54.11%` | `6,518.00` |
| `Live` | `Short` | `0.1250` | 331,730.00 USD | 375.15 USD | 0.00 USD | `+57.64%` | `3,000.00` |
| `Live` | `Short` | `0.1270` | 331,840.00 USD | 108.80 USD | 0.00 USD | `+60.04%` | `857.00` |
| `Live` | `Short` | `0.1288` | 333,400.00 USD | 1,560.00 USD | 0.00 USD | `+62.43%` | `12,089.00` |
| `Live` | `Short` | `0.1293` | 335,760.00 USD | 2,350.00 USD | 0.00 USD | `+63.06%` | `18,202.00` |
| `Live` | `Short` | `0.1296` | 335,930.00 USD | 171.66 USD | 0.00 USD | `+63.44%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 338,070.00 USD | 2,140.00 USD | 0.00 USD | `+65.33%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 338,170.00 USD | 102.97 USD | 0.00 USD | `+66.21%` | `781.00` |
| `Live` | `Short` | `0.1320` | 3,100,000.00 USD | 2,760,000.00 USD | 0.00 USD | `+66.34%` | `20,910,149.00` |
| `Live` | `Short` | `0.1338` | 3,100,000.00 USD | 205.31 USD | 0.00 USD | `+68.61%` | `1,535.00` |
| `Live` | `Short` | `0.1381` | 3,100,000.00 USD | 997.30 USD | 0.00 USD | `+74.16%` | `7,219.00` |
| `Live` | `Short` | `0.1391` | 3,120,000.00 USD | 22,550.00 USD | 0.00 USD | `+75.29%` | `162,180.00` |
| `Live` | `Short` | `0.1404` | 3,120,000.00 USD | 663.63 USD | 0.00 USD | `+77.06%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 3,120,000.00 USD | 1,800.00 USD | 0.00 USD | `+77.94%` | `12,780.00` |
| `Live` | `Short` | `0.1432` | 3,130,000.00 USD | 1,860.00 USD | 0.00 USD | `+80.59%` | `13,010.00` |
| `Live` | `Short` | `0.1459` | 3,130,000.00 USD | 2,340.00 USD | 0.00 USD | `+83.99%` | `16,000.00` |
| `Live` | `Short` | `0.1479` | 3,140,000.00 USD | 8,320.00 USD | 0.00 USD | `+86.39%` | `56,294.00` |
| `Live` | `Short` | `0.1484` | 3,140,000.00 USD | 701.13 USD | 0.00 USD | `+87.14%` | `4,723.00` |
| `Live` | `Short` | `0.1487` | 3,140,000.00 USD | 393.33 USD | 0.00 USD | `+87.39%` | `2,646.00` |
| `Live` | `Short` | `0.1512` | 3,140,000.00 USD | 1,870.00 USD | 0.00 USD | `+90.67%` | `12,354.00` |
| `Live` | `Short` | `0.1515` | 3,140,000.00 USD | 2,010.00 USD | 0.00 USD | `+91.05%` | `13,240.00` |
| `Live` | `Short` | `0.1519` | 3,200,000.00 USD | 56,850.00 USD | 0.00 USD | `+91.43%` | `374,415.00` |
| `Live` | `Short` | `0.1525` | 3,200,000.00 USD | 267.55 USD | 0.00 USD | `+92.18%` | `1,755.00` |
| `Live` | `Short` | `0.1527` | 3,200,000.00 USD | 195.39 USD | 0.00 USD | `+92.44%` | `1,280.00` |
| `Live` | `Short` | `0.1527` | 3,200,000.00 USD | 194.45 USD | 0.00 USD | `+92.56%` | `1,273.00` |
| `Live` | `Short` | `0.1568` | 3,200,000.00 USD | 341.15 USD | 0.00 USD | `+97.73%` | `2,175.00` |
| `Live` | `Short` | `0.1570` | 3,200,000.00 USD | 4,830.00 USD | 0.00 USD | `+97.86%` | `30,755.00` |
| `Live` | `Short` | `0.1570` | 3,200,000.00 USD | 980.15 USD | 0.00 USD | `+97.98%` | `6,241.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 606,610.00 USD | 0.00 USD | 375.42 USD | `-67.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 606,240.00 USD | 0.00 USD | 409.59 USD | `-49.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 605,830.00 USD | 0.00 USD | 132.68 USD | `-48.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 605,700.00 USD | 0.00 USD | 286.87 USD | `-43.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 605,410.00 USD | 0.00 USD | 252.42 USD | `-41.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 605,160.00 USD | 0.00 USD | 468.67 USD | `-40.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 604,690.00 USD | 0.00 USD | 5,160.00 USD | `-38.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 599,530.00 USD | 0.00 USD | 920.48 USD | `-37.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 598,610.00 USD | 0.00 USD | 1,860.00 USD | `-37.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 596,750.00 USD | 0.00 USD | 175.41 USD | `-35.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 596,570.00 USD | 0.00 USD | 1,370.00 USD | `-30.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 595,200.00 USD | 0.00 USD | 437.58 USD | `-29.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 594,760.00 USD | 0.00 USD | 752.54 USD | `-26.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 594,010.00 USD | 0.00 USD | 9,830.00 USD | `-25.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 584,180.00 USD | 0.00 USD | 1,210.00 USD | `-25.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 582,970.00 USD | 0.00 USD | 1,560.00 USD | `-24.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 581,410.00 USD | 0.00 USD | 134.12 USD | `-24.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 581,280.00 USD | 0.00 USD | 8,800.00 USD | `-23.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 572,480.00 USD | 0.00 USD | 504.26 USD | `-22.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 571,970.00 USD | 0.00 USD | 4,200.00 USD | `-21.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 567,770.00 USD | 0.00 USD | 1,280.00 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 566,490.00 USD | 0.00 USD | 920.18 USD | `-19.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 565,570.00 USD | 0.00 USD | 370.79 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 565,200.00 USD | 0.00 USD | 1,130.00 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 564,070.00 USD | 0.00 USD | 362.24 USD | `-17.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 563,710.00 USD | 0.00 USD | 3,140.00 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 560,570.00 USD | 0.00 USD | 1,200.00 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 559,370.00 USD | 0.00 USD | 996.31 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 558,370.00 USD | 0.00 USD | 632.88 USD | `-15.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 557,740.00 USD | 0.00 USD | 115.57 USD | `-15.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 557,630.00 USD | 0.00 USD | 33,620.00 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 524,000.00 USD | 0.00 USD | 12,860.00 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 511,140.00 USD | 0.00 USD | 1,260.00 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 509,880.00 USD | 0.00 USD | 108.08 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 509,770.00 USD | 0.00 USD | 2,960.00 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 506,810.00 USD | 0.00 USD | 1,430.00 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 505,380.00 USD | 0.00 USD | 7,990.00 USD | `-14.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 497,390.00 USD | 0.00 USD | 8,580.00 USD | `-14.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 488,810.00 USD | 0.00 USD | 606.47 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 488,200.00 USD | 0.00 USD | 38,710.00 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 449,500.00 USD | 0.00 USD | 660.06 USD | `-13.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 448,840.00 USD | 0.00 USD | 102.34 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 448,740.00 USD | 0.00 USD | 697.50 USD | `-12.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 448,040.00 USD | 0.00 USD | 699.90 USD | `-11.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 447,340.00 USD | 0.00 USD | 17,020.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 430,320.00 USD | 0.00 USD | 895.27 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 429,420.00 USD | 0.00 USD | 523.23 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 428,900.00 USD | 0.00 USD | 235.12 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 428,660.00 USD | 0.00 USD | 107,230.00 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 321,440.00 USD | 0.00 USD | 12,930.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 308,500.00 USD | 0.00 USD | 20,070.00 USD | `-10.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 288,430.00 USD | 0.00 USD | 233.74 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 288,200.00 USD | 0.00 USD | 16,880.00 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 271,320.00 USD | 0.00 USD | 1,670.00 USD | `-9.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 269,650.00 USD | 0.00 USD | 4,710.00 USD | `-9.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 264,940.00 USD | 0.00 USD | 8,570.00 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 256,370.00 USD | 0.00 USD | 413.42 USD | `-9.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 255,960.00 USD | 0.00 USD | 703.43 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 255,260.00 USD | 0.00 USD | 621.12 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 254,630.00 USD | 0.00 USD | 1,700.00 USD | `-8.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 252,940.00 USD | 0.00 USD | 29,060.00 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 223,870.00 USD | 0.00 USD | 976.95 USD | `-8.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 222,900.00 USD | 0.00 USD | 2,090.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 220,810.00 USD | 0.00 USD | 28,750.00 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 192,060.00 USD | 0.00 USD | 2,710.00 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 189,350.00 USD | 0.00 USD | 115.12 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 189,240.00 USD | 0.00 USD | 4,680.00 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 184,560.00 USD | 0.00 USD | 1,860.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 182,700.00 USD | 0.00 USD | 2,900.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 179,800.00 USD | 0.00 USD | 107.66 USD | `-6.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 179,700.00 USD | 0.00 USD | 5,000.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 174,700.00 USD | 0.00 USD | 1,410.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 173,290.00 USD | 0.00 USD | 375.86 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 172,910.00 USD | 0.00 USD | 193.90 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 172,720.00 USD | 0.00 USD | 140.04 USD | `-5.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 172,580.00 USD | 0.00 USD | 7,100.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 165,480.00 USD | 0.00 USD | 736.17 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 164,740.00 USD | 0.00 USD | 192.73 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 164,550.00 USD | 0.00 USD | 358.13 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 164,190.00 USD | 0.00 USD | 4,880.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 159,310.00 USD | 0.00 USD | 193.49 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 159,120.00 USD | 0.00 USD | 2,280.00 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 156,840.00 USD | 0.00 USD | 3,130.00 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 153,710.00 USD | 0.00 USD | 806.81 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0762` | 152,900.00 USD | 0.00 USD | 359.60 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0764` | 152,540.00 USD | 0.00 USD | 335.56 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0765` | 152,210.00 USD | 0.00 USD | 3,730.00 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 148,470.00 USD | 0.00 USD | 1,130.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 147,340.00 USD | 0.00 USD | 3,540.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0767` | 143,810.00 USD | 0.00 USD | 192.95 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0769` | 143,610.00 USD | 0.00 USD | 297.49 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0770` | 143,310.00 USD | 0.00 USD | 11,510.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0771` | 131,810.00 USD | 0.00 USD | 3,980.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0772` | 127,820.00 USD | 0.00 USD | 4,530.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0774` | 123,290.00 USD | 0.00 USD | 157.18 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 123,140.00 USD | 0.00 USD | 2,450.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 120,690.00 USD | 0.00 USD | 604.81 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0776` | 120,090.00 USD | 0.00 USD | 193.97 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0777` | 119,890.00 USD | 0.00 USD | 41,810.00 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0779` | 78,090.00 USD | 0.00 USD | 41,440.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 36,640.00 USD | 0.00 USD | 3,000.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 33,640.00 USD | 0.00 USD | 2,010.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0781` | 31,630.00 USD | 0.00 USD | 1,350.00 USD | `-1.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0783` | 30,290.00 USD | 0.00 USD | 3,140.00 USD | `-1.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0784` | 27,150.00 USD | 0.00 USD | 4,370.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 22,780.00 USD | 0.00 USD | 573.31 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 22,210.00 USD | 0.00 USD | 589.13 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0786` | 21,620.00 USD | 0.00 USD | 495.57 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0788` | 21,120.00 USD | 0.00 USD | 3,030.00 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0789` | 18,090.00 USD | 0.00 USD | 303.73 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 17,790.00 USD | 0.00 USD | 706.60 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 17,080.00 USD | 0.00 USD | 10,230.00 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0791` | 6,850.00 USD | 0.00 USD | 4,600.00 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0793` | 2,260.00 USD | 0.00 USD | 2,260.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 1,010.00 USD | 1,010.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 1,160.00 USD | 148.25 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 1,410.00 USD | 248.91 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 1,540.00 USD | 125.45 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 1,880.00 USD | 342.85 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 2,200.00 USD | 319.16 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 3,320.00 USD | 1,120.00 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 7,660.00 USD | 4,350.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 8,060.00 USD | 400.91 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 8,260.00 USD | 200.46 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 8,410.00 USD | 141.34 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 9,110.00 USD | 707.08 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 11,370.00 USD | 2,260.00 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 108,150.00 USD | 96,780.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 108,960.00 USD | 807.50 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 111,120.00 USD | 2,160.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 111,540.00 USD | 424.74 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 111,640.00 USD | 101.80 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 113,030.00 USD | 1,380.00 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 113,290.00 USD | 264.63 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 114,730.00 USD | 1,430.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 115,220.00 USD | 492.77 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 116,440.00 USD | 1,220.00 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 119,360.00 USD | 2,920.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 128,720.00 USD | 9,360.00 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 131,730.00 USD | 3,010.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 132,470.00 USD | 740.75 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 133,080.00 USD | 607.58 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 146,870.00 USD | 13,790.00 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 150,860.00 USD | 3,980.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 151,370.00 USD | 512.05 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 152,580.00 USD | 1,220.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 152,970.00 USD | 389.31 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 153,280.00 USD | 303.56 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 153,390.00 USD | 112.89 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 153,770.00 USD | 381.45 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 153,930.00 USD | 155.82 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 154,340.00 USD | 415.83 USD | 0.00 USD | `+4.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 154,690.00 USD | 348.82 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 156,130.00 USD | 1,440.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 156,340.00 USD | 210.88 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,910,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,910,000.00 USD | 3,380.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,910,000.00 USD | 341.34 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,910,000.00 USD | 107.71 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,920,000.00 USD | 2,690.00 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,920,000.00 USD | 1,330.00 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,920,000.00 USD | 219.07 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,920,000.00 USD | 326.97 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,920,000.00 USD | 242.84 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,930,000.00 USD | 10,140.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 1,930,000.00 USD | 152.92 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,960,000.00 USD | 30,370.00 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,960,000.00 USD | 205.59 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,960,000.00 USD | 503.19 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,960,000.00 USD | 307.41 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,960,000.00 USD | 614.09 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,960,000.00 USD | 644.62 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 1,960,000.00 USD | 180.45 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,960,000.00 USD | 2,020.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,010,000.00 USD | 43,760.00 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,010,000.00 USD | 1,080.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,010,000.00 USD | 384.06 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,010,000.00 USD | 1,840.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,010,000.00 USD | 2,760.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,010,000.00 USD | 117.71 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,010,000.00 USD | 111.61 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,010,000.00 USD | 571.18 USD | 0.00 USD | `+11.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,010,000.00 USD | 375.94 USD | 0.00 USD | `+11.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,010,000.00 USD | 627.55 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,010,000.00 USD | 211.04 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,010,000.00 USD | 108.36 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,020,000.00 USD | 543.32 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,020,000.00 USD | 1,820.00 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,020,000.00 USD | 2,080.00 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,040,000.00 USD | 17,680.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,040,000.00 USD | 1,810.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,040,000.00 USD | 1,640.00 USD | 0.00 USD | `+12.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,050,000.00 USD | 5,340.00 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,050,000.00 USD | 1,090.00 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,050,000.00 USD | 224.86 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,070,000.00 USD | 20,540.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,070,000.00 USD | 114.93 USD | 0.00 USD | `+14.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,070,000.00 USD | 840.47 USD | 0.00 USD | `+14.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,070,000.00 USD | 173.36 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,070,000.00 USD | 4,690.00 USD | 0.00 USD | `+15.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,080,000.00 USD | 1,870.00 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,080,000.00 USD | 2,170.00 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,080,000.00 USD | 541.32 USD | 0.00 USD | `+16.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,220,000.00 USD | 137,500.00 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,220,000.00 USD | 691.07 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,220,000.00 USD | 6,250.00 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,240,000.00 USD | 13,480.00 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,240,000.00 USD | 734.82 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,240,000.00 USD | 1,230.00 USD | 0.00 USD | `+17.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,240,000.00 USD | 184.09 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,240,000.00 USD | 1,120.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,240,000.00 USD | 1,860.00 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,240,000.00 USD | 512.15 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,250,000.00 USD | 6,620.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,250,000.00 USD | 404.96 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,250,000.00 USD | 129.85 USD | 0.00 USD | `+20.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,250,000.00 USD | 3,740.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,250,000.00 USD | 2,400.00 USD | 0.00 USD | `+20.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,260,000.00 USD | 409.17 USD | 0.00 USD | `+21.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,260,000.00 USD | 203.74 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,260,000.00 USD | 2,800.00 USD | 0.00 USD | `+22.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,260,000.00 USD | 1,320.00 USD | 0.00 USD | `+22.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,260,000.00 USD | 694.56 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,260,000.00 USD | 940.91 USD | 0.00 USD | `+23.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,260,000.00 USD | 2,980.00 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,260,000.00 USD | 104.99 USD | 0.00 USD | `+24.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,270,000.00 USD | 1,930.00 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,270,000.00 USD | 1,490.00 USD | 0.00 USD | `+25.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,270,000.00 USD | 1,090.00 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,270,000.00 USD | 438.96 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,270,000.00 USD | 973.76 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,380,000.00 USD | 113,580.00 USD | 0.00 USD | `+26.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,380,000.00 USD | 175.59 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,380,000.00 USD | 482.89 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,380,000.00 USD | 201.90 USD | 0.00 USD | `+27.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,390,000.00 USD | 489.46 USD | 0.00 USD | `+27.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,390,000.00 USD | 103.68 USD | 0.00 USD | `+28.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,390,000.00 USD | 203.70 USD | 0.00 USD | `+28.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,390,000.00 USD | 3,810.00 USD | 0.00 USD | `+28.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,400,000.00 USD | 11,200.00 USD | 0.00 USD | `+28.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,400,000.00 USD | 4,330.00 USD | 0.00 USD | `+28.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,400,000.00 USD | 205.50 USD | 0.00 USD | `+29.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,410,000.00 USD | 1,540.00 USD | 0.00 USD | `+29.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,410,000.00 USD | 207.50 USD | 0.00 USD | `+30.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,410,000.00 USD | 813.88 USD | 0.00 USD | `+31.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,430,000.00 USD | 23,160.00 USD | 0.00 USD | `+31.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,430,000.00 USD | 781.51 USD | 0.00 USD | `+31.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,430,000.00 USD | 209.30 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,430,000.00 USD | 1,440.00 USD | 0.00 USD | `+32.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,440,000.00 USD | 5,140.00 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,440,000.00 USD | 585.32 USD | 0.00 USD | `+32.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,440,000.00 USD | 210.90 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,440,000.00 USD | 1,850.00 USD | 0.00 USD | `+33.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,440,000.00 USD | 105.75 USD | 0.00 USD | `+33.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,440,000.00 USD | 3,220.00 USD | 0.00 USD | `+33.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,450,000.00 USD | 1,600.00 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,450,000.00 USD | 212.90 USD | 0.00 USD | `+34.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,450,000.00 USD | 472.63 USD | 0.00 USD | `+34.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,450,000.00 USD | 214.50 USD | 0.00 USD | `+35.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,450,000.00 USD | 1,040.00 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,450,000.00 USD | 136.12 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,450,000.00 USD | 216.10 USD | 0.00 USD | `+36.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,490,000.00 USD | 40,920.00 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,490,000.00 USD | 217.90 USD | 0.00 USD | `+37.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,490,000.00 USD | 219.70 USD | 0.00 USD | `+38.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,500,000.00 USD | 7,920.00 USD | 0.00 USD | `+38.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,500,000.00 USD | 154.22 USD | 0.00 USD | `+39.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,500,000.00 USD | 221.30 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,520,000.00 USD | 24,440.00 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,520,000.00 USD | 223.10 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,530,000.00 USD | 2,120.00 USD | 0.00 USD | `+41.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,530,000.00 USD | 226.30 USD | 0.00 USD | `+42.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,530,000.00 USD | 351.57 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,530,000.00 USD | 950.34 USD | 0.00 USD | `+43.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,530,000.00 USD | 229.50 USD | 0.00 USD | `+44.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,530,000.00 USD | 771.08 USD | 0.00 USD | `+44.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,530,000.00 USD | 230.90 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,530,000.00 USD | 288.18 USD | 0.00 USD | `+45.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,530,000.00 USD | 619.10 USD | 0.00 USD | `+46.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,530,000.00 USD | 1,250.00 USD | 0.00 USD | `+46.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,530,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,530,000.00 USD | 232.30 USD | 0.00 USD | `+46.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,530,000.00 USD | 1,600.00 USD | 0.00 USD | `+47.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,530,000.00 USD | 1,050.00 USD | 0.00 USD | `+47.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,540,000.00 USD | 3,730.00 USD | 0.00 USD | `+47.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,540,000.00 USD | 676.22 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,540,000.00 USD | 648.25 USD | 0.00 USD | `+48.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,540,000.00 USD | 1,510.00 USD | 0.00 USD | `+48.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,540,000.00 USD | 448.52 USD | 0.00 USD | `+49.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,540,000.00 USD | 136.93 USD | 0.00 USD | `+49.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,540,000.00 USD | 433.07 USD | 0.00 USD | `+49.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,540,000.00 USD | 1,050.00 USD | 0.00 USD | `+50.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,540,000.00 USD | 691.80 USD | 0.00 USD | `+50.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,660,000.00 USD | 118,550.00 USD | 0.00 USD | `+51.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,660,000.00 USD | 143.22 USD | 0.00 USD | `+51.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,660,000.00 USD | 803.95 USD | 0.00 USD | `+52.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,660,000.00 USD | 1,380.00 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,670,000.00 USD | 2,270.00 USD | 0.00 USD | `+53.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,670,000.00 USD | 871.99 USD | 0.00 USD | `+54.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,690,000.00 USD | 24,560.00 USD | 0.00 USD | `+59.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,690,000.00 USD | 400.21 USD | 0.00 USD | `+60.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,710,000.00 USD | 13,850.00 USD | 0.00 USD | `+66.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,710,000.00 USD | 2,360.00 USD | 0.00 USD | `+66.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,710,000.00 USD | 4,160.00 USD | 0.00 USD | `+70.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,710,000.00 USD | 235.54 USD | 0.00 USD | `+76.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,710,000.00 USD | 1,160.00 USD | 0.00 USD | `+78.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,710,000.00 USD | 173.57 USD | 0.00 USD | `+79.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,720,000.00 USD | 380.09 USD | 0.00 USD | `+79.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,730,000.00 USD | 17,150.00 USD | 0.00 USD | `+79.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,730,000.00 USD | 433.35 USD | 0.00 USD | `+82.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,740,000.00 USD | 3,640.00 USD | 0.00 USD | `+85.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,790,000.00 USD | 55,720.00 USD | 0.00 USD | `+86.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,790,000.00 USD | 2,120.00 USD | 0.00 USD | `+86.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,810,000.00 USD | 18,810.00 USD | 0.00 USD | `+89.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1532` | 2,820,000.00 USD | 4,750.00 USD | 0.00 USD | `+93.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1552` | 2,820,000.00 USD | 630.53 USD | 0.00 USD | `+95.59%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 24,090,000.00 USD | 0.00 USD | 24,090,000.00 USD | 33,080.00 USD | 20,050.00 USD | 85,240.00 USD |
| `1D` | `0.0712` | 23,950,000.00 USD | 0.00 USD | 23,950,000.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 23,890,000.00 USD | 0.00 USD | 23,890,000.00 USD | 34,400.00 USD | 58,130.00 USD | 62,360.00 USD |
| `1D` | `0.0714` | 23,730,000.00 USD | 0.00 USD | 23,730,000.00 USD | 32,300.00 USD | 33,120.00 USD | 8,650.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 23,660,000.00 USD | 0.00 USD | 23,660,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD |
| `1D` | `0.0716` | 23,590,000.00 USD | 0.00 USD | 23,590,000.00 USD | 30,130.00 USD | 31,610.00 USD | 270.12 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 23,530,000.00 USD | 0.00 USD | 23,530,000.00 USD | 15,510.00 USD | 7,710.00 USD | 21,730.00 USD |
| `1D` | `0.0718` | 23,490,000.00 USD | 0.00 USD | 23,490,000.00 USD | 63,040.00 USD | 36,880.00 USD | 50,690.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 23,340,000.00 USD | 0.00 USD | 23,340,000.00 USD | 15,840.00 USD | 3,820.00 USD | 7,570.00 USD |
| `1D` | `0.0720` | 23,310,000.00 USD | 0.00 USD | 23,310,000.00 USD | 48,000.00 USD | 15,600.00 USD | 32,030.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 23,210,000.00 USD | 0.00 USD | 23,210,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,520.00 USD |
| `1D` | `0.0722` | 23,150,000.00 USD | 0.00 USD | 23,150,000.00 USD | 29,680.00 USD | 15,630.00 USD | 28,060.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 23,070,000.00 USD | 0.00 USD | 23,070,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,700.00 USD |
| `1D` | `0.0724` | 22,960,000.00 USD | 0.00 USD | 22,960,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,150.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 22,830,000.00 USD | 0.00 USD | 22,830,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,830.00 USD |
| `1D` | `0.0726` | 22,670,000.00 USD | 0.00 USD | 22,670,000.00 USD | 31,660.00 USD | 0.00 USD | 175.16 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 22,640,000.00 USD | 0.00 USD | 22,640,000.00 USD | 20,420.00 USD | 0.00 USD | 285.35 USD |
| `1D` | `0.0728` | 22,620,000.00 USD | 0.00 USD | 22,620,000.00 USD | 15,580.00 USD | 802.30 USD | 261.29 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 22,600,000.00 USD | 0.00 USD | 22,600,000.00 USD | 17,820.00 USD | 0.00 USD | 18,900.00 USD |
| `1D` | `0.0730` | 22,570,000.00 USD | 0.00 USD | 22,570,000.00 USD | 14,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 22,550,000.00 USD | 0.00 USD | 22,550,000.00 USD | 42,980.00 USD | 0.00 USD | 187.18 USD |
| `1D` | `0.0732` | 22,510,000.00 USD | 0.00 USD | 22,510,000.00 USD | 42,110.00 USD | 0.00 USD | 41.24 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 22,470,000.00 USD | 0.00 USD | 22,470,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0734` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 4,580.00 USD | 0.00 USD | 258.52 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 24,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0736` | 22,430,000.00 USD | 0.00 USD | 22,430,000.00 USD | 8,600.00 USD | 0.00 USD | 1.38 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 22,420,000.00 USD | 0.00 USD | 22,420,000.00 USD | 48,230.00 USD | 0.00 USD | 154.70 USD |
| `1D` | `0.0738` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 31,820.00 USD | 0.00 USD | 162.16 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 32,610.00 USD | 0.00 USD | 107.41 USD |
| `1D` | `0.0740` | 22,300,000.00 USD | 0.00 USD | 22,300,000.00 USD | 33,740.00 USD | 0.00 USD | 380.95 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 22,270,000.00 USD | 0.00 USD | 22,270,000.00 USD | 31,820.00 USD | 0.00 USD | 348.56 USD |
| `1D` | `0.0742` | 22,240,000.00 USD | 0.00 USD | 22,240,000.00 USD | 25,930.00 USD | 0.00 USD | 596.52 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 22,210,000.00 USD | 0.00 USD | 22,210,000.00 USD | 28,250.00 USD | 27,500.00 USD | 0.00 USD |
| `1D` | `0.0744` | 22,160,000.00 USD | 0.00 USD | 22,160,000.00 USD | 41,210.00 USD | 1,840.00 USD | 15,030.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 106,370.00 USD | 57,220.00 USD | 25,090.00 USD |
| `1D` | `0.0746` | 21,910,000.00 USD | 0.00 USD | 21,910,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,790.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 21,370,000.00 USD | 0.00 USD | 21,370,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,370.00 USD |
| `1D` | `0.0748` | 20,910,000.00 USD | 0.00 USD | 20,910,000.00 USD | 169,810.00 USD | 65,720.00 USD | 99,490.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 20,580,000.00 USD | 0.00 USD | 20,580,000.00 USD | 194,160.00 USD | 144,960.00 USD | 8,470.00 USD |
| `1D` | `0.0750` | 20,230,000.00 USD | 0.00 USD | 20,230,000.00 USD | 233,830.00 USD | 83,730.00 USD | 120,970.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 19,790,000.00 USD | 0.00 USD | 19,790,000.00 USD | 268,200.00 USD | 82,120.00 USD | 65,030.00 USD |
| `1D` | `0.0752` | 19,370,000.00 USD | 0.00 USD | 19,370,000.00 USD | 117,830.00 USD | 19,450.00 USD | 85,660.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 19,150,000.00 USD | 0.00 USD | 19,150,000.00 USD | 133,330.00 USD | 72,710.00 USD | 28,690.00 USD |
| `1D` | `0.0754` | 18,920,000.00 USD | 0.00 USD | 18,920,000.00 USD | 87,330.00 USD | 62,330.00 USD | 19,270.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 18,750,000.00 USD | 0.00 USD | 18,750,000.00 USD | 109,960.00 USD | 15,650.00 USD | 69,100.00 USD |
| `1D` | `0.0756` | 18,550,000.00 USD | 0.00 USD | 18,550,000.00 USD | 164,890.00 USD | 147,310.00 USD | 112,120.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 88,960.00 USD | 44,210.00 USD | 103,780.00 USD |
| `1D` | `0.0758` | 17,890,000.00 USD | 0.00 USD | 17,890,000.00 USD | 70,320.00 USD | 31,960.00 USD | 91,650.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 17,700,000.00 USD | 0.00 USD | 17,700,000.00 USD | 195,880.00 USD | 130,420.00 USD | 8,990.00 USD |
| `1D` | `0.0760` | 17,360,000.00 USD | 0.00 USD | 17,360,000.00 USD | 235,330.00 USD | 313,670.00 USD | 277,460.00 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 16,540,000.00 USD | 0.00 USD | 16,540,000.00 USD | 500,630.00 USD | 440,880.00 USD | 277,970.00 USD |
| `1D` | `0.0762` | 15,320,000.00 USD | 0.00 USD | 15,320,000.00 USD | 579,620.00 USD | 303,280.00 USD | 223,570.00 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 305,000.00 USD | 179,660.00 USD | 197,480.00 USD |
| `1D` | `0.0764` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 356,430.00 USD | 327,090.00 USD | 23,820.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 12,820,000.00 USD | 0.00 USD | 12,820,000.00 USD | 497,560.00 USD | 213,120.00 USD | 313,980.00 USD |
| `1D` | `0.0766` | 11,800,000.00 USD | 0.00 USD | 11,800,000.00 USD | 621,080.00 USD | 262,670.00 USD | 279,850.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 229,810.00 USD | 78,490.00 USD | 214,190.00 USD |
| `1D` | `0.0768` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 426,850.00 USD | 236,860.00 USD | 142,280.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,000.00 USD |
| `1D` | `0.0770` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,350.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 231,550.00 USD | 266,030.00 USD | 189,840.00 USD |
| `1D` | `0.0772` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 169,730.00 USD | 297,590.00 USD | 333,360.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 272,980.00 USD | 149,960.00 USD | 241,340.00 USD |
| `1D` | `0.0774` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 143,850.00 USD | 97,350.00 USD | 230,920.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 359,420.00 USD | 150,850.00 USD | 17,020.00 USD |
| `1D` | `0.0776` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 137,380.00 USD | 345,400.00 USD | 381,410.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 74,870.00 USD | 182,120.00 USD | 12,500.00 USD |
| `1D` | `0.0778` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 148,860.00 USD | 120,190.00 USD | 200,710.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 85,950.00 USD | 0.00 USD |
| `1D` | `0.0780` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 217,760.00 USD | 88,770.00 USD | 0.00 USD |
| `1D` | `0.0781` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD |
| `1D` | `0.0782` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 44,780.00 USD | 75,640.00 USD | 85,130.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD |
| `1D` | `0.0784` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD |
| `1D` | `0.0788` | 689,800.00 USD | 0.00 USD | 689,800.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 267,030.00 USD | 0.00 USD | 267,030.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD |
| `1D` | `0.0790` | 36,980.00 USD | 0.00 USD | 36,980.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 33,720.00 USD | 0.00 USD | 33,720.00 USD | 0.00 USD | 3,690.00 USD | 30,030.00 USD |
| `1D` | `0.0793` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0796` | 16,260.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 414,540.00 USD | 414,540.00 USD | 0.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD |
| `1D` | `0.0798` | 569,220.00 USD | 569,220.00 USD | 0.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 912,240.00 USD | 912,240.00 USD | 0.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD |
| `1D` | `0.0800` | 917,850.00 USD | 917,850.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `1D` | `0.0804` | 928,750.00 USD | 928,750.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0806` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 3,520.00 USD | 0.00 USD | 162,840.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 200,420.00 USD | 208,070.00 USD | 40,970.00 USD |
| `1D` | `0.0808` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 411,890.00 USD | 131,030.00 USD | 522,290.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 445,800.00 USD | 291,790.00 USD | 12,430.00 USD |
| `1D` | `0.0810` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 293,220.00 USD | 180,540.00 USD | 132,410.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 241,410.00 USD | 233.41 USD |
| `1D` | `0.0812` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 93,910.00 USD | 75,260.00 USD | 135,630.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 27,080.00 USD | 18,240.00 USD | 208,970.00 USD |
| `1D` | `0.0814` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 22,430.00 USD | 10,710.00 USD | 386,300.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 232,650.00 USD | 151,890.00 USD | 112,440.00 USD |
| `1D` | `0.0816` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 441,880.00 USD | 245,220.00 USD | 189,570.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 361,650.00 USD | 152,470.00 USD | 130,280.00 USD |
| `1D` | `0.0818` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 298,910.00 USD | 161,880.00 USD | 322,350.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 8,680,000.00 USD | 8,680,000.00 USD | 0.00 USD | 171,350.00 USD | 368,950.00 USD | 156,680.00 USD |
| `1D` | `0.0820` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 215,860.00 USD | 275,570.00 USD | 499,320.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 383,530.00 USD | 167,310.00 USD | 170,450.00 USD |
| `1D` | `0.0822` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 260,030.00 USD | 184,710.00 USD | 187,620.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 264,720.00 USD | 75,420.00 USD | 8,640.00 USD |
| `1D` | `0.0824` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 147,030.00 USD | 226,510.00 USD | 198,650.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 124,920.00 USD | 94,070.00 USD | 27,800.00 USD |
| `1D` | `0.0826` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 102,880.00 USD | 60,100.00 USD | 190,420.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 52,670.00 USD | 48,230.00 USD | 675.30 USD |
| `1D` | `0.0828` | 12,920,000.00 USD | 12,920,000.00 USD | 0.00 USD | 224,210.00 USD | 37,180.00 USD | 7,510.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 206,610.00 USD | 79,000.00 USD | 72,320.00 USD |
| `1D` | `0.0830` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 262,060.00 USD | 98,430.00 USD | 150,710.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 97,970.00 USD | 39,590.00 USD | 42,870.00 USD |
| `1D` | `0.0832` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 233,350.00 USD | 91,440.00 USD | 86,250.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 159,920.00 USD | 68,410.00 USD | 31,450.00 USD |
| `1D` | `0.0834` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 146,880.00 USD | 60,550.00 USD | 133,390.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 110,610.00 USD | 184,470.00 USD | 78,880.00 USD |
| `1D` | `0.0836` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 71,510.00 USD | 84,520.00 USD | 221,910.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 189,060.00 USD | 61,550.00 USD | 34,020.00 USD |
| `1D` | `0.0838` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 145,530.00 USD | 76,380.00 USD | 48,400.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 67,620.00 USD | 0.00 USD | 855.10 USD |
| `1D` | `0.0840` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 35,250.00 USD | 15,480.00 USD | 1,070.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 32,120.00 USD | 2,010.00 USD | 458.39 USD |
| `1D` | `0.0842` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 30,040.00 USD | 0.00 USD | 47,340.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 37,310.00 USD | 0.00 USD | 140.36 USD |
| `1D` | `0.0844` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 81,010.00 USD | 0.00 USD | 168.86 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 16,660,000.00 USD | 16,660,000.00 USD | 0.00 USD | 15,700.00 USD | 0.00 USD | 575.75 USD |
| `1D` | `0.0846` | 16,740,000.00 USD | 16,740,000.00 USD | 0.00 USD | 72,340.00 USD | 16,670.00 USD | 0.29 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 16,760,000.00 USD | 16,760,000.00 USD | 0.00 USD | 12,740.00 USD | 0.00 USD | 304.58 USD |
| `1D` | `0.0848` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 11,540.00 USD | 0.00 USD | 404.98 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0849` | 16,780,000.00 USD | 16,780,000.00 USD | 0.00 USD | 6,070.00 USD | 0.00 USD | 292.60 USD |
| `1D` | `0.0850` | 16,800,000.00 USD | 16,800,000.00 USD | 0.00 USD | 20,730.00 USD | 0.00 USD | 11.66 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0851` | 16,830,000.00 USD | 16,830,000.00 USD | 0.00 USD | 26,040.00 USD | 11,000.00 USD | 469.88 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `1D` | `0.0853` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 12,910.00 USD | 737.47 USD | 450.74 USD |
| `1D` | `0.0854` | 16,910,000.00 USD | 16,910,000.00 USD | 0.00 USD | 35,960.00 USD | 13,190.00 USD | 10,290.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `1D` | `0.0855` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 64,150.00 USD | 45,460.00 USD | 36,170.00 USD |
| `1D` | `0.0856` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 92,490.00 USD | 32,810.00 USD | 20,120.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `1D` | `0.0857` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 50,540.00 USD | 18,030.00 USD | 27,700.00 USD |
| `1D` | `0.0858` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 48,130.00 USD | 36,780.00 USD | 185.71 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `1D` | `0.0859` | 17,510,000.00 USD | 17,510,000.00 USD | 0.00 USD | 72,260.00 USD | 20,870.00 USD | 40,350.00 USD |
| `1D` | `0.0860` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 44,920.00 USD | 22,170.00 USD | 20,040.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0861` | 17,650,000.00 USD | 17,650,000.00 USD | 0.00 USD | 20,430.00 USD | 0.00 USD | 32,460.00 USD |
| `1D` | `0.0862` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 33,780.00 USD | 29,080.00 USD | 11,390.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0863` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 219.34 USD |
| `1D` | `0.0864` | 17,780,000.00 USD | 17,780,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 5,160.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `1D` | `0.0865` | 17,830,000.00 USD | 17,830,000.00 USD | 0.00 USD | 31,770.00 USD | 1,280.00 USD | 17,790.00 USD |
| `1D` | `0.0866` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 25,410.00 USD | 16,310.00 USD | 19,510.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `1D` | `0.0867` | 17,960,000.00 USD | 17,960,000.00 USD | 0.00 USD | 24,580.00 USD | 37,120.00 USD | 14,100.00 USD |
| `1D` | `0.0868` | 18,020,000.00 USD | 18,020,000.00 USD | 0.00 USD | 8,080.00 USD | 9,300.00 USD | 34,580.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `1D` | `0.0869` | 18,080,000.00 USD | 18,080,000.00 USD | 0.00 USD | 16,230.00 USD | 8,560.00 USD | 36,560.00 USD |
| `1D` | `0.0870` | 18,140,000.00 USD | 18,140,000.00 USD | 0.00 USD | 51,830.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0871` | 18,300,000.00 USD | 18,300,000.00 USD | 0.00 USD | 34,400.00 USD | 58,130.00 USD | 62,360.00 USD |
| `1D` | `0.0872` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 32,300.00 USD | 33,120.00 USD | 8,650.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `1D` | `0.0873` | 18,430,000.00 USD | 18,430,000.00 USD | 0.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `1D` | `0.0875` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 9,700.00 USD | 17,190.00 USD | 0.00 USD |
| `1D` | `0.0876` | 18,500,000.00 USD | 18,500,000.00 USD | 0.00 USD | 20,430.00 USD | 14,420.00 USD | 0.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `1D` | `0.0877` | 18,530,000.00 USD | 18,530,000.00 USD | 0.00 USD | 8,360.00 USD | 5,020.00 USD | 21,730.00 USD |
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
  * Total Open Interest: `1.12B` | Total OI Tokens: `14,117,784,219.1 DOGE`
  * 1h OI Change: `+0.18%` | 4h OI Change: `-0.76%` | 24h OI Change: `-2.73%`
  * Exchange Breakdown: Binance=`270.73M` | Bybit=`110.58M` | OKX=`116.01M` | Hyperliquid=`80.04M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `42.32K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0086%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0066%` | **USDT Bitget** | `0.0081%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `55.47%` | `44.53%` | `1.25` | 6,330,000.00 USD |
| `15M` | `Binance` | `58.35%` | `41.65%` | `1.40` | 2,230,000.00 USD |
| `15M` | `OKX` | `55.27%` | `44.73%` | `1.24` | 1,420,000.00 USD |
| `15M` | `Bybit` | `75.72%` | `24.28%` | `3.12` | 354,330.00 USD |
| `15M` | `KuCoin` | `69.16%` | `30.84%` | `2.24` | 30,910.00 USD |
| `15M` | `Gate` | `50.67%` | `49.33%` | `1.03` | 1,060,000.00 USD |
| `15M` | `Bitget` | `23.29%` | `76.71%` | `0.30` | 62,350.00 USD |
| `15M` | `BingX` | `51.07%` | `48.93%` | `1.04` | 91,270.00 USD |
| `15M` | `MEXC` | `64.17%` | `35.83%` | `1.79` | 329,600.00 USD |
| `15M` | `Bitunix` | `56.32%` | `43.68%` | `1.29` | 225,170.00 USD |
| `15M` | `Hyperliquid` | `63.46%` | `36.54%` | `1.74` | 7,940.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.25%` | `47.75%` | `1.09` | 46,570.00 USD |
| `15M` | `Crypto.com` | `66.58%` | `33.42%` | `1.99` | 15,820.00 USD |
| `15M` | `WhiteBIT` | `42.41%` | `57.59%` | `0.74` | 295,550.00 USD |
| `15M` | `HTX` | `74.03%` | `25.97%` | `2.85` | 6,260.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `50.27%` | `49.73%` | `1.01` | 35,170.00 USD |
| `15M` | `Aster` | `9.06%` | `90.94%` | `0.10` | 117,970.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 176.40 USD |
| `15M` | `Whale Positions` | `58.35%` | `41.65%` | `1.40` | 2,230,000.00 USD |
| `15M` | `Global Accounts` | `55.47%` | `44.53%` | `1.25` | 6,330,000.00 USD |
| `1H` | `DOGE` | `57.12%` | `42.88%` | `1.33` | 13,890,000.00 USD |
| `1H` | `Binance` | `58.62%` | `41.38%` | `1.42` | 8,990,000.00 USD |
| `1H` | `OKX` | `62.71%` | `37.29%` | `1.68` | 679,940.00 USD |
| `1H` | `Bybit` | `68.17%` | `31.83%` | `2.14` | 300,710.00 USD |
| `1H` | `KuCoin` | `45.9%` | `54.1%` | `0.85` | 38,630.00 USD |
| `1H` | `Gate` | `57.77%` | `42.23%` | `1.37` | 471,890.00 USD |
| `1H` | `Bitget` | `49.76%` | `50.24%` | `0.99` | 88,180.00 USD |
| `1H` | `BingX` | `39.28%` | `60.72%` | `0.65` | 1,850,000.00 USD |
| `1H` | `MEXC` | `68.38%` | `31.62%` | `2.16` | 320,110.00 USD |
| `1H` | `Bitunix` | `55.36%` | `44.64%` | `1.24` | 319,410.00 USD |
| `1H` | `Hyperliquid` | `56.29%` | `43.71%` | `1.29` | 46,590.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.85%` | `48.15%` | `1.08` | 258,370.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.15%` | `1.85%` | `53.05` | 170,200.00 USD |
| `1H` | `HTX` | `79.28%` | `20.72%` | `3.83` | 80,450.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.98%` | `32.02%` | `2.12` | 3,600.00 USD |
| `1H` | `Aster` | `73.66%` | `26.34%` | `2.80` | 140,820.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.09%` | `39.91%` | `1.51` | 135,930.00 USD |
| `1H` | `Whale Positions` | `58.62%` | `41.38%` | `1.42` | 8,990,000.00 USD |
| `1H` | `Global Accounts` | `57.12%` | `42.88%` | `1.33` | 13,890,000.00 USD |
| `4H` | `DOGE` | `49.85%` | `50.15%` | `0.99` | 139,010,000.00 USD |
| `4H` | `Binance` | `49.85%` | `50.15%` | `0.99` | 89,600,000.00 USD |
| `4H` | `OKX` | `47.68%` | `52.32%` | `0.91` | 8,290,000.00 USD |
| `4H` | `Bybit` | `44.5%` | `55.5%` | `0.80` | 3,960,000.00 USD |
| `4H` | `KuCoin` | `48.54%` | `51.46%` | `0.94` | 762,630.00 USD |
| `4H` | `Gate` | `57.5%` | `42.5%` | `1.35` | 10,690,000.00 USD |
| `4H` | `Bitget` | `62.57%` | `37.43%` | `1.67` | 3,630,000.00 USD |
| `4H` | `BingX` | `36.33%` | `63.67%` | `0.57` | 8,050,000.00 USD |
| `4H` | `MEXC` | `47.58%` | `52.42%` | `0.91` | 2,100,000.00 USD |
| `4H` | `Bitunix` | `44.01%` | `55.99%` | `0.79` | 3,840,000.00 USD |
| `4H` | `Hyperliquid` | `22.99%` | `77.01%` | `0.30` | 957,330.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.73%` | `49.27%` | `1.03` | 2,920,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `89.5%` | `10.5%` | `8.52` | 818,730.00 USD |
| `4H` | `HTX` | `52.82%` | `47.18%` | `1.12` | 784,710.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `75.01%` | `24.99%` | `3.00` | 143,210.00 USD |
| `4H` | `Aster` | `54.58%` | `45.42%` | `1.20` | 1,240,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `71.73%` | `28.27%` | `2.54` | 1,250,000.00 USD |
| `4H` | `Whale Positions` | `49.85%` | `50.15%` | `0.99` | 89,600,000.00 USD |
| `4H` | `Global Accounts` | `49.85%` | `50.15%` | `0.99` | 139,010,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.0796` | `0.0798` | `0.0796` | `0.0802` | `0.0795` | 5,871,793.04 USD | 2,200,842.18 USD | 3,670,950.86 USD | -1,470,108.68 USD | `-25.04%` | `4B / 23S` |
| `5:00 UTC` | `0.0793` | `0.0794` | `0.0793` | `0.0796` | `0.0792` | 7,734,342.64 USD | 3,622,970.91 USD | 4,111,371.72 USD | -488,400.81 USD | `-6.31%` | `4B / 4S` |
| `0:00 UTC` | `0.0795` | `0.0796` | `0.0795` | `0.0797` | `0.0794` | 2,831,870.97 USD | 1,358,858.88 USD | 1,473,012.09 USD | -114,153.20 USD | `-4.03%` | `5B / 6S` |
| `5:00 UTC` | `0.0795` | `0.0795` | `0.0795` | `0.0797` | `0.0793` | 3,357,728.54 USD | 1,747,237.98 USD | 1,610,490.56 USD | 136,747.43 USD | `+4.07%` | `3B / 4S` |
| `0:00 UTC` | `0.0791` | `0.0791` | `0.0791` | `0.0794` | `0.0789` | 5,383,971.27 USD | 2,616,260.04 USD | 2,767,711.23 USD | -151,451.19 USD | `-2.81%` | `3B / 9S` |
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0790` | 3,072,363.78 USD | 1,995,905.48 USD | 1,076,458.30 USD | 919,447.18 USD | `+29.93%` | `17B / 6S` |
| `0:00 UTC` | `0.0792` | `0.0792` | `0.0792` | `0.0793` | `0.0791` | 2,162,354.33 USD | 812,153.86 USD | 1,350,200.47 USD | -538,046.61 USD | `-24.88%` | `2B / 9S` |
| `5:00 UTC` | `0.0791` | `0.0791` | `0.0791` | `0.0792` | `0.0790` | 1,623,560.28 USD | 710,933.62 USD | 912,626.66 USD | -201,693.05 USD | `-12.42%` | `1B / 6S` |
| `0:00 UTC` | `0.0794` | `0.0794` | `0.0794` | `0.0795` | `0.0791` | 2,224,641.24 USD | 1,501,047.07 USD | 723,594.17 USD | 777,452.89 USD | `+34.95%` | `11B / 0S` |
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0792` | 1,784,065.21 USD | 767,366.55 USD | 1,016,698.67 USD | -249,332.12 USD | `-13.98%` | `3B / 3S` |

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
| `5m` | 43,190.00 USD | 48,120.00 USD | **`ACCUMULATION`** |
| `15m` | 17,880.00 USD | 655,710.00 USD | **`ACCUMULATION`** |
| `30m` | 3,200.00 USD | 946,900.00 USD | **`ACCUMULATION`** |
| `1h` | -42,750.00 USD | 1,470,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,060,000.00 USD | 1,160,000.00 USD | **`ACCUMULATION`** |
| `4h` | -3,350,000.00 USD | -3,750,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,710,000.00 USD | 2,400,000.00 USD | **`ACCUMULATION`** |
| `8h` | -535,420.00 USD | -159,260.00 USD | **`DISTRIBUTION`** |
| `12h` | 516,710.00 USD | -2,310,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -4,440,000.00 USD | -12,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -41,220,000.00 USD | -125,070,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -267,760,000.00 USD | -747,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+43.19K` | 15m=`+17.88K` | 1h=`-42.75K` | 24h=`-4.44M`
* Futures Capital Netflows: 5m=`+48.12K` | 15m=`+655.71K` | 1h=`+1.47M` | 24h=`-12.00M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0786` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0822` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0681`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0800`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
