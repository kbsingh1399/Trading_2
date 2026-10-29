# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 00:17:12 IST` (`2026-10-29 18:47:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `100.25` | **Live Ask Quote**: `100.50` | **Mid Price**: `100.38`
- **Spread Points**: `25.00` | **Spread BPS**: `24.91 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `100.38` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `101.08` | Lower -3.00σ Band: `99.67`
  * Upper +2.51σ Band: `100.93` | Lower -2.51σ Band: `99.82`
  * Upper +2.01σ Band: `100.80` | Lower -2.01σ Band: `99.95`
  * Upper +2.00σ Band: `100.78` | Lower -2.00σ Band: `99.97`
  * Upper +1.28σ Band: `100.66` | Lower -1.28σ Band: `100.09`
  * Upper +1.00σ Band: `100.58` | Lower -1.00σ Band: `100.17`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`100.38` | EMA-20=`100.38` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`100.38` (Slope: `+0.0000`) | EMA-100=`100.38`
  * Institutional Anchors: EMA-144=`100.38` | EMA-200=`100.38` (Slope: `+0.0000`) | EMA-233=`100.38`
- **Range Boundaries**: 24H High=`101.38` | 24H Low=`99.37` | Weekly High=`102.38` | Weekly Low=`98.37`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `101.32` (Distance: `-0.91%`)
  * Point of Control (POC) = `99.92` (Distance: `+0.48%`)
  * Value Area Low (VAL) = `99.18` (Distance: `+1.23%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.11` | POC=`100.90` | VAL=`100.63`
  * Prior Day Extremes: PDH=`103.63` | PDL=`100.15` | PDC=`102.27`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.48` | Weekly POC=`100.91` | Weekly VAL=`99.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.77` | Low=`98.95`
  * London Session (08:00-16:00 UTC): High=`100.61` | Low=`99.44`
  * New York Session (13:00-21:00 UTC): High=`102.93` | Low=`99.78`
  * Initial Balance (First Hour): IB High=`100.61` | IB Low=`99.91`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `99.97` - `100.78`
  * Optimal Trade Entry (OTE 0.705): `100.58`
  * Structural Invalidation Anchor (0.786): `101.18`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.89` | `100.91` | `100.75` | `100.79` | `23,639` | 2,382,856.32 USD | -522,161.22 USD | `-21.91%` | -66,799,235.20 USD | `+0.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `100.78` | `100.80` | `100.30` | `100.51` | `178,308` | 17,916,375.53 USD | -6,550,887.72 USD | `-36.56%` | -73,350,122.92 USD | `-3.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `100.51` | `100.51` | `100.45` | `100.47` | `3,769` | 378,636.34 USD | 56,760.92 USD | `+14.99%` | -73,293,362.00 USD | `+0.57` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `101.06` | `101.18` | `100.89` | `101.10` | `117,256` | 11,845,890.84 USD | -551,250.53 USD | `-4.65%` | -66,210,016.15 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `101.10` | `101.17` | `100.75` | `100.79` | `76,073` | 7,681,327.85 USD | -601,405.98 USD | `-7.83%` | -66,811,422.12 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `100.78` | `100.80` | `100.30` | `100.47` | `182,076` | 18,295,011.86 USD | -6,494,126.80 USD | `-35.50%` | -73,305,548.92 USD | `-1.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `102.66` | `103.16` | `101.75` | `101.86` | `1,100,013` | 112,591,915.90 USD | -12,028,545.03 USD | `-10.68%` | -51,660,705.06 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `101.87` | `101.93` | `100.71` | `101.06` | `773,410` | 78,387,335.50 USD | -11,810,112.06 USD | `-15.07%` | -63,470,817.13 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.06` | `101.18` | `100.30` | `100.47` | `375,426` | 37,824,239.95 USD | -7,644,773.90 USD | `-20.21%` | -71,115,591.03 USD | `-0.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.30` | `100.47` | `2,248,849` | 228,803,491.35 USD | -31,483,430.99 USD | `-13.76%` | -75,352,074.21 USD | `-1.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `102.37` | `102.50` | `99.16` | `99.64` | `3,450,297` | 345,810,531.49 USD | -35,022,306.76 USD | `-10.13%` | -43,673,756.58 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -38,017,362.01 USD | `+1.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.29` | `100.49` | `2,337,377` | 237,693,962.68 USD | -32,256,191.21 USD | `-13.57%` | -76,124,834.43 USD | `-1.27` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`100.38`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `100.33` | `1791.6100` | 179,752.23 USD | 6,408,903.08 USD | `7 orders` | `-0.19%` | `-` |
