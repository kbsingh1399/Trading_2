# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGUSD
**Canonical Key**: `XAGUSD` | **Broker Instrument**: `XAGUSD.pi` | **Asset Class**: `Precious Metal`
**Timestamp**: `2026-10-30 01:20:51 IST` (`2026-10-29 19:50:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `52.12` | **Live Ask Quote**: `52.16` | **Mid Price**: `52.14`
- **Spread Points**: `36.00` | **Spread BPS**: `6.90 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `52.75` | VWAP Z-Score: `-1.13` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2001` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.08` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.38` | Lower -3.00σ Band: `51.13`
  * Upper +2.51σ Band: `54.11` | Lower -2.51σ Band: `51.39`
  * Upper +2.01σ Band: `53.84` | Lower -2.01σ Band: `51.67`
  * Upper +2.00σ Band: `53.84` | Lower -2.00σ Band: `51.67`
  * Upper +1.28σ Band: `53.45` | Lower -1.28σ Band: `52.06`
  * Upper +1.00σ Band: `53.29` | Lower -1.00σ Band: `52.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.11` | EMA-20=`52.22` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.50` (Slope: `+0.0000`) | EMA-100=`52.86`
  * Institutional Anchors: EMA-144=`53.05` | EMA-200=`53.22` (Slope: `-0.2592`) | EMA-233=`53.29`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.95` | Weekly High=`54.61` | Weekly Low=`51.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.96` (Distance: `-1.54%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.60%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.30%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.22`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `51.93` - `52.35`
  * Optimal Trade Entry (OTE 0.705): `52.25`
  * Structural Invalidation Anchor (0.786): `52.56`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.40` | `52.43` | `52.34` | `52.34` | `1,390` | 72,759.55 USD | -49,033.61 USD | `-67.39%` | -631,417.17 USD | `-0.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `52.34` | `52.36` | `52.29` | `52.34` | `1,176` | 61,554.19 USD | 11,597.17 USD | `+18.84%` | -619,820.01 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `52.34` | `52.43` | `52.34` | `52.40` | `1,135` | 59,471.73 USD | 25,259.50 USD | `+42.47%` | -594,560.51 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.51` | `52.51` | `52.26` | `52.39` | `5,381` | 281,915.97 USD | -53,564.03 USD | `-19.00%` | -1,383,024.73 USD | `-0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.39` | `52.48` | `52.35` | `52.40` | `4,100` | 214,823.60 USD | -25,957.85 USD | `-12.08%` | -1,408,982.58 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `52.40` | `52.43` | `52.29` | `52.40` | `3,701` | 193,925.00 USD | 50,559.02 USD | `+26.07%` | -1,358,423.56 USD | `+0.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.24` | `52.76` | `52.03` | `52.61` | `32,755` | 1,723,273.30 USD | 951,587.73 USD | `+55.22%` | -679,727.93 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.61` | `52.65` | `52.32` | `52.51` | `20,260` | 1,063,771.56 USD | -103,422.23 USD | `-9.72%` | -783,150.17 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `52.51` | `52.51` | `52.26` | `52.42` | `15,925` | 834,740.72 USD | -28,381.18 USD | `-3.40%` | -811,531.35 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
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
| `BID` | `52.15` | `38.1300` | 1,988.63 USD | 760,184.52 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.15` | `10.0000` | 521.53 USD | 760,706.05 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.15` | `311.9200` | 16,267.25 USD | 776,973.30 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.15` | `75.6000` | 3,942.62 USD | 780,915.92 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.15` | `19.3400` | 1,008.58 USD | 781,924.50 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.15` | `523.4800` | 27,298.96 USD | 809,223.46 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.15` | `985.5100` | 51,392.38 USD | 860,615.84 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `52.15` | `4.7400` | 247.18 USD | 860,863.01 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.15` | `80.3500` | 4,189.93 USD | 865,052.94 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.15` | `6176.1900` | 322,057.43 USD | 1,187,110.37 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.16` | `64.3100` | 3,354.73 USD | 3,354.73 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.16` | `283.0600` | 14,765.54 USD | 18,120.27 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `52.16` | `380.3500` | 19,840.20 USD | 37,960.47 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `52.16` | `1894.1300` | 98,799.71 USD | 136,760.18 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `52.16` | `185.1400` | 9,656.90 USD | 146,417.09 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.16` | `152.2200` | 7,939.64 USD | 154,356.73 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.16` | `315.6500` | 16,463.67 USD | 170,820.40 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `52.16` | `804.2800` | 41,948.83 USD | 212,769.24 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.16` | `5833.9500` | 304,275.50 USD | 517,044.73 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `52.16` | `4623.7400` | 241,151.16 USD | 758,195.89 USD | `3 orders` | `-0.02%` | `-` |
| `ASK` | `52.17` | `2004.8600` | 104,603.57 USD | 220,328.34 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `52.17` | `1119.4800` | 58,407.75 USD | 115,724.77 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.17` | `464.1200` | 24,214.53 USD | 57,317.02 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.17` | `75.9900` | 3,964.55 USD | 33,102.49 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.17` | `205.8500` | 10,739.40 USD | 29,137.94 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `52.17` | `47.3500` | 2,470.25 USD | 18,398.54 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.17` | `170.2900` | 8,883.69 USD | 15,928.29 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.17` | `100.6500` | 5,250.61 USD | 7,044.60 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.17` | `34.3900` | 1,793.99 USD | 1,793.99 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.17` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.17` | `0.00%` | `-` |
| `ASK` | `52.18` | `56.7900` | 2,963.53 USD | 1,061,236.94 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.18` | `2959.6400` | 154,442.89 USD | 1,058,273.41 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.18` | `1486.5200` | 77,569.59 USD | 903,830.52 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `52.18` | `184.1500` | 9,609.13 USD | 826,260.93 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.18` | `3879.7900` | 202,447.44 USD | 816,651.80 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.18` | `5804.4200` | 302,868.83 USD | 614,204.36 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.18` | `749.8200` | 39,124.11 USD | 311,335.53 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `52.18` | `308.1500` | 16,078.34 USD | 272,211.42 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.18` | `686.2300` | 35,804.74 USD | 256,133.08 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.19` | `24.3100` | 1,268.64 USD | 1,070,278.02 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.19` | `148.9400` | 7,772.43 USD | 1,069,009.37 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,409,834.47 USD | `333,790.30` | `59.15` | `52.16` | `536.05` | 2,333,199.48 USD | `+13.40%` | `5X Cross` |
| `125` | `0x4692...164f` | `SHORT` | 16,255,899.76 USD | `311,654.52` | `53.36` | `52.16` | `240.41` | 373,700.79 USD | `+2.30%` | `5X Cross` |
| `177` | `0x49e9...e1d0` | `SHORT` | 11,690,759.02 USD | `224,132.65` | `55.61` | `52.16` | `87.38` | 772,287.57 USD | `+6.61%` | `4X Cross` |
| `208` | `0xacb6...efbd` | `SHORT` | 10,494,332.63 USD | `201,133.33` | `59.63` | `52.16` | `76.46` | 1,498,324.49 USD | `+14.28%` | `6X Cross` |
| `247` | `0xc26c...b8f4` | `LONG` | 9,464,768.54 USD | `181,463.41` | `55.43` | `52.16` | `0.000000` | -593,986.54 USD | `-6.28%` | `2X Cross` |
| `362` | `0x645b...87b8` | `LONG` | 6,588,074.89 USD | `126,309.96` | `56.63` | `52.16` | `0.000000` | -565,405.99 USD | `-8.58%` | `3X Cross` |
| `363` | `0xd8c5...99b0` | `SHORT` | 6,587,211.13 USD | `126,320.04` | `61.98` | `52.16` | `194.71` | 1,242,126.72 USD | `+18.86%` | `3X Cross` |
| `401` | `0xe9ff...5903` | `SHORT` | 5,894,440.51 USD | `112,996.08` | `60.07` | `52.16` | `196.87` | 893,510.29 USD | `+15.16%` | `5X Cross` |
| `432` | `0xfc66...ca06` | `SHORT` | 5,408,156.40 USD | `103,683.98` | `54.61` | `52.16` | `435.99` | 253,624.13 USD | `+4.69%` | `3X Cross` |
| `629` | `0x9aa5...58af` | `LONG` | 3,717,197.20 USD | `71,243.43` | `61.59` | `52.16` | `0.000000` | -670,960.32 USD | `-18.05%` | `20X Cross` |
| `750` | `0x2056...8396` | `LONG` | 3,130,560.00 USD | `60,000.00` | `66.92` | `52.16` | `21.34` | -884,767.14 USD | `-28.26%` | `10X Cross` |
| `758` | `0x354b...6425` | `LONG` | 3,100,522.36 USD | `59,442.53` | `52.43` | `52.16` | `0.000000` | -15,954.14 USD | `-0.51%` | `10X Cross` |
| `868` | `0x4e23...20c3` | `SHORT` | 2,637,566.99 USD | `50,540.69` | `52.44` | `52.16` | `304.06` | 12,938.42 USD | `+0.49%` | `16X Cross` |
| `875` | `0x0242...ffa1` | `SHORT` | 2,603,553.67 USD | `49,916.67` | `56.48` | `52.16` | `280.71` | 215,578.19 USD | `+8.28%` | `10X Cross` |
| `886` | `0x960b...f0fc` | `LONG` | 2,579,727.19 USD | `49,457.96` | `55.82` | `52.16` | `0.000000` | -181,209.84 USD | `-7.02%` | `25X Cross` |
| `977` | `0x8b9d...7b28` | `LONG` | 2,338,037.02 USD | `44,823.47` | `58.35` | `52.16` | `0.000000` | -277,411.53 USD | `-11.87%` | `10X Cross` |
| `1070` | `0x5647...e7de` | `LONG` | 2,100,552.72 USD | `40,262.07` | `57.38` | `52.16` | `0.000000` | -209,684.88 USD | `-9.98%` | `20X Cross` |
| `1079` | `0xa2ce...3126` | `LONG` | 2,087,280.00 USD | `40,000.00` | `74.30` | `52.16` | `0.000000` | -884,775.49 USD | `-42.39%` | `20X Cross` |
| `1453` | `0x5a88...d997` | `LONG` | 1,564,500.00 USD | `30,000.00` | `59.50` | `52.16` | `37.70` | -220,387.59 USD | `-14.09%` | `25X Cross` |
| `1454` | `0x3678...b209` | `LONG` | 1,564,410.00 USD | `30,000.00` | `57.15` | `52.16` | `0.000000` | -150,090.00 USD | `-9.59%` | `20X Cross` |
| `1677` | `0x7ea9...fc7f` | `LONG` | 1,304,025.00 USD | `25,000.00` | `53.60` | `52.16` | `18.27` | -35,979.05 USD | `-2.76%` | `25X Cross` |
| `1799` | `0xf517...c032` | `LONG` | 1,180,861.34 USD | `22,627.50` | `66.29` | `52.16` | `0.000000` | -319,133.76 USD | `-27.03%` | `20X Cross` |
| `1802` | `0xce97...7e78` | `LONG` | 1,179,483.87 USD | `22,605.87` | `52.21` | `52.16` | `0.000000` | -810.81 USD | `-0.07%` | `5X Cross` |
| `1920` | `0xcc9f...d218` | `LONG` | 1,070,682.83 USD | `20,520.60` | `52.63` | `52.16` | `26.86` | -9,225.22 USD | `-0.86%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `81.27` | 429.11 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.43K USD at 81.2710 USD [API] | `2026-02-01 23:01:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.52` (Vol: 3,600,000.00 USD, Dist: `+2.39%`) | Long MP=`51.68` (Vol: 2,700,000.00 USD, Dist: `--1.13%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.38%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.13%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.38%`) | Long MP=`51.96` (Vol: 4,000,000.00 USD, Dist: `--0.60%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+4.89%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.60%`)
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
  * Current Rate: `66.64K` | Last 24h: `163.44K` | Last 3d: `421.23K` | Last 7d: `760.43K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0115%` | **USDT BingX** | `-` |
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
  * `2026-10-30 00:57:53 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:19:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `51.69` (Risk Distance: `0.2941` pts)
  * +2.5R Take Profit: `52.72`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.96` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.25` (Risk Distance: `0.2941` pts)
  * +2.5R Take Profit: `52.22`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`52.56`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
