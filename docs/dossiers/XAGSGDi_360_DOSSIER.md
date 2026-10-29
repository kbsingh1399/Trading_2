# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 00:17:13 IST` (`2026-10-29 18:47:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `66.62` | **Live Ask Quote**: `66.63` | **Mid Price**: `66.62`
- **Spread Points**: `10.00` | **Spread BPS**: `1.50 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `66.62` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `67.09` | Lower -3.00σ Band: `66.16`
  * Upper +2.51σ Band: `66.99` | Lower -2.51σ Band: `66.26`
  * Upper +2.01σ Band: `66.90` | Lower -2.01σ Band: `66.34`
  * Upper +2.00σ Band: `66.89` | Lower -2.00σ Band: `66.36`
  * Upper +1.28σ Band: `66.81` | Lower -1.28σ Band: `66.44`
  * Upper +1.00σ Band: `66.76` | Lower -1.00σ Band: `66.49`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`66.62` | EMA-20=`66.62` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`66.62` (Slope: `+0.0000`) | EMA-100=`66.62`
  * Institutional Anchors: EMA-144=`66.62` | EMA-200=`66.62` (Slope: `+0.0000`) | EMA-233=`66.62`
- **Range Boundaries**: 24H High=`67.29` | 24H Low=`65.96` | Weekly High=`67.96` | Weekly Low=`65.29`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.97` (Distance: `-1.80%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.83%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.36` - `66.89`
  * Optimal Trade Entry (OTE 0.705): `66.76`
  * Structural Invalidation Anchor (0.786): `67.16`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.42` | `52.47` | `52.39` | `52.45` | `1,835` | 96,245.75 USD | 37,810.83 USD | `+39.29%` | -558,220.43 USD | `+0.36` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.45` | `52.59` | `52.45` | `52.54` | `1,968` | 103,398.72 USD | 48,032.74 USD | `+46.45%` | -510,187.69 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.54` | `52.55` | `52.39` | `52.43` | `1,406` | 73,716.58 USD | -44,690.68 USD | `-60.63%` | -554,878.37 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.61` | `52.62` | `52.38` | `52.46` | `5,790` | 303,726.03 USD | -150,581.47 USD | `-49.58%` | -1,352,022.35 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.46` | `52.51` | `52.38` | `52.45` | `4,685` | 245,728.25 USD | -3,839.50 USD | `-1.56%` | -1,355,861.85 USD | `+0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `52.45` | `52.59` | `52.39` | `52.47` | `4,569` | 239,726.29 USD | -13,580.55 USD | `-5.67%` | -1,369,442.41 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `52.37` | `52.61` | `51.98` | `52.24` | `41,435` | 2,164,605.83 USD | -391,069.83 USD | `-18.07%` | -1,511,737.72 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.24` | `52.76` | `52.03` | `52.61` | `32,755` | 1,723,273.30 USD | 951,587.73 USD | `+55.22%` | -560,149.99 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.61` | `52.65` | `52.32` | `52.51` | `20,260` | 1,063,771.56 USD | -103,422.23 USD | `-9.72%` | -663,572.22 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -2,786,118.52 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -4,826,166.37 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,279,386.10 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `53.52` | `54.09` | `53.37` | `53.37` | `22,849` | 1,219,382.58 USD | -735,688.52 USD | `-60.33%` | -336,770.30 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,495,594.11 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -2,786,118.52 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -4,826,166.37 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,279,386.10 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `52.02` | `396.6000` | 20,633.12 USD | 271,065.35 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.02` | `473.2500` | 24,620.36 USD | 295,685.71 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `52.02` | `3302.4500` | 171,803.36 USD | 467,489.06 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.02` | `52.1800` | 2,714.51 USD | 470,203.57 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.02` | `3385.9800` | 176,142.07 USD | 646,345.64 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `52.02` | `5683.7100` | 295,666.59 USD | 942,012.23 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.02` | `0.2000` | 10.40 USD | 942,022.63 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.02` | `226.4000` | 11,776.88 USD | 953,799.51 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.02` | `1819.7600` | 94,658.46 USD | 1,048,457.97 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.02` | `5951.3200` | 309,563.86 USD | 1,358,021.83 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.02` | `617.2700` | 32,107.30 USD | 1,390,129.13 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.03` | `58.1900` | 3,027.92 USD | 66,888.91 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `52.03` | `233.4100` | 12,145.02 USD | 79,033.93 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `52.03` | `1615.0600` | 84,033.19 USD | 163,067.12 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.03` | `168.7300` | 8,778.85 USD | 171,845.97 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.03` | `46.9500` | 2,442.71 USD | 174,288.69 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.03` | `373.5300` | 19,433.65 USD | 193,722.33 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.03` | `1090.0300` | 56,709.90 USD | 250,432.23 USD | `3 orders` | `-0.02%` | `-` |
| `ASK` | `52.04` | `1864.3200` | 97,026.67 USD | 122,282.74 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.04` | `44.9800` | 2,340.89 USD | 25,256.07 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.04` | `153.0900` | 7,967.11 USD | 22,915.17 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.04` | `98.6600` | 5,134.37 USD | 14,948.06 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.04` | `184.4600` | 9,599.30 USD | 9,813.70 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.04` | `4.1200` | 214.40 USD | 214.40 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.04` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.04` | `0.00%` | `-` |
| `BID` | `52.04` | `333.2200` | 17,339.77 USD | 17,339.77 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `52.04` | `894.0200` | 46,521.22 USD | 63,860.99 USD | `7 orders` | `-0.00%` | `-` |
| `ASK` | `52.05` | `557.2700` | 29,008.69 USD | 556,542.15 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.05` | `67.0300` | 3,489.18 USD | 527,533.46 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.05` | `187.3800` | 9,753.69 USD | 524,044.29 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `52.05` | `1888.9500` | 98,323.63 USD | 514,290.59 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.05` | `3326.0700` | 173,125.27 USD | 415,966.97 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.05` | `169.6000` | 8,827.51 USD | 242,841.70 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.05` | `740.1500` | 38,523.33 USD | 234,014.19 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.05` | `535.7200` | 27,882.62 USD | 195,490.86 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.05` | `34.5300` | 1,797.15 USD | 167,608.24 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.05` | `836.3600` | 43,528.36 USD | 165,811.09 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.06` | `619.3000` | 32,240.76 USD | 1,238,654.13 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `52.06` | `1037.1000` | 53,990.39 USD | 1,206,413.37 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `52.06` | `5683.7100` | 295,876.89 USD | 1,152,422.98 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.06` | `5763.1000` | 300,003.93 USD | 856,546.09 USD | `1 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,380,794.71 USD | `333,790.30` | `59.15` | `52.07` | `537.17` | 2,362,239.24 USD | `+13.59%` | `5X Cross` |
| `125` | `0x4692...164f` | `SHORT` | 16,262,448.66 USD | `312,312.97` | `53.39` | `52.07` | `240.69` | 411,909.20 USD | `+2.53%` | `5X Cross` |
| `178` | `0x49e9...e1d0` | `SHORT` | 11,729,766.53 USD | `225,264.86` | `55.61` | `52.07` | `86.99` | 796,237.37 USD | `+6.79%` | `4X Cross` |
| `209` | `0xacb6...efbd` | `SHORT` | 10,473,213.63 USD | `201,133.33` | `59.63` | `52.07` | `76.59` | 1,519,443.49 USD | `+14.51%` | `6X Cross` |
| `250` | `0xc26c...b8f4` | `LONG` | 9,448,981.22 USD | `181,463.41` | `55.43` | `52.07` | `0.000000` | -609,773.86 USD | `-6.45%` | `2X Cross` |
| `369` | `0xd8c5...99b0` | `SHORT` | 6,577,610.80 USD | `126,320.04` | `61.98` | `52.07` | `195.32` | 1,251,727.04 USD | `+19.03%` | `3X Cross` |
| `371` | `0x645b...87b8` | `LONG` | 6,575,684.18 USD | `126,283.04` | `56.64` | `52.07` | `0.000000` | -576,396.56 USD | `-8.77%` | `3X Cross` |
| `403` | `0xe9ff...5903` | `SHORT` | 5,884,270.87 USD | `112,996.08` | `60.07` | `52.07` | `197.04` | 903,679.94 USD | `+15.36%` | `5X Cross` |
| `427` | `0xfc66...ca06` | `SHORT` | 5,510,198.00 USD | `105,820.86` | `54.61` | `52.07` | `448.84` | 268,269.26 USD | `+4.87%` | `3X Cross` |
| `548` | `0x354b...6425` | `LONG` | 4,162,697.89 USD | `79,942.73` | `52.44` | `52.07` | `0.000000` | -29,315.41 USD | `-0.70%` | `10X Cross` |
| `583` | `0x4e23...20c3` | `SHORT` | 3,970,843.86 USD | `76,258.26` | `52.44` | `52.07` | `220.18` | 28,368.07 USD | `+0.71%` | `16X Cross` |
| `629` | `0x9aa5...58af` | `LONG` | 3,709,716.64 USD | `71,243.43` | `61.59` | `52.07` | `0.000000` | -678,440.88 USD | `-18.29%` | `20X Cross` |
| `751` | `0x2056...8396` | `LONG` | 3,124,260.00 USD | `60,000.00` | `66.92` | `52.07` | `21.34` | -891,067.14 USD | `-28.52%` | `10X Cross` |
| `877` | `0x0242...ffa1` | `SHORT` | 2,599,210.92 USD | `49,916.67` | `56.48` | `52.07` | `284.59` | 219,920.94 USD | `+8.46%` | `10X Cross` |
| `888` | `0x960b...f0fc` | `LONG` | 2,575,325.44 USD | `49,457.96` | `55.82` | `52.07` | `0.000000` | -185,611.59 USD | `-7.21%` | `25X Cross` |
| `976` | `0x8b9d...7b28` | `LONG` | 2,334,182.20 USD | `44,823.47` | `58.35` | `52.07` | `0.000000` | -281,266.34 USD | `-12.05%` | `10X Cross` |
| `1065` | `0x5647...e7de` | `LONG` | 2,096,123.89 USD | `40,262.07` | `57.38` | `52.07` | `0.000000` | -214,113.71 USD | `-10.21%` | `20X Cross` |
| `1075` | `0xa2ce...3126` | `LONG` | 2,083,000.00 USD | `40,000.00` | `74.30` | `52.07` | `0.000000` | -889,055.49 USD | `-42.68%` | `20X Cross` |
| `1447` | `0x5a88...d997` | `LONG` | 1,562,250.00 USD | `30,000.00` | `59.50` | `52.07` | `37.51` | -222,637.59 USD | `-14.25%` | `25X Cross` |
| `1448` | `0x3678...b209` | `LONG` | 1,562,130.00 USD | `30,000.00` | `57.15` | `52.07` | `0.000000` | -152,370.00 USD | `-9.75%` | `20X Cross` |
| `1675` | `0x7ea9...fc7f` | `LONG` | 1,301,875.00 USD | `25,000.00` | `53.60` | `52.07` | `18.30` | -38,129.05 USD | `-2.93%` | `25X Cross` |
| `1721` | `0xce97...7e78` | `LONG` | 1,267,379.50 USD | `24,339.45` | `52.28` | `52.07` | `0.000000` | -5,078.35 USD | `-0.40%` | `5X Cross` |
| `1796` | `0xf517...c032` | `LONG` | 1,178,236.55 USD | `22,627.50` | `66.29` | `52.07` | `0.000000` | -321,758.55 USD | `-27.31%` | `20X Cross` |
| `1917` | `0xcc9f...d218` | `LONG` | 1,068,528.16 USD | `20,520.60` | `52.63` | `52.07` | `26.86` | -11,379.89 USD | `-1.07%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `81.27` | 429.11 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.43K USD at 81.2710 USD [API] | `2026-02-01 23:01:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.30` (Vol: 3,200,000.00 USD, Dist: `+2.19%`) | Long MP=`51.92` (Vol: 3,200,000.00 USD, Dist: `--0.46%`)
  * 48H Horizon: Short MP=`55.09` (Vol: 4,300,000.00 USD, Dist: `+5.63%`) | Long MP=`51.92` (Vol: 3,500,000.00 USD, Dist: `--0.46%`)
  * 3D Horizon: Short MP=`55.09` (Vol: 4,700,000.00 USD, Dist: `+5.63%`) | Long MP=`51.92` (Vol: 4,500,000.00 USD, Dist: `--0.46%`)
  * 7D Horizon: Short MP=`55.09` (Vol: 9,300,000.00 USD, Dist: `+5.61%`) | Long MP=`51.92` (Vol: 5,400,000.00 USD, Dist: `--0.46%`)
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
  * Current Rate: `60.41K` | Last 24h: `163.44K` | Last 3d: `421.23K` | Last 7d: `760.43K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0105%` | **USDT BingX** | `-` |
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
  * Execution Entry: `51.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.77` (Risk Distance: `1.22` pts)
  * +2.5R Take Profit: `55.02`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.97` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `54.19` (Risk Distance: `1.22` pts)
  * +2.5R Take Profit: `49.93`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.16`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