| `BID` | `100.34` | `765.6300` | 76,823.31 USD | 6,229,150.84 USD | `12 orders` | `-0.18%` | `-` |
| `BID` | `100.35` | `4384.3000` | 439,964.51 USD | 6,152,327.53 USD | `16 orders` | `-0.17%` | `-` |
| `BID` | `100.36` | `4649.2600` | 466,599.73 USD | 5,712,363.03 USD | `12 orders` | `-0.16%` | `-` |
| `BID` | `100.37` | `3918.4800` | 393,297.84 USD | 5,245,763.29 USD | `13 orders` | `-0.15%` | `-` |
| `BID` | `100.38` | `2737.5600` | 274,796.27 USD | 4,852,465.45 USD | `18 orders` | `-0.14%` | `-` |
| `BID` | `100.39` | `6747.1600` | 677,347.39 USD | 4,577,669.18 USD | `14 orders` | `-0.13%` | `-` |
| `BID` | `100.40` | `1667.4300` | 167,409.97 USD | 3,900,321.79 USD | `17 orders` | `-0.12%` | `-` |
| `BID` | `100.41` | `5014.1600` | 503,471.81 USD | 3,732,911.82 USD | `16 orders` | `-0.11%` | `-` |
| `BID` | `100.42` | `1581.5500` | 158,819.25 USD | 3,229,440.01 USD | `19 orders` | `-0.10%` | `-` |
| `BID` | `100.43` | `3833.3600` | 384,984.34 USD | 3,070,620.76 USD | `23 orders` | `-0.09%` | `-` |
| `BID` | `100.44` | `3410.6100` | 342,561.67 USD | 2,685,636.42 USD | `23 orders` | `-0.08%` | `-` |
| `BID` | `100.45` | `3538.9800` | 355,490.54 USD | 2,343,074.75 USD | `21 orders` | `-0.07%` | `-` |
| `BID` | `100.46` | `6716.8000` | 674,769.73 USD | 1,987,584.21 USD | `33 orders` | `-0.06%` | `-` |
| `BID` | `100.47` | `4529.7200` | 455,100.97 USD | 1,312,814.48 USD | `31 orders` | `-0.05%` | `-` |
| `BID` | `100.48` | `2389.3900` | 240,085.91 USD | 857,713.51 USD | `21 orders` | `-0.04%` | `-` |
| `BID` | `100.49` | `3351.0100` | 336,742.99 USD | 617,627.60 USD | `18 orders` | `-0.03%` | `-` |
| `BID` | `100.50` | `1320.6500` | 132,725.33 USD | 280,884.61 USD | `20 orders` | `-0.02%` | `-` |
| `BID` | `100.51` | `820.2200` | 82,440.31 USD | 148,159.28 USD | `11 orders` | `-0.01%` | `-` |
| `BID` | `100.52` | `653.7900` | 65,718.97 USD | 65,718.97 USD | `10 orders` | `-0.00%` | `-` |
| `ASK` | `100.53` | `516.0900` | 51,882.53 USD | 51,882.53 USD | `21 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `100.53` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 100.53` | `0.00%` | `-` |
| `ASK` | `100.54` | `993.3400` | 99,870.40 USD | 151,752.93 USD | `20 orders` | `+0.01%` | `-` |
| `ASK` | `100.55` | `4028.5200` | 405,067.69 USD | 556,820.62 USD | `25 orders` | `+0.02%` | `-` |
| `ASK` | `100.56` | `1656.3600` | 166,563.56 USD | 723,384.18 USD | `27 orders` | `+0.03%` | `-` |
| `ASK` | `100.57` | `4612.2100` | 463,849.96 USD | 1,187,234.14 USD | `24 orders` | `+0.04%` | `-` |
| `ASK` | `100.58` | `2155.7400` | 216,824.33 USD | 1,404,058.47 USD | `29 orders` | `+0.05%` | `-` |
| `ASK` | `100.59` | `2823.1900` | 283,984.68 USD | 1,688,043.15 USD | `22 orders` | `+0.06%` | `-` |
| `ASK` | `100.60` | `1892.6500` | 190,400.59 USD | 1,878,443.74 USD | `19 orders` | `+0.07%` | `-` |
| `ASK` | `100.61` | `2767.1500` | 278,402.96 USD | 2,156,846.70 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `100.62` | `5805.8200` | 584,181.61 USD | 2,741,028.31 USD | `24 orders` | `+0.09%` | `-` |
| `ASK` | `100.63` | `3313.3700` | 333,424.42 USD | 3,074,452.73 USD | `9 orders` | `+0.10%` | `-` |
| `ASK` | `100.64` | `2328.3300` | 234,323.13 USD | 3,308,775.86 USD | `12 orders` | `+0.11%` | `-` |
| `ASK` | `100.65` | `3359.8100` | 338,164.88 USD | 3,646,940.74 USD | `13 orders` | `+0.12%` | `-` |
| `ASK` | `100.66` | `869.7900` | 87,553.06 USD | 3,734,493.80 USD | `15 orders` | `+0.13%` | `-` |
| `ASK` | `100.67` | `2209.8500` | 222,465.60 USD | 3,956,959.40 USD | `9 orders` | `+0.14%` | `-` |
| `ASK` | `100.68` | `1597.7100` | 160,857.44 USD | 4,117,816.84 USD | `13 orders` | `+0.15%` | `-` |
| `ASK` | `100.69` | `3642.0500` | 366,718.01 USD | 4,484,534.86 USD | `8 orders` | `+0.16%` | `-` |
| `ASK` | `100.70` | `5223.1600` | 525,972.21 USD | 5,010,507.07 USD | `9 orders` | `+0.17%` | `-` |
| `ASK` | `100.71` | `2273.7500` | 228,989.36 USD | 5,239,496.43 USD | `8 orders` | `+0.18%` | `-` |
| `ASK` | `100.72` | `803.9500` | 80,973.84 USD | 5,320,470.28 USD | `12 orders` | `+0.19%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `14` | `0x5b5d...c060` | `SHORT` | 72,520,378.55 USD | `721,165.26` | `94.33` | `100.58` | `318.88` | -4,489,488.13 USD | `-6.19%` | `7X Cross` |
| `21` | `0x9c6a...a4ed` | `LONG` | 55,250,807.58 USD | `550,087.69` | `80.86` | `100.58` | `68.17` | 10,771,821.19 USD | `+19.50%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 26,051,017.32 USD | `259,300.02` | `91.42` | `100.58` | `615.35` | -2,345,884.30 USD | `-9.00%` | `5X Cross` |
| `78` | `0x3dc9...54b0` | `SHORT` | 22,096,819.08 USD | `220,000.19` | `105.90` | `100.58` | `165.99` | 1,202,288.19 USD | `+5.44%` | `20X Cross` |
| `101` | `0x9c89...600e` | `LONG` | 19,036,302.07 USD | `189,472.50` | `115.21` | `100.58` | `34.73` | -2,792,713.19 USD | `-14.67%` | `20X Cross` |
| `113` | `0x4a20...3c26` | `LONG` | 18,100,800.00 USD | `180,000.00` | `106.43` | `100.58` | `65.80` | -1,057,478.71 USD | `-5.84%` | `20X Cross` |
| `137` | `0xecb6...2b00` | `SHORT` | 15,006,088.12 USD | `149,225.22` | `102.73` | `100.58` | `283.23` | 324,247.20 USD | `+2.16%` | `20X Cross` |
| `228` | `0xc63a...a3cd` | `LONG` | 10,056,000.00 USD | `100,000.00` | `112.22` | `100.58` | `0.000000` | -1,166,108.97 USD | `-11.60%` | `20X Cross` |
| `230` | `0x7a5a...0394` | `SHORT` | 10,016,586.95 USD | `99,598.16` | `100.92` | `100.58` | `126.69` | 34,762.77 USD | `+0.35%` | `10X Cross` |
| `242` | `0x13da...08be` | `LONG` | 9,624,727.32 USD | `95,711.29` | `100.55` | `100.58` | `98.09` | 986.65 USD | `+0.01%` | `20X Isolated` |
| `266` | `0xb581...6f4f` | `LONG` | 9,042,300.00 USD | `90,000.00` | `114.59` | `100.58` | `0.000000` | -1,270,992.29 USD | `-14.06%` | `3X Cross` |
| `287` | `0x645b...87b8` | `SHORT` | 8,397,315.33 USD | `83,605.29` | `103.91` | `100.58` | `332.83` | 289,813.84 USD | `+3.45%` | `20X Cross` |
| `298` | `0xdb3a...cf3b` | `LONG` | 8,223,648.34 USD | `81,851.78` | `106.04` | `100.58` | `46.36` | -456,098.52 USD | `-5.55%` | `4X Cross` |
| `316` | `0xe927...98ef` | `LONG` | 7,835,100.00 USD | `78,000.00` | `96.34` | `100.58` | `38.44` | 320,958.52 USD | `+4.10%` | `3X Cross` |
| `324` | `0xca49...53c8` | `SHORT` | 7,435,753.33 USD | `73,943.45` | `110.70` | `100.58` | `275.76` | 749,868.93 USD | `+10.08%` | `20X Cross` |
| `328` | `0x8ae4...3d60` | `LONG` | 7,248,096.86 USD | `72,180.05` | `111.72` | `100.58` | `2.77` | -816,063.37 USD | `-11.26%` | `10X Cross` |
| `333` | `0xa0b7...6165` | `SHORT` | 7,162,698.42 USD | `71,044.42` | `107.87` | `100.58` | `190.90` | 500,768.78 USD | `+6.99%` | `2X Cross` |
| `349` | `0xf517...c032` | `SHORT` | 6,817,164.55 USD | `67,778.53` | `84.64` | `100.58` | `233.40` | -1,080,133.38 USD | `-15.84%` | `20X Cross` |
| `476` | `0x7e23...5a5a` | `LONG` | 4,883,652.15 USD | `48,564.56` | `105.17` | `100.58` | `78.11` | -223,917.01 USD | `-4.59%` | `5X Isolated` |
| `575` | `0x2e2b...2fab` | `LONG` | 4,018,000.00 USD | `40,000.00` | `119.55` | `100.58` | `53.76` | -764,035.64 USD | `-19.02%` | `10X Cross` |
| `578` | `0x7fda...17d1` | `SHORT` | 3,998,609.52 USD | `39,763.42` | `103.76` | `100.58` | `996.98` | 127,228.29 USD | `+3.18%` | `20X Cross` |
| `597` | `0xf899...88db` | `SHORT` | 3,875,990.82 USD | `38,586.27` | `87.86` | `100.58` | `117.19` | -485,615.63 USD | `-12.53%` | `20X Cross` |
| `614` | `0x9946...0852` | `SHORT` | 3,800,395.18 USD | `37,784.80` | `112.11` | `100.58` | `129.97` | 435,832.13 USD | `+11.47%` | `20X Cross` |
| `643` | `0x27b8...12fc` | `LONG` | 3,623,729.01 USD | `36,085.73` | `110.86` | `100.58` | `15.04` | -376,616.25 USD | `-10.39%` | `10X Cross` |
| `644` | `0x9c16...4a6f` | `SHORT` | 3,597,951.32 USD | `35,779.15` | `90.45` | `100.58` | `128.57` | -361,846.29 USD | `-10.06%` | `20X Cross` |
| `650` | `0x3440...32c5` | `SHORT` | 3,573,518.89 USD | `35,529.12` | `95.02` | `100.58` | `168.59` | -197,497.46 USD | `-5.53%` | `20X Cross` |
| `726` | `0x96a7...79df` | `LONG` | 3,214,080.00 USD | `32,000.00` | `74.39` | `100.58` | `0.000000` | 833,674.15 USD | `+25.94%` | `20X Cross` |
| `741` | `0x023a...2355` | `SHORT` | 3,159,830.51 USD | `31,422.34` | `101.48` | `100.58` | `361.58` | 28,807.67 USD | `+0.91%` | `20X Cross` |
| `771` | `0xbe19...8bd1` | `SHORT` | 3,062,526.46 USD | `30,451.69` | `97.62` | `100.58` | `732.73` | -89,979.83 USD | `-2.94%` | `3X Cross` |
| `774` | `0x482b...cae4` | `SHORT` | 3,048,022.87 USD | `30,310.49` | `88.03` | `100.58` | `156.69` | -379,774.59 USD | `-12.46%` | `20X Cross` |
| `787` | `0x610b...b613` | `LONG` | 2,976,453.02 USD | `29,634.14` | `101.23` | `100.58` | `70.38` | -23,546.33 USD | `-0.79%` | `3X Isolated` |
| `798` | `0x45d2...4029` | `SHORT` | 2,938,363.20 USD | `29,220.00` | `93.28` | `100.58` | `1360.91` | -212,587.22 USD | `-7.23%` | `20X Cross` |
| `806` | `0xa61c...66b9` | `LONG` | 2,905,555.04 USD | `28,888.00` | `104.39` | `100.58` | `0.000000` | -110,009.08 USD | `-3.79%` | `5X Cross` |
| `834` | `0xfc66...ca06` | `SHORT` | 2,798,649.16 USD | `27,830.64` | `102.27` | `100.58` | `1363.17` | 47,722.52 USD | `+1.71%` | `20X Cross` |
| `848` | `0x458d...ab3b` | `LONG` | 2,750,552.41 USD | `27,385.03` | `117.17` | `100.58` | `81.07` | -458,110.10 USD | `-16.66%` | `3X Isolated` |
| `880` | `0xfc27...9d9d` | `SHORT` | 2,593,800.39 USD | `25,793.56` | `102.76` | `100.58` | `665.26` | 56,687.40 USD | `+2.19%` | `20X Cross` |
| `909` | `0x051c...693c` | `LONG` | 2,525,031.47 USD | `25,139.70` | `89.76` | `100.58` | `24.68` | 268,470.14 USD | `+10.63%` | `20X Cross` |
| `945` | `0x638f...f5f0` | `LONG` | 2,413,440.00 USD | `24,000.00` | `136.71` | `100.58` | `42.81` | -867,528.54 USD | `-35.95%` | `20X Cross` |
| `1003` | `0x7178...0854` | `LONG` | 2,263,993.00 USD | `22,545.24` | `110.94` | `100.58` | `31.58` | -237,151.47 USD | `-10.47%` | `10X Cross` |
| `1025` | `0x739c...cfb2` | `LONG` | 2,209,680.00 USD | `22,000.00` | `91.95` | `100.58` | `72.48` | 186,772.69 USD | `+8.45%` | `20X Cross` |
| `1034` | `0x69cc...14fd` | `SHORT` | 2,182,526.89 USD | `21,701.57` | `99.01` | `100.58` | `456.70` | -33,874.15 USD | `-1.55%` | `20X Cross` |
| `1051` | `0xb90d...870c` | `SHORT` | 2,121,866.75 USD | `21,120.10` | `102.00` | `100.58` | `112.16` | 32,458.02 USD | `+1.53%` | `20X Cross` |
| `1097` | `0x7737...bf66` | `SHORT` | 2,047,578.83 USD | `20,384.06` | `102.94` | `100.58` | `983.20` | 50,763.06 USD | `+2.48%` | `10X Cross` |
| `1117` | `0x251f...6e5d` | `LONG` | 2,011,600.00 USD | `20,000.00` | `101.15` | `100.58` | `47.80` | -11,497.77 USD | `-0.57%` | `20X Cross` |
| `1118` | `0xbfc7...80b4` | `SHORT` | 2,011,544.00 USD | `20,000.00` | `85.98` | `100.58` | `326.99` | -292,009.50 USD | `-14.52%` | `20X Cross` |
| `1119` | `0xea00...a918` | `LONG` | 2,011,078.98 USD | `20,022.69` | `66.09` | `100.58` | `0.000000` | 687,770.38 USD | `+34.20%` | `20X Cross` |
| `1122` | `0x3fc5...c0c1` | `SHORT` | 2,009,200.00 USD | `20,000.00` | `98.28` | `100.58` | `205.43` | -43,640.16 USD | `-2.17%` | `20X Cross` |
| `1123` | `0xdf60...d3c7` | `LONG` | 2,009,200.00 USD | `20,000.00` | `120.12` | `100.58` | `94.00` | -393,208.53 USD | `-19.57%` | `7X Isolated` |
| `1126` | `0x5986...89d9` | `LONG` | 2,008,400.00 USD | `20,000.00` | `101.84` | `100.58` | `47.11` | -28,397.53 USD | `-1.41%` | `20X Cross` |
| `1142` | `0xb322...d51f` | `LONG` | 1,988,951.40 USD | `19,774.82` | `102.98` | `100.58` | `56.12` | -47,520.00 USD | `-2.39%` | `20X Cross` |
| `1148` | `0x34e6...8d74` | `LONG` | 1,979,832.32 USD | `19,688.07` | `101.19` | `100.58` | `53.20` | -12,331.48 USD | `-0.62%` | `20X Cross` |
| `1167` | `0x936c...bb0f` | `SHORT` | 1,954,861.56 USD | `19,437.82` | `105.65` | `100.58` | `636.87` | 98,652.82 USD | `+5.05%` | `20X Cross` |
| `1169` | `0x7160...d47c` | `LONG` | 1,954,681.78 USD | `19,434.10` | `105.03` | `100.58` | `80.42` | -86,539.51 USD | `-4.43%` | `20X Cross` |
| `1195` | `0xe097...d0fe` | `LONG` | 1,910,212.62 USD | `18,995.75` | `109.71` | `100.58` | `0.000000` | -173,784.27 USD | `-9.10%` | `20X Cross` |
| `1285` | `0xe98b...8cd5` | `SHORT` | 1,770,219.30 USD | `17,622.89` | `187.95` | `100.58` | `260.35` | 1,542,001.42 USD | `+87.11%` | `20X Cross` |
| `1296` | `0xdf95...7d72` | `SHORT` | 1,752,015.10 USD | `17,443.40` | `104.70` | `100.58` | `2232.62` | 74,248.56 USD | `+4.24%` | `20X Cross` |
| `1326` | `0xee2b...d67e` | `LONG` | 1,706,157.65 USD | `16,963.19` | `119.86` | `100.58` | `21.26` | -327,113.99 USD | `-19.17%` | `4X Cross` |
| `1330` | `0x123d...3bff` | `LONG` | 1,701,317.32 USD | `16,918.43` | `89.53` | `100.58` | `0.000000` | 186,530.84 USD | `+10.96%` | `10X Cross` |
| `1357` | `0x7277...0b98` | `SHORT` | 1,669,774.77 USD | `16,603.11` | `101.18` | `100.58` | `179.76` | 10,153.43 USD | `+0.61%` | `20X Cross` |
| `1438` | `0x73d7...8be1` | `LONG` | 1,575,669.61 USD | `15,668.95` | `106.60` | `100.58` | `71.26` | -94,671.35 USD | `-6.01%` | `20X Cross` |
| `1450` | `0xc74a...ab93` | `LONG` | 1,560,207.46 USD | `15,536.82` | `64.06` | `100.58` | `54.88` | 564,978.63 USD | `+36.21%` | `5X Isolated` |
| `1499` | `0xc7d1...51af` | `SHORT` | 1,505,550.00 USD | `15,000.00` | `105.79` | `100.58` | `138.76` | 81,325.00 USD | `+5.40%` | `20X Cross` |
| `1527` | `0xffb2...5ed6` | `LONG` | 1,456,496.70 USD | `14,504.05` | `117.89` | `100.58` | `89.10` | -253,408.01 USD | `-17.40%` | `20X Cross` |
| `1560` | `0x0d6a...ca57` | `LONG` | 1,427,200.06 USD | `14,206.65` | `110.41` | `100.58` | `91.59` | -141,390.30 USD | `-9.91%` | `5X Isolated` |
| `1835` | `0x2482...0e55` | `LONG` | 1,141,701.57 USD | `11,363.98` | `122.03` | `100.58` | `94.24` | -245,000.35 USD | `-21.46%` | `20X Isolated` |
| `1854` | `0xe105...6a47` | `LONG` | 1,127,003.93 USD | `11,205.05` | `107.11` | `100.58` | `92.29` | -73,153.12 USD | `-6.49%` | `20X Cross` |
| `1863` | `0x45db...86eb` | `LONG` | 1,116,216.00 USD | `11,100.00` | `110.69` | `100.58` | `67.96` | -112,465.90 USD | `-10.08%` | `5X Cross` |
| `1896` | `0x1d04...7c43` | `LONG` | 1,085,716.94 USD | `10,811.76` | `111.55` | `100.58` | `18.49` | -120,344.55 USD | `-11.08%` | `6X Cross` |
| `2013` | `0x0daf...47e0` | `SHORT` | 1,004,169.00 USD | `10,000.00` | `99.07` | `100.58` | `250.97` | -13,456.78 USD | `-1.34%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `130.74` | 1,361.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.36K USD at 130.7400 USD [API] | `2026-01-21 15:16:43` |
| `ANNOUNCEMENT` | `INFO` | `122.75` | 4,485.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.49K USD at 122.7500 USD [API] | `2025-12-23 13:36:37` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 3,751.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 3.75K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 820.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.82K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `126.81` | 3,182.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.18K USD at 126.8100 USD [API] | `2025-12-17 15:52:14` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,808.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.81K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,998.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.00K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,510.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.51K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `129.25` | 4,809.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.81K USD at 129.2500 USD [API] | `2025-12-14 23:27:00` |
| `ANNOUNCEMENT` | `INFO` | `134.26` | 5,544.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.54K USD at 134.2600 USD [API] | `2025-12-11 18:35:47` |
| `ANNOUNCEMENT` | `INFO` | `128.92` | 6,032.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.03K USD at 128.9200 USD [API] | `2025-12-07 14:24:53` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 6,367.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.37K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 19.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 12.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 202.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 1,588.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.59K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,040.30 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.04K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,710.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.71K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 1,543.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.54K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 2,490.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.49K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.65` (Vol: 2,900,000.00 USD, Dist: `+2.84%`) | Long MP=`98.78` (Vol: 4,200,000.00 USD, Dist: `--1.99%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+3.28%`) | Long MP=`98.78` (Vol: 4,300,000.00 USD, Dist: `--1.99%`)
  * 3D Horizon: Short MP=`104.03` (Vol: 4,200,000.00 USD, Dist: `+3.23%`) | Long MP=`99.07` (Vol: 5,900,000.00 USD, Dist: `--1.69%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+3.24%`) | Long MP=`98.63` (Vol: 8,800,000.00 USD, Dist: `--2.13%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `20.50` | 500,800.00 USD | 140,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.50` | 9,590.00 USD | 140,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.50` | 640,090.00 USD | 140,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.50` | 52,490.00 USD | 139,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.50` | 29,610.00 USD | 139,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.50` | 14,650.00 USD | 139,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 159,830.00 USD | 139,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 5,310.00 USD | 139,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 25,020.00 USD | 139,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 112,130.00 USD | 139,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 811,380.00 USD | 139,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 65,450.00 USD | 138,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 54,260.00 USD | 138,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 324,140.00 USD | 138,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 6,550,000.00 USD | 138,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 28,890.00 USD | 131,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 13,230.00 USD | 131,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 348,620.00 USD | 131,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 3,020,000.00 USD | 131,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 74,740.00 USD | 128,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 77,130.00 USD | 128,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 43,170.00 USD | 127,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 1,090,000.00 USD | 127,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 46,760.00 USD | 126,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 305,790.00 USD | 126,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 1,880,000.00 USD | 126,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 6,000.00 USD | 124,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 3,920,000.00 USD | 124,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 64,870.00 USD | 120,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 80,310.00 USD | 120,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 163,360.00 USD | 120,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 800,950.00 USD | 120,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 101,460.00 USD | 119,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 3,420,000.00 USD | 119,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 1,120,000.00 USD | 116,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 182,390.00 USD | 114,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,590,000.00 USD | 114,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 112,290.00 USD | 113,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 184,220.00 USD | 113,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 134,170.00 USD | 112,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 177,470.00 USD | 112,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 228,150.00 USD | 112,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 217,380.00 USD | 112,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 376,000.00 USD | 112,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 75,240.00 USD | 111,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 11,940,000.00 USD | 111,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 99,120.00 USD | 99,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 1,050,000.00 USD | 99,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 37,930,000.00 USD | 98,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 172,850.00 USD | 60,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 3,590,000.00 USD | 60,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 497,880.00 USD | 56,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 1,920,000.00 USD | 56,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 590,970.00 USD | 54,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 644,710.00 USD | 53,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 871,540.00 USD | 53,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 441,110.00 USD | 52,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 757,050.00 USD | 51,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 5,380,000.00 USD | 51,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 430,910.00 USD | 45,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 2,020,000.00 USD | 45,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.50` | 2,600,000.00 USD | 43,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,420,000.00 USD | 40,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 721,890.00 USD | 39,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 610,240.00 USD | 38,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 956,570.00 USD | 37,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 882,970.00 USD | 37,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,420,000.00 USD | 36,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 3,930,000.00 USD | 34,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,870,000.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.60` | 369,220,000.00 USD | 369,220,000.00 USD | 700,630.00 USD | 276,340.00 USD | 577,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.80` | 367,670,000.00 USD | 367,670,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 366,680,000.00 USD | 366,680,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 364,960,000.00 USD | 364,960,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.30` | 175,930,000.00 USD | 175,930,000.00 USD | 362,900.00 USD | 536,640.00 USD | 506,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 362,960,000.00 USD | 362,960,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.50` | 174,520,000.00 USD | 174,520,000.00 USD | 486,210.00 USD | 399,670.00 USD | 359,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.50` | 426,080.00 USD | 28,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.60` | 361,560,000.00 USD | 361,560,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.70` | 173,270,000.00 USD | 173,270,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 358,450,000.00 USD | 358,450,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.90` | 172,770,000.00 USD | 172,770,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 355,470,000.00 USD | 355,470,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.10` | 172,670,000.00 USD | 172,670,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 353,410,000.00 USD | 353,410,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.30` | 172,480,000.00 USD | 172,480,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 351,080,000.00 USD | 351,080,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.50` | 172,330,000.00 USD | 172,330,000.00 USD | 21,670.00 USD | 87,530.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.50` | 3,170,000.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.60` | 347,750,000.00 USD | 347,750,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.70` | 172,220,000.00 USD | 172,220,000.00 USD | 107,440.00 USD | 112,260.00 USD | 56,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 346,130,000.00 USD | 346,130,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.90` | 171,950,000.00 USD | 171,950,000.00 USD | 326,750.00 USD | 140,660.00 USD | 177,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 343,930,000.00 USD | 343,930,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.10` | 171,300,000.00 USD | 171,300,000.00 USD | 218,720.00 USD | 124,560.00 USD | 64,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 342,190,000.00 USD | 342,190,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.30` | 170,890,000.00 USD | 170,890,000.00 USD | 219,340.00 USD | 97,250.00 USD | 738,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 341,330,000.00 USD | 341,330,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.50` | 169,840,000.00 USD | 169,840,000.00 USD | 37,670.00 USD | 53,380.00 USD | 168,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.50` | 2,310,000.00 USD | 25,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.60` | 339,420,000.00 USD | 339,420,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.70` | 169,580,000.00 USD | 169,580,000.00 USD | 0.00 USD | 86,970.00 USD | 168,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 338,340,000.00 USD | 338,340,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.90` | 169,330,000.00 USD | 169,330,000.00 USD | 100,830.00 USD | 0.00 USD | 60,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.00` | 338,110,000.00 USD | 338,110,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.10` | 169,160,000.00 USD | 169,160,000.00 USD | 0.00 USD | 2,580.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.20` | 337,720,000.00 USD | 337,720,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.30` | 169,050,000.00 USD | 169,050,000.00 USD | 0.00 USD | 103,020.00 USD | 99,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.40` | 337,610,000.00 USD | 337,610,000.00 USD | 15,260.00 USD | 81,430.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.50` | 3,170,000.00 USD | 23,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 337,520,000.00 USD | 337,520,000.00 USD | 238,200.00 USD | 343,740.00 USD | 114,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.80` | 336,820,000.00 USD | 336,820,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.00` | 336,140,000.00 USD | 336,140,000.00 USD | 78,790.00 USD | 153,680.00 USD | 134,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.20` | 335,780,000.00 USD | 335,780,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.40` | 335,120,000.00 USD | 335,120,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,910,000.00 USD | 19,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.60` | 334,820,000.00 USD | 334,820,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 334,740,000.00 USD | 334,740,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 334,720,000.00 USD | 334,720,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.10` | 168,840,000.00 USD | 168,840,000.00 USD | 13,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 333,750,000.00 USD | 333,750,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.30` | 168,830,000.00 USD | 168,830,000.00 USD | 18,710.00 USD | 89,760.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 333,370,000.00 USD | 333,370,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.50` | 168,710,000.00 USD | 168,710,000.00 USD | 679,320.00 USD | 458,400.00 USD | 465,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.50` | 1,620,000.00 USD | 16,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.60` | 331,850,000.00 USD | 331,850,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.70` | 167,110,000.00 USD | 167,110,000.00 USD | 1,490,000.00 USD | 1,130,000.00 USD | 649,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 327,800,000.00 USD | 327,800,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.90` | 163,840,000.00 USD | 163,840,000.00 USD | 1,150,000.00 USD | 885,010.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 323,560,000.00 USD | 323,560,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.10` | 160,570,000.00 USD | 160,570,000.00 USD | 1,430,000.00 USD | 1,420,000.00 USD | 942,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 317,130,000.00 USD | 317,130,000.00 USD | 2,940,000.00 USD | 1,970,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 156,780,000.00 USD | 156,780,000.00 USD | 875,730.00 USD | 1,140,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 310,230,000.00 USD | 310,230,000.00 USD | 2,950,000.00 USD | 643,110.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.50` | 153,580,000.00 USD | 153,580,000.00 USD | 1,220,000.00 USD | 924,880.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.50` | 1,360,000.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `96.60` | 304,260,000.00 USD | 304,260,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.70` | 150,430,000.00 USD | 150,430,000.00 USD | 681,660.00 USD | 858,670.00 USD | 909,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 296,160,000.00 USD | 296,160,000.00 USD | 3,000,000.00 USD | 2,770,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.90` | 147,980,000.00 USD | 147,980,000.00 USD | 383,880.00 USD | 290,640.00 USD | 167,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.00` | 287,430,000.00 USD | 287,430,000.00 USD | 5,510,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.10` | 147,140,000.00 USD | 147,140,000.00 USD | 271,410.00 USD | 113,790.00 USD | 379,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.20` | 277,340,000.00 USD | 277,340,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.30` | 146,380,000.00 USD | 146,380,000.00 USD | 197,550.00 USD | 378,560.00 USD | 121,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.40` | 263,530,000.00 USD | 263,530,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.50` | 145,680,000.00 USD | 145,680,000.00 USD | 1,460,000.00 USD | 1,060,000.00 USD | 960,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.50` | 2,470,000.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `97.60` | 253,110,000.00 USD | 253,110,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.70` | 142,190,000.00 USD | 142,190,000.00 USD | 3,210,000.00 USD | 2,660,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.80` | 237,760,000.00 USD | 237,760,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.90` | 134,890,000.00 USD | 134,890,000.00 USD | 3,490,000.00 USD | 2,490,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.00` | 224,300,000.00 USD | 224,300,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.10` | 125,940,000.00 USD | 125,940,000.00 USD | 3,460,000.00 USD | 3,450,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.20` | 199,630,000.00 USD | 199,630,000.00 USD | 7,790,000.00 USD | 6,660,000.00 USD | 5,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.30` | 116,430,000.00 USD | 116,430,000.00 USD | 2,900,000.00 USD | 2,950,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.40` | 179,500,000.00 USD | 179,500,000.00 USD | 9,460,000.00 USD | 2,950,000.00 USD | 9,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.50` | 107,890,000.00 USD | 107,890,000.00 USD | 5,870,000.00 USD | 3,960,000.00 USD | 5,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.50` | 10,960,000.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `98.60` | 157,470,000.00 USD | 157,470,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.70` | 92,440,000.00 USD | 92,440,000.00 USD | 7,440,000.00 USD | 6,270,000.00 USD | 4,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.80` | 121,980,000.00 USD | 121,980,000.00 USD | 12,600,000.00 USD | 9,880,000.00 USD | 13,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.90` | 73,800,000.00 USD | 73,800,000.00 USD | 5,040,000.00 USD | 4,270,000.00 USD | 5,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.00` | 86,420,000.00 USD | 86,420,000.00 USD | 14,280,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.10` | 58,750,000.00 USD | 58,750,000.00 USD | 6,070,000.00 USD | 5,760,000.00 USD | 4,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.20` | 44,750,000.00 USD | 44,750,000.00 USD | 12,590,000.00 USD | 6,970,000.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.30` | 42,190,000.00 USD | 42,190,000.00 USD | 3,310,000.00 USD | 4,420,000.00 USD | 4,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.40` | 19,270,000.00 USD | 19,270,000.00 USD | 2,300,000.00 USD | 599,290.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.50` | 29,490,000.00 USD | 29,490,000.00 USD | 4,600,000.00 USD | 3,860,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.50` | 481,350.00 USD | 519,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `99.60` | 9,690,000.00 USD | 9,690,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.70` | 17,160,000.00 USD | 17,160,000.00 USD | 2,480,000.00 USD | 3,410,000.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.80` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.90` | 8,040,000.00 USD | 8,040,000.00 USD | 1,650,000.00 USD | 1,300,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.00` | 2,450,000.00 USD | 2,450,000.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.10` | 3,990,000.00 USD | 3,990,000.00 USD | 1,290,000.00 USD | 914,930.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.20` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.30` | 344,600.00 USD | 344,600.00 USD | 163,250.00 USD | 176,110.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.40` | 1,320,000.00 USD | 1,320,000.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.40` | 2,640,000.00 USD | 2,640,000.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.50` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `100.50` | 37,930.00 USD | 37,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.60` | 4,410,000.00 USD | 4,410,000.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.70` | 4,470,000.00 USD | 4,470,000.00 USD | 274,280.00 USD | 970,010.00 USD | 476,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.80` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 981,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.90` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 953,600.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 4,560,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.10` | 15,130,000.00 USD | 15,130,000.00 USD | 6,610,000.00 USD | 3,090,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.20` | 21,550,000.00 USD | 21,550,000.00 USD | 2,190,000.00 USD | 3,220,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.30` | 24,440,000.00 USD | 24,440,000.00 USD | 2,660,000.00 USD | 3,940,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 32,050,000.00 USD | 32,050,000.00 USD | 3,020,000.00 USD | 0.00 USD | 7,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.50` | 37,310,000.00 USD | 37,310,000.00 USD | 1,360,000.00 USD | 3,350,000.00 USD | 8,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.50` | 96,850.00 USD | 96,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.60` | 41,900,000.00 USD | 41,900,000.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.70` | 50,630,000.00 USD | 50,630,000.00 USD | 4,420,000.00 USD | 0.00 USD | 8,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 51,250,000.00 USD | 51,250,000.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.90` | 55,160,000.00 USD | 55,160,000.00 USD | 1,320,000.00 USD | 142,780.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 53,920,000.00 USD | 53,920,000.00 USD | 843,730.00 USD | 0.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.10` | 56,780,000.00 USD | 56,780,000.00 USD | 407,760.00 USD | 439,590.00 USD | 768,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 57,190,000.00 USD | 57,190,000.00 USD | 369,280.00 USD | 578,040.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.30` | 61,090,000.00 USD | 61,090,000.00 USD | 799,010.00 USD | 1,170,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 60,220,000.00 USD | 60,220,000.00 USD | 1,150,000.00 USD | 299,640.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.50` | 62,090,000.00 USD | 62,090,000.00 USD | 699,160.00 USD | 292,190.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.50` | 11,120.00 USD | 107,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.60` | 62,640,000.00 USD | 62,640,000.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.70` | 63,550,000.00 USD | 63,550,000.00 USD | 931,170.00 USD | 524,710.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 70,520,000.00 USD | 70,520,000.00 USD | 7,600,000.00 USD | 0.00 USD | 277,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.90` | 67,490,000.00 USD | 67,490,000.00 USD | 1,380,000.00 USD | 1,770,000.00 USD | 792,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 85,040,000.00 USD | 85,040,000.00 USD | 11,690,000.00 USD | 0.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.10` | 73,660,000.00 USD | 73,660,000.00 USD | 2,780,000.00 USD | 1,800,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 99,330,000.00 USD | 99,330,000.00 USD | 13,650,000.00 USD | 4,380.00 USD | 631,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.30` | 78,790,000.00 USD | 78,790,000.00 USD | 2,390,000.00 USD | 1,920,000.00 USD | 815,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 114,330,000.00 USD | 114,330,000.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.50` | 91,300,000.00 USD | 91,300,000.00 USD | 4,290,000.00 USD | 2,690,000.00 USD | 5,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.50` | 29,050.00 USD | 137,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.60` | 132,720,000.00 USD | 132,720,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.70` | 103,220,000.00 USD | 103,220,000.00 USD | 4,210,000.00 USD | 2,380,000.00 USD | 5,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 145,070,000.00 USD | 145,070,000.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.90` | 112,870,000.00 USD | 112,870,000.00 USD | 2,770,000.00 USD | 3,080,000.00 USD | 3,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 173,480,000.00 USD | 173,480,000.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.10` | 123,550,000.00 USD | 123,550,000.00 USD | 4,520,000.00 USD | 2,760,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 193,570,000.00 USD | 193,570,000.00 USD | 7,510,000.00 USD | 6,900,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.30` | 132,020,000.00 USD | 132,020,000.00 USD | 3,020,000.00 USD | 2,140,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 209,710,000.00 USD | 209,710,000.00 USD | 4,800,000.00 USD | 3,700,000.00 USD | 7,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.50` | 139,030,000.00 USD | 139,030,000.00 USD | 2,440,000.00 USD | 2,120,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.50` | 1,190,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.60` | 227,270,000.00 USD | 227,270,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.70` | 148,900,000.00 USD | 148,900,000.00 USD | 2,650,000.00 USD | 2,140,000.00 USD | 5,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 244,400,000.00 USD | 244,400,000.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.90` | 151,870,000.00 USD | 151,870,000.00 USD | 1,020,000.00 USD | 592,030.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 261,520,000.00 USD | 261,520,000.00 USD | 5,730,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.10` | 154,310,000.00 USD | 154,310,000.00 USD | 421,810.00 USD | 622,250.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 274,240,000.00 USD | 274,240,000.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.30` | 155,250,000.00 USD | 155,250,000.00 USD | 506,770.00 USD | 2,430.00 USD | 425,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 286,880,000.00 USD | 286,880,000.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.50` | 156,300,000.00 USD | 156,300,000.00 USD | 157,550.00 USD | 209,490.00 USD | 684,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.50` | 167,490.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.60` | 304,360,000.00 USD | 304,360,000.00 USD | 5,650,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.70` | 157,630,000.00 USD | 157,630,000.00 USD | 294,800.00 USD | 506,510.00 USD | 529,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 315,150,000.00 USD | 315,150,000.00 USD | 3,560,000.00 USD | 3,030,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.90` | 158,650,000.00 USD | 158,650,000.00 USD | 223,920.00 USD | 666,590.00 USD | 135,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 326,160,000.00 USD | 326,160,000.00 USD | 4,420,000.00 USD | 3,040,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.10` | 161,050,000.00 USD | 161,050,000.00 USD | 1,180,000.00 USD | 721,660.00 USD | 495,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 340,510,000.00 USD | 340,510,000.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.30` | 162,990,000.00 USD | 162,990,000.00 USD | 598,770.00 USD | 621,450.00 USD | 711,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 349,020,000.00 USD | 349,020,000.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.50` | 164,810,000.00 USD | 164,810,000.00 USD | 1,150,000.00 USD | 336,210.00 USD | 333,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.50` | 13,380.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.60` | 358,220,000.00 USD | 358,220,000.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.70` | 167,900,000.00 USD | 167,900,000.00 USD | 890,450.00 USD | 383,670.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 364,110,000.00 USD | 364,110,000.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.90` | 168,960,000.00 USD | 168,960,000.00 USD | 317,210.00 USD | 150,690.00 USD | 594,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 369,670,000.00 USD | 369,670,000.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.10` | 169,810,000.00 USD | 169,810,000.00 USD | 88,570.00 USD | 254,230.00 USD | 510,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 371,390,000.00 USD | 371,390,000.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.30` | 170,280,000.00 USD | 170,280,000.00 USD | 252,090.00 USD | 0.00 USD | 212,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 372,370,000.00 USD | 372,370,000.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.50` | 170,570,000.00 USD | 170,570,000.00 USD | 0.00 USD | 6,440.00 USD | 288,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.50` | 368,250.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.60` | 372,740,000.00 USD | 372,740,000.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.70` | 171,100,000.00 USD | 171,100,000.00 USD | 94,360.00 USD | 181,310.00 USD | 249,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 373,530,000.00 USD | 373,530,000.00 USD | 499,750.00 USD | 14,850.00 USD | 277,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.90` | 171,230,000.00 USD | 171,230,000.00 USD | 0.00 USD | 128,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.00` | 373,870,000.00 USD | 373,870,000.00 USD | 130,170.00 USD | 200,240.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.20` | 376,200,000.00 USD | 376,200,000.00 USD | 966,370.00 USD | 938,650.00 USD | 427,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.40` | 378,690,000.00 USD | 378,690,000.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.50` | 102,250.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 380,120,000.00 USD | 380,120,000.00 USD | 401,600.00 USD | 515,740.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.80` | 382,790,000.00 USD | 382,790,000.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.00` | 383,330,000.00 USD | 383,330,000.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.10` | 171,230,000.00 USD | 171,230,000.00 USD | 5,350.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.20` | 384,560,000.00 USD | 384,560,000.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.30` | 171,370,000.00 USD | 171,370,000.00 USD | 126,020.00 USD | 9,360.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.40` | 384,890,000.00 USD | 384,890,000.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.50` | 171,630,000.00 USD | 171,630,000.00 USD | 133,350.00 USD | 84,430.00 USD | 44,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.50` | 609,280.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.60` | 385,950,000.00 USD | 385,950,000.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.70` | 172,540,000.00 USD | 172,540,000.00 USD | 456,990.00 USD | 277,760.00 USD | 171,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.80` | 386,940,000.00 USD | 386,940,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.90` | 173,480,000.00 USD | 173,480,000.00 USD | 268,320.00 USD | 266,300.00 USD | 405,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.00` | 388,660,000.00 USD | 388,660,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.10` | 174,520,000.00 USD | 174,520,000.00 USD | 258,510.00 USD | 467,380.00 USD | 313,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.20` | 390,660,000.00 USD | 390,660,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.30` | 175,510,000.00 USD | 175,510,000.00 USD | 238,980.00 USD | 341,180.00 USD | 406,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.40` | 392,060,000.00 USD | 392,060,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.50` | 176,000,000.00 USD | 176,000,000.00 USD | 263,180.00 USD | 150,770.00 USD | 83,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.50` | 195,830.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.60` | 393,160,000.00 USD | 393,160,000.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.70` | 176,750,000.00 USD | 176,750,000.00 USD | 223,030.00 USD | 248,900.00 USD | 276,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.80` | 395,170,000.00 USD | 395,170,000.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.90` | 177,250,000.00 USD | 177,250,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.00` | 398,150,000.00 USD | 398,150,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.10` | 177,360,000.00 USD | 177,360,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.20` | 400,210,000.00 USD | 400,210,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.30` | 177,540,000.00 USD | 177,540,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.40` | 402,540,000.00 USD | 402,540,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.50` | 177,690,000.00 USD | 177,690,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.50` | 2,390,000.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.60` | 403,500,000.00 USD | 403,500,000.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.70` | 177,720,000.00 USD | 177,720,000.00 USD | 0.00 USD | 27,410.00 USD | 641.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.80` | 405,870,000.00 USD | 405,870,000.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.90` | 177,800,000.00 USD | 177,800,000.00 USD | 21,670.00 USD | 60,130.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.00` | 407,490,000.00 USD | 407,490,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.10` | 178,080,000.00 USD | 178,080,000.00 USD | 107,440.00 USD | 112,260.00 USD | 56,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.20` | 409,690,000.00 USD | 409,690,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.30` | 178,720,000.00 USD | 178,720,000.00 USD | 326,750.00 USD | 140,660.00 USD | 177,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.40` | 411,430,000.00 USD | 411,430,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.50` | 179,110,000.00 USD | 179,110,000.00 USD | 214,080.00 USD | 112,930.00 USD | 62,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.50` | 125,350.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `112.60` | 179,270,000.00 USD | 179,270,000.00 USD | 59,050.00 USD | 20,870.00 USD | 76,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.60` | 412,290,000.00 USD | 412,290,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.80` | 413,170,000.00 USD | 413,170,000.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.00` | 414,200,000.00 USD | 414,200,000.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.20` | 415,280,000.00 USD | 415,280,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.40` | 415,510,000.00 USD | 415,510,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.50` | 224,480.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.60` | 415,900,000.00 USD | 415,900,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.80` | 415,900,000.00 USD | 415,900,000.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.50` | 62,000.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.50` | 945,940.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.50` | 157,330.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.50` | 4,600,000.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.50` | 725,160.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.50` | 358,660.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.50` | 7,000.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 113,860.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 82,340.00 USD | 12,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 17,790.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 204,410.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 512,840.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 12,540,000.00 USD | 25,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 770,400.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 10,500,000.00 USD | 37,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 164,320.00 USD | 37,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 602,490.00 USD | 37,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 18,810.00 USD | 37,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 68,510.00 USD | 37,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 1,270,000.00 USD | 39,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 35,860.00 USD | 39,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 719,490.00 USD | 40,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 8,680.00 USD | 40,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 3,760.00 USD | 40,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,320,000.00 USD | 42,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 1,150,000.00 USD | 43,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 14,240.00 USD | 43,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 462,490.00 USD | 43,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 96,470.00 USD | 44,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 198,910.00 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 957,190.00 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 16,290.00 USD | 45,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 691,960.00 USD | 45,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 103,680.00 USD | 46,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,350,000.00 USD | 48,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.50` | 19,740.00 USD | 48,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 5,850.00 USD | 48,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 19,740.00 USD | 48,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 2,330,000.00 USD | 50,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.50` | 429,190.00 USD | 51,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 7,250.00 USD | 51,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 168,990.00 USD | 51,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.50` | 5,000,000.00 USD | 56,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 1,660,000.00 USD | 58,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 120,580.00 USD | 58,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.50` | 148,650.00 USD | 58,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 817,810.00 USD | 59,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.50` | 297,730.00 USD | 59,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 12,910.00 USD | 59,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 3,880.00 USD | 59,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 261,230.00 USD | 59,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.50` | 36,550,000.00 USD | 96,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 1,230,000.00 USD | 97,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 5,980,000.00 USD | 103,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 485,410.00 USD | 103,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 101,700.00 USD | 104,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 231.88 USD | 104,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 509.35 USD | 104,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 65,260.00 USD | 104,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 63,530.00 USD | 104,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 557,520.00 USD | 104,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 4,880.00 USD | 104,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 27,570.00 USD | 104,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 78,100.00 USD | 104,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.50` | 2,980,000.00 USD | 107,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 829.29 USD | 107,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 13,820.00 USD | 107,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 11,650.00 USD | 107,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 297,920.00 USD | 108,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 372,500.00 USD | 108,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 165,370.00 USD | 108,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 206,840.00 USD | 108,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 774,320.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 41,020.00 USD | 109,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 187,240.00 USD | 109,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 349,140.00 USD | 110,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 13,880,000.00 USD | 124,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 321.72 USD | 124,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 109,870.00 USD | 124,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 144,570.00 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 148,800.00 USD | 124,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 62,580.00 USD | 124,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 15,680.00 USD | 124,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.50` | 246,140.00 USD | 124,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 84,450.00 USD | 124,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 53,380.00 USD | 124,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 314,450.00 USD | 125,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 9,970.00 USD | 125,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `202.50` | 4,310,000.00 USD | 129,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `20.50` | 140,890,000.00 USD | 0.00 USD | 500,800.00 USD | `-79.72%` | `24,429.37` |
| `Live` | `Long` | `21.50` | 140,390,000.00 USD | 0.00 USD | 9,590.00 USD | `-78.73%` | `446.10` |
| `Live` | `Long` | `22.50` | 140,380,000.00 USD | 0.00 USD | 640,090.00 USD | `-77.75%` | `28,448.44` |
| `Live` | `Long` | `23.50` | 139,740,000.00 USD | 0.00 USD | 52,490.00 USD | `-76.76%` | `2,233.79` |
| `Live` | `Long` | `24.50` | 139,690,000.00 USD | 0.00 USD | 29,610.00 USD | `-75.77%` | `1,208.64` |
| `Live` | `Long` | `25.50` | 139,660,000.00 USD | 0.00 USD | 14,650.00 USD | `-74.78%` | `574.36` |
| `Live` | `Long` | `26.50` | 139,650,000.00 USD | 0.00 USD | 159,830.00 USD | `-73.79%` | `6,031.39` |
| `Live` | `Long` | `27.50` | 139,490,000.00 USD | 0.00 USD | 5,310.00 USD | `-72.80%` | `193.26` |
| `Live` | `Long` | `28.50` | 139,480,000.00 USD | 0.00 USD | 25,020.00 USD | `-71.81%` | `877.99` |
| `Live` | `Long` | `29.50` | 139,460,000.00 USD | 0.00 USD | 112,130.00 USD | `-70.82%` | `3,800.88` |
| `Live` | `Long` | `30.50` | 139,350,000.00 USD | 0.00 USD | 811,380.00 USD | `-69.83%` | `26,602.57` |
| `Live` | `Long` | `31.50` | 138,530,000.00 USD | 0.00 USD | 65,450.00 USD | `-68.84%` | `2,077.71` |
| `Live` | `Long` | `32.50` | 138,470,000.00 USD | 0.00 USD | 54,260.00 USD | `-67.85%` | `1,669.61` |
| `Live` | `Long` | `33.50` | 138,410,000.00 USD | 0.00 USD | 324,140.00 USD | `-66.87%` | `9,675.70` |
| `Live` | `Long` | `34.50` | 138,090,000.00 USD | 0.00 USD | 6,550,000.00 USD | `-65.88%` | `189,784.79` |
| `Live` | `Long` | `35.50` | 131,540,000.00 USD | 0.00 USD | 28,890.00 USD | `-64.89%` | `813.68` |
| `Live` | `Long` | `36.50` | 131,510,000.00 USD | 0.00 USD | 13,230.00 USD | `-63.90%` | `362.55` |
| `Live` | `Long` | `37.50` | 131,500,000.00 USD | 0.00 USD | 348,620.00 USD | `-62.91%` | `9,296.55` |
| `Live` | `Long` | `38.50` | 131,150,000.00 USD | 0.00 USD | 3,020,000.00 USD | `-61.92%` | `78,325.77` |
| `Live` | `Long` | `39.50` | 128,140,000.00 USD | 0.00 USD | 74,740.00 USD | `-60.93%` | `1,892.06` |
| `Live` | `Long` | `40.50` | 128,060,000.00 USD | 0.00 USD | 77,130.00 USD | `-59.94%` | `1,904.44` |
| `Live` | `Long` | `41.50` | 127,980,000.00 USD | 0.00 USD | 43,170.00 USD | `-58.95%` | `1,040.15` |
| `Live` | `Long` | `42.50` | 127,940,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-57.96%` | `25,592.18` |
| `Live` | `Long` | `43.50` | 126,850,000.00 USD | 0.00 USD | 46,760.00 USD | `-56.97%` | `1,074.97` |
| `Live` | `Long` | `44.50` | 126,810,000.00 USD | 0.00 USD | 305,790.00 USD | `-55.98%` | `6,871.68` |
| `Live` | `Long` | `45.50` | 126,500,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-55.00%` | `41,399.20` |
| `Live` | `Long` | `46.50` | 124,620,000.00 USD | 0.00 USD | 6,000.00 USD | `-54.01%` | `129.09` |
| `Live` | `Long` | `47.50` | 124,610,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-53.02%` | `82,498.98` |
| `Live` | `Long` | `48.50` | 120,690,000.00 USD | 0.00 USD | 64,870.00 USD | `-52.03%` | `1,337.48` |
| `Live` | `Long` | `49.50` | 120,630,000.00 USD | 0.00 USD | 80,310.00 USD | `-51.04%` | `1,622.49` |
| `Live` | `Long` | `50.50` | 120,550,000.00 USD | 0.00 USD | 163,360.00 USD | `-50.05%` | `3,234.85` |
| `Live` | `Long` | `51.50` | 120,380,000.00 USD | 0.00 USD | 800,950.00 USD | `-49.06%` | `15,552.44` |
| `Live` | `Long` | `52.50` | 119,580,000.00 USD | 0.00 USD | 101,460.00 USD | `-48.07%` | `1,932.48` |
| `Live` | `Long` | `53.50` | 119,480,000.00 USD | 0.00 USD | 3,420,000.00 USD | `-47.08%` | `63,935.80` |
| `Live` | `Long` | `54.50` | 116,060,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-46.09%` | `20,606.51` |
| `Live` | `Long` | `55.50` | 114,940,000.00 USD | 0.00 USD | 182,390.00 USD | `-45.10%` | `3,286.39` |
| `Live` | `Long` | `56.50` | 114,760,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-44.12%` | `28,105.53` |
| `Live` | `Long` | `57.50` | 113,170,000.00 USD | 0.00 USD | 112,290.00 USD | `-43.13%` | `1,952.89` |
| `Live` | `Long` | `58.50` | 113,060,000.00 USD | 0.00 USD | 184,220.00 USD | `-42.14%` | `3,149.06` |
| `Live` | `Long` | `59.50` | 112,870,000.00 USD | 0.00 USD | 134,170.00 USD | `-41.15%` | `2,255.03` |
| `Live` | `Long` | `60.50` | 112,740,000.00 USD | 0.00 USD | 177,470.00 USD | `-40.16%` | `2,933.39` |
| `Live` | `Long` | `61.50` | 112,560,000.00 USD | 0.00 USD | 228,150.00 USD | `-39.17%` | `3,709.83` |
| `Live` | `Long` | `62.50` | 112,330,000.00 USD | 0.00 USD | 217,380.00 USD | `-38.18%` | `3,478.04` |
| `Live` | `Long` | `63.50` | 112,110,000.00 USD | 0.00 USD | 376,000.00 USD | `-37.19%` | `5,921.33` |
| `Live` | `Long` | `64.50` | 111,740,000.00 USD | 0.00 USD | 75,240.00 USD | `-36.20%` | `1,166.47` |
| `Live` | `Long` | `65.50` | 111,660,000.00 USD | 0.00 USD | 11,940,000.00 USD | `-35.21%` | `182,345.10` |
| `Live` | `Long` | `66.50` | 99,720,000.00 USD | 0.00 USD | 99,120.00 USD | `-34.22%` | `1,490.55` |
| `Live` | `Long` | `67.50` | 99,620,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-33.24%` | `15,598.58` |
| `Live` | `Long` | `68.50` | 98,570,000.00 USD | 0.00 USD | 37,930,000.00 USD | `-32.25%` | `553,664.83` |
| `Live` | `Long` | `69.50` | 60,640,000.00 USD | 0.00 USD | 172,850.00 USD | `-31.26%` | `2,487.09` |
| `Live` | `Long` | `70.50` | 60,470,000.00 USD | 0.00 USD | 3,590,000.00 USD | `-30.27%` | `50,879.87` |
| `Live` | `Long` | `71.50` | 56,880,000.00 USD | 0.00 USD | 497,880.00 USD | `-29.28%` | `6,963.33` |
| `Live` | `Long` | `72.50` | 56,380,000.00 USD | 0.00 USD | 1,920,000.00 USD | `-28.29%` | `26,480.44` |
| `Live` | `Long` | `73.50` | 54,460,000.00 USD | 0.00 USD | 590,970.00 USD | `-27.30%` | `8,040.40` |
| `Live` | `Long` | `74.50` | 53,870,000.00 USD | 0.00 USD | 644,710.00 USD | `-26.31%` | `8,653.88` |
| `Live` | `Long` | `75.50` | 53,230,000.00 USD | 0.00 USD | 871,540.00 USD | `-25.32%` | `11,543.64` |
| `Live` | `Long` | `76.50` | 52,360,000.00 USD | 0.00 USD | 441,110.00 USD | `-24.33%` | `5,766.12` |
| `Live` | `Long` | `77.50` | 51,920,000.00 USD | 0.00 USD | 757,050.00 USD | `-23.34%` | `9,768.43` |
| `Live` | `Long` | `78.50` | 51,160,000.00 USD | 0.00 USD | 5,380,000.00 USD | `-22.36%` | `68,540.65` |
| `Live` | `Long` | `79.50` | 45,780,000.00 USD | 0.00 USD | 430,910.00 USD | `-21.37%` | `5,420.22` |
| `Live` | `Long` | `80.50` | 45,350,000.00 USD | 0.00 USD | 2,020,000.00 USD | `-20.38%` | `25,087.54` |
| `Live` | `Long` | `81.50` | 43,330,000.00 USD | 0.00 USD | 2,600,000.00 USD | `-19.39%` | `31,899.01` |
| `Live` | `Long` | `82.50` | 40,730,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-18.40%` | `17,173.82` |
| `Live` | `Long` | `83.50` | 39,310,000.00 USD | 0.00 USD | 721,890.00 USD | `-17.41%` | `8,645.35` |
| `Live` | `Long` | `84.50` | 38,590,000.00 USD | 0.00 USD | 610,240.00 USD | `-16.42%` | `7,221.77` |
| `Live` | `Long` | `85.50` | 37,980,000.00 USD | 0.00 USD | 956,570.00 USD | `-15.43%` | `11,187.94` |
| `Live` | `Long` | `86.50` | 37,020,000.00 USD | 0.00 USD | 882,970.00 USD | `-14.44%` | `10,207.76` |
| `Live` | `Long` | `87.50` | 36,140,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-13.45%` | `16,186.37` |
| `Live` | `Long` | `88.50` | 34,720,000.00 USD | 0.00 USD | 3,930,000.00 USD | `-12.46%` | `44,426.70` |
| `Live` | `Long` | `89.50` | 30,790,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-11.48%` | `20,893.76` |
| `Live` | `Long` | `90.50` | 28,920,000.00 USD | 0.00 USD | 426,080.00 USD | `-10.49%` | `4,708.06` |
| `Live` | `Long` | `91.50` | 28,490,000.00 USD | 0.00 USD | 3,170,000.00 USD | `-9.50%` | `34,668.72` |
| `Live` | `Long` | `92.50` | 25,320,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-8.51%` | `24,997.59` |
| `Live` | `Long` | `93.50` | 23,010,000.00 USD | 0.00 USD | 3,170,000.00 USD | `-7.52%` | `33,932.78` |
| `Live` | `Long` | `94.50` | 19,840,000.00 USD | 0.00 USD | 2,910,000.00 USD | `-6.53%` | `30,794.19` |
| `Live` | `Long` | `95.50` | 16,930,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-5.54%` | `16,934.75` |
| `Live` | `Long` | `96.50` | 15,310,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-4.55%` | `14,096.22` |
| `Live` | `Long` | `97.50` | 13,950,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-3.56%` | `25,290.68` |
| `Live` | `Long` | `98.50` | 11,480,000.00 USD | 0.00 USD | 10,960,000.00 USD | `-2.57%` | `111,319.00` |
| `Live` | `Long` | `99.50` | 519,290.00 USD | 0.00 USD | 481,350.00 USD | `-1.58%` | `4,837.73` |
| `Live` | `Long` | `100.50` | 37,930.00 USD | 0.00 USD | 37,930.00 USD | `-0.60%` | `377.44` |
| `Live` | `Short` | `101.50` | 96,850.00 USD | 96,850.00 USD | 0.00 USD | `+0.39%` | `954.19` |
| `Live` | `Short` | `102.50` | 107,970.00 USD | 11,120.00 USD | 0.00 USD | `+1.38%` | `108.53` |
| `Live` | `Short` | `103.50` | 137,030.00 USD | 29,050.00 USD | 0.00 USD | `+2.37%` | `280.71` |
| `Live` | `Short` | `104.50` | 1,330,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+3.36%` | `11,422.89` |
| `Live` | `Short` | `105.50` | 1,500,000.00 USD | 167,490.00 USD | 0.00 USD | `+4.35%` | `1,587.59` |
| `Live` | `Short` | `106.50` | 1,510,000.00 USD | 13,380.00 USD | 0.00 USD | `+5.34%` | `125.60` |
| `Live` | `Short` | `107.50` | 1,880,000.00 USD | 368,250.00 USD | 0.00 USD | `+6.33%` | `3,425.54` |
| `Live` | `Short` | `108.50` | 1,980,000.00 USD | 102,250.00 USD | 0.00 USD | `+7.32%` | `942.41` |
| `Live` | `Short` | `109.50` | 2,590,000.00 USD | 609,280.00 USD | 0.00 USD | `+8.31%` | `5,564.22` |
| `Live` | `Short` | `110.50` | 2,790,000.00 USD | 195,830.00 USD | 0.00 USD | `+9.30%` | `1,772.19` |
| `Live` | `Short` | `111.50` | 5,180,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+10.29%` | `21,434.38` |
| `Live` | `Short` | `112.50` | 5,300,000.00 USD | 125,350.00 USD | 0.00 USD | `+11.27%` | `1,114.19` |
| `Live` | `Short` | `113.50` | 5,530,000.00 USD | 224,480.00 USD | 0.00 USD | `+12.26%` | `1,977.81` |
| `Live` | `Short` | `114.50` | 5,590,000.00 USD | 62,000.00 USD | 0.00 USD | `+13.25%` | `541.48` |
| `Live` | `Short` | `115.50` | 6,530,000.00 USD | 945,940.00 USD | 0.00 USD | `+14.24%` | `8,189.93` |
| `Live` | `Short` | `116.50` | 6,690,000.00 USD | 157,330.00 USD | 0.00 USD | `+15.23%` | `1,350.46` |
| `Live` | `Short` | `117.50` | 11,290,000.00 USD | 4,600,000.00 USD | 0.00 USD | `+16.22%` | `39,166.67` |
| `Live` | `Short` | `118.50` | 12,020,000.00 USD | 725,160.00 USD | 0.00 USD | `+17.21%` | `6,119.46` |
| `Live` | `Short` | `119.50` | 12,380,000.00 USD | 358,660.00 USD | 0.00 USD | `+18.20%` | `3,001.30` |
| `Live` | `Short` | `120.50` | 12,390,000.00 USD | 7,000.00 USD | 0.00 USD | `+19.19%` | `58.05` |
| `Live` | `Short` | `121.50` | 12,500,000.00 USD | 113,860.00 USD | 0.00 USD | `+20.18%` | `937.09` |
| `Live` | `Short` | `122.50` | 12,580,000.00 USD | 82,340.00 USD | 0.00 USD | `+21.17%` | `672.17` |
| `Live` | `Short` | `123.50` | 12,600,000.00 USD | 17,790.00 USD | 0.00 USD | `+22.15%` | `144.05` |
| `Live` | `Short` | `124.50` | 12,800,000.00 USD | 204,410.00 USD | 0.00 USD | `+23.14%` | `1,641.86` |
| `Live` | `Short` | `125.50` | 13,320,000.00 USD | 512,840.00 USD | 0.00 USD | `+24.13%` | `4,086.37` |
| `Live` | `Short` | `126.50` | 25,860,000.00 USD | 12,540,000.00 USD | 0.00 USD | `+25.12%` | `99,153.38` |
| `Live` | `Short` | `127.50` | 26,630,000.00 USD | 770,400.00 USD | 0.00 USD | `+26.11%` | `6,042.37` |
| `Live` | `Short` | `128.50` | 37,130,000.00 USD | 10,500,000.00 USD | 0.00 USD | `+27.10%` | `81,695.44` |
| `Live` | `Short` | `129.50` | 37,290,000.00 USD | 164,320.00 USD | 0.00 USD | `+28.09%` | `1,268.86` |
| `Live` | `Short` | `130.50` | 37,890,000.00 USD | 602,490.00 USD | 0.00 USD | `+29.08%` | `4,616.78` |
| `Live` | `Short` | `131.50` | 37,910,000.00 USD | 18,810.00 USD | 0.00 USD | `+30.07%` | `143.01` |
| `Live` | `Short` | `132.50` | 37,980,000.00 USD | 68,510.00 USD | 0.00 USD | `+31.06%` | `517.05` |
| `Live` | `Short` | `133.50` | 39,260,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+32.05%` | `9,542.34` |
| `Live` | `Short` | `134.50` | 39,290,000.00 USD | 35,860.00 USD | 0.00 USD | `+33.03%` | `266.61` |
| `Live` | `Short` | `135.50` | 40,010,000.00 USD | 719,490.00 USD | 0.00 USD | `+34.02%` | `5,309.86` |
| `Live` | `Short` | `136.50` | 40,020,000.00 USD | 8,680.00 USD | 0.00 USD | `+35.01%` | `63.60` |
| `Live` | `Short` | `137.50` | 40,020,000.00 USD | 3,760.00 USD | 0.00 USD | `+36.00%` | `27.32` |
| `Live` | `Short` | `138.50` | 42,340,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+36.99%` | `16,733.65` |
| `Live` | `Short` | `139.50` | 43,490,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+37.98%` | `8,252.19` |
| `Live` | `Short` | `140.50` | 43,510,000.00 USD | 14,240.00 USD | 0.00 USD | `+38.97%` | `101.38` |
| `Live` | `Short` | `141.50` | 43,970,000.00 USD | 462,490.00 USD | 0.00 USD | `+39.96%` | `3,268.45` |
| `Live` | `Short` | `142.50` | 44,070,000.00 USD | 96,470.00 USD | 0.00 USD | `+40.95%` | `676.97` |
| `Live` | `Short` | `143.50` | 44,260,000.00 USD | 198,910.00 USD | 0.00 USD | `+41.94%` | `1,386.10` |
| `Live` | `Short` | `144.50` | 45,220,000.00 USD | 957,190.00 USD | 0.00 USD | `+42.93%` | `6,624.16` |
| `Live` | `Short` | `145.50` | 45,240,000.00 USD | 16,290.00 USD | 0.00 USD | `+43.91%` | `111.97` |
| `Live` | `Short` | `146.50` | 45,930,000.00 USD | 691,960.00 USD | 0.00 USD | `+44.90%` | `4,723.31` |
| `Live` | `Short` | `147.50` | 46,030,000.00 USD | 103,680.00 USD | 0.00 USD | `+45.89%` | `702.90` |
| `Live` | `Short` | `148.50` | 48,380,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+46.88%` | `15,827.51` |
| `Live` | `Short` | `149.50` | 48,400,000.00 USD | 19,740.00 USD | 0.00 USD | `+47.87%` | `132.06` |
| `Live` | `Short` | `150.50` | 48,410,000.00 USD | 5,850.00 USD | 0.00 USD | `+48.86%` | `38.87` |
| `Live` | `Short` | `151.50` | 48,430,000.00 USD | 19,740.00 USD | 0.00 USD | `+49.85%` | `130.32` |
| `Live` | `Short` | `152.50` | 50,760,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+50.84%` | `15,304.70` |
| `Live` | `Short` | `153.50` | 51,190,000.00 USD | 429,190.00 USD | 0.00 USD | `+51.83%` | `2,796.03` |
| `Live` | `Short` | `154.50` | 51,200,000.00 USD | 7,250.00 USD | 0.00 USD | `+52.82%` | `46.90` |
| `Live` | `Short` | `155.50` | 51,370,000.00 USD | 168,990.00 USD | 0.00 USD | `+53.81%` | `1,086.78` |
| `Live` | `Short` | `156.50` | 56,370,000.00 USD | 5,000,000.00 USD | 0.00 USD | `+54.79%` | `31,929.23` |
| `Live` | `Short` | `157.50` | 58,030,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+55.78%` | `10,540.87` |
| `Live` | `Short` | `158.50` | 58,150,000.00 USD | 120,580.00 USD | 0.00 USD | `+56.77%` | `760.78` |
| `Live` | `Short` | `159.50` | 58,290,000.00 USD | 148,650.00 USD | 0.00 USD | `+57.76%` | `931.95` |
| `Live` | `Short` | `160.50` | 59,110,000.00 USD | 817,810.00 USD | 0.00 USD | `+58.75%` | `5,095.36` |
| `Live` | `Short` | `161.50` | 59,410,000.00 USD | 297,730.00 USD | 0.00 USD | `+59.74%` | `1,843.51` |
| `Live` | `Short` | `162.50` | 59,420,000.00 USD | 12,910.00 USD | 0.00 USD | `+60.73%` | `79.45` |
| `Live` | `Short` | `163.50` | 59,430,000.00 USD | 3,880.00 USD | 0.00 USD | `+61.72%` | `23.71` |
| `Live` | `Short` | `164.50` | 59,690,000.00 USD | 261,230.00 USD | 0.00 USD | `+62.71%` | `1,588.02` |
| `Live` | `Short` | `165.50` | 96,240,000.00 USD | 36,550,000.00 USD | 0.00 USD | `+63.70%` | `220,873.34` |
| `Live` | `Short` | `166.50` | 97,470,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+64.69%` | `7,393.77` |
| `Live` | `Short` | `167.50` | 103,450,000.00 USD | 5,980,000.00 USD | 0.00 USD | `+65.67%` | `35,677.30` |
| `Live` | `Short` | `168.50` | 103,940,000.00 USD | 485,410.00 USD | 0.00 USD | `+66.66%` | `2,880.80` |
| `Live` | `Short` | `169.50` | 104,040,000.00 USD | 101,700.00 USD | 0.00 USD | `+67.65%` | `600.00` |
| `Live` | `Short` | `170.50` | 104,040,000.00 USD | 231.88 USD | 0.00 USD | `+68.64%` | `1.36` |
| `Live` | `Short` | `171.50` | 104,040,000.00 USD | 509.35 USD | 0.00 USD | `+69.63%` | `2.97` |
| `Live` | `Short` | `172.50` | 104,100,000.00 USD | 65,260.00 USD | 0.00 USD | `+70.62%` | `378.33` |
| `Live` | `Short` | `173.50` | 104,170,000.00 USD | 63,530.00 USD | 0.00 USD | `+71.61%` | `366.15` |
| `Live` | `Short` | `174.50` | 104,720,000.00 USD | 557,520.00 USD | 0.00 USD | `+72.60%` | `3,194.96` |
| `Live` | `Short` | `175.50` | 104,730,000.00 USD | 4,880.00 USD | 0.00 USD | `+73.59%` | `27.80` |
| `Live` | `Short` | `176.50` | 104,760,000.00 USD | 27,570.00 USD | 0.00 USD | `+74.58%` | `156.23` |
| `Live` | `Short` | `177.50` | 104,830,000.00 USD | 78,100.00 USD | 0.00 USD | `+75.57%` | `440.00` |
| `Live` | `Short` | `178.50` | 107,820,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+76.56%` | `16,710.60` |
| `Live` | `Short` | `179.50` | 107,820,000.00 USD | 829.29 USD | 0.00 USD | `+77.54%` | `4.62` |
| `Live` | `Short` | `180.50` | 107,830,000.00 USD | 13,820.00 USD | 0.00 USD | `+78.53%` | `76.54` |
| `Live` | `Short` | `181.50` | 107,840,000.00 USD | 11,650.00 USD | 0.00 USD | `+79.52%` | `64.21` |
| `Live` | `Short` | `182.50` | 108,140,000.00 USD | 297,920.00 USD | 0.00 USD | `+80.51%` | `1,632.44` |
| `Live` | `Short` | `183.50` | 108,510,000.00 USD | 372,500.00 USD | 0.00 USD | `+81.50%` | `2,030.00` |
| `Live` | `Short` | `184.50` | 108,680,000.00 USD | 165,370.00 USD | 0.00 USD | `+82.49%` | `896.30` |
| `Live` | `Short` | `185.50` | 108,890,000.00 USD | 206,840.00 USD | 0.00 USD | `+83.48%` | `1,115.02` |
| `Live` | `Short` | `186.50` | 109,660,000.00 USD | 774,320.00 USD | 0.00 USD | `+84.47%` | `4,151.86` |
| `Live` | `Short` | `187.50` | 109,700,000.00 USD | 41,020.00 USD | 0.00 USD | `+85.46%` | `218.77` |
| `Live` | `Short` | `188.50` | 109,890,000.00 USD | 187,240.00 USD | 0.00 USD | `+86.45%` | `993.33` |
| `Live` | `Short` | `189.50` | 110,240,000.00 USD | 349,140.00 USD | 0.00 USD | `+87.44%` | `1,842.41` |
| `Live` | `Short` | `190.50` | 124,120,000.00 USD | 13,880,000.00 USD | 0.00 USD | `+88.42%` | `72,853.82` |
| `Live` | `Short` | `191.50` | 124,120,000.00 USD | 321.72 USD | 0.00 USD | `+89.41%` | `1.68` |
| `Live` | `Short` | `192.50` | 124,230,000.00 USD | 109,870.00 USD | 0.00 USD | `+90.40%` | `570.74` |
| `Live` | `Short` | `193.50` | 124,370,000.00 USD | 144,570.00 USD | 0.00 USD | `+91.39%` | `747.11` |
| `Live` | `Short` | `194.50` | 124,520,000.00 USD | 148,800.00 USD | 0.00 USD | `+92.38%` | `765.03` |
| `Live` | `Short` | `195.50` | 124,580,000.00 USD | 62,580.00 USD | 0.00 USD | `+93.37%` | `320.12` |
| `Live` | `Short` | `196.50` | 124,600,000.00 USD | 15,680.00 USD | 0.00 USD | `+94.36%` | `79.79` |
| `Live` | `Short` | `197.50` | 124,840,000.00 USD | 246,140.00 USD | 0.00 USD | `+95.35%` | `1,246.30` |
| `Live` | `Short` | `198.50` | 124,930,000.00 USD | 84,450.00 USD | 0.00 USD | `+96.34%` | `425.42` |
| `Live` | `Short` | `199.50` | 124,980,000.00 USD | 53,380.00 USD | 0.00 USD | `+97.33%` | `267.58` |
| `Live` | `Short` | `200.50` | 125,300,000.00 USD | 314,450.00 USD | 0.00 USD | `+98.32%` | `1,568.35` |
| `Live` | `Short` | `201.50` | 125,310,000.00 USD | 9,970.00 USD | 0.00 USD | `+99.30%` | `49.48` |
| `Live` | `Short` | `202.50` | 129,620,000.00 USD | 4,310,000.00 USD | 0.00 USD | `+100.29%` | `21,284.01` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.50` | 12,730,000.00 USD | 0.00 USD | 15,460.00 USD | `-76.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.50` | 12,710,000.00 USD | 0.00 USD | 3,830.00 USD | `-74.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.50` | 12,710,000.00 USD | 0.00 USD | 105.20 USD | `-73.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.50` | 12,710,000.00 USD | 0.00 USD | 527.35 USD | `-69.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.50` | 12,710,000.00 USD | 0.00 USD | 829.46 USD | `-66.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.50` | 12,710,000.00 USD | 0.00 USD | 1,320.00 USD | `-65.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.50` | 12,710,000.00 USD | 0.00 USD | 199.88 USD | `-62.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.50` | 12,710,000.00 USD | 0.00 USD | 205.21 USD | `-61.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.50` | 12,710,000.00 USD | 0.00 USD | 3,620.00 USD | `-60.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.50` | 12,700,000.00 USD | 0.00 USD | 423.63 USD | `-59.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.50` | 12,700,000.00 USD | 0.00 USD | 170,330.00 USD | `-57.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.50` | 12,530,000.00 USD | 0.00 USD | 104.40 USD | `-56.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.50` | 12,530,000.00 USD | 0.00 USD | 64,090.00 USD | `-55.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.50` | 12,470,000.00 USD | 0.00 USD | 249.71 USD | `-54.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.50` | 12,470,000.00 USD | 0.00 USD | 332.50 USD | `-53.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.50` | 12,470,000.00 USD | 0.00 USD | 102.82 USD | `-52.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.50` | 12,470,000.00 USD | 0.00 USD | 5,510.00 USD | `-50.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.50` | 12,460,000.00 USD | 0.00 USD | 4,070.00 USD | `-49.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.50` | 12,460,000.00 USD | 0.00 USD | 427.88 USD | `-48.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.50` | 12,460,000.00 USD | 0.00 USD | 26,860.00 USD | `-47.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.50` | 12,430,000.00 USD | 0.00 USD | 785.89 USD | `-46.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.50` | 12,430,000.00 USD | 0.00 USD | 210.90 USD | `-45.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.50` | 12,430,000.00 USD | 0.00 USD | 5,860.00 USD | `-44.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.50` | 12,420,000.00 USD | 0.00 USD | 6,550.00 USD | `-43.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.50` | 12,420,000.00 USD | 0.00 USD | 159.71 USD | `-42.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.50` | 12,420,000.00 USD | 0.00 USD | 10,860.00 USD | `-41.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.50` | 12,410,000.00 USD | 0.00 USD | 40,470.00 USD | `-40.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.50` | 12,370,000.00 USD | 0.00 USD | 18,990.00 USD | `-39.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.50` | 12,350,000.00 USD | 0.00 USD | 4,810.00 USD | `-38.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.50` | 12,340,000.00 USD | 0.00 USD | 13,260.00 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.50` | 12,330,000.00 USD | 0.00 USD | 129.00 USD | `-36.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.50` | 12,330,000.00 USD | 0.00 USD | 4,650.00 USD | `-35.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.50` | 12,320,000.00 USD | 0.00 USD | 7,690.00 USD | `-34.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.50` | 12,320,000.00 USD | 0.00 USD | 607.50 USD | `-33.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.50` | 12,320,000.00 USD | 0.00 USD | 7,360.00 USD | `-32.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.50` | 12,310,000.00 USD | 0.00 USD | 54,850.00 USD | `-31.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.50` | 12,250,000.00 USD | 0.00 USD | 50,700.00 USD | `-30.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.50` | 12,200,000.00 USD | 0.00 USD | 1,470.00 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.50` | 12,200,000.00 USD | 0.00 USD | 120,230.00 USD | `-28.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.50` | 12,080,000.00 USD | 0.00 USD | 139.65 USD | `-27.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.50` | 12,080,000.00 USD | 0.00 USD | 52,170.00 USD | `-26.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.50` | 12,030,000.00 USD | 0.00 USD | 26,730.00 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.50` | 12,000,000.00 USD | 0.00 USD | 16,050.00 USD | `-24.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.50` | 11,990,000.00 USD | 0.00 USD | 14,790.00 USD | `-23.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.50` | 11,970,000.00 USD | 0.00 USD | 81,220.00 USD | `-22.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.50` | 11,890,000.00 USD | 0.00 USD | 13,780.00 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.50` | 11,880,000.00 USD | 0.00 USD | 118,650.00 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.50` | 11,760,000.00 USD | 0.00 USD | 91,450.00 USD | `-19.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.50` | 11,670,000.00 USD | 0.00 USD | 27,520.00 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.50` | 11,640,000.00 USD | 0.00 USD | 74,090.00 USD | `-17.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.50` | 11,560,000.00 USD | 0.00 USD | 24,890.00 USD | `-16.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.50` | 11,540,000.00 USD | 0.00 USD | 171,750.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.50` | 11,370,000.00 USD | 0.00 USD | 16,860.00 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.50` | 11,350,000.00 USD | 0.00 USD | 233,390.00 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.50` | 11,120,000.00 USD | 0.00 USD | 281,840.00 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.50` | 10,840,000.00 USD | 0.00 USD | 69,740.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.50` | 10,770,000.00 USD | 0.00 USD | 175,260.00 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.50` | 10,590,000.00 USD | 0.00 USD | 435,590.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.50` | 10,150,000.00 USD | 0.00 USD | 224,950.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.50` | 9,930,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.50` | 8,860,000.00 USD | 0.00 USD | 591,380.00 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.50` | 8,270,000.00 USD | 0.00 USD | 976,790.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.50` | 7,290,000.00 USD | 0.00 USD | 604,550.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.50` | 6,680,000.00 USD | 0.00 USD | 491,960.00 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.50` | 6,190,000.00 USD | 0.00 USD | 3,480,000.00 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.50` | 2,710,000.00 USD | 0.00 USD | 910,510.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `100.50` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.50` | 797,300.00 USD | 797,300.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.50` | 1,600,000.00 USD | 805,020.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.50` | 1,950,000.00 USD | 348,530.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.50` | 2,690,000.00 USD | 742,710.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.50` | 3,130,000.00 USD | 438,000.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.50` | 3,500,000.00 USD | 364,850.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.50` | 3,710,000.00 USD | 210,000.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.50` | 4,070,000.00 USD | 359,420.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.50` | 8,370,000.00 USD | 4,300,000.00 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.50` | 9,750,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+9.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.50` | 9,800,000.00 USD | 54,160.00 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.50` | 10,030,000.00 USD | 222,460.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.50` | 10,310,000.00 USD | 281,630.00 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.50` | 10,340,000.00 USD | 32,520.00 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.50` | 10,460,000.00 USD | 119,540.00 USD | 0.00 USD | `+14.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.50` | 10,510,000.00 USD | 47,920.00 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.50` | 10,760,000.00 USD | 254,840.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.50` | 10,940,000.00 USD | 178,980.00 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.50` | 11,180,000.00 USD | 239,490.00 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.50` | 11,330,000.00 USD | 153,100.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.50` | 11,410,000.00 USD | 75,990.00 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.50` | 11,940,000.00 USD | 526,980.00 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.50` | 13,000,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.50` | 13,170,000.00 USD | 166,110.00 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.50` | 13,720,000.00 USD | 554,500.00 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.50` | 13,840,000.00 USD | 114,230.00 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.50` | 14,110,000.00 USD | 275,030.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.50` | 14,170,000.00 USD | 58,000.00 USD | 0.00 USD | `+27.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.50` | 16,830,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.50` | 16,890,000.00 USD | 54,500.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.50` | 17,060,000.00 USD | 179,050.00 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.50` | 17,090,000.00 USD | 26,010.00 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.50` | 17,100,000.00 USD | 13,090.00 USD | 0.00 USD | `+32.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.50` | 17,350,000.00 USD | 250,620.00 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.50` | 17,430,000.00 USD | 74,880.00 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.50` | 17,430,000.00 USD | 3,770.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.50` | 17,470,000.00 USD | 34,120.00 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.50` | 24,230,000.00 USD | 6,760,000.00 USD | 0.00 USD | `+36.99%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `139.50` | 26,440,000.00 USD | 2,220,000.00 USD | 0.00 USD | `+37.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.50` | 26,730,000.00 USD | 286,300.00 USD | 0.00 USD | `+38.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.50` | 26,740,000.00 USD | 10,520.00 USD | 0.00 USD | `+39.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.50` | 27,080,000.00 USD | 346,440.00 USD | 0.00 USD | `+40.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.50` | 27,080,000.00 USD | 529.51 USD | 0.00 USD | `+41.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.50` | 27,350,000.00 USD | 269,670.00 USD | 0.00 USD | `+42.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.50` | 27,370,000.00 USD | 13,070.00 USD | 0.00 USD | `+43.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.50` | 27,570,000.00 USD | 198,500.00 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.50` | 27,610,000.00 USD | 46,350.00 USD | 0.00 USD | `+45.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.50` | 28,950,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.50` | 29,460,000.00 USD | 512,760.00 USD | 0.00 USD | `+47.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.50` | 29,730,000.00 USD | 269,220.00 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.50` | 29,750,000.00 USD | 16,890.00 USD | 0.00 USD | `+49.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.50` | 29,760,000.00 USD | 12,020.00 USD | 0.00 USD | `+50.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.50` | 29,770,000.00 USD | 11,660.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.50` | 29,780,000.00 USD | 12,130.00 USD | 0.00 USD | `+52.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.50` | 29,790,000.00 USD | 13,650.00 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.50` | 29,800,000.00 USD | 2,230.00 USD | 0.00 USD | `+54.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.50` | 29,820,000.00 USD | 22,350.00 USD | 0.00 USD | `+56.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.50` | 29,820,000.00 USD | 815.04 USD | 0.00 USD | `+57.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.50` | 30,060,000.00 USD | 242,540.00 USD | 0.00 USD | `+58.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.50` | 30,060,000.00 USD | 282.62 USD | 0.00 USD | `+59.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.50` | 30,070,000.00 USD | 5,030.00 USD | 0.00 USD | `+61.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.50` | 30,150,000.00 USD | 83,570.00 USD | 0.00 USD | `+63.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.50` | 30,150,000.00 USD | 517.81 USD | 0.00 USD | `+64.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.50` | 30,150,000.00 USD | 2,030.00 USD | 0.00 USD | `+65.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.50` | 30,160,000.00 USD | 5,560.00 USD | 0.00 USD | `+66.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.50` | 30,160,000.00 USD | 1,410.00 USD | 0.00 USD | `+67.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.50` | 30,200,000.00 USD | 42,950.00 USD | 0.00 USD | `+68.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.50` | 30,200,000.00 USD | 686.00 USD | 0.00 USD | `+69.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.50` | 30,240,000.00 USD | 36,070.00 USD | 0.00 USD | `+70.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.50` | 30,250,000.00 USD | 6,550.00 USD | 0.00 USD | `+71.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.50` | 30,320,000.00 USD | 74,640.00 USD | 0.00 USD | `+73.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.50` | 30,320,000.00 USD | 1,450.00 USD | 0.00 USD | `+74.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.50` | 30,330,000.00 USD | 2,140.00 USD | 0.00 USD | `+75.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.50` | 30,330,000.00 USD | 2,990.00 USD | 0.00 USD | `+76.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.50` | 30,330,000.00 USD | 262.07 USD | 0.00 USD | `+77.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.50` | 30,430,000.00 USD | 102,680.00 USD | 0.00 USD | `+78.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.50` | 30,430,000.00 USD | 2,730.00 USD | 0.00 USD | `+79.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.50` | 30,450,000.00 USD | 19,620.00 USD | 0.00 USD | `+80.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.50` | 31,000,000.00 USD | 550,500.00 USD | 0.00 USD | `+81.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.50` | 31,030,000.00 USD | 29,490.00 USD | 0.00 USD | `+83.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.50` | 31,220,000.00 USD | 191,020.00 USD | 0.00 USD | `+85.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.50` | 31,370,000.00 USD | 141,530.00 USD | 0.00 USD | `+86.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.50` | 31,410,000.00 USD | 38,960.00 USD | 0.00 USD | `+88.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.50` | 31,410,000.00 USD | 4,280.00 USD | 0.00 USD | `+92.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.50` | 31,410,000.00 USD | 1,760.00 USD | 0.00 USD | `+93.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `196.50` | 31,670,000.00 USD | 253,980.00 USD | 0.00 USD | `+94.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.50` | 31,760,000.00 USD | 94,590.00 USD | 0.00 USD | `+95.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.50` | 32,130,000.00 USD | 374,220.00 USD | 0.00 USD | `+96.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `199.50` | 32,160,000.00 USD | 28,310.00 USD | 0.00 USD | `+97.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `200.50` | 32,470,000.00 USD | 302,560.00 USD | 0.00 USD | `+98.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `201.50` | 32,470,000.00 USD | 398.97 USD | 0.00 USD | `+99.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `202.50` | 32,470,000.00 USD | 2,430.00 USD | 0.00 USD | `+100.29%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `89.60` | 369,220,000.00 USD | 0.00 USD | 369,220,000.00 USD | 700,630.00 USD | 276,340.00 USD | 577,220.00 USD |
| `7D` | `89.80` | 367,670,000.00 USD | 0.00 USD | 367,670,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD |
| `7D` | `90.00` | 366,680,000.00 USD | 0.00 USD | 366,680,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `7D` | `90.20` | 364,960,000.00 USD | 0.00 USD | 364,960,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD |
| `1D` | `90.30` | 175,930,000.00 USD | 0.00 USD | 175,930,000.00 USD | 362,900.00 USD | 536,640.00 USD | 506,490.00 USD |
| `7D` | `90.40` | 362,960,000.00 USD | 0.00 USD | 362,960,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `90.50` | 174,520,000.00 USD | 0.00 USD | 174,520,000.00 USD | 486,210.00 USD | 399,670.00 USD | 359,630.00 USD |
| `7D` | `90.60` | 361,560,000.00 USD | 0.00 USD | 361,560,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD |
| `1D` | `90.70` | 173,270,000.00 USD | 0.00 USD | 173,270,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD |
| `7D` | `90.80` | 358,450,000.00 USD | 0.00 USD | 358,450,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `90.90` | 172,770,000.00 USD | 0.00 USD | 172,770,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD |
| `7D` | `91.00` | 355,470,000.00 USD | 0.00 USD | 355,470,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `91.10` | 172,670,000.00 USD | 0.00 USD | 172,670,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD |
| `7D` | `91.20` | 353,410,000.00 USD | 0.00 USD | 353,410,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `91.30` | 172,480,000.00 USD | 0.00 USD | 172,480,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD |
| `7D` | `91.40` | 351,080,000.00 USD | 0.00 USD | 351,080,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD |
| `1D` | `91.50` | 172,330,000.00 USD | 0.00 USD | 172,330,000.00 USD | 21,670.00 USD | 87,530.00 USD | 1,730.00 USD |
| `7D` | `91.60` | 347,750,000.00 USD | 0.00 USD | 347,750,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `91.70` | 172,220,000.00 USD | 0.00 USD | 172,220,000.00 USD | 107,440.00 USD | 112,260.00 USD | 56,750.00 USD |
| `7D` | `91.80` | 346,130,000.00 USD | 0.00 USD | 346,130,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `91.90` | 171,950,000.00 USD | 0.00 USD | 171,950,000.00 USD | 326,750.00 USD | 140,660.00 USD | 177,950.00 USD |
| `7D` | `92.00` | 343,930,000.00 USD | 0.00 USD | 343,930,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `92.10` | 171,300,000.00 USD | 0.00 USD | 171,300,000.00 USD | 218,720.00 USD | 124,560.00 USD | 64,070.00 USD |
| `7D` | `92.20` | 342,190,000.00 USD | 0.00 USD | 342,190,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `1D` | `92.30` | 170,890,000.00 USD | 0.00 USD | 170,890,000.00 USD | 219,340.00 USD | 97,250.00 USD | 738,010.00 USD |
| `7D` | `92.40` | 341,330,000.00 USD | 0.00 USD | 341,330,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD |
| `1D` | `92.50` | 169,840,000.00 USD | 0.00 USD | 169,840,000.00 USD | 37,670.00 USD | 53,380.00 USD | 168,480.00 USD |
| `7D` | `92.60` | 339,420,000.00 USD | 0.00 USD | 339,420,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `1D` | `92.70` | 169,580,000.00 USD | 0.00 USD | 169,580,000.00 USD | 0.00 USD | 86,970.00 USD | 168,150.00 USD |
| `7D` | `92.80` | 338,340,000.00 USD | 0.00 USD | 338,340,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `1D` | `92.90` | 169,330,000.00 USD | 0.00 USD | 169,330,000.00 USD | 100,830.00 USD | 0.00 USD | 60,580.00 USD |
| `7D` | `93.00` | 338,110,000.00 USD | 0.00 USD | 338,110,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `1D` | `93.10` | 169,160,000.00 USD | 0.00 USD | 169,160,000.00 USD | 0.00 USD | 2,580.00 USD | 115,350.00 USD |
| `7D` | `93.20` | 337,720,000.00 USD | 0.00 USD | 337,720,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD |
| `1D` | `93.30` | 169,050,000.00 USD | 0.00 USD | 169,050,000.00 USD | 0.00 USD | 103,020.00 USD | 99,970.00 USD |
| `7D` | `93.40` | 337,610,000.00 USD | 0.00 USD | 337,610,000.00 USD | 15,260.00 USD | 81,430.00 USD | 1,290.00 USD |
| `7D` | `93.60` | 337,520,000.00 USD | 0.00 USD | 337,520,000.00 USD | 238,200.00 USD | 343,740.00 USD | 114,860.00 USD |
| `7D` | `93.80` | 336,820,000.00 USD | 0.00 USD | 336,820,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD |
| `7D` | `94.00` | 336,140,000.00 USD | 0.00 USD | 336,140,000.00 USD | 78,790.00 USD | 153,680.00 USD | 134,360.00 USD |
| `7D` | `94.20` | 335,780,000.00 USD | 0.00 USD | 335,780,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD |
| `7D` | `94.40` | 335,120,000.00 USD | 0.00 USD | 335,120,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD |
| `7D` | `94.60` | 334,820,000.00 USD | 0.00 USD | 334,820,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `94.80` | 334,740,000.00 USD | 0.00 USD | 334,740,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD |
| `7D` | `95.00` | 334,720,000.00 USD | 0.00 USD | 334,720,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD |
| `1D` | `95.10` | 168,840,000.00 USD | 0.00 USD | 168,840,000.00 USD | 13,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `95.20` | 333,750,000.00 USD | 0.00 USD | 333,750,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD |
| `1D` | `95.30` | 168,830,000.00 USD | 0.00 USD | 168,830,000.00 USD | 18,710.00 USD | 89,760.00 USD | 6,930.00 USD |
| `7D` | `95.40` | 333,370,000.00 USD | 0.00 USD | 333,370,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD |
| `1D` | `95.50` | 168,710,000.00 USD | 0.00 USD | 168,710,000.00 USD | 679,320.00 USD | 458,400.00 USD | 465,470.00 USD |
| `7D` | `95.60` | 331,850,000.00 USD | 0.00 USD | 331,850,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD |
| `1D` | `95.70` | 167,110,000.00 USD | 0.00 USD | 167,110,000.00 USD | 1,490,000.00 USD | 1,130,000.00 USD | 649,920.00 USD |
| `7D` | `95.80` | 327,800,000.00 USD | 0.00 USD | 327,800,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD |
| `1D` | `95.90` | 163,840,000.00 USD | 0.00 USD | 163,840,000.00 USD | 1,150,000.00 USD | 885,010.00 USD | 1,240,000.00 USD |
| `7D` | `96.00` | 323,560,000.00 USD | 0.00 USD | 323,560,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD |
| `1D` | `96.10` | 160,570,000.00 USD | 0.00 USD | 160,570,000.00 USD | 1,430,000.00 USD | 1,420,000.00 USD | 942,310.00 USD |
| `7D` | `96.20` | 317,130,000.00 USD | 0.00 USD | 317,130,000.00 USD | 2,940,000.00 USD | 1,970,000.00 USD | 1,990,000.00 USD |
| `1D` | `96.30` | 156,780,000.00 USD | 0.00 USD | 156,780,000.00 USD | 875,730.00 USD | 1,140,000.00 USD | 1,180,000.00 USD |
| `7D` | `96.40` | 310,230,000.00 USD | 0.00 USD | 310,230,000.00 USD | 2,950,000.00 USD | 643,110.00 USD | 2,370,000.00 USD |
| `1D` | `96.50` | 153,580,000.00 USD | 0.00 USD | 153,580,000.00 USD | 1,220,000.00 USD | 924,880.00 USD | 1,010,000.00 USD |
| `7D` | `96.60` | 304,260,000.00 USD | 0.00 USD | 304,260,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD |
| `1D` | `96.70` | 150,430,000.00 USD | 0.00 USD | 150,430,000.00 USD | 681,660.00 USD | 858,670.00 USD | 909,580.00 USD |
| `7D` | `96.80` | 296,160,000.00 USD | 0.00 USD | 296,160,000.00 USD | 3,000,000.00 USD | 2,770,000.00 USD | 2,960,000.00 USD |
| `1D` | `96.90` | 147,980,000.00 USD | 0.00 USD | 147,980,000.00 USD | 383,880.00 USD | 290,640.00 USD | 167,820.00 USD |
| `7D` | `97.00` | 287,430,000.00 USD | 0.00 USD | 287,430,000.00 USD | 5,510,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD |
| `1D` | `97.10` | 147,140,000.00 USD | 0.00 USD | 147,140,000.00 USD | 271,410.00 USD | 113,790.00 USD | 379,350.00 USD |
| `7D` | `97.20` | 277,340,000.00 USD | 0.00 USD | 277,340,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,980,000.00 USD |
| `1D` | `97.30` | 146,380,000.00 USD | 0.00 USD | 146,380,000.00 USD | 197,550.00 USD | 378,560.00 USD | 121,680.00 USD |
| `7D` | `97.40` | 263,530,000.00 USD | 0.00 USD | 263,530,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD |
| `1D` | `97.50` | 145,680,000.00 USD | 0.00 USD | 145,680,000.00 USD | 1,460,000.00 USD | 1,060,000.00 USD | 960,650.00 USD |
| `7D` | `97.60` | 253,110,000.00 USD | 0.00 USD | 253,110,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD |
| `1D` | `97.70` | 142,190,000.00 USD | 0.00 USD | 142,190,000.00 USD | 3,210,000.00 USD | 2,660,000.00 USD | 1,430,000.00 USD |
| `7D` | `97.80` | 237,760,000.00 USD | 0.00 USD | 237,760,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD |
| `1D` | `97.90` | 134,890,000.00 USD | 0.00 USD | 134,890,000.00 USD | 3,490,000.00 USD | 2,490,000.00 USD | 2,970,000.00 USD |
| `7D` | `98.00` | 224,300,000.00 USD | 0.00 USD | 224,300,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,710,000.00 USD |
| `1D` | `98.10` | 125,940,000.00 USD | 0.00 USD | 125,940,000.00 USD | 3,460,000.00 USD | 3,450,000.00 USD | 2,600,000.00 USD |
| `7D` | `98.20` | 199,630,000.00 USD | 0.00 USD | 199,630,000.00 USD | 7,790,000.00 USD | 6,660,000.00 USD | 5,670,000.00 USD |
| `1D` | `98.30` | 116,430,000.00 USD | 0.00 USD | 116,430,000.00 USD | 2,900,000.00 USD | 2,950,000.00 USD | 2,690,000.00 USD |
| `7D` | `98.40` | 179,500,000.00 USD | 0.00 USD | 179,500,000.00 USD | 9,460,000.00 USD | 2,950,000.00 USD | 9,620,000.00 USD |
| `1D` | `98.50` | 107,890,000.00 USD | 0.00 USD | 107,890,000.00 USD | 5,870,000.00 USD | 3,960,000.00 USD | 5,640,000.00 USD |
| `7D` | `98.60` | 157,470,000.00 USD | 0.00 USD | 157,470,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD |
| `1D` | `98.70` | 92,440,000.00 USD | 0.00 USD | 92,440,000.00 USD | 7,440,000.00 USD | 6,270,000.00 USD | 4,920,000.00 USD |
| `7D` | `98.80` | 121,980,000.00 USD | 0.00 USD | 121,980,000.00 USD | 12,600,000.00 USD | 9,880,000.00 USD | 13,080,000.00 USD |
| `1D` | `98.90` | 73,800,000.00 USD | 0.00 USD | 73,800,000.00 USD | 5,040,000.00 USD | 4,270,000.00 USD | 5,750,000.00 USD |
| `7D` | `99.00` | 86,420,000.00 USD | 0.00 USD | 86,420,000.00 USD | 14,280,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD |
| `1D` | `99.10` | 58,750,000.00 USD | 0.00 USD | 58,750,000.00 USD | 6,070,000.00 USD | 5,760,000.00 USD | 4,720,000.00 USD |
| `7D` | `99.20` | 44,750,000.00 USD | 0.00 USD | 44,750,000.00 USD | 12,590,000.00 USD | 6,970,000.00 USD | 5,910,000.00 USD |
| `1D` | `99.30` | 42,190,000.00 USD | 0.00 USD | 42,190,000.00 USD | 3,310,000.00 USD | 4,420,000.00 USD | 4,970,000.00 USD |
| `7D` | `99.40` | 19,270,000.00 USD | 0.00 USD | 19,270,000.00 USD | 2,300,000.00 USD | 599,290.00 USD | 6,690,000.00 USD |
| `1D` | `99.50` | 29,490,000.00 USD | 0.00 USD | 29,490,000.00 USD | 4,600,000.00 USD | 3,860,000.00 USD | 3,860,000.00 USD |
| `7D` | `99.60` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD |
| `1D` | `99.70` | 17,160,000.00 USD | 0.00 USD | 17,160,000.00 USD | 2,480,000.00 USD | 3,410,000.00 USD | 3,230,000.00 USD |
| `7D` | `99.80` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD |
| `1D` | `99.90` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 1,650,000.00 USD | 1,300,000.00 USD | 1,100,000.00 USD |
| `7D` | `100.00` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD |
| `1D` | `100.10` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 1,290,000.00 USD | 914,930.00 USD | 1,430,000.00 USD |
| `7D` | `100.20` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD |
| `1D` | `100.30` | 344,600.00 USD | 0.00 USD | 344,600.00 USD | 163,250.00 USD | 176,110.00 USD | 5,240.00 USD |
| `1D` | `100.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `100.40` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD |
| `7D` | `100.40` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD |
| `1D` | `100.50` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,750,000.00 USD |
| `7D` | `100.60` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD |
| `1D` | `100.70` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 274,280.00 USD | 970,010.00 USD | 476,700.00 USD |
| `7D` | `100.80` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 981,100.00 USD | 0.00 USD |
| `1D` | `100.90` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 953,600.00 USD | 5,230.00 USD |
| `7D` | `101.00` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 4,560,000.00 USD | 3,730,000.00 USD |
| `1D` | `101.10` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 6,610,000.00 USD | 3,090,000.00 USD | 0.00 USD |
| `7D` | `101.20` | 21,550,000.00 USD | 21,550,000.00 USD | 0.00 USD | 2,190,000.00 USD | 3,220,000.00 USD | 2,450,000.00 USD |
| `1D` | `101.30` | 24,440,000.00 USD | 24,440,000.00 USD | 0.00 USD | 2,660,000.00 USD | 3,940,000.00 USD | 2,710,000.00 USD |
| `7D` | `101.40` | 32,050,000.00 USD | 32,050,000.00 USD | 0.00 USD | 3,020,000.00 USD | 0.00 USD | 7,490,000.00 USD |
| `1D` | `101.50` | 37,310,000.00 USD | 37,310,000.00 USD | 0.00 USD | 1,360,000.00 USD | 3,350,000.00 USD | 8,160,000.00 USD |
| `7D` | `101.60` | 41,900,000.00 USD | 41,900,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD |
| `1D` | `101.70` | 50,630,000.00 USD | 50,630,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 8,900,000.00 USD |
| `7D` | `101.80` | 51,250,000.00 USD | 51,250,000.00 USD | 0.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD |
| `1D` | `101.90` | 55,160,000.00 USD | 55,160,000.00 USD | 0.00 USD | 1,320,000.00 USD | 142,780.00 USD | 3,070,000.00 USD |
| `7D` | `102.00` | 53,920,000.00 USD | 53,920,000.00 USD | 0.00 USD | 843,730.00 USD | 0.00 USD | 1,830,000.00 USD |
| `1D` | `102.10` | 56,780,000.00 USD | 56,780,000.00 USD | 0.00 USD | 407,760.00 USD | 439,590.00 USD | 768,500.00 USD |
| `7D` | `102.20` | 57,190,000.00 USD | 57,190,000.00 USD | 0.00 USD | 369,280.00 USD | 578,040.00 USD | 2,320,000.00 USD |
| `1D` | `102.30` | 61,090,000.00 USD | 61,090,000.00 USD | 0.00 USD | 799,010.00 USD | 1,170,000.00 USD | 2,350,000.00 USD |
| `7D` | `102.40` | 60,220,000.00 USD | 60,220,000.00 USD | 0.00 USD | 1,150,000.00 USD | 299,640.00 USD | 1,580,000.00 USD |
| `1D` | `102.50` | 62,090,000.00 USD | 62,090,000.00 USD | 0.00 USD | 699,160.00 USD | 292,190.00 USD | 6,570.00 USD |
| `7D` | `102.60` | 62,640,000.00 USD | 62,640,000.00 USD | 0.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD |
| `1D` | `102.70` | 63,550,000.00 USD | 63,550,000.00 USD | 0.00 USD | 931,170.00 USD | 524,710.00 USD | 3,170.00 USD |
| `7D` | `102.80` | 70,520,000.00 USD | 70,520,000.00 USD | 0.00 USD | 7,600,000.00 USD | 0.00 USD | 277,920.00 USD |
| `1D` | `102.90` | 67,490,000.00 USD | 67,490,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,770,000.00 USD | 792,760.00 USD |
| `7D` | `103.00` | 85,040,000.00 USD | 85,040,000.00 USD | 0.00 USD | 11,690,000.00 USD | 0.00 USD | 2,830,000.00 USD |
| `1D` | `103.10` | 73,660,000.00 USD | 73,660,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,800,000.00 USD | 1,590,000.00 USD |
| `7D` | `103.20` | 99,330,000.00 USD | 99,330,000.00 USD | 0.00 USD | 13,650,000.00 USD | 4,380.00 USD | 631,060.00 USD |
| `1D` | `103.30` | 78,790,000.00 USD | 78,790,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,920,000.00 USD | 815,560.00 USD |
| `7D` | `103.40` | 114,330,000.00 USD | 114,330,000.00 USD | 0.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD |
| `1D` | `103.50` | 91,300,000.00 USD | 91,300,000.00 USD | 0.00 USD | 4,290,000.00 USD | 2,690,000.00 USD | 5,530,000.00 USD |
| `7D` | `103.60` | 132,720,000.00 USD | 132,720,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.70` | 103,220,000.00 USD | 103,220,000.00 USD | 0.00 USD | 4,210,000.00 USD | 2,380,000.00 USD | 5,340,000.00 USD |
| `7D` | `103.80` | 145,070,000.00 USD | 145,070,000.00 USD | 0.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `103.90` | 112,870,000.00 USD | 112,870,000.00 USD | 0.00 USD | 2,770,000.00 USD | 3,080,000.00 USD | 3,810,000.00 USD |
| `7D` | `104.00` | 173,480,000.00 USD | 173,480,000.00 USD | 0.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD |
| `1D` | `104.10` | 123,550,000.00 USD | 123,550,000.00 USD | 0.00 USD | 4,520,000.00 USD | 2,760,000.00 USD | 3,390,000.00 USD |
| `7D` | `104.20` | 193,570,000.00 USD | 193,570,000.00 USD | 0.00 USD | 7,510,000.00 USD | 6,900,000.00 USD | 5,680,000.00 USD |
| `1D` | `104.30` | 132,020,000.00 USD | 132,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 2,140,000.00 USD | 3,320,000.00 USD |
| `7D` | `104.40` | 209,710,000.00 USD | 209,710,000.00 USD | 0.00 USD | 4,800,000.00 USD | 3,700,000.00 USD | 7,640,000.00 USD |
| `1D` | `104.50` | 139,030,000.00 USD | 139,030,000.00 USD | 0.00 USD | 2,440,000.00 USD | 2,120,000.00 USD | 2,440,000.00 USD |
| `7D` | `104.60` | 227,270,000.00 USD | 227,270,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD |
| `1D` | `104.70` | 148,900,000.00 USD | 148,900,000.00 USD | 0.00 USD | 2,650,000.00 USD | 2,140,000.00 USD | 5,080,000.00 USD |
| `7D` | `104.80` | 244,400,000.00 USD | 244,400,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD |
| `1D` | `104.90` | 151,870,000.00 USD | 151,870,000.00 USD | 0.00 USD | 1,020,000.00 USD | 592,030.00 USD | 1,360,000.00 USD |
| `7D` | `105.00` | 261,520,000.00 USD | 261,520,000.00 USD | 0.00 USD | 5,730,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.10` | 154,310,000.00 USD | 154,310,000.00 USD | 0.00 USD | 421,810.00 USD | 622,250.00 USD | 1,400,000.00 USD |
| `7D` | `105.20` | 274,240,000.00 USD | 274,240,000.00 USD | 0.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.30` | 155,250,000.00 USD | 155,250,000.00 USD | 0.00 USD | 506,770.00 USD | 2,430.00 USD | 425,580.00 USD |
| `7D` | `105.40` | 286,880,000.00 USD | 286,880,000.00 USD | 0.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 5,240,000.00 USD |
| `1D` | `105.50` | 156,300,000.00 USD | 156,300,000.00 USD | 0.00 USD | 157,550.00 USD | 209,490.00 USD | 684,590.00 USD |
| `7D` | `105.60` | 304,360,000.00 USD | 304,360,000.00 USD | 0.00 USD | 5,650,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD |
| `1D` | `105.70` | 157,630,000.00 USD | 157,630,000.00 USD | 0.00 USD | 294,800.00 USD | 506,510.00 USD | 529,580.00 USD |
| `7D` | `105.80` | 315,150,000.00 USD | 315,150,000.00 USD | 0.00 USD | 3,560,000.00 USD | 3,030,000.00 USD | 4,200,000.00 USD |
| `1D` | `105.90` | 158,650,000.00 USD | 158,650,000.00 USD | 0.00 USD | 223,920.00 USD | 666,590.00 USD | 135,010.00 USD |
| `7D` | `106.00` | 326,160,000.00 USD | 326,160,000.00 USD | 0.00 USD | 4,420,000.00 USD | 3,040,000.00 USD | 3,550,000.00 USD |
| `1D` | `106.10` | 161,050,000.00 USD | 161,050,000.00 USD | 0.00 USD | 1,180,000.00 USD | 721,660.00 USD | 495,870.00 USD |
| `7D` | `106.20` | 340,510,000.00 USD | 340,510,000.00 USD | 0.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,830,000.00 USD |
| `1D` | `106.30` | 162,990,000.00 USD | 162,990,000.00 USD | 0.00 USD | 598,770.00 USD | 621,450.00 USD | 711,540.00 USD |
| `7D` | `106.40` | 349,020,000.00 USD | 349,020,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 2,250,000.00 USD |
| `1D` | `106.50` | 164,810,000.00 USD | 164,810,000.00 USD | 0.00 USD | 1,150,000.00 USD | 336,210.00 USD | 333,130.00 USD |
| `7D` | `106.60` | 358,220,000.00 USD | 358,220,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD |
| `1D` | `106.70` | 167,900,000.00 USD | 167,900,000.00 USD | 0.00 USD | 890,450.00 USD | 383,670.00 USD | 1,820,000.00 USD |
| `7D` | `106.80` | 364,110,000.00 USD | 364,110,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD |
| `1D` | `106.90` | 168,960,000.00 USD | 168,960,000.00 USD | 0.00 USD | 317,210.00 USD | 150,690.00 USD | 594,370.00 USD |
| `7D` | `107.00` | 369,670,000.00 USD | 369,670,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD |
| `1D` | `107.10` | 169,810,000.00 USD | 169,810,000.00 USD | 0.00 USD | 88,570.00 USD | 254,230.00 USD | 510,390.00 USD |
| `7D` | `107.20` | 371,390,000.00 USD | 371,390,000.00 USD | 0.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD |
| `1D` | `107.30` | 170,280,000.00 USD | 170,280,000.00 USD | 0.00 USD | 252,090.00 USD | 0.00 USD | 212,790.00 USD |
| `7D` | `107.40` | 372,370,000.00 USD | 372,370,000.00 USD | 0.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD |
| `1D` | `107.50` | 170,570,000.00 USD | 170,570,000.00 USD | 0.00 USD | 0.00 USD | 6,440.00 USD | 288,380.00 USD |
| `7D` | `107.60` | 372,740,000.00 USD | 372,740,000.00 USD | 0.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD |
| `1D` | `107.70` | 171,100,000.00 USD | 171,100,000.00 USD | 0.00 USD | 94,360.00 USD | 181,310.00 USD | 249,940.00 USD |
| `7D` | `107.80` | 373,530,000.00 USD | 373,530,000.00 USD | 0.00 USD | 499,750.00 USD | 14,850.00 USD | 277,390.00 USD |
| `1D` | `107.90` | 171,230,000.00 USD | 171,230,000.00 USD | 0.00 USD | 0.00 USD | 128,660.00 USD | 0.00 USD |
| `7D` | `108.00` | 373,870,000.00 USD | 373,870,000.00 USD | 0.00 USD | 130,170.00 USD | 200,240.00 USD | 5,560.00 USD |
| `7D` | `108.20` | 376,200,000.00 USD | 376,200,000.00 USD | 0.00 USD | 966,370.00 USD | 938,650.00 USD | 427,140.00 USD |
| `7D` | `108.40` | 378,690,000.00 USD | 378,690,000.00 USD | 0.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD |
| `7D` | `108.60` | 380,120,000.00 USD | 380,120,000.00 USD | 0.00 USD | 401,600.00 USD | 515,740.00 USD | 505,810.00 USD |
| `7D` | `108.80` | 382,790,000.00 USD | 382,790,000.00 USD | 0.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD |
| `7D` | `109.00` | 383,330,000.00 USD | 383,330,000.00 USD | 0.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD |
| `1D` | `109.10` | 171,230,000.00 USD | 171,230,000.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `109.20` | 384,560,000.00 USD | 384,560,000.00 USD | 0.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD |
| `1D` | `109.30` | 171,370,000.00 USD | 171,370,000.00 USD | 0.00 USD | 126,020.00 USD | 9,360.00 USD | 2,950.00 USD |
| `7D` | `109.40` | 384,890,000.00 USD | 384,890,000.00 USD | 0.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD |
| `1D` | `109.50` | 171,630,000.00 USD | 171,630,000.00 USD | 0.00 USD | 133,350.00 USD | 84,430.00 USD | 44,310.00 USD |
| `7D` | `109.60` | 385,950,000.00 USD | 385,950,000.00 USD | 0.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD |
| `1D` | `109.70` | 172,540,000.00 USD | 172,540,000.00 USD | 0.00 USD | 456,990.00 USD | 277,760.00 USD | 171,080.00 USD |
| `7D` | `109.80` | 386,940,000.00 USD | 386,940,000.00 USD | 0.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD |
| `1D` | `109.90` | 173,480,000.00 USD | 173,480,000.00 USD | 0.00 USD | 268,320.00 USD | 266,300.00 USD | 405,440.00 USD |
| `7D` | `110.00` | 388,660,000.00 USD | 388,660,000.00 USD | 0.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `1D` | `110.10` | 174,520,000.00 USD | 174,520,000.00 USD | 0.00 USD | 258,510.00 USD | 467,380.00 USD | 313,070.00 USD |
| `7D` | `110.20` | 390,660,000.00 USD | 390,660,000.00 USD | 0.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD |
| `1D` | `110.30` | 175,510,000.00 USD | 175,510,000.00 USD | 0.00 USD | 238,980.00 USD | 341,180.00 USD | 406,900.00 USD |
| `7D` | `110.40` | 392,060,000.00 USD | 392,060,000.00 USD | 0.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `110.50` | 176,000,000.00 USD | 176,000,000.00 USD | 0.00 USD | 263,180.00 USD | 150,770.00 USD | 83,370.00 USD |
| `7D` | `110.60` | 393,160,000.00 USD | 393,160,000.00 USD | 0.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD |
| `1D` | `110.70` | 176,750,000.00 USD | 176,750,000.00 USD | 0.00 USD | 223,030.00 USD | 248,900.00 USD | 276,260.00 USD |
| `7D` | `110.80` | 395,170,000.00 USD | 395,170,000.00 USD | 0.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD |
| `1D` | `110.90` | 177,250,000.00 USD | 177,250,000.00 USD | 0.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD |
| `7D` | `111.00` | 398,150,000.00 USD | 398,150,000.00 USD | 0.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `111.10` | 177,360,000.00 USD | 177,360,000.00 USD | 0.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD |
| `7D` | `111.20` | 400,210,000.00 USD | 400,210,000.00 USD | 0.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `111.30` | 177,540,000.00 USD | 177,540,000.00 USD | 0.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD |
| `7D` | `111.40` | 402,540,000.00 USD | 402,540,000.00 USD | 0.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `111.50` | 177,690,000.00 USD | 177,690,000.00 USD | 0.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD |
| `7D` | `111.60` | 403,500,000.00 USD | 403,500,000.00 USD | 0.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD |
| `1D` | `111.70` | 177,720,000.00 USD | 177,720,000.00 USD | 0.00 USD | 0.00 USD | 27,410.00 USD | 641.98 USD |
| `7D` | `111.80` | 405,870,000.00 USD | 405,870,000.00 USD | 0.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD |
| `1D` | `111.90` | 177,800,000.00 USD | 177,800,000.00 USD | 0.00 USD | 21,670.00 USD | 60,130.00 USD | 1,090.00 USD |
| `7D` | `112.00` | 407,490,000.00 USD | 407,490,000.00 USD | 0.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `112.10` | 178,080,000.00 USD | 178,080,000.00 USD | 0.00 USD | 107,440.00 USD | 112,260.00 USD | 56,750.00 USD |
| `7D` | `112.20` | 409,690,000.00 USD | 409,690,000.00 USD | 0.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `112.30` | 178,720,000.00 USD | 178,720,000.00 USD | 0.00 USD | 326,750.00 USD | 140,660.00 USD | 177,950.00 USD |
| `7D` | `112.40` | 411,430,000.00 USD | 411,430,000.00 USD | 0.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `112.50` | 179,110,000.00 USD | 179,110,000.00 USD | 0.00 USD | 214,080.00 USD | 112,930.00 USD | 62,120.00 USD |
| `1D` | `112.60` | 179,270,000.00 USD | 179,270,000.00 USD | 0.00 USD | 59,050.00 USD | 20,870.00 USD | 76,980.00 USD |
| `7D` | `112.60` | 412,290,000.00 USD | 412,290,000.00 USD | 0.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `7D` | `112.80` | 413,170,000.00 USD | 413,170,000.00 USD | 0.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD |
| `7D` | `113.00` | 414,200,000.00 USD | 414,200,000.00 USD | 0.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD |
| `7D` | `113.20` | 415,280,000.00 USD | 415,280,000.00 USD | 0.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `7D` | `113.40` | 415,510,000.00 USD | 415,510,000.00 USD | 0.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `7D` | `113.60` | 415,900,000.00 USD | 415,900,000.00 USD | 0.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.80` | 415,900,000.00 USD | 415,900,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `6.22B` | Total OI Tokens: `61,894,328.4 SOL`
  * 1h OI Change: `-1.19%` | 4h OI Change: `-3.85%` | 24h OI Change: `-3.03%`
  * Exchange Breakdown: Binance=`1.09B` | Bybit=`612.76M` | OKX=`353.25M` | Hyperliquid=`566.32M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `193.74K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0066%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `41.49%` | `58.51%` | `0.71` | 97,500,000.00 USD |
| `15M` | `Binance` | `38.22%` | `61.78%` | `0.62` | 30,920,000.00 USD |
| `15M` | `OKX` | `42.92%` | `57.08%` | `0.75` | 14,090,000.00 USD |
| `15M` | `Bybit` | `35.65%` | `64.35%` | `0.55` | 11,720,000.00 USD |
| `15M` | `KuCoin` | `63.27%` | `36.73%` | `1.72` | 396,790.00 USD |
| `15M` | `Gate` | `43.62%` | `56.38%` | `0.77` | 7,420,000.00 USD |
| `15M` | `Bitget` | `55.39%` | `44.61%` | `1.24` | 3,290,000.00 USD |
| `15M` | `BingX` | `56.11%` | `43.89%` | `1.28` | 6,610,000.00 USD |
| `15M` | `MEXC` | `36.93%` | `63.07%` | `0.59` | 8,830,000.00 USD |
| `15M` | `Bitunix` | `52.3%` | `47.7%` | `1.10` | 6,290,000.00 USD |
| `15M` | `Hyperliquid` | `47.22%` | `52.78%` | `0.89` | 1,780,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.05%` | `49.95%` | `1.00` | 1,610,000.00 USD |
| `15M` | `Crypto.com` | `39.15%` | `60.85%` | `0.64` | 120,550.00 USD |
| `15M` | `WhiteBIT` | `6.65%` | `93.35%` | `0.07` | 1,910,000.00 USD |
| `15M` | `HTX` | `10.22%` | `89.78%` | `0.11` | 301,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `49.32%` | `50.68%` | `0.97` | 791,510.00 USD |
| `15M` | `Aster` | `39.85%` | `60.15%` | `0.66` | 860,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.5%` | `55.5%` | `0.80` | 580,310.00 USD |
| `15M` | `Whale Positions` | `38.22%` | `61.78%` | `0.62` | 30,920,000.00 USD |
| `15M` | `Global Accounts` | `41.49%` | `58.51%` | `0.71` | 97,500,000.00 USD |
| `1H` | `SOL` | `39.14%` | `60.86%` | `0.64` | 159,340,000.00 USD |
| `1H` | `Binance` | `39.61%` | `60.39%` | `0.66` | 56,200,000.00 USD |
| `1H` | `OKX` | `38.43%` | `61.57%` | `0.62` | 16,990,000.00 USD |
| `1H` | `Bybit` | `33.56%` | `66.44%` | `0.51` | 23,580,000.00 USD |
| `1H` | `KuCoin` | `41.16%` | `58.84%` | `0.70` | 1,880,000.00 USD |
| `1H` | `Gate` | `46.99%` | `53.01%` | `0.89` | 6,060,000.00 USD |
| `1H` | `Bitget` | `37.77%` | `62.23%` | `0.61` | 13,350,000.00 USD |
| `1H` | `BingX` | `32.35%` | `67.65%` | `0.48` | 3,340,000.00 USD |
| `1H` | `MEXC` | `40.1%` | `59.9%` | `0.67` | 16,440,000.00 USD |
| `1H` | `Bitunix` | `41.64%` | `58.36%` | `0.71` | 8,840,000.00 USD |
| `1H` | `Hyperliquid` | `33.24%` | `66.76%` | `0.50` | 2,740,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `72.06%` | `27.94%` | `2.58` | 795,950.00 USD |
| `1H` | `Crypto.com` | `48.9%` | `51.1%` | `0.96` | 190,250.00 USD |
| `1H` | `WhiteBIT` | `45.37%` | `54.63%` | `0.83` | 6,520,000.00 USD |
| `1H` | `HTX` | `51.14%` | `48.86%` | `1.05` | 37,350.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `28.06%` | `71.94%` | `0.39` | 727,610.00 USD |
| `1H` | `Aster` | `54.87%` | `45.13%` | `1.22` | 1,490,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.41%` | `54.59%` | `0.83` | 144,770.00 USD |
| `1H` | `Whale Positions` | `39.61%` | `60.39%` | `0.66` | 56,200,000.00 USD |
| `1H` | `Global Accounts` | `39.14%` | `60.86%` | `0.64` | 159,340,000.00 USD |
| `4H` | `SOL` | `44.42%` | `55.58%` | `0.80` | 622,310,000.00 USD |
| `4H` | `Binance` | `45.49%` | `54.51%` | `0.83` | 204,530,000.00 USD |
| `4H` | `OKX` | `45.36%` | `54.64%` | `0.83` | 64,570,000.00 USD |
| `4H` | `Bybit` | `43.28%` | `56.72%` | `0.76` | 88,220,000.00 USD |
| `4H` | `KuCoin` | `47.48%` | `52.52%` | `0.90` | 6,760,000.00 USD |
| `4H` | `Gate` | `45.56%` | `54.44%` | `0.84` | 25,790,000.00 USD |
| `4H` | `Bitget` | `44.89%` | `55.11%` | `0.81` | 51,530,000.00 USD |
| `4H` | `BingX` | `30.76%` | `69.24%` | `0.44` | 13,740,000.00 USD |
| `4H` | `MEXC` | `47.24%` | `52.76%` | `0.90` | 82,160,000.00 USD |
| `4H` | `Bitunix` | `45.91%` | `54.09%` | `0.85` | 34,270,000.00 USD |
| `4H` | `Hyperliquid` | `45.81%` | `54.19%` | `0.85` | 14,970,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.38%` | `44.62%` | `1.24` | 3,020,000.00 USD |
| `4H` | `Crypto.com` | `48.64%` | `51.36%` | `0.95` | 813,400.00 USD |
| `4H` | `WhiteBIT` | `24.63%` | `75.37%` | `0.33` | 20,870,000.00 USD |
| `4H` | `HTX` | `53.62%` | `46.38%` | `1.16` | 243,860.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.95%` | `48.05%` | `1.08` | 3,640,000.00 USD |
| `4H` | `Aster` | `41.15%` | `58.85%` | `0.70` | 6,490,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.97%` | `55.03%` | `0.82` | 702,470.00 USD |
| `4H` | `Whale Positions` | `45.49%` | `54.51%` | `0.83` | 204,530,000.00 USD |
| `4H` | `Global Accounts` | `44.42%` | `55.58%` | `0.80` | 622,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `102.31` | `102.32` | `102.31` | `102.66` | `102.10` | 27,443,327.62 USD | 11,049,929.69 USD | 16,393,397.93 USD | -5,343,468.24 USD | `-19.47%` | `1B / 16S` |
| `0:00 UTC` | `102.00` | `102.00` | `102.00` | `102.22` | `101.81` | 25,493,228.16 USD | 11,241,280.68 USD | 14,251,947.48 USD | -3,010,666.79 USD | `-11.81%` | `2B / 10S` |
| `5:00 UTC` | `101.94` | `101.88` | `101.94` | `102.02` | `101.75` | 15,546,239.68 USD | 7,009,090.38 USD | 8,537,149.31 USD | -1,528,058.93 USD | `-9.83%` | `0B / 1S` |
| `0:00 UTC` | `101.70` | `101.72` | `101.70` | `101.94` | `101.53` | 20,486,970.74 USD | 7,002,058.55 USD | 13,484,912.18 USD | -6,482,853.63 USD | `-31.64%` | `0B / 15S` |
| `5:00 UTC` | `101.65` | `101.65` | `101.65` | `101.78` | `101.53` | 12,871,901.66 USD | 6,991,731.87 USD | 5,880,169.78 USD | 1,111,562.09 USD | `+8.64%` | `1B / 2S` |
| `0:00 UTC` | `101.00` | `101.32` | `101.00` | `101.77` | `100.97` | 23,345,961.64 USD | 9,081,895.18 USD | 14,264,066.46 USD | -5,182,171.27 USD | `-22.20%` | `6B / 20S` |
| `5:00 UTC` | `100.91` | `100.89` | `100.91` | `101.13` | `100.72` | 21,682,501.47 USD | 10,212,926.11 USD | 11,469,575.36 USD | -1,256,649.25 USD | `-5.80%` | `6B / 4S` |
| `0:00 UTC` | `101.07` | `101.03` | `101.07` | `101.19` | `100.90` | 11,845,890.84 USD | 5,647,320.15 USD | 6,198,570.68 USD | -551,250.53 USD | `-4.65%` | `2B / 1S` |
| `5:00 UTC` | `100.81` | `100.98` | `100.81` | `101.18` | `100.75` | 7,681,327.85 USD | 3,539,960.94 USD | 4,141,366.91 USD | -601,405.98 USD | `-7.83%` | `5B / 12S` |
| `0:00 UTC` | `100.37` | `100.47` | `100.37` | `100.81` | `100.30` | 25,268,354.53 USD | 8,798,908.17 USD | 16,469,446.37 USD | -7,670,538.20 USD | `-30.36%` | `0B / 21S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 18:37` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `101.13` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 500K SOL` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `101.76` | 0.00 USD | 0.00 USD |
| `10-28 15:32` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.87` | 99,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `102.88` | 0.00 USD | 0.00 USD |
| `10-28 13:30` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.22` | 103,000.00 USD | 0.00 USD |
| `10-28 10:59` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `101.76` | 110,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -31,520.00 USD | -344,460.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,270,000.00 USD | -12,750,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,260,000.00 USD | -12,900,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,640,000.00 USD | -18,530,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,820,000.00 USD | -43,300,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 2,700,000.00 USD | -53,810,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 13,670,000.00 USD | -23,110,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 12,400,000.00 USD | -66,260,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 23,080,000.00 USD | -56,450,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 23,610,000.00 USD | -115,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 82,810,000.00 USD | -305,470,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 60,850,000.00 USD | -1,900,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-31.52K` | 15m=`-1.27M` | 1h=`-2.64M` | 24h=`+23.61M`
* Futures Capital Netflows: 5m=`-344.46K` | 15m=`-12.75M` | 1h=`-18.53M` | 24h=`-115.52M`
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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `99.18` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `97.61` (Risk Distance: `1.58` pts)
  * +2.5R Take Profit: `103.12`
  * Mathematical Lot Sizing: **`6.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `101.32` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `102.89` (Risk Distance: `1.58` pts)
  * +2.5R Take Profit: `97.38`
  * Mathematical Lot Sizing: **`6.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`101.18`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
