# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 15:51:23 IST` (`2026-10-30 10:21:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `64.64` | **Live Ask Quote**: `64.66` | **Mid Price**: `64.65`
- **Spread Points**: `21.00` | **Spread BPS**: `3.25 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `51.20` | VWAP Z-Score: `-1.81` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1996` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.22` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.30` | Lower -3.00σ Band: `50.10`
  * Upper +2.51σ Band: `52.12` | Lower -2.51σ Band: `50.28`
  * Upper +2.01σ Band: `51.94` | Lower -2.01σ Band: `50.47`
  * Upper +2.00σ Band: `51.94` | Lower -2.00σ Band: `50.47`
  * Upper +1.28σ Band: `51.67` | Lower -1.28σ Band: `50.73`
  * Upper +1.00σ Band: `51.57` | Lower -1.00σ Band: `50.84`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`50.73` | EMA-20=`50.87` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.26` (Slope: `+0.0000`) | EMA-100=`51.78`
  * Institutional Anchors: EMA-144=`52.11` | EMA-200=`52.44` (Slope: `-0.4183`) | EMA-233=`52.65`
- **Range Boundaries**: 24H High=`53.07` | 24H Low=`50.40` | Weekly High=`54.61` | Weekly Low=`50.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.07` (Distance: `-2.81%`)
  * Point of Control (POC) = `51.44` (Distance: `-1.61%`)
  * Value Area Low (VAL) = `50.91` (Distance: `-0.58%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.51` | Weekly POC=`53.87` | Weekly VAL=`52.63`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.79` | Low=`50.40`
  * New York Session (13:00-21:00 UTC): High=`50.77` | Low=`50.50`
  * Initial Balance (First Hour): IB High=`51.79` | IB Low=`50.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `64.39` - `64.91`
  * Optimal Trade Entry (OTE 0.705): `64.78`
  * Structural Invalidation Anchor (0.786): `65.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `50.79` | `50.80` | `50.74` | `50.79` | `810` | 41,139.09 USD | 10,121.52 USD | `+24.60%` | -1,223,024.01 USD | `+0.80` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `50.79` | `50.87` | `50.75` | `50.75` | `924` | 46,890.23 USD | -31,719.86 USD | `-67.65%` | -1,254,743.87 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `50.75` | `50.75` | `50.69` | `50.73` | `761` | 38,607.81 USD | 4,609.89 USD | `+11.94%` | -1,250,133.98 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `50.82` | `50.90` | `50.66` | `50.78` | `4,640` | 235,609.92 USD | -25,313.46 USD | `-10.74%` | -1,937,099.02 USD | `-0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `50.78` | `50.82` | `50.68` | `50.79` | `3,277` | 166,435.55 USD | 54,875.49 USD | `+32.97%` | -1,882,223.53 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `50.79` | `50.87` | `50.64` | `50.65` | `2,364` | 119,727.14 USD | -95,249.59 USD | `-79.56%` | -1,977,473.13 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `BID` | `50.60` | `431.7000` | 21,846.18 USD | 1,693,256.62 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `50.61` | `42.8500` | 2,168.81 USD | 1,275,861.91 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `50.61` | `513.3100` | 25,980.16 USD | 1,301,842.07 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.61` | `5881.9100` | 297,695.23 USD | 1,599,537.29 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.61` | `789.7900` | 39,972.06 USD | 1,639,509.36 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.61` | `488.5300` | 24,724.50 USD | 1,664,233.86 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.61` | `48.3200` | 2,445.43 USD | 1,666,679.29 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.61` | `93.4900` | 4,731.15 USD | 1,671,410.44 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `50.62` | `521.6900` | 26,410.56 USD | 438,548.65 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `50.62` | `287.8800` | 14,573.64 USD | 453,122.29 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `50.62` | `0.2100` | 10.63 USD | 453,132.92 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `50.62` | `202.1100` | 10,231.21 USD | 463,364.13 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `50.62` | `11729.7600` | 593,772.18 USD | 1,057,136.31 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `50.62` | `253.5100` | 12,832.42 USD | 1,069,968.73 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `50.62` | `4024.9800` | 203,724.36 USD | 1,273,693.10 USD | `3 orders` | `-0.03%` | `-` |
