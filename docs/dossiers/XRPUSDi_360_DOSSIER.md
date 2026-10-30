# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 10:04:32 IST` (`2026-10-30 04:34:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.25`
- **Spread Points**: `4.00` | **Spread BPS**: `32.00 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.25` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.26` | Lower -3.00σ Band: `1.24`
  * Upper +2.51σ Band: `1.26` | Lower -2.51σ Band: `1.24`
  * Upper +2.01σ Band: `1.26` | Lower -2.01σ Band: `1.24`
  * Upper +2.00σ Band: `1.25` | Lower -2.00σ Band: `1.25`
  * Upper +1.28σ Band: `1.25` | Lower -1.28σ Band: `1.25`
  * Upper +1.00σ Band: `1.25` | Lower -1.00σ Band: `1.25`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.25`
  * Institutional Anchors: EMA-144=`1.25` | EMA-200=`1.25` (Slope: `+0.0000`) | EMA-233=`1.25`
- **Range Boundaries**: 24H High=`1.26` | 24H Low=`1.24` | Weekly High=`1.27` | Weekly Low=`1.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.70%`)
  * Point of Control (POC) = `1.24` (Distance: `+0.60%`)
  * Value Area Low (VAL) = `1.22` (Distance: `+2.55%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.25` | Low=`1.25`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.24`
  * Initial Balance (First Hour): IB High=`1.25` | IB Low=`1.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.25` - `1.25`
  * Optimal Trade Entry (OTE 0.705): `1.25`
  * Structural Invalidation Anchor (0.786): `1.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `2,700,121` | 3,377,628.02 USD | -654,743.60 USD | `-19.38%` | -45,721,957.03 USD | `-1.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `1,863,344` | 2,332,093.70 USD | 600,943.36 USD | `+25.77%` | -45,121,013.67 USD | `+0.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `362,964` | 454,855.48 USD | 261,295.85 USD | `+57.45%` | -44,859,717.82 USD | `-0.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.25` | `1.25` | `1.24` | `1.25` | `9,323,963` | 11,613,423.54 USD | 989,110.21 USD | `+8.52%` | -45,639,416.65 USD | `+0.33` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `9,056,603` | 11,339,160.52 USD | -412,212.84 USD | `-3.64%` | -46,051,629.48 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `362,964` | 454,855.48 USD | 261,295.85 USD | `+57.45%` | -45,790,333.63 USD | `+0.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.21` | `1.23` | `1.21` | `1.22` | `41,352,402` | 50,352,977.66 USD | 2,483,683.00 USD | `+4.93%` | -52,136,643.37 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.22` | `1.25` | `1.22` | `1.25` | `36,941,941` | 45,661,386.25 USD | 4,453,356.28 USD | `+9.75%` | -47,683,287.09 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.25` | `1.24` | `1.25` | `18,722,074` | 23,380,539.96 USD | 835,161.95 USD | `+3.57%` | -46,848,125.14 USD | `+0.35` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.25` | `1.24` | `1.25` | `18,722,074` | 23,380,539.96 USD | 835,161.95 USD | `+3.57%` | -44,551,424.45 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | 545,129.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -14,866,665.27 USD | `-1.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.25` | `1.24` | `1.25` | `18,722,074` | 23,380,539.96 USD | 835,161.95 USD | `+3.57%` | -44,551,424.45 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `ASK` | `1.25` | `21932.0000` | 27,524.66 USD | 909,272.13 USD | `6 orders` | `+0.11%` | `-` |
| `ASK` | `1.25` | `54100.0000` | 67,890.09 USD | 881,747.47 USD | `10 orders` | `+0.10%` | `-` |
| `ASK` | `1.25` | `103150.0000` | 129,432.62 USD | 813,857.38 USD | `6 orders` | `+0.09%` | `-` |
| `ASK` | `1.25` | `25757.0000` | 32,317.31 USD | 684,424.76 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `261427.0000` | 327,986.31 USD | 652,107.45 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `99754.0000` | 125,141.39 USD | 324,121.14 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.25` | `59607.0000` | 74,771.02 USD | 198,979.75 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `1.25` | `32539.0000` | 40,813.67 USD | 124,208.73 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `1.25` | `34786.0000` | 43,628.60 USD | 83,395.06 USD | `11 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `17191.0000` | 21,559.23 USD | 39,766.46 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `9976.0000` | 12,509.90 USD | 18,207.22 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `1.25` | `536.0000` | 672.09 USD | 5,697.32 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `1.25` | `3996.0000` | 5,010.18 USD | 5,025.23 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `1.25` | `12.0000` | 15.04 USD | 15.04 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.25` | `0.00%` | `-` |
| `BID` | `1.25` | `66232.0000` | 83,028.44 USD | 83,028.44 USD | `11 orders` | `-0.00%` | `-` |
| `BID` | `1.25` | `18619.0000` | 23,338.92 USD | 106,367.35 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `1.25` | `48142.0000` | 60,341.18 USD | 166,708.53 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `1.25` | `44550.0000` | 55,834.52 USD | 222,543.05 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `1.25` | `77253.0000` | 96,813.46 USD | 319,356.51 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `44230.0000` | 55,424.61 USD | 374,781.12 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `47950.0000` | 60,081.35 USD | 434,862.47 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `1.25` | `255253.0000` | 319,806.48 USD | 754,668.96 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `1.25` | `138389.0000` | 173,373.74 USD | 928,042.69 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `1.25` | `59131.0000` | 74,073.40 USD | 1,002,116.10 USD | `7 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `224557.0000` | 281,280.10 USD | 1,283,396.20 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `11862.0000` | 14,857.15 USD | 1,298,253.35 USD | `3 orders` | `-0.09%` | `-` |
| `BID` | `1.25` | `53825.0000` | 67,410.43 USD | 1,365,663.78 USD | `6 orders` | `-0.10%` | `-` |
| `BID` | `1.25` | `5370.0000` | 6,724.85 USD | 1,372,388.63 USD | `2 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `39516.0000` | 49,481.94 USD | 1,421,870.57 USD | `9 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `63618.0000` | 79,656.10 USD | 1,501,526.67 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `23968.0000` | 30,007.94 USD | 1,531,534.60 USD | `3 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `26128.0000` | 32,709.64 USD | 1,564,244.25 USD | `4 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `40729.0000` | 50,984.56 USD | 1,615,228.81 USD | `4 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `14486.0000` | 18,132.13 USD | 1,633,360.93 USD | `3 orders` | `-0.16%` | `-` |
| `ASK` | `1.26` | `29718.0000` | 37,313.92 USD | 1,664,661.77 USD | `9 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `42247.0000` | 53,041.11 USD | 1,627,347.85 USD | `7 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `69034.0000` | 86,665.28 USD | 1,574,306.74 USD | `3 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `14487.0000` | 18,185.53 USD | 1,487,641.46 USD | `5 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `351767.0000` | 441,537.94 USD | 1,469,455.93 USD | `13 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `94531.0000` | 118,645.86 USD | 1,027,917.99 USD | `8 orders` | `+0.12%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `28` | `0x31b1...1434` | `LONG` | 43,869,859.79 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,290,976.52 USD | `+9.78%` | `10X Cross` |
| `90` | `0x5b5d...c060` | `SHORT` | 20,043,117.13 USD | `15,964,251.00` | `1.44` | `1.26` | `11.36` | 2,872,951.58 USD | `+14.33%` | `5X Cross` |
| `156` | `0xb83d...6e36` | `SHORT` | 13,248,113.63 USD | `10,555,450.00` | `1.50` | `1.26` | `13.85` | 2,574,456.02 USD | `+19.43%` | `5X Cross` |
| `345` | `0x58f0...0d20` | `LONG` | 6,662,592.34 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 59,748.84 USD | `+0.90%` | `20X Cross` |
| `410` | `0xecb6...2b00` | `SHORT` | 5,399,577.22 USD | `4,300,396.00` | `1.27` | `1.26` | `7.65` | 65,632.58 USD | `+1.22%` | `10X Cross` |
| `422` | `0xca49...53c8` | `SHORT` | 5,199,268.59 USD | `4,138,886.00` | `1.44` | `1.26` | `4.83` | 754,054.14 USD | `+14.50%` | `20X Cross` |
| `438` | `0xdd53...2b13` | `SHORT` | 4,988,766.24 USD | `3,973,213.00` | `1.40` | `1.26` | `16.97` | 575,916.71 USD | `+11.54%` | `3X Cross` |
| `503` | `0x610b...b613` | `LONG` | 4,447,652.23 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8146` | -652,340.38 USD | `-14.67%` | `5X Cross` |
| `532` | `0xfc27...9d9d` | `SHORT` | 4,182,324.50 USD | `3,330,937.00` | `1.29` | `1.26` | `6.67` | 125,696.03 USD | `+3.01%` | `20X Cross` |
| `617` | `0x9946...0852` | `SHORT` | 3,656,832.04 USD | `2,912,418.00` | `1.41` | `1.26` | `1.79` | 451,670.53 USD | `+12.35%` | `20X Cross` |
| `667` | `0xc30c...a4c9` | `SHORT` | 3,355,660.35 USD | `2,672,981.00` | `1.42` | `1.26` | `1.59` | 431,303.76 USD | `+12.85%` | `6X Cross` |
| `698` | `0xf48f...10fe` | `LONG` | 3,220,301.53 USD | `2,565,779.00` | `1.53` | `1.26` | `0.9851` | -704,339.20 USD | `-21.87%` | `4X Cross` |
| `734` | `0x023a...2355` | `SHORT` | 3,094,962.34 USD | `2,464,927.00` | `1.32` | `1.26` | `3.35` | 158,033.90 USD | `+5.11%` | `20X Cross` |
| `744` | `0x45d2...4029` | `SHORT` | 3,081,301.61 USD | `2,453,000.00` | `1.48` | `1.26` | `18.39` | 556,978.82 USD | `+18.08%` | `20X Cross` |
| `1079` | `0xeadc...9d55` | `LONG` | 2,028,481.80 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 69,638.78 USD | `+3.43%` | `20X Cross` |
| `1147` | `0x94b2...599e` | `SHORT` | 1,934,343.83 USD | `1,540,696.00` | `1.36` | `1.26` | `1.87` | 166,122.62 USD | `+8.59%` | `20X Cross` |
| `1152` | `0xbcd4...0dd2` | `SHORT` | 1,919,626.50 USD | `1,529,461.00` | `1.31` | `1.26` | `1.91` | 84,918.10 USD | `+4.42%` | `20X Cross` |
| `1172` | `0x3fc5...c0c1` | `SHORT` | 1,897,282.65 USD | `1,511,779.00` | `1.52` | `1.26` | `2.37` | 394,331.96 USD | `+20.78%` | `20X Cross` |
| `1191` | `0x31ef...f715` | `LONG` | 1,851,815.43 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -347,449.97 USD | `-18.76%` | `3X Isolated` |
| `1250` | `0x7737...bf66` | `SHORT` | 1,774,606.56 USD | `1,413,466.00` | `1.41` | `1.26` | `13.51` | 224,262.09 USD | `+12.64%` | `10X Cross` |
| `1308` | `0x95da...2328` | `LONG` | 1,663,249.33 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0949` | -130,391.77 USD | `-7.84%` | `5X Cross` |
| `1330` | `0xee2b...d67e` | `LONG` | 1,639,647.68 USD | `1,306,284.00` | `1.55` | `1.26` | `0.4065` | -391,007.22 USD | `-23.85%` | `4X Cross` |
| `1378` | `0x215d...f80a` | `LONG` | 1,571,606.02 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -82,848.20 USD | `-5.27%` | `14X Cross` |
| `1407` | `0x5fa3...35b7` | `SHORT` | 1,558,009.53 USD | `1,240,651.00` | `1.30` | `1.26` | `2.65` | 58,482.61 USD | `+3.75%` | `20X Cross` |
| `1441` | `0x123d...3bff` | `LONG` | 1,525,967.09 USD | `1,215,329.00` | `1.35` | `1.26` | `0.000000` | -111,102.13 USD | `-7.28%` | `10X Cross` |
| `1493` | `0xdf95...7d72` | `SHORT` | 1,457,158.96 USD | `1,160,528.00` | `1.37` | `1.26` | `34.51` | 136,316.18 USD | `+9.35%` | `20X Cross` |
| `1574` | `0xc179...e0c8` | `SHORT` | 1,374,922.18 USD | `1,095,032.00` | `1.29` | `1.26` | `7.20` | 42,597.11 USD | `+3.10%` | `10X Cross` |
| `1577` | `0xef96...9383` | `SHORT` | 1,372,122.07 USD | `1,092,976.00` | `1.34` | `1.26` | `4.60` | 90,625.37 USD | `+6.60%` | `20X Cross` |
| `1604` | `0x7fda...17d1` | `LONG` | 1,334,690.24 USD | `1,062,990.00` | `1.21` | `1.26` | `0.000000` | 45,400.01 USD | `+3.40%` | `20X Cross` |
| `1654` | `0xb1ce...681b` | `LONG` | 1,283,474.54 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -240,581.95 USD | `-18.74%` | `4X Isolated` |
| `1760` | `0x3c36...461a` | `LONG` | 1,179,586.34 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -39,494.28 USD | `-3.35%` | `10X Cross` |
| `1788` | `0x2577...4897` | `SHORT` | 1,165,377.61 USD | `928,144.00` | `1.24` | `1.26` | `4.77` | -12,625.93 USD | `-1.08%` | `20X Cross` |
| `2016` | `0xbfc7...80b4` | `SHORT` | 1,004,480.00 USD | `800,000.00` | `1.48` | `1.26` | `3.25` | 178,974.65 USD | `+17.82%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.51` | 14,176.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 14.18K USD at 1.5122 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 13,327.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 13.33K USD at 1.5123 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,998.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5123 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 1,649.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.65K USD at 1.5123 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 8,805.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.81K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,998.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 33,324.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 33.32K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 48,283.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 48.28K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 2,614.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.61K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 12,590.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.59K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 12.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.5125 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,109.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.11K USD at 1.5125 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 1,650.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.65K USD at 1.5126 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 202.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.20K USD at 1.5126 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 4,999.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.5127 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 6,478.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.48K USD at 1.5127 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 12,067.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.07K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 399.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 7,568.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.57K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 2,281.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.28K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,998.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 1,651.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.65K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 4,999.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.5137 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 8,255.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.26K USD at 1.5137 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,381.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.38K USD at 1.3270 USD [API] | `2026-10-28 23:22:54` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 237.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.24K USD at 1.3420 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 193.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.19K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,752.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.75K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,552.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.55K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 505.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.51K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,996.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.00K USD at 1.3423 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 36,396.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 36.40K USD at 1.3424 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 400.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3424 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 53.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3424 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 166.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3425 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,037.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.04K USD at 1.3425 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,753.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.75K USD at 1.3425 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,152.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.15K USD at 1.3426 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,754.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.75K USD at 1.3426 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 13,568.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 13.57K USD at 1.3428 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,499.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.50K USD at 1.3428 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,154.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.15K USD at 1.3429 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,130.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.13K USD at 1.3431 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,162.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.16K USD at 1.3431 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,871.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.87K USD at 1.3431 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,003.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3432 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,002.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3434 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,009.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.01K USD at 1.3435 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 17,373.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 17.37K USD at 1.3250 USD [API] | `2026-10-28 23:50:00` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 19,875.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 19.88K USD at 1.3250 USD [API] | `2026-10-28 23:51:12` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,800.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.80K USD at 1.3240 USD [API] | `2026-10-29 00:10:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,944.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.94K USD at 1.3240 USD [API] | `2026-10-29 00:10:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,012.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.01K USD at 1.3240 USD [API] | `2026-10-29 00:10:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 32,462.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 32.46K USD at 1.3245 USD [API] | `2026-10-29 00:10:43` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,833.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.83K USD at 1.3245 USD [API] | `2026-10-29 00:10:43` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3245 USD [API] | `2026-10-29 00:10:43` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,673.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.67K USD at 1.3244 USD [API] | `2026-10-29 00:16:28` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,591.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.59K USD at 1.3230 USD [API] | `2026-10-29 00:21:23` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 30,298.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 30.30K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 31,405.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 31.41K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 25,590.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 25.59K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,410.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.41K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,194.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.19K USD at 1.3235 USD [API] | `2026-10-29 00:30:53` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3234 USD [API] | `2026-10-29 00:43:09` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 29,859.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 29.86K USD at 1.3222 USD [API] | `2026-10-29 00:50:57` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,000.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.00K USD at 1.3220 USD [API] | `2026-10-29 00:53:55` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,975.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.98K USD at 1.3181 USD [API] | `2026-10-29 01:15:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,269.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.27K USD at 1.3186 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3187 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3187 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 33,334.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 33.33K USD at 1.3187 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,344.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.34K USD at 1.3176 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,493.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.49K USD at 1.3176 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 24,542.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 24.54K USD at 1.3175 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,114.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.11K USD at 1.3175 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 40,493.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 40.49K USD at 1.3101 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3102 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,861.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.86K USD at 1.3102 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,125.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.13K USD at 1.3102 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,491.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.49K USD at 1.3101 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 39,284.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 39.28K USD at 1.3101 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 8,058.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.06K USD at 1.3101 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 13,338.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.34K USD at 1.3100 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,710.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.71K USD at 1.3078 USD [API] | `2026-10-29 01:42:24` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,813.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.81K USD at 1.3084 USD [API] | `2026-10-29 01:42:21` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3097 USD [API] | `2026-10-29 01:44:12` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,108.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.11K USD at 1.2850 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,999.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,087.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.09K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,535.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.54K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 105.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.11K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 889.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.89K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,446.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.45K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,856.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.86K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,427.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.43K USD at 1.3357 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,509.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.51K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,255.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.26K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,255.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.26K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,975.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.98K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 10,779.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.78K USD at 1.2611 USD [API] | `2026-10-18 19:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,842.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.84K USD at 1.2999 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 399.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,500.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.50K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 130.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.13K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,872.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.87K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 13.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 499.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 35.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.04K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 72.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,260.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.26K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,471.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.47K USD at 1.3020 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,971.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.97K USD at 1.3026 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 379.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.38K USD at 1.3026 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,506.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.51K USD at 1.3028 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 16,681.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 16.68K USD at 1.3269 USD [API] | `2026-10-13 00:08:28` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 1,232.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.23K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,292.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.29K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,999.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 49.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 50.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,939.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.94K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 6,587.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.59K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 5,005.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 6,586.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.59K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 2,902.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.90K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 506.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.51K USD at 1.4178 USD [API] | `2026-10-07 17:27:02` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 3,842.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.84K USD at 1.4178 USD [API] | `2026-10-07 17:27:02` |
| `ANNOUNCEMENT` | `INFO` | `1.43` | 12,403.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.40K USD at 1.4323 USD [API] | `2026-10-07 02:01:21` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 15,911.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 15.91K USD at 1.4627 USD [API] | `2026-10-02 18:39:33` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 2,571.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.57K USD at 1.4627 USD [API] | `2026-10-02 18:39:33` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 10,642.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.64K USD at 1.4627 USD [API] | `2026-10-02 18:39:33` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 158.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.16K USD at 1.4800 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 198.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.20K USD at 1.4800 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 10,777.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.78K USD at 1.4800 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 595.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.60K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 399.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 5,001.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 7,943.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.94K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 39,758.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 39.76K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 1,363.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.36K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 284.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.28K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 1,499.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.50K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 85.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 4,860.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.86K USD at 1.4532 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 4,698.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.70K USD at 1.4532 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 7,710.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.71K USD at 1.4946 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 272.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.27K USD at 1.4946 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,216.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.22K USD at 1.4947 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 11,231.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 11.23K USD at 1.4948 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 9,771.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.77K USD at 1.4948 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 1,459.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.46K USD at 1.4949 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,518.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.52K USD at 1.4949 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,217.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.22K USD at 1.4949 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 1,154.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.15K USD at 1.4950 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 400.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.4950 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 879.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.88K USD at 1.4951 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 1,294.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.29K USD at 1.3960 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,999.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3960 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 1,717.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.72K USD at 1.3960 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 418.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.42K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,448.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.45K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 400.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.80%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--3.92%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+6.04%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--3.93%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+8.21%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--3.93%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,000,000.00 USD, Dist: `+7.87%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--3.93%`)
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
| `Live` | `Long Liquidation` | `1.07` | 955,410.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 188,350.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 381,630.00 USD | 13,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 376,130.00 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.11` | 31,160,000.00 USD | 31,160,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 52,480,000.00 USD | 52,480,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 31,140,000.00 USD | 31,140,000.00 USD | 18,710.00 USD | 0.00 USD | 121,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 31,000,000.00 USD | 31,000,000.00 USD | 0.00 USD | 2,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 52,460,000.00 USD | 52,460,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 289,050.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 31,000,000.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 62,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,450,000.00 USD | 52,450,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,940,000.00 USD | 30,940,000.00 USD | 0.00 USD | 47,340.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,880,000.00 USD | 30,880,000.00 USD | 10,140.00 USD | 2,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,370,000.00 USD | 52,370,000.00 USD | 17,190.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,870,000.00 USD | 30,870,000.00 USD | 0.00 USD | 1,530.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,350,000.00 USD | 52,350,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,810,000.00 USD | 30,810,000.00 USD | 66,330.00 USD | 29,190.00 USD | 56,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,350,000.00 USD | 52,350,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,210,000.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,660,000.00 USD | 30,660,000.00 USD | 0.00 USD | 783.15 USD | 104,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,550,000.00 USD | 30,550,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 52,140,000.00 USD | 52,140,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,430,000.00 USD | 30,430,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 51,950,000.00 USD | 51,950,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,200,000.00 USD | 30,200,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 51,930,000.00 USD | 51,930,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 30,140,000.00 USD | 30,140,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,460,000.00 USD | 51,460,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 131,930.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 30,090,000.00 USD | 30,090,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,210,000.00 USD | 51,210,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 30,000,000.00 USD | 30,000,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,110,000.00 USD | 51,110,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 29,980,000.00 USD | 29,980,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,100,000.00 USD | 51,100,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 29,910,000.00 USD | 29,910,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,040,000.00 USD | 51,040,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 29,770,000.00 USD | 29,770,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,920,000.00 USD | 50,920,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 332,060.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,910,000.00 USD | 50,910,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 29,730,000.00 USD | 29,730,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,770,000.00 USD | 50,770,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,410,000.00 USD | 50,410,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 29,720,000.00 USD | 29,720,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,250,000.00 USD | 50,250,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 29,520,000.00 USD | 29,520,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 49,870,000.00 USD | 49,870,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 531,180.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 29,180,000.00 USD | 29,180,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 49,220,000.00 USD | 49,220,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 29,110,000.00 USD | 29,110,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 48,420,000.00 USD | 48,420,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 28,790,000.00 USD | 28,790,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 47,900,000.00 USD | 47,900,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 28,170,000.00 USD | 28,170,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 46,870,000.00 USD | 46,870,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 27,550,000.00 USD | 27,550,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 45,500,000.00 USD | 45,500,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,610,000.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 27,340,000.00 USD | 27,340,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 44,870,000.00 USD | 44,870,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 27,030,000.00 USD | 27,030,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 43,490,000.00 USD | 43,490,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 26,860,000.00 USD | 26,860,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 41,990,000.00 USD | 41,990,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 26,690,000.00 USD | 26,690,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 40,600,000.00 USD | 40,600,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 26,440,000.00 USD | 26,440,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 39,800,000.00 USD | 39,800,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 514,860.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 26,100,000.00 USD | 26,100,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 38,920,000.00 USD | 38,920,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 25,970,000.00 USD | 25,970,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 38,460,000.00 USD | 38,460,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 25,790,000.00 USD | 25,790,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 37,750,000.00 USD | 37,750,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 25,750,000.00 USD | 25,750,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 37,370,000.00 USD | 37,370,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 25,640,000.00 USD | 25,640,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 37,240,000.00 USD | 37,240,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 443,330.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 25,520,000.00 USD | 25,520,000.00 USD | 16,710.00 USD | 139,070.00 USD | 324,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 36,730,000.00 USD | 36,730,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 25,040,000.00 USD | 25,040,000.00 USD | 239,430.00 USD | 8,930.00 USD | 410,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 35,960,000.00 USD | 35,960,000.00 USD | 182,110.00 USD | 132,500.00 USD | 276,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 24,380,000.00 USD | 24,380,000.00 USD | 48,220.00 USD | 10,480.00 USD | 205,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 35,370,000.00 USD | 35,370,000.00 USD | 152,830.00 USD | 265,920.00 USD | 471,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 24,110,000.00 USD | 24,110,000.00 USD | 25,890.00 USD | 217,630.00 USD | 79,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 34,480,000.00 USD | 34,480,000.00 USD | 218,910.00 USD | 106,640.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,790,000.00 USD | 23,790,000.00 USD | 15,240.00 USD | 40,110.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 33,820,000.00 USD | 33,820,000.00 USD | 381,050.00 USD | 81,170.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 742,780.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,690,000.00 USD | 23,690,000.00 USD | 21,190.00 USD | 3,620.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 33,060,000.00 USD | 33,060,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,660,000.00 USD | 23,660,000.00 USD | 66,960.00 USD | 22,280.00 USD | 291,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 32,770,000.00 USD | 32,770,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,280,000.00 USD | 23,280,000.00 USD | 169,810.00 USD | 250,260.00 USD | 180,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 31,800,000.00 USD | 31,800,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 22,680,000.00 USD | 22,680,000.00 USD | 102,120.00 USD | 4,970.00 USD | 260,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 31,320,000.00 USD | 31,320,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 22,310,000.00 USD | 22,310,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 30,440,000.00 USD | 30,440,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 4,610.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 21,810,000.00 USD | 21,810,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 30,340,000.00 USD | 30,340,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 21,280,000.00 USD | 21,280,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 30,240,000.00 USD | 30,240,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 20,980,000.00 USD | 20,980,000.00 USD | 99,310.00 USD | 425,250.00 USD | 731,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 28,690,000.00 USD | 28,690,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 19,720,000.00 USD | 19,720,000.00 USD | 419,060.00 USD | 162,630.00 USD | 699,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 27,450,000.00 USD | 27,450,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 18,440,000.00 USD | 18,440,000.00 USD | 166,960.00 USD | 8,790.00 USD | 102,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 27,040,000.00 USD | 27,040,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 18,160,000.00 USD | 18,160,000.00 USD | 118,950.00 USD | 5,680.00 USD | 470,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 26,870,000.00 USD | 26,870,000.00 USD | 157,620.00 USD | 396,140.00 USD | 396,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 17,570,000.00 USD | 17,570,000.00 USD | 285,170.00 USD | 423,840.00 USD | 178,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 25,920,000.00 USD | 25,920,000.00 USD | 256,390.00 USD | 8,330.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 16,680,000.00 USD | 16,680,000.00 USD | 54,610.00 USD | 42,060.00 USD | 228,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 25,610,000.00 USD | 25,610,000.00 USD | 245,120.00 USD | 10,480.00 USD | 328,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 16,360,000.00 USD | 16,360,000.00 USD | 141,030.00 USD | 525,900.00 USD | 394,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 25,030,000.00 USD | 25,030,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 15,290,000.00 USD | 15,290,000.00 USD | 828,850.00 USD | 352,590.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 23,780,000.00 USD | 23,780,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 433.65 USD | 433.65 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 11,360,000.00 USD | 11,360,000.00 USD | 344,500.00 USD | 161,310.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 20,890,000.00 USD | 20,890,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 9,820,000.00 USD | 9,820,000.00 USD | 105,710.00 USD | 213,020.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 8,420,000.00 USD | 8,420,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 17,540,000.00 USD | 17,540,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 6,930,000.00 USD | 6,930,000.00 USD | 281,800.00 USD | 336,650.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 16,260,000.00 USD | 16,260,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 5,290,000.00 USD | 5,290,000.00 USD | 433,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 14,510,000.00 USD | 14,510,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 4,850,000.00 USD | 4,850,000.00 USD | 267,830.00 USD | 542,950.00 USD | 739,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 12,450,000.00 USD | 12,450,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 3,300,000.00 USD | 3,300,000.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 6,500,000.00 USD | 6,500,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 3,100,000.00 USD | 3,100,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 1,640,000.00 USD | 1,640,000.00 USD | 305,740.00 USD | 774,420.00 USD | 560,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 896,470.00 USD | 896,470.00 USD | 896,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 3,330,000.00 USD | 3,330,000.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 6,650,000.00 USD | 6,650,000.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 4,250,000.00 USD | 4,250,000.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 8,510,000.00 USD | 8,510,000.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 7,760,000.00 USD | 7,760,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 10,740,000.00 USD | 10,740,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 10,880,000.00 USD | 10,880,000.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 8,350,000.00 USD | 8,350,000.00 USD | 202,510.00 USD | 0.00 USD | 392,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 11,060,000.00 USD | 11,060,000.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 532,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 12,000,000.00 USD | 12,000,000.00 USD | 74,170.00 USD | 0.00 USD | 860,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 9,680,000.00 USD | 9,680,000.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 12,190,000.00 USD | 12,190,000.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 9,740.00 USD | 9,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.26` | 10,820,000.00 USD | 10,820,000.00 USD | 803,540.00 USD | 140,210.00 USD | 193,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 10,910,000.00 USD | 10,910,000.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 12,290,000.00 USD | 12,290,000.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 12,990,000.00 USD | 12,990,000.00 USD | 331,210.00 USD | 66,520.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 16,360,000.00 USD | 16,360,000.00 USD | 1,050,000.00 USD | 696,320.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 18,800,000.00 USD | 18,800,000.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 20,010,000.00 USD | 20,010,000.00 USD | 367,910.00 USD | 759,740.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 25,740,000.00 USD | 25,740,000.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 120,440.00 USD | 130,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 22,260,000.00 USD | 22,260,000.00 USD | 39,860.00 USD | 1,080,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 39,370,000.00 USD | 39,370,000.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 24,360,000.00 USD | 24,360,000.00 USD | 23,990.00 USD | 2,070,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 44,140,000.00 USD | 44,140,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 27,350,000.00 USD | 27,350,000.00 USD | 369,350.00 USD | 841,430.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 47,780,000.00 USD | 47,780,000.00 USD | 1,030,000.00 USD | 2,480,000.00 USD | 123,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 30,230,000.00 USD | 30,230,000.00 USD | 1,860,000.00 USD | 348,710.00 USD | 676,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 52,550,000.00 USD | 52,550,000.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 36,770,000.00 USD | 36,770,000.00 USD | 778,390.00 USD | 2,410,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 68,980,000.00 USD | 68,980,000.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 10,160.00 USD | 140,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 47,340,000.00 USD | 47,340,000.00 USD | 3,100,000.00 USD | 2,940,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 87,260,000.00 USD | 87,260,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 55,070,000.00 USD | 55,070,000.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 93,550,000.00 USD | 93,550,000.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 56,400,000.00 USD | 56,400,000.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 94,510,000.00 USD | 94,510,000.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 59,260,000.00 USD | 59,260,000.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 96,510,000.00 USD | 96,510,000.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 61,290,000.00 USD | 61,290,000.00 USD | 421,680.00 USD | 611,360.00 USD | 993,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 100,110,000.00 USD | 100,110,000.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,390.00 USD | 142,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 63,200,000.00 USD | 63,200,000.00 USD | 726,790.00 USD | 768,570.00 USD | 419,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 101,270,000.00 USD | 101,270,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 63,520,000.00 USD | 63,520,000.00 USD | 210,950.00 USD | 8,830.00 USD | 99,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 101,390,000.00 USD | 101,390,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 63,830,000.00 USD | 63,830,000.00 USD | 151,350.00 USD | 0.00 USD | 157,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 103,670,000.00 USD | 103,670,000.00 USD | 1,060,000.00 USD | 198,070.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 66,720,000.00 USD | 66,720,000.00 USD | 546,160.00 USD | 195,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 104,100,000.00 USD | 104,100,000.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 72,670,000.00 USD | 72,670,000.00 USD | 1,810,000.00 USD | 645,070.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 113,780,000.00 USD | 113,780,000.00 USD | 3,400,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 692.82 USD | 143,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 74,920,000.00 USD | 74,920,000.00 USD | 518,910.00 USD | 633,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 115,010,000.00 USD | 115,010,000.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 75,640,000.00 USD | 75,640,000.00 USD | 321,680.00 USD | 109,620.00 USD | 291,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 117,070,000.00 USD | 117,070,000.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 77,770,000.00 USD | 77,770,000.00 USD | 443,890.00 USD | 332,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 118,740,000.00 USD | 118,740,000.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 79,490,000.00 USD | 79,490,000.00 USD | 587,440.00 USD | 869,380.00 USD | 260,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 80,760,000.00 USD | 80,760,000.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 246.65 USD | 143,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 83,050,000.00 USD | 83,050,000.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 124,840,000.00 USD | 124,840,000.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 86,290,000.00 USD | 86,290,000.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 129,300,000.00 USD | 129,300,000.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 88,610,000.00 USD | 88,610,000.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 132,560,000.00 USD | 132,560,000.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 91,540,000.00 USD | 91,540,000.00 USD | 1,320,000.00 USD | 664,910.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 135,400,000.00 USD | 135,400,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 94,470,000.00 USD | 94,470,000.00 USD | 372,630.00 USD | 454,810.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 137,860,000.00 USD | 137,860,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,980,000.00 USD | 100,980,000.00 USD | 1,320,000.00 USD | 1,640,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,480,000.00 USD | 142,480,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 106,060,000.00 USD | 106,060,000.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 145,560,000.00 USD | 145,560,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 109,560,000.00 USD | 109,560,000.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 147,390,000.00 USD | 147,390,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 114,150,000.00 USD | 114,150,000.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 151,850,000.00 USD | 151,850,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 116,150,000.00 USD | 116,150,000.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 154,220,000.00 USD | 154,220,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 56,950.00 USD | 200,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 118,680,000.00 USD | 118,680,000.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 154,760,000.00 USD | 154,760,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 120,920,000.00 USD | 120,920,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 155,910,000.00 USD | 155,910,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 123,770,000.00 USD | 123,770,000.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 157,630,000.00 USD | 157,630,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 126,160,000.00 USD | 126,160,000.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 161,680,000.00 USD | 161,680,000.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 128,240,000.00 USD | 128,240,000.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 162,230,000.00 USD | 162,230,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,430.00 USD | 202,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 130,220,000.00 USD | 130,220,000.00 USD | 829,900.00 USD | 219,260.00 USD | 927,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 164,180,000.00 USD | 164,180,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 132,490,000.00 USD | 132,490,000.00 USD | 1,010,000.00 USD | 331,250.00 USD | 927,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 166,520,000.00 USD | 166,520,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 134,360,000.00 USD | 134,360,000.00 USD | 892,570.00 USD | 387,310.00 USD | 592,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 171,230,000.00 USD | 171,230,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 137,610,000.00 USD | 137,610,000.00 USD | 1,410,000.00 USD | 693,530.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 176,870,000.00 USD | 176,870,000.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 139,380,000.00 USD | 139,380,000.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 187,840,000.00 USD | 187,840,000.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 17,330.00 USD | 219,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 140,420,000.00 USD | 140,420,000.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 194,780,000.00 USD | 194,780,000.00 USD | 2,310,000.00 USD | 2,170,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 141,910,000.00 USD | 141,910,000.00 USD | 749,450.00 USD | 149,380.00 USD | 591,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 205,030,000.00 USD | 205,030,000.00 USD | 4,290,000.00 USD | 1,640,000.00 USD | 4,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 142,940,000.00 USD | 142,940,000.00 USD | 471,590.00 USD | 126,450.00 USD | 425,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 212,740,000.00 USD | 212,740,000.00 USD | 2,580,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 144,360,000.00 USD | 144,360,000.00 USD | 597,310.00 USD | 312,930.00 USD | 511,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 221,000,000.00 USD | 221,000,000.00 USD | 2,620,000.00 USD | 1,160,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 145,150,000.00 USD | 145,150,000.00 USD | 142,180.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 229,230,000.00 USD | 229,230,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 2,700.00 USD | 222,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 146,090,000.00 USD | 146,090,000.00 USD | 391,410.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 233,320,000.00 USD | 233,320,000.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 146,430,000.00 USD | 146,430,000.00 USD | 213,710.00 USD | 42,480.00 USD | 84,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 237,110,000.00 USD | 237,110,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 147,180,000.00 USD | 147,180,000.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 239,240,000.00 USD | 239,240,000.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 147,520,000.00 USD | 147,520,000.00 USD | 171,250.00 USD | 2,700.00 USD | 166,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 243,340,000.00 USD | 243,340,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 147,630,000.00 USD | 147,630,000.00 USD | 0.00 USD | 26,460.00 USD | 88,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 245,060,000.00 USD | 245,060,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 193,360.00 USD | 415,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 147,960,000.00 USD | 147,960,000.00 USD | 53,740.00 USD | 104,420.00 USD | 171,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 245,550,000.00 USD | 245,550,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 148,160,000.00 USD | 148,160,000.00 USD | 126,110.00 USD | 2,890.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 246,960,000.00 USD | 246,960,000.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 148,360,000.00 USD | 148,360,000.00 USD | 7,080.00 USD | 67,780.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 248,150,000.00 USD | 248,150,000.00 USD | 351,750.00 USD | 372,470.00 USD | 461,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 148,560,000.00 USD | 148,560,000.00 USD | 75,340.00 USD | 1,780.00 USD | 126,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 250,620,000.00 USD | 250,620,000.00 USD | 821,620.00 USD | 376,730.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 148,840,000.00 USD | 148,840,000.00 USD | 120,880.00 USD | 30,080.00 USD | 125,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 252,420,000.00 USD | 252,420,000.00 USD | 536,130.00 USD | 295,850.00 USD | 966,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 65,510.00 USD | 480,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,230,000.00 USD | 149,230,000.00 USD | 93,260.00 USD | 50,590.00 USD | 254,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 253,910,000.00 USD | 253,910,000.00 USD | 617,230.00 USD | 329,740.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,710,000.00 USD | 149,710,000.00 USD | 195,140.00 USD | 100,700.00 USD | 182,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 256,010,000.00 USD | 256,010,000.00 USD | 579,450.00 USD | 256,720.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,790,000.00 USD | 149,790,000.00 USD | 12,100.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 258,560,000.00 USD | 258,560,000.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,960,000.00 USD | 149,960,000.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 259,650,000.00 USD | 259,650,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,010,000.00 USD | 150,010,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 260,930,000.00 USD | 260,930,000.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 482,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,070,000.00 USD | 150,070,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 261,480,000.00 USD | 261,480,000.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,160,000.00 USD | 150,160,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 262,580,000.00 USD | 262,580,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 262,740,000.00 USD | 262,740,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,180,000.00 USD | 150,180,000.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 263,070,000.00 USD | 263,070,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,240,000.00 USD | 263,240,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 484,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,360,000.00 USD | 263,360,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,370,000.00 USD | 263,370,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,500,000.00 USD | 263,500,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,620,000.00 USD | 263,620,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 263,860,000.00 USD | 263,860,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 635.06 USD | 484,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 264,030,000.00 USD | 264,030,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 264,410,000.00 USD | 264,410,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 265,050,000.00 USD | 265,050,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 265,230,000.00 USD | 265,230,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 265,850,000.00 USD | 265,850,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,930.00 USD | 488,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 266,380,000.00 USD | 266,380,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 267,400,000.00 USD | 267,400,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 268,780,000.00 USD | 268,780,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 269,400,000.00 USD | 269,400,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 269,760,000.00 USD | 269,760,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,280.00 USD | 582,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 270,780,000.00 USD | 270,780,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 272,290,000.00 USD | 272,290,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 273,680,000.00 USD | 273,680,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 274,480,000.00 USD | 274,480,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 275,010,000.00 USD | 275,010,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 988.72 USD | 583,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 275,360,000.00 USD | 275,360,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 275,810,000.00 USD | 275,810,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 276,530,000.00 USD | 276,530,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 276,900,000.00 USD | 276,900,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 277,030,000.00 USD | 277,030,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 583,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 277,160,000.00 USD | 277,160,000.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 277,490,000.00 USD | 277,490,000.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 278,100,000.00 USD | 278,100,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 278,660,000.00 USD | 278,660,000.00 USD | 182,110.00 USD | 128,180.00 USD | 249,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,120,000.00 USD | 279,120,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,280,000.00 USD | 279,280,000.00 USD | 85,350.00 USD | 50,790.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,750,000.00 USD | 279,750,000.00 USD | 119,110.00 USD | 55,850.00 USD | 296,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,960,000.00 USD | 279,960,000.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.2550` | 64,310,000.00 USD | 0.00 USD | 496.49 USD | `-79.50%` | `1,947.00` |
| `Live` | `Long` | `0.2650` | 64,310,000.00 USD | 0.00 USD | 1,060.00 USD | `-78.69%` | `3,993.00` |
| `Live` | `Long` | `0.2750` | 64,310,000.00 USD | 0.00 USD | 1,190.00 USD | `-77.89%` | `4,321.00` |
| `Live` | `Long` | `0.2850` | 64,300,000.00 USD | 0.00 USD | 1,120.00 USD | `-77.09%` | `3,942.00` |
| `Live` | `Long` | `0.3050` | 64,300,000.00 USD | 0.00 USD | 23,570.00 USD | `-75.48%` | `77,273.00` |
| `Live` | `Long` | `0.3150` | 64,280,000.00 USD | 0.00 USD | 9,600.00 USD | `-74.67%` | `30,461.00` |
| `Live` | `Long` | `0.3250` | 64,270,000.00 USD | 0.00 USD | 8,310.00 USD | `-73.87%` | `25,565.00` |
| `Live` | `Long` | `0.3350` | 64,260,000.00 USD | 0.00 USD | 20,510.00 USD | `-73.07%` | `61,233.00` |
| `Live` | `Long` | `0.3450` | 64,240,000.00 USD | 0.00 USD | 1,580.00 USD | `-72.26%` | `4,586.00` |
| `Live` | `Long` | `0.3550` | 64,240,000.00 USD | 0.00 USD | 30,620.00 USD | `-71.46%` | `86,246.00` |
| `Live` | `Long` | `0.3650` | 64,210,000.00 USD | 0.00 USD | 2,860.00 USD | `-70.65%` | `7,827.00` |
| `Live` | `Long` | `0.3750` | 64,210,000.00 USD | 0.00 USD | 183.00 USD | `-69.85%` | `488.00` |
| `Live` | `Long` | `0.3850` | 64,210,000.00 USD | 0.00 USD | 312.62 USD | `-69.05%` | `812.00` |
| `Live` | `Long` | `0.3950` | 64,210,000.00 USD | 0.00 USD | 174.59 USD | `-68.24%` | `442.00` |
| `Live` | `Long` | `0.4050` | 64,210,000.00 USD | 0.00 USD | 167.27 USD | `-67.44%` | `413.00` |
| `Live` | `Long` | `0.4150` | 64,210,000.00 USD | 0.00 USD | 2,090.00 USD | `-66.63%` | `5,039.00` |
| `Live` | `Long` | `0.4250` | 64,200,000.00 USD | 0.00 USD | 707,570.00 USD | `-65.83%` | `1,664,877.00` |
| `Live` | `Long` | `0.4350` | 63,500,000.00 USD | 0.00 USD | 18,000.00 USD | `-65.03%` | `41,377.00` |
| `Live` | `Long` | `0.4450` | 63,480,000.00 USD | 0.00 USD | 1,070.00 USD | `-64.22%` | `2,400.00` |
| `Live` | `Long` | `0.4550` | 63,480,000.00 USD | 0.00 USD | 244.34 USD | `-63.42%` | `537.00` |
| `Live` | `Long` | `0.4650` | 63,480,000.00 USD | 0.00 USD | 11,930.00 USD | `-62.61%` | `25,650.00` |
| `Live` | `Long` | `0.4750` | 63,460,000.00 USD | 0.00 USD | 10,880.00 USD | `-61.81%` | `22,904.00` |
| `Live` | `Long` | `0.4850` | 63,450,000.00 USD | 0.00 USD | 4,030.00 USD | `-61.01%` | `8,312.00` |
| `Live` | `Long` | `0.4950` | 63,450,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.20%` | `2,057.00` |
| `Live` | `Long` | `0.5050` | 63,450,000.00 USD | 0.00 USD | 188.87 USD | `-59.40%` | `374.00` |
| `Live` | `Long` | `0.5150` | 63,450,000.00 USD | 0.00 USD | 1,960.00 USD | `-58.59%` | `3,812.00` |
| `Live` | `Long` | `0.5250` | 63,450,000.00 USD | 0.00 USD | 1,430.00 USD | `-57.79%` | `2,732.00` |
| `Live` | `Long` | `0.5350` | 63,450,000.00 USD | 0.00 USD | 45,410.00 USD | `-56.99%` | `84,883.00` |
| `Live` | `Long` | `0.5450` | 63,400,000.00 USD | 0.00 USD | 276.31 USD | `-56.18%` | `507.00` |
| `Live` | `Long` | `0.5550` | 63,400,000.00 USD | 0.00 USD | 3,060.00 USD | `-55.38%` | `5,508.00` |
| `Live` | `Long` | `0.5650` | 63,400,000.00 USD | 0.00 USD | 162,420.00 USD | `-54.57%` | `287,461.00` |
| `Live` | `Long` | `0.5750` | 63,230,000.00 USD | 0.00 USD | 6,560.00 USD | `-53.77%` | `11,417.00` |
| `Live` | `Long` | `0.5850` | 63,230,000.00 USD | 0.00 USD | 1,550.00 USD | `-52.97%` | `2,653.00` |
| `Live` | `Long` | `0.5950` | 63,230,000.00 USD | 0.00 USD | 7,660.00 USD | `-52.16%` | `12,869.00` |
| `Live` | `Long` | `0.6050` | 63,220,000.00 USD | 0.00 USD | 20,970.00 USD | `-51.36%` | `34,659.00` |
| `Live` | `Long` | `0.6150` | 63,200,000.00 USD | 0.00 USD | 38,950.00 USD | `-50.55%` | `63,339.00` |
| `Live` | `Long` | `0.6250` | 63,160,000.00 USD | 0.00 USD | 2,050.00 USD | `-49.75%` | `3,282.00` |
| `Live` | `Long` | `0.6350` | 63,160,000.00 USD | 0.00 USD | 11,300.00 USD | `-48.95%` | `17,794.00` |
| `Live` | `Long` | `0.6450` | 63,140,000.00 USD | 0.00 USD | 19,040.00 USD | `-48.14%` | `29,515.00` |
| `Live` | `Long` | `0.6550` | 63,130,000.00 USD | 0.00 USD | 1,290.00 USD | `-47.34%` | `1,965.00` |
| `Live` | `Long` | `0.6650` | 63,120,000.00 USD | 0.00 USD | 17,920.00 USD | `-46.53%` | `26,954.00` |
| `Live` | `Long` | `0.6750` | 63,110,000.00 USD | 0.00 USD | 27,760.00 USD | `-45.73%` | `41,124.00` |
| `Live` | `Long` | `0.6850` | 63,080,000.00 USD | 0.00 USD | 5,320.00 USD | `-44.93%` | `7,764.00` |
| `Live` | `Long` | `0.6950` | 63,070,000.00 USD | 0.00 USD | 144,240.00 USD | `-44.12%` | `207,541.00` |
| `Live` | `Long` | `0.7050` | 62,930,000.00 USD | 0.00 USD | 49,520.00 USD | `-43.32%` | `70,240.00` |
| `Live` | `Long` | `0.7150` | 62,880,000.00 USD | 0.00 USD | 73,620.00 USD | `-42.51%` | `102,963.00` |
| `Live` | `Long` | `0.7250` | 62,810,000.00 USD | 0.00 USD | 219,560.00 USD | `-41.71%` | `302,846.00` |
| `Live` | `Long` | `0.7350` | 62,590,000.00 USD | 0.00 USD | 44,260.00 USD | `-40.91%` | `60,220.00` |
| `Live` | `Long` | `0.7450` | 62,540,000.00 USD | 0.00 USD | 56,770.00 USD | `-40.10%` | `76,196.00` |
| `Live` | `Long` | `0.7550` | 62,490,000.00 USD | 0.00 USD | 86,500.00 USD | `-39.30%` | `114,564.00` |
| `Live` | `Long` | `0.7650` | 62,400,000.00 USD | 0.00 USD | 123,440.00 USD | `-38.49%` | `161,366.00` |
| `Live` | `Long` | `0.7750` | 62,280,000.00 USD | 0.00 USD | 5,740.00 USD | `-37.69%` | `7,408.00` |
| `Live` | `Long` | `0.7850` | 62,270,000.00 USD | 0.00 USD | 16,010.00 USD | `-36.89%` | `20,401.00` |
| `Live` | `Long` | `0.7950` | 62,250,000.00 USD | 0.00 USD | 508,760.00 USD | `-36.08%` | `639,954.00` |
| `Live` | `Long` | `0.8050` | 61,750,000.00 USD | 0.00 USD | 10,860.00 USD | `-35.28%` | `13,488.00` |
| `Live` | `Long` | `0.8150` | 61,730,000.00 USD | 0.00 USD | 49,720.00 USD | `-34.47%` | `61,009.00` |
| `Live` | `Long` | `0.8250` | 61,680,000.00 USD | 0.00 USD | 2,950,000.00 USD | `-33.67%` | `3,581,413.00` |
| `Live` | `Long` | `0.8350` | 58,730,000.00 USD | 0.00 USD | 34,670.00 USD | `-32.87%` | `41,516.00` |
| `Live` | `Long` | `0.8450` | 58,700,000.00 USD | 0.00 USD | 75,630.00 USD | `-32.06%` | `89,498.00` |
| `Live` | `Long` | `0.8550` | 58,620,000.00 USD | 0.00 USD | 48,680.00 USD | `-31.26%` | `56,934.00` |
| `Live` | `Long` | `0.8650` | 58,570,000.00 USD | 0.00 USD | 5,460.00 USD | `-30.46%` | `6,313.00` |
| `Live` | `Long` | `0.8750` | 58,570,000.00 USD | 0.00 USD | 95,210.00 USD | `-29.65%` | `108,806.00` |
| `Live` | `Long` | `0.8850` | 58,470,000.00 USD | 0.00 USD | 344,110.00 USD | `-28.85%` | `388,827.00` |
| `Live` | `Long` | `0.8950` | 58,130,000.00 USD | 0.00 USD | 108,160.00 USD | `-28.04%` | `120,851.00` |
| `Live` | `Long` | `0.9050` | 58,020,000.00 USD | 0.00 USD | 138,790.00 USD | `-27.24%` | `153,355.00` |
| `Live` | `Long` | `0.9150` | 57,880,000.00 USD | 0.00 USD | 81,300.00 USD | `-26.44%` | `88,854.00` |
| `Live` | `Long` | `0.9250` | 57,800,000.00 USD | 0.00 USD | 80,910.00 USD | `-25.63%` | `87,471.00` |
| `Live` | `Long` | `0.9350` | 57,720,000.00 USD | 0.00 USD | 271,720.00 USD | `-24.83%` | `290,612.00` |
| `Live` | `Long` | `0.9450` | 57,450,000.00 USD | 0.00 USD | 65,480.00 USD | `-24.02%` | `69,295.00` |
| `Live` | `Long` | `0.9550` | 57,380,000.00 USD | 0.00 USD | 156,510.00 USD | `-23.22%` | `163,889.00` |
| `Live` | `Long` | `0.9650` | 57,220,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-22.42%` | `35,116,718.00` |
| `Live` | `Long` | `0.9750` | 23,340,000.00 USD | 0.00 USD | 178,750.00 USD | `-21.61%` | `183,331.00` |
| `Live` | `Long` | `0.9850` | 23,160,000.00 USD | 0.00 USD | 459,360.00 USD | `-20.81%` | `466,358.00` |
| `Live` | `Long` | `0.9950` | 22,700,000.00 USD | 0.00 USD | 2,670,000.00 USD | `-20.00%` | `2,683,734.00` |
| `Live` | `Long` | `1.00` | 20,030,000.00 USD | 0.00 USD | 463,000.00 USD | `-19.20%` | `460,692.00` |
| `Live` | `Long` | `1.01` | 19,560,000.00 USD | 0.00 USD | 386,700.00 USD | `-18.40%` | `380,984.00` |
| `Live` | `Long` | `1.02` | 19,180,000.00 USD | 0.00 USD | 52,650.00 USD | `-17.59%` | `51,367.00` |
| `Live` | `Long` | `1.03` | 19,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-16.79%` | `2,046,550.00` |
| `Live` | `Long` | `1.04` | 17,010,000.00 USD | 0.00 USD | 662,160.00 USD | `-15.98%` | `633,650.00` |
| `Live` | `Long` | `1.05` | 16,340,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-15.18%` | `1,081,155.00` |
| `Live` | `Long` | `1.06` | 15,200,000.00 USD | 0.00 USD | 747,180.00 USD | `-14.38%` | `701,579.00` |
| `Live` | `Long` | `1.07` | 14,460,000.00 USD | 0.00 USD | 955,410.00 USD | `-13.57%` | `888,757.00` |
| `Live` | `Long` | `1.08` | 13,500,000.00 USD | 0.00 USD | 188,350.00 USD | `-12.77%` | `173,590.00` |
| `Live` | `Long` | `1.09` | 13,310,000.00 USD | 0.00 USD | 381,630.00 USD | `-11.96%` | `348,521.00` |
| `Live` | `Long` | `1.10` | 12,930,000.00 USD | 0.00 USD | 376,130.00 USD | `-11.16%` | `340,392.00` |
| `Live` | `Long` | `1.11` | 12,560,000.00 USD | 0.00 USD | 289,050.00 USD | `-10.36%` | `259,237.00` |
| `Live` | `Long` | `1.12` | 12,270,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-9.55%` | `1,962,559.00` |
| `Live` | `Long` | `1.14` | 10,060,000.00 USD | 0.00 USD | 131,930.00 USD | `-8.75%` | `116,242.00` |
| `Live` | `Long` | `1.15` | 9,930,000.00 USD | 0.00 USD | 332,060.00 USD | `-7.94%` | `290,006.00` |
| `Live` | `Long` | `1.16` | 9,590,000.00 USD | 0.00 USD | 531,180.00 USD | `-7.14%` | `459,897.00` |
| `Live` | `Long` | `1.17` | 9,060,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-6.34%` | `1,385,303.00` |
| `Live` | `Long` | `1.18` | 7,450,000.00 USD | 0.00 USD | 514,860.00 USD | `-5.53%` | `438,177.00` |
| `Live` | `Long` | `1.19` | 6,930,000.00 USD | 0.00 USD | 443,330.00 USD | `-4.73%` | `374,117.00` |
| `Live` | `Long` | `1.20` | 6,490,000.00 USD | 0.00 USD | 742,780.00 USD | `-3.92%` | `621,573.00` |
| `Live` | `Long` | `1.21` | 5,750,000.00 USD | 0.00 USD | 4,610.00 USD | `-3.12%` | `3,827.00` |
| `Live` | `Long` | `1.22` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | `-2.32%` | `4,726,954.00` |
| `Live` | `Long` | `1.23` | 433.65 USD | 0.00 USD | 433.65 USD | `-1.51%` | `354.00` |
| `Live` | `Short` | `1.25` | 9,740.00 USD | 9,740.00 USD | 0.00 USD | `+0.90%` | `7,764.00` |
| `Live` | `Short` | `1.26` | 130,190.00 USD | 120,440.00 USD | 0.00 USD | `+1.70%` | `95,211.00` |
| `Live` | `Short` | `1.27` | 140,340.00 USD | 10,160.00 USD | 0.00 USD | `+2.51%` | `7,966.00` |
| `Live` | `Short` | `1.28` | 142,740.00 USD | 2,390.00 USD | 0.00 USD | `+3.31%` | `1,862.00` |
| `Live` | `Short` | `1.29` | 143,430.00 USD | 692.82 USD | 0.00 USD | `+4.12%` | `535.00` |
| `Live` | `Short` | `1.30` | 143,670.00 USD | 246.65 USD | 0.00 USD | `+4.92%` | `189.00` |
| `Live` | `Short` | `1.32` | 200,620.00 USD | 56,950.00 USD | 0.00 USD | `+6.53%` | `42,980.00` |
| `Live` | `Short` | `1.33` | 202,050.00 USD | 1,430.00 USD | 0.00 USD | `+7.33%` | `1,072.00` |
| `Live` | `Short` | `1.34` | 219,390.00 USD | 17,330.00 USD | 0.00 USD | `+8.14%` | `12,888.00` |
| `Live` | `Short` | `1.35` | 222,080.00 USD | 2,700.00 USD | 0.00 USD | `+8.94%` | `1,989.00` |
| `Live` | `Short` | `1.36` | 415,440.00 USD | 193,360.00 USD | 0.00 USD | `+9.74%` | `141,656.00` |
| `Live` | `Short` | `1.38` | 480,960.00 USD | 65,510.00 USD | 0.00 USD | `+10.55%` | `47,645.00` |
| `Live` | `Short` | `1.39` | 482,230.00 USD | 1,280.00 USD | 0.00 USD | `+11.35%` | `921.00` |
| `Live` | `Short` | `1.40` | 484,320.00 USD | 2,090.00 USD | 0.00 USD | `+12.16%` | `1,500.00` |
| `Live` | `Short` | `1.41` | 484,960.00 USD | 635.06 USD | 0.00 USD | `+12.96%` | `452.00` |
| `Live` | `Short` | `1.42` | 488,890.00 USD | 3,930.00 USD | 0.00 USD | `+13.76%` | `2,776.00` |
| `Live` | `Short` | `1.43` | 582,170.00 USD | 93,280.00 USD | 0.00 USD | `+14.57%` | `65,460.00` |
| `Live` | `Short` | `1.44` | 583,160.00 USD | 988.72 USD | 0.00 USD | `+15.37%` | `689.00` |
| `Live` | `Short` | `1.45` | 583,440.00 USD | 284.66 USD | 0.00 USD | `+16.18%` | `197.00` |
| `Live` | `Short` | `1.47` | 1,280,000.00 USD | 697,610.00 USD | 0.00 USD | `+17.78%` | `476,186.00` |
| `Live` | `Short` | `1.50` | 1,290,000.00 USD | 12,150.00 USD | 0.00 USD | `+20.20%` | `8,126.00` |
| `Live` | `Short` | `1.50` | 1,310,000.00 USD | 12,630.00 USD | 0.00 USD | `+21.00%` | `8,392.00` |
| `Live` | `Short` | `1.51` | 1,320,000.00 USD | 11,570.00 USD | 0.00 USD | `+21.80%` | `7,640.00` |
| `Live` | `Short` | `1.53` | 1,320,000.00 USD | 1,390.00 USD | 0.00 USD | `+23.41%` | `903.00` |
| `Live` | `Short` | `1.54` | 1,320,000.00 USD | 1,370.00 USD | 0.00 USD | `+24.22%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,320,000.00 USD | 1,360.00 USD | 0.00 USD | `+25.02%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,320,000.00 USD | 679.21 USD | 0.00 USD | `+25.82%` | `434.00` |
| `Live` | `Short` | `1.57` | 1,330,000.00 USD | 2,900.00 USD | 0.00 USD | `+26.63%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,330,000.00 USD | 123.63 USD | 0.00 USD | `+27.43%` | `78.00` |
| `Live` | `Short` | `1.59` | 5,590,000.00 USD | 4,260,000.00 USD | 0.00 USD | `+28.24%` | `2,672,981.00` |
| `Live` | `Short` | `1.60` | 5,590,000.00 USD | 239.15 USD | 0.00 USD | `+29.04%` | `149.00` |
| `Live` | `Short` | `1.61` | 5,590,000.00 USD | 2,660.00 USD | 0.00 USD | `+29.84%` | `1,647.00` |
| `Live` | `Short` | `1.62` | 5,590,000.00 USD | 2,210.00 USD | 0.00 USD | `+30.65%` | `1,362.00` |
| `Live` | `Short` | `1.64` | 5,600,000.00 USD | 4,850.00 USD | 0.00 USD | `+31.45%` | `2,969.00` |
| `Live` | `Short` | `1.65` | 5,730,000.00 USD | 135,940.00 USD | 0.00 USD | `+32.26%` | `82,639.00` |
| `Live` | `Short` | `1.66` | 5,730,000.00 USD | 147.30 USD | 0.00 USD | `+33.06%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,740,000.00 USD | 586.08 USD | 0.00 USD | `+33.86%` | `352.00` |
| `Live` | `Short` | `1.68` | 5,740,000.00 USD | 298.15 USD | 0.00 USD | `+34.67%` | `178.00` |
| `Live` | `Short` | `1.69` | 5,740,000.00 USD | 4,060.00 USD | 0.00 USD | `+35.47%` | `2,409.00` |
| `Live` | `Short` | `1.70` | 5,740,000.00 USD | 110.17 USD | 0.00 USD | `+36.28%` | `65.00` |
| `Live` | `Short` | `1.71` | 5,740,000.00 USD | 4,070.00 USD | 0.00 USD | `+37.08%` | `2,388.00` |
| `Live` | `Short` | `1.72` | 5,750,000.00 USD | 1,230.00 USD | 0.00 USD | `+37.88%` | `720.00` |
| `Live` | `Short` | `1.74` | 5,750,000.00 USD | 2,970.00 USD | 0.00 USD | `+39.49%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 5,760,000.00 USD | 8,390.00 USD | 0.00 USD | `+40.30%` | `4,810.00` |
| `Live` | `Short` | `1.75` | 5,760,000.00 USD | 591.43 USD | 0.00 USD | `+41.10%` | `337.00` |
| `Live` | `Short` | `1.76` | 5,760,000.00 USD | 808.37 USD | 0.00 USD | `+41.90%` | `458.00` |
| `Live` | `Short` | `1.78` | 5,890,000.00 USD | 130,410.00 USD | 0.00 USD | `+43.51%` | `73,058.00` |
| `Live` | `Short` | `1.79` | 5,890,000.00 USD | 5,420.00 USD | 0.00 USD | `+44.32%` | `3,019.00` |
| `Live` | `Short` | `1.80` | 5,890,000.00 USD | 889.87 USD | 0.00 USD | `+45.12%` | `493.00` |
| `Live` | `Short` | `1.81` | 5,910,000.00 USD | 19,040.00 USD | 0.00 USD | `+45.92%` | `10,490.00` |
| `Live` | `Short` | `1.82` | 6,090,000.00 USD | 173,030.00 USD | 0.00 USD | `+46.73%` | `94,810.00` |
| `Live` | `Short` | `1.83` | 6,100,000.00 USD | 12,360.00 USD | 0.00 USD | `+47.53%` | `6,737.00` |
| `Live` | `Short` | `1.84` | 6,210,000.00 USD | 108,590.00 USD | 0.00 USD | `+48.34%` | `58,855.00` |
| `Live` | `Short` | `1.85` | 11,160,000.00 USD | 4,960,000.00 USD | 0.00 USD | `+49.14%` | `2,671,376.00` |
| `Live` | `Short` | `1.86` | 14,040,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+49.94%` | `1,541,696.00` |
| `Live` | `Short` | `1.90` | 14,040,000.00 USD | 4,190.00 USD | 0.00 USD | `+52.36%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 14,100,000.00 USD | 56,390.00 USD | 0.00 USD | `+53.16%` | `29,599.00` |
| `Live` | `Short` | `1.92` | 17,030,000.00 USD | 2,930,000.00 USD | 0.00 USD | `+53.96%` | `1,532,127.00` |
| `Live` | `Short` | `1.93` | 17,290,000.00 USD | 257,200.00 USD | 0.00 USD | `+54.77%` | `133,610.00` |
| `Live` | `Short` | `1.94` | 17,600,000.00 USD | 312,150.00 USD | 0.00 USD | `+55.57%` | `161,320.00` |
| `Live` | `Short` | `1.95` | 17,600,000.00 USD | 807.17 USD | 0.00 USD | `+56.38%` | `415.00` |
| `Live` | `Short` | `1.96` | 17,600,000.00 USD | 293.25 USD | 0.00 USD | `+57.18%` | `150.00` |
| `Live` | `Short` | `1.97` | 17,870,000.00 USD | 266,860.00 USD | 0.00 USD | `+57.98%` | `135,806.00` |
| `Live` | `Short` | `1.98` | 17,870,000.00 USD | 1,340.00 USD | 0.00 USD | `+58.79%` | `680.00` |
| `Live` | `Short` | `1.99` | 17,870,000.00 USD | 397.00 USD | 0.00 USD | `+59.59%` | `200.00` |
| `Live` | `Short` | `2.02` | 17,870,000.00 USD | 513.83 USD | 0.00 USD | `+62.00%` | `255.00` |
| `Live` | `Short` | `2.02` | 18,280,000.00 USD | 405,000.00 USD | 0.00 USD | `+62.81%` | `200,000.00` |
| `Live` | `Short` | `2.04` | 18,280,000.00 USD | 989.78 USD | 0.00 USD | `+64.42%` | `484.00` |
| `Live` | `Short` | `2.06` | 18,280,000.00 USD | 584.39 USD | 0.00 USD | `+66.02%` | `283.00` |
| `Live` | `Short` | `2.08` | 18,280,000.00 USD | 373.50 USD | 0.00 USD | `+66.83%` | `180.00` |
| `Live` | `Short` | `2.10` | 18,280,000.00 USD | 806.57 USD | 0.00 USD | `+68.44%` | `385.00` |
| `Live` | `Short` | `2.10` | 18,280,000.00 USD | 294.70 USD | 0.00 USD | `+69.24%` | `140.00` |
| `Live` | `Short` | `2.12` | 18,280,000.00 USD | 3,100.00 USD | 0.00 USD | `+70.04%` | `1,468.00` |
| `Live` | `Short` | `2.12` | 18,530,000.00 USD | 249,460.00 USD | 0.00 USD | `+70.85%` | `117,391.00` |
| `Live` | `Short` | `2.13` | 18,530,000.00 USD | 926.59 USD | 0.00 USD | `+71.65%` | `434.00` |
| `Live` | `Short` | `2.15` | 18,530,000.00 USD | 631.42 USD | 0.00 USD | `+73.26%` | `293.00` |
| `Live` | `Short` | `2.17` | 18,540,000.00 USD | 2,630.00 USD | 0.00 USD | `+74.87%` | `1,207.00` |
| `Live` | `Short` | `2.19` | 18,540,000.00 USD | 201.02 USD | 0.00 USD | `+75.67%` | `92.00` |
| `Live` | `Short` | `2.19` | 18,540,000.00 USD | 201.94 USD | 0.00 USD | `+76.48%` | `92.00` |
| `Live` | `Short` | `2.21` | 18,540,000.00 USD | 2,130.00 USD | 0.00 USD | `+77.28%` | `965.00` |
| `Live` | `Short` | `2.21` | 18,540,000.00 USD | 101.89 USD | 0.00 USD | `+78.08%` | `46.00` |
| `Live` | `Short` | `2.23` | 18,600,000.00 USD | 62,200.00 USD | 0.00 USD | `+78.89%` | `27,956.00` |
| `Live` | `Short` | `2.23` | 18,680,000.00 USD | 79,110.00 USD | 0.00 USD | `+79.69%` | `35,398.00` |
| `Live` | `Short` | `2.25` | 18,760,000.00 USD | 83,090.00 USD | 0.00 USD | `+81.30%` | `36,849.00` |
| `Live` | `Short` | `2.27` | 18,760,000.00 USD | 104.19 USD | 0.00 USD | `+82.10%` | `46.00` |
| `Live` | `Short` | `2.31` | 18,760,000.00 USD | 142.91 USD | 0.00 USD | `+85.32%` | `62.00` |
| `Live` | `Short` | `2.31` | 18,890,000.00 USD | 122,260.00 USD | 0.00 USD | `+86.12%` | `52,814.00` |
| `Live` | `Short` | `2.33` | 18,890,000.00 USD | 106.95 USD | 0.00 USD | `+86.93%` | `46.00` |
| `Live` | `Short` | `2.33` | 18,890,000.00 USD | 3,580.00 USD | 0.00 USD | `+87.73%` | `1,535.00` |
| `Live` | `Short` | `2.35` | 18,900,000.00 USD | 11,860.00 USD | 0.00 USD | `+88.54%` | `5,057.00` |
| `Live` | `Short` | `2.38` | 18,910,000.00 USD | 2,850.00 USD | 0.00 USD | `+90.95%` | `1,199.00` |
| `Live` | `Short` | `2.38` | 22,510,000.00 USD | 3,610,000.00 USD | 0.00 USD | `+91.75%` | `1,512,779.00` |
| `Live` | `Short` | `2.42` | 22,510,000.00 USD | 678.62 USD | 0.00 USD | `+94.16%` | `281.00` |
| `Live` | `Short` | `2.42` | 22,630,000.00 USD | 117,850.00 USD | 0.00 USD | `+94.97%` | `48,597.00` |
| `Live` | `Short` | `2.44` | 22,640,000.00 USD | 3,910.00 USD | 0.00 USD | `+96.58%` | `1,598.00` |
| `Live` | `Short` | `2.46` | 22,640,000.00 USD | 360.88 USD | 0.00 USD | `+97.38%` | `147.00` |
| `Live` | `Short` | `2.46` | 22,660,000.00 USD | 23,250.00 USD | 0.00 USD | `+98.18%` | `9,432.00` |
| `Live` | `Short` | `2.48` | 22,660,000.00 USD | 337.96 USD | 0.00 USD | `+99.79%` | `136.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 2,090,000.00 USD | 0.00 USD | 102.00 USD | `-79.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 2,090,000.00 USD | 0.00 USD | 351.50 USD | `-70.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 2,090,000.00 USD | 0.00 USD | 139.12 USD | `-69.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 2,090,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 2,090,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 2,080,000.00 USD | 0.00 USD | 408.51 USD | `-64.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 2,080,000.00 USD | 0.00 USD | 273.00 USD | `-63.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 2,080,000.00 USD | 0.00 USD | 151.12 USD | `-62.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 2,080,000.00 USD | 0.00 USD | 142.50 USD | `-61.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 2,080,000.00 USD | 0.00 USD | 145.50 USD | `-61.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 2,080,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 2,080,000.00 USD | 0.00 USD | 285.82 USD | `-58.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 2,080,000.00 USD | 0.00 USD | 306.60 USD | `-57.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 2,080,000.00 USD | 0.00 USD | 121.55 USD | `-55.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 2,080,000.00 USD | 0.00 USD | 656.53 USD | `-54.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 2,080,000.00 USD | 0.00 USD | 100.62 USD | `-52.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 2,080,000.00 USD | 0.00 USD | 203.75 USD | `-49.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 2,080,000.00 USD | 0.00 USD | 791.85 USD | `-48.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 2,080,000.00 USD | 0.00 USD | 573.40 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 2,080,000.00 USD | 0.00 USD | 244.31 USD | `-47.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 2,080,000.00 USD | 0.00 USD | 29,530.00 USD | `-46.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 2,050,000.00 USD | 0.00 USD | 503.55 USD | `-45.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 2,050,000.00 USD | 0.00 USD | 480.19 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 2,050,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 2,040,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 2,030,000.00 USD | 0.00 USD | 228.80 USD | `-42.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 2,030,000.00 USD | 0.00 USD | 536.50 USD | `-41.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 2,030,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 2,030,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 2,030,000.00 USD | 0.00 USD | 878.48 USD | `-36.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 2,030,000.00 USD | 0.00 USD | 6,020.00 USD | `-33.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 2,020,000.00 USD | 0.00 USD | 1,360.00 USD | `-31.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 2,020,000.00 USD | 0.00 USD | 690.38 USD | `-29.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 2,020,000.00 USD | 0.00 USD | 1,210.00 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 2,020,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 2,020,000.00 USD | 0.00 USD | 838.94 USD | `-27.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 2,020,000.00 USD | 0.00 USD | 338.55 USD | `-26.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 2,020,000.00 USD | 0.00 USD | 1,060.00 USD | `-25.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 2,010,000.00 USD | 0.00 USD | 1,090.00 USD | `-24.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 2,010,000.00 USD | 0.00 USD | 112.46 USD | `-24.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 2,010,000.00 USD | 0.00 USD | 1,730.00 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 2,010,000.00 USD | 0.00 USD | 4,010.00 USD | `-22.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 2,010,000.00 USD | 0.00 USD | 6,200.00 USD | `-21.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 2,000,000.00 USD | 0.00 USD | 4,890.00 USD | `-20.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 2,000,000.00 USD | 0.00 USD | 902.47 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,000,000.00 USD | 0.00 USD | 15,420.00 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,980,000.00 USD | 0.00 USD | 6,640.00 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,970,000.00 USD | 0.00 USD | 1,840.00 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,970,000.00 USD | 0.00 USD | 42,670.00 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,930,000.00 USD | 0.00 USD | 1,780.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,930,000.00 USD | 0.00 USD | 24,230.00 USD | `-15.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,900,000.00 USD | 0.00 USD | 4,570.00 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,900,000.00 USD | 0.00 USD | 48,460.00 USD | `-13.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,850,000.00 USD | 0.00 USD | 3,690.00 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,850,000.00 USD | 0.00 USD | 279,970.00 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,570,000.00 USD | 0.00 USD | 21,590.00 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,540,000.00 USD | 0.00 USD | 9,410.00 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,540,000.00 USD | 0.00 USD | 101,980.00 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,430,000.00 USD | 0.00 USD | 13,490.00 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,420,000.00 USD | 0.00 USD | 120,050.00 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,300,000.00 USD | 0.00 USD | 40,320.00 USD | `-7.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,260,000.00 USD | 0.00 USD | 42,080.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,220,000.00 USD | 0.00 USD | 94,830.00 USD | `-5.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 1,120,000.00 USD | 0.00 USD | 221,020.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 901,340.00 USD | 0.00 USD | 409,570.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 491,780.00 USD | 0.00 USD | 93,540.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 398,230.00 USD | 0.00 USD | 289,680.00 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 108,550.00 USD | 0.00 USD | 22,330.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 86,220.00 USD | 0.00 USD | 86,220.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 89,900.00 USD | 89,900.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 164,730.00 USD | 74,830.00 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 468,750.00 USD | 304,020.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 486,910.00 USD | 18,160.00 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 737,700.00 USD | 250,780.00 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 791,940.00 USD | 54,240.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 1,030,000.00 USD | 242,720.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,680,000.00 USD | 649,810.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,900,000.00 USD | 214,110.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,950,000.00 USD | 47,230.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 2,060,000.00 USD | 112,700.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 2,070,000.00 USD | 14,640.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 2,320,000.00 USD | 249,240.00 USD | 0.00 USD | `+9.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 2,400,000.00 USD | 81,760.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 2,460,000.00 USD | 53,860.00 USD | 0.00 USD | `+11.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 2,460,000.00 USD | 3,960.00 USD | 0.00 USD | `+12.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,310,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+12.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,310,000.00 USD | 3,710.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,320,000.00 USD | 5,990.00 USD | 0.00 USD | `+14.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,390,000.00 USD | 78,630.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,640,000.00 USD | 242,580.00 USD | 0.00 USD | `+16.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,640,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,670,000.00 USD | 23,260.00 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,780,000.00 USD | 108,020.00 USD | 0.00 USD | `+18.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,790,000.00 USD | 14,970.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,810,000.00 USD | 15,800.00 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,860,000.00 USD | 57,590.00 USD | 0.00 USD | `+21.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,880,000.00 USD | 11,760.00 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,900,000.00 USD | 19,430.00 USD | 0.00 USD | `+22.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,940,000.00 USD | 45,620.00 USD | 0.00 USD | `+23.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,950,000.00 USD | 10,870.00 USD | 0.00 USD | `+24.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,950,000.00 USD | 2,380.00 USD | 0.00 USD | `+25.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,960,000.00 USD | 6,450.00 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,970,000.00 USD | 5,570.00 USD | 0.00 USD | `+26.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,980,000.00 USD | 10,250.00 USD | 0.00 USD | `+27.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 7,090,000.00 USD | 113,910.00 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 7,130,000.00 USD | 40,290.00 USD | 0.00 USD | `+29.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,210,000.00 USD | 80,330.00 USD | 0.00 USD | `+29.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,210,000.00 USD | 464.75 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,390,000.00 USD | 179,860.00 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,390,000.00 USD | 2,670.00 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,480,000.00 USD | 85,010.00 USD | 0.00 USD | `+33.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,490,000.00 USD | 6,080.00 USD | 0.00 USD | `+33.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,500,000.00 USD | 18,400.00 USD | 0.00 USD | `+34.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,570,000.00 USD | 70,850.00 USD | 0.00 USD | `+35.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,590,000.00 USD | 18,000.00 USD | 0.00 USD | `+36.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,810,000.00 USD | 217,560.00 USD | 0.00 USD | `+37.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,820,000.00 USD | 14,250.00 USD | 0.00 USD | `+37.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,830,000.00 USD | 3,980.00 USD | 0.00 USD | `+38.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,870,000.00 USD | 43,240.00 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,870,000.00 USD | 3,330.00 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,880,000.00 USD | 9,200.00 USD | 0.00 USD | `+41.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,910,000.00 USD | 21,720.00 USD | 0.00 USD | `+41.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 8,030,000.00 USD | 128,330.00 USD | 0.00 USD | `+42.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 8,130,000.00 USD | 96,600.00 USD | 0.00 USD | `+43.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,130,000.00 USD | 3,980.00 USD | 0.00 USD | `+44.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,130,000.00 USD | 254.51 USD | 0.00 USD | `+45.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,150,000.00 USD | 12,860.00 USD | 0.00 USD | `+45.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,150,000.00 USD | 3,970.00 USD | 0.00 USD | `+46.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,160,000.00 USD | 8,170.00 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,160,000.00 USD | 843.17 USD | 0.00 USD | `+48.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,170,000.00 USD | 8,390.00 USD | 0.00 USD | `+49.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,170,000.00 USD | 4,420.00 USD | 0.00 USD | `+50.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,170,000.00 USD | 591.89 USD | 0.00 USD | `+51.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,220,000.00 USD | 46,370.00 USD | 0.00 USD | `+52.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,230,000.00 USD | 9,270.00 USD | 0.00 USD | `+53.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,230,000.00 USD | 265.10 USD | 0.00 USD | `+55.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,230,000.00 USD | 2,040.00 USD | 0.00 USD | `+56.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,230,000.00 USD | 807.42 USD | 0.00 USD | `+57.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,250,000.00 USD | 14,120.00 USD | 0.00 USD | `+57.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,250,000.00 USD | 4,010.00 USD | 0.00 USD | `+58.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,250,000.00 USD | 325.54 USD | 0.00 USD | `+59.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,260,000.00 USD | 7,020.00 USD | 0.00 USD | `+60.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,380,000.00 USD | 123,020.00 USD | 0.00 USD | `+61.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,380,000.00 USD | 3,350.00 USD | 0.00 USD | `+62.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,380,000.00 USD | 181.12 USD | 0.00 USD | `+63.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,390,000.00 USD | 382.41 USD | 0.00 USD | `+64.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,390,000.00 USD | 3,420.00 USD | 0.00 USD | `+66.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,390,000.00 USD | 661.93 USD | 0.00 USD | `+66.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,510,000.00 USD | 124,400.00 USD | 0.00 USD | `+68.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,520,000.00 USD | 1,580.00 USD | 0.00 USD | `+69.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,530,000.00 USD | 13,900.00 USD | 0.00 USD | `+70.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,550,000.00 USD | 24,840.00 USD | 0.00 USD | `+72.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,600,000.00 USD | 50,580.00 USD | 0.00 USD | `+73.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,610,000.00 USD | 2,690.00 USD | 0.00 USD | `+74.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,610,000.00 USD | 2,180.00 USD | 0.00 USD | `+76.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,760,000.00 USD | 151,380.00 USD | 0.00 USD | `+78.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,760,000.00 USD | 3,120.00 USD | 0.00 USD | `+82.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,770,000.00 USD | 1,140.00 USD | 0.00 USD | `+83.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,780,000.00 USD | 11,670.00 USD | 0.00 USD | `+84.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,780,000.00 USD | 370.40 USD | 0.00 USD | `+86.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,780,000.00 USD | 733.19 USD | 0.00 USD | `+87.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,780,000.00 USD | 2,410.00 USD | 0.00 USD | `+90.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,780,000.00 USD | 475.00 USD | 0.00 USD | `+90.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,780,000.00 USD | 1,190.00 USD | 0.00 USD | `+91.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,780,000.00 USD | 2,540.00 USD | 0.00 USD | `+92.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,790,000.00 USD | 1,590.00 USD | 0.00 USD | `+93.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,790,000.00 USD | 1,370.00 USD | 0.00 USD | `+94.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,810,000.00 USD | 19,590.00 USD | 0.00 USD | `+94.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,810,000.00 USD | 564.92 USD | 0.00 USD | `+95.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,820,000.00 USD | 8,110.00 USD | 0.00 USD | `+97.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,820,000.00 USD | 3,420.00 USD | 0.00 USD | `+99.79%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `1.11` | 31,160,000.00 USD | 0.00 USD | 31,160,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.11` | 52,480,000.00 USD | 0.00 USD | 52,480,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.11` | 31,140,000.00 USD | 0.00 USD | 31,140,000.00 USD | 18,710.00 USD | 0.00 USD | 121,720.00 USD |
| `1D` | `1.11` | 31,000,000.00 USD | 0.00 USD | 31,000,000.00 USD | 0.00 USD | 2,700.00 USD | 0.00 USD |
| `7D` | `1.11` | 52,460,000.00 USD | 0.00 USD | 52,460,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 31,000,000.00 USD | 0.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 62,820.00 USD |
| `7D` | `1.12` | 52,450,000.00 USD | 0.00 USD | 52,450,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 30,940,000.00 USD | 0.00 USD | 30,940,000.00 USD | 0.00 USD | 47,340.00 USD | 5,360.00 USD |
| `1D` | `1.12` | 30,880,000.00 USD | 0.00 USD | 30,880,000.00 USD | 10,140.00 USD | 2,890.00 USD | 0.00 USD |
| `7D` | `1.12` | 52,370,000.00 USD | 0.00 USD | 52,370,000.00 USD | 17,190.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `1.12` | 30,870,000.00 USD | 0.00 USD | 30,870,000.00 USD | 0.00 USD | 1,530.00 USD | 57,100.00 USD |
| `7D` | `1.12` | 52,350,000.00 USD | 0.00 USD | 52,350,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD |
| `1D` | `1.12` | 30,810,000.00 USD | 0.00 USD | 30,810,000.00 USD | 66,330.00 USD | 29,190.00 USD | 56,030.00 USD |
| `7D` | `1.12` | 52,350,000.00 USD | 0.00 USD | 52,350,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 30,660,000.00 USD | 0.00 USD | 30,660,000.00 USD | 0.00 USD | 783.15 USD | 104,240.00 USD |
| `1D` | `1.13` | 30,550,000.00 USD | 0.00 USD | 30,550,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD |
| `7D` | `1.13` | 52,140,000.00 USD | 0.00 USD | 52,140,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 30,430,000.00 USD | 0.00 USD | 30,430,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD |
| `7D` | `1.13` | 51,950,000.00 USD | 0.00 USD | 51,950,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD |
| `1D` | `1.13` | 30,200,000.00 USD | 0.00 USD | 30,200,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.13` | 51,930,000.00 USD | 0.00 USD | 51,930,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD |
| `1D` | `1.14` | 30,140,000.00 USD | 0.00 USD | 30,140,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.14` | 51,460,000.00 USD | 0.00 USD | 51,460,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD |
| `1D` | `1.14` | 30,090,000.00 USD | 0.00 USD | 30,090,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.14` | 51,210,000.00 USD | 0.00 USD | 51,210,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 30,000,000.00 USD | 0.00 USD | 30,000,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.14` | 51,110,000.00 USD | 0.00 USD | 51,110,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 29,980,000.00 USD | 0.00 USD | 29,980,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD |
| `7D` | `1.14` | 51,100,000.00 USD | 0.00 USD | 51,100,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 29,910,000.00 USD | 0.00 USD | 29,910,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 51,040,000.00 USD | 0.00 USD | 51,040,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.15` | 29,770,000.00 USD | 0.00 USD | 29,770,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 50,920,000.00 USD | 0.00 USD | 50,920,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 50,910,000.00 USD | 0.00 USD | 50,910,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 29,730,000.00 USD | 0.00 USD | 29,730,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 50,770,000.00 USD | 0.00 USD | 50,770,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 50,410,000.00 USD | 0.00 USD | 50,410,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 29,720,000.00 USD | 0.00 USD | 29,720,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 50,250,000.00 USD | 0.00 USD | 50,250,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.16` | 29,520,000.00 USD | 0.00 USD | 29,520,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 49,870,000.00 USD | 0.00 USD | 49,870,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 29,180,000.00 USD | 0.00 USD | 29,180,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD |
| `7D` | `1.16` | 49,220,000.00 USD | 0.00 USD | 49,220,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 29,110,000.00 USD | 0.00 USD | 29,110,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD |
| `7D` | `1.16` | 48,420,000.00 USD | 0.00 USD | 48,420,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 28,790,000.00 USD | 0.00 USD | 28,790,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD |
| `7D` | `1.16` | 47,900,000.00 USD | 0.00 USD | 47,900,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 28,170,000.00 USD | 0.00 USD | 28,170,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD |
| `7D` | `1.16` | 46,870,000.00 USD | 0.00 USD | 46,870,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.17` | 27,550,000.00 USD | 0.00 USD | 27,550,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD |
| `7D` | `1.17` | 45,500,000.00 USD | 0.00 USD | 45,500,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 27,340,000.00 USD | 0.00 USD | 27,340,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD |
| `7D` | `1.17` | 44,870,000.00 USD | 0.00 USD | 44,870,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 27,030,000.00 USD | 0.00 USD | 27,030,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD |
| `7D` | `1.17` | 43,490,000.00 USD | 0.00 USD | 43,490,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 26,860,000.00 USD | 0.00 USD | 26,860,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD |
| `7D` | `1.17` | 41,990,000.00 USD | 0.00 USD | 41,990,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 26,690,000.00 USD | 0.00 USD | 26,690,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD |
| `7D` | `1.17` | 40,600,000.00 USD | 0.00 USD | 40,600,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.18` | 26,440,000.00 USD | 0.00 USD | 26,440,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD |
| `7D` | `1.18` | 39,800,000.00 USD | 0.00 USD | 39,800,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 26,100,000.00 USD | 0.00 USD | 26,100,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD |
| `7D` | `1.18` | 38,920,000.00 USD | 0.00 USD | 38,920,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 25,970,000.00 USD | 0.00 USD | 25,970,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD |
| `7D` | `1.18` | 38,460,000.00 USD | 0.00 USD | 38,460,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 25,790,000.00 USD | 0.00 USD | 25,790,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD |
| `7D` | `1.18` | 37,750,000.00 USD | 0.00 USD | 37,750,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 25,750,000.00 USD | 0.00 USD | 25,750,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD |
| `7D` | `1.18` | 37,370,000.00 USD | 0.00 USD | 37,370,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.19` | 25,640,000.00 USD | 0.00 USD | 25,640,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD |
| `7D` | `1.19` | 37,240,000.00 USD | 0.00 USD | 37,240,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 25,520,000.00 USD | 0.00 USD | 25,520,000.00 USD | 16,710.00 USD | 139,070.00 USD | 324,370.00 USD |
| `7D` | `1.19` | 36,730,000.00 USD | 0.00 USD | 36,730,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD |
| `1D` | `1.19` | 25,040,000.00 USD | 0.00 USD | 25,040,000.00 USD | 239,430.00 USD | 8,930.00 USD | 410,930.00 USD |
| `7D` | `1.19` | 35,960,000.00 USD | 0.00 USD | 35,960,000.00 USD | 182,110.00 USD | 132,500.00 USD | 276,980.00 USD |
| `1D` | `1.19` | 24,380,000.00 USD | 0.00 USD | 24,380,000.00 USD | 48,220.00 USD | 10,480.00 USD | 205,240.00 USD |
| `7D` | `1.19` | 35,370,000.00 USD | 0.00 USD | 35,370,000.00 USD | 152,830.00 USD | 265,920.00 USD | 471,430.00 USD |
| `1D` | `1.19` | 24,110,000.00 USD | 0.00 USD | 24,110,000.00 USD | 25,890.00 USD | 217,630.00 USD | 79,010.00 USD |
| `7D` | `1.19` | 34,480,000.00 USD | 0.00 USD | 34,480,000.00 USD | 218,910.00 USD | 106,640.00 USD | 335,240.00 USD |
| `1D` | `1.20` | 23,790,000.00 USD | 0.00 USD | 23,790,000.00 USD | 15,240.00 USD | 40,110.00 USD | 48,430.00 USD |
| `7D` | `1.20` | 33,820,000.00 USD | 0.00 USD | 33,820,000.00 USD | 381,050.00 USD | 81,170.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 23,690,000.00 USD | 0.00 USD | 23,690,000.00 USD | 21,190.00 USD | 3,620.00 USD | 3,770.00 USD |
| `7D` | `1.20` | 33,060,000.00 USD | 0.00 USD | 33,060,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 23,660,000.00 USD | 0.00 USD | 23,660,000.00 USD | 66,960.00 USD | 22,280.00 USD | 291,610.00 USD |
| `7D` | `1.20` | 32,770,000.00 USD | 0.00 USD | 32,770,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD |
| `1D` | `1.20` | 23,280,000.00 USD | 0.00 USD | 23,280,000.00 USD | 169,810.00 USD | 250,260.00 USD | 180,340.00 USD |
| `7D` | `1.20` | 31,800,000.00 USD | 0.00 USD | 31,800,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 22,680,000.00 USD | 0.00 USD | 22,680,000.00 USD | 102,120.00 USD | 4,970.00 USD | 260,610.00 USD |
| `7D` | `1.20` | 31,320,000.00 USD | 0.00 USD | 31,320,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD |
| `1D` | `1.21` | 22,310,000.00 USD | 0.00 USD | 22,310,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD |
| `7D` | `1.21` | 30,440,000.00 USD | 0.00 USD | 30,440,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 21,810,000.00 USD | 0.00 USD | 21,810,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD |
| `7D` | `1.21` | 30,340,000.00 USD | 0.00 USD | 30,340,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 21,280,000.00 USD | 0.00 USD | 21,280,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD |
| `7D` | `1.21` | 30,240,000.00 USD | 0.00 USD | 30,240,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD |
| `1D` | `1.21` | 20,980,000.00 USD | 0.00 USD | 20,980,000.00 USD | 99,310.00 USD | 425,250.00 USD | 731,080.00 USD |
| `7D` | `1.21` | 28,690,000.00 USD | 0.00 USD | 28,690,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD |
| `1D` | `1.21` | 19,720,000.00 USD | 0.00 USD | 19,720,000.00 USD | 419,060.00 USD | 162,630.00 USD | 699,260.00 USD |
| `7D` | `1.21` | 27,450,000.00 USD | 0.00 USD | 27,450,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.22` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 166,960.00 USD | 8,790.00 USD | 102,180.00 USD |
| `7D` | `1.22` | 27,040,000.00 USD | 0.00 USD | 27,040,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD |
| `1D` | `1.22` | 18,160,000.00 USD | 0.00 USD | 18,160,000.00 USD | 118,950.00 USD | 5,680.00 USD | 470,840.00 USD |
| `7D` | `1.22` | 26,870,000.00 USD | 0.00 USD | 26,870,000.00 USD | 157,620.00 USD | 396,140.00 USD | 396,840.00 USD |
| `1D` | `1.22` | 17,570,000.00 USD | 0.00 USD | 17,570,000.00 USD | 285,170.00 USD | 423,840.00 USD | 178,880.00 USD |
| `7D` | `1.22` | 25,920,000.00 USD | 0.00 USD | 25,920,000.00 USD | 256,390.00 USD | 8,330.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 54,610.00 USD | 42,060.00 USD | 228,420.00 USD |
| `7D` | `1.22` | 25,610,000.00 USD | 0.00 USD | 25,610,000.00 USD | 245,120.00 USD | 10,480.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 16,360,000.00 USD | 0.00 USD | 16,360,000.00 USD | 141,030.00 USD | 525,900.00 USD | 394,250.00 USD |
| `7D` | `1.22` | 25,030,000.00 USD | 0.00 USD | 25,030,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD |
| `1D` | `1.23` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 828,850.00 USD | 352,590.00 USD | 2,750,000.00 USD |
| `7D` | `1.23` | 23,780,000.00 USD | 0.00 USD | 23,780,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD |
| `1D` | `1.23` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 344,500.00 USD | 161,310.00 USD | 1,030,000.00 USD |
| `7D` | `1.23` | 20,890,000.00 USD | 0.00 USD | 20,890,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 105,710.00 USD | 213,020.00 USD | 1,080,000.00 USD |
| `7D` | `1.23` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,790,000.00 USD |
| `1D` | `1.23` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD |
| `7D` | `1.23` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD |
| `1D` | `1.23` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 281,800.00 USD | 336,650.00 USD | 1,030,000.00 USD |
| `7D` | `1.23` | 16,260,000.00 USD | 0.00 USD | 16,260,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD |
| `1D` | `1.24` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 433,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.24` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD |
| `1D` | `1.24` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 267,830.00 USD | 542,950.00 USD | 739,970.00 USD |
| `7D` | `1.24` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD |
| `1D` | `1.24` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD |
| `7D` | `1.24` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD |
| `7D` | `1.24` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD |
| `1D` | `1.24` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 305,740.00 USD | 774,420.00 USD | 560,940.00 USD |
| `7D` | `1.24` | 896,470.00 USD | 0.00 USD | 896,470.00 USD | 896,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD |
| `1D` | `1.25` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD |
| `7D` | `1.25` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD |
| `7D` | `1.25` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD |
| `1D` | `1.25` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 202,510.00 USD | 0.00 USD | 392,980.00 USD |
| `7D` | `1.25` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 532,200.00 USD |
| `7D` | `1.25` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 74,170.00 USD | 0.00 USD | 860,180.00 USD |
| `1D` | `1.25` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD |
| `1D` | `1.26` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 803,540.00 USD | 140,210.00 USD | 193,710.00 USD |
| `1D` | `1.26` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD |
| `7D` | `1.26` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 331,210.00 USD | 66,520.00 USD | 1,690,000.00 USD |
| `7D` | `1.26` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD |
| `1D` | `1.26` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 1,050,000.00 USD | 696,320.00 USD | 1,620,000.00 USD |
| `7D` | `1.26` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 20,010,000.00 USD | 20,010,000.00 USD | 0.00 USD | 367,910.00 USD | 759,740.00 USD | 2,520,000.00 USD |
| `7D` | `1.26` | 25,740,000.00 USD | 25,740,000.00 USD | 0.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 39,860.00 USD | 1,080,000.00 USD | 1,130,000.00 USD |
| `7D` | `1.27` | 39,370,000.00 USD | 39,370,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,640,000.00 USD |
| `1D` | `1.27` | 24,360,000.00 USD | 24,360,000.00 USD | 0.00 USD | 23,990.00 USD | 2,070,000.00 USD | 0.00 USD |
| `7D` | `1.27` | 44,140,000.00 USD | 44,140,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 27,350,000.00 USD | 27,350,000.00 USD | 0.00 USD | 369,350.00 USD | 841,430.00 USD | 1,780,000.00 USD |
| `7D` | `1.27` | 47,780,000.00 USD | 47,780,000.00 USD | 0.00 USD | 1,030,000.00 USD | 2,480,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 30,230,000.00 USD | 30,230,000.00 USD | 0.00 USD | 1,860,000.00 USD | 348,710.00 USD | 676,760.00 USD |
| `7D` | `1.27` | 52,550,000.00 USD | 52,550,000.00 USD | 0.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD |
| `1D` | `1.27` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 778,390.00 USD | 2,410,000.00 USD | 3,350,000.00 USD |
| `7D` | `1.27` | 68,980,000.00 USD | 68,980,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD |
| `1D` | `1.28` | 47,340,000.00 USD | 47,340,000.00 USD | 0.00 USD | 3,100,000.00 USD | 2,940,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 87,260,000.00 USD | 87,260,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 55,070,000.00 USD | 55,070,000.00 USD | 0.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD |
| `7D` | `1.28` | 93,550,000.00 USD | 93,550,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 56,400,000.00 USD | 56,400,000.00 USD | 0.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD |
| `7D` | `1.28` | 94,510,000.00 USD | 94,510,000.00 USD | 0.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 59,260,000.00 USD | 59,260,000.00 USD | 0.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD |
| `7D` | `1.28` | 96,510,000.00 USD | 96,510,000.00 USD | 0.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD |
| `1D` | `1.28` | 61,290,000.00 USD | 61,290,000.00 USD | 0.00 USD | 421,680.00 USD | 611,360.00 USD | 993,120.00 USD |
| `7D` | `1.28` | 100,110,000.00 USD | 100,110,000.00 USD | 0.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD |
| `1D` | `1.29` | 63,200,000.00 USD | 63,200,000.00 USD | 0.00 USD | 726,790.00 USD | 768,570.00 USD | 419,810.00 USD |
| `7D` | `1.29` | 101,270,000.00 USD | 101,270,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 63,520,000.00 USD | 63,520,000.00 USD | 0.00 USD | 210,950.00 USD | 8,830.00 USD | 99,970.00 USD |
| `7D` | `1.29` | 101,390,000.00 USD | 101,390,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 63,830,000.00 USD | 63,830,000.00 USD | 0.00 USD | 151,350.00 USD | 0.00 USD | 157,060.00 USD |
| `7D` | `1.29` | 103,670,000.00 USD | 103,670,000.00 USD | 0.00 USD | 1,060,000.00 USD | 198,070.00 USD | 1,030,000.00 USD |
| `1D` | `1.29` | 66,720,000.00 USD | 66,720,000.00 USD | 0.00 USD | 546,160.00 USD | 195,000.00 USD | 2,140,000.00 USD |
| `7D` | `1.29` | 104,100,000.00 USD | 104,100,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 72,670,000.00 USD | 72,670,000.00 USD | 0.00 USD | 1,810,000.00 USD | 645,070.00 USD | 3,500,000.00 USD |
| `7D` | `1.29` | 113,780,000.00 USD | 113,780,000.00 USD | 0.00 USD | 3,400,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 74,920,000.00 USD | 74,920,000.00 USD | 0.00 USD | 518,910.00 USD | 633,000.00 USD | 1,100,000.00 USD |
| `7D` | `1.30` | 115,010,000.00 USD | 115,010,000.00 USD | 0.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 75,640,000.00 USD | 75,640,000.00 USD | 0.00 USD | 321,680.00 USD | 109,620.00 USD | 291,610.00 USD |
| `7D` | `1.30` | 117,070,000.00 USD | 117,070,000.00 USD | 0.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD |
| `1D` | `1.30` | 77,770,000.00 USD | 77,770,000.00 USD | 0.00 USD | 443,890.00 USD | 332,000.00 USD | 1,350,000.00 USD |
| `7D` | `1.30` | 118,740,000.00 USD | 118,740,000.00 USD | 0.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 79,490,000.00 USD | 79,490,000.00 USD | 0.00 USD | 587,440.00 USD | 869,380.00 USD | 260,610.00 USD |
| `7D` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 80,760,000.00 USD | 80,760,000.00 USD | 0.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD |
| `7D` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD |
| `1D` | `1.31` | 83,050,000.00 USD | 83,050,000.00 USD | 0.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD |
| `7D` | `1.31` | 124,840,000.00 USD | 124,840,000.00 USD | 0.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 86,290,000.00 USD | 86,290,000.00 USD | 0.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD |
| `7D` | `1.31` | 129,300,000.00 USD | 129,300,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD |
| `1D` | `1.31` | 88,610,000.00 USD | 88,610,000.00 USD | 0.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD |
| `7D` | `1.31` | 132,560,000.00 USD | 132,560,000.00 USD | 0.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD |
| `1D` | `1.31` | 91,540,000.00 USD | 91,540,000.00 USD | 0.00 USD | 1,320,000.00 USD | 664,910.00 USD | 944,450.00 USD |
| `7D` | `1.31` | 135,400,000.00 USD | 135,400,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 94,470,000.00 USD | 94,470,000.00 USD | 0.00 USD | 372,630.00 USD | 454,810.00 USD | 2,110,000.00 USD |
| `7D` | `1.31` | 137,860,000.00 USD | 137,860,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 100,980,000.00 USD | 100,980,000.00 USD | 0.00 USD | 1,320,000.00 USD | 1,640,000.00 USD | 3,550,000.00 USD |
| `7D` | `1.32` | 142,480,000.00 USD | 142,480,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 106,060,000.00 USD | 106,060,000.00 USD | 0.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD |
| `7D` | `1.32` | 145,560,000.00 USD | 145,560,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 109,560,000.00 USD | 109,560,000.00 USD | 0.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD |
| `7D` | `1.32` | 147,390,000.00 USD | 147,390,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 114,150,000.00 USD | 114,150,000.00 USD | 0.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD |
| `7D` | `1.32` | 151,850,000.00 USD | 151,850,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 116,150,000.00 USD | 116,150,000.00 USD | 0.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD |
| `7D` | `1.32` | 154,220,000.00 USD | 154,220,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 118,680,000.00 USD | 118,680,000.00 USD | 0.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD |
| `7D` | `1.33` | 154,760,000.00 USD | 154,760,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 120,920,000.00 USD | 120,920,000.00 USD | 0.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD |
| `7D` | `1.33` | 155,910,000.00 USD | 155,910,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 123,770,000.00 USD | 123,770,000.00 USD | 0.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD |
| `7D` | `1.33` | 157,630,000.00 USD | 157,630,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 126,160,000.00 USD | 126,160,000.00 USD | 0.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD |
| `7D` | `1.33` | 161,680,000.00 USD | 161,680,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 128,240,000.00 USD | 128,240,000.00 USD | 0.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD |
| `7D` | `1.33` | 162,230,000.00 USD | 162,230,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 130,220,000.00 USD | 130,220,000.00 USD | 0.00 USD | 829,900.00 USD | 219,260.00 USD | 927,340.00 USD |
| `7D` | `1.34` | 164,180,000.00 USD | 164,180,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 132,490,000.00 USD | 132,490,000.00 USD | 0.00 USD | 1,010,000.00 USD | 331,250.00 USD | 927,070.00 USD |
| `7D` | `1.34` | 166,520,000.00 USD | 166,520,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 134,360,000.00 USD | 134,360,000.00 USD | 0.00 USD | 892,570.00 USD | 387,310.00 USD | 592,540.00 USD |
| `7D` | `1.34` | 171,230,000.00 USD | 171,230,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 137,610,000.00 USD | 137,610,000.00 USD | 0.00 USD | 1,410,000.00 USD | 693,530.00 USD | 1,150,000.00 USD |
| `7D` | `1.34` | 176,870,000.00 USD | 176,870,000.00 USD | 0.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD |
| `1D` | `1.34` | 139,380,000.00 USD | 139,380,000.00 USD | 0.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD |
| `7D` | `1.34` | 187,840,000.00 USD | 187,840,000.00 USD | 0.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 140,420,000.00 USD | 140,420,000.00 USD | 0.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD |
| `7D` | `1.35` | 194,780,000.00 USD | 194,780,000.00 USD | 0.00 USD | 2,310,000.00 USD | 2,170,000.00 USD | 2,460,000.00 USD |
| `1D` | `1.35` | 141,910,000.00 USD | 141,910,000.00 USD | 0.00 USD | 749,450.00 USD | 149,380.00 USD | 591,590.00 USD |
| `7D` | `1.35` | 205,030,000.00 USD | 205,030,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,640,000.00 USD | 4,310,000.00 USD |
| `1D` | `1.35` | 142,940,000.00 USD | 142,940,000.00 USD | 0.00 USD | 471,590.00 USD | 126,450.00 USD | 425,480.00 USD |
| `7D` | `1.35` | 212,740,000.00 USD | 212,740,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 144,360,000.00 USD | 144,360,000.00 USD | 0.00 USD | 597,310.00 USD | 312,930.00 USD | 511,530.00 USD |
| `7D` | `1.35` | 221,000,000.00 USD | 221,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,160,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 145,150,000.00 USD | 145,150,000.00 USD | 0.00 USD | 142,180.00 USD | 79,810.00 USD | 571,660.00 USD |
| `7D` | `1.35` | 229,230,000.00 USD | 229,230,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 146,090,000.00 USD | 146,090,000.00 USD | 0.00 USD | 391,410.00 USD | 17,220.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 233,320,000.00 USD | 233,320,000.00 USD | 0.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 146,430,000.00 USD | 146,430,000.00 USD | 0.00 USD | 213,710.00 USD | 42,480.00 USD | 84,480.00 USD |
| `7D` | `1.36` | 237,110,000.00 USD | 237,110,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 147,180,000.00 USD | 147,180,000.00 USD | 0.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD |
| `7D` | `1.36` | 239,240,000.00 USD | 239,240,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 147,520,000.00 USD | 147,520,000.00 USD | 0.00 USD | 171,250.00 USD | 2,700.00 USD | 166,760.00 USD |
| `7D` | `1.36` | 243,340,000.00 USD | 243,340,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 147,630,000.00 USD | 147,630,000.00 USD | 0.00 USD | 0.00 USD | 26,460.00 USD | 88,450.00 USD |
| `7D` | `1.36` | 245,060,000.00 USD | 245,060,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 147,960,000.00 USD | 147,960,000.00 USD | 0.00 USD | 53,740.00 USD | 104,420.00 USD | 171,320.00 USD |
| `7D` | `1.37` | 245,550,000.00 USD | 245,550,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 148,160,000.00 USD | 148,160,000.00 USD | 0.00 USD | 126,110.00 USD | 2,890.00 USD | 68,720.00 USD |
| `7D` | `1.37` | 246,960,000.00 USD | 246,960,000.00 USD | 0.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 148,360,000.00 USD | 148,360,000.00 USD | 0.00 USD | 7,080.00 USD | 67,780.00 USD | 119,540.00 USD |
| `7D` | `1.37` | 248,150,000.00 USD | 248,150,000.00 USD | 0.00 USD | 351,750.00 USD | 372,470.00 USD | 461,160.00 USD |
| `1D` | `1.37` | 148,560,000.00 USD | 148,560,000.00 USD | 0.00 USD | 75,340.00 USD | 1,780.00 USD | 126,860.00 USD |
| `7D` | `1.37` | 250,620,000.00 USD | 250,620,000.00 USD | 0.00 USD | 821,620.00 USD | 376,730.00 USD | 1,270,000.00 USD |
| `1D` | `1.38` | 148,840,000.00 USD | 148,840,000.00 USD | 0.00 USD | 120,880.00 USD | 30,080.00 USD | 125,000.00 USD |
| `7D` | `1.38` | 252,420,000.00 USD | 252,420,000.00 USD | 0.00 USD | 536,130.00 USD | 295,850.00 USD | 966,400.00 USD |
| `1D` | `1.38` | 149,230,000.00 USD | 149,230,000.00 USD | 0.00 USD | 93,260.00 USD | 50,590.00 USD | 254,190.00 USD |
| `7D` | `1.38` | 253,910,000.00 USD | 253,910,000.00 USD | 0.00 USD | 617,230.00 USD | 329,740.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 149,710,000.00 USD | 149,710,000.00 USD | 0.00 USD | 195,140.00 USD | 100,700.00 USD | 182,120.00 USD |
| `7D` | `1.38` | 256,010,000.00 USD | 256,010,000.00 USD | 0.00 USD | 579,450.00 USD | 256,720.00 USD | 1,260,000.00 USD |
| `1D` | `1.38` | 149,790,000.00 USD | 149,790,000.00 USD | 0.00 USD | 12,100.00 USD | 65,520.00 USD | 0.00 USD |
| `7D` | `1.38` | 258,560,000.00 USD | 258,560,000.00 USD | 0.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 149,960,000.00 USD | 149,960,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD |
| `7D` | `1.38` | 259,650,000.00 USD | 259,650,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.39` | 150,010,000.00 USD | 150,010,000.00 USD | 0.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.39` | 260,930,000.00 USD | 260,930,000.00 USD | 0.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 150,070,000.00 USD | 150,070,000.00 USD | 0.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.39` | 261,480,000.00 USD | 261,480,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD |
| `1D` | `1.39` | 150,160,000.00 USD | 150,160,000.00 USD | 0.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.39` | 262,580,000.00 USD | 262,580,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 262,740,000.00 USD | 262,740,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 150,180,000.00 USD | 150,180,000.00 USD | 0.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 263,070,000.00 USD | 263,070,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.40` | 263,240,000.00 USD | 263,240,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 263,360,000.00 USD | 263,360,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 263,370,000.00 USD | 263,370,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 263,500,000.00 USD | 263,500,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 263,620,000.00 USD | 263,620,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 263,860,000.00 USD | 263,860,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 264,030,000.00 USD | 264,030,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 264,410,000.00 USD | 264,410,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `7D` | `1.41` | 265,050,000.00 USD | 265,050,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `7D` | `1.41` | 265,230,000.00 USD | 265,230,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `7D` | `1.42` | 265,850,000.00 USD | 265,850,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `7D` | `1.42` | 266,380,000.00 USD | 266,380,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `7D` | `1.42` | 267,400,000.00 USD | 267,400,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.42` | 268,780,000.00 USD | 268,780,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `7D` | `1.42` | 269,400,000.00 USD | 269,400,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 269,760,000.00 USD | 269,760,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 270,780,000.00 USD | 270,780,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 272,290,000.00 USD | 272,290,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 273,680,000.00 USD | 273,680,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 274,480,000.00 USD | 274,480,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 275,010,000.00 USD | 275,010,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 275,360,000.00 USD | 275,360,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 275,810,000.00 USD | 275,810,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 276,530,000.00 USD | 276,530,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 276,900,000.00 USD | 276,900,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 277,030,000.00 USD | 277,030,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 277,160,000.00 USD | 277,160,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 277,490,000.00 USD | 277,490,000.00 USD | 0.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 278,100,000.00 USD | 278,100,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 278,660,000.00 USD | 278,660,000.00 USD | 0.00 USD | 182,110.00 USD | 128,180.00 USD | 249,400.00 USD |
| `7D` | `1.46` | 279,120,000.00 USD | 279,120,000.00 USD | 0.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `7D` | `1.46` | 279,280,000.00 USD | 279,280,000.00 USD | 0.00 USD | 85,350.00 USD | 50,790.00 USD | 20,990.00 USD |
| `7D` | `1.46` | 279,750,000.00 USD | 279,750,000.00 USD | 0.00 USD | 119,110.00 USD | 55,850.00 USD | 296,470.00 USD |
| `7D` | `1.46` | 279,960,000.00 USD | 279,960,000.00 USD | 0.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.83B` | Total OI Tokens: `2,251,062,697.2 XRP`
  * 1h OI Change: `+1.16%` | 4h OI Change: `+4.26%` | 24h OI Change: `-2.62%`
  * Exchange Breakdown: Binance=`438.61M` | Bybit=`316.84M` | OKX=`94.13M` | Hyperliquid=`199.66M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-102.89K` | Last 24h: `81.98K` | Last 3d: `547.43K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0032%` | **USDT OKX** | `-0.0125%` |
| **USDT Bybit** | `-0.0392%` | **USDT KuCoin** | `-0.0039%` |
| **USDT MEXC** | `0.0032%` | **USDT BingX** | `0.0032%` |
| **USDT Gate** | `-0.0018%` | **USDT Bitget** | `-0.0042%` |
| **CoinM Binance** | `0.0106%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `56.10%` | `43.90%` | `1.28` | 535,710,000.00 USD |
| `15M` | `Binance` | `57.78%` | `42.22%` | `1.37` | 182,780,000.00 USD |
| `15M` | `OKX` | `54.51%` | `45.49%` | `1.20` | 125,610,000.00 USD |
| `15M` | `Bybit` | `61.79%` | `38.21%` | `1.62` | 31,960,000.00 USD |
| `15M` | `KuCoin` | `55.15%` | `44.85%` | `1.23` | 1,630,000.00 USD |
| `15M` | `Gate` | `50.16%` | `49.84%` | `1.01` | 82,100,000.00 USD |
| `15M` | `Bitget` | `54.28%` | `45.72%` | `1.19` | 24,320,000.00 USD |
| `15M` | `BingX` | `71.16%` | `28.84%` | `2.47` | 6,800,000.00 USD |
| `15M` | `MEXC` | `56.51%` | `43.49%` | `1.30` | 14,470,000.00 USD |
| `15M` | `Bitunix` | `53.69%` | `46.31%` | `1.16` | 23,120,000.00 USD |
| `15M` | `Hyperliquid` | `64.7%` | `35.3%` | `1.83` | 7,560,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `25.17%` | `74.83%` | `0.34` | 1,440,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `27.4%` | `72.6%` | `0.38` | 4,490,000.00 USD |
| `15M` | `HTX` | `81.16%` | `18.84%` | `4.31` | 12,660,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `55.48%` | `44.52%` | `1.25` | 1,550,000.00 USD |
| `15M` | `Bitfinex` | `34.37%` | `65.63%` | `0.52` | 166,650.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `50.77%` | `49.23%` | `1.03` | 3,110,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.65%` | `43.35%` | `1.31` | 11,950,000.00 USD |
| `15M` | `Whale Positions` | `57.78%` | `42.22%` | `1.37` | 182,780,000.00 USD |
| `15M` | `Global Accounts` | `56.10%` | `43.90%` | `1.28` | 535,710,000.00 USD |
| `1H` | `XRP` | `53.61%` | `46.39%` | `1.16` | 2,180,000,000.00 USD |
| `1H` | `Binance` | `52.89%` | `47.11%` | `1.12` | 707,040,000.00 USD |
| `1H` | `OKX` | `52.87%` | `47.13%` | `1.12` | 465,210,000.00 USD |
| `1H` | `Bybit` | `54.4%` | `45.6%` | `1.19` | 147,870,000.00 USD |
| `1H` | `KuCoin` | `63.83%` | `36.17%` | `1.76` | 6,970,000.00 USD |
| `1H` | `Gate` | `48.52%` | `51.48%` | `0.94` | 333,330,000.00 USD |
| `1H` | `Bitget` | `55.7%` | `44.3%` | `1.26` | 130,490,000.00 USD |
| `1H` | `BingX` | `56.97%` | `43.03%` | `1.32` | 21,250,000.00 USD |
| `1H` | `MEXC` | `54.95%` | `45.05%` | `1.22` | 53,520,000.00 USD |
| `1H` | `Bitunix` | `50.08%` | `49.92%` | `1.00` | 88,890,000.00 USD |
| `1H` | `Hyperliquid` | `57.37%` | `42.63%` | `1.35` | 46,420,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.39%` | `41.61%` | `1.40` | 12,790,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `38.46%` | `61.54%` | `0.62` | 26,860,000.00 USD |
| `1H` | `HTX` | `84.67%` | `15.33%` | `5.52` | 78,050,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `59.28%` | `40.72%` | `1.46` | 8,670,000.00 USD |
| `1H` | `Bitfinex` | `36.7%` | `63.3%` | `0.58` | 1,030,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `61.28%` | `38.72%` | `1.58` | 17,360,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.47%` | `51.53%` | `0.94` | 30,700,000.00 USD |
| `1H` | `Whale Positions` | `52.89%` | `47.11%` | `1.12` | 707,040,000.00 USD |
| `1H` | `Global Accounts` | `53.61%` | `46.39%` | `1.16` | 2,180,000,000.00 USD |
| `4H` | `XRP` | `49.35%` | `50.65%` | `0.97` | 12,950,000,000.00 USD |
| `4H` | `Binance` | `49.43%` | `50.57%` | `0.98` | 4,070,000,000.00 USD |
| `4H` | `OKX` | `49.46%` | `50.54%` | `0.98` | 2,450,000,000.00 USD |
| `4H` | `Bybit` | `51.62%` | `48.38%` | `1.07` | 872,800,000.00 USD |
| `4H` | `KuCoin` | `60.82%` | `39.18%` | `1.55` | 149,290,000.00 USD |
| `4H` | `Gate` | `49.27%` | `50.73%` | `0.97` | 1,620,000,000.00 USD |
| `4H` | `Bitget` | `52.26%` | `47.74%` | `1.09` | 529,000,000.00 USD |
| `4H` | `BingX` | `52.64%` | `47.36%` | `1.11` | 106,690,000.00 USD |
| `4H` | `MEXC` | `50.68%` | `49.32%` | `1.03` | 394,240,000.00 USD |
| `4H` | `Bitunix` | `50.72%` | `49.28%` | `1.03` | 458,250,000.00 USD |
| `4H` | `Hyperliquid` | `56.93%` | `43.07%` | `1.32` | 581,290,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `56.93%` | `43.07%` | `1.32` | 51,960,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `35.75%` | `64.25%` | `0.56` | 1,100,000,000.00 USD |
| `4H` | `HTX` | `69.26%` | `30.74%` | `2.25` | 189,230,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.89%` | `49.11%` | `1.04` | 70,400,000.00 USD |
| `4H` | `Bitfinex` | `28.77%` | `71.23%` | `0.40` | 9,600,000.00 USD |
| `4H` | `Kraken` | `38.91%` | `61.09%` | `0.64` | 23,820,000.00 USD |
| `4H` | `Aster` | `50.98%` | `49.02%` | `1.04` | 114,290,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.46%` | `55.54%` | `0.80` | 156,520,000.00 USD |
| `4H` | `Whale Positions` | `49.43%` | `50.57%` | `0.98` | 4,070,000,000.00 USD |
| `4H` | `Global Accounts` | `49.35%` | `50.65%` | `0.97` | 12,950,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.21` | `1.21` | `1.21` | `1.22` | `1.21` | 14,612,277.95 USD | 7,327,776.10 USD | 7,284,501.85 USD | 43,274.26 USD | `+0.30%` | `14B / 9S` |
| `5:00 UTC` | `1.22` | `1.22` | `1.22` | `1.22` | `1.21` | 14,809,006.05 USD | 8,905,687.74 USD | 5,903,318.31 USD | 3,002,369.44 USD | `+20.27%` | `27B / 5S` |
| `0:00 UTC` | `1.22` | `1.22` | `1.22` | `1.23` | `1.22` | 11,190,777.85 USD | 5,458,091.58 USD | 5,732,686.27 USD | -274,594.69 USD | `-2.45%` | `2B / 5S` |
| `5:00 UTC` | `1.22` | `1.22` | `1.22` | `1.22` | `1.22` | 9,740,915.81 USD | 4,726,774.90 USD | 5,014,140.91 USD | -287,366.00 USD | `-2.95%` | `9B / 19S` |
| `0:00 UTC` | `1.23` | `1.23` | `1.23` | `1.23` | `1.22` | 10,276,393.47 USD | 5,352,457.47 USD | 4,923,936.00 USD | 428,521.46 USD | `+4.17%` | `12B / 9S` |
| `5:00 UTC` | `1.23` | `1.23` | `1.23` | `1.23` | `1.22` | 7,441,662.05 USD | 4,516,863.46 USD | 2,924,798.59 USD | 1,592,064.87 USD | `+21.39%` | `27B / 7S` |
| `0:00 UTC` | `1.24` | `1.24` | `1.24` | `1.24` | `1.23` | 14,534,365.59 USD | 7,960,789.37 USD | 6,573,576.22 USD | 1,387,213.15 USD | `+9.54%` | `20B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.24` | 13,408,965.14 USD | 7,227,260.97 USD | 6,181,704.17 USD | 1,045,556.80 USD | `+7.80%` | `8B / 3S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.25` | `1.24` | 11,613,568.18 USD | 6,301,411.52 USD | 5,312,156.67 USD | 989,254.85 USD | `+8.52%` | `26B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 10,302,361.55 USD | 4,741,417.22 USD | 5,560,944.33 USD | -819,527.11 USD | `-7.95%` | `6B / 6S` |

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
| `5m` | 590,550.00 USD | 1,800,000.00 USD | **`ACCUMULATION`** |
| `15m` | 817,570.00 USD | 2,930,000.00 USD | **`ACCUMULATION`** |
| `30m` | 2,680,000.00 USD | 5,840,000.00 USD | **`ACCUMULATION`** |
| `1h` | 9,460,000.00 USD | 14,320,000.00 USD | **`ACCUMULATION`** |
| `2h` | 12,700,000.00 USD | 19,820,000.00 USD | **`ACCUMULATION`** |
| `4h` | 14,450,000.00 USD | 9,410,000.00 USD | **`ACCUMULATION`** |
| `6h` | -19,070,000.00 USD | -11,500,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -43,700,000.00 USD | -111,010,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -58,950,000.00 USD | -136,740,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -55,320,000.00 USD | -135,320,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -126,350,000.00 USD | -222,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -600,570,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+590.55K` | 15m=`+817.57K` | 1h=`+9.46M` | 24h=`-55.32M`
* Futures Capital Netflows: 5m=`+1.80M` | 15m=`+2.93M` | 1h=`+14.32M` | 24h=`-135.32M`
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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0144` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `4.24`
  * Mathematical Lot Sizing: **`8.29 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.47` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `-1.75`
  * Mathematical Lot Sizing: **`8.29 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
