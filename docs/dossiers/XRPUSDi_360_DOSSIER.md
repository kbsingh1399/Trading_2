# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:26:38 IST` (`2026-10-30 08:56:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.25`
- **Spread Points**: `3.00` | **Spread BPS**: `23.99 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `1.25` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.26` | Lower -3.00σ Band: `1.24`
  * Upper +2.51σ Band: `1.26` | Lower -2.51σ Band: `1.24`
  * Upper +2.01σ Band: `1.26` | Lower -2.01σ Band: `1.25`
  * Upper +2.00σ Band: `1.26` | Lower -2.00σ Band: `1.25`
  * Upper +1.28σ Band: `1.25` | Lower -1.28σ Band: `1.25`
  * Upper +1.00σ Band: `1.25` | Lower -1.00σ Band: `1.25`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.25`
  * Institutional Anchors: EMA-144=`1.25` | EMA-200=`1.25` (Slope: `+0.0000`) | EMA-233=`1.25`
- **Range Boundaries**: 24H High=`1.26` | 24H Low=`1.24` | Weekly High=`1.28` | Weekly Low=`1.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.88%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.04%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+1.52%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.27` | Low=`1.24`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.24`
  * Initial Balance (First Hour): IB High=`1.26` | IB Low=`1.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.25` - `1.26`
  * Optimal Trade Entry (OTE 0.705): `1.25`
  * Structural Invalidation Anchor (0.786): `1.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.25` | `1.26` | `1.25` | `1.25` | `1,727,821` | 2,166,989.58 USD | -324,064.88 USD | `-14.95%` | -39,593,443.13 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.25` | `1.26` | `1.25` | `1.25` | `1,137,802` | 1,426,452.77 USD | -253,839.12 USD | `-17.80%` | -39,847,282.25 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `282,191` | 353,518.56 USD | 62,034.49 USD | `+17.55%` | -39,785,247.76 USD | `+0.61` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `6,751,314` | 8,443,326.41 USD | -48,758.76 USD | `-0.58%` | -40,497,168.60 USD | `-0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `5,884,571` | 7,390,743.66 USD | 1,227,790.35 USD | `+16.61%` | -39,269,378.25 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `3,039,749` | 3,811,616.24 USD | -619,654.58 USD | `-16.26%` | -39,889,032.83 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.26` | `1.27` | `1.25` | `1.27` | `29,822,893` | 37,702,150.80 USD | 3,737,787.01 USD | `+9.91%` | -35,003,757.54 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.27` | `1.27` | `1.25` | `1.25` | `31,555,138` | 39,629,532.33 USD | -5,613,699.06 USD | `-14.17%` | -40,617,456.60 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.25` | `15,675,634` | 19,645,686.31 USD | 559,377.01 USD | `+2.85%` | -40,058,079.60 USD | `+0.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.25` | `1.25` | `15,676,725` | 19,647,053.23 USD | 558,010.09 USD | `+2.84%` | -38,723,518.84 USD | `+0.60` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -13,549,801.29 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -41,639,935.50 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.25` | `1.25` | `15,676,725` | 19,647,053.23 USD | 558,010.09 USD | `+2.84%` | -38,723,518.84 USD | `+0.60` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`1.25`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.25` | `271822.0000` | 340,783.24 USD | 2,477,343.20 USD | `7 orders` | `+0.16%` | `-` |
| `ASK` | `1.25` | `331775.0000` | 415,913.14 USD | 2,136,559.96 USD | `3 orders` | `+0.15%` | `-` |
| `ASK` | `1.25` | `33732.0000` | 42,283.06 USD | 1,720,646.82 USD | `8 orders` | `+0.14%` | `-` |
| `ASK` | `1.25` | `241862.0000` | 303,149.83 USD | 1,678,363.76 USD | `6 orders` | `+0.13%` | `-` |
| `ASK` | `1.25` | `50895.0000` | 63,786.70 USD | 1,375,213.93 USD | `10 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `67248.0000` | 84,275.19 USD | 1,311,427.22 USD | `20 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `48816.0000` | 61,171.33 USD | 1,227,152.03 USD | `12 orders` | `+0.11%` | `-` |
| `ASK` | `1.25` | `86888.0000` | 108,870.66 USD | 1,165,980.70 USD | `6 orders` | `+0.10%` | `-` |
| `ASK` | `1.25` | `109812.0000` | 137,583.45 USD | 1,057,110.04 USD | `11 orders` | `+0.09%` | `-` |
| `ASK` | `1.25` | `110528.0000` | 138,469.48 USD | 919,526.58 USD | `16 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `24548.0000` | 30,751.28 USD | 781,057.10 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `36543.0000` | 45,773.76 USD | 750,305.82 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `1.25` | `344281.0000` | 431,211.95 USD | 704,532.06 USD | `17 orders` | `+0.06%` | `-` |
| `ASK` | `1.25` | `61444.0000` | 76,952.47 USD | 273,320.11 USD | `15 orders` | `+0.05%` | `-` |
| `ASK` | `1.25` | `38102.0000` | 47,715.13 USD | 196,367.64 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `45815.0000` | 57,369.54 USD | 148,652.51 USD | `11 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `52863.0000` | 66,189.76 USD | 91,282.97 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `1.25` | `10035.0000` | 12,563.82 USD | 25,093.20 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `1.25` | `1179.0000` | 1,475.99 USD | 12,529.38 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `1.25` | `8830.0000` | 11,053.39 USD | 11,053.39 USD | `4 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.25` | `0.00%` | `-` |
| `BID` | `1.25` | `8794.0000` | 11,007.45 USD | 11,007.45 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `1.25` | `6307.0000` | 7,893.84 USD | 18,901.29 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `1.25` | `61836.0000` | 77,387.75 USD | 96,289.04 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `1.25` | `15782.0000` | 19,749.59 USD | 116,038.64 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `1.25` | `29214.0000` | 36,555.48 USD | 152,594.12 USD | `11 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `15946.0000` | 19,951.64 USD | 172,545.75 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `92129.0000` | 115,262.59 USD | 287,808.35 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `1.25` | `79521.0000` | 99,480.77 USD | 387,289.12 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `1.25` | `51412.0000` | 64,311.27 USD | 451,600.39 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `1.25` | `47611.0000` | 59,551.84 USD | 511,152.23 USD | `11 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `119208.0000` | 149,093.45 USD | 660,245.67 USD | `10 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `36218.0000` | 45,294.23 USD | 705,539.90 USD | `5 orders` | `-0.09%` | `-` |
| `BID` | `1.25` | `262663.0000` | 328,460.08 USD | 1,033,999.98 USD | `9 orders` | `-0.10%` | `-` |
| `BID` | `1.25` | `14134.0000` | 17,673.15 USD | 1,051,673.14 USD | `6 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `267734.0000` | 334,747.82 USD | 1,386,420.96 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `464081.0000` | 580,194.07 USD | 1,966,615.02 USD | `8 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `84555.0000` | 105,702.21 USD | 2,072,317.23 USD | `7 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `13435.0000` | 16,793.75 USD | 2,089,110.98 USD | `5 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `14249.0000` | 17,809.83 USD | 2,106,920.80 USD | `4 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `38602.0000` | 48,244.78 USD | 2,155,165.58 USD | `5 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 43,869,859.79 USD | `35,031,430.00` | `1.13` | `1.25` | `0.9612` | 4,290,976.52 USD | `+9.78%` | `10X Cross` |
| `90` | `0x5b5d...c060` | `SHORT` | 19,993,627.95 USD | `15,964,251.00` | `1.44` | `1.25` | `11.16` | 2,922,440.75 USD | `+14.62%` | `5X Cross` |
| `156` | `0xb83d...6e36` | `SHORT` | 13,218,590.04 USD | `10,555,450.00` | `1.50` | `1.25` | `13.51` | 2,603,979.61 USD | `+19.70%` | `5X Cross` |
| `347` | `0x58f0...0d20` | `LONG` | 6,644,548.04 USD | `5,307,147.00` | `1.24` | `1.25` | `1.22` | 41,704.54 USD | `+0.63%` | `20X Cross` |
| `383` | `0xecb6...2b00` | `SHORT` | 6,039,412.20 USD | `4,822,271.00` | `1.27` | `1.25` | `7.73` | 81,838.35 USD | `+1.36%` | `10X Cross` |
| `427` | `0xca49...53c8` | `SHORT` | 5,182,965.52 USD | `4,138,886.00` | `1.44` | `1.25` | `4.92` | 770,357.21 USD | `+14.86%` | `20X Cross` |
| `438` | `0xdd53...2b13` | `SHORT` | 5,006,240.44 USD | `3,998,914.00` | `1.40` | `1.25` | `16.83` | 590,635.67 USD | `+11.80%` | `3X Cross` |
| `507` | `0x610b...b613` | `LONG` | 4,437,020.39 USD | `3,543,946.00` | `1.44` | `1.25` | `0.8453` | -662,972.22 USD | `-14.94%` | `5X Cross` |
| `599` | `0x9946...0852` | `SHORT` | 3,843,937.67 USD | `3,070,483.00` | `1.40` | `1.25` | `1.77` | 464,564.55 USD | `+12.09%` | `20X Cross` |
| `645` | `0xc179...e0c8` | `SHORT` | 3,516,443.57 USD | `2,808,661.00` | `1.27` | `1.25` | `3.37` | 42,501.49 USD | `+1.21%` | `10X Cross` |
| `651` | `0xc30c...a4c9` | `SHORT` | 3,494,976.78 USD | `2,791,515.00` | `1.41` | `1.25` | `1.59` | 441,535.95 USD | `+12.63%` | `8X Cross` |
| `658` | `0xfc27...9d9d` | `SHORT` | 3,427,792.50 USD | `2,736,979.00` | `1.29` | `1.25` | `8.04` | 112,040.80 USD | `+3.27%` | `20X Cross` |
| `707` | `0xf48f...10fe` | `LONG` | 3,209,789.53 USD | `2,565,779.00` | `1.53` | `1.25` | `1.03` | -714,851.20 USD | `-22.27%` | `4X Cross` |
| `746` | `0x023a...2355` | `SHORT` | 3,084,126.72 USD | `2,463,360.00` | `1.32` | `1.25` | `3.35` | 166,801.53 USD | `+5.41%` | `20X Cross` |
| `755` | `0x45d2...4029` | `SHORT` | 3,070,420.10 USD | `2,453,000.00` | `1.48` | `1.25` | `18.86` | 567,860.32 USD | `+18.49%` | `20X Cross` |
| `1086` | `0xeadc...9d55` | `LONG` | 2,028,481.80 USD | `1,619,805.00` | `1.21` | `1.25` | `0.000000` | 69,638.78 USD | `+3.43%` | `20X Cross` |
| `1157` | `0x94b2...599e` | `SHORT` | 1,929,413.60 USD | `1,540,696.00` | `1.36` | `1.25` | `1.88` | 171,052.85 USD | `+8.87%` | `20X Cross` |
| `1179` | `0x3fc5...c0c1` | `SHORT` | 1,892,747.31 USD | `1,511,779.00` | `1.52` | `1.25` | `2.43` | 398,867.29 USD | `+21.07%` | `20X Cross` |
| `1199` | `0x31ef...f715` | `LONG` | 1,846,800.16 USD | `1,475,080.00` | `1.49` | `1.25` | `1.04` | -352,465.24 USD | `-19.09%` | `3X Isolated` |
| `1264` | `0x7737...bf66` | `SHORT` | 1,770,083.47 USD | `1,413,466.00` | `1.41` | `1.25` | `14.03` | 228,785.18 USD | `+12.93%` | `10X Cross` |
| `1319` | `0x95da...2328` | `LONG` | 1,658,744.75 USD | `1,324,876.00` | `1.35` | `1.25` | `0.0981` | -134,896.35 USD | `-8.13%` | `5X Cross` |
| `1337` | `0xee2b...d67e` | `LONG` | 1,635,336.94 USD | `1,306,284.00` | `1.55` | `1.25` | `0.4318` | -395,317.96 USD | `-24.17%` | `4X Cross` |
| `1378` | `0x215d...f80a` | `LONG` | 1,567,600.34 USD | `1,251,777.00` | `1.32` | `1.25` | `1.13` | -86,853.89 USD | `-5.54%` | `14X Cross` |
| `1410` | `0x5fa3...35b7` | `SHORT` | 1,553,667.25 USD | `1,240,651.00` | `1.30` | `1.25` | `2.66` | 62,824.89 USD | `+4.04%` | `20X Cross` |
| `1443` | `0x123d...3bff` | `LONG` | 1,517,285.03 USD | `1,211,889.00` | `1.35` | `1.25` | `0.000000` | -115,150.45 USD | `-7.59%` | `10X Cross` |
| `1461` | `0xbcd4...0dd2` | `SHORT` | 1,497,907.34 USD | `1,196,125.00` | `1.31` | `1.25` | `2.05` | 69,759.90 USD | `+4.66%` | `20X Cross` |
| `1556` | `0x7fda...17d1` | `LONG` | 1,387,212.09 USD | `1,107,643.00` | `1.22` | `1.25` | `0.000000` | 38,045.45 USD | `+2.74%` | `20X Cross` |
| `1566` | `0xdf95...7d72` | `SHORT` | 1,377,682.78 USD | `1,100,122.00` | `1.37` | `1.25` | `36.81` | 132,459.61 USD | `+9.61%` | `20X Cross` |
| `1614` | `0x9a31...6525` | `LONG` | 1,326,301.67 USD | `1,059,431.00` | `1.25` | `1.25` | `0.1472` | -978.11 USD | `-0.07%` | `5X Cross` |
| `1645` | `0xef96...9383` | `SHORT` | 1,298,029.78 USD | `1,036,765.00` | `1.34` | `1.25` | `4.66` | 89,489.57 USD | `+6.89%` | `20X Cross` |
| `1664` | `0xb1ce...681b` | `LONG` | 1,278,942.00 USD | `1,021,764.00` | `1.49` | `1.25` | `1.16` | -245,114.50 USD | `-19.17%` | `4X Isolated` |
| `1772` | `0x3c36...461a` | `LONG` | 1,176,849.85 USD | `940,051.00` | `1.30` | `1.25` | `1.05` | -42,230.77 USD | `-3.59%` | `10X Cross` |
| `1912` | `0x2577...4897` | `SHORT` | 1,060,744.44 USD | `847,037.00` | `1.24` | `1.25` | `5.13` | -7,881.57 USD | `-0.74%` | `20X Cross` |
| `2012` | `0xbfc7...80b4` | `SHORT` | 1,001,840.00 USD | `800,000.00` | `1.48` | `1.25` | `3.21` | 181,614.65 USD | `+18.13%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2938 USD [API] | `2026-10-29 08:19:36` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2938 USD [API] | `2026-10-29 08:19:36` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2928 USD [API] | `2026-10-29 08:22:42` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,074.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.07K USD at 1.2920 USD [API] | `2026-10-29 08:36:41` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,896.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.90K USD at 1.2920 USD [API] | `2026-10-29 08:36:41` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,836.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.84K USD at 1.2916 USD [API] | `2026-10-29 09:05:03` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2916 USD [API] | `2026-10-29 09:05:03` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2948 USD [API] | `2026-10-29 09:09:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 2,965.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.97K USD at 1.3149 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,167.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.17K USD at 1.3149 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,999.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3149 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,167.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.17K USD at 1.3150 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,998.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3150 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 65.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.3150 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 77.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.08K USD at 1.3150 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,890.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.89K USD at 1.3151 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 4,209.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.21K USD at 1.3151 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 3,999.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3151 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 1,562.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.56K USD at 1.3151 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 4,209.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.21K USD at 1.3152 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 3,999.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3152 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,140.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.14K USD at 1.3009 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,998.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3009 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 166.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3009 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 9,520.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.52K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 9,520.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.52K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 50.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,999.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,127.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.13K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 640.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.64K USD at 1.3656 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 501.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3656 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,998.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3657 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,999.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3658 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 19,998.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 20.00K USD at 1.3658 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 868.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.87K USD at 1.3658 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 9,316.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.32K USD at 1.4543 USD [API] | `2026-10-07 02:01:14` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 261.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.26K USD at 1.4543 USD [API] | `2026-10-07 02:01:14` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 2,056.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.06K USD at 1.4544 USD [API] | `2026-10-07 02:01:14` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 8,237.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.24K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 20.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 6,140.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.14K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 399.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,725.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.73K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,441.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.44K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,998.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 2,103.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.10K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 411.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.41K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,176.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.18K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 20.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,998.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 49.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,999.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3729 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 399.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3730 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 189.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.19K USD at 1.3730 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 199.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.20K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 2,911.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.91K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 5,004.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 58.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.06K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 2,990.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.99K USD at 1.2533 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 30.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.03K USD at 1.2533 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 2,981.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.98K USD at 1.2533 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,394.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.39K USD at 1.2925 USD [API] | `2026-10-29 09:16:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,645.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.65K USD at 1.2925 USD [API] | `2026-10-29 09:16:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,074.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.07K USD at 1.2927 USD [API] | `2026-10-29 09:17:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,064.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.06K USD at 1.2894 USD [API] | `2026-10-29 09:35:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,778.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.78K USD at 1.2894 USD [API] | `2026-10-29 09:35:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 8,858.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.86K USD at 1.2892 USD [API] | `2026-10-29 09:36:34` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2906 USD [API] | `2026-10-29 09:41:44` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,461.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.46K USD at 1.3409 USD [API] | `2026-10-14 14:11:09` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,195.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.20K USD at 1.3409 USD [API] | `2026-10-14 14:11:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 929.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.93K USD at 1.4622 USD [API] | `2026-10-07 02:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 11,087.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.09K USD at 1.2901 USD [API] | `2026-10-29 09:43:08` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 13,935.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.94K USD at 1.2901 USD [API] | `2026-10-29 09:47:30` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,122.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.12K USD at 1.2887 USD [API] | `2026-10-29 10:13:41` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2875 USD [API] | `2026-10-29 10:29:08` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,472.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.47K USD at 1.2902 USD [API] | `2026-10-29 10:34:37` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,443.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.44K USD at 1.2920 USD [API] | `2026-10-29 10:38:44` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2920 USD [API] | `2026-10-29 10:38:44` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 16,342.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 16.34K USD at 1.2905 USD [API] | `2026-10-29 10:43:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,104.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.10K USD at 1.2905 USD [API] | `2026-10-29 10:43:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2931 USD [API] | `2026-10-29 10:46:40` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 14.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 44.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 11.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 154.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,957.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.96K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 70.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 47.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,567.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.57K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 355.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.36K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 19.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 90.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 11.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,358.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.36K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 187.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.19K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 982.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.98K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 146.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,959.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.96K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2901 USD [API] | `2026-10-29 11:31:10` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,414.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.41K USD at 1.2902 USD [API] | `2026-10-29 11:31:10` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,159.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.16K USD at 1.2911 USD [API] | `2026-10-29 11:32:13` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,498.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.50K USD at 1.2924 USD [API] | `2026-10-29 11:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 8,228.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.23K USD at 1.2907 USD [API] | `2026-10-29 12:29:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,227.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.23K USD at 1.2906 USD [API] | `2026-10-29 12:29:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 20,952.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 20.95K USD at 1.2864 USD [API] | `2026-10-29 12:35:14` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,749.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.75K USD at 1.2923 USD [API] | `2026-10-29 12:44:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2913 USD [API] | `2026-10-29 12:45:48` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,573.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.57K USD at 1.2897 USD [API] | `2026-10-29 12:47:36` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,553.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.55K USD at 1.2906 USD [API] | `2026-10-29 12:49:50` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,463.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.46K USD at 1.2926 USD [API] | `2026-10-29 13:06:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2918 USD [API] | `2026-10-29 13:05:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,869.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.87K USD at 1.2918 USD [API] | `2026-10-29 13:05:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 65.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2866 USD [API] | `2026-10-29 04:06:15` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2882 USD [API] | `2026-10-29 04:02:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,106.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.11K USD at 1.2882 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 68.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2890 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,721.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.72K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 104.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 478.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.48K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 96.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2894 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,805.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.81K USD at 1.2926 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,029.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.03K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 192.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.19K USD at 1.2984 USD [API] | `2026-10-29 01:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 493.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.49K USD at 1.2984 USD [API] | `2026-10-29 01:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 131.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.13K USD at 1.2984 USD [API] | `2026-10-29 01:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 238.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.24K USD at 1.3016 USD [API] | `2026-10-29 01:48:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 101.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.3016 USD [API] | `2026-10-29 01:48:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 396.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.40K USD at 1.2920 USD [API] | `2026-10-29 06:47:28` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,558.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.56K USD at 1.2921 USD [API] | `2026-10-29 13:07:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 15,294.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 15.29K USD at 1.2949 USD [API] | `2026-10-29 13:17:10` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 17,335.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 17.34K USD at 1.2929 USD [API] | `2026-10-29 13:18:15` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,263.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.26K USD at 1.2931 USD [API] | `2026-10-29 13:23:39` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2941 USD [API] | `2026-10-29 13:29:53` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,825.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.83K USD at 1.2903 USD [API] | `2026-10-29 13:33:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2886 USD [API] | `2026-10-29 13:47:02` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,409.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.41K USD at 1.2897 USD [API] | `2026-10-29 13:53:35` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 972.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.97K USD at 1.3018 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 489.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.49K USD at 1.3715 USD [API] | `2026-10-12 14:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 1,001.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.00K USD at 1.3776 USD [API] | `2026-10-08 15:15:00` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 11.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.4139 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 500.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4139 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 3,286.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.29K USD at 1.4140 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 398.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.4141 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 551.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.55K USD at 1.5100 USD [API] | `2026-09-29 15:27:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,115.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.12K USD at 1.2939 USD [API] | `2026-10-29 13:59:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2916 USD [API] | `2026-10-29 14:12:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2923 USD [API] | `2026-10-29 14:13:41` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.48%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.22%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+5.70%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.23%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+7.87%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.23%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 2,900,000.00 USD, Dist: `+7.76%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.23%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 827.48 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 1,400.00 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,090.00 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 3,800.00 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 120.36 USD | 64,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 122.00 USD | 64,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 16,150.00 USD | 64,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 19,750.00 USD | 64,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 59,960.00 USD | 64,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 439.88 USD | 64,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 8,430.00 USD | 64,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 4,990.00 USD | 64,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 6,590.00 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 269.50 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 2,640.00 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 688,700.00 USD | 64,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 23,930.00 USD | 63,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 16,860.00 USD | 63,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 1,540.00 USD | 63,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 5,160.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 283.72 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 1,480.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 1,160.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 12,250.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 14,270.00 USD | 63,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 966.75 USD | 63,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 159,160.00 USD | 63,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 720.39 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 7,030.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 7,770.00 USD | 63,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 3,310.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 4,540.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 27,410.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 31,360.00 USD | 63,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,130.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 10,810.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,650.00 USD | 63,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 2,310.00 USD | 63,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 18,150.00 USD | 63,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 26,710.00 USD | 63,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 6,600.00 USD | 63,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 194,370.00 USD | 63,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 24,740.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 86,300.00 USD | 63,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 216,840.00 USD | 62,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 44,260.00 USD | 62,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 111,510.00 USD | 62,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 147,570.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 62,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 7,110.00 USD | 62,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 16,330.00 USD | 62,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 508,640.00 USD | 62,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 5,330.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 77,140.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 6,620.00 USD | 61,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 3,000,000.00 USD | 61,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 59,990.00 USD | 58,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 75,770.00 USD | 58,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 22,360.00 USD | 58,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 95,970.00 USD | 58,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 367,410.00 USD | 58,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 96,190.00 USD | 58,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 137,830.00 USD | 58,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 134,950.00 USD | 57,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 79,310.00 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 92,190.00 USD | 57,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 55,870.00 USD | 57,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 156,170.00 USD | 57,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,890,000.00 USD | 57,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 152,440.00 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 452,590.00 USD | 23,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 117,230.00 USD | 22,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 497,840.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 287,950.00 USD | 22,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 2,680,000.00 USD | 22,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,130,000.00 USD | 19,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 180,980.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,650,000.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 382,300.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 99,100,000.00 USD | 99,100,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 1,310,000.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 176,480.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 99,090,000.00 USD | 99,090,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 99,050,000.00 USD | 99,050,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 98,950,000.00 USD | 98,950,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 390,190.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 98,910,000.00 USD | 98,910,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 98,910,000.00 USD | 98,910,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 98,620,000.00 USD | 98,620,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 109,910.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 98,620,000.00 USD | 98,620,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 98,620,000.00 USD | 98,620,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 98,620,000.00 USD | 98,620,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 578,850.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,560,000.00 USD | 98,560,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,550,000.00 USD | 98,550,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,470,000.00 USD | 98,470,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 90,300,000.00 USD | 90,300,000.00 USD | 25,830.00 USD | 44,000.00 USD | 175,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,450,000.00 USD | 98,450,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 90,060,000.00 USD | 90,060,000.00 USD | 97,300.00 USD | 49,730.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,180,000.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.13` | 98,240,000.00 USD | 98,240,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 89,740,000.00 USD | 89,740,000.00 USD | 31,450.00 USD | 41,790.00 USD | 153,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 98,090,000.00 USD | 98,090,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 89,510,000.00 USD | 89,510,000.00 USD | 71,920.00 USD | 76,730.00 USD | 192,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 97,890,000.00 USD | 97,890,000.00 USD | 5,450.00 USD | 55,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 89,170,000.00 USD | 89,170,000.00 USD | 6,330.00 USD | 101,970.00 USD | 318,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 97,830,000.00 USD | 97,830,000.00 USD | 69,750.00 USD | 93,260.00 USD | 108,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 88,740,000.00 USD | 88,740,000.00 USD | 88,690.00 USD | 39,080.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 97,560,000.00 USD | 97,560,000.00 USD | 74,920.00 USD | 99,410.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 88,570,000.00 USD | 88,570,000.00 USD | 4,270.00 USD | 151,320.00 USD | 175,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 165,490.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.14` | 97,160,000.00 USD | 97,160,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 88,240,000.00 USD | 88,240,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,620,000.00 USD | 96,620,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 88,010,000.00 USD | 88,010,000.00 USD | 26,280.00 USD | 52,050.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,600,000.00 USD | 96,600,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 87,830,000.00 USD | 87,830,000.00 USD | 29,510.00 USD | 10,830.00 USD | 153,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,250,000.00 USD | 96,250,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 87,640,000.00 USD | 87,640,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,110,000.00 USD | 96,110,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 87,490,000.00 USD | 87,490,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 280,040.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 96,100,000.00 USD | 96,100,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 96,040,000.00 USD | 96,040,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 87,460,000.00 USD | 87,460,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 95,670,000.00 USD | 95,670,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 95,510,000.00 USD | 95,510,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 87,440,000.00 USD | 87,440,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 95,350,000.00 USD | 95,350,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 87,240,000.00 USD | 87,240,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 359,890.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 94,470,000.00 USD | 94,470,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 86,900,000.00 USD | 86,900,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 94,240,000.00 USD | 94,240,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 86,780,000.00 USD | 86,780,000.00 USD | 125,390.00 USD | 15,500.00 USD | 445,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 93,370,000.00 USD | 93,370,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 86,190,000.00 USD | 86,190,000.00 USD | 196,310.00 USD | 74,700.00 USD | 134,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 92,290,000.00 USD | 92,290,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 85,780,000.00 USD | 85,780,000.00 USD | 189,220.00 USD | 289,860.00 USD | 292,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 90,990,000.00 USD | 90,990,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 85,010,000.00 USD | 85,010,000.00 USD | 73,960.00 USD | 29,590.00 USD | 473,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,300,000.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 89,320,000.00 USD | 89,320,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 84,430,000.00 USD | 84,430,000.00 USD | 121,070.00 USD | 109,760.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 87,980,000.00 USD | 87,980,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 84,100,000.00 USD | 84,100,000.00 USD | 101,220.00 USD | 95,020.00 USD | 206,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 86,910,000.00 USD | 86,910,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 83,700,000.00 USD | 83,700,000.00 USD | 361,890.00 USD | 3,910.00 USD | 415,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 84,870,000.00 USD | 84,870,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 82,920,000.00 USD | 82,920,000.00 USD | 104,550.00 USD | 79,710.00 USD | 338,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 83,670,000.00 USD | 83,670,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 82,390,000.00 USD | 82,390,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 274,310.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 82,100,000.00 USD | 82,100,000.00 USD | 181,850.00 USD | 71,240.00 USD | 372,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 81,440,000.00 USD | 81,440,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 81,480,000.00 USD | 81,480,000.00 USD | 85,020.00 USD | 73,410.00 USD | 483,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 81,070,000.00 USD | 81,070,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 80,830,000.00 USD | 80,830,000.00 USD | 267,580.00 USD | 134,360.00 USD | 200,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 80,740,000.00 USD | 80,740,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 80,230,000.00 USD | 80,230,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 80,570,000.00 USD | 80,570,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 79,960,000.00 USD | 79,960,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,740,000.00 USD | 79,740,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 568,290.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 78,860,000.00 USD | 78,860,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,310,000.00 USD | 79,310,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 78,010,000.00 USD | 78,010,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 78,030,000.00 USD | 78,030,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 77,220,000.00 USD | 77,220,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 76,290,000.00 USD | 76,290,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 76,240,000.00 USD | 76,240,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 75,800,000.00 USD | 75,800,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 74,880,000.00 USD | 74,880,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 74,700,000.00 USD | 74,700,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 607,930.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 74,050,000.00 USD | 74,050,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 72,120,000.00 USD | 72,120,000.00 USD | 748,570.00 USD | 87,450.00 USD | 794,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 72,470,000.00 USD | 72,470,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 70,490,000.00 USD | 70,490,000.00 USD | 179,370.00 USD | 934,870.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 69,460,000.00 USD | 69,460,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 67,860,000.00 USD | 67,860,000.00 USD | 873,590.00 USD | 570,220.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 68,000,000.00 USD | 68,000,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 64,400,000.00 USD | 64,400,000.00 USD | 328,320.00 USD | 134,770.00 USD | 839,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 67,120,000.00 USD | 67,120,000.00 USD | 47,500.00 USD | 723,100.00 USD | 155,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 63,100,000.00 USD | 63,100,000.00 USD | 363,980.00 USD | 920,650.00 USD | 376,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 11,860.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 66,200,000.00 USD | 66,200,000.00 USD | 0.00 USD | 77,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 61,440,000.00 USD | 61,440,000.00 USD | 866,390.00 USD | 210,790.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 66,120,000.00 USD | 66,120,000.00 USD | 556,190.00 USD | 0.00 USD | 387,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 58,570,000.00 USD | 58,570,000.00 USD | 1,680,000.00 USD | 245,020.00 USD | 950,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 65,180,000.00 USD | 65,180,000.00 USD | 257,960.00 USD | 498,260.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 55,700,000.00 USD | 55,700,000.00 USD | 205,850.00 USD | 723,700.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 61,330,000.00 USD | 61,330,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 52,860,000.00 USD | 52,860,000.00 USD | 1,480,000.00 USD | 334,090.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 59,080,000.00 USD | 59,080,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 49,750,000.00 USD | 49,750,000.00 USD | 56,590.00 USD | 268,640.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 54,190.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 57,550,000.00 USD | 57,550,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 48,410,000.00 USD | 48,410,000.00 USD | 307,460.00 USD | 66,380.00 USD | 536,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 57,150,000.00 USD | 57,150,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 47,500,000.00 USD | 47,500,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 56,410,000.00 USD | 56,410,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 47,240,000.00 USD | 47,240,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,330,000.00 USD | 55,330,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 46,550,000.00 USD | 46,550,000.00 USD | 124,230.00 USD | 5,400.00 USD | 359,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,150,000.00 USD | 55,150,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 46,060,000.00 USD | 46,060,000.00 USD | 586,370.00 USD | 613,210.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,610,000.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 54,900,000.00 USD | 54,900,000.00 USD | 112,770.00 USD | 802,580.00 USD | 482,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 41,680,000.00 USD | 41,680,000.00 USD | 213,750.00 USD | 267,560.00 USD | 415,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 53,500,000.00 USD | 53,500,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 40,780,000.00 USD | 40,780,000.00 USD | 624,850.00 USD | 1,170,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 52,460,000.00 USD | 52,460,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 36,170,000.00 USD | 36,170,000.00 USD | 202,670.00 USD | 1,290,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 50,000,000.00 USD | 50,000,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 31,700,000.00 USD | 31,700,000.00 USD | 1,550,000.00 USD | 677,020.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 46,310,000.00 USD | 46,310,000.00 USD | 1,660,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 26,800,000.00 USD | 26,800,000.00 USD | 424,470.00 USD | 1,530,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 62,550.00 USD | 62,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 38,970,000.00 USD | 38,970,000.00 USD | 2,040,000.00 USD | 1,820,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 22,700,000.00 USD | 22,700,000.00 USD | 283,950.00 USD | 567,990.00 USD | 632,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 32,370,000.00 USD | 32,370,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 21,210,000.00 USD | 21,210,000.00 USD | 831,940.00 USD | 955,200.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 22,940,000.00 USD | 22,940,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,400,000.00 USD | 16,400,000.00 USD | 843,320.00 USD | 564,910.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 18,360,000.00 USD | 18,360,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 13,010,000.00 USD | 13,010,000.00 USD | 828,020.00 USD | 969,790.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 15,640,000.00 USD | 15,640,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 8,320,000.00 USD | 8,320,000.00 USD | 1,700,000.00 USD | 472,540.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 12,440,000.00 USD | 12,440,000.00 USD | 3,770,000.00 USD | 337,070.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 4,860,000.00 USD | 4,860,000.00 USD | 1,020,000.00 USD | 769,380.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 6,040,000.00 USD | 6,040,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 712,500.00 USD | 652,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 489,680.00 USD | 489,680.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 3,370.00 USD | 3,370.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 63,660.00 USD | 63,660.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 258,050.00 USD | 258,050.00 USD | 0.00 USD | 12,640.00 USD | 242,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 222,480.00 USD | 222,480.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 343,310.00 USD | 343,310.00 USD | 73,940.00 USD | 11,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 242,310.00 USD | 242,310.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 379,460.00 USD | 379,460.00 USD | 0.00 USD | 24,960.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 334,770.00 USD | 334,770.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 631,340.00 USD | 631,340.00 USD | 229,640.00 USD | 8,660.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 482,320.00 USD | 482,320.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,510,000.00 USD | 2,510,000.00 USD | 409,480.00 USD | 308,120.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 542,940.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 4,120,000.00 USD | 4,120,000.00 USD | 549,850.00 USD | 423,290.00 USD | 643,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 1,010.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.27` | 6,340,000.00 USD | 6,340,000.00 USD | 4,260,000.00 USD | 9,150.00 USD | 20,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 5,810,000.00 USD | 5,810,000.00 USD | 845,960.00 USD | 161,980.00 USD | 682,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 1,870,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 10,030,000.00 USD | 10,030,000.00 USD | 715,560.00 USD | 1,940,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 16,110,000.00 USD | 16,110,000.00 USD | 138,500.00 USD | 2,750,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 15,330,000.00 USD | 15,330,000.00 USD | 734,620.00 USD | 1,400,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 24,190,000.00 USD | 24,190,000.00 USD | 1,680,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 21,280,000.00 USD | 21,280,000.00 USD | 2,180,000.00 USD | 1,080,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 40,430,000.00 USD | 40,430,000.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 29,490,000.00 USD | 29,490,000.00 USD | 1,130,000.00 USD | 2,630,000.00 USD | 4,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 5,670.00 USD | 6,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.28` | 55,300,000.00 USD | 55,300,000.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 37,020,000.00 USD | 37,020,000.00 USD | 2,170,000.00 USD | 1,630,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 74,460,000.00 USD | 74,460,000.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 7,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 45,970,000.00 USD | 45,970,000.00 USD | 2,540,000.00 USD | 2,300,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 77,560,000.00 USD | 77,560,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 49,760,000.00 USD | 49,760,000.00 USD | 393,830.00 USD | 759,560.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 79,580,000.00 USD | 79,580,000.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 53,580,000.00 USD | 53,580,000.00 USD | 1,330,000.00 USD | 472,310.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 83,170,000.00 USD | 83,170,000.00 USD | 1,100,000.00 USD | 1,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 56,960,000.00 USD | 56,960,000.00 USD | 817,320.00 USD | 640,040.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 6,190.00 USD | 12,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.29` | 87,740,000.00 USD | 87,740,000.00 USD | 796,960.00 USD | 1,300,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 59,960,000.00 USD | 59,960,000.00 USD | 864,310.00 USD | 1,100,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 88,460,000.00 USD | 88,460,000.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 61,090,000.00 USD | 61,090,000.00 USD | 454,460.00 USD | 148,440.00 USD | 518,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 90,070,000.00 USD | 90,070,000.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 62,460,000.00 USD | 62,460,000.00 USD | 186,090.00 USD | 270,800.00 USD | 919,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 92,660,000.00 USD | 92,660,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 66,270,000.00 USD | 66,270,000.00 USD | 570,020.00 USD | 278,090.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 96,310,000.00 USD | 96,310,000.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 72,430,000.00 USD | 72,430,000.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 51,250.00 USD | 64,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 103,600,000.00 USD | 103,600,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 75,010,000.00 USD | 75,010,000.00 USD | 554,720.00 USD | 706,700.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 105,550,000.00 USD | 105,550,000.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 75,840,000.00 USD | 75,840,000.00 USD | 401,840.00 USD | 109,620.00 USD | 312,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 107,920,000.00 USD | 107,920,000.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 78,730,000.00 USD | 78,730,000.00 USD | 674,250.00 USD | 469,750.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 108,950,000.00 USD | 108,950,000.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 80,700,000.00 USD | 80,700,000.00 USD | 774,950.00 USD | 645,090.00 USD | 554,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 111,760,000.00 USD | 111,760,000.00 USD | 0.00 USD | 2,170,000.00 USD | 635,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 82,180,000.00 USD | 82,180,000.00 USD | 372,370.00 USD | 649,450.00 USD | 458,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,630.00 USD | 65,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 113,770,000.00 USD | 113,770,000.00 USD | 1,770,000.00 USD | 238,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 85,160,000.00 USD | 85,160,000.00 USD | 777,430.00 USD | 253,070.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 118,930,000.00 USD | 118,930,000.00 USD | 1,550,000.00 USD | 821,310.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 88,800,000.00 USD | 88,800,000.00 USD | 1,240,000.00 USD | 442,560.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 121,340,000.00 USD | 121,340,000.00 USD | 1,340,000.00 USD | 414,180.00 USD | 647,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 91,380,000.00 USD | 91,380,000.00 USD | 944,800.00 USD | 557,880.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 126,220,000.00 USD | 126,220,000.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 93,300,000.00 USD | 93,300,000.00 USD | 515,120.00 USD | 340,250.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 127,510,000.00 USD | 127,510,000.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 95,440,000.00 USD | 95,440,000.00 USD | 438,320.00 USD | 320,320.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 62,960.00 USD | 128,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.32` | 132,220,000.00 USD | 132,220,000.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,590,000.00 USD | 100,590,000.00 USD | 1,280,000.00 USD | 787,490.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 137,320,000.00 USD | 137,320,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 105,340,000.00 USD | 105,340,000.00 USD | 1,560,000.00 USD | 684,990.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 139,350,000.00 USD | 139,350,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 107,890,000.00 USD | 107,890,000.00 USD | 1,340,000.00 USD | 339,190.00 USD | 867,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,700,000.00 USD | 142,700,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 110,800,000.00 USD | 110,800,000.00 USD | 885,300.00 USD | 460,840.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 145,480,000.00 USD | 145,480,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 111,800,000.00 USD | 111,800,000.00 USD | 599,940.00 USD | 61,650.00 USD | 341,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 7,390.00 USD | 136,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 147,280,000.00 USD | 147,280,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 112,880,000.00 USD | 112,880,000.00 USD | 412,050.00 USD | 225,260.00 USD | 436,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 148,380,000.00 USD | 148,380,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 114,250,000.00 USD | 114,250,000.00 USD | 504,110.00 USD | 72,470.00 USD | 798,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 150,100,000.00 USD | 150,100,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 116,420,000.00 USD | 116,420,000.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 152,560,000.00 USD | 152,560,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 118,380,000.00 USD | 118,380,000.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 154,590,000.00 USD | 154,590,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 119,710,000.00 USD | 119,710,000.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 44,630.00 USD | 180,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 156,130,000.00 USD | 156,130,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 120,450,000.00 USD | 120,450,000.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 158,570,000.00 USD | 158,570,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 121,050,000.00 USD | 121,050,000.00 USD | 179,460.00 USD | 82,510.00 USD | 332,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 160,430,000.00 USD | 160,430,000.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 122,360,000.00 USD | 122,360,000.00 USD | 630,370.00 USD | 243,030.00 USD | 439,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 165,890,000.00 USD | 165,890,000.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 123,920,000.00 USD | 123,920,000.00 USD | 712,070.00 USD | 240,640.00 USD | 606,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 173,020,000.00 USD | 173,020,000.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 125,230,000.00 USD | 125,230,000.00 USD | 497,250.00 USD | 284,400.00 USD | 524,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 4,170.00 USD | 184,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 181,270,000.00 USD | 181,270,000.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 125,620,000.00 USD | 125,620,000.00 USD | 127,140.00 USD | 103,350.00 USD | 158,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 189,020,000.00 USD | 189,020,000.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,160,000.00 USD | 126,160,000.00 USD | 249,180.00 USD | 23,180.00 USD | 275,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 197,040,000.00 USD | 197,040,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,580,000.00 USD | 126,580,000.00 USD | 146,270.00 USD | 30,410.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 206,160,000.00 USD | 206,160,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,720,000.00 USD | 126,720,000.00 USD | 66,220.00 USD | 30,780.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 212,910,000.00 USD | 212,910,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 127,240,000.00 USD | 127,240,000.00 USD | 86,720.00 USD | 34,870.00 USD | 395,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 5,020.00 USD | 189,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 219,250,000.00 USD | 219,250,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,200,000.00 USD | 128,200,000.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 221,790,000.00 USD | 221,790,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,530,000.00 USD | 128,530,000.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 224,800,000.00 USD | 224,800,000.00 USD | 1,460,000.00 USD | 339,580.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,190,000.00 USD | 129,190,000.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 228,580,000.00 USD | 228,580,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,490,000.00 USD | 129,490,000.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 231,320,000.00 USD | 231,320,000.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,610,000.00 USD | 129,610,000.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 99,140.00 USD | 289,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 232,140,000.00 USD | 232,140,000.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,860,000.00 USD | 129,860,000.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 233,190,000.00 USD | 233,190,000.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,010,000.00 USD | 130,010,000.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 234,510,000.00 USD | 234,510,000.00 USD | 367,350.00 USD | 211,750.00 USD | 733,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,110,000.00 USD | 130,110,000.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 235,740,000.00 USD | 235,740,000.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,200,000.00 USD | 130,200,000.00 USD | 5,470.00 USD | 2,610.00 USD | 85,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 237,410,000.00 USD | 237,410,000.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,520,000.00 USD | 130,520,000.00 USD | 97,300.00 USD | 49,730.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,780.00 USD | 292,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 238,440,000.00 USD | 238,440,000.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,750,000.00 USD | 130,750,000.00 USD | 31,450.00 USD | 41,790.00 USD | 153,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 239,900,000.00 USD | 239,900,000.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,090,000.00 USD | 131,090,000.00 USD | 71,920.00 USD | 76,730.00 USD | 192,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 241,600,000.00 USD | 241,600,000.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,160,000.00 USD | 131,160,000.00 USD | 2,300.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 243,460,000.00 USD | 243,460,000.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,520,000.00 USD | 131,520,000.00 USD | 4,030.00 USD | 36,450.00 USD | 318,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 244,340,000.00 USD | 244,340,000.00 USD | 403,730.00 USD | 253,120.00 USD | 228,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 131,690,000.00 USD | 131,690,000.00 USD | 88,690.00 USD | 39,080.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,130.00 USD | 293,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 245,370,000.00 USD | 245,370,000.00 USD | 377,810.00 USD | 234,230.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,020,000.00 USD | 132,020,000.00 USD | 4,270.00 USD | 151,320.00 USD | 175,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 246,580,000.00 USD | 246,580,000.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,250,000.00 USD | 132,250,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 247,330,000.00 USD | 247,330,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,260,000.00 USD | 132,260,000.00 USD | 0.00 USD | 18,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 247,860,000.00 USD | 247,860,000.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,430,000.00 USD | 132,430,000.00 USD | 26,280.00 USD | 33,400.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 248,030,000.00 USD | 248,030,000.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 132,620,000.00 USD | 132,620,000.00 USD | 29,510.00 USD | 10,080.00 USD | 151,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 296,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,250,000.00 USD | 248,250,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 132,750,000.00 USD | 132,750,000.00 USD | 77,100.00 USD | 0.00 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,250,000.00 USD | 248,250,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,320,000.00 USD | 248,320,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,390,000.00 USD | 248,390,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,690,000.00 USD | 248,690,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 635.06 USD | 296,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 248,840,000.00 USD | 248,840,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 248,980,000.00 USD | 248,980,000.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 249,260,000.00 USD | 249,260,000.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,730.00 USD | 300,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,510.00 USD | 393,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 988.72 USD | 394,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 561,440.00 USD | 956,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 129,320.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 551.65 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,470.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 11,570.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 4,400,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 3,290.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 130,580.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,660.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 1,300.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 6,710.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 2,580.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 5,020.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 110.17 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 1,100.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 7,300.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,490.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 5,420,000.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 131,990.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 3,680.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 1,340.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 260.98 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 99,280.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 2,730,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 12,810.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,010.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 2,890,000.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 307,570.00 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 1,410.00 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,560.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 694.75 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 164.41 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 1,060.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 123.30 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 413,630.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 373.50 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 4,870.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 17,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 249,280.00 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 631.42 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,830.00 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 51,830.00 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.97 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 81,150.00 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.89 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 338.20 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 102.81 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 11,330.00 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 141.67 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 105.57 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 77,210.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 44,970.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,850.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,550.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 11,860.00 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 146.63 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 2,380.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 3,700,000.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 18,600.00 USD | 22,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 1,160.00 USD | 22,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 24,420.00 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 645.27 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 370,330.00 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 227.70 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 337.96 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 1,590,000.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 1,880.00 USD | 24,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,500,000.00 USD | 0.00 USD | 827.48 USD | `-79.60%` | `3,245.00` |
| `Live` | `Long` | `0.2650` | 64,500,000.00 USD | 0.00 USD | 1,400.00 USD | `-78.80%` | `5,275.00` |
| `Live` | `Long` | `0.2750` | 64,500,000.00 USD | 0.00 USD | 1,090.00 USD | `-78.00%` | `3,950.00` |
| `Live` | `Long` | `0.2850` | 64,500,000.00 USD | 0.00 USD | 3,800.00 USD | `-77.20%` | `13,348.00` |
| `Live` | `Long` | `0.2950` | 64,490,000.00 USD | 0.00 USD | 120.36 USD | `-76.40%` | `408.00` |
| `Live` | `Long` | `0.3050` | 64,490,000.00 USD | 0.00 USD | 122.00 USD | `-75.60%` | `400.00` |
| `Live` | `Long` | `0.3150` | 64,490,000.00 USD | 0.00 USD | 16,150.00 USD | `-74.80%` | `51,268.00` |
| `Live` | `Long` | `0.3250` | 64,480,000.00 USD | 0.00 USD | 19,750.00 USD | `-74.00%` | `60,778.00` |
| `Live` | `Long` | `0.3350` | 64,460,000.00 USD | 0.00 USD | 59,960.00 USD | `-73.20%` | `178,993.00` |
| `Live` | `Long` | `0.3450` | 64,400,000.00 USD | 0.00 USD | 439.88 USD | `-72.40%` | `1,275.00` |
| `Live` | `Long` | `0.3550` | 64,400,000.00 USD | 0.00 USD | 8,430.00 USD | `-71.60%` | `23,742.00` |
| `Live` | `Long` | `0.3650` | 64,390,000.00 USD | 0.00 USD | 4,990.00 USD | `-70.80%` | `13,682.00` |
| `Live` | `Long` | `0.3750` | 64,380,000.00 USD | 0.00 USD | 6,590.00 USD | `-70.00%` | `17,571.00` |
| `Live` | `Long` | `0.3850` | 64,380,000.00 USD | 0.00 USD | 269.50 USD | `-69.20%` | `700.00` |
| `Live` | `Long` | `0.3950` | 64,380,000.00 USD | 0.00 USD | 174.59 USD | `-68.40%` | `442.00` |
| `Live` | `Long` | `0.4050` | 64,380,000.00 USD | 0.00 USD | 2,640.00 USD | `-67.60%` | `6,512.00` |
| `Live` | `Long` | `0.4150` | 64,370,000.00 USD | 0.00 USD | 688,700.00 USD | `-66.80%` | `1,659,518.00` |
| `Live` | `Long` | `0.4250` | 63,690,000.00 USD | 0.00 USD | 23,930.00 USD | `-66.00%` | `56,300.00` |
| `Live` | `Long` | `0.4350` | 63,660,000.00 USD | 0.00 USD | 16,860.00 USD | `-65.20%` | `38,765.00` |
| `Live` | `Long` | `0.4550` | 63,650,000.00 USD | 0.00 USD | 1,540.00 USD | `-63.60%` | `3,377.00` |
| `Live` | `Long` | `0.4750` | 63,640,000.00 USD | 0.00 USD | 5,160.00 USD | `-62.00%` | `10,861.00` |
| `Live` | `Long` | `0.4850` | 63,640,000.00 USD | 0.00 USD | 283.72 USD | `-61.20%` | `585.00` |
| `Live` | `Long` | `0.4950` | 63,640,000.00 USD | 0.00 USD | 1,480.00 USD | `-60.40%` | `2,986.00` |
| `Live` | `Long` | `0.5050` | 63,640,000.00 USD | 0.00 USD | 1,160.00 USD | `-59.60%` | `2,292.00` |
| `Live` | `Long` | `0.5150` | 63,640,000.00 USD | 0.00 USD | 12,250.00 USD | `-58.80%` | `23,783.00` |
| `Live` | `Long` | `0.5250` | 63,620,000.00 USD | 0.00 USD | 14,270.00 USD | `-58.00%` | `27,185.00` |
| `Live` | `Long` | `0.5350` | 63,610,000.00 USD | 0.00 USD | 966.75 USD | `-57.20%` | `1,807.00` |
| `Live` | `Long` | `0.5450` | 63,610,000.00 USD | 0.00 USD | 159,160.00 USD | `-56.40%` | `292,045.00` |
| `Live` | `Long` | `0.5550` | 63,450,000.00 USD | 0.00 USD | 720.39 USD | `-55.60%` | `1,298.00` |
| `Live` | `Long` | `0.5650` | 63,450,000.00 USD | 0.00 USD | 7,030.00 USD | `-54.80%` | `12,446.00` |
| `Live` | `Long` | `0.5750` | 63,440,000.00 USD | 0.00 USD | 7,770.00 USD | `-54.00%` | `13,507.00` |
| `Live` | `Long` | `0.5850` | 63,430,000.00 USD | 0.00 USD | 3,310.00 USD | `-53.20%` | `5,653.00` |
| `Live` | `Long` | `0.5950` | 63,430,000.00 USD | 0.00 USD | 4,540.00 USD | `-52.40%` | `7,623.00` |
| `Live` | `Long` | `0.6050` | 63,430,000.00 USD | 0.00 USD | 27,410.00 USD | `-51.60%` | `45,308.00` |
| `Live` | `Long` | `0.6150` | 63,400,000.00 USD | 0.00 USD | 31,360.00 USD | `-50.80%` | `51,000.00` |
| `Live` | `Long` | `0.6250` | 63,370,000.00 USD | 0.00 USD | 1,130.00 USD | `-50.00%` | `1,803.00` |
| `Live` | `Long` | `0.6350` | 63,370,000.00 USD | 0.00 USD | 10,810.00 USD | `-49.20%` | `17,020.00` |
| `Live` | `Long` | `0.6450` | 63,350,000.00 USD | 0.00 USD | 19,650.00 USD | `-48.40%` | `30,458.00` |
| `Live` | `Long` | `0.6550` | 63,340,000.00 USD | 0.00 USD | 2,310.00 USD | `-47.60%` | `3,529.00` |
| `Live` | `Long` | `0.6650` | 63,330,000.00 USD | 0.00 USD | 18,150.00 USD | `-46.80%` | `27,300.00` |
| `Live` | `Long` | `0.6750` | 63,310,000.00 USD | 0.00 USD | 26,710.00 USD | `-46.00%` | `39,563.00` |
| `Live` | `Long` | `0.6850` | 63,290,000.00 USD | 0.00 USD | 6,600.00 USD | `-45.20%` | `9,631.00` |
| `Live` | `Long` | `0.6950` | 63,280,000.00 USD | 0.00 USD | 194,370.00 USD | `-44.40%` | `279,665.00` |
| `Live` | `Long` | `0.7050` | 63,090,000.00 USD | 0.00 USD | 24,740.00 USD | `-43.60%` | `35,096.00` |
| `Live` | `Long` | `0.7150` | 63,060,000.00 USD | 0.00 USD | 86,300.00 USD | `-42.80%` | `120,700.00` |
| `Live` | `Long` | `0.7250` | 62,980,000.00 USD | 0.00 USD | 216,840.00 USD | `-42.00%` | `299,086.00` |
| `Live` | `Long` | `0.7350` | 62,760,000.00 USD | 0.00 USD | 44,260.00 USD | `-41.20%` | `60,220.00` |
| `Live` | `Long` | `0.7450` | 62,720,000.00 USD | 0.00 USD | 111,510.00 USD | `-40.40%` | `149,674.00` |
| `Live` | `Long` | `0.7550` | 62,600,000.00 USD | 0.00 USD | 147,570.00 USD | `-39.60%` | `195,456.00` |
| `Live` | `Long` | `0.7650` | 62,460,000.00 USD | 0.00 USD | 2,190.00 USD | `-38.80%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 62,450,000.00 USD | 0.00 USD | 7,110.00 USD | `-38.00%` | `9,170.00` |
| `Live` | `Long` | `0.7850` | 62,450,000.00 USD | 0.00 USD | 16,330.00 USD | `-37.21%` | `20,798.00` |
| `Live` | `Long` | `0.7950` | 62,430,000.00 USD | 0.00 USD | 508,640.00 USD | `-36.41%` | `639,802.00` |
| `Live` | `Long` | `0.8050` | 61,920,000.00 USD | 0.00 USD | 5,330.00 USD | `-35.61%` | `6,619.00` |
| `Live` | `Long` | `0.8150` | 61,920,000.00 USD | 0.00 USD | 77,140.00 USD | `-34.81%` | `94,656.00` |
| `Live` | `Long` | `0.8250` | 61,840,000.00 USD | 0.00 USD | 6,620.00 USD | `-34.01%` | `8,022.00` |
| `Live` | `Long` | `0.8350` | 61,830,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-33.21%` | `3,588,692.00` |
| `Live` | `Long` | `0.8450` | 58,840,000.00 USD | 0.00 USD | 59,990.00 USD | `-32.41%` | `70,994.00` |
| `Live` | `Long` | `0.8550` | 58,780,000.00 USD | 0.00 USD | 75,770.00 USD | `-31.61%` | `88,621.00` |
| `Live` | `Long` | `0.8650` | 58,700,000.00 USD | 0.00 USD | 22,360.00 USD | `-30.81%` | `25,846.00` |
| `Live` | `Long` | `0.8750` | 58,680,000.00 USD | 0.00 USD | 95,970.00 USD | `-30.01%` | `109,677.00` |
| `Live` | `Long` | `0.8850` | 58,580,000.00 USD | 0.00 USD | 367,410.00 USD | `-29.21%` | `415,158.00` |
| `Live` | `Long` | `0.8950` | 58,210,000.00 USD | 0.00 USD | 96,190.00 USD | `-28.41%` | `107,475.00` |
| `Live` | `Long` | `0.9050` | 58,120,000.00 USD | 0.00 USD | 137,830.00 USD | `-27.61%` | `152,298.00` |
| `Live` | `Long` | `0.9150` | 57,980,000.00 USD | 0.00 USD | 134,950.00 USD | `-26.81%` | `147,483.00` |
| `Live` | `Long` | `0.9250` | 57,850,000.00 USD | 0.00 USD | 79,310.00 USD | `-26.01%` | `85,742.00` |
| `Live` | `Long` | `0.9350` | 57,770,000.00 USD | 0.00 USD | 92,190.00 USD | `-25.21%` | `98,596.00` |
| `Live` | `Long` | `0.9450` | 57,670,000.00 USD | 0.00 USD | 55,870.00 USD | `-24.41%` | `59,123.00` |
| `Live` | `Long` | `0.9550` | 57,620,000.00 USD | 0.00 USD | 156,170.00 USD | `-23.61%` | `163,532.00` |
| `Live` | `Long` | `0.9650` | 57,460,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-22.81%` | `35,119,594.00` |
| `Live` | `Long` | `0.9750` | 23,570,000.00 USD | 0.00 USD | 152,440.00 USD | `-22.01%` | `156,347.00` |
| `Live` | `Long` | `0.9850` | 23,420,000.00 USD | 0.00 USD | 452,590.00 USD | `-21.21%` | `459,479.00` |
| `Live` | `Long` | `0.9950` | 22,970,000.00 USD | 0.00 USD | 117,230.00 USD | `-20.41%` | `117,815.00` |
| `Live` | `Long` | `1.00` | 22,850,000.00 USD | 0.00 USD | 497,840.00 USD | `-19.61%` | `495,362.00` |
| `Live` | `Long` | `1.01` | 22,350,000.00 USD | 0.00 USD | 287,950.00 USD | `-18.81%` | `283,696.00` |
| `Live` | `Long` | `1.02` | 22,060,000.00 USD | 0.00 USD | 2,680,000.00 USD | `-18.01%` | `2,616,046.00` |
| `Live` | `Long` | `1.03` | 19,380,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-17.21%` | `2,061,017.00` |
| `Live` | `Long` | `1.04` | 17,250,000.00 USD | 0.00 USD | 180,980.00 USD | `-16.41%` | `173,184.00` |
| `Live` | `Long` | `1.05` | 17,070,000.00 USD | 0.00 USD | 1,650,000.00 USD | `-15.61%` | `1,567,704.00` |
| `Live` | `Long` | `1.06` | 15,410,000.00 USD | 0.00 USD | 382,300.00 USD | `-14.81%` | `358,971.00` |
| `Live` | `Long` | `1.07` | 15,030,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-14.01%` | `1,220,385.00` |
| `Live` | `Long` | `1.08` | 13,720,000.00 USD | 0.00 USD | 176,480.00 USD | `-13.21%` | `162,656.00` |
| `Live` | `Long` | `1.09` | 13,540,000.00 USD | 0.00 USD | 390,190.00 USD | `-12.41%` | `356,339.00` |
| `Live` | `Long` | `1.10` | 13,150,000.00 USD | 0.00 USD | 109,910.00 USD | `-11.61%` | `99,465.00` |
| `Live` | `Long` | `1.11` | 13,040,000.00 USD | 0.00 USD | 578,850.00 USD | `-10.81%` | `519,148.00` |
| `Live` | `Long` | `1.12` | 12,460,000.00 USD | 0.00 USD | 2,180,000.00 USD | `-10.01%` | `1,935,545.00` |
| `Live` | `Long` | `1.14` | 10,290,000.00 USD | 0.00 USD | 165,490.00 USD | `-9.21%` | `145,805.00` |
| `Live` | `Long` | `1.15` | 10,120,000.00 USD | 0.00 USD | 280,040.00 USD | `-8.41%` | `244,575.00` |
| `Live` | `Long` | `1.16` | 9,840,000.00 USD | 0.00 USD | 359,890.00 USD | `-7.61%` | `311,596.00` |
| `Live` | `Long` | `1.17` | 9,480,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-6.81%` | `1,112,210.00` |
| `Live` | `Long` | `1.18` | 8,190,000.00 USD | 0.00 USD | 274,310.00 USD | `-6.01%` | `233,457.00` |
| `Live` | `Long` | `1.19` | 7,910,000.00 USD | 0.00 USD | 568,290.00 USD | `-5.21%` | `479,571.00` |
| `Live` | `Long` | `1.20` | 7,340,000.00 USD | 0.00 USD | 607,930.00 USD | `-4.41%` | `508,730.00` |
| `Live` | `Long` | `1.21` | 6,740,000.00 USD | 0.00 USD | 11,860.00 USD | `-3.61%` | `9,841.00` |
| `Live` | `Long` | `1.22` | 6,720,000.00 USD | 0.00 USD | 54,190.00 USD | `-2.81%` | `44,599.00` |
| `Live` | `Long` | `1.23` | 6,670,000.00 USD | 0.00 USD | 6,610,000.00 USD | `-2.01%` | `5,393,182.00` |
| `Live` | `Long` | `1.24` | 62,550.00 USD | 0.00 USD | 62,550.00 USD | `-1.21%` | `50,651.00` |
| `Live` | `Short` | `1.26` | 1,010.00 USD | 1,010.00 USD | 0.00 USD | `+1.19%` | `798.00` |
| `Live` | `Short` | `1.27` | 6,680.00 USD | 5,670.00 USD | 0.00 USD | `+1.99%` | `4,447.00` |
| `Live` | `Short` | `1.28` | 12,870.00 USD | 6,190.00 USD | 0.00 USD | `+2.79%` | `4,820.00` |
| `Live` | `Short` | `1.29` | 64,130.00 USD | 51,250.00 USD | 0.00 USD | `+3.59%` | `39,578.00` |
| `Live` | `Short` | `1.30` | 65,750.00 USD | 1,630.00 USD | 0.00 USD | `+4.39%` | `1,246.00` |
| `Live` | `Short` | `1.31` | 128,720.00 USD | 62,960.00 USD | 0.00 USD | `+5.19%` | `47,881.00` |
| `Live` | `Short` | `1.32` | 136,100.00 USD | 7,390.00 USD | 0.00 USD | `+5.99%` | `5,576.00` |
| `Live` | `Short` | `1.33` | 180,730.00 USD | 44,630.00 USD | 0.00 USD | `+6.79%` | `33,429.00` |
| `Live` | `Short` | `1.34` | 184,900.00 USD | 4,170.00 USD | 0.00 USD | `+7.59%` | `3,098.00` |
| `Live` | `Short` | `1.35` | 189,920.00 USD | 5,020.00 USD | 0.00 USD | `+8.39%` | `3,706.00` |
| `Live` | `Short` | `1.36` | 289,060.00 USD | 99,140.00 USD | 0.00 USD | `+9.19%` | `72,630.00` |
| `Live` | `Short` | `1.38` | 292,840.00 USD | 3,780.00 USD | 0.00 USD | `+9.99%` | `2,747.00` |
| `Live` | `Short` | `1.39` | 293,970.00 USD | 1,130.00 USD | 0.00 USD | `+10.79%` | `816.00` |
| `Live` | `Short` | `1.40` | 296,060.00 USD | 2,090.00 USD | 0.00 USD | `+11.59%` | `1,500.00` |
| `Live` | `Short` | `1.41` | 296,700.00 USD | 635.06 USD | 0.00 USD | `+12.39%` | `452.00` |
| `Live` | `Short` | `1.42` | 300,420.00 USD | 3,730.00 USD | 0.00 USD | `+13.19%` | `2,635.00` |
| `Live` | `Short` | `1.43` | 393,930.00 USD | 93,510.00 USD | 0.00 USD | `+13.99%` | `65,619.00` |
| `Live` | `Short` | `1.44` | 394,920.00 USD | 988.72 USD | 0.00 USD | `+14.79%` | `689.00` |
| `Live` | `Short` | `1.45` | 956,360.00 USD | 561,440.00 USD | 0.00 USD | `+15.59%` | `388,541.00` |
| `Live` | `Short` | `1.47` | 1,090,000.00 USD | 129,320.00 USD | 0.00 USD | `+17.19%` | `88,271.00` |
| `Live` | `Short` | `1.48` | 1,090,000.00 USD | 551.65 USD | 0.00 USD | `+17.99%` | `374.00` |
| `Live` | `Short` | `1.50` | 1,100,000.00 USD | 12,470.00 USD | 0.00 USD | `+19.59%` | `8,338.00` |
| `Live` | `Short` | `1.51` | 1,110,000.00 USD | 11,570.00 USD | 0.00 USD | `+21.19%` | `7,640.00` |
| `Live` | `Short` | `1.53` | 1,110,000.00 USD | 174.99 USD | 0.00 USD | `+22.79%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,110,000.00 USD | 1,370.00 USD | 0.00 USD | `+23.59%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,110,000.00 USD | 1,360.00 USD | 0.00 USD | `+24.39%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,110,000.00 USD | 555.57 USD | 0.00 USD | `+25.19%` | `355.00` |
| `Live` | `Short` | `1.57` | 5,510,000.00 USD | 4,400,000.00 USD | 0.00 USD | `+25.99%` | `2,793,358.00` |
| `Live` | `Short` | `1.58` | 5,520,000.00 USD | 3,290.00 USD | 0.00 USD | `+26.79%` | `2,078.00` |
| `Live` | `Short` | `1.60` | 5,650,000.00 USD | 130,580.00 USD | 0.00 USD | `+28.39%` | `81,359.00` |
| `Live` | `Short` | `1.61` | 5,650,000.00 USD | 2,660.00 USD | 0.00 USD | `+29.19%` | `1,647.00` |
| `Live` | `Short` | `1.62` | 5,650,000.00 USD | 1,300.00 USD | 0.00 USD | `+29.99%` | `798.00` |
| `Live` | `Short` | `1.64` | 5,660,000.00 USD | 6,710.00 USD | 0.00 USD | `+30.79%` | `4,102.00` |
| `Live` | `Short` | `1.65` | 5,660,000.00 USD | 2,580.00 USD | 0.00 USD | `+31.59%` | `1,571.00` |
| `Live` | `Short` | `1.66` | 5,660,000.00 USD | 147.30 USD | 0.00 USD | `+32.39%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,660,000.00 USD | 586.08 USD | 0.00 USD | `+33.19%` | `352.00` |
| `Live` | `Short` | `1.68` | 5,670,000.00 USD | 5,020.00 USD | 0.00 USD | `+33.99%` | `3,000.00` |
| `Live` | `Short` | `1.69` | 5,670,000.00 USD | 4,180.00 USD | 0.00 USD | `+34.79%` | `2,481.00` |
| `Live` | `Short` | `1.70` | 5,670,000.00 USD | 110.17 USD | 0.00 USD | `+35.59%` | `65.00` |
| `Live` | `Short` | `1.71` | 5,670,000.00 USD | 1,980.00 USD | 0.00 USD | `+36.39%` | `1,163.00` |
| `Live` | `Short` | `1.72` | 5,670,000.00 USD | 1,100.00 USD | 0.00 USD | `+37.19%` | `642.00` |
| `Live` | `Short` | `1.74` | 5,680,000.00 USD | 7,300.00 USD | 0.00 USD | `+38.79%` | `4,208.00` |
| `Live` | `Short` | `1.75` | 5,680,000.00 USD | 2,730.00 USD | 0.00 USD | `+39.59%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 5,690,000.00 USD | 2,490.00 USD | 0.00 USD | `+40.39%` | `1,419.00` |
| `Live` | `Short` | `1.76` | 11,110,000.00 USD | 5,420,000.00 USD | 0.00 USD | `+41.19%` | `3,071,193.00` |
| `Live` | `Short` | `1.78` | 11,240,000.00 USD | 131,990.00 USD | 0.00 USD | `+42.79%` | `73,946.00` |
| `Live` | `Short` | `1.79` | 11,240,000.00 USD | 3,680.00 USD | 0.00 USD | `+43.59%` | `2,051.00` |
| `Live` | `Short` | `1.80` | 11,240,000.00 USD | 889.87 USD | 0.00 USD | `+44.39%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,240,000.00 USD | 1,340.00 USD | 0.00 USD | `+45.19%` | `736.00` |
| `Live` | `Short` | `1.82` | 11,240,000.00 USD | 260.98 USD | 0.00 USD | `+45.99%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,340,000.00 USD | 99,280.00 USD | 0.00 USD | `+46.79%` | `54,101.00` |
| `Live` | `Short` | `1.84` | 14,080,000.00 USD | 2,730,000.00 USD | 0.00 USD | `+47.59%` | `1,481,016.00` |
| `Live` | `Short` | `1.85` | 14,090,000.00 USD | 12,810.00 USD | 0.00 USD | `+48.39%` | `6,908.00` |
| `Live` | `Short` | `1.86` | 14,090,000.00 USD | 2,010.00 USD | 0.00 USD | `+49.19%` | `1,079.00` |
| `Live` | `Short` | `1.88` | 16,980,000.00 USD | 2,890,000.00 USD | 0.00 USD | `+49.99%` | `1,540,696.00` |
| `Live` | `Short` | `1.90` | 16,980,000.00 USD | 4,190.00 USD | 0.00 USD | `+51.59%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 17,290,000.00 USD | 307,570.00 USD | 0.00 USD | `+52.39%` | `161,455.00` |
| `Live` | `Short` | `1.92` | 17,290,000.00 USD | 1,410.00 USD | 0.00 USD | `+53.19%` | `737.00` |
| `Live` | `Short` | `1.96` | 17,290,000.00 USD | 293.25 USD | 0.00 USD | `+56.39%` | `150.00` |
| `Live` | `Short` | `1.97` | 17,520,000.00 USD | 227,560.00 USD | 0.00 USD | `+57.19%` | `115,806.00` |
| `Live` | `Short` | `1.98` | 17,520,000.00 USD | 651.75 USD | 0.00 USD | `+57.99%` | `330.00` |
| `Live` | `Short` | `1.99` | 17,520,000.00 USD | 694.75 USD | 0.00 USD | `+58.79%` | `350.00` |
| `Live` | `Short` | `2.00` | 17,520,000.00 USD | 164.41 USD | 0.00 USD | `+60.39%` | `82.00` |
| `Live` | `Short` | `2.02` | 17,520,000.00 USD | 513.83 USD | 0.00 USD | `+61.19%` | `255.00` |
| `Live` | `Short` | `2.02` | 17,520,000.00 USD | 1,060.00 USD | 0.00 USD | `+61.99%` | `522.00` |
| `Live` | `Short` | `2.04` | 17,520,000.00 USD | 198.36 USD | 0.00 USD | `+63.59%` | `97.00` |
| `Live` | `Short` | `2.06` | 17,520,000.00 USD | 123.30 USD | 0.00 USD | `+64.39%` | `60.00` |
| `Live` | `Short` | `2.06` | 17,940,000.00 USD | 413,630.00 USD | 0.00 USD | `+65.19%` | `200,306.00` |
| `Live` | `Short` | `2.08` | 17,940,000.00 USD | 373.50 USD | 0.00 USD | `+65.99%` | `180.00` |
| `Live` | `Short` | `2.10` | 17,940,000.00 USD | 4,870.00 USD | 0.00 USD | `+67.59%` | `2,325.00` |
| `Live` | `Short` | `2.10` | 17,940,000.00 USD | 294.70 USD | 0.00 USD | `+68.39%` | `140.00` |
| `Live` | `Short` | `2.12` | 17,950,000.00 USD | 3,100.00 USD | 0.00 USD | `+69.19%` | `1,468.00` |
| `Live` | `Short` | `2.12` | 18,200,000.00 USD | 249,280.00 USD | 0.00 USD | `+69.99%` | `117,308.00` |
| `Live` | `Short` | `2.15` | 18,200,000.00 USD | 631.42 USD | 0.00 USD | `+72.39%` | `293.00` |
| `Live` | `Short` | `2.17` | 18,200,000.00 USD | 2,830.00 USD | 0.00 USD | `+73.99%` | `1,299.00` |
| `Live` | `Short` | `2.19` | 18,250,000.00 USD | 51,830.00 USD | 0.00 USD | `+74.79%` | `23,723.00` |
| `Live` | `Short` | `2.19` | 18,250,000.00 USD | 100.97 USD | 0.00 USD | `+75.59%` | `46.00` |
| `Live` | `Short` | `2.21` | 18,330,000.00 USD | 81,150.00 USD | 0.00 USD | `+76.39%` | `36,803.00` |
| `Live` | `Short` | `2.21` | 18,330,000.00 USD | 101.89 USD | 0.00 USD | `+77.19%` | `46.00` |
| `Live` | `Short` | `2.23` | 18,330,000.00 USD | 338.20 USD | 0.00 USD | `+77.99%` | `152.00` |
| `Live` | `Short` | `2.23` | 18,330,000.00 USD | 102.81 USD | 0.00 USD | `+78.79%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,340,000.00 USD | 11,330.00 USD | 0.00 USD | `+79.59%` | `5,046.00` |
| `Live` | `Short` | `2.29` | 18,340,000.00 USD | 141.67 USD | 0.00 USD | `+82.79%` | `62.00` |
| `Live` | `Short` | `2.29` | 18,340,000.00 USD | 105.57 USD | 0.00 USD | `+83.59%` | `46.00` |
| `Live` | `Short` | `2.31` | 18,420,000.00 USD | 77,210.00 USD | 0.00 USD | `+84.39%` | `33,497.00` |
| `Live` | `Short` | `2.31` | 18,470,000.00 USD | 44,970.00 USD | 0.00 USD | `+85.19%` | `19,425.00` |
| `Live` | `Short` | `2.33` | 18,470,000.00 USD | 2,850.00 USD | 0.00 USD | `+85.99%` | `1,227.00` |
| `Live` | `Short` | `2.33` | 18,470,000.00 USD | 2,550.00 USD | 0.00 USD | `+86.79%` | `1,090.00` |
| `Live` | `Short` | `2.35` | 18,480,000.00 USD | 11,860.00 USD | 0.00 USD | `+87.58%` | `5,057.00` |
| `Live` | `Short` | `2.37` | 18,480,000.00 USD | 146.63 USD | 0.00 USD | `+89.18%` | `62.00` |
| `Live` | `Short` | `2.38` | 18,490,000.00 USD | 2,380.00 USD | 0.00 USD | `+89.98%` | `1,000.00` |
| `Live` | `Short` | `2.38` | 22,190,000.00 USD | 3,700,000.00 USD | 0.00 USD | `+90.78%` | `1,551,874.00` |
| `Live` | `Short` | `2.40` | 22,210,000.00 USD | 18,600.00 USD | 0.00 USD | `+92.38%` | `7,734.00` |
| `Live` | `Short` | `2.42` | 22,210,000.00 USD | 1,160.00 USD | 0.00 USD | `+93.18%` | `481.00` |
| `Live` | `Short` | `2.42` | 22,230,000.00 USD | 24,420.00 USD | 0.00 USD | `+93.98%` | `10,070.00` |
| `Live` | `Short` | `2.44` | 22,230,000.00 USD | 645.27 USD | 0.00 USD | `+94.78%` | `265.00` |
| `Live` | `Short` | `2.44` | 22,600,000.00 USD | 370,330.00 USD | 0.00 USD | `+95.58%` | `151,463.00` |
| `Live` | `Short` | `2.48` | 22,600,000.00 USD | 227.70 USD | 0.00 USD | `+97.98%` | `92.00` |
| `Live` | `Short` | `2.48` | 22,600,000.00 USD | 337.96 USD | 0.00 USD | `+98.78%` | `136.00` |
| `Live` | `Short` | `2.50` | 24,190,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+99.58%` | `637,352.00` |
| `Live` | `Short` | `2.50` | 24,200,000.00 USD | 1,880.00 USD | 0.00 USD | `+100.38%` | `750.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 3,990,000.00 USD | 0.00 USD | 102.00 USD | `-79.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 3,990,000.00 USD | 0.00 USD | 351.50 USD | `-70.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,990,000.00 USD | 0.00 USD | 139.12 USD | `-70.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 3,990,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 3,980,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,980,000.00 USD | 0.00 USD | 408.51 USD | `-64.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,980,000.00 USD | 0.00 USD | 273.00 USD | `-63.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,980,000.00 USD | 0.00 USD | 151.12 USD | `-62.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,980,000.00 USD | 0.00 USD | 142.50 USD | `-62.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,980,000.00 USD | 0.00 USD | 145.50 USD | `-61.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4950` | 3,980,000.00 USD | 0.00 USD | 562.81 USD | `-60.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,980,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 3,980,000.00 USD | 0.00 USD | 285.82 USD | `-58.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,980,000.00 USD | 0.00 USD | 306.60 USD | `-58.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,980,000.00 USD | 0.00 USD | 121.55 USD | `-55.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,980,000.00 USD | 0.00 USD | 656.53 USD | `-54.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,980,000.00 USD | 0.00 USD | 100.62 USD | `-53.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 3,980,000.00 USD | 0.00 USD | 203.75 USD | `-50.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,980,000.00 USD | 0.00 USD | 791.85 USD | `-49.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,970,000.00 USD | 0.00 USD | 573.40 USD | `-48.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,970,000.00 USD | 0.00 USD | 244.31 USD | `-47.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,970,000.00 USD | 0.00 USD | 29,530.00 USD | `-46.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 3,940,000.00 USD | 0.00 USD | 503.55 USD | `-46.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 3,940,000.00 USD | 0.00 USD | 480.19 USD | `-45.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,940,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,930,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 3,930,000.00 USD | 0.00 USD | 228.80 USD | `-42.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 3,930,000.00 USD | 0.00 USD | 536.50 USD | `-42.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,930,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,930,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,920,000.00 USD | 0.00 USD | 25,490.00 USD | `-36.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 3,900,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-34.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,590,000.00 USD | 0.00 USD | 1,260.00 USD | `-31.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,590,000.00 USD | 0.00 USD | 690.38 USD | `-30.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,590,000.00 USD | 0.00 USD | 1,400.00 USD | `-29.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,590,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,580,000.00 USD | 0.00 USD | 838.94 USD | `-27.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,580,000.00 USD | 0.00 USD | 338.55 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,580,000.00 USD | 0.00 USD | 1,840.00 USD | `-26.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,580,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,580,000.00 USD | 0.00 USD | 112.46 USD | `-24.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,580,000.00 USD | 0.00 USD | 1,730.00 USD | `-23.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,580,000.00 USD | 0.00 USD | 4,010.00 USD | `-22.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,570,000.00 USD | 0.00 USD | 6,300.00 USD | `-22.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,570,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,560,000.00 USD | 0.00 USD | 902.47 USD | `-20.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,560,000.00 USD | 0.00 USD | 45,660.00 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,520,000.00 USD | 0.00 USD | 4,760.00 USD | `-18.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,510,000.00 USD | 0.00 USD | 1,840.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,510,000.00 USD | 0.00 USD | 48,180.00 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,460,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,460,000.00 USD | 0.00 USD | 23,530.00 USD | `-15.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,440,000.00 USD | 0.00 USD | 3,960.00 USD | `-14.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,430,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,380,000.00 USD | 0.00 USD | 3,360.00 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,380,000.00 USD | 0.00 USD | 16,830.00 USD | `-12.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,360,000.00 USD | 0.00 USD | 12,830.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,350,000.00 USD | 0.00 USD | 9,780.00 USD | `-10.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,340,000.00 USD | 0.00 USD | 77,260.00 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,260,000.00 USD | 0.00 USD | 13,380.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,250,000.00 USD | 0.00 USD | 124,570.00 USD | `-8.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,120,000.00 USD | 0.00 USD | 58,820.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,070,000.00 USD | 0.00 USD | 37,230.00 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,030,000.00 USD | 0.00 USD | 103,110.00 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 925,760.00 USD | 0.00 USD | 248,520.00 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 677,240.00 USD | 0.00 USD | 190,020.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 487,220.00 USD | 0.00 USD | 138,380.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 348,840.00 USD | 0.00 USD | 28,670.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 320,170.00 USD | 0.00 USD | 115,990.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 204,190.00 USD | 0.00 USD | 59,190.00 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 145,000.00 USD | 0.00 USD | 145,000.00 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 38,700.00 USD | 38,700.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 40,360.00 USD | 1,660.00 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 95,980.00 USD | 55,620.00 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 404,140.00 USD | 308,160.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 447,580.00 USD | 43,440.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 467,810.00 USD | 20,230.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,080,000.00 USD | 611,420.00 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,200,000.00 USD | 123,090.00 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,250,000.00 USD | 43,890.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,310,000.00 USD | 65,480.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,330,000.00 USD | 14,640.00 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,580,000.00 USD | 249,090.00 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,660,000.00 USD | 81,760.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,710,000.00 USD | 55,590.00 USD | 0.00 USD | `+10.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,720,000.00 USD | 3,960.00 USD | 0.00 USD | `+11.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,120,000.00 USD | 4,400,000.00 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,120,000.00 USD | 3,230.00 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,130,000.00 USD | 6,460.00 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,130,000.00 USD | 1,450.00 USD | 0.00 USD | `+14.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,370,000.00 USD | 242,580.00 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,380,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,400,000.00 USD | 21,430.00 USD | 0.00 USD | `+17.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,510,000.00 USD | 108,020.00 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,530,000.00 USD | 14,870.00 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,540,000.00 USD | 17,790.00 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,630,000.00 USD | 85,390.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,640,000.00 USD | 11,760.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,660,000.00 USD | 19,430.00 USD | 0.00 USD | `+21.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,710,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,720,000.00 USD | 12,200.00 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,720,000.00 USD | 2,380.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,730,000.00 USD | 7,160.00 USD | 0.00 USD | `+25.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,730,000.00 USD | 5,570.00 USD | 0.00 USD | `+25.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,740,000.00 USD | 10,570.00 USD | 0.00 USD | `+26.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,880,000.00 USD | 139,120.00 USD | 0.00 USD | `+27.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,880,000.00 USD | 1,840.00 USD | 0.00 USD | `+28.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,970,000.00 USD | 80,330.00 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,970,000.00 USD | 464.75 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,150,000.00 USD | 179,860.00 USD | 0.00 USD | `+30.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,150,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,230,000.00 USD | 85,010.00 USD | 0.00 USD | `+32.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,240,000.00 USD | 6,080.00 USD | 0.00 USD | `+33.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,260,000.00 USD | 18,400.00 USD | 0.00 USD | `+33.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,330,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,350,000.00 USD | 18,000.00 USD | 0.00 USD | `+35.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,580,000.00 USD | 231,640.00 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,590,000.00 USD | 14,250.00 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,590,000.00 USD | 534.75 USD | 0.00 USD | `+37.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,640,000.00 USD | 43,240.00 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,640,000.00 USD | 3,330.00 USD | 0.00 USD | `+39.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,650,000.00 USD | 9,200.00 USD | 0.00 USD | `+40.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,670,000.00 USD | 21,720.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,800,000.00 USD | 126,830.00 USD | 0.00 USD | `+41.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,920,000.00 USD | 124,660.00 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,930,000.00 USD | 3,980.00 USD | 0.00 USD | `+43.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,930,000.00 USD | 254.51 USD | 0.00 USD | `+44.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,940,000.00 USD | 11,080.00 USD | 0.00 USD | `+45.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,940,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,950,000.00 USD | 8,170.00 USD | 0.00 USD | `+46.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,950,000.00 USD | 843.17 USD | 0.00 USD | `+47.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,960,000.00 USD | 8,390.00 USD | 0.00 USD | `+48.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,960,000.00 USD | 4,420.00 USD | 0.00 USD | `+49.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,960,000.00 USD | 591.89 USD | 0.00 USD | `+50.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,010,000.00 USD | 46,370.00 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,020,000.00 USD | 9,270.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,020,000.00 USD | 265.10 USD | 0.00 USD | `+54.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,020,000.00 USD | 2,040.00 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,020,000.00 USD | 807.42 USD | 0.00 USD | `+56.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,040,000.00 USD | 14,120.00 USD | 0.00 USD | `+57.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,040,000.00 USD | 4,010.00 USD | 0.00 USD | `+57.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,040,000.00 USD | 325.54 USD | 0.00 USD | `+58.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,050,000.00 USD | 7,020.00 USD | 0.00 USD | `+59.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,230,000.00 USD | 184,840.00 USD | 0.00 USD | `+60.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,240,000.00 USD | 3,350.00 USD | 0.00 USD | `+61.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,240,000.00 USD | 181.12 USD | 0.00 USD | `+62.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,240,000.00 USD | 382.41 USD | 0.00 USD | `+63.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,240,000.00 USD | 3,420.00 USD | 0.00 USD | `+65.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,240,000.00 USD | 661.93 USD | 0.00 USD | `+65.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,370,000.00 USD | 124,400.00 USD | 0.00 USD | `+67.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,370,000.00 USD | 1,580.00 USD | 0.00 USD | `+68.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,380,000.00 USD | 13,900.00 USD | 0.00 USD | `+69.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,410,000.00 USD | 24,840.00 USD | 0.00 USD | `+71.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,460,000.00 USD | 50,580.00 USD | 0.00 USD | `+72.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,460,000.00 USD | 2,690.00 USD | 0.00 USD | `+73.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,460,000.00 USD | 2,180.00 USD | 0.00 USD | `+75.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,610,000.00 USD | 151,380.00 USD | 0.00 USD | `+77.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,610,000.00 USD | 2,230.00 USD | 0.00 USD | `+81.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,620,000.00 USD | 1,140.00 USD | 0.00 USD | `+82.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,630,000.00 USD | 11,670.00 USD | 0.00 USD | `+83.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,630,000.00 USD | 370.40 USD | 0.00 USD | `+85.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,630,000.00 USD | 733.19 USD | 0.00 USD | `+86.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,630,000.00 USD | 2,410.00 USD | 0.00 USD | `+89.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,630,000.00 USD | 475.00 USD | 0.00 USD | `+89.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,630,000.00 USD | 1,190.00 USD | 0.00 USD | `+90.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,640,000.00 USD | 2,540.00 USD | 0.00 USD | `+91.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,640,000.00 USD | 1,590.00 USD | 0.00 USD | `+92.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,640,000.00 USD | 1,370.00 USD | 0.00 USD | `+93.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,660,000.00 USD | 19,590.00 USD | 0.00 USD | `+93.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,660,000.00 USD | 564.92 USD | 0.00 USD | `+94.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,660,000.00 USD | 3,420.00 USD | 0.00 USD | `+98.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,660,000.00 USD | 124.75 USD | 0.00 USD | `+99.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,690,000.00 USD | 29,920.00 USD | 0.00 USD | `+100.38%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 99,100,000.00 USD | 0.00 USD | 99,100,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `1.09` | 99,090,000.00 USD | 0.00 USD | 99,090,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 99,050,000.00 USD | 0.00 USD | 99,050,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 98,950,000.00 USD | 0.00 USD | 98,950,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 98,910,000.00 USD | 0.00 USD | 98,910,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 98,910,000.00 USD | 0.00 USD | 98,910,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 98,620,000.00 USD | 0.00 USD | 98,620,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 98,620,000.00 USD | 0.00 USD | 98,620,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 98,620,000.00 USD | 0.00 USD | 98,620,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 98,620,000.00 USD | 0.00 USD | 98,620,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.12` | 98,560,000.00 USD | 0.00 USD | 98,560,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `7D` | `1.12` | 98,550,000.00 USD | 0.00 USD | 98,550,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `7D` | `1.12` | 98,470,000.00 USD | 0.00 USD | 98,470,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `1.12` | 90,580,000.00 USD | 0.00 USD | 90,580,000.00 USD | 25,830.00 USD | 44,000.00 USD | 175,200.00 USD |
| `7D` | `1.12` | 98,450,000.00 USD | 0.00 USD | 98,450,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.12` | 90,340,000.00 USD | 0.00 USD | 90,340,000.00 USD | 97,300.00 USD | 49,730.00 USD | 172,240.00 USD |
| `7D` | `1.13` | 98,240,000.00 USD | 0.00 USD | 98,240,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD |
| `1D` | `1.13` | 90,020,000.00 USD | 0.00 USD | 90,020,000.00 USD | 31,450.00 USD | 41,790.00 USD | 153,110.00 USD |
| `7D` | `1.13` | 98,090,000.00 USD | 0.00 USD | 98,090,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 89,790,000.00 USD | 0.00 USD | 89,790,000.00 USD | 74,730.00 USD | 82,720.00 USD | 192,970.00 USD |
| `7D` | `1.13` | 97,890,000.00 USD | 0.00 USD | 97,890,000.00 USD | 5,450.00 USD | 55,710.00 USD | 0.00 USD |
| `1D` | `1.13` | 89,440,000.00 USD | 0.00 USD | 89,440,000.00 USD | 6,330.00 USD | 101,970.00 USD | 318,110.00 USD |
| `7D` | `1.13` | 97,830,000.00 USD | 0.00 USD | 97,830,000.00 USD | 69,750.00 USD | 93,260.00 USD | 108,230.00 USD |
| `1D` | `1.13` | 89,010,000.00 USD | 0.00 USD | 89,010,000.00 USD | 88,690.00 USD | 39,080.00 USD | 40,030.00 USD |
| `7D` | `1.13` | 97,560,000.00 USD | 0.00 USD | 97,560,000.00 USD | 74,920.00 USD | 99,410.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 88,850,000.00 USD | 0.00 USD | 88,850,000.00 USD | 4,270.00 USD | 151,320.00 USD | 175,830.00 USD |
| `7D` | `1.14` | 97,160,000.00 USD | 0.00 USD | 97,160,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD |
| `1D` | `1.14` | 88,510,000.00 USD | 0.00 USD | 88,510,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD |
| `7D` | `1.14` | 96,620,000.00 USD | 0.00 USD | 96,620,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 88,290,000.00 USD | 0.00 USD | 88,290,000.00 USD | 26,280.00 USD | 52,050.00 USD | 107,470.00 USD |
| `7D` | `1.14` | 96,600,000.00 USD | 0.00 USD | 96,600,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD |
| `1D` | `1.14` | 88,100,000.00 USD | 0.00 USD | 88,100,000.00 USD | 29,510.00 USD | 10,830.00 USD | 153,170.00 USD |
| `7D` | `1.14` | 96,250,000.00 USD | 0.00 USD | 96,250,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 87,910,000.00 USD | 0.00 USD | 87,910,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 96,110,000.00 USD | 0.00 USD | 96,110,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `1D` | `1.15` | 87,770,000.00 USD | 0.00 USD | 87,770,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 96,100,000.00 USD | 0.00 USD | 96,100,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.15` | 96,040,000.00 USD | 0.00 USD | 96,040,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `1D` | `1.15` | 87,730,000.00 USD | 0.00 USD | 87,730,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 95,670,000.00 USD | 0.00 USD | 95,670,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.15` | 95,510,000.00 USD | 0.00 USD | 95,510,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 87,710,000.00 USD | 0.00 USD | 87,710,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 95,350,000.00 USD | 0.00 USD | 95,350,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 87,510,000.00 USD | 0.00 USD | 87,510,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 94,470,000.00 USD | 0.00 USD | 94,470,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 87,170,000.00 USD | 0.00 USD | 87,170,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD |
| `7D` | `1.16` | 94,240,000.00 USD | 0.00 USD | 94,240,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 125,390.00 USD | 15,500.00 USD | 433,350.00 USD |
| `7D` | `1.16` | 93,370,000.00 USD | 0.00 USD | 93,370,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 86,470,000.00 USD | 0.00 USD | 86,470,000.00 USD | 196,310.00 USD | 74,700.00 USD | 134,620.00 USD |
| `7D` | `1.16` | 92,290,000.00 USD | 0.00 USD | 92,290,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 189,220.00 USD | 289,860.00 USD | 292,640.00 USD |
| `7D` | `1.16` | 90,990,000.00 USD | 0.00 USD | 90,990,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 85,300,000.00 USD | 0.00 USD | 85,300,000.00 USD | 73,960.00 USD | 29,590.00 USD | 473,830.00 USD |
| `7D` | `1.17` | 89,320,000.00 USD | 0.00 USD | 89,320,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 84,720,000.00 USD | 0.00 USD | 84,720,000.00 USD | 121,070.00 USD | 109,760.00 USD | 102,520.00 USD |
| `7D` | `1.17` | 87,980,000.00 USD | 0.00 USD | 87,980,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 84,390,000.00 USD | 0.00 USD | 84,390,000.00 USD | 101,220.00 USD | 95,020.00 USD | 206,520.00 USD |
| `7D` | `1.17` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 83,980,000.00 USD | 0.00 USD | 83,980,000.00 USD | 361,890.00 USD | 3,910.00 USD | 415,800.00 USD |
| `7D` | `1.17` | 84,870,000.00 USD | 0.00 USD | 84,870,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 83,200,000.00 USD | 0.00 USD | 83,200,000.00 USD | 104,550.00 USD | 79,710.00 USD | 338,000.00 USD |
| `7D` | `1.17` | 83,670,000.00 USD | 0.00 USD | 83,670,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 82,680,000.00 USD | 0.00 USD | 82,680,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD |
| `7D` | `1.18` | 82,100,000.00 USD | 0.00 USD | 82,100,000.00 USD | 181,850.00 USD | 71,240.00 USD | 372,750.00 USD |
| `1D` | `1.18` | 81,730,000.00 USD | 0.00 USD | 81,730,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD |
| `7D` | `1.18` | 81,480,000.00 USD | 0.00 USD | 81,480,000.00 USD | 85,020.00 USD | 73,410.00 USD | 483,980.00 USD |
| `1D` | `1.18` | 81,360,000.00 USD | 0.00 USD | 81,360,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD |
| `7D` | `1.18` | 80,830,000.00 USD | 0.00 USD | 80,830,000.00 USD | 267,580.00 USD | 134,360.00 USD | 200,920.00 USD |
| `1D` | `1.18` | 81,030,000.00 USD | 0.00 USD | 81,030,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD |
| `7D` | `1.18` | 80,230,000.00 USD | 0.00 USD | 80,230,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 80,860,000.00 USD | 0.00 USD | 80,860,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD |
| `7D` | `1.18` | 79,960,000.00 USD | 0.00 USD | 79,960,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD |
| `7D` | `1.19` | 78,860,000.00 USD | 0.00 USD | 78,860,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 79,590,000.00 USD | 0.00 USD | 79,590,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD |
| `7D` | `1.19` | 78,010,000.00 USD | 0.00 USD | 78,010,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD |
| `1D` | `1.19` | 78,310,000.00 USD | 0.00 USD | 78,310,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD |
| `7D` | `1.19` | 77,220,000.00 USD | 0.00 USD | 77,220,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD |
| `1D` | `1.19` | 76,570,000.00 USD | 0.00 USD | 76,570,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD |
| `7D` | `1.19` | 76,240,000.00 USD | 0.00 USD | 76,240,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 76,090,000.00 USD | 0.00 USD | 76,090,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD |
| `7D` | `1.19` | 74,880,000.00 USD | 0.00 USD | 74,880,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD |
| `1D` | `1.20` | 74,980,000.00 USD | 0.00 USD | 74,980,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD |
| `7D` | `1.20` | 74,050,000.00 USD | 0.00 USD | 74,050,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD |
| `1D` | `1.20` | 72,400,000.00 USD | 0.00 USD | 72,400,000.00 USD | 748,570.00 USD | 87,450.00 USD | 794,380.00 USD |
| `7D` | `1.20` | 72,470,000.00 USD | 0.00 USD | 72,470,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 70,770,000.00 USD | 0.00 USD | 70,770,000.00 USD | 179,370.00 USD | 934,870.00 USD | 1,510,000.00 USD |
| `7D` | `1.20` | 69,460,000.00 USD | 0.00 USD | 69,460,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD |
| `1D` | `1.20` | 68,140,000.00 USD | 0.00 USD | 68,140,000.00 USD | 873,590.00 USD | 570,220.00 USD | 2,020,000.00 USD |
| `7D` | `1.20` | 68,000,000.00 USD | 0.00 USD | 68,000,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD |
| `1D` | `1.20` | 64,680,000.00 USD | 0.00 USD | 64,680,000.00 USD | 356,900.00 USD | 134,770.00 USD | 839,260.00 USD |
| `7D` | `1.20` | 67,120,000.00 USD | 0.00 USD | 67,120,000.00 USD | 47,500.00 USD | 723,100.00 USD | 155,510.00 USD |
| `1D` | `1.21` | 63,350,000.00 USD | 0.00 USD | 63,350,000.00 USD | 363,980.00 USD | 935,640.00 USD | 376,690.00 USD |
| `7D` | `1.21` | 66,200,000.00 USD | 0.00 USD | 66,200,000.00 USD | 0.00 USD | 77,080.00 USD | 0.00 USD |
| `1D` | `1.21` | 61,680,000.00 USD | 0.00 USD | 61,680,000.00 USD | 866,390.00 USD | 210,790.00 USD | 1,780,000.00 USD |
| `7D` | `1.21` | 66,120,000.00 USD | 0.00 USD | 66,120,000.00 USD | 556,190.00 USD | 0.00 USD | 387,800.00 USD |
| `1D` | `1.21` | 58,810,000.00 USD | 0.00 USD | 58,810,000.00 USD | 1,680,000.00 USD | 245,020.00 USD | 950,050.00 USD |
| `7D` | `1.21` | 65,180,000.00 USD | 0.00 USD | 65,180,000.00 USD | 257,960.00 USD | 498,260.00 USD | 3,090,000.00 USD |
| `1D` | `1.21` | 55,940,000.00 USD | 0.00 USD | 55,940,000.00 USD | 205,850.00 USD | 723,700.00 USD | 1,910,000.00 USD |
| `7D` | `1.21` | 61,330,000.00 USD | 0.00 USD | 61,330,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD |
| `1D` | `1.21` | 53,100,000.00 USD | 0.00 USD | 53,100,000.00 USD | 1,480,000.00 USD | 334,090.00 USD | 1,300,000.00 USD |
| `7D` | `1.21` | 59,080,000.00 USD | 0.00 USD | 59,080,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD |
| `1D` | `1.22` | 49,990,000.00 USD | 0.00 USD | 49,990,000.00 USD | 56,590.00 USD | 268,640.00 USD | 1,010,000.00 USD |
| `7D` | `1.22` | 57,550,000.00 USD | 0.00 USD | 57,550,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD |
| `1D` | `1.22` | 48,650,000.00 USD | 0.00 USD | 48,650,000.00 USD | 307,460.00 USD | 66,380.00 USD | 536,520.00 USD |
| `7D` | `1.22` | 57,150,000.00 USD | 0.00 USD | 57,150,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 47,740,000.00 USD | 0.00 USD | 47,740,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD |
| `7D` | `1.22` | 56,410,000.00 USD | 0.00 USD | 56,410,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 47,480,000.00 USD | 0.00 USD | 47,480,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD |
| `7D` | `1.22` | 55,330,000.00 USD | 0.00 USD | 55,330,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD |
| `1D` | `1.22` | 46,790,000.00 USD | 0.00 USD | 46,790,000.00 USD | 124,230.00 USD | 5,400.00 USD | 359,060.00 USD |
| `7D` | `1.22` | 55,150,000.00 USD | 0.00 USD | 55,150,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 46,300,000.00 USD | 0.00 USD | 46,300,000.00 USD | 586,370.00 USD | 613,210.00 USD | 3,190,000.00 USD |
| `7D` | `1.23` | 54,900,000.00 USD | 0.00 USD | 54,900,000.00 USD | 112,770.00 USD | 802,580.00 USD | 482,570.00 USD |
| `1D` | `1.23` | 41,910,000.00 USD | 0.00 USD | 41,910,000.00 USD | 256,900.00 USD | 267,560.00 USD | 415,360.00 USD |
| `7D` | `1.23` | 53,500,000.00 USD | 0.00 USD | 53,500,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD |
| `1D` | `1.23` | 40,970,000.00 USD | 0.00 USD | 40,970,000.00 USD | 638,880.00 USD | 1,200,000.00 USD | 2,810,000.00 USD |
| `7D` | `1.23` | 52,460,000.00 USD | 0.00 USD | 52,460,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,110,000.00 USD |
| `1D` | `1.23` | 36,320,000.00 USD | 0.00 USD | 36,320,000.00 USD | 202,670.00 USD | 1,290,000.00 USD | 2,980,000.00 USD |
| `7D` | `1.23` | 50,000,000.00 USD | 0.00 USD | 50,000,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 31,850,000.00 USD | 0.00 USD | 31,850,000.00 USD | 1,550,000.00 USD | 677,020.00 USD | 2,680,000.00 USD |
| `7D` | `1.23` | 46,310,000.00 USD | 0.00 USD | 46,310,000.00 USD | 1,660,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD |
| `1D` | `1.24` | 26,940,000.00 USD | 0.00 USD | 26,940,000.00 USD | 424,470.00 USD | 1,530,000.00 USD | 2,140,000.00 USD |
| `7D` | `1.24` | 38,970,000.00 USD | 0.00 USD | 38,970,000.00 USD | 2,040,000.00 USD | 1,820,000.00 USD | 2,740,000.00 USD |
| `1D` | `1.24` | 22,850,000.00 USD | 0.00 USD | 22,850,000.00 USD | 283,950.00 USD | 567,990.00 USD | 632,550.00 USD |
| `7D` | `1.24` | 32,370,000.00 USD | 0.00 USD | 32,370,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 4,430,000.00 USD |
| `1D` | `1.24` | 21,360,000.00 USD | 0.00 USD | 21,360,000.00 USD | 918,230.00 USD | 955,200.00 USD | 3,020,000.00 USD |
| `7D` | `1.24` | 22,940,000.00 USD | 0.00 USD | 22,940,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 1,280,000.00 USD |
| `1D` | `1.24` | 16,460,000.00 USD | 0.00 USD | 16,460,000.00 USD | 843,320.00 USD | 624,890.00 USD | 1,990,000.00 USD |
| `7D` | `1.24` | 18,360,000.00 USD | 0.00 USD | 18,360,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 1,080,000.00 USD |
| `1D` | `1.24` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 828,020.00 USD | 969,790.00 USD | 2,890,000.00 USD |
| `7D` | `1.24` | 15,640,000.00 USD | 0.00 USD | 15,640,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 1,550,000.00 USD |
| `1D` | `1.25` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 1,700,000.00 USD | 472,540.00 USD | 1,290,000.00 USD |
| `7D` | `1.25` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 3,770,000.00 USD | 337,070.00 USD | 2,290,000.00 USD |
| `1D` | `1.25` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 1,020,000.00 USD | 769,380.00 USD | 1,700,000.00 USD |
| `7D` | `1.25` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 3,600,000.00 USD |
| `1D` | `1.25` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 712,500.00 USD | 652,640.00 USD |
| `7D` | `1.25` | 489,680.00 USD | 0.00 USD | 489,680.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 4,760.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD |
| `7D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 3,370.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD |
| `1D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 63,660.00 USD | 63,660.00 USD | 0.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 254,670.00 USD | 254,670.00 USD | 0.00 USD | 0.00 USD | 12,640.00 USD | 242,040.00 USD |
| `7D` | `1.26` | 222,480.00 USD | 222,480.00 USD | 0.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD |
| `1D` | `1.26` | 339,940.00 USD | 339,940.00 USD | 0.00 USD | 73,940.00 USD | 11,320.00 USD | 0.00 USD |
| `7D` | `1.26` | 242,310.00 USD | 242,310.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD |
| `1D` | `1.26` | 376,090.00 USD | 376,090.00 USD | 0.00 USD | 0.00 USD | 24,960.00 USD | 11,190.00 USD |
| `7D` | `1.26` | 334,770.00 USD | 334,770.00 USD | 0.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD |
| `1D` | `1.26` | 627,970.00 USD | 627,970.00 USD | 0.00 USD | 229,640.00 USD | 8,660.00 USD | 13,580.00 USD |
| `7D` | `1.26` | 482,320.00 USD | 482,320.00 USD | 0.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD |
| `1D` | `1.26` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 409,480.00 USD | 308,120.00 USD | 1,160,000.00 USD |
| `7D` | `1.26` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 542,940.00 USD | 1,020,000.00 USD |
| `1D` | `1.26` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 636,140.00 USD | 423,290.00 USD | 643,560.00 USD |
| `7D` | `1.27` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 4,260,000.00 USD | 9,150.00 USD | 20,550.00 USD |
| `1D` | `1.27` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 845,960.00 USD | 221,950.00 USD | 682,820.00 USD |
| `7D` | `1.27` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 1,870,000.00 USD | 3,110,000.00 USD |
| `1D` | `1.27` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 715,560.00 USD | 1,940,000.00 USD | 1,570,000.00 USD |
| `7D` | `1.27` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 138,500.00 USD | 2,750,000.00 USD | 1,900,000.00 USD |
| `1D` | `1.27` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 734,620.00 USD | 1,400,000.00 USD | 3,160,000.00 USD |
| `7D` | `1.27` | 24,190,000.00 USD | 24,190,000.00 USD | 0.00 USD | 1,680,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD |
| `1D` | `1.27` | 21,430,000.00 USD | 21,430,000.00 USD | 0.00 USD | 2,180,000.00 USD | 1,080,000.00 USD | 2,690,000.00 USD |
| `7D` | `1.27` | 40,430,000.00 USD | 40,430,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 10,660,000.00 USD |
| `1D` | `1.27` | 29,440,000.00 USD | 29,440,000.00 USD | 0.00 USD | 1,130,000.00 USD | 2,630,000.00 USD | 4,260,000.00 USD |
| `7D` | `1.28` | 55,300,000.00 USD | 55,300,000.00 USD | 0.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,640,000.00 USD |
| `1D` | `1.28` | 36,890,000.00 USD | 36,890,000.00 USD | 0.00 USD | 2,160,000.00 USD | 1,560,000.00 USD | 3,730,000.00 USD |
| `7D` | `1.28` | 74,460,000.00 USD | 74,460,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 7,620,000.00 USD |
| `1D` | `1.28` | 45,870,000.00 USD | 45,870,000.00 USD | 0.00 USD | 2,550,000.00 USD | 2,330,000.00 USD | 4,110,000.00 USD |
| `7D` | `1.28` | 77,560,000.00 USD | 77,560,000.00 USD | 0.00 USD | 0.00 USD | 1,700,000.00 USD | 1,400,000.00 USD |
| `1D` | `1.28` | 49,670,000.00 USD | 49,670,000.00 USD | 0.00 USD | 393,830.00 USD | 759,560.00 USD | 2,640,000.00 USD |
| `7D` | `1.28` | 79,580,000.00 USD | 79,580,000.00 USD | 0.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD |
| `1D` | `1.28` | 53,480,000.00 USD | 53,480,000.00 USD | 0.00 USD | 1,330,000.00 USD | 472,310.00 USD | 2,010,000.00 USD |
| `7D` | `1.28` | 83,170,000.00 USD | 83,170,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `1.28` | 56,860,000.00 USD | 56,860,000.00 USD | 0.00 USD | 817,320.00 USD | 640,040.00 USD | 1,920,000.00 USD |
| `7D` | `1.29` | 87,740,000.00 USD | 87,740,000.00 USD | 0.00 USD | 796,960.00 USD | 1,300,000.00 USD | 2,480,000.00 USD |
| `1D` | `1.29` | 59,870,000.00 USD | 59,870,000.00 USD | 0.00 USD | 864,310.00 USD | 1,100,000.00 USD | 1,040,000.00 USD |
| `7D` | `1.29` | 88,460,000.00 USD | 88,460,000.00 USD | 0.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 60,990,000.00 USD | 60,990,000.00 USD | 0.00 USD | 454,460.00 USD | 148,440.00 USD | 518,370.00 USD |
| `7D` | `1.29` | 90,070,000.00 USD | 90,070,000.00 USD | 0.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD |
| `1D` | `1.29` | 62,370,000.00 USD | 62,370,000.00 USD | 0.00 USD | 186,090.00 USD | 270,800.00 USD | 919,950.00 USD |
| `7D` | `1.29` | 92,660,000.00 USD | 92,660,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD |
| `1D` | `1.29` | 66,170,000.00 USD | 66,170,000.00 USD | 0.00 USD | 570,020.00 USD | 278,090.00 USD | 2,960,000.00 USD |
| `7D` | `1.29` | 96,310,000.00 USD | 96,310,000.00 USD | 0.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD |
| `1D` | `1.29` | 72,340,000.00 USD | 72,340,000.00 USD | 0.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD |
| `7D` | `1.30` | 103,600,000.00 USD | 103,600,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD |
| `1D` | `1.30` | 74,920,000.00 USD | 74,920,000.00 USD | 0.00 USD | 554,720.00 USD | 706,700.00 USD | 1,320,000.00 USD |
| `7D` | `1.30` | 105,550,000.00 USD | 105,550,000.00 USD | 0.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 75,740,000.00 USD | 75,740,000.00 USD | 0.00 USD | 401,840.00 USD | 109,620.00 USD | 313,530.00 USD |
| `7D` | `1.30` | 107,920,000.00 USD | 107,920,000.00 USD | 0.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD |
| `1D` | `1.30` | 78,630,000.00 USD | 78,630,000.00 USD | 0.00 USD | 674,250.00 USD | 469,750.00 USD | 1,740,000.00 USD |
| `7D` | `1.30` | 108,950,000.00 USD | 108,950,000.00 USD | 0.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD |
| `1D` | `1.30` | 80,630,000.00 USD | 80,630,000.00 USD | 0.00 USD | 803,540.00 USD | 645,090.00 USD | 554,270.00 USD |
| `7D` | `1.30` | 111,760,000.00 USD | 111,760,000.00 USD | 0.00 USD | 0.00 USD | 2,170,000.00 USD | 635,640.00 USD |
| `1D` | `1.30` | 82,130,000.00 USD | 82,130,000.00 USD | 0.00 USD | 372,370.00 USD | 664,450.00 USD | 458,020.00 USD |
| `7D` | `1.31` | 113,770,000.00 USD | 113,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 238,140.00 USD | 0.00 USD |
| `1D` | `1.31` | 85,110,000.00 USD | 85,110,000.00 USD | 0.00 USD | 777,430.00 USD | 253,070.00 USD | 1,950,000.00 USD |
| `7D` | `1.31` | 118,930,000.00 USD | 118,930,000.00 USD | 0.00 USD | 1,550,000.00 USD | 821,310.00 USD | 2,790,000.00 USD |
| `1D` | `1.31` | 88,750,000.00 USD | 88,750,000.00 USD | 0.00 USD | 1,240,000.00 USD | 442,560.00 USD | 1,960,000.00 USD |
| `7D` | `1.31` | 121,340,000.00 USD | 121,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 414,180.00 USD | 647,870.00 USD |
| `1D` | `1.31` | 91,330,000.00 USD | 91,330,000.00 USD | 0.00 USD | 944,800.00 USD | 557,880.00 USD | 1,080,000.00 USD |
| `7D` | `1.31` | 126,220,000.00 USD | 126,220,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD |
| `1D` | `1.31` | 93,250,000.00 USD | 93,250,000.00 USD | 0.00 USD | 515,120.00 USD | 340,250.00 USD | 1,060,000.00 USD |
| `7D` | `1.31` | 127,510,000.00 USD | 127,510,000.00 USD | 0.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.31` | 95,390,000.00 USD | 95,390,000.00 USD | 0.00 USD | 437,130.00 USD | 320,320.00 USD | 1,390,000.00 USD |
| `7D` | `1.32` | 132,220,000.00 USD | 132,220,000.00 USD | 0.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.32` | 100,510,000.00 USD | 100,510,000.00 USD | 0.00 USD | 1,280,000.00 USD | 753,370.00 USD | 3,080,000.00 USD |
| `7D` | `1.32` | 137,320,000.00 USD | 137,320,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD |
| `1D` | `1.32` | 105,260,000.00 USD | 105,260,000.00 USD | 0.00 USD | 1,560,000.00 USD | 684,990.00 USD | 2,500,000.00 USD |
| `7D` | `1.32` | 139,350,000.00 USD | 139,350,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 107,810,000.00 USD | 107,810,000.00 USD | 0.00 USD | 1,340,000.00 USD | 339,190.00 USD | 867,210.00 USD |
| `7D` | `1.32` | 142,700,000.00 USD | 142,700,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 110,720,000.00 USD | 110,720,000.00 USD | 0.00 USD | 885,300.00 USD | 460,840.00 USD | 1,560,000.00 USD |
| `7D` | `1.32` | 145,480,000.00 USD | 145,480,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.32` | 111,720,000.00 USD | 111,720,000.00 USD | 0.00 USD | 599,940.00 USD | 61,650.00 USD | 341,150.00 USD |
| `7D` | `1.33` | 147,280,000.00 USD | 147,280,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 112,790,000.00 USD | 112,790,000.00 USD | 0.00 USD | 412,050.00 USD | 225,260.00 USD | 436,220.00 USD |
| `7D` | `1.33` | 148,380,000.00 USD | 148,380,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 114,170,000.00 USD | 114,170,000.00 USD | 0.00 USD | 504,110.00 USD | 72,470.00 USD | 798,680.00 USD |
| `7D` | `1.33` | 150,100,000.00 USD | 150,100,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 116,340,000.00 USD | 116,340,000.00 USD | 0.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 152,560,000.00 USD | 152,560,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 118,290,000.00 USD | 118,290,000.00 USD | 0.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD |
| `7D` | `1.33` | 154,590,000.00 USD | 154,590,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.33` | 119,630,000.00 USD | 119,630,000.00 USD | 0.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD |
| `7D` | `1.34` | 156,130,000.00 USD | 156,130,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 120,370,000.00 USD | 120,370,000.00 USD | 0.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD |
| `7D` | `1.34` | 158,570,000.00 USD | 158,570,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 120,910,000.00 USD | 120,910,000.00 USD | 0.00 USD | 179,460.00 USD | 82,510.00 USD | 282,570.00 USD |
| `7D` | `1.34` | 160,430,000.00 USD | 160,430,000.00 USD | 0.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 122,230,000.00 USD | 122,230,000.00 USD | 0.00 USD | 629,770.00 USD | 243,030.00 USD | 439,220.00 USD |
| `7D` | `1.34` | 165,890,000.00 USD | 165,890,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 123,750,000.00 USD | 123,750,000.00 USD | 0.00 USD | 697,160.00 USD | 223,580.00 USD | 606,640.00 USD |
| `7D` | `1.34` | 173,020,000.00 USD | 173,020,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.34` | 125,060,000.00 USD | 125,060,000.00 USD | 0.00 USD | 497,250.00 USD | 284,400.00 USD | 524,700.00 USD |
| `7D` | `1.35` | 181,270,000.00 USD | 181,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD |
| `1D` | `1.35` | 125,450,000.00 USD | 125,450,000.00 USD | 0.00 USD | 127,140.00 USD | 103,350.00 USD | 158,220.00 USD |
| `7D` | `1.35` | 189,020,000.00 USD | 189,020,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 126,000,000.00 USD | 126,000,000.00 USD | 0.00 USD | 249,180.00 USD | 23,180.00 USD | 275,620.00 USD |
| `7D` | `1.35` | 197,040,000.00 USD | 197,040,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 126,410,000.00 USD | 126,410,000.00 USD | 0.00 USD | 146,270.00 USD | 30,410.00 USD | 237,640.00 USD |
| `7D` | `1.35` | 206,160,000.00 USD | 206,160,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 126,560,000.00 USD | 126,560,000.00 USD | 0.00 USD | 66,220.00 USD | 30,780.00 USD | 49,480.00 USD |
| `7D` | `1.35` | 212,910,000.00 USD | 212,910,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.35` | 127,070,000.00 USD | 127,070,000.00 USD | 0.00 USD | 86,720.00 USD | 34,870.00 USD | 395,480.00 USD |
| `7D` | `1.36` | 219,250,000.00 USD | 219,250,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 128,030,000.00 USD | 128,030,000.00 USD | 0.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 221,790,000.00 USD | 221,790,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD |
| `1D` | `1.36` | 128,370,000.00 USD | 128,370,000.00 USD | 0.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD |
| `7D` | `1.36` | 224,800,000.00 USD | 224,800,000.00 USD | 0.00 USD | 1,460,000.00 USD | 339,580.00 USD | 1,210,000.00 USD |
| `1D` | `1.36` | 129,020,000.00 USD | 129,020,000.00 USD | 0.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD |
| `7D` | `1.36` | 228,580,000.00 USD | 228,580,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 129,320,000.00 USD | 129,320,000.00 USD | 0.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD |
| `7D` | `1.36` | 231,320,000.00 USD | 231,320,000.00 USD | 0.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD |
| `1D` | `1.36` | 129,440,000.00 USD | 129,440,000.00 USD | 0.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD |
| `7D` | `1.37` | 232,140,000.00 USD | 232,140,000.00 USD | 0.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 129,700,000.00 USD | 129,700,000.00 USD | 0.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD |
| `7D` | `1.37` | 233,190,000.00 USD | 233,190,000.00 USD | 0.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 129,840,000.00 USD | 129,840,000.00 USD | 0.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD |
| `7D` | `1.37` | 234,510,000.00 USD | 234,510,000.00 USD | 0.00 USD | 367,350.00 USD | 211,750.00 USD | 733,820.00 USD |
| `1D` | `1.37` | 129,940,000.00 USD | 129,940,000.00 USD | 0.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD |
| `7D` | `1.37` | 235,740,000.00 USD | 235,740,000.00 USD | 0.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD |
| `1D` | `1.37` | 130,040,000.00 USD | 130,040,000.00 USD | 0.00 USD | 5,470.00 USD | 2,610.00 USD | 85,390.00 USD |
| `7D` | `1.37` | 237,410,000.00 USD | 237,410,000.00 USD | 0.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD |
| `1D` | `1.38` | 130,360,000.00 USD | 130,360,000.00 USD | 0.00 USD | 97,300.00 USD | 49,730.00 USD | 172,240.00 USD |
| `7D` | `1.38` | 238,440,000.00 USD | 238,440,000.00 USD | 0.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD |
| `1D` | `1.38` | 130,580,000.00 USD | 130,580,000.00 USD | 0.00 USD | 31,450.00 USD | 41,790.00 USD | 153,110.00 USD |
| `7D` | `1.38` | 239,900,000.00 USD | 239,900,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD |
| `1D` | `1.38` | 130,930,000.00 USD | 130,930,000.00 USD | 0.00 USD | 74,730.00 USD | 82,720.00 USD | 192,970.00 USD |
| `7D` | `1.38` | 241,600,000.00 USD | 241,600,000.00 USD | 0.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 131,000,000.00 USD | 131,000,000.00 USD | 0.00 USD | 2,300.00 USD | 65,520.00 USD | 0.00 USD |
| `7D` | `1.38` | 243,460,000.00 USD | 243,460,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD |
| `1D` | `1.38` | 131,360,000.00 USD | 131,360,000.00 USD | 0.00 USD | 4,030.00 USD | 36,450.00 USD | 318,110.00 USD |
| `7D` | `1.38` | 244,340,000.00 USD | 244,340,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 228,560.00 USD |
| `1D` | `1.39` | 131,530,000.00 USD | 131,530,000.00 USD | 0.00 USD | 88,690.00 USD | 39,080.00 USD | 40,030.00 USD |
| `7D` | `1.39` | 245,370,000.00 USD | 245,370,000.00 USD | 0.00 USD | 377,810.00 USD | 234,230.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 131,860,000.00 USD | 131,860,000.00 USD | 0.00 USD | 4,270.00 USD | 151,320.00 USD | 175,830.00 USD |
| `7D` | `1.39` | 246,580,000.00 USD | 246,580,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD |
| `1D` | `1.39` | 132,090,000.00 USD | 132,090,000.00 USD | 0.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD |
| `7D` | `1.39` | 247,330,000.00 USD | 247,330,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `1D` | `1.39` | 132,110,000.00 USD | 132,110,000.00 USD | 0.00 USD | 0.00 USD | 18,650.00 USD | 0.00 USD |
| `7D` | `1.39` | 247,860,000.00 USD | 247,860,000.00 USD | 0.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD |
| `1D` | `1.39` | 132,270,000.00 USD | 132,270,000.00 USD | 0.00 USD | 26,280.00 USD | 33,400.00 USD | 107,470.00 USD |
| `7D` | `1.39` | 248,030,000.00 USD | 248,030,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD |
| `1D` | `1.40` | 132,460,000.00 USD | 132,460,000.00 USD | 0.00 USD | 29,510.00 USD | 10,080.00 USD | 151,080.00 USD |
| `7D` | `1.40` | 248,250,000.00 USD | 248,250,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.40` | 132,590,000.00 USD | 132,590,000.00 USD | 0.00 USD | 77,100.00 USD | 0.00 USD | 49,840.00 USD |
| `7D` | `1.40` | 248,250,000.00 USD | 248,250,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 248,320,000.00 USD | 248,320,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 248,390,000.00 USD | 248,390,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 248,690,000.00 USD | 248,690,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 248,840,000.00 USD | 248,840,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 248,980,000.00 USD | 248,980,000.00 USD | 0.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD |
| `7D` | `1.41` | 249,260,000.00 USD | 249,260,000.00 USD | 0.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.84B` | Total OI Tokens: `2,262,135,862.6 XRP`
  * 1h OI Change: `+0.40%` | 4h OI Change: `+0.41%` | 24h OI Change: `-4.69%`
  * Exchange Breakdown: Binance=`427.41M` | Bybit=`323.14M` | OKX=`95.93M` | Hyperliquid=`200.74M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-71.36K` | Last 24h: `21.94K` | Last 3d: `414.05K` | Last 7d: `1.06M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0083%` | **USDT OKX** | `-0.0156%` |
