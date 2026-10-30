# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:20:35 IST` (`2026-10-30 08:50:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9100` | **Live Ask Quote**: `0.9102` | **Mid Price**: `0.9101`
- **Spread Points**: `0.000182` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
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
  * Session VWAP: `0.9101` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9165` | Lower -3.00σ Band: `0.9037`
  * Upper +2.51σ Band: `0.9151` | Lower -2.51σ Band: `0.9051`
  * Upper +2.01σ Band: `0.9139` | Lower -2.01σ Band: `0.9063`
  * Upper +2.00σ Band: `0.9137` | Lower -2.00σ Band: `0.9065`
  * Upper +1.28σ Band: `0.9126` | Lower -1.28σ Band: `0.9075`
  * Upper +1.00σ Band: `0.9119` | Lower -1.00σ Band: `0.9083`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9101` | EMA-20=`0.9101` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9101` (Slope: `+0.0000`) | EMA-100=`0.9101`
  * Institutional Anchors: EMA-144=`0.9101` | EMA-200=`0.9101` (Slope: `+0.0000`) | EMA-233=`0.9101`
- **Range Boundaries**: 24H High=`0.9192` | 24H Low=`0.9010` | Weekly High=`0.9283` | Weekly Low=`0.8919`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9128` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.9101` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.9074` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9137` | POC=`0.9101` | VAL=`0.9065`
  * Prior Day Extremes: PDH=`0.9156` | PDL=`0.9046` | PDC=`0.9101`
  * Monday Range Blueprint: High=`0.9146` | Mid=`0.9101` | Low=`0.9055`
  * Developing Weekly Value Area: Weekly VAH=`0.9174` | Weekly POC=`0.9101` | Weekly VAL=`0.9028`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9119` | Low=`0.9083`
  * London Session (08:00-16:00 UTC): High=`0.9137` | Low=`0.9065`
  * New York Session (13:00-21:00 UTC): High=`0.9156` | Low=`0.9046`
  * Initial Balance (First Hour): IB High=`0.9128` | IB Low=`0.9074`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9065` - `0.9137`
  * Optimal Trade Entry (OTE 0.705): `0.9119`
  * Structural Invalidation Anchor (0.786): `0.9174`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.8842` | `0.8847` | `0.8824` | `0.8837` | `918,380` | 811,521.16 USD | 288,874.76 USD | `+35.60%` | -16,253,790.28 USD | `+1.64` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.8836` | `0.8847` | `0.8816` | `0.8834` | `630,006` | 556,327.93 USD | -23,575.92 USD | `-4.24%` | -16,277,366.20 USD | `+0.23` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.8835` | `0.8836` | `0.8817` | `0.8827` | `191,228` | 168,724.81 USD | 96,255.13 USD | `+57.05%` | -16,181,111.07 USD | `+0.71` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.8851` | `0.8874` | `0.8802` | `0.8868` | `2,706,884` | 2,392,175.76 USD | -150,530.73 USD | `-6.29%` | -16,499,038.14 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.8869` | `0.8882` | `0.8831` | `0.8841` | `2,073,286` | 1,835,307.01 USD | -43,626.90 USD | `-2.38%` | -16,542,665.04 USD | `+0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.8842` | `0.8847` | `0.8816` | `0.8817` | `1,607,036` | 1,419,619.71 USD | 258,929.64 USD | `+18.24%` | -16,283,735.40 USD | `+1.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.8904` | `0.9022` | `0.8872` | `0.8956` | `10,514,403` | 9,396,983.01 USD | -506,206.28 USD | `-5.39%` | -14,878,999.74 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8957` | `0.8970` | `0.8816` | `0.8851` | `11,435,469` | 10,155,670.71 USD | -1,564,974.23 USD | `-15.41%` | -16,443,973.97 USD | `-0.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.8851` | `0.8882` | `0.8802` | `0.8817` | `6,387,265` | 5,647,153.80 USD | 64,720.70 USD | `+1.15%` | -16,379,253.27 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,183,102.89 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8851` | `53,790,878` | 48,001,087.15 USD | -4,396,820.97 USD | `-9.16%` | -16,579,923.86 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8851` | `0.8882` | `0.8802` | `0.8817` | `6,387,265` | 5,647,153.80 USD | 64,720.70 USD | `+1.15%` | -16,515,203.16 USD | `+0.90` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -544,594.77 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,247,029.61 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,183,102.89 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8851` | `53,790,878` | 48,001,087.15 USD | -4,396,820.97 USD | `-9.16%` | -16,579,923.86 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8851` | `0.8882` | `0.8802` | `0.8817` | `6,387,265` | 5,647,153.80 USD | 64,720.70 USD | `+1.15%` | -16,515,203.16 USD | `+0.90` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.9101`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.8819` | `1261.7000` | 1,112.73 USD | 29,998.52 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8819` | `2488.3000` | 2,194.48 USD | 32,193.00 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8819` | `4535.7000` | 3,999.90 USD | 36,192.90 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.8820` | `1273.2000` | 1,122.99 USD | 12,322.28 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8820` | `5677.9000` | 5,007.91 USD | 17,330.19 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8820` | `11347.0000` | 10,007.94 USD | 27,338.13 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.8820` | `85.0000` | 74.97 USD | 27,413.09 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8820` | `1669.8000` | 1,472.70 USD | 28,885.79 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8821` | `1273.2000` | 1,123.13 USD | 5,616.84 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8821` | `1273.4000` | 1,123.28 USD | 6,740.12 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8821` | `2719.3000` | 2,398.69 USD | 9,138.82 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8821` | `2335.9000` | 2,060.47 USD | 11,199.29 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8822` | `1273.2000` | 1,123.22 USD | 3,913.69 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8822` | `50.8000` | 44.82 USD | 3,958.51 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8822` | `130.7000` | 115.30 USD | 4,073.81 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8822` | `476.0000` | 419.91 USD | 4,493.71 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.8823` | `1135.2000` | 1,001.58 USD | 1,667.17 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8823` | `1273.2000` | 1,123.31 USD | 2,790.47 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8824` | `723.8000` | 638.67 USD | 665.59 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8825` | `30.5000` | 26.92 USD | 26.92 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `0.8826` | `2408.0000` | 2,125.37 USD | 9,824.36 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.8826` | `6798.3000` | 6,000.32 USD | 7,698.99 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8826` | `42.8000` | 37.78 USD | 1,698.68 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8826` | `1134.9000` | 1,001.63 USD | 1,660.90 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `0.8826` | `747.0000` | 659.27 USD | 659.27 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.8826` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.88` | `0.00%` | `-` |
| `ASK` | `0.8827` | `1273.2000` | 1,123.85 USD | 10,948.22 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8828` | `1273.1000` | 1,123.92 USD | 23,212.16 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8828` | `5673.0000` | 5,008.12 USD | 22,088.24 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8828` | `5673.0000` | 5,008.07 USD | 17,080.12 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8828` | `1273.1000` | 1,123.83 USD | 12,072.05 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8829` | `1560.3000` | 1,377.65 USD | 27,215.10 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8829` | `1089.5000` | 961.93 USD | 25,837.45 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8829` | `1273.1000` | 1,124.01 USD | 24,875.52 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8829` | `497.7000` | 439.41 USD | 23,751.51 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8829` | `113.2000` | 99.94 USD | 23,312.10 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8830` | `1261.5000` | 1,113.90 USD | 29,453.10 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8830` | `1273.1000` | 1,124.10 USD | 28,339.19 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8831` | `692.4000` | 611.44 USD | 42,492.55 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8831` | `2719.4000` | 2,401.42 USD | 41,881.11 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8831` | `11354.5000` | 10,026.59 USD | 39,479.69 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `674` | `0xb83d...6e36` | `SHORT` | 3,370,261.93 USD | `3,817,609.40` | `1.11` | `0.8828` | `33.23` | 848,473.39 USD | `+25.18%` | `3X Cross` |
| `1016` | `0xa2ce...3126` | `LONG` | 2,205,559.18 USD | `2,500,010.40` | `0.8597` | `0.8828` | `0.000000` | 56,352.64 USD | `+2.56%` | `10X Cross` |
| `1525` | `0x9946...0852` | `SHORT` | 1,423,904.17 USD | `1,613,032.20` | `1.06` | `0.8831` | `1.84` | 284,773.91 USD | `+20.00%` | `10X Cross` |
| `1920` | `0x9df2...c665` | `SHORT` | 1,059,384.00 USD | `1,200,000.00` | `0.7465` | `0.8831` | `26.14` | -163,531.60 USD | `-15.44%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9070` | 5,006.08 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9070 USD [API] | `2026-10-29 08:09:57` |
| `ANNOUNCEMENT` | `INFO` | `0.9097` | 12,247.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 12.25K USD at 0.9097 USD [API] | `2026-10-29 08:26:24` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 1,313.92 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.31K USD at 1.0671 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,887.95 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.89K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 399.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.40K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 639.25 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.64K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,811.97 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.81K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,655.76 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.66K USD at 1.0673 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 1,999.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.00K USD at 1.0675 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 10.25 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.01K USD at 1.0675 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 5,003.24 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 5.00K USD at 1.0677 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 791.63 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.79K USD at 1.0679 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,836.50 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.84K USD at 1.0680 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 2,515.30 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.52K USD at 1.1066 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 9,682.20 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 9.68K USD at 1.1066 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 1,660.05 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.66K USD at 1.1067 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 399.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.40K USD at 1.1067 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 3,348.76 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.35K USD at 1.1067 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `0.9111` | 5,342.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9111 USD [API] | `2026-10-29 09:38:03` |
| `ANNOUNCEMENT` | `INFO` | `0.9130` | 5,343.70 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9130 USD [API] | `2026-10-29 09:42:02` |
| `ANNOUNCEMENT` | `INFO` | `0.9240` | 5,089.80 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.09K USD at 0.9240 USD [API] | `2026-10-29 10:48:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9247` | 16,233.60 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 16.23K USD at 0.9247 USD [API] | `2026-10-29 11:01:51` |
| `ANNOUNCEMENT` | `INFO` | `0.9234` | 5,154.59 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.15K USD at 0.9234 USD [API] | `2026-10-29 11:05:05` |
| `ANNOUNCEMENT` | `INFO` | `0.9231` | 17,331.58 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 17.33K USD at 0.9231 USD [API] | `2026-10-29 11:07:33` |
| `ANNOUNCEMENT` | `INFO` | `0.9254` | 5,344.08 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9254 USD [API] | `2026-10-29 11:09:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9222` | 6,029.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.03K USD at 0.9222 USD [API] | `2026-10-29 11:29:21` |
| `ANNOUNCEMENT` | `INFO` | `0.9260` | 12,149.38 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 12.15K USD at 0.9260 USD [API] | `2026-10-29 12:46:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9260` | 5,344.06 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9260 USD [API] | `2026-10-29 12:46:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9278` | 5,999.95 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.00K USD at 0.9278 USD [API] | `2026-10-29 13:20:55` |
| `ANNOUNCEMENT` | `INFO` | `0.9244` | 7,325.08 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 7.33K USD at 0.9244 USD [API] | `2026-10-29 13:39:14` |
| `ANNOUNCEMENT` | `INFO` | `0.9277` | 11,844.84 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 11.84K USD at 0.9277 USD [API] | `2026-10-29 13:41:43` |
| `ANNOUNCEMENT` | `INFO` | `0.9315` | 5,006.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9315 USD [API] | `2026-10-29 14:03:28` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 13.62 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.01K USD at 1.0320 USD [API] | `2026-09-24 20:04:05` |
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 1,601.78 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.60K USD at 0.9406 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 661.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.66K USD at 0.9406 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 919.02 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.92K USD at 0.9406 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 415.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.42K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 686.09 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.69K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 725.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.73K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 725.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.73K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9345` | 16,444.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 16.44K USD at 0.9345 USD [API] | `2026-10-29 14:13:52` |
| `ANNOUNCEMENT` | `INFO` | `0.9470` | 5,005.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9470 USD [API] | `2026-10-29 17:00:22` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9069` (Vol: 414,400.00 USD, Dist: `+2.86%`) | Long MP=`0.8716` (Vol: 414,400.00 USD, Dist: `--1.15%`)
  * 48H Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+2.93%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--1.18%`)
  * 3D Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+2.93%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--1.18%`)
  * 7D Horizon: Short MP=`0.9731` (Vol: 542,500.00 USD, Dist: `+10.37%`) | Long MP=`0.8715` (Vol: 414,400.00 USD, Dist: `--1.16%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1835` | 183.50 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 448.46 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 3,130.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 229.50 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 1,670.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 1,620.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 151.36 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 168.52 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 2,640.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 849.48 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 23,900.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 195.33 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 340.94 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 603.12 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3095` | 126.71 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3185` | 105.39 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3205` | 3,900.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3325` | 3,330.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3395` | 9,670.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 1,230.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3475` | 3,850.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3525` | 27,390.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3535` | 4,390.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3745` | 2,050.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3765` | 6,400.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3775` | 420.95 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 2,020.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4005` | 5,010.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 3,360.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4165` | 8,330.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4175` | 29,230.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4215` | 3,930.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4245` | 468.61 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 771.39 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4275` | 753.25 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 44,400.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,920.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 105.25 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 151.88 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 1,020.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4585` | 141.26 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 3,720.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 9,230.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 166.70 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 3,540.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 646.73 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 5,690.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 4,730.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 5,680.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 537.10 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 106.04 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 1,070.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5205` | 1,710.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5225` | 273.58 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5255` | 7,230.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 123,370.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5305` | 1,720.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5335` | 7,790.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 113.47 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5365` | 252.96 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 126.46 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 6,150.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 618.53 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5615` | 442.63 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 4,800.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 7,200.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 109,930.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 217.37 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 7,350.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 81,340.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 584.50 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,280.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 822.98 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 225.93 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 1,130.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,400.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 608.61 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5975` | 3,420.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 840.95 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 4,760.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 323.79 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 2,730.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 886.10 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6095` | 214.54 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,280.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 438.73 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 112.33 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 2,110.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 44,160.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,980.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 12,570.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 2,400.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 708.53 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 33,460.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 1,310.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6325` | 18,210.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 843.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 1,100.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 33,040.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 477.63 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,190.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 2,810.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 3,290.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 344.82 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 106.75 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6525` | 2,350.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 2,840.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 7,850.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 7,360.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 7,070.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 1,200.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 4,960.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 4,840.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 1,190.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 528.73 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 2,260.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 5,670.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,630.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 2,240.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,280.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 27,680.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 387.20 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 744.15 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 2,370.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 122.94 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 43,650.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 19,300.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 15,130.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,960.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 6,110.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 192.16 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 3,170.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 3,600.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 722.28 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,700.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,030.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 4,830.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 235.37 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7025` | 39,470.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 8,970.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 141.38 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 143.14 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 1,560.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,020.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 1,140.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 4,190.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 639.47 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 927.55 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 11,030.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 4,620.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7185` | 126.96 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 420.19 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 8,450.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,420.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 8,480.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7245` | 2,520.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 311.60 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 3,410.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 39,490.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 424.86 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7315` | 529.39 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 907.93 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 448,360.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 6,240.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 3,450.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7380` | 10,540,000.00 USD | 10,540,000.00 USD | 56,620.00 USD | 28,770.00 USD | 82,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,020.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7400` | 10,370,000.00 USD | 10,370,000.00 USD | 17,280.00 USD | 13,180.00 USD | 24,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7420` | 10,320,000.00 USD | 10,320,000.00 USD | 31,920.00 USD | 8,580.00 USD | 37,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7425` | 2,280.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 783,980.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7440` | 10,240,000.00 USD | 10,240,000.00 USD | 65,280.00 USD | 21,190.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7455` | 2,160.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7460` | 10,110,000.00 USD | 10,110,000.00 USD | 22,100.00 USD | 24,720.00 USD | 42,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7465` | 359.96 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7480` | 10,020,000.00 USD | 10,020,000.00 USD | 11,220.00 USD | 6,300.00 USD | 375.99 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7500` | 10,000,000.00 USD | 10,000,000.00 USD | 25,600.00 USD | 12,880.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7520` | 9,950,000.00 USD | 9,950,000.00 USD | 2,130.00 USD | 10,160.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7535` | 569.50 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7540` | 9,920,000.00 USD | 9,920,000.00 USD | 9,690.00 USD | 4,770.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7545` | 922.07 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,070.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7560` | 9,890,000.00 USD | 9,890,000.00 USD | 2,690.00 USD | 17,670.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7580` | 9,870,000.00 USD | 9,870,000.00 USD | 19,590.00 USD | 20,390.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 7,810.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7600` | 9,830,000.00 USD | 9,830,000.00 USD | 8,420.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7620` | 9,810,000.00 USD | 9,810,000.00 USD | 40,420.00 USD | 16,580.00 USD | 630.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7625` | 859.11 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 782.36 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7640` | 9,750,000.00 USD | 9,750,000.00 USD | 556.58 USD | 118.70 USD | 573.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,060.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 2,740.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7660` | 9,750,000.00 USD | 9,750,000.00 USD | 1,280.00 USD | 23,260.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7665` | 2,950.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7675` | 24,420.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7680` | 9,700,000.00 USD | 9,700,000.00 USD | 182.28 USD | 3,780.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7685` | 6,600.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7695` | 144,250.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7700` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7720` | 9,690,000.00 USD | 9,690,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,940.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 5,230.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 324,090.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 2,930.00 USD | 775,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 772,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 744,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 2,640.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 743,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7820` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 1,440.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 21,600.00 USD | 739,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7840` | 9,660,000.00 USD | 9,660,000.00 USD | 6,050.00 USD | 2,680.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7845` | 155.96 USD | 718,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7860` | 9,650,000.00 USD | 9,650,000.00 USD | 1,740.00 USD | 45,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 718,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 714,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7900` | 9,600,000.00 USD | 9,600,000.00 USD | 6,610.00 USD | 28,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,160.00 USD | 714,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7910` | 7,360,000.00 USD | 7,360,000.00 USD | 13,200.00 USD | 12,510.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 11,600.00 USD | 711,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 7,330,000.00 USD | 7,330,000.00 USD | 8,420.00 USD | 9,490.00 USD | 36,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7920` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 23,790.00 USD | 69,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 3,800.00 USD | 699,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7930` | 7,270,000.00 USD | 7,270,000.00 USD | 952.83 USD | 12,430.00 USD | 7,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 695,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7940` | 7,250,000.00 USD | 7,250,000.00 USD | 20,620.00 USD | 8,610.00 USD | 14,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 1,760.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 736.66 USD | 694,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7950` | 7,210,000.00 USD | 7,210,000.00 USD | 5,840.00 USD | 3,900.00 USD | 24,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 52,610.00 USD | 694,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 7,170,000.00 USD | 7,170,000.00 USD | 1,860.00 USD | 2,710.00 USD | 20,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 9,470,000.00 USD | 9,470,000.00 USD | 4,090.00 USD | 19,750.00 USD | 87,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 12,980.00 USD | 641,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 7,150,000.00 USD | 7,150,000.00 USD | 16,800.00 USD | 16,290.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,460.00 USD | 628,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 7,070,000.00 USD | 7,070,000.00 USD | 8,320.00 USD | 0.00 USD | 165.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 9,360,000.00 USD | 9,360,000.00 USD | 33,940.00 USD | 3,570.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 40,230.00 USD | 621,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7990` | 7,070,000.00 USD | 7,070,000.00 USD | 1,600.00 USD | 20,590.00 USD | 18,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 4,220.00 USD | 580,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 7,020,000.00 USD | 7,020,000.00 USD | 30,830.00 USD | 10,990.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 9,270,000.00 USD | 9,270,000.00 USD | 41,450.00 USD | 16,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 7,110.00 USD | 576,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8010` | 6,970,000.00 USD | 6,970,000.00 USD | 1,140.00 USD | 3,860.00 USD | 200.14 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 6,710.00 USD | 569,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8020` | 6,960,000.00 USD | 6,960,000.00 USD | 796.46 USD | 6,400.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 9,210,000.00 USD | 9,210,000.00 USD | 1,890.00 USD | 29,180.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 1,350.00 USD | 562,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8030` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 1,400.00 USD | 159.97 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,790.00 USD | 561,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8040` | 6,950,000.00 USD | 6,950,000.00 USD | 43,320.00 USD | 22,790.00 USD | 21,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8045` | 15,720.00 USD | 553,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8050` | 6,860,000.00 USD | 6,860,000.00 USD | 19,550.00 USD | 7,230.00 USD | 330.63 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 361.11 USD | 538,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 6,830,000.00 USD | 6,830,000.00 USD | 32,080.00 USD | 11,640.00 USD | 73,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 9,130,000.00 USD | 9,130,000.00 USD | 12,280.00 USD | 737.70 USD | 1,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 537,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 6,710,000.00 USD | 6,710,000.00 USD | 8,540.00 USD | 14,620.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 530,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8080` | 6,690,000.00 USD | 6,690,000.00 USD | 2,530.00 USD | 4,510.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 9,110,000.00 USD | 9,110,000.00 USD | 5,030.00 USD | 11,280.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 527,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8090` | 6,680,000.00 USD | 6,680,000.00 USD | 587.71 USD | 5,580.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 130,110.00 USD | 505,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 6,670,000.00 USD | 6,670,000.00 USD | 1,830.00 USD | 5,380.00 USD | 248.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 9,090,000.00 USD | 9,090,000.00 USD | 4,310.00 USD | 9,850.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 7,750.00 USD | 375,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8110` | 6,670,000.00 USD | 6,670,000.00 USD | 1,650.00 USD | 2,090.00 USD | 196.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,970.00 USD | 367,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 6,660,000.00 USD | 6,660,000.00 USD | 13,640.00 USD | 780.21 USD | 23,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 9,070,000.00 USD | 9,070,000.00 USD | 73,000.00 USD | 9,210.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 1,160.00 USD | 364,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8130` | 6,620,000.00 USD | 6,620,000.00 USD | 683.00 USD | 989.28 USD | 706.99 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 363,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 6,620,000.00 USD | 6,620,000.00 USD | 14,810.00 USD | 523.16 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8140` | 8,950,000.00 USD | 8,950,000.00 USD | 55,190.00 USD | 31,920.00 USD | 79,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 6,590,000.00 USD | 6,590,000.00 USD | 4,970.00 USD | 1,140.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 2,810.00 USD | 359,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 6,580,000.00 USD | 6,580,000.00 USD | 17,910.00 USD | 1,970.00 USD | 23,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 8,780,000.00 USD | 8,780,000.00 USD | 186,980.00 USD | 49,790.00 USD | 146,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 104.92 USD | 356,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8170` | 6,540,000.00 USD | 6,540,000.00 USD | 56,460.00 USD | 4,990.00 USD | 30,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 77,840.00 USD | 356,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 6,450,000.00 USD | 6,450,000.00 USD | 361.35 USD | 1,680.00 USD | 213.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 8,400,000.00 USD | 8,400,000.00 USD | 82,600.00 USD | 41,370.00 USD | 43,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 24,130.00 USD | 278,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8190` | 6,440,000.00 USD | 6,440,000.00 USD | 24,470.00 USD | 1,600.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,720.00 USD | 254,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 6,410,000.00 USD | 6,410,000.00 USD | 87,930.00 USD | 4,880.00 USD | 73,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 8,230,000.00 USD | 8,230,000.00 USD | 205,920.00 USD | 48,700.00 USD | 97,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 1,400.00 USD | 253,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8210` | 6,240,000.00 USD | 6,240,000.00 USD | 15,840.00 USD | 83,090.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 474.01 USD | 251,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 6,090,000.00 USD | 6,090,000.00 USD | 58,680.00 USD | 3,580.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8220` | 7,880,000.00 USD | 7,880,000.00 USD | 110,800.00 USD | 74,480.00 USD | 175,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 1,490.00 USD | 251,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 6,000,000.00 USD | 6,000,000.00 USD | 7,960.00 USD | 5,500.00 USD | 105,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 1,870.00 USD | 249,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 5,880,000.00 USD | 5,880,000.00 USD | 8,230.00 USD | 2,400.00 USD | 32,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8240` | 7,520,000.00 USD | 7,520,000.00 USD | 104,380.00 USD | 43,480.00 USD | 87,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 20,280.00 USD | 247,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 5,840,000.00 USD | 5,840,000.00 USD | 26,090.00 USD | 2,480.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 1,580.00 USD | 227,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 5,800,000.00 USD | 5,800,000.00 USD | 19,170.00 USD | 8,970.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 7,280,000.00 USD | 7,280,000.00 USD | 197,160.00 USD | 32,880.00 USD | 111,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8270` | 5,760,000.00 USD | 5,760,000.00 USD | 39,540.00 USD | 22,100.00 USD | 8,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 226,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 5,690,000.00 USD | 5,690,000.00 USD | 1,490.00 USD | 773.90 USD | 313.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 6,940,000.00 USD | 6,940,000.00 USD | 118,780.00 USD | 44,400.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 221,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8290` | 5,690,000.00 USD | 5,690,000.00 USD | 24,750.00 USD | 11,650.00 USD | 46,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8300` | 5,600,000.00 USD | 5,600,000.00 USD | 3,410.00 USD | 3,180.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 6,690,000.00 USD | 6,690,000.00 USD | 33,770.00 USD | 45,100.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8310` | 5,590,000.00 USD | 5,590,000.00 USD | 2,590.00 USD | 27,590.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 5,540,000.00 USD | 5,540,000.00 USD | 867.90 USD | 10,780.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 6,560,000.00 USD | 6,560,000.00 USD | 90,830.00 USD | 77,110.00 USD | 150,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 5,500,000.00 USD | 5,500,000.00 USD | 7,940.00 USD | 19,140.00 USD | 74,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 5,400,000.00 USD | 5,400,000.00 USD | 142,540.00 USD | 21,960.00 USD | 30,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 6,240,000.00 USD | 6,240,000.00 USD | 114,580.00 USD | 56,360.00 USD | 180,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8345` | 5,750.00 USD | 101,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8350` | 5,200,000.00 USD | 5,200,000.00 USD | 14,620.00 USD | 13,380.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 5,170,000.00 USD | 5,170,000.00 USD | 45,630.00 USD | 1,600.00 USD | 397.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 5,890,000.00 USD | 5,890,000.00 USD | 178,100.00 USD | 28,000.00 USD | 99,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8370` | 5,130,000.00 USD | 5,130,000.00 USD | 19,230.00 USD | 9,130.00 USD | 129,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 327.21 USD | 95,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 4,970,000.00 USD | 4,970,000.00 USD | 32,770.00 USD | 59,720.00 USD | 16,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 5,590,000.00 USD | 5,590,000.00 USD | 65,710.00 USD | 221,490.00 USD | 223,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 7,300.00 USD | 95,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8390` | 4,860,000.00 USD | 4,860,000.00 USD | 42,590.00 USD | 792.50 USD | 33,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 4,780,000.00 USD | 4,780,000.00 USD | 4,220.00 USD | 9,410.00 USD | 22,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 5,080,000.00 USD | 5,080,000.00 USD | 88,890.00 USD | 56,210.00 USD | 61,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 4,750,000.00 USD | 4,750,000.00 USD | 17,400.00 USD | 16,230.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 134.47 USD | 87,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 4,660,000.00 USD | 4,660,000.00 USD | 71,930.00 USD | 48,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 4,870,000.00 USD | 4,870,000.00 USD | 96,530.00 USD | 66,440.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 11,390.00 USD | 87,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 4,540,000.00 USD | 4,540,000.00 USD | 17,820.00 USD | 18,730.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 103.24 USD | 76,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 4,480,000.00 USD | 4,480,000.00 USD | 49,800.00 USD | 44,320.00 USD | 166.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 4,700,000.00 USD | 4,700,000.00 USD | 28,900.00 USD | 111,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 803.20 USD | 76,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8450` | 4,390,000.00 USD | 4,390,000.00 USD | 22,880.00 USD | 30,550.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 10,690.00 USD | 75,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 4,320,000.00 USD | 4,320,000.00 USD | 623.10 USD | 63,560.00 USD | 26,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 4,560,000.00 USD | 4,560,000.00 USD | 52,800.00 USD | 57,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 284.68 USD | 64,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8470` | 4,230,000.00 USD | 4,230,000.00 USD | 51,620.00 USD | 37,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 1,270.00 USD | 64,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 36,960.00 USD | 82,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 4,450,000.00 USD | 4,450,000.00 USD | 73,880.00 USD | 61,480.00 USD | 82,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 4,020,000.00 USD | 4,020,000.00 USD | 57,710.00 USD | 61,840.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 6,910.00 USD | 63,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 3,830,000.00 USD | 3,830,000.00 USD | 35,490.00 USD | 37,570.00 USD | 107,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 4,230,000.00 USD | 4,230,000.00 USD | 85,470.00 USD | 58,490.00 USD | 50,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8505` | 13,600.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 3,650,000.00 USD | 3,650,000.00 USD | 41,500.00 USD | 106,640.00 USD | 49,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 3,450,000.00 USD | 3,450,000.00 USD | 59,930.00 USD | 95,740.00 USD | 88,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 4,030,000.00 USD | 4,030,000.00 USD | 77,320.00 USD | 53,520.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 42,610.00 USD | 42,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8530` | 3,210,000.00 USD | 3,210,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 104.30 USD | 104.30 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 13,200.00 USD | 128.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 3,850,000.00 USD | 3,850,000.00 USD | 277,690.00 USD | 50,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 3,000,000.00 USD | 3,000,000.00 USD | 1,920.00 USD | 37,290.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,950,000.00 USD | 2,950,000.00 USD | 30,660.00 USD | 17,140.00 USD | 52,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 3,520,000.00 USD | 3,520,000.00 USD | 87,380.00 USD | 91,360.00 USD | 33,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,850,000.00 USD | 2,850,000.00 USD | 14,730.00 USD | 12,760.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,810,000.00 USD | 2,810,000.00 USD | 32,900.00 USD | 54,050.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 3,310,000.00 USD | 3,310,000.00 USD | 146,570.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,700,000.00 USD | 2,700,000.00 USD | 13,810.00 USD | 6,720.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,640,000.00 USD | 2,640,000.00 USD | 75,640.00 USD | 32,480.00 USD | 200.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 3,150,000.00 USD | 3,150,000.00 USD | 38,890.00 USD | 164,470.00 USD | 20,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,540,000.00 USD | 2,540,000.00 USD | 21,600.00 USD | 0.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,510,000.00 USD | 2,510,000.00 USD | 42,920.00 USD | 25,800.00 USD | 26,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 2,920,000.00 USD | 2,920,000.00 USD | 25,100.00 USD | 145,110.00 USD | 394,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 2,410,000.00 USD | 2,410,000.00 USD | 48,390.00 USD | 98,690.00 USD | 113,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,150,000.00 USD | 2,150,000.00 USD | 28,850.00 USD | 51,300.00 USD | 29.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 2,360,000.00 USD | 2,360,000.00 USD | 83,850.00 USD | 0.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 35,750.00 USD | 136,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,900,000.00 USD | 1,900,000.00 USD | 127,140.00 USD | 13,430.00 USD | 54,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 2,270,000.00 USD | 2,270,000.00 USD | 294,020.00 USD | 122,950.00 USD | 678,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8670` | 1,700,000.00 USD | 1,700,000.00 USD | 100,220.00 USD | 33,880.00 USD | 142,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,430,000.00 USD | 1,430,000.00 USD | 50,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 1,180,000.00 USD | 1,180,000.00 USD | 213,340.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 97,830.00 USD | 31,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 952,500.00 USD | 952,500.00 USD | 0.00 USD | 34,600.00 USD | 111,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,220,000.00 USD | 1,220,000.00 USD | 152,210.00 USD | 62,100.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 855,600.00 USD | 855,600.00 USD | 30,060.00 USD | 26,400.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 806,620.00 USD | 806,620.00 USD | 207,250.00 USD | 101,630.00 USD | 87,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 778,130.00 USD | 778,130.00 USD | 55,600.00 USD | 39,670.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 652,890.00 USD | 652,890.00 USD | 61,330.00 USD | 20,260.00 USD | 39,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 410,210.00 USD | 410,210.00 USD | 9,520.00 USD | 72,100.00 USD | 71,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 531,870.00 USD | 531,870.00 USD | 29,460.00 USD | 0.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 418,910.00 USD | 418,910.00 USD | 0.00 USD | 0.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 256,990.00 USD | 256,990.00 USD | 16,700.00 USD | 29,060.00 USD | 189,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 365,840.00 USD | 365,840.00 USD | 27,620.00 USD | 20,280.00 USD | 94,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 223,650.00 USD | 223,650.00 USD | 79,990.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 21,780.00 USD | 21,780.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 126,240.00 USD | 126,240.00 USD | 39,180.00 USD | 0.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 74,130.00 USD | 74,130.00 USD | 4,760.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 20,310.00 USD | 20,310.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 68,360.00 USD | 68,360.00 USD | 37,200.00 USD | 0.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8820` | 94,270.00 USD | 94,270.00 USD | 0.00 USD | 0.00 USD | 94,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8820` | 188,540.00 USD | 188,540.00 USD | 0.00 USD | 0.00 USD | 94,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8840` | 190,360.00 USD | 190,360.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8850` | 190,580.00 USD | 190,580.00 USD | 0.00 USD | 0.00 USD | 214.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8860` | 191,690.00 USD | 191,690.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8870` | 193,090.00 USD | 193,090.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8880` | 315,850.00 USD | 315,850.00 USD | 122,200.00 USD | 0.00 USD | 560.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8880` | 3,860.00 USD | 3,860.00 USD | 0.00 USD | 3,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8900` | 318,710.00 USD | 318,710.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8900` | 12,670.00 USD | 12,670.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8910` | 406,910.00 USD | 406,910.00 USD | 87,950.00 USD | 0.00 USD | 251.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 408,700.00 USD | 408,700.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8920` | 1,520,000.00 USD | 1,520,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8930` | 427,520.00 USD | 427,520.00 USD | 0.00 USD | 18,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8940` | 449,090.00 USD | 449,090.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8940` | 2,790,000.00 USD | 2,790,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8950` | 526,940.00 USD | 526,940.00 USD | 0.00 USD | 77,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8960` | 3,490,000.00 USD | 3,490,000.00 USD | 593,680.00 USD | 107,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8970` | 527,900.00 USD | 527,900.00 USD | 969.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8980` | 661,740.00 USD | 661,740.00 USD | 73,030.00 USD | 60,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8980` | 4,570,000.00 USD | 4,570,000.00 USD | 615,200.00 USD | 118,950.00 USD | 339,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8990` | 853,210.00 USD | 853,210.00 USD | 70,970.00 USD | 120,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9000` | 1,020,000.00 USD | 1,020,000.00 USD | 167,020.00 USD | 1,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9000` | 4,780,000.00 USD | 4,780,000.00 USD | 198,040.00 USD | 16,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9010` | 1,160,000.00 USD | 1,160,000.00 USD | 3,390.00 USD | 107,900.00 USD | 24,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 1,230,000.00 USD | 1,230,000.00 USD | 20,120.00 USD | 53,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9020` | 5,560,000.00 USD | 5,560,000.00 USD | 85,610.00 USD | 221,330.00 USD | 476,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9030` | 1,380,000.00 USD | 1,380,000.00 USD | 25,600.00 USD | 108,680.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9040` | 1,690,000.00 USD | 1,690,000.00 USD | 175,130.00 USD | 136,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9040` | 6,010,000.00 USD | 6,010,000.00 USD | 223,750.00 USD | 2,890.00 USD | 218,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9050` | 1,850,000.00 USD | 1,850,000.00 USD | 90,340.00 USD | 26,270.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9060` | 2,350,000.00 USD | 2,350,000.00 USD | 168,180.00 USD | 158,360.00 USD | 165,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9060` | 6,430,000.00 USD | 6,430,000.00 USD | 286,790.00 USD | 34,600.00 USD | 104,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9070` | 2,730,000.00 USD | 2,730,000.00 USD | 135,160.00 USD | 128,180.00 USD | 115,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9080` | 2,900,000.00 USD | 2,900,000.00 USD | 113,830.00 USD | 45,320.00 USD | 17,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9080` | 7,340,000.00 USD | 7,340,000.00 USD | 389,350.00 USD | 288,590.00 USD | 227,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9085` | 383.66 USD | 383.66 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9090` | 3,060,000.00 USD | 3,060,000.00 USD | 76,970.00 USD | 49,730.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 3,240,000.00 USD | 3,240,000.00 USD | 83,550.00 USD | 50,130.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9100` | 7,610,000.00 USD | 7,610,000.00 USD | 123,910.00 USD | 78,920.00 USD | 70,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9110` | 3,380,000.00 USD | 3,380,000.00 USD | 97,650.00 USD | 16,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 3,560,000.00 USD | 3,560,000.00 USD | 32,690.00 USD | 81,230.00 USD | 69,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9120` | 7,910,000.00 USD | 7,910,000.00 USD | 135,210.00 USD | 163,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9130` | 3,730,000.00 USD | 3,730,000.00 USD | 45,950.00 USD | 25,330.00 USD | 92,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 4,090,000.00 USD | 4,090,000.00 USD | 162,940.00 USD | 61,860.00 USD | 142,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9140` | 8,140,000.00 USD | 8,140,000.00 USD | 143,540.00 USD | 83,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 4,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9150` | 4,460,000.00 USD | 4,460,000.00 USD | 109,360.00 USD | 68,860.00 USD | 184,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9160` | 4,670,000.00 USD | 4,670,000.00 USD | 60,590.00 USD | 100,190.00 USD | 52,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9160` | 8,610,000.00 USD | 8,610,000.00 USD | 212,270.00 USD | 84,510.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9170` | 4,830,000.00 USD | 4,830,000.00 USD | 64,160.00 USD | 26,950.00 USD | 67,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9175` | 2,480.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9180` | 4,980,000.00 USD | 4,980,000.00 USD | 26,530.00 USD | 60,340.00 USD | 68,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9180` | 8,900,000.00 USD | 8,900,000.00 USD | 38,590.00 USD | 63,520.00 USD | 187,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9190` | 5,110,000.00 USD | 5,110,000.00 USD | 57,560.00 USD | 16,580.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9195` | 9,200.00 USD | 16,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 5,290,000.00 USD | 5,290,000.00 USD | 65,430.00 USD | 16,940.00 USD | 100,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9200` | 9,490,000.00 USD | 9,490,000.00 USD | 445,890.00 USD | 32,570.00 USD | 114,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9210` | 5,560,000.00 USD | 5,560,000.00 USD | 85,860.00 USD | 61,240.00 USD | 124,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 5,860,000.00 USD | 5,860,000.00 USD | 129,150.00 USD | 32,770.00 USD | 136,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9220` | 9,880,000.00 USD | 9,880,000.00 USD | 6,470.00 USD | 66,370.00 USD | 318,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9230` | 6,180,000.00 USD | 6,180,000.00 USD | 107,110.00 USD | 55,720.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9235` | 209.36 USD | 16,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9240` | 6,490,000.00 USD | 6,490,000.00 USD | 133,310.00 USD | 59,770.00 USD | 117,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9240` | 10,310,000.00 USD | 10,310,000.00 USD | 111,800.00 USD | 62,860.00 USD | 256,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9250` | 6,730,000.00 USD | 6,730,000.00 USD | 132,110.00 USD | 61,310.00 USD | 55,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 6,860,000.00 USD | 6,860,000.00 USD | 3,870.00 USD | 71,300.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9260` | 10,710,000.00 USD | 10,710,000.00 USD | 209,940.00 USD | 97,540.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9270` | 6,960,000.00 USD | 6,960,000.00 USD | 7,220.00 USD | 67,290.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 7,100,000.00 USD | 7,100,000.00 USD | 36,920.00 USD | 30,650.00 USD | 68,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9280` | 10,910,000.00 USD | 10,910,000.00 USD | 121,460.00 USD | 43,320.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9290` | 7,200,000.00 USD | 7,200,000.00 USD | 53,450.00 USD | 2,870.00 USD | 44,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9295` | 1,240.00 USD | 17,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9300` | 7,330,000.00 USD | 7,330,000.00 USD | 5,010.00 USD | 59,350.00 USD | 65,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9300` | 11,380,000.00 USD | 11,380,000.00 USD | 186,110.00 USD | 113,080.00 USD | 168,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9310` | 7,500,000.00 USD | 7,500,000.00 USD | 118,420.00 USD | 16,270.00 USD | 36,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 7,640,000.00 USD | 7,640,000.00 USD | 71,540.00 USD | 28,860.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9320` | 11,500,000.00 USD | 11,500,000.00 USD | 4,410.00 USD | 53,880.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9330` | 7,690,000.00 USD | 7,690,000.00 USD | 24,270.00 USD | 19,640.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9335` | 927.53 USD | 18,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9340` | 7,710,000.00 USD | 7,710,000.00 USD | 1,200.00 USD | 16,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9340` | 11,630,000.00 USD | 11,630,000.00 USD | 50,160.00 USD | 78,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 7,730,000.00 USD | 7,730,000.00 USD | 964.55 USD | 637.37 USD | 19,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9355` | 340.15 USD | 18,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9360` | 7,860,000.00 USD | 7,860,000.00 USD | 48,380.00 USD | 29,620.00 USD | 55,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9360` | 11,770,000.00 USD | 11,770,000.00 USD | 131,450.00 USD | 3,160.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9365` | 478.55 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9370` | 8,130,000.00 USD | 8,130,000.00 USD | 80,470.00 USD | 54,520.00 USD | 135,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9375` | 454.59 USD | 19,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9380` | 8,270,000.00 USD | 8,270,000.00 USD | 15,820.00 USD | 9,200.00 USD | 110,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9380` | 12,130,000.00 USD | 12,130,000.00 USD | 168,030.00 USD | 5,150.00 USD | 179,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 43,080.00 USD | 62,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9390` | 8,310,000.00 USD | 8,310,000.00 USD | 2,230.00 USD | 3,000.00 USD | 34,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 8,410,000.00 USD | 8,410,000.00 USD | 45,080.00 USD | 1,460.00 USD | 56,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 12,470,000.00 USD | 12,470,000.00 USD | 173,610.00 USD | 39,110.00 USD | 129,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 8,440,000.00 USD | 8,440,000.00 USD | 18,300.00 USD | 15,240.00 USD | 616.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 8,470,000.00 USD | 8,470,000.00 USD | 5,130.00 USD | 1,340.00 USD | 24,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 12,540,000.00 USD | 12,540,000.00 USD | 7,320.00 USD | 31,200.00 USD | 37,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9425` | 1,300.00 USD | 64,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9430` | 8,480,000.00 USD | 8,480,000.00 USD | 2,790.00 USD | 2,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 8,550,000.00 USD | 8,550,000.00 USD | 4,930.00 USD | 23,400.00 USD | 46,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 12,770,000.00 USD | 12,770,000.00 USD | 6,180.00 USD | 217,840.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9445` | 103.90 USD | 64,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9450` | 8,670,000.00 USD | 8,670,000.00 USD | 4,850.00 USD | 793.93 USD | 107,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 8,770,000.00 USD | 8,770,000.00 USD | 56,940.00 USD | 26,210.00 USD | 24,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 8,860,000.00 USD | 8,860,000.00 USD | 36,440.00 USD | 24,720.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 9,000,000.00 USD | 9,000,000.00 USD | 55,350.00 USD | 48,320.00 USD | 35,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 78,160.00 USD | 291,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 9,050,000.00 USD | 9,050,000.00 USD | 18,020.00 USD | 14,650.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 9,130,000.00 USD | 9,130,000.00 USD | 7,440.00 USD | 22,120.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 13,740,000.00 USD | 13,740,000.00 USD | 2,840.00 USD | 30,430.00 USD | 375,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 9,340,000.00 USD | 9,340,000.00 USD | 52,590.00 USD | 28,760.00 USD | 128,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 9,420,000.00 USD | 9,420,000.00 USD | 466.70 USD | 155.85 USD | 84,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 87,720.00 USD | 362,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 9,550,000.00 USD | 9,550,000.00 USD | 29,490.00 USD | 27,080.00 USD | 70,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 9,630,000.00 USD | 9,630,000.00 USD | 28,300.00 USD | 24,560.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 14,270,000.00 USD | 14,270,000.00 USD | 13,570.00 USD | 3,670.00 USD | 60,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 9,690,000.00 USD | 9,690,000.00 USD | 21,030.00 USD | 15,610.00 USD | 24,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 9,750,000.00 USD | 9,750,000.00 USD | 20,640.00 USD | 11,590.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 14,350,000.00 USD | 14,350,000.00 USD | 74,460.00 USD | 3,500.00 USD | 2,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 9,770,000.00 USD | 9,770,000.00 USD | 16,640.00 USD | 2,570.00 USD | 692.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 9,830,000.00 USD | 9,830,000.00 USD | 10,110.00 USD | 42,520.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 15,200,000.00 USD | 15,200,000.00 USD | 846,080.00 USD | 1,220.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 9,890,000.00 USD | 9,890,000.00 USD | 33,840.00 USD | 27,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 10,060,000.00 USD | 10,060,000.00 USD | 69,660.00 USD | 23,730.00 USD | 78,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 15,810,000.00 USD | 15,810,000.00 USD | 358,610.00 USD | 118,450.00 USD | 131,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 10,420,000.00 USD | 10,420,000.00 USD | 137,750.00 USD | 51,970.00 USD | 166,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 10,570,000.00 USD | 10,570,000.00 USD | 129,590.00 USD | 13,950.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 17,350,000.00 USD | 17,350,000.00 USD | 715,790.00 USD | 231,300.00 USD | 588,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 10,770,000.00 USD | 10,770,000.00 USD | 112,130.00 USD | 28,520.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 10,980,000.00 USD | 10,980,000.00 USD | 125,880.00 USD | 39,890.00 USD | 49,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 18,920,000.00 USD | 18,920,000.00 USD | 693,720.00 USD | 366,520.00 USD | 508,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 11,100,000.00 USD | 11,100,000.00 USD | 18,690.00 USD | 72,860.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 11,340,000.00 USD | 11,340,000.00 USD | 135,070.00 USD | 55,850.00 USD | 42,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 20,640,000.00 USD | 20,640,000.00 USD | 962,420.00 USD | 245,250.00 USD | 514,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 11,680,000.00 USD | 11,680,000.00 USD | 93,370.00 USD | 53,730.00 USD | 191,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 11,880,000.00 USD | 11,880,000.00 USD | 80,570.00 USD | 13,220.00 USD | 112,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 22,660,000.00 USD | 22,660,000.00 USD | 856,440.00 USD | 625,850.00 USD | 538,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 12,250,000.00 USD | 12,250,000.00 USD | 161,940.00 USD | 72,530.00 USD | 130,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 12,450,000.00 USD | 12,450,000.00 USD | 111,440.00 USD | 39,150.00 USD | 56,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 23,910,000.00 USD | 23,910,000.00 USD | 657,220.00 USD | 324,760.00 USD | 264,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 12,620,000.00 USD | 12,620,000.00 USD | 64,520.00 USD | 27,540.00 USD | 71,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 12,740,000.00 USD | 12,740,000.00 USD | 38,110.00 USD | 36,660.00 USD | 51,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 24,730,000.00 USD | 24,730,000.00 USD | 402,400.00 USD | 197,100.00 USD | 222,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 12,770,000.00 USD | 12,770,000.00 USD | 24,020.00 USD | 1,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 12,830,000.00 USD | 12,830,000.00 USD | 12,150.00 USD | 5,900.00 USD | 47,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 25,300,000.00 USD | 25,300,000.00 USD | 334,930.00 USD | 116,990.00 USD | 124,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 12,970,000.00 USD | 12,970,000.00 USD | 20,270.00 USD | 28,720.00 USD | 84,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9755` | 3,590.00 USD | 67,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 12,970,000.00 USD | 12,970,000.00 USD | 423.77 USD | 370.46 USD | 154.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 26,040,000.00 USD | 26,040,000.00 USD | 182,900.00 USD | 286,070.00 USD | 265,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 13,030,000.00 USD | 13,030,000.00 USD | 4,370.00 USD | 20,600.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 13,150,000.00 USD | 13,150,000.00 USD | 28,530.00 USD | 21,450.00 USD | 70,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 27,090,000.00 USD | 27,090,000.00 USD | 323,530.00 USD | 211,120.00 USD | 513,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 13,210,000.00 USD | 13,210,000.00 USD | 18,030.00 USD | 15,220.00 USD | 32,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 13,370,000.00 USD | 13,370,000.00 USD | 43,300.00 USD | 32,650.00 USD | 81,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 27,640,000.00 USD | 27,640,000.00 USD | 247,060.00 USD | 66,910.00 USD | 240,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 68,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 13,420,000.00 USD | 13,420,000.00 USD | 44,730.00 USD | 4,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 13,460,000.00 USD | 13,460,000.00 USD | 37,830.00 USD | 836.01 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 27,960,000.00 USD | 27,960,000.00 USD | 108,220.00 USD | 68,030.00 USD | 142,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 13,510,000.00 USD | 13,510,000.00 USD | 31,020.00 USD | 21,700.00 USD | 47.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 13,540,000.00 USD | 13,540,000.00 USD | 2,480.00 USD | 22,540.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 28,660,000.00 USD | 28,660,000.00 USD | 397,850.00 USD | 123,740.00 USD | 177,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 13,600,000.00 USD | 13,600,000.00 USD | 19,260.00 USD | 19,940.00 USD | 14,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 13,750,000.00 USD | 13,750,000.00 USD | 51,980.00 USD | 24,590.00 USD | 81,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 29,000,000.00 USD | 29,000,000.00 USD | 108,860.00 USD | 154,250.00 USD | 74,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 69,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9870` | 13,810,000.00 USD | 13,810,000.00 USD | 28,620.00 USD | 9,650.00 USD | 16,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 13,900,000.00 USD | 13,900,000.00 USD | 55,150.00 USD | 11,470.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 29,310,000.00 USD | 29,310,000.00 USD | 209,770.00 USD | 75,650.00 USD | 26,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 73,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9890` | 13,970,000.00 USD | 13,970,000.00 USD | 44,590.00 USD | 15,760.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 29,620,000.00 USD | 29,620,000.00 USD | 201,410.00 USD | 100,430.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9915` | 1,570.00 USD | 75,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9920` | 30,070,000.00 USD | 30,070,000.00 USD | 288,210.00 USD | 79,650.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 75,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9940` | 30,540,000.00 USD | 30,540,000.00 USD | 143,340.00 USD | 183,310.00 USD | 146,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 31,000,000.00 USD | 31,000,000.00 USD | 107,780.00 USD | 55,790.00 USD | 291,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 31,440,000.00 USD | 31,440,000.00 USD | 238,490.00 USD | 42,080.00 USD | 163,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,650,000.00 USD | 31,650,000.00 USD | 94,210.00 USD | 53,610.00 USD | 65,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 75,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,080,000.00 USD | 32,080,000.00 USD | 250,490.00 USD | 49,140.00 USD | 126,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,430,000.00 USD | 32,430,000.00 USD | 148,700.00 USD | 47,010.00 USD | 157,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 5,710.00 USD | 81,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.01` | 705.99 USD | 81,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 82,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.03` | 11,040.00 USD | 93,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 5,810.00 USD | 99,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 104.25 USD | 99,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 99,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 102,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.07` | 1,750.00 USD | 103,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.07` | 1,530.00 USD | 105,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 108,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 114,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 114,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 115,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 8,940.00 USD | 124,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 147,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 148,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 129.88 USD | 148,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.16` | 645.46 USD | 148,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 177.65 USD | 148,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 153,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 383.01 USD | 153,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 154,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 3,930.00 USD | 158,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 160,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 163,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 1,060.00 USD | 164,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 204,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 9,850.00 USD | 213,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 214,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 214,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 215,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 24,040.00 USD | 239,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 7,490.00 USD | 246,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 253,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 275,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 281,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 640,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.38` | 135.86 USD | 640,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 644,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 645,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 16,100.00 USD | 661,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 661,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 21,270.00 USD | 682,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 151.05 USD | 682,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 687,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 9,930.00 USD | 696,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 697,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 697,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,180.00 USD | 698,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 275,850.00 USD | 974,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 123.81 USD | 974,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,130.00 USD | 975,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,190.00 USD | 977,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 999,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 531.15 USD | 999,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 3,940.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 140.06 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 3,620.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,090.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 172.19 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 150.02 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 895.75 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 9,680.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 86,130.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 496.91 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1835` | 4,690,000.00 USD | 0.00 USD | 183.50 USD | `-79.27%` | `1,000.00` |
| `Live` | `Long` | `0.1995` | 4,690,000.00 USD | 0.00 USD | 256.00 USD | `-77.46%` | `1,283.20` |
| `Live` | `Long` | `0.2095` | 4,690,000.00 USD | 0.00 USD | 448.46 USD | `-76.33%` | `2,140.60` |
| `Live` | `Long` | `0.2135` | 4,690,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.88%` | `18,919.90` |
| `Live` | `Long` | `0.2195` | 4,680,000.00 USD | 0.00 USD | 3,130.00 USD | `-75.20%` | `14,245.00` |
| `Live` | `Long` | `0.2295` | 4,680,000.00 USD | 0.00 USD | 229.50 USD | `-74.07%` | `1,000.00` |
| `Live` | `Long` | `0.2355` | 4,680,000.00 USD | 0.00 USD | 1,670.00 USD | `-73.39%` | `7,101.90` |
| `Live` | `Long` | `0.2385` | 4,680,000.00 USD | 0.00 USD | 156.36 USD | `-73.05%` | `655.60` |
| `Live` | `Long` | `0.2415` | 4,680,000.00 USD | 0.00 USD | 1,620.00 USD | `-72.71%` | `6,725.00` |
| `Live` | `Long` | `0.2525` | 4,680,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.47%` | `8,897.00` |
| `Live` | `Long` | `0.2535` | 4,670,000.00 USD | 0.00 USD | 151.36 USD | `-71.36%` | `597.10` |
| `Live` | `Long` | `0.2595` | 4,670,000.00 USD | 0.00 USD | 168.52 USD | `-70.68%` | `649.40` |
| `Live` | `Long` | `0.2605` | 4,670,000.00 USD | 0.00 USD | 2,640.00 USD | `-70.57%` | `10,152.10` |
| `Live` | `Long` | `0.2625` | 4,670,000.00 USD | 0.00 USD | 849.48 USD | `-70.34%` | `3,236.10` |
| `Live` | `Long` | `0.2685` | 4,670,000.00 USD | 0.00 USD | 106.16 USD | `-69.66%` | `395.40` |
| `Live` | `Long` | `0.2735` | 4,670,000.00 USD | 0.00 USD | 248.34 USD | `-69.10%` | `908.00` |
| `Live` | `Long` | `0.2775` | 4,670,000.00 USD | 0.00 USD | 23,900.00 USD | `-68.65%` | `86,117.40` |
| `Live` | `Long` | `0.2885` | 4,650,000.00 USD | 0.00 USD | 29,070.00 USD | `-67.40%` | `100,768.40` |
| `Live` | `Long` | `0.2905` | 4,620,000.00 USD | 0.00 USD | 195.33 USD | `-67.18%` | `672.40` |
| `Live` | `Long` | `0.2925` | 4,620,000.00 USD | 0.00 USD | 340.94 USD | `-66.95%` | `1,165.60` |
| `Live` | `Long` | `0.2975` | 4,620,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.39%` | `14,561.30` |
| `Live` | `Long` | `0.3015` | 4,610,000.00 USD | 0.00 USD | 603.12 USD | `-65.93%` | `2,000.40` |
| `Live` | `Long` | `0.3095` | 4,610,000.00 USD | 0.00 USD | 126.71 USD | `-65.03%` | `409.40` |
| `Live` | `Long` | `0.3115` | 4,610,000.00 USD | 0.00 USD | 270.38 USD | `-64.80%` | `868.00` |
| `Live` | `Long` | `0.3185` | 4,610,000.00 USD | 0.00 USD | 105.39 USD | `-64.01%` | `330.90` |
| `Live` | `Long` | `0.3205` | 4,610,000.00 USD | 0.00 USD | 3,900.00 USD | `-63.79%` | `12,176.00` |
| `Live` | `Long` | `0.3325` | 4,610,000.00 USD | 0.00 USD | 3,330.00 USD | `-62.43%` | `10,000.00` |
| `Live` | `Long` | `0.3395` | 4,600,000.00 USD | 0.00 USD | 9,670.00 USD | `-61.64%` | `28,480.20` |
| `Live` | `Long` | `0.3465` | 4,590,000.00 USD | 0.00 USD | 1,230.00 USD | `-60.85%` | `3,555.40` |
| `Live` | `Long` | `0.3475` | 4,590,000.00 USD | 0.00 USD | 3,850.00 USD | `-60.74%` | `11,077.80` |
| `Live` | `Long` | `0.3505` | 4,590,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.40%` | `2,908.00` |
| `Live` | `Long` | `0.3525` | 4,590,000.00 USD | 0.00 USD | 27,390.00 USD | `-60.17%` | `77,706.40` |
| `Live` | `Long` | `0.3535` | 4,560,000.00 USD | 0.00 USD | 4,390.00 USD | `-60.06%` | `12,426.00` |
| `Live` | `Long` | `0.3585` | 4,560,000.00 USD | 0.00 USD | 595.72 USD | `-59.49%` | `1,661.70` |
| `Live` | `Long` | `0.3665` | 4,560,000.00 USD | 0.00 USD | 274.88 USD | `-58.59%` | `750.00` |
| `Live` | `Long` | `0.3745` | 4,550,000.00 USD | 0.00 USD | 2,050.00 USD | `-57.69%` | `5,481.20` |
| `Live` | `Long` | `0.3765` | 4,550,000.00 USD | 0.00 USD | 6,400.00 USD | `-57.46%` | `17,000.00` |
| `Live` | `Long` | `0.3775` | 4,550,000.00 USD | 0.00 USD | 420.95 USD | `-57.35%` | `1,115.10` |
| `Live` | `Long` | `0.3795` | 4,550,000.00 USD | 0.00 USD | 278.02 USD | `-57.12%` | `732.60` |
| `Live` | `Long` | `0.3845` | 4,550,000.00 USD | 0.00 USD | 2,020.00 USD | `-56.56%` | `5,262.20` |
| `Live` | `Long` | `0.3895` | 4,540,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.99%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 4,540,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.65%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,540,000.00 USD | 0.00 USD | 754.48 USD | `-55.43%` | `1,912.50` |
| `Live` | `Long` | `0.4005` | 4,530,000.00 USD | 0.00 USD | 5,010.00 USD | `-54.75%` | `12,500.00` |
| `Live` | `Long` | `0.4035` | 4,530,000.00 USD | 0.00 USD | 935.03 USD | `-54.41%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,530,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.30%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,520,000.00 USD | 0.00 USD | 3,360.00 USD | `-54.07%` | `8,275.50` |
| `Live` | `Long` | `0.4165` | 4,520,000.00 USD | 0.00 USD | 8,330.00 USD | `-52.94%` | `20,000.00` |
| `Live` | `Long` | `0.4175` | 4,510,000.00 USD | 0.00 USD | 29,230.00 USD | `-52.83%` | `70,000.00` |
| `Live` | `Long` | `0.4215` | 4,480,000.00 USD | 0.00 USD | 3,930.00 USD | `-52.38%` | `9,320.00` |
| `Live` | `Long` | `0.4245` | 4,480,000.00 USD | 0.00 USD | 468.61 USD | `-52.04%` | `1,103.90` |
| `Live` | `Long` | `0.4255` | 4,480,000.00 USD | 0.00 USD | 771.39 USD | `-51.92%` | `1,812.90` |
| `Live` | `Long` | `0.4275` | 4,480,000.00 USD | 0.00 USD | 753.25 USD | `-51.70%` | `1,762.00` |
| `Live` | `Long` | `0.4385` | 4,480,000.00 USD | 0.00 USD | 122.91 USD | `-50.45%` | `280.30` |
| `Live` | `Long` | `0.4435` | 4,480,000.00 USD | 0.00 USD | 44,400.00 USD | `-49.89%` | `100,105.50` |
| `Live` | `Long` | `0.4455` | 4,430,000.00 USD | 0.00 USD | 574.83 USD | `-49.66%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,430,000.00 USD | 0.00 USD | 19,920.00 USD | `-49.55%` | `44,606.00` |
| `Live` | `Long` | `0.4475` | 4,410,000.00 USD | 0.00 USD | 105.25 USD | `-49.44%` | `235.20` |
| `Live` | `Long` | `0.4515` | 4,410,000.00 USD | 0.00 USD | 151.88 USD | `-48.99%` | `336.40` |
| `Live` | `Long` | `0.4535` | 4,410,000.00 USD | 0.00 USD | 1,020.00 USD | `-48.76%` | `2,246.80` |
| `Live` | `Long` | `0.4585` | 4,410,000.00 USD | 0.00 USD | 141.26 USD | `-48.19%` | `308.10` |
| `Live` | `Long` | `0.4595` | 4,410,000.00 USD | 0.00 USD | 3,720.00 USD | `-48.08%` | `8,093.30` |
| `Live` | `Long` | `0.4705` | 4,410,000.00 USD | 0.00 USD | 9,230.00 USD | `-46.84%` | `19,627.90` |
| `Live` | `Long` | `0.4785` | 4,400,000.00 USD | 0.00 USD | 110.10 USD | `-45.93%` | `230.10` |
| `Live` | `Long` | `0.4825` | 4,400,000.00 USD | 0.00 USD | 166.70 USD | `-45.48%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,400,000.00 USD | 0.00 USD | 174.01 USD | `-45.37%` | `359.90` |
| `Live` | `Long` | `0.4845` | 4,400,000.00 USD | 0.00 USD | 3,540.00 USD | `-45.26%` | `7,307.20` |
| `Live` | `Long` | `0.4865` | 4,390,000.00 USD | 0.00 USD | 201.07 USD | `-45.03%` | `413.30` |
| `Live` | `Long` | `0.4895` | 4,390,000.00 USD | 0.00 USD | 646.73 USD | `-44.69%` | `1,321.20` |
| `Live` | `Long` | `0.4915` | 4,390,000.00 USD | 0.00 USD | 2,380.00 USD | `-44.47%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 4,390,000.00 USD | 0.00 USD | 5,690.00 USD | `-44.13%` | `11,505.30` |
| `Live` | `Long` | `0.4955` | 4,380,000.00 USD | 0.00 USD | 211.88 USD | `-44.01%` | `427.60` |
| `Live` | `Long` | `0.4975` | 4,380,000.00 USD | 0.00 USD | 4,730.00 USD | `-43.79%` | `9,500.00` |
| `Live` | `Long` | `0.4985` | 4,380,000.00 USD | 0.00 USD | 216.75 USD | `-43.67%` | `434.80` |
| `Live` | `Long` | `0.5015` | 4,380,000.00 USD | 0.00 USD | 212.49 USD | `-43.34%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,380,000.00 USD | 0.00 USD | 1,230.00 USD | `-43.22%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 4,380,000.00 USD | 0.00 USD | 211.25 USD | `-42.88%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,380,000.00 USD | 0.00 USD | 5,680.00 USD | `-42.54%` | `11,163.80` |
| `Live` | `Long` | `0.5095` | 4,370,000.00 USD | 0.00 USD | 195.75 USD | `-42.43%` | `384.20` |
| `Live` | `Long` | `0.5105` | 4,370,000.00 USD | 0.00 USD | 537.10 USD | `-42.32%` | `1,052.10` |
| `Live` | `Long` | `0.5155` | 4,370,000.00 USD | 0.00 USD | 106.04 USD | `-41.75%` | `205.70` |
| `Live` | `Long` | `0.5165` | 4,370,000.00 USD | 0.00 USD | 619.80 USD | `-41.64%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,370,000.00 USD | 0.00 USD | 1,070.00 USD | `-41.53%` | `2,073.10` |
| `Live` | `Long` | `0.5185` | 4,370,000.00 USD | 0.00 USD | 121.74 USD | `-41.42%` | `234.80` |
| `Live` | `Long` | `0.5205` | 4,370,000.00 USD | 0.00 USD | 1,710.00 USD | `-41.19%` | `3,280.30` |
| `Live` | `Long` | `0.5225` | 4,370,000.00 USD | 0.00 USD | 273.58 USD | `-40.96%` | `523.60` |
| `Live` | `Long` | `0.5255` | 4,370,000.00 USD | 0.00 USD | 7,230.00 USD | `-40.62%` | `13,753.30` |
| `Live` | `Long` | `0.5275` | 4,360,000.00 USD | 0.00 USD | 348.36 USD | `-40.40%` | `660.40` |
| `Live` | `Long` | `0.5295` | 4,360,000.00 USD | 0.00 USD | 123,370.00 USD | `-40.17%` | `233,000.00` |
| `Live` | `Long` | `0.5305` | 4,240,000.00 USD | 0.00 USD | 1,720.00 USD | `-40.06%` | `3,250.50` |
| `Live` | `Long` | `0.5325` | 4,230,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.83%` | `5,038.10` |
| `Live` | `Long` | `0.5335` | 4,230,000.00 USD | 0.00 USD | 7,790.00 USD | `-39.72%` | `14,603.90` |
| `Live` | `Long` | `0.5355` | 4,220,000.00 USD | 0.00 USD | 113.47 USD | `-39.49%` | `211.90` |
| `Live` | `Long` | `0.5365` | 4,220,000.00 USD | 0.00 USD | 252.96 USD | `-39.38%` | `471.50` |
| `Live` | `Long` | `0.5395` | 4,220,000.00 USD | 0.00 USD | 126.46 USD | `-39.04%` | `234.40` |
| `Live` | `Long` | `0.5405` | 4,220,000.00 USD | 0.00 USD | 7,090.00 USD | `-38.93%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,220,000.00 USD | 0.00 USD | 269.13 USD | `-38.70%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,220,000.00 USD | 0.00 USD | 230.32 USD | `-38.48%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,220,000.00 USD | 0.00 USD | 272.87 USD | `-38.25%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,220,000.00 USD | 0.00 USD | 1,240.00 USD | `-38.14%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,210,000.00 USD | 0.00 USD | 28,790.00 USD | `-37.91%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,190,000.00 USD | 0.00 USD | 248.06 USD | `-37.80%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,190,000.00 USD | 0.00 USD | 6,150.00 USD | `-37.69%` | `11,154.50` |
| `Live` | `Long` | `0.5525` | 4,180,000.00 USD | 0.00 USD | 582.56 USD | `-37.57%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,180,000.00 USD | 0.00 USD | 271.88 USD | `-37.46%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,180,000.00 USD | 0.00 USD | 531.60 USD | `-37.35%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,180,000.00 USD | 0.00 USD | 7,950.00 USD | `-37.23%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,170,000.00 USD | 0.00 USD | 141.97 USD | `-36.90%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,170,000.00 USD | 0.00 USD | 618.53 USD | `-36.78%` | `1,105.50` |
| `Live` | `Long` | `0.5615` | 4,170,000.00 USD | 0.00 USD | 442.63 USD | `-36.56%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,170,000.00 USD | 0.00 USD | 330.53 USD | `-36.44%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,170,000.00 USD | 0.00 USD | 4,800.00 USD | `-36.33%` | `8,511.90` |
| `Live` | `Long` | `0.5655` | 4,160,000.00 USD | 0.00 USD | 8,190.00 USD | `-36.10%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,160,000.00 USD | 0.00 USD | 7,200.00 USD | `-35.99%` | `12,714.00` |
| `Live` | `Long` | `0.5675` | 4,150,000.00 USD | 0.00 USD | 1,560.00 USD | `-35.88%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,150,000.00 USD | 0.00 USD | 973.22 USD | `-35.65%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,150,000.00 USD | 0.00 USD | 139.23 USD | `-35.31%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,150,000.00 USD | 0.00 USD | 109,930.00 USD | `-35.20%` | `191,690.40` |
| `Live` | `Long` | `0.5745` | 4,040,000.00 USD | 0.00 USD | 144.03 USD | `-35.09%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,040,000.00 USD | 0.00 USD | 217.37 USD | `-34.97%` | `377.70` |
| `Live` | `Long` | `0.5765` | 4,040,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.86%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,030,000.00 USD | 0.00 USD | 7,350.00 USD | `-34.75%` | `12,723.50` |
| `Live` | `Long` | `0.5795` | 4,030,000.00 USD | 0.00 USD | 81,340.00 USD | `-34.52%` | `140,367.30` |
| `Live` | `Long` | `0.5805` | 3,950,000.00 USD | 0.00 USD | 1,410.00 USD | `-34.41%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 3,940,000.00 USD | 0.00 USD | 6,470.00 USD | `-34.18%` | `11,099.00` |
| `Live` | `Long` | `0.5845` | 3,940,000.00 USD | 0.00 USD | 584.50 USD | `-33.96%` | `1,000.00` |
| `Live` | `Long` | `0.5855` | 3,940,000.00 USD | 0.00 USD | 2,280.00 USD | `-33.84%` | `3,901.10` |
| `Live` | `Long` | `0.5865` | 3,930,000.00 USD | 0.00 USD | 822.98 USD | `-33.73%` | `1,403.20` |
| `Live` | `Long` | `0.5885` | 3,930,000.00 USD | 0.00 USD | 311.14 USD | `-33.51%` | `528.70` |
| `Live` | `Long` | `0.5905` | 3,930,000.00 USD | 0.00 USD | 225.93 USD | `-33.28%` | `382.60` |
| `Live` | `Long` | `0.5935` | 3,930,000.00 USD | 0.00 USD | 1,130.00 USD | `-32.94%` | `1,901.00` |
| `Live` | `Long` | `0.5945` | 3,930,000.00 USD | 0.00 USD | 8,400.00 USD | `-32.83%` | `14,133.50` |
| `Live` | `Long` | `0.5965` | 3,920,000.00 USD | 0.00 USD | 608.61 USD | `-32.60%` | `1,020.30` |
| `Live` | `Long` | `0.5975` | 3,920,000.00 USD | 0.00 USD | 3,420.00 USD | `-32.49%` | `5,729.40` |
| `Live` | `Long` | `0.5985` | 3,920,000.00 USD | 0.00 USD | 840.95 USD | `-32.38%` | `1,405.10` |
| `Live` | `Long` | `0.5995` | 3,920,000.00 USD | 0.00 USD | 4,760.00 USD | `-32.26%` | `7,936.80` |
| `Live` | `Long` | `0.6005` | 3,910,000.00 USD | 0.00 USD | 351.11 USD | `-32.15%` | `584.70` |
| `Live` | `Long` | `0.6015` | 3,910,000.00 USD | 0.00 USD | 323.79 USD | `-32.04%` | `538.30` |
| `Live` | `Long` | `0.6025` | 3,910,000.00 USD | 0.00 USD | 432.35 USD | `-31.92%` | `717.60` |
| `Live` | `Long` | `0.6065` | 3,910,000.00 USD | 0.00 USD | 2,730.00 USD | `-31.47%` | `4,500.00` |
| `Live` | `Long` | `0.6075` | 3,910,000.00 USD | 0.00 USD | 851.05 USD | `-31.36%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 3,910,000.00 USD | 0.00 USD | 886.10 USD | `-31.25%` | `1,456.20` |
| `Live` | `Long` | `0.6095` | 3,910,000.00 USD | 0.00 USD | 214.54 USD | `-31.13%` | `352.00` |
| `Live` | `Long` | `0.6115` | 3,910,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.91%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 3,900,000.00 USD | 0.00 USD | 438.73 USD | `-30.79%` | `716.30` |
| `Live` | `Long` | `0.6135` | 3,900,000.00 USD | 0.00 USD | 112.33 USD | `-30.68%` | `183.10` |
| `Live` | `Long` | `0.6145` | 3,900,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.57%` | `3,435.00` |
| `Live` | `Long` | `0.6155` | 3,900,000.00 USD | 0.00 USD | 935.13 USD | `-30.46%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 3,900,000.00 USD | 0.00 USD | 44,160.00 USD | `-30.34%` | `71,627.40` |
| `Live` | `Long` | `0.6175` | 3,850,000.00 USD | 0.00 USD | 4,980.00 USD | `-30.23%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 3,850,000.00 USD | 0.00 USD | 12,570.00 USD | `-30.12%` | `20,327.90` |
| `Live` | `Long` | `0.6195` | 3,840,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.00%` | `3,868.00` |
| `Live` | `Long` | `0.6225` | 3,830,000.00 USD | 0.00 USD | 708.53 USD | `-29.66%` | `1,138.20` |
| `Live` | `Long` | `0.6245` | 3,830,000.00 USD | 0.00 USD | 356.65 USD | `-29.44%` | `571.10` |
| `Live` | `Long` | `0.6255` | 3,830,000.00 USD | 0.00 USD | 33,460.00 USD | `-29.33%` | `53,492.10` |
| `Live` | `Long` | `0.6285` | 3,800,000.00 USD | 0.00 USD | 102.45 USD | `-28.99%` | `163.00` |
| `Live` | `Long` | `0.6295` | 3,800,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.87%` | `2,073.70` |
| `Live` | `Long` | `0.6305` | 3,800,000.00 USD | 0.00 USD | 319.35 USD | `-28.76%` | `506.50` |
| `Live` | `Long` | `0.6325` | 3,800,000.00 USD | 0.00 USD | 18,210.00 USD | `-28.53%` | `28,791.40` |
| `Live` | `Long` | `0.6345` | 3,780,000.00 USD | 0.00 USD | 843.00 USD | `-28.31%` | `1,328.60` |
| `Live` | `Long` | `0.6365` | 3,780,000.00 USD | 0.00 USD | 3,060.00 USD | `-28.08%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,780,000.00 USD | 0.00 USD | 1,100.00 USD | `-27.97%` | `1,726.70` |
| `Live` | `Long` | `0.6405` | 3,770,000.00 USD | 0.00 USD | 33,040.00 USD | `-27.63%` | `51,581.80` |
| `Live` | `Long` | `0.6415` | 3,740,000.00 USD | 0.00 USD | 86,920.00 USD | `-27.52%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,650,000.00 USD | 0.00 USD | 477.63 USD | `-27.40%` | `743.40` |
| `Live` | `Long` | `0.6435` | 3,650,000.00 USD | 0.00 USD | 3,190.00 USD | `-27.29%` | `4,951.30` |
| `Live` | `Long` | `0.6445` | 3,650,000.00 USD | 0.00 USD | 65,790.00 USD | `-27.18%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,590,000.00 USD | 0.00 USD | 14,590.00 USD | `-27.07%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,570,000.00 USD | 0.00 USD | 146.76 USD | `-26.95%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,570,000.00 USD | 0.00 USD | 2,810.00 USD | `-26.84%` | `4,340.10` |
| `Live` | `Long` | `0.6485` | 3,570,000.00 USD | 0.00 USD | 3,290.00 USD | `-26.73%` | `5,076.00` |
| `Live` | `Long` | `0.6495` | 3,560,000.00 USD | 0.00 USD | 344.82 USD | `-26.61%` | `530.90` |
| `Live` | `Long` | `0.6505` | 3,560,000.00 USD | 0.00 USD | 106.75 USD | `-26.50%` | `164.10` |
| `Live` | `Long` | `0.6515` | 3,560,000.00 USD | 0.00 USD | 403,320.00 USD | `-26.39%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,160,000.00 USD | 0.00 USD | 2,350.00 USD | `-26.27%` | `3,599.00` |
| `Live` | `Long` | `0.6535` | 3,160,000.00 USD | 0.00 USD | 2,840.00 USD | `-26.16%` | `4,345.80` |
| `Live` | `Long` | `0.6545` | 3,160,000.00 USD | 0.00 USD | 7,850.00 USD | `-26.05%` | `11,993.00` |
| `Live` | `Long` | `0.6555` | 3,150,000.00 USD | 0.00 USD | 7,360.00 USD | `-25.94%` | `11,232.10` |
| `Live` | `Long` | `0.6565` | 3,140,000.00 USD | 0.00 USD | 7,070.00 USD | `-25.82%` | `10,764.20` |
| `Live` | `Long` | `0.6575` | 3,130,000.00 USD | 0.00 USD | 13,280.00 USD | `-25.71%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,120,000.00 USD | 0.00 USD | 2,970.00 USD | `-25.60%` | `4,508.30` |
| `Live` | `Long` | `0.6595` | 3,120,000.00 USD | 0.00 USD | 1,200.00 USD | `-25.48%` | `1,827.00` |
| `Live` | `Long` | `0.6615` | 3,120,000.00 USD | 0.00 USD | 4,960.00 USD | `-25.26%` | `7,503.30` |
| `Live` | `Long` | `0.6625` | 3,110,000.00 USD | 0.00 USD | 4,840.00 USD | `-25.14%` | `7,306.80` |
| `Live` | `Long` | `0.6645` | 3,110,000.00 USD | 0.00 USD | 1,190.00 USD | `-24.92%` | `1,794.80` |
| `Live` | `Long` | `0.6665` | 3,100,000.00 USD | 0.00 USD | 528.73 USD | `-24.69%` | `793.30` |
| `Live` | `Long` | `0.6675` | 3,100,000.00 USD | 0.00 USD | 2,260.00 USD | `-24.58%` | `3,386.00` |
| `Live` | `Long` | `0.6685` | 3,100,000.00 USD | 0.00 USD | 5,670.00 USD | `-24.47%` | `8,488.90` |
| `Live` | `Long` | `0.6705` | 3,100,000.00 USD | 0.00 USD | 2,630.00 USD | `-24.24%` | `3,915.40` |
| `Live` | `Long` | `0.6715` | 3,090,000.00 USD | 0.00 USD | 2,240.00 USD | `-24.13%` | `3,341.20` |
| `Live` | `Long` | `0.6725` | 3,090,000.00 USD | 0.00 USD | 1,280.00 USD | `-24.01%` | `1,906.60` |
| `Live` | `Long` | `0.6735` | 3,090,000.00 USD | 0.00 USD | 27,680.00 USD | `-23.90%` | `41,094.80` |
| `Live` | `Long` | `0.6745` | 3,060,000.00 USD | 0.00 USD | 6,520.00 USD | `-23.79%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 3,060,000.00 USD | 0.00 USD | 387.20 USD | `-23.68%` | `573.20` |
| `Live` | `Long` | `0.6765` | 3,060,000.00 USD | 0.00 USD | 744.15 USD | `-23.56%` | `1,100.00` |
| `Live` | `Long` | `0.6775` | 3,060,000.00 USD | 0.00 USD | 2,370.00 USD | `-23.45%` | `3,500.00` |
| `Live` | `Long` | `0.6785` | 3,050,000.00 USD | 0.00 USD | 122.94 USD | `-23.34%` | `181.20` |
| `Live` | `Long` | `0.6795` | 3,050,000.00 USD | 0.00 USD | 43,650.00 USD | `-23.22%` | `64,238.50` |
| `Live` | `Long` | `0.6825` | 3,010,000.00 USD | 0.00 USD | 19,300.00 USD | `-22.88%` | `28,284.70` |
| `Live` | `Long` | `0.6835` | 2,990,000.00 USD | 0.00 USD | 15,130.00 USD | `-22.77%` | `22,136.50` |
| `Live` | `Long` | `0.6845` | 2,970,000.00 USD | 0.00 USD | 5,960.00 USD | `-22.66%` | `8,711.60` |
| `Live` | `Long` | `0.6865` | 2,970,000.00 USD | 0.00 USD | 112.59 USD | `-22.43%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,970,000.00 USD | 0.00 USD | 6,110.00 USD | `-22.32%` | `8,883.90` |
| `Live` | `Long` | `0.6885` | 2,960,000.00 USD | 0.00 USD | 192.16 USD | `-22.21%` | `279.10` |
| `Live` | `Long` | `0.6895` | 2,960,000.00 USD | 0.00 USD | 3,170.00 USD | `-22.09%` | `4,601.40` |
| `Live` | `Long` | `0.6905` | 2,960,000.00 USD | 0.00 USD | 3,360.00 USD | `-21.98%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,960,000.00 USD | 0.00 USD | 8,970.00 USD | `-21.87%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 2,950,000.00 USD | 0.00 USD | 3,600.00 USD | `-21.64%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 2,940,000.00 USD | 0.00 USD | 722.28 USD | `-21.53%` | `1,040.00` |
| `Live` | `Long` | `0.6955` | 2,940,000.00 USD | 0.00 USD | 1,700.00 USD | `-21.42%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,940,000.00 USD | 0.00 USD | 273.03 USD | `-21.30%` | `392.00` |
| `Live` | `Long` | `0.6975` | 2,940,000.00 USD | 0.00 USD | 1,030.00 USD | `-21.19%` | `1,482.80` |
| `Live` | `Long` | `0.6985` | 2,940,000.00 USD | 0.00 USD | 4,830.00 USD | `-21.08%` | `6,919.90` |
| `Live` | `Long` | `0.7005` | 2,930,000.00 USD | 0.00 USD | 235.37 USD | `-20.85%` | `336.00` |
| `Live` | `Long` | `0.7015` | 2,930,000.00 USD | 0.00 USD | 1,990.00 USD | `-20.74%` | `2,841.50` |
| `Live` | `Long` | `0.7025` | 2,930,000.00 USD | 0.00 USD | 39,470.00 USD | `-20.63%` | `56,186.20` |
| `Live` | `Long` | `0.7045` | 2,890,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.40%` | `12,729.60` |
| `Live` | `Long` | `0.7055` | 2,880,000.00 USD | 0.00 USD | 141.38 USD | `-20.29%` | `200.40` |
| `Live` | `Long` | `0.7065` | 2,880,000.00 USD | 0.00 USD | 143.14 USD | `-20.17%` | `202.60` |
| `Live` | `Long` | `0.7075` | 2,880,000.00 USD | 0.00 USD | 1,560.00 USD | `-20.06%` | `2,202.70` |
| `Live` | `Long` | `0.7085` | 2,880,000.00 USD | 0.00 USD | 2,020.00 USD | `-19.95%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,880,000.00 USD | 0.00 USD | 1,140.00 USD | `-19.83%` | `1,603.50` |
| `Live` | `Long` | `0.7105` | 2,880,000.00 USD | 0.00 USD | 4,190.00 USD | `-19.72%` | `5,890.40` |
| `Live` | `Long` | `0.7125` | 2,870,000.00 USD | 0.00 USD | 639.47 USD | `-19.50%` | `897.50` |
| `Live` | `Long` | `0.7135` | 2,870,000.00 USD | 0.00 USD | 927.55 USD | `-19.38%` | `1,300.00` |
| `Live` | `Long` | `0.7155` | 2,870,000.00 USD | 0.00 USD | 11,030.00 USD | `-19.16%` | `15,416.10` |
| `Live` | `Long` | `0.7165` | 2,860,000.00 USD | 0.00 USD | 4,620.00 USD | `-19.04%` | `6,444.00` |
| `Live` | `Long` | `0.7185` | 2,860,000.00 USD | 0.00 USD | 126.96 USD | `-18.82%` | `176.70` |
| `Live` | `Long` | `0.7195` | 2,860,000.00 USD | 0.00 USD | 420.19 USD | `-18.70%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,860,000.00 USD | 0.00 USD | 8,450.00 USD | `-18.48%` | `11,706.20` |
| `Live` | `Long` | `0.7225` | 2,850,000.00 USD | 0.00 USD | 1,420.00 USD | `-18.37%` | `1,965.70` |
| `Live` | `Long` | `0.7235` | 2,850,000.00 USD | 0.00 USD | 8,480.00 USD | `-18.25%` | `11,721.50` |
| `Live` | `Long` | `0.7245` | 2,840,000.00 USD | 0.00 USD | 2,520.00 USD | `-18.14%` | `3,475.80` |
| `Live` | `Long` | `0.7255` | 2,840,000.00 USD | 0.00 USD | 311.60 USD | `-18.03%` | `429.50` |
| `Live` | `Long` | `0.7265` | 2,840,000.00 USD | 0.00 USD | 3,410.00 USD | `-17.91%` | `4,687.00` |
| `Live` | `Long` | `0.7275` | 2,830,000.00 USD | 0.00 USD | 39,490.00 USD | `-17.80%` | `54,282.40` |
| `Live` | `Long` | `0.7285` | 2,790,000.00 USD | 0.00 USD | 424.86 USD | `-17.69%` | `583.20` |
| `Live` | `Long` | `0.7295` | 2,790,000.00 USD | 0.00 USD | 375.98 USD | `-17.57%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,790,000.00 USD | 0.00 USD | 119.88 USD | `-17.46%` | `164.10` |
| `Live` | `Long` | `0.7315` | 2,790,000.00 USD | 0.00 USD | 529.39 USD | `-17.35%` | `723.70` |
| `Live` | `Long` | `0.7325` | 2,790,000.00 USD | 0.00 USD | 907.93 USD | `-17.24%` | `1,239.50` |
| `Live` | `Long` | `0.7335` | 2,790,000.00 USD | 0.00 USD | 448,360.00 USD | `-17.12%` | `611,261.30` |
| `Live` | `Long` | `0.7345` | 2,340,000.00 USD | 0.00 USD | 6,240.00 USD | `-17.01%` | `8,498.00` |
| `Live` | `Long` | `0.7355` | 2,340,000.00 USD | 0.00 USD | 51,920.00 USD | `-16.90%` | `70,595.50` |
| `Live` | `Long` | `0.7375` | 2,280,000.00 USD | 0.00 USD | 3,450.00 USD | `-16.67%` | `4,683.00` |
| `Live` | `Long` | `0.7385` | 2,280,000.00 USD | 0.00 USD | 6,020.00 USD | `-16.56%` | `8,146.50` |
| `Live` | `Long` | `0.7395` | 2,270,000.00 USD | 0.00 USD | 3,380.00 USD | `-16.44%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,270,000.00 USD | 0.00 USD | 3,530.00 USD | `-16.33%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,270,000.00 USD | 0.00 USD | 382.61 USD | `-16.22%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,270,000.00 USD | 0.00 USD | 2,280.00 USD | `-16.11%` | `3,074.90` |
| `Live` | `Long` | `0.7435` | 2,260,000.00 USD | 0.00 USD | 783,980.00 USD | `-15.99%` | `1,054,441.80` |
| `Live` | `Long` | `0.7455` | 1,480,000.00 USD | 0.00 USD | 2,160.00 USD | `-15.77%` | `2,892.60` |
| `Live` | `Long` | `0.7465` | 1,480,000.00 USD | 0.00 USD | 359.96 USD | `-15.65%` | `482.20` |
| `Live` | `Long` | `0.7475` | 1,480,000.00 USD | 0.00 USD | 107,260.00 USD | `-15.54%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,370,000.00 USD | 0.00 USD | 599.60 USD | `-15.31%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,370,000.00 USD | 0.00 USD | 1,210.00 USD | `-15.09%` | `1,613.50` |
| `Live` | `Long` | `0.7535` | 1,370,000.00 USD | 0.00 USD | 569.50 USD | `-14.86%` | `755.80` |
| `Live` | `Long` | `0.7545` | 1,370,000.00 USD | 0.00 USD | 922.07 USD | `-14.75%` | `1,222.10` |
| `Live` | `Long` | `0.7555` | 1,370,000.00 USD | 0.00 USD | 2,070.00 USD | `-14.64%` | `2,744.00` |
| `Live` | `Long` | `0.7575` | 1,370,000.00 USD | 0.00 USD | 1,900.00 USD | `-14.41%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,360,000.00 USD | 0.00 USD | 40,520.00 USD | `-14.30%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,320,000.00 USD | 0.00 USD | 7,810.00 USD | `-14.18%` | `10,288.50` |
| `Live` | `Long` | `0.7615` | 1,320,000.00 USD | 0.00 USD | 351.43 USD | `-13.96%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,320,000.00 USD | 0.00 USD | 859.11 USD | `-13.85%` | `1,126.70` |
| `Live` | `Long` | `0.7635` | 1,310,000.00 USD | 0.00 USD | 782.36 USD | `-13.73%` | `1,024.70` |
| `Live` | `Long` | `0.7645` | 1,310,000.00 USD | 0.00 USD | 1,060.00 USD | `-13.62%` | `1,384.30` |
| `Live` | `Long` | `0.7655` | 1,310,000.00 USD | 0.00 USD | 2,740.00 USD | `-13.51%` | `3,585.10` |
| `Live` | `Long` | `0.7665` | 1,310,000.00 USD | 0.00 USD | 2,950.00 USD | `-13.39%` | `3,852.60` |
| `Live` | `Long` | `0.7675` | 1,310,000.00 USD | 0.00 USD | 24,420.00 USD | `-13.28%` | `31,823.60` |
| `Live` | `Long` | `0.7685` | 1,280,000.00 USD | 0.00 USD | 6,600.00 USD | `-13.17%` | `8,589.60` |
| `Live` | `Long` | `0.7695` | 1,280,000.00 USD | 0.00 USD | 144,250.00 USD | `-13.05%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 1,130,000.00 USD | 0.00 USD | 5,640.00 USD | `-12.94%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 1,130,000.00 USD | 0.00 USD | 19,250.00 USD | `-12.83%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 1,110,000.00 USD | 0.00 USD | 1,940.00 USD | `-12.72%` | `2,515.50` |
| `Live` | `Long` | `0.7735` | 1,100,000.00 USD | 0.00 USD | 5,230.00 USD | `-12.60%` | `6,756.40` |
| `Live` | `Long` | `0.7755` | 1,100,000.00 USD | 0.00 USD | 324,090.00 USD | `-12.38%` | `417,913.70` |
| `Live` | `Long` | `0.7765` | 775,260.00 USD | 0.00 USD | 2,930.00 USD | `-12.26%` | `3,768.50` |
| `Live` | `Long` | `0.7785` | 772,330.00 USD | 0.00 USD | 28,010.00 USD | `-12.04%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 744,320.00 USD | 0.00 USD | 338.69 USD | `-11.92%` | `434.50` |
| `Live` | `Long` | `0.7815` | 743,980.00 USD | 0.00 USD | 4,160.00 USD | `-11.70%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 739,820.00 USD | 0.00 USD | 21,600.00 USD | `-11.47%` | `27,572.80` |
| `Live` | `Long` | `0.7845` | 718,220.00 USD | 0.00 USD | 155.96 USD | `-11.36%` | `198.80` |
| `Live` | `Long` | `0.7865` | 718,060.00 USD | 0.00 USD | 3,470.00 USD | `-11.13%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 714,590.00 USD | 0.00 USD | 288.70 USD | `-11.02%` | `366.60` |
| `Live` | `Long` | `0.7905` | 714,300.00 USD | 0.00 USD | 3,160.00 USD | `-10.68%` | `4,000.00` |
| `Live` | `Long` | `0.7915` | 711,140.00 USD | 0.00 USD | 11,600.00 USD | `-10.57%` | `14,657.80` |
| `Live` | `Long` | `0.7925` | 699,540.00 USD | 0.00 USD | 3,800.00 USD | `-10.46%` | `4,789.00` |
| `Live` | `Long` | `0.7935` | 695,740.00 USD | 0.00 USD | 809.45 USD | `-10.34%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 694,930.00 USD | 0.00 USD | 736.66 USD | `-10.23%` | `927.20` |
| `Live` | `Long` | `0.7955` | 694,190.00 USD | 0.00 USD | 52,610.00 USD | `-10.12%` | `66,134.90` |
| `Live` | `Long` | `0.7965` | 641,580.00 USD | 0.00 USD | 12,980.00 USD | `-10.00%` | `16,300.50` |
| `Live` | `Long` | `0.7975` | 628,600.00 USD | 0.00 USD | 7,460.00 USD | `-9.89%` | `9,359.90` |
| `Live` | `Long` | `0.7985` | 621,140.00 USD | 0.00 USD | 40,230.00 USD | `-9.78%` | `50,386.80` |
| `Live` | `Long` | `0.7995` | 580,900.00 USD | 0.00 USD | 4,220.00 USD | `-9.67%` | `5,276.70` |
| `Live` | `Long` | `0.8005` | 576,680.00 USD | 0.00 USD | 7,110.00 USD | `-9.55%` | `8,879.30` |
| `Live` | `Long` | `0.8015` | 569,580.00 USD | 0.00 USD | 6,710.00 USD | `-9.44%` | `8,367.40` |
| `Live` | `Long` | `0.8025` | 562,870.00 USD | 0.00 USD | 1,350.00 USD | `-9.33%` | `1,686.70` |
| `Live` | `Long` | `0.8035` | 561,520.00 USD | 0.00 USD | 7,790.00 USD | `-9.21%` | `9,698.20` |
| `Live` | `Long` | `0.8045` | 553,720.00 USD | 0.00 USD | 15,720.00 USD | `-9.10%` | `19,542.50` |
| `Live` | `Long` | `0.8055` | 538,000.00 USD | 0.00 USD | 361.11 USD | `-8.99%` | `448.30` |
| `Live` | `Long` | `0.8065` | 537,640.00 USD | 0.00 USD | 6,910.00 USD | `-8.87%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 530,730.00 USD | 0.00 USD | 2,770.00 USD | `-8.76%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 527,960.00 USD | 0.00 USD | 22,170.00 USD | `-8.65%` | `27,427.20` |
| `Live` | `Long` | `0.8095` | 505,790.00 USD | 0.00 USD | 130,110.00 USD | `-8.54%` | `160,732.40` |
| `Live` | `Long` | `0.8105` | 375,670.00 USD | 0.00 USD | 7,750.00 USD | `-8.42%` | `9,562.60` |
| `Live` | `Long` | `0.8115` | 367,920.00 USD | 0.00 USD | 2,970.00 USD | `-8.31%` | `3,654.30` |
| `Live` | `Long` | `0.8125` | 364,960.00 USD | 0.00 USD | 1,160.00 USD | `-8.20%` | `1,421.60` |
| `Live` | `Long` | `0.8135` | 363,800.00 USD | 0.00 USD | 3,800.00 USD | `-8.08%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 360,000.00 USD | 0.00 USD | 277.42 USD | `-7.97%` | `340.60` |
| `Live` | `Long` | `0.8155` | 359,720.00 USD | 0.00 USD | 2,810.00 USD | `-7.86%` | `3,447.40` |
| `Live` | `Long` | `0.8165` | 356,910.00 USD | 0.00 USD | 104.92 USD | `-7.74%` | `128.50` |
| `Live` | `Long` | `0.8175` | 356,800.00 USD | 0.00 USD | 77,840.00 USD | `-7.63%` | `95,214.30` |
| `Live` | `Long` | `0.8185` | 278,970.00 USD | 0.00 USD | 24,130.00 USD | `-7.52%` | `29,480.00` |
| `Live` | `Long` | `0.8195` | 254,840.00 USD | 0.00 USD | 1,720.00 USD | `-7.41%` | `2,098.80` |
| `Live` | `Long` | `0.8205` | 253,120.00 USD | 0.00 USD | 1,400.00 USD | `-7.29%` | `1,706.20` |
| `Live` | `Long` | `0.8215` | 251,720.00 USD | 0.00 USD | 474.01 USD | `-7.18%` | `577.00` |
| `Live` | `Long` | `0.8225` | 251,240.00 USD | 0.00 USD | 1,490.00 USD | `-7.07%` | `1,805.60` |
| `Live` | `Long` | `0.8235` | 249,760.00 USD | 0.00 USD | 1,870.00 USD | `-6.95%` | `2,274.90` |
| `Live` | `Long` | `0.8245` | 247,890.00 USD | 0.00 USD | 20,280.00 USD | `-6.84%` | `24,598.50` |
| `Live` | `Long` | `0.8255` | 227,600.00 USD | 0.00 USD | 1,580.00 USD | `-6.73%` | `1,911.90` |
| `Live` | `Long` | `0.8275` | 226,030.00 USD | 0.00 USD | 4,690.00 USD | `-6.50%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 221,340.00 USD | 0.00 USD | 120,070.00 USD | `-6.39%` | `144,926.90` |
| `Live` | `Long` | `0.8345` | 101,270.00 USD | 0.00 USD | 5,750.00 USD | `-5.71%` | `6,885.20` |
| `Live` | `Long` | `0.8375` | 95,520.00 USD | 0.00 USD | 327.21 USD | `-5.37%` | `390.70` |
| `Live` | `Long` | `0.8385` | 95,190.00 USD | 0.00 USD | 7,300.00 USD | `-5.26%` | `8,701.00` |
| `Live` | `Long` | `0.8415` | 87,900.00 USD | 0.00 USD | 134.47 USD | `-4.92%` | `159.80` |
| `Live` | `Long` | `0.8425` | 87,760.00 USD | 0.00 USD | 11,390.00 USD | `-4.81%` | `13,521.40` |
| `Live` | `Long` | `0.8435` | 76,370.00 USD | 0.00 USD | 103.24 USD | `-4.69%` | `122.40` |
| `Live` | `Long` | `0.8445` | 76,270.00 USD | 0.00 USD | 803.20 USD | `-4.58%` | `951.10` |
| `Live` | `Long` | `0.8455` | 75,470.00 USD | 0.00 USD | 10,690.00 USD | `-4.47%` | `12,645.90` |
| `Live` | `Long` | `0.8465` | 64,770.00 USD | 0.00 USD | 284.68 USD | `-4.35%` | `336.30` |
| `Live` | `Long` | `0.8475` | 64,490.00 USD | 0.00 USD | 1,270.00 USD | `-4.24%` | `1,493.20` |
| `Live` | `Long` | `0.8495` | 63,220.00 USD | 0.00 USD | 6,910.00 USD | `-4.02%` | `8,134.60` |
| `Live` | `Long` | `0.8505` | 56,310.00 USD | 0.00 USD | 13,600.00 USD | `-3.90%` | `15,990.30` |
| `Live` | `Long` | `0.8525` | 42,710.00 USD | 0.00 USD | 42,610.00 USD | `-3.68%` | `49,980.80` |
| `Live` | `Long` | `0.8535` | 104.30 USD | 0.00 USD | 104.30 USD | `-3.56%` | `122.20` |
| `Live` | `Short` | `0.9085` | 383.66 USD | 383.66 USD | 0.00 USD | `+2.65%` | `422.30` |
| `Live` | `Short` | `0.9145` | 4,450.00 USD | 4,060.00 USD | 0.00 USD | `+3.33%` | `4,444.10` |
| `Live` | `Short` | `0.9175` | 6,930.00 USD | 2,480.00 USD | 0.00 USD | `+3.67%` | `2,707.70` |
| `Live` | `Short` | `0.9195` | 16,130.00 USD | 9,200.00 USD | 0.00 USD | `+3.89%` | `10,000.00` |
| `Live` | `Short` | `0.9235` | 16,340.00 USD | 209.36 USD | 0.00 USD | `+4.35%` | `226.70` |
| `Live` | `Short` | `0.9295` | 17,580.00 USD | 1,240.00 USD | 0.00 USD | `+5.02%` | `1,337.00` |
| `Live` | `Short` | `0.9335` | 18,510.00 USD | 927.53 USD | 0.00 USD | `+5.48%` | `993.60` |
| `Live` | `Short` | `0.9355` | 18,850.00 USD | 340.15 USD | 0.00 USD | `+5.70%` | `363.60` |
| `Live` | `Short` | `0.9365` | 19,330.00 USD | 478.55 USD | 0.00 USD | `+5.81%` | `511.00` |
| `Live` | `Short` | `0.9375` | 19,780.00 USD | 454.59 USD | 0.00 USD | `+5.93%` | `484.90` |
| `Live` | `Short` | `0.9385` | 62,860.00 USD | 43,080.00 USD | 0.00 USD | `+6.04%` | `45,903.60` |
| `Live` | `Short` | `0.9425` | 64,170.00 USD | 1,300.00 USD | 0.00 USD | `+6.49%` | `1,384.40` |
| `Live` | `Short` | `0.9445` | 64,270.00 USD | 103.90 USD | 0.00 USD | `+6.72%` | `110.00` |
| `Live` | `Short` | `0.9755` | 67,860.00 USD | 3,590.00 USD | 0.00 USD | `+10.22%` | `3,680.60` |
| `Live` | `Short` | `0.9805` | 68,910.00 USD | 1,050.00 USD | 0.00 USD | `+10.79%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 69,270.00 USD | 365.70 USD | 0.00 USD | `+11.46%` | `370.70` |
| `Live` | `Short` | `0.9885` | 73,530.00 USD | 4,250.00 USD | 0.00 USD | `+11.69%` | `4,304.30` |
| `Live` | `Short` | `0.9915` | 75,100.00 USD | 1,570.00 USD | 0.00 USD | `+12.03%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 75,240.00 USD | 139.59 USD | 0.00 USD | `+12.25%` | `140.50` |
| `Live` | `Short` | `1.00` | 75,570.00 USD | 330.29 USD | 0.00 USD | `+13.16%` | `329.80` |
| `Live` | `Short` | `1.01` | 81,280.00 USD | 5,710.00 USD | 0.00 USD | `+14.51%` | `5,629.50` |
| `Live` | `Short` | `1.01` | 81,980.00 USD | 705.99 USD | 0.00 USD | `+14.63%` | `695.90` |
| `Live` | `Short` | `1.02` | 82,150.00 USD | 170.40 USD | 0.00 USD | `+14.74%` | `167.80` |
| `Live` | `Short` | `1.03` | 93,190.00 USD | 11,040.00 USD | 0.00 USD | `+16.32%` | `10,723.80` |
| `Live` | `Short` | `1.04` | 99,010.00 USD | 5,810.00 USD | 0.00 USD | `+17.11%` | `5,609.70` |
| `Live` | `Short` | `1.04` | 99,110.00 USD | 104.25 USD | 0.00 USD | `+17.79%` | `100.00` |
| `Live` | `Short` | `1.05` | 99,710.00 USD | 597.52 USD | 0.00 USD | `+18.70%` | `568.80` |
| `Live` | `Short` | `1.05` | 102,100.00 USD | 2,390.00 USD | 0.00 USD | `+18.81%` | `2,272.10` |
| `Live` | `Short` | `1.07` | 103,850.00 USD | 1,750.00 USD | 0.00 USD | `+20.50%` | `1,639.00` |
| `Live` | `Short` | `1.07` | 105,380.00 USD | 1,530.00 USD | 0.00 USD | `+21.18%` | `1,429.60` |
| `Live` | `Short` | `1.08` | 108,960.00 USD | 3,580.00 USD | 0.00 USD | `+22.08%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 114,510.00 USD | 5,550.00 USD | 0.00 USD | `+23.10%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 114,840.00 USD | 324.90 USD | 0.00 USD | `+24.23%` | `295.50` |
| `Live` | `Short` | `1.10` | 115,120.00 USD | 277.22 USD | 0.00 USD | `+24.34%` | `251.90` |
| `Live` | `Short` | `1.11` | 124,050.00 USD | 8,940.00 USD | 0.00 USD | `+25.47%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 147,360.00 USD | 23,310.00 USD | 0.00 USD | `+27.28%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 148,000.00 USD | 634.09 USD | 0.00 USD | `+27.96%` | `559.90` |
| `Live` | `Short` | `1.15` | 148,130.00 USD | 129.88 USD | 0.00 USD | `+30.33%` | `112.60` |
| `Live` | `Short` | `1.16` | 148,770.00 USD | 645.46 USD | 0.00 USD | `+30.56%` | `558.60` |
| `Live` | `Short` | `1.20` | 148,950.00 USD | 177.65 USD | 0.00 USD | `+35.53%` | `148.10` |
| `Live` | `Short` | `1.22` | 153,390.00 USD | 4,440.00 USD | 0.00 USD | `+37.68%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 153,770.00 USD | 383.01 USD | 0.00 USD | `+38.13%` | `313.30` |
| `Live` | `Short` | `1.23` | 154,160.00 USD | 380.84 USD | 0.00 USD | `+39.49%` | `308.50` |
| `Live` | `Short` | `1.24` | 158,080.00 USD | 3,930.00 USD | 0.00 USD | `+40.05%` | `3,169.40` |
| `Live` | `Short` | `1.26` | 160,750.00 USD | 2,670.00 USD | 0.00 USD | `+42.31%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 163,060.00 USD | 2,300.00 USD | 0.00 USD | `+44.34%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 164,120.00 USD | 1,060.00 USD | 0.00 USD | `+44.80%` | `826.40` |
| `Live` | `Short` | `1.28` | 204,000.00 USD | 39,880.00 USD | 0.00 USD | `+44.91%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 213,850.00 USD | 9,850.00 USD | 0.00 USD | `+46.04%` | `7,618.00` |
| `Live` | `Short` | `1.29` | 214,070.00 USD | 226.80 USD | 0.00 USD | `+46.26%` | `175.20` |
| `Live` | `Short` | `1.30` | 214,190.00 USD | 114.40 USD | 0.00 USD | `+46.72%` | `88.10` |
| `Live` | `Short` | `1.31` | 215,200.00 USD | 1,020.00 USD | 0.00 USD | `+47.96%` | `777.20` |
| `Live` | `Short` | `1.31` | 239,250.00 USD | 24,040.00 USD | 0.00 USD | `+48.19%` | `18,332.80` |
| `Live` | `Short` | `1.31` | 246,740.00 USD | 7,490.00 USD | 0.00 USD | `+48.30%` | `5,709.60` |
| `Live` | `Short` | `1.33` | 253,080.00 USD | 6,340.00 USD | 0.00 USD | `+49.77%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 275,050.00 USD | 21,970.00 USD | 0.00 USD | `+50.11%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 281,900.00 USD | 6,860.00 USD | 0.00 USD | `+51.35%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 640,190.00 USD | 358,280.00 USD | 0.00 USD | `+55.08%` | `261,043.60` |
| `Live` | `Short` | `1.38` | 640,320.00 USD | 135.86 USD | 0.00 USD | `+56.32%` | `98.20` |
| `Live` | `Short` | `1.41` | 644,770.00 USD | 4,450.00 USD | 0.00 USD | `+59.82%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 645,170.00 USD | 402.08 USD | 0.00 USD | `+62.31%` | `279.90` |
| `Live` | `Short` | `1.44` | 661,270.00 USD | 16,100.00 USD | 0.00 USD | `+62.65%` | `11,182.60` |
| `Live` | `Short` | `1.44` | 661,560.00 USD | 288.68 USD | 0.00 USD | `+62.76%` | `200.40` |
| `Live` | `Short` | `1.47` | 682,830.00 USD | 21,270.00 USD | 0.00 USD | `+66.49%` | `14,437.60` |
| `Live` | `Short` | `1.51` | 682,980.00 USD | 151.05 USD | 0.00 USD | `+70.67%` | `100.00` |
| `Live` | `Short` | `1.51` | 687,000.00 USD | 4,020.00 USD | 0.00 USD | `+71.12%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 696,930.00 USD | 9,930.00 USD | 0.00 USD | `+72.93%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 697,080.00 USD | 144.34 USD | 0.00 USD | `+73.49%` | `94.00` |
| `Live` | `Short` | `1.58` | 697,360.00 USD | 285.21 USD | 0.00 USD | `+78.24%` | `180.80` |
| `Live` | `Short` | `1.59` | 698,550.00 USD | 1,180.00 USD | 0.00 USD | `+80.05%` | `743.20` |
| `Live` | `Short` | `1.59` | 974,400.00 USD | 275,850.00 USD | 0.00 USD | `+80.16%` | `173,000.00` |
| `Live` | `Short` | `1.60` | 974,520.00 USD | 123.81 USD | 0.00 USD | `+80.50%` | `77.50` |
| `Live` | `Short` | `1.60` | 975,650.00 USD | 1,130.00 USD | 0.00 USD | `+81.07%` | `704.60` |
| `Live` | `Short` | `1.61` | 977,840.00 USD | 2,190.00 USD | 0.00 USD | `+82.08%` | `1,360.10` |
| `Live` | `Short` | `1.65` | 999,180.00 USD | 21,330.00 USD | 0.00 USD | `+86.04%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 999,710.00 USD | 531.15 USD | 0.00 USD | `+86.26%` | `322.20` |
| `Live` | `Short` | `1.65` | 1,000,000.00 USD | 3,940.00 USD | 0.00 USD | `+86.83%` | `2,381.50` |
| `Live` | `Short` | `1.66` | 1,000,000.00 USD | 140.06 USD | 0.00 USD | `+87.28%` | `84.50` |
| `Live` | `Short` | `1.66` | 1,010,000.00 USD | 3,620.00 USD | 0.00 USD | `+87.51%` | `2,184.10` |
| `Live` | `Short` | `1.66` | 1,050,000.00 USD | 39,090.00 USD | 0.00 USD | `+87.73%` | `23,529.40` |
| `Live` | `Short` | `1.69` | 1,050,000.00 USD | 172.19 USD | 0.00 USD | `+90.56%` | `102.10` |
| `Live` | `Short` | `1.69` | 1,050,000.00 USD | 150.02 USD | 0.00 USD | `+90.67%` | `88.90` |
| `Live` | `Short` | `1.71` | 1,050,000.00 USD | 895.75 USD | 0.00 USD | `+92.93%` | `524.60` |
| `Live` | `Short` | `1.71` | 1,050,000.00 USD | 205.67 USD | 0.00 USD | `+93.49%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,060,000.00 USD | 9,680.00 USD | 0.00 USD | `+93.83%` | `5,645.40` |
| `Live` | `Short` | `1.73` | 1,060,000.00 USD | 226.05 USD | 0.00 USD | `+95.87%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,140,000.00 USD | 86,130.00 USD | 0.00 USD | `+96.43%` | `49,543.90` |
| `Live` | `Short` | `1.74` | 1,140,000.00 USD | 496.91 USD | 0.00 USD | `+96.66%` | `285.50` |
| `Live` | `Short` | `1.74` | 1,150,000.00 USD | 2,080.00 USD | 0.00 USD | `+96.77%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 1,170,000.00 USD | 19,920.00 USD | 0.00 USD | `+97.90%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 1,180,000.00 USD | 11,350.00 USD | 0.00 USD | `+98.13%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,180,000.00 USD | 1,520.00 USD | 0.00 USD | `+98.24%` | `868.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,130,000.00 USD | 0.00 USD | 497.31 USD | `-70.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,130,000.00 USD | 0.00 USD | 102.75 USD | `-61.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,130,000.00 USD | 0.00 USD | 256.78 USD | `-60.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,130,000.00 USD | 0.00 USD | 428.87 USD | `-56.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,130,000.00 USD | 0.00 USD | 123.45 USD | `-53.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,130,000.00 USD | 0.00 USD | 818.15 USD | `-52.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,130,000.00 USD | 0.00 USD | 436.41 USD | `-50.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,130,000.00 USD | 0.00 USD | 876.79 USD | `-50.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,130,000.00 USD | 0.00 USD | 466.72 USD | `-49.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,130,000.00 USD | 0.00 USD | 142.95 USD | `-46.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,130,000.00 USD | 0.00 USD | 3,010.00 USD | `-43.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,120,000.00 USD | 0.00 USD | 151.74 USD | `-41.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,120,000.00 USD | 0.00 USD | 123.91 USD | `-41.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,120,000.00 USD | 0.00 USD | 219.80 USD | `-37.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,120,000.00 USD | 0.00 USD | 237,400.00 USD | `-37.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 884,920.00 USD | 0.00 USD | 276.75 USD | `-37.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 884,640.00 USD | 0.00 USD | 1,680.00 USD | `-36.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 882,960.00 USD | 0.00 USD | 853.41 USD | `-35.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 882,110.00 USD | 0.00 USD | 119.76 USD | `-34.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 881,990.00 USD | 0.00 USD | 3,520.00 USD | `-33.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 878,460.00 USD | 0.00 USD | 470.62 USD | `-32.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 877,990.00 USD | 0.00 USD | 108.39 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 877,880.00 USD | 0.00 USD | 123.28 USD | `-31.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 877,760.00 USD | 0.00 USD | 488.52 USD | `-29.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 877,270.00 USD | 0.00 USD | 4,070.00 USD | `-29.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 873,200.00 USD | 0.00 USD | 242.24 USD | `-28.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 872,960.00 USD | 0.00 USD | 193.95 USD | `-26.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 872,770.00 USD | 0.00 USD | 149.22 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 872,620.00 USD | 0.00 USD | 195.47 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 872,420.00 USD | 0.00 USD | 112.91 USD | `-25.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 872,310.00 USD | 0.00 USD | 181.31 USD | `-25.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 872,130.00 USD | 0.00 USD | 190.25 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 871,940.00 USD | 0.00 USD | 153.53 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 871,790.00 USD | 0.00 USD | 52,450.00 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 819,340.00 USD | 0.00 USD | 536.11 USD | `-23.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 818,800.00 USD | 0.00 USD | 918.68 USD | `-23.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 817,880.00 USD | 0.00 USD | 340.75 USD | `-23.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 817,540.00 USD | 0.00 USD | 9,270.00 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 808,280.00 USD | 0.00 USD | 120.53 USD | `-21.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 808,160.00 USD | 0.00 USD | 160.71 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 808,000.00 USD | 0.00 USD | 738.08 USD | `-21.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 807,260.00 USD | 0.00 USD | 187.61 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 807,070.00 USD | 0.00 USD | 8,500.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 798,570.00 USD | 0.00 USD | 89,150.00 USD | `-20.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 709,420.00 USD | 0.00 USD | 5,650.00 USD | `-20.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 703,770.00 USD | 0.00 USD | 371.68 USD | `-19.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 703,400.00 USD | 0.00 USD | 152.05 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 703,250.00 USD | 0.00 USD | 123.41 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 703,120.00 USD | 0.00 USD | 745.54 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 702,380.00 USD | 0.00 USD | 1,130.00 USD | `-17.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 701,250.00 USD | 0.00 USD | 18,770.00 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 682,480.00 USD | 0.00 USD | 7,970.00 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 674,510.00 USD | 0.00 USD | 257.26 USD | `-16.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 674,250.00 USD | 0.00 USD | 161.72 USD | `-16.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 674,090.00 USD | 0.00 USD | 1,590.00 USD | `-15.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 672,500.00 USD | 0.00 USD | 10,160.00 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 662,340.00 USD | 0.00 USD | 94,190.00 USD | `-15.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 568,150.00 USD | 0.00 USD | 1,230.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 566,920.00 USD | 0.00 USD | 1,840.00 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 565,080.00 USD | 0.00 USD | 804.61 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 564,280.00 USD | 0.00 USD | 590.68 USD | `-14.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 563,690.00 USD | 0.00 USD | 635.62 USD | `-13.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 563,050.00 USD | 0.00 USD | 191.12 USD | `-13.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 562,860.00 USD | 0.00 USD | 273.92 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 562,580.00 USD | 0.00 USD | 125.92 USD | `-12.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 562,460.00 USD | 0.00 USD | 1,980.00 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 560,480.00 USD | 0.00 USD | 1,150.00 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 559,330.00 USD | 0.00 USD | 1,500.00 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 557,840.00 USD | 0.00 USD | 1,860.00 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 555,980.00 USD | 0.00 USD | 128.47 USD | `-11.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7815` | 555,850.00 USD | 0.00 USD | 7,820.00 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 548,030.00 USD | 0.00 USD | 6,960.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 541,080.00 USD | 0.00 USD | 135.11 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 540,940.00 USD | 0.00 USD | 7,870.00 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7885` | 533,080.00 USD | 0.00 USD | 1,090.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 531,980.00 USD | 0.00 USD | 1,500.00 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7935` | 530,490.00 USD | 0.00 USD | 1,290.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 529,200.00 USD | 0.00 USD | 23,890.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 505,310.00 USD | 0.00 USD | 1,260.00 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 504,050.00 USD | 0.00 USD | 319.40 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 503,730.00 USD | 0.00 USD | 4,740.00 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 498,990.00 USD | 0.00 USD | 1,800.00 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 497,190.00 USD | 0.00 USD | 144.67 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 497,050.00 USD | 0.00 USD | 1,510.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 495,540.00 USD | 0.00 USD | 390.59 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 495,150.00 USD | 0.00 USD | 263.25 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 494,880.00 USD | 0.00 USD | 1,250.00 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8095` | 493,630.00 USD | 0.00 USD | 218.32 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 493,410.00 USD | 0.00 USD | 182,300.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 311,110.00 USD | 0.00 USD | 174.63 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 310,940.00 USD | 0.00 USD | 1,420.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 309,520.00 USD | 0.00 USD | 123,350.00 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 186,160.00 USD | 0.00 USD | 1,160.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 185,010.00 USD | 0.00 USD | 216.70 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 184,790.00 USD | 0.00 USD | 125.72 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 184,660.00 USD | 0.00 USD | 375.49 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 184,290.00 USD | 0.00 USD | 14,050.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 170,240.00 USD | 0.00 USD | 7,160.00 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 163,090.00 USD | 0.00 USD | 226.71 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 162,860.00 USD | 0.00 USD | 3,780.00 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 159,080.00 USD | 0.00 USD | 6,050.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 153,020.00 USD | 0.00 USD | 325.56 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 152,700.00 USD | 0.00 USD | 666.55 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 152,030.00 USD | 0.00 USD | 577.25 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 151,460.00 USD | 0.00 USD | 3,950.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 147,500.00 USD | 0.00 USD | 171.46 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 147,330.00 USD | 0.00 USD | 7,920.00 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 139,410.00 USD | 0.00 USD | 690.30 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 138,720.00 USD | 0.00 USD | 161.89 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 138,560.00 USD | 0.00 USD | 263.43 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 138,300.00 USD | 0.00 USD | 610.23 USD | `-5.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 137,690.00 USD | 0.00 USD | 699.65 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 136,990.00 USD | 0.00 USD | 320.31 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 136,670.00 USD | 0.00 USD | 240.52 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 136,420.00 USD | 0.00 USD | 10,140.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 126,280.00 USD | 0.00 USD | 1,020.00 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 125,260.00 USD | 0.00 USD | 510.57 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 124,750.00 USD | 0.00 USD | 212.81 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 124,540.00 USD | 0.00 USD | 1,940.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 122,600.00 USD | 0.00 USD | 12,850.00 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 109,740.00 USD | 0.00 USD | 481.80 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 109,260.00 USD | 0.00 USD | 1,330.00 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 107,930.00 USD | 0.00 USD | 1,430.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 106,510.00 USD | 0.00 USD | 2,930.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8525` | 103,570.00 USD | 0.00 USD | 1,070.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 102,500.00 USD | 0.00 USD | 5,150.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 97,340.00 USD | 0.00 USD | 6,960.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 90,380.00 USD | 0.00 USD | 5,020.00 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 85,360.00 USD | 0.00 USD | 240.10 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 85,120.00 USD | 0.00 USD | 8,900.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 76,210.00 USD | 0.00 USD | 1,740.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 74,470.00 USD | 0.00 USD | 1,230.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 73,250.00 USD | 0.00 USD | 6,160.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 67,090.00 USD | 0.00 USD | 1,960.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 65,130.00 USD | 0.00 USD | 611.88 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 64,520.00 USD | 0.00 USD | 26,840.00 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 37,670.00 USD | 0.00 USD | 5,080.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 32,600.00 USD | 0.00 USD | 734.45 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 31,860.00 USD | 0.00 USD | 541.15 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 31,320.00 USD | 0.00 USD | 279.83 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 31,040.00 USD | 0.00 USD | 666.30 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 30,370.00 USD | 0.00 USD | 124.74 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 30,250.00 USD | 0.00 USD | 3,710.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 26,540.00 USD | 0.00 USD | 1,500.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 25,040.00 USD | 0.00 USD | 3,450.00 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 21,580.00 USD | 0.00 USD | 866.37 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 20,720.00 USD | 0.00 USD | 2,570.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 18,140.00 USD | 0.00 USD | 4,500.00 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 13,640.00 USD | 0.00 USD | 123.55 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 13,520.00 USD | 0.00 USD | 1,380.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 12,130.00 USD | 0.00 USD | 281.09 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 11,850.00 USD | 0.00 USD | 4,580.00 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 7,270.00 USD | 0.00 USD | 4,070.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 3,200.00 USD | 0.00 USD | 563.65 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 2,640.00 USD | 0.00 USD | 425.94 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 2,210.00 USD | 0.00 USD | 2,210.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 4,210.00 USD | 4,210.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 7,810.00 USD | 3,600.00 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 8,050.00 USD | 235.54 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 19,410.00 USD | 11,360.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 28,190.00 USD | 8,780.00 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 29,420.00 USD | 1,230.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 29,890.00 USD | 469.91 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 40,500.00 USD | 10,610.00 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 40,780.00 USD | 277.07 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 40,880.00 USD | 100.09 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 44,270.00 USD | 3,390.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 45,550.00 USD | 1,280.00 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 63,760.00 USD | 18,210.00 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 64,650.00 USD | 889.43 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 93,610.00 USD | 28,960.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 94,250.00 USD | 638.09 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 96,300.00 USD | 2,050.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 97,230.00 USD | 926.06 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 97,420.00 USD | 188.92 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 100,370.00 USD | 2,950.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 103,490.00 USD | 3,120.00 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 103,940.00 USD | 444.19 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 104,190.00 USD | 250.83 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 105,280.00 USD | 1,090.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 106,810.00 USD | 1,520.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 108,180.00 USD | 1,370.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 108,440.00 USD | 260.23 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 111,330.00 USD | 2,890.00 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 114,350.00 USD | 3,020.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 117,530.00 USD | 3,180.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 127,250.00 USD | 9,730.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 127,550.00 USD | 295.30 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 131,450.00 USD | 3,900.00 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 133,420.00 USD | 1,970.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 133,540.00 USD | 116.59 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 136,700.00 USD | 3,160.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 288,670.00 USD | 151,960.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 288,810.00 USD | 145.02 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 289,310.00 USD | 495.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 290,710.00 USD | 1,400.00 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 295,730.00 USD | 5,030.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 297,940.00 USD | 2,200.00 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 298,220.00 USD | 287.62 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 298,420.00 USD | 199.16 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 299,510.00 USD | 1,090.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 299,960.00 USD | 448.69 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 300,080.00 USD | 120.16 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 303,510.00 USD | 3,430.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 304,080.00 USD | 568.87 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 304,370.00 USD | 292.78 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 305,320.00 USD | 944.76 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 306,340.00 USD | 1,020.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 306,440.00 USD | 104.53 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 359,500.00 USD | 53,060.00 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 363,410.00 USD | 3,910.00 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 372,370.00 USD | 8,960.00 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 372,900.00 USD | 529.50 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 373,570.00 USD | 667.86 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 375,270.00 USD | 1,700.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 376,060.00 USD | 789.04 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 384,620.00 USD | 8,560.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 385,670.00 USD | 1,050.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 386,520.00 USD | 848.20 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 405,640.00 USD | 19,120.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 406,800.00 USD | 1,160.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 412,620.00 USD | 5,820.00 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 414,770.00 USD | 2,150.00 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 424,680.00 USD | 9,910.00 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 427,830.00 USD | 3,150.00 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 429,260.00 USD | 1,440.00 USD | 0.00 USD | `+7.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 432,150.00 USD | 2,890.00 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 433,280.00 USD | 1,130.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 433,400.00 USD | 121.54 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 434,480.00 USD | 1,070.00 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 439,860.00 USD | 5,390.00 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 458,740.00 USD | 18,870.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 478,140.00 USD | 19,400.00 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 478,400.00 USD | 259.86 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 479,730.00 USD | 1,340.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 480,210.00 USD | 476.57 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 480,600.00 USD | 386.60 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 483,760.00 USD | 3,160.00 USD | 0.00 USD | `+9.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 484,750.00 USD | 993.78 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 484,960.00 USD | 212.90 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 485,130.00 USD | 165.86 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 485,260.00 USD | 125.61 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 485,700.00 USD | 441.51 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 495,890.00 USD | 10,190.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 499,480.00 USD | 3,590.00 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 503,680.00 USD | 4,200.00 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 503,850.00 USD | 176.73 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 504,370.00 USD | 513.32 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 539,730.00 USD | 35,360.00 USD | 0.00 USD | `+10.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 571,690.00 USD | 31,960.00 USD | 0.00 USD | `+10.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 576,680.00 USD | 4,990.00 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 577,230.00 USD | 558.35 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 578,300.00 USD | 1,060.00 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 579,480.00 USD | 1,180.00 USD | 0.00 USD | `+11.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 579,970.00 USD | 490.99 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 580,360.00 USD | 395.21 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 581,360.00 USD | 991.50 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 591,690.00 USD | 10,340.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 592,100.00 USD | 409.52 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 592,390.00 USD | 284.92 USD | 0.00 USD | `+12.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 592,740.00 USD | 350.37 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 592,860.00 USD | 124.04 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 594,420.00 USD | 1,560.00 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 596,590.00 USD | 2,180.00 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 597,370.00 USD | 778.64 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 597,740.00 USD | 363.87 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 598,320.00 USD | 589.52 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 598,440.00 USD | 110.62 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 608,520.00 USD | 10,090.00 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 613,940.00 USD | 5,420.00 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 616,470.00 USD | 2,520.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 616,720.00 USD | 248.49 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 625,870.00 USD | 9,150.00 USD | 0.00 USD | `+14.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 626,590.00 USD | 722.63 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 626,900.00 USD | 312.07 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 627,070.00 USD | 171.24 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 627,630.00 USD | 561.11 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 627,880.00 USD | 249.30 USD | 0.00 USD | `+15.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 629,350.00 USD | 1,470.00 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 629,780.00 USD | 432.18 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 629,920.00 USD | 137.88 USD | 0.00 USD | `+16.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 632,260.00 USD | 2,340.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 632,960.00 USD | 694.72 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 633,120.00 USD | 160.60 USD | 0.00 USD | `+17.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 639,680.00 USD | 6,560.00 USD | 0.00 USD | `+17.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 642,590.00 USD | 2,920.00 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 642,820.00 USD | 224.56 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 646,390.00 USD | 3,570.00 USD | 0.00 USD | `+18.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 646,820.00 USD | 432.19 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 648,670.00 USD | 1,850.00 USD | 0.00 USD | `+18.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,350,000.00 USD | 1,700,000.00 USD | 0.00 USD | `+19.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 5,390.00 USD | 0.00 USD | `+19.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 285.32 USD | 0.00 USD | `+19.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 1,130.00 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 1,240.00 USD | 0.00 USD | `+19.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 278.06 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 309.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 228.98 USD | 0.00 USD | `+20.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 272.12 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 117.12 USD | 0.00 USD | `+21.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,500,000.00 USD | 140,120.00 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,500,000.00 USD | 530.01 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,500,000.00 USD | 128.23 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,610,000.00 USD | 108,190.00 USD | 0.00 USD | `+22.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,610,000.00 USD | 3,430.00 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,610,000.00 USD | 550.49 USD | 0.00 USD | `+22.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,620,000.00 USD | 5,810.00 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,620,000.00 USD | 1,520.00 USD | 0.00 USD | `+22.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 5,570.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 1,290.00 USD | 0.00 USD | `+23.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 294.81 USD | 0.00 USD | `+23.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 183.11 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,630,000.00 USD | 123.13 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,630,000.00 USD | 494.98 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,630,000.00 USD | 613.52 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,740,000.00 USD | 115,100.00 USD | 0.00 USD | `+24.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,740,000.00 USD | 409.76 USD | 0.00 USD | `+24.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,740,000.00 USD | 162.77 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,750,000.00 USD | 959.70 USD | 0.00 USD | `+24.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,750,000.00 USD | 160.18 USD | 0.00 USD | `+25.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,750,000.00 USD | 669.85 USD | 0.00 USD | `+25.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,750,000.00 USD | 293.61 USD | 0.00 USD | `+26.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,860,000.00 USD | 112,050.00 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,860,000.00 USD | 462.47 USD | 0.00 USD | `+27.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,860,000.00 USD | 2,180.00 USD | 0.00 USD | `+27.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,860,000.00 USD | 273.34 USD | 0.00 USD | `+27.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,860,000.00 USD | 119.49 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,880,000.00 USD | 20,740.00 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,880,000.00 USD | 468.47 USD | 0.00 USD | `+28.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,880,000.00 USD | 1,430.00 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,890,000.00 USD | 338.50 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,890,000.00 USD | 2,640.00 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,890,000.00 USD | 1,230.00 USD | 0.00 USD | `+30.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,890,000.00 USD | 2,450.00 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,890,000.00 USD | 1,250.00 USD | 0.00 USD | `+30.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,890,000.00 USD | 143.67 USD | 0.00 USD | `+31.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,890,000.00 USD | 989.81 USD | 0.00 USD | `+31.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,890,000.00 USD | 304.33 USD | 0.00 USD | `+32.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,890,000.00 USD | 255.14 USD | 0.00 USD | `+32.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,890,000.00 USD | 241.65 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,890,000.00 USD | 239.97 USD | 0.00 USD | `+33.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,900,000.00 USD | 2,470.00 USD | 0.00 USD | `+33.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,900,000.00 USD | 3,060.00 USD | 0.00 USD | `+33.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,210,000.00 USD | 310,250.00 USD | 0.00 USD | `+34.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,210,000.00 USD | 309.53 USD | 0.00 USD | `+34.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,210,000.00 USD | 159.09 USD | 0.00 USD | `+34.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,210,000.00 USD | 146.21 USD | 0.00 USD | `+35.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,230,000.00 USD | 18,560.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,230,000.00 USD | 933.81 USD | 0.00 USD | `+35.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,230,000.00 USD | 658.86 USD | 0.00 USD | `+36.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,440,000.00 USD | 213,390.00 USD | 0.00 USD | `+36.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,450,000.00 USD | 560.05 USD | 0.00 USD | `+37.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,450,000.00 USD | 1,050.00 USD | 0.00 USD | `+37.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,450,000.00 USD | 108.05 USD | 0.00 USD | `+37.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,450,000.00 USD | 509.71 USD | 0.00 USD | `+38.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,450,000.00 USD | 162.15 USD | 0.00 USD | `+38.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,450,000.00 USD | 187.04 USD | 0.00 USD | `+39.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,450,000.00 USD | 542.12 USD | 0.00 USD | `+39.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,470,000.00 USD | 23,740.00 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,470,000.00 USD | 2,010.00 USD | 0.00 USD | `+39.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,470,000.00 USD | 345.91 USD | 0.00 USD | `+39.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,470,000.00 USD | 104.79 USD | 0.00 USD | `+40.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,470,000.00 USD | 100.04 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,470,000.00 USD | 517.52 USD | 0.00 USD | `+41.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,470,000.00 USD | 152.29 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,480,000.00 USD | 1,480.00 USD | 0.00 USD | `+42.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,480,000.00 USD | 1,010.00 USD | 0.00 USD | `+42.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,480,000.00 USD | 2,780.00 USD | 0.00 USD | `+43.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,480,000.00 USD | 340.38 USD | 0.00 USD | `+43.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,480,000.00 USD | 903.22 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,480,000.00 USD | 475.01 USD | 0.00 USD | `+44.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,520,000.00 USD | 41,160.00 USD | 0.00 USD | `+44.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,540,000.00 USD | 12,840.00 USD | 0.00 USD | `+45.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,730,000.00 USD | 194,770.00 USD | 0.00 USD | `+45.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,740,000.00 USD | 12,890.00 USD | 0.00 USD | `+45.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,750,000.00 USD | 8,820.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,750,000.00 USD | 466.95 USD | 0.00 USD | `+46.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,750,000.00 USD | 613.59 USD | 0.00 USD | `+46.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,750,000.00 USD | 1,420.00 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,770,000.00 USD | 13,000.00 USD | 0.00 USD | `+46.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,770,000.00 USD | 284.42 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,790,000.00 USD | 22,810.00 USD | 0.00 USD | `+49.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,790,000.00 USD | 640.82 USD | 0.00 USD | `+50.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,790,000.00 USD | 134.75 USD | 0.00 USD | `+50.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,810,000.00 USD | 13,400.00 USD | 0.00 USD | `+51.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,810,000.00 USD | 541.96 USD | 0.00 USD | `+51.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,820,000.00 USD | 13,490.00 USD | 0.00 USD | `+52.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,830,000.00 USD | 11,580.00 USD | 0.00 USD | `+52.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,830,000.00 USD | 3,610.00 USD | 0.00 USD | `+53.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,840,000.00 USD | 1,500.00 USD | 0.00 USD | `+54.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,850,000.00 USD | 15,000.00 USD | 0.00 USD | `+54.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,860,000.00 USD | 9,030.00 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,860,000.00 USD | 405.86 USD | 0.00 USD | `+56.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,870,000.00 USD | 13,890.00 USD | 0.00 USD | `+57.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,890,000.00 USD | 14,000.00 USD | 0.00 USD | `+58.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,900,000.00 USD | 12,560.00 USD | 0.00 USD | `+58.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,930,000.00 USD | 32,860.00 USD | 0.00 USD | `+59.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,930,000.00 USD | 102.40 USD | 0.00 USD | `+59.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,930,000.00 USD | 106.64 USD | 0.00 USD | `+59.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,940,000.00 USD | 1,430.00 USD | 0.00 USD | `+59.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,940,000.00 USD | 2,810.00 USD | 0.00 USD | `+59.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,950,000.00 USD | 8,420.00 USD | 0.00 USD | `+60.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 3,950,000.00 USD | 1,410.00 USD | 0.00 USD | `+61.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,950,000.00 USD | 145.37 USD | 0.00 USD | `+62.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,950,000.00 USD | 1,390.00 USD | 0.00 USD | `+62.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,960,000.00 USD | 14,390.00 USD | 0.00 USD | `+62.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,970,000.00 USD | 7,000.00 USD | 0.00 USD | `+63.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,990,000.00 USD | 14,490.00 USD | 0.00 USD | `+63.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,990,000.00 USD | 1,340.00 USD | 0.00 USD | `+65.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,990,000.00 USD | 342.08 USD | 0.00 USD | `+66.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,000,000.00 USD | 14,890.00 USD | 0.00 USD | `+68.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,010,000.00 USD | 9,580.00 USD | 0.00 USD | `+68.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,030,000.00 USD | 14,980.00 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,030,000.00 USD | 5,110.00 USD | 0.00 USD | `+69.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,030,000.00 USD | 1,180.00 USD | 0.00 USD | `+69.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,030,000.00 USD | 1,260.00 USD | 0.00 USD | `+72.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,040,000.00 USD | 2,150.00 USD | 0.00 USD | `+74.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,040,000.00 USD | 158.76 USD | 0.00 USD | `+76.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,070,000.00 USD | 30,710.00 USD | 0.00 USD | `+76.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,070,000.00 USD | 574.53 USD | 0.00 USD | `+79.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,070,000.00 USD | 391.32 USD | 0.00 USD | `+80.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,070,000.00 USD | 1,160.00 USD | 0.00 USD | `+82.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,070,000.00 USD | 1,140.00 USD | 0.00 USD | `+85.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,070,000.00 USD | 1,970.00 USD | 0.00 USD | `+85.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,070,000.00 USD | 281.45 USD | 0.00 USD | `+87.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,070,000.00 USD | 2,070.00 USD | 0.00 USD | `+87.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,090,000.00 USD | 13,060.00 USD | 0.00 USD | `+92.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 4,090,000.00 USD | 1,390.00 USD | 0.00 USD | `+96.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,090,000.00 USD | 1,070.00 USD | 0.00 USD | `+97.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,090,000.00 USD | 320.52 USD | 0.00 USD | `+97.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 4,090,000.00 USD | 1,710.00 USD | 0.00 USD | `+99.60%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7380` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 56,620.00 USD | 28,770.00 USD | 82,570.00 USD |
| `7D` | `0.7400` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 17,280.00 USD | 13,180.00 USD | 24,540.00 USD |
| `7D` | `0.7420` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 31,920.00 USD | 8,580.00 USD | 37,420.00 USD |
| `7D` | `0.7440` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 65,280.00 USD | 21,190.00 USD | 41,020.00 USD |
| `7D` | `0.7460` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 22,100.00 USD | 24,720.00 USD | 42,470.00 USD |
| `7D` | `0.7480` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 11,220.00 USD | 6,300.00 USD | 375.99 USD |
| `7D` | `0.7500` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 25,600.00 USD | 12,880.00 USD | 11,450.00 USD |
| `7D` | `0.7520` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 2,130.00 USD | 10,160.00 USD | 22,250.00 USD |
| `7D` | `0.7540` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 9,690.00 USD | 4,770.00 USD | 13,530.00 USD |
| `7D` | `0.7560` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 2,690.00 USD | 17,670.00 USD | 5,490.00 USD |
| `7D` | `0.7580` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 19,590.00 USD | 20,390.00 USD | 1,090.00 USD |
| `7D` | `0.7600` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 8,420.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `0.7620` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 40,420.00 USD | 16,580.00 USD | 630.66 USD |
| `7D` | `0.7640` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 556.58 USD | 118.70 USD | 573.15 USD |
| `7D` | `0.7660` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 1,280.00 USD | 23,260.00 USD | 32,410.00 USD |
| `7D` | `0.7680` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 182.28 USD | 3,780.00 USD | 1,880.00 USD |
| `7D` | `0.7700` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD |
| `7D` | `0.7720` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7780` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD |
| `7D` | `0.7800` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 0.00 USD | 2,640.00 USD | 1,330.00 USD |
| `7D` | `0.7820` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 0.00 USD | 1,440.00 USD | 10,610.00 USD |
| `7D` | `0.7840` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 6,050.00 USD | 2,680.00 USD | 1,320.00 USD |
| `7D` | `0.7860` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 1,740.00 USD | 45,250.00 USD | 0.00 USD |
| `7D` | `0.7900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 6,610.00 USD | 28,080.00 USD | 0.00 USD |
| `1D` | `0.7910` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 13,200.00 USD | 12,510.00 USD | 9,350.00 USD |
| `1D` | `0.7920` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 8,420.00 USD | 9,490.00 USD | 36,790.00 USD |
| `7D` | `0.7920` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 23,790.00 USD | 69,490.00 USD |
| `1D` | `0.7930` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 952.83 USD | 12,430.00 USD | 7,560.00 USD |
| `1D` | `0.7940` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 20,620.00 USD | 8,610.00 USD | 14,590.00 USD |
| `7D` | `0.7940` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 0.00 USD | 1,760.00 USD | 4,720.00 USD |
| `1D` | `0.7950` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 5,840.00 USD | 3,900.00 USD | 24,940.00 USD |
| `1D` | `0.7960` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 1,860.00 USD | 2,710.00 USD | 20,810.00 USD |
| `7D` | `0.7960` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 4,090.00 USD | 19,750.00 USD | 87,940.00 USD |
| `1D` | `0.7970` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 16,800.00 USD | 16,290.00 USD | 40,370.00 USD |
| `1D` | `0.7980` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 8,320.00 USD | 0.00 USD | 165.92 USD |
| `7D` | `0.7980` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 33,940.00 USD | 3,570.00 USD | 49,630.00 USD |
| `1D` | `0.7990` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 1,600.00 USD | 20,590.00 USD | 18,860.00 USD |
| `1D` | `0.8000` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 30,830.00 USD | 10,990.00 USD | 16,320.00 USD |
| `7D` | `0.8000` | 9,270,000.00 USD | 0.00 USD | 9,270,000.00 USD | 41,450.00 USD | 16,710.00 USD | 0.00 USD |
| `1D` | `0.8010` | 6,970,000.00 USD | 0.00 USD | 6,970,000.00 USD | 1,140.00 USD | 3,860.00 USD | 200.14 USD |
| `1D` | `0.8020` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 796.46 USD | 6,400.00 USD | 6,570.00 USD |
| `7D` | `0.8020` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 1,890.00 USD | 29,180.00 USD | 35,910.00 USD |
| `1D` | `0.8030` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 0.00 USD | 1,400.00 USD | 159.97 USD |
| `1D` | `0.8040` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 43,320.00 USD | 22,790.00 USD | 21,430.00 USD |
| `7D` | `0.8040` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD |
| `1D` | `0.8050` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 19,550.00 USD | 7,230.00 USD | 330.63 USD |
| `1D` | `0.8060` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 32,080.00 USD | 11,640.00 USD | 73,980.00 USD |
| `7D` | `0.8060` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 12,280.00 USD | 737.70 USD | 1,170.00 USD |
| `1D` | `0.8070` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 8,540.00 USD | 14,620.00 USD | 1,120.00 USD |
| `1D` | `0.8080` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 2,530.00 USD | 4,510.00 USD | 1,630.00 USD |
| `7D` | `0.8080` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 5,030.00 USD | 11,280.00 USD | 8,230.00 USD |
| `1D` | `0.8090` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 587.71 USD | 5,580.00 USD | 1,870.00 USD |
| `1D` | `0.8100` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 1,830.00 USD | 5,380.00 USD | 248.40 USD |
| `7D` | `0.8100` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 4,310.00 USD | 9,850.00 USD | 5,630.00 USD |
| `1D` | `0.8110` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 1,650.00 USD | 2,090.00 USD | 196.09 USD |
| `1D` | `0.8120` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 13,640.00 USD | 780.21 USD | 23,580.00 USD |
| `7D` | `0.8120` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 73,000.00 USD | 9,210.00 USD | 38,210.00 USD |
| `1D` | `0.8130` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 683.00 USD | 989.28 USD | 706.99 USD |
| `1D` | `0.8140` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 14,810.00 USD | 523.16 USD | 11,360.00 USD |
| `7D` | `0.8140` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 55,190.00 USD | 31,920.00 USD | 79,240.00 USD |
| `1D` | `0.8150` | 6,590,000.00 USD | 0.00 USD | 6,590,000.00 USD | 4,970.00 USD | 1,140.00 USD | 7,080.00 USD |
| `1D` | `0.8160` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 17,910.00 USD | 1,970.00 USD | 23,400.00 USD |
| `7D` | `0.8160` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 186,980.00 USD | 49,790.00 USD | 146,720.00 USD |
| `1D` | `0.8170` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 56,460.00 USD | 4,990.00 USD | 30,370.00 USD |
| `1D` | `0.8180` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 361.35 USD | 1,680.00 USD | 213.40 USD |
| `7D` | `0.8180` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 82,600.00 USD | 41,370.00 USD | 43,240.00 USD |
| `1D` | `0.8190` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 24,470.00 USD | 1,600.00 USD | 10,410.00 USD |
| `1D` | `0.8200` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 87,930.00 USD | 4,880.00 USD | 73,280.00 USD |
| `7D` | `0.8200` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 205,920.00 USD | 48,700.00 USD | 97,610.00 USD |
| `1D` | `0.8210` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 15,840.00 USD | 83,090.00 USD | 50,570.00 USD |
| `1D` | `0.8220` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 58,680.00 USD | 3,580.00 USD | 26,590.00 USD |
| `7D` | `0.8220` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 110,800.00 USD | 74,480.00 USD | 175,590.00 USD |
| `1D` | `0.8230` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 7,960.00 USD | 5,500.00 USD | 105,860.00 USD |
| `1D` | `0.8240` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 8,230.00 USD | 2,400.00 USD | 32,680.00 USD |
| `7D` | `0.8240` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 104,380.00 USD | 43,480.00 USD | 87,630.00 USD |
| `1D` | `0.8250` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 26,090.00 USD | 2,480.00 USD | 8,200.00 USD |
| `1D` | `0.8260` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 19,170.00 USD | 8,970.00 USD | 17,260.00 USD |
| `7D` | `0.8260` | 7,280,000.00 USD | 0.00 USD | 7,280,000.00 USD | 197,160.00 USD | 32,880.00 USD | 111,970.00 USD |
| `1D` | `0.8270` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 39,540.00 USD | 22,100.00 USD | 8,150.00 USD |
| `1D` | `0.8280` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 1,490.00 USD | 773.90 USD | 313.76 USD |
| `7D` | `0.8280` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 118,780.00 USD | 44,400.00 USD | 87,990.00 USD |
| `1D` | `0.8290` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 24,750.00 USD | 11,650.00 USD | 46,490.00 USD |
| `1D` | `0.8300` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 3,410.00 USD | 3,180.00 USD | 7,300.00 USD |
| `7D` | `0.8300` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 33,770.00 USD | 45,100.00 USD | 48,290.00 USD |
| `1D` | `0.8310` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 2,590.00 USD | 27,590.00 USD | 23,300.00 USD |
| `1D` | `0.8320` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 867.90 USD | 10,780.00 USD | 22,900.00 USD |
| `7D` | `0.8320` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 90,830.00 USD | 77,110.00 USD | 150,430.00 USD |
| `1D` | `0.8330` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 7,940.00 USD | 19,140.00 USD | 74,670.00 USD |
| `1D` | `0.8340` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 142,540.00 USD | 21,960.00 USD | 30,560.00 USD |
| `7D` | `0.8340` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 114,580.00 USD | 56,360.00 USD | 180,080.00 USD |
| `1D` | `0.8350` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 14,620.00 USD | 13,380.00 USD | 1,070.00 USD |
| `1D` | `0.8360` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 45,630.00 USD | 1,600.00 USD | 397.88 USD |
| `7D` | `0.8360` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 178,100.00 USD | 28,000.00 USD | 99,550.00 USD |
| `1D` | `0.8370` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 19,230.00 USD | 9,130.00 USD | 129,040.00 USD |
| `1D` | `0.8380` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 32,770.00 USD | 59,720.00 USD | 16,830.00 USD |
| `7D` | `0.8380` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 65,710.00 USD | 221,490.00 USD | 223,070.00 USD |
| `1D` | `0.8390` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 42,590.00 USD | 792.50 USD | 33,000.00 USD |
| `1D` | `0.8400` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 4,220.00 USD | 9,410.00 USD | 22,280.00 USD |
| `7D` | `0.8400` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 88,890.00 USD | 56,210.00 USD | 61,950.00 USD |
| `1D` | `0.8410` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 17,400.00 USD | 16,230.00 USD | 55,700.00 USD |
| `1D` | `0.8420` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 71,930.00 USD | 48,120.00 USD | 0.00 USD |
| `7D` | `0.8420` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 96,530.00 USD | 66,440.00 USD | 9,570.00 USD |
| `1D` | `0.8430` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 17,820.00 USD | 18,730.00 USD | 21,880.00 USD |
| `1D` | `0.8440` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 49,800.00 USD | 44,320.00 USD | 166.34 USD |
| `7D` | `0.8440` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 28,900.00 USD | 111,080.00 USD | 0.00 USD |
| `1D` | `0.8450` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 22,880.00 USD | 30,550.00 USD | 12,980.00 USD |
| `1D` | `0.8460` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 623.10 USD | 63,560.00 USD | 26,100.00 USD |
| `7D` | `0.8460` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 52,800.00 USD | 57,770.00 USD | 0.00 USD |
| `1D` | `0.8470` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 51,620.00 USD | 37,640.00 USD | 0.00 USD |
| `1D` | `0.8480` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 0.00 USD | 36,960.00 USD | 82,740.00 USD |
| `7D` | `0.8480` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 73,880.00 USD | 61,480.00 USD | 82,870.00 USD |
| `1D` | `0.8490` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 57,710.00 USD | 61,840.00 USD | 67,980.00 USD |
| `1D` | `0.8500` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 35,490.00 USD | 37,570.00 USD | 107,590.00 USD |
| `7D` | `0.8500` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 85,470.00 USD | 58,490.00 USD | 50,360.00 USD |
| `1D` | `0.8510` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 41,500.00 USD | 106,640.00 USD | 49,410.00 USD |
| `1D` | `0.8520` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 59,930.00 USD | 95,740.00 USD | 88,510.00 USD |
| `7D` | `0.8520` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 77,320.00 USD | 53,520.00 USD | 54,650.00 USD |
| `1D` | `0.8530` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,030.00 USD |
| `1D` | `0.8540` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 13,200.00 USD | 128.06 USD |
| `7D` | `0.8540` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 277,690.00 USD | 50,820.00 USD | 0.00 USD |
| `1D` | `0.8550` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 1,920.00 USD | 37,290.00 USD | 15,370.00 USD |
| `1D` | `0.8560` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 30,660.00 USD | 17,140.00 USD | 52,090.00 USD |
| `7D` | `0.8560` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 87,380.00 USD | 91,360.00 USD | 33,190.00 USD |
| `1D` | `0.8570` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 14,730.00 USD | 12,760.00 USD | 3,770.00 USD |
| `1D` | `0.8580` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 32,900.00 USD | 54,050.00 USD | 26,530.00 USD |
| `7D` | `0.8580` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 146,570.00 USD | 14,530.00 USD | 0.00 USD |
| `1D` | `0.8590` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 13,810.00 USD | 6,720.00 USD | 36,530.00 USD |
| `1D` | `0.8600` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 75,640.00 USD | 32,480.00 USD | 200.12 USD |
| `7D` | `0.8600` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 38,890.00 USD | 164,470.00 USD | 20,680.00 USD |
| `1D` | `0.8610` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 21,600.00 USD | 0.00 USD | 6,800.00 USD |
| `1D` | `0.8620` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 42,920.00 USD | 25,800.00 USD | 26,120.00 USD |
| `7D` | `0.8620` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 25,100.00 USD | 145,110.00 USD | 394,640.00 USD |
| `1D` | `0.8630` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 48,390.00 USD | 98,690.00 USD | 113,770.00 USD |
| `1D` | `0.8640` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 28,850.00 USD | 51,300.00 USD | 29.91 USD |
| `7D` | `0.8640` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 83,850.00 USD | 0.00 USD | 2,680.00 USD |
| `1D` | `0.8650` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | 35,750.00 USD | 136,870.00 USD |
| `1D` | `0.8660` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 127,140.00 USD | 13,430.00 USD | 54,950.00 USD |
| `7D` | `0.8660` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 294,020.00 USD | 122,950.00 USD | 678,840.00 USD |
| `1D` | `0.8670` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 100,220.00 USD | 33,880.00 USD | 142,270.00 USD |
| `1D` | `0.8680` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 50,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8680` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 213,340.00 USD | 0.00 USD | 10,240.00 USD |
| `1D` | `0.8690` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 25,820.00 USD |
| `1D` | `0.8700` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 97,830.00 USD | 31,630.00 USD |
| `7D` | `0.8700` | 952,500.00 USD | 0.00 USD | 952,500.00 USD | 0.00 USD | 34,600.00 USD | 111,270.00 USD |
| `1D` | `0.8710` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 152,210.00 USD | 62,100.00 USD | 151,880.00 USD |
| `1D` | `0.8720` | 855,600.00 USD | 0.00 USD | 855,600.00 USD | 30,060.00 USD | 26,400.00 USD | 21,020.00 USD |
| `7D` | `0.8720` | 806,620.00 USD | 0.00 USD | 806,620.00 USD | 207,250.00 USD | 101,630.00 USD | 87,530.00 USD |
| `1D` | `0.8730` | 778,130.00 USD | 0.00 USD | 778,130.00 USD | 55,600.00 USD | 39,670.00 USD | 29,960.00 USD |
| `1D` | `0.8740` | 652,890.00 USD | 0.00 USD | 652,890.00 USD | 61,330.00 USD | 20,260.00 USD | 39,440.00 USD |
| `7D` | `0.8740` | 410,210.00 USD | 0.00 USD | 410,210.00 USD | 9,520.00 USD | 72,100.00 USD | 71,600.00 USD |
| `1D` | `0.8750` | 531,870.00 USD | 0.00 USD | 531,870.00 USD | 29,460.00 USD | 0.00 USD | 83,500.00 USD |
| `1D` | `0.8760` | 418,910.00 USD | 0.00 USD | 418,910.00 USD | 0.00 USD | 0.00 USD | 53,070.00 USD |
| `7D` | `0.8760` | 256,990.00 USD | 0.00 USD | 256,990.00 USD | 16,700.00 USD | 29,060.00 USD | 189,440.00 USD |
| `1D` | `0.8770` | 365,840.00 USD | 0.00 USD | 365,840.00 USD | 27,620.00 USD | 20,280.00 USD | 94,280.00 USD |
| `1D` | `0.8780` | 223,650.00 USD | 0.00 USD | 223,650.00 USD | 79,990.00 USD | 17,410.00 USD | 0.00 USD |
| `7D` | `0.8780` | 21,780.00 USD | 0.00 USD | 21,780.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `1D` | `0.8790` | 126,240.00 USD | 0.00 USD | 126,240.00 USD | 39,180.00 USD | 0.00 USD | 12,930.00 USD |
| `1D` | `0.8800` | 74,130.00 USD | 0.00 USD | 74,130.00 USD | 4,760.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `0.8800` | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8810` | 68,360.00 USD | 0.00 USD | 68,360.00 USD | 37,200.00 USD | 0.00 USD | 31,170.00 USD |
| `1D` | `0.8820` | 94,270.00 USD | 94,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 94,270.00 USD |
| `1D` | `0.8820` | 188,540.00 USD | 188,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 94,270.00 USD |
| `7D` | `0.8820` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8840` | 190,360.00 USD | 190,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `1D` | `0.8850` | 190,580.00 USD | 190,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 214.94 USD |
| `1D` | `0.8860` | 191,690.00 USD | 191,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `1D` | `0.8870` | 193,090.00 USD | 193,090.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD |
| `1D` | `0.8880` | 315,850.00 USD | 315,850.00 USD | 0.00 USD | 122,200.00 USD | 0.00 USD | 560.38 USD |
| `7D` | `0.8880` | 3,860.00 USD | 3,860.00 USD | 0.00 USD | 0.00 USD | 3,860.00 USD | 0.00 USD |
| `1D` | `0.8900` | 318,710.00 USD | 318,710.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8900` | 12,670.00 USD | 12,670.00 USD | 0.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8910` | 406,910.00 USD | 406,910.00 USD | 0.00 USD | 87,950.00 USD | 0.00 USD | 251.48 USD |
| `1D` | `0.8920` | 408,700.00 USD | 408,700.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8920` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8930` | 427,520.00 USD | 427,520.00 USD | 0.00 USD | 0.00 USD | 18,820.00 USD | 0.00 USD |
| `1D` | `0.8940` | 449,090.00 USD | 449,090.00 USD | 0.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `7D` | `0.8940` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8950` | 526,940.00 USD | 526,940.00 USD | 0.00 USD | 0.00 USD | 77,850.00 USD | 0.00 USD |
| `7D` | `0.8960` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 593,680.00 USD | 107,280.00 USD | 0.00 USD |
| `1D` | `0.8970` | 527,900.00 USD | 527,900.00 USD | 0.00 USD | 969.20 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8980` | 661,740.00 USD | 661,740.00 USD | 0.00 USD | 73,030.00 USD | 60,810.00 USD | 0.00 USD |
| `7D` | `0.8980` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 615,200.00 USD | 118,950.00 USD | 339,780.00 USD |
| `1D` | `0.8990` | 853,210.00 USD | 853,210.00 USD | 0.00 USD | 70,970.00 USD | 120,500.00 USD | 0.00 USD |
| `1D` | `0.9000` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 167,020.00 USD | 1,490.00 USD | 0.00 USD |
| `7D` | `0.9000` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 198,040.00 USD | 16,730.00 USD | 0.00 USD |
| `1D` | `0.9010` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 3,390.00 USD | 107,900.00 USD | 24,790.00 USD |
| `1D` | `0.9020` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 20,120.00 USD | 53,510.00 USD | 0.00 USD |
| `7D` | `0.9020` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 85,610.00 USD | 221,330.00 USD | 476,390.00 USD |
| `1D` | `0.9030` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 25,600.00 USD | 108,680.00 USD | 16,750.00 USD |
| `1D` | `0.9040` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 175,130.00 USD | 136,350.00 USD | 0.00 USD |
| `7D` | `0.9040` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 223,750.00 USD | 2,890.00 USD | 218,670.00 USD |
| `1D` | `0.9050` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 90,340.00 USD | 26,270.00 USD | 44,370.00 USD |
| `1D` | `0.9060` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 168,180.00 USD | 158,360.00 USD | 165,470.00 USD |
| `7D` | `0.9060` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 286,790.00 USD | 34,600.00 USD | 104,620.00 USD |
| `1D` | `0.9070` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 135,160.00 USD | 128,180.00 USD | 115,990.00 USD |
| `1D` | `0.9080` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 113,830.00 USD | 45,320.00 USD | 17,240.00 USD |
| `7D` | `0.9080` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 389,350.00 USD | 288,590.00 USD | 227,140.00 USD |
| `1D` | `0.9090` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 76,970.00 USD | 49,730.00 USD | 33,090.00 USD |
| `1D` | `0.9100` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 83,550.00 USD | 50,130.00 USD | 40,220.00 USD |
| `7D` | `0.9100` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 123,910.00 USD | 78,920.00 USD | 70,600.00 USD |
| `1D` | `0.9110` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 97,650.00 USD | 16,590.00 USD | 29,110.00 USD |
| `1D` | `0.9120` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 32,690.00 USD | 81,230.00 USD | 69,240.00 USD |
| `7D` | `0.9120` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 135,210.00 USD | 163,810.00 USD | 0.00 USD |
| `1D` | `0.9130` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 45,950.00 USD | 25,330.00 USD | 92,690.00 USD |
| `1D` | `0.9140` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 162,940.00 USD | 61,860.00 USD | 142,770.00 USD |
| `7D` | `0.9140` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 143,540.00 USD | 83,230.00 USD | 0.00 USD |
| `1D` | `0.9150` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 109,360.00 USD | 68,860.00 USD | 184,390.00 USD |
| `1D` | `0.9160` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 60,590.00 USD | 100,190.00 USD | 52,430.00 USD |
| `7D` | `0.9160` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 212,270.00 USD | 84,510.00 USD | 172,440.00 USD |
| `1D` | `0.9170` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 64,160.00 USD | 26,950.00 USD | 67,570.00 USD |
| `1D` | `0.9180` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 26,530.00 USD | 60,340.00 USD | 68,440.00 USD |
| `7D` | `0.9180` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 38,590.00 USD | 63,520.00 USD | 187,840.00 USD |
| `1D` | `0.9190` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 57,560.00 USD | 16,580.00 USD | 49,670.00 USD |
| `1D` | `0.9200` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 65,430.00 USD | 16,940.00 USD | 100,020.00 USD |
| `7D` | `0.9200` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 445,890.00 USD | 32,570.00 USD | 114,170.00 USD |
| `1D` | `0.9210` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 85,860.00 USD | 61,240.00 USD | 124,600.00 USD |
| `1D` | `0.9220` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 129,150.00 USD | 32,770.00 USD | 136,590.00 USD |
| `7D` | `0.9220` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 6,470.00 USD | 66,370.00 USD | 318,200.00 USD |
| `1D` | `0.9230` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 107,110.00 USD | 55,720.00 USD | 151,880.00 USD |
| `1D` | `0.9240` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 133,310.00 USD | 59,770.00 USD | 117,430.00 USD |
| `7D` | `0.9240` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 111,800.00 USD | 62,860.00 USD | 256,790.00 USD |
| `1D` | `0.9250` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 132,110.00 USD | 61,310.00 USD | 55,080.00 USD |
| `1D` | `0.9260` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 3,870.00 USD | 71,300.00 USD | 52,810.00 USD |
| `7D` | `0.9260` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 209,940.00 USD | 97,540.00 USD | 89,770.00 USD |
| `1D` | `0.9270` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 7,220.00 USD | 67,290.00 USD | 27,410.00 USD |
| `1D` | `0.9280` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 36,920.00 USD | 30,650.00 USD | 68,280.00 USD |
| `7D` | `0.9280` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 121,460.00 USD | 43,320.00 USD | 36,720.00 USD |
| `1D` | `0.9290` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 53,450.00 USD | 2,870.00 USD | 44,980.00 USD |
| `1D` | `0.9300` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 5,010.00 USD | 59,350.00 USD | 65,490.00 USD |
| `7D` | `0.9300` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 186,110.00 USD | 113,080.00 USD | 168,120.00 USD |
| `1D` | `0.9310` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 118,420.00 USD | 16,270.00 USD | 36,900.00 USD |
| `1D` | `0.9320` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 71,540.00 USD | 28,860.00 USD | 35,540.00 USD |
| `7D` | `0.9320` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 4,410.00 USD | 53,880.00 USD | 63,160.00 USD |
| `1D` | `0.9330` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 24,270.00 USD | 19,640.00 USD | 6,470.00 USD |
| `1D` | `0.9340` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 1,200.00 USD | 16,430.00 USD | 0.00 USD |
| `7D` | `0.9340` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 50,160.00 USD | 78,870.00 USD | 0.00 USD |
| `1D` | `0.9350` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 964.55 USD | 637.37 USD | 19,260.00 USD |
| `1D` | `0.9360` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 48,380.00 USD | 29,620.00 USD | 55,350.00 USD |
| `7D` | `0.9360` | 11,770,000.00 USD | 11,770,000.00 USD | 0.00 USD | 131,450.00 USD | 3,160.00 USD | 8,180.00 USD |
| `1D` | `0.9370` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 80,470.00 USD | 54,520.00 USD | 135,700.00 USD |
| `1D` | `0.9380` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 15,820.00 USD | 9,200.00 USD | 110,030.00 USD |
| `7D` | `0.9380` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 168,030.00 USD | 5,150.00 USD | 179,560.00 USD |
| `1D` | `0.9390` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 2,230.00 USD | 3,000.00 USD | 34,210.00 USD |
| `1D` | `0.9400` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 45,080.00 USD | 1,460.00 USD | 56,200.00 USD |
| `7D` | `0.9400` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 173,610.00 USD | 39,110.00 USD | 129,920.00 USD |
| `1D` | `0.9410` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 18,300.00 USD | 15,240.00 USD | 616.58 USD |
| `1D` | `0.9420` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 5,130.00 USD | 1,340.00 USD | 24,870.00 USD |
| `7D` | `0.9420` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 7,320.00 USD | 31,200.00 USD | 37,360.00 USD |
| `1D` | `0.9430` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 2,790.00 USD | 2,340.00 USD | 0.00 USD |
| `1D` | `0.9440` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 4,930.00 USD | 23,400.00 USD | 46,190.00 USD |
| `7D` | `0.9440` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 6,180.00 USD | 217,840.00 USD | 1,280.00 USD |
| `1D` | `0.9450` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 4,850.00 USD | 793.93 USD | 107,000.00 USD |
| `1D` | `0.9460` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 56,940.00 USD | 26,210.00 USD | 24,340.00 USD |
| `7D` | `0.9460` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD |
| `1D` | `0.9470` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 36,440.00 USD | 24,720.00 USD | 20,480.00 USD |
| `1D` | `0.9480` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 55,350.00 USD | 48,320.00 USD | 35,870.00 USD |
| `7D` | `0.9480` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 0.00 USD | 78,160.00 USD | 291,990.00 USD |
| `1D` | `0.9490` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 18,020.00 USD | 14,650.00 USD | 22,780.00 USD |
| `1D` | `0.9500` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 7,440.00 USD | 22,120.00 USD | 47,610.00 USD |
| `7D` | `0.9500` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 2,840.00 USD | 30,430.00 USD | 375,100.00 USD |
| `1D` | `0.9510` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 52,590.00 USD | 28,760.00 USD | 128,260.00 USD |
| `1D` | `0.9520` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 466.70 USD | 155.85 USD | 84,080.00 USD |
| `7D` | `0.9520` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 0.00 USD | 87,720.00 USD | 362,480.00 USD |
| `1D` | `0.9530` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 29,490.00 USD | 27,080.00 USD | 70,520.00 USD |
| `1D` | `0.9540` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 28,300.00 USD | 24,560.00 USD | 27,680.00 USD |
| `7D` | `0.9540` | 14,270,000.00 USD | 14,270,000.00 USD | 0.00 USD | 13,570.00 USD | 3,670.00 USD | 60,880.00 USD |
| `1D` | `0.9550` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 21,030.00 USD | 15,610.00 USD | 24,930.00 USD |
| `1D` | `0.9560` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 20,640.00 USD | 11,590.00 USD | 23,330.00 USD |
| `7D` | `0.9560` | 14,350,000.00 USD | 14,350,000.00 USD | 0.00 USD | 74,460.00 USD | 3,500.00 USD | 2,410.00 USD |
| `1D` | `0.9570` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 16,640.00 USD | 2,570.00 USD | 692.84 USD |
| `1D` | `0.9580` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 10,110.00 USD | 42,520.00 USD | 12,560.00 USD |
| `7D` | `0.9580` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 846,080.00 USD | 1,220.00 USD | 1,790.00 USD |
| `1D` | `0.9590` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 33,840.00 USD | 27,020.00 USD | 0.00 USD |
| `1D` | `0.9600` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 69,660.00 USD | 23,730.00 USD | 78,070.00 USD |
| `7D` | `0.9600` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 358,610.00 USD | 118,450.00 USD | 131,760.00 USD |
| `1D` | `0.9610` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 137,750.00 USD | 51,970.00 USD | 166,430.00 USD |
| `1D` | `0.9620` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 129,590.00 USD | 13,950.00 USD | 10,290.00 USD |
| `7D` | `0.9620` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 715,790.00 USD | 231,300.00 USD | 588,980.00 USD |
| `1D` | `0.9630` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 112,130.00 USD | 28,520.00 USD | 53,290.00 USD |
| `1D` | `0.9640` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 125,880.00 USD | 39,890.00 USD | 49,130.00 USD |
| `7D` | `0.9640` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 693,720.00 USD | 366,520.00 USD | 508,260.00 USD |
| `1D` | `0.9650` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 18,690.00 USD | 72,860.00 USD | 29,960.00 USD |
| `1D` | `0.9660` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 135,070.00 USD | 55,850.00 USD | 42,300.00 USD |
| `7D` | `0.9660` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 962,420.00 USD | 245,250.00 USD | 514,790.00 USD |
| `1D` | `0.9670` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 93,370.00 USD | 53,730.00 USD | 191,400.00 USD |
| `1D` | `0.9680` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 80,570.00 USD | 13,220.00 USD | 112,420.00 USD |
| `7D` | `0.9680` | 22,660,000.00 USD | 22,660,000.00 USD | 0.00 USD | 856,440.00 USD | 625,850.00 USD | 538,900.00 USD |
| `1D` | `0.9690` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 161,940.00 USD | 72,530.00 USD | 130,210.00 USD |
| `1D` | `0.9700` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 111,440.00 USD | 39,150.00 USD | 56,540.00 USD |
| `7D` | `0.9700` | 23,910,000.00 USD | 23,910,000.00 USD | 0.00 USD | 657,220.00 USD | 324,760.00 USD | 264,680.00 USD |
| `1D` | `0.9710` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 64,520.00 USD | 27,540.00 USD | 71,860.00 USD |
| `1D` | `0.9720` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 38,110.00 USD | 36,660.00 USD | 51,070.00 USD |
| `7D` | `0.9720` | 24,730,000.00 USD | 24,730,000.00 USD | 0.00 USD | 402,400.00 USD | 197,100.00 USD | 222,870.00 USD |
| `1D` | `0.9730` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 24,020.00 USD | 1,020.00 USD | 0.00 USD |
| `1D` | `0.9740` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 12,150.00 USD | 5,900.00 USD | 47,290.00 USD |
| `7D` | `0.9740` | 25,300,000.00 USD | 25,300,000.00 USD | 0.00 USD | 334,930.00 USD | 116,990.00 USD | 124,030.00 USD |
| `1D` | `0.9750` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 20,270.00 USD | 28,720.00 USD | 84,460.00 USD |
| `1D` | `0.9760` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 423.77 USD | 370.46 USD | 154.26 USD |
| `7D` | `0.9760` | 26,040,000.00 USD | 26,040,000.00 USD | 0.00 USD | 182,900.00 USD | 286,070.00 USD | 265,750.00 USD |
| `1D` | `0.9770` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 4,370.00 USD | 20,600.00 USD | 32,110.00 USD |
| `1D` | `0.9780` | 13,150,000.00 USD | 13,150,000.00 USD | 0.00 USD | 28,530.00 USD | 21,450.00 USD | 70,630.00 USD |
| `7D` | `0.9780` | 27,090,000.00 USD | 27,090,000.00 USD | 0.00 USD | 323,530.00 USD | 211,120.00 USD | 513,910.00 USD |
| `1D` | `0.9790` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 18,030.00 USD | 15,220.00 USD | 32,800.00 USD |
| `1D` | `0.9800` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 43,300.00 USD | 32,650.00 USD | 81,360.00 USD |
| `7D` | `0.9800` | 27,640,000.00 USD | 27,640,000.00 USD | 0.00 USD | 247,060.00 USD | 66,910.00 USD | 240,420.00 USD |
| `1D` | `0.9810` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 44,730.00 USD | 4,820.00 USD | 0.00 USD |
| `1D` | `0.9820` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 37,830.00 USD | 836.01 USD | 0.00 USD |
| `7D` | `0.9820` | 27,960,000.00 USD | 27,960,000.00 USD | 0.00 USD | 108,220.00 USD | 68,030.00 USD | 142,510.00 USD |
| `1D` | `0.9830` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 31,020.00 USD | 21,700.00 USD | 47.72 USD |
| `1D` | `0.9840` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 2,480.00 USD | 22,540.00 USD | 5,930.00 USD |
| `7D` | `0.9840` | 28,660,000.00 USD | 28,660,000.00 USD | 0.00 USD | 397,850.00 USD | 123,740.00 USD | 177,280.00 USD |
| `1D` | `0.9850` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 19,260.00 USD | 19,940.00 USD | 14,540.00 USD |
| `1D` | `0.9860` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 51,980.00 USD | 24,590.00 USD | 81,170.00 USD |
| `7D` | `0.9860` | 29,000,000.00 USD | 29,000,000.00 USD | 0.00 USD | 108,860.00 USD | 154,250.00 USD | 74,460.00 USD |
| `1D` | `0.9870` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 28,620.00 USD | 9,650.00 USD | 16,370.00 USD |
| `1D` | `0.9880` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 55,150.00 USD | 11,470.00 USD | 26,140.00 USD |
| `7D` | `0.9880` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 209,770.00 USD | 75,650.00 USD | 26,750.00 USD |
| `1D` | `0.9890` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 44,590.00 USD | 15,760.00 USD | 6,860.00 USD |
| `7D` | `0.9900` | 29,620,000.00 USD | 29,620,000.00 USD | 0.00 USD | 201,410.00 USD | 100,430.00 USD | 6,630.00 USD |
| `7D` | `0.9920` | 30,070,000.00 USD | 30,070,000.00 USD | 0.00 USD | 288,210.00 USD | 79,650.00 USD | 81,440.00 USD |
| `7D` | `0.9940` | 30,540,000.00 USD | 30,540,000.00 USD | 0.00 USD | 143,340.00 USD | 183,310.00 USD | 146,940.00 USD |
| `7D` | `0.9960` | 31,000,000.00 USD | 31,000,000.00 USD | 0.00 USD | 107,780.00 USD | 55,790.00 USD | 291,980.00 USD |
| `7D` | `0.9980` | 31,440,000.00 USD | 31,440,000.00 USD | 0.00 USD | 238,490.00 USD | 42,080.00 USD | 163,410.00 USD |
| `7D` | `1.00` | 31,650,000.00 USD | 31,650,000.00 USD | 0.00 USD | 94,210.00 USD | 53,610.00 USD | 65,960.00 USD |
| `7D` | `1.00` | 32,080,000.00 USD | 32,080,000.00 USD | 0.00 USD | 250,490.00 USD | 49,140.00 USD | 126,410.00 USD |
| `7D` | `1.00` | 32,430,000.00 USD | 32,430,000.00 USD | 0.00 USD | 148,700.00 USD | 47,010.00 USD | 157,970.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `557.84M` | Total OI Tokens: `632,814,631.1 SUI`
  * 1h OI Change: `-0.57%` | 4h OI Change: `-3.23%` | 24h OI Change: `-10.36%`
  * Exchange Breakdown: Binance=`99.16M` | Bybit=`74.79M` | OKX=`32.76M` | Hyperliquid=`29.49M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-14.35K` | Last 24h: `2.87K` | Last 3d: `42.29K` | Last 7d: `152.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0052%` | **USDT OKX** | `-0.0015%` |
