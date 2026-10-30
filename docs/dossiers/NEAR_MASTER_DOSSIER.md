# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:38:27 IST` (`2026-10-30 06:08:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.17` | **Live Ask Quote**: `4.20` | **Mid Price**: `4.18`
- **Spread Points**: `30.00` | **Spread BPS**: `71.74 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `4.05` | VWAP Z-Score: `+1.35` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0508` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `53.95` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.33` | Lower -3.00σ Band: `3.76`
  * Upper +2.51σ Band: `4.29` | Lower -2.51σ Band: `3.81`
  * Upper +2.01σ Band: `4.24` | Lower -2.01σ Band: `3.86`
  * Upper +2.00σ Band: `4.24` | Lower -2.00σ Band: `3.86`
  * Upper +1.28σ Band: `4.17` | Lower -1.28σ Band: `3.93`
  * Upper +1.00σ Band: `4.14` | Lower -1.00σ Band: `3.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.19` | EMA-20=`4.15` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.19` (Slope: `+0.0000`) | EMA-100=`4.28`
  * Institutional Anchors: EMA-144=`4.34` | EMA-200=`4.39` (Slope: `-0.6117`) | EMA-233=`4.42`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.15` (Distance: `+0.81%`)
  * Point of Control (POC) = `4.09` (Distance: `+2.20%`)
  * Value Area Low (VAL) = `3.96` (Distance: `+5.76%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.69` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.27` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.21` | Low=`4.16`
  * Initial Balance (First Hour): IB High=`4.27` | IB Low=`4.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.17` - `4.20`
  * Optimal Trade Entry (OTE 0.705): `4.19`
  * Structural Invalidation Anchor (0.786): `4.22`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.26` | `4.27` | `4.25` | `4.26` | `437,364` | 1,862,347.22 USD | -434,058.56 USD | `-23.31%` | -27,784,237.34 USD | `-0.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.26` | `4.26` | `4.24` | `4.24` | `296,117` | 1,259,772.59 USD | -546,727.64 USD | `-43.40%` | -28,330,964.98 USD | `-0.64` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.24` | `4.26` | `4.24` | `4.25` | `392,399` | 1,665,381.30 USD | -304,574.34 USD | `-18.29%` | -28,635,539.32 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.22` | `4.29` | `4.22` | `4.26` | `1,821,158` | 7,750,191.14 USD | -355,382.65 USD | `-4.59%` | -27,108,225.23 USD | `-0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.26` | `4.28` | `4.25` | `4.26` | `1,101,148` | 4,694,349.73 USD | -241,953.55 USD | `-5.15%` | -27,350,178.78 USD | `-0.50` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.26` | `4.27` | `4.24` | `4.25` | `1,126,256` | 4,789,100.62 USD | -1,284,050.31 USD | `-26.81%` | -28,634,229.09 USD | `-1.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4.06` | `4.17` | `4.06` | `4.16` | `6,011,715` | 24,741,893.48 USD | 4,089,779.03 USD | `+16.53%` | -28,096,918.96 USD | `+1.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4.16` | `4.24` | `4.12` | `4.22` | `7,320,214` | 30,649,363.67 USD | 998,131.84 USD | `+3.26%` | -27,098,787.12 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `4.22` | `4.29` | `4.22` | `4.25` | `4,036,839` | 17,183,777.49 USD | -1,895,040.86 USD | `-11.03%` | -28,993,827.99 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -12,896,665.02 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -13,309,029.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.29` | `4.12` | `4.25` | `11,368,776` | 47,883,005.16 USD | -883,254.66 USD | `-1.84%` | -14,192,284.63 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | 3,315,318.08 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -853,625.74 USD | `-1.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -12,896,665.02 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -13,309,029.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.29` | `4.12` | `4.21` | `12,253,366` | 51,628,051.67 USD | -1,941,922.03 USD | `-3.76%` | -15,250,951.99 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `62` | `0x7737...bf66` | `LONG` | 23,621,895.94 USD | `5,640,376.30` | `2.35` | `4.19` | `0.8543` | 10,349,993.12 USD | `+43.82%` | `10X Cross` |
