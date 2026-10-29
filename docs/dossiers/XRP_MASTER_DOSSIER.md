# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 23:07:12 IST` (`2026-10-29 17:37:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.29` | **Live Ask Quote**: `1.30` | **Mid Price**: `1.29`
- **Spread Points**: `4.00` | **Spread BPS**: `30.91 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.30` | Lower -3.00σ Band: `1.28`
  * Upper +2.51σ Band: `1.30` | Lower -2.51σ Band: `1.29`
  * Upper +2.01σ Band: `1.30` | Lower -2.01σ Band: `1.29`
  * Upper +2.00σ Band: `1.30` | Lower -2.00σ Band: `1.29`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.29`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.29` | EMA-20=`1.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.29` (Slope: `+0.0000`) | EMA-100=`1.29`
  * Institutional Anchors: EMA-144=`1.29` | EMA-200=`1.29` (Slope: `+0.0000`) | EMA-233=`1.29`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.28` | Weekly High=`1.32` | Weekly Low=`1.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-0.33%`)
  * Point of Control (POC) = `1.29` (Distance: `+0.44%`)
  * Value Area Low (VAL) = `1.28` (Distance: `+0.83%`)
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
  * Structural Invalidation Anchor (0.786): `1.30`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.30` | `1.30` | `1.29` | `1.29` | `2,480,987` | 3,217,387.77 USD | 462,795.39 USD | `+14.38%` | -22,895,096.48 USD | `+0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.29` | `1.30` | `1.29` | `1.30` | `1,542,540` | 1,998,090.08 USD | -9,438.67 USD | `-0.47%` | -22,904,535.15 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `1.30` | `1.30` | `1.30` | `1.30` | `1,489,076` | 1,931,777.56 USD | 400,428.42 USD | `+20.73%` | -22,504,106.73 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.30` | `1.30` | `1.30` | `1.30` | `3,676,406` | 4,776,328.08 USD | 220,088.84 USD | `+4.61%` | -22,053,288.99 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.30` | `1.30` | `1.29` | `1.29` | `7,092,611` | 9,199,982.08 USD | -824,824.35 USD | `-8.97%` | -22,878,113.34 USD | `-0.61` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.29` | `1.30` | `1.29` | `1.30` | `3,005,758` | 3,896,328.05 USD | 357,813.31 USD | `+9.18%` | -22,520,300.02 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.31` | `1.30` | `1.31` | `30,464,520` | 39,839,799.06 USD | 106,608.94 USD | `+0.27%` | -19,101,925.36 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.31` | `1.32` | `1.30` | `1.30` | `30,534,069` | 39,864,527.69 USD | -3,664,960.48 USD | `-9.19%` | -22,766,885.83 USD | `-0.63` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.29` | `1.30` | `10,097,008` | 13,094,545.79 USD | -466,143.96 USD | `-3.56%` | -23,233,029.79 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.29` | `1.30` | `40,632,437` | 52,960,837.82 USD | -4,131,971.51 USD | `-7.80%` | -28,634,146.65 USD | `+0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.29` | `1.30` | `40,632,437` | 52,960,837.82 USD | -4,131,971.51 USD | `-7.80%` | -28,634,146.65 USD | `+0.08` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.29`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `1.29` | `75596.0000` | 97,896.82 USD | 178,320.36 USD | `14 orders` | `-0.03%` | `-` |
