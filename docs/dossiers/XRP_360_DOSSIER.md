# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:09:00 IST` (`2026-10-30 09:39:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.26` | **Mid Price**: `1.25`
- **Spread Points**: `3.00` | **Spread BPS**: `23.91 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.24` | VWAP Z-Score: `+0.90` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0080` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `56.47` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.30` | Lower -3.00σ Band: `1.18`
  * Upper +2.51σ Band: `1.29` | Lower -2.51σ Band: `1.19`
  * Upper +2.01σ Band: `1.28` | Lower -2.01σ Band: `1.20`
  * Upper +2.00σ Band: `1.28` | Lower -2.00σ Band: `1.20`
  * Upper +1.28σ Band: `1.26` | Lower -1.28σ Band: `1.21`
  * Upper +1.00σ Band: `1.26` | Lower -1.00σ Band: `1.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.26`
  * Institutional Anchors: EMA-144=`1.27` | EMA-200=`1.28` (Slope: `-0.2551`) | EMA-233=`1.28`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.49%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.36%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+1.85%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.27` | Low=`1.24`
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
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `2,138,316` | 2,689,605.35 USD | -513,179.47 USD | `-19.08%` | -39,860,642.83 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,318,241` | 1,656,569.61 USD | 40,710.44 USD | `+2.46%` | -39,819,932.39 USD | `+0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `270,177` | 339,683.62 USD | -113,762.94 USD | `-33.49%` | -39,933,695.33 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `10,169,439` | 12,807,415.42 USD | 578,544.93 USD | `+4.52%` | -39,093,274.83 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `6,049,226` | 7,616,675.33 USD | -933,268.81 USD | `-12.25%` | -40,026,543.64 USD | `-0.91` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `270,177` | 339,683.62 USD | -113,762.94 USD | `-33.49%` | -40,140,306.58 USD | `-0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.27` | `1.27` | `1.25` | `1.25` | `31,555,138` | 39,629,532.33 USD | -5,613,699.06 USD | `-14.17%` | -41,162,507.62 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `20,218,037` | 25,337,061.54 USD | 668,152.80 USD | `+2.64%` | -40,494,354.82 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.26` | `1.26` | `1.26` | `1.26` | `16,509,364` | 20,789,563.20 USD | -442,697.99 USD | `-2.13%` | -40,937,052.81 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.25` | `1.26` | `36,727,401` | 46,126,624.74 USD | 225,454.81 USD | `+0.49%` | -39,056,074.12 USD | `+0.58` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -13,549,801.29 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -41,639,935.50 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.25` | `1.26` | `36,727,401` | 46,126,624.74 USD | 225,454.81 USD | `+0.49%` | -39,056,074.12 USD | `+0.58` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `BID` | `1.25` | `65194.0000` | 81,818.47 USD | 1,142,472.91 USD | `7 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `132075.0000` | 165,740.92 USD | 1,308,213.82 USD | `8 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `24172.0000` | 30,331.03 USD | 1,338,544.85 USD | `4 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `12966.0000` | 16,268.44 USD | 1,354,813.29 USD | `5 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `56392.0000` | 70,749.40 USD | 1,425,562.69 USD | `7 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `19535.0000` | 24,506.66 USD | 1,450,069.35 USD | `4 orders` | `-0.16%` | `-` |
| `ASK` | `1.26` | `9040.0000` | 11,376.84 USD | 2,557,709.79 USD | `6 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `257358.0000` | 323,859.31 USD | 2,546,332.95 USD | `9 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `36852.0000` | 46,370.87 USD | 2,222,473.65 USD | `5 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `216036.0000` | 271,816.50 USD | 2,176,102.77 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `35230.0000` | 44,322.86 USD | 1,904,286.28 USD | `6 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `447051.0000` | 562,390.16 USD | 1,859,963.42 USD | `9 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `48413.0000` | 60,898.71 USD | 1,297,573.26 USD | `7 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `59408.0000` | 74,723.38 USD | 1,236,674.54 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `97721.0000` | 122,903.70 USD | 1,161,951.16 USD | `9 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `38339.0000` | 48,215.13 USD | 1,039,047.46 USD | `8 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `67398.0000` | 84,752.99 USD | 990,832.33 USD | `12 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `53487.0000` | 67,254.55 USD | 906,079.35 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `320407.0000` | 402,847.72 USD | 838,824.80 USD | `12 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `40219.0000` | 50,563.33 USD | 435,977.07 USD | `9 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `71053.0000` | 89,320.73 USD | 385,413.75 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `50263.0000` | 63,180.59 USD | 296,093.02 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `74198.0000` | 93,259.47 USD | 232,912.43 USD | `11 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `23237.0000` | 29,204.26 USD | 139,652.96 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `73849.0000` | 92,806.04 USD | 110,448.70 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `14040.0000` | 17,642.66 USD | 17,642.66 USD | `7 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `2695.0000` | 3,386.00 USD | 3,386.00 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `8019.0000` | 10,074.27 USD | 13,460.27 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `28886.0000` | 36,286.59 USD | 49,746.86 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `14215.0000` | 17,855.46 USD | 67,602.32 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `11470.0000` | 14,406.32 USD | 82,008.64 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `20498.0000` | 25,743.44 USD | 107,752.08 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `71264.0000` | 89,493.33 USD | 197,245.41 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `68094.0000` | 85,505.64 USD | 282,751.05 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `120466.0000` | 151,257.11 USD | 434,008.16 USD | `15 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `44206.0000` | 55,500.63 USD | 489,508.79 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `37645.0000` | 47,259.53 USD | 536,768.32 USD | `6 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `245730.0000` | 308,464.87 USD | 845,233.19 USD | `6 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `121960.0000` | 153,084.19 USD | 998,317.38 USD | `11 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `49667.0000` | 62,337.05 USD | 1,060,654.44 USD | `6 orders` | `-0.11%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:01:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 44,027,501.22 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,448,617.96 USD | `+10.10%` | `10X Cross` |
| `91` | `0x5b5d...c060` | `SHORT` | 19,597,455.89 USD | `15,586,937.00` | `1.44` | `1.26` | `11.02` | 2,776,993.07 USD | `+14.17%` | `5X Cross` |
| `158` | `0xb83d...6e36` | `SHORT` | 12,841,910.07 USD | `10,213,879.00` | `1.50` | `1.26` | `12.83` | 2,468,646.26 USD | `+19.22%` | `5X Cross` |
| `338` | `0x58f0...0d20` | `LONG` | 6,671,614.49 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 68,770.99 USD | `+1.03%` | `20X Cross` |
| `372` | `0xecb6...2b00` | `SHORT` | 6,210,623.01 USD | `4,939,258.00` | `1.27` | `1.26` | `7.64` | 57,588.23 USD | `+0.93%` | `10X Cross` |
| `421` | `0xca49...53c8` | `SHORT` | 5,196,371.37 USD | `4,138,886.00` | `1.44` | `1.26` | `4.97` | 756,951.36 USD | `+14.57%` | `20X Cross` |
| `432` | `0xdd53...2b13` | `SHORT` | 5,025,435.22 USD | `3,998,914.00` | `1.40` | `1.26` | `16.97` | 571,440.89 USD | `+11.37%` | `3X Cross` |
| `497` | `0x610b...b613` | `LONG` | 4,455,094.52 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8493` | -644,898.09 USD | `-14.48%` | `5X Cross` |
| `592` | `0x9946...0852` | `SHORT` | 3,859,290.08 USD | `3,070,483.00` | `1.40` | `1.26` | `1.78` | 449,212.14 USD | `+11.64%` | `20X Cross` |
| `644` | `0xc30c...a4c9` | `SHORT` | 3,508,376.05 USD | `2,791,515.00` | `1.41` | `1.26` | `1.59` | 428,136.68 USD | `+12.20%` | `8X Cross` |
| `654` | `0xc179...e0c8` | `SHORT` | 3,481,470.26 USD | `2,768,785.00` | `1.27` | `1.26` | `3.37` | 26,946.63 USD | `+0.77%` | `10X Cross` |
| `658` | `0xfc27...9d9d` | `SHORT` | 3,439,529.80 USD | `2,736,736.00` | `1.29` | `1.26` | `8.22` | 99,989.21 USD | `+2.91%` | `20X Cross` |
| `695` | `0xf48f...10fe` | `LONG` | 3,224,927.63 USD | `2,565,779.00` | `1.53` | `1.26` | `1.03` | -699,713.10 USD | `-21.70%` | `4X Cross` |
| `738` | `0x023a...2355` | `SHORT` | 3,095,458.18 USD | `2,463,360.00` | `1.32` | `1.26` | `3.37` | 155,470.07 USD | `+5.02%` | `20X Cross` |
| `741` | `0x45d2...4029` | `SHORT` | 3,082,930.40 USD | `2,453,000.00` | `1.48` | `1.26` | `19.04` | 555,350.02 USD | `+18.01%` | `20X Cross` |
| `1066` | `0xeadc...9d55` | `LONG` | 2,035,770.92 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 76,927.90 USD | `+3.78%` | `20X Cross` |
| `1142` | `0x94b2...599e` | `SHORT` | 1,936,808.94 USD | `1,540,696.00` | `1.36` | `1.26` | `1.88` | 163,657.51 USD | `+8.45%` | `20X Cross` |
| `1167` | `0x3fc5...c0c1` | `SHORT` | 1,900,155.03 USD | `1,511,779.00` | `1.52` | `1.26` | `2.46` | 391,459.58 USD | `+20.60%` | `20X Cross` |
| `1190` | `0x31ef...f715` | `LONG` | 1,853,880.54 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -345,384.86 USD | `-18.63%` | `3X Isolated` |
| `1252` | `0x7737...bf66` | `SHORT` | 1,776,444.07 USD | `1,413,466.00` | `1.41` | `1.26` | `13.95` | 222,424.58 USD | `+12.52%` | `10X Cross` |
| `1303` | `0x95da...2328` | `LONG` | 1,665,104.16 USD | `1,324,876.00` | `1.35` | `1.26` | `0.1070` | -128,536.94 USD | `-7.72%` | `5X Cross` |
| `1318` | `0xee2b...d67e` | `LONG` | 1,641,868.36 USD | `1,306,284.00` | `1.55` | `1.26` | `0.4508` | -388,786.54 USD | `-23.68%` | `4X Cross` |
| `1363` | `0x215d...f80a` | `LONG` | 1,573,233.33 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -81,220.89 USD | `-5.16%` | `14X Cross` |
| `1377` | `0x5fa3...35b7` | `SHORT` | 1,559,994.57 USD | `1,240,651.00` | `1.30` | `1.26` | `2.69` | 56,497.57 USD | `+3.62%` | `20X Cross` |
| `1427` | `0x123d...3bff` | `LONG` | 1,523,102.10 USD | `1,211,889.00` | `1.35` | `1.26` | `0.000000` | -109,333.39 USD | `-7.18%` | `10X Cross` |
| `1448` | `0xbcd4...0dd2` | `SHORT` | 1,504,007.57 USD | `1,196,125.00` | `1.31` | `1.26` | `2.05` | 63,659.67 USD | `+4.23%` | `20X Cross` |
| `1542` | `0x7fda...17d1` | `LONG` | 1,393,472.06 USD | `1,108,217.00` | `1.22` | `1.26` | `0.000000` | 43,233.22 USD | `+3.10%` | `20X Cross` |
| `1552` | `0xdf95...7d72` | `SHORT` | 1,382,795.47 USD | `1,099,726.00` | `1.37` | `1.26` | `37.19` | 126,803.33 USD | `+9.17%` | `20X Cross` |
| `1627` | `0xef96...9383` | `SHORT` | 1,303,006.25 USD | `1,036,765.00` | `1.34` | `1.26` | `4.67` | 84,513.09 USD | `+6.49%` | `20X Cross` |
| `1647` | `0xb1ce...681b` | `LONG` | 1,284,153.00 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -239,903.50 USD | `-18.68%` | `4X Isolated` |
| `1759` | `0x3c36...461a` | `LONG` | 1,180,516.05 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -38,564.57 USD | `-3.27%` | `10X Cross` |
| `1790` | `0x2577...4897` | `SHORT` | 1,160,083.05 USD | `922,678.00` | `1.24` | `1.26` | `4.77` | -11,966.20 USD | `-1.03%` | `20X Cross` |
| `1994` | `0xbfc7...80b4` | `SHORT` | 1,006,000.00 USD | `800,000.00` | `1.48` | `1.26` | `3.29` | 177,454.65 USD | `+17.64%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `1.30` | 9,733.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.73K USD at 1.2978 USD [API] | `2026-10-29 17:21:47` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.12%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.55%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+5.33%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.57%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+7.50%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.57%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 2,900,000.00 USD, Dist: `+7.38%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.57%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 1,360.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 1,720.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 3,220.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 378.20 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 28,780.00 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 235.16 USD | 64,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 5,320.00 USD | 64,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 4,710.00 USD | 64,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 1,930.00 USD | 64,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 16,980.00 USD | 64,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,180.00 USD | 64,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 49,350.00 USD | 64,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 3,160.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 2,170.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 614.38 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 1,170.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 29,680.00 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 577,120.00 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 883.77 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 160,020.00 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 397.11 USD | 63,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 2,000.00 USD | 63,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 323.98 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 6,470.00 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 188.87 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 9,050.00 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 2,810.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 3,530.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 27,050.00 USD | 63,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 160,990.00 USD | 63,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 2,070.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,760.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 4,900.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 198.13 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 23,080.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 39,120.00 USD | 63,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,130.00 USD | 63,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 10,510.00 USD | 63,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 21,730.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 2,630.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 17,790.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 26,110.00 USD | 63,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 2,980.00 USD | 63,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 160,780.00 USD | 63,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 23,200.00 USD | 63,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 68,280.00 USD | 63,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 235,740.00 USD | 63,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 45,360.00 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 81,440.00 USD | 62,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 147,720.00 USD | 62,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 62,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 5,930.00 USD | 62,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 16,460.00 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 44,850.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 511,010.00 USD | 62,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 61,010.00 USD | 62,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 23,130.00 USD | 61,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 32,170.00 USD | 61,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 3,050,000.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 61,290.00 USD | 58,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 38,050.00 USD | 58,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 93,870.00 USD | 58,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 358,270.00 USD | 58,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 97,380.00 USD | 58,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 231,270.00 USD | 58,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 87,390.00 USD | 57,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 76,320.00 USD | 57,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 97,440.00 USD | 57,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 56,350.00 USD | 57,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 153,860.00 USD | 57,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,890,000.00 USD | 57,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 155,450.00 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 455,050.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 113,040.00 USD | 23,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 506,580.00 USD | 22,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 304,640.00 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 2,710,000.00 USD | 22,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,130,000.00 USD | 19,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 178,070.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,640,000.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 388,560.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 103,680,000.00 USD | 103,680,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 1,340,000.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 178,030.00 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 103,680,000.00 USD | 103,680,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 103,640,000.00 USD | 103,640,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 103,540,000.00 USD | 103,540,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 377,320.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 103,500,000.00 USD | 103,500,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 103,500,000.00 USD | 103,500,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 103,210,000.00 USD | 103,210,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 101,470.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 103,210,000.00 USD | 103,210,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 103,200,000.00 USD | 103,200,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 103,200,000.00 USD | 103,200,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 278,180.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 103,150,000.00 USD | 103,150,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 103,130,000.00 USD | 103,130,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 103,060,000.00 USD | 103,060,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 93,970,000.00 USD | 93,970,000.00 USD | 21,900.00 USD | 45,520.00 USD | 161,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 103,030,000.00 USD | 103,030,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,410,000.00 USD | 12,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 93,740,000.00 USD | 93,740,000.00 USD | 126,800.00 USD | 70,270.00 USD | 204,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 102,820,000.00 USD | 102,820,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 93,340,000.00 USD | 93,340,000.00 USD | 74,360.00 USD | 54,840.00 USD | 167,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 102,680,000.00 USD | 102,680,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 93,040,000.00 USD | 93,040,000.00 USD | 7,580.00 USD | 114,120.00 USD | 275,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 102,480,000.00 USD | 102,480,000.00 USD | 5,450.00 USD | 55,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 92,640,000.00 USD | 92,640,000.00 USD | 5,520.00 USD | 70,330.00 USD | 275,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 102,420,000.00 USD | 102,420,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 92,290,000.00 USD | 92,290,000.00 USD | 91,470.00 USD | 89,100.00 USD | 115,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 102,050,000.00 USD | 102,050,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 185,410.00 USD | 10,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 92,000,000.00 USD | 92,000,000.00 USD | 42,870.00 USD | 153,630.00 USD | 163,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 101,560,000.00 USD | 101,560,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 91,640,000.00 USD | 91,640,000.00 USD | 38,180.00 USD | 18,650.00 USD | 49,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 101,030,000.00 USD | 101,030,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 91,530,000.00 USD | 91,530,000.00 USD | 34,800.00 USD | 43,480.00 USD | 258,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 101,000,000.00 USD | 101,000,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 91,190,000.00 USD | 91,190,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 100,650,000.00 USD | 100,650,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 91,120,000.00 USD | 91,120,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 100,510,000.00 USD | 100,510,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 284,790.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 100,500,000.00 USD | 100,500,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 90,990,000.00 USD | 90,990,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 100,440,000.00 USD | 100,440,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 100,070,000.00 USD | 100,070,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 90,970,000.00 USD | 90,970,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 99,920,000.00 USD | 99,920,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 90,910,000.00 USD | 90,910,000.00 USD | 73,200.00 USD | 45,600.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 99,750,000.00 USD | 99,750,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 361,410.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 90,520,000.00 USD | 90,520,000.00 USD | 20,480.00 USD | 25,050.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 98,870,000.00 USD | 98,870,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 90,400,000.00 USD | 90,400,000.00 USD | 122,170.00 USD | 20,880.00 USD | 380,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 98,640,000.00 USD | 98,640,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 89,870,000.00 USD | 89,870,000.00 USD | 185,400.00 USD | 56,140.00 USD | 142,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 97,770,000.00 USD | 97,770,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 89,490,000.00 USD | 89,490,000.00 USD | 172,080.00 USD | 254,990.00 USD | 113,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 96,690,000.00 USD | 96,690,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 88,950,000.00 USD | 88,950,000.00 USD | 95,580.00 USD | 61,900.00 USD | 642,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 95,390,000.00 USD | 95,390,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,280,000.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 88,150,000.00 USD | 88,150,000.00 USD | 62,000.00 USD | 12,130.00 USD | 106,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 93,720,000.00 USD | 93,720,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 87,970,000.00 USD | 87,970,000.00 USD | 104,050.00 USD | 166,040.00 USD | 170,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 92,380,000.00 USD | 92,380,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 87,530,000.00 USD | 87,530,000.00 USD | 152,210.00 USD | 22,380.00 USD | 358,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 91,310,000.00 USD | 91,310,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 86,990,000.00 USD | 86,990,000.00 USD | 371,850.00 USD | 5,850.00 USD | 266,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 89,270,000.00 USD | 89,270,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 86,350,000.00 USD | 86,350,000.00 USD | 124,360.00 USD | 130,370.00 USD | 474,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 88,070,000.00 USD | 88,070,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 276,740.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 85,620,000.00 USD | 85,620,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 86,500,000.00 USD | 86,500,000.00 USD | 181,850.00 USD | 71,240.00 USD | 372,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 84,870,000.00 USD | 84,870,000.00 USD | 71,040.00 USD | 84,480.00 USD | 175,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 85,880,000.00 USD | 85,880,000.00 USD | 85,020.00 USD | 27,270.00 USD | 483,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 84,540,000.00 USD | 84,540,000.00 USD | 113,290.00 USD | 10,150.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 85,280,000.00 USD | 85,280,000.00 USD | 267,580.00 USD | 112,520.00 USD | 194,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 84,390,000.00 USD | 84,390,000.00 USD | 222,930.00 USD | 10,160.00 USD | 666,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 84,710,000.00 USD | 84,710,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 83,500,000.00 USD | 83,500,000.00 USD | 196,910.00 USD | 73,630.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 84,440,000.00 USD | 84,440,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 568,820.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 83,080,000.00 USD | 83,080,000.00 USD | 86,540.00 USD | 511,780.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 83,340,000.00 USD | 83,340,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 82,420,000.00 USD | 82,420,000.00 USD | 365,260.00 USD | 93,260.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 82,480,000.00 USD | 82,480,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 80,390,000.00 USD | 80,390,000.00 USD | 110,600.00 USD | 45,410.00 USD | 319,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 81,700,000.00 USD | 81,700,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,920,000.00 USD | 79,920,000.00 USD | 147,820.00 USD | 199,810.00 USD | 469,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 80,720,000.00 USD | 80,720,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,100,000.00 USD | 79,100,000.00 USD | 190,850.00 USD | 428,210.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 79,360,000.00 USD | 79,360,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 591,080.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 76,790,000.00 USD | 76,790,000.00 USD | 784,530.00 USD | 121,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 78,520,000.00 USD | 78,520,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 74,660,000.00 USD | 74,660,000.00 USD | 273,620.00 USD | 837,160.00 USD | 663,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 76,940,000.00 USD | 76,940,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 72,890,000.00 USD | 72,890,000.00 USD | 866,770.00 USD | 471,100.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 73,930,000.00 USD | 73,930,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,980,000.00 USD | 68,980,000.00 USD | 215,570.00 USD | 258,510.00 USD | 985,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 72,470,000.00 USD | 72,470,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 67,520,000.00 USD | 67,520,000.00 USD | 567,590.00 USD | 566,410.00 USD | 551,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 71,600,000.00 USD | 71,600,000.00 USD | 47,500.00 USD | 723,100.00 USD | 155,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 2,340.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 65,830,000.00 USD | 65,830,000.00 USD | 403,550.00 USD | 553,180.00 USD | 678,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 70,670,000.00 USD | 70,670,000.00 USD | 0.00 USD | 77,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 64,200,000.00 USD | 64,200,000.00 USD | 1,700,000.00 USD | 343,110.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 70,600,000.00 USD | 70,600,000.00 USD | 556,190.00 USD | 0.00 USD | 635,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 60,170,000.00 USD | 60,170,000.00 USD | 668,540.00 USD | 487,120.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 69,410,000.00 USD | 69,410,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 57,700,000.00 USD | 57,700,000.00 USD | 1,520,000.00 USD | 657,210.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 65,200,000.00 USD | 65,200,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 53,960,000.00 USD | 53,960,000.00 USD | 30,610.00 USD | 180,830.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 62,950,000.00 USD | 62,950,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 88,230.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 52,660,000.00 USD | 52,660,000.00 USD | 226,520.00 USD | 196,610.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 61,420,000.00 USD | 61,420,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 51,060,000.00 USD | 51,060,000.00 USD | 143,650.00 USD | 4,200.00 USD | 243,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 61,010,000.00 USD | 61,010,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 50,670,000.00 USD | 50,670,000.00 USD | 222,150.00 USD | 97,750.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 60,280,000.00 USD | 60,280,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 50,350,000.00 USD | 50,350,000.00 USD | 113,990.00 USD | 279,120.00 USD | 446,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 59,190,000.00 USD | 59,190,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 49,510,000.00 USD | 49,510,000.00 USD | 256,850.00 USD | 0.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 59,020,000.00 USD | 59,020,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,650,000.00 USD | 6,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 46,610,000.00 USD | 46,610,000.00 USD | 567,980.00 USD | 786,020.00 USD | 996,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 58,760,000.00 USD | 58,760,000.00 USD | 112,770.00 USD | 802,580.00 USD | 482,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 44,260,000.00 USD | 44,260,000.00 USD | 542,470.00 USD | 753,290.00 USD | 587,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 57,360,000.00 USD | 57,360,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 42,380,000.00 USD | 42,380,000.00 USD | 306,680.00 USD | 1,040,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 56,330,000.00 USD | 56,330,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 37,640,000.00 USD | 37,640,000.00 USD | 1,280,000.00 USD | 1,370,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 53,870,000.00 USD | 53,870,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 30,740,000.00 USD | 30,740,000.00 USD | 563,990.00 USD | 1,290,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 50,180,000.00 USD | 50,180,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 58,510.00 USD | 58,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 26,930,000.00 USD | 26,930,000.00 USD | 324,100.00 USD | 1,140,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 42,160,000.00 USD | 42,160,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 23,930,000.00 USD | 23,930,000.00 USD | 1,040,000.00 USD | 677,190.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 35,010,000.00 USD | 35,010,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 20,130,000.00 USD | 20,130,000.00 USD | 765,930.00 USD | 711,040.00 USD | 2,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 25,590,000.00 USD | 25,590,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,320,000.00 USD | 16,320,000.00 USD | 505,370.00 USD | 1,090,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 21,010,000.00 USD | 21,010,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 13,220,000.00 USD | 13,220,000.00 USD | 1,850,000.00 USD | 531,700.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 18,280,000.00 USD | 18,280,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 7,170,000.00 USD | 7,170,000.00 USD | 1,260,000.00 USD | 585,560.00 USD | 895,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 15,080,000.00 USD | 15,080,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 4,430,000.00 USD | 4,430,000.00 USD | 313,550.00 USD | 1,380,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 7,360,000.00 USD | 7,360,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 262,800.00 USD | 262,800.00 USD | 0.00 USD | 4,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 712,160.00 USD | 712,160.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 258,050.00 USD | 258,050.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 254,670.00 USD | 254,670.00 USD | 0.00 USD | 4,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 222,480.00 USD | 222,480.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 249,690.00 USD | 249,690.00 USD | 0.00 USD | 7,650.00 USD | 242,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 158,820.00 USD | 158,820.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 24,960.00 USD | 24,960.00 USD | 0.00 USD | 24,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 19,840.00 USD | 19,840.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 29,940.00 USD | 29,940.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 182,400.00 USD | 182,400.00 USD | 0.00 USD | 100,700.00 USD | 56,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 177,500.00 USD | 177,500.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,760,000.00 USD | 2,760,000.00 USD | 580,850.00 USD | 445,620.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 542,940.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 4,620,000.00 USD | 4,620,000.00 USD | 1,130,000.00 USD | 347,010.00 USD | 381,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 6,030,000.00 USD | 6,030,000.00 USD | 4,260,000.00 USD | 9,150.00 USD | 20,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 6,870,000.00 USD | 6,870,000.00 USD | 424,040.00 USD | 1,340,000.00 USD | 487,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 1,870,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 14,070,000.00 USD | 14,070,000.00 USD | 1,080,000.00 USD | 1,440,000.00 USD | 4,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 15,800,000.00 USD | 15,800,000.00 USD | 138,500.00 USD | 2,750,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 18,180,000.00 USD | 18,180,000.00 USD | 1,460,000.00 USD | 1,170,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 25,210,000.00 USD | 25,210,000.00 USD | 1,680,000.00 USD | 5,300,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 26,070,000.00 USD | 26,070,000.00 USD | 1,130,000.00 USD | 2,290,000.00 USD | 4,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 42,550,000.00 USD | 42,550,000.00 USD | 2,710,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 11,660.00 USD | 11,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 33,670,000.00 USD | 33,670,000.00 USD | 1,650,000.00 USD | 2,090,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 57,420,000.00 USD | 57,420,000.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 43,450,000.00 USD | 43,450,000.00 USD | 3,740,000.00 USD | 1,540,000.00 USD | 4,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 76,570,000.00 USD | 76,570,000.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 7,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 48,670,000.00 USD | 48,670,000.00 USD | 373,090.00 USD | 1,940,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 79,670,000.00 USD | 79,670,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 52,800,000.00 USD | 52,800,000.00 USD | 943,390.00 USD | 371,640.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 81,700,000.00 USD | 81,700,000.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 55,880,000.00 USD | 55,880,000.00 USD | 1,210,000.00 USD | 556,340.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 85,950,000.00 USD | 85,950,000.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 236,840.00 USD | 248,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 60,180,000.00 USD | 60,180,000.00 USD | 818,130.00 USD | 1,150,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 91,080,000.00 USD | 91,080,000.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 62,020,000.00 USD | 62,020,000.00 USD | 787,490.00 USD | 459,210.00 USD | 591,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 91,800,000.00 USD | 91,800,000.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 62,850,000.00 USD | 62,850,000.00 USD | 156,280.00 USD | 216,580.00 USD | 456,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 93,410,000.00 USD | 93,410,000.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 66,190,000.00 USD | 66,190,000.00 USD | 378,690.00 USD | 236,920.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 96,000,000.00 USD | 96,000,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 70,450,000.00 USD | 70,450,000.00 USD | 1,170,000.00 USD | 375,550.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 99,650,000.00 USD | 99,650,000.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 49,010.00 USD | 297,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 75,730,000.00 USD | 75,730,000.00 USD | 1,460,000.00 USD | 1,240,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 106,940,000.00 USD | 106,940,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 76,880,000.00 USD | 76,880,000.00 USD | 473,750.00 USD | 23,070.00 USD | 653,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 108,890,000.00 USD | 108,890,000.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 78,660,000.00 USD | 78,660,000.00 USD | 361,100.00 USD | 395,780.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 111,260,000.00 USD | 111,260,000.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 81,380,000.00 USD | 81,380,000.00 USD | 804,300.00 USD | 722,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 112,290,000.00 USD | 112,290,000.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 82,750,000.00 USD | 82,750,000.00 USD | 407,960.00 USD | 304,910.00 USD | 660,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 115,090,000.00 USD | 115,090,000.00 USD | 0.00 USD | 2,170,000.00 USD | 635,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 2,250.00 USD | 299,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 84,610,000.00 USD | 84,610,000.00 USD | 568,970.00 USD | 528,000.00 USD | 760,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 117,100,000.00 USD | 117,100,000.00 USD | 1,770,000.00 USD | 238,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 88,310,000.00 USD | 88,310,000.00 USD | 937,850.00 USD | 491,550.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 122,520,000.00 USD | 122,520,000.00 USD | 1,550,000.00 USD | 821,310.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 91,690,000.00 USD | 91,690,000.00 USD | 1,290,000.00 USD | 360,440.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 125,290,000.00 USD | 125,290,000.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 94,400,000.00 USD | 94,400,000.00 USD | 928,510.00 USD | 636,000.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 130,160,000.00 USD | 130,160,000.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 95,970,000.00 USD | 95,970,000.00 USD | 520,400.00 USD | 158,070.00 USD | 891,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 131,460,000.00 USD | 131,460,000.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 55,110.00 USD | 354,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 99,030,000.00 USD | 99,030,000.00 USD | 190,130.00 USD | 633,280.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 136,170,000.00 USD | 136,170,000.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 105,100,000.00 USD | 105,100,000.00 USD | 1,760,000.00 USD | 781,570.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 141,270,000.00 USD | 141,270,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 107,470,000.00 USD | 107,470,000.00 USD | 1,270,000.00 USD | 214,860.00 USD | 886,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 143,290,000.00 USD | 143,290,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 110,400,000.00 USD | 110,400,000.00 USD | 1,140,000.00 USD | 648,560.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 146,650,000.00 USD | 146,650,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 112,180,000.00 USD | 112,180,000.00 USD | 867,870.00 USD | 62,710.00 USD | 851,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 149,430,000.00 USD | 149,430,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 7,390.00 USD | 362,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 113,220,000.00 USD | 113,220,000.00 USD | 405,790.00 USD | 56,240.00 USD | 578,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 151,230,000.00 USD | 151,230,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 114,430,000.00 USD | 114,430,000.00 USD | 545,530.00 USD | 170,390.00 USD | 494,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 152,330,000.00 USD | 152,330,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 116,130,000.00 USD | 116,130,000.00 USD | 729,070.00 USD | 105,530.00 USD | 862,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 154,040,000.00 USD | 154,040,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 117,950,000.00 USD | 117,950,000.00 USD | 465,720.00 USD | 179,640.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 156,510,000.00 USD | 156,510,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 119,810,000.00 USD | 119,810,000.00 USD | 783,210.00 USD | 229,580.00 USD | 838,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 158,540,000.00 USD | 158,540,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 44,760.00 USD | 407,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 120,920,000.00 USD | 120,920,000.00 USD | 286,040.00 USD | 208,270.00 USD | 616,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 160,080,000.00 USD | 160,080,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 121,450,000.00 USD | 121,450,000.00 USD | 289,820.00 USD | 79,720.00 USD | 164,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 162,520,000.00 USD | 162,520,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 122,310,000.00 USD | 122,310,000.00 USD | 347,480.00 USD | 138,730.00 USD | 373,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 164,380,000.00 USD | 164,380,000.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 123,680,000.00 USD | 123,680,000.00 USD | 755,550.00 USD | 209,130.00 USD | 407,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 169,840,000.00 USD | 169,840,000.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 125,010,000.00 USD | 125,010,000.00 USD | 496,280.00 USD | 327,230.00 USD | 502,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 176,970,000.00 USD | 176,970,000.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,380.00 USD | 413,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 125,640,000.00 USD | 125,640,000.00 USD | 221,820.00 USD | 72,280.00 USD | 333,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 185,220,000.00 USD | 185,220,000.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,130,000.00 USD | 126,130,000.00 USD | 177,760.00 USD | 23,630.00 USD | 287,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 192,970,000.00 USD | 192,970,000.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,480,000.00 USD | 126,480,000.00 USD | 177,170.00 USD | 30,570.00 USD | 146,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 200,990,000.00 USD | 200,990,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,750,000.00 USD | 126,750,000.00 USD | 69,740.00 USD | 28,660.00 USD | 174,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 210,110,000.00 USD | 210,110,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 127,060,000.00 USD | 127,060,000.00 USD | 105,080.00 USD | 3,170.00 USD | 194,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 216,860,000.00 USD | 216,860,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 14,410.00 USD | 427,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 127,880,000.00 USD | 127,880,000.00 USD | 335,960.00 USD | 65,930.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 223,200,000.00 USD | 223,200,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,390,000.00 USD | 128,390,000.00 USD | 148,530.00 USD | 42,970.00 USD | 310,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 225,740,000.00 USD | 225,740,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,940,000.00 USD | 128,940,000.00 USD | 269,010.00 USD | 49,330.00 USD | 234,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 228,610,000.00 USD | 228,610,000.00 USD | 1,380,000.00 USD | 282,890.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,470,000.00 USD | 129,470,000.00 USD | 143,090.00 USD | 115,680.00 USD | 276,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 232,150,000.00 USD | 232,150,000.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,570,000.00 USD | 129,570,000.00 USD | 78,610.00 USD | 14,730.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 234,880,000.00 USD | 234,880,000.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 99,580.00 USD | 527,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,840,000.00 USD | 129,840,000.00 USD | 56,040.00 USD | 1,320.00 USD | 206,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 235,700,000.00 USD | 235,700,000.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,070,000.00 USD | 130,070,000.00 USD | 97,000.00 USD | 109,930.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 236,760,000.00 USD | 236,760,000.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,080,000.00 USD | 130,080,000.00 USD | 0.00 USD | 10,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 238,070,000.00 USD | 238,070,000.00 USD | 367,350.00 USD | 211,750.00 USD | 733,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,210,000.00 USD | 130,210,000.00 USD | 5,340.00 USD | 30,930.00 USD | 88,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 239,300,000.00 USD | 239,300,000.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,290,000.00 USD | 130,290,000.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 240,970,000.00 USD | 240,970,000.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,780.00 USD | 531,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,690,000.00 USD | 130,690,000.00 USD | 126,800.00 USD | 70,270.00 USD | 204,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 242,000,000.00 USD | 242,000,000.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,990,000.00 USD | 130,990,000.00 USD | 74,360.00 USD | 54,840.00 USD | 167,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 243,460,000.00 USD | 243,460,000.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,170,000.00 USD | 131,170,000.00 USD | 2,320.00 USD | 47,610.00 USD | 130,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 245,160,000.00 USD | 245,160,000.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,380,000.00 USD | 131,380,000.00 USD | 5,270.00 USD | 66,500.00 USD | 144,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 247,020,000.00 USD | 247,020,000.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,740,000.00 USD | 131,740,000.00 USD | 5,520.00 USD | 70,330.00 USD | 275,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 248,000,000.00 USD | 248,000,000.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,790.00 USD | 532,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,030,000.00 USD | 132,030,000.00 USD | 91,470.00 USD | 89,100.00 USD | 115,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 249,120,000.00 USD | 249,120,000.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,390,000.00 USD | 132,390,000.00 USD | 42,870.00 USD | 153,630.00 USD | 163,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 250,330,000.00 USD | 250,330,000.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,500,000.00 USD | 132,500,000.00 USD | 38,180.00 USD | 18,330.00 USD | 49,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,080,000.00 USD | 251,080,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,610,000.00 USD | 251,610,000.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,770,000.00 USD | 251,770,000.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,310.00 USD | 535,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 251,990,000.00 USD | 251,990,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,000,000.00 USD | 252,000,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,060,000.00 USD | 252,060,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,140,000.00 USD | 252,140,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,440,000.00 USD | 252,440,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 858.46 USD | 536,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 252,590,000.00 USD | 252,590,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 252,730,000.00 USD | 252,730,000.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 253,010,000.00 USD | 253,010,000.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,730.00 USD | 539,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,510.00 USD | 633,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 581,410.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 131,660.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 551.65 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,150.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 445.48 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 12,020.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 4,430,000.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,260.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 130,580.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,530.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 1,300.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 7,750.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 233.59 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 5,020.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 110.17 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 1,100.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 113,500.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 591.43 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 808.37 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 5,450,000.00 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 130,160.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 6,020.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 1,750.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 260.98 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 32,740.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,010.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 2,890,000.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 309,780.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 1,410.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 844.13 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,560.00 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 701.75 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 679.06 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 178.20 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 2,450,000.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 460.50 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 124.50 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 548.36 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 419,330.00 USD | 18,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 18,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 23,880.00 USD | 18,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 249,280.00 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 631.42 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 52,120.00 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.02 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 2,230.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 82,330.00 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 102.81 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 103.27 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 11,280.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 122.31 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 142.29 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 106.03 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 44,930.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 144.15 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 82,210.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 1,320.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 11,910.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 20,890.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 477.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 96,030.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 678.62 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 654.75 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 24,350.00 USD | 18,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 3,700,000.00 USD | 22,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 58,200.00 USD | 22,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 1,900,000.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 1,870.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,630.00 USD | 24,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,650,000.00 USD | 0.00 USD | 1,360.00 USD | `-79.73%` | `5,324.00` |
| `Live` | `Long` | `0.2650` | 64,650,000.00 USD | 0.00 USD | 1,720.00 USD | `-78.93%` | `6,474.00` |
| `Live` | `Long` | `0.2750` | 64,650,000.00 USD | 0.00 USD | 3,220.00 USD | `-78.14%` | `11,707.00` |
| `Live` | `Long` | `0.2850` | 64,640,000.00 USD | 0.00 USD | 378.20 USD | `-77.34%` | `1,327.00` |
| `Live` | `Long` | `0.2950` | 64,640,000.00 USD | 0.00 USD | 28,780.00 USD | `-76.55%` | `97,549.00` |
| `Live` | `Long` | `0.3050` | 64,610,000.00 USD | 0.00 USD | 235.16 USD | `-75.75%` | `771.00` |
| `Live` | `Long` | `0.3150` | 64,610,000.00 USD | 0.00 USD | 5,320.00 USD | `-74.96%` | `16,894.00` |
| `Live` | `Long` | `0.3250` | 64,610,000.00 USD | 0.00 USD | 4,710.00 USD | `-74.16%` | `14,484.00` |
| `Live` | `Long` | `0.3350` | 64,600,000.00 USD | 0.00 USD | 1,930.00 USD | `-73.37%` | `5,751.00` |
| `Live` | `Long` | `0.3450` | 64,600,000.00 USD | 0.00 USD | 16,980.00 USD | `-72.57%` | `49,212.00` |
| `Live` | `Long` | `0.3550` | 64,580,000.00 USD | 0.00 USD | 2,180.00 USD | `-71.78%` | `6,137.00` |
| `Live` | `Long` | `0.3650` | 64,580,000.00 USD | 0.00 USD | 49,350.00 USD | `-70.98%` | `135,212.00` |
| `Live` | `Long` | `0.3750` | 64,530,000.00 USD | 0.00 USD | 3,160.00 USD | `-70.19%` | `8,418.00` |
| `Live` | `Long` | `0.3950` | 64,530,000.00 USD | 0.00 USD | 2,170.00 USD | `-68.60%` | `5,496.00` |
| `Live` | `Long` | `0.4050` | 64,530,000.00 USD | 0.00 USD | 614.38 USD | `-67.80%` | `1,517.00` |
| `Live` | `Long` | `0.4150` | 64,530,000.00 USD | 0.00 USD | 1,170.00 USD | `-67.01%` | `2,821.00` |
| `Live` | `Long` | `0.4250` | 64,520,000.00 USD | 0.00 USD | 29,680.00 USD | `-66.21%` | `69,842.00` |
| `Live` | `Long` | `0.4350` | 64,500,000.00 USD | 0.00 USD | 577,120.00 USD | `-65.42%` | `1,326,707.00` |
| `Live` | `Long` | `0.4450` | 63,920,000.00 USD | 0.00 USD | 883.77 USD | `-64.62%` | `1,986.00` |
| `Live` | `Long` | `0.4550` | 63,920,000.00 USD | 0.00 USD | 160,020.00 USD | `-63.83%` | `351,693.00` |
| `Live` | `Long` | `0.4650` | 63,760,000.00 USD | 0.00 USD | 397.11 USD | `-63.03%` | `854.00` |
| `Live` | `Long` | `0.4750` | 63,760,000.00 USD | 0.00 USD | 2,000.00 USD | `-62.24%` | `4,211.00` |
| `Live` | `Long` | `0.4850` | 63,750,000.00 USD | 0.00 USD | 323.98 USD | `-61.44%` | `668.00` |
| `Live` | `Long` | `0.4950` | 63,750,000.00 USD | 0.00 USD | 6,470.00 USD | `-60.65%` | `13,074.00` |
| `Live` | `Long` | `0.5050` | 63,750,000.00 USD | 0.00 USD | 188.87 USD | `-59.85%` | `374.00` |
| `Live` | `Long` | `0.5150` | 63,750,000.00 USD | 0.00 USD | 9,050.00 USD | `-59.06%` | `17,571.00` |
| `Live` | `Long` | `0.5250` | 63,740,000.00 USD | 0.00 USD | 2,810.00 USD | `-58.26%` | `5,352.00` |
| `Live` | `Long` | `0.5350` | 63,740,000.00 USD | 0.00 USD | 3,530.00 USD | `-57.47%` | `6,591.00` |
| `Live` | `Long` | `0.5450` | 63,730,000.00 USD | 0.00 USD | 27,050.00 USD | `-56.67%` | `49,627.00` |
| `Live` | `Long` | `0.5550` | 63,710,000.00 USD | 0.00 USD | 160,990.00 USD | `-55.88%` | `290,074.00` |
| `Live` | `Long` | `0.5650` | 63,540,000.00 USD | 0.00 USD | 2,070.00 USD | `-55.08%` | `3,667.00` |
| `Live` | `Long` | `0.5750` | 63,540,000.00 USD | 0.00 USD | 8,760.00 USD | `-54.29%` | `15,235.00` |
| `Live` | `Long` | `0.5850` | 63,530,000.00 USD | 0.00 USD | 4,900.00 USD | `-53.49%` | `8,376.00` |
| `Live` | `Long` | `0.5950` | 63,530,000.00 USD | 0.00 USD | 198.13 USD | `-52.70%` | `333.00` |
| `Live` | `Long` | `0.6050` | 63,530,000.00 USD | 0.00 USD | 23,080.00 USD | `-51.90%` | `38,148.00` |
| `Live` | `Long` | `0.6150` | 63,510,000.00 USD | 0.00 USD | 39,120.00 USD | `-51.11%` | `63,607.00` |
| `Live` | `Long` | `0.6250` | 63,470,000.00 USD | 0.00 USD | 1,130.00 USD | `-50.31%` | `1,803.00` |
| `Live` | `Long` | `0.6350` | 63,470,000.00 USD | 0.00 USD | 10,510.00 USD | `-49.52%` | `16,554.00` |
| `Live` | `Long` | `0.6450` | 63,450,000.00 USD | 0.00 USD | 21,730.00 USD | `-48.72%` | `33,694.00` |
| `Live` | `Long` | `0.6550` | 63,430,000.00 USD | 0.00 USD | 2,630.00 USD | `-47.93%` | `4,011.00` |
| `Live` | `Long` | `0.6650` | 63,430,000.00 USD | 0.00 USD | 17,790.00 USD | `-47.13%` | `26,754.00` |
| `Live` | `Long` | `0.6750` | 63,410,000.00 USD | 0.00 USD | 26,110.00 USD | `-46.34%` | `38,677.00` |
| `Live` | `Long` | `0.6850` | 63,390,000.00 USD | 0.00 USD | 2,980.00 USD | `-45.54%` | `4,356.00` |
| `Live` | `Long` | `0.6950` | 63,380,000.00 USD | 0.00 USD | 160,780.00 USD | `-44.75%` | `231,342.00` |
| `Live` | `Long` | `0.7050` | 63,220,000.00 USD | 0.00 USD | 23,200.00 USD | `-43.95%` | `32,902.00` |
| `Live` | `Long` | `0.7150` | 63,200,000.00 USD | 0.00 USD | 68,280.00 USD | `-43.16%` | `95,503.00` |
| `Live` | `Long` | `0.7250` | 63,130,000.00 USD | 0.00 USD | 235,740.00 USD | `-42.36%` | `325,156.00` |
| `Live` | `Long` | `0.7350` | 62,900,000.00 USD | 0.00 USD | 45,360.00 USD | `-41.57%` | `61,711.00` |
| `Live` | `Long` | `0.7450` | 62,850,000.00 USD | 0.00 USD | 81,440.00 USD | `-40.77%` | `109,317.00` |
| `Live` | `Long` | `0.7550` | 62,770,000.00 USD | 0.00 USD | 147,720.00 USD | `-39.98%` | `195,652.00` |
| `Live` | `Long` | `0.7650` | 62,620,000.00 USD | 0.00 USD | 2,190.00 USD | `-39.18%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 62,620,000.00 USD | 0.00 USD | 5,930.00 USD | `-38.39%` | `7,652.00` |
| `Live` | `Long` | `0.7850` | 62,610,000.00 USD | 0.00 USD | 16,460.00 USD | `-37.59%` | `20,966.00` |
| `Live` | `Long` | `0.7950` | 62,600,000.00 USD | 0.00 USD | 44,850.00 USD | `-36.80%` | `56,417.00` |
| `Live` | `Long` | `0.8050` | 62,550,000.00 USD | 0.00 USD | 511,010.00 USD | `-36.00%` | `634,796.00` |
| `Live` | `Long` | `0.8150` | 62,040,000.00 USD | 0.00 USD | 61,010.00 USD | `-35.21%` | `74,853.00` |
| `Live` | `Long` | `0.8250` | 61,980,000.00 USD | 0.00 USD | 23,130.00 USD | `-34.41%` | `28,036.00` |
| `Live` | `Long` | `0.8350` | 61,960,000.00 USD | 0.00 USD | 32,170.00 USD | `-33.62%` | `38,528.00` |
| `Live` | `Long` | `0.8450` | 61,920,000.00 USD | 0.00 USD | 3,050,000.00 USD | `-32.82%` | `3,614,999.00` |
| `Live` | `Long` | `0.8550` | 58,870,000.00 USD | 0.00 USD | 61,290.00 USD | `-32.03%` | `71,682.00` |
| `Live` | `Long` | `0.8650` | 58,810,000.00 USD | 0.00 USD | 38,050.00 USD | `-31.23%` | `43,985.00` |
| `Live` | `Long` | `0.8750` | 58,770,000.00 USD | 0.00 USD | 93,870.00 USD | `-30.44%` | `107,279.00` |
| `Live` | `Long` | `0.8850` | 58,680,000.00 USD | 0.00 USD | 358,270.00 USD | `-29.64%` | `404,830.00` |
| `Live` | `Long` | `0.8950` | 58,320,000.00 USD | 0.00 USD | 97,380.00 USD | `-28.85%` | `108,809.00` |
| `Live` | `Long` | `0.9050` | 58,220,000.00 USD | 0.00 USD | 231,270.00 USD | `-28.05%` | `255,546.00` |
| `Live` | `Long` | `0.9150` | 57,990,000.00 USD | 0.00 USD | 87,390.00 USD | `-27.26%` | `95,507.00` |
| `Live` | `Long` | `0.9250` | 57,900,000.00 USD | 0.00 USD | 76,320.00 USD | `-26.46%` | `82,511.00` |
| `Live` | `Long` | `0.9350` | 57,830,000.00 USD | 0.00 USD | 97,440.00 USD | `-25.67%` | `104,213.00` |
| `Live` | `Long` | `0.9450` | 57,730,000.00 USD | 0.00 USD | 56,350.00 USD | `-24.87%` | `59,627.00` |
| `Live` | `Long` | `0.9550` | 57,670,000.00 USD | 0.00 USD | 153,860.00 USD | `-24.08%` | `161,112.00` |
| `Live` | `Long` | `0.9650` | 57,520,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-23.28%` | `35,121,908.00` |
| `Live` | `Long` | `0.9750` | 23,630,000.00 USD | 0.00 USD | 155,450.00 USD | `-22.49%` | `159,439.00` |
| `Live` | `Long` | `0.9850` | 23,470,000.00 USD | 0.00 USD | 455,050.00 USD | `-21.69%` | `461,984.00` |
| `Live` | `Long` | `0.9950` | 23,010,000.00 USD | 0.00 USD | 113,040.00 USD | `-20.90%` | `113,607.00` |
| `Live` | `Long` | `1.00` | 22,900,000.00 USD | 0.00 USD | 506,580.00 USD | `-20.10%` | `504,061.00` |
| `Live` | `Long` | `1.01` | 22,400,000.00 USD | 0.00 USD | 304,640.00 USD | `-19.31%` | `300,135.00` |
| `Live` | `Long` | `1.02` | 22,090,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-18.51%` | `2,643,366.00` |
| `Live` | `Long` | `1.03` | 19,380,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-17.72%` | `2,061,017.00` |
| `Live` | `Long` | `1.04` | 17,250,000.00 USD | 0.00 USD | 178,070.00 USD | `-16.93%` | `170,398.00` |
| `Live` | `Long` | `1.05` | 17,070,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-16.13%` | `1,556,547.00` |
| `Live` | `Long` | `1.06` | 15,430,000.00 USD | 0.00 USD | 388,560.00 USD | `-15.34%` | `364,841.00` |
| `Live` | `Long` | `1.07` | 15,040,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-14.54%` | `1,246,853.00` |
| `Live` | `Long` | `1.08` | 13,700,000.00 USD | 0.00 USD | 178,030.00 USD | `-13.75%` | `164,087.00` |
| `Live` | `Long` | `1.09` | 13,520,000.00 USD | 0.00 USD | 377,320.00 USD | `-12.95%` | `344,587.00` |
| `Live` | `Long` | `1.10` | 13,140,000.00 USD | 0.00 USD | 101,470.00 USD | `-12.16%` | `91,829.00` |
| `Live` | `Long` | `1.11` | 13,040,000.00 USD | 0.00 USD | 278,180.00 USD | `-11.36%` | `249,487.00` |
| `Live` | `Long` | `1.12` | 12,760,000.00 USD | 0.00 USD | 2,410,000.00 USD | `-10.57%` | `2,145,674.00` |
| `Live` | `Long` | `1.14` | 10,350,000.00 USD | 0.00 USD | 185,410.00 USD | `-9.77%` | `163,353.00` |
| `Live` | `Long` | `1.15` | 10,160,000.00 USD | 0.00 USD | 284,790.00 USD | `-8.98%` | `248,727.00` |
| `Live` | `Long` | `1.16` | 9,880,000.00 USD | 0.00 USD | 361,410.00 USD | `-8.18%` | `312,909.00` |
| `Live` | `Long` | `1.17` | 9,520,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-7.39%` | `1,102,296.00` |
| `Live` | `Long` | `1.18` | 8,230,000.00 USD | 0.00 USD | 276,740.00 USD | `-6.59%` | `235,527.00` |
| `Live` | `Long` | `1.19` | 7,960,000.00 USD | 0.00 USD | 568,820.00 USD | `-5.80%` | `480,017.00` |
| `Live` | `Long` | `1.20` | 7,390,000.00 USD | 0.00 USD | 591,080.00 USD | `-5.00%` | `494,630.00` |
| `Live` | `Long` | `1.21` | 6,800,000.00 USD | 0.00 USD | 2,340.00 USD | `-4.21%` | `1,944.00` |
| `Live` | `Long` | `1.22` | 6,800,000.00 USD | 0.00 USD | 88,230.00 USD | `-3.41%` | `72,621.00` |
| `Live` | `Long` | `1.23` | 6,710,000.00 USD | 0.00 USD | 6,650,000.00 USD | `-2.62%` | `5,427,233.00` |
| `Live` | `Long` | `1.24` | 58,510.00 USD | 0.00 USD | 58,510.00 USD | `-1.82%` | `47,377.00` |
| `Live` | `Short` | `1.27` | 11,660.00 USD | 11,660.00 USD | 0.00 USD | `+1.36%` | `9,146.00` |
| `Live` | `Short` | `1.28` | 248,500.00 USD | 236,840.00 USD | 0.00 USD | `+2.15%` | `184,310.00` |
| `Live` | `Short` | `1.29` | 297,510.00 USD | 49,010.00 USD | 0.00 USD | `+2.95%` | `37,848.00` |
| `Live` | `Short` | `1.30` | 299,770.00 USD | 2,250.00 USD | 0.00 USD | `+3.74%` | `1,726.00` |
| `Live` | `Short` | `1.31` | 354,880.00 USD | 55,110.00 USD | 0.00 USD | `+4.54%` | `41,912.00` |
| `Live` | `Short` | `1.32` | 362,270.00 USD | 7,390.00 USD | 0.00 USD | `+5.33%` | `5,576.00` |
| `Live` | `Short` | `1.33` | 407,030.00 USD | 44,760.00 USD | 0.00 USD | `+6.13%` | `33,531.00` |
| `Live` | `Short` | `1.34` | 413,410.00 USD | 6,380.00 USD | 0.00 USD | `+6.92%` | `4,742.00` |
| `Live` | `Short` | `1.35` | 427,820.00 USD | 14,410.00 USD | 0.00 USD | `+7.72%` | `10,638.00` |
| `Live` | `Short` | `1.36` | 527,400.00 USD | 99,580.00 USD | 0.00 USD | `+8.51%` | `72,950.00` |
| `Live` | `Short` | `1.38` | 531,180.00 USD | 3,780.00 USD | 0.00 USD | `+9.31%` | `2,747.00` |
| `Live` | `Short` | `1.39` | 532,970.00 USD | 1,790.00 USD | 0.00 USD | `+10.10%` | `1,293.00` |
| `Live` | `Short` | `1.40` | 535,280.00 USD | 2,310.00 USD | 0.00 USD | `+10.90%` | `1,659.00` |
| `Live` | `Short` | `1.41` | 536,140.00 USD | 858.46 USD | 0.00 USD | `+11.69%` | `611.00` |
| `Live` | `Short` | `1.42` | 539,870.00 USD | 3,730.00 USD | 0.00 USD | `+12.49%` | `2,635.00` |
| `Live` | `Short` | `1.43` | 633,380.00 USD | 93,510.00 USD | 0.00 USD | `+13.28%` | `65,619.00` |
| `Live` | `Short` | `1.44` | 1,210,000.00 USD | 581,410.00 USD | 0.00 USD | `+14.08%` | `405,163.00` |
| `Live` | `Short` | `1.45` | 1,220,000.00 USD | 284.66 USD | 0.00 USD | `+14.87%` | `197.00` |
| `Live` | `Short` | `1.47` | 1,350,000.00 USD | 131,660.00 USD | 0.00 USD | `+16.46%` | `89,871.00` |
| `Live` | `Short` | `1.48` | 1,350,000.00 USD | 551.65 USD | 0.00 USD | `+17.26%` | `374.00` |
| `Live` | `Short` | `1.50` | 1,360,000.00 USD | 12,150.00 USD | 0.00 USD | `+18.85%` | `8,126.00` |
| `Live` | `Short` | `1.50` | 1,360,000.00 USD | 445.48 USD | 0.00 USD | `+19.64%` | `296.00` |
| `Live` | `Short` | `1.51` | 1,370,000.00 USD | 12,020.00 USD | 0.00 USD | `+20.44%` | `7,935.00` |
| `Live` | `Short` | `1.53` | 1,370,000.00 USD | 174.99 USD | 0.00 USD | `+22.03%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,370,000.00 USD | 1,370.00 USD | 0.00 USD | `+22.82%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,370,000.00 USD | 1,360.00 USD | 0.00 USD | `+23.62%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,380,000.00 USD | 555.57 USD | 0.00 USD | `+24.41%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,380,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.21%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 5,810,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+26.00%` | `2,793,593.00` |
| `Live` | `Short` | `1.59` | 5,810,000.00 USD | 1,260.00 USD | 0.00 USD | `+26.80%` | `789.00` |
| `Live` | `Short` | `1.60` | 5,940,000.00 USD | 130,580.00 USD | 0.00 USD | `+27.59%` | `81,359.00` |
| `Live` | `Short` | `1.61` | 5,940,000.00 USD | 2,530.00 USD | 0.00 USD | `+28.39%` | `1,567.00` |
| `Live` | `Short` | `1.62` | 5,940,000.00 USD | 1,300.00 USD | 0.00 USD | `+29.18%` | `798.00` |
| `Live` | `Short` | `1.64` | 5,950,000.00 USD | 7,750.00 USD | 0.00 USD | `+29.98%` | `4,742.00` |
| `Live` | `Short` | `1.65` | 5,950,000.00 USD | 233.59 USD | 0.00 USD | `+30.77%` | `142.00` |
| `Live` | `Short` | `1.66` | 5,950,000.00 USD | 147.30 USD | 0.00 USD | `+31.57%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,950,000.00 USD | 586.08 USD | 0.00 USD | `+32.36%` | `352.00` |
| `Live` | `Short` | `1.68` | 5,960,000.00 USD | 5,020.00 USD | 0.00 USD | `+33.16%` | `3,000.00` |
| `Live` | `Short` | `1.69` | 5,960,000.00 USD | 4,180.00 USD | 0.00 USD | `+33.95%` | `2,481.00` |
| `Live` | `Short` | `1.70` | 5,960,000.00 USD | 110.17 USD | 0.00 USD | `+34.75%` | `65.00` |
| `Live` | `Short` | `1.71` | 5,960,000.00 USD | 1,980.00 USD | 0.00 USD | `+35.54%` | `1,163.00` |
| `Live` | `Short` | `1.72` | 5,960,000.00 USD | 1,100.00 USD | 0.00 USD | `+36.34%` | `642.00` |
| `Live` | `Short` | `1.74` | 5,970,000.00 USD | 2,970.00 USD | 0.00 USD | `+37.93%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 6,080,000.00 USD | 113,500.00 USD | 0.00 USD | `+38.72%` | `65,043.00` |
| `Live` | `Short` | `1.75` | 6,080,000.00 USD | 591.43 USD | 0.00 USD | `+39.52%` | `337.00` |
| `Live` | `Short` | `1.76` | 6,080,000.00 USD | 808.37 USD | 0.00 USD | `+40.31%` | `458.00` |
| `Live` | `Short` | `1.77` | 11,540,000.00 USD | 5,450,000.00 USD | 0.00 USD | `+41.11%` | `3,073,224.00` |
| `Live` | `Short` | `1.78` | 11,670,000.00 USD | 130,160.00 USD | 0.00 USD | `+41.90%` | `72,921.00` |
| `Live` | `Short` | `1.79` | 11,670,000.00 USD | 6,020.00 USD | 0.00 USD | `+42.70%` | `3,354.00` |
| `Live` | `Short` | `1.80` | 11,670,000.00 USD | 889.87 USD | 0.00 USD | `+43.49%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,670,000.00 USD | 1,750.00 USD | 0.00 USD | `+44.29%` | `963.00` |
| `Live` | `Short` | `1.82` | 11,670,000.00 USD | 260.98 USD | 0.00 USD | `+45.08%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,710,000.00 USD | 32,740.00 USD | 0.00 USD | `+45.88%` | `17,842.00` |
| `Live` | `Short` | `1.84` | 11,720,000.00 USD | 9,340.00 USD | 0.00 USD | `+46.67%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,720,000.00 USD | 428.50 USD | 0.00 USD | `+47.47%` | `231.00` |
| `Live` | `Short` | `1.86` | 11,720,000.00 USD | 2,010.00 USD | 0.00 USD | `+48.26%` | `1,079.00` |
| `Live` | `Short` | `1.88` | 14,610,000.00 USD | 2,890,000.00 USD | 0.00 USD | `+49.06%` | `1,540,696.00` |
| `Live` | `Short` | `1.90` | 14,920,000.00 USD | 309,780.00 USD | 0.00 USD | `+50.65%` | `163,470.00` |
| `Live` | `Short` | `1.91` | 14,920,000.00 USD | 373.38 USD | 0.00 USD | `+51.44%` | `196.00` |
| `Live` | `Short` | `1.92` | 14,920,000.00 USD | 1,410.00 USD | 0.00 USD | `+52.24%` | `737.00` |
| `Live` | `Short` | `1.95` | 14,920,000.00 USD | 844.13 USD | 0.00 USD | `+54.62%` | `434.00` |
| `Live` | `Short` | `1.96` | 14,920,000.00 USD | 293.25 USD | 0.00 USD | `+55.42%` | `150.00` |
| `Live` | `Short` | `1.97` | 15,150,000.00 USD | 227,560.00 USD | 0.00 USD | `+56.21%` | `115,806.00` |
| `Live` | `Short` | `1.98` | 15,150,000.00 USD | 651.75 USD | 0.00 USD | `+57.01%` | `330.00` |
| `Live` | `Short` | `2.00` | 15,150,000.00 USD | 701.75 USD | 0.00 USD | `+59.39%` | `350.00` |
| `Live` | `Short` | `2.02` | 15,150,000.00 USD | 679.06 USD | 0.00 USD | `+60.19%` | `337.00` |
| `Live` | `Short` | `2.02` | 15,150,000.00 USD | 178.20 USD | 0.00 USD | `+60.98%` | `88.00` |
| `Live` | `Short` | `2.04` | 17,600,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+62.57%` | `1,196,222.00` |
| `Live` | `Short` | `2.06` | 17,600,000.00 USD | 460.50 USD | 0.00 USD | `+64.16%` | `223.00` |
| `Live` | `Short` | `2.08` | 17,600,000.00 USD | 124.50 USD | 0.00 USD | `+64.96%` | `60.00` |
| `Live` | `Short` | `2.08` | 17,600,000.00 USD | 548.36 USD | 0.00 USD | `+65.75%` | `263.00` |
| `Live` | `Short` | `2.10` | 18,020,000.00 USD | 419,330.00 USD | 0.00 USD | `+66.55%` | `200,158.00` |
| `Live` | `Short` | `2.10` | 18,020,000.00 USD | 294.70 USD | 0.00 USD | `+67.34%` | `140.00` |
| `Live` | `Short` | `2.12` | 18,040,000.00 USD | 23,880.00 USD | 0.00 USD | `+68.14%` | `11,293.00` |
| `Live` | `Short` | `2.12` | 18,290,000.00 USD | 249,280.00 USD | 0.00 USD | `+68.93%` | `117,308.00` |
| `Live` | `Short` | `2.15` | 18,290,000.00 USD | 631.42 USD | 0.00 USD | `+71.32%` | `293.00` |
| `Live` | `Short` | `2.17` | 18,340,000.00 USD | 52,120.00 USD | 0.00 USD | `+72.91%` | `23,965.00` |
| `Live` | `Short` | `2.19` | 18,340,000.00 USD | 201.02 USD | 0.00 USD | `+73.70%` | `92.00` |
| `Live` | `Short` | `2.21` | 18,350,000.00 USD | 2,230.00 USD | 0.00 USD | `+75.29%` | `1,011.00` |
| `Live` | `Short` | `2.23` | 18,430,000.00 USD | 82,330.00 USD | 0.00 USD | `+76.88%` | `37,001.00` |
| `Live` | `Short` | `2.23` | 18,430,000.00 USD | 102.81 USD | 0.00 USD | `+77.68%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,430,000.00 USD | 103.27 USD | 0.00 USD | `+78.47%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,440,000.00 USD | 11,280.00 USD | 0.00 USD | `+79.27%` | `5,000.00` |
| `Live` | `Short` | `2.27` | 18,440,000.00 USD | 122.31 USD | 0.00 USD | `+80.06%` | `54.00` |
| `Live` | `Short` | `2.29` | 18,440,000.00 USD | 142.29 USD | 0.00 USD | `+82.45%` | `62.00` |
| `Live` | `Short` | `2.31` | 18,440,000.00 USD | 106.03 USD | 0.00 USD | `+83.24%` | `46.00` |
| `Live` | `Short` | `2.31` | 18,490,000.00 USD | 44,930.00 USD | 0.00 USD | `+84.04%` | `19,409.00` |
| `Live` | `Short` | `2.33` | 18,490,000.00 USD | 144.15 USD | 0.00 USD | `+84.83%` | `62.00` |
| `Live` | `Short` | `2.33` | 18,570,000.00 USD | 82,210.00 USD | 0.00 USD | `+85.63%` | `35,206.00` |
| `Live` | `Short` | `2.35` | 18,570,000.00 USD | 1,320.00 USD | 0.00 USD | `+86.42%` | `562.00` |
| `Live` | `Short` | `2.35` | 18,580,000.00 USD | 11,910.00 USD | 0.00 USD | `+87.22%` | `5,057.00` |
| `Live` | `Short` | `2.38` | 18,600,000.00 USD | 20,890.00 USD | 0.00 USD | `+88.81%` | `8,796.00` |
| `Live` | `Short` | `2.38` | 18,600,000.00 USD | 477.00 USD | 0.00 USD | `+89.60%` | `200.00` |
| `Live` | `Short` | `2.40` | 18,700,000.00 USD | 96,030.00 USD | 0.00 USD | `+90.40%` | `40,095.00` |
| `Live` | `Short` | `2.42` | 18,700,000.00 USD | 678.62 USD | 0.00 USD | `+91.99%` | `281.00` |
| `Live` | `Short` | `2.42` | 18,700,000.00 USD | 654.75 USD | 0.00 USD | `+92.78%` | `270.00` |
| `Live` | `Short` | `2.44` | 18,720,000.00 USD | 24,350.00 USD | 0.00 USD | `+93.58%` | `10,000.00` |
| `Live` | `Short` | `2.44` | 22,430,000.00 USD | 3,700,000.00 USD | 0.00 USD | `+94.37%` | `1,514,056.00` |
| `Live` | `Short` | `2.46` | 22,480,000.00 USD | 58,200.00 USD | 0.00 USD | `+95.17%` | `23,706.00` |
| `Live` | `Short` | `2.48` | 24,380,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+97.55%` | `763,874.00` |
| `Live` | `Short` | `2.50` | 24,380,000.00 USD | 1,870.00 USD | 0.00 USD | `+98.35%` | `750.00` |
| `Live` | `Short` | `2.52` | 24,390,000.00 USD | 5,630.00 USD | 0.00 USD | `+99.94%` | `2,240.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 3,950,000.00 USD | 0.00 USD | 102.00 USD | `-79.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 3,950,000.00 USD | 0.00 USD | 351.50 USD | `-70.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,950,000.00 USD | 0.00 USD | 139.12 USD | `-70.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 3,950,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 3,950,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,940,000.00 USD | 0.00 USD | 408.51 USD | `-64.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,940,000.00 USD | 0.00 USD | 273.00 USD | `-63.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,940,000.00 USD | 0.00 USD | 151.12 USD | `-63.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,940,000.00 USD | 0.00 USD | 142.50 USD | `-62.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,940,000.00 USD | 0.00 USD | 145.50 USD | `-61.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4950` | 3,940,000.00 USD | 0.00 USD | 562.81 USD | `-60.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,940,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 3,940,000.00 USD | 0.00 USD | 285.82 USD | `-59.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,940,000.00 USD | 0.00 USD | 306.60 USD | `-58.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,940,000.00 USD | 0.00 USD | 121.55 USD | `-55.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,940,000.00 USD | 0.00 USD | 656.53 USD | `-55.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,940,000.00 USD | 0.00 USD | 100.62 USD | `-53.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 3,940,000.00 USD | 0.00 USD | 203.75 USD | `-50.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,940,000.00 USD | 0.00 USD | 791.85 USD | `-49.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,940,000.00 USD | 0.00 USD | 573.40 USD | `-48.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,940,000.00 USD | 0.00 USD | 244.31 USD | `-47.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,940,000.00 USD | 0.00 USD | 29,530.00 USD | `-47.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 3,910,000.00 USD | 0.00 USD | 503.55 USD | `-46.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 3,910,000.00 USD | 0.00 USD | 480.19 USD | `-45.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,910,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,900,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 3,890,000.00 USD | 0.00 USD | 228.80 USD | `-43.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 3,890,000.00 USD | 0.00 USD | 536.50 USD | `-42.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,890,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,890,000.00 USD | 0.00 USD | 2,880.00 USD | `-39.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,890,000.00 USD | 0.00 USD | 25,490.00 USD | `-36.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 3,860,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-34.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,550,000.00 USD | 0.00 USD | 1,260.00 USD | `-32.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,550,000.00 USD | 0.00 USD | 690.38 USD | `-30.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,550,000.00 USD | 0.00 USD | 1,400.00 USD | `-29.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,550,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,550,000.00 USD | 0.00 USD | 838.94 USD | `-28.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,550,000.00 USD | 0.00 USD | 338.55 USD | `-27.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,550,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,540,000.00 USD | 0.00 USD | 1,850.00 USD | `-25.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,540,000.00 USD | 0.00 USD | 112.46 USD | `-24.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,540,000.00 USD | 0.00 USD | 1,730.00 USD | `-24.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,540,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,540,000.00 USD | 0.00 USD | 6,300.00 USD | `-22.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,530,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,530,000.00 USD | 0.00 USD | 902.47 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,530,000.00 USD | 0.00 USD | 45,660.00 USD | `-20.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,480,000.00 USD | 0.00 USD | 4,760.00 USD | `-19.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,470,000.00 USD | 0.00 USD | 1,840.00 USD | `-18.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,470,000.00 USD | 0.00 USD | 48,180.00 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,420,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,420,000.00 USD | 0.00 USD | 23,530.00 USD | `-16.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,400,000.00 USD | 0.00 USD | 3,960.00 USD | `-15.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,400,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,350,000.00 USD | 0.00 USD | 3,360.00 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,340,000.00 USD | 0.00 USD | 16,830.00 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,330,000.00 USD | 0.00 USD | 12,830.00 USD | `-12.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,310,000.00 USD | 0.00 USD | 9,410.00 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,300,000.00 USD | 0.00 USD | 77,260.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,230,000.00 USD | 0.00 USD | 13,380.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,210,000.00 USD | 0.00 USD | 123,390.00 USD | `-8.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,090,000.00 USD | 0.00 USD | 58,820.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,030,000.00 USD | 0.00 USD | 17,890.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,010,000.00 USD | 0.00 USD | 92,150.00 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 921,500.00 USD | 0.00 USD | 250,600.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 670,900.00 USD | 0.00 USD | 201,790.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 469,110.00 USD | 0.00 USD | 138,890.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 330,220.00 USD | 0.00 USD | 27,970.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 302,260.00 USD | 0.00 USD | 111,110.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 191,140.00 USD | 0.00 USD | 56,300.00 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 134,850.00 USD | 0.00 USD | 119,660.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 15,190.00 USD | 0.00 USD | 15,190.00 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 1,660.00 USD | 1,660.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 91,510.00 USD | 89,850.00 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 392,860.00 USD | 301,350.00 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 437,160.00 USD | 44,300.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 456,770.00 USD | 19,610.00 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,070,000.00 USD | 611,340.00 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,190,000.00 USD | 123,090.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,240,000.00 USD | 43,890.00 USD | 0.00 USD | `+6.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,300,000.00 USD | 67,570.00 USD | 0.00 USD | `+6.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,320,000.00 USD | 14,640.00 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,570,000.00 USD | 249,090.00 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,650,000.00 USD | 81,760.00 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,700,000.00 USD | 55,590.00 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,710,000.00 USD | 5,430.00 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,110,000.00 USD | 4,400,000.00 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,120,000.00 USD | 3,230.00 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,120,000.00 USD | 6,460.00 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,120,000.00 USD | 1,450.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,370,000.00 USD | 242,580.00 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,370,000.00 USD | 7,510.00 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,400,000.00 USD | 21,430.00 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,500,000.00 USD | 108,020.00 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,520,000.00 USD | 14,870.00 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,540,000.00 USD | 17,790.00 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,600,000.00 USD | 66,840.00 USD | 0.00 USD | `+19.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,610,000.00 USD | 11,760.00 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,630,000.00 USD | 19,430.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,680,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,690,000.00 USD | 12,200.00 USD | 0.00 USD | `+22.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,690,000.00 USD | 2,380.00 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,700,000.00 USD | 7,160.00 USD | 0.00 USD | `+24.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,710,000.00 USD | 5,570.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,720,000.00 USD | 10,570.00 USD | 0.00 USD | `+26.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,860,000.00 USD | 139,120.00 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,860,000.00 USD | 1,840.00 USD | 0.00 USD | `+27.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,940,000.00 USD | 80,330.00 USD | 0.00 USD | `+28.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,940,000.00 USD | 464.75 USD | 0.00 USD | `+29.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,120,000.00 USD | 183,340.00 USD | 0.00 USD | `+29.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,130,000.00 USD | 2,670.00 USD | 0.00 USD | `+30.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,210,000.00 USD | 85,010.00 USD | 0.00 USD | `+31.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,220,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,240,000.00 USD | 18,400.00 USD | 0.00 USD | `+33.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,310,000.00 USD | 70,850.00 USD | 0.00 USD | `+33.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,320,000.00 USD | 18,000.00 USD | 0.00 USD | `+34.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,570,000.00 USD | 251,050.00 USD | 0.00 USD | `+35.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,590,000.00 USD | 14,250.00 USD | 0.00 USD | `+36.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,590,000.00 USD | 534.75 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,630,000.00 USD | 43,240.00 USD | 0.00 USD | `+37.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,640,000.00 USD | 3,330.00 USD | 0.00 USD | `+38.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,650,000.00 USD | 9,200.00 USD | 0.00 USD | `+39.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,670,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,790,000.00 USD | 126,830.00 USD | 0.00 USD | `+41.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,890,000.00 USD | 96,600.00 USD | 0.00 USD | `+41.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,890,000.00 USD | 3,980.00 USD | 0.00 USD | `+42.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,890,000.00 USD | 254.51 USD | 0.00 USD | `+43.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,910,000.00 USD | 11,080.00 USD | 0.00 USD | `+44.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,910,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,920,000.00 USD | 8,170.00 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,920,000.00 USD | 843.17 USD | 0.00 USD | `+46.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,930,000.00 USD | 8,390.00 USD | 0.00 USD | `+47.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,930,000.00 USD | 4,420.00 USD | 0.00 USD | `+49.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,930,000.00 USD | 591.89 USD | 0.00 USD | `+49.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,980,000.00 USD | 46,370.00 USD | 0.00 USD | `+50.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,990,000.00 USD | 9,270.00 USD | 0.00 USD | `+51.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,990,000.00 USD | 265.10 USD | 0.00 USD | `+53.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,990,000.00 USD | 2,040.00 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,990,000.00 USD | 807.42 USD | 0.00 USD | `+55.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,010,000.00 USD | 14,120.00 USD | 0.00 USD | `+56.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,010,000.00 USD | 4,010.00 USD | 0.00 USD | `+57.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,010,000.00 USD | 325.54 USD | 0.00 USD | `+57.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,020,000.00 USD | 7,020.00 USD | 0.00 USD | `+58.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,140,000.00 USD | 127,100.00 USD | 0.00 USD | `+59.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,150,000.00 USD | 3,350.00 USD | 0.00 USD | `+60.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,150,000.00 USD | 181.12 USD | 0.00 USD | `+61.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,150,000.00 USD | 382.41 USD | 0.00 USD | `+62.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,150,000.00 USD | 3,420.00 USD | 0.00 USD | `+64.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,150,000.00 USD | 661.93 USD | 0.00 USD | `+64.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,280,000.00 USD | 124,400.00 USD | 0.00 USD | `+66.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,280,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,290,000.00 USD | 13,900.00 USD | 0.00 USD | `+68.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,320,000.00 USD | 24,840.00 USD | 0.00 USD | `+70.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,370,000.00 USD | 50,580.00 USD | 0.00 USD | `+71.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,370,000.00 USD | 2,690.00 USD | 0.00 USD | `+72.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,370,000.00 USD | 2,180.00 USD | 0.00 USD | `+74.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,520,000.00 USD | 151,380.00 USD | 0.00 USD | `+76.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,530,000.00 USD | 2,230.00 USD | 0.00 USD | `+80.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,530,000.00 USD | 1,140.00 USD | 0.00 USD | `+81.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,540,000.00 USD | 11,670.00 USD | 0.00 USD | `+82.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,540,000.00 USD | 370.40 USD | 0.00 USD | `+84.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,540,000.00 USD | 733.19 USD | 0.00 USD | `+85.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,540,000.00 USD | 2,410.00 USD | 0.00 USD | `+88.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,540,000.00 USD | 475.00 USD | 0.00 USD | `+88.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,540,000.00 USD | 1,190.00 USD | 0.00 USD | `+89.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,550,000.00 USD | 2,540.00 USD | 0.00 USD | `+90.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,550,000.00 USD | 1,590.00 USD | 0.00 USD | `+91.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,550,000.00 USD | 1,370.00 USD | 0.00 USD | `+91.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,570,000.00 USD | 19,590.00 USD | 0.00 USD | `+92.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,570,000.00 USD | 564.92 USD | 0.00 USD | `+93.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,570,000.00 USD | 3,420.00 USD | 0.00 USD | `+97.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,570,000.00 USD | 124.75 USD | 0.00 USD | `+98.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,600,000.00 USD | 29,920.00 USD | 0.00 USD | `+99.14%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 103,680,000.00 USD | 0.00 USD | 103,680,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `1.09` | 103,680,000.00 USD | 0.00 USD | 103,680,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 103,640,000.00 USD | 0.00 USD | 103,640,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 103,540,000.00 USD | 0.00 USD | 103,540,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 103,500,000.00 USD | 0.00 USD | 103,500,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 103,500,000.00 USD | 0.00 USD | 103,500,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 103,210,000.00 USD | 0.00 USD | 103,210,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 103,210,000.00 USD | 0.00 USD | 103,210,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 103,200,000.00 USD | 0.00 USD | 103,200,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 103,200,000.00 USD | 0.00 USD | 103,200,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.12` | 103,150,000.00 USD | 0.00 USD | 103,150,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `7D` | `1.12` | 103,130,000.00 USD | 0.00 USD | 103,130,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `7D` | `1.12` | 103,060,000.00 USD | 0.00 USD | 103,060,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `1.12` | 93,970,000.00 USD | 0.00 USD | 93,970,000.00 USD | 21,900.00 USD | 45,520.00 USD | 161,640.00 USD |
| `7D` | `1.12` | 103,030,000.00 USD | 0.00 USD | 103,030,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 93,740,000.00 USD | 0.00 USD | 93,740,000.00 USD | 126,800.00 USD | 70,270.00 USD | 204,850.00 USD |
| `7D` | `1.13` | 102,820,000.00 USD | 0.00 USD | 102,820,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD |
| `1D` | `1.13` | 93,340,000.00 USD | 0.00 USD | 93,340,000.00 USD | 74,360.00 USD | 54,840.00 USD | 167,980.00 USD |
| `7D` | `1.13` | 102,680,000.00 USD | 0.00 USD | 102,680,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 93,040,000.00 USD | 0.00 USD | 93,040,000.00 USD | 7,580.00 USD | 114,120.00 USD | 275,410.00 USD |
| `7D` | `1.13` | 102,480,000.00 USD | 0.00 USD | 102,480,000.00 USD | 5,450.00 USD | 55,710.00 USD | 0.00 USD |
| `1D` | `1.13` | 92,640,000.00 USD | 0.00 USD | 92,640,000.00 USD | 5,520.00 USD | 70,330.00 USD | 275,380.00 USD |
| `7D` | `1.13` | 102,420,000.00 USD | 0.00 USD | 102,420,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD |
| `1D` | `1.13` | 92,290,000.00 USD | 0.00 USD | 92,290,000.00 USD | 91,470.00 USD | 89,100.00 USD | 115,470.00 USD |
| `7D` | `1.13` | 102,050,000.00 USD | 0.00 USD | 102,050,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 92,000,000.00 USD | 0.00 USD | 92,000,000.00 USD | 42,870.00 USD | 153,630.00 USD | 163,320.00 USD |
| `7D` | `1.14` | 101,560,000.00 USD | 0.00 USD | 101,560,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD |
| `1D` | `1.14` | 91,640,000.00 USD | 0.00 USD | 91,640,000.00 USD | 38,180.00 USD | 18,650.00 USD | 49,660.00 USD |
| `7D` | `1.14` | 101,030,000.00 USD | 0.00 USD | 101,030,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 91,530,000.00 USD | 0.00 USD | 91,530,000.00 USD | 34,800.00 USD | 43,480.00 USD | 258,540.00 USD |
| `7D` | `1.14` | 101,000,000.00 USD | 0.00 USD | 101,000,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD |
| `1D` | `1.14` | 91,190,000.00 USD | 0.00 USD | 91,190,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 100,650,000.00 USD | 0.00 USD | 100,650,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 91,120,000.00 USD | 0.00 USD | 91,120,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.14` | 100,510,000.00 USD | 0.00 USD | 100,510,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.15` | 100,500,000.00 USD | 0.00 USD | 100,500,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `1D` | `1.15` | 90,990,000.00 USD | 0.00 USD | 90,990,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 100,440,000.00 USD | 0.00 USD | 100,440,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `7D` | `1.15` | 100,070,000.00 USD | 0.00 USD | 100,070,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 90,970,000.00 USD | 0.00 USD | 90,970,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 99,920,000.00 USD | 0.00 USD | 99,920,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 90,910,000.00 USD | 0.00 USD | 90,910,000.00 USD | 73,200.00 USD | 45,600.00 USD | 263,680.00 USD |
| `7D` | `1.15` | 99,750,000.00 USD | 0.00 USD | 99,750,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 90,520,000.00 USD | 0.00 USD | 90,520,000.00 USD | 20,480.00 USD | 25,050.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 98,870,000.00 USD | 0.00 USD | 98,870,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 90,400,000.00 USD | 0.00 USD | 90,400,000.00 USD | 122,170.00 USD | 20,880.00 USD | 380,500.00 USD |
| `7D` | `1.16` | 98,640,000.00 USD | 0.00 USD | 98,640,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 89,870,000.00 USD | 0.00 USD | 89,870,000.00 USD | 185,400.00 USD | 56,140.00 USD | 142,470.00 USD |
| `7D` | `1.16` | 97,770,000.00 USD | 0.00 USD | 97,770,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 89,490,000.00 USD | 0.00 USD | 89,490,000.00 USD | 172,080.00 USD | 254,990.00 USD | 113,360.00 USD |
| `7D` | `1.16` | 96,690,000.00 USD | 0.00 USD | 96,690,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 88,950,000.00 USD | 0.00 USD | 88,950,000.00 USD | 95,580.00 USD | 61,900.00 USD | 642,980.00 USD |
| `7D` | `1.16` | 95,390,000.00 USD | 0.00 USD | 95,390,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 88,150,000.00 USD | 0.00 USD | 88,150,000.00 USD | 62,000.00 USD | 12,130.00 USD | 106,000.00 USD |
| `7D` | `1.17` | 93,720,000.00 USD | 0.00 USD | 93,720,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 87,970,000.00 USD | 0.00 USD | 87,970,000.00 USD | 104,050.00 USD | 166,040.00 USD | 170,840.00 USD |
| `7D` | `1.17` | 92,380,000.00 USD | 0.00 USD | 92,380,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 87,530,000.00 USD | 0.00 USD | 87,530,000.00 USD | 152,210.00 USD | 22,380.00 USD | 358,690.00 USD |
| `7D` | `1.17` | 91,310,000.00 USD | 0.00 USD | 91,310,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 86,990,000.00 USD | 0.00 USD | 86,990,000.00 USD | 371,850.00 USD | 5,850.00 USD | 266,890.00 USD |
| `7D` | `1.17` | 89,270,000.00 USD | 0.00 USD | 89,270,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 86,350,000.00 USD | 0.00 USD | 86,350,000.00 USD | 124,360.00 USD | 130,370.00 USD | 474,190.00 USD |
| `7D` | `1.17` | 88,070,000.00 USD | 0.00 USD | 88,070,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 85,620,000.00 USD | 0.00 USD | 85,620,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD |
| `7D` | `1.18` | 86,500,000.00 USD | 0.00 USD | 86,500,000.00 USD | 181,850.00 USD | 71,240.00 USD | 372,750.00 USD |
| `1D` | `1.18` | 84,870,000.00 USD | 0.00 USD | 84,870,000.00 USD | 71,040.00 USD | 84,480.00 USD | 175,590.00 USD |
| `7D` | `1.18` | 85,880,000.00 USD | 0.00 USD | 85,880,000.00 USD | 85,020.00 USD | 27,270.00 USD | 483,980.00 USD |
| `1D` | `1.18` | 84,540,000.00 USD | 0.00 USD | 84,540,000.00 USD | 113,290.00 USD | 10,150.00 USD | 24,100.00 USD |
| `7D` | `1.18` | 85,280,000.00 USD | 0.00 USD | 85,280,000.00 USD | 267,580.00 USD | 112,520.00 USD | 194,450.00 USD |
| `1D` | `1.18` | 84,390,000.00 USD | 0.00 USD | 84,390,000.00 USD | 222,930.00 USD | 10,160.00 USD | 666,440.00 USD |
| `7D` | `1.18` | 84,710,000.00 USD | 0.00 USD | 84,710,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 83,500,000.00 USD | 0.00 USD | 83,500,000.00 USD | 196,910.00 USD | 73,630.00 USD | 143,880.00 USD |
| `7D` | `1.18` | 84,440,000.00 USD | 0.00 USD | 84,440,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 83,080,000.00 USD | 0.00 USD | 83,080,000.00 USD | 86,540.00 USD | 511,780.00 USD | 65,030.00 USD |
| `7D` | `1.19` | 83,340,000.00 USD | 0.00 USD | 83,340,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 82,420,000.00 USD | 0.00 USD | 82,420,000.00 USD | 365,260.00 USD | 93,260.00 USD | 1,570,000.00 USD |
| `7D` | `1.19` | 82,480,000.00 USD | 0.00 USD | 82,480,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD |
| `1D` | `1.19` | 80,390,000.00 USD | 0.00 USD | 80,390,000.00 USD | 110,600.00 USD | 45,410.00 USD | 319,610.00 USD |
| `7D` | `1.19` | 81,700,000.00 USD | 0.00 USD | 81,700,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD |
| `1D` | `1.19` | 79,920,000.00 USD | 0.00 USD | 79,920,000.00 USD | 147,820.00 USD | 199,810.00 USD | 469,390.00 USD |
| `7D` | `1.19` | 80,720,000.00 USD | 0.00 USD | 80,720,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 79,100,000.00 USD | 0.00 USD | 79,100,000.00 USD | 190,850.00 USD | 428,210.00 USD | 1,690,000.00 USD |
| `7D` | `1.19` | 79,360,000.00 USD | 0.00 USD | 79,360,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD |
| `1D` | `1.20` | 76,790,000.00 USD | 0.00 USD | 76,790,000.00 USD | 784,530.00 USD | 121,000.00 USD | 1,220,000.00 USD |
| `7D` | `1.20` | 78,520,000.00 USD | 0.00 USD | 78,520,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD |
| `1D` | `1.20` | 74,660,000.00 USD | 0.00 USD | 74,660,000.00 USD | 273,620.00 USD | 837,160.00 USD | 663,320.00 USD |
| `7D` | `1.20` | 76,940,000.00 USD | 0.00 USD | 76,940,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 72,890,000.00 USD | 0.00 USD | 72,890,000.00 USD | 866,770.00 USD | 471,100.00 USD | 2,580,000.00 USD |
| `7D` | `1.20` | 73,930,000.00 USD | 0.00 USD | 73,930,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD |
| `1D` | `1.20` | 68,980,000.00 USD | 0.00 USD | 68,980,000.00 USD | 215,570.00 USD | 258,510.00 USD | 985,010.00 USD |
| `7D` | `1.20` | 72,470,000.00 USD | 0.00 USD | 72,470,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD |
| `1D` | `1.20` | 67,520,000.00 USD | 0.00 USD | 67,520,000.00 USD | 567,590.00 USD | 566,410.00 USD | 551,700.00 USD |
| `7D` | `1.20` | 71,600,000.00 USD | 0.00 USD | 71,600,000.00 USD | 47,500.00 USD | 723,100.00 USD | 155,510.00 USD |
| `1D` | `1.21` | 65,830,000.00 USD | 0.00 USD | 65,830,000.00 USD | 403,550.00 USD | 553,180.00 USD | 678,540.00 USD |
| `7D` | `1.21` | 70,670,000.00 USD | 0.00 USD | 70,670,000.00 USD | 0.00 USD | 77,080.00 USD | 0.00 USD |
| `1D` | `1.21` | 64,200,000.00 USD | 0.00 USD | 64,200,000.00 USD | 1,700,000.00 USD | 343,110.00 USD | 1,980,000.00 USD |
| `7D` | `1.21` | 70,600,000.00 USD | 0.00 USD | 70,600,000.00 USD | 556,190.00 USD | 0.00 USD | 635,770.00 USD |
| `1D` | `1.21` | 60,170,000.00 USD | 0.00 USD | 60,170,000.00 USD | 668,540.00 USD | 487,120.00 USD | 1,320,000.00 USD |
| `7D` | `1.21` | 69,410,000.00 USD | 0.00 USD | 69,410,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD |
| `1D` | `1.21` | 57,700,000.00 USD | 0.00 USD | 57,700,000.00 USD | 1,520,000.00 USD | 657,210.00 USD | 1,560,000.00 USD |
| `7D` | `1.21` | 65,200,000.00 USD | 0.00 USD | 65,200,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD |
| `1D` | `1.21` | 53,960,000.00 USD | 0.00 USD | 53,960,000.00 USD | 30,610.00 USD | 180,830.00 USD | 1,100,000.00 USD |
| `7D` | `1.21` | 62,950,000.00 USD | 0.00 USD | 62,950,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD |
| `1D` | `1.22` | 52,660,000.00 USD | 0.00 USD | 52,660,000.00 USD | 226,520.00 USD | 196,610.00 USD | 1,170,000.00 USD |
| `7D` | `1.22` | 61,420,000.00 USD | 0.00 USD | 61,420,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD |
| `1D` | `1.22` | 51,060,000.00 USD | 0.00 USD | 51,060,000.00 USD | 143,650.00 USD | 4,200.00 USD | 243,580.00 USD |
| `7D` | `1.22` | 61,010,000.00 USD | 0.00 USD | 61,010,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 50,670,000.00 USD | 0.00 USD | 50,670,000.00 USD | 222,150.00 USD | 97,750.00 USD | 4,090.00 USD |
| `7D` | `1.22` | 60,280,000.00 USD | 0.00 USD | 60,280,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 50,350,000.00 USD | 0.00 USD | 50,350,000.00 USD | 113,990.00 USD | 279,120.00 USD | 446,620.00 USD |
| `7D` | `1.22` | 59,190,000.00 USD | 0.00 USD | 59,190,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD |
| `1D` | `1.22` | 49,510,000.00 USD | 0.00 USD | 49,510,000.00 USD | 256,850.00 USD | 0.00 USD | 2,640,000.00 USD |
| `7D` | `1.22` | 59,020,000.00 USD | 0.00 USD | 59,020,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 46,610,000.00 USD | 0.00 USD | 46,610,000.00 USD | 567,980.00 USD | 786,020.00 USD | 996,900.00 USD |
| `7D` | `1.23` | 58,760,000.00 USD | 0.00 USD | 58,760,000.00 USD | 112,770.00 USD | 802,580.00 USD | 482,570.00 USD |
| `1D` | `1.23` | 44,260,000.00 USD | 0.00 USD | 44,260,000.00 USD | 542,470.00 USD | 753,290.00 USD | 587,330.00 USD |
| `7D` | `1.23` | 57,360,000.00 USD | 0.00 USD | 57,360,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD |
| `1D` | `1.23` | 42,380,000.00 USD | 0.00 USD | 42,380,000.00 USD | 306,680.00 USD | 1,040,000.00 USD | 3,390,000.00 USD |
| `7D` | `1.23` | 56,330,000.00 USD | 0.00 USD | 56,330,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,110,000.00 USD |
| `1D` | `1.23` | 37,640,000.00 USD | 0.00 USD | 37,640,000.00 USD | 1,280,000.00 USD | 1,370,000.00 USD | 4,250,000.00 USD |
| `7D` | `1.23` | 53,870,000.00 USD | 0.00 USD | 53,870,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 30,740,000.00 USD | 0.00 USD | 30,740,000.00 USD | 563,990.00 USD | 1,290,000.00 USD | 1,950,000.00 USD |
| `7D` | `1.23` | 50,180,000.00 USD | 0.00 USD | 50,180,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 4,360,000.00 USD |
| `1D` | `1.24` | 26,930,000.00 USD | 0.00 USD | 26,930,000.00 USD | 324,100.00 USD | 1,140,000.00 USD | 1,550,000.00 USD |
| `7D` | `1.24` | 42,160,000.00 USD | 0.00 USD | 42,160,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD |
| `1D` | `1.24` | 23,930,000.00 USD | 0.00 USD | 23,930,000.00 USD | 1,040,000.00 USD | 677,190.00 USD | 2,080,000.00 USD |
| `7D` | `1.24` | 35,010,000.00 USD | 0.00 USD | 35,010,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 4,430,000.00 USD |
| `1D` | `1.24` | 20,130,000.00 USD | 0.00 USD | 20,130,000.00 USD | 765,930.00 USD | 711,040.00 USD | 2,330,000.00 USD |
| `7D` | `1.24` | 25,590,000.00 USD | 0.00 USD | 25,590,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 1,280,000.00 USD |
| `1D` | `1.24` | 16,320,000.00 USD | 0.00 USD | 16,320,000.00 USD | 505,370.00 USD | 1,090,000.00 USD | 1,500,000.00 USD |
| `7D` | `1.24` | 21,010,000.00 USD | 0.00 USD | 21,010,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 1,080,000.00 USD |
| `1D` | `1.24` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 1,850,000.00 USD | 531,700.00 USD | 3,670,000.00 USD |
| `7D` | `1.24` | 18,280,000.00 USD | 0.00 USD | 18,280,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 1,550,000.00 USD |
| `1D` | `1.25` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 1,260,000.00 USD | 585,560.00 USD | 895,030.00 USD |
| `7D` | `1.25` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 3,260,000.00 USD |
| `1D` | `1.25` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 313,550.00 USD | 1,380,000.00 USD | 2,480,000.00 USD |
| `7D` | `1.25` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 4,170,000.00 USD |
| `1D` | `1.25` | 262,800.00 USD | 0.00 USD | 262,800.00 USD | 0.00 USD | 4,750.00 USD | 0.00 USD |
| `7D` | `1.25` | 712,160.00 USD | 0.00 USD | 712,160.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 258,050.00 USD | 0.00 USD | 258,050.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD |
| `1D` | `1.25` | 254,670.00 USD | 0.00 USD | 254,670.00 USD | 0.00 USD | 4,990.00 USD | 0.00 USD |
| `7D` | `1.25` | 222,480.00 USD | 0.00 USD | 222,480.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 249,690.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 7,650.00 USD | 242,040.00 USD |
| `7D` | `1.26` | 158,820.00 USD | 0.00 USD | 158,820.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD |
| `1D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 24,960.00 USD | 24,960.00 USD | 0.00 USD | 0.00 USD | 24,960.00 USD | 0.00 USD |
| `7D` | `1.26` | 19,840.00 USD | 19,840.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD |
| `7D` | `1.26` | 29,940.00 USD | 29,940.00 USD | 0.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD |
| `1D` | `1.26` | 182,400.00 USD | 182,400.00 USD | 0.00 USD | 0.00 USD | 100,700.00 USD | 56,740.00 USD |
| `7D` | `1.26` | 177,500.00 USD | 177,500.00 USD | 0.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD |
| `1D` | `1.26` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 580,850.00 USD | 445,620.00 USD | 1,560,000.00 USD |
| `7D` | `1.26` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 542,940.00 USD | 1,020,000.00 USD |
| `1D` | `1.27` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 1,130,000.00 USD | 347,010.00 USD | 381,140.00 USD |
| `7D` | `1.27` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 4,260,000.00 USD | 9,150.00 USD | 20,550.00 USD |
| `1D` | `1.27` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 424,040.00 USD | 1,340,000.00 USD | 487,620.00 USD |
| `7D` | `1.27` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 0.00 USD | 1,870,000.00 USD | 3,110,000.00 USD |
| `1D` | `1.27` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 1,080,000.00 USD | 1,440,000.00 USD | 4,670,000.00 USD |
| `7D` | `1.27` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 138,500.00 USD | 2,750,000.00 USD | 1,900,000.00 USD |
| `1D` | `1.27` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,170,000.00 USD | 1,490,000.00 USD |
| `7D` | `1.27` | 25,210,000.00 USD | 25,210,000.00 USD | 0.00 USD | 1,680,000.00 USD | 5,300,000.00 USD | 2,420,000.00 USD |
| `1D` | `1.27` | 26,070,000.00 USD | 26,070,000.00 USD | 0.00 USD | 1,130,000.00 USD | 2,290,000.00 USD | 4,460,000.00 USD |
| `7D` | `1.27` | 42,550,000.00 USD | 42,550,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD |
| `1D` | `1.28` | 33,670,000.00 USD | 33,670,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,090,000.00 USD | 3,860,000.00 USD |
| `7D` | `1.28` | 57,420,000.00 USD | 57,420,000.00 USD | 0.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,640,000.00 USD |
| `1D` | `1.28` | 43,450,000.00 USD | 43,450,000.00 USD | 0.00 USD | 3,740,000.00 USD | 1,540,000.00 USD | 4,490,000.00 USD |
| `7D` | `1.28` | 76,570,000.00 USD | 76,570,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 7,620,000.00 USD |
| `1D` | `1.28` | 48,670,000.00 USD | 48,670,000.00 USD | 0.00 USD | 373,090.00 USD | 1,940,000.00 USD | 2,900,000.00 USD |
| `7D` | `1.28` | 79,670,000.00 USD | 79,670,000.00 USD | 0.00 USD | 0.00 USD | 1,700,000.00 USD | 1,400,000.00 USD |
| `1D` | `1.28` | 52,800,000.00 USD | 52,800,000.00 USD | 0.00 USD | 943,390.00 USD | 371,640.00 USD | 2,820,000.00 USD |
| `7D` | `1.28` | 81,700,000.00 USD | 81,700,000.00 USD | 0.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD |
| `1D` | `1.28` | 55,880,000.00 USD | 55,880,000.00 USD | 0.00 USD | 1,210,000.00 USD | 556,340.00 USD | 1,310,000.00 USD |
| `7D` | `1.28` | 85,950,000.00 USD | 85,950,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD |
| `1D` | `1.29` | 60,180,000.00 USD | 60,180,000.00 USD | 0.00 USD | 818,130.00 USD | 1,150,000.00 USD | 2,340,000.00 USD |
| `7D` | `1.29` | 91,080,000.00 USD | 91,080,000.00 USD | 0.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.29` | 62,020,000.00 USD | 62,020,000.00 USD | 0.00 USD | 787,490.00 USD | 459,210.00 USD | 591,760.00 USD |
| `7D` | `1.29` | 91,800,000.00 USD | 91,800,000.00 USD | 0.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 62,850,000.00 USD | 62,850,000.00 USD | 0.00 USD | 156,280.00 USD | 216,580.00 USD | 456,570.00 USD |
| `7D` | `1.29` | 93,410,000.00 USD | 93,410,000.00 USD | 0.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD |
| `1D` | `1.29` | 66,190,000.00 USD | 66,190,000.00 USD | 0.00 USD | 378,690.00 USD | 236,920.00 USD | 2,720,000.00 USD |
| `7D` | `1.29` | 96,000,000.00 USD | 96,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD |
| `1D` | `1.29` | 70,450,000.00 USD | 70,450,000.00 USD | 0.00 USD | 1,170,000.00 USD | 375,550.00 USD | 2,730,000.00 USD |
| `7D` | `1.29` | 99,650,000.00 USD | 99,650,000.00 USD | 0.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD |
| `1D` | `1.30` | 75,730,000.00 USD | 75,730,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,240,000.00 USD | 2,570,000.00 USD |
| `7D` | `1.30` | 106,940,000.00 USD | 106,940,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD |
| `1D` | `1.30` | 76,880,000.00 USD | 76,880,000.00 USD | 0.00 USD | 473,750.00 USD | 23,070.00 USD | 653,440.00 USD |
| `7D` | `1.30` | 108,890,000.00 USD | 108,890,000.00 USD | 0.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 78,660,000.00 USD | 78,660,000.00 USD | 0.00 USD | 361,100.00 USD | 395,780.00 USD | 1,030,000.00 USD |
| `7D` | `1.30` | 111,260,000.00 USD | 111,260,000.00 USD | 0.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD |
| `1D` | `1.30` | 81,380,000.00 USD | 81,380,000.00 USD | 0.00 USD | 804,300.00 USD | 722,000.00 USD | 1,190,000.00 USD |
| `7D` | `1.30` | 112,290,000.00 USD | 112,290,000.00 USD | 0.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD |
| `1D` | `1.30` | 82,750,000.00 USD | 82,750,000.00 USD | 0.00 USD | 407,960.00 USD | 304,910.00 USD | 660,580.00 USD |
| `7D` | `1.30` | 115,090,000.00 USD | 115,090,000.00 USD | 0.00 USD | 0.00 USD | 2,170,000.00 USD | 635,640.00 USD |
| `1D` | `1.31` | 84,610,000.00 USD | 84,610,000.00 USD | 0.00 USD | 568,970.00 USD | 528,000.00 USD | 760,890.00 USD |
| `7D` | `1.31` | 117,100,000.00 USD | 117,100,000.00 USD | 0.00 USD | 1,770,000.00 USD | 238,140.00 USD | 0.00 USD |
| `1D` | `1.31` | 88,310,000.00 USD | 88,310,000.00 USD | 0.00 USD | 937,850.00 USD | 491,550.00 USD | 2,270,000.00 USD |
| `7D` | `1.31` | 122,520,000.00 USD | 122,520,000.00 USD | 0.00 USD | 1,550,000.00 USD | 821,310.00 USD | 3,040,000.00 USD |
| `1D` | `1.31` | 91,690,000.00 USD | 91,690,000.00 USD | 0.00 USD | 1,290,000.00 USD | 360,440.00 USD | 1,730,000.00 USD |
| `7D` | `1.31` | 125,290,000.00 USD | 125,290,000.00 USD | 0.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD |
| `1D` | `1.31` | 94,400,000.00 USD | 94,400,000.00 USD | 0.00 USD | 928,510.00 USD | 636,000.00 USD | 1,150,000.00 USD |
| `7D` | `1.31` | 130,160,000.00 USD | 130,160,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD |
| `1D` | `1.31` | 95,970,000.00 USD | 95,970,000.00 USD | 0.00 USD | 520,400.00 USD | 158,070.00 USD | 891,380.00 USD |
| `7D` | `1.31` | 131,460,000.00 USD | 131,460,000.00 USD | 0.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.32` | 99,030,000.00 USD | 99,030,000.00 USD | 0.00 USD | 190,130.00 USD | 633,280.00 USD | 2,230,000.00 USD |
| `7D` | `1.32` | 136,170,000.00 USD | 136,170,000.00 USD | 0.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.32` | 105,100,000.00 USD | 105,100,000.00 USD | 0.00 USD | 1,760,000.00 USD | 781,570.00 USD | 3,520,000.00 USD |
| `7D` | `1.32` | 141,270,000.00 USD | 141,270,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD |
| `1D` | `1.32` | 107,470,000.00 USD | 107,470,000.00 USD | 0.00 USD | 1,270,000.00 USD | 214,860.00 USD | 886,810.00 USD |
| `7D` | `1.32` | 143,290,000.00 USD | 143,290,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 110,400,000.00 USD | 110,400,000.00 USD | 0.00 USD | 1,140,000.00 USD | 648,560.00 USD | 1,150,000.00 USD |
| `7D` | `1.32` | 146,650,000.00 USD | 146,650,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 112,180,000.00 USD | 112,180,000.00 USD | 0.00 USD | 867,870.00 USD | 62,710.00 USD | 851,430.00 USD |
| `7D` | `1.32` | 149,430,000.00 USD | 149,430,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.33` | 113,220,000.00 USD | 113,220,000.00 USD | 0.00 USD | 405,790.00 USD | 56,240.00 USD | 578,770.00 USD |
| `7D` | `1.33` | 151,230,000.00 USD | 151,230,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 114,430,000.00 USD | 114,430,000.00 USD | 0.00 USD | 545,530.00 USD | 170,390.00 USD | 494,230.00 USD |
| `7D` | `1.33` | 152,330,000.00 USD | 152,330,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 116,130,000.00 USD | 116,130,000.00 USD | 0.00 USD | 729,070.00 USD | 105,530.00 USD | 862,480.00 USD |
| `7D` | `1.33` | 154,040,000.00 USD | 154,040,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 117,950,000.00 USD | 117,950,000.00 USD | 0.00 USD | 465,720.00 USD | 179,640.00 USD | 1,180,000.00 USD |
| `7D` | `1.33` | 156,510,000.00 USD | 156,510,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 119,810,000.00 USD | 119,810,000.00 USD | 0.00 USD | 783,210.00 USD | 229,580.00 USD | 838,970.00 USD |
| `7D` | `1.33` | 158,540,000.00 USD | 158,540,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.34` | 120,920,000.00 USD | 120,920,000.00 USD | 0.00 USD | 286,040.00 USD | 208,270.00 USD | 616,920.00 USD |
| `7D` | `1.34` | 160,080,000.00 USD | 160,080,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 121,450,000.00 USD | 121,450,000.00 USD | 0.00 USD | 289,820.00 USD | 79,720.00 USD | 164,110.00 USD |
| `7D` | `1.34` | 162,520,000.00 USD | 162,520,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 122,310,000.00 USD | 122,310,000.00 USD | 0.00 USD | 347,480.00 USD | 138,730.00 USD | 373,260.00 USD |
| `7D` | `1.34` | 164,380,000.00 USD | 164,380,000.00 USD | 0.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 123,680,000.00 USD | 123,680,000.00 USD | 0.00 USD | 755,550.00 USD | 209,130.00 USD | 407,740.00 USD |
| `7D` | `1.34` | 169,840,000.00 USD | 169,840,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 125,010,000.00 USD | 125,010,000.00 USD | 0.00 USD | 496,280.00 USD | 327,230.00 USD | 502,590.00 USD |
| `7D` | `1.34` | 176,970,000.00 USD | 176,970,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.35` | 125,640,000.00 USD | 125,640,000.00 USD | 0.00 USD | 221,820.00 USD | 72,280.00 USD | 333,320.00 USD |
| `7D` | `1.35` | 185,220,000.00 USD | 185,220,000.00 USD | 0.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD |
| `1D` | `1.35` | 126,130,000.00 USD | 126,130,000.00 USD | 0.00 USD | 177,760.00 USD | 23,630.00 USD | 287,400.00 USD |
| `7D` | `1.35` | 192,970,000.00 USD | 192,970,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 126,480,000.00 USD | 126,480,000.00 USD | 0.00 USD | 177,170.00 USD | 30,570.00 USD | 146,530.00 USD |
| `7D` | `1.35` | 200,990,000.00 USD | 200,990,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 126,750,000.00 USD | 126,750,000.00 USD | 0.00 USD | 69,740.00 USD | 28,660.00 USD | 174,610.00 USD |
| `7D` | `1.35` | 210,110,000.00 USD | 210,110,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 127,060,000.00 USD | 127,060,000.00 USD | 0.00 USD | 105,080.00 USD | 3,170.00 USD | 194,110.00 USD |
| `7D` | `1.35` | 216,860,000.00 USD | 216,860,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.36` | 127,880,000.00 USD | 127,880,000.00 USD | 0.00 USD | 335,960.00 USD | 65,930.00 USD | 426,530.00 USD |
| `7D` | `1.36` | 223,200,000.00 USD | 223,200,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 128,390,000.00 USD | 128,390,000.00 USD | 0.00 USD | 148,530.00 USD | 42,970.00 USD | 310,320.00 USD |
| `7D` | `1.36` | 225,740,000.00 USD | 225,740,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD |
| `1D` | `1.36` | 128,940,000.00 USD | 128,940,000.00 USD | 0.00 USD | 269,010.00 USD | 49,330.00 USD | 234,460.00 USD |
| `7D` | `1.36` | 228,610,000.00 USD | 228,610,000.00 USD | 0.00 USD | 1,380,000.00 USD | 282,890.00 USD | 1,210,000.00 USD |
| `1D` | `1.36` | 129,470,000.00 USD | 129,470,000.00 USD | 0.00 USD | 143,090.00 USD | 115,680.00 USD | 276,810.00 USD |
| `7D` | `1.36` | 232,150,000.00 USD | 232,150,000.00 USD | 0.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,400,000.00 USD |
| `1D` | `1.36` | 129,570,000.00 USD | 129,570,000.00 USD | 0.00 USD | 78,610.00 USD | 14,730.00 USD | 6,070.00 USD |
| `7D` | `1.36` | 234,880,000.00 USD | 234,880,000.00 USD | 0.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD |
| `1D` | `1.37` | 129,840,000.00 USD | 129,840,000.00 USD | 0.00 USD | 56,040.00 USD | 1,320.00 USD | 206,760.00 USD |
| `7D` | `1.37` | 235,700,000.00 USD | 235,700,000.00 USD | 0.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 130,070,000.00 USD | 130,070,000.00 USD | 0.00 USD | 97,000.00 USD | 109,930.00 USD | 29,680.00 USD |
| `7D` | `1.37` | 236,760,000.00 USD | 236,760,000.00 USD | 0.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 130,080,000.00 USD | 130,080,000.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD | 0.00 USD |
| `7D` | `1.37` | 238,070,000.00 USD | 238,070,000.00 USD | 0.00 USD | 367,350.00 USD | 211,750.00 USD | 733,820.00 USD |
| `1D` | `1.37` | 130,210,000.00 USD | 130,210,000.00 USD | 0.00 USD | 5,340.00 USD | 30,930.00 USD | 88,420.00 USD |
| `7D` | `1.37` | 239,300,000.00 USD | 239,300,000.00 USD | 0.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD |
| `1D` | `1.37` | 130,290,000.00 USD | 130,290,000.00 USD | 0.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD |
| `7D` | `1.37` | 240,970,000.00 USD | 240,970,000.00 USD | 0.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD |
| `1D` | `1.38` | 130,690,000.00 USD | 130,690,000.00 USD | 0.00 USD | 126,800.00 USD | 70,270.00 USD | 204,850.00 USD |
| `7D` | `1.38` | 242,000,000.00 USD | 242,000,000.00 USD | 0.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD |
| `1D` | `1.38` | 130,990,000.00 USD | 130,990,000.00 USD | 0.00 USD | 74,360.00 USD | 54,840.00 USD | 167,980.00 USD |
| `7D` | `1.38` | 243,460,000.00 USD | 243,460,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD |
| `1D` | `1.38` | 131,170,000.00 USD | 131,170,000.00 USD | 0.00 USD | 2,320.00 USD | 47,610.00 USD | 130,700.00 USD |
| `7D` | `1.38` | 245,160,000.00 USD | 245,160,000.00 USD | 0.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 131,380,000.00 USD | 131,380,000.00 USD | 0.00 USD | 5,270.00 USD | 66,500.00 USD | 144,710.00 USD |
| `7D` | `1.38` | 247,020,000.00 USD | 247,020,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD |
| `1D` | `1.38` | 131,740,000.00 USD | 131,740,000.00 USD | 0.00 USD | 5,520.00 USD | 70,330.00 USD | 275,380.00 USD |
| `7D` | `1.38` | 248,000,000.00 USD | 248,000,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD |
| `1D` | `1.39` | 132,030,000.00 USD | 132,030,000.00 USD | 0.00 USD | 91,470.00 USD | 89,100.00 USD | 115,470.00 USD |
| `7D` | `1.39` | 249,120,000.00 USD | 249,120,000.00 USD | 0.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 132,390,000.00 USD | 132,390,000.00 USD | 0.00 USD | 42,870.00 USD | 153,630.00 USD | 163,320.00 USD |
| `7D` | `1.39` | 250,330,000.00 USD | 250,330,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD |
| `1D` | `1.39` | 132,500,000.00 USD | 132,500,000.00 USD | 0.00 USD | 38,180.00 USD | 18,330.00 USD | 49,660.00 USD |
| `7D` | `1.39` | 251,080,000.00 USD | 251,080,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `7D` | `1.39` | 251,610,000.00 USD | 251,610,000.00 USD | 0.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD |
| `7D` | `1.39` | 251,770,000.00 USD | 251,770,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD |
| `7D` | `1.40` | 251,990,000.00 USD | 251,990,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 252,000,000.00 USD | 252,000,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 252,060,000.00 USD | 252,060,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 252,140,000.00 USD | 252,140,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 252,440,000.00 USD | 252,440,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 252,590,000.00 USD | 252,590,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 252,730,000.00 USD | 252,730,000.00 USD | 0.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD |
| `7D` | `1.41` | 253,010,000.00 USD | 253,010,000.00 USD | 0.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.83B` | Total OI Tokens: `2,250,652,910.3 XRP`
  * 1h OI Change: `-0.39%` | 4h OI Change: `-1.34%` | 24h OI Change: `-5.52%`
  * Exchange Breakdown: Binance=`426.38M` | Bybit=`322.20M` | OKX=`96.97M` | Hyperliquid=`199.91M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-51.34K` | Last 24h: `21.94K` | Last 3d: `414.05K` | Last 7d: `1.06M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0087%` | **USDT OKX** | `-0.0155%` |
