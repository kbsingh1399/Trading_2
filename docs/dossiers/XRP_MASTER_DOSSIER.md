# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:16:49 IST` (`2026-10-29 22:46:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.25`
- **Spread Points**: `3.00` | **Spread BPS**: `24.07 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.28` | VWAP Z-Score: `-1.47` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0117` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.32` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.35` | Lower -3.00σ Band: `1.21`
  * Upper +2.51σ Band: `1.33` | Lower -2.51σ Band: `1.22`
  * Upper +2.01σ Band: `1.32` | Lower -2.01σ Band: `1.23`
  * Upper +2.00σ Band: `1.32` | Lower -2.00σ Band: `1.23`
  * Upper +1.28σ Band: `1.31` | Lower -1.28σ Band: `1.25`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.26`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.26` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.28` (Slope: `+0.0000`) | EMA-100=`1.29`
  * Institutional Anchors: EMA-144=`1.29` | EMA-200=`1.30` (Slope: `-0.4397`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.33` | 24H Low=`1.22` | Weekly High=`1.34` | Weekly Low=`1.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.86%`)
  * Point of Control (POC) = `1.25` (Distance: `-0.29%`)
  * Value Area Low (VAL) = `1.24` (Distance: `+0.12%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.32` | Weekly POC=`1.29` | Weekly VAL=`1.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.23`
  * London Session (08:00-16:00 UTC): High=`1.25` | Low=`1.24`
  * New York Session (13:00-21:00 UTC): High=`1.25` | Low=`1.24`
  * Initial Balance (First Hour): IB High=`1.25` | IB Low=`1.24`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.24` - `1.25`
  * Optimal Trade Entry (OTE 0.705): `1.25`
  * Structural Invalidation Anchor (0.786): `1.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `11,418,654` | 14,283,492.34 USD | -45,579.05 USD | `-0.32%` | -77,331,341.55 USD | `+0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `4,879,498` | 6,103,007.37 USD | -211,923.84 USD | `-3.47%` | -77,543,265.39 USD | `-0.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `4,678,017` | 5,842,525.42 USD | 524,479.19 USD | `+8.98%` | -77,018,786.20 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `30,318,431` | 37,964,913.08 USD | -1,211,583.20 USD | `-3.19%` | -76,658,136.95 USD | `+0.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `23,926,964` | 29,915,763.66 USD | -1,023,021.32 USD | `-3.42%` | -77,681,158.28 USD | `+0.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `4,678,017` | 5,842,525.42 USD | 524,479.19 USD | `+8.98%` | -77,156,679.08 USD | `+0.48` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.28` | `1.28` | `1.22` | `1.24` | `208,906,305` | 260,797,546.37 USD | -37,805,029.03 USD | `-14.50%` | -77,339,869.93 USD | `-3.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.24` | `1.26` | `1.23` | `1.25` | `86,510,066` | 108,215,327.13 USD | 1,874,321.17 USD | `+1.73%` | -75,465,548.76 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.25` | `58,912,278` | 73,709,272.85 USD | -1,723,951.07 USD | `-2.34%` | -77,189,499.82 USD | `+0.13` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `354,328,650` | 442,722,146.34 USD | -37,654,658.93 USD | `-8.51%` | -77,593,688.74 USD | `-1.75` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `354,328,650` | 442,722,146.34 USD | -37,654,658.93 USD | `-8.51%` | -77,593,688.74 USD | `-1.75` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `ASK` | `1.25` | `5954.0000` | 7,436.55 USD | 1,377,558.59 USD | `4 orders` | `+0.16%` | `-` |
| `ASK` | `1.25` | `44796.0000` | 55,945.72 USD | 1,370,122.04 USD | `5 orders` | `+0.15%` | `-` |
| `ASK` | `1.25` | `27816.0000` | 34,736.62 USD | 1,314,176.32 USD | `5 orders` | `+0.14%` | `-` |
| `ASK` | `1.25` | `91135.0000` | 113,800.27 USD | 1,279,439.70 USD | `8 orders` | `+0.13%` | `-` |
| `ASK` | `1.25` | `367228.0000` | 458,520.88 USD | 1,165,639.42 USD | `13 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `11335.0000` | 14,151.75 USD | 707,118.54 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `14069.0000` | 17,563.74 USD | 692,966.79 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.25` | `51234.0000` | 63,955.40 USD | 675,403.05 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.25` | `27370.0000` | 34,163.23 USD | 611,447.65 USD | `6 orders` | `+0.09%` | `-` |
| `ASK` | `1.25` | `66943.0000` | 83,551.56 USD | 577,284.42 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `248322.0000` | 309,905.86 USD | 493,732.86 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `43100.0000` | 53,784.49 USD | 183,827.00 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `1.25` | `27843.0000` | 34,742.50 USD | 130,042.51 USD | `6 orders` | `+0.06%` | `-` |
| `ASK` | `1.25` | `10503.0000` | 13,104.59 USD | 95,300.02 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `1.25` | `20518.0000` | 25,598.26 USD | 82,195.42 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `13460.0000` | 16,791.35 USD | 56,597.17 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `6768.0000` | 8,442.40 USD | 39,805.82 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `1.25` | `10797.0000` | 13,467.10 USD | 31,363.41 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `1.25` | `4316.0000` | 5,382.92 USD | 17,896.32 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `1.25` | `10034.0000` | 12,513.40 USD | 12,513.40 USD | `5 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.25` | `0.00%` | `-` |
| `BID` | `1.25` | `26404.0000` | 32,925.79 USD | 32,925.79 USD | `7 orders` | `-0.00%` | `-` |
| `BID` | `1.25` | `2630.0000` | 3,279.35 USD | 36,205.14 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `1.25` | `61709.0000` | 76,938.78 USD | 113,143.92 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `1.25` | `65466.0000` | 81,616.46 USD | 194,760.38 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `1.25` | `49708.0000` | 61,965.99 USD | 256,726.37 USD | `14 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `21907.0000` | 27,307.08 USD | 284,033.45 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `16062.0000` | 20,019.68 USD | 304,053.12 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `1.25` | `276870.0000` | 345,063.08 USD | 649,116.20 USD | `15 orders` | `-0.06%` | `-` |
| `BID` | `1.25` | `126065.0000` | 157,102.20 USD | 806,218.41 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `1.25` | `26792.0000` | 33,385.51 USD | 839,603.92 USD | `7 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `28450.0000` | 35,448.70 USD | 875,052.62 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `12011.0000` | 14,964.50 USD | 890,017.12 USD | `2 orders` | `-0.09%` | `-` |
| `BID` | `1.25` | `27992.0000` | 34,872.43 USD | 924,889.56 USD | `6 orders` | `-0.10%` | `-` |
| `BID` | `1.25` | `12135.0000` | 15,116.57 USD | 940,006.13 USD | `2 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `264314.0000` | 329,229.52 USD | 1,269,235.65 USD | `8 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `47227.0000` | 58,821.23 USD | 1,328,056.87 USD | `6 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `36221.0000` | 45,109.63 USD | 1,373,166.51 USD | `6 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `8568.0000` | 10,669.73 USD | 1,383,836.24 USD | `3 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `340180.0000` | 423,592.14 USD | 1,807,428.37 USD | `4 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `66163.0000` | 82,379.55 USD | 1,889,807.92 USD | `9 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 43,838,331.50 USD | `35,031,430.00` | `1.13` | `1.25` | `0.9612` | 4,259,448.24 USD | `+9.72%` | `10X Cross` |
| `92` | `0x5b5d...c060` | `SHORT` | 19,971,677.11 USD | `15,964,251.00` | `1.44` | `1.25` | `12.34` | 2,944,391.60 USD | `+14.74%` | `5X Cross` |
| `157` | `0xb83d...6e36` | `SHORT` | 13,209,090.13 USD | `10,555,450.00` | `1.50` | `1.25` | `15.54` | 2,613,479.51 USD | `+19.79%` | `5X Cross` |
| `242` | `0x58f0...0d20` | `LONG` | 9,416,659.37 USD | `7,526,704.00` | `1.25` | `1.25` | `1.22` | 25,494.82 USD | `+0.27%` | `20X Cross` |
| `383` | `0x77ee...a018` | `LONG` | 6,174,186.93 USD | `4,943,700.00` | `1.27` | `1.25` | `0.2971` | -104,312.07 USD | `-1.69%` | `20X Cross` |
| `401` | `0xecb6...2b00` | `SHORT` | 5,759,082.97 USD | `4,601,009.00` | `1.28` | `1.25` | `7.50` | 138,209.51 USD | `+2.40%` | `10X Cross` |
| `426` | `0xca49...53c8` | `SHORT` | 5,185,196.38 USD | `4,138,886.00` | `1.44` | `1.25` | `4.71` | 768,126.35 USD | `+14.81%` | `20X Cross` |
| `494` | `0xfc27...9d9d` | `SHORT` | 4,475,689.66 USD | `3,576,546.00` | `1.30` | `1.25` | `6.05` | 190,186.07 USD | `+4.25%` | `20X Cross` |
| `501` | `0x610b...b613` | `LONG` | 4,433,476.45 USD | `3,543,946.00` | `1.44` | `1.25` | `0.8250` | -666,516.16 USD | `-15.03%` | `5X Cross` |
| `504` | `0xdd53...2b13` | `SHORT` | 4,391,126.64 USD | `3,505,050.00` | `1.42` | `1.25` | `19.31` | 599,840.61 USD | `+13.66%` | `3X Cross` |
| `607` | `0x9946...0852` | `SHORT` | 3,743,440.57 USD | `2,990,580.00` | `1.43` | `1.25` | `1.75` | 520,509.90 USD | `+13.90%` | `20X Cross` |
| `670` | `0xc30c...a4c9` | `SHORT` | 3,412,141.28 USD | `2,727,531.00` | `1.42` | `1.25` | `1.60` | 452,106.91 USD | `+13.25%` | `8X Cross` |
| `693` | `0x9aa5...58af` | `SHORT` | 3,258,228.65 USD | `2,604,083.00` | `1.46` | `1.25` | `4.75` | 539,492.01 USD | `+16.56%` | `20X Cross` |
| `704` | `0xf48f...10fe` | `LONG` | 3,210,046.11 USD | `2,565,779.00` | `1.53` | `1.25` | `1.02` | -714,594.62 USD | `-22.26%` | `4X Cross` |
| `739` | `0x023a...2355` | `SHORT` | 3,089,046.98 USD | `2,469,657.00` | `1.32` | `1.25` | `4.04` | 175,855.17 USD | `+5.69%` | `20X Cross` |
| `745` | `0x45d2...4029` | `SHORT` | 3,069,684.20 USD | `2,453,000.00` | `1.48` | `1.25` | `18.32` | 568,596.22 USD | `+18.52%` | `20X Cross` |
| `1064` | `0xc179...e0c8` | `SHORT` | 2,061,700.83 USD | `1,646,989.00` | `1.30` | `1.25` | `5.26` | 81,333.45 USD | `+3.94%` | `10X Cross` |
| `1082` | `0xeadc...9d55` | `LONG` | 2,024,918.23 USD | `1,619,805.00` | `1.21` | `1.25` | `0.000000` | 66,075.21 USD | `+3.26%` | `20X Cross` |
| `1161` | `0x94b2...599e` | `SHORT` | 1,926,024.07 USD | `1,540,696.00` | `1.36` | `1.25` | `1.86` | 174,442.38 USD | `+9.06%` | `20X Cross` |
| `1173` | `0xbcd4...0dd2` | `SHORT` | 1,913,661.60 USD | `1,529,461.00` | `1.31` | `1.25` | `1.98` | 90,882.99 USD | `+4.75%` | `20X Cross` |
| `1184` | `0x3fc5...c0c1` | `SHORT` | 1,892,596.13 USD | `1,511,779.00` | `1.52` | `1.25` | `2.67` | 399,018.47 USD | `+21.08%` | `20X Cross` |
| `1214` | `0x31ef...f715` | `LONG` | 1,843,702.49 USD | `1,475,080.00` | `1.49` | `1.25` | `1.04` | -355,562.91 USD | `-19.29%` | `3X Isolated` |
| `1267` | `0x7737...bf66` | `SHORT` | 1,766,973.85 USD | `1,413,466.00` | `1.41` | `1.25` | `13.30` | 231,894.80 USD | `+13.12%` | `10X Cross` |
| `1310` | `0xe9d1...d2d3` | `SHORT` | 1,685,976.90 USD | `1,345,767.00` | `1.27` | `1.25` | `2.05` | 22,883.16 USD | `+1.36%` | `10X Cross` |
| `1338` | `0x95da...2328` | `LONG` | 1,656,227.49 USD | `1,324,876.00` | `1.35` | `1.25` | `0.0884` | -137,413.61 USD | `-8.30%` | `5X Cross` |
| `1343` | `0xef96...9383` | `SHORT` | 1,651,245.62 USD | `1,319,097.00` | `1.34` | `1.25` | `4.53` | 116,198.85 USD | `+7.04%` | `20X Cross` |
| `1359` | `0xee2b...d67e` | `LONG` | 1,633,900.03 USD | `1,306,284.00` | `1.55` | `1.25` | `0.3827` | -396,754.87 USD | `-24.28%` | `4X Cross` |
| `1420` | `0x215d...f80a` | `LONG` | 1,564,846.43 USD | `1,251,777.00` | `1.32` | `1.25` | `1.15` | -89,607.80 USD | `-5.73%` | `14X Cross` |
| `1432` | `0x2482...0e55` | `LONG` | 1,550,395.65 USD | `1,239,226.00` | `1.33` | `1.25` | `1.21` | -99,971.40 USD | `-6.45%` | `20X Isolated` |
| `1456` | `0x123d...3bff` | `LONG` | 1,520,619.64 USD | `1,215,329.00` | `1.35` | `1.25` | `0.000000` | -116,449.58 USD | `-7.66%` | `10X Cross` |
| `1472` | `0x5fa3...35b7` | `SHORT` | 1,494,659.98 USD | `1,194,104.00` | `1.31` | `1.25` | `3.36` | 64,713.71 USD | `+4.33%` | `20X Cross` |
| `1504` | `0xdf95...7d72` | `SHORT` | 1,452,007.59 USD | `1,160,492.00` | `1.37` | `1.25` | `35.69` | 141,424.04 USD | `+9.74%` | `20X Cross` |
| `1557` | `0x4537...8732` | `SHORT` | 1,405,045.25 USD | `1,124,576.00` | `1.25` | `1.25` | `2.15` | -1,900.60 USD | `-0.14%` | `10X Cross` |
| `1661` | `0xb1ce...681b` | `LONG` | 1,280,270.29 USD | `1,021,764.00` | `1.49` | `1.25` | `1.16` | -243,786.20 USD | `-19.04%` | `4X Isolated` |
| `1775` | `0x3c36...461a` | `LONG` | 1,175,627.78 USD | `940,051.00` | `1.30` | `1.25` | `1.05` | -43,452.83 USD | `-3.70%` | `10X Cross` |
| `2008` | `0xbfc7...80b4` | `SHORT` | 1,000,080.00 USD | `800,000.00` | `1.48` | `1.25` | `5.67` | 183,374.65 USD | `+18.34%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `1.52` | 1,301.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.30K USD at 1.5200 USD [API] | `2026-09-28 16:26:54` |
| `ANNOUNCEMENT` | `INFO` | `1.52` | 7,742.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.74K USD at 1.5200 USD [API] | `2026-09-28 16:26:54` |
| `ANNOUNCEMENT` | `INFO` | `1.52` | 76.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.5200 USD [API] | `2026-09-28 16:26:54` |
| `ANNOUNCEMENT` | `INFO` | `1.53` | 2,498.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.50K USD at 1.5345 USD [API] | `2026-09-24 16:48:05` |
| `ANNOUNCEMENT` | `INFO` | `1.53` | 5,174.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.17K USD at 1.5345 USD [API] | `2026-09-24 16:48:05` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,315.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.32K USD at 1.3275 USD [API] | `2026-10-28 18:37:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,400.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.40K USD at 1.3263 USD [API] | `2026-10-28 18:40:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,228.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.23K USD at 1.3264 USD [API] | `2026-10-28 18:40:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,973.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.97K USD at 1.3289 USD [API] | `2026-10-28 18:41:59` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,077.07 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.08K USD at 1.3290 USD [API] | `2026-10-28 18:41:55` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,681.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.68K USD at 1.3309 USD [API] | `2026-10-28 18:44:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 11,451.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.45K USD at 1.3309 USD [API] | `2026-10-28 18:44:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 46,926.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 46.93K USD at 1.3306 USD [API] | `2026-10-28 18:50:53` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,005.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.01K USD at 1.3306 USD [API] | `2026-10-28 18:50:53` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,621.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.62K USD at 1.3273 USD [API] | `2026-10-28 18:59:08` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,004.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3277 USD [API] | `2026-10-28 18:58:43` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,004.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3275 USD [API] | `2026-10-28 19:01:57` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,899.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.90K USD at 1.3265 USD [API] | `2026-10-28 19:01:19` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,412.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.41K USD at 1.3087 USD [API] | `2026-10-25 02:05:20` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,486.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.49K USD at 1.3087 USD [API] | `2026-10-25 02:05:20` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,565.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.57K USD at 1.3085 USD [API] | `2026-10-25 02:05:20` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,076.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.08K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 247.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.25K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 3,999.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 9,709.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.71K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 2,644.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.64K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 2,644.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.64K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,880.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.88K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 2,737.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.74K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,546.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.55K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 245.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.25K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,830.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.83K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 693.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.69K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,485.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.49K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 128.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.13K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,492.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.49K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,519.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.52K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,485.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.49K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,555.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.56K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,010.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.01K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,626.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.63K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,674.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.67K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 404.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 245.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.25K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,005.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,876.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.88K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,509.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.51K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,508.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.51K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,425.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.43K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,262.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.26K USD at 1.3355 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,568.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.57K USD at 1.3355 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,783.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.78K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,999.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,997.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.00K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,376.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.38K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,239.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.24K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.39` | 11,492.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 11.49K USD at 1.3865 USD [API] | `2026-10-12 12:37:31` |
| `ANNOUNCEMENT` | `INFO` | `1.39` | 2,086.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.09K USD at 1.3866 USD [API] | `2026-10-12 12:37:31` |
| `ANNOUNCEMENT` | `INFO` | `1.39` | 28,219.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 28.22K USD at 1.3917 USD [API] | `2026-10-08 04:20:41` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.60%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 3,500,000.00 USD, Dist: `+7.93%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 3,400,000.00 USD, Dist: `+7.93%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 4,100,000.00 USD, Dist: `+7.93%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 24,230.00 USD | 73,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 972.02 USD | 73,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,730.00 USD | 73,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 18,290.00 USD | 73,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 103,250.00 USD | 73,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 37,750.00 USD | 72,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 1,560,000.00 USD | 72,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 635.05 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 708.53 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 517.50 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 3,380.00 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 2,260.00 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 503,080.00 USD | 71,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 497.34 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 1,110.00 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 1,210.00 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 7,840.00 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 19,800.00 USD | 70,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 10,340.00 USD | 70,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 179.96 USD | 70,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 1,180.00 USD | 70,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 9,470.00 USD | 70,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 188.87 USD | 70,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 4,360.00 USD | 70,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 6,570.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 1,700.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 3,260.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 2,020.00 USD | 70,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 162,700.00 USD | 70,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,170.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 4,040.00 USD | 70,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 20,150.00 USD | 70,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 36,310.00 USD | 70,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,130.00 USD | 70,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 12,730.00 USD | 70,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 18,960.00 USD | 70,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 7,470.00 USD | 70,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 27,220.00 USD | 70,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 37,010.00 USD | 70,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 2,910.00 USD | 70,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 24,280.00 USD | 70,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 176,640.00 USD | 70,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 78,860.00 USD | 70,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 216,700.00 USD | 70,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 61,790.00 USD | 69,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 117,880.00 USD | 69,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 113,690.00 USD | 69,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 69,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 6,770.00 USD | 69,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 20,130.00 USD | 69,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,250.00 USD | 69,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 12,260.00 USD | 69,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 2,900,000.00 USD | 69,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 35,830.00 USD | 66,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 39,540.00 USD | 66,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 76,610.00 USD | 66,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 44,630.00 USD | 66,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 39,750.00 USD | 66,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 88,910.00 USD | 66,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 384,970.00 USD | 66,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 101,830.00 USD | 65,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 211,390.00 USD | 65,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 73,280.00 USD | 65,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 120,100.00 USD | 65,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 86,160.00 USD | 65,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 64,920.00 USD | 65,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 109,220.00 USD | 65,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,880,000.00 USD | 65,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 151,090.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 458,840.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 93,970.00 USD | 30,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 3,050,000.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 828,610.00 USD | 27,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 150,730.00 USD | 26,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,140,000.00 USD | 26,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 1,290,000.00 USD | 24,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,360,000.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 294,960.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 472,550.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 742,690.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 365,440.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 68,820.00 USD | 19,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 62,410,000.00 USD | 62,410,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 35,830,000.00 USD | 35,830,000.00 USD | 17,310.00 USD | 0.00 USD | 116,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 35,700,000.00 USD | 35,700,000.00 USD | 18,710.00 USD | 937.65 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 62,380,000.00 USD | 62,380,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 493,430.00 USD | 19,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 35,680,000.00 USD | 35,680,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 62,370,000.00 USD | 62,370,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 35,680,000.00 USD | 35,680,000.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 35,660,000.00 USD | 35,660,000.00 USD | 0.00 USD | 47,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 62,290,000.00 USD | 62,290,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 35,610,000.00 USD | 35,610,000.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 62,290,000.00 USD | 62,290,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 35,610,000.00 USD | 35,610,000.00 USD | 0.00 USD | 2,460.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 62,290,000.00 USD | 62,290,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 401,530.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 35,600,000.00 USD | 35,600,000.00 USD | 66,330.00 USD | 27,680.00 USD | 48,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 35,460,000.00 USD | 35,460,000.00 USD | 0.00 USD | 1,660.00 USD | 51,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 62,080,000.00 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 35,400,000.00 USD | 35,400,000.00 USD | 0.00 USD | 107,140.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 61,880,000.00 USD | 61,880,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 61,870,000.00 USD | 61,870,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 35,050,000.00 USD | 35,050,000.00 USD | 53,700.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 61,390,000.00 USD | 61,390,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 202,400.00 USD | 18,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 34,990,000.00 USD | 34,990,000.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 61,150,000.00 USD | 61,150,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 61,050,000.00 USD | 61,050,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 34,850,000.00 USD | 34,850,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 61,040,000.00 USD | 61,040,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 34,790,000.00 USD | 34,790,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 60,970,000.00 USD | 60,970,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 34,720,000.00 USD | 34,720,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 60,850,000.00 USD | 60,850,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 1,770,000.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 60,850,000.00 USD | 60,850,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 34,580,000.00 USD | 34,580,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 60,710,000.00 USD | 60,710,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 60,350,000.00 USD | 60,350,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 34,570,000.00 USD | 34,570,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 60,190,000.00 USD | 60,190,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 34,500,000.00 USD | 34,500,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 59,800,000.00 USD | 59,800,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 320,470.00 USD | 16,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 34,120,000.00 USD | 34,120,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 59,160,000.00 USD | 59,160,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 34,000,000.00 USD | 34,000,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 58,360,000.00 USD | 58,360,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 33,820,000.00 USD | 33,820,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 57,830,000.00 USD | 57,830,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 33,440,000.00 USD | 33,440,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 56,810,000.00 USD | 56,810,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 32,700,000.00 USD | 32,700,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 55,440,000.00 USD | 55,440,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,520,000.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 32,270,000.00 USD | 32,270,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 54,810,000.00 USD | 54,810,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 31,940,000.00 USD | 31,940,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 53,430,000.00 USD | 53,430,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 31,760,000.00 USD | 31,760,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 51,920,000.00 USD | 51,920,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 31,600,000.00 USD | 31,600,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 50,530,000.00 USD | 50,530,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 31,380,000.00 USD | 31,380,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 49,740,000.00 USD | 49,740,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 495,380.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 31,110,000.00 USD | 31,110,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 48,860,000.00 USD | 48,860,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 30,890,000.00 USD | 30,890,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 48,400,000.00 USD | 48,400,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 30,710,000.00 USD | 30,710,000.00 USD | 71,950.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 47,680,000.00 USD | 47,680,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 30,610,000.00 USD | 30,610,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 47,310,000.00 USD | 47,310,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 30,530,000.00 USD | 30,530,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 47,180,000.00 USD | 47,180,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 320,270.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 30,420,000.00 USD | 30,420,000.00 USD | 59,140.00 USD | 145,870.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 46,670,000.00 USD | 46,670,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 30,190,000.00 USD | 30,190,000.00 USD | 189,200.00 USD | 3,790.00 USD | 599,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 45,900,000.00 USD | 45,900,000.00 USD | 182,110.00 USD | 132,500.00 USD | 278,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 29,390,000.00 USD | 29,390,000.00 USD | 10,800.00 USD | 3,540.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 45,300,000.00 USD | 45,300,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 29,360,000.00 USD | 29,360,000.00 USD | 39,850.00 USD | 17,460.00 USD | 92,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 44,610,000.00 USD | 44,610,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 29,210,000.00 USD | 29,210,000.00 USD | 64,160.00 USD | 215,840.00 USD | 69,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 43,950,000.00 USD | 43,950,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 387,750.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 28,860,000.00 USD | 28,860,000.00 USD | 0.00 USD | 2,370.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 43,240,000.00 USD | 43,240,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 28,850,000.00 USD | 28,850,000.00 USD | 66,960.00 USD | 19,950.00 USD | 62,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 42,950,000.00 USD | 42,950,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 28,700,000.00 USD | 28,700,000.00 USD | 169,810.00 USD | 176,190.00 USD | 219,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 41,980,000.00 USD | 41,980,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 28,130,000.00 USD | 28,130,000.00 USD | 70,990.00 USD | 80,650.00 USD | 188,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 41,500,000.00 USD | 41,500,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 27,790,000.00 USD | 27,790,000.00 USD | 35,480.00 USD | 106,230.00 USD | 195,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 40,610,000.00 USD | 40,610,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 1,490,000.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 27,460,000.00 USD | 27,460,000.00 USD | 0.00 USD | 193,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 40,520,000.00 USD | 40,520,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 27,260,000.00 USD | 27,260,000.00 USD | 81,900.00 USD | 99,520.00 USD | 415,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 40,420,000.00 USD | 40,420,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 26,660,000.00 USD | 26,660,000.00 USD | 320,140.00 USD | 244,960.00 USD | 91,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 38,870,000.00 USD | 38,870,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 26,010,000.00 USD | 26,010,000.00 USD | 419,060.00 USD | 334,050.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 37,630,000.00 USD | 37,630,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 24,020,000.00 USD | 24,020,000.00 USD | 9,150.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 37,220,000.00 USD | 37,220,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 11,710,000.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 24,000,000.00 USD | 24,000,000.00 USD | 117,720.00 USD | 0.00 USD | 122,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 37,050,000.00 USD | 37,050,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 23,760,000.00 USD | 23,760,000.00 USD | 174,270.00 USD | 380,580.00 USD | 135,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 36,490,000.00 USD | 36,490,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 23,070,000.00 USD | 23,070,000.00 USD | 157,550.00 USD | 9,600.00 USD | 208,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 36,190,000.00 USD | 36,190,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 22,700,000.00 USD | 22,700,000.00 USD | 0.00 USD | 5,120.00 USD | 55,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 35,690,000.00 USD | 35,690,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 22,640,000.00 USD | 22,640,000.00 USD | 173,990.00 USD | 530,550.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 34,440,000.00 USD | 34,440,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 453,880.00 USD | 688,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 20,450,000.00 USD | 20,450,000.00 USD | 788,770.00 USD | 500,530.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 31,560,000.00 USD | 31,560,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 17,650,000.00 USD | 17,650,000.00 USD | 190,540.00 USD | 9,950.00 USD | 258,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 31,100,000.00 USD | 31,100,000.00 USD | 0.00 USD | 1,110,000.00 USD | 995,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 17,190,000.00 USD | 17,190,000.00 USD | 200,000.00 USD | 623,370.00 USD | 551,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 29,000,000.00 USD | 29,000,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 15,820,000.00 USD | 15,820,000.00 USD | 435,700.00 USD | 821,750.00 USD | 831,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 27,720,000.00 USD | 27,720,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 13,730,000.00 USD | 13,730,000.00 USD | 318,380.00 USD | 134,700.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 25,970,000.00 USD | 25,970,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 234,750.00 USD | 234,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 13,260,000.00 USD | 13,260,000.00 USD | 405,830.00 USD | 298,200.00 USD | 227,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 23,910,000.00 USD | 23,910,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 12,330,000.00 USD | 12,330,000.00 USD | 663,280.00 USD | 1,240,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 17,960,000.00 USD | 17,960,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 9,380,000.00 USD | 9,380,000.00 USD | 266,660.00 USD | 0.00 USD | 857,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 14,550,000.00 USD | 14,550,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 8,260,000.00 USD | 8,260,000.00 USD | 112,970.00 USD | 774,420.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 10,410,000.00 USD | 10,410,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 6,120,000.00 USD | 6,120,000.00 USD | 1,050,000.00 USD | 116,230.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 8,500,000.00 USD | 8,500,000.00 USD | 3,440,000.00 USD | 923,130.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 2,610,000.00 USD | 2,610,000.00 USD | 1,330,000.00 USD | 351,240.00 USD | 551,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,470,000.00 USD | 2,470,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 381,120.00 USD | 381,120.00 USD | 381,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 140,880.00 USD | 140,880.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 180,020.00 USD | 180,020.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 360,040.00 USD | 360,040.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 4,230.00 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 8,460.00 USD | 8,460.00 USD | 0.00 USD | 0.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 500,700.00 USD | 500,700.00 USD | 74,170.00 USD | 0.00 USD | 66,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 176,980.00 USD | 176,980.00 USD | 168,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 691,470.00 USD | 691,470.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 1,610,000.00 USD | 1,610,000.00 USD | 1,430,000.00 USD | 2,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 798,620.00 USD | 798,620.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,270,000.00 USD | 2,270,000.00 USD | 384,710.00 USD | 68,210.00 USD | 202,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 4,240,000.00 USD | 4,240,000.00 USD | 424,010.00 USD | 0.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 7,310,000.00 USD | 7,310,000.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 8,180,000.00 USD | 8,180,000.00 USD | 663,280.00 USD | 1,020,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 14,240,000.00 USD | 14,240,000.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 4,420.00 USD | 4,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 10,110,000.00 USD | 10,110,000.00 USD | 306,520.00 USD | 1,030,000.00 USD | 599,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 27,480,000.00 USD | 27,480,000.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 2,050,000.00 USD | 794,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 32,250,000.00 USD | 32,250,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 15,850,000.00 USD | 15,850,000.00 USD | 327,600.00 USD | 899,410.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 35,860,000.00 USD | 35,860,000.00 USD | 943,110.00 USD | 2,540,000.00 USD | 123,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 17,930,000.00 USD | 17,930,000.00 USD | 1,430,000.00 USD | 588,250.00 USD | 64,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 40,620,000.00 USD | 40,620,000.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 21,660,000.00 USD | 21,660,000.00 USD | 465,090.00 USD | 1,250,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 57,060,000.00 USD | 57,060,000.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 5,770.00 USD | 10,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 28,030,000.00 USD | 28,030,000.00 USD | 817,960.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 75,330,000.00 USD | 75,330,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 41,510,000.00 USD | 41,510,000.00 USD | 6,020,000.00 USD | 2,730,000.00 USD | 4,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 81,620,000.00 USD | 81,620,000.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 44,420,000.00 USD | 44,420,000.00 USD | 197,050.00 USD | 2,010,000.00 USD | 703,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 82,580,000.00 USD | 82,580,000.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 46,430,000.00 USD | 46,430,000.00 USD | 710,910.00 USD | 64,340.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 84,590,000.00 USD | 84,590,000.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 48,630,000.00 USD | 48,630,000.00 USD | 905,740.00 USD | 418,710.00 USD | 869,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 88,180,000.00 USD | 88,180,000.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 10,130.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 50,780,000.00 USD | 50,780,000.00 USD | 441,010.00 USD | 687,930.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 89,350,000.00 USD | 89,350,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 51,780,000.00 USD | 51,780,000.00 USD | 584,100.00 USD | 411,690.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 89,470,000.00 USD | 89,470,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 51,810,000.00 USD | 51,810,000.00 USD | 18,290.00 USD | 3,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 91,550,000.00 USD | 91,550,000.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 53,590,000.00 USD | 53,590,000.00 USD | 369,880.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 91,970,000.00 USD | 91,970,000.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 57,540,000.00 USD | 57,540,000.00 USD | 1,110,000.00 USD | 305,230.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 101,610,000.00 USD | 101,610,000.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 11,500.00 USD | 31,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 62,440,000.00 USD | 62,440,000.00 USD | 1,400,000.00 USD | 1,130,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 102,840,000.00 USD | 102,840,000.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 63,320,000.00 USD | 63,320,000.00 USD | 411,640.00 USD | 20,370.00 USD | 446,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 104,900,000.00 USD | 104,900,000.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 64,570,000.00 USD | 64,570,000.00 USD | 169,810.00 USD | 344,440.00 USD | 730,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 106,570,000.00 USD | 106,570,000.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 67,030,000.00 USD | 67,030,000.00 USD | 673,010.00 USD | 945,470.00 USD | 848,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 109,660,000.00 USD | 109,660,000.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 67,750,000.00 USD | 67,750,000.00 USD | 192,870.00 USD | 204,330.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 109,670,000.00 USD | 109,670,000.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 11,730.00 USD | 43,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 69,070,000.00 USD | 69,070,000.00 USD | 493,480.00 USD | 507,360.00 USD | 320,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 112,670,000.00 USD | 112,670,000.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 72,180,000.00 USD | 72,180,000.00 USD | 849,240.00 USD | 310,710.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 117,130,000.00 USD | 117,130,000.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 74,970,000.00 USD | 74,970,000.00 USD | 1,090,000.00 USD | 396,100.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 120,390,000.00 USD | 120,390,000.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 78,290,000.00 USD | 78,290,000.00 USD | 1,800,000.00 USD | 778,210.00 USD | 745,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 123,230,000.00 USD | 123,230,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 80,000,000.00 USD | 80,000,000.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 125,690,000.00 USD | 125,690,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 4,910.00 USD | 48,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 85,600,000.00 USD | 85,600,000.00 USD | 222,150.00 USD | 1,620,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 130,320,000.00 USD | 130,320,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 92,400,000.00 USD | 92,400,000.00 USD | 2,080,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 133,400,000.00 USD | 133,400,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 95,650,000.00 USD | 95,650,000.00 USD | 1,680,000.00 USD | 546,460.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 135,230,000.00 USD | 135,230,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,290,000.00 USD | 100,290,000.00 USD | 1,870,000.00 USD | 845,300.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 139,680,000.00 USD | 139,680,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 103,340,000.00 USD | 103,340,000.00 USD | 1,770,000.00 USD | 259,620.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,050,000.00 USD | 142,050,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 56,840.00 USD | 105,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 105,630,000.00 USD | 105,630,000.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 142,590,000.00 USD | 142,590,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 107,820,000.00 USD | 107,820,000.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 143,740,000.00 USD | 143,740,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 110,260,000.00 USD | 110,260,000.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 145,460,000.00 USD | 145,460,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 112,520,000.00 USD | 112,520,000.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 149,520,000.00 USD | 149,520,000.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 114,840,000.00 USD | 114,840,000.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 150,060,000.00 USD | 150,060,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 3,240.00 USD | 108,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 117,290,000.00 USD | 117,290,000.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 152,010,000.00 USD | 152,010,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 119,970,000.00 USD | 119,970,000.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 154,350,000.00 USD | 154,350,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 122,370,000.00 USD | 122,370,000.00 USD | 1,020,000.00 USD | 302,930.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 159,060,000.00 USD | 159,060,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 125,300,000.00 USD | 125,300,000.00 USD | 1,330,000.00 USD | 669,200.00 USD | 930,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 164,710,000.00 USD | 164,710,000.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 127,850,000.00 USD | 127,850,000.00 USD | 946,370.00 USD | 626,040.00 USD | 979,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 175,670,000.00 USD | 175,670,000.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 2,240.00 USD | 110,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 129,020,000.00 USD | 129,020,000.00 USD | 498,430.00 USD | 189,010.00 USD | 481,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 182,780,000.00 USD | 182,780,000.00 USD | 2,410,000.00 USD | 2,230,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 130,280,000.00 USD | 130,280,000.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 193,090,000.00 USD | 193,090,000.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 131,770,000.00 USD | 131,770,000.00 USD | 768,810.00 USD | 229,320.00 USD | 486,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 200,860,000.00 USD | 200,860,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 133,090,000.00 USD | 133,090,000.00 USD | 554,870.00 USD | 207,050.00 USD | 556,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 209,190,000.00 USD | 209,190,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 134,420,000.00 USD | 134,420,000.00 USD | 493,530.00 USD | 170,640.00 USD | 668,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 217,420,000.00 USD | 217,420,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 8,910.00 USD | 119,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 135,330,000.00 USD | 135,330,000.00 USD | 351,630.00 USD | 92,050.00 USD | 468,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 221,510,000.00 USD | 221,510,000.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 135,830,000.00 USD | 135,830,000.00 USD | 148,530.00 USD | 41,890.00 USD | 312,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 225,300,000.00 USD | 225,300,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 136,380,000.00 USD | 136,380,000.00 USD | 266,880.00 USD | 47,170.00 USD | 233,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 227,440,000.00 USD | 227,440,000.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 137,050,000.00 USD | 137,050,000.00 USD | 241,460.00 USD | 104,340.00 USD | 321,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 231,530,000.00 USD | 231,530,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 137,190,000.00 USD | 137,190,000.00 USD | 80,160.00 USD | 27,780.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 233,250,000.00 USD | 233,250,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 261,140.00 USD | 380,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 137,380,000.00 USD | 137,380,000.00 USD | 53,740.00 USD | 0.00 USD | 138,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 233,740,000.00 USD | 233,740,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 137,610,000.00 USD | 137,610,000.00 USD | 84,710.00 USD | 105,400.00 USD | 44,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 235,160,000.00 USD | 235,160,000.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 137,790,000.00 USD | 137,790,000.00 USD | 38,340.00 USD | 26,490.00 USD | 110,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 236,320,000.00 USD | 236,320,000.00 USD | 334,560.00 USD | 372,470.00 USD | 461,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 137,930,000.00 USD | 137,930,000.00 USD | 3,890.00 USD | 42,450.00 USD | 93,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 238,870,000.00 USD | 238,870,000.00 USD | 870,810.00 USD | 406,050.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 138,080,000.00 USD | 138,080,000.00 USD | 74,330.00 USD | 2,720.00 USD | 77,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 240,680,000.00 USD | 240,680,000.00 USD | 536,130.00 USD | 295,850.00 USD | 969,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 138,480,000.00 USD | 138,480,000.00 USD | 169,050.00 USD | 60,310.00 USD | 169,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 242,230,000.00 USD | 242,230,000.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 139,030,000.00 USD | 139,030,000.00 USD | 228,570.00 USD | 72,280.00 USD | 246,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 244,370,000.00 USD | 244,370,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 139,450,000.00 USD | 139,450,000.00 USD | 158,070.00 USD | 75,630.00 USD | 183,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 246,910,000.00 USD | 246,910,000.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 139,530,000.00 USD | 139,530,000.00 USD | 0.00 USD | 65,520.00 USD | 20,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 248,000,000.00 USD | 248,000,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 139,700,000.00 USD | 139,700,000.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 249,290,000.00 USD | 249,290,000.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 382,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,760,000.00 USD | 139,760,000.00 USD | 53,700.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 249,830,000.00 USD | 249,830,000.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,900,000.00 USD | 139,900,000.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 250,930,000.00 USD | 250,930,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,100,000.00 USD | 251,100,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,900,000.00 USD | 139,900,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,420,000.00 USD | 251,420,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,960,000.00 USD | 139,960,000.00 USD | 22,630.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 139,980,000.00 USD | 139,980,000.00 USD | 21,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 251,590,000.00 USD | 251,590,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 4,180.00 USD | 386,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 251,710,000.00 USD | 251,710,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 251,720,000.00 USD | 251,720,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 251,860,000.00 USD | 251,860,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 251,970,000.00 USD | 251,970,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 252,220,000.00 USD | 252,220,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 795.23 USD | 387,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 252,380,000.00 USD | 252,380,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 252,760,000.00 USD | 252,760,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 253,410,000.00 USD | 253,410,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 253,580,000.00 USD | 253,580,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 254,210,000.00 USD | 254,210,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,600.00 USD | 390,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 254,730,000.00 USD | 254,730,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 255,750,000.00 USD | 255,750,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 257,130,000.00 USD | 257,130,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 257,760,000.00 USD | 257,760,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 258,120,000.00 USD | 258,120,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,610.00 USD | 484,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 259,140,000.00 USD | 259,140,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 260,640,000.00 USD | 260,640,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 262,030,000.00 USD | 262,030,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 262,830,000.00 USD | 262,830,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 263,360,000.00 USD | 263,360,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 258.30 USD | 484,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 263,710,000.00 USD | 263,710,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 264,170,000.00 USD | 264,170,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 264,880,000.00 USD | 264,880,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 265,260,000.00 USD | 265,260,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 265,390,000.00 USD | 265,390,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 265,510,000.00 USD | 265,510,000.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 265,840,000.00 USD | 265,840,000.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 266,450,000.00 USD | 266,450,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 267,020,000.00 USD | 267,020,000.00 USD | 182,110.00 USD | 128,180.00 USD | 251,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 267,480,000.00 USD | 267,480,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 1,590.00 USD | 486,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.46` | 267,630,000.00 USD | 267,630,000.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 268,110,000.00 USD | 268,110,000.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 268,320,000.00 USD | 268,320,000.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.47` | 697,740.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 18,070.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 128,990.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 915.06 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 776.71 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 2,130.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 6,800.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 123.63 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 129,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 117.16 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 108.21 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 4,430,000.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 3,800.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 2,170.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 1,160.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 3,960.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 5,250,000.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 7,340.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 351.45 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 2,850.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 747.78 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 2,020.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 128.45 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,880,000.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 113,220.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 552.45 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 794.73 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 309,300.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 8,870.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 3,320.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,680.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 119.10 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 401,000.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 1,290.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 2,010.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 5,960,000.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 460.50 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 1,200.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 2,680,000.00 USD | 23,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 23,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 247,230.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 1,390.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 3,000.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 301.53 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.94 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 873.18 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 2,750.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 75,280.00 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 205.62 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 103.27 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 103.73 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 208.38 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 44,140.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 459.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 2,860.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 11,850.00 USD | 24,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,540.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 144.77 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 222.77 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 108.79 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 56,430.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 225,350.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 155.68 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 481.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 27,800.00 USD | 24,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 18,830.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 2,840.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 94,260.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 337.96 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 4,370.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 73,050,000.00 USD | 0.00 USD | 24,230.00 USD | `-79.67%` | `95,000.00` |
| `Live` | `Long` | `0.2650` | 73,030,000.00 USD | 0.00 USD | 972.02 USD | `-78.87%` | `3,668.00` |
| `Live` | `Long` | `0.2750` | 73,030,000.00 USD | 0.00 USD | 1,730.00 USD | `-78.07%` | `6,284.00` |
| `Live` | `Long` | `0.2850` | 73,020,000.00 USD | 0.00 USD | 18,290.00 USD | `-77.27%` | `64,190.00` |
| `Live` | `Long` | `0.2950` | 73,010,000.00 USD | 0.00 USD | 103,250.00 USD | `-76.48%` | `350,000.00` |
| `Live` | `Long` | `0.3050` | 72,900,000.00 USD | 0.00 USD | 37,750.00 USD | `-75.68%` | `123,760.00` |
| `Live` | `Long` | `0.3150` | 72,860,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-74.88%` | `4,960,402.00` |
| `Live` | `Long` | `0.3250` | 71,300,000.00 USD | 0.00 USD | 635.05 USD | `-74.09%` | `1,954.00` |
| `Live` | `Long` | `0.3350` | 71,300,000.00 USD | 0.00 USD | 708.53 USD | `-73.29%` | `2,115.00` |
| `Live` | `Long` | `0.3450` | 71,300,000.00 USD | 0.00 USD | 517.50 USD | `-72.49%` | `1,500.00` |
| `Live` | `Long` | `0.3550` | 71,300,000.00 USD | 0.00 USD | 3,380.00 USD | `-71.69%` | `9,515.00` |
| `Live` | `Long` | `0.3650` | 71,300,000.00 USD | 0.00 USD | 2,260.00 USD | `-70.90%` | `6,200.00` |
| `Live` | `Long` | `0.3850` | 71,290,000.00 USD | 0.00 USD | 503,080.00 USD | `-69.30%` | `1,306,697.00` |
| `Live` | `Long` | `0.3950` | 70,790,000.00 USD | 0.00 USD | 174.59 USD | `-68.50%` | `442.00` |
| `Live` | `Long` | `0.4050` | 70,790,000.00 USD | 0.00 USD | 497.34 USD | `-67.71%` | `1,228.00` |
| `Live` | `Long` | `0.4150` | 70,790,000.00 USD | 0.00 USD | 1,110.00 USD | `-66.91%` | `2,686.00` |
| `Live` | `Long` | `0.4250` | 70,790,000.00 USD | 0.00 USD | 1,210.00 USD | `-66.11%` | `2,847.00` |
| `Live` | `Long` | `0.4350` | 70,790,000.00 USD | 0.00 USD | 7,840.00 USD | `-65.31%` | `18,023.00` |
| `Live` | `Long` | `0.4450` | 70,780,000.00 USD | 0.00 USD | 19,800.00 USD | `-64.52%` | `44,484.00` |
| `Live` | `Long` | `0.4550` | 70,760,000.00 USD | 0.00 USD | 10,340.00 USD | `-63.72%` | `22,719.00` |
| `Live` | `Long` | `0.4650` | 70,750,000.00 USD | 0.00 USD | 179.96 USD | `-62.92%` | `387.00` |
| `Live` | `Long` | `0.4750` | 70,750,000.00 USD | 0.00 USD | 1,180.00 USD | `-62.12%` | `2,475.00` |
| `Live` | `Long` | `0.4850` | 70,750,000.00 USD | 0.00 USD | 9,470.00 USD | `-61.33%` | `19,518.00` |
| `Live` | `Long` | `0.5050` | 70,740,000.00 USD | 0.00 USD | 188.87 USD | `-59.73%` | `374.00` |
| `Live` | `Long` | `0.5150` | 70,740,000.00 USD | 0.00 USD | 4,360.00 USD | `-58.93%` | `8,470.00` |
| `Live` | `Long` | `0.5250` | 70,730,000.00 USD | 0.00 USD | 6,570.00 USD | `-58.14%` | `12,505.00` |
| `Live` | `Long` | `0.5350` | 70,730,000.00 USD | 0.00 USD | 1,700.00 USD | `-57.34%` | `3,171.00` |
| `Live` | `Long` | `0.5450` | 70,730,000.00 USD | 0.00 USD | 3,260.00 USD | `-56.54%` | `5,989.00` |
| `Live` | `Long` | `0.5550` | 70,720,000.00 USD | 0.00 USD | 2,020.00 USD | `-55.75%` | `3,644.00` |
| `Live` | `Long` | `0.5650` | 70,720,000.00 USD | 0.00 USD | 162,700.00 USD | `-54.95%` | `287,957.00` |
| `Live` | `Long` | `0.5750` | 70,560,000.00 USD | 0.00 USD | 8,170.00 USD | `-54.15%` | `14,208.00` |
| `Live` | `Long` | `0.5950` | 70,550,000.00 USD | 0.00 USD | 4,040.00 USD | `-52.56%` | `6,788.00` |
| `Live` | `Long` | `0.6050` | 70,550,000.00 USD | 0.00 USD | 20,150.00 USD | `-51.76%` | `33,298.00` |
| `Live` | `Long` | `0.6150` | 70,530,000.00 USD | 0.00 USD | 36,310.00 USD | `-50.96%` | `59,041.00` |
| `Live` | `Long` | `0.6250` | 70,490,000.00 USD | 0.00 USD | 1,130.00 USD | `-50.16%` | `1,803.00` |
| `Live` | `Long` | `0.6350` | 70,490,000.00 USD | 0.00 USD | 12,730.00 USD | `-49.37%` | `20,044.00` |
| `Live` | `Long` | `0.6450` | 70,480,000.00 USD | 0.00 USD | 18,960.00 USD | `-48.57%` | `29,393.00` |
| `Live` | `Long` | `0.6550` | 70,460,000.00 USD | 0.00 USD | 7,470.00 USD | `-47.77%` | `11,401.00` |
| `Live` | `Long` | `0.6650` | 70,450,000.00 USD | 0.00 USD | 27,220.00 USD | `-46.97%` | `40,929.00` |
| `Live` | `Long` | `0.6750` | 70,420,000.00 USD | 0.00 USD | 37,010.00 USD | `-46.18%` | `54,836.00` |
| `Live` | `Long` | `0.6850` | 70,390,000.00 USD | 0.00 USD | 2,910.00 USD | `-45.38%` | `4,255.00` |
| `Live` | `Long` | `0.6950` | 70,380,000.00 USD | 0.00 USD | 24,280.00 USD | `-44.58%` | `34,940.00` |
| `Live` | `Long` | `0.7050` | 70,360,000.00 USD | 0.00 USD | 176,640.00 USD | `-43.78%` | `250,556.00` |
| `Live` | `Long` | `0.7150` | 70,180,000.00 USD | 0.00 USD | 78,860.00 USD | `-42.99%` | `110,288.00` |
| `Live` | `Long` | `0.7250` | 70,100,000.00 USD | 0.00 USD | 216,700.00 USD | `-42.19%` | `298,897.00` |
| `Live` | `Long` | `0.7350` | 69,890,000.00 USD | 0.00 USD | 61,790.00 USD | `-41.39%` | `84,072.00` |
| `Live` | `Long` | `0.7450` | 69,820,000.00 USD | 0.00 USD | 117,880.00 USD | `-40.60%` | `158,223.00` |
| `Live` | `Long` | `0.7550` | 69,710,000.00 USD | 0.00 USD | 113,690.00 USD | `-39.80%` | `150,580.00` |
| `Live` | `Long` | `0.7650` | 69,590,000.00 USD | 0.00 USD | 2,190.00 USD | `-39.00%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 69,590,000.00 USD | 0.00 USD | 6,770.00 USD | `-38.20%` | `8,730.00` |
| `Live` | `Long` | `0.7850` | 69,580,000.00 USD | 0.00 USD | 20,130.00 USD | `-37.41%` | `25,638.00` |
| `Live` | `Long` | `0.7950` | 69,560,000.00 USD | 0.00 USD | 11,250.00 USD | `-36.61%` | `14,145.00` |
| `Live` | `Long` | `0.8050` | 69,550,000.00 USD | 0.00 USD | 12,260.00 USD | `-35.81%` | `15,233.00` |
| `Live` | `Long` | `0.8150` | 69,540,000.00 USD | 0.00 USD | 2,900,000.00 USD | `-35.01%` | `3,558,215.00` |
| `Live` | `Long` | `0.8250` | 66,640,000.00 USD | 0.00 USD | 35,830.00 USD | `-34.22%` | `43,435.00` |
| `Live` | `Long` | `0.8350` | 66,600,000.00 USD | 0.00 USD | 39,540.00 USD | `-33.42%` | `47,355.00` |
| `Live` | `Long` | `0.8450` | 66,560,000.00 USD | 0.00 USD | 76,610.00 USD | `-32.62%` | `90,665.00` |
| `Live` | `Long` | `0.8550` | 66,490,000.00 USD | 0.00 USD | 44,630.00 USD | `-31.82%` | `52,196.00` |
| `Live` | `Long` | `0.8650` | 66,440,000.00 USD | 0.00 USD | 39,750.00 USD | `-31.03%` | `45,955.00` |
| `Live` | `Long` | `0.8750` | 66,400,000.00 USD | 0.00 USD | 88,910.00 USD | `-30.23%` | `101,615.00` |
| `Live` | `Long` | `0.8850` | 66,310,000.00 USD | 0.00 USD | 384,970.00 USD | `-29.43%` | `434,990.00` |
| `Live` | `Long` | `0.8950` | 65,930,000.00 USD | 0.00 USD | 101,830.00 USD | `-28.63%` | `113,780.00` |
| `Live` | `Long` | `0.9050` | 65,830,000.00 USD | 0.00 USD | 211,390.00 USD | `-27.84%` | `233,581.00` |
| `Live` | `Long` | `0.9150` | 65,620,000.00 USD | 0.00 USD | 73,280.00 USD | `-27.04%` | `80,086.00` |
| `Live` | `Long` | `0.9250` | 65,540,000.00 USD | 0.00 USD | 120,100.00 USD | `-26.24%` | `129,843.00` |
| `Live` | `Long` | `0.9350` | 65,420,000.00 USD | 0.00 USD | 86,160.00 USD | `-25.44%` | `92,148.00` |
| `Live` | `Long` | `0.9450` | 65,340,000.00 USD | 0.00 USD | 64,920.00 USD | `-24.65%` | `68,694.00` |
| `Live` | `Long` | `0.9550` | 65,270,000.00 USD | 0.00 USD | 109,220.00 USD | `-23.85%` | `114,369.00` |
| `Live` | `Long` | `0.9650` | 65,160,000.00 USD | 0.00 USD | 33,880,000.00 USD | `-23.05%` | `35,110,024.00` |
| `Live` | `Long` | `0.9750` | 31,280,000.00 USD | 0.00 USD | 151,090.00 USD | `-22.26%` | `154,965.00` |
| `Live` | `Long` | `0.9850` | 31,130,000.00 USD | 0.00 USD | 458,840.00 USD | `-21.46%` | `465,827.00` |
| `Live` | `Long` | `0.9950` | 30,670,000.00 USD | 0.00 USD | 93,970.00 USD | `-20.66%` | `94,439.00` |
| `Live` | `Long` | `1.00` | 30,580,000.00 USD | 0.00 USD | 3,050,000.00 USD | `-19.86%` | `3,039,105.00` |
| `Live` | `Long` | `1.01` | 27,520,000.00 USD | 0.00 USD | 828,610.00 USD | `-19.07%` | `816,367.00` |
| `Live` | `Long` | `1.02` | 26,690,000.00 USD | 0.00 USD | 150,730.00 USD | `-18.27%` | `147,055.00` |
| `Live` | `Long` | `1.03` | 26,540,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-17.47%` | `2,064,373.00` |
| `Live` | `Long` | `1.04` | 24,410,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-16.67%` | `1,235,312.00` |
| `Live` | `Long` | `1.05` | 23,120,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-15.88%` | `1,292,575.00` |
| `Live` | `Long` | `1.06` | 21,750,000.00 USD | 0.00 USD | 294,960.00 USD | `-15.08%` | `276,957.00` |
| `Live` | `Long` | `1.07` | 21,460,000.00 USD | 0.00 USD | 472,550.00 USD | `-14.28%` | `439,578.00` |
| `Live` | `Long` | `1.08` | 20,990,000.00 USD | 0.00 USD | 742,690.00 USD | `-13.48%` | `684,506.00` |
| `Live` | `Long` | `1.09` | 20,240,000.00 USD | 0.00 USD | 365,440.00 USD | `-12.69%` | `333,731.00` |
| `Live` | `Long` | `1.10` | 19,880,000.00 USD | 0.00 USD | 68,820.00 USD | `-11.89%` | `62,279.00` |
| `Live` | `Long` | `1.11` | 19,810,000.00 USD | 0.00 USD | 493,430.00 USD | `-11.09%` | `442,537.00` |
| `Live` | `Long` | `1.12` | 19,320,000.00 USD | 0.00 USD | 401,530.00 USD | `-10.29%` | `356,917.00` |
| `Live` | `Long` | `1.14` | 18,910,000.00 USD | 0.00 USD | 202,400.00 USD | `-9.50%` | `178,323.00` |
| `Live` | `Long` | `1.15` | 18,710,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-8.70%` | `1,549,998.00` |
| `Live` | `Long` | `1.16` | 16,940,000.00 USD | 0.00 USD | 320,470.00 USD | `-7.90%` | `277,465.00` |
| `Live` | `Long` | `1.17` | 16,620,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-7.11%` | `1,308,732.00` |
| `Live` | `Long` | `1.18` | 15,090,000.00 USD | 0.00 USD | 495,380.00 USD | `-6.31%` | `421,600.00` |
| `Live` | `Long` | `1.19` | 14,600,000.00 USD | 0.00 USD | 320,270.00 USD | `-5.51%` | `270,266.00` |
| `Live` | `Long` | `1.20` | 14,280,000.00 USD | 0.00 USD | 387,750.00 USD | `-4.71%` | `324,474.00` |
| `Live` | `Long` | `1.21` | 13,890,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-3.92%` | `1,239,522.00` |
| `Live` | `Long` | `1.22` | 12,390,000.00 USD | 0.00 USD | 11,710,000.00 USD | `-3.12%` | `9,634,308.00` |
| `Live` | `Long` | `1.23` | 688,620.00 USD | 0.00 USD | 453,880.00 USD | `-2.32%` | `370,511.00` |
| `Live` | `Long` | `1.24` | 234,750.00 USD | 0.00 USD | 234,750.00 USD | `-1.52%` | `190,080.00` |
| `Live` | `Short` | `1.26` | 4,420.00 USD | 4,420.00 USD | 0.00 USD | `+0.87%` | `3,491.00` |
| `Live` | `Short` | `1.27` | 10,180.00 USD | 5,770.00 USD | 0.00 USD | `+1.67%` | `4,524.00` |
| `Live` | `Short` | `1.28` | 20,320.00 USD | 10,130.00 USD | 0.00 USD | `+2.46%` | `7,885.00` |
| `Live` | `Short` | `1.29` | 31,820.00 USD | 11,500.00 USD | 0.00 USD | `+3.26%` | `8,880.00` |
| `Live` | `Short` | `1.30` | 43,550.00 USD | 11,730.00 USD | 0.00 USD | `+4.06%` | `8,988.00` |
| `Live` | `Short` | `1.31` | 48,450.00 USD | 4,910.00 USD | 0.00 USD | `+4.86%` | `3,732.00` |
| `Live` | `Short` | `1.32` | 105,290.00 USD | 56,840.00 USD | 0.00 USD | `+5.65%` | `42,899.00` |
| `Live` | `Short` | `1.33` | 108,540.00 USD | 3,240.00 USD | 0.00 USD | `+6.45%` | `2,428.00` |
| `Live` | `Short` | `1.34` | 110,780.00 USD | 2,240.00 USD | 0.00 USD | `+7.25%` | `1,669.00` |
| `Live` | `Short` | `1.35` | 119,690.00 USD | 8,910.00 USD | 0.00 USD | `+8.05%` | `6,577.00` |
| `Live` | `Short` | `1.36` | 380,840.00 USD | 261,140.00 USD | 0.00 USD | `+8.84%` | `191,314.00` |
| `Live` | `Short` | `1.39` | 382,110.00 USD | 1,280.00 USD | 0.00 USD | `+10.44%` | `921.00` |
| `Live` | `Short` | `1.40` | 386,300.00 USD | 4,180.00 USD | 0.00 USD | `+11.23%` | `3,000.00` |
| `Live` | `Short` | `1.41` | 387,090.00 USD | 795.23 USD | 0.00 USD | `+12.03%` | `566.00` |
| `Live` | `Short` | `1.42` | 390,690.00 USD | 3,600.00 USD | 0.00 USD | `+12.83%` | `2,544.00` |
| `Live` | `Short` | `1.43` | 484,300.00 USD | 93,610.00 USD | 0.00 USD | `+13.63%` | `65,689.00` |
| `Live` | `Short` | `1.44` | 484,560.00 USD | 258.30 USD | 0.00 USD | `+14.42%` | `180.00` |
| `Live` | `Short` | `1.46` | 486,140.00 USD | 1,590.00 USD | 0.00 USD | `+16.02%` | `1,090.00` |
| `Live` | `Short` | `1.47` | 1,180,000.00 USD | 697,740.00 USD | 0.00 USD | `+16.82%` | `476,270.00` |
| `Live` | `Short` | `1.48` | 1,200,000.00 USD | 18,070.00 USD | 0.00 USD | `+17.61%` | `12,249.00` |
| `Live` | `Short` | `1.49` | 1,330,000.00 USD | 128,990.00 USD | 0.00 USD | `+18.41%` | `86,861.00` |
| `Live` | `Short` | `1.50` | 1,340,000.00 USD | 11,950.00 USD | 0.00 USD | `+19.21%` | `7,994.00` |
| `Live` | `Short` | `1.51` | 1,340,000.00 USD | 915.06 USD | 0.00 USD | `+20.80%` | `604.00` |
| `Live` | `Short` | `1.53` | 1,340,000.00 USD | 776.71 USD | 0.00 USD | `+22.40%` | `506.00` |
| `Live` | `Short` | `1.54` | 1,350,000.00 USD | 2,130.00 USD | 0.00 USD | `+23.20%` | `1,377.00` |
| `Live` | `Short` | `1.55` | 1,350,000.00 USD | 6,800.00 USD | 0.00 USD | `+23.99%` | `4,373.00` |
| `Live` | `Short` | `1.56` | 1,350,000.00 USD | 555.57 USD | 0.00 USD | `+24.79%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,360,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.59%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,360,000.00 USD | 123.63 USD | 0.00 USD | `+26.38%` | `78.00` |
| `Live` | `Short` | `1.59` | 1,490,000.00 USD | 129,530.00 USD | 0.00 USD | `+27.18%` | `81,210.00` |
| `Live` | `Short` | `1.60` | 1,490,000.00 USD | 117.16 USD | 0.00 USD | `+27.98%` | `73.00` |
| `Live` | `Short` | `1.61` | 1,490,000.00 USD | 108.21 USD | 0.00 USD | `+28.78%` | `67.00` |
| `Live` | `Short` | `1.62` | 5,920,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+29.57%` | `2,727,698.00` |
| `Live` | `Short` | `1.64` | 5,920,000.00 USD | 3,800.00 USD | 0.00 USD | `+30.37%` | `2,326.00` |
| `Live` | `Short` | `1.66` | 5,920,000.00 USD | 147.30 USD | 0.00 USD | `+31.97%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,920,000.00 USD | 586.08 USD | 0.00 USD | `+32.76%` | `352.00` |
| `Live` | `Short` | `1.68` | 5,930,000.00 USD | 2,170.00 USD | 0.00 USD | `+33.56%` | `1,297.00` |
| `Live` | `Short` | `1.69` | 5,930,000.00 USD | 4,180.00 USD | 0.00 USD | `+34.36%` | `2,483.00` |
| `Live` | `Short` | `1.70` | 5,930,000.00 USD | 1,160.00 USD | 0.00 USD | `+35.16%` | `686.00` |
| `Live` | `Short` | `1.71` | 5,930,000.00 USD | 1,980.00 USD | 0.00 USD | `+35.95%` | `1,163.00` |
| `Live` | `Short` | `1.74` | 5,940,000.00 USD | 3,960.00 USD | 0.00 USD | `+38.35%` | `2,285.00` |
| `Live` | `Short` | `1.75` | 5,940,000.00 USD | 2,730.00 USD | 0.00 USD | `+39.14%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 11,190,000.00 USD | 5,250,000.00 USD | 0.00 USD | `+39.94%` | `2,990,665.00` |
| `Live` | `Short` | `1.76` | 11,200,000.00 USD | 7,340.00 USD | 0.00 USD | `+40.74%` | `4,157.00` |
| `Live` | `Short` | `1.77` | 11,200,000.00 USD | 351.45 USD | 0.00 USD | `+41.54%` | `198.00` |
| `Live` | `Short` | `1.78` | 11,330,000.00 USD | 129,540.00 USD | 0.00 USD | `+42.33%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 11,330,000.00 USD | 2,850.00 USD | 0.00 USD | `+43.13%` | `1,590.00` |
| `Live` | `Short` | `1.80` | 11,330,000.00 USD | 889.87 USD | 0.00 USD | `+43.93%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,330,000.00 USD | 747.78 USD | 0.00 USD | `+44.72%` | `412.00` |
| `Live` | `Short` | `1.82` | 11,330,000.00 USD | 2,020.00 USD | 0.00 USD | `+45.52%` | `1,107.00` |
| `Live` | `Short` | `1.83` | 11,330,000.00 USD | 128.45 USD | 0.00 USD | `+46.32%` | `70.00` |
| `Live` | `Short` | `1.84` | 11,340,000.00 USD | 9,340.00 USD | 0.00 USD | `+47.12%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,340,000.00 USD | 428.50 USD | 0.00 USD | `+47.91%` | `231.00` |
| `Live` | `Short` | `1.86` | 14,220,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+48.71%` | `1,541,791.00` |
| `Live` | `Short` | `1.88` | 14,330,000.00 USD | 113,220.00 USD | 0.00 USD | `+49.51%` | `60,386.00` |
| `Live` | `Short` | `1.90` | 14,340,000.00 USD | 4,190.00 USD | 0.00 USD | `+51.10%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 14,340,000.00 USD | 552.45 USD | 0.00 USD | `+51.90%` | `290.00` |
| `Live` | `Short` | `1.92` | 14,340,000.00 USD | 794.73 USD | 0.00 USD | `+52.70%` | `415.00` |
| `Live` | `Short` | `1.93` | 14,650,000.00 USD | 309,300.00 USD | 0.00 USD | `+53.50%` | `160,677.00` |
| `Live` | `Short` | `1.94` | 14,650,000.00 USD | 8,870.00 USD | 0.00 USD | `+54.29%` | `4,584.00` |
| `Live` | `Short` | `1.95` | 14,660,000.00 USD | 3,320.00 USD | 0.00 USD | `+55.09%` | `1,709.00` |
| `Live` | `Short` | `1.96` | 14,660,000.00 USD | 293.25 USD | 0.00 USD | `+55.89%` | `150.00` |
| `Live` | `Short` | `1.97` | 14,890,000.00 USD | 227,680.00 USD | 0.00 USD | `+56.69%` | `115,869.00` |
| `Live` | `Short` | `1.98` | 14,890,000.00 USD | 651.75 USD | 0.00 USD | `+57.48%` | `330.00` |
| `Live` | `Short` | `1.99` | 14,890,000.00 USD | 119.10 USD | 0.00 USD | `+58.28%` | `60.00` |
| `Live` | `Short` | `2.00` | 15,290,000.00 USD | 401,000.00 USD | 0.00 USD | `+59.87%` | `200,000.00` |
| `Live` | `Short` | `2.02` | 15,290,000.00 USD | 1,290.00 USD | 0.00 USD | `+60.67%` | `642.00` |
| `Live` | `Short` | `2.04` | 15,290,000.00 USD | 2,010.00 USD | 0.00 USD | `+62.27%` | `989.00` |
| `Live` | `Short` | `2.04` | 21,250,000.00 USD | 5,960,000.00 USD | 0.00 USD | `+63.06%` | `2,912,713.00` |
| `Live` | `Short` | `2.06` | 21,250,000.00 USD | 460.50 USD | 0.00 USD | `+64.66%` | `223.00` |
| `Live` | `Short` | `2.08` | 21,250,000.00 USD | 1,200.00 USD | 0.00 USD | `+65.46%` | `577.00` |
| `Live` | `Short` | `2.08` | 23,930,000.00 USD | 2,680,000.00 USD | 0.00 USD | `+66.25%` | `1,286,016.00` |
| `Live` | `Short` | `2.10` | 23,930,000.00 USD | 331.01 USD | 0.00 USD | `+67.05%` | `158.00` |
| `Live` | `Short` | `2.10` | 24,180,000.00 USD | 247,230.00 USD | 0.00 USD | `+67.85%` | `117,448.00` |
| `Live` | `Short` | `2.12` | 24,180,000.00 USD | 3,100.00 USD | 0.00 USD | `+68.65%` | `1,468.00` |
| `Live` | `Short` | `2.15` | 24,180,000.00 USD | 1,390.00 USD | 0.00 USD | `+71.84%` | `646.00` |
| `Live` | `Short` | `2.17` | 24,190,000.00 USD | 3,000.00 USD | 0.00 USD | `+73.43%` | `1,379.00` |
| `Live` | `Short` | `2.19` | 24,190,000.00 USD | 301.53 USD | 0.00 USD | `+74.23%` | `138.00` |
| `Live` | `Short` | `2.19` | 24,190,000.00 USD | 201.94 USD | 0.00 USD | `+75.03%` | `92.00` |
| `Live` | `Short` | `2.21` | 24,190,000.00 USD | 873.18 USD | 0.00 USD | `+75.82%` | `396.00` |
| `Live` | `Short` | `2.21` | 24,190,000.00 USD | 2,750.00 USD | 0.00 USD | `+76.62%` | `1,243.00` |
| `Live` | `Short` | `2.23` | 24,270,000.00 USD | 75,280.00 USD | 0.00 USD | `+77.42%` | `33,833.00` |
| `Live` | `Short` | `2.23` | 24,270,000.00 USD | 205.62 USD | 0.00 USD | `+78.21%` | `92.00` |
| `Live` | `Short` | `2.25` | 24,270,000.00 USD | 103.27 USD | 0.00 USD | `+79.01%` | `46.00` |
| `Live` | `Short` | `2.25` | 24,270,000.00 USD | 103.73 USD | 0.00 USD | `+79.81%` | `46.00` |
| `Live` | `Short` | `2.27` | 24,270,000.00 USD | 208.38 USD | 0.00 USD | `+80.61%` | `92.00` |
| `Live` | `Short` | `2.29` | 24,310,000.00 USD | 44,140.00 USD | 0.00 USD | `+82.20%` | `19,317.00` |
| `Live` | `Short` | `2.29` | 24,310,000.00 USD | 459.00 USD | 0.00 USD | `+83.00%` | `200.00` |
| `Live` | `Short` | `2.31` | 24,310,000.00 USD | 2,860.00 USD | 0.00 USD | `+83.80%` | `1,239.00` |
| `Live` | `Short` | `2.31` | 24,320,000.00 USD | 11,850.00 USD | 0.00 USD | `+84.59%` | `5,119.00` |
| `Live` | `Short` | `2.33` | 24,330,000.00 USD | 2,540.00 USD | 0.00 USD | `+85.39%` | `1,093.00` |
| `Live` | `Short` | `2.33` | 24,330,000.00 USD | 144.77 USD | 0.00 USD | `+86.19%` | `62.00` |
| `Live` | `Short` | `2.35` | 24,330,000.00 USD | 222.77 USD | 0.00 USD | `+86.99%` | `95.00` |
| `Live` | `Short` | `2.37` | 24,330,000.00 USD | 108.79 USD | 0.00 USD | `+88.58%` | `46.00` |
| `Live` | `Short` | `2.38` | 24,380,000.00 USD | 56,430.00 USD | 0.00 USD | `+89.38%` | `23,758.00` |
| `Live` | `Short` | `2.38` | 24,610,000.00 USD | 225,350.00 USD | 0.00 USD | `+90.18%` | `94,485.00` |
| `Live` | `Short` | `2.40` | 24,610,000.00 USD | 155.68 USD | 0.00 USD | `+90.97%` | `65.00` |
| `Live` | `Short` | `2.40` | 24,610,000.00 USD | 481.00 USD | 0.00 USD | `+91.77%` | `200.00` |
| `Live` | `Short` | `2.42` | 24,640,000.00 USD | 27,800.00 USD | 0.00 USD | `+93.36%` | `11,463.00` |
| `Live` | `Short` | `2.44` | 24,660,000.00 USD | 18,830.00 USD | 0.00 USD | `+94.16%` | `7,734.00` |
| `Live` | `Short` | `2.44` | 24,660,000.00 USD | 2,840.00 USD | 0.00 USD | `+94.96%` | `1,160.00` |
| `Live` | `Short` | `2.46` | 24,750,000.00 USD | 94,260.00 USD | 0.00 USD | `+95.76%` | `38,397.00` |
| `Live` | `Short` | `2.48` | 24,750,000.00 USD | 337.96 USD | 0.00 USD | `+98.15%` | `136.00` |
| `Live` | `Short` | `2.50` | 24,760,000.00 USD | 4,370.00 USD | 0.00 USD | `+99.74%` | `1,744.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 1,210,000.00 USD | 0.00 USD | 112.45 USD | `-79.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 1,210,000.00 USD | 0.00 USD | 139.12 USD | `-70.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 1,210,000.00 USD | 0.00 USD | 200.86 USD | `-66.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 1,210,000.00 USD | 0.00 USD | 408.51 USD | `-64.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 1,210,000.00 USD | 0.00 USD | 273.00 USD | `-63.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 1,210,000.00 USD | 0.00 USD | 151.12 USD | `-62.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 1,210,000.00 USD | 0.00 USD | 142.50 USD | `-62.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 1,210,000.00 USD | 0.00 USD | 145.50 USD | `-61.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 1,210,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 1,210,000.00 USD | 0.00 USD | 285.82 USD | `-58.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 1,210,000.00 USD | 0.00 USD | 306.60 USD | `-58.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 1,210,000.00 USD | 0.00 USD | 121.55 USD | `-55.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 1,210,000.00 USD | 0.00 USD | 374.60 USD | `-54.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 1,210,000.00 USD | 0.00 USD | 100.62 USD | `-53.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 1,210,000.00 USD | 0.00 USD | 203.75 USD | `-50.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 1,210,000.00 USD | 0.00 USD | 791.85 USD | `-49.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 1,210,000.00 USD | 0.00 USD | 573.40 USD | `-48.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 1,210,000.00 USD | 0.00 USD | 364.18 USD | `-47.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 1,210,000.00 USD | 0.00 USD | 3,220.00 USD | `-46.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 1,200,000.00 USD | 0.00 USD | 503.55 USD | `-46.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 1,200,000.00 USD | 0.00 USD | 480.19 USD | `-45.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 1,200,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 1,190,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 1,190,000.00 USD | 0.00 USD | 228.80 USD | `-42.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 1,190,000.00 USD | 0.00 USD | 536.50 USD | `-42.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 1,190,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 1,190,000.00 USD | 0.00 USD | 2,880.00 USD | `-39.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 1,180,000.00 USD | 0.00 USD | 1,080.00 USD | `-36.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,180,000.00 USD | 0.00 USD | 798.57 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,180,000.00 USD | 0.00 USD | 690.38 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,180,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,180,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,180,000.00 USD | 0.00 USD | 838.94 USD | `-27.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,170,000.00 USD | 0.00 USD | 338.55 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,170,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,170,000.00 USD | 0.00 USD | 1,180.00 USD | `-25.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,170,000.00 USD | 0.00 USD | 112.46 USD | `-24.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,170,000.00 USD | 0.00 USD | 2,360.00 USD | `-23.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,170,000.00 USD | 0.00 USD | 3,910.00 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,170,000.00 USD | 0.00 USD | 7,230.00 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,160,000.00 USD | 0.00 USD | 5,000.00 USD | `-21.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,150,000.00 USD | 0.00 USD | 661.67 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,150,000.00 USD | 0.00 USD | 16,410.00 USD | `-19.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,140,000.00 USD | 0.00 USD | 6,900.00 USD | `-19.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,130,000.00 USD | 0.00 USD | 2,020.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,130,000.00 USD | 0.00 USD | 38,000.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,090,000.00 USD | 0.00 USD | 3,490.00 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,090,000.00 USD | 0.00 USD | 2,110.00 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,080,000.00 USD | 0.00 USD | 3,960.00 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,080,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,030,000.00 USD | 0.00 USD | 868.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,030,000.00 USD | 0.00 USD | 38,150.00 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 992,730.00 USD | 0.00 USD | 3,700.00 USD | `-11.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 989,030.00 USD | 0.00 USD | 11,630.00 USD | `-11.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 977,400.00 USD | 0.00 USD | 80,050.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 897,350.00 USD | 0.00 USD | 13,830.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 883,520.00 USD | 0.00 USD | 14,460.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 869,060.00 USD | 0.00 USD | 30,090.00 USD | `-7.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 838,970.00 USD | 0.00 USD | 38,810.00 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 800,160.00 USD | 0.00 USD | 7,640.00 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 792,520.00 USD | 0.00 USD | 145,060.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 647,460.00 USD | 0.00 USD | 145,280.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 502,180.00 USD | 0.00 USD | 214,020.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 288,160.00 USD | 0.00 USD | 122,190.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 165,970.00 USD | 0.00 USD | 57,920.00 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 108,050.00 USD | 0.00 USD | 77,520.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 30,530.00 USD | 0.00 USD | 30,530.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 15,880.00 USD | 15,880.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 110,030.00 USD | 94,150.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 117,350.00 USD | 7,310.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 356,080.00 USD | 238,730.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 419,040.00 USD | 62,960.00 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 467,000.00 USD | 47,960.00 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 860,930.00 USD | 393,930.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,070,000.00 USD | 207,660.00 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,100,000.00 USD | 36,000.00 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,300,000.00 USD | 196,480.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,320,000.00 USD | 15,250.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,590,000.00 USD | 275,680.00 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,670,000.00 USD | 82,920.00 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,730,000.00 USD | 50,450.00 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,730,000.00 USD | 6,060.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,090,000.00 USD | 4,360,000.00 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,090,000.00 USD | 1,980.00 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,100,000.00 USD | 6,850.00 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,180,000.00 USD | 80,260.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,390,000.00 USD | 213,140.00 USD | 0.00 USD | `+15.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,400,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,420,000.00 USD | 22,800.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,530,000.00 USD | 107,960.00 USD | 0.00 USD | `+17.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,580,000.00 USD | 55,680.00 USD | 0.00 USD | `+18.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,600,000.00 USD | 13,980.00 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,640,000.00 USD | 43,080.00 USD | 0.00 USD | `+20.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,650,000.00 USD | 10,320.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,740,000.00 USD | 93,330.00 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,790,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,810,000.00 USD | 22,220.00 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,810,000.00 USD | 2,690.00 USD | 0.00 USD | `+23.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,820,000.00 USD | 7,340.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,830,000.00 USD | 5,940.00 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,840,000.00 USD | 11,870.00 USD | 0.00 USD | `+26.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,990,000.00 USD | 148,780.00 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,990,000.00 USD | 1,840.00 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,070,000.00 USD | 80,320.00 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,070,000.00 USD | 464.75 USD | 0.00 USD | `+29.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,260,000.00 USD | 184,610.00 USD | 0.00 USD | `+30.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,260,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,280,000.00 USD | 18,210.00 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,280,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,300,000.00 USD | 18,400.00 USD | 0.00 USD | `+33.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,370,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,370,000.00 USD | 2,770.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,610,000.00 USD | 240,380.00 USD | 0.00 USD | `+35.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,630,000.00 USD | 14,030.00 USD | 0.00 USD | `+36.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,630,000.00 USD | 5,910.00 USD | 0.00 USD | `+37.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,680,000.00 USD | 44,100.00 USD | 0.00 USD | `+38.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,680,000.00 USD | 4,710.00 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,690,000.00 USD | 5,510.00 USD | 0.00 USD | `+39.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,710,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,840,000.00 USD | 124,780.00 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,930,000.00 USD | 96,600.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,970,000.00 USD | 36,490.00 USD | 0.00 USD | `+43.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,970,000.00 USD | 254.51 USD | 0.00 USD | `+43.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,970,000.00 USD | 2,530.00 USD | 0.00 USD | `+44.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,970,000.00 USD | 1,830.00 USD | 0.00 USD | `+45.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,980,000.00 USD | 7,280.00 USD | 0.00 USD | `+46.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,980,000.00 USD | 1,010.00 USD | 0.00 USD | `+47.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,990,000.00 USD | 8,390.00 USD | 0.00 USD | `+47.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,990,000.00 USD | 4,250.00 USD | 0.00 USD | `+49.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,990,000.00 USD | 591.89 USD | 0.00 USD | `+50.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,030,000.00 USD | 38,610.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,070,000.00 USD | 38,940.00 USD | 0.00 USD | `+51.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 8,080,000.00 USD | 7,410.00 USD | 0.00 USD | `+52.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,080,000.00 USD | 265.10 USD | 0.00 USD | `+54.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,080,000.00 USD | 2,040.00 USD | 0.00 USD | `+55.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,080,000.00 USD | 1,070.00 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,100,000.00 USD | 14,120.00 USD | 0.00 USD | `+56.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,100,000.00 USD | 4,010.00 USD | 0.00 USD | `+57.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,100,000.00 USD | 325.54 USD | 0.00 USD | `+58.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,110,000.00 USD | 7,020.00 USD | 0.00 USD | `+59.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,230,000.00 USD | 123,150.00 USD | 0.00 USD | `+59.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,230,000.00 USD | 781.82 USD | 0.00 USD | `+60.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,230,000.00 USD | 222.75 USD | 0.00 USD | `+61.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,230,000.00 USD | 862.84 USD | 0.00 USD | `+62.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,230,000.00 USD | 382.41 USD | 0.00 USD | `+63.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,240,000.00 USD | 3,420.00 USD | 0.00 USD | `+64.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,240,000.00 USD | 661.93 USD | 0.00 USD | `+65.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,360,000.00 USD | 124,400.00 USD | 0.00 USD | `+67.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,360,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,380,000.00 USD | 13,900.00 USD | 0.00 USD | `+69.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,400,000.00 USD | 24,840.00 USD | 0.00 USD | `+71.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,450,000.00 USD | 50,580.00 USD | 0.00 USD | `+71.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,460,000.00 USD | 2,690.00 USD | 0.00 USD | `+72.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,480,000.00 USD | 20,370.00 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,630,000.00 USD | 151,380.00 USD | 0.00 USD | `+76.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,640,000.00 USD | 7,340.00 USD | 0.00 USD | `+78.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,640,000.00 USD | 3,120.00 USD | 0.00 USD | `+81.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,640,000.00 USD | 1,140.00 USD | 0.00 USD | `+82.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,650,000.00 USD | 12,150.00 USD | 0.00 USD | `+83.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,650,000.00 USD | 370.40 USD | 0.00 USD | `+84.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,650,000.00 USD | 733.19 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,650,000.00 USD | 2,410.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,660,000.00 USD | 475.00 USD | 0.00 USD | `+89.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,660,000.00 USD | 2,540.00 USD | 0.00 USD | `+90.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,660,000.00 USD | 1,590.00 USD | 0.00 USD | `+91.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,660,000.00 USD | 1,370.00 USD | 0.00 USD | `+92.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,680,000.00 USD | 19,590.00 USD | 0.00 USD | `+93.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,690,000.00 USD | 4,580.00 USD | 0.00 USD | `+94.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,690,000.00 USD | 8,110.00 USD | 0.00 USD | `+95.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,700,000.00 USD | 3,420.00 USD | 0.00 USD | `+98.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,700,000.00 USD | 124.75 USD | 0.00 USD | `+98.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,730,000.00 USD | 30,920.00 USD | 0.00 USD | `+99.74%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.11` | 62,410,000.00 USD | 0.00 USD | 62,410,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.11` | 35,830,000.00 USD | 0.00 USD | 35,830,000.00 USD | 17,310.00 USD | 0.00 USD | 116,380.00 USD |
| `1D` | `1.11` | 35,700,000.00 USD | 0.00 USD | 35,700,000.00 USD | 18,710.00 USD | 937.65 USD | 3,250.00 USD |
| `7D` | `1.11` | 62,380,000.00 USD | 0.00 USD | 62,380,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 35,680,000.00 USD | 0.00 USD | 35,680,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD |
| `7D` | `1.12` | 62,370,000.00 USD | 0.00 USD | 62,370,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 35,680,000.00 USD | 0.00 USD | 35,680,000.00 USD | 0.00 USD | 0.00 USD | 14,180.00 USD |
| `1D` | `1.12` | 35,660,000.00 USD | 0.00 USD | 35,660,000.00 USD | 0.00 USD | 47,700.00 USD | 0.00 USD |
| `7D` | `1.12` | 62,290,000.00 USD | 0.00 USD | 62,290,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `1.12` | 35,610,000.00 USD | 0.00 USD | 35,610,000.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD |
| `7D` | `1.12` | 62,290,000.00 USD | 0.00 USD | 62,290,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD |
| `1D` | `1.12` | 35,610,000.00 USD | 0.00 USD | 35,610,000.00 USD | 0.00 USD | 2,460.00 USD | 10,870.00 USD |
| `7D` | `1.12` | 62,290,000.00 USD | 0.00 USD | 62,290,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 35,600,000.00 USD | 0.00 USD | 35,600,000.00 USD | 66,330.00 USD | 27,680.00 USD | 48,500.00 USD |
| `1D` | `1.13` | 35,460,000.00 USD | 0.00 USD | 35,460,000.00 USD | 0.00 USD | 1,660.00 USD | 51,720.00 USD |
| `7D` | `1.13` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 35,400,000.00 USD | 0.00 USD | 35,400,000.00 USD | 0.00 USD | 107,140.00 USD | 78,200.00 USD |
| `7D` | `1.13` | 61,880,000.00 USD | 0.00 USD | 61,880,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD |
| `1D` | `1.13` | 35,220,000.00 USD | 0.00 USD | 35,220,000.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD |
| `7D` | `1.13` | 61,870,000.00 USD | 0.00 USD | 61,870,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD |
| `1D` | `1.13` | 35,050,000.00 USD | 0.00 USD | 35,050,000.00 USD | 53,700.00 USD | 0.00 USD | 8,110.00 USD |
| `7D` | `1.14` | 61,390,000.00 USD | 0.00 USD | 61,390,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD |
| `1D` | `1.14` | 34,990,000.00 USD | 0.00 USD | 34,990,000.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD |
| `7D` | `1.14` | 61,150,000.00 USD | 0.00 USD | 61,150,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `7D` | `1.14` | 61,050,000.00 USD | 0.00 USD | 61,050,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 34,850,000.00 USD | 0.00 USD | 34,850,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.14` | 61,040,000.00 USD | 0.00 USD | 61,040,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 34,790,000.00 USD | 0.00 USD | 34,790,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 60,970,000.00 USD | 0.00 USD | 60,970,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.14` | 34,720,000.00 USD | 0.00 USD | 34,720,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.15` | 60,850,000.00 USD | 0.00 USD | 60,850,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 60,850,000.00 USD | 0.00 USD | 60,850,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 34,580,000.00 USD | 0.00 USD | 34,580,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 60,710,000.00 USD | 0.00 USD | 60,710,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 60,350,000.00 USD | 0.00 USD | 60,350,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 34,570,000.00 USD | 0.00 USD | 34,570,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 60,190,000.00 USD | 0.00 USD | 60,190,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.15` | 34,500,000.00 USD | 0.00 USD | 34,500,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.16` | 59,800,000.00 USD | 0.00 USD | 59,800,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 34,120,000.00 USD | 0.00 USD | 34,120,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 59,160,000.00 USD | 0.00 USD | 59,160,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 34,000,000.00 USD | 0.00 USD | 34,000,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD |
| `7D` | `1.16` | 58,360,000.00 USD | 0.00 USD | 58,360,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 33,820,000.00 USD | 0.00 USD | 33,820,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 57,830,000.00 USD | 0.00 USD | 57,830,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 33,440,000.00 USD | 0.00 USD | 33,440,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 56,810,000.00 USD | 0.00 USD | 56,810,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 32,700,000.00 USD | 0.00 USD | 32,700,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.17` | 55,440,000.00 USD | 0.00 USD | 55,440,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 32,270,000.00 USD | 0.00 USD | 32,270,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 54,810,000.00 USD | 0.00 USD | 54,810,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 31,940,000.00 USD | 0.00 USD | 31,940,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 53,430,000.00 USD | 0.00 USD | 53,430,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 31,760,000.00 USD | 0.00 USD | 31,760,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 51,920,000.00 USD | 0.00 USD | 51,920,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 31,600,000.00 USD | 0.00 USD | 31,600,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 50,530,000.00 USD | 0.00 USD | 50,530,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.17` | 31,380,000.00 USD | 0.00 USD | 31,380,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.18` | 49,740,000.00 USD | 0.00 USD | 49,740,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 31,110,000.00 USD | 0.00 USD | 31,110,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 48,860,000.00 USD | 0.00 USD | 48,860,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 30,890,000.00 USD | 0.00 USD | 30,890,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 48,400,000.00 USD | 0.00 USD | 48,400,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 30,710,000.00 USD | 0.00 USD | 30,710,000.00 USD | 71,950.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 47,680,000.00 USD | 0.00 USD | 47,680,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 30,610,000.00 USD | 0.00 USD | 30,610,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 47,310,000.00 USD | 0.00 USD | 47,310,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.18` | 30,530,000.00 USD | 0.00 USD | 30,530,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.19` | 47,180,000.00 USD | 0.00 USD | 47,180,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 30,420,000.00 USD | 0.00 USD | 30,420,000.00 USD | 59,140.00 USD | 145,870.00 USD | 25,350.00 USD |
| `7D` | `1.19` | 46,670,000.00 USD | 0.00 USD | 46,670,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD |
| `1D` | `1.19` | 30,190,000.00 USD | 0.00 USD | 30,190,000.00 USD | 189,200.00 USD | 3,790.00 USD | 599,810.00 USD |
| `7D` | `1.19` | 45,900,000.00 USD | 0.00 USD | 45,900,000.00 USD | 182,110.00 USD | 132,500.00 USD | 278,870.00 USD |
| `1D` | `1.19` | 29,390,000.00 USD | 0.00 USD | 29,390,000.00 USD | 10,800.00 USD | 3,540.00 USD | 21,580.00 USD |
| `7D` | `1.19` | 45,300,000.00 USD | 0.00 USD | 45,300,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD |
| `1D` | `1.19` | 29,360,000.00 USD | 0.00 USD | 29,360,000.00 USD | 39,850.00 USD | 17,460.00 USD | 92,300.00 USD |
| `7D` | `1.19` | 44,610,000.00 USD | 0.00 USD | 44,610,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 29,210,000.00 USD | 0.00 USD | 29,210,000.00 USD | 64,160.00 USD | 215,840.00 USD | 69,720.00 USD |
| `7D` | `1.20` | 43,950,000.00 USD | 0.00 USD | 43,950,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 28,860,000.00 USD | 0.00 USD | 28,860,000.00 USD | 0.00 USD | 2,370.00 USD | 8,380.00 USD |
| `7D` | `1.20` | 43,240,000.00 USD | 0.00 USD | 43,240,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 28,850,000.00 USD | 0.00 USD | 28,850,000.00 USD | 66,960.00 USD | 19,950.00 USD | 62,750.00 USD |
| `7D` | `1.20` | 42,950,000.00 USD | 0.00 USD | 42,950,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD |
| `1D` | `1.20` | 28,700,000.00 USD | 0.00 USD | 28,700,000.00 USD | 169,810.00 USD | 176,190.00 USD | 219,520.00 USD |
| `7D` | `1.20` | 41,980,000.00 USD | 0.00 USD | 41,980,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 28,130,000.00 USD | 0.00 USD | 28,130,000.00 USD | 70,990.00 USD | 80,650.00 USD | 188,390.00 USD |
| `7D` | `1.20` | 41,500,000.00 USD | 0.00 USD | 41,500,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD |
| `1D` | `1.20` | 27,790,000.00 USD | 0.00 USD | 27,790,000.00 USD | 35,480.00 USD | 106,230.00 USD | 195,510.00 USD |
| `7D` | `1.21` | 40,610,000.00 USD | 0.00 USD | 40,610,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 27,460,000.00 USD | 0.00 USD | 27,460,000.00 USD | 0.00 USD | 193,610.00 USD | 0.00 USD |
| `7D` | `1.21` | 40,520,000.00 USD | 0.00 USD | 40,520,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 27,260,000.00 USD | 0.00 USD | 27,260,000.00 USD | 81,900.00 USD | 99,520.00 USD | 415,780.00 USD |
| `7D` | `1.21` | 40,420,000.00 USD | 0.00 USD | 40,420,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD |
| `1D` | `1.21` | 26,660,000.00 USD | 0.00 USD | 26,660,000.00 USD | 320,140.00 USD | 244,960.00 USD | 91,370.00 USD |
| `7D` | `1.21` | 38,870,000.00 USD | 0.00 USD | 38,870,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD |
| `1D` | `1.21` | 26,010,000.00 USD | 0.00 USD | 26,010,000.00 USD | 419,060.00 USD | 334,050.00 USD | 1,230,000.00 USD |
| `7D` | `1.21` | 37,630,000.00 USD | 0.00 USD | 37,630,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.21` | 24,020,000.00 USD | 0.00 USD | 24,020,000.00 USD | 9,150.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `1.22` | 37,220,000.00 USD | 0.00 USD | 37,220,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD |
| `1D` | `1.22` | 24,000,000.00 USD | 0.00 USD | 24,000,000.00 USD | 117,720.00 USD | 0.00 USD | 122,170.00 USD |
| `7D` | `1.22` | 37,050,000.00 USD | 0.00 USD | 37,050,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD |
| `1D` | `1.22` | 23,760,000.00 USD | 0.00 USD | 23,760,000.00 USD | 174,270.00 USD | 380,580.00 USD | 135,230.00 USD |
| `7D` | `1.22` | 36,490,000.00 USD | 0.00 USD | 36,490,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 23,070,000.00 USD | 0.00 USD | 23,070,000.00 USD | 157,550.00 USD | 9,600.00 USD | 208,620.00 USD |
| `7D` | `1.22` | 36,190,000.00 USD | 0.00 USD | 36,190,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 22,700,000.00 USD | 0.00 USD | 22,700,000.00 USD | 0.00 USD | 5,120.00 USD | 55,100.00 USD |
| `7D` | `1.22` | 35,690,000.00 USD | 0.00 USD | 35,690,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD |
| `1D` | `1.22` | 22,640,000.00 USD | 0.00 USD | 22,640,000.00 USD | 173,990.00 USD | 530,550.00 USD | 1,480,000.00 USD |
| `7D` | `1.23` | 34,440,000.00 USD | 0.00 USD | 34,440,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD |
| `1D` | `1.23` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 788,770.00 USD | 500,530.00 USD | 1,510,000.00 USD |
| `7D` | `1.23` | 31,560,000.00 USD | 0.00 USD | 31,560,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 17,650,000.00 USD | 0.00 USD | 17,650,000.00 USD | 190,540.00 USD | 9,950.00 USD | 258,620.00 USD |
| `7D` | `1.23` | 31,100,000.00 USD | 0.00 USD | 31,100,000.00 USD | 0.00 USD | 1,110,000.00 USD | 995,690.00 USD |
| `1D` | `1.23` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 200,000.00 USD | 623,370.00 USD | 551,100.00 USD |
| `7D` | `1.23` | 29,000,000.00 USD | 0.00 USD | 29,000,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD |
| `1D` | `1.23` | 15,820,000.00 USD | 0.00 USD | 15,820,000.00 USD | 435,700.00 USD | 821,750.00 USD | 831,560.00 USD |
| `7D` | `1.23` | 27,720,000.00 USD | 0.00 USD | 27,720,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD |
| `1D` | `1.23` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 318,380.00 USD | 134,700.00 USD | 14,480.00 USD |
| `7D` | `1.24` | 25,970,000.00 USD | 0.00 USD | 25,970,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD |
| `1D` | `1.24` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 405,830.00 USD | 298,200.00 USD | 227,540.00 USD |
| `7D` | `1.24` | 23,910,000.00 USD | 0.00 USD | 23,910,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD |
| `1D` | `1.24` | 12,330,000.00 USD | 0.00 USD | 12,330,000.00 USD | 663,280.00 USD | 1,240,000.00 USD | 1,040,000.00 USD |
| `7D` | `1.24` | 17,960,000.00 USD | 0.00 USD | 17,960,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD |
| `1D` | `1.24` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 266,660.00 USD | 0.00 USD | 857,830.00 USD |
| `7D` | `1.24` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 1,940,000.00 USD |
| `1D` | `1.24` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 112,970.00 USD | 774,420.00 USD | 1,260,000.00 USD |
| `7D` | `1.24` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `1.24` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 1,050,000.00 USD | 116,230.00 USD | 2,340,000.00 USD |
| `7D` | `1.25` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 3,440,000.00 USD | 923,130.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 1,330,000.00 USD | 351,240.00 USD | 551,670.00 USD |
| `7D` | `1.25` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 381,120.00 USD | 0.00 USD | 381,120.00 USD | 381,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 140,880.00 USD | 0.00 USD | 140,880.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 180,020.00 USD | 180,020.00 USD | 0.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 360,040.00 USD | 360,040.00 USD | 0.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 4,230.00 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,230.00 USD |
| `1D` | `1.25` | 8,460.00 USD | 8,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,230.00 USD |
| `7D` | `1.25` | 500,700.00 USD | 500,700.00 USD | 0.00 USD | 74,170.00 USD | 0.00 USD | 66,490.00 USD |
| `1D` | `1.25` | 176,980.00 USD | 176,980.00 USD | 0.00 USD | 168,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 691,470.00 USD | 691,470.00 USD | 0.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD |
| `1D` | `1.26` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,600.00 USD | 0.00 USD |
| `1D` | `1.26` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD |
| `7D` | `1.26` | 798,620.00 USD | 798,620.00 USD | 0.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 384,710.00 USD | 68,210.00 USD | 202,460.00 USD |
| `7D` | `1.26` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD |
| `1D` | `1.26` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 424,010.00 USD | 0.00 USD | 1,550,000.00 USD |
| `7D` | `1.26` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 663,280.00 USD | 1,020,000.00 USD | 2,250,000.00 USD |
| `7D` | `1.26` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 306,520.00 USD | 1,030,000.00 USD | 599,690.00 USD |
| `7D` | `1.27` | 27,480,000.00 USD | 27,480,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,250,000.00 USD |
| `1D` | `1.27` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 2,050,000.00 USD | 794,130.00 USD |
| `7D` | `1.27` | 32,250,000.00 USD | 32,250,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 327,600.00 USD | 899,410.00 USD | 1,660,000.00 USD |
| `7D` | `1.27` | 35,860,000.00 USD | 35,860,000.00 USD | 0.00 USD | 943,110.00 USD | 2,540,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 17,930,000.00 USD | 17,930,000.00 USD | 0.00 USD | 1,430,000.00 USD | 588,250.00 USD | 64,670.00 USD |
| `7D` | `1.27` | 40,620,000.00 USD | 40,620,000.00 USD | 0.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD |
| `1D` | `1.27` | 21,660,000.00 USD | 21,660,000.00 USD | 0.00 USD | 465,090.00 USD | 1,250,000.00 USD | 2,020,000.00 USD |
| `7D` | `1.27` | 57,060,000.00 USD | 57,060,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD |
| `1D` | `1.28` | 28,030,000.00 USD | 28,030,000.00 USD | 0.00 USD | 817,960.00 USD | 2,340,000.00 USD | 3,210,000.00 USD |
| `7D` | `1.28` | 75,330,000.00 USD | 75,330,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 41,510,000.00 USD | 41,510,000.00 USD | 0.00 USD | 6,020,000.00 USD | 2,730,000.00 USD | 4,730,000.00 USD |
| `7D` | `1.28` | 81,620,000.00 USD | 81,620,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 44,420,000.00 USD | 44,420,000.00 USD | 0.00 USD | 197,050.00 USD | 2,010,000.00 USD | 703,330.00 USD |
| `7D` | `1.28` | 82,580,000.00 USD | 82,580,000.00 USD | 0.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 46,430,000.00 USD | 46,430,000.00 USD | 0.00 USD | 710,910.00 USD | 64,340.00 USD | 1,240,000.00 USD |
| `7D` | `1.28` | 84,590,000.00 USD | 84,590,000.00 USD | 0.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD |
| `1D` | `1.28` | 48,630,000.00 USD | 48,630,000.00 USD | 0.00 USD | 905,740.00 USD | 418,710.00 USD | 869,370.00 USD |
| `7D` | `1.28` | 88,180,000.00 USD | 88,180,000.00 USD | 0.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD |
| `1D` | `1.29` | 50,780,000.00 USD | 50,780,000.00 USD | 0.00 USD | 441,010.00 USD | 687,930.00 USD | 1,020,000.00 USD |
| `7D` | `1.29` | 89,350,000.00 USD | 89,350,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 51,780,000.00 USD | 51,780,000.00 USD | 0.00 USD | 584,100.00 USD | 411,690.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 89,470,000.00 USD | 89,470,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 51,810,000.00 USD | 51,810,000.00 USD | 0.00 USD | 18,290.00 USD | 3,310.00 USD | 0.00 USD |
| `7D` | `1.29` | 91,550,000.00 USD | 91,550,000.00 USD | 0.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD |
| `1D` | `1.29` | 53,590,000.00 USD | 53,590,000.00 USD | 0.00 USD | 369,880.00 USD | 0.00 USD | 1,420,000.00 USD |
| `7D` | `1.29` | 91,970,000.00 USD | 91,970,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 57,540,000.00 USD | 57,540,000.00 USD | 0.00 USD | 1,110,000.00 USD | 305,230.00 USD | 2,530,000.00 USD |
| `7D` | `1.29` | 101,610,000.00 USD | 101,610,000.00 USD | 0.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 62,440,000.00 USD | 62,440,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,130,000.00 USD | 2,380,000.00 USD |
| `7D` | `1.30` | 102,840,000.00 USD | 102,840,000.00 USD | 0.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 63,320,000.00 USD | 63,320,000.00 USD | 0.00 USD | 411,640.00 USD | 20,370.00 USD | 446,060.00 USD |
| `7D` | `1.30` | 104,900,000.00 USD | 104,900,000.00 USD | 0.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD |
| `1D` | `1.30` | 64,570,000.00 USD | 64,570,000.00 USD | 0.00 USD | 169,810.00 USD | 344,440.00 USD | 730,290.00 USD |
| `7D` | `1.30` | 106,570,000.00 USD | 106,570,000.00 USD | 0.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 67,030,000.00 USD | 67,030,000.00 USD | 0.00 USD | 673,010.00 USD | 945,470.00 USD | 848,130.00 USD |
| `7D` | `1.30` | 109,660,000.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 67,750,000.00 USD | 67,750,000.00 USD | 0.00 USD | 192,870.00 USD | 204,330.00 USD | 322,840.00 USD |
| `7D` | `1.30` | 109,670,000.00 USD | 109,670,000.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD |
| `1D` | `1.31` | 69,070,000.00 USD | 69,070,000.00 USD | 0.00 USD | 493,480.00 USD | 507,360.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 112,670,000.00 USD | 112,670,000.00 USD | 0.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 72,180,000.00 USD | 72,180,000.00 USD | 0.00 USD | 849,240.00 USD | 310,710.00 USD | 1,950,000.00 USD |
| `7D` | `1.31` | 117,130,000.00 USD | 117,130,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD |
| `1D` | `1.31` | 74,970,000.00 USD | 74,970,000.00 USD | 0.00 USD | 1,090,000.00 USD | 396,100.00 USD | 1,290,000.00 USD |
| `7D` | `1.31` | 120,390,000.00 USD | 120,390,000.00 USD | 0.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD |
| `1D` | `1.31` | 78,290,000.00 USD | 78,290,000.00 USD | 0.00 USD | 1,800,000.00 USD | 778,210.00 USD | 745,480.00 USD |
| `7D` | `1.31` | 123,230,000.00 USD | 123,230,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 80,000,000.00 USD | 80,000,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 125,690,000.00 USD | 125,690,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 85,600,000.00 USD | 85,600,000.00 USD | 0.00 USD | 222,150.00 USD | 1,620,000.00 USD | 3,750,000.00 USD |
| `7D` | `1.32` | 130,320,000.00 USD | 130,320,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 92,400,000.00 USD | 92,400,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD |
| `7D` | `1.32` | 133,400,000.00 USD | 133,400,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 95,650,000.00 USD | 95,650,000.00 USD | 0.00 USD | 1,680,000.00 USD | 546,460.00 USD | 1,030,000.00 USD |
| `7D` | `1.32` | 135,230,000.00 USD | 135,230,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 100,290,000.00 USD | 100,290,000.00 USD | 0.00 USD | 1,870,000.00 USD | 845,300.00 USD | 1,920,000.00 USD |
| `7D` | `1.32` | 139,680,000.00 USD | 139,680,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 103,340,000.00 USD | 103,340,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,620.00 USD | 1,020,000.00 USD |
| `7D` | `1.32` | 142,050,000.00 USD | 142,050,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 105,630,000.00 USD | 105,630,000.00 USD | 0.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 142,590,000.00 USD | 142,590,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 107,820,000.00 USD | 107,820,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 143,740,000.00 USD | 143,740,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 110,260,000.00 USD | 110,260,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 145,460,000.00 USD | 145,460,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 112,520,000.00 USD | 112,520,000.00 USD | 0.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD |
| `7D` | `1.33` | 149,520,000.00 USD | 149,520,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 114,840,000.00 USD | 114,840,000.00 USD | 0.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD |
| `7D` | `1.33` | 150,060,000.00 USD | 150,060,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 117,290,000.00 USD | 117,290,000.00 USD | 0.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 152,010,000.00 USD | 152,010,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 119,970,000.00 USD | 119,970,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD |
| `7D` | `1.34` | 154,350,000.00 USD | 154,350,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 122,370,000.00 USD | 122,370,000.00 USD | 0.00 USD | 1,020,000.00 USD | 302,930.00 USD | 1,080,000.00 USD |
| `7D` | `1.34` | 159,060,000.00 USD | 159,060,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 125,300,000.00 USD | 125,300,000.00 USD | 0.00 USD | 1,330,000.00 USD | 669,200.00 USD | 930,610.00 USD |
| `7D` | `1.34` | 164,710,000.00 USD | 164,710,000.00 USD | 0.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD |
| `1D` | `1.34` | 127,850,000.00 USD | 127,850,000.00 USD | 0.00 USD | 946,370.00 USD | 626,040.00 USD | 979,370.00 USD |
| `7D` | `1.34` | 175,670,000.00 USD | 175,670,000.00 USD | 0.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 129,020,000.00 USD | 129,020,000.00 USD | 0.00 USD | 498,430.00 USD | 189,010.00 USD | 481,220.00 USD |
| `7D` | `1.35` | 182,780,000.00 USD | 182,780,000.00 USD | 0.00 USD | 2,410,000.00 USD | 2,230,000.00 USD | 2,470,000.00 USD |
| `1D` | `1.35` | 130,280,000.00 USD | 130,280,000.00 USD | 0.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD |
| `7D` | `1.35` | 193,090,000.00 USD | 193,090,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 131,770,000.00 USD | 131,770,000.00 USD | 0.00 USD | 768,810.00 USD | 229,320.00 USD | 486,150.00 USD |
| `7D` | `1.35` | 200,860,000.00 USD | 200,860,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 133,090,000.00 USD | 133,090,000.00 USD | 0.00 USD | 554,870.00 USD | 207,050.00 USD | 556,870.00 USD |
| `7D` | `1.35` | 209,190,000.00 USD | 209,190,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 134,420,000.00 USD | 134,420,000.00 USD | 0.00 USD | 493,530.00 USD | 170,640.00 USD | 668,380.00 USD |
| `7D` | `1.35` | 217,420,000.00 USD | 217,420,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 135,330,000.00 USD | 135,330,000.00 USD | 0.00 USD | 351,630.00 USD | 92,050.00 USD | 468,450.00 USD |
| `7D` | `1.36` | 221,510,000.00 USD | 221,510,000.00 USD | 0.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 135,830,000.00 USD | 135,830,000.00 USD | 0.00 USD | 148,530.00 USD | 41,890.00 USD | 312,160.00 USD |
| `7D` | `1.36` | 225,300,000.00 USD | 225,300,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 136,380,000.00 USD | 136,380,000.00 USD | 0.00 USD | 266,880.00 USD | 47,170.00 USD | 233,330.00 USD |
| `7D` | `1.36` | 227,440,000.00 USD | 227,440,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 137,050,000.00 USD | 137,050,000.00 USD | 0.00 USD | 241,460.00 USD | 104,340.00 USD | 321,110.00 USD |
| `7D` | `1.36` | 231,530,000.00 USD | 231,530,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 137,190,000.00 USD | 137,190,000.00 USD | 0.00 USD | 80,160.00 USD | 27,780.00 USD | 31,150.00 USD |
| `7D` | `1.36` | 233,250,000.00 USD | 233,250,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 137,380,000.00 USD | 137,380,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 138,790.00 USD |
| `7D` | `1.37` | 233,740,000.00 USD | 233,740,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 137,610,000.00 USD | 137,610,000.00 USD | 0.00 USD | 84,710.00 USD | 105,400.00 USD | 44,320.00 USD |
| `7D` | `1.37` | 235,160,000.00 USD | 235,160,000.00 USD | 0.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 137,790,000.00 USD | 137,790,000.00 USD | 0.00 USD | 38,340.00 USD | 26,490.00 USD | 110,310.00 USD |
| `7D` | `1.37` | 236,320,000.00 USD | 236,320,000.00 USD | 0.00 USD | 334,560.00 USD | 372,470.00 USD | 461,160.00 USD |
| `1D` | `1.37` | 137,930,000.00 USD | 137,930,000.00 USD | 0.00 USD | 3,890.00 USD | 42,450.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 238,870,000.00 USD | 238,870,000.00 USD | 0.00 USD | 870,810.00 USD | 406,050.00 USD | 1,270,000.00 USD |
| `1D` | `1.37` | 138,080,000.00 USD | 138,080,000.00 USD | 0.00 USD | 74,330.00 USD | 2,720.00 USD | 77,720.00 USD |
| `7D` | `1.38` | 240,680,000.00 USD | 240,680,000.00 USD | 0.00 USD | 536,130.00 USD | 295,850.00 USD | 969,400.00 USD |
| `1D` | `1.38` | 138,480,000.00 USD | 138,480,000.00 USD | 0.00 USD | 169,050.00 USD | 60,310.00 USD | 169,890.00 USD |
| `7D` | `1.38` | 242,230,000.00 USD | 242,230,000.00 USD | 0.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 139,030,000.00 USD | 139,030,000.00 USD | 0.00 USD | 228,570.00 USD | 72,280.00 USD | 246,930.00 USD |
| `7D` | `1.38` | 244,370,000.00 USD | 244,370,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD |
| `1D` | `1.38` | 139,450,000.00 USD | 139,450,000.00 USD | 0.00 USD | 158,070.00 USD | 75,630.00 USD | 183,470.00 USD |
| `7D` | `1.38` | 246,910,000.00 USD | 246,910,000.00 USD | 0.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 139,530,000.00 USD | 139,530,000.00 USD | 0.00 USD | 0.00 USD | 65,520.00 USD | 20,960.00 USD |
| `7D` | `1.38` | 248,000,000.00 USD | 248,000,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 139,700,000.00 USD | 139,700,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD |
| `7D` | `1.39` | 249,290,000.00 USD | 249,290,000.00 USD | 0.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 139,760,000.00 USD | 139,760,000.00 USD | 0.00 USD | 53,700.00 USD | 0.00 USD | 8,110.00 USD |
| `7D` | `1.39` | 249,830,000.00 USD | 249,830,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD |
| `1D` | `1.39` | 139,900,000.00 USD | 139,900,000.00 USD | 0.00 USD | 40,370.00 USD | 96,300.00 USD | 0.00 USD |
| `7D` | `1.39` | 250,930,000.00 USD | 250,930,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 251,100,000.00 USD | 251,100,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 139,900,000.00 USD | 139,900,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 251,420,000.00 USD | 251,420,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 139,960,000.00 USD | 139,960,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 31,230.00 USD |
| `1D` | `1.40` | 139,980,000.00 USD | 139,980,000.00 USD | 0.00 USD | 21,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.40` | 251,590,000.00 USD | 251,590,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 251,710,000.00 USD | 251,710,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 251,720,000.00 USD | 251,720,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 251,860,000.00 USD | 251,860,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 251,970,000.00 USD | 251,970,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 252,220,000.00 USD | 252,220,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 252,380,000.00 USD | 252,380,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 252,760,000.00 USD | 252,760,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `7D` | `1.41` | 253,410,000.00 USD | 253,410,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `7D` | `1.41` | 253,580,000.00 USD | 253,580,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `7D` | `1.42` | 254,210,000.00 USD | 254,210,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `7D` | `1.42` | 254,730,000.00 USD | 254,730,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `7D` | `1.42` | 255,750,000.00 USD | 255,750,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.42` | 257,130,000.00 USD | 257,130,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `7D` | `1.42` | 257,760,000.00 USD | 257,760,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 258,120,000.00 USD | 258,120,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 259,140,000.00 USD | 259,140,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 260,640,000.00 USD | 260,640,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 262,030,000.00 USD | 262,030,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 262,830,000.00 USD | 262,830,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 263,360,000.00 USD | 263,360,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 263,710,000.00 USD | 263,710,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 264,170,000.00 USD | 264,170,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 264,880,000.00 USD | 264,880,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 265,260,000.00 USD | 265,260,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 265,390,000.00 USD | 265,390,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 265,510,000.00 USD | 265,510,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 265,840,000.00 USD | 265,840,000.00 USD | 0.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 266,450,000.00 USD | 266,450,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 267,020,000.00 USD | 267,020,000.00 USD | 0.00 USD | 182,110.00 USD | 128,180.00 USD | 251,300.00 USD |
| `7D` | `1.46` | 267,480,000.00 USD | 267,480,000.00 USD | 0.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `7D` | `1.46` | 267,630,000.00 USD | 267,630,000.00 USD | 0.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD |
| `7D` | `1.46` | 268,110,000.00 USD | 268,110,000.00 USD | 0.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD |
| `7D` | `1.46` | 268,320,000.00 USD | 268,320,000.00 USD | 0.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.88B` | Total OI Tokens: `2,303,217,338.0 XRP`
  * 1h OI Change: `-1.22%` | 4h OI Change: `-2.93%` | 24h OI Change: `-3.31%`
  * Exchange Breakdown: Binance=`463.17M` | Bybit=`323.04M` | OKX=`100.29M` | Hyperliquid=`218.90M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-4.90K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0035%` | **USDT OKX** | `0.0013%` |
| **USDT Bybit** | `-0.0085%` | **USDT KuCoin** | `-0.0006%` |
| **USDT MEXC** | `0.0033%` | **USDT BingX** | `0.0034%` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `-0.0041%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `66.38%` | `33.62%` | `1.97` | 902,170,000.00 USD |
| `15M` | `Binance` | `55.24%` | `44.76%` | `1.23` | 225,150,000.00 USD |
| `15M` | `OKX` | `49.3%` | `50.7%` | `0.97` | 123,370,000.00 USD |
| `15M` | `Bybit` | `61.14%` | `38.86%` | `1.57` | 58,330,000.00 USD |
| `15M` | `KuCoin` | `66.8%` | `33.2%` | `2.01` | 6,810,000.00 USD |
| `15M` | `Gate` | `49.91%` | `50.09%` | `1.00` | 108,260,000.00 USD |
| `15M` | `Bitget` | `50.46%` | `49.54%` | `1.02` | 20,450,000.00 USD |
| `15M` | `BingX` | `47.55%` | `52.45%` | `0.91` | 6,070,000.00 USD |
| `15M` | `MEXC` | `58.49%` | `41.51%` | `1.41` | 33,440,000.00 USD |
| `15M` | `Bitunix` | `54.13%` | `45.87%` | `1.18` | 22,610,000.00 USD |
| `15M` | `Hyperliquid` | `50.03%` | `49.97%` | `1.00` | 17,450,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.93%` | `64.07%` | `0.56` | 1,080,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.58%` | `0.42%` | `237.10` | 244,080,000.00 USD |
| `15M` | `HTX` | `71.29%` | `28.71%` | `2.48` | 12,370,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `45.68%` | `54.32%` | `0.84` | 7,310,000.00 USD |
| `15M` | `Bitfinex` | `40.63%` | `59.37%` | `0.68` | 671,240.00 USD |
| `15M` | `Kraken` | `62.29%` | `37.71%` | `1.65` | 3,130,000.00 USD |
| `15M` | `Aster` | `62.4%` | `37.6%` | `1.66` | 3,090,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `69.45%` | `30.55%` | `2.27` | 8,490,000.00 USD |
| `15M` | `Whale Positions` | `55.24%` | `44.76%` | `1.23` | 225,150,000.00 USD |
| `15M` | `Global Accounts` | `66.38%` | `33.62%` | `1.97` | 902,170,000.00 USD |
| `1H` | `XRP` | `51.78%` | `48.22%` | `1.07` | 4,020,000,000.00 USD |
| `1H` | `Binance` | `48.11%` | `51.89%` | `0.93` | 1,100,000,000.00 USD |
| `1H` | `OKX` | `50.35%` | `49.65%` | `1.01` | 666,980,000.00 USD |
| `1H` | `Bybit` | `47.99%` | `52.01%` | `0.92` | 291,510,000.00 USD |
| `1H` | `KuCoin` | `61.45%` | `38.55%` | `1.59` | 24,130,000.00 USD |
| `1H` | `Gate` | `49.15%` | `50.85%` | `0.97` | 556,370,000.00 USD |
| `1H` | `Bitget` | `56.26%` | `43.74%` | `1.29` | 132,690,000.00 USD |
| `1H` | `BingX` | `45.07%` | `54.93%` | `0.82` | 31,200,000.00 USD |
| `1H` | `MEXC` | `48.4%` | `51.6%` | `0.94` | 198,280,000.00 USD |
| `1H` | `Bitunix` | `52.48%` | `47.52%` | `1.10` | 119,780,000.00 USD |
| `1H` | `Hyperliquid` | `42.52%` | `57.48%` | `0.74` | 268,040,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.33%` | `52.67%` | `0.90` | 9,210,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `83.47%` | `16.53%` | `5.05` | 398,890,000.00 USD |
| `1H` | `HTX` | `23.94%` | `76.06%` | `0.31` | 84,050,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `53.36%` | `46.64%` | `1.14` | 40,170,000.00 USD |
| `1H` | `Bitfinex` | `29.58%` | `70.42%` | `0.42` | 1,260,000.00 USD |
| `1H` | `Kraken` | `51.06%` | `48.94%` | `1.04` | 16,320,000.00 USD |
| `1H` | `Aster` | `45.67%` | `54.33%` | `0.84` | 22,530,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.32%` | `50.68%` | `0.97` | 58,780,000.00 USD |
| `1H` | `Whale Positions` | `48.11%` | `51.89%` | `0.93` | 1,100,000,000.00 USD |
| `1H` | `Global Accounts` | `51.78%` | `48.22%` | `1.07` | 4,020,000,000.00 USD |
| `4H` | `XRP` | `47.99%` | `52.01%` | `0.92` | 31,780,000,000.00 USD |
| `4H` | `Binance` | `45.65%` | `54.35%` | `0.84` | 8,760,000,000.00 USD |
| `4H` | `OKX` | `46.07%` | `53.93%` | `0.85` | 3,800,000,000.00 USD |
| `4H` | `Bybit` | `45.61%` | `54.39%` | `0.84` | 3,800,000,000.00 USD |
| `4H` | `KuCoin` | `54.57%` | `45.43%` | `1.20` | 130,930,000.00 USD |
| `4H` | `Gate` | `49.63%` | `50.37%` | `0.99` | 2,560,000,000.00 USD |
| `4H` | `Bitget` | `51.88%` | `48.12%` | `1.08` | 1,360,000,000.00 USD |
| `4H` | `BingX` | `49.6%` | `50.4%` | `0.98` | 379,080,000.00 USD |
| `4H` | `MEXC` | `48.65%` | `51.35%` | `0.95` | 1,330,000,000.00 USD |
| `4H` | `Bitunix` | `47.96%` | `52.04%` | `0.92` | 1,340,000,000.00 USD |
| `4H` | `Hyperliquid` | `46.53%` | `53.47%` | `0.87` | 2,050,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.8%` | `48.2%` | `1.07` | 135,720,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 148,280,000.00 USD |
| `4H` | `WhiteBIT` | `54.94%` | `45.06%` | `1.22` | 4,360,000,000.00 USD |
| `4H` | `HTX` | `35.11%` | `64.89%` | `0.54` | 98,280,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `49.86%` | `50.14%` | `0.99` | 592,720,000.00 USD |
| `4H` | `Bitfinex` | `27.34%` | `72.66%` | `0.38` | 36,630,000.00 USD |
| `4H` | `Kraken` | `49.67%` | `50.33%` | `0.99` | 282,810,000.00 USD |
| `4H` | `Aster` | `46.97%` | `53.03%` | `0.89` | 252,550,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.29%` | `50.71%` | `0.97` | 349,190,000.00 USD |
| `4H` | `Whale Positions` | `45.65%` | `54.35%` | `0.84` | 8,760,000,000.00 USD |
| `4H` | `Global Accounts` | `47.99%` | `52.01%` | `0.92` | 31,780,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.27` | 9,197,225.16 USD | 4,639,147.41 USD | 4,558,077.75 USD | 81,069.66 USD | `+0.88%` | `4B / 5S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.27` | `1.23` | 112,851,214.34 USD | 44,440,734.72 USD | 68,410,479.62 USD | -23,969,744.90 USD | `-21.24%` | `0B / 35S` |
| `5:00 UTC` | `1.24` | `1.24` | `1.24` | `1.25` | `1.22` | 96,971,024.45 USD | 46,182,833.37 USD | 50,788,191.08 USD | -4,605,357.71 USD | `-4.75%` | `1B / 8S` |
| `0:00 UTC` | `1.25` | `1.24` | `1.25` | `1.25` | `1.23` | 42,899,530.36 USD | 22,765,315.89 USD | 20,134,214.47 USD | 2,631,101.42 USD | `+6.13%` | `25B / 6S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 36,075,332.57 USD | 17,198,898.48 USD | 18,876,434.09 USD | -1,677,535.61 USD | `-4.65%` | `12B / 8S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 16,161,725.94 USD | 8,623,195.09 USD | 7,538,530.84 USD | 1,084,664.25 USD | `+6.71%` | `17B / 20S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 13,078,738.26 USD | 6,457,414.69 USD | 6,621,323.57 USD | -163,908.89 USD | `-1.25%` | `11B / 13S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 37,964,913.08 USD | 18,376,664.94 USD | 19,588,248.14 USD | -1,211,583.20 USD | `-3.19%` | `12B / 11S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 29,915,763.66 USD | 14,446,371.17 USD | 15,469,392.49 USD | -1,023,021.32 USD | `-3.42%` | `7B / 11S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 13,084,596.34 USD | 7,589,609.84 USD | 5,494,986.50 USD | 2,094,623.34 USD | `+16.01%` | `16B / 3S` |

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
| `5m` | -1,960,000.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -3,910,000.00 USD | -1,490,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -4,290,000.00 USD | -5,300,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -5,400,000.00 USD | -10,210,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -5,440,000.00 USD | -73,430,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -31,510,000.00 USD | -115,520,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -43,130,000.00 USD | -125,750,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -41,890,000.00 USD | -125,550,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -41,220,000.00 USD | -124,610,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -61,380,000.00 USD | -179,750,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -107,550,000.00 USD | -193,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -584,620,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.96M` | 15m=`-3.91M` | 1h=`-5.40M` | 24h=`-61.38M`
* Futures Capital Netflows: 5m=`-1.01M` | 15m=`-1.49M` | 1h=`-10.21M` | 24h=`-179.75M`
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
  * `2026-10-30 03:30:16 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:10:16 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.24` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.22` (Risk Distance: `0.0186` pts)
  * +2.5R Take Profit: `1.29`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0186` pts)
  * +2.5R Take Profit: `1.21`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
