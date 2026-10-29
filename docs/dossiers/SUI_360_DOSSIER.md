# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:37:48 IST` (`2026-10-29 18:07:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.9325` | `0.9363` | `0.9318` | `0.9361` | `864,960` | 808,236.25 USD | 201,225.76 USD | `+24.90%` | -8,190,962.13 USD | `+1.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9362` | `0.9372` | `0.9335` | `0.9356` | `1,094,693` | 1,024,081.90 USD | -246,640.91 USD | `-24.08%` | -8,437,603.05 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9356` | `0.9368` | `0.9356` | `0.9368` | `35,879` | 33,584.72 USD | 8,152.19 USD | `+24.27%` | -8,429,450.86 USD | `+0.46` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9439` | `0.9464` | `0.9328` | `0.9342` | `3,683,391` | 3,456,784.57 USD | -882,323.36 USD | `-25.52%` | -7,869,066.50 USD | `-1.50` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9343` | `0.9363` | `0.9282` | `0.9361` | `4,292,420` | 4,003,241.44 USD | -167,829.08 USD | `-4.19%` | -8,036,895.58 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9362` | `0.9372` | `0.9335` | `0.9363` | `1,128,276` | 1,055,516.00 USD | -240,045.42 USD | `-22.74%` | -8,276,941.00 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9539` | `0.9617` | `0.9424` | `0.9474` | `16,224,609` | 15,442,165.70 USD | -1,242,937.53 USD | `-8.05%` | -7,902,962.81 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9475` | `0.9481` | `0.9282` | `0.9361` | `13,061,944` | 12,258,406.01 USD | -1,086,968.70 USD | `-8.87%` | -8,989,931.51 USD | `-0.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9362` | `0.9372` | `0.9335` | `0.9368` | `1,130,572` | 1,057,666.62 USD | -238,488.72 USD | `-22.55%` | -9,228,420.23 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -10,284,836.62 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -8,256,119.70 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9282` | `0.9365` | `30,415,136` | 28,756,374.54 USD | -2,569,664.80 USD | `-8.94%` | -10,825,784.50 USD | `-0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9429` | `0.9465` | `0.8981` | `0.9043` | `62,278,068` | 57,050,963.40 USD | -8,597,484.18 USD | `-15.07%` | -10,264,352.04 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -10,145,601.55 USD | `+0.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -10,284,836.62 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -8,256,119.70 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9282` | `0.9365` | `30,415,136` | 28,756,374.54 USD | -2,569,664.80 USD | `-8.94%` | -10,825,784.50 USD | `-0.23` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.9368` | `266.7000` | 249.84 USD | 87,678.66 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.9369` | `2668.3000` | 2,499.93 USD | 85,173.26 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9369` | `2407.5000` | 2,255.56 USD | 87,428.82 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9370` | `3100.6000` | 2,905.39 USD | 39,261.67 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9370` | `2407.8000` | 2,256.13 USD | 41,517.80 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9370` | `2488.3000` | 2,331.54 USD | 43,849.34 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9370` | `5342.0000` | 5,005.40 USD | 48,854.74 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9370` | `2408.0000` | 2,256.25 USD | 51,110.99 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9370` | `33685.9000` | 31,562.34 USD | 82,673.33 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.9371` | `2136.5000` | 2,002.14 USD | 19,012.56 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9371` | `11451.3000` | 10,731.01 USD | 29,743.57 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.9371` | `3616.8000` | 3,389.27 USD | 33,132.84 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `0.9371` | `2407.8000` | 2,256.30 USD | 35,389.14 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9371` | `1032.1000` | 967.14 USD | 36,356.28 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9372` | `1068.1000` | 1,001.07 USD | 9,592.05 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9372` | `1806.0000` | 1,692.55 USD | 11,284.60 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9372` | `6109.7000` | 5,725.83 USD | 17,010.42 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9373` | `3638.7000` | 3,410.55 USD | 6,333.90 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.9373` | `2408.2000` | 2,257.09 USD | 8,590.98 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `0.9374` | `1067.9000` | 1,001.09 USD | 1,001.09 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.9374` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.94` | `0.00%` | `-` |
| `BID` | `0.9374` | `3118.7000` | 2,923.34 USD | 2,923.34 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `0.9375` | `1059.5000` | 993.33 USD | 2,383.02 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9375` | `414.5000` | 388.59 USD | 1,389.69 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.9376` | `220.8000` | 207.03 USD | 5,161.52 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9376` | `514.2000` | 482.12 USD | 4,954.49 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.9376` | `2114.2000` | 1,982.27 USD | 4,472.37 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.9376` | `114.2000` | 107.07 USD | 2,490.09 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9377` | `2408.0000` | 2,258.08 USD | 18,760.74 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9377` | `1093.6000` | 1,025.49 USD | 16,502.67 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9377` | `5337.9000` | 5,005.40 USD | 15,477.18 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9377` | `3141.0000` | 2,945.28 USD | 10,471.77 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9377` | `2522.2000` | 2,364.97 USD | 7,526.49 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9378` | `500.0000` | 468.92 USD | 41,586.26 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9378` | `2408.0000` | 2,258.27 USD | 41,117.34 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9378` | `447.8000` | 419.95 USD | 38,859.07 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9378` | `2000.0000` | 1,875.60 USD | 38,439.12 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9378` | `17644.2000` | 16,546.55 USD | 36,563.52 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9378` | `1339.6000` | 1,256.22 USD | 20,016.97 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9379` | `5337.0000` | 5,005.47 USD | 49,709.21 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9379` | `3324.0000` | 3,117.48 USD | 44,703.74 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `652` | `0xb83d...6e36` | `SHORT` | 3,573,778.69 USD | `3,817,609.40` | `1.11` | `0.9361` | `33.58` | 644,956.63 USD | `+18.05%` | `3X Cross` |
| `977` | `0xa2ce...3126` | `LONG` | 2,341,584.74 USD | `2,500,010.40` | `0.8597` | `0.9361` | `0.000000` | 192,378.21 USD | `+8.22%` | `10X Cross` |
| `1458` | `0x9946...0852` | `SHORT` | 1,559,172.71 USD | `1,664,573.50` | `1.08` | `0.9361` | `1.54` | 237,146.90 USD | `+15.21%` | `10X Cross` |
| `1772` | `0x9aa5...58af` | `SHORT` | 1,206,524.66 USD | `1,288,168.80` | `1.14` | `0.9361` | `6.56` | 261,168.22 USD | `+21.65%` | `10X Cross` |
| `1861` | `0x9df2...c665` | `SHORT` | 1,123,452.00 USD | `1,200,000.00` | `0.7465` | `0.9361` | `24.31` | -227,599.60 USD | `-20.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 5,006.90 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9297 USD [API] | `2026-10-27 21:45:02` |
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 12,732.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 12.73K USD at 0.9297 USD [API] | `2026-10-27 21:45:02` |
| `ANNOUNCEMENT` | `INFO` | `0.9310` | 7,756.86 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 7.76K USD at 0.9310 USD [API] | `2026-10-27 21:46:21` |
| `ANNOUNCEMENT` | `INFO` | `0.9292` | 10,211.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.21K USD at 0.9292 USD [API] | `2026-10-27 21:53:25` |
| `ANNOUNCEMENT` | `INFO` | `0.9292` | 10,211.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.21K USD at 0.9292 USD [API] | `2026-10-27 21:53:25` |
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 5,807.03 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.81K USD at 0.9297 USD [API] | `2026-10-27 22:04:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 10,217.29 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 10.22K USD at 0.9297 USD [API] | `2026-10-27 22:04:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9275` | 9,715.98 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 9.72K USD at 0.9275 USD [API] | `2026-10-27 22:12:18` |
| `ANNOUNCEMENT` | `INFO` | `0.9276` | 6,289.06 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.29K USD at 0.9276 USD [API] | `2026-10-27 22:27:01` |
| `ANNOUNCEMENT` | `INFO` | `0.9138` | 7,972.82 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 7.97K USD at 0.9138 USD [API] | `2026-10-24 14:16:53` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9706` (Vol: 378,700.00 USD, Dist: `+3.60%`) | Long MP=`0.8887` (Vol: 546,500.00 USD, Dist: `--5.14%`)
  * 48H Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+3.60%`) | Long MP=`0.8887` (Vol: 546,500.00 USD, Dist: `--5.14%`)
  * 3D Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+3.60%`) | Long MP=`0.8887` (Vol: 859,700.00 USD, Dist: `--5.14%`)
  * 7D Horizon: Short MP=`0.9685` (Vol: 565,100.00 USD, Dist: `+3.37%`) | Long MP=`0.8890` (Vol: 1,100,000.00 USD, Dist: `--5.12%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1865` | 1,890.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 4,890.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2005` | 130.20 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 218.31 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 17,830.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 307.45 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 220.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 164.21 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 2,160.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 137.09 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,710.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 2,880.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 687.92 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 28,700.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 354.04 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3345` | 589.39 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3355` | 303.66 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3525` | 61,690.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3695` | 230.94 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3745` | 173.69 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3755` | 6,380.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 26,840.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3835` | 5,200.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3875` | 2,330.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 28,820.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 276.85 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3965` | 1,020.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4005` | 3,950.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4015` | 97,110.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4145` | 458.44 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 467.50 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4365` | 43,480.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4415` | 5,800.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 662.50 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4445` | 573.54 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 16,360.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 3,980.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 702.74 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4565` | 249.71 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 295.78 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 5,220.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4675` | 244.78 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 916.89 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4725` | 5,110.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4795` | 241.72 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 173.65 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 1,050.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,120.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 139.02 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 3,230.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 2,460.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 1,440.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5045` | 837.57 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 258.21 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 2,030.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 1,620.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 1,240.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5205` | 422.33 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5225` | 244.90 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 5,280.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5265` | 347.70 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 122,910.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 9,680.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 264.06 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 417.12 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5365` | 13,140.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 185.44 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 319.98 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 43,580.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5435` | 1,620.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 9,870.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5565` | 3,830.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 8,300.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 609.99 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 195.93 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,760.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 609.95 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 947.90 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 286,930.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 1,010.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,650.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 133,580.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 104.60 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5875` | 969.32 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 7,370.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5955` | 1,590.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 5,540.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 151.97 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 1,110.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,780.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 213.64 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 245.40 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 1,540.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 4,400.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6205` | 7,160.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,070.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6265` | 546.18 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 3,510.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 450.05 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 207.17 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,970.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 2,240.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6395` | 20,710.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 956.01 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 477.63 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 489.83 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 471.21 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 8,080.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 210.50 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 721.59 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 631.12 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 408,650.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 126,530.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 1,580.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 35,690.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 635.76 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 10,930.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 38,240.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 602.30 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 5,280.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 11,130.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 161.22 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 10,560.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,500.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 13,740.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 1,040.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 2,950.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 5,620.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 3,380.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 15,920.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 6,380.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 7,140.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 480.49 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 83,790.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 4,010.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6925` | 17,150.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 4,400.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 560.64 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 1,930.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 759.59 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 1,170.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 769.59 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 787.73 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 3,890.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 2,550.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 3,530.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 718.76 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 156.39 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 62,620.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 8,870.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 1,470.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 11,720.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 742.50 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 129.26 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 2,660.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 1,280.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 762.57 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 214.03 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 302,280.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7315` | 145.42 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 907.93 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 2,520.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 6,900.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 1,400.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 5,590.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 412.05 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 510.15 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 784,090.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 105.64 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 103,310.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7485` | 105.91 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 811.78 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7505` | 1,580.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,340.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 106.03 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 5,480.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 922.07 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7565` | 1,900.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 36,710.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,390.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 1,530.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 604.16 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,850.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 6,290.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 499.14 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7675` | 10,680.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 499.99 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7695` | 147,750.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 842.93 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7715` | 3,190.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,490.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 4,570.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7745` | 184.95 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 7,660.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 4,630.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 544.25 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 6,450.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 444.63 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,630.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7835` | 950.23 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7855` | 3,020.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 44,690.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7875` | 5,400.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7895` | 8,660.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7905` | 4,910.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7915` | 1,290.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 385.87 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7945` | 7,640.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7955` | 3,030.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7975` | 1,170.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7985` | 643.43 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7995` | 2,580.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8005` | 11,670.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8015` | 88,780.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 421.31 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 26,280.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 15,590.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 206.85 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8105` | 5,190.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8110` | 32,660,000.00 USD | 32,660,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,620.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8130` | 32,560,000.00 USD | 32,560,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 11,260.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 32,490,000.00 USD | 32,490,000.00 USD | 135,770.00 USD | 50,280.00 USD | 124,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 8,160.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8165` | 362.12 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8170` | 32,180,000.00 USD | 32,180,000.00 USD | 91,050.00 USD | 23,590.00 USD | 78,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 104,090.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8185` | 773.65 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 31,980,000.00 USD | 31,980,000.00 USD | 195,400.00 USD | 52,010.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 643.31 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 31,690,000.00 USD | 31,690,000.00 USD | 138,580.00 USD | 47,520.00 USD | 119,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 10,310.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8225` | 466.85 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 31,380,000.00 USD | 31,380,000.00 USD | 37,880.00 USD | 24,290.00 USD | 64,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 659.29 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8245` | 3,510.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 31,260,000.00 USD | 31,260,000.00 USD | 187,510.00 USD | 27,530.00 USD | 126,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 30,920,000.00 USD | 30,920,000.00 USD | 144,410.00 USD | 51,050.00 USD | 63,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 27,960.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 118,200.00 USD | 990,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8290` | 30,660,000.00 USD | 30,660,000.00 USD | 89,470.00 USD | 39,850.00 USD | 82,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 32,530.00 USD | 871,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8305` | 1,670.00 USD | 839,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8310` | 30,450,000.00 USD | 30,450,000.00 USD | 34,030.00 USD | 30,800.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8325` | 18,980.00 USD | 837,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8330` | 30,360,000.00 USD | 30,360,000.00 USD | 150,740.00 USD | 85,780.00 USD | 198,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8335` | 686.97 USD | 818,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8340` | 12,990,000.00 USD | 12,990,000.00 USD | 66,840.00 USD | 33,800.00 USD | 80,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 29,920,000.00 USD | 29,920,000.00 USD | 74,030.00 USD | 14,320.00 USD | 83,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 17,770.00 USD | 818,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 12,810,000.00 USD | 12,810,000.00 USD | 54,120.00 USD | 3,830.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 29,750,000.00 USD | 29,750,000.00 USD | 146,890.00 USD | 48,060.00 USD | 102,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 137.85 USD | 800,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 12,730,000.00 USD | 12,730,000.00 USD | 29,520.00 USD | 7,690.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 79,450.00 USD | 800,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8390` | 29,450,000.00 USD | 29,450,000.00 USD | 24,790.00 USD | 51,510.00 USD | 77,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 27,150.00 USD | 720,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 12,660,000.00 USD | 12,660,000.00 USD | 25,130.00 USD | 19,380.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 744.51 USD | 693,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8410` | 29,300,000.00 USD | 29,300,000.00 USD | 55,190.00 USD | 40,110.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 3,890.00 USD | 692,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 12,590,000.00 USD | 12,590,000.00 USD | 12,220.00 USD | 13,260.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 13,400.00 USD | 688,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8430` | 29,180,000.00 USD | 29,180,000.00 USD | 81,850.00 USD | 49,990.00 USD | 30,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 1,340.00 USD | 675,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 12,550,000.00 USD | 12,550,000.00 USD | 23,630.00 USD | 15,080.00 USD | 6,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 893.23 USD | 674,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8450` | 29,010,000.00 USD | 29,010,000.00 USD | 43,800.00 USD | 55,690.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 8,710.00 USD | 673,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 12,510,000.00 USD | 12,510,000.00 USD | 19,430.00 USD | 21,540.00 USD | 47,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 13,750.00 USD | 664,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8470` | 28,870,000.00 USD | 28,870,000.00 USD | 23,930.00 USD | 4,350.00 USD | 32,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 29,810.00 USD | 650,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 12,420,000.00 USD | 12,420,000.00 USD | 32,420.00 USD | 20,130.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,890.00 USD | 621,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8490` | 28,810,000.00 USD | 28,810,000.00 USD | 45,210.00 USD | 16,670.00 USD | 46,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 804.99 USD | 619,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 12,320,000.00 USD | 12,320,000.00 USD | 61,890.00 USD | 7,390.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 28,700,000.00 USD | 28,700,000.00 USD | 95,990.00 USD | 42,650.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 618,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 12,230,000.00 USD | 12,230,000.00 USD | 30,310.00 USD | 27,790.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 4,220.00 USD | 617,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8530` | 28,520,000.00 USD | 28,520,000.00 USD | 30,570.00 USD | 50,890.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 11,410.00 USD | 612,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 12,160,000.00 USD | 12,160,000.00 USD | 20,080.00 USD | 11,230.00 USD | 41,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8545` | 2,030.00 USD | 601,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8550` | 28,410,000.00 USD | 28,410,000.00 USD | 78,320.00 USD | 26,490.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8555` | 139.53 USD | 599,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 12,090,000.00 USD | 12,090,000.00 USD | 27,930.00 USD | 22,280.00 USD | 25,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 36,350.00 USD | 599,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8570` | 28,300,000.00 USD | 28,300,000.00 USD | 99,680.00 USD | 45,070.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 12,010,000.00 USD | 12,010,000.00 USD | 56,290.00 USD | 13,730.00 USD | 14,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 14,660.00 USD | 562,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8590` | 28,150,000.00 USD | 28,150,000.00 USD | 51,400.00 USD | 22,020.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 7,610.00 USD | 548,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 11,930,000.00 USD | 11,930,000.00 USD | 16,950.00 USD | 6,660.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 19,020.00 USD | 540,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8610` | 28,060,000.00 USD | 28,060,000.00 USD | 36,870.00 USD | 71,110.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8615` | 2,080.00 USD | 521,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 11,890,000.00 USD | 11,890,000.00 USD | 6,110.00 USD | 5,870.00 USD | 127.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 9,140.00 USD | 519,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 27,920,000.00 USD | 27,920,000.00 USD | 30,710.00 USD | 13,800.00 USD | 48,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 4,710.00 USD | 510,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 11,870,000.00 USD | 11,870,000.00 USD | 52,440.00 USD | 24,580.00 USD | 60,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 2,580.00 USD | 505,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 27,820,000.00 USD | 27,820,000.00 USD | 235,900.00 USD | 43,890.00 USD | 100,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8655` | 2,210.00 USD | 503,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 11,740,000.00 USD | 11,740,000.00 USD | 137,930.00 USD | 1,740.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,040.00 USD | 500,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 27,440,000.00 USD | 27,440,000.00 USD | 159,120.00 USD | 71,510.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8675` | 11,820.00 USD | 499,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 11,580,000.00 USD | 11,580,000.00 USD | 103,830.00 USD | 61,020.00 USD | 33,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8685` | 289.04 USD | 488,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8690` | 27,150,000.00 USD | 27,150,000.00 USD | 182,190.00 USD | 79,290.00 USD | 194,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 5,030.00 USD | 487,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 11,390,000.00 USD | 11,390,000.00 USD | 110,320.00 USD | 90,530.00 USD | 226,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 14,970.00 USD | 482,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8710` | 26,700,000.00 USD | 26,700,000.00 USD | 604,760.00 USD | 169,010.00 USD | 362,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 2,870.00 USD | 467,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 10,960,000.00 USD | 10,960,000.00 USD | 211,980.00 USD | 63,580.00 USD | 201,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8725` | 29,520.00 USD | 464,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8730` | 25,560,000.00 USD | 25,560,000.00 USD | 333,320.00 USD | 199,340.00 USD | 215,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8735` | 13,270.00 USD | 435,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8740` | 10,480,000.00 USD | 10,480,000.00 USD | 43,750.00 USD | 20,320.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8745` | 15,980.00 USD | 422,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8750` | 24,810,000.00 USD | 24,810,000.00 USD | 643,630.00 USD | 230,460.00 USD | 324,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8755` | 1,420.00 USD | 406,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8760` | 10,400,000.00 USD | 10,400,000.00 USD | 76,420.00 USD | 73,290.00 USD | 141,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 33,510.00 USD | 404,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 23,610,000.00 USD | 23,610,000.00 USD | 399,330.00 USD | 184,560.00 USD | 420,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8775` | 16,030.00 USD | 371,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 10,100,000.00 USD | 10,100,000.00 USD | 64,740.00 USD | 48,670.00 USD | 31,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8785` | 56,160.00 USD | 355,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8790` | 22,610,000.00 USD | 22,610,000.00 USD | 312,210.00 USD | 124,520.00 USD | 221,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 172,470.00 USD | 299,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 9,960,000.00 USD | 9,960,000.00 USD | 13,090.00 USD | 11,350.00 USD | 44,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8805` | 1,530.00 USD | 126,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8810` | 21,950,000.00 USD | 21,950,000.00 USD | 641,660.00 USD | 159,780.00 USD | 487,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8815` | 8,730.00 USD | 125,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8820` | 9,890,000.00 USD | 9,890,000.00 USD | 108,450.00 USD | 63,180.00 USD | 145,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8825` | 5,300.00 USD | 116,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8830` | 20,660,000.00 USD | 20,660,000.00 USD | 783,040.00 USD | 270,900.00 USD | 529,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8835` | 7,220.00 USD | 111,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8840` | 9,570,000.00 USD | 9,570,000.00 USD | 303,250.00 USD | 65,530.00 USD | 151,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 3,550.00 USD | 103,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8850` | 19,080,000.00 USD | 19,080,000.00 USD | 519,370.00 USD | 265,360.00 USD | 259,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8855` | 2,660.00 USD | 100,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8860` | 9,050,000.00 USD | 9,050,000.00 USD | 273,240.00 USD | 127,160.00 USD | 87,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8865` | 28,370.00 USD | 97,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8870` | 18,040,000.00 USD | 18,040,000.00 USD | 649,180.00 USD | 279,830.00 USD | 511,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8875` | 12,780.00 USD | 69,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8880` | 8,570,000.00 USD | 8,570,000.00 USD | 324,630.00 USD | 224,670.00 USD | 540,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8885` | 697.38 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8890` | 16,600,000.00 USD | 16,600,000.00 USD | 1,550,000.00 USD | 530,540.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8895` | 3,530.00 USD | 55,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8900` | 7,480,000.00 USD | 7,480,000.00 USD | 524,630.00 USD | 171,920.00 USD | 548,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8905` | 139.90 USD | 52,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8910` | 13,360,000.00 USD | 13,360,000.00 USD | 818,970.00 USD | 471,140.00 USD | 681,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8915` | 1,100.00 USD | 52,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8920` | 6,230,000.00 USD | 6,230,000.00 USD | 235,610.00 USD | 49,510.00 USD | 114,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 1,040.00 USD | 50,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8930` | 11,390,000.00 USD | 11,390,000.00 USD | 1,790,000.00 USD | 646,070.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8935` | 2,470.00 USD | 49,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8940` | 5,830,000.00 USD | 5,830,000.00 USD | 167,880.00 USD | 130,550.00 USD | 281,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8945` | 5,380.00 USD | 47,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8950` | 7,900,000.00 USD | 7,900,000.00 USD | 771,020.00 USD | 443,450.00 USD | 829,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 5,250,000.00 USD | 5,250,000.00 USD | 149,410.00 USD | 148,110.00 USD | 187,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8965` | 29,550.00 USD | 42,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8970` | 5,860,000.00 USD | 5,860,000.00 USD | 673,010.00 USD | 276,920.00 USD | 492,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8975` | 3,540.00 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8980` | 4,760,000.00 USD | 4,760,000.00 USD | 120,980.00 USD | 57,070.00 USD | 76,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 320.05 USD | 8,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8990` | 4,420,000.00 USD | 4,420,000.00 USD | 322,820.00 USD | 147,390.00 USD | 897.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 143.92 USD | 8,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 4,510,000.00 USD | 4,510,000.00 USD | 53,800.00 USD | 24,210.00 USD | 40,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9005` | 2,600.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9010` | 3,950,000.00 USD | 3,950,000.00 USD | 130,380.00 USD | 15,640.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 4,390,000.00 USD | 4,390,000.00 USD | 49,680.00 USD | 79,010.00 USD | 191,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 3,790,000.00 USD | 3,790,000.00 USD | 5,880.00 USD | 50,720.00 USD | 146,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 4,070,000.00 USD | 4,070,000.00 USD | 128,110.00 USD | 81,940.00 USD | 139,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 3,590,000.00 USD | 3,590,000.00 USD | 122,230.00 USD | 0.00 USD | 46,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 300.72 USD | 8,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 3,720,000.00 USD | 3,720,000.00 USD | 215,300.00 USD | 10,170.00 USD | 58,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 3,420,000.00 USD | 3,420,000.00 USD | 341,080.00 USD | 19,890.00 USD | 127,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9075` | 8,220.00 USD | 8,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9080` | 3,440,000.00 USD | 3,440,000.00 USD | 248,490.00 USD | 116,800.00 USD | 213,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 2,930,000.00 USD | 2,930,000.00 USD | 53,970.00 USD | 0.00 USD | 128,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 2,860,000.00 USD | 2,860,000.00 USD | 174,550.00 USD | 32,520.00 USD | 153,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 2,750,000.00 USD | 2,750,000.00 USD | 212,760.00 USD | 106,160.00 USD | 35,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 2,500,000.00 USD | 2,500,000.00 USD | 211,640.00 USD | 39,820.00 USD | 204,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 2,400,000.00 USD | 2,400,000.00 USD | 80,230.00 USD | 95,530.00 USD | 166,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 2,040,000.00 USD | 2,040,000.00 USD | 172,190.00 USD | 87,890.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 2,050,000.00 USD | 2,050,000.00 USD | 111,690.00 USD | 26,360.00 USD | 38,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 1,670,000.00 USD | 1,670,000.00 USD | 32,680.00 USD | 25,880.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 1,880,000.00 USD | 1,880,000.00 USD | 123,530.00 USD | 0.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 1,610,000.00 USD | 1,610,000.00 USD | 154,870.00 USD | 9,020.00 USD | 46,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 1,720,000.00 USD | 1,720,000.00 USD | 257,890.00 USD | 23,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 1,440,000.00 USD | 1,440,000.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 1,390,000.00 USD | 1,390,000.00 USD | 32,990.00 USD | 39,420.00 USD | 133,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 1,230,000.00 USD | 1,230,000.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 1,180,000.00 USD | 1,180,000.00 USD | 170,280.00 USD | 58,320.00 USD | 150,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 768,980.00 USD | 768,980.00 USD | 52,570.00 USD | 41,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 804,700.00 USD | 804,700.00 USD | 125,460.00 USD | 28,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 674,690.00 USD | 674,690.00 USD | 209,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 650,880.00 USD | 650,880.00 USD | 31,930.00 USD | 80,990.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 464,750.00 USD | 464,750.00 USD | 0.00 USD | 78,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 526,160.00 USD | 526,160.00 USD | 82,700.00 USD | 110,920.00 USD | 166,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9310` | 385,810.00 USD | 385,810.00 USD | 177,720.00 USD | 29,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 165,760.00 USD | 165,760.00 USD | 100,660.00 USD | 0.00 USD | 13,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 51,380.00 USD | 51,380.00 USD | 0.00 USD | 0.00 USD | 51,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 178,920.00 USD | 178,920.00 USD | 50,160.00 USD | 52,710.00 USD | 76,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 152,670.00 USD | 152,670.00 USD | 0.00 USD | 39,480.00 USD | 113,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 293,700.00 USD | 293,700.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 811,120.00 USD | 811,120.00 USD | 246,090.00 USD | 118,850.00 USD | 293,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 673,150.00 USD | 673,150.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 930,660.00 USD | 930,660.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 796,150.00 USD | 796,150.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 858,240.00 USD | 858,240.00 USD | 0.00 USD | 62,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 28,980.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 50.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 35,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 1,270,000.00 USD | 1,270,000.00 USD | 1,330.00 USD | 6,400.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 62,510.00 USD | 700,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 1,410,000.00 USD | 1,410,000.00 USD | 37,450.00 USD | 17,280.00 USD | 86,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 1,470,000.00 USD | 1,470,000.00 USD | 20,720.00 USD | 42,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 2,280,000.00 USD | 2,280,000.00 USD | 71,910.00 USD | 1,290.00 USD | 288.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 33,360.00 USD | 164.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 2,740,000.00 USD | 2,740,000.00 USD | 463,830.00 USD | 2,240.00 USD | 511.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 1,550,000.00 USD | 1,550,000.00 USD | 689.00 USD | 43,140.00 USD | 59.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 3,310,000.00 USD | 3,310,000.00 USD | 562,050.00 USD | 1,040.00 USD | 289.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 1,840,000.00 USD | 1,840,000.00 USD | 110,240.00 USD | 65,470.00 USD | 108,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 4,660,000.00 USD | 4,660,000.00 USD | 698,570.00 USD | 176,650.00 USD | 476,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 2,730,000.00 USD | 2,730,000.00 USD | 410,030.00 USD | 135,810.00 USD | 345,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 6,180,000.00 USD | 6,180,000.00 USD | 604,860.00 USD | 301,610.00 USD | 615,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 3,450,000.00 USD | 3,450,000.00 USD | 347,170.00 USD | 124,900.00 USD | 253,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 7,750,000.00 USD | 7,750,000.00 USD | 857,470.00 USD | 301,210.00 USD | 412,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 4,000,000.00 USD | 4,000,000.00 USD | 273,420.00 USD | 130,220.00 USD | 142,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 9,860,000.00 USD | 9,860,000.00 USD | 916,920.00 USD | 487,590.00 USD | 705,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9680` | 4,790,000.00 USD | 4,790,000.00 USD | 302,380.00 USD | 118,860.00 USD | 365,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 11,220,000.00 USD | 11,220,000.00 USD | 596,350.00 USD | 343,680.00 USD | 420,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 5,400,000.00 USD | 5,400,000.00 USD | 265,560.00 USD | 150,830.00 USD | 200,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 70,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9710` | 12,320,000.00 USD | 12,320,000.00 USD | 645,500.00 USD | 305,860.00 USD | 144,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 5,940,000.00 USD | 5,940,000.00 USD | 326,660.00 USD | 114,070.00 USD | 99,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 13,080,000.00 USD | 13,080,000.00 USD | 456,990.00 USD | 160,420.00 USD | 146,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 6,200,000.00 USD | 6,200,000.00 USD | 167,080.00 USD | 34,110.00 USD | 52,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 13,770,000.00 USD | 13,770,000.00 USD | 201,510.00 USD | 293,590.00 USD | 193,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 6,370,000.00 USD | 6,370,000.00 USD | 40,320.00 USD | 41,480.00 USD | 88,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9765` | 214.44 USD | 71,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9770` | 14,810,000.00 USD | 14,810,000.00 USD | 329,170.00 USD | 211,000.00 USD | 499,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 6,720,000.00 USD | 6,720,000.00 USD | 110,140.00 USD | 55,790.00 USD | 189,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 15,490,000.00 USD | 15,490,000.00 USD | 409,890.00 USD | 84,800.00 USD | 186,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 7,060,000.00 USD | 7,060,000.00 USD | 102,630.00 USD | 72,440.00 USD | 157,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 15,580.00 USD | 86,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 16,010,000.00 USD | 16,010,000.00 USD | 264,890.00 USD | 83,040.00 USD | 169,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 7,330,000.00 USD | 7,330,000.00 USD | 185,860.00 USD | 32,830.00 USD | 53,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 16,570,000.00 USD | 16,570,000.00 USD | 260,850.00 USD | 99,420.00 USD | 199,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 7,500,000.00 USD | 7,500,000.00 USD | 80,920.00 USD | 67,090.00 USD | 28,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9845` | 10,440.00 USD | 97,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9850` | 16,980,000.00 USD | 16,980,000.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 7,840,000.00 USD | 7,840,000.00 USD | 131,110.00 USD | 61,330.00 USD | 139,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 17,480,000.00 USD | 17,480,000.00 USD | 248,980.00 USD | 191,820.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 54,920.00 USD | 151,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 8,030,000.00 USD | 8,030,000.00 USD | 85,110.00 USD | 34,550.00 USD | 71,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 13,550.00 USD | 165,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9890` | 17,770,000.00 USD | 17,770,000.00 USD | 194,850.00 USD | 78,280.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9895` | 5,760.00 USD | 171,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9900` | 8,300,000.00 USD | 8,300,000.00 USD | 144,770.00 USD | 50,410.00 USD | 79,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 20,050.00 USD | 191,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9910` | 18,140,000.00 USD | 18,140,000.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 8,510,000.00 USD | 8,510,000.00 USD | 143,390.00 USD | 46,290.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,290.00 USD | 193,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 18,510,000.00 USD | 18,510,000.00 USD | 228,340.00 USD | 63,950.00 USD | 73,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 8,670,000.00 USD | 8,670,000.00 USD | 60,500.00 USD | 36,520.00 USD | 58,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9945` | 6,430.00 USD | 200,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9950` | 18,820,000.00 USD | 18,820,000.00 USD | 48,120.00 USD | 138,500.00 USD | 130,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 8,710,000.00 USD | 8,710,000.00 USD | 6,800.00 USD | 11,390.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9965` | 5,440.00 USD | 205,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9970` | 19,470,000.00 USD | 19,470,000.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 9,020,000.00 USD | 9,020,000.00 USD | 140,230.00 USD | 32,300.00 USD | 142,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 19,750,000.00 USD | 19,750,000.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,070,000.00 USD | 9,070,000.00 USD | 19,510.00 USD | 17,530.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 20,200,000.00 USD | 20,200,000.00 USD | 202,970.00 USD | 57,170.00 USD | 185,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,120,000.00 USD | 9,120,000.00 USD | 12,840.00 USD | 18,430.00 USD | 20,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 20,780,000.00 USD | 20,780,000.00 USD | 316,600.00 USD | 52,200.00 USD | 216,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,170,000.00 USD | 9,170,000.00 USD | 17,620.00 USD | 13,280.00 USD | 22,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 449.11 USD | 205,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 20,980,000.00 USD | 20,980,000.00 USD | 96,930.00 USD | 29,470.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,210,000.00 USD | 9,210,000.00 USD | 9,900.00 USD | 14,230.00 USD | 11,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 21,490,000.00 USD | 21,490,000.00 USD | 283,350.00 USD | 15,900.00 USD | 212,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,250,000.00 USD | 9,250,000.00 USD | 19,520.00 USD | 9,720.00 USD | 12,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 22,090,000.00 USD | 22,090,000.00 USD | 247,480.00 USD | 105,290.00 USD | 247,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,280,000.00 USD | 9,280,000.00 USD | 13,150.00 USD | 5,570.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 23,040,000.00 USD | 23,040,000.00 USD | 457,740.00 USD | 174,650.00 USD | 319,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,350,000.00 USD | 9,350,000.00 USD | 21,660.00 USD | 13,820.00 USD | 34,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 117,860.00 USD | 323,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 24,010,000.00 USD | 24,010,000.00 USD | 342,220.00 USD | 281,430.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,400,000.00 USD | 9,400,000.00 USD | 13,360.00 USD | 11,680.00 USD | 26,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 24,550,000.00 USD | 24,550,000.00 USD | 325,510.00 USD | 91,280.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 323,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,450,000.00 USD | 9,450,000.00 USD | 23,240.00 USD | 15,330.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 25,390,000.00 USD | 25,390,000.00 USD | 383,690.00 USD | 97,830.00 USD | 360,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,490,000.00 USD | 9,490,000.00 USD | 23,270.00 USD | 3,970.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 26,250,000.00 USD | 26,250,000.00 USD | 303,920.00 USD | 88,570.00 USD | 469,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,600,000.00 USD | 9,600,000.00 USD | 36,260.00 USD | 16,330.00 USD | 56,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 26,740,000.00 USD | 26,740,000.00 USD | 167,390.00 USD | 63,770.00 USD | 260,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,680,000.00 USD | 9,680,000.00 USD | 55,590.00 USD | 4,130.00 USD | 22,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 27,100,000.00 USD | 27,100,000.00 USD | 185,100.00 USD | 50,190.00 USD | 123,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,740,000.00 USD | 9,740,000.00 USD | 29,960.00 USD | 7,690.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 27,360,000.00 USD | 27,360,000.00 USD | 112,970.00 USD | 54,210.00 USD | 94,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,810,000.00 USD | 9,810,000.00 USD | 23,940.00 USD | 16,440.00 USD | 22,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 27,620,000.00 USD | 27,620,000.00 USD | 106,360.00 USD | 35,230.00 USD | 110,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,820,000.00 USD | 9,820,000.00 USD | 6,330.00 USD | 0.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 8,840.00 USD | 332,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.03` | 27,830,000.00 USD | 27,830,000.00 USD | 87,950.00 USD | 57,010.00 USD | 67,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,840,000.00 USD | 9,840,000.00 USD | 4,130.00 USD | 10,320.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 28,260,000.00 USD | 28,260,000.00 USD | 198,340.00 USD | 79,470.00 USD | 157,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,880,000.00 USD | 9,880,000.00 USD | 21,900.00 USD | 11,130.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 28,710,000.00 USD | 28,710,000.00 USD | 136,400.00 USD | 149,600.00 USD | 163,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,960,000.00 USD | 9,960,000.00 USD | 16,600.00 USD | 19,650.00 USD | 47,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 28,900,000.00 USD | 28,900,000.00 USD | 113,490.00 USD | 13,040.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,060,000.00 USD | 10,060,000.00 USD | 26,990.00 USD | 18,830.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,300,000.00 USD | 29,300,000.00 USD | 176,930.00 USD | 41,220.00 USD | 181,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,140,000.00 USD | 10,140,000.00 USD | 59,260.00 USD | 7,020.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,610,000.00 USD | 29,610,000.00 USD | 114,060.00 USD | 21,690.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 10,400.00 USD | 343,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,170,000.00 USD | 10,170,000.00 USD | 8,210.00 USD | 7,840.00 USD | 8,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 343,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,850,000.00 USD | 29,850,000.00 USD | 105,050.00 USD | 55,100.00 USD | 72,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,210,000.00 USD | 10,210,000.00 USD | 21,580.00 USD | 18,300.00 USD | 6,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,940,000.00 USD | 29,940,000.00 USD | 20,680.00 USD | 49,420.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,280,000.00 USD | 10,280,000.00 USD | 19,660.00 USD | 8,720.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 30,030,000.00 USD | 30,030,000.00 USD | 69,360.00 USD | 17,730.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 10,350,000.00 USD | 10,350,000.00 USD | 25,330.00 USD | 17,080.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,140,000.00 USD | 30,140,000.00 USD | 79,950.00 USD | 31,290.00 USD | 294.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 10,430,000.00 USD | 10,430,000.00 USD | 53,350.00 USD | 10,090.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,210,000.00 USD | 30,210,000.00 USD | 38,030.00 USD | 13,720.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 10,440,000.00 USD | 10,440,000.00 USD | 12,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 343,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,240,000.00 USD | 30,240,000.00 USD | 23,320.00 USD | 0.00 USD | 538.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 346,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 142.30 USD | 14,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,330.00 USD | 347,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,320,000.00 USD | 30,320,000.00 USD | 8,370.00 USD | 47,690.00 USD | 28,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 348,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 10,460,000.00 USD | 10,460,000.00 USD | 303.15 USD | 202.65 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 217.44 USD | 348,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,370,000.00 USD | 30,370,000.00 USD | 3,770.00 USD | 5,360.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 10,480,000.00 USD | 10,480,000.00 USD | 11,980.00 USD | 4,220.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,390,000.00 USD | 30,390,000.00 USD | 6,580.00 USD | 3,950.00 USD | 197.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,390,000.00 USD | 30,390,000.00 USD | 1,110.00 USD | 194.87 USD | 59.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,420,000.00 USD | 30,420,000.00 USD | 17,530.00 USD | 3,870.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,430,000.00 USD | 30,430,000.00 USD | 10,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 112.62 USD | 348,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.07` | 1,310.00 USD | 349,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 1,150.00 USD | 350,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 12,800.00 USD | 363,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 367,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 166.43 USD | 367,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 1,110.00 USD | 368,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 374,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 374,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 374,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 397,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.16` | 268,350.00 USD | 666,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 1,450.00 USD | 667,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 253.69 USD | 667,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 9,150.00 USD | 677,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 29,760.00 USD | 706,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 147.43 USD | 707,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 711,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 711,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 5,310.00 USD | 717,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 137.21 USD | 717,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 719,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 759,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 760,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 760,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 761,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 792,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 2,170.00 USD | 794,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 801,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 823,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 253.40 USD | 823,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 358.30 USD | 823,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,520.00 USD | 825,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 832,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.36` | 142.87 USD | 832,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 1,170.00 USD | 833,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.38` | 171,940.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 139.20 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 4,740.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 1,200.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 9,430.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 2,480,000.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 24,510.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 120.29 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 9,650.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 291.72 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 281,210.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 18,320.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 9,340.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 39,260.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 84,600.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 238.30 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 112.65 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 18,400.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 238.64 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 781.77 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 952.52 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 2,480.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 14,230.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 203.88 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 943.75 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 190.35 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 149.36 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 2,010.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1865` | 5,410,000.00 USD | 0.00 USD | 6,010.00 USD | `-80.08%` | `32,244.50` |