| `ASK` | `50.63` | `38.8400` | 1,966.66 USD | 1,977.30 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.63` | `0.2100` | 10.63 USD | 10.63 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `50.63` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 50.63` | `0.00%` | `-` |
| `BID` | `50.63` | `222.2000` | 11,249.99 USD | 11,249.99 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `50.63` | `7356.1700` | 372,435.53 USD | 383,685.52 USD | `9 orders` | `-0.00%` | `-` |
| `BID` | `50.63` | `69.0200` | 3,494.34 USD | 387,179.86 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `50.63` | `120.0600` | 6,078.28 USD | 393,258.14 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `50.63` | `372.9300` | 18,879.95 USD | 412,138.09 USD | `3 orders` | `-0.01%` | `-` |
| `ASK` | `50.64` | `118.7800` | 6,015.49 USD | 36,135.82 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.64` | `48.2200` | 2,442.01 USD | 30,120.32 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `50.64` | `123.2400` | 6,241.12 USD | 27,678.32 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `50.64` | `129.0900` | 6,537.25 USD | 21,437.20 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `50.64` | `93.7200` | 4,745.79 USD | 14,899.95 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.64` | `161.4800` | 8,176.86 USD | 10,154.16 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `50.65` | `231.9500` | 11,749.20 USD | 501,382.32 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `50.65` | `2124.4500` | 107,609.77 USD | 489,633.12 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `50.65` | `5685.0200` | 287,957.63 USD | 382,023.36 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.65` | `646.3200` | 32,736.11 USD | 94,065.73 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.65` | `90.4800` | 4,582.72 USD | 61,329.62 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `50.65` | `81.1500` | 4,109.92 USD | 56,746.90 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.65` | `325.8200` | 16,501.15 USD | 52,636.97 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `50.66` | `3954.6600` | 200,343.08 USD | 1,266,418.44 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `50.66` | `6749.4200` | 341,918.87 USD | 1,066,075.36 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `50.66` | `4068.1800` | 206,085.86 USD | 724,156.49 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `50.66` | `197.5100` | 10,005.26 USD | 518,070.63 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `50.66` | `131.9300` | 6,683.05 USD | 508,065.37 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,525,135.17 USD | `346,127.65` | `58.90` | `50.63` | `503.57` | 2,861,224.92 USD | `+16.33%` | `5X Cross` |
| `122` | `0x4692...164f` | `SHORT` | 15,722,796.98 USD | `310,530.83` | `52.29` | `50.63` | `258.65` | 513,997.04 USD | `+3.27%` | `5X Cross` |
| `206` | `0xacb6...efbd` | `SHORT` | 10,186,397.50 USD | `201,133.33` | `59.63` | `50.63` | `77.05` | 1,806,259.62 USD | `+17.73%` | `6X Cross` |
| `240` | `0xc26c...b8f4` | `LONG` | 9,187,855.38 USD | `181,463.41` | `55.43` | `50.63` | `0.000000` | -870,899.70 USD | `-9.48%` | `2X Cross` |
| `276` | `0x49e9...e1d0` | `SHORT` | 8,394,011.86 USD | `165,778.17` | `55.18` | `50.63` | `99.31` | 752,860.23 USD | `+8.97%` | `4X Cross` |
| `354` | `0x645b...87b8` | `LONG` | 6,510,106.11 USD | `128,576.91` | `56.54` | `50.63` | `0.000000` | -759,963.13 USD | `-11.67%` | `3X Cross` |
| `361` | `0xd8c5...99b0` | `SHORT` | 6,396,088.91 USD | `126,320.04` | `61.98` | `50.63` | `198.78` | 1,433,248.94 USD | `+22.41%` | `3X Cross` |
| `395` | `0xe9ff...5903` | `SHORT` | 5,720,313.55 USD | `112,996.08` | `60.07` | `50.63` | `175.04` | 1,067,637.25 USD | `+18.66%` | `5X Cross` |
| `675` | `0x354b...6425` | `SHORT` | 3,307,283.76 USD | `65,317.45` | `51.01` | `50.63` | `218.26` | 24,346.45 USD | `+0.74%` | `10X Cross` |
| `683` | `0x9aa5...58af` | `LONG` | 3,256,680.05 USD | `64,299.00` | `61.59` | `50.63` | `0.000000` | -703,743.26 USD | `-21.61%` | `20X Cross` |
| `750` | `0x2056...8396` | `LONG` | 3,038,040.00 USD | `60,000.00` | `66.92` | `50.63` | `21.36` | -977,287.14 USD | `-32.17%` | `10X Cross` |
| `874` | `0x0242...ffa1` | `SHORT` | 2,527,380.84 USD | `49,916.67` | `56.48` | `50.63` | `331.48` | 291,751.03 USD | `+11.54%` | `10X Cross` |
| `880` | `0x960b...f0fc` | `LONG` | 2,504,155.43 USD | `49,457.96` | `55.82` | `50.63` | `0.000000` | -256,781.60 USD | `-10.25%` | `25X Cross` |
| `970` | `0x8b9d...7b28` | `LONG` | 2,269,188.17 USD | `44,823.47` | `58.35` | `50.63` | `0.000000` | -346,260.38 USD | `-15.26%` | `10X Cross` |
| `1056` | `0x5647...e7de` | `LONG` | 2,039,072.54 USD | `40,262.07` | `57.38` | `50.63` | `0.000000` | -271,165.06 USD | `-13.30%` | `20X Cross` |
| `1067` | `0xa2ce...3126` | `LONG` | 2,025,000.00 USD | `40,000.00` | `74.30` | `50.63` | `0.000000` | -947,055.49 USD | `-46.77%` | `20X Cross` |
| `1094` | `0xb078...de15` | `SHORT` | 1,974,648.51 USD | `39,000.01` | `52.58` | `50.63` | `200.49` | 75,870.45 USD | `+3.84%` | `8X Cross` |
| `1424` | `0x3678...b209` | `LONG` | 1,519,020.00 USD | `30,000.00` | `57.15` | `50.63` | `0.000000` | -195,480.00 USD | `-12.87%` | `20X Cross` |
| `1425` | `0x5a88...d997` | `LONG` | 1,518,990.00 USD | `30,000.00` | `59.50` | `50.63` | `38.47` | -265,897.59 USD | `-17.50%` | `25X Cross` |
| `1616` | `0xed62...e004` | `SHORT` | 1,299,291.23 USD | `25,660.45` | `50.81` | `50.63` | `54.72` | 4,516.24 USD | `+0.35%` | `25X Cross` |
| `1649` | `0x7ea9...fc7f` | `LONG` | 1,265,625.00 USD | `25,000.00` | `53.60` | `50.63` | `35.33` | -74,379.05 USD | `-5.88%` | `25X Cross` |
| `1794` | `0xf517...c032` | `LONG` | 1,146,014.99 USD | `22,627.50` | `66.29` | `50.63` | `0.000000` | -353,980.11 USD | `-30.89%` | `20X Cross` |
| `1800` | `0x24fb...ed0f` | `LONG` | 1,141,846.88 USD | `22,555.00` | `51.37` | `50.63` | `0.000000` | -16,819.70 USD | `-1.47%` | `20X Cross` |
| `1839` | `0x9e11...22a3` | `LONG` | 1,111,169.37 USD | `21,945.99` | `50.67` | `50.63` | `34.46` | -753.03 USD | `-0.07%` | `3X Isolated` |
| `1921` | `0xcc9f...d218` | `LONG` | 1,039,265.79 USD | `20,520.60` | `52.63` | `50.63` | `26.87` | -40,642.26 USD | `-3.91%` | `2X Isolated` |

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
  * 24H Horizon: Short MP=`52.71` (Vol: 3,600,000.00 USD, Dist: `+4.01%`) | Long MP=`50.59` (Vol: 2,100,000.00 USD, Dist: `--0.17%`)
  * 48H Horizon: Short MP=`54.87` (Vol: 4,200,000.00 USD, Dist: `+8.26%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.15%`)
  * 3D Horizon: Short MP=`54.97` (Vol: 5,200,000.00 USD, Dist: `+8.46%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.15%`)
  * 7D Horizon: Short MP=`55.07` (Vol: 7,700,000.00 USD, Dist: `+8.67%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.15%`)
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
  * Current Rate: `44.14K` | Last 24h: `158.28K` | Last 3d: `386.46K` | Last 7d: `548.84K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0077%` | **USDT BingX** | `-` |
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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `50.91` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.64` (Risk Distance: `0.2710` pts)
  * +2.5R Take Profit: `51.58`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.34` (Risk Distance: `0.2710` pts)
  * +2.5R Take Profit: `51.39`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`65.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
