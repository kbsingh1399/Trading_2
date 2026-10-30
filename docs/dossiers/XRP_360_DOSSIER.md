# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 10:37:50 IST` (`2026-10-30 05:07:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.25`
- **Spread Points**: `4.00` | **Spread BPS**: `31.92 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.22` | VWAP Z-Score: `+1.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0100` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `60.98` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.27` | Lower -3.00σ Band: `1.18`
  * Upper +2.51σ Band: `1.26` | Lower -2.51σ Band: `1.18`
  * Upper +2.01σ Band: `1.26` | Lower -2.01σ Band: `1.19`
  * Upper +2.00σ Band: `1.26` | Lower -2.00σ Band: `1.19`
  * Upper +1.28σ Band: `1.24` | Lower -1.28σ Band: `1.20`
  * Upper +1.00σ Band: `1.24` | Lower -1.00σ Band: `1.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.24` | EMA-20=`1.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.26`
  * Institutional Anchors: EMA-144=`1.27` | EMA-200=`1.28` (Slope: `-0.4895`) | EMA-233=`1.29`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.54%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.62%`)
  * Value Area Low (VAL) = `1.22` (Distance: `+2.56%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.25` | Low=`1.25`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.25`
  * Initial Balance (First Hour): IB High=`1.25` | IB Low=`1.25`
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
| `5m` | `1.25` | `1.26` | `1.25` | `1.25` | `1,784,500` | 2,236,990.96 USD | 789,699.40 USD | `+35.30%` | -44,402,055.30 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `1,479,091` | 1,854,852.11 USD | -22,677.37 USD | `-1.22%` | -44,424,732.66 USD | `-0.67` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `1.25` | `1.26` | `1.25` | `1.26` | `2,501,388` | 3,140,280.38 USD | 928,443.03 USD | `+29.57%` | -43,496,289.64 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `7,956,358` | 9,975,142.90 USD | 1,860,696.23 USD | `+18.65%` | -46,275,363.39 USD | `+0.78` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `5,435,736` | 6,812,599.45 USD | 998,364.47 USD | `+14.65%` | -45,276,998.93 USD | `+0.41` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.26` | `2,497,062` | 3,134,846.05 USD | 932,369.91 USD | `+29.74%` | -44,344,629.01 USD | `+0.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.22` | `1.25` | `1.22` | `1.25` | `36,941,941` | 45,661,386.25 USD | 4,453,356.28 USD | `+9.75%` | -46,975,781.11 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.24` | `1.25` | `31,772,661` | 39,740,326.41 USD | 3,435,958.07 USD | `+8.65%` | -43,539,823.04 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `2,501,388` | 3,140,280.38 USD | 928,443.03 USD | `+29.57%` | -42,611,380.02 USD | `+0.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `34,274,049` | 42,880,606.79 USD | 4,364,401.10 USD | `+10.18%` | -41,022,185.30 USD | `+0.98` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | 545,129.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -14,866,665.27 USD | `-1.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `34,274,049` | 42,880,606.79 USD | 4,364,401.10 USD | `+10.18%` | -41,022,185.30 USD | `+0.98` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `1.25` | `123629.0000` | 155,154.39 USD | 1,013,805.80 USD | `8 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `55822.0000` | 70,051.03 USD | 1,083,856.83 USD | `4 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `265388.0000` | 333,008.86 USD | 1,416,865.69 USD | `6 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `28447.0000` | 35,692.45 USD | 1,452,558.14 USD | `4 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `227727.0000` | 285,706.29 USD | 1,738,264.43 USD | `3 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `36815.0000` | 46,184.42 USD | 1,784,448.85 USD | `6 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `4870.0000` | 6,108.93 USD | 1,790,557.78 USD | `2 orders` | `-0.16%` | `-` |
| `ASK` | `1.26` | `33893.0000` | 42,647.56 USD | 2,055,344.42 USD | `5 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `39394.0000` | 49,565.53 USD | 2,012,696.86 USD | `2 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `42633.0000` | 53,636.58 USD | 1,963,131.33 USD | `6 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `202823.0000` | 255,151.33 USD | 1,909,494.75 USD | `7 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `39899.0000` | 50,188.95 USD | 1,654,343.42 USD | `6 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `63753.0000` | 80,188.52 USD | 1,604,154.46 USD | `1 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `354962.0000` | 446,435.71 USD | 1,523,965.94 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `60350.0000` | 75,896.16 USD | 1,077,530.23 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `50535.0000` | 63,547.76 USD | 1,001,634.07 USD | `9 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `70640.0000` | 88,822.74 USD | 938,086.31 USD | `3 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `78499.0000` | 98,696.79 USD | 849,263.58 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `25020.0000` | 31,455.14 USD | 750,566.78 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `299462.0000` | 376,453.68 USD | 719,111.64 USD | `9 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `22910.0000` | 28,797.87 USD | 342,657.96 USD | `7 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `62375.0000` | 78,399.14 USD | 313,860.09 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `70898.0000` | 89,104.61 USD | 235,460.95 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `44612.0000` | 56,063.90 USD | 146,356.34 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `21130.0000` | 26,551.96 USD | 90,292.44 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `20576.0000` | 25,853.74 USD | 63,740.49 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `1.26` | `30155.0000` | 37,886.74 USD | 37,886.74 USD | `8 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `1738.0000` | 2,183.45 USD | 2,183.45 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `1.26` | `3199.0000` | 4,018.58 USD | 6,202.03 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `4654.0000` | 5,845.89 USD | 12,047.92 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `19393.0000` | 24,357.61 USD | 36,405.53 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `54677.0000` | 68,668.84 USD | 105,074.37 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `38948.0000` | 48,910.90 USD | 153,985.27 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `13294.0000` | 16,693.28 USD | 170,678.55 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `95094.0000` | 119,400.03 USD | 290,078.58 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `77930.0000` | 97,841.12 USD | 387,919.69 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `258127.0000` | 324,052.64 USD | 711,972.33 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `30263.0000` | 37,989.14 USD | 749,961.47 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `32948.0000` | 41,356.33 USD | 791,317.80 USD | `6 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `53648.0000` | 67,333.60 USD | 858,651.40 USD | `6 orders` | `-0.10%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `28` | `0x31b1...1434` | `LONG` | 44,016,991.80 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,438,108.53 USD | `+10.08%` | `10X Cross` |
| `91` | `0x5b5d...c060` | `SHORT` | 20,059,081.38 USD | `15,964,251.00` | `1.44` | `1.26` | `11.36` | 2,856,987.33 USD | `+14.24%` | `5X Cross` |
| `158` | `0xb83d...6e36` | `SHORT` | 13,268,200.65 USD | `10,555,450.00` | `1.50` | `1.26` | `13.81` | 2,554,368.99 USD | `+19.25%` | `5X Cross` |
| `344` | `0x58f0...0d20` | `LONG` | 6,669,550.01 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 66,706.51 USD | `+1.00%` | `20X Cross` |
| `409` | `0xecb6...2b00` | `SHORT` | 5,460,149.65 USD | `4,345,523.00` | `1.27` | `1.26` | `7.90` | 61,673.29 USD | `+1.13%` | `10X Cross` |
| `425` | `0xca49...53c8` | `SHORT` | 5,198,440.82 USD | `4,138,886.00` | `1.44` | `1.26` | `4.84` | 754,881.92 USD | `+14.52%` | `20X Cross` |
| `437` | `0xdd53...2b13` | `SHORT` | 5,021,836.20 USD | `3,998,914.00` | `1.40` | `1.26` | `16.85` | 575,039.91 USD | `+11.45%` | `3X Cross` |
| `504` | `0x610b...b613` | `LONG` | 4,454,031.33 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8147` | -645,961.28 USD | `-14.50%` | `5X Cross` |
| `536` | `0xfc27...9d9d` | `SHORT` | 4,185,322.34 USD | `3,330,937.00` | `1.29` | `1.26` | `6.65` | 122,698.19 USD | `+2.93%` | `20X Cross` |
| `619` | `0x9946...0852` | `SHORT` | 3,657,997.01 USD | `2,912,418.00` | `1.41` | `1.26` | `1.78` | 450,505.57 USD | `+12.32%` | `20X Cross` |
| `672` | `0xc30c...a4c9` | `SHORT` | 3,359,164.63 USD | `2,672,981.00` | `1.42` | `1.26` | `1.59` | 427,799.48 USD | `+12.74%` | `6X Cross` |
| `701` | `0xf48f...10fe` | `LONG` | 3,225,184.20 USD | `2,565,779.00` | `1.53` | `1.26` | `0.9944` | -699,456.52 USD | `-21.69%` | `4X Cross` |
| `736` | `0x023a...2355` | `SHORT` | 3,096,687.79 USD | `2,464,927.00` | `1.32` | `1.26` | `3.35` | 156,308.45 USD | `+5.05%` | `20X Cross` |
| `744` | `0x45d2...4029` | `SHORT` | 3,080,477.40 USD | `2,453,000.00` | `1.48` | `1.26` | `18.28` | 557,803.02 USD | `+18.11%` | `20X Cross` |
| `1075` | `0xeadc...9d55` | `LONG` | 2,035,284.98 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 76,441.96 USD | `+3.76%` | `20X Cross` |
| `1150` | `0x94b2...599e` | `SHORT` | 1,935,884.52 USD | `1,540,696.00` | `1.36` | `1.26` | `1.86` | 164,581.93 USD | `+8.50%` | `20X Cross` |
| `1155` | `0xbcd4...0dd2` | `SHORT` | 1,922,532.48 USD | `1,529,461.00` | `1.31` | `1.26` | `1.87` | 82,012.12 USD | `+4.27%` | `20X Cross` |
| `1172` | `0x3fc5...c0c1` | `SHORT` | 1,900,306.20 USD | `1,511,779.00` | `1.52` | `1.26` | `2.37` | 391,308.40 USD | `+20.59%` | `20X Cross` |
| `1202` | `0x31ef...f715` | `LONG` | 1,853,749.26 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -345,516.14 USD | `-18.64%` | `3X Isolated` |
| `1250` | `0x7737...bf66` | `SHORT` | 1,776,020.03 USD | `1,413,466.00` | `1.41` | `1.26` | `13.62` | 222,848.62 USD | `+12.55%` | `10X Cross` |
| `1304` | `0x95da...2328` | `LONG` | 1,664,986.24 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0791` | -128,654.85 USD | `-7.73%` | `5X Cross` |
| `1327` | `0xee2b...d67e` | `LONG` | 1,641,998.99 USD | `1,306,284.00` | `1.55` | `1.26` | `0.4030` | -388,655.91 USD | `-23.67%` | `4X Cross` |
| `1372` | `0x215d...f80a` | `LONG` | 1,572,857.80 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -81,596.43 USD | `-5.19%` | `14X Cross` |
| `1401` | `0x5fa3...35b7` | `SHORT` | 1,558,763.84 USD | `1,240,651.00` | `1.30` | `1.26` | `2.63` | 57,728.29 USD | `+3.70%` | `20X Cross` |
| `1434` | `0x123d...3bff` | `LONG` | 1,527,060.89 USD | `1,215,329.00` | `1.35` | `1.26` | `0.000000` | -110,008.33 USD | `-7.20%` | `10X Cross` |
| `1490` | `0xdf95...7d72` | `SHORT` | 1,457,971.33 USD | `1,160,528.00` | `1.37` | `1.26` | `34.42` | 135,503.81 USD | `+9.29%` | `20X Cross` |
| `1567` | `0xef96...9383` | `SHORT` | 1,372,777.86 USD | `1,092,976.00` | `1.34` | `1.26` | `4.57` | 89,969.58 USD | `+6.55%` | `20X Cross` |
| `1573` | `0xc179...e0c8` | `SHORT` | 1,367,425.08 USD | `1,088,281.00` | `1.29` | `1.26` | `7.02` | 41,355.04 USD | `+3.02%` | `10X Cross` |
| `1606` | `0x7fda...17d1` | `LONG` | 1,329,253.86 USD | `1,057,902.00` | `1.21` | `1.26` | `0.000000` | 46,044.96 USD | `+3.46%` | `20X Cross` |
| `1651` | `0xb1ce...681b` | `LONG` | 1,283,131.23 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -240,925.26 USD | `-18.78%` | `4X Isolated` |
| `1759` | `0x3c36...461a` | `LONG` | 1,181,080.08 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -38,000.54 USD | `-3.22%` | `10X Cross` |
| `1794` | `0x2577...4897` | `SHORT` | 1,161,292.48 USD | `924,228.00` | `1.24` | `1.26` | `4.82` | -13,404.47 USD | `-1.15%` | `20X Cross` |
| `2013` | `0xbfc7...80b4` | `SHORT` | 1,005,126.40 USD | `800,000.00` | `1.48` | `1.26` | `3.22` | 178,328.25 USD | `+17.74%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,999.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 41.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.04K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 5,001.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3962 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 1,717.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.72K USD at 1.3962 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 5,001.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3963 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,265.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.27K USD at 1.3963 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 5,000.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3964 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,935.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.94K USD at 1.3965 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 17,312.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 17.31K USD at 1.2550 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 62.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.06K USD at 1.2550 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 899.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2550 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 51.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.2551 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 3,587.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.59K USD at 1.2552 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 376.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.38K USD at 1.2553 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 76.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.08K USD at 1.2553 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 48.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.2555 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 12.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.2555 USD [API] | `2026-09-16 17:40:05` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 20,968.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 20.97K USD at 1.3543 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 4,314.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.31K USD at 1.3543 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 349.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.35K USD at 1.3543 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 219.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.22K USD at 1.3544 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 4,315.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.32K USD at 1.3544 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 293.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.29K USD at 1.3545 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 3,330.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.33K USD at 1.3545 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 2,329.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.33K USD at 1.3546 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 399.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3546 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 139.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.14K USD at 1.3546 USD [API] | `2026-09-11 18:04:36` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 3,199.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.20K USD at 1.3288 USD [API] | `2026-09-11 11:02:12` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 1,843.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.84K USD at 1.3289 USD [API] | `2026-09-11 11:02:12` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 13,608.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 13.61K USD at 1.3434 USD [API] | `2026-09-10 12:47:17` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 4,969.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.97K USD at 1.3842 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 499.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3843 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 1,748.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.75K USD at 1.3843 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 1,236.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.24K USD at 1.3844 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,274.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.27K USD at 1.3844 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,196.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.20K USD at 1.3844 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 499.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3844 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 146.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.15K USD at 1.3845 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 12,694.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.69K USD at 1.3846 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 84.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.08K USD at 1.3848 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 691.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.69K USD at 1.3848 USD [API] | `2026-09-04 14:49:46` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,550.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.55K USD at 1.3325 USD [API] | `2026-09-02 01:40:45` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,523.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.52K USD at 1.3325 USD [API] | `2026-09-02 01:40:45` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 7,638.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.64K USD at 1.3550 USD [API] | `2026-08-30 23:38:38` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 67.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.3550 USD [API] | `2026-08-30 23:38:38` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 4,998.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3551 USD [API] | `2026-08-30 23:38:38` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 432.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.43K USD at 1.3551 USD [API] | `2026-08-30 23:38:38` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 1,192.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.19K USD at 1.3551 USD [API] | `2026-08-30 23:38:38` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 4,360.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.36K USD at 1.3553 USD [API] | `2026-08-30 23:38:38` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 30,338.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 30.34K USD at 1.3741 USD [API] | `2026-08-28 16:25:16` |
| `ANNOUNCEMENT` | `INFO` | `1.39` | 53,656.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 53.66K USD at 1.3891 USD [API] | `2026-08-28 14:04:34` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 1,995.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.00K USD at 1.3801 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 10,139.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.14K USD at 1.3801 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 169.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3801 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 151.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.15K USD at 1.3801 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,784.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.78K USD at 1.3801 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 276.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.28K USD at 1.3801 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,941.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.94K USD at 1.3801 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 4,111.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.11K USD at 1.3802 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 15,001.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 15.00K USD at 1.3802 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,942.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.94K USD at 1.3803 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 171.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3803 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 4,737.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.74K USD at 1.3804 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 669.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.67K USD at 1.3804 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 2,985.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.99K USD at 1.3804 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,101.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.10K USD at 1.3804 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 2,014.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.01K USD at 1.3804 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 16.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3804 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 476.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.48K USD at 1.3805 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 760.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.76K USD at 1.3805 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 49.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3805 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 52.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3805 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 175.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.18K USD at 1.3805 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 376.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.38K USD at 1.3806 USD [API] | `2026-08-26 13:28:06` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 22,572.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 22.57K USD at 1.4056 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 697.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.70K USD at 1.4056 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 2,915.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.92K USD at 1.4057 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 5,060.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.06K USD at 1.4057 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 4,409.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.41K USD at 1.4057 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 437.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.44K USD at 1.4058 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 4,999.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4058 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 5,315.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.32K USD at 1.4058 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 1,539.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.54K USD at 1.4059 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 642.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.64K USD at 1.4059 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 241.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.24K USD at 1.4059 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 241.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.24K USD at 1.4059 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 1,802.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.80K USD at 1.4060 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 452.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.45K USD at 1.4060 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 3,103.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.10K USD at 1.4060 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 2,047.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.05K USD at 1.4061 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 99.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.4061 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 4,998.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4061 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 11.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.4062 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 4,999.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4062 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 10,012.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.01K USD at 1.4062 USD [API] | `2026-08-26 10:01:17` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 94,969.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 94.97K USD at 1.4084 USD [API] | `2026-08-25 21:08:08` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 360.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.36K USD at 1.4763 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 504.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4763 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 4,938.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.94K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 442.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.44K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 3,369.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.37K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,669.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.67K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,002.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.00K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,248.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.25K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 6,270.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.27K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 504.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 504.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4764 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 30,003.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 30.00K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,696.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.70K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 1,334.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.33K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 667.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.67K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 667.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.67K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 4,498.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.50K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,248.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.25K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 504.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 504.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4765 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 14,002.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 14.00K USD at 1.4766 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,248.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.25K USD at 1.4766 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 505.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4766 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 505.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4766 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 505.07 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.51K USD at 1.4768 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 505.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.51K USD at 1.4770 USD [API] | `2026-08-24 17:22:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 1,959.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.96K USD at 1.4632 USD [API] | `2026-08-24 02:03:48` |
| `ANNOUNCEMENT` | `INFO` | `0.9926` | 9,934.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.93K USD at 0.9926 USD [API] | `2026-08-11 14:57:16` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 22.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.0205 USD [API] | `2026-08-07 03:56:04` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 533.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.53K USD at 1.0205 USD [API] | `2026-08-07 03:56:04` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 1,112.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.11K USD at 1.0205 USD [API] | `2026-08-07 03:56:04` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 1,106.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.11K USD at 1.0205 USD [API] | `2026-08-07 03:56:04` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 1,310.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.31K USD at 1.0205 USD [API] | `2026-08-07 03:56:04` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 655.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.66K USD at 1.0205 USD [API] | `2026-08-07 03:56:04` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 655.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.66K USD at 1.0205 USD [API] | `2026-08-07 03:56:04` |
| `ANNOUNCEMENT` | `INFO` | `1.04` | 12,106.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.11K USD at 1.0409 USD [API] | `2026-08-06 02:19:44` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 3,344.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.34K USD at 1.0602 USD [API] | `2026-07-28 00:27:28` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 84.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.08K USD at 1.0602 USD [API] | `2026-07-28 00:27:28` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 242.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.24K USD at 1.0603 USD [API] | `2026-07-28 00:27:28` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 8.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.0603 USD [API] | `2026-07-28 00:27:28` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 397.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.0859 USD [API] | `2026-07-24 16:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 499.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.0859 USD [API] | `2026-07-24 16:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 5,454.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.45K USD at 1.0860 USD [API] | `2026-07-24 16:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 399.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.0860 USD [API] | `2026-07-24 16:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 903.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.0860 USD [API] | `2026-07-24 16:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.12` | 17,186.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 17.19K USD at 1.1161 USD [API] | `2026-07-23 13:06:14` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 5,983.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.98K USD at 1.0711 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 1,570.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.57K USD at 1.0711 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,205.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.21K USD at 1.0711 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 85.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.0711 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 53.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.0711 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 87.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.0711 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 99.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.0711 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 500.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.0712 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 232.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.23K USD at 1.0712 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 73.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.0715 USD [API] | `2026-07-13 03:10:48` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 1,008.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.01K USD at 1.0867 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 1,217.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.22K USD at 1.0867 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 278.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.28K USD at 1.0867 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 10.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.0867 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 1,119.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.12K USD at 1.0868 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 336.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.34K USD at 1.0868 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 30.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.03K USD at 1.0868 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 10.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.0868 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 429.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.43K USD at 1.0869 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 19.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.0869 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 86.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.0869 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 982.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.98K USD at 1.0870 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 10.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.0870 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 498.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.0870 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 16.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.0870 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 472.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.47K USD at 1.0871 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 326.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.33K USD at 1.0871 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 10.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.0872 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 1,312.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.31K USD at 1.0872 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.09` | 904.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.0873 USD [API] | `2026-07-08 06:21:10` |
| `ANNOUNCEMENT` | `INFO` | `1.12` | 19,681.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 19.68K USD at 1.1155 USD [API] | `2026-07-07 14:15:13` |
| `ANNOUNCEMENT` | `INFO` | `1.01` | 1,675.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.68K USD at 1.0095 USD [API] | `2026-06-26 03:03:07` |
| `ANNOUNCEMENT` | `INFO` | `1.04` | 3,650.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.65K USD at 1.0423 USD [API] | `2026-06-25 13:47:36` |
| `ANNOUNCEMENT` | `INFO` | `1.08` | 2,825.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.83K USD at 1.0752 USD [API] | `2026-06-24 13:48:22` |
| `ANNOUNCEMENT` | `INFO` | `1.08` | 161.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.16K USD at 1.0752 USD [API] | `2026-06-24 13:48:22` |
| `ANNOUNCEMENT` | `INFO` | `1.08` | 4,485.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.49K USD at 1.0752 USD [API] | `2026-06-24 13:48:22` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 1,928.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.93K USD at 1.0987 USD [API] | `2026-06-23 08:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 4,766.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.77K USD at 1.0988 USD [API] | `2026-06-23 08:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 20.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.0988 USD [API] | `2026-06-23 08:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 4,996.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.0989 USD [API] | `2026-06-23 08:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 4,293.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.29K USD at 1.0990 USD [API] | `2026-06-23 08:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.12` | 7,795.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.80K USD at 1.1234 USD [API] | `2026-06-19 07:37:07` |
| `ANNOUNCEMENT` | `INFO` | `1.12` | 17,144.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 17.14K USD at 1.1234 USD [API] | `2026-06-19 07:37:07` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 4,040.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.04K USD at 1.0664 USD [API] | `2026-06-06 04:19:59` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 661.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.66K USD at 1.0665 USD [API] | `2026-06-06 04:19:59` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 9,710.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.71K USD at 1.0970 USD [API] | `2026-06-05 15:14:11` |
| `ANNOUNCEMENT` | `INFO` | `1.14` | 20,334.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 20.33K USD at 1.1371 USD [API] | `2026-06-05 02:43:26` |
| `ANNOUNCEMENT` | `INFO` | `1.14` | 1,429.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.43K USD at 1.1408 USD [API] | `2026-06-04 11:15:11` |
| `ANNOUNCEMENT` | `INFO` | `1.14` | 400.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.1408 USD [API] | `2026-06-04 11:15:11` |
| `ANNOUNCEMENT` | `INFO` | `1.14` | 365.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.37K USD at 1.1408 USD [API] | `2026-06-04 11:15:11` |
| `ANNOUNCEMENT` | `INFO` | `1.14` | 1,359.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.36K USD at 1.1408 USD [API] | `2026-06-04 11:15:11` |
| `ANNOUNCEMENT` | `INFO` | `1.14` | 11.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.1408 USD [API] | `2026-06-04 11:15:11` |
| `ANNOUNCEMENT` | `INFO` | `1.17` | 2,799.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.80K USD at 1.1728 USD [API] | `2026-06-04 01:23:13` |
| `ANNOUNCEMENT` | `INFO` | `1.17` | 4,837.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.84K USD at 1.1728 USD [API] | `2026-06-04 01:23:13` |
| `ANNOUNCEMENT` | `INFO` | `1.21` | 1,780.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.78K USD at 1.2089 USD [API] | `2026-06-02 19:33:25` |
| `ANNOUNCEMENT` | `INFO` | `1.22` | 3,875.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.88K USD at 1.2217 USD [API] | `2026-06-02 15:30:56` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 2,322.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.32K USD at 1.2532 USD [API] | `2026-06-02 14:10:02` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 6,018.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.02K USD at 1.2533 USD [API] | `2026-06-02 14:10:02` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 17,667.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 17.67K USD at 1.2962 USD [API] | `2026-05-28 03:17:50` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 15,168.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 15.17K USD at 1.3123 USD [API] | `2026-05-23 07:50:37` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,177.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.18K USD at 1.3125 USD [API] | `2026-05-23 07:50:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 3,056.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.06K USD at 1.3506 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 1,323.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.32K USD at 1.3507 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 1,457.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.46K USD at 1.3507 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 2,999.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.00K USD at 1.3507 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 4,998.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3507 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 299.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.30K USD at 1.3508 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 798.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.80K USD at 1.3508 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 2,958.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.96K USD at 1.3508 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 445.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.45K USD at 1.3508 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 433.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.43K USD at 1.3508 USD [API] | `2026-05-20 01:28:37` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,625.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.63K USD at 1.3717 USD [API] | `2026-05-18 14:35:39` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 14,823.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 14.82K USD at 1.3717 USD [API] | `2026-05-18 14:35:39` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 16,209.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 16.21K USD at 1.4164 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 3,814.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.81K USD at 1.4164 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 4,987.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.99K USD at 1.4164 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 3,431.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.43K USD at 1.4164 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 3,431.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.43K USD at 1.4164 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 888.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.89K USD at 1.4165 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 424.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.42K USD at 1.4166 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 1,929.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.93K USD at 1.4166 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 4,251.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.25K USD at 1.4167 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 1,826.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.83K USD at 1.4169 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 296.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.30K USD at 1.4170 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 1,486.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.49K USD at 1.4171 USD [API] | `2026-05-16 04:37:45` |
| `ANNOUNCEMENT` | `INFO` | `1.43` | 1,475.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.48K USD at 1.4349 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.43` | 4,761.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.76K USD at 1.4349 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 5,000.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4350 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 5,000.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4350 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 5,001.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4351 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 921.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.92K USD at 1.4351 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 8,999.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.00K USD at 1.4351 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 1,186.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.19K USD at 1.4351 USD [API] | `2026-05-12 13:56:54` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 18,574.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 18.57K USD at 1.4468 USD [API] | `2026-05-10 20:49:06` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 9,997.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.00K USD at 1.4468 USD [API] | `2026-05-10 20:49:06` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 23.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.4468 USD [API] | `2026-05-10 20:49:06` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 49.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.4468 USD [API] | `2026-05-10 20:49:06` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 21.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.4469 USD [API] | `2026-05-10 20:49:06` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 23.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.4471 USD [API] | `2026-05-10 20:49:06` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 11.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.4472 USD [API] | `2026-05-10 20:49:06` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3061 USD [API] | `2026-10-29 01:48:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,758.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.76K USD at 1.3061 USD [API] | `2026-10-29 01:48:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3060 USD [API] | `2026-10-29 01:48:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 9,329.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 9.33K USD at 1.3032 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 67.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.3032 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,752.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.75K USD at 1.3032 USD [API] | `2026-10-29 01:48:20` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 22,757.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 22.76K USD at 1.3008 USD [API] | `2026-10-29 01:52:49` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 7,002.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.00K USD at 1.3037 USD [API] | `2026-10-29 01:55:14` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,295.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.30K USD at 1.3002 USD [API] | `2026-10-29 01:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11,323.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.32K USD at 1.3003 USD [API] | `2026-10-29 01:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11,323.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.32K USD at 1.3003 USD [API] | `2026-10-29 01:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,200.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.20K USD at 1.2988 USD [API] | `2026-10-29 01:49:22` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 4,742.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.74K USD at 1.2989 USD [API] | `2026-10-29 01:49:22` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 357.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.36K USD at 1.2989 USD [API] | `2026-10-29 01:49:22` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,178.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.18K USD at 1.3035 USD [API] | `2026-10-29 01:48:26` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 572.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.57K USD at 1.3035 USD [API] | `2026-10-29 01:48:26` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,936.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.94K USD at 1.2973 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 10,391.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.39K USD at 1.2985 USD [API] | `2026-10-29 01:59:57` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,613.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.61K USD at 1.3003 USD [API] | `2026-10-29 02:01:50` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,901.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.90K USD at 1.3003 USD [API] | `2026-10-29 02:01:50` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 14,998.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 15.00K USD at 1.3003 USD [API] | `2026-10-29 02:01:50` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,214.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.21K USD at 1.2966 USD [API] | `2026-10-29 02:06:01` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,955.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.96K USD at 1.2980 USD [API] | `2026-10-29 02:06:53` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 573.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.57K USD at 1.2953 USD [API] | `2026-10-29 02:11:05` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 305.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.31K USD at 1.2953 USD [API] | `2026-10-29 02:11:05` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,006.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2977 USD [API] | `2026-10-29 02:14:42` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 292.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.29K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 117.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.12K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 86.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,005.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.01K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 2,959.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.96K USD at 1.2948 USD [API] | `2026-10-29 02:17:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 167.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.17K USD at 1.2948 USD [API] | `2026-10-29 02:17:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 15.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2948 USD [API] | `2026-10-29 02:17:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,320.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.32K USD at 1.2948 USD [API] | `2026-10-29 02:17:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 195.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2948 USD [API] | `2026-10-29 02:17:09` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,258.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.26K USD at 1.2984 USD [API] | `2026-10-29 02:18:56` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,332.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.33K USD at 1.2984 USD [API] | `2026-10-29 02:18:56` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11,283.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.28K USD at 1.2963 USD [API] | `2026-10-29 02:22:50` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,535.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.54K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.01K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,901.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.90K USD at 1.2940 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 55.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.06K USD at 1.2940 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 651.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.65K USD at 1.2946 USD [API] | `2026-10-29 02:27:25` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2946 USD [API] | `2026-10-29 02:27:25` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 41.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2946 USD [API] | `2026-10-29 02:27:25` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 647.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.65K USD at 1.2946 USD [API] | `2026-10-29 02:27:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 91.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2946 USD [API] | `2026-10-29 02:27:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,781.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.78K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 51.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 380.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.38K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 666.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.67K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,781.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.78K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,951.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.95K USD at 1.2931 USD [API] | `2026-10-29 02:28:24` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,544.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.54K USD at 1.2941 USD [API] | `2026-10-29 02:29:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,426.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.43K USD at 1.2941 USD [API] | `2026-10-29 02:29:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,398.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 6.40K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 210.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.21K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 15.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 386.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.39K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 10,210.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 10.21K USD at 1.3650 USD [API] | `2026-08-30 23:29:31` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 11,967.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.97K USD at 1.2923 USD [API] | `2026-10-29 02:32:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 11,967.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.97K USD at 1.2923 USD [API] | `2026-10-29 02:32:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 91.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2914 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,703.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.70K USD at 1.2930 USD [API] | `2026-10-29 02:29:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 641.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.64K USD at 1.2930 USD [API] | `2026-10-29 02:29:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2930 USD [API] | `2026-10-29 02:29:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 29.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 29.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,202.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.20K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 541.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.54K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 953.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.95K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 126.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.13K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 541.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.54K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 19.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 144.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 673.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.67K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 77.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 148.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 584.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.58K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 112.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.11K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 53.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,263.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.26K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 393.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.39K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 69.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,471.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.47K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 2,293.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.29K USD at 1.2942 USD [API] | `2026-10-29 02:28:14` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,605.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.61K USD at 1.2882 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.01K USD at 1.2882 USD [API] | `2026-10-29 02:36:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.29%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.39%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+5.51%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.41%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+7.68%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.41%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,000,000.00 USD, Dist: `+7.33%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.41%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 496.49 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 1,060.00 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,190.00 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 1,120.00 USD | 64,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 23,570.00 USD | 64,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 9,600.00 USD | 64,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 8,310.00 USD | 64,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 20,510.00 USD | 64,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 1,580.00 USD | 64,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 30,620.00 USD | 64,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 2,860.00 USD | 64,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 183.00 USD | 64,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 312.62 USD | 64,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 64,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 167.27 USD | 64,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 2,090.00 USD | 64,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 707,570.00 USD | 64,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 18,000.00 USD | 63,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 1,070.00 USD | 63,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 244.34 USD | 63,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 11,930.00 USD | 63,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 10,880.00 USD | 63,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 4,030.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 1,020.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 188.87 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 1,960.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 1,430.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 45,410.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 276.31 USD | 63,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 3,060.00 USD | 63,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 162,420.00 USD | 63,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 6,560.00 USD | 63,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 1,550.00 USD | 63,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 7,660.00 USD | 63,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 20,970.00 USD | 63,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 38,950.00 USD | 63,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 2,050.00 USD | 63,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 11,300.00 USD | 63,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,040.00 USD | 63,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 1,290.00 USD | 63,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 17,920.00 USD | 63,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 27,760.00 USD | 63,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 5,320.00 USD | 63,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 144,240.00 USD | 63,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 49,520.00 USD | 62,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 73,620.00 USD | 62,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 219,560.00 USD | 62,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 44,260.00 USD | 62,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 56,770.00 USD | 62,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 86,500.00 USD | 62,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 123,440.00 USD | 62,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 5,740.00 USD | 62,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 16,010.00 USD | 62,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 508,760.00 USD | 62,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 10,860.00 USD | 61,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 49,720.00 USD | 61,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 2,950,000.00 USD | 61,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 34,670.00 USD | 58,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 75,630.00 USD | 58,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 48,680.00 USD | 58,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 5,460.00 USD | 58,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 95,210.00 USD | 58,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 344,110.00 USD | 58,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 108,160.00 USD | 58,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 138,790.00 USD | 58,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 81,300.00 USD | 57,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 80,910.00 USD | 57,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 271,720.00 USD | 57,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 65,480.00 USD | 57,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 156,510.00 USD | 57,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,890,000.00 USD | 57,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 178,750.00 USD | 23,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 459,360.00 USD | 23,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 2,670,000.00 USD | 22,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 463,000.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 386,700.00 USD | 19,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 52,650.00 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 19,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 662,160.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,140,000.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 747,180.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 78,580,000.00 USD | 78,580,000.00 USD | 23,750.00 USD | 0.00 USD | 39,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 955,410.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 188,350.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 78,520,000.00 USD | 78,520,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 78,480,000.00 USD | 78,480,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 78,380,000.00 USD | 78,380,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.09` | 68,350,000.00 USD | 68,350,000.00 USD | 0.00 USD | 64,380.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 381,630.00 USD | 13,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.10` | 68,270,000.00 USD | 68,270,000.00 USD | 35,350.00 USD | 1,130.00 USD | 130,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 78,340,000.00 USD | 78,340,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.10` | 68,100,000.00 USD | 68,100,000.00 USD | 72,120.00 USD | 2,030.00 USD | 75,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 78,340,000.00 USD | 78,340,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.10` | 67,950,000.00 USD | 67,950,000.00 USD | 6,450.00 USD | 46,740.00 USD | 131,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.10` | 67,760,000.00 USD | 67,760,000.00 USD | 72,970.00 USD | 27,450.00 USD | 64,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 78,050,000.00 USD | 78,050,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.10` | 67,600,000.00 USD | 67,600,000.00 USD | 3,520.00 USD | 361.50 USD | 67,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 376,130.00 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.11` | 67,530,000.00 USD | 67,530,000.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 78,050,000.00 USD | 78,050,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 67,530,000.00 USD | 67,530,000.00 USD | 6,020.00 USD | 0.00 USD | 846.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 78,040,000.00 USD | 78,040,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 67,520,000.00 USD | 67,520,000.00 USD | 17,310.00 USD | 15,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 78,040,000.00 USD | 78,040,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 67,490,000.00 USD | 67,490,000.00 USD | 71,640.00 USD | 13,130.00 USD | 123,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 67,280,000.00 USD | 67,280,000.00 USD | 0.00 USD | 3,300.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 289,050.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 77,990,000.00 USD | 77,990,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 67,270,000.00 USD | 67,270,000.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 77,970,000.00 USD | 77,970,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 67,150,000.00 USD | 67,150,000.00 USD | 7,460.00 USD | 48,180.00 USD | 41,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 67,060,000.00 USD | 67,060,000.00 USD | 16,420.00 USD | 60,880.00 USD | 88,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 77,900,000.00 USD | 77,900,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 66,890,000.00 USD | 66,890,000.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 77,870,000.00 USD | 77,870,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 66,800,000.00 USD | 66,800,000.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,210,000.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 66,630,000.00 USD | 66,630,000.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 77,660,000.00 USD | 77,660,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 66,510,000.00 USD | 66,510,000.00 USD | 69,610.00 USD | 60,790.00 USD | 140,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 77,470,000.00 USD | 77,470,000.00 USD | 5,450.00 USD | 2,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 66,240,000.00 USD | 66,240,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 77,460,000.00 USD | 77,460,000.00 USD | 69,750.00 USD | 93,260.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 66,000,000.00 USD | 66,000,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 77,290,000.00 USD | 77,290,000.00 USD | 74,920.00 USD | 97,060.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 65,950,000.00 USD | 65,950,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 131,930.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.14` | 76,890,000.00 USD | 76,890,000.00 USD | 79,780.00 USD | 88,050.00 USD | 71,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 65,890,000.00 USD | 65,890,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 76,650,000.00 USD | 76,650,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 65,800,000.00 USD | 65,800,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 76,620,000.00 USD | 76,620,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 65,780,000.00 USD | 65,780,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 76,580,000.00 USD | 76,580,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 65,710,000.00 USD | 65,710,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 76,450,000.00 USD | 76,450,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 65,570,000.00 USD | 65,570,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 332,060.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 76,440,000.00 USD | 76,440,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 76,370,000.00 USD | 76,370,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 65,540,000.00 USD | 65,540,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 76,000,000.00 USD | 76,000,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 75,850,000.00 USD | 75,850,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 65,520,000.00 USD | 65,520,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 75,680,000.00 USD | 75,680,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 65,320,000.00 USD | 65,320,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 531,180.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 74,800,000.00 USD | 74,800,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 64,980,000.00 USD | 64,980,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 74,570,000.00 USD | 74,570,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 64,860,000.00 USD | 64,860,000.00 USD | 126,860.00 USD | 16,130.00 USD | 446,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 73,700,000.00 USD | 73,700,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 64,270,000.00 USD | 64,270,000.00 USD | 253,200.00 USD | 126,280.00 USD | 170,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 72,620,000.00 USD | 72,620,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 63,720,000.00 USD | 63,720,000.00 USD | 253,180.00 USD | 314,800.00 USD | 334,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 71,320,000.00 USD | 71,320,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 62,810,000.00 USD | 62,810,000.00 USD | 95,890.00 USD | 51,030.00 USD | 486,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,610,000.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 69,660,000.00 USD | 69,660,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 62,180,000.00 USD | 62,180,000.00 USD | 148,160.00 USD | 120,500.00 USD | 131,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 68,310,000.00 USD | 68,310,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 61,780,000.00 USD | 61,780,000.00 USD | 135,220.00 USD | 101,000.00 USD | 210,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 67,240,000.00 USD | 67,240,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 61,330,000.00 USD | 61,330,000.00 USD | 365,570.00 USD | 32,690.00 USD | 449,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 65,210,000.00 USD | 65,210,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 60,490,000.00 USD | 60,490,000.00 USD | 104,550.00 USD | 90,830.00 USD | 392,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 64,010,000.00 USD | 64,010,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 59,900,000.00 USD | 59,900,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 514,860.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 62,440,000.00 USD | 62,440,000.00 USD | 181,850.00 USD | 100,190.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 58,950,000.00 USD | 58,950,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 61,780,000.00 USD | 61,780,000.00 USD | 85,020.00 USD | 74,230.00 USD | 489,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 58,580,000.00 USD | 58,580,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 61,130,000.00 USD | 61,130,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 58,250,000.00 USD | 58,250,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 60,520,000.00 USD | 60,520,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 58,080,000.00 USD | 58,080,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 60,250,000.00 USD | 60,250,000.00 USD | 299,450.00 USD | 571,980.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 57,250,000.00 USD | 57,250,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 443,330.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 59,140,000.00 USD | 59,140,000.00 USD | 76,370.00 USD | 109,420.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 56,810,000.00 USD | 56,810,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 58,250,000.00 USD | 58,250,000.00 USD | 250,710.00 USD | 115,630.00 USD | 585,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 55,530,000.00 USD | 55,530,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 57,300,000.00 USD | 57,300,000.00 USD | 227,280.00 USD | 92,240.00 USD | 795,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 53,790,000.00 USD | 53,790,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 56,190,000.00 USD | 56,190,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 53,310,000.00 USD | 53,310,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 54,820,000.00 USD | 54,820,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 52,200,000.00 USD | 52,200,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 742,780.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 53,990,000.00 USD | 53,990,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 49,620,000.00 USD | 49,620,000.00 USD | 748,570.00 USD | 84,750.00 USD | 788,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 52,410,000.00 USD | 52,410,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 48,000,000.00 USD | 48,000,000.00 USD | 112,900.00 USD | 934,870.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 49,400,000.00 USD | 49,400,000.00 USD | 736,290.00 USD | 330,310.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 45,440,000.00 USD | 45,440,000.00 USD | 730,270.00 USD | 464,920.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 48,310,000.00 USD | 48,310,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 42,610,000.00 USD | 42,610,000.00 USD | 314,820.00 USD | 47,550.00 USD | 740,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 47,440,000.00 USD | 47,440,000.00 USD | 47,500.00 USD | 589,990.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 41,510,000.00 USD | 41,510,000.00 USD | 295,960.00 USD | 920,650.00 USD | 241,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 4,610.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 46,800,000.00 USD | 46,800,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 40,050,000.00 USD | 40,050,000.00 USD | 778,920.00 USD | 104,970.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 46,770,000.00 USD | 46,770,000.00 USD | 432,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 37,880,000.00 USD | 37,880,000.00 USD | 1,570,000.00 USD | 133,210.00 USD | 763,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 46,340,000.00 USD | 46,340,000.00 USD | 257,960.00 USD | 326,720.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 35,420,000.00 USD | 35,420,000.00 USD | 127,210.00 USD | 462,270.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 42,880,000.00 USD | 42,880,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 33,420,000.00 USD | 33,420,000.00 USD | 1,350,000.00 USD | 271,760.00 USD | 998,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 41,650,000.00 USD | 41,650,000.00 USD | 108,640.00 USD | 0.00 USD | 910,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 30,800,000.00 USD | 30,800,000.00 USD | 52,290.00 USD | 154,650.00 USD | 685,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 40,630,000.00 USD | 40,630,000.00 USD | 142,210.00 USD | 9,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 29,910,000.00 USD | 29,910,000.00 USD | 307,460.00 USD | 26,150.00 USD | 176,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 40,480,000.00 USD | 40,480,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 29,400,000.00 USD | 29,400,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 39,750,000.00 USD | 39,750,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 29,130,000.00 USD | 29,130,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 38,660,000.00 USD | 38,660,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 28,450,000.00 USD | 28,450,000.00 USD | 106,100.00 USD | 0.00 USD | 348,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 38,490,000.00 USD | 38,490,000.00 USD | 51,610.00 USD | 166,160.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 27,990,000.00 USD | 27,990,000.00 USD | 270,600.00 USD | 510,520.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 433.65 USD | 433.65 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 38,230,000.00 USD | 38,230,000.00 USD | 112,770.00 USD | 535,430.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 24,570,000.00 USD | 24,570,000.00 USD | 107,280.00 USD | 64,900.00 USD | 86,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 37,580,000.00 USD | 37,580,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 24,310,000.00 USD | 24,310,000.00 USD | 556,720.00 USD | 1,090,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 36,540,000.00 USD | 36,540,000.00 USD | 198,530.00 USD | 888,470.00 USD | 807,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 20,220,000.00 USD | 20,220,000.00 USD | 66,520.00 USD | 1,250,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 34,650,000.00 USD | 34,650,000.00 USD | 1,020,000.00 USD | 963,040.00 USD | 824,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 16,630,000.00 USD | 16,630,000.00 USD | 1,380,000.00 USD | 443,480.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 31,840,000.00 USD | 31,840,000.00 USD | 1,420,000.00 USD | 1,650,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 12,590,000.00 USD | 12,590,000.00 USD | 122,830.00 USD | 1,130,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 25,340,000.00 USD | 25,340,000.00 USD | 2,040,000.00 USD | 1,640,000.00 USD | 941,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 10,060,000.00 USD | 10,060,000.00 USD | 18,660.00 USD | 280,340.00 USD | 61,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 20,710,000.00 USD | 20,710,000.00 USD | 2,630,000.00 USD | 1,580,000.00 USD | 3,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 9,700,000.00 USD | 9,700,000.00 USD | 15,170.00 USD | 220,870.00 USD | 931,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 13,020,000.00 USD | 13,020,000.00 USD | 2,070,000.00 USD | 950,140.00 USD | 535,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 8,530,000.00 USD | 8,530,000.00 USD | 734,030.00 USD | 182,970.00 USD | 651,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 9,460,000.00 USD | 9,460,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 6,960,000.00 USD | 6,960,000.00 USD | 658,110.00 USD | 818,040.00 USD | 863,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 8,330,000.00 USD | 8,330,000.00 USD | 1,420,000.00 USD | 15,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 4,620,000.00 USD | 4,620,000.00 USD | 1,520,000.00 USD | 10,130.00 USD | 379,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 6,900,000.00 USD | 6,900,000.00 USD | 3,370,000.00 USD | 0.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 2,720,000.00 USD | 2,720,000.00 USD | 617,230.00 USD | 3,790.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,090,000.00 USD | 2,090,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 2,080,000.00 USD | 2,080,000.00 USD | 331,570.00 USD | 306,030.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 464,350.00 USD | 464,350.00 USD | 0.00 USD | 9,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 1,230,000.00 USD | 1,230,000.00 USD | 202,510.00 USD | 1,390.00 USD | 993,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 455,200.00 USD | 455,200.00 USD | 0.00 USD | 0.00 USD | 455,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 30,590.00 USD | 30,590.00 USD | 17,600.00 USD | 8,750.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 949,920.00 USD | 949,920.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 1,900,000.00 USD | 1,900,000.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 1,330,000.00 USD | 1,330,000.00 USD | 633,250.00 USD | 12,640.00 USD | 681,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 9,740.00 USD | 9,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.26` | 3,110,000.00 USD | 3,110,000.00 USD | 150,010.00 USD | 273,460.00 USD | 783,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 3,410,000.00 USD | 3,410,000.00 USD | 1,090,000.00 USD | 443,180.00 USD | 551,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 19,840.00 USD | 239,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 5,290,000.00 USD | 5,290,000.00 USD | 295,510.00 USD | 561,050.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 4,230,000.00 USD | 4,230,000.00 USD | 107,140.00 USD | 670,900.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 7,970,000.00 USD | 7,970,000.00 USD | 532,070.00 USD | 86,770.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 8,510,000.00 USD | 8,510,000.00 USD | 144,170.00 USD | 408,460.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 11,800,000.00 USD | 11,800,000.00 USD | 1,250,000.00 USD | 819,120.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 13,960,000.00 USD | 13,960,000.00 USD | 834,020.00 USD | 925,190.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 15,420,000.00 USD | 15,420,000.00 USD | 479,740.00 USD | 980,510.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 120,440.00 USD | 130,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.27` | 30,010,000.00 USD | 30,010,000.00 USD | 4,260,000.00 USD | 3,030,000.00 USD | 8,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 19,740,000.00 USD | 19,740,000.00 USD | 745,260.00 USD | 1,270,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 35,760,000.00 USD | 35,760,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 22,800,000.00 USD | 22,800,000.00 USD | 466,250.00 USD | 2,030,000.00 USD | 566,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 38,790,000.00 USD | 38,790,000.00 USD | 138,500.00 USD | 2,540,000.00 USD | 350,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 26,540,000.00 USD | 26,540,000.00 USD | 521,360.00 USD | 956,980.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 45,280,000.00 USD | 45,280,000.00 USD | 1,280,000.00 USD | 4,610,000.00 USD | 598,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 29,730,000.00 USD | 29,730,000.00 USD | 1,820,000.00 USD | 356,430.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 57,590,000.00 USD | 57,590,000.00 USD | 2,710,000.00 USD | 2,540,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 35,770,000.00 USD | 35,770,000.00 USD | 836,830.00 USD | 2,200,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 10,160.00 USD | 140,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.28` | 71,230,000.00 USD | 71,230,000.00 USD | 4,660,000.00 USD | 2,810,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 43,090,000.00 USD | 43,090,000.00 USD | 1,980,000.00 USD | 1,810,000.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 88,340,000.00 USD | 88,340,000.00 USD | 7,780,000.00 USD | 3,210,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 50,910,000.00 USD | 50,910,000.00 USD | 3,090,000.00 USD | 2,110,000.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 89,860,000.00 USD | 89,860,000.00 USD | 0.00 USD | 1,440,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 52,230,000.00 USD | 52,230,000.00 USD | 257,680.00 USD | 558,100.00 USD | 510,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 91,000,000.00 USD | 91,000,000.00 USD | 1,030,000.00 USD | 30,200.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 55,180,000.00 USD | 55,180,000.00 USD | 1,170,000.00 USD | 238,770.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 93,750,000.00 USD | 93,750,000.00 USD | 854,670.00 USD | 956,050.00 USD | 929,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 57,130,000.00 USD | 57,130,000.00 USD | 515,680.00 USD | 380,450.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,390.00 USD | 142,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.29` | 96,350,000.00 USD | 96,350,000.00 USD | 796,960.00 USD | 1,120,000.00 USD | 680,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 59,240,000.00 USD | 59,240,000.00 USD | 828,650.00 USD | 812,440.00 USD | 472,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 96,820,000.00 USD | 96,820,000.00 USD | 440,460.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 59,630,000.00 USD | 59,630,000.00 USD | 210,950.00 USD | 24,800.00 USD | 148,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 97,410,000.00 USD | 97,410,000.00 USD | 70,460.00 USD | 4,320.00 USD | 510,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 60,120,000.00 USD | 60,120,000.00 USD | 177,490.00 USD | 42,820.00 USD | 268,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 99,490,000.00 USD | 99,490,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 846,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 63,120,000.00 USD | 63,120,000.00 USD | 570,020.00 USD | 197,630.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 103,140,000.00 USD | 103,140,000.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 69,290,000.00 USD | 69,290,000.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 692.82 USD | 143,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 110,430,000.00 USD | 110,430,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 71,860,000.00 USD | 71,860,000.00 USD | 554,720.00 USD | 703,990.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 112,380,000.00 USD | 112,380,000.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 72,620,000.00 USD | 72,620,000.00 USD | 335,370.00 USD | 109,620.00 USD | 312,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 114,380,000.00 USD | 114,380,000.00 USD | 208,510.00 USD | 298,720.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 74,870,000.00 USD | 74,870,000.00 USD | 530,940.00 USD | 364,450.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 115,410,000.00 USD | 115,410,000.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 76,900,000.00 USD | 76,900,000.00 USD | 761,460.00 USD | 808,970.00 USD | 455,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 117,930,000.00 USD | 117,930,000.00 USD | 0.00 USD | 2,040,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 78,170,000.00 USD | 78,170,000.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 246.65 USD | 143,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 119,890,000.00 USD | 119,890,000.00 USD | 1,770,000.00 USD | 183,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 80,460,000.00 USD | 80,460,000.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 124,540,000.00 USD | 124,540,000.00 USD | 1,430,000.00 USD | 821,310.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 83,700,000.00 USD | 83,700,000.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 126,560,000.00 USD | 126,560,000.00 USD | 1,340,000.00 USD | 242,640.00 USD | 433,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 85,570,000.00 USD | 85,570,000.00 USD | 866,160.00 USD | 434,290.00 USD | 573,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 130,540,000.00 USD | 130,540,000.00 USD | 189,510.00 USD | 858,660.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 87,660,000.00 USD | 87,660,000.00 USD | 729,330.00 USD | 417,190.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 131,710,000.00 USD | 131,710,000.00 USD | 515,950.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 90,420,000.00 USD | 90,420,000.00 USD | 342,500.00 USD | 387,380.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 135,910,000.00 USD | 135,910,000.00 USD | 68,520.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 95,720,000.00 USD | 95,720,000.00 USD | 1,300,000.00 USD | 1,040,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 140,760,000.00 USD | 140,760,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,600,000.00 USD | 100,600,000.00 USD | 1,680,000.00 USD | 733,340.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,780,000.00 USD | 142,780,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 103,560,000.00 USD | 103,560,000.00 USD | 1,500,000.00 USD | 499,050.00 USD | 959,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 146,140,000.00 USD | 146,140,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 106,730,000.00 USD | 106,730,000.00 USD | 1,010,000.00 USD | 481,660.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 148,920,000.00 USD | 148,920,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 108,040,000.00 USD | 108,040,000.00 USD | 830,310.00 USD | 111,810.00 USD | 368,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 56,950.00 USD | 200,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 150,720,000.00 USD | 150,720,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 109,650,000.00 USD | 109,650,000.00 USD | 503,480.00 USD | 452,830.00 USD | 647,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 151,820,000.00 USD | 151,820,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 111,510,000.00 USD | 111,510,000.00 USD | 578,690.00 USD | 128,070.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 153,530,000.00 USD | 153,530,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 113,680,000.00 USD | 113,680,000.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 156,000,000.00 USD | 156,000,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 115,630,000.00 USD | 115,630,000.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 158,030,000.00 USD | 158,030,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 116,970,000.00 USD | 116,970,000.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,430.00 USD | 202,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 159,570,000.00 USD | 159,570,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 117,710,000.00 USD | 117,710,000.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 162,010,000.00 USD | 162,010,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 118,310,000.00 USD | 118,310,000.00 USD | 179,460.00 USD | 83,160.00 USD | 334,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 163,880,000.00 USD | 163,880,000.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 119,820,000.00 USD | 119,820,000.00 USD | 701,920.00 USD | 312,600.00 USD | 499,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 169,400,000.00 USD | 169,400,000.00 USD | 2,380,000.00 USD | 2,490,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 121,870,000.00 USD | 121,870,000.00 USD | 963,900.00 USD | 368,440.00 USD | 716,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 176,810,000.00 USD | 176,810,000.00 USD | 2,000,000.00 USD | 2,170,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 123,440,000.00 USD | 123,440,000.00 USD | 556,930.00 USD | 328,690.00 USD | 683,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 17,330.00 USD | 219,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 186,060,000.00 USD | 186,060,000.00 USD | 3,530,000.00 USD | 1,830,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 124,030,000.00 USD | 124,030,000.00 USD | 206,540.00 USD | 183,280.00 USD | 204,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 194,650,000.00 USD | 194,650,000.00 USD | 3,010,000.00 USD | 1,970,000.00 USD | 3,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 124,710,000.00 USD | 124,710,000.00 USD | 312,230.00 USD | 33,600.00 USD | 333,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 202,670,000.00 USD | 202,670,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 125,280,000.00 USD | 125,280,000.00 USD | 261,450.00 USD | 55,490.00 USD | 251,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 211,790,000.00 USD | 211,790,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 125,690,000.00 USD | 125,690,000.00 USD | 111,940.00 USD | 144,570.00 USD | 154,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 218,540,000.00 USD | 218,540,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,450,000.00 USD | 126,450,000.00 USD | 124,010.00 USD | 62,670.00 USD | 572,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 2,700.00 USD | 222,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 224,880,000.00 USD | 224,880,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 127,410,000.00 USD | 127,410,000.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 227,430,000.00 USD | 227,430,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 127,740,000.00 USD | 127,740,000.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 230,530,000.00 USD | 230,530,000.00 USD | 1,460,000.00 USD | 414,770.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,400,000.00 USD | 128,400,000.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 234,320,000.00 USD | 234,320,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,700,000.00 USD | 128,700,000.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 237,080,000.00 USD | 237,080,000.00 USD | 1,430,000.00 USD | 616,140.00 USD | 713,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,820,000.00 USD | 128,820,000.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 193,360.00 USD | 415,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 237,890,000.00 USD | 237,890,000.00 USD | 206,650.00 USD | 190,380.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,070,000.00 USD | 129,070,000.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 239,000,000.00 USD | 239,000,000.00 USD | 535,200.00 USD | 181,820.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,220,000.00 USD | 129,220,000.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 240,490,000.00 USD | 240,490,000.00 USD | 415,220.00 USD | 339,760.00 USD | 733,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,320,000.00 USD | 129,320,000.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 242,150,000.00 USD | 242,150,000.00 USD | 553,200.00 USD | 287,880.00 USD | 820,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,410,000.00 USD | 129,410,000.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 244,070,000.00 USD | 244,070,000.00 USD | 619,020.00 USD | 407,640.00 USD | 893,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 129,580,000.00 USD | 129,580,000.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 65,510.00 USD | 480,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 245,320,000.00 USD | 245,320,000.00 USD | 360,280.00 USD | 298,220.00 USD | 586,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 129,700,000.00 USD | 129,700,000.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 246,780,000.00 USD | 246,780,000.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 129,970,000.00 USD | 129,970,000.00 USD | 69,610.00 USD | 60,790.00 USD | 140,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 248,420,000.00 USD | 248,420,000.00 USD | 436,360.00 USD | 142,590.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,040,000.00 USD | 130,040,000.00 USD | 0.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 250,280,000.00 USD | 250,280,000.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,210,000.00 USD | 130,210,000.00 USD | 0.00 USD | 0.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 251,070,000.00 USD | 251,070,000.00 USD | 403,730.00 USD | 253,120.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 130,250,000.00 USD | 130,250,000.00 USD | 46,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 482,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 252,090,000.00 USD | 252,090,000.00 USD | 377,810.00 USD | 231,880.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 253,010,000.00 USD | 253,010,000.00 USD | 384,080.00 USD | 308,280.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 253,760,000.00 USD | 253,760,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,080,000.00 USD | 254,080,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,140,000.00 USD | 254,140,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 484,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,370,000.00 USD | 254,370,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,370,000.00 USD | 254,370,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,440,000.00 USD | 254,440,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,510,000.00 USD | 254,510,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,810,000.00 USD | 254,810,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 635.06 USD | 484,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 254,960,000.00 USD | 254,960,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 255,130,000.00 USD | 255,130,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,010,000.00 USD | 256,010,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,240,000.00 USD | 256,240,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,540,000.00 USD | 256,540,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,930.00 USD | 488,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 257,100,000.00 USD | 257,100,000.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 257,840,000.00 USD | 257,840,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 258,890,000.00 USD | 258,890,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 260,220,000.00 USD | 260,220,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 260,420,000.00 USD | 260,420,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 260,730,000.00 USD | 260,730,000.00 USD | 67,230.00 USD | 65,630.00 USD | 183,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,280.00 USD | 582,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 988.72 USD | 583,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 583,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 697,610.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,150.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,630.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 11,570.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,390.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 679.21 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 123.63 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 4,260,000.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 239.15 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,660.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,210.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 4,850.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 135,940.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 298.15 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,060.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 110.17 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 4,070.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 1,230.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 8,390.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 591.43 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 808.37 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 130,410.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 5,420.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 19,040.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 173,030.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 12,360.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 108,590.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 4,960,000.00 USD | 11,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,880,000.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 56,390.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 2,930,000.00 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 257,200.00 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 312,150.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 807.17 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 266,860.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 1,340.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 397.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 405,000.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 989.78 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 584.39 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 373.50 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 806.57 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 249,460.00 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.13` | 926.59 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 631.42 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,630.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.02 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.94 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 2,130.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.89 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 62,200.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 79,110.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 83,090.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 104.19 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 142.91 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 122,260.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 106.95 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 3,580.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 11,860.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 2,850.00 USD | 18,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 3,610,000.00 USD | 22,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 678.62 USD | 22,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 117,850.00 USD | 22,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 3,910.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 360.88 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 23,250.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 337.96 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,470,000.00 USD | 0.00 USD | 8,750.00 USD | `-79.66%` | `34,317.00` |
| `Live` | `Long` | `0.2750` | 64,460,000.00 USD | 0.00 USD | 1,090.00 USD | `-78.06%` | `3,950.00` |
| `Live` | `Long` | `0.2850` | 64,460,000.00 USD | 0.00 USD | 25,980.00 USD | `-77.26%` | `91,168.00` |
| `Live` | `Long` | `0.2950` | 64,440,000.00 USD | 0.00 USD | 20,650.00 USD | `-76.46%` | `69,994.00` |
| `Live` | `Long` | `0.3050` | 64,410,000.00 USD | 0.00 USD | 9,190.00 USD | `-75.67%` | `30,141.00` |
| `Live` | `Long` | `0.3150` | 64,410,000.00 USD | 0.00 USD | 5,840.00 USD | `-74.87%` | `18,525.00` |
| `Live` | `Long` | `0.3350` | 64,400,000.00 USD | 0.00 USD | 28,240.00 USD | `-73.27%` | `84,306.00` |
| `Live` | `Long` | `0.3450` | 64,370,000.00 USD | 0.00 USD | 6,060.00 USD | `-72.47%` | `17,571.00` |
| `Live` | `Long` | `0.3550` | 64,370,000.00 USD | 0.00 USD | 1,280.00 USD | `-71.68%` | `3,619.00` |
| `Live` | `Long` | `0.3650` | 64,360,000.00 USD | 0.00 USD | 4,090.00 USD | `-70.88%` | `11,212.00` |
| `Live` | `Long` | `0.3750` | 64,360,000.00 USD | 0.00 USD | 6,600.00 USD | `-70.08%` | `17,605.00` |
| `Live` | `Long` | `0.3950` | 64,350,000.00 USD | 0.00 USD | 139,290.00 USD | `-68.49%` | `352,642.00` |
| `Live` | `Long` | `0.4050` | 64,210,000.00 USD | 0.00 USD | 530,660.00 USD | `-67.69%` | `1,310,276.00` |
| `Live` | `Long` | `0.4150` | 63,680,000.00 USD | 0.00 USD | 509.62 USD | `-66.89%` | `1,228.00` |
| `Live` | `Long` | `0.4250` | 63,680,000.00 USD | 0.00 USD | 3,700.00 USD | `-66.09%` | `8,700.00` |
| `Live` | `Long` | `0.4350` | 63,680,000.00 USD | 0.00 USD | 15,820.00 USD | `-65.29%` | `36,365.00` |
| `Live` | `Long` | `0.4550` | 63,660,000.00 USD | 0.00 USD | 632.90 USD | `-63.70%` | `1,391.00` |
| `Live` | `Long` | `0.4750` | 63,660,000.00 USD | 0.00 USD | 4,610.00 USD | `-62.10%` | `9,705.00` |
| `Live` | `Long` | `0.4850` | 63,660,000.00 USD | 0.00 USD | 13,480.00 USD | `-61.31%` | `27,793.00` |
| `Live` | `Long` | `0.4950` | 63,640,000.00 USD | 0.00 USD | 2,220.00 USD | `-60.51%` | `4,475.00` |
| `Live` | `Long` | `0.5050` | 63,640,000.00 USD | 0.00 USD | 2,660.00 USD | `-59.71%` | `5,258.00` |
| `Live` | `Long` | `0.5150` | 63,640,000.00 USD | 0.00 USD | 8,250.00 USD | `-58.91%` | `16,012.00` |
| `Live` | `Long` | `0.5250` | 63,630,000.00 USD | 0.00 USD | 2,340.00 USD | `-58.11%` | `4,460.00` |
| `Live` | `Long` | `0.5350` | 63,630,000.00 USD | 0.00 USD | 3,420.00 USD | `-57.32%` | `6,390.00` |
| `Live` | `Long` | `0.5450` | 63,630,000.00 USD | 0.00 USD | 164,540.00 USD | `-56.52%` | `301,902.00` |
| `Live` | `Long` | `0.5550` | 63,460,000.00 USD | 0.00 USD | 1,110.00 USD | `-55.72%` | `2,009.00` |
| `Live` | `Long` | `0.5650` | 63,460,000.00 USD | 0.00 USD | 1,600.00 USD | `-54.92%` | `2,839.00` |
| `Live` | `Long` | `0.5750` | 63,460,000.00 USD | 0.00 USD | 7,820.00 USD | `-54.12%` | `13,601.00` |
| `Live` | `Long` | `0.5850` | 63,450,000.00 USD | 0.00 USD | 1,970.00 USD | `-53.33%` | `3,376.00` |
| `Live` | `Long` | `0.5950` | 63,450,000.00 USD | 0.00 USD | 5,380.00 USD | `-52.53%` | `9,046.00` |
| `Live` | `Long` | `0.6050` | 63,440,000.00 USD | 0.00 USD | 24,310.00 USD | `-51.73%` | `40,178.00` |
| `Live` | `Long` | `0.6150` | 63,420,000.00 USD | 0.00 USD | 32,120.00 USD | `-50.93%` | `52,223.00` |
| `Live` | `Long` | `0.6250` | 63,390,000.00 USD | 0.00 USD | 33,040.00 USD | `-50.14%` | `52,858.00` |
| `Live` | `Long` | `0.6350` | 63,350,000.00 USD | 0.00 USD | 11,070.00 USD | `-49.34%` | `17,430.00` |
| `Live` | `Long` | `0.6450` | 63,340,000.00 USD | 0.00 USD | 21,460.00 USD | `-48.54%` | `33,272.00` |
| `Live` | `Long` | `0.6550` | 63,320,000.00 USD | 0.00 USD | 5,440.00 USD | `-47.74%` | `8,312.00` |
| `Live` | `Long` | `0.6650` | 63,320,000.00 USD | 0.00 USD | 17,830.00 USD | `-46.94%` | `26,813.00` |
| `Live` | `Long` | `0.6750` | 63,300,000.00 USD | 0.00 USD | 37,140.00 USD | `-46.15%` | `55,029.00` |
| `Live` | `Long` | `0.6850` | 63,260,000.00 USD | 0.00 USD | 5,800.00 USD | `-45.35%` | `8,473.00` |
| `Live` | `Long` | `0.6950` | 63,250,000.00 USD | 0.00 USD | 161,800.00 USD | `-44.55%` | `232,806.00` |
| `Live` | `Long` | `0.7050` | 63,090,000.00 USD | 0.00 USD | 19,510.00 USD | `-43.75%` | `27,677.00` |
| `Live` | `Long` | `0.7150` | 63,070,000.00 USD | 0.00 USD | 70,640.00 USD | `-42.96%` | `98,791.00` |
| `Live` | `Long` | `0.7250` | 63,000,000.00 USD | 0.00 USD | 245,330.00 USD | `-42.16%` | `338,391.00` |
| `Live` | `Long` | `0.7350` | 62,760,000.00 USD | 0.00 USD | 73,300.00 USD | `-41.36%` | `99,726.00` |
| `Live` | `Long` | `0.7450` | 62,680,000.00 USD | 0.00 USD | 113,230.00 USD | `-40.56%` | `151,990.00` |
| `Live` | `Long` | `0.7550` | 62,570,000.00 USD | 0.00 USD | 88,950.00 USD | `-39.76%` | `117,815.00` |
| `Live` | `Long` | `0.7650` | 62,480,000.00 USD | 0.00 USD | 2,190.00 USD | `-38.97%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 62,480,000.00 USD | 0.00 USD | 7,080.00 USD | `-38.17%` | `9,140.00` |
| `Live` | `Long` | `0.7850` | 62,470,000.00 USD | 0.00 USD | 507,020.00 USD | `-37.37%` | `645,886.00` |
| `Live` | `Long` | `0.7950` | 61,970,000.00 USD | 0.00 USD | 19,410.00 USD | `-36.57%` | `24,409.00` |
| `Live` | `Long` | `0.8050` | 61,950,000.00 USD | 0.00 USD | 17,740.00 USD | `-35.77%` | `22,042.00` |
| `Live` | `Long` | `0.8150` | 61,930,000.00 USD | 0.00 USD | 2,940,000.00 USD | `-34.98%` | `3,602,095.00` |
| `Live` | `Long` | `0.8250` | 58,990,000.00 USD | 0.00 USD | 136,650.00 USD | `-34.18%` | `165,633.00` |
| `Live` | `Long` | `0.8350` | 58,860,000.00 USD | 0.00 USD | 42,390.00 USD | `-33.38%` | `50,768.00` |
| `Live` | `Long` | `0.8450` | 58,810,000.00 USD | 0.00 USD | 59,040.00 USD | `-32.58%` | `69,872.00` |
| `Live` | `Long` | `0.8550` | 58,750,000.00 USD | 0.00 USD | 56,260.00 USD | `-31.79%` | `65,798.00` |
| `Live` | `Long` | `0.8650` | 58,700,000.00 USD | 0.00 USD | 14,630.00 USD | `-30.99%` | `16,919.00` |
| `Live` | `Long` | `0.8750` | 58,680,000.00 USD | 0.00 USD | 107,360.00 USD | `-30.19%` | `122,695.00` |
| `Live` | `Long` | `0.8850` | 58,580,000.00 USD | 0.00 USD | 352,960.00 USD | `-29.39%` | `398,825.00` |
| `Live` | `Long` | `0.8950` | 58,220,000.00 USD | 0.00 USD | 87,440.00 USD | `-28.59%` | `97,701.00` |
| `Live` | `Long` | `0.9050` | 58,140,000.00 USD | 0.00 USD | 163,090.00 USD | `-27.80%` | `180,215.00` |
| `Live` | `Long` | `0.9150` | 57,970,000.00 USD | 0.00 USD | 136,030.00 USD | `-27.00%` | `148,666.00` |
| `Live` | `Long` | `0.9250` | 57,840,000.00 USD | 0.00 USD | 69,680.00 USD | `-26.20%` | `75,328.00` |
| `Live` | `Long` | `0.9350` | 57,770,000.00 USD | 0.00 USD | 199,270.00 USD | `-25.40%` | `213,126.00` |
| `Live` | `Long` | `0.9450` | 57,570,000.00 USD | 0.00 USD | 57,060.00 USD | `-24.61%` | `60,378.00` |
| `Live` | `Long` | `0.9550` | 57,510,000.00 USD | 0.00 USD | 152,100.00 USD | `-23.81%` | `159,272.00` |
| `Live` | `Long` | `0.9650` | 57,360,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-23.01%` | `35,121,040.00` |
| `Live` | `Long` | `0.9750` | 23,470,000.00 USD | 0.00 USD | 177,550.00 USD | `-22.21%` | `182,104.00` |
| `Live` | `Long` | `0.9850` | 23,290,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-21.41%` | `3,031,520.00` |
| `Live` | `Long` | `0.9950` | 20,300,000.00 USD | 0.00 USD | 130,060.00 USD | `-20.62%` | `130,718.00` |
| `Live` | `Long` | `1.00` | 20,170,000.00 USD | 0.00 USD | 490,240.00 USD | `-19.82%` | `487,803.00` |
| `Live` | `Long` | `1.01` | 19,680,000.00 USD | 0.00 USD | 346,370.00 USD | `-19.02%` | `341,252.00` |
| `Live` | `Long` | `1.02` | 19,340,000.00 USD | 0.00 USD | 59,550.00 USD | `-18.22%` | `58,097.00` |
| `Live` | `Long` | `1.03` | 19,280,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-17.42%` | `2,048,357.00` |
| `Live` | `Long` | `1.04` | 17,160,000.00 USD | 0.00 USD | 660,310.00 USD | `-16.63%` | `631,874.00` |
| `Live` | `Long` | `1.05` | 16,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | `-15.83%` | `1,419,096.00` |
| `Live` | `Long` | `1.06` | 15,000,000.00 USD | 0.00 USD | 378,350.00 USD | `-15.03%` | `355,256.00` |
| `Live` | `Long` | `1.07` | 14,620,000.00 USD | 0.00 USD | 950,500.00 USD | `-14.23%` | `884,182.00` |
| `Live` | `Long` | `1.08` | 13,670,000.00 USD | 0.00 USD | 191,170.00 USD | `-13.44%` | `176,192.00` |
| `Live` | `Long` | `1.09` | 13,480,000.00 USD | 0.00 USD | 361,000.00 USD | `-12.64%` | `329,682.00` |
| `Live` | `Long` | `1.10` | 13,120,000.00 USD | 0.00 USD | 388,580.00 USD | `-11.84%` | `351,656.00` |
| `Live` | `Long` | `1.11` | 12,730,000.00 USD | 0.00 USD | 283,400.00 USD | `-11.04%` | `254,169.00` |
| `Live` | `Long` | `1.12` | 12,450,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-10.24%` | `1,986,295.00` |
| `Live` | `Long` | `1.14` | 10,210,000.00 USD | 0.00 USD | 129,840.00 USD | `-9.45%` | `114,400.00` |
| `Live` | `Long` | `1.15` | 10,080,000.00 USD | 0.00 USD | 306,590.00 USD | `-8.65%` | `267,767.00` |
| `Live` | `Long` | `1.16` | 9,780,000.00 USD | 0.00 USD | 337,540.00 USD | `-7.85%` | `292,239.00` |
| `Live` | `Long` | `1.17` | 9,440,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-7.05%` | `1,105,276.00` |
| `Live` | `Long` | `1.18` | 8,150,000.00 USD | 0.00 USD | 394,220.00 USD | `-6.25%` | `335,506.00` |
| `Live` | `Long` | `1.19` | 7,760,000.00 USD | 0.00 USD | 520,520.00 USD | `-5.46%` | `439,259.00` |
| `Live` | `Long` | `1.20` | 7,240,000.00 USD | 0.00 USD | 672,400.00 USD | `-4.66%` | `562,674.00` |
| `Live` | `Long` | `1.21` | 6,560,000.00 USD | 0.00 USD | 12,330.00 USD | `-3.86%` | `10,233.00` |
| `Live` | `Long` | `1.22` | 6,550,000.00 USD | 0.00 USD | 40,860.00 USD | `-3.06%` | `33,630.00` |
| `Live` | `Long` | `1.23` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | `-2.27%` | `5,314,604.00` |
| `Live` | `Short` | `1.25` | 559.73 USD | 559.73 USD | 0.00 USD | `+0.13%` | `446.00` |
| `Live` | `Short` | `1.26` | 117,500.00 USD | 116,940.00 USD | 0.00 USD | `+0.93%` | `92,442.00` |
| `Live` | `Short` | `1.27` | 133,090.00 USD | 15,590.00 USD | 0.00 USD | `+1.72%` | `12,225.00` |
| `Live` | `Short` | `1.28` | 181,830.00 USD | 48,740.00 USD | 0.00 USD | `+2.52%` | `37,930.00` |
| `Live` | `Short` | `1.30` | 183,450.00 USD | 1,630.00 USD | 0.00 USD | `+4.12%` | `1,246.00` |
| `Live` | `Short` | `1.32` | 220,410.00 USD | 36,960.00 USD | 0.00 USD | `+5.71%` | `27,896.00` |
| `Live` | `Short` | `1.33` | 222,370.00 USD | 1,950.00 USD | 0.00 USD | `+6.51%` | `1,462.00` |
| `Live` | `Short` | `1.34` | 239,450.00 USD | 17,080.00 USD | 0.00 USD | `+7.31%` | `12,702.00` |
| `Live` | `Short` | `1.35` | 242,150.00 USD | 2,700.00 USD | 0.00 USD | `+8.11%` | `1,989.00` |
| `Live` | `Short` | `1.36` | 435,510.00 USD | 193,360.00 USD | 0.00 USD | `+8.90%` | `141,656.00` |
| `Live` | `Short` | `1.38` | 497,230.00 USD | 61,720.00 USD | 0.00 USD | `+9.70%` | `44,888.00` |
| `Live` | `Short` | `1.39` | 498,500.00 USD | 1,280.00 USD | 0.00 USD | `+10.50%` | `921.00` |
| `Live` | `Short` | `1.40` | 500,590.00 USD | 2,090.00 USD | 0.00 USD | `+11.30%` | `1,500.00` |
| `Live` | `Short` | `1.41` | 518,360.00 USD | 17,770.00 USD | 0.00 USD | `+12.10%` | `12,646.00` |
| `Live` | `Short` | `1.42` | 522,290.00 USD | 3,930.00 USD | 0.00 USD | `+12.89%` | `2,776.00` |
| `Live` | `Short` | `1.43` | 615,800.00 USD | 93,510.00 USD | 0.00 USD | `+13.69%` | `65,619.00` |
| `Live` | `Short` | `1.44` | 619,600.00 USD | 3,800.00 USD | 0.00 USD | `+14.49%` | `2,649.00` |
| `Live` | `Short` | `1.45` | 619,880.00 USD | 284.66 USD | 0.00 USD | `+15.29%` | `197.00` |
| `Live` | `Short` | `1.46` | 1,180,000.00 USD | 565,040.00 USD | 0.00 USD | `+16.08%` | `388,344.00` |
| `Live` | `Short` | `1.47` | 1,310,000.00 USD | 128,580.00 USD | 0.00 USD | `+16.88%` | `87,771.00` |
| `Live` | `Short` | `1.50` | 1,330,000.00 USD | 12,470.00 USD | 0.00 USD | `+19.28%` | `8,338.00` |
| `Live` | `Short` | `1.51` | 1,340,000.00 USD | 11,570.00 USD | 0.00 USD | `+20.87%` | `7,640.00` |
| `Live` | `Short` | `1.53` | 1,340,000.00 USD | 174.99 USD | 0.00 USD | `+22.47%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,340,000.00 USD | 1,370.00 USD | 0.00 USD | `+23.26%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,340,000.00 USD | 1,360.00 USD | 0.00 USD | `+24.06%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,340,000.00 USD | 679.21 USD | 0.00 USD | `+24.86%` | `434.00` |
| `Live` | `Short` | `1.57` | 1,340,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.66%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,350,000.00 USD | 4,540.00 USD | 0.00 USD | `+26.46%` | `2,867.00` |
| `Live` | `Short` | `1.59` | 5,610,000.00 USD | 4,260,000.00 USD | 0.00 USD | `+27.25%` | `2,672,981.00` |
| `Live` | `Short` | `1.60` | 5,610,000.00 USD | 239.15 USD | 0.00 USD | `+28.05%` | `149.00` |
| `Live` | `Short` | `1.61` | 5,620,000.00 USD | 4,590.00 USD | 0.00 USD | `+28.85%` | `2,842.00` |
| `Live` | `Short` | `1.62` | 5,620,000.00 USD | 271.38 USD | 0.00 USD | `+29.65%` | `167.00` |
| `Live` | `Short` | `1.64` | 5,620,000.00 USD | 3,530.00 USD | 0.00 USD | `+30.45%` | `2,160.00` |
| `Live` | `Short` | `1.65` | 5,760,000.00 USD | 135,940.00 USD | 0.00 USD | `+31.24%` | `82,639.00` |
| `Live` | `Short` | `1.66` | 5,760,000.00 USD | 147.30 USD | 0.00 USD | `+32.04%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,760,000.00 USD | 586.08 USD | 0.00 USD | `+32.84%` | `352.00` |
| `Live` | `Short` | `1.69` | 5,760,000.00 USD | 4,180.00 USD | 0.00 USD | `+34.43%` | `2,481.00` |
| `Live` | `Short` | `1.70` | 5,760,000.00 USD | 974.62 USD | 0.00 USD | `+35.23%` | `575.00` |
| `Live` | `Short` | `1.71` | 5,770,000.00 USD | 4,200.00 USD | 0.00 USD | `+36.03%` | `2,466.00` |
| `Live` | `Short` | `1.72` | 5,770,000.00 USD | 5,250.00 USD | 0.00 USD | `+36.83%` | `3,059.00` |
| `Live` | `Short` | `1.73` | 5,770,000.00 USD | 1,430.00 USD | 0.00 USD | `+37.63%` | `829.00` |
| `Live` | `Short` | `1.74` | 5,780,000.00 USD | 2,970.00 USD | 0.00 USD | `+38.42%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 5,780,000.00 USD | 2,730.00 USD | 0.00 USD | `+39.22%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 5,780,000.00 USD | 591.43 USD | 0.00 USD | `+40.02%` | `337.00` |
| `Live` | `Short` | `1.76` | 5,780,000.00 USD | 808.37 USD | 0.00 USD | `+40.82%` | `458.00` |
| `Live` | `Short` | `1.77` | 5,780,000.00 USD | 876.85 USD | 0.00 USD | `+41.61%` | `494.00` |
| `Live` | `Short` | `1.78` | 11,110,000.00 USD | 5,330,000.00 USD | 0.00 USD | `+42.41%` | `2,986,501.00` |
| `Live` | `Short` | `1.79` | 11,110,000.00 USD | 2,690.00 USD | 0.00 USD | `+43.21%` | `1,500.00` |
| `Live` | `Short` | `1.80` | 11,120,000.00 USD | 889.87 USD | 0.00 USD | `+44.01%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,310,000.00 USD | 190,860.00 USD | 0.00 USD | `+44.81%` | `105,157.00` |
| `Live` | `Short` | `1.82` | 11,310,000.00 USD | 260.98 USD | 0.00 USD | `+45.60%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,310,000.00 USD | 425.72 USD | 0.00 USD | `+46.40%` | `232.00` |
| `Live` | `Short` | `1.84` | 11,430,000.00 USD | 120,750.00 USD | 0.00 USD | `+47.20%` | `65,447.00` |
| `Live` | `Short` | `1.85` | 11,430,000.00 USD | 428.50 USD | 0.00 USD | `+48.00%` | `231.00` |
| `Live` | `Short` | `1.86` | 14,300,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+48.80%` | `1,541,696.00` |
| `Live` | `Short` | `1.89` | 17,190,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+50.39%` | `1,529,461.00` |
| `Live` | `Short` | `1.90` | 17,190,000.00 USD | 4,190.00 USD | 0.00 USD | `+51.19%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 17,450,000.00 USD | 256,010.00 USD | 0.00 USD | `+51.99%` | `134,388.00` |
| `Live` | `Short` | `1.92` | 17,450,000.00 USD | 160.86 USD | 0.00 USD | `+52.78%` | `84.00` |
| `Live` | `Short` | `1.93` | 17,490,000.00 USD | 39,740.00 USD | 0.00 USD | `+53.58%` | `20,643.00` |
| `Live` | `Short` | `1.94` | 17,800,000.00 USD | 315,580.00 USD | 0.00 USD | `+54.38%` | `163,092.00` |
| `Live` | `Short` | `1.96` | 17,800,000.00 USD | 293.25 USD | 0.00 USD | `+55.98%` | `150.00` |
| `Live` | `Short` | `1.97` | 18,030,000.00 USD | 228,250.00 USD | 0.00 USD | `+56.77%` | `116,156.00` |
| `Live` | `Short` | `1.98` | 18,030,000.00 USD | 651.75 USD | 0.00 USD | `+57.57%` | `330.00` |
| `Live` | `Short` | `2.00` | 18,030,000.00 USD | 164.41 USD | 0.00 USD | `+59.96%` | `82.00` |
| `Live` | `Short` | `2.02` | 18,030,000.00 USD | 513.83 USD | 0.00 USD | `+60.76%` | `255.00` |
| `Live` | `Short` | `2.02` | 18,030,000.00 USD | 121.50 USD | 0.00 USD | `+61.56%` | `60.00` |
| `Live` | `Short` | `2.04` | 18,030,000.00 USD | 787.55 USD | 0.00 USD | `+62.36%` | `387.00` |
| `Live` | `Short` | `2.04` | 18,440,000.00 USD | 409,200.00 USD | 0.00 USD | `+63.16%` | `200,097.00` |
| `Live` | `Short` | `2.06` | 18,440,000.00 USD | 832.19 USD | 0.00 USD | `+64.75%` | `403.00` |
| `Live` | `Short` | `2.10` | 18,440,000.00 USD | 1,240.00 USD | 0.00 USD | `+67.15%` | `592.00` |
| `Live` | `Short` | `2.10` | 18,440,000.00 USD | 294.70 USD | 0.00 USD | `+67.94%` | `140.00` |
| `Live` | `Short` | `2.12` | 18,700,000.00 USD | 251,390.00 USD | 0.00 USD | `+68.74%` | `118,859.00` |
| `Live` | `Short` | `2.13` | 18,710,000.00 USD | 16,560.00 USD | 0.00 USD | `+70.34%` | `7,757.00` |
| `Live` | `Short` | `2.15` | 18,710,000.00 USD | 196.11 USD | 0.00 USD | `+71.93%` | `91.00` |
| `Live` | `Short` | `2.17` | 18,710,000.00 USD | 437.33 USD | 0.00 USD | `+72.73%` | `202.00` |
| `Live` | `Short` | `2.17` | 18,720,000.00 USD | 2,730.00 USD | 0.00 USD | `+73.53%` | `1,253.00` |
| `Live` | `Short` | `2.19` | 18,720,000.00 USD | 100.51 USD | 0.00 USD | `+74.33%` | `46.00` |
| `Live` | `Short` | `2.19` | 18,850,000.00 USD | 132,960.00 USD | 0.00 USD | `+75.12%` | `60,572.00` |
| `Live` | `Short` | `2.21` | 18,850,000.00 USD | 101.89 USD | 0.00 USD | `+76.72%` | `46.00` |
| `Live` | `Short` | `2.23` | 18,860,000.00 USD | 11,460.00 USD | 0.00 USD | `+77.52%` | `5,152.00` |
| `Live` | `Short` | `2.23` | 18,860,000.00 USD | 102.81 USD | 0.00 USD | `+78.31%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,860,000.00 USD | 103.27 USD | 0.00 USD | `+79.11%` | `46.00` |
| `Live` | `Short` | `2.29` | 18,980,000.00 USD | 121,240.00 USD | 0.00 USD | `+83.10%` | `52,830.00` |
| `Live` | `Short` | `2.31` | 18,980,000.00 USD | 212.06 USD | 0.00 USD | `+83.90%` | `92.00` |
| `Live` | `Short` | `2.31` | 18,980,000.00 USD | 250.02 USD | 0.00 USD | `+84.70%` | `108.00` |
| `Live` | `Short` | `2.33` | 18,990,000.00 USD | 2,850.00 USD | 0.00 USD | `+85.50%` | `1,227.00` |
| `Live` | `Short` | `2.33` | 19,000,000.00 USD | 11,810.00 USD | 0.00 USD | `+86.29%` | `5,057.00` |
| `Live` | `Short` | `2.35` | 19,000,000.00 USD | 469.00 USD | 0.00 USD | `+87.09%` | `200.00` |
| `Live` | `Short` | `2.35` | 19,000,000.00 USD | 2,570.00 USD | 0.00 USD | `+87.89%` | `1,090.00` |
| `Live` | `Short` | `2.37` | 19,000,000.00 USD | 551.05 USD | 0.00 USD | `+88.69%` | `233.00` |
| `Live` | `Short` | `2.38` | 22,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | `+89.48%` | `1,511,779.00` |
| `Live` | `Short` | `2.40` | 22,690,000.00 USD | 94,360.00 USD | 0.00 USD | `+91.08%` | `39,397.00` |
| `Live` | `Short` | `2.42` | 22,690,000.00 USD | 1,160.00 USD | 0.00 USD | `+92.68%` | `481.00` |
| `Live` | `Short` | `2.42` | 22,690,000.00 USD | 169.75 USD | 0.00 USD | `+93.47%` | `70.00` |
| `Live` | `Short` | `2.44` | 22,710,000.00 USD | 24,510.00 USD | 0.00 USD | `+94.27%` | `10,065.00` |
| `Live` | `Short` | `2.44` | 22,720,000.00 USD | 3,580.00 USD | 0.00 USD | `+95.07%` | `1,463.00` |
| `Live` | `Short` | `2.46` | 22,720,000.00 USD | 360.88 USD | 0.00 USD | `+95.87%` | `147.00` |
| `Live` | `Short` | `2.46` | 22,740,000.00 USD | 23,250.00 USD | 0.00 USD | `+96.67%` | `9,432.00` |
| `Live` | `Short` | `2.48` | 22,740,000.00 USD | 306.90 USD | 0.00 USD | `+97.46%` | `124.00` |
| `Live` | `Short` | `2.48` | 22,830,000.00 USD | 95,780.00 USD | 0.00 USD | `+98.26%` | `38,544.00` |
| `Live` | `Short` | `2.50` | 23,040,000.00 USD | 201,990.00 USD | 0.00 USD | `+99.06%` | `80,958.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 2,180,000.00 USD | 0.00 USD | 102.00 USD | `-79.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 2,180,000.00 USD | 0.00 USD | 351.50 USD | `-70.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 2,180,000.00 USD | 0.00 USD | 139.12 USD | `-70.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 2,180,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 2,180,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 2,170,000.00 USD | 0.00 USD | 408.51 USD | `-64.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 2,170,000.00 USD | 0.00 USD | 273.00 USD | `-63.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 2,170,000.00 USD | 0.00 USD | 151.12 USD | `-62.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 2,170,000.00 USD | 0.00 USD | 142.50 USD | `-62.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 2,170,000.00 USD | 0.00 USD | 145.50 USD | `-61.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 2,170,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 2,170,000.00 USD | 0.00 USD | 285.82 USD | `-58.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 2,170,000.00 USD | 0.00 USD | 306.60 USD | `-58.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 2,170,000.00 USD | 0.00 USD | 121.55 USD | `-55.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 2,170,000.00 USD | 0.00 USD | 656.53 USD | `-54.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 2,170,000.00 USD | 0.00 USD | 100.62 USD | `-53.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 2,170,000.00 USD | 0.00 USD | 203.75 USD | `-50.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 2,170,000.00 USD | 0.00 USD | 791.85 USD | `-49.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 2,170,000.00 USD | 0.00 USD | 573.40 USD | `-48.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 2,170,000.00 USD | 0.00 USD | 244.31 USD | `-47.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 2,170,000.00 USD | 0.00 USD | 29,530.00 USD | `-46.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 2,140,000.00 USD | 0.00 USD | 503.55 USD | `-46.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 2,140,000.00 USD | 0.00 USD | 480.19 USD | `-45.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 2,140,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 2,130,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 2,120,000.00 USD | 0.00 USD | 228.80 USD | `-42.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 2,120,000.00 USD | 0.00 USD | 536.50 USD | `-42.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 2,120,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 2,120,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 2,120,000.00 USD | 0.00 USD | 878.48 USD | `-36.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 2,120,000.00 USD | 0.00 USD | 6,020.00 USD | `-34.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 2,110,000.00 USD | 0.00 USD | 1,360.00 USD | `-31.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 2,110,000.00 USD | 0.00 USD | 690.38 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 2,110,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 2,110,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 2,110,000.00 USD | 0.00 USD | 838.94 USD | `-27.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 2,110,000.00 USD | 0.00 USD | 338.55 USD | `-27.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 2,110,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 2,100,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 2,100,000.00 USD | 0.00 USD | 112.46 USD | `-24.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 2,100,000.00 USD | 0.00 USD | 1,730.00 USD | `-23.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 2,100,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 2,100,000.00 USD | 0.00 USD | 6,200.00 USD | `-22.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 2,090,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 2,090,000.00 USD | 0.00 USD | 902.47 USD | `-20.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,090,000.00 USD | 0.00 USD | 15,420.00 USD | `-19.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,070,000.00 USD | 0.00 USD | 6,640.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 2,060,000.00 USD | 0.00 USD | 1,840.00 USD | `-18.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 2,060,000.00 USD | 0.00 USD | 42,670.00 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 2,020,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 2,020,000.00 USD | 0.00 USD | 24,230.00 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,990,000.00 USD | 0.00 USD | 4,570.00 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,990,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,940,000.00 USD | 0.00 USD | 3,690.00 USD | `-13.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,940,000.00 USD | 0.00 USD | 279,970.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,660,000.00 USD | 0.00 USD | 21,590.00 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,630,000.00 USD | 0.00 USD | 9,410.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,630,000.00 USD | 0.00 USD | 101,980.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,520,000.00 USD | 0.00 USD | 13,490.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,510,000.00 USD | 0.00 USD | 120,050.00 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,390,000.00 USD | 0.00 USD | 40,320.00 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,350,000.00 USD | 0.00 USD | 42,080.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,310,000.00 USD | 0.00 USD | 94,830.00 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 1,210,000.00 USD | 0.00 USD | 221,020.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 991,250.00 USD | 0.00 USD | 409,570.00 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 581,680.00 USD | 0.00 USD | 93,540.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 488,140.00 USD | 0.00 USD | 289,680.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 198,450.00 USD | 0.00 USD | 22,330.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 176,120.00 USD | 0.00 USD | 86,220.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 89,900.00 USD | 0.00 USD | 89,900.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 74,830.00 USD | 74,830.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 378,850.00 USD | 304,020.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 397,010.00 USD | 18,160.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 647,790.00 USD | 250,780.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 702,030.00 USD | 54,240.00 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 944,760.00 USD | 242,720.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,590,000.00 USD | 649,810.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,810,000.00 USD | 214,110.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,860,000.00 USD | 47,230.00 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,970,000.00 USD | 112,700.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,980,000.00 USD | 14,640.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 2,230,000.00 USD | 249,240.00 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 2,310,000.00 USD | 81,760.00 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 2,370,000.00 USD | 53,860.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 2,370,000.00 USD | 3,960.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,220,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,220,000.00 USD | 3,710.00 USD | 0.00 USD | `+12.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,230,000.00 USD | 5,990.00 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,300,000.00 USD | 78,630.00 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,550,000.00 USD | 242,580.00 USD | 0.00 USD | `+15.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,550,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,580,000.00 USD | 23,260.00 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,690,000.00 USD | 108,020.00 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,700,000.00 USD | 14,970.00 USD | 0.00 USD | `+18.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,720,000.00 USD | 15,800.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,770,000.00 USD | 57,590.00 USD | 0.00 USD | `+20.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,790,000.00 USD | 11,760.00 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,810,000.00 USD | 19,430.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,850,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,860,000.00 USD | 10,870.00 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,860,000.00 USD | 2,380.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,870,000.00 USD | 6,450.00 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,880,000.00 USD | 5,570.00 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,890,000.00 USD | 10,250.00 USD | 0.00 USD | `+26.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 7,000,000.00 USD | 113,910.00 USD | 0.00 USD | `+27.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 7,040,000.00 USD | 40,290.00 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,120,000.00 USD | 80,330.00 USD | 0.00 USD | `+28.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,120,000.00 USD | 464.75 USD | 0.00 USD | `+29.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,300,000.00 USD | 179,860.00 USD | 0.00 USD | `+30.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,300,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,390,000.00 USD | 85,010.00 USD | 0.00 USD | `+32.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,400,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,410,000.00 USD | 18,400.00 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,480,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,500,000.00 USD | 18,000.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,720,000.00 USD | 217,560.00 USD | 0.00 USD | `+36.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,730,000.00 USD | 14,250.00 USD | 0.00 USD | `+36.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,740,000.00 USD | 3,980.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,780,000.00 USD | 43,240.00 USD | 0.00 USD | `+38.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,780,000.00 USD | 3,330.00 USD | 0.00 USD | `+39.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,790,000.00 USD | 9,200.00 USD | 0.00 USD | `+40.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,820,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,940,000.00 USD | 128,330.00 USD | 0.00 USD | `+41.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 8,040,000.00 USD | 96,600.00 USD | 0.00 USD | `+42.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,040,000.00 USD | 3,980.00 USD | 0.00 USD | `+43.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,040,000.00 USD | 254.51 USD | 0.00 USD | `+44.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,060,000.00 USD | 12,860.00 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,060,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,070,000.00 USD | 8,170.00 USD | 0.00 USD | `+46.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,070,000.00 USD | 843.17 USD | 0.00 USD | `+47.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,080,000.00 USD | 8,390.00 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,080,000.00 USD | 4,420.00 USD | 0.00 USD | `+49.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,080,000.00 USD | 591.89 USD | 0.00 USD | `+50.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,130,000.00 USD | 46,370.00 USD | 0.00 USD | `+51.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,140,000.00 USD | 9,270.00 USD | 0.00 USD | `+51.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,140,000.00 USD | 265.10 USD | 0.00 USD | `+54.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,140,000.00 USD | 2,040.00 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,140,000.00 USD | 807.42 USD | 0.00 USD | `+55.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,160,000.00 USD | 14,120.00 USD | 0.00 USD | `+56.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,160,000.00 USD | 4,010.00 USD | 0.00 USD | `+57.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,160,000.00 USD | 325.54 USD | 0.00 USD | `+58.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,170,000.00 USD | 7,020.00 USD | 0.00 USD | `+59.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,290,000.00 USD | 123,020.00 USD | 0.00 USD | `+59.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,290,000.00 USD | 3,350.00 USD | 0.00 USD | `+61.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,290,000.00 USD | 181.12 USD | 0.00 USD | `+62.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,300,000.00 USD | 382.41 USD | 0.00 USD | `+63.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,300,000.00 USD | 3,420.00 USD | 0.00 USD | `+64.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,300,000.00 USD | 661.93 USD | 0.00 USD | `+65.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,420,000.00 USD | 124,400.00 USD | 0.00 USD | `+67.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,430,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,440,000.00 USD | 13,900.00 USD | 0.00 USD | `+69.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,460,000.00 USD | 24,840.00 USD | 0.00 USD | `+71.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,510,000.00 USD | 50,580.00 USD | 0.00 USD | `+71.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,520,000.00 USD | 2,690.00 USD | 0.00 USD | `+72.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,520,000.00 USD | 2,180.00 USD | 0.00 USD | `+75.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,670,000.00 USD | 151,380.00 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,670,000.00 USD | 3,120.00 USD | 0.00 USD | `+81.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,680,000.00 USD | 1,140.00 USD | 0.00 USD | `+82.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,690,000.00 USD | 11,670.00 USD | 0.00 USD | `+83.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,690,000.00 USD | 370.40 USD | 0.00 USD | `+84.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,690,000.00 USD | 733.19 USD | 0.00 USD | `+86.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,690,000.00 USD | 2,410.00 USD | 0.00 USD | `+88.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,690,000.00 USD | 475.00 USD | 0.00 USD | `+89.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,690,000.00 USD | 1,190.00 USD | 0.00 USD | `+90.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,690,000.00 USD | 2,540.00 USD | 0.00 USD | `+91.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,700,000.00 USD | 1,590.00 USD | 0.00 USD | `+91.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,700,000.00 USD | 1,370.00 USD | 0.00 USD | `+92.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,720,000.00 USD | 19,590.00 USD | 0.00 USD | `+93.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,720,000.00 USD | 564.92 USD | 0.00 USD | `+94.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,730,000.00 USD | 8,110.00 USD | 0.00 USD | `+95.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,730,000.00 USD | 3,420.00 USD | 0.00 USD | `+98.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,730,000.00 USD | 124.75 USD | 0.00 USD | `+99.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,760,000.00 USD | 29,920.00 USD | 0.00 USD | `+99.86%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 78,580,000.00 USD | 0.00 USD | 78,580,000.00 USD | 23,750.00 USD | 0.00 USD | 39,860.00 USD |
| `7D` | `1.09` | 78,520,000.00 USD | 0.00 USD | 78,520,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 78,480,000.00 USD | 0.00 USD | 78,480,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 78,380,000.00 USD | 0.00 USD | 78,380,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `1D` | `1.09` | 68,350,000.00 USD | 0.00 USD | 68,350,000.00 USD | 0.00 USD | 64,380.00 USD | 16,540.00 USD |
| `1D` | `1.10` | 68,270,000.00 USD | 0.00 USD | 68,270,000.00 USD | 35,350.00 USD | 1,130.00 USD | 130,220.00 USD |
| `7D` | `1.10` | 78,340,000.00 USD | 0.00 USD | 78,340,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `1D` | `1.10` | 68,100,000.00 USD | 0.00 USD | 68,100,000.00 USD | 72,120.00 USD | 2,030.00 USD | 75,830.00 USD |
| `7D` | `1.10` | 78,340,000.00 USD | 0.00 USD | 78,340,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `1D` | `1.10` | 67,950,000.00 USD | 0.00 USD | 67,950,000.00 USD | 6,450.00 USD | 46,740.00 USD | 131,840.00 USD |
| `1D` | `1.10` | 67,760,000.00 USD | 0.00 USD | 67,760,000.00 USD | 72,970.00 USD | 27,450.00 USD | 64,210.00 USD |
| `7D` | `1.10` | 78,050,000.00 USD | 0.00 USD | 78,050,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `1D` | `1.10` | 67,600,000.00 USD | 0.00 USD | 67,600,000.00 USD | 3,520.00 USD | 361.50 USD | 67,060.00 USD |
| `1D` | `1.11` | 67,530,000.00 USD | 0.00 USD | 67,530,000.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD |
| `7D` | `1.11` | 78,050,000.00 USD | 0.00 USD | 78,050,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `1D` | `1.11` | 67,530,000.00 USD | 0.00 USD | 67,530,000.00 USD | 6,020.00 USD | 0.00 USD | 846.03 USD |
| `7D` | `1.11` | 78,040,000.00 USD | 0.00 USD | 78,040,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `1D` | `1.11` | 67,520,000.00 USD | 0.00 USD | 67,520,000.00 USD | 17,310.00 USD | 15,600.00 USD | 0.00 USD |
| `7D` | `1.11` | 78,040,000.00 USD | 0.00 USD | 78,040,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `1D` | `1.11` | 67,490,000.00 USD | 0.00 USD | 67,490,000.00 USD | 71,640.00 USD | 13,130.00 USD | 123,540.00 USD |
| `1D` | `1.11` | 67,280,000.00 USD | 0.00 USD | 67,280,000.00 USD | 0.00 USD | 3,300.00 USD | 1,840.00 USD |
| `7D` | `1.12` | 77,990,000.00 USD | 0.00 USD | 77,990,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 67,270,000.00 USD | 0.00 USD | 67,270,000.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD |
| `7D` | `1.12` | 77,970,000.00 USD | 0.00 USD | 77,970,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 67,150,000.00 USD | 0.00 USD | 67,150,000.00 USD | 7,460.00 USD | 48,180.00 USD | 41,970.00 USD |
| `1D` | `1.12` | 67,060,000.00 USD | 0.00 USD | 67,060,000.00 USD | 16,420.00 USD | 60,880.00 USD | 88,470.00 USD |
| `7D` | `1.12` | 77,900,000.00 USD | 0.00 USD | 77,900,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `1.12` | 66,890,000.00 USD | 0.00 USD | 66,890,000.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD |
| `7D` | `1.12` | 77,870,000.00 USD | 0.00 USD | 77,870,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.12` | 66,800,000.00 USD | 0.00 USD | 66,800,000.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD |
| `1D` | `1.13` | 66,630,000.00 USD | 0.00 USD | 66,630,000.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD |
| `7D` | `1.13` | 77,660,000.00 USD | 0.00 USD | 77,660,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 66,510,000.00 USD | 0.00 USD | 66,510,000.00 USD | 69,610.00 USD | 60,790.00 USD | 140,470.00 USD |
| `7D` | `1.13` | 77,470,000.00 USD | 0.00 USD | 77,470,000.00 USD | 5,450.00 USD | 2,460.00 USD | 0.00 USD |
| `1D` | `1.13` | 66,240,000.00 USD | 0.00 USD | 66,240,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD |
| `7D` | `1.13` | 77,460,000.00 USD | 0.00 USD | 77,460,000.00 USD | 69,750.00 USD | 93,260.00 USD | 8,990.00 USD |
| `1D` | `1.13` | 66,000,000.00 USD | 0.00 USD | 66,000,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.13` | 77,290,000.00 USD | 0.00 USD | 77,290,000.00 USD | 74,920.00 USD | 97,060.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 65,950,000.00 USD | 0.00 USD | 65,950,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.14` | 76,890,000.00 USD | 0.00 USD | 76,890,000.00 USD | 79,780.00 USD | 88,050.00 USD | 71,350.00 USD |
| `1D` | `1.14` | 65,890,000.00 USD | 0.00 USD | 65,890,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.14` | 76,650,000.00 USD | 0.00 USD | 76,650,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 65,800,000.00 USD | 0.00 USD | 65,800,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.14` | 76,620,000.00 USD | 0.00 USD | 76,620,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 65,780,000.00 USD | 0.00 USD | 65,780,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD |
| `7D` | `1.14` | 76,580,000.00 USD | 0.00 USD | 76,580,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 65,710,000.00 USD | 0.00 USD | 65,710,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 76,450,000.00 USD | 0.00 USD | 76,450,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `1D` | `1.15` | 65,570,000.00 USD | 0.00 USD | 65,570,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 76,440,000.00 USD | 0.00 USD | 76,440,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.15` | 76,370,000.00 USD | 0.00 USD | 76,370,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `1D` | `1.15` | 65,540,000.00 USD | 0.00 USD | 65,540,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 76,000,000.00 USD | 0.00 USD | 76,000,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.15` | 75,850,000.00 USD | 0.00 USD | 75,850,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 65,520,000.00 USD | 0.00 USD | 65,520,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 75,680,000.00 USD | 0.00 USD | 75,680,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 65,320,000.00 USD | 0.00 USD | 65,320,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 74,800,000.00 USD | 0.00 USD | 74,800,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 64,980,000.00 USD | 0.00 USD | 64,980,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD |
| `7D` | `1.16` | 74,570,000.00 USD | 0.00 USD | 74,570,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 64,860,000.00 USD | 0.00 USD | 64,860,000.00 USD | 126,860.00 USD | 16,130.00 USD | 446,310.00 USD |
| `7D` | `1.16` | 73,700,000.00 USD | 0.00 USD | 73,700,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 64,270,000.00 USD | 0.00 USD | 64,270,000.00 USD | 253,200.00 USD | 126,280.00 USD | 170,950.00 USD |
| `7D` | `1.16` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 63,720,000.00 USD | 0.00 USD | 63,720,000.00 USD | 253,180.00 USD | 314,800.00 USD | 334,700.00 USD |
| `7D` | `1.16` | 71,320,000.00 USD | 0.00 USD | 71,320,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 62,810,000.00 USD | 0.00 USD | 62,810,000.00 USD | 95,890.00 USD | 51,030.00 USD | 486,240.00 USD |
| `7D` | `1.17` | 69,660,000.00 USD | 0.00 USD | 69,660,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 62,180,000.00 USD | 0.00 USD | 62,180,000.00 USD | 148,160.00 USD | 120,500.00 USD | 131,100.00 USD |
| `7D` | `1.17` | 68,310,000.00 USD | 0.00 USD | 68,310,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 61,780,000.00 USD | 0.00 USD | 61,780,000.00 USD | 135,220.00 USD | 101,000.00 USD | 210,200.00 USD |
| `7D` | `1.17` | 67,240,000.00 USD | 0.00 USD | 67,240,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 61,330,000.00 USD | 0.00 USD | 61,330,000.00 USD | 365,570.00 USD | 32,690.00 USD | 449,480.00 USD |
| `7D` | `1.17` | 65,210,000.00 USD | 0.00 USD | 65,210,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 60,490,000.00 USD | 0.00 USD | 60,490,000.00 USD | 104,550.00 USD | 90,830.00 USD | 392,460.00 USD |
| `7D` | `1.17` | 64,010,000.00 USD | 0.00 USD | 64,010,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 59,900,000.00 USD | 0.00 USD | 59,900,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD |
| `7D` | `1.18` | 62,440,000.00 USD | 0.00 USD | 62,440,000.00 USD | 181,850.00 USD | 100,190.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 58,950,000.00 USD | 0.00 USD | 58,950,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD |
| `7D` | `1.18` | 61,780,000.00 USD | 0.00 USD | 61,780,000.00 USD | 85,020.00 USD | 74,230.00 USD | 489,310.00 USD |
| `1D` | `1.18` | 58,580,000.00 USD | 0.00 USD | 58,580,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD |
| `7D` | `1.18` | 61,130,000.00 USD | 0.00 USD | 61,130,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD |
| `1D` | `1.18` | 58,250,000.00 USD | 0.00 USD | 58,250,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD |
| `7D` | `1.18` | 60,520,000.00 USD | 0.00 USD | 60,520,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 58,080,000.00 USD | 0.00 USD | 58,080,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD |
| `7D` | `1.18` | 60,250,000.00 USD | 0.00 USD | 60,250,000.00 USD | 299,450.00 USD | 571,980.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 57,250,000.00 USD | 0.00 USD | 57,250,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD |
| `7D` | `1.19` | 59,140,000.00 USD | 0.00 USD | 59,140,000.00 USD | 76,370.00 USD | 109,420.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 56,810,000.00 USD | 0.00 USD | 56,810,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD |
| `7D` | `1.19` | 58,250,000.00 USD | 0.00 USD | 58,250,000.00 USD | 250,710.00 USD | 115,630.00 USD | 585,020.00 USD |
| `1D` | `1.19` | 55,530,000.00 USD | 0.00 USD | 55,530,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD |
| `7D` | `1.19` | 57,300,000.00 USD | 0.00 USD | 57,300,000.00 USD | 227,280.00 USD | 92,240.00 USD | 795,050.00 USD |
| `1D` | `1.19` | 53,790,000.00 USD | 0.00 USD | 53,790,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD |
| `7D` | `1.19` | 56,190,000.00 USD | 0.00 USD | 56,190,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 53,310,000.00 USD | 0.00 USD | 53,310,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD |
| `7D` | `1.19` | 54,820,000.00 USD | 0.00 USD | 54,820,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD |
| `1D` | `1.20` | 52,200,000.00 USD | 0.00 USD | 52,200,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD |
| `7D` | `1.20` | 53,990,000.00 USD | 0.00 USD | 53,990,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD |
| `1D` | `1.20` | 49,620,000.00 USD | 0.00 USD | 49,620,000.00 USD | 748,570.00 USD | 84,750.00 USD | 788,910.00 USD |
| `7D` | `1.20` | 52,410,000.00 USD | 0.00 USD | 52,410,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 48,000,000.00 USD | 0.00 USD | 48,000,000.00 USD | 112,900.00 USD | 934,870.00 USD | 1,510,000.00 USD |
| `7D` | `1.20` | 49,400,000.00 USD | 0.00 USD | 49,400,000.00 USD | 736,290.00 USD | 330,310.00 USD | 18,590.00 USD |
| `1D` | `1.20` | 45,440,000.00 USD | 0.00 USD | 45,440,000.00 USD | 730,270.00 USD | 464,920.00 USD | 1,630,000.00 USD |
| `7D` | `1.20` | 48,310,000.00 USD | 0.00 USD | 48,310,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD |
| `1D` | `1.20` | 42,610,000.00 USD | 0.00 USD | 42,610,000.00 USD | 314,820.00 USD | 47,550.00 USD | 740,300.00 USD |
| `7D` | `1.20` | 47,440,000.00 USD | 0.00 USD | 47,440,000.00 USD | 47,500.00 USD | 589,990.00 USD | 5,570.00 USD |
| `1D` | `1.21` | 41,510,000.00 USD | 0.00 USD | 41,510,000.00 USD | 295,960.00 USD | 920,650.00 USD | 241,500.00 USD |
| `7D` | `1.21` | 46,800,000.00 USD | 0.00 USD | 46,800,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `1.21` | 40,050,000.00 USD | 0.00 USD | 40,050,000.00 USD | 778,920.00 USD | 104,970.00 USD | 1,290,000.00 USD |
| `7D` | `1.21` | 46,770,000.00 USD | 0.00 USD | 46,770,000.00 USD | 432,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.21` | 37,880,000.00 USD | 0.00 USD | 37,880,000.00 USD | 1,570,000.00 USD | 133,210.00 USD | 763,780.00 USD |
| `7D` | `1.21` | 46,340,000.00 USD | 0.00 USD | 46,340,000.00 USD | 257,960.00 USD | 326,720.00 USD | 2,870,000.00 USD |
| `1D` | `1.21` | 35,420,000.00 USD | 0.00 USD | 35,420,000.00 USD | 127,210.00 USD | 462,270.00 USD | 1,410,000.00 USD |
| `7D` | `1.21` | 42,880,000.00 USD | 0.00 USD | 42,880,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.21` | 33,420,000.00 USD | 0.00 USD | 33,420,000.00 USD | 1,350,000.00 USD | 271,760.00 USD | 998,520.00 USD |
| `7D` | `1.21` | 41,650,000.00 USD | 0.00 USD | 41,650,000.00 USD | 108,640.00 USD | 0.00 USD | 910,410.00 USD |
| `1D` | `1.22` | 30,800,000.00 USD | 0.00 USD | 30,800,000.00 USD | 52,290.00 USD | 154,650.00 USD | 685,980.00 USD |
| `7D` | `1.22` | 40,630,000.00 USD | 0.00 USD | 40,630,000.00 USD | 142,210.00 USD | 9,150.00 USD | 0.00 USD |
| `1D` | `1.22` | 29,910,000.00 USD | 0.00 USD | 29,910,000.00 USD | 307,460.00 USD | 26,150.00 USD | 176,390.00 USD |
| `7D` | `1.22` | 40,480,000.00 USD | 0.00 USD | 40,480,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 29,400,000.00 USD | 0.00 USD | 29,400,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD |
| `7D` | `1.22` | 39,750,000.00 USD | 0.00 USD | 39,750,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 29,130,000.00 USD | 0.00 USD | 29,130,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD |
| `7D` | `1.22` | 38,660,000.00 USD | 0.00 USD | 38,660,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD |
| `1D` | `1.22` | 28,450,000.00 USD | 0.00 USD | 28,450,000.00 USD | 106,100.00 USD | 0.00 USD | 348,120.00 USD |
| `7D` | `1.22` | 38,490,000.00 USD | 0.00 USD | 38,490,000.00 USD | 51,610.00 USD | 166,160.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 27,990,000.00 USD | 0.00 USD | 27,990,000.00 USD | 270,600.00 USD | 510,520.00 USD | 2,640,000.00 USD |
| `7D` | `1.23` | 38,230,000.00 USD | 0.00 USD | 38,230,000.00 USD | 112,770.00 USD | 535,430.00 USD | 9,210.00 USD |
| `1D` | `1.23` | 24,570,000.00 USD | 0.00 USD | 24,570,000.00 USD | 107,280.00 USD | 64,900.00 USD | 86,210.00 USD |
| `7D` | `1.23` | 37,580,000.00 USD | 0.00 USD | 37,580,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD |
| `1D` | `1.23` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 556,720.00 USD | 1,090,000.00 USD | 2,440,000.00 USD |
| `7D` | `1.23` | 36,540,000.00 USD | 0.00 USD | 36,540,000.00 USD | 198,530.00 USD | 888,470.00 USD | 807,050.00 USD |
| `1D` | `1.23` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 66,520.00 USD | 1,250,000.00 USD | 2,270,000.00 USD |
| `7D` | `1.23` | 34,650,000.00 USD | 0.00 USD | 34,650,000.00 USD | 1,020,000.00 USD | 963,040.00 USD | 824,300.00 USD |
| `1D` | `1.23` | 16,630,000.00 USD | 0.00 USD | 16,630,000.00 USD | 1,380,000.00 USD | 443,480.00 USD | 2,210,000.00 USD |
| `7D` | `1.23` | 31,840,000.00 USD | 0.00 USD | 31,840,000.00 USD | 1,420,000.00 USD | 1,650,000.00 USD | 3,440,000.00 USD |
| `1D` | `1.24` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 122,830.00 USD | 1,130,000.00 USD | 1,280,000.00 USD |
| `7D` | `1.24` | 25,340,000.00 USD | 0.00 USD | 25,340,000.00 USD | 2,040,000.00 USD | 1,640,000.00 USD | 941,570.00 USD |
| `1D` | `1.24` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 18,660.00 USD | 280,340.00 USD | 61,110.00 USD |
| `7D` | `1.24` | 20,710,000.00 USD | 0.00 USD | 20,710,000.00 USD | 2,630,000.00 USD | 1,580,000.00 USD | 3,490,000.00 USD |
| `1D` | `1.24` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 15,170.00 USD | 220,870.00 USD | 931,900.00 USD |
| `7D` | `1.24` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 2,070,000.00 USD | 950,140.00 USD | 535,960.00 USD |
| `1D` | `1.24` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 734,030.00 USD | 182,970.00 USD | 651,390.00 USD |
| `7D` | `1.24` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.24` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 658,110.00 USD | 818,040.00 USD | 863,760.00 USD |
| `7D` | `1.24` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 1,420,000.00 USD | 15,000.00 USD | 0.00 USD |
| `1D` | `1.25` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,520,000.00 USD | 10,130.00 USD | 379,170.00 USD |
| `7D` | `1.25` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 3,370,000.00 USD | 0.00 USD | 1,440,000.00 USD |
| `1D` | `1.25` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 617,230.00 USD | 3,790.00 USD | 19,750.00 USD |
| `7D` | `1.25` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 331,570.00 USD | 306,030.00 USD | 210,580.00 USD |
| `7D` | `1.25` | 464,350.00 USD | 0.00 USD | 464,350.00 USD | 0.00 USD | 9,140.00 USD | 0.00 USD |
| `1D` | `1.25` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 202,510.00 USD | 1,390.00 USD | 993,050.00 USD |
| `7D` | `1.25` | 455,200.00 USD | 0.00 USD | 455,200.00 USD | 0.00 USD | 0.00 USD | 455,200.00 USD |
| `1D` | `1.25` | 30,590.00 USD | 0.00 USD | 30,590.00 USD | 17,600.00 USD | 8,750.00 USD | 4,230.00 USD |
| `1D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 949,920.00 USD | 949,920.00 USD | 0.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD |
| `7D` | `1.25` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD |
| `1D` | `1.25` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 633,250.00 USD | 12,640.00 USD | 681,030.00 USD |
| `7D` | `1.26` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 150,010.00 USD | 273,460.00 USD | 783,060.00 USD |
| `1D` | `1.26` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 1,090,000.00 USD | 443,180.00 USD | 551,970.00 USD |
| `7D` | `1.26` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 239,910.00 USD |
| `1D` | `1.26` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 295,510.00 USD | 561,050.00 USD | 1,020,000.00 USD |
| `7D` | `1.26` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 107,140.00 USD | 670,900.00 USD | 82,350.00 USD |
| `1D` | `1.26` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 532,070.00 USD | 86,770.00 USD | 2,060,000.00 USD |
| `7D` | `1.26` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 144,170.00 USD | 408,460.00 USD | 3,730,000.00 USD |
| `1D` | `1.26` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 1,250,000.00 USD | 819,120.00 USD | 1,770,000.00 USD |
| `7D` | `1.26` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 834,020.00 USD | 925,190.00 USD | 3,700,000.00 USD |
| `1D` | `1.26` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 479,740.00 USD | 980,510.00 USD | 2,160,000.00 USD |
| `7D` | `1.27` | 30,010,000.00 USD | 30,010,000.00 USD | 0.00 USD | 4,260,000.00 USD | 3,030,000.00 USD | 8,760,000.00 USD |
| `1D` | `1.27` | 19,740,000.00 USD | 19,740,000.00 USD | 0.00 USD | 745,260.00 USD | 1,270,000.00 USD | 2,300,000.00 USD |
| `7D` | `1.27` | 35,760,000.00 USD | 35,760,000.00 USD | 0.00 USD | 0.00 USD | 1,360,000.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 22,800,000.00 USD | 22,800,000.00 USD | 0.00 USD | 466,250.00 USD | 2,030,000.00 USD | 566,700.00 USD |
| `7D` | `1.27` | 38,790,000.00 USD | 38,790,000.00 USD | 0.00 USD | 138,500.00 USD | 2,540,000.00 USD | 350,390.00 USD |
| `1D` | `1.27` | 26,540,000.00 USD | 26,540,000.00 USD | 0.00 USD | 521,360.00 USD | 956,980.00 USD | 2,260,000.00 USD |
| `7D` | `1.27` | 45,280,000.00 USD | 45,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 4,610,000.00 USD | 598,230.00 USD |
| `1D` | `1.27` | 29,730,000.00 USD | 29,730,000.00 USD | 0.00 USD | 1,820,000.00 USD | 356,430.00 USD | 1,010,000.00 USD |
| `7D` | `1.27` | 57,590,000.00 USD | 57,590,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,540,000.00 USD | 7,060,000.00 USD |
| `1D` | `1.27` | 35,770,000.00 USD | 35,770,000.00 USD | 0.00 USD | 836,830.00 USD | 2,200,000.00 USD | 3,000,000.00 USD |
| `7D` | `1.28` | 71,230,000.00 USD | 71,230,000.00 USD | 0.00 USD | 4,660,000.00 USD | 2,810,000.00 USD | 6,170,000.00 USD |
| `1D` | `1.28` | 43,090,000.00 USD | 43,090,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,810,000.00 USD | 3,540,000.00 USD |
| `7D` | `1.28` | 88,340,000.00 USD | 88,340,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,210,000.00 USD | 6,120,000.00 USD |
| `1D` | `1.28` | 50,910,000.00 USD | 50,910,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,110,000.00 USD | 2,610,000.00 USD |
| `7D` | `1.28` | 89,860,000.00 USD | 89,860,000.00 USD | 0.00 USD | 0.00 USD | 1,440,000.00 USD | 84,070.00 USD |
| `1D` | `1.28` | 52,230,000.00 USD | 52,230,000.00 USD | 0.00 USD | 257,680.00 USD | 558,100.00 USD | 510,090.00 USD |
| `7D` | `1.28` | 91,000,000.00 USD | 91,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 30,200.00 USD | 85,990.00 USD |
| `1D` | `1.28` | 55,180,000.00 USD | 55,180,000.00 USD | 0.00 USD | 1,170,000.00 USD | 238,770.00 USD | 1,540,000.00 USD |
| `7D` | `1.28` | 93,750,000.00 USD | 93,750,000.00 USD | 0.00 USD | 854,670.00 USD | 956,050.00 USD | 929,630.00 USD |
| `1D` | `1.28` | 57,130,000.00 USD | 57,130,000.00 USD | 0.00 USD | 515,680.00 USD | 380,450.00 USD | 1,050,000.00 USD |
| `7D` | `1.29` | 96,350,000.00 USD | 96,350,000.00 USD | 0.00 USD | 796,960.00 USD | 1,120,000.00 USD | 680,350.00 USD |
| `1D` | `1.29` | 59,240,000.00 USD | 59,240,000.00 USD | 0.00 USD | 828,650.00 USD | 812,440.00 USD | 472,460.00 USD |
| `7D` | `1.29` | 96,820,000.00 USD | 96,820,000.00 USD | 0.00 USD | 440,460.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 59,630,000.00 USD | 59,630,000.00 USD | 0.00 USD | 210,950.00 USD | 24,800.00 USD | 148,370.00 USD |
| `7D` | `1.29` | 97,410,000.00 USD | 97,410,000.00 USD | 0.00 USD | 70,460.00 USD | 4,320.00 USD | 510,220.00 USD |
| `1D` | `1.29` | 60,120,000.00 USD | 60,120,000.00 USD | 0.00 USD | 177,490.00 USD | 42,820.00 USD | 268,660.00 USD |
| `7D` | `1.29` | 99,490,000.00 USD | 99,490,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 846,810.00 USD |
| `1D` | `1.29` | 63,120,000.00 USD | 63,120,000.00 USD | 0.00 USD | 570,020.00 USD | 197,630.00 USD | 2,240,000.00 USD |
| `7D` | `1.29` | 103,140,000.00 USD | 103,140,000.00 USD | 0.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD |
| `1D` | `1.29` | 69,290,000.00 USD | 69,290,000.00 USD | 0.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD |
| `7D` | `1.30` | 110,430,000.00 USD | 110,430,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD |
| `1D` | `1.30` | 71,860,000.00 USD | 71,860,000.00 USD | 0.00 USD | 554,720.00 USD | 703,990.00 USD | 1,310,000.00 USD |
| `7D` | `1.30` | 112,380,000.00 USD | 112,380,000.00 USD | 0.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 72,620,000.00 USD | 72,620,000.00 USD | 0.00 USD | 335,370.00 USD | 109,620.00 USD | 312,020.00 USD |
| `7D` | `1.30` | 114,380,000.00 USD | 114,380,000.00 USD | 0.00 USD | 208,510.00 USD | 298,720.00 USD | 1,490,000.00 USD |
| `1D` | `1.30` | 74,870,000.00 USD | 74,870,000.00 USD | 0.00 USD | 530,940.00 USD | 364,450.00 USD | 1,360,000.00 USD |
| `7D` | `1.30` | 115,410,000.00 USD | 115,410,000.00 USD | 0.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD |
| `1D` | `1.30` | 76,900,000.00 USD | 76,900,000.00 USD | 0.00 USD | 761,460.00 USD | 808,970.00 USD | 455,310.00 USD |
| `7D` | `1.30` | 117,930,000.00 USD | 117,930,000.00 USD | 0.00 USD | 0.00 USD | 2,040,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 78,170,000.00 USD | 78,170,000.00 USD | 0.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD |
| `7D` | `1.31` | 119,890,000.00 USD | 119,890,000.00 USD | 0.00 USD | 1,770,000.00 USD | 183,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 80,460,000.00 USD | 80,460,000.00 USD | 0.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD |
| `7D` | `1.31` | 124,540,000.00 USD | 124,540,000.00 USD | 0.00 USD | 1,430,000.00 USD | 821,310.00 USD | 2,400,000.00 USD |
| `1D` | `1.31` | 83,700,000.00 USD | 83,700,000.00 USD | 0.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD |
| `7D` | `1.31` | 126,560,000.00 USD | 126,560,000.00 USD | 0.00 USD | 1,340,000.00 USD | 242,640.00 USD | 433,950.00 USD |
| `1D` | `1.31` | 85,570,000.00 USD | 85,570,000.00 USD | 0.00 USD | 866,160.00 USD | 434,290.00 USD | 573,540.00 USD |
| `7D` | `1.31` | 130,540,000.00 USD | 130,540,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 2,930,000.00 USD |
| `1D` | `1.31` | 87,660,000.00 USD | 87,660,000.00 USD | 0.00 USD | 729,330.00 USD | 417,190.00 USD | 944,450.00 USD |
| `7D` | `1.31` | 131,710,000.00 USD | 131,710,000.00 USD | 0.00 USD | 515,950.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.31` | 90,420,000.00 USD | 90,420,000.00 USD | 0.00 USD | 342,500.00 USD | 387,380.00 USD | 2,020,000.00 USD |
| `7D` | `1.32` | 135,910,000.00 USD | 135,910,000.00 USD | 0.00 USD | 68,520.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 95,720,000.00 USD | 95,720,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,040,000.00 USD | 2,970,000.00 USD |
| `7D` | `1.32` | 140,760,000.00 USD | 140,760,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 100,600,000.00 USD | 100,600,000.00 USD | 0.00 USD | 1,680,000.00 USD | 733,340.00 USD | 2,460,000.00 USD |
| `7D` | `1.32` | 142,780,000.00 USD | 142,780,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 103,560,000.00 USD | 103,560,000.00 USD | 0.00 USD | 1,500,000.00 USD | 499,050.00 USD | 959,190.00 USD |
| `7D` | `1.32` | 146,140,000.00 USD | 146,140,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 106,730,000.00 USD | 106,730,000.00 USD | 0.00 USD | 1,010,000.00 USD | 481,660.00 USD | 1,680,000.00 USD |
| `7D` | `1.32` | 148,920,000.00 USD | 148,920,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.32` | 108,040,000.00 USD | 108,040,000.00 USD | 0.00 USD | 830,310.00 USD | 111,810.00 USD | 368,640.00 USD |
| `7D` | `1.33` | 150,720,000.00 USD | 150,720,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 109,650,000.00 USD | 109,650,000.00 USD | 0.00 USD | 503,480.00 USD | 452,830.00 USD | 647,120.00 USD |
| `7D` | `1.33` | 151,820,000.00 USD | 151,820,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 111,510,000.00 USD | 111,510,000.00 USD | 0.00 USD | 578,690.00 USD | 128,070.00 USD | 1,150,000.00 USD |
| `7D` | `1.33` | 153,530,000.00 USD | 153,530,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 113,680,000.00 USD | 113,680,000.00 USD | 0.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 156,000,000.00 USD | 156,000,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 115,630,000.00 USD | 115,630,000.00 USD | 0.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD |
| `7D` | `1.33` | 158,030,000.00 USD | 158,030,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.33` | 116,970,000.00 USD | 116,970,000.00 USD | 0.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD |
| `7D` | `1.34` | 159,570,000.00 USD | 159,570,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 117,710,000.00 USD | 117,710,000.00 USD | 0.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD |
| `7D` | `1.34` | 162,010,000.00 USD | 162,010,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 118,310,000.00 USD | 118,310,000.00 USD | 0.00 USD | 179,460.00 USD | 83,160.00 USD | 334,340.00 USD |
| `7D` | `1.34` | 163,880,000.00 USD | 163,880,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 119,820,000.00 USD | 119,820,000.00 USD | 0.00 USD | 701,920.00 USD | 312,600.00 USD | 499,950.00 USD |
| `7D` | `1.34` | 169,400,000.00 USD | 169,400,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,490,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 121,870,000.00 USD | 121,870,000.00 USD | 0.00 USD | 963,900.00 USD | 368,440.00 USD | 716,420.00 USD |
| `7D` | `1.34` | 176,810,000.00 USD | 176,810,000.00 USD | 0.00 USD | 2,000,000.00 USD | 2,170,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.34` | 123,440,000.00 USD | 123,440,000.00 USD | 0.00 USD | 556,930.00 USD | 328,690.00 USD | 683,630.00 USD |
| `7D` | `1.35` | 186,060,000.00 USD | 186,060,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,830,000.00 USD | 3,880,000.00 USD |
| `1D` | `1.35` | 124,030,000.00 USD | 124,030,000.00 USD | 0.00 USD | 206,540.00 USD | 183,280.00 USD | 204,210.00 USD |
| `7D` | `1.35` | 194,650,000.00 USD | 194,650,000.00 USD | 0.00 USD | 3,010,000.00 USD | 1,970,000.00 USD | 3,610,000.00 USD |
| `1D` | `1.35` | 124,710,000.00 USD | 124,710,000.00 USD | 0.00 USD | 312,230.00 USD | 33,600.00 USD | 333,430.00 USD |
| `7D` | `1.35` | 202,670,000.00 USD | 202,670,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 125,280,000.00 USD | 125,280,000.00 USD | 0.00 USD | 261,450.00 USD | 55,490.00 USD | 251,380.00 USD |
| `7D` | `1.35` | 211,790,000.00 USD | 211,790,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 125,690,000.00 USD | 125,690,000.00 USD | 0.00 USD | 111,940.00 USD | 144,570.00 USD | 154,930.00 USD |
| `7D` | `1.35` | 218,540,000.00 USD | 218,540,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.35` | 126,450,000.00 USD | 126,450,000.00 USD | 0.00 USD | 124,010.00 USD | 62,670.00 USD | 572,500.00 USD |
| `7D` | `1.36` | 224,880,000.00 USD | 224,880,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 127,410,000.00 USD | 127,410,000.00 USD | 0.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 227,430,000.00 USD | 227,430,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 127,740,000.00 USD | 127,740,000.00 USD | 0.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD |
| `7D` | `1.36` | 230,530,000.00 USD | 230,530,000.00 USD | 0.00 USD | 1,460,000.00 USD | 414,770.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 128,400,000.00 USD | 128,400,000.00 USD | 0.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD |
| `7D` | `1.36` | 234,320,000.00 USD | 234,320,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 128,700,000.00 USD | 128,700,000.00 USD | 0.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD |
| `7D` | `1.36` | 237,080,000.00 USD | 237,080,000.00 USD | 0.00 USD | 1,430,000.00 USD | 616,140.00 USD | 713,350.00 USD |
| `1D` | `1.36` | 128,820,000.00 USD | 128,820,000.00 USD | 0.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD |
| `7D` | `1.37` | 237,890,000.00 USD | 237,890,000.00 USD | 0.00 USD | 206,650.00 USD | 190,380.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 129,070,000.00 USD | 129,070,000.00 USD | 0.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD |
| `7D` | `1.37` | 239,000,000.00 USD | 239,000,000.00 USD | 0.00 USD | 535,200.00 USD | 181,820.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 129,220,000.00 USD | 129,220,000.00 USD | 0.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD |
| `7D` | `1.37` | 240,490,000.00 USD | 240,490,000.00 USD | 0.00 USD | 415,220.00 USD | 339,760.00 USD | 733,820.00 USD |
| `1D` | `1.37` | 129,320,000.00 USD | 129,320,000.00 USD | 0.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD |
| `7D` | `1.37` | 242,150,000.00 USD | 242,150,000.00 USD | 0.00 USD | 553,200.00 USD | 287,880.00 USD | 820,700.00 USD |
| `1D` | `1.37` | 129,410,000.00 USD | 129,410,000.00 USD | 0.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD |
| `7D` | `1.37` | 244,070,000.00 USD | 244,070,000.00 USD | 0.00 USD | 619,020.00 USD | 407,640.00 USD | 893,850.00 USD |
| `1D` | `1.38` | 129,580,000.00 USD | 129,580,000.00 USD | 0.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD |
| `7D` | `1.38` | 245,320,000.00 USD | 245,320,000.00 USD | 0.00 USD | 360,280.00 USD | 298,220.00 USD | 586,390.00 USD |
| `1D` | `1.38` | 129,700,000.00 USD | 129,700,000.00 USD | 0.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD |
| `7D` | `1.38` | 246,780,000.00 USD | 246,780,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD |
| `1D` | `1.38` | 129,970,000.00 USD | 129,970,000.00 USD | 0.00 USD | 69,610.00 USD | 60,790.00 USD | 140,470.00 USD |
| `7D` | `1.38` | 248,420,000.00 USD | 248,420,000.00 USD | 0.00 USD | 436,360.00 USD | 142,590.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 130,040,000.00 USD | 130,040,000.00 USD | 0.00 USD | 0.00 USD | 65,520.00 USD | 0.00 USD |
| `7D` | `1.38` | 250,280,000.00 USD | 250,280,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD |
| `1D` | `1.38` | 130,210,000.00 USD | 130,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 166,310.00 USD |
| `7D` | `1.38` | 251,070,000.00 USD | 251,070,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 129,320.00 USD |
| `1D` | `1.39` | 130,250,000.00 USD | 130,250,000.00 USD | 0.00 USD | 46,440.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 252,090,000.00 USD | 252,090,000.00 USD | 0.00 USD | 377,810.00 USD | 231,880.00 USD | 413,510.00 USD |
| `7D` | `1.39` | 253,010,000.00 USD | 253,010,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 218,620.00 USD |
| `7D` | `1.39` | 253,760,000.00 USD | 253,760,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `7D` | `1.39` | 254,080,000.00 USD | 254,080,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.39` | 254,140,000.00 USD | 254,140,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 254,370,000.00 USD | 254,370,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 254,370,000.00 USD | 254,370,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 254,440,000.00 USD | 254,440,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 254,510,000.00 USD | 254,510,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 254,810,000.00 USD | 254,810,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 254,960,000.00 USD | 254,960,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 255,130,000.00 USD | 255,130,000.00 USD | 0.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `7D` | `1.41` | 256,010,000.00 USD | 256,010,000.00 USD | 0.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `7D` | `1.41` | 256,240,000.00 USD | 256,240,000.00 USD | 0.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `7D` | `1.41` | 256,540,000.00 USD | 256,540,000.00 USD | 0.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD |
| `7D` | `1.42` | 257,100,000.00 USD | 257,100,000.00 USD | 0.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD |
| `7D` | `1.42` | 257,840,000.00 USD | 257,840,000.00 USD | 0.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `7D` | `1.42` | 258,890,000.00 USD | 258,890,000.00 USD | 0.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `7D` | `1.42` | 260,220,000.00 USD | 260,220,000.00 USD | 0.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `7D` | `1.42` | 260,420,000.00 USD | 260,420,000.00 USD | 0.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD |
| `7D` | `1.43` | 260,730,000.00 USD | 260,730,000.00 USD | 0.00 USD | 67,230.00 USD | 65,630.00 USD | 183,690.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.83B` | Total OI Tokens: `2,250,677,152.3 XRP`
  * 1h OI Change: `+0.83%` | 4h OI Change: `+2.56%` | 24h OI Change: `-3.42%`
  * Exchange Breakdown: Binance=`436.70M` | Bybit=`317.50M` | OKX=`94.24M` | Hyperliquid=`199.37M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-79.71K` | Last 24h: `81.98K` | Last 3d: `547.43K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0047%` | **USDT OKX** | `-0.0125%` |
| **USDT Bybit** | `-0.0337%` | **USDT KuCoin** | `-0.0035%` |
| **USDT MEXC** | `0.0046%` | **USDT BingX** | `0.0044%` |
| **USDT Gate** | `-0.0013%` | **USDT Bitget** | `-0.0040%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `53.96%` | `46.04%` | `1.17` | 1,280,000,000.00 USD |
| `15M` | `Binance` | `52.62%` | `47.38%` | `1.11` | 122,730,000.00 USD |
| `15M` | `OKX` | `43.87%` | `56.13%` | `0.78` | 79,420,000.00 USD |
| `15M` | `Bybit` | `54.37%` | `45.63%` | `1.19` | 40,390,000.00 USD |
| `15M` | `KuCoin` | `63.07%` | `36.93%` | `1.71` | 904,700.00 USD |
| `15M` | `Gate` | `45.47%` | `54.53%` | `0.83` | 53,240,000.00 USD |
| `15M` | `Bitget` | `49.09%` | `50.91%` | `0.96` | 18,520,000.00 USD |
| `15M` | `BingX` | `45.13%` | `54.87%` | `0.82` | 2,660,000.00 USD |
| `15M` | `MEXC` | `34.63%` | `65.37%` | `0.53` | 10,520,000.00 USD |
| `15M` | `Bitunix` | `54.14%` | `45.86%` | `1.18` | 13,800,000.00 USD |
| `15M` | `Hyperliquid` | `40.68%` | `59.32%` | `0.69` | 11,800,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `91.39%` | `8.61%` | `10.61` | 2,040,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `55.97%` | `44.03%` | `1.27` | 905,220,000.00 USD |
| `15M` | `HTX` | `69.15%` | `30.85%` | `2.24` | 8,300,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `42.93%` | `57.07%` | `0.75` | 2,500,000.00 USD |
| `15M` | `Bitfinex` | `13.29%` | `86.71%` | `0.15` | 219,680.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `30.66%` | `69.34%` | `0.44` | 4,230,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.21%` | `54.79%` | `0.83` | 3,030,000.00 USD |
| `15M` | `Whale Positions` | `52.62%` | `47.38%` | `1.11` | 122,730,000.00 USD |
| `15M` | `Global Accounts` | `53.96%` | `46.04%` | `1.17` | 1,280,000,000.00 USD |
| `1H` | `XRP` | `53.75%` | `46.25%` | `1.16` | 2,430,000,000.00 USD |
| `1H` | `Binance` | `52.5%` | `47.5%` | `1.11` | 557,340,000.00 USD |
| `1H` | `OKX` | `49.1%` | `50.9%` | `0.96` | 344,490,000.00 USD |
| `1H` | `Bybit` | `57.5%` | `42.5%` | `1.35` | 117,260,000.00 USD |
| `1H` | `KuCoin` | `34.34%` | `65.66%` | `0.52` | 5,950,000.00 USD |
| `1H` | `Gate` | `49.8%` | `50.2%` | `0.99` | 234,680,000.00 USD |
| `1H` | `Bitget` | `50.78%` | `49.22%` | `1.03` | 74,340,000.00 USD |
| `1H` | `BingX` | `61.92%` | `38.08%` | `1.63` | 19,020,000.00 USD |
| `1H` | `MEXC` | `50.18%` | `49.82%` | `1.01` | 45,220,000.00 USD |
| `1H` | `Bitunix` | `52.87%` | `47.13%` | `1.12` | 66,620,000.00 USD |
| `1H` | `Hyperliquid` | `56.55%` | `43.45%` | `1.30` | 36,460,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.6%` | `47.4%` | `1.11` | 7,420,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `56.65%` | `43.35%` | `1.31` | 837,400,000.00 USD |
| `1H` | `HTX` | `79.99%` | `20.01%` | `4.00` | 38,720,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `45.61%` | `54.39%` | `0.84` | 7,770,000.00 USD |
| `1H` | `Bitfinex` | `18.77%` | `81.23%` | `0.23` | 1,140,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `40.5%` | `59.5%` | `0.68` | 12,920,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.27%` | `49.73%` | `1.01` | 24,070,000.00 USD |
| `1H` | `Whale Positions` | `52.5%` | `47.5%` | `1.11` | 557,340,000.00 USD |
| `1H` | `Global Accounts` | `53.75%` | `46.25%` | `1.16` | 2,430,000,000.00 USD |
| `4H` | `XRP` | `48.45%` | `51.55%` | `0.94` | 12,160,000,000.00 USD |
| `4H` | `Binance` | `49.27%` | `50.73%` | `0.97` | 3,630,000,000.00 USD |
| `4H` | `OKX` | `48.24%` | `51.76%` | `0.93` | 2,170,000,000.00 USD |
| `4H` | `Bybit` | `50.47%` | `49.53%` | `1.02` | 767,330,000.00 USD |
| `4H` | `KuCoin` | `58.42%` | `41.58%` | `1.41` | 118,020,000.00 USD |
| `4H` | `Gate` | `49.3%` | `50.7%` | `0.97` | 1,520,000,000.00 USD |
| `4H` | `Bitget` | `52.7%` | `47.3%` | `1.11` | 491,820,000.00 USD |
| `4H` | `BingX` | `53.04%` | `46.96%` | `1.13` | 97,690,000.00 USD |
| `4H` | `MEXC` | `48.81%` | `51.19%` | `0.95` | 334,440,000.00 USD |
| `4H` | `Bitunix` | `49.9%` | `50.1%` | `1.00` | 403,350,000.00 USD |
| `4H` | `Hyperliquid` | `55.71%` | `44.29%` | `1.26` | 404,390,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.45%` | `45.55%` | `1.20` | 48,020,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `38.27%` | `61.73%` | `0.62` | 1,630,000,000.00 USD |
| `4H` | `HTX` | `70.96%` | `29.04%` | `2.44` | 191,630,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `48.67%` | `51.33%` | `0.95` | 61,520,000.00 USD |
| `4H` | `Bitfinex` | `27.19%` | `72.81%` | `0.37` | 9,890,000.00 USD |
| `4H` | `Kraken` | `37.77%` | `62.23%` | `0.61` | 18,110,000.00 USD |
| `4H` | `Aster` | `49.72%` | `50.28%` | `0.99` | 105,630,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.2%` | `54.8%` | `0.82` | 145,740,000.00 USD |
| `4H` | `Whale Positions` | `49.27%` | `50.73%` | `0.97` | 3,630,000,000.00 USD |
| `4H` | `Global Accounts` | `48.45%` | `51.55%` | `0.94` | 12,160,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.22` | `1.22` | `1.22` | `1.22` | `1.22` | 9,740,915.81 USD | 4,726,774.90 USD | 5,014,140.91 USD | -287,366.00 USD | `-2.95%` | `9B / 19S` |
| `0:00 UTC` | `1.23` | `1.23` | `1.23` | `1.23` | `1.22` | 10,276,393.47 USD | 5,352,457.47 USD | 4,923,936.00 USD | 428,521.46 USD | `+4.17%` | `12B / 9S` |
| `5:00 UTC` | `1.23` | `1.23` | `1.23` | `1.23` | `1.22` | 7,441,662.05 USD | 4,516,863.46 USD | 2,924,798.59 USD | 1,592,064.87 USD | `+21.39%` | `27B / 7S` |
| `0:00 UTC` | `1.24` | `1.24` | `1.24` | `1.24` | `1.23` | 14,534,365.59 USD | 7,960,789.37 USD | 6,573,576.22 USD | 1,387,213.15 USD | `+9.54%` | `20B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.24` | 13,408,965.14 USD | 7,227,260.97 USD | 6,181,704.17 USD | 1,045,556.80 USD | `+7.80%` | `8B / 3S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.25` | `1.24` | 11,613,568.18 USD | 6,301,411.52 USD | 5,312,156.67 USD | 989,254.85 USD | `+8.52%` | `26B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 11,339,015.88 USD | 5,463,329.20 USD | 5,875,686.68 USD | -412,357.48 USD | `-3.64%` | `7B / 6S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 9,975,142.90 USD | 5,917,919.57 USD | 4,057,223.33 USD | 1,860,696.23 USD | `+18.65%` | `9B / 2S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 6,812,599.45 USD | 3,905,481.96 USD | 2,907,117.49 USD | 998,364.47 USD | `+14.65%` | `4B / 3S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 666,499.73 USD | 385,544.72 USD | 280,955.00 USD | 104,589.72 USD | `+15.69%` | `5B / 2S` |

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
| `5m` | 965,120.00 USD | 2,070,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,710,000.00 USD | 2,550,000.00 USD | **`ACCUMULATION`** |
| `30m` | 2,020,000.00 USD | 5,500,000.00 USD | **`ACCUMULATION`** |
| `1h` | 4,320,000.00 USD | 13,950,000.00 USD | **`ACCUMULATION`** |
| `2h` | 13,130,000.00 USD | 28,320,000.00 USD | **`ACCUMULATION`** |
| `4h` | 14,270,000.00 USD | 15,890,000.00 USD | **`ACCUMULATION`** |
| `6h` | -8,930,000.00 USD | -2,640,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -15,020,000.00 USD | -104,480,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -55,310,000.00 USD | -125,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -55,300,000.00 USD | -134,200,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -124,000,000.00 USD | -217,550,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -599,160,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+965.12K` | 15m=`+1.71M` | 1h=`+4.32M` | 24h=`-55.30M`
* Futures Capital Netflows: 5m=`+2.07M` | 15m=`+2.55M` | 1h=`+13.95M` | 24h=`-134.20M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.22` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.20` (Risk Distance: `0.0180` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `0.0180` pts)
  * +2.5R Take Profit: `1.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
