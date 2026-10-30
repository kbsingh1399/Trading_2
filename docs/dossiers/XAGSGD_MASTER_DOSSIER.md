# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 09:34:19 IST` (`2026-10-30 04:04:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `65.45` | **Live Ask Quote**: `65.49` | **Mid Price**: `65.47`
- **Spread Points**: `31.00` | **Spread BPS**: `4.73 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `51.47` | VWAP Z-Score: `-1.03` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2495` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `38.50` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.09` | Lower -3.00σ Band: `50.86`
  * Upper +2.51σ Band: `51.99` | Lower -2.51σ Band: `50.96`
  * Upper +2.01σ Band: `51.88` | Lower -2.01σ Band: `51.06`
  * Upper +2.00σ Band: `51.88` | Lower -2.00σ Band: `51.06`
  * Upper +1.28σ Band: `51.73` | Lower -1.28σ Band: `51.21`
  * Upper +1.00σ Band: `51.68` | Lower -1.00σ Band: `51.27`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`51.41` | EMA-20=`51.57` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.92` (Slope: `+0.0000`) | EMA-100=`52.34`
  * Institutional Anchors: EMA-144=`52.60` | EMA-200=`52.84` (Slope: `-0.3479`) | EMA-233=`52.99`
- **Range Boundaries**: 24H High=`53.64` | 24H Low=`51.08` | Weekly High=`54.61` | Weekly Low=`51.08`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `51.64` (Distance: `-0.77%`)
  * Point of Control (POC) = `51.39` (Distance: `-0.29%`)
  * Value Area Low (VAL) = `51.11` (Distance: `+0.26%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.53` | Weekly POC=`53.89` | Weekly VAL=`52.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`65.73` | Low=`65.21`
  * New York Session (13:00-21:00 UTC): High=`65.86` | Low=`65.08`
  * Initial Balance (First Hour): IB High=`65.67` | IB Low=`65.27`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `65.21` - `65.73`
  * Optimal Trade Entry (OTE 0.705): `65.60`
  * Structural Invalidation Anchor (0.786): `65.99`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `51.91` | `52.02` | `51.86` | `52.01` | `1,148` | 59,702.89 USD | 40,461.29 USD | `+67.77%` | -627,732.45 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.01` | `52.06` | `51.98` | `51.98` | `1,459` | 75,846.12 USD | -42,189.40 USD | `-55.63%` | -669,921.85 USD | `-2.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.98` | `51.99` | `51.89` | `51.91` | `1,735` | 90,070.79 USD | -58,362.20 USD | `-64.80%` | -728,284.05 USD | `-2.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.93` | `52.02` | `51.84` | `51.92` | `2,905` | 150,836.32 USD | -5,931.77 USD | `-3.93%` | -1,639,706.22 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `51.92` | `52.02` | `51.85` | `52.01` | `3,369` | 175,208.21 USD | 113,885.34 USD | `+65.00%` | -1,525,820.88 USD | `+1.72` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.01` | `52.06` | `51.73` | `51.78` | `4,794` | 248,228.53 USD | -175,511.27 USD | `-70.71%` | -1,701,332.15 USD | `-2.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `BID` | `51.24` | `8695.4700` | 445,599.36 USD | 921,615.49 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `51.24` | `411.1500` | 21,068.97 USD | 942,684.46 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.24` | `79.6300` | 4,080.48 USD | 946,764.94 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.25` | `280.4100` | 14,372.13 USD | 99,245.68 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `51.25` | `893.5300` | 45,796.09 USD | 145,041.78 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `51.25` | `409.5800` | 20,991.79 USD | 166,033.57 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.25` | `1945.3000` | 99,698.57 USD | 265,732.14 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.25` | `3900.7600` | 199,913.95 USD | 465,646.09 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.25` | `88.9600` | 4,559.11 USD | 470,205.20 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.25` | `69.5300` | 3,563.27 USD | 473,768.48 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.25` | `43.8600` | 2,247.65 USD | 476,016.13 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.26` | `221.7200` | 11,366.25 USD | 13,266.13 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `51.26` | `16.7400` | 858.14 USD | 14,124.28 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.26` | `221.9700` | 11,378.63 USD | 25,502.90 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.26` | `180.1900` | 9,236.72 USD | 34,739.62 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `51.26` | `104.4800` | 5,355.64 USD | 40,095.27 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.26` | `88.9500` | 4,559.49 USD | 44,654.76 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.26` | `20.0000` | 1,025.12 USD | 45,679.88 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `51.26` | `764.6800` | 39,193.67 USD | 84,873.55 USD | `3 orders` | `-0.02%` | `-` |
| `ASK` | `51.27` | `66.7100` | 3,420.56 USD | 264,822.98 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.27` | `71.1300` | 3,647.12 USD | 261,402.42 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.27` | `2801.7800` | 143,655.67 USD | 257,755.30 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.27` | `19.0800` | 978.27 USD | 114,099.64 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.27` | `24.8400` | 1,273.57 USD | 113,121.37 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `51.27` | `52.1200` | 2,672.14 USD | 111,847.79 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.27` | `2065.3300` | 105,885.34 USD | 109,175.65 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `51.27` | `64.1800` | 3,290.32 USD | 3,290.32 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `51.27` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 51.27` | `0.00%` | `-` |
| `BID` | `51.27` | `37.0600` | 1,899.88 USD | 1,899.88 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `51.28` | `88.9500` | 4,561.80 USD | 566,682.13 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.28` | `216.2900` | 11,092.22 USD | 562,120.33 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.28` | `88.9500` | 4,561.62 USD | 551,028.12 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.28` | `39.9900` | 2,050.77 USD | 546,466.49 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `51.28` | `5166.5700` | 264,946.88 USD | 544,415.73 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `51.28` | `87.2500` | 4,474.09 USD | 279,468.85 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `51.28` | `1.2000` | 61.53 USD | 274,994.76 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.28` | `157.6900` | 8,085.87 USD | 274,933.22 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `51.28` | `39.4800` | 2,024.38 USD | 266,847.35 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.29` | `379.6800` | 19,473.79 USD | 594,748.04 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `51.29` | `88.9500` | 4,562.07 USD | 575,274.25 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.29` | `78.5800` | 4,030.05 USD | 570,712.19 USD | `2 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `115` | `0x5b5d...c060` | `SHORT` | 17,759,117.47 USD | `346,127.65` | `58.90` | `51.31` | `536.84` | 2,627,242.62 USD | `+14.79%` | `5X Cross` |
| `121` | `0x4692...164f` | `SHORT` | 15,923,960.63 USD | `310,360.19` | `52.93` | `51.31` | `254.34` | 502,770.34 USD | `+3.16%` | `5X Cross` |
| `204` | `0xacb6...efbd` | `SHORT` | 10,319,748.90 USD | `201,133.33` | `59.63` | `51.31` | `76.90` | 1,672,908.22 USD | `+16.21%` | `6X Cross` |
| `239` | `0xc26c...b8f4` | `LONG` | 9,310,524.64 USD | `181,463.41` | `55.43` | `51.31` | `0.000000` | -748,230.44 USD | `-8.04%` | `2X Cross` |
| `283` | `0x49e9...e1d0` | `SHORT` | 8,203,513.49 USD | `159,887.61` | `55.44` | `51.31` | `101.76` | 660,242.22 USD | `+8.05%` | `4X Cross` |
| `352` | `0x645b...87b8` | `LONG` | 6,565,177.74 USD | `127,956.22` | `56.57` | `51.31` | `0.000000` | -673,264.83 USD | `-10.26%` | `3X Cross` |
| `356` | `0xd8c5...99b0` | `SHORT` | 6,480,975.97 USD | `126,320.04` | `61.98` | `51.31` | `199.76` | 1,348,361.88 USD | `+20.80%` | `3X Cross` |
| `389` | `0xe9ff...5903` | `SHORT` | 5,798,167.85 USD | `112,996.08` | `60.07` | `51.31` | `178.77` | 989,782.95 USD | `+17.07%` | `5X Cross` |
| `615` | `0x9aa5...58af` | `LONG` | 3,655,357.91 USD | `71,243.43` | `61.59` | `51.31` | `0.000000` | -732,799.62 USD | `-20.05%` | `20X Cross` |
| `741` | `0x2056...8396` | `LONG` | 3,079,020.00 USD | `60,000.00` | `66.92` | `51.31` | `21.35` | -936,307.14 USD | `-30.41%` | `10X Cross` |
| `835` | `0x354b...6425` | `SHORT` | 2,718,764.60 USD | `52,990.13` | `51.40` | `51.31` | `253.78` | 4,715.84 USD | `+0.17%` | `10X Cross` |
| `887` | `0x0242...ffa1` | `SHORT` | 2,561,074.59 USD | `49,916.67` | `56.48` | `51.31` | `333.33` | 258,057.28 USD | `+10.08%` | `10X Cross` |
| `894` | `0x960b...f0fc` | `LONG` | 2,537,589.01 USD | `49,457.96` | `55.82` | `51.31` | `0.000000` | -223,348.02 USD | `-8.80%` | `25X Cross` |
| `976` | `0x8b9d...7b28` | `LONG` | 2,300,026.72 USD | `44,823.47` | `58.35` | `51.31` | `0.000000` | -315,421.83 USD | `-13.71%` | `10X Cross` |
| `1056` | `0x5647...e7de` | `LONG` | 2,065,806.55 USD | `40,262.07` | `57.38` | `51.31` | `0.000000` | -244,431.05 USD | `-11.83%` | `20X Cross` |
| `1062` | `0xa2ce...3126` | `LONG` | 2,052,960.00 USD | `40,000.00` | `74.30` | `51.31` | `0.000000` | -919,095.49 USD | `-44.77%` | `20X Cross` |
| `1098` | `0xb078...de15` | `SHORT` | 2,000,973.51 USD | `39,000.01` | `52.58` | `51.31` | `201.35` | 49,545.44 USD | `+2.48%` | `8X Cross` |
| `1417` | `0x5a88...d997` | `LONG` | 1,539,180.00 USD | `30,000.00` | `59.50` | `51.31` | `38.66` | -245,707.59 USD | `-15.96%` | `25X Cross` |
| `1418` | `0x3678...b209` | `LONG` | 1,539,180.00 USD | `30,000.00` | `57.15` | `51.31` | `0.000000` | -175,320.00 USD | `-11.39%` | `20X Cross` |
| `1570` | `0xce97...7e78` | `LONG` | 1,367,808.05 USD | `26,656.17` | `51.57` | `51.31` | `0.000000` | -6,956.94 USD | `-0.51%` | `5X Cross` |
| `1648` | `0x7ea9...fc7f` | `LONG` | 1,282,825.00 USD | `25,000.00` | `53.60` | `51.31` | `34.56` | -57,179.05 USD | `-4.46%` | `25X Cross` |
| `1746` | `0x24fb...ed0f` | `LONG` | 1,185,843.43 USD | `23,110.00` | `51.37` | `51.31` | `0.000000` | -1,333.90 USD | `-0.11%` | `20X Cross` |
| `1784` | `0xf517...c032` | `LONG` | 1,160,971.77 USD | `22,627.50` | `66.29` | `51.31` | `0.000000` | -339,023.33 USD | `-29.20%` | `20X Cross` |
| `1913` | `0xcc9f...d218` | `LONG` | 1,053,035.11 USD | `20,520.60` | `52.63` | `51.31` | `26.86` | -26,872.94 USD | `-2.55%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.36` (Vol: 4,300,000.00 USD, Dist: `+3.57%`) | Long MP=`51.16` (Vol: 1,800,000.00 USD, Dist: `--0.71%`)
  * 48H Horizon: Short MP=`54.84` (Vol: 4,200,000.00 USD, Dist: `+6.45%`) | Long MP=`51.17` (Vol: 2,500,000.00 USD, Dist: `--0.68%`)
  * 3D Horizon: Short MP=`55.09` (Vol: 5,200,000.00 USD, Dist: `+6.93%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.68%`)
  * 7D Horizon: Short MP=`55.09` (Vol: 8,900,000.00 USD, Dist: `+6.93%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.68%`)
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
  * Current Rate: `7.46K` | Last 24h: `229.04K` | Last 3d: `461.48K` | Last 7d: `657.16K`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.11` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.77` (Risk Distance: `0.3459` pts)
  * +2.5R Take Profit: `51.98`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `51.64` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `51.98` (Risk Distance: `0.3459` pts)
  * +2.5R Take Profit: `50.77`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`65.99`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
