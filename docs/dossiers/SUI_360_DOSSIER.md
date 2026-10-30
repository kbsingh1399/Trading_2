# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 08:15:37 IST` (`2026-10-30 02:45:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8678` | `0.8690` | `0.8651` | `0.8653` | `1,359,007` | 1,178,975.54 USD | 177,697.66 USD | `+15.07%` | -15,278,617.15 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.8653` | `0.8707` | `0.8652` | `0.8689` | `773,222` | 671,895.50 USD | 135,316.61 USD | `+20.14%` | -15,143,300.54 USD | `+0.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.8689` | `0.8704` | `0.8685` | `0.8697` | `370,167` | 321,930.79 USD | 23,338.08 USD | `+7.25%` | -15,119,962.47 USD | `-0.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8556` | `0.8595` | `0.8482` | `0.8593` | `3,481,232` | 2,970,160.51 USD | 244,482.37 USD | `+8.23%` | -15,836,211.50 USD | `+0.41` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8592` | `0.8693` | `0.8592` | `0.8678` | `3,552,914` | 3,068,721.14 USD | 379,896.70 USD | `+12.38%` | -15,456,314.81 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8678` | `0.8707` | `0.8651` | `0.8696` | `2,499,466` | 2,170,254.59 USD | 338,865.31 USD | `+15.61%` | -15,117,449.50 USD | `+0.46` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.8693` | `0.8739` | `0.8264` | `0.8548` | `61,139,792` | 51,862,497.60 USD | -6,331,760.89 USD | `-12.21%` | -15,789,847.21 USD | `-2.86` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8549` | `0.8637` | `0.8453` | `0.8555` | `17,720,786` | 15,162,870.44 USD | -425,226.29 USD | `-2.80%` | -16,215,073.50 USD | `+0.15` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8556` | `0.8707` | `0.8482` | `0.8696` | `9,533,657` | 8,209,175.45 USD | 963,223.25 USD | `+11.73%` | -15,251,850.25 USD | `+0.84` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -565,079.35 USD | `-1.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,267,514.18 USD | `-1.80` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8739` | `0.8264` | `0.8697` | `88,397,119` | 75,237,051.50 USD | -5,796,255.77 USD | `-7.70%` | -14,063,769.95 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -20,484.57 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | 2,008,232.35 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -565,079.35 USD | `-1.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,267,514.18 USD | `-1.80` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8739` | `0.8264` | `0.8697` | `88,397,119` | 75,237,051.50 USD | -5,796,255.77 USD | `-7.70%` | -14,063,769.95 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `0.8698` | `1727.3000` | 1,502.35 USD | 38,955.92 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8699` | `2123.2000` | 1,847.01 USD | 28,799.05 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.8699` | `1149.5000` | 999.94 USD | 29,798.99 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8699` | `7072.4000` | 6,152.00 USD | 35,950.99 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.8699` | `1727.4000` | 1,502.58 USD | 37,453.57 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8700` | `2873.4000` | 2,499.94 USD | 24,062.67 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8700` | `153.3000` | 133.37 USD | 24,196.05 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8700` | `1153.3000` | 1,003.38 USD | 25,199.43 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8700` | `1727.3000` | 1,502.75 USD | 26,702.18 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8700` | `287.2000` | 249.86 USD | 26,952.04 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8701` | `1727.3000` | 1,503.01 USD | 8,179.69 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8701` | `5758.3000` | 5,010.53 USD | 13,190.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8701` | `7895.3000` | 6,869.62 USD | 20,059.84 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `0.8701` | `1727.3000` | 1,502.89 USD | 21,562.73 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8702` | `1727.3000` | 1,503.15 USD | 4,943.80 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8702` | `696.0000` | 605.67 USD | 5,549.48 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8702` | `1295.4000` | 1,127.21 USD | 6,676.68 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8703` | `2302.8000` | 2,004.15 USD | 3,006.21 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8703` | `499.2000` | 434.45 USD | 3,440.66 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `0.8704` | `120.0000` | 104.45 USD | 104.45 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.8704` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.87` | `0.00%` | `-` |
| `BID` | `0.8704` | `1151.3000` | 1,002.06 USD | 1,002.06 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `0.8705` | `735.4000` | 640.19 USD | 1,092.83 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8705` | `400.0000` | 348.20 USD | 452.64 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8706` | `1727.4000` | 1,503.86 USD | 2,596.69 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8707` | `114.8000` | 99.96 USD | 11,321.76 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8707` | `1842.1000` | 1,603.97 USD | 11,221.80 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.8707` | `114.8000` | 99.96 USD | 9,617.82 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8707` | `114.8000` | 99.96 USD | 9,517.86 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8707` | `114.8000` | 99.96 USD | 9,417.91 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8707` | `5753.6000` | 5,009.54 USD | 9,317.95 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8707` | `238.6000` | 207.74 USD | 4,308.41 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8707` | `1727.4000` | 1,503.98 USD | 4,100.66 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8708` | `1727.0000` | 1,503.87 USD | 15,823.73 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8708` | `495.6000` | 431.56 USD | 14,319.86 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8708` | `114.8000` | 99.97 USD | 13,888.30 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8708` | `114.8000` | 99.96 USD | 13,788.33 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8708` | `114.8000` | 99.96 USD | 13,688.37 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8708` | `2603.1000` | 2,266.65 USD | 13,588.41 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.8709` | `4593.5000` | 4,000.30 USD | 20,098.26 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8709` | `314.9000` | 274.23 USD | 16,097.96 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:13:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `671` | `0xb83d...6e36` | `SHORT` | 3,322,007.35 USD | `3,817,609.40` | `1.11` | `0.8697` | `35.90` | 896,727.97 USD | `+26.99%` | `3X Cross` |
| `1005` | `0xa2ce...3126` | `LONG` | 2,174,284.04 USD | `2,500,010.40` | `0.8597` | `0.8697` | `0.000000` | 25,077.51 USD | `+1.15%` | `10X Cross` |
| `1535` | `0x9946...0852` | `SHORT` | 1,396,913.17 USD | `1,604,743.50` | `1.08` | `0.8697` | `1.93` | 334,841.07 USD | `+23.97%` | `10X Cross` |
| `1900` | `0x9df2...c665` | `SHORT` | 1,043,928.00 USD | `1,200,000.00` | `0.7465` | `0.8697` | `26.90` | -148,075.60 USD | `-14.18%` | `10X Cross` |
| `1976` | `0x9aa5...58af` | `SHORT` | 1,004,408.14 USD | `1,154,372.70` | `1.14` | `0.8697` | `8.84` | 310,842.31 USD | `+30.95%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9477` | 5,004.13 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.00K USD at 0.9477 USD [API] | `2026-10-28 21:02:33` |
| `ANNOUNCEMENT` | `INFO` | `0.9548` | 34.75 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.03K USD at 0.9548 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `0.9548` | 9,356.46 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 9.36K USD at 0.9548 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `0.9486` | 6,358.94 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.36K USD at 0.9486 USD [API] | `2026-10-28 21:13:42` |
| `ANNOUNCEMENT` | `INFO` | `0.9454` | 6,531.87 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 6.53K USD at 0.9454 USD [API] | `2026-10-28 21:31:12` |
| `ANNOUNCEMENT` | `INFO` | `0.9522` | 10,274.00 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.27K USD at 0.9522 USD [API] | `2026-10-28 21:52:30` |
| `ANNOUNCEMENT` | `INFO` | `0.9522` | 5,005.05 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9522 USD [API] | `2026-10-28 21:52:30` |
| `ANNOUNCEMENT` | `INFO` | `0.9480` | 6,110.27 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 6.11K USD at 0.9480 USD [API] | `2026-10-28 22:14:07` |
| `ANNOUNCEMENT` | `INFO` | `0.9435` | 5,005.82 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9435 USD [API] | `2026-10-28 23:04:55` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9682` (Vol: 265,800.00 USD, Dist: `+10.09%`) | Long MP=`0.8652` (Vol: 154,300.00 USD, Dist: `--1.62%`)
  * 48H Horizon: Short MP=`0.9707` (Vol: 232,500.00 USD, Dist: `+10.37%`) | Long MP=`0.8657` (Vol: 154,300.00 USD, Dist: `--1.57%`)
  * 3D Horizon: Short MP=`0.9707` (Vol: 232,500.00 USD, Dist: `+10.37%`) | Long MP=`0.8657` (Vol: 154,300.00 USD, Dist: `--1.57%`)
  * 7D Horizon: Short MP=`0.9713` (Vol: 513,800.00 USD, Dist: `+10.43%`) | Long MP=`0.8660` (Vol: 154,300.00 USD, Dist: `--1.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1845` | 1,090.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 291.48 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 1,820.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 1,160.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 5,550.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2065` | 1,030.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 303.72 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 1,740.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 745.68 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 4,770.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 1,230.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 314.11 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 286.50 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 100.20 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 130.04 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3055` | 3,100.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3095` | 200.99 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3105` | 621.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3135` | 1,230.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3325` | 110.02 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3455` | 1,130.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 31,070.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3565` | 245.45 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3625` | 4,020.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3715` | 2,500.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3755` | 408.24 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3765` | 112.95 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3775` | 154.55 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3835` | 6,520.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3935` | 243.26 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 276.85 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3975` | 130.98 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 3,360.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4115` | 31,980.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 5,500.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4165` | 29,160.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 1,570.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 467.50 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4355` | 871.17 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4415` | 43,980.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 219.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 692.53 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 105.25 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4495` | 449.50 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 1,020.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4545` | 4,540.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 3,330.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 322.35 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 1,720.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4775` | 464.46 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4795` | 844.88 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4805` | 14,250.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 166.70 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 4,040.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 1,380.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 4,050.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 70,630.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 8,390.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 5,680.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 5,760.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 1,680.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5225` | 577.88 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5235` | 7,650.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 1,220.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 264.06 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5305` | 123,610.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 113.47 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5365` | 1,630.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 127.57 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 11,120.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 162,050.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 701.51 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 8,240.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5575` | 5,300.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 441.84 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 534.03 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5645` | 249.57 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 6,720.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 182.72 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 217.37 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 4,660.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 6,980.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 357.12 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 1,070.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 355.57 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 608.61 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5975` | 4,360.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 419.73 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 4,310.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 323.79 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6035` | 1,220.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 886.10 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 13,930.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 438.73 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 112.33 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 2,110.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,980.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 14,440.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 1,050.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6205` | 620.50 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6215` | 444.75 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 263.07 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,070.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 256.55 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 843.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 1,100.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6385` | 671.77 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 33,040.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 1,260.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,190.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 3,200.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 668.34 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 7,360.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 106.75 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6525` | 4,590.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 127,900.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 6,700.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 676.54 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 10,020.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6605` | 841.81 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 4,370.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 1,960.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 528.73 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 3,050.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 135.71 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 337.36 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 2,240.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,280.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 1,190.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 9,150.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 122.94 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 44,890.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 28,920.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 8,150.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 15,920.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 11,170.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 348,240.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 22,010.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 44,250.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 10,590.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 3,600.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 7,670.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,700.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,630.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 1,670.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 10,190.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 169.67 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 912.73 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 787.73 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,020.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 570.08 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 25,230.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 283.22 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 927.55 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 297.23 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 12,340.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 4,890.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7185` | 126.96 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 420.19 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 8,450.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,990.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 7,510.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 311.60 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 3,410.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 35,890.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 432.58 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 907.93 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 8,360.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 3,450.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 203.11 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,480.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 5,210.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 785,210.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 421.12 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 2,160.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7465` | 359.96 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 264.86 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 1,250.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 1,750.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,900.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7625` | 1,170.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 11,990,000.00 USD | 11,990,000.00 USD | 37,590.00 USD | 14,770.00 USD | 934.78 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 5,110.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 3,510.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 11,940,000.00 USD | 11,940,000.00 USD | 556.58 USD | 23,090.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,480.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 11,900,000.00 USD | 11,900,000.00 USD | 1,280.00 USD | 177.87 USD | 18,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 25,580.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 207.19 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 11,880,000.00 USD | 11,880,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 150,510.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 11,880,000.00 USD | 11,880,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,940.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 5,230.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7745` | 2,970.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 13,940.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 3,510.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 8,980.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 5,390.00 USD | 36.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 993,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7810` | 11,870,000.00 USD | 11,870,000.00 USD | 0.00 USD | 185.50 USD | 5,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 992,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 21,600.00 USD | 988,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7850` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 587.33 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7850` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7855` | 108.63 USD | 967,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 966,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7870` | 5,550,000.00 USD | 5,550,000.00 USD | 16,780.00 USD | 318.35 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7870` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 963,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7890` | 5,530,000.00 USD | 5,530,000.00 USD | 10,020.00 USD | 12,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 11,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 963,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7910` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 4,750.00 USD | 285.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 29,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 1,280.00 USD | 959,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 7,330.00 USD | 958,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7930` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 12,600.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 12,880.00 USD | 77,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 950,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7945` | 894.61 USD | 950,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7950` | 5,460,000.00 USD | 5,460,000.00 USD | 13,930.00 USD | 266.53 USD | 14,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 18,870.00 USD | 51,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 31,180.00 USD | 949,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7965` | 342,330.00 USD | 918,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 5,430,000.00 USD | 5,430,000.00 USD | 3,300.00 USD | 9,330.00 USD | 22,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 11,630,000.00 USD | 11,630,000.00 USD | 12,100.00 USD | 0.00 USD | 38,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,580.00 USD | 575,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7985` | 39,870.00 USD | 568,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7990` | 5,390,000.00 USD | 5,390,000.00 USD | 505.25 USD | 322.55 USD | 18,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 11,580,000.00 USD | 11,580,000.00 USD | 488.55 USD | 0.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 12,940.00 USD | 528,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8005` | 906.49 USD | 515,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8010` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 10,940.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 11,570,000.00 USD | 11,570,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 6,810.00 USD | 514,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 6,050.00 USD | 507,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,680.00 USD | 501,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 16,830.00 USD | 493,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8050` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 6,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 11,520,000.00 USD | 11,520,000.00 USD | 2,040.00 USD | 15,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 190.90 USD | 477,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 476,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 5,340,000.00 USD | 5,340,000.00 USD | 12,740.00 USD | 14,260.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 469,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 467,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8090` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 130,110.00 USD | 445,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 314,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8110` | 5,300,000.00 USD | 5,300,000.00 USD | 40,190.00 USD | 6,030.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 11,490,000.00 USD | 11,490,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,970.00 USD | 312,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8125` | 1,160.00 USD | 309,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8130` | 5,230,000.00 USD | 5,230,000.00 USD | 23,290.00 USD | 13,030.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 11,390,000.00 USD | 11,390,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 308,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8145` | 2,500.00 USD | 304,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 5,180,000.00 USD | 5,180,000.00 USD | 66,820.00 USD | 25,820.00 USD | 100,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 11,310,000.00 USD | 11,310,000.00 USD | 135,770.00 USD | 51,810.00 USD | 124,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 46,410.00 USD | 302,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8165` | 3,590.00 USD | 255,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8170` | 4,990,000.00 USD | 4,990,000.00 USD | 68,580.00 USD | 28,480.00 USD | 79,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 11,000,000.00 USD | 11,000,000.00 USD | 91,050.00 USD | 25,080.00 USD | 78,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 102,870.00 USD | 252,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8185` | 491.10 USD | 149,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8190` | 4,810,000.00 USD | 4,810,000.00 USD | 12,140.00 USD | 6,480.00 USD | 15,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 10,810,000.00 USD | 10,810,000.00 USD | 195,400.00 USD | 53,380.00 USD | 47,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,110.00 USD | 148,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8205` | 1,300.00 USD | 147,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8210` | 4,780,000.00 USD | 4,780,000.00 USD | 16,970.00 USD | 30,830.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 10,510,000.00 USD | 10,510,000.00 USD | 138,580.00 USD | 58,400.00 USD | 152,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 3,080.00 USD | 146,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 4,690,000.00 USD | 4,690,000.00 USD | 11,730.00 USD | 18,140.00 USD | 20,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 10,160,000.00 USD | 10,160,000.00 USD | 37,880.00 USD | 37,160.00 USD | 64,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 18,280.00 USD | 143,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 4,640,000.00 USD | 4,640,000.00 USD | 18,440.00 USD | 8,600.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 10,020,000.00 USD | 10,020,000.00 USD | 187,510.00 USD | 30,370.00 USD | 126,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 317.82 USD | 125,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8270` | 4,590,000.00 USD | 4,590,000.00 USD | 29,570.00 USD | 10,040.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 9,680,000.00 USD | 9,680,000.00 USD | 147,770.00 USD | 51,050.00 USD | 63,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 124,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 120,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8290` | 4,540,000.00 USD | 4,540,000.00 USD | 12,280.00 USD | 15,940.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 9,410,000.00 USD | 9,410,000.00 USD | 89,470.00 USD | 42,420.00 USD | 82,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8310` | 4,460,000.00 USD | 4,460,000.00 USD | 25,970.00 USD | 22,490.00 USD | 59,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 9,200,000.00 USD | 9,200,000.00 USD | 36,870.00 USD | 32,050.00 USD | 26,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 4,350,000.00 USD | 4,350,000.00 USD | 43,050.00 USD | 23,450.00 USD | 42,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 9,100,000.00 USD | 9,100,000.00 USD | 150,740.00 USD | 87,770.00 USD | 198,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8350` | 4,240,000.00 USD | 4,240,000.00 USD | 23,790.00 USD | 20,000.00 USD | 22,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 8,670,000.00 USD | 8,670,000.00 USD | 77,100.00 USD | 17,250.00 USD | 84,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8370` | 4,180,000.00 USD | 4,180,000.00 USD | 85,240.00 USD | 18,990.00 USD | 30,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 8,490,000.00 USD | 8,490,000.00 USD | 146,890.00 USD | 64,240.00 USD | 102,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 4,040,000.00 USD | 4,040,000.00 USD | 70,320.00 USD | 36,150.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 8,170,000.00 USD | 8,170,000.00 USD | 24,790.00 USD | 89,740.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 3,890,000.00 USD | 3,890,000.00 USD | 79,140.00 USD | 23,550.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 7,980,000.00 USD | 7,980,000.00 USD | 59,670.00 USD | 41,980.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8430` | 3,770,000.00 USD | 3,770,000.00 USD | 29,850.00 USD | 50,900.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 7,850,000.00 USD | 7,850,000.00 USD | 81,850.00 USD | 112,960.00 USD | 30,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 3,660,000.00 USD | 3,660,000.00 USD | 11,600.00 USD | 34,120.00 USD | 115,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 7,630,000.00 USD | 7,630,000.00 USD | 43,800.00 USD | 115,170.00 USD | 219,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 3,500,000.00 USD | 3,500,000.00 USD | 62,880.00 USD | 76,000.00 USD | 87,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 7,250,000.00 USD | 7,250,000.00 USD | 27,720.00 USD | 6,020.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 3,280,000.00 USD | 3,280,000.00 USD | 64,500.00 USD | 68,710.00 USD | 180,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 7,180,000.00 USD | 7,180,000.00 USD | 87,880.00 USD | 78,940.00 USD | 151,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8510` | 2,960,000.00 USD | 2,960,000.00 USD | 79,800.00 USD | 60,360.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 6,860,000.00 USD | 6,860,000.00 USD | 95,990.00 USD | 42,650.00 USD | 151,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 2,760,000.00 USD | 2,760,000.00 USD | 83,020.00 USD | 52,480.00 USD | 103,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 6,570,000.00 USD | 6,570,000.00 USD | 30,570.00 USD | 52,520.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 2,520,000.00 USD | 2,520,000.00 USD | 58,930.00 USD | 11,700.00 USD | 17,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 6,460,000.00 USD | 6,460,000.00 USD | 78,320.00 USD | 63,400.00 USD | 93,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,430,000.00 USD | 2,430,000.00 USD | 106,410.00 USD | 43,970.00 USD | 124.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 6,220,000.00 USD | 6,220,000.00 USD | 99,680.00 USD | 166,050.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,280,000.00 USD | 2,280,000.00 USD | 144,580.00 USD | 97,280.00 USD | 31,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 5,950,000.00 USD | 5,950,000.00 USD | 51,400.00 USD | 69,250.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,010,000.00 USD | 2,010,000.00 USD | 37,090.00 USD | 47,640.00 USD | 641.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 5,810,000.00 USD | 5,810,000.00 USD | 36,870.00 USD | 174,840.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 1,920,000.00 USD | 1,920,000.00 USD | 53,710.00 USD | 147,460.00 USD | 278,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 5,570,000.00 USD | 5,570,000.00 USD | 30,710.00 USD | 78,200.00 USD | 388,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8650` | 1,440,000.00 USD | 1,440,000.00 USD | 248,690.00 USD | 34,470.00 USD | 72,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 5,070,000.00 USD | 5,070,000.00 USD | 313,070.00 USD | 110,550.00 USD | 311,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8670` | 1,090,000.00 USD | 1,090,000.00 USD | 41,460.00 USD | 20,170.00 USD | 125.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 4,340,000.00 USD | 4,340,000.00 USD | 159,120.00 USD | 41,080.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,030,000.00 USD | 1,030,000.00 USD | 148,850.00 USD | 87,020.00 USD | 112,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 4,080,000.00 USD | 4,080,000.00 USD | 182,190.00 USD | 9,930.00 USD | 413,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 677,070.00 USD | 677,070.00 USD | 93,860.00 USD | 54,700.00 USD | 349,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 3,470,000.00 USD | 3,470,000.00 USD | 604,760.00 USD | 0.00 USD | 396,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 178,520.00 USD | 178,520.00 USD | 0.00 USD | 0.00 USD | 74,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 2,470,000.00 USD | 2,470,000.00 USD | 333,320.00 USD | 73,820.00 USD | 394,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 103,640.00 USD | 103,640.00 USD | 0.00 USD | 0.00 USD | 103,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,670,000.00 USD | 1,670,000.00 USD | 643,280.00 USD | 0.00 USD | 324,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 83.36 USD | 83.36 USD | 0.00 USD | 0.00 USD | 83.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 700,590.00 USD | 700,590.00 USD | 398,780.00 USD | 0.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8790` | 6,790.00 USD | 6,790.00 USD | 6,560.00 USD | 0.00 USD | 222.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8790` | 13,570.00 USD | 13,570.00 USD | 6,560.00 USD | 0.00 USD | 222.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 299,490.00 USD | 299,490.00 USD | 296,940.00 USD | 0.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8810` | 19,190.00 USD | 19,190.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8810` | 31,770.00 USD | 31,770.00 USD | 26,040.00 USD | 0.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8830` | 20,420.00 USD | 20,420.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8830` | 65,800.00 USD | 65,800.00 USD | 27,880.00 USD | 0.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8850` | 22,460.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8850` | 73,560.00 USD | 73,560.00 USD | 0.00 USD | 0.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8870` | 22,990.00 USD | 22,990.00 USD | 0.00 USD | 0.00 USD | 530.85 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8875` | 2,740.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8885` | 1,570.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8890` | 957,850.00 USD | 957,850.00 USD | 884,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8910` | 220,290.00 USD | 220,290.00 USD | 186,060.00 USD | 10,900.00 USD | 347.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8910` | 1,760,000.00 USD | 1,760,000.00 USD | 806,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8930` | 264,950.00 USD | 264,950.00 USD | 44,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8930` | 3,530,000.00 USD | 3,530,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8935` | 245.27 USD | 4,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8950` | 444,180.00 USD | 444,180.00 USD | 98,920.00 USD | 48,760.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 4,300,000.00 USD | 4,300,000.00 USD | 719,730.00 USD | 56,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8965` | 187.46 USD | 4,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8970` | 466,400.00 USD | 466,400.00 USD | 0.00 USD | 22,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8970` | 5,020,000.00 USD | 5,020,000.00 USD | 659,500.00 USD | 54,550.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8985` | 4,360.00 USD | 9,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8990` | 948,300.00 USD | 948,300.00 USD | 51,680.00 USD | 152,190.00 USD | 278,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8990` | 5,730,000.00 USD | 5,730,000.00 USD | 308,910.00 USD | 64,400.00 USD | 340,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9010` | 1,530,000.00 USD | 1,530,000.00 USD | 249,240.00 USD | 99,300.00 USD | 230,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 6,270,000.00 USD | 6,270,000.00 USD | 207,550.00 USD | 109,410.00 USD | 216,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9015` | 7,830.00 USD | 16,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9030` | 1,660,000.00 USD | 1,660,000.00 USD | 3,140.00 USD | 76,840.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9030` | 6,350,000.00 USD | 6,350,000.00 USD | 5,880.00 USD | 78,550.00 USD | 860.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9050` | 2,050,000.00 USD | 2,050,000.00 USD | 144,360.00 USD | 134,060.00 USD | 111,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9050` | 6,690,000.00 USD | 6,690,000.00 USD | 122,230.00 USD | 0.00 USD | 218,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9070` | 2,400,000.00 USD | 2,400,000.00 USD | 111,680.00 USD | 55,120.00 USD | 175,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 7,030,000.00 USD | 7,030,000.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9090` | 2,580,000.00 USD | 2,580,000.00 USD | 167,160.00 USD | 11,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 7,380,000.00 USD | 7,380,000.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9110` | 2,680,000.00 USD | 2,680,000.00 USD | 70,890.00 USD | 34,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 7,690,000.00 USD | 7,690,000.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9130` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 62,740.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 7,840,000.00 USD | 7,840,000.00 USD | 80,230.00 USD | 62,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 21,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9150` | 3,270,000.00 USD | 3,270,000.00 USD | 119,590.00 USD | 92,390.00 USD | 299,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 8,230,000.00 USD | 8,230,000.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9170` | 3,550,000.00 USD | 3,550,000.00 USD | 106,060.00 USD | 107,790.00 USD | 62,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 8,350,000.00 USD | 8,350,000.00 USD | 123,530.00 USD | 2,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9175` | 2,910.00 USD | 23,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9190` | 3,630,000.00 USD | 3,630,000.00 USD | 26,960.00 USD | 27,310.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 8,820,000.00 USD | 8,820,000.00 USD | 296,480.00 USD | 60,800.00 USD | 104,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9210` | 3,870,000.00 USD | 3,870,000.00 USD | 48,420.00 USD | 60,370.00 USD | 128,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 9,140,000.00 USD | 9,140,000.00 USD | 128,930.00 USD | 18,660.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9230` | 4,450,000.00 USD | 4,450,000.00 USD | 230,840.00 USD | 77,080.00 USD | 272,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 9,600,000.00 USD | 9,600,000.00 USD | 51,510.00 USD | 66,370.00 USD | 341,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9250` | 4,810,000.00 USD | 4,810,000.00 USD | 195,300.00 USD | 37,890.00 USD | 123,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 9,760,000.00 USD | 9,760,000.00 USD | 52,570.00 USD | 45,710.00 USD | 67,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9270` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 99,610.00 USD | 64,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 10,100,000.00 USD | 10,100,000.00 USD | 209,950.00 USD | 40,600.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9290` | 5,120,000.00 USD | 5,120,000.00 USD | 38,710.00 USD | 21,240.00 USD | 88,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 10,160,000.00 USD | 10,160,000.00 USD | 4,480.00 USD | 53,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9310` | 5,330,000.00 USD | 5,330,000.00 USD | 104,570.00 USD | 67,630.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 10,550,000.00 USD | 10,550,000.00 USD | 177,720.00 USD | 48,210.00 USD | 166,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9330` | 5,440,000.00 USD | 5,440,000.00 USD | 32,530.00 USD | 39,200.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 76,570.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 5,460,000.00 USD | 5,460,000.00 USD | 1,360.00 USD | 13,120.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 10,810,000.00 USD | 10,810,000.00 USD | 53,950.00 USD | 55,880.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 6,000,000.00 USD | 6,000,000.00 USD | 198,110.00 USD | 85,110.00 USD | 261,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 11,100,000.00 USD | 11,100,000.00 USD | 251,760.00 USD | 1,370.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 6,400,000.00 USD | 6,400,000.00 USD | 171,940.00 USD | 72,880.00 USD | 153,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 11,490,000.00 USD | 11,490,000.00 USD | 86,850.00 USD | 36,340.00 USD | 263,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 6,510,000.00 USD | 6,510,000.00 USD | 52,890.00 USD | 4,990.00 USD | 55,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 11,610,000.00 USD | 11,610,000.00 USD | 123,000.00 USD | 2,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 6,530,000.00 USD | 6,530,000.00 USD | 702.40 USD | 3,090.00 USD | 17,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 66,560.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9450` | 6,850,000.00 USD | 6,850,000.00 USD | 6,770.00 USD | 76,490.00 USD | 234,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 12,050,000.00 USD | 12,050,000.00 USD | 3,360.00 USD | 244,270.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 7,040,000.00 USD | 7,040,000.00 USD | 92,510.00 USD | 52,870.00 USD | 44,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 7,230,000.00 USD | 7,230,000.00 USD | 71,990.00 USD | 62,590.00 USD | 58,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 7,510,000.00 USD | 7,510,000.00 USD | 53,450.00 USD | 49,760.00 USD | 175,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 13,320,000.00 USD | 13,320,000.00 USD | 2,840.00 USD | 88,970.00 USD | 736,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 7,700,000.00 USD | 7,700,000.00 USD | 32,500.00 USD | 26,060.00 USD | 129,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 7,870,000.00 USD | 7,870,000.00 USD | 50,010.00 USD | 82,110.00 USD | 35,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 13,460,000.00 USD | 13,460,000.00 USD | 74,980.00 USD | 2,400.00 USD | 60,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 7,880,000.00 USD | 7,880,000.00 USD | 8,380.00 USD | 2,420.00 USD | 159.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 13,930,000.00 USD | 13,930,000.00 USD | 463,830.00 USD | 3,460.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 7,970,000.00 USD | 7,970,000.00 USD | 33,930.00 USD | 53,830.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 14,490,000.00 USD | 14,490,000.00 USD | 562,050.00 USD | 1,040.00 USD | 289.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 8,570,000.00 USD | 8,570,000.00 USD | 207,270.00 USD | 108,280.00 USD | 290,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 15,850,000.00 USD | 15,850,000.00 USD | 698,570.00 USD | 190,470.00 USD | 476,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 9,110,000.00 USD | 9,110,000.00 USD | 322,010.00 USD | 84,410.00 USD | 129,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 17,350,000.00 USD | 17,350,000.00 USD | 579,300.00 USD | 301,610.00 USD | 616,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 9,470,000.00 USD | 9,470,000.00 USD | 147,390.00 USD | 134,010.00 USD | 82,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 18,930,000.00 USD | 18,930,000.00 USD | 857,470.00 USD | 312,610.00 USD | 412,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 10,090,000.00 USD | 10,090,000.00 USD | 264,730.00 USD | 114,200.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 21,080,000.00 USD | 21,080,000.00 USD | 889,580.00 USD | 555,340.00 USD | 705,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 10,660,000.00 USD | 10,660,000.00 USD | 235,940.00 USD | 95,400.00 USD | 239,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 22,530,000.00 USD | 22,530,000.00 USD | 596,350.00 USD | 356,560.00 USD | 488,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 11,020,000.00 USD | 11,020,000.00 USD | 170,370.00 USD | 69,530.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 23,620,000.00 USD | 23,620,000.00 USD | 645,500.00 USD | 319,140.00 USD | 126,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 11,230,000.00 USD | 11,230,000.00 USD | 80,510.00 USD | 64,370.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 24,410,000.00 USD | 24,410,000.00 USD | 456,990.00 USD | 160,420.00 USD | 177,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 11,440,000.00 USD | 11,440,000.00 USD | 58,820.00 USD | 45,650.00 USD | 103,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 25,130,000.00 USD | 25,130,000.00 USD | 203,760.00 USD | 293,590.00 USD | 222,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 11,510,000.00 USD | 11,510,000.00 USD | 15,370.00 USD | 8,230.00 USD | 42,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 26,170,000.00 USD | 26,170,000.00 USD | 329,170.00 USD | 211,000.00 USD | 500,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9775` | 100.88 USD | 24,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9790` | 11,670,000.00 USD | 11,670,000.00 USD | 19,400.00 USD | 33,280.00 USD | 105,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 26,910,000.00 USD | 26,910,000.00 USD | 411,780.00 USD | 99,560.00 USD | 222,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 25,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 11,910,000.00 USD | 11,910,000.00 USD | 100,630.00 USD | 45,360.00 USD | 103,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 27,420,000.00 USD | 27,420,000.00 USD | 264,890.00 USD | 83,040.00 USD | 169,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 12,060,000.00 USD | 12,060,000.00 USD | 91,650.00 USD | 38,020.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 28,000,000.00 USD | 28,000,000.00 USD | 262,900.00 USD | 116,030.00 USD | 199,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 12,140,000.00 USD | 12,140,000.00 USD | 22,370.00 USD | 48,410.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 28,410,000.00 USD | 28,410,000.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 25,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9870` | 12,330,000.00 USD | 12,330,000.00 USD | 56,760.00 USD | 31,400.00 USD | 97,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 28,920,000.00 USD | 28,920,000.00 USD | 248,980.00 USD | 203,100.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 29,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9890` | 12,490,000.00 USD | 12,490,000.00 USD | 100,670.00 USD | 32,930.00 USD | 33,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 29,210,000.00 USD | 29,210,000.00 USD | 194,850.00 USD | 78,280.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 1,570.00 USD | 31,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9910` | 12,660,000.00 USD | 12,660,000.00 USD | 80,380.00 USD | 30,860.00 USD | 50,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 29,580,000.00 USD | 29,580,000.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 12,720,000.00 USD | 12,720,000.00 USD | 33,580.00 USD | 16,590.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 29,950,000.00 USD | 29,950,000.00 USD | 228,340.00 USD | 63,950.00 USD | 74,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 31,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9950` | 30,270,000.00 USD | 30,270,000.00 USD | 48,120.00 USD | 138,500.00 USD | 130,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 30,920,000.00 USD | 30,920,000.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 31,200,000.00 USD | 31,200,000.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,640,000.00 USD | 31,640,000.00 USD | 202,970.00 USD | 57,170.00 USD | 185,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 31,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,140,000.00 USD | 32,140,000.00 USD | 226,340.00 USD | 61,540.00 USD | 208,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,300,000.00 USD | 32,300,000.00 USD | 51,930.00 USD | 39,560.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 32,780,000.00 USD | 32,780,000.00 USD | 256,020.00 USD | 15,900.00 USD | 212,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 33,380,000.00 USD | 33,380,000.00 USD | 247,480.00 USD | 105,290.00 USD | 247,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,180,000.00 USD | 34,180,000.00 USD | 398,890.00 USD | 134,240.00 USD | 259,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,890,000.00 USD | 34,890,000.00 USD | 188,370.00 USD | 177,300.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 35,240,000.00 USD | 35,240,000.00 USD | 168,660.00 USD | 59,720.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 31,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 36,000,000.00 USD | 36,000,000.00 USD | 300,680.00 USD | 97,830.00 USD | 360,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 2,850.00 USD | 34,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 36,760,000.00 USD | 36,760,000.00 USD | 291,360.00 USD | 74,810.00 USD | 396,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 37,190,000.00 USD | 37,190,000.00 USD | 153,580.00 USD | 41,370.00 USD | 235,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 37,500,000.00 USD | 37,500,000.00 USD | 151,650.00 USD | 60,000.00 USD | 103,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 37,730,000.00 USD | 37,730,000.00 USD | 75,770.00 USD | 54,210.00 USD | 94,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 37,980,000.00 USD | 37,980,000.00 USD | 104,260.00 USD | 35,230.00 USD | 110,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 38,190,000.00 USD | 38,190,000.00 USD | 85,920.00 USD | 56,310.00 USD | 67,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 38,540,000.00 USD | 38,540,000.00 USD | 168,010.00 USD | 58,600.00 USD | 127,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 38,870,000.00 USD | 38,870,000.00 USD | 57,570.00 USD | 103,690.00 USD | 163,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 39,010,000.00 USD | 39,010,000.00 USD | 64,880.00 USD | 13,040.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,390,000.00 USD | 39,390,000.00 USD | 156,670.00 USD | 38,980.00 USD | 181,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,650,000.00 USD | 39,650,000.00 USD | 110,420.00 USD | 18,150.00 USD | 139,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 155.92 USD | 34,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 1,840.00 USD | 36,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,880,000.00 USD | 39,880,000.00 USD | 102,550.00 USD | 52,580.00 USD | 72,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,970,000.00 USD | 39,970,000.00 USD | 18,340.00 USD | 48,310.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 40,060,000.00 USD | 40,060,000.00 USD | 65,240.00 USD | 17,210.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,160,000.00 USD | 40,160,000.00 USD | 76,550.00 USD | 30,790.00 USD | 294.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,240,000.00 USD | 40,240,000.00 USD | 35,930.00 USD | 20,630.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 37,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,260,000.00 USD | 40,260,000.00 USD | 22,610.00 USD | 0.00 USD | 538.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 39,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,340,000.00 USD | 40,340,000.00 USD | 8,370.00 USD | 46,830.00 USD | 28,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,400,000.00 USD | 40,400,000.00 USD | 1,650.00 USD | 9,420.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,430,000.00 USD | 40,430,000.00 USD | 5,290.00 USD | 2,060.00 USD | 21,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,430,000.00 USD | 40,430,000.00 USD | 0.00 USD | 638.17 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,480,000.00 USD | 40,480,000.00 USD | 16,370.00 USD | 3,040.00 USD | 33,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,490,000.00 USD | 40,490,000.00 USD | 9,950.00 USD | 0.00 USD | 609.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,500,000.00 USD | 40,500,000.00 USD | 5,370.00 USD | 1,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 40,500,000.00 USD | 40,500,000.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 40,530,000.00 USD | 40,530,000.00 USD | 2,410.00 USD | 12,740.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 43,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 48,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 49,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 49,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 1,310.00 USD | 50,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 8,940.00 USD | 59,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 83,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 83,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 477.74 USD | 84,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 30,330.00 USD | 114,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 253.69 USD | 114,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 4,830.00 USD | 119,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 123,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 382.70 USD | 124,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 124,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 3,930.00 USD | 128,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 1,230.00 USD | 129,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 132,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 134,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 174,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 20,570.00 USD | 195,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 195,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 195,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,080.00 USD | 196,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 197,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 229,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 16,440.00 USD | 245,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 267,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 274,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.36` | 653.49 USD | 275,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 633,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 637,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 638,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 638,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.46` | 123.41 USD | 638,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 16,690.00 USD | 655,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 659,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 1,510.00 USD | 660,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 9,940.00 USD | 670,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 671,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 182.27 USD | 671,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 671,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 3,350.00 USD | 674,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 123.81 USD | 674,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,130.00 USD | 676,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 169.11 USD | 676,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 697,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 3,940.00 USD | 701,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,020.00 USD | 740,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 3,620.00 USD | 744,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 291,420.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 165.81 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1845` | 4,720,000.00 USD | 0.00 USD | 1,090.00 USD | `-78.44%` | `5,921.50` |
| `Live` | `Long` | `0.1905` | 4,720,000.00 USD | 0.00 USD | 291.48 USD | `-77.74%` | `1,530.10` |
| `Live` | `Long` | `0.1955` | 4,720,000.00 USD | 0.00 USD | 1,820.00 USD | `-77.15%` | `9,320.00` |
| `Live` | `Long` | `0.1985` | 4,720,000.00 USD | 0.00 USD | 1,160.00 USD | `-76.80%` | `5,865.20` |
| `Live` | `Long` | `0.1995` | 4,720,000.00 USD | 0.00 USD | 256.00 USD | `-76.69%` | `1,283.20` |
| `Live` | `Long` | `0.2025` | 4,710,000.00 USD | 0.00 USD | 5,550.00 USD | `-76.34%` | `27,392.40` |
| `Live` | `Long` | `0.2065` | 4,710,000.00 USD | 0.00 USD | 1,030.00 USD | `-75.87%` | `4,984.90` |
| `Live` | `Long` | `0.2135` | 4,710,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.05%` | `18,919.90` |
| `Live` | `Long` | `0.2205` | 4,700,000.00 USD | 0.00 USD | 303.72 USD | `-74.23%` | `1,377.40` |
| `Live` | `Long` | `0.2355` | 4,700,000.00 USD | 0.00 USD | 789.66 USD | `-72.48%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,700,000.00 USD | 0.00 USD | 156.36 USD | `-72.13%` | `655.60` |
| `Live` | `Long` | `0.2405` | 4,700,000.00 USD | 0.00 USD | 1,740.00 USD | `-71.90%` | `7,229.50` |
| `Live` | `Long` | `0.2445` | 4,700,000.00 USD | 0.00 USD | 745.68 USD | `-71.43%` | `3,049.80` |
| `Live` | `Long` | `0.2485` | 4,700,000.00 USD | 0.00 USD | 4,770.00 USD | `-70.96%` | `19,202.90` |
| `Live` | `Long` | `0.2525` | 4,700,000.00 USD | 0.00 USD | 2,250.00 USD | `-70.49%` | `8,897.00` |
| `Live` | `Long` | `0.2555` | 4,690,000.00 USD | 0.00 USD | 1,230.00 USD | `-70.14%` | `4,822.00` |
| `Live` | `Long` | `0.2685` | 4,690,000.00 USD | 0.00 USD | 106.16 USD | `-68.62%` | `395.40` |
| `Live` | `Long` | `0.2735` | 4,690,000.00 USD | 0.00 USD | 248.34 USD | `-68.04%` | `908.00` |
| `Live` | `Long` | `0.2745` | 4,690,000.00 USD | 0.00 USD | 314.11 USD | `-67.92%` | `1,144.30` |
| `Live` | `Long` | `0.2865` | 4,690,000.00 USD | 0.00 USD | 286.50 USD | `-66.52%` | `1,000.00` |
| `Live` | `Long` | `0.2885` | 4,690,000.00 USD | 0.00 USD | 29,070.00 USD | `-66.29%` | `100,768.40` |
| `Live` | `Long` | `0.2935` | 4,660,000.00 USD | 0.00 USD | 100.20 USD | `-65.70%` | `341.40` |
| `Live` | `Long` | `0.2975` | 4,660,000.00 USD | 0.00 USD | 4,330.00 USD | `-65.24%` | `14,561.30` |
| `Live` | `Long` | `0.3025` | 4,660,000.00 USD | 0.00 USD | 130.04 USD | `-64.65%` | `429.90` |
| `Live` | `Long` | `0.3055` | 4,660,000.00 USD | 0.00 USD | 3,100.00 USD | `-64.30%` | `10,152.10` |
| `Live` | `Long` | `0.3095` | 4,650,000.00 USD | 0.00 USD | 200.99 USD | `-63.83%` | `649.40` |
| `Live` | `Long` | `0.3105` | 4,650,000.00 USD | 0.00 USD | 621.00 USD | `-63.72%` | `2,000.00` |
| `Live` | `Long` | `0.3115` | 4,650,000.00 USD | 0.00 USD | 270.38 USD | `-63.60%` | `868.00` |
| `Live` | `Long` | `0.3135` | 4,650,000.00 USD | 0.00 USD | 1,230.00 USD | `-63.37%` | `3,934.90` |
| `Live` | `Long` | `0.3325` | 4,650,000.00 USD | 0.00 USD | 110.02 USD | `-61.15%` | `330.90` |
| `Live` | `Long` | `0.3455` | 4,650,000.00 USD | 0.00 USD | 1,130.00 USD | `-59.63%` | `3,277.00` |
| `Live` | `Long` | `0.3465` | 4,650,000.00 USD | 0.00 USD | 31,070.00 USD | `-59.51%` | `89,672.80` |
| `Live` | `Long` | `0.3505` | 4,620,000.00 USD | 0.00 USD | 1,020.00 USD | `-59.04%` | `2,908.00` |
| `Live` | `Long` | `0.3565` | 4,620,000.00 USD | 0.00 USD | 245.45 USD | `-58.34%` | `688.50` |
| `Live` | `Long` | `0.3585` | 4,620,000.00 USD | 0.00 USD | 595.72 USD | `-58.11%` | `1,661.70` |
| `Live` | `Long` | `0.3625` | 4,620,000.00 USD | 0.00 USD | 4,020.00 USD | `-57.64%` | `11,077.80` |
| `Live` | `Long` | `0.3665` | 4,610,000.00 USD | 0.00 USD | 274.88 USD | `-57.17%` | `750.00` |
| `Live` | `Long` | `0.3715` | 4,610,000.00 USD | 0.00 USD | 2,500.00 USD | `-56.59%` | `6,725.00` |
| `Live` | `Long` | `0.3755` | 4,610,000.00 USD | 0.00 USD | 408.24 USD | `-56.12%` | `1,087.20` |
| `Live` | `Long` | `0.3765` | 4,610,000.00 USD | 0.00 USD | 112.95 USD | `-56.00%` | `300.00` |
| `Live` | `Long` | `0.3775` | 4,610,000.00 USD | 0.00 USD | 154.55 USD | `-55.89%` | `409.40` |
| `Live` | `Long` | `0.3795` | 4,610,000.00 USD | 0.00 USD | 278.02 USD | `-55.65%` | `732.60` |
| `Live` | `Long` | `0.3835` | 4,610,000.00 USD | 0.00 USD | 6,520.00 USD | `-55.19%` | `17,000.00` |
| `Live` | `Long` | `0.3845` | 4,600,000.00 USD | 0.00 USD | 1,750.00 USD | `-55.07%` | `4,562.20` |
| `Live` | `Long` | `0.3895` | 4,600,000.00 USD | 0.00 USD | 2,980.00 USD | `-54.48%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 4,600,000.00 USD | 0.00 USD | 5,030.00 USD | `-54.13%` | `12,808.60` |
| `Live` | `Long` | `0.3935` | 4,590,000.00 USD | 0.00 USD | 243.26 USD | `-54.02%` | `618.20` |
| `Live` | `Long` | `0.3945` | 4,590,000.00 USD | 0.00 USD | 754.48 USD | `-53.90%` | `1,912.50` |
| `Live` | `Long` | `0.3955` | 4,590,000.00 USD | 0.00 USD | 276.85 USD | `-53.78%` | `700.00` |
| `Live` | `Long` | `0.3975` | 4,590,000.00 USD | 0.00 USD | 130.98 USD | `-53.55%` | `329.50` |
| `Live` | `Long` | `0.4035` | 4,590,000.00 USD | 0.00 USD | 935.03 USD | `-52.85%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,590,000.00 USD | 0.00 USD | 5,520.00 USD | `-52.73%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,590,000.00 USD | 0.00 USD | 3,360.00 USD | `-52.50%` | `8,275.50` |
| `Live` | `Long` | `0.4115` | 4,580,000.00 USD | 0.00 USD | 31,980.00 USD | `-51.91%` | `77,706.40` |
| `Live` | `Long` | `0.4135` | 4,550,000.00 USD | 0.00 USD | 5,500.00 USD | `-51.68%` | `13,291.10` |
| `Live` | `Long` | `0.4165` | 4,550,000.00 USD | 0.00 USD | 29,160.00 USD | `-51.33%` | `70,000.00` |
| `Live` | `Long` | `0.4185` | 4,520,000.00 USD | 0.00 USD | 1,570.00 USD | `-51.10%` | `3,748.80` |
| `Live` | `Long` | `0.4235` | 4,510,000.00 USD | 0.00 USD | 467.50 USD | `-50.51%` | `1,103.90` |
| `Live` | `Long` | `0.4355` | 4,510,000.00 USD | 0.00 USD | 871.17 USD | `-49.11%` | `2,000.40` |
| `Live` | `Long` | `0.4385` | 4,510,000.00 USD | 0.00 USD | 122.91 USD | `-48.76%` | `280.30` |
| `Live` | `Long` | `0.4415` | 4,510,000.00 USD | 0.00 USD | 43,980.00 USD | `-48.41%` | `99,611.70` |
| `Live` | `Long` | `0.4435` | 4,470,000.00 USD | 0.00 USD | 219.00 USD | `-48.17%` | `493.80` |
| `Live` | `Long` | `0.4455` | 4,470,000.00 USD | 0.00 USD | 692.53 USD | `-47.94%` | `1,554.50` |
| `Live` | `Long` | `0.4465` | 4,470,000.00 USD | 0.00 USD | 19,600.00 USD | `-47.82%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,450,000.00 USD | 0.00 USD | 105.25 USD | `-47.71%` | `235.20` |
| `Live` | `Long` | `0.4495` | 4,450,000.00 USD | 0.00 USD | 449.50 USD | `-47.47%` | `1,000.00` |
| `Live` | `Long` | `0.4535` | 4,450,000.00 USD | 0.00 USD | 1,020.00 USD | `-47.01%` | `2,246.80` |
| `Live` | `Long` | `0.4545` | 4,450,000.00 USD | 0.00 USD | 4,540.00 USD | `-46.89%` | `10,000.00` |
| `Live` | `Long` | `0.4595` | 4,440,000.00 USD | 0.00 USD | 3,330.00 USD | `-46.31%` | `7,245.50` |
| `Live` | `Long` | `0.4605` | 4,440,000.00 USD | 0.00 USD | 322.35 USD | `-46.19%` | `700.00` |
| `Live` | `Long` | `0.4715` | 4,440,000.00 USD | 0.00 USD | 1,720.00 USD | `-44.90%` | `3,650.40` |
| `Live` | `Long` | `0.4775` | 4,440,000.00 USD | 0.00 USD | 464.46 USD | `-44.20%` | `972.70` |
| `Live` | `Long` | `0.4785` | 4,440,000.00 USD | 0.00 USD | 110.10 USD | `-44.08%` | `230.10` |
| `Live` | `Long` | `0.4795` | 4,440,000.00 USD | 0.00 USD | 844.88 USD | `-43.97%` | `1,762.00` |
| `Live` | `Long` | `0.4805` | 4,440,000.00 USD | 0.00 USD | 14,250.00 USD | `-43.85%` | `29,662.60` |
| `Live` | `Long` | `0.4825` | 4,420,000.00 USD | 0.00 USD | 166.70 USD | `-43.62%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,420,000.00 USD | 0.00 USD | 4,040.00 USD | `-43.50%` | `8,345.80` |
| `Live` | `Long` | `0.4845` | 4,420,000.00 USD | 0.00 USD | 1,380.00 USD | `-43.38%` | `2,855.70` |
| `Live` | `Long` | `0.4865` | 4,420,000.00 USD | 0.00 USD | 4,050.00 USD | `-43.15%` | `8,325.90` |
| `Live` | `Long` | `0.4895` | 4,410,000.00 USD | 0.00 USD | 105.34 USD | `-42.80%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,410,000.00 USD | 0.00 USD | 2,380.00 USD | `-42.57%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 4,410,000.00 USD | 0.00 USD | 106.32 USD | `-42.22%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,410,000.00 USD | 0.00 USD | 211.88 USD | `-42.10%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,410,000.00 USD | 0.00 USD | 216.75 USD | `-41.75%` | `434.80` |
| `Live` | `Long` | `0.5015` | 4,410,000.00 USD | 0.00 USD | 70,630.00 USD | `-41.40%` | `140,845.40` |
| `Live` | `Long` | `0.5025` | 4,340,000.00 USD | 0.00 USD | 8,390.00 USD | `-41.28%` | `16,696.10` |
| `Live` | `Long` | `0.5055` | 4,330,000.00 USD | 0.00 USD | 211.25 USD | `-40.93%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,330,000.00 USD | 0.00 USD | 5,680.00 USD | `-40.58%` | `11,163.80` |
| `Live` | `Long` | `0.5095` | 4,320,000.00 USD | 0.00 USD | 195.75 USD | `-40.46%` | `384.20` |
| `Live` | `Long` | `0.5105` | 4,320,000.00 USD | 0.00 USD | 5,760.00 USD | `-40.35%` | `11,290.30` |
| `Live` | `Long` | `0.5155` | 4,320,000.00 USD | 0.00 USD | 1,680.00 USD | `-39.76%` | `3,257.30` |
| `Live` | `Long` | `0.5165` | 4,320,000.00 USD | 0.00 USD | 619.80 USD | `-39.64%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,320,000.00 USD | 0.00 USD | 213.68 USD | `-39.53%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,320,000.00 USD | 0.00 USD | 121.74 USD | `-39.41%` | `234.80` |
| `Live` | `Long` | `0.5225` | 4,320,000.00 USD | 0.00 USD | 577.88 USD | `-38.94%` | `1,106.00` |
| `Live` | `Long` | `0.5235` | 4,310,000.00 USD | 0.00 USD | 7,650.00 USD | `-38.83%` | `14,603.90` |
| `Live` | `Long` | `0.5275` | 4,310,000.00 USD | 0.00 USD | 1,220.00 USD | `-38.36%` | `2,320.60` |
| `Live` | `Long` | `0.5295` | 4,310,000.00 USD | 0.00 USD | 264.06 USD | `-38.13%` | `498.70` |
| `Live` | `Long` | `0.5305` | 4,310,000.00 USD | 0.00 USD | 123,610.00 USD | `-38.01%` | `233,000.00` |
| `Live` | `Long` | `0.5325` | 4,180,000.00 USD | 0.00 USD | 2,680.00 USD | `-37.77%` | `5,038.10` |
| `Live` | `Long` | `0.5355` | 4,180,000.00 USD | 0.00 USD | 113.47 USD | `-37.42%` | `211.90` |
| `Live` | `Long` | `0.5365` | 4,180,000.00 USD | 0.00 USD | 1,630.00 USD | `-37.31%` | `3,043.40` |
| `Live` | `Long` | `0.5385` | 4,180,000.00 USD | 0.00 USD | 127.57 USD | `-37.07%` | `236.90` |
| `Live` | `Long` | `0.5405` | 4,180,000.00 USD | 0.00 USD | 7,090.00 USD | `-36.84%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,170,000.00 USD | 0.00 USD | 11,120.00 USD | `-36.61%` | `20,496.10` |
| `Live` | `Long` | `0.5445` | 4,160,000.00 USD | 0.00 USD | 230.32 USD | `-36.37%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,160,000.00 USD | 0.00 USD | 272.87 USD | `-36.14%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,160,000.00 USD | 0.00 USD | 1,240.00 USD | `-36.02%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,160,000.00 USD | 0.00 USD | 162,050.00 USD | `-35.79%` | `294,906.00` |
| `Live` | `Long` | `0.5505` | 4,000,000.00 USD | 0.00 USD | 248.06 USD | `-35.67%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,000,000.00 USD | 0.00 USD | 160.93 USD | `-35.55%` | `291.80` |
| `Live` | `Long` | `0.5525` | 3,990,000.00 USD | 0.00 USD | 701.51 USD | `-35.44%` | `1,269.70` |
| `Live` | `Long` | `0.5535` | 3,990,000.00 USD | 0.00 USD | 271.88 USD | `-35.32%` | `491.20` |
| `Live` | `Long` | `0.5545` | 3,990,000.00 USD | 0.00 USD | 531.60 USD | `-35.20%` | `958.70` |
| `Live` | `Long` | `0.5555` | 3,990,000.00 USD | 0.00 USD | 8,240.00 USD | `-35.09%` | `14,833.70` |
| `Live` | `Long` | `0.5575` | 3,990,000.00 USD | 0.00 USD | 5,300.00 USD | `-34.85%` | `9,500.00` |
| `Live` | `Long` | `0.5585` | 3,980,000.00 USD | 0.00 USD | 141.97 USD | `-34.74%` | `254.20` |
| `Live` | `Long` | `0.5595` | 3,980,000.00 USD | 0.00 USD | 304.93 USD | `-34.62%` | `545.00` |
| `Live` | `Long` | `0.5605` | 3,980,000.00 USD | 0.00 USD | 441.84 USD | `-34.50%` | `788.30` |
| `Live` | `Long` | `0.5625` | 3,980,000.00 USD | 0.00 USD | 330.53 USD | `-34.27%` | `587.60` |
| `Live` | `Long` | `0.5635` | 3,980,000.00 USD | 0.00 USD | 534.03 USD | `-34.15%` | `947.70` |
| `Live` | `Long` | `0.5645` | 3,980,000.00 USD | 0.00 USD | 249.57 USD | `-34.04%` | `442.10` |
| `Live` | `Long` | `0.5655` | 3,980,000.00 USD | 0.00 USD | 8,190.00 USD | `-33.92%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 3,970,000.00 USD | 0.00 USD | 6,720.00 USD | `-33.80%` | `11,868.90` |
| `Live` | `Long` | `0.5675` | 3,960,000.00 USD | 0.00 USD | 1,560.00 USD | `-33.68%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 3,960,000.00 USD | 0.00 USD | 973.22 USD | `-33.45%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 3,960,000.00 USD | 0.00 USD | 139.23 USD | `-33.10%` | `243.20` |
| `Live` | `Long` | `0.5735` | 3,960,000.00 USD | 0.00 USD | 182.72 USD | `-32.98%` | `318.60` |
| `Live` | `Long` | `0.5745` | 3,960,000.00 USD | 0.00 USD | 144.03 USD | `-32.87%` | `250.70` |
| `Live` | `Long` | `0.5755` | 3,960,000.00 USD | 0.00 USD | 217.37 USD | `-32.75%` | `377.70` |
| `Live` | `Long` | `0.5765` | 3,960,000.00 USD | 0.00 USD | 1,150.00 USD | `-32.63%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 3,960,000.00 USD | 0.00 USD | 497.75 USD | `-32.52%` | `861.90` |
| `Live` | `Long` | `0.5785` | 3,960,000.00 USD | 0.00 USD | 4,660.00 USD | `-32.40%` | `8,054.90` |
| `Live` | `Long` | `0.5795` | 3,950,000.00 USD | 0.00 USD | 212.85 USD | `-32.28%` | `367.30` |
| `Live` | `Long` | `0.5805` | 3,950,000.00 USD | 0.00 USD | 1,410.00 USD | `-32.17%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 3,950,000.00 USD | 0.00 USD | 6,470.00 USD | `-31.93%` | `11,099.00` |
| `Live` | `Long` | `0.5845` | 3,950,000.00 USD | 0.00 USD | 6,980.00 USD | `-31.70%` | `11,935.50` |
| `Live` | `Long` | `0.5855` | 3,940,000.00 USD | 0.00 USD | 2,640.00 USD | `-31.58%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 3,940,000.00 USD | 0.00 USD | 466.85 USD | `-31.46%` | `796.00` |
| `Live` | `Long` | `0.5885` | 3,940,000.00 USD | 0.00 USD | 311.14 USD | `-31.23%` | `528.70` |
| `Live` | `Long` | `0.5895` | 3,930,000.00 USD | 0.00 USD | 357.12 USD | `-31.11%` | `605.80` |
| `Live` | `Long` | `0.5905` | 3,930,000.00 USD | 0.00 USD | 1,070.00 USD | `-31.00%` | `1,812.90` |
| `Live` | `Long` | `0.5925` | 3,930,000.00 USD | 0.00 USD | 994.16 USD | `-30.76%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 3,930,000.00 USD | 0.00 USD | 132.41 USD | `-30.65%` | `223.10` |
| `Live` | `Long` | `0.5945` | 3,930,000.00 USD | 0.00 USD | 8,220.00 USD | `-30.53%` | `13,833.50` |
| `Live` | `Long` | `0.5955` | 3,920,000.00 USD | 0.00 USD | 355.57 USD | `-30.41%` | `597.10` |
| `Live` | `Long` | `0.5965` | 3,920,000.00 USD | 0.00 USD | 608.61 USD | `-30.30%` | `1,020.30` |
| `Live` | `Long` | `0.5975` | 3,920,000.00 USD | 0.00 USD | 4,360.00 USD | `-30.18%` | `7,291.60` |
| `Live` | `Long` | `0.5985` | 3,920,000.00 USD | 0.00 USD | 419.73 USD | `-30.06%` | `701.30` |
| `Live` | `Long` | `0.5995` | 3,920,000.00 USD | 0.00 USD | 4,310.00 USD | `-29.95%` | `7,195.00` |
| `Live` | `Long` | `0.6005` | 3,910,000.00 USD | 0.00 USD | 351.11 USD | `-29.83%` | `584.70` |
| `Live` | `Long` | `0.6015` | 3,910,000.00 USD | 0.00 USD | 323.79 USD | `-29.71%` | `538.30` |
| `Live` | `Long` | `0.6025` | 3,910,000.00 USD | 0.00 USD | 432.35 USD | `-29.59%` | `717.60` |
| `Live` | `Long` | `0.6035` | 3,910,000.00 USD | 0.00 USD | 1,220.00 USD | `-29.48%` | `2,023.70` |
| `Live` | `Long` | `0.6075` | 3,910,000.00 USD | 0.00 USD | 851.05 USD | `-29.01%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 3,910,000.00 USD | 0.00 USD | 886.10 USD | `-28.89%` | `1,456.20` |
| `Live` | `Long` | `0.6115` | 3,910,000.00 USD | 0.00 USD | 13,930.00 USD | `-28.54%` | `22,777.40` |
| `Live` | `Long` | `0.6125` | 3,900,000.00 USD | 0.00 USD | 438.73 USD | `-28.43%` | `716.30` |
| `Live` | `Long` | `0.6135` | 3,900,000.00 USD | 0.00 USD | 112.33 USD | `-28.31%` | `183.10` |
| `Live` | `Long` | `0.6145` | 3,900,000.00 USD | 0.00 USD | 2,110.00 USD | `-28.19%` | `3,435.00` |
| `Live` | `Long` | `0.6155` | 3,890,000.00 USD | 0.00 USD | 935.13 USD | `-28.08%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 3,890,000.00 USD | 0.00 USD | 29,900.00 USD | `-27.96%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 3,860,000.00 USD | 0.00 USD | 4,980.00 USD | `-27.84%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 3,860,000.00 USD | 0.00 USD | 14,440.00 USD | `-27.73%` | `23,339.50` |
| `Live` | `Long` | `0.6195` | 3,840,000.00 USD | 0.00 USD | 1,050.00 USD | `-27.61%` | `1,700.60` |
| `Live` | `Long` | `0.6205` | 3,840,000.00 USD | 0.00 USD | 620.50 USD | `-27.49%` | `1,000.00` |
| `Live` | `Long` | `0.6215` | 3,840,000.00 USD | 0.00 USD | 444.75 USD | `-27.37%` | `715.60` |
| `Live` | `Long` | `0.6225` | 3,840,000.00 USD | 0.00 USD | 263.07 USD | `-27.26%` | `422.60` |
| `Live` | `Long` | `0.6245` | 3,840,000.00 USD | 0.00 USD | 356.65 USD | `-27.02%` | `571.10` |
| `Live` | `Long` | `0.6255` | 3,840,000.00 USD | 0.00 USD | 32,070.00 USD | `-26.91%` | `51,265.70` |
| `Live` | `Long` | `0.6285` | 3,810,000.00 USD | 0.00 USD | 256.55 USD | `-26.56%` | `408.20` |
| `Live` | `Long` | `0.6305` | 3,810,000.00 USD | 0.00 USD | 319.35 USD | `-26.32%` | `506.50` |
| `Live` | `Long` | `0.6345` | 3,810,000.00 USD | 0.00 USD | 843.00 USD | `-25.86%` | `1,328.60` |
| `Live` | `Long` | `0.6365` | 3,810,000.00 USD | 0.00 USD | 3,060.00 USD | `-25.62%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,800,000.00 USD | 0.00 USD | 1,100.00 USD | `-25.50%` | `1,726.70` |
| `Live` | `Long` | `0.6385` | 3,800,000.00 USD | 0.00 USD | 671.77 USD | `-25.39%` | `1,052.10` |
| `Live` | `Long` | `0.6405` | 3,800,000.00 USD | 0.00 USD | 33,040.00 USD | `-25.15%` | `51,581.80` |
| `Live` | `Long` | `0.6415` | 3,770,000.00 USD | 0.00 USD | 86,920.00 USD | `-25.04%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,680,000.00 USD | 0.00 USD | 1,260.00 USD | `-24.92%` | `1,956.60` |
| `Live` | `Long` | `0.6435` | 3,680,000.00 USD | 0.00 USD | 3,190.00 USD | `-24.80%` | `4,951.30` |
| `Live` | `Long` | `0.6445` | 3,680,000.00 USD | 0.00 USD | 65,790.00 USD | `-24.69%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,610,000.00 USD | 0.00 USD | 14,590.00 USD | `-24.57%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,600,000.00 USD | 0.00 USD | 146.76 USD | `-24.45%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,600,000.00 USD | 0.00 USD | 3,200.00 USD | `-24.34%` | `4,945.10` |
| `Live` | `Long` | `0.6485` | 3,590,000.00 USD | 0.00 USD | 668.34 USD | `-24.22%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,590,000.00 USD | 0.00 USD | 7,360.00 USD | `-24.10%` | `11,336.20` |
| `Live` | `Long` | `0.6505` | 3,590,000.00 USD | 0.00 USD | 106.75 USD | `-23.99%` | `164.10` |
| `Live` | `Long` | `0.6515` | 3,590,000.00 USD | 0.00 USD | 403,320.00 USD | `-23.87%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,180,000.00 USD | 0.00 USD | 4,590.00 USD | `-23.75%` | `7,039.40` |
| `Live` | `Long` | `0.6535` | 3,180,000.00 USD | 0.00 USD | 127,900.00 USD | `-23.64%` | `195,717.60` |
| `Live` | `Long` | `0.6545` | 3,050,000.00 USD | 0.00 USD | 6,700.00 USD | `-23.52%` | `10,231.40` |
| `Live` | `Long` | `0.6555` | 3,040,000.00 USD | 0.00 USD | 676.54 USD | `-23.40%` | `1,032.10` |
| `Live` | `Long` | `0.6565` | 3,040,000.00 USD | 0.00 USD | 10,020.00 USD | `-23.28%` | `15,264.20` |
| `Live` | `Long` | `0.6575` | 3,030,000.00 USD | 0.00 USD | 13,280.00 USD | `-23.17%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,020,000.00 USD | 0.00 USD | 2,970.00 USD | `-23.05%` | `4,508.30` |
| `Live` | `Long` | `0.6605` | 3,020,000.00 USD | 0.00 USD | 841.81 USD | `-22.82%` | `1,274.50` |
| `Live` | `Long` | `0.6615` | 3,020,000.00 USD | 0.00 USD | 4,370.00 USD | `-22.70%` | `6,607.90` |
| `Live` | `Long` | `0.6625` | 3,010,000.00 USD | 0.00 USD | 1,960.00 USD | `-22.58%` | `2,952.50` |
| `Live` | `Long` | `0.6645` | 3,010,000.00 USD | 0.00 USD | 448.54 USD | `-22.35%` | `675.00` |
| `Live` | `Long` | `0.6665` | 3,010,000.00 USD | 0.00 USD | 528.73 USD | `-22.12%` | `793.30` |
| `Live` | `Long` | `0.6675` | 3,010,000.00 USD | 0.00 USD | 3,050.00 USD | `-22.00%` | `4,574.20` |
| `Live` | `Long` | `0.6685` | 3,010,000.00 USD | 0.00 USD | 135.71 USD | `-21.88%` | `203.00` |
| `Live` | `Long` | `0.6695` | 3,010,000.00 USD | 0.00 USD | 337.36 USD | `-21.77%` | `503.90` |
| `Live` | `Long` | `0.6705` | 3,000,000.00 USD | 0.00 USD | 2,290.00 USD | `-21.65%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,000,000.00 USD | 0.00 USD | 2,240.00 USD | `-21.53%` | `3,341.20` |
| `Live` | `Long` | `0.6725` | 3,000,000.00 USD | 0.00 USD | 1,280.00 USD | `-21.41%` | `1,906.60` |
| `Live` | `Long` | `0.6735` | 3,000,000.00 USD | 0.00 USD | 633.09 USD | `-21.30%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,000,000.00 USD | 0.00 USD | 6,520.00 USD | `-21.18%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 2,990,000.00 USD | 0.00 USD | 1,190.00 USD | `-21.06%` | `1,765.20` |
| `Live` | `Long` | `0.6775` | 2,990,000.00 USD | 0.00 USD | 9,150.00 USD | `-20.83%` | `13,500.00` |
| `Live` | `Long` | `0.6785` | 2,980,000.00 USD | 0.00 USD | 122.94 USD | `-20.71%` | `181.20` |
| `Live` | `Long` | `0.6795` | 2,980,000.00 USD | 0.00 USD | 44,890.00 USD | `-20.60%` | `66,065.50` |
| `Live` | `Long` | `0.6805` | 2,940,000.00 USD | 0.00 USD | 28,920.00 USD | `-20.48%` | `42,502.80` |
| `Live` | `Long` | `0.6815` | 2,910,000.00 USD | 0.00 USD | 8,150.00 USD | `-20.36%` | `11,966.00` |
| `Live` | `Long` | `0.6825` | 2,900,000.00 USD | 0.00 USD | 15,920.00 USD | `-20.25%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 2,880,000.00 USD | 0.00 USD | 11,170.00 USD | `-20.13%` | `16,336.60` |
| `Live` | `Long` | `0.6845` | 2,870,000.00 USD | 0.00 USD | 348,240.00 USD | `-20.01%` | `508,750.20` |
| `Live` | `Long` | `0.6865` | 2,520,000.00 USD | 0.00 USD | 112.59 USD | `-19.78%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,520,000.00 USD | 0.00 USD | 22,010.00 USD | `-19.66%` | `32,008.20` |
| `Live` | `Long` | `0.6885` | 2,500,000.00 USD | 0.00 USD | 44,250.00 USD | `-19.55%` | `64,274.80` |
| `Live` | `Long` | `0.6895` | 2,460,000.00 USD | 0.00 USD | 2,110.00 USD | `-19.43%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,460,000.00 USD | 0.00 USD | 3,360.00 USD | `-19.31%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,450,000.00 USD | 0.00 USD | 10,590.00 USD | `-19.19%` | `15,317.60` |
| `Live` | `Long` | `0.6935` | 2,440,000.00 USD | 0.00 USD | 3,600.00 USD | `-18.96%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 2,440,000.00 USD | 0.00 USD | 7,670.00 USD | `-18.84%` | `11,040.00` |
| `Live` | `Long` | `0.6955` | 2,430,000.00 USD | 0.00 USD | 1,700.00 USD | `-18.73%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,430,000.00 USD | 0.00 USD | 273.03 USD | `-18.61%` | `392.00` |
| `Live` | `Long` | `0.6975` | 2,430,000.00 USD | 0.00 USD | 1,630.00 USD | `-18.49%` | `2,337.60` |
| `Live` | `Long` | `0.6985` | 2,430,000.00 USD | 0.00 USD | 1,670.00 USD | `-18.38%` | `2,396.30` |
| `Live` | `Long` | `0.7015` | 2,430,000.00 USD | 0.00 USD | 1,990.00 USD | `-18.03%` | `2,841.50` |
| `Live` | `Long` | `0.7045` | 2,420,000.00 USD | 0.00 USD | 10,190.00 USD | `-17.68%` | `14,469.20` |
| `Live` | `Long` | `0.7055` | 2,410,000.00 USD | 0.00 USD | 169.67 USD | `-17.56%` | `240.50` |
| `Live` | `Long` | `0.7065` | 2,410,000.00 USD | 0.00 USD | 912.73 USD | `-17.44%` | `1,291.90` |
| `Live` | `Long` | `0.7075` | 2,410,000.00 USD | 0.00 USD | 787.73 USD | `-17.32%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 2,410,000.00 USD | 0.00 USD | 2,020.00 USD | `-17.21%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,410,000.00 USD | 0.00 USD | 570.08 USD | `-17.09%` | `803.50` |
| `Live` | `Long` | `0.7105` | 2,410,000.00 USD | 0.00 USD | 25,230.00 USD | `-16.97%` | `35,512.10` |
| `Live` | `Long` | `0.7125` | 2,380,000.00 USD | 0.00 USD | 283.22 USD | `-16.74%` | `397.50` |
| `Live` | `Long` | `0.7135` | 2,380,000.00 USD | 0.00 USD | 927.55 USD | `-16.62%` | `1,300.00` |
| `Live` | `Long` | `0.7145` | 2,380,000.00 USD | 0.00 USD | 297.23 USD | `-16.51%` | `416.00` |
| `Live` | `Long` | `0.7155` | 2,380,000.00 USD | 0.00 USD | 12,340.00 USD | `-16.39%` | `17,244.80` |
| `Live` | `Long` | `0.7165` | 2,370,000.00 USD | 0.00 USD | 4,890.00 USD | `-16.27%` | `6,822.00` |
| `Live` | `Long` | `0.7185` | 2,360,000.00 USD | 0.00 USD | 126.96 USD | `-16.04%` | `176.70` |
| `Live` | `Long` | `0.7195` | 2,360,000.00 USD | 0.00 USD | 420.19 USD | `-15.92%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,360,000.00 USD | 0.00 USD | 8,450.00 USD | `-15.69%` | `11,706.20` |
| `Live` | `Long` | `0.7225` | 2,360,000.00 USD | 0.00 USD | 1,990.00 USD | `-15.57%` | `2,752.10` |
| `Live` | `Long` | `0.7235` | 2,350,000.00 USD | 0.00 USD | 7,510.00 USD | `-15.46%` | `10,375.60` |
| `Live` | `Long` | `0.7255` | 2,350,000.00 USD | 0.00 USD | 311.60 USD | `-15.22%` | `429.50` |
| `Live` | `Long` | `0.7265` | 2,350,000.00 USD | 0.00 USD | 3,410.00 USD | `-15.10%` | `4,687.00` |
| `Live` | `Long` | `0.7275` | 2,340,000.00 USD | 0.00 USD | 35,890.00 USD | `-14.99%` | `49,332.50` |
| `Live` | `Long` | `0.7285` | 2,310,000.00 USD | 0.00 USD | 432.58 USD | `-14.87%` | `593.80` |
| `Live` | `Long` | `0.7295` | 2,310,000.00 USD | 0.00 USD | 375.98 USD | `-14.75%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,310,000.00 USD | 0.00 USD | 119.88 USD | `-14.64%` | `164.10` |
| `Live` | `Long` | `0.7325` | 2,310,000.00 USD | 0.00 USD | 907.93 USD | `-14.40%` | `1,239.50` |
| `Live` | `Long` | `0.7335` | 2,300,000.00 USD | 0.00 USD | 8,360.00 USD | `-14.29%` | `11,403.60` |
| `Live` | `Long` | `0.7345` | 2,300,000.00 USD | 0.00 USD | 2,340.00 USD | `-14.17%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,290,000.00 USD | 0.00 USD | 51,920.00 USD | `-14.05%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 2,240,000.00 USD | 0.00 USD | 3,450.00 USD | `-13.94%` | `4,683.00` |
| `Live` | `Long` | `0.7375` | 2,240,000.00 USD | 0.00 USD | 203.11 USD | `-13.82%` | `275.40` |
| `Live` | `Long` | `0.7385` | 2,240,000.00 USD | 0.00 USD | 6,480.00 USD | `-13.70%` | `8,776.20` |
| `Live` | `Long` | `0.7395` | 2,230,000.00 USD | 0.00 USD | 3,380.00 USD | `-13.59%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,230,000.00 USD | 0.00 USD | 5,210.00 USD | `-13.47%` | `7,038.80` |
| `Live` | `Long` | `0.7415` | 2,220,000.00 USD | 0.00 USD | 382.61 USD | `-13.35%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,220,000.00 USD | 0.00 USD | 785,210.00 USD | `-13.24%` | `1,057,516.70` |
| `Live` | `Long` | `0.7435` | 1,440,000.00 USD | 0.00 USD | 421.12 USD | `-13.12%` | `566.40` |
| `Live` | `Long` | `0.7455` | 1,440,000.00 USD | 0.00 USD | 2,160.00 USD | `-12.88%` | `2,892.60` |
| `Live` | `Long` | `0.7465` | 1,440,000.00 USD | 0.00 USD | 359.96 USD | `-12.77%` | `482.20` |
| `Live` | `Long` | `0.7475` | 1,430,000.00 USD | 0.00 USD | 107,260.00 USD | `-12.65%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,330,000.00 USD | 0.00 USD | 599.60 USD | `-12.42%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,330,000.00 USD | 0.00 USD | 1,210.00 USD | `-12.18%` | `1,613.50` |
| `Live` | `Long` | `0.7535` | 1,330,000.00 USD | 0.00 USD | 264.86 USD | `-11.95%` | `351.50` |
| `Live` | `Long` | `0.7545` | 1,330,000.00 USD | 0.00 USD | 1,250.00 USD | `-11.83%` | `1,650.60` |
| `Live` | `Long` | `0.7555` | 1,320,000.00 USD | 0.00 USD | 1,750.00 USD | `-11.72%` | `2,315.50` |
| `Live` | `Long` | `0.7575` | 1,320,000.00 USD | 0.00 USD | 1,900.00 USD | `-11.48%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,320,000.00 USD | 0.00 USD | 40,520.00 USD | `-11.37%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,280,000.00 USD | 0.00 USD | 4,900.00 USD | `-11.25%` | `6,448.30` |
| `Live` | `Long` | `0.7615` | 1,280,000.00 USD | 0.00 USD | 351.43 USD | `-11.01%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,270,000.00 USD | 0.00 USD | 1,170.00 USD | `-10.90%` | `1,534.70` |
| `Live` | `Long` | `0.7635` | 1,270,000.00 USD | 0.00 USD | 5,110.00 USD | `-10.78%` | `6,696.30` |
| `Live` | `Long` | `0.7645` | 1,270,000.00 USD | 0.00 USD | 3,510.00 USD | `-10.66%` | `4,596.60` |
| `Live` | `Long` | `0.7655` | 1,260,000.00 USD | 0.00 USD | 4,430.00 USD | `-10.55%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,260,000.00 USD | 0.00 USD | 1,480.00 USD | `-10.43%` | `1,928.20` |
| `Live` | `Long` | `0.7675` | 1,260,000.00 USD | 0.00 USD | 25,580.00 USD | `-10.31%` | `33,323.60` |
| `Live` | `Long` | `0.7685` | 1,230,000.00 USD | 0.00 USD | 207.19 USD | `-10.20%` | `269.60` |
| `Live` | `Long` | `0.7695` | 1,230,000.00 USD | 0.00 USD | 150,510.00 USD | `-10.08%` | `195,593.50` |
| `Live` | `Long` | `0.7705` | 1,080,000.00 USD | 0.00 USD | 5,640.00 USD | `-9.96%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 1,080,000.00 USD | 0.00 USD | 19,250.00 USD | `-9.85%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 1,060,000.00 USD | 0.00 USD | 1,940.00 USD | `-9.73%` | `2,515.50` |
| `Live` | `Long` | `0.7735` | 1,060,000.00 USD | 0.00 USD | 5,230.00 USD | `-9.61%` | `6,756.40` |
| `Live` | `Long` | `0.7745` | 1,050,000.00 USD | 0.00 USD | 2,970.00 USD | `-9.50%` | `3,840.20` |
| `Live` | `Long` | `0.7755` | 1,050,000.00 USD | 0.00 USD | 13,940.00 USD | `-9.38%` | `17,976.80` |
| `Live` | `Long` | `0.7765` | 1,030,000.00 USD | 0.00 USD | 3,510.00 USD | `-9.26%` | `4,518.50` |
| `Live` | `Long` | `0.7775` | 1,030,000.00 USD | 0.00 USD | 8,980.00 USD | `-9.15%` | `11,545.90` |
| `Live` | `Long` | `0.7785` | 1,020,000.00 USD | 0.00 USD | 28,010.00 USD | `-9.03%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 993,200.00 USD | 0.00 USD | 338.69 USD | `-8.91%` | `434.50` |
| `Live` | `Long` | `0.7815` | 992,860.00 USD | 0.00 USD | 4,160.00 USD | `-8.68%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 988,700.00 USD | 0.00 USD | 21,600.00 USD | `-8.44%` | `27,572.80` |
| `Live` | `Long` | `0.7855` | 967,090.00 USD | 0.00 USD | 108.63 USD | `-8.21%` | `138.30` |
| `Live` | `Long` | `0.7865` | 966,980.00 USD | 0.00 USD | 3,470.00 USD | `-8.09%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 963,510.00 USD | 0.00 USD | 288.70 USD | `-7.98%` | `366.60` |
| `Live` | `Long` | `0.7905` | 963,220.00 USD | 0.00 USD | 3,670.00 USD | `-7.63%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 959,550.00 USD | 0.00 USD | 1,280.00 USD | `-7.51%` | `1,623.00` |
| `Live` | `Long` | `0.7925` | 958,270.00 USD | 0.00 USD | 7,330.00 USD | `-7.39%` | `9,255.10` |
| `Live` | `Long` | `0.7935` | 950,940.00 USD | 0.00 USD | 809.45 USD | `-7.28%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 950,130.00 USD | 0.00 USD | 894.61 USD | `-7.16%` | `1,126.00` |
| `Live` | `Long` | `0.7955` | 949,230.00 USD | 0.00 USD | 31,180.00 USD | `-7.04%` | `39,190.00` |
| `Live` | `Long` | `0.7965` | 918,060.00 USD | 0.00 USD | 342,330.00 USD | `-6.92%` | `429,789.40` |
| `Live` | `Long` | `0.7975` | 575,730.00 USD | 0.00 USD | 7,580.00 USD | `-6.81%` | `9,508.60` |
| `Live` | `Long` | `0.7985` | 568,150.00 USD | 0.00 USD | 39,870.00 USD | `-6.69%` | `49,928.60` |
| `Live` | `Long` | `0.7995` | 528,280.00 USD | 0.00 USD | 12,940.00 USD | `-6.57%` | `16,183.60` |
| `Live` | `Long` | `0.8005` | 515,340.00 USD | 0.00 USD | 906.49 USD | `-6.46%` | `1,132.40` |
| `Live` | `Long` | `0.8015` | 514,430.00 USD | 0.00 USD | 6,810.00 USD | `-6.34%` | `8,499.50` |
| `Live` | `Long` | `0.8025` | 507,620.00 USD | 0.00 USD | 6,050.00 USD | `-6.22%` | `7,539.00` |
| `Live` | `Long` | `0.8035` | 501,570.00 USD | 0.00 USD | 7,680.00 USD | `-6.11%` | `9,559.90` |
| `Live` | `Long` | `0.8045` | 493,890.00 USD | 0.00 USD | 16,830.00 USD | `-5.99%` | `20,921.30` |
| `Live` | `Long` | `0.8055` | 477,060.00 USD | 0.00 USD | 190.90 USD | `-5.87%` | `237.00` |
| `Live` | `Long` | `0.8065` | 476,870.00 USD | 0.00 USD | 6,910.00 USD | `-5.76%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 469,950.00 USD | 0.00 USD | 2,770.00 USD | `-5.64%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 467,190.00 USD | 0.00 USD | 22,170.00 USD | `-5.52%` | `27,427.20` |
| `Live` | `Long` | `0.8095` | 445,010.00 USD | 0.00 USD | 130,110.00 USD | `-5.41%` | `160,732.40` |
| `Live` | `Long` | `0.8105` | 314,900.00 USD | 0.00 USD | 2,250.00 USD | `-5.29%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 312,650.00 USD | 0.00 USD | 2,970.00 USD | `-5.17%` | `3,654.30` |
| `Live` | `Long` | `0.8125` | 309,680.00 USD | 0.00 USD | 1,160.00 USD | `-5.06%` | `1,421.60` |
| `Live` | `Long` | `0.8135` | 308,530.00 USD | 0.00 USD | 3,800.00 USD | `-4.94%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 304,720.00 USD | 0.00 USD | 2,500.00 USD | `-4.82%` | `3,068.40` |
| `Live` | `Long` | `0.8155` | 302,220.00 USD | 0.00 USD | 46,410.00 USD | `-4.70%` | `56,908.50` |
| `Live` | `Long` | `0.8165` | 255,810.00 USD | 0.00 USD | 3,590.00 USD | `-4.59%` | `4,402.10` |
| `Live` | `Long` | `0.8175` | 252,220.00 USD | 0.00 USD | 102,870.00 USD | `-4.47%` | `125,840.80` |
| `Live` | `Long` | `0.8185` | 149,340.00 USD | 0.00 USD | 491.10 USD | `-4.35%` | `600.00` |
| `Live` | `Long` | `0.8195` | 148,850.00 USD | 0.00 USD | 1,110.00 USD | `-4.24%` | `1,360.00` |
| `Live` | `Long` | `0.8205` | 147,740.00 USD | 0.00 USD | 1,300.00 USD | `-4.12%` | `1,580.30` |
| `Live` | `Long` | `0.8225` | 146,440.00 USD | 0.00 USD | 3,080.00 USD | `-3.89%` | `3,747.80` |
| `Live` | `Long` | `0.8245` | 143,360.00 USD | 0.00 USD | 18,280.00 USD | `-3.65%` | `22,175.00` |
| `Live` | `Long` | `0.8255` | 125,080.00 USD | 0.00 USD | 317.82 USD | `-3.54%` | `385.00` |
| `Live` | `Long` | `0.8275` | 124,760.00 USD | 0.00 USD | 4,690.00 USD | `-3.30%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 120,070.00 USD | 0.00 USD | 120,070.00 USD | `-3.19%` | `144,926.90` |
| `Live` | `Short` | `0.8875` | 2,740.00 USD | 2,740.00 USD | 0.00 USD | `+3.71%` | `3,086.60` |
| `Live` | `Short` | `0.8885` | 4,310.00 USD | 1,570.00 USD | 0.00 USD | `+3.83%` | `1,772.50` |
| `Live` | `Short` | `0.8935` | 4,560.00 USD | 245.27 USD | 0.00 USD | `+4.41%` | `274.50` |
| `Live` | `Short` | `0.8965` | 4,750.00 USD | 187.46 USD | 0.00 USD | `+4.76%` | `209.10` |
| `Live` | `Short` | `0.8985` | 9,110.00 USD | 4,360.00 USD | 0.00 USD | `+4.99%` | `4,853.90` |
| `Live` | `Short` | `0.9015` | 16,930.00 USD | 7,830.00 USD | 0.00 USD | `+5.34%` | `8,680.50` |
| `Live` | `Short` | `0.9145` | 21,000.00 USD | 4,060.00 USD | 0.00 USD | `+6.86%` | `4,444.10` |
| `Live` | `Short` | `0.9175` | 23,910.00 USD | 2,910.00 USD | 0.00 USD | `+7.21%` | `3,170.30` |
| `Live` | `Short` | `0.9775` | 24,010.00 USD | 100.88 USD | 0.00 USD | `+14.23%` | `103.20` |
| `Live` | `Short` | `0.9805` | 25,060.00 USD | 1,050.00 USD | 0.00 USD | `+14.58%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 25,420.00 USD | 365.70 USD | 0.00 USD | `+15.28%` | `370.70` |
| `Live` | `Short` | `0.9885` | 29,680.00 USD | 4,250.00 USD | 0.00 USD | `+15.51%` | `4,304.30` |
| `Live` | `Short` | `0.9905` | 31,250.00 USD | 1,570.00 USD | 0.00 USD | `+15.75%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 31,390.00 USD | 139.59 USD | 0.00 USD | `+16.10%` | `140.50` |
| `Live` | `Short` | `1.00` | 31,720.00 USD | 330.29 USD | 0.00 USD | `+17.03%` | `329.80` |
| `Live` | `Short` | `1.02` | 31,890.00 USD | 170.40 USD | 0.00 USD | `+18.67%` | `167.80` |
| `Live` | `Short` | `1.02` | 34,730.00 USD | 2,850.00 USD | 0.00 USD | `+19.02%` | `2,794.00` |
| `Live` | `Short` | `1.04` | 34,890.00 USD | 155.92 USD | 0.00 USD | `+21.47%` | `150.00` |
| `Live` | `Short` | `1.04` | 36,730.00 USD | 1,840.00 USD | 0.00 USD | `+21.59%` | `1,772.80` |
| `Live` | `Short` | `1.05` | 37,330.00 USD | 597.52 USD | 0.00 USD | `+22.76%` | `568.80` |
| `Live` | `Short` | `1.05` | 39,720.00 USD | 2,390.00 USD | 0.00 USD | `+22.87%` | `2,272.10` |
| `Live` | `Short` | `1.08` | 43,300.00 USD | 3,580.00 USD | 0.00 USD | `+26.26%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 48,850.00 USD | 5,550.00 USD | 0.00 USD | `+27.31%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 49,180.00 USD | 324.90 USD | 0.00 USD | `+28.48%` | `295.50` |
| `Live` | `Short` | `1.10` | 49,460.00 USD | 277.22 USD | 0.00 USD | `+28.60%` | `251.90` |
| `Live` | `Short` | `1.10` | 50,760.00 USD | 1,310.00 USD | 0.00 USD | `+29.07%` | `1,182.10` |
| `Live` | `Short` | `1.11` | 59,700.00 USD | 8,940.00 USD | 0.00 USD | `+29.77%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 83,010.00 USD | 23,310.00 USD | 0.00 USD | `+31.64%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 83,640.00 USD | 634.09 USD | 0.00 USD | `+32.34%` | `559.90` |
| `Live` | `Short` | `1.13` | 84,120.00 USD | 477.74 USD | 0.00 USD | `+32.57%` | `421.10` |
| `Live` | `Short` | `1.17` | 114,450.00 USD | 30,330.00 USD | 0.00 USD | `+36.55%` | `25,957.80` |
| `Live` | `Short` | `1.20` | 114,700.00 USD | 253.69 USD | 0.00 USD | `+40.17%` | `211.50` |
| `Live` | `Short` | `1.21` | 119,530.00 USD | 4,830.00 USD | 0.00 USD | `+40.99%` | `3,999.60` |
| `Live` | `Short` | `1.22` | 123,970.00 USD | 4,440.00 USD | 0.00 USD | `+42.39%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 124,360.00 USD | 382.70 USD | 0.00 USD | `+42.74%` | `313.30` |
| `Live` | `Short` | `1.23` | 124,740.00 USD | 380.84 USD | 0.00 USD | `+44.26%` | `308.50` |
| `Live` | `Short` | `1.24` | 128,660.00 USD | 3,930.00 USD | 0.00 USD | `+44.73%` | `3,169.40` |
| `Live` | `Short` | `1.24` | 129,890.00 USD | 1,230.00 USD | 0.00 USD | `+44.96%` | `989.90` |
| `Live` | `Short` | `1.26` | 132,560.00 USD | 2,670.00 USD | 0.00 USD | `+47.18%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 134,860.00 USD | 2,300.00 USD | 0.00 USD | `+49.28%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 174,750.00 USD | 39,880.00 USD | 0.00 USD | `+49.87%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 195,320.00 USD | 20,570.00 USD | 0.00 USD | `+50.80%` | `15,941.90` |
| `Live` | `Short` | `1.29` | 195,550.00 USD | 226.80 USD | 0.00 USD | `+51.27%` | `175.20` |
| `Live` | `Short` | `1.30` | 195,660.00 USD | 114.40 USD | 0.00 USD | `+51.74%` | `88.10` |
| `Live` | `Short` | `1.30` | 196,740.00 USD | 1,080.00 USD | 0.00 USD | `+52.09%` | `826.40` |
| `Live` | `Short` | `1.31` | 197,750.00 USD | 1,020.00 USD | 0.00 USD | `+53.02%` | `777.20` |
| `Live` | `Short` | `1.31` | 229,290.00 USD | 31,530.00 USD | 0.00 USD | `+53.26%` | `24,042.40` |
| `Live` | `Short` | `1.33` | 245,720.00 USD | 16,440.00 USD | 0.00 USD | `+54.89%` | `12,399.30` |
| `Live` | `Short` | `1.33` | 267,690.00 USD | 21,970.00 USD | 0.00 USD | `+55.24%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 274,550.00 USD | 6,860.00 USD | 0.00 USD | `+56.53%` | `5,119.30` |
| `Live` | `Short` | `1.36` | 275,200.00 USD | 653.49 USD | 0.00 USD | `+58.40%` | `482.10` |
| `Live` | `Short` | `1.37` | 633,480.00 USD | 358,280.00 USD | 0.00 USD | `+60.38%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 637,930.00 USD | 4,450.00 USD | 0.00 USD | `+65.29%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 638,330.00 USD | 402.08 USD | 0.00 USD | `+67.86%` | `279.90` |
| `Live` | `Short` | `1.44` | 638,620.00 USD | 288.68 USD | 0.00 USD | `+68.33%` | `200.40` |
| `Live` | `Short` | `1.46` | 638,740.00 USD | 123.41 USD | 0.00 USD | `+70.67%` | `84.50` |
| `Live` | `Short` | `1.49` | 655,430.00 USD | 16,690.00 USD | 0.00 USD | `+74.41%` | `11,182.60` |
| `Live` | `Short` | `1.51` | 659,450.00 USD | 4,020.00 USD | 0.00 USD | `+76.98%` | `2,654.10` |
| `Live` | `Short` | `1.52` | 660,960.00 USD | 1,510.00 USD | 0.00 USD | `+78.15%` | `990.70` |
| `Live` | `Short` | `1.53` | 670,900.00 USD | 9,940.00 USD | 0.00 USD | `+78.96%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 671,050.00 USD | 144.34 USD | 0.00 USD | `+79.43%` | `94.00` |
| `Live` | `Short` | `1.56` | 671,230.00 USD | 182.27 USD | 0.00 USD | `+82.35%` | `116.80` |
| `Live` | `Short` | `1.58` | 671,510.00 USD | 285.21 USD | 0.00 USD | `+84.34%` | `180.80` |
| `Live` | `Short` | `1.59` | 674,870.00 USD | 3,350.00 USD | 0.00 USD | `+86.21%` | `2,103.30` |
| `Live` | `Short` | `1.60` | 674,990.00 USD | 123.81 USD | 0.00 USD | `+86.68%` | `77.50` |
| `Live` | `Short` | `1.60` | 676,120.00 USD | 1,130.00 USD | 0.00 USD | `+87.26%` | `704.60` |
| `Live` | `Short` | `1.64` | 676,290.00 USD | 169.11 USD | 0.00 USD | `+91.12%` | `103.40` |
| `Live` | `Short` | `1.65` | 697,620.00 USD | 21,330.00 USD | 0.00 USD | `+92.40%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 701,560.00 USD | 3,940.00 USD | 0.00 USD | `+93.22%` | `2,381.50` |
| `Live` | `Short` | `1.66` | 740,580.00 USD | 39,020.00 USD | 0.00 USD | `+93.80%` | `23,529.40` |
| `Live` | `Short` | `1.66` | 744,210.00 USD | 3,620.00 USD | 0.00 USD | `+93.92%` | `2,184.10` |
| `Live` | `Short` | `1.68` | 1,040,000.00 USD | 291,420.00 USD | 0.00 USD | `+96.84%` | `173,000.00` |
| `Live` | `Short` | `1.69` | 1,040,000.00 USD | 165.81 USD | 0.00 USD | `+97.31%` | `98.20` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,180,000.00 USD | 0.00 USD | 497.31 USD | `-69.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2745` | 1,180,000.00 USD | 0.00 USD | 455.97 USD | `-67.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,180,000.00 USD | 0.00 USD | 102.75 USD | `-59.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,180,000.00 USD | 0.00 USD | 256.78 USD | `-59.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,180,000.00 USD | 0.00 USD | 428.87 USD | `-54.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,180,000.00 USD | 0.00 USD | 123.45 USD | `-51.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,180,000.00 USD | 0.00 USD | 818.15 USD | `-50.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,180,000.00 USD | 0.00 USD | 436.41 USD | `-49.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,180,000.00 USD | 0.00 USD | 876.79 USD | `-49.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,180,000.00 USD | 0.00 USD | 466.72 USD | `-47.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,180,000.00 USD | 0.00 USD | 142.95 USD | `-44.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,180,000.00 USD | 0.00 USD | 3,010.00 USD | `-41.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,180,000.00 USD | 0.00 USD | 151.74 USD | `-39.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,170,000.00 USD | 0.00 USD | 123.91 USD | `-39.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,170,000.00 USD | 0.00 USD | 219.80 USD | `-35.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,170,000.00 USD | 0.00 USD | 237,400.00 USD | `-35.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 937,250.00 USD | 0.00 USD | 276.75 USD | `-35.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 936,970.00 USD | 0.00 USD | 1,680.00 USD | `-34.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 935,290.00 USD | 0.00 USD | 853.41 USD | `-33.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 934,440.00 USD | 0.00 USD | 119.76 USD | `-32.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 934,320.00 USD | 0.00 USD | 3,520.00 USD | `-31.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 930,790.00 USD | 0.00 USD | 470.62 USD | `-30.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 930,320.00 USD | 0.00 USD | 108.39 USD | `-29.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 930,220.00 USD | 0.00 USD | 123.28 USD | `-29.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 930,090.00 USD | 0.00 USD | 488.52 USD | `-27.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 929,600.00 USD | 0.00 USD | 4,230.00 USD | `-26.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 925,380.00 USD | 0.00 USD | 242.24 USD | `-26.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 925,140.00 USD | 0.00 USD | 193.95 USD | `-24.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 924,940.00 USD | 0.00 USD | 149.22 USD | `-23.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 924,790.00 USD | 0.00 USD | 158.54 USD | `-23.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 924,630.00 USD | 0.00 USD | 195.47 USD | `-23.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 924,440.00 USD | 0.00 USD | 112.91 USD | `-22.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 924,330.00 USD | 0.00 USD | 181.31 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 924,140.00 USD | 0.00 USD | 190.25 USD | `-22.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 923,950.00 USD | 0.00 USD | 153.53 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 923,800.00 USD | 0.00 USD | 52,450.00 USD | `-21.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 871,350.00 USD | 0.00 USD | 536.11 USD | `-21.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 870,820.00 USD | 0.00 USD | 918.68 USD | `-20.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 869,900.00 USD | 0.00 USD | 340.75 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 869,560.00 USD | 0.00 USD | 9,270.00 USD | `-19.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 860,290.00 USD | 0.00 USD | 120.53 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 860,170.00 USD | 0.00 USD | 160.71 USD | `-18.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 860,010.00 USD | 0.00 USD | 738.08 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 859,270.00 USD | 0.00 USD | 187.61 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 859,090.00 USD | 0.00 USD | 2,920.00 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 856,170.00 USD | 0.00 USD | 89,150.00 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 767,010.00 USD | 0.00 USD | 189.06 USD | `-17.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 766,830.00 USD | 0.00 USD | 5,650.00 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 761,170.00 USD | 0.00 USD | 371.68 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 760,800.00 USD | 0.00 USD | 152.05 USD | `-16.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 760,650.00 USD | 0.00 USD | 123.41 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 760,530.00 USD | 0.00 USD | 745.54 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 759,780.00 USD | 0.00 USD | 1,130.00 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 758,650.00 USD | 0.00 USD | 18,770.00 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 739,880.00 USD | 0.00 USD | 7,970.00 USD | `-14.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 731,910.00 USD | 0.00 USD | 257.26 USD | `-13.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 731,660.00 USD | 0.00 USD | 161.72 USD | `-13.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 731,490.00 USD | 0.00 USD | 1,590.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 729,900.00 USD | 0.00 USD | 10,160.00 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 719,740.00 USD | 0.00 USD | 94,190.00 USD | `-12.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 625,550.00 USD | 0.00 USD | 1,230.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 624,320.00 USD | 0.00 USD | 1,840.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 622,480.00 USD | 0.00 USD | 804.61 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 621,680.00 USD | 0.00 USD | 590.68 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 621,090.00 USD | 0.00 USD | 635.62 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 620,450.00 USD | 0.00 USD | 191.12 USD | `-10.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 620,260.00 USD | 0.00 USD | 909.56 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 619,350.00 USD | 0.00 USD | 125.92 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 619,230.00 USD | 0.00 USD | 1,980.00 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 617,250.00 USD | 0.00 USD | 1,150.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 616,100.00 USD | 0.00 USD | 1,500.00 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 614,600.00 USD | 0.00 USD | 1,860.00 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 612,750.00 USD | 0.00 USD | 167,180.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 445,560.00 USD | 0.00 USD | 6,960.00 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 438,610.00 USD | 0.00 USD | 135.11 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 438,470.00 USD | 0.00 USD | 8,870.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 429,600.00 USD | 0.00 USD | 1,500.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 428,100.00 USD | 0.00 USD | 25,170.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 402,930.00 USD | 0.00 USD | 103.42 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 402,830.00 USD | 0.00 USD | 1,260.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 401,570.00 USD | 0.00 USD | 319.40 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 401,250.00 USD | 0.00 USD | 4,740.00 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 396,510.00 USD | 0.00 USD | 2,590.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 393,920.00 USD | 0.00 USD | 144.67 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 393,780.00 USD | 0.00 USD | 1,510.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 392,270.00 USD | 0.00 USD | 50,540.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 341,730.00 USD | 0.00 USD | 263.25 USD | `-5.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 341,470.00 USD | 0.00 USD | 1,250.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 340,220.00 USD | 0.00 USD | 91,080.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 249,140.00 USD | 0.00 USD | 174.63 USD | `-5.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 248,970.00 USD | 0.00 USD | 1,010.00 USD | `-5.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 247,950.00 USD | 0.00 USD | 123,350.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 124,600.00 USD | 0.00 USD | 1,160.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 123,440.00 USD | 0.00 USD | 216.70 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 123,230.00 USD | 0.00 USD | 125.72 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 123,100.00 USD | 0.00 USD | 4,860.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 118,240.00 USD | 0.00 USD | 21,270.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 96,970.00 USD | 0.00 USD | 7,160.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 89,820.00 USD | 0.00 USD | 226.71 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 89,590.00 USD | 0.00 USD | 22,470.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 67,120.00 USD | 0.00 USD | 1,320.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 65,800.00 USD | 0.00 USD | 325.56 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 65,480.00 USD | 0.00 USD | 666.55 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 64,810.00 USD | 0.00 USD | 577.25 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 64,230.00 USD | 0.00 USD | 5,760.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 58,480.00 USD | 0.00 USD | 171.46 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 58,300.00 USD | 0.00 USD | 12,800.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 45,500.00 USD | 0.00 USD | 1,270.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 44,230.00 USD | 0.00 USD | 4,170.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 40,060.00 USD | 0.00 USD | 1,800.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 38,260.00 USD | 0.00 USD | 610.23 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 37,650.00 USD | 0.00 USD | 699.65 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 36,950.00 USD | 0.00 USD | 320.31 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 36,630.00 USD | 0.00 USD | 240.52 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 36,390.00 USD | 0.00 USD | 4,080.00 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 32,310.00 USD | 0.00 USD | 710.23 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 31,600.00 USD | 0.00 USD | 212.81 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 31,380.00 USD | 0.00 USD | 585.76 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 30,800.00 USD | 0.00 USD | 481.80 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 30,320.00 USD | 0.00 USD | 451.83 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 29,860.00 USD | 0.00 USD | 12,890.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 16,970.00 USD | 0.00 USD | 345.13 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 16,630.00 USD | 0.00 USD | 16,630.00 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8565` | 3,640.00 USD | 3,640.00 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8575` | 7,650.00 USD | 4,010.00 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8585` | 16,550.00 USD | 8,900.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8595` | 24,350.00 USD | 7,800.00 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8605` | 28,780.00 USD | 4,430.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8615` | 34,930.00 USD | 6,160.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8625` | 39,120.00 USD | 4,190.00 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8635` | 40,110.00 USD | 987.33 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8645` | 42,520.00 USD | 2,420.00 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8655` | 45,830.00 USD | 3,310.00 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8665` | 52,740.00 USD | 6,910.00 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8675` | 53,480.00 USD | 741.45 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8685` | 53,890.00 USD | 410.11 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8695` | 59,230.00 USD | 5,340.00 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8705` | 71,190.00 USD | 11,960.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8715` | 71,900.00 USD | 712.45 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 72,020.00 USD | 116.74 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8735` | 74,440.00 USD | 2,420.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8745` | 75,310.00 USD | 866.37 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8755` | 110,330.00 USD | 35,020.00 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8765` | 110,960.00 USD | 635.29 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8775` | 120,030.00 USD | 9,070.00 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8785` | 120,180.00 USD | 151.10 USD | 0.00 USD | `+2.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8795` | 122,180.00 USD | 2,000.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8805` | 123,210.00 USD | 1,030.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8815` | 127,280.00 USD | 4,070.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8825` | 127,840.00 USD | 563.65 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8835` | 128,780.00 USD | 940.66 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 132,440.00 USD | 3,660.00 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 136,040.00 USD | 3,600.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 136,270.00 USD | 235.54 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 147,630.00 USD | 11,360.00 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 156,410.00 USD | 8,780.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 157,430.00 USD | 1,020.00 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 157,900.00 USD | 469.91 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 168,510.00 USD | 10,610.00 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 168,790.00 USD | 277.07 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 168,890.00 USD | 100.09 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 169,020.00 USD | 129.22 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 169,310.00 USD | 289.12 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 187,510.00 USD | 18,210.00 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 188,400.00 USD | 889.43 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 217,370.00 USD | 28,960.00 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 219,170.00 USD | 1,800.00 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 221,220.00 USD | 2,050.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 222,150.00 USD | 926.06 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 222,340.00 USD | 188.92 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 225,290.00 USD | 2,950.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 227,280.00 USD | 1,990.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 227,420.00 USD | 138.69 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 227,670.00 USD | 250.83 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 228,770.00 USD | 1,090.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 230,290.00 USD | 1,520.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 231,220.00 USD | 933.08 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 231,480.00 USD | 260.23 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 232,510.00 USD | 1,030.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 235,540.00 USD | 3,020.00 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 238,610.00 USD | 3,070.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 239,180.00 USD | 570.08 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 239,490.00 USD | 309.14 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 243,390.00 USD | 3,900.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 245,360.00 USD | 1,970.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 245,480.00 USD | 116.59 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 504,600.00 USD | 259,120.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 656,560.00 USD | 151,960.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 661,630.00 USD | 5,070.00 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 662,130.00 USD | 495.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 663,530.00 USD | 1,400.00 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 668,400.00 USD | 4,880.00 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 670,610.00 USD | 2,200.00 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 670,900.00 USD | 287.62 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 671,100.00 USD | 199.16 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 671,230.00 USD | 130.59 USD | 0.00 USD | `+8.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 671,680.00 USD | 448.69 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 671,800.00 USD | 120.16 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 672,830.00 USD | 1,030.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 673,400.00 USD | 568.87 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 673,690.00 USD | 292.78 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 674,210.00 USD | 523.79 USD | 0.00 USD | `+9.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 674,910.00 USD | 701.16 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 675,020.00 USD | 104.53 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 728,080.00 USD | 53,060.00 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 731,990.00 USD | 3,910.00 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 740,950.00 USD | 8,960.00 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 741,480.00 USD | 529.50 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 741,780.00 USD | 301.79 USD | 0.00 USD | `+10.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 743,480.00 USD | 1,700.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 744,270.00 USD | 789.04 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 744,390.00 USD | 117.81 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 745,440.00 USD | 1,050.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 751,440.00 USD | 6,000.00 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 770,560.00 USD | 19,120.00 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 770,830.00 USD | 261.97 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 775,050.00 USD | 4,220.00 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 775,210.00 USD | 159.19 USD | 0.00 USD | `+11.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 785,120.00 USD | 9,910.00 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 788,260.00 USD | 3,150.00 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 789,700.00 USD | 1,440.00 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 792,590.00 USD | 2,890.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 793,720.00 USD | 1,130.00 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 793,840.00 USD | 121.54 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 794,000.00 USD | 155.06 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 846,500.00 USD | 52,510.00 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 846,670.00 USD | 161.82 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 866,070.00 USD | 19,400.00 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 866,210.00 USD | 139.23 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 867,540.00 USD | 1,340.00 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 868,080.00 USD | 537.78 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 868,610.00 USD | 531.57 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 871,770.00 USD | 3,160.00 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 872,770.00 USD | 993.78 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 872,980.00 USD | 212.90 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 884,660.00 USD | 11,680.00 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 884,780.00 USD | 125.61 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 885,220.00 USD | 441.51 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 895,410.00 USD | 10,190.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 895,670.00 USD | 253.14 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 899,870.00 USD | 4,200.00 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 900,040.00 USD | 176.73 USD | 0.00 USD | `+14.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 900,560.00 USD | 513.32 USD | 0.00 USD | `+14.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 935,920.00 USD | 35,360.00 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 967,770.00 USD | 31,850.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 972,570.00 USD | 4,800.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 973,120.00 USD | 558.35 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 974,190.00 USD | 1,060.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 975,370.00 USD | 1,180.00 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 975,860.00 USD | 490.99 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 976,250.00 USD | 395.21 USD | 0.00 USD | `+15.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 977,250.00 USD | 991.50 USD | 0.00 USD | `+15.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 987,580.00 USD | 10,340.00 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 987,990.00 USD | 409.52 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 988,280.00 USD | 284.92 USD | 0.00 USD | `+16.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 988,630.00 USD | 350.37 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 988,750.00 USD | 124.04 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 988,870.00 USD | 117.26 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 991,040.00 USD | 2,180.00 USD | 0.00 USD | `+17.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 991,820.00 USD | 778.64 USD | 0.00 USD | `+17.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 992,190.00 USD | 363.87 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 992,780.00 USD | 589.52 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 992,890.00 USD | 110.62 USD | 0.00 USD | `+17.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,000,000.00 USD | 10,090.00 USD | 0.00 USD | `+17.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 5,420.00 USD | 0.00 USD | `+17.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,010,000.00 USD | 248.49 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,020,000.00 USD | 9,150.00 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,020,000.00 USD | 722.63 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,020,000.00 USD | 312.07 USD | 0.00 USD | `+19.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,020,000.00 USD | 171.24 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,020,000.00 USD | 561.11 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,020,000.00 USD | 249.30 USD | 0.00 USD | `+19.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,020,000.00 USD | 1,470.00 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,020,000.00 USD | 432.18 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,020,000.00 USD | 137.88 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,030,000.00 USD | 2,340.00 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,030,000.00 USD | 694.72 USD | 0.00 USD | `+20.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,030,000.00 USD | 160.60 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,030,000.00 USD | 6,560.00 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,040,000.00 USD | 2,920.00 USD | 0.00 USD | `+21.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,040,000.00 USD | 224.56 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,040,000.00 USD | 3,570.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,040,000.00 USD | 432.19 USD | 0.00 USD | `+22.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,040,000.00 USD | 1,700.00 USD | 0.00 USD | `+22.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,740,000.00 USD | 1,690,000.00 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,740,000.00 USD | 5,390.00 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,740,000.00 USD | 285.32 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,740,000.00 USD | 1,130.00 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,740,000.00 USD | 1,240.00 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,750,000.00 USD | 278.06 USD | 0.00 USD | `+24.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,750,000.00 USD | 309.00 USD | 0.00 USD | `+24.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,750,000.00 USD | 228.98 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,750,000.00 USD | 272.12 USD | 0.00 USD | `+25.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,750,000.00 USD | 117.12 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,890,000.00 USD | 140,120.00 USD | 0.00 USD | `+25.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,890,000.00 USD | 530.01 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,890,000.00 USD | 128.23 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,990,000.00 USD | 108,190.00 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,000,000.00 USD | 3,430.00 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,000,000.00 USD | 550.49 USD | 0.00 USD | `+26.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,000,000.00 USD | 5,810.00 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,010,000.00 USD | 1,520.00 USD | 0.00 USD | `+26.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,010,000.00 USD | 5,570.00 USD | 0.00 USD | `+27.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,010,000.00 USD | 1,290.00 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,010,000.00 USD | 294.81 USD | 0.00 USD | `+27.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,010,000.00 USD | 183.11 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,010,000.00 USD | 123.13 USD | 0.00 USD | `+28.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,010,000.00 USD | 494.98 USD | 0.00 USD | `+28.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,010,000.00 USD | 613.52 USD | 0.00 USD | `+28.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,130,000.00 USD | 115,100.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,130,000.00 USD | 409.76 USD | 0.00 USD | `+28.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,130,000.00 USD | 162.77 USD | 0.00 USD | `+28.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,130,000.00 USD | 959.70 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,130,000.00 USD | 160.18 USD | 0.00 USD | `+29.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,130,000.00 USD | 669.85 USD | 0.00 USD | `+29.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,130,000.00 USD | 293.61 USD | 0.00 USD | `+30.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,240,000.00 USD | 112,050.00 USD | 0.00 USD | `+30.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,250,000.00 USD | 462.47 USD | 0.00 USD | `+31.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,250,000.00 USD | 2,180.00 USD | 0.00 USD | `+31.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,250,000.00 USD | 273.34 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,250,000.00 USD | 119.49 USD | 0.00 USD | `+32.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,270,000.00 USD | 20,740.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,270,000.00 USD | 468.47 USD | 0.00 USD | `+32.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,270,000.00 USD | 1,430.00 USD | 0.00 USD | `+33.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,270,000.00 USD | 338.50 USD | 0.00 USD | `+33.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,270,000.00 USD | 2,640.00 USD | 0.00 USD | `+34.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,270,000.00 USD | 1,230.00 USD | 0.00 USD | `+34.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,280,000.00 USD | 2,450.00 USD | 0.00 USD | `+35.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,280,000.00 USD | 1,250.00 USD | 0.00 USD | `+35.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,280,000.00 USD | 143.67 USD | 0.00 USD | `+35.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,280,000.00 USD | 989.81 USD | 0.00 USD | `+36.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,280,000.00 USD | 304.33 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,280,000.00 USD | 255.14 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,280,000.00 USD | 241.65 USD | 0.00 USD | `+37.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,280,000.00 USD | 239.97 USD | 0.00 USD | `+37.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,280,000.00 USD | 2,470.00 USD | 0.00 USD | `+37.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,290,000.00 USD | 3,060.00 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,600,000.00 USD | 310,250.00 USD | 0.00 USD | `+38.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,600,000.00 USD | 309.53 USD | 0.00 USD | `+39.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,600,000.00 USD | 159.09 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,600,000.00 USD | 146.21 USD | 0.00 USD | `+39.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,620,000.00 USD | 18,420.00 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,620,000.00 USD | 933.81 USD | 0.00 USD | `+40.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,620,000.00 USD | 658.86 USD | 0.00 USD | `+40.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,830,000.00 USD | 213,390.00 USD | 0.00 USD | `+41.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,830,000.00 USD | 211.10 USD | 0.00 USD | `+41.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,830,000.00 USD | 1,050.00 USD | 0.00 USD | `+42.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,830,000.00 USD | 509.71 USD | 0.00 USD | `+42.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,830,000.00 USD | 162.15 USD | 0.00 USD | `+43.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,830,000.00 USD | 187.04 USD | 0.00 USD | `+43.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,830,000.00 USD | 542.12 USD | 0.00 USD | `+44.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,860,000.00 USD | 23,740.00 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,860,000.00 USD | 2,010.00 USD | 0.00 USD | `+44.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,860,000.00 USD | 345.91 USD | 0.00 USD | `+44.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,860,000.00 USD | 104.79 USD | 0.00 USD | `+45.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,860,000.00 USD | 100.04 USD | 0.00 USD | `+46.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,860,000.00 USD | 517.52 USD | 0.00 USD | `+46.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,860,000.00 USD | 152.29 USD | 0.00 USD | `+46.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,860,000.00 USD | 1,480.00 USD | 0.00 USD | `+47.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,860,000.00 USD | 1,010.00 USD | 0.00 USD | `+47.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,870,000.00 USD | 2,780.00 USD | 0.00 USD | `+48.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,870,000.00 USD | 340.38 USD | 0.00 USD | `+48.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,870,000.00 USD | 903.22 USD | 0.00 USD | `+48.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,870,000.00 USD | 475.01 USD | 0.00 USD | `+48.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,910,000.00 USD | 41,160.00 USD | 0.00 USD | `+49.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,920,000.00 USD | 12,840.00 USD | 0.00 USD | `+49.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,120,000.00 USD | 194,770.00 USD | 0.00 USD | `+50.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,130,000.00 USD | 12,890.00 USD | 0.00 USD | `+50.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,140,000.00 USD | 8,820.00 USD | 0.00 USD | `+50.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,140,000.00 USD | 466.95 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,140,000.00 USD | 613.59 USD | 0.00 USD | `+51.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,140,000.00 USD | 1,420.00 USD | 0.00 USD | `+51.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,150,000.00 USD | 13,000.00 USD | 0.00 USD | `+51.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,150,000.00 USD | 284.42 USD | 0.00 USD | `+51.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 4,180,000.00 USD | 22,810.00 USD | 0.00 USD | `+54.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,180,000.00 USD | 640.82 USD | 0.00 USD | `+55.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,180,000.00 USD | 134.75 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 4,190,000.00 USD | 13,400.00 USD | 0.00 USD | `+56.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,200,000.00 USD | 13,490.00 USD | 0.00 USD | `+57.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,220,000.00 USD | 11,580.00 USD | 0.00 USD | `+57.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,220,000.00 USD | 3,610.00 USD | 0.00 USD | `+58.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,220,000.00 USD | 1,500.00 USD | 0.00 USD | `+59.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,240,000.00 USD | 15,000.00 USD | 0.00 USD | `+59.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,240,000.00 USD | 9,030.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,240,000.00 USD | 405.86 USD | 0.00 USD | `+62.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,260,000.00 USD | 13,890.00 USD | 0.00 USD | `+62.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,270,000.00 USD | 14,000.00 USD | 0.00 USD | `+63.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,290,000.00 USD | 12,560.00 USD | 0.00 USD | `+63.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,320,000.00 USD | 32,860.00 USD | 0.00 USD | `+64.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,320,000.00 USD | 102.40 USD | 0.00 USD | `+64.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,320,000.00 USD | 106.64 USD | 0.00 USD | `+65.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,320,000.00 USD | 1,430.00 USD | 0.00 USD | `+65.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,320,000.00 USD | 2,810.00 USD | 0.00 USD | `+65.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,330,000.00 USD | 8,420.00 USD | 0.00 USD | `+65.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,330,000.00 USD | 1,410.00 USD | 0.00 USD | `+66.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,330,000.00 USD | 145.37 USD | 0.00 USD | `+67.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,330,000.00 USD | 1,390.00 USD | 0.00 USD | `+68.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,350,000.00 USD | 14,390.00 USD | 0.00 USD | `+68.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,360,000.00 USD | 7,000.00 USD | 0.00 USD | `+69.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,370,000.00 USD | 14,490.00 USD | 0.00 USD | `+69.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,370,000.00 USD | 1,370.00 USD | 0.00 USD | `+69.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,370,000.00 USD | 1,350.00 USD | 0.00 USD | `+70.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,370,000.00 USD | 1,340.00 USD | 0.00 USD | `+71.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,370,000.00 USD | 342.08 USD | 0.00 USD | `+72.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,380,000.00 USD | 1,330.00 USD | 0.00 USD | `+72.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,380,000.00 USD | 1,310.00 USD | 0.00 USD | `+73.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,390,000.00 USD | 14,890.00 USD | 0.00 USD | `+74.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,400,000.00 USD | 9,580.00 USD | 0.00 USD | `+74.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,420,000.00 USD | 14,980.00 USD | 0.00 USD | `+75.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,440,000.00 USD | 20,120.00 USD | 0.00 USD | `+75.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,440,000.00 USD | 1,180.00 USD | 0.00 USD | `+75.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,440,000.00 USD | 1,270.00 USD | 0.00 USD | `+77.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,440,000.00 USD | 1,260.00 USD | 0.00 USD | `+78.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,440,000.00 USD | 2,150.00 USD | 0.00 USD | `+80.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,440,000.00 USD | 158.76 USD | 0.00 USD | `+82.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,440,000.00 USD | 574.53 USD | 0.00 USD | `+85.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,440,000.00 USD | 391.32 USD | 0.00 USD | `+87.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,440,000.00 USD | 1,160.00 USD | 0.00 USD | `+89.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,450,000.00 USD | 1,140.00 USD | 0.00 USD | `+91.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,450,000.00 USD | 1,970.00 USD | 0.00 USD | `+91.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,450,000.00 USD | 281.45 USD | 0.00 USD | `+93.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,450,000.00 USD | 2,070.00 USD | 0.00 USD | `+94.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,460,000.00 USD | 13,060.00 USD | 0.00 USD | `+98.71%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7630` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 37,590.00 USD | 14,770.00 USD | 934.78 USD |
| `7D` | `0.7650` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 556.58 USD | 23,090.00 USD | 10,610.00 USD |
| `7D` | `0.7670` | 11,900,000.00 USD | 0.00 USD | 11,900,000.00 USD | 1,280.00 USD | 177.87 USD | 18,920.00 USD |
| `7D` | `0.7690` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD |
| `7D` | `0.7710` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7790` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 0.00 USD | 5,390.00 USD | 36.15 USD |
| `7D` | `0.7810` | 11,870,000.00 USD | 0.00 USD | 11,870,000.00 USD | 0.00 USD | 185.50 USD | 5,200.00 USD |
| `7D` | `0.7830` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD |
| `1D` | `0.7850` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 0.00 USD | 587.33 USD | 0.00 USD |
| `7D` | `0.7850` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD |
| `1D` | `0.7870` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 16,780.00 USD | 318.35 USD | 0.00 USD |
| `7D` | `0.7870` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD |
| `1D` | `0.7890` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 10,020.00 USD | 12,010.00 USD | 0.00 USD |
| `7D` | `0.7890` | 11,830,000.00 USD | 0.00 USD | 11,830,000.00 USD | 0.00 USD | 11,400.00 USD | 0.00 USD |
| `1D` | `0.7910` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 0.00 USD | 4,750.00 USD | 285.55 USD |
| `7D` | `0.7910` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 0.00 USD | 29,560.00 USD | 0.00 USD |
| `1D` | `0.7930` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | 12,600.00 USD | 31,460.00 USD |
| `7D` | `0.7930` | 11,790,000.00 USD | 0.00 USD | 11,790,000.00 USD | 0.00 USD | 12,880.00 USD | 77,250.00 USD |
| `1D` | `0.7950` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 13,930.00 USD | 266.53 USD | 14,720.00 USD |
| `7D` | `0.7950` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 0.00 USD | 18,870.00 USD | 51,850.00 USD |
| `1D` | `0.7970` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 3,300.00 USD | 9,330.00 USD | 22,070.00 USD |
| `7D` | `0.7970` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 12,100.00 USD | 0.00 USD | 38,500.00 USD |
| `1D` | `0.7990` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 505.25 USD | 322.55 USD | 18,780.00 USD |
| `7D` | `0.7990` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 488.55 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `0.8010` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 0.00 USD | 10,940.00 USD | 16,320.00 USD |
| `7D` | `0.8010` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,910.00 USD |
| `1D` | `0.8050` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 0.00 USD | 6,830.00 USD | 0.00 USD |
| `7D` | `0.8050` | 11,520,000.00 USD | 0.00 USD | 11,520,000.00 USD | 2,040.00 USD | 15,820.00 USD | 0.00 USD |
| `1D` | `0.8070` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 12,740.00 USD | 14,260.00 USD | 14,150.00 USD |
| `7D` | `0.8070` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD |
| `1D` | `0.8090` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `1D` | `0.8110` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 40,190.00 USD | 6,030.00 USD | 25,250.00 USD |
| `7D` | `0.8110` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD |
| `1D` | `0.8130` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 23,290.00 USD | 13,030.00 USD | 5,890.00 USD |
| `7D` | `0.8130` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD |
| `1D` | `0.8150` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 66,820.00 USD | 25,820.00 USD | 100,870.00 USD |
| `7D` | `0.8150` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 135,770.00 USD | 51,810.00 USD | 124,810.00 USD |
| `1D` | `0.8170` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 68,580.00 USD | 28,480.00 USD | 79,700.00 USD |
| `7D` | `0.8170` | 11,000,000.00 USD | 0.00 USD | 11,000,000.00 USD | 91,050.00 USD | 25,080.00 USD | 78,040.00 USD |
| `1D` | `0.8190` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 12,140.00 USD | 6,480.00 USD | 15,760.00 USD |
| `7D` | `0.8190` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 195,400.00 USD | 53,380.00 USD | 47,340.00 USD |
| `1D` | `0.8210` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 16,970.00 USD | 30,830.00 USD | 46,170.00 USD |
| `7D` | `0.8210` | 10,510,000.00 USD | 0.00 USD | 10,510,000.00 USD | 138,580.00 USD | 58,400.00 USD | 152,490.00 USD |
| `1D` | `0.8230` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 11,730.00 USD | 18,140.00 USD | 20,010.00 USD |
| `7D` | `0.8230` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 37,880.00 USD | 37,160.00 USD | 64,410.00 USD |
| `1D` | `0.8250` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 18,440.00 USD | 8,600.00 USD | 20,180.00 USD |
| `7D` | `0.8250` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 187,510.00 USD | 30,370.00 USD | 126,190.00 USD |
| `1D` | `0.8270` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 29,570.00 USD | 10,040.00 USD | 13,000.00 USD |
| `7D` | `0.8270` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 147,770.00 USD | 51,050.00 USD | 63,610.00 USD |
| `1D` | `0.8290` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 12,280.00 USD | 15,940.00 USD | 49,860.00 USD |
| `7D` | `0.8290` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 89,470.00 USD | 42,420.00 USD | 82,590.00 USD |
| `1D` | `0.8310` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 25,970.00 USD | 22,490.00 USD | 59,310.00 USD |
| `7D` | `0.8310` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 36,870.00 USD | 32,050.00 USD | 26,600.00 USD |
| `1D` | `0.8330` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 43,050.00 USD | 23,450.00 USD | 42,640.00 USD |
| `7D` | `0.8330` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 150,740.00 USD | 87,770.00 USD | 198,210.00 USD |
| `1D` | `0.8350` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 23,790.00 USD | 20,000.00 USD | 22,200.00 USD |
| `7D` | `0.8350` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 77,100.00 USD | 17,250.00 USD | 84,180.00 USD |
| `1D` | `0.8370` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 85,240.00 USD | 18,990.00 USD | 30,780.00 USD |
| `7D` | `0.8370` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 146,890.00 USD | 64,240.00 USD | 102,790.00 USD |
| `1D` | `0.8390` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 70,320.00 USD | 36,150.00 USD | 39,480.00 USD |
| `7D` | `0.8390` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 24,790.00 USD | 89,740.00 USD | 77,610.00 USD |
| `1D` | `0.8410` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 79,140.00 USD | 23,550.00 USD | 20,480.00 USD |
| `7D` | `0.8410` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 59,670.00 USD | 41,980.00 USD | 27,780.00 USD |
| `1D` | `0.8430` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 29,850.00 USD | 50,900.00 USD | 26,880.00 USD |
| `7D` | `0.8430` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 81,850.00 USD | 112,960.00 USD | 30,430.00 USD |
| `1D` | `0.8450` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 11,600.00 USD | 34,120.00 USD | 115,610.00 USD |
| `7D` | `0.8450` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 43,800.00 USD | 115,170.00 USD | 219,200.00 USD |
| `1D` | `0.8470` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 62,880.00 USD | 76,000.00 USD | 87,390.00 USD |
| `7D` | `0.8470` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 27,720.00 USD | 6,020.00 USD | 37,460.00 USD |
| `1D` | `0.8490` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 64,500.00 USD | 68,710.00 USD | 180,210.00 USD |
| `7D` | `0.8490` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 87,880.00 USD | 78,940.00 USD | 151,660.00 USD |
| `1D` | `0.8510` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 79,800.00 USD | 60,360.00 USD | 62,330.00 USD |
| `7D` | `0.8510` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 95,990.00 USD | 42,650.00 USD | 151,740.00 USD |
| `1D` | `0.8530` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 83,020.00 USD | 52,480.00 USD | 103,380.00 USD |
| `7D` | `0.8530` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 30,570.00 USD | 52,520.00 USD | 29,460.00 USD |
| `1D` | `0.8550` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 58,930.00 USD | 11,700.00 USD | 17,540.00 USD |
| `7D` | `0.8550` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 78,320.00 USD | 63,400.00 USD | 93,270.00 USD |
| `1D` | `0.8570` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 106,410.00 USD | 43,970.00 USD | 124.72 USD |
| `7D` | `0.8570` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 99,680.00 USD | 166,050.00 USD | 5,400.00 USD |
| `1D` | `0.8590` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 144,580.00 USD | 97,280.00 USD | 31,980.00 USD |
| `7D` | `0.8590` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 51,400.00 USD | 69,250.00 USD | 18,570.00 USD |
| `1D` | `0.8610` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 37,090.00 USD | 47,640.00 USD | 641.01 USD |
| `7D` | `0.8610` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 36,870.00 USD | 174,840.00 USD | 30,720.00 USD |
| `1D` | `0.8630` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 53,710.00 USD | 147,460.00 USD | 278,850.00 USD |
| `7D` | `0.8630` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 30,710.00 USD | 78,200.00 USD | 388,160.00 USD |
| `1D` | `0.8650` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 248,690.00 USD | 34,470.00 USD | 72,720.00 USD |
| `7D` | `0.8650` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 313,070.00 USD | 110,550.00 USD | 311,990.00 USD |
| `1D` | `0.8670` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 41,460.00 USD | 20,170.00 USD | 125.19 USD |
| `7D` | `0.8670` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 159,120.00 USD | 41,080.00 USD | 58,910.00 USD |
| `1D` | `0.8690` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 148,850.00 USD | 87,020.00 USD | 112,880.00 USD |
| `7D` | `0.8690` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 182,190.00 USD | 9,930.00 USD | 413,530.00 USD |
| `1D` | `0.8710` | 677,070.00 USD | 0.00 USD | 677,070.00 USD | 93,860.00 USD | 54,700.00 USD | 349,990.00 USD |
| `7D` | `0.8710` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 604,760.00 USD | 0.00 USD | 396,740.00 USD |
| `1D` | `0.8730` | 178,520.00 USD | 0.00 USD | 178,520.00 USD | 0.00 USD | 0.00 USD | 74,880.00 USD |
| `7D` | `0.8730` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 333,320.00 USD | 73,820.00 USD | 394,690.00 USD |
| `1D` | `0.8750` | 103,640.00 USD | 0.00 USD | 103,640.00 USD | 0.00 USD | 0.00 USD | 103,560.00 USD |
| `7D` | `0.8750` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 643,280.00 USD | 0.00 USD | 324,670.00 USD |
| `1D` | `0.8770` | 83.36 USD | 0.00 USD | 83.36 USD | 0.00 USD | 0.00 USD | 83.36 USD |
| `7D` | `0.8770` | 700,590.00 USD | 0.00 USD | 700,590.00 USD | 398,780.00 USD | 0.00 USD | 2,320.00 USD |
| `1D` | `0.8790` | 6,790.00 USD | 6,790.00 USD | 0.00 USD | 6,560.00 USD | 0.00 USD | 222.48 USD |
| `1D` | `0.8790` | 13,570.00 USD | 13,570.00 USD | 0.00 USD | 6,560.00 USD | 0.00 USD | 222.48 USD |
| `7D` | `0.8790` | 299,490.00 USD | 0.00 USD | 299,490.00 USD | 296,940.00 USD | 0.00 USD | 2,550.00 USD |
| `7D` | `0.8800` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8810` | 19,190.00 USD | 19,190.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8810` | 31,770.00 USD | 31,770.00 USD | 0.00 USD | 26,040.00 USD | 0.00 USD | 5,730.00 USD |
| `1D` | `0.8830` | 20,420.00 USD | 20,420.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8830` | 65,800.00 USD | 65,800.00 USD | 0.00 USD | 27,880.00 USD | 0.00 USD | 6,140.00 USD |
| `1D` | `0.8850` | 22,460.00 USD | 22,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD |
| `7D` | `0.8850` | 73,560.00 USD | 73,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,760.00 USD |
| `1D` | `0.8870` | 22,990.00 USD | 22,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 530.85 USD |
| `7D` | `0.8890` | 957,850.00 USD | 957,850.00 USD | 0.00 USD | 884,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8910` | 220,290.00 USD | 220,290.00 USD | 0.00 USD | 186,060.00 USD | 10,900.00 USD | 347.32 USD |
| `7D` | `0.8910` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 806,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8930` | 264,950.00 USD | 264,950.00 USD | 0.00 USD | 44,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8930` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8950` | 444,180.00 USD | 444,180.00 USD | 0.00 USD | 98,920.00 USD | 48,760.00 USD | 31,550.00 USD |
| `7D` | `0.8950` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 719,730.00 USD | 56,980.00 USD | 0.00 USD |
| `1D` | `0.8970` | 466,400.00 USD | 466,400.00 USD | 0.00 USD | 0.00 USD | 22,220.00 USD | 0.00 USD |
| `7D` | `0.8970` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 659,500.00 USD | 54,550.00 USD | 1,760.00 USD |
| `1D` | `0.8990` | 948,300.00 USD | 948,300.00 USD | 0.00 USD | 51,680.00 USD | 152,190.00 USD | 278,020.00 USD |
| `7D` | `0.8990` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 308,910.00 USD | 64,400.00 USD | 340,680.00 USD |
| `1D` | `0.9010` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 249,240.00 USD | 99,300.00 USD | 230,500.00 USD |
| `7D` | `0.9010` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 207,550.00 USD | 109,410.00 USD | 216,090.00 USD |
| `1D` | `0.9030` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 3,140.00 USD | 76,840.00 USD | 56,580.00 USD |
| `7D` | `0.9030` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 5,880.00 USD | 78,550.00 USD | 860.58 USD |
| `1D` | `0.9050` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 144,360.00 USD | 134,060.00 USD | 111,910.00 USD |
| `7D` | `0.9050` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 122,230.00 USD | 0.00 USD | 218,670.00 USD |
| `1D` | `0.9070` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 111,680.00 USD | 55,120.00 USD | 175,810.00 USD |
| `7D` | `0.9070` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9090` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 167,160.00 USD | 11,830.00 USD | 0.00 USD |
| `7D` | `0.9090` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD |
| `1D` | `0.9110` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 70,890.00 USD | 34,900.00 USD | 0.00 USD |
| `7D` | `0.9110` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD |
| `1D` | `0.9130` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 62,740.00 USD | 15,770.00 USD |
| `7D` | `0.9130` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 80,230.00 USD | 62,970.00 USD | 0.00 USD |
| `1D` | `0.9150` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 119,590.00 USD | 92,390.00 USD | 299,990.00 USD |
| `7D` | `0.9150` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD |
| `1D` | `0.9170` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 106,060.00 USD | 107,790.00 USD | 62,770.00 USD |
| `7D` | `0.9170` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 123,530.00 USD | 2,050.00 USD | 0.00 USD |
| `1D` | `0.9190` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 26,960.00 USD | 27,310.00 USD | 28,090.00 USD |
| `7D` | `0.9190` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 296,480.00 USD | 60,800.00 USD | 104,960.00 USD |
| `1D` | `0.9210` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 48,420.00 USD | 60,370.00 USD | 128,940.00 USD |
| `7D` | `0.9210` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 128,930.00 USD | 18,660.00 USD | 173,150.00 USD |
| `1D` | `0.9230` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 230,840.00 USD | 77,080.00 USD | 272,920.00 USD |
| `7D` | `0.9230` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 51,510.00 USD | 66,370.00 USD | 341,030.00 USD |
| `1D` | `0.9250` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 195,300.00 USD | 37,890.00 USD | 123,440.00 USD |
| `7D` | `0.9250` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 52,570.00 USD | 45,710.00 USD | 67,310.00 USD |
| `1D` | `0.9270` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 99,610.00 USD | 64,140.00 USD |
| `7D` | `0.9270` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 209,950.00 USD | 40,600.00 USD | 89,770.00 USD |
| `1D` | `0.9290` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 38,710.00 USD | 21,240.00 USD | 88,550.00 USD |
| `7D` | `0.9290` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 4,480.00 USD | 53,740.00 USD | 0.00 USD |
| `1D` | `0.9310` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 104,570.00 USD | 67,630.00 USD | 39,300.00 USD |
| `7D` | `0.9310` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 177,720.00 USD | 48,210.00 USD | 166,200.00 USD |
| `1D` | `0.9330` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 32,530.00 USD | 39,200.00 USD | 35,380.00 USD |
| `7D` | `0.9330` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 0.00 USD | 76,570.00 USD | 63,160.00 USD |
| `1D` | `0.9350` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 1,360.00 USD | 13,120.00 USD | 3,500.00 USD |
| `7D` | `0.9350` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 53,950.00 USD | 55,880.00 USD | 5,030.00 USD |
| `1D` | `0.9370` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 198,110.00 USD | 85,110.00 USD | 261,310.00 USD |
| `7D` | `0.9370` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 251,760.00 USD | 1,370.00 USD | 41,940.00 USD |
| `1D` | `0.9390` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 171,940.00 USD | 72,880.00 USD | 153,730.00 USD |
| `7D` | `0.9390` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 86,850.00 USD | 36,340.00 USD | 263,360.00 USD |
| `1D` | `0.9410` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 52,890.00 USD | 4,990.00 USD | 55,640.00 USD |
| `7D` | `0.9410` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 123,000.00 USD | 2,780.00 USD | 0.00 USD |
| `1D` | `0.9430` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 702.40 USD | 3,090.00 USD | 17,690.00 USD |
| `7D` | `0.9430` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 66,560.00 USD | 33,660.00 USD |
| `1D` | `0.9450` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 6,770.00 USD | 76,490.00 USD | 234,000.00 USD |
| `7D` | `0.9450` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 3,360.00 USD | 244,270.00 USD | 90,360.00 USD |
| `1D` | `0.9470` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 92,510.00 USD | 52,870.00 USD | 44,530.00 USD |
| `7D` | `0.9470` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `1D` | `0.9490` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 71,990.00 USD | 62,590.00 USD | 58,530.00 USD |
| `7D` | `0.9490` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD |
| `1D` | `0.9510` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 53,450.00 USD | 49,760.00 USD | 175,450.00 USD |
| `7D` | `0.9510` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 2,840.00 USD | 88,970.00 USD | 736,280.00 USD |
| `1D` | `0.9530` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 32,500.00 USD | 26,060.00 USD | 129,250.00 USD |
| `7D` | `0.9530` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD |
| `1D` | `0.9550` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 50,010.00 USD | 82,110.00 USD | 35,430.00 USD |
| `7D` | `0.9550` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 74,980.00 USD | 2,400.00 USD | 60,590.00 USD |
| `1D` | `0.9570` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 8,380.00 USD | 2,420.00 USD | 159.08 USD |
| `7D` | `0.9570` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 463,830.00 USD | 3,460.00 USD | 1,170.00 USD |
| `1D` | `0.9590` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 33,930.00 USD | 53,830.00 USD | 12.64 USD |
| `7D` | `0.9590` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 562,050.00 USD | 1,040.00 USD | 289.76 USD |
| `1D` | `0.9610` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 207,270.00 USD | 108,280.00 USD | 290,310.00 USD |
| `7D` | `0.9610` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 698,570.00 USD | 190,470.00 USD | 476,080.00 USD |
| `1D` | `0.9630` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 322,010.00 USD | 84,410.00 USD | 129,150.00 USD |
| `7D` | `0.9630` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 579,300.00 USD | 301,610.00 USD | 616,480.00 USD |
| `1D` | `0.9650` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 147,390.00 USD | 134,010.00 USD | 82,660.00 USD |
| `7D` | `0.9650` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 857,470.00 USD | 312,610.00 USD | 412,280.00 USD |
| `1D` | `0.9670` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 264,730.00 USD | 114,200.00 USD | 238,840.00 USD |
| `7D` | `0.9670` | 21,080,000.00 USD | 21,080,000.00 USD | 0.00 USD | 889,580.00 USD | 555,340.00 USD | 705,590.00 USD |
| `1D` | `0.9690` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 235,940.00 USD | 95,400.00 USD | 239,460.00 USD |
| `7D` | `0.9690` | 22,530,000.00 USD | 22,530,000.00 USD | 0.00 USD | 596,350.00 USD | 356,560.00 USD | 488,070.00 USD |
| `1D` | `0.9710` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 170,370.00 USD | 69,530.00 USD | 117,140.00 USD |
| `7D` | `0.9710` | 23,620,000.00 USD | 23,620,000.00 USD | 0.00 USD | 645,500.00 USD | 319,140.00 USD | 126,950.00 USD |
| `1D` | `0.9730` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 80,510.00 USD | 64,370.00 USD | 70,750.00 USD |
| `7D` | `0.9730` | 24,410,000.00 USD | 24,410,000.00 USD | 0.00 USD | 456,990.00 USD | 160,420.00 USD | 177,120.00 USD |
| `1D` | `0.9750` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 58,820.00 USD | 45,650.00 USD | 103,300.00 USD |
| `7D` | `0.9750` | 25,130,000.00 USD | 25,130,000.00 USD | 0.00 USD | 203,760.00 USD | 293,590.00 USD | 222,120.00 USD |
| `1D` | `0.9770` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 15,370.00 USD | 8,230.00 USD | 42,340.00 USD |
| `7D` | `0.9770` | 26,170,000.00 USD | 26,170,000.00 USD | 0.00 USD | 329,170.00 USD | 211,000.00 USD | 500,390.00 USD |
| `1D` | `0.9790` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 19,400.00 USD | 33,280.00 USD | 105,760.00 USD |
| `7D` | `0.9790` | 26,910,000.00 USD | 26,910,000.00 USD | 0.00 USD | 411,780.00 USD | 99,560.00 USD | 222,510.00 USD |
| `1D` | `0.9810` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 100,630.00 USD | 45,360.00 USD | 103,220.00 USD |
| `7D` | `0.9810` | 27,420,000.00 USD | 27,420,000.00 USD | 0.00 USD | 264,890.00 USD | 83,040.00 USD | 169,310.00 USD |
| `1D` | `0.9830` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 91,650.00 USD | 38,020.00 USD | 20,170.00 USD |
| `7D` | `0.9830` | 28,000,000.00 USD | 28,000,000.00 USD | 0.00 USD | 262,900.00 USD | 116,030.00 USD | 199,120.00 USD |
| `1D` | `0.9850` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 22,370.00 USD | 48,410.00 USD | 6,000.00 USD |
| `7D` | `0.9850` | 28,410,000.00 USD | 28,410,000.00 USD | 0.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD |
| `1D` | `0.9870` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 56,760.00 USD | 31,400.00 USD | 97,770.00 USD |
| `7D` | `0.9870` | 28,920,000.00 USD | 28,920,000.00 USD | 0.00 USD | 248,980.00 USD | 203,100.00 USD | 58,100.00 USD |
| `1D` | `0.9890` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 100,670.00 USD | 32,930.00 USD | 33,030.00 USD |
| `7D` | `0.9890` | 29,210,000.00 USD | 29,210,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 19,900.00 USD |
| `1D` | `0.9910` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 80,380.00 USD | 30,860.00 USD | 50,940.00 USD |
| `7D` | `0.9910` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD |
| `1D` | `0.9930` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 33,580.00 USD | 16,590.00 USD | 15,190.00 USD |
| `7D` | `0.9930` | 29,950,000.00 USD | 29,950,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 74,270.00 USD |
| `7D` | `0.9950` | 30,270,000.00 USD | 30,270,000.00 USD | 0.00 USD | 48,120.00 USD | 138,500.00 USD | 130,850.00 USD |
| `7D` | `0.9970` | 30,920,000.00 USD | 30,920,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD |
| `7D` | `0.9990` | 31,200,000.00 USD | 31,200,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD |
| `7D` | `1.00` | 31,640,000.00 USD | 31,640,000.00 USD | 0.00 USD | 202,970.00 USD | 57,170.00 USD | 185,430.00 USD |
| `7D` | `1.00` | 32,140,000.00 USD | 32,140,000.00 USD | 0.00 USD | 226,340.00 USD | 61,540.00 USD | 208,880.00 USD |
| `7D` | `1.00` | 32,300,000.00 USD | 32,300,000.00 USD | 0.00 USD | 51,930.00 USD | 39,560.00 USD | 65,670.00 USD |
| `7D` | `1.01` | 32,780,000.00 USD | 32,780,000.00 USD | 0.00 USD | 256,020.00 USD | 15,900.00 USD | 212,150.00 USD |
| `7D` | `1.01` | 33,380,000.00 USD | 33,380,000.00 USD | 0.00 USD | 247,480.00 USD | 105,290.00 USD | 247,940.00 USD |
| `7D` | `1.01` | 34,180,000.00 USD | 34,180,000.00 USD | 0.00 USD | 398,890.00 USD | 134,240.00 USD | 259,740.00 USD |
| `7D` | `1.01` | 34,890,000.00 USD | 34,890,000.00 USD | 0.00 USD | 188,370.00 USD | 177,300.00 USD | 344,360.00 USD |
| `7D` | `1.01` | 35,240,000.00 USD | 35,240,000.00 USD | 0.00 USD | 168,660.00 USD | 59,720.00 USD | 124,520.00 USD |
| `7D` | `1.02` | 36,000,000.00 USD | 36,000,000.00 USD | 0.00 USD | 300,680.00 USD | 97,830.00 USD | 360,110.00 USD |
| `7D` | `1.02` | 36,760,000.00 USD | 36,760,000.00 USD | 0.00 USD | 291,360.00 USD | 74,810.00 USD | 396,430.00 USD |
| `7D` | `1.02` | 37,190,000.00 USD | 37,190,000.00 USD | 0.00 USD | 153,580.00 USD | 41,370.00 USD | 235,320.00 USD |
| `7D` | `1.02` | 37,500,000.00 USD | 37,500,000.00 USD | 0.00 USD | 151,650.00 USD | 60,000.00 USD | 103,070.00 USD |
| `7D` | `1.02` | 37,730,000.00 USD | 37,730,000.00 USD | 0.00 USD | 75,770.00 USD | 54,210.00 USD | 94,770.00 USD |
| `7D` | `1.03` | 37,980,000.00 USD | 37,980,000.00 USD | 0.00 USD | 104,260.00 USD | 35,230.00 USD | 110,730.00 USD |
| `7D` | `1.03` | 38,190,000.00 USD | 38,190,000.00 USD | 0.00 USD | 85,920.00 USD | 56,310.00 USD | 67,150.00 USD |
| `7D` | `1.03` | 38,540,000.00 USD | 38,540,000.00 USD | 0.00 USD | 168,010.00 USD | 58,600.00 USD | 127,380.00 USD |
| `7D` | `1.03` | 38,870,000.00 USD | 38,870,000.00 USD | 0.00 USD | 57,570.00 USD | 103,690.00 USD | 163,030.00 USD |
| `7D` | `1.03` | 39,010,000.00 USD | 39,010,000.00 USD | 0.00 USD | 64,880.00 USD | 13,040.00 USD | 63,310.00 USD |
| `7D` | `1.04` | 39,390,000.00 USD | 39,390,000.00 USD | 0.00 USD | 156,670.00 USD | 38,980.00 USD | 181,310.00 USD |
| `7D` | `1.04` | 39,650,000.00 USD | 39,650,000.00 USD | 0.00 USD | 110,420.00 USD | 18,150.00 USD | 139,200.00 USD |
| `7D` | `1.04` | 39,880,000.00 USD | 39,880,000.00 USD | 0.00 USD | 102,550.00 USD | 52,580.00 USD | 72,600.00 USD |
| `7D` | `1.04` | 39,970,000.00 USD | 39,970,000.00 USD | 0.00 USD | 18,340.00 USD | 48,310.00 USD | 24,740.00 USD |
| `7D` | `1.04` | 40,060,000.00 USD | 40,060,000.00 USD | 0.00 USD | 65,240.00 USD | 17,210.00 USD | 1,410.00 USD |
| `7D` | `1.05` | 40,160,000.00 USD | 40,160,000.00 USD | 0.00 USD | 76,550.00 USD | 30,790.00 USD | 294.86 USD |
| `7D` | `1.05` | 40,240,000.00 USD | 40,240,000.00 USD | 0.00 USD | 35,930.00 USD | 20,630.00 USD | 17,210.00 USD |
| `7D` | `1.05` | 40,260,000.00 USD | 40,260,000.00 USD | 0.00 USD | 22,610.00 USD | 0.00 USD | 538.06 USD |
| `7D` | `1.05` | 40,340,000.00 USD | 40,340,000.00 USD | 0.00 USD | 8,370.00 USD | 46,830.00 USD | 28,430.00 USD |
| `7D` | `1.05` | 40,400,000.00 USD | 40,400,000.00 USD | 0.00 USD | 1,650.00 USD | 9,420.00 USD | 46,120.00 USD |
| `7D` | `1.06` | 40,430,000.00 USD | 40,430,000.00 USD | 0.00 USD | 5,290.00 USD | 2,060.00 USD | 21,150.00 USD |
| `7D` | `1.06` | 40,430,000.00 USD | 40,430,000.00 USD | 0.00 USD | 0.00 USD | 638.17 USD | 0.00 USD |
| `7D` | `1.06` | 40,480,000.00 USD | 40,480,000.00 USD | 0.00 USD | 16,370.00 USD | 3,040.00 USD | 33,060.00 USD |
| `7D` | `1.06` | 40,490,000.00 USD | 40,490,000.00 USD | 0.00 USD | 9,950.00 USD | 0.00 USD | 609.22 USD |
| `7D` | `1.06` | 40,500,000.00 USD | 40,500,000.00 USD | 0.00 USD | 5,370.00 USD | 1,110.00 USD | 0.00 USD |
| `7D` | `1.07` | 40,500,000.00 USD | 40,500,000.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `1.07` | 40,530,000.00 USD | 40,530,000.00 USD | 0.00 USD | 2,410.00 USD | 12,740.00 USD | 17,950.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `563.02M` | Total OI Tokens: `648,789,103.7 SUI`
  * 1h OI Change: `+2.65%` | 4h OI Change: `-4.00%` | 24h OI Change: `-8.14%`
  * Exchange Breakdown: Binance=`102.66M` | Bybit=`75.52M` | OKX=`32.38M` | Hyperliquid=`29.70M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-21.72K` | Last 24h: `-2.19K` | Last 3d: `56.09K` | Last 7d: `151.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0160%` | **USDT OKX** | `-0.0101%` |
