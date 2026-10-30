# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 16:27:43 IST` (`2026-10-30 10:57:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `64.45` | **Live Ask Quote**: `64.47` | **Mid Price**: `64.46`
- **Spread Points**: `14.00` | **Spread BPS**: `2.17 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `51.19` | VWAP Z-Score: `-1.73` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1859` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.15` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.31` | Lower -3.00σ Band: `50.06`
  * Upper +2.51σ Band: `52.13` | Lower -2.51σ Band: `50.24`
  * Upper +2.01σ Band: `51.94` | Lower -2.01σ Band: `50.43`
  * Upper +2.00σ Band: `51.94` | Lower -2.00σ Band: `50.43`
  * Upper +1.28σ Band: `51.67` | Lower -1.28σ Band: `50.70`
  * Upper +1.00σ Band: `51.56` | Lower -1.00σ Band: `50.81`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`50.66` | EMA-20=`50.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.21` (Slope: `+0.0000`) | EMA-100=`51.73`
  * Institutional Anchors: EMA-144=`52.07` | EMA-200=`52.41` (Slope: `-0.4161`) | EMA-233=`52.62`
- **Range Boundaries**: 24H High=`53.07` | 24H Low=`50.40` | Weekly High=`54.61` | Weekly Low=`50.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.07` (Distance: `-3.05%`)
  * Point of Control (POC) = `51.44` (Distance: `-1.86%`)
  * Value Area Low (VAL) = `50.88` (Distance: `-0.79%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.51` | Weekly POC=`53.87` | Weekly VAL=`52.63`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.79` | Low=`50.40`
  * New York Session (13:00-21:00 UTC): High=`50.77` | Low=`50.42`
  * Initial Balance (First Hour): IB High=`51.79` | IB Low=`50.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `64.20` - `64.72`
  * Optimal Trade Entry (OTE 0.705): `64.59`
  * Structural Invalidation Anchor (0.786): `64.98`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `50.73` | `50.74` | `50.64` | `50.67` | `825` | 41,806.05 USD | -19,868.22 USD | `-47.52%` | -1,279,910.36 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `50.67` | `50.71` | `50.56` | `50.57` | `910` | 46,019.61 USD | -37,157.73 USD | `-80.74%` | -1,317,068.09 USD | `-0.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `50.57` | `50.60` | `50.41` | `50.47` | `1,212` | 61,167.22 USD | -27,255.86 USD | `-44.56%` | -1,344,323.95 USD | `-0.57` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `50.79` | `50.87` | `50.64` | `50.65` | `2,364` | 119,727.14 USD | -95,249.59 USD | `-79.56%` | -1,888,327.35 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `50.65` | `50.74` | `50.57` | `50.67` | `2,542` | 128,813.31 USD | 22,485.16 USD | `+17.46%` | -1,865,842.19 USD | `+0.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `50.67` | `50.71` | `50.40` | `50.61` | `3,016` | 152,627.70 USD | 7,116.08 USD | `+4.66%` | -1,858,726.10 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `51.36` | `51.79` | `50.87` | `51.08` | `15,419` | 787,556.26 USD | -339,906.20 USD | `-43.16%` | -2,034,303.71 USD | `-0.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.08` | `51.12` | `50.66` | `50.78` | `20,835` | 1,057,959.63 USD | -603,060.14 USD | `-57.00%` | -2,637,363.85 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `50.78` | `50.87` | `50.40` | `50.61` | `11,199` | 566,736.59 USD | -139,241.32 USD | `-24.57%` | -2,776,605.17 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -3,487,681.50 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -5,082,081.83 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.36` | `51.79` | `50.40` | `50.89` | `62,135` | 3,162,174.42 USD | -1,002,113.55 USD | `-31.69%` | -6,084,195.37 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -1,493,267.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -2,486,578.48 USD | `-0.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -3,487,681.50 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -5,082,081.83 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.36` | `51.79` | `50.40` | `50.89` | `62,135` | 3,162,174.42 USD | -1,002,113.55 USD | `-31.69%` | -6,084,195.37 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `50.48` | `5683.7100` | 286,942.10 USD | 1,548,389.78 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.48` | `4.7400` | 239.29 USD | 1,548,629.07 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.48` | `350.1100` | 17,674.60 USD | 1,566,303.68 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `50.49` | `8207.0000` | 414,412.46 USD | 815,086.04 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `50.49` | `90.7100` | 4,580.31 USD | 819,666.35 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `50.49` | `168.3400` | 8,499.82 USD | 828,166.18 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `50.49` | `184.4800` | 9,314.58 USD | 837,480.76 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `50.49` | `198.2000` | 10,007.12 USD | 847,487.87 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `50.49` | `6248.7900` | 315,495.16 USD | 1,162,983.03 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `50.49` | `862.8900` | 43,565.59 USD | 1,206,548.62 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.49` | `1087.3900` | 54,899.06 USD | 1,261,447.68 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `50.50` | `396.6400` | 20,031.91 USD | 22,192.05 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `50.50` | `994.5700` | 50,228.77 USD | 72,420.82 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `50.50` | `1963.3000` | 99,150.58 USD | 171,571.39 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `50.50` | `352.6300` | 17,808.17 USD | 189,379.56 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `50.50` | `202.7300` | 10,237.86 USD | 199,617.43 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `50.50` | `544.7700` | 27,510.34 USD | 227,127.77 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `50.50` | `147.7100` | 7,458.91 USD | 234,586.68 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `50.50` | `3289.1100` | 166,086.90 USD | 400,673.58 USD | `2 orders` | `-0.02%` | `-` |
| `ASK` | `50.51` | `46.3900` | 2,343.34 USD | 48,972.45 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.51` | `184.8300` | 9,336.32 USD | 46,629.11 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `50.51` | `190.2000` | 9,607.38 USD | 37,292.79 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `50.51` | `189.9900` | 9,596.58 USD | 27,685.41 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `50.51` | `38.8700` | 1,963.32 USD | 18,088.82 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.51` | `127.8000` | 6,454.92 USD | 16,125.50 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `50.51` | `191.4700` | 9,670.58 USD | 9,670.58 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `50.51` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 50.51` | `0.00%` | `-` |
| `BID` | `50.51` | `42.7700` | 2,160.14 USD | 2,160.14 USD | `2 orders` | `-0.00%` | `-` |
| `ASK` | `50.52` | `488.4700` | 24,679.95 USD | 806,740.52 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `50.52` | `3704.7800` | 187,180.30 USD | 782,060.57 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `50.52` | `126.3700` | 6,384.59 USD | 594,880.27 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.52` | `5881.6900` | 297,154.74 USD | 588,495.68 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `50.52` | `895.1100` | 45,221.85 USD | 291,340.94 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `50.52` | `99.9600` | 5,049.98 USD | 246,119.08 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `50.52` | `1270.5300` | 64,185.91 USD | 241,069.10 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `50.52` | `267.3000` | 13,503.46 USD | 176,883.20 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `50.52` | `405.4000` | 20,479.59 USD | 163,379.74 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `50.52` | `1619.0800` | 81,789.45 USD | 142,900.15 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `50.52` | `240.2900` | 12,138.25 USD | 61,110.70 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `50.53` | `1920.1600` | 97,021.84 USD | 912,262.35 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `50.53` | `168.2300` | 8,499.99 USD | 815,240.51 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,495,022.07 USD | `346,127.65` | `58.90` | `50.54` | `488.85` | 2,891,338.02 USD | `+16.53%` | `5X Cross` |
| `125` | `0x4692...164f` | `SHORT` | 15,605,238.18 USD | `308,751.72` | `52.16` | `50.54` | `260.21` | 499,715.36 USD | `+3.20%` | `5X Cross` |
| `209` | `0xacb6...efbd` | `SHORT` | 10,166,485.30 USD | `201,133.33` | `59.63` | `50.54` | `77.15` | 1,826,171.82 USD | `+17.96%` | `6X Cross` |
| `244` | `0xc26c...b8f4` | `LONG` | 9,171,523.67 USD | `181,463.41` | `55.43` | `50.54` | `0.000000` | -887,231.41 USD | `-9.67%` | `2X Cross` |
| `276` | `0x49e9...e1d0` | `SHORT` | 8,379,820.17 USD | `165,789.30` | `55.17` | `50.54` | `100.82` | 767,614.85 USD | `+9.16%` | `4X Cross` |
| `357` | `0x645b...87b8` | `LONG` | 6,498,534.19 USD | `128,576.91` | `56.54` | `50.54` | `0.000000` | -771,535.06 USD | `-11.87%` | `3X Cross` |
| `361` | `0xd8c5...99b0` | `SHORT` | 6,384,720.10 USD | `126,320.04` | `61.98` | `50.54` | `198.17` | 1,444,617.75 USD | `+22.63%` | `3X Cross` |
| `393` | `0xe9ff...5903` | `SHORT` | 5,711,838.85 USD | `112,996.08` | `60.07` | `50.54` | `175.03` | 1,076,111.96 USD | `+18.84%` | `5X Cross` |
| `672` | `0xfc66...ca06` | `SHORT` | 3,331,220.39 USD | `65,908.64` | `50.61` | `50.54` | `330.76` | 4,310.30 USD | `+0.13%` | `7X Cross` |
| `734` | `0x9aa5...58af` | `LONG` | 3,100,722.96 USD | `61,345.79` | `61.59` | `50.54` | `0.000000` | -677,800.76 USD | `-21.86%` | `20X Cross` |
| `752` | `0x2056...8396` | `LONG` | 3,032,700.00 USD | `60,000.00` | `66.92` | `50.54` | `21.36` | -982,627.14 USD | `-32.40%` | `10X Cross` |
| `882` | `0x0242...ffa1` | `SHORT` | 2,522,888.34 USD | `49,916.67` | `56.48` | `50.54` | `333.63` | 296,243.53 USD | `+11.74%` | `10X Cross` |
| `888` | `0x960b...f0fc` | `LONG` | 2,499,852.59 USD | `49,457.96` | `55.82` | `50.54` | `0.000000` | -261,084.44 USD | `-10.44%` | `25X Cross` |
| `975` | `0x8b9d...7b28` | `LONG` | 2,264,436.88 USD | `44,823.47` | `58.35` | `50.54` | `0.000000` | -351,011.66 USD | `-15.50%` | `10X Cross` |
| `1061` | `0x5647...e7de` | `LONG` | 2,034,683.97 USD | `40,262.07` | `57.38` | `50.54` | `0.000000` | -275,553.63 USD | `-13.54%` | `20X Cross` |
| `1072` | `0xa2ce...3126` | `LONG` | 2,021,960.00 USD | `40,000.00` | `74.30` | `50.54` | `0.000000` | -950,095.49 USD | `-46.99%` | `20X Cross` |
| `1101` | `0xb078...de15` | `SHORT` | 1,971,294.51 USD | `39,000.01` | `52.58` | `50.54` | `205.66` | 79,224.45 USD | `+4.02%` | `8X Cross` |
| `1430` | `0x5a88...d997` | `LONG` | 1,516,410.00 USD | `30,000.00` | `59.50` | `50.54` | `38.12` | -268,477.59 USD | `-17.70%` | `25X Cross` |
| `1431` | `0x3678...b209` | `LONG` | 1,516,320.00 USD | `30,000.00` | `57.15` | `50.54` | `0.000000` | -198,180.00 USD | `-13.07%` | `20X Cross` |
| `1624` | `0xed62...e004` | `SHORT` | 1,296,981.78 USD | `25,660.45` | `50.81` | `50.54` | `54.72` | 6,825.68 USD | `+0.53%` | `25X Cross` |
| `1658` | `0x7ea9...fc7f` | `LONG` | 1,263,725.00 USD | `25,000.00` | `53.60` | `50.54` | `35.38` | -76,279.05 USD | `-6.04%` | `25X Cross` |
| `1805` | `0xf517...c032` | `LONG` | 1,143,729.61 USD | `22,627.50` | `66.29` | `50.54` | `0.000000` | -356,265.49 USD | `-31.15%` | `20X Cross` |
| `1812` | `0x24fb...ed0f` | `LONG` | 1,140,132.70 USD | `22,555.00` | `51.37` | `50.54` | `0.000000` | -18,533.88 USD | `-1.63%` | `20X Cross` |
| `1851` | `0x9e11...22a3` | `LONG` | 1,109,194.23 USD | `21,945.99` | `50.67` | `50.54` | `34.46` | -2,728.17 USD | `-0.25%` | `3X Isolated` |
| `1931` | `0xcc9f...d218` | `LONG` | 1,037,049.56 USD | `20,520.60` | `52.63` | `50.54` | `26.87` | -42,858.49 USD | `-4.13%` | `2X Isolated` |
| `1960` | `0xce97...7e78` | `LONG` | 1,021,918.30 USD | `20,217.59` | `50.75` | `50.54` | `0.000000` | -4,125.45 USD | `-0.40%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `77.50` | 38,750.00 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 38.75K USD at 77.5000 USD [API] | `2026-01-30 18:21:38` |
| `ANNOUNCEMENT` | `INFO` | `80.86` | 2,533.31 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 2.53K USD at 80.8590 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.86` | 4,990.62 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 4.99K USD at 80.8590 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.86` | 55.79 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.06K USD at 80.8610 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.87` | 7,164.82 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 7.16K USD at 80.8670 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `80.88` | 25,691.71 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 25.69K USD at 80.8780 USD [API] | `2026-01-30 18:17:17` |
| `ANNOUNCEMENT` | `INFO` | `84.07` | 1,894.12 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 1.89K USD at 84.0710 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.07` | 280.81 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.28K USD at 84.0740 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 300.16 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.30K USD at 84.0780 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 16,982.48 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 16.98K USD at 84.0800 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 2,932.75 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 2.93K USD at 84.0810 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 219.45 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.22K USD at 84.0820 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.08` | 315.31 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.32K USD at 84.0820 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 2,609.34 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 2.61K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 4,204.55 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 4.20K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 301.89 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.30K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 433.91 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.43K USD at 84.0910 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 420.46 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.42K USD at 84.0920 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `84.09` | 11,147.37 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 11.15K USD at 84.0930 USD [API] | `2026-01-30 18:09:32` |
| `ANNOUNCEMENT` | `INFO` | `86.18` | 14,853.47 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 14.85K USD at 86.1770 USD [API] | `2026-01-30 17:53:32` |
| `ANNOUNCEMENT` | `INFO` | `86.18` | 24,224.35 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 24.22K USD at 86.1770 USD [API] | `2026-01-30 17:53:32` |
| `ANNOUNCEMENT` | `INFO` | `86.19` | 4,011.24 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 4.01K USD at 86.1890 USD [API] | `2026-01-30 17:53:32` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`52.71` (Vol: 3,600,000.00 USD, Dist: `+4.03%`) | Long MP=`50.23` (Vol: 3,100,000.00 USD, Dist: `--0.86%`)
  * 48H Horizon: Short MP=`54.87` (Vol: 4,200,000.00 USD, Dist: `+8.28%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
  * 3D Horizon: Short MP=`54.97` (Vol: 5,200,000.00 USD, Dist: `+8.49%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
  * 7D Horizon: Short MP=`55.07` (Vol: 7,100,000.00 USD, Dist: `+8.69%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
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
  * Current Rate: `46.80K` | Last 24h: `158.28K` | Last 3d: `386.46K` | Last 7d: `548.84K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0092%` | **USDT BingX** | `-` |
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
  * Execution Entry: `50.88` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.64` (Risk Distance: `0.2441` pts)
  * +2.5R Take Profit: `51.49`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.31` (Risk Distance: `0.2441` pts)
  * +2.5R Take Profit: `51.46`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`64.98`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