| **USDT Bybit** | `-0.0311%` | **USDT KuCoin** | `-0.0104%` |
| **USDT MEXC** | `0.0083%` | **USDT BingX** | `0.0084%` |
| **USDT Gate** | `-0.0034%` | **USDT Bitget** | `-0.0064%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0041%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `41.17%` | `58.83%` | `0.70` | 362,380,000.00 USD |
| `15M` | `Binance` | `48.27%` | `51.73%` | `0.93` | 113,630,000.00 USD |
| `15M` | `OKX` | `53.07%` | `46.93%` | `1.13` | 67,890,000.00 USD |
| `15M` | `Bybit` | `50.96%` | `49.04%` | `1.04` | 18,140,000.00 USD |
| `15M` | `KuCoin` | `43.97%` | `56.03%` | `0.78` | 1,560,000.00 USD |
| `15M` | `Gate` | `43.48%` | `56.52%` | `0.77` | 58,410,000.00 USD |
| `15M` | `Bitget` | `52.44%` | `47.56%` | `1.10` | 15,430,000.00 USD |
| `15M` | `BingX` | `31.06%` | `68.94%` | `0.45` | 3,390,000.00 USD |
| `15M` | `MEXC` | `34.24%` | `65.76%` | `0.52` | 10,730,000.00 USD |
| `15M` | `Bitunix` | `54.67%` | `45.33%` | `1.21` | 12,130,000.00 USD |
| `15M` | `Hyperliquid` | `35.86%` | `64.14%` | `0.56` | 39,470,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.65%` | `50.35%` | `0.99` | 681,300.00 USD |
| `15M` | `Crypto.com` | `58.27%` | `41.73%` | `1.40` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,670,000.00 USD |
| `15M` | `HTX` | `65.56%` | `34.44%` | `1.90` | 7,010,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 2,870,000.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 78,990.00 USD |
| `15M` | `Kraken` | `7.42%` | `92.58%` | `0.08` | 1,410,000.00 USD |
| `15M` | `Aster` | `12.37%` | `87.63%` | `0.14` | 3,620,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.69%` | `53.31%` | `0.88` | 4,240,000.00 USD |
| `15M` | `Whale Positions` | `48.27%` | `51.73%` | `0.93` | 113,630,000.00 USD |
| `15M` | `Global Accounts` | `41.17%` | `58.83%` | `0.70` | 362,380,000.00 USD |
| `1H` | `XRP` | `49.93%` | `50.07%` | `1.00` | 100,510,000.00 USD |
| `1H` | `Binance` | `51.29%` | `48.71%` | `1.05` | 32,150,000.00 USD |
| `1H` | `OKX` | `48.55%` | `51.45%` | `0.94` | 8,550,000.00 USD |
| `1H` | `Bybit` | `60.46%` | `39.54%` | `1.53` | 16,080,000.00 USD |
| `1H` | `KuCoin` | `57.84%` | `42.16%` | `1.37` | 974,580.00 USD |
| `1H` | `Gate` | `56.2%` | `43.8%` | `1.28` | 6,890,000.00 USD |
| `1H` | `Bitget` | `51.34%` | `48.66%` | `1.06` | 8,110,000.00 USD |
| `1H` | `BingX` | `28.78%` | `71.22%` | `0.40` | 2,160,000.00 USD |
| `1H` | `MEXC` | `46.45%` | `53.55%` | `0.87` | 11,390,000.00 USD |
| `1H` | `Bitunix` | `47.64%` | `52.36%` | `0.91` | 3,470,000.00 USD |
| `1H` | `Hyperliquid` | `72.03%` | `27.97%` | `2.58` | 3,780,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.66%` | `43.34%` | `1.31` | 486,860.00 USD |
| `1H` | `Crypto.com` | `56.48%` | `43.52%` | `1.30` | 240,120.00 USD |
| `1H` | `WhiteBIT` | `1.44%` | `98.56%` | `0.01` | 4,540,000.00 USD |
| `1H` | `HTX` | `46.76%` | `53.24%` | `0.88` | 34,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.89%` | `80.11%` | `0.25` | 721,110.00 USD |
| `1H` | `Aster` | `26.41%` | `73.59%` | `0.36` | 780,700.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.39%` | `39.61%` | `1.52` | 161,670.00 USD |
| `1H` | `Whale Positions` | `51.29%` | `48.71%` | `1.05` | 32,150,000.00 USD |
| `1H` | `Global Accounts` | `49.93%` | `50.07%` | `1.00` | 100,510,000.00 USD |
| `4H` | `XRP` | `48.99%` | `51.01%` | `0.96` | 466,950,000.00 USD |
| `4H` | `Binance` | `50.41%` | `49.59%` | `1.02` | 158,360,000.00 USD |
| `4H` | `OKX` | `47.9%` | `52.1%` | `0.92` | 56,130,000.00 USD |
| `4H` | `Bybit` | `51.07%` | `48.93%` | `1.04` | 75,240,000.00 USD |
| `4H` | `KuCoin` | `49.4%` | `50.6%` | `0.98` | 4,310,000.00 USD |
| `4H` | `Gate` | `56.92%` | `43.08%` | `1.32` | 23,780,000.00 USD |
| `4H` | `Bitget` | `50.27%` | `49.73%` | `1.01` | 33,380,000.00 USD |
| `4H` | `BingX` | `20.92%` | `79.08%` | `0.26` | 12,320,000.00 USD |
| `4H` | `MEXC` | `49.64%` | `50.36%` | `0.99` | 59,790,000.00 USD |
| `4H` | `Bitunix` | `46.44%` | `53.56%` | `0.87` | 17,120,000.00 USD |
| `4H` | `Hyperliquid` | `61.16%` | `38.84%` | `1.57` | 10,220,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `58.02%` | `41.98%` | `1.38` | 1,760,000.00 USD |
| `4H` | `Crypto.com` | `51.32%` | `48.68%` | `1.05` | 854,510.00 USD |
| `4H` | `WhiteBIT` | `16.75%` | `83.25%` | `0.20` | 8,960,000.00 USD |
| `4H` | `HTX` | `60.92%` | `39.08%` | `1.56` | 258,900.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `20.25%` | `79.75%` | `0.25` | 742,230.00 USD |
| `4H` | `Aster` | `35.67%` | `64.33%` | `0.55` | 3,190,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.95%` | `46.05%` | `1.17` | 547,980.00 USD |
| `4H` | `Whale Positions` | `50.41%` | `49.59%` | `1.02` | 158,360,000.00 USD |
| `4H` | `Global Accounts` | `48.99%` | `51.01%` | `0.96` | 466,950,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.26` | 12,144,743.65 USD | 6,990,191.91 USD | 5,154,551.74 USD | 1,835,640.16 USD | `+15.11%` | `14B / 14S` |
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.26` | 6,182,046.10 USD | 3,146,565.70 USD | 3,035,480.40 USD | 111,085.31 USD | `+1.80%` | `10B / 10S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.27` | `1.26` | 7,034,590.80 USD | 2,893,991.39 USD | 4,140,599.40 USD | -1,246,608.01 USD | `-17.72%` | `5B / 17S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,492,630.91 USD | 2,570,238.18 USD | 4,922,392.73 USD | -2,352,154.55 USD | `-31.39%` | `6B / 29S` |
| `0:00 UTC` | `1.26` | `1.25` | `1.26` | `1.26` | `1.25` | 16,486,336.19 USD | 7,622,620.76 USD | 8,863,715.43 USD | -1,241,094.67 USD | `-7.53%` | `10B / 24S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 8,615,974.43 USD | 3,921,066.30 USD | 4,694,908.13 USD | -773,841.83 USD | `-8.98%` | `6B / 4S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 8,443,326.41 USD | 4,197,283.82 USD | 4,246,042.59 USD | -48,758.76 USD | `-0.58%` | `16B / 5S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 7,390,743.66 USD | 4,309,267.00 USD | 3,081,476.65 USD | 1,227,790.35 USD | `+16.61%` | `9B / 4S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,021,258.97 USD | 2,177,548.60 USD | 2,843,710.37 USD | -666,161.77 USD | `-13.27%` | `1B / 5S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 1,027,335.22 USD | 504,331.61 USD | 523,003.61 USD | -18,672.00 USD | `-1.82%` | `1B / 1S` |

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
| `5m` | -135,350.00 USD | -187,160.00 USD | **`DISTRIBUTION`** |
| `15m` | 409,120.00 USD | -537,150.00 USD | **`DISTRIBUTION`** |
| `30m` | 260,970.00 USD | -1,640,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 3,000,000.00 USD | 3,190,000.00 USD | **`ACCUMULATION`** |
| `2h` | 683,930.00 USD | -14,690,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 7,510,000.00 USD | -204,420.00 USD | **`ACCUMULATION`** |
| `6h` | 19,640,000.00 USD | 30,810,000.00 USD | **`ACCUMULATION`** |
| `8h` | 20,550,000.00 USD | -10,960,000.00 USD | **`ACCUMULATION`** |
| `12h` | -10,020,000.00 USD | -7,730,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -47,750,000.00 USD | -130,810,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -116,330,000.00 USD | -224,160,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -592,740,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-135.35K` | 15m=`+409.12K` | 1h=`+3.00M` | 24h=`-47.75M`
* Futures Capital Netflows: 5m=`-187.16K` | 15m=`-537.15K` | 1h=`+3.19M` | 24h=`-130.81M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.23` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0273` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `4.24`
  * Mathematical Lot Sizing: **`8.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.47` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-1.75`
  * Mathematical Lot Sizing: **`8.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