| **USDT Bybit** | `-0.0067%` | **USDT KuCoin** | `-0.0104%` |
| **USDT MEXC** | `-0.0160%` | **USDT BingX** | `-0.0047%` |
| **USDT Gate** | `-0.0030%` | **USDT Bitget** | `-0.0064%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `56.55%` | `43.45%` | `1.30` | 7,090,000.00 USD |
| `15M` | `Binance` | `53.49%` | `46.51%` | `1.15` | 2,860,000.00 USD |
| `15M` | `OKX` | `63.51%` | `36.49%` | `1.74` | 840,030.00 USD |
| `15M` | `Bybit` | `56.14%` | `43.86%` | `1.28` | 816,680.00 USD |
| `15M` | `KuCoin` | `74.64%` | `25.36%` | `2.94` | 123,040.00 USD |
| `15M` | `Gate` | `58.12%` | `41.88%` | `1.39` | 330,000.00 USD |
| `15M` | `Bitget` | `52.49%` | `47.51%` | `1.10` | 259,490.00 USD |
| `15M` | `BingX` | `69.13%` | `30.87%` | `2.24` | 282,620.00 USD |
| `15M` | `MEXC` | `56.68%` | `43.32%` | `1.31` | 641,820.00 USD |
| `15M` | `Bitunix` | `75.08%` | `24.92%` | `3.01` | 231,900.00 USD |
| `15M` | `Hyperliquid` | `29.72%` | `70.28%` | `0.42` | 468,240.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.34%` | `43.66%` | `1.29` | 85,870.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 103,240.00 USD |
| `15M` | `HTX` | `70.59%` | `29.41%` | `2.40` | 10,620.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `49.9%` | `50.1%` | `1.00` | 1,360.00 USD |
| `15M` | `Aster` | `99.24%` | `0.76%` | `130.58` | 34,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `62.66%` | `37.34%` | `1.68` | 9,320.00 USD |
| `15M` | `Whale Positions` | `53.49%` | `46.51%` | `1.15` | 2,860,000.00 USD |
| `15M` | `Global Accounts` | `56.55%` | `43.45%` | `1.30` | 7,090,000.00 USD |
| `1H` | `SUI` | `54.17%` | `45.83%` | `1.18` | 31,070,000.00 USD |
| `1H` | `Binance` | `51.97%` | `48.03%` | `1.08` | 12,660,000.00 USD |
| `1H` | `OKX` | `54.42%` | `45.58%` | `1.19` | 4,040,000.00 USD |
| `1H` | `Bybit` | `53.41%` | `46.59%` | `1.15` | 3,650,000.00 USD |
| `1H` | `KuCoin` | `59.39%` | `40.61%` | `1.46` | 362,140.00 USD |
| `1H` | `Gate` | `51.78%` | `48.22%` | `1.07` | 1,240,000.00 USD |
| `1H` | `Bitget` | `47.47%` | `52.53%` | `0.90` | 1,920,000.00 USD |
| `1H` | `BingX` | `50.32%` | `49.68%` | `1.01` | 1,160,000.00 USD |
| `1H` | `MEXC` | `62.65%` | `37.35%` | `1.68` | 2,600,000.00 USD |
| `1H` | `Bitunix` | `55.17%` | `44.83%` | `1.23` | 833,060.00 USD |
| `1H` | `Hyperliquid` | `55.85%` | `44.15%` | `1.27` | 1,290,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.99%` | `50.01%` | `1.00` | 308,220.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `95.91%` | `4.09%` | `23.45` | 635,560.00 USD |
| `1H` | `HTX` | `47.85%` | `52.15%` | `0.92` | 47,530.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `28.71%` | `71.29%` | `0.40` | 146,460.00 USD |
| `1H` | `Aster` | `64.33%` | `35.67%` | `1.80` | 157,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `55.55%` | `44.45%` | `1.25` | 18,790.00 USD |
| `1H` | `Whale Positions` | `51.97%` | `48.03%` | `1.08` | 12,660,000.00 USD |
| `1H` | `Global Accounts` | `54.17%` | `45.83%` | `1.18` | 31,070,000.00 USD |
| `4H` | `SUI` | `44.82%` | `55.18%` | `0.81` | 276,290,000.00 USD |
| `4H` | `Binance` | `45.44%` | `54.56%` | `0.83` | 103,920,000.00 USD |
| `4H` | `OKX` | `48.29%` | `51.71%` | `0.93` | 36,400,000.00 USD |
| `4H` | `Bybit` | `46.58%` | `53.42%` | `0.87` | 39,890,000.00 USD |
| `4H` | `KuCoin` | `44.47%` | `55.53%` | `0.80` | 4,160,000.00 USD |
| `4H` | `Gate` | `40.18%` | `59.82%` | `0.67` | 9,670,000.00 USD |
| `4H` | `Bitget` | `43.27%` | `56.73%` | `0.76` | 20,800,000.00 USD |
| `4H` | `BingX` | `26.81%` | `73.19%` | `0.37` | 9,360,000.00 USD |
| `4H` | `MEXC` | `43.89%` | `56.11%` | `0.78` | 23,120,000.00 USD |
| `4H` | `Bitunix` | `42.17%` | `57.83%` | `0.73` | 8,520,000.00 USD |
| `4H` | `Hyperliquid` | `46.08%` | `53.92%` | `0.85` | 10,010,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `29.46%` | `70.54%` | `0.42` | 2,720,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `57.01%` | `42.99%` | `1.33` | 3,700,000.00 USD |
| `4H` | `HTX` | `47.45%` | `52.55%` | `0.90` | 528,730.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `54.6%` | `45.4%` | `1.20` | 1,640,000.00 USD |
| `4H` | `Aster` | `44.02%` | `55.98%` | `0.79` | 1,430,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `38.68%` | `61.32%` | `0.63` | 426,190.00 USD |
| `4H` | `Whale Positions` | `45.44%` | `54.56%` | `0.83` | 103,920,000.00 USD |
| `4H` | `Global Accounts` | `44.82%` | `55.18%` | `0.81` | 276,290,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.8398` | `0.8438` | `0.8398` | `0.8698` | `0.8266` | 29,390,673.77 USD | 11,130,026.21 USD | 18,260,647.56 USD | -7,130,621.35 USD | `-24.26%` | `1B / 21S` |
| `0:00 UTC` | `0.8400` | `0.8437` | `0.8400` | `0.8527` | `0.8329` | 9,049,851.50 USD | 4,379,148.85 USD | 4,670,702.66 USD | -291,553.81 USD | `-3.22%` | `17B / 14S` |
| `5:00 UTC` | `0.8558` | `0.8528` | `0.8558` | `0.8565` | `0.8462` | 5,948,896.47 USD | 3,550,806.65 USD | 2,398,089.83 USD | 1,152,716.82 USD | `+19.38%` | `16B / 10S` |
| `0:00 UTC` | `0.8621` | `0.8568` | `0.8621` | `0.8638` | `0.8502` | 3,733,291.08 USD | 1,909,433.28 USD | 1,823,857.80 USD | 85,575.47 USD | `+2.29%` | `21B / 15S` |
| `5:00 UTC` | `0.8541` | `0.8569` | `0.8541` | `0.8620` | `0.8529` | 3,325,958.12 USD | 1,568,402.64 USD | 1,757,555.48 USD | -189,152.83 USD | `-5.69%` | `11B / 25S` |
| `0:00 UTC` | `0.8526` | `0.8547` | `0.8526` | `0.8621` | `0.8454` | 4,889,853.32 USD | 2,504,692.46 USD | 2,385,160.86 USD | 119,531.61 USD | `+2.44%` | `30B / 12S` |
| `5:00 UTC` | `0.8554` | `0.8547` | `0.8554` | `0.8589` | `0.8518` | 3,213,767.92 USD | 1,386,293.70 USD | 1,827,474.23 USD | -441,180.53 USD | `-13.73%` | `5B / 12S` |
| `0:00 UTC` | `0.8503` | `0.8533` | `0.8503` | `0.8596` | `0.8482` | 2,970,160.51 USD | 1,607,321.44 USD | 1,362,839.07 USD | 244,482.37 USD | `+8.23%` | `19B / 6S` |
| `5:00 UTC` | `0.8605` | `0.8638` | `0.8605` | `0.8693` | `0.8592` | 3,068,721.14 USD | 1,724,308.92 USD | 1,344,412.22 USD | 379,896.70 USD | `+12.38%` | `24B / 7S` |
| `0:00 UTC` | `0.8684` | `0.8681` | `0.8684` | `0.8708` | `0.8651` | 1,842,956.51 USD | 1,081,942.65 USD | 761,013.86 USD | 320,928.79 USD | `+17.41%` | `10B / 9S` |

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
| `5m` | 65,370.00 USD | 161,490.00 USD | **`ACCUMULATION`** |
| `15m` | 407,060.00 USD | 851,050.00 USD | **`ACCUMULATION`** |
| `30m` | 1,250,000.00 USD | 2,050,000.00 USD | **`ACCUMULATION`** |
| `1h` | 563,040.00 USD | 1,110,000.00 USD | **`ACCUMULATION`** |
| `2h` | 561,430.00 USD | 2,540,000.00 USD | **`ACCUMULATION`** |
| `4h` | -6,170,000.00 USD | -13,120,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,830,000.00 USD | -22,580,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -14,690,000.00 USD | -24,790,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -12,570,000.00 USD | -32,230,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,900,000.00 USD | -28,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -28,160,000.00 USD | -91,650,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -158,120,000.00 USD | -488,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+65.37K` | 15m=`+407.06K` | 1h=`+563.04K` | 24h=`-9.90M`
* Futures Capital Netflows: 5m=`+161.49K` | 15m=`+851.05K` | 1h=`+1.11M` | 24h=`-28.84M`
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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
