# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.25` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.26` | Lower -3.00σ Band: `1.25`
  * Upper +2.51σ Band: `1.26` | Lower -2.51σ Band: `1.25`
  * Upper +2.01σ Band: `1.26` | Lower -2.01σ Band: `1.25`
  * Upper +2.00σ Band: `1.26` | Lower -2.00σ Band: `1.25`
  * Upper +1.28σ Band: `1.26` | Lower -1.28σ Band: `1.25`
  * Upper +1.00σ Band: `1.26` | Lower -1.00σ Band: `1.25`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.25`
  * Institutional Anchors: EMA-144=`1.25` | EMA-200=`1.25` (Slope: `+0.0000`) | EMA-233=`1.25`
- **Range Boundaries**: 24H High=`1.27` | 24H Low=`1.24` | Weekly High=`1.28` | Weekly Low=`1.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.41%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.44%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+1.80%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.27` | Low=`1.24`
  * New York Session (13:00-21:00 UTC): High=`1.25` | Low=`1.24`
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
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,403,876` | 1,763,981.10 USD | -52,647.86 USD | `-2.98%` | -42,535,504.45 USD | `+0.28` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `1.26` | `1.26` | `1.25` | `1.25` | `970,250` | 1,217,595.83 USD | -80,674.26 USD | `-6.63%` | -42,616,178.71 USD | `+0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.25` | `1.26` | `1.25` | `1.26` | `669,550` | 840,313.14 USD | 73,636.66 USD | `+8.76%` | -42,542,542.05 USD | `+0.46` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.25` | `1.24` | `1.25` | `6,024,899` | 7,510,859.07 USD | -893,786.33 USD | `-11.90%` | -43,607,456.38 USD | `-0.64` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.26` | `8,798,021` | 11,036,044.54 USD | 1,314,492.40 USD | `+11.91%` | -42,292,963.98 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.26` | `1.26` | `1.25` | `1.26` | `1,646,779` | 2,066,681.51 USD | -2,930.17 USD | `-0.14%` | -42,295,894.15 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `20,218,037` | 25,337,061.54 USD | 668,152.80 USD | `+2.64%` | -40,542,234.62 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.26` | `1.26` | `1.25` | `1.25` | `24,012,060` | 30,200,518.12 USD | -808,085.55 USD | `-2.68%` | -41,350,320.17 USD | `+0.13` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.25` | `1.26` | `1.24` | `1.26` | `21,949,750` | 27,460,575.65 USD | -949,596.16 USD | `-3.46%` | -42,299,916.34 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `66,176,996` | 82,994,573.63 USD | -1,093,110.60 USD | `-1.32%` | -40,374,639.53 USD | `+0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -13,549,801.29 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -41,639,935.50 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `66,176,996` | 82,994,573.63 USD | -1,093,110.60 USD | `-1.32%` | -40,374,639.53 USD | `+0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `1.25` | `281879.0000` | 353,758.14 USD | 1,915,299.30 USD | `5 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `26873.0000` | 33,722.93 USD | 1,949,022.23 USD | `5 orders` | `-0.16%` | `-` |
| `ASK` | `1.26` | `621497.0000` | 782,340.42 USD | 3,166,122.21 USD | `6 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `16314.0000` | 20,534.43 USD | 2,383,781.79 USD | `2 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `243657.0000` | 306,666.70 USD | 2,363,247.36 USD | `3 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `42679.0000` | 53,711.52 USD | 2,056,580.66 USD | `6 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `39902.0000` | 50,212.68 USD | 2,002,869.13 USD | `6 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `249495.0000` | 313,939.56 USD | 1,952,656.46 USD | `4 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `358012.0000` | 450,450.70 USD | 1,638,716.90 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `255760.0000` | 321,771.66 USD | 1,188,266.20 USD | `5 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `132347.0000` | 166,492.53 USD | 866,494.54 USD | `10 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `102301.0000` | 128,684.43 USD | 700,002.02 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `31313.0000` | 39,385.49 USD | 571,317.59 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `52482.0000` | 66,006.61 USD | 531,932.10 USD | `3 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `71318.0000` | 89,689.52 USD | 465,925.49 USD | `14 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `71186.0000` | 89,516.40 USD | 376,235.97 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `26224.0000` | 32,974.06 USD | 286,719.58 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `90375.0000` | 113,628.49 USD | 253,745.52 USD | `13 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `68210.0000` | 85,753.61 USD | 140,117.03 USD | `13 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `25841.0000` | 32,484.72 USD | 54,363.42 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `10963.0000` | 13,780.49 USD | 21,878.70 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `1.26` | `6443.0000` | 8,098.21 USD | 8,098.21 USD | `4 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `10804.0000` | 13,578.47 USD | 13,578.47 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `1.26` | `7213.0000` | 9,064.58 USD | 22,643.04 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `3384.0000` | 4,252.33 USD | 26,895.38 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `34950.0000` | 43,914.67 USD | 70,810.05 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `9875.0000` | 12,406.95 USD | 83,217.00 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `29938.0000` | 37,611.11 USD | 120,828.11 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `21818.0000` | 27,407.77 USD | 148,235.88 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `53679.0000` | 67,426.19 USD | 215,662.08 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `18788.0000` | 23,597.73 USD | 239,259.80 USD | `4 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `127349.0000` | 159,937.61 USD | 399,197.41 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `52711.0000` | 66,194.47 USD | 465,391.89 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `45132.0000` | 56,672.25 USD | 522,064.14 USD | `4 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `33175.0000` | 41,654.53 USD | 563,718.67 USD | `6 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `82454.0000` | 103,521.00 USD | 667,239.67 USD | `4 orders` | `-0.11%` | `-` |
| `BID` | `1.26` | `256456.0000` | 321,954.86 USD | 989,194.53 USD | `4 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `18505.0000` | 23,229.33 USD | 1,012,423.86 USD | `4 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `60333.0000` | 75,729.98 USD | 1,088,153.84 USD | `6 orders` | `-0.13%` | `-` |
| `BID` | `1.26` | `377171.0000` | 473,387.32 USD | 1,561,541.16 USD | `8 orders` | `-0.14%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 44,034,507.51 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,455,624.24 USD | `+10.12%` | `10X Cross` |
| `95` | `0x5b5d...c060` | `SHORT` | 19,490,627.33 USD | `15,519,251.00` | `1.44` | `1.26` | `10.79` | 2,786,660.98 USD | `+14.30%` | `5X Cross` |
| `165` | `0xb83d...6e36` | `SHORT` | 12,454,331.00 USD | `9,905,616.00` | `1.50` | `1.26` | `11.86` | 2,394,140.55 USD | `+19.22%` | `5X Cross` |
| `339` | `0x58f0...0d20` | `LONG` | 6,671,083.78 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 68,240.28 USD | `+1.02%` | `20X Cross` |
| `377` | `0xecb6...2b00` | `SHORT` | 6,055,564.01 USD | `4,821,117.00` | `1.27` | `1.26` | `7.95` | 61,112.98 USD | `+1.01%` | `10X Cross` |
| `426` | `0xca49...53c8` | `SHORT` | 5,198,647.76 USD | `4,138,886.00` | `1.44` | `1.26` | `4.89` | 754,674.97 USD | `+14.52%` | `20X Cross` |
| `438` | `0xdd53...2b13` | `SHORT` | 5,022,092.13 USD | `3,998,914.00` | `1.40` | `1.26` | `16.66` | 574,783.98 USD | `+11.45%` | `3X Cross` |
| `499` | `0x610b...b613` | `LONG` | 4,455,094.52 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8351` | -644,898.09 USD | `-14.48%` | `5X Cross` |
| `583` | `0x9946...0852` | `SHORT` | 3,856,219.60 USD | `3,070,483.00` | `1.40` | `1.26` | `1.76` | 452,282.62 USD | `+11.73%` | `20X Cross` |
| `642` | `0xc30c...a4c9` | `SHORT` | 3,508,934.35 USD | `2,791,515.00` | `1.41` | `1.26` | `1.59` | 427,578.38 USD | `+12.19%` | `8X Cross` |
| `647` | `0xc179...e0c8` | `SHORT` | 3,477,732.40 USD | `2,768,785.00` | `1.27` | `1.26` | `3.38` | 30,684.49 USD | `+0.88%` | `10X Cross` |
| `652` | `0xfc27...9d9d` | `SHORT` | 3,448,717.73 USD | `2,746,013.00` | `1.29` | `1.26` | `8.15` | 102,466.19 USD | `+2.97%` | `20X Cross` |
| `693` | `0xf48f...10fe` | `LONG` | 3,225,953.94 USD | `2,565,779.00` | `1.53` | `1.26` | `1.00` | -698,686.79 USD | `-21.66%` | `4X Cross` |
| `736` | `0x023a...2355` | `SHORT` | 3,093,241.15 USD | `2,463,360.00` | `1.32` | `1.26` | `3.33` | 157,687.10 USD | `+5.10%` | `20X Cross` |
| `739` | `0x45d2...4029` | `SHORT` | 3,080,722.70 USD | `2,453,000.00` | `1.48` | `1.26` | `18.43` | 557,557.72 USD | `+18.10%` | `20X Cross` |
| `1066` | `0xeadc...9d55` | `LONG` | 2,033,503.20 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 74,660.17 USD | `+3.67%` | `20X Cross` |
| `1138` | `0x94b2...599e` | `SHORT` | 1,934,189.76 USD | `1,540,696.00` | `1.36` | `1.26` | `1.87` | 166,276.69 USD | `+8.60%` | `20X Cross` |
| `1156` | `0x3fc5...c0c1` | `SHORT` | 1,900,608.56 USD | `1,511,779.00` | `1.52` | `1.26` | `2.39` | 391,006.04 USD | `+20.57%` | `20X Cross` |
| `1192` | `0x31ef...f715` | `LONG` | 1,852,552.97 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -346,712.43 USD | `-18.72%` | `3X Isolated` |
| `1239` | `0x7737...bf66` | `SHORT` | 1,775,171.95 USD | `1,413,466.00` | `1.41` | `1.26` | `14.04` | 223,696.70 USD | `+12.60%` | `10X Cross` |
| `1299` | `0x95da...2328` | `LONG` | 1,662,851.87 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0771` | -130,789.23 USD | `-7.87%` | `5X Cross` |
| `1313` | `0xee2b...d67e` | `LONG` | 1,640,300.82 USD | `1,306,284.00` | `1.55` | `1.26` | `0.4412` | -390,354.08 USD | `-23.80%` | `4X Cross` |
| `1363` | `0x215d...f80a` | `LONG` | 1,572,106.73 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -82,347.49 USD | `-5.24%` | `14X Cross` |
| `1374` | `0x5fa3...35b7` | `SHORT` | 1,558,319.69 USD | `1,240,651.00` | `1.30` | `1.26` | `2.63` | 58,172.44 USD | `+3.73%` | `20X Cross` |
| `1416` | `0x123d...3bff` | `LONG` | 1,523,465.66 USD | `1,211,889.00` | `1.35` | `1.26` | `0.000000` | -108,969.82 USD | `-7.15%` | `10X Cross` |
| `1436` | `0xbcd4...0dd2` | `SHORT` | 1,503,768.35 USD | `1,196,125.00` | `1.31` | `1.26` | `2.00` | 63,898.89 USD | `+4.25%` | `20X Cross` |
| `1550` | `0xdf95...7d72` | `SHORT` | 1,381,585.77 USD | `1,099,726.00` | `1.37` | `1.26` | `36.54` | 128,013.03 USD | `+9.27%` | `20X Cross` |
| `1580` | `0x7fda...17d1` | `LONG` | 1,345,591.52 USD | `1,071,075.00` | `1.22` | `1.26` | `0.000000` | 40,450.92 USD | `+3.01%` | `20X Cross` |
| `1613` | `0xef96...9383` | `SHORT` | 1,302,902.58 USD | `1,036,765.00` | `1.34` | `1.26` | `4.61` | 84,616.77 USD | `+6.49%` | `20X Cross` |
| `1637` | `0xb1ce...681b` | `LONG` | 1,283,233.41 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -240,823.09 USD | `-18.77%` | `4X Isolated` |
| `1747` | `0x3c36...461a` | `LONG` | 1,180,986.07 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -38,094.54 USD | `-3.23%` | `10X Cross` |
| `1882` | `0x2577...4897` | `SHORT` | 1,080,608.70 USD | `860,323.00` | `1.24` | `1.26` | `5.15` | -10,004.03 USD | `-0.93%` | `20X Cross` |
| `1995` | `0xbfc7...80b4` | `SHORT` | 1,004,720.00 USD | `800,000.00` | `1.48` | `1.26` | `3.17` | 178,734.65 USD | `+17.79%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `1.29` | 29,134.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 29.13K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,953.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.95K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 38,693.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 38.69K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 17,223.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 17.22K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,439.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.44K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 12,657.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 12.66K USD at 1.2924 USD [API] | `2026-10-29 18:11:20` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,407.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.41K USD at 1.2835 USD [API] | `2026-10-29 18:34:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,320.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.32K USD at 1.2835 USD [API] | `2026-10-29 18:34:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,004.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.2835 USD [API] | `2026-10-29 18:34:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 7,794.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.79K USD at 1.2813 USD [API] | `2026-10-29 18:36:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 165.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.17K USD at 1.2854 USD [API] | `2026-10-29 18:31:36` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 614.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.61K USD at 1.2854 USD [API] | `2026-10-29 18:31:36` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 7,892.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.89K USD at 1.3047 USD [API] | `2026-10-29 16:29:53` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 8,234.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.23K USD at 1.2803 USD [API] | `2026-10-29 18:40:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,876.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.88K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,003.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,218.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.22K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,911.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.91K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 400.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3429 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,873.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.87K USD at 1.3429 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,573.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.57K USD at 1.3429 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 1,011.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.01K USD at 1.4803 USD [API] | `2026-09-28 05:23:54` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 905.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.91K USD at 1.4803 USD [API] | `2026-09-28 05:23:54` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 17.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 91.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 7,933.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.93K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 3,171.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.17K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 14,525.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 14.53K USD at 1.2824 USD [API] | `2026-10-29 18:45:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 30,950.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 30.95K USD at 1.2863 USD [API] | `2026-10-29 18:51:28` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,048.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.05K USD at 1.2863 USD [API] | `2026-10-29 18:51:28` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,512.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.51K USD at 1.2840 USD [API] | `2026-10-29 19:12:52` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,807.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.81K USD at 1.2824 USD [API] | `2026-10-29 19:14:08` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,005.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2842 USD [API] | `2026-10-29 19:23:02` |
| `ANNOUNCEMENT` | `INFO` | `2.26` | 4,521.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.52K USD at 2.2605 USD [API] | `2025-02-03 00:43:28` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,004.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.2839 USD [API] | `2026-10-29 19:48:16` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 7,813.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.81K USD at 1.2769 USD [API] | `2026-10-29 20:02:41` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 6,213.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.21K USD at 1.2771 USD [API] | `2026-10-29 20:02:41` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.26%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.42%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+5.49%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.43%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,800,000.00 USD, Dist: `+7.65%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.43%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 2,900,000.00 USD, Dist: `+7.54%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.43%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 1,970.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 3,860.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 3,350.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 864.41 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 235.16 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 1,220.00 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 6,180.00 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,470.00 USD | 64,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 53,790.00 USD | 64,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 7,140.00 USD | 64,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 8,020.00 USD | 64,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 167.27 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 967.78 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 30,360.00 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 12,330.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 1,540.00 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 595,960.00 USD | 64,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 2,200.00 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 987.52 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 170,070.00 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 3,990.00 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 371.18 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 2,620.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 2,000.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 3,430.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 14,250.00 USD | 63,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 177,740.00 USD | 63,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 6,200.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 5,800.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 32,730.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 37,700.00 USD | 63,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 9,170.00 USD | 63,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 10,510.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,340.00 USD | 63,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 1,830.00 USD | 63,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 17,310.00 USD | 63,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 29,510.00 USD | 63,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 4,230.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 152,040.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 32,690.00 USD | 63,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,660.00 USD | 63,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 216,840.00 USD | 63,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 41,820.00 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 77,980.00 USD | 62,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 115,930.00 USD | 62,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 64,620.00 USD | 62,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 5,930.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 16,840.00 USD | 62,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,250.00 USD | 62,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 520,520.00 USD | 62,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 47,390.00 USD | 62,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 19,520.00 USD | 62,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 37,780.00 USD | 61,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 58,470.00 USD | 61,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 3,080,000.00 USD | 61,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 34,850.00 USD | 58,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 100,640.00 USD | 58,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 409,130.00 USD | 58,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 149,180.00 USD | 58,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 141,240.00 USD | 58,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 78,240.00 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 73,880.00 USD | 57,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 98,970.00 USD | 57,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 58,620.00 USD | 57,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 83,870.00 USD | 57,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,980,000.00 USD | 57,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 153,270.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 447,720.00 USD | 23,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 120,630.00 USD | 22,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 471,340.00 USD | 22,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 303,520.00 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 2,710,000.00 USD | 22,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,130,000.00 USD | 19,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 241,120.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,660,000.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 386,620.00 USD | 15,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 102,310,000.00 USD | 102,310,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 1,260,000.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 199,330.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 102,310,000.00 USD | 102,310,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 102,260,000.00 USD | 102,260,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 102,170,000.00 USD | 102,170,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 411,770.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 102,130,000.00 USD | 102,130,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 102,130,000.00 USD | 102,130,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 101,840,000.00 USD | 101,840,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 101,190.00 USD | 13,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 101,840,000.00 USD | 101,840,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 101,830,000.00 USD | 101,830,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 101,830,000.00 USD | 101,830,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 285,030.00 USD | 12,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 101,770,000.00 USD | 101,770,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 101,760,000.00 USD | 101,760,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 97,520,000.00 USD | 97,520,000.00 USD | 8,700.00 USD | 49,330.00 USD | 149,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 97,310,000.00 USD | 97,310,000.00 USD | 17,600.00 USD | 59,970.00 USD | 233,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 101,680,000.00 USD | 101,680,000.00 USD | 17,190.00 USD | 3,530.00 USD | 108,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 97,000,000.00 USD | 97,000,000.00 USD | 17,670.00 USD | 2,160.00 USD | 86,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 101,550,000.00 USD | 101,550,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 96,890,000.00 USD | 96,890,000.00 USD | 97,300.00 USD | 60,030.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,150,000.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.13` | 101,340,000.00 USD | 101,340,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 96,560,000.00 USD | 96,560,000.00 USD | 33,730.00 USD | 45,760.00 USD | 238,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 101,200,000.00 USD | 101,200,000.00 USD | 0.00 USD | 0.00 USD | 295,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 96,250,000.00 USD | 96,250,000.00 USD | 96,120.00 USD | 82,870.00 USD | 193,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 100,900,000.00 USD | 100,900,000.00 USD | 5,450.00 USD | 55,710.00 USD | 98,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 95,870,000.00 USD | 95,870,000.00 USD | 9,300.00 USD | 115,610.00 USD | 421,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 100,740,000.00 USD | 100,740,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 95,330,000.00 USD | 95,330,000.00 USD | 88,690.00 USD | 54,850.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 100,370,000.00 USD | 100,370,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 95,140,000.00 USD | 95,140,000.00 USD | 4,270.00 USD | 165,790.00 USD | 224,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 464,270.00 USD | 10,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.14` | 99,890,000.00 USD | 99,890,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 94,750,000.00 USD | 94,750,000.00 USD | 81,050.00 USD | 49,270.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 99,350,000.00 USD | 99,350,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 94,520,000.00 USD | 94,520,000.00 USD | 26,280.00 USD | 52,480.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 99,320,000.00 USD | 99,320,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 94,330,000.00 USD | 94,330,000.00 USD | 29,510.00 USD | 10,080.00 USD | 153,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 98,970,000.00 USD | 98,970,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 94,140,000.00 USD | 94,140,000.00 USD | 89,980.00 USD | 1,070.00 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 98,830,000.00 USD | 98,830,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 94,000,000.00 USD | 94,000,000.00 USD | 5,140.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 284,740.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 98,820,000.00 USD | 98,820,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 98,760,000.00 USD | 98,760,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 93,960,000.00 USD | 93,960,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 98,390,000.00 USD | 98,390,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 93,940,000.00 USD | 93,940,000.00 USD | 0.00 USD | 75.47 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 98,240,000.00 USD | 98,240,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 93,940,000.00 USD | 93,940,000.00 USD | 4,040.00 USD | 14,940.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 98,070,000.00 USD | 98,070,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 93,740,000.00 USD | 93,740,000.00 USD | 91,040.00 USD | 52,340.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 361,700.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 97,190,000.00 USD | 97,190,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 93,400,000.00 USD | 93,400,000.00 USD | 70,730.00 USD | 14,020.00 USD | 30,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 96,960,000.00 USD | 96,960,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 93,290,000.00 USD | 93,290,000.00 USD | 111,450.00 USD | 15,410.00 USD | 409,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 96,090,000.00 USD | 96,090,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 92,750,000.00 USD | 92,750,000.00 USD | 160,420.00 USD | 55,490.00 USD | 116,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 95,010,000.00 USD | 95,010,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 92,420,000.00 USD | 92,420,000.00 USD | 111,610.00 USD | 268,790.00 USD | 256,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 93,710,000.00 USD | 93,710,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 91,780,000.00 USD | 91,780,000.00 USD | 59,160.00 USD | 8,460.00 USD | 473,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,290,000.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 92,040,000.00 USD | 92,040,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 91,240,000.00 USD | 91,240,000.00 USD | 121,070.00 USD | 105,910.00 USD | 85,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 90,700,000.00 USD | 90,700,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 90,930,000.00 USD | 90,930,000.00 USD | 101,220.00 USD | 97,850.00 USD | 206,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 89,630,000.00 USD | 89,630,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 90,520,000.00 USD | 90,520,000.00 USD | 361,890.00 USD | 3,860.00 USD | 415,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 87,590,000.00 USD | 87,590,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 89,740,000.00 USD | 89,740,000.00 USD | 104,550.00 USD | 77,530.00 USD | 338,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 86,390,000.00 USD | 86,390,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 89,220,000.00 USD | 89,220,000.00 USD | 396,370.00 USD | 140,940.00 USD | 416,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 274,850.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 84,820,000.00 USD | 84,820,000.00 USD | 181,850.00 USD | 71,240.00 USD | 311,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 88,260,000.00 USD | 88,260,000.00 USD | 71,610.00 USD | 43,850.00 USD | 250,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 84,260,000.00 USD | 84,260,000.00 USD | 85,020.00 USD | 27,270.00 USD | 380,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 87,900,000.00 USD | 87,900,000.00 USD | 90,040.00 USD | 41,360.00 USD | 198,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 83,770,000.00 USD | 83,770,000.00 USD | 267,580.00 USD | 112,520.00 USD | 194,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 87,570,000.00 USD | 87,570,000.00 USD | 144,240.00 USD | 13,850.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 83,190,000.00 USD | 83,190,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 87,400,000.00 USD | 87,400,000.00 USD | 150,010.00 USD | 34,200.00 USD | 660,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 82,920,000.00 USD | 82,920,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 86,560,000.00 USD | 86,560,000.00 USD | 225,800.00 USD | 59,960.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 530,310.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 81,820,000.00 USD | 81,820,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 86,130,000.00 USD | 86,130,000.00 USD | 109,160.00 USD | 514,490.00 USD | 653,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 80,970,000.00 USD | 80,970,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 84,850,000.00 USD | 84,850,000.00 USD | 360,560.00 USD | 84,730.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 80,180,000.00 USD | 80,180,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 83,120,000.00 USD | 83,120,000.00 USD | 61,250.00 USD | 47,690.00 USD | 373,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 79,200,000.00 USD | 79,200,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 82,630,000.00 USD | 82,630,000.00 USD | 161,950.00 USD | 512,200.00 USD | 449,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 77,840,000.00 USD | 77,840,000.00 USD | 229,630.00 USD | 59,450.00 USD | 558,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 81,510,000.00 USD | 81,510,000.00 USD | 383,970.00 USD | 161,130.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 591,080.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 76,990,000.00 USD | 76,990,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 707,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 78,710,000.00 USD | 78,710,000.00 USD | 749,510.00 USD | 76,460.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 74,980,000.00 USD | 74,980,000.00 USD | 31,150.00 USD | 373,690.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 76,880,000.00 USD | 76,880,000.00 USD | 246,130.00 USD | 945,930.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 71,970,000.00 USD | 71,970,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 74,080,000.00 USD | 74,080,000.00 USD | 873,590.00 USD | 593,880.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 70,510,000.00 USD | 70,510,000.00 USD | 337,020.00 USD | 144,630.00 USD | 622,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 70,480,000.00 USD | 70,480,000.00 USD | 388,410.00 USD | 160,660.00 USD | 945,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 69,400,000.00 USD | 69,400,000.00 USD | 47,500.00 USD | 723,100.00 USD | 407,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 68,990,000.00 USD | 68,990,000.00 USD | 433,580.00 USD | 976,200.00 USD | 376,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 3,290.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 68,230,000.00 USD | 68,230,000.00 USD | 0.00 USD | 77,080.00 USD | 245,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 67,200,000.00 USD | 67,200,000.00 USD | 892,680.00 USD | 237,590.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 67,900,000.00 USD | 67,900,000.00 USD | 556,190.00 USD | 0.00 USD | 635,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 64,020,000.00 USD | 64,020,000.00 USD | 1,710,000.00 USD | 282,950.00 USD | 953,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 66,710,000.00 USD | 66,710,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 61,080,000.00 USD | 61,080,000.00 USD | 227,840.00 USD | 771,870.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 62,500,000.00 USD | 62,500,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 58,050,000.00 USD | 58,050,000.00 USD | 1,480,000.00 USD | 336,510.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 60,250,000.00 USD | 60,250,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 54,930,000.00 USD | 54,930,000.00 USD | 56,590.00 USD | 268,640.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 81,730.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 58,720,000.00 USD | 58,720,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 53,600,000.00 USD | 53,600,000.00 USD | 307,460.00 USD | 62,180.00 USD | 538,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 58,320,000.00 USD | 58,320,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 52,690,000.00 USD | 52,690,000.00 USD | 212,220.00 USD | 53,890.00 USD | 422,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 57,580,000.00 USD | 57,580,000.00 USD | 156,790.00 USD | 928,300.00 USD | 569,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 52,000,000.00 USD | 52,000,000.00 USD | 70,250.00 USD | 321,780.00 USD | 735,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,930,000.00 USD | 55,930,000.00 USD | 0.00 USD | 167,460.00 USD | 340,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 50,870,000.00 USD | 50,870,000.00 USD | 187,090.00 USD | 1,280.00 USD | 554,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,420,000.00 USD | 55,420,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 50,130,000.00 USD | 50,130,000.00 USD | 658,900.00 USD | 664,730.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,620,000.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 55,160,000.00 USD | 55,160,000.00 USD | 258,810.00 USD | 802,580.00 USD | 790,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 45,620,000.00 USD | 45,620,000.00 USD | 274,000.00 USD | 319,850.00 USD | 842,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 53,310,000.00 USD | 53,310,000.00 USD | 59,160.00 USD | 950,550.00 USD | 538,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 44,180,000.00 USD | 44,180,000.00 USD | 786,440.00 USD | 1,220,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 51,760,000.00 USD | 51,760,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 39,360,000.00 USD | 39,360,000.00 USD | 292,800.00 USD | 1,360,000.00 USD | 3,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 48,810,000.00 USD | 48,810,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 34,370,000.00 USD | 34,370,000.00 USD | 1,560,000.00 USD | 805,110.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 45,120,000.00 USD | 45,120,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 28,340,000.00 USD | 28,340,000.00 USD | 511,510.00 USD | 1,630,000.00 USD | 3,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 59,060.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 35,370,000.00 USD | 35,370,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 23,190,000.00 USD | 23,190,000.00 USD | 543,000.00 USD | 569,580.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 28,210,000.00 USD | 28,210,000.00 USD | 3,160,000.00 USD | 2,120,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 20,820,000.00 USD | 20,820,000.00 USD | 918,230.00 USD | 1,140,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 17,880,000.00 USD | 17,880,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 14,910,000.00 USD | 14,910,000.00 USD | 1,130,000.00 USD | 666,510.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 12,290,000.00 USD | 12,290,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 11,130,000.00 USD | 11,130,000.00 USD | 964,230.00 USD | 1,090,000.00 USD | 3,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 8,590,000.00 USD | 8,590,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 5,520,000.00 USD | 5,520,000.00 USD | 1,700,000.00 USD | 718,690.00 USD | 525,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 6,940,000.00 USD | 6,940,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 2,580,000.00 USD | 2,580,000.00 USD | 885,060.00 USD | 986,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,480,000.00 USD | 2,480,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 709,140.00 USD | 709,140.00 USD | 0.00 USD | 709,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 242,040.00 USD | 242,040.00 USD | 0.00 USD | 0.00 USD | 242,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 484,080.00 USD | 484,080.00 USD | 0.00 USD | 0.00 USD | 242,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 158,820.00 USD | 158,820.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 822,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 19,840.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 856,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,810,000.00 USD | 2,810,000.00 USD | 259,050.00 USD | 7,900.00 USD | 379,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 2,080,000.00 USD | 2,080,000.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 4,750,000.00 USD | 4,750,000.00 USD | 409,480.00 USD | 372,590.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 4,550,000.00 USD | 4,550,000.00 USD | 292,090.00 USD | 542,940.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 7,370,000.00 USD | 7,370,000.00 USD | 636,140.00 USD | 522,800.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 9,850,000.00 USD | 9,850,000.00 USD | 4,260,000.00 USD | 9,150.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 9,440,000.00 USD | 9,440,000.00 USD | 1,130,000.00 USD | 252,140.00 USD | 685,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 1,870,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 14,920,000.00 USD | 14,920,000.00 USD | 874,880.00 USD | 1,910,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 21,170,000.00 USD | 21,170,000.00 USD | 156,790.00 USD | 2,750,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 21,230,000.00 USD | 21,230,000.00 USD | 740,490.00 USD | 1,650,000.00 USD | 3,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 30,910,000.00 USD | 30,910,000.00 USD | 1,680,000.00 USD | 5,310,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 27,820,000.00 USD | 27,820,000.00 USD | 2,420,000.00 USD | 1,290,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 48,250,000.00 USD | 48,250,000.00 USD | 2,710,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 36,130,000.00 USD | 36,130,000.00 USD | 1,200,000.00 USD | 2,600,000.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 14,460.00 USD | 14,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.28` | 63,570,000.00 USD | 63,570,000.00 USD | 5,290,000.00 USD | 3,080,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 43,480,000.00 USD | 43,480,000.00 USD | 2,090,000.00 USD | 1,430,000.00 USD | 3,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 83,240,000.00 USD | 83,240,000.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 51,460,000.00 USD | 51,460,000.00 USD | 2,340,000.00 USD | 1,980,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 86,830,000.00 USD | 86,830,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 55,770,000.00 USD | 55,770,000.00 USD | 483,960.00 USD | 826,970.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 88,860,000.00 USD | 88,860,000.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 59,890,000.00 USD | 59,890,000.00 USD | 1,340,000.00 USD | 598,170.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 93,110,000.00 USD | 93,110,000.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 63,470,000.00 USD | 63,470,000.00 USD | 904,370.00 USD | 743,290.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 243,660.00 USD | 258,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.29` | 98,240,000.00 USD | 98,240,000.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 66,720,000.00 USD | 66,720,000.00 USD | 864,310.00 USD | 1,100,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 98,960,000.00 USD | 98,960,000.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 67,840,000.00 USD | 67,840,000.00 USD | 454,460.00 USD | 142,490.00 USD | 518,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 100,560,000.00 USD | 100,560,000.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 69,220,000.00 USD | 69,220,000.00 USD | 186,090.00 USD | 275,630.00 USD | 919,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 103,160,000.00 USD | 103,160,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 73,030,000.00 USD | 73,030,000.00 USD | 574,390.00 USD | 275,550.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 106,820,000.00 USD | 106,820,000.00 USD | 1,780,000.00 USD | 8,810.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 79,410,000.00 USD | 79,410,000.00 USD | 1,880,000.00 USD | 720,770.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 56,490.00 USD | 314,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 114,540,000.00 USD | 114,540,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 82,200,000.00 USD | 82,200,000.00 USD | 555,660.00 USD | 702,980.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 116,490,000.00 USD | 116,490,000.00 USD | 25,800.00 USD | 173,700.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 83,190,000.00 USD | 83,190,000.00 USD | 468,600.00 USD | 109,540.00 USD | 408,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 118,870,000.00 USD | 118,870,000.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 86,210,000.00 USD | 86,210,000.00 USD | 674,250.00 USD | 493,820.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 120,130,000.00 USD | 120,130,000.00 USD | 158,990.00 USD | 944,610.00 USD | 158,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 88,270,000.00 USD | 88,270,000.00 USD | 835,040.00 USD | 564,380.00 USD | 660,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 123,190,000.00 USD | 123,190,000.00 USD | 0.00 USD | 2,170,000.00 USD | 887,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 89,870,000.00 USD | 89,870,000.00 USD | 441,960.00 USD | 703,580.00 USD | 458,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 5,520.00 USD | 320,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 125,440,000.00 USD | 125,440,000.00 USD | 1,770,000.00 USD | 238,140.00 USD | 245,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 93,170,000.00 USD | 93,170,000.00 USD | 803,720.00 USD | 281,570.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 130,860,000.00 USD | 130,860,000.00 USD | 1,550,000.00 USD | 821,310.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 96,880,000.00 USD | 96,880,000.00 USD | 1,270,000.00 USD | 481,050.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 133,620,000.00 USD | 133,620,000.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 99,660,000.00 USD | 99,660,000.00 USD | 966,790.00 USD | 606,030.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 138,500,000.00 USD | 138,500,000.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 101,560,000.00 USD | 101,560,000.00 USD | 499,000.00 USD | 340,130.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 139,790,000.00 USD | 139,790,000.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 103,630,000.00 USD | 103,630,000.00 USD | 415,520.00 USD | 266,240.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 55,110.00 USD | 375,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.32` | 144,510,000.00 USD | 144,510,000.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 108,200,000.00 USD | 108,200,000.00 USD | 1,260,000.00 USD | 636,870.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 149,610,000.00 USD | 149,610,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 112,310,000.00 USD | 112,310,000.00 USD | 1,150,000.00 USD | 582,420.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 151,630,000.00 USD | 151,630,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 114,560,000.00 USD | 114,560,000.00 USD | 1,320,000.00 USD | 195,100.00 USD | 744,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 154,980,000.00 USD | 154,980,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 117,470,000.00 USD | 117,470,000.00 USD | 885,300.00 USD | 456,600.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 157,760,000.00 USD | 157,760,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 118,470,000.00 USD | 118,470,000.00 USD | 599,940.00 USD | 60,300.00 USD | 341,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 7,390.00 USD | 382,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 159,570,000.00 USD | 159,570,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 119,540,000.00 USD | 119,540,000.00 USD | 412,050.00 USD | 224,860.00 USD | 436,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 160,670,000.00 USD | 160,670,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 120,920,000.00 USD | 120,920,000.00 USD | 504,110.00 USD | 75,550.00 USD | 798,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 162,380,000.00 USD | 162,380,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 123,090,000.00 USD | 123,090,000.00 USD | 848,670.00 USD | 99,880.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 164,850,000.00 USD | 164,850,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 125,040,000.00 USD | 125,040,000.00 USD | 737,030.00 USD | 194,010.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 166,870,000.00 USD | 166,870,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 126,370,000.00 USD | 126,370,000.00 USD | 459,140.00 USD | 355,590.00 USD | 517,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 43,550.00 USD | 426,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 168,420,000.00 USD | 168,420,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 127,110,000.00 USD | 127,110,000.00 USD | 384,130.00 USD | 22,640.00 USD | 331,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 170,860,000.00 USD | 170,860,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 127,590,000.00 USD | 127,590,000.00 USD | 134,820.00 USD | 84,090.00 USD | 260,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 172,710,000.00 USD | 172,710,000.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 128,690,000.00 USD | 128,690,000.00 USD | 496,210.00 USD | 196,970.00 USD | 401,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 178,180,000.00 USD | 178,180,000.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 129,830,000.00 USD | 129,830,000.00 USD | 579,000.00 USD | 162,370.00 USD | 406,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 185,300,000.00 USD | 185,300,000.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 130,820,000.00 USD | 130,820,000.00 USD | 291,740.00 USD | 235,320.00 USD | 457,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,570.00 USD | 432,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 193,560,000.00 USD | 193,560,000.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 131,060,000.00 USD | 131,060,000.00 USD | 112,770.00 USD | 30,480.00 USD | 96,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 201,310,000.00 USD | 201,310,000.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 131,610,000.00 USD | 131,610,000.00 USD | 249,180.00 USD | 21,780.00 USD | 275,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 209,330,000.00 USD | 209,330,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 132,020,000.00 USD | 132,020,000.00 USD | 146,270.00 USD | 30,050.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 218,450,000.00 USD | 218,450,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 132,170,000.00 USD | 132,170,000.00 USD | 66,220.00 USD | 30,090.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 225,200,000.00 USD | 225,200,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 132,680,000.00 USD | 132,680,000.00 USD | 86,720.00 USD | 36,350.00 USD | 395,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 7,930.00 USD | 440,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 231,530,000.00 USD | 231,530,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 133,640,000.00 USD | 133,640,000.00 USD | 391,410.00 USD | 32,490.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 234,070,000.00 USD | 234,070,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 133,970,000.00 USD | 133,970,000.00 USD | 209,880.00 USD | 43,130.00 USD | 82,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 236,720,000.00 USD | 236,720,000.00 USD | 1,300,000.00 USD | 282,890.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 134,630,000.00 USD | 134,630,000.00 USD | 225,120.00 USD | 162,660.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 239,980,000.00 USD | 239,980,000.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 134,930,000.00 USD | 134,930,000.00 USD | 130,140.00 USD | 2,390.00 USD | 166,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 242,720,000.00 USD | 242,720,000.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 135,050,000.00 USD | 135,050,000.00 USD | 0.00 USD | 13,170.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 99,580.00 USD | 540,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 243,540,000.00 USD | 243,540,000.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,310,000.00 USD | 135,310,000.00 USD | 61,210.00 USD | 90,280.00 USD | 103,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 244,590,000.00 USD | 244,590,000.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,510,000.00 USD | 135,510,000.00 USD | 93,070.00 USD | 20,920.00 USD | 86,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 246,010,000.00 USD | 246,010,000.00 USD | 367,350.00 USD | 211,750.00 USD | 841,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,700,000.00 USD | 135,700,000.00 USD | 6,510.00 USD | 39,050.00 USD | 147,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 247,250,000.00 USD | 247,250,000.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 135,810,000.00 USD | 135,810,000.00 USD | 17,670.00 USD | 2,160.00 USD | 86,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 248,910,000.00 USD | 248,910,000.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 136,140,000.00 USD | 136,140,000.00 USD | 97,300.00 USD | 60,030.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,780.00 USD | 544,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 249,940,000.00 USD | 249,940,000.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 136,450,000.00 USD | 136,450,000.00 USD | 33,730.00 USD | 45,760.00 USD | 238,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 251,500,000.00 USD | 251,500,000.00 USD | 692,200.00 USD | 267,730.00 USD | 600,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 136,830,000.00 USD | 136,830,000.00 USD | 96,120.00 USD | 82,870.00 USD | 193,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 253,200,000.00 USD | 253,200,000.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 136,900,000.00 USD | 136,900,000.00 USD | 2,300.00 USD | 71,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 255,160,000.00 USD | 255,160,000.00 USD | 710,620.00 USD | 348,810.00 USD | 900,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 137,370,000.00 USD | 137,370,000.00 USD | 7,000.00 USD | 43,760.00 USD | 421,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 256,150,000.00 USD | 256,150,000.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 137,560,000.00 USD | 137,560,000.00 USD | 88,690.00 USD | 54,850.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 649,900.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 257,260,000.00 USD | 257,260,000.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 137,950,000.00 USD | 137,950,000.00 USD | 4,270.00 USD | 165,790.00 USD | 224,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 258,470,000.00 USD | 258,470,000.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 138,180,000.00 USD | 138,180,000.00 USD | 81,050.00 USD | 49,270.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 259,220,000.00 USD | 259,220,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 138,200,000.00 USD | 138,200,000.00 USD | 0.00 USD | 18,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 259,750,000.00 USD | 259,750,000.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 259,920,000.00 USD | 259,920,000.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,310.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,140,000.00 USD | 260,140,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,150,000.00 USD | 260,150,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,210,000.00 USD | 260,210,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,290,000.00 USD | 260,290,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,580,000.00 USD | 260,580,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 858.46 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 260,730,000.00 USD | 260,730,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 260,880,000.00 USD | 260,880,000.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 261,160,000.00 USD | 261,160,000.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,690.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 1,220.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 129,900.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 551.65 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,150.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 11,820.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 323.30 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,790.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 13,390.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 4,580,000.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 239.15 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,530.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 401.38 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 8,640.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 5,020.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,060.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 232.21 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 110,470.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,870.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,160.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 808.37 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 5,450,000.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 130,160.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 7,940.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 4,240.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 747.78 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 12,290.00 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 30,700.00 USD | 11,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,010.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 2,930,000.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 309,780.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 1,410.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 945.17 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 230,510.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 2,410,000.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 178.20 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 460.50 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 296.73 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 673.60 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 426,100.00 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 331,410.00 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 433.29 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 52,320.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.02 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 438.80 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 2,140.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 82,220.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 102.81 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 224.50 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 11,380.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 248.94 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 358.05 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 49,200.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 180.56 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 13,230.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 18,290.00 USD | 18,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 81,970.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 4,080.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 678.62 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 24,250.00 USD | 18,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 657.45 USD | 18,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 3,740.00 USD | 18,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 3,710,000.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 2,310.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 1,860.00 USD | 22,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 1,530,000.00 USD | 24,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 59,380.00 USD | 24,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,650,000.00 USD | 0.00 USD | 1,970.00 USD | `-79.60%` | `7,717.00` |
| `Live` | `Long` | `0.2650` | 64,650,000.00 USD | 0.00 USD | 3,860.00 USD | `-78.79%` | `14,556.00` |
| `Live` | `Long` | `0.2750` | 64,650,000.00 USD | 0.00 USD | 3,350.00 USD | `-77.99%` | `12,190.00` |
| `Live` | `Long` | `0.2850` | 64,650,000.00 USD | 0.00 USD | 864.41 USD | `-77.19%` | `3,033.00` |
| `Live` | `Long` | `0.3050` | 64,640,000.00 USD | 0.00 USD | 235.16 USD | `-75.59%` | `771.00` |
| `Live` | `Long` | `0.3150` | 64,640,000.00 USD | 0.00 USD | 4,910.00 USD | `-74.79%` | `15,577.00` |
| `Live` | `Long` | `0.3350` | 64,640,000.00 USD | 0.00 USD | 1,220.00 USD | `-73.19%` | `3,636.00` |
| `Live` | `Long` | `0.3450` | 64,640,000.00 USD | 0.00 USD | 6,180.00 USD | `-72.39%` | `17,916.00` |
| `Live` | `Long` | `0.3550` | 64,630,000.00 USD | 0.00 USD | 2,470.00 USD | `-71.59%` | `6,970.00` |
| `Live` | `Long` | `0.3650` | 64,630,000.00 USD | 0.00 USD | 53,790.00 USD | `-70.79%` | `147,378.00` |
| `Live` | `Long` | `0.3750` | 64,580,000.00 USD | 0.00 USD | 7,140.00 USD | `-69.99%` | `19,043.00` |
| `Live` | `Long` | `0.3850` | 64,570,000.00 USD | 0.00 USD | 8,020.00 USD | `-69.19%` | `20,836.00` |
| `Live` | `Long` | `0.3950` | 64,560,000.00 USD | 0.00 USD | 174.59 USD | `-68.39%` | `442.00` |
| `Live` | `Long` | `0.4050` | 64,560,000.00 USD | 0.00 USD | 167.27 USD | `-67.59%` | `413.00` |
| `Live` | `Long` | `0.4150` | 64,560,000.00 USD | 0.00 USD | 967.78 USD | `-66.79%` | `2,332.00` |
| `Live` | `Long` | `0.4250` | 64,560,000.00 USD | 0.00 USD | 30,360.00 USD | `-65.99%` | `71,435.00` |
| `Live` | `Long` | `0.4350` | 64,530,000.00 USD | 0.00 USD | 12,330.00 USD | `-65.19%` | `28,353.00` |
| `Live` | `Long` | `0.4450` | 64,520,000.00 USD | 0.00 USD | 1,540.00 USD | `-64.39%` | `3,467.00` |
| `Live` | `Long` | `0.4550` | 64,510,000.00 USD | 0.00 USD | 595,960.00 USD | `-63.59%` | `1,309,807.00` |
| `Live` | `Long` | `0.4650` | 63,920,000.00 USD | 0.00 USD | 2,200.00 USD | `-62.79%` | `4,729.00` |
| `Live` | `Long` | `0.4750` | 63,920,000.00 USD | 0.00 USD | 987.52 USD | `-61.99%` | `2,079.00` |
| `Live` | `Long` | `0.4850` | 63,920,000.00 USD | 0.00 USD | 170,070.00 USD | `-61.19%` | `350,668.00` |
| `Live` | `Long` | `0.4950` | 63,750,000.00 USD | 0.00 USD | 3,990.00 USD | `-60.39%` | `8,062.00` |
| `Live` | `Long` | `0.5050` | 63,740,000.00 USD | 0.00 USD | 371.18 USD | `-59.59%` | `735.00` |
| `Live` | `Long` | `0.5250` | 63,740,000.00 USD | 0.00 USD | 2,620.00 USD | `-57.99%` | `4,991.00` |
| `Live` | `Long` | `0.5350` | 63,740,000.00 USD | 0.00 USD | 2,000.00 USD | `-57.19%` | `3,741.00` |
| `Live` | `Long` | `0.5450` | 63,740,000.00 USD | 0.00 USD | 3,430.00 USD | `-56.39%` | `6,293.00` |
| `Live` | `Long` | `0.5550` | 63,730,000.00 USD | 0.00 USD | 14,250.00 USD | `-55.59%` | `25,672.00` |
| `Live` | `Long` | `0.5650` | 63,720,000.00 USD | 0.00 USD | 177,740.00 USD | `-54.79%` | `314,578.00` |
| `Live` | `Long` | `0.5750` | 63,540,000.00 USD | 0.00 USD | 6,200.00 USD | `-53.99%` | `10,784.00` |
| `Live` | `Long` | `0.5850` | 63,530,000.00 USD | 0.00 USD | 5,800.00 USD | `-53.19%` | `9,907.00` |
| `Live` | `Long` | `0.6050` | 63,530,000.00 USD | 0.00 USD | 32,730.00 USD | `-51.59%` | `54,098.00` |
| `Live` | `Long` | `0.6150` | 63,500,000.00 USD | 0.00 USD | 37,700.00 USD | `-50.79%` | `61,305.00` |
| `Live` | `Long` | `0.6250` | 63,460,000.00 USD | 0.00 USD | 9,170.00 USD | `-49.99%` | `14,668.00` |
| `Live` | `Long` | `0.6350` | 63,450,000.00 USD | 0.00 USD | 10,510.00 USD | `-49.19%` | `16,554.00` |
| `Live` | `Long` | `0.6450` | 63,440,000.00 USD | 0.00 USD | 19,340.00 USD | `-48.39%` | `29,983.00` |
| `Live` | `Long` | `0.6550` | 63,420,000.00 USD | 0.00 USD | 1,830.00 USD | `-47.59%` | `2,788.00` |
| `Live` | `Long` | `0.6650` | 63,420,000.00 USD | 0.00 USD | 17,310.00 USD | `-46.79%` | `26,027.00` |
| `Live` | `Long` | `0.6750` | 63,400,000.00 USD | 0.00 USD | 29,510.00 USD | `-45.99%` | `43,712.00` |
| `Live` | `Long` | `0.6850` | 63,370,000.00 USD | 0.00 USD | 4,230.00 USD | `-45.19%` | `6,172.00` |
| `Live` | `Long` | `0.6950` | 63,370,000.00 USD | 0.00 USD | 152,040.00 USD | `-44.39%` | `218,767.00` |
| `Live` | `Long` | `0.7050` | 63,210,000.00 USD | 0.00 USD | 32,690.00 USD | `-43.59%` | `46,363.00` |
| `Live` | `Long` | `0.7150` | 63,180,000.00 USD | 0.00 USD | 67,660.00 USD | `-42.79%` | `94,630.00` |
| `Live` | `Long` | `0.7250` | 63,110,000.00 USD | 0.00 USD | 216,840.00 USD | `-41.99%` | `299,086.00` |
| `Live` | `Long` | `0.7350` | 62,900,000.00 USD | 0.00 USD | 41,820.00 USD | `-41.19%` | `56,895.00` |
| `Live` | `Long` | `0.7450` | 62,860,000.00 USD | 0.00 USD | 77,980.00 USD | `-40.39%` | `104,674.00` |
| `Live` | `Long` | `0.7550` | 62,780,000.00 USD | 0.00 USD | 115,930.00 USD | `-39.59%` | `153,553.00` |
| `Live` | `Long` | `0.7650` | 62,660,000.00 USD | 0.00 USD | 64,620.00 USD | `-38.79%` | `84,473.00` |
| `Live` | `Long` | `0.7750` | 62,600,000.00 USD | 0.00 USD | 5,930.00 USD | `-37.99%` | `7,651.00` |
| `Live` | `Long` | `0.7850` | 62,590,000.00 USD | 0.00 USD | 16,840.00 USD | `-37.18%` | `21,451.00` |
| `Live` | `Long` | `0.7950` | 62,570,000.00 USD | 0.00 USD | 11,250.00 USD | `-36.38%` | `14,145.00` |
| `Live` | `Long` | `0.8050` | 62,560,000.00 USD | 0.00 USD | 520,520.00 USD | `-35.58%` | `646,603.00` |
| `Live` | `Long` | `0.8150` | 62,040,000.00 USD | 0.00 USD | 47,390.00 USD | `-34.78%` | `58,149.00` |
| `Live` | `Long` | `0.8250` | 62,000,000.00 USD | 0.00 USD | 19,520.00 USD | `-33.98%` | `23,656.00` |
| `Live` | `Long` | `0.8350` | 61,980,000.00 USD | 0.00 USD | 37,780.00 USD | `-33.18%` | `45,244.00` |
| `Live` | `Long` | `0.8450` | 61,940,000.00 USD | 0.00 USD | 58,470.00 USD | `-32.38%` | `69,192.00` |
| `Live` | `Long` | `0.8550` | 61,880,000.00 USD | 0.00 USD | 3,080,000.00 USD | `-31.58%` | `3,606,628.00` |
| `Live` | `Long` | `0.8650` | 58,800,000.00 USD | 0.00 USD | 34,850.00 USD | `-30.78%` | `40,293.00` |
| `Live` | `Long` | `0.8750` | 58,760,000.00 USD | 0.00 USD | 100,640.00 USD | `-29.98%` | `115,016.00` |
| `Live` | `Long` | `0.8850` | 58,660,000.00 USD | 0.00 USD | 409,130.00 USD | `-29.18%` | `462,299.00` |
| `Live` | `Long` | `0.8950` | 58,250,000.00 USD | 0.00 USD | 149,180.00 USD | `-28.38%` | `166,676.00` |
| `Live` | `Long` | `0.9050` | 58,100,000.00 USD | 0.00 USD | 141,240.00 USD | `-27.58%` | `156,071.00` |
| `Live` | `Long` | `0.9150` | 57,960,000.00 USD | 0.00 USD | 78,240.00 USD | `-26.78%` | `85,507.00` |
| `Live` | `Long` | `0.9250` | 57,880,000.00 USD | 0.00 USD | 73,880.00 USD | `-25.98%` | `79,865.00` |
| `Live` | `Long` | `0.9350` | 57,810,000.00 USD | 0.00 USD | 98,970.00 USD | `-25.18%` | `105,845.00` |
| `Live` | `Long` | `0.9450` | 57,710,000.00 USD | 0.00 USD | 58,620.00 USD | `-24.38%` | `62,036.00` |
| `Live` | `Long` | `0.9550` | 57,650,000.00 USD | 0.00 USD | 83,870.00 USD | `-23.58%` | `87,821.00` |
| `Live` | `Long` | `0.9650` | 57,570,000.00 USD | 0.00 USD | 33,980,000.00 USD | `-22.78%` | `35,208,016.00` |
| `Live` | `Long` | `0.9750` | 23,590,000.00 USD | 0.00 USD | 153,270.00 USD | `-21.98%` | `157,196.00` |
| `Live` | `Long` | `0.9850` | 23,440,000.00 USD | 0.00 USD | 447,720.00 USD | `-21.18%` | `454,534.00` |
| `Live` | `Long` | `0.9950` | 22,990,000.00 USD | 0.00 USD | 120,630.00 USD | `-20.38%` | `121,234.00` |
| `Live` | `Long` | `1.00` | 22,870,000.00 USD | 0.00 USD | 471,340.00 USD | `-19.58%` | `468,997.00` |
| `Live` | `Long` | `1.01` | 22,400,000.00 USD | 0.00 USD | 303,520.00 USD | `-18.78%` | `299,030.00` |
| `Live` | `Long` | `1.02` | 22,100,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-17.98%` | `2,642,875.00` |
| `Live` | `Long` | `1.03` | 19,390,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-17.18%` | `2,062,761.00` |
| `Live` | `Long` | `1.04` | 17,250,000.00 USD | 0.00 USD | 241,120.00 USD | `-16.38%` | `230,733.00` |
| `Live` | `Long` | `1.05` | 17,010,000.00 USD | 0.00 USD | 1,660,000.00 USD | `-15.58%` | `1,575,028.00` |
| `Live` | `Long` | `1.06` | 15,350,000.00 USD | 0.00 USD | 386,620.00 USD | `-14.78%` | `363,022.00` |
| `Live` | `Long` | `1.07` | 14,960,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-13.98%` | `1,168,042.00` |
| `Live` | `Long` | `1.08` | 13,710,000.00 USD | 0.00 USD | 199,330.00 USD | `-13.18%` | `183,718.00` |
| `Live` | `Long` | `1.09` | 13,510,000.00 USD | 0.00 USD | 411,770.00 USD | `-12.38%` | `376,042.00` |
| `Live` | `Long` | `1.10` | 13,100,000.00 USD | 0.00 USD | 101,190.00 USD | `-11.58%` | `91,575.00` |
| `Live` | `Long` | `1.11` | 12,990,000.00 USD | 0.00 USD | 285,030.00 USD | `-10.78%` | `255,635.00` |
| `Live` | `Long` | `1.12` | 12,710,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-9.98%` | `1,913,541.00` |
| `Live` | `Long` | `1.14` | 10,560,000.00 USD | 0.00 USD | 464,270.00 USD | `-9.18%` | `409,052.00` |
| `Live` | `Long` | `1.15` | 10,090,000.00 USD | 0.00 USD | 284,740.00 USD | `-8.38%` | `248,677.00` |
| `Live` | `Long` | `1.16` | 9,810,000.00 USD | 0.00 USD | 361,700.00 USD | `-7.58%` | `313,158.00` |
| `Live` | `Long` | `1.17` | 9,450,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-6.78%` | `1,103,539.00` |
| `Live` | `Long` | `1.18` | 8,160,000.00 USD | 0.00 USD | 274,850.00 USD | `-5.98%` | `233,916.00` |
| `Live` | `Long` | `1.19` | 7,880,000.00 USD | 0.00 USD | 530,310.00 USD | `-5.18%` | `447,521.00` |
| `Live` | `Long` | `1.20` | 7,350,000.00 USD | 0.00 USD | 591,080.00 USD | `-4.38%` | `494,630.00` |
| `Live` | `Long` | `1.21` | 6,760,000.00 USD | 0.00 USD | 3,290.00 USD | `-3.58%` | `2,728.00` |
| `Live` | `Long` | `1.22` | 6,760,000.00 USD | 0.00 USD | 81,730.00 USD | `-2.78%` | `67,269.00` |
| `Live` | `Long` | `1.23` | 6,680,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-1.98%` | `5,403,657.00` |
| `Live` | `Long` | `1.24` | 59,060.00 USD | 0.00 USD | 59,060.00 USD | `-1.18%` | `47,823.00` |
| `Live` | `Short` | `1.27` | 14,460.00 USD | 14,460.00 USD | 0.00 USD | `+2.02%` | `11,339.00` |
| `Live` | `Short` | `1.28` | 258,120.00 USD | 243,660.00 USD | 0.00 USD | `+2.82%` | `189,621.00` |
| `Live` | `Short` | `1.29` | 314,610.00 USD | 56,490.00 USD | 0.00 USD | `+3.62%` | `43,622.00` |
| `Live` | `Short` | `1.30` | 320,130.00 USD | 5,520.00 USD | 0.00 USD | `+4.43%` | `4,227.00` |
| `Live` | `Short` | `1.31` | 375,240.00 USD | 55,110.00 USD | 0.00 USD | `+5.23%` | `41,912.00` |
| `Live` | `Short` | `1.32` | 382,630.00 USD | 7,390.00 USD | 0.00 USD | `+6.03%` | `5,576.00` |
| `Live` | `Short` | `1.33` | 426,180.00 USD | 43,550.00 USD | 0.00 USD | `+6.83%` | `32,622.00` |
| `Live` | `Short` | `1.34` | 432,750.00 USD | 6,570.00 USD | 0.00 USD | `+7.63%` | `4,885.00` |
| `Live` | `Short` | `1.35` | 440,680.00 USD | 7,930.00 USD | 0.00 USD | `+8.43%` | `5,850.00` |
| `Live` | `Short` | `1.36` | 540,250.00 USD | 99,580.00 USD | 0.00 USD | `+9.23%` | `72,950.00` |
| `Live` | `Short` | `1.38` | 544,030.00 USD | 3,780.00 USD | 0.00 USD | `+10.03%` | `2,747.00` |
| `Live` | `Short` | `1.39` | 1,190,000.00 USD | 649,900.00 USD | 0.00 USD | `+10.83%` | `469,242.00` |
| `Live` | `Short` | `1.40` | 1,200,000.00 USD | 2,310.00 USD | 0.00 USD | `+11.63%` | `1,659.00` |
| `Live` | `Short` | `1.41` | 1,200,000.00 USD | 858.46 USD | 0.00 USD | `+12.43%` | `611.00` |
| `Live` | `Short` | `1.42` | 1,200,000.00 USD | 3,860.00 USD | 0.00 USD | `+13.23%` | `2,729.00` |
| `Live` | `Short` | `1.43` | 1,290,000.00 USD | 93,690.00 USD | 0.00 USD | `+14.03%` | `65,744.00` |
| `Live` | `Short` | `1.44` | 1,300,000.00 USD | 1,220.00 USD | 0.00 USD | `+14.83%` | `848.00` |
| `Live` | `Short` | `1.45` | 1,300,000.00 USD | 284.66 USD | 0.00 USD | `+15.63%` | `197.00` |
| `Live` | `Short` | `1.47` | 1,430,000.00 USD | 129,900.00 USD | 0.00 USD | `+17.23%` | `88,671.00` |
| `Live` | `Short` | `1.48` | 1,430,000.00 USD | 551.65 USD | 0.00 USD | `+18.03%` | `374.00` |
| `Live` | `Short` | `1.50` | 1,440,000.00 USD | 12,150.00 USD | 0.00 USD | `+19.63%` | `8,126.00` |
| `Live` | `Short` | `1.51` | 1,450,000.00 USD | 11,820.00 USD | 0.00 USD | `+21.23%` | `7,799.00` |
| `Live` | `Short` | `1.52` | 1,450,000.00 USD | 323.30 USD | 0.00 USD | `+22.03%` | `212.00` |
| `Live` | `Short` | `1.53` | 1,450,000.00 USD | 174.99 USD | 0.00 USD | `+22.83%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,450,000.00 USD | 1,370.00 USD | 0.00 USD | `+23.63%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,450,000.00 USD | 1,360.00 USD | 0.00 USD | `+24.43%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,460,000.00 USD | 1,790.00 USD | 0.00 USD | `+25.23%` | `1,144.00` |
| `Live` | `Short` | `1.57` | 1,460,000.00 USD | 2,900.00 USD | 0.00 USD | `+26.03%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,470,000.00 USD | 13,390.00 USD | 0.00 USD | `+26.83%` | `8,445.00` |
| `Live` | `Short` | `1.59` | 6,050,000.00 USD | 4,580,000.00 USD | 0.00 USD | `+27.63%` | `2,872,725.00` |
| `Live` | `Short` | `1.60` | 6,050,000.00 USD | 239.15 USD | 0.00 USD | `+28.43%` | `149.00` |
| `Live` | `Short` | `1.61` | 6,060,000.00 USD | 2,530.00 USD | 0.00 USD | `+29.23%` | `1,567.00` |
| `Live` | `Short` | `1.62` | 6,060,000.00 USD | 401.38 USD | 0.00 USD | `+30.03%` | `247.00` |
| `Live` | `Short` | `1.64` | 6,070,000.00 USD | 8,640.00 USD | 0.00 USD | `+30.83%` | `5,284.00` |
| `Live` | `Short` | `1.66` | 6,070,000.00 USD | 147.30 USD | 0.00 USD | `+32.43%` | `89.00` |
| `Live` | `Short` | `1.67` | 6,070,000.00 USD | 586.08 USD | 0.00 USD | `+33.23%` | `352.00` |
| `Live` | `Short` | `1.68` | 6,070,000.00 USD | 5,020.00 USD | 0.00 USD | `+34.03%` | `3,000.00` |
| `Live` | `Short` | `1.69` | 6,080,000.00 USD | 4,060.00 USD | 0.00 USD | `+34.83%` | `2,409.00` |
| `Live` | `Short` | `1.70` | 6,080,000.00 USD | 232.21 USD | 0.00 USD | `+35.63%` | `137.00` |
| `Live` | `Short` | `1.71` | 6,080,000.00 USD | 1,980.00 USD | 0.00 USD | `+36.43%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 6,190,000.00 USD | 110,470.00 USD | 0.00 USD | `+38.03%` | `64,043.00` |
| `Live` | `Short` | `1.74` | 6,190,000.00 USD | 2,970.00 USD | 0.00 USD | `+38.83%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 6,190,000.00 USD | 2,870.00 USD | 0.00 USD | `+39.63%` | `1,642.00` |
| `Live` | `Short` | `1.75` | 6,200,000.00 USD | 1,160.00 USD | 0.00 USD | `+40.43%` | `661.00` |
| `Live` | `Short` | `1.76` | 6,200,000.00 USD | 808.37 USD | 0.00 USD | `+41.23%` | `458.00` |
| `Live` | `Short` | `1.77` | 11,650,000.00 USD | 5,450,000.00 USD | 0.00 USD | `+42.03%` | `3,070,483.00` |
| `Live` | `Short` | `1.78` | 11,780,000.00 USD | 130,160.00 USD | 0.00 USD | `+42.83%` | `72,921.00` |
| `Live` | `Short` | `1.79` | 11,780,000.00 USD | 7,940.00 USD | 0.00 USD | `+43.63%` | `4,422.00` |
| `Live` | `Short` | `1.80` | 11,790,000.00 USD | 4,240.00 USD | 0.00 USD | `+44.43%` | `2,347.00` |
| `Live` | `Short` | `1.81` | 11,790,000.00 USD | 747.78 USD | 0.00 USD | `+45.23%` | `412.00` |
| `Live` | `Short` | `1.82` | 11,800,000.00 USD | 12,290.00 USD | 0.00 USD | `+46.04%` | `6,735.00` |
| `Live` | `Short` | `1.83` | 11,830,000.00 USD | 30,700.00 USD | 0.00 USD | `+46.84%` | `16,729.00` |
| `Live` | `Short` | `1.84` | 11,840,000.00 USD | 9,340.00 USD | 0.00 USD | `+47.64%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,840,000.00 USD | 428.50 USD | 0.00 USD | `+48.44%` | `231.00` |
| `Live` | `Short` | `1.86` | 11,840,000.00 USD | 2,010.00 USD | 0.00 USD | `+49.24%` | `1,079.00` |
| `Live` | `Short` | `1.89` | 14,770,000.00 USD | 2,930,000.00 USD | 0.00 USD | `+50.84%` | `1,551,725.00` |
| `Live` | `Short` | `1.90` | 15,080,000.00 USD | 309,780.00 USD | 0.00 USD | `+51.64%` | `163,470.00` |
| `Live` | `Short` | `1.91` | 15,080,000.00 USD | 373.38 USD | 0.00 USD | `+52.44%` | `196.00` |
| `Live` | `Short` | `1.92` | 15,080,000.00 USD | 1,410.00 USD | 0.00 USD | `+53.24%` | `737.00` |
| `Live` | `Short` | `1.93` | 15,080,000.00 USD | 945.17 USD | 0.00 USD | `+54.04%` | `491.00` |
| `Live` | `Short` | `1.96` | 15,080,000.00 USD | 293.25 USD | 0.00 USD | `+56.44%` | `150.00` |
| `Live` | `Short` | `1.97` | 15,310,000.00 USD | 230,510.00 USD | 0.00 USD | `+57.24%` | `117,306.00` |
| `Live` | `Short` | `1.98` | 15,310,000.00 USD | 651.75 USD | 0.00 USD | `+58.04%` | `330.00` |
| `Live` | `Short` | `2.02` | 17,720,000.00 USD | 2,410,000.00 USD | 0.00 USD | `+61.24%` | `1,196,812.00` |
| `Live` | `Short` | `2.02` | 17,720,000.00 USD | 178.20 USD | 0.00 USD | `+62.04%` | `88.00` |
| `Live` | `Short` | `2.04` | 17,720,000.00 USD | 198.36 USD | 0.00 USD | `+63.64%` | `97.00` |
| `Live` | `Short` | `2.06` | 17,730,000.00 USD | 460.50 USD | 0.00 USD | `+65.24%` | `223.00` |
| `Live` | `Short` | `2.08` | 17,730,000.00 USD | 296.73 USD | 0.00 USD | `+66.04%` | `143.00` |
| `Live` | `Short` | `2.10` | 17,730,000.00 USD | 331.01 USD | 0.00 USD | `+67.64%` | `158.00` |
| `Live` | `Short` | `2.10` | 17,730,000.00 USD | 673.60 USD | 0.00 USD | `+68.44%` | `320.00` |
| `Live` | `Short` | `2.12` | 18,150,000.00 USD | 426,100.00 USD | 0.00 USD | `+69.24%` | `201,468.00` |
| `Live` | `Short` | `2.12` | 18,480,000.00 USD | 331,410.00 USD | 0.00 USD | `+70.04%` | `155,959.00` |
| `Live` | `Short` | `2.15` | 18,480,000.00 USD | 433.29 USD | 0.00 USD | `+71.64%` | `202.00` |
| `Live` | `Short` | `2.15` | 18,480,000.00 USD | 196.11 USD | 0.00 USD | `+72.44%` | `91.00` |
| `Live` | `Short` | `2.17` | 18,540,000.00 USD | 52,320.00 USD | 0.00 USD | `+74.04%` | `24,057.00` |
| `Live` | `Short` | `2.19` | 18,540,000.00 USD | 201.02 USD | 0.00 USD | `+74.84%` | `92.00` |
| `Live` | `Short` | `2.21` | 18,540,000.00 USD | 438.80 USD | 0.00 USD | `+76.44%` | `199.00` |
| `Live` | `Short` | `2.21` | 18,540,000.00 USD | 2,140.00 USD | 0.00 USD | `+77.24%` | `965.00` |
| `Live` | `Short` | `2.23` | 18,620,000.00 USD | 82,220.00 USD | 0.00 USD | `+78.04%` | `36,955.00` |
| `Live` | `Short` | `2.23` | 18,620,000.00 USD | 102.81 USD | 0.00 USD | `+78.84%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,620,000.00 USD | 224.50 USD | 0.00 USD | `+79.64%` | `100.00` |
| `Live` | `Short` | `2.25` | 18,630,000.00 USD | 11,380.00 USD | 0.00 USD | `+80.44%` | `5,046.00` |
| `Live` | `Short` | `2.31` | 18,630,000.00 USD | 248.94 USD | 0.00 USD | `+84.44%` | `108.00` |
| `Live` | `Short` | `2.33` | 18,630,000.00 USD | 358.05 USD | 0.00 USD | `+86.04%` | `154.00` |
| `Live` | `Short` | `2.33` | 18,680,000.00 USD | 49,200.00 USD | 0.00 USD | `+86.84%` | `21,072.00` |
| `Live` | `Short` | `2.35` | 18,680,000.00 USD | 180.56 USD | 0.00 USD | `+87.65%` | `77.00` |
| `Live` | `Short` | `2.35` | 18,700,000.00 USD | 13,230.00 USD | 0.00 USD | `+88.45%` | `5,619.00` |
| `Live` | `Short` | `2.37` | 18,720,000.00 USD | 18,290.00 USD | 0.00 USD | `+89.25%` | `7,734.00` |
| `Live` | `Short` | `2.38` | 18,800,000.00 USD | 81,970.00 USD | 0.00 USD | `+90.05%` | `34,513.00` |
| `Live` | `Short` | `2.40` | 18,800,000.00 USD | 4,080.00 USD | 0.00 USD | `+92.45%` | `1,698.00` |
| `Live` | `Short` | `2.42` | 18,800,000.00 USD | 678.62 USD | 0.00 USD | `+93.25%` | `281.00` |
| `Live` | `Short` | `2.42` | 18,830,000.00 USD | 24,250.00 USD | 0.00 USD | `+94.05%` | `10,000.00` |
| `Live` | `Short` | `2.44` | 18,830,000.00 USD | 657.45 USD | 0.00 USD | `+94.85%` | `270.00` |
| `Live` | `Short` | `2.44` | 18,830,000.00 USD | 3,740.00 USD | 0.00 USD | `+95.65%` | `1,528.00` |
| `Live` | `Short` | `2.46` | 22,540,000.00 USD | 3,710,000.00 USD | 0.00 USD | `+96.45%` | `1,511,779.00` |
| `Live` | `Short` | `2.46` | 22,540,000.00 USD | 2,310.00 USD | 0.00 USD | `+97.25%` | `937.00` |
| `Live` | `Short` | `2.48` | 22,550,000.00 USD | 1,860.00 USD | 0.00 USD | `+98.05%` | `750.00` |
| `Live` | `Short` | `2.48` | 24,070,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+98.85%` | `613,782.00` |
| `Live` | `Short` | `2.50` | 24,130,000.00 USD | 59,380.00 USD | 0.00 USD | `+99.65%` | `23,798.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 3,900,000.00 USD | 0.00 USD | 102.00 USD | `-79.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 3,900,000.00 USD | 0.00 USD | 351.50 USD | `-70.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,900,000.00 USD | 0.00 USD | 139.12 USD | `-69.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 3,900,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 3,900,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,890,000.00 USD | 0.00 USD | 408.51 USD | `-64.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,890,000.00 USD | 0.00 USD | 273.00 USD | `-63.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,890,000.00 USD | 0.00 USD | 151.12 USD | `-62.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,890,000.00 USD | 0.00 USD | 142.50 USD | `-61.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,890,000.00 USD | 0.00 USD | 145.50 USD | `-61.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4950` | 3,890,000.00 USD | 0.00 USD | 562.81 USD | `-60.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,890,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 3,890,000.00 USD | 0.00 USD | 285.82 USD | `-58.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,890,000.00 USD | 0.00 USD | 306.60 USD | `-57.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,890,000.00 USD | 0.00 USD | 121.55 USD | `-55.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,890,000.00 USD | 0.00 USD | 656.53 USD | `-54.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,890,000.00 USD | 0.00 USD | 100.62 USD | `-53.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 3,890,000.00 USD | 0.00 USD | 203.75 USD | `-49.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,890,000.00 USD | 0.00 USD | 791.85 USD | `-49.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,890,000.00 USD | 0.00 USD | 573.40 USD | `-48.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,890,000.00 USD | 0.00 USD | 244.31 USD | `-47.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,890,000.00 USD | 0.00 USD | 29,530.00 USD | `-46.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 3,860,000.00 USD | 0.00 USD | 503.55 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 3,860,000.00 USD | 0.00 USD | 480.19 USD | `-45.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,860,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,840,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 3,840,000.00 USD | 0.00 USD | 228.80 USD | `-42.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 3,840,000.00 USD | 0.00 USD | 536.50 USD | `-41.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,840,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,840,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,840,000.00 USD | 0.00 USD | 25,490.00 USD | `-36.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 3,810,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-33.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,500,000.00 USD | 0.00 USD | 1,260.00 USD | `-31.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,500,000.00 USD | 0.00 USD | 690.38 USD | `-29.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,500,000.00 USD | 0.00 USD | 1,400.00 USD | `-29.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,500,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,500,000.00 USD | 0.00 USD | 838.94 USD | `-27.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,500,000.00 USD | 0.00 USD | 338.55 USD | `-26.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,490,000.00 USD | 0.00 USD | 1,060.00 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,490,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,490,000.00 USD | 0.00 USD | 112.46 USD | `-24.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,490,000.00 USD | 0.00 USD | 2,500.00 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,490,000.00 USD | 0.00 USD | 4,010.00 USD | `-22.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,490,000.00 USD | 0.00 USD | 6,300.00 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,480,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,470,000.00 USD | 0.00 USD | 902.47 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,470,000.00 USD | 0.00 USD | 45,660.00 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,430,000.00 USD | 0.00 USD | 4,760.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,420,000.00 USD | 0.00 USD | 1,840.00 USD | `-17.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,420,000.00 USD | 0.00 USD | 48,180.00 USD | `-17.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,370,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,370,000.00 USD | 0.00 USD | 27,270.00 USD | `-15.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,340,000.00 USD | 0.00 USD | 3,960.00 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,340,000.00 USD | 0.00 USD | 48,460.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,290,000.00 USD | 0.00 USD | 3,360.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,290,000.00 USD | 0.00 USD | 16,710.00 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,270,000.00 USD | 0.00 USD | 12,830.00 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,260,000.00 USD | 0.00 USD | 9,410.00 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,250,000.00 USD | 0.00 USD | 77,260.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,170,000.00 USD | 0.00 USD | 13,250.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,160,000.00 USD | 0.00 USD | 118,970.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,040,000.00 USD | 0.00 USD | 58,820.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 981,440.00 USD | 0.00 USD | 17,890.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 963,550.00 USD | 0.00 USD | 92,150.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 871,400.00 USD | 0.00 USD | 251,790.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 619,610.00 USD | 0.00 USD | 201,940.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 417,670.00 USD | 0.00 USD | 93,320.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 324,340.00 USD | 0.00 USD | 23,110.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 301,230.00 USD | 0.00 USD | 113,810.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 187,420.00 USD | 0.00 USD | 58,150.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 129,270.00 USD | 0.00 USD | 129,270.00 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 13,720.00 USD | 13,720.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 24,800.00 USD | 11,080.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 133,190.00 USD | 108,390.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 434,540.00 USD | 301,350.00 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 485,480.00 USD | 50,940.00 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 504,710.00 USD | 19,230.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,120,000.00 USD | 611,440.00 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,240,000.00 USD | 122,550.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,280,000.00 USD | 43,890.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,350,000.00 USD | 70,930.00 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,370,000.00 USD | 14,640.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,420,000.00 USD | 47,040.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,500,000.00 USD | 82,000.00 USD | 0.00 USD | `+10.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,550,000.00 USD | 55,590.00 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,560,000.00 USD | 5,430.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,960,000.00 USD | 4,400,000.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,970,000.00 USD | 3,230.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,970,000.00 USD | 6,460.00 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 5,970,000.00 USD | 1,450.00 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,220,000.00 USD | 242,580.00 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,220,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,240,000.00 USD | 21,280.00 USD | 0.00 USD | `+17.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,350,000.00 USD | 108,020.00 USD | 0.00 USD | `+18.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,370,000.00 USD | 14,870.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,390,000.00 USD | 17,790.00 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,460,000.00 USD | 70,600.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,470,000.00 USD | 11,760.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,490,000.00 USD | 19,430.00 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,530,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,540,000.00 USD | 12,200.00 USD | 0.00 USD | `+23.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,550,000.00 USD | 2,380.00 USD | 0.00 USD | `+24.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,550,000.00 USD | 7,160.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,560,000.00 USD | 5,570.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,570,000.00 USD | 10,570.00 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,710,000.00 USD | 139,120.00 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,710,000.00 USD | 1,840.00 USD | 0.00 USD | `+28.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,790,000.00 USD | 80,330.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,790,000.00 USD | 464.75 USD | 0.00 USD | `+30.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 6,980,000.00 USD | 183,460.00 USD | 0.00 USD | `+30.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 6,980,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,000,000.00 USD | 18,210.00 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,000,000.00 USD | 6,080.00 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,030,000.00 USD | 25,340.00 USD | 0.00 USD | `+34.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,100,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,120,000.00 USD | 18,000.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,370,000.00 USD | 251,050.00 USD | 0.00 USD | `+36.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,380,000.00 USD | 14,250.00 USD | 0.00 USD | `+37.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,380,000.00 USD | 534.75 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,430,000.00 USD | 43,240.00 USD | 0.00 USD | `+38.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,430,000.00 USD | 3,330.00 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,440,000.00 USD | 9,200.00 USD | 0.00 USD | `+40.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,460,000.00 USD | 21,720.00 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,590,000.00 USD | 126,830.00 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,680,000.00 USD | 96,600.00 USD | 0.00 USD | `+42.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,690,000.00 USD | 3,980.00 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,690,000.00 USD | 254.51 USD | 0.00 USD | `+44.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,700,000.00 USD | 11,080.00 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,700,000.00 USD | 3,970.00 USD | 0.00 USD | `+46.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,710,000.00 USD | 8,170.00 USD | 0.00 USD | `+46.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,710,000.00 USD | 843.17 USD | 0.00 USD | `+47.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,720,000.00 USD | 8,390.00 USD | 0.00 USD | `+48.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,720,000.00 USD | 4,420.00 USD | 0.00 USD | `+50.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,730,000.00 USD | 591.89 USD | 0.00 USD | `+50.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,770,000.00 USD | 46,370.00 USD | 0.00 USD | `+51.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,780,000.00 USD | 9,270.00 USD | 0.00 USD | `+52.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,780,000.00 USD | 265.10 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,780,000.00 USD | 2,040.00 USD | 0.00 USD | `+55.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,780,000.00 USD | 807.42 USD | 0.00 USD | `+56.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 7,800,000.00 USD | 14,120.00 USD | 0.00 USD | `+57.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 7,800,000.00 USD | 4,010.00 USD | 0.00 USD | `+58.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 7,800,000.00 USD | 325.54 USD | 0.00 USD | `+58.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,810,000.00 USD | 7,020.00 USD | 0.00 USD | `+59.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,940,000.00 USD | 127,100.00 USD | 0.00 USD | `+60.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 7,940,000.00 USD | 3,350.00 USD | 0.00 USD | `+62.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,940,000.00 USD | 181.12 USD | 0.00 USD | `+62.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,940,000.00 USD | 382.41 USD | 0.00 USD | `+63.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 7,940,000.00 USD | 3,420.00 USD | 0.00 USD | `+65.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 7,940,000.00 USD | 661.93 USD | 0.00 USD | `+66.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,070,000.00 USD | 124,400.00 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,070,000.00 USD | 1,580.00 USD | 0.00 USD | `+68.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,080,000.00 USD | 13,900.00 USD | 0.00 USD | `+70.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,110,000.00 USD | 24,840.00 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,160,000.00 USD | 50,580.00 USD | 0.00 USD | `+72.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,160,000.00 USD | 2,690.00 USD | 0.00 USD | `+73.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,160,000.00 USD | 2,180.00 USD | 0.00 USD | `+75.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,320,000.00 USD | 151,380.00 USD | 0.00 USD | `+77.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,320,000.00 USD | 2,230.00 USD | 0.00 USD | `+82.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,320,000.00 USD | 1,140.00 USD | 0.00 USD | `+82.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,330,000.00 USD | 11,670.00 USD | 0.00 USD | `+83.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,330,000.00 USD | 370.40 USD | 0.00 USD | `+85.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,330,000.00 USD | 733.19 USD | 0.00 USD | `+86.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,330,000.00 USD | 2,410.00 USD | 0.00 USD | `+89.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,340,000.00 USD | 475.00 USD | 0.00 USD | `+90.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,340,000.00 USD | 1,190.00 USD | 0.00 USD | `+90.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,340,000.00 USD | 2,540.00 USD | 0.00 USD | `+91.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,340,000.00 USD | 1,590.00 USD | 0.00 USD | `+92.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,340,000.00 USD | 1,370.00 USD | 0.00 USD | `+93.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,360,000.00 USD | 19,590.00 USD | 0.00 USD | `+94.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,360,000.00 USD | 564.92 USD | 0.00 USD | `+94.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,370,000.00 USD | 3,420.00 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,370,000.00 USD | 124.75 USD | 0.00 USD | `+99.65%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 102,310,000.00 USD | 0.00 USD | 102,310,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `1.09` | 102,310,000.00 USD | 0.00 USD | 102,310,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 102,260,000.00 USD | 0.00 USD | 102,260,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 102,170,000.00 USD | 0.00 USD | 102,170,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 102,130,000.00 USD | 0.00 USD | 102,130,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 102,130,000.00 USD | 0.00 USD | 102,130,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 101,840,000.00 USD | 0.00 USD | 101,840,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 101,840,000.00 USD | 0.00 USD | 101,840,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 101,830,000.00 USD | 0.00 USD | 101,830,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 101,830,000.00 USD | 0.00 USD | 101,830,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.12` | 101,770,000.00 USD | 0.00 USD | 101,770,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `7D` | `1.12` | 101,760,000.00 USD | 0.00 USD | 101,760,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 97,520,000.00 USD | 0.00 USD | 97,520,000.00 USD | 8,700.00 USD | 49,330.00 USD | 149,440.00 USD |
| `1D` | `1.12` | 97,310,000.00 USD | 0.00 USD | 97,310,000.00 USD | 17,600.00 USD | 59,970.00 USD | 233,760.00 USD |
| `7D` | `1.12` | 101,680,000.00 USD | 0.00 USD | 101,680,000.00 USD | 17,190.00 USD | 3,530.00 USD | 108,090.00 USD |
| `1D` | `1.12` | 97,000,000.00 USD | 0.00 USD | 97,000,000.00 USD | 17,670.00 USD | 2,160.00 USD | 86,640.00 USD |
| `7D` | `1.12` | 101,550,000.00 USD | 0.00 USD | 101,550,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.12` | 96,890,000.00 USD | 0.00 USD | 96,890,000.00 USD | 97,300.00 USD | 60,030.00 USD | 172,240.00 USD |
| `7D` | `1.13` | 101,340,000.00 USD | 0.00 USD | 101,340,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD |
| `1D` | `1.13` | 96,560,000.00 USD | 0.00 USD | 96,560,000.00 USD | 33,730.00 USD | 45,760.00 USD | 238,500.00 USD |
| `7D` | `1.13` | 101,200,000.00 USD | 0.00 USD | 101,200,000.00 USD | 0.00 USD | 0.00 USD | 295,180.00 USD |
| `1D` | `1.13` | 96,250,000.00 USD | 0.00 USD | 96,250,000.00 USD | 96,120.00 USD | 82,870.00 USD | 193,810.00 USD |
| `7D` | `1.13` | 100,900,000.00 USD | 0.00 USD | 100,900,000.00 USD | 5,450.00 USD | 55,710.00 USD | 98,170.00 USD |
| `1D` | `1.13` | 95,870,000.00 USD | 0.00 USD | 95,870,000.00 USD | 9,300.00 USD | 115,610.00 USD | 421,780.00 USD |
| `7D` | `1.13` | 100,740,000.00 USD | 0.00 USD | 100,740,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD |
| `1D` | `1.13` | 95,330,000.00 USD | 0.00 USD | 95,330,000.00 USD | 88,690.00 USD | 54,850.00 USD | 41,560.00 USD |
| `7D` | `1.13` | 100,370,000.00 USD | 0.00 USD | 100,370,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 95,140,000.00 USD | 0.00 USD | 95,140,000.00 USD | 4,270.00 USD | 165,790.00 USD | 224,860.00 USD |
| `7D` | `1.14` | 99,890,000.00 USD | 0.00 USD | 99,890,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD |
| `1D` | `1.14` | 94,750,000.00 USD | 0.00 USD | 94,750,000.00 USD | 81,050.00 USD | 49,270.00 USD | 97,090.00 USD |
| `7D` | `1.14` | 99,350,000.00 USD | 0.00 USD | 99,350,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 94,520,000.00 USD | 0.00 USD | 94,520,000.00 USD | 26,280.00 USD | 52,480.00 USD | 107,470.00 USD |
| `7D` | `1.14` | 99,320,000.00 USD | 0.00 USD | 99,320,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD |
| `1D` | `1.14` | 94,330,000.00 USD | 0.00 USD | 94,330,000.00 USD | 29,510.00 USD | 10,080.00 USD | 153,170.00 USD |
| `7D` | `1.14` | 98,970,000.00 USD | 0.00 USD | 98,970,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 94,140,000.00 USD | 0.00 USD | 94,140,000.00 USD | 89,980.00 USD | 1,070.00 USD | 49,840.00 USD |
| `7D` | `1.14` | 98,830,000.00 USD | 0.00 USD | 98,830,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `1D` | `1.15` | 94,000,000.00 USD | 0.00 USD | 94,000,000.00 USD | 5,140.00 USD | 0.00 USD | 33,610.00 USD |
| `7D` | `1.15` | 98,820,000.00 USD | 0.00 USD | 98,820,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.15` | 98,760,000.00 USD | 0.00 USD | 98,760,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `1D` | `1.15` | 93,960,000.00 USD | 0.00 USD | 93,960,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 98,390,000.00 USD | 0.00 USD | 98,390,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 93,940,000.00 USD | 0.00 USD | 93,940,000.00 USD | 0.00 USD | 75.47 USD | 0.00 USD |
| `7D` | `1.15` | 98,240,000.00 USD | 0.00 USD | 98,240,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 93,940,000.00 USD | 0.00 USD | 93,940,000.00 USD | 4,040.00 USD | 14,940.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 98,070,000.00 USD | 0.00 USD | 98,070,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 93,740,000.00 USD | 0.00 USD | 93,740,000.00 USD | 91,040.00 USD | 52,340.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 97,190,000.00 USD | 0.00 USD | 97,190,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 93,400,000.00 USD | 0.00 USD | 93,400,000.00 USD | 70,730.00 USD | 14,020.00 USD | 30,130.00 USD |
| `7D` | `1.16` | 96,960,000.00 USD | 0.00 USD | 96,960,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 93,290,000.00 USD | 0.00 USD | 93,290,000.00 USD | 111,450.00 USD | 15,410.00 USD | 409,490.00 USD |
| `7D` | `1.16` | 96,090,000.00 USD | 0.00 USD | 96,090,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 92,750,000.00 USD | 0.00 USD | 92,750,000.00 USD | 160,420.00 USD | 55,490.00 USD | 116,840.00 USD |
| `7D` | `1.16` | 95,010,000.00 USD | 0.00 USD | 95,010,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 92,420,000.00 USD | 0.00 USD | 92,420,000.00 USD | 111,610.00 USD | 268,790.00 USD | 256,680.00 USD |
| `7D` | `1.16` | 93,710,000.00 USD | 0.00 USD | 93,710,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 91,780,000.00 USD | 0.00 USD | 91,780,000.00 USD | 59,160.00 USD | 8,460.00 USD | 473,830.00 USD |
| `7D` | `1.17` | 92,040,000.00 USD | 0.00 USD | 92,040,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 91,240,000.00 USD | 0.00 USD | 91,240,000.00 USD | 121,070.00 USD | 105,910.00 USD | 85,820.00 USD |
| `7D` | `1.17` | 90,700,000.00 USD | 0.00 USD | 90,700,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 90,930,000.00 USD | 0.00 USD | 90,930,000.00 USD | 101,220.00 USD | 97,850.00 USD | 206,520.00 USD |
| `7D` | `1.17` | 89,630,000.00 USD | 0.00 USD | 89,630,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 90,520,000.00 USD | 0.00 USD | 90,520,000.00 USD | 361,890.00 USD | 3,860.00 USD | 415,800.00 USD |
| `7D` | `1.17` | 87,590,000.00 USD | 0.00 USD | 87,590,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 89,740,000.00 USD | 0.00 USD | 89,740,000.00 USD | 104,550.00 USD | 77,530.00 USD | 338,000.00 USD |
| `7D` | `1.17` | 86,390,000.00 USD | 0.00 USD | 86,390,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 89,220,000.00 USD | 0.00 USD | 89,220,000.00 USD | 396,370.00 USD | 140,940.00 USD | 416,380.00 USD |
| `7D` | `1.18` | 84,820,000.00 USD | 0.00 USD | 84,820,000.00 USD | 181,850.00 USD | 71,240.00 USD | 311,840.00 USD |
| `1D` | `1.18` | 88,260,000.00 USD | 0.00 USD | 88,260,000.00 USD | 71,610.00 USD | 43,850.00 USD | 250,850.00 USD |
| `7D` | `1.18` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 85,020.00 USD | 27,270.00 USD | 380,570.00 USD |
| `1D` | `1.18` | 87,900,000.00 USD | 0.00 USD | 87,900,000.00 USD | 90,040.00 USD | 41,360.00 USD | 198,520.00 USD |
| `7D` | `1.18` | 83,770,000.00 USD | 0.00 USD | 83,770,000.00 USD | 267,580.00 USD | 112,520.00 USD | 194,450.00 USD |
| `1D` | `1.18` | 87,570,000.00 USD | 0.00 USD | 87,570,000.00 USD | 144,240.00 USD | 13,850.00 USD | 6,800.00 USD |
| `7D` | `1.18` | 83,190,000.00 USD | 0.00 USD | 83,190,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 87,400,000.00 USD | 0.00 USD | 87,400,000.00 USD | 150,010.00 USD | 34,200.00 USD | 660,810.00 USD |
| `7D` | `1.18` | 82,920,000.00 USD | 0.00 USD | 82,920,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 86,560,000.00 USD | 0.00 USD | 86,560,000.00 USD | 225,800.00 USD | 59,960.00 USD | 143,880.00 USD |
| `7D` | `1.19` | 81,820,000.00 USD | 0.00 USD | 81,820,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 86,130,000.00 USD | 0.00 USD | 86,130,000.00 USD | 109,160.00 USD | 514,490.00 USD | 653,320.00 USD |
| `7D` | `1.19` | 80,970,000.00 USD | 0.00 USD | 80,970,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD |
| `1D` | `1.19` | 84,850,000.00 USD | 0.00 USD | 84,850,000.00 USD | 360,560.00 USD | 84,730.00 USD | 1,290,000.00 USD |
| `7D` | `1.19` | 80,180,000.00 USD | 0.00 USD | 80,180,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD |
| `1D` | `1.19` | 83,120,000.00 USD | 0.00 USD | 83,120,000.00 USD | 61,250.00 USD | 47,690.00 USD | 373,810.00 USD |
| `7D` | `1.19` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 82,630,000.00 USD | 0.00 USD | 82,630,000.00 USD | 161,950.00 USD | 512,200.00 USD | 449,720.00 USD |
| `7D` | `1.19` | 77,840,000.00 USD | 0.00 USD | 77,840,000.00 USD | 229,630.00 USD | 59,450.00 USD | 558,970.00 USD |
| `1D` | `1.20` | 81,510,000.00 USD | 0.00 USD | 81,510,000.00 USD | 383,970.00 USD | 161,130.00 USD | 2,250,000.00 USD |
| `7D` | `1.20` | 76,990,000.00 USD | 0.00 USD | 76,990,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 707,370.00 USD |
| `1D` | `1.20` | 78,710,000.00 USD | 0.00 USD | 78,710,000.00 USD | 749,510.00 USD | 76,460.00 USD | 1,010,000.00 USD |
| `7D` | `1.20` | 74,980,000.00 USD | 0.00 USD | 74,980,000.00 USD | 31,150.00 USD | 373,690.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 76,880,000.00 USD | 0.00 USD | 76,880,000.00 USD | 246,130.00 USD | 945,930.00 USD | 1,610,000.00 USD |
| `7D` | `1.20` | 71,970,000.00 USD | 0.00 USD | 71,970,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD |
| `1D` | `1.20` | 74,080,000.00 USD | 0.00 USD | 74,080,000.00 USD | 873,590.00 USD | 593,880.00 USD | 2,130,000.00 USD |
| `7D` | `1.20` | 70,510,000.00 USD | 0.00 USD | 70,510,000.00 USD | 337,020.00 USD | 144,630.00 USD | 622,930.00 USD |
| `1D` | `1.20` | 70,480,000.00 USD | 0.00 USD | 70,480,000.00 USD | 388,410.00 USD | 160,660.00 USD | 945,900.00 USD |
| `7D` | `1.20` | 69,400,000.00 USD | 0.00 USD | 69,400,000.00 USD | 47,500.00 USD | 723,100.00 USD | 407,740.00 USD |
| `1D` | `1.21` | 68,990,000.00 USD | 0.00 USD | 68,990,000.00 USD | 433,580.00 USD | 976,200.00 USD | 376,690.00 USD |
| `7D` | `1.21` | 68,230,000.00 USD | 0.00 USD | 68,230,000.00 USD | 0.00 USD | 77,080.00 USD | 245,420.00 USD |
| `1D` | `1.21` | 67,200,000.00 USD | 0.00 USD | 67,200,000.00 USD | 892,680.00 USD | 237,590.00 USD | 2,050,000.00 USD |
| `7D` | `1.21` | 67,900,000.00 USD | 0.00 USD | 67,900,000.00 USD | 556,190.00 USD | 0.00 USD | 635,770.00 USD |
| `1D` | `1.21` | 64,020,000.00 USD | 0.00 USD | 64,020,000.00 USD | 1,710,000.00 USD | 282,950.00 USD | 953,880.00 USD |
| `7D` | `1.21` | 66,710,000.00 USD | 0.00 USD | 66,710,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD |
| `1D` | `1.21` | 61,080,000.00 USD | 0.00 USD | 61,080,000.00 USD | 227,840.00 USD | 771,870.00 USD | 2,040,000.00 USD |
| `7D` | `1.21` | 62,500,000.00 USD | 0.00 USD | 62,500,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD |
| `1D` | `1.21` | 58,050,000.00 USD | 0.00 USD | 58,050,000.00 USD | 1,480,000.00 USD | 336,510.00 USD | 1,300,000.00 USD |
| `7D` | `1.21` | 60,250,000.00 USD | 0.00 USD | 60,250,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD |
| `1D` | `1.22` | 54,930,000.00 USD | 0.00 USD | 54,930,000.00 USD | 56,590.00 USD | 268,640.00 USD | 1,010,000.00 USD |
| `7D` | `1.22` | 58,720,000.00 USD | 0.00 USD | 58,720,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD |
| `1D` | `1.22` | 53,600,000.00 USD | 0.00 USD | 53,600,000.00 USD | 307,460.00 USD | 62,180.00 USD | 538,990.00 USD |
| `7D` | `1.22` | 58,320,000.00 USD | 0.00 USD | 58,320,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 52,690,000.00 USD | 0.00 USD | 52,690,000.00 USD | 212,220.00 USD | 53,890.00 USD | 422,030.00 USD |
| `7D` | `1.22` | 57,580,000.00 USD | 0.00 USD | 57,580,000.00 USD | 156,790.00 USD | 928,300.00 USD | 569,650.00 USD |
| `1D` | `1.22` | 52,000,000.00 USD | 0.00 USD | 52,000,000.00 USD | 70,250.00 USD | 321,780.00 USD | 735,560.00 USD |
| `7D` | `1.22` | 55,930,000.00 USD | 0.00 USD | 55,930,000.00 USD | 0.00 USD | 167,460.00 USD | 340,920.00 USD |
| `1D` | `1.22` | 50,870,000.00 USD | 0.00 USD | 50,870,000.00 USD | 187,090.00 USD | 1,280.00 USD | 554,820.00 USD |
| `7D` | `1.22` | 55,420,000.00 USD | 0.00 USD | 55,420,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 50,130,000.00 USD | 0.00 USD | 50,130,000.00 USD | 658,900.00 USD | 664,730.00 USD | 3,190,000.00 USD |
| `7D` | `1.23` | 55,160,000.00 USD | 0.00 USD | 55,160,000.00 USD | 258,810.00 USD | 802,580.00 USD | 790,120.00 USD |
| `1D` | `1.23` | 45,620,000.00 USD | 0.00 USD | 45,620,000.00 USD | 274,000.00 USD | 319,850.00 USD | 842,310.00 USD |
| `7D` | `1.23` | 53,310,000.00 USD | 0.00 USD | 53,310,000.00 USD | 59,160.00 USD | 950,550.00 USD | 538,800.00 USD |
| `1D` | `1.23` | 44,180,000.00 USD | 0.00 USD | 44,180,000.00 USD | 786,440.00 USD | 1,220,000.00 USD | 2,810,000.00 USD |
| `7D` | `1.23` | 51,760,000.00 USD | 0.00 USD | 51,760,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 39,360,000.00 USD | 0.00 USD | 39,360,000.00 USD | 292,800.00 USD | 1,360,000.00 USD | 3,340,000.00 USD |
| `7D` | `1.23` | 48,810,000.00 USD | 0.00 USD | 48,810,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 34,370,000.00 USD | 0.00 USD | 34,370,000.00 USD | 1,560,000.00 USD | 805,110.00 USD | 3,670,000.00 USD |
| `7D` | `1.23` | 45,120,000.00 USD | 0.00 USD | 45,120,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 6,100,000.00 USD |
| `1D` | `1.24` | 28,340,000.00 USD | 0.00 USD | 28,340,000.00 USD | 511,510.00 USD | 1,630,000.00 USD | 3,010,000.00 USD |
| `7D` | `1.24` | 35,370,000.00 USD | 0.00 USD | 35,370,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD |
| `1D` | `1.24` | 23,190,000.00 USD | 0.00 USD | 23,190,000.00 USD | 543,000.00 USD | 569,580.00 USD | 1,260,000.00 USD |
| `7D` | `1.24` | 28,210,000.00 USD | 0.00 USD | 28,210,000.00 USD | 3,160,000.00 USD | 2,120,000.00 USD | 5,050,000.00 USD |
| `1D` | `1.24` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 918,230.00 USD | 1,140,000.00 USD | 3,850,000.00 USD |
| `7D` | `1.24` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 2,290,000.00 USD |
| `1D` | `1.24` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 1,130,000.00 USD | 666,510.00 USD | 1,990,000.00 USD |
| `7D` | `1.24` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 2,060,000.00 USD |
| `1D` | `1.24` | 11,130,000.00 USD | 0.00 USD | 11,130,000.00 USD | 964,230.00 USD | 1,090,000.00 USD | 3,560,000.00 USD |
| `7D` | `1.24` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 0.00 USD |
| `1D` | `1.25` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 1,700,000.00 USD | 718,690.00 USD | 525,240.00 USD |
| `7D` | `1.25` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 0.00 USD |
| `1D` | `1.25` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 885,060.00 USD | 986,030.00 USD | 0.00 USD |
| `7D` | `1.25` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 0.00 USD |
| `1D` | `1.25` | 709,140.00 USD | 0.00 USD | 709,140.00 USD | 0.00 USD | 709,140.00 USD | 0.00 USD |
| `7D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 242,040.00 USD | 242,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 242,040.00 USD |
| `1D` | `1.25` | 484,080.00 USD | 484,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 242,040.00 USD |
| `7D` | `1.26` | 158,820.00 USD | 158,820.00 USD | 0.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD |
| `1D` | `1.26` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 822,520.00 USD |
| `7D` | `1.26` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 1,740,000.00 USD |
| `1D` | `1.26` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 856,480.00 USD |
| `7D` | `1.26` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD |
| `1D` | `1.26` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 259,050.00 USD | 7,900.00 USD | 379,020.00 USD |
| `7D` | `1.26` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD |
| `1D` | `1.26` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 409,480.00 USD | 372,590.00 USD | 1,150,000.00 USD |
| `7D` | `1.26` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 292,090.00 USD | 542,940.00 USD | 1,640,000.00 USD |
| `1D` | `1.26` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 636,140.00 USD | 522,800.00 USD | 1,460,000.00 USD |
| `7D` | `1.27` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 4,260,000.00 USD | 9,150.00 USD | 1,030,000.00 USD |
| `1D` | `1.27` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 1,130,000.00 USD | 252,140.00 USD | 685,300.00 USD |
| `7D` | `1.27` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 0.00 USD | 1,870,000.00 USD | 4,090,000.00 USD |
| `1D` | `1.27` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 874,880.00 USD | 1,910,000.00 USD | 2,690,000.00 USD |
| `7D` | `1.27` | 21,170,000.00 USD | 21,170,000.00 USD | 0.00 USD | 156,790.00 USD | 2,750,000.00 USD | 2,450,000.00 USD |
| `1D` | `1.27` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 740,490.00 USD | 1,650,000.00 USD | 3,920,000.00 USD |
| `7D` | `1.27` | 30,910,000.00 USD | 30,910,000.00 USD | 0.00 USD | 1,680,000.00 USD | 5,310,000.00 USD | 2,750,000.00 USD |
| `1D` | `1.27` | 27,820,000.00 USD | 27,820,000.00 USD | 0.00 USD | 2,420,000.00 USD | 1,290,000.00 USD | 2,890,000.00 USD |
| `7D` | `1.27` | 48,250,000.00 USD | 48,250,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD |
| `1D` | `1.27` | 36,130,000.00 USD | 36,130,000.00 USD | 0.00 USD | 1,200,000.00 USD | 2,600,000.00 USD | 4,510,000.00 USD |
| `7D` | `1.28` | 63,570,000.00 USD | 63,570,000.00 USD | 0.00 USD | 5,290,000.00 USD | 3,080,000.00 USD | 6,950,000.00 USD |
| `1D` | `1.28` | 43,480,000.00 USD | 43,480,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,430,000.00 USD | 3,820,000.00 USD |
| `7D` | `1.28` | 83,240,000.00 USD | 83,240,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 8,130,000.00 USD |
| `1D` | `1.28` | 51,460,000.00 USD | 51,460,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,980,000.00 USD | 3,660,000.00 USD |
| `7D` | `1.28` | 86,830,000.00 USD | 86,830,000.00 USD | 0.00 USD | 0.00 USD | 1,700,000.00 USD | 1,890,000.00 USD |
| `1D` | `1.28` | 55,770,000.00 USD | 55,770,000.00 USD | 0.00 USD | 483,960.00 USD | 826,970.00 USD | 3,000,000.00 USD |
| `7D` | `1.28` | 88,860,000.00 USD | 88,860,000.00 USD | 0.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD |
| `1D` | `1.28` | 59,890,000.00 USD | 59,890,000.00 USD | 0.00 USD | 1,340,000.00 USD | 598,170.00 USD | 2,180,000.00 USD |
| `7D` | `1.28` | 93,110,000.00 USD | 93,110,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD |
| `1D` | `1.28` | 63,470,000.00 USD | 63,470,000.00 USD | 0.00 USD | 904,370.00 USD | 743,290.00 USD | 1,930,000.00 USD |
| `7D` | `1.29` | 98,240,000.00 USD | 98,240,000.00 USD | 0.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.29` | 66,720,000.00 USD | 66,720,000.00 USD | 0.00 USD | 864,310.00 USD | 1,100,000.00 USD | 1,290,000.00 USD |
| `7D` | `1.29` | 98,960,000.00 USD | 98,960,000.00 USD | 0.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 67,840,000.00 USD | 67,840,000.00 USD | 0.00 USD | 454,460.00 USD | 142,490.00 USD | 518,370.00 USD |
| `7D` | `1.29` | 100,560,000.00 USD | 100,560,000.00 USD | 0.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD |
| `1D` | `1.29` | 69,220,000.00 USD | 69,220,000.00 USD | 0.00 USD | 186,090.00 USD | 275,630.00 USD | 919,950.00 USD |
| `7D` | `1.29` | 103,160,000.00 USD | 103,160,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD |
| `1D` | `1.29` | 73,030,000.00 USD | 73,030,000.00 USD | 0.00 USD | 574,390.00 USD | 275,550.00 USD | 2,960,000.00 USD |
| `7D` | `1.29` | 106,820,000.00 USD | 106,820,000.00 USD | 0.00 USD | 1,780,000.00 USD | 8,810.00 USD | 1,880,000.00 USD |
| `1D` | `1.29` | 79,410,000.00 USD | 79,410,000.00 USD | 0.00 USD | 1,880,000.00 USD | 720,770.00 USD | 3,780,000.00 USD |
| `7D` | `1.30` | 114,540,000.00 USD | 114,540,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 4,170,000.00 USD |
| `1D` | `1.30` | 82,200,000.00 USD | 82,200,000.00 USD | 0.00 USD | 555,660.00 USD | 702,980.00 USD | 1,540,000.00 USD |
| `7D` | `1.30` | 116,490,000.00 USD | 116,490,000.00 USD | 0.00 USD | 25,800.00 USD | 173,700.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 83,190,000.00 USD | 83,190,000.00 USD | 0.00 USD | 468,600.00 USD | 109,540.00 USD | 408,290.00 USD |
| `7D` | `1.30` | 118,870,000.00 USD | 118,870,000.00 USD | 0.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD |
| `1D` | `1.30` | 86,210,000.00 USD | 86,210,000.00 USD | 0.00 USD | 674,250.00 USD | 493,820.00 USD | 1,850,000.00 USD |
| `7D` | `1.30` | 120,130,000.00 USD | 120,130,000.00 USD | 0.00 USD | 158,990.00 USD | 944,610.00 USD | 158,700.00 USD |
| `1D` | `1.30` | 88,270,000.00 USD | 88,270,000.00 USD | 0.00 USD | 835,040.00 USD | 564,380.00 USD | 660,910.00 USD |
| `7D` | `1.30` | 123,190,000.00 USD | 123,190,000.00 USD | 0.00 USD | 0.00 USD | 2,170,000.00 USD | 887,870.00 USD |
| `1D` | `1.30` | 89,870,000.00 USD | 89,870,000.00 USD | 0.00 USD | 441,960.00 USD | 703,580.00 USD | 458,020.00 USD |
| `7D` | `1.31` | 125,440,000.00 USD | 125,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 238,140.00 USD | 245,420.00 USD |
| `1D` | `1.31` | 93,170,000.00 USD | 93,170,000.00 USD | 0.00 USD | 803,720.00 USD | 281,570.00 USD | 2,210,000.00 USD |
| `7D` | `1.31` | 130,860,000.00 USD | 130,860,000.00 USD | 0.00 USD | 1,550,000.00 USD | 821,310.00 USD | 3,040,000.00 USD |
| `1D` | `1.31` | 96,880,000.00 USD | 96,880,000.00 USD | 0.00 USD | 1,270,000.00 USD | 481,050.00 USD | 1,960,000.00 USD |
| `7D` | `1.31` | 133,620,000.00 USD | 133,620,000.00 USD | 0.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD |
| `1D` | `1.31` | 99,660,000.00 USD | 99,660,000.00 USD | 0.00 USD | 966,790.00 USD | 606,030.00 USD | 1,200,000.00 USD |
| `7D` | `1.31` | 138,500,000.00 USD | 138,500,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD |
| `1D` | `1.31` | 101,560,000.00 USD | 101,560,000.00 USD | 0.00 USD | 499,000.00 USD | 340,130.00 USD | 1,060,000.00 USD |
| `7D` | `1.31` | 139,790,000.00 USD | 139,790,000.00 USD | 0.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.31` | 103,630,000.00 USD | 103,630,000.00 USD | 0.00 USD | 415,520.00 USD | 266,240.00 USD | 1,390,000.00 USD |
| `7D` | `1.32` | 144,510,000.00 USD | 144,510,000.00 USD | 0.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.32` | 108,200,000.00 USD | 108,200,000.00 USD | 0.00 USD | 1,260,000.00 USD | 636,870.00 USD | 2,680,000.00 USD |
| `7D` | `1.32` | 149,610,000.00 USD | 149,610,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD |
| `1D` | `1.32` | 112,310,000.00 USD | 112,310,000.00 USD | 0.00 USD | 1,150,000.00 USD | 582,420.00 USD | 2,370,000.00 USD |
| `7D` | `1.32` | 151,630,000.00 USD | 151,630,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 114,560,000.00 USD | 114,560,000.00 USD | 0.00 USD | 1,320,000.00 USD | 195,100.00 USD | 744,150.00 USD |
| `7D` | `1.32` | 154,980,000.00 USD | 154,980,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 117,470,000.00 USD | 117,470,000.00 USD | 0.00 USD | 885,300.00 USD | 456,600.00 USD | 1,560,000.00 USD |
| `7D` | `1.32` | 157,760,000.00 USD | 157,760,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.32` | 118,470,000.00 USD | 118,470,000.00 USD | 0.00 USD | 599,940.00 USD | 60,300.00 USD | 341,150.00 USD |
| `7D` | `1.33` | 159,570,000.00 USD | 159,570,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 119,540,000.00 USD | 119,540,000.00 USD | 0.00 USD | 412,050.00 USD | 224,860.00 USD | 436,220.00 USD |
| `7D` | `1.33` | 160,670,000.00 USD | 160,670,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 120,920,000.00 USD | 120,920,000.00 USD | 0.00 USD | 504,110.00 USD | 75,550.00 USD | 798,680.00 USD |
| `7D` | `1.33` | 162,380,000.00 USD | 162,380,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 123,090,000.00 USD | 123,090,000.00 USD | 0.00 USD | 848,670.00 USD | 99,880.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 164,850,000.00 USD | 164,850,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 125,040,000.00 USD | 125,040,000.00 USD | 0.00 USD | 737,030.00 USD | 194,010.00 USD | 1,020,000.00 USD |
| `7D` | `1.33` | 166,870,000.00 USD | 166,870,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.33` | 126,370,000.00 USD | 126,370,000.00 USD | 0.00 USD | 459,140.00 USD | 355,590.00 USD | 517,170.00 USD |
| `7D` | `1.34` | 168,420,000.00 USD | 168,420,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 127,110,000.00 USD | 127,110,000.00 USD | 0.00 USD | 384,130.00 USD | 22,640.00 USD | 331,600.00 USD |
| `7D` | `1.34` | 170,860,000.00 USD | 170,860,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 127,590,000.00 USD | 127,590,000.00 USD | 0.00 USD | 134,820.00 USD | 84,090.00 USD | 260,400.00 USD |
| `7D` | `1.34` | 172,710,000.00 USD | 172,710,000.00 USD | 0.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 128,690,000.00 USD | 128,690,000.00 USD | 0.00 USD | 496,210.00 USD | 196,970.00 USD | 401,080.00 USD |
| `7D` | `1.34` | 178,180,000.00 USD | 178,180,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 129,830,000.00 USD | 129,830,000.00 USD | 0.00 USD | 579,000.00 USD | 162,370.00 USD | 406,200.00 USD |
| `7D` | `1.34` | 185,300,000.00 USD | 185,300,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.34` | 130,820,000.00 USD | 130,820,000.00 USD | 0.00 USD | 291,740.00 USD | 235,320.00 USD | 457,850.00 USD |
| `7D` | `1.35` | 193,560,000.00 USD | 193,560,000.00 USD | 0.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD |
| `1D` | `1.35` | 131,060,000.00 USD | 131,060,000.00 USD | 0.00 USD | 112,770.00 USD | 30,480.00 USD | 96,690.00 USD |
| `7D` | `1.35` | 201,310,000.00 USD | 201,310,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 131,610,000.00 USD | 131,610,000.00 USD | 0.00 USD | 249,180.00 USD | 21,780.00 USD | 275,620.00 USD |
| `7D` | `1.35` | 209,330,000.00 USD | 209,330,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 132,020,000.00 USD | 132,020,000.00 USD | 0.00 USD | 146,270.00 USD | 30,050.00 USD | 237,640.00 USD |
| `7D` | `1.35` | 218,450,000.00 USD | 218,450,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 132,170,000.00 USD | 132,170,000.00 USD | 0.00 USD | 66,220.00 USD | 30,090.00 USD | 49,480.00 USD |
| `7D` | `1.35` | 225,200,000.00 USD | 225,200,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.35` | 132,680,000.00 USD | 132,680,000.00 USD | 0.00 USD | 86,720.00 USD | 36,350.00 USD | 395,480.00 USD |
| `7D` | `1.36` | 231,530,000.00 USD | 231,530,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 133,640,000.00 USD | 133,640,000.00 USD | 0.00 USD | 391,410.00 USD | 32,490.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 234,070,000.00 USD | 234,070,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD |
| `1D` | `1.36` | 133,970,000.00 USD | 133,970,000.00 USD | 0.00 USD | 209,880.00 USD | 43,130.00 USD | 82,650.00 USD |
| `7D` | `1.36` | 236,720,000.00 USD | 236,720,000.00 USD | 0.00 USD | 1,300,000.00 USD | 282,890.00 USD | 1,060,000.00 USD |
| `1D` | `1.36` | 134,630,000.00 USD | 134,630,000.00 USD | 0.00 USD | 225,120.00 USD | 162,660.00 USD | 269,830.00 USD |
| `7D` | `1.36` | 239,980,000.00 USD | 239,980,000.00 USD | 0.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,140,000.00 USD |
| `1D` | `1.36` | 134,930,000.00 USD | 134,930,000.00 USD | 0.00 USD | 130,140.00 USD | 2,390.00 USD | 166,000.00 USD |
| `7D` | `1.36` | 242,720,000.00 USD | 242,720,000.00 USD | 0.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD |
| `1D` | `1.36` | 135,050,000.00 USD | 135,050,000.00 USD | 0.00 USD | 0.00 USD | 13,170.00 USD | 107,470.00 USD |
| `7D` | `1.37` | 243,540,000.00 USD | 243,540,000.00 USD | 0.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 135,310,000.00 USD | 135,310,000.00 USD | 0.00 USD | 61,210.00 USD | 90,280.00 USD | 103,780.00 USD |
| `7D` | `1.37` | 244,590,000.00 USD | 244,590,000.00 USD | 0.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 135,510,000.00 USD | 135,510,000.00 USD | 0.00 USD | 93,070.00 USD | 20,920.00 USD | 86,650.00 USD |
| `7D` | `1.37` | 246,010,000.00 USD | 246,010,000.00 USD | 0.00 USD | 367,350.00 USD | 211,750.00 USD | 841,910.00 USD |
| `1D` | `1.37` | 135,700,000.00 USD | 135,700,000.00 USD | 0.00 USD | 6,510.00 USD | 39,050.00 USD | 147,110.00 USD |
| `7D` | `1.37` | 247,250,000.00 USD | 247,250,000.00 USD | 0.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD |
| `1D` | `1.37` | 135,810,000.00 USD | 135,810,000.00 USD | 0.00 USD | 17,670.00 USD | 2,160.00 USD | 86,640.00 USD |
| `7D` | `1.37` | 248,910,000.00 USD | 248,910,000.00 USD | 0.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD |
| `1D` | `1.38` | 136,140,000.00 USD | 136,140,000.00 USD | 0.00 USD | 97,300.00 USD | 60,030.00 USD | 172,240.00 USD |
| `7D` | `1.38` | 249,940,000.00 USD | 249,940,000.00 USD | 0.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD |
| `1D` | `1.38` | 136,450,000.00 USD | 136,450,000.00 USD | 0.00 USD | 33,730.00 USD | 45,760.00 USD | 238,500.00 USD |
| `7D` | `1.38` | 251,500,000.00 USD | 251,500,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 600,610.00 USD |
| `1D` | `1.38` | 136,830,000.00 USD | 136,830,000.00 USD | 0.00 USD | 96,120.00 USD | 82,870.00 USD | 193,810.00 USD |
| `7D` | `1.38` | 253,200,000.00 USD | 253,200,000.00 USD | 0.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 136,900,000.00 USD | 136,900,000.00 USD | 0.00 USD | 2,300.00 USD | 71,850.00 USD | 0.00 USD |
| `7D` | `1.38` | 255,160,000.00 USD | 255,160,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 900,700.00 USD |
| `1D` | `1.38` | 137,370,000.00 USD | 137,370,000.00 USD | 0.00 USD | 7,000.00 USD | 43,760.00 USD | 421,780.00 USD |
| `7D` | `1.38` | 256,150,000.00 USD | 256,150,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD |
| `1D` | `1.39` | 137,560,000.00 USD | 137,560,000.00 USD | 0.00 USD | 88,690.00 USD | 54,850.00 USD | 41,560.00 USD |
| `7D` | `1.39` | 257,260,000.00 USD | 257,260,000.00 USD | 0.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 137,950,000.00 USD | 137,950,000.00 USD | 0.00 USD | 4,270.00 USD | 165,790.00 USD | 224,860.00 USD |
| `7D` | `1.39` | 258,470,000.00 USD | 258,470,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD |
| `1D` | `1.39` | 138,180,000.00 USD | 138,180,000.00 USD | 0.00 USD | 81,050.00 USD | 49,270.00 USD | 97,090.00 USD |
| `7D` | `1.39` | 259,220,000.00 USD | 259,220,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `1D` | `1.39` | 138,200,000.00 USD | 138,200,000.00 USD | 0.00 USD | 0.00 USD | 18,330.00 USD | 0.00 USD |
| `7D` | `1.39` | 259,750,000.00 USD | 259,750,000.00 USD | 0.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD |
| `7D` | `1.39` | 259,920,000.00 USD | 259,920,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD |
| `7D` | `1.40` | 260,140,000.00 USD | 260,140,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 260,150,000.00 USD | 260,150,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 260,210,000.00 USD | 260,210,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 260,290,000.00 USD | 260,290,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 260,580,000.00 USD | 260,580,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 260,730,000.00 USD | 260,730,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 260,880,000.00 USD | 260,880,000.00 USD | 0.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD |
| `7D` | `1.41` | 261,160,000.00 USD | 261,160,000.00 USD | 0.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.83B` | Total OI Tokens: `2,253,467,500.1 XRP`
  * 1h OI Change: `+0.03%` | 4h OI Change: `-1.38%` | 24h OI Change: `-5.92%`
  * Exchange Breakdown: Binance=`424.92M` | Bybit=`326.48M` | OKX=`96.58M` | Hyperliquid=`198.62M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-22.66K` | Last 24h: `21.94K` | Last 3d: `414.05K` | Last 7d: `1.06M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0112%` |
