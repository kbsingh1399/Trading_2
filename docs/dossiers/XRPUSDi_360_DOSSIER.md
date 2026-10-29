# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 03:19:12 IST` (`2026-10-29 21:49:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.26` | **Mid Price**: `1.25`
- **Spread Points**: `4.00` | **Spread BPS**: `31.90 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.28` | VWAP Z-Score: `-1.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0120` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.35` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.34` | Lower -3.00σ Band: `1.22`
  * Upper +2.51σ Band: `1.33` | Lower -2.51σ Band: `1.23`
  * Upper +2.01σ Band: `1.32` | Lower -2.01σ Band: `1.24`
  * Upper +2.00σ Band: `1.32` | Lower -2.00σ Band: `1.24`
  * Upper +1.28σ Band: `1.31` | Lower -1.28σ Band: `1.26`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.26`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.26` | EMA-20=`1.27` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.28` (Slope: `+0.0000`) | EMA-100=`1.29`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.3252`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.33` | 24H Low=`1.22` | Weekly High=`1.34` | Weekly Low=`1.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.65%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.16%`)
  * Value Area Low (VAL) = `1.25` (Distance: `+0.28%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.32` | Weekly POC=`1.29` | Weekly VAL=`1.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.23`
  * London Session (08:00-16:00 UTC): High=`1.26` | Low=`1.25`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.25`
  * Initial Balance (First Hour): IB High=`1.26` | IB Low=`1.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.25` - `1.26`
  * Optimal Trade Entry (OTE 0.705): `1.26`
  * Structural Invalidation Anchor (0.786): `1.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `5,460,009` | 6,878,945.73 USD | 1,435,373.25 USD | `+20.87%` | -76,554,798.59 USD | `+0.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `3,796,815` | 4,793,385.13 USD | 402,857.67 USD | `+8.40%` | -76,151,940.91 USD | `+0.52` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.26` | `1.26` | `1.25` | `1.25` | `3,179,748` | 4,000,797.30 USD | -640,326.94 USD | `-16.00%` | -76,792,267.86 USD | `+0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.24` | `1.25` | `1.23` | `1.25` | `34,560,808` | 42,899,530.36 USD | 2,631,101.42 USD | `+6.13%` | -76,312,636.23 USD | `+0.88` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.26` | `28,716,400` | 36,075,332.57 USD | -1,677,535.61 USD | `-4.65%` | -77,990,171.83 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.26` | `1.26` | `1.25` | `1.25` | `12,457,973` | 15,699,977.70 USD | 1,181,267.49 USD | `+7.52%` | -76,808,904.34 USD | `+0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.28` | `17,509,907` | 22,469,016.48 USD | -1,419,504.92 USD | `-6.32%` | -40,597,161.54 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.28` | `1.28` | `1.22` | `1.24` | `208,906,305` | 260,797,546.37 USD | -37,805,029.03 USD | `-14.50%` | -78,402,190.57 USD | `-3.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.24` | `1.26` | `1.23` | `1.25` | `75,837,115` | 94,802,675.27 USD | 2,080,683.49 USD | `+2.19%` | -76,321,507.08 USD | `+0.60` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `284,580,397` | 355,395,736.17 USD | -35,652,823.15 USD | `-10.03%` | -75,591,852.96 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `284,580,397` | 355,395,736.17 USD | -35,652,823.15 USD | `-10.03%` | -75,591,852.96 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `ASK` | `1.25` | `39721.0000` | 49,849.85 USD | 172,206.86 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `15982.0000` | 20,055.81 USD | 122,357.01 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `23608.0000` | 29,623.32 USD | 102,301.20 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `1.25` | `4051.0000` | 5,082.79 USD | 72,677.88 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `1.25` | `13754.0000` | 17,255.77 USD | 67,595.09 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `1.25` | `40127.0000` | 50,339.32 USD | 50,339.32 USD | `8 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.25` | `0.00%` | `-` |
