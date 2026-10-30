# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGUSD
**Canonical Key**: `XAGUSD` | **Broker Instrument**: `XAGUSD.pi` | **Asset Class**: `Precious Metal`
**Timestamp**: `2026-10-30 16:12:33 IST` (`2026-10-30 10:42:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `50.57` | **Live Ask Quote**: `50.61` | **Mid Price**: `50.59`
- **Spread Points**: `36.00` | **Spread BPS**: `7.12 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `51.19` | VWAP Z-Score: `-1.78` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1932` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.09` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.31` | Lower -3.00σ Band: `50.08`
  * Upper +2.51σ Band: `52.13` | Lower -2.51σ Band: `50.26`
  * Upper +2.01σ Band: `51.94` | Lower -2.01σ Band: `50.45`
  * Upper +2.00σ Band: `51.94` | Lower -2.00σ Band: `50.45`
  * Upper +1.28σ Band: `51.67` | Lower -1.28σ Band: `50.72`
  * Upper +1.00σ Band: `51.57` | Lower -1.00σ Band: `50.82`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`50.69` | EMA-20=`50.84` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.24` (Slope: `+0.0000`) | EMA-100=`51.76`
  * Institutional Anchors: EMA-144=`52.09` | EMA-200=`52.43` (Slope: `-0.4168`) | EMA-233=`52.63`
- **Range Boundaries**: 24H High=`53.07` | 24H Low=`50.40` | Weekly High=`54.61` | Weekly Low=`50.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.07` (Distance: `-2.85%`)
  * Point of Control (POC) = `51.44` (Distance: `-1.66%`)
  * Value Area Low (VAL) = `50.89` (Distance: `-0.60%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `50.39` - `50.79`
  * Optimal Trade Entry (OTE 0.705): `50.69`
  * Structural Invalidation Anchor (0.786): `50.99`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `50.65` | `50.67` | `50.58` | `50.60` | `868` | 43,919.06 USD | -24,320.77 USD | `-55.38%` | -1,317,702.06 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `50.60` | `50.74` | `50.57` | `50.73` | `849` | 43,071.47 USD | 36,149.27 USD | `+83.93%` | -1,281,552.79 USD | `+1.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `50.73` | `50.74` | `50.64` | `50.67` | `825` | 41,806.05 USD | -19,868.22 USD | `-47.52%` | -1,301,421.01 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `50.78` | `50.82` | `50.68` | `50.79` | `3,277` | 166,435.55 USD | 54,875.49 USD | `+32.97%` | -1,898,652.78 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `50.79` | `50.87` | `50.64` | `50.65` | `2,364` | 119,727.14 USD | -95,249.59 USD | `-79.56%` | -1,993,902.38 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `50.65` | `50.74` | `50.57` | `50.67` | `2,542` | 128,813.31 USD | 22,485.16 USD | `+17.46%` | -1,971,417.21 USD | `+0.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `BID` | `50.59` | `5833.1600` | 295,128.73 USD | 1,510,576.79 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `50.60` | `764.7300` | 38,699.16 USD | 597,779.57 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `50.60` | `175.4400` | 8,877.97 USD | 606,657.54 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `50.60` | `3096.0600` | 156,669.92 USD | 763,327.46 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `50.60` | `642.5900` | 32,516.34 USD | 795,843.80 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `50.60` | `6374.6900` | 322,559.31 USD | 1,118,403.12 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `50.60` | `4.7400` | 239.84 USD | 1,118,642.96 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `50.60` | `1913.2200` | 96,805.11 USD | 1,215,448.06 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `50.61` | `460.9500` | 23,330.52 USD | 42,257.39 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `50.61` | `65.2300` | 3,301.49 USD | 45,558.88 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `50.61` | `763.0200` | 38,617.97 USD | 84,176.85 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `50.61` | `2029.6500` | 102,722.62 USD | 186,899.46 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `50.61` | `236.8300` | 11,985.97 USD | 198,885.43 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `50.61` | `76.5400` | 3,873.61 USD | 202,759.04 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `50.61` | `1191.7900` | 60,314.11 USD | 263,073.15 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `50.61` | `5683.7100` | 287,635.51 USD | 550,708.66 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `50.61` | `165.4300` | 8,371.75 USD | 559,080.41 USD | `2 orders` | `-0.02%` | `-` |
| `ASK` | `50.62` | `70.6100` | 3,574.63 USD | 120,119.48 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `50.62` | `1441.2500` | 72,960.40 USD | 116,544.85 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `50.62` | `331.7400` | 16,793.34 USD | 43,584.45 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `50.62` | `183.6700` | 9,297.38 USD | 26,791.11 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `50.62` | `154.1300` | 7,801.91 USD | 17,493.73 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `50.62` | `191.4700` | 9,691.83 USD | 9,691.83 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `50.62` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 50.62` | `0.00%` | `-` |
| `BID` | `50.62` | `194.6300` | 9,851.59 USD | 9,851.59 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `50.62` | `12.7900` | 647.38 USD | 10,498.97 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `50.62` | `166.5100` | 8,427.90 USD | 18,926.87 USD | `3 orders` | `-0.00%` | `-` |
| `ASK` | `50.63` | `4.7400` | 240.01 USD | 491,667.01 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.63` | `10.0000` | 506.34 USD | 491,427.00 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.63` | `104.8800` | 5,310.39 USD | 490,920.66 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `50.63` | `1922.2800` | 97,328.88 USD | 485,610.27 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `50.63` | `3525.7700` | 178,513.26 USD | 388,281.39 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `50.63` | `225.9700` | 11,440.86 USD | 209,768.13 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `50.63` | `96.7300` | 4,897.34 USD | 198,327.27 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `50.63` | `954.3600` | 48,316.38 USD | 193,429.92 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `50.63` | `493.7000` | 24,994.06 USD | 145,113.54 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `50.64` | `1193.9400` | 60,461.12 USD | 1,210,529.38 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.64` | `902.9500` | 45,724.49 USD | 1,150,068.26 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `50.64` | `5924.4100` | 300,000.27 USD | 1,104,343.78 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `50.64` | `5779.7600` | 292,669.71 USD | 804,343.50 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `50.64` | `395.1100` | 20,006.79 USD | 511,673.80 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `115` | `0x5b5d...c060` | `SHORT` | 17,523,750.66 USD | `346,127.65` | `58.90` | `50.64` | `494.25` | 2,862,609.43 USD | `+16.34%` | `5X Cross` |
| `123` | `0x4692...164f` | `SHORT` | 15,686,113.88 USD | `309,763.50` | `52.21` | `50.64` | `259.05` | 486,793.07 USD | `+3.10%` | `5X Cross` |
| `207` | `0xacb6...efbd` | `SHORT` | 10,181,168.03 USD | `201,133.33` | `59.63` | `50.64` | `77.11` | 1,811,489.08 USD | `+17.79%` | `6X Cross` |
| `244` | `0xc26c...b8f4` | `LONG` | 9,190,032.94 USD | `181,463.41` | `55.43` | `50.64` | `0.000000` | -868,722.14 USD | `-9.45%` | `2X Cross` |
| `275` | `0x49e9...e1d0` | `SHORT` | 8,396,233.31 USD | `165,789.30` | `55.17` | `50.64` | `99.54` | 751,201.71 USD | `+8.95%` | `4X Cross` |
| `356` | `0x645b...87b8` | `LONG` | 6,509,977.53 USD | `128,576.91` | `56.54` | `50.64` | `0.000000` | -760,091.71 USD | `-11.68%` | `3X Cross` |
| `361` | `0xd8c5...99b0` | `SHORT` | 6,397,352.11 USD | `126,320.04` | `61.98` | `50.64` | `198.24` | 1,431,985.74 USD | `+22.38%` | `3X Cross` |
| `395` | `0xe9ff...5903` | `SHORT` | 5,720,539.55 USD | `112,996.08` | `60.07` | `50.64` | `175.02` | 1,067,411.26 USD | `+18.66%` | `5X Cross` |
| `720` | `0x9aa5...58af` | `LONG` | 3,123,388.54 USD | `61,657.59` | `61.59` | `50.64` | `0.000000` | -674,340.14 USD | `-21.59%` | `20X Cross` |
| `752` | `0x2056...8396` | `LONG` | 3,039,420.00 USD | `60,000.00` | `66.92` | `50.64` | `21.36` | -975,907.14 USD | `-32.11%` | `10X Cross` |
| `854` | `0xfc66...ca06` | `SHORT` | 2,635,258.64 USD | `52,035.99` | `50.62` | `50.64` | `404.29` | -1,431.37 USD | `-0.05%` | `7X Cross` |
| `878` | `0x0242...ffa1` | `SHORT` | 2,528,528.92 USD | `49,916.67` | `56.48` | `50.64` | `329.41` | 290,602.95 USD | `+11.49%` | `10X Cross` |
| `885` | `0x960b...f0fc` | `LONG` | 2,505,540.25 USD | `49,457.96` | `55.82` | `50.64` | `0.000000` | -255,396.78 USD | `-10.19%` | `25X Cross` |
| `972` | `0x8b9d...7b28` | `LONG` | 2,270,353.58 USD | `44,823.47` | `58.35` | `50.64` | `0.000000` | -345,094.97 USD | `-15.20%` | `10X Cross` |
| `1061` | `0x5647...e7de` | `LONG` | 2,038,307.56 USD | `40,262.07` | `57.38` | `50.64` | `0.000000` | -271,930.04 USD | `-13.34%` | `20X Cross` |
| `1071` | `0xa2ce...3126` | `LONG` | 2,026,040.00 USD | `40,000.00` | `74.30` | `50.64` | `0.000000` | -946,015.49 USD | `-46.69%` | `20X Cross` |
| `1094` | `0xb078...de15` | `SHORT` | 1,975,545.51 USD | `39,000.01` | `52.58` | `50.64` | `208.08` | 74,973.45 USD | `+3.80%` | `8X Cross` |
| `1427` | `0x3678...b209` | `LONG` | 1,519,440.00 USD | `30,000.00` | `57.15` | `50.64` | `0.000000` | -195,060.00 USD | `-12.84%` | `20X Cross` |
| `1429` | `0x5a88...d997` | `LONG` | 1,519,050.00 USD | `30,000.00` | `59.50` | `50.64` | `37.99` | -265,837.59 USD | `-17.50%` | `25X Cross` |
| `1617` | `0xed62...e004` | `SHORT` | 1,299,650.47 USD | `25,660.45` | `50.81` | `50.64` | `54.72` | 4,156.99 USD | `+0.32%` | `25X Cross` |
| `1655` | `0x7ea9...fc7f` | `LONG` | 1,266,275.00 USD | `25,000.00` | `53.60` | `50.64` | `35.38` | -73,729.05 USD | `-5.82%` | `25X Cross` |
| `1794` | `0xf517...c032` | `LONG` | 1,145,924.48 USD | `22,627.50` | `66.29` | `50.64` | `0.000000` | -354,070.62 USD | `-30.90%` | `20X Cross` |
| `1802` | `0x24fb...ed0f` | `LONG` | 1,141,891.99 USD | `22,555.00` | `51.37` | `50.64` | `0.000000` | -16,774.59 USD | `-1.47%` | `20X Cross` |
| `1840` | `0x9e11...22a3` | `LONG` | 1,111,674.12 USD | `21,945.99` | `50.67` | `50.64` | `34.46` | -248.28 USD | `-0.02%` | `3X Isolated` |
| `1928` | `0xcc9f...d218` | `LONG` | 1,038,732.25 USD | `20,520.60` | `52.63` | `50.64` | `26.87` | -41,175.80 USD | `-3.96%` | `2X Isolated` |

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
  * 24H Horizon: Short MP=`52.71` (Vol: 3,600,000.00 USD, Dist: `+3.86%`) | Long MP=`50.59` (Vol: 2,100,000.00 USD, Dist: `--0.31%`)
  * 48H Horizon: Short MP=`54.87` (Vol: 4,200,000.00 USD, Dist: `+8.11%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.29%`)
  * 3D Horizon: Short MP=`54.97` (Vol: 5,200,000.00 USD, Dist: `+8.32%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.29%`)
  * 7D Horizon: Short MP=`55.07` (Vol: 7,100,000.00 USD, Dist: `+8.52%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.29%`)
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
  * Current Rate: `44.45K` | Last 24h: `158.28K` | Last 3d: `386.46K` | Last 7d: `548.84K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0082%` | **USDT BingX** | `-` |
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `50.89` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.61` (Risk Distance: `0.2859` pts)
  * +2.5R Take Profit: `51.61`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.36` (Risk Distance: `0.2859` pts)
  * +2.5R Take Profit: `51.36`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`50.99`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
