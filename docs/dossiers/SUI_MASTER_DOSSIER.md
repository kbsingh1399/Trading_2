# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:11:09 IST` (`2026-10-30 05:41:09 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.9021` | `0.9031` | `0.9007` | `0.9014` | `742,353` | 669,569.55 USD | -78,989.05 USD | `-11.80%` | -12,851,445.42 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.9013` | `0.9019` | `0.9000` | `0.9007` | `746,898` | 672,797.15 USD | -103,494.11 USD | `-15.38%` | -12,954,939.53 USD | `-0.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9007` | `0.9020` | `0.8986` | `0.9005` | `705,225` | 634,670.89 USD | -155,548.98 USD | `-24.51%` | -13,110,488.51 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8945` | `0.9049` | `0.8940` | `0.9024` | `8,094,812` | 7,284,926.68 USD | -365,499.52 USD | `-5.02%` | -12,555,852.82 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9024` | `0.9031` | `0.9000` | `0.9007` | `2,598,793` | 2,342,731.18 USD | -205,719.11 USD | `-8.78%` | -12,761,571.93 USD | `-0.78` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9007` | `0.9020` | `0.8986` | `0.9002` | `689,469` | 620,486.82 USD | -165,628.33 USD | `-26.69%` | -12,927,200.26 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.8661` | `0.8873` | `0.8656` | `0.8841` | `13,301,873` | 11,663,934.28 USD | 1,975,651.91 USD | `+16.94%` | -11,594,640.69 USD | `+1.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.8841` | `0.8966` | `0.8777` | `0.8946` | `15,840,652` | 14,060,418.53 USD | -340,237.43 USD | `-2.42%` | -11,934,878.12 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8945` | `0.9049` | `0.8940` | `0.9005` | `11,398,830` | 10,262,328.75 USD | -726,767.61 USD | `-7.08%` | -12,661,645.73 USD | `-0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.9002` | `27,223,727` | 24,308,563.20 USD | -1,077,084.39 USD | `-4.43%` | -13,399,422.35 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | 1,889,481.85 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -683,829.84 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.9002` | `27,223,727` | 24,308,563.20 USD | -1,077,084.39 USD | `-4.43%` | -13,399,422.35 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `0.8999` | `1971.0000` | 1,773.72 USD | 39,337.40 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.9000` | `83.3000` | 74.97 USD | 31,244.93 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.9000` | `1662.9000` | 1,496.64 USD | 32,741.58 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.9000` | `4111.0000` | 3,699.78 USD | 36,441.35 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.9000` | `1247.1000` | 1,122.33 USD | 37,563.68 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.9001` | `1662.9000` | 1,496.76 USD | 31,169.96 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9002` | `1797.9000` | 1,618.56 USD | 9,435.96 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.9002` | `135.0000` | 121.53 USD | 9,557.50 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9002` | `190.0000` | 171.04 USD | 9,728.54 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.9002` | `5904.7000` | 5,315.53 USD | 15,044.07 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `0.9002` | `5720.7000` | 5,149.83 USD | 20,193.90 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.9002` | `135.0000` | 121.53 USD | 20,315.43 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9002` | `689.9000` | 621.04 USD | 20,936.47 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.9002` | `2488.3000` | 2,239.92 USD | 23,176.39 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9002` | `7217.4000` | 6,496.81 USD | 29,673.20 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.9003` | `5564.5000` | 5,009.89 USD | 6,077.19 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9003` | `1662.9000` | 1,497.14 USD | 7,574.33 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9003` | `135.0000` | 121.54 USD | 7,695.87 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9003` | `135.0000` | 121.54 USD | 7,817.40 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9004` | `1185.3000` | 1,067.30 USD | 1,067.30 USD | `1 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `0.9005` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.90` | `0.00%` | `-` |
| `ASK` | `0.9006` | `1196.1000` | 1,077.24 USD | 1,077.24 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9007` | `1663.1000` | 1,497.94 USD | 3,652.47 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9007` | `1196.1000` | 1,077.29 USD | 2,154.53 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9008` | `3325.6000` | 2,995.80 USD | 11,224.17 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9008` | `90.7000` | 81.70 USD | 8,228.37 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9008` | `3326.2000` | 2,996.14 USD | 8,146.67 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9008` | `1663.1000` | 1,498.05 USD | 5,150.53 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9009` | `400.0000` | 360.38 USD | 13,282.48 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9009` | `110.9000` | 99.91 USD | 12,922.10 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9009` | `1773.8000` | 1,598.02 USD | 12,822.19 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.9010` | `1662.9000` | 1,498.34 USD | 27,000.02 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.9010` | `6026.4000` | 5,429.97 USD | 25,501.68 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `0.9010` | `5561.4000` | 5,010.82 USD | 20,071.72 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9010` | `1662.8000` | 1,498.13 USD | 15,060.90 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9010` | `110.9000` | 99.92 USD | 13,562.76 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9010` | `200.2000` | 180.37 USD | 13,462.85 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9011` | `1246.3000` | 1,123.04 USD | 29,697.31 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.9011` | `500.0000` | 450.54 USD | 28,574.27 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.9011` | `1247.1000` | 1,123.70 USD | 28,123.72 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.9012` | `1110.1000` | 1,000.37 USD | 30,697.68 USD | `1 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `661` | `0xb83d...6e36` | `SHORT` | 3,435,237.64 USD | `3,817,609.40` | `1.11` | `0.9002` | `33.71` | 783,497.67 USD | `+22.81%` | `3X Cross` |
| `991` | `0xa2ce...3126` | `LONG` | 2,249,609.36 USD | `2,500,010.40` | `0.8597` | `0.9002` | `0.000000` | 100,402.83 USD | `+4.46%` | `10X Cross` |
| `1542` | `0x9946...0852` | `SHORT` | 1,401,146.53 USD | `1,557,106.30` | `1.07` | `0.9000` | `1.84` | 257,531.27 USD | `+18.38%` | `10X Cross` |
| `1888` | `0x9df2...c665` | `SHORT` | 1,079,808.00 USD | `1,200,000.00` | `0.7465` | `0.9000` | `25.64` | -183,955.60 USD | `-17.04%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9026` | 47.30 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.05K USD at 0.9026 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `0.9026` | 11.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.01K USD at 0.9026 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `0.9026` | 227.27 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.23K USD at 0.9026 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `0.8977` | 97.67 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.10K USD at 0.8977 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `0.8977` | 370.32 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.37K USD at 0.8977 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `0.9010` | 5,006.50 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9010 USD [API] | `2026-10-29 02:44:07` |
| `ANNOUNCEMENT` | `INFO` | `0.9048` | 5,070.15 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.07K USD at 0.9048 USD [API] | `2026-10-29 03:18:13` |
| `ANNOUNCEMENT` | `INFO` | `0.9038` | 5,341.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9038 USD [API] | `2026-10-29 04:14:26` |
| `ANNOUNCEMENT` | `INFO` | `0.9014` | 853.20 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.85K USD at 0.9014 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `0.9013` | 1,980.18 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.98K USD at 0.9013 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `0.9014` | 1,001.32 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.00K USD at 0.9014 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `0.9024` | 1,001.35 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.00K USD at 0.9024 USD [API] | `2026-10-29 07:17:06` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9069` (Vol: 414,400.00 USD, Dist: `+0.85%`) | Long MP=`0.8716` (Vol: 414,400.00 USD, Dist: `--3.08%`)
  * 48H Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+0.92%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--3.12%`)
  * 3D Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+0.92%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--3.12%`)
  * 7D Horizon: Short MP=`0.9682` (Vol: 687,400.00 USD, Dist: `+7.66%`) | Long MP=`0.8711` (Vol: 414,400.00 USD, Dist: `--3.14%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1855` | 695.40 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 1,820.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 439.89 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 131.06 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 3,390.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,630.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 2,540.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 158.57 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 1,020.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 32,580.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 25,020.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 3,670.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,450.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3055` | 611.12 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3165` | 104.73 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3315` | 3,310.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3425` | 9,750.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 5,070.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3555` | 27,620.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3685` | 668.05 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3735` | 416.49 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3805` | 6,470.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3835` | 268.45 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3875` | 1,940.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3885` | 4,860.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 3,360.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4085` | 28,820.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 8,270.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4245` | 1,220.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 43,880.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 529.45 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 105.25 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4505` | 381.93 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 1,020.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 3,330.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4725` | 5,180.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 166.70 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 4,040.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 926.34 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 8,550.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 544.71 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 5,570.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 7,080.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 298.31 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 4,140.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 106.04 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 1,070.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5235` | 124.02 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 123,640.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 279.86 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 113.47 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5365` | 7,830.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 126.46 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 7,610.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 34,760.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 798.56 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 441.84 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 534.03 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,370.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 7,200.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5715` | 263.98 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 110,080.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 217.37 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 6,670.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 225.93 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,760.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 608.61 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5975` | 4,360.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 299.25 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 4,760.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 323.79 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6035` | 1,220.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 14,900.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 886.10 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6095` | 214.54 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6105` | 2,750.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,280.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 438.73 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 112.33 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 2,110.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,980.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 12,570.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 2,400.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 708.53 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,070.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 416.70 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 1,100.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 843.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 1,100.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 33,040.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 4,980.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,380.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 9,810.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 668.34 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 344.82 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 106.75 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6525` | 2,350.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 2,840.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 7,890.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 1,830.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 7,070.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 2,600.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 97,590.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 528.73 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 2,260.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 135.71 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 337.36 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,470.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 2,450.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 28,290.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 854.64 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 189.22 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 9,150.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 122.94 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 43,650.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 2,110.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 17,190.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 15,130.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,960.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 6,110.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 1,060.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 10,590.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 3,600.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 7,670.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,700.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,030.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 4,830.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 8,970.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 287.84 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 143.14 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 3,620.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,020.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 823.37 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 25,230.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 283.22 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 927.55 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 297.23 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 441,770.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 4,620.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7185` | 126.96 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 420.19 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 8,450.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,940.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 127.05 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7245` | 2,520.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 311.60 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 11,790.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 35,890.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 424.86 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 13,500.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 11,890.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 6,240.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7350` | 15,120,000.00 USD | 15,120,000.00 USD | 69,900.00 USD | 26,690.00 USD | 51,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7370` | 14,970,000.00 USD | 14,970,000.00 USD | 38,700.00 USD | 17,190.00 USD | 32,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7375` | 3,450.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,020.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7390` | 14,880,000.00 USD | 14,880,000.00 USD | 27,490.00 USD | 24,560.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7410` | 14,800,000.00 USD | 14,800,000.00 USD | 18,820.00 USD | 8,780.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 2,280.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7430` | 14,740,000.00 USD | 14,740,000.00 USD | 44,520.00 USD | 5,210.00 USD | 33,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7435` | 784,400.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7450` | 14,660,000.00 USD | 14,660,000.00 USD | 34,130.00 USD | 21,270.00 USD | 43,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7455` | 4,020.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7465` | 359.96 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7470` | 14,560,000.00 USD | 14,560,000.00 USD | 23,010.00 USD | 19,630.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7490` | 14,500,000.00 USD | 14,500,000.00 USD | 26,370.00 USD | 12,290.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7495` | 4,820.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7510` | 14,450,000.00 USD | 14,450,000.00 USD | 10,970.00 USD | 16,630.00 USD | 21,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7530` | 14,400,000.00 USD | 14,400,000.00 USD | 1,690.00 USD | 654.10 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7535` | 264.86 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 1,250.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7550` | 14,390,000.00 USD | 14,390,000.00 USD | 8,700.00 USD | 6,530.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7555` | 1,750.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7570` | 14,360,000.00 USD | 14,360,000.00 USD | 22,280.00 USD | 16,160.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7590` | 14,320,000.00 USD | 14,320,000.00 USD | 6,840.00 USD | 25,130.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,900.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 2,920.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7610` | 14,280,000.00 USD | 14,280,000.00 USD | 21,310.00 USD | 16,580.00 USD | 630.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7625` | 859.11 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 14,250,000.00 USD | 14,250,000.00 USD | 20,690.00 USD | 118.70 USD | 573.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 5,550.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 3,510.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 14,220,000.00 USD | 14,220,000.00 USD | 556.58 USD | 23,090.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,260.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 14,190,000.00 USD | 14,190,000.00 USD | 1,280.00 USD | 3,960.00 USD | 18,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 25,580.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 207.19 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 14,170,000.00 USD | 14,170,000.00 USD | 182.28 USD | 161.63 USD | 3,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 150,510.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 14,160,000.00 USD | 14,160,000.00 USD | 7,690.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,940.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 325,060.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 3,430.00 USD | 793,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 3,510.00 USD | 789,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 786,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 5,390.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 758,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7810` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 185.50 USD | 5,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 757,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 3,930.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 21,760.00 USD | 753,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7850` | 14,130,000.00 USD | 14,130,000.00 USD | 7,790.00 USD | 20,370.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 731,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 25,170.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 728,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7890` | 8,400,000.00 USD | 8,400,000.00 USD | 46,190.00 USD | 26,370.00 USD | 9,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 14,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 7,440.00 USD | 728,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7910` | 8,320,000.00 USD | 8,320,000.00 USD | 9,770.00 USD | 12,270.00 USD | 8,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 14,050,000.00 USD | 14,050,000.00 USD | 6,610.00 USD | 24,700.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 7,620.00 USD | 720,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 10,810.00 USD | 712,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7930` | 8,290,000.00 USD | 8,290,000.00 USD | 9,370.00 USD | 21,610.00 USD | 45,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 12,880.00 USD | 67,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 702,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7945` | 736.66 USD | 701,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7950` | 8,210,000.00 USD | 8,210,000.00 USD | 24,110.00 USD | 11,950.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 13,930,000.00 USD | 13,930,000.00 USD | 2,210.00 USD | 20,100.00 USD | 62,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 52,610.00 USD | 700,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7965` | 12,980.00 USD | 648,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 8,140,000.00 USD | 8,140,000.00 USD | 17,740.00 USD | 14,480.00 USD | 56,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 13,850,000.00 USD | 13,850,000.00 USD | 26,700.00 USD | 3,570.00 USD | 63,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,580.00 USD | 635,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7985` | 40,230.00 USD | 627,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7990` | 8,050,000.00 USD | 8,050,000.00 USD | 9,910.00 USD | 10,360.00 USD | 18,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 13,750,000.00 USD | 13,750,000.00 USD | 8,560.00 USD | 2,220.00 USD | 26,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 7,590.00 USD | 587,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8005` | 3,620.00 USD | 579,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8010` | 8,010,000.00 USD | 8,010,000.00 USD | 31,970.00 USD | 10,940.00 USD | 16,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 13,720,000.00 USD | 13,720,000.00 USD | 43,340.00 USD | 14,760.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 7,500.00 USD | 576,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 4,920.00 USD | 568,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8030` | 7,950,000.00 USD | 7,950,000.00 USD | 588.76 USD | 1,660.00 USD | 141.89 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,680.00 USD | 563,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 16,770.00 USD | 555,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8050` | 7,950,000.00 USD | 7,950,000.00 USD | 56,980.00 USD | 30,020.00 USD | 22,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 13,620,000.00 USD | 13,620,000.00 USD | 10,860.00 USD | 19,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 361.11 USD | 539,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 538,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 7,840,000.00 USD | 7,840,000.00 USD | 32,120.00 USD | 22,690.00 USD | 69,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 13,590,000.00 USD | 13,590,000.00 USD | 5,030.00 USD | 11,280.00 USD | 1,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 531,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,510.00 USD | 529,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8090` | 7,720,000.00 USD | 7,720,000.00 USD | 3,120.00 USD | 10,080.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 130,110.00 USD | 506,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 376,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8110` | 7,700,000.00 USD | 7,700,000.00 USD | 3,580.00 USD | 2,810.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 13,560,000.00 USD | 13,560,000.00 USD | 61,670.00 USD | 8,310.00 USD | 44,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,970.00 USD | 374,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8125` | 1,160.00 USD | 371,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8130` | 7,690,000.00 USD | 7,690,000.00 USD | 20,250.00 USD | 2,010.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 13,450,000.00 USD | 13,450,000.00 USD | 45,800.00 USD | 19,710.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 370,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 366,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 7,640,000.00 USD | 7,640,000.00 USD | 59,890.00 USD | 22,200.00 USD | 101,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 13,370,000.00 USD | 13,370,000.00 USD | 139,680.00 USD | 51,810.00 USD | 172,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 38,250.00 USD | 366,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8165` | 104.92 USD | 327,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8170` | 7,460,000.00 USD | 7,460,000.00 USD | 136,090.00 USD | 19,460.00 USD | 115,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 13,010,000.00 USD | 13,010,000.00 USD | 91,050.00 USD | 25,080.00 USD | 77,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 77,840.00 USD | 327,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8185` | 25,070.00 USD | 249,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8190` | 7,190,000.00 USD | 7,190,000.00 USD | 34,660.00 USD | 5,600.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 12,820,000.00 USD | 12,820,000.00 USD | 200,250.00 USD | 53,380.00 USD | 49,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,230.00 USD | 224,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8205` | 7,960.00 USD | 223,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8210` | 7,130,000.00 USD | 7,130,000.00 USD | 107,660.00 USD | 87,200.00 USD | 130,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 12,510,000.00 USD | 12,510,000.00 USD | 138,580.00 USD | 80,040.00 USD | 199,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 474.01 USD | 215,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8225` | 2,890.00 USD | 215,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 6,800,000.00 USD | 6,800,000.00 USD | 74,120.00 USD | 11,200.00 USD | 142,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 12,090,000.00 USD | 12,090,000.00 USD | 44,590.00 USD | 40,420.00 USD | 63,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 463.63 USD | 212,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8245` | 18,980.00 USD | 211,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 6,580,000.00 USD | 6,580,000.00 USD | 28,040.00 USD | 4,970.00 USD | 47,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 11,950,000.00 USD | 11,950,000.00 USD | 198,230.00 USD | 30,370.00 USD | 124,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 1,580.00 USD | 192,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8270` | 6,500,000.00 USD | 6,500,000.00 USD | 58,700.00 USD | 30,530.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 11,590,000.00 USD | 11,590,000.00 USD | 147,770.00 USD | 53,560.00 USD | 60,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 191,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 186,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8290` | 6,380,000.00 USD | 6,380,000.00 USD | 25,760.00 USD | 12,310.00 USD | 46,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 11,330,000.00 USD | 11,330,000.00 USD | 94,690.00 USD | 42,420.00 USD | 84,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 46,590.00 USD | 66,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8310` | 6,300,000.00 USD | 6,300,000.00 USD | 5,540.00 USD | 30,230.00 USD | 30,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 11,110,000.00 USD | 11,110,000.00 USD | 36,870.00 USD | 32,050.00 USD | 111,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 6,230,000.00 USD | 6,230,000.00 USD | 8,810.00 USD | 29,570.00 USD | 89,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 10,930,000.00 USD | 10,930,000.00 USD | 157,210.00 USD | 105,720.00 USD | 197,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8345` | 5,750.00 USD | 19,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8350` | 6,100,000.00 USD | 6,100,000.00 USD | 155,620.00 USD | 35,340.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 10,470,000.00 USD | 10,470,000.00 USD | 117,940.00 USD | 16,770.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8370` | 5,880,000.00 USD | 5,880,000.00 USD | 64,460.00 USD | 9,500.00 USD | 127,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 10,250,000.00 USD | 10,250,000.00 USD | 140,480.00 USD | 109,700.00 USD | 140,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 327.21 USD | 14,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8385` | 7,300.00 USD | 13,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8390` | 5,680,000.00 USD | 5,680,000.00 USD | 67,860.00 USD | 57,980.00 USD | 49,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 9,860,000.00 USD | 9,860,000.00 USD | 30,810.00 USD | 160,930.00 USD | 164,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 1,440.00 USD | 6,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8410` | 5,500,000.00 USD | 5,500,000.00 USD | 19,770.00 USD | 25,270.00 USD | 77,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 9,500,000.00 USD | 9,500,000.00 USD | 91,790.00 USD | 34,400.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 134.47 USD | 5,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8425` | 4,130.00 USD | 4,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 5,380,000.00 USD | 5,380,000.00 USD | 89,750.00 USD | 66,490.00 USD | 27,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 9,350,000.00 USD | 9,350,000.00 USD | 67,920.00 USD | 123,520.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 5,200,000.00 USD | 5,200,000.00 USD | 72,050.00 USD | 74,720.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 9,150,000.00 USD | 9,150,000.00 USD | 34,560.00 USD | 102,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 745.82 USD | 745.82 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8470` | 5,040,000.00 USD | 5,040,000.00 USD | 51,620.00 USD | 100,260.00 USD | 25,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 9,010,000.00 USD | 9,010,000.00 USD | 44,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 4,860,000.00 USD | 4,860,000.00 USD | 48,890.00 USD | 87,320.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 8,960,000.00 USD | 8,960,000.00 USD | 64,910.00 USD | 69,480.00 USD | 135,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8510` | 4,580,000.00 USD | 4,580,000.00 USD | 53,320.00 USD | 132,930.00 USD | 148,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 8,690,000.00 USD | 8,690,000.00 USD | 155,060.00 USD | 72,120.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 4,250,000.00 USD | 4,250,000.00 USD | 153,840.00 USD | 156,860.00 USD | 96,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 8,470,000.00 USD | 8,470,000.00 USD | 215,880.00 USD | 17,300.00 USD | 54,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 3,840,000.00 USD | 3,840,000.00 USD | 1,920.00 USD | 17,460.00 USD | 485.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 8,180,000.00 USD | 8,180,000.00 USD | 78,320.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 19,770.00 USD | 46,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 8,090,000.00 USD | 8,090,000.00 USD | 99,680.00 USD | 55,310.00 USD | 39,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 3,760,000.00 USD | 3,760,000.00 USD | 46,710.00 USD | 60,770.00 USD | 49,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 7,900,000.00 USD | 7,900,000.00 USD | 132,610.00 USD | 56,980.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 3,600,000.00 USD | 3,600,000.00 USD | 79,530.00 USD | 23,780.00 USD | 224.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 7,700,000.00 USD | 7,700,000.00 USD | 36,870.00 USD | 188,190.00 USD | 32,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 3,500,000.00 USD | 3,500,000.00 USD | 91,300.00 USD | 124,490.00 USD | 124,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 7,450,000.00 USD | 7,450,000.00 USD | 100,980.00 USD | 64,400.00 USD | 387,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8650` | 3,150,000.00 USD | 3,150,000.00 USD | 28,850.00 USD | 52,640.00 USD | 112,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 6,890,000.00 USD | 6,890,000.00 USD | 254,940.00 USD | 106,760.00 USD | 564,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8670` | 2,960,000.00 USD | 2,960,000.00 USD | 212,100.00 USD | 25,640.00 USD | 180,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 5,970,000.00 USD | 5,970,000.00 USD | 252,430.00 USD | 0.00 USD | 128,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 2,540,000.00 USD | 2,540,000.00 USD | 27,920.00 USD | 0.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 109,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 2,490,000.00 USD | 2,490,000.00 USD | 152,210.00 USD | 100,950.00 USD | 176,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 5,480,000.00 USD | 5,480,000.00 USD | 207,250.00 USD | 34,600.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 2,060,000.00 USD | 2,060,000.00 USD | 85,660.00 USD | 0.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 87,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 117,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 5,140,000.00 USD | 5,140,000.00 USD | 26,230.00 USD | 0.00 USD | 257,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,840,000.00 USD | 1,840,000.00 USD | 27,620.00 USD | 20,280.00 USD | 122,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,670,000.00 USD | 1,670,000.00 USD | 79,990.00 USD | 0.00 USD | 1,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,580,000.00 USD | 1,580,000.00 USD | 41,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 4,850,000.00 USD | 4,850,000.00 USD | 20,310.00 USD | 3,570.00 USD | 576.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 2,260.00 USD | 94,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 25,990.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,450,000.00 USD | 1,450,000.00 USD | 30,450.00 USD | 0.00 USD | 24,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 35,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 1,390,000.00 USD | 1,390,000.00 USD | 122,200.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 4,750,000.00 USD | 4,750,000.00 USD | 8,820.00 USD | 3,860.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 1,270,000.00 USD | 1,270,000.00 USD | 138,820.00 USD | 0.00 USD | 61,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 4,730,000.00 USD | 4,730,000.00 USD | 523,470.00 USD | 55,310.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 1,070,000.00 USD | 1,070,000.00 USD | 69,970.00 USD | 18,820.00 USD | 208.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 4,150,000.00 USD | 4,150,000.00 USD | 1,750,000.00 USD | 0.00 USD | 728.40 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 977,420.00 USD | 977,420.00 USD | 134,710.00 USD | 99,420.00 USD | 975.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 2,400,000.00 USD | 2,400,000.00 USD | 800,940.00 USD | 68,760.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8965` | 187.46 USD | 187.46 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8970` | 742,310.00 USD | 742,310.00 USD | 969.20 USD | 58,730.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 1,530,000.00 USD | 1,530,000.00 USD | 634,760.00 USD | 93,070.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 681,330.00 USD | 681,330.00 USD | 143,990.00 USD | 181,310.00 USD | 356,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 786,750.00 USD | 786,750.00 USD | 379,180.00 USD | 67,360.00 USD | 340,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9010` | 328,070.00 USD | 328,070.00 USD | 170,400.00 USD | 156,270.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 681,560.00 USD | 681,560.00 USD | 207,550.00 USD | 97,520.00 USD | 376,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9030` | 477,810.00 USD | 477,810.00 USD | 8,120.00 USD | 140,180.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9030` | 1,010,000.00 USD | 1,010,000.00 USD | 124,030.00 USD | 99,390.00 USD | 106,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9050` | 928,680.00 USD | 928,680.00 USD | 243,190.00 USD | 162,620.00 USD | 45,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9050` | 1,500,000.00 USD | 1,500,000.00 USD | 169,680.00 USD | 0.00 USD | 323,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9070` | 1,730,000.00 USD | 1,730,000.00 USD | 303,340.00 USD | 227,560.00 USD | 274,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 2,180,000.00 USD | 2,180,000.00 USD | 548,330.00 USD | 85,530.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9090` | 1,970,000.00 USD | 1,970,000.00 USD | 190,800.00 USD | 28,990.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 2,560,000.00 USD | 2,560,000.00 USD | 60,680.00 USD | 142,850.00 USD | 179,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9110` | 2,160,000.00 USD | 2,160,000.00 USD | 90,400.00 USD | 46,460.00 USD | 50,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 3,000,000.00 USD | 3,000,000.00 USD | 259,120.00 USD | 103,750.00 USD | 71,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9130` | 2,480,000.00 USD | 2,480,000.00 USD | 78,640.00 USD | 106,560.00 USD | 135,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 3,170,000.00 USD | 3,170,000.00 USD | 80,230.00 USD | 86,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 4,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9150` | 3,140,000.00 USD | 3,140,000.00 USD | 233,130.00 USD | 113,310.00 USD | 315,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 3,560,000.00 USD | 3,560,000.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9170` | 3,480,000.00 USD | 3,480,000.00 USD | 124,750.00 USD | 127,130.00 USD | 89,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 3,730,000.00 USD | 3,730,000.00 USD | 163,880.00 USD | 2,050.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9190` | 3,710,000.00 USD | 3,710,000.00 USD | 75,990.00 USD | 41,040.00 USD | 106,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 4,350,000.00 USD | 4,350,000.00 USD | 296,480.00 USD | 86,790.00 USD | 238,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9195` | 9,200.00 USD | 13,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9210` | 4,110,000.00 USD | 4,110,000.00 USD | 129,450.00 USD | 67,170.00 USD | 211,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 4,730,000.00 USD | 4,730,000.00 USD | 194,470.00 USD | 18,660.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9230` | 4,730,000.00 USD | 4,730,000.00 USD | 236,260.00 USD | 88,490.00 USD | 288,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 5,260,000.00 USD | 5,260,000.00 USD | 56,540.00 USD | 68,150.00 USD | 398,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9235` | 209.36 USD | 13,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9250` | 5,260,000.00 USD | 5,260,000.00 USD | 265,410.00 USD | 90,560.00 USD | 171,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 5,550,000.00 USD | 5,550,000.00 USD | 158,890.00 USD | 63,010.00 USD | 69,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9270` | 5,430,000.00 USD | 5,430,000.00 USD | 3,590.00 USD | 103,030.00 USD | 64,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 5,910,000.00 USD | 5,910,000.00 USD | 220,880.00 USD | 46,830.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9290` | 5,600,000.00 USD | 5,600,000.00 USD | 43,130.00 USD | 23,020.00 USD | 104,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 6,000,000.00 USD | 6,000,000.00 USD | 4,480.00 USD | 53,740.00 USD | 38,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9310` | 5,890,000.00 USD | 5,890,000.00 USD | 123,440.00 USD | 75,260.00 USD | 93,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 6,400,000.00 USD | 6,400,000.00 USD | 181,630.00 USD | 50,140.00 USD | 168,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9330` | 6,040,000.00 USD | 6,040,000.00 USD | 75,580.00 USD | 39,640.00 USD | 35,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 6,550,000.00 USD | 6,550,000.00 USD | 4,410.00 USD | 76,570.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 6,060,000.00 USD | 6,060,000.00 USD | 2,160.00 USD | 16,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 6,660,000.00 USD | 6,660,000.00 USD | 53,950.00 USD | 55,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9365` | 8,170.00 USD | 21,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9370` | 6,450,000.00 USD | 6,450,000.00 USD | 128,220.00 USD | 71,160.00 USD | 190,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 6,980,000.00 USD | 6,980,000.00 USD | 256,610.00 USD | 18,150.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 39,850.00 USD | 61,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9390` | 6,650,000.00 USD | 6,650,000.00 USD | 54,270.00 USD | 11,160.00 USD | 140,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 7,370,000.00 USD | 7,370,000.00 USD | 86,850.00 USD | 36,340.00 USD | 266,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9405` | 352.88 USD | 62,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9410` | 6,790,000.00 USD | 6,790,000.00 USD | 60,820.00 USD | 14,850.00 USD | 58,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 7,490,000.00 USD | 7,490,000.00 USD | 123,000.00 USD | 6,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 6,820,000.00 USD | 6,820,000.00 USD | 1,630.00 USD | 3,360.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 7,600,000.00 USD | 7,600,000.00 USD | 4,970.00 USD | 68,030.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9450` | 7,060,000.00 USD | 7,060,000.00 USD | 9,780.00 USD | 36,750.00 USD | 190,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 7,940,000.00 USD | 7,940,000.00 USD | 3,360.00 USD | 244,270.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 7,250,000.00 USD | 7,250,000.00 USD | 93,380.00 USD | 56,310.00 USD | 44,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 7,440,000.00 USD | 7,440,000.00 USD | 72,890.00 USD | 62,860.00 USD | 58,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 7,730,000.00 USD | 7,730,000.00 USD | 60,880.00 USD | 50,330.00 USD | 175,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 9,210,000.00 USD | 9,210,000.00 USD | 2,840.00 USD | 88,970.00 USD | 734,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 7,940,000.00 USD | 7,940,000.00 USD | 32,110.00 USD | 26,880.00 USD | 150,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 8,080,000.00 USD | 8,080,000.00 USD | 48,260.00 USD | 40,160.00 USD | 52,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 9,340,000.00 USD | 9,340,000.00 USD | 74,980.00 USD | 2,400.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 8,160,000.00 USD | 8,160,000.00 USD | 36,890.00 USD | 13,960.00 USD | 23,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 9,820,000.00 USD | 9,820,000.00 USD | 463,830.00 USD | 4,720.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 8,280,000.00 USD | 8,280,000.00 USD | 44,640.00 USD | 69,890.00 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 10,410,000.00 USD | 10,410,000.00 USD | 563,790.00 USD | 21,410.00 USD | 3,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 8,810,000.00 USD | 8,810,000.00 USD | 207,550.00 USD | 76,640.00 USD | 244,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 11,790,000.00 USD | 11,790,000.00 USD | 698,570.00 USD | 201,530.00 USD | 480,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 9,160,000.00 USD | 9,160,000.00 USD | 241,720.00 USD | 43,610.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 13,290,000.00 USD | 13,290,000.00 USD | 579,300.00 USD | 301,610.00 USD | 624,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 9,500,000.00 USD | 9,500,000.00 USD | 145,180.00 USD | 112,750.00 USD | 79,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 14,870,000.00 USD | 14,870,000.00 USD | 857,470.00 USD | 312,610.00 USD | 408,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 10,070,000.00 USD | 10,070,000.00 USD | 230,840.00 USD | 111,230.00 USD | 233,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 16,840,000.00 USD | 16,840,000.00 USD | 801,890.00 USD | 555,340.00 USD | 616,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 10,650,000.00 USD | 10,650,000.00 USD | 244,130.00 USD | 85,700.00 USD | 241,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 18,150,000.00 USD | 18,150,000.00 USD | 596,350.00 USD | 312,990.00 USD | 398,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 11,010,000.00 USD | 11,010,000.00 USD | 173,950.00 USD | 66,390.00 USD | 123,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 19,270,000.00 USD | 19,270,000.00 USD | 647,710.00 USD | 319,140.00 USD | 146,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 11,160,000.00 USD | 11,160,000.00 USD | 61,720.00 USD | 37,940.00 USD | 50,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 20,080,000.00 USD | 20,080,000.00 USD | 456,990.00 USD | 160,420.00 USD | 192,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 11,350,000.00 USD | 11,350,000.00 USD | 32,420.00 USD | 30,100.00 USD | 128,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 20,820,000.00 USD | 20,820,000.00 USD | 227,380.00 USD | 293,590.00 USD | 223,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 11,400,000.00 USD | 11,400,000.00 USD | 4,790.00 USD | 11,480.00 USD | 32,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 21,890,000.00 USD | 21,890,000.00 USD | 329,170.00 USD | 211,000.00 USD | 524,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 11,580,000.00 USD | 11,580,000.00 USD | 46,560.00 USD | 32,950.00 USD | 103,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 22,520,000.00 USD | 22,520,000.00 USD | 342,340.00 USD | 72,140.00 USD | 223,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 63,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 11,780,000.00 USD | 11,780,000.00 USD | 87,820.00 USD | 31,320.00 USD | 75,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 22,960,000.00 USD | 22,960,000.00 USD | 206,910.00 USD | 60,620.00 USD | 166,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 11,860,000.00 USD | 11,860,000.00 USD | 62,950.00 USD | 22,530.00 USD | 47.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 23,540,000.00 USD | 23,540,000.00 USD | 262,900.00 USD | 116,030.00 USD | 200,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 11,940,000.00 USD | 11,940,000.00 USD | 21,080.00 USD | 42,480.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 23,950,000.00 USD | 23,950,000.00 USD | 234,160.00 USD | 58,210.00 USD | 117,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 63,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9870` | 12,140,000.00 USD | 12,140,000.00 USD | 72,760.00 USD | 30,670.00 USD | 97,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 24,460,000.00 USD | 24,460,000.00 USD | 248,980.00 USD | 203,100.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 67,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9890` | 12,310,000.00 USD | 12,310,000.00 USD | 100,210.00 USD | 31,480.00 USD | 34,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 24,750,000.00 USD | 24,750,000.00 USD | 194,850.00 USD | 78,280.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 12,400,000.00 USD | 12,400,000.00 USD | 40,670.00 USD | 24,540.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 25,120,000.00 USD | 25,120,000.00 USD | 198,890.00 USD | 89,640.00 USD | 84,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9915` | 1,570.00 USD | 69,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9930` | 12,440,000.00 USD | 12,440,000.00 USD | 20,890.00 USD | 3,890.00 USD | 16,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 25,490,000.00 USD | 25,490,000.00 USD | 228,340.00 USD | 63,950.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 69,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9950` | 12,550,000.00 USD | 12,550,000.00 USD | 36,320.00 USD | 19,930.00 USD | 54,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 25,800,000.00 USD | 25,800,000.00 USD | 48,120.00 USD | 138,500.00 USD | 125,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 12,700,000.00 USD | 12,700,000.00 USD | 36,450.00 USD | 11,490.00 USD | 103,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 26,450,000.00 USD | 26,450,000.00 USD | 215,040.00 USD | 81,210.00 USD | 360,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 12,840,000.00 USD | 12,840,000.00 USD | 61,500.00 USD | 8,720.00 USD | 65,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 26,740,000.00 USD | 26,740,000.00 USD | 145,170.00 USD | 35,870.00 USD | 101,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 27,180,000.00 USD | 27,180,000.00 USD | 202,970.00 USD | 57,170.00 USD | 183,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 69,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 27,680,000.00 USD | 27,680,000.00 USD | 226,340.00 USD | 61,540.00 USD | 206,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 27,830,000.00 USD | 27,830,000.00 USD | 51,930.00 USD | 39,560.00 USD | 66,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 28,140,000.00 USD | 28,140,000.00 USD | 168,320.00 USD | 16,800.00 USD | 121,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 28,610,000.00 USD | 28,610,000.00 USD | 247,480.00 USD | 61,720.00 USD | 157,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 29,060,000.00 USD | 29,060,000.00 USD | 301,110.00 USD | 84,080.00 USD | 62,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 29,540,000.00 USD | 29,540,000.00 USD | 188,370.00 USD | 121,340.00 USD | 171,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 705.99 USD | 70,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 29,890,000.00 USD | 29,890,000.00 USD | 168,660.00 USD | 60,680.00 USD | 126,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 70,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 30,370,000.00 USD | 30,370,000.00 USD | 148,890.00 USD | 62,970.00 USD | 266,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 30,840,000.00 USD | 30,840,000.00 USD | 180,470.00 USD | 47,380.00 USD | 243,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 31,110,000.00 USD | 31,110,000.00 USD | 95,590.00 USD | 18,960.00 USD | 149,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 31,420,000.00 USD | 31,420,000.00 USD | 151,650.00 USD | 61,120.00 USD | 103,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 31,620,000.00 USD | 31,620,000.00 USD | 59,440.00 USD | 54,210.00 USD | 78,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 31,810,000.00 USD | 31,810,000.00 USD | 76,740.00 USD | 35,970.00 USD | 82,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 31,950,000.00 USD | 31,950,000.00 USD | 85,920.00 USD | 34,530.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 32,140,000.00 USD | 32,140,000.00 USD | 119,110.00 USD | 33,520.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 32,350,000.00 USD | 32,350,000.00 USD | 57,570.00 USD | 75,720.00 USD | 76,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 32,490,000.00 USD | 32,490,000.00 USD | 64,880.00 USD | 13,040.00 USD | 63,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 32,720,000.00 USD | 32,720,000.00 USD | 79,670.00 USD | 20,460.00 USD | 134,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 32,840,000.00 USD | 32,840,000.00 USD | 53,800.00 USD | 0.00 USD | 63,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 155.92 USD | 70,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,720.00 USD | 72,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 73,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 75,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 79,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 84,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 84,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 85,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 8,940.00 USD | 94,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 117,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 118,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 129.88 USD | 118,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 177.65 USD | 118,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 122,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 383.01 USD | 123,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 123,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 3,930.00 USD | 127,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 1,230.00 USD | 128,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 131,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 133,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 9,760.00 USD | 143,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 183,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 183,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 183,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 184,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 216,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 228.36 USD | 216,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 222,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,100.00 USD | 223,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 245,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 252,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 22,980.00 USD | 275,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 634,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.38` | 135.66 USD | 634,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 638,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 639,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 639,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 16,770.00 USD | 656,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 660,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 152.95 USD | 660,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 9,940.00 USD | 670,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 670,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 670,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,180.00 USD | 671,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 123.81 USD | 671,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,130.00 USD | 673,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 138.45 USD | 673,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 694,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 3,940.00 USD | 698,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 3,620.00 USD | 702,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,140.00 USD | 741,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 2,280.00 USD | 743,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 150.02 USD | 743,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 296,470.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 9,670.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 495.77 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 982.50 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 20,830.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 87,070.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 7,040.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 782.21 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 134.32 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1855` | 4,700,000.00 USD | 0.00 USD | 695.40 USD | `-79.27%` | `3,748.80` |
| `Live` | `Long` | `0.1955` | 4,700,000.00 USD | 0.00 USD | 1,820.00 USD | `-78.16%` | `9,320.00` |
| `Live` | `Long` | `0.1995` | 4,700,000.00 USD | 0.00 USD | 256.00 USD | `-77.71%` | `1,283.20` |
| `Live` | `Long` | `0.2055` | 4,700,000.00 USD | 0.00 USD | 439.89 USD | `-77.04%` | `2,140.60` |
| `Live` | `Long` | `0.2135` | 4,700,000.00 USD | 0.00 USD | 4,040.00 USD | `-76.15%` | `18,919.90` |
| `Live` | `Long` | `0.2195` | 4,690,000.00 USD | 0.00 USD | 131.06 USD | `-75.47%` | `597.10` |
| `Live` | `Long` | `0.2225` | 4,690,000.00 USD | 0.00 USD | 3,390.00 USD | `-75.14%` | `15,245.00` |
| `Live` | `Long` | `0.2355` | 4,690,000.00 USD | 0.00 USD | 789.66 USD | `-73.69%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,690,000.00 USD | 0.00 USD | 156.36 USD | `-73.35%` | `655.60` |
| `Live` | `Long` | `0.2425` | 4,690,000.00 USD | 0.00 USD | 1,630.00 USD | `-72.91%` | `6,725.00` |
| `Live` | `Long` | `0.2505` | 4,690,000.00 USD | 0.00 USD | 2,540.00 USD | `-72.01%` | `10,152.10` |
| `Live` | `Long` | `0.2525` | 4,680,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.79%` | `8,897.00` |
| `Live` | `Long` | `0.2565` | 4,680,000.00 USD | 0.00 USD | 158.57 USD | `-71.34%` | `618.20` |
| `Live` | `Long` | `0.2625` | 4,680,000.00 USD | 0.00 USD | 1,020.00 USD | `-70.67%` | `3,885.50` |
| `Live` | `Long` | `0.2685` | 4,680,000.00 USD | 0.00 USD | 106.16 USD | `-70.00%` | `395.40` |
| `Live` | `Long` | `0.2735` | 4,680,000.00 USD | 0.00 USD | 248.34 USD | `-69.44%` | `908.00` |
| `Live` | `Long` | `0.2885` | 4,680,000.00 USD | 0.00 USD | 32,580.00 USD | `-67.77%` | `112,944.40` |
| `Live` | `Long` | `0.2905` | 4,650,000.00 USD | 0.00 USD | 25,020.00 USD | `-67.54%` | `86,117.40` |
| `Live` | `Long` | `0.2955` | 4,620,000.00 USD | 0.00 USD | 3,670.00 USD | `-66.98%` | `12,426.00` |
| `Live` | `Long` | `0.2975` | 4,620,000.00 USD | 0.00 USD | 4,450.00 USD | `-66.76%` | `14,970.70` |
| `Live` | `Long` | `0.3055` | 4,610,000.00 USD | 0.00 USD | 611.12 USD | `-65.87%` | `2,000.40` |
| `Live` | `Long` | `0.3115` | 4,610,000.00 USD | 0.00 USD | 270.38 USD | `-65.20%` | `868.00` |
| `Live` | `Long` | `0.3165` | 4,610,000.00 USD | 0.00 USD | 104.73 USD | `-64.64%` | `330.90` |
| `Live` | `Long` | `0.3315` | 4,610,000.00 USD | 0.00 USD | 3,310.00 USD | `-62.96%` | `10,000.00` |
| `Live` | `Long` | `0.3425` | 4,610,000.00 USD | 0.00 USD | 9,750.00 USD | `-61.73%` | `28,480.20` |
| `Live` | `Long` | `0.3465` | 4,600,000.00 USD | 0.00 USD | 5,070.00 USD | `-61.28%` | `14,633.20` |
| `Live` | `Long` | `0.3505` | 4,590,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.84%` | `2,908.00` |
| `Live` | `Long` | `0.3555` | 4,590,000.00 USD | 0.00 USD | 27,620.00 USD | `-60.28%` | `77,706.40` |
| `Live` | `Long` | `0.3585` | 4,570,000.00 USD | 0.00 USD | 595.72 USD | `-59.94%` | `1,661.70` |
| `Live` | `Long` | `0.3665` | 4,570,000.00 USD | 0.00 USD | 274.88 USD | `-59.05%` | `750.00` |
| `Live` | `Long` | `0.3685` | 4,570,000.00 USD | 0.00 USD | 668.05 USD | `-58.83%` | `1,812.90` |
| `Live` | `Long` | `0.3735` | 4,560,000.00 USD | 0.00 USD | 416.49 USD | `-58.27%` | `1,115.10` |
| `Live` | `Long` | `0.3795` | 4,560,000.00 USD | 0.00 USD | 278.02 USD | `-57.60%` | `732.60` |
| `Live` | `Long` | `0.3805` | 4,560,000.00 USD | 0.00 USD | 6,470.00 USD | `-57.49%` | `17,000.00` |
| `Live` | `Long` | `0.3835` | 4,560,000.00 USD | 0.00 USD | 268.45 USD | `-57.15%` | `700.00` |
| `Live` | `Long` | `0.3845` | 4,560,000.00 USD | 0.00 USD | 1,750.00 USD | `-57.04%` | `4,562.20` |
| `Live` | `Long` | `0.3875` | 4,560,000.00 USD | 0.00 USD | 1,940.00 USD | `-56.70%` | `5,000.00` |
| `Live` | `Long` | `0.3885` | 4,550,000.00 USD | 0.00 USD | 4,860.00 USD | `-56.59%` | `12,500.00` |
| `Live` | `Long` | `0.3895` | 4,550,000.00 USD | 0.00 USD | 2,980.00 USD | `-56.48%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 4,550,000.00 USD | 0.00 USD | 5,030.00 USD | `-56.15%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,540,000.00 USD | 0.00 USD | 754.48 USD | `-55.92%` | `1,912.50` |
| `Live` | `Long` | `0.4035` | 4,540,000.00 USD | 0.00 USD | 935.03 USD | `-54.92%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,540,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.80%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,530,000.00 USD | 0.00 USD | 3,360.00 USD | `-54.58%` | `8,275.50` |
| `Live` | `Long` | `0.4085` | 4,530,000.00 USD | 0.00 USD | 28,820.00 USD | `-54.36%` | `70,547.40` |
| `Live` | `Long` | `0.4135` | 4,500,000.00 USD | 0.00 USD | 8,270.00 USD | `-53.80%` | `20,000.00` |
| `Live` | `Long` | `0.4245` | 4,490,000.00 USD | 0.00 USD | 1,220.00 USD | `-52.57%` | `2,865.90` |
| `Live` | `Long` | `0.4385` | 4,490,000.00 USD | 0.00 USD | 122.91 USD | `-51.01%` | `280.30` |
| `Live` | `Long` | `0.4405` | 4,490,000.00 USD | 0.00 USD | 43,880.00 USD | `-50.78%` | `99,611.70` |
| `Live` | `Long` | `0.4435` | 4,450,000.00 USD | 0.00 USD | 529.45 USD | `-50.45%` | `1,193.80` |
| `Live` | `Long` | `0.4455` | 4,450,000.00 USD | 0.00 USD | 574.83 USD | `-50.22%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,450,000.00 USD | 0.00 USD | 19,600.00 USD | `-50.11%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,430,000.00 USD | 0.00 USD | 105.25 USD | `-50.00%` | `235.20` |
| `Live` | `Long` | `0.4505` | 4,430,000.00 USD | 0.00 USD | 381.93 USD | `-49.66%` | `847.80` |
| `Live` | `Long` | `0.4535` | 4,430,000.00 USD | 0.00 USD | 1,020.00 USD | `-49.33%` | `2,246.80` |
| `Live` | `Long` | `0.4595` | 4,430,000.00 USD | 0.00 USD | 3,330.00 USD | `-48.66%` | `7,245.50` |
| `Live` | `Long` | `0.4725` | 4,420,000.00 USD | 0.00 USD | 5,180.00 USD | `-47.21%` | `10,957.60` |
| `Live` | `Long` | `0.4785` | 4,420,000.00 USD | 0.00 USD | 110.10 USD | `-46.54%` | `230.10` |
| `Live` | `Long` | `0.4825` | 4,420,000.00 USD | 0.00 USD | 166.70 USD | `-46.09%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,420,000.00 USD | 0.00 USD | 4,040.00 USD | `-45.98%` | `8,345.80` |
| `Live` | `Long` | `0.4865` | 4,410,000.00 USD | 0.00 USD | 201.07 USD | `-45.64%` | `413.30` |
| `Live` | `Long` | `0.4885` | 4,410,000.00 USD | 0.00 USD | 926.34 USD | `-45.42%` | `1,896.30` |
| `Live` | `Long` | `0.4895` | 4,410,000.00 USD | 0.00 USD | 105.34 USD | `-45.31%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,410,000.00 USD | 0.00 USD | 8,550.00 USD | `-45.08%` | `17,392.10` |
| `Live` | `Long` | `0.4925` | 4,400,000.00 USD | 0.00 USD | 544.71 USD | `-44.97%` | `1,106.00` |
| `Live` | `Long` | `0.4935` | 4,400,000.00 USD | 0.00 USD | 5,570.00 USD | `-44.86%` | `11,290.30` |
| `Live` | `Long` | `0.4945` | 4,400,000.00 USD | 0.00 USD | 106.32 USD | `-44.75%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,400,000.00 USD | 0.00 USD | 211.88 USD | `-44.64%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,400,000.00 USD | 0.00 USD | 216.75 USD | `-44.30%` | `434.80` |
| `Live` | `Long` | `0.5015` | 4,400,000.00 USD | 0.00 USD | 212.49 USD | `-43.97%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,400,000.00 USD | 0.00 USD | 1,230.00 USD | `-43.85%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 4,390,000.00 USD | 0.00 USD | 211.25 USD | `-43.52%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,390,000.00 USD | 0.00 USD | 7,080.00 USD | `-43.18%` | `13,915.60` |
| `Live` | `Long` | `0.5095` | 4,390,000.00 USD | 0.00 USD | 298.31 USD | `-43.07%` | `585.50` |
| `Live` | `Long` | `0.5145` | 4,390,000.00 USD | 0.00 USD | 4,140.00 USD | `-42.51%` | `8,054.90` |
| `Live` | `Long` | `0.5155` | 4,380,000.00 USD | 0.00 USD | 106.04 USD | `-42.40%` | `205.70` |
| `Live` | `Long` | `0.5165` | 4,380,000.00 USD | 0.00 USD | 619.80 USD | `-42.29%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,380,000.00 USD | 0.00 USD | 1,070.00 USD | `-42.18%` | `2,073.10` |
| `Live` | `Long` | `0.5185` | 4,380,000.00 USD | 0.00 USD | 121.74 USD | `-42.07%` | `234.80` |
| `Live` | `Long` | `0.5235` | 4,380,000.00 USD | 0.00 USD | 124.02 USD | `-41.51%` | `236.90` |
| `Live` | `Long` | `0.5275` | 4,380,000.00 USD | 0.00 USD | 348.36 USD | `-41.06%` | `660.40` |
| `Live` | `Long` | `0.5295` | 4,380,000.00 USD | 0.00 USD | 123,640.00 USD | `-40.84%` | `233,498.70` |
| `Live` | `Long` | `0.5325` | 4,260,000.00 USD | 0.00 USD | 2,680.00 USD | `-40.50%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,250,000.00 USD | 0.00 USD | 279.86 USD | `-40.28%` | `523.60` |
| `Live` | `Long` | `0.5355` | 4,250,000.00 USD | 0.00 USD | 113.47 USD | `-40.17%` | `211.90` |
| `Live` | `Long` | `0.5365` | 4,250,000.00 USD | 0.00 USD | 7,830.00 USD | `-40.06%` | `14,603.90` |
| `Live` | `Long` | `0.5395` | 4,250,000.00 USD | 0.00 USD | 126.46 USD | `-39.72%` | `234.40` |
| `Live` | `Long` | `0.5405` | 4,250,000.00 USD | 0.00 USD | 7,090.00 USD | `-39.61%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,240,000.00 USD | 0.00 USD | 269.13 USD | `-39.39%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,240,000.00 USD | 0.00 USD | 7,610.00 USD | `-39.16%` | `13,975.00` |
| `Live` | `Long` | `0.5465` | 4,230,000.00 USD | 0.00 USD | 272.87 USD | `-38.94%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,230,000.00 USD | 0.00 USD | 1,240.00 USD | `-38.83%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,230,000.00 USD | 0.00 USD | 34,760.00 USD | `-38.60%` | `63,254.80` |
| `Live` | `Long` | `0.5505` | 4,190,000.00 USD | 0.00 USD | 798.56 USD | `-38.49%` | `1,450.60` |
| `Live` | `Long` | `0.5515` | 4,190,000.00 USD | 0.00 USD | 160.93 USD | `-38.38%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,190,000.00 USD | 0.00 USD | 582.56 USD | `-38.27%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,190,000.00 USD | 0.00 USD | 271.88 USD | `-38.16%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,190,000.00 USD | 0.00 USD | 531.60 USD | `-38.04%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,190,000.00 USD | 0.00 USD | 7,950.00 USD | `-37.93%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,180,000.00 USD | 0.00 USD | 141.97 USD | `-37.60%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,180,000.00 USD | 0.00 USD | 304.93 USD | `-37.49%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,180,000.00 USD | 0.00 USD | 441.84 USD | `-37.37%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,180,000.00 USD | 0.00 USD | 330.53 USD | `-37.15%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,180,000.00 USD | 0.00 USD | 534.03 USD | `-37.04%` | `947.70` |
| `Live` | `Long` | `0.5655` | 4,180,000.00 USD | 0.00 USD | 8,370.00 USD | `-36.82%` | `14,800.00` |
| `Live` | `Long` | `0.5665` | 4,170,000.00 USD | 0.00 USD | 7,200.00 USD | `-36.70%` | `12,714.00` |
| `Live` | `Long` | `0.5675` | 4,170,000.00 USD | 0.00 USD | 1,560.00 USD | `-36.59%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,170,000.00 USD | 0.00 USD | 973.22 USD | `-36.37%` | `1,708.90` |
| `Live` | `Long` | `0.5715` | 4,160,000.00 USD | 0.00 USD | 263.98 USD | `-36.15%` | `461.90` |
| `Live` | `Long` | `0.5725` | 4,160,000.00 USD | 0.00 USD | 139.23 USD | `-36.03%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,160,000.00 USD | 0.00 USD | 110,080.00 USD | `-35.92%` | `191,935.60` |
| `Live` | `Long` | `0.5745` | 4,050,000.00 USD | 0.00 USD | 144.03 USD | `-35.81%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,050,000.00 USD | 0.00 USD | 217.37 USD | `-35.70%` | `377.70` |
| `Live` | `Long` | `0.5765` | 4,050,000.00 USD | 0.00 USD | 1,150.00 USD | `-35.59%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,050,000.00 USD | 0.00 USD | 497.75 USD | `-35.47%` | `861.90` |
| `Live` | `Long` | `0.5795` | 4,050,000.00 USD | 0.00 USD | 212.85 USD | `-35.25%` | `367.30` |
| `Live` | `Long` | `0.5805` | 4,050,000.00 USD | 0.00 USD | 1,410.00 USD | `-35.14%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,050,000.00 USD | 0.00 USD | 6,470.00 USD | `-34.92%` | `11,099.00` |
| `Live` | `Long` | `0.5845` | 4,040,000.00 USD | 0.00 USD | 6,670.00 USD | `-34.69%` | `11,411.10` |
| `Live` | `Long` | `0.5855` | 4,040,000.00 USD | 0.00 USD | 2,640.00 USD | `-34.58%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,030,000.00 USD | 0.00 USD | 466.85 USD | `-34.47%` | `796.00` |
| `Live` | `Long` | `0.5885` | 4,030,000.00 USD | 0.00 USD | 311.14 USD | `-34.25%` | `528.70` |
| `Live` | `Long` | `0.5905` | 4,030,000.00 USD | 0.00 USD | 225.93 USD | `-34.02%` | `382.60` |
| `Live` | `Long` | `0.5925` | 4,030,000.00 USD | 0.00 USD | 994.16 USD | `-33.80%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,030,000.00 USD | 0.00 USD | 132.41 USD | `-33.69%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,030,000.00 USD | 0.00 USD | 8,760.00 USD | `-33.58%` | `14,738.60` |
| `Live` | `Long` | `0.5965` | 4,020,000.00 USD | 0.00 USD | 608.61 USD | `-33.35%` | `1,020.30` |
| `Live` | `Long` | `0.5975` | 4,020,000.00 USD | 0.00 USD | 4,360.00 USD | `-33.24%` | `7,291.60` |
| `Live` | `Long` | `0.5985` | 4,020,000.00 USD | 0.00 USD | 299.25 USD | `-33.13%` | `500.00` |
| `Live` | `Long` | `0.5995` | 4,020,000.00 USD | 0.00 USD | 4,760.00 USD | `-33.02%` | `7,936.80` |
| `Live` | `Long` | `0.6005` | 4,010,000.00 USD | 0.00 USD | 351.11 USD | `-32.91%` | `584.70` |
| `Live` | `Long` | `0.6015` | 4,010,000.00 USD | 0.00 USD | 323.79 USD | `-32.79%` | `538.30` |
| `Live` | `Long` | `0.6025` | 4,010,000.00 USD | 0.00 USD | 432.35 USD | `-32.68%` | `717.60` |
| `Live` | `Long` | `0.6035` | 4,010,000.00 USD | 0.00 USD | 1,220.00 USD | `-32.57%` | `2,023.70` |
| `Live` | `Long` | `0.6075` | 4,010,000.00 USD | 0.00 USD | 14,900.00 USD | `-32.12%` | `24,525.20` |
| `Live` | `Long` | `0.6085` | 4,000,000.00 USD | 0.00 USD | 886.10 USD | `-32.01%` | `1,456.20` |
| `Live` | `Long` | `0.6095` | 4,000,000.00 USD | 0.00 USD | 214.54 USD | `-31.90%` | `352.00` |
| `Live` | `Long` | `0.6105` | 4,000,000.00 USD | 0.00 USD | 2,750.00 USD | `-31.79%` | `4,500.00` |
| `Live` | `Long` | `0.6115` | 3,990,000.00 USD | 0.00 USD | 6,280.00 USD | `-31.68%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 3,990,000.00 USD | 0.00 USD | 438.73 USD | `-31.56%` | `716.30` |
| `Live` | `Long` | `0.6135` | 3,990,000.00 USD | 0.00 USD | 112.33 USD | `-31.45%` | `183.10` |
| `Live` | `Long` | `0.6145` | 3,990,000.00 USD | 0.00 USD | 2,110.00 USD | `-31.34%` | `3,435.00` |
| `Live` | `Long` | `0.6155` | 3,980,000.00 USD | 0.00 USD | 935.13 USD | `-31.23%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 3,980,000.00 USD | 0.00 USD | 29,900.00 USD | `-31.12%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 3,950,000.00 USD | 0.00 USD | 4,980.00 USD | `-31.01%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 3,950,000.00 USD | 0.00 USD | 12,570.00 USD | `-30.89%` | `20,327.90` |
| `Live` | `Long` | `0.6195` | 3,940,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.78%` | `3,868.00` |
| `Live` | `Long` | `0.6225` | 3,930,000.00 USD | 0.00 USD | 708.53 USD | `-30.45%` | `1,138.20` |
| `Live` | `Long` | `0.6245` | 3,930,000.00 USD | 0.00 USD | 356.65 USD | `-30.22%` | `571.10` |
| `Live` | `Long` | `0.6255` | 3,930,000.00 USD | 0.00 USD | 32,070.00 USD | `-30.11%` | `51,265.70` |
| `Live` | `Long` | `0.6285` | 3,900,000.00 USD | 0.00 USD | 416.70 USD | `-29.78%` | `663.00` |
| `Live` | `Long` | `0.6295` | 3,900,000.00 USD | 0.00 USD | 1,100.00 USD | `-29.66%` | `1,739.60` |
| `Live` | `Long` | `0.6305` | 3,900,000.00 USD | 0.00 USD | 319.35 USD | `-29.55%` | `506.50` |
| `Live` | `Long` | `0.6345` | 3,900,000.00 USD | 0.00 USD | 843.00 USD | `-29.11%` | `1,328.60` |
| `Live` | `Long` | `0.6365` | 3,900,000.00 USD | 0.00 USD | 3,060.00 USD | `-28.88%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,890,000.00 USD | 0.00 USD | 1,100.00 USD | `-28.77%` | `1,726.70` |
| `Live` | `Long` | `0.6405` | 3,890,000.00 USD | 0.00 USD | 33,040.00 USD | `-28.44%` | `51,581.80` |
| `Live` | `Long` | `0.6415` | 3,860,000.00 USD | 0.00 USD | 86,920.00 USD | `-28.32%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,770,000.00 USD | 0.00 USD | 4,980.00 USD | `-28.21%` | `7,754.70` |
| `Live` | `Long` | `0.6435` | 3,770,000.00 USD | 0.00 USD | 3,380.00 USD | `-28.10%` | `5,251.30` |
| `Live` | `Long` | `0.6445` | 3,760,000.00 USD | 0.00 USD | 65,790.00 USD | `-27.99%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,700,000.00 USD | 0.00 USD | 14,590.00 USD | `-27.88%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,680,000.00 USD | 0.00 USD | 146.76 USD | `-27.77%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,680,000.00 USD | 0.00 USD | 9,810.00 USD | `-27.65%` | `15,145.10` |
| `Live` | `Long` | `0.6485` | 3,670,000.00 USD | 0.00 USD | 668.34 USD | `-27.54%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,670,000.00 USD | 0.00 USD | 344.82 USD | `-27.43%` | `530.90` |
| `Live` | `Long` | `0.6505` | 3,670,000.00 USD | 0.00 USD | 106.75 USD | `-27.32%` | `164.10` |
| `Live` | `Long` | `0.6515` | 3,670,000.00 USD | 0.00 USD | 403,320.00 USD | `-27.21%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,270,000.00 USD | 0.00 USD | 2,350.00 USD | `-27.09%` | `3,599.00` |
| `Live` | `Long` | `0.6535` | 3,270,000.00 USD | 0.00 USD | 2,840.00 USD | `-26.98%` | `4,345.80` |
| `Live` | `Long` | `0.6545` | 3,260,000.00 USD | 0.00 USD | 7,890.00 USD | `-26.87%` | `12,058.40` |
| `Live` | `Long` | `0.6555` | 3,260,000.00 USD | 0.00 USD | 1,830.00 USD | `-26.76%` | `2,793.70` |
| `Live` | `Long` | `0.6565` | 3,250,000.00 USD | 0.00 USD | 7,070.00 USD | `-26.65%` | `10,764.20` |
| `Live` | `Long` | `0.6575` | 3,250,000.00 USD | 0.00 USD | 13,280.00 USD | `-26.54%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,230,000.00 USD | 0.00 USD | 2,970.00 USD | `-26.42%` | `4,508.30` |
| `Live` | `Long` | `0.6615` | 3,230,000.00 USD | 0.00 USD | 2,600.00 USD | `-26.09%` | `3,932.40` |
| `Live` | `Long` | `0.6625` | 3,230,000.00 USD | 0.00 USD | 97,590.00 USD | `-25.98%` | `147,306.80` |
| `Live` | `Long` | `0.6645` | 3,130,000.00 USD | 0.00 USD | 448.54 USD | `-25.75%` | `675.00` |
| `Live` | `Long` | `0.6665` | 3,130,000.00 USD | 0.00 USD | 528.73 USD | `-25.53%` | `793.30` |
| `Live` | `Long` | `0.6675` | 3,130,000.00 USD | 0.00 USD | 2,260.00 USD | `-25.42%` | `3,386.00` |
| `Live` | `Long` | `0.6685` | 3,130,000.00 USD | 0.00 USD | 135.71 USD | `-25.31%` | `203.00` |
| `Live` | `Long` | `0.6695` | 3,130,000.00 USD | 0.00 USD | 337.36 USD | `-25.20%` | `503.90` |
| `Live` | `Long` | `0.6705` | 3,130,000.00 USD | 0.00 USD | 2,470.00 USD | `-25.08%` | `3,690.60` |
| `Live` | `Long` | `0.6715` | 3,130,000.00 USD | 0.00 USD | 2,450.00 USD | `-24.97%` | `3,641.20` |
| `Live` | `Long` | `0.6725` | 3,120,000.00 USD | 0.00 USD | 28,290.00 USD | `-24.86%` | `42,061.40` |
| `Live` | `Long` | `0.6735` | 3,090,000.00 USD | 0.00 USD | 633.09 USD | `-24.75%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,090,000.00 USD | 0.00 USD | 6,520.00 USD | `-24.64%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 3,090,000.00 USD | 0.00 USD | 854.64 USD | `-24.53%` | `1,265.20` |
| `Live` | `Long` | `0.6765` | 3,090,000.00 USD | 0.00 USD | 189.22 USD | `-24.41%` | `279.70` |
| `Live` | `Long` | `0.6775` | 3,090,000.00 USD | 0.00 USD | 9,150.00 USD | `-24.30%` | `13,500.00` |
| `Live` | `Long` | `0.6785` | 3,080,000.00 USD | 0.00 USD | 122.94 USD | `-24.19%` | `181.20` |
| `Live` | `Long` | `0.6795` | 3,080,000.00 USD | 0.00 USD | 43,650.00 USD | `-24.08%` | `64,238.50` |
| `Live` | `Long` | `0.6805` | 3,030,000.00 USD | 0.00 USD | 1,600.00 USD | `-23.97%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 3,030,000.00 USD | 0.00 USD | 2,110.00 USD | `-23.85%` | `3,092.70` |
| `Live` | `Long` | `0.6825` | 3,030,000.00 USD | 0.00 USD | 17,190.00 USD | `-23.74%` | `25,192.00` |
| `Live` | `Long` | `0.6835` | 3,010,000.00 USD | 0.00 USD | 15,130.00 USD | `-23.63%` | `22,136.50` |
| `Live` | `Long` | `0.6845` | 3,000,000.00 USD | 0.00 USD | 5,960.00 USD | `-23.52%` | `8,711.60` |
| `Live` | `Long` | `0.6865` | 2,990,000.00 USD | 0.00 USD | 112.59 USD | `-23.30%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,990,000.00 USD | 0.00 USD | 6,110.00 USD | `-23.18%` | `8,883.90` |
| `Live` | `Long` | `0.6885` | 2,990,000.00 USD | 0.00 USD | 1,060.00 USD | `-23.07%` | `1,536.40` |
| `Live` | `Long` | `0.6895` | 2,980,000.00 USD | 0.00 USD | 2,110.00 USD | `-22.96%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,980,000.00 USD | 0.00 USD | 3,360.00 USD | `-22.85%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,980,000.00 USD | 0.00 USD | 10,590.00 USD | `-22.74%` | `15,317.60` |
| `Live` | `Long` | `0.6935` | 2,970,000.00 USD | 0.00 USD | 3,600.00 USD | `-22.51%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 2,960,000.00 USD | 0.00 USD | 7,670.00 USD | `-22.40%` | `11,040.00` |
| `Live` | `Long` | `0.6955` | 2,960,000.00 USD | 0.00 USD | 1,700.00 USD | `-22.29%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,950,000.00 USD | 0.00 USD | 273.03 USD | `-22.18%` | `392.00` |
| `Live` | `Long` | `0.6975` | 2,950,000.00 USD | 0.00 USD | 1,030.00 USD | `-22.07%` | `1,482.80` |
| `Live` | `Long` | `0.6985` | 2,950,000.00 USD | 0.00 USD | 4,830.00 USD | `-21.96%` | `6,919.90` |
| `Live` | `Long` | `0.7015` | 2,950,000.00 USD | 0.00 USD | 1,990.00 USD | `-21.62%` | `2,841.50` |
| `Live` | `Long` | `0.7045` | 2,950,000.00 USD | 0.00 USD | 8,970.00 USD | `-21.28%` | `12,729.60` |
| `Live` | `Long` | `0.7055` | 2,940,000.00 USD | 0.00 USD | 287.84 USD | `-21.17%` | `408.00` |
| `Live` | `Long` | `0.7065` | 2,940,000.00 USD | 0.00 USD | 143.14 USD | `-21.06%` | `202.60` |
| `Live` | `Long` | `0.7075` | 2,940,000.00 USD | 0.00 USD | 3,620.00 USD | `-20.95%` | `5,122.60` |
| `Live` | `Long` | `0.7085` | 2,930,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.84%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,930,000.00 USD | 0.00 USD | 823.37 USD | `-20.73%` | `1,160.50` |
| `Live` | `Long` | `0.7105` | 2,930,000.00 USD | 0.00 USD | 25,230.00 USD | `-20.61%` | `35,512.10` |
| `Live` | `Long` | `0.7125` | 2,910,000.00 USD | 0.00 USD | 283.22 USD | `-20.39%` | `397.50` |
| `Live` | `Long` | `0.7135` | 2,910,000.00 USD | 0.00 USD | 927.55 USD | `-20.28%` | `1,300.00` |
| `Live` | `Long` | `0.7145` | 2,900,000.00 USD | 0.00 USD | 297.23 USD | `-20.17%` | `416.00` |
| `Live` | `Long` | `0.7155` | 2,900,000.00 USD | 0.00 USD | 441,770.00 USD | `-20.06%` | `617,421.50` |
| `Live` | `Long` | `0.7165` | 2,460,000.00 USD | 0.00 USD | 4,620.00 USD | `-19.94%` | `6,444.00` |
| `Live` | `Long` | `0.7185` | 2,460,000.00 USD | 0.00 USD | 126.96 USD | `-19.72%` | `176.70` |
| `Live` | `Long` | `0.7195` | 2,460,000.00 USD | 0.00 USD | 420.19 USD | `-19.61%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,460,000.00 USD | 0.00 USD | 8,450.00 USD | `-19.39%` | `11,706.20` |
| `Live` | `Long` | `0.7225` | 2,450,000.00 USD | 0.00 USD | 1,940.00 USD | `-19.27%` | `2,689.40` |
| `Live` | `Long` | `0.7235` | 2,450,000.00 USD | 0.00 USD | 127.05 USD | `-19.16%` | `175.60` |
| `Live` | `Long` | `0.7245` | 2,450,000.00 USD | 0.00 USD | 2,520.00 USD | `-19.05%` | `3,475.80` |
| `Live` | `Long` | `0.7255` | 2,440,000.00 USD | 0.00 USD | 311.60 USD | `-18.94%` | `429.50` |
| `Live` | `Long` | `0.7265` | 2,440,000.00 USD | 0.00 USD | 11,790.00 USD | `-18.83%` | `16,232.90` |
| `Live` | `Long` | `0.7275` | 2,430,000.00 USD | 0.00 USD | 35,890.00 USD | `-18.72%` | `49,332.50` |
| `Live` | `Long` | `0.7285` | 2,400,000.00 USD | 0.00 USD | 424.86 USD | `-18.60%` | `583.20` |
| `Live` | `Long` | `0.7295` | 2,400,000.00 USD | 0.00 USD | 375.98 USD | `-18.49%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,400,000.00 USD | 0.00 USD | 119.88 USD | `-18.38%` | `164.10` |
| `Live` | `Long` | `0.7325` | 2,400,000.00 USD | 0.00 USD | 13,500.00 USD | `-18.16%` | `18,432.50` |
| `Live` | `Long` | `0.7335` | 2,380,000.00 USD | 0.00 USD | 11,890.00 USD | `-18.04%` | `16,211.20` |
| `Live` | `Long` | `0.7345` | 2,370,000.00 USD | 0.00 USD | 6,240.00 USD | `-17.93%` | `8,498.00` |
| `Live` | `Long` | `0.7355` | 2,360,000.00 USD | 0.00 USD | 51,920.00 USD | `-17.82%` | `70,595.50` |
| `Live` | `Long` | `0.7375` | 2,310,000.00 USD | 0.00 USD | 3,450.00 USD | `-17.60%` | `4,683.00` |
| `Live` | `Long` | `0.7385` | 2,310,000.00 USD | 0.00 USD | 6,020.00 USD | `-17.49%` | `8,146.50` |
| `Live` | `Long` | `0.7395` | 2,300,000.00 USD | 0.00 USD | 3,380.00 USD | `-17.37%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,300,000.00 USD | 0.00 USD | 3,530.00 USD | `-17.26%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,300,000.00 USD | 0.00 USD | 382.61 USD | `-17.15%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,300,000.00 USD | 0.00 USD | 2,280.00 USD | `-17.04%` | `3,074.90` |
| `Live` | `Long` | `0.7435` | 2,290,000.00 USD | 0.00 USD | 784,400.00 USD | `-16.93%` | `1,055,008.20` |
| `Live` | `Long` | `0.7455` | 1,510,000.00 USD | 0.00 USD | 4,020.00 USD | `-16.70%` | `5,393.10` |
| `Live` | `Long` | `0.7465` | 1,500,000.00 USD | 0.00 USD | 359.96 USD | `-16.59%` | `482.20` |
| `Live` | `Long` | `0.7475` | 1,500,000.00 USD | 0.00 USD | 107,260.00 USD | `-16.48%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,400,000.00 USD | 0.00 USD | 4,820.00 USD | `-16.26%` | `6,426.70` |
| `Live` | `Long` | `0.7515` | 1,390,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.03%` | `1,613.50` |
| `Live` | `Long` | `0.7535` | 1,390,000.00 USD | 0.00 USD | 264.86 USD | `-15.81%` | `351.50` |
| `Live` | `Long` | `0.7545` | 1,390,000.00 USD | 0.00 USD | 1,250.00 USD | `-15.70%` | `1,650.60` |
| `Live` | `Long` | `0.7555` | 1,390,000.00 USD | 0.00 USD | 1,750.00 USD | `-15.59%` | `2,315.50` |
| `Live` | `Long` | `0.7575` | 1,390,000.00 USD | 0.00 USD | 1,900.00 USD | `-15.36%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,390,000.00 USD | 0.00 USD | 40,520.00 USD | `-15.25%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,340,000.00 USD | 0.00 USD | 4,900.00 USD | `-15.14%` | `6,448.30` |
| `Live` | `Long` | `0.7605` | 1,340,000.00 USD | 0.00 USD | 2,920.00 USD | `-15.03%` | `3,840.20` |
| `Live` | `Long` | `0.7615` | 1,340,000.00 USD | 0.00 USD | 351.43 USD | `-14.92%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,340,000.00 USD | 0.00 USD | 859.11 USD | `-14.80%` | `1,126.70` |
| `Live` | `Long` | `0.7635` | 1,340,000.00 USD | 0.00 USD | 5,550.00 USD | `-14.69%` | `7,271.90` |
| `Live` | `Long` | `0.7645` | 1,330,000.00 USD | 0.00 USD | 3,510.00 USD | `-14.58%` | `4,596.60` |
| `Live` | `Long` | `0.7655` | 1,330,000.00 USD | 0.00 USD | 4,430.00 USD | `-14.47%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,320,000.00 USD | 0.00 USD | 1,260.00 USD | `-14.36%` | `1,649.10` |
| `Live` | `Long` | `0.7675` | 1,320,000.00 USD | 0.00 USD | 25,580.00 USD | `-14.25%` | `33,323.60` |
| `Live` | `Long` | `0.7685` | 1,300,000.00 USD | 0.00 USD | 207.19 USD | `-14.13%` | `269.60` |
| `Live` | `Long` | `0.7695` | 1,300,000.00 USD | 0.00 USD | 150,510.00 USD | `-14.02%` | `195,593.50` |
| `Live` | `Long` | `0.7705` | 1,140,000.00 USD | 0.00 USD | 5,640.00 USD | `-13.91%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 1,140,000.00 USD | 0.00 USD | 19,250.00 USD | `-13.80%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 1,120,000.00 USD | 0.00 USD | 1,940.00 USD | `-13.69%` | `2,515.50` |
| `Live` | `Long` | `0.7735` | 1,120,000.00 USD | 0.00 USD | 325,060.00 USD | `-13.58%` | `420,245.30` |
| `Live` | `Long` | `0.7755` | 793,010.00 USD | 0.00 USD | 3,430.00 USD | `-13.35%` | `4,424.80` |
| `Live` | `Long` | `0.7765` | 789,580.00 USD | 0.00 USD | 3,510.00 USD | `-13.24%` | `4,518.50` |
| `Live` | `Long` | `0.7785` | 786,070.00 USD | 0.00 USD | 28,010.00 USD | `-13.02%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 758,060.00 USD | 0.00 USD | 338.69 USD | `-12.91%` | `434.50` |
| `Live` | `Long` | `0.7815` | 757,720.00 USD | 0.00 USD | 4,160.00 USD | `-12.68%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 753,560.00 USD | 0.00 USD | 21,760.00 USD | `-12.46%` | `27,771.60` |
| `Live` | `Long` | `0.7865` | 731,800.00 USD | 0.00 USD | 3,470.00 USD | `-12.12%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 728,330.00 USD | 0.00 USD | 288.70 USD | `-12.01%` | `366.60` |
| `Live` | `Long` | `0.7905` | 728,040.00 USD | 0.00 USD | 7,440.00 USD | `-11.68%` | `9,415.00` |
| `Live` | `Long` | `0.7915` | 720,590.00 USD | 0.00 USD | 7,620.00 USD | `-11.56%` | `9,623.00` |
| `Live` | `Long` | `0.7925` | 712,980.00 USD | 0.00 USD | 10,810.00 USD | `-11.45%` | `13,636.90` |
| `Live` | `Long` | `0.7935` | 702,170.00 USD | 0.00 USD | 809.45 USD | `-11.34%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 701,360.00 USD | 0.00 USD | 736.66 USD | `-11.23%` | `927.20` |
| `Live` | `Long` | `0.7955` | 700,620.00 USD | 0.00 USD | 52,610.00 USD | `-11.12%` | `66,134.90` |
| `Live` | `Long` | `0.7965` | 648,010.00 USD | 0.00 USD | 12,980.00 USD | `-11.01%` | `16,300.50` |
| `Live` | `Long` | `0.7975` | 635,030.00 USD | 0.00 USD | 7,580.00 USD | `-10.89%` | `9,508.60` |
| `Live` | `Long` | `0.7985` | 627,450.00 USD | 0.00 USD | 40,230.00 USD | `-10.78%` | `50,386.80` |
| `Live` | `Long` | `0.7995` | 587,210.00 USD | 0.00 USD | 7,590.00 USD | `-10.67%` | `9,489.80` |
| `Live` | `Long` | `0.8005` | 579,630.00 USD | 0.00 USD | 3,620.00 USD | `-10.56%` | `4,522.90` |
| `Live` | `Long` | `0.8015` | 576,010.00 USD | 0.00 USD | 7,500.00 USD | `-10.45%` | `9,361.90` |
| `Live` | `Long` | `0.8025` | 568,500.00 USD | 0.00 USD | 4,920.00 USD | `-10.34%` | `6,136.70` |
| `Live` | `Long` | `0.8035` | 563,580.00 USD | 0.00 USD | 7,680.00 USD | `-10.22%` | `9,559.90` |
| `Live` | `Long` | `0.8045` | 555,900.00 USD | 0.00 USD | 16,770.00 USD | `-10.11%` | `20,848.30` |
| `Live` | `Long` | `0.8055` | 539,120.00 USD | 0.00 USD | 361.11 USD | `-10.00%` | `448.30` |
| `Live` | `Long` | `0.8065` | 538,760.00 USD | 0.00 USD | 6,910.00 USD | `-9.89%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 531,850.00 USD | 0.00 USD | 2,770.00 USD | `-9.78%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 529,090.00 USD | 0.00 USD | 22,510.00 USD | `-9.66%` | `27,845.30` |
| `Live` | `Long` | `0.8095` | 506,570.00 USD | 0.00 USD | 130,110.00 USD | `-9.55%` | `160,732.40` |
| `Live` | `Long` | `0.8105` | 376,460.00 USD | 0.00 USD | 2,250.00 USD | `-9.44%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 374,210.00 USD | 0.00 USD | 2,970.00 USD | `-9.33%` | `3,654.30` |
| `Live` | `Long` | `0.8125` | 371,240.00 USD | 0.00 USD | 1,160.00 USD | `-9.22%` | `1,421.60` |
| `Live` | `Long` | `0.8135` | 370,090.00 USD | 0.00 USD | 3,800.00 USD | `-9.11%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 366,280.00 USD | 0.00 USD | 277.42 USD | `-8.99%` | `340.60` |
| `Live` | `Long` | `0.8155` | 366,000.00 USD | 0.00 USD | 38,250.00 USD | `-8.88%` | `46,908.50` |
| `Live` | `Long` | `0.8165` | 327,750.00 USD | 0.00 USD | 104.92 USD | `-8.77%` | `128.50` |
| `Live` | `Long` | `0.8175` | 327,640.00 USD | 0.00 USD | 77,840.00 USD | `-8.66%` | `95,214.30` |
| `Live` | `Long` | `0.8185` | 249,810.00 USD | 0.00 USD | 25,070.00 USD | `-8.55%` | `30,624.60` |
| `Live` | `Long` | `0.8195` | 224,740.00 USD | 0.00 USD | 1,230.00 USD | `-8.44%` | `1,498.80` |
| `Live` | `Long` | `0.8205` | 223,510.00 USD | 0.00 USD | 7,960.00 USD | `-8.32%` | `9,697.10` |
| `Live` | `Long` | `0.8215` | 215,560.00 USD | 0.00 USD | 474.01 USD | `-8.21%` | `577.00` |
| `Live` | `Long` | `0.8225` | 215,080.00 USD | 0.00 USD | 2,890.00 USD | `-8.10%` | `3,517.50` |
| `Live` | `Long` | `0.8235` | 212,190.00 USD | 0.00 USD | 463.63 USD | `-7.99%` | `563.00` |
| `Live` | `Long` | `0.8245` | 211,730.00 USD | 0.00 USD | 18,980.00 USD | `-7.88%` | `23,022.60` |
| `Live` | `Long` | `0.8255` | 192,740.00 USD | 0.00 USD | 1,580.00 USD | `-7.77%` | `1,911.90` |
| `Live` | `Long` | `0.8275` | 191,170.00 USD | 0.00 USD | 4,690.00 USD | `-7.54%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 186,480.00 USD | 0.00 USD | 120,070.00 USD | `-7.43%` | `144,926.90` |
| `Live` | `Long` | `0.8295` | 66,410.00 USD | 0.00 USD | 46,590.00 USD | `-7.32%` | `56,161.30` |
| `Live` | `Long` | `0.8345` | 19,820.00 USD | 0.00 USD | 5,750.00 USD | `-6.76%` | `6,885.20` |
| `Live` | `Long` | `0.8375` | 14,070.00 USD | 0.00 USD | 327.21 USD | `-6.42%` | `390.70` |
| `Live` | `Long` | `0.8385` | 13,750.00 USD | 0.00 USD | 7,300.00 USD | `-6.31%` | `8,701.00` |
| `Live` | `Long` | `0.8405` | 6,450.00 USD | 0.00 USD | 1,440.00 USD | `-6.09%` | `1,709.20` |
| `Live` | `Long` | `0.8415` | 5,020.00 USD | 0.00 USD | 134.47 USD | `-5.98%` | `159.80` |
| `Live` | `Long` | `0.8425` | 4,880.00 USD | 0.00 USD | 4,130.00 USD | `-5.87%` | `4,907.70` |
| `Live` | `Long` | `0.8455` | 745.82 USD | 0.00 USD | 745.82 USD | `-5.53%` | `882.10` |
| `Live` | `Short` | `0.8965` | 187.46 USD | 187.46 USD | 0.00 USD | `+0.17%` | `209.10` |
| `Live` | `Short` | `0.9145` | 4,250.00 USD | 4,060.00 USD | 0.00 USD | `+2.18%` | `4,444.10` |
| `Live` | `Short` | `0.9195` | 13,450.00 USD | 9,200.00 USD | 0.00 USD | `+2.74%` | `10,000.00` |
| `Live` | `Short` | `0.9235` | 13,660.00 USD | 209.36 USD | 0.00 USD | `+3.18%` | `226.70` |
| `Live` | `Short` | `0.9365` | 21,830.00 USD | 8,170.00 USD | 0.00 USD | `+4.64%` | `8,726.20` |
| `Live` | `Short` | `0.9385` | 61,670.00 USD | 39,850.00 USD | 0.00 USD | `+4.86%` | `42,456.90` |
| `Live` | `Short` | `0.9405` | 62,030.00 USD | 352.88 USD | 0.00 USD | `+5.08%` | `375.20` |
| `Live` | `Short` | `0.9805` | 63,070.00 USD | 1,050.00 USD | 0.00 USD | `+9.55%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 63,440.00 USD | 365.70 USD | 0.00 USD | `+10.22%` | `370.70` |
| `Live` | `Short` | `0.9885` | 67,700.00 USD | 4,250.00 USD | 0.00 USD | `+10.45%` | `4,304.30` |
| `Live` | `Short` | `0.9915` | 69,270.00 USD | 1,570.00 USD | 0.00 USD | `+10.78%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 69,410.00 USD | 139.59 USD | 0.00 USD | `+11.01%` | `140.50` |
| `Live` | `Short` | `1.00` | 69,740.00 USD | 330.29 USD | 0.00 USD | `+11.90%` | `329.80` |
| `Live` | `Short` | `1.01` | 70,440.00 USD | 705.99 USD | 0.00 USD | `+13.35%` | `695.90` |
| `Live` | `Short` | `1.02` | 70,610.00 USD | 170.40 USD | 0.00 USD | `+13.46%` | `167.80` |
| `Live` | `Short` | `1.04` | 70,770.00 USD | 155.92 USD | 0.00 USD | `+16.15%` | `150.00` |
| `Live` | `Short` | `1.05` | 72,490.00 USD | 1,720.00 USD | 0.00 USD | `+17.04%` | `1,639.00` |
| `Live` | `Short` | `1.05` | 73,080.00 USD | 597.52 USD | 0.00 USD | `+17.37%` | `568.80` |
| `Live` | `Short` | `1.05` | 75,470.00 USD | 2,390.00 USD | 0.00 USD | `+17.49%` | `2,272.10` |
| `Live` | `Short` | `1.08` | 79,060.00 USD | 3,580.00 USD | 0.00 USD | `+20.73%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 84,610.00 USD | 5,550.00 USD | 0.00 USD | `+21.73%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 84,930.00 USD | 324.90 USD | 0.00 USD | `+22.85%` | `295.50` |
| `Live` | `Short` | `1.10` | 85,210.00 USD | 277.22 USD | 0.00 USD | `+22.96%` | `251.90` |
| `Live` | `Short` | `1.11` | 94,150.00 USD | 8,940.00 USD | 0.00 USD | `+24.08%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 117,460.00 USD | 23,310.00 USD | 0.00 USD | `+25.87%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 118,090.00 USD | 634.09 USD | 0.00 USD | `+26.54%` | `559.90` |
| `Live` | `Short` | `1.15` | 118,220.00 USD | 129.88 USD | 0.00 USD | `+28.88%` | `112.60` |
| `Live` | `Short` | `1.20` | 118,400.00 USD | 177.65 USD | 0.00 USD | `+34.02%` | `148.10` |
| `Live` | `Short` | `1.22` | 122,840.00 USD | 4,440.00 USD | 0.00 USD | `+36.15%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 123,220.00 USD | 383.01 USD | 0.00 USD | `+36.59%` | `313.30` |
| `Live` | `Short` | `1.23` | 123,600.00 USD | 380.84 USD | 0.00 USD | `+37.93%` | `308.50` |
| `Live` | `Short` | `1.24` | 127,530.00 USD | 3,930.00 USD | 0.00 USD | `+38.49%` | `3,169.40` |
| `Live` | `Short` | `1.24` | 128,760.00 USD | 1,230.00 USD | 0.00 USD | `+38.60%` | `989.90` |
| `Live` | `Short` | `1.26` | 131,430.00 USD | 2,670.00 USD | 0.00 USD | `+40.73%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 133,730.00 USD | 2,300.00 USD | 0.00 USD | `+42.74%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 143,500.00 USD | 9,760.00 USD | 0.00 USD | `+43.18%` | `7,618.00` |
| `Live` | `Short` | `1.28` | 183,380.00 USD | 39,880.00 USD | 0.00 USD | `+43.30%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 183,610.00 USD | 226.80 USD | 0.00 USD | `+44.64%` | `175.20` |
| `Live` | `Short` | `1.30` | 183,720.00 USD | 114.40 USD | 0.00 USD | `+45.08%` | `88.10` |
| `Live` | `Short` | `1.31` | 184,740.00 USD | 1,020.00 USD | 0.00 USD | `+46.31%` | `777.20` |
| `Live` | `Short` | `1.31` | 216,270.00 USD | 31,530.00 USD | 0.00 USD | `+46.54%` | `24,042.40` |
| `Live` | `Short` | `1.32` | 216,500.00 USD | 228.36 USD | 0.00 USD | `+47.32%` | `173.20` |
| `Live` | `Short` | `1.33` | 222,840.00 USD | 6,340.00 USD | 0.00 USD | `+48.10%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 223,930.00 USD | 1,100.00 USD | 0.00 USD | `+48.32%` | `826.40` |
| `Live` | `Short` | `1.33` | 245,900.00 USD | 21,970.00 USD | 0.00 USD | `+48.44%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 252,760.00 USD | 6,860.00 USD | 0.00 USD | `+49.66%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 275,740.00 USD | 22,980.00 USD | 0.00 USD | `+52.68%` | `16,816.80` |
| `Live` | `Short` | `1.37` | 634,020.00 USD | 358,280.00 USD | 0.00 USD | `+53.35%` | `261,043.60` |
| `Live` | `Short` | `1.38` | 634,160.00 USD | 135.66 USD | 0.00 USD | `+54.36%` | `98.20` |
| `Live` | `Short` | `1.41` | 638,600.00 USD | 4,450.00 USD | 0.00 USD | `+58.04%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 639,000.00 USD | 402.08 USD | 0.00 USD | `+60.50%` | `279.90` |
| `Live` | `Short` | `1.44` | 639,290.00 USD | 288.68 USD | 0.00 USD | `+60.95%` | `200.40` |
| `Live` | `Short` | `1.50` | 656,060.00 USD | 16,770.00 USD | 0.00 USD | `+67.54%` | `11,182.60` |
| `Live` | `Short` | `1.51` | 660,080.00 USD | 4,020.00 USD | 0.00 USD | `+69.22%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 660,230.00 USD | 152.95 USD | 0.00 USD | `+70.89%` | `100.00` |
| `Live` | `Short` | `1.53` | 670,170.00 USD | 9,940.00 USD | 0.00 USD | `+71.12%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 670,320.00 USD | 144.34 USD | 0.00 USD | `+71.56%` | `94.00` |
| `Live` | `Short` | `1.58` | 670,600.00 USD | 285.21 USD | 0.00 USD | `+76.26%` | `180.80` |
| `Live` | `Short` | `1.59` | 671,790.00 USD | 1,180.00 USD | 0.00 USD | `+78.04%` | `743.20` |
| `Live` | `Short` | `1.60` | 671,910.00 USD | 123.81 USD | 0.00 USD | `+78.49%` | `77.50` |
| `Live` | `Short` | `1.60` | 673,040.00 USD | 1,130.00 USD | 0.00 USD | `+79.05%` | `704.60` |
| `Live` | `Short` | `1.64` | 673,180.00 USD | 138.45 USD | 0.00 USD | `+83.07%` | `84.50` |
| `Live` | `Short` | `1.65` | 694,510.00 USD | 21,330.00 USD | 0.00 USD | `+83.97%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 698,450.00 USD | 3,940.00 USD | 0.00 USD | `+84.75%` | `2,381.50` |
| `Live` | `Short` | `1.66` | 702,080.00 USD | 3,620.00 USD | 0.00 USD | `+85.42%` | `2,184.10` |
| `Live` | `Short` | `1.66` | 741,220.00 USD | 39,140.00 USD | 0.00 USD | `+85.87%` | `23,529.40` |
| `Live` | `Short` | `1.68` | 743,500.00 USD | 2,280.00 USD | 0.00 USD | `+87.21%` | `1,360.10` |
| `Live` | `Short` | `1.69` | 743,650.00 USD | 150.02 USD | 0.00 USD | `+88.55%` | `88.90` |
| `Live` | `Short` | `1.71` | 1,040,000.00 USD | 296,470.00 USD | 0.00 USD | `+91.34%` | `173,120.10` |
| `Live` | `Short` | `1.71` | 1,050,000.00 USD | 9,670.00 USD | 0.00 USD | `+91.45%` | `5,645.40` |
| `Live` | `Short` | `1.73` | 1,050,000.00 USD | 226.05 USD | 0.00 USD | `+93.69%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,050,000.00 USD | 495.77 USD | 0.00 USD | `+94.02%` | `285.50` |
| `Live` | `Short` | `1.74` | 1,050,000.00 USD | 2,080.00 USD | 0.00 USD | `+94.58%` | `1,197.00` |
| `Live` | `Short` | `1.74` | 1,050,000.00 USD | 982.50 USD | 0.00 USD | `+94.92%` | `563.20` |
| `Live` | `Short` | `1.75` | 1,070,000.00 USD | 20,830.00 USD | 0.00 USD | `+95.70%` | `11,894.90` |
| `Live` | `Short` | `1.75` | 1,090,000.00 USD | 11,350.00 USD | 0.00 USD | `+95.92%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,090,000.00 USD | 1,520.00 USD | 0.00 USD | `+96.03%` | `868.90` |
| `Live` | `Short` | `1.76` | 1,170,000.00 USD | 87,070.00 USD | 0.00 USD | `+96.37%` | `49,543.90` |
| `Live` | `Short` | `1.76` | 1,180,000.00 USD | 7,040.00 USD | 0.00 USD | `+96.59%` | `4,000.00` |
| `Live` | `Short` | `1.79` | 1,180,000.00 USD | 782.21 USD | 0.00 USD | `+99.72%` | `437.60` |
| `Live` | `Short` | `1.79` | 1,180,000.00 USD | 134.32 USD | 0.00 USD | `+99.83%` | `75.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,240,000.00 USD | 0.00 USD | 497.31 USD | `-70.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,240,000.00 USD | 0.00 USD | 102.75 USD | `-61.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,240,000.00 USD | 0.00 USD | 256.78 USD | `-60.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,240,000.00 USD | 0.00 USD | 428.87 USD | `-56.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,240,000.00 USD | 0.00 USD | 123.45 USD | `-54.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,240,000.00 USD | 0.00 USD | 818.15 USD | `-53.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,240,000.00 USD | 0.00 USD | 436.41 USD | `-51.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,240,000.00 USD | 0.00 USD | 876.79 USD | `-51.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,240,000.00 USD | 0.00 USD | 466.72 USD | `-49.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,240,000.00 USD | 0.00 USD | 142.95 USD | `-46.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,240,000.00 USD | 0.00 USD | 3,010.00 USD | `-44.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,240,000.00 USD | 0.00 USD | 151.74 USD | `-42.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,240,000.00 USD | 0.00 USD | 123.91 USD | `-42.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,240,000.00 USD | 0.00 USD | 219.80 USD | `-38.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,230,000.00 USD | 0.00 USD | 237,400.00 USD | `-38.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 997,410.00 USD | 0.00 USD | 276.75 USD | `-38.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 997,130.00 USD | 0.00 USD | 1,680.00 USD | `-37.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 995,450.00 USD | 0.00 USD | 853.41 USD | `-36.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 994,590.00 USD | 0.00 USD | 119.76 USD | `-35.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 994,470.00 USD | 0.00 USD | 3,520.00 USD | `-34.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 990,950.00 USD | 0.00 USD | 470.62 USD | `-33.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 990,480.00 USD | 0.00 USD | 108.39 USD | `-32.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 990,370.00 USD | 0.00 USD | 123.28 USD | `-32.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 990,250.00 USD | 0.00 USD | 488.52 USD | `-30.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 989,760.00 USD | 0.00 USD | 4,230.00 USD | `-30.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 985,530.00 USD | 0.00 USD | 242.24 USD | `-29.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 985,290.00 USD | 0.00 USD | 193.95 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 985,100.00 USD | 0.00 USD | 149.22 USD | `-27.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 984,950.00 USD | 0.00 USD | 195.47 USD | `-26.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 984,750.00 USD | 0.00 USD | 112.91 USD | `-26.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 984,640.00 USD | 0.00 USD | 181.31 USD | `-26.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 984,460.00 USD | 0.00 USD | 190.25 USD | `-26.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 984,270.00 USD | 0.00 USD | 153.53 USD | `-25.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 984,110.00 USD | 0.00 USD | 52,450.00 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 931,670.00 USD | 0.00 USD | 536.11 USD | `-24.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 931,130.00 USD | 0.00 USD | 918.68 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 930,210.00 USD | 0.00 USD | 340.75 USD | `-23.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 929,870.00 USD | 0.00 USD | 9,270.00 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 920,600.00 USD | 0.00 USD | 120.53 USD | `-22.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 920,480.00 USD | 0.00 USD | 160.71 USD | `-22.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 920,320.00 USD | 0.00 USD | 738.08 USD | `-22.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 919,590.00 USD | 0.00 USD | 187.61 USD | `-21.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 919,400.00 USD | 0.00 USD | 8,500.00 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 910,900.00 USD | 0.00 USD | 89,150.00 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 821,750.00 USD | 0.00 USD | 189.06 USD | `-21.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 821,560.00 USD | 0.00 USD | 5,650.00 USD | `-20.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 815,910.00 USD | 0.00 USD | 371.68 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 815,540.00 USD | 0.00 USD | 152.05 USD | `-20.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 815,390.00 USD | 0.00 USD | 123.41 USD | `-19.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 815,260.00 USD | 0.00 USD | 745.54 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 814,520.00 USD | 0.00 USD | 1,130.00 USD | `-18.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 813,390.00 USD | 0.00 USD | 18,770.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 794,620.00 USD | 0.00 USD | 7,970.00 USD | `-18.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 786,650.00 USD | 0.00 USD | 257.26 USD | `-17.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 786,390.00 USD | 0.00 USD | 161.72 USD | `-17.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 786,230.00 USD | 0.00 USD | 1,590.00 USD | `-16.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 784,640.00 USD | 0.00 USD | 10,160.00 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 774,480.00 USD | 0.00 USD | 94,190.00 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 680,280.00 USD | 0.00 USD | 1,230.00 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 679,060.00 USD | 0.00 USD | 1,840.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 677,220.00 USD | 0.00 USD | 804.61 USD | `-15.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 676,410.00 USD | 0.00 USD | 590.68 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 675,820.00 USD | 0.00 USD | 635.62 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 675,190.00 USD | 0.00 USD | 191.12 USD | `-14.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 675,000.00 USD | 0.00 USD | 273.92 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 674,720.00 USD | 0.00 USD | 125.92 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 674,600.00 USD | 0.00 USD | 1,980.00 USD | `-13.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 672,620.00 USD | 0.00 USD | 1,150.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 671,470.00 USD | 0.00 USD | 1,500.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 669,980.00 USD | 0.00 USD | 1,860.00 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 668,120.00 USD | 0.00 USD | 128.47 USD | `-12.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 667,990.00 USD | 0.00 USD | 6,960.00 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 661,030.00 USD | 0.00 USD | 135.11 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 660,900.00 USD | 0.00 USD | 8,870.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 652,030.00 USD | 0.00 USD | 1,500.00 USD | `-11.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7935` | 650,530.00 USD | 0.00 USD | 1,290.00 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 649,240.00 USD | 0.00 USD | 23,420.00 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 625,820.00 USD | 0.00 USD | 1,260.00 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 624,560.00 USD | 0.00 USD | 319.40 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 624,240.00 USD | 0.00 USD | 4,740.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 619,500.00 USD | 0.00 USD | 1,800.00 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 617,710.00 USD | 0.00 USD | 144.67 USD | `-10.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 617,560.00 USD | 0.00 USD | 1,510.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 616,050.00 USD | 0.00 USD | 50,540.00 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 565,510.00 USD | 0.00 USD | 263.25 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 565,250.00 USD | 0.00 USD | 1,250.00 USD | `-9.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8095` | 564,000.00 USD | 0.00 USD | 218.32 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 563,780.00 USD | 0.00 USD | 181,850.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 381,930.00 USD | 0.00 USD | 353.81 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 381,580.00 USD | 0.00 USD | 1,010.00 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 380,570.00 USD | 0.00 USD | 123,350.00 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 257,210.00 USD | 0.00 USD | 1,160.00 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 256,050.00 USD | 0.00 USD | 216.70 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 255,840.00 USD | 0.00 USD | 125.72 USD | `-8.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 255,710.00 USD | 0.00 USD | 375.49 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 255,340.00 USD | 0.00 USD | 13,790.00 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 241,540.00 USD | 0.00 USD | 7,160.00 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 234,390.00 USD | 0.00 USD | 226.71 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 234,160.00 USD | 0.00 USD | 3,780.00 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 230,380.00 USD | 0.00 USD | 1,320.00 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 229,060.00 USD | 0.00 USD | 325.56 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 228,740.00 USD | 0.00 USD | 666.55 USD | `-7.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 228,070.00 USD | 0.00 USD | 577.25 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 227,490.00 USD | 0.00 USD | 3,950.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 223,540.00 USD | 0.00 USD | 171.46 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 223,370.00 USD | 0.00 USD | 7,920.00 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 215,450.00 USD | 0.00 USD | 690.30 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 214,760.00 USD | 0.00 USD | 144.54 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 214,610.00 USD | 0.00 USD | 263.43 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 214,350.00 USD | 0.00 USD | 610.23 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 213,740.00 USD | 0.00 USD | 699.65 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 213,040.00 USD | 0.00 USD | 320.31 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 212,720.00 USD | 0.00 USD | 240.52 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 212,480.00 USD | 0.00 USD | 388.23 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 212,090.00 USD | 0.00 USD | 3,040.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 209,050.00 USD | 0.00 USD | 510.57 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 208,540.00 USD | 0.00 USD | 212.81 USD | `-5.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 208,320.00 USD | 0.00 USD | 2,530.00 USD | `-5.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 205,790.00 USD | 0.00 USD | 12,850.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 192,940.00 USD | 0.00 USD | 481.80 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 192,460.00 USD | 0.00 USD | 1,330.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 191,130.00 USD | 0.00 USD | 25,350.00 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8525` | 165,780.00 USD | 0.00 USD | 7,700.00 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 158,080.00 USD | 0.00 USD | 345.13 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 157,740.00 USD | 0.00 USD | 1,420.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 156,320.00 USD | 0.00 USD | 1,470.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 154,850.00 USD | 0.00 USD | 105.30 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 154,740.00 USD | 0.00 USD | 8,900.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 145,840.00 USD | 0.00 USD | 1,740.00 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 144,100.00 USD | 0.00 USD | 3,880.00 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 140,210.00 USD | 0.00 USD | 6,160.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 134,060.00 USD | 0.00 USD | 1,960.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 132,100.00 USD | 0.00 USD | 2,590.00 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 129,510.00 USD | 0.00 USD | 2,420.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 127,090.00 USD | 0.00 USD | 3,310.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 123,780.00 USD | 0.00 USD | 6,910.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 116,870.00 USD | 0.00 USD | 3,020.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 113,860.00 USD | 0.00 USD | 410.11 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 113,450.00 USD | 0.00 USD | 5,340.00 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 108,110.00 USD | 0.00 USD | 11,960.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 96,150.00 USD | 0.00 USD | 712.45 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 95,440.00 USD | 0.00 USD | 1,500.00 USD | `-2.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 93,940.00 USD | 0.00 USD | 314.55 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 93,620.00 USD | 0.00 USD | 866.37 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 92,760.00 USD | 0.00 USD | 35,020.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 57,740.00 USD | 0.00 USD | 635.29 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 57,100.00 USD | 0.00 USD | 9,070.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 48,040.00 USD | 0.00 USD | 151.10 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 47,890.00 USD | 0.00 USD | 2,000.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 45,890.00 USD | 0.00 USD | 1,030.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 44,860.00 USD | 0.00 USD | 4,070.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 40,780.00 USD | 0.00 USD | 563.65 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 40,220.00 USD | 0.00 USD | 425.94 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8855` | 39,800.00 USD | 0.00 USD | 4,210.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 35,580.00 USD | 0.00 USD | 3,600.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 31,980.00 USD | 0.00 USD | 235.54 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8885` | 31,750.00 USD | 0.00 USD | 11,360.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 20,390.00 USD | 0.00 USD | 8,780.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8905` | 11,610.00 USD | 0.00 USD | 152.36 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 11,460.00 USD | 0.00 USD | 469.91 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 10,990.00 USD | 0.00 USD | 10,610.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 377.17 USD | 0.00 USD | 277.07 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8945` | 100.09 USD | 0.00 USD | 100.09 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 3,390.00 USD | 3,390.00 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 3,680.00 USD | 289.12 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 21,890.00 USD | 18,210.00 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 22,780.00 USD | 889.43 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 51,740.00 USD | 28,960.00 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 53,360.00 USD | 1,620.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 55,420.00 USD | 2,050.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 56,340.00 USD | 926.06 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 56,530.00 USD | 188.92 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 59,490.00 USD | 2,950.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 61,480.00 USD | 1,990.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 61,620.00 USD | 138.69 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 61,870.00 USD | 250.83 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 62,960.00 USD | 1,090.00 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 64,490.00 USD | 1,520.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 65,420.00 USD | 933.08 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 65,680.00 USD | 260.23 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 68,570.00 USD | 2,890.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 71,590.00 USD | 3,020.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 74,670.00 USD | 3,070.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 75,240.00 USD | 570.08 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 75,540.00 USD | 309.14 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 79,450.00 USD | 3,900.00 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 81,420.00 USD | 1,970.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 81,540.00 USD | 116.59 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 340,650.00 USD | 259,120.00 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 492,620.00 USD | 151,960.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 497,690.00 USD | 5,070.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 498,180.00 USD | 495.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 499,580.00 USD | 1,400.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 504,460.00 USD | 4,880.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 506,660.00 USD | 2,200.00 USD | 0.00 USD | `+3.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 506,950.00 USD | 287.62 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 507,150.00 USD | 199.16 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 507,280.00 USD | 130.59 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 507,730.00 USD | 448.69 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 507,850.00 USD | 120.16 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 508,880.00 USD | 1,030.00 USD | 0.00 USD | `+4.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 509,450.00 USD | 568.87 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 509,740.00 USD | 292.78 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 510,270.00 USD | 523.79 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 510,970.00 USD | 701.16 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 511,070.00 USD | 104.53 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 564,130.00 USD | 53,060.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 568,040.00 USD | 3,910.00 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 577,000.00 USD | 8,960.00 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 577,530.00 USD | 529.50 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 577,830.00 USD | 301.79 USD | 0.00 USD | `+5.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 579,540.00 USD | 1,700.00 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 580,320.00 USD | 789.04 USD | 0.00 USD | `+5.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 588,890.00 USD | 8,560.00 USD | 0.00 USD | `+5.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 589,940.00 USD | 1,050.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 590,790.00 USD | 848.20 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 609,910.00 USD | 19,120.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 610,170.00 USD | 261.97 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 614,390.00 USD | 4,220.00 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 614,550.00 USD | 159.19 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 624,460.00 USD | 9,910.00 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 627,610.00 USD | 3,150.00 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 629,050.00 USD | 1,440.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 631,930.00 USD | 2,890.00 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 633,060.00 USD | 1,130.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 633,190.00 USD | 121.54 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 633,340.00 USD | 155.06 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 685,850.00 USD | 52,510.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 686,010.00 USD | 161.82 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 705,410.00 USD | 19,400.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 705,670.00 USD | 259.86 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 707,010.00 USD | 1,340.00 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 707,480.00 USD | 476.57 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 708,020.00 USD | 531.57 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 711,180.00 USD | 3,160.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 712,170.00 USD | 993.78 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 712,380.00 USD | 212.90 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 724,060.00 USD | 11,680.00 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 724,190.00 USD | 125.61 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 724,630.00 USD | 441.51 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 734,820.00 USD | 10,190.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 735,070.00 USD | 253.14 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 739,270.00 USD | 4,200.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 739,450.00 USD | 176.73 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 739,960.00 USD | 513.32 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 775,320.00 USD | 35,360.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 807,170.00 USD | 31,850.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 811,970.00 USD | 4,800.00 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 812,530.00 USD | 558.35 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 813,590.00 USD | 1,060.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 814,770.00 USD | 1,180.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 815,260.00 USD | 490.99 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 815,660.00 USD | 395.21 USD | 0.00 USD | `+10.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 816,650.00 USD | 991.50 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 826,980.00 USD | 10,340.00 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 827,390.00 USD | 409.52 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 827,680.00 USD | 284.92 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 828,030.00 USD | 350.37 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 828,150.00 USD | 124.04 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 828,270.00 USD | 117.26 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 830,450.00 USD | 2,180.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 831,230.00 USD | 778.64 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 831,590.00 USD | 363.87 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 832,180.00 USD | 589.52 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 832,290.00 USD | 110.62 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 842,380.00 USD | 10,090.00 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 847,800.00 USD | 5,420.00 USD | 0.00 USD | `+12.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 850,320.00 USD | 2,520.00 USD | 0.00 USD | `+12.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 850,570.00 USD | 248.49 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 859,720.00 USD | 9,150.00 USD | 0.00 USD | `+13.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 860,440.00 USD | 722.63 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 860,750.00 USD | 312.07 USD | 0.00 USD | `+13.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 860,930.00 USD | 171.24 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 861,490.00 USD | 561.11 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 861,740.00 USD | 249.30 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 863,200.00 USD | 1,470.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 863,630.00 USD | 432.18 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 863,770.00 USD | 137.88 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 866,120.00 USD | 2,340.00 USD | 0.00 USD | `+15.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 866,810.00 USD | 694.72 USD | 0.00 USD | `+15.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 866,970.00 USD | 160.60 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 873,530.00 USD | 6,560.00 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 876,450.00 USD | 2,920.00 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 876,670.00 USD | 224.56 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 880,240.00 USD | 3,570.00 USD | 0.00 USD | `+16.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 880,680.00 USD | 432.19 USD | 0.00 USD | `+17.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 882,380.00 USD | 1,700.00 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,410,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+17.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,410,000.00 USD | 5,390.00 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,410,000.00 USD | 285.32 USD | 0.00 USD | `+18.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,410,000.00 USD | 1,130.00 USD | 0.00 USD | `+18.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,410,000.00 USD | 1,240.00 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,420,000.00 USD | 278.06 USD | 0.00 USD | `+18.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,420,000.00 USD | 309.00 USD | 0.00 USD | `+19.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,420,000.00 USD | 228.98 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,420,000.00 USD | 272.12 USD | 0.00 USD | `+19.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,420,000.00 USD | 117.12 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,560,000.00 USD | 140,120.00 USD | 0.00 USD | `+19.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,560,000.00 USD | 530.01 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,560,000.00 USD | 128.23 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,670,000.00 USD | 108,190.00 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,670,000.00 USD | 3,430.00 USD | 0.00 USD | `+21.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,670,000.00 USD | 550.49 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,670,000.00 USD | 5,810.00 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,680,000.00 USD | 1,520.00 USD | 0.00 USD | `+21.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,680,000.00 USD | 5,570.00 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,680,000.00 USD | 1,290.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,680,000.00 USD | 294.81 USD | 0.00 USD | `+22.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,680,000.00 USD | 183.11 USD | 0.00 USD | `+22.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,680,000.00 USD | 123.13 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,680,000.00 USD | 494.98 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,680,000.00 USD | 613.52 USD | 0.00 USD | `+22.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,800,000.00 USD | 115,100.00 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,800,000.00 USD | 409.76 USD | 0.00 USD | `+23.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,800,000.00 USD | 162.77 USD | 0.00 USD | `+23.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,800,000.00 USD | 959.70 USD | 0.00 USD | `+23.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,800,000.00 USD | 160.18 USD | 0.00 USD | `+23.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,800,000.00 USD | 669.85 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,800,000.00 USD | 293.61 USD | 0.00 USD | `+24.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,910,000.00 USD | 112,050.00 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,920,000.00 USD | 462.47 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,920,000.00 USD | 2,180.00 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,920,000.00 USD | 273.34 USD | 0.00 USD | `+26.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,920,000.00 USD | 119.49 USD | 0.00 USD | `+26.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,940,000.00 USD | 20,740.00 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,940,000.00 USD | 468.47 USD | 0.00 USD | `+26.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,940,000.00 USD | 1,430.00 USD | 0.00 USD | `+27.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,940,000.00 USD | 338.50 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,940,000.00 USD | 2,640.00 USD | 0.00 USD | `+28.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,940,000.00 USD | 1,230.00 USD | 0.00 USD | `+28.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,950,000.00 USD | 2,450.00 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,950,000.00 USD | 1,250.00 USD | 0.00 USD | `+29.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,950,000.00 USD | 143.67 USD | 0.00 USD | `+29.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,950,000.00 USD | 989.81 USD | 0.00 USD | `+30.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,950,000.00 USD | 304.33 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,950,000.00 USD | 255.14 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,950,000.00 USD | 241.65 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,950,000.00 USD | 239.97 USD | 0.00 USD | `+31.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,950,000.00 USD | 2,470.00 USD | 0.00 USD | `+31.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,960,000.00 USD | 3,060.00 USD | 0.00 USD | `+31.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,270,000.00 USD | 310,250.00 USD | 0.00 USD | `+32.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,270,000.00 USD | 309.53 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,270,000.00 USD | 159.09 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,270,000.00 USD | 146.21 USD | 0.00 USD | `+33.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,290,000.00 USD | 18,420.00 USD | 0.00 USD | `+34.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,290,000.00 USD | 933.81 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,290,000.00 USD | 658.86 USD | 0.00 USD | `+34.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,500,000.00 USD | 213,390.00 USD | 0.00 USD | `+35.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,500,000.00 USD | 560.05 USD | 0.00 USD | `+35.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+36.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,500,000.00 USD | 509.71 USD | 0.00 USD | `+36.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,500,000.00 USD | 162.15 USD | 0.00 USD | `+37.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,500,000.00 USD | 187.04 USD | 0.00 USD | `+37.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,500,000.00 USD | 542.12 USD | 0.00 USD | `+37.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,530,000.00 USD | 23,740.00 USD | 0.00 USD | `+37.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,530,000.00 USD | 2,010.00 USD | 0.00 USD | `+38.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,530,000.00 USD | 345.91 USD | 0.00 USD | `+38.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,530,000.00 USD | 104.79 USD | 0.00 USD | `+39.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,530,000.00 USD | 100.04 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,530,000.00 USD | 517.52 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,530,000.00 USD | 152.29 USD | 0.00 USD | `+40.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,530,000.00 USD | 1,480.00 USD | 0.00 USD | `+40.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,530,000.00 USD | 1,010.00 USD | 0.00 USD | `+40.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,540,000.00 USD | 2,780.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,540,000.00 USD | 340.38 USD | 0.00 USD | `+42.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,540,000.00 USD | 903.22 USD | 0.00 USD | `+42.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,540,000.00 USD | 475.01 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,580,000.00 USD | 41,160.00 USD | 0.00 USD | `+42.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,590,000.00 USD | 12,840.00 USD | 0.00 USD | `+43.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,790,000.00 USD | 194,770.00 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,800,000.00 USD | 12,890.00 USD | 0.00 USD | `+44.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,810,000.00 USD | 8,820.00 USD | 0.00 USD | `+44.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,810,000.00 USD | 466.95 USD | 0.00 USD | `+44.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,810,000.00 USD | 613.59 USD | 0.00 USD | `+44.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,810,000.00 USD | 1,420.00 USD | 0.00 USD | `+44.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,820,000.00 USD | 13,000.00 USD | 0.00 USD | `+45.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,820,000.00 USD | 284.42 USD | 0.00 USD | `+45.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,850,000.00 USD | 22,810.00 USD | 0.00 USD | `+47.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,850,000.00 USD | 640.82 USD | 0.00 USD | `+48.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,850,000.00 USD | 134.75 USD | 0.00 USD | `+48.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,860,000.00 USD | 13,400.00 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,870,000.00 USD | 13,490.00 USD | 0.00 USD | `+50.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,890,000.00 USD | 11,580.00 USD | 0.00 USD | `+50.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,890,000.00 USD | 3,610.00 USD | 0.00 USD | `+51.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,890,000.00 USD | 1,500.00 USD | 0.00 USD | `+52.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,910,000.00 USD | 15,000.00 USD | 0.00 USD | `+52.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,910,000.00 USD | 9,030.00 USD | 0.00 USD | `+53.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,920,000.00 USD | 405.86 USD | 0.00 USD | `+55.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,930,000.00 USD | 13,890.00 USD | 0.00 USD | `+55.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,940,000.00 USD | 14,000.00 USD | 0.00 USD | `+56.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,960,000.00 USD | 12,560.00 USD | 0.00 USD | `+56.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,990,000.00 USD | 32,860.00 USD | 0.00 USD | `+57.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,990,000.00 USD | 102.40 USD | 0.00 USD | `+57.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,990,000.00 USD | 106.64 USD | 0.00 USD | `+57.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,990,000.00 USD | 1,430.00 USD | 0.00 USD | `+58.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,990,000.00 USD | 2,810.00 USD | 0.00 USD | `+58.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,000,000.00 USD | 8,420.00 USD | 0.00 USD | `+58.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,000,000.00 USD | 1,410.00 USD | 0.00 USD | `+59.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,000,000.00 USD | 145.37 USD | 0.00 USD | `+60.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,000,000.00 USD | 1,390.00 USD | 0.00 USD | `+60.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,020,000.00 USD | 14,390.00 USD | 0.00 USD | `+60.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,030,000.00 USD | 7,000.00 USD | 0.00 USD | `+61.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,040,000.00 USD | 14,490.00 USD | 0.00 USD | `+61.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,040,000.00 USD | 1,370.00 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,040,000.00 USD | 1,350.00 USD | 0.00 USD | `+63.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,040,000.00 USD | 1,340.00 USD | 0.00 USD | `+63.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,040,000.00 USD | 342.08 USD | 0.00 USD | `+64.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,050,000.00 USD | 1,330.00 USD | 0.00 USD | `+64.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,060,000.00 USD | 14,890.00 USD | 0.00 USD | `+66.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,070,000.00 USD | 9,580.00 USD | 0.00 USD | `+66.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,090,000.00 USD | 14,980.00 USD | 0.00 USD | `+67.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,110,000.00 USD | 20,120.00 USD | 0.00 USD | `+67.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,110,000.00 USD | 1,180.00 USD | 0.00 USD | `+67.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,110,000.00 USD | 1,260.00 USD | 0.00 USD | `+70.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,110,000.00 USD | 2,150.00 USD | 0.00 USD | `+72.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,110,000.00 USD | 158.76 USD | 0.00 USD | `+74.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,110,000.00 USD | 574.53 USD | 0.00 USD | `+77.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,110,000.00 USD | 391.32 USD | 0.00 USD | `+78.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,110,000.00 USD | 1,160.00 USD | 0.00 USD | `+80.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,110,000.00 USD | 1,140.00 USD | 0.00 USD | `+83.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,120,000.00 USD | 1,970.00 USD | 0.00 USD | `+83.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,120,000.00 USD | 281.45 USD | 0.00 USD | `+85.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,120,000.00 USD | 2,070.00 USD | 0.00 USD | `+85.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,130,000.00 USD | 13,060.00 USD | 0.00 USD | `+90.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,130,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,130,000.00 USD | 320.52 USD | 0.00 USD | `+95.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 4,130,000.00 USD | 1,710.00 USD | 0.00 USD | `+97.37%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7350` | 15,120,000.00 USD | 0.00 USD | 15,120,000.00 USD | 69,900.00 USD | 26,690.00 USD | 51,140.00 USD |
| `7D` | `0.7370` | 14,970,000.00 USD | 0.00 USD | 14,970,000.00 USD | 38,700.00 USD | 17,190.00 USD | 32,710.00 USD |
| `7D` | `0.7390` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 27,490.00 USD | 24,560.00 USD | 26,770.00 USD |
| `7D` | `0.7410` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 18,820.00 USD | 8,780.00 USD | 29,600.00 USD |
| `7D` | `0.7430` | 14,740,000.00 USD | 0.00 USD | 14,740,000.00 USD | 44,520.00 USD | 5,210.00 USD | 33,170.00 USD |
| `7D` | `0.7450` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 34,130.00 USD | 21,270.00 USD | 43,150.00 USD |
| `7D` | `0.7470` | 14,560,000.00 USD | 0.00 USD | 14,560,000.00 USD | 23,010.00 USD | 19,630.00 USD | 24,100.00 USD |
| `7D` | `0.7490` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 26,370.00 USD | 12,290.00 USD | 5,480.00 USD |
| `7D` | `0.7510` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 10,970.00 USD | 16,630.00 USD | 21,840.00 USD |
| `7D` | `0.7530` | 14,400,000.00 USD | 0.00 USD | 14,400,000.00 USD | 1,690.00 USD | 654.10 USD | 6,820.00 USD |
| `7D` | `0.7550` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 8,700.00 USD | 6,530.00 USD | 18,880.00 USD |
| `7D` | `0.7570` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 22,280.00 USD | 16,160.00 USD | 1,880.00 USD |
| `7D` | `0.7590` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 6,840.00 USD | 25,130.00 USD | 1,190.00 USD |
| `7D` | `0.7610` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 21,310.00 USD | 16,580.00 USD | 630.66 USD |
| `7D` | `0.7630` | 14,250,000.00 USD | 0.00 USD | 14,250,000.00 USD | 20,690.00 USD | 118.70 USD | 573.15 USD |
| `7D` | `0.7650` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 556.58 USD | 23,090.00 USD | 10,340.00 USD |
| `7D` | `0.7670` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 1,280.00 USD | 3,960.00 USD | 18,920.00 USD |
| `7D` | `0.7690` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 182.28 USD | 161.63 USD | 3,150.00 USD |
| `7D` | `0.7710` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 7,690.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.7790` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 0.00 USD | 5,390.00 USD | 1,290.00 USD |
| `7D` | `0.7810` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 0.00 USD | 185.50 USD | 5,230.00 USD |
| `7D` | `0.7830` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 0.00 USD | 3,930.00 USD | 5,450.00 USD |
| `7D` | `0.7850` | 14,130,000.00 USD | 0.00 USD | 14,130,000.00 USD | 7,790.00 USD | 20,370.00 USD | 17,370.00 USD |
| `7D` | `0.7870` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 0.00 USD | 25,170.00 USD | 1,280.00 USD |
| `1D` | `0.7890` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 46,190.00 USD | 26,370.00 USD | 9,330.00 USD |
| `7D` | `0.7890` | 14,060,000.00 USD | 0.00 USD | 14,060,000.00 USD | 0.00 USD | 14,290.00 USD | 0.00 USD |
| `1D` | `0.7910` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 9,770.00 USD | 12,270.00 USD | 8,960.00 USD |
| `7D` | `0.7910` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 6,610.00 USD | 24,700.00 USD | 1,530.00 USD |
| `1D` | `0.7930` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 9,370.00 USD | 21,610.00 USD | 45,540.00 USD |
| `7D` | `0.7930` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 0.00 USD | 12,880.00 USD | 67,960.00 USD |
| `1D` | `0.7950` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 24,110.00 USD | 11,950.00 USD | 33,310.00 USD |
| `7D` | `0.7950` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 2,210.00 USD | 20,100.00 USD | 62,700.00 USD |
| `1D` | `0.7970` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 17,740.00 USD | 14,480.00 USD | 56,910.00 USD |
| `7D` | `0.7970` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 26,700.00 USD | 3,570.00 USD | 63,280.00 USD |
| `1D` | `0.7990` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 9,910.00 USD | 10,360.00 USD | 18,920.00 USD |
| `7D` | `0.7990` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 8,560.00 USD | 2,220.00 USD | 26,550.00 USD |
| `1D` | `0.8010` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 31,970.00 USD | 10,940.00 USD | 16,900.00 USD |
| `7D` | `0.8010` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 43,340.00 USD | 14,760.00 USD | 35,910.00 USD |
| `1D` | `0.8030` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 588.76 USD | 1,660.00 USD | 141.89 USD |
| `1D` | `0.8050` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 56,980.00 USD | 30,020.00 USD | 22,540.00 USD |
| `7D` | `0.8050` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 10,860.00 USD | 19,680.00 USD | 0.00 USD |
| `1D` | `0.8070` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 32,120.00 USD | 22,690.00 USD | 69,710.00 USD |
| `7D` | `0.8070` | 13,590,000.00 USD | 0.00 USD | 13,590,000.00 USD | 5,030.00 USD | 11,280.00 USD | 1,940.00 USD |
| `1D` | `0.8090` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 3,120.00 USD | 10,080.00 USD | 1,180.00 USD |
| `7D` | `0.8090` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD |
| `1D` | `0.8110` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 3,580.00 USD | 2,810.00 USD | 1,720.00 USD |
| `7D` | `0.8110` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 61,670.00 USD | 8,310.00 USD | 44,510.00 USD |
| `1D` | `0.8130` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 20,250.00 USD | 2,010.00 USD | 30,750.00 USD |
| `7D` | `0.8130` | 13,450,000.00 USD | 0.00 USD | 13,450,000.00 USD | 45,800.00 USD | 19,710.00 USD | 12,050.00 USD |
| `1D` | `0.8150` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 59,890.00 USD | 22,200.00 USD | 101,460.00 USD |
| `7D` | `0.8150` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 139,680.00 USD | 51,810.00 USD | 172,260.00 USD |
| `1D` | `0.8170` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 136,090.00 USD | 19,460.00 USD | 115,620.00 USD |
| `7D` | `0.8170` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 91,050.00 USD | 25,080.00 USD | 77,680.00 USD |
| `1D` | `0.8190` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 34,660.00 USD | 5,600.00 USD | 17,500.00 USD |
| `7D` | `0.8190` | 12,820,000.00 USD | 0.00 USD | 12,820,000.00 USD | 200,250.00 USD | 53,380.00 USD | 49,120.00 USD |
| `1D` | `0.8210` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 107,660.00 USD | 87,200.00 USD | 130,050.00 USD |
| `7D` | `0.8210` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 138,580.00 USD | 80,040.00 USD | 199,020.00 USD |
| `1D` | `0.8230` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 74,120.00 USD | 11,200.00 USD | 142,670.00 USD |
| `7D` | `0.8230` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 44,590.00 USD | 40,420.00 USD | 63,940.00 USD |
| `1D` | `0.8250` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 28,040.00 USD | 4,970.00 USD | 47,540.00 USD |
| `7D` | `0.8250` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 198,230.00 USD | 30,370.00 USD | 124,360.00 USD |
| `1D` | `0.8270` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 58,700.00 USD | 30,530.00 USD | 25,360.00 USD |
| `7D` | `0.8270` | 11,590,000.00 USD | 0.00 USD | 11,590,000.00 USD | 147,770.00 USD | 53,560.00 USD | 60,860.00 USD |
| `1D` | `0.8290` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 25,760.00 USD | 12,310.00 USD | 46,330.00 USD |
| `7D` | `0.8290` | 11,330,000.00 USD | 0.00 USD | 11,330,000.00 USD | 94,690.00 USD | 42,420.00 USD | 84,440.00 USD |
| `1D` | `0.8310` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 5,540.00 USD | 30,230.00 USD | 30,430.00 USD |
| `7D` | `0.8310` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 36,870.00 USD | 32,050.00 USD | 111,870.00 USD |
| `1D` | `0.8330` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 8,810.00 USD | 29,570.00 USD | 89,260.00 USD |
| `7D` | `0.8330` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 157,210.00 USD | 105,720.00 USD | 197,890.00 USD |
| `1D` | `0.8350` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 155,620.00 USD | 35,340.00 USD | 30,960.00 USD |
| `7D` | `0.8350` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 117,940.00 USD | 16,770.00 USD | 85,370.00 USD |
| `1D` | `0.8370` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 64,460.00 USD | 9,500.00 USD | 127,870.00 USD |
| `7D` | `0.8370` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 140,480.00 USD | 109,700.00 USD | 140,920.00 USD |
| `1D` | `0.8390` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 67,860.00 USD | 57,980.00 USD | 49,130.00 USD |
| `7D` | `0.8390` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 30,810.00 USD | 160,930.00 USD | 164,020.00 USD |
| `1D` | `0.8410` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 19,770.00 USD | 25,270.00 USD | 77,980.00 USD |
| `7D` | `0.8410` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 91,790.00 USD | 34,400.00 USD | 27,510.00 USD |
| `1D` | `0.8430` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 89,750.00 USD | 66,490.00 USD | 27,580.00 USD |
| `7D` | `0.8430` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 67,920.00 USD | 123,520.00 USD | 9,570.00 USD |
| `1D` | `0.8450` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 72,050.00 USD | 74,720.00 USD | 13,380.00 USD |
| `7D` | `0.8450` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 34,560.00 USD | 102,460.00 USD | 0.00 USD |
| `1D` | `0.8470` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 51,620.00 USD | 100,260.00 USD | 25,930.00 USD |
| `7D` | `0.8470` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 44,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8490` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 48,890.00 USD | 87,320.00 USD | 139,010.00 USD |
| `7D` | `0.8490` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 64,910.00 USD | 69,480.00 USD | 135,690.00 USD |
| `1D` | `0.8510` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 53,320.00 USD | 132,930.00 USD | 148,730.00 USD |
| `7D` | `0.8510` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 155,060.00 USD | 72,120.00 USD | 2,380.00 USD |
| `1D` | `0.8530` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 153,840.00 USD | 156,860.00 USD | 96,580.00 USD |
| `7D` | `0.8530` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 215,880.00 USD | 17,300.00 USD | 54,560.00 USD |
| `1D` | `0.8550` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 1,920.00 USD | 17,460.00 USD | 485.01 USD |
| `7D` | `0.8550` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 78,320.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `0.8570` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 0.00 USD | 19,770.00 USD | 46,020.00 USD |
| `7D` | `0.8570` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 99,680.00 USD | 55,310.00 USD | 39,460.00 USD |
| `1D` | `0.8590` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 46,710.00 USD | 60,770.00 USD | 49,870.00 USD |
| `7D` | `0.8590` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 132,610.00 USD | 56,980.00 USD | 2,210.00 USD |
| `1D` | `0.8610` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 79,530.00 USD | 23,780.00 USD | 224.25 USD |
| `7D` | `0.8610` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 36,870.00 USD | 188,190.00 USD | 32,650.00 USD |
| `1D` | `0.8630` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 91,300.00 USD | 124,490.00 USD | 124,360.00 USD |
| `7D` | `0.8630` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 100,980.00 USD | 64,400.00 USD | 387,000.00 USD |
| `1D` | `0.8650` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 28,850.00 USD | 52,640.00 USD | 112,440.00 USD |
| `7D` | `0.8650` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 254,940.00 USD | 106,760.00 USD | 564,020.00 USD |
| `1D` | `0.8670` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 212,100.00 USD | 25,640.00 USD | 180,460.00 USD |
| `7D` | `0.8670` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 252,430.00 USD | 0.00 USD | 128,870.00 USD |
| `1D` | `0.8690` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 27,920.00 USD | 0.00 USD | 25,440.00 USD |
| `7D` | `0.8690` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 109,170.00 USD |
| `1D` | `0.8710` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 152,210.00 USD | 100,950.00 USD | 176,610.00 USD |
| `7D` | `0.8710` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 207,250.00 USD | 34,600.00 USD | 11,670.00 USD |
| `1D` | `0.8730` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 85,660.00 USD | 0.00 USD | 21,060.00 USD |
| `7D` | `0.8730` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 87,530.00 USD |
| `1D` | `0.8750` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 117,080.00 USD |
| `7D` | `0.8750` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 26,230.00 USD | 0.00 USD | 257,780.00 USD |
| `1D` | `0.8770` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 27,620.00 USD | 20,280.00 USD | 122,740.00 USD |
| `7D` | `0.8770` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 3,440.00 USD |
| `1D` | `0.8790` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 79,990.00 USD | 0.00 USD | 1,000.00 USD |
| `7D` | `0.8790` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 3,300.00 USD |
| `1D` | `0.8810` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 41,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8810` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 20,310.00 USD | 3,570.00 USD | 576.82 USD |
| `1D` | `0.8830` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 2,260.00 USD | 94,270.00 USD |
| `7D` | `0.8830` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 0.00 USD | 25,990.00 USD | 5,630.00 USD |
| `1D` | `0.8850` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 30,450.00 USD | 0.00 USD | 24,220.00 USD |
| `7D` | `0.8850` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 0.00 USD | 35,900.00 USD | 0.00 USD |
| `1D` | `0.8870` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD |
| `7D` | `0.8870` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 3,050.00 USD |
| `1D` | `0.8890` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 122,200.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `0.8890` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 8,820.00 USD | 3,860.00 USD | 5,380.00 USD |
| `1D` | `0.8910` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 138,820.00 USD | 0.00 USD | 61,060.00 USD |
| `7D` | `0.8910` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 523,470.00 USD | 55,310.00 USD | 4,740.00 USD |
| `1D` | `0.8930` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 69,970.00 USD | 18,820.00 USD | 208.28 USD |
| `7D` | `0.8930` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 1,750,000.00 USD | 0.00 USD | 728.40 USD |
| `1D` | `0.8950` | 977,420.00 USD | 0.00 USD | 977,420.00 USD | 134,710.00 USD | 99,420.00 USD | 975.22 USD |
| `7D` | `0.8950` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 800,940.00 USD | 68,760.00 USD | 3,460.00 USD |
| `1D` | `0.8970` | 742,310.00 USD | 0.00 USD | 742,310.00 USD | 969.20 USD | 58,730.00 USD | 1,280.00 USD |
| `7D` | `0.8970` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 634,760.00 USD | 93,070.00 USD | 11,160.00 USD |
| `1D` | `0.8990` | 681,330.00 USD | 0.00 USD | 681,330.00 USD | 143,990.00 USD | 181,310.00 USD | 356,030.00 USD |
| `7D` | `0.8990` | 786,750.00 USD | 0.00 USD | 786,750.00 USD | 379,180.00 USD | 67,360.00 USD | 340,220.00 USD |
| `1D` | `0.9000` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9000` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9010` | 328,070.00 USD | 328,070.00 USD | 0.00 USD | 170,400.00 USD | 156,270.00 USD | 1,400.00 USD |
| `7D` | `0.9010` | 681,560.00 USD | 681,560.00 USD | 0.00 USD | 207,550.00 USD | 97,520.00 USD | 376,490.00 USD |
| `1D` | `0.9030` | 477,810.00 USD | 477,810.00 USD | 0.00 USD | 8,120.00 USD | 140,180.00 USD | 1,440.00 USD |
| `7D` | `0.9030` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 124,030.00 USD | 99,390.00 USD | 106,470.00 USD |
| `1D` | `0.9050` | 928,680.00 USD | 928,680.00 USD | 0.00 USD | 243,190.00 USD | 162,620.00 USD | 45,060.00 USD |
| `7D` | `0.9050` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 169,680.00 USD | 0.00 USD | 323,290.00 USD |
| `1D` | `0.9070` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 303,340.00 USD | 227,560.00 USD | 274,910.00 USD |
| `7D` | `0.9070` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 548,330.00 USD | 85,530.00 USD | 42,890.00 USD |
| `1D` | `0.9090` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 190,800.00 USD | 28,990.00 USD | 18,490.00 USD |
| `7D` | `0.9090` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 60,680.00 USD | 142,850.00 USD | 179,540.00 USD |
| `1D` | `0.9110` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 90,400.00 USD | 46,460.00 USD | 50,030.00 USD |
| `7D` | `0.9110` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 259,120.00 USD | 103,750.00 USD | 71,100.00 USD |
| `1D` | `0.9130` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 78,640.00 USD | 106,560.00 USD | 135,580.00 USD |
| `7D` | `0.9130` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 80,230.00 USD | 86,960.00 USD | 0.00 USD |
| `1D` | `0.9150` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 233,130.00 USD | 113,310.00 USD | 315,460.00 USD |
| `7D` | `0.9150` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD |
| `1D` | `0.9170` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 124,750.00 USD | 127,130.00 USD | 89,140.00 USD |
| `7D` | `0.9170` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 163,880.00 USD | 2,050.00 USD | 2,550.00 USD |
| `1D` | `0.9190` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 75,990.00 USD | 41,040.00 USD | 106,030.00 USD |
| `7D` | `0.9190` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 296,480.00 USD | 86,790.00 USD | 238,200.00 USD |
| `1D` | `0.9210` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 129,450.00 USD | 67,170.00 USD | 211,830.00 USD |
| `7D` | `0.9210` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 194,470.00 USD | 18,660.00 USD | 173,150.00 USD |
| `1D` | `0.9230` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 236,260.00 USD | 88,490.00 USD | 288,600.00 USD |
| `7D` | `0.9230` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 56,540.00 USD | 68,150.00 USD | 398,340.00 USD |
| `1D` | `0.9250` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 265,410.00 USD | 90,560.00 USD | 171,230.00 USD |
| `7D` | `0.9250` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 158,890.00 USD | 63,010.00 USD | 69,190.00 USD |
| `1D` | `0.9270` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 3,590.00 USD | 103,030.00 USD | 64,530.00 USD |
| `7D` | `0.9270` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 220,880.00 USD | 46,830.00 USD | 89,770.00 USD |
| `1D` | `0.9290` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 43,130.00 USD | 23,020.00 USD | 104,150.00 USD |
| `7D` | `0.9290` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 4,480.00 USD | 53,740.00 USD | 38,220.00 USD |
| `1D` | `0.9310` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 123,440.00 USD | 75,260.00 USD | 93,780.00 USD |
| `7D` | `0.9310` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 181,630.00 USD | 50,140.00 USD | 168,120.00 USD |
| `1D` | `0.9330` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 75,580.00 USD | 39,640.00 USD | 35,660.00 USD |
| `7D` | `0.9330` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 4,410.00 USD | 76,570.00 USD | 63,160.00 USD |
| `1D` | `0.9350` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 2,160.00 USD | 16,790.00 USD | 0.00 USD |
| `7D` | `0.9350` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 53,950.00 USD | 55,880.00 USD | 0.00 USD |
| `1D` | `0.9370` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 128,220.00 USD | 71,160.00 USD | 190,710.00 USD |
| `7D` | `0.9370` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 256,610.00 USD | 18,150.00 USD | 44,240.00 USD |
| `1D` | `0.9390` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 54,270.00 USD | 11,160.00 USD | 140,190.00 USD |
| `7D` | `0.9390` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 86,850.00 USD | 36,340.00 USD | 266,510.00 USD |
| `1D` | `0.9410` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 60,820.00 USD | 14,850.00 USD | 58,830.00 USD |
| `7D` | `0.9410` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 123,000.00 USD | 6,050.00 USD | 0.00 USD |
| `1D` | `0.9430` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 1,630.00 USD | 3,360.00 USD | 24,470.00 USD |
| `7D` | `0.9430` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 4,970.00 USD | 68,030.00 USD | 33,660.00 USD |
| `1D` | `0.9450` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 9,780.00 USD | 36,750.00 USD | 190,260.00 USD |
| `7D` | `0.9450` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 3,360.00 USD | 244,270.00 USD | 94,130.00 USD |
| `1D` | `0.9470` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 93,380.00 USD | 56,310.00 USD | 44,830.00 USD |
| `7D` | `0.9470` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `1D` | `0.9490` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 72,890.00 USD | 62,860.00 USD | 58,640.00 USD |
| `7D` | `0.9490` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD |
| `1D` | `0.9510` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 60,880.00 USD | 50,330.00 USD | 175,900.00 USD |
| `7D` | `0.9510` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 2,840.00 USD | 88,970.00 USD | 734,250.00 USD |
| `1D` | `0.9530` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 32,110.00 USD | 26,880.00 USD | 150,150.00 USD |
| `7D` | `0.9530` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD |
| `1D` | `0.9550` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 48,260.00 USD | 40,160.00 USD | 52,890.00 USD |
| `7D` | `0.9550` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 74,980.00 USD | 2,400.00 USD | 60,300.00 USD |
| `1D` | `0.9570` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 36,890.00 USD | 13,960.00 USD | 23,450.00 USD |
| `7D` | `0.9570` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 463,830.00 USD | 4,720.00 USD | 2,940.00 USD |
| `1D` | `0.9590` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 44,640.00 USD | 69,890.00 USD | 12,880.00 USD |
| `7D` | `0.9590` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 563,790.00 USD | 21,410.00 USD | 3,520.00 USD |
| `1D` | `0.9610` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 207,550.00 USD | 76,640.00 USD | 244,830.00 USD |
| `7D` | `0.9610` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 698,570.00 USD | 201,530.00 USD | 480,590.00 USD |
| `1D` | `0.9630` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 241,720.00 USD | 43,610.00 USD | 63,410.00 USD |
| `7D` | `0.9630` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 579,300.00 USD | 301,610.00 USD | 624,890.00 USD |
| `1D` | `0.9650` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 145,180.00 USD | 112,750.00 USD | 79,120.00 USD |
| `7D` | `0.9650` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 857,470.00 USD | 312,610.00 USD | 408,950.00 USD |
| `1D` | `0.9670` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 230,840.00 USD | 111,230.00 USD | 233,640.00 USD |
| `7D` | `0.9670` | 16,840,000.00 USD | 16,840,000.00 USD | 0.00 USD | 801,890.00 USD | 555,340.00 USD | 616,730.00 USD |
| `1D` | `0.9690` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 244,130.00 USD | 85,700.00 USD | 241,970.00 USD |
| `7D` | `0.9690` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 596,350.00 USD | 312,990.00 USD | 398,260.00 USD |
| `1D` | `0.9710` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 173,950.00 USD | 66,390.00 USD | 123,570.00 USD |
| `7D` | `0.9710` | 19,270,000.00 USD | 19,270,000.00 USD | 0.00 USD | 647,710.00 USD | 319,140.00 USD | 146,570.00 USD |
| `1D` | `0.9730` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 61,720.00 USD | 37,940.00 USD | 50,990.00 USD |
| `7D` | `0.9730` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 456,990.00 USD | 160,420.00 USD | 192,990.00 USD |
| `1D` | `0.9750` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 32,420.00 USD | 30,100.00 USD | 128,650.00 USD |
| `7D` | `0.9750` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 227,380.00 USD | 293,590.00 USD | 223,590.00 USD |
| `1D` | `0.9770` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 4,790.00 USD | 11,480.00 USD | 32,020.00 USD |
| `7D` | `0.9770` | 21,890,000.00 USD | 21,890,000.00 USD | 0.00 USD | 329,170.00 USD | 211,000.00 USD | 524,320.00 USD |
| `1D` | `0.9790` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 46,560.00 USD | 32,950.00 USD | 103,400.00 USD |
| `7D` | `0.9790` | 22,520,000.00 USD | 22,520,000.00 USD | 0.00 USD | 342,340.00 USD | 72,140.00 USD | 223,900.00 USD |
| `1D` | `0.9810` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 87,820.00 USD | 31,320.00 USD | 75,360.00 USD |
| `7D` | `0.9810` | 22,960,000.00 USD | 22,960,000.00 USD | 0.00 USD | 206,910.00 USD | 60,620.00 USD | 166,860.00 USD |
| `1D` | `0.9830` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 62,950.00 USD | 22,530.00 USD | 47.72 USD |
| `7D` | `0.9830` | 23,540,000.00 USD | 23,540,000.00 USD | 0.00 USD | 262,900.00 USD | 116,030.00 USD | 200,330.00 USD |
| `1D` | `0.9850` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 21,080.00 USD | 42,480.00 USD | 15,170.00 USD |
| `7D` | `0.9850` | 23,950,000.00 USD | 23,950,000.00 USD | 0.00 USD | 234,160.00 USD | 58,210.00 USD | 117,390.00 USD |
| `1D` | `0.9870` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 72,760.00 USD | 30,670.00 USD | 97,950.00 USD |
| `7D` | `0.9870` | 24,460,000.00 USD | 24,460,000.00 USD | 0.00 USD | 248,980.00 USD | 203,100.00 USD | 57,080.00 USD |
| `1D` | `0.9890` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 100,210.00 USD | 31,480.00 USD | 34,040.00 USD |
| `7D` | `0.9890` | 24,750,000.00 USD | 24,750,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 18,200.00 USD |
| `1D` | `0.9910` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 40,670.00 USD | 24,540.00 USD | 25,770.00 USD |
| `7D` | `0.9910` | 25,120,000.00 USD | 25,120,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 84,050.00 USD |
| `1D` | `0.9930` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 20,890.00 USD | 3,890.00 USD | 16,120.00 USD |
| `7D` | `0.9930` | 25,490,000.00 USD | 25,490,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 72,830.00 USD |
| `1D` | `0.9950` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 36,320.00 USD | 19,930.00 USD | 54,740.00 USD |
| `7D` | `0.9950` | 25,800,000.00 USD | 25,800,000.00 USD | 0.00 USD | 48,120.00 USD | 138,500.00 USD | 125,920.00 USD |
| `1D` | `0.9970` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 36,450.00 USD | 11,490.00 USD | 103,270.00 USD |
| `7D` | `0.9970` | 26,450,000.00 USD | 26,450,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 360,870.00 USD |
| `1D` | `0.9980` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 61,500.00 USD | 8,720.00 USD | 65,440.00 USD |
| `7D` | `0.9990` | 26,740,000.00 USD | 26,740,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 101,850.00 USD |
| `7D` | `1.00` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 202,970.00 USD | 57,170.00 USD | 183,960.00 USD |
| `7D` | `1.00` | 27,680,000.00 USD | 27,680,000.00 USD | 0.00 USD | 226,340.00 USD | 61,540.00 USD | 206,730.00 USD |
| `7D` | `1.00` | 27,830,000.00 USD | 27,830,000.00 USD | 0.00 USD | 51,930.00 USD | 39,560.00 USD | 66,390.00 USD |
| `7D` | `1.01` | 28,140,000.00 USD | 28,140,000.00 USD | 0.00 USD | 168,320.00 USD | 16,800.00 USD | 121,550.00 USD |
| `7D` | `1.01` | 28,610,000.00 USD | 28,610,000.00 USD | 0.00 USD | 247,480.00 USD | 61,720.00 USD | 157,960.00 USD |
| `7D` | `1.01` | 29,060,000.00 USD | 29,060,000.00 USD | 0.00 USD | 301,110.00 USD | 84,080.00 USD | 62,420.00 USD |
| `7D` | `1.01` | 29,540,000.00 USD | 29,540,000.00 USD | 0.00 USD | 188,370.00 USD | 121,340.00 USD | 171,740.00 USD |
| `7D` | `1.01` | 29,890,000.00 USD | 29,890,000.00 USD | 0.00 USD | 168,660.00 USD | 60,680.00 USD | 126,540.00 USD |
| `7D` | `1.02` | 30,370,000.00 USD | 30,370,000.00 USD | 0.00 USD | 148,890.00 USD | 62,970.00 USD | 266,660.00 USD |
| `7D` | `1.02` | 30,840,000.00 USD | 30,840,000.00 USD | 0.00 USD | 180,470.00 USD | 47,380.00 USD | 243,860.00 USD |
| `7D` | `1.02` | 31,110,000.00 USD | 31,110,000.00 USD | 0.00 USD | 95,590.00 USD | 18,960.00 USD | 149,860.00 USD |
| `7D` | `1.02` | 31,420,000.00 USD | 31,420,000.00 USD | 0.00 USD | 151,650.00 USD | 61,120.00 USD | 103,400.00 USD |
| `7D` | `1.02` | 31,620,000.00 USD | 31,620,000.00 USD | 0.00 USD | 59,440.00 USD | 54,210.00 USD | 78,550.00 USD |
| `7D` | `1.03` | 31,810,000.00 USD | 31,810,000.00 USD | 0.00 USD | 76,740.00 USD | 35,970.00 USD | 82,630.00 USD |
| `7D` | `1.03` | 31,950,000.00 USD | 31,950,000.00 USD | 0.00 USD | 85,920.00 USD | 34,530.00 USD | 21,710.00 USD |
| `7D` | `1.03` | 32,140,000.00 USD | 32,140,000.00 USD | 0.00 USD | 119,110.00 USD | 33,520.00 USD | 29,670.00 USD |
| `7D` | `1.03` | 32,350,000.00 USD | 32,350,000.00 USD | 0.00 USD | 57,570.00 USD | 75,720.00 USD | 76,670.00 USD |
| `7D` | `1.03` | 32,490,000.00 USD | 32,490,000.00 USD | 0.00 USD | 64,880.00 USD | 13,040.00 USD | 63,350.00 USD |
| `7D` | `1.04` | 32,720,000.00 USD | 32,720,000.00 USD | 0.00 USD | 79,670.00 USD | 20,460.00 USD | 134,080.00 USD |
| `7D` | `1.04` | 32,840,000.00 USD | 32,840,000.00 USD | 0.00 USD | 53,800.00 USD | 0.00 USD | 63,320.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `579.90M` | Total OI Tokens: `644,616,116.9 SUI`
  * 1h OI Change: `+0.37%` | 4h OI Change: `+4.21%` | 24h OI Change: `-6.05%`
  * Exchange Breakdown: Binance=`104.69M` | Bybit=`77.78M` | OKX=`33.38M` | Hyperliquid=`30.10M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-20.14K` | Last 24h: `-2.19K` | Last 3d: `56.09K` | Last 7d: `151.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0045%` | **USDT OKX** | `-0.0055%` |
| **USDT Bybit** | `-0.0200%` | **USDT KuCoin** | `0.0000%` |
| **USDT MEXC** | `-0.0046%` | **USDT BingX** | `-0.0039%` |
| **USDT Gate** | `-0.0065%` | **USDT Bitget** | `-0.0145%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `50.98%` | `49.02%` | `1.04` | 2,810,000.00 USD |
| `15M` | `Binance` | `53.4%` | `46.6%` | `1.15` | 892,870.00 USD |
| `15M` | `OKX` | `33%` | `67%` | `0.49` | 243,680.00 USD |
| `15M` | `Bybit` | `43.34%` | `56.66%` | `0.76` | 228,320.00 USD |
| `15M` | `KuCoin` | `41.93%` | `58.07%` | `0.72` | 15,780.00 USD |
| `15M` | `Gate` | `31.8%` | `68.2%` | `0.47` | 72,220.00 USD |
| `15M` | `Bitget` | `41.02%` | `58.98%` | `0.70` | 51,440.00 USD |
| `15M` | `BingX` | `43.28%` | `56.72%` | `0.76` | 787,460.00 USD |
| `15M` | `MEXC` | `54.68%` | `45.32%` | `1.21` | 44,760.00 USD |
| `15M` | `Bitunix` | `39.34%` | `60.66%` | `0.65` | 55,910.00 USD |
| `15M` | `Hyperliquid` | `64.67%` | `35.33%` | `1.83` | 7,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.04%` | `55.96%` | `0.79` | 396,510.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 6.84 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 12,510.00 USD |
| `15M` | `HTX` | `80.94%` | `19.06%` | `4.25` | 711.27 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `99.97%` | `0.03%` | `3332.33` | 77.17 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `1.1%` | `98.9%` | `0.01` | 1,370.00 USD |
| `15M` | `Whale Positions` | `53.4%` | `46.6%` | `1.15` | 892,870.00 USD |
| `15M` | `Global Accounts` | `50.98%` | `49.02%` | `1.04` | 2,810,000.00 USD |
| `1H` | `SUI` | `48.74%` | `51.26%` | `0.95` | 17,460,000.00 USD |
| `1H` | `Binance` | `52.83%` | `47.17%` | `1.12` | 6,620,000.00 USD |
| `1H` | `OKX` | `36.61%` | `63.39%` | `0.58` | 1,190,000.00 USD |
| `1H` | `Bybit` | `45.79%` | `54.21%` | `0.84` | 1,310,000.00 USD |
| `1H` | `KuCoin` | `58.4%` | `41.6%` | `1.40` | 58,060.00 USD |
| `1H` | `Gate` | `57.11%` | `42.89%` | `1.33` | 405,100.00 USD |
| `1H` | `Bitget` | `55.05%` | `44.95%` | `1.22` | 289,230.00 USD |
| `1H` | `BingX` | `47.9%` | `52.1%` | `0.92` | 3,130,000.00 USD |
| `1H` | `MEXC` | `54.2%` | `45.8%` | `1.18` | 641,980.00 USD |
| `1H` | `Bitunix` | `42.94%` | `57.06%` | `0.75` | 308,230.00 USD |
| `1H` | `Hyperliquid` | `72.68%` | `27.32%` | `2.66` | 81,990.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.54%` | `57.46%` | `0.74` | 3,250,000.00 USD |
| `1H` | `Crypto.com` | `51.24%` | `48.76%` | `1.05` | 34.97 USD |
| `1H` | `WhiteBIT` | `77.54%` | `22.46%` | `3.45` | 85,930.00 USD |
| `1H` | `HTX` | `41.59%` | `58.41%` | `0.71` | 6,260.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `93.82%` | `6.18%` | `15.18` | 42,120.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `55.37%` | `44.63%` | `1.24` | 31,620.00 USD |
| `1H` | `Whale Positions` | `52.83%` | `47.17%` | `1.12` | 6,620,000.00 USD |
| `1H` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 17,460,000.00 USD |
| `4H` | `SUI` | `48.32%` | `51.68%` | `0.93` | 68,230,000.00 USD |
| `4H` | `Binance` | `55.23%` | `44.77%` | `1.23` | 23,520,000.00 USD |
| `4H` | `OKX` | `46.37%` | `53.63%` | `0.86` | 3,800,000.00 USD |
| `4H` | `Bybit` | `51.9%` | `48.1%` | `1.08` | 5,200,000.00 USD |
| `4H` | `KuCoin` | `51.72%` | `48.28%` | `1.07` | 534,960.00 USD |
| `4H` | `Gate` | `44.56%` | `55.44%` | `0.80` | 1,880,000.00 USD |
| `4H` | `Bitget` | `53.17%` | `46.83%` | `1.14` | 1,150,000.00 USD |
| `4H` | `BingX` | `38.45%` | `61.55%` | `0.62` | 14,430,000.00 USD |
| `4H` | `MEXC` | `52.43%` | `47.57%` | `1.10` | 2,630,000.00 USD |
| `4H` | `Bitunix` | `50.6%` | `49.4%` | `1.02` | 1,400,000.00 USD |
| `4H` | `Hyperliquid` | `38.86%` | `61.14%` | `0.64` | 1,370,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `46.41%` | `53.59%` | `0.87` | 11,330,000.00 USD |
| `4H` | `Crypto.com` | `20.02%` | `79.98%` | `0.25` | 4,410.00 USD |
| `4H` | `WhiteBIT` | `25.55%` | `74.45%` | `0.34` | 520,590.00 USD |
| `4H` | `HTX` | `59.2%` | `40.8%` | `1.45` | 28,530.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.52%` | `50.48%` | `0.98` | 130,410.00 USD |
| `4H` | `Aster` | `89.42%` | `10.58%` | `8.45` | 66,880.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.06%` | `60.94%` | `0.64` | 221,050.00 USD |
| `4H` | `Whale Positions` | `55.23%` | `44.77%` | `1.23` | 23,520,000.00 USD |
| `4H` | `Global Accounts` | `48.32%` | `51.68%` | `0.93` | 68,230,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.8700` | `0.8715` | `0.8700` | `0.8748` | `0.8669` | 2,353,506.52 USD | 1,517,666.93 USD | 835,839.59 USD | 681,827.34 USD | `+28.97%` | `29B / 5S` |
| `0:00 UTC` | `0.8800` | `0.8785` | `0.8800` | `0.8828` | `0.8730` | 3,913,129.55 USD | 2,396,328.40 USD | 1,516,801.15 USD | 879,527.25 USD | `+22.48%` | `20B / 6S` |
| `5:00 UTC` | `0.8851` | `0.8843` | `0.8851` | `0.8873` | `0.8813` | 3,303,378.86 USD | 1,747,933.70 USD | 1,555,445.16 USD | 192,488.53 USD | `+5.83%` | `6B / 8S` |
| `0:00 UTC` | `0.8790` | `0.8806` | `0.8790` | `0.8870` | `0.8778` | 3,823,669.01 USD | 1,840,836.89 USD | 1,982,832.12 USD | -141,995.24 USD | `-3.71%` | `23B / 14S` |
| `5:00 UTC` | `0.8903` | `0.8884` | `0.8903` | `0.8908` | `0.8844` | 3,559,512.45 USD | 1,938,272.96 USD | 1,621,239.49 USD | 317,033.48 USD | `+8.91%` | `9B / 6S` |
| `0:00 UTC` | `0.8865` | `0.8876` | `0.8865` | `0.8905` | `0.8850` | 2,686,854.06 USD | 1,226,021.69 USD | 1,460,832.37 USD | -234,810.69 USD | `-8.74%` | `3B / 8S` |
| `5:00 UTC` | `0.8950` | `0.8939` | `0.8950` | `0.8966` | `0.8897` | 3,990,383.01 USD | 1,854,959.02 USD | 2,135,424.00 USD | -280,464.98 USD | `-7.03%` | `14B / 6S` |
| `0:00 UTC` | `0.9031` | `0.9000` | `0.9031` | `0.9050` | `0.8941` | 7,284,926.68 USD | 3,459,713.58 USD | 3,825,213.10 USD | -365,499.52 USD | `-5.02%` | `21B / 11S` |
| `5:00 UTC` | `0.9010` | `0.9015` | `0.9010` | `0.9032` | `0.9001` | 2,342,731.18 USD | 1,068,506.03 USD | 1,274,225.14 USD | -205,719.11 USD | `-8.78%` | `0B / 2S` |
| `0:00 UTC` | `0.9001` | `0.8998` | `0.9001` | `0.9021` | `0.8978` | 1,862,366.04 USD | 740,552.75 USD | 1,121,813.29 USD | -381,260.54 USD | `-20.47%` | `0B / 13S` |

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
| `5m` | -312,550.00 USD | -176,490.00 USD | **`DISTRIBUTION`** |
| `15m` | -311,480.00 USD | -538,050.00 USD | **`DISTRIBUTION`** |
| `30m` | 52,170.00 USD | -1,150,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 1,620,000.00 USD | -2,220,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,190,000.00 USD | -112,810.00 USD | **`ACCUMULATION`** |
| `4h` | 3,090,000.00 USD | 3,030,000.00 USD | **`ACCUMULATION`** |
| `6h` | -4,620,000.00 USD | -10,130,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -3,770,000.00 USD | -21,800,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -12,930,000.00 USD | -24,540,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,780,000.00 USD | -26,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -25,720,000.00 USD | -88,670,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -155,850,000.00 USD | -486,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-312.55K` | 15m=`-311.48K` | 1h=`+1.62M` | 24h=`-7.78M`
* Futures Capital Netflows: 5m=`-176.49K` | 15m=`-538.05K` | 1h=`-2.22M` | 24h=`-26.52M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