| **USDT Bybit** | `-0.0234%` | **USDT KuCoin** | `-0.0111%` |
| **USDT MEXC** | `0.0087%` | **USDT BingX** | `0.0086%` |
| **USDT Gate** | `-0.0054%` | **USDT Bitget** | `-0.0059%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-0.0000%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `68.42%` | `31.58%` | `2.17` | 433,200,000.00 USD |
| `15M` | `Binance` | `55.93%` | `44.07%` | `1.27` | 84,880,000.00 USD |
| `15M` | `OKX` | `48.97%` | `51.03%` | `0.96` | 38,860,000.00 USD |
| `15M` | `Bybit` | `50.69%` | `49.31%` | `1.03` | 16,200,000.00 USD |
| `15M` | `KuCoin` | `49.95%` | `50.05%` | `1.00` | 910,820.00 USD |
| `15M` | `Gate` | `48.98%` | `51.02%` | `0.96` | 42,160,000.00 USD |
| `15M` | `Bitget` | `56.05%` | `43.95%` | `1.28` | 7,910,000.00 USD |
| `15M` | `BingX` | `45.32%` | `54.68%` | `0.83` | 2,420,000.00 USD |
| `15M` | `MEXC` | `55.98%` | `44.02%` | `1.27` | 8,110,000.00 USD |
| `15M` | `Bitunix` | `48.33%` | `51.67%` | `0.94` | 7,960,000.00 USD |
| `15M` | `Hyperliquid` | `46.39%` | `53.61%` | `0.87` | 9,780,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.53%` | `53.47%` | `0.87` | 1,930,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `87.51%` | `12.49%` | `7.01` | 202,620,000.00 USD |
| `15M` | `HTX` | `43.16%` | `56.84%` | `0.76` | 3,500,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `43.11%` | `56.89%` | `0.76` | 1,950,000.00 USD |
| `15M` | `Bitfinex` | `51.94%` | `48.06%` | `1.08` | 27,090.00 USD |
| `15M` | `Kraken` | `21.89%` | `78.11%` | `0.28` | 1,190,000.00 USD |
| `15M` | `Aster` | `47.23%` | `52.77%` | `0.90` | 1,040,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.82%` | `55.18%` | `0.81` | 1,770,000.00 USD |
| `15M` | `Whale Positions` | `55.93%` | `44.07%` | `1.27` | 84,880,000.00 USD |
| `15M` | `Global Accounts` | `68.42%` | `31.58%` | `2.17` | 433,200,000.00 USD |
| `1H` | `XRP` | `53.64%` | `46.36%` | `1.16` | 1,350,000,000.00 USD |
| `1H` | `Binance` | `46.92%` | `53.08%` | `0.88` | 373,480,000.00 USD |
| `1H` | `OKX` | `44.7%` | `55.3%` | `0.81` | 226,140,000.00 USD |
| `1H` | `Bybit` | `50.3%` | `49.7%` | `1.01` | 70,650,000.00 USD |
| `1H` | `KuCoin` | `46.98%` | `53.02%` | `0.89` | 4,930,000.00 USD |
| `1H` | `Gate` | `48.85%` | `51.15%` | `0.96` | 187,940,000.00 USD |
| `1H` | `Bitget` | `50.83%` | `49.17%` | `1.03` | 42,220,000.00 USD |
| `1H` | `BingX` | `57.84%` | `42.16%` | `1.37` | 14,230,000.00 USD |
| `1H` | `MEXC` | `45.13%` | `54.87%` | `0.82` | 34,860,000.00 USD |
| `1H` | `Bitunix` | `44.53%` | `55.47%` | `0.80` | 39,730,000.00 USD |
| `1H` | `Hyperliquid` | `63.07%` | `36.93%` | `1.71` | 82,560,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.76%` | `51.24%` | `0.95` | 4,060,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `86.86%` | `13.14%` | `6.61` | 205,540,000.00 USD |
| `1H` | `HTX` | `18.61%` | `81.39%` | `0.23` | 25,510,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `48.85%` | `51.15%` | `0.96` | 12,410,000.00 USD |
| `1H` | `Bitfinex` | `57.01%` | `42.99%` | `1.33` | 828,930.00 USD |
| `1H` | `Kraken` | `40%` | `60%` | `0.67` | 4,610,000.00 USD |
| `1H` | `Aster` | `37.31%` | `62.69%` | `0.60` | 8,090,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.52%` | `48.48%` | `1.06` | 11,940,000.00 USD |
| `1H` | `Whale Positions` | `46.92%` | `53.08%` | `0.88` | 373,480,000.00 USD |
| `1H` | `Global Accounts` | `53.64%` | `46.36%` | `1.16` | 1,350,000,000.00 USD |
| `4H` | `XRP` | `49.66%` | `50.34%` | `0.99` | 6,340,000,000.00 USD |
| `4H` | `Binance` | `49.45%` | `50.55%` | `0.98` | 2,080,000,000.00 USD |
| `4H` | `OKX` | `48.17%` | `51.83%` | `0.93` | 1,130,000,000.00 USD |
| `4H` | `Bybit` | `44.85%` | `55.15%` | `0.81` | 377,050,000.00 USD |
| `4H` | `KuCoin` | `46.9%` | `53.1%` | `0.88` | 19,920,000.00 USD |
| `4H` | `Gate` | `50.1%` | `49.9%` | `1.00` | 934,400,000.00 USD |
| `4H` | `Bitget` | `47.56%` | `52.44%` | `0.91` | 223,020,000.00 USD |
| `4H` | `BingX` | `46.42%` | `53.58%` | `0.87` | 66,610,000.00 USD |
| `4H` | `MEXC` | `52.37%` | `47.63%` | `1.10` | 248,960,000.00 USD |
| `4H` | `Bitunix` | `49.85%` | `50.15%` | `0.99` | 206,500,000.00 USD |
| `4H` | `Hyperliquid` | `40.89%` | `59.11%` | `0.69` | 260,690,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.44%` | `49.56%` | `1.02` | 36,520,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `63.42%` | `36.58%` | `1.73` | 482,680,000.00 USD |
| `4H` | `HTX` | `45.1%` | `54.9%` | `0.82` | 82,400,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `43.16%` | `56.84%` | `0.76` | 66,720,000.00 USD |
| `4H` | `Bitfinex` | `34.28%` | `65.72%` | `0.52` | 2,010,000.00 USD |
| `4H` | `Kraken` | `45.65%` | `54.35%` | `0.84` | 9,140,000.00 USD |
| `4H` | `Aster` | `48.5%` | `51.5%` | `0.94` | 51,630,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.96%` | `49.04%` | `1.04` | 74,960,000.00 USD |
| `4H` | `Whale Positions` | `49.45%` | `50.55%` | `0.98` | 2,080,000,000.00 USD |
| `4H` | `Global Accounts` | `49.66%` | `50.34%` | `0.99` | 6,340,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,492,630.91 USD | 2,570,238.18 USD | 4,922,392.73 USD | -2,352,154.55 USD | `-31.39%` | `6B / 29S` |
| `0:00 UTC` | `1.26` | `1.25` | `1.26` | `1.26` | `1.25` | 16,486,336.19 USD | 7,622,620.76 USD | 8,863,715.43 USD | -1,241,094.67 USD | `-7.53%` | `10B / 24S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 8,615,974.43 USD | 3,921,066.30 USD | 4,694,908.13 USD | -773,841.83 USD | `-8.98%` | `6B / 4S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 8,443,326.41 USD | 4,197,283.82 USD | 4,246,042.59 USD | -48,758.76 USD | `-0.58%` | `16B / 5S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 7,390,743.66 USD | 4,309,267.00 USD | 3,081,476.65 USD | 1,227,790.35 USD | `+16.61%` | `9B / 4S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,021,258.97 USD | 2,177,548.60 USD | 2,843,710.37 USD | -666,161.77 USD | `-13.27%` | `1B / 5S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 4,481,732.50 USD | 2,318,507.74 USD | 2,163,224.76 USD | 155,282.98 USD | `+3.46%` | `9B / 5S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 12,807,415.42 USD | 6,692,980.18 USD | 6,114,435.24 USD | 578,544.93 USD | `+4.52%` | `12B / 4S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,616,675.33 USD | 3,341,703.26 USD | 4,274,972.07 USD | -933,268.81 USD | `-12.25%` | `11B / 16S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 1,976,733.36 USD | 1,044,909.90 USD | 931,823.46 USD | 113,086.44 USD | `+5.72%` | `3B / 2S` |

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
| `5m` | 36,820.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,600,000.00 USD | -4,780,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -709,360.00 USD | -2,900,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 853,480.00 USD | -3,300,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 893,750.00 USD | -7,440,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 5,240,000.00 USD | -6,130,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 18,100,000.00 USD | 17,680,000.00 USD | **`ACCUMULATION`** |
| `8h` | 23,660,000.00 USD | -8,960,000.00 USD | **`ACCUMULATION`** |
| `12h` | -12,600,000.00 USD | -15,390,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -47,890,000.00 USD | -136,080,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -114,530,000.00 USD | -215,380,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -596,340,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+36.82K` | 15m=`-1.60M` | 1h=`+853.48K` | 24h=`-47.89M`
* Futures Capital Netflows: 5m=`-1.01M` | 15m=`-4.78M` | 1h=`-3.30M` | 24h=`-136.08M`
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
  * Execution Entry: `1.23` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.22` (Risk Distance: `0.0141` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0141` pts)
  * +2.5R Take Profit: `1.23`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