| `BID` | `1.25` | `7231.0000` | 9,070.57 USD | 9,070.57 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `1.25` | `8930.0000` | 11,200.90 USD | 20,271.47 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `1.25` | `8954.0000` | 11,230.11 USD | 31,501.57 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `1.25` | `20296.0000` | 25,453.21 USD | 56,954.79 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `1.25` | `83963.0000` | 105,289.60 USD | 162,244.39 USD | `12 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `14959.0000` | 18,757.09 USD | 181,001.48 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `38524.0000` | 48,301.39 USD | 229,302.87 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `1.25` | `285883.0000` | 358,411.52 USD | 587,714.39 USD | `15 orders` | `-0.06%` | `-` |
| `BID` | `1.25` | `74177.0000` | 92,988.29 USD | 680,702.67 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `1.25` | `63021.0000` | 78,996.82 USD | 759,699.50 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `110667.0000` | 138,710.02 USD | 898,409.51 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `70653.0000` | 88,549.40 USD | 986,958.92 USD | `10 orders` | `-0.09%` | `-` |
| `BID` | `1.25` | `213414.0000` | 267,450.42 USD | 1,254,409.34 USD | `7 orders` | `-0.10%` | `-` |
| `BID` | `1.25` | `30151.0000` | 37,782.22 USD | 1,292,191.56 USD | `8 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `335990.0000` | 420,995.47 USD | 1,713,187.03 USD | `8 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `67911.0000` | 85,085.69 USD | 1,798,272.72 USD | `9 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `34784.0000` | 43,577.40 USD | 1,841,850.12 USD | `6 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `20452.0000` | 25,620.22 USD | 1,867,470.34 USD | `7 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `77722.0000` | 97,354.58 USD | 1,964,824.92 USD | `11 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `23270.0000` | 29,145.67 USD | 1,993,970.59 USD | `11 orders` | `-0.16%` | `-` |
| `ASK` | `1.26` | `43012.0000` | 54,040.28 USD | 1,111,889.63 USD | `6 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `7832.0000` | 9,839.34 USD | 1,057,849.35 USD | `3 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `49171.0000` | 61,768.61 USD | 1,048,010.01 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `73504.0000` | 92,328.37 USD | 986,241.40 USD | `12 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `16313.0000` | 20,489.13 USD | 893,913.03 USD | `9 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `25425.0000` | 31,931.26 USD | 873,423.90 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `242640.0000` | 304,707.31 USD | 841,492.64 USD | `9 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `39308.0000` | 49,359.06 USD | 536,785.33 USD | `10 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `49934.0000` | 62,697.13 USD | 487,426.27 USD | `10 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `40996.0000` | 51,470.48 USD | 424,729.14 USD | `14 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `63792.0000` | 80,084.48 USD | 373,258.67 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `41566.0000` | 52,177.80 USD | 293,174.19 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `37694.0000` | 47,313.51 USD | 240,996.39 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `17111.0000` | 21,476.02 USD | 193,682.88 USD | `5 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:15:37 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `25` | `0x31b1...1434` | `LONG` | 44,076,440.13 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,497,556.86 USD | `+10.20%` | `10X Cross` |
| `89` | `0x5b5d...c060` | `SHORT` | 20,089,413.46 USD | `15,964,251.00` | `1.44` | `1.26` | `12.27` | 2,826,655.25 USD | `+14.07%` | `5X Cross` |
| `157` | `0xb83d...6e36` | `SHORT` | 13,276,645.01 USD | `10,555,450.00` | `1.50` | `1.26` | `15.10` | 2,545,924.63 USD | `+19.18%` | `5X Cross` |
| `242` | `0x58f0...0d20` | `LONG` | 9,466,335.62 USD | `7,526,704.00` | `1.25` | `1.26` | `1.22` | 75,171.07 USD | `+0.79%` | `20X Cross` |
| `383` | `0x77ee...a018` | `LONG` | 6,216,208.38 USD | `4,943,700.00` | `1.27` | `1.26` | `0.3481` | -62,290.62 USD | `-1.00%` | `20X Cross` |
| `430` | `0xca49...53c8` | `SHORT` | 5,202,165.81 USD | `4,138,886.00` | `1.44` | `1.26` | `4.74` | 751,156.92 USD | `+14.44%` | `20X Cross` |
| `479` | `0xecb6...2b00` | `SHORT` | 4,690,839.92 USD | `3,731,774.00` | `1.29` | `1.26` | `8.89` | 117,734.62 USD | `+2.51%` | `10X Cross` |
| `497` | `0xfc27...9d9d` | `SHORT` | 4,496,433.63 USD | `3,576,546.00` | `1.30` | `1.26` | `5.99` | 169,442.10 USD | `+3.77%` | `20X Cross` |
| `500` | `0x610b...b613` | `LONG` | 4,457,220.88 USD | `3,543,946.00` | `1.44` | `1.26` | `0.7995` | -642,771.72 USD | `-14.42%` | `5X Cross` |
| `519` | `0xdd53...2b13` | `SHORT` | 4,228,336.00 USD | `3,360,089.00` | `1.43` | `1.26` | `19.76` | 581,264.01 USD | `+13.75%` | `3X Cross` |
| `609` | `0x9946...0852` | `SHORT` | 3,761,850.58 USD | `2,990,580.00` | `1.43` | `1.26` | `1.75` | 502,099.89 USD | `+13.35%` | `20X Cross` |
| `677` | `0xc30c...a4c9` | `SHORT` | 3,430,415.74 USD | `2,727,531.00` | `1.42` | `1.26` | `1.61` | 433,832.45 USD | `+12.65%` | `7X Cross` |
| `697` | `0x9aa5...58af` | `SHORT` | 3,287,654.79 USD | `2,604,083.00` | `1.46` | `1.26` | `4.54` | 510,065.87 USD | `+15.51%` | `20X Cross` |
| `715` | `0xf48f...10fe` | `LONG` | 3,228,776.29 USD | `2,565,779.00` | `1.53` | `1.26` | `1.00` | -695,864.43 USD | `-21.55%` | `4X Cross` |
| `745` | `0x023a...2355` | `SHORT` | 3,106,828.51 USD | `2,469,657.00` | `1.32` | `1.26` | `4.44` | 158,073.64 USD | `+5.09%` | `20X Cross` |
| `751` | `0x45d2...4029` | `SHORT` | 3,081,703.90 USD | `2,453,000.00` | `1.48` | `1.26` | `17.87` | 556,576.52 USD | `+18.06%` | `20X Cross` |
| `940` | `0xfc66...ca06` | `SHORT` | 2,421,911.57 USD | `1,926,433.00` | `1.30` | `1.26` | `16.34` | 83,982.64 USD | `+3.47%` | `20X Cross` |
| `1064` | `0xc179...e0c8` | `SHORT` | 2,097,122.24 USD | `1,668,355.00` | `1.30` | `1.26` | `5.08` | 73,713.13 USD | `+3.51%` | `10X Cross` |
| `1085` | `0xeadc...9d55` | `LONG` | 2,044,355.89 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 85,512.87 USD | `+4.18%` | `20X Cross` |
| `1175` | `0x94b2...599e` | `SHORT` | 1,937,271.15 USD | `1,540,696.00` | `1.36` | `1.26` | `1.86` | 163,195.30 USD | `+8.42%` | `20X Cross` |
| `1185` | `0xbcd4...0dd2` | `SHORT` | 1,917,017.24 USD | `1,529,461.00` | `1.31` | `1.26` | `2.04` | 87,527.36 USD | `+4.57%` | `20X Cross` |
| `1195` | `0x3fc5...c0c1` | `SHORT` | 1,901,364.45 USD | `1,511,779.00` | `1.52` | `1.26` | `2.62` | 390,250.15 USD | `+20.52%` | `20X Cross` |
| `1225` | `0x31ef...f715` | `LONG` | 1,855,208.12 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -344,057.29 USD | `-18.55%` | `3X Isolated` |
| `1235` | `0x4537...8732` | `SHORT` | 1,839,033.58 USD | `1,461,642.00` | `1.25` | `1.26` | `1.93` | -15,370.12 USD | `-0.84%` | `10X Cross` |
| `1275` | `0x7737...bf66` | `SHORT` | 1,783,935.44 USD | `1,413,466.00` | `1.41` | `1.26` | `13.61` | 214,933.21 USD | `+12.05%` | `10X Cross` |
| `1293` | `0xe9d1...d2d3` | `SHORT` | 1,765,408.73 USD | `1,404,462.00` | `1.27` | `1.26` | `2.03` | 18,548.40 USD | `+1.05%` | `10X Cross` |
| `1351` | `0x95da...2328` | `LONG` | 1,660,599.58 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0639` | -133,041.52 USD | `-8.01%` | `5X Cross` |
| `1354` | `0xef96...9383` | `SHORT` | 1,659,687.85 USD | `1,319,097.00` | `1.34` | `1.26` | `4.50` | 107,756.63 USD | `+6.49%` | `20X Cross` |
| `1377` | `0xee2b...d67e` | `LONG` | 1,637,688.25 USD | `1,306,284.00` | `1.55` | `1.26` | `0.3763` | -392,966.65 USD | `-24.00%` | `4X Cross` |
| `1429` | `0x215d...f80a` | `LONG` | 1,579,867.75 USD | `1,251,777.00` | `1.32` | `1.26` | `1.15` | -74,586.48 USD | `-4.72%` | `14X Cross` |
| `1449` | `0x2482...0e55` | `LONG` | 1,558,698.46 USD | `1,239,226.00` | `1.33` | `1.26` | `1.21` | -91,668.59 USD | `-5.88%` | `20X Isolated` |
| `1470` | `0x123d...3bff` | `LONG` | 1,528,519.28 USD | `1,215,329.00` | `1.35` | `1.26` | `0.000000` | -108,549.94 USD | `-7.10%` | `10X Cross` |
| `1513` | `0x5fa3...35b7` | `SHORT` | 1,472,864.28 USD | `1,170,615.00` | `1.31` | `1.26` | `3.35` | 57,121.79 USD | `+3.88%` | `20X Cross` |
| `1533` | `0xdf95...7d72` | `SHORT` | 1,458,738.44 USD | `1,160,492.00` | `1.37` | `1.26` | `35.73` | 134,693.18 USD | `+9.23%` | `20X Cross` |
| `1681` | `0xb1ce...681b` | `LONG` | 1,280,270.29 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -243,786.20 USD | `-19.04%` | `4X Isolated` |
| `1781` | `0x3c36...461a` | `LONG` | 1,182,020.13 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -37,060.49 USD | `-3.14%` | `10X Cross` |
| `2001` | `0xbfc7...80b4` | `SHORT` | 1,005,920.00 USD | `800,000.00` | `1.48` | `1.26` | `6.65` | 177,534.65 USD | `+17.65%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,298.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.30K USD at 1.3182 USD [API] | `2026-10-28 12:25:08` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 2,778.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.78K USD at 1.3237 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 922.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.92K USD at 1.3237 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 2,338.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.34K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 264.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.26K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 2,481.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.48K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 1,703.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.70K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 3,999.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.00K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,074.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.07K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,535.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 6.54K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 153.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3236 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 221.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.22K USD at 1.3235 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,074.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.07K USD at 1.3235 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 3,999.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.00K USD at 1.3235 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 2,030.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.03K USD at 1.3235 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 1,422.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.42K USD at 1.3234 USD [API] | `2026-10-20 14:07:04` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 57,838.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 57.84K USD at 1.2956 USD [API] | `2026-10-16 17:18:07` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,597.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.60K USD at 1.3189 USD [API] | `2026-10-28 12:28:40` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3284 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 19,275.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 19.28K USD at 1.3178 USD [API] | `2026-10-28 12:31:05` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,137.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.14K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,665.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.67K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,341.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.34K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,386.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.39K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,939.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.94K USD at 1.3153 USD [API] | `2026-10-28 12:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3153 USD [API] | `2026-10-28 12:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,055.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.06K USD at 1.3153 USD [API] | `2026-10-28 12:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3140 USD [API] | `2026-10-28 12:39:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 12,828.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.83K USD at 1.3147 USD [API] | `2026-10-28 12:40:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 12.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3330 USD [API] | `2026-10-27 23:48:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 12.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3330 USD [API] | `2026-10-27 23:48:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 53.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3330 USD [API] | `2026-10-27 23:48:29` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 224.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.22K USD at 1.3308 USD [API] | `2026-10-27 23:46:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,936.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.94K USD at 1.3160 USD [API] | `2026-10-28 12:44:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,897.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.90K USD at 1.3147 USD [API] | `2026-10-28 12:45:54` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,739.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.74K USD at 1.3147 USD [API] | `2026-10-28 12:45:54` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3147 USD [API] | `2026-10-28 12:45:54` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,007.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3149 USD [API] | `2026-10-28 12:49:56` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3150 USD [API] | `2026-10-28 12:49:56` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 13,385.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.39K USD at 1.3163 USD [API] | `2026-10-28 13:24:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3169 USD [API] | `2026-10-28 13:35:00` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,810.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.81K USD at 1.3211 USD [API] | `2026-10-28 13:40:07` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,784.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.78K USD at 1.3156 USD [API] | `2026-10-28 13:49:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 15,126.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.13K USD at 1.3156 USD [API] | `2026-10-28 13:51:21` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,367.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.37K USD at 1.3156 USD [API] | `2026-10-28 13:51:21` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 10,276.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.28K USD at 1.3150 USD [API] | `2026-10-28 13:52:34` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,104.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.10K USD at 1.3150 USD [API] | `2026-10-28 13:52:34` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,914.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.91K USD at 1.3150 USD [API] | `2026-10-28 13:52:34` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 11,323.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.32K USD at 1.3119 USD [API] | `2026-10-28 14:31:36` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 12,101.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.10K USD at 1.3104 USD [API] | `2026-10-28 14:35:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,762.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.76K USD at 1.3097 USD [API] | `2026-10-28 14:37:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,822.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.82K USD at 1.3097 USD [API] | `2026-10-28 14:37:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,048.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.05K USD at 1.3106 USD [API] | `2026-10-28 14:39:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3106 USD [API] | `2026-10-28 14:39:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,328.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.33K USD at 1.3108 USD [API] | `2026-10-28 14:40:55` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 85.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.2610 USD [API] | `2026-10-24 15:16:21` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 872.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.87K USD at 1.2610 USD [API] | `2026-10-24 15:16:21` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 3,747.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.75K USD at 1.2610 USD [API] | `2026-10-24 15:16:21` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,533.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.53K USD at 1.3116 USD [API] | `2026-10-28 14:41:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,016.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.02K USD at 1.3130 USD [API] | `2026-10-28 14:42:18` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3119 USD [API] | `2026-10-28 14:43:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,484.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.48K USD at 1.3121 USD [API] | `2026-10-28 14:47:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3122 USD [API] | `2026-10-28 14:47:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3115 USD [API] | `2026-10-28 14:46:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,186.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.19K USD at 1.3115 USD [API] | `2026-10-28 14:46:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 33.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.03K USD at 1.3444 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 22.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3434 USD [API] | `2026-10-28 02:18:02` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 288.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.29K USD at 1.3434 USD [API] | `2026-10-28 02:18:02` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 406.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.41K USD at 1.3379 USD [API] | `2026-10-28 02:11:35` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 12.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3371 USD [API] | `2026-10-28 01:42:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3131 USD [API] | `2026-10-28 14:49:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3131 USD [API] | `2026-10-28 14:49:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3116 USD [API] | `2026-10-28 14:51:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3117 USD [API] | `2026-10-28 14:51:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 8,303.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.30K USD at 1.3118 USD [API] | `2026-10-28 14:58:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3118 USD [API] | `2026-10-28 14:58:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,411.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.41K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,944.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.94K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,259.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.26K USD at 1.3149 USD [API] | `2026-10-28 15:03:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,346.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.35K USD at 1.3149 USD [API] | `2026-10-28 15:03:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3115 USD [API] | `2026-10-28 15:37:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,448.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.45K USD at 1.2734 USD [API] | `2026-10-24 09:43:05` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,516.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.52K USD at 1.2734 USD [API] | `2026-10-24 09:43:05` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 384.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.38K USD at 1.2734 USD [API] | `2026-10-24 09:43:05` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,665.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.67K USD at 1.2896 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,535.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.54K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,011.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.01K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,593.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.59K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 56.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.06K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 688.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.69K USD at 1.3420 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,594.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.59K USD at 1.3687 USD [API] | `2026-10-08 15:20:54` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 75.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.08K USD at 1.3687 USD [API] | `2026-10-08 15:20:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 3,048.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.05K USD at 1.4364 USD [API] | `2026-10-07 13:34:46` |
| `ANNOUNCEMENT` | `INFO` | `1.53` | 2,943.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.94K USD at 1.5252 USD [API] | `2026-09-26 18:38:35` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3130 USD [API] | `2026-10-28 15:42:20` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,230.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.23K USD at 1.3108 USD [API] | `2026-10-28 15:48:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,372.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.37K USD at 1.3103 USD [API] | `2026-10-28 15:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3106 USD [API] | `2026-10-28 15:59:31` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3122 USD [API] | `2026-10-28 16:14:28` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3121 USD [API] | `2026-10-28 16:14:28` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,745.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.75K USD at 1.3111 USD [API] | `2026-10-28 16:19:56` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 5,071.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.07K USD at 1.4880 USD [API] | `2026-08-22 05:16:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 8,919.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.92K USD at 1.4750 USD [API] | `2026-08-22 05:10:38` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3104 USD [API] | `2026-10-28 16:37:56` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3103 USD [API] | `2026-10-28 16:37:56` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3102 USD [API] | `2026-10-28 16:37:56` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 13,015.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.02K USD at 1.3164 USD [API] | `2026-10-28 16:55:05` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,141.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.14K USD at 1.3127 USD [API] | `2026-10-28 17:32:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 10,189.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.19K USD at 1.3127 USD [API] | `2026-10-28 17:32:23` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,057.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.06K USD at 1.3158 USD [API] | `2026-10-28 17:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,892.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.89K USD at 1.3172 USD [API] | `2026-10-28 17:44:02` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3200 USD [API] | `2026-10-28 17:50:51` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3193 USD [API] | `2026-10-28 17:54:39` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,972.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.97K USD at 1.3186 USD [API] | `2026-10-28 17:56:50` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,452.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.45K USD at 1.3186 USD [API] | `2026-10-28 18:00:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,380.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.38K USD at 1.3243 USD [API] | `2026-10-28 18:04:24` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,315.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.32K USD at 1.3211 USD [API] | `2026-10-28 18:06:08` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 47,579.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 47.58K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.00K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.00K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,273.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.27K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,430.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.43K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,677.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.68K USD at 1.3198 USD [API] | `2026-10-28 18:19:21` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3198 USD [API] | `2026-10-28 18:19:21` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,003.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.00K USD at 1.3195 USD [API] | `2026-10-28 18:21:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,920.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.92K USD at 1.3200 USD [API] | `2026-10-27 12:48:45` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 496.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.50K USD at 1.3445 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 505.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.51K USD at 1.3444 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,445.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.45K USD at 1.3443 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,850.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.85K USD at 1.3443 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 457.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.46K USD at 1.3443 USD [API] | `2026-10-20 22:40:11` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,000,000.00 USD, Dist: `+4.08%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 3,500,000.00 USD, Dist: `+6.18%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+6.24%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+6.33%`) | Long MP=`1.27` (Vol: 2,800,000.00 USD, Dist: `--0.44%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 354.96 USD | 70,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 25,040.00 USD | 70,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 2,740.00 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 6,670.00 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 14,270.00 USD | 70,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 1,380.00 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 114,130.00 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 708.53 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 12,510.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 30,620.00 USD | 70,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 17,450.00 USD | 70,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 421.88 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 346.88 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 530,350.00 USD | 70,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 7,840.00 USD | 70,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 2,210,000.00 USD | 70,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 1,600.00 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 551.96 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 1,930.00 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 63,660.00 USD | 67,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 6,260.00 USD | 67,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 2,890.00 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 1,780.00 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 588.50 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 7,290.00 USD | 67,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 633.26 USD | 67,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 3,540.00 USD | 67,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,870.00 USD | 67,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 168,060.00 USD | 67,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 2,980.00 USD | 67,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 29,530.00 USD | 67,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 32,370.00 USD | 67,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,130.00 USD | 67,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 22,110.00 USD | 67,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 1,560.00 USD | 67,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 1,030.00 USD | 67,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 15,700.00 USD | 67,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 30,110.00 USD | 67,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 21,150.00 USD | 67,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 7,810.00 USD | 67,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 28,070.00 USD | 67,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,440.00 USD | 67,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 244,720.00 USD | 67,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 21,910.00 USD | 67,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 62,010.00 USD | 67,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 107,370.00 USD | 67,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 218,080.00 USD | 66,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 5,760.00 USD | 66,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 27,790.00 USD | 66,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 12,080.00 USD | 66,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 23,890.00 USD | 66,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 14,900.00 USD | 66,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 55,220.00 USD | 66,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 3,000,000.00 USD | 66,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 283,660.00 USD | 63,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 72,590.00 USD | 63,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 6,060.00 USD | 63,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 85,730.00 USD | 63,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 371,120.00 USD | 63,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 102,690.00 USD | 62,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 148,850.00 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 50,060.00 USD | 62,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 147,510.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 87,100.00 USD | 62,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 97,300.00 USD | 62,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 116,510.00 USD | 62,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,920,000.00 USD | 62,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 158,540.00 USD | 28,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 450,730.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 98,040.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 451,390.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 181,040.00 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 3,440,000.00 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 23,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 1,280,000.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,130,000.00 USD | 19,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 532,180.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 440,750.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 758,070.00 USD | 17,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 603,690.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 65,590.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 68,720,000.00 USD | 68,720,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 36,290,000.00 USD | 36,290,000.00 USD | 17,310.00 USD | 0.00 USD | 116,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 36,150,000.00 USD | 36,150,000.00 USD | 18,710.00 USD | 937.65 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 68,700,000.00 USD | 68,700,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 249,040.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 36,130,000.00 USD | 36,130,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 68,690,000.00 USD | 68,690,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 36,130,000.00 USD | 36,130,000.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 36,110,000.00 USD | 36,110,000.00 USD | 0.00 USD | 47,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 68,610,000.00 USD | 68,610,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 267,340.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 36,070,000.00 USD | 36,070,000.00 USD | 0.00 USD | 1,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 68,610,000.00 USD | 68,610,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 36,060,000.00 USD | 36,060,000.00 USD | 0.00 USD | 107,140.00 USD | 76,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 68,410,000.00 USD | 68,410,000.00 USD | 5,450.00 USD | 2,160.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 35,880,000.00 USD | 35,880,000.00 USD | 0.00 USD | 0.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 68,400,000.00 USD | 68,400,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 35,710,000.00 USD | 35,710,000.00 USD | 7,260.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 67,920,000.00 USD | 67,920,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 215,570.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 35,700,000.00 USD | 35,700,000.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 67,680,000.00 USD | 67,680,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 67,580,000.00 USD | 67,580,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 35,560,000.00 USD | 35,560,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 67,570,000.00 USD | 67,570,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 35,500,000.00 USD | 35,500,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 67,510,000.00 USD | 67,510,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 35,420,000.00 USD | 35,420,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 67,390,000.00 USD | 67,390,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 1,710,000.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 67,380,000.00 USD | 67,380,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 35,290,000.00 USD | 35,290,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 67,240,000.00 USD | 67,240,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 66,880,000.00 USD | 66,880,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 35,280,000.00 USD | 35,280,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 66,720,000.00 USD | 66,720,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 35,210,000.00 USD | 35,210,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 66,330,000.00 USD | 66,330,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 482,060.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 34,830,000.00 USD | 34,830,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 65,690,000.00 USD | 65,690,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 34,710,000.00 USD | 34,710,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 64,890,000.00 USD | 64,890,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 34,530,000.00 USD | 34,530,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 64,360,000.00 USD | 64,360,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 34,150,000.00 USD | 34,150,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 63,340,000.00 USD | 63,340,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 33,410,000.00 USD | 33,410,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 61,970,000.00 USD | 61,970,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,510,000.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 32,980,000.00 USD | 32,980,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 61,340,000.00 USD | 61,340,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 32,650,000.00 USD | 32,650,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 59,960,000.00 USD | 59,960,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 32,470,000.00 USD | 32,470,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 58,450,000.00 USD | 58,450,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 32,310,000.00 USD | 32,310,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 57,070,000.00 USD | 57,070,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 32,090,000.00 USD | 32,090,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 56,270,000.00 USD | 56,270,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 481,590.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 31,820,000.00 USD | 31,820,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 55,390,000.00 USD | 55,390,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 31,600,000.00 USD | 31,600,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 54,930,000.00 USD | 54,930,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 31,420,000.00 USD | 31,420,000.00 USD | 71,950.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 54,210,000.00 USD | 54,210,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 31,320,000.00 USD | 31,320,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 53,840,000.00 USD | 53,840,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 31,240,000.00 USD | 31,240,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 53,710,000.00 USD | 53,710,000.00 USD | 127,700.00 USD | 97,270.00 USD | 289,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 741,690.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 31,130,000.00 USD | 31,130,000.00 USD | 59,140.00 USD | 145,870.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 53,200,000.00 USD | 53,200,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 30,900,000.00 USD | 30,900,000.00 USD | 189,200.00 USD | 3,790.00 USD | 599,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 52,420,000.00 USD | 52,420,000.00 USD | 182,110.00 USD | 132,500.00 USD | 278,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 30,100,000.00 USD | 30,100,000.00 USD | 10,800.00 USD | 3,540.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 51,830,000.00 USD | 51,830,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 30,070,000.00 USD | 30,070,000.00 USD | 40,460.00 USD | 17,460.00 USD | 92,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 51,140,000.00 USD | 51,140,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 29,920,000.00 USD | 29,920,000.00 USD | 66,050.00 USD | 221,930.00 USD | 69,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 50,480,000.00 USD | 50,480,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 379,860.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 29,560,000.00 USD | 29,560,000.00 USD | 31,180.00 USD | 6,070.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 49,770,000.00 USD | 49,770,000.00 USD | 5,350.00 USD | 97,860.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 29,490,000.00 USD | 29,490,000.00 USD | 39,940.00 USD | 0.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 49,480,000.00 USD | 49,480,000.00 USD | 67,200.00 USD | 57,670.00 USD | 201,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 29,440,000.00 USD | 29,440,000.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 49,150,000.00 USD | 49,150,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 29,440,000.00 USD | 29,440,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 49,070,000.00 USD | 49,070,000.00 USD | 202,570.00 USD | 53,170.00 USD | 534,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 29,440,000.00 USD | 29,440,000.00 USD | 31,120.00 USD | 106,230.00 USD | 191,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 48,280,000.00 USD | 48,280,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 9,230,000.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 29,110,000.00 USD | 29,110,000.00 USD | 0.00 USD | 163,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 48,190,000.00 USD | 48,190,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 28,940,000.00 USD | 28,940,000.00 USD | 0.00 USD | 67,350.00 USD | 415,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 48,090,000.00 USD | 48,090,000.00 USD | 468,800.00 USD | 518,690.00 USD | 368,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 28,460,000.00 USD | 28,460,000.00 USD | 135,040.00 USD | 244,960.00 USD | 91,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 46,740,000.00 USD | 46,740,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 27,990,000.00 USD | 27,990,000.00 USD | 419,060.00 USD | 334,050.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 45,490,000.00 USD | 45,490,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 26,010,000.00 USD | 26,010,000.00 USD | 9,150.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 45,080,000.00 USD | 45,080,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 710,620.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 25,980,000.00 USD | 25,980,000.00 USD | 117,720.00 USD | 0.00 USD | 122,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 44,910,000.00 USD | 44,910,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 25,740,000.00 USD | 25,740,000.00 USD | 174,270.00 USD | 380,580.00 USD | 135,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 44,360,000.00 USD | 44,360,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 25,050,000.00 USD | 25,050,000.00 USD | 157,550.00 USD | 6,840.00 USD | 208,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 44,060,000.00 USD | 44,060,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 24,680,000.00 USD | 24,680,000.00 USD | 0.00 USD | 211.25 USD | 47,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 43,560,000.00 USD | 43,560,000.00 USD | 0.00 USD | 191,360.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 24,630,000.00 USD | 24,630,000.00 USD | 40,080.00 USD | 486,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 42,350,000.00 USD | 42,350,000.00 USD | 627,450.00 USD | 191,250.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 421,580.00 USD | 425,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 22,940,000.00 USD | 22,940,000.00 USD | 449,150.00 USD | 0.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 41,520,000.00 USD | 41,520,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 21,340,000.00 USD | 21,340,000.00 USD | 48,560.00 USD | 8,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 41,060,000.00 USD | 41,060,000.00 USD | 0.00 USD | 917,970.00 USD | 995,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 21,280,000.00 USD | 21,280,000.00 USD | 191,290.00 USD | 563,770.00 USD | 543,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 39,150,000.00 USD | 39,150,000.00 USD | 782,590.00 USD | 479,460.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 19,990,000.00 USD | 19,990,000.00 USD | 271,900.00 USD | 757,410.00 USD | 831,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 37,880,000.00 USD | 37,880,000.00 USD | 656,500.00 USD | 597,200.00 USD | 112,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 18,120,000.00 USD | 18,120,000.00 USD | 86,170.00 USD | 134,700.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 36,510,000.00 USD | 36,510,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 4,170.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 233,740.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 34,450,000.00 USD | 34,450,000.00 USD | 1,640,000.00 USD | 1,110,000.00 USD | 719,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 17,630,000.00 USD | 17,630,000.00 USD | 0.00 USD | 244,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 30,980,000.00 USD | 30,980,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 17,390,000.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 340,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 29,210,000.00 USD | 29,210,000.00 USD | 1,820,000.00 USD | 0.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 17,040,000.00 USD | 17,040,000.00 USD | 112,970.00 USD | 655,230.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 25,440,000.00 USD | 25,440,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 15,020,000.00 USD | 15,020,000.00 USD | 721,110.00 USD | 0.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 23,530,000.00 USD | 23,530,000.00 USD | 2,670,000.00 USD | 923,130.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 8,790.00 USD | 8,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 11,960,000.00 USD | 11,960,000.00 USD | 861,120.00 USD | 351,240.00 USD | 551,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 18,260,000.00 USD | 18,260,000.00 USD | 2,330,000.00 USD | 2,110,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 10,190,000.00 USD | 10,190,000.00 USD | 218,430.00 USD | 1,300,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 13,820,000.00 USD | 13,820,000.00 USD | 2,720,000.00 USD | 1,770,000.00 USD | 51,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 6,650,000.00 USD | 6,650,000.00 USD | 1,110,000.00 USD | 489,510.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 9,290,000.00 USD | 9,290,000.00 USD | 2,810,000.00 USD | 888,720.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,890,000.00 USD | 3,890,000.00 USD | 351,630.00 USD | 0.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 5,540,000.00 USD | 5,540,000.00 USD | 1,240,000.00 USD | 403,270.00 USD | 104,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,530,000.00 USD | 3,530,000.00 USD | 551,630.00 USD | 0.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 3,790,000.00 USD | 3,790,000.00 USD | 998,540.00 USD | 0.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 39,570.00 USD | 48,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 2,970,000.00 USD | 2,970,000.00 USD | 1,460,000.00 USD | 2,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 2,770,000.00 USD | 2,770,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 1,510,000.00 USD | 1,510,000.00 USD | 1,030,000.00 USD | 2,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 592,290.00 USD | 592,290.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 476,680.00 USD | 476,680.00 USD | 472,940.00 USD | 3,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 485,150.00 USD | 485,150.00 USD | 0.00 USD | 0.00 USD | 485,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 1,660,000.00 USD | 1,660,000.00 USD | 424,010.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 3,320,000.00 USD | 3,320,000.00 USD | 424,010.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 23,320.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 8,850,000.00 USD | 8,850,000.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 45,120.00 USD | 93,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 6,020,000.00 USD | 6,020,000.00 USD | 39,860.00 USD | 1,030,000.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 21,710,000.00 USD | 21,710,000.00 USD | 2,620,000.00 USD | 1,990,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 1,930,000.00 USD | 794,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 26,480,000.00 USD | 26,480,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 780,430.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 29,320,000.00 USD | 29,320,000.00 USD | 178,380.00 USD | 2,540,000.00 USD | 123,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 12,790,000.00 USD | 12,790,000.00 USD | 961,090.00 USD | 583,330.00 USD | 57,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 34,050,000.00 USD | 34,050,000.00 USD | 186,960.00 USD | 3,970,000.00 USD | 567,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 15,770,000.00 USD | 15,770,000.00 USD | 60,090.00 USD | 1,220,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 48,430,000.00 USD | 48,430,000.00 USD | 4,420,000.00 USD | 1,750,000.00 USD | 8,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 234,140.00 USD | 327,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 21,010,000.00 USD | 21,010,000.00 USD | 481,200.00 USD | 1,850,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 66,700,000.00 USD | 66,700,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 34,280,000.00 USD | 34,280,000.00 USD | 6,010,000.00 USD | 2,730,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 72,800,000.00 USD | 72,800,000.00 USD | 3,260,000.00 USD | 1,750,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 37,120,000.00 USD | 37,120,000.00 USD | 188,330.00 USD | 1,960,000.00 USD | 695,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 73,750,000.00 USD | 73,750,000.00 USD | 0.00 USD | 873,350.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 38,910,000.00 USD | 38,910,000.00 USD | 547,110.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 75,380,000.00 USD | 75,380,000.00 USD | 1,080,000.00 USD | 478,060.00 USD | 67,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 40,870,000.00 USD | 40,870,000.00 USD | 673,540.00 USD | 418,710.00 USD | 869,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 78,970,000.00 USD | 78,970,000.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 102,990.00 USD | 430,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 42,880,000.00 USD | 42,880,000.00 USD | 303,010.00 USD | 687,930.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 80,140,000.00 USD | 80,140,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 43,890,000.00 USD | 43,890,000.00 USD | 584,100.00 USD | 411,690.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 80,250,000.00 USD | 80,250,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 43,910,000.00 USD | 43,910,000.00 USD | 18,290.00 USD | 3,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 82,340,000.00 USD | 82,340,000.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 45,700,000.00 USD | 45,700,000.00 USD | 369,880.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 82,760,000.00 USD | 82,760,000.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 49,640,000.00 USD | 49,640,000.00 USD | 1,110,000.00 USD | 305,230.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 92,400,000.00 USD | 92,400,000.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 1,550.00 USD | 432,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 54,550,000.00 USD | 54,550,000.00 USD | 1,400,000.00 USD | 1,120,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 93,630,000.00 USD | 93,630,000.00 USD | 209,360.00 USD | 393,370.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 55,280,000.00 USD | 55,280,000.00 USD | 344,680.00 USD | 422.50 USD | 383,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 95,050,000.00 USD | 95,050,000.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 55,950,000.00 USD | 55,950,000.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 96,310,000.00 USD | 96,310,000.00 USD | 0.00 USD | 286,660.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 58,110,000.00 USD | 58,110,000.00 USD | 602,010.00 USD | 897,120.00 USD | 659,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 99,310,000.00 USD | 99,310,000.00 USD | 0.00 USD | 2,510,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 58,830,000.00 USD | 58,830,000.00 USD | 188,510.00 USD | 204,330.00 USD | 319,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 4,310.00 USD | 436,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 60,120,000.00 USD | 60,120,000.00 USD | 493,480.00 USD | 477,560.00 USD | 320,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 102,320,000.00 USD | 102,320,000.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 63,110,000.00 USD | 63,110,000.00 USD | 767,340.00 USD | 278,540.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 106,580,000.00 USD | 106,580,000.00 USD | 1,480,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 65,710,000.00 USD | 65,710,000.00 USD | 908,870.00 USD | 396,100.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 109,840,000.00 USD | 109,840,000.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 69,030,000.00 USD | 69,030,000.00 USD | 1,800,000.00 USD | 778,210.00 USD | 745,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 112,690,000.00 USD | 112,690,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 70,750,000.00 USD | 70,750,000.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 115,140,000.00 USD | 115,140,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,700.00 USD | 438,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 76,520,000.00 USD | 76,520,000.00 USD | 222,150.00 USD | 1,680,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 119,770,000.00 USD | 119,770,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 83,320,000.00 USD | 83,320,000.00 USD | 2,080,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 122,850,000.00 USD | 122,850,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 86,630,000.00 USD | 86,630,000.00 USD | 1,680,000.00 USD | 608,860.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 124,680,000.00 USD | 124,680,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 91,270,000.00 USD | 91,270,000.00 USD | 1,870,000.00 USD | 845,300.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 129,130,000.00 USD | 129,130,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 94,320,000.00 USD | 94,320,000.00 USD | 1,770,000.00 USD | 259,620.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 131,500,000.00 USD | 131,500,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 46,520.00 USD | 484,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 96,610,000.00 USD | 96,610,000.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 132,040,000.00 USD | 132,040,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 98,800,000.00 USD | 98,800,000.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 133,190,000.00 USD | 133,190,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 101,240,000.00 USD | 101,240,000.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 134,910,000.00 USD | 134,910,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 103,500,000.00 USD | 103,500,000.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 138,970,000.00 USD | 138,970,000.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 105,830,000.00 USD | 105,830,000.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 139,510,000.00 USD | 139,510,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 3,460.00 USD | 488,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 108,270,000.00 USD | 108,270,000.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 141,460,000.00 USD | 141,460,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 110,950,000.00 USD | 110,950,000.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 143,800,000.00 USD | 143,800,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 113,420,000.00 USD | 113,420,000.00 USD | 1,020,000.00 USD | 362,960.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 148,510,000.00 USD | 148,510,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 116,920,000.00 USD | 116,920,000.00 USD | 1,630,000.00 USD | 729,880.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 154,180,000.00 USD | 154,180,000.00 USD | 1,730,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 120,190,000.00 USD | 120,190,000.00 USD | 1,470,000.00 USD | 626,040.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 165,240,000.00 USD | 165,240,000.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 1,920.00 USD | 490,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 121,420,000.00 USD | 121,420,000.00 USD | 498,430.00 USD | 251,400.00 USD | 481,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 172,360,000.00 USD | 172,360,000.00 USD | 2,410,000.00 USD | 2,230,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 122,680,000.00 USD | 122,680,000.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 182,670,000.00 USD | 182,670,000.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 124,170,000.00 USD | 124,170,000.00 USD | 771,840.00 USD | 229,490.00 USD | 488,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 190,440,000.00 USD | 190,440,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 125,490,000.00 USD | 125,490,000.00 USD | 558,120.00 USD | 207,050.00 USD | 556,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 198,760,000.00 USD | 198,760,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,860,000.00 USD | 126,860,000.00 USD | 503,350.00 USD | 201,050.00 USD | 668,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 206,990,000.00 USD | 206,990,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 23,410.00 USD | 513,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,080,000.00 USD | 128,080,000.00 USD | 510,040.00 USD | 122,540.00 USD | 579,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 211,090,000.00 USD | 211,090,000.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,940,000.00 USD | 128,940,000.00 USD | 412,060.00 USD | 41,890.00 USD | 409,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 214,870,000.00 USD | 214,870,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,520,000.00 USD | 129,520,000.00 USD | 266,880.00 USD | 78,370.00 USD | 233,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 217,010,000.00 USD | 217,010,000.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 130,180,000.00 USD | 130,180,000.00 USD | 241,460.00 USD | 104,340.00 USD | 321,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 221,110,000.00 USD | 221,110,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 130,320,000.00 USD | 130,320,000.00 USD | 80,160.00 USD | 27,780.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 222,830,000.00 USD | 222,830,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 255,670.00 USD | 769,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,520,000.00 USD | 130,520,000.00 USD | 53,740.00 USD | 0.00 USD | 138,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 223,310,000.00 USD | 223,310,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,750,000.00 USD | 130,750,000.00 USD | 84,710.00 USD | 105,400.00 USD | 44,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 224,730,000.00 USD | 224,730,000.00 USD | 528,490.00 USD | 136,720.00 USD | 753,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,930,000.00 USD | 130,930,000.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 225,910,000.00 USD | 225,910,000.00 USD | 345,700.00 USD | 372,470.00 USD | 461,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 131,060,000.00 USD | 131,060,000.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 228,510,000.00 USD | 228,510,000.00 USD | 920,600.00 USD | 404,120.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 131,210,000.00 USD | 131,210,000.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 230,100,000.00 USD | 230,100,000.00 USD | 536,130.00 USD | 294,500.00 USD | 759,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,460,000.00 USD | 131,460,000.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 231,660,000.00 USD | 231,660,000.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,960,000.00 USD | 131,960,000.00 USD | 231,710.00 USD | 72,370.00 USD | 195,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 233,790,000.00 USD | 233,790,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 132,400,000.00 USD | 132,400,000.00 USD | 162,970.00 USD | 90,840.00 USD | 182,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 236,340,000.00 USD | 236,340,000.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 132,640,000.00 USD | 132,640,000.00 USD | 79,200.00 USD | 80,770.00 USD | 76,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 237,420,000.00 USD | 237,420,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 132,980,000.00 USD | 132,980,000.00 USD | 131,770.00 USD | 0.00 USD | 214,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 238,710,000.00 USD | 238,710,000.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 770,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 133,010,000.00 USD | 133,010,000.00 USD | 7,260.00 USD | 15,600.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 239,250,000.00 USD | 239,250,000.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 133,150,000.00 USD | 133,150,000.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 240,350,000.00 USD | 240,350,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 240,520,000.00 USD | 240,520,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 133,150,000.00 USD | 133,150,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 240,850,000.00 USD | 240,850,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 133,220,000.00 USD | 133,220,000.00 USD | 31,140.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 241,010,000.00 USD | 241,010,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,640.00 USD | 782,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 133,290,000.00 USD | 133,290,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 241,130,000.00 USD | 241,130,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 133,420,000.00 USD | 133,420,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 241,140,000.00 USD | 241,140,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 241,280,000.00 USD | 241,280,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 241,400,000.00 USD | 241,400,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 133,430,000.00 USD | 133,430,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 241,640,000.00 USD | 241,640,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 5,310.00 USD | 787,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 241,800,000.00 USD | 241,800,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 133,500,000.00 USD | 133,500,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 242,180,000.00 USD | 242,180,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 133,880,000.00 USD | 133,880,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 242,830,000.00 USD | 242,830,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 134,000,000.00 USD | 134,000,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 243,010,000.00 USD | 243,010,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 134,010,000.00 USD | 134,010,000.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 243,630,000.00 USD | 243,630,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,400.00 USD | 790,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 134,180,000.00 USD | 134,180,000.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 244,160,000.00 USD | 244,160,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 134,560,000.00 USD | 134,560,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 245,180,000.00 USD | 245,180,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 135,300,000.00 USD | 135,300,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 246,550,000.00 USD | 246,550,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 135,720,000.00 USD | 135,720,000.00 USD | 149,490.00 USD | 92,570.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 247,180,000.00 USD | 247,180,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 247,540,000.00 USD | 247,540,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,140.00 USD | 883,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 248,560,000.00 USD | 248,560,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 250,070,000.00 USD | 250,070,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 251,450,000.00 USD | 251,450,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 252,250,000.00 USD | 252,250,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 252,780,000.00 USD | 252,780,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 258.30 USD | 884,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 253,130,000.00 USD | 253,130,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 253,590,000.00 USD | 253,590,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 254,310,000.00 USD | 254,310,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 254,680,000.00 USD | 254,680,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 254,810,000.00 USD | 254,810,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 254,930,000.00 USD | 254,930,000.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 255,270,000.00 USD | 255,270,000.00 USD | 66,640.00 USD | 96,050.00 USD | 173,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 255,880,000.00 USD | 255,880,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 256,440,000.00 USD | 256,440,000.00 USD | 182,110.00 USD | 128,180.00 USD | 251,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 256,900,000.00 USD | 256,900,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 1,590.00 USD | 885,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.46` | 257,060,000.00 USD | 257,060,000.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 257,530,000.00 USD | 257,530,000.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 257,740,000.00 USD | 257,740,000.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.47` | 28,460.00 USD | 914,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 11,470.00 USD | 925,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 128,990.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 468,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 1,600.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 776.71 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 2,130.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 6,800.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,420.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 123.63 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 599.17 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 271.38 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 133,590.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 177.55 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 2,130.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 4,530,000.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,280.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 1,680.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 5,310,000.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 3,970.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 20,140.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 260.98 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 128.45 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 534.24 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,980,000.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 870.87 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 308,670.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 13,110.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 794.73 USD | 15,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 3,120,000.00 USD | 18,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 9,960.00 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,680.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 2,920.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 404,290.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 122.10 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 18,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 5,710,000.00 USD | 24,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 6,230.00 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 2,050.00 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 251,210.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.13` | 747.25 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 259.55 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,630.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.51 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 627.77 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.43 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 47,420.00 USD | 24,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 75,930.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 205.62 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 4,980.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 214.22 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 155,670.00 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 104.65 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 105.57 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 2,760.00 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 11,900.00 USD | 25,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 1,550.00 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 114.90 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 146.01 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 108.79 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 109.71 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 57,050.00 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 591.63 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 3,710.00 USD | 25,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 282,730.00 USD | 25,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 171.85 USD | 25,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 70,900,000.00 USD | 0.00 USD | 354.96 USD | `-79.39%` | `1,392.00` |
| `Live` | `Long` | `0.2650` | 70,900,000.00 USD | 0.00 USD | 25,040.00 USD | `-78.58%` | `94,507.00` |
| `Live` | `Long` | `0.2750` | 70,880,000.00 USD | 0.00 USD | 2,740.00 USD | `-77.77%` | `9,956.00` |
| `Live` | `Long` | `0.2850` | 70,880,000.00 USD | 0.00 USD | 6,670.00 USD | `-76.97%` | `23,409.00` |
| `Live` | `Long` | `0.2950` | 70,870,000.00 USD | 0.00 USD | 14,270.00 USD | `-76.16%` | `48,379.00` |
| `Live` | `Long` | `0.3050` | 70,850,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.35%` | `4,526.00` |
| `Live` | `Long` | `0.3150` | 70,850,000.00 USD | 0.00 USD | 4,910.00 USD | `-74.54%` | `15,577.00` |
| `Live` | `Long` | `0.3250` | 70,850,000.00 USD | 0.00 USD | 114,130.00 USD | `-73.73%` | `351,158.00` |
| `Live` | `Long` | `0.3350` | 70,730,000.00 USD | 0.00 USD | 708.53 USD | `-72.92%` | `2,115.00` |
| `Live` | `Long` | `0.3450` | 70,730,000.00 USD | 0.00 USD | 12,510.00 USD | `-72.12%` | `36,260.00` |
| `Live` | `Long` | `0.3550` | 70,720,000.00 USD | 0.00 USD | 30,620.00 USD | `-71.31%` | `86,246.00` |
| `Live` | `Long` | `0.3650` | 70,690,000.00 USD | 0.00 USD | 17,450.00 USD | `-70.50%` | `47,796.00` |
| `Live` | `Long` | `0.3750` | 70,670,000.00 USD | 0.00 USD | 421.88 USD | `-69.69%` | `1,125.00` |
| `Live` | `Long` | `0.3850` | 70,670,000.00 USD | 0.00 USD | 346.88 USD | `-68.88%` | `901.00` |
| `Live` | `Long` | `0.3950` | 70,670,000.00 USD | 0.00 USD | 174.59 USD | `-68.08%` | `442.00` |
| `Live` | `Long` | `0.4050` | 70,670,000.00 USD | 0.00 USD | 530,350.00 USD | `-67.27%` | `1,309,498.00` |
| `Live` | `Long` | `0.4350` | 70,140,000.00 USD | 0.00 USD | 7,840.00 USD | `-64.84%` | `18,023.00` |
| `Live` | `Long` | `0.4450` | 70,130,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-64.03%` | `4,965,142.00` |
| `Live` | `Long` | `0.4550` | 67,920,000.00 USD | 0.00 USD | 1,600.00 USD | `-63.23%` | `3,523.00` |
| `Live` | `Long` | `0.4650` | 67,920,000.00 USD | 0.00 USD | 551.96 USD | `-62.42%` | `1,187.00` |
| `Live` | `Long` | `0.4850` | 67,920,000.00 USD | 0.00 USD | 1,930.00 USD | `-60.80%` | `3,971.00` |
| `Live` | `Long` | `0.4950` | 67,920,000.00 USD | 0.00 USD | 63,660.00 USD | `-59.99%` | `128,596.00` |
| `Live` | `Long` | `0.5050` | 67,860,000.00 USD | 0.00 USD | 6,260.00 USD | `-59.19%` | `12,395.00` |
| `Live` | `Long` | `0.5150` | 67,850,000.00 USD | 0.00 USD | 2,890.00 USD | `-58.38%` | `5,606.00` |
| `Live` | `Long` | `0.5250` | 67,850,000.00 USD | 0.00 USD | 1,780.00 USD | `-57.57%` | `3,400.00` |
| `Live` | `Long` | `0.5350` | 67,850,000.00 USD | 0.00 USD | 588.50 USD | `-56.76%` | `1,100.00` |
| `Live` | `Long` | `0.5450` | 67,850,000.00 USD | 0.00 USD | 7,290.00 USD | `-55.95%` | `13,376.00` |
| `Live` | `Long` | `0.5550` | 67,840,000.00 USD | 0.00 USD | 633.26 USD | `-55.14%` | `1,141.00` |
| `Live` | `Long` | `0.5650` | 67,840,000.00 USD | 0.00 USD | 3,540.00 USD | `-54.34%` | `6,270.00` |
| `Live` | `Long` | `0.5750` | 67,830,000.00 USD | 0.00 USD | 8,870.00 USD | `-53.53%` | `15,431.00` |
| `Live` | `Long` | `0.5850` | 67,820,000.00 USD | 0.00 USD | 168,060.00 USD | `-52.72%` | `287,275.00` |
| `Live` | `Long` | `0.5950` | 67,660,000.00 USD | 0.00 USD | 2,980.00 USD | `-51.91%` | `5,015.00` |
| `Live` | `Long` | `0.6050` | 67,650,000.00 USD | 0.00 USD | 29,530.00 USD | `-51.10%` | `48,804.00` |
| `Live` | `Long` | `0.6150` | 67,620,000.00 USD | 0.00 USD | 32,370.00 USD | `-50.29%` | `52,627.00` |
| `Live` | `Long` | `0.6250` | 67,590,000.00 USD | 0.00 USD | 1,130.00 USD | `-49.49%` | `1,803.00` |
| `Live` | `Long` | `0.6350` | 67,590,000.00 USD | 0.00 USD | 22,110.00 USD | `-48.68%` | `34,821.00` |
| `Live` | `Long` | `0.6450` | 67,570,000.00 USD | 0.00 USD | 1,560.00 USD | `-47.87%` | `2,412.00` |
| `Live` | `Long` | `0.6550` | 67,570,000.00 USD | 0.00 USD | 1,030.00 USD | `-47.06%` | `1,579.00` |
| `Live` | `Long` | `0.6650` | 67,570,000.00 USD | 0.00 USD | 15,700.00 USD | `-46.25%` | `23,602.00` |
| `Live` | `Long` | `0.6750` | 67,550,000.00 USD | 0.00 USD | 30,110.00 USD | `-45.45%` | `44,612.00` |
| `Live` | `Long` | `0.6850` | 67,520,000.00 USD | 0.00 USD | 21,150.00 USD | `-44.64%` | `30,869.00` |
| `Live` | `Long` | `0.6950` | 67,500,000.00 USD | 0.00 USD | 7,810.00 USD | `-43.83%` | `11,236.00` |
| `Live` | `Long` | `0.7050` | 67,490,000.00 USD | 0.00 USD | 28,070.00 USD | `-43.02%` | `39,817.00` |
| `Live` | `Long` | `0.7150` | 67,460,000.00 USD | 0.00 USD | 67,440.00 USD | `-42.21%` | `94,326.00` |
| `Live` | `Long` | `0.7250` | 67,400,000.00 USD | 0.00 USD | 244,720.00 USD | `-41.40%` | `337,538.00` |
| `Live` | `Long` | `0.7350` | 67,150,000.00 USD | 0.00 USD | 21,910.00 USD | `-40.60%` | `29,816.00` |
| `Live` | `Long` | `0.7450` | 67,130,000.00 USD | 0.00 USD | 62,010.00 USD | `-39.79%` | `83,239.00` |
| `Live` | `Long` | `0.7550` | 67,070,000.00 USD | 0.00 USD | 107,370.00 USD | `-38.98%` | `142,217.00` |
| `Live` | `Long` | `0.7650` | 66,960,000.00 USD | 0.00 USD | 218,080.00 USD | `-38.17%` | `285,075.00` |
| `Live` | `Long` | `0.7750` | 66,740,000.00 USD | 0.00 USD | 5,760.00 USD | `-37.36%` | `7,427.00` |
| `Live` | `Long` | `0.7850` | 66,740,000.00 USD | 0.00 USD | 27,790.00 USD | `-36.56%` | `35,403.00` |
| `Live` | `Long` | `0.7950` | 66,710,000.00 USD | 0.00 USD | 12,080.00 USD | `-35.75%` | `15,195.00` |
| `Live` | `Long` | `0.8050` | 66,700,000.00 USD | 0.00 USD | 23,890.00 USD | `-34.94%` | `29,676.00` |
| `Live` | `Long` | `0.8150` | 66,670,000.00 USD | 0.00 USD | 14,900.00 USD | `-34.13%` | `18,284.00` |
| `Live` | `Long` | `0.8250` | 66,660,000.00 USD | 0.00 USD | 55,220.00 USD | `-33.32%` | `66,938.00` |
| `Live` | `Long` | `0.8350` | 66,600,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-32.51%` | `3,597,985.00` |
| `Live` | `Long` | `0.8450` | 63,600,000.00 USD | 0.00 USD | 283,660.00 USD | `-31.71%` | `335,694.00` |
| `Live` | `Long` | `0.8550` | 63,310,000.00 USD | 0.00 USD | 72,590.00 USD | `-30.90%` | `84,898.00` |
| `Live` | `Long` | `0.8650` | 63,240,000.00 USD | 0.00 USD | 6,060.00 USD | `-30.09%` | `7,005.00` |
| `Live` | `Long` | `0.8750` | 63,240,000.00 USD | 0.00 USD | 85,730.00 USD | `-29.28%` | `97,974.00` |
| `Live` | `Long` | `0.8850` | 63,150,000.00 USD | 0.00 USD | 371,120.00 USD | `-28.47%` | `419,341.00` |
| `Live` | `Long` | `0.8950` | 62,780,000.00 USD | 0.00 USD | 102,690.00 USD | `-27.67%` | `114,739.00` |
| `Live` | `Long` | `0.9050` | 62,680,000.00 USD | 0.00 USD | 148,850.00 USD | `-26.86%` | `164,474.00` |
| `Live` | `Long` | `0.9150` | 62,530,000.00 USD | 0.00 USD | 50,060.00 USD | `-26.05%` | `54,713.00` |
| `Live` | `Long` | `0.9250` | 62,480,000.00 USD | 0.00 USD | 147,510.00 USD | `-25.24%` | `159,475.00` |
| `Live` | `Long` | `0.9350` | 62,330,000.00 USD | 0.00 USD | 87,100.00 USD | `-24.43%` | `93,153.00` |
| `Live` | `Long` | `0.9450` | 62,240,000.00 USD | 0.00 USD | 97,300.00 USD | `-23.62%` | `102,963.00` |
| `Live` | `Long` | `0.9550` | 62,150,000.00 USD | 0.00 USD | 116,510.00 USD | `-22.82%` | `121,996.00` |
| `Live` | `Long` | `0.9650` | 62,030,000.00 USD | 0.00 USD | 33,920,000.00 USD | `-22.01%` | `35,150,501.00` |
| `Live` | `Long` | `0.9750` | 28,110,000.00 USD | 0.00 USD | 158,540.00 USD | `-21.20%` | `162,607.00` |
| `Live` | `Long` | `0.9850` | 27,950,000.00 USD | 0.00 USD | 450,730.00 USD | `-20.39%` | `457,598.00` |
| `Live` | `Long` | `0.9950` | 27,500,000.00 USD | 0.00 USD | 98,040.00 USD | `-19.58%` | `98,536.00` |
| `Live` | `Long` | `1.00` | 27,400,000.00 USD | 0.00 USD | 451,390.00 USD | `-18.77%` | `449,144.00` |
| `Live` | `Long` | `1.01` | 26,950,000.00 USD | 0.00 USD | 181,040.00 USD | `-17.97%` | `178,361.00` |
| `Live` | `Long` | `1.02` | 26,770,000.00 USD | 0.00 USD | 3,440,000.00 USD | `-17.16%` | `3,352,579.00` |
| `Live` | `Long` | `1.03` | 23,330,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-16.35%` | `2,044,058.00` |
| `Live` | `Long` | `1.04` | 21,220,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-15.54%` | `1,228,581.00` |
| `Live` | `Long` | `1.05` | 19,930,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-14.73%` | `1,069,141.00` |
| `Live` | `Long` | `1.06` | 18,800,000.00 USD | 0.00 USD | 532,180.00 USD | `-13.93%` | `499,701.00` |
| `Live` | `Long` | `1.07` | 18,270,000.00 USD | 0.00 USD | 440,750.00 USD | `-13.12%` | `409,998.00` |
| `Live` | `Long` | `1.08` | 17,830,000.00 USD | 0.00 USD | 758,070.00 USD | `-12.31%` | `698,686.00` |
| `Live` | `Long` | `1.09` | 17,070,000.00 USD | 0.00 USD | 603,690.00 USD | `-11.50%` | `551,316.00` |
| `Live` | `Long` | `1.10` | 16,470,000.00 USD | 0.00 USD | 65,590.00 USD | `-10.69%` | `59,353.00` |
| `Live` | `Long` | `1.11` | 16,400,000.00 USD | 0.00 USD | 249,040.00 USD | `-9.88%` | `223,353.00` |
| `Live` | `Long` | `1.12` | 16,160,000.00 USD | 0.00 USD | 267,340.00 USD | `-9.08%` | `237,638.00` |
| `Live` | `Long` | `1.14` | 15,890,000.00 USD | 0.00 USD | 215,570.00 USD | `-8.27%` | `189,933.00` |
| `Live` | `Long` | `1.15` | 15,670,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-7.46%` | `1,491,595.00` |
| `Live` | `Long` | `1.16` | 13,960,000.00 USD | 0.00 USD | 482,060.00 USD | `-6.65%` | `417,368.00` |
| `Live` | `Long` | `1.17` | 13,480,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-5.84%` | `1,294,842.00` |
| `Live` | `Long` | `1.18` | 11,970,000.00 USD | 0.00 USD | 481,590.00 USD | `-5.04%` | `409,867.00` |
| `Live` | `Long` | `1.19` | 11,490,000.00 USD | 0.00 USD | 741,690.00 USD | `-4.23%` | `625,902.00` |
| `Live` | `Long` | `1.20` | 10,750,000.00 USD | 0.00 USD | 379,860.00 USD | `-3.42%` | `317,875.00` |
| `Live` | `Long` | `1.21` | 10,370,000.00 USD | 0.00 USD | 9,230,000.00 USD | `-2.61%` | `7,663,579.00` |
| `Live` | `Long` | `1.22` | 1,140,000.00 USD | 0.00 USD | 710,620.00 USD | `-1.80%` | `584,872.00` |
| `Live` | `Long` | `1.23` | 425,740.00 USD | 0.00 USD | 421,580.00 USD | `-0.99%` | `344,143.00` |
| `Live` | `Long` | `1.24` | 4,170.00 USD | 0.00 USD | 4,170.00 USD | `-0.19%` | `3,373.00` |
| `Live` | `Short` | `1.25` | 8,790.00 USD | 8,790.00 USD | 0.00 USD | `+0.62%` | `7,061.00` |
| `Live` | `Short` | `1.25` | 48,360.00 USD | 39,570.00 USD | 0.00 USD | `+1.43%` | `31,530.00` |
| `Live` | `Short` | `1.26` | 93,480.00 USD | 45,120.00 USD | 0.00 USD | `+2.24%` | `35,671.00` |
| `Live` | `Short` | `1.27` | 327,630.00 USD | 234,140.00 USD | 0.00 USD | `+3.05%` | `183,641.00` |
| `Live` | `Short` | `1.28` | 430,620.00 USD | 102,990.00 USD | 0.00 USD | `+3.86%` | `80,151.00` |
| `Live` | `Short` | `1.29` | 432,180.00 USD | 1,550.00 USD | 0.00 USD | `+4.66%` | `1,200.00` |
| `Live` | `Short` | `1.30` | 436,480.00 USD | 4,310.00 USD | 0.00 USD | `+5.47%` | `3,300.00` |
| `Live` | `Short` | `1.31` | 438,180.00 USD | 1,700.00 USD | 0.00 USD | `+6.28%` | `1,292.00` |
| `Live` | `Short` | `1.32` | 484,710.00 USD | 46,520.00 USD | 0.00 USD | `+7.09%` | `35,113.00` |
| `Live` | `Short` | `1.33` | 488,160.00 USD | 3,460.00 USD | 0.00 USD | `+7.90%` | `2,589.00` |
| `Live` | `Short` | `1.34` | 490,090.00 USD | 1,920.00 USD | 0.00 USD | `+8.70%` | `1,431.00` |
| `Live` | `Short` | `1.35` | 513,500.00 USD | 23,410.00 USD | 0.00 USD | `+9.51%` | `17,276.00` |
| `Live` | `Short` | `1.36` | 769,170.00 USD | 255,670.00 USD | 0.00 USD | `+10.32%` | `187,304.00` |
| `Live` | `Short` | `1.39` | 770,440.00 USD | 1,280.00 USD | 0.00 USD | `+11.94%` | `921.00` |
| `Live` | `Short` | `1.40` | 782,080.00 USD | 11,640.00 USD | 0.00 USD | `+12.75%` | `8,341.00` |
| `Live` | `Short` | `1.41` | 787,390.00 USD | 5,310.00 USD | 0.00 USD | `+13.55%` | `3,782.00` |
| `Live` | `Short` | `1.42` | 790,790.00 USD | 3,400.00 USD | 0.00 USD | `+14.36%` | `2,403.00` |
| `Live` | `Short` | `1.43` | 883,930.00 USD | 93,140.00 USD | 0.00 USD | `+15.17%` | `65,362.00` |
| `Live` | `Short` | `1.44` | 884,190.00 USD | 258.30 USD | 0.00 USD | `+15.98%` | `180.00` |
| `Live` | `Short` | `1.46` | 885,780.00 USD | 1,590.00 USD | 0.00 USD | `+17.59%` | `1,090.00` |
| `Live` | `Short` | `1.47` | 914,240.00 USD | 28,460.00 USD | 0.00 USD | `+18.40%` | `19,428.00` |
| `Live` | `Short` | `1.48` | 925,710.00 USD | 11,470.00 USD | 0.00 USD | `+19.21%` | `7,778.00` |
| `Live` | `Short` | `1.49` | 1,050,000.00 USD | 128,990.00 USD | 0.00 USD | `+20.02%` | `86,861.00` |
| `Live` | `Short` | `1.50` | 1,070,000.00 USD | 11,950.00 USD | 0.00 USD | `+20.83%` | `7,994.00` |
| `Live` | `Short` | `1.51` | 1,530,000.00 USD | 468,000.00 USD | 0.00 USD | `+22.44%` | `308,913.00` |
| `Live` | `Short` | `1.52` | 1,540,000.00 USD | 1,600.00 USD | 0.00 USD | `+23.25%` | `1,052.00` |
| `Live` | `Short` | `1.53` | 1,540,000.00 USD | 776.71 USD | 0.00 USD | `+24.06%` | `506.00` |
| `Live` | `Short` | `1.54` | 1,540,000.00 USD | 2,130.00 USD | 0.00 USD | `+24.87%` | `1,377.00` |
| `Live` | `Short` | `1.55` | 1,550,000.00 USD | 6,800.00 USD | 0.00 USD | `+25.68%` | `4,373.00` |
| `Live` | `Short` | `1.56` | 1,550,000.00 USD | 555.57 USD | 0.00 USD | `+26.49%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,550,000.00 USD | 2,420.00 USD | 0.00 USD | `+27.29%` | `1,539.00` |
| `Live` | `Short` | `1.58` | 1,550,000.00 USD | 123.63 USD | 0.00 USD | `+28.10%` | `78.00` |
| `Live` | `Short` | `1.61` | 1,550,000.00 USD | 599.17 USD | 0.00 USD | `+30.53%` | `371.00` |
| `Live` | `Short` | `1.62` | 1,550,000.00 USD | 271.38 USD | 0.00 USD | `+31.33%` | `167.00` |
| `Live` | `Short` | `1.64` | 1,560,000.00 USD | 11,270.00 USD | 0.00 USD | `+32.14%` | `6,892.00` |
| `Live` | `Short` | `1.65` | 1,690,000.00 USD | 133,590.00 USD | 0.00 USD | `+32.95%` | `81,210.00` |
| `Live` | `Short` | `1.66` | 1,690,000.00 USD | 147.30 USD | 0.00 USD | `+33.76%` | `89.00` |
| `Live` | `Short` | `1.67` | 1,700,000.00 USD | 586.08 USD | 0.00 USD | `+34.57%` | `352.00` |
| `Live` | `Short` | `1.68` | 1,700,000.00 USD | 177.55 USD | 0.00 USD | `+35.38%` | `106.00` |
| `Live` | `Short` | `1.69` | 1,700,000.00 USD | 4,180.00 USD | 0.00 USD | `+36.18%` | `2,483.00` |
| `Live` | `Short` | `1.70` | 1,700,000.00 USD | 2,130.00 USD | 0.00 USD | `+36.99%` | `1,256.00` |
| `Live` | `Short` | `1.71` | 1,700,000.00 USD | 1,980.00 USD | 0.00 USD | `+37.80%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 6,230,000.00 USD | 4,530,000.00 USD | 0.00 USD | `+39.42%` | `2,626,058.00` |
| `Live` | `Short` | `1.74` | 6,240,000.00 USD | 2,970.00 USD | 0.00 USD | `+40.22%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 6,240,000.00 USD | 2,730.00 USD | 0.00 USD | `+41.03%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 6,240,000.00 USD | 1,280.00 USD | 0.00 USD | `+41.84%` | `727.00` |
| `Live` | `Short` | `1.76` | 6,240,000.00 USD | 1,680.00 USD | 0.00 USD | `+42.65%` | `952.00` |
| `Live` | `Short` | `1.77` | 11,550,000.00 USD | 5,310,000.00 USD | 0.00 USD | `+43.46%` | `2,990,580.00` |
| `Live` | `Short` | `1.78` | 11,680,000.00 USD | 129,540.00 USD | 0.00 USD | `+44.27%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 11,680,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.07%` | `2,211.00` |
| `Live` | `Short` | `1.80` | 11,690,000.00 USD | 889.87 USD | 0.00 USD | `+45.88%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,710,000.00 USD | 20,140.00 USD | 0.00 USD | `+46.69%` | `11,096.00` |
| `Live` | `Short` | `1.82` | 11,710,000.00 USD | 260.98 USD | 0.00 USD | `+47.50%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,710,000.00 USD | 128.45 USD | 0.00 USD | `+48.31%` | `70.00` |
| `Live` | `Short` | `1.84` | 11,720,000.00 USD | 9,340.00 USD | 0.00 USD | `+49.12%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,720,000.00 USD | 534.24 USD | 0.00 USD | `+49.92%` | `288.00` |
| `Live` | `Short` | `1.86` | 14,690,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+50.73%` | `1,595,959.00` |
| `Live` | `Short` | `1.89` | 14,690,000.00 USD | 870.87 USD | 0.00 USD | `+52.35%` | `462.00` |
| `Live` | `Short` | `1.90` | 15,000,000.00 USD | 308,670.00 USD | 0.00 USD | `+53.16%` | `162,888.00` |
| `Live` | `Short` | `1.91` | 15,010,000.00 USD | 13,110.00 USD | 0.00 USD | `+53.96%` | `6,882.00` |
| `Live` | `Short` | `1.92` | 15,020,000.00 USD | 794.73 USD | 0.00 USD | `+54.77%` | `415.00` |
| `Live` | `Short` | `1.93` | 18,140,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+55.58%` | `1,622,843.00` |
| `Live` | `Short` | `1.94` | 18,150,000.00 USD | 9,960.00 USD | 0.00 USD | `+56.39%` | `5,145.00` |
| `Live` | `Short` | `1.96` | 18,150,000.00 USD | 293.25 USD | 0.00 USD | `+58.01%` | `150.00` |
| `Live` | `Short` | `1.97` | 18,380,000.00 USD | 227,680.00 USD | 0.00 USD | `+58.81%` | `115,869.00` |
| `Live` | `Short` | `1.98` | 18,380,000.00 USD | 2,920.00 USD | 0.00 USD | `+59.62%` | `1,478.00` |
| `Live` | `Short` | `2.02` | 18,780,000.00 USD | 404,290.00 USD | 0.00 USD | `+62.85%` | `200,642.00` |
| `Live` | `Short` | `2.04` | 18,780,000.00 USD | 122.10 USD | 0.00 USD | `+64.47%` | `60.00` |
| `Live` | `Short` | `2.04` | 18,790,000.00 USD | 198.36 USD | 0.00 USD | `+65.28%` | `97.00` |
| `Live` | `Short` | `2.06` | 24,500,000.00 USD | 5,710,000.00 USD | 0.00 USD | `+66.09%` | `2,780,943.00` |
| `Live` | `Short` | `2.06` | 24,510,000.00 USD | 6,230.00 USD | 0.00 USD | `+66.90%` | `3,017.00` |
| `Live` | `Short` | `2.08` | 24,510,000.00 USD | 2,050.00 USD | 0.00 USD | `+67.70%` | `989.00` |
| `Live` | `Short` | `2.10` | 24,510,000.00 USD | 331.01 USD | 0.00 USD | `+69.32%` | `158.00` |
| `Live` | `Short` | `2.10` | 24,510,000.00 USD | 294.70 USD | 0.00 USD | `+70.13%` | `140.00` |
| `Live` | `Short` | `2.12` | 24,760,000.00 USD | 251,210.00 USD | 0.00 USD | `+70.94%` | `118,776.00` |
| `Live` | `Short` | `2.13` | 24,760,000.00 USD | 747.25 USD | 0.00 USD | `+72.55%` | `350.00` |
| `Live` | `Short` | `2.15` | 24,760,000.00 USD | 259.55 USD | 0.00 USD | `+73.36%` | `121.00` |
| `Live` | `Short` | `2.15` | 24,760,000.00 USD | 196.11 USD | 0.00 USD | `+74.17%` | `91.00` |
| `Live` | `Short` | `2.17` | 24,760,000.00 USD | 2,630.00 USD | 0.00 USD | `+75.79%` | `1,207.00` |
| `Live` | `Short` | `2.19` | 24,760,000.00 USD | 100.51 USD | 0.00 USD | `+76.59%` | `46.00` |
| `Live` | `Short` | `2.19` | 24,760,000.00 USD | 627.77 USD | 0.00 USD | `+77.40%` | `286.00` |
| `Live` | `Short` | `2.21` | 24,760,000.00 USD | 101.43 USD | 0.00 USD | `+78.21%` | `46.00` |
| `Live` | `Short` | `2.21` | 24,810,000.00 USD | 47,420.00 USD | 0.00 USD | `+79.02%` | `21,408.00` |
| `Live` | `Short` | `2.23` | 24,890,000.00 USD | 75,930.00 USD | 0.00 USD | `+79.83%` | `34,127.00` |
| `Live` | `Short` | `2.23` | 24,890,000.00 USD | 205.62 USD | 0.00 USD | `+80.64%` | `92.00` |
| `Live` | `Short` | `2.25` | 24,890,000.00 USD | 4,980.00 USD | 0.00 USD | `+81.44%` | `2,218.00` |
| `Live` | `Short` | `2.25` | 24,890,000.00 USD | 214.22 USD | 0.00 USD | `+82.25%` | `95.00` |
| `Live` | `Short` | `2.27` | 25,050,000.00 USD | 155,670.00 USD | 0.00 USD | `+83.06%` | `68,730.00` |
| `Live` | `Short` | `2.27` | 25,050,000.00 USD | 104.65 USD | 0.00 USD | `+83.87%` | `46.00` |
| `Live` | `Short` | `2.29` | 25,050,000.00 USD | 105.57 USD | 0.00 USD | `+85.48%` | `46.00` |
| `Live` | `Short` | `2.31` | 25,050,000.00 USD | 2,760.00 USD | 0.00 USD | `+87.10%` | `1,193.00` |
| `Live` | `Short` | `2.33` | 25,060,000.00 USD | 11,900.00 USD | 0.00 USD | `+87.91%` | `5,119.00` |
| `Live` | `Short` | `2.33` | 25,070,000.00 USD | 1,550.00 USD | 0.00 USD | `+88.72%` | `665.00` |
| `Live` | `Short` | `2.35` | 25,070,000.00 USD | 114.90 USD | 0.00 USD | `+89.53%` | `49.00` |
| `Live` | `Short` | `2.35` | 25,070,000.00 USD | 146.01 USD | 0.00 USD | `+90.33%` | `62.00` |
| `Live` | `Short` | `2.37` | 25,070,000.00 USD | 108.79 USD | 0.00 USD | `+91.14%` | `46.00` |
| `Live` | `Short` | `2.38` | 25,070,000.00 USD | 109.71 USD | 0.00 USD | `+92.76%` | `46.00` |
| `Live` | `Short` | `2.40` | 25,120,000.00 USD | 57,050.00 USD | 0.00 USD | `+93.57%` | `23,820.00` |
| `Live` | `Short` | `2.40` | 25,120,000.00 USD | 591.63 USD | 0.00 USD | `+94.37%` | `246.00` |
| `Live` | `Short` | `2.42` | 25,130,000.00 USD | 3,710.00 USD | 0.00 USD | `+95.99%` | `1,528.00` |
| `Live` | `Short` | `2.44` | 25,410,000.00 USD | 282,730.00 USD | 0.00 USD | `+96.80%` | `116,111.00` |
| `Live` | `Short` | `2.46` | 25,410,000.00 USD | 171.85 USD | 0.00 USD | `+98.42%` | `70.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 7,500,000.00 USD | 0.00 USD | 112.45 USD | `-79.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 7,500,000.00 USD | 0.00 USD | 139.12 USD | `-69.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 7,500,000.00 USD | 0.00 USD | 200.86 USD | `-66.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 7,500,000.00 USD | 0.00 USD | 408.51 USD | `-64.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 7,500,000.00 USD | 0.00 USD | 273.00 USD | `-63.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 7,500,000.00 USD | 0.00 USD | 151.12 USD | `-62.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 7,500,000.00 USD | 0.00 USD | 142.50 USD | `-61.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 7,500,000.00 USD | 0.00 USD | 145.50 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 7,500,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 7,500,000.00 USD | 0.00 USD | 285.82 USD | `-58.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 7,500,000.00 USD | 0.00 USD | 306.60 USD | `-57.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 7,500,000.00 USD | 0.00 USD | 121.55 USD | `-55.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 7,500,000.00 USD | 0.00 USD | 374.60 USD | `-54.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 7,500,000.00 USD | 0.00 USD | 100.62 USD | `-52.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 7,500,000.00 USD | 0.00 USD | 791.85 USD | `-48.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 7,500,000.00 USD | 0.00 USD | 573.40 USD | `-47.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 7,500,000.00 USD | 0.00 USD | 364.18 USD | `-47.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 7,500,000.00 USD | 0.00 USD | 3,010.00 USD | `-46.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 7,500,000.00 USD | 0.00 USD | 503.55 USD | `-45.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 7,500,000.00 USD | 0.00 USD | 480.19 USD | `-44.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 7,490,000.00 USD | 0.00 USD | 11,870.00 USD | `-43.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 7,480,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 7,480,000.00 USD | 0.00 USD | 536.50 USD | `-41.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 7,480,000.00 USD | 0.00 USD | 1,300.00 USD | `-38.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 7,480,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 7,480,000.00 USD | 0.00 USD | 878.48 USD | `-35.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 7,470,000.00 USD | 0.00 USD | 798.57 USD | `-30.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 7,470,000.00 USD | 0.00 USD | 690.38 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 7,470,000.00 USD | 0.00 USD | 1,060.00 USD | `-28.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 7,470,000.00 USD | 0.00 USD | 3,230.00 USD | `-27.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 7,470,000.00 USD | 0.00 USD | 838.94 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 7,470,000.00 USD | 0.00 USD | 188.49 USD | `-26.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 7,470,000.00 USD | 0.00 USD | 2,730.00 USD | `-25.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 7,470,000.00 USD | 0.00 USD | 1,180.00 USD | `-24.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 7,460,000.00 USD | 0.00 USD | 112.46 USD | `-23.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 7,460,000.00 USD | 0.00 USD | 2,360.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 7,460,000.00 USD | 0.00 USD | 3,910.00 USD | `-22.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 7,460,000.00 USD | 0.00 USD | 546,370.00 USD | `-21.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 6,910,000.00 USD | 0.00 USD | 4,360.00 USD | `-20.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 6,910,000.00 USD | 0.00 USD | 805.95 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 6,910,000.00 USD | 0.00 USD | 15,150.00 USD | `-18.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 6,890,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 6,890,000.00 USD | 0.00 USD | 2,020.00 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 6,880,000.00 USD | 0.00 USD | 38,000.00 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 6,850,000.00 USD | 0.00 USD | 3,490.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 6,840,000.00 USD | 0.00 USD | 2,110.00 USD | `-14.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 6,840,000.00 USD | 0.00 USD | 2,800.00 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 6,840,000.00 USD | 0.00 USD | 48,080.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 6,790,000.00 USD | 0.00 USD | 3,760.00 USD | `-12.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 6,790,000.00 USD | 0.00 USD | 5,110.00 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 6,780,000.00 USD | 0.00 USD | 3,650.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 6,780,000.00 USD | 0.00 USD | 9,460.00 USD | `-9.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 6,770,000.00 USD | 0.00 USD | 80,260.00 USD | `-9.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 6,690,000.00 USD | 0.00 USD | 13,830.00 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 6,670,000.00 USD | 0.00 USD | 15,230.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 6,660,000.00 USD | 0.00 USD | 30,270.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 6,630,000.00 USD | 0.00 USD | 18,740.00 USD | `-5.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 6,610,000.00 USD | 0.00 USD | 6,300.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 6,600,000.00 USD | 0.00 USD | 136,710.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 6,470,000.00 USD | 0.00 USD | 12,840.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 6,450,000.00 USD | 0.00 USD | 151,430.00 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 6,300,000.00 USD | 0.00 USD | 131,030.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 6,170,000.00 USD | 0.00 USD | 6,120,000.00 USD | `-0.99%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1.24` | 52,660.00 USD | 0.00 USD | 52,660.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,070.00 USD | 4,070.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 26,840.00 USD | 22,770.00 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 34,310.00 USD | 7,460.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 6,340,000.00 USD | 6,310,000.00 USD | 0.00 USD | `+3.05%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.28` | 6,360,000.00 USD | 21,440.00 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 6,370,000.00 USD | 7,760.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 6,390,000.00 USD | 17,230.00 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 6,780,000.00 USD | 393,840.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 6,990,000.00 USD | 204,110.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 7,020,000.00 USD | 34,350.00 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 7,190,000.00 USD | 167,640.00 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 7,190,000.00 USD | 907.85 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 7,460,000.00 USD | 275,480.00 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 7,550,000.00 USD | 82,810.00 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 7,600,000.00 USD | 49,450.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 7,600,000.00 USD | 6,060.00 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 11,890,000.00 USD | 4,290,000.00 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 11,890,000.00 USD | 1,980.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 11,900,000.00 USD | 10,470.00 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 11,980,000.00 USD | 80,260.00 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 12,190,000.00 USD | 203,890.00 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 12,190,000.00 USD | 7,510.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 12,220,000.00 USD | 23,130.00 USD | 0.00 USD | `+18.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 12,320,000.00 USD | 107,960.00 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 12,380,000.00 USD | 55,680.00 USD | 0.00 USD | `+20.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 12,390,000.00 USD | 13,980.00 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 12,430,000.00 USD | 32,340.00 USD | 0.00 USD | `+21.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 12,440,000.00 USD | 18,000.00 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 12,540,000.00 USD | 93,330.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 12,580,000.00 USD | 45,870.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 12,610,000.00 USD | 22,270.00 USD | 0.00 USD | `+24.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 12,610,000.00 USD | 2,220.00 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 12,610,000.00 USD | 6,450.00 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 12,620,000.00 USD | 5,940.00 USD | 0.00 USD | `+27.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 12,630,000.00 USD | 11,620.00 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 12,780,000.00 USD | 148,780.00 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 12,780,000.00 USD | 1,840.00 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 12,860,000.00 USD | 80,320.00 USD | 0.00 USD | `+30.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 12,860,000.00 USD | 464.75 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 13,050,000.00 USD | 184,300.00 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 13,050,000.00 USD | 2,670.00 USD | 0.00 USD | `+32.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 13,070,000.00 USD | 18,210.00 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 13,070,000.00 USD | 6,080.00 USD | 0.00 USD | `+34.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 13,090,000.00 USD | 18,400.00 USD | 0.00 USD | `+35.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 13,160,000.00 USD | 70,850.00 USD | 0.00 USD | `+36.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 13,170,000.00 USD | 2,770.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 13,410,000.00 USD | 240,380.00 USD | 0.00 USD | `+37.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 13,420,000.00 USD | 14,030.00 USD | 0.00 USD | `+38.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 13,430,000.00 USD | 5,910.00 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 13,470,000.00 USD | 44,100.00 USD | 0.00 USD | `+40.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 13,480,000.00 USD | 4,710.00 USD | 0.00 USD | `+41.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 13,480,000.00 USD | 5,510.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 13,500,000.00 USD | 21,720.00 USD | 0.00 USD | `+42.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 13,630,000.00 USD | 124,420.00 USD | 0.00 USD | `+43.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 13,720,000.00 USD | 96,600.00 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 13,760,000.00 USD | 36,490.00 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 13,760,000.00 USD | 254.51 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 13,760,000.00 USD | 2,530.00 USD | 0.00 USD | `+46.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 13,770,000.00 USD | 1,830.00 USD | 0.00 USD | `+47.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 13,770,000.00 USD | 7,630.00 USD | 0.00 USD | `+48.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 13,770,000.00 USD | 1,010.00 USD | 0.00 USD | `+49.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 13,780,000.00 USD | 8,390.00 USD | 0.00 USD | `+49.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 13,790,000.00 USD | 4,250.00 USD | 0.00 USD | `+51.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 13,790,000.00 USD | 591.89 USD | 0.00 USD | `+52.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 13,830,000.00 USD | 38,610.00 USD | 0.00 USD | `+53.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 13,860,000.00 USD | 38,940.00 USD | 0.00 USD | `+53.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 13,870,000.00 USD | 7,410.00 USD | 0.00 USD | `+54.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 13,870,000.00 USD | 265.10 USD | 0.00 USD | `+56.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 13,870,000.00 USD | 2,040.00 USD | 0.00 USD | `+57.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 13,880,000.00 USD | 1,660.00 USD | 0.00 USD | `+58.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 13,890,000.00 USD | 14,120.00 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 13,890,000.00 USD | 4,010.00 USD | 0.00 USD | `+59.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 13,890,000.00 USD | 325.54 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 13,900,000.00 USD | 7,020.00 USD | 0.00 USD | `+61.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 14,020,000.00 USD | 122,910.00 USD | 0.00 USD | `+62.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 14,030,000.00 USD | 781.82 USD | 0.00 USD | `+62.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 14,030,000.00 USD | 222.75 USD | 0.00 USD | `+63.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 14,030,000.00 USD | 862.84 USD | 0.00 USD | `+64.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 14,030,000.00 USD | 382.41 USD | 0.00 USD | `+65.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 14,030,000.00 USD | 3,420.00 USD | 0.00 USD | `+66.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 14,030,000.00 USD | 661.93 USD | 0.00 USD | `+67.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 14,160,000.00 USD | 124,400.00 USD | 0.00 USD | `+69.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 14,160,000.00 USD | 1,580.00 USD | 0.00 USD | `+70.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 14,170,000.00 USD | 13,900.00 USD | 0.00 USD | `+71.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 14,200,000.00 USD | 24,840.00 USD | 0.00 USD | `+73.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 14,250,000.00 USD | 50,580.00 USD | 0.00 USD | `+74.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 14,250,000.00 USD | 2,690.00 USD | 0.00 USD | `+74.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 14,270,000.00 USD | 20,370.00 USD | 0.00 USD | `+77.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 14,420,000.00 USD | 151,380.00 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 14,430,000.00 USD | 7,340.00 USD | 0.00 USD | `+80.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 14,430,000.00 USD | 3,120.00 USD | 0.00 USD | `+83.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 14,430,000.00 USD | 1,140.00 USD | 0.00 USD | `+84.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 14,460,000.00 USD | 25,760.00 USD | 0.00 USD | `+85.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 14,460,000.00 USD | 370.40 USD | 0.00 USD | `+87.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 14,460,000.00 USD | 733.19 USD | 0.00 USD | `+88.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 14,460,000.00 USD | 2,410.00 USD | 0.00 USD | `+91.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 14,460,000.00 USD | 475.00 USD | 0.00 USD | `+91.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 14,460,000.00 USD | 2,540.00 USD | 0.00 USD | `+93.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 14,470,000.00 USD | 721.50 USD | 0.00 USD | `+94.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 14,470,000.00 USD | 2,240.00 USD | 0.00 USD | `+95.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 14,490,000.00 USD | 19,590.00 USD | 0.00 USD | `+95.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 14,490,000.00 USD | 564.92 USD | 0.00 USD | `+96.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 14,500,000.00 USD | 8,110.00 USD | 0.00 USD | `+98.42%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.11` | 68,720,000.00 USD | 0.00 USD | 68,720,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.11` | 36,290,000.00 USD | 0.00 USD | 36,290,000.00 USD | 17,310.00 USD | 0.00 USD | 116,380.00 USD |
| `1D` | `1.11` | 36,150,000.00 USD | 0.00 USD | 36,150,000.00 USD | 18,710.00 USD | 937.65 USD | 3,250.00 USD |
| `7D` | `1.11` | 68,700,000.00 USD | 0.00 USD | 68,700,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 36,130,000.00 USD | 0.00 USD | 36,130,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD |
| `7D` | `1.12` | 68,690,000.00 USD | 0.00 USD | 68,690,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 36,130,000.00 USD | 0.00 USD | 36,130,000.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD |
| `1D` | `1.12` | 36,110,000.00 USD | 0.00 USD | 36,110,000.00 USD | 0.00 USD | 47,700.00 USD | 0.00 USD |
| `7D` | `1.12` | 68,610,000.00 USD | 0.00 USD | 68,610,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `1.13` | 36,070,000.00 USD | 0.00 USD | 36,070,000.00 USD | 0.00 USD | 1,660.00 USD | 0.00 USD |
| `7D` | `1.13` | 68,610,000.00 USD | 0.00 USD | 68,610,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 36,060,000.00 USD | 0.00 USD | 36,060,000.00 USD | 0.00 USD | 107,140.00 USD | 76,730.00 USD |
| `7D` | `1.13` | 68,410,000.00 USD | 0.00 USD | 68,410,000.00 USD | 5,450.00 USD | 2,160.00 USD | 3,970.00 USD |
| `1D` | `1.13` | 35,880,000.00 USD | 0.00 USD | 35,880,000.00 USD | 0.00 USD | 0.00 USD | 166,310.00 USD |
| `7D` | `1.13` | 68,400,000.00 USD | 0.00 USD | 68,400,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD |
| `1D` | `1.13` | 35,710,000.00 USD | 0.00 USD | 35,710,000.00 USD | 7,260.00 USD | 0.00 USD | 8,110.00 USD |
| `7D` | `1.14` | 67,920,000.00 USD | 0.00 USD | 67,920,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD |
| `1D` | `1.14` | 35,700,000.00 USD | 0.00 USD | 35,700,000.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD |
| `7D` | `1.14` | 67,680,000.00 USD | 0.00 USD | 67,680,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `7D` | `1.14` | 67,580,000.00 USD | 0.00 USD | 67,580,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 35,560,000.00 USD | 0.00 USD | 35,560,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.14` | 67,570,000.00 USD | 0.00 USD | 67,570,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 35,500,000.00 USD | 0.00 USD | 35,500,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 67,510,000.00 USD | 0.00 USD | 67,510,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.14` | 35,420,000.00 USD | 0.00 USD | 35,420,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.15` | 67,390,000.00 USD | 0.00 USD | 67,390,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 67,380,000.00 USD | 0.00 USD | 67,380,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 35,290,000.00 USD | 0.00 USD | 35,290,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 67,240,000.00 USD | 0.00 USD | 67,240,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 66,880,000.00 USD | 0.00 USD | 66,880,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 35,280,000.00 USD | 0.00 USD | 35,280,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 66,720,000.00 USD | 0.00 USD | 66,720,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.15` | 35,210,000.00 USD | 0.00 USD | 35,210,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.16` | 66,330,000.00 USD | 0.00 USD | 66,330,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 34,830,000.00 USD | 0.00 USD | 34,830,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 65,690,000.00 USD | 0.00 USD | 65,690,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 34,710,000.00 USD | 0.00 USD | 34,710,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD |
| `7D` | `1.16` | 64,890,000.00 USD | 0.00 USD | 64,890,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 34,530,000.00 USD | 0.00 USD | 34,530,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 64,360,000.00 USD | 0.00 USD | 64,360,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 34,150,000.00 USD | 0.00 USD | 34,150,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 63,340,000.00 USD | 0.00 USD | 63,340,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 33,410,000.00 USD | 0.00 USD | 33,410,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.17` | 61,970,000.00 USD | 0.00 USD | 61,970,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 32,980,000.00 USD | 0.00 USD | 32,980,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 61,340,000.00 USD | 0.00 USD | 61,340,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 32,650,000.00 USD | 0.00 USD | 32,650,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 59,960,000.00 USD | 0.00 USD | 59,960,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 32,470,000.00 USD | 0.00 USD | 32,470,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 58,450,000.00 USD | 0.00 USD | 58,450,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 32,310,000.00 USD | 0.00 USD | 32,310,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 57,070,000.00 USD | 0.00 USD | 57,070,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.17` | 32,090,000.00 USD | 0.00 USD | 32,090,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.18` | 56,270,000.00 USD | 0.00 USD | 56,270,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 31,820,000.00 USD | 0.00 USD | 31,820,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 55,390,000.00 USD | 0.00 USD | 55,390,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 31,600,000.00 USD | 0.00 USD | 31,600,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 54,930,000.00 USD | 0.00 USD | 54,930,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 31,420,000.00 USD | 0.00 USD | 31,420,000.00 USD | 71,950.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 54,210,000.00 USD | 0.00 USD | 54,210,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 31,320,000.00 USD | 0.00 USD | 31,320,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 53,840,000.00 USD | 0.00 USD | 53,840,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.18` | 31,240,000.00 USD | 0.00 USD | 31,240,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.19` | 53,710,000.00 USD | 0.00 USD | 53,710,000.00 USD | 127,700.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 31,130,000.00 USD | 0.00 USD | 31,130,000.00 USD | 59,140.00 USD | 145,870.00 USD | 25,350.00 USD |
| `7D` | `1.19` | 53,200,000.00 USD | 0.00 USD | 53,200,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD |
| `1D` | `1.19` | 30,900,000.00 USD | 0.00 USD | 30,900,000.00 USD | 189,200.00 USD | 3,790.00 USD | 599,810.00 USD |
| `7D` | `1.19` | 52,420,000.00 USD | 0.00 USD | 52,420,000.00 USD | 182,110.00 USD | 132,500.00 USD | 278,870.00 USD |
| `1D` | `1.19` | 30,100,000.00 USD | 0.00 USD | 30,100,000.00 USD | 10,800.00 USD | 3,540.00 USD | 21,580.00 USD |
| `7D` | `1.19` | 51,830,000.00 USD | 0.00 USD | 51,830,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD |
| `1D` | `1.19` | 30,070,000.00 USD | 0.00 USD | 30,070,000.00 USD | 40,460.00 USD | 17,460.00 USD | 92,300.00 USD |
| `7D` | `1.19` | 51,140,000.00 USD | 0.00 USD | 51,140,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 66,050.00 USD | 221,930.00 USD | 69,720.00 USD |
| `7D` | `1.20` | 50,480,000.00 USD | 0.00 USD | 50,480,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 29,560,000.00 USD | 0.00 USD | 29,560,000.00 USD | 31,180.00 USD | 6,070.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 49,770,000.00 USD | 0.00 USD | 49,770,000.00 USD | 5,350.00 USD | 97,860.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 29,490,000.00 USD | 0.00 USD | 29,490,000.00 USD | 39,940.00 USD | 0.00 USD | 8,200.00 USD |
| `7D` | `1.20` | 49,480,000.00 USD | 0.00 USD | 49,480,000.00 USD | 67,200.00 USD | 57,670.00 USD | 201,810.00 USD |
| `1D` | `1.20` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD |
| `7D` | `1.20` | 49,150,000.00 USD | 0.00 USD | 49,150,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD |
| `7D` | `1.20` | 49,070,000.00 USD | 0.00 USD | 49,070,000.00 USD | 202,570.00 USD | 53,170.00 USD | 534,000.00 USD |
| `1D` | `1.20` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 31,120.00 USD | 106,230.00 USD | 191,830.00 USD |
| `7D` | `1.21` | 48,280,000.00 USD | 0.00 USD | 48,280,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 29,110,000.00 USD | 0.00 USD | 29,110,000.00 USD | 0.00 USD | 163,810.00 USD | 0.00 USD |
| `7D` | `1.21` | 48,190,000.00 USD | 0.00 USD | 48,190,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 28,940,000.00 USD | 0.00 USD | 28,940,000.00 USD | 0.00 USD | 67,350.00 USD | 415,780.00 USD |
| `7D` | `1.21` | 48,090,000.00 USD | 0.00 USD | 48,090,000.00 USD | 468,800.00 USD | 518,690.00 USD | 368,310.00 USD |
| `1D` | `1.21` | 28,460,000.00 USD | 0.00 USD | 28,460,000.00 USD | 135,040.00 USD | 244,960.00 USD | 91,370.00 USD |
| `7D` | `1.21` | 46,740,000.00 USD | 0.00 USD | 46,740,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD |
| `1D` | `1.21` | 27,990,000.00 USD | 0.00 USD | 27,990,000.00 USD | 419,060.00 USD | 334,050.00 USD | 1,230,000.00 USD |
| `7D` | `1.21` | 45,490,000.00 USD | 0.00 USD | 45,490,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.21` | 26,010,000.00 USD | 0.00 USD | 26,010,000.00 USD | 9,150.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `1.22` | 45,080,000.00 USD | 0.00 USD | 45,080,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD |
| `1D` | `1.22` | 25,980,000.00 USD | 0.00 USD | 25,980,000.00 USD | 117,720.00 USD | 0.00 USD | 122,170.00 USD |
| `7D` | `1.22` | 44,910,000.00 USD | 0.00 USD | 44,910,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD |
| `1D` | `1.22` | 25,740,000.00 USD | 0.00 USD | 25,740,000.00 USD | 174,270.00 USD | 380,580.00 USD | 135,230.00 USD |
| `7D` | `1.22` | 44,360,000.00 USD | 0.00 USD | 44,360,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 25,050,000.00 USD | 0.00 USD | 25,050,000.00 USD | 157,550.00 USD | 6,840.00 USD | 208,620.00 USD |
| `7D` | `1.22` | 44,060,000.00 USD | 0.00 USD | 44,060,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 24,680,000.00 USD | 0.00 USD | 24,680,000.00 USD | 0.00 USD | 211.25 USD | 47,550.00 USD |
| `7D` | `1.22` | 43,560,000.00 USD | 0.00 USD | 43,560,000.00 USD | 0.00 USD | 191,360.00 USD | 1,020,000.00 USD |
| `1D` | `1.22` | 24,630,000.00 USD | 0.00 USD | 24,630,000.00 USD | 40,080.00 USD | 486,000.00 USD | 1,160,000.00 USD |
| `7D` | `1.23` | 42,350,000.00 USD | 0.00 USD | 42,350,000.00 USD | 627,450.00 USD | 191,250.00 USD | 4,910.00 USD |
| `1D` | `1.23` | 22,940,000.00 USD | 0.00 USD | 22,940,000.00 USD | 449,150.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `1.23` | 41,520,000.00 USD | 0.00 USD | 41,520,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 21,340,000.00 USD | 0.00 USD | 21,340,000.00 USD | 48,560.00 USD | 8,280.00 USD | 0.00 USD |
| `7D` | `1.23` | 41,060,000.00 USD | 0.00 USD | 41,060,000.00 USD | 0.00 USD | 917,970.00 USD | 995,690.00 USD |
| `1D` | `1.23` | 21,280,000.00 USD | 0.00 USD | 21,280,000.00 USD | 191,290.00 USD | 563,770.00 USD | 543,750.00 USD |
| `7D` | `1.23` | 39,150,000.00 USD | 0.00 USD | 39,150,000.00 USD | 782,590.00 USD | 479,460.00 USD | 8,010.00 USD |
| `1D` | `1.23` | 19,990,000.00 USD | 0.00 USD | 19,990,000.00 USD | 271,900.00 USD | 757,410.00 USD | 831,560.00 USD |
| `7D` | `1.23` | 37,880,000.00 USD | 0.00 USD | 37,880,000.00 USD | 656,500.00 USD | 597,200.00 USD | 112,990.00 USD |
| `1D` | `1.23` | 18,120,000.00 USD | 0.00 USD | 18,120,000.00 USD | 86,170.00 USD | 134,700.00 USD | 14,480.00 USD |
| `7D` | `1.24` | 36,510,000.00 USD | 0.00 USD | 36,510,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,120.00 USD |
| `1D` | `1.24` | 17,890,000.00 USD | 0.00 USD | 17,890,000.00 USD | 0.00 USD | 233,740.00 USD | 25,090.00 USD |
| `7D` | `1.24` | 34,450,000.00 USD | 0.00 USD | 34,450,000.00 USD | 1,640,000.00 USD | 1,110,000.00 USD | 719,360.00 USD |
| `1D` | `1.24` | 17,630,000.00 USD | 0.00 USD | 17,630,000.00 USD | 0.00 USD | 244,750.00 USD | 0.00 USD |
| `7D` | `1.24` | 30,980,000.00 USD | 0.00 USD | 30,980,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.24` | 17,390,000.00 USD | 0.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 340,590.00 USD |
| `7D` | `1.24` | 29,210,000.00 USD | 0.00 USD | 29,210,000.00 USD | 1,820,000.00 USD | 0.00 USD | 1,940,000.00 USD |
| `1D` | `1.24` | 17,040,000.00 USD | 0.00 USD | 17,040,000.00 USD | 112,970.00 USD | 655,230.00 USD | 1,260,000.00 USD |
| `7D` | `1.24` | 25,440,000.00 USD | 0.00 USD | 25,440,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `1.24` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 721,110.00 USD | 0.00 USD | 2,340,000.00 USD |
| `7D` | `1.25` | 23,530,000.00 USD | 0.00 USD | 23,530,000.00 USD | 2,670,000.00 USD | 923,130.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 11,960,000.00 USD | 0.00 USD | 11,960,000.00 USD | 861,120.00 USD | 351,240.00 USD | 551,670.00 USD |
| `7D` | `1.25` | 18,260,000.00 USD | 0.00 USD | 18,260,000.00 USD | 2,330,000.00 USD | 2,110,000.00 USD | 0.00 USD |
| `1D` | `1.25` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 218,430.00 USD | 1,300,000.00 USD | 2,020,000.00 USD |
| `7D` | `1.25` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 2,720,000.00 USD | 1,770,000.00 USD | 51,920.00 USD |
| `1D` | `1.25` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 1,110,000.00 USD | 489,510.00 USD | 1,170,000.00 USD |
| `7D` | `1.25` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 2,810,000.00 USD | 888,720.00 USD | 44,180.00 USD |
| `1D` | `1.25` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 351,630.00 USD | 0.00 USD | 4,230.00 USD |
| `7D` | `1.25` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 1,240,000.00 USD | 403,270.00 USD | 104,700.00 USD |
| `1D` | `1.25` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 551,630.00 USD | 0.00 USD | 6,120.00 USD |
| `7D` | `1.25` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 998,540.00 USD | 0.00 USD | 18,740.00 USD |
| `1D` | `1.26` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 1,460,000.00 USD | 2,600.00 USD | 0.00 USD |
| `7D` | `1.26` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,030,000.00 USD | 2,680.00 USD | 0.00 USD |
| `7D` | `1.26` | 592,290.00 USD | 0.00 USD | 592,290.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 476,680.00 USD | 0.00 USD | 476,680.00 USD | 472,940.00 USD | 3,750.00 USD | 0.00 USD |
| `7D` | `1.26` | 485,150.00 USD | 0.00 USD | 485,150.00 USD | 0.00 USD | 0.00 USD | 485,150.00 USD |
| `1D` | `1.26` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 424,010.00 USD | 0.00 USD | 1,230,000.00 USD |
| `1D` | `1.26` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 424,010.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.26` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 23,320.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 39,860.00 USD | 1,030,000.00 USD | 82,450.00 USD |
| `7D` | `1.27` | 21,710,000.00 USD | 21,710,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,990,000.00 USD | 8,250,000.00 USD |
| `1D` | `1.27` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 1,930,000.00 USD | 794,130.00 USD |
| `7D` | `1.27` | 26,480,000.00 USD | 26,480,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 780,430.00 USD | 1,660,000.00 USD |
| `7D` | `1.27` | 29,320,000.00 USD | 29,320,000.00 USD | 0.00 USD | 178,380.00 USD | 2,540,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 961,090.00 USD | 583,330.00 USD | 57,120.00 USD |
| `7D` | `1.27` | 34,050,000.00 USD | 34,050,000.00 USD | 0.00 USD | 186,960.00 USD | 3,970,000.00 USD | 567,370.00 USD |
| `1D` | `1.27` | 15,770,000.00 USD | 15,770,000.00 USD | 0.00 USD | 60,090.00 USD | 1,220,000.00 USD | 1,700,000.00 USD |
| `7D` | `1.27` | 48,430,000.00 USD | 48,430,000.00 USD | 0.00 USD | 4,420,000.00 USD | 1,750,000.00 USD | 8,210,000.00 USD |
| `1D` | `1.28` | 21,010,000.00 USD | 21,010,000.00 USD | 0.00 USD | 481,200.00 USD | 1,850,000.00 USD | 2,910,000.00 USD |
| `7D` | `1.28` | 66,700,000.00 USD | 66,700,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 34,280,000.00 USD | 34,280,000.00 USD | 0.00 USD | 6,010,000.00 USD | 2,730,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 72,800,000.00 USD | 72,800,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,750,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 37,120,000.00 USD | 37,120,000.00 USD | 0.00 USD | 188,330.00 USD | 1,960,000.00 USD | 695,980.00 USD |
| `7D` | `1.28` | 73,750,000.00 USD | 73,750,000.00 USD | 0.00 USD | 0.00 USD | 873,350.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 38,910,000.00 USD | 38,910,000.00 USD | 0.00 USD | 547,110.00 USD | 0.00 USD | 1,240,000.00 USD |
| `7D` | `1.28` | 75,380,000.00 USD | 75,380,000.00 USD | 0.00 USD | 1,080,000.00 USD | 478,060.00 USD | 67,480.00 USD |
| `1D` | `1.28` | 40,870,000.00 USD | 40,870,000.00 USD | 0.00 USD | 673,540.00 USD | 418,710.00 USD | 869,370.00 USD |
| `7D` | `1.28` | 78,970,000.00 USD | 78,970,000.00 USD | 0.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD |
| `1D` | `1.29` | 42,880,000.00 USD | 42,880,000.00 USD | 0.00 USD | 303,010.00 USD | 687,930.00 USD | 1,020,000.00 USD |
| `7D` | `1.29` | 80,140,000.00 USD | 80,140,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 43,890,000.00 USD | 43,890,000.00 USD | 0.00 USD | 584,100.00 USD | 411,690.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 80,250,000.00 USD | 80,250,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 43,910,000.00 USD | 43,910,000.00 USD | 0.00 USD | 18,290.00 USD | 3,310.00 USD | 0.00 USD |
| `7D` | `1.29` | 82,340,000.00 USD | 82,340,000.00 USD | 0.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD |
| `1D` | `1.29` | 45,700,000.00 USD | 45,700,000.00 USD | 0.00 USD | 369,880.00 USD | 0.00 USD | 1,420,000.00 USD |
| `7D` | `1.29` | 82,760,000.00 USD | 82,760,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 49,640,000.00 USD | 49,640,000.00 USD | 0.00 USD | 1,110,000.00 USD | 305,230.00 USD | 2,530,000.00 USD |
| `7D` | `1.29` | 92,400,000.00 USD | 92,400,000.00 USD | 0.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 54,550,000.00 USD | 54,550,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,120,000.00 USD | 2,380,000.00 USD |
| `7D` | `1.30` | 93,630,000.00 USD | 93,630,000.00 USD | 0.00 USD | 209,360.00 USD | 393,370.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 55,280,000.00 USD | 55,280,000.00 USD | 0.00 USD | 344,680.00 USD | 422.50 USD | 383,310.00 USD |
| `7D` | `1.30` | 95,050,000.00 USD | 95,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD |
| `1D` | `1.30` | 55,950,000.00 USD | 55,950,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD |
| `7D` | `1.30` | 96,310,000.00 USD | 96,310,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 58,110,000.00 USD | 58,110,000.00 USD | 0.00 USD | 602,010.00 USD | 897,120.00 USD | 659,740.00 USD |
| `7D` | `1.30` | 99,310,000.00 USD | 99,310,000.00 USD | 0.00 USD | 0.00 USD | 2,510,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 58,830,000.00 USD | 58,830,000.00 USD | 0.00 USD | 188,510.00 USD | 204,330.00 USD | 319,160.00 USD |
| `1D` | `1.31` | 60,120,000.00 USD | 60,120,000.00 USD | 0.00 USD | 493,480.00 USD | 477,560.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 102,320,000.00 USD | 102,320,000.00 USD | 0.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 63,110,000.00 USD | 63,110,000.00 USD | 0.00 USD | 767,340.00 USD | 278,540.00 USD | 1,950,000.00 USD |
| `7D` | `1.31` | 106,580,000.00 USD | 106,580,000.00 USD | 0.00 USD | 1,480,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD |
| `1D` | `1.31` | 65,710,000.00 USD | 65,710,000.00 USD | 0.00 USD | 908,870.00 USD | 396,100.00 USD | 1,290,000.00 USD |
| `7D` | `1.31` | 109,840,000.00 USD | 109,840,000.00 USD | 0.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD |
| `1D` | `1.31` | 69,030,000.00 USD | 69,030,000.00 USD | 0.00 USD | 1,800,000.00 USD | 778,210.00 USD | 745,480.00 USD |
| `7D` | `1.31` | 112,690,000.00 USD | 112,690,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 70,750,000.00 USD | 70,750,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 115,140,000.00 USD | 115,140,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 76,520,000.00 USD | 76,520,000.00 USD | 0.00 USD | 222,150.00 USD | 1,680,000.00 USD | 3,860,000.00 USD |
| `7D` | `1.32` | 119,770,000.00 USD | 119,770,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 83,320,000.00 USD | 83,320,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD |
| `7D` | `1.32` | 122,850,000.00 USD | 122,850,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 86,630,000.00 USD | 86,630,000.00 USD | 0.00 USD | 1,680,000.00 USD | 608,860.00 USD | 1,030,000.00 USD |
| `7D` | `1.32` | 124,680,000.00 USD | 124,680,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 91,270,000.00 USD | 91,270,000.00 USD | 0.00 USD | 1,870,000.00 USD | 845,300.00 USD | 1,920,000.00 USD |
| `7D` | `1.32` | 129,130,000.00 USD | 129,130,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 94,320,000.00 USD | 94,320,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,620.00 USD | 1,020,000.00 USD |
| `7D` | `1.32` | 131,500,000.00 USD | 131,500,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 96,610,000.00 USD | 96,610,000.00 USD | 0.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 132,040,000.00 USD | 132,040,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 98,800,000.00 USD | 98,800,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 133,190,000.00 USD | 133,190,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 101,240,000.00 USD | 101,240,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 134,910,000.00 USD | 134,910,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 103,500,000.00 USD | 103,500,000.00 USD | 0.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD |
| `7D` | `1.33` | 138,970,000.00 USD | 138,970,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 105,830,000.00 USD | 105,830,000.00 USD | 0.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD |
| `7D` | `1.33` | 139,510,000.00 USD | 139,510,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 108,270,000.00 USD | 108,270,000.00 USD | 0.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 141,460,000.00 USD | 141,460,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 110,950,000.00 USD | 110,950,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD |
| `7D` | `1.34` | 143,800,000.00 USD | 143,800,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 113,420,000.00 USD | 113,420,000.00 USD | 0.00 USD | 1,020,000.00 USD | 362,960.00 USD | 1,080,000.00 USD |
| `7D` | `1.34` | 148,510,000.00 USD | 148,510,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 116,920,000.00 USD | 116,920,000.00 USD | 0.00 USD | 1,630,000.00 USD | 729,880.00 USD | 1,140,000.00 USD |
| `7D` | `1.34` | 154,180,000.00 USD | 154,180,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD |
| `1D` | `1.34` | 120,190,000.00 USD | 120,190,000.00 USD | 0.00 USD | 1,470,000.00 USD | 626,040.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 165,240,000.00 USD | 165,240,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 121,420,000.00 USD | 121,420,000.00 USD | 0.00 USD | 498,430.00 USD | 251,400.00 USD | 481,220.00 USD |
| `7D` | `1.35` | 172,360,000.00 USD | 172,360,000.00 USD | 0.00 USD | 2,410,000.00 USD | 2,230,000.00 USD | 2,470,000.00 USD |
| `1D` | `1.35` | 122,680,000.00 USD | 122,680,000.00 USD | 0.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD |
| `7D` | `1.35` | 182,670,000.00 USD | 182,670,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 124,170,000.00 USD | 124,170,000.00 USD | 0.00 USD | 771,840.00 USD | 229,490.00 USD | 488,180.00 USD |
| `7D` | `1.35` | 190,440,000.00 USD | 190,440,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 125,490,000.00 USD | 125,490,000.00 USD | 0.00 USD | 558,120.00 USD | 207,050.00 USD | 556,870.00 USD |
| `7D` | `1.35` | 198,760,000.00 USD | 198,760,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 126,860,000.00 USD | 126,860,000.00 USD | 0.00 USD | 503,350.00 USD | 201,050.00 USD | 668,380.00 USD |
| `7D` | `1.35` | 206,990,000.00 USD | 206,990,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 128,080,000.00 USD | 128,080,000.00 USD | 0.00 USD | 510,040.00 USD | 122,540.00 USD | 579,020.00 USD |
| `7D` | `1.36` | 211,090,000.00 USD | 211,090,000.00 USD | 0.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 128,940,000.00 USD | 128,940,000.00 USD | 0.00 USD | 412,060.00 USD | 41,890.00 USD | 409,020.00 USD |
| `7D` | `1.36` | 214,870,000.00 USD | 214,870,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 129,520,000.00 USD | 129,520,000.00 USD | 0.00 USD | 266,880.00 USD | 78,370.00 USD | 233,330.00 USD |
| `7D` | `1.36` | 217,010,000.00 USD | 217,010,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 130,180,000.00 USD | 130,180,000.00 USD | 0.00 USD | 241,460.00 USD | 104,340.00 USD | 321,110.00 USD |
| `7D` | `1.36` | 221,110,000.00 USD | 221,110,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 130,320,000.00 USD | 130,320,000.00 USD | 0.00 USD | 80,160.00 USD | 27,780.00 USD | 31,150.00 USD |
| `7D` | `1.36` | 222,830,000.00 USD | 222,830,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 130,520,000.00 USD | 130,520,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 138,790.00 USD |
| `7D` | `1.37` | 223,310,000.00 USD | 223,310,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 130,750,000.00 USD | 130,750,000.00 USD | 0.00 USD | 84,710.00 USD | 105,400.00 USD | 44,320.00 USD |
| `7D` | `1.37` | 224,730,000.00 USD | 224,730,000.00 USD | 0.00 USD | 528,490.00 USD | 136,720.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 130,930,000.00 USD | 130,930,000.00 USD | 0.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD |
| `7D` | `1.37` | 225,910,000.00 USD | 225,910,000.00 USD | 0.00 USD | 345,700.00 USD | 372,470.00 USD | 461,160.00 USD |
| `1D` | `1.37` | 131,060,000.00 USD | 131,060,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 228,510,000.00 USD | 228,510,000.00 USD | 0.00 USD | 920,600.00 USD | 404,120.00 USD | 1,270,000.00 USD |
| `1D` | `1.37` | 131,210,000.00 USD | 131,210,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.38` | 230,100,000.00 USD | 230,100,000.00 USD | 0.00 USD | 536,130.00 USD | 294,500.00 USD | 759,750.00 USD |
| `1D` | `1.38` | 131,460,000.00 USD | 131,460,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 231,660,000.00 USD | 231,660,000.00 USD | 0.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 131,960,000.00 USD | 131,960,000.00 USD | 0.00 USD | 231,710.00 USD | 72,370.00 USD | 195,200.00 USD |
| `7D` | `1.38` | 233,790,000.00 USD | 233,790,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD |
| `1D` | `1.38` | 132,400,000.00 USD | 132,400,000.00 USD | 0.00 USD | 162,970.00 USD | 90,840.00 USD | 182,000.00 USD |
| `7D` | `1.38` | 236,340,000.00 USD | 236,340,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 132,640,000.00 USD | 132,640,000.00 USD | 0.00 USD | 79,200.00 USD | 80,770.00 USD | 76,250.00 USD |
| `7D` | `1.38` | 237,420,000.00 USD | 237,420,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 132,980,000.00 USD | 132,980,000.00 USD | 0.00 USD | 131,770.00 USD | 0.00 USD | 214,750.00 USD |
| `7D` | `1.39` | 238,710,000.00 USD | 238,710,000.00 USD | 0.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 133,010,000.00 USD | 133,010,000.00 USD | 0.00 USD | 7,260.00 USD | 15,600.00 USD | 8,110.00 USD |
| `7D` | `1.39` | 239,250,000.00 USD | 239,250,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD |
| `1D` | `1.39` | 133,150,000.00 USD | 133,150,000.00 USD | 0.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD |
| `7D` | `1.39` | 240,350,000.00 USD | 240,350,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 240,520,000.00 USD | 240,520,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 133,150,000.00 USD | 133,150,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 240,850,000.00 USD | 240,850,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 133,220,000.00 USD | 133,220,000.00 USD | 0.00 USD | 31,140.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.40` | 241,010,000.00 USD | 241,010,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 133,290,000.00 USD | 133,290,000.00 USD | 0.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.40` | 241,130,000.00 USD | 241,130,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.40` | 133,420,000.00 USD | 133,420,000.00 USD | 0.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.40` | 241,140,000.00 USD | 241,140,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 241,280,000.00 USD | 241,280,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 241,400,000.00 USD | 241,400,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `1D` | `1.40` | 133,430,000.00 USD | 133,430,000.00 USD | 0.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.41` | 241,640,000.00 USD | 241,640,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 241,800,000.00 USD | 241,800,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.41` | 133,500,000.00 USD | 133,500,000.00 USD | 0.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.41` | 242,180,000.00 USD | 242,180,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.41` | 133,880,000.00 USD | 133,880,000.00 USD | 0.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.41` | 242,830,000.00 USD | 242,830,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.41` | 134,000,000.00 USD | 134,000,000.00 USD | 0.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.41` | 243,010,000.00 USD | 243,010,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.41` | 134,010,000.00 USD | 134,010,000.00 USD | 0.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD |
| `7D` | `1.42` | 243,630,000.00 USD | 243,630,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `1D` | `1.42` | 134,180,000.00 USD | 134,180,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD |
| `7D` | `1.42` | 244,160,000.00 USD | 244,160,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.42` | 134,560,000.00 USD | 134,560,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 245,180,000.00 USD | 245,180,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.42` | 135,300,000.00 USD | 135,300,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 246,550,000.00 USD | 246,550,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.42` | 135,720,000.00 USD | 135,720,000.00 USD | 0.00 USD | 149,490.00 USD | 92,570.00 USD | 175,760.00 USD |
| `7D` | `1.42` | 247,180,000.00 USD | 247,180,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 247,540,000.00 USD | 247,540,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 248,560,000.00 USD | 248,560,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 250,070,000.00 USD | 250,070,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 251,450,000.00 USD | 251,450,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 252,250,000.00 USD | 252,250,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 252,780,000.00 USD | 252,780,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 253,130,000.00 USD | 253,130,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 253,590,000.00 USD | 253,590,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 254,310,000.00 USD | 254,310,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 254,680,000.00 USD | 254,680,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 254,810,000.00 USD | 254,810,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 254,930,000.00 USD | 254,930,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 255,270,000.00 USD | 255,270,000.00 USD | 0.00 USD | 66,640.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 255,880,000.00 USD | 255,880,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 256,440,000.00 USD | 256,440,000.00 USD | 0.00 USD | 182,110.00 USD | 128,180.00 USD | 251,300.00 USD |
| `7D` | `1.46` | 256,900,000.00 USD | 256,900,000.00 USD | 0.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `7D` | `1.46` | 257,060,000.00 USD | 257,060,000.00 USD | 0.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD |
| `7D` | `1.46` | 257,530,000.00 USD | 257,530,000.00 USD | 0.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD |
| `7D` | `1.46` | 257,740,000.00 USD | 257,740,000.00 USD | 0.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.89B` | Total OI Tokens: `2,302,999,549.3 XRP`
  * 1h OI Change: `+2.05%` | 4h OI Change: `-3.57%` | 24h OI Change: `-3.14%`
  * Exchange Breakdown: Binance=`466.74M` | Bybit=`322.77M` | OKX=`98.35M` | Hyperliquid=`222.07M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-18.09K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0005%` | **USDT OKX** | `0.0024%` |
