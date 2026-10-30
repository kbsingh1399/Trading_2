# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:25:13 IST` (`2026-10-30 03:55:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.15` | **Live Ask Quote**: `4.18` | **Mid Price**: `4.16`
- **Spread Points**: `30.00` | **Spread BPS**: `72.08 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.00` | VWAP Z-Score: `+2.89` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0573` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `55.49` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.15` | Lower -3.00σ Band: `3.86`
  * Upper +2.51σ Band: `4.12` | Lower -2.51σ Band: `3.88`
  * Upper +2.01σ Band: `4.10` | Lower -2.01σ Band: `3.91`
  * Upper +2.00σ Band: `4.10` | Lower -2.00σ Band: `3.91`
  * Upper +1.28σ Band: `4.06` | Lower -1.28σ Band: `3.94`
  * Upper +1.00σ Band: `4.05` | Lower -1.00σ Band: `3.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.07` | EMA-20=`4.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.18` (Slope: `+0.0000`) | EMA-100=`4.30`
  * Institutional Anchors: EMA-144=`4.36` | EMA-200=`4.40` (Slope: `-1.0323`) | EMA-233=`4.43`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.13` (Distance: `+0.79%`)
  * Point of Control (POC) = `4.09` (Distance: `+1.58%`)
  * Value Area Low (VAL) = `3.95` (Distance: `+5.19%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.68` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.18` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.19` | Low=`4.14`
  * Initial Balance (First Hour): IB High=`4.17` | IB Low=`4.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.15` - `4.18`
  * Optimal Trade Entry (OTE 0.705): `4.17`
  * Structural Invalidation Anchor (0.786): `4.20`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.12` | `4.14` | `4.12` | `4.13` | `760,994` | 3,143,238.73 USD | 282,578.94 USD | `+8.99%` | -30,347,782.66 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4.13` | `4.16` | `4.13` | `4.16` | `956,959` | 3,968,681.06 USD | 806,131.37 USD | `+20.31%` | -29,541,651.29 USD | `+1.08` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.16` | `4.17` | `4.14` | `4.16` | `509,244` | 2,114,042.95 USD | 180,758.89 USD | `+8.55%` | -29,360,892.40 USD | `-0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4.08` | `4.11` | `4.07` | `4.11` | `1,059,310` | 4,324,346.41 USD | 961,608.74 USD | `+22.24%` | -31,350,723.04 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.11` | `4.16` | `4.10` | `4.16` | `2,417,383` | 9,990,039.56 USD | 1,647,200.46 USD | `+16.49%` | -29,703,522.59 USD | `+1.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.16` | `4.17` | `4.14` | `4.16` | `516,322` | 2,143,497.07 USD | 193,528.69 USD | `+9.03%` | -29,509,993.89 USD | `+0.17` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `3.99` | `4.04` | `3.95` | `4.00` | `8,344,084` | 33,377,841.60 USD | -1,208,714.23 USD | `-3.62%` | -36,547,776.95 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4.00` | `4.11` | `3.97` | `4.06` | `7,535,910` | 30,558,990.03 USD | 3,476,842.65 USD | `+11.38%` | -33,070,934.30 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.06` | `4.17` | `4.06` | `4.16` | `5,316,001` | 21,850,471.68 USD | 3,560,940.41 USD | `+16.30%` | -29,509,993.89 USD | `+1.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,135,129` | 185,302,753.20 USD | -941,303.40 USD | `-0.51%` | -29,510,093.73 USD | `+0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -16,765,834.34 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -12,356,807.24 USD | `+1.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,135,129` | 185,302,753.20 USD | -941,303.40 USD | `-0.51%` | -29,510,093.73 USD | `+0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:20:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `65` | `0x7737...bf66` | `LONG` | 23,403,613.38 USD | `5,640,376.30` | `2.35` | `4.15` | `0.8388` | 10,131,710.55 USD | `+43.29%` | `10X Cross` |
| `105` | `0xefe4...194b` | `SHORT` | 18,717,308.98 USD | `4,507,262.50` | `4.21` | `4.15` | `6.66` | 257,787.73 USD | `+1.38%` | `5X Cross` |
| `132` | `0xb581...6f4f` | `LONG` | 14,968,440.00 USD | `3,600,000.00` | `5.19` | `4.15` | `0.000000` | -3,724,595.22 USD | `-24.88%` | `4X Cross` |
| `213` | `0xdd53...2b13` | `SHORT` | 9,974,279.43 USD | `2,400,202.00` | `2.31` | `4.15` | `29.27` | -4,428,430.87 USD | `-44.40%` | `3X Cross` |
| `270` | `0x77ee...2902` | `LONG` | 8,567,116.03 USD | `2,063,023.10` | `1.93` | `4.15` | `0.000000` | 4,575,920.09 USD | `+53.41%` | `10X Cross` |
| `364` | `0x9df2...c665` | `SHORT` | 6,290,955.33 USD | `1,514,579.00` | `2.36` | `4.15` | `24.00` | -2,710,965.67 USD | `-43.09%` | `10X Cross` |
| `379` | `0xb83d...6e36` | `SHORT` | 6,004,092.97 USD | `1,445,759.10` | `5.19` | `4.15` | `93.10` | 1,505,355.98 USD | `+25.07%` | `3X Cross` |
| `380` | `0x7fda...17d1` | `SHORT` | 5,996,579.41 USD | `1,443,915.10` | `4.28` | `4.15` | `28.90` | 185,499.11 USD | `+3.09%` | `10X Cross` |
| `397` | `0xb46b...538e` | `SHORT` | 5,554,019.20 USD | `1,336,000.00` | `4.33` | `4.15` | `7.46` | 230,844.86 USD | `+4.16%` | `10X Cross` |
| `476` | `0x60b0...991e` | `LONG` | 4,658,470.35 USD | `1,121,307.10` | `5.00` | `4.15` | `0.000000` | -942,954.08 USD | `-20.24%` | `10X Cross` |
| `499` | `0xcac1...26b3` | `SHORT` | 4,460,332.16 USD | `1,073,743.90` | `2.48` | `4.15` | `12.15` | -1,800,388.70 USD | `-40.36%` | `10X Cross` |
| `515` | `0x781e...96b7` | `SHORT` | 4,316,750.18 USD | `1,039,604.60` | `2.45` | `4.15` | `7.49` | -1,772,412.99 USD | `-41.06%` | `10X Cross` |
| `596` | `0x45d2...4029` | `SHORT` | 3,776,101.62 USD | `909,400.00` | `3.26` | `4.15` | `48.72` | -809,951.72 USD | `-21.45%` | `10X Cross` |
| `601` | `0x4cae...7c34` | `LONG` | 3,736,897.36 USD | `900,587.40` | `3.97` | `4.15` | `2.83` | 158,704.57 USD | `+4.25%` | `10X Cross` |
| `838` | `0x005a...61fe` | `LONG` | 2,711,174.11 USD | `652,414.60` | `2.08` | `4.15` | `2.40` | 1,353,642.88 USD | `+49.93%` | `7X Cross` |
| `844` | `0xba5d...a352` | `SHORT` | 2,689,008.21 USD | `647,532.50` | `2.83` | `4.15` | `13.50` | -856,293.27 USD | `-31.84%` | `10X Cross` |
| `858` | `0xb695...a92d` | `SHORT` | 2,654,665.33 USD | `639,231.70` | `4.57` | `4.15` | `45.16` | 268,693.60 USD | `+10.12%` | `10X Cross` |
| `865` | `0xd1dd...9e85` | `SHORT` | 2,643,276.98 USD | `637,621.00` | `4.96` | `4.15` | `18.42` | 520,195.75 USD | `+19.68%` | `10X Cross` |
| `867` | `0x123d...3bff` | `SHORT` | 2,638,784.22 USD | `635,392.30` | `2.09` | `4.15` | `9.09` | -1,312,835.75 USD | `-49.75%` | `10X Cross` |
| `879` | `0xcf53...ee11` | `SHORT` | 2,582,865.67 USD | `621,598.40` | `5.07` | `4.15` | `25.38` | 569,304.58 USD | `+22.04%` | `10X Cross` |
| `1006` | `0xbfc7...80b4` | `SHORT` | 2,204,552.70 USD | `531,000.00` | `2.01` | `4.15` | `7.23` | -1,139,353.31 USD | `-51.68%` | `10X Cross` |
| `1261` | `0x0eec...d4c5` | `LONG` | 1,754,116.73 USD | `422,373.40` | `4.01` | `4.15` | `1.22` | 61,815.36 USD | `+3.52%` | `10X Cross` |
| `1302` | `0xe097...d0fe` | `LONG` | 1,662,080.00 USD | `400,000.00` | `5.29` | `4.15` | `0.000000` | -454,707.30 USD | `-27.36%` | `10X Cross` |
| `1445` | `0x6e8f...4364` | `LONG` | 1,500,323.93 USD | `361,210.50` | `3.28` | `4.15` | `3.50` | 316,263.71 USD | `+21.08%` | `10X Cross` |
| `1457` | `0xef96...9383` | `SHORT` | 1,485,167.25 USD | `357,165.90` | `4.50` | `4.15` | `14.17` | 123,074.55 USD | `+8.29%` | `10X Cross` |
| `1482` | `0xdf95...7d72` | `SHORT` | 1,454,948.32 USD | `350,446.40` | `4.23` | `4.15` | `110.29` | 28,250.87 USD | `+1.94%` | `10X Cross` |
| `1484` | `0xcf67...eb24` | `LONG` | 1,453,515.00 USD | `350,000.00` | `1.98` | `4.15` | `1.49` | 761,897.12 USD | `+52.42%` | `10X Cross` |
| `1600` | `0xfc27...9d9d` | `SHORT` | 1,328,950.45 USD | `319,997.70` | `5.01` | `4.15` | `60.42` | 274,592.17 USD | `+20.66%` | `10X Cross` |
| `1606` | `0x089f...a4f8` | `LONG` | 1,325,816.34 USD | `319,043.30` | `4.06` | `4.15` | `0.000000` | 30,959.63 USD | `+2.34%` | `1X Cross` |
| `1632` | `0x9aa5...58af` | `SHORT` | 1,296,995.60 USD | `312,303.30` | `4.78` | `4.15` | `32.87` | 195,392.57 USD | `+15.07%` | `10X Cross` |
| `1665` | `0x17c3...a868` | `LONG` | 1,266,441.09 USD | `304,638.00` | `4.36` | `4.15` | `0.000000` | -62,962.28 USD | `-4.97%` | `3X Cross` |
| `1688` | `0x9836...457e` | `LONG` | 1,248,692.50 USD | `300,000.60` | `4.57` | `4.15` | `1.84` | -123,380.67 USD | `-9.88%` | `10X Cross` |
| `1737` | `0xe065...0f85` | `SHORT` | 1,196,151.07 USD | `288,027.90` | `2.81` | `4.15` | `5.54` | -385,597.94 USD | `-32.24%` | `10X Cross` |
| `1939` | `0xff43...d924` | `LONG` | 1,035,992.76 USD | `249,474.50` | `4.64` | `4.15` | `3.28` | -122,050.92 USD | `-11.78%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.74` | 10,286.86 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.29K USD at 4.7418 USD [API] | `2026-10-28 22:47:46` |
| `ANNOUNCEMENT` | `INFO` | `5.00` | 5,000.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 5.00K USD at 5.0000 USD [API] | `2026-10-12 23:39:10` |
| `ANNOUNCEMENT` | `INFO` | `4.72` | 6,698.21 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.70K USD at 4.7237 USD [API] | `2026-10-29 00:27:21` |
| `ANNOUNCEMENT` | `INFO` | `4.72` | 5,843.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.84K USD at 4.7242 USD [API] | `2026-10-29 00:29:14` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 6,417.66 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.42K USD at 4.6899 USD [API] | `2026-10-29 00:52:41` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 14,286.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 14.29K USD at 4.6907 USD [API] | `2026-10-29 00:52:26` |
| `ANNOUNCEMENT` | `INFO` | `4.67` | 5,170.82 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.17K USD at 4.6744 USD [API] | `2026-10-29 00:57:59` |
| `ANNOUNCEMENT` | `INFO` | `4.66` | 8,960.91 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.96K USD at 4.6601 USD [API] | `2026-10-29 01:18:47` |
| `ANNOUNCEMENT` | `INFO` | `4.62` | 8,623.49 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.62K USD at 4.6189 USD [API] | `2026-10-29 01:33:58` |
| `ANNOUNCEMENT` | `INFO` | `4.58` | 7,940.40 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.94K USD at 4.5795 USD [API] | `2026-10-29 01:39:37` |
| `ANNOUNCEMENT` | `INFO` | `4.51` | 2,645.11 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.65K USD at 4.5123 USD [API] | `2026-10-29 01:49:15` |
| `ANNOUNCEMENT` | `INFO` | `4.52` | 3,997.91 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 4.00K USD at 4.5169 USD [API] | `2026-10-29 01:49:08` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+6.28%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.19%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+6.20%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.21%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+6.20%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.21%`)
  * 7D Horizon: Short MP=`5.01` (Vol: 953,300.00 USD, Dist: `+20.52%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.18%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8350` | 3,400.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 806.81 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 2,060.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 1,160.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 751.19 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 713.23 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 12,280.00 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 523.34 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 1,240.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 3,340.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 9,870.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 707.53 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 21,400.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 15,410.00 USD | 21,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 34,960.00 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 4,330.00 USD | 21,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216.89 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 2,730.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 178.20 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 21,740.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 26,620.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 647.54 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 128.46 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 545,080.00 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 1,200.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 416.83 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 13,040.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 5,090.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 9,860.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 234.51 USD | 20,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 3,360.00 USD | 20,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 2,100.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,000.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 1,640.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,720.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 1,360.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 931.86 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 82,080.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 3,860.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.44` | 762.85 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 30,680.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 145,240.00 USD | 20,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 4,360.00 USD | 20,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 438.63 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 1,250.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 2,110.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 20,570.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 919.17 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 1,980.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 4,340.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 80,440.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 207.19 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 32,940.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 113.70 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 1,830.00 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 2,790.00 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 615,660.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 254.25 USD | 19,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 2,190.00 USD | 19,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 188.65 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 6,150.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 7,770.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 1,320.00 USD | 19,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 91,070.00 USD | 19,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,470.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 2,930.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 6,870.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 909,920.00 USD | 19,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 28,850.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 4,160.00 USD | 18,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 984.26 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 600,480.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,250.00 USD | 17,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 4,610.00 USD | 17,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 5,860.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 1,870.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 16,430.00 USD | 17,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 3,550.00 USD | 17,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 34,950.00 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 1,490.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 1,000.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 1,640.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 260.62 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 411.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 6,070.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 115,690.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 19,630.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 1,910.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 6,980.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 355,570.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 35,160.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 1,660.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 1,150.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 1,020.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 190,720.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 19,250.00 USD | 16,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 92,620.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,120.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 44,560.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 1,200.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 1,620.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,590.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 311,490.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 149,240.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 379,560.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 463.86 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 2,860.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 43,180.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,970.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,690.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 13,800.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 26,070.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 30,610.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 3,450.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 533,900.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 5,860.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 115.20 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 420,800.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 1,860,000.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 2,320.00 USD | 13,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,830.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 35,430.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 18,070.00 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 21,470.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 76,980.00 USD | 12,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 1,110.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 6,000.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 1,290.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 29,000.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 254,240.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 35,030.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 2,880.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 10,170.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,260.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 905.27 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 116,650.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 3,580.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 13,670.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,180.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 37,330.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,650.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 16,760.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 12,860.00 USD | 12,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 7,140.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,970.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 3,260.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 120,220.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 25,340.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 27,780.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 13,540.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 41,170.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 25,260.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 349,840.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 398.77 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 51,460.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 26,200.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 94,090.00 USD | 11,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 4,110.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 8,640.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 1,710.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,030.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 5,640.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 8,690.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 405,640.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 93,770.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 16,720.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 94,420.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 85,280.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 47,510.00 USD | 10,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 49,960.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 18,120.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,470.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 6,880.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 43,150.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 206,990.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,000.00 USD | 10,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 10,410.00 USD | 10,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 21,690.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 20,590.00 USD | 10,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 17,500.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 374,580.00 USD | 10,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 23,800.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,550.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 91,140.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 31,900.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,590.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 24,750.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 32,910.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 22,120.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 7,780.00 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 220,990.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 168,940.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 91,330.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 26,600.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 245,670.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 9,520.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 16,350.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,780.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 43,870.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 74,100.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 5,640.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 52,930.00 USD | 8,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 868,070.00 USD | 8,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 3,180.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 133,280.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 125,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 17,590.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 9,990.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 74,540.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 31,800.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 2,440.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 141,980.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 69,770.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 54,830.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 10,810.00 USD | 7,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 98,820.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 552,690.00 USD | 7,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 38,260.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 34,830.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 13,870.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 12,320.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,030.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 181,230.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 24,690.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 62,550.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 32,800.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 8,020.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 205,380.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 1,440,000.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 168,380.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 383,600.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 8,960.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 43,530.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 34,670.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 12,300,000.00 USD | 12,300,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 24,080.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 11,920,000.00 USD | 11,920,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 60,200.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 11,810,000.00 USD | 11,810,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 21,040.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 11,690,000.00 USD | 11,690,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 125,390.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.63` | 5,930,000.00 USD | 5,930,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.63` | 11,480,000.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 10,560.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.64` | 5,900,000.00 USD | 5,900,000.00 USD | 152.80 USD | 5,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.64` | 11,420,000.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 50,500.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.65` | 5,890,000.00 USD | 5,890,000.00 USD | 386.30 USD | 0.00 USD | 13.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.65` | 11,280,000.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 14,180.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 5,890,000.00 USD | 5,890,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 11,190,000.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 50,850.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 5,890,000.00 USD | 5,890,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 11,020,000.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 87,540.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.68` | 5,860,000.00 USD | 5,860,000.00 USD | 216.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 146,340.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 5,860,000.00 USD | 5,860,000.00 USD | 23,960.00 USD | 0.00 USD | 281.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,900,000.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 94,330.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 5,840,000.00 USD | 5,840,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 10,820,000.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 212,700.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 5,740,000.00 USD | 5,740,000.00 USD | 430.40 USD | 0.00 USD | 522.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 10,680,000.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 15,680.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 5,740,000.00 USD | 5,740,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 10,550,000.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 271,510.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 5,740,000.00 USD | 5,740,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 10,550,000.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 394,290.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 5,710,000.00 USD | 5,710,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 10,440,000.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 39,750.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 10,150,000.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 153,580.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 10,080,000.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 69,750.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 5,510,000.00 USD | 5,510,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 10,020,000.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 67,960.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 5,500,000.00 USD | 5,500,000.00 USD | 106.91 USD | 4,490.00 USD | 29,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,970,000.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 46,300.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 5,470,000.00 USD | 5,470,000.00 USD | 472.79 USD | 0.00 USD | 176.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,900,000.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 145,620.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 5,470,000.00 USD | 5,470,000.00 USD | 1,270.00 USD | 0.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,810,000.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 472,430.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 5,470,000.00 USD | 5,470,000.00 USD | 54,290.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 202,270.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 5,400,000.00 USD | 5,400,000.00 USD | 487.48 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 9,770,000.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 159,740.00 USD | 960,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 5,390,000.00 USD | 5,390,000.00 USD | 1,150.00 USD | 18,900.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 207,570.00 USD | 800,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 784.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 9,720,000.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 133,920.00 USD | 593,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 5,350,000.00 USD | 5,350,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 122,550.00 USD | 459,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 5,340,000.00 USD | 5,340,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,720,000.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 27,290.00 USD | 336,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 5,270,000.00 USD | 5,270,000.00 USD | 1,690.00 USD | 11,800.00 USD | 845.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,640,000.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 136,810.00 USD | 309,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 5,260,000.00 USD | 5,260,000.00 USD | 106,680.00 USD | 6,860.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 9,550,000.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 88,930.00 USD | 172,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 5,100,000.00 USD | 5,100,000.00 USD | 113,490.00 USD | 37,150.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,340,000.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 75,910.00 USD | 83,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 4,930,000.00 USD | 4,930,000.00 USD | 31,410.00 USD | 10,910.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 9,280,000.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 4,350.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 4,870,000.00 USD | 4,870,000.00 USD | 32,140.00 USD | 35,760.00 USD | 39,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 9,030,000.00 USD | 9,030,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.92` | 4,760,000.00 USD | 4,760,000.00 USD | 148,140.00 USD | 26,030.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,960,000.00 USD | 8,960,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.93` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 29,900.00 USD | 38,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,730,000.00 USD | 8,730,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.94` | 4,480,000.00 USD | 4,480,000.00 USD | 96,340.00 USD | 14,940.00 USD | 20,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,640,000.00 USD | 8,640,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.95` | 4,350,000.00 USD | 4,350,000.00 USD | 95,940.00 USD | 15,880.00 USD | 95,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 8,430,000.00 USD | 8,430,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.96` | 4,150,000.00 USD | 4,150,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 8,400,000.00 USD | 8,400,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.97` | 4,000,000.00 USD | 4,000,000.00 USD | 190,720.00 USD | 66,010.00 USD | 102,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,910,000.00 USD | 7,910,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.98` | 3,640,000.00 USD | 3,640,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 7,300,000.00 USD | 7,300,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 3,390,000.00 USD | 3,390,000.00 USD | 413,960.00 USD | 106,190.00 USD | 138,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 6,630,000.00 USD | 6,630,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.00` | 2,730,000.00 USD | 2,730,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 6,380,000.00 USD | 6,380,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.01` | 2,510,000.00 USD | 2,510,000.00 USD | 112,570.00 USD | 72,850.00 USD | 129,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 5,770,000.00 USD | 5,770,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.02` | 2,190,000.00 USD | 2,190,000.00 USD | 243,600.00 USD | 50,310.00 USD | 107,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 4,850,000.00 USD | 4,850,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.03` | 1,790,000.00 USD | 1,790,000.00 USD | 189,730.00 USD | 76,190.00 USD | 266,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 4,230,000.00 USD | 4,230,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.04` | 1,260,000.00 USD | 1,260,000.00 USD | 105,670.00 USD | 48,960.00 USD | 207,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 3,780,000.00 USD | 3,780,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.05` | 898,580.00 USD | 898,580.00 USD | 2,370.00 USD | 46,690.00 USD | 95,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 2,900,000.00 USD | 2,900,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.06` | 753,820.00 USD | 753,820.00 USD | 0.00 USD | 27,150.00 USD | 125,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 2,410,000.00 USD | 2,410,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.07` | 600,750.00 USD | 600,750.00 USD | 0.00 USD | 72,110.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 1,840,000.00 USD | 1,840,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.08` | 506,300.00 USD | 506,300.00 USD | 506,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 575,150.00 USD | 575,150.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 218,520.00 USD | 218,520.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 143,210.00 USD | 143,210.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 286,420.00 USD | 286,420.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.12` | 309,660.00 USD | 309,660.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.12` | 1,450.00 USD | 1,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.13` | 471,110.00 USD | 471,110.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.13` | 6,730.00 USD | 8,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.14` | 531,130.00 USD | 531,130.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.14` | 1,430.00 USD | 9,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.15` | 595,400.00 USD | 595,400.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.16` | 638.21 USD | 10,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.17` | 664,710.00 USD | 664,710.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 10,040.00 USD | 20,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.18` | 874,490.00 USD | 874,490.00 USD | 192,730.00 USD | 17,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.18` | 54,820.00 USD | 75,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.19` | 1,250,000.00 USD | 1,250,000.00 USD | 174,270.00 USD | 20,540.00 USD | 185,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.20` | 666.59 USD | 75,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 4,460.00 USD | 80,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.21` | 1,330,000.00 USD | 1,330,000.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 837.10 USD | 81,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.22` | 1,530,000.00 USD | 1,530,000.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.22` | 1,060.00 USD | 82,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.23` | 2,200,000.00 USD | 2,200,000.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.24` | 5,820.00 USD | 87,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,880,000.00 USD | 2,880,000.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.25` | 649.06 USD | 88,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.25` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 3,480,000.00 USD | 3,480,000.00 USD | 92,160.00 USD | 173,320.00 USD | 248.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.26` | 208.99 USD | 88,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.27` | 4,340,000.00 USD | 4,340,000.00 USD | 677,660.00 USD | 34,890.00 USD | 152,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.28` | 4,860.00 USD | 93,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,970,000.00 USD | 4,970,000.00 USD | 305,690.00 USD | 30,410.00 USD | 288,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 163.69 USD | 93,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.29` | 5,320,000.00 USD | 5,320,000.00 USD | 153,130.00 USD | 32,690.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 207,690.00 USD | 301,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.30` | 5,560,000.00 USD | 5,560,000.00 USD | 32,410.00 USD | 45,120.00 USD | 163,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.30` | 5,070.00 USD | 306,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,970,000.00 USD | 5,970,000.00 USD | 304,920.00 USD | 13,580.00 USD | 95,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 31,130.00 USD | 337,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 6,130,000.00 USD | 6,130,000.00 USD | 86,850.00 USD | 73,400.00 USD | 18.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 373.68 USD | 338,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.33` | 6,570,000.00 USD | 6,570,000.00 USD | 255,620.00 USD | 93,880.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 7,090,000.00 USD | 7,090,000.00 USD | 270,720.00 USD | 140,540.00 USD | 114,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 4,130.00 USD | 342,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 7,180,000.00 USD | 7,180,000.00 USD | 855.62 USD | 0.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,050.00 USD | 345,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 7,310,000.00 USD | 7,310,000.00 USD | 84,880.00 USD | 12,310.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 7,540,000.00 USD | 7,540,000.00 USD | 52,520.00 USD | 46,860.00 USD | 130,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 1,110.00 USD | 346,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 8,380,000.00 USD | 8,380,000.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 8,710,000.00 USD | 8,710,000.00 USD | 399.48 USD | 17,360.00 USD | 310,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 192,710.00 USD | 539,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 9,110,000.00 USD | 9,110,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,410.00 USD | 540,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 196,820.00 USD | 112,990.00 USD | 65,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 104.87 USD | 540,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 9,690,000.00 USD | 9,690,000.00 USD | 5,100.00 USD | 49,400.00 USD | 98,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 10,470,000.00 USD | 10,470,000.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 10,530,000.00 USD | 10,530,000.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 10,540,000.00 USD | 10,540,000.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 541,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 10,570,000.00 USD | 10,570,000.00 USD | 210.23 USD | 16,700.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 629.18 USD | 541,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 10,790,000.00 USD | 10,790,000.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 11,350,000.00 USD | 11,350,000.00 USD | 252,600.00 USD | 155,000.00 USD | 150,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 90,180.00 USD | 631,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 11,890,000.00 USD | 11,890,000.00 USD | 361,770.00 USD | 65,710.00 USD | 120,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 283.81 USD | 632,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 12,700,000.00 USD | 12,700,000.00 USD | 186,860.00 USD | 307,580.00 USD | 312,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 967.56 USD | 633,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 13,320,000.00 USD | 13,320,000.00 USD | 287,830.00 USD | 92,260.00 USD | 242,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,820.00 USD | 651,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 14,090,000.00 USD | 14,090,000.00 USD | 487,540.00 USD | 0.00 USD | 279,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 14,810,000.00 USD | 14,810,000.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 394.51 USD | 652,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 22,540.00 USD | 195,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 15,430,000.00 USD | 15,430,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 243.77 USD | 652,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 15,740,000.00 USD | 15,740,000.00 USD | 177,440.00 USD | 70,180.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 182,510.00 USD | 835,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.58` | 17,200,000.00 USD | 17,200,000.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 18,180,000.00 USD | 18,180,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 827.10 USD | 835,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 18,380,000.00 USD | 18,380,000.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 1,050.00 USD | 836,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 18,520,000.00 USD | 18,520,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 3,920.00 USD | 840,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.62` | 18,670,000.00 USD | 18,670,000.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 18,670,000.00 USD | 18,670,000.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 990.04 USD | 841,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 19,080,000.00 USD | 19,080,000.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 169.54 USD | 842,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 20,150,000.00 USD | 20,150,000.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 124.75 USD | 842,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 21,130,000.00 USD | 21,130,000.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 101.70 USD | 842,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 21,690,000.00 USD | 21,690,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 22,300,000.00 USD | 22,300,000.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 48,020.00 USD | 890,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 22,800,000.00 USD | 22,800,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 890,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 23,140,000.00 USD | 23,140,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 898,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 24,100,000.00 USD | 24,100,000.00 USD | 359,510.00 USD | 284,360.00 USD | 316,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 460.18 USD | 898,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 4,310.00 USD | 902,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 227.77 USD | 903,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 8,780.00 USD | 911,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 911,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 913,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 45,670.00 USD | 958,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 3,020.00 USD | 961,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,950.00 USD | 963,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 975,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 137.68 USD | 975,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 976,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 996,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 998,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 999,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 999,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 60,660,000.00 USD | 60,660,000.00 USD | 358,750.00 USD | 137,080.00 USD | 542,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 61,180,000.00 USD | 61,180,000.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 1,090.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 61,720,000.00 USD | 61,720,000.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 62,110,000.00 USD | 62,110,000.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 62,700,000.00 USD | 62,700,000.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 37,150.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.12` | 63,270,000.00 USD | 63,270,000.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 63,840,000.00 USD | 63,840,000.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.14` | 64,280,000.00 USD | 64,280,000.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.15` | 64,830,000.00 USD | 64,830,000.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 65,350,000.00 USD | 65,350,000.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 65,960,000.00 USD | 65,960,000.00 USD | 280,710.00 USD | 85,040.00 USD | 244,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.18` | 66,210,000.00 USD | 66,210,000.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.18` | 82,840.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.19` | 66,430,000.00 USD | 66,430,000.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 22,080.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 66,680,000.00 USD | 66,680,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.21` | 66,920,000.00 USD | 66,920,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.22` | 66,980,000.00 USD | 66,980,000.00 USD | 48,760.00 USD | 13,410.00 USD | 398.26 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 74,720.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 67,040,000.00 USD | 67,040,000.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 1,970.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 16,140.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 134.77 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 718.59 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 1,070,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 616.28 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 142.44 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 5,410.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 61,270.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 702.41 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 43,980.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 627.98 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 66,470.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 71,830.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,580.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 56,050.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 1,620,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 2,670.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.82` | 127.93 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 310.95 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.87` | 200.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 7,150.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.91` | 151.76 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 343,290.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 103,650.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 388,640.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 345,420.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.04` | 196,080.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 23,590.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 5,270.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 288,250.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 2,060.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 1,460.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 5,740.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 173.47 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 77,220.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 55,720.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.49` | 911.79 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 269,120.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.61` | 700.79 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.64` | 29,950,000.00 USD | 36,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 48,430.00 USD | 36,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 36,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 36,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 37,150.00 USD | 36,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 11,490.00 USD | 36,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 38,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.76` | 90,430.00 USD | 38,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 15,200.00 USD | 38,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.88` | 295.62 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 38,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 1,310,000.00 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.00` | 190.96 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 665.27 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.20` | 171.96 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 39,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 39,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.32` | 580.08 USD | 39,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 39,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.34` | 11,120.00 USD | 39,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 1,850.00 USD | 39,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 106,000.00 USD | 39,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 39,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 783.38 USD | 39,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 10,050,000.00 USD | 49,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.54` | 2,340.00 USD | 49,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.57` | 7,860,000.00 USD | 57,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 2,630.00 USD | 57,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 6,030.00 USD | 57,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 27,330.00 USD | 57,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 57,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 15,390.00 USD | 57,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 4,100,000.00 USD | 61,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 505.87 USD | 61,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 105,820.00 USD | 61,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 33,540.00 USD | 61,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 997,510.00 USD | 62,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 505.58 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 1,800.00 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 62,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,410.00 USD | 63,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 63,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 63,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8350` | 21,460,000.00 USD | 0.00 USD | 3,400.00 USD | `-79.43%` | `4,071.50` |
| `Live` | `Long` | `0.8450` | 21,460,000.00 USD | 0.00 USD | 806.81 USD | `-79.18%` | `954.80` |
| `Live` | `Long` | `0.8550` | 21,460,000.00 USD | 0.00 USD | 2,060.00 USD | `-78.93%` | `2,406.30` |
| `Live` | `Long` | `0.8650` | 21,460,000.00 USD | 0.00 USD | 433.80 USD | `-78.69%` | `501.50` |
| `Live` | `Long` | `0.8750` | 21,460,000.00 USD | 0.00 USD | 1,160.00 USD | `-78.44%` | `1,321.80` |
| `Live` | `Long` | `0.8850` | 21,460,000.00 USD | 0.00 USD | 751.19 USD | `-78.19%` | `848.80` |
| `Live` | `Long` | `0.8950` | 21,460,000.00 USD | 0.00 USD | 38,570.00 USD | `-77.95%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 21,420,000.00 USD | 0.00 USD | 713.23 USD | `-77.70%` | `788.10` |
| `Live` | `Long` | `0.9150` | 21,420,000.00 USD | 0.00 USD | 12,280.00 USD | `-77.46%` | `13,425.00` |
| `Live` | `Long` | `0.9450` | 21,400,000.00 USD | 0.00 USD | 523.34 USD | `-76.72%` | `553.80` |
| `Live` | `Long` | `0.9550` | 21,400,000.00 USD | 0.00 USD | 1,240.00 USD | `-76.47%` | `1,295.60` |
| `Live` | `Long` | `0.9650` | 21,400,000.00 USD | 0.00 USD | 3,340.00 USD | `-76.22%` | `3,458.00` |
| `Live` | `Long` | `0.9750` | 21,400,000.00 USD | 0.00 USD | 9,870.00 USD | `-75.98%` | `10,126.70` |
| `Live` | `Long` | `0.9850` | 21,390,000.00 USD | 0.00 USD | 707.53 USD | `-75.73%` | `718.30` |
| `Live` | `Long` | `0.9950` | 21,390,000.00 USD | 0.00 USD | 154,200.00 USD | `-75.48%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 21,230,000.00 USD | 0.00 USD | 21,400.00 USD | `-75.24%` | `21,288.70` |
| `Live` | `Long` | `1.02` | 21,210,000.00 USD | 0.00 USD | 15,410.00 USD | `-74.75%` | `15,033.00` |
| `Live` | `Long` | `1.03` | 21,200,000.00 USD | 0.00 USD | 5,070.00 USD | `-74.50%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 21,190,000.00 USD | 0.00 USD | 34,960.00 USD | `-74.25%` | `33,454.20` |
| `Live` | `Long` | `1.05` | 21,160,000.00 USD | 0.00 USD | 4,330.00 USD | `-74.01%` | `4,108.90` |
| `Live` | `Long` | `1.06` | 21,150,000.00 USD | 0.00 USD | 892.90 USD | `-73.76%` | `838.40` |
| `Live` | `Long` | `1.07` | 21,150,000.00 USD | 0.00 USD | 7,510.00 USD | `-73.51%` | `6,989.70` |
| `Live` | `Long` | `1.08` | 21,140,000.00 USD | 0.00 USD | 216.89 USD | `-73.27%` | `199.90` |
| `Live` | `Long` | `1.09` | 21,140,000.00 USD | 0.00 USD | 2,730.00 USD | `-73.02%` | `2,491.20` |
| `Live` | `Long` | `1.11` | 21,140,000.00 USD | 0.00 USD | 557.50 USD | `-72.53%` | `500.00` |
| `Live` | `Long` | `1.12` | 21,140,000.00 USD | 0.00 USD | 178.20 USD | `-72.28%` | `158.40` |
| `Live` | `Long` | `1.14` | 21,140,000.00 USD | 0.00 USD | 21,740.00 USD | `-72.04%` | `19,152.50` |
| `Live` | `Long` | `1.15` | 21,120,000.00 USD | 0.00 USD | 26,620.00 USD | `-71.79%` | `23,252.70` |
| `Live` | `Long` | `1.18` | 21,090,000.00 USD | 0.00 USD | 647.54 USD | `-71.05%` | `551.10` |
| `Live` | `Long` | `1.20` | 21,090,000.00 USD | 0.00 USD | 128.46 USD | `-70.56%` | `107.50` |
| `Live` | `Long` | `1.22` | 21,090,000.00 USD | 0.00 USD | 545,080.00 USD | `-70.06%` | `448,629.50` |
| `Live` | `Long` | `1.24` | 20,550,000.00 USD | 0.00 USD | 1,200.00 USD | `-69.57%` | `971.20` |
| `Live` | `Long` | `1.25` | 20,550,000.00 USD | 0.00 USD | 416.83 USD | `-69.33%` | `334.80` |
| `Live` | `Long` | `1.25` | 20,550,000.00 USD | 0.00 USD | 13,040.00 USD | `-69.08%` | `10,389.00` |
| `Live` | `Long` | `1.26` | 20,530,000.00 USD | 0.00 USD | 2,060.00 USD | `-68.83%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 20,530,000.00 USD | 0.00 USD | 5,090.00 USD | `-68.59%` | `3,991.50` |
| `Live` | `Long` | `1.28` | 20,530,000.00 USD | 0.00 USD | 9,860.00 USD | `-68.34%` | `7,669.60` |
| `Live` | `Long` | `1.30` | 20,520,000.00 USD | 0.00 USD | 234.51 USD | `-67.85%` | `179.70` |
| `Live` | `Long` | `1.32` | 20,520,000.00 USD | 0.00 USD | 3,360.00 USD | `-67.35%` | `2,532.40` |
| `Live` | `Long` | `1.34` | 20,510,000.00 USD | 0.00 USD | 2,100.00 USD | `-66.86%` | `1,562.70` |
| `Live` | `Long` | `1.35` | 20,510,000.00 USD | 0.00 USD | 2,000.00 USD | `-66.61%` | `1,474.80` |
| `Live` | `Long` | `1.36` | 20,510,000.00 USD | 0.00 USD | 1,640.00 USD | `-66.37%` | `1,200.00` |
| `Live` | `Long` | `1.38` | 20,510,000.00 USD | 0.00 USD | 12,720.00 USD | `-66.12%` | `9,250.10` |
| `Live` | `Long` | `1.39` | 20,490,000.00 USD | 0.00 USD | 1,360.00 USD | `-65.88%` | `983.50` |
| `Live` | `Long` | `1.40` | 20,490,000.00 USD | 0.00 USD | 931.86 USD | `-65.63%` | `668.00` |
| `Live` | `Long` | `1.42` | 20,490,000.00 USD | 0.00 USD | 82,080.00 USD | `-65.14%` | `58,008.90` |
| `Live` | `Long` | `1.43` | 20,410,000.00 USD | 0.00 USD | 3,860.00 USD | `-64.89%` | `2,707.30` |
| `Live` | `Long` | `1.44` | 20,410,000.00 USD | 0.00 USD | 762.85 USD | `-64.64%` | `531.60` |
| `Live` | `Long` | `1.45` | 20,400,000.00 USD | 0.00 USD | 30,680.00 USD | `-64.40%` | `21,231.00` |
| `Live` | `Long` | `1.46` | 20,370,000.00 USD | 0.00 USD | 145,240.00 USD | `-64.15%` | `99,819.90` |
| `Live` | `Long` | `1.48` | 20,230,000.00 USD | 0.00 USD | 4,360.00 USD | `-63.66%` | `2,957.50` |
| `Live` | `Long` | `1.50` | 20,220,000.00 USD | 0.00 USD | 438.63 USD | `-63.17%` | `293.40` |
| `Live` | `Long` | `1.50` | 20,220,000.00 USD | 0.00 USD | 1,250.00 USD | `-62.92%` | `833.40` |
| `Live` | `Long` | `1.51` | 20,220,000.00 USD | 0.00 USD | 454.50 USD | `-62.67%` | `300.00` |
| `Live` | `Long` | `1.53` | 20,220,000.00 USD | 0.00 USD | 2,110.00 USD | `-62.18%` | `1,376.90` |
| `Live` | `Long` | `1.56` | 20,220,000.00 USD | 0.00 USD | 20,570.00 USD | `-61.44%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 20,200,000.00 USD | 0.00 USD | 919.17 USD | `-61.19%` | `583.60` |
| `Live` | `Long` | `1.58` | 20,200,000.00 USD | 0.00 USD | 1,980.00 USD | `-60.95%` | `1,246.60` |
| `Live` | `Long` | `1.59` | 20,200,000.00 USD | 0.00 USD | 4,340.00 USD | `-60.70%` | `2,719.70` |
| `Live` | `Long` | `1.60` | 20,190,000.00 USD | 0.00 USD | 80,440.00 USD | `-60.46%` | `50,119.40` |
| `Live` | `Long` | `1.62` | 20,110,000.00 USD | 0.00 USD | 207.19 USD | `-59.96%` | `127.50` |
| `Live` | `Long` | `1.64` | 20,110,000.00 USD | 0.00 USD | 32,940.00 USD | `-59.72%` | `20,149.30` |
| `Live` | `Long` | `1.65` | 20,080,000.00 USD | 0.00 USD | 981.08 USD | `-59.47%` | `596.40` |
| `Live` | `Long` | `1.66` | 20,080,000.00 USD | 0.00 USD | 113.70 USD | `-59.22%` | `68.70` |
| `Live` | `Long` | `1.67` | 20,080,000.00 USD | 0.00 USD | 1,830.00 USD | `-58.98%` | `1,098.60` |
| `Live` | `Long` | `1.68` | 20,080,000.00 USD | 0.00 USD | 2,790.00 USD | `-58.73%` | `1,664.90` |
| `Live` | `Long` | `1.69` | 20,070,000.00 USD | 0.00 USD | 615,660.00 USD | `-58.48%` | `365,374.80` |
| `Live` | `Long` | `1.70` | 19,460,000.00 USD | 0.00 USD | 254.25 USD | `-58.24%` | `150.00` |
| `Live` | `Long` | `1.71` | 19,460,000.00 USD | 0.00 USD | 2,190.00 USD | `-57.99%` | `1,286.10` |
| `Live` | `Long` | `1.72` | 19,450,000.00 USD | 0.00 USD | 188.65 USD | `-57.75%` | `110.00` |
| `Live` | `Long` | `1.73` | 19,450,000.00 USD | 0.00 USD | 6,150.00 USD | `-57.50%` | `3,564.50` |
| `Live` | `Long` | `1.74` | 19,450,000.00 USD | 0.00 USD | 7,770.00 USD | `-57.25%` | `4,476.10` |
| `Live` | `Long` | `1.75` | 19,440,000.00 USD | 0.00 USD | 1,320.00 USD | `-57.01%` | `758.60` |
| `Live` | `Long` | `1.75` | 19,440,000.00 USD | 0.00 USD | 91,070.00 USD | `-56.76%` | `51,892.20` |
| `Live` | `Long` | `1.77` | 19,350,000.00 USD | 0.00 USD | 3,470.00 USD | `-56.27%` | `1,953.10` |
| `Live` | `Long` | `1.80` | 19,340,000.00 USD | 0.00 USD | 2,930.00 USD | `-55.53%` | `1,624.20` |
| `Live` | `Long` | `1.81` | 19,340,000.00 USD | 0.00 USD | 6,870.00 USD | `-55.28%` | `3,785.90` |
| `Live` | `Long` | `1.82` | 19,330,000.00 USD | 0.00 USD | 909,920.00 USD | `-55.03%` | `498,587.40` |
| `Live` | `Long` | `1.83` | 18,420,000.00 USD | 0.00 USD | 28,850.00 USD | `-54.79%` | `15,723.50` |
| `Live` | `Long` | `1.84` | 18,400,000.00 USD | 0.00 USD | 4,160.00 USD | `-54.54%` | `2,254.30` |
| `Live` | `Long` | `1.85` | 18,390,000.00 USD | 0.00 USD | 984.26 USD | `-54.30%` | `530.60` |
| `Live` | `Long` | `1.89` | 18,390,000.00 USD | 0.00 USD | 600,480.00 USD | `-53.56%` | `318,555.60` |
| `Live` | `Long` | `1.90` | 17,790,000.00 USD | 0.00 USD | 2,250.00 USD | `-53.31%` | `1,189.70` |
| `Live` | `Long` | `1.91` | 17,790,000.00 USD | 0.00 USD | 4,610.00 USD | `-53.06%` | `2,421.50` |
| `Live` | `Long` | `1.92` | 17,780,000.00 USD | 0.00 USD | 5,860.00 USD | `-52.82%` | `3,058.80` |
| `Live` | `Long` | `1.93` | 17,780,000.00 USD | 0.00 USD | 1,870.00 USD | `-52.57%` | `971.20` |
| `Live` | `Long` | `1.95` | 17,780,000.00 USD | 0.00 USD | 2,740.00 USD | `-52.08%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 17,770,000.00 USD | 0.00 USD | 16,430.00 USD | `-51.83%` | `8,402.70` |
| `Live` | `Long` | `1.97` | 17,760,000.00 USD | 0.00 USD | 3,550.00 USD | `-51.59%` | `1,806.10` |
| `Live` | `Long` | `1.98` | 17,750,000.00 USD | 0.00 USD | 34,950.00 USD | `-51.34%` | `17,697.20` |
| `Live` | `Long` | `1.99` | 17,720,000.00 USD | 0.00 USD | 1,490.00 USD | `-51.09%` | `750.00` |
| `Live` | `Long` | `2.00` | 17,720,000.00 USD | 0.00 USD | 1,000.00 USD | `-50.60%` | `499.30` |
| `Live` | `Long` | `2.02` | 17,720,000.00 USD | 0.00 USD | 1,640.00 USD | `-50.35%` | `816.00` |
| `Live` | `Long` | `2.02` | 17,710,000.00 USD | 0.00 USD | 260.62 USD | `-50.11%` | `128.70` |
| `Live` | `Long` | `2.04` | 17,710,000.00 USD | 0.00 USD | 3,460.00 USD | `-49.61%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 17,710,000.00 USD | 0.00 USD | 411.00 USD | `-49.37%` | `200.00` |
| `Live` | `Long` | `2.06` | 17,710,000.00 USD | 0.00 USD | 6,070.00 USD | `-49.12%` | `2,938.70` |
| `Live` | `Long` | `2.08` | 17,700,000.00 USD | 0.00 USD | 115,690.00 USD | `-48.88%` | `55,754.70` |
| `Live` | `Long` | `2.08` | 17,590,000.00 USD | 0.00 USD | 19,630.00 USD | `-48.63%` | `9,416.40` |
| `Live` | `Long` | `2.10` | 17,570,000.00 USD | 0.00 USD | 1,910.00 USD | `-48.38%` | `912.30` |
| `Live` | `Long` | `2.10` | 17,570,000.00 USD | 0.00 USD | 6,980.00 USD | `-48.14%` | `3,314.60` |
| `Live` | `Long` | `2.12` | 17,560,000.00 USD | 0.00 USD | 355,570.00 USD | `-47.89%` | `168,117.90` |
| `Live` | `Long` | `2.12` | 17,200,000.00 USD | 0.00 USD | 35,160.00 USD | `-47.64%` | `16,547.70` |
| `Live` | `Long` | `2.13` | 17,170,000.00 USD | 0.00 USD | 1,660.00 USD | `-47.40%` | `777.50` |
| `Live` | `Long` | `2.15` | 17,170,000.00 USD | 0.00 USD | 1,150.00 USD | `-47.15%` | `537.20` |
| `Live` | `Long` | `2.15` | 17,170,000.00 USD | 0.00 USD | 1,020.00 USD | `-46.90%` | `475.20` |
| `Live` | `Long` | `2.17` | 17,170,000.00 USD | 0.00 USD | 190,720.00 USD | `-46.66%` | `88,091.60` |
| `Live` | `Long` | `2.17` | 16,970,000.00 USD | 0.00 USD | 19,250.00 USD | `-46.41%` | `8,851.60` |
| `Live` | `Long` | `2.19` | 16,960,000.00 USD | 0.00 USD | 92,620.00 USD | `-46.17%` | `42,388.50` |
| `Live` | `Long` | `2.19` | 16,860,000.00 USD | 0.00 USD | 10,120.00 USD | `-45.92%` | `4,611.40` |
| `Live` | `Long` | `2.21` | 16,850,000.00 USD | 0.00 USD | 44,560.00 USD | `-45.67%` | `20,208.60` |
| `Live` | `Long` | `2.21` | 16,810,000.00 USD | 0.00 USD | 1,200.00 USD | `-45.43%` | `542.90` |
| `Live` | `Long` | `2.23` | 16,810,000.00 USD | 0.00 USD | 1,620.00 USD | `-45.18%` | `729.00` |
| `Live` | `Long` | `2.23` | 16,800,000.00 USD | 0.00 USD | 2,590.00 USD | `-44.93%` | `1,158.10` |
| `Live` | `Long` | `2.25` | 16,800,000.00 USD | 0.00 USD | 311,490.00 USD | `-44.69%` | `138,750.10` |
| `Live` | `Long` | `2.25` | 16,490,000.00 USD | 0.00 USD | 149,240.00 USD | `-44.44%` | `66,181.30` |
| `Live` | `Long` | `2.27` | 16,340,000.00 USD | 0.00 USD | 379,560.00 USD | `-43.95%` | `166,841.40` |
| `Live` | `Long` | `2.29` | 15,960,000.00 USD | 0.00 USD | 463.86 USD | `-43.70%` | `203.00` |
| `Live` | `Long` | `2.29` | 15,960,000.00 USD | 0.00 USD | 2,860.00 USD | `-43.45%` | `1,245.80` |
| `Live` | `Long` | `2.31` | 15,960,000.00 USD | 0.00 USD | 43,180.00 USD | `-43.21%` | `18,732.10` |
| `Live` | `Long` | `2.31` | 15,920,000.00 USD | 0.00 USD | 1,970.00 USD | `-42.96%` | `849.40` |
| `Live` | `Long` | `2.33` | 15,910,000.00 USD | 0.00 USD | 2,690.00 USD | `-42.72%` | `1,156.20` |
| `Live` | `Long` | `2.33` | 15,910,000.00 USD | 0.00 USD | 13,800.00 USD | `-42.47%` | `5,908.80` |
| `Live` | `Long` | `2.35` | 15,900,000.00 USD | 0.00 USD | 26,070.00 USD | `-42.22%` | `11,119.30` |
| `Live` | `Long` | `2.35` | 15,870,000.00 USD | 0.00 USD | 30,610.00 USD | `-41.98%` | `13,000.00` |
| `Live` | `Long` | `2.37` | 15,840,000.00 USD | 0.00 USD | 3,450.00 USD | `-41.73%` | `1,460.20` |
| `Live` | `Long` | `2.38` | 15,840,000.00 USD | 0.00 USD | 533,900.00 USD | `-41.48%` | `224,799.20` |
| `Live` | `Long` | `2.38` | 15,300,000.00 USD | 0.00 USD | 5,860.00 USD | `-41.24%` | `2,457.90` |
| `Live` | `Long` | `2.40` | 15,300,000.00 USD | 0.00 USD | 115.20 USD | `-40.99%` | `48.10` |
| `Live` | `Long` | `2.42` | 15,300,000.00 USD | 0.00 USD | 420,800.00 USD | `-40.50%` | `174,245.10` |
| `Live` | `Long` | `2.42` | 14,880,000.00 USD | 0.00 USD | 1,860,000.00 USD | `-40.25%` | `766,884.10` |
| `Live` | `Long` | `2.44` | 13,020,000.00 USD | 0.00 USD | 2,320.00 USD | `-40.01%` | `953.50` |
| `Live` | `Long` | `2.44` | 13,010,000.00 USD | 0.00 USD | 3,830.00 USD | `-39.76%` | `1,564.60` |
| `Live` | `Long` | `2.46` | 13,010,000.00 USD | 0.00 USD | 35,430.00 USD | `-39.51%` | `14,430.30` |
| `Live` | `Long` | `2.46` | 12,980,000.00 USD | 0.00 USD | 18,070.00 USD | `-39.27%` | `7,329.10` |
| `Live` | `Long` | `2.48` | 12,960,000.00 USD | 0.00 USD | 21,470.00 USD | `-39.02%` | `8,675.10` |
| `Live` | `Long` | `2.48` | 12,940,000.00 USD | 0.00 USD | 76,980.00 USD | `-38.77%` | `30,978.30` |
| `Live` | `Long` | `2.50` | 12,860,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.53%` | `443.10` |
| `Live` | `Long` | `2.50` | 12,860,000.00 USD | 0.00 USD | 6,000.00 USD | `-38.28%` | `2,395.50` |
| `Live` | `Long` | `2.52` | 12,850,000.00 USD | 0.00 USD | 1,290.00 USD | `-38.03%` | `511.60` |
| `Live` | `Long` | `2.52` | 12,850,000.00 USD | 0.00 USD | 29,000.00 USD | `-37.79%` | `11,486.00` |
| `Live` | `Long` | `2.54` | 12,820,000.00 USD | 0.00 USD | 254,240.00 USD | `-37.54%` | `100,293.80` |
| `Live` | `Long` | `2.54` | 12,570,000.00 USD | 0.00 USD | 35,030.00 USD | `-37.30%` | `13,763.60` |
| `Live` | `Long` | `2.56` | 12,530,000.00 USD | 0.00 USD | 2,880.00 USD | `-37.05%` | `1,126.90` |
| `Live` | `Long` | `2.56` | 12,530,000.00 USD | 0.00 USD | 10,170.00 USD | `-36.80%` | `3,966.60` |
| `Live` | `Long` | `2.58` | 12,520,000.00 USD | 0.00 USD | 1,260.00 USD | `-36.56%` | `490.00` |
| `Live` | `Long` | `2.58` | 12,520,000.00 USD | 0.00 USD | 905.27 USD | `-36.31%` | `350.20` |
| `Live` | `Long` | `2.60` | 12,520,000.00 USD | 0.00 USD | 116,650.00 USD | `-36.06%` | `44,950.30` |
| `Live` | `Long` | `2.60` | 12,400,000.00 USD | 0.00 USD | 3,580.00 USD | `-35.82%` | `1,374.40` |
| `Live` | `Long` | `2.62` | 12,400,000.00 USD | 0.00 USD | 13,670.00 USD | `-35.57%` | `5,226.30` |
| `Live` | `Long` | `2.62` | 12,380,000.00 USD | 0.00 USD | 1,180.00 USD | `-35.32%` | `447.70` |
| `Live` | `Long` | `2.63` | 12,380,000.00 USD | 0.00 USD | 37,330.00 USD | `-35.08%` | `14,167.70` |
| `Live` | `Long` | `2.65` | 12,340,000.00 USD | 0.00 USD | 2,650.00 USD | `-34.83%` | `1,000.00` |
| `Live` | `Long` | `2.65` | 12,340,000.00 USD | 0.00 USD | 16,760.00 USD | `-34.58%` | `6,313.40` |
| `Live` | `Long` | `2.67` | 12,320,000.00 USD | 0.00 USD | 12,860.00 USD | `-34.34%` | `4,825.60` |
| `Live` | `Long` | `2.67` | 12,310,000.00 USD | 0.00 USD | 7,140.00 USD | `-34.09%` | `2,670.60` |
| `Live` | `Long` | `2.69` | 12,300,000.00 USD | 0.00 USD | 4,970.00 USD | `-33.85%` | `1,849.60` |
| `Live` | `Long` | `2.69` | 12,300,000.00 USD | 0.00 USD | 3,260.00 USD | `-33.60%` | `1,210.20` |
| `Live` | `Long` | `2.71` | 12,300,000.00 USD | 0.00 USD | 120,220.00 USD | `-33.35%` | `44,443.30` |
| `Live` | `Long` | `2.71` | 12,180,000.00 USD | 0.00 USD | 25,340.00 USD | `-33.11%` | `9,333.60` |
| `Live` | `Long` | `2.73` | 12,150,000.00 USD | 0.00 USD | 27,780.00 USD | `-32.86%` | `10,194.90` |
| `Live` | `Long` | `2.73` | 12,120,000.00 USD | 0.00 USD | 13,540.00 USD | `-32.61%` | `4,949.50` |
| `Live` | `Long` | `2.75` | 12,110,000.00 USD | 0.00 USD | 41,170.00 USD | `-32.37%` | `14,997.30` |
| `Live` | `Long` | `2.75` | 12,070,000.00 USD | 0.00 USD | 25,260.00 USD | `-32.12%` | `9,167.40` |
| `Live` | `Long` | `2.77` | 12,040,000.00 USD | 0.00 USD | 349,840.00 USD | `-31.87%` | `126,526.20` |
| `Live` | `Long` | `2.77` | 11,690,000.00 USD | 0.00 USD | 398.77 USD | `-31.63%` | `143.70` |
| `Live` | `Long` | `2.79` | 11,690,000.00 USD | 0.00 USD | 51,460.00 USD | `-31.38%` | `18,475.90` |
| `Live` | `Long` | `2.79` | 11,640,000.00 USD | 0.00 USD | 26,200.00 USD | `-31.14%` | `9,372.90` |
| `Live` | `Long` | `2.81` | 11,620,000.00 USD | 0.00 USD | 94,090.00 USD | `-30.89%` | `33,544.40` |
| `Live` | `Long` | `2.81` | 11,520,000.00 USD | 0.00 USD | 4,110.00 USD | `-30.64%` | `1,459.90` |
| `Live` | `Long` | `2.83` | 11,520,000.00 USD | 0.00 USD | 8,640.00 USD | `-30.40%` | `3,058.00` |
| `Live` | `Long` | `2.83` | 11,510,000.00 USD | 0.00 USD | 1,710.00 USD | `-30.15%` | `602.50` |
| `Live` | `Long` | `2.85` | 11,510,000.00 USD | 0.00 USD | 3,030.00 USD | `-29.90%` | `1,063.60` |
| `Live` | `Long` | `2.85` | 11,500,000.00 USD | 0.00 USD | 5,640.00 USD | `-29.66%` | `1,976.10` |
| `Live` | `Long` | `2.87` | 11,500,000.00 USD | 0.00 USD | 8,690.00 USD | `-29.41%` | `3,034.00` |
| `Live` | `Long` | `2.88` | 11,490,000.00 USD | 0.00 USD | 405,640.00 USD | `-29.16%` | `141,093.00` |
| `Live` | `Long` | `2.88` | 11,080,000.00 USD | 0.00 USD | 93,770.00 USD | `-28.92%` | `32,501.30` |
| `Live` | `Long` | `2.90` | 10,990,000.00 USD | 0.00 USD | 16,720.00 USD | `-28.67%` | `5,774.30` |
| `Live` | `Long` | `2.90` | 10,970,000.00 USD | 0.00 USD | 94,420.00 USD | `-28.43%` | `32,502.40` |
| `Live` | `Long` | `2.92` | 10,880,000.00 USD | 0.00 USD | 85,280.00 USD | `-28.18%` | `29,254.30` |
| `Live` | `Long` | `2.92` | 10,790,000.00 USD | 0.00 USD | 47,510.00 USD | `-27.93%` | `16,244.40` |
| `Live` | `Long` | `2.94` | 10,750,000.00 USD | 0.00 USD | 49,960.00 USD | `-27.69%` | `17,022.90` |
| `Live` | `Long` | `2.94` | 10,700,000.00 USD | 0.00 USD | 18,120.00 USD | `-27.44%` | `6,152.60` |
| `Live` | `Long` | `2.96` | 10,680,000.00 USD | 0.00 USD | 1,470.00 USD | `-27.19%` | `497.80` |
| `Live` | `Long` | `2.96` | 10,680,000.00 USD | 0.00 USD | 6,880.00 USD | `-26.95%` | `2,321.90` |
| `Live` | `Long` | `2.98` | 10,670,000.00 USD | 0.00 USD | 43,150.00 USD | `-26.70%` | `14,503.80` |
| `Live` | `Long` | `2.98` | 10,630,000.00 USD | 0.00 USD | 206,990.00 USD | `-26.45%` | `69,343.40` |
| `Live` | `Long` | `3.00` | 10,420,000.00 USD | 0.00 USD | 2,000.00 USD | `-26.21%` | `666.40` |
| `Live` | `Long` | `3.00` | 10,420,000.00 USD | 0.00 USD | 10,410.00 USD | `-25.96%` | `3,463.30` |
| `Live` | `Long` | `3.02` | 10,410,000.00 USD | 0.00 USD | 21,690.00 USD | `-25.72%` | `7,194.20` |
| `Live` | `Long` | `3.02` | 10,390,000.00 USD | 0.00 USD | 20,590.00 USD | `-25.47%` | `6,805.10` |
| `Live` | `Long` | `3.04` | 10,360,000.00 USD | 0.00 USD | 17,500.00 USD | `-25.22%` | `5,766.20` |
| `Live` | `Long` | `3.04` | 10,350,000.00 USD | 0.00 USD | 374,580.00 USD | `-24.98%` | `123,013.60` |
| `Live` | `Long` | `3.06` | 9,970,000.00 USD | 0.00 USD | 23,800.00 USD | `-24.73%` | `7,790.30` |
| `Live` | `Long` | `3.06` | 9,950,000.00 USD | 0.00 USD | 115,550.00 USD | `-24.48%` | `37,700.70` |
| `Live` | `Long` | `3.08` | 9,830,000.00 USD | 0.00 USD | 91,140.00 USD | `-24.24%` | `29,639.00` |
| `Live` | `Long` | `3.08` | 9,740,000.00 USD | 0.00 USD | 31,900.00 USD | `-23.99%` | `10,339.90` |
| `Live` | `Long` | `3.10` | 9,710,000.00 USD | 0.00 USD | 5,590.00 USD | `-23.74%` | `1,805.90` |
| `Live` | `Long` | `3.10` | 9,700,000.00 USD | 0.00 USD | 24,750.00 USD | `-23.50%` | `7,971.70` |
| `Live` | `Long` | `3.12` | 9,680,000.00 USD | 0.00 USD | 32,910.00 USD | `-23.25%` | `10,565.20` |
| `Live` | `Long` | `3.12` | 9,650,000.00 USD | 0.00 USD | 22,120.00 USD | `-23.00%` | `7,077.20` |
| `Live` | `Long` | `3.13` | 9,630,000.00 USD | 0.00 USD | 7,780.00 USD | `-22.76%` | `2,481.00` |
| `Live` | `Long` | `3.15` | 9,620,000.00 USD | 0.00 USD | 220,990.00 USD | `-22.51%` | `70,266.40` |
| `Live` | `Long` | `3.15` | 9,400,000.00 USD | 0.00 USD | 168,940.00 USD | `-22.27%` | `53,547.40` |
| `Live` | `Long` | `3.17` | 9,230,000.00 USD | 0.00 USD | 91,330.00 USD | `-22.02%` | `28,855.50` |
| `Live` | `Long` | `3.17` | 9,140,000.00 USD | 0.00 USD | 26,600.00 USD | `-21.77%` | `8,376.60` |
| `Live` | `Long` | `3.19` | 9,110,000.00 USD | 0.00 USD | 245,670.00 USD | `-21.53%` | `77,132.70` |
| `Live` | `Long` | `3.21` | 8,860,000.00 USD | 0.00 USD | 9,520.00 USD | `-21.03%` | `2,971.20` |
| `Live` | `Long` | `3.21` | 8,850,000.00 USD | 0.00 USD | 16,350.00 USD | `-20.79%` | `5,086.80` |
| `Live` | `Long` | `3.23` | 8,840,000.00 USD | 0.00 USD | 23,780.00 USD | `-20.54%` | `7,374.20` |
| `Live` | `Long` | `3.23` | 8,810,000.00 USD | 0.00 USD | 43,870.00 USD | `-20.29%` | `13,560.40` |
| `Live` | `Long` | `3.25` | 8,770,000.00 USD | 0.00 USD | 74,100.00 USD | `-20.05%` | `22,834.70` |
| `Live` | `Long` | `3.25` | 8,700,000.00 USD | 0.00 USD | 5,640.00 USD | `-19.80%` | `1,733.30` |
| `Live` | `Long` | `3.27` | 8,690,000.00 USD | 0.00 USD | 52,930.00 USD | `-19.56%` | `16,210.30` |
| `Live` | `Long` | `3.27` | 8,640,000.00 USD | 0.00 USD | 868,070.00 USD | `-19.31%` | `265,060.40` |
| `Live` | `Long` | `3.29` | 7,770,000.00 USD | 0.00 USD | 3,180.00 USD | `-19.06%` | `967.90` |
| `Live` | `Long` | `3.29` | 7,770,000.00 USD | 0.00 USD | 133,280.00 USD | `-18.82%` | `40,449.50` |
| `Live` | `Long` | `3.31` | 7,630,000.00 USD | 0.00 USD | 125,000.00 USD | `-18.57%` | `37,822.50` |
| `Live` | `Long` | `3.31` | 7,510,000.00 USD | 0.00 USD | 17,590.00 USD | `-18.32%` | `5,307.20` |
| `Live` | `Long` | `3.33` | 7,490,000.00 USD | 0.00 USD | 9,990.00 USD | `-18.08%` | `3,003.30` |
| `Live` | `Long` | `3.33` | 7,480,000.00 USD | 0.00 USD | 74,540.00 USD | `-17.83%` | `22,351.30` |
| `Live` | `Long` | `3.35` | 7,410,000.00 USD | 0.00 USD | 31,800.00 USD | `-17.58%` | `9,506.80` |
| `Live` | `Long` | `3.35` | 7,370,000.00 USD | 0.00 USD | 2,440.00 USD | `-17.34%` | `727.80` |
| `Live` | `Long` | `3.37` | 7,370,000.00 USD | 0.00 USD | 141,980.00 USD | `-17.09%` | `42,193.60` |
| `Live` | `Long` | `3.38` | 7,230,000.00 USD | 0.00 USD | 69,770.00 USD | `-16.85%` | `20,673.60` |
| `Live` | `Long` | `3.38` | 7,160,000.00 USD | 0.00 USD | 54,830.00 USD | `-16.60%` | `16,197.80` |
| `Live` | `Long` | `3.40` | 7,110,000.00 USD | 0.00 USD | 10,810.00 USD | `-16.35%` | `3,183.40` |
| `Live` | `Long` | `3.40` | 7,090,000.00 USD | 0.00 USD | 98,820.00 USD | `-16.11%` | `29,022.40` |
| `Live` | `Long` | `3.42` | 7,000,000.00 USD | 0.00 USD | 552,690.00 USD | `-15.86%` | `161,843.10` |
| `Live` | `Long` | `3.42` | 6,440,000.00 USD | 0.00 USD | 38,260.00 USD | `-15.61%` | `11,171.70` |
| `Live` | `Long` | `3.44` | 6,400,000.00 USD | 0.00 USD | 34,830.00 USD | `-15.37%` | `10,138.80` |
| `Live` | `Long` | `3.44` | 6,370,000.00 USD | 0.00 USD | 13,870.00 USD | `-15.12%` | `4,025.40` |
| `Live` | `Long` | `3.46` | 6,360,000.00 USD | 0.00 USD | 12,320.00 USD | `-14.87%` | `3,564.90` |
| `Live` | `Long` | `3.46` | 6,340,000.00 USD | 0.00 USD | 14,030.00 USD | `-14.63%` | `4,050.10` |
| `Live` | `Long` | `3.48` | 6,330,000.00 USD | 0.00 USD | 181,230.00 USD | `-14.38%` | `52,152.00` |
| `Live` | `Long` | `3.48` | 6,150,000.00 USD | 0.00 USD | 24,690.00 USD | `-14.14%` | `7,084.60` |
| `Live` | `Long` | `3.50` | 6,120,000.00 USD | 0.00 USD | 62,550.00 USD | `-13.89%` | `17,895.80` |
| `Live` | `Long` | `3.50` | 6,060,000.00 USD | 0.00 USD | 32,800.00 USD | `-13.64%` | `9,357.20` |
| `Live` | `Long` | `3.52` | 6,030,000.00 USD | 0.00 USD | 8,020.00 USD | `-13.40%` | `2,280.90` |
| `Live` | `Long` | `3.52` | 6,020,000.00 USD | 0.00 USD | 205,380.00 USD | `-13.15%` | `58,262.70` |
| `Live` | `Long` | `3.54` | 5,810,000.00 USD | 0.00 USD | 1,440,000.00 USD | `-12.90%` | `406,919.30` |
| `Live` | `Long` | `3.54` | 4,380,000.00 USD | 0.00 USD | 168,380.00 USD | `-12.66%` | `47,498.20` |
| `Live` | `Long` | `3.56` | 4,210,000.00 USD | 0.00 USD | 383,600.00 USD | `-12.41%` | `107,904.10` |
| `Live` | `Long` | `3.56` | 3,820,000.00 USD | 0.00 USD | 8,960.00 USD | `-12.16%` | `2,512.40` |
| `Live` | `Long` | `3.58` | 3,820,000.00 USD | 0.00 USD | 43,530.00 USD | `-11.92%` | `12,176.10` |
| `Live` | `Long` | `3.58` | 3,770,000.00 USD | 0.00 USD | 34,670.00 USD | `-11.67%` | `9,670.90` |
| `Live` | `Long` | `3.60` | 3,740,000.00 USD | 0.00 USD | 24,080.00 USD | `-11.42%` | `6,699.10` |
| `Live` | `Long` | `3.60` | 3,710,000.00 USD | 0.00 USD | 60,200.00 USD | `-11.18%` | `16,699.70` |
| `Live` | `Long` | `3.62` | 3,650,000.00 USD | 0.00 USD | 21,040.00 USD | `-10.93%` | `5,820.90` |
| `Live` | `Long` | `3.62` | 3,630,000.00 USD | 0.00 USD | 125,390.00 USD | `-10.69%` | `34,589.10` |
| `Live` | `Long` | `3.63` | 3,510,000.00 USD | 0.00 USD | 10,560.00 USD | `-10.44%` | `2,904.90` |
| `Live` | `Long` | `3.65` | 3,500,000.00 USD | 0.00 USD | 50,500.00 USD | `-10.19%` | `13,854.50` |
| `Live` | `Long` | `3.65` | 3,450,000.00 USD | 0.00 USD | 14,180.00 USD | `-9.95%` | `3,879.10` |
| `Live` | `Long` | `3.67` | 3,430,000.00 USD | 0.00 USD | 50,850.00 USD | `-9.70%` | `13,874.40` |
| `Live` | `Long` | `3.67` | 3,380,000.00 USD | 0.00 USD | 87,540.00 USD | `-9.45%` | `23,820.60` |
| `Live` | `Long` | `3.69` | 3,290,000.00 USD | 0.00 USD | 146,340.00 USD | `-9.21%` | `39,713.70` |
| `Live` | `Long` | `3.69` | 3,150,000.00 USD | 0.00 USD | 94,330.00 USD | `-8.96%` | `25,529.50` |
| `Live` | `Long` | `3.71` | 3,050,000.00 USD | 0.00 USD | 212,700.00 USD | `-8.71%` | `57,408.40` |
| `Live` | `Long` | `3.71` | 2,840,000.00 USD | 0.00 USD | 15,680.00 USD | `-8.47%` | `4,221.10` |
| `Live` | `Long` | `3.73` | 2,820,000.00 USD | 0.00 USD | 271,510.00 USD | `-8.22%` | `72,888.50` |
| `Live` | `Long` | `3.73` | 2,550,000.00 USD | 0.00 USD | 394,290.00 USD | `-7.98%` | `105,565.50` |
| `Live` | `Long` | `3.75` | 2,160,000.00 USD | 0.00 USD | 39,750.00 USD | `-7.73%` | `10,614.40` |
| `Live` | `Long` | `3.75` | 2,120,000.00 USD | 0.00 USD | 153,580.00 USD | `-7.48%` | `40,900.20` |
| `Live` | `Long` | `3.77` | 1,960,000.00 USD | 0.00 USD | 69,750.00 USD | `-7.24%` | `18,526.80` |
| `Live` | `Long` | `3.77` | 1,890,000.00 USD | 0.00 USD | 67,960.00 USD | `-6.99%` | `18,002.80` |
| `Live` | `Long` | `3.79` | 1,830,000.00 USD | 0.00 USD | 46,300.00 USD | `-6.74%` | `12,233.00` |
| `Live` | `Long` | `3.79` | 1,780,000.00 USD | 0.00 USD | 145,620.00 USD | `-6.50%` | `38,371.30` |
| `Live` | `Long` | `3.81` | 1,640,000.00 USD | 0.00 USD | 472,430.00 USD | `-6.25%` | `124,159.20` |
| `Live` | `Long` | `3.81` | 1,160,000.00 USD | 0.00 USD | 202,270.00 USD | `-6.00%` | `53,019.80` |
| `Live` | `Long` | `3.83` | 960,370.00 USD | 0.00 USD | 159,740.00 USD | `-5.76%` | `41,762.10` |
| `Live` | `Long` | `3.83` | 800,630.00 USD | 0.00 USD | 207,570.00 USD | `-5.51%` | `54,126.30` |
| `Live` | `Long` | `3.85` | 593,050.00 USD | 0.00 USD | 133,920.00 USD | `-5.27%` | `34,829.50` |
| `Live` | `Long` | `3.85` | 459,130.00 USD | 0.00 USD | 122,550.00 USD | `-5.02%` | `31,788.70` |
| `Live` | `Long` | `3.87` | 336,590.00 USD | 0.00 USD | 27,290.00 USD | `-4.77%` | `7,061.30` |
| `Live` | `Long` | `3.88` | 309,300.00 USD | 0.00 USD | 136,810.00 USD | `-4.53%` | `35,305.30` |
| `Live` | `Long` | `3.88` | 172,490.00 USD | 0.00 USD | 88,930.00 USD | `-4.28%` | `22,890.40` |
| `Live` | `Long` | `3.90` | 83,560.00 USD | 0.00 USD | 75,910.00 USD | `-4.03%` | `19,488.70` |
| `Live` | `Long` | `3.90` | 7,650.00 USD | 0.00 USD | 4,350.00 USD | `-3.79%` | `1,114.10` |
| `Live` | `Long` | `3.98` | 3,300.00 USD | 0.00 USD | 3,300.00 USD | `-1.82%` | `828.40` |
| `Live` | `Short` | `4.12` | 1,450.00 USD | 1,450.00 USD | 0.00 USD | `+1.63%` | `352.50` |
| `Live` | `Short` | `4.13` | 8,180.00 USD | 6,730.00 USD | 0.00 USD | `+1.88%` | `1,626.90` |
| `Live` | `Short` | `4.14` | 9,620.00 USD | 1,430.00 USD | 0.00 USD | `+2.13%` | `346.20` |
| `Live` | `Short` | `4.16` | 10,250.00 USD | 638.21 USD | 0.00 USD | `+2.37%` | `153.60` |
| `Live` | `Short` | `4.17` | 20,290.00 USD | 10,040.00 USD | 0.00 USD | `+2.87%` | `2,404.60` |
| `Live` | `Short` | `4.18` | 75,120.00 USD | 54,820.00 USD | 0.00 USD | `+3.11%` | `13,099.50` |
| `Live` | `Short` | `4.20` | 75,780.00 USD | 666.59 USD | 0.00 USD | `+3.36%` | `158.90` |
| `Live` | `Short` | `4.21` | 80,240.00 USD | 4,460.00 USD | 0.00 USD | `+3.60%` | `1,059.90` |
| `Live` | `Short` | `4.21` | 81,080.00 USD | 837.10 USD | 0.00 USD | `+3.85%` | `198.60` |
| `Live` | `Short` | `4.22` | 82,130.00 USD | 1,060.00 USD | 0.00 USD | `+4.10%` | `250.70` |
| `Live` | `Short` | `4.24` | 87,960.00 USD | 5,820.00 USD | 0.00 USD | `+4.34%` | `1,374.70` |
| `Live` | `Short` | `4.25` | 88,610.00 USD | 649.06 USD | 0.00 USD | `+4.59%` | `152.90` |
| `Live` | `Short` | `4.26` | 88,810.00 USD | 208.99 USD | 0.00 USD | `+5.08%` | `49.00` |
| `Live` | `Short` | `4.28` | 93,680.00 USD | 4,860.00 USD | 0.00 USD | `+5.33%` | `1,137.50` |
| `Live` | `Short` | `4.29` | 93,840.00 USD | 163.69 USD | 0.00 USD | `+5.58%` | `38.20` |
| `Live` | `Short` | `4.29` | 301,530.00 USD | 207,690.00 USD | 0.00 USD | `+5.82%` | `48,355.30` |
| `Live` | `Short` | `4.30` | 306,600.00 USD | 5,070.00 USD | 0.00 USD | `+6.07%` | `1,178.30` |
| `Live` | `Short` | `4.32` | 337,730.00 USD | 31,130.00 USD | 0.00 USD | `+6.31%` | `7,213.30` |
| `Live` | `Short` | `4.33` | 338,100.00 USD | 373.68 USD | 0.00 USD | `+6.56%` | `86.40` |
| `Live` | `Short` | `4.34` | 342,220.00 USD | 4,130.00 USD | 0.00 USD | `+7.05%` | `949.40` |
| `Live` | `Short` | `4.36` | 345,280.00 USD | 3,050.00 USD | 0.00 USD | `+7.30%` | `701.00` |
| `Live` | `Short` | `4.38` | 346,390.00 USD | 1,110.00 USD | 0.00 USD | `+7.79%` | `254.40` |
| `Live` | `Short` | `4.39` | 539,100.00 USD | 192,710.00 USD | 0.00 USD | `+8.29%` | `43,846.50` |
| `Live` | `Short` | `4.41` | 540,500.00 USD | 1,410.00 USD | 0.00 USD | `+8.53%` | `319.80` |
| `Live` | `Short` | `4.42` | 540,610.00 USD | 104.87 USD | 0.00 USD | `+9.03%` | `23.70` |
| `Live` | `Short` | `4.46` | 541,080.00 USD | 468.38 USD | 0.00 USD | `+10.01%` | `104.90` |
| `Live` | `Short` | `4.47` | 541,710.00 USD | 629.18 USD | 0.00 USD | `+10.26%` | `140.60` |
| `Live` | `Short` | `4.50` | 631,890.00 USD | 90,180.00 USD | 0.00 USD | `+10.75%` | `20,062.40` |
| `Live` | `Short` | `4.50` | 632,170.00 USD | 283.81 USD | 0.00 USD | `+11.00%` | `63.00` |
| `Live` | `Short` | `4.51` | 633,140.00 USD | 967.56 USD | 0.00 USD | `+11.24%` | `214.30` |
| `Live` | `Short` | `4.53` | 651,960.00 USD | 18,820.00 USD | 0.00 USD | `+11.49%` | `4,160.10` |
| `Live` | `Short` | `4.54` | 652,360.00 USD | 394.51 USD | 0.00 USD | `+11.98%` | `86.80` |
| `Live` | `Short` | `4.57` | 652,600.00 USD | 243.77 USD | 0.00 USD | `+12.47%` | `53.40` |
| `Live` | `Short` | `4.58` | 835,110.00 USD | 182,510.00 USD | 0.00 USD | `+12.72%` | `39,893.60` |
| `Live` | `Short` | `4.59` | 835,940.00 USD | 827.10 USD | 0.00 USD | `+13.21%` | `180.00` |
| `Live` | `Short` | `4.61` | 836,990.00 USD | 1,050.00 USD | 0.00 USD | `+13.46%` | `227.10` |
| `Live` | `Short` | `4.62` | 840,910.00 USD | 3,920.00 USD | 0.00 USD | `+13.71%` | `849.60` |
| `Live` | `Short` | `4.63` | 841,900.00 USD | 990.04 USD | 0.00 USD | `+14.20%` | `213.60` |
| `Live` | `Short` | `4.64` | 842,070.00 USD | 169.54 USD | 0.00 USD | `+14.45%` | `36.50` |
| `Live` | `Short` | `4.66` | 842,190.00 USD | 124.75 USD | 0.00 USD | `+14.69%` | `26.80` |
| `Live` | `Short` | `4.67` | 842,290.00 USD | 101.70 USD | 0.00 USD | `+14.94%` | `21.80` |
| `Live` | `Short` | `4.68` | 890,320.00 USD | 48,020.00 USD | 0.00 USD | `+15.43%` | `10,250.40` |
| `Live` | `Short` | `4.70` | 890,550.00 USD | 230.06 USD | 0.00 USD | `+15.68%` | `49.00` |
| `Live` | `Short` | `4.71` | 898,030.00 USD | 7,480.00 USD | 0.00 USD | `+15.92%` | `1,590.30` |
| `Live` | `Short` | `4.71` | 898,490.00 USD | 460.18 USD | 0.00 USD | `+16.17%` | `97.60` |
| `Live` | `Short` | `4.75` | 902,790.00 USD | 4,310.00 USD | 0.00 USD | `+16.91%` | `907.30` |
| `Live` | `Short` | `4.76` | 903,020.00 USD | 227.77 USD | 0.00 USD | `+17.40%` | `47.80` |
| `Live` | `Short` | `4.78` | 911,810.00 USD | 8,780.00 USD | 0.00 USD | `+17.65%` | `1,839.40` |
| `Live` | `Short` | `4.79` | 911,950.00 USD | 143.55 USD | 0.00 USD | `+17.89%` | `30.00` |
| `Live` | `Short` | `4.79` | 913,280.00 USD | 1,330.00 USD | 0.00 USD | `+18.14%` | `277.70` |
| `Live` | `Short` | `4.82` | 958,950.00 USD | 45,670.00 USD | 0.00 USD | `+18.63%` | `9,484.50` |
| `Live` | `Short` | `4.83` | 961,970.00 USD | 3,020.00 USD | 0.00 USD | `+18.88%` | `625.50` |
| `Live` | `Short` | `4.83` | 963,920.00 USD | 1,950.00 USD | 0.00 USD | `+19.13%` | `403.60` |
| `Live` | `Short` | `4.84` | 975,140.00 USD | 11,220.00 USD | 0.00 USD | `+19.37%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 975,280.00 USD | 137.68 USD | 0.00 USD | `+19.87%` | `28.30` |
| `Live` | `Short` | `4.88` | 976,110.00 USD | 827.03 USD | 0.00 USD | `+20.36%` | `169.30` |
| `Live` | `Short` | `4.92` | 996,820.00 USD | 20,720.00 USD | 0.00 USD | `+21.10%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 998,920.00 USD | 2,100.00 USD | 0.00 USD | `+21.34%` | `425.70` |
| `Live` | `Short` | `4.93` | 999,080.00 USD | 157.43 USD | 0.00 USD | `+21.59%` | `31.90` |
| `Live` | `Short` | `4.96` | 999,420.00 USD | 342.89 USD | 0.00 USD | `+22.08%` | `69.20` |
| `Live` | `Short` | `4.97` | 1,100,000.00 USD | 99,810.00 USD | 0.00 USD | `+22.58%` | `20,062.00` |
| `Live` | `Short` | `5.00` | 1,100,000.00 USD | 339.66 USD | 0.00 USD | `+23.07%` | `68.00` |
| `Live` | `Short` | `5.05` | 1,130,000.00 USD | 35,380.00 USD | 0.00 USD | `+24.55%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,140,000.00 USD | 3,420.00 USD | 0.00 USD | `+24.79%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,140,000.00 USD | 1,090.00 USD | 0.00 USD | `+25.29%` | `214.10` |
| `Live` | `Short` | `5.12` | 1,180,000.00 USD | 37,150.00 USD | 0.00 USD | `+26.03%` | `7,262.50` |
| `Live` | `Short` | `5.12` | 1,180,000.00 USD | 2,560.00 USD | 0.00 USD | `+26.27%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,180,000.00 USD | 751.51 USD | 0.00 USD | `+27.26%` | `145.50` |
| `Live` | `Short` | `5.18` | 1,260,000.00 USD | 82,840.00 USD | 0.00 USD | `+27.75%` | `15,976.20` |
| `Live` | `Short` | `5.20` | 1,280,000.00 USD | 22,080.00 USD | 0.00 USD | `+28.00%` | `4,251.20` |
| `Live` | `Short` | `5.22` | 1,360,000.00 USD | 74,720.00 USD | 0.00 USD | `+28.74%` | `14,300.00` |
| `Live` | `Short` | `5.25` | 1,360,000.00 USD | 143.71 USD | 0.00 USD | `+29.23%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,360,000.00 USD | 1,970.00 USD | 0.00 USD | `+29.47%` | `375.40` |
| `Live` | `Short` | `5.26` | 1,380,000.00 USD | 16,140.00 USD | 0.00 USD | `+29.72%` | `3,066.10` |
| `Live` | `Short` | `5.29` | 1,380,000.00 USD | 134.77 USD | 0.00 USD | `+30.21%` | `25.50` |
| `Live` | `Short` | `5.30` | 1,380,000.00 USD | 524.66 USD | 0.00 USD | `+30.71%` | `98.90` |
| `Live` | `Short` | `5.32` | 1,380,000.00 USD | 718.59 USD | 0.00 USD | `+30.95%` | `135.20` |
| `Live` | `Short` | `5.33` | 2,450,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+31.45%` | `200,000.00` |
| `Live` | `Short` | `5.34` | 2,450,000.00 USD | 616.28 USD | 0.00 USD | `+31.69%` | `115.30` |
| `Live` | `Short` | `5.36` | 2,450,000.00 USD | 142.44 USD | 0.00 USD | `+31.94%` | `26.60` |
| `Live` | `Short` | `5.41` | 2,450,000.00 USD | 5,410.00 USD | 0.00 USD | `+33.17%` | `1,000.00` |
| `Live` | `Short` | `5.43` | 2,510,000.00 USD | 61,270.00 USD | 0.00 USD | `+33.91%` | `11,273.30` |
| `Live` | `Short` | `5.45` | 2,510,000.00 USD | 702.41 USD | 0.00 USD | `+34.16%` | `129.00` |
| `Live` | `Short` | `5.46` | 2,560,000.00 USD | 43,980.00 USD | 0.00 USD | `+34.40%` | `8,061.90` |
| `Live` | `Short` | `5.47` | 2,560,000.00 USD | 627.98 USD | 0.00 USD | `+34.90%` | `114.70` |
| `Live` | `Short` | `5.50` | 2,630,000.00 USD | 66,470.00 USD | 0.00 USD | `+35.39%` | `12,097.30` |
| `Live` | `Short` | `5.51` | 2,660,000.00 USD | 38,800.00 USD | 0.00 USD | `+35.88%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 2,660,000.00 USD | 209.22 USD | 0.00 USD | `+36.37%` | `37.80` |
| `Live` | `Short` | `5.57` | 2,740,000.00 USD | 71,830.00 USD | 0.00 USD | `+37.11%` | `12,907.10` |
| `Live` | `Short` | `5.58` | 2,800,000.00 USD | 62,580.00 USD | 0.00 USD | `+37.61%` | `11,205.20` |
| `Live` | `Short` | `5.59` | 2,800,000.00 USD | 686.51 USD | 0.00 USD | `+37.85%` | `122.70` |
| `Live` | `Short` | `5.61` | 2,860,000.00 USD | 56,050.00 USD | 0.00 USD | `+38.10%` | `10,000.00` |
| `Live` | `Short` | `5.62` | 4,480,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+38.59%` | `288,027.90` |
| `Live` | `Short` | `5.67` | 4,480,000.00 USD | 211.30 USD | 0.00 USD | `+39.58%` | `37.30` |
| `Live` | `Short` | `5.67` | 4,480,000.00 USD | 228.70 USD | 0.00 USD | `+39.82%` | `40.30` |
| `Live` | `Short` | `5.68` | 4,500,000.00 USD | 26,090.00 USD | 0.00 USD | `+40.07%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 4,500,000.00 USD | 1,520.00 USD | 0.00 USD | `+40.32%` | `267.40` |
| `Live` | `Short` | `5.71` | 4,510,000.00 USD | 2,130.00 USD | 0.00 USD | `+40.81%` | `372.40` |
| `Live` | `Short` | `5.75` | 4,510,000.00 USD | 4,580.00 USD | 0.00 USD | `+41.55%` | `796.90` |
| `Live` | `Short` | `5.75` | 4,510,000.00 USD | 286.02 USD | 0.00 USD | `+41.79%` | `49.70` |
| `Live` | `Short` | `5.80` | 4,510,000.00 USD | 2,670.00 USD | 0.00 USD | `+43.03%` | `460.20` |
| `Live` | `Short` | `5.82` | 4,510,000.00 USD | 127.93 USD | 0.00 USD | `+43.27%` | `22.00` |
| `Live` | `Short` | `5.84` | 4,510,000.00 USD | 310.95 USD | 0.00 USD | `+44.01%` | `53.20` |
| `Live` | `Short` | `5.86` | 4,510,000.00 USD | 848.39 USD | 0.00 USD | `+44.26%` | `144.90` |
| `Live` | `Short` | `5.87` | 4,510,000.00 USD | 200.00 USD | 0.00 USD | `+44.50%` | `34.10` |
| `Live` | `Short` | `5.88` | 4,520,000.00 USD | 7,150.00 USD | 0.00 USD | `+45.00%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 4,610,000.00 USD | 88,590.00 USD | 0.00 USD | `+45.24%` | `15,027.60` |
| `Live` | `Short` | `5.91` | 4,610,000.00 USD | 151.76 USD | 0.00 USD | `+45.49%` | `25.70` |
| `Live` | `Short` | `5.92` | 4,610,000.00 USD | 189.28 USD | 0.00 USD | `+45.74%` | `32.00` |
| `Live` | `Short` | `5.92` | 4,950,000.00 USD | 343,290.00 USD | 0.00 USD | `+45.98%` | `57,938.40` |
| `Live` | `Short` | `5.95` | 5,060,000.00 USD | 103,650.00 USD | 0.00 USD | `+46.48%` | `17,434.80` |
| `Live` | `Short` | `6.00` | 5,450,000.00 USD | 388,640.00 USD | 0.00 USD | `+47.95%` | `64,719.30` |
| `Live` | `Short` | `6.03` | 5,790,000.00 USD | 345,420.00 USD | 0.00 USD | `+48.45%` | `57,330.80` |
| `Live` | `Short` | `6.04` | 5,990,000.00 USD | 196,080.00 USD | 0.00 USD | `+48.69%` | `32,490.00` |
| `Live` | `Short` | `6.07` | 5,990,000.00 USD | 740.54 USD | 0.00 USD | `+49.43%` | `122.10` |
| `Live` | `Short` | `6.08` | 6,010,000.00 USD | 23,590.00 USD | 0.00 USD | `+49.68%` | `3,883.80` |
| `Live` | `Short` | `6.08` | 6,020,000.00 USD | 5,920.00 USD | 0.00 USD | `+49.92%` | `973.10` |
| `Live` | `Short` | `6.09` | 6,060,000.00 USD | 37,510.00 USD | 0.00 USD | `+50.17%` | `6,154.10` |
| `Live` | `Short` | `6.13` | 6,060,000.00 USD | 2,430.00 USD | 0.00 USD | `+51.16%` | `396.10` |
| `Live` | `Short` | `6.18` | 6,060,000.00 USD | 5,270.00 USD | 0.00 USD | `+52.39%` | `852.80` |
| `Live` | `Short` | `6.24` | 6,350,000.00 USD | 288,250.00 USD | 0.00 USD | `+53.62%` | `46,230.70` |
| `Live` | `Short` | `6.25` | 6,360,000.00 USD | 7,300.00 USD | 0.00 USD | `+53.87%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 6,360,000.00 USD | 439.10 USD | 0.00 USD | `+54.11%` | `70.20` |
| `Live` | `Short` | `6.28` | 6,360,000.00 USD | 397.84 USD | 0.00 USD | `+54.61%` | `63.40` |
| `Live` | `Short` | `6.32` | 6,360,000.00 USD | 310.70 USD | 0.00 USD | `+55.59%` | `49.20` |
| `Live` | `Short` | `6.33` | 6,360,000.00 USD | 382.00 USD | 0.00 USD | `+56.08%` | `60.30` |
| `Live` | `Short` | `6.34` | 6,360,000.00 USD | 214.46 USD | 0.00 USD | `+56.33%` | `33.80` |
| `Live` | `Short` | `6.37` | 6,360,000.00 USD | 2,060.00 USD | 0.00 USD | `+56.82%` | `322.90` |
| `Live` | `Short` | `6.38` | 6,360,000.00 USD | 1,460.00 USD | 0.00 USD | `+57.07%` | `228.80` |
| `Live` | `Short` | `6.38` | 6,370,000.00 USD | 2,000.00 USD | 0.00 USD | `+57.32%` | `312.80` |
| `Live` | `Short` | `6.41` | 6,370,000.00 USD | 5,740.00 USD | 0.00 USD | `+57.81%` | `896.30` |
| `Live` | `Short` | `6.42` | 6,380,000.00 USD | 8,700.00 USD | 0.00 USD | `+58.06%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 6,380,000.00 USD | 173.47 USD | 0.00 USD | `+58.30%` | `27.00` |
| `Live` | `Short` | `6.43` | 6,460,000.00 USD | 77,220.00 USD | 0.00 USD | `+58.55%` | `12,000.00` |
| `Live` | `Short` | `6.45` | 6,510,000.00 USD | 55,720.00 USD | 0.00 USD | `+58.79%` | `8,645.80` |
| `Live` | `Short` | `6.46` | 6,520,000.00 USD | 7,150.00 USD | 0.00 USD | `+59.04%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 6,520,000.00 USD | 1,940.00 USD | 0.00 USD | `+59.29%` | `300.00` |
| `Live` | `Short` | `6.49` | 6,520,000.00 USD | 911.79 USD | 0.00 USD | `+59.78%` | `140.60` |
| `Live` | `Short` | `6.51` | 6,520,000.00 USD | 380.48 USD | 0.00 USD | `+60.52%` | `58.40` |
| `Live` | `Short` | `6.54` | 6,520,000.00 USD | 265.07 USD | 0.00 USD | `+61.26%` | `40.50` |
| `Live` | `Short` | `6.58` | 6,790,000.00 USD | 269,120.00 USD | 0.00 USD | `+62.24%` | `40,869.30` |
| `Live` | `Short` | `6.59` | 6,790,000.00 USD | 418.78 USD | 0.00 USD | `+62.49%` | `63.50` |
| `Live` | `Short` | `6.61` | 6,790,000.00 USD | 700.79 USD | 0.00 USD | `+62.74%` | `106.10` |
| `Live` | `Short` | `6.64` | 36,750,000.00 USD | 29,950,000.00 USD | 0.00 USD | `+63.72%` | `4,507,262.50` |
| `Live` | `Short` | `6.66` | 36,790,000.00 USD | 48,430.00 USD | 0.00 USD | `+63.97%` | `7,276.90` |
| `Live` | `Short` | `6.67` | 36,790,000.00 USD | 233.94 USD | 0.00 USD | `+64.22%` | `35.10` |
| `Live` | `Short` | `6.67` | 36,790,000.00 USD | 200.25 USD | 0.00 USD | `+64.46%` | `30.00` |
| `Live` | `Short` | `6.68` | 36,830,000.00 USD | 37,150.00 USD | 0.00 USD | `+64.71%` | `5,556.90` |
| `Live` | `Short` | `6.75` | 36,840,000.00 USD | 11,490.00 USD | 0.00 USD | `+66.19%` | `1,704.00` |
| `Live` | `Short` | `6.75` | 38,090,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+66.43%` | `184,501.00` |
| `Live` | `Short` | `6.76` | 38,180,000.00 USD | 90,430.00 USD | 0.00 USD | `+66.68%` | `13,367.10` |
| `Live` | `Short` | `6.79` | 38,190,000.00 USD | 15,200.00 USD | 0.00 USD | `+67.42%` | `2,237.40` |
| `Live` | `Short` | `6.84` | 38,200,000.00 USD | 753.63 USD | 0.00 USD | `+68.65%` | `110.10` |
| `Live` | `Short` | `6.87` | 38,200,000.00 USD | 2,650.00 USD | 0.00 USD | `+69.14%` | `386.60` |
| `Live` | `Short` | `6.88` | 38,200,000.00 USD | 295.62 USD | 0.00 USD | `+69.39%` | `43.00` |
| `Live` | `Short` | `6.92` | 38,210,000.00 USD | 6,920.00 USD | 0.00 USD | `+70.62%` | `1,000.00` |
| `Live` | `Short` | `6.99` | 39,520,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+72.10%` | `188,095.10` |
| `Live` | `Short` | `7.00` | 39,520,000.00 USD | 190.96 USD | 0.00 USD | `+72.35%` | `27.30` |
| `Live` | `Short` | `7.03` | 39,520,000.00 USD | 665.27 USD | 0.00 USD | `+73.08%` | `94.70` |
| `Live` | `Short` | `7.09` | 39,520,000.00 USD | 699.57 USD | 0.00 USD | `+74.81%` | `98.60` |
| `Live` | `Short` | `7.20` | 39,520,000.00 USD | 171.96 USD | 0.00 USD | `+77.27%` | `23.90` |
| `Live` | `Short` | `7.21` | 39,530,000.00 USD | 13,560.00 USD | 0.00 USD | `+77.77%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 39,540,000.00 USD | 4,910.00 USD | 0.00 USD | `+78.26%` | `679.30` |
| `Live` | `Short` | `7.32` | 39,540,000.00 USD | 580.08 USD | 0.00 USD | `+80.23%` | `79.30` |
| `Live` | `Short` | `7.33` | 39,540,000.00 USD | 1,320.00 USD | 0.00 USD | `+80.72%` | `180.00` |
| `Live` | `Short` | `7.34` | 39,550,000.00 USD | 11,120.00 USD | 0.00 USD | `+80.97%` | `1,514.20` |
| `Live` | `Short` | `7.38` | 39,550,000.00 USD | 1,850.00 USD | 0.00 USD | `+81.95%` | `250.00` |
| `Live` | `Short` | `7.42` | 39,660,000.00 USD | 106,000.00 USD | 0.00 USD | `+82.94%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 39,660,000.00 USD | 1,420.00 USD | 0.00 USD | `+83.68%` | `191.10` |
| `Live` | `Short` | `7.47` | 39,660,000.00 USD | 783.38 USD | 0.00 USD | `+84.17%` | `104.80` |
| `Live` | `Short` | `7.53` | 49,720,000.00 USD | 10,050,000.00 USD | 0.00 USD | `+85.40%` | `1,336,208.40` |
| `Live` | `Short` | `7.54` | 49,720,000.00 USD | 2,340.00 USD | 0.00 USD | `+85.65%` | `310.00` |
| `Live` | `Short` | `7.57` | 57,580,000.00 USD | 7,860,000.00 USD | 0.00 USD | `+86.39%` | `1,039,604.60` |
| `Live` | `Short` | `7.58` | 57,590,000.00 USD | 2,630.00 USD | 0.00 USD | `+86.64%` | `347.20` |
| `Live` | `Short` | `7.58` | 57,590,000.00 USD | 6,030.00 USD | 0.00 USD | `+86.88%` | `794.40` |
| `Live` | `Short` | `7.62` | 57,620,000.00 USD | 27,330.00 USD | 0.00 USD | `+87.62%` | `3,588.70` |
| `Live` | `Short` | `7.63` | 57,640,000.00 USD | 19,210.00 USD | 0.00 USD | `+88.11%` | `2,516.10` |
| `Live` | `Short` | `7.67` | 57,660,000.00 USD | 15,390.00 USD | 0.00 USD | `+88.85%` | `2,008.30` |
| `Live` | `Short` | `7.72` | 61,760,000.00 USD | 4,100,000.00 USD | 0.00 USD | `+90.33%` | `531,033.60` |
| `Live` | `Short` | `7.74` | 61,760,000.00 USD | 505.87 USD | 0.00 USD | `+90.58%` | `65.40` |
| `Live` | `Short` | `7.75` | 61,860,000.00 USD | 105,820.00 USD | 0.00 USD | `+90.82%` | `13,662.50` |
| `Live` | `Short` | `7.79` | 61,900,000.00 USD | 33,540.00 USD | 0.00 USD | `+91.81%` | `4,308.50` |
| `Live` | `Short` | `7.79` | 62,890,000.00 USD | 997,510.00 USD | 0.00 USD | `+92.06%` | `127,967.40` |
| `Live` | `Short` | `7.87` | 62,900,000.00 USD | 2,980.00 USD | 0.00 USD | `+93.78%` | `378.70` |
| `Live` | `Short` | `7.88` | 62,900,000.00 USD | 505.58 USD | 0.00 USD | `+94.03%` | `64.20` |
| `Live` | `Short` | `7.92` | 62,900,000.00 USD | 1,800.00 USD | 0.00 USD | `+95.26%` | `226.70` |
| `Live` | `Short` | `7.95` | 62,910,000.00 USD | 6,120.00 USD | 0.00 USD | `+95.75%` | `769.80` |
| `Live` | `Short` | `7.96` | 63,040,000.00 USD | 134,410.00 USD | 0.00 USD | `+96.25%` | `16,875.20` |
| `Live` | `Short` | `7.99` | 63,040,000.00 USD | 399.25 USD | 0.00 USD | `+96.74%` | `50.00` |
| `Live` | `Short` | `8.03` | 63,480,000.00 USD | 435,420.00 USD | 0.00 USD | `+97.72%` | `54,257.40` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 2,600,000.00 USD | 0.00 USD | 585.51 USD | `-75.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,600,000.00 USD | 0.00 USD | 339.82 USD | `-74.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,600,000.00 USD | 0.00 USD | 196.58 USD | `-70.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 2,600,000.00 USD | 0.00 USD | 331.54 USD | `-66.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 2,600,000.00 USD | 0.00 USD | 345.25 USD | `-66.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 2,600,000.00 USD | 0.00 USD | 5,640.00 USD | `-66.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 2,590,000.00 USD | 0.00 USD | 997.29 USD | `-65.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 2,590,000.00 USD | 0.00 USD | 139.83 USD | `-62.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 2,590,000.00 USD | 0.00 USD | 113.28 USD | `-62.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 2,590,000.00 USD | 0.00 USD | 4,000.00 USD | `-61.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 2,590,000.00 USD | 0.00 USD | 324.22 USD | `-61.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 2,590,000.00 USD | 0.00 USD | 4,590.00 USD | `-60.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 2,580,000.00 USD | 0.00 USD | 739.67 USD | `-60.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 2,580,000.00 USD | 0.00 USD | 1,740.00 USD | `-59.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 2,580,000.00 USD | 0.00 USD | 6,260.00 USD | `-59.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 2,580,000.00 USD | 0.00 USD | 345.40 USD | `-59.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 2,580,000.00 USD | 0.00 USD | 167.50 USD | `-58.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 2,580,000.00 USD | 0.00 USD | 669.02 USD | `-58.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 2,570,000.00 USD | 0.00 USD | 105.88 USD | `-57.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 2,570,000.00 USD | 0.00 USD | 172.50 USD | `-57.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 2,570,000.00 USD | 0.00 USD | 10,650.00 USD | `-56.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 2,560,000.00 USD | 0.00 USD | 722.00 USD | `-55.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 2,560,000.00 USD | 0.00 USD | 259.00 USD | `-55.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 2,560,000.00 USD | 0.00 USD | 103.84 USD | `-55.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 2,560,000.00 USD | 0.00 USD | 109.00 USD | `-54.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 2,560,000.00 USD | 0.00 USD | 222.19 USD | `-53.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 2,560,000.00 USD | 0.00 USD | 10,280.00 USD | `-53.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 2,550,000.00 USD | 0.00 USD | 558.36 USD | `-53.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 2,550,000.00 USD | 0.00 USD | 1,520.00 USD | `-52.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 2,550,000.00 USD | 0.00 USD | 222.14 USD | `-52.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 2,550,000.00 USD | 0.00 USD | 279.50 USD | `-52.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 2,550,000.00 USD | 0.00 USD | 197.50 USD | `-51.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,550,000.00 USD | 0.00 USD | 935.66 USD | `-50.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,550,000.00 USD | 0.00 USD | 18,860.00 USD | `-50.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,530,000.00 USD | 0.00 USD | 3,020.00 USD | `-50.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,530,000.00 USD | 0.00 USD | 214.52 USD | `-49.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,530,000.00 USD | 0.00 USD | 1,200.00 USD | `-49.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,520,000.00 USD | 0.00 USD | 578.41 USD | `-49.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,520,000.00 USD | 0.00 USD | 18,070.00 USD | `-48.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,510,000.00 USD | 0.00 USD | 108.62 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,510,000.00 USD | 0.00 USD | 107.23 USD | `-47.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,510,000.00 USD | 0.00 USD | 1,590.00 USD | `-47.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,500,000.00 USD | 0.00 USD | 5,830.00 USD | `-47.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,500,000.00 USD | 0.00 USD | 310.32 USD | `-46.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,500,000.00 USD | 0.00 USD | 1,170.00 USD | `-46.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,500,000.00 USD | 0.00 USD | 576.18 USD | `-46.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,500,000.00 USD | 0.00 USD | 295.67 USD | `-45.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,500,000.00 USD | 0.00 USD | 1,430.00 USD | `-45.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,490,000.00 USD | 0.00 USD | 812.68 USD | `-45.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,490,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,490,000.00 USD | 0.00 USD | 106.16 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,490,000.00 USD | 0.00 USD | 6,270.00 USD | `-44.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,490,000.00 USD | 0.00 USD | 478.06 USD | `-44.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,490,000.00 USD | 0.00 USD | 540.88 USD | `-44.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,480,000.00 USD | 0.00 USD | 867.46 USD | `-43.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,480,000.00 USD | 0.00 USD | 759.76 USD | `-43.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,480,000.00 USD | 0.00 USD | 11,060.00 USD | `-43.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,470,000.00 USD | 0.00 USD | 3,690.00 USD | `-43.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,470,000.00 USD | 0.00 USD | 722.15 USD | `-42.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,470,000.00 USD | 0.00 USD | 467.00 USD | `-42.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,470,000.00 USD | 0.00 USD | 506.75 USD | `-42.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,470,000.00 USD | 0.00 USD | 214.27 USD | `-41.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,470,000.00 USD | 0.00 USD | 428.69 USD | `-41.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,470,000.00 USD | 0.00 USD | 322.45 USD | `-41.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,470,000.00 USD | 0.00 USD | 108.25 USD | `-40.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,470,000.00 USD | 0.00 USD | 3,900.00 USD | `-40.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,460,000.00 USD | 0.00 USD | 799.04 USD | `-40.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,460,000.00 USD | 0.00 USD | 6,830.00 USD | `-40.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,450,000.00 USD | 0.00 USD | 137.16 USD | `-39.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,450,000.00 USD | 0.00 USD | 504.41 USD | `-39.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,450,000.00 USD | 0.00 USD | 963.93 USD | `-38.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,450,000.00 USD | 0.00 USD | 6,690.00 USD | `-38.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,450,000.00 USD | 0.00 USD | 541.98 USD | `-38.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,450,000.00 USD | 0.00 USD | 108.75 USD | `-37.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,450,000.00 USD | 0.00 USD | 766.55 USD | `-37.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,440,000.00 USD | 0.00 USD | 7,110.00 USD | `-37.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,440,000.00 USD | 0.00 USD | 1,100.00 USD | `-36.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,440,000.00 USD | 0.00 USD | 100.04 USD | `-36.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,440,000.00 USD | 0.00 USD | 1,220.00 USD | `-35.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,430,000.00 USD | 0.00 USD | 5,090.00 USD | `-35.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,430,000.00 USD | 0.00 USD | 226.57 USD | `-34.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,430,000.00 USD | 0.00 USD | 104.98 USD | `-33.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,430,000.00 USD | 0.00 USD | 889.89 USD | `-33.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,430,000.00 USD | 0.00 USD | 7,270.00 USD | `-33.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,420,000.00 USD | 0.00 USD | 107.21 USD | `-32.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,420,000.00 USD | 0.00 USD | 197.37 USD | `-32.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,420,000.00 USD | 0.00 USD | 8,110.00 USD | `-32.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,410,000.00 USD | 0.00 USD | 108.39 USD | `-31.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,410,000.00 USD | 0.00 USD | 435.95 USD | `-31.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,410,000.00 USD | 0.00 USD | 217.23 USD | `-31.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,410,000.00 USD | 0.00 USD | 437.98 USD | `-31.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,410,000.00 USD | 0.00 USD | 2,720.00 USD | `-30.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,410,000.00 USD | 0.00 USD | 8,380.00 USD | `-30.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,400,000.00 USD | 0.00 USD | 283.50 USD | `-30.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,400,000.00 USD | 0.00 USD | 109.53 USD | `-29.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,400,000.00 USD | 0.00 USD | 1,230.00 USD | `-29.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,400,000.00 USD | 0.00 USD | 1,960.00 USD | `-29.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,400,000.00 USD | 0.00 USD | 746.06 USD | `-28.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,400,000.00 USD | 0.00 USD | 2,900.00 USD | `-28.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,390,000.00 USD | 0.00 USD | 4,870.00 USD | `-28.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,390,000.00 USD | 0.00 USD | 1,700.00 USD | `-27.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,390,000.00 USD | 0.00 USD | 15,370.00 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,370,000.00 USD | 0.00 USD | 738.75 USD | `-27.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,370,000.00 USD | 0.00 USD | 523.32 USD | `-26.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,370,000.00 USD | 0.00 USD | 4,470.00 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,370,000.00 USD | 0.00 USD | 22,640.00 USD | `-25.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,340,000.00 USD | 0.00 USD | 1,020.00 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,340,000.00 USD | 0.00 USD | 345.76 USD | `-25.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,340,000.00 USD | 0.00 USD | 214.57 USD | `-25.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,340,000.00 USD | 0.00 USD | 249.08 USD | `-24.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,340,000.00 USD | 0.00 USD | 305.50 USD | `-24.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,340,000.00 USD | 0.00 USD | 109.42 USD | `-24.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 2,340,000.00 USD | 0.00 USD | 721.58 USD | `-23.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,340,000.00 USD | 0.00 USD | 9,300.00 USD | `-23.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,330,000.00 USD | 0.00 USD | 8,570.00 USD | `-23.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,320,000.00 USD | 0.00 USD | 104.69 USD | `-23.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,320,000.00 USD | 0.00 USD | 315.69 USD | `-22.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,320,000.00 USD | 0.00 USD | 17,510.00 USD | `-22.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,300,000.00 USD | 0.00 USD | 258,640.00 USD | `-22.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,050,000.00 USD | 0.00 USD | 4,210.00 USD | `-22.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,040,000.00 USD | 0.00 USD | 1,030.00 USD | `-21.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,040,000.00 USD | 0.00 USD | 218.81 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,040,000.00 USD | 0.00 USD | 25,410.00 USD | `-21.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,010,000.00 USD | 0.00 USD | 144.67 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,010,000.00 USD | 0.00 USD | 27,380.00 USD | `-20.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 1,990,000.00 USD | 0.00 USD | 1,840.00 USD | `-19.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 1,990,000.00 USD | 0.00 USD | 104.81 USD | `-19.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 1,990,000.00 USD | 0.00 USD | 200.10 USD | `-19.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 1,990,000.00 USD | 0.00 USD | 1,480.00 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 1,980,000.00 USD | 0.00 USD | 1,870.00 USD | `-18.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 1,980,000.00 USD | 0.00 USD | 18,240.00 USD | `-18.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 1,960,000.00 USD | 0.00 USD | 240.67 USD | `-18.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 1,960,000.00 USD | 0.00 USD | 465.50 USD | `-18.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 1,960,000.00 USD | 0.00 USD | 6,590.00 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 1,960,000.00 USD | 0.00 USD | 505.76 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 1,960,000.00 USD | 0.00 USD | 73,220.00 USD | `-17.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 1,880,000.00 USD | 0.00 USD | 19,600.00 USD | `-16.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 1,860,000.00 USD | 0.00 USD | 8,490.00 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 1,850,000.00 USD | 0.00 USD | 111,650.00 USD | `-16.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,740,000.00 USD | 0.00 USD | 421.41 USD | `-15.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,740,000.00 USD | 0.00 USD | 506.22 USD | `-15.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,740,000.00 USD | 0.00 USD | 171.75 USD | `-15.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,740,000.00 USD | 0.00 USD | 2,550.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,740,000.00 USD | 0.00 USD | 3,060.00 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,740,000.00 USD | 0.00 USD | 344.07 USD | `-14.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 1,740,000.00 USD | 0.00 USD | 156.83 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,740,000.00 USD | 0.00 USD | 894.72 USD | `-13.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,730,000.00 USD | 0.00 USD | 67,780.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,670,000.00 USD | 0.00 USD | 21,320.00 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,650,000.00 USD | 0.00 USD | 3,700.00 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,640,000.00 USD | 0.00 USD | 16,250.00 USD | `-12.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,630,000.00 USD | 0.00 USD | 5,130.00 USD | `-12.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,620,000.00 USD | 0.00 USD | 17,420.00 USD | `-12.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,600,000.00 USD | 0.00 USD | 18,440.00 USD | `-12.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,580,000.00 USD | 0.00 USD | 78,170.00 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,510,000.00 USD | 0.00 USD | 1,250.00 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,510,000.00 USD | 0.00 USD | 331.46 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,500,000.00 USD | 0.00 USD | 15,710.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,490,000.00 USD | 0.00 USD | 632.99 USD | `-10.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,490,000.00 USD | 0.00 USD | 172.19 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,490,000.00 USD | 0.00 USD | 1,410.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,490,000.00 USD | 0.00 USD | 179.33 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,490,000.00 USD | 0.00 USD | 4,080.00 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,480,000.00 USD | 0.00 USD | 4,070.00 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,480,000.00 USD | 0.00 USD | 367.50 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,480,000.00 USD | 0.00 USD | 34,720.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,440,000.00 USD | 0.00 USD | 4,370.00 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,440,000.00 USD | 0.00 USD | 234,410.00 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,200,000.00 USD | 0.00 USD | 6,300.00 USD | `-8.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,200,000.00 USD | 0.00 USD | 2,490.00 USD | `-8.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,200,000.00 USD | 0.00 USD | 32,040.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,160,000.00 USD | 0.00 USD | 28,820.00 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,140,000.00 USD | 0.00 USD | 14,490.00 USD | `-7.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,120,000.00 USD | 0.00 USD | 250,790.00 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 869,860.00 USD | 0.00 USD | 1,510.00 USD | `-6.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 868,350.00 USD | 0.00 USD | 183.19 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 868,170.00 USD | 0.00 USD | 181,010.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 687,150.00 USD | 0.00 USD | 8,720.00 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 678,440.00 USD | 0.00 USD | 22,340.00 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 656,090.00 USD | 0.00 USD | 36,060.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 620,040.00 USD | 0.00 USD | 7,990.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 612,040.00 USD | 0.00 USD | 43,060.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 568,990.00 USD | 0.00 USD | 5,640.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 563,350.00 USD | 0.00 USD | 8,620.00 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 554,730.00 USD | 0.00 USD | 161,220.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 393,510.00 USD | 0.00 USD | 27,540.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 365,970.00 USD | 0.00 USD | 7,770.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 358,200.00 USD | 0.00 USD | 48,840.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 309,360.00 USD | 0.00 USD | 441.22 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 308,920.00 USD | 0.00 USD | 5,190.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 303,720.00 USD | 0.00 USD | 1,180.00 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 302,550.00 USD | 0.00 USD | 4,830.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 297,720.00 USD | 0.00 USD | 3,600.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 294,120.00 USD | 0.00 USD | 31,820.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 262,290.00 USD | 0.00 USD | 317.60 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 261,980.00 USD | 0.00 USD | 786.24 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 261,190.00 USD | 0.00 USD | 6,000.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 255,190.00 USD | 0.00 USD | 192,170.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 63,020.00 USD | 0.00 USD | 20,520.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 42,500.00 USD | 0.00 USD | 9,590.00 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 32,910.00 USD | 0.00 USD | 15,530.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 17,380.00 USD | 0.00 USD | 1,780.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 15,600.00 USD | 0.00 USD | 15,600.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.07` | 113.41 USD | 113.41 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.08` | 1,400.00 USD | 1,290.00 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.08` | 40,000.00 USD | 38,600.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.09` | 81,980.00 USD | 41,980.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.11` | 82,130.00 USD | 149.83 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 141,100.00 USD | 58,980.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 143,120.00 USD | 2,010.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.13` | 144,240.00 USD | 1,120.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.14` | 147,520.00 USD | 3,280.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.16` | 149,240.00 USD | 1,730.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 234,080.00 USD | 84,840.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 236,140.00 USD | 2,060.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 236,700.00 USD | 557.02 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 608,690.00 USD | 371,990.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 795,790.00 USD | 187,090.00 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 796,480.00 USD | 687.04 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 796,610.00 USD | 131.82 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 797,000.00 USD | 390.47 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 800,680.00 USD | 3,680.00 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 833,920.00 USD | 33,240.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 836,090.00 USD | 2,180.00 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 857,130.00 USD | 21,040.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 862,560.00 USD | 5,430.00 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 893,970.00 USD | 31,410.00 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 921,080.00 USD | 27,110.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 921,350.00 USD | 269.26 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 923,770.00 USD | 2,420.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 925,300.00 USD | 1,540.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 942,680.00 USD | 17,380.00 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 942,800.00 USD | 120.63 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 943,270.00 USD | 464.00 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 968,770.00 USD | 25,510.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 1,040,000.00 USD | 71,900.00 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 1,080,000.00 USD | 42,310.00 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 1,510,000.00 USD | 422,530.00 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,520,000.00 USD | 13,130.00 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,520,000.00 USD | 4,090.00 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 1,520,000.00 USD | 301.58 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 1,520,000.00 USD | 524.07 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,590,000.00 USD | 62,580.00 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,590,000.00 USD | 2,470.00 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 1,590,000.00 USD | 375.90 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 1,590,000.00 USD | 133.20 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,620,000.00 USD | 29,550.00 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,640,000.00 USD | 20,580.00 USD | 0.00 USD | `+11.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 1,650,000.00 USD | 13,100.00 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 1,700,000.00 USD | 52,300.00 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,710,000.00 USD | 3,390.00 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,710,000.00 USD | 3,180.00 USD | 0.00 USD | `+11.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,710,000.00 USD | 1,190.00 USD | 0.00 USD | `+12.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,710,000.00 USD | 227.79 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,710,000.00 USD | 2,030.00 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,720,000.00 USD | 1,150.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,730,000.00 USD | 17,590.00 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,760,000.00 USD | 24,120.00 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,760,000.00 USD | 289.82 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,760,000.00 USD | 3,670.00 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,760,000.00 USD | 1,100.00 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,770,000.00 USD | 7,530.00 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,810,000.00 USD | 44,520.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,830,000.00 USD | 16,750.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,830,000.00 USD | 617.10 USD | 0.00 USD | `+15.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,850,000.00 USD | 15,710.00 USD | 0.00 USD | `+15.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,850,000.00 USD | 152.12 USD | 0.00 USD | `+15.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,210,000.00 USD | 357,870.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,420,000.00 USD | 218,120.00 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,430,000.00 USD | 2,650.00 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,510,000.00 USD | 84,180.00 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,520,000.00 USD | 6,160.00 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,540,000.00 USD | 27,130.00 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,560,000.00 USD | 13,030.00 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,560,000.00 USD | 2,640.00 USD | 0.00 USD | `+17.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,390,000.00 USD | 832,330.00 USD | 0.00 USD | `+17.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,390,000.00 USD | 559.58 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,570,000.00 USD | 177,030.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,590,000.00 USD | 20,720.00 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,600,000.00 USD | 8,540.00 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,600,000.00 USD | 283.33 USD | 0.00 USD | `+19.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,610,000.00 USD | 11,760.00 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,640,000.00 USD | 24,370.00 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,660,000.00 USD | 22,170.00 USD | 0.00 USD | `+19.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,670,000.00 USD | 10,400.00 USD | 0.00 USD | `+20.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,690,000.00 USD | 19,890.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,690,000.00 USD | 4,060.00 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,820,000.00 USD | 125,180.00 USD | 0.00 USD | `+20.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,820,000.00 USD | 156.30 USD | 0.00 USD | `+21.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,830,000.00 USD | 13,180.00 USD | 0.00 USD | `+21.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,830,000.00 USD | 4,420.00 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,830,000.00 USD | 313.51 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,840,000.00 USD | 5,070.00 USD | 0.00 USD | `+22.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,890,000.00 USD | 47,350.00 USD | 0.00 USD | `+22.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,890,000.00 USD | 187.06 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,980,000.00 USD | 92,570.00 USD | 0.00 USD | `+22.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,980,000.00 USD | 2,540.00 USD | 0.00 USD | `+23.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 4,020,000.00 USD | 40,150.00 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 4,050,000.00 USD | 25,080.00 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 4,050,000.00 USD | 5,030.00 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 4,070,000.00 USD | 19,640.00 USD | 0.00 USD | `+24.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 4,070,000.00 USD | 120.58 USD | 0.00 USD | `+24.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 4,090,000.00 USD | 14,440.00 USD | 0.00 USD | `+24.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 4,090,000.00 USD | 6,090.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,180,000.00 USD | 87,290.00 USD | 0.00 USD | `+25.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,190,000.00 USD | 5,640.00 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,190,000.00 USD | 178.33 USD | 0.00 USD | `+25.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,250,000.00 USD | 68,210.00 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,270,000.00 USD | 17,900.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,270,000.00 USD | 179.38 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,270,000.00 USD | 179.72 USD | 0.00 USD | `+26.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,270,000.00 USD | 217.63 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,270,000.00 USD | 493.85 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,270,000.00 USD | 575.38 USD | 0.00 USD | `+27.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,270,000.00 USD | 327.58 USD | 0.00 USD | `+27.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,270,000.00 USD | 163.85 USD | 0.00 USD | `+27.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,400,000.00 USD | 120,930.00 USD | 0.00 USD | `+28.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,430,000.00 USD | 38,230.00 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,440,000.00 USD | 1,710.00 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,440,000.00 USD | 432.63 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,440,000.00 USD | 2,620.00 USD | 0.00 USD | `+28.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,440,000.00 USD | 537.61 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,860,000.00 USD | 420,400.00 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,860,000.00 USD | 278.52 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,860,000.00 USD | 589.22 USD | 0.00 USD | `+29.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,860,000.00 USD | 733.03 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,860,000.00 USD | 423.60 USD | 0.00 USD | `+30.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,870,000.00 USD | 10,930.00 USD | 0.00 USD | `+30.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,870,000.00 USD | 381.09 USD | 0.00 USD | `+30.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,870,000.00 USD | 961.16 USD | 0.00 USD | `+31.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,880,000.00 USD | 1,570.00 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,880,000.00 USD | 5,650.00 USD | 0.00 USD | `+31.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,880,000.00 USD | 160.11 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,880,000.00 USD | 225.33 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,880,000.00 USD | 438.60 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,890,000.00 USD | 6,800.00 USD | 0.00 USD | `+32.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,930,000.00 USD | 40,880.00 USD | 0.00 USD | `+32.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,950,000.00 USD | 19,950.00 USD | 0.00 USD | `+33.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,950,000.00 USD | 270.75 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,950,000.00 USD | 639.61 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,950,000.00 USD | 1,710.00 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,960,000.00 USD | 12,600.00 USD | 0.00 USD | `+34.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,970,000.00 USD | 4,190.00 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,160,000.00 USD | 192,640.00 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 5,190,000.00 USD | 30,110.00 USD | 0.00 USD | `+34.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 5,230,000.00 USD | 38,920.00 USD | 0.00 USD | `+35.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,230,000.00 USD | 1,180.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,200,000.00 USD | 968,610.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,210,000.00 USD | 5,600.00 USD | 0.00 USD | `+35.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,230,000.00 USD | 19,110.00 USD | 0.00 USD | `+36.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,240,000.00 USD | 18,790.00 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,300,000.00 USD | 58,030.00 USD | 0.00 USD | `+36.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,350,000.00 USD | 46,110.00 USD | 0.00 USD | `+36.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,360,000.00 USD | 14,320.00 USD | 0.00 USD | `+37.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,370,000.00 USD | 11,740.00 USD | 0.00 USD | `+37.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,390,000.00 USD | 20,540.00 USD | 0.00 USD | `+37.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,390,000.00 USD | 384.94 USD | 0.00 USD | `+37.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,400,000.00 USD | 573.39 USD | 0.00 USD | `+38.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,400,000.00 USD | 347.06 USD | 0.00 USD | `+38.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,400,000.00 USD | 581.53 USD | 0.00 USD | `+38.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,400,000.00 USD | 491.11 USD | 0.00 USD | `+39.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,400,000.00 USD | 3,290.00 USD | 0.00 USD | `+39.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,400,000.00 USD | 281.55 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,410,000.00 USD | 6,590.00 USD | 0.00 USD | `+39.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 6,410,000.00 USD | 235.93 USD | 0.00 USD | `+40.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,410,000.00 USD | 5,860.00 USD | 0.00 USD | `+40.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,520,000.00 USD | 103,470.00 USD | 0.00 USD | `+40.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,520,000.00 USD | 705.23 USD | 0.00 USD | `+40.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,520,000.00 USD | 5,720.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,520,000.00 USD | 139.03 USD | 0.00 USD | `+41.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,530,000.00 USD | 2,450.00 USD | 0.00 USD | `+41.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,530,000.00 USD | 1,850.00 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,530,000.00 USD | 286.94 USD | 0.00 USD | `+42.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,530,000.00 USD | 7,120.00 USD | 0.00 USD | `+43.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,540,000.00 USD | 329.13 USD | 0.00 USD | `+43.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,540,000.00 USD | 1,970.00 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,540,000.00 USD | 1,020.00 USD | 0.00 USD | `+43.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,540,000.00 USD | 1,150.00 USD | 0.00 USD | `+44.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,540,000.00 USD | 1,190.00 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,540,000.00 USD | 1,770.00 USD | 0.00 USD | `+44.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,550,000.00 USD | 3,450.00 USD | 0.00 USD | `+44.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,550,000.00 USD | 345.45 USD | 0.00 USD | `+45.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,610,000.00 USD | 65,320.00 USD | 0.00 USD | `+45.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,610,000.00 USD | 2,510.00 USD | 0.00 USD | `+45.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,620,000.00 USD | 1,020.00 USD | 0.00 USD | `+45.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,770,000.00 USD | 153,150.00 USD | 0.00 USD | `+46.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,790,000.00 USD | 26,180.00 USD | 0.00 USD | `+46.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,800,000.00 USD | 5,440.00 USD | 0.00 USD | `+46.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,810,000.00 USD | 8,940.00 USD | 0.00 USD | `+47.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,930,000.00 USD | 119,340.00 USD | 0.00 USD | `+47.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,930,000.00 USD | 3,000.00 USD | 0.00 USD | `+47.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,130,000.00 USD | 200,290.00 USD | 0.00 USD | `+47.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,150,000.00 USD | 13,710.00 USD | 0.00 USD | `+48.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,240,000.00 USD | 90,380.00 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,240,000.00 USD | 2,170.00 USD | 0.00 USD | `+48.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,240,000.00 USD | 3,300.00 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,240,000.00 USD | 1,040.00 USD | 0.00 USD | `+49.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,240,000.00 USD | 425.76 USD | 0.00 USD | `+49.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,240,000.00 USD | 2,030.00 USD | 0.00 USD | `+49.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,250,000.00 USD | 4,120.00 USD | 0.00 USD | `+49.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,250,000.00 USD | 2,000.00 USD | 0.00 USD | `+50.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,310,000.00 USD | 61,050.00 USD | 0.00 USD | `+50.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,310,000.00 USD | 1,610.00 USD | 0.00 USD | `+50.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,310,000.00 USD | 1,200.00 USD | 0.00 USD | `+51.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,310,000.00 USD | 420.32 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,320,000.00 USD | 1,940.00 USD | 0.00 USD | `+51.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,320,000.00 USD | 4,010.00 USD | 0.00 USD | `+52.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,320,000.00 USD | 3,960.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,390,000.00 USD | 66,060.00 USD | 0.00 USD | `+52.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,390,000.00 USD | 1,890.00 USD | 0.00 USD | `+53.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,390,000.00 USD | 195.46 USD | 0.00 USD | `+53.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,390,000.00 USD | 1,540.00 USD | 0.00 USD | `+53.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 7,390,000.00 USD | 116.16 USD | 0.00 USD | `+53.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,400,000.00 USD | 7,310.00 USD | 0.00 USD | `+55.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,400,000.00 USD | 310.70 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,400,000.00 USD | 325.62 USD | 0.00 USD | `+56.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,400,000.00 USD | 1,760.00 USD | 0.00 USD | `+56.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,410,000.00 USD | 3,230.00 USD | 0.00 USD | `+57.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,410,000.00 USD | 5,120.00 USD | 0.00 USD | `+57.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,410,000.00 USD | 613.26 USD | 0.00 USD | `+58.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,410,000.00 USD | 1,310.00 USD | 0.00 USD | `+60.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,450,000.00 USD | 30,990.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,450,000.00 USD | 104.24 USD | 0.00 USD | `+60.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,460,000.00 USD | 13,580.00 USD | 0.00 USD | `+61.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,460,000.00 USD | 1,630.00 USD | 0.00 USD | `+62.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 7,460,000.00 USD | 1,370.00 USD | 0.00 USD | `+62.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,470,000.00 USD | 5,400.00 USD | 0.00 USD | `+62.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,470,000.00 USD | 1,620.00 USD | 0.00 USD | `+62.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,470,000.00 USD | 3,220.00 USD | 0.00 USD | `+63.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,470,000.00 USD | 450.55 USD | 0.00 USD | `+64.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,480,000.00 USD | 3,060.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,480,000.00 USD | 3,070.00 USD | 0.00 USD | `+65.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,480,000.00 USD | 3,120.00 USD | 0.00 USD | `+65.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,480,000.00 USD | 1,550.00 USD | 0.00 USD | `+66.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,490,000.00 USD | 3,080.00 USD | 0.00 USD | `+66.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,490,000.00 USD | 647.56 USD | 0.00 USD | `+67.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,490,000.00 USD | 1,420.00 USD | 0.00 USD | `+67.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,490,000.00 USD | 2,130.00 USD | 0.00 USD | `+67.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,500,000.00 USD | 6,870.00 USD | 0.00 USD | `+68.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,500,000.00 USD | 342.25 USD | 0.00 USD | `+68.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,500,000.00 USD | 2,990.00 USD | 0.00 USD | `+69.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,500,000.00 USD | 2,970.00 USD | 0.00 USD | `+69.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,500,000.00 USD | 324.54 USD | 0.00 USD | `+70.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,500,000.00 USD | 504.21 USD | 0.00 USD | `+71.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,510,000.00 USD | 166.00 USD | 0.00 USD | `+71.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,510,000.00 USD | 4,190.00 USD | 0.00 USD | `+72.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,520,000.00 USD | 12,970.00 USD | 0.00 USD | `+72.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,530,000.00 USD | 2,860.00 USD | 0.00 USD | `+73.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,530,000.00 USD | 264.31 USD | 0.00 USD | `+75.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,530,000.00 USD | 599.34 USD | 0.00 USD | `+75.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,530,000.00 USD | 193.19 USD | 0.00 USD | `+76.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,530,000.00 USD | 3,950.00 USD | 0.00 USD | `+77.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,530,000.00 USD | 1,940.00 USD | 0.00 USD | `+77.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,690,000.00 USD | 160,550.00 USD | 0.00 USD | `+78.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,690,000.00 USD | 1,290.00 USD | 0.00 USD | `+79.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,700,000.00 USD | 1,180.00 USD | 0.00 USD | `+80.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,700,000.00 USD | 630.05 USD | 0.00 USD | `+82.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,700,000.00 USD | 1,410.00 USD | 0.00 USD | `+82.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,700,000.00 USD | 2,610.00 USD | 0.00 USD | `+82.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,710,000.00 USD | 7,630.00 USD | 0.00 USD | `+84.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,710,000.00 USD | 4,640.00 USD | 0.00 USD | `+86.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,710,000.00 USD | 371.88 USD | 0.00 USD | `+87.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,710,000.00 USD | 2,510.00 USD | 0.00 USD | `+87.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,720,000.00 USD | 380.68 USD | 0.00 USD | `+89.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,720,000.00 USD | 1,490.00 USD | 0.00 USD | `+91.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,720,000.00 USD | 1,470.00 USD | 0.00 USD | `+91.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,730,000.00 USD | 11,170.00 USD | 0.00 USD | `+92.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,760,000.00 USD | 34,360.00 USD | 0.00 USD | `+92.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,760,000.00 USD | 253.21 USD | 0.00 USD | `+92.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,760,000.00 USD | 100.29 USD | 0.00 USD | `+93.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,770,000.00 USD | 10,610.00 USD | 0.00 USD | `+96.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,780,000.00 USD | 309.43 USD | 0.00 USD | `+96.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,810,000.00 USD | 36,300.00 USD | 0.00 USD | `+97.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,890,000.00 USD | 81,310.00 USD | 0.00 USD | `+97.72%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.59` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD |
| `7D` | `3.60` | 11,920,000.00 USD | 0.00 USD | 11,920,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `1D` | `3.63` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,610.00 USD |
| `7D` | `3.63` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `1D` | `3.64` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 152.80 USD | 5,040.00 USD | 0.00 USD |
| `7D` | `3.64` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD |
| `1D` | `3.65` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 386.30 USD | 0.00 USD | 13.37 USD |
| `7D` | `3.65` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD |
| `1D` | `3.66` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.66` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD |
| `1D` | `3.67` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,520.00 USD |
| `7D` | `3.67` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD |
| `1D` | `3.68` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 216.77 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.69` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 23,960.00 USD | 0.00 USD | 281.19 USD |
| `7D` | `3.69` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `1D` | `3.70` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,010.00 USD |
| `7D` | `3.70` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `1D` | `3.71` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 430.40 USD | 0.00 USD | 522.93 USD |
| `7D` | `3.71` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD |
| `1D` | `3.72` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD |
| `7D` | `3.72` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `1D` | `3.73` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD |
| `7D` | `3.73` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,360.00 USD |
| `7D` | `3.74` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD |
| `1D` | `3.75` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3.75` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD |
| `1D` | `3.76` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD |
| `7D` | `3.76` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `1D` | `3.77` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD |
| `7D` | `3.77` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD |
| `1D` | `3.78` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 106.91 USD | 4,490.00 USD | 29,810.00 USD |
| `7D` | `3.78` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 472.79 USD | 0.00 USD | 176.51 USD |
| `7D` | `3.79` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD |
| `1D` | `3.80` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 1,270.00 USD | 0.00 USD | 1,720.00 USD |
| `7D` | `3.80` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD |
| `1D` | `3.81` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 54,290.00 USD | 0.00 USD | 13,100.00 USD |
| `7D` | `3.81` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD |
| `1D` | `3.82` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 487.48 USD | 11,960.00 USD | 0.00 USD |
| `7D` | `3.82` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 1,150.00 USD | 18,900.00 USD | 17,280.00 USD |
| `7D` | `3.83` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD |
| `1D` | `3.84` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 784.00 USD |
| `7D` | `3.84` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.85` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD |
| `7D` | `3.85` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `3.86` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,290.00 USD |
| `7D` | `3.86` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 1,690.00 USD | 11,800.00 USD | 845.92 USD |
| `7D` | `3.87` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD |
| `1D` | `3.88` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 106,680.00 USD | 6,860.00 USD | 39,950.00 USD |
| `7D` | `3.88` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD |
| `1D` | `3.89` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 113,490.00 USD | 37,150.00 USD | 23,350.00 USD |
| `7D` | `3.89` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD |
| `1D` | `3.90` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 31,410.00 USD | 10,910.00 USD | 21,360.00 USD |
| `7D` | `3.90` | 9,280,000.00 USD | 0.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD |
| `1D` | `3.91` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 32,140.00 USD | 35,760.00 USD | 39,260.00 USD |
| `7D` | `3.91` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 148,140.00 USD | 26,030.00 USD | 33,330.00 USD |
| `7D` | `3.92` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD |
| `1D` | `3.93` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 29,900.00 USD | 38,510.00 USD |
| `7D` | `3.93` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD |
| `1D` | `3.94` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 96,340.00 USD | 14,940.00 USD | 20,530.00 USD |
| `7D` | `3.94` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD |
| `1D` | `3.95` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 95,940.00 USD | 15,880.00 USD | 95,070.00 USD |
| `7D` | `3.95` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD |
| `1D` | `3.96` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,690.00 USD |
| `7D` | `3.96` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD |
| `1D` | `3.97` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 190,720.00 USD | 66,010.00 USD | 102,960.00 USD |
| `7D` | `3.97` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD |
| `1D` | `3.98` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,880.00 USD |
| `7D` | `3.98` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD |
| `1D` | `3.99` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 413,960.00 USD | 106,190.00 USD | 138,330.00 USD |
| `7D` | `3.99` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD |
| `1D` | `4.00` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,490.00 USD |
| `7D` | `4.00` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 112,570.00 USD | 72,850.00 USD | 129,520.00 USD |
| `7D` | `4.01` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD |
| `1D` | `4.02` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 243,600.00 USD | 50,310.00 USD | 107,340.00 USD |
| `7D` | `4.02` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD |
| `1D` | `4.03` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 189,730.00 USD | 76,190.00 USD | 266,680.00 USD |
| `7D` | `4.03` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD |
| `1D` | `4.04` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 105,670.00 USD | 48,960.00 USD | 207,560.00 USD |
| `7D` | `4.04` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD |
| `1D` | `4.05` | 898,580.00 USD | 0.00 USD | 898,580.00 USD | 2,370.00 USD | 46,690.00 USD | 95,690.00 USD |
| `7D` | `4.05` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD |
| `1D` | `4.06` | 753,820.00 USD | 0.00 USD | 753,820.00 USD | 0.00 USD | 27,150.00 USD | 125,920.00 USD |
| `7D` | `4.06` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD |
| `1D` | `4.07` | 600,750.00 USD | 0.00 USD | 600,750.00 USD | 0.00 USD | 72,110.00 USD | 22,350.00 USD |
| `7D` | `4.07` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD |
| `1D` | `4.08` | 506,300.00 USD | 0.00 USD | 506,300.00 USD | 506,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.08` | 575,150.00 USD | 0.00 USD | 575,150.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD |
| `7D` | `4.09` | 218,520.00 USD | 0.00 USD | 218,520.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD |
| `7D` | `4.10` | 143,210.00 USD | 143,210.00 USD | 0.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD |
| `7D` | `4.10` | 286,420.00 USD | 286,420.00 USD | 0.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD |
| `1D` | `4.11` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.12` | 309,660.00 USD | 309,660.00 USD | 0.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD |
| `1D` | `4.13` | 471,110.00 USD | 471,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD |
| `1D` | `4.14` | 531,130.00 USD | 531,130.00 USD | 0.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD |
| `1D` | `4.15` | 595,400.00 USD | 595,400.00 USD | 0.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD |
| `1D` | `4.17` | 664,710.00 USD | 664,710.00 USD | 0.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD |
| `1D` | `4.18` | 874,490.00 USD | 874,490.00 USD | 0.00 USD | 192,730.00 USD | 17,040.00 USD | 0.00 USD |
| `1D` | `4.19` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 174,270.00 USD | 20,540.00 USD | 185,170.00 USD |
| `7D` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD |
| `1D` | `4.22` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD |
| `1D` | `4.23` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD |
| `1D` | `4.24` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD |
| `1D` | `4.25` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD |
| `7D` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD |
| `1D` | `4.26` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 92,160.00 USD | 173,320.00 USD | 248.22 USD |
| `7D` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 677,660.00 USD | 34,890.00 USD | 152,200.00 USD |
| `7D` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 305,690.00 USD | 30,410.00 USD | 288,910.00 USD |
| `7D` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD |
| `1D` | `4.29` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 153,130.00 USD | 32,690.00 USD | 161,450.00 USD |
| `7D` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 32,410.00 USD | 45,120.00 USD | 163,210.00 USD |
| `7D` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 304,920.00 USD | 13,580.00 USD | 95,430.00 USD |
| `7D` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD |
| `1D` | `4.32` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 86,850.00 USD | 73,400.00 USD | 18.65 USD |
| `7D` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD |
| `1D` | `4.33` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 255,620.00 USD | 93,880.00 USD | 87,760.00 USD |
| `7D` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 270,720.00 USD | 140,540.00 USD | 114,690.00 USD |
| `7D` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD |
| `1D` | `4.35` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 855.62 USD | 0.00 USD | 84,830.00 USD |
| `7D` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 84,880.00 USD | 12,310.00 USD | 31,110.00 USD |
| `7D` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD |
| `1D` | `4.37` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 52,520.00 USD | 46,860.00 USD | 130,010.00 USD |
| `1D` | `4.38` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD |
| `7D` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 399.48 USD | 17,360.00 USD | 310,880.00 USD |
| `7D` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD |
| `1D` | `4.40` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 288,790.00 USD | 34,040.00 USD | 81,970.00 USD |
| `7D` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD |
| `1D` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 196,820.00 USD | 112,990.00 USD | 65,530.00 USD |
| `7D` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD |
| `7D` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 5,100.00 USD | 49,400.00 USD | 98,670.00 USD |
| `7D` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD |
| `1D` | `4.44` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD |
| `7D` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD |
| `1D` | `4.45` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD |
| `1D` | `4.46` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD |
| `7D` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD |
| `1D` | `4.47` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 210.23 USD | 16,700.00 USD | 18,310.00 USD |
| `7D` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD |
| `7D` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `4.49` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 252,600.00 USD | 155,000.00 USD | 150,280.00 USD |
| `7D` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 361,770.00 USD | 65,710.00 USD | 120,210.00 USD |
| `7D` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD |
| `1D` | `4.51` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 186,860.00 USD | 307,580.00 USD | 312,530.00 USD |
| `7D` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `4.52` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 287,830.00 USD | 92,260.00 USD | 242,880.00 USD |
| `7D` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 487,540.00 USD | 0.00 USD | 279,080.00 USD |
| `7D` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD |
| `1D` | `4.54` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD |
| `7D` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 195,790.00 USD |
| `1D` | `4.56` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD |
| `7D` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 177,440.00 USD | 70,180.00 USD | 67,980.00 USD |
| `7D` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD |
| `1D` | `4.58` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD |
| `7D` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD |
| `7D` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 18,380,000.00 USD | 18,380,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD |
| `7D` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD |
| `7D` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD |
| `1D` | `4.62` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD |
| `7D` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `4.63` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD |
| `7D` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 19,080,000.00 USD | 19,080,000.00 USD | 0.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD |
| `7D` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD |
| `1D` | `4.65` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD |
| `7D` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD |
| `1D` | `4.66` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD |
| `7D` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD |
| `7D` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 22,300,000.00 USD | 22,300,000.00 USD | 0.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD |
| `7D` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 22,800,000.00 USD | 22,800,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 254,150.00 USD |
| `7D` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 23,140,000.00 USD | 23,140,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,310.00 USD |
| `7D` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 359,510.00 USD | 284,360.00 USD | 316,030.00 USD |
| `7D` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `7D` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `7D` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 0.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD |
| `7D` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `7D` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `7D` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD |
| `7D` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `7D` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 0.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD |
| `7D` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `7D` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `7D` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD |
| `7D` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `7D` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `7D` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `7D` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 0.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD |
| `7D` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `7D` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD |
| `7D` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `7D` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `7D` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `7D` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD |
| `7D` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD |
| `7D` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD |
| `7D` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD |
| `7D` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 0.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD |
| `7D` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD |
| `7D` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD |
| `7D` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 0.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD |
| `7D` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 0.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD |
| `7D` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 0.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD |
| `7D` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 0.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD |
| `7D` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 0.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD |
| `7D` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 0.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD |
| `7D` | `5.07` | 60,660,000.00 USD | 60,660,000.00 USD | 0.00 USD | 358,750.00 USD | 137,080.00 USD | 542,550.00 USD |
| `7D` | `5.08` | 61,180,000.00 USD | 61,180,000.00 USD | 0.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD |
| `7D` | `5.09` | 61,720,000.00 USD | 61,720,000.00 USD | 0.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD |
| `7D` | `5.10` | 62,110,000.00 USD | 62,110,000.00 USD | 0.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD |
| `7D` | `5.11` | 62,700,000.00 USD | 62,700,000.00 USD | 0.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD |
| `7D` | `5.12` | 63,270,000.00 USD | 63,270,000.00 USD | 0.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD |
| `7D` | `5.13` | 63,840,000.00 USD | 63,840,000.00 USD | 0.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD |
| `7D` | `5.14` | 64,280,000.00 USD | 64,280,000.00 USD | 0.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD |
| `7D` | `5.15` | 64,830,000.00 USD | 64,830,000.00 USD | 0.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD |
| `7D` | `5.16` | 65,350,000.00 USD | 65,350,000.00 USD | 0.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD |
| `7D` | `5.17` | 65,960,000.00 USD | 65,960,000.00 USD | 0.00 USD | 280,710.00 USD | 85,040.00 USD | 244,330.00 USD |
| `7D` | `5.18` | 66,210,000.00 USD | 66,210,000.00 USD | 0.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD |
| `7D` | `5.19` | 66,430,000.00 USD | 66,430,000.00 USD | 0.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD |
| `7D` | `5.20` | 66,680,000.00 USD | 66,680,000.00 USD | 0.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD |
| `7D` | `5.21` | 66,920,000.00 USD | 66,920,000.00 USD | 0.00 USD | 105,330.00 USD | 20,850.00 USD | 110,400.00 USD |
| `7D` | `5.22` | 66,980,000.00 USD | 66,980,000.00 USD | 0.00 USD | 48,760.00 USD | 13,410.00 USD | 398.26 USD |
| `7D` | `5.23` | 67,040,000.00 USD | 67,040,000.00 USD | 0.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.08B` | Total OI Tokens: `260,962,802.6 NEAR`
  * 1h OI Change: `+1.95%` | 4h OI Change: `-3.00%` | 24h OI Change: `-13.77%`
  * Exchange Breakdown: Binance=`206.92M` | Bybit=`147.37M` | OKX=`50.66M` | Hyperliquid=`236.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-16.46K` | Last 24h: `59.84K` | Last 3d: `308.79K` | Last 7d: `236.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0010%` | **USDT OKX** | `-0.0174%` |
| **USDT Bybit** | `-0.0101%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0010%` | **USDT BingX** | `0.0019%` |
| **USDT Gate** | `-0.0610%` | **USDT Bitget** | `-0.0106%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `58.76%` | `41.24%` | `1.42` | 24,230,000.00 USD |
| `15M` | `Binance` | `55.39%` | `44.61%` | `1.24` | 10,050,000.00 USD |
| `15M` | `OKX` | `59.61%` | `40.39%` | `1.48` | 3,100,000.00 USD |
| `15M` | `Bybit` | `54.59%` | `45.41%` | `1.20` | 3,260,000.00 USD |
| `15M` | `KuCoin` | `52.87%` | `47.13%` | `1.12` | 160,650.00 USD |
| `15M` | `Gate` | `47.71%` | `52.29%` | `0.91` | 681,290.00 USD |
| `15M` | `Bitget` | `68.4%` | `31.6%` | `2.16` | 1,310,000.00 USD |
| `15M` | `BingX` | `40.49%` | `59.51%` | `0.68` | 1,240,000.00 USD |
| `15M` | `MEXC` | `67.67%` | `32.33%` | `2.09` | 988,670.00 USD |
| `15M` | `Bitunix` | `65.93%` | `34.07%` | `1.94` | 664,350.00 USD |
| `15M` | `Hyperliquid` | `75.5%` | `24.5%` | `3.08` | 2,310,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.98%` | `49.02%` | `1.04` | 81,640.00 USD |
| `15M` | `Crypto.com` | `49.34%` | `50.66%` | `0.97` | 5,520.00 USD |
| `15M` | `WhiteBIT` | `98.39%` | `1.61%` | `61.11` | 253,240.00 USD |
| `15M` | `HTX` | `68.56%` | `31.44%` | `2.18` | 17,370.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `74.84%` | `25.16%` | `2.97` | 56,470.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `75.3%` | `24.7%` | `3.05` | 42,600.00 USD |
| `15M` | `Whale Positions` | `55.39%` | `44.61%` | `1.24` | 10,050,000.00 USD |
| `15M` | `Global Accounts` | `58.76%` | `41.24%` | `1.42` | 24,230,000.00 USD |
| `1H` | `NEAR` | `60.65%` | `39.35%` | `1.54` | 27,410,000.00 USD |
| `1H` | `Binance` | `55.98%` | `44.02%` | `1.27` | 11,560,000.00 USD |
| `1H` | `OKX` | `61.64%` | `38.36%` | `1.61` | 4,550,000.00 USD |
| `1H` | `Bybit` | `58.8%` | `41.2%` | `1.43` | 3,510,000.00 USD |
| `1H` | `KuCoin` | `52.48%` | `47.52%` | `1.10` | 412,340.00 USD |
| `1H` | `Gate` | `63.16%` | `36.84%` | `1.71` | 573,050.00 USD |
| `1H` | `Bitget` | `59.84%` | `40.16%` | `1.49` | 705,680.00 USD |
| `1H` | `BingX` | `71.35%` | `28.65%` | `2.49` | 940,420.00 USD |
| `1H` | `MEXC` | `67.91%` | `32.09%` | `2.12` | 2,400,000.00 USD |
| `1H` | `Bitunix` | `59.52%` | `40.48%` | `1.47` | 1,020,000.00 USD |
| `1H` | `Hyperliquid` | `64.73%` | `35.27%` | `1.84` | 1,080,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `66.92%` | `33.08%` | `2.02` | 133,970.00 USD |
| `1H` | `Crypto.com` | `41.76%` | `58.24%` | `0.72` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.47%` | `0.53%` | `187.68` | 409,450.00 USD |
| `1H` | `HTX` | `58.38%` | `41.62%` | `1.40` | 31,250.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `99.26%` | `0.74%` | `134.14` | 1,360.00 USD |
| `1H` | `Aster` | `66.58%` | `33.42%` | `1.99` | 74,880.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.14%` | `56.86%` | `0.76` | 33,060.00 USD |
| `1H` | `Whale Positions` | `55.98%` | `44.02%` | `1.27` | 11,560,000.00 USD |
| `1H` | `Global Accounts` | `60.65%` | `39.35%` | `1.54` | 27,410,000.00 USD |
| `4H` | `NEAR` | `50.08%` | `49.92%` | `1.00` | 255,900,000.00 USD |
| `4H` | `Binance` | `49.66%` | `50.34%` | `0.99` | 98,770,000.00 USD |
| `4H` | `OKX` | `52.51%` | `47.49%` | `1.11` | 34,590,000.00 USD |
| `4H` | `Bybit` | `50.44%` | `49.56%` | `1.02` | 37,970,000.00 USD |
| `4H` | `KuCoin` | `47.35%` | `52.65%` | `0.90` | 3,860,000.00 USD |
| `4H` | `Gate` | `47.03%` | `52.97%` | `0.89` | 7,550,000.00 USD |
| `4H` | `Bitget` | `52.76%` | `47.24%` | `1.12` | 17,160,000.00 USD |
| `4H` | `BingX` | `53.14%` | `46.86%` | `1.13` | 8,230,000.00 USD |
| `4H` | `MEXC` | `48.32%` | `51.68%` | `0.93` | 22,000,000.00 USD |
| `4H` | `Bitunix` | `51.61%` | `48.39%` | `1.07` | 7,830,000.00 USD |
| `4H` | `Hyperliquid` | `46.18%` | `53.82%` | `0.86` | 9,390,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.99%` | `45.01%` | `1.22` | 2,420,000.00 USD |
| `4H` | `Crypto.com` | `42.29%` | `57.71%` | `0.73` | 0.00 USD |
| `4H` | `WhiteBIT` | `82.07%` | `17.93%` | `4.58` | 2,630,000.00 USD |
| `4H` | `HTX` | `40.6%` | `59.4%` | `0.68` | 512,100.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.59%` | `54.41%` | `0.84` | 1,430,000.00 USD |
| `4H` | `Aster` | `20.85%` | `79.15%` | `0.26` | 1,260,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.11%` | `54.89%` | `0.82` | 323,740.00 USD |
| `4H` | `Whale Positions` | `49.66%` | `50.34%` | `0.99` | 98,770,000.00 USD |
| `4H` | `Global Accounts` | `50.08%` | `49.92%` | `1.00` | 255,900,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4.02` | `4.00` | `4.02` | `4.03` | `3.95` | 11,016,623.88 USD | 5,505,508.67 USD | 5,511,115.21 USD | -5,606.55 USD | `-0.05%` | `3B / 8S` |
| `5:00 UTC` | `3.99` | `3.99` | `3.99` | `4.01` | `3.97` | 6,380,993.73 USD | 2,663,458.31 USD | 3,717,535.41 USD | -1,054,077.10 USD | `-16.52%` | `2B / 11S` |
| `0:00 UTC` | `4.03` | `4.01` | `4.03` | `4.04` | `3.97` | 7,316,250.26 USD | 4,215,105.63 USD | 3,101,144.64 USD | 1,113,960.99 USD | `+15.23%` | `9B / 6S` |
| `5:00 UTC` | `4.06` | `4.05` | `4.06` | `4.08` | `4.02` | 8,251,415.10 USD | 5,342,802.98 USD | 2,908,612.12 USD | 2,434,190.86 USD | `+29.50%` | `19B / 0S` |
| `0:00 UTC` | `4.10` | `4.09` | `4.10` | `4.11` | `4.07` | 8,076,911.53 USD | 4,345,296.52 USD | 3,731,615.01 USD | 613,681.51 USD | `+7.60%` | `5B / 1S` |
| `5:00 UTC` | `4.06` | `4.07` | `4.06` | `4.10` | `4.05` | 6,914,413.13 USD | 3,114,711.21 USD | 3,799,701.92 USD | -684,990.71 USD | `-9.91%` | `2B / 8S` |
| `0:00 UTC` | `4.08` | `4.08` | `4.08` | `4.09` | `4.06` | 5,392,588.64 USD | 3,075,595.58 USD | 2,316,993.06 USD | 758,602.52 USD | `+14.07%` | `1B / 1S` |
| `5:00 UTC` | `4.07` | `4.08` | `4.07` | `4.11` | `4.07` | 4,324,346.41 USD | 2,642,977.58 USD | 1,681,368.84 USD | 961,608.74 USD | `+22.24%` | `17B / 1S` |
| `0:00 UTC` | `4.14` | `4.13` | `4.14` | `4.16` | `4.10` | 9,990,039.56 USD | 5,818,620.01 USD | 4,171,419.55 USD | 1,647,200.46 USD | `+16.49%` | `10B / 2S` |
| `5:00 UTC` | `4.15` | `4.15` | `4.15` | `4.16` | `4.14` | 1,018,754.20 USD | 516,725.51 USD | 502,028.69 USD | 14,696.82 USD | `+1.44%` | `1B / 5S` |

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
| `5m` | 278,800.00 USD | 1,190,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,990,000.00 USD | 2,270,000.00 USD | **`ACCUMULATION`** |
| `30m` | 2,990,000.00 USD | 5,000,000.00 USD | **`ACCUMULATION`** |
| `1h` | 3,130,000.00 USD | 5,440,000.00 USD | **`ACCUMULATION`** |
| `2h` | 5,490,000.00 USD | 14,320,000.00 USD | **`ACCUMULATION`** |
| `4h` | 2,820,000.00 USD | 1,410,000.00 USD | **`ACCUMULATION`** |
| `6h` | -729,190.00 USD | -5,850,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,540,000.00 USD | -17,580,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -14,590,000.00 USD | -31,380,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -14,560,000.00 USD | -54,380,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -77,500,000.00 USD | -129,680,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -245,220,000.00 USD | -679,090,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+278.80K` | 15m=`+1.99M` | 1h=`+3.13M` | 24h=`-14.56M`
* Futures Capital Netflows: 5m=`+1.19M` | 15m=`+2.27M` | 1h=`+5.44M` | 24h=`-54.38M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3.84` (Risk Distance: `0.1137` pts)
  * +2.5R Take Profit: `4.24`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.13` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.24` (Risk Distance: `0.1137` pts)
  * +2.5R Take Profit: `3.84`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.20`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