| `106` | `0xefe4...194b` | `SHORT` | 18,874,161.72 USD | `4,507,262.50` | `4.21` | `4.19` | `6.60` | 100,935.00 USD | `+0.53%` | `5X Cross` |
| `134` | `0xb581...6f4f` | `LONG` | 15,080,400.00 USD | `3,600,000.00` | `5.19` | `4.19` | `0.000000` | -3,612,635.22 USD | `-23.96%` | `4X Cross` |
| `214` | `0xdd53...2b13` | `SHORT` | 10,053,006.06 USD | `2,400,202.00` | `2.31` | `4.19` | `28.71` | -4,507,157.50 USD | `-44.83%` | `3X Cross` |
| `269` | `0x77ee...2902` | `LONG` | 8,642,210.07 USD | `2,063,023.10` | `1.93` | `4.19` | `0.000000` | 4,651,014.13 USD | `+53.82%` | `10X Cross` |
| `362` | `0x9df2...c665` | `SHORT` | 6,342,299.56 USD | `1,514,579.00` | `2.36` | `4.19` | `23.94` | -2,762,309.90 USD | `-43.55%` | `10X Cross` |
| `379` | `0xb83d...6e36` | `SHORT` | 6,054,116.23 USD | `1,445,759.10` | `5.19` | `4.19` | `92.18` | 1,455,332.71 USD | `+24.04%` | `3X Cross` |
| `380` | `0x7fda...17d1` | `SHORT` | 6,048,560.35 USD | `1,443,915.10` | `4.28` | `4.19` | `28.95` | 133,518.17 USD | `+2.21%` | `10X Cross` |
| `399` | `0xb46b...538e` | `SHORT` | 5,595,702.40 USD | `1,336,000.00` | `4.33` | `4.19` | `7.43` | 189,161.66 USD | `+3.38%` | `10X Cross` |
| `472` | `0x60b0...991e` | `LONG` | 4,696,706.92 USD | `1,121,307.10` | `5.00` | `4.19` | `0.000000` | -904,717.51 USD | `-19.26%` | `10X Cross` |
| `491` | `0xcac1...26b3` | `SHORT` | 4,495,228.84 USD | `1,073,743.90` | `2.48` | `4.19` | `12.11` | -1,835,285.37 USD | `-40.83%` | `10X Cross` |
| `512` | `0x781e...96b7` | `SHORT` | 4,353,344.26 USD | `1,039,604.60` | `2.45` | `4.19` | `7.48` | -1,809,007.07 USD | `-41.55%` | `10X Cross` |
| `593` | `0x45d2...4029` | `SHORT` | 3,808,112.50 USD | `909,400.00` | `3.26` | `4.19` | `48.20` | -841,962.60 USD | `-22.11%` | `10X Cross` |
| `601` | `0x4cae...7c34` | `LONG` | 3,772,650.68 USD | `900,587.40` | `3.97` | `4.19` | `2.92` | 194,457.89 USD | `+5.15%` | `10X Cross` |
| `828` | `0x005a...61fe` | `LONG` | 2,731,072.76 USD | `652,414.60` | `2.08` | `4.19` | `2.40` | 1,373,541.52 USD | `+50.29%` | `7X Cross` |
| `832` | `0xba5d...a352` | `SHORT` | 2,712,513.64 USD | `647,532.50` | `2.83` | `4.19` | `13.32` | -879,798.70 USD | `-32.43%` | `10X Cross` |
| `845` | `0xb695...a92d` | `SHORT` | 2,677,358.05 USD | `639,231.70` | `4.57` | `4.19` | `44.62` | 246,000.88 USD | `+9.19%` | `10X Cross` |
| `848` | `0xd1dd...9e85` | `SHORT` | 2,671,058.13 USD | `637,621.00` | `4.96` | `4.19` | `18.57` | 492,414.61 USD | `+18.44%` | `10X Cross` |
| `856` | `0x123d...3bff` | `SHORT` | 2,633,596.28 USD | `628,228.40` | `2.09` | `4.19` | `9.16` | -1,322,597.57 USD | `-50.22%` | `10X Cross` |
| `866` | `0xcf53...ee11` | `SHORT` | 2,602,881.14 USD | `621,598.40` | `5.07` | `4.19` | `25.13` | 549,289.11 USD | `+21.10%` | `10X Cross` |
| `993` | `0xbfc7...80b4` | `SHORT` | 2,224,359.00 USD | `531,000.00` | `2.01` | `4.19` | `7.06` | -1,159,159.61 USD | `-52.11%` | `10X Cross` |
| `1260` | `0x0eec...d4c5` | `LONG` | 1,754,171.25 USD | `418,446.90` | `4.01` | `4.19` | `1.18` | 77,601.98 USD | `+4.42%` | `10X Cross` |
| `1298` | `0xe097...d0fe` | `LONG` | 1,674,960.00 USD | `400,000.00` | `5.29` | `4.19` | `0.000000` | -441,827.30 USD | `-26.38%` | `10X Cross` |
| `1433` | `0x6e8f...4364` | `LONG` | 1,512,532.85 USD | `361,210.50` | `3.28` | `4.19` | `3.52` | 328,472.62 USD | `+21.72%` | `10X Cross` |
| `1444` | `0xef96...9383` | `SHORT` | 1,498,310.62 USD | `357,412.90` | `4.50` | `4.19` | `13.98` | 110,951.11 USD | `+7.41%` | `10X Cross` |
| `1466` | `0xdf95...7d72` | `SHORT` | 1,467,330.99 USD | `350,407.40` | `4.23` | `4.19` | `109.24` | 15,703.14 USD | `+1.07%` | `10X Cross` |
| `1470` | `0xcf67...eb24` | `LONG` | 1,465,975.00 USD | `350,000.00` | `1.98` | `4.19` | `1.50` | 774,357.12 USD | `+52.82%` | `10X Cross` |
| `1590` | `0xfc27...9d9d` | `SHORT` | 1,339,990.37 USD | `319,997.70` | `5.01` | `4.19` | `58.60` | 263,552.25 USD | `+19.67%` | `10X Cross` |
| `1591` | `0x089f...a4f8` | `LONG` | 1,335,547.16 USD | `319,043.30` | `4.06` | `4.19` | `0.000000` | 40,690.45 USD | `+3.05%` | `1X Cross` |
| `1637` | `0x17c3...a868` | `LONG` | 1,285,552.85 USD | `306,924.40` | `4.36` | `4.19` | `0.000000` | -53,479.75 USD | `-4.16%` | `3X Cross` |
| `1670` | `0x9836...457e` | `LONG` | 1,256,222.51 USD | `300,000.60` | `4.57` | `4.19` | `1.86` | -115,850.66 USD | `-9.22%` | `10X Cross` |
| `1716` | `0xe065...0f85` | `SHORT` | 1,206,404.86 USD | `288,027.90` | `2.81` | `4.19` | `5.59` | -395,851.74 USD | `-32.81%` | `10X Cross` |
| `1818` | `0x9aa5...58af` | `SHORT` | 1,122,879.98 USD | `268,220.90` | `4.78` | `4.19` | `37.56` | 158,853.84 USD | `+14.15%` | `10X Cross` |
| `1912` | `0xff43...d924` | `LONG` | 1,045,048.68 USD | `249,474.50` | `4.64` | `4.19` | `3.28` | -112,995.00 USD | `-10.81%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.42` | 6,628.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.63K USD at 4.4150 USD [API] | `2026-10-29 03:41:29` |
| `ANNOUNCEMENT` | `INFO` | `4.41` | 371.70 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.37K USD at 4.4092 USD [API] | `2026-10-29 03:25:48` |
| `ANNOUNCEMENT` | `INFO` | `4.41` | 444.01 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.44K USD at 4.4092 USD [API] | `2026-10-29 03:25:48` |
| `ANNOUNCEMENT` | `INFO` | `4.42` | 5,318.83 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.32K USD at 4.4180 USD [API] | `2026-10-29 03:44:11` |
| `ANNOUNCEMENT` | `INFO` | `4.42` | 7,907.78 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.91K USD at 4.4180 USD [API] | `2026-10-29 03:44:11` |
| `ANNOUNCEMENT` | `INFO` | `4.42` | 9,240.69 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.24K USD at 4.4180 USD [API] | `2026-10-29 03:44:11` |
| `ANNOUNCEMENT` | `INFO` | `4.42` | 249.08 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.25K USD at 4.4163 USD [API] | `2026-10-29 03:25:38` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 6,181.45 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.18K USD at 4.4551 USD [API] | `2026-10-29 04:47:00` |
| `ANNOUNCEMENT` | `INFO` | `4.52` | 19.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.02K USD at 4.5161 USD [API] | `2026-10-29 01:49:08` |
| `ANNOUNCEMENT` | `INFO` | `4.52` | 3,028.05 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 3.03K USD at 4.5161 USD [API] | `2026-10-29 01:49:08` |
| `ANNOUNCEMENT` | `INFO` | `4.45` | 9,660.77 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.66K USD at 4.4532 USD [API] | `2026-10-29 04:52:14` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 47,812.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 47.81K USD at 4.4638 USD [API] | `2026-10-29 04:56:34` |
| `ANNOUNCEMENT` | `INFO` | `4.45` | 5,400.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.40K USD at 4.4516 USD [API] | `2026-10-29 04:57:39` |
| `ANNOUNCEMENT` | `INFO` | `4.45` | 9,659.04 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.66K USD at 4.4524 USD [API] | `2026-10-29 04:57:39` |
| `ANNOUNCEMENT` | `INFO` | `5.02` | 2,221.25 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.22K USD at 5.0175 USD [API] | `2026-10-22 05:44:49` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 704.35 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.70K USD at 5.0636 USD [API] | `2026-10-22 04:35:57` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 35.45 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.04K USD at 5.0636 USD [API] | `2026-10-22 04:35:57` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 182.80 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.18K USD at 5.0636 USD [API] | `2026-10-22 04:35:57` |
| `ANNOUNCEMENT` | `INFO` | `4.49` | 6,711.20 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.71K USD at 4.4903 USD [API] | `2026-10-29 05:07:53` |
| `ANNOUNCEMENT` | `INFO` | `4.38` | 9,348.69 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 9.35K USD at 4.3796 USD [API] | `2026-10-24 14:15:20` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 777.25 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.78K USD at 4.6964 USD [API] | `2026-10-23 22:32:04` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 1,299.96 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.30K USD at 4.6964 USD [API] | `2026-10-23 22:32:04` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 1,299.96 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.30K USD at 4.6964 USD [API] | `2026-10-23 22:32:04` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 1,299.96 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.30K USD at 4.6964 USD [API] | `2026-10-23 22:32:04` |
| `ANNOUNCEMENT` | `INFO` | `4.28` | 11,347.17 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 11.35K USD at 4.2847 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `4.29` | 9,011.31 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.01K USD at 4.2862 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 13,684.31 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 13.68K USD at 4.3027 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 11,347.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 11.35K USD at 4.3030 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,010.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.01K USD at 4.3039 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.36` | 9,011.72 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.01K USD at 4.3577 USD [API] | `2026-10-29 06:43:15` |
| `ANNOUNCEMENT` | `INFO` | `4.32` | 9,865.15 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.87K USD at 4.3200 USD [API] | `2026-10-29 07:43:12` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,823.82 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.82K USD at 4.3019 USD [API] | `2026-10-29 07:17:06` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,825.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.83K USD at 4.3027 USD [API] | `2026-10-29 07:17:06` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,825.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.83K USD at 4.3027 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,827.70 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.83K USD at 4.3036 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,829.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.83K USD at 4.3044 USD [API] | `2026-10-29 06:47:16` |
| `ANNOUNCEMENT` | `INFO` | `4.66` | 4,689.17 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 4.69K USD at 4.6612 USD [API] | `2026-10-02 18:20:16` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+3.71%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--8.46%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+3.63%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--8.48%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+3.63%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--8.48%`)
  * 7D Horizon: Short MP=`5.01` (Vol: 953,300.00 USD, Dist: `+17.61%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--8.45%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8450` | 17,780.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 4,820,000.00 USD | 27,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 23,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 484.57 USD | 23,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 23,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 23,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 23,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 84,010.00 USD | 23,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 100.51 USD | 22,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 945.00 USD | 22,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 6,750.00 USD | 22,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 707.53 USD | 22,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 22,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 110.55 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 31,300.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 2,740.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 4,540.00 USD | 22,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 22,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 5,310.00 USD | 22,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 8,400.00 USD | 22,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 16,340.00 USD | 22,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 1,500.00 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 856.24 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 26,620.00 USD | 22,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 17,320.00 USD | 22,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 144.69 USD | 22,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 3,900.00 USD | 22,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 238.78 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 1,290.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 507,290.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,120.00 USD | 22,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 7,130.00 USD | 22,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 15,020.00 USD | 22,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 104,800.00 USD | 22,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 5,090.00 USD | 22,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 1,670.00 USD | 22,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 258.35 USD | 22,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 471.63 USD | 22,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 2,810.00 USD | 22,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 2,830.00 USD | 22,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 5,850.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 73,140.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 21,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 21,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 931.86 USD | 21,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 1,680.00 USD | 21,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 4,710.00 USD | 21,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 33,990.00 USD | 21,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.44` | 17,030.00 USD | 21,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 1,530.00 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 587,440.00 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 512.75 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.49` | 742.50 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 602.00 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 3,980.00 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 327.72 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 6,040.00 USD | 21,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 311.00 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 32,700.00 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 1,980.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 5,300.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 12,450.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 2,330.00 USD | 21,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 1,220.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 7,460.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 5,190.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 113.70 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 683.65 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 5,230.00 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 12,850.00 USD | 21,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 4,110.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 3,580.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 169.96 USD | 21,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,460.00 USD | 21,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 2,790.00 USD | 21,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,250.00 USD | 21,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,470.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 923.02 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 2,360.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 10,190.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 28,360.00 USD | 21,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 984.26 USD | 21,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 76,780.00 USD | 21,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 562,500.00 USD | 21,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 1,880.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,080.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 416.43 USD | 20,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 979.71 USD | 20,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 2,760.00 USD | 20,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 4,110.00 USD | 20,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 1,090.00 USD | 20,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 1,590.00 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 34,960.00 USD | 20,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 456.55 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 2,000.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 1,820.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 926.64 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 27,560.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 20,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 411.00 USD | 20,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 6,070.00 USD | 20,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 39,990.00 USD | 20,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 18,600.00 USD | 20,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 2,970.00 USD | 20,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 9,390.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 12,650.00 USD | 20,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 64,840.00 USD | 20,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 1,540.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 92,580.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 65,640.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 188,590.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 292.32 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 8,170.00 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 217,960.00 USD | 19,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 44,900.00 USD | 19,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 1,200.00 USD | 19,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 9,420.00 USD | 19,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,670.00 USD | 19,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 307,460.00 USD | 19,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 116,500.00 USD | 19,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 339.75 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 380,350.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 4,090.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 3,030.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 11,600.00 USD | 18,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,970.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 4,910.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 30,900.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 10,510.00 USD | 18,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 42,440.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 10,940.00 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 2,520.00 USD | 18,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,570,000.00 USD | 18,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 185,860.00 USD | 17,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 273,510.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 5,750.00 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,700.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 3,010.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 252,240.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 796.46 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 2,760.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 1,110.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 6,000.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 15,360.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 35,080.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 395.71 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 105.36 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 26,190.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 437,910.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 6,410.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 905.27 USD | 15,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 82,690.00 USD | 15,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 15,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 18,360.00 USD | 15,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 28,300.00 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,650.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 16,510.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 1,920.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 90,780.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 5,130.00 USD | 15,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 170,500.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 435,960.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 32,590.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 28,380.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 2,160.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 43,670.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 25,260.00 USD | 14,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 349,980.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 10,760.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 50,500.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 15,730.00 USD | 14,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 104,120.00 USD | 14,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 33,830.00 USD | 14,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 11,060.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,560,000.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 8,780.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,870.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 13,160.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 476,330.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 8,400.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 225,540.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 13,880.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 84,030.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 49,800.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 48,480.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 17,440.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,450.00 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 160,150.00 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 43,620.00 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111,490.00 USD | 10,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 18,560.00 USD | 10,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 11,020.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 21,610.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 20,250.00 USD | 10,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 2,540.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 171,230.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 65,890.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,880.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 45,630.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 8,010.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,110.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 100,200.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 31,130.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 8,180.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 13,150.00 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 23,850.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 54,840.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 38,060.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 3,820.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 245,320.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 6,250.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 2,290.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 33,530.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 146,260.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 56,130.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 19,810.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 5,640.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 49,440.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 868,070.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 14,120.00 USD | 8,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 137,180.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 132,030.00 USD | 8,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 17,060.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 10,720.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 73,390.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 27,090.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,780.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 169,280.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 46,700.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 44,790.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 1,230.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 98,820.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 415,990.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 30,850.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 32,060.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 48,230.00 USD | 7,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 11,010.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 16,340.00 USD | 6,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.47` | 13,960,000.00 USD | 13,960,000.00 USD | 40,560.00 USD | 26,960.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 91,230.00 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.48` | 13,890,000.00 USD | 13,890,000.00 USD | 44,910.00 USD | 13,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 50,130.00 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.49` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 33.52 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 1,310,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.50` | 13,830,000.00 USD | 13,830,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 34,500.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.51` | 13,770,000.00 USD | 13,770,000.00 USD | 3,690.00 USD | 0.00 USD | 122.64 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 42,030.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 13,770,000.00 USD | 13,770,000.00 USD | 15,180.00 USD | 0.00 USD | 40,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 296,250.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 13,710,000.00 USD | 13,710,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 209,090.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 13,480,000.00 USD | 13,480,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 167,840.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 13,390,000.00 USD | 13,390,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 375,150.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 13,160,000.00 USD | 13,160,000.00 USD | 61,170.00 USD | 0.00 USD | 191.07 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 22,250.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 13,100,000.00 USD | 13,100,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 61,150.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 12,900,000.00 USD | 12,900,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 248,010.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 12,620,000.00 USD | 12,620,000.00 USD | 535.75 USD | 18,170.00 USD | 127.05 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 23,000.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 12,600,000.00 USD | 12,600,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 60,200.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 12,490,000.00 USD | 12,490,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 31,960.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 12,350,000.00 USD | 12,350,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 123,450.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 12,130,000.00 USD | 12,130,000.00 USD | 50,840.00 USD | 8,120.00 USD | 482.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 3,960.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 12,080,000.00 USD | 12,080,000.00 USD | 2,410.00 USD | 41,960.00 USD | 118,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 23,090.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 11,910,000.00 USD | 11,910,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 15,510.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 11,820,000.00 USD | 11,820,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 40,280.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.67` | 11,650,000.00 USD | 11,650,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 101,410.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.68` | 11,530,000.00 USD | 11,530,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 183,600.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.69` | 11,530,000.00 USD | 11,530,000.00 USD | 27,750.00 USD | 0.00 USD | 59,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 93,270.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 12,150,000.00 USD | 12,150,000.00 USD | 63,640.00 USD | 4,110.00 USD | 67,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 11,440,000.00 USD | 11,440,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 212,700.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 12,010,000.00 USD | 12,010,000.00 USD | 16,480.00 USD | 0.00 USD | 251.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 11,300,000.00 USD | 11,300,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 72,730.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 12,000,000.00 USD | 12,000,000.00 USD | 18,460.00 USD | 0.00 USD | 330.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 11,170,000.00 USD | 11,170,000.00 USD | 425.03 USD | 0.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 213,580.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 11,980,000.00 USD | 11,980,000.00 USD | 405.02 USD | 11,920.00 USD | 25,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 11,170,000.00 USD | 11,170,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 121,750.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 11,940,000.00 USD | 11,940,000.00 USD | 108,320.00 USD | 56,340.00 USD | 83,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 11,060,000.00 USD | 11,060,000.00 USD | 130,620.00 USD | 40,020.00 USD | 123,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 40,190.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 11,690,000.00 USD | 11,690,000.00 USD | 1,720.00 USD | 0.00 USD | 50,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 10,770,000.00 USD | 10,770,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 191,910.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 11,640,000.00 USD | 11,640,000.00 USD | 1,260.00 USD | 8,310.00 USD | 144.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 10,580,000.00 USD | 10,580,000.00 USD | 32,650.00 USD | 10,110.00 USD | 21,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 70,180.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 11,630,000.00 USD | 11,630,000.00 USD | 48,010.00 USD | 54,910.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 10,520,000.00 USD | 10,520,000.00 USD | 15,340.00 USD | 8,090.00 USD | 22,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 61,240.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 11,530,000.00 USD | 11,530,000.00 USD | 4,250.00 USD | 0.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 10,470,000.00 USD | 10,470,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 32,110.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 11,500,000.00 USD | 11,500,000.00 USD | 4,270.00 USD | 24,440.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 10,310,000.00 USD | 10,310,000.00 USD | 51,640.00 USD | 0.00 USD | 137,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 152,480.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 11,400,000.00 USD | 11,400,000.00 USD | 3,400.00 USD | 0.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 10,120,000.00 USD | 10,120,000.00 USD | 6,530.00 USD | 18,170.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 456,920.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 11,330,000.00 USD | 11,330,000.00 USD | 212,830.00 USD | 0.00 USD | 78,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 10,080,000.00 USD | 10,080,000.00 USD | 5,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 96,110.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 11,040,000.00 USD | 11,040,000.00 USD | 3,240.00 USD | 21,590.00 USD | 115,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 10,070,000.00 USD | 10,070,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 161,990.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 10,900,000.00 USD | 10,900,000.00 USD | 93,470.00 USD | 91,390.00 USD | 114,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 33,630.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 185,530.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 10,600,000.00 USD | 10,600,000.00 USD | 150,080.00 USD | 33,720.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 9,990,000.00 USD | 9,990,000.00 USD | 7,940.00 USD | 33,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 122,450.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 10,380,000.00 USD | 10,380,000.00 USD | 156,570.00 USD | 160,920.00 USD | 545.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 9,950,000.00 USD | 9,950,000.00 USD | 3,390.00 USD | 49,170.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 26,550.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 10,060,000.00 USD | 10,060,000.00 USD | 39,850.00 USD | 46,130.00 USD | 106,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,890,000.00 USD | 9,890,000.00 USD | 5,190.00 USD | 156,620.00 USD | 72,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 164,270.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 9,870,000.00 USD | 9,870,000.00 USD | 3,490.00 USD | 70,020.00 USD | 153,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,650,000.00 USD | 9,650,000.00 USD | 63,710.00 USD | 0.00 USD | 228,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 29,160.00 USD | 930,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 9,640,000.00 USD | 9,640,000.00 USD | 109,330.00 USD | 24,380.00 USD | 228,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 9,360,000.00 USD | 9,360,000.00 USD | 110,160.00 USD | 77,860.00 USD | 101,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 211,110.00 USD | 901,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 9,280,000.00 USD | 9,280,000.00 USD | 446,590.00 USD | 91,430.00 USD | 195,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,070,000.00 USD | 9,070,000.00 USD | 4,240.00 USD | 50,710.00 USD | 84,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 98,420.00 USD | 690,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 8,550,000.00 USD | 8,550,000.00 USD | 32,970.00 USD | 59,980.00 USD | 244,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 8,930,000.00 USD | 8,930,000.00 USD | 274,050.00 USD | 28,250.00 USD | 52,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 20,880.00 USD | 592,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 8,210,000.00 USD | 8,210,000.00 USD | 337,210.00 USD | 120,100.00 USD | 262,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 8,580,000.00 USD | 8,580,000.00 USD | 121,570.00 USD | 67,260.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 14,270.00 USD | 571,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 7,490,000.00 USD | 7,490,000.00 USD | 317,510.00 USD | 8,570.00 USD | 127,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,340,000.00 USD | 8,340,000.00 USD | 85,790.00 USD | 66,710.00 USD | 103,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 7,790.00 USD | 557,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 7,040,000.00 USD | 7,040,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,090,000.00 USD | 8,090,000.00 USD | 30,960.00 USD | 28,720.00 USD | 248.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 151,080.00 USD | 549,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 6,720,000.00 USD | 6,720,000.00 USD | 132,520.00 USD | 53,060.00 USD | 137,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,030,000.00 USD | 8,030,000.00 USD | 75,150.00 USD | 0.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 164,860.00 USD | 398,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 6,400,000.00 USD | 6,400,000.00 USD | 114,710.00 USD | 0.00 USD | 32,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 7,950,000.00 USD | 7,950,000.00 USD | 8,490.00 USD | 0.00 USD | 583.72 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 31,700.00 USD | 233,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 6,250,000.00 USD | 6,250,000.00 USD | 66,520.00 USD | 22,830.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 7,940,000.00 USD | 7,940,000.00 USD | 165,060.00 USD | 0.00 USD | 105.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 160,690.00 USD | 201,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 6,150,000.00 USD | 6,150,000.00 USD | 942.71 USD | 36,470.00 USD | 137,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,770,000.00 USD | 7,770,000.00 USD | 235,890.00 USD | 0.00 USD | 437.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 28,360.00 USD | 40,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 5,970,000.00 USD | 5,970,000.00 USD | 19,950.00 USD | 76,990.00 USD | 94,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 7,540,000.00 USD | 7,540,000.00 USD | 506,280.00 USD | 0.00 USD | 279,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 4,850.00 USD | 12,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 5,780,000.00 USD | 5,780,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 6,750,000.00 USD | 6,750,000.00 USD | 298,270.00 USD | 26,340.00 USD | 79,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.00` | 5,570,000.00 USD | 5,570,000.00 USD | 39,240.00 USD | 17,140.00 USD | 137,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 6,350,000.00 USD | 6,350,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 6,980.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 5,380,000.00 USD | 5,380,000.00 USD | 473.90 USD | 158,450.00 USD | 222,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 5,400,000.00 USD | 5,400,000.00 USD | 368,350.00 USD | 57,440.00 USD | 438,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.02` | 5,000,000.00 USD | 5,000,000.00 USD | 109,790.00 USD | 41,930.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 4,530,000.00 USD | 4,530,000.00 USD | 271,690.00 USD | 156,620.00 USD | 248,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.03` | 4,780,000.00 USD | 4,780,000.00 USD | 38,390.00 USD | 48,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 3,850,000.00 USD | 3,850,000.00 USD | 245,910.00 USD | 0.00 USD | 344,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.04` | 4,700,000.00 USD | 4,700,000.00 USD | 66,450.00 USD | 21,940.00 USD | 183,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 3,260,000.00 USD | 3,260,000.00 USD | 321,230.00 USD | 0.00 USD | 491,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.05` | 4,420,000.00 USD | 4,420,000.00 USD | 347,800.00 USD | 23,720.00 USD | 56.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.06` | 4,050,000.00 USD | 4,050,000.00 USD | 34,760.00 USD | 72,940.00 USD | 386,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 72,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.07` | 3,560,000.00 USD | 3,560,000.00 USD | 242,710.00 USD | 179,680.00 USD | 240,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 287,180.00 USD | 166,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.08` | 2,890,000.00 USD | 2,890,000.00 USD | 68,020.00 USD | 215,680.00 USD | 79,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 237,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.09` | 2,530,000.00 USD | 2,530,000.00 USD | 163,310.00 USD | 27,940.00 USD | 168,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 1,690,000.00 USD | 1,690,000.00 USD | 127,170.00 USD | 137,180.00 USD | 432,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.10` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 58,480.00 USD | 61,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 989,600.00 USD | 989,600.00 USD | 24,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.11` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 60,170.00 USD | 100,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 964,700.00 USD | 964,700.00 USD | 0.00 USD | 0.00 USD | 98,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 709.01 USD | 709.01 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 379,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 865,980.00 USD | 865,980.00 USD | 0.00 USD | 137,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.13` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 310,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 728,040.00 USD | 728,040.00 USD | 0.00 USD | 0.00 USD | 164,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.14` | 1,200,000.00 USD | 1,200,000.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 564,050.00 USD | 564,050.00 USD | 238,150.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.15` | 1,140,000.00 USD | 1,140,000.00 USD | 469,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 235,070.00 USD | 235,070.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.16` | 671,160.00 USD | 671,160.00 USD | 47,820.00 USD | 0.00 USD | 103,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.17` | 520,100.00 USD | 520,100.00 USD | 58,020.00 USD | 94,940.00 USD | 37,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.18` | 329,400.00 USD | 329,400.00 USD | 329,080.00 USD | 0.00 USD | 327.27 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.19` | 204,980.00 USD | 204,980.00 USD | 204,570.00 USD | 0.00 USD | 405.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.19` | 409,960.00 USD | 409,960.00 USD | 204,570.00 USD | 0.00 USD | 405.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.19` | 2,760.00 USD | 2,760.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.19` | 5,520.00 USD | 5,520.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.20` | 549,500.00 USD | 549,500.00 USD | 66,990.00 USD | 0.00 USD | 72,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.20` | 604,830.00 USD | 604,830.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.21` | 859,410.00 USD | 859,410.00 USD | 168,700.00 USD | 98,820.00 USD | 42,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.21` | 689,740.00 USD | 689,740.00 USD | 2,900.00 USD | 0.00 USD | 82,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.22` | 1,400,000.00 USD | 1,400,000.00 USD | 97,990.00 USD | 129,920.00 USD | 308,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.22` | 811,640.00 USD | 811,640.00 USD | 121,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.23` | 2,050,000.00 USD | 2,050,000.00 USD | 1,340.00 USD | 427,200.00 USD | 222,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.23` | 1,100,000.00 USD | 1,100,000.00 USD | 117,530.00 USD | 0.00 USD | 166,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,180,000.00 USD | 2,180,000.00 USD | 631.50 USD | 137,280.00 USD | 341.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.24` | 1,250,000.00 USD | 1,250,000.00 USD | 2,900.00 USD | 52,690.00 USD | 95,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.25` | 2,690,000.00 USD | 2,690,000.00 USD | 4,080.00 USD | 0.00 USD | 501,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,910,000.00 USD | 1,910,000.00 USD | 3,390.00 USD | 223,240.00 USD | 432,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 2,840,000.00 USD | 2,840,000.00 USD | 150,470.00 USD | 0.00 USD | 303.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 2,640,000.00 USD | 2,640,000.00 USD | 2,960.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.26` | 5,950.00 USD | 5,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.27` | 3,710,000.00 USD | 3,710,000.00 USD | 667,120.00 USD | 51,930.00 USD | 152,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 4,440,000.00 USD | 4,440,000.00 USD | 24,810.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,160,000.00 USD | 4,160,000.00 USD | 125,880.00 USD | 41,380.00 USD | 285,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 6,360,000.00 USD | 6,360,000.00 USD | 119,230.00 USD | 497,680.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 29,460.00 USD | 35,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.29` | 4,520,000.00 USD | 4,520,000.00 USD | 156,040.00 USD | 32,690.00 USD | 162,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 6,410,000.00 USD | 6,410,000.00 USD | 5,150.00 USD | 46,530.00 USD | 1,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 290,210.00 USD | 325,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.30` | 4,800,000.00 USD | 4,800,000.00 USD | 65,250.00 USD | 56,980.00 USD | 163,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,880,000.00 USD | 6,880,000.00 USD | 214,920.00 USD | 180,920.00 USD | 79,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,420,000.00 USD | 5,420,000.00 USD | 376,510.00 USD | 50,050.00 USD | 194,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 7,330,000.00 USD | 7,330,000.00 USD | 215,700.00 USD | 53,890.00 USD | 174,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 28,990.00 USD | 354,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 5,880,000.00 USD | 5,880,000.00 USD | 155,370.00 USD | 106,760.00 USD | 197,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 8,060,000.00 USD | 8,060,000.00 USD | 268,260.00 USD | 160,980.00 USD | 306,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 6,600.00 USD | 361,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.33` | 6,460,000.00 USD | 6,460,000.00 USD | 292,220.00 USD | 158,240.00 USD | 126,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 8,250,000.00 USD | 8,250,000.00 USD | 8,950.00 USD | 84,830.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 533.64 USD | 361,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.34` | 7,100,000.00 USD | 7,100,000.00 USD | 273,450.00 USD | 179,610.00 USD | 189,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 8,710,000.00 USD | 8,710,000.00 USD | 9,550.00 USD | 97,260.00 USD | 356,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 4,130.00 USD | 365,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 7,380,000.00 USD | 7,380,000.00 USD | 2,840.00 USD | 94,890.00 USD | 181,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 8,800,000.00 USD | 8,800,000.00 USD | 2,410.00 USD | 0.00 USD | 89,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,210.00 USD | 369,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 7,550,000.00 USD | 7,550,000.00 USD | 86,330.00 USD | 20,830.00 USD | 60,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 8,960,000.00 USD | 8,960,000.00 USD | 10,460.00 USD | 0.00 USD | 144,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 7,860,000.00 USD | 7,860,000.00 USD | 110,040.00 USD | 46,860.00 USD | 157,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 83,560.00 USD | 452,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 8,730,000.00 USD | 8,730,000.00 USD | 250,760.00 USD | 34,500.00 USD | 581,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 6,090.00 USD | 458,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.39` | 9,140,000.00 USD | 9,140,000.00 USD | 37,480.00 USD | 41,380.00 USD | 330,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 9,880,000.00 USD | 9,880,000.00 USD | 252,620.00 USD | 108,260.00 USD | 151,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 193,270.00 USD | 652,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 9,670,000.00 USD | 9,670,000.00 USD | 385,030.00 USD | 47,530.00 USD | 93,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 10,480,000.00 USD | 10,480,000.00 USD | 111,810.00 USD | 26,950.00 USD | 465,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,410.00 USD | 653,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 10,130,000.00 USD | 10,130,000.00 USD | 221,770.00 USD | 130,890.00 USD | 115,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 10,820,000.00 USD | 10,820,000.00 USD | 1,450.00 USD | 65,600.00 USD | 277,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 14,680.00 USD | 668,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 10,240,000.00 USD | 10,240,000.00 USD | 1,080.00 USD | 80,300.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 11,480,000.00 USD | 11,480,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 18,410.00 USD | 686,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 10,440,000.00 USD | 10,440,000.00 USD | 6,140.00 USD | 77,340.00 USD | 114,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 11,760,000.00 USD | 11,760,000.00 USD | 163,540.00 USD | 46,230.00 USD | 75,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 210.22 USD | 686,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 11,220,000.00 USD | 11,220,000.00 USD | 154,690.00 USD | 339,100.00 USD | 292,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 143,990.00 USD | 72,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 87,920.00 USD | 774,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 11,280,000.00 USD | 11,280,000.00 USD | 1,750.00 USD | 50,720.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.45` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 0.00 USD | 141.32 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 2,000.00 USD | 776,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 11,310,000.00 USD | 11,310,000.00 USD | 2,300.00 USD | 24,070.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 12,040,000.00 USD | 12,040,000.00 USD | 3,070.00 USD | 62,110.00 USD | 257.33 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 6.70 USD | 776,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 11,360,000.00 USD | 11,360,000.00 USD | 1,030.00 USD | 25,190.00 USD | 32,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 12,380,000.00 USD | 12,380,000.00 USD | 204,140.00 USD | 135,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.48` | 11,640,000.00 USD | 11,640,000.00 USD | 167,410.00 USD | 86,520.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 12,390,000.00 USD | 12,390,000.00 USD | 1,870.00 USD | 0.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 12,220,000.00 USD | 12,220,000.00 USD | 253,770.00 USD | 155,000.00 USD | 162,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 12,730,000.00 USD | 12,730,000.00 USD | 244,370.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 20,540.00 USD | 797,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 12,800,000.00 USD | 12,800,000.00 USD | 362,590.00 USD | 69,580.00 USD | 149,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 13,300,000.00 USD | 13,300,000.00 USD | 374,250.00 USD | 200,700.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 283.81 USD | 797,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 13,530,000.00 USD | 13,530,000.00 USD | 187,350.00 USD | 223,860.00 USD | 325,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 13,380,000.00 USD | 13,380,000.00 USD | 77,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 389.19 USD | 797,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 14,160,000.00 USD | 14,160,000.00 USD | 287,830.00 USD | 92,260.00 USD | 242,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 13,520,000.00 USD | 13,520,000.00 USD | 2,080.00 USD | 0.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,100.00 USD | 815,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 14,940,000.00 USD | 14,940,000.00 USD | 501,550.00 USD | 0.00 USD | 281,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 14,500,000.00 USD | 14,500,000.00 USD | 439,420.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 15,340,000.00 USD | 15,340,000.00 USD | 12,950.00 USD | 150,600.00 USD | 234,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 816,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 15,480,000.00 USD | 15,480,000.00 USD | 170.61 USD | 34,450.00 USD | 109,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 0.00 USD | 326.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 15,880,000.00 USD | 15,880,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 16,230,000.00 USD | 16,230,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 16,230,000.00 USD | 16,230,000.00 USD | 177,440.00 USD | 70,180.00 USD | 99,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 16,770,000.00 USD | 16,770,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 17,380,000.00 USD | 17,380,000.00 USD | 420,740.00 USD | 99,430.00 USD | 633,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 16,900,000.00 USD | 16,900,000.00 USD | 44,380.00 USD | 0.00 USD | 85,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 18,020,000.00 USD | 18,020,000.00 USD | 454,840.00 USD | 75,460.00 USD | 109,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 18,610,000.00 USD | 18,610,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 18,190,000.00 USD | 18,190,000.00 USD | 54,700.00 USD | 50,860.00 USD | 67,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 18,730,000.00 USD | 18,730,000.00 USD | 3,460.00 USD | 112,080.00 USD | 171.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 18,330,000.00 USD | 18,330,000.00 USD | 66,880.00 USD | 7,560.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 18,730,000.00 USD | 18,730,000.00 USD | 3,350.00 USD | 0.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 18,480,000.00 USD | 18,480,000.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 18,870,000.00 USD | 18,870,000.00 USD | 134,680.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 18,480,000.00 USD | 18,480,000.00 USD | 1,180.00 USD | 0.00 USD | 335.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 19,080,000.00 USD | 19,080,000.00 USD | 213,490.00 USD | 0.00 USD | 272.08 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 990.04 USD | 817,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 18,650,000.00 USD | 18,650,000.00 USD | 118,230.00 USD | 11,270.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 19,600,000.00 USD | 19,600,000.00 USD | 501,930.00 USD | 18,170.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 143.07 USD | 817,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 19,360,000.00 USD | 19,360,000.00 USD | 201,570.00 USD | 52,020.00 USD | 461,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 20,030,000.00 USD | 20,030,000.00 USD | 420,940.00 USD | 0.00 USD | 520.39 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 756.44 USD | 818,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 20,090,000.00 USD | 20,090,000.00 USD | 156,340.00 USD | 299,030.00 USD | 270,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 20,340,000.00 USD | 20,340,000.00 USD | 144,860.00 USD | 18,370.00 USD | 153,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 101.70 USD | 818,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 20,440,000.00 USD | 20,440,000.00 USD | 88,770.00 USD | 0.00 USD | 259,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 20,610,000.00 USD | 20,610,000.00 USD | 59,770.00 USD | 81,340.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 21,300,000.00 USD | 21,300,000.00 USD | 381,910.00 USD | 83,630.00 USD | 452,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 150,890.00 USD | 969,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 20,960,000.00 USD | 20,960,000.00 USD | 137,640.00 USD | 40,000.00 USD | 168,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 21,400,000.00 USD | 21,400,000.00 USD | 2,450.00 USD | 0.00 USD | 89,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 969,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 21,260,000.00 USD | 21,260,000.00 USD | 70,410.00 USD | 85,020.00 USD | 143,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 21,710,000.00 USD | 21,710,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 976,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 22,220,000.00 USD | 22,220,000.00 USD | 361,050.00 USD | 284,360.00 USD | 316,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 22,120,000.00 USD | 22,120,000.00 USD | 178,360.00 USD | 232,800.00 USD | 456.30 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 250.37 USD | 977,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 22,520,000.00 USD | 22,520,000.00 USD | 3,450.00 USD | 188,370.00 USD | 103,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 22,310,000.00 USD | 22,310,000.00 USD | 7,140.00 USD | 0.00 USD | 180,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.73` | 22,610,000.00 USD | 22,610,000.00 USD | 52,120.00 USD | 37,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 22,390,000.00 USD | 22,390,000.00 USD | 59,970.00 USD | 15,660.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 12,500.00 USD | 989,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.74` | 22,710,000.00 USD | 22,710,000.00 USD | 14,750.00 USD | 173,100.00 USD | 130,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 23,250,000.00 USD | 23,250,000.00 USD | 17,340.00 USD | 185,060.00 USD | 342,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 24,600,000.00 USD | 24,600,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 274,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 25,510,000.00 USD | 25,510,000.00 USD | 731,680.00 USD | 73,410.00 USD | 103,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 8,780.00 USD | 998,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 26,640,000.00 USD | 26,640,000.00 USD | 499,950.00 USD | 477,230.00 USD | 152,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 998,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 27,670,000.00 USD | 27,670,000.00 USD | 713,060.00 USD | 249,310.00 USD | 70,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,920.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 29,260,000.00 USD | 29,260,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 29,890,000.00 USD | 29,890,000.00 USD | 400,800.00 USD | 125,900.00 USD | 103,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 4,090.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 32,660,000.00 USD | 32,660,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 34,310,000.00 USD | 34,310,000.00 USD | 822,860.00 USD | 85,680.00 USD | 741,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,540.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 34,800,000.00 USD | 34,800,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 36,830,000.00 USD | 36,830,000.00 USD | 487,940.00 USD | 380,760.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 38,240,000.00 USD | 38,240,000.00 USD | 444,810.00 USD | 162,380.00 USD | 801,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 137.68 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 39,300,000.00 USD | 39,300,000.00 USD | 264,730.00 USD | 136,820.00 USD | 661,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 40,820,000.00 USD | 40,820,000.00 USD | 450,900.00 USD | 266,980.00 USD | 793,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 41,400,000.00 USD | 41,400,000.00 USD | 213,960.00 USD | 100,850.00 USD | 273,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 42,540,000.00 USD | 42,540,000.00 USD | 451,360.00 USD | 145,910.00 USD | 538,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.96` | 488.56 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.96` | 36,060.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,370.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.11` | 57,160.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.20` | 15,040.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 748.46 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 17,380.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 1,050,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 21,390.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 147.23 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 1,710.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 142.44 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 5,410.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 276,410.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 42,690.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 2,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 66,470.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 1,650,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 697.99 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,580.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.64` | 440,450.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 1,630.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 1,770.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.74` | 147.39 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.78` | 2,710.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 270,730.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 7,150.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 319.41 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 104,080.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 325,240.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 13,680.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 357,880.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 24,100.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 1,900.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 526,230.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.36` | 259,720.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.39` | 2,000.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 5,780.00 USD | 7,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 173.47 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 1,220,000.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 40,780.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.57` | 51,390.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 6,040.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 29,860,000.00 USD | 38,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 38,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 38,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 89,430.00 USD | 38,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 9,250.00 USD | 38,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 37,370.00 USD | 38,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 39,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.80` | 722.01 USD | 39,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.82` | 1,700.00 USD | 39,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 39,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 39,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 39,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 39,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 665.27 USD | 39,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.05` | 559.46 USD | 39,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 39,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.12` | 3,780,000.00 USD | 43,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.13` | 1,000.00 USD | 43,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 43,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 43,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 767.66 USD | 43,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 4,850.00 USD | 43,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 9,930,000.00 USD | 53,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.45` | 106,290.00 USD | 53,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 53,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 7,760,000.00 USD | 61,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,570.00 USD | 61,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.57` | 485.67 USD | 61,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 2,640.00 USD | 61,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 11,550.00 USD | 61,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 61,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 26,080.00 USD | 61,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 676.82 USD | 61,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.68` | 61,480.00 USD | 61,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 13,780.00 USD | 61,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 505.87 USD | 61,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 63,970.00 USD | 61,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 33,540.00 USD | 61,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.82` | 93,780.00 USD | 61,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 61,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.89` | 1,670.00 USD | 61,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 61,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 166.47 USD | 61,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 61,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 62,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 63,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 191.79 USD | 63,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.45` | 76,000.00 USD | 63,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8450` | 27,660,000.00 USD | 0.00 USD | 467.96 USD | `-79.84%` | `553.80` |
| `Live` | `Long` | `0.8650` | 27,660,000.00 USD | 0.00 USD | 4,880,000.00 USD | `-79.37%` | `5,640,877.80` |
| `Live` | `Long` | `0.8850` | 22,780,000.00 USD | 0.00 USD | 5,310.00 USD | `-78.89%` | `6,000.00` |
| `Live` | `Long` | `0.8950` | 22,780,000.00 USD | 0.00 USD | 41,280.00 USD | `-78.65%` | `46,121.20` |
| `Live` | `Long` | `0.9050` | 22,740,000.00 USD | 0.00 USD | 292.22 USD | `-78.41%` | `322.90` |
| `Live` | `Long` | `0.9150` | 22,740,000.00 USD | 0.00 USD | 11,510.00 USD | `-78.18%` | `12,575.00` |
| `Live` | `Long` | `0.9450` | 22,720,000.00 USD | 0.00 USD | 945.00 USD | `-77.46%` | `1,000.00` |
| `Live` | `Long` | `0.9650` | 22,720,000.00 USD | 0.00 USD | 965.00 USD | `-76.98%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 22,720,000.00 USD | 0.00 USD | 707.53 USD | `-76.51%` | `718.30` |
| `Live` | `Long` | `0.9950` | 22,720,000.00 USD | 0.00 USD | 154,200.00 USD | `-76.27%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 22,570,000.00 USD | 0.00 USD | 30,990.00 USD | `-76.03%` | `30,836.80` |
| `Live` | `Long` | `1.01` | 22,540,000.00 USD | 0.00 USD | 111.65 USD | `-75.79%` | `110.00` |
| `Live` | `Long` | `1.02` | 22,540,000.00 USD | 0.00 USD | 10,250.00 USD | `-75.55%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 22,530,000.00 USD | 0.00 USD | 5,070.00 USD | `-75.31%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 22,520,000.00 USD | 0.00 USD | 18,530.00 USD | `-75.07%` | `17,728.50` |
| `Live` | `Long` | `1.05` | 22,500,000.00 USD | 0.00 USD | 5,230.00 USD | `-74.84%` | `4,955.90` |
| `Live` | `Long` | `1.06` | 22,500,000.00 USD | 0.00 USD | 8,920.00 USD | `-74.60%` | `8,376.30` |
| `Live` | `Long` | `1.07` | 22,490,000.00 USD | 0.00 USD | 5,310.00 USD | `-74.36%` | `4,939.60` |
| `Live` | `Long` | `1.08` | 22,480,000.00 USD | 0.00 USD | 216.89 USD | `-74.12%` | `199.90` |
| `Live` | `Long` | `1.11` | 22,480,000.00 USD | 0.00 USD | 17,040.00 USD | `-73.40%` | `15,283.90` |
| `Live` | `Long` | `1.12` | 22,470,000.00 USD | 0.00 USD | 856.24 USD | `-73.17%` | `761.10` |
| `Live` | `Long` | `1.14` | 22,460,000.00 USD | 0.00 USD | 5,990.00 USD | `-72.93%` | `5,281.00` |
| `Live` | `Long` | `1.15` | 22,460,000.00 USD | 0.00 USD | 27,720.00 USD | `-72.69%` | `24,210.30` |
| `Live` | `Long` | `1.16` | 22,430,000.00 USD | 0.00 USD | 521.60 USD | `-72.45%` | `451.60` |
| `Live` | `Long` | `1.17` | 22,430,000.00 USD | 0.00 USD | 58,720.00 USD | `-72.21%` | `50,407.00` |
| `Live` | `Long` | `1.18` | 22,370,000.00 USD | 0.00 USD | 40,740.00 USD | `-71.97%` | `34,673.20` |
| `Live` | `Long` | `1.19` | 22,330,000.00 USD | 0.00 USD | 559,930.00 USD | `-71.74%` | `472,515.70` |
| `Live` | `Long` | `1.20` | 21,770,000.00 USD | 0.00 USD | 4,490.00 USD | `-71.50%` | `3,755.60` |
| `Live` | `Long` | `1.21` | 21,770,000.00 USD | 0.00 USD | 722.40 USD | `-71.26%` | `599.50` |
| `Live` | `Long` | `1.23` | 21,770,000.00 USD | 0.00 USD | 13,480.00 USD | `-70.78%` | `11,000.00` |
| `Live` | `Long` | `1.24` | 21,750,000.00 USD | 0.00 USD | 62,580.00 USD | `-70.54%` | `50,671.90` |
| `Live` | `Long` | `1.25` | 21,690,000.00 USD | 0.00 USD | 958.77 USD | `-70.30%` | `770.10` |
| `Live` | `Long` | `1.25` | 21,690,000.00 USD | 0.00 USD | 1,220.00 USD | `-70.07%` | `969.60` |
| `Live` | `Long` | `1.26` | 21,690,000.00 USD | 0.00 USD | 4,090.00 USD | `-69.83%` | `3,233.40` |
| `Live` | `Long` | `1.27` | 21,680,000.00 USD | 0.00 USD | 3,060.00 USD | `-69.59%` | `2,396.70` |
| `Live` | `Long` | `1.28` | 21,680,000.00 USD | 0.00 USD | 169.23 USD | `-69.35%` | `131.70` |
| `Live` | `Long` | `1.29` | 21,680,000.00 USD | 0.00 USD | 3,900.00 USD | `-69.11%` | `3,012.70` |
| `Live` | `Long` | `1.30` | 21,680,000.00 USD | 0.00 USD | 116.80 USD | `-68.87%` | `89.50` |
| `Live` | `Long` | `1.32` | 21,680,000.00 USD | 0.00 USD | 8,110.00 USD | `-68.40%` | `6,120.80` |
| `Live` | `Long` | `1.33` | 21,670,000.00 USD | 0.00 USD | 267.00 USD | `-68.16%` | `200.00` |
| `Live` | `Long` | `1.34` | 21,670,000.00 USD | 0.00 USD | 603.91 USD | `-67.92%` | `449.00` |
| `Live` | `Long` | `1.35` | 21,670,000.00 USD | 0.00 USD | 2,000.00 USD | `-67.68%` | `1,474.80` |
| `Live` | `Long` | `1.38` | 21,670,000.00 USD | 0.00 USD | 13,110.00 USD | `-67.20%` | `9,531.60` |
| `Live` | `Long` | `1.39` | 21,650,000.00 USD | 0.00 USD | 7,620.00 USD | `-66.96%` | `5,504.50` |
| `Live` | `Long` | `1.40` | 21,640,000.00 USD | 0.00 USD | 4,010.00 USD | `-66.73%` | `2,875.40` |
| `Live` | `Long` | `1.41` | 21,640,000.00 USD | 0.00 USD | 412.23 USD | `-66.49%` | `293.40` |
| `Live` | `Long` | `1.42` | 21,640,000.00 USD | 0.00 USD | 4,710.00 USD | `-66.25%` | `3,325.90` |
| `Live` | `Long` | `1.43` | 21,640,000.00 USD | 0.00 USD | 528,850.00 USD | `-66.01%` | `371,121.10` |
| `Live` | `Long` | `1.44` | 21,110,000.00 USD | 0.00 USD | 13,420.00 USD | `-65.77%` | `9,350.00` |
| `Live` | `Long` | `1.45` | 21,090,000.00 USD | 0.00 USD | 1,530.00 USD | `-65.53%` | `1,061.70` |
| `Live` | `Long` | `1.46` | 21,090,000.00 USD | 0.00 USD | 6,020.00 USD | `-65.30%` | `4,138.20` |
| `Live` | `Long` | `1.48` | 21,090,000.00 USD | 0.00 USD | 1,990.00 USD | `-64.82%` | `1,350.00` |
| `Live` | `Long` | `1.50` | 21,080,000.00 USD | 0.00 USD | 1,800.00 USD | `-64.34%` | `1,203.10` |
| `Live` | `Long` | `1.50` | 21,080,000.00 USD | 0.00 USD | 1,400.00 USD | `-64.10%` | `932.00` |
| `Live` | `Long` | `1.51` | 21,080,000.00 USD | 0.00 USD | 454.50 USD | `-63.86%` | `300.00` |
| `Live` | `Long` | `1.52` | 21,080,000.00 USD | 0.00 USD | 509.81 USD | `-63.63%` | `334.30` |
| `Live` | `Long` | `1.53` | 21,080,000.00 USD | 0.00 USD | 279.37 USD | `-63.39%` | `182.00` |
| `Live` | `Long` | `1.55` | 21,080,000.00 USD | 0.00 USD | 348.94 USD | `-62.91%` | `224.40` |
| `Live` | `Long` | `1.56` | 21,080,000.00 USD | 0.00 USD | 21,750.00 USD | `-62.67%` | `13,896.30` |
| `Live` | `Long` | `1.57` | 21,060,000.00 USD | 0.00 USD | 589.52 USD | `-62.43%` | `374.30` |
| `Live` | `Long` | `1.58` | 21,060,000.00 USD | 0.00 USD | 2,210.00 USD | `-62.19%` | `1,396.60` |
| `Live` | `Long` | `1.59` | 21,050,000.00 USD | 0.00 USD | 3,840.00 USD | `-61.96%` | `2,405.60` |
| `Live` | `Long` | `1.60` | 21,050,000.00 USD | 0.00 USD | 13,850.00 USD | `-61.72%` | `8,628.30` |
| `Live` | `Long` | `1.61` | 21,040,000.00 USD | 0.00 USD | 4,940.00 USD | `-61.48%` | `3,058.80` |
| `Live` | `Long` | `1.62` | 21,030,000.00 USD | 0.00 USD | 2,600.00 USD | `-61.24%` | `1,600.00` |
| `Live` | `Long` | `1.64` | 21,030,000.00 USD | 0.00 USD | 2,030.00 USD | `-61.00%` | `1,241.00` |
| `Live` | `Long` | `1.65` | 21,030,000.00 USD | 0.00 USD | 2,040.00 USD | `-60.76%` | `1,240.20` |
| `Live` | `Long` | `1.66` | 21,030,000.00 USD | 0.00 USD | 15,570.00 USD | `-60.52%` | `9,405.00` |
| `Live` | `Long` | `1.68` | 21,010,000.00 USD | 0.00 USD | 2,930.00 USD | `-60.05%` | `1,751.70` |
| `Live` | `Long` | `1.69` | 21,010,000.00 USD | 0.00 USD | 12,850.00 USD | `-59.81%` | `7,624.50` |
| `Live` | `Long` | `1.71` | 20,990,000.00 USD | 0.00 USD | 2,190.00 USD | `-59.33%` | `1,286.10` |
| `Live` | `Long` | `1.73` | 20,990,000.00 USD | 0.00 USD | 6,860.00 USD | `-58.86%` | `3,977.50` |
| `Live` | `Long` | `1.74` | 20,980,000.00 USD | 0.00 USD | 34,310.00 USD | `-58.62%` | `19,777.30` |
| `Live` | `Long` | `1.75` | 20,950,000.00 USD | 0.00 USD | 10,700.00 USD | `-58.14%` | `6,096.20` |
| `Live` | `Long` | `1.76` | 20,940,000.00 USD | 0.00 USD | 8,590.00 USD | `-57.90%` | `4,867.40` |
| `Live` | `Long` | `1.77` | 20,930,000.00 USD | 0.00 USD | 3,470.00 USD | `-57.66%` | `1,953.10` |
| `Live` | `Long` | `1.79` | 20,930,000.00 USD | 0.00 USD | 471.73 USD | `-57.19%` | `262.80` |
| `Live` | `Long` | `1.80` | 20,930,000.00 USD | 0.00 USD | 529.05 USD | `-56.95%` | `293.10` |
| `Live` | `Long` | `1.81` | 20,930,000.00 USD | 0.00 USD | 6,570.00 USD | `-56.71%` | `3,621.40` |
| `Live` | `Long` | `1.83` | 20,920,000.00 USD | 0.00 USD | 37,770.00 USD | `-56.23%` | `20,583.80` |
| `Live` | `Long` | `1.84` | 20,880,000.00 USD | 0.00 USD | 3,350.00 USD | `-55.99%` | `1,817.20` |
| `Live` | `Long` | `1.85` | 20,880,000.00 USD | 0.00 USD | 557,490.00 USD | `-55.75%` | `300,531.20` |
| `Live` | `Long` | `1.86` | 20,320,000.00 USD | 0.00 USD | 35,270.00 USD | `-55.52%` | `18,910.70` |
| `Live` | `Long` | `1.88` | 20,290,000.00 USD | 0.00 USD | 936.19 USD | `-55.28%` | `499.30` |
| `Live` | `Long` | `1.90` | 20,290,000.00 USD | 0.00 USD | 2,080.00 USD | `-54.80%` | `1,100.00` |
| `Live` | `Long` | `1.91` | 20,280,000.00 USD | 0.00 USD | 4,750.00 USD | `-54.56%` | `2,493.70` |
| `Live` | `Long` | `1.93` | 20,280,000.00 USD | 0.00 USD | 8,610.00 USD | `-54.08%` | `4,474.50` |
| `Live` | `Long` | `1.94` | 20,270,000.00 USD | 0.00 USD | 172.99 USD | `-53.85%` | `89.40` |
| `Live` | `Long` | `1.95` | 20,270,000.00 USD | 0.00 USD | 2,740.00 USD | `-53.61%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 20,270,000.00 USD | 0.00 USD | 1,090.00 USD | `-53.37%` | `555.60` |
| `Live` | `Long` | `1.97` | 20,270,000.00 USD | 0.00 USD | 4,090.00 USD | `-53.13%` | `2,082.70` |
| `Live` | `Long` | `1.98` | 20,260,000.00 USD | 0.00 USD | 34,960.00 USD | `-52.89%` | `17,700.10` |
| `Live` | `Long` | `2.00` | 20,230,000.00 USD | 0.00 USD | 1,560.00 USD | `-52.18%` | `777.50` |
| `Live` | `Long` | `2.02` | 20,230,000.00 USD | 0.00 USD | 20,300.00 USD | `-51.94%` | `10,075.80` |
| `Live` | `Long` | `2.02` | 20,200,000.00 USD | 0.00 USD | 6,120.00 USD | `-51.70%` | `3,020.50` |
| `Live` | `Long` | `2.04` | 20,200,000.00 USD | 0.00 USD | 3,810.00 USD | `-51.22%` | `1,863.20` |
| `Live` | `Long` | `2.06` | 20,190,000.00 USD | 0.00 USD | 411.00 USD | `-50.98%` | `200.00` |
| `Live` | `Long` | `2.06` | 20,190,000.00 USD | 0.00 USD | 4,110.00 USD | `-50.75%` | `1,988.50` |
| `Live` | `Long` | `2.08` | 20,190,000.00 USD | 0.00 USD | 41,860.00 USD | `-50.51%` | `20,173.10` |
| `Live` | `Long` | `2.08` | 20,150,000.00 USD | 0.00 USD | 21,400.00 USD | `-50.27%` | `10,261.50` |
| `Live` | `Long` | `2.10` | 20,130,000.00 USD | 0.00 USD | 1,100.00 USD | `-50.03%` | `527.40` |
| `Live` | `Long` | `2.10` | 20,130,000.00 USD | 0.00 USD | 6,090.00 USD | `-49.79%` | `2,894.60` |
| `Live` | `Long` | `2.12` | 20,120,000.00 USD | 0.00 USD | 211,070.00 USD | `-49.55%` | `99,795.30` |
| `Live` | `Long` | `2.12` | 19,910,000.00 USD | 0.00 USD | 73,580.00 USD | `-49.31%` | `34,627.20` |
| `Live` | `Long` | `2.13` | 19,840,000.00 USD | 0.00 USD | 115,670.00 USD | `-49.08%` | `54,179.40` |
| `Live` | `Long` | `2.15` | 19,720,000.00 USD | 0.00 USD | 857.04 USD | `-48.60%` | `397.70` |
| `Live` | `Long` | `2.17` | 19,720,000.00 USD | 0.00 USD | 188,440.00 USD | `-48.36%` | `87,040.30` |
| `Live` | `Long` | `2.17` | 19,530,000.00 USD | 0.00 USD | 439.57 USD | `-48.12%` | `202.10` |
| `Live` | `Long` | `2.19` | 19,530,000.00 USD | 0.00 USD | 1,630.00 USD | `-47.88%` | `747.90` |
| `Live` | `Long` | `2.19` | 19,530,000.00 USD | 0.00 USD | 12,830.00 USD | `-47.64%` | `5,843.40` |
| `Live` | `Long` | `2.21` | 19,520,000.00 USD | 0.00 USD | 42,060.00 USD | `-47.41%` | `19,074.20` |
| `Live` | `Long` | `2.21` | 19,470,000.00 USD | 0.00 USD | 5,490.00 USD | `-47.17%` | `2,477.80` |
| `Live` | `Long` | `2.23` | 19,470,000.00 USD | 0.00 USD | 1,960.00 USD | `-46.93%` | `882.80` |
| `Live` | `Long` | `2.23` | 19,470,000.00 USD | 0.00 USD | 2,450.00 USD | `-46.69%` | `1,097.50` |
| `Live` | `Long` | `2.25` | 19,460,000.00 USD | 0.00 USD | 39,270.00 USD | `-46.45%` | `17,493.60` |
| `Live` | `Long` | `2.25` | 19,420,000.00 USD | 0.00 USD | 115,820.00 USD | `-46.21%` | `51,360.80` |
| `Live` | `Long` | `2.27` | 19,310,000.00 USD | 0.00 USD | 379,690.00 USD | `-45.74%` | `166,896.10` |
| `Live` | `Long` | `2.29` | 18,930,000.00 USD | 0.00 USD | 7,410.00 USD | `-45.50%` | `3,243.30` |
| `Live` | `Long` | `2.29` | 18,920,000.00 USD | 0.00 USD | 2,150.00 USD | `-45.26%` | `936.90` |
| `Live` | `Long` | `2.31` | 18,920,000.00 USD | 0.00 USD | 32,150.00 USD | `-45.02%` | `13,947.20` |
| `Live` | `Long` | `2.31` | 18,890,000.00 USD | 0.00 USD | 1,970.00 USD | `-44.78%` | `849.40` |
| `Live` | `Long` | `2.33` | 18,890,000.00 USD | 0.00 USD | 3,800.00 USD | `-44.31%` | `1,629.40` |
| `Live` | `Long` | `2.35` | 18,880,000.00 USD | 0.00 USD | 9,370.00 USD | `-44.07%` | `3,997.00` |
| `Live` | `Long` | `2.35` | 18,870,000.00 USD | 0.00 USD | 2,690.00 USD | `-43.83%` | `1,142.10` |
| `Live` | `Long` | `2.37` | 18,870,000.00 USD | 0.00 USD | 26,830.00 USD | `-43.59%` | `11,344.40` |
| `Live` | `Long` | `2.38` | 18,840,000.00 USD | 0.00 USD | 38,740.00 USD | `-43.35%` | `16,311.30` |
| `Live` | `Long` | `2.38` | 18,800,000.00 USD | 0.00 USD | 17,970.00 USD | `-43.11%` | `7,535.00` |
| `Live` | `Long` | `2.40` | 18,790,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-42.87%` | `652,648.60` |
| `Live` | `Long` | `2.42` | 17,220,000.00 USD | 0.00 USD | 185,860.00 USD | `-42.40%` | `76,961.80` |
| `Live` | `Long` | `2.42` | 17,040,000.00 USD | 0.00 USD | 273,790.00 USD | `-42.16%` | `112,901.40` |
| `Live` | `Long` | `2.44` | 16,760,000.00 USD | 0.00 USD | 8,140.00 USD | `-41.92%` | `3,343.00` |
| `Live` | `Long` | `2.44` | 16,750,000.00 USD | 0.00 USD | 3,700.00 USD | `-41.68%` | `1,515.10` |
| `Live` | `Long` | `2.46` | 16,750,000.00 USD | 0.00 USD | 1,240.00 USD | `-41.44%` | `504.90` |
| `Live` | `Long` | `2.46` | 16,750,000.00 USD | 0.00 USD | 259,210.00 USD | `-41.20%` | `105,155.00` |
| `Live` | `Long` | `2.48` | 16,490,000.00 USD | 0.00 USD | 336.35 USD | `-40.97%` | `135.90` |
| `Live` | `Long` | `2.48` | 16,490,000.00 USD | 0.00 USD | 2,760.00 USD | `-40.73%` | `1,112.50` |
| `Live` | `Long` | `2.50` | 16,490,000.00 USD | 0.00 USD | 1,110.00 USD | `-40.49%` | `443.10` |
| `Live` | `Long` | `2.50` | 16,490,000.00 USD | 0.00 USD | 18,360.00 USD | `-40.25%` | `7,329.70` |
| `Live` | `Long` | `2.52` | 16,470,000.00 USD | 0.00 USD | 33,060.00 USD | `-39.77%` | `13,093.90` |
| `Live` | `Long` | `2.54` | 16,440,000.00 USD | 0.00 USD | 395.71 USD | `-39.53%` | `156.10` |
| `Live` | `Long` | `2.54` | 16,430,000.00 USD | 0.00 USD | 5,200.00 USD | `-39.30%` | `2,041.40` |
| `Live` | `Long` | `2.56` | 16,430,000.00 USD | 0.00 USD | 145,540.00 USD | `-39.06%` | `56,963.00` |
| `Live` | `Long` | `2.56` | 16,280,000.00 USD | 0.00 USD | 7,890.00 USD | `-38.82%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 16,280,000.00 USD | 0.00 USD | 1,570.00 USD | `-38.58%` | `610.60` |
| `Live` | `Long` | `2.58` | 16,270,000.00 USD | 0.00 USD | 905.27 USD | `-38.34%` | `350.20` |
| `Live` | `Long` | `2.60` | 16,270,000.00 USD | 0.00 USD | 82,690.00 USD | `-38.10%` | `31,866.60` |
| `Live` | `Long` | `2.60` | 16,190,000.00 USD | 0.00 USD | 3,940.00 USD | `-37.87%` | `1,513.80` |
| `Live` | `Long` | `2.62` | 16,190,000.00 USD | 0.00 USD | 2,360.00 USD | `-37.63%` | `901.90` |
| `Live` | `Long` | `2.62` | 16,180,000.00 USD | 0.00 USD | 183,600.00 USD | `-37.39%` | `69,944.50` |
| `Live` | `Long` | `2.63` | 16,000,000.00 USD | 0.00 USD | 24,310.00 USD | `-37.15%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 15,980,000.00 USD | 0.00 USD | 3,950.00 USD | `-36.91%` | `1,491.60` |
| `Live` | `Long` | `2.65` | 15,970,000.00 USD | 0.00 USD | 16,510.00 USD | `-36.67%` | `6,216.80` |
| `Live` | `Long` | `2.67` | 15,960,000.00 USD | 0.00 USD | 1,920.00 USD | `-36.43%` | `721.80` |
| `Live` | `Long` | `2.67` | 15,950,000.00 USD | 0.00 USD | 4,470.00 USD | `-36.20%` | `1,670.60` |
| `Live` | `Long` | `2.69` | 15,950,000.00 USD | 0.00 USD | 4,980.00 USD | `-35.96%` | `1,855.60` |
| `Live` | `Long` | `2.69` | 15,940,000.00 USD | 0.00 USD | 150,740.00 USD | `-35.72%` | `55,932.20` |
| `Live` | `Long` | `2.71` | 15,790,000.00 USD | 0.00 USD | 124,720.00 USD | `-35.48%` | `46,107.40` |
| `Live` | `Long` | `2.71` | 15,670,000.00 USD | 0.00 USD | 11,750.00 USD | `-35.24%` | `4,327.50` |
| `Live` | `Long` | `2.73` | 15,660,000.00 USD | 0.00 USD | 126,890.00 USD | `-35.00%` | `46,564.80` |
| `Live` | `Long` | `2.73` | 15,530,000.00 USD | 0.00 USD | 1,960.00 USD | `-34.76%` | `715.80` |
| `Live` | `Long` | `2.75` | 15,530,000.00 USD | 0.00 USD | 41,060.00 USD | `-34.53%` | `14,958.60` |
| `Live` | `Long` | `2.75` | 15,490,000.00 USD | 0.00 USD | 114,010.00 USD | `-34.29%` | `41,383.20` |
| `Live` | `Long` | `2.77` | 15,370,000.00 USD | 0.00 USD | 351,320.00 USD | `-34.05%` | `127,058.30` |
| `Live` | `Long` | `2.77` | 15,020,000.00 USD | 0.00 USD | 31,180.00 USD | `-33.81%` | `11,235.90` |
| `Live` | `Long` | `2.79` | 14,990,000.00 USD | 0.00 USD | 48,970.00 USD | `-33.57%` | `17,582.90` |
| `Live` | `Long` | `2.79` | 14,940,000.00 USD | 0.00 USD | 20,730.00 USD | `-33.33%` | `7,416.00` |
| `Live` | `Long` | `2.81` | 14,920,000.00 USD | 0.00 USD | 92,700.00 USD | `-33.09%` | `33,047.60` |
| `Live` | `Long` | `2.81` | 14,830,000.00 USD | 0.00 USD | 4,220.00 USD | `-32.86%` | `1,500.40` |
| `Live` | `Long` | `2.83` | 14,820,000.00 USD | 0.00 USD | 2,870.00 USD | `-32.62%` | `1,017.50` |
| `Live` | `Long` | `2.83` | 14,820,000.00 USD | 0.00 USD | 1,140.00 USD | `-32.38%` | `402.50` |
| `Live` | `Long` | `2.85` | 14,820,000.00 USD | 0.00 USD | 8,780.00 USD | `-32.14%` | `3,084.70` |
| `Live` | `Long` | `2.85` | 14,810,000.00 USD | 0.00 USD | 2,580,000.00 USD | `-31.90%` | `904,159.50` |
| `Live` | `Long` | `2.87` | 12,230,000.00 USD | 0.00 USD | 202,730.00 USD | `-31.66%` | `70,759.50` |
| `Live` | `Long` | `2.88` | 12,030,000.00 USD | 0.00 USD | 966,120.00 USD | `-31.43%` | `336,040.60` |
| `Live` | `Long` | `2.88` | 11,060,000.00 USD | 0.00 USD | 6,140.00 USD | `-31.19%` | `2,127.40` |
| `Live` | `Long` | `2.90` | 11,060,000.00 USD | 0.00 USD | 29,480.00 USD | `-30.95%` | `10,182.30` |
| `Live` | `Long` | `2.90` | 11,030,000.00 USD | 0.00 USD | 15,340.00 USD | `-30.71%` | `5,281.80` |
| `Live` | `Long` | `2.92` | 11,010,000.00 USD | 0.00 USD | 88,920.00 USD | `-30.47%` | `30,503.70` |
| `Live` | `Long` | `2.92` | 10,920,000.00 USD | 0.00 USD | 47,510.00 USD | `-30.23%` | `16,244.40` |
| `Live` | `Long` | `2.94` | 10,870,000.00 USD | 0.00 USD | 50,770.00 USD | `-29.99%` | `17,297.80` |
| `Live` | `Long` | `2.94` | 10,820,000.00 USD | 0.00 USD | 175,140.00 USD | `-29.76%` | `59,469.60` |
| `Live` | `Long` | `2.96` | 10,650,000.00 USD | 0.00 USD | 2,270.00 USD | `-29.52%` | `768.40` |
| `Live` | `Long` | `2.96` | 10,650,000.00 USD | 0.00 USD | 1,380.00 USD | `-29.28%` | `465.60` |
| `Live` | `Long` | `2.98` | 10,640,000.00 USD | 0.00 USD | 37,560.00 USD | `-29.04%` | `12,626.10` |
| `Live` | `Long` | `2.98` | 10,610,000.00 USD | 0.00 USD | 12,050.00 USD | `-28.80%` | `4,036.10` |
| `Live` | `Long` | `3.00` | 10,590,000.00 USD | 0.00 USD | 18,040.00 USD | `-28.56%` | `6,022.60` |
| `Live` | `Long` | `3.00` | 10,580,000.00 USD | 0.00 USD | 11,020.00 USD | `-28.32%` | `3,667.70` |
| `Live` | `Long` | `3.02` | 10,570,000.00 USD | 0.00 USD | 24,390.00 USD | `-28.09%` | `8,089.80` |
| `Live` | `Long` | `3.02` | 10,540,000.00 USD | 0.00 USD | 23,880.00 USD | `-27.85%` | `7,894.10` |
| `Live` | `Long` | `3.04` | 10,520,000.00 USD | 0.00 USD | 14,960.00 USD | `-27.61%` | `4,930.20` |
| `Live` | `Long` | `3.04` | 10,500,000.00 USD | 0.00 USD | 170,550.00 USD | `-27.37%` | `56,009.20` |
| `Live` | `Long` | `3.06` | 10,330,000.00 USD | 0.00 USD | 63,710.00 USD | `-27.13%` | `20,853.30` |
| `Live` | `Long` | `3.06` | 10,270,000.00 USD | 0.00 USD | 118,440.00 USD | `-26.89%` | `38,643.60` |
| `Live` | `Long` | `3.08` | 10,150,000.00 USD | 0.00 USD | 121,730.00 USD | `-26.65%` | `39,587.40` |
| `Live` | `Long` | `3.08` | 10,030,000.00 USD | 0.00 USD | 9,130.00 USD | `-26.42%` | `2,959.70` |
| `Live` | `Long` | `3.10` | 10,020,000.00 USD | 0.00 USD | 5,800.00 USD | `-26.18%` | `1,874.30` |
| `Live` | `Long` | `3.10` | 10,010,000.00 USD | 0.00 USD | 21,890.00 USD | `-25.94%` | `7,048.40` |
| `Live` | `Long` | `3.12` | 9,990,000.00 USD | 0.00 USD | 31,290.00 USD | `-25.70%` | `10,044.00` |
| `Live` | `Long` | `3.12` | 9,960,000.00 USD | 0.00 USD | 7,930.00 USD | `-25.46%` | `2,537.20` |
| `Live` | `Long` | `3.13` | 9,950,000.00 USD | 0.00 USD | 7,780.00 USD | `-25.22%` | `2,481.00` |
| `Live` | `Long` | `3.15` | 9,940,000.00 USD | 0.00 USD | 77,990.00 USD | `-24.99%` | `24,796.70` |
| `Live` | `Long` | `3.17` | 9,870,000.00 USD | 0.00 USD | 14,450.00 USD | `-24.51%` | `4,567.00` |
| `Live` | `Long` | `3.17` | 9,850,000.00 USD | 0.00 USD | 32,810.00 USD | `-24.27%` | `10,333.50` |
| `Live` | `Long` | `3.19` | 9,820,000.00 USD | 0.00 USD | 245,320.00 USD | `-24.03%` | `77,025.00` |
| `Live` | `Long` | `3.19` | 9,570,000.00 USD | 0.00 USD | 7,680.00 USD | `-23.79%` | `2,404.10` |
| `Live` | `Long` | `3.21` | 9,570,000.00 USD | 0.00 USD | 4,250.00 USD | `-23.55%` | `1,326.60` |
| `Live` | `Long` | `3.21` | 9,560,000.00 USD | 0.00 USD | 14,170.00 USD | `-23.32%` | `4,408.00` |
| `Live` | `Long` | `3.23` | 9,550,000.00 USD | 0.00 USD | 23,110.00 USD | `-23.08%` | `7,167.00` |
| `Live` | `Long` | `3.23` | 9,520,000.00 USD | 0.00 USD | 57,130.00 USD | `-22.84%` | `17,659.90` |
| `Live` | `Long` | `3.25` | 9,470,000.00 USD | 0.00 USD | 20,130.00 USD | `-22.60%` | `6,204.10` |
| `Live` | `Long` | `3.25` | 9,450,000.00 USD | 0.00 USD | 4,050.00 USD | `-22.36%` | `1,245.10` |
| `Live` | `Long` | `3.27` | 9,440,000.00 USD | 0.00 USD | 38,000.00 USD | `-22.12%` | `11,639.20` |
| `Live` | `Long` | `3.27` | 9,410,000.00 USD | 0.00 USD | 868,070.00 USD | `-21.88%` | `265,060.40` |
| `Live` | `Long` | `3.29` | 8,540,000.00 USD | 0.00 USD | 4,080.00 USD | `-21.65%` | `1,240.60` |
| `Live` | `Long` | `3.29` | 8,530,000.00 USD | 0.00 USD | 143,070.00 USD | `-21.41%` | `43,420.40` |
| `Live` | `Long` | `3.31` | 8,390,000.00 USD | 0.00 USD | 132,030.00 USD | `-21.17%` | `39,948.60` |
| `Live` | `Long` | `3.31` | 8,260,000.00 USD | 0.00 USD | 24,690.00 USD | `-20.93%` | `7,448.70` |
| `Live` | `Long` | `3.33` | 8,230,000.00 USD | 0.00 USD | 9,900.00 USD | `-20.69%` | `2,977.10` |
| `Live` | `Long` | `3.33` | 8,220,000.00 USD | 0.00 USD | 73,890.00 USD | `-20.45%` | `22,154.80` |
| `Live` | `Long` | `3.35` | 8,150,000.00 USD | 0.00 USD | 19,110.00 USD | `-20.21%` | `5,712.10` |
| `Live` | `Long` | `3.35` | 8,130,000.00 USD | 0.00 USD | 11,850.00 USD | `-19.98%` | `3,531.00` |
| `Live` | `Long` | `3.37` | 8,120,000.00 USD | 0.00 USD | 25,860.00 USD | `-19.74%` | `7,684.00` |
| `Live` | `Long` | `3.38` | 8,090,000.00 USD | 0.00 USD | 63,170.00 USD | `-19.50%` | `18,718.10` |
| `Live` | `Long` | `3.38` | 8,030,000.00 USD | 0.00 USD | 180,800.00 USD | `-19.26%` | `53,412.10` |
| `Live` | `Long` | `3.40` | 7,850,000.00 USD | 0.00 USD | 1,230.00 USD | `-19.02%` | `361.70` |
| `Live` | `Long` | `3.40` | 7,850,000.00 USD | 0.00 USD | 100,380.00 USD | `-18.78%` | `29,478.80` |
| `Live` | `Long` | `3.42` | 7,750,000.00 USD | 0.00 USD | 415,990.00 USD | `-18.55%` | `121,813.20` |
| `Live` | `Long` | `3.42` | 7,330,000.00 USD | 0.00 USD | 28,690.00 USD | `-18.31%` | `8,375.70` |
| `Live` | `Long` | `3.44` | 7,300,000.00 USD | 0.00 USD | 31,440.00 USD | `-18.07%` | `9,153.20` |
| `Live` | `Long` | `3.44` | 7,270,000.00 USD | 0.00 USD | 30,940.00 USD | `-17.83%` | `8,981.80` |
| `Live` | `Long` | `3.46` | 7,240,000.00 USD | 0.00 USD | 11,190.00 USD | `-17.59%` | `3,240.00` |
| `Live` | `Long` | `3.46` | 7,230,000.00 USD | 0.00 USD | 16,150.00 USD | `-17.35%` | `4,661.90` |
| `Live` | `Long` | `3.48` | 7,210,000.00 USD | 0.00 USD | 191,450.00 USD | `-17.11%` | `55,093.80` |
| `Live` | `Long` | `3.48` | 7,020,000.00 USD | 0.00 USD | 33,310.00 USD | `-16.88%` | `9,558.50` |
| `Live` | `Long` | `3.50` | 6,990,000.00 USD | 0.00 USD | 56,910.00 USD | `-16.64%` | `16,283.20` |
| `Live` | `Long` | `3.50` | 6,930,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-16.40%` | `370,647.60` |
| `Live` | `Long` | `3.52` | 5,630,000.00 USD | 0.00 USD | 42,550.00 USD | `-16.16%` | `12,106.60` |
| `Live` | `Long` | `3.52` | 5,590,000.00 USD | 0.00 USD | 114,450.00 USD | `-15.92%` | `32,467.70` |
| `Live` | `Long` | `3.54` | 5,480,000.00 USD | 0.00 USD | 395,520.00 USD | `-15.68%` | `111,888.00` |
| `Live` | `Long` | `3.54` | 5,080,000.00 USD | 0.00 USD | 167,840.00 USD | `-15.44%` | `47,344.30` |
| `Live` | `Long` | `3.56` | 4,910,000.00 USD | 0.00 USD | 555,700.00 USD | `-15.21%` | `156,315.50` |
| `Live` | `Long` | `3.56` | 4,360,000.00 USD | 0.00 USD | 10,290.00 USD | `-14.97%` | `2,885.50` |
| `Live` | `Long` | `3.58` | 4,350,000.00 USD | 0.00 USD | 61,790.00 USD | `-14.73%` | `17,284.50` |
| `Live` | `Long` | `3.58` | 4,280,000.00 USD | 0.00 USD | 43,410.00 USD | `-14.49%` | `12,109.10` |
| `Live` | `Long` | `3.60` | 4,240,000.00 USD | 0.00 USD | 107,820.00 USD | `-14.25%` | `29,992.60` |
| `Live` | `Long` | `3.60` | 4,130,000.00 USD | 0.00 USD | 71,270.00 USD | `-14.01%` | `19,768.60` |
| `Live` | `Long` | `3.62` | 4,060,000.00 USD | 0.00 USD | 16,470.00 USD | `-13.77%` | `4,555.60` |
| `Live` | `Long` | `3.62` | 4,040,000.00 USD | 0.00 USD | 123,280.00 USD | `-13.54%` | `34,008.80` |
| `Live` | `Long` | `3.63` | 3,920,000.00 USD | 0.00 USD | 3,550.00 USD | `-13.30%` | `975.40` |
| `Live` | `Long` | `3.65` | 3,920,000.00 USD | 0.00 USD | 23,090.00 USD | `-13.06%` | `6,334.30` |
| `Live` | `Long` | `3.65` | 3,890,000.00 USD | 0.00 USD | 15,510.00 USD | `-12.82%` | `4,242.50` |
| `Live` | `Long` | `3.67` | 3,880,000.00 USD | 0.00 USD | 38,130.00 USD | `-12.58%` | `10,404.40` |
| `Live` | `Long` | `3.67` | 3,840,000.00 USD | 0.00 USD | 100,150.00 USD | `-12.34%` | `27,252.10` |
| `Live` | `Long` | `3.69` | 3,740,000.00 USD | 0.00 USD | 217,880.00 USD | `-12.10%` | `59,126.00` |
| `Live` | `Long` | `3.69` | 3,520,000.00 USD | 0.00 USD | 93,270.00 USD | `-11.87%` | `25,241.00` |
| `Live` | `Long` | `3.71` | 3,430,000.00 USD | 0.00 USD | 181,250.00 USD | `-11.63%` | `48,920.10` |
| `Live` | `Long` | `3.71` | 3,250,000.00 USD | 0.00 USD | 16,470.00 USD | `-11.39%` | `4,434.60` |
| `Live` | `Long` | `3.73` | 3,230,000.00 USD | 0.00 USD | 161,130.00 USD | `-11.15%` | `43,256.50` |
| `Live` | `Long` | `3.73` | 3,070,000.00 USD | 0.00 USD | 136,970.00 USD | `-10.91%` | `36,672.30` |
| `Live` | `Long` | `3.75` | 2,930,000.00 USD | 0.00 USD | 39,750.00 USD | `-10.67%` | `10,614.40` |
| `Live` | `Long` | `3.75` | 2,890,000.00 USD | 0.00 USD | 151,240.00 USD | `-10.44%` | `40,276.20` |
| `Live` | `Long` | `3.77` | 2,740,000.00 USD | 0.00 USD | 69,100.00 USD | `-10.20%` | `18,353.50` |
| `Live` | `Long` | `3.77` | 2,670,000.00 USD | 0.00 USD | 54,560.00 USD | `-9.96%` | `14,453.50` |
| `Live` | `Long` | `3.79` | 2,620,000.00 USD | 0.00 USD | 52,750.00 USD | `-9.72%` | `13,937.70` |
| `Live` | `Long` | `3.79` | 2,570,000.00 USD | 0.00 USD | 137,090.00 USD | `-9.48%` | `36,122.80` |
| `Live` | `Long` | `3.81` | 2,430,000.00 USD | 0.00 USD | 458,720.00 USD | `-9.24%` | `120,556.90` |
| `Live` | `Long` | `3.81` | 1,970,000.00 USD | 0.00 USD | 10,250.00 USD | `-9.00%` | `2,685.90` |
| `Live` | `Long` | `3.83` | 1,960,000.00 USD | 0.00 USD | 160,810.00 USD | `-8.77%` | `42,041.30` |
| `Live` | `Long` | `3.83` | 1,800,000.00 USD | 0.00 USD | 181,280.00 USD | `-8.53%` | `47,270.30` |
| `Live` | `Long` | `3.85` | 1,620,000.00 USD | 0.00 USD | 119,460.00 USD | `-8.29%` | `31,069.30` |
| `Live` | `Long` | `3.85` | 1,500,000.00 USD | 0.00 USD | 26,330.00 USD | `-8.05%` | `6,830.70` |
| `Live` | `Long` | `3.87` | 1,470,000.00 USD | 0.00 USD | 163,800.00 USD | `-7.81%` | `42,381.60` |
| `Live` | `Long` | `3.88` | 1,310,000.00 USD | 0.00 USD | 16,460.00 USD | `-7.57%` | `4,248.60` |
| `Live` | `Long` | `3.88` | 1,290,000.00 USD | 0.00 USD | 354,420.00 USD | `-7.33%` | `91,226.90` |
| `Live` | `Long` | `3.90` | 938,190.00 USD | 0.00 USD | 121,470.00 USD | `-7.10%` | `31,185.00` |
| `Live` | `Long` | `3.90` | 816,720.00 USD | 0.00 USD | 7,240.00 USD | `-6.86%` | `1,855.20` |
| `Live` | `Long` | `3.92` | 809,480.00 USD | 0.00 USD | 7,930.00 USD | `-6.62%` | `2,025.30` |
| `Live` | `Long` | `3.92` | 801,550.00 USD | 0.00 USD | 8,940.00 USD | `-6.38%` | `2,278.70` |
| `Live` | `Long` | `3.94` | 792,610.00 USD | 0.00 USD | 18,150.00 USD | `-6.14%` | `4,613.00` |
| `Live` | `Long` | `3.94` | 774,460.00 USD | 0.00 USD | 257,710.00 USD | `-5.90%` | `65,325.60` |
| `Live` | `Long` | `3.96` | 516,750.00 USD | 0.00 USD | 32,430.00 USD | `-5.66%` | `8,200.20` |
| `Live` | `Long` | `3.96` | 484,310.00 USD | 0.00 USD | 11,060.00 USD | `-5.43%` | `2,788.90` |
| `Live` | `Long` | `3.98` | 473,260.00 USD | 0.00 USD | 16,590.00 USD | `-5.19%` | `4,173.30` |
| `Live` | `Long` | `3.98` | 456,670.00 USD | 0.00 USD | 170,770.00 USD | `-4.95%` | `42,853.90` |
| `Live` | `Long` | `4.00` | 285,890.00 USD | 0.00 USD | 71,910.00 USD | `-4.71%` | `18,000.00` |
| `Live` | `Long` | `4.00` | 213,980.00 USD | 0.00 USD | 11,640.00 USD | `-4.47%` | `2,906.50` |
| `Live` | `Long` | `4.01` | 202,340.00 USD | 0.00 USD | 29,050.00 USD | `-4.23%` | `7,234.30` |
| `Live` | `Long` | `4.03` | 173,300.00 USD | 0.00 USD | 60,610.00 USD | `-4.00%` | `15,058.50` |
| `Live` | `Long` | `4.04` | 112,690.00 USD | 0.00 USD | 31,270.00 USD | `-3.76%` | `7,750.50` |
| `Live` | `Long` | `4.04` | 81,410.00 USD | 0.00 USD | 71,750.00 USD | `-3.52%` | `17,737.90` |
| `Live` | `Long` | `4.05` | 9,660.00 USD | 0.00 USD | 9,370.00 USD | `-3.28%` | `2,311.40` |
| `Live` | `Long` | `4.18` | 291.69 USD | 0.00 USD | 291.69 USD | `-0.18%` | `69.70` |
| `Live` | `Short` | `4.22` | 581.36 USD | 581.36 USD | 0.00 USD | `+0.78%` | `137.60` |
| `Live` | `Short` | `4.29` | 211,310.00 USD | 210,730.00 USD | 0.00 USD | `+2.44%` | `49,064.30` |
| `Live` | `Short` | `4.32` | 212,010.00 USD | 699.03 USD | 0.00 USD | `+2.92%` | `162.00` |
| `Live` | `Short` | `4.33` | 218,610.00 USD | 6,600.00 USD | 0.00 USD | `+3.16%` | `1,526.60` |
| `Live` | `Short` | `4.34` | 222,740.00 USD | 4,130.00 USD | 0.00 USD | `+3.64%` | `949.40` |
| `Live` | `Short` | `4.36` | 225,790.00 USD | 3,050.00 USD | 0.00 USD | `+3.88%` | `701.00` |
| `Live` | `Short` | `4.37` | 235,290.00 USD | 9,500.00 USD | 0.00 USD | `+4.11%` | `2,176.50` |
| `Live` | `Short` | `4.38` | 318,850.00 USD | 83,560.00 USD | 0.00 USD | `+4.35%` | `19,099.00` |
| `Live` | `Short` | `4.38` | 319,410.00 USD | 561.72 USD | 0.00 USD | `+4.59%` | `128.10` |
| `Live` | `Short` | `4.39` | 633,040.00 USD | 313,630.00 USD | 0.00 USD | `+4.83%` | `71,360.00` |
| `Live` | `Short` | `4.45` | 633,400.00 USD | 358.27 USD | 0.00 USD | `+6.02%` | `80.60` |
| `Live` | `Short` | `4.46` | 656,940.00 USD | 23,540.00 USD | 0.00 USD | `+6.26%` | `5,284.70` |
| `Live` | `Short` | `4.46` | 657,870.00 USD | 926.93 USD | 0.00 USD | `+6.50%` | `207.60` |
| `Live` | `Short` | `4.47` | 658,720.00 USD | 850.25 USD | 0.00 USD | `+6.74%` | `190.00` |
| `Live` | `Short` | `4.49` | 659,810.00 USD | 1,090.00 USD | 0.00 USD | `+6.98%` | `243.20` |
| `Live` | `Short` | `4.50` | 676,640.00 USD | 16,830.00 USD | 0.00 USD | `+7.22%` | `3,745.20` |
| `Live` | `Short` | `4.50` | 676,930.00 USD | 283.81 USD | 0.00 USD | `+7.45%` | `63.00` |
| `Live` | `Short` | `4.51` | 677,430.00 USD | 505.23 USD | 0.00 USD | `+7.69%` | `111.90` |
| `Live` | `Short` | `4.53` | 695,530.00 USD | 18,100.00 USD | 0.00 USD | `+7.93%` | `4,000.00` |
| `Live` | `Short` | `4.54` | 699,240.00 USD | 3,700.00 USD | 0.00 USD | `+8.17%` | `816.60` |
| `Live` | `Short` | `4.54` | 699,490.00 USD | 252.70 USD | 0.00 USD | `+8.41%` | `55.60` |
| `Live` | `Short` | `4.57` | 699,910.00 USD | 425.00 USD | 0.00 USD | `+8.88%` | `93.10` |
| `Live` | `Short` | `4.63` | 700,900.00 USD | 990.04 USD | 0.00 USD | `+10.55%` | `213.60` |
| `Live` | `Short` | `4.64` | 755,590.00 USD | 54,680.00 USD | 0.00 USD | `+10.79%` | `11,772.20` |
| `Live` | `Short` | `4.66` | 756,340.00 USD | 756.44 USD | 0.00 USD | `+11.03%` | `162.50` |
| `Live` | `Short` | `4.67` | 756,440.00 USD | 101.70 USD | 0.00 USD | `+11.27%` | `21.80` |
| `Live` | `Short` | `4.70` | 756,670.00 USD | 230.06 USD | 0.00 USD | `+11.99%` | `49.00` |
| `Live` | `Short` | `4.71` | 915,690.00 USD | 159,020.00 USD | 0.00 USD | `+12.22%` | `33,797.70` |
| `Live` | `Short` | `4.74` | 928,200.00 USD | 12,500.00 USD | 0.00 USD | `+12.94%` | `2,640.70` |
| `Live` | `Short` | `4.78` | 936,980.00 USD | 8,780.00 USD | 0.00 USD | `+13.89%` | `1,839.40` |
| `Live` | `Short` | `4.79` | 937,120.00 USD | 143.55 USD | 0.00 USD | `+14.13%` | `30.00` |
| `Live` | `Short` | `4.79` | 939,050.00 USD | 1,920.00 USD | 0.00 USD | `+14.37%` | `401.10` |
| `Live` | `Short` | `4.83` | 940,790.00 USD | 1,740.00 USD | 0.00 USD | `+15.09%` | `360.90` |
| `Live` | `Short` | `4.83` | 942,320.00 USD | 1,540.00 USD | 0.00 USD | `+15.32%` | `317.90` |
| `Live` | `Short` | `4.84` | 1,000,000.00 USD | 59,340.00 USD | 0.00 USD | `+15.56%` | `12,248.30` |
| `Live` | `Short` | `4.87` | 1,000,000.00 USD | 137.68 USD | 0.00 USD | `+16.04%` | `28.30` |
| `Live` | `Short` | `4.88` | 1,040,000.00 USD | 39,550.00 USD | 0.00 USD | `+16.28%` | `8,112.10` |
| `Live` | `Short` | `4.88` | 1,040,000.00 USD | 827.03 USD | 0.00 USD | `+16.52%` | `169.30` |
| `Live` | `Short` | `4.92` | 1,060,000.00 USD | 20,720.00 USD | 0.00 USD | `+17.23%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,060,000.00 USD | 2,100.00 USD | 0.00 USD | `+17.47%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,070,000.00 USD | 157.43 USD | 0.00 USD | `+17.71%` | `31.90` |
| `Live` | `Short` | `4.96` | 1,070,000.00 USD | 488.56 USD | 0.00 USD | `+18.19%` | `98.60` |
| `Live` | `Short` | `4.97` | 1,170,000.00 USD | 99,370.00 USD | 0.00 USD | `+18.66%` | `19,974.00` |
| `Live` | `Short` | `5.05` | 1,200,000.00 USD | 35,380.00 USD | 0.00 USD | `+20.57%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,200,000.00 USD | 3,420.00 USD | 0.00 USD | `+20.81%` | `675.80` |
| `Live` | `Short` | `5.12` | 1,210,000.00 USD | 2,560.00 USD | 0.00 USD | `+22.24%` | `500.00` |
| `Live` | `Short` | `5.16` | 1,210,000.00 USD | 2,580.00 USD | 0.00 USD | `+22.96%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,210,000.00 USD | 751.51 USD | 0.00 USD | `+23.20%` | `145.50` |
| `Live` | `Short` | `5.20` | 1,220,000.00 USD | 12,440.00 USD | 0.00 USD | `+23.91%` | `2,395.50` |
| `Live` | `Short` | `5.21` | 1,220,000.00 USD | 601.29 USD | 0.00 USD | `+24.39%` | `115.30` |
| `Live` | `Short` | `5.22` | 1,290,000.00 USD | 72,110.00 USD | 0.00 USD | `+24.63%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 1,350,000.00 USD | 58,870.00 USD | 0.00 USD | `+25.10%` | `11,223.60` |
| `Live` | `Short` | `5.25` | 1,370,000.00 USD | 17,380.00 USD | 0.00 USD | `+25.34%` | `3,307.90` |
| `Live` | `Short` | `5.26` | 1,380,000.00 USD | 5,610.00 USD | 0.00 USD | `+25.58%` | `1,066.10` |
| `Live` | `Short` | `5.29` | 1,380,000.00 USD | 134.77 USD | 0.00 USD | `+26.06%` | `25.50` |
| `Live` | `Short` | `5.29` | 2,460,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+26.30%` | `204,022.20` |
| `Live` | `Short` | `5.30` | 2,460,000.00 USD | 524.66 USD | 0.00 USD | `+26.54%` | `98.90` |
| `Live` | `Short` | `5.32` | 2,460,000.00 USD | 147.23 USD | 0.00 USD | `+26.77%` | `27.70` |
| `Live` | `Short` | `5.34` | 2,460,000.00 USD | 1,710.00 USD | 0.00 USD | `+27.49%` | `320.50` |
| `Live` | `Short` | `5.36` | 2,460,000.00 USD | 142.44 USD | 0.00 USD | `+27.73%` | `26.60` |
| `Live` | `Short` | `5.37` | 2,750,000.00 USD | 293,090.00 USD | 0.00 USD | `+27.97%` | `54,629.40` |
| `Live` | `Short` | `5.38` | 2,750,000.00 USD | 182.21 USD | 0.00 USD | `+28.21%` | `33.90` |
| `Live` | `Short` | `5.43` | 2,750,000.00 USD | 419.04 USD | 0.00 USD | `+29.64%` | `77.10` |
| `Live` | `Short` | `5.46` | 3,200,000.00 USD | 451,170.00 USD | 0.00 USD | `+30.35%` | `82,556.10` |
| `Live` | `Short` | `5.47` | 3,210,000.00 USD | 627.98 USD | 0.00 USD | `+30.59%` | `114.70` |
| `Live` | `Short` | `5.50` | 3,270,000.00 USD | 67,850.00 USD | 0.00 USD | `+31.07%` | `12,347.30` |
| `Live` | `Short` | `5.51` | 3,370,000.00 USD | 93,950.00 USD | 0.00 USD | `+31.54%` | `17,034.90` |
| `Live` | `Short` | `5.54` | 3,370,000.00 USD | 209.22 USD | 0.00 USD | `+32.02%` | `37.80` |
| `Live` | `Short` | `5.55` | 4,970,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+32.50%` | `288,027.90` |
| `Live` | `Short` | `5.57` | 4,980,000.00 USD | 8,670.00 USD | 0.00 USD | `+32.74%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 5,040,000.00 USD | 62,420.00 USD | 0.00 USD | `+33.21%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 5,040,000.00 USD | 686.51 USD | 0.00 USD | `+33.45%` | `122.70` |
| `Live` | `Short` | `5.62` | 5,100,000.00 USD | 63,730.00 USD | 0.00 USD | `+33.93%` | `11,349.70` |
| `Live` | `Short` | `5.64` | 5,100,000.00 USD | 706.75 USD | 0.00 USD | `+34.65%` | `125.20` |
| `Live` | `Short` | `5.67` | 5,100,000.00 USD | 1,630.00 USD | 0.00 USD | `+35.12%` | `287.30` |
| `Live` | `Short` | `5.67` | 5,110,000.00 USD | 228.70 USD | 0.00 USD | `+35.36%` | `40.30` |
| `Live` | `Short` | `5.68` | 5,130,000.00 USD | 26,090.00 USD | 0.00 USD | `+35.60%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 5,130,000.00 USD | 1,520.00 USD | 0.00 USD | `+35.84%` | `267.40` |
| `Live` | `Short` | `5.71` | 5,130,000.00 USD | 2,130.00 USD | 0.00 USD | `+36.31%` | `372.40` |
| `Live` | `Short` | `5.74` | 5,140,000.00 USD | 147.39 USD | 0.00 USD | `+36.79%` | `25.70` |
| `Live` | `Short` | `5.75` | 5,140,000.00 USD | 6,360.00 USD | 0.00 USD | `+37.03%` | `1,106.90` |
| `Live` | `Short` | `5.75` | 5,140,000.00 USD | 286.02 USD | 0.00 USD | `+37.27%` | `49.70` |
| `Live` | `Short` | `5.76` | 5,140,000.00 USD | 2,720.00 USD | 0.00 USD | `+37.51%` | `471.60` |
| `Live` | `Short` | `5.79` | 5,410,000.00 USD | 267,440.00 USD | 0.00 USD | `+37.98%` | `46,230.70` |
| `Live` | `Short` | `5.83` | 5,410,000.00 USD | 198.97 USD | 0.00 USD | `+39.18%` | `34.10` |
| `Live` | `Short` | `5.84` | 5,410,000.00 USD | 310.95 USD | 0.00 USD | `+39.42%` | `53.20` |
| `Live` | `Short` | `5.86` | 5,410,000.00 USD | 848.39 USD | 0.00 USD | `+39.65%` | `144.90` |
| `Live` | `Short` | `5.88` | 5,420,000.00 USD | 7,150.00 USD | 0.00 USD | `+40.37%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 5,510,000.00 USD | 88,590.00 USD | 0.00 USD | `+40.61%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 5,510,000.00 USD | 189.28 USD | 0.00 USD | `+41.09%` | `32.00` |
| `Live` | `Short` | `5.95` | 5,630,000.00 USD | 117,510.00 USD | 0.00 USD | `+41.80%` | `19,766.20` |
| `Live` | `Short` | `6.03` | 5,650,000.00 USD | 23,060.00 USD | 0.00 USD | `+43.71%` | `3,827.40` |
| `Live` | `Short` | `6.07` | 5,650,000.00 USD | 740.54 USD | 0.00 USD | `+44.66%` | `122.10` |
| `Live` | `Short` | `6.08` | 5,660,000.00 USD | 5,920.00 USD | 0.00 USD | `+45.14%` | `973.10` |
| `Live` | `Short` | `6.09` | 5,690,000.00 USD | 37,910.00 USD | 0.00 USD | `+45.38%` | `6,220.10` |
| `Live` | `Short` | `6.12` | 6,020,000.00 USD | 327,710.00 USD | 0.00 USD | `+46.09%` | `53,503.40` |
| `Live` | `Short` | `6.13` | 6,020,000.00 USD | 2,430.00 USD | 0.00 USD | `+46.33%` | `396.10` |
| `Live` | `Short` | `6.16` | 6,380,000.00 USD | 356,610.00 USD | 0.00 USD | `+46.81%` | `57,938.40` |
| `Live` | `Short` | `6.18` | 6,380,000.00 USD | 1,890.00 USD | 0.00 USD | `+47.53%` | `305.00` |
| `Live` | `Short` | `6.24` | 6,910,000.00 USD | 526,230.00 USD | 0.00 USD | `+48.72%` | `84,400.00` |
| `Live` | `Short` | `6.25` | 6,920,000.00 USD | 7,300.00 USD | 0.00 USD | `+48.96%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 6,920,000.00 USD | 439.10 USD | 0.00 USD | `+49.19%` | `70.20` |
| `Live` | `Short` | `6.26` | 7,170,000.00 USD | 256,050.00 USD | 0.00 USD | `+49.43%` | `40,869.30` |
| `Live` | `Short` | `6.28` | 7,170,000.00 USD | 397.84 USD | 0.00 USD | `+49.67%` | `63.40` |
| `Live` | `Short` | `6.29` | 8,380,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+50.15%` | `191,883.80` |
| `Live` | `Short` | `6.32` | 8,380,000.00 USD | 310.70 USD | 0.00 USD | `+50.63%` | `49.20` |
| `Live` | `Short` | `6.33` | 8,380,000.00 USD | 382.00 USD | 0.00 USD | `+51.10%` | `60.30` |
| `Live` | `Short` | `6.34` | 8,380,000.00 USD | 214.46 USD | 0.00 USD | `+51.34%` | `33.80` |
| `Live` | `Short` | `6.37` | 8,380,000.00 USD | 113.93 USD | 0.00 USD | `+51.82%` | `17.90` |
| `Live` | `Short` | `6.38` | 8,380,000.00 USD | 288.15 USD | 0.00 USD | `+52.06%` | `45.20` |
| `Live` | `Short` | `6.38` | 8,380,000.00 USD | 2,010.00 USD | 0.00 USD | `+52.30%` | `314.70` |
| `Live` | `Short` | `6.39` | 8,390,000.00 USD | 2,000.00 USD | 0.00 USD | `+52.53%` | `312.80` |
| `Live` | `Short` | `6.41` | 8,390,000.00 USD | 3,780.00 USD | 0.00 USD | `+52.77%` | `590.10` |
| `Live` | `Short` | `6.42` | 8,390,000.00 USD | 943.65 USD | 0.00 USD | `+53.01%` | `147.10` |
| `Live` | `Short` | `6.42` | 8,390,000.00 USD | 173.47 USD | 0.00 USD | `+53.25%` | `27.00` |
| `Live` | `Short` | `6.45` | 8,400,000.00 USD | 5,270.00 USD | 0.00 USD | `+53.73%` | `818.40` |
| `Live` | `Short` | `6.46` | 8,400,000.00 USD | 7,150.00 USD | 0.00 USD | `+53.97%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 8,410,000.00 USD | 1,940.00 USD | 0.00 USD | `+54.20%` | `300.00` |
| `Live` | `Short` | `6.51` | 8,410,000.00 USD | 380.48 USD | 0.00 USD | `+55.40%` | `58.40` |
| `Live` | `Short` | `6.53` | 8,450,000.00 USD | 40,390.00 USD | 0.00 USD | `+55.64%` | `6,190.00` |
| `Live` | `Short` | `6.54` | 8,450,000.00 USD | 265.07 USD | 0.00 USD | `+56.11%` | `40.50` |
| `Live` | `Short` | `6.59` | 38,220,000.00 USD | 29,780,000.00 USD | 0.00 USD | `+57.30%` | `4,515,153.40` |
| `Live` | `Short` | `6.66` | 38,230,000.00 USD | 7,230.00 USD | 0.00 USD | `+58.74%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 38,230,000.00 USD | 233.94 USD | 0.00 USD | `+58.97%` | `35.10` |
| `Live` | `Short` | `6.67` | 38,230,000.00 USD | 200.25 USD | 0.00 USD | `+59.21%` | `30.00` |
| `Live` | `Short` | `6.70` | 38,240,000.00 USD | 9,270.00 USD | 0.00 USD | `+59.69%` | `1,384.00` |
| `Live` | `Short` | `6.72` | 38,250,000.00 USD | 5,740.00 USD | 0.00 USD | `+60.41%` | `852.80` |
| `Live` | `Short` | `6.75` | 38,280,000.00 USD | 37,480.00 USD | 0.00 USD | `+60.88%` | `5,556.90` |
| `Live` | `Short` | `6.75` | 39,530,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+61.12%` | `184,501.00` |
| `Live` | `Short` | `6.78` | 39,530,000.00 USD | 186.31 USD | 0.00 USD | `+61.60%` | `27.50` |
| `Live` | `Short` | `6.80` | 39,620,000.00 USD | 90,960.00 USD | 0.00 USD | `+62.31%` | `13,367.10` |
| `Live` | `Short` | `6.82` | 39,620,000.00 USD | 156.75 USD | 0.00 USD | `+62.55%` | `23.00` |
| `Live` | `Short` | `6.84` | 39,620,000.00 USD | 753.63 USD | 0.00 USD | `+63.27%` | `110.10` |
| `Live` | `Short` | `6.87` | 39,630,000.00 USD | 3,380.00 USD | 0.00 USD | `+63.74%` | `492.70` |
| `Live` | `Short` | `6.92` | 39,630,000.00 USD | 6,920.00 USD | 0.00 USD | `+65.18%` | `1,000.00` |
| `Live` | `Short` | `6.95` | 43,320,000.00 USD | 3,690,000.00 USD | 0.00 USD | `+65.65%` | `531,000.00` |
| `Live` | `Short` | `6.99` | 43,320,000.00 USD | 664.27 USD | 0.00 USD | `+66.61%` | `95.10` |
| `Live` | `Short` | `7.00` | 43,320,000.00 USD | 554.70 USD | 0.00 USD | `+66.85%` | `79.30` |
| `Live` | `Short` | `7.03` | 43,320,000.00 USD | 665.27 USD | 0.00 USD | `+67.56%` | `94.70` |
| `Live` | `Short` | `7.09` | 43,320,000.00 USD | 699.57 USD | 0.00 USD | `+69.23%` | `98.60` |
| `Live` | `Short` | `7.21` | 43,340,000.00 USD | 13,560.00 USD | 0.00 USD | `+72.09%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 43,340,000.00 USD | 4,910.00 USD | 0.00 USD | `+72.57%` | `679.30` |
| `Live` | `Short` | `7.28` | 43,360,000.00 USD | 22,140.00 USD | 0.00 USD | `+73.52%` | `3,043.90` |
| `Live` | `Short` | `7.29` | 43,360,000.00 USD | 764.52 USD | 0.00 USD | `+74.00%` | `104.80` |
| `Live` | `Short` | `7.33` | 43,370,000.00 USD | 1,320.00 USD | 0.00 USD | `+74.96%` | `180.00` |
| `Live` | `Short` | `7.37` | 43,370,000.00 USD | 3,550.00 USD | 0.00 USD | `+75.67%` | `481.50` |
| `Live` | `Short` | `7.39` | 43,370,000.00 USD | 1,040.00 USD | 0.00 USD | `+76.39%` | `140.60` |
| `Live` | `Short` | `7.42` | 53,280,000.00 USD | 9,910,000.00 USD | 0.00 USD | `+76.86%` | `1,336,000.00` |
| `Live` | `Short` | `7.46` | 61,140,000.00 USD | 7,860,000.00 USD | 0.00 USD | `+77.82%` | `1,054,072.20` |
| `Live` | `Short` | `7.50` | 61,200,000.00 USD | 59,960.00 USD | 0.00 USD | `+78.77%` | `8,000.00` |
| `Live` | `Short` | `7.53` | 61,200,000.00 USD | 1,570.00 USD | 0.00 USD | `+79.49%` | `208.40` |
| `Live` | `Short` | `7.54` | 61,200,000.00 USD | 483.75 USD | 0.00 USD | `+79.73%` | `64.20` |
| `Live` | `Short` | `7.57` | 61,280,000.00 USD | 83,220.00 USD | 0.00 USD | `+80.44%` | `11,000.00` |
| `Live` | `Short` | `7.61` | 61,280,000.00 USD | 2,640.00 USD | 0.00 USD | `+81.40%` | `347.20` |
| `Live` | `Short` | `7.63` | 61,300,000.00 USD | 19,210.00 USD | 0.00 USD | `+82.11%` | `2,516.10` |
| `Live` | `Short` | `7.66` | 61,320,000.00 USD | 20,000.00 USD | 0.00 USD | `+82.59%` | `2,612.80` |
| `Live` | `Short` | `7.67` | 61,320,000.00 USD | 360.25 USD | 0.00 USD | `+82.83%` | `47.00` |
| `Live` | `Short` | `7.68` | 61,330,000.00 USD | 11,530.00 USD | 0.00 USD | `+83.30%` | `1,500.00` |
| `Live` | `Short` | `7.70` | 61,430,000.00 USD | 92,340.00 USD | 0.00 USD | `+83.54%` | `12,000.00` |
| `Live` | `Short` | `7.72` | 61,430,000.00 USD | 6,400.00 USD | 0.00 USD | `+84.26%` | `828.00` |
| `Live` | `Short` | `7.74` | 61,450,000.00 USD | 12,220.00 USD | 0.00 USD | `+84.50%` | `1,579.60` |
| `Live` | `Short` | `7.75` | 61,450,000.00 USD | 949.54 USD | 0.00 USD | `+84.73%` | `122.60` |
| `Live` | `Short` | `7.78` | 61,480,000.00 USD | 33,500.00 USD | 0.00 USD | `+85.45%` | `4,308.50` |
| `Live` | `Short` | `7.79` | 61,490,000.00 USD | 13,640.00 USD | 0.00 USD | `+85.93%` | `1,750.00` |
| `Live` | `Short` | `7.80` | 61,520,000.00 USD | 27,290.00 USD | 0.00 USD | `+86.17%` | `3,496.50` |
| `Live` | `Short` | `7.87` | 61,520,000.00 USD | 2,980.00 USD | 0.00 USD | `+87.60%` | `378.70` |
| `Live` | `Short` | `7.88` | 61,530,000.00 USD | 1,700.00 USD | 0.00 USD | `+87.84%` | `216.50` |
| `Live` | `Short` | `7.89` | 61,530,000.00 USD | 254.22 USD | 0.00 USD | `+88.31%` | `32.20` |
| `Live` | `Short` | `7.93` | 61,530,000.00 USD | 165.84 USD | 0.00 USD | `+89.27%` | `20.90` |
| `Live` | `Short` | `7.95` | 61,530,000.00 USD | 6,120.00 USD | 0.00 USD | `+89.51%` | `769.80` |
| `Live` | `Short` | `7.99` | 61,540,000.00 USD | 4,030.00 USD | 0.00 USD | `+90.46%` | `504.70` |
| `Live` | `Short` | `8.03` | 61,970,000.00 USD | 435,420.00 USD | 0.00 USD | `+91.41%` | `54,257.40` |
| `Live` | `Short` | `8.12` | 61,980,000.00 USD | 11,890.00 USD | 0.00 USD | `+93.56%` | `1,465.10` |
| `Live` | `Short` | `8.26` | 63,030,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+96.90%` | `127,081.90` |
| `Live` | `Short` | `8.35` | 63,060,000.00 USD | 25,310.00 USD | 0.00 USD | `+99.05%` | `3,032.60` |
| `Live` | `Short` | `8.37` | 64,160,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+99.52%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 64,160,000.00 USD | 191.79 USD | 0.00 USD | `+99.76%` | `22.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,050,000.00 USD | 0.00 USD | 585.51 USD | `-76.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,050,000.00 USD | 0.00 USD | 339.82 USD | `-75.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,050,000.00 USD | 0.00 USD | 196.58 USD | `-71.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,050,000.00 USD | 0.00 USD | 331.54 USD | `-67.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,050,000.00 USD | 0.00 USD | 345.25 USD | `-67.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,050,000.00 USD | 0.00 USD | 5,640.00 USD | `-67.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,040,000.00 USD | 0.00 USD | 997.29 USD | `-66.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,040,000.00 USD | 0.00 USD | 741.29 USD | `-63.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,040,000.00 USD | 0.00 USD | 113.28 USD | `-63.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,040,000.00 USD | 0.00 USD | 4,000.00 USD | `-63.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,030,000.00 USD | 0.00 USD | 324.22 USD | `-62.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,030,000.00 USD | 0.00 USD | 4,590.00 USD | `-61.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,030,000.00 USD | 0.00 USD | 739.67 USD | `-61.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,030,000.00 USD | 0.00 USD | 1,740.00 USD | `-61.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,030,000.00 USD | 0.00 USD | 6,260.00 USD | `-61.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,020,000.00 USD | 0.00 USD | 345.40 USD | `-60.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,020,000.00 USD | 0.00 USD | 167.50 USD | `-60.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,020,000.00 USD | 0.00 USD | 669.02 USD | `-59.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,020,000.00 USD | 0.00 USD | 105.88 USD | `-59.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,020,000.00 USD | 0.00 USD | 172.50 USD | `-58.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,020,000.00 USD | 0.00 USD | 10,650.00 USD | `-57.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,010,000.00 USD | 0.00 USD | 722.00 USD | `-56.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,010,000.00 USD | 0.00 USD | 259.00 USD | `-56.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,010,000.00 USD | 0.00 USD | 103.84 USD | `-56.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,010,000.00 USD | 0.00 USD | 109.00 USD | `-56.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,010,000.00 USD | 0.00 USD | 222.19 USD | `-55.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,010,000.00 USD | 0.00 USD | 10,280.00 USD | `-55.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,000,000.00 USD | 0.00 USD | 558.36 USD | `-54.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,000,000.00 USD | 0.00 USD | 1,520.00 USD | `-54.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,000,000.00 USD | 0.00 USD | 222.14 USD | `-53.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,000,000.00 USD | 0.00 USD | 279.50 USD | `-53.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 2,990,000.00 USD | 0.00 USD | 197.50 USD | `-52.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,990,000.00 USD | 0.00 USD | 935.66 USD | `-52.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,990,000.00 USD | 0.00 USD | 18,860.00 USD | `-52.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,970,000.00 USD | 0.00 USD | 3,020.00 USD | `-51.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,970,000.00 USD | 0.00 USD | 214.52 USD | `-51.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,970,000.00 USD | 0.00 USD | 1,200.00 USD | `-50.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,970,000.00 USD | 0.00 USD | 578.41 USD | `-50.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,970,000.00 USD | 0.00 USD | 18,070.00 USD | `-50.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,950,000.00 USD | 0.00 USD | 108.62 USD | `-49.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,950,000.00 USD | 0.00 USD | 107.23 USD | `-49.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,950,000.00 USD | 0.00 USD | 1,590.00 USD | `-49.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,950,000.00 USD | 0.00 USD | 5,830.00 USD | `-48.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,940,000.00 USD | 0.00 USD | 310.32 USD | `-48.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,940,000.00 USD | 0.00 USD | 1,170.00 USD | `-48.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,940,000.00 USD | 0.00 USD | 576.18 USD | `-47.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,940,000.00 USD | 0.00 USD | 295.67 USD | `-47.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,940,000.00 USD | 0.00 USD | 1,430.00 USD | `-47.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,940,000.00 USD | 0.00 USD | 812.68 USD | `-47.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,940,000.00 USD | 0.00 USD | 1,440.00 USD | `-46.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,940,000.00 USD | 0.00 USD | 106.16 USD | `-46.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,940,000.00 USD | 0.00 USD | 6,270.00 USD | `-46.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,930,000.00 USD | 0.00 USD | 478.06 USD | `-46.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,930,000.00 USD | 0.00 USD | 540.88 USD | `-45.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,930,000.00 USD | 0.00 USD | 867.46 USD | `-45.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,930,000.00 USD | 0.00 USD | 759.76 USD | `-45.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,930,000.00 USD | 0.00 USD | 11,060.00 USD | `-45.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,920,000.00 USD | 0.00 USD | 3,690.00 USD | `-45.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,910,000.00 USD | 0.00 USD | 722.15 USD | `-44.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,910,000.00 USD | 0.00 USD | 467.00 USD | `-44.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,910,000.00 USD | 0.00 USD | 506.75 USD | `-44.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,910,000.00 USD | 0.00 USD | 214.27 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,910,000.00 USD | 0.00 USD | 428.69 USD | `-43.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,910,000.00 USD | 0.00 USD | 322.45 USD | `-43.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,910,000.00 USD | 0.00 USD | 108.25 USD | `-42.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,910,000.00 USD | 0.00 USD | 3,900.00 USD | `-42.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,910,000.00 USD | 0.00 USD | 799.04 USD | `-42.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,910,000.00 USD | 0.00 USD | 6,830.00 USD | `-41.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,900,000.00 USD | 0.00 USD | 137.16 USD | `-41.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,900,000.00 USD | 0.00 USD | 504.41 USD | `-40.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,900,000.00 USD | 0.00 USD | 963.93 USD | `-40.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,900,000.00 USD | 0.00 USD | 6,690.00 USD | `-40.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,890,000.00 USD | 0.00 USD | 541.98 USD | `-40.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,890,000.00 USD | 0.00 USD | 108.75 USD | `-39.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,890,000.00 USD | 0.00 USD | 766.55 USD | `-39.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,890,000.00 USD | 0.00 USD | 7,110.00 USD | `-39.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,880,000.00 USD | 0.00 USD | 1,100.00 USD | `-38.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,880,000.00 USD | 0.00 USD | 100.04 USD | `-38.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,880,000.00 USD | 0.00 USD | 1,220.00 USD | `-37.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,880,000.00 USD | 0.00 USD | 5,090.00 USD | `-37.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,880,000.00 USD | 0.00 USD | 226.57 USD | `-36.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,880,000.00 USD | 0.00 USD | 104.98 USD | `-35.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,880,000.00 USD | 0.00 USD | 889.89 USD | `-35.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,870,000.00 USD | 0.00 USD | 7,270.00 USD | `-35.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,870,000.00 USD | 0.00 USD | 107.21 USD | `-34.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,870,000.00 USD | 0.00 USD | 197.37 USD | `-34.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,870,000.00 USD | 0.00 USD | 8,110.00 USD | `-34.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,860,000.00 USD | 0.00 USD | 108.39 USD | `-34.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,860,000.00 USD | 0.00 USD | 435.95 USD | `-33.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,860,000.00 USD | 0.00 USD | 217.23 USD | `-33.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,860,000.00 USD | 0.00 USD | 437.98 USD | `-33.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,860,000.00 USD | 0.00 USD | 2,720.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,850,000.00 USD | 0.00 USD | 8,380.00 USD | `-32.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,850,000.00 USD | 0.00 USD | 283.50 USD | `-32.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,850,000.00 USD | 0.00 USD | 109.53 USD | `-32.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,850,000.00 USD | 0.00 USD | 1,230.00 USD | `-31.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,840,000.00 USD | 0.00 USD | 1,960.00 USD | `-31.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,840,000.00 USD | 0.00 USD | 157.81 USD | `-31.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,840,000.00 USD | 0.00 USD | 2,900.00 USD | `-30.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,840,000.00 USD | 0.00 USD | 4,870.00 USD | `-30.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,830,000.00 USD | 0.00 USD | 1,320.00 USD | `-30.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,830,000.00 USD | 0.00 USD | 358.90 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,830,000.00 USD | 0.00 USD | 15,370.00 USD | `-29.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,820,000.00 USD | 0.00 USD | 738.75 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,820,000.00 USD | 0.00 USD | 523.32 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,820,000.00 USD | 0.00 USD | 4,470.00 USD | `-29.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,810,000.00 USD | 0.00 USD | 22,950.00 USD | `-28.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,790,000.00 USD | 0.00 USD | 1,020.00 USD | `-28.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,790,000.00 USD | 0.00 USD | 214.57 USD | `-27.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,790,000.00 USD | 0.00 USD | 249.08 USD | `-27.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,790,000.00 USD | 0.00 USD | 305.50 USD | `-27.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,790,000.00 USD | 0.00 USD | 109.42 USD | `-26.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,790,000.00 USD | 0.00 USD | 9,300.00 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,780,000.00 USD | 0.00 USD | 8,570.00 USD | `-25.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,770,000.00 USD | 0.00 USD | 104.69 USD | `-25.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,770,000.00 USD | 0.00 USD | 315.69 USD | `-25.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,770,000.00 USD | 0.00 USD | 17,510.00 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,750,000.00 USD | 0.00 USD | 269,150.00 USD | `-24.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,480,000.00 USD | 0.00 USD | 4,210.00 USD | `-24.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,480,000.00 USD | 0.00 USD | 1,030.00 USD | `-24.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,480,000.00 USD | 0.00 USD | 218.81 USD | `-24.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,480,000.00 USD | 0.00 USD | 24,840.00 USD | `-23.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,450,000.00 USD | 0.00 USD | 144.67 USD | `-23.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,450,000.00 USD | 0.00 USD | 27,380.00 USD | `-22.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,420,000.00 USD | 0.00 USD | 1,670.00 USD | `-22.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,420,000.00 USD | 0.00 USD | 104.81 USD | `-22.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,420,000.00 USD | 0.00 USD | 200.10 USD | `-21.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,420,000.00 USD | 0.00 USD | 1,480.00 USD | `-21.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,420,000.00 USD | 0.00 USD | 1,870.00 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,420,000.00 USD | 0.00 USD | 18,240.00 USD | `-21.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,400,000.00 USD | 0.00 USD | 240.67 USD | `-20.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,400,000.00 USD | 0.00 USD | 306.56 USD | `-20.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,400,000.00 USD | 0.00 USD | 6,590.00 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 2,390,000.00 USD | 0.00 USD | 505.76 USD | `-20.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,390,000.00 USD | 0.00 USD | 73,220.00 USD | `-19.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,320,000.00 USD | 0.00 USD | 19,600.00 USD | `-19.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,300,000.00 USD | 0.00 USD | 8,490.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,290,000.00 USD | 0.00 USD | 111,650.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,180,000.00 USD | 0.00 USD | 421.41 USD | `-18.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,180,000.00 USD | 0.00 USD | 506.22 USD | `-18.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,180,000.00 USD | 0.00 USD | 171.75 USD | `-18.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,180,000.00 USD | 0.00 USD | 2,550.00 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,180,000.00 USD | 0.00 USD | 1,380.00 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,180,000.00 USD | 0.00 USD | 344.07 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,170,000.00 USD | 0.00 USD | 24,320.00 USD | `-17.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,150,000.00 USD | 0.00 USD | 156.83 USD | `-16.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,150,000.00 USD | 0.00 USD | 894.72 USD | `-16.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,150,000.00 USD | 0.00 USD | 67,780.00 USD | `-16.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,080,000.00 USD | 0.00 USD | 21,320.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,060,000.00 USD | 0.00 USD | 3,700.00 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,060,000.00 USD | 0.00 USD | 17,230.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,040,000.00 USD | 0.00 USD | 5,130.00 USD | `-15.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,030,000.00 USD | 0.00 USD | 17,420.00 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,020,000.00 USD | 0.00 USD | 18,440.00 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,000,000.00 USD | 0.00 USD | 78,170.00 USD | `-14.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,920,000.00 USD | 0.00 USD | 1,250.00 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,920,000.00 USD | 0.00 USD | 331.46 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,920,000.00 USD | 0.00 USD | 16,250.00 USD | `-14.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,900,000.00 USD | 0.00 USD | 632.99 USD | `-13.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,900,000.00 USD | 0.00 USD | 172.19 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,900,000.00 USD | 0.00 USD | 1,210.00 USD | `-13.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,900,000.00 USD | 0.00 USD | 179.33 USD | `-13.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,900,000.00 USD | 0.00 USD | 4,080.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,900,000.00 USD | 0.00 USD | 4,070.00 USD | `-12.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,890,000.00 USD | 0.00 USD | 367.50 USD | `-12.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,890,000.00 USD | 0.00 USD | 34,850.00 USD | `-12.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,860,000.00 USD | 0.00 USD | 4,370.00 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,850,000.00 USD | 0.00 USD | 234,410.00 USD | `-11.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,620,000.00 USD | 0.00 USD | 6,300.00 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,610,000.00 USD | 0.00 USD | 2,490.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,610,000.00 USD | 0.00 USD | 32,040.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,580,000.00 USD | 0.00 USD | 28,820.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,550,000.00 USD | 0.00 USD | 14,490.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,530,000.00 USD | 0.00 USD | 257,990.00 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,280,000.00 USD | 0.00 USD | 1,510.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,270,000.00 USD | 0.00 USD | 1,660.00 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,270,000.00 USD | 0.00 USD | 181,010.00 USD | `-9.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,090,000.00 USD | 0.00 USD | 7,500.00 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,080,000.00 USD | 0.00 USD | 22,340.00 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,060,000.00 USD | 0.00 USD | 36,060.00 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,030,000.00 USD | 0.00 USD | 41,340.00 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 984,680.00 USD | 0.00 USD | 43,060.00 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 941,620.00 USD | 0.00 USD | 7,710.00 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 933,920.00 USD | 0.00 USD | 8,620.00 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 925,300.00 USD | 0.00 USD | 161,080.00 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 764,210.00 USD | 0.00 USD | 57,280.00 USD | `-7.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 706,940.00 USD | 0.00 USD | 12,210.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 694,730.00 USD | 0.00 USD | 46,290.00 USD | `-6.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 648,440.00 USD | 0.00 USD | 2,340.00 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 646,100.00 USD | 0.00 USD | 5,190.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 640,910.00 USD | 0.00 USD | 934.17 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 639,970.00 USD | 0.00 USD | 3,510.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 636,460.00 USD | 0.00 USD | 5,800.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 630,660.00 USD | 0.00 USD | 37,740.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 592,920.00 USD | 0.00 USD | 317.60 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 592,600.00 USD | 0.00 USD | 3,960.00 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 588,640.00 USD | 0.00 USD | 993.16 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 587,640.00 USD | 0.00 USD | 201,270.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 386,370.00 USD | 0.00 USD | 20,520.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 365,850.00 USD | 0.00 USD | 9,590.00 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 356,260.00 USD | 0.00 USD | 1,470.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 354,800.00 USD | 0.00 USD | 16,870.00 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 337,920.00 USD | 0.00 USD | 62,450.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 275,470.00 USD | 0.00 USD | 113.41 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 275,360.00 USD | 0.00 USD | 1,290.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 274,070.00 USD | 0.00 USD | 5,360.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 268,710.00 USD | 0.00 USD | 34,290.00 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 234,410.00 USD | 0.00 USD | 410.91 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 234,000.00 USD | 0.00 USD | 1,710.00 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 232,290.00 USD | 0.00 USD | 46,570.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 185,720.00 USD | 0.00 USD | 1,120.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 184,600.00 USD | 0.00 USD | 3,280.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 181,320.00 USD | 0.00 USD | 1,730.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 179,600.00 USD | 0.00 USD | 84,840.00 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 94,760.00 USD | 0.00 USD | 2,700.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 92,060.00 USD | 0.00 USD | 92,060.00 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 371,990.00 USD | 371,990.00 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 387,080.00 USD | 15,080.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 387,870.00 USD | 791.58 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 389,000.00 USD | 1,130.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 563,570.00 USD | 174,570.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 568,760.00 USD | 5,190.00 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 603,210.00 USD | 34,450.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 605,600.00 USD | 2,390.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 628,840.00 USD | 23,230.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 667,490.00 USD | 38,650.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 701,940.00 USD | 34,450.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 729,050.00 USD | 27,110.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 729,320.00 USD | 269.26 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 731,740.00 USD | 2,420.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 733,270.00 USD | 1,540.00 USD | 0.00 USD | `+3.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 750,650.00 USD | 17,380.00 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 750,880.00 USD | 222.11 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 907,420.00 USD | 156,540.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 949,500.00 USD | 42,080.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 951,120.00 USD | 1,620.00 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 993,430.00 USD | 42,310.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 1,410,000.00 USD | 411,780.00 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,420,000.00 USD | 12,210.00 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,420,000.00 USD | 4,090.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 1,420,000.00 USD | 543.29 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 1,420,000.00 USD | 524.07 USD | 0.00 USD | `+6.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,490,000.00 USD | 71,220.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,500,000.00 USD | 2,470.00 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 1,500,000.00 USD | 1,700.00 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 1,500,000.00 USD | 1,310.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,530,000.00 USD | 29,550.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,550,000.00 USD | 20,340.00 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 1,560,000.00 USD | 13,100.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 1,610,000.00 USD | 52,300.00 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,610,000.00 USD | 200.45 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,620,000.00 USD | 1,990.00 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,620,000.00 USD | 1,190.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,620,000.00 USD | 227.79 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,620,000.00 USD | 2,030.00 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,620,000.00 USD | 1,470.00 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,670,000.00 USD | 52,450.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,700,000.00 USD | 27,250.00 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,700,000.00 USD | 289.82 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,720,000.00 USD | 20,960.00 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,720,000.00 USD | 1,100.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,730,000.00 USD | 7,380.00 USD | 0.00 USD | `+10.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,780,000.00 USD | 44,520.00 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,790,000.00 USD | 16,750.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,790,000.00 USD | 617.10 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,810,000.00 USD | 15,710.00 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,810,000.00 USD | 152.12 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,170,000.00 USD | 357,870.00 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,380,000.00 USD | 218,120.00 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,390,000.00 USD | 2,650.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,470,000.00 USD | 84,180.00 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,480,000.00 USD | 8,450.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,510,000.00 USD | 27,130.00 USD | 0.00 USD | `+13.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,520,000.00 USD | 13,030.00 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,520,000.00 USD | 2,640.00 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,270,000.00 USD | 749,110.00 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,270,000.00 USD | 559.58 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,450,000.00 USD | 176,880.00 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,480,000.00 USD | 33,510.00 USD | 0.00 USD | `+14.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,490,000.00 USD | 8,540.00 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,490,000.00 USD | 283.33 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,500,000.00 USD | 11,760.00 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,530,000.00 USD | 24,370.00 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,540,000.00 USD | 10,460.00 USD | 0.00 USD | `+16.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,550,000.00 USD | 10,400.00 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,570,000.00 USD | 19,890.00 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,570,000.00 USD | 4,060.00 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,690,000.00 USD | 120,030.00 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,690,000.00 USD | 156.30 USD | 0.00 USD | `+17.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,710,000.00 USD | 13,180.00 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,710,000.00 USD | 4,420.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,710,000.00 USD | 313.51 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,720,000.00 USD | 5,070.00 USD | 0.00 USD | `+18.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,760,000.00 USD | 47,350.00 USD | 0.00 USD | `+18.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,760,000.00 USD | 187.06 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,860,000.00 USD | 92,570.00 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,860,000.00 USD | 2,540.00 USD | 0.00 USD | `+19.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,900,000.00 USD | 40,150.00 USD | 0.00 USD | `+19.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,920,000.00 USD | 25,080.00 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,930,000.00 USD | 5,030.00 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,950,000.00 USD | 19,640.00 USD | 0.00 USD | `+20.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,950,000.00 USD | 120.58 USD | 0.00 USD | `+20.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,960,000.00 USD | 14,690.00 USD | 0.00 USD | `+20.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,970,000.00 USD | 6,090.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,060,000.00 USD | 87,290.00 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,060,000.00 USD | 5,640.00 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,060,000.00 USD | 178.33 USD | 0.00 USD | `+21.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,130,000.00 USD | 68,210.00 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,150,000.00 USD | 15,350.00 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,150,000.00 USD | 179.38 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,150,000.00 USD | 179.72 USD | 0.00 USD | `+22.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,150,000.00 USD | 217.63 USD | 0.00 USD | `+22.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,150,000.00 USD | 493.85 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,150,000.00 USD | 575.38 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,150,000.00 USD | 327.58 USD | 0.00 USD | `+23.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,150,000.00 USD | 163.85 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,270,000.00 USD | 120,930.00 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,310,000.00 USD | 38,410.00 USD | 0.00 USD | `+24.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,310,000.00 USD | 1,710.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,310,000.00 USD | 432.63 USD | 0.00 USD | `+24.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,310,000.00 USD | 2,620.00 USD | 0.00 USD | `+24.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,310,000.00 USD | 537.61 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,730,000.00 USD | 420,400.00 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,730,000.00 USD | 278.52 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,730,000.00 USD | 589.22 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,730,000.00 USD | 733.03 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,740,000.00 USD | 423.60 USD | 0.00 USD | `+26.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,750,000.00 USD | 10,930.00 USD | 0.00 USD | `+26.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,750,000.00 USD | 381.09 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,750,000.00 USD | 961.16 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,750,000.00 USD | 1,570.00 USD | 0.00 USD | `+27.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,750,000.00 USD | 5,650.00 USD | 0.00 USD | `+27.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,750,000.00 USD | 160.11 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,760,000.00 USD | 225.33 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,760,000.00 USD | 438.60 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,760,000.00 USD | 6,800.00 USD | 0.00 USD | `+28.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,800,000.00 USD | 40,880.00 USD | 0.00 USD | `+28.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,820,000.00 USD | 19,950.00 USD | 0.00 USD | `+28.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,820,000.00 USD | 270.75 USD | 0.00 USD | `+29.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,820,000.00 USD | 639.61 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,830,000.00 USD | 1,710.00 USD | 0.00 USD | `+29.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,840,000.00 USD | 12,600.00 USD | 0.00 USD | `+29.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,840,000.00 USD | 1,020.00 USD | 0.00 USD | `+30.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,030,000.00 USD | 192,640.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 5,060,000.00 USD | 30,110.00 USD | 0.00 USD | `+30.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 5,100,000.00 USD | 38,920.00 USD | 0.00 USD | `+30.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,100,000.00 USD | 1,180.00 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,070,000.00 USD | 968,550.00 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,080,000.00 USD | 5,600.00 USD | 0.00 USD | `+31.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,100,000.00 USD | 19,110.00 USD | 0.00 USD | `+31.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,110,000.00 USD | 18,790.00 USD | 0.00 USD | `+32.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,170,000.00 USD | 58,030.00 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,220,000.00 USD | 46,110.00 USD | 0.00 USD | `+32.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,230,000.00 USD | 14,320.00 USD | 0.00 USD | `+32.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,240,000.00 USD | 11,740.00 USD | 0.00 USD | `+32.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,270,000.00 USD | 20,540.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,270,000.00 USD | 384.94 USD | 0.00 USD | `+33.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,270,000.00 USD | 573.39 USD | 0.00 USD | `+33.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,270,000.00 USD | 347.06 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,270,000.00 USD | 491.11 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,270,000.00 USD | 3,290.00 USD | 0.00 USD | `+34.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,270,000.00 USD | 281.55 USD | 0.00 USD | `+35.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,280,000.00 USD | 6,590.00 USD | 0.00 USD | `+35.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 6,280,000.00 USD | 586.69 USD | 0.00 USD | `+35.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,280,000.00 USD | 5,860.00 USD | 0.00 USD | `+35.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,390,000.00 USD | 103,470.00 USD | 0.00 USD | `+36.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,390,000.00 USD | 705.23 USD | 0.00 USD | `+36.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,390,000.00 USD | 5,720.00 USD | 0.00 USD | `+36.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,390,000.00 USD | 139.03 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,400,000.00 USD | 2,450.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,400,000.00 USD | 1,850.00 USD | 0.00 USD | `+37.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,400,000.00 USD | 286.94 USD | 0.00 USD | `+37.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,410,000.00 USD | 7,120.00 USD | 0.00 USD | `+38.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,410,000.00 USD | 329.13 USD | 0.00 USD | `+38.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,410,000.00 USD | 1,970.00 USD | 0.00 USD | `+38.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,410,000.00 USD | 1,020.00 USD | 0.00 USD | `+39.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,410,000.00 USD | 1,150.00 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,410,000.00 USD | 1,190.00 USD | 0.00 USD | `+39.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,410,000.00 USD | 1,770.00 USD | 0.00 USD | `+39.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,420,000.00 USD | 3,450.00 USD | 0.00 USD | `+40.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,420,000.00 USD | 345.45 USD | 0.00 USD | `+40.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,500,000.00 USD | 81,630.00 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,500,000.00 USD | 2,510.00 USD | 0.00 USD | `+41.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,500,000.00 USD | 1,020.00 USD | 0.00 USD | `+41.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,650,000.00 USD | 153,150.00 USD | 0.00 USD | `+41.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,680,000.00 USD | 26,180.00 USD | 0.00 USD | `+42.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,690,000.00 USD | 5,440.00 USD | 0.00 USD | `+42.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,700,000.00 USD | 8,940.00 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,810,000.00 USD | 119,340.00 USD | 0.00 USD | `+42.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,820,000.00 USD | 3,000.00 USD | 0.00 USD | `+42.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,020,000.00 USD | 201,800.00 USD | 0.00 USD | `+43.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,030,000.00 USD | 13,710.00 USD | 0.00 USD | `+43.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,120,000.00 USD | 90,380.00 USD | 0.00 USD | `+43.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,130,000.00 USD | 2,170.00 USD | 0.00 USD | `+43.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,130,000.00 USD | 3,300.00 USD | 0.00 USD | `+44.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,130,000.00 USD | 1,040.00 USD | 0.00 USD | `+44.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,130,000.00 USD | 425.76 USD | 0.00 USD | `+44.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,130,000.00 USD | 2,030.00 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,140,000.00 USD | 4,120.00 USD | 0.00 USD | `+45.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,140,000.00 USD | 2,000.00 USD | 0.00 USD | `+45.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,200,000.00 USD | 61,050.00 USD | 0.00 USD | `+45.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,200,000.00 USD | 1,610.00 USD | 0.00 USD | `+45.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,200,000.00 USD | 1,200.00 USD | 0.00 USD | `+46.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,200,000.00 USD | 420.32 USD | 0.00 USD | `+46.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,200,000.00 USD | 1,940.00 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,210,000.00 USD | 4,010.00 USD | 0.00 USD | `+47.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,270,000.00 USD | 66,060.00 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,280,000.00 USD | 1,890.00 USD | 0.00 USD | `+48.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,280,000.00 USD | 195.46 USD | 0.00 USD | `+48.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,280,000.00 USD | 289.93 USD | 0.00 USD | `+48.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 7,280,000.00 USD | 116.16 USD | 0.00 USD | `+48.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,280,000.00 USD | 7,310.00 USD | 0.00 USD | `+50.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,280,000.00 USD | 310.70 USD | 0.00 USD | `+50.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,290,000.00 USD | 325.62 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,290,000.00 USD | 1,760.00 USD | 0.00 USD | `+51.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,290,000.00 USD | 3,230.00 USD | 0.00 USD | `+52.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,300,000.00 USD | 5,120.00 USD | 0.00 USD | `+52.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,300,000.00 USD | 1,310.00 USD | 0.00 USD | `+54.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,330,000.00 USD | 30,990.00 USD | 0.00 USD | `+55.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,330,000.00 USD | 104.24 USD | 0.00 USD | `+55.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,340,000.00 USD | 13,580.00 USD | 0.00 USD | `+56.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,340,000.00 USD | 1,630.00 USD | 0.00 USD | `+57.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 7,340,000.00 USD | 1,370.00 USD | 0.00 USD | `+57.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,350,000.00 USD | 5,400.00 USD | 0.00 USD | `+57.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,350,000.00 USD | 1,620.00 USD | 0.00 USD | `+57.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,350,000.00 USD | 3,220.00 USD | 0.00 USD | `+58.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,360,000.00 USD | 450.55 USD | 0.00 USD | `+58.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,360,000.00 USD | 3,060.00 USD | 0.00 USD | `+59.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,360,000.00 USD | 3,070.00 USD | 0.00 USD | `+59.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,360,000.00 USD | 3,120.00 USD | 0.00 USD | `+60.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,370,000.00 USD | 1,550.00 USD | 0.00 USD | `+60.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,370,000.00 USD | 3,080.00 USD | 0.00 USD | `+61.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,370,000.00 USD | 647.56 USD | 0.00 USD | `+62.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,370,000.00 USD | 1,420.00 USD | 0.00 USD | `+62.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,370,000.00 USD | 2,130.00 USD | 0.00 USD | `+62.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,380,000.00 USD | 6,870.00 USD | 0.00 USD | `+62.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,380,000.00 USD | 342.25 USD | 0.00 USD | `+63.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,380,000.00 USD | 2,990.00 USD | 0.00 USD | `+63.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,390,000.00 USD | 2,970.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,390,000.00 USD | 324.54 USD | 0.00 USD | `+64.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,390,000.00 USD | 504.21 USD | 0.00 USD | `+65.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,390,000.00 USD | 166.00 USD | 0.00 USD | `+66.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,390,000.00 USD | 4,190.00 USD | 0.00 USD | `+66.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,400,000.00 USD | 12,970.00 USD | 0.00 USD | `+67.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,410,000.00 USD | 2,860.00 USD | 0.00 USD | `+68.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,410,000.00 USD | 264.31 USD | 0.00 USD | `+69.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,410,000.00 USD | 599.34 USD | 0.00 USD | `+70.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,410,000.00 USD | 193.19 USD | 0.00 USD | `+70.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,410,000.00 USD | 3,950.00 USD | 0.00 USD | `+71.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,410,000.00 USD | 1,940.00 USD | 0.00 USD | `+72.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,570,000.00 USD | 160,550.00 USD | 0.00 USD | `+72.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,580,000.00 USD | 1,290.00 USD | 0.00 USD | `+73.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,580,000.00 USD | 1,180.00 USD | 0.00 USD | `+74.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,580,000.00 USD | 630.05 USD | 0.00 USD | `+76.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,580,000.00 USD | 1,410.00 USD | 0.00 USD | `+76.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,580,000.00 USD | 2,610.00 USD | 0.00 USD | `+76.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,590,000.00 USD | 7,630.00 USD | 0.00 USD | `+79.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,590,000.00 USD | 4,640.00 USD | 0.00 USD | `+80.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,590,000.00 USD | 371.88 USD | 0.00 USD | `+81.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,600,000.00 USD | 2,510.00 USD | 0.00 USD | `+81.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,600,000.00 USD | 380.68 USD | 0.00 USD | `+83.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,600,000.00 USD | 1,470.00 USD | 0.00 USD | `+85.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,610,000.00 USD | 11,170.00 USD | 0.00 USD | `+85.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,640,000.00 USD | 34,360.00 USD | 0.00 USD | `+86.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,640,000.00 USD | 253.21 USD | 0.00 USD | `+86.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,640,000.00 USD | 100.29 USD | 0.00 USD | `+86.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,660,000.00 USD | 10,610.00 USD | 0.00 USD | `+89.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,660,000.00 USD | 309.43 USD | 0.00 USD | `+90.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,690,000.00 USD | 36,740.00 USD | 0.00 USD | `+90.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,770,000.00 USD | 81,310.00 USD | 0.00 USD | `+91.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 7,780,000.00 USD | 1,390.00 USD | 0.00 USD | `+93.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,780,000.00 USD | 216.90 USD | 0.00 USD | `+95.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,780,000.00 USD | 1,990.00 USD | 0.00 USD | `+95.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,780,000.00 USD | 7,200.00 USD | 0.00 USD | `+95.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 7,790,000.00 USD | 1,350.00 USD | 0.00 USD | `+98.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,840,000.00 USD | 56,000.00 USD | 0.00 USD | `+100.00%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.48` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,130.00 USD |
| `7D` | `3.50` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD |
| `7D` | `3.51` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD |
| `7D` | `3.52` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `3.53` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD |
| `7D` | `3.54` | 13,460,000.00 USD | 0.00 USD | 13,460,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD |
| `7D` | `3.55` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD |
| `7D` | `3.56` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD |
| `7D` | `3.57` | 13,080,000.00 USD | 0.00 USD | 13,080,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD |
| `7D` | `3.58` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD |
| `7D` | `3.59` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD |
| `7D` | `3.60` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 12,330,000.00 USD | 0.00 USD | 12,330,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `7D` | `3.63` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `7D` | `3.64` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD |
| `7D` | `3.65` | 11,890,000.00 USD | 0.00 USD | 11,890,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD |
| `7D` | `3.66` | 11,800,000.00 USD | 0.00 USD | 11,800,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD |
| `7D` | `3.67` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD |
| `7D` | `3.68` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.69` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `7D` | `3.70` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `1D` | `3.71` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 56,160.00 USD | 4,110.00 USD | 55,260.00 USD |
| `7D` | `3.71` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD |
| `1D` | `3.72` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 18,460.00 USD | 0.00 USD | 330.84 USD |
| `7D` | `3.72` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `1D` | `3.73` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 405.02 USD | 11,920.00 USD | 25,870.00 USD |
| `7D` | `3.73` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 108,320.00 USD | 56,340.00 USD | 83,320.00 USD |
| `7D` | `3.74` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD |
| `1D` | `3.75` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 1,720.00 USD | 0.00 USD | 50,350.00 USD |
| `7D` | `3.75` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD |
| `1D` | `3.76` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 1,260.00 USD | 8,310.00 USD | 144.08 USD |
| `7D` | `3.76` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `1D` | `3.77` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 48,010.00 USD | 54,910.00 USD | 17,430.00 USD |
| `7D` | `3.77` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD |
| `1D` | `3.78` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 4,250.00 USD | 0.00 USD | 20,180.00 USD |
| `7D` | `3.78` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 11,780,000.00 USD | 0.00 USD | 11,780,000.00 USD | 4,270.00 USD | 24,440.00 USD | 68,640.00 USD |
| `7D` | `3.79` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD |
| `1D` | `3.80` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 3,400.00 USD | 0.00 USD | 74,400.00 USD |
| `7D` | `3.80` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 6,530.00 USD | 18,170.00 USD | 17,780.00 USD |
| `1D` | `3.81` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 212,830.00 USD | 0.00 USD | 78,340.00 USD |
| `7D` | `3.81` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 5,310.00 USD | 0.00 USD | 1,350.00 USD |
| `1D` | `3.82` | 11,320,000.00 USD | 0.00 USD | 11,320,000.00 USD | 3,240.00 USD | 21,590.00 USD | 115,290.00 USD |
| `7D` | `3.82` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 11,180,000.00 USD | 0.00 USD | 11,180,000.00 USD | 93,470.00 USD | 91,390.00 USD | 114,510.00 USD |
| `7D` | `3.83` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 0.00 USD | 33,630.00 USD | 89.29 USD |
| `1D` | `3.84` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 150,080.00 USD | 33,720.00 USD | 32,470.00 USD |
| `7D` | `3.84` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 7,940.00 USD | 33,350.00 USD | 0.00 USD |
| `1D` | `3.85` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 156,570.00 USD | 160,920.00 USD | 545.16 USD |
| `7D` | `3.85` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 3,390.00 USD | 49,170.00 USD | 5,500.00 USD |
| `1D` | `3.86` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 39,850.00 USD | 46,130.00 USD | 106,800.00 USD |
| `7D` | `3.86` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 5,190.00 USD | 156,620.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 3,490.00 USD | 70,020.00 USD | 153,250.00 USD |
| `7D` | `3.87` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 63,710.00 USD | 0.00 USD | 227,340.00 USD |
| `1D` | `3.88` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 109,330.00 USD | 24,380.00 USD | 228,270.00 USD |
| `7D` | `3.88` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 110,160.00 USD | 77,860.00 USD | 101,810.00 USD |
| `1D` | `3.89` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 446,590.00 USD | 91,430.00 USD | 195,740.00 USD |
| `7D` | `3.89` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD |
| `1D` | `3.90` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 32,970.00 USD | 59,980.00 USD | 244,090.00 USD |
| `7D` | `3.90` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,480.00 USD |
| `1D` | `3.91` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 337,210.00 USD | 120,100.00 USD | 262,860.00 USD |
| `7D` | `3.91` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 121,570.00 USD | 67,260.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 317,510.00 USD | 8,570.00 USD | 127,670.00 USD |
| `7D` | `3.92` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 85,790.00 USD | 66,710.00 USD | 104,900.00 USD |
| `1D` | `3.93` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,520.00 USD |
| `7D` | `3.93` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 30,960.00 USD | 28,720.00 USD | 67.04 USD |
| `1D` | `3.94` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 132,520.00 USD | 53,060.00 USD | 137,210.00 USD |
| `7D` | `3.94` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 52,810.00 USD | 0.00 USD | 2,150.00 USD |
| `1D` | `3.95` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 114,710.00 USD | 0.00 USD | 32,990.00 USD |
| `7D` | `3.95` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 8,490.00 USD | 0.00 USD | 2,700.00 USD |
| `1D` | `3.96` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 66,520.00 USD | 22,830.00 USD | 17,260.00 USD |
| `7D` | `3.96` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 165,060.00 USD | 0.00 USD | 226.33 USD |
| `1D` | `3.97` | 6,430,000.00 USD | 0.00 USD | 6,430,000.00 USD | 942.71 USD | 36,470.00 USD | 137,530.00 USD |
| `7D` | `3.97` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 235,890.00 USD | 0.00 USD | 2,880.00 USD |
| `1D` | `3.98` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 19,950.00 USD | 76,990.00 USD | 94,420.00 USD |
| `7D` | `3.98` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 506,280.00 USD | 0.00 USD | 279,530.00 USD |
| `1D` | `3.99` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,190.00 USD |
| `7D` | `3.99` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,470.00 USD |
| `1D` | `4.00` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 39,240.00 USD | 17,140.00 USD | 137,600.00 USD |
| `7D` | `4.00` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,460.00 USD |
| `1D` | `4.01` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 473.90 USD | 158,450.00 USD | 222,680.00 USD |
| `7D` | `4.01` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 368,350.00 USD | 57,440.00 USD | 438,650.00 USD |
| `1D` | `4.02` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 132,300.00 USD | 52,150.00 USD | 125,070.00 USD |
| `7D` | `4.02` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 271,690.00 USD | 156,620.00 USD | 250,940.00 USD |
| `1D` | `4.03` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 38,390.00 USD | 48,890.00 USD | 0.00 USD |
| `7D` | `4.03` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 245,910.00 USD | 0.00 USD | 344,620.00 USD |
| `1D` | `4.04` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 66,450.00 USD | 21,940.00 USD | 183,170.00 USD |
| `7D` | `4.04` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 321,230.00 USD | 0.00 USD | 491,990.00 USD |
| `1D` | `4.05` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 347,800.00 USD | 23,720.00 USD | 56.80 USD |
| `1D` | `4.06` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 34,760.00 USD | 72,940.00 USD | 386,930.00 USD |
| `7D` | `4.06` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 72,410.00 USD | 0.00 USD |
| `1D` | `4.07` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 242,710.00 USD | 179,680.00 USD | 240,980.00 USD |
| `7D` | `4.07` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 287,180.00 USD | 166,480.00 USD |
| `1D` | `4.08` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 68,020.00 USD | 215,680.00 USD | 79,930.00 USD |
| `7D` | `4.08` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 0.00 USD | 237,170.00 USD | 0.00 USD |
| `1D` | `4.09` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 163,310.00 USD | 27,940.00 USD | 168,050.00 USD |
| `7D` | `4.09` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 127,170.00 USD | 137,180.00 USD | 432,940.00 USD |
| `1D` | `4.10` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 0.00 USD | 58,480.00 USD | 61,980.00 USD |
| `7D` | `4.10` | 992,360.00 USD | 0.00 USD | 992,360.00 USD | 24,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.11` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 45,020.00 USD | 80,610.00 USD | 223,150.00 USD |
| `7D` | `4.11` | 967,460.00 USD | 0.00 USD | 967,460.00 USD | 0.00 USD | 0.00 USD | 98,730.00 USD |
| `1D` | `4.12` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 379,180.00 USD |
| `7D` | `4.12` | 868,740.00 USD | 0.00 USD | 868,740.00 USD | 0.00 USD | 137,940.00 USD | 0.00 USD |
| `1D` | `4.13` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 310,560.00 USD |
| `7D` | `4.13` | 730,800.00 USD | 0.00 USD | 730,800.00 USD | 0.00 USD | 0.00 USD | 164,000.00 USD |
| `1D` | `4.14` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.14` | 566,800.00 USD | 0.00 USD | 566,800.00 USD | 238,150.00 USD | 90,830.00 USD | 0.00 USD |
| `1D` | `4.15` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 469,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.15` | 237,830.00 USD | 0.00 USD | 237,830.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.16` | 671,560.00 USD | 0.00 USD | 671,560.00 USD | 47,820.00 USD | 0.00 USD | 103,230.00 USD |
| `1D` | `4.17` | 520,510.00 USD | 0.00 USD | 520,510.00 USD | 58,020.00 USD | 94,940.00 USD | 37,730.00 USD |
| `1D` | `4.18` | 329,810.00 USD | 0.00 USD | 329,810.00 USD | 329,080.00 USD | 0.00 USD | 327.27 USD |
| `1D` | `4.19` | 405.08 USD | 0.00 USD | 405.08 USD | 0.00 USD | 0.00 USD | 405.08 USD |
| `7D` | `4.19` | 2,760.00 USD | 0.00 USD | 2,760.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.20` | 139,540.00 USD | 139,540.00 USD | 0.00 USD | 66,990.00 USD | 0.00 USD | 72,550.00 USD |
| `1D` | `4.20` | 279,080.00 USD | 279,080.00 USD | 0.00 USD | 66,990.00 USD | 0.00 USD | 72,550.00 USD |
| `7D` | `4.20` | 599,320.00 USD | 599,320.00 USD | 0.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD |
| `7D` | `4.20` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 588,990.00 USD | 588,990.00 USD | 0.00 USD | 168,700.00 USD | 98,820.00 USD | 42,390.00 USD |
| `7D` | `4.21` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 2,900.00 USD | 0.00 USD | 82,000.00 USD |
| `1D` | `4.22` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 97,990.00 USD | 129,920.00 USD | 308,200.00 USD |
| `7D` | `4.22` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 121,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.23` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 1,340.00 USD | 427,200.00 USD | 222,270.00 USD |
| `7D` | `4.23` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 117,530.00 USD | 0.00 USD | 166,480.00 USD |
| `1D` | `4.24` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 631.50 USD | 137,280.00 USD | 341.30 USD |
| `7D` | `4.24` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 2,900.00 USD | 52,690.00 USD | 95,800.00 USD |
| `1D` | `4.25` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 4,080.00 USD | 0.00 USD | 501,390.00 USD |
| `7D` | `4.25` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 3,390.00 USD | 223,240.00 USD | 432,940.00 USD |
| `1D` | `4.26` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 150,470.00 USD | 0.00 USD | 303.65 USD |
| `7D` | `4.26` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 2,960.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 712,140.00 USD | 72,370.00 USD | 274,350.00 USD |
| `7D` | `4.27` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 24,810.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 125,880.00 USD | 41,380.00 USD | 285,430.00 USD |
| `7D` | `4.28` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 119,230.00 USD | 497,680.00 USD | 1,300,000.00 USD |
| `1D` | `4.29` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 156,040.00 USD | 32,690.00 USD | 162,030.00 USD |
| `7D` | `4.29` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 5,150.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 65,250.00 USD | 56,980.00 USD | 163,400.00 USD |
| `7D` | `4.30` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 376,510.00 USD | 50,050.00 USD | 194,500.00 USD |
| `7D` | `4.31` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 215,700.00 USD | 53,890.00 USD | 170,400.00 USD |
| `1D` | `4.32` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 155,370.00 USD | 106,760.00 USD | 197,980.00 USD |
| `7D` | `4.32` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 268,260.00 USD | 160,980.00 USD | 306,170.00 USD |
| `1D` | `4.33` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 292,220.00 USD | 158,240.00 USD | 126,730.00 USD |
| `7D` | `4.33` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 8,950.00 USD | 84,830.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 273,450.00 USD | 179,610.00 USD | 189,360.00 USD |
| `7D` | `4.34` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 9,550.00 USD | 97,260.00 USD | 358,370.00 USD |
| `1D` | `4.35` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 2,840.00 USD | 94,890.00 USD | 181,100.00 USD |
| `7D` | `4.35` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 108,840.00 USD | 31,050.00 USD | 122,000.00 USD |
| `7D` | `4.36` | 9,530,000.00 USD | 9,530,000.00 USD | 0.00 USD | 10,460.00 USD | 0.00 USD | 140,550.00 USD |
| `1D` | `4.37` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 110,040.00 USD | 46,860.00 USD | 157,530.00 USD |
| `1D` | `4.38` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 250,760.00 USD | 34,500.00 USD | 581,430.00 USD |
| `7D` | `4.38` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 37,480.00 USD | 41,380.00 USD | 330,520.00 USD |
| `7D` | `4.39` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 252,620.00 USD | 108,260.00 USD | 154,000.00 USD |
| `1D` | `4.40` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 385,030.00 USD | 47,530.00 USD | 93,950.00 USD |
| `7D` | `4.40` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 111,810.00 USD | 26,950.00 USD | 463,990.00 USD |
| `1D` | `4.41` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 221,770.00 USD | 130,890.00 USD | 115,220.00 USD |
| `7D` | `4.41` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 1,450.00 USD | 65,600.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 1,080.00 USD | 80,300.00 USD | 22,170.00 USD |
| `7D` | `4.42` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 6,140.00 USD | 77,340.00 USD | 114,240.00 USD |
| `7D` | `4.43` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD |
| `1D` | `4.44` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 154,690.00 USD | 339,100.00 USD | 292,720.00 USD |
| `7D` | `4.44` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 143,990.00 USD | 72,830.00 USD |
| `1D` | `4.45` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 1,750.00 USD | 50,720.00 USD | 1,780.00 USD |
| `1D` | `4.46` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 2,300.00 USD | 24,070.00 USD | 3,290.00 USD |
| `7D` | `4.46` | 12,610,000.00 USD | 12,610,000.00 USD | 0.00 USD | 3,070.00 USD | 62,110.00 USD | 2,220.00 USD |
| `1D` | `4.47` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 1,030.00 USD | 25,190.00 USD | 32,390.00 USD |
| `7D` | `4.47` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 204,140.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 167,410.00 USD | 86,520.00 USD | 25,450.00 USD |
| `7D` | `4.48` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `4.49` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 253,770.00 USD | 155,000.00 USD | 162,970.00 USD |
| `7D` | `4.49` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 244,370.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 362,590.00 USD | 69,580.00 USD | 149,180.00 USD |
| `7D` | `4.50` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 374,250.00 USD | 200,700.00 USD | 1,820.00 USD |
| `1D` | `4.51` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 187,350.00 USD | 223,860.00 USD | 325,290.00 USD |
| `7D` | `4.51` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `4.52` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 287,830.00 USD | 92,260.00 USD | 242,940.00 USD |
| `7D` | `4.52` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 501,550.00 USD | 0.00 USD | 281,140.00 USD |
| `7D` | `4.53` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 439,420.00 USD | 232,800.00 USD | 309,670.00 USD |
| `1D` | `4.54` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 12,950.00 USD | 150,600.00 USD | 234,050.00 USD |
| `7D` | `4.54` | 16,310,000.00 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 15,490,000.00 USD | 15,490,000.00 USD | 0.00 USD | 170.61 USD | 34,450.00 USD | 109,260.00 USD |
| `1D` | `4.56` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD |
| `7D` | `4.56` | 16,800,000.00 USD | 16,800,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 177,440.00 USD | 70,180.00 USD | 99,290.00 USD |
| `7D` | `4.57` | 17,340,000.00 USD | 17,340,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD |
| `1D` | `4.58` | 17,390,000.00 USD | 17,390,000.00 USD | 0.00 USD | 420,740.00 USD | 99,430.00 USD | 633,960.00 USD |
| `7D` | `4.58` | 17,470,000.00 USD | 17,470,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 454,840.00 USD | 75,460.00 USD | 109,520.00 USD |
| `7D` | `4.59` | 19,180,000.00 USD | 19,180,000.00 USD | 0.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD |
| `1D` | `4.60` | 18,210,000.00 USD | 18,210,000.00 USD | 0.00 USD | 54,700.00 USD | 50,860.00 USD | 67,260.00 USD |
| `7D` | `4.60` | 19,300,000.00 USD | 19,300,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 66,880.00 USD | 7,560.00 USD | 76,080.00 USD |
| `7D` | `4.61` | 19,310,000.00 USD | 19,310,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD |
| `1D` | `4.62` | 18,500,000.00 USD | 18,500,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD |
| `7D` | `4.62` | 19,440,000.00 USD | 19,440,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `4.63` | 18,500,000.00 USD | 18,500,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 335.46 USD |
| `7D` | `4.63` | 19,660,000.00 USD | 19,660,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 118,230.00 USD | 11,270.00 USD | 41,360.00 USD |
| `7D` | `4.64` | 20,180,000.00 USD | 20,180,000.00 USD | 0.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD |
| `1D` | `4.65` | 19,390,000.00 USD | 19,390,000.00 USD | 0.00 USD | 201,570.00 USD | 52,020.00 USD | 461,040.00 USD |
| `7D` | `4.65` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD |
| `1D` | `4.66` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 156,340.00 USD | 299,030.00 USD | 270,640.00 USD |
| `7D` | `4.66` | 20,920,000.00 USD | 20,920,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 88,770.00 USD | 0.00 USD | 259,350.00 USD |
| `7D` | `4.67` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 59,770.00 USD | 81,340.00 USD | 37,000.00 USD |
| `7D` | `4.68` | 21,880,000.00 USD | 21,880,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 137,640.00 USD | 40,000.00 USD | 168,800.00 USD |
| `7D` | `4.69` | 21,970,000.00 USD | 21,970,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 21,290,000.00 USD | 21,290,000.00 USD | 0.00 USD | 70,410.00 USD | 85,020.00 USD | 143,500.00 USD |
| `7D` | `4.70` | 22,280,000.00 USD | 22,280,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 22,250,000.00 USD | 22,250,000.00 USD | 0.00 USD | 361,050.00 USD | 284,360.00 USD | 316,290.00 USD |
| `7D` | `4.71` | 22,690,000.00 USD | 22,690,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `1D` | `4.72` | 22,540,000.00 USD | 22,540,000.00 USD | 0.00 USD | 3,450.00 USD | 188,370.00 USD | 103,550.00 USD |
| `7D` | `4.72` | 22,880,000.00 USD | 22,880,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 22,630,000.00 USD | 22,630,000.00 USD | 0.00 USD | 52,120.00 USD | 37,010.00 USD | 0.00 USD |
| `7D` | `4.73` | 22,960,000.00 USD | 22,960,000.00 USD | 0.00 USD | 59,970.00 USD | 15,660.00 USD | 894.74 USD |
| `7D` | `4.74` | 23,270,000.00 USD | 23,270,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `7D` | `4.75` | 23,820,000.00 USD | 23,820,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `7D` | `4.76` | 25,160,000.00 USD | 25,160,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD |
| `7D` | `4.77` | 26,070,000.00 USD | 26,070,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `7D` | `4.78` | 27,200,000.00 USD | 27,200,000.00 USD | 0.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD |
| `7D` | `4.79` | 28,240,000.00 USD | 28,240,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `7D` | `4.80` | 29,830,000.00 USD | 29,830,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `7D` | `4.81` | 30,460,000.00 USD | 30,460,000.00 USD | 0.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD |
| `7D` | `4.82` | 33,220,000.00 USD | 33,220,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `7D` | `4.83` | 34,870,000.00 USD | 34,870,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 35,360,000.00 USD | 35,360,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 37,400,000.00 USD | 37,400,000.00 USD | 0.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 38,800,000.00 USD | 38,800,000.00 USD | 0.00 USD | 437,750.00 USD | 162,380.00 USD | 800,900.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.09B` | Total OI Tokens: `261,149,958.0 NEAR`
  * 1h OI Change: `-2.65%` | 4h OI Change: `+4.46%` | 24h OI Change: `-14.57%`
  * Exchange Breakdown: Binance=`200.60M` | Bybit=`144.51M` | OKX=`50.14M` | Hyperliquid=`237.81M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-60.12K` | Last 24h: `59.84K` | Last 3d: `308.79K` | Last 7d: `236.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0001%` | **USDT OKX** | `-0.0258%` |
| **USDT Bybit** | `-0.0326%` | **USDT KuCoin** | `0.0097%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-0.0004%` |
| **USDT Gate** | `-0.0353%` | **USDT Bitget** | `-0.0215%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `35.29%` | `64.71%` | `0.55` | 7,360,000.00 USD |
| `15M` | `Binance` | `43.57%` | `56.43%` | `0.77` | 2,340,000.00 USD |
| `15M` | `OKX` | `45.55%` | `54.45%` | `0.84` | 557,720.00 USD |
| `15M` | `Bybit` | `27.81%` | `72.19%` | `0.39` | 971,350.00 USD |
| `15M` | `KuCoin` | `32.95%` | `67.05%` | `0.49` | 35,150.00 USD |
| `15M` | `Gate` | `20.78%` | `79.22%` | `0.26` | 110,010.00 USD |
| `15M` | `Bitget` | `31.67%` | `68.33%` | `0.46` | 183,160.00 USD |
| `15M` | `BingX` | `33.5%` | `66.5%` | `0.50` | 126,700.00 USD |
| `15M` | `MEXC` | `38.21%` | `61.79%` | `0.62` | 1,700,000.00 USD |
| `15M` | `Bitunix` | `18.07%` | `81.93%` | `0.22` | 1,080,000.00 USD |
| `15M` | `Hyperliquid` | `32.21%` | `67.79%` | `0.48` | 157,210.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `26.81%` | `73.19%` | `0.37` | 46,620.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 2,580.00 USD |
| `15M` | `HTX` | `28.31%` | `71.69%` | `0.39` | 1,200.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0.88%` | `99.12%` | `0.01` | 26,760.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `28.02%` | `71.98%` | `0.39` | 9,820.00 USD |
| `15M` | `Whale Positions` | `43.57%` | `56.43%` | `0.77` | 2,340,000.00 USD |
| `15M` | `Global Accounts` | `35.29%` | `64.71%` | `0.55` | 7,360,000.00 USD |
| `1H` | `NEAR` | `43.93%` | `56.07%` | `0.78` | 21,300,000.00 USD |
| `1H` | `Binance` | `50.46%` | `49.54%` | `1.02` | 7,240,000.00 USD |
| `1H` | `OKX` | `44.07%` | `55.93%` | `0.79` | 1,580,000.00 USD |
| `1H` | `Bybit` | `32.75%` | `67.25%` | `0.49` | 2,510,000.00 USD |
| `1H` | `KuCoin` | `35.85%` | `64.15%` | `0.56` | 101,150.00 USD |
| `1H` | `Gate` | `30.94%` | `69.06%` | `0.45` | 317,720.00 USD |
| `1H` | `Bitget` | `34.02%` | `65.98%` | `0.52` | 618,270.00 USD |
| `1H` | `BingX` | `31.51%` | `68.49%` | `0.46` | 486,050.00 USD |
| `1H` | `MEXC` | `44.92%` | `55.08%` | `0.82` | 5,920,000.00 USD |
| `1H` | `Bitunix` | `20.38%` | `79.62%` | `0.26` | 1,320,000.00 USD |
| `1H` | `Hyperliquid` | `49.1%` | `50.9%` | `0.96` | 443,050.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `66.25%` | `33.75%` | `1.96` | 519,200.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `100%` | `0%` | `1.00` | 40,720.00 USD |
| `1H` | `HTX` | `61.77%` | `38.23%` | `1.62` | 8,260.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `82.78%` | `17.22%` | `4.81` | 175,890.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `29.13%` | `70.87%` | `0.41` | 19,360.00 USD |
| `1H` | `Whale Positions` | `50.46%` | `49.54%` | `1.02` | 7,240,000.00 USD |
| `1H` | `Global Accounts` | `43.93%` | `56.07%` | `0.78` | 21,300,000.00 USD |
| `4H` | `NEAR` | `51.69%` | `48.31%` | `1.07` | 126,890,000.00 USD |
| `4H` | `Binance` | `50.9%` | `49.1%` | `1.04` | 54,770,000.00 USD |
| `4H` | `OKX` | `53.51%` | `46.49%` | `1.15` | 18,010,000.00 USD |
| `4H` | `Bybit` | `50.83%` | `49.17%` | `1.03` | 16,270,000.00 USD |
| `4H` | `KuCoin` | `48.64%` | `51.36%` | `0.95` | 1,760,000.00 USD |
| `4H` | `Gate` | `53.37%` | `46.63%` | `1.14` | 3,090,000.00 USD |
| `4H` | `Bitget` | `48.56%` | `51.44%` | `0.94` | 6,380,000.00 USD |
| `4H` | `BingX` | `48.36%` | `51.64%` | `0.94` | 4,300,000.00 USD |
| `4H` | `MEXC` | `53.21%` | `46.79%` | `1.14` | 10,070,000.00 USD |
| `4H` | `Bitunix` | `48.31%` | `51.69%` | `0.93` | 4,980,000.00 USD |
| `4H` | `Hyperliquid` | `32.35%` | `67.65%` | `0.48` | 3,060,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `72.31%` | `27.69%` | `2.61` | 1,400,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.25%` | `3.75%` | `25.67` | 2,030,000.00 USD |
| `4H` | `HTX` | `41.71%` | `58.29%` | `0.72` | 182,740.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `19.93%` | `80.07%` | `0.25` | 64,680.00 USD |
| `4H` | `Aster` | `62.2%` | `37.8%` | `1.65` | 393,700.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.33%` | `48.67%` | `1.05` | 147,390.00 USD |
| `4H` | `Whale Positions` | `50.9%` | `49.1%` | `1.04` | 54,770,000.00 USD |
| `4H` | `Global Accounts` | `51.69%` | `48.31%` | `1.07` | 126,890,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.15` | `4.15` | `4.15` | `4.17` | `4.14` | 5,034,918.87 USD | 2,878,643.09 USD | 2,156,275.78 USD | 722,367.31 USD | `+14.35%` | `2B / 1S` |
| `0:00 UTC` | `4.14` | `4.14` | `4.14` | `4.16` | `4.12` | 6,119,703.21 USD | 2,845,557.53 USD | 3,274,145.68 USD | -428,588.16 USD | `-7.00%` | `1B / 5S` |
| `5:00 UTC` | `4.18` | `4.19` | `4.18` | `4.22` | `4.15` | 12,847,139.28 USD | 7,912,037.28 USD | 4,935,102.00 USD | 2,976,935.28 USD | `+23.17%` | `8B / 2S` |
| `0:00 UTC` | `4.19` | `4.19` | `4.19` | `4.20` | `4.18` | 4,234,860.30 USD | 1,755,713.34 USD | 2,479,146.96 USD | -723,433.62 USD | `-17.08%` | `2B / 1S` |
| `5:00 UTC` | `4.23` | `4.23` | `4.23` | `4.24` | `4.20` | 7,447,660.88 USD | 3,310,439.61 USD | 4,137,221.27 USD | -826,781.65 USD | `-11.10%` | `6B / 7S` |
| `0:00 UTC` | `4.25` | `4.26` | `4.25` | `4.29` | `4.22` | 7,750,191.14 USD | 3,697,404.25 USD | 4,052,786.89 USD | -355,382.65 USD | `-4.59%` | `7B / 8S` |
| `5:00 UTC` | `4.26` | `4.26` | `4.26` | `4.28` | `4.25` | 4,694,349.73 USD | 2,226,198.09 USD | 2,468,151.64 USD | -241,953.55 USD | `-5.15%` | `1B / 1S` |
| `0:00 UTC` | `4.24` | `4.25` | `4.24` | `4.27` | `4.24` | 5,094,395.38 USD | 1,906,564.76 USD | 3,187,830.62 USD | -1,281,265.85 USD | `-25.15%` | `0B / 14S` |
| `5:00 UTC` | `4.19` | `4.21` | `4.19` | `4.26` | `4.18` | 7,454,532.40 USD | 2,255,345.80 USD | 5,199,186.60 USD | -2,943,840.80 USD | `-39.49%` | `2B / 31S` |
| `0:00 UTC` | `4.20` | `4.19` | `4.20` | `4.20` | `4.19` | 117,170.52 USD | 83,690.20 USD | 33,480.32 USD | 50,209.88 USD | `+42.85%` | `4B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:10` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.65` | 100,000.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4.64` | 0.00 USD | 0.00 USD |
| `10-28 20:33` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.63` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.57` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.54` | 0.00 USD | 0.00 USD |
| `10-28 19:51` | `Volume 2.0M NEAR` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.54` | 0.00 USD | 0.00 USD |
| `10-28 19:32` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.61` | 185,000.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 2.0M NEAR` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.65` | 419,000.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 2.0M NEAR` | `Trapped longs` | **`BEARISH`** | Failed breakout | `4.65` | 419,000.00 USD | 0.00 USD |
| `10-28 18:51` | `Volume 2.0M NEAR` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.59` | 469,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.61` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Range 0.02` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4.62` | 0.00 USD | 0.00 USD |
| `10-28 17:34` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.66` | 0.00 USD | 0.00 USD |
| `10-28 17:34` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.64` | 209,000.00 USD | 0.00 USD |
| `10-28 16:42` | `Volume 2.0M NEAR` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.65` | 0.00 USD | 0.00 USD |
| `10-28 14:29` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.72` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Volume 2.0M NEAR` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.76` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.75` | 145,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.02` | `Trapped longs` | **`BEARISH`** | Failed breakout | `4.75` | 145,000.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.71` | 84,000.00 USD | 0.00 USD |
| `10-28 06:42` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.65` | 0.00 USD | 0.00 USD |
| `10-28 06:42` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.63` | 166,000.00 USD | 0.00 USD |
| `10-28 06:40` | `Volume 2.0M NEAR` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.63` | 374,000.00 USD | 0.00 USD |
| `10-28 05:31` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.65` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -61,550.00 USD | -674,140.00 USD | **`DISTRIBUTION`** |
| `15m` | -712,370.00 USD | -5,790,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -189,720.00 USD | -7,330,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -50,860.00 USD | -9,500,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,320,000.00 USD | -8,670,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 7,400,000.00 USD | 7,510,000.00 USD | **`ACCUMULATION`** |
| `6h` | 5,590,000.00 USD | -5,910,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 459,560.00 USD | -16,550,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,690,000.00 USD | -23,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,820,000.00 USD | -62,560,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -75,430,000.00 USD | -141,990,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -243,310,000.00 USD | -687,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-61.55K` | 15m=`-712.37K` | 1h=`-50.86K` | 24h=`-11.82M`
* Futures Capital Netflows: 5m=`-674.14K` | 15m=`-5.79M` | 1h=`-9.50M` | 24h=`-62.56M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3.96` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3.85` (Risk Distance: `0.1059` pts)
  * +2.5R Take Profit: `4.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.26` (Risk Distance: `0.1059` pts)
  * +2.5R Take Profit: `3.89`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.22`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