| **USDT Bybit** | `-0.0088%` | **USDT KuCoin** | `0.0023%` |
| **USDT MEXC** | `0.0004%` | **USDT BingX** | `0.0028%` |
| **USDT Gate** | `-0.0010%` | **USDT Bitget** | `-0.0019%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `49.71%` | `50.29%` | `0.99` | 1,380,000,000.00 USD |
| `15M` | `Binance` | `43.35%` | `56.65%` | `0.77` | 411,940,000.00 USD |
| `15M` | `OKX` | `57.72%` | `42.28%` | `1.37` | 203,500,000.00 USD |
| `15M` | `Bybit` | `46.17%` | `53.83%` | `0.86` | 168,480,000.00 USD |
| `15M` | `KuCoin` | `61.74%` | `38.26%` | `1.61` | 5,760,000.00 USD |
| `15M` | `Gate` | `51.61%` | `48.39%` | `1.07` | 121,320,000.00 USD |
| `15M` | `Bitget` | `53.09%` | `46.91%` | `1.13` | 60,590,000.00 USD |
| `15M` | `BingX` | `45.37%` | `54.63%` | `0.83` | 14,520,000.00 USD |
| `15M` | `MEXC` | `45.13%` | `54.87%` | `0.82` | 54,080,000.00 USD |
| `15M` | `Bitunix` | `41.25%` | `58.75%` | `0.70` | 51,330,000.00 USD |
| `15M` | `Hyperliquid` | `50.11%` | `49.89%` | `1.00` | 152,090,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.58%` | `64.42%` | `0.55` | 6,210,000.00 USD |
| `15M` | `Crypto.com` | `54.67%` | `45.33%` | `1.21` | 3,360,000.00 USD |
| `15M` | `WhiteBIT` | `86.07%` | `13.93%` | `6.18` | 41,280,000.00 USD |
| `15M` | `HTX` | `48.85%` | `51.15%` | `0.96` | 3,440,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `60.19%` | `39.81%` | `1.51` | 31,030,000.00 USD |
| `15M` | `Bitfinex` | `42.24%` | `57.76%` | `0.73` | 1,180,000.00 USD |
| `15M` | `Kraken` | `54.71%` | `45.29%` | `1.21` | 16,600,000.00 USD |
| `15M` | `Aster` | `46.76%` | `53.24%` | `0.88` | 7,790,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `47.79%` | `52.21%` | `0.92` | 23,310,000.00 USD |
| `15M` | `Whale Positions` | `43.35%` | `56.65%` | `0.77` | 411,940,000.00 USD |
| `15M` | `Global Accounts` | `49.71%` | `50.29%` | `0.99` | 1,380,000,000.00 USD |
| `1H` | `XRP` | `49.03%` | `50.97%` | `0.96` | 9,870,000,000.00 USD |
| `1H` | `Binance` | `47.88%` | `52.12%` | `0.92` | 2,820,000,000.00 USD |
| `1H` | `OKX` | `48.04%` | `51.96%` | `0.92` | 1,450,000,000.00 USD |
| `1H` | `Bybit` | `51.28%` | `48.72%` | `1.05` | 686,440,000.00 USD |
| `1H` | `KuCoin` | `60.55%` | `39.45%` | `1.53` | 127,960,000.00 USD |
| `1H` | `Gate` | `50.01%` | `49.99%` | `1.00` | 996,500,000.00 USD |
| `1H` | `Bitget` | `51.12%` | `48.88%` | `1.05` | 413,400,000.00 USD |
| `1H` | `BingX` | `52.39%` | `47.61%` | `1.10` | 102,110,000.00 USD |
| `1H` | `MEXC` | `51.43%` | `48.57%` | `1.06` | 258,090,000.00 USD |
| `1H` | `Bitunix` | `48.55%` | `51.45%` | `0.94` | 295,550,000.00 USD |
| `1H` | `Hyperliquid` | `45.9%` | `54.1%` | `0.85` | 610,930,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.54%` | `44.46%` | `1.25` | 22,290,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `49.57%` | `50.43%` | `0.98` | 1,740,000,000.00 USD |
| `1H` | `HTX` | `42.67%` | `57.33%` | `0.74` | 65,020,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `51%` | `49%` | `1.04` | 47,450,000.00 USD |
| `1H` | `Bitfinex` | `31.7%` | `68.3%` | `0.46` | 2,850,000.00 USD |
| `1H` | `Kraken` | `48.34%` | `51.66%` | `0.94` | 38,480,000.00 USD |
| `1H` | `Aster` | `47.09%` | `52.91%` | `0.89` | 79,570,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.22%` | `47.78%` | `1.09` | 107,700,000.00 USD |
| `1H` | `Whale Positions` | `47.88%` | `52.12%` | `0.92` | 2,820,000,000.00 USD |
| `1H` | `Global Accounts` | `49.03%` | `50.97%` | `0.96` | 9,870,000,000.00 USD |
| `4H` | `XRP` | `46.74%` | `53.26%` | `0.88` | 27,170,000,000.00 USD |
| `4H` | `Binance` | `45.42%` | `54.58%` | `0.83` | 7,560,000,000.00 USD |
| `4H` | `OKX` | `45.6%` | `54.4%` | `0.84` | 3,350,000,000.00 USD |
| `4H` | `Bybit` | `44.19%` | `55.81%` | `0.79` | 3,280,000,000.00 USD |
| `4H` | `KuCoin` | `50%` | `50%` | `1.00` | 122,060,000.00 USD |
| `4H` | `Gate` | `51.35%` | `48.65%` | `1.06` | 2,170,000,000.00 USD |
| `4H` | `Bitget` | `51.8%` | `48.2%` | `1.07` | 1,190,000,000.00 USD |
| `4H` | `BingX` | `51.83%` | `48.17%` | `1.08` | 370,130,000.00 USD |
| `4H` | `MEXC` | `48.46%` | `51.54%` | `0.94` | 1,210,000,000.00 USD |
| `4H` | `Bitunix` | `50.41%` | `49.59%` | `1.02` | 1,200,000,000.00 USD |
| `4H` | `Hyperliquid` | `44.62%` | `55.38%` | `0.81` | 1,760,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.89%` | `47.11%` | `1.12` | 133,550,000.00 USD |
| `4H` | `Crypto.com` | `50.84%` | `49.16%` | `1.03` | 142,180,000.00 USD |
| `4H` | `WhiteBIT` | `46.55%` | `53.45%` | `0.87` | 3,250,000,000.00 USD |
| `4H` | `HTX` | `44.43%` | `55.57%` | `0.80` | 90,400,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.6%` | `48.4%` | `1.07` | 526,180,000.00 USD |
| `4H` | `Bitfinex` | `17.62%` | `82.38%` | `0.21` | 32,370,000.00 USD |
| `4H` | `Kraken` | `44%` | `56%` | `0.79` | 241,800,000.00 USD |
| `4H` | `Aster` | `45.18%` | `54.82%` | `0.82` | 236,020,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.68%` | `53.32%` | `0.88` | 306,950,000.00 USD |
| `4H` | `Whale Positions` | `45.42%` | `54.58%` | `0.83` | 7,560,000,000.00 USD |
| `4H` | `Global Accounts` | `46.74%` | `53.26%` | `0.88` | 27,170,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,036,330.68 USD | 2,484,228.37 USD | 2,552,102.32 USD | -67,873.95 USD | `-1.35%` | `8B / 7S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.28` | 3,779,916.77 USD | 1,963,240.26 USD | 1,816,676.51 USD | 146,563.75 USD | `+3.88%` | `6B / 5S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 7,767,016.10 USD | 3,262,612.53 USD | 4,504,403.57 USD | -1,241,791.04 USD | `-15.99%` | `7B / 12S` |
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.28` | `1.26` | 41,778,066.41 USD | 16,233,527.16 USD | 25,544,539.25 USD | -9,311,012.09 USD | `-22.29%` | `4B / 58S` |
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.27` | 9,197,225.16 USD | 4,639,147.41 USD | 4,558,077.75 USD | 81,069.66 USD | `+0.88%` | `4B / 5S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.27` | `1.23` | 112,851,214.34 USD | 44,440,734.72 USD | 68,410,479.62 USD | -23,969,744.90 USD | `-21.24%` | `0B / 35S` |
| `5:00 UTC` | `1.24` | `1.24` | `1.24` | `1.25` | `1.22` | 96,971,024.45 USD | 46,182,833.37 USD | 50,788,191.08 USD | -4,605,357.71 USD | `-4.75%` | `1B / 8S` |
| `0:00 UTC` | `1.25` | `1.24` | `1.25` | `1.25` | `1.23` | 42,899,530.36 USD | 22,765,315.89 USD | 20,134,214.47 USD | 2,631,101.42 USD | `+6.13%` | `25B / 6S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 36,075,332.57 USD | 17,198,898.48 USD | 18,876,434.09 USD | -1,677,535.61 USD | `-4.65%` | `12B / 8S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 13,585,521.24 USD | 7,455,777.07 USD | 6,129,744.17 USD | 1,326,032.90 USD | `+9.76%` | `8B / 3S` |

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
| `5m` | -89,690.00 USD | -319,600.00 USD | **`DISTRIBUTION`** |
| `15m` | 430,180.00 USD | 2,180,000.00 USD | **`ACCUMULATION`** |
| `30m` | 3,910,000.00 USD | 4,390,000.00 USD | **`ACCUMULATION`** |
| `1h` | -38,980.00 USD | -29,850,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -27,730,000.00 USD | -89,590,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -35,010,000.00 USD | -108,400,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -38,010,000.00 USD | -120,540,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -31,990,000.00 USD | -114,550,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -35,440,000.00 USD | -114,760,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -55,700,000.00 USD | -171,940,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -102,330,000.00 USD | -181,730,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -581,170,000.00 USD | -1,280,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-89.69K` | 15m=`+430.18K` | 1h=`-38.98K` | 24h=`-55.70M`
* Futures Capital Netflows: 5m=`-319.60K` | 15m=`+2.18M` | 1h=`-29.85M` | 24h=`-171.94M`
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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.25` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.23` (Risk Distance: `0.0203` pts)
  * +2.5R Take Profit: `1.30`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `0.0203` pts)
  * +2.5R Take Profit: `1.21`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