| **USDT Bybit** | `-0.0266%` | **USDT KuCoin** | `0.0058%` |
| **USDT MEXC** | `0.0051%` | **USDT BingX** | `0.0052%` |
| **USDT Gate** | `-0.0097%` | **USDT Bitget** | `-0.0113%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `59.10%` | `40.90%` | `1.44` | 9,940,000.00 USD |
| `15M` | `Binance` | `56.99%` | `43.01%` | `1.33` | 4,370,000.00 USD |
| `15M` | `OKX` | `50.54%` | `49.46%` | `1.02` | 1,200,000.00 USD |
| `15M` | `Bybit` | `61.72%` | `38.28%` | `1.61` | 903,150.00 USD |
| `15M` | `KuCoin` | `48.82%` | `51.18%` | `0.95` | 164,080.00 USD |
| `15M` | `Gate` | `34.76%` | `65.24%` | `0.53` | 736,740.00 USD |
| `15M` | `Bitget` | `80.24%` | `19.76%` | `4.06` | 339,140.00 USD |
| `15M` | `BingX` | `67.38%` | `32.62%` | `2.07` | 100,190.00 USD |
| `15M` | `MEXC` | `64.93%` | `35.07%` | `1.85` | 66,500.00 USD |
| `15M` | `Bitunix` | `55.04%` | `44.96%` | `1.22` | 182,730.00 USD |
| `15M` | `Hyperliquid` | `79.63%` | `20.37%` | `3.91` | 1,570,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.69%` | `49.31%` | `1.03` | 159,170.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 812.13 USD |
| `15M` | `HTX` | `39.57%` | `60.43%` | `0.65` | 24,300.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `68.59%` | `31.41%` | `2.18` | 67,550.00 USD |
| `15M` | `Aster` | `82.56%` | `17.44%` | `4.73` | 20,890.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `5.39%` | `94.61%` | `0.06` | 43,470.00 USD |
| `15M` | `Whale Positions` | `56.99%` | `43.01%` | `1.33` | 4,370,000.00 USD |
| `15M` | `Global Accounts` | `59.10%` | `40.90%` | `1.44` | 9,940,000.00 USD |
| `1H` | `SUI` | `54.18%` | `45.82%` | `1.18` | 40,900,000.00 USD |
| `1H` | `Binance` | `54.1%` | `45.9%` | `1.18` | 16,190,000.00 USD |
| `1H` | `OKX` | `45.88%` | `54.12%` | `0.85` | 5,380,000.00 USD |
| `1H` | `Bybit` | `57.93%` | `42.07%` | `1.38` | 4,990,000.00 USD |
| `1H` | `KuCoin` | `49.77%` | `50.23%` | `0.99` | 768,670.00 USD |
| `1H` | `Gate` | `41.8%` | `58.2%` | `0.72` | 1,770,000.00 USD |
| `1H` | `Bitget` | `56.51%` | `43.49%` | `1.30` | 1,880,000.00 USD |
| `1H` | `BingX` | `65.06%` | `34.94%` | `1.86` | 321,940.00 USD |
| `1H` | `MEXC` | `59.77%` | `40.23%` | `1.49` | 460,840.00 USD |
| `1H` | `Bitunix` | `54.19%` | `45.81%` | `1.18` | 542,920.00 USD |
| `1H` | `Hyperliquid` | `60.88%` | `39.12%` | `1.56` | 7,430,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.45%` | `51.55%` | `0.94` | 490,620.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `13.6%` | `86.4%` | `0.16` | 145,940.00 USD |
| `1H` | `HTX` | `45.03%` | `54.97%` | `0.82` | 83,400.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `61.77%` | `38.23%` | `1.62` | 139,290.00 USD |
| `1H` | `Aster` | `63.32%` | `36.68%` | `1.73` | 131,640.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.46%` | `49.54%` | `1.02` | 184,880.00 USD |
| `1H` | `Whale Positions` | `54.1%` | `45.9%` | `1.18` | 16,190,000.00 USD |
| `1H` | `Global Accounts` | `54.18%` | `45.82%` | `1.18` | 40,900,000.00 USD |
| `4H` | `SUI` | `47.33%` | `52.67%` | `0.90` | 90,940,000.00 USD |
| `4H` | `Binance` | `51.26%` | `48.74%` | `1.05` | 32,660,000.00 USD |
| `4H` | `OKX` | `49.43%` | `50.57%` | `0.98` | 6,770,000.00 USD |
| `4H` | `Bybit` | `42.81%` | `57.19%` | `0.75` | 8,270,000.00 USD |
| `4H` | `KuCoin` | `48.96%` | `51.04%` | `0.96` | 445,570.00 USD |
| `4H` | `Gate` | `42.97%` | `57.03%` | `0.75` | 1,290,000.00 USD |
| `4H` | `Bitget` | `41.76%` | `58.24%` | `0.72` | 2,970,000.00 USD |
| `4H` | `BingX` | `35.67%` | `64.33%` | `0.55` | 4,120,000.00 USD |
| `4H` | `MEXC` | `48.04%` | `51.96%` | `0.92` | 20,440,000.00 USD |
| `4H` | `Bitunix` | `44.01%` | `55.99%` | `0.79` | 8,020,000.00 USD |
| `4H` | `Hyperliquid` | `49.06%` | `50.94%` | `0.96` | 1,460,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.99%` | `47.01%` | `1.13` | 2,250,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `17.76%` | `82.24%` | `0.22` | 1,650,000.00 USD |
| `4H` | `HTX` | `55.26%` | `44.74%` | `1.24` | 102,360.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `76.54%` | `23.46%` | `3.26` | 38,650.00 USD |
| `4H` | `Aster` | `79.93%` | `20.07%` | `3.98` | 290,590.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `38.86%` | `61.14%` | `0.64` | 156,400.00 USD |
| `4H` | `Whale Positions` | `51.26%` | `48.74%` | `1.05` | 32,660,000.00 USD |
| `4H` | `Global Accounts` | `47.33%` | `52.67%` | `0.90` | 90,940,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.8970` | `0.8976` | `0.8970` | `0.9022` | `0.8950` | 2,019,135.62 USD | 771,181.10 USD | 1,247,954.52 USD | -476,773.41 USD | `-23.61%` | `11B / 22S` |
| `5:00 UTC` | `0.8966` | `0.8946` | `0.8966` | `0.8979` | `0.8913` | 2,000,675.78 USD | 906,317.59 USD | 1,094,358.19 USD | -188,040.60 USD | `-9.40%` | `9B / 13S` |
| `0:00 UTC` | `0.8931` | `0.8934` | `0.8931` | `0.8971` | `0.8900` | 1,974,065.79 USD | 794,673.98 USD | 1,179,391.81 USD | -384,717.84 USD | `-19.49%` | `2B / 21S` |
| `5:00 UTC` | `0.8911` | `0.8910` | `0.8911` | `0.8931` | `0.8898` | 1,611,113.83 USD | 837,255.00 USD | 773,858.84 USD | 63,396.16 USD | `+3.93%` | `8B / 3S` |
| `0:00 UTC` | `0.8831` | `0.8870` | `0.8831` | `0.8949` | `0.8817` | 3,990,178.39 USD | 1,362,331.47 USD | 2,627,846.92 USD | -1,265,515.46 USD | `-31.72%` | `5B / 47S` |
| `5:00 UTC` | `0.8842` | `0.8841` | `0.8842` | `0.8867` | `0.8819` | 2,580,312.70 USD | 1,301,087.80 USD | 1,279,224.90 USD | 21,862.90 USD | `+0.85%` | `8B / 6S` |
| `0:00 UTC` | `0.8841` | `0.8838` | `0.8841` | `0.8874` | `0.8802` | 2,392,175.76 USD | 1,120,822.52 USD | 1,271,353.25 USD | -150,530.73 USD | `-6.29%` | `11B / 13S` |
| `5:00 UTC` | `0.8845` | `0.8853` | `0.8845` | `0.8882` | `0.8831` | 1,835,307.01 USD | 895,840.06 USD | 939,466.95 USD | -43,626.90 USD | `-2.38%` | `5B / 13S` |
| `0:00 UTC` | `0.8830` | `0.8831` | `0.8830` | `0.8848` | `0.8809` | 2,001,953.56 USD | 1,149,882.09 USD | 852,071.47 USD | 297,810.61 USD | `+14.88%` | `5B / 4S` |
| `5:00 UTC` | `0.8821` | `0.8819` | `0.8821` | `0.8829` | `0.8813` | 276,101.81 USD | 153,385.68 USD | 122,716.13 USD | 30,669.55 USD | `+11.11%` | `4B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:49` | `Volume 5.0M SUI` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.9287` | 0.00 USD | 0.00 USD |
| `10-28 19:47` | `Range 0.0025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.9190` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Volume 5.0M SUI` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.9164` | 1,200,000.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.0025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9184` | 316,000.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9184` | 0.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.0025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.9184` | 316,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.0025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9216` | 447,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.0025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.9216` | 447,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9270` | 0.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.0025` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.9363` | 244,000.00 USD | 0.00 USD |
| `10-28 16:37` | `Volume 5.0M SUI` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9388` | 1,300,000.00 USD | 0.00 USD |
| `10-28 15:31` | `Range 0.0025` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.9459` | 418,000.00 USD | 0.00 USD |
| `10-28 15:15` | `Range 0.0025` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.9429` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.0025` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.9479` | 312,000.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.0025` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.9479` | 312,000.00 USD | 0.00 USD |
| `10-28 13:59` | `Volume 5.0M SUI` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.9479` | 2,000,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.0025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.9455` | 0.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9318` | 0.00 USD | 0.00 USD |
| `10-28 11:50` | `Range 0.0025` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.9399` | 1,200,000.00 USD | 0.00 USD |
| `10-28 11:10` | `Range 0.0025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.9359` | 0.00 USD | 0.00 USD |
| `10-28 11:10` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9332` | 0.00 USD | 0.00 USD |
| `10-28 10:36` | `Range 0.0025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.9342` | 0.00 USD | 0.00 USD |
| `10-28 07:42` | `Range 0.0025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.9370` | 450,000.00 USD | 0.00 USD |
| `10-28 06:51` | `Range 0.0025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.9348` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -45,550.00 USD | -45,510.00 USD | **`DISTRIBUTION`** |
| `15m` | -18,490.00 USD | 84,760.00 USD | **`ACCUMULATION`** |
| `30m` | 205,420.00 USD | 485,840.00 USD | **`ACCUMULATION`** |
| `1h` | 522,400.00 USD | -1,920,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 20,490.00 USD | -4,020,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,360,000.00 USD | -7,280,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 2,330,000.00 USD | -3,620,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 2,550,000.00 USD | -15,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,630,000.00 USD | -26,060,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,560,000.00 USD | -31,630,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -26,240,000.00 USD | -91,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -153,450,000.00 USD | -492,230,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-45.55K` | 15m=`-18.49K` | 1h=`+522.40K` | 24h=`-8.56M`
* Futures Capital Netflows: 5m=`-45.51K` | 15m=`+84.76K` | 1h=`-1.92M` | 24h=`-31.63M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.9074` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.2929` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.91`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9128` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.11` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.09`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9174`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
