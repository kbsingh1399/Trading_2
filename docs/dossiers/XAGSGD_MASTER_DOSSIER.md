# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-29 22:36:54 IST` (`2026-10-29 17:06:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `67.11` | **Live Ask Quote**: `67.12` | **Mid Price**: `67.12`
- **Spread Points**: `10.00` | **Spread BPS**: `1.49 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `67.12` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `67.59` | Lower -3.00σ Band: `66.65`
  * Upper +2.51σ Band: `67.49` | Lower -2.51σ Band: `66.75`
  * Upper +2.01σ Band: `67.40` | Lower -2.01σ Band: `66.83`
  * Upper +2.00σ Band: `67.38` | Lower -2.00σ Band: `66.85`
  * Upper +1.28σ Band: `67.30` | Lower -1.28σ Band: `66.93`
  * Upper +1.00σ Band: `67.25` | Lower -1.00σ Band: `66.98`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`67.12` | EMA-20=`67.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`67.12` (Slope: `+0.0000`) | EMA-100=`67.12`
  * Institutional Anchors: EMA-144=`67.12` | EMA-200=`67.12` (Slope: `+0.0000`) | EMA-233=`67.12`
- **Range Boundaries**: 24H High=`67.79` | 24H Low=`66.44` | Weekly High=`68.46` | Weekly Low=`65.77`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `53.09` (Distance: `-1.24%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.04%`)
  * Value Area Low (VAL) = `52.03` (Distance: `+0.76%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.48` | Weekly POC=`53.86` | Weekly VAL=`53.30`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.85` - `67.38`
  * Optimal Trade Entry (OTE 0.705): `67.25`
  * Structural Invalidation Anchor (0.786): `67.65`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.14` | `52.23` | `51.98` | `52.01` | `3,251` | 169,084.51 USD | -111,568.06 USD | `-65.98%` | -883,811.11 USD | `-1.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `52.01` | `52.35` | `51.98` | `52.24` | `2,765` | 144,446.36 USD | 72,793.37 USD | `+50.39%` | -811,017.74 USD | `+1.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.24` | `52.43` | `52.24` | `52.40` | `3,543` | 185,656.74 USD | 148,023.62 USD | `+79.73%` | -662,994.12 USD | `+1.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.31` | `52.52` | `52.03` | `52.05` | `12,846` | 668,582.92 USD | -492,568.23 USD | `-73.67%` | -1,957,334.03 USD | `-2.70` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.05` | `52.35` | `51.98` | `52.24` | `9,551` | 498,953.79 USD | 227,811.80 USD | `+45.66%` | -1,729,522.24 USD | `+1.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.24` | `52.45` | `52.03` | `52.16` | `9,968` | 519,900.98 USD | -154,732.43 USD | `-29.76%` | -1,884,254.67 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.36` | `52.72` | `52.30` | `52.37` | `22,190` | 1,162,090.30 USD | -379,003.07 USD | `-32.61%` | -1,358,348.37 USD | `-0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `52.37` | `52.61` | `51.98` | `52.24` | `41,435` | 2,164,605.83 USD | -391,069.83 USD | `-18.07%` | -1,749,418.20 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.24` | `52.76` | `52.03` | `52.61` | `32,755` | 1,723,273.30 USD | 951,587.73 USD | `+55.22%` | -797,830.47 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `BID` | `52.43` | `113.2000` | 5,935.53 USD | 556,305.44 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.43` | `1319.2800` | 69,173.81 USD | 625,479.25 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `52.43` | `6045.9700` | 317,002.30 USD | 942,481.54 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.43` | `1023.7200` | 53,674.66 USD | 996,156.21 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.43` | `130.9800` | 6,867.28 USD | 1,003,023.49 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.44` | `647.2400` | 33,943.85 USD | 299,352.23 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `52.44` | `178.3000` | 9,350.59 USD | 308,702.82 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.44` | `518.4200` | 27,186.98 USD | 335,889.80 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.44` | `3038.7600` | 159,355.61 USD | 495,245.42 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `52.44` | `423.4500` | 22,205.72 USD | 517,451.13 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.44` | `252.2100` | 13,225.64 USD | 530,676.77 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.44` | `39.7600` | 2,084.93 USD | 532,761.71 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.44` | `190.3600` | 9,981.91 USD | 542,743.62 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.44` | `145.4400` | 7,626.29 USD | 550,369.91 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `52.45` | `0.2000` | 10.49 USD | 10.49 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.45` | `0.00%` | `-` |
| `BID` | `52.45` | `665.1400` | 34,886.59 USD | 34,886.59 USD | `10 orders` | `-0.00%` | `-` |
| `BID` | `52.45` | `2351.1800` | 123,317.04 USD | 158,203.63 USD | `10 orders` | `-0.00%` | `-` |
| `BID` | `52.45` | `712.2900` | 37,358.19 USD | 195,561.82 USD | `6 orders` | `-0.00%` | `-` |
| `BID` | `52.45` | `41.1800` | 2,159.77 USD | 197,721.59 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.45` | `227.5200` | 11,932.51 USD | 209,654.10 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.45` | `1063.1000` | 55,754.28 USD | 265,408.38 USD | `4 orders` | `-0.01%` | `-` |
| `ASK` | `52.46` | `1110.1900` | 58,245.01 USD | 228,068.73 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `52.46` | `149.3000` | 7,832.73 USD | 169,823.72 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.46` | `1919.7200` | 100,712.35 USD | 161,991.00 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.46` | `1074.5400` | 56,368.22 USD | 61,278.65 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.46` | `23.6500` | 1,240.61 USD | 4,910.43 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.46` | `69.7600` | 3,659.33 USD | 3,669.82 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.47` | `5740.5000` | 301,227.00 USD | 1,389,955.13 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.47` | `404.2000` | 21,209.59 USD | 1,088,728.13 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `52.47` | `179.5500` | 9,421.35 USD | 1,067,518.54 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.47` | `4062.8500` | 213,181.80 USD | 1,058,097.20 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `52.47` | `339.1300` | 17,794.15 USD | 844,915.39 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `52.47` | `3255.6000` | 170,818.08 USD | 827,121.24 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `52.47` | `488.9800` | 25,655.80 USD | 656,303.17 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.47` | `5768.8000` | 302,671.63 USD | 630,647.36 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.47` | `1904.2600` | 99,907.00 USD | 327,975.73 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `52.48` | `343.5400` | 18,028.29 USD | 1,835,468.68 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `52.48` | `6360.0700` | 333,757.39 USD | 1,817,440.38 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `52.48` | `166.9500` | 8,760.87 USD | 1,483,682.99 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `52.48` | `1619.1900` | 84,967.00 USD | 1,474,922.12 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:34:53 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `100` | `0x49e9...e1d0` | `SHORT` | 19,110,207.28 USD | `365,962.72` | `55.61` | `52.20` | `77.62` | 1,239,395.66 USD | `+6.49%` | `4X Cross` |
| `119` | `0x5b5d...c060` | `SHORT` | 17,422,518.50 USD | `333,790.30` | `59.15` | `52.20` | `490.48` | 2,320,515.45 USD | `+13.32%` | `5X Cross` |
| `121` | `0x4692...164f` | `SHORT` | 16,999,969.12 USD | `325,576.35` | `53.52` | `52.20` | `229.94` | 423,299.35 USD | `+2.49%` | `5X Cross` |
| `131` | `0x4e23...20c3` | `LONG` | 15,878,028.20 USD | `304,066.11` | `53.93` | `52.20` | `16.30` | -521,717.75 USD | `-3.29%` | `16X Cross` |
| `218` | `0xacb6...efbd` | `SHORT` | 10,507,406.29 USD | `201,133.33` | `59.63` | `52.20` | `76.43` | 1,485,250.82 USD | `+14.14%` | `6X Cross` |
| `284` | `0xc26c...b8f4` | `LONG` | 8,766,072.88 USD | `167,945.30` | `55.67` | `52.20` | `0.000000` | -582,661.97 USD | `-6.65%` | `2X Cross` |
| `370` | `0xd8c5...99b0` | `SHORT` | 6,599,716.81 USD | `126,320.04` | `61.98` | `52.20` | `194.43` | 1,229,621.04 USD | `+18.63%` | `3X Cross` |
| `371` | `0x645b...87b8` | `LONG` | 6,587,737.54 USD | `126,211.54` | `56.64` | `52.20` | `0.000000` | -560,620.01 USD | `-8.51%` | `3X Cross` |
| `376` | `0xfc66...ca06` | `SHORT` | 6,451,088.06 USD | `123,548.56` | `54.61` | `52.20` | `386.44` | 295,420.23 USD | `+4.58%` | `3X Cross` |
| `407` | `0xe9ff...5903` | `SHORT` | 5,897,491.41 USD | `112,996.08` | `60.07` | `52.20` | `196.95` | 890,459.40 USD | `+15.10%` | `5X Cross` |
| `630` | `0x9aa5...58af` | `LONG` | 3,720,973.11 USD | `71,243.43` | `61.59` | `52.20` | `0.000000` | -667,184.42 USD | `-17.93%` | `20X Cross` |
| `744` | `0x2056...8396` | `LONG` | 3,133,740.00 USD | `60,000.00` | `66.92` | `52.20` | `21.34` | -881,587.14 USD | `-28.13%` | `10X Cross` |
| `857` | `0xb078...de15` | `SHORT` | 2,716,763.79 USD | `51,999.46` | `54.67` | `52.20` | `168.29` | 125,832.89 USD | `+4.63%` | `8X Cross` |
| `882` | `0x0242...ffa1` | `SHORT` | 2,605,450.51 USD | `49,916.67` | `56.48` | `52.20` | `261.64` | 213,681.36 USD | `+8.20%` | `10X Cross` |
| `890` | `0x960b...f0fc` | `LONG` | 2,581,507.68 USD | `49,457.96` | `55.82` | `52.20` | `0.000000` | -179,429.35 USD | `-6.95%` | `25X Cross` |
| `980` | `0x8b9d...7b28` | `LONG` | 2,337,230.20 USD | `44,823.47` | `58.35` | `52.20` | `0.000000` | -278,218.35 USD | `-11.90%` | `10X Cross` |
| `1079` | `0x5647...e7de` | `LONG` | 2,103,532.11 USD | `40,262.07` | `57.38` | `52.20` | `0.000000` | -206,705.49 USD | `-9.83%` | `20X Cross` |
| `1092` | `0xa2ce...3126` | `LONG` | 2,085,720.00 USD | `40,000.00` | `74.30` | `52.20` | `0.000000` | -886,335.49 USD | `-42.50%` | `20X Cross` |
| `1458` | `0x5a88...d997` | `LONG` | 1,566,000.00 USD | `30,000.00` | `59.50` | `52.20` | `38.62` | -218,887.59 USD | `-13.98%` | `25X Cross` |
| `1459` | `0x3678...b209` | `LONG` | 1,565,880.00 USD | `30,000.00` | `57.15` | `52.20` | `0.000000` | -148,620.00 USD | `-9.49%` | `20X Cross` |
| `1674` | `0x7ea9...fc7f` | `LONG` | 1,305,150.00 USD | `25,000.00` | `53.60` | `52.20` | `0.000000` | -34,854.05 USD | `-2.67%` | `25X Cross` |
| `1810` | `0xf517...c032` | `LONG` | 1,181,811.70 USD | `22,627.50` | `66.29` | `52.20` | `0.000000` | -318,183.41 USD | `-26.92%` | `20X Cross` |
| `1940` | `0xcc9f...d218` | `LONG` | 1,072,016.66 USD | `20,520.60` | `52.63` | `52.20` | `26.85` | -7,891.39 USD | `-0.74%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.86` (Vol: 3,800,000.00 USD, Dist: `+2.44%`) | Long MP=`51.93` (Vol: 2,700,000.00 USD, Dist: `--1.24%`)
  * 48H Horizon: Short MP=`54.97` (Vol: 4,800,000.00 USD, Dist: `+4.54%`) | Long MP=`51.93` (Vol: 2,400,000.00 USD, Dist: `--1.24%`)
  * 3D Horizon: Short MP=`55.10` (Vol: 5,400,000.00 USD, Dist: `+4.80%`) | Long MP=`51.93` (Vol: 5,000,000.00 USD, Dist: `--1.24%`)
  * 7D Horizon: Short MP=`54.85` (Vol: 8,300,000.00 USD, Dist: `+4.32%`) | Long MP=`51.85` (Vol: 5,600,000.00 USD, Dist: `--1.39%`)
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
  * Current Rate: `52.75K` | Last 24h: `133.17K` | Last 3d: `385.56K` | Last 7d: `803.65K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0079%` | **USDT BingX** | `-` |
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `52.03` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.82` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `55.07`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `53.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `54.30` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `50.05`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.65`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