| **USDT Bybit** | `-0.0163%` | **USDT KuCoin** | `-0.0077%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0012%` | **USDT Bitget** | `-0.0034%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-0.0060%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `46.13%` | `53.87%` | `0.86` | 18,010,000.00 USD |
| `15M` | `Binance` | `54.36%` | `45.64%` | `1.19` | 5,830,000.00 USD |
| `15M` | `OKX` | `43.07%` | `56.93%` | `0.76` | 1,730,000.00 USD |
| `15M` | `Bybit` | `46.59%` | `53.41%` | `0.87` | 2,420,000.00 USD |
| `15M` | `KuCoin` | `73.99%` | `26.01%` | `2.84` | 89,910.00 USD |
| `15M` | `Gate` | `53.87%` | `46.13%` | `1.17` | 487,550.00 USD |
| `15M` | `Bitget` | `52.58%` | `47.42%` | `1.11` | 1,080,000.00 USD |
| `15M` | `BingX` | `37.74%` | `62.26%` | `0.61` | 284,510.00 USD |
| `15M` | `MEXC` | `48.04%` | `51.96%` | `0.92` | 2,440,000.00 USD |
| `15M` | `Bitunix` | `52.61%` | `47.39%` | `1.11` | 1,190,000.00 USD |
| `15M` | `Hyperliquid` | `50.45%` | `49.55%` | `1.02` | 576,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.56%` | `56.44%` | `0.77` | 92,080.00 USD |
| `15M` | `Crypto.com` | `59.08%` | `40.92%` | `1.44` | 34,950.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,510,000.00 USD |
| `15M` | `HTX` | `50.63%` | `49.37%` | `1.03` | 6,100.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `35.82%` | `64.18%` | `0.56` | 78,960.00 USD |
| `15M` | `Aster` | `48.89%` | `51.11%` | `0.96` | 127,890.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `55.9%` | `44.1%` | `1.27` | 29,390.00 USD |
| `15M` | `Whale Positions` | `54.36%` | `45.64%` | `1.19` | 5,830,000.00 USD |
| `15M` | `Global Accounts` | `46.13%` | `53.87%` | `0.86` | 18,010,000.00 USD |
| `1H` | `XRP` | `43.03%` | `56.97%` | `0.76` | 1,700,000,000.00 USD |
| `1H` | `Binance` | `48.44%` | `51.56%` | `0.94` | 544,000,000.00 USD |
| `1H` | `OKX` | `45.18%` | `54.82%` | `0.82` | 352,660,000.00 USD |
| `1H` | `Bybit` | `34.68%` | `65.32%` | `0.53` | 105,690,000.00 USD |
| `1H` | `KuCoin` | `42.86%` | `57.14%` | `0.75` | 12,050,000.00 USD |
| `1H` | `Gate` | `53.23%` | `46.77%` | `1.14` | 254,160,000.00 USD |
| `1H` | `Bitget` | `55.01%` | `44.99%` | `1.22` | 63,920,000.00 USD |
| `1H` | `BingX` | `32.33%` | `67.67%` | `0.48` | 30,930,000.00 USD |
| `1H` | `MEXC` | `44.62%` | `55.38%` | `0.81` | 69,800,000.00 USD |
| `1H` | `Bitunix` | `49.76%` | `50.24%` | `0.99` | 62,720,000.00 USD |
| `1H` | `Hyperliquid` | `51.49%` | `48.51%` | `1.06` | 104,550,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.95%` | `51.05%` | `0.96` | 3,730,000.00 USD |
| `1H` | `Crypto.com` | `63.54%` | `36.46%` | `1.74` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.25%` | `99.75%` | `0.00` | 10,850,000.00 USD |
| `1H` | `HTX` | `56.65%` | `43.35%` | `1.31` | 24,300,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 11,790,000.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 555,290.00 USD |
| `1H` | `Kraken` | `47.7%` | `52.3%` | `0.91` | 9,690,000.00 USD |
| `1H` | `Aster` | `45.33%` | `54.67%` | `0.83` | 20,260,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.92%` | `51.08%` | `0.96` | 15,610,000.00 USD |
| `1H` | `Whale Positions` | `48.44%` | `51.56%` | `0.94` | 544,000,000.00 USD |
| `1H` | `Global Accounts` | `43.03%` | `56.97%` | `0.76` | 1,700,000,000.00 USD |
| `4H` | `XRP` | `51.13%` | `48.87%` | `1.05` | 6,640,000,000.00 USD |
| `4H` | `Binance` | `50.04%` | `49.96%` | `1.00` | 2,120,000,000.00 USD |
| `4H` | `OKX` | `50.41%` | `49.59%` | `1.02` | 1,180,000,000.00 USD |
| `4H` | `Bybit` | `49.81%` | `50.19%` | `0.99` | 389,100,000.00 USD |
| `4H` | `KuCoin` | `54.75%` | `45.25%` | `1.21` | 28,420,000.00 USD |
| `4H` | `Gate` | `50.92%` | `49.08%` | `1.04` | 962,500,000.00 USD |
| `4H` | `Bitget` | `51.14%` | `48.86%` | `1.05` | 218,570,000.00 USD |
| `4H` | `BingX` | `49.2%` | `50.8%` | `0.97` | 84,010,000.00 USD |
| `4H` | `MEXC` | `52.96%` | `47.04%` | `1.13` | 254,750,000.00 USD |
| `4H` | `Bitunix` | `50.05%` | `49.95%` | `1.00` | 215,840,000.00 USD |
| `4H` | `Hyperliquid` | `49.33%` | `50.67%` | `0.97` | 352,630,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.42%` | `52.58%` | `0.90` | 31,830,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `63.78%` | `36.22%` | `1.76` | 484,650,000.00 USD |
| `4H` | `HTX` | `36.08%` | `63.92%` | `0.56` | 92,170,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `45.13%` | `54.87%` | `0.82` | 74,160,000.00 USD |
| `4H` | `Bitfinex` | `48.49%` | `51.51%` | `0.94` | 2,020,000.00 USD |
| `4H` | `Kraken` | `51.1%` | `48.9%` | `1.04` | 18,950,000.00 USD |
| `4H` | `Aster` | `51.37%` | `48.63%` | `1.06` | 55,910,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.49%` | `46.51%` | `1.15` | 76,520,000.00 USD |
| `4H` | `Whale Positions` | `50.04%` | `49.96%` | `1.00` | 2,120,000,000.00 USD |
| `4H` | `Global Accounts` | `51.13%` | `48.87%` | `1.05` | 6,640,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,021,258.97 USD | 2,177,548.60 USD | 2,843,710.37 USD | -666,161.77 USD | `-13.27%` | `1B / 5S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 4,481,732.50 USD | 2,318,507.74 USD | 2,163,224.76 USD | 155,282.98 USD | `+3.46%` | `9B / 5S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 12,807,415.42 USD | 6,692,980.18 USD | 6,114,435.24 USD | 578,544.93 USD | `+4.52%` | `12B / 4S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,616,675.33 USD | 3,341,703.26 USD | 4,274,972.07 USD | -933,268.81 USD | `-12.25%` | `11B / 16S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 4,530,946.41 USD | 2,213,429.43 USD | 2,317,516.98 USD | -104,087.54 USD | `-2.30%` | `0B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,245,480.96 USD | 2,448,103.42 USD | 2,797,377.55 USD | -349,274.13 USD | `-6.66%` | `3B / 8S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 6,871,051.82 USD | 2,753,850.97 USD | 4,117,200.85 USD | -1,363,349.88 USD | `-19.84%` | `6B / 18S` |
| `5:00 UTC` | `1.24` | `1.25` | `1.24` | `1.25` | `1.24` | 7,510,859.07 USD | 3,308,536.37 USD | 4,202,322.70 USD | -893,786.33 USD | `-11.90%` | `5B / 11S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 11,036,044.54 USD | 6,175,268.47 USD | 4,860,776.07 USD | 1,314,492.40 USD | `+11.91%` | `19B / 7S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 1,156,581.30 USD | 517,044.00 USD | 639,537.30 USD | -122,493.30 USD | `-10.59%` | `6B / 12S` |

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
| `5m` | -7,130.00 USD | -200,250.00 USD | **`DISTRIBUTION`** |
| `15m` | 690,260.00 USD | 1,060,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,870,000.00 USD | 2,470,000.00 USD | **`ACCUMULATION`** |
| `1h` | 912,780.00 USD | -7,580,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,250,000.00 USD | -12,610,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,890,000.00 USD | -27,230,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 8,760,000.00 USD | -12,220,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 21,120,000.00 USD | 11,190,000.00 USD | **`ACCUMULATION`** |
| `12h` | -4,290,000.00 USD | -23,580,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -47,240,000.00 USD | -146,910,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -111,900,000.00 USD | -230,200,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -593,260,000.00 USD | -1,310,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-7.13K` | 15m=`+690.26K` | 1h=`+912.78K` | 24h=`-47.24M`
* Futures Capital Netflows: 5m=`-200.25K` | 15m=`+1.06M` | 1h=`-7.58M` | 24h=`-146.91M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0288` (Risk Distance: `1.20` pts)
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
