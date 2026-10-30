# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGUSD
**Canonical Key**: `XAGUSD` | **Broker Instrument**: `XAGUSD.pi` | **Asset Class**: `Precious Metal`
**Timestamp**: `2026-10-30 09:10:06 IST` (`2026-10-30 03:40:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `51.36` | **Live Ask Quote**: `51.40` | **Mid Price**: `51.38`
- **Spread Points**: `36.00` | **Spread BPS**: `7.01 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `5,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `5.00 USD` | Point Value (0.01 Lot): `0.0500 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `51.38` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `51.74` | Lower -3.00σ Band: `51.02`
  * Upper +2.51σ Band: `51.66` | Lower -2.51σ Band: `51.10`
  * Upper +2.01σ Band: `51.60` | Lower -2.01σ Band: `51.17`
  * Upper +2.00σ Band: `51.59` | Lower -2.00σ Band: `51.18`
  * Upper +1.28σ Band: `51.53` | Lower -1.28σ Band: `51.24`
  * Upper +1.00σ Band: `51.48` | Lower -1.00σ Band: `51.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`51.38` | EMA-20=`51.38` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.38` (Slope: `+0.0000`) | EMA-100=`51.38`
  * Institutional Anchors: EMA-144=`51.38` | EMA-200=`51.38` (Slope: `+0.0000`) | EMA-233=`51.38`
- **Range Boundaries**: 24H High=`51.90` | 24H Low=`50.87` | Weekly High=`52.41` | Weekly Low=`50.35`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `51.66` (Distance: `-0.53%`)
  * Point of Control (POC) = `51.39` (Distance: `-0.01%`)
  * Value Area Low (VAL) = `51.09` (Distance: `+0.58%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.53` | Weekly POC=`53.89` | Weekly VAL=`52.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.59` | Low=`51.18`
  * New York Session (13:00-21:00 UTC): High=`51.69` | Low=`51.07`
  * Initial Balance (First Hour): IB High=`51.54` | IB Low=`51.23`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `51.18` - `51.59`
  * Optimal Trade Entry (OTE 0.705): `51.48`
  * Structural Invalidation Anchor (0.786): `51.79`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `51.93` | `51.93` | `51.88` | `51.92` | `482` | 25,027.37 USD | 7,460.08 USD | `+29.81%` | -774,459.01 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `51.92` | `51.97` | `51.90` | `51.93` | `876` | 45,488.05 USD | -1,672.35 USD | `-3.68%` | -776,131.37 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `51.93` | `51.93` | `51.85` | `51.87` | `806` | 41,810.44 USD | -20,650.28 USD | `-49.39%` | -796,781.65 USD | `-1.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.95` | `52.00` | `51.88` | `51.88` | `1,419` | 73,623.40 USD | -56,633.38 USD | `-76.92%` | -1,938,619.22 USD | `-0.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.88` | `51.94` | `51.85` | `51.92` | `1,567` | 81,364.91 USD | 40,682.45 USD | `+50.00%` | -1,897,936.77 USD | `+0.66` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.92` | `51.97` | `51.85` | `51.93` | `2,736` | 142,083.22 USD | 34,316.71 USD | `+24.15%` | -1,863,620.06 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.14` | `52.22` | `51.93` | `51.97` | `4,907` | 254,992.26 USD | -178,406.04 USD | `-69.97%` | -1,415,413.12 USD | `-0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.96` | `52.01` | `51.81` | `51.92` | `6,169` | 320,319.16 USD | -7,812.66 USD | `-2.44%` | -1,423,225.78 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `51.92` | `52.06` | `51.73` | `51.78` | `13,804` | 714,757.32 USD | -415,480.10 USD | `-58.13%` | -1,838,705.88 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -3,942,615.79 USD | `+1.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -4,935,926.70 USD | `-0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -5,937,029.72 USD | `-0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -2,449,348.22 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -4,489,396.06 USD | `-1.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -3,942,615.79 USD | `+1.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -4,935,926.70 USD | `-0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -5,937,029.72 USD | `-0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `51.39` | `143.1300` | 7,356.02 USD | 553,061.69 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.39` | `8004.2600` | 411,338.92 USD | 964,400.61 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `51.39` | `5990.9000` | 307,866.36 USD | 1,272,266.98 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `51.39` | `56.0400` | 2,879.78 USD | 1,275,146.76 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `51.40` | `176.2000` | 9,057.38 USD | 121,916.70 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `25.4200` | 1,306.66 USD | 123,223.37 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `3944.7800` | 202,769.58 USD | 325,992.95 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `31.4700` | 1,617.59 USD | 327,610.54 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `75.3600` | 3,873.50 USD | 331,484.04 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.40` | `313.5400` | 16,115.64 USD | 347,599.68 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `51.40` | `161.5700` | 8,304.21 USD | 355,903.90 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.40` | `3634.7700` | 186,812.64 USD | 542,716.54 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.40` | `58.1600` | 2,989.13 USD | 545,705.67 USD | `2 orders` | `-0.04%` | `-` |
| `ASK` | `51.41` | `0.2000` | 10.28 USD | 2,139.85 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `51.41` | `41.4200` | 2,129.57 USD | 2,129.57 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `51.41` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 51.41` | `0.00%` | `-` |
| `BID` | `51.41` | `54.0900` | 2,780.93 USD | 2,780.93 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.41` | `127.8400` | 6,572.51 USD | 9,353.44 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.41` | `73.1000` | 3,758.14 USD | 13,111.58 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `51.41` | `90.2600` | 4,640.18 USD | 17,751.76 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.41` | `90.2700` | 4,640.60 USD | 22,392.36 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.41` | `163.5800` | 8,409.16 USD | 30,801.52 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `51.41` | `1596.3000` | 82,057.80 USD | 112,859.32 USD | `2 orders` | `-0.02%` | `-` |
| `ASK` | `51.42` | `3124.6600` | 160,685.64 USD | 570,047.05 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `5582.6600` | 287,082.71 USD | 409,361.41 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `25.3400` | 1,303.06 USD | 122,278.71 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `113.6400` | 5,843.48 USD | 120,975.65 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.42` | `115.6000` | 5,944.15 USD | 115,132.16 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.42` | `1836.5400` | 94,433.05 USD | 109,188.01 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.42` | `85.2700` | 4,384.41 USD | 14,754.96 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.42` | `25.4400` | 1,308.05 USD | 10,370.55 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.42` | `134.6400` | 6,922.65 USD | 9,062.50 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `51.43` | `770.8500` | 39,647.90 USD | 1,284,481.95 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `51.43` | `5832.8300` | 299,999.95 USD | 1,244,834.05 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.43` | `779.2100` | 40,076.33 USD | 944,834.10 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.43` | `5562.8400` | 286,102.42 USD | 904,757.77 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `51.43` | `476.2500` | 24,493.54 USD | 618,655.35 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `51.43` | `296.6000` | 15,253.54 USD | 594,161.81 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `51.43` | `172.3100` | 8,861.21 USD | 578,908.27 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `51.44` | `263.2800` | 13,542.33 USD | 1,300,945.33 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `51.44` | `56.7900` | 2,921.05 USD | 1,287,403.00 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:07:15 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `113` | `0x5b5d...c060` | `SHORT` | 17,787,153.81 USD | `346,127.65` | `58.90` | `51.39` | `542.14` | 2,599,206.28 USD | `+14.61%` | `5X Cross` |
| `121` | `0x4692...164f` | `SHORT` | 15,946,271.35 USD | `310,305.15` | `52.93` | `51.39` | `254.62` | 478,315.92 USD | `+3.00%` | `5X Cross` |
| `203` | `0xacb6...efbd` | `SHORT` | 10,336,442.96 USD | `201,133.33` | `59.63` | `51.39` | `76.90` | 1,656,214.15 USD | `+16.02%` | `6X Cross` |
| `238` | `0xc26c...b8f4` | `LONG` | 9,325,041.71 USD | `181,463.41` | `55.43` | `51.39` | `0.000000` | -733,713.37 USD | `-7.87%` | `2X Cross` |
| `281` | `0x49e9...e1d0` | `SHORT` | 8,216,464.39 USD | `159,887.61` | `55.44` | `51.39` | `101.87` | 647,291.32 USD | `+7.88%` | `4X Cross` |
| `347` | `0x645b...87b8` | `LONG` | 6,575,542.19 USD | `127,956.22` | `56.57` | `51.39` | `0.000000` | -662,900.38 USD | `-10.08%` | `3X Cross` |
| `352` | `0xd8c5...99b0` | `SHORT` | 6,491,460.54 USD | `126,320.04` | `61.98` | `51.39` | `199.66` | 1,337,877.31 USD | `+20.61%` | `3X Cross` |
| `386` | `0xe9ff...5903` | `SHORT` | 5,806,981.55 USD | `112,996.08` | `60.07` | `51.39` | `178.79` | 980,969.26 USD | `+16.89%` | `5X Cross` |
| `609` | `0x9aa5...58af` | `LONG` | 3,661,271.11 USD | `71,243.43` | `61.59` | `51.39` | `0.000000` | -726,886.41 USD | `-19.85%` | `20X Cross` |
| `736` | `0x2056...8396` | `LONG` | 3,083,460.00 USD | `60,000.00` | `66.92` | `51.39` | `21.35` | -931,867.14 USD | `-30.22%` | `10X Cross` |
| `858` | `0x354b...6425` | `SHORT` | 2,666,178.49 USD | `51,882.28` | `51.40` | `51.39` | `258.15` | 442.28 USD | `+0.02%` | `10X Cross` |
| `888` | `0x0242...ffa1` | `SHORT` | 2,565,167.75 USD | `49,916.67` | `56.48` | `51.39` | `336.71` | 253,964.11 USD | `+9.90%` | `10X Cross` |
| `893` | `0x960b...f0fc` | `LONG` | 2,541,595.11 USD | `49,457.96` | `55.82` | `51.39` | `0.000000` | -219,341.92 USD | `-8.63%` | `25X Cross` |
| `975` | `0x8b9d...7b28` | `LONG` | 2,303,164.36 USD | `44,823.47` | `58.35` | `51.39` | `0.000000` | -312,284.19 USD | `-13.56%` | `10X Cross` |
| `1047` | `0x5647...e7de` | `LONG` | 2,069,027.52 USD | `40,262.07` | `57.38` | `51.39` | `0.000000` | -241,210.08 USD | `-11.66%` | `20X Cross` |
| `1054` | `0xa2ce...3126` | `LONG` | 2,055,320.00 USD | `40,000.00` | `74.30` | `51.39` | `0.000000` | -916,735.49 USD | `-44.60%` | `20X Cross` |
| `1089` | `0xb078...de15` | `SHORT` | 2,004,132.51 USD | `39,000.01` | `52.58` | `51.39` | `201.73` | 46,386.44 USD | `+2.31%` | `8X Cross` |
| `1406` | `0x5a88...d997` | `LONG` | 1,541,670.00 USD | `30,000.00` | `59.50` | `51.39` | `38.87` | -243,217.59 USD | `-15.78%` | `25X Cross` |
| `1407` | `0x3678...b209` | `LONG` | 1,541,640.00 USD | `30,000.00` | `57.15` | `51.39` | `0.000000` | -172,860.00 USD | `-11.21%` | `20X Cross` |
| `1579` | `0xce97...7e78` | `LONG` | 1,345,331.07 USD | `26,178.34` | `51.58` | `51.39` | `0.000000` | -5,036.03 USD | `-0.37%` | `5X Cross` |
| `1643` | `0x7ea9...fc7f` | `LONG` | 1,284,575.00 USD | `25,000.00` | `53.60` | `51.39` | `34.41` | -55,429.05 USD | `-4.31%` | `25X Cross` |
| `1747` | `0x24fb...ed0f` | `LONG` | 1,187,461.13 USD | `23,110.00` | `51.37` | `51.39` | `0.000000` | 283.80 USD | `+0.02%` | `20X Cross` |
| `1784` | `0xf517...c032` | `LONG` | 1,162,849.85 USD | `22,627.50` | `66.29` | `51.39` | `0.000000` | -337,145.25 USD | `-28.99%` | `20X Cross` |
| `1906` | `0xcc9f...d218` | `LONG` | 1,054,574.15 USD | `20,520.60` | `52.63` | `51.39` | `26.86` | -25,333.90 USD | `-2.40%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.36` (Vol: 4,300,000.00 USD, Dist: `+3.53%`) | Long MP=`51.16` (Vol: 1,800,000.00 USD, Dist: `--0.75%`)
  * 48H Horizon: Short MP=`54.84` (Vol: 4,200,000.00 USD, Dist: `+6.41%`) | Long MP=`51.17` (Vol: 2,500,000.00 USD, Dist: `--0.72%`)
  * 3D Horizon: Short MP=`55.09` (Vol: 5,200,000.00 USD, Dist: `+6.89%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.72%`)
  * 7D Horizon: Short MP=`55.09` (Vol: 8,900,000.00 USD, Dist: `+6.89%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.72%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.94K` | Last 24h: `229.04K` | Last 3d: `461.48K` | Last 7d: `657.16K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BEARISH (BELOW PIVOT)`** | SILVER (XAGUSD.pi) Metal Auction: ROTATI | `53.72` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 08:34:50 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:50 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:02:50 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:02:50 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:01:50 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:03:50 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:03:50 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:03:50 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.09` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `49.83` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `54.22`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `51.66` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.92` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `48.53`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`51.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