| `BID` | `1.29` | `15328.0000` | 19,848.23 USD | 198,168.59 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `1.29` | `130737.0000` | 169,278.27 USD | 367,446.85 USD | `17 orders` | `-0.05%` | `-` |
| `BID` | `1.29` | `69663.0000` | 90,192.69 USD | 457,639.54 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `1.29` | `294924.0000` | 381,808.61 USD | 839,448.15 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `1.29` | `67247.0000` | 87,051.24 USD | 926,499.39 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `1.29` | `52306.0000` | 67,704.89 USD | 994,204.28 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `1.29` | `116387.0000` | 150,639.69 USD | 1,144,843.97 USD | `15 orders` | `-0.09%` | `-` |
| `BID` | `1.29` | `93936.0000` | 121,571.97 USD | 1,266,415.94 USD | `16 orders` | `-0.10%` | `-` |
| `BID` | `1.29` | `45552.0000` | 58,948.84 USD | 1,325,364.79 USD | `11 orders` | `-0.10%` | `-` |
| `BID` | `1.29` | `287290.0000` | 371,753.26 USD | 1,697,118.05 USD | `10 orders` | `-0.11%` | `-` |
| `BID` | `1.29` | `552166.0000` | 714,447.59 USD | 2,411,565.63 USD | `11 orders` | `-0.12%` | `-` |
| `BID` | `1.29` | `64119.0000` | 82,957.16 USD | 2,494,522.80 USD | `8 orders` | `-0.13%` | `-` |
| `BID` | `1.29` | `80677.0000` | 104,371.83 USD | 2,598,894.63 USD | `11 orders` | `-0.14%` | `-` |
| `BID` | `1.29` | `25721.0000` | 33,272.69 USD | 2,632,167.32 USD | `8 orders` | `-0.14%` | `-` |
| `BID` | `1.29` | `159850.0000` | 206,765.98 USD | 2,838,933.29 USD | `6 orders` | `-0.15%` | `-` |
| `ASK` | `1.30` | `79929.0000` | 103,699.88 USD | 2,808,250.02 USD | `12 orders` | `+0.15%` | `-` |
| `ASK` | `1.30` | `326208.0000` | 423,189.64 USD | 2,704,550.14 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.30` | `35422.0000` | 45,949.42 USD | 2,281,360.50 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.30` | `91934.0000` | 119,247.59 USD | 2,235,411.08 USD | `12 orders` | `+0.13%` | `-` |
| `ASK` | `1.30` | `315899.0000` | 409,721.00 USD | 2,116,163.49 USD | `10 orders` | `+0.12%` | `-` |
| `ASK` | `1.30` | `28027.0000` | 36,348.22 USD | 1,706,442.49 USD | `7 orders` | `+0.11%` | `-` |
| `ASK` | `1.30` | `311944.0000` | 404,528.98 USD | 1,670,094.27 USD | `11 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `83596.0000` | 108,398.93 USD | 1,265,565.29 USD | `11 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `67117.0000` | 87,023.90 USD | 1,157,166.36 USD | `10 orders` | `+0.09%` | `-` |
| `ASK` | `1.30` | `121200.0000` | 157,135.80 USD | 1,070,142.46 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `1.30` | `13516.0000` | 17,522.14 USD | 913,006.66 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `338283.0000` | 438,516.25 USD | 895,484.51 USD | `12 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `64827.0000` | 84,028.76 USD | 456,968.26 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `1.30` | `68694.0000` | 89,034.29 USD | 372,939.50 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `1.30` | `67474.0000` | 87,446.30 USD | 283,905.21 USD | `14 orders` | `+0.04%` | `-` |
| `ASK` | `1.30` | `53919.0000` | 69,873.63 USD | 196,458.91 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `37220.0000` | 48,229.68 USD | 126,585.27 USD | `16 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `23527.0000` | 30,483.93 USD | 78,355.60 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `1.30` | `16440.0000` | 21,299.66 USD | 47,871.66 USD | `8 orders` | `+0.01%` | `-` |
| `ASK` | `1.30` | `20511.0000` | 26,572.00 USD | 26,572.00 USD | `6 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.30` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.30` | `0.00%` | `-` |
| `BID` | `1.30` | `11667.0000` | 15,113.43 USD | 15,113.43 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `1.30` | `13284.0000` | 17,206.77 USD | 32,320.20 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `1.30` | `7376.0000` | 9,553.40 USD | 41,873.59 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `1.30` | `29766.0000` | 38,549.95 USD | 80,423.54 USD | `7 orders` | `-0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 45,460,286.71 USD | `35,031,430.00` | `1.13` | `1.30` | `0.9611` | 5,881,403.44 USD | `+12.94%` | `10X Cross` |
| `91` | `0x5b5d...c060` | `SHORT` | 20,406,449.86 USD | `15,729,939.00` | `1.44` | `1.30` | `10.92` | 2,208,564.35 USD | `+10.82%` | `5X Cross` |
| `147` | `0x58f0...0d20` | `LONG` | 14,184,247.76 USD | `10,931,629.00` | `1.36` | `1.30` | `1.25` | -680,905.20 USD | `-4.80%` | `20X Cross` |
| `156` | `0xb83d...6e36` | `SHORT` | 13,693,585.29 USD | `10,555,450.00` | `1.50` | `1.30` | `13.30` | 2,128,984.36 USD | `+15.55%` | `5X Cross` |
| `445` | `0xca49...53c8` | `SHORT` | 5,368,962.92 USD | `4,138,886.00` | `1.44` | `1.30` | `4.31` | 584,359.81 USD | `+10.88%` | `20X Cross` |
| `462` | `0xfc27...9d9d` | `SHORT` | 5,136,134.24 USD | `3,959,608.00` | `1.31` | `1.30` | `4.80` | 69,072.64 USD | `+1.34%` | `20X Cross` |
| `516` | `0x610b...b613` | `LONG` | 4,597,337.88 USD | `3,543,946.00` | `1.44` | `1.30` | `0.6898` | -502,654.73 USD | `-10.93%` | `5X Cross` |
| `546` | `0xc30c...a4c9` | `SHORT` | 4,284,991.74 USD | `3,302,753.00` | `1.42` | `1.30` | `1.60` | 414,895.11 USD | `+9.68%` | `8X Cross` |
| `564` | `0xdd53...2b13` | `SHORT` | 4,189,783.43 USD | `3,229,618.00` | `1.44` | `1.30` | `18.29` | 458,601.67 USD | `+10.95%` | `3X Cross` |
| `605` | `0xecb6...2b00` | `SHORT` | 3,938,998.48 USD | `3,036,305.00` | `1.31` | `1.30` | `11.63` | 29,919.21 USD | `+0.76%` | `10X Cross` |
| `607` | `0x9946...0852` | `SHORT` | 3,924,476.50 USD | `3,025,111.00` | `1.43` | `1.30` | `1.62` | 388,708.06 USD | `+9.90%` | `20X Cross` |
| `698` | `0x9aa5...58af` | `SHORT` | 3,379,318.51 USD | `2,604,083.00` | `1.46` | `1.30` | `4.07` | 418,402.15 USD | `+12.38%` | `20X Cross` |
| `711` | `0xf48f...10fe` | `LONG` | 3,328,585.10 USD | `2,565,779.00` | `1.53` | `1.30` | `0.8908` | -596,055.63 USD | `-17.91%` | `4X Cross` |
| `728` | `0x023a...2355` | `SHORT` | 3,243,885.68 USD | `2,500,490.00` | `1.33` | `1.30` | `4.77` | 76,009.38 USD | `+2.34%` | `20X Cross` |
| `747` | `0x45d2...4029` | `SHORT` | 3,181,864.80 USD | `2,453,000.00` | `1.48` | `1.30` | `15.78` | 456,415.63 USD | `+14.34%` | `20X Cross` |
| `1012` | `0xc179...e0c8` | `SHORT` | 2,285,390.86 USD | `1,761,516.00` | `1.30` | `1.30` | `4.62` | 6,972.99 USD | `+0.31%` | `10X Cross` |
| `1081` | `0xeadc...9d55` | `LONG` | 2,101,765.02 USD | `1,619,805.00` | `1.21` | `1.30` | `0.000000` | 142,922.00 USD | `+6.80%` | `20X Cross` |
| `1083` | `0xfc66...ca06` | `SHORT` | 2,100,331.29 USD | `1,619,002.00` | `1.31` | `1.30` | `22.64` | 21,071.38 USD | `+1.00%` | `20X Cross` |
| `1145` | `0x94b2...599e` | `SHORT` | 1,999,117.77 USD | `1,540,696.00` | `1.36` | `1.30` | `1.82` | 101,348.68 USD | `+5.07%` | `20X Cross` |
| `1161` | `0xbcd4...0dd2` | `SHORT` | 1,984,169.76 USD | `1,529,461.00` | `1.31` | `1.30` | `2.21` | 20,374.84 USD | `+1.03%` | `20X Cross` |
| `1181` | `0x3fc5...c0c1` | `SHORT` | 1,961,230.90 USD | `1,511,779.00` | `1.52` | `1.30` | `2.58` | 330,383.71 USD | `+16.85%` | `20X Cross` |
| `1205` | `0x31ef...f715` | `LONG` | 1,913,768.79 USD | `1,475,080.00` | `1.49` | `1.30` | `1.04` | -285,496.61 USD | `-14.92%` | `3X Isolated` |
| `1261` | `0x7737...bf66` | `SHORT` | 1,834,254.83 USD | `1,413,466.00` | `1.41` | `1.30` | `14.43` | 164,613.82 USD | `+8.97%` | `10X Cross` |
| `1282` | `0xef96...9383` | `SHORT` | 1,804,682.10 USD | `1,390,999.00` | `1.34` | `1.30` | `3.92` | 59,103.12 USD | `+3.27%` | `20X Cross` |
| `1356` | `0xee2b...d67e` | `LONG` | 1,694,642.23 USD | `1,306,284.00` | `1.55` | `1.30` | `0.2194` | -336,012.67 USD | `-19.83%` | `4X Cross` |
| `1407` | `0x215d...f80a` | `LONG` | 1,624,431.01 USD | `1,251,777.00` | `1.32` | `1.30` | `1.19` | -30,023.21 USD | `-1.85%` | `14X Cross` |
| `1460` | `0x123d...3bff` | `LONG` | 1,576,646.31 USD | `1,215,329.00` | `1.35` | `1.30` | `0.000000` | -60,422.91 USD | `-3.83%` | `10X Cross` |
| `1509` | `0x95da...2328` | `LONG` | 1,520,481.77 USD | `1,171,817.00` | `1.37` | `1.30` | `0.000000` | -81,294.22 USD | `-5.35%` | `5X Cross` |
| `1518` | `0xdf95...7d72` | `SHORT` | 1,504,996.43 USD | `1,160,099.00` | `1.37` | `1.30` | `32.37` | 88,342.30 USD | `+5.87%` | `20X Cross` |
| `1583` | `0x5fa3...35b7` | `SHORT` | 1,428,779.38 USD | `1,101,009.00` | `1.31` | `1.30` | `3.00` | 13,069.16 USD | `+0.91%` | `20X Cross` |
| `1678` | `0xb1ce...681b` | `LONG` | 1,325,362.78 USD | `1,021,764.00` | `1.49` | `1.30` | `1.16` | -198,693.71 USD | `-14.99%` | `4X Isolated` |
| `1685` | `0x4537...8732` | `SHORT` | 1,322,194.09 USD | `1,018,875.00` | `1.32` | `1.30` | `2.24` | 18,622.81 USD | `+1.41%` | `10X Cross` |
| `1781` | `0x3c36...461a` | `LONG` | 1,219,622.17 USD | `940,051.00` | `1.30` | `1.30` | `1.06` | 541.55 USD | `+0.04%` | `10X Cross` |
| `2001` | `0xbfc7...80b4` | `SHORT` | 1,038,160.00 USD | `800,000.00` | `1.48` | `1.30` | `6.57` | 145,294.65 USD | `+14.00%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,782.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.78K USD at 1.3233 USD [API] | `2026-10-27 22:01:08` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,988.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.99K USD at 1.3234 USD [API] | `2026-10-27 22:01:08` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,801.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.80K USD at 1.3232 USD [API] | `2026-10-27 22:01:07` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 273.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.27K USD at 1.3255 USD [API] | `2026-10-27 15:24:40` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 18,012.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 18.01K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 15,118.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.12K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,482.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.48K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,542.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.54K USD at 1.3255 USD [API] | `2026-10-27 22:04:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,355.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.36K USD at 1.3251 USD [API] | `2026-10-27 22:07:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3254 USD [API] | `2026-10-27 22:07:01` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,415.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.42K USD at 1.3251 USD [API] | `2026-10-27 22:11:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 11,907.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.91K USD at 1.3251 USD [API] | `2026-10-27 22:11:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,416.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.42K USD at 1.3252 USD [API] | `2026-10-27 22:10:49` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,280.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.28K USD at 1.3268 USD [API] | `2026-10-27 22:18:23` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,006.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3269 USD [API] | `2026-10-27 22:18:23` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,049.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.05K USD at 1.3248 USD [API] | `2026-10-27 22:22:42` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,530.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.53K USD at 1.3234 USD [API] | `2026-10-27 22:27:14` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,697.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.70K USD at 1.3230 USD [API] | `2026-10-27 22:29:04` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 35,708.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 35.71K USD at 1.3223 USD [API] | `2026-10-27 22:30:20` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 25,123.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 25.12K USD at 1.3223 USD [API] | `2026-10-27 22:30:20` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,672.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.67K USD at 1.3241 USD [API] | `2026-10-27 22:35:15` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,149.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.15K USD at 1.3241 USD [API] | `2026-10-27 22:35:15` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,796.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.80K USD at 1.3262 USD [API] | `2026-10-27 22:53:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,200,000.00 USD, Dist: `+2.02%`) | Long MP=`1.28` (Vol: 2,900,000.00 USD, Dist: `--1.40%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+4.16%`) | Long MP=`1.28` (Vol: 2,900,000.00 USD, Dist: `--1.40%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,600,000.00 USD, Dist: `+4.16%`) | Long MP=`1.28` (Vol: 3,700,000.00 USD, Dist: `--0.93%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+4.24%`) | Long MP=`1.28` (Vol: 4,400,000.00 USD, Dist: `--0.98%`)
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
| `7D` | `Long Liquidation` | `1.16` | 222,460,000.00 USD | 222,460,000.00 USD | 100,770.00 USD | 64,860.00 USD | 127,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 108,390.00 USD | 23,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 222,160,000.00 USD | 222,160,000.00 USD | 173,190.00 USD | 99,350.00 USD | 396,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 221,490,000.00 USD | 221,490,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 221,060,000.00 USD | 221,060,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 220,040,000.00 USD | 220,040,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 82,150,000.00 USD | 82,150,000.00 USD | 354,980.00 USD | 112,400.00 USD | 267,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 218,670,000.00 USD | 218,670,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,680,000.00 USD | 23,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 81,410,000.00 USD | 81,410,000.00 USD | 121,620.00 USD | 93,470.00 USD | 82,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 218,040,000.00 USD | 218,040,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 81,120,000.00 USD | 81,120,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 216,660,000.00 USD | 216,660,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 80,940,000.00 USD | 80,940,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 215,150,000.00 USD | 215,150,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 80,770,000.00 USD | 80,770,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 213,770,000.00 USD | 213,770,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 80,550,000.00 USD | 80,550,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 212,970,000.00 USD | 212,970,000.00 USD | 290,470.00 USD | 92,530.00 USD | 505,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 806,220.00 USD | 21,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 80,280,000.00 USD | 80,280,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 212,080,000.00 USD | 212,080,000.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 80,060,000.00 USD | 80,060,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 211,580,000.00 USD | 211,580,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 79,880,000.00 USD | 79,880,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 210,690,000.00 USD | 210,690,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 79,800,000.00 USD | 79,800,000.00 USD | 25,860.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 210,190,000.00 USD | 210,190,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 79,720,000.00 USD | 79,720,000.00 USD | 53,340.00 USD | 30,330.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 210,050,000.00 USD | 210,050,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,650,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,590,000.00 USD | 79,590,000.00 USD | 28,500.00 USD | 37,670.00 USD | 53,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 209,440,000.00 USD | 209,440,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,470,000.00 USD | 79,470,000.00 USD | 58,560.00 USD | 17,340.00 USD | 62,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 208,830,000.00 USD | 208,830,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,330,000.00 USD | 79,330,000.00 USD | 37,540.00 USD | 238.88 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 208,170,000.00 USD | 208,170,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,270,000.00 USD | 79,270,000.00 USD | 28,700.00 USD | 18,150.00 USD | 84,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 207,710,000.00 USD | 207,710,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,140,000.00 USD | 79,140,000.00 USD | 130,470.00 USD | 44,250.00 USD | 113,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 207,040,000.00 USD | 207,040,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 477,200.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 78,850,000.00 USD | 78,850,000.00 USD | 89,360.00 USD | 18,340.00 USD | 72,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 206,340,000.00 USD | 206,340,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 78,670,000.00 USD | 78,670,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 206,050,000.00 USD | 206,050,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 78,540,000.00 USD | 78,540,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 205,900,000.00 USD | 205,900,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 78,490,000.00 USD | 78,490,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 205,830,000.00 USD | 205,830,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 205,520,000.00 USD | 205,520,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 656,350.00 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 78,360,000.00 USD | 78,360,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 205,430,000.00 USD | 205,430,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 78,350,000.00 USD | 78,350,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 205,330,000.00 USD | 205,330,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 204,570,000.00 USD | 204,570,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 203,890,000.00 USD | 203,890,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 203,520,000.00 USD | 203,520,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 355,520.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 203,480,000.00 USD | 203,480,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 203,380,000.00 USD | 203,380,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 203,340,000.00 USD | 203,340,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 203,270,000.00 USD | 203,270,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 202,860,000.00 USD | 202,860,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,680,000.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 201,820,000.00 USD | 201,820,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 201,290,000.00 USD | 201,290,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 200,740,000.00 USD | 200,740,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 199,950,000.00 USD | 199,950,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 78,320,000.00 USD | 78,320,000.00 USD | 11,570.00 USD | 989.25 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 198,630,000.00 USD | 198,630,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 401,010.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 78,310,000.00 USD | 78,310,000.00 USD | 461,130.00 USD | 120,320.00 USD | 258,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 194,830,000.00 USD | 194,830,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 77,470,000.00 USD | 77,470,000.00 USD | 1,040,000.00 USD | 649,220.00 USD | 709,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 190,440,000.00 USD | 190,440,000.00 USD | 1,890,000.00 USD | 930,140.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 75,070,000.00 USD | 75,070,000.00 USD | 892,170.00 USD | 405,360.00 USD | 708,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 185,360,000.00 USD | 185,360,000.00 USD | 1,980,000.00 USD | 633,060.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 73,060,000.00 USD | 73,060,000.00 USD | 297,370.00 USD | 172,840.00 USD | 341,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 180,180,000.00 USD | 180,180,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 72,250,000.00 USD | 72,250,000.00 USD | 368,310.00 USD | 122,390.00 USD | 420,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 177,370,000.00 USD | 177,370,000.00 USD | 2,160,000.00 USD | 376,950.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 13,870,000.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 71,340,000.00 USD | 71,340,000.00 USD | 522,930.00 USD | 129,710.00 USD | 130,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 173,010,000.00 USD | 173,010,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 70,560,000.00 USD | 70,560,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 164,400,000.00 USD | 164,400,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 69,880,000.00 USD | 69,880,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 157,280,000.00 USD | 157,280,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 69,150,000.00 USD | 69,150,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 151,550,000.00 USD | 151,550,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 68,280,000.00 USD | 68,280,000.00 USD | 131,220.00 USD | 41,890.00 USD | 312,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 148,150,000.00 USD | 148,150,000.00 USD | 625,270.00 USD | 526,820.00 USD | 776,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 641,680.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 67,790,000.00 USD | 67,790,000.00 USD | 266,880.00 USD | 47,170.00 USD | 116,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 146,220,000.00 USD | 146,220,000.00 USD | 370,280.00 USD | 446,010.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 67,360,000.00 USD | 67,360,000.00 USD | 222,740.00 USD | 104,190.00 USD | 319,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 145,060,000.00 USD | 145,060,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 890,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 66,710,000.00 USD | 66,710,000.00 USD | 293,150.00 USD | 71,910.00 USD | 164,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 142,530,000.00 USD | 142,530,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 66,180,000.00 USD | 66,180,000.00 USD | 890,560.00 USD | 254,090.00 USD | 554,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 139,080,000.00 USD | 139,080,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 64,480,000.00 USD | 64,480,000.00 USD | 2,160,000.00 USD | 1,360,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 132,470,000.00 USD | 132,470,000.00 USD | 3,640,000.00 USD | 1,750,000.00 USD | 4,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 464,620.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 59,390,000.00 USD | 59,390,000.00 USD | 1,930,000.00 USD | 923,130.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 122,620,000.00 USD | 122,620,000.00 USD | 3,940,000.00 USD | 1,540,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 54,790,000.00 USD | 54,790,000.00 USD | 767,190.00 USD | 356,380.00 USD | 750,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 110,710,000.00 USD | 110,710,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 52,910,000.00 USD | 52,910,000.00 USD | 859,780.00 USD | 291,610.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 104,810,000.00 USD | 104,810,000.00 USD | 4,070,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 50,730,000.00 USD | 50,730,000.00 USD | 1,280,000.00 USD | 332,670.00 USD | 502,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 94,980,000.00 USD | 94,980,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 9,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 48,610,000.00 USD | 48,610,000.00 USD | 1,460,000.00 USD | 569,500.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 78,420,000.00 USD | 78,420,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 479,930.00 USD | 598,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.28` | 45,290,000.00 USD | 45,290,000.00 USD | 2,850,000.00 USD | 1,230,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 65,900,000.00 USD | 65,900,000.00 USD | 6,760,000.00 USD | 2,990,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 38,800,000.00 USD | 38,800,000.00 USD | 6,020,000.00 USD | 2,660,000.00 USD | 4,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 47,800,000.00 USD | 47,800,000.00 USD | 4,830,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 25,710,000.00 USD | 25,710,000.00 USD | 2,270,000.00 USD | 1,150,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 35,000,000.00 USD | 35,000,000.00 USD | 4,610,000.00 USD | 1,440,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 19,380,000.00 USD | 19,380,000.00 USD | 1,310,000.00 USD | 1,040,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 25,110,000.00 USD | 25,110,000.00 USD | 3,450,000.00 USD | 2,130,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 15,640,000.00 USD | 15,640,000.00 USD | 2,400,000.00 USD | 530,190.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 17,040,000.00 USD | 17,040,000.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 118,740.00 USD | 118,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.29` | 11,070,000.00 USD | 11,070,000.00 USD | 1,390,000.00 USD | 327,360.00 USD | 975,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 7,540,000.00 USD | 7,540,000.00 USD | 724,970.00 USD | 0.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 8,370,000.00 USD | 8,370,000.00 USD | 369,910.00 USD | 183,710.00 USD | 305,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 7,510,000.00 USD | 7,510,000.00 USD | 312,060.00 USD | 127,400.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 3,120,000.00 USD | 3,120,000.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 5,520,000.00 USD | 5,520,000.00 USD | 1,400,000.00 USD | 68,880.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 213,200.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.29` | 1,940,000.00 USD | 1,940,000.00 USD | 807,360.00 USD | 167,570.00 USD | 238,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 747,810.00 USD | 747,810.00 USD | 440,550.00 USD | 0.00 USD | 307,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.30` | 731,690.00 USD | 731,690.00 USD | 0.00 USD | 597,860.00 USD | 133,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 389,370.00 USD | 389,370.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 778,740.00 USD | 778,740.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 168,250.00 USD | 168,250.00 USD | 0.00 USD | 168,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 1,340,000.00 USD | 1,340,000.00 USD | 327,930.00 USD | 841,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 5,180,000.00 USD | 5,180,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 5,720,000.00 USD | 5,720,000.00 USD | 543,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 2,590,000.00 USD | 2,590,000.00 USD | 515,020.00 USD | 344,570.00 USD | 388,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 8,100,000.00 USD | 8,100,000.00 USD | 704,520.00 USD | 318,670.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 5,290,000.00 USD | 5,290,000.00 USD | 1,570,000.00 USD | 443,660.00 USD | 682,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 10,460,000.00 USD | 10,460,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 6,310,000.00 USD | 6,310,000.00 USD | 355,560.00 USD | 483,320.00 USD | 181,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 12,870,000.00 USD | 12,870,000.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 4,840.00 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 12,400,000.00 USD | 12,400,000.00 USD | 116,540.00 USD | 1,800,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 17,410,000.00 USD | 17,410,000.00 USD | 1,120,000.00 USD | 1,120,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 19,040,000.00 USD | 19,040,000.00 USD | 2,240,000.00 USD | 879,590.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 20,340,000.00 USD | 20,340,000.00 USD | 755,330.00 USD | 406,240.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 22,430,000.00 USD | 22,430,000.00 USD | 1,620,000.00 USD | 711,160.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 21,910,000.00 USD | 21,910,000.00 USD | 966,720.00 USD | 235,180.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 26,750,000.00 USD | 26,750,000.00 USD | 1,820,000.00 USD | 981,550.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 25,950,000.00 USD | 25,950,000.00 USD | 1,980,000.00 USD | 761,100.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 29,640,000.00 USD | 29,640,000.00 USD | 1,720,000.00 USD | 259,410.00 USD | 905,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 28,320,000.00 USD | 28,320,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 22,430.00 USD | 27,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 31,890,000.00 USD | 31,890,000.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 28,850,000.00 USD | 28,850,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 34,080,000.00 USD | 34,080,000.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 30,010,000.00 USD | 30,010,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 36,470,000.00 USD | 36,470,000.00 USD | 822,840.00 USD | 283,020.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 31,730,000.00 USD | 31,730,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 37,980,000.00 USD | 37,980,000.00 USD | 262,430.00 USD | 248,670.00 USD | 999,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 33,670,000.00 USD | 33,670,000.00 USD | 830,370.00 USD | 108,920.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 39,390,000.00 USD | 39,390,000.00 USD | 819,570.00 USD | 94,350.00 USD | 492,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 34,170,000.00 USD | 34,170,000.00 USD | 109,550.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 57,610.00 USD | 84,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 41,680,000.00 USD | 41,680,000.00 USD | 842,300.00 USD | 333,220.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 35,800,000.00 USD | 35,800,000.00 USD | 679,750.00 USD | 645,230.00 USD | 312,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 44,370,000.00 USD | 44,370,000.00 USD | 1,220,000.00 USD | 398,480.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 37,910,000.00 USD | 37,910,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 48,220,000.00 USD | 48,220,000.00 USD | 1,680,000.00 USD | 549,090.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 42,630,000.00 USD | 42,630,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 51,870,000.00 USD | 51,870,000.00 USD | 1,580,000.00 USD | 863,920.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 48,330,000.00 USD | 48,330,000.00 USD | 1,730,000.00 USD | 2,830,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 56,280,000.00 USD | 56,280,000.00 USD | 2,360,000.00 USD | 675,180.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 59,520,000.00 USD | 59,520,000.00 USD | 3,700,000.00 USD | 1,880,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 163,410.00 USD | 248,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 58,690,000.00 USD | 58,690,000.00 USD | 997,910.00 USD | 469,060.00 USD | 940,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 67,270,000.00 USD | 67,270,000.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 60,570,000.00 USD | 60,570,000.00 USD | 915,920.00 USD | 263,070.00 USD | 702,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 77,770,000.00 USD | 77,770,000.00 USD | 4,410,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 63,260,000.00 USD | 63,260,000.00 USD | 1,140,000.00 USD | 329,530.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 85,540,000.00 USD | 85,540,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 64,670,000.00 USD | 64,670,000.00 USD | 558,120.00 USD | 208,670.00 USD | 646,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 93,860,000.00 USD | 93,860,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 67,020,000.00 USD | 67,020,000.00 USD | 935,850.00 USD | 363,450.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 102,090,000.00 USD | 102,090,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 252,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 69,330,000.00 USD | 69,330,000.00 USD | 911,460.00 USD | 199,730.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 106,170,000.00 USD | 106,170,000.00 USD | 1,320,000.00 USD | 881,730.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 70,680,000.00 USD | 70,680,000.00 USD | 812,050.00 USD | 113,780.00 USD | 425,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 110,030,000.00 USD | 110,030,000.00 USD | 1,490,000.00 USD | 693,390.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 71,490,000.00 USD | 71,490,000.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 112,530,000.00 USD | 112,530,000.00 USD | 671,910.00 USD | 581,640.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 72,450,000.00 USD | 72,450,000.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 116,930,000.00 USD | 116,930,000.00 USD | 2,100,000.00 USD | 918,100.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 73,100,000.00 USD | 73,100,000.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 118,840,000.00 USD | 118,840,000.00 USD | 664,020.00 USD | 328,930.00 USD | 923,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 201,820.00 USD | 454,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 73,290,000.00 USD | 73,290,000.00 USD | 65,890.00 USD | 0.00 USD | 124,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 119,340,000.00 USD | 119,340,000.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 73,530,000.00 USD | 73,530,000.00 USD | 106,670.00 USD | 85,720.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 121,130,000.00 USD | 121,130,000.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 74,030,000.00 USD | 74,030,000.00 USD | 120,300.00 USD | 65,300.00 USD | 315,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 122,530,000.00 USD | 122,530,000.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 74,620,000.00 USD | 74,620,000.00 USD | 147,360.00 USD | 112,420.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 125,390,000.00 USD | 125,390,000.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 74,870,000.00 USD | 74,870,000.00 USD | 172,450.00 USD | 10,690.00 USD | 66,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 127,080,000.00 USD | 127,080,000.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 75,230,000.00 USD | 75,230,000.00 USD | 123,150.00 USD | 46,840.00 USD | 190,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 128,700,000.00 USD | 128,700,000.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 75,790,000.00 USD | 75,790,000.00 USD | 235,940.00 USD | 73,260.00 USD | 241,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 130,630,000.00 USD | 130,630,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 76,560,000.00 USD | 76,560,000.00 USD | 379,220.00 USD | 102,400.00 USD | 295,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 133,180,000.00 USD | 133,180,000.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 77,080,000.00 USD | 77,080,000.00 USD | 241,850.00 USD | 53,840.00 USD | 224,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 134,270,000.00 USD | 134,270,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 77,520,000.00 USD | 77,520,000.00 USD | 340,420.00 USD | 35,940.00 USD | 56,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 135,370,000.00 USD | 135,370,000.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,530.00 USD | 485,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 77,710,000.00 USD | 77,710,000.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 135,860,000.00 USD | 135,860,000.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 77,860,000.00 USD | 77,860,000.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 136,950,000.00 USD | 136,950,000.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 78,120,000.00 USD | 78,120,000.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 137,110,000.00 USD | 137,110,000.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 137,430,000.00 USD | 137,430,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 78,140,000.00 USD | 78,140,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 137,580,000.00 USD | 137,580,000.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,740.00 USD | 497,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 78,240,000.00 USD | 78,240,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 137,590,000.00 USD | 137,590,000.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 137,600,000.00 USD | 137,600,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 137,740,000.00 USD | 137,740,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 137,860,000.00 USD | 137,860,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 138,100,000.00 USD | 138,100,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 952.59 USD | 498,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 138,260,000.00 USD | 138,260,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 138,430,000.00 USD | 138,430,000.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 138,590,000.00 USD | 138,590,000.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 78,240,000.00 USD | 78,240,000.00 USD | 0.00 USD | 158.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 138,760,000.00 USD | 138,760,000.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 78,250,000.00 USD | 78,250,000.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 139,250,000.00 USD | 139,250,000.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 502,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 78,360,000.00 USD | 78,360,000.00 USD | 60,530.00 USD | 27,040.00 USD | 25,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 139,680,000.00 USD | 139,680,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 78,690,000.00 USD | 78,690,000.00 USD | 176,350.00 USD | 69,160.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 140,710,000.00 USD | 140,710,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 79,400,000.00 USD | 79,400,000.00 USD | 362,640.00 USD | 148,060.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 142,080,000.00 USD | 142,080,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 79,810,000.00 USD | 79,810,000.00 USD | 157,740.00 USD | 72,390.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 142,710,000.00 USD | 142,710,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 79,890,000.00 USD | 79,890,000.00 USD | 9,670.00 USD | 54,730.00 USD | 21,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 143,070,000.00 USD | 143,070,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 95,360.00 USD | 597,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 80,110,000.00 USD | 80,110,000.00 USD | 111,940.00 USD | 38,740.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 144,090,000.00 USD | 144,090,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 80,280,000.00 USD | 80,280,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 145,590,000.00 USD | 145,590,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 80,450,000.00 USD | 80,450,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 146,980,000.00 USD | 146,980,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 80,670,000.00 USD | 80,670,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 147,780,000.00 USD | 147,780,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 80,940,000.00 USD | 80,940,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 148,310,000.00 USD | 148,310,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 181,920.00 USD | 779,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.44` | 81,070,000.00 USD | 81,070,000.00 USD | 21,660.00 USD | 0.00 USD | 105,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 148,670,000.00 USD | 148,670,000.00 USD | 74,670.00 USD | 68,640.00 USD | 215,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 81,160,000.00 USD | 81,160,000.00 USD | 47,660.00 USD | 16,990.00 USD | 30,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 149,160,000.00 USD | 149,160,000.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 81,340,000.00 USD | 81,340,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 150,050,000.00 USD | 150,050,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 81,420,000.00 USD | 81,420,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 150,560,000.00 USD | 150,560,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 81,510,000.00 USD | 81,510,000.00 USD | 25,860.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 150,700,000.00 USD | 150,700,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 11,390.00 USD | 790,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.45` | 81,550,000.00 USD | 81,550,000.00 USD | 1,080.00 USD | 22,830.00 USD | 16,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 150,830,000.00 USD | 150,830,000.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 81,630,000.00 USD | 81,630,000.00 USD | 52,260.00 USD | 7,500.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 151,300,000.00 USD | 151,300,000.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 81,750,000.00 USD | 81,750,000.00 USD | 28,500.00 USD | 37,670.00 USD | 53,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 151,900,000.00 USD | 151,900,000.00 USD | 190,550.00 USD | 38,510.00 USD | 370,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 81,880,000.00 USD | 81,880,000.00 USD | 46,680.00 USD | 17,340.00 USD | 62,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 152,530,000.00 USD | 152,530,000.00 USD | 161,500.00 USD | 127,370.00 USD | 338,310.00 USD | `Tier 1 CEX` |
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
| `7D` | `1.16` | 222,460,000.00 USD | 0.00 USD | 222,460,000.00 USD | 100,770.00 USD | 64,860.00 USD | 127,210.00 USD |
| `7D` | `1.16` | 222,160,000.00 USD | 0.00 USD | 222,160,000.00 USD | 173,190.00 USD | 99,350.00 USD | 396,520.00 USD |
| `7D` | `1.16` | 221,490,000.00 USD | 0.00 USD | 221,490,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `7D` | `1.16` | 221,060,000.00 USD | 0.00 USD | 221,060,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.16` | 220,040,000.00 USD | 0.00 USD | 220,040,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 82,150,000.00 USD | 0.00 USD | 82,150,000.00 USD | 354,980.00 USD | 112,400.00 USD | 267,840.00 USD |
| `7D` | `1.17` | 218,670,000.00 USD | 0.00 USD | 218,670,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 81,410,000.00 USD | 0.00 USD | 81,410,000.00 USD | 121,620.00 USD | 93,470.00 USD | 82,960.00 USD |
| `7D` | `1.17` | 218,040,000.00 USD | 0.00 USD | 218,040,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 81,120,000.00 USD | 0.00 USD | 81,120,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 216,660,000.00 USD | 0.00 USD | 216,660,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 80,940,000.00 USD | 0.00 USD | 80,940,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 215,150,000.00 USD | 0.00 USD | 215,150,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 80,770,000.00 USD | 0.00 USD | 80,770,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 213,770,000.00 USD | 0.00 USD | 213,770,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.17` | 80,550,000.00 USD | 0.00 USD | 80,550,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.18` | 212,970,000.00 USD | 0.00 USD | 212,970,000.00 USD | 290,470.00 USD | 92,530.00 USD | 505,430.00 USD |
| `1D` | `1.18` | 80,280,000.00 USD | 0.00 USD | 80,280,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 212,080,000.00 USD | 0.00 USD | 212,080,000.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 80,060,000.00 USD | 0.00 USD | 80,060,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 211,580,000.00 USD | 0.00 USD | 211,580,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD |
| `1D` | `1.18` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 210,690,000.00 USD | 0.00 USD | 210,690,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD |
| `1D` | `1.18` | 79,800,000.00 USD | 0.00 USD | 79,800,000.00 USD | 25,860.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 210,190,000.00 USD | 0.00 USD | 210,190,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.18` | 79,720,000.00 USD | 0.00 USD | 79,720,000.00 USD | 53,340.00 USD | 30,330.00 USD | 44,280.00 USD |
| `7D` | `1.19` | 210,050,000.00 USD | 0.00 USD | 210,050,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD |
| `1D` | `1.19` | 79,590,000.00 USD | 0.00 USD | 79,590,000.00 USD | 28,500.00 USD | 37,670.00 USD | 53,040.00 USD |
| `7D` | `1.19` | 209,440,000.00 USD | 0.00 USD | 209,440,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD |
| `1D` | `1.19` | 79,470,000.00 USD | 0.00 USD | 79,470,000.00 USD | 58,560.00 USD | 17,340.00 USD | 62,510.00 USD |
| `7D` | `1.19` | 208,830,000.00 USD | 0.00 USD | 208,830,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD |
| `1D` | `1.19` | 79,330,000.00 USD | 0.00 USD | 79,330,000.00 USD | 37,540.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 208,170,000.00 USD | 0.00 USD | 208,170,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `1D` | `1.19` | 79,270,000.00 USD | 0.00 USD | 79,270,000.00 USD | 28,700.00 USD | 18,150.00 USD | 84,160.00 USD |
| `7D` | `1.19` | 207,710,000.00 USD | 0.00 USD | 207,710,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 79,140,000.00 USD | 0.00 USD | 79,140,000.00 USD | 130,470.00 USD | 44,250.00 USD | 113,180.00 USD |
| `7D` | `1.20` | 207,040,000.00 USD | 0.00 USD | 207,040,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 78,850,000.00 USD | 0.00 USD | 78,850,000.00 USD | 89,360.00 USD | 18,340.00 USD | 72,750.00 USD |
| `7D` | `1.20` | 206,340,000.00 USD | 0.00 USD | 206,340,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 78,670,000.00 USD | 0.00 USD | 78,670,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD |
| `7D` | `1.20` | 206,050,000.00 USD | 0.00 USD | 206,050,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD |
| `1D` | `1.20` | 78,540,000.00 USD | 0.00 USD | 78,540,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 205,900,000.00 USD | 0.00 USD | 205,900,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 78,490,000.00 USD | 0.00 USD | 78,490,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 205,830,000.00 USD | 0.00 USD | 205,830,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD |
| `7D` | `1.21` | 205,520,000.00 USD | 0.00 USD | 205,520,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 78,360,000.00 USD | 0.00 USD | 78,360,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 205,430,000.00 USD | 0.00 USD | 205,430,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 78,350,000.00 USD | 0.00 USD | 78,350,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 205,330,000.00 USD | 0.00 USD | 205,330,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD |
| `7D` | `1.21` | 204,570,000.00 USD | 0.00 USD | 204,570,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD |
| `7D` | `1.21` | 203,890,000.00 USD | 0.00 USD | 203,890,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD |
| `7D` | `1.22` | 203,520,000.00 USD | 0.00 USD | 203,520,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD |
| `7D` | `1.22` | 203,480,000.00 USD | 0.00 USD | 203,480,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 203,380,000.00 USD | 0.00 USD | 203,380,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD |
| `7D` | `1.22` | 203,340,000.00 USD | 0.00 USD | 203,340,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD |
| `7D` | `1.22` | 203,270,000.00 USD | 0.00 USD | 203,270,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD |
| `7D` | `1.23` | 202,860,000.00 USD | 0.00 USD | 202,860,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD |
| `7D` | `1.23` | 201,820,000.00 USD | 0.00 USD | 201,820,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD |
| `7D` | `1.23` | 201,290,000.00 USD | 0.00 USD | 201,290,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD |
| `7D` | `1.23` | 200,740,000.00 USD | 0.00 USD | 200,740,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD |
| `7D` | `1.23` | 199,950,000.00 USD | 0.00 USD | 199,950,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD |
| `1D` | `1.23` | 78,320,000.00 USD | 0.00 USD | 78,320,000.00 USD | 11,570.00 USD | 989.25 USD | 1,410.00 USD |
| `7D` | `1.24` | 198,630,000.00 USD | 0.00 USD | 198,630,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD |
| `1D` | `1.24` | 78,310,000.00 USD | 0.00 USD | 78,310,000.00 USD | 461,130.00 USD | 120,320.00 USD | 258,880.00 USD |
| `7D` | `1.24` | 194,830,000.00 USD | 0.00 USD | 194,830,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD |
| `1D` | `1.24` | 77,470,000.00 USD | 0.00 USD | 77,470,000.00 USD | 1,040,000.00 USD | 649,220.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 190,440,000.00 USD | 0.00 USD | 190,440,000.00 USD | 1,890,000.00 USD | 930,140.00 USD | 2,250,000.00 USD |
| `1D` | `1.24` | 75,070,000.00 USD | 0.00 USD | 75,070,000.00 USD | 892,170.00 USD | 405,360.00 USD | 708,470.00 USD |
| `7D` | `1.24` | 185,360,000.00 USD | 0.00 USD | 185,360,000.00 USD | 1,980,000.00 USD | 633,060.00 USD | 2,560,000.00 USD |
| `1D` | `1.24` | 73,060,000.00 USD | 0.00 USD | 73,060,000.00 USD | 297,370.00 USD | 172,840.00 USD | 341,680.00 USD |
| `7D` | `1.24` | 180,180,000.00 USD | 0.00 USD | 180,180,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,100,000.00 USD |
| `1D` | `1.24` | 72,250,000.00 USD | 0.00 USD | 72,250,000.00 USD | 368,310.00 USD | 122,390.00 USD | 420,220.00 USD |
| `7D` | `1.25` | 177,370,000.00 USD | 0.00 USD | 177,370,000.00 USD | 2,160,000.00 USD | 376,950.00 USD | 1,810,000.00 USD |
| `1D` | `1.25` | 71,340,000.00 USD | 0.00 USD | 71,340,000.00 USD | 522,930.00 USD | 129,710.00 USD | 130,470.00 USD |
| `7D` | `1.25` | 173,010,000.00 USD | 0.00 USD | 173,010,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD |
| `1D` | `1.25` | 70,560,000.00 USD | 0.00 USD | 70,560,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD |
| `7D` | `1.25` | 164,400,000.00 USD | 0.00 USD | 164,400,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD |
| `1D` | `1.25` | 69,880,000.00 USD | 0.00 USD | 69,880,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 157,280,000.00 USD | 0.00 USD | 157,280,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD |
| `1D` | `1.25` | 69,150,000.00 USD | 0.00 USD | 69,150,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 151,550,000.00 USD | 0.00 USD | 151,550,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD |
| `1D` | `1.25` | 68,280,000.00 USD | 0.00 USD | 68,280,000.00 USD | 131,220.00 USD | 41,890.00 USD | 312,160.00 USD |
| `7D` | `1.25` | 148,150,000.00 USD | 0.00 USD | 148,150,000.00 USD | 625,270.00 USD | 526,820.00 USD | 776,740.00 USD |
| `1D` | `1.26` | 67,790,000.00 USD | 0.00 USD | 67,790,000.00 USD | 266,880.00 USD | 47,170.00 USD | 116,960.00 USD |
| `7D` | `1.26` | 146,220,000.00 USD | 0.00 USD | 146,220,000.00 USD | 370,280.00 USD | 446,010.00 USD | 344,360.00 USD |
| `1D` | `1.26` | 67,360,000.00 USD | 0.00 USD | 67,360,000.00 USD | 222,740.00 USD | 104,190.00 USD | 319,670.00 USD |
| `7D` | `1.26` | 145,060,000.00 USD | 0.00 USD | 145,060,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 890,430.00 USD |
| `1D` | `1.26` | 66,710,000.00 USD | 0.00 USD | 66,710,000.00 USD | 293,150.00 USD | 71,910.00 USD | 164,680.00 USD |
| `7D` | `1.26` | 142,530,000.00 USD | 0.00 USD | 142,530,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD |
| `1D` | `1.26` | 66,180,000.00 USD | 0.00 USD | 66,180,000.00 USD | 890,560.00 USD | 254,090.00 USD | 554,880.00 USD |
| `7D` | `1.26` | 139,080,000.00 USD | 0.00 USD | 139,080,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD |
| `1D` | `1.26` | 64,480,000.00 USD | 0.00 USD | 64,480,000.00 USD | 2,160,000.00 USD | 1,360,000.00 USD | 1,570,000.00 USD |
| `7D` | `1.26` | 132,470,000.00 USD | 0.00 USD | 132,470,000.00 USD | 3,640,000.00 USD | 1,750,000.00 USD | 4,470,000.00 USD |
| `1D` | `1.27` | 59,390,000.00 USD | 0.00 USD | 59,390,000.00 USD | 1,930,000.00 USD | 923,130.00 USD | 1,750,000.00 USD |
| `7D` | `1.27` | 122,620,000.00 USD | 0.00 USD | 122,620,000.00 USD | 3,940,000.00 USD | 1,540,000.00 USD | 6,430,000.00 USD |
| `1D` | `1.27` | 54,790,000.00 USD | 0.00 USD | 54,790,000.00 USD | 767,190.00 USD | 356,380.00 USD | 750,220.00 USD |
| `7D` | `1.27` | 110,710,000.00 USD | 0.00 USD | 110,710,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 2,410,000.00 USD |
| `1D` | `1.27` | 52,910,000.00 USD | 0.00 USD | 52,910,000.00 USD | 859,780.00 USD | 291,610.00 USD | 1,030,000.00 USD |
| `7D` | `1.27` | 104,810,000.00 USD | 0.00 USD | 104,810,000.00 USD | 4,070,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD |
| `1D` | `1.27` | 50,730,000.00 USD | 0.00 USD | 50,730,000.00 USD | 1,280,000.00 USD | 332,670.00 USD | 502,270.00 USD |
| `7D` | `1.27` | 94,980,000.00 USD | 0.00 USD | 94,980,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 9,250,000.00 USD |
| `1D` | `1.27` | 48,610,000.00 USD | 0.00 USD | 48,610,000.00 USD | 1,460,000.00 USD | 569,500.00 USD | 1,290,000.00 USD |
| `7D` | `1.27` | 78,420,000.00 USD | 0.00 USD | 78,420,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD |
| `1D` | `1.28` | 45,290,000.00 USD | 0.00 USD | 45,290,000.00 USD | 2,850,000.00 USD | 1,230,000.00 USD | 2,410,000.00 USD |
| `7D` | `1.28` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 6,760,000.00 USD | 2,990,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 38,800,000.00 USD | 0.00 USD | 38,800,000.00 USD | 6,020,000.00 USD | 2,660,000.00 USD | 4,410,000.00 USD |
| `7D` | `1.28` | 47,800,000.00 USD | 0.00 USD | 47,800,000.00 USD | 4,830,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD |
| `1D` | `1.28` | 25,710,000.00 USD | 0.00 USD | 25,710,000.00 USD | 2,270,000.00 USD | 1,150,000.00 USD | 2,910,000.00 USD |
| `7D` | `1.28` | 35,000,000.00 USD | 0.00 USD | 35,000,000.00 USD | 4,610,000.00 USD | 1,440,000.00 USD | 3,850,000.00 USD |
| `1D` | `1.28` | 19,380,000.00 USD | 0.00 USD | 19,380,000.00 USD | 1,310,000.00 USD | 1,040,000.00 USD | 1,400,000.00 USD |
| `7D` | `1.28` | 25,110,000.00 USD | 0.00 USD | 25,110,000.00 USD | 3,450,000.00 USD | 2,130,000.00 USD | 2,480,000.00 USD |
| `1D` | `1.28` | 15,640,000.00 USD | 0.00 USD | 15,640,000.00 USD | 2,400,000.00 USD | 530,190.00 USD | 1,640,000.00 USD |
| `7D` | `1.28` | 17,040,000.00 USD | 0.00 USD | 17,040,000.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 4,130,000.00 USD |
| `1D` | `1.29` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 1,390,000.00 USD | 327,360.00 USD | 975,970.00 USD |
| `7D` | `1.29` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 724,970.00 USD | 0.00 USD | 3,030,000.00 USD |
| `1D` | `1.29` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 369,910.00 USD | 183,710.00 USD | 305,580.00 USD |
| `7D` | `1.29` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD |
| `1D` | `1.29` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 312,060.00 USD | 127,400.00 USD | 1,550,000.00 USD |
| `7D` | `1.29` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD |
| `1D` | `1.29` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 1,400,000.00 USD | 68,880.00 USD | 2,110,000.00 USD |
| `7D` | `1.29` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 213,200.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 807,360.00 USD | 167,570.00 USD | 238,060.00 USD |
| `7D` | `1.29` | 747,810.00 USD | 0.00 USD | 747,810.00 USD | 440,550.00 USD | 0.00 USD | 307,250.00 USD |
| `1D` | `1.30` | 731,690.00 USD | 0.00 USD | 731,690.00 USD | 0.00 USD | 597,860.00 USD | 133,830.00 USD |
| `7D` | `1.30` | 389,370.00 USD | 389,370.00 USD | 0.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD |
| `7D` | `1.30` | 778,740.00 USD | 778,740.00 USD | 0.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD |
| `1D` | `1.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.30` | 168,250.00 USD | 168,250.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 0.00 USD |
| `7D` | `1.30` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD |
| `1D` | `1.30` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 327,930.00 USD | 841,930.00 USD | 0.00 USD |
| `7D` | `1.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD |
| `1D` | `1.31` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 5,810.00 USD | 0.00 USD |
| `7D` | `1.31` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.31` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | 0.00 USD |
| `7D` | `1.31` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 543,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.31` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 515,020.00 USD | 344,570.00 USD | 388,870.00 USD |
| `7D` | `1.31` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 704,520.00 USD | 318,670.00 USD | 1,350,000.00 USD |
| `1D` | `1.31` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 1,570,000.00 USD | 443,660.00 USD | 682,300.00 USD |
| `7D` | `1.31` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD |
| `1D` | `1.31` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 355,560.00 USD | 483,320.00 USD | 181,970.00 USD |
| `7D` | `1.31` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD |
| `1D` | `1.32` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 116,540.00 USD | 1,800,000.00 USD | 4,170,000.00 USD |
| `7D` | `1.32` | 17,410,000.00 USD | 17,410,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,120,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 19,040,000.00 USD | 19,040,000.00 USD | 0.00 USD | 2,240,000.00 USD | 879,590.00 USD | 3,520,000.00 USD |
| `7D` | `1.32` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 755,330.00 USD | 406,240.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 22,430,000.00 USD | 22,430,000.00 USD | 0.00 USD | 1,620,000.00 USD | 711,160.00 USD | 1,060,000.00 USD |
| `7D` | `1.32` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 966,720.00 USD | 235,180.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 26,750,000.00 USD | 26,750,000.00 USD | 0.00 USD | 1,820,000.00 USD | 981,550.00 USD | 1,520,000.00 USD |
| `7D` | `1.32` | 25,950,000.00 USD | 25,950,000.00 USD | 0.00 USD | 1,980,000.00 USD | 761,100.00 USD | 1,290,000.00 USD |
| `1D` | `1.32` | 29,640,000.00 USD | 29,640,000.00 USD | 0.00 USD | 1,720,000.00 USD | 259,410.00 USD | 905,890.00 USD |
| `7D` | `1.32` | 28,320,000.00 USD | 28,320,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 31,890,000.00 USD | 31,890,000.00 USD | 0.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 28,850,000.00 USD | 28,850,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 34,080,000.00 USD | 34,080,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 30,010,000.00 USD | 30,010,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 36,470,000.00 USD | 36,470,000.00 USD | 0.00 USD | 822,840.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 31,730,000.00 USD | 31,730,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 37,980,000.00 USD | 37,980,000.00 USD | 0.00 USD | 262,430.00 USD | 248,670.00 USD | 999,630.00 USD |
| `7D` | `1.33` | 33,670,000.00 USD | 33,670,000.00 USD | 0.00 USD | 830,370.00 USD | 108,920.00 USD | 1,000,000.00 USD |
| `1D` | `1.33` | 39,390,000.00 USD | 39,390,000.00 USD | 0.00 USD | 819,570.00 USD | 94,350.00 USD | 492,850.00 USD |
| `7D` | `1.33` | 34,170,000.00 USD | 34,170,000.00 USD | 0.00 USD | 109,550.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 41,680,000.00 USD | 41,680,000.00 USD | 0.00 USD | 842,300.00 USD | 333,220.00 USD | 1,110,000.00 USD |
| `7D` | `1.34` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 312,290.00 USD |
| `1D` | `1.34` | 44,370,000.00 USD | 44,370,000.00 USD | 0.00 USD | 1,220,000.00 USD | 398,480.00 USD | 1,070,000.00 USD |
| `7D` | `1.34` | 37,910,000.00 USD | 37,910,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD |
| `1D` | `1.34` | 48,220,000.00 USD | 48,220,000.00 USD | 0.00 USD | 1,680,000.00 USD | 549,090.00 USD | 1,630,000.00 USD |
| `7D` | `1.34` | 42,630,000.00 USD | 42,630,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD |
| `1D` | `1.34` | 51,870,000.00 USD | 51,870,000.00 USD | 0.00 USD | 1,580,000.00 USD | 863,920.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 48,330,000.00 USD | 48,330,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,830,000.00 USD | 1,140,000.00 USD |
| `1D` | `1.34` | 56,280,000.00 USD | 56,280,000.00 USD | 0.00 USD | 2,360,000.00 USD | 675,180.00 USD | 1,380,000.00 USD |
| `7D` | `1.34` | 59,520,000.00 USD | 59,520,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,880,000.00 USD | 5,610,000.00 USD |
| `1D` | `1.35` | 58,690,000.00 USD | 58,690,000.00 USD | 0.00 USD | 997,910.00 USD | 469,060.00 USD | 940,830.00 USD |
| `7D` | `1.35` | 67,270,000.00 USD | 67,270,000.00 USD | 0.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,980,000.00 USD |
| `1D` | `1.35` | 60,570,000.00 USD | 60,570,000.00 USD | 0.00 USD | 915,920.00 USD | 263,070.00 USD | 702,970.00 USD |
| `7D` | `1.35` | 77,770,000.00 USD | 77,770,000.00 USD | 0.00 USD | 4,410,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 63,260,000.00 USD | 63,260,000.00 USD | 0.00 USD | 1,140,000.00 USD | 329,530.00 USD | 1,210,000.00 USD |
| `7D` | `1.35` | 85,540,000.00 USD | 85,540,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 64,670,000.00 USD | 64,670,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 646,720.00 USD |
| `7D` | `1.35` | 93,860,000.00 USD | 93,860,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 67,020,000.00 USD | 67,020,000.00 USD | 0.00 USD | 935,850.00 USD | 363,450.00 USD | 1,050,000.00 USD |
| `7D` | `1.35` | 102,090,000.00 USD | 102,090,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 69,330,000.00 USD | 69,330,000.00 USD | 0.00 USD | 911,460.00 USD | 199,730.00 USD | 1,200,000.00 USD |
| `7D` | `1.36` | 106,170,000.00 USD | 106,170,000.00 USD | 0.00 USD | 1,320,000.00 USD | 881,730.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 70,680,000.00 USD | 70,680,000.00 USD | 0.00 USD | 812,050.00 USD | 113,780.00 USD | 425,930.00 USD |
| `7D` | `1.36` | 110,030,000.00 USD | 110,030,000.00 USD | 0.00 USD | 1,490,000.00 USD | 693,390.00 USD | 1,680,000.00 USD |
| `1D` | `1.36` | 71,490,000.00 USD | 71,490,000.00 USD | 0.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD |
| `7D` | `1.36` | 112,530,000.00 USD | 112,530,000.00 USD | 0.00 USD | 671,910.00 USD | 581,640.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 72,450,000.00 USD | 72,450,000.00 USD | 0.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD |
| `7D` | `1.36` | 116,930,000.00 USD | 116,930,000.00 USD | 0.00 USD | 2,100,000.00 USD | 918,100.00 USD | 1,380,000.00 USD |
| `1D` | `1.36` | 73,100,000.00 USD | 73,100,000.00 USD | 0.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD |
| `7D` | `1.36` | 118,840,000.00 USD | 118,840,000.00 USD | 0.00 USD | 664,020.00 USD | 328,930.00 USD | 923,440.00 USD |
| `1D` | `1.37` | 73,290,000.00 USD | 73,290,000.00 USD | 0.00 USD | 65,890.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 119,340,000.00 USD | 119,340,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD |
| `1D` | `1.37` | 73,530,000.00 USD | 73,530,000.00 USD | 0.00 USD | 106,670.00 USD | 85,720.00 USD | 49,080.00 USD |
| `7D` | `1.37` | 121,130,000.00 USD | 121,130,000.00 USD | 0.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD |
| `1D` | `1.37` | 74,030,000.00 USD | 74,030,000.00 USD | 0.00 USD | 120,300.00 USD | 65,300.00 USD | 315,240.00 USD |
| `7D` | `1.37` | 122,530,000.00 USD | 122,530,000.00 USD | 0.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD |
| `1D` | `1.37` | 74,620,000.00 USD | 74,620,000.00 USD | 0.00 USD | 147,360.00 USD | 112,420.00 USD | 333,550.00 USD |
| `7D` | `1.37` | 125,390,000.00 USD | 125,390,000.00 USD | 0.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD |
| `1D` | `1.37` | 74,870,000.00 USD | 74,870,000.00 USD | 0.00 USD | 172,450.00 USD | 10,690.00 USD | 66,850.00 USD |
| `7D` | `1.38` | 127,080,000.00 USD | 127,080,000.00 USD | 0.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD |
| `1D` | `1.38` | 75,230,000.00 USD | 75,230,000.00 USD | 0.00 USD | 123,150.00 USD | 46,840.00 USD | 190,660.00 USD |
| `7D` | `1.38` | 128,700,000.00 USD | 128,700,000.00 USD | 0.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 75,790,000.00 USD | 75,790,000.00 USD | 0.00 USD | 235,940.00 USD | 73,260.00 USD | 241,330.00 USD |
| `7D` | `1.38` | 130,630,000.00 USD | 130,630,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 76,560,000.00 USD | 76,560,000.00 USD | 0.00 USD | 379,220.00 USD | 102,400.00 USD | 295,250.00 USD |
| `7D` | `1.38` | 133,180,000.00 USD | 133,180,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 77,080,000.00 USD | 77,080,000.00 USD | 0.00 USD | 241,850.00 USD | 53,840.00 USD | 224,750.00 USD |
| `7D` | `1.38` | 134,270,000.00 USD | 134,270,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 77,520,000.00 USD | 77,520,000.00 USD | 0.00 USD | 340,420.00 USD | 35,940.00 USD | 56,890.00 USD |
| `7D` | `1.39` | 135,370,000.00 USD | 135,370,000.00 USD | 0.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 77,710,000.00 USD | 77,710,000.00 USD | 0.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD |
| `7D` | `1.39` | 135,860,000.00 USD | 135,860,000.00 USD | 0.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD |
| `1D` | `1.39` | 77,860,000.00 USD | 77,860,000.00 USD | 0.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD |
| `7D` | `1.39` | 136,950,000.00 USD | 136,950,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD |
| `1D` | `1.39` | 78,120,000.00 USD | 78,120,000.00 USD | 0.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD |
| `7D` | `1.39` | 137,110,000.00 USD | 137,110,000.00 USD | 0.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD |
| `7D` | `1.39` | 137,430,000.00 USD | 137,430,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 78,140,000.00 USD | 78,140,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.40` | 137,580,000.00 USD | 137,580,000.00 USD | 0.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 78,240,000.00 USD | 78,240,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 137,590,000.00 USD | 137,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 137,600,000.00 USD | 137,600,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 137,740,000.00 USD | 137,740,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 137,860,000.00 USD | 137,860,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 138,100,000.00 USD | 138,100,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 138,260,000.00 USD | 138,260,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 138,430,000.00 USD | 138,430,000.00 USD | 0.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD |
| `7D` | `1.41` | 138,590,000.00 USD | 138,590,000.00 USD | 0.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD |
| `1D` | `1.41` | 78,240,000.00 USD | 78,240,000.00 USD | 0.00 USD | 0.00 USD | 158.40 USD | 0.00 USD |
| `7D` | `1.41` | 138,760,000.00 USD | 138,760,000.00 USD | 0.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.41` | 78,250,000.00 USD | 78,250,000.00 USD | 0.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD |
| `7D` | `1.42` | 139,250,000.00 USD | 139,250,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD |
| `1D` | `1.42` | 78,360,000.00 USD | 78,360,000.00 USD | 0.00 USD | 60,530.00 USD | 27,040.00 USD | 25,730.00 USD |
| `7D` | `1.42` | 139,680,000.00 USD | 139,680,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.42` | 78,690,000.00 USD | 78,690,000.00 USD | 0.00 USD | 176,350.00 USD | 69,160.00 USD | 79,970.00 USD |
| `7D` | `1.42` | 140,710,000.00 USD | 140,710,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.42` | 79,400,000.00 USD | 79,400,000.00 USD | 0.00 USD | 362,640.00 USD | 148,060.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 142,080,000.00 USD | 142,080,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.42` | 79,810,000.00 USD | 79,810,000.00 USD | 0.00 USD | 157,740.00 USD | 72,390.00 USD | 181,030.00 USD |
| `7D` | `1.42` | 142,710,000.00 USD | 142,710,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.42` | 79,890,000.00 USD | 79,890,000.00 USD | 0.00 USD | 9,670.00 USD | 54,730.00 USD | 21,210.00 USD |
| `7D` | `1.43` | 143,070,000.00 USD | 143,070,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `1D` | `1.43` | 80,110,000.00 USD | 80,110,000.00 USD | 0.00 USD | 111,940.00 USD | 38,740.00 USD | 61,750.00 USD |
| `7D` | `1.43` | 144,090,000.00 USD | 144,090,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `1D` | `1.43` | 80,280,000.00 USD | 80,280,000.00 USD | 0.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.43` | 145,590,000.00 USD | 145,590,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.43` | 80,450,000.00 USD | 80,450,000.00 USD | 0.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.43` | 146,980,000.00 USD | 146,980,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.43` | 80,670,000.00 USD | 80,670,000.00 USD | 0.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.43` | 147,780,000.00 USD | 147,780,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.43` | 80,940,000.00 USD | 80,940,000.00 USD | 0.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.44` | 148,310,000.00 USD | 148,310,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `1D` | `1.44` | 81,070,000.00 USD | 81,070,000.00 USD | 0.00 USD | 21,660.00 USD | 0.00 USD | 105,000.00 USD |
| `7D` | `1.44` | 148,670,000.00 USD | 148,670,000.00 USD | 0.00 USD | 74,670.00 USD | 68,640.00 USD | 215,310.00 USD |
| `1D` | `1.44` | 81,160,000.00 USD | 81,160,000.00 USD | 0.00 USD | 47,660.00 USD | 16,990.00 USD | 30,940.00 USD |
| `7D` | `1.44` | 149,160,000.00 USD | 149,160,000.00 USD | 0.00 USD | 154,760.00 USD | 93,720.00 USD | 245,840.00 USD |
| `1D` | `1.44` | 81,340,000.00 USD | 81,340,000.00 USD | 0.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.44` | 150,050,000.00 USD | 150,050,000.00 USD | 0.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD |
| `1D` | `1.44` | 81,420,000.00 USD | 81,420,000.00 USD | 0.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.44` | 150,560,000.00 USD | 150,560,000.00 USD | 0.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD |
| `1D` | `1.44` | 81,510,000.00 USD | 81,510,000.00 USD | 0.00 USD | 25,860.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.45` | 150,700,000.00 USD | 150,700,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.45` | 81,550,000.00 USD | 81,550,000.00 USD | 0.00 USD | 1,080.00 USD | 22,830.00 USD | 16,200.00 USD |
| `7D` | `1.45` | 150,830,000.00 USD | 150,830,000.00 USD | 0.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD |
| `1D` | `1.45` | 81,630,000.00 USD | 81,630,000.00 USD | 0.00 USD | 52,260.00 USD | 7,500.00 USD | 28,080.00 USD |
| `7D` | `1.45` | 151,300,000.00 USD | 151,300,000.00 USD | 0.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD |
| `1D` | `1.45` | 81,750,000.00 USD | 81,750,000.00 USD | 0.00 USD | 28,500.00 USD | 37,670.00 USD | 53,040.00 USD |
| `7D` | `1.45` | 151,900,000.00 USD | 151,900,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 370,320.00 USD |
| `1D` | `1.45` | 81,880,000.00 USD | 81,880,000.00 USD | 0.00 USD | 46,680.00 USD | 17,340.00 USD | 62,280.00 USD |
| `7D` | `1.45` | 152,530,000.00 USD | 152,530,000.00 USD | 0.00 USD | 161,500.00 USD | 127,370.00 USD | 338,310.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `3.02B` | Total OI Tokens: `2,327,264,242.2 XRP`
  * 1h OI Change: `-0.47%` | 4h OI Change: `-0.03%` | 24h OI Change: `+2.58%`
  * Exchange Breakdown: Binance=`499.58M` | Bybit=`330.93M` | OKX=`102.88M` | Hyperliquid=`227.44M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `82.54K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0044%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `49.97%` | `50.03%` | `1.00` | 782,520,000.00 USD |
| `15M` | `Binance` | `39.94%` | `60.06%` | `0.67` | 223,710,000.00 USD |
| `15M` | `OKX` | `52.03%` | `47.97%` | `1.08` | 119,850,000.00 USD |
| `15M` | `Bybit` | `50.74%` | `49.26%` | `1.03` | 56,010,000.00 USD |
| `15M` | `KuCoin` | `52.38%` | `47.62%` | `1.10` | 1,970,000.00 USD |
| `15M` | `Gate` | `48.19%` | `51.81%` | `0.93` | 105,090,000.00 USD |
| `15M` | `Bitget` | `46.48%` | `53.52%` | `0.87` | 43,030,000.00 USD |
| `15M` | `BingX` | `68.68%` | `31.32%` | `2.19` | 13,260,000.00 USD |
| `15M` | `MEXC` | `49.44%` | `50.56%` | `0.98` | 50,010,000.00 USD |
| `15M` | `Bitunix` | `53.63%` | `46.37%` | `1.16` | 31,880,000.00 USD |
| `15M` | `Hyperliquid` | `67.26%` | `32.74%` | `2.05` | 61,820,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `77.22%` | `22.78%` | `3.39` | 5,780,000.00 USD |
| `15M` | `Crypto.com` | `50.42%` | `49.58%` | `1.02` | 8,710,000.00 USD |
| `15M` | `WhiteBIT` | `82.43%` | `17.57%` | `4.69` | 19,760,000.00 USD |
| `15M` | `HTX` | `57.42%` | `42.58%` | `1.35` | 2,350,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `55.17%` | `44.83%` | `1.23` | 15,840,000.00 USD |
| `15M` | `Bitfinex` | `39.81%` | `60.19%` | `0.66` | 381,670.00 USD |
| `15M` | `Kraken` | `63.96%` | `36.04%` | `1.77` | 3,440,000.00 USD |
| `15M` | `Aster` | `43.17%` | `56.83%` | `0.76` | 7,810,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `48.86%` | `51.14%` | `0.96` | 11,810,000.00 USD |
| `15M` | `Whale Positions` | `39.94%` | `60.06%` | `0.67` | 223,710,000.00 USD |
| `15M` | `Global Accounts` | `49.97%` | `50.03%` | `1.00` | 782,520,000.00 USD |
| `1H` | `XRP` | `46.92%` | `53.08%` | `0.88` | 3,640,000,000.00 USD |
| `1H` | `Binance` | `42.6%` | `57.4%` | `0.74` | 1,250,000,000.00 USD |
| `1H` | `OKX` | `46.68%` | `53.32%` | `0.88` | 457,190,000.00 USD |
| `1H` | `Bybit` | `45.76%` | `54.24%` | `0.84` | 323,110,000.00 USD |
| `1H` | `KuCoin` | `29.45%` | `70.55%` | `0.42` | 14,270,000.00 USD |
| `1H` | `Gate` | `49.23%` | `50.77%` | `0.97` | 434,160,000.00 USD |
| `1H` | `Bitget` | `42.83%` | `57.17%` | `0.75` | 185,090,000.00 USD |
| `1H` | `BingX` | `56.5%` | `43.5%` | `1.30` | 69,110,000.00 USD |
| `1H` | `MEXC` | `52.7%` | `47.3%` | `1.11` | 187,100,000.00 USD |
| `1H` | `Bitunix` | `50.8%` | `49.2%` | `1.03` | 153,110,000.00 USD |
| `1H` | `Hyperliquid` | `52.28%` | `47.72%` | `1.10` | 178,800,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `67.99%` | `32.01%` | `2.12` | 28,050,000.00 USD |
| `1H` | `Crypto.com` | `48.63%` | `51.37%` | `0.95` | 30,680,000.00 USD |
| `1H` | `WhiteBIT` | `69.24%` | `30.76%` | `2.25` | 74,940,000.00 USD |
| `1H` | `HTX` | `45.24%` | `54.76%` | `0.83` | 14,480,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `55.52%` | `44.48%` | `1.25` | 86,180,000.00 USD |
| `1H` | `Bitfinex` | `38.64%` | `61.36%` | `0.63` | 2,490,000.00 USD |
| `1H` | `Kraken` | `47.3%` | `52.7%` | `0.90` | 31,690,000.00 USD |
| `1H` | `Aster` | `34.66%` | `65.34%` | `0.53` | 46,450,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.34%` | `50.66%` | `0.97` | 63,180,000.00 USD |
| `1H` | `Whale Positions` | `42.6%` | `57.4%` | `0.74` | 1,250,000,000.00 USD |
| `1H` | `Global Accounts` | `46.92%` | `53.08%` | `0.88` | 3,640,000,000.00 USD |
| `4H` | `XRP` | `50.24%` | `49.76%` | `1.01` | 21,140,000,000.00 USD |
| `4H` | `Binance` | `49.63%` | `50.37%` | `0.99` | 6,710,000,000.00 USD |
| `4H` | `OKX` | `50.02%` | `49.98%` | `1.00` | 3,060,000,000.00 USD |
| `4H` | `Bybit` | `49.55%` | `50.45%` | `0.98` | 2,100,000,000.00 USD |
| `4H` | `KuCoin` | `47.94%` | `52.06%` | `0.92` | 83,220,000.00 USD |
| `4H` | `Gate` | `50.17%` | `49.83%` | `1.01` | 2,510,000,000.00 USD |
| `4H` | `Bitget` | `49.54%` | `50.46%` | `0.98` | 1,270,000,000.00 USD |
| `4H` | `BingX` | `49.9%` | `50.1%` | `1.00` | 385,850,000.00 USD |
| `4H` | `MEXC` | `54.13%` | `45.87%` | `1.18` | 1,160,000,000.00 USD |
| `4H` | `Bitunix` | `47.88%` | `52.12%` | `0.92` | 1,060,000,000.00 USD |
| `4H` | `Hyperliquid` | `53.3%` | `46.7%` | `1.14` | 976,630,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.65%` | `50.35%` | `0.99` | 134,580,000.00 USD |
| `4H` | `Crypto.com` | `47.92%` | `52.08%` | `0.92` | 139,200,000.00 USD |
| `4H` | `WhiteBIT` | `56.97%` | `43.03%` | `1.32` | 371,800,000.00 USD |
| `4H` | `HTX` | `47.21%` | `52.79%` | `0.89` | 85,040,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.22%` | `48.78%` | `1.05` | 412,820,000.00 USD |
| `4H` | `Bitfinex` | `65.95%` | `34.05%` | `1.94` | 29,080,000.00 USD |
| `4H` | `Kraken` | `53.09%` | `46.91%` | `1.13` | 162,550,000.00 USD |
| `4H` | `Aster` | `48.04%` | `51.96%` | `0.92` | 227,460,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.19%` | `49.81%` | `1.01` | 265,600,000.00 USD |
| `4H` | `Whale Positions` | `49.63%` | `50.37%` | `0.99` | 6,710,000,000.00 USD |
| `4H` | `Global Accounts` | `50.24%` | `49.76%` | `1.01` | 21,140,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.31` | `1.31` | `1.31` | `1.31` | `1.30` | 9,428,108.38 USD | 3,943,451.38 USD | 5,484,657.00 USD | -1,541,205.63 USD | `-16.35%` | `8B / 24S` |
| `0:00 UTC` | `1.30` | `1.31` | `1.30` | `1.31` | `1.30` | 9,077,727.01 USD | 4,773,597.25 USD | 4,304,129.76 USD | 469,467.49 USD | `+5.17%` | `10B / 12S` |
| `5:00 UTC` | `1.31` | `1.31` | `1.31` | `1.31` | `1.31` | 9,791,336.03 USD | 4,585,305.80 USD | 5,206,030.23 USD | -620,724.44 USD | `-6.34%` | `2B / 6S` |
| `0:00 UTC` | `1.31` | `1.31` | `1.31` | `1.32` | `1.31` | 13,794,897.02 USD | 7,005,423.08 USD | 6,789,473.94 USD | 215,949.13 USD | `+1.57%` | `17B / 16S` |
| `5:00 UTC` | `1.30` | `1.31` | `1.30` | `1.31` | `1.30` | 11,087,990.94 USD | 4,090,249.58 USD | 6,997,741.36 USD | -2,907,491.79 USD | `-26.22%` | `5B / 28S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 10,205,311.65 USD | 4,505,902.50 USD | 5,699,409.15 USD | -1,193,506.66 USD | `-11.69%` | `6B / 11S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 4,776,328.08 USD | 2,498,208.46 USD | 2,278,119.62 USD | 220,088.84 USD | `+4.61%` | `7B / 8S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 9,199,982.08 USD | 4,187,578.87 USD | 5,012,403.21 USD | -824,824.35 USD | `-8.97%` | `4B / 7S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 5,359,755.08 USD | 2,909,456.29 USD | 2,450,298.78 USD | 459,157.51 USD | `+8.57%` | `5B / 3S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 1,035,410.56 USD | 532,733.03 USD | 502,677.53 USD | 30,055.50 USD | `+2.90%` | `6B / 9S` |

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
| `5m` | 190,930.00 USD | 991,480.00 USD | **`ACCUMULATION`** |
| `15m` | -128,040.00 USD | 1,700,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,010,000.00 USD | -1,720,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,500,000.00 USD | -5,120,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,030,000.00 USD | -10,730,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 656,940.00 USD | -5,610,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -263,020.00 USD | -4,690,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,610.00 USD | -3,250,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,070,000.00 USD | -12,620,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -14,630,000.00 USD | -46,340,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -73,410,000.00 USD | -83,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -547,950,000.00 USD | -1,170,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+190.93K` | 15m=`-128.04K` | 1h=`-2.50M` | 24h=`-14.63M`
* Futures Capital Netflows: 5m=`+991.48K` | 15m=`+1.70M` | 1h=`-5.12M` | 24h=`-46.34M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0778` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `4.30`
  * Mathematical Lot Sizing: **`8.29 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.50` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `-1.72`
  * Mathematical Lot Sizing: **`8.29 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.30`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
