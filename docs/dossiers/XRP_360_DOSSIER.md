# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 22:36:53 IST` (`2026-10-29 17:06:53 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.29` | **Live Ask Quote**: `1.30` | **Mid Price**: `1.30`
- **Spread Points**: `4.00` | **Spread BPS**: `30.84 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `+0.38` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0067` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.63` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.32` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.32` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.31` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.31` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.30` | EMA-20=`1.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.30` (Slope: `+0.0000`) | EMA-100=`1.30`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.0296`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.28` | Weekly High=`1.34` | Weekly Low=`1.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-0.21%`)
  * Point of Control (POC) = `1.29` (Distance: `+0.59%`)
  * Value Area Low (VAL) = `1.28` (Distance: `+0.99%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.32`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.30` | PDC=`1.33`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.31` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.33` | Low=`1.28`
  * London Session (08:00-16:00 UTC): High=`1.30` | Low=`1.28`
  * New York Session (13:00-21:00 UTC): High=`1.31` | Low=`1.28`
  * Initial Balance (First Hour): IB High=`1.30` | IB Low=`1.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.29` - `1.30`
  * Optimal Trade Entry (OTE 0.705): `1.30`
  * Structural Invalidation Anchor (0.786): `1.31`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.30` | `1.30` | `1.30` | `1.30` | `965,394` | 1,254,042.95 USD | 226,303.94 USD | `+18.05%` | -21,231,232.42 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.30` | `1.30` | `1.30` | `1.30` | `929,685` | 1,207,096.57 USD | 243,081.13 USD | `+20.14%` | -20,988,151.28 USD | `+0.62` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.30` | `1.30` | `1.30` | `1.30` | `1,101,479` | 1,430,778.30 USD | -37,337.99 USD | `-2.61%` | -21,025,489.27 USD | `+0.23` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `1.30` | `1.30` | `1.30` | `1.30` | `7,848,039` | 10,205,311.65 USD | -1,193,506.66 USD | `-11.69%` | -21,679,226.41 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.30` | `1.30` | `1.30` | `1.30` | `3,676,406` | 4,776,328.08 USD | 220,088.84 USD | `+4.61%` | -21,459,137.57 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.30` | `1.30` | `1.30` | `1.30` | `1,259,986` | 1,636,431.66 USD | -227,046.76 USD | `-13.87%` | -21,686,184.33 USD | `-0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.31` | `1.30` | `1.31` | `30,464,520` | 39,839,799.06 USD | 106,608.94 USD | `+0.27%` | -19,101,925.36 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.31` | `1.32` | `1.30` | `1.30` | `30,534,069` | 39,864,527.69 USD | -3,664,960.48 USD | `-9.19%` | -22,766,885.83 USD | `-0.63` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.30` | `1.30` | `1,101,479` | 1,430,778.30 USD | -37,337.99 USD | `-2.61%` | -22,804,223.82 USD | `+0.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.30` | `1.30` | `31,635,553` | 41,295,312.99 USD | -3,702,305.47 USD | `-8.97%` | -28,204,480.61 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.30` | `1.30` | `31,635,553` | 41,295,312.99 USD | -3,702,305.47 USD | `-8.97%` | -28,204,480.61 USD | `+0.12` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.30`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.30` | `11852.0000` | 15,400.49 USD | 2,763,384.66 USD | `5 orders` | `+0.15%` | `-` |
| `ASK` | `1.30` | `101199.0000` | 131,487.86 USD | 2,747,984.17 USD | `8 orders` | `+0.14%` | `-` |
| `ASK` | `1.30` | `325171.0000` | 422,462.16 USD | 2,616,496.31 USD | `4 orders` | `+0.13%` | `-` |
| `ASK` | `1.30` | `227415.0000` | 295,434.83 USD | 2,194,034.15 USD | `6 orders` | `+0.13%` | `-` |
| `ASK` | `1.30` | `125512.0000` | 163,040.09 USD | 1,898,599.32 USD | `15 orders` | `+0.12%` | `-` |
| `ASK` | `1.30` | `359022.0000` | 466,333.68 USD | 1,735,559.23 USD | `14 orders` | `+0.11%` | `-` |
| `ASK` | `1.30` | `39117.0000` | 50,805.16 USD | 1,269,225.55 USD | `8 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `83321.0000` | 108,208.98 USD | 1,218,420.40 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `96434.0000` | 125,229.19 USD | 1,110,211.41 USD | `13 orders` | `+0.09%` | `-` |
| `ASK` | `1.30` | `35712.0000` | 46,372.03 USD | 984,982.22 USD | `3 orders` | `+0.08%` | `-` |
| `ASK` | `1.30` | `77982.0000` | 101,251.83 USD | 938,610.19 USD | `12 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `29650.0000` | 38,494.60 USD | 837,358.36 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `305882.0000` | 397,096.01 USD | 798,863.76 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `1.30` | `115936.0000` | 150,496.52 USD | 401,767.75 USD | `12 orders` | `+0.05%` | `-` |
| `ASK` | `1.30` | `35446.0000` | 46,008.91 USD | 251,271.23 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `1.30` | `54108.0000` | 70,226.77 USD | 205,262.32 USD | `12 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `39398.0000` | 51,130.72 USD | 135,035.55 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `42967.0000` | 55,758.28 USD | 83,904.82 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `1.30` | `11787.0000` | 15,294.81 USD | 28,146.55 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `1.30` | `9905.0000` | 12,851.74 USD | 12,851.74 USD | `7 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.30` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.30` | `0.00%` | `-` |
| `BID` | `1.30` | `9453.0000` | 12,264.32 USD | 12,264.32 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `1.30` | `10324.0000` | 13,393.33 USD | 25,657.65 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `1.30` | `23807.0000` | 30,882.44 USD | 56,540.09 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `1.30` | `38153.0000` | 49,488.26 USD | 106,028.34 USD | `12 orders` | `-0.03%` | `-` |
| `BID` | `1.30` | `90958.0000` | 117,972.53 USD | 224,000.87 USD | `19 orders` | `-0.03%` | `-` |
| `BID` | `1.30` | `96744.0000` | 125,467.29 USD | 349,468.16 USD | `16 orders` | `-0.04%` | `-` |
| `BID` | `1.30` | `68386.0000` | 88,682.96 USD | 438,151.13 USD | `10 orders` | `-0.05%` | `-` |
| `BID` | `1.30` | `105505.0000` | 136,808.33 USD | 574,959.46 USD | `16 orders` | `-0.06%` | `-` |
| `BID` | `1.30` | `326977.0000` | 423,958.38 USD | 998,917.84 USD | `17 orders` | `-0.07%` | `-` |
| `BID` | `1.30` | `110053.0000` | 142,683.71 USD | 1,141,601.55 USD | `10 orders` | `-0.07%` | `-` |
| `BID` | `1.30` | `106241.0000` | 137,730.83 USD | 1,279,332.39 USD | `11 orders` | `-0.08%` | `-` |
| `BID` | `1.30` | `53200.0000` | 68,963.16 USD | 1,348,295.55 USD | `11 orders` | `-0.09%` | `-` |
| `BID` | `1.30` | `300103.0000` | 388,993.51 USD | 1,737,289.06 USD | `15 orders` | `-0.10%` | `-` |
| `BID` | `1.30` | `114330.0000` | 148,183.11 USD | 1,885,472.17 USD | `12 orders` | `-0.10%` | `-` |
| `BID` | `1.30` | `359585.0000` | 466,022.16 USD | 2,351,494.33 USD | `11 orders` | `-0.11%` | `-` |
| `BID` | `1.30` | `78958.0000` | 102,321.67 USD | 2,453,816.00 USD | `6 orders` | `-0.12%` | `-` |
| `BID` | `1.30` | `7392.0000` | 9,578.55 USD | 2,463,394.55 USD | `2 orders` | `-0.13%` | `-` |
| `BID` | `1.30` | `38228.0000` | 49,532.02 USD | 2,512,926.57 USD | `10 orders` | `-0.13%` | `-` |
| `BID` | `1.30` | `302480.0000` | 391,893.09 USD | 2,904,819.66 USD | `7 orders` | `-0.14%` | `-` |
| `BID` | `1.30` | `66232.0000` | 85,803.56 USD | 2,990,623.22 USD | `11 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:34:53 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `28` | `0x31b1...1434` | `LONG` | 45,267,613.85 USD | `35,031,430.00` | `1.13` | `1.29` | `0.9611` | 5,688,730.58 USD | `+12.57%` | `10X Cross` |
| `102` | `0x5b5d...c060` | `SHORT` | 19,064,166.70 USD | `14,754,405.00` | `1.45` | `1.29` | `10.95` | 2,279,846.67 USD | `+11.96%` | `5X Cross` |
| `155` | `0x58f0...0d20` | `LONG` | 14,122,571.51 USD | `10,931,629.00` | `1.36` | `1.29` | `1.25` | -742,581.46 USD | `-5.26%` | `20X Cross` |
| `163` | `0xb83d...6e36` | `SHORT` | 13,638,696.95 USD | `10,555,450.00` | `1.50` | `1.29` | `12.32` | 2,183,872.70 USD | `+16.01%` | `5X Cross` |
| `442` | `0xca49...53c8` | `SHORT` | 5,349,096.27 USD | `4,138,886.00` | `1.44` | `1.29` | `4.30` | 604,226.47 USD | `+11.30%` | `20X Cross` |
| `507` | `0xfc27...9d9d` | `SHORT` | 4,617,578.48 USD | `3,572,871.00` | `1.32` | `1.29` | `5.46` | 84,283.28 USD | `+1.83%` | `20X Cross` |
| `509` | `0x610b...b613` | `LONG` | 4,579,132.63 USD | `3,543,946.00` | `1.44` | `1.29` | `0.7196` | -520,859.98 USD | `-11.37%` | `5X Cross` |
| `548` | `0xc30c...a4c9` | `SHORT` | 4,203,513.17 USD | `3,253,745.00` | `1.42` | `1.29` | `1.65` | 432,710.10 USD | `+10.29%` | `7X Cross` |
| `563` | `0xdd53...2b13` | `SHORT` | 4,102,554.09 USD | `3,174,860.00` | `1.44` | `1.29` | `19.41` | 474,450.10 USD | `+11.56%` | `3X Cross` |
| `588` | `0xecb6...2b00` | `SHORT` | 3,957,849.60 USD | `3,063,114.00` | `1.31` | `1.29` | `9.78` | 48,237.94 USD | `+1.22%` | `10X Cross` |
| `600` | `0x9946...0852` | `SHORT` | 3,909,653.46 USD | `3,025,111.00` | `1.43` | `1.29` | `1.65` | 403,531.10 USD | `+10.32%` | `20X Cross` |
| `688` | `0x9aa5...58af` | `SHORT` | 3,362,652.38 USD | `2,604,083.00` | `1.46` | `1.29` | `4.30` | 435,068.28 USD | `+12.94%` | `20X Cross` |
| `702` | `0xf48f...10fe` | `LONG` | 3,315,243.05 USD | `2,565,779.00` | `1.53` | `1.29` | `0.9557` | -609,397.68 USD | `-18.38%` | `4X Cross` |
| `709` | `0x023a...2355` | `SHORT` | 3,263,426.55 USD | `2,525,481.00` | `1.33` | `1.29` | `4.37` | 90,212.05 USD | `+2.76%` | `20X Cross` |
| `735` | `0x45d2...4029` | `SHORT` | 3,170,257.20 USD | `2,453,000.00` | `1.48` | `1.29` | `15.52` | 468,023.22 USD | `+14.76%` | `20X Cross` |
| `1004` | `0xc179...e0c8` | `SHORT` | 2,288,353.17 USD | `1,770,623.00` | `1.30` | `1.29` | `4.57` | 15,885.85 USD | `+0.69%` | `10X Cross` |
| `1070` | `0xfc66...ca06` | `SHORT` | 2,115,333.98 USD | `1,637,002.00` | `1.31` | `1.29` | `19.75` | 29,657.49 USD | `+1.40%` | `20X Cross` |
| `1085` | `0xeadc...9d55` | `LONG` | 2,092,464.10 USD | `1,619,805.00` | `1.21` | `1.29` | `0.000000` | 133,621.08 USD | `+6.39%` | `20X Cross` |
| `1153` | `0x94b2...599e` | `SHORT` | 1,990,271.09 USD | `1,540,696.00` | `1.36` | `1.29` | `1.85` | 110,195.36 USD | `+5.54%` | `20X Cross` |
| `1179` | `0x3fc5...c0c1` | `SHORT` | 1,952,613.76 USD | `1,511,779.00` | `1.52` | `1.29` | `2.53` | 339,000.85 USD | `+17.36%` | `20X Cross` |
| `1211` | `0x31ef...f715` | `LONG` | 1,905,655.85 USD | `1,475,080.00` | `1.49` | `1.29` | `1.04` | -293,609.55 USD | `-15.41%` | `3X Isolated` |
| `1259` | `0x7737...bf66` | `SHORT` | 1,825,349.99 USD | `1,413,466.00` | `1.41` | `1.29` | `14.08` | 173,518.66 USD | `+9.51%` | `10X Cross` |
| `1285` | `0xef96...9383` | `SHORT` | 1,797,727.11 USD | `1,390,999.00` | `1.34` | `1.29` | `4.12` | 66,058.11 USD | `+3.67%` | `20X Cross` |
| `1340` | `0xbcd4...0dd2` | `SHORT` | 1,699,802.43 USD | `1,316,044.00` | `1.31` | `1.29` | `2.41` | 25,495.44 USD | `+1.50%` | `20X Cross` |
| `1348` | `0xee2b...d67e` | `LONG` | 1,688,241.44 USD | `1,306,284.00` | `1.55` | `1.29` | `0.2597` | -342,413.46 USD | `-20.28%` | `4X Cross` |
| `1401` | `0x215d...f80a` | `LONG` | 1,617,546.24 USD | `1,251,777.00` | `1.32` | `1.29` | `1.19` | -36,907.99 USD | `-2.28%` | `14X Cross` |
| `1454` | `0x123d...3bff` | `LONG` | 1,569,718.94 USD | `1,215,329.00` | `1.35` | `1.29` | `0.000000` | -67,350.28 USD | `-4.29%` | `10X Cross` |
| `1498` | `0x95da...2328` | `LONG` | 1,513,870.38 USD | `1,171,817.00` | `1.37` | `1.29` | `0.000000` | -87,905.61 USD | `-5.81%` | `5X Cross` |
| `1511` | `0xdf95...7d72` | `SHORT` | 1,499,079.93 USD | `1,160,099.00` | `1.37` | `1.29` | `32.37` | 94,258.80 USD | `+6.29%` | `20X Cross` |
| `1584` | `0x5fa3...35b7` | `SHORT` | 1,410,042.89 USD | `1,091,280.00` | `1.31` | `1.29` | `3.10` | 19,216.92 USD | `+1.36%` | `20X Cross` |
| `1643` | `0x4537...8732` | `SHORT` | 1,334,541.76 USD | `1,033,487.00` | `1.32` | `1.29` | `2.23` | 25,504.20 USD | `+1.91%` | `10X Cross` |
| `1658` | `0xb1ce...681b` | `LONG` | 1,320,527.79 USD | `1,021,764.00` | `1.49` | `1.29` | `1.16` | -203,528.70 USD | `-15.41%` | `4X Isolated` |
| `1769` | `0x3c36...461a` | `LONG` | 1,214,357.88 USD | `940,051.00` | `1.30` | `1.29` | `1.06` | -4,722.73 USD | `-0.39%` | `10X Cross` |
| `1991` | `0xbfc7...80b4` | `SHORT` | 1,033,760.00 USD | `800,000.00` | `1.48` | `1.29` | `6.96` | 149,694.65 USD | `+14.48%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.32` | 17,109.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 17.11K USD at 1.3231 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,024.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.02K USD at 1.3231 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,853.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.85K USD at 1.3231 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,366.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.37K USD at 1.3232 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,313.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.31K USD at 1.3232 USD [API] | `2026-10-27 19:18:58` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3224 USD [API] | `2026-10-27 19:25:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,941.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.94K USD at 1.3221 USD [API] | `2026-10-27 19:32:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,142.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.14K USD at 1.3225 USD [API] | `2026-10-27 19:34:38` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 12,586.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.59K USD at 1.3231 USD [API] | `2026-10-27 19:40:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,236.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.24K USD at 1.3233 USD [API] | `2026-10-27 19:50:17` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,372.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.37K USD at 1.3245 USD [API] | `2026-10-27 19:58:34` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,956.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.96K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,333.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.33K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,354.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.35K USD at 1.3245 USD [API] | `2026-10-27 19:58:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,429.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.43K USD at 1.3251 USD [API] | `2026-10-27 20:05:47` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,828.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.83K USD at 1.3248 USD [API] | `2026-10-27 20:05:41` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3248 USD [API] | `2026-10-27 20:05:41` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3248 USD [API] | `2026-10-27 20:05:41` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 32,202.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 32.20K USD at 1.3240 USD [API] | `2026-10-27 20:18:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 15,001.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 15.00K USD at 1.3231 USD [API] | `2026-10-27 20:20:17` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 13,924.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.92K USD at 1.3225 USD [API] | `2026-10-27 20:28:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,592.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.59K USD at 1.3225 USD [API] | `2026-10-27 20:28:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3217 USD [API] | `2026-10-27 20:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3217 USD [API] | `2026-10-27 20:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,874.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.87K USD at 1.3217 USD [API] | `2026-10-27 20:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,007.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3215 USD [API] | `2026-10-27 20:30:42` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 37,802.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 37.80K USD at 1.3197 USD [API] | `2026-10-27 20:41:48` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,861.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.86K USD at 1.3198 USD [API] | `2026-10-27 20:41:48` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,373.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.37K USD at 1.3191 USD [API] | `2026-10-27 20:43:35` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 15,275.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.28K USD at 1.3191 USD [API] | `2026-10-27 20:43:35` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,579.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.58K USD at 1.3206 USD [API] | `2026-10-27 20:49:53` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,824.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.82K USD at 1.3206 USD [API] | `2026-10-27 20:49:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,449.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.45K USD at 1.3204 USD [API] | `2026-10-27 21:16:32` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 73,780.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 73.78K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,099.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.10K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 30,750.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 30.75K USD at 1.3180 USD [API] | `2026-10-27 21:24:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,640.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.64K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,188.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.19K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,112.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.11K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,572.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.57K USD at 1.3187 USD [API] | `2026-10-27 21:26:10` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,590.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.59K USD at 1.3180 USD [API] | `2026-10-27 21:29:26` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 583.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.58K USD at 1.2611 USD [API] | `2026-10-18 19:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 10,779.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 10.78K USD at 1.2611 USD [API] | `2026-10-18 19:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 389.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.39K USD at 1.2611 USD [API] | `2026-10-18 19:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 355.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.36K USD at 1.2611 USD [API] | `2026-10-18 19:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 35,023.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 35.02K USD at 1.2611 USD [API] | `2026-10-18 19:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 721.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.72K USD at 1.2611 USD [API] | `2026-10-18 19:35:49` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 94,303.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 94.30K USD at 1.2611 USD [API] | `2026-10-18 19:35:49` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2670 USD [API] | `2026-10-18 19:30:42` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 89.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2670 USD [API] | `2026-10-18 19:30:42` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 39,789.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 39.79K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 97.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 139.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 30.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 27.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 16,159.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 16.16K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 12.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 635.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.64K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 82.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 40.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 523.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.52K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 424.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.42K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 139.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,369.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.37K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 528.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.53K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 34.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 199.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 3,439.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.44K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 953.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.95K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 10.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 23,519.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 23.52K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 204.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 198.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 57.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.06K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 24.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,327.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.33K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 116.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.12K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 739.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.74K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 4,381.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.38K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 107.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.11K USD at 1.3310 USD [API] | `2026-10-14 14:37:05` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,500.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.50K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 89.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 246.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.25K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.3340 USD [API] | `2026-10-14 14:31:12` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 33,375.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 33.38K USD at 1.3350 USD [API] | `2026-10-14 14:28:24` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,345.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.35K USD at 1.3288 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,266.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.27K USD at 1.3288 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,371.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.37K USD at 1.3289 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,939.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.94K USD at 1.3290 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,355.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.36K USD at 1.3290 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,633.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.63K USD at 1.3281 USD [API] | `2026-10-27 21:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 12,869.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.87K USD at 1.3253 USD [API] | `2026-10-27 21:41:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,391.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.39K USD at 1.3253 USD [API] | `2026-10-27 21:41:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,362.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.36K USD at 1.3256 USD [API] | `2026-10-27 21:42:55` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 184.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.18K USD at 1.3303 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:46:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:46:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,482.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.48K USD at 1.3265 USD [API] | `2026-10-27 21:51:19` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,630.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.63K USD at 1.3265 USD [API] | `2026-10-27 21:51:19` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3261 USD [API] | `2026-10-27 21:55:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 1,700,000.00 USD, Dist: `+2.33%`) | Long MP=`1.28` (Vol: 2,200,000.00 USD, Dist: `--1.10%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+4.48%`) | Long MP=`1.28` (Vol: 2,300,000.00 USD, Dist: `--1.19%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,600,000.00 USD, Dist: `+4.48%`) | Long MP=`1.28` (Vol: 3,500,000.00 USD, Dist: `--0.63%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,300,000.00 USD, Dist: `+4.55%`) | Long MP=`1.28` (Vol: 4,000,000.00 USD, Dist: `--1.15%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2650` | 4,330.00 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 379.50 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 1,500.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 1,060.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 5,060.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 1,010.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 1,140.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 1,900.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 9,820.00 USD | 74,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 1,250.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 1,320.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 2,620.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 151,310.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 15,910.00 USD | 74,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 376.27 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 2,680.00 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 989.06 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 3,100.00 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 30,430.00 USD | 74,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 3,140.00 USD | 74,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 6,750.00 USD | 74,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 2,030.00 USD | 74,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 50,280.00 USD | 74,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 10,910.00 USD | 74,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 2,730.00 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 374.03 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 6,200.00 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 889.20 USD | 74,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 5,760.00 USD | 74,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 32,400.00 USD | 74,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 50,190.00 USD | 74,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 7,150.00 USD | 74,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 8,030.00 USD | 74,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 140,570.00 USD | 74,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 31,770.00 USD | 74,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 28,620.00 USD | 74,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 2,450,000.00 USD | 74,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 11,360.00 USD | 71,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 25,010.00 USD | 71,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,440.00 USD | 71,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 217,680.00 USD | 71,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 23,650.00 USD | 71,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 52,420.00 USD | 71,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 563,960.00 USD | 71,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 70,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 29,790.00 USD | 70,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 40,330.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,580.00 USD | 70,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 22,350.00 USD | 70,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 22,650.00 USD | 70,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 11,200.00 USD | 70,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 44,490.00 USD | 70,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 70,540.00 USD | 70,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 165,960.00 USD | 70,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 28,530.00 USD | 70,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 128,340.00 USD | 70,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 357,260.00 USD | 70,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 2,390,000.00 USD | 69,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 151,820.00 USD | 67,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 26,030.00 USD | 67,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 647,340.00 USD | 67,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 86,480.00 USD | 66,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 79,680.00 USD | 66,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 238,350.00 USD | 66,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 34,010,000.00 USD | 66,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 601,530.00 USD | 32,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 451,370.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 109,310.00 USD | 30,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 472,770.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 155,310.00 USD | 30,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 136,000.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,110,000.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 88,220.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,120,000.00 USD | 27,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 390,040.00 USD | 26,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 455,900.00 USD | 26,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 744,660.00 USD | 25,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 124,020.00 USD | 25,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 107,230.00 USD | 25,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 874,470.00 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 260,740.00 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 86,630.00 USD | 23,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 366,370.00 USD | 23,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 108,390.00 USD | 23,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 209,270,000.00 USD | 209,270,000.00 USD | 201,150.00 USD | 124,580.00 USD | 404,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 63,750,000.00 USD | 63,750,000.00 USD | 65,160.00 USD | 27,440.00 USD | 25,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 208,540,000.00 USD | 208,540,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 63,640,000.00 USD | 63,640,000.00 USD | 176,350.00 USD | 69,040.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 208,110,000.00 USD | 208,110,000.00 USD | 347,490.00 USD | 254,030.00 USD | 414,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 63,310,000.00 USD | 63,310,000.00 USD | 360,460.00 USD | 147,590.00 USD | 199,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 207,100,000.00 USD | 207,100,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 62,600,000.00 USD | 62,600,000.00 USD | 157,740.00 USD | 72,450.00 USD | 158,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 205,720,000.00 USD | 205,720,000.00 USD | 204,250.00 USD | 165,260.00 USD | 248,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,680,000.00 USD | 23,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 62,210,000.00 USD | 62,210,000.00 USD | 85,740.00 USD | 92,510.00 USD | 57,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 205,100,000.00 USD | 205,100,000.00 USD | 330,500.00 USD | 131,130.00 USD | 785,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 61,980,000.00 USD | 61,980,000.00 USD | 103,020.00 USD | 19,070.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 203,860,000.00 USD | 203,860,000.00 USD | 315,770.00 USD | 292,810.00 USD | 991,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 61,850,000.00 USD | 61,850,000.00 USD | 37,660.00 USD | 22,050.00 USD | 70,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 202,250,000.00 USD | 202,250,000.00 USD | 449,440.00 USD | 172,600.00 USD | 709,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 61,720,000.00 USD | 61,720,000.00 USD | 3,680.00 USD | 28,780.00 USD | 80,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 200,920,000.00 USD | 200,920,000.00 USD | 282,820.00 USD | 57,330.00 USD | 336,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 61,610,000.00 USD | 61,610,000.00 USD | 0.00 USD | 11,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 200,250,000.00 USD | 200,250,000.00 USD | 174,190.00 USD | 86,610.00 USD | 505,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 806,220.00 USD | 21,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 61,590,000.00 USD | 61,590,000.00 USD | 3,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 199,480,000.00 USD | 199,480,000.00 USD | 215,940.00 USD | 95,580.00 USD | 240,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 61,590,000.00 USD | 61,590,000.00 USD | 43,120.00 USD | 213.30 USD | 29,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 198,930,000.00 USD | 198,930,000.00 USD | 299,590.00 USD | 106,500.00 USD | 451,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 61,520,000.00 USD | 61,520,000.00 USD | 79,970.00 USD | 47,860.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 198,070,000.00 USD | 198,070,000.00 USD | 12,770.00 USD | 152,290.00 USD | 286,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 61,360,000.00 USD | 61,360,000.00 USD | 63,590.00 USD | 24,610.00 USD | 101,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 197,620,000.00 USD | 197,620,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 61,170,000.00 USD | 61,170,000.00 USD | 51,420.00 USD | 28,660.00 USD | 76,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 197,490,000.00 USD | 197,490,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,650,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 61,010,000.00 USD | 61,010,000.00 USD | 28,500.00 USD | 38,300.00 USD | 53,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 196,880,000.00 USD | 196,880,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 60,890,000.00 USD | 60,890,000.00 USD | 58,560.00 USD | 16,550.00 USD | 62,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 196,270,000.00 USD | 196,270,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 60,760,000.00 USD | 60,760,000.00 USD | 37,540.00 USD | 238.88 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 195,600,000.00 USD | 195,600,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 60,700,000.00 USD | 60,700,000.00 USD | 28,700.00 USD | 17,460.00 USD | 84,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 195,140,000.00 USD | 195,140,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 60,570,000.00 USD | 60,570,000.00 USD | 130,470.00 USD | 44,940.00 USD | 113,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 194,480,000.00 USD | 194,480,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 477,200.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 60,280,000.00 USD | 60,280,000.00 USD | 89,360.00 USD | 18,340.00 USD | 72,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 193,770,000.00 USD | 193,770,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 60,100,000.00 USD | 60,100,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 193,480,000.00 USD | 193,480,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 59,970,000.00 USD | 59,970,000.00 USD | 26,800.00 USD | 20,920.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 193,340,000.00 USD | 193,340,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 59,920,000.00 USD | 59,920,000.00 USD | 55,140.00 USD | 13,890.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 193,260,000.00 USD | 193,260,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 192,960,000.00 USD | 192,960,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 656,350.00 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 59,790,000.00 USD | 59,790,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 192,860,000.00 USD | 192,860,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 59,780,000.00 USD | 59,780,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 192,770,000.00 USD | 192,770,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 192,000,000.00 USD | 192,000,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 191,320,000.00 USD | 191,320,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 190,960,000.00 USD | 190,960,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 355,520.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 190,910,000.00 USD | 190,910,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 190,810,000.00 USD | 190,810,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 190,770,000.00 USD | 190,770,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 190,700,000.00 USD | 190,700,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 190,290,000.00 USD | 190,290,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,680,000.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 189,250,000.00 USD | 189,250,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 188,720,000.00 USD | 188,720,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 188,180,000.00 USD | 188,180,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 187,380,000.00 USD | 187,380,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 59,750,000.00 USD | 59,750,000.00 USD | 11,570.00 USD | 330.88 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 186,070,000.00 USD | 186,070,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 401,010.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 59,730,000.00 USD | 59,730,000.00 USD | 461,130.00 USD | 121,480.00 USD | 258,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 182,260,000.00 USD | 182,260,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 58,890,000.00 USD | 58,890,000.00 USD | 1,030,000.00 USD | 637,760.00 USD | 709,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 177,870,000.00 USD | 177,870,000.00 USD | 1,880,000.00 USD | 930,130.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 56,510,000.00 USD | 56,510,000.00 USD | 871,190.00 USD | 394,760.00 USD | 650,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 172,860,000.00 USD | 172,860,000.00 USD | 1,970,000.00 USD | 633,060.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 54,600,000.00 USD | 54,600,000.00 USD | 297,370.00 USD | 175,590.00 USD | 289,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 167,650,000.00 USD | 167,650,000.00 USD | 982,310.00 USD | 738,740.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 53,840,000.00 USD | 53,840,000.00 USD | 249,140.00 USD | 118,060.00 USD | 310,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 164,850,000.00 USD | 164,850,000.00 USD | 1,850,000.00 USD | 378,130.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 13,870,000.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 53,160,000.00 USD | 53,160,000.00 USD | 372,360.00 USD | 98,350.00 USD | 82,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 160,910,000.00 USD | 160,910,000.00 USD | 2,260,000.00 USD | 1,190,000.00 USD | 5,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 52,600,000.00 USD | 52,600,000.00 USD | 148,690.00 USD | 80,870.00 USD | 180,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 151,940,000.00 USD | 151,940,000.00 USD | 2,150,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 52,190,000.00 USD | 52,190,000.00 USD | 75,260.00 USD | 94,330.00 USD | 264,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 144,960,000.00 USD | 144,960,000.00 USD | 2,790,000.00 USD | 918,840.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 51,760,000.00 USD | 51,760,000.00 USD | 18,760.00 USD | 40,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 139,530,000.00 USD | 139,530,000.00 USD | 961,030.00 USD | 673,830.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 51,700,000.00 USD | 51,700,000.00 USD | 0.00 USD | 0.00 USD | 1,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 136,580,000.00 USD | 136,580,000.00 USD | 515,130.00 USD | 563,470.00 USD | 711,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 641,680.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,700,000.00 USD | 51,700,000.00 USD | 25,000.00 USD | 206.70 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 134,790,000.00 USD | 134,790,000.00 USD | 315,510.00 USD | 370,190.00 USD | 249,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,670,000.00 USD | 51,670,000.00 USD | 218,870.00 USD | 63,890.00 USD | 227,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 133,860,000.00 USD | 133,860,000.00 USD | 1,130,000.00 USD | 449,360.00 USD | 877,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,160,000.00 USD | 51,160,000.00 USD | 522,370.00 USD | 281,580.00 USD | 449,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 131,400,000.00 USD | 131,400,000.00 USD | 1,330,000.00 USD | 1,130,000.00 USD | 852,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 49,910,000.00 USD | 49,910,000.00 USD | 923,370.00 USD | 286,350.00 USD | 633,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 128,090,000.00 USD | 128,090,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 48,060,000.00 USD | 48,060,000.00 USD | 2,140,000.00 USD | 1,360,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 121,480,000.00 USD | 121,480,000.00 USD | 3,610,000.00 USD | 1,750,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 464,620.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 42,940,000.00 USD | 42,940,000.00 USD | 1,890,000.00 USD | 901,940.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 111,760,000.00 USD | 111,760,000.00 USD | 3,920,000.00 USD | 1,540,000.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 38,520,000.00 USD | 38,520,000.00 USD | 767,190.00 USD | 361,880.00 USD | 645,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 99,780,000.00 USD | 99,780,000.00 USD | 1,990,000.00 USD | 1,490,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 36,740,000.00 USD | 36,740,000.00 USD | 621,430.00 USD | 283,050.00 USD | 811,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 93,920,000.00 USD | 93,920,000.00 USD | 3,450,000.00 USD | 1,680,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 35,020,000.00 USD | 35,020,000.00 USD | 980,660.00 USD | 274,890.00 USD | 405,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 84,910,000.00 USD | 84,910,000.00 USD | 4,280,000.00 USD | 3,000,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 33,360,000.00 USD | 33,360,000.00 USD | 1,320,000.00 USD | 523,530.00 USD | 942,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 68,700,000.00 USD | 68,700,000.00 USD | 3,720,000.00 USD | 1,290,000.00 USD | 7,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 479,930.00 USD | 598,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.28` | 30,580,000.00 USD | 30,580,000.00 USD | 2,640,000.00 USD | 1,180,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 56,460,000.00 USD | 56,460,000.00 USD | 6,720,000.00 USD | 2,990,000.00 USD | 7,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 24,740,000.00 USD | 24,740,000.00 USD | 5,350,000.00 USD | 2,560,000.00 USD | 3,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 38,970,000.00 USD | 38,970,000.00 USD | 4,250,000.00 USD | 1,750,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 13,260,000.00 USD | 13,260,000.00 USD | 1,920,000.00 USD | 1,030,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 27,120,000.00 USD | 27,120,000.00 USD | 4,390,000.00 USD | 1,330,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 8,240,000.00 USD | 8,240,000.00 USD | 825,050.00 USD | 947,870.00 USD | 964,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 17,730,000.00 USD | 17,730,000.00 USD | 2,860,000.00 USD | 1,940,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 5,510,000.00 USD | 5,510,000.00 USD | 1,860,000.00 USD | 451,170.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 10,630,000.00 USD | 10,630,000.00 USD | 3,010,000.00 USD | 1,550,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 118,740.00 USD | 118,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.29` | 2,140,000.00 USD | 2,140,000.00 USD | 998,060.00 USD | 522,880.00 USD | 602,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 14,800.00 USD | 14,800.00 USD | 0.00 USD | 0.00 USD | 10,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 3,990.00 USD | 3,990.00 USD | 0.00 USD | 3,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 498.17 USD | 498.17 USD | 0.00 USD | 498.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 1,100,000.00 USD | 1,100,000.00 USD | 641,370.00 USD | 168,250.00 USD | 286,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 1,250,000.00 USD | 1,250,000.00 USD | 963,880.00 USD | 286,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 4,540,000.00 USD | 4,540,000.00 USD | 1,680,000.00 USD | 973,640.00 USD | 787,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 7,580,000.00 USD | 7,580,000.00 USD | 3,480,000.00 USD | 2,340,000.00 USD | 503,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 16,180,000.00 USD | 16,180,000.00 USD | 5,850,000.00 USD | 1,380,000.00 USD | 4,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 20,440,000.00 USD | 20,440,000.00 USD | 4,280,000.00 USD | 2,170,000.00 USD | 6,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 23,600,000.00 USD | 23,600,000.00 USD | 2,450,000.00 USD | 1,520,000.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 28,330,000.00 USD | 28,330,000.00 USD | 2,880,000.00 USD | 1,620,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 26,870,000.00 USD | 26,870,000.00 USD | 1,120,000.00 USD | 1,020,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 32,680,000.00 USD | 32,680,000.00 USD | 580,260.00 USD | 1,810,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 29,740,000.00 USD | 29,740,000.00 USD | 1,350,000.00 USD | 522,680.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 35,070,000.00 USD | 35,070,000.00 USD | 743,110.00 USD | 705,120.00 USD | 935,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 32,610,000.00 USD | 32,610,000.00 USD | 1,920,000.00 USD | 331,160.00 USD | 612,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 38,160,000.00 USD | 38,160,000.00 USD | 1,900,000.00 USD | 430,030.00 USD | 759,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 37,460,000.00 USD | 37,460,000.00 USD | 2,590,000.00 USD | 846,070.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 41,680,000.00 USD | 41,680,000.00 USD | 1,800,000.00 USD | 1,070,000.00 USD | 651,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 4,840.00 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 43,950,000.00 USD | 43,950,000.00 USD | 2,210,000.00 USD | 1,650,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 46,090,000.00 USD | 46,090,000.00 USD | 1,920,000.00 USD | 1,120,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 49,090,000.00 USD | 49,090,000.00 USD | 3,050,000.00 USD | 789,520.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 48,580,000.00 USD | 48,580,000.00 USD | 731,560.00 USD | 193,040.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 51,170,000.00 USD | 51,170,000.00 USD | 809,820.00 USD | 549,070.00 USD | 721,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 49,360,000.00 USD | 49,360,000.00 USD | 526,160.00 USD | 230,290.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 53,320,000.00 USD | 53,320,000.00 USD | 962,470.00 USD | 375,040.00 USD | 805,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 51,660,000.00 USD | 51,660,000.00 USD | 1,140,000.00 USD | 371,730.00 USD | 783,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 54,580,000.00 USD | 54,580,000.00 USD | 902,980.00 USD | 196,710.00 USD | 164,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 52,900,000.00 USD | 52,900,000.00 USD | 811,770.00 USD | 194,320.00 USD | 231,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 22,430.00 USD | 27,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 55,860,000.00 USD | 55,860,000.00 USD | 297,380.00 USD | 267,590.00 USD | 714,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 53,150,000.00 USD | 53,150,000.00 USD | 197,140.00 USD | 0.00 USD | 53,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 56,950,000.00 USD | 56,950,000.00 USD | 150,520.00 USD | 250,520.00 USD | 685,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 53,700,000.00 USD | 53,700,000.00 USD | 14,750.00 USD | 10,370.00 USD | 522,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 57,720,000.00 USD | 57,720,000.00 USD | 157,110.00 USD | 180,230.00 USD | 433,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 54,470,000.00 USD | 54,470,000.00 USD | 0.00 USD | 268,860.00 USD | 500,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 58,260,000.00 USD | 58,260,000.00 USD | 0.00 USD | 164,890.00 USD | 378,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 55,920,000.00 USD | 55,920,000.00 USD | 610,090.00 USD | 0.00 USD | 840,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 58,860,000.00 USD | 58,860,000.00 USD | 335,800.00 USD | 413.40 USD | 264,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 57,610.00 USD | 84,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 60,240,000.00 USD | 60,240,000.00 USD | 662,270.00 USD | 128,780.00 USD | 585,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 57,420,000.00 USD | 57,420,000.00 USD | 570,060.00 USD | 645,230.00 USD | 285,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 63,510,000.00 USD | 63,510,000.00 USD | 1,620,000.00 USD | 405,560.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 59,240,000.00 USD | 59,240,000.00 USD | 960,450.00 USD | 362,920.00 USD | 494,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 67,870,000.00 USD | 67,870,000.00 USD | 1,870,000.00 USD | 466,350.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 63,970,000.00 USD | 63,970,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 71,340,000.00 USD | 71,340,000.00 USD | 1,420,000.00 USD | 853,290.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 69,600,000.00 USD | 69,600,000.00 USD | 1,720,000.00 USD | 2,830,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 75,670,000.00 USD | 75,670,000.00 USD | 2,340,000.00 USD | 667,740.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 80,820,000.00 USD | 80,820,000.00 USD | 3,690,000.00 USD | 1,880,000.00 USD | 5,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 163,410.00 USD | 248,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 78,020,000.00 USD | 78,020,000.00 USD | 997,910.00 USD | 467,820.00 USD | 888,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 88,550,000.00 USD | 88,550,000.00 USD | 2,550,000.00 USD | 2,220,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 79,670,000.00 USD | 79,670,000.00 USD | 796,750.00 USD | 258,460.00 USD | 593,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 98,640,000.00 USD | 98,640,000.00 USD | 4,100,000.00 USD | 1,770,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 82,120,000.00 USD | 82,120,000.00 USD | 993,350.00 USD | 294,820.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 106,770,000.00 USD | 106,770,000.00 USD | 2,720,000.00 USD | 1,440,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 83,280,000.00 USD | 83,280,000.00 USD | 488,380.00 USD | 201,800.00 USD | 472,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 114,950,000.00 USD | 114,950,000.00 USD | 2,490,000.00 USD | 1,220,000.00 USD | 4,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 85,320,000.00 USD | 85,320,000.00 USD | 833,710.00 USD | 345,300.00 USD | 855,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 122,880,000.00 USD | 122,880,000.00 USD | 3,760,000.00 USD | 873,380.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 252,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 86,820,000.00 USD | 86,820,000.00 USD | 578,590.00 USD | 148,190.00 USD | 770,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 126,510,000.00 USD | 126,510,000.00 USD | 1,050,000.00 USD | 883,690.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 87,690,000.00 USD | 87,690,000.00 USD | 680,830.00 USD | 73,510.00 USD | 115,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 130,390,000.00 USD | 130,390,000.00 USD | 1,540,000.00 USD | 732,700.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,090,000.00 USD | 88,090,000.00 USD | 188,490.00 USD | 104,800.00 USD | 115,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 132,900,000.00 USD | 132,900,000.00 USD | 705,260.00 USD | 507,830.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,910,000.00 USD | 88,910,000.00 USD | 386,600.00 USD | 133,350.00 USD | 297,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 137,230,000.00 USD | 137,230,000.00 USD | 2,040,000.00 USD | 918,100.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 90,130,000.00 USD | 90,130,000.00 USD | 452,510.00 USD | 269,500.00 USD | 495,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 139,000,000.00 USD | 139,000,000.00 USD | 521,770.00 USD | 328,930.00 USD | 923,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 201,820.00 USD | 454,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 90,480,000.00 USD | 90,480,000.00 USD | 95,670.00 USD | 0.00 USD | 252,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 139,500,000.00 USD | 139,500,000.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 90,860,000.00 USD | 90,860,000.00 USD | 139,480.00 USD | 116,910.00 USD | 127,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 141,280,000.00 USD | 141,280,000.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,430,000.00 USD | 91,430,000.00 USD | 120,300.00 USD | 80,070.00 USD | 364,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 142,690,000.00 USD | 142,690,000.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 92,020,000.00 USD | 92,020,000.00 USD | 147,360.00 USD | 112,420.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 145,540,000.00 USD | 145,540,000.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 92,270,000.00 USD | 92,270,000.00 USD | 172,450.00 USD | 10,690.00 USD | 66,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 147,230,000.00 USD | 147,230,000.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 92,630,000.00 USD | 92,630,000.00 USD | 123,150.00 USD | 46,920.00 USD | 190,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 148,850,000.00 USD | 148,850,000.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 93,190,000.00 USD | 93,190,000.00 USD | 235,940.00 USD | 78,180.00 USD | 241,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 150,790,000.00 USD | 150,790,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 93,960,000.00 USD | 93,960,000.00 USD | 379,220.00 USD | 97,470.00 USD | 295,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 153,340,000.00 USD | 153,340,000.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 94,480,000.00 USD | 94,480,000.00 USD | 241,850.00 USD | 53,770.00 USD | 224,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 154,420,000.00 USD | 154,420,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 94,910,000.00 USD | 94,910,000.00 USD | 340,420.00 USD | 36,760.00 USD | 56,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 155,520,000.00 USD | 155,520,000.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,530.00 USD | 485,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 95,100,000.00 USD | 95,100,000.00 USD | 81,750.00 USD | 52,300.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,010,000.00 USD | 156,010,000.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 95,260,000.00 USD | 95,260,000.00 USD | 83,870.00 USD | 34,730.00 USD | 36,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 157,100,000.00 USD | 157,100,000.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 95,520,000.00 USD | 95,520,000.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 157,260,000.00 USD | 157,260,000.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 157,590,000.00 USD | 157,590,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 95,540,000.00 USD | 95,540,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,730,000.00 USD | 157,730,000.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,740.00 USD | 497,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 95,640,000.00 USD | 95,640,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,750,000.00 USD | 157,750,000.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,760,000.00 USD | 157,760,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,890,000.00 USD | 157,890,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,010,000.00 USD | 158,010,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,250,000.00 USD | 158,250,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 952.59 USD | 498,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,420,000.00 USD | 158,420,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,590,000.00 USD | 158,590,000.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,740,000.00 USD | 158,740,000.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,910,000.00 USD | 158,910,000.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 95,640,000.00 USD | 95,640,000.00 USD | 4,630.00 USD | 132.35 USD | 204.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 159,410,000.00 USD | 159,410,000.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 502,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 95,760,000.00 USD | 95,760,000.00 USD | 60,530.00 USD | 27,310.00 USD | 25,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 159,840,000.00 USD | 159,840,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 96,080,000.00 USD | 96,080,000.00 USD | 176,350.00 USD | 69,040.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 160,860,000.00 USD | 160,860,000.00 USD | 347,490.00 USD | 254,030.00 USD | 414,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 96,790,000.00 USD | 96,790,000.00 USD | 360,460.00 USD | 147,590.00 USD | 199,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 162,230,000.00 USD | 162,230,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 97,180,000.00 USD | 97,180,000.00 USD | 157,740.00 USD | 72,450.00 USD | 158,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 162,850,000.00 USD | 162,850,000.00 USD | 204,250.00 USD | 165,260.00 USD | 248,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 97,240,000.00 USD | 97,240,000.00 USD | 9,670.00 USD | 54,600.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 97,330,000.00 USD | 97,330,000.00 USD | 29,370.00 USD | 27,060.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 163,200,000.00 USD | 163,200,000.00 USD | 87,470.00 USD | 68,830.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 95,360.00 USD | 597,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 164,100,000.00 USD | 164,100,000.00 USD | 243,040.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 165,700,000.00 USD | 165,700,000.00 USD | 315,770.00 USD | 292,810.00 USD | 991,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 167,030,000.00 USD | 167,030,000.00 USD | 449,440.00 USD | 172,600.00 USD | 709,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 167,710,000.00 USD | 167,710,000.00 USD | 282,820.00 USD | 57,330.00 USD | 336,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 168,120,000.00 USD | 168,120,000.00 USD | 106,080.00 USD | 23,880.00 USD | 281,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 181,920.00 USD | 779,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 168,130,000.00 USD | 168,130,000.00 USD | 0.00 USD | 12,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 11,390.00 USD | 790,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.46` | 5,760.00 USD | 796,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 28,340.00 USD | 824,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 11,820.00 USD | 836,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 227.20 USD | 837,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,680.00 USD | 849,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 47,570.00 USD | 897,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 1,940.00 USD | 899,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,130.00 USD | 900,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 6,320.00 USD | 906,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 908,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 908,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,840.00 USD | 911,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 7,570.00 USD | 918,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 321,070.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 5,220,000.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 4,890,000.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 6,420.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 133,590.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 911.91 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 760.45 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 47,320.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 1,040.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 10,410.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,920.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 3,260.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 4,000.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 2,540.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 2,040.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 3,210.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 2,800,000.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 297.48 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 889.98 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 5,540.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 632.55 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,040.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 246,040.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 339.30 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 69,460.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 103.95 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 8,870.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 287.86 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 333,390.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 1,120.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 393,140.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 279,600.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 5,330.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 2,540.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 1,960.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,830.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.51 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 72,080.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 3,890.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 2,350,000.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 3,460,000.00 USD | 21,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 14,930.00 USD | 21,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 1,060,000.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 92,880.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 3,280.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 175,880.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 108.33 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 146.63 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 91,880.00 USD | 23,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 74,260.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 167.65 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 1,210.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 2,420.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 24,840.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 256,540.00 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 114.77 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,640.00 USD | 23,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 42,710.00 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 613.47 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 3,870,000.00 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 346.27 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 2,250.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 23,350.00 USD | 27,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2650` | 74,630,000.00 USD | 0.00 USD | 4,330.00 USD | `-79.60%` | `16,327.00` |
| `Live` | `Long` | `0.2750` | 74,630,000.00 USD | 0.00 USD | 379.50 USD | `-78.83%` | `1,380.00` |
| `Live` | `Long` | `0.2850` | 74,620,000.00 USD | 0.00 USD | 1,500.00 USD | `-78.06%` | `5,267.00` |
| `Live` | `Long` | `0.2950` | 74,620,000.00 USD | 0.00 USD | 1,060.00 USD | `-77.29%` | `3,596.00` |
| `Live` | `Long` | `0.3150` | 74,620,000.00 USD | 0.00 USD | 5,060.00 USD | `-75.75%` | `16,065.00` |
| `Live` | `Long` | `0.3450` | 74,620,000.00 USD | 0.00 USD | 1,010.00 USD | `-73.45%` | `2,922.00` |
| `Live` | `Long` | `0.3550` | 74,620,000.00 USD | 0.00 USD | 1,140.00 USD | `-72.68%` | `3,215.00` |
| `Live` | `Long` | `0.3650` | 74,620,000.00 USD | 0.00 USD | 1,900.00 USD | `-71.91%` | `5,205.00` |
| `Live` | `Long` | `0.3750` | 74,610,000.00 USD | 0.00 USD | 9,820.00 USD | `-71.14%` | `26,194.00` |
| `Live` | `Long` | `0.3850` | 74,600,000.00 USD | 0.00 USD | 1,250.00 USD | `-70.37%` | `3,252.00` |
| `Live` | `Long` | `0.3950` | 74,600,000.00 USD | 0.00 USD | 1,320.00 USD | `-69.60%` | `3,342.00` |
| `Live` | `Long` | `0.4050` | 74,600,000.00 USD | 0.00 USD | 2,620.00 USD | `-68.83%` | `6,463.00` |
| `Live` | `Long` | `0.4150` | 74,600,000.00 USD | 0.00 USD | 151,310.00 USD | `-68.06%` | `364,614.00` |
| `Live` | `Long` | `0.4250` | 74,450,000.00 USD | 0.00 USD | 15,910.00 USD | `-67.29%` | `37,429.00` |
| `Live` | `Long` | `0.4350` | 74,430,000.00 USD | 0.00 USD | 376.27 USD | `-66.52%` | `865.00` |
| `Live` | `Long` | `0.4550` | 74,430,000.00 USD | 0.00 USD | 2,680.00 USD | `-64.98%` | `5,884.00` |
| `Live` | `Long` | `0.4650` | 74,430,000.00 USD | 0.00 USD | 989.06 USD | `-64.21%` | `2,127.00` |
| `Live` | `Long` | `0.4750` | 74,430,000.00 USD | 0.00 USD | 3,100.00 USD | `-63.44%` | `6,526.00` |
| `Live` | `Long` | `0.4850` | 74,420,000.00 USD | 0.00 USD | 30,430.00 USD | `-62.67%` | `62,742.00` |
| `Live` | `Long` | `0.4950` | 74,390,000.00 USD | 0.00 USD | 3,140.00 USD | `-61.90%` | `6,342.00` |
| `Live` | `Long` | `0.5050` | 74,390,000.00 USD | 0.00 USD | 6,750.00 USD | `-61.13%` | `13,373.00` |
| `Live` | `Long` | `0.5150` | 74,380,000.00 USD | 0.00 USD | 2,030.00 USD | `-60.36%` | `3,945.00` |
| `Live` | `Long` | `0.5250` | 74,380,000.00 USD | 0.00 USD | 50,280.00 USD | `-59.59%` | `95,774.00` |
| `Live` | `Long` | `0.5350` | 74,330,000.00 USD | 0.00 USD | 10,910.00 USD | `-58.82%` | `20,395.00` |
| `Live` | `Long` | `0.5550` | 74,320,000.00 USD | 0.00 USD | 2,730.00 USD | `-57.28%` | `4,927.00` |
| `Live` | `Long` | `0.5650` | 74,320,000.00 USD | 0.00 USD | 374.03 USD | `-56.51%` | `662.00` |
| `Live` | `Long` | `0.5750` | 74,320,000.00 USD | 0.00 USD | 6,200.00 USD | `-55.74%` | `10,784.00` |
| `Live` | `Long` | `0.5850` | 74,310,000.00 USD | 0.00 USD | 889.20 USD | `-54.97%` | `1,520.00` |
| `Live` | `Long` | `0.5950` | 74,310,000.00 USD | 0.00 USD | 5,760.00 USD | `-54.20%` | `9,684.00` |
| `Live` | `Long` | `0.6050` | 74,300,000.00 USD | 0.00 USD | 32,400.00 USD | `-53.43%` | `53,561.00` |
| `Live` | `Long` | `0.6150` | 74,270,000.00 USD | 0.00 USD | 50,190.00 USD | `-52.66%` | `81,617.00` |
| `Live` | `Long` | `0.6250` | 74,220,000.00 USD | 0.00 USD | 7,150.00 USD | `-51.89%` | `11,446.00` |
| `Live` | `Long` | `0.6450` | 74,210,000.00 USD | 0.00 USD | 8,030.00 USD | `-50.35%` | `12,457.00` |
| `Live` | `Long` | `0.6550` | 74,210,000.00 USD | 0.00 USD | 140,570.00 USD | `-49.58%` | `214,605.00` |
| `Live` | `Long` | `0.6650` | 74,070,000.00 USD | 0.00 USD | 31,770.00 USD | `-48.81%` | `47,779.00` |
| `Live` | `Long` | `0.6750` | 74,030,000.00 USD | 0.00 USD | 28,620.00 USD | `-48.04%` | `42,397.00` |
| `Live` | `Long` | `0.6850` | 74,010,000.00 USD | 0.00 USD | 2,450,000.00 USD | `-47.28%` | `3,574,974.00` |
| `Live` | `Long` | `0.6950` | 71,560,000.00 USD | 0.00 USD | 11,360.00 USD | `-46.51%` | `16,348.00` |
| `Live` | `Long` | `0.7050` | 71,550,000.00 USD | 0.00 USD | 25,010.00 USD | `-45.74%` | `35,475.00` |
| `Live` | `Long` | `0.7150` | 71,520,000.00 USD | 0.00 USD | 67,440.00 USD | `-44.97%` | `94,326.00` |
| `Live` | `Long` | `0.7250` | 71,450,000.00 USD | 0.00 USD | 217,680.00 USD | `-44.20%` | `300,251.00` |
| `Live` | `Long` | `0.7350` | 71,240,000.00 USD | 0.00 USD | 23,650.00 USD | `-43.43%` | `32,174.00` |
| `Live` | `Long` | `0.7450` | 71,210,000.00 USD | 0.00 USD | 52,420.00 USD | `-42.66%` | `70,363.00` |
| `Live` | `Long` | `0.7550` | 71,160,000.00 USD | 0.00 USD | 563,960.00 USD | `-41.89%` | `746,966.00` |
| `Live` | `Long` | `0.7650` | 70,600,000.00 USD | 0.00 USD | 2,190.00 USD | `-41.12%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 70,590,000.00 USD | 0.00 USD | 29,790.00 USD | `-40.35%` | `38,433.00` |
| `Live` | `Long` | `0.7850` | 70,560,000.00 USD | 0.00 USD | 40,330.00 USD | `-39.58%` | `51,375.00` |
| `Live` | `Long` | `0.7950` | 70,520,000.00 USD | 0.00 USD | 11,580.00 USD | `-38.81%` | `14,569.00` |
| `Live` | `Long` | `0.8050` | 70,510,000.00 USD | 0.00 USD | 22,350.00 USD | `-38.04%` | `27,761.00` |
| `Live` | `Long` | `0.8150` | 70,490,000.00 USD | 0.00 USD | 22,650.00 USD | `-37.27%` | `27,793.00` |
| `Live` | `Long` | `0.8250` | 70,470,000.00 USD | 0.00 USD | 11,200.00 USD | `-36.50%` | `13,578.00` |
| `Live` | `Long` | `0.8350` | 70,460,000.00 USD | 0.00 USD | 44,490.00 USD | `-35.73%` | `53,278.00` |
| `Live` | `Long` | `0.8450` | 70,410,000.00 USD | 0.00 USD | 70,540.00 USD | `-34.96%` | `83,477.00` |
| `Live` | `Long` | `0.8550` | 70,340,000.00 USD | 0.00 USD | 165,960.00 USD | `-34.19%` | `194,107.00` |
| `Live` | `Long` | `0.8650` | 70,170,000.00 USD | 0.00 USD | 28,530.00 USD | `-33.42%` | `32,977.00` |
| `Live` | `Long` | `0.8750` | 70,150,000.00 USD | 0.00 USD | 128,340.00 USD | `-32.65%` | `146,671.00` |
| `Live` | `Long` | `0.8850` | 70,020,000.00 USD | 0.00 USD | 357,260.00 USD | `-31.88%` | `403,678.00` |
| `Live` | `Long` | `0.8950` | 69,660,000.00 USD | 0.00 USD | 2,390,000.00 USD | `-31.11%` | `2,667,409.00` |
| `Live` | `Long` | `0.9050` | 67,270,000.00 USD | 0.00 USD | 151,820.00 USD | `-30.34%` | `167,753.00` |
| `Live` | `Long` | `0.9150` | 67,120,000.00 USD | 0.00 USD | 26,030.00 USD | `-29.57%` | `28,446.00` |
| `Live` | `Long` | `0.9250` | 67,090,000.00 USD | 0.00 USD | 647,340.00 USD | `-28.80%` | `699,828.00` |
| `Live` | `Long` | `0.9350` | 66,450,000.00 USD | 0.00 USD | 86,480.00 USD | `-28.03%` | `92,488.00` |
| `Live` | `Long` | `0.9450` | 66,360,000.00 USD | 0.00 USD | 79,680.00 USD | `-27.26%` | `84,321.00` |
| `Live` | `Long` | `0.9550` | 66,280,000.00 USD | 0.00 USD | 238,350.00 USD | `-26.49%` | `249,585.00` |
| `Live` | `Long` | `0.9650` | 66,040,000.00 USD | 0.00 USD | 34,010,000.00 USD | `-25.72%` | `35,243,710.00` |
| `Live` | `Long` | `0.9750` | 32,030,000.00 USD | 0.00 USD | 601,530.00 USD | `-24.95%` | `616,951.00` |
| `Live` | `Long` | `0.9850` | 31,430,000.00 USD | 0.00 USD | 451,370.00 USD | `-24.18%` | `458,242.00` |
| `Live` | `Long` | `0.9950` | 30,980,000.00 USD | 0.00 USD | 109,310.00 USD | `-23.41%` | `109,856.00` |
| `Live` | `Long` | `1.00` | 30,870,000.00 USD | 0.00 USD | 472,770.00 USD | `-22.64%` | `470,421.00` |
| `Live` | `Long` | `1.01` | 30,400,000.00 USD | 0.00 USD | 155,310.00 USD | `-21.87%` | `153,014.00` |
| `Live` | `Long` | `1.02` | 30,240,000.00 USD | 0.00 USD | 136,000.00 USD | `-21.11%` | `132,685.00` |
| `Live` | `Long` | `1.03` | 30,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | `-20.34%` | `2,038,781.00` |
| `Live` | `Long` | `1.04` | 28,000,000.00 USD | 0.00 USD | 88,220.00 USD | `-19.57%` | `84,423.00` |
| `Live` | `Long` | `1.05` | 27,910,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-18.80%` | `1,059,173.00` |
| `Live` | `Long` | `1.06` | 26,790,000.00 USD | 0.00 USD | 390,040.00 USD | `-18.03%` | `366,231.00` |
| `Live` | `Long` | `1.07` | 26,400,000.00 USD | 0.00 USD | 455,900.00 USD | `-17.26%` | `424,092.00` |
| `Live` | `Long` | `1.08` | 25,940,000.00 USD | 0.00 USD | 744,660.00 USD | `-16.49%` | `686,318.00` |
| `Live` | `Long` | `1.09` | 25,200,000.00 USD | 0.00 USD | 124,020.00 USD | `-15.72%` | `113,256.00` |
| `Live` | `Long` | `1.10` | 25,080,000.00 USD | 0.00 USD | 107,230.00 USD | `-14.95%` | `97,040.00` |
| `Live` | `Long` | `1.11` | 24,970,000.00 USD | 0.00 USD | 874,470.00 USD | `-14.18%` | `784,280.00` |
| `Live` | `Long` | `1.12` | 24,090,000.00 USD | 0.00 USD | 260,740.00 USD | `-13.41%` | `231,773.00` |
| `Live` | `Long` | `1.14` | 23,830,000.00 USD | 0.00 USD | 86,630.00 USD | `-12.64%` | `76,330.00` |
| `Live` | `Long` | `1.15` | 23,750,000.00 USD | 0.00 USD | 366,370.00 USD | `-11.87%` | `319,977.00` |
| `Live` | `Long` | `1.16` | 23,380,000.00 USD | 0.00 USD | 108,390.00 USD | `-11.10%` | `93,846.00` |
| `Live` | `Long` | `1.17` | 23,270,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-10.33%` | `1,438,783.00` |
| `Live` | `Long` | `1.18` | 21,600,000.00 USD | 0.00 USD | 806,220.00 USD | `-9.56%` | `686,142.00` |
| `Live` | `Long` | `1.19` | 20,790,000.00 USD | 0.00 USD | 1,650,000.00 USD | `-8.79%` | `1,388,418.00` |
| `Live` | `Long` | `1.20` | 19,140,000.00 USD | 0.00 USD | 477,200.00 USD | `-8.02%` | `399,331.00` |
| `Live` | `Long` | `1.21` | 18,670,000.00 USD | 0.00 USD | 656,350.00 USD | `-7.25%` | `544,691.00` |
| `Live` | `Long` | `1.22` | 18,010,000.00 USD | 0.00 USD | 355,520.00 USD | `-6.48%` | `292,612.00` |
| `Live` | `Long` | `1.23` | 17,660,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-5.71%` | `1,367,921.00` |
| `Live` | `Long` | `1.24` | 15,980,000.00 USD | 0.00 USD | 401,010.00 USD | `-4.94%` | `324,705.00` |
| `Live` | `Long` | `1.25` | 15,580,000.00 USD | 0.00 USD | 13,870,000.00 USD | `-4.17%` | `11,143,653.00` |
| `Live` | `Long` | `1.25` | 1,700,000.00 USD | 0.00 USD | 641,680.00 USD | `-3.40%` | `511,296.00` |
| `Live` | `Long` | `1.26` | 1,060,000.00 USD | 0.00 USD | 464,620.00 USD | `-2.63%` | `367,291.00` |
| `Live` | `Long` | `1.27` | 598,670.00 USD | 0.00 USD | 479,930.00 USD | `-1.86%` | `376,418.00` |
| `Live` | `Long` | `1.28` | 118,740.00 USD | 0.00 USD | 118,740.00 USD | `-1.09%` | `92,404.00` |
| `Live` | `Short` | `1.31` | 4,840.00 USD | 4,840.00 USD | 0.00 USD | `+1.22%` | `3,680.00` |
| `Live` | `Short` | `1.32` | 27,260.00 USD | 22,430.00 USD | 0.00 USD | `+1.99%` | `16,925.00` |
| `Live` | `Short` | `1.33` | 84,880.00 USD | 57,610.00 USD | 0.00 USD | `+2.76%` | `43,154.00` |
| `Live` | `Short` | `1.34` | 248,280.00 USD | 163,410.00 USD | 0.00 USD | `+3.53%` | `121,492.00` |
| `Live` | `Short` | `1.35` | 252,280.00 USD | 3,990.00 USD | 0.00 USD | `+4.29%` | `2,947.00` |
| `Live` | `Short` | `1.36` | 454,100.00 USD | 201,820.00 USD | 0.00 USD | `+5.06%` | `147,857.00` |
| `Live` | `Short` | `1.39` | 485,630.00 USD | 31,530.00 USD | 0.00 USD | `+6.60%` | `22,763.00` |
| `Live` | `Short` | `1.40` | 497,370.00 USD | 11,740.00 USD | 0.00 USD | `+7.37%` | `8,418.00` |
| `Live` | `Short` | `1.41` | 498,320.00 USD | 952.59 USD | 0.00 USD | `+8.14%` | `678.00` |
| `Live` | `Short` | `1.42` | 502,180.00 USD | 3,860.00 USD | 0.00 USD | `+8.91%` | `2,727.00` |
| `Live` | `Short` | `1.43` | 597,540.00 USD | 95,360.00 USD | 0.00 USD | `+9.68%` | `66,921.00` |
| `Live` | `Short` | `1.44` | 779,460.00 USD | 181,920.00 USD | 0.00 USD | `+10.45%` | `126,772.00` |
| `Live` | `Short` | `1.45` | 790,850.00 USD | 11,390.00 USD | 0.00 USD | `+11.22%` | `7,884.00` |
| `Live` | `Short` | `1.46` | 796,610.00 USD | 5,760.00 USD | 0.00 USD | `+11.99%` | `3,957.00` |
| `Live` | `Short` | `1.47` | 824,950.00 USD | 28,340.00 USD | 0.00 USD | `+12.76%` | `19,347.00` |
| `Live` | `Short` | `1.48` | 836,780.00 USD | 11,820.00 USD | 0.00 USD | `+13.53%` | `8,016.00` |
| `Live` | `Short` | `1.49` | 837,010.00 USD | 227.20 USD | 0.00 USD | `+14.30%` | `153.00` |
| `Live` | `Short` | `1.50` | 849,690.00 USD | 12,680.00 USD | 0.00 USD | `+15.07%` | `8,482.00` |
| `Live` | `Short` | `1.50` | 897,260.00 USD | 47,570.00 USD | 0.00 USD | `+15.84%` | `31,611.00` |
| `Live` | `Short` | `1.51` | 899,200.00 USD | 1,940.00 USD | 0.00 USD | `+16.61%` | `1,280.00` |
| `Live` | `Short` | `1.53` | 900,330.00 USD | 1,130.00 USD | 0.00 USD | `+18.15%` | `734.00` |
| `Live` | `Short` | `1.54` | 906,640.00 USD | 6,320.00 USD | 0.00 USD | `+18.92%` | `4,088.00` |
| `Live` | `Short` | `1.55` | 908,000.00 USD | 1,360.00 USD | 0.00 USD | `+19.69%` | `873.00` |
| `Live` | `Short` | `1.56` | 908,560.00 USD | 555.57 USD | 0.00 USD | `+20.46%` | `355.00` |
| `Live` | `Short` | `1.57` | 911,390.00 USD | 2,840.00 USD | 0.00 USD | `+21.23%` | `1,800.00` |
| `Live` | `Short` | `1.58` | 918,960.00 USD | 7,570.00 USD | 0.00 USD | `+22.00%` | `4,773.00` |
| `Live` | `Short` | `1.59` | 1,240,000.00 USD | 321,070.00 USD | 0.00 USD | `+22.77%` | `201,298.00` |
| `Live` | `Short` | `1.60` | 6,460,000.00 USD | 5,220,000.00 USD | 0.00 USD | `+23.54%` | `3,253,745.00` |
| `Live` | `Short` | `1.61` | 11,350,000.00 USD | 4,890,000.00 USD | 0.00 USD | `+24.31%` | `3,025,482.00` |
| `Live` | `Short` | `1.62` | 11,350,000.00 USD | 6,420.00 USD | 0.00 USD | `+25.08%` | `3,950.00` |
| `Live` | `Short` | `1.64` | 11,370,000.00 USD | 11,270.00 USD | 0.00 USD | `+25.85%` | `6,892.00` |
| `Live` | `Short` | `1.65` | 11,500,000.00 USD | 133,590.00 USD | 0.00 USD | `+26.62%` | `81,210.00` |
| `Live` | `Short` | `1.66` | 11,500,000.00 USD | 911.91 USD | 0.00 USD | `+27.39%` | `551.00` |
| `Live` | `Short` | `1.67` | 11,500,000.00 USD | 586.08 USD | 0.00 USD | `+28.16%` | `352.00` |
| `Live` | `Short` | `1.68` | 11,500,000.00 USD | 760.45 USD | 0.00 USD | `+28.93%` | `454.00` |
| `Live` | `Short` | `1.69` | 11,550,000.00 USD | 47,320.00 USD | 0.00 USD | `+29.70%` | `28,084.00` |
| `Live` | `Short` | `1.70` | 11,550,000.00 USD | 1,040.00 USD | 0.00 USD | `+30.46%` | `615.00` |
| `Live` | `Short` | `1.71` | 11,550,000.00 USD | 1,980.00 USD | 0.00 USD | `+31.23%` | `1,163.00` |
| `Live` | `Short` | `1.72` | 11,560,000.00 USD | 10,410.00 USD | 0.00 USD | `+32.00%` | `6,068.00` |
| `Live` | `Short` | `1.73` | 11,560,000.00 USD | 1,920.00 USD | 0.00 USD | `+32.77%` | `1,115.00` |
| `Live` | `Short` | `1.74` | 11,570,000.00 USD | 2,970.00 USD | 0.00 USD | `+33.54%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 11,570,000.00 USD | 3,260.00 USD | 0.00 USD | `+34.31%` | `1,869.00` |
| `Live` | `Short` | `1.75` | 11,570,000.00 USD | 4,000.00 USD | 0.00 USD | `+35.08%` | `2,277.00` |
| `Live` | `Short` | `1.76` | 11,580,000.00 USD | 2,540.00 USD | 0.00 USD | `+35.85%` | `1,440.00` |
| `Live` | `Short` | `1.77` | 11,580,000.00 USD | 2,040.00 USD | 0.00 USD | `+36.62%` | `1,148.00` |
| `Live` | `Short` | `1.78` | 11,710,000.00 USD | 129,540.00 USD | 0.00 USD | `+37.39%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 11,710,000.00 USD | 3,210.00 USD | 0.00 USD | `+38.16%` | `1,790.00` |
| `Live` | `Short` | `1.80` | 11,710,000.00 USD | 889.87 USD | 0.00 USD | `+38.93%` | `493.00` |
| `Live` | `Short` | `1.81` | 14,510,000.00 USD | 2,800,000.00 USD | 0.00 USD | `+39.70%` | `1,541,357.00` |
| `Live` | `Short` | `1.82` | 14,510,000.00 USD | 297.48 USD | 0.00 USD | `+40.47%` | `163.00` |
| `Live` | `Short` | `1.83` | 14,510,000.00 USD | 889.98 USD | 0.00 USD | `+41.24%` | `485.00` |
| `Live` | `Short` | `1.84` | 14,520,000.00 USD | 5,540.00 USD | 0.00 USD | `+42.01%` | `3,000.00` |
| `Live` | `Short` | `1.85` | 14,520,000.00 USD | 632.55 USD | 0.00 USD | `+42.78%` | `341.00` |
| `Live` | `Short` | `1.86` | 14,520,000.00 USD | 2,040.00 USD | 0.00 USD | `+43.55%` | `1,095.00` |
| `Live` | `Short` | `1.88` | 14,770,000.00 USD | 246,040.00 USD | 0.00 USD | `+44.32%` | `131,222.00` |
| `Live` | `Short` | `1.89` | 14,770,000.00 USD | 339.30 USD | 0.00 USD | `+45.09%` | `180.00` |
| `Live` | `Short` | `1.90` | 14,770,000.00 USD | 4,190.00 USD | 0.00 USD | `+45.86%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 14,840,000.00 USD | 69,460.00 USD | 0.00 USD | `+46.63%` | `36,460.00` |
| `Live` | `Short` | `1.93` | 14,840,000.00 USD | 103.95 USD | 0.00 USD | `+48.17%` | `54.00` |
| `Live` | `Short` | `1.94` | 14,850,000.00 USD | 8,870.00 USD | 0.00 USD | `+48.94%` | `4,584.00` |
| `Live` | `Short` | `1.95` | 14,850,000.00 USD | 287.86 USD | 0.00 USD | `+49.71%` | `148.00` |
| `Live` | `Short` | `1.96` | 14,850,000.00 USD | 293.25 USD | 0.00 USD | `+50.48%` | `150.00` |
| `Live` | `Short` | `1.97` | 15,180,000.00 USD | 333,390.00 USD | 0.00 USD | `+51.25%` | `169,663.00` |
| `Live` | `Short` | `1.98` | 15,180,000.00 USD | 651.75 USD | 0.00 USD | `+52.02%` | `330.00` |
| `Live` | `Short` | `2.00` | 15,180,000.00 USD | 1,120.00 USD | 0.00 USD | `+53.56%` | `561.00` |
| `Live` | `Short` | `2.00` | 15,580,000.00 USD | 393,140.00 USD | 0.00 USD | `+54.33%` | `196,081.00` |
| `Live` | `Short` | `2.02` | 15,580,000.00 USD | 513.83 USD | 0.00 USD | `+55.10%` | `255.00` |
| `Live` | `Short` | `2.04` | 15,860,000.00 USD | 279,600.00 USD | 0.00 USD | `+57.40%` | `136,722.00` |
| `Live` | `Short` | `2.06` | 15,860,000.00 USD | 5,330.00 USD | 0.00 USD | `+58.94%` | `2,583.00` |
| `Live` | `Short` | `2.10` | 15,870,000.00 USD | 2,540.00 USD | 0.00 USD | `+61.25%` | `1,214.00` |
| `Live` | `Short` | `2.10` | 15,870,000.00 USD | 1,960.00 USD | 0.00 USD | `+62.02%` | `929.00` |
| `Live` | `Short` | `2.12` | 15,870,000.00 USD | 3,100.00 USD | 0.00 USD | `+62.79%` | `1,468.00` |
| `Live` | `Short` | `2.15` | 15,870,000.00 USD | 196.11 USD | 0.00 USD | `+65.87%` | `91.00` |
| `Live` | `Short` | `2.17` | 15,870,000.00 USD | 2,830.00 USD | 0.00 USD | `+67.41%` | `1,299.00` |
| `Live` | `Short` | `2.19` | 15,870,000.00 USD | 100.51 USD | 0.00 USD | `+68.18%` | `46.00` |
| `Live` | `Short` | `2.19` | 15,950,000.00 USD | 72,080.00 USD | 0.00 USD | `+68.95%` | `32,837.00` |
| `Live` | `Short` | `2.23` | 15,950,000.00 USD | 3,890.00 USD | 0.00 USD | `+71.26%` | `1,748.00` |
| `Live` | `Short` | `2.25` | 18,300,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+72.80%` | `1,048,956.00` |
| `Live` | `Short` | `2.27` | 21,770,000.00 USD | 3,460,000.00 USD | 0.00 USD | `+74.34%` | `1,529,461.00` |
| `Live` | `Short` | `2.27` | 21,780,000.00 USD | 14,930.00 USD | 0.00 USD | `+75.11%` | `6,561.00` |
| `Live` | `Short` | `2.29` | 22,850,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+75.88%` | `465,112.00` |
| `Live` | `Short` | `2.31` | 22,940,000.00 USD | 92,880.00 USD | 0.00 USD | `+77.42%` | `40,296.00` |
| `Live` | `Short` | `2.33` | 22,940,000.00 USD | 3,280.00 USD | 0.00 USD | `+78.96%` | `1,409.00` |
| `Live` | `Short` | `2.33` | 23,120,000.00 USD | 175,880.00 USD | 0.00 USD | `+79.73%` | `75,323.00` |
| `Live` | `Short` | `2.35` | 23,120,000.00 USD | 108.33 USD | 0.00 USD | `+81.27%` | `46.00` |
| `Live` | `Short` | `2.37` | 23,120,000.00 USD | 146.63 USD | 0.00 USD | `+82.04%` | `62.00` |
| `Live` | `Short` | `2.38` | 23,210,000.00 USD | 91,880.00 USD | 0.00 USD | `+82.80%` | `38,688.00` |
| `Live` | `Short` | `2.38` | 23,290,000.00 USD | 74,260.00 USD | 0.00 USD | `+83.57%` | `31,136.00` |
| `Live` | `Short` | `2.40` | 23,290,000.00 USD | 167.65 USD | 0.00 USD | `+84.34%` | `70.00` |
| `Live` | `Short` | `2.40` | 23,290,000.00 USD | 1,210.00 USD | 0.00 USD | `+85.11%` | `504.00` |
| `Live` | `Short` | `2.42` | 23,290,000.00 USD | 2,420.00 USD | 0.00 USD | `+85.88%` | `1,000.00` |
| `Live` | `Short` | `2.46` | 23,310,000.00 USD | 24,840.00 USD | 0.00 USD | `+89.73%` | `10,078.00` |
| `Live` | `Short` | `2.48` | 23,570,000.00 USD | 256,540.00 USD | 0.00 USD | `+90.50%` | `103,651.00` |
| `Live` | `Short` | `2.50` | 23,570,000.00 USD | 114.77 USD | 0.00 USD | `+92.04%` | `46.00` |
| `Live` | `Short` | `2.52` | 23,580,000.00 USD | 5,640.00 USD | 0.00 USD | `+93.58%` | `2,244.00` |
| `Live` | `Short` | `2.52` | 23,620,000.00 USD | 42,710.00 USD | 0.00 USD | `+94.35%` | `16,914.00` |
| `Live` | `Short` | `2.54` | 23,620,000.00 USD | 613.47 USD | 0.00 USD | `+95.12%` | `242.00` |
| `Live` | `Short` | `2.56` | 27,490,000.00 USD | 3,870,000.00 USD | 0.00 USD | `+96.66%` | `1,516,193.00` |
| `Live` | `Short` | `2.56` | 27,490,000.00 USD | 346.27 USD | 0.00 USD | `+97.43%` | `135.00` |
| `Live` | `Short` | `2.58` | 27,500,000.00 USD | 2,250.00 USD | 0.00 USD | `+98.20%` | `875.00` |
| `Live` | `Short` | `2.58` | 27,520,000.00 USD | 23,350.00 USD | 0.00 USD | `+98.97%` | `9,031.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3050` | 197,030,000.00 USD | 0.00 USD | 147.62 USD | `-76.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3250` | 197,030,000.00 USD | 0.00 USD | 145.28 USD | `-74.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 197,030,000.00 USD | 0.00 USD | 139.12 USD | `-71.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 197,030,000.00 USD | 0.00 USD | 200.86 USD | `-68.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4250` | 197,030,000.00 USD | 0.00 USD | 173.82 USD | `-67.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 197,030,000.00 USD | 0.00 USD | 408.51 USD | `-65.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 197,030,000.00 USD | 0.00 USD | 520.52 USD | `-64.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 197,030,000.00 USD | 0.00 USD | 151.12 USD | `-64.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 197,030,000.00 USD | 0.00 USD | 190.00 USD | `-63.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 197,030,000.00 USD | 0.00 USD | 145.50 USD | `-62.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 197,020,000.00 USD | 0.00 USD | 1,030.00 USD | `-61.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 197,020,000.00 USD | 0.00 USD | 306.60 USD | `-59.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 197,020,000.00 USD | 0.00 USD | 6,750.00 USD | `-57.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 197,020,000.00 USD | 0.00 USD | 374.60 USD | `-56.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 197,020,000.00 USD | 0.00 USD | 100.62 USD | `-54.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 197,020,000.00 USD | 0.00 USD | 791.85 USD | `-51.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 197,020,000.00 USD | 0.00 USD | 573.40 USD | `-50.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 197,010,000.00 USD | 0.00 USD | 3,450.00 USD | `-49.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 197,010,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 197,010,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 197,010,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 197,010,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 197,000,000.00 USD | 0.00 USD | 2,880.00 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 197,000,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 197,000,000.00 USD | 0.00 USD | 798.57 USD | `-34.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 197,000,000.00 USD | 0.00 USD | 690.38 USD | `-32.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 197,000,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 197,000,000.00 USD | 0.00 USD | 1,910.00 USD | `-31.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 197,000,000.00 USD | 0.00 USD | 838.94 USD | `-30.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 196,990,000.00 USD | 0.00 USD | 188.49 USD | `-29.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 196,990,000.00 USD | 0.00 USD | 2,730.00 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 196,990,000.00 USD | 0.00 USD | 1,150.00 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 196,990,000.00 USD | 0.00 USD | 112.46 USD | `-27.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 196,990,000.00 USD | 0.00 USD | 2,360.00 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 196,990,000.00 USD | 0.00 USD | 3,910.00 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 196,980,000.00 USD | 0.00 USD | 546,370.00 USD | `-24.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 196,440,000.00 USD | 0.00 USD | 5,250.00 USD | `-24.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 196,430,000.00 USD | 0.00 USD | 897.49 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 196,430,000.00 USD | 0.00 USD | 15,070.00 USD | `-22.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 196,420,000.00 USD | 0.00 USD | 4,330.00 USD | `-21.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 196,410,000.00 USD | 0.00 USD | 2,020.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 196,410,000.00 USD | 0.00 USD | 38,000.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 196,370,000.00 USD | 0.00 USD | 3,970.00 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 196,370,000.00 USD | 0.00 USD | 7,090.00 USD | `-18.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 196,360,000.00 USD | 0.00 USD | 3,230.00 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 196,360,000.00 USD | 0.00 USD | 34,770.00 USD | `-17.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 196,320,000.00 USD | 0.00 USD | 973.25 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 196,320,000.00 USD | 0.00 USD | 8,250.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 196,310,000.00 USD | 0.00 USD | 2,970.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 196,310,000.00 USD | 0.00 USD | 9,300.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 196,300,000.00 USD | 0.00 USD | 77,120.00 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 196,220,000.00 USD | 0.00 USD | 12,910.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 196,210,000.00 USD | 0.00 USD | 35,220.00 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 196,180,000.00 USD | 0.00 USD | 5,360.00 USD | `-11.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 196,170,000.00 USD | 0.00 USD | 14,080.00 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 196,160,000.00 USD | 0.00 USD | 4,790.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 196,150,000.00 USD | 0.00 USD | 90,010.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 196,060,000.00 USD | 0.00 USD | 12,570.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 196,050,000.00 USD | 0.00 USD | 57,020.00 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 195,990,000.00 USD | 0.00 USD | 57,160.00 USD | `-6.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 195,940,000.00 USD | 0.00 USD | 144,860.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 195,790,000.00 USD | 0.00 USD | 398,990.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 195,390,000.00 USD | 0.00 USD | 258,780.00 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 195,130,000.00 USD | 0.00 USD | 480,130.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 194,650,000.00 USD | 0.00 USD | 134,550.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 194,520,000.00 USD | 0.00 USD | 360,930.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.28` | 194,160,000.00 USD | 0.00 USD | 64,520,000.00 USD | `-1.09%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1.29` | 129,630,000.00 USD | 0.00 USD | 129,630,000.00 USD | `-0.32%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.30` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 69,370.00 USD | 66,700.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 352,430.00 USD | 283,070.00 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 462,870.00 USD | 110,440.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 635,700.00 USD | 172,830.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 664,110.00 USD | 28,410.00 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 964,200.00 USD | 300,090.00 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,040,000.00 USD | 73,650.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,110,000.00 USD | 71,640.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,190,000.00 USD | 81,740.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,560,000.00 USD | 4,370,000.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,600,000.00 USD | 31,160.00 USD | 0.00 USD | `+8.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,620,000.00 USD | 19,800.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 5,700,000.00 USD | 82,400.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 5,960,000.00 USD | 260,610.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,000,000.00 USD | 44,870.00 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,030,000.00 USD | 27,080.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,140,000.00 USD | 108,480.00 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,220,000.00 USD | 84,290.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,240,000.00 USD | 15,160.00 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,320,000.00 USD | 84,680.00 USD | 0.00 USD | `+15.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,340,000.00 USD | 18,210.00 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,370,000.00 USD | 32,440.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,430,000.00 USD | 57,450.00 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,470,000.00 USD | 36,160.00 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,470,000.00 USD | 6,110.00 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,480,000.00 USD | 6,300.00 USD | 0.00 USD | `+20.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,490,000.00 USD | 6,410.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,500,000.00 USD | 9,700.00 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,620,000.00 USD | 126,740.00 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,620,000.00 USD | 1,130.00 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,710,000.00 USD | 83,090.00 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,710,000.00 USD | 464.75 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 6,910,000.00 USD | 199,230.00 USD | 0.00 USD | `+25.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 6,910,000.00 USD | 3,970.00 USD | 0.00 USD | `+26.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 6,940,000.00 USD | 33,550.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 6,950,000.00 USD | 8,220.00 USD | 0.00 USD | `+28.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 6,960,000.00 USD | 5,760.00 USD | 0.00 USD | `+28.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,030,000.00 USD | 70,850.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,040,000.00 USD | 8,570.00 USD | 0.00 USD | `+30.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,300,000.00 USD | 259,410.00 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,310,000.00 USD | 14,030.00 USD | 0.00 USD | `+32.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,330,000.00 USD | 14,560.00 USD | 0.00 USD | `+32.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,370,000.00 USD | 44,100.00 USD | 0.00 USD | `+33.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,370,000.00 USD | 4,710.00 USD | 0.00 USD | `+34.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,380,000.00 USD | 6,330.00 USD | 0.00 USD | `+35.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,400,000.00 USD | 21,720.00 USD | 0.00 USD | `+35.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,520,000.00 USD | 122,200.00 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,620,000.00 USD | 96,900.00 USD | 0.00 USD | `+37.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,660,000.00 USD | 33,690.00 USD | 0.00 USD | `+38.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,660,000.00 USD | 254.51 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,660,000.00 USD | 2,530.00 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,660,000.00 USD | 1,830.00 USD | 0.00 USD | `+40.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,670,000.00 USD | 7,630.00 USD | 0.00 USD | `+41.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,670,000.00 USD | 5,700.00 USD | 0.00 USD | `+42.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,680,000.00 USD | 8,390.00 USD | 0.00 USD | `+42.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,690,000.00 USD | 4,550.00 USD | 0.00 USD | `+44.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,690,000.00 USD | 591.89 USD | 0.00 USD | `+45.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,730,000.00 USD | 44,350.00 USD | 0.00 USD | `+45.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,740,000.00 USD | 10,020.00 USD | 0.00 USD | `+46.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 7,750,000.00 USD | 7,410.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,750,000.00 USD | 265.10 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,750,000.00 USD | 2,040.00 USD | 0.00 USD | `+49.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,750,000.00 USD | 1,510.00 USD | 0.00 USD | `+50.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 7,770,000.00 USD | 14,120.00 USD | 0.00 USD | `+51.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 7,770,000.00 USD | 4,010.00 USD | 0.00 USD | `+52.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 7,770,000.00 USD | 325.54 USD | 0.00 USD | `+52.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,780,000.00 USD | 7,020.00 USD | 0.00 USD | `+53.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,920,000.00 USD | 138,900.00 USD | 0.00 USD | `+54.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 7,920,000.00 USD | 781.82 USD | 0.00 USD | `+55.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 7,920,000.00 USD | 222.75 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,920,000.00 USD | 862.84 USD | 0.00 USD | `+56.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,920,000.00 USD | 3,490.00 USD | 0.00 USD | `+57.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 7,930,000.00 USD | 3,940.00 USD | 0.00 USD | `+58.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 7,930,000.00 USD | 661.93 USD | 0.00 USD | `+59.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,050,000.00 USD | 124,400.00 USD | 0.00 USD | `+61.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,050,000.00 USD | 1,580.00 USD | 0.00 USD | `+62.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,070,000.00 USD | 13,900.00 USD | 0.00 USD | `+63.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,090,000.00 USD | 24,840.00 USD | 0.00 USD | `+65.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,140,000.00 USD | 50,580.00 USD | 0.00 USD | `+65.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,140,000.00 USD | 1,710.00 USD | 0.00 USD | `+66.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,150,000.00 USD | 1,970.00 USD | 0.00 USD | `+68.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,300,000.00 USD | 151,380.00 USD | 0.00 USD | `+70.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,300,000.00 USD | 7,340.00 USD | 0.00 USD | `+72.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,310,000.00 USD | 3,120.00 USD | 0.00 USD | `+75.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,310,000.00 USD | 1,140.00 USD | 0.00 USD | `+75.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,320,000.00 USD | 12,150.00 USD | 0.00 USD | `+76.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,320,000.00 USD | 370.40 USD | 0.00 USD | `+78.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,370,000.00 USD | 47,430.00 USD | 0.00 USD | `+79.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,370,000.00 USD | 2,410.00 USD | 0.00 USD | `+82.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,370,000.00 USD | 475.00 USD | 0.00 USD | `+82.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,370,000.00 USD | 2,540.00 USD | 0.00 USD | `+84.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,630,000.00 USD | 251,200.00 USD | 0.00 USD | `+85.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,630,000.00 USD | 1,370.00 USD | 0.00 USD | `+85.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,630,000.00 USD | 564.92 USD | 0.00 USD | `+87.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,640,000.00 USD | 8,110.00 USD | 0.00 USD | `+88.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,640,000.00 USD | 3,420.00 USD | 0.00 USD | `+91.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,640,000.00 USD | 124.75 USD | 0.00 USD | `+92.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,680,000.00 USD | 42,600.00 USD | 0.00 USD | `+92.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 8,680,000.00 USD | 378.75 USD | 0.00 USD | `+94.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 8,680,000.00 USD | 389.88 USD | 0.00 USD | `+97.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.58` | 8,680,000.00 USD | 775.50 USD | 0.00 USD | `+98.97%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.16` | 209,270,000.00 USD | 0.00 USD | 209,270,000.00 USD | 201,150.00 USD | 124,580.00 USD | 404,890.00 USD |
| `1D` | `1.16` | 63,750,000.00 USD | 0.00 USD | 63,750,000.00 USD | 65,160.00 USD | 27,440.00 USD | 25,930.00 USD |
| `7D` | `1.16` | 208,540,000.00 USD | 0.00 USD | 208,540,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.16` | 63,640,000.00 USD | 0.00 USD | 63,640,000.00 USD | 176,350.00 USD | 69,040.00 USD | 79,970.00 USD |
| `7D` | `1.16` | 208,110,000.00 USD | 0.00 USD | 208,110,000.00 USD | 347,490.00 USD | 254,030.00 USD | 414,710.00 USD |
| `1D` | `1.16` | 63,310,000.00 USD | 0.00 USD | 63,310,000.00 USD | 360,460.00 USD | 147,590.00 USD | 199,700.00 USD |
| `7D` | `1.16` | 207,100,000.00 USD | 0.00 USD | 207,100,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 62,600,000.00 USD | 0.00 USD | 62,600,000.00 USD | 157,740.00 USD | 72,450.00 USD | 158,530.00 USD |
| `7D` | `1.17` | 205,720,000.00 USD | 0.00 USD | 205,720,000.00 USD | 204,250.00 USD | 165,260.00 USD | 248,940.00 USD |
| `1D` | `1.17` | 62,210,000.00 USD | 0.00 USD | 62,210,000.00 USD | 85,740.00 USD | 92,510.00 USD | 57,820.00 USD |
| `7D` | `1.17` | 205,100,000.00 USD | 0.00 USD | 205,100,000.00 USD | 330,500.00 USD | 131,130.00 USD | 785,270.00 USD |
| `1D` | `1.17` | 61,980,000.00 USD | 0.00 USD | 61,980,000.00 USD | 103,020.00 USD | 19,070.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 203,860,000.00 USD | 0.00 USD | 203,860,000.00 USD | 315,770.00 USD | 292,810.00 USD | 991,730.00 USD |
| `1D` | `1.17` | 61,850,000.00 USD | 0.00 USD | 61,850,000.00 USD | 37,660.00 USD | 22,050.00 USD | 70,330.00 USD |
| `7D` | `1.17` | 202,250,000.00 USD | 0.00 USD | 202,250,000.00 USD | 449,440.00 USD | 172,600.00 USD | 709,440.00 USD |
| `1D` | `1.17` | 61,720,000.00 USD | 0.00 USD | 61,720,000.00 USD | 3,680.00 USD | 28,780.00 USD | 80,990.00 USD |
| `7D` | `1.17` | 200,920,000.00 USD | 0.00 USD | 200,920,000.00 USD | 282,820.00 USD | 57,330.00 USD | 336,880.00 USD |
| `1D` | `1.17` | 61,610,000.00 USD | 0.00 USD | 61,610,000.00 USD | 0.00 USD | 11,120.00 USD | 0.00 USD |
| `7D` | `1.18` | 200,250,000.00 USD | 0.00 USD | 200,250,000.00 USD | 174,190.00 USD | 86,610.00 USD | 505,470.00 USD |
| `1D` | `1.18` | 61,590,000.00 USD | 0.00 USD | 61,590,000.00 USD | 3,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.18` | 199,480,000.00 USD | 0.00 USD | 199,480,000.00 USD | 215,940.00 USD | 95,580.00 USD | 240,920.00 USD |
| `1D` | `1.18` | 61,590,000.00 USD | 0.00 USD | 61,590,000.00 USD | 43,120.00 USD | 213.30 USD | 29,730.00 USD |
| `7D` | `1.18` | 198,930,000.00 USD | 0.00 USD | 198,930,000.00 USD | 299,590.00 USD | 106,500.00 USD | 451,600.00 USD |
| `1D` | `1.18` | 61,520,000.00 USD | 0.00 USD | 61,520,000.00 USD | 79,970.00 USD | 47,860.00 USD | 28,680.00 USD |
| `7D` | `1.18` | 198,070,000.00 USD | 0.00 USD | 198,070,000.00 USD | 12,770.00 USD | 152,290.00 USD | 286,090.00 USD |
| `1D` | `1.18` | 61,360,000.00 USD | 0.00 USD | 61,360,000.00 USD | 63,590.00 USD | 24,610.00 USD | 101,460.00 USD |
| `7D` | `1.18` | 197,620,000.00 USD | 0.00 USD | 197,620,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.18` | 61,170,000.00 USD | 0.00 USD | 61,170,000.00 USD | 51,420.00 USD | 28,660.00 USD | 76,490.00 USD |
| `7D` | `1.19` | 197,490,000.00 USD | 0.00 USD | 197,490,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD |
| `1D` | `1.19` | 61,010,000.00 USD | 0.00 USD | 61,010,000.00 USD | 28,500.00 USD | 38,300.00 USD | 53,040.00 USD |
| `7D` | `1.19` | 196,880,000.00 USD | 0.00 USD | 196,880,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD |
| `1D` | `1.19` | 60,890,000.00 USD | 0.00 USD | 60,890,000.00 USD | 58,560.00 USD | 16,550.00 USD | 62,510.00 USD |
| `7D` | `1.19` | 196,270,000.00 USD | 0.00 USD | 196,270,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD |
| `1D` | `1.19` | 60,760,000.00 USD | 0.00 USD | 60,760,000.00 USD | 37,540.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 195,600,000.00 USD | 0.00 USD | 195,600,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `1D` | `1.19` | 60,700,000.00 USD | 0.00 USD | 60,700,000.00 USD | 28,700.00 USD | 17,460.00 USD | 84,160.00 USD |
| `7D` | `1.19` | 195,140,000.00 USD | 0.00 USD | 195,140,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 60,570,000.00 USD | 0.00 USD | 60,570,000.00 USD | 130,470.00 USD | 44,940.00 USD | 113,180.00 USD |
| `7D` | `1.20` | 194,480,000.00 USD | 0.00 USD | 194,480,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 60,280,000.00 USD | 0.00 USD | 60,280,000.00 USD | 89,360.00 USD | 18,340.00 USD | 72,750.00 USD |
| `7D` | `1.20` | 193,770,000.00 USD | 0.00 USD | 193,770,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 60,100,000.00 USD | 0.00 USD | 60,100,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD |
| `7D` | `1.20` | 193,480,000.00 USD | 0.00 USD | 193,480,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD |
| `1D` | `1.20` | 59,970,000.00 USD | 0.00 USD | 59,970,000.00 USD | 26,800.00 USD | 20,920.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 193,340,000.00 USD | 0.00 USD | 193,340,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 59,920,000.00 USD | 0.00 USD | 59,920,000.00 USD | 55,140.00 USD | 13,890.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 193,260,000.00 USD | 0.00 USD | 193,260,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD |
| `7D` | `1.21` | 192,960,000.00 USD | 0.00 USD | 192,960,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 59,790,000.00 USD | 0.00 USD | 59,790,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 192,860,000.00 USD | 0.00 USD | 192,860,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 59,780,000.00 USD | 0.00 USD | 59,780,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 192,770,000.00 USD | 0.00 USD | 192,770,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD |
| `7D` | `1.21` | 192,000,000.00 USD | 0.00 USD | 192,000,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD |
| `7D` | `1.21` | 191,320,000.00 USD | 0.00 USD | 191,320,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD |
| `7D` | `1.22` | 190,960,000.00 USD | 0.00 USD | 190,960,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD |
| `7D` | `1.22` | 190,910,000.00 USD | 0.00 USD | 190,910,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 190,810,000.00 USD | 0.00 USD | 190,810,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD |
| `7D` | `1.22` | 190,770,000.00 USD | 0.00 USD | 190,770,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD |
| `7D` | `1.22` | 190,700,000.00 USD | 0.00 USD | 190,700,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD |
| `7D` | `1.23` | 190,290,000.00 USD | 0.00 USD | 190,290,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD |
| `7D` | `1.23` | 189,250,000.00 USD | 0.00 USD | 189,250,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD |
| `7D` | `1.23` | 188,720,000.00 USD | 0.00 USD | 188,720,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD |
| `7D` | `1.23` | 188,180,000.00 USD | 0.00 USD | 188,180,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD |
| `7D` | `1.23` | 187,380,000.00 USD | 0.00 USD | 187,380,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD |
| `1D` | `1.23` | 59,750,000.00 USD | 0.00 USD | 59,750,000.00 USD | 11,570.00 USD | 330.88 USD | 1,410.00 USD |
| `7D` | `1.24` | 186,070,000.00 USD | 0.00 USD | 186,070,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD |
| `1D` | `1.24` | 59,730,000.00 USD | 0.00 USD | 59,730,000.00 USD | 461,130.00 USD | 121,480.00 USD | 258,880.00 USD |
| `7D` | `1.24` | 182,260,000.00 USD | 0.00 USD | 182,260,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD |
| `1D` | `1.24` | 58,890,000.00 USD | 0.00 USD | 58,890,000.00 USD | 1,030,000.00 USD | 637,760.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 177,870,000.00 USD | 0.00 USD | 177,870,000.00 USD | 1,880,000.00 USD | 930,130.00 USD | 2,190,000.00 USD |
| `1D` | `1.24` | 56,510,000.00 USD | 0.00 USD | 56,510,000.00 USD | 871,190.00 USD | 394,760.00 USD | 650,530.00 USD |
| `7D` | `1.24` | 172,860,000.00 USD | 0.00 USD | 172,860,000.00 USD | 1,970,000.00 USD | 633,060.00 USD | 2,610,000.00 USD |
| `1D` | `1.24` | 54,600,000.00 USD | 0.00 USD | 54,600,000.00 USD | 297,370.00 USD | 175,590.00 USD | 289,470.00 USD |
| `7D` | `1.24` | 167,650,000.00 USD | 0.00 USD | 167,650,000.00 USD | 982,310.00 USD | 738,740.00 USD | 1,080,000.00 USD |
| `1D` | `1.24` | 53,840,000.00 USD | 0.00 USD | 53,840,000.00 USD | 249,140.00 USD | 118,060.00 USD | 310,590.00 USD |
| `7D` | `1.25` | 164,850,000.00 USD | 0.00 USD | 164,850,000.00 USD | 1,850,000.00 USD | 378,130.00 USD | 1,710,000.00 USD |
| `1D` | `1.25` | 53,160,000.00 USD | 0.00 USD | 53,160,000.00 USD | 372,360.00 USD | 98,350.00 USD | 82,150.00 USD |
| `7D` | `1.25` | 160,910,000.00 USD | 0.00 USD | 160,910,000.00 USD | 2,260,000.00 USD | 1,190,000.00 USD | 5,520,000.00 USD |
| `1D` | `1.25` | 52,600,000.00 USD | 0.00 USD | 52,600,000.00 USD | 148,690.00 USD | 80,870.00 USD | 180,400.00 USD |
| `7D` | `1.25` | 151,940,000.00 USD | 0.00 USD | 151,940,000.00 USD | 2,150,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD |
| `1D` | `1.25` | 52,190,000.00 USD | 0.00 USD | 52,190,000.00 USD | 75,260.00 USD | 94,330.00 USD | 264,590.00 USD |
| `7D` | `1.25` | 144,960,000.00 USD | 0.00 USD | 144,960,000.00 USD | 2,790,000.00 USD | 918,840.00 USD | 1,710,000.00 USD |
| `1D` | `1.25` | 51,760,000.00 USD | 0.00 USD | 51,760,000.00 USD | 18,760.00 USD | 40,660.00 USD | 0.00 USD |
| `7D` | `1.25` | 139,530,000.00 USD | 0.00 USD | 139,530,000.00 USD | 961,030.00 USD | 673,830.00 USD | 1,310,000.00 USD |
| `1D` | `1.25` | 51,700,000.00 USD | 0.00 USD | 51,700,000.00 USD | 0.00 USD | 0.00 USD | 1,830.00 USD |
| `7D` | `1.25` | 136,580,000.00 USD | 0.00 USD | 136,580,000.00 USD | 515,130.00 USD | 563,470.00 USD | 711,210.00 USD |
| `1D` | `1.26` | 51,700,000.00 USD | 0.00 USD | 51,700,000.00 USD | 25,000.00 USD | 206.70 USD | 2,790.00 USD |
| `7D` | `1.26` | 134,790,000.00 USD | 0.00 USD | 134,790,000.00 USD | 315,510.00 USD | 370,190.00 USD | 249,530.00 USD |
| `1D` | `1.26` | 51,670,000.00 USD | 0.00 USD | 51,670,000.00 USD | 218,870.00 USD | 63,890.00 USD | 227,630.00 USD |
| `7D` | `1.26` | 133,860,000.00 USD | 0.00 USD | 133,860,000.00 USD | 1,130,000.00 USD | 449,360.00 USD | 877,110.00 USD |
| `1D` | `1.26` | 51,160,000.00 USD | 0.00 USD | 51,160,000.00 USD | 522,370.00 USD | 281,580.00 USD | 449,880.00 USD |
| `7D` | `1.26` | 131,400,000.00 USD | 0.00 USD | 131,400,000.00 USD | 1,330,000.00 USD | 1,130,000.00 USD | 852,870.00 USD |
| `1D` | `1.26` | 49,910,000.00 USD | 0.00 USD | 49,910,000.00 USD | 923,370.00 USD | 286,350.00 USD | 633,190.00 USD |
| `7D` | `1.26` | 128,090,000.00 USD | 0.00 USD | 128,090,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD |
| `1D` | `1.26` | 48,060,000.00 USD | 0.00 USD | 48,060,000.00 USD | 2,140,000.00 USD | 1,360,000.00 USD | 1,620,000.00 USD |
| `7D` | `1.26` | 121,480,000.00 USD | 0.00 USD | 121,480,000.00 USD | 3,610,000.00 USD | 1,750,000.00 USD | 4,360,000.00 USD |
| `1D` | `1.27` | 42,940,000.00 USD | 0.00 USD | 42,940,000.00 USD | 1,890,000.00 USD | 901,940.00 USD | 1,630,000.00 USD |
| `7D` | `1.27` | 111,760,000.00 USD | 0.00 USD | 111,760,000.00 USD | 3,920,000.00 USD | 1,540,000.00 USD | 6,520,000.00 USD |
| `1D` | `1.27` | 38,520,000.00 USD | 0.00 USD | 38,520,000.00 USD | 767,190.00 USD | 361,880.00 USD | 645,800.00 USD |
| `7D` | `1.27` | 99,780,000.00 USD | 0.00 USD | 99,780,000.00 USD | 1,990,000.00 USD | 1,490,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.27` | 36,740,000.00 USD | 0.00 USD | 36,740,000.00 USD | 621,430.00 USD | 283,050.00 USD | 811,850.00 USD |
| `7D` | `1.27` | 93,920,000.00 USD | 0.00 USD | 93,920,000.00 USD | 3,450,000.00 USD | 1,680,000.00 USD | 3,880,000.00 USD |
| `1D` | `1.27` | 35,020,000.00 USD | 0.00 USD | 35,020,000.00 USD | 980,660.00 USD | 274,890.00 USD | 405,630.00 USD |
| `7D` | `1.27` | 84,910,000.00 USD | 0.00 USD | 84,910,000.00 USD | 4,280,000.00 USD | 3,000,000.00 USD | 8,930,000.00 USD |
| `1D` | `1.27` | 33,360,000.00 USD | 0.00 USD | 33,360,000.00 USD | 1,320,000.00 USD | 523,530.00 USD | 942,530.00 USD |
| `7D` | `1.27` | 68,700,000.00 USD | 0.00 USD | 68,700,000.00 USD | 3,720,000.00 USD | 1,290,000.00 USD | 7,220,000.00 USD |
| `1D` | `1.28` | 30,580,000.00 USD | 0.00 USD | 30,580,000.00 USD | 2,640,000.00 USD | 1,180,000.00 USD | 2,020,000.00 USD |
| `7D` | `1.28` | 56,460,000.00 USD | 0.00 USD | 56,460,000.00 USD | 6,720,000.00 USD | 2,990,000.00 USD | 7,780,000.00 USD |
| `1D` | `1.28` | 24,740,000.00 USD | 0.00 USD | 24,740,000.00 USD | 5,350,000.00 USD | 2,560,000.00 USD | 3,560,000.00 USD |
| `7D` | `1.28` | 38,970,000.00 USD | 0.00 USD | 38,970,000.00 USD | 4,250,000.00 USD | 1,750,000.00 USD | 5,850,000.00 USD |
| `1D` | `1.28` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 1,920,000.00 USD | 1,030,000.00 USD | 2,070,000.00 USD |
| `7D` | `1.28` | 27,120,000.00 USD | 0.00 USD | 27,120,000.00 USD | 4,390,000.00 USD | 1,330,000.00 USD | 3,680,000.00 USD |
| `1D` | `1.28` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 825,050.00 USD | 947,870.00 USD | 964,900.00 USD |
| `7D` | `1.28` | 17,730,000.00 USD | 0.00 USD | 17,730,000.00 USD | 2,860,000.00 USD | 1,940,000.00 USD | 2,290,000.00 USD |
| `1D` | `1.28` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 1,860,000.00 USD | 451,170.00 USD | 1,060,000.00 USD |
| `7D` | `1.28` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 3,010,000.00 USD | 1,550,000.00 USD | 3,690,000.00 USD |
| `1D` | `1.29` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 998,060.00 USD | 522,880.00 USD | 602,110.00 USD |
| `7D` | `1.29` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 2,390,000.00 USD |
| `1D` | `1.29` | 14,800.00 USD | 0.00 USD | 14,800.00 USD | 0.00 USD | 0.00 USD | 10,810.00 USD |
| `1D` | `1.29` | 3,990.00 USD | 0.00 USD | 3,990.00 USD | 0.00 USD | 3,990.00 USD | 0.00 USD |
| `7D` | `1.29` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.29` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.29` | 498.17 USD | 498.17 USD | 0.00 USD | 0.00 USD | 498.17 USD | 0.00 USD |
| `1D` | `1.30` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 641,370.00 USD | 168,250.00 USD | 286,490.00 USD |
| `7D` | `1.30` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 963,880.00 USD | 286,660.00 USD | 0.00 USD |
| `1D` | `1.30` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 1,680,000.00 USD | 973,640.00 USD | 787,890.00 USD |
| `7D` | `1.30` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 3,480,000.00 USD | 2,340,000.00 USD | 503,260.00 USD |
| `1D` | `1.30` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 5,850,000.00 USD | 1,380,000.00 USD | 4,410,000.00 USD |
| `7D` | `1.30` | 20,440,000.00 USD | 20,440,000.00 USD | 0.00 USD | 4,280,000.00 USD | 2,170,000.00 USD | 6,410,000.00 USD |
| `1D` | `1.31` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 2,450,000.00 USD | 1,520,000.00 USD | 3,450,000.00 USD |
| `7D` | `1.31` | 28,330,000.00 USD | 28,330,000.00 USD | 0.00 USD | 2,880,000.00 USD | 1,620,000.00 USD | 3,390,000.00 USD |
| `1D` | `1.31` | 26,870,000.00 USD | 26,870,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,020,000.00 USD | 1,120,000.00 USD |
| `7D` | `1.31` | 32,680,000.00 USD | 32,680,000.00 USD | 0.00 USD | 580,260.00 USD | 1,810,000.00 USD | 1,960,000.00 USD |
| `1D` | `1.31` | 29,740,000.00 USD | 29,740,000.00 USD | 0.00 USD | 1,350,000.00 USD | 522,680.00 USD | 1,000,000.00 USD |
| `7D` | `1.31` | 35,070,000.00 USD | 35,070,000.00 USD | 0.00 USD | 743,110.00 USD | 705,120.00 USD | 935,330.00 USD |
| `1D` | `1.31` | 32,610,000.00 USD | 32,610,000.00 USD | 0.00 USD | 1,920,000.00 USD | 331,160.00 USD | 612,560.00 USD |
| `7D` | `1.31` | 38,160,000.00 USD | 38,160,000.00 USD | 0.00 USD | 1,900,000.00 USD | 430,030.00 USD | 759,020.00 USD |
| `1D` | `1.31` | 37,460,000.00 USD | 37,460,000.00 USD | 0.00 USD | 2,590,000.00 USD | 846,070.00 USD | 1,420,000.00 USD |
| `7D` | `1.31` | 41,680,000.00 USD | 41,680,000.00 USD | 0.00 USD | 1,800,000.00 USD | 1,070,000.00 USD | 651,540.00 USD |
| `1D` | `1.32` | 43,950,000.00 USD | 43,950,000.00 USD | 0.00 USD | 2,210,000.00 USD | 1,650,000.00 USD | 2,640,000.00 USD |
| `7D` | `1.32` | 46,090,000.00 USD | 46,090,000.00 USD | 0.00 USD | 1,920,000.00 USD | 1,120,000.00 USD | 1,370,000.00 USD |
| `1D` | `1.32` | 49,090,000.00 USD | 49,090,000.00 USD | 0.00 USD | 3,050,000.00 USD | 789,520.00 USD | 1,300,000.00 USD |
| `7D` | `1.32` | 48,580,000.00 USD | 48,580,000.00 USD | 0.00 USD | 731,560.00 USD | 193,040.00 USD | 1,560,000.00 USD |
| `1D` | `1.32` | 51,170,000.00 USD | 51,170,000.00 USD | 0.00 USD | 809,820.00 USD | 549,070.00 USD | 721,110.00 USD |
| `7D` | `1.32` | 49,360,000.00 USD | 49,360,000.00 USD | 0.00 USD | 526,160.00 USD | 230,290.00 USD | 29,560.00 USD |
| `1D` | `1.32` | 53,320,000.00 USD | 53,320,000.00 USD | 0.00 USD | 962,470.00 USD | 375,040.00 USD | 805,760.00 USD |
| `7D` | `1.32` | 51,660,000.00 USD | 51,660,000.00 USD | 0.00 USD | 1,140,000.00 USD | 371,730.00 USD | 783,260.00 USD |
| `1D` | `1.32` | 54,580,000.00 USD | 54,580,000.00 USD | 0.00 USD | 902,980.00 USD | 196,710.00 USD | 164,300.00 USD |
| `7D` | `1.32` | 52,900,000.00 USD | 52,900,000.00 USD | 0.00 USD | 811,770.00 USD | 194,320.00 USD | 231,250.00 USD |
| `1D` | `1.33` | 55,860,000.00 USD | 55,860,000.00 USD | 0.00 USD | 297,380.00 USD | 267,590.00 USD | 714,520.00 USD |
| `7D` | `1.33` | 53,150,000.00 USD | 53,150,000.00 USD | 0.00 USD | 197,140.00 USD | 0.00 USD | 53,600.00 USD |
| `1D` | `1.33` | 56,950,000.00 USD | 56,950,000.00 USD | 0.00 USD | 150,520.00 USD | 250,520.00 USD | 685,870.00 USD |
| `7D` | `1.33` | 53,700,000.00 USD | 53,700,000.00 USD | 0.00 USD | 14,750.00 USD | 10,370.00 USD | 522,090.00 USD |
| `1D` | `1.33` | 57,720,000.00 USD | 57,720,000.00 USD | 0.00 USD | 157,110.00 USD | 180,230.00 USD | 433,050.00 USD |
| `7D` | `1.33` | 54,470,000.00 USD | 54,470,000.00 USD | 0.00 USD | 0.00 USD | 268,860.00 USD | 500,050.00 USD |
| `1D` | `1.33` | 58,260,000.00 USD | 58,260,000.00 USD | 0.00 USD | 0.00 USD | 164,890.00 USD | 378,990.00 USD |
| `7D` | `1.33` | 55,920,000.00 USD | 55,920,000.00 USD | 0.00 USD | 610,090.00 USD | 0.00 USD | 840,910.00 USD |
| `1D` | `1.33` | 58,860,000.00 USD | 58,860,000.00 USD | 0.00 USD | 335,800.00 USD | 413.40 USD | 264,510.00 USD |
| `1D` | `1.34` | 60,240,000.00 USD | 60,240,000.00 USD | 0.00 USD | 662,270.00 USD | 128,780.00 USD | 585,910.00 USD |
| `7D` | `1.34` | 57,420,000.00 USD | 57,420,000.00 USD | 0.00 USD | 570,060.00 USD | 645,230.00 USD | 285,630.00 USD |
| `1D` | `1.34` | 63,510,000.00 USD | 63,510,000.00 USD | 0.00 USD | 1,620,000.00 USD | 405,560.00 USD | 1,250,000.00 USD |
| `7D` | `1.34` | 59,240,000.00 USD | 59,240,000.00 USD | 0.00 USD | 960,450.00 USD | 362,920.00 USD | 494,950.00 USD |
| `1D` | `1.34` | 67,870,000.00 USD | 67,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 466,350.00 USD | 2,030,000.00 USD |
| `7D` | `1.34` | 63,970,000.00 USD | 63,970,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD |
| `1D` | `1.34` | 71,340,000.00 USD | 71,340,000.00 USD | 0.00 USD | 1,420,000.00 USD | 853,290.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 69,600,000.00 USD | 69,600,000.00 USD | 0.00 USD | 1,720,000.00 USD | 2,830,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.34` | 75,670,000.00 USD | 75,670,000.00 USD | 0.00 USD | 2,340,000.00 USD | 667,740.00 USD | 1,320,000.00 USD |
| `7D` | `1.34` | 80,820,000.00 USD | 80,820,000.00 USD | 0.00 USD | 3,690,000.00 USD | 1,880,000.00 USD | 5,650,000.00 USD |
| `1D` | `1.35` | 78,020,000.00 USD | 78,020,000.00 USD | 0.00 USD | 997,910.00 USD | 467,820.00 USD | 888,620.00 USD |
| `7D` | `1.35` | 88,550,000.00 USD | 88,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 2,220,000.00 USD | 2,960,000.00 USD |
| `1D` | `1.35` | 79,670,000.00 USD | 79,670,000.00 USD | 0.00 USD | 796,750.00 USD | 258,460.00 USD | 593,340.00 USD |
| `7D` | `1.35` | 98,640,000.00 USD | 98,640,000.00 USD | 0.00 USD | 4,100,000.00 USD | 1,770,000.00 USD | 4,210,000.00 USD |
| `1D` | `1.35` | 82,120,000.00 USD | 82,120,000.00 USD | 0.00 USD | 993,350.00 USD | 294,820.00 USD | 1,160,000.00 USD |
| `7D` | `1.35` | 106,770,000.00 USD | 106,770,000.00 USD | 0.00 USD | 2,720,000.00 USD | 1,440,000.00 USD | 3,970,000.00 USD |
| `1D` | `1.35` | 83,280,000.00 USD | 83,280,000.00 USD | 0.00 USD | 488,380.00 USD | 201,800.00 USD | 472,100.00 USD |
| `7D` | `1.35` | 114,950,000.00 USD | 114,950,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,220,000.00 USD | 4,470,000.00 USD |
| `1D` | `1.35` | 85,320,000.00 USD | 85,320,000.00 USD | 0.00 USD | 833,710.00 USD | 345,300.00 USD | 855,080.00 USD |
| `7D` | `1.35` | 122,880,000.00 USD | 122,880,000.00 USD | 0.00 USD | 3,760,000.00 USD | 873,380.00 USD | 3,300,000.00 USD |
| `1D` | `1.36` | 86,820,000.00 USD | 86,820,000.00 USD | 0.00 USD | 578,590.00 USD | 148,190.00 USD | 770,760.00 USD |
| `7D` | `1.36` | 126,510,000.00 USD | 126,510,000.00 USD | 0.00 USD | 1,050,000.00 USD | 883,690.00 USD | 1,700,000.00 USD |
| `1D` | `1.36` | 87,690,000.00 USD | 87,690,000.00 USD | 0.00 USD | 680,830.00 USD | 73,510.00 USD | 115,610.00 USD |
| `7D` | `1.36` | 130,390,000.00 USD | 130,390,000.00 USD | 0.00 USD | 1,540,000.00 USD | 732,700.00 USD | 1,610,000.00 USD |
| `1D` | `1.36` | 88,090,000.00 USD | 88,090,000.00 USD | 0.00 USD | 188,490.00 USD | 104,800.00 USD | 115,490.00 USD |
| `7D` | `1.36` | 132,900,000.00 USD | 132,900,000.00 USD | 0.00 USD | 705,260.00 USD | 507,830.00 USD | 1,290,000.00 USD |
| `1D` | `1.36` | 88,910,000.00 USD | 88,910,000.00 USD | 0.00 USD | 386,600.00 USD | 133,350.00 USD | 297,860.00 USD |
| `7D` | `1.36` | 137,230,000.00 USD | 137,230,000.00 USD | 0.00 USD | 2,040,000.00 USD | 918,100.00 USD | 1,360,000.00 USD |
| `1D` | `1.36` | 90,130,000.00 USD | 90,130,000.00 USD | 0.00 USD | 452,510.00 USD | 269,500.00 USD | 495,450.00 USD |
| `7D` | `1.36` | 139,000,000.00 USD | 139,000,000.00 USD | 0.00 USD | 521,770.00 USD | 328,930.00 USD | 923,440.00 USD |
| `1D` | `1.37` | 90,480,000.00 USD | 90,480,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 252,650.00 USD |
| `7D` | `1.37` | 139,500,000.00 USD | 139,500,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD |
| `1D` | `1.37` | 90,860,000.00 USD | 90,860,000.00 USD | 0.00 USD | 139,480.00 USD | 116,910.00 USD | 127,390.00 USD |
| `7D` | `1.37` | 141,280,000.00 USD | 141,280,000.00 USD | 0.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD |
| `1D` | `1.37` | 91,430,000.00 USD | 91,430,000.00 USD | 0.00 USD | 120,300.00 USD | 80,070.00 USD | 364,550.00 USD |
| `7D` | `1.37` | 142,690,000.00 USD | 142,690,000.00 USD | 0.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD |
| `1D` | `1.37` | 92,020,000.00 USD | 92,020,000.00 USD | 0.00 USD | 147,360.00 USD | 112,420.00 USD | 333,550.00 USD |
| `7D` | `1.37` | 145,540,000.00 USD | 145,540,000.00 USD | 0.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD |
| `1D` | `1.37` | 92,270,000.00 USD | 92,270,000.00 USD | 0.00 USD | 172,450.00 USD | 10,690.00 USD | 66,850.00 USD |
| `7D` | `1.38` | 147,230,000.00 USD | 147,230,000.00 USD | 0.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD |
| `1D` | `1.38` | 92,630,000.00 USD | 92,630,000.00 USD | 0.00 USD | 123,150.00 USD | 46,920.00 USD | 190,660.00 USD |
| `7D` | `1.38` | 148,850,000.00 USD | 148,850,000.00 USD | 0.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 93,190,000.00 USD | 93,190,000.00 USD | 0.00 USD | 235,940.00 USD | 78,180.00 USD | 241,330.00 USD |
| `7D` | `1.38` | 150,790,000.00 USD | 150,790,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 93,960,000.00 USD | 93,960,000.00 USD | 0.00 USD | 379,220.00 USD | 97,470.00 USD | 295,250.00 USD |
| `7D` | `1.38` | 153,340,000.00 USD | 153,340,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 94,480,000.00 USD | 94,480,000.00 USD | 0.00 USD | 241,850.00 USD | 53,770.00 USD | 224,750.00 USD |
| `7D` | `1.38` | 154,420,000.00 USD | 154,420,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 94,910,000.00 USD | 94,910,000.00 USD | 0.00 USD | 340,420.00 USD | 36,760.00 USD | 56,890.00 USD |
| `7D` | `1.39` | 155,520,000.00 USD | 155,520,000.00 USD | 0.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 95,100,000.00 USD | 95,100,000.00 USD | 0.00 USD | 81,750.00 USD | 52,300.00 USD | 56,350.00 USD |
| `7D` | `1.39` | 156,010,000.00 USD | 156,010,000.00 USD | 0.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD |
| `1D` | `1.39` | 95,260,000.00 USD | 95,260,000.00 USD | 0.00 USD | 83,870.00 USD | 34,730.00 USD | 36,020.00 USD |
| `7D` | `1.39` | 157,100,000.00 USD | 157,100,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD |
| `1D` | `1.39` | 95,520,000.00 USD | 95,520,000.00 USD | 0.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD |
| `7D` | `1.39` | 157,260,000.00 USD | 157,260,000.00 USD | 0.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD |
| `7D` | `1.39` | 157,590,000.00 USD | 157,590,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 95,540,000.00 USD | 95,540,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.40` | 157,730,000.00 USD | 157,730,000.00 USD | 0.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 95,640,000.00 USD | 95,640,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 157,750,000.00 USD | 157,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 157,760,000.00 USD | 157,760,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 157,890,000.00 USD | 157,890,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 158,010,000.00 USD | 158,010,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 158,250,000.00 USD | 158,250,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 158,420,000.00 USD | 158,420,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 158,590,000.00 USD | 158,590,000.00 USD | 0.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD |
| `7D` | `1.41` | 158,740,000.00 USD | 158,740,000.00 USD | 0.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD |
| `7D` | `1.41` | 158,910,000.00 USD | 158,910,000.00 USD | 0.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.41` | 95,640,000.00 USD | 95,640,000.00 USD | 0.00 USD | 4,630.00 USD | 132.35 USD | 204.46 USD |
| `7D` | `1.42` | 159,410,000.00 USD | 159,410,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD |
| `1D` | `1.42` | 95,760,000.00 USD | 95,760,000.00 USD | 0.00 USD | 60,530.00 USD | 27,310.00 USD | 25,730.00 USD |
| `7D` | `1.42` | 159,840,000.00 USD | 159,840,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.42` | 96,080,000.00 USD | 96,080,000.00 USD | 0.00 USD | 176,350.00 USD | 69,040.00 USD | 79,970.00 USD |
| `7D` | `1.42` | 160,860,000.00 USD | 160,860,000.00 USD | 0.00 USD | 347,490.00 USD | 254,030.00 USD | 414,710.00 USD |
| `1D` | `1.42` | 96,790,000.00 USD | 96,790,000.00 USD | 0.00 USD | 360,460.00 USD | 147,590.00 USD | 199,700.00 USD |
| `7D` | `1.42` | 162,230,000.00 USD | 162,230,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.42` | 97,180,000.00 USD | 97,180,000.00 USD | 0.00 USD | 157,740.00 USD | 72,450.00 USD | 158,530.00 USD |
| `7D` | `1.42` | 162,850,000.00 USD | 162,850,000.00 USD | 0.00 USD | 204,250.00 USD | 165,260.00 USD | 248,940.00 USD |
| `1D` | `1.42` | 97,240,000.00 USD | 97,240,000.00 USD | 0.00 USD | 9,670.00 USD | 54,600.00 USD | 1,030.00 USD |
| `1D` | `1.43` | 97,330,000.00 USD | 97,330,000.00 USD | 0.00 USD | 29,370.00 USD | 27,060.00 USD | 28,790.00 USD |
| `7D` | `1.43` | 163,200,000.00 USD | 163,200,000.00 USD | 0.00 USD | 87,470.00 USD | 68,830.00 USD | 196,840.00 USD |
| `7D` | `1.43` | 164,100,000.00 USD | 164,100,000.00 USD | 0.00 USD | 243,040.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 165,700,000.00 USD | 165,700,000.00 USD | 0.00 USD | 315,770.00 USD | 292,810.00 USD | 991,730.00 USD |
| `7D` | `1.43` | 167,030,000.00 USD | 167,030,000.00 USD | 0.00 USD | 449,440.00 USD | 172,600.00 USD | 709,440.00 USD |
| `7D` | `1.43` | 167,710,000.00 USD | 167,710,000.00 USD | 0.00 USD | 282,820.00 USD | 57,330.00 USD | 336,880.00 USD |
| `7D` | `1.44` | 168,120,000.00 USD | 168,120,000.00 USD | 0.00 USD | 106,080.00 USD | 23,880.00 USD | 281,670.00 USD |
| `7D` | `1.44` | 168,130,000.00 USD | 168,130,000.00 USD | 0.00 USD | 0.00 USD | 12,030.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `3.04B` | Total OI Tokens: `2,353,513,305.0 XRP`
  * 1h OI Change: `+0.49%` | 4h OI Change: `+1.60%` | 24h OI Change: `+2.30%`
  * Exchange Breakdown: Binance=`495.67M` | Bybit=`327.62M` | OKX=`106.00M` | Hyperliquid=`225.03M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `52.38K` | Last 24h: `174.40K` | Last 3d: `625.14K` | Last 7d: `1.13M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0099%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0004%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0098%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0086%` | **USDT Bitget** | `0.0034%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `42.89%` | `57.11%` | `0.75` | 641,890,000.00 USD |
| `15M` | `Binance` | `37.98%` | `62.02%` | `0.61` | 252,730,000.00 USD |
| `15M` | `OKX` | `48.76%` | `51.24%` | `0.95` | 76,540,000.00 USD |
| `15M` | `Bybit` | `36.97%` | `63.03%` | `0.59` | 59,290,000.00 USD |
| `15M` | `KuCoin` | `45.08%` | `54.92%` | `0.82` | 1,740,000.00 USD |
| `15M` | `Gate` | `45.27%` | `54.73%` | `0.83` | 67,240,000.00 USD |
| `15M` | `Bitget` | `45.78%` | `54.22%` | `0.84` | 28,760,000.00 USD |
| `15M` | `BingX` | `51.74%` | `48.26%` | `1.07` | 8,500,000.00 USD |
| `15M` | `MEXC` | `45.24%` | `54.76%` | `0.83` | 30,850,000.00 USD |
| `15M` | `Bitunix` | `51.28%` | `48.72%` | `1.05` | 25,930,000.00 USD |
| `15M` | `Hyperliquid` | `48.25%` | `51.75%` | `0.93` | 22,030,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `81.28%` | `18.72%` | `4.34` | 6,300,000.00 USD |
| `15M` | `Crypto.com` | `45.67%` | `54.33%` | `0.84` | 6,650,000.00 USD |
| `15M` | `WhiteBIT` | `51.23%` | `48.77%` | `1.05` | 17,600,000.00 USD |
| `15M` | `HTX` | `40.04%` | `59.96%` | `0.67` | 2,350,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `48.3%` | `51.7%` | `0.93` | 10,990,000.00 USD |
| `15M` | `Bitfinex` | `35.76%` | `64.24%` | `0.56` | 345,040.00 USD |
| `15M` | `Kraken` | `70.1%` | `29.9%` | `2.34` | 2,720,000.00 USD |
| `15M` | `Aster` | `26.67%` | `73.33%` | `0.36` | 9,870,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.33%` | `53.67%` | `0.86` | 11,460,000.00 USD |
| `15M` | `Whale Positions` | `37.98%` | `62.02%` | `0.61` | 252,730,000.00 USD |
| `15M` | `Global Accounts` | `42.89%` | `57.11%` | `0.75` | 641,890,000.00 USD |
| `1H` | `XRP` | `43.09%` | `56.91%` | `0.76` | 2,560,000,000.00 USD |
| `1H` | `Binance` | `42.43%` | `57.57%` | `0.74` | 752,800,000.00 USD |
| `1H` | `OKX` | `46.01%` | `53.99%` | `0.85` | 443,930,000.00 USD |
| `1H` | `Bybit` | `40.32%` | `59.68%` | `0.68` | 195,570,000.00 USD |
| `1H` | `KuCoin` | `48.41%` | `51.59%` | `0.94` | 6,630,000.00 USD |
| `1H` | `Gate` | `49.48%` | `50.52%` | `0.98` | 387,750,000.00 USD |
| `1H` | `Bitget` | `51.56%` | `48.44%` | `1.06` | 138,000,000.00 USD |
| `1H` | `BingX` | `40.6%` | `59.4%` | `0.68` | 39,430,000.00 USD |
| `1H` | `MEXC` | `51.37%` | `48.63%` | `1.06` | 93,360,000.00 USD |
| `1H` | `Bitunix` | `44.1%` | `55.9%` | `0.79` | 90,990,000.00 USD |
| `1H` | `Hyperliquid` | `28.18%` | `71.82%` | `0.39` | 52,190,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `40.75%` | `59.25%` | `0.69` | 6,130,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `21.81%` | `78.19%` | `0.28` | 234,840,000.00 USD |
| `1H` | `HTX` | `54.85%` | `45.15%` | `1.21` | 30,570,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `51.17%` | `48.83%` | `1.05` | 5,300,000.00 USD |
| `1H` | `Bitfinex` | `39.93%` | `60.07%` | `0.66` | 962,000.00 USD |
| `1H` | `Kraken` | `67.71%` | `32.29%` | `2.10` | 17,520,000.00 USD |
| `1H` | `Aster` | `42.7%` | `57.3%` | `0.75` | 26,720,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.56%` | `49.44%` | `1.02` | 34,850,000.00 USD |
| `1H` | `Whale Positions` | `42.43%` | `57.57%` | `0.74` | 752,800,000.00 USD |
| `1H` | `Global Accounts` | `43.09%` | `56.91%` | `0.76` | 2,560,000,000.00 USD |
| `4H` | `XRP` | `49.17%` | `50.83%` | `0.97` | 11,730,000,000.00 USD |
| `4H` | `Binance` | `50.47%` | `49.53%` | `1.02` | 3,560,000,000.00 USD |
| `4H` | `OKX` | `51.16%` | `48.84%` | `1.05` | 2,260,000,000.00 USD |
| `4H` | `Bybit` | `52.03%` | `47.97%` | `1.08` | 874,990,000.00 USD |
| `4H` | `KuCoin` | `64.37%` | `35.63%` | `1.81` | 40,710,000.00 USD |
| `4H` | `Gate` | `50.54%` | `49.46%` | `1.02` | 1,890,000,000.00 USD |
| `4H` | `Bitget` | `49.72%` | `50.28%` | `0.99` | 592,640,000.00 USD |
| `4H` | `BingX` | `46%` | `54%` | `0.85` | 181,010,000.00 USD |
| `4H` | `MEXC` | `50.38%` | `49.62%` | `1.02` | 468,220,000.00 USD |
| `4H` | `Bitunix` | `48.52%` | `51.48%` | `0.94` | 435,790,000.00 USD |
| `4H` | `Hyperliquid` | `42.84%` | `57.16%` | `0.75` | 320,140,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.72%` | `51.28%` | `0.95` | 47,800,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `18.53%` | `81.47%` | `0.23` | 537,260,000.00 USD |
| `4H` | `HTX` | `68.65%` | `31.35%` | `2.19` | 182,910,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `47.25%` | `52.75%` | `0.90` | 42,690,000.00 USD |
| `4H` | `Bitfinex` | `43.53%` | `56.47%` | `0.77` | 2,800,000.00 USD |
| `4H` | `Kraken` | `65.97%` | `34.03%` | `1.94` | 55,480,000.00 USD |
| `4H` | `Aster` | `43.8%` | `56.2%` | `0.78` | 99,770,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.09%` | `52.91%` | `0.89` | 129,280,000.00 USD |
| `4H` | `Whale Positions` | `50.47%` | `49.53%` | `1.02` | 3,560,000,000.00 USD |
| `4H` | `Global Accounts` | `49.17%` | `50.83%` | `0.97` | 11,730,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 2,395,540.70 USD | 1,294,716.83 USD | 1,100,823.87 USD | 193,892.96 USD | `+8.09%` | `5B / 6S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 3,708,593.79 USD | 1,708,187.76 USD | 2,000,406.03 USD | -292,218.27 USD | `-7.88%` | `5B / 8S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 3,235,274.79 USD | 1,734,954.94 USD | 1,500,319.85 USD | 234,635.09 USD | `+7.25%` | `4B / 5S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 10,648,485.09 USD | 5,001,723.73 USD | 5,646,761.36 USD | -645,037.63 USD | `-6.06%` | `11B / 11S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 2,650,440.42 USD | 1,251,776.39 USD | 1,398,664.04 USD | -146,887.65 USD | `-5.54%` | `5B / 5S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 6,435,174.90 USD | 4,046,805.23 USD | 2,388,369.67 USD | 1,658,435.57 USD | `+25.77%` | `15B / 1S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.30` | `1.29` | 4,174,750.63 USD | 2,453,557.94 USD | 1,721,192.69 USD | 732,365.25 USD | `+17.54%` | `9B / 4S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 10,397,241.47 USD | 4,625,186.56 USD | 5,772,054.90 USD | -1,146,868.34 USD | `-11.03%` | `6B / 14S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 8,662,889.80 USD | 4,349,377.80 USD | 4,313,512.00 USD | 35,865.80 USD | `+0.41%` | `15B / 14S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 3,958,311.72 USD | 2,245,978.73 USD | 1,712,333.00 USD | 533,645.73 USD | `+13.48%` | `9B / 2S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:52` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.31` | 0.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 10M XRP` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1.32` | 2,000,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Volume 10M XRP` | `Trapped longs` | **`BEARISH`** | Failed breakout | `1.32` | 2,000,000.00 USD | 0.00 USD |
| `10-28 18:52` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.31` | 1,200,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.31` | 3,000,000.00 USD | 0.00 USD |
| `10-28 12:56` | `Range 0.005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1.32` | 0.00 USD | 0.00 USD |
| `10-28 10:21` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 3,600,000.00 USD | 0.00 USD |
| `10-28 08:33` | `Volume 10M XRP` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 2,100,000.00 USD | 0.00 USD |
| `10-28 08:12` | `Range 0.005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1.33` | 3,700,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 10M XRP` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.34` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.005` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `1.34` | 0.00 USD | 0.00 USD |
| `10-28 07:20` | `Volume 10M XRP` | `Divergence` | **`BULLISH`** | Drop without taker selling | `1.33` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -29,520.00 USD | -609,210.00 USD | **`DISTRIBUTION`** |
| `15m` | 280,510.00 USD | -1,160,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -796,690.00 USD | 28,400.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,170,000.00 USD | -8,830,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 183,280.00 USD | -9,180,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,940,000.00 USD | -2,140,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 454,090.00 USD | -4,920,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 715,710.00 USD | -3,070,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 43,860.00 USD | -9,010,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -13,180,000.00 USD | -44,120,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -72,230,000.00 USD | -81,640,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -549,200,000.00 USD | -1,170,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-29.52K` | 15m=`+280.51K` | 1h=`-2.17M` | 24h=`-13.18M`
* Futures Capital Netflows: 5m=`-609.21K` | 15m=`-1.16M` | 1h=`-8.83M` | 24h=`-44.12M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.28` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0140` pts)
  * +2.5R Take Profit: `1.32`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `0.0140` pts)
  * +2.5R Take Profit: `1.26`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.31`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