| `Live` | `Long` | `0.1945` | 5,400,000.00 USD | 0.00 USD | 1,970.00 USD | `-79.23%` | `10,152.10` |
| `Live` | `Long` | `0.1995` | 5,400,000.00 USD | 0.00 USD | 256.00 USD | `-78.70%` | `1,283.20` |
| `Live` | `Long` | `0.2135` | 5,400,000.00 USD | 0.00 USD | 138.65 USD | `-77.20%` | `649.40` |
| `Live` | `Long` | `0.2355` | 5,400,000.00 USD | 0.00 USD | 789.66 USD | `-74.85%` | `3,353.10` |
| `Live` | `Long` | `0.2365` | 5,400,000.00 USD | 0.00 USD | 307.45 USD | `-74.75%` | `1,300.00` |
| `Live` | `Long` | `0.2385` | 5,400,000.00 USD | 0.00 USD | 156.36 USD | `-74.53%` | `655.60` |
| `Live` | `Long` | `0.2515` | 5,400,000.00 USD | 0.00 USD | 264.60 USD | `-73.14%` | `1,052.10` |
| `Live` | `Long` | `0.2525` | 5,400,000.00 USD | 0.00 USD | 21,870.00 USD | `-73.04%` | `86,603.40` |
| `Live` | `Long` | `0.2575` | 5,380,000.00 USD | 0.00 USD | 557.56 USD | `-72.50%` | `2,165.30` |
| `Live` | `Long` | `0.2685` | 5,380,000.00 USD | 0.00 USD | 106.16 USD | `-71.33%` | `395.40` |
| `Live` | `Long` | `0.2725` | 5,380,000.00 USD | 0.00 USD | 1,910.00 USD | `-70.90%` | `7,000.00` |
| `Live` | `Long` | `0.2735` | 5,380,000.00 USD | 0.00 USD | 248.34 USD | `-70.79%` | `908.00` |
| `Live` | `Long` | `0.2815` | 5,380,000.00 USD | 0.00 USD | 238.66 USD | `-69.94%` | `847.80` |
| `Live` | `Long` | `0.2885` | 5,380,000.00 USD | 0.00 USD | 29,070.00 USD | `-69.19%` | `100,768.40` |
| `Live` | `Long` | `0.2895` | 5,350,000.00 USD | 0.00 USD | 7,470.00 USD | `-69.09%` | `25,791.20` |
| `Live` | `Long` | `0.2945` | 5,340,000.00 USD | 0.00 USD | 687.92 USD | `-68.55%` | `2,335.90` |
| `Live` | `Long` | `0.2965` | 5,340,000.00 USD | 0.00 USD | 7,100.00 USD | `-68.34%` | `23,938.30` |
| `Live` | `Long` | `0.2975` | 5,330,000.00 USD | 0.00 USD | 7,310.00 USD | `-68.23%` | `24,561.30` |
| `Live` | `Long` | `0.3115` | 5,320,000.00 USD | 0.00 USD | 270.38 USD | `-66.74%` | `868.00` |
| `Live` | `Long` | `0.3185` | 5,320,000.00 USD | 0.00 USD | 3,140.00 USD | `-65.99%` | `9,865.70` |
| `Live` | `Long` | `0.3205` | 5,320,000.00 USD | 0.00 USD | 157.21 USD | `-65.78%` | `490.50` |
| `Live` | `Long` | `0.3395` | 5,320,000.00 USD | 0.00 USD | 378.58 USD | `-63.75%` | `1,115.10` |
| `Live` | `Long` | `0.3485` | 5,320,000.00 USD | 0.00 USD | 2,000.00 USD | `-62.79%` | `5,733.30` |
| `Live` | `Long` | `0.3505` | 5,320,000.00 USD | 0.00 USD | 1,640.00 USD | `-62.57%` | `4,670.00` |
| `Live` | `Long` | `0.3585` | 5,320,000.00 USD | 0.00 USD | 595.72 USD | `-61.72%` | `1,661.70` |
| `Live` | `Long` | `0.3645` | 5,320,000.00 USD | 0.00 USD | 227.81 USD | `-61.08%` | `625.00` |
| `Live` | `Long` | `0.3665` | 5,320,000.00 USD | 0.00 USD | 274.88 USD | `-60.86%` | `750.00` |
| `Live` | `Long` | `0.3765` | 5,310,000.00 USD | 0.00 USD | 6,630.00 USD | `-59.80%` | `17,618.50` |
| `Live` | `Long` | `0.3795` | 5,310,000.00 USD | 0.00 USD | 278.02 USD | `-59.48%` | `732.60` |
| `Live` | `Long` | `0.3825` | 5,310,000.00 USD | 0.00 USD | 26,770.00 USD | `-59.16%` | `70,000.00` |
| `Live` | `Long` | `0.3845` | 5,280,000.00 USD | 0.00 USD | 1,750.00 USD | `-58.94%` | `4,562.20` |
| `Live` | `Long` | `0.3895` | 5,280,000.00 USD | 0.00 USD | 2,980.00 USD | `-58.41%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 5,280,000.00 USD | 0.00 USD | 5,030.00 USD | `-58.09%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 5,270,000.00 USD | 0.00 USD | 357.06 USD | `-57.87%` | `905.10` |
| `Live` | `Long` | `0.3995` | 5,270,000.00 USD | 0.00 USD | 69,910.00 USD | `-57.34%` | `175,000.00` |
| `Live` | `Long` | `0.4015` | 5,200,000.00 USD | 0.00 USD | 281.05 USD | `-57.13%` | `700.00` |
| `Live` | `Long` | `0.4035` | 5,200,000.00 USD | 0.00 USD | 935.03 USD | `-56.91%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 5,200,000.00 USD | 0.00 USD | 5,520.00 USD | `-56.81%` | `13,640.50` |
| `Live` | `Long` | `0.4195` | 5,190,000.00 USD | 0.00 USD | 102.86 USD | `-55.20%` | `245.20` |
| `Live` | `Long` | `0.4235` | 5,190,000.00 USD | 0.00 USD | 467.50 USD | `-54.78%` | `1,103.90` |
| `Live` | `Long` | `0.4245` | 5,190,000.00 USD | 0.00 USD | 1,290.00 USD | `-54.67%` | `3,043.40` |
| `Live` | `Long` | `0.4295` | 5,190,000.00 USD | 0.00 USD | 475.03 USD | `-54.14%` | `1,106.00` |
| `Live` | `Long` | `0.4315` | 5,190,000.00 USD | 0.00 USD | 1,120.00 USD | `-53.92%` | `2,584.80` |
| `Live` | `Long` | `0.4365` | 5,190,000.00 USD | 0.00 USD | 43,480.00 USD | `-53.39%` | `99,611.70` |
| `Live` | `Long` | `0.4385` | 5,150,000.00 USD | 0.00 USD | 6,070.00 USD | `-53.18%` | `13,832.30` |
| `Live` | `Long` | `0.4415` | 5,140,000.00 USD | 0.00 USD | 5,800.00 USD | `-52.86%` | `13,146.20` |
| `Live` | `Long` | `0.4435` | 5,140,000.00 USD | 0.00 USD | 219.00 USD | `-52.64%` | `493.80` |
| `Live` | `Long` | `0.4445` | 5,140,000.00 USD | 0.00 USD | 573.54 USD | `-52.54%` | `1,290.30` |
| `Live` | `Long` | `0.4455` | 5,130,000.00 USD | 0.00 USD | 16,360.00 USD | `-52.43%` | `36,725.40` |
| `Live` | `Long` | `0.4465` | 5,120,000.00 USD | 0.00 USD | 3,210.00 USD | `-52.32%` | `7,180.60` |
| `Live` | `Long` | `0.4535` | 5,120,000.00 USD | 0.00 USD | 702.74 USD | `-51.57%` | `1,549.60` |
| `Live` | `Long` | `0.4595` | 5,110,000.00 USD | 0.00 USD | 295.78 USD | `-50.93%` | `643.70` |
| `Live` | `Long` | `0.4605` | 5,110,000.00 USD | 0.00 USD | 899.31 USD | `-50.83%` | `1,952.90` |
| `Live` | `Long` | `0.4715` | 5,110,000.00 USD | 0.00 USD | 5,320.00 USD | `-49.65%` | `11,290.30` |
| `Live` | `Long` | `0.4725` | 5,110,000.00 USD | 0.00 USD | 472.50 USD | `-49.55%` | `1,000.00` |
| `Live` | `Long` | `0.4755` | 5,110,000.00 USD | 0.00 USD | 33,280.00 USD | `-49.22%` | `70,000.00` |
| `Live` | `Long` | `0.4785` | 5,070,000.00 USD | 0.00 USD | 110.10 USD | `-48.90%` | `230.10` |
| `Live` | `Long` | `0.4815` | 5,070,000.00 USD | 0.00 USD | 252.11 USD | `-48.58%` | `523.60` |
| `Live` | `Long` | `0.4835` | 5,070,000.00 USD | 0.00 USD | 174.01 USD | `-48.37%` | `359.90` |
| `Live` | `Long` | `0.4865` | 5,070,000.00 USD | 0.00 USD | 201.07 USD | `-48.05%` | `413.30` |
| `Live` | `Long` | `0.4885` | 5,070,000.00 USD | 0.00 USD | 6,330.00 USD | `-47.84%` | `12,957.10` |
| `Live` | `Long` | `0.4895` | 5,070,000.00 USD | 0.00 USD | 373.10 USD | `-47.73%` | `762.20` |
| `Live` | `Long` | `0.4915` | 5,070,000.00 USD | 0.00 USD | 2,380.00 USD | `-47.52%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 5,060,000.00 USD | 0.00 USD | 106.32 USD | `-47.20%` | `215.00` |
| `Live` | `Long` | `0.4955` | 5,060,000.00 USD | 0.00 USD | 3,120.00 USD | `-47.09%` | `6,305.00` |
| `Live` | `Long` | `0.4985` | 5,060,000.00 USD | 0.00 USD | 216.75 USD | `-46.77%` | `434.80` |
| `Live` | `Long` | `0.5015` | 5,060,000.00 USD | 0.00 USD | 212.49 USD | `-46.45%` | `423.70` |
| `Live` | `Long` | `0.5025` | 5,060,000.00 USD | 0.00 USD | 1,230.00 USD | `-46.34%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 5,060,000.00 USD | 0.00 USD | 211.25 USD | `-46.02%` | `417.90` |
| `Live` | `Long` | `0.5065` | 5,060,000.00 USD | 0.00 USD | 258.21 USD | `-45.91%` | `509.80` |
| `Live` | `Long` | `0.5075` | 5,060,000.00 USD | 0.00 USD | 842.55 USD | `-45.81%` | `1,660.20` |
| `Live` | `Long` | `0.5085` | 5,060,000.00 USD | 0.00 USD | 2,030.00 USD | `-45.70%` | `4,000.00` |
| `Live` | `Long` | `0.5095` | 5,060,000.00 USD | 0.00 USD | 2,490.00 USD | `-45.59%` | `4,884.20` |
| `Live` | `Long` | `0.5125` | 5,050,000.00 USD | 0.00 USD | 5,330.00 USD | `-45.27%` | `10,405.20` |
| `Live` | `Long` | `0.5155` | 5,050,000.00 USD | 0.00 USD | 1,240.00 USD | `-44.95%` | `2,409.50` |
| `Live` | `Long` | `0.5165` | 5,050,000.00 USD | 0.00 USD | 619.80 USD | `-44.85%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 5,050,000.00 USD | 0.00 USD | 213.68 USD | `-44.74%` | `412.90` |
| `Live` | `Long` | `0.5185` | 5,050,000.00 USD | 0.00 USD | 121.74 USD | `-44.63%` | `234.80` |
| `Live` | `Long` | `0.5205` | 5,050,000.00 USD | 0.00 USD | 422.33 USD | `-44.42%` | `811.40` |
| `Live` | `Long` | `0.5225` | 5,050,000.00 USD | 0.00 USD | 244.90 USD | `-44.21%` | `468.70` |
| `Live` | `Long` | `0.5245` | 5,050,000.00 USD | 0.00 USD | 5,280.00 USD | `-43.99%` | `10,075.20` |
| `Live` | `Long` | `0.5265` | 5,040,000.00 USD | 0.00 USD | 347.70 USD | `-43.78%` | `660.40` |
| `Live` | `Long` | `0.5285` | 5,040,000.00 USD | 0.00 USD | 125,730.00 USD | `-43.57%` | `237,897.40` |
| `Live` | `Long` | `0.5295` | 4,910,000.00 USD | 0.00 USD | 264.06 USD | `-43.46%` | `498.70` |
| `Live` | `Long` | `0.5325` | 4,910,000.00 USD | 0.00 USD | 2,680.00 USD | `-43.14%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,910,000.00 USD | 0.00 USD | 417.12 USD | `-42.92%` | `780.40` |
| `Live` | `Long` | `0.5375` | 4,910,000.00 USD | 0.00 USD | 1,190.00 USD | `-42.60%` | `2,206.50` |
| `Live` | `Long` | `0.5385` | 4,910,000.00 USD | 0.00 USD | 5,850.00 USD | `-42.50%` | `10,862.70` |
| `Live` | `Long` | `0.5395` | 4,900,000.00 USD | 0.00 USD | 319.98 USD | `-42.39%` | `593.10` |
| `Live` | `Long` | `0.5405` | 4,900,000.00 USD | 0.00 USD | 7,090.00 USD | `-42.28%` | `13,118.90` |
| `Live` | `Long` | `0.5415` | 4,900,000.00 USD | 0.00 USD | 1,390.00 USD | `-42.18%` | `2,559.80` |
| `Live` | `Long` | `0.5425` | 4,890,000.00 USD | 0.00 USD | 269.13 USD | `-42.07%` | `496.10` |
| `Live` | `Long` | `0.5435` | 4,890,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.96%` | `2,984.20` |
| `Live` | `Long` | `0.5445` | 4,890,000.00 USD | 0.00 USD | 230.32 USD | `-41.86%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,890,000.00 USD | 0.00 USD | 272.87 USD | `-41.64%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,890,000.00 USD | 0.00 USD | 1,240.00 USD | `-41.54%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,890,000.00 USD | 0.00 USD | 28,790.00 USD | `-41.32%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,860,000.00 USD | 0.00 USD | 248.06 USD | `-41.22%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,860,000.00 USD | 0.00 USD | 160.93 USD | `-41.11%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,860,000.00 USD | 0.00 USD | 582.56 USD | `-41.00%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,860,000.00 USD | 0.00 USD | 271.88 USD | `-40.90%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,860,000.00 USD | 0.00 USD | 531.60 USD | `-40.79%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,860,000.00 USD | 0.00 USD | 16,060.00 USD | `-40.68%` | `28,914.00` |
| `Live` | `Long` | `0.5585` | 4,840,000.00 USD | 0.00 USD | 141.97 USD | `-40.36%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,840,000.00 USD | 0.00 USD | 304.93 USD | `-40.25%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,840,000.00 USD | 0.00 USD | 441.84 USD | `-40.15%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,840,000.00 USD | 0.00 USD | 330.53 USD | `-39.93%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,840,000.00 USD | 0.00 USD | 195.93 USD | `-39.83%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,840,000.00 USD | 0.00 USD | 8,190.00 USD | `-39.61%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,840,000.00 USD | 0.00 USD | 570.01 USD | `-39.51%` | `1,006.20` |
| `Live` | `Long` | `0.5675` | 4,830,000.00 USD | 0.00 USD | 1,560.00 USD | `-39.40%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,830,000.00 USD | 0.00 USD | 973.22 USD | `-39.19%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,830,000.00 USD | 0.00 USD | 139.23 USD | `-38.87%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,830,000.00 USD | 0.00 USD | 182.72 USD | `-38.76%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,830,000.00 USD | 0.00 USD | 144.03 USD | `-38.65%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,830,000.00 USD | 0.00 USD | 1,010.00 USD | `-38.55%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,830,000.00 USD | 0.00 USD | 1,150.00 USD | `-38.44%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,830,000.00 USD | 0.00 USD | 497.75 USD | `-38.33%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,830,000.00 USD | 0.00 USD | 1,240.00 USD | `-38.23%` | `2,136.70` |
| `Live` | `Long` | `0.5795` | 4,830,000.00 USD | 0.00 USD | 278.45 USD | `-38.12%` | `480.50` |
| `Live` | `Long` | `0.5805` | 4,830,000.00 USD | 0.00 USD | 1,410.00 USD | `-38.01%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,830,000.00 USD | 0.00 USD | 6,470.00 USD | `-37.80%` | `11,099.00` |
| `Live` | `Long` | `0.5835` | 4,820,000.00 USD | 0.00 USD | 11,670.00 USD | `-37.69%` | `20,000.00` |
| `Live` | `Long` | `0.5855` | 4,810,000.00 USD | 0.00 USD | 2,640.00 USD | `-37.48%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,810,000.00 USD | 0.00 USD | 135,670.00 USD | `-37.37%` | `231,317.60` |
| `Live` | `Long` | `0.5875` | 4,670,000.00 USD | 0.00 USD | 58,220.00 USD | `-37.27%` | `99,093.90` |
| `Live` | `Long` | `0.5885` | 4,610,000.00 USD | 0.00 USD | 311.14 USD | `-37.16%` | `528.70` |
| `Live` | `Long` | `0.5925` | 4,610,000.00 USD | 0.00 USD | 297,240.00 USD | `-36.73%` | `501,677.90` |
| `Live` | `Long` | `0.5935` | 4,310,000.00 USD | 0.00 USD | 132.41 USD | `-36.62%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,310,000.00 USD | 0.00 USD | 8,220.00 USD | `-36.52%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,310,000.00 USD | 0.00 USD | 5,540.00 USD | `-36.30%` | `9,295.80` |
| `Live` | `Long` | `0.5995` | 4,300,000.00 USD | 0.00 USD | 151.97 USD | `-35.98%` | `253.50` |
| `Live` | `Long` | `0.6005` | 4,300,000.00 USD | 0.00 USD | 351.11 USD | `-35.88%` | `584.70` |
| `Live` | `Long` | `0.6025` | 4,300,000.00 USD | 0.00 USD | 432.35 USD | `-35.66%` | `717.60` |
| `Live` | `Long` | `0.6075` | 4,300,000.00 USD | 0.00 USD | 851.05 USD | `-35.13%` | `1,400.90` |
| `Live` | `Long` | `0.6095` | 4,300,000.00 USD | 0.00 USD | 1,390.00 USD | `-34.92%` | `2,280.00` |
| `Live` | `Long` | `0.6115` | 4,300,000.00 USD | 0.00 USD | 6,780.00 USD | `-34.70%` | `11,093.80` |
| `Live` | `Long` | `0.6125` | 4,290,000.00 USD | 0.00 USD | 213.64 USD | `-34.60%` | `348.80` |
| `Live` | `Long` | `0.6135` | 4,290,000.00 USD | 0.00 USD | 245.40 USD | `-34.49%` | `400.00` |
| `Live` | `Long` | `0.6155` | 4,290,000.00 USD | 0.00 USD | 935.13 USD | `-34.28%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 4,290,000.00 USD | 0.00 USD | 29,900.00 USD | `-34.17%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 4,260,000.00 USD | 0.00 USD | 2,670.00 USD | `-34.06%` | `4,327.00` |
| `Live` | `Long` | `0.6185` | 4,260,000.00 USD | 0.00 USD | 4,400.00 USD | `-33.95%` | `7,107.00` |
| `Live` | `Long` | `0.6245` | 4,250,000.00 USD | 0.00 USD | 356.65 USD | `-33.31%` | `571.10` |
| `Live` | `Long` | `0.6255` | 4,250,000.00 USD | 0.00 USD | 39,890.00 USD | `-33.21%` | `63,765.70` |
| `Live` | `Long` | `0.6265` | 4,210,000.00 USD | 0.00 USD | 546.18 USD | `-33.10%` | `871.80` |
| `Live` | `Long` | `0.6285` | 4,210,000.00 USD | 0.00 USD | 102.45 USD | `-32.89%` | `163.00` |
| `Live` | `Long` | `0.6305` | 4,210,000.00 USD | 0.00 USD | 319.35 USD | `-32.67%` | `506.50` |
| `Live` | `Long` | `0.6315` | 4,210,000.00 USD | 0.00 USD | 3,510.00 USD | `-32.57%` | `5,564.80` |
| `Live` | `Long` | `0.6345` | 4,210,000.00 USD | 0.00 USD | 450.05 USD | `-32.25%` | `709.30` |
| `Live` | `Long` | `0.6355` | 4,210,000.00 USD | 0.00 USD | 207.17 USD | `-32.14%` | `326.00` |
| `Live` | `Long` | `0.6365` | 4,210,000.00 USD | 0.00 USD | 2,850.00 USD | `-32.03%` | `4,478.70` |
| `Live` | `Long` | `0.6375` | 4,200,000.00 USD | 0.00 USD | 2,240.00 USD | `-31.93%` | `3,513.60` |
| `Live` | `Long` | `0.6385` | 4,200,000.00 USD | 0.00 USD | 1,120.00 USD | `-31.82%` | `1,761.60` |
| `Live` | `Long` | `0.6395` | 4,200,000.00 USD | 0.00 USD | 2,270.00 USD | `-31.71%` | `3,541.90` |
| `Live` | `Long` | `0.6405` | 4,200,000.00 USD | 0.00 USD | 939.17 USD | `-31.61%` | `1,466.30` |
| `Live` | `Long` | `0.6415` | 4,200,000.00 USD | 0.00 USD | 86,920.00 USD | `-31.50%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 4,110,000.00 USD | 0.00 USD | 7,900.00 USD | `-31.39%` | `12,289.30` |
| `Live` | `Long` | `0.6435` | 4,100,000.00 USD | 0.00 USD | 489.83 USD | `-31.29%` | `761.20` |
| `Live` | `Long` | `0.6445` | 4,100,000.00 USD | 0.00 USD | 65,790.00 USD | `-31.18%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 4,040,000.00 USD | 0.00 USD | 471.21 USD | `-31.07%` | `730.00` |
| `Live` | `Long` | `0.6475` | 4,040,000.00 USD | 0.00 USD | 8,080.00 USD | `-30.86%` | `12,473.20` |
| `Live` | `Long` | `0.6485` | 4,030,000.00 USD | 0.00 USD | 210.50 USD | `-30.75%` | `324.60` |
| `Live` | `Long` | `0.6495` | 4,030,000.00 USD | 0.00 USD | 721.59 USD | `-30.64%` | `1,111.00` |
| `Live` | `Long` | `0.6505` | 4,030,000.00 USD | 0.00 USD | 631.12 USD | `-30.54%` | `970.20` |
| `Live` | `Long` | `0.6515` | 4,030,000.00 USD | 0.00 USD | 408,650.00 USD | `-30.43%` | `627,245.30` |
| `Live` | `Long` | `0.6535` | 3,620,000.00 USD | 0.00 USD | 126,530.00 USD | `-30.22%` | `193,618.10` |
| `Live` | `Long` | `0.6555` | 3,490,000.00 USD | 0.00 USD | 1,580.00 USD | `-30.00%` | `2,403.40` |
| `Live` | `Long` | `0.6565` | 3,490,000.00 USD | 0.00 USD | 7,070.00 USD | `-29.90%` | `10,764.20` |
| `Live` | `Long` | `0.6575` | 3,480,000.00 USD | 0.00 USD | 13,280.00 USD | `-29.79%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,470,000.00 USD | 0.00 USD | 2,970.00 USD | `-29.68%` | `4,508.30` |
| `Live` | `Long` | `0.6615` | 3,470,000.00 USD | 0.00 USD | 10,930.00 USD | `-29.36%` | `16,517.10` |
| `Live` | `Long` | `0.6625` | 3,450,000.00 USD | 0.00 USD | 2,820.00 USD | `-29.26%` | `4,259.20` |
| `Live` | `Long` | `0.6645` | 3,450,000.00 USD | 0.00 USD | 602.30 USD | `-29.04%` | `906.40` |
| `Live` | `Long` | `0.6675` | 3,450,000.00 USD | 0.00 USD | 5,280.00 USD | `-28.72%` | `7,907.60` |
| `Live` | `Long` | `0.6685` | 3,450,000.00 USD | 0.00 USD | 2,810.00 USD | `-28.62%` | `4,203.00` |
| `Live` | `Long` | `0.6695` | 3,440,000.00 USD | 0.00 USD | 161.22 USD | `-28.51%` | `240.80` |
| `Live` | `Long` | `0.6705` | 3,440,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.40%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,440,000.00 USD | 0.00 USD | 37,780.00 USD | `-28.30%` | `56,262.60` |
| `Live` | `Long` | `0.6725` | 3,400,000.00 USD | 0.00 USD | 1,500.00 USD | `-28.19%` | `2,227.70` |
| `Live` | `Long` | `0.6735` | 3,400,000.00 USD | 0.00 USD | 633.09 USD | `-28.08%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,400,000.00 USD | 0.00 USD | 6,520.00 USD | `-27.97%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 3,390,000.00 USD | 0.00 USD | 111.59 USD | `-27.87%` | `165.20` |
| `Live` | `Long` | `0.6765` | 3,390,000.00 USD | 0.00 USD | 5,100.00 USD | `-27.76%` | `7,539.20` |
| `Live` | `Long` | `0.6785` | 3,390,000.00 USD | 0.00 USD | 2,950.00 USD | `-27.55%` | `4,351.40` |
| `Live` | `Long` | `0.6795` | 3,390,000.00 USD | 0.00 USD | 5,620.00 USD | `-27.44%` | `8,270.70` |
| `Live` | `Long` | `0.6805` | 3,380,000.00 USD | 0.00 USD | 9,020.00 USD | `-27.33%` | `13,248.00` |
| `Live` | `Long` | `0.6815` | 3,370,000.00 USD | 0.00 USD | 3,380.00 USD | `-27.23%` | `4,954.70` |
| `Live` | `Long` | `0.6825` | 3,370,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.12%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 3,350,000.00 USD | 0.00 USD | 7,040.00 USD | `-27.01%` | `10,294.10` |
| `Live` | `Long` | `0.6845` | 3,340,000.00 USD | 0.00 USD | 5,790.00 USD | `-26.91%` | `8,455.80` |
| `Live` | `Long` | `0.6875` | 3,340,000.00 USD | 0.00 USD | 480.49 USD | `-26.59%` | `698.90` |
| `Live` | `Long` | `0.6885` | 3,340,000.00 USD | 0.00 USD | 83,790.00 USD | `-26.48%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 3,250,000.00 USD | 0.00 USD | 2,110.00 USD | `-26.37%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 3,250,000.00 USD | 0.00 USD | 3,360.00 USD | `-26.27%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 3,250,000.00 USD | 0.00 USD | 8,970.00 USD | `-26.16%` | `12,967.20` |
| `Live` | `Long` | `0.6925` | 3,240,000.00 USD | 0.00 USD | 17,150.00 USD | `-26.05%` | `24,770.70` |
| `Live` | `Long` | `0.6935` | 3,220,000.00 USD | 0.00 USD | 2,980.00 USD | `-25.95%` | `4,299.80` |
| `Live` | `Long` | `0.6965` | 3,220,000.00 USD | 0.00 USD | 273.03 USD | `-25.63%` | `392.00` |
| `Live` | `Long` | `0.6975` | 3,220,000.00 USD | 0.00 USD | 102.25 USD | `-25.52%` | `146.60` |
| `Live` | `Long` | `0.6985` | 3,220,000.00 USD | 0.00 USD | 11,290.00 USD | `-25.41%` | `16,162.40` |
| `Live` | `Long` | `0.7005` | 3,210,000.00 USD | 0.00 USD | 1,390.00 USD | `-25.20%` | `1,977.40` |
| `Live` | `Long` | `0.7045` | 3,210,000.00 USD | 0.00 USD | 759.59 USD | `-24.77%` | `1,078.20` |
| `Live` | `Long` | `0.7065` | 3,210,000.00 USD | 0.00 USD | 769.59 USD | `-24.56%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 3,210,000.00 USD | 0.00 USD | 787.73 USD | `-24.45%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 3,200,000.00 USD | 0.00 USD | 3,890.00 USD | `-24.34%` | `5,484.60` |
| `Live` | `Long` | `0.7095` | 3,200,000.00 USD | 0.00 USD | 2,550.00 USD | `-24.24%` | `3,589.20` |
| `Live` | `Long` | `0.7105` | 3,200,000.00 USD | 0.00 USD | 3,530.00 USD | `-24.13%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 3,190,000.00 USD | 0.00 USD | 569.20 USD | `-24.02%` | `800.00` |
| `Live` | `Long` | `0.7125` | 3,190,000.00 USD | 0.00 USD | 156.39 USD | `-23.92%` | `219.50` |
| `Live` | `Long` | `0.7145` | 3,190,000.00 USD | 0.00 USD | 22,830.00 USD | `-23.70%` | `31,949.70` |
| `Live` | `Long` | `0.7155` | 3,170,000.00 USD | 0.00 USD | 150.40 USD | `-23.60%` | `210.20` |
| `Live` | `Long` | `0.7175` | 3,170,000.00 USD | 0.00 USD | 1,470.00 USD | `-23.38%` | `2,050.00` |
| `Live` | `Long` | `0.7195` | 3,170,000.00 USD | 0.00 USD | 11,720.00 USD | `-23.17%` | `16,293.90` |
| `Live` | `Long` | `0.7225` | 3,160,000.00 USD | 0.00 USD | 5,110.00 USD | `-22.85%` | `7,066.90` |
| `Live` | `Long` | `0.7255` | 3,150,000.00 USD | 0.00 USD | 5,150.00 USD | `-22.53%` | `7,103.20` |
| `Live` | `Long` | `0.7265` | 3,150,000.00 USD | 0.00 USD | 1,280.00 USD | `-22.42%` | `1,755.10` |
| `Live` | `Long` | `0.7275` | 3,150,000.00 USD | 0.00 USD | 762.57 USD | `-22.32%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 3,150,000.00 USD | 0.00 USD | 214.03 USD | `-22.21%` | `293.80` |
| `Live` | `Long` | `0.7295` | 3,150,000.00 USD | 0.00 USD | 375.98 USD | `-22.10%` | `515.40` |
| `Live` | `Long` | `0.7305` | 3,150,000.00 USD | 0.00 USD | 119.88 USD | `-22.00%` | `164.10` |
| `Live` | `Long` | `0.7325` | 3,150,000.00 USD | 0.00 USD | 907.93 USD | `-21.78%` | `1,239.50` |
| `Live` | `Long` | `0.7345` | 3,140,000.00 USD | 0.00 USD | 2,340.00 USD | `-21.57%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 3,140,000.00 USD | 0.00 USD | 51,920.00 USD | `-21.46%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 3,090,000.00 USD | 0.00 USD | 311,430.00 USD | `-21.35%` | `422,854.90` |
| `Live` | `Long` | `0.7385` | 2,780,000.00 USD | 0.00 USD | 46,940.00 USD | `-21.14%` | `63,563.60` |
| `Live` | `Long` | `0.7395` | 2,730,000.00 USD | 0.00 USD | 147.01 USD | `-21.03%` | `198.80` |
| `Live` | `Long` | `0.7405` | 2,730,000.00 USD | 0.00 USD | 3,530.00 USD | `-20.93%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,730,000.00 USD | 0.00 USD | 1,110.00 USD | `-20.82%` | `1,494.10` |
| `Live` | `Long` | `0.7425` | 2,730,000.00 USD | 0.00 USD | 784,090.00 USD | `-20.71%` | `1,056,015.30` |
| `Live` | `Long` | `0.7445` | 1,940,000.00 USD | 0.00 USD | 1,630.00 USD | `-20.50%` | `2,184.30` |
| `Live` | `Long` | `0.7475` | 1,940,000.00 USD | 0.00 USD | 103,310.00 USD | `-20.18%` | `138,200.90` |
| `Live` | `Long` | `0.7485` | 1,840,000.00 USD | 0.00 USD | 105.91 USD | `-20.07%` | `141.50` |
| `Live` | `Long` | `0.7495` | 1,840,000.00 USD | 0.00 USD | 811.78 USD | `-19.97%` | `1,083.10` |
| `Live` | `Long` | `0.7505` | 1,840,000.00 USD | 0.00 USD | 437.47 USD | `-19.86%` | `582.90` |
| `Live` | `Long` | `0.7515` | 1,840,000.00 USD | 0.00 USD | 1,340.00 USD | `-19.75%` | `1,779.90` |
| `Live` | `Long` | `0.7525` | 1,840,000.00 USD | 0.00 USD | 106.03 USD | `-19.65%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,830,000.00 USD | 0.00 USD | 1,200.00 USD | `-19.54%` | `1,588.10` |
| `Live` | `Long` | `0.7545` | 1,830,000.00 USD | 0.00 USD | 922.07 USD | `-19.43%` | `1,222.10` |
| `Live` | `Long` | `0.7555` | 1,830,000.00 USD | 0.00 USD | 2,210.00 USD | `-19.33%` | `2,928.00` |
| `Live` | `Long` | `0.7565` | 1,830,000.00 USD | 0.00 USD | 1,900.00 USD | `-19.22%` | `2,514.80` |
| `Live` | `Long` | `0.7575` | 1,830,000.00 USD | 0.00 USD | 1,590.00 USD | `-19.11%` | `2,098.80` |
| `Live` | `Long` | `0.7585` | 1,830,000.00 USD | 0.00 USD | 36,710.00 USD | `-19.01%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,790,000.00 USD | 0.00 USD | 4,390.00 USD | `-18.90%` | `5,776.10` |
| `Live` | `Long` | `0.7615` | 1,790,000.00 USD | 0.00 USD | 351.43 USD | `-18.68%` | `461.50` |
| `Live` | `Long` | `0.7635` | 1,790,000.00 USD | 0.00 USD | 604.16 USD | `-18.47%` | `791.30` |
| `Live` | `Long` | `0.7645` | 1,790,000.00 USD | 0.00 USD | 1,060.00 USD | `-18.36%` | `1,384.30` |
| `Live` | `Long` | `0.7655` | 1,780,000.00 USD | 0.00 USD | 6,290.00 USD | `-18.26%` | `8,212.10` |
| `Live` | `Long` | `0.7665` | 1,780,000.00 USD | 0.00 USD | 4,860.00 USD | `-18.15%` | `6,337.40` |
| `Live` | `Long` | `0.7675` | 1,770,000.00 USD | 0.00 USD | 10,680.00 USD | `-18.04%` | `13,912.80` |
| `Live` | `Long` | `0.7685` | 1,760,000.00 USD | 0.00 USD | 499.99 USD | `-17.94%` | `650.60` |
| `Live` | `Long` | `0.7695` | 1,760,000.00 USD | 0.00 USD | 144,250.00 USD | `-17.83%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 1,620,000.00 USD | 0.00 USD | 4,350.00 USD | `-17.72%` | `5,644.90` |
| `Live` | `Long` | `0.7715` | 1,610,000.00 USD | 0.00 USD | 3,190.00 USD | `-17.62%` | `4,137.70` |
| `Live` | `Long` | `0.7725` | 1,610,000.00 USD | 0.00 USD | 1,490.00 USD | `-17.51%` | `1,922.50` |
| `Live` | `Long` | `0.7735` | 1,610,000.00 USD | 0.00 USD | 4,570.00 USD | `-17.40%` | `5,912.10` |
| `Live` | `Long` | `0.7745` | 1,600,000.00 USD | 0.00 USD | 24,410.00 USD | `-17.30%` | `31,516.40` |
| `Live` | `Long` | `0.7755` | 1,580,000.00 USD | 0.00 USD | 126.41 USD | `-17.19%` | `163.00` |
| `Live` | `Long` | `0.7765` | 1,580,000.00 USD | 0.00 USD | 4,630.00 USD | `-17.08%` | `5,964.40` |
| `Live` | `Long` | `0.7775` | 1,570,000.00 USD | 0.00 USD | 544.25 USD | `-16.98%` | `700.00` |
| `Live` | `Long` | `0.7785` | 1,570,000.00 USD | 0.00 USD | 6,450.00 USD | `-16.87%` | `8,285.30` |
| `Live` | `Long` | `0.7795` | 1,570,000.00 USD | 0.00 USD | 444.63 USD | `-16.76%` | `570.40` |
| `Live` | `Long` | `0.7815` | 1,570,000.00 USD | 0.00 USD | 4,630.00 USD | `-16.55%` | `5,918.40` |
| `Live` | `Long` | `0.7835` | 1,560,000.00 USD | 0.00 USD | 950.23 USD | `-16.34%` | `1,212.80` |
| `Live` | `Long` | `0.7855` | 1,560,000.00 USD | 0.00 USD | 3,020.00 USD | `-16.12%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 1,560,000.00 USD | 0.00 USD | 4,460.00 USD | `-16.02%` | `5,665.20` |
| `Live` | `Long` | `0.7875` | 1,550,000.00 USD | 0.00 USD | 6,210.00 USD | `-15.91%` | `7,888.00` |
| `Live` | `Long` | `0.7895` | 1,550,000.00 USD | 0.00 USD | 8,660.00 USD | `-15.69%` | `10,969.90` |
| `Live` | `Long` | `0.7905` | 1,540,000.00 USD | 0.00 USD | 3,850.00 USD | `-15.59%` | `4,876.20` |
| `Live` | `Long` | `0.7915` | 1,540,000.00 USD | 0.00 USD | 1,290.00 USD | `-15.48%` | `1,623.50` |
| `Live` | `Long` | `0.7925` | 1,530,000.00 USD | 0.00 USD | 8,090.00 USD | `-15.37%` | `10,206.60` |
| `Live` | `Long` | `0.7935` | 1,530,000.00 USD | 0.00 USD | 2,220.00 USD | `-15.27%` | `2,799.50` |
| `Live` | `Long` | `0.7945` | 1,520,000.00 USD | 0.00 USD | 9,230.00 USD | `-15.16%` | `11,619.00` |
| `Live` | `Long` | `0.7955` | 1,510,000.00 USD | 0.00 USD | 23,610.00 USD | `-15.05%` | `29,676.80` |
| `Live` | `Long` | `0.7965` | 1,490,000.00 USD | 0.00 USD | 42,350.00 USD | `-14.95%` | `53,170.80` |
| `Live` | `Long` | `0.7975` | 1,450,000.00 USD | 0.00 USD | 1,170.00 USD | `-14.84%` | `1,464.30` |
| `Live` | `Long` | `0.7985` | 1,450,000.00 USD | 0.00 USD | 643.43 USD | `-14.73%` | `805.80` |
| `Live` | `Long` | `0.7995` | 1,450,000.00 USD | 0.00 USD | 2,580.00 USD | `-14.63%` | `3,228.10` |
| `Live` | `Long` | `0.8005` | 1,440,000.00 USD | 0.00 USD | 1,150.00 USD | `-14.52%` | `1,432.40` |
| `Live` | `Long` | `0.8015` | 1,440,000.00 USD | 0.00 USD | 86,410.00 USD | `-14.41%` | `107,816.10` |
| `Live` | `Long` | `0.8025` | 1,360,000.00 USD | 0.00 USD | 421.31 USD | `-14.31%` | `525.00` |
| `Live` | `Long` | `0.8035` | 1,360,000.00 USD | 0.00 USD | 26,280.00 USD | `-14.20%` | `32,702.50` |
| `Live` | `Long` | `0.8045` | 1,330,000.00 USD | 0.00 USD | 15,590.00 USD | `-14.09%` | `19,380.70` |
| `Live` | `Long` | `0.8085` | 1,310,000.00 USD | 0.00 USD | 22,170.00 USD | `-13.67%` | `27,427.20` |
| `Live` | `Long` | `0.8105` | 1,290,000.00 USD | 0.00 USD | 5,190.00 USD | `-13.45%` | `6,403.40` |
| `Live` | `Long` | `0.8115` | 1,290,000.00 USD | 0.00 USD | 2,620.00 USD | `-13.35%` | `3,234.70` |
| `Live` | `Long` | `0.8135` | 1,280,000.00 USD | 0.00 USD | 11,260.00 USD | `-13.13%` | `13,843.50` |
| `Live` | `Long` | `0.8155` | 1,270,000.00 USD | 0.00 USD | 8,360.00 USD | `-12.92%` | `10,256.80` |
| `Live` | `Long` | `0.8165` | 1,260,000.00 USD | 0.00 USD | 362.12 USD | `-12.81%` | `443.50` |
| `Live` | `Long` | `0.8175` | 1,260,000.00 USD | 0.00 USD | 103,660.00 USD | `-12.71%` | `126,800.10` |
| `Live` | `Long` | `0.8185` | 1,160,000.00 USD | 0.00 USD | 491.10 USD | `-12.60%` | `600.00` |
| `Live` | `Long` | `0.8195` | 1,160,000.00 USD | 0.00 USD | 999.13 USD | `-12.49%` | `1,219.20` |
| `Live` | `Long` | `0.8205` | 1,160,000.00 USD | 0.00 USD | 2,280.00 USD | `-12.38%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 1,160,000.00 USD | 0.00 USD | 5,180.00 USD | `-12.28%` | `6,300.50` |
| `Live` | `Long` | `0.8225` | 1,150,000.00 USD | 0.00 USD | 466.85 USD | `-12.17%` | `567.60` |
| `Live` | `Long` | `0.8235` | 1,150,000.00 USD | 0.00 USD | 11,490.00 USD | `-12.06%` | `13,949.90` |
| `Live` | `Long` | `0.8245` | 1,140,000.00 USD | 0.00 USD | 3,190.00 USD | `-11.96%` | `3,871.50` |
| `Live` | `Long` | `0.8255` | 1,140,000.00 USD | 0.00 USD | 317.82 USD | `-11.85%` | `385.00` |
| `Live` | `Long` | `0.8275` | 1,140,000.00 USD | 0.00 USD | 11,410.00 USD | `-11.64%` | `13,785.20` |
| `Live` | `Long` | `0.8285` | 1,120,000.00 USD | 0.00 USD | 118,200.00 USD | `-11.53%` | `142,661.50` |
| `Live` | `Long` | `0.8295` | 1,010,000.00 USD | 0.00 USD | 32,530.00 USD | `-11.42%` | `39,217.20` |
| `Live` | `Long` | `0.8305` | 974,240.00 USD | 0.00 USD | 1,670.00 USD | `-11.32%` | `2,011.70` |
| `Live` | `Long` | `0.8325` | 972,570.00 USD | 0.00 USD | 18,980.00 USD | `-11.10%` | `22,795.90` |
| `Live` | `Long` | `0.8345` | 953,590.00 USD | 0.00 USD | 687.79 USD | `-10.89%` | `824.20` |
| `Live` | `Long` | `0.8355` | 952,900.00 USD | 0.00 USD | 17,890.00 USD | `-10.78%` | `21,407.70` |
| `Live` | `Long` | `0.8375` | 935,010.00 USD | 0.00 USD | 137.85 USD | `-10.57%` | `164.60` |
| `Live` | `Long` | `0.8385` | 934,880.00 USD | 0.00 USD | 79,450.00 USD | `-10.46%` | `94,750.80` |
| `Live` | `Long` | `0.8395` | 855,430.00 USD | 0.00 USD | 27,150.00 USD | `-10.36%` | `32,340.20` |
| `Live` | `Long` | `0.8405` | 828,280.00 USD | 0.00 USD | 1,380.00 USD | `-10.25%` | `1,647.50` |
| `Live` | `Long` | `0.8415` | 826,890.00 USD | 0.00 USD | 2,200.00 USD | `-10.14%` | `2,616.80` |
| `Live` | `Long` | `0.8425` | 824,690.00 USD | 0.00 USD | 25,310.00 USD | `-10.04%` | `30,043.20` |
| `Live` | `Long` | `0.8435` | 799,380.00 USD | 0.00 USD | 6,280.00 USD | `-9.93%` | `7,446.40` |
| `Live` | `Long` | `0.8445` | 793,100.00 USD | 0.00 USD | 133.18 USD | `-9.82%` | `157.70` |
| `Live` | `Long` | `0.8455` | 792,970.00 USD | 0.00 USD | 6,630.00 USD | `-9.72%` | `7,840.60` |
| `Live` | `Long` | `0.8465` | 786,340.00 USD | 0.00 USD | 15,830.00 USD | `-9.61%` | `18,696.70` |
| `Live` | `Long` | `0.8475` | 770,510.00 USD | 0.00 USD | 29,810.00 USD | `-9.50%` | `35,169.30` |
| `Live` | `Long` | `0.8485` | 740,700.00 USD | 0.00 USD | 1,890.00 USD | `-9.39%` | `2,222.00` |
| `Live` | `Long` | `0.8495` | 738,820.00 USD | 0.00 USD | 804.99 USD | `-9.29%` | `947.60` |
| `Live` | `Long` | `0.8515` | 738,010.00 USD | 0.00 USD | 1,220.00 USD | `-9.07%` | `1,433.90` |
| `Live` | `Long` | `0.8525` | 736,790.00 USD | 0.00 USD | 4,220.00 USD | `-8.97%` | `4,952.40` |
| `Live` | `Long` | `0.8535` | 732,570.00 USD | 0.00 USD | 11,410.00 USD | `-8.86%` | `13,374.00` |
| `Live` | `Long` | `0.8545` | 721,160.00 USD | 0.00 USD | 2,030.00 USD | `-8.75%` | `2,375.90` |
| `Live` | `Long` | `0.8555` | 719,130.00 USD | 0.00 USD | 139.53 USD | `-8.65%` | `163.10` |
| `Live` | `Long` | `0.8565` | 718,990.00 USD | 0.00 USD | 36,350.00 USD | `-8.54%` | `42,440.00` |
| `Live` | `Long` | `0.8585` | 682,640.00 USD | 0.00 USD | 14,660.00 USD | `-8.33%` | `17,077.30` |
| `Live` | `Long` | `0.8595` | 667,980.00 USD | 0.00 USD | 7,610.00 USD | `-8.22%` | `8,848.50` |
| `Live` | `Long` | `0.8605` | 660,370.00 USD | 0.00 USD | 19,020.00 USD | `-8.11%` | `22,098.50` |
| `Live` | `Long` | `0.8615` | 641,350.00 USD | 0.00 USD | 1,090.00 USD | `-8.01%` | `1,265.90` |
| `Live` | `Long` | `0.8625` | 640,260.00 USD | 0.00 USD | 9,140.00 USD | `-7.90%` | `10,602.70` |
| `Live` | `Long` | `0.8635` | 631,120.00 USD | 0.00 USD | 5,160.00 USD | `-7.79%` | `5,974.70` |
| `Live` | `Long` | `0.8645` | 625,960.00 USD | 0.00 USD | 2,580.00 USD | `-7.69%` | `2,988.60` |
| `Live` | `Long` | `0.8655` | 623,380.00 USD | 0.00 USD | 1,230.00 USD | `-7.58%` | `1,426.30` |
| `Live` | `Long` | `0.8665` | 622,140.00 USD | 0.00 USD | 1,040.00 USD | `-7.47%` | `1,205.70` |
| `Live` | `Long` | `0.8675` | 621,100.00 USD | 0.00 USD | 13,120.00 USD | `-7.37%` | `15,120.10` |
| `Live` | `Long` | `0.8685` | 607,980.00 USD | 0.00 USD | 289.04 USD | `-7.26%` | `332.80` |
| `Live` | `Long` | `0.8695` | 607,690.00 USD | 0.00 USD | 4,920.00 USD | `-7.15%` | `5,663.60` |
| `Live` | `Long` | `0.8705` | 602,770.00 USD | 0.00 USD | 14,520.00 USD | `-7.05%` | `16,678.90` |
| `Live` | `Long` | `0.8715` | 588,250.00 USD | 0.00 USD | 2,870.00 USD | `-6.94%` | `3,293.40` |
| `Live` | `Long` | `0.8725` | 585,380.00 USD | 0.00 USD | 29,520.00 USD | `-6.83%` | `33,829.20` |
| `Live` | `Long` | `0.8735` | 555,860.00 USD | 0.00 USD | 129,080.00 USD | `-6.73%` | `147,768.00` |
| `Live` | `Long` | `0.8745` | 426,790.00 USD | 0.00 USD | 13,880.00 USD | `-6.62%` | `15,872.80` |
| `Live` | `Long` | `0.8755` | 412,910.00 USD | 0.00 USD | 1,420.00 USD | `-6.51%` | `1,624.00` |
| `Live` | `Long` | `0.8765` | 411,480.00 USD | 0.00 USD | 33,510.00 USD | `-6.40%` | `38,226.70` |
| `Live` | `Long` | `0.8775` | 377,980.00 USD | 0.00 USD | 16,030.00 USD | `-6.30%` | `18,270.50` |
| `Live` | `Long` | `0.8785` | 361,950.00 USD | 0.00 USD | 56,160.00 USD | `-6.19%` | `63,924.50` |
| `Live` | `Long` | `0.8795` | 305,790.00 USD | 0.00 USD | 172,470.00 USD | `-6.08%` | `196,099.30` |
| `Live` | `Long` | `0.8805` | 133,320.00 USD | 0.00 USD | 1,530.00 USD | `-5.98%` | `1,737.40` |
| `Live` | `Long` | `0.8815` | 131,790.00 USD | 0.00 USD | 8,730.00 USD | `-5.87%` | `9,904.10` |
| `Live` | `Long` | `0.8825` | 123,060.00 USD | 0.00 USD | 5,300.00 USD | `-5.76%` | `6,002.40` |
| `Live` | `Long` | `0.8835` | 117,760.00 USD | 0.00 USD | 7,220.00 USD | `-5.66%` | `8,171.40` |
| `Live` | `Long` | `0.8845` | 110,540.00 USD | 0.00 USD | 3,550.00 USD | `-5.55%` | `4,018.00` |
| `Live` | `Long` | `0.8855` | 106,990.00 USD | 0.00 USD | 2,660.00 USD | `-5.44%` | `2,998.60` |
| `Live` | `Long` | `0.8865` | 104,330.00 USD | 0.00 USD | 19,190.00 USD | `-5.34%` | `21,649.30` |
| `Live` | `Long` | `0.8875` | 85,140.00 USD | 0.00 USD | 12,780.00 USD | `-5.23%` | `14,398.30` |
| `Live` | `Long` | `0.8885` | 72,360.00 USD | 0.00 USD | 697.38 USD | `-5.12%` | `784.90` |
| `Live` | `Long` | `0.8895` | 71,660.00 USD | 0.00 USD | 3,530.00 USD | `-5.02%` | `3,972.10` |
| `Live` | `Short` | `0.8905` | 892.28 USD | 892.28 USD | 0.00 USD | `-4.91%` | `1,002.00` |
| `Live` | `Long` | `0.8915` | 68,130.00 USD | 0.00 USD | 1,100.00 USD | `-4.80%` | `1,229.80` |
| `Live` | `Long` | `0.8925` | 67,040.00 USD | 0.00 USD | 1,040.00 USD | `-4.70%` | `1,162.90` |
| `Live` | `Long` | `0.8935` | 66,000.00 USD | 0.00 USD | 20,360.00 USD | `-4.59%` | `22,791.70` |
| `Live` | `Long` | `0.8945` | 45,630.00 USD | 0.00 USD | 5,750.00 USD | `-4.48%` | `6,428.20` |
| `Live` | `Long` | `0.8955` | 39,880.00 USD | 0.00 USD | 257.01 USD | `-4.38%` | `287.00` |
| `Live` | `Long` | `0.8965` | 39,630.00 USD | 0.00 USD | 29,550.00 USD | `-4.27%` | `32,958.10` |
| `Live` | `Long` | `0.8975` | 10,080.00 USD | 0.00 USD | 3,540.00 USD | `-4.16%` | `3,941.60` |
| `Live` | `Long` | `0.8985` | 6,540.00 USD | 0.00 USD | 320.05 USD | `-4.06%` | `356.20` |
| `Live` | `Long` | `0.8995` | 6,220.00 USD | 0.00 USD | 143.92 USD | `-3.95%` | `160.00` |
| `Live` | `Long` | `0.9055` | 6,080.00 USD | 0.00 USD | 119.44 USD | `-3.31%` | `131.90` |
| `Live` | `Long` | `0.9075` | 5,960.00 USD | 0.00 USD | 5,960.00 USD | `-3.09%` | `6,565.50` |
| `Live` | `Short` | `0.9675` | 4,050.00 USD | 3,160.00 USD | 0.00 USD | `+3.31%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 69,120.00 USD | 65,060.00 USD | 0.00 USD | `+3.63%` | `67,040.50` |
| `Live` | `Short` | `0.9765` | 69,330.00 USD | 214.44 USD | 0.00 USD | `+4.27%` | `219.60` |
| `Live` | `Short` | `0.9805` | 84,910.00 USD | 15,580.00 USD | 0.00 USD | `+4.70%` | `15,886.90` |
| `Live` | `Short` | `0.9845` | 90,990.00 USD | 6,080.00 USD | 0.00 USD | `+5.13%` | `6,175.20` |
| `Live` | `Short` | `0.9865` | 91,720.00 USD | 731.29 USD | 0.00 USD | `+5.34%` | `741.30` |
| `Live` | `Short` | `0.9875` | 146,320.00 USD | 54,600.00 USD | 0.00 USD | `+5.45%` | `55,292.50` |
| `Live` | `Short` | `0.9885` | 151,240.00 USD | 4,930.00 USD | 0.00 USD | `+5.55%` | `4,982.50` |
| `Live` | `Short` | `0.9895` | 157,010.00 USD | 5,760.00 USD | 0.00 USD | `+5.66%` | `5,824.20` |
| `Live` | `Short` | `0.9905` | 177,060.00 USD | 20,050.00 USD | 0.00 USD | `+5.77%` | `20,246.30` |
| `Live` | `Short` | `0.9925` | 179,480.00 USD | 2,420.00 USD | 0.00 USD | `+5.98%` | `2,434.50` |
| `Live` | `Short` | `0.9945` | 185,900.00 USD | 6,430.00 USD | 0.00 USD | `+6.20%` | `6,462.70` |
| `Live` | `Short` | `0.9965` | 190,680.00 USD | 4,780.00 USD | 0.00 USD | `+6.41%` | `4,795.10` |
| `Live` | `Short` | `1.00` | 191,130.00 USD | 449.11 USD | 0.00 USD | `+7.26%` | `447.10` |
| `Live` | `Short` | `1.02` | 191,300.00 USD | 170.40 USD | 0.00 USD | `+8.44%` | `167.80` |
| `Live` | `Short` | `1.03` | 654,580.00 USD | 463,280.00 USD | 0.00 USD | `+9.93%` | `450,000.00` |
| `Live` | `Short` | `1.03` | 657,760.00 USD | 3,190.00 USD | 0.00 USD | `+10.15%` | `3,089.60` |
| `Live` | `Short` | `1.04` | 668,170.00 USD | 10,400.00 USD | 0.00 USD | `+11.00%` | `10,007.60` |
| `Live` | `Short` | `1.04` | 668,310.00 USD | 139.22 USD | 0.00 USD | `+11.11%` | `133.80` |
| `Live` | `Short` | `1.05` | 668,900.00 USD | 597.52 USD | 0.00 USD | `+12.18%` | `568.80` |
| `Live` | `Short` | `1.05` | 671,290.00 USD | 2,390.00 USD | 0.00 USD | `+12.28%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 672,620.00 USD | 1,330.00 USD | 0.00 USD | `+12.39%` | `1,260.50` |
| `Live` | `Short` | `1.05` | 672,940.00 USD | 317.52 USD | 0.00 USD | `+12.50%` | `301.40` |
| `Live` | `Short` | `1.05` | 673,270.00 USD | 328.69 USD | 0.00 USD | `+12.60%` | `311.70` |
| `Live` | `Short` | `1.07` | 673,380.00 USD | 116.04 USD | 0.00 USD | `+14.52%` | `108.20` |
| `Live` | `Short` | `1.08` | 674,530.00 USD | 1,150.00 USD | 0.00 USD | `+15.06%` | `1,066.30` |
| `Live` | `Short` | `1.08` | 680,230.00 USD | 5,700.00 USD | 0.00 USD | `+15.27%` | `5,278.70` |
| `Live` | `Short` | `1.08` | 683,810.00 USD | 3,580.00 USD | 0.00 USD | `+15.38%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 686,940.00 USD | 3,120.00 USD | 0.00 USD | `+15.49%` | `2,889.30` |
| `Live` | `Short` | `1.08` | 687,100.00 USD | 166.43 USD | 0.00 USD | `+15.70%` | `153.60` |
| `Live` | `Short` | `1.08` | 688,220.00 USD | 1,110.00 USD | 0.00 USD | `+15.81%` | `1,026.10` |
| `Live` | `Short` | `1.09` | 693,770.00 USD | 5,550.00 USD | 0.00 USD | `+16.34%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 694,090.00 USD | 324.90 USD | 0.00 USD | `+17.41%` | `295.50` |
| `Live` | `Short` | `1.10` | 694,370.00 USD | 277.22 USD | 0.00 USD | `+17.51%` | `251.90` |
| `Live` | `Short` | `1.13` | 717,680.00 USD | 23,310.00 USD | 0.00 USD | `+20.29%` | `20,691.10` |
| `Live` | `Short` | `1.20` | 719,130.00 USD | 1,450.00 USD | 0.00 USD | `+27.87%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 719,390.00 USD | 253.69 USD | 0.00 USD | `+28.09%` | `211.50` |
| `Live` | `Short` | `1.20` | 749,150.00 USD | 29,760.00 USD | 0.00 USD | `+28.41%` | `24,749.90` |
| `Live` | `Short` | `1.21` | 749,290.00 USD | 147.43 USD | 0.00 USD | `+28.73%` | `122.30` |
| `Live` | `Short` | `1.22` | 752,180.00 USD | 2,880.00 USD | 0.00 USD | `+30.01%` | `2,367.80` |
| `Live` | `Short` | `1.22` | 756,620.00 USD | 4,440.00 USD | 0.00 USD | `+30.11%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 765,910.00 USD | 9,290.00 USD | 0.00 USD | `+30.22%` | `7,618.00` |
| `Live` | `Short` | `1.23` | 771,180.00 USD | 5,270.00 USD | 0.00 USD | `+31.61%` | `4,273.60` |
| `Live` | `Short` | `1.23` | 771,560.00 USD | 380.84 USD | 0.00 USD | `+31.82%` | `308.50` |
| `Live` | `Short` | `1.26` | 771,700.00 USD | 137.21 USD | 0.00 USD | `+34.17%` | `109.20` |
| `Live` | `Short` | `1.26` | 985,520.00 USD | 213,830.00 USD | 0.00 USD | `+34.28%` | `170,042.00` |
| `Live` | `Short` | `1.26` | 988,190.00 USD | 2,670.00 USD | 0.00 USD | `+34.49%` | `2,118.80` |
| `Live` | `Short` | `1.27` | 990,280.00 USD | 2,090.00 USD | 0.00 USD | `+35.88%` | `1,639.00` |
| `Live` | `Short` | `1.28` | 1,030,000.00 USD | 39,880.00 USD | 0.00 USD | `+36.95%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 1,030,000.00 USD | 226.80 USD | 0.00 USD | `+38.23%` | `175.20` |
| `Live` | `Short` | `1.30` | 1,030,000.00 USD | 114.40 USD | 0.00 USD | `+38.66%` | `88.10` |
| `Live` | `Short` | `1.31` | 1,030,000.00 USD | 1,020.00 USD | 0.00 USD | `+39.73%` | `777.20` |
| `Live` | `Short` | `1.31` | 1,060,000.00 USD | 31,530.00 USD | 0.00 USD | `+40.05%` | `24,042.40` |
| `Live` | `Short` | `1.33` | 1,070,000.00 USD | 6,340.00 USD | 0.00 USD | `+41.54%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 1,090,000.00 USD | 21,970.00 USD | 0.00 USD | `+41.86%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 1,090,000.00 USD | 358.30 USD | 0.00 USD | `+42.07%` | `269.30` |
| `Live` | `Short` | `1.33` | 1,090,000.00 USD | 1,520.00 USD | 0.00 USD | `+42.29%` | `1,143.40` |
| `Live` | `Short` | `1.34` | 1,100,000.00 USD | 6,860.00 USD | 0.00 USD | `+43.04%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 1,100,000.00 USD | 260.65 USD | 0.00 USD | `+46.03%` | `190.60` |
| `Live` | `Short` | `1.37` | 1,460,000.00 USD | 358,280.00 USD | 0.00 USD | `+46.56%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 1,460,000.00 USD | 4,450.00 USD | 0.00 USD | `+51.04%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 1,460,000.00 USD | 402.08 USD | 0.00 USD | `+53.39%` | `279.90` |
| `Live` | `Short` | `1.44` | 1,460,000.00 USD | 288.68 USD | 0.00 USD | `+53.82%` | `200.40` |
| `Live` | `Short` | `1.45` | 1,460,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.89%` | `826.40` |
| `Live` | `Short` | `1.46` | 1,470,000.00 USD | 9,490.00 USD | 0.00 USD | `+56.06%` | `6,491.20` |
| `Live` | `Short` | `1.47` | 1,470,000.00 USD | 143.91 USD | 0.00 USD | `+56.49%` | `98.20` |
| `Live` | `Short` | `1.47` | 1,480,000.00 USD | 4,820.00 USD | 0.00 USD | `+56.92%` | `3,279.70` |
| `Live` | `Short` | `1.48` | 1,480,000.00 USD | 1,090.00 USD | 0.00 USD | `+57.99%` | `736.60` |
| `Live` | `Short` | `1.49` | 1,480,000.00 USD | 1,360.00 USD | 0.00 USD | `+58.95%` | `910.40` |
| `Live` | `Short` | `1.51` | 1,490,000.00 USD | 4,020.00 USD | 0.00 USD | `+61.72%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 1,510,000.00 USD | 24,350.00 USD | 0.00 USD | `+63.11%` | `15,941.90` |
| `Live` | `Short` | `1.54` | 1,510,000.00 USD | 144.34 USD | 0.00 USD | `+63.97%` | `94.00` |
| `Live` | `Short` | `1.55` | 4,090,000.00 USD | 2,580,000.00 USD | 0.00 USD | `+65.57%` | `1,664,573.50` |
| `Live` | `Short` | `1.58` | 4,110,000.00 USD | 17,720.00 USD | 0.00 USD | `+69.20%` | `11,182.60` |
| `Live` | `Short` | `1.59` | 4,110,000.00 USD | 287.38 USD | 0.00 USD | `+69.73%` | `180.80` |
| `Live` | `Short` | `1.61` | 4,110,000.00 USD | 122.73 USD | 0.00 USD | `+71.76%` | `76.30` |
| `Live` | `Short` | `1.62` | 4,120,000.00 USD | 9,710.00 USD | 0.00 USD | `+72.72%` | `6,000.00` |
| `Live` | `Short` | `1.65` | 4,140,000.00 USD | 21,330.00 USD | 0.00 USD | `+75.82%` | `12,957.30` |
| `Live` | `Short` | `1.67` | 4,150,000.00 USD | 9,400.00 USD | 0.00 USD | `+77.85%` | `5,645.40` |
| `Live` | `Short` | `1.67` | 4,190,000.00 USD | 39,240.00 USD | 0.00 USD | `+78.06%` | `23,529.40` |
| `Live` | `Short` | `1.69` | 4,480,000.00 USD | 291,760.00 USD | 0.00 USD | `+80.09%` | `173,000.00` |
| `Live` | `Short` | `1.71` | 4,480,000.00 USD | 205.67 USD | 0.00 USD | `+82.87%` | `120.10` |
| `Live` | `Short` | `1.72` | 4,570,000.00 USD | 84,990.00 USD | 0.00 USD | `+83.19%` | `49,543.90` |
| `Live` | `Short` | `1.73` | 4,570,000.00 USD | 226.05 USD | 0.00 USD | `+85.11%` | `130.40` |
| `Live` | `Short` | `1.74` | 4,570,000.00 USD | 2,080.00 USD | 0.00 USD | `+85.86%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 4,590,000.00 USD | 19,920.00 USD | 0.00 USD | `+87.03%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 4,600,000.00 USD | 11,350.00 USD | 0.00 USD | `+87.14%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 4,600,000.00 USD | 1,520.00 USD | 0.00 USD | `+87.35%` | `868.90` |
| `Live` | `Short` | `1.79` | 4,600,000.00 USD | 781.77 USD | 0.00 USD | `+90.77%` | `437.60` |
| `Live` | `Short` | `1.79` | 4,600,000.00 USD | 952.52 USD | 0.00 USD | `+91.62%` | `530.80` |
| `Live` | `Short` | `1.81` | 4,610,000.00 USD | 2,470.00 USD | 0.00 USD | `+93.76%` | `1,360.10` |
| `Live` | `Short` | `1.83` | 4,620,000.00 USD | 14,230.00 USD | 0.00 USD | `+95.04%` | `7,789.30` |
| `Live` | `Short` | `1.83` | 4,620,000.00 USD | 203.88 USD | 0.00 USD | `+95.25%` | `111.50` |
| `Live` | `Short` | `1.85` | 4,620,000.00 USD | 943.75 USD | 0.00 USD | `+97.60%` | `510.00` |
| `Live` | `Short` | `1.85` | 4,620,000.00 USD | 190.35 USD | 0.00 USD | `+97.92%` | `102.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2745` | 1,860,000.00 USD | 0.00 USD | 455.97 USD | `-70.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,860,000.00 USD | 0.00 USD | 102.75 USD | `-63.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,860,000.00 USD | 0.00 USD | 256.78 USD | `-62.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,860,000.00 USD | 0.00 USD | 428.87 USD | `-58.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,860,000.00 USD | 0.00 USD | 123.45 USD | `-56.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,860,000.00 USD | 0.00 USD | 818.15 USD | `-55.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 1,860,000.00 USD | 0.00 USD | 454.04 USD | `-54.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,860,000.00 USD | 0.00 USD | 436.41 USD | `-53.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,860,000.00 USD | 0.00 USD | 876.79 USD | `-53.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,860,000.00 USD | 0.00 USD | 466.72 USD | `-51.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,860,000.00 USD | 0.00 USD | 142.95 USD | `-49.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,860,000.00 USD | 0.00 USD | 5,650.00 USD | `-46.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,850,000.00 USD | 0.00 USD | 151.74 USD | `-45.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,850,000.00 USD | 0.00 USD | 123.91 USD | `-44.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,850,000.00 USD | 0.00 USD | 219.80 USD | `-41.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,850,000.00 USD | 0.00 USD | 237,400.00 USD | `-41.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 1,610,000.00 USD | 0.00 USD | 276.75 USD | `-40.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 1,610,000.00 USD | 0.00 USD | 2,010.00 USD | `-40.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 1,610,000.00 USD | 0.00 USD | 119.76 USD | `-38.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 1,610,000.00 USD | 0.00 USD | 108.39 USD | `-35.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 1,610,000.00 USD | 0.00 USD | 123.28 USD | `-35.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 1,610,000.00 USD | 0.00 USD | 488.52 USD | `-33.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 1,610,000.00 USD | 0.00 USD | 5,940.00 USD | `-33.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 1,600,000.00 USD | 0.00 USD | 242.24 USD | `-32.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 1,600,000.00 USD | 0.00 USD | 193.95 USD | `-30.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 1,600,000.00 USD | 0.00 USD | 647.50 USD | `-30.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 1,600,000.00 USD | 0.00 USD | 834.79 USD | `-30.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 1,600,000.00 USD | 0.00 USD | 158.54 USD | `-30.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 1,600,000.00 USD | 0.00 USD | 195.47 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 1,600,000.00 USD | 0.00 USD | 190.25 USD | `-29.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 1,600,000.00 USD | 0.00 USD | 52,450.00 USD | `-28.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 1,550,000.00 USD | 0.00 USD | 536.11 USD | `-28.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 1,550,000.00 USD | 0.00 USD | 5,490.00 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 1,540,000.00 USD | 0.00 USD | 340.75 USD | `-27.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 1,540,000.00 USD | 0.00 USD | 9,270.00 USD | `-26.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 1,530,000.00 USD | 0.00 USD | 120.53 USD | `-26.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6935` | 1,530,000.00 USD | 0.00 USD | 126.98 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 1,530,000.00 USD | 0.00 USD | 160.71 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 1,530,000.00 USD | 0.00 USD | 187.61 USD | `-25.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 1,530,000.00 USD | 0.00 USD | 2,920.00 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 1,530,000.00 USD | 0.00 USD | 89,150.00 USD | `-25.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 1,440,000.00 USD | 0.00 USD | 189.06 USD | `-24.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 1,440,000.00 USD | 0.00 USD | 5,650.00 USD | `-24.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 1,430,000.00 USD | 0.00 USD | 100.47 USD | `-24.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 1,430,000.00 USD | 0.00 USD | 152.05 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 1,430,000.00 USD | 0.00 USD | 123.41 USD | `-23.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 1,430,000.00 USD | 0.00 USD | 1,130.00 USD | `-22.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 1,430,000.00 USD | 0.00 USD | 18,770.00 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 1,410,000.00 USD | 0.00 USD | 257.26 USD | `-21.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 1,410,000.00 USD | 0.00 USD | 10,160.00 USD | `-20.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 1,400,000.00 USD | 0.00 USD | 93,810.00 USD | `-19.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 1,310,000.00 USD | 0.00 USD | 1,230.00 USD | `-19.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 1,310,000.00 USD | 0.00 USD | 924.99 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 1,310,000.00 USD | 0.00 USD | 804.61 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 1,310,000.00 USD | 0.00 USD | 191.12 USD | `-18.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 1,310,000.00 USD | 0.00 USD | 1,370.00 USD | `-18.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 1,310,000.00 USD | 0.00 USD | 125.92 USD | `-17.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 1,310,000.00 USD | 0.00 USD | 1,150.00 USD | `-17.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 1,300,000.00 USD | 0.00 USD | 200.39 USD | `-17.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 1,300,000.00 USD | 0.00 USD | 1,860.00 USD | `-16.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 1,300,000.00 USD | 0.00 USD | 128.47 USD | `-16.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 1,300,000.00 USD | 0.00 USD | 3,130.00 USD | `-16.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 1,300,000.00 USD | 0.00 USD | 135.11 USD | `-16.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 1,300,000.00 USD | 0.00 USD | 1,500.00 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 1,300,000.00 USD | 0.00 USD | 25,170.00 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 1,270,000.00 USD | 0.00 USD | 103.42 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 1,270,000.00 USD | 0.00 USD | 1,260.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 1,270,000.00 USD | 0.00 USD | 5,660.00 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 1,270,000.00 USD | 0.00 USD | 144.67 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 1,270,000.00 USD | 0.00 USD | 50,540.00 USD | `-13.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 1,210,000.00 USD | 0.00 USD | 263.25 USD | `-13.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 1,210,000.00 USD | 0.00 USD | 16,870.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 1,200,000.00 USD | 0.00 USD | 91,080.00 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 1,110,000.00 USD | 0.00 USD | 174.63 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8175` | 1,110,000.00 USD | 0.00 USD | 16,350.00 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 1,090,000.00 USD | 0.00 USD | 125.72 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 1,090,000.00 USD | 0.00 USD | 340.83 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 1,090,000.00 USD | 0.00 USD | 11,040.00 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 1,080,000.00 USD | 0.00 USD | 922.29 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 1,080,000.00 USD | 0.00 USD | 1,120.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 1,080,000.00 USD | 0.00 USD | 124.43 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 1,080,000.00 USD | 0.00 USD | 4,380.00 USD | `-11.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 1,070,000.00 USD | 0.00 USD | 171.46 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 1,070,000.00 USD | 0.00 USD | 1,270.00 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 1,070,000.00 USD | 0.00 USD | 4,170.00 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 1,070,000.00 USD | 0.00 USD | 610.23 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 1,070,000.00 USD | 0.00 USD | 475.87 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 1,070,000.00 USD | 0.00 USD | 320.31 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 1,060,000.00 USD | 0.00 USD | 1,010.00 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8425` | 1,060,000.00 USD | 0.00 USD | 1,390.00 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 1,060,000.00 USD | 0.00 USD | 221.25 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 1,060,000.00 USD | 0.00 USD | 212.81 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 1,060,000.00 USD | 0.00 USD | 462.49 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 1,060,000.00 USD | 0.00 USD | 108.44 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 1,060,000.00 USD | 0.00 USD | 481.80 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 1,060,000.00 USD | 0.00 USD | 12,210.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 1,050,000.00 USD | 0.00 USD | 901.40 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 1,050,000.00 USD | 0.00 USD | 242.93 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 1,050,000.00 USD | 0.00 USD | 6,200.00 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 1,040,000.00 USD | 0.00 USD | 108.13 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 1,040,000.00 USD | 0.00 USD | 1,640.00 USD | `-8.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 1,040,000.00 USD | 0.00 USD | 4,300.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 1,040,000.00 USD | 0.00 USD | 202.45 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 1,040,000.00 USD | 0.00 USD | 921.70 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 1,030,000.00 USD | 0.00 USD | 161.49 USD | `-7.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 1,030,000.00 USD | 0.00 USD | 1,270.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 1,030,000.00 USD | 0.00 USD | 741.45 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 1,030,000.00 USD | 0.00 USD | 168.75 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 1,030,000.00 USD | 0.00 USD | 2,110.00 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 1,030,000.00 USD | 0.00 USD | 3,350.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 1,030,000.00 USD | 0.00 USD | 712.45 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 1,030,000.00 USD | 0.00 USD | 58,490.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 967,320.00 USD | 0.00 USD | 281.70 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 967,030.00 USD | 0.00 USD | 133.10 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 966,900.00 USD | 0.00 USD | 246.98 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 966,650.00 USD | 0.00 USD | 876.50 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 965,780.00 USD | 0.00 USD | 9,070.00 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 956,710.00 USD | 0.00 USD | 151.10 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 956,560.00 USD | 0.00 USD | 507.74 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 956,050.00 USD | 0.00 USD | 8,100.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 947,950.00 USD | 0.00 USD | 157,870.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 790,090.00 USD | 0.00 USD | 5,020.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 785,070.00 USD | 0.00 USD | 11,690.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 773,380.00 USD | 0.00 USD | 559.80 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8855` | 772,820.00 USD | 0.00 USD | 3,660.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 769,160.00 USD | 0.00 USD | 11,560.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 757,610.00 USD | 0.00 USD | 886.79 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8885` | 756,720.00 USD | 0.00 USD | 11,360.00 USD | `-5.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 745,360.00 USD | 0.00 USD | 7,820.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8905` | 737,550.00 USD | 0.00 USD | 10,130.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 727,420.00 USD | 0.00 USD | 469.91 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 726,950.00 USD | 0.00 USD | 10,610.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 716,340.00 USD | 0.00 USD | 7,100.00 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8945` | 709,240.00 USD | 0.00 USD | 2,920.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8955` | 706,320.00 USD | 0.00 USD | 3,900.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 702,420.00 USD | 0.00 USD | 7,930.00 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8975` | 694,500.00 USD | 0.00 USD | 18,210.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 676,290.00 USD | 0.00 USD | 2,460.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8995` | 673,830.00 USD | 0.00 USD | 28,960.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 644,860.00 USD | 0.00 USD | 4,300.00 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9015` | 640,560.00 USD | 0.00 USD | 1,230.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 639,340.00 USD | 0.00 USD | 926.06 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 638,410.00 USD | 0.00 USD | 561.16 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 637,850.00 USD | 0.00 USD | 1,140.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9055` | 636,710.00 USD | 0.00 USD | 1,990.00 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 634,720.00 USD | 0.00 USD | 30,120.00 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 604,600.00 USD | 0.00 USD | 4,680.00 USD | `-3.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 599,920.00 USD | 0.00 USD | 1,440.00 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 598,480.00 USD | 0.00 USD | 1,520.00 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9105` | 596,950.00 USD | 0.00 USD | 637.90 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 596,320.00 USD | 0.00 USD | 6,170.00 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9125` | 590,150.00 USD | 0.00 USD | 14,760.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 575,390.00 USD | 0.00 USD | 465.70 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 574,920.00 USD | 0.00 USD | 337.72 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 574,580.00 USD | 0.00 USD | 5,070.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 569,520.00 USD | 0.00 USD | 5,040.00 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 564,480.00 USD | 0.00 USD | 1,470.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 563,000.00 USD | 0.00 USD | 302.74 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 562,700.00 USD | 0.00 USD | 1,380.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 561,320.00 USD | 0.00 USD | 16,090.00 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 545,230.00 USD | 0.00 USD | 7,650.00 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 537,580.00 USD | 0.00 USD | 84,100.00 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 453,480.00 USD | 0.00 USD | 3,230.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 450,250.00 USD | 0.00 USD | 498.77 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 449,760.00 USD | 0.00 USD | 235,060.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 214,690.00 USD | 0.00 USD | 160,180.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 54,510.00 USD | 0.00 USD | 146.27 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 54,360.00 USD | 0.00 USD | 195.17 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 54,170.00 USD | 0.00 USD | 103.17 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 54,060.00 USD | 0.00 USD | 186.29 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 53,880.00 USD | 0.00 USD | 148.85 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 53,730.00 USD | 0.00 USD | 5,600.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 48,130.00 USD | 0.00 USD | 979.71 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9345` | 47,150.00 USD | 0.00 USD | 45,680.00 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 1,470.00 USD | 0.00 USD | 1,470.00 USD | `-0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 103.95 USD | 103.95 USD | 0.00 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 279.83 USD | 175.88 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 53,340.00 USD | 53,060.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 57,250.00 USD | 3,910.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 66,210.00 USD | 8,960.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 66,370.00 USD | 158.55 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 66,500.00 USD | 132.80 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 66,620.00 USD | 121.15 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 70,970.00 USD | 4,340.00 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 71,990.00 USD | 1,030.00 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 73,050.00 USD | 1,050.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 79,050.00 USD | 6,000.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 79,210.00 USD | 158.49 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 79,470.00 USD | 261.97 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 79,740.00 USD | 265.66 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 80,000.00 USD | 263.76 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 81,000.00 USD | 999.27 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 83,560.00 USD | 2,560.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 86,710.00 USD | 3,150.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 88,140.00 USD | 1,440.00 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 91,030.00 USD | 2,890.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 98,630.00 USD | 7,600.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 106,490.00 USD | 7,860.00 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 106,590.00 USD | 100.17 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 147,430.00 USD | 40,840.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 147,600.00 USD | 161.82 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 147,790.00 USD | 197.79 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 148,690.00 USD | 900.10 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 150,030.00 USD | 1,340.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 150,230.00 USD | 204.20 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 152,100.00 USD | 1,860.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 155,690.00 USD | 3,590.00 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 156,840.00 USD | 1,150.00 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 157,350.00 USD | 513.54 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 162,660.00 USD | 5,310.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 162,870.00 USD | 210.33 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 163,990.00 USD | 1,130.00 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 174,570.00 USD | 10,580.00 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 174,830.00 USD | 253.14 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 175,070.00 USD | 244.81 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 175,360.00 USD | 285.72 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 175,560.00 USD | 201.77 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 175,980.00 USD | 421.87 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 212,430.00 USD | 36,450.00 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 217,900.00 USD | 5,470.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 218,620.00 USD | 714.28 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 219,680.00 USD | 1,060.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 219,950.00 USD | 271.90 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 220,440.00 USD | 490.99 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 221,210.00 USD | 769.72 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 222,200.00 USD | 991.50 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 232,540.00 USD | 10,340.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 232,820.00 USD | 284.92 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 233,100.00 USD | 277.64 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 233,450.00 USD | 350.37 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 233,600.00 USD | 144.04 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 233,700.00 USD | 105.44 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 242,470.00 USD | 8,760.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 244,040.00 USD | 1,570.00 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 246,220.00 USD | 2,180.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 246,580.00 USD | 363.87 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 247,170.00 USD | 589.52 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 247,830.00 USD | 660.52 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 257,920.00 USD | 10,090.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 263,340.00 USD | 5,420.00 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 266,110.00 USD | 2,770.00 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 299,560.00 USD | 33,450.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 300,290.00 USD | 722.63 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 300,600.00 USD | 312.07 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 300,770.00 USD | 171.24 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 301,330.00 USD | 561.11 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 302,940.00 USD | 1,610.00 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 305,160.00 USD | 2,210.00 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 305,590.00 USD | 432.18 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 305,730.00 USD | 137.88 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 309,890.00 USD | 4,170.00 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 310,020.00 USD | 132.52 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 310,180.00 USD | 160.60 USD | 0.00 USD | `+11.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 316,850.00 USD | 6,670.00 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 324,530.00 USD | 7,680.00 USD | 0.00 USD | `+11.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 324,750.00 USD | 224.56 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 328,330.00 USD | 3,570.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 334,510.00 USD | 6,190.00 USD | 0.00 USD | `+12.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,090,000.00 USD | 1,760,000.00 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,090,000.00 USD | 1,810.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,090,000.00 USD | 248.20 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,100,000.00 USD | 5,390.00 USD | 0.00 USD | `+13.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,100,000.00 USD | 285.32 USD | 0.00 USD | `+13.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,100,000.00 USD | 2,570.00 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,100,000.00 USD | 1,240.00 USD | 0.00 USD | `+13.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,100,000.00 USD | 278.06 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,100,000.00 USD | 100.93 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,100,000.00 USD | 309.00 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,100,000.00 USD | 272.12 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,100,000.00 USD | 117.12 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,240,000.00 USD | 140,120.00 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,240,000.00 USD | 530.01 USD | 0.00 USD | `+14.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,240,000.00 USD | 128.23 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,350,000.00 USD | 108,190.00 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,350,000.00 USD | 550.49 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,360,000.00 USD | 5,810.00 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,360,000.00 USD | 5,570.00 USD | 0.00 USD | `+16.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,370,000.00 USD | 1,290.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,370,000.00 USD | 294.81 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,370,000.00 USD | 123.13 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,370,000.00 USD | 494.98 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,370,000.00 USD | 613.52 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,490,000.00 USD | 117,450.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,490,000.00 USD | 409.76 USD | 0.00 USD | `+17.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,490,000.00 USD | 162.77 USD | 0.00 USD | `+17.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,490,000.00 USD | 959.70 USD | 0.00 USD | `+17.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,490,000.00 USD | 160.18 USD | 0.00 USD | `+18.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,490,000.00 USD | 433.10 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,490,000.00 USD | 628.71 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,490,000.00 USD | 293.61 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,600,000.00 USD | 112,050.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,600,000.00 USD | 462.47 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,600,000.00 USD | 2,180.00 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,600,000.00 USD | 273.34 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,600,000.00 USD | 141.31 USD | 0.00 USD | `+20.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,620,000.00 USD | 20,740.00 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,630,000.00 USD | 1,430.00 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,630,000.00 USD | 338.50 USD | 0.00 USD | `+22.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,630,000.00 USD | 769.57 USD | 0.00 USD | `+22.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,630,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,630,000.00 USD | 2,450.00 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,630,000.00 USD | 1,250.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,630,000.00 USD | 143.67 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,630,000.00 USD | 1,700.00 USD | 0.00 USD | `+24.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,700,000.00 USD | 63,070.00 USD | 0.00 USD | `+24.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,700,000.00 USD | 304.33 USD | 0.00 USD | `+24.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,700,000.00 USD | 241.65 USD | 0.00 USD | `+25.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,700,000.00 USD | 239.97 USD | 0.00 USD | `+25.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,700,000.00 USD | 2,470.00 USD | 0.00 USD | `+25.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,700,000.00 USD | 3,060.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,700,000.00 USD | 351.02 USD | 0.00 USD | `+26.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,010,000.00 USD | 310,250.00 USD | 0.00 USD | `+26.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,010,000.00 USD | 309.53 USD | 0.00 USD | `+27.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,010,000.00 USD | 159.09 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,010,000.00 USD | 146.21 USD | 0.00 USD | `+27.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,090,000.00 USD | 79,220.00 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,090,000.00 USD | 933.81 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,090,000.00 USD | 658.86 USD | 0.00 USD | `+28.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,310,000.00 USD | 213,390.00 USD | 0.00 USD | `+29.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,310,000.00 USD | 211.10 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,310,000.00 USD | 1,050.00 USD | 0.00 USD | `+30.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,310,000.00 USD | 812.24 USD | 0.00 USD | `+30.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,310,000.00 USD | 509.71 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,310,000.00 USD | 162.15 USD | 0.00 USD | `+31.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,310,000.00 USD | 187.04 USD | 0.00 USD | `+31.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,310,000.00 USD | 542.12 USD | 0.00 USD | `+31.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,340,000.00 USD | 23,740.00 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,340,000.00 USD | 2,010.00 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,340,000.00 USD | 345.91 USD | 0.00 USD | `+32.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,340,000.00 USD | 104.79 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,340,000.00 USD | 6,870.00 USD | 0.00 USD | `+33.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,350,000.00 USD | 265.62 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,350,000.00 USD | 1,480.00 USD | 0.00 USD | `+34.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,350,000.00 USD | 1,010.00 USD | 0.00 USD | `+34.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,350,000.00 USD | 340.38 USD | 0.00 USD | `+35.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,350,000.00 USD | 903.22 USD | 0.00 USD | `+35.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,350,000.00 USD | 424.15 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,390,000.00 USD | 41,160.00 USD | 0.00 USD | `+36.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,400,000.00 USD | 12,840.00 USD | 0.00 USD | `+37.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,420,000.00 USD | 12,890.00 USD | 0.00 USD | `+37.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,420,000.00 USD | 8,820.00 USD | 0.00 USD | `+37.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,430,000.00 USD | 466.95 USD | 0.00 USD | `+38.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,430,000.00 USD | 613.59 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,430,000.00 USD | 1,420.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,440,000.00 USD | 13,000.00 USD | 0.00 USD | `+38.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,440,000.00 USD | 284.42 USD | 0.00 USD | `+38.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,460,000.00 USD | 22,710.00 USD | 0.00 USD | `+41.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,460,000.00 USD | 640.82 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,480,000.00 USD | 13,400.00 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,480,000.00 USD | 1,580.00 USD | 0.00 USD | `+43.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,480,000.00 USD | 1,580.00 USD | 0.00 USD | `+43.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,490,000.00 USD | 13,490.00 USD | 0.00 USD | `+44.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,510,000.00 USD | 11,580.00 USD | 0.00 USD | `+44.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,510,000.00 USD | 3,610.00 USD | 0.00 USD | `+44.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,510,000.00 USD | 1,540.00 USD | 0.00 USD | `+45.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,510,000.00 USD | 1,500.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,530,000.00 USD | 15,000.00 USD | 0.00 USD | `+45.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,540,000.00 USD | 9,030.00 USD | 0.00 USD | `+46.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,540,000.00 USD | 569.84 USD | 0.00 USD | `+48.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,550,000.00 USD | 13,890.00 USD | 0.00 USD | `+48.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,550,000.00 USD | 2,710.00 USD | 0.00 USD | `+49.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,570,000.00 USD | 15,500.00 USD | 0.00 USD | `+49.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,580,000.00 USD | 13,100.00 USD | 0.00 USD | `+49.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,610,000.00 USD | 32,860.00 USD | 0.00 USD | `+50.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,620,000.00 USD | 7,090.00 USD | 0.00 USD | `+50.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,620,000.00 USD | 106.64 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,620,000.00 USD | 1,430.00 USD | 0.00 USD | `+51.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,630,000.00 USD | 2,810.00 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,630,000.00 USD | 8,420.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 3,640,000.00 USD | 1,410.00 USD | 0.00 USD | `+52.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,640,000.00 USD | 431.38 USD | 0.00 USD | `+53.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,640,000.00 USD | 1,390.00 USD | 0.00 USD | `+53.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,650,000.00 USD | 14,390.00 USD | 0.00 USD | `+53.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,660,000.00 USD | 7,000.00 USD | 0.00 USD | `+54.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,660,000.00 USD | 434.98 USD | 0.00 USD | `+54.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,670,000.00 USD | 14,490.00 USD | 0.00 USD | `+54.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,680,000.00 USD | 1,370.00 USD | 0.00 USD | `+54.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 3,680,000.00 USD | 1,350.00 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,680,000.00 USD | 1,340.00 USD | 0.00 USD | `+56.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,680,000.00 USD | 1,300.00 USD | 0.00 USD | `+57.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,680,000.00 USD | 342.08 USD | 0.00 USD | `+57.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 3,680,000.00 USD | 1,330.00 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,680,000.00 USD | 1,320.00 USD | 0.00 USD | `+58.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,680,000.00 USD | 1,310.00 USD | 0.00 USD | `+58.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,700,000.00 USD | 14,890.00 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,710,000.00 USD | 9,580.00 USD | 0.00 USD | `+59.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,720,000.00 USD | 14,980.00 USD | 0.00 USD | `+60.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,730,000.00 USD | 5,110.00 USD | 0.00 USD | `+60.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,730,000.00 USD | 1,270.00 USD | 0.00 USD | `+62.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,730,000.00 USD | 1,260.00 USD | 0.00 USD | `+62.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 3,730,000.00 USD | 1,980.00 USD | 0.00 USD | `+64.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 3,730,000.00 USD | 574.53 USD | 0.00 USD | `+69.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 3,730,000.00 USD | 391.32 USD | 0.00 USD | `+70.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 3,740,000.00 USD | 1,160.00 USD | 0.00 USD | `+72.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,740,000.00 USD | 1,140.00 USD | 0.00 USD | `+74.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,740,000.00 USD | 1,970.00 USD | 0.00 USD | `+75.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 3,740,000.00 USD | 281.45 USD | 0.00 USD | `+77.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 3,740,000.00 USD | 958.84 USD | 0.00 USD | `+80.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 3,740,000.00 USD | 3,550.00 USD | 0.00 USD | `+81.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 3,740,000.00 USD | 1,070.00 USD | 0.00 USD | `+86.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 3,750,000.00 USD | 1,710.00 USD | 0.00 USD | `+88.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,760,000.00 USD | 13,670.00 USD | 0.00 USD | `+92.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,760,000.00 USD | 295.46 USD | 0.00 USD | `+92.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,760,000.00 USD | 328.97 USD | 0.00 USD | `+94.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,760,000.00 USD | 394.87 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,770,000.00 USD | 10,950.00 USD | 0.00 USD | `+97.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,810,000.00 USD | 41,990.00 USD | 0.00 USD | `+97.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.86` | 3,810,000.00 USD | 149.08 USD | 0.00 USD | `+98.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.87` | 3,830,000.00 USD | 17,290.00 USD | 0.00 USD | `+99.74%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8110` | 32,660,000.00 USD | 0.00 USD | 32,660,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD |
| `7D` | `0.8130` | 32,560,000.00 USD | 0.00 USD | 32,560,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD |
| `7D` | `0.8150` | 32,490,000.00 USD | 0.00 USD | 32,490,000.00 USD | 135,770.00 USD | 50,280.00 USD | 124,810.00 USD |
| `7D` | `0.8170` | 32,180,000.00 USD | 0.00 USD | 32,180,000.00 USD | 91,050.00 USD | 23,590.00 USD | 78,040.00 USD |
| `7D` | `0.8190` | 31,980,000.00 USD | 0.00 USD | 31,980,000.00 USD | 195,400.00 USD | 52,010.00 USD | 47,010.00 USD |
| `7D` | `0.8210` | 31,690,000.00 USD | 0.00 USD | 31,690,000.00 USD | 138,580.00 USD | 47,520.00 USD | 119,250.00 USD |
| `7D` | `0.8230` | 31,380,000.00 USD | 0.00 USD | 31,380,000.00 USD | 37,880.00 USD | 24,290.00 USD | 64,410.00 USD |
| `7D` | `0.8250` | 31,260,000.00 USD | 0.00 USD | 31,260,000.00 USD | 187,510.00 USD | 27,530.00 USD | 126,000.00 USD |
| `7D` | `0.8270` | 30,920,000.00 USD | 0.00 USD | 30,920,000.00 USD | 144,410.00 USD | 51,050.00 USD | 63,610.00 USD |
| `7D` | `0.8290` | 30,660,000.00 USD | 0.00 USD | 30,660,000.00 USD | 89,470.00 USD | 39,850.00 USD | 82,590.00 USD |
| `7D` | `0.8310` | 30,450,000.00 USD | 0.00 USD | 30,450,000.00 USD | 34,030.00 USD | 30,800.00 USD | 22,830.00 USD |
| `7D` | `0.8330` | 30,360,000.00 USD | 0.00 USD | 30,360,000.00 USD | 150,740.00 USD | 85,780.00 USD | 198,210.00 USD |
| `1D` | `0.8340` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 66,840.00 USD | 33,800.00 USD | 80,150.00 USD |
| `7D` | `0.8350` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 74,030.00 USD | 14,320.00 USD | 83,830.00 USD |
| `1D` | `0.8360` | 12,810,000.00 USD | 0.00 USD | 12,810,000.00 USD | 54,120.00 USD | 3,830.00 USD | 22,550.00 USD |
| `7D` | `0.8370` | 29,750,000.00 USD | 0.00 USD | 29,750,000.00 USD | 146,890.00 USD | 48,060.00 USD | 102,790.00 USD |
| `1D` | `0.8380` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 29,520.00 USD | 7,690.00 USD | 27,800.00 USD |
| `7D` | `0.8390` | 29,450,000.00 USD | 0.00 USD | 29,450,000.00 USD | 24,790.00 USD | 51,510.00 USD | 77,420.00 USD |
| `1D` | `0.8400` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 25,130.00 USD | 19,380.00 USD | 22,180.00 USD |
| `7D` | `0.8410` | 29,300,000.00 USD | 0.00 USD | 29,300,000.00 USD | 55,190.00 USD | 40,110.00 USD | 27,780.00 USD |
| `1D` | `0.8420` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 12,220.00 USD | 13,260.00 USD | 15,220.00 USD |
| `7D` | `0.8430` | 29,180,000.00 USD | 0.00 USD | 29,180,000.00 USD | 81,850.00 USD | 49,990.00 USD | 30,430.00 USD |
| `1D` | `0.8440` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 23,630.00 USD | 15,080.00 USD | 6,260.00 USD |
| `7D` | `0.8450` | 29,010,000.00 USD | 0.00 USD | 29,010,000.00 USD | 43,800.00 USD | 55,690.00 USD | 49,310.00 USD |
| `1D` | `0.8460` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 19,430.00 USD | 21,540.00 USD | 47,070.00 USD |
| `7D` | `0.8470` | 28,870,000.00 USD | 0.00 USD | 28,870,000.00 USD | 23,930.00 USD | 4,350.00 USD | 32,430.00 USD |
| `1D` | `0.8480` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 32,420.00 USD | 20,130.00 USD | 49,210.00 USD |
| `7D` | `0.8490` | 28,810,000.00 USD | 0.00 USD | 28,810,000.00 USD | 45,210.00 USD | 16,670.00 USD | 46,210.00 USD |
| `1D` | `0.8500` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 61,890.00 USD | 7,390.00 USD | 16,720.00 USD |
| `7D` | `0.8510` | 28,700,000.00 USD | 0.00 USD | 28,700,000.00 USD | 95,990.00 USD | 42,650.00 USD | 42,410.00 USD |
| `1D` | `0.8520` | 12,230,000.00 USD | 0.00 USD | 12,230,000.00 USD | 30,310.00 USD | 27,790.00 USD | 15,090.00 USD |
| `7D` | `0.8530` | 28,520,000.00 USD | 0.00 USD | 28,520,000.00 USD | 30,570.00 USD | 50,890.00 USD | 29,460.00 USD |
| `1D` | `0.8540` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 20,080.00 USD | 11,230.00 USD | 41,710.00 USD |
| `7D` | `0.8550` | 28,410,000.00 USD | 0.00 USD | 28,410,000.00 USD | 78,320.00 USD | 26,490.00 USD | 3,080.00 USD |
| `1D` | `0.8560` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 27,930.00 USD | 22,280.00 USD | 25,480.00 USD |
| `7D` | `0.8570` | 28,300,000.00 USD | 0.00 USD | 28,300,000.00 USD | 99,680.00 USD | 45,070.00 USD | 5,400.00 USD |
| `1D` | `0.8580` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 56,290.00 USD | 13,730.00 USD | 14,750.00 USD |
| `7D` | `0.8590` | 28,150,000.00 USD | 0.00 USD | 28,150,000.00 USD | 51,400.00 USD | 22,020.00 USD | 18,570.00 USD |
| `1D` | `0.8600` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 16,950.00 USD | 6,660.00 USD | 15,560.00 USD |
| `7D` | `0.8610` | 28,060,000.00 USD | 0.00 USD | 28,060,000.00 USD | 36,870.00 USD | 71,110.00 USD | 30,720.00 USD |
| `1D` | `0.8620` | 11,890,000.00 USD | 0.00 USD | 11,890,000.00 USD | 6,110.00 USD | 5,870.00 USD | 127.55 USD |
| `7D` | `0.8630` | 27,920,000.00 USD | 0.00 USD | 27,920,000.00 USD | 30,710.00 USD | 13,800.00 USD | 48,380.00 USD |
| `1D` | `0.8640` | 11,870,000.00 USD | 0.00 USD | 11,870,000.00 USD | 52,440.00 USD | 24,580.00 USD | 60,880.00 USD |
| `7D` | `0.8650` | 27,820,000.00 USD | 0.00 USD | 27,820,000.00 USD | 235,900.00 USD | 43,890.00 USD | 100,880.00 USD |
| `1D` | `0.8660` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 137,930.00 USD | 1,740.00 USD | 13,540.00 USD |
| `7D` | `0.8670` | 27,440,000.00 USD | 0.00 USD | 27,440,000.00 USD | 159,120.00 USD | 71,510.00 USD | 58,910.00 USD |
| `1D` | `0.8680` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 103,830.00 USD | 61,020.00 USD | 33,070.00 USD |
| `7D` | `0.8690` | 27,150,000.00 USD | 0.00 USD | 27,150,000.00 USD | 182,190.00 USD | 79,290.00 USD | 194,430.00 USD |
| `1D` | `0.8700` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 110,320.00 USD | 90,530.00 USD | 226,830.00 USD |
| `7D` | `0.8710` | 26,700,000.00 USD | 0.00 USD | 26,700,000.00 USD | 604,760.00 USD | 169,010.00 USD | 362,510.00 USD |
| `1D` | `0.8720` | 10,960,000.00 USD | 0.00 USD | 10,960,000.00 USD | 211,980.00 USD | 63,580.00 USD | 201,290.00 USD |
| `7D` | `0.8730` | 25,560,000.00 USD | 0.00 USD | 25,560,000.00 USD | 333,320.00 USD | 199,340.00 USD | 215,150.00 USD |
| `1D` | `0.8740` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 43,750.00 USD | 20,320.00 USD | 21,570.00 USD |
| `7D` | `0.8750` | 24,810,000.00 USD | 0.00 USD | 24,810,000.00 USD | 643,630.00 USD | 230,460.00 USD | 324,670.00 USD |
| `1D` | `0.8760` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 76,420.00 USD | 73,290.00 USD | 141,460.00 USD |
| `7D` | `0.8770` | 23,610,000.00 USD | 0.00 USD | 23,610,000.00 USD | 399,330.00 USD | 184,560.00 USD | 420,350.00 USD |
| `1D` | `0.8780` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 64,740.00 USD | 48,670.00 USD | 31,790.00 USD |
| `7D` | `0.8790` | 22,610,000.00 USD | 0.00 USD | 22,610,000.00 USD | 312,210.00 USD | 124,520.00 USD | 221,400.00 USD |
| `1D` | `0.8800` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 13,090.00 USD | 11,350.00 USD | 44,060.00 USD |
| `7D` | `0.8810` | 21,950,000.00 USD | 0.00 USD | 21,950,000.00 USD | 641,660.00 USD | 159,780.00 USD | 487,390.00 USD |
| `1D` | `0.8820` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 108,450.00 USD | 63,180.00 USD | 145,270.00 USD |
| `7D` | `0.8830` | 20,660,000.00 USD | 0.00 USD | 20,660,000.00 USD | 783,040.00 USD | 270,900.00 USD | 529,050.00 USD |
| `1D` | `0.8840` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 303,250.00 USD | 65,530.00 USD | 151,790.00 USD |
| `7D` | `0.8850` | 19,080,000.00 USD | 0.00 USD | 19,080,000.00 USD | 519,370.00 USD | 265,360.00 USD | 259,150.00 USD |
| `1D` | `0.8860` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 273,240.00 USD | 127,160.00 USD | 87,550.00 USD |
| `7D` | `0.8870` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 649,180.00 USD | 279,830.00 USD | 511,220.00 USD |
| `1D` | `0.8880` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 324,630.00 USD | 224,670.00 USD | 540,230.00 USD |
| `7D` | `0.8890` | 16,600,000.00 USD | 0.00 USD | 16,600,000.00 USD | 1,550,000.00 USD | 530,540.00 USD | 1,160,000.00 USD |
| `1D` | `0.8900` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 524,630.00 USD | 171,920.00 USD | 548,630.00 USD |
| `7D` | `0.8910` | 13,360,000.00 USD | 0.00 USD | 13,360,000.00 USD | 818,970.00 USD | 471,140.00 USD | 681,670.00 USD |
| `1D` | `0.8920` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 235,610.00 USD | 49,510.00 USD | 114,860.00 USD |
| `7D` | `0.8930` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 1,790,000.00 USD | 646,070.00 USD | 1,040,000.00 USD |
| `1D` | `0.8940` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 167,880.00 USD | 130,550.00 USD | 281,620.00 USD |
| `7D` | `0.8950` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 771,020.00 USD | 443,450.00 USD | 829,660.00 USD |
| `1D` | `0.8960` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 149,410.00 USD | 148,110.00 USD | 187,930.00 USD |
| `7D` | `0.8970` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 673,010.00 USD | 276,920.00 USD | 492,850.00 USD |
| `1D` | `0.8980` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 120,980.00 USD | 57,070.00 USD | 76,150.00 USD |
| `7D` | `0.8990` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 322,820.00 USD | 147,390.00 USD | 897.80 USD |
| `1D` | `0.9000` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 53,800.00 USD | 24,210.00 USD | 40,460.00 USD |
| `7D` | `0.9010` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 130,380.00 USD | 15,640.00 USD | 6,170.00 USD |
| `1D` | `0.9020` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 49,680.00 USD | 79,010.00 USD | 191,650.00 USD |
| `7D` | `0.9030` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 5,880.00 USD | 50,720.00 USD | 146,360.00 USD |
| `1D` | `0.9040` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 128,110.00 USD | 81,940.00 USD | 139,050.00 USD |
| `7D` | `0.9050` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 122,230.00 USD | 0.00 USD | 46,500.00 USD |
| `1D` | `0.9060` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 215,300.00 USD | 10,170.00 USD | 58,470.00 USD |
| `7D` | `0.9070` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 341,080.00 USD | 19,890.00 USD | 127,760.00 USD |
| `1D` | `0.9080` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 248,490.00 USD | 116,800.00 USD | 213,650.00 USD |
| `7D` | `0.9090` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 53,970.00 USD | 0.00 USD | 128,660.00 USD |
| `1D` | `0.9100` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 174,550.00 USD | 32,520.00 USD | 153,690.00 USD |
| `7D` | `0.9110` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 212,760.00 USD | 106,160.00 USD | 35,810.00 USD |
| `1D` | `0.9120` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 211,640.00 USD | 39,820.00 USD | 204,180.00 USD |
| `7D` | `0.9130` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 80,230.00 USD | 95,530.00 USD | 166,660.00 USD |
| `1D` | `0.9140` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 172,190.00 USD | 87,890.00 USD | 109,160.00 USD |
| `7D` | `0.9150` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 111,690.00 USD | 26,360.00 USD | 38,020.00 USD |
| `1D` | `0.9160` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 32,680.00 USD | 25,880.00 USD | 10,460.00 USD |
| `7D` | `0.9170` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 123,530.00 USD | 0.00 USD | 37,740.00 USD |
| `1D` | `0.9180` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 154,870.00 USD | 9,020.00 USD | 46,150.00 USD |
| `7D` | `0.9190` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 257,890.00 USD | 23,790.00 USD | 0.00 USD |
| `1D` | `0.9200` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD |
| `7D` | `0.9210` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD |
| `1D` | `0.9220` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 32,990.00 USD | 39,420.00 USD | 133,380.00 USD |
| `7D` | `0.9230` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD |
| `1D` | `0.9240` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 170,280.00 USD | 58,320.00 USD | 150,050.00 USD |
| `7D` | `0.9250` | 768,980.00 USD | 0.00 USD | 768,980.00 USD | 52,570.00 USD | 41,710.00 USD | 0.00 USD |
| `1D` | `0.9260` | 804,700.00 USD | 0.00 USD | 804,700.00 USD | 125,460.00 USD | 28,360.00 USD | 0.00 USD |
| `7D` | `0.9270` | 674,690.00 USD | 0.00 USD | 674,690.00 USD | 209,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9280` | 650,880.00 USD | 0.00 USD | 650,880.00 USD | 31,930.00 USD | 80,990.00 USD | 11,800.00 USD |
| `7D` | `0.9290` | 464,750.00 USD | 0.00 USD | 464,750.00 USD | 0.00 USD | 78,940.00 USD | 0.00 USD |
| `1D` | `0.9300` | 526,160.00 USD | 0.00 USD | 526,160.00 USD | 82,700.00 USD | 110,920.00 USD | 166,780.00 USD |
| `7D` | `0.9310` | 385,810.00 USD | 0.00 USD | 385,810.00 USD | 177,720.00 USD | 29,170.00 USD | 0.00 USD |
| `1D` | `0.9320` | 165,760.00 USD | 0.00 USD | 165,760.00 USD | 100,660.00 USD | 0.00 USD | 13,720.00 USD |
| `1D` | `0.9340` | 51,380.00 USD | 0.00 USD | 51,380.00 USD | 0.00 USD | 0.00 USD | 51,380.00 USD |
| `1D` | `0.9350` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9350` | 178,920.00 USD | 0.00 USD | 178,920.00 USD | 50,160.00 USD | 52,710.00 USD | 76,050.00 USD |
| `1D` | `0.9360` | 152,670.00 USD | 152,670.00 USD | 0.00 USD | 0.00 USD | 39,480.00 USD | 113,190.00 USD |
| `7D` | `0.9360` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9370` | 293,700.00 USD | 293,700.00 USD | 0.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD |
| `1D` | `0.9380` | 811,120.00 USD | 811,120.00 USD | 0.00 USD | 246,090.00 USD | 118,850.00 USD | 293,510.00 USD |
| `7D` | `0.9390` | 673,150.00 USD | 673,150.00 USD | 0.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD |
| `1D` | `0.9400` | 930,660.00 USD | 930,660.00 USD | 0.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD |
| `7D` | `0.9410` | 796,150.00 USD | 796,150.00 USD | 0.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9430` | 858,240.00 USD | 858,240.00 USD | 0.00 USD | 0.00 USD | 62,100.00 USD | 0.00 USD |
| `1D` | `0.9440` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD |
| `7D` | `0.9450` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD |
| `1D` | `0.9460` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 28,980.00 USD | 160,460.00 USD |
| `7D` | `0.9470` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `1D` | `0.9480` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 50.92 USD |
| `7D` | `0.9490` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35,810.00 USD |
| `1D` | `0.9500` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 1,330.00 USD | 6,400.00 USD | 32,110.00 USD |
| `7D` | `0.9510` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 62,510.00 USD | 700,930.00 USD |
| `1D` | `0.9520` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 37,450.00 USD | 17,280.00 USD | 86,050.00 USD |
| `7D` | `0.9530` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD |
| `1D` | `0.9540` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 20,720.00 USD | 42,610.00 USD | 0.00 USD |
| `7D` | `0.9550` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 71,910.00 USD | 1,290.00 USD | 288.96 USD |
| `1D` | `0.9560` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 33,360.00 USD | 164.22 USD |
| `7D` | `0.9570` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 463,830.00 USD | 2,240.00 USD | 511.50 USD |
| `1D` | `0.9580` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 689.00 USD | 43,140.00 USD | 59.86 USD |
| `7D` | `0.9590` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 562,050.00 USD | 1,040.00 USD | 289.76 USD |
| `1D` | `0.9600` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 110,240.00 USD | 65,470.00 USD | 108,950.00 USD |
| `7D` | `0.9610` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 698,570.00 USD | 176,650.00 USD | 476,080.00 USD |
| `1D` | `0.9620` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 410,030.00 USD | 135,810.00 USD | 345,380.00 USD |
| `7D` | `0.9630` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 604,860.00 USD | 301,610.00 USD | 615,910.00 USD |
| `1D` | `0.9640` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 347,170.00 USD | 124,900.00 USD | 253,740.00 USD |
| `7D` | `0.9650` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 857,470.00 USD | 301,210.00 USD | 412,280.00 USD |
| `1D` | `0.9660` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 273,420.00 USD | 130,220.00 USD | 142,590.00 USD |
| `7D` | `0.9670` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 916,920.00 USD | 487,590.00 USD | 705,590.00 USD |
| `1D` | `0.9680` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 302,380.00 USD | 118,860.00 USD | 365,630.00 USD |
| `7D` | `0.9690` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 596,350.00 USD | 343,680.00 USD | 420,110.00 USD |
| `1D` | `0.9700` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 265,560.00 USD | 150,830.00 USD | 200,910.00 USD |
| `7D` | `0.9710` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 645,500.00 USD | 305,860.00 USD | 144,130.00 USD |
| `1D` | `0.9720` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 326,660.00 USD | 114,070.00 USD | 99,880.00 USD |
| `7D` | `0.9730` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 456,990.00 USD | 160,420.00 USD | 146,260.00 USD |
| `1D` | `0.9740` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 167,080.00 USD | 34,110.00 USD | 52,790.00 USD |
| `7D` | `0.9750` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 201,510.00 USD | 293,590.00 USD | 193,410.00 USD |
| `1D` | `0.9760` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 40,320.00 USD | 41,480.00 USD | 88,090.00 USD |
| `7D` | `0.9770` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 329,170.00 USD | 211,000.00 USD | 499,960.00 USD |
| `1D` | `0.9780` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 110,140.00 USD | 55,790.00 USD | 189,850.00 USD |
| `7D` | `0.9790` | 15,490,000.00 USD | 15,490,000.00 USD | 0.00 USD | 409,890.00 USD | 84,800.00 USD | 186,030.00 USD |
| `1D` | `0.9800` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 102,630.00 USD | 72,440.00 USD | 157,160.00 USD |
| `7D` | `0.9810` | 16,010,000.00 USD | 16,010,000.00 USD | 0.00 USD | 264,890.00 USD | 83,040.00 USD | 169,310.00 USD |
| `1D` | `0.9820` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 185,860.00 USD | 32,830.00 USD | 53,380.00 USD |
| `7D` | `0.9830` | 16,570,000.00 USD | 16,570,000.00 USD | 0.00 USD | 260,850.00 USD | 99,420.00 USD | 199,120.00 USD |
| `1D` | `0.9840` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 80,920.00 USD | 67,090.00 USD | 28,490.00 USD |
| `7D` | `0.9850` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD |
| `1D` | `0.9860` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 131,110.00 USD | 61,330.00 USD | 139,440.00 USD |
| `7D` | `0.9870` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 248,980.00 USD | 191,820.00 USD | 58,100.00 USD |
| `1D` | `0.9880` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 85,110.00 USD | 34,550.00 USD | 71,220.00 USD |
| `7D` | `0.9890` | 17,770,000.00 USD | 17,770,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 19,370.00 USD |
| `1D` | `0.9900` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 144,770.00 USD | 50,410.00 USD | 79,610.00 USD |
| `7D` | `0.9910` | 18,140,000.00 USD | 18,140,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD |
| `1D` | `0.9920` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 143,390.00 USD | 46,290.00 USD | 21,010.00 USD |
| `7D` | `0.9930` | 18,510,000.00 USD | 18,510,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 73,840.00 USD |
| `1D` | `0.9940` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 60,500.00 USD | 36,520.00 USD | 58,730.00 USD |
| `7D` | `0.9950` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 48,120.00 USD | 138,500.00 USD | 130,850.00 USD |
| `1D` | `0.9960` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 6,800.00 USD | 11,390.00 USD | 21,110.00 USD |
| `7D` | `0.9970` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD |
| `1D` | `0.9980` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 140,230.00 USD | 32,300.00 USD | 142,030.00 USD |
| `7D` | `0.9990` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD |
| `1D` | `1.00` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 19,510.00 USD | 17,530.00 USD | 6,150.00 USD |
| `7D` | `1.00` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 202,970.00 USD | 57,170.00 USD | 185,100.00 USD |
| `1D` | `1.00` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 12,840.00 USD | 18,430.00 USD | 20,620.00 USD |
| `7D` | `1.00` | 20,780,000.00 USD | 20,780,000.00 USD | 0.00 USD | 316,600.00 USD | 52,200.00 USD | 216,090.00 USD |
| `1D` | `1.00` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 17,620.00 USD | 13,280.00 USD | 22,390.00 USD |
| `7D` | `1.00` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 96,930.00 USD | 29,470.00 USD | 65,670.00 USD |
| `1D` | `1.01` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 9,900.00 USD | 14,230.00 USD | 11,290.00 USD |
| `7D` | `1.01` | 21,490,000.00 USD | 21,490,000.00 USD | 0.00 USD | 283,350.00 USD | 15,900.00 USD | 212,150.00 USD |
| `1D` | `1.01` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 19,520.00 USD | 9,720.00 USD | 12,630.00 USD |
| `7D` | `1.01` | 22,090,000.00 USD | 22,090,000.00 USD | 0.00 USD | 247,480.00 USD | 105,290.00 USD | 247,750.00 USD |
| `1D` | `1.01` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 13,150.00 USD | 5,570.00 USD | 8,570.00 USD |
| `7D` | `1.01` | 23,040,000.00 USD | 23,040,000.00 USD | 0.00 USD | 457,740.00 USD | 174,650.00 USD | 319,400.00 USD |
| `1D` | `1.01` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 21,660.00 USD | 13,820.00 USD | 34,420.00 USD |
| `7D` | `1.01` | 24,010,000.00 USD | 24,010,000.00 USD | 0.00 USD | 342,220.00 USD | 281,430.00 USD | 344,360.00 USD |
| `1D` | `1.01` | 9,400,000.00 USD | 9,400,000.00 USD | 0.00 USD | 13,360.00 USD | 11,680.00 USD | 26,070.00 USD |
| `7D` | `1.01` | 24,550,000.00 USD | 24,550,000.00 USD | 0.00 USD | 325,510.00 USD | 91,280.00 USD | 124,520.00 USD |
| `1D` | `1.02` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 23,240.00 USD | 15,330.00 USD | 19,220.00 USD |
| `7D` | `1.02` | 25,390,000.00 USD | 25,390,000.00 USD | 0.00 USD | 383,690.00 USD | 97,830.00 USD | 360,110.00 USD |
| `1D` | `1.02` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 23,270.00 USD | 3,970.00 USD | 4,610.00 USD |
| `7D` | `1.02` | 26,250,000.00 USD | 26,250,000.00 USD | 0.00 USD | 303,920.00 USD | 88,570.00 USD | 469,230.00 USD |
| `1D` | `1.02` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 36,260.00 USD | 16,330.00 USD | 56,500.00 USD |
| `7D` | `1.02` | 26,740,000.00 USD | 26,740,000.00 USD | 0.00 USD | 167,390.00 USD | 63,770.00 USD | 260,150.00 USD |
| `1D` | `1.02` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 55,590.00 USD | 4,130.00 USD | 22,550.00 USD |
| `7D` | `1.02` | 27,100,000.00 USD | 27,100,000.00 USD | 0.00 USD | 185,100.00 USD | 50,190.00 USD | 123,500.00 USD |
| `1D` | `1.02` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 29,960.00 USD | 7,690.00 USD | 28,240.00 USD |
| `7D` | `1.02` | 27,360,000.00 USD | 27,360,000.00 USD | 0.00 USD | 112,970.00 USD | 54,210.00 USD | 94,800.00 USD |
| `1D` | `1.03` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 23,940.00 USD | 16,440.00 USD | 22,110.00 USD |
| `7D` | `1.03` | 27,620,000.00 USD | 27,620,000.00 USD | 0.00 USD | 106,360.00 USD | 35,230.00 USD | 110,930.00 USD |
| `1D` | `1.03` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 6,330.00 USD | 0.00 USD | 4,950.00 USD |
| `7D` | `1.03` | 27,830,000.00 USD | 27,830,000.00 USD | 0.00 USD | 87,950.00 USD | 57,010.00 USD | 67,150.00 USD |
| `1D` | `1.03` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 4,130.00 USD | 10,320.00 USD | 10,170.00 USD |
| `7D` | `1.03` | 28,260,000.00 USD | 28,260,000.00 USD | 0.00 USD | 198,340.00 USD | 79,470.00 USD | 157,430.00 USD |
| `1D` | `1.03` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 21,900.00 USD | 11,130.00 USD | 5,690.00 USD |
| `7D` | `1.03` | 28,710,000.00 USD | 28,710,000.00 USD | 0.00 USD | 136,400.00 USD | 149,600.00 USD | 163,030.00 USD |
| `1D` | `1.03` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 16,600.00 USD | 19,650.00 USD | 47,050.00 USD |
| `7D` | `1.03` | 28,900,000.00 USD | 28,900,000.00 USD | 0.00 USD | 113,490.00 USD | 13,040.00 USD | 63,310.00 USD |
| `1D` | `1.04` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 26,990.00 USD | 18,830.00 USD | 49,210.00 USD |
| `7D` | `1.04` | 29,300,000.00 USD | 29,300,000.00 USD | 0.00 USD | 176,930.00 USD | 41,220.00 USD | 181,310.00 USD |
| `1D` | `1.04` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 59,260.00 USD | 7,020.00 USD | 16,600.00 USD |
| `7D` | `1.04` | 29,610,000.00 USD | 29,610,000.00 USD | 0.00 USD | 114,060.00 USD | 21,690.00 USD | 175,760.00 USD |
| `1D` | `1.04` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 8,210.00 USD | 7,840.00 USD | 8,100.00 USD |
| `7D` | `1.04` | 29,850,000.00 USD | 29,850,000.00 USD | 0.00 USD | 105,050.00 USD | 55,100.00 USD | 72,870.00 USD |
| `1D` | `1.04` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 21,580.00 USD | 18,300.00 USD | 6,940.00 USD |
| `7D` | `1.04` | 29,940,000.00 USD | 29,940,000.00 USD | 0.00 USD | 20,680.00 USD | 49,420.00 USD | 24,820.00 USD |
| `1D` | `1.04` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 19,660.00 USD | 8,720.00 USD | 41,490.00 USD |
| `7D` | `1.04` | 30,030,000.00 USD | 30,030,000.00 USD | 0.00 USD | 69,360.00 USD | 17,730.00 USD | 1,560.00 USD |
| `1D` | `1.05` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 25,330.00 USD | 17,080.00 USD | 25,240.00 USD |
| `7D` | `1.05` | 30,140,000.00 USD | 30,140,000.00 USD | 0.00 USD | 79,950.00 USD | 31,290.00 USD | 294.86 USD |
| `1D` | `1.05` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 53,350.00 USD | 10,090.00 USD | 14,690.00 USD |
| `7D` | `1.05` | 30,210,000.00 USD | 30,210,000.00 USD | 0.00 USD | 38,030.00 USD | 13,720.00 USD | 17,370.00 USD |
| `1D` | `1.05` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 12,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.05` | 30,240,000.00 USD | 30,240,000.00 USD | 0.00 USD | 23,320.00 USD | 0.00 USD | 538.06 USD |
| `1D` | `1.05` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 142.30 USD | 14,720.00 USD |
| `7D` | `1.05` | 30,320,000.00 USD | 30,320,000.00 USD | 0.00 USD | 8,370.00 USD | 47,690.00 USD | 28,430.00 USD |
| `1D` | `1.05` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 303.15 USD | 202.65 USD | 0.00 USD |
| `7D` | `1.05` | 30,370,000.00 USD | 30,370,000.00 USD | 0.00 USD | 3,770.00 USD | 5,360.00 USD | 46,120.00 USD |
| `1D` | `1.06` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 11,980.00 USD | 4,220.00 USD | 5,600.00 USD |
| `7D` | `1.06` | 30,390,000.00 USD | 30,390,000.00 USD | 0.00 USD | 6,580.00 USD | 3,950.00 USD | 197.80 USD |
| `7D` | `1.06` | 30,390,000.00 USD | 30,390,000.00 USD | 0.00 USD | 1,110.00 USD | 194.87 USD | 59.76 USD |
| `7D` | `1.06` | 30,420,000.00 USD | 30,420,000.00 USD | 0.00 USD | 17,530.00 USD | 3,870.00 USD | 12,060.00 USD |
| `7D` | `1.06` | 30,430,000.00 USD | 30,430,000.00 USD | 0.00 USD | 10,210.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `628.64M` | Total OI Tokens: `667,494,057.7 SUI`
  * 1h OI Change: `-0.53%` | 4h OI Change: `+0.76%` | 24h OI Change: `+0.96%`
  * Exchange Breakdown: Binance=`121.81M` | Bybit=`84.06M` | OKX=`34.40M` | Hyperliquid=`32.93M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `22.89K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0094%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0084%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `53.41%` | `46.59%` | `1.15` | 8,590,000.00 USD |
| `15M` | `Binance` | `47.42%` | `52.58%` | `0.90` | 3,180,000.00 USD |
| `15M` | `OKX` | `53.69%` | `46.31%` | `1.16` | 975,060.00 USD |
| `15M` | `Bybit` | `34.53%` | `65.47%` | `0.53` | 1,200,000.00 USD |
| `15M` | `KuCoin` | `49.66%` | `50.34%` | `0.99` | 64,100.00 USD |
| `15M` | `Gate` | `60.11%` | `39.89%` | `1.51` | 232,810.00 USD |
| `15M` | `Bitget` | `62.62%` | `37.38%` | `1.68` | 314,640.00 USD |
| `15M` | `BingX` | `62.77%` | `37.23%` | `1.69` | 332,870.00 USD |
| `15M` | `MEXC` | `46.38%` | `53.62%` | `0.86` | 689,060.00 USD |
| `15M` | `Bitunix` | `74.52%` | `25.48%` | `2.92` | 606,170.00 USD |
| `15M` | `Hyperliquid` | `91.68%` | `8.32%` | `11.02` | 506,080.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.73%` | `49.27%` | `1.03` | 55,580.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `71.33%` | `28.67%` | `2.49` | 351,980.00 USD |
| `15M` | `HTX` | `99.62%` | `0.38%` | `262.16` | 2,450.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `60.92%` | `39.08%` | `1.56` | 73,380.00 USD |
| `15M` | `Aster` | `72%` | `28%` | `2.57` | 2,130.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `4.95%` | `95.05%` | `0.05` | 674.64 USD |
| `15M` | `Whale Positions` | `47.42%` | `52.58%` | `0.90` | 3,180,000.00 USD |
| `15M` | `Global Accounts` | `53.41%` | `46.59%` | `1.15` | 8,590,000.00 USD |
| `1H` | `SUI` | `46.64%` | `53.36%` | `0.87` | 37,340,000.00 USD |
| `1H` | `Binance` | `46.13%` | `53.87%` | `0.86` | 13,050,000.00 USD |
| `1H` | `OKX` | `39.11%` | `60.89%` | `0.64` | 4,520,000.00 USD |
| `1H` | `Bybit` | `44.23%` | `55.77%` | `0.79` | 6,190,000.00 USD |
| `1H` | `KuCoin` | `51.61%` | `48.39%` | `1.07` | 442,620.00 USD |
| `1H` | `Gate` | `52.15%` | `47.85%` | `1.09` | 947,120.00 USD |
| `1H` | `Bitget` | `49.7%` | `50.3%` | `0.99` | 2,080,000.00 USD |
| `1H` | `BingX` | `40.8%` | `59.2%` | `0.69` | 1,270,000.00 USD |
| `1H` | `MEXC` | `47.1%` | `52.9%` | `0.89` | 3,370,000.00 USD |
| `1H` | `Bitunix` | `58.82%` | `41.18%` | `1.43` | 1,660,000.00 USD |
| `1H` | `Hyperliquid` | `46.1%` | `53.9%` | `0.86` | 1,720,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `36.13%` | `63.87%` | `0.57` | 316,220.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `68.47%` | `31.53%` | `2.17` | 1,310,000.00 USD |
| `1H` | `HTX` | `50.7%` | `49.3%` | `1.03` | 31,730.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `60.79%` | `39.21%` | `1.55` | 347,460.00 USD |
| `1H` | `Aster` | `13.06%` | `86.94%` | `0.15` | 72,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `61.52%` | `38.48%` | `1.60` | 23,330.00 USD |
| `1H` | `Whale Positions` | `46.13%` | `53.87%` | `0.86` | 13,050,000.00 USD |
| `1H` | `Global Accounts` | `46.64%` | `53.36%` | `0.87` | 37,340,000.00 USD |
| `4H` | `SUI` | `47.92%` | `52.08%` | `0.92` | 170,590,000.00 USD |
| `4H` | `Binance` | `48.93%` | `51.07%` | `0.96` | 61,700,000.00 USD |
| `4H` | `OKX` | `45.48%` | `54.52%` | `0.83` | 25,950,000.00 USD |
| `4H` | `Bybit` | `47.18%` | `52.82%` | `0.89` | 22,380,000.00 USD |
| `4H` | `KuCoin` | `49.69%` | `50.31%` | `0.99` | 2,290,000.00 USD |
| `4H` | `Gate` | `49.78%` | `50.22%` | `0.99` | 4,760,000.00 USD |
| `4H` | `Bitget` | `48.89%` | `51.11%` | `0.96` | 8,570,000.00 USD |
| `4H` | `BingX` | `48.53%` | `51.47%` | `0.94` | 6,760,000.00 USD |
| `4H` | `MEXC` | `44.71%` | `55.29%` | `0.81` | 18,160,000.00 USD |
| `4H` | `Bitunix` | `52.09%` | `47.91%` | `1.09` | 6,150,000.00 USD |
| `4H` | `Hyperliquid` | `47.11%` | `52.89%` | `0.89` | 4,790,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.57%` | `52.43%` | `0.91` | 1,190,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `60.29%` | `39.71%` | `1.52` | 4,840,000.00 USD |
| `4H` | `HTX` | `48.43%` | `51.57%` | `0.94` | 228,870.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.76%` | `64.24%` | `0.56` | 2,260,000.00 USD |
| `4H` | `Aster` | `40.2%` | `59.8%` | `0.67` | 354,250.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.18%` | `58.82%` | `0.70` | 223,160.00 USD |
| `4H` | `Whale Positions` | `48.93%` | `51.07%` | `0.96` | 61,700,000.00 USD |
| `4H` | `Global Accounts` | `47.92%` | `52.08%` | `0.92` | 170,590,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9523` | `0.9521` | `0.9523` | `0.9548` | `0.9486` | 2,922,269.66 USD | 1,453,739.73 USD | 1,468,529.93 USD | -14,790.20 USD | `-0.51%` | `10B / 8S` |
| `0:00 UTC` | `0.9600` | `0.9565` | `0.9600` | `0.9617` | `0.9503` | 6,416,225.57 USD | 3,530,243.57 USD | 2,885,982.00 USD | 644,261.57 USD | `+10.04%` | `18B / 17S` |
| `5:00 UTC` | `0.9485` | `0.9509` | `0.9485` | `0.9584` | `0.9476` | 4,295,336.29 USD | 1,504,736.83 USD | 2,790,599.46 USD | -1,285,862.63 USD | `-29.94%` | `4B / 41S` |
| `0:00 UTC` | `0.9476` | `0.9462` | `0.9476` | `0.9495` | `0.9425` | 3,274,884.41 USD | 1,392,018.83 USD | 1,882,865.59 USD | -490,846.76 USD | `-14.99%` | `3B / 22S` |
| `5:00 UTC` | `0.9473` | `0.9468` | `0.9473` | `0.9484` | `0.9444` | 1,455,719.43 USD | 672,614.86 USD | 783,104.57 USD | -110,489.71 USD | `-7.59%` | `4B / 16S` |
| `0:00 UTC` | `0.9443` | `0.9448` | `0.9443` | `0.9482` | `0.9416` | 1,894,016.62 USD | 669,877.01 USD | 1,224,139.61 USD | -554,262.60 USD | `-29.26%` | `2B / 19S` |
| `5:00 UTC` | `0.9422` | `0.9426` | `0.9422` | `0.9456` | `0.9405` | 2,904,363.37 USD | 1,710,904.86 USD | 1,193,458.51 USD | 517,446.35 USD | `+17.82%` | `9B / 3S` |
| `0:00 UTC` | `0.9365` | `0.9385` | `0.9365` | `0.9465` | `0.9328` | 3,456,784.57 USD | 1,287,230.60 USD | 2,169,553.97 USD | -882,323.36 USD | `-25.52%` | `11B / 45S` |
| `5:00 UTC` | `0.9311` | `0.9327` | `0.9311` | `0.9364` | `0.9283` | 4,003,241.44 USD | 1,917,706.18 USD | 2,085,535.26 USD | -167,829.08 USD | `-4.19%` | `12B / 10S` |
| `0:00 UTC` | `0.9367` | `0.9357` | `0.9367` | `0.9373` | `0.9335` | 812,559.61 USD | 279,572.84 USD | 532,986.77 USD | -253,413.93 USD | `-31.19%` | `1B / 11S` |

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
| `5m` | 12,130.00 USD | -77,680.00 USD | **`DISTRIBUTION`** |
| `15m` | 180,500.00 USD | -459,650.00 USD | **`DISTRIBUTION`** |
| `30m` | -206,110.00 USD | -3,210,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 183,880.00 USD | -2,650,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,000,000.00 USD | -6,750,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 4,810,000.00 USD | -5,520,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 4,700,000.00 USD | -3,740,000.00 USD | **`ACCUMULATION`** |
| `8h` | 4,530,000.00 USD | -5,240,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 5,110,000.00 USD | -3,970,000.00 USD | **`ACCUMULATION`** |
| `24h` | 5,030,000.00 USD | -15,690,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -13,900,000.00 USD | -65,190,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -141,850,000.00 USD | -464,780,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+12.13K` | 15m=`+180.50K` | 1h=`+183.88K` | 24h=`+5.03M`
* Futures Capital Netflows: 5m=`-77.68K` | 15m=`-459.65K` | 1h=`-2.65M` | 24h=`-15.69M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
