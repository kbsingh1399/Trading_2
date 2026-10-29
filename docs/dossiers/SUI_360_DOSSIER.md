# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:55:04 IST` (`2026-10-29 17:25:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.9442` | `0.9452` | `0.9416` | `0.9416` | `508,582` | 479,880.63 USD | -143,558.24 USD | `-29.92%` | -6,652,259.37 USD | `-0.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9416` | `0.9429` | `0.9406` | `0.9407` | `947,224` | 891,992.86 USD | 49,236.03 USD | `+5.52%` | -6,603,023.34 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9407` | `0.9435` | `0.9405` | `0.9435` | `870,411` | 820,291.05 USD | 343,466.96 USD | `+41.87%` | -6,259,556.38 USD | `+1.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9470` | `0.9483` | `0.9443` | `0.9474` | `1,537,534` | 1,455,719.43 USD | -110,489.71 USD | `-7.59%` | -6,108,115.27 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9475` | `0.9481` | `0.9416` | `0.9416` | `2,004,760` | 1,894,016.62 USD | -554,262.60 USD | `-29.26%` | -6,662,377.87 USD | `-1.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9416` | `0.9435` | `0.9405` | `0.9435` | `1,817,635` | 1,712,283.91 USD | 392,702.99 USD | `+22.93%` | -6,269,674.88 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.9418` | `0.9548` | `0.9405` | `0.9539` | `12,091,008` | 11,471,016.76 USD | 18,231.41 USD | `+0.16%` | -5,532,614.90 USD | `+0.36` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9539` | `0.9617` | `0.9424` | `0.9474` | `16,224,609` | 15,442,165.70 USD | -1,242,937.53 USD | `-8.05%` | -6,775,552.42 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9475` | `0.9481` | `0.9405` | `0.9433` | `3,815,996` | 3,600,264.94 USD | -167,455.03 USD | `-4.65%` | -6,943,007.45 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -10,284,836.62 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -8,256,119.70 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9405` | `0.9435` | `20,047,004` | 19,048,466.23 USD | -1,404,497.13 USD | `-7.37%` | -9,660,616.83 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9429` | `0.9465` | `0.8981` | `0.9043` | `62,278,068` | 57,050,963.40 USD | -8,597,484.18 USD | `-15.07%` | -10,264,352.04 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -10,145,601.55 USD | `+0.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -10,284,836.62 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -8,256,119.70 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9405` | `0.9435` | `20,047,004` | 19,048,466.23 USD | -1,404,497.13 USD | `-7.37%` | -9,660,616.83 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.9431` | `500.0000` | 471.57 USD | 34,433.58 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9431` | `2544.5000` | 2,399.79 USD | 36,833.37 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9431` | `500.0000` | 471.55 USD | 37,304.92 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9431` | `2210.7000` | 2,084.89 USD | 39,389.81 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9431` | `17684.3000` | 16,677.71 USD | 56,067.52 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9431` | `5307.5000` | 5,005.34 USD | 61,072.87 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9432` | `8684.4000` | 8,191.47 USD | 23,652.81 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.9432` | `2120.3000` | 1,999.93 USD | 25,652.74 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9432` | `2210.6000` | 2,084.99 USD | 27,737.74 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9432` | `2210.7000` | 2,085.07 USD | 29,822.80 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9432` | `500.0000` | 471.58 USD | 30,294.38 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9432` | `3888.7000` | 3,667.63 USD | 33,962.01 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.9433` | `2210.6000` | 2,085.35 USD | 8,956.25 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9433` | `2210.7000` | 2,085.42 USD | 11,041.66 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9433` | `2474.7000` | 2,334.41 USD | 13,376.07 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.9433` | `2210.7000` | 2,085.26 USD | 15,461.34 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9434` | `2672.7000` | 2,521.48 USD | 3,522.49 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.9434` | `1061.1000` | 1,001.02 USD | 4,523.51 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9434` | `2488.3000` | 2,347.39 USD | 6,870.90 USD | `1 orders` | `-0.02%` | `-` |
| `MID_SPREAD` | `0.9435` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.94` | `0.00%` | `-` |
| `BID` | `0.9435` | `1061.0000` | 1,001.01 USD | 1,001.01 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `0.9436` | `400.0000` | 377.46 USD | 388.50 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9436` | `11.7000` | 11.04 USD | 11.04 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9437` | `400.0000` | 377.49 USD | 3,453.58 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9437` | `1401.0000` | 1,322.11 USD | 3,076.09 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.9437` | `386.2000` | 364.45 USD | 1,753.98 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.9437` | `1060.8000` | 1,001.03 USD | 1,389.53 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9438` | `447.7000` | 422.56 USD | 9,088.96 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9438` | `2119.0000` | 1,999.98 USD | 8,666.41 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9438` | `3404.2000` | 3,212.85 USD | 6,666.43 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9439` | `5802.7000` | 5,477.46 USD | 34,863.51 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.9439` | `1562.8000` | 1,475.19 USD | 29,386.05 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.9439` | `52.9000` | 49.93 USD | 27,910.86 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9439` | `7513.5000` | 7,092.14 USD | 27,860.92 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.9439` | `2079.4000` | 1,962.75 USD | 20,768.78 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.9439` | `2210.7000` | 2,086.66 USD | 18,806.04 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9439` | `6113.2000` | 5,770.07 USD | 16,719.38 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.9439` | `1971.0000` | 1,860.35 USD | 10,949.31 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9440` | `2210.7000` | 2,086.88 USD | 42,190.86 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9440` | `4237.5000` | 4,000.12 USD | 40,103.99 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9440` | `1314.0000` | 1,240.36 USD | 36,103.87 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `664` | `0xb83d...6e36` | `SHORT` | 3,595,195.48 USD | `3,817,609.40` | `1.11` | `0.9419` | `32.66` | 623,539.84 USD | `+17.34%` | `3X Cross` |
| `983` | `0xa2ce...3126` | `LONG` | 2,354,634.80 USD | `2,500,010.40` | `0.8597` | `0.9419` | `0.000000` | 205,428.26 USD | `+8.72%` | `10X Cross` |
| `1468` | `0x9946...0852` | `SHORT` | 1,567,562.16 USD | `1,664,573.50` | `1.08` | `0.9419` | `1.52` | 228,757.45 USD | `+14.59%` | `10X Cross` |
| `1785` | `0x9aa5...58af` | `SHORT` | 1,215,387.26 USD | `1,288,168.80` | `1.14` | `0.9419` | `6.39` | 252,305.62 USD | `+20.76%` | `10X Cross` |
| `1890` | `0x9df2...c665` | `SHORT` | 1,130,304.00 USD | `1,200,000.00` | `0.7465` | `0.9419` | `24.00` | -234,451.60 USD | `-20.74%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9265` | 5,006.50 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9265 USD [API] | `2026-10-27 19:39:00` |
| `ANNOUNCEMENT` | `INFO` | `0.9288` | 5,006.32 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9288 USD [API] | `2026-10-27 19:45:33` |
| `ANNOUNCEMENT` | `INFO` | `0.9283` | 15,178.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 15.18K USD at 0.9283 USD [API] | `2026-10-27 19:47:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 5,006.90 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9297 USD [API] | `2026-10-27 21:45:02` |
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 12,732.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 12.73K USD at 0.9297 USD [API] | `2026-10-27 21:45:02` |
| `ANNOUNCEMENT` | `INFO` | `0.9310` | 7,756.86 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 7.76K USD at 0.9310 USD [API] | `2026-10-27 21:46:21` |
| `ANNOUNCEMENT` | `INFO` | `0.9292` | 10,211.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.21K USD at 0.9292 USD [API] | `2026-10-27 21:53:25` |
| `ANNOUNCEMENT` | `INFO` | `0.9292` | 10,211.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.21K USD at 0.9292 USD [API] | `2026-10-27 21:53:25` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9706` (Vol: 378,700.00 USD, Dist: `+3.15%`) | Long MP=`0.8887` (Vol: 546,500.00 USD, Dist: `--5.56%`)
  * 48H Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+3.15%`) | Long MP=`0.8887` (Vol: 546,500.00 USD, Dist: `--5.56%`)
  * 3D Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+3.15%`) | Long MP=`0.8887` (Vol: 859,700.00 USD, Dist: `--5.56%`)
  * 7D Horizon: Short MP=`0.9685` (Vol: 565,100.00 USD, Dist: `+2.92%`) | Long MP=`0.8890` (Vol: 1,100,000.00 USD, Dist: `--5.53%`)
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
| `7D` | `Long Liquidation` | `0.8110` | 33,140,000.00 USD | 33,140,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,620.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8130` | 33,030,000.00 USD | 33,030,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 11,260.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 32,960,000.00 USD | 32,960,000.00 USD | 135,770.00 USD | 50,280.00 USD | 124,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 8,160.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8165` | 362.12 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8170` | 32,650,000.00 USD | 32,650,000.00 USD | 91,050.00 USD | 23,590.00 USD | 78,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 104,090.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8185` | 773.65 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 32,460,000.00 USD | 32,460,000.00 USD | 195,400.00 USD | 52,010.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 643.31 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 32,160,000.00 USD | 32,160,000.00 USD | 138,580.00 USD | 47,520.00 USD | 119,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 10,310.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8225` | 466.85 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 31,860,000.00 USD | 31,860,000.00 USD | 37,880.00 USD | 24,290.00 USD | 64,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 659.29 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8245` | 3,510.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 31,730,000.00 USD | 31,730,000.00 USD | 187,510.00 USD | 27,530.00 USD | 126,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 31,390,000.00 USD | 31,390,000.00 USD | 144,410.00 USD | 51,050.00 USD | 63,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 27,960.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 118,200.00 USD | 990,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8290` | 31,130,000.00 USD | 31,130,000.00 USD | 89,470.00 USD | 39,850.00 USD | 82,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 32,530.00 USD | 871,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8305` | 1,670.00 USD | 839,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8310` | 30,920,000.00 USD | 30,920,000.00 USD | 34,030.00 USD | 30,800.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8325` | 18,980.00 USD | 837,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8330` | 30,830,000.00 USD | 30,830,000.00 USD | 150,740.00 USD | 85,780.00 USD | 198,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8335` | 686.97 USD | 818,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8350` | 30,390,000.00 USD | 30,390,000.00 USD | 74,030.00 USD | 14,320.00 USD | 83,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 17,770.00 USD | 818,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 30,220,000.00 USD | 30,220,000.00 USD | 146,890.00 USD | 48,060.00 USD | 102,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 137.85 USD | 800,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8385` | 79,450.00 USD | 800,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8390` | 29,920,000.00 USD | 29,920,000.00 USD | 24,790.00 USD | 51,510.00 USD | 77,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 27,150.00 USD | 720,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8405` | 744.51 USD | 693,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8410` | 29,770,000.00 USD | 29,770,000.00 USD | 55,190.00 USD | 40,110.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 3,890.00 USD | 692,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8425` | 13,400.00 USD | 688,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8430` | 29,650,000.00 USD | 29,650,000.00 USD | 81,850.00 USD | 49,990.00 USD | 30,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 1,340.00 USD | 675,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8445` | 893.23 USD | 674,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8450` | 29,490,000.00 USD | 29,490,000.00 USD | 43,800.00 USD | 55,690.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 8,710.00 USD | 673,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 13,370,000.00 USD | 13,370,000.00 USD | 28,740.00 USD | 30,760.00 USD | 46,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 13,750.00 USD | 664,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8470` | 29,340,000.00 USD | 29,340,000.00 USD | 23,930.00 USD | 4,350.00 USD | 32,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 29,810.00 USD | 650,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 13,260,000.00 USD | 13,260,000.00 USD | 24,470.00 USD | 17,830.00 USD | 27,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,890.00 USD | 621,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8490` | 29,280,000.00 USD | 29,280,000.00 USD | 45,210.00 USD | 16,670.00 USD | 46,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 804.99 USD | 619,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 13,190,000.00 USD | 13,190,000.00 USD | 53,880.00 USD | 7,390.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 29,170,000.00 USD | 29,170,000.00 USD | 95,990.00 USD | 42,650.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 618,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 13,120,000.00 USD | 13,120,000.00 USD | 30,310.00 USD | 27,790.00 USD | 16,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 4,220.00 USD | 617,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8530` | 28,990,000.00 USD | 28,990,000.00 USD | 30,570.00 USD | 50,890.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 11,410.00 USD | 612,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 13,040,000.00 USD | 13,040,000.00 USD | 20,080.00 USD | 11,230.00 USD | 42,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8545` | 2,030.00 USD | 601,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8550` | 28,880,000.00 USD | 28,880,000.00 USD | 78,320.00 USD | 26,490.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8555` | 139.53 USD | 599,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 12,970,000.00 USD | 12,970,000.00 USD | 27,930.00 USD | 22,280.00 USD | 25,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 36,350.00 USD | 599,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8570` | 28,770,000.00 USD | 28,770,000.00 USD | 99,680.00 USD | 45,070.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 12,890,000.00 USD | 12,890,000.00 USD | 56,290.00 USD | 13,830.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 14,660.00 USD | 562,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8590` | 28,620,000.00 USD | 28,620,000.00 USD | 51,400.00 USD | 22,020.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 7,610.00 USD | 548,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 12,810,000.00 USD | 12,810,000.00 USD | 17,410.00 USD | 6,920.00 USD | 14,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 19,020.00 USD | 540,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8610` | 28,530,000.00 USD | 28,530,000.00 USD | 36,870.00 USD | 71,110.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8615` | 2,080.00 USD | 521,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 12,770,000.00 USD | 12,770,000.00 USD | 6,110.00 USD | 5,870.00 USD | 673.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 9,140.00 USD | 519,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 28,390,000.00 USD | 28,390,000.00 USD | 30,710.00 USD | 13,800.00 USD | 48,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 4,710.00 USD | 510,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 12,760,000.00 USD | 12,760,000.00 USD | 53,230.00 USD | 24,840.00 USD | 60,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 2,580.00 USD | 505,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 28,300,000.00 USD | 28,300,000.00 USD | 235,900.00 USD | 43,890.00 USD | 100,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8655` | 2,210.00 USD | 503,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 12,620,000.00 USD | 12,620,000.00 USD | 139,410.00 USD | 1,740.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,040.00 USD | 500,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 27,910,000.00 USD | 27,910,000.00 USD | 159,120.00 USD | 71,510.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8675` | 11,820.00 USD | 499,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 12,460,000.00 USD | 12,460,000.00 USD | 103,830.00 USD | 60,300.00 USD | 33,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8685` | 289.04 USD | 488,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8690` | 27,630,000.00 USD | 27,630,000.00 USD | 182,190.00 USD | 79,290.00 USD | 193,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 5,030.00 USD | 487,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 12,270,000.00 USD | 12,270,000.00 USD | 110,320.00 USD | 89,890.00 USD | 226,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 14,970.00 USD | 482,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8710` | 27,170,000.00 USD | 27,170,000.00 USD | 604,760.00 USD | 167,740.00 USD | 362,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 2,870.00 USD | 467,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 11,840,000.00 USD | 11,840,000.00 USD | 211,520.00 USD | 63,380.00 USD | 201,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8725` | 29,520.00 USD | 464,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8730` | 26,030,000.00 USD | 26,030,000.00 USD | 333,320.00 USD | 199,690.00 USD | 215,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8735` | 13,270.00 USD | 435,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8740` | 11,360,000.00 USD | 11,360,000.00 USD | 43,750.00 USD | 20,450.00 USD | 21,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8745` | 15,980.00 USD | 422,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8750` | 25,290,000.00 USD | 25,290,000.00 USD | 643,630.00 USD | 230,460.00 USD | 324,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8755` | 1,420.00 USD | 406,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8760` | 11,280,000.00 USD | 11,280,000.00 USD | 77,040.00 USD | 73,640.00 USD | 139,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 33,510.00 USD | 404,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 24,090,000.00 USD | 24,090,000.00 USD | 399,330.00 USD | 194,000.00 USD | 420,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8775` | 16,030.00 USD | 371,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 10,990,000.00 USD | 10,990,000.00 USD | 64,740.00 USD | 48,440.00 USD | 31,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8785` | 56,160.00 USD | 355,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8790` | 23,070,000.00 USD | 23,070,000.00 USD | 312,210.00 USD | 124,520.00 USD | 220,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 172,470.00 USD | 299,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 10,840,000.00 USD | 10,840,000.00 USD | 14,150.00 USD | 11,490.00 USD | 41,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8805` | 1,530.00 USD | 126,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8810` | 22,420,000.00 USD | 22,420,000.00 USD | 641,660.00 USD | 159,780.00 USD | 487,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8815` | 8,730.00 USD | 125,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8820` | 10,770,000.00 USD | 10,770,000.00 USD | 110,430.00 USD | 63,180.00 USD | 145,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8825` | 5,300.00 USD | 116,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8830` | 21,130,000.00 USD | 21,130,000.00 USD | 783,040.00 USD | 270,900.00 USD | 529,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8835` | 7,220.00 USD | 111,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8840` | 10,460,000.00 USD | 10,460,000.00 USD | 303,250.00 USD | 69,500.00 USD | 158,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 3,550.00 USD | 103,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8850` | 19,540,000.00 USD | 19,540,000.00 USD | 519,370.00 USD | 263,660.00 USD | 258,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8855` | 2,660.00 USD | 100,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8860` | 9,920,000.00 USD | 9,920,000.00 USD | 285,170.00 USD | 128,260.00 USD | 88,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8865` | 28,370.00 USD | 97,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8870` | 18,500,000.00 USD | 18,500,000.00 USD | 649,180.00 USD | 279,830.00 USD | 511,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8875` | 12,780.00 USD | 69,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8880` | 9,420,000.00 USD | 9,420,000.00 USD | 332,020.00 USD | 224,400.00 USD | 540,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8885` | 697.38 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8890` | 17,060,000.00 USD | 17,060,000.00 USD | 1,550,000.00 USD | 530,540.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8895` | 3,530.00 USD | 55,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8900` | 8,330,000.00 USD | 8,330,000.00 USD | 524,630.00 USD | 174,460.00 USD | 573,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8905` | 139.90 USD | 52,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8910` | 13,820,000.00 USD | 13,820,000.00 USD | 818,970.00 USD | 471,140.00 USD | 681,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8915` | 1,100.00 USD | 52,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8920` | 7,050,000.00 USD | 7,050,000.00 USD | 235,610.00 USD | 49,510.00 USD | 115,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 1,040.00 USD | 50,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8930` | 11,850,000.00 USD | 11,850,000.00 USD | 1,790,000.00 USD | 646,070.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8935` | 2,470.00 USD | 49,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8940` | 6,650,000.00 USD | 6,650,000.00 USD | 167,880.00 USD | 127,050.00 USD | 266,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8945` | 5,380.00 USD | 47,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8950` | 8,370,000.00 USD | 8,370,000.00 USD | 771,020.00 USD | 443,450.00 USD | 798,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 6,090,000.00 USD | 6,090,000.00 USD | 130,690.00 USD | 139,190.00 USD | 168,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8965` | 29,550.00 USD | 42,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8970` | 6,360,000.00 USD | 6,360,000.00 USD | 673,010.00 USD | 276,920.00 USD | 492,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8975` | 3,540.00 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8980` | 5,650,000.00 USD | 5,650,000.00 USD | 114,240.00 USD | 50,830.00 USD | 76,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 320.05 USD | 8,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8990` | 4,920,000.00 USD | 4,920,000.00 USD | 322,820.00 USD | 147,390.00 USD | 897.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 143.92 USD | 8,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 5,410,000.00 USD | 5,410,000.00 USD | 53,800.00 USD | 24,210.00 USD | 44,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9005` | 2,600.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.9010` | 4,440,000.00 USD | 4,440,000.00 USD | 130,380.00 USD | 15,640.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 5,290,000.00 USD | 5,290,000.00 USD | 49,680.00 USD | 79,010.00 USD | 192,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 4,290,000.00 USD | 4,290,000.00 USD | 5,880.00 USD | 50,720.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 4,970,000.00 USD | 4,970,000.00 USD | 91,760.00 USD | 76,800.00 USD | 73,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 4,120,000.00 USD | 4,120,000.00 USD | 70,190.00 USD | 0.00 USD | 46,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 300.72 USD | 8,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 4,730,000.00 USD | 4,730,000.00 USD | 195,270.00 USD | 6,440.00 USD | 58,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 4,000,000.00 USD | 4,000,000.00 USD | 341,080.00 USD | 19,890.00 USD | 127,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9075` | 8,220.00 USD | 8,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9080` | 4,470,000.00 USD | 4,470,000.00 USD | 241,380.00 USD | 116,800.00 USD | 207,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 3,510,000.00 USD | 3,510,000.00 USD | 53,970.00 USD | 0.00 USD | 128,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 3,900,000.00 USD | 3,900,000.00 USD | 174,550.00 USD | 32,520.00 USD | 153,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 3,330,000.00 USD | 3,330,000.00 USD | 212,760.00 USD | 106,160.00 USD | 35,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 3,540,000.00 USD | 3,540,000.00 USD | 211,640.00 USD | 33,420.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 2,970,000.00 USD | 2,970,000.00 USD | 80,230.00 USD | 95,530.00 USD | 105,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 3,120,000.00 USD | 3,120,000.00 USD | 134,740.00 USD | 70,610.00 USD | 76,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 2,690,000.00 USD | 2,690,000.00 USD | 111,690.00 USD | 26,360.00 USD | 38,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 2,840,000.00 USD | 2,840,000.00 USD | 19,210.00 USD | 13,400.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 2,520,000.00 USD | 2,520,000.00 USD | 123,530.00 USD | 0.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 2,800,000.00 USD | 2,800,000.00 USD | 154,870.00 USD | 9,020.00 USD | 46,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 2,360,000.00 USD | 2,360,000.00 USD | 257,890.00 USD | 23,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 2,070,000.00 USD | 2,070,000.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 39,420.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 64,540.00 USD | 286,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 2,470,000.00 USD | 2,470,000.00 USD | 90,500.00 USD | 40,590.00 USD | 82,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 41,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 2,260,000.00 USD | 2,260,000.00 USD | 111,230.00 USD | 28,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 1,470,000.00 USD | 1,470,000.00 USD | 209,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 2,120,000.00 USD | 2,120,000.00 USD | 31,930.00 USD | 80,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 78,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 2,010,000.00 USD | 2,010,000.00 USD | 82,700.00 USD | 110,920.00 USD | 166,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9310` | 1,180,000.00 USD | 1,180,000.00 USD | 177,720.00 USD | 29,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 1,650,000.00 USD | 1,650,000.00 USD | 189,840.00 USD | 54,470.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 1,340,000.00 USD | 1,340,000.00 USD | 198,250.00 USD | 74,630.00 USD | 51,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9350` | 975,070.00 USD | 975,070.00 USD | 50,160.00 USD | 52,710.00 USD | 76,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 1,010,000.00 USD | 1,010,000.00 USD | 81,170.00 USD | 39,480.00 USD | 113,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9370` | 796,150.00 USD | 796,150.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9380` | 777,990.00 USD | 777,990.00 USD | 246,090.00 USD | 118,850.00 USD | 293,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9390` | 502,440.00 USD | 502,440.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 119,550.00 USD | 119,550.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9410` | 123,000.00 USD | 123,000.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 62,100.00 USD | 62,100.00 USD | 0.00 USD | 62,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 110,210.00 USD | 110,210.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 396,730.00 USD | 396,730.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 380,390.00 USD | 380,390.00 USD | 0.00 USD | 28,980.00 USD | 241,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 607,360.00 USD | 607,360.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 643,170.00 USD | 643,170.00 USD | 0.00 USD | 0.00 USD | 35,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 381,820.00 USD | 381,820.00 USD | 1,330.00 USD | 0.00 USD | 107.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 62,510.00 USD | 639,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 435,880.00 USD | 435,880.00 USD | 0.00 USD | 0.00 USD | 54,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 473,250.00 USD | 473,250.00 USD | 7,240.00 USD | 30,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 1,420,000.00 USD | 1,420,000.00 USD | 71,910.00 USD | 1,290.00 USD | 288.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 506,920.00 USD | 506,920.00 USD | 0.00 USD | 33,360.00 USD | 303.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 1,890,000.00 USD | 1,890,000.00 USD | 463,830.00 USD | 2,240.00 USD | 511.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 550,740.00 USD | 550,740.00 USD | 689.00 USD | 43,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 2,450,000.00 USD | 2,450,000.00 USD | 562,050.00 USD | 1,040.00 USD | 289.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 737,500.00 USD | 737,500.00 USD | 77,250.00 USD | 65,470.00 USD | 44,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 3,700,000.00 USD | 3,700,000.00 USD | 647,060.00 USD | 176,650.00 USD | 421,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 1,470,000.00 USD | 1,470,000.00 USD | 338,260.00 USD | 118,080.00 USD | 277,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 5,170,000.00 USD | 5,170,000.00 USD | 552,290.00 USD | 301,610.00 USD | 615,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 2,210,000.00 USD | 2,210,000.00 USD | 332,940.00 USD | 127,440.00 USD | 278,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 6,740,000.00 USD | 6,740,000.00 USD | 857,470.00 USD | 301,210.00 USD | 412,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 2,750,000.00 USD | 2,750,000.00 USD | 273,420.00 USD | 130,360.00 USD | 133,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 8,850,000.00 USD | 8,850,000.00 USD | 916,920.00 USD | 487,590.00 USD | 705,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9680` | 3,520,000.00 USD | 3,520,000.00 USD | 303,010.00 USD | 116,010.00 USD | 350,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 10,180,000.00 USD | 10,180,000.00 USD | 596,350.00 USD | 343,680.00 USD | 389,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 4,090,000.00 USD | 4,090,000.00 USD | 246,830.00 USD | 142,190.00 USD | 184,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 70,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9710` | 11,270,000.00 USD | 11,270,000.00 USD | 645,500.00 USD | 305,860.00 USD | 144,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 4,620,000.00 USD | 4,620,000.00 USD | 320,980.00 USD | 108,180.00 USD | 99,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 12,040,000.00 USD | 12,040,000.00 USD | 456,990.00 USD | 160,420.00 USD | 146,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 4,880,000.00 USD | 4,880,000.00 USD | 169,060.00 USD | 34,110.00 USD | 53,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 12,720,000.00 USD | 12,720,000.00 USD | 201,510.00 USD | 293,590.00 USD | 193,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 5,050,000.00 USD | 5,050,000.00 USD | 40,320.00 USD | 41,480.00 USD | 88,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9765` | 214.44 USD | 71,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9770` | 13,760,000.00 USD | 13,760,000.00 USD | 329,170.00 USD | 211,000.00 USD | 499,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 5,400,000.00 USD | 5,400,000.00 USD | 110,140.00 USD | 54,830.00 USD | 189,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 14,420,000.00 USD | 14,420,000.00 USD | 409,890.00 USD | 83,100.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 5,620,000.00 USD | 5,620,000.00 USD | 66,270.00 USD | 66,440.00 USD | 90,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 15,580.00 USD | 86,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 14,880,000.00 USD | 14,880,000.00 USD | 212,850.00 USD | 83,040.00 USD | 169,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 5,870,000.00 USD | 5,870,000.00 USD | 165,210.00 USD | 28,940.00 USD | 53,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 15,440,000.00 USD | 15,440,000.00 USD | 260,850.00 USD | 99,420.00 USD | 199,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 6,040,000.00 USD | 6,040,000.00 USD | 74,270.00 USD | 67,350.00 USD | 22,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9845` | 10,440.00 USD | 97,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9850` | 15,850,000.00 USD | 15,850,000.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 6,370,000.00 USD | 6,370,000.00 USD | 131,110.00 USD | 61,330.00 USD | 136,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 16,350,000.00 USD | 16,350,000.00 USD | 248,980.00 USD | 191,820.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 54,920.00 USD | 151,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 6,560,000.00 USD | 6,560,000.00 USD | 85,900.00 USD | 34,510.00 USD | 70,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 13,550.00 USD | 165,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9890` | 16,640,000.00 USD | 16,640,000.00 USD | 194,850.00 USD | 78,280.00 USD | 18,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9895` | 5,760.00 USD | 171,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9900` | 6,830,000.00 USD | 6,830,000.00 USD | 146,250.00 USD | 50,130.00 USD | 77,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 20,050.00 USD | 191,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9910` | 17,010,000.00 USD | 17,010,000.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 7,040,000.00 USD | 7,040,000.00 USD | 143,390.00 USD | 45,570.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,290.00 USD | 193,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 17,380,000.00 USD | 17,380,000.00 USD | 228,340.00 USD | 63,950.00 USD | 73,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 7,200,000.00 USD | 7,200,000.00 USD | 60,490.00 USD | 36,310.00 USD | 61,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9945` | 6,430.00 USD | 200,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9950` | 17,690,000.00 USD | 17,690,000.00 USD | 48,120.00 USD | 137,230.00 USD | 130,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 7,240,000.00 USD | 7,240,000.00 USD | 6,800.00 USD | 10,960.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9965` | 5,440.00 USD | 205,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9970` | 18,340,000.00 USD | 18,340,000.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 7,550,000.00 USD | 7,550,000.00 USD | 139,760.00 USD | 32,100.00 USD | 142,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 18,620,000.00 USD | 18,620,000.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 7,600,000.00 USD | 7,600,000.00 USD | 19,510.00 USD | 17,530.00 USD | 6,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 19,070,000.00 USD | 19,070,000.00 USD | 202,970.00 USD | 57,170.00 USD | 185,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 7,650,000.00 USD | 7,650,000.00 USD | 12,840.00 USD | 18,430.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 19,650,000.00 USD | 19,650,000.00 USD | 316,600.00 USD | 52,200.00 USD | 216,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 7,700,000.00 USD | 7,700,000.00 USD | 17,620.00 USD | 13,050.00 USD | 22,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 449.11 USD | 205,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 19,850,000.00 USD | 19,850,000.00 USD | 96,930.00 USD | 29,470.00 USD | 65,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 7,730,000.00 USD | 7,730,000.00 USD | 9,900.00 USD | 14,020.00 USD | 9,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 20,360,000.00 USD | 20,360,000.00 USD | 283,350.00 USD | 15,900.00 USD | 212,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 7,770,000.00 USD | 7,770,000.00 USD | 19,520.00 USD | 9,720.00 USD | 12,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 20,960,000.00 USD | 20,960,000.00 USD | 247,480.00 USD | 105,290.00 USD | 247,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 7,800,000.00 USD | 7,800,000.00 USD | 13,140.00 USD | 5,570.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 21,910,000.00 USD | 21,910,000.00 USD | 457,740.00 USD | 174,650.00 USD | 319,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 7,880,000.00 USD | 7,880,000.00 USD | 21,660.00 USD | 15,860.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 117,860.00 USD | 323,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 22,900,000.00 USD | 22,900,000.00 USD | 342,220.00 USD | 305,010.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 7,930,000.00 USD | 7,930,000.00 USD | 16,320.00 USD | 11,680.00 USD | 27,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 23,440,000.00 USD | 23,440,000.00 USD | 325,510.00 USD | 91,280.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 323,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 7,990,000.00 USD | 7,990,000.00 USD | 23,240.00 USD | 15,330.00 USD | 19,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 24,280,000.00 USD | 24,280,000.00 USD | 383,690.00 USD | 97,830.00 USD | 360,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 8,020,000.00 USD | 8,020,000.00 USD | 26,650.00 USD | 4,040.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 25,150,000.00 USD | 25,150,000.00 USD | 303,920.00 USD | 89,280.00 USD | 469,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 8,140,000.00 USD | 8,140,000.00 USD | 36,470.00 USD | 16,330.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 25,640,000.00 USD | 25,640,000.00 USD | 167,390.00 USD | 64,370.00 USD | 260,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 8,230,000.00 USD | 8,230,000.00 USD | 55,940.00 USD | 4,130.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 26,000,000.00 USD | 26,000,000.00 USD | 185,100.00 USD | 50,190.00 USD | 123,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 8,280,000.00 USD | 8,280,000.00 USD | 29,960.00 USD | 7,480.00 USD | 21,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 26,260,000.00 USD | 26,260,000.00 USD | 112,970.00 USD | 54,210.00 USD | 94,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 8,330,000.00 USD | 8,330,000.00 USD | 16,450.00 USD | 12,750.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 26,510,000.00 USD | 26,510,000.00 USD | 106,360.00 USD | 35,230.00 USD | 110,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 8,340,000.00 USD | 8,340,000.00 USD | 6,020.00 USD | 0.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 8,840.00 USD | 332,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.03` | 26,720,000.00 USD | 26,720,000.00 USD | 87,950.00 USD | 57,010.00 USD | 67,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 8,370,000.00 USD | 8,370,000.00 USD | 4,130.00 USD | 10,190.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 27,160,000.00 USD | 27,160,000.00 USD | 198,340.00 USD | 79,470.00 USD | 157,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 8,400,000.00 USD | 8,400,000.00 USD | 21,900.00 USD | 11,130.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 27,610,000.00 USD | 27,610,000.00 USD | 136,400.00 USD | 149,600.00 USD | 163,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 8,490,000.00 USD | 8,490,000.00 USD | 16,600.00 USD | 19,650.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 27,800,000.00 USD | 27,800,000.00 USD | 113,490.00 USD | 13,570.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 8,550,000.00 USD | 8,550,000.00 USD | 19,040.00 USD | 16,530.00 USD | 27,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 28,200,000.00 USD | 28,200,000.00 USD | 176,930.00 USD | 41,660.00 USD | 181,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 8,620,000.00 USD | 8,620,000.00 USD | 51,250.00 USD | 7,020.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 28,510,000.00 USD | 28,510,000.00 USD | 114,060.00 USD | 21,690.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 10,400.00 USD | 343,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 8,650,000.00 USD | 8,650,000.00 USD | 8,210.00 USD | 7,840.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 343,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 28,740,000.00 USD | 28,740,000.00 USD | 105,050.00 USD | 55,100.00 USD | 72,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 8,690,000.00 USD | 8,690,000.00 USD | 21,580.00 USD | 18,300.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 28,840,000.00 USD | 28,840,000.00 USD | 20,680.00 USD | 49,420.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 8,770,000.00 USD | 8,770,000.00 USD | 19,660.00 USD | 8,720.00 USD | 41,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 28,930,000.00 USD | 28,930,000.00 USD | 69,360.00 USD | 17,730.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 8,830,000.00 USD | 8,830,000.00 USD | 25,330.00 USD | 17,080.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 29,040,000.00 USD | 29,040,000.00 USD | 79,950.00 USD | 31,290.00 USD | 294.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 8,910,000.00 USD | 8,910,000.00 USD | 53,350.00 USD | 10,090.00 USD | 14,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 29,110,000.00 USD | 29,110,000.00 USD | 38,030.00 USD | 13,720.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 8,920,000.00 USD | 8,920,000.00 USD | 12,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 343,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 29,130,000.00 USD | 29,130,000.00 USD | 23,320.00 USD | 0.00 USD | 538.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 346,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 142.30 USD | 14,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,330.00 USD | 347,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 29,210,000.00 USD | 29,210,000.00 USD | 8,370.00 USD | 47,690.00 USD | 28,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 348,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.05` | 8,940,000.00 USD | 8,940,000.00 USD | 303.15 USD | 202.65 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 217.44 USD | 348,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 29,270,000.00 USD | 29,270,000.00 USD | 3,770.00 USD | 5,360.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.06` | 8,960,000.00 USD | 8,960,000.00 USD | 11,980.00 USD | 4,220.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 29,280,000.00 USD | 29,280,000.00 USD | 6,580.00 USD | 3,950.00 USD | 197.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 29,280,000.00 USD | 29,280,000.00 USD | 1,110.00 USD | 194.87 USD | 59.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 29,320,000.00 USD | 29,320,000.00 USD | 17,530.00 USD | 3,870.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 29,330,000.00 USD | 29,330,000.00 USD | 10,210.00 USD | 0.00 USD | 388.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 29,330,000.00 USD | 29,330,000.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.1865` | 5,390,000.00 USD | 0.00 USD | 1,890.00 USD | `-80.31%` | `10,152.10` |
| `Live` | `Long` | `0.1895` | 5,390,000.00 USD | 0.00 USD | 4,890.00 USD | `-79.99%` | `25,791.20` |
| `Live` | `Long` | `0.1995` | 5,380,000.00 USD | 0.00 USD | 256.00 USD | `-78.94%` | `1,283.20` |
| `Live` | `Long` | `0.2005` | 5,380,000.00 USD | 0.00 USD | 130.20 USD | `-78.83%` | `649.40` |
| `Live` | `Long` | `0.2075` | 5,380,000.00 USD | 0.00 USD | 218.31 USD | `-78.09%` | `1,052.10` |
| `Live` | `Long` | `0.2295` | 5,380,000.00 USD | 0.00 USD | 17,830.00 USD | `-75.77%` | `77,706.40` |
| `Live` | `Long` | `0.2355` | 5,360,000.00 USD | 0.00 USD | 789.66 USD | `-75.14%` | `3,353.10` |
| `Live` | `Long` | `0.2365` | 5,360,000.00 USD | 0.00 USD | 307.45 USD | `-75.03%` | `1,300.00` |
| `Live` | `Long` | `0.2385` | 5,360,000.00 USD | 0.00 USD | 156.36 USD | `-74.82%` | `655.60` |
| `Live` | `Long` | `0.2525` | 5,360,000.00 USD | 0.00 USD | 2,250.00 USD | `-73.34%` | `8,897.00` |
| `Live` | `Long` | `0.2595` | 5,360,000.00 USD | 0.00 USD | 220.00 USD | `-72.60%` | `847.80` |
| `Live` | `Long` | `0.2655` | 5,360,000.00 USD | 0.00 USD | 164.21 USD | `-71.97%` | `618.50` |
| `Live` | `Long` | `0.2685` | 5,360,000.00 USD | 0.00 USD | 106.16 USD | `-71.65%` | `395.40` |
| `Live` | `Long` | `0.2735` | 5,360,000.00 USD | 0.00 USD | 2,160.00 USD | `-71.12%` | `7,908.00` |
| `Live` | `Long` | `0.2795` | 5,360,000.00 USD | 0.00 USD | 137.09 USD | `-70.49%` | `490.50` |
| `Live` | `Long` | `0.2805` | 5,360,000.00 USD | 0.00 USD | 6,710.00 USD | `-70.38%` | `23,938.30` |
| `Live` | `Long` | `0.2875` | 5,350,000.00 USD | 0.00 USD | 2,880.00 USD | `-69.65%` | `10,000.00` |
| `Live` | `Long` | `0.2885` | 5,350,000.00 USD | 0.00 USD | 29,070.00 USD | `-69.54%` | `100,768.40` |
| `Live` | `Long` | `0.2945` | 5,320,000.00 USD | 0.00 USD | 687.92 USD | `-68.91%` | `2,335.90` |
| `Live` | `Long` | `0.2955` | 5,320,000.00 USD | 0.00 USD | 28,700.00 USD | `-68.80%` | `97,131.80` |
| `Live` | `Long` | `0.2975` | 5,290,000.00 USD | 0.00 USD | 4,330.00 USD | `-68.59%` | `14,561.30` |
| `Live` | `Long` | `0.3115` | 5,290,000.00 USD | 0.00 USD | 270.38 USD | `-67.11%` | `868.00` |
| `Live` | `Long` | `0.3175` | 5,290,000.00 USD | 0.00 USD | 354.04 USD | `-66.48%` | `1,115.10` |
| `Live` | `Long` | `0.3345` | 5,290,000.00 USD | 0.00 USD | 589.39 USD | `-64.68%` | `1,762.00` |
| `Live` | `Long` | `0.3355` | 5,280,000.00 USD | 0.00 USD | 303.66 USD | `-64.58%` | `905.10` |
| `Live` | `Long` | `0.3505` | 5,280,000.00 USD | 0.00 USD | 1,020.00 USD | `-62.99%` | `2,908.00` |
| `Live` | `Long` | `0.3525` | 5,280,000.00 USD | 0.00 USD | 61,690.00 USD | `-62.78%` | `175,000.00` |
| `Live` | `Long` | `0.3585` | 5,220,000.00 USD | 0.00 USD | 595.72 USD | `-62.15%` | `1,661.70` |
| `Live` | `Long` | `0.3665` | 5,220,000.00 USD | 0.00 USD | 274.88 USD | `-61.30%` | `750.00` |
| `Live` | `Long` | `0.3695` | 5,220,000.00 USD | 0.00 USD | 230.94 USD | `-60.99%` | `625.00` |
| `Live` | `Long` | `0.3745` | 5,220,000.00 USD | 0.00 USD | 173.69 USD | `-60.46%` | `463.80` |
| `Live` | `Long` | `0.3755` | 5,220,000.00 USD | 0.00 USD | 6,380.00 USD | `-60.35%` | `17,000.00` |
| `Live` | `Long` | `0.3795` | 5,210,000.00 USD | 0.00 USD | 26,840.00 USD | `-59.93%` | `70,732.60` |
| `Live` | `Long` | `0.3835` | 5,190,000.00 USD | 0.00 USD | 5,200.00 USD | `-59.51%` | `13,552.00` |
| `Live` | `Long` | `0.3845` | 5,180,000.00 USD | 0.00 USD | 1,750.00 USD | `-59.40%` | `4,562.20` |
| `Live` | `Long` | `0.3875` | 5,180,000.00 USD | 0.00 USD | 2,330.00 USD | `-59.09%` | `6,000.00` |
| `Live` | `Long` | `0.3895` | 5,180,000.00 USD | 0.00 USD | 2,980.00 USD | `-58.88%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 5,170,000.00 USD | 0.00 USD | 5,030.00 USD | `-58.56%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 5,170,000.00 USD | 0.00 USD | 28,820.00 USD | `-58.35%` | `73,043.40` |
| `Live` | `Long` | `0.3955` | 5,140,000.00 USD | 0.00 USD | 276.85 USD | `-58.24%` | `700.00` |
| `Live` | `Long` | `0.3965` | 5,140,000.00 USD | 0.00 USD | 1,020.00 USD | `-58.14%` | `2,584.80` |
| `Live` | `Long` | `0.4005` | 5,140,000.00 USD | 0.00 USD | 3,950.00 USD | `-57.72%` | `9,865.70` |
| `Live` | `Long` | `0.4015` | 5,140,000.00 USD | 0.00 USD | 97,110.00 USD | `-57.61%` | `241,876.40` |
| `Live` | `Long` | `0.4035` | 5,040,000.00 USD | 0.00 USD | 935.03 USD | `-57.40%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 5,040,000.00 USD | 0.00 USD | 5,520.00 USD | `-57.29%` | `13,640.50` |
| `Live` | `Long` | `0.4145` | 5,030,000.00 USD | 0.00 USD | 458.44 USD | `-56.24%` | `1,106.00` |
| `Live` | `Long` | `0.4235` | 5,030,000.00 USD | 0.00 USD | 467.50 USD | `-55.29%` | `1,103.90` |
| `Live` | `Long` | `0.4365` | 5,030,000.00 USD | 0.00 USD | 43,480.00 USD | `-53.91%` | `99,611.70` |
| `Live` | `Long` | `0.4385` | 4,990,000.00 USD | 0.00 USD | 122.91 USD | `-53.70%` | `280.30` |
| `Live` | `Long` | `0.4415` | 4,990,000.00 USD | 0.00 USD | 5,800.00 USD | `-53.39%` | `13,146.20` |
| `Live` | `Long` | `0.4435` | 4,980,000.00 USD | 0.00 USD | 662.50 USD | `-53.18%` | `1,493.80` |
| `Live` | `Long` | `0.4445` | 4,980,000.00 USD | 0.00 USD | 573.54 USD | `-53.07%` | `1,290.30` |
| `Live` | `Long` | `0.4455` | 4,980,000.00 USD | 0.00 USD | 16,360.00 USD | `-52.96%` | `36,725.40` |
| `Live` | `Long` | `0.4465` | 4,960,000.00 USD | 0.00 USD | 3,980.00 USD | `-52.86%` | `8,924.20` |
| `Live` | `Long` | `0.4535` | 4,960,000.00 USD | 0.00 USD | 702.74 USD | `-52.12%` | `1,549.60` |
| `Live` | `Long` | `0.4565` | 4,960,000.00 USD | 0.00 USD | 249.71 USD | `-51.80%` | `547.00` |
| `Live` | `Long` | `0.4595` | 4,960,000.00 USD | 0.00 USD | 295.78 USD | `-51.49%` | `643.70` |
| `Live` | `Long` | `0.4625` | 4,960,000.00 USD | 0.00 USD | 5,220.00 USD | `-51.17%` | `11,290.30` |
| `Live` | `Long` | `0.4675` | 4,950,000.00 USD | 0.00 USD | 244.78 USD | `-50.64%` | `523.60` |
| `Live` | `Long` | `0.4695` | 4,950,000.00 USD | 0.00 USD | 916.89 USD | `-50.43%` | `1,952.90` |
| `Live` | `Long` | `0.4725` | 4,950,000.00 USD | 0.00 USD | 5,110.00 USD | `-50.11%` | `10,805.30` |
| `Live` | `Long` | `0.4785` | 4,950,000.00 USD | 0.00 USD | 110.10 USD | `-49.48%` | `230.10` |
| `Live` | `Long` | `0.4795` | 4,950,000.00 USD | 0.00 USD | 241.72 USD | `-49.37%` | `504.10` |
| `Live` | `Long` | `0.4825` | 4,950,000.00 USD | 0.00 USD | 173.65 USD | `-49.06%` | `359.90` |
| `Live` | `Long` | `0.4865` | 4,950,000.00 USD | 0.00 USD | 201.07 USD | `-48.64%` | `413.30` |
| `Live` | `Long` | `0.4885` | 4,950,000.00 USD | 0.00 USD | 1,050.00 USD | `-48.42%` | `2,151.80` |
| `Live` | `Long` | `0.4895` | 4,950,000.00 USD | 0.00 USD | 105.34 USD | `-48.32%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,950,000.00 USD | 0.00 USD | 2,380.00 USD | `-48.11%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 4,940,000.00 USD | 0.00 USD | 106.32 USD | `-47.79%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,940,000.00 USD | 0.00 USD | 3,120.00 USD | `-47.69%` | `6,305.00` |
| `Live` | `Long` | `0.4965` | 4,940,000.00 USD | 0.00 USD | 139.02 USD | `-47.58%` | `280.00` |
| `Live` | `Long` | `0.4975` | 4,940,000.00 USD | 0.00 USD | 3,230.00 USD | `-47.47%` | `6,500.00` |
| `Live` | `Long` | `0.4985` | 4,940,000.00 USD | 0.00 USD | 2,460.00 USD | `-47.37%` | `4,934.80` |
| `Live` | `Long` | `0.5015` | 4,930,000.00 USD | 0.00 USD | 1,440.00 USD | `-47.05%` | `2,874.80` |
| `Live` | `Long` | `0.5045` | 4,930,000.00 USD | 0.00 USD | 837.57 USD | `-46.73%` | `1,660.20` |
| `Live` | `Long` | `0.5055` | 4,930,000.00 USD | 0.00 USD | 211.25 USD | `-46.63%` | `417.90` |
| `Live` | `Long` | `0.5065` | 4,930,000.00 USD | 0.00 USD | 258.21 USD | `-46.52%` | `509.80` |
| `Live` | `Long` | `0.5085` | 4,930,000.00 USD | 0.00 USD | 2,030.00 USD | `-46.31%` | `4,000.00` |
| `Live` | `Long` | `0.5095` | 4,930,000.00 USD | 0.00 USD | 195.75 USD | `-46.21%` | `384.20` |
| `Live` | `Long` | `0.5125` | 4,930,000.00 USD | 0.00 USD | 1,620.00 USD | `-45.89%` | `3,166.20` |
| `Live` | `Long` | `0.5155` | 4,930,000.00 USD | 0.00 USD | 1,240.00 USD | `-45.57%` | `2,409.50` |
| `Live` | `Long` | `0.5165` | 4,930,000.00 USD | 0.00 USD | 619.80 USD | `-45.47%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,930,000.00 USD | 0.00 USD | 213.68 USD | `-45.36%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,930,000.00 USD | 0.00 USD | 121.74 USD | `-45.26%` | `234.80` |
| `Live` | `Long` | `0.5205` | 4,930,000.00 USD | 0.00 USD | 422.33 USD | `-45.05%` | `811.40` |
| `Live` | `Long` | `0.5225` | 4,920,000.00 USD | 0.00 USD | 244.90 USD | `-44.83%` | `468.70` |
| `Live` | `Long` | `0.5245` | 4,920,000.00 USD | 0.00 USD | 5,280.00 USD | `-44.62%` | `10,075.20` |
| `Live` | `Long` | `0.5265` | 4,920,000.00 USD | 0.00 USD | 347.70 USD | `-44.41%` | `660.40` |
| `Live` | `Long` | `0.5275` | 4,920,000.00 USD | 0.00 USD | 122,910.00 USD | `-44.31%` | `233,000.00` |
| `Live` | `Long` | `0.5285` | 4,800,000.00 USD | 0.00 USD | 9,680.00 USD | `-44.20%` | `18,319.90` |
| `Live` | `Long` | `0.5295` | 4,790,000.00 USD | 0.00 USD | 264.06 USD | `-44.10%` | `498.70` |
| `Live` | `Long` | `0.5325` | 4,790,000.00 USD | 0.00 USD | 2,680.00 USD | `-43.78%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,780,000.00 USD | 0.00 USD | 417.12 USD | `-43.57%` | `780.40` |
| `Live` | `Long` | `0.5365` | 4,780,000.00 USD | 0.00 USD | 13,140.00 USD | `-43.36%` | `24,486.50` |
| `Live` | `Long` | `0.5375` | 4,770,000.00 USD | 0.00 USD | 185.44 USD | `-43.25%` | `345.00` |
| `Live` | `Long` | `0.5395` | 4,770,000.00 USD | 0.00 USD | 319.98 USD | `-43.04%` | `593.10` |
| `Live` | `Long` | `0.5405` | 4,770,000.00 USD | 0.00 USD | 7,090.00 USD | `-42.93%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,760,000.00 USD | 0.00 USD | 43,580.00 USD | `-42.72%` | `80,328.80` |
| `Live` | `Long` | `0.5435` | 4,720,000.00 USD | 0.00 USD | 1,620.00 USD | `-42.62%` | `2,984.20` |
| `Live` | `Long` | `0.5445` | 4,720,000.00 USD | 0.00 USD | 230.32 USD | `-42.51%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,720,000.00 USD | 0.00 USD | 272.87 USD | `-42.30%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,720,000.00 USD | 0.00 USD | 1,240.00 USD | `-42.20%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,720,000.00 USD | 0.00 USD | 28,790.00 USD | `-41.98%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,690,000.00 USD | 0.00 USD | 248.06 USD | `-41.88%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,690,000.00 USD | 0.00 USD | 9,870.00 USD | `-41.77%` | `17,903.10` |
| `Live` | `Long` | `0.5525` | 4,680,000.00 USD | 0.00 USD | 582.56 USD | `-41.67%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,680,000.00 USD | 0.00 USD | 271.88 USD | `-41.56%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,680,000.00 USD | 0.00 USD | 531.60 USD | `-41.46%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,680,000.00 USD | 0.00 USD | 7,950.00 USD | `-41.35%` | `14,310.10` |
| `Live` | `Long` | `0.5565` | 4,670,000.00 USD | 0.00 USD | 3,830.00 USD | `-41.24%` | `6,888.00` |
| `Live` | `Long` | `0.5585` | 4,660,000.00 USD | 0.00 USD | 8,300.00 USD | `-41.03%` | `14,858.10` |
| `Live` | `Long` | `0.5595` | 4,650,000.00 USD | 0.00 USD | 304.93 USD | `-40.93%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,650,000.00 USD | 0.00 USD | 609.99 USD | `-40.82%` | `1,088.30` |
| `Live` | `Long` | `0.5625` | 4,650,000.00 USD | 0.00 USD | 330.53 USD | `-40.61%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,650,000.00 USD | 0.00 USD | 195.93 USD | `-40.51%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,650,000.00 USD | 0.00 USD | 8,760.00 USD | `-40.29%` | `15,490.90` |
| `Live` | `Long` | `0.5665` | 4,640,000.00 USD | 0.00 USD | 609.95 USD | `-40.19%` | `1,076.70` |
| `Live` | `Long` | `0.5675` | 4,640,000.00 USD | 0.00 USD | 947.90 USD | `-40.08%` | `1,670.30` |
| `Live` | `Long` | `0.5695` | 4,640,000.00 USD | 0.00 USD | 973.22 USD | `-39.87%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,640,000.00 USD | 0.00 USD | 139.23 USD | `-39.56%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,640,000.00 USD | 0.00 USD | 286,930.00 USD | `-39.45%` | `500,318.60` |
| `Live` | `Long` | `0.5745` | 4,360,000.00 USD | 0.00 USD | 144.03 USD | `-39.34%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-39.24%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,350,000.00 USD | 0.00 USD | 1,650.00 USD | `-39.13%` | `2,856.10` |
| `Live` | `Long` | `0.5785` | 4,350,000.00 USD | 0.00 USD | 133,580.00 USD | `-38.92%` | `230,914.70` |
| `Live` | `Long` | `0.5795` | 4,220,000.00 USD | 0.00 USD | 104.60 USD | `-38.82%` | `180.50` |
| `Live` | `Long` | `0.5805` | 4,220,000.00 USD | 0.00 USD | 1,410.00 USD | `-38.71%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,220,000.00 USD | 0.00 USD | 6,470.00 USD | `-38.50%` | `11,099.00` |
| `Live` | `Long` | `0.5855` | 4,210,000.00 USD | 0.00 USD | 2,640.00 USD | `-38.18%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,210,000.00 USD | 0.00 USD | 466.85 USD | `-38.08%` | `796.00` |
| `Live` | `Long` | `0.5875` | 4,210,000.00 USD | 0.00 USD | 969.32 USD | `-37.97%` | `1,649.90` |
| `Live` | `Long` | `0.5885` | 4,210,000.00 USD | 0.00 USD | 311.14 USD | `-37.87%` | `528.70` |
| `Live` | `Long` | `0.5895` | 4,210,000.00 USD | 0.00 USD | 7,370.00 USD | `-37.76%` | `12,500.00` |
| `Live` | `Long` | `0.5925` | 4,200,000.00 USD | 0.00 USD | 994.16 USD | `-37.44%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,200,000.00 USD | 0.00 USD | 132.41 USD | `-37.34%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,200,000.00 USD | 0.00 USD | 8,220.00 USD | `-37.23%` | `13,833.50` |
| `Live` | `Long` | `0.5955` | 4,190,000.00 USD | 0.00 USD | 1,590.00 USD | `-37.13%` | `2,666.60` |
| `Live` | `Long` | `0.5965` | 4,190,000.00 USD | 0.00 USD | 5,540.00 USD | `-37.02%` | `9,295.80` |
| `Live` | `Long` | `0.5995` | 4,180,000.00 USD | 0.00 USD | 151.97 USD | `-36.70%` | `253.50` |
| `Live` | `Long` | `0.6005` | 4,180,000.00 USD | 0.00 USD | 351.11 USD | `-36.60%` | `584.70` |
| `Live` | `Long` | `0.6025` | 4,180,000.00 USD | 0.00 USD | 432.35 USD | `-36.39%` | `717.60` |
| `Live` | `Long` | `0.6075` | 4,180,000.00 USD | 0.00 USD | 851.05 USD | `-35.86%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,180,000.00 USD | 0.00 USD | 1,110.00 USD | `-35.75%` | `1,827.00` |
| `Live` | `Long` | `0.6115` | 4,180,000.00 USD | 0.00 USD | 6,780.00 USD | `-35.44%` | `11,093.80` |
| `Live` | `Long` | `0.6125` | 4,170,000.00 USD | 0.00 USD | 213.64 USD | `-35.33%` | `348.80` |
| `Live` | `Long` | `0.6135` | 4,170,000.00 USD | 0.00 USD | 245.40 USD | `-35.23%` | `400.00` |
| `Live` | `Long` | `0.6155` | 4,170,000.00 USD | 0.00 USD | 935.13 USD | `-35.02%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 4,170,000.00 USD | 0.00 USD | 29,900.00 USD | `-34.91%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 4,140,000.00 USD | 0.00 USD | 1,540.00 USD | `-34.80%` | `2,500.00` |
| `Live` | `Long` | `0.6185` | 4,140,000.00 USD | 0.00 USD | 4,400.00 USD | `-34.70%` | `7,107.00` |
| `Live` | `Long` | `0.6205` | 4,140,000.00 USD | 0.00 USD | 7,160.00 USD | `-34.49%` | `11,545.90` |
| `Live` | `Long` | `0.6245` | 4,130,000.00 USD | 0.00 USD | 356.65 USD | `-34.07%` | `571.10` |
| `Live` | `Long` | `0.6255` | 4,130,000.00 USD | 0.00 USD | 32,070.00 USD | `-33.96%` | `51,265.70` |
| `Live` | `Long` | `0.6265` | 4,100,000.00 USD | 0.00 USD | 546.18 USD | `-33.85%` | `871.80` |
| `Live` | `Long` | `0.6285` | 4,100,000.00 USD | 0.00 USD | 102.45 USD | `-33.64%` | `163.00` |
| `Live` | `Long` | `0.6305` | 4,100,000.00 USD | 0.00 USD | 319.35 USD | `-33.43%` | `506.50` |
| `Live` | `Long` | `0.6315` | 4,100,000.00 USD | 0.00 USD | 3,510.00 USD | `-33.33%` | `5,564.80` |
| `Live` | `Long` | `0.6345` | 4,090,000.00 USD | 0.00 USD | 450.05 USD | `-33.01%` | `709.30` |
| `Live` | `Long` | `0.6355` | 4,090,000.00 USD | 0.00 USD | 207.17 USD | `-32.90%` | `326.00` |
| `Live` | `Long` | `0.6365` | 4,090,000.00 USD | 0.00 USD | 3,970.00 USD | `-32.80%` | `6,240.30` |
| `Live` | `Long` | `0.6375` | 4,090,000.00 USD | 0.00 USD | 2,240.00 USD | `-32.69%` | `3,513.60` |
| `Live` | `Long` | `0.6395` | 4,080,000.00 USD | 0.00 USD | 20,710.00 USD | `-32.48%` | `32,391.70` |
| `Live` | `Long` | `0.6405` | 4,060,000.00 USD | 0.00 USD | 956.01 USD | `-32.38%` | `1,492.60` |
| `Live` | `Long` | `0.6415` | 4,060,000.00 USD | 0.00 USD | 86,920.00 USD | `-32.27%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,980,000.00 USD | 0.00 USD | 477.63 USD | `-32.16%` | `743.40` |
| `Live` | `Long` | `0.6435` | 3,980,000.00 USD | 0.00 USD | 489.83 USD | `-32.06%` | `761.20` |
| `Live` | `Long` | `0.6445` | 3,980,000.00 USD | 0.00 USD | 65,790.00 USD | `-31.95%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,910,000.00 USD | 0.00 USD | 471.21 USD | `-31.85%` | `730.00` |
| `Live` | `Long` | `0.6475` | 3,910,000.00 USD | 0.00 USD | 8,080.00 USD | `-31.64%` | `12,473.20` |
| `Live` | `Long` | `0.6485` | 3,900,000.00 USD | 0.00 USD | 210.50 USD | `-31.53%` | `324.60` |
| `Live` | `Long` | `0.6495` | 3,900,000.00 USD | 0.00 USD | 721.59 USD | `-31.43%` | `1,111.00` |
| `Live` | `Long` | `0.6505` | 3,900,000.00 USD | 0.00 USD | 631.12 USD | `-31.32%` | `970.20` |
| `Live` | `Long` | `0.6515` | 3,900,000.00 USD | 0.00 USD | 408,650.00 USD | `-31.21%` | `627,245.30` |
| `Live` | `Long` | `0.6535` | 3,490,000.00 USD | 0.00 USD | 126,530.00 USD | `-31.00%` | `193,618.10` |
| `Live` | `Long` | `0.6555` | 3,360,000.00 USD | 0.00 USD | 1,580.00 USD | `-30.79%` | `2,403.40` |
| `Live` | `Long` | `0.6565` | 3,360,000.00 USD | 0.00 USD | 35,690.00 USD | `-30.69%` | `54,365.60` |
| `Live` | `Long` | `0.6575` | 3,330,000.00 USD | 0.00 USD | 13,280.00 USD | `-30.58%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,310,000.00 USD | 0.00 USD | 2,970.00 USD | `-30.48%` | `4,508.30` |
| `Live` | `Long` | `0.6595` | 3,310,000.00 USD | 0.00 USD | 635.76 USD | `-30.37%` | `964.00` |
| `Live` | `Long` | `0.6615` | 3,310,000.00 USD | 0.00 USD | 10,930.00 USD | `-30.16%` | `16,517.10` |
| `Live` | `Long` | `0.6625` | 3,300,000.00 USD | 0.00 USD | 38,240.00 USD | `-30.05%` | `57,728.30` |
| `Live` | `Long` | `0.6645` | 3,260,000.00 USD | 0.00 USD | 602.30 USD | `-29.84%` | `906.40` |
| `Live` | `Long` | `0.6675` | 3,260,000.00 USD | 0.00 USD | 5,280.00 USD | `-29.53%` | `7,907.60` |
| `Live` | `Long` | `0.6685` | 3,250,000.00 USD | 0.00 USD | 11,130.00 USD | `-29.42%` | `16,644.30` |
| `Live` | `Long` | `0.6695` | 3,240,000.00 USD | 0.00 USD | 161.22 USD | `-29.31%` | `240.80` |
| `Live` | `Long` | `0.6705` | 3,240,000.00 USD | 0.00 USD | 2,290.00 USD | `-29.21%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,240,000.00 USD | 0.00 USD | 10,560.00 USD | `-29.10%` | `15,729.50` |
| `Live` | `Long` | `0.6725` | 3,230,000.00 USD | 0.00 USD | 1,500.00 USD | `-29.00%` | `2,227.70` |
| `Live` | `Long` | `0.6735` | 3,230,000.00 USD | 0.00 USD | 633.09 USD | `-28.89%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,230,000.00 USD | 0.00 USD | 13,740.00 USD | `-28.79%` | `20,373.20` |
| `Live` | `Long` | `0.6755` | 3,210,000.00 USD | 0.00 USD | 111.59 USD | `-28.68%` | `165.20` |
| `Live` | `Long` | `0.6765` | 3,210,000.00 USD | 0.00 USD | 1,040.00 USD | `-28.58%` | `1,539.20` |
| `Live` | `Long` | `0.6785` | 3,210,000.00 USD | 0.00 USD | 2,950.00 USD | `-28.36%` | `4,351.40` |
| `Live` | `Long` | `0.6795` | 3,210,000.00 USD | 0.00 USD | 5,620.00 USD | `-28.26%` | `8,270.70` |
| `Live` | `Long` | `0.6805` | 3,210,000.00 USD | 0.00 USD | 1,600.00 USD | `-28.15%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 3,200,000.00 USD | 0.00 USD | 3,380.00 USD | `-28.05%` | `4,954.70` |
| `Live` | `Long` | `0.6825` | 3,200,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.94%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 3,180,000.00 USD | 0.00 USD | 6,380.00 USD | `-27.84%` | `9,330.10` |
| `Live` | `Long` | `0.6845` | 3,180,000.00 USD | 0.00 USD | 7,140.00 USD | `-27.73%` | `10,433.20` |
| `Live` | `Long` | `0.6875` | 3,170,000.00 USD | 0.00 USD | 480.49 USD | `-27.41%` | `698.90` |
| `Live` | `Long` | `0.6885` | 3,170,000.00 USD | 0.00 USD | 83,790.00 USD | `-27.31%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 3,090,000.00 USD | 0.00 USD | 2,110.00 USD | `-27.20%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 3,080,000.00 USD | 0.00 USD | 4,010.00 USD | `-27.10%` | `5,800.60` |
| `Live` | `Long` | `0.6915` | 3,080,000.00 USD | 0.00 USD | 8,970.00 USD | `-26.99%` | `12,967.20` |
| `Live` | `Long` | `0.6925` | 3,070,000.00 USD | 0.00 USD | 17,150.00 USD | `-26.89%` | `24,770.70` |
| `Live` | `Long` | `0.6935` | 3,050,000.00 USD | 0.00 USD | 4,400.00 USD | `-26.78%` | `6,342.20` |
| `Live` | `Long` | `0.6955` | 3,050,000.00 USD | 0.00 USD | 560.64 USD | `-26.57%` | `806.10` |
| `Live` | `Long` | `0.6965` | 3,050,000.00 USD | 0.00 USD | 273.03 USD | `-26.46%` | `392.00` |
| `Live` | `Long` | `0.6985` | 3,050,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.25%` | `2,759.10` |
| `Live` | `Long` | `0.7045` | 3,050,000.00 USD | 0.00 USD | 759.59 USD | `-25.62%` | `1,078.20` |
| `Live` | `Long` | `0.7055` | 3,050,000.00 USD | 0.00 USD | 1,170.00 USD | `-25.51%` | `1,661.80` |
| `Live` | `Long` | `0.7065` | 3,050,000.00 USD | 0.00 USD | 769.59 USD | `-25.41%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 3,040,000.00 USD | 0.00 USD | 787.73 USD | `-25.30%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 3,040,000.00 USD | 0.00 USD | 3,890.00 USD | `-25.20%` | `5,484.60` |
| `Live` | `Long` | `0.7095` | 3,040,000.00 USD | 0.00 USD | 2,550.00 USD | `-25.09%` | `3,589.20` |
| `Live` | `Long` | `0.7105` | 3,040,000.00 USD | 0.00 USD | 3,530.00 USD | `-24.99%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 3,030,000.00 USD | 0.00 USD | 718.76 USD | `-24.88%` | `1,010.20` |
| `Live` | `Long` | `0.7125` | 3,030,000.00 USD | 0.00 USD | 156.39 USD | `-24.77%` | `219.50` |
| `Live` | `Long` | `0.7145` | 3,030,000.00 USD | 0.00 USD | 62,620.00 USD | `-24.56%` | `87,642.20` |
| `Live` | `Long` | `0.7165` | 2,970,000.00 USD | 0.00 USD | 8,870.00 USD | `-24.35%` | `12,380.50` |
| `Live` | `Long` | `0.7175` | 2,960,000.00 USD | 0.00 USD | 1,470.00 USD | `-24.25%` | `2,050.00` |
| `Live` | `Long` | `0.7195` | 2,960,000.00 USD | 0.00 USD | 11,720.00 USD | `-24.04%` | `16,293.90` |
| `Live` | `Long` | `0.7215` | 2,950,000.00 USD | 0.00 USD | 742.50 USD | `-23.82%` | `1,029.10` |
| `Live` | `Long` | `0.7225` | 2,950,000.00 USD | 0.00 USD | 129.26 USD | `-23.72%` | `178.90` |
| `Live` | `Long` | `0.7255` | 2,950,000.00 USD | 0.00 USD | 2,660.00 USD | `-23.40%` | `3,662.80` |
| `Live` | `Long` | `0.7265` | 2,940,000.00 USD | 0.00 USD | 1,280.00 USD | `-23.30%` | `1,755.10` |
| `Live` | `Long` | `0.7275` | 2,940,000.00 USD | 0.00 USD | 762.57 USD | `-23.19%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 2,940,000.00 USD | 0.00 USD | 214.03 USD | `-23.09%` | `293.80` |
| `Live` | `Long` | `0.7295` | 2,940,000.00 USD | 0.00 USD | 375.98 USD | `-22.98%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,940,000.00 USD | 0.00 USD | 302,280.00 USD | `-22.87%` | `413,793.50` |
| `Live` | `Long` | `0.7315` | 2,640,000.00 USD | 0.00 USD | 145.42 USD | `-22.77%` | `198.80` |
| `Live` | `Long` | `0.7325` | 2,640,000.00 USD | 0.00 USD | 907.93 USD | `-22.66%` | `1,239.50` |
| `Live` | `Long` | `0.7335` | 2,640,000.00 USD | 0.00 USD | 2,520.00 USD | `-22.56%` | `3,440.40` |
| `Live` | `Long` | `0.7345` | 2,640,000.00 USD | 0.00 USD | 2,340.00 USD | `-22.45%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,630,000.00 USD | 0.00 USD | 51,920.00 USD | `-22.35%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 2,580,000.00 USD | 0.00 USD | 6,900.00 USD | `-22.24%` | `9,366.00` |
| `Live` | `Long` | `0.7375` | 2,570,000.00 USD | 0.00 USD | 1,400.00 USD | `-22.13%` | `1,898.90` |
| `Live` | `Long` | `0.7385` | 2,570,000.00 USD | 0.00 USD | 5,590.00 USD | `-22.03%` | `7,571.70` |
| `Live` | `Long` | `0.7395` | 2,570,000.00 USD | 0.00 USD | 412.05 USD | `-21.92%` | `557.20` |
| `Live` | `Long` | `0.7405` | 2,570,000.00 USD | 0.00 USD | 3,530.00 USD | `-21.82%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,560,000.00 USD | 0.00 USD | 510.15 USD | `-21.71%` | `688.00` |
| `Live` | `Long` | `0.7425` | 2,560,000.00 USD | 0.00 USD | 784,090.00 USD | `-21.61%` | `1,056,015.30` |
| `Live` | `Long` | `0.7445` | 1,780,000.00 USD | 0.00 USD | 105.64 USD | `-21.40%` | `141.90` |
| `Live` | `Long` | `0.7475` | 1,780,000.00 USD | 0.00 USD | 103,310.00 USD | `-21.08%` | `138,200.90` |
| `Live` | `Long` | `0.7485` | 1,680,000.00 USD | 0.00 USD | 105.91 USD | `-20.97%` | `141.50` |
| `Live` | `Long` | `0.7495` | 1,680,000.00 USD | 0.00 USD | 811.78 USD | `-20.87%` | `1,083.10` |
| `Live` | `Long` | `0.7505` | 1,670,000.00 USD | 0.00 USD | 1,580.00 USD | `-20.76%` | `2,098.80` |
| `Live` | `Long` | `0.7515` | 1,670,000.00 USD | 0.00 USD | 1,340.00 USD | `-20.66%` | `1,779.90` |
| `Live` | `Long` | `0.7525` | 1,670,000.00 USD | 0.00 USD | 106.03 USD | `-20.55%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,670,000.00 USD | 0.00 USD | 5,480.00 USD | `-20.45%` | `7,274.30` |
| `Live` | `Long` | `0.7545` | 1,670,000.00 USD | 0.00 USD | 922.07 USD | `-20.34%` | `1,222.10` |
| `Live` | `Long` | `0.7565` | 1,670,000.00 USD | 0.00 USD | 1,900.00 USD | `-20.13%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,660,000.00 USD | 0.00 USD | 36,710.00 USD | `-19.92%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,630,000.00 USD | 0.00 USD | 4,390.00 USD | `-19.81%` | `5,776.10` |
| `Live` | `Long` | `0.7605` | 1,620,000.00 USD | 0.00 USD | 1,530.00 USD | `-19.71%` | `2,013.30` |
| `Live` | `Long` | `0.7615` | 1,620,000.00 USD | 0.00 USD | 351.43 USD | `-19.60%` | `461.50` |
| `Live` | `Long` | `0.7635` | 1,620,000.00 USD | 0.00 USD | 604.16 USD | `-19.39%` | `791.30` |
| `Live` | `Long` | `0.7645` | 1,620,000.00 USD | 0.00 USD | 1,850.00 USD | `-19.28%` | `2,420.30` |
| `Live` | `Long` | `0.7655` | 1,620,000.00 USD | 0.00 USD | 6,290.00 USD | `-19.18%` | `8,212.10` |
| `Live` | `Long` | `0.7665` | 1,610,000.00 USD | 0.00 USD | 499.14 USD | `-19.07%` | `651.20` |
| `Live` | `Long` | `0.7675` | 1,610,000.00 USD | 0.00 USD | 10,680.00 USD | `-18.97%` | `13,912.80` |
| `Live` | `Long` | `0.7685` | 1,600,000.00 USD | 0.00 USD | 499.99 USD | `-18.86%` | `650.60` |
| `Live` | `Long` | `0.7695` | 1,600,000.00 USD | 0.00 USD | 147,750.00 USD | `-18.76%` | `192,010.40` |
| `Live` | `Long` | `0.7705` | 1,450,000.00 USD | 0.00 USD | 842.93 USD | `-18.65%` | `1,094.00` |
| `Live` | `Long` | `0.7715` | 1,450,000.00 USD | 0.00 USD | 3,190.00 USD | `-18.55%` | `4,137.70` |
| `Live` | `Long` | `0.7725` | 1,450,000.00 USD | 0.00 USD | 1,490.00 USD | `-18.44%` | `1,922.50` |
| `Live` | `Long` | `0.7735` | 1,450,000.00 USD | 0.00 USD | 4,570.00 USD | `-18.33%` | `5,912.10` |
| `Live` | `Long` | `0.7745` | 1,440,000.00 USD | 0.00 USD | 184.95 USD | `-18.23%` | `238.80` |
| `Live` | `Long` | `0.7755` | 1,440,000.00 USD | 0.00 USD | 7,660.00 USD | `-18.12%` | `9,882.70` |
| `Live` | `Long` | `0.7765` | 1,430,000.00 USD | 0.00 USD | 4,630.00 USD | `-18.02%` | `5,964.40` |
| `Live` | `Long` | `0.7775` | 1,430,000.00 USD | 0.00 USD | 544.25 USD | `-17.91%` | `700.00` |
| `Live` | `Long` | `0.7785` | 1,430,000.00 USD | 0.00 USD | 6,450.00 USD | `-17.81%` | `8,285.30` |
| `Live` | `Long` | `0.7795` | 1,420,000.00 USD | 0.00 USD | 444.63 USD | `-17.70%` | `570.40` |
| `Live` | `Long` | `0.7815` | 1,420,000.00 USD | 0.00 USD | 4,630.00 USD | `-17.49%` | `5,918.40` |
| `Live` | `Long` | `0.7835` | 1,420,000.00 USD | 0.00 USD | 950.23 USD | `-17.28%` | `1,212.80` |
| `Live` | `Long` | `0.7855` | 1,420,000.00 USD | 0.00 USD | 3,020.00 USD | `-17.07%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 1,410,000.00 USD | 0.00 USD | 44,690.00 USD | `-16.96%` | `56,822.70` |
| `Live` | `Long` | `0.7875` | 1,370,000.00 USD | 0.00 USD | 5,400.00 USD | `-16.86%` | `6,852.00` |
| `Live` | `Long` | `0.7895` | 1,360,000.00 USD | 0.00 USD | 8,660.00 USD | `-16.64%` | `10,969.90` |
| `Live` | `Long` | `0.7905` | 1,360,000.00 USD | 0.00 USD | 4,910.00 USD | `-16.54%` | `6,210.60` |
| `Live` | `Long` | `0.7915` | 1,350,000.00 USD | 0.00 USD | 1,290.00 USD | `-16.43%` | `1,623.50` |
| `Live` | `Long` | `0.7925` | 1,350,000.00 USD | 0.00 USD | 385.87 USD | `-16.33%` | `486.90` |
| `Live` | `Long` | `0.7945` | 1,350,000.00 USD | 0.00 USD | 7,640.00 USD | `-16.12%` | `9,619.00` |
| `Live` | `Long` | `0.7955` | 1,340,000.00 USD | 0.00 USD | 3,030.00 USD | `-16.01%` | `3,807.60` |
| `Live` | `Long` | `0.7975` | 1,340,000.00 USD | 0.00 USD | 1,170.00 USD | `-15.80%` | `1,464.30` |
| `Live` | `Long` | `0.7985` | 1,340,000.00 USD | 0.00 USD | 643.43 USD | `-15.69%` | `805.80` |
| `Live` | `Long` | `0.7995` | 1,340,000.00 USD | 0.00 USD | 2,580.00 USD | `-15.59%` | `3,228.10` |
| `Live` | `Long` | `0.8005` | 1,330,000.00 USD | 0.00 USD | 11,670.00 USD | `-15.48%` | `14,581.70` |
| `Live` | `Long` | `0.8015` | 1,320,000.00 USD | 0.00 USD | 88,780.00 USD | `-15.38%` | `110,767.80` |
| `Live` | `Long` | `0.8025` | 1,230,000.00 USD | 0.00 USD | 421.31 USD | `-15.27%` | `525.00` |
| `Live` | `Long` | `0.8035` | 1,230,000.00 USD | 0.00 USD | 26,280.00 USD | `-15.17%` | `32,702.50` |
| `Live` | `Long` | `0.8045` | 1,210,000.00 USD | 0.00 USD | 15,590.00 USD | `-15.06%` | `19,380.70` |
| `Live` | `Long` | `0.8055` | 1,190,000.00 USD | 0.00 USD | 206.85 USD | `-14.96%` | `256.80` |
| `Live` | `Long` | `0.8085` | 1,190,000.00 USD | 0.00 USD | 22,170.00 USD | `-14.64%` | `27,427.20` |
| `Live` | `Long` | `0.8105` | 1,170,000.00 USD | 0.00 USD | 5,190.00 USD | `-14.43%` | `6,403.40` |
| `Live` | `Long` | `0.8115` | 1,160,000.00 USD | 0.00 USD | 2,620.00 USD | `-14.32%` | `3,234.70` |
| `Live` | `Long` | `0.8135` | 1,160,000.00 USD | 0.00 USD | 11,260.00 USD | `-14.11%` | `13,843.50` |
| `Live` | `Long` | `0.8155` | 1,150,000.00 USD | 0.00 USD | 8,160.00 USD | `-13.90%` | `10,000.00` |
| `Live` | `Long` | `0.8165` | 1,140,000.00 USD | 0.00 USD | 362.12 USD | `-13.79%` | `443.50` |
| `Live` | `Long` | `0.8175` | 1,140,000.00 USD | 0.00 USD | 104,090.00 USD | `-13.69%` | `127,325.20` |
| `Live` | `Long` | `0.8185` | 1,040,000.00 USD | 0.00 USD | 773.65 USD | `-13.58%` | `945.20` |
| `Live` | `Long` | `0.8195` | 1,040,000.00 USD | 0.00 USD | 643.31 USD | `-13.48%` | `785.00` |
| `Live` | `Long` | `0.8205` | 1,040,000.00 USD | 0.00 USD | 2,280.00 USD | `-13.37%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 1,030,000.00 USD | 0.00 USD | 10,310.00 USD | `-13.27%` | `12,555.60` |
| `Live` | `Long` | `0.8225` | 1,020,000.00 USD | 0.00 USD | 466.85 USD | `-13.16%` | `567.60` |
| `Live` | `Long` | `0.8235` | 1,020,000.00 USD | 0.00 USD | 659.29 USD | `-13.05%` | `800.60` |
| `Live` | `Long` | `0.8245` | 1,020,000.00 USD | 0.00 USD | 3,510.00 USD | `-12.95%` | `4,256.50` |
| `Live` | `Long` | `0.8275` | 1,020,000.00 USD | 0.00 USD | 27,960.00 USD | `-12.63%` | `33,785.20` |
| `Live` | `Long` | `0.8285` | 990,090.00 USD | 0.00 USD | 118,200.00 USD | `-12.53%` | `142,661.50` |
| `Live` | `Long` | `0.8295` | 871,890.00 USD | 0.00 USD | 32,530.00 USD | `-12.42%` | `39,217.20` |
| `Live` | `Long` | `0.8305` | 839,360.00 USD | 0.00 USD | 1,670.00 USD | `-12.32%` | `2,011.70` |
| `Live` | `Long` | `0.8325` | 837,690.00 USD | 0.00 USD | 18,980.00 USD | `-12.10%` | `22,795.90` |
| `Live` | `Long` | `0.8335` | 818,710.00 USD | 0.00 USD | 686.97 USD | `-12.00%` | `824.20` |
| `Live` | `Long` | `0.8355` | 818,030.00 USD | 0.00 USD | 17,770.00 USD | `-11.79%` | `21,269.40` |
| `Live` | `Long` | `0.8375` | 800,260.00 USD | 0.00 USD | 137.85 USD | `-11.58%` | `164.60` |
| `Live` | `Long` | `0.8385` | 800,120.00 USD | 0.00 USD | 79,450.00 USD | `-11.47%` | `94,750.80` |
| `Live` | `Long` | `0.8395` | 720,670.00 USD | 0.00 USD | 27,150.00 USD | `-11.37%` | `32,340.20` |
| `Live` | `Long` | `0.8405` | 693,520.00 USD | 0.00 USD | 744.51 USD | `-11.26%` | `885.80` |
| `Live` | `Long` | `0.8415` | 692,780.00 USD | 0.00 USD | 3,890.00 USD | `-11.15%` | `4,616.80` |
| `Live` | `Long` | `0.8425` | 688,890.00 USD | 0.00 USD | 13,400.00 USD | `-11.05%` | `15,906.90` |
| `Live` | `Long` | `0.8435` | 675,490.00 USD | 0.00 USD | 1,340.00 USD | `-10.94%` | `1,582.70` |
| `Live` | `Long` | `0.8445` | 674,160.00 USD | 0.00 USD | 893.23 USD | `-10.84%` | `1,057.70` |
| `Live` | `Long` | `0.8455` | 673,260.00 USD | 0.00 USD | 8,710.00 USD | `-10.73%` | `10,298.10` |
| `Live` | `Long` | `0.8465` | 664,560.00 USD | 0.00 USD | 13,750.00 USD | `-10.63%` | `16,239.20` |
| `Live` | `Long` | `0.8475` | 650,810.00 USD | 0.00 USD | 29,810.00 USD | `-10.52%` | `35,169.30` |
| `Live` | `Long` | `0.8485` | 621,000.00 USD | 0.00 USD | 1,890.00 USD | `-10.42%` | `2,222.00` |
| `Live` | `Long` | `0.8495` | 619,120.00 USD | 0.00 USD | 804.99 USD | `-10.31%` | `947.60` |
| `Live` | `Long` | `0.8515` | 618,310.00 USD | 0.00 USD | 1,220.00 USD | `-10.10%` | `1,433.90` |
| `Live` | `Long` | `0.8525` | 617,090.00 USD | 0.00 USD | 4,220.00 USD | `-9.99%` | `4,952.40` |
| `Live` | `Long` | `0.8535` | 612,870.00 USD | 0.00 USD | 11,410.00 USD | `-9.89%` | `13,374.00` |
| `Live` | `Long` | `0.8545` | 601,450.00 USD | 0.00 USD | 2,030.00 USD | `-9.78%` | `2,375.90` |
| `Live` | `Long` | `0.8555` | 599,420.00 USD | 0.00 USD | 139.53 USD | `-9.68%` | `163.10` |
| `Live` | `Long` | `0.8565` | 599,280.00 USD | 0.00 USD | 36,350.00 USD | `-9.57%` | `42,440.00` |
| `Live` | `Long` | `0.8585` | 562,940.00 USD | 0.00 USD | 14,660.00 USD | `-9.36%` | `17,077.30` |
| `Live` | `Long` | `0.8595` | 548,270.00 USD | 0.00 USD | 7,610.00 USD | `-9.25%` | `8,848.50` |
| `Live` | `Long` | `0.8605` | 540,670.00 USD | 0.00 USD | 19,020.00 USD | `-9.15%` | `22,098.50` |
| `Live` | `Long` | `0.8615` | 521,650.00 USD | 0.00 USD | 2,080.00 USD | `-9.04%` | `2,412.60` |
| `Live` | `Long` | `0.8625` | 519,570.00 USD | 0.00 USD | 9,140.00 USD | `-8.94%` | `10,602.70` |
| `Live` | `Long` | `0.8635` | 510,430.00 USD | 0.00 USD | 4,710.00 USD | `-8.83%` | `5,449.60` |
| `Live` | `Long` | `0.8645` | 505,720.00 USD | 0.00 USD | 2,580.00 USD | `-8.73%` | `2,988.60` |
| `Live` | `Long` | `0.8655` | 503,140.00 USD | 0.00 USD | 2,210.00 USD | `-8.62%` | `2,557.30` |
| `Live` | `Long` | `0.8665` | 500,930.00 USD | 0.00 USD | 1,040.00 USD | `-8.52%` | `1,205.70` |
| `Live` | `Long` | `0.8675` | 499,880.00 USD | 0.00 USD | 11,820.00 USD | `-8.41%` | `13,628.20` |
| `Live` | `Long` | `0.8685` | 488,060.00 USD | 0.00 USD | 289.04 USD | `-8.30%` | `332.80` |
| `Live` | `Long` | `0.8695` | 487,770.00 USD | 0.00 USD | 5,030.00 USD | `-8.20%` | `5,786.10` |
| `Live` | `Long` | `0.8705` | 482,740.00 USD | 0.00 USD | 14,970.00 USD | `-8.09%` | `17,194.90` |
| `Live` | `Long` | `0.8715` | 467,770.00 USD | 0.00 USD | 2,870.00 USD | `-7.99%` | `3,293.40` |
| `Live` | `Long` | `0.8725` | 464,900.00 USD | 0.00 USD | 29,520.00 USD | `-7.88%` | `33,829.20` |
| `Live` | `Long` | `0.8735` | 435,390.00 USD | 0.00 USD | 13,270.00 USD | `-7.78%` | `15,188.90` |
| `Live` | `Long` | `0.8745` | 422,120.00 USD | 0.00 USD | 15,980.00 USD | `-7.67%` | `18,267.80` |
| `Live` | `Long` | `0.8755` | 406,140.00 USD | 0.00 USD | 1,420.00 USD | `-7.56%` | `1,624.00` |
| `Live` | `Long` | `0.8765` | 404,720.00 USD | 0.00 USD | 33,510.00 USD | `-7.46%` | `38,226.70` |
| `Live` | `Long` | `0.8775` | 371,220.00 USD | 0.00 USD | 16,030.00 USD | `-7.35%` | `18,270.50` |
| `Live` | `Long` | `0.8785` | 355,180.00 USD | 0.00 USD | 56,160.00 USD | `-7.25%` | `63,924.50` |
| `Live` | `Long` | `0.8795` | 299,030.00 USD | 0.00 USD | 172,470.00 USD | `-7.14%` | `196,099.30` |
| `Live` | `Long` | `0.8805` | 126,560.00 USD | 0.00 USD | 1,530.00 USD | `-7.04%` | `1,737.40` |
| `Live` | `Long` | `0.8815` | 125,030.00 USD | 0.00 USD | 8,730.00 USD | `-6.93%` | `9,904.10` |
| `Live` | `Long` | `0.8825` | 116,300.00 USD | 0.00 USD | 5,300.00 USD | `-6.83%` | `6,002.40` |
| `Live` | `Long` | `0.8835` | 111,000.00 USD | 0.00 USD | 7,220.00 USD | `-6.72%` | `8,171.40` |
| `Live` | `Long` | `0.8845` | 103,780.00 USD | 0.00 USD | 3,550.00 USD | `-6.61%` | `4,018.00` |
| `Live` | `Long` | `0.8855` | 100,230.00 USD | 0.00 USD | 2,660.00 USD | `-6.51%` | `2,998.60` |
| `Live` | `Long` | `0.8865` | 97,570.00 USD | 0.00 USD | 28,370.00 USD | `-6.40%` | `31,996.80` |
| `Live` | `Long` | `0.8875` | 69,200.00 USD | 0.00 USD | 12,780.00 USD | `-6.30%` | `14,398.30` |
| `Live` | `Long` | `0.8885` | 56,430.00 USD | 0.00 USD | 697.38 USD | `-6.19%` | `784.90` |
| `Live` | `Long` | `0.8895` | 55,730.00 USD | 0.00 USD | 3,530.00 USD | `-6.09%` | `3,972.10` |
| `Live` | `Long` | `0.8905` | 52,200.00 USD | 0.00 USD | 139.90 USD | `-5.98%` | `157.10` |
| `Live` | `Long` | `0.8915` | 52,060.00 USD | 0.00 USD | 1,100.00 USD | `-5.88%` | `1,229.80` |
| `Live` | `Long` | `0.8925` | 50,960.00 USD | 0.00 USD | 1,040.00 USD | `-5.77%` | `1,162.90` |
| `Live` | `Long` | `0.8935` | 49,920.00 USD | 0.00 USD | 2,470.00 USD | `-5.66%` | `2,762.70` |
| `Live` | `Long` | `0.8945` | 47,450.00 USD | 0.00 USD | 5,380.00 USD | `-5.56%` | `6,014.50` |
| `Live` | `Long` | `0.8965` | 42,070.00 USD | 0.00 USD | 29,550.00 USD | `-5.35%` | `32,958.10` |
| `Live` | `Long` | `0.8975` | 12,530.00 USD | 0.00 USD | 3,540.00 USD | `-5.24%` | `3,941.60` |
| `Live` | `Long` | `0.8985` | 8,990.00 USD | 0.00 USD | 320.05 USD | `-5.14%` | `356.20` |
| `Live` | `Long` | `0.8995` | 8,670.00 USD | 0.00 USD | 143.92 USD | `-5.03%` | `160.00` |
| `Live` | `Short` | `0.9005` | 2,600.00 USD | 2,600.00 USD | 0.00 USD | `-4.93%` | `2,889.30` |
| `Live` | `Long` | `0.9055` | 8,520.00 USD | 0.00 USD | 300.72 USD | `-4.40%` | `332.10` |
| `Live` | `Long` | `0.9075` | 8,220.00 USD | 0.00 USD | 8,220.00 USD | `-4.19%` | `9,062.20` |
| `Live` | `Short` | `0.9675` | 5,760.00 USD | 3,160.00 USD | 0.00 USD | `+2.15%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 70,830.00 USD | 65,060.00 USD | 0.00 USD | `+2.47%` | `67,040.50` |
| `Live` | `Short` | `0.9765` | 71,040.00 USD | 214.44 USD | 0.00 USD | `+3.10%` | `219.60` |
| `Live` | `Short` | `0.9805` | 86,620.00 USD | 15,580.00 USD | 0.00 USD | `+3.52%` | `15,886.90` |
| `Live` | `Short` | `0.9845` | 97,060.00 USD | 10,440.00 USD | 0.00 USD | `+3.94%` | `10,608.60` |
| `Live` | `Short` | `0.9875` | 151,980.00 USD | 54,920.00 USD | 0.00 USD | `+4.26%` | `55,611.80` |
| `Live` | `Short` | `0.9885` | 165,530.00 USD | 13,550.00 USD | 0.00 USD | `+4.37%` | `13,712.20` |
| `Live` | `Short` | `0.9895` | 171,300.00 USD | 5,760.00 USD | 0.00 USD | `+4.47%` | `5,824.20` |
| `Live` | `Short` | `0.9905` | 191,350.00 USD | 20,050.00 USD | 0.00 USD | `+4.58%` | `20,246.30` |
| `Live` | `Short` | `0.9925` | 193,640.00 USD | 2,290.00 USD | 0.00 USD | `+4.79%` | `2,309.60` |
| `Live` | `Short` | `0.9945` | 200,070.00 USD | 6,430.00 USD | 0.00 USD | `+5.00%` | `6,462.70` |
| `Live` | `Short` | `0.9965` | 205,510.00 USD | 5,440.00 USD | 0.00 USD | `+5.21%` | `5,463.60` |
| `Live` | `Short` | `1.00` | 205,960.00 USD | 449.11 USD | 0.00 USD | `+6.06%` | `447.10` |
| `Live` | `Short` | `1.01` | 323,820.00 USD | 117,860.00 USD | 0.00 USD | `+6.90%` | `116,406.80` |
| `Live` | `Short` | `1.02` | 323,990.00 USD | 170.40 USD | 0.00 USD | `+7.22%` | `167.80` |
| `Live` | `Short` | `1.03` | 332,830.00 USD | 8,840.00 USD | 0.00 USD | `+8.59%` | `8,592.20` |
| `Live` | `Short` | `1.04` | 343,230.00 USD | 10,400.00 USD | 0.00 USD | `+9.75%` | `10,007.60` |
| `Live` | `Short` | `1.04` | 343,370.00 USD | 139.22 USD | 0.00 USD | `+9.86%` | `133.80` |
| `Live` | `Short` | `1.05` | 343,970.00 USD | 597.52 USD | 0.00 USD | `+10.91%` | `568.80` |
| `Live` | `Short` | `1.05` | 346,360.00 USD | 2,390.00 USD | 0.00 USD | `+11.02%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 347,690.00 USD | 1,330.00 USD | 0.00 USD | `+11.12%` | `1,260.50` |
| `Live` | `Short` | `1.05` | 348,000.00 USD | 317.52 USD | 0.00 USD | `+11.23%` | `301.40` |
| `Live` | `Short` | `1.05` | 348,220.00 USD | 217.44 USD | 0.00 USD | `+11.33%` | `206.20` |
| `Live` | `Short` | `1.07` | 348,330.00 USD | 112.62 USD | 0.00 USD | `+12.71%` | `105.50` |
| `Live` | `Short` | `1.07` | 349,650.00 USD | 1,310.00 USD | 0.00 USD | `+13.45%` | `1,222.30` |
| `Live` | `Short` | `1.08` | 350,800.00 USD | 1,150.00 USD | 0.00 USD | `+13.76%` | `1,066.30` |
| `Live` | `Short` | `1.08` | 363,590.00 USD | 12,800.00 USD | 0.00 USD | `+13.97%` | `11,855.60` |
| `Live` | `Short` | `1.08` | 367,180.00 USD | 3,580.00 USD | 0.00 USD | `+14.08%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 367,340.00 USD | 166.43 USD | 0.00 USD | `+14.40%` | `153.60` |
| `Live` | `Short` | `1.08` | 368,460.00 USD | 1,110.00 USD | 0.00 USD | `+14.50%` | `1,026.10` |
| `Live` | `Short` | `1.09` | 374,010.00 USD | 5,550.00 USD | 0.00 USD | `+15.03%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 374,330.00 USD | 324.90 USD | 0.00 USD | `+16.09%` | `295.50` |
| `Live` | `Short` | `1.10` | 374,610.00 USD | 277.22 USD | 0.00 USD | `+16.19%` | `251.90` |
| `Live` | `Short` | `1.13` | 397,920.00 USD | 23,310.00 USD | 0.00 USD | `+18.94%` | `20,691.10` |
| `Live` | `Short` | `1.16` | 666,270.00 USD | 268,350.00 USD | 0.00 USD | `+22.74%` | `230,842.00` |
| `Live` | `Short` | `1.20` | 667,730.00 USD | 1,450.00 USD | 0.00 USD | `+26.43%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 667,980.00 USD | 253.69 USD | 0.00 USD | `+26.64%` | `211.50` |
| `Live` | `Short` | `1.20` | 677,130.00 USD | 9,150.00 USD | 0.00 USD | `+26.85%` | `7,618.00` |
| `Live` | `Short` | `1.20` | 706,890.00 USD | 29,760.00 USD | 0.00 USD | `+26.96%` | `24,749.90` |
| `Live` | `Short` | `1.21` | 707,040.00 USD | 147.43 USD | 0.00 USD | `+27.28%` | `122.30` |
| `Live` | `Short` | `1.22` | 711,490.00 USD | 4,440.00 USD | 0.00 USD | `+28.65%` | `3,646.70` |
| `Live` | `Short` | `1.23` | 711,870.00 USD | 380.84 USD | 0.00 USD | `+30.34%` | `308.50` |
| `Live` | `Short` | `1.24` | 717,170.00 USD | 5,310.00 USD | 0.00 USD | `+31.08%` | `4,273.60` |
| `Live` | `Short` | `1.26` | 717,310.00 USD | 137.21 USD | 0.00 USD | `+32.66%` | `109.20` |
| `Live` | `Short` | `1.26` | 719,980.00 USD | 2,670.00 USD | 0.00 USD | `+32.98%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 759,860.00 USD | 39,880.00 USD | 0.00 USD | `+35.41%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 760,090.00 USD | 226.80 USD | 0.00 USD | `+36.67%` | `175.20` |
| `Live` | `Short` | `1.30` | 760,200.00 USD | 114.40 USD | 0.00 USD | `+37.10%` | `88.10` |
| `Live` | `Short` | `1.31` | 761,220.00 USD | 1,020.00 USD | 0.00 USD | `+38.15%` | `777.20` |
| `Live` | `Short` | `1.31` | 792,750.00 USD | 31,530.00 USD | 0.00 USD | `+38.47%` | `24,042.40` |
| `Live` | `Short` | `1.32` | 794,920.00 USD | 2,170.00 USD | 0.00 USD | `+39.84%` | `1,639.00` |
| `Live` | `Short` | `1.33` | 801,260.00 USD | 6,340.00 USD | 0.00 USD | `+39.95%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 823,230.00 USD | 21,970.00 USD | 0.00 USD | `+40.26%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 823,480.00 USD | 253.40 USD | 0.00 USD | `+40.37%` | `190.60` |
| `Live` | `Short` | `1.33` | 823,840.00 USD | 358.30 USD | 0.00 USD | `+40.47%` | `269.30` |
| `Live` | `Short` | `1.33` | 825,360.00 USD | 1,520.00 USD | 0.00 USD | `+40.69%` | `1,143.40` |
| `Live` | `Short` | `1.34` | 832,220.00 USD | 6,860.00 USD | 0.00 USD | `+41.42%` | `5,119.30` |
| `Live` | `Short` | `1.36` | 832,360.00 USD | 142.87 USD | 0.00 USD | `+43.11%` | `105.40` |
| `Live` | `Short` | `1.37` | 833,530.00 USD | 1,170.00 USD | 0.00 USD | `+44.17%` | `854.60` |
| `Live` | `Short` | `1.37` | 1,190,000.00 USD | 358,280.00 USD | 0.00 USD | `+44.91%` | `261,043.60` |
| `Live` | `Short` | `1.38` | 1,360,000.00 USD | 171,940.00 USD | 0.00 USD | `+45.23%` | `125,000.00` |
| `Live` | `Short` | `1.41` | 1,370,000.00 USD | 4,450.00 USD | 0.00 USD | `+49.34%` | `3,142.60` |
| `Live` | `Short` | `1.42` | 1,370,000.00 USD | 139.20 USD | 0.00 USD | `+49.66%` | `98.20` |
| `Live` | `Short` | `1.44` | 1,370,000.00 USD | 402.08 USD | 0.00 USD | `+51.67%` | `279.90` |
| `Live` | `Short` | `1.44` | 1,370,000.00 USD | 288.68 USD | 0.00 USD | `+52.09%` | `200.40` |
| `Live` | `Short` | `1.45` | 1,370,000.00 USD | 4,740.00 USD | 0.00 USD | `+52.62%` | `3,279.70` |
| `Live` | `Short` | `1.45` | 1,370,000.00 USD | 1,200.00 USD | 0.00 USD | `+53.25%` | `826.40` |
| `Live` | `Short` | `1.45` | 1,380,000.00 USD | 9,430.00 USD | 0.00 USD | `+53.35%` | `6,491.20` |
| `Live` | `Short` | `1.51` | 1,390,000.00 USD | 4,020.00 USD | 0.00 USD | `+59.90%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 3,870,000.00 USD | 2,480,000.00 USD | 0.00 USD | `+61.27%` | `1,622,322.00` |
| `Live` | `Short` | `1.54` | 3,870,000.00 USD | 144.34 USD | 0.00 USD | `+62.12%` | `94.00` |
| `Live` | `Short` | `1.54` | 3,890,000.00 USD | 24,510.00 USD | 0.00 USD | `+62.33%` | `15,941.90` |
| `Live` | `Short` | `1.58` | 3,890,000.00 USD | 120.29 USD | 0.00 USD | `+66.45%` | `76.30` |
| `Live` | `Short` | `1.61` | 3,900,000.00 USD | 9,650.00 USD | 0.00 USD | `+69.83%` | `6,000.00` |
| `Live` | `Short` | `1.61` | 3,900,000.00 USD | 291.72 USD | 0.00 USD | `+70.35%` | `180.80` |
| `Live` | `Short` | `1.63` | 4,180,000.00 USD | 281,210.00 USD | 0.00 USD | `+71.62%` | `173,000.00` |
| `Live` | `Short` | `1.64` | 4,200,000.00 USD | 18,320.00 USD | 0.00 USD | `+72.99%` | `11,182.60` |
| `Live` | `Short` | `1.65` | 4,220,000.00 USD | 21,330.00 USD | 0.00 USD | `+73.84%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 4,230,000.00 USD | 9,340.00 USD | 0.00 USD | `+74.68%` | `5,645.40` |
| `Live` | `Short` | `1.67` | 4,270,000.00 USD | 39,260.00 USD | 0.00 USD | `+76.16%` | `23,529.40` |
| `Live` | `Short` | `1.71` | 4,360,000.00 USD | 84,600.00 USD | 0.00 USD | `+80.28%` | `49,543.90` |
| `Live` | `Short` | `1.71` | 4,360,000.00 USD | 238.30 USD | 0.00 USD | `+80.49%` | `139.40` |
| `Live` | `Short` | `1.71` | 4,360,000.00 USD | 205.67 USD | 0.00 USD | `+80.81%` | `120.10` |
| `Live` | `Short` | `1.72` | 4,360,000.00 USD | 112.65 USD | 0.00 USD | `+81.86%` | `65.40` |
| `Live` | `Short` | `1.73` | 4,360,000.00 USD | 226.05 USD | 0.00 USD | `+83.02%` | `130.40` |
| `Live` | `Short` | `1.74` | 4,360,000.00 USD | 2,080.00 USD | 0.00 USD | `+83.76%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 4,380,000.00 USD | 19,920.00 USD | 0.00 USD | `+84.92%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 4,390,000.00 USD | 11,350.00 USD | 0.00 USD | `+85.03%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 4,390,000.00 USD | 1,520.00 USD | 0.00 USD | `+85.24%` | `868.90` |
| `Live` | `Short` | `1.76` | 4,410,000.00 USD | 18,400.00 USD | 0.00 USD | `+85.66%` | `10,466.10` |
| `Live` | `Short` | `1.76` | 4,410,000.00 USD | 238.64 USD | 0.00 USD | `+86.08%` | `135.40` |
| `Live` | `Short` | `1.79` | 4,410,000.00 USD | 781.77 USD | 0.00 USD | `+88.62%` | `437.60` |
| `Live` | `Short` | `1.79` | 4,410,000.00 USD | 952.52 USD | 0.00 USD | `+89.46%` | `530.80` |
| `Live` | `Short` | `1.82` | 4,410,000.00 USD | 2,480.00 USD | 0.00 USD | `+92.21%` | `1,360.10` |
| `Live` | `Short` | `1.83` | 4,430,000.00 USD | 14,230.00 USD | 0.00 USD | `+92.84%` | `7,789.30` |
| `Live` | `Short` | `1.83` | 4,430,000.00 USD | 203.88 USD | 0.00 USD | `+93.05%` | `111.50` |
| `Live` | `Short` | `1.85` | 4,430,000.00 USD | 943.75 USD | 0.00 USD | `+95.38%` | `510.00` |
| `Live` | `Short` | `1.85` | 4,430,000.00 USD | 190.35 USD | 0.00 USD | `+95.69%` | `102.70` |
| `Live` | `Short` | `1.88` | 4,430,000.00 USD | 149.36 USD | 0.00 USD | `+98.86%` | `79.30` |
| `Live` | `Short` | `1.89` | 4,430,000.00 USD | 2,010.00 USD | 0.00 USD | `+99.18%` | `1,065.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2745` | 1,930,000.00 USD | 0.00 USD | 455.97 USD | `-71.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,930,000.00 USD | 0.00 USD | 102.75 USD | `-63.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,930,000.00 USD | 0.00 USD | 256.78 USD | `-62.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,930,000.00 USD | 0.00 USD | 428.87 USD | `-58.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,930,000.00 USD | 0.00 USD | 123.45 USD | `-56.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,930,000.00 USD | 0.00 USD | 818.15 USD | `-55.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 1,930,000.00 USD | 0.00 USD | 454.04 USD | `-54.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,930,000.00 USD | 0.00 USD | 436.41 USD | `-54.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,930,000.00 USD | 0.00 USD | 876.79 USD | `-54.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,930,000.00 USD | 0.00 USD | 466.72 USD | `-52.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,930,000.00 USD | 0.00 USD | 142.95 USD | `-49.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,930,000.00 USD | 0.00 USD | 5,650.00 USD | `-47.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,920,000.00 USD | 0.00 USD | 151.74 USD | `-45.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,920,000.00 USD | 0.00 USD | 123.91 USD | `-45.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,920,000.00 USD | 0.00 USD | 219.80 USD | `-41.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,920,000.00 USD | 0.00 USD | 237,400.00 USD | `-41.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 1,690,000.00 USD | 0.00 USD | 276.75 USD | `-41.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 1,690,000.00 USD | 0.00 USD | 2,010.00 USD | `-40.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 1,680,000.00 USD | 0.00 USD | 119.76 USD | `-38.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 1,680,000.00 USD | 0.00 USD | 108.39 USD | `-36.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 1,680,000.00 USD | 0.00 USD | 123.28 USD | `-36.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 1,680,000.00 USD | 0.00 USD | 488.52 USD | `-34.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 1,680,000.00 USD | 0.00 USD | 5,940.00 USD | `-33.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 1,680,000.00 USD | 0.00 USD | 242.24 USD | `-33.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 1,680,000.00 USD | 0.00 USD | 193.95 USD | `-31.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 1,680,000.00 USD | 0.00 USD | 647.50 USD | `-31.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 1,680,000.00 USD | 0.00 USD | 834.79 USD | `-31.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 1,680,000.00 USD | 0.00 USD | 158.54 USD | `-31.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 1,670,000.00 USD | 0.00 USD | 195.47 USD | `-30.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 1,670,000.00 USD | 0.00 USD | 190.25 USD | `-30.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 1,670,000.00 USD | 0.00 USD | 52,450.00 USD | `-29.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 1,620,000.00 USD | 0.00 USD | 536.11 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 1,620,000.00 USD | 0.00 USD | 5,490.00 USD | `-28.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 1,620,000.00 USD | 0.00 USD | 340.75 USD | `-28.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 1,620,000.00 USD | 0.00 USD | 9,270.00 USD | `-27.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 1,610,000.00 USD | 0.00 USD | 120.53 USD | `-26.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6935` | 1,610,000.00 USD | 0.00 USD | 126.98 USD | `-26.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 1,610,000.00 USD | 0.00 USD | 160.71 USD | `-26.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 1,610,000.00 USD | 0.00 USD | 187.61 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 1,610,000.00 USD | 0.00 USD | 2,920.00 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 1,600,000.00 USD | 0.00 USD | 89,150.00 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 1,510,000.00 USD | 0.00 USD | 189.06 USD | `-25.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 1,510,000.00 USD | 0.00 USD | 5,650.00 USD | `-25.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 1,510,000.00 USD | 0.00 USD | 100.47 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 1,510,000.00 USD | 0.00 USD | 152.05 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 1,510,000.00 USD | 0.00 USD | 123.41 USD | `-24.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 1,510,000.00 USD | 0.00 USD | 1,130.00 USD | `-22.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 1,510,000.00 USD | 0.00 USD | 18,770.00 USD | `-22.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 1,490,000.00 USD | 0.00 USD | 257.26 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 1,490,000.00 USD | 0.00 USD | 10,160.00 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 1,480,000.00 USD | 0.00 USD | 93,810.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 1,380,000.00 USD | 0.00 USD | 1,230.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 1,380,000.00 USD | 0.00 USD | 924.99 USD | `-19.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 1,380,000.00 USD | 0.00 USD | 804.61 USD | `-19.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 1,380,000.00 USD | 0.00 USD | 191.12 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 1,380,000.00 USD | 0.00 USD | 1,370.00 USD | `-18.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 1,380,000.00 USD | 0.00 USD | 125.92 USD | `-18.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 1,380,000.00 USD | 0.00 USD | 1,150.00 USD | `-18.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 1,380,000.00 USD | 0.00 USD | 200.39 USD | `-18.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 1,380,000.00 USD | 0.00 USD | 1,860.00 USD | `-17.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 1,380,000.00 USD | 0.00 USD | 128.47 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 1,380,000.00 USD | 0.00 USD | 3,130.00 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 1,370,000.00 USD | 0.00 USD | 135.11 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 1,370,000.00 USD | 0.00 USD | 1,500.00 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 1,370,000.00 USD | 0.00 USD | 25,170.00 USD | `-16.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 1,350,000.00 USD | 0.00 USD | 103.42 USD | `-16.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 1,350,000.00 USD | 0.00 USD | 1,260.00 USD | `-15.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 1,340,000.00 USD | 0.00 USD | 5,660.00 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 1,340,000.00 USD | 0.00 USD | 144.67 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 1,340,000.00 USD | 0.00 USD | 50,540.00 USD | `-14.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 1,290,000.00 USD | 0.00 USD | 263.25 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 1,290,000.00 USD | 0.00 USD | 16,870.00 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 1,270,000.00 USD | 0.00 USD | 91,080.00 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 1,180,000.00 USD | 0.00 USD | 174.63 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8175` | 1,180,000.00 USD | 0.00 USD | 16,350.00 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 1,160,000.00 USD | 0.00 USD | 125.72 USD | `-13.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 1,160,000.00 USD | 0.00 USD | 340.83 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 1,160,000.00 USD | 0.00 USD | 11,040.00 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 1,150,000.00 USD | 0.00 USD | 922.29 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 1,150,000.00 USD | 0.00 USD | 1,120.00 USD | `-12.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 1,150,000.00 USD | 0.00 USD | 124.43 USD | `-12.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 1,150,000.00 USD | 0.00 USD | 4,380.00 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 1,150,000.00 USD | 0.00 USD | 171.46 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 1,140,000.00 USD | 0.00 USD | 1,270.00 USD | `-12.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 1,140,000.00 USD | 0.00 USD | 4,170.00 USD | `-11.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 1,140,000.00 USD | 0.00 USD | 610.23 USD | `-11.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 1,140,000.00 USD | 0.00 USD | 475.87 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 1,140,000.00 USD | 0.00 USD | 320.31 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 1,140,000.00 USD | 0.00 USD | 1,010.00 USD | `-11.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8425` | 1,140,000.00 USD | 0.00 USD | 1,390.00 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 1,140,000.00 USD | 0.00 USD | 221.25 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 1,140,000.00 USD | 0.00 USD | 212.81 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 1,140,000.00 USD | 0.00 USD | 462.49 USD | `-10.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 1,130,000.00 USD | 0.00 USD | 108.44 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 1,130,000.00 USD | 0.00 USD | 481.80 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 1,130,000.00 USD | 0.00 USD | 12,210.00 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 1,120,000.00 USD | 0.00 USD | 901.40 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 1,120,000.00 USD | 0.00 USD | 242.93 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 1,120,000.00 USD | 0.00 USD | 6,200.00 USD | `-9.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 1,110,000.00 USD | 0.00 USD | 108.13 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 1,110,000.00 USD | 0.00 USD | 1,640.00 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 1,110,000.00 USD | 0.00 USD | 4,300.00 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 1,110,000.00 USD | 0.00 USD | 202.45 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 1,110,000.00 USD | 0.00 USD | 921.70 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 1,110,000.00 USD | 0.00 USD | 161.49 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 1,110,000.00 USD | 0.00 USD | 1,270.00 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 1,110,000.00 USD | 0.00 USD | 741.45 USD | `-8.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 1,110,000.00 USD | 0.00 USD | 168.75 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 1,110,000.00 USD | 0.00 USD | 2,110.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 1,100,000.00 USD | 0.00 USD | 3,350.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 1,100,000.00 USD | 0.00 USD | 712.45 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 1,100,000.00 USD | 0.00 USD | 58,490.00 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 1,040,000.00 USD | 0.00 USD | 281.70 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 1,040,000.00 USD | 0.00 USD | 133.10 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 1,040,000.00 USD | 0.00 USD | 246.98 USD | `-7.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 1,040,000.00 USD | 0.00 USD | 876.50 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 1,040,000.00 USD | 0.00 USD | 9,070.00 USD | `-7.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 1,030,000.00 USD | 0.00 USD | 151.10 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 1,030,000.00 USD | 0.00 USD | 507.74 USD | `-7.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 1,030,000.00 USD | 0.00 USD | 8,100.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 1,020,000.00 USD | 0.00 USD | 157,870.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 863,140.00 USD | 0.00 USD | 5,020.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 858,120.00 USD | 0.00 USD | 11,690.00 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 846,430.00 USD | 0.00 USD | 559.80 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8855` | 845,870.00 USD | 0.00 USD | 3,660.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 842,210.00 USD | 0.00 USD | 11,560.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 830,650.00 USD | 0.00 USD | 886.79 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8885` | 829,770.00 USD | 0.00 USD | 11,360.00 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 818,410.00 USD | 0.00 USD | 7,820.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8905` | 810,600.00 USD | 0.00 USD | 10,130.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 800,470.00 USD | 0.00 USD | 469.91 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 800,000.00 USD | 0.00 USD | 10,610.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 789,390.00 USD | 0.00 USD | 7,100.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8945` | 782,290.00 USD | 0.00 USD | 2,920.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8955` | 779,370.00 USD | 0.00 USD | 3,900.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 775,470.00 USD | 0.00 USD | 7,930.00 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8975` | 767,540.00 USD | 0.00 USD | 18,210.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 749,340.00 USD | 0.00 USD | 2,460.00 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8995` | 746,870.00 USD | 0.00 USD | 28,960.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 717,910.00 USD | 0.00 USD | 4,300.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9015` | 713,610.00 USD | 0.00 USD | 1,230.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 712,390.00 USD | 0.00 USD | 926.06 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 711,460.00 USD | 0.00 USD | 561.16 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 710,900.00 USD | 0.00 USD | 1,140.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9055` | 709,760.00 USD | 0.00 USD | 1,990.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 707,770.00 USD | 0.00 USD | 30,120.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 677,650.00 USD | 0.00 USD | 4,680.00 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 672,970.00 USD | 0.00 USD | 1,440.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 671,530.00 USD | 0.00 USD | 1,520.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9105` | 670,000.00 USD | 0.00 USD | 637.90 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 669,360.00 USD | 0.00 USD | 6,170.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9125` | 663,200.00 USD | 0.00 USD | 14,760.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 648,440.00 USD | 0.00 USD | 465.70 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 647,970.00 USD | 0.00 USD | 337.72 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 647,630.00 USD | 0.00 USD | 5,070.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 642,560.00 USD | 0.00 USD | 5,040.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 637,520.00 USD | 0.00 USD | 1,470.00 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 636,050.00 USD | 0.00 USD | 302.74 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 635,750.00 USD | 0.00 USD | 1,380.00 USD | `-2.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 634,370.00 USD | 0.00 USD | 16,090.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 618,280.00 USD | 0.00 USD | 7,650.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 610,630.00 USD | 0.00 USD | 84,100.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 526,530.00 USD | 0.00 USD | 3,230.00 USD | `-2.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 523,300.00 USD | 0.00 USD | 498.77 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 522,800.00 USD | 0.00 USD | 235,060.00 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 287,740.00 USD | 0.00 USD | 160,180.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 127,560.00 USD | 0.00 USD | 146.27 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 127,410.00 USD | 0.00 USD | 195.17 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 127,220.00 USD | 0.00 USD | 103.17 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 127,110.00 USD | 0.00 USD | 186.29 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 126,930.00 USD | 0.00 USD | 148.85 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 126,780.00 USD | 0.00 USD | 5,600.00 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 121,180.00 USD | 0.00 USD | 979.71 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9345` | 120,200.00 USD | 0.00 USD | 45,680.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 74,520.00 USD | 0.00 USD | 1,470.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9365` | 73,050.00 USD | 0.00 USD | 103.95 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9375` | 72,940.00 USD | 0.00 USD | 175.88 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9385` | 72,770.00 USD | 0.00 USD | 53,060.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9395` | 19,710.00 USD | 0.00 USD | 3,910.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9405` | 15,800.00 USD | 0.00 USD | 8,960.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9415` | 6,840.00 USD | 0.00 USD | 158.55 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9425` | 6,680.00 USD | 0.00 USD | 132.80 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9435` | 6,550.00 USD | 0.00 USD | 121.15 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9445` | 6,430.00 USD | 0.00 USD | 4,340.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9455` | 2,080.00 USD | 0.00 USD | 1,030.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9465` | 1,050.00 USD | 0.00 USD | 1,050.00 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 6,000.00 USD | 6,000.00 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 6,160.00 USD | 158.49 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 6,420.00 USD | 261.97 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 6,690.00 USD | 265.66 USD | 0.00 USD | `+0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 6,950.00 USD | 263.76 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 7,950.00 USD | 999.27 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 10,510.00 USD | 2,560.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 13,660.00 USD | 3,150.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 15,090.00 USD | 1,440.00 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 17,980.00 USD | 2,890.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 25,580.00 USD | 7,600.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 33,440.00 USD | 7,860.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 33,540.00 USD | 100.17 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 74,390.00 USD | 40,840.00 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 74,550.00 USD | 161.82 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 74,750.00 USD | 197.79 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 75,650.00 USD | 900.10 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 76,980.00 USD | 1,340.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 77,190.00 USD | 204.20 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 79,050.00 USD | 1,860.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 82,640.00 USD | 3,590.00 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 83,790.00 USD | 1,150.00 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 84,300.00 USD | 513.54 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 89,610.00 USD | 5,310.00 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 89,820.00 USD | 210.33 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 90,940.00 USD | 1,130.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 101,520.00 USD | 10,580.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 101,780.00 USD | 253.14 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 102,020.00 USD | 244.81 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 102,310.00 USD | 285.72 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 102,510.00 USD | 201.77 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 102,930.00 USD | 421.87 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 139,390.00 USD | 36,450.00 USD | 0.00 USD | `+3.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 144,850.00 USD | 5,470.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 145,570.00 USD | 714.28 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 146,630.00 USD | 1,060.00 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 146,900.00 USD | 271.90 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 147,390.00 USD | 490.99 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 148,160.00 USD | 769.72 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 149,160.00 USD | 991.50 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 159,490.00 USD | 10,340.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 159,780.00 USD | 284.92 USD | 0.00 USD | `+5.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 160,050.00 USD | 277.64 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 160,400.00 USD | 350.37 USD | 0.00 USD | `+5.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 160,550.00 USD | 144.04 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 160,650.00 USD | 105.44 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 169,420.00 USD | 8,760.00 USD | 0.00 USD | `+5.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 170,990.00 USD | 1,570.00 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 173,170.00 USD | 2,180.00 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 173,530.00 USD | 363.87 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 174,120.00 USD | 589.52 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 174,780.00 USD | 660.52 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 184,870.00 USD | 10,090.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 190,290.00 USD | 5,420.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 193,060.00 USD | 2,770.00 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 226,520.00 USD | 33,450.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 227,240.00 USD | 722.63 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 227,550.00 USD | 312.07 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 227,720.00 USD | 171.24 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 228,280.00 USD | 561.11 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 229,890.00 USD | 1,610.00 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 232,110.00 USD | 2,210.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 232,540.00 USD | 432.18 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 232,680.00 USD | 137.88 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 236,840.00 USD | 4,170.00 USD | 0.00 USD | `+8.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 236,980.00 USD | 132.52 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 237,140.00 USD | 160.60 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 243,800.00 USD | 6,670.00 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 251,480.00 USD | 7,680.00 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 251,710.00 USD | 224.56 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 255,280.00 USD | 3,570.00 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 261,470.00 USD | 6,190.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,020,000.00 USD | 1,760,000.00 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,020,000.00 USD | 1,810.00 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,020,000.00 USD | 248.20 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,030,000.00 USD | 5,390.00 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,030,000.00 USD | 285.32 USD | 0.00 USD | `+11.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,030,000.00 USD | 2,570.00 USD | 0.00 USD | `+11.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,030,000.00 USD | 1,240.00 USD | 0.00 USD | `+12.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,030,000.00 USD | 278.06 USD | 0.00 USD | `+12.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,030,000.00 USD | 100.93 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,030,000.00 USD | 309.00 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,030,000.00 USD | 272.12 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,030,000.00 USD | 117.12 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,170,000.00 USD | 140,120.00 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,170,000.00 USD | 530.01 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,170,000.00 USD | 128.23 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,280,000.00 USD | 108,190.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,280,000.00 USD | 550.49 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,290,000.00 USD | 5,810.00 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,290,000.00 USD | 5,570.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,290,000.00 USD | 1,290.00 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,290,000.00 USD | 294.81 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,290,000.00 USD | 123.13 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,290,000.00 USD | 494.98 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,290,000.00 USD | 613.52 USD | 0.00 USD | `+16.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,410,000.00 USD | 117,450.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,410,000.00 USD | 409.76 USD | 0.00 USD | `+16.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,410,000.00 USD | 162.77 USD | 0.00 USD | `+16.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,410,000.00 USD | 959.70 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,410,000.00 USD | 160.18 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,410,000.00 USD | 433.10 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,410,000.00 USD | 628.71 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,420,000.00 USD | 293.61 USD | 0.00 USD | `+18.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,530,000.00 USD | 112,050.00 USD | 0.00 USD | `+18.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,530,000.00 USD | 462.47 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,530,000.00 USD | 2,180.00 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,530,000.00 USD | 273.34 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,530,000.00 USD | 141.31 USD | 0.00 USD | `+19.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,550,000.00 USD | 20,740.00 USD | 0.00 USD | `+19.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,550,000.00 USD | 1,430.00 USD | 0.00 USD | `+20.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,550,000.00 USD | 338.50 USD | 0.00 USD | `+20.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,550,000.00 USD | 769.57 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,550,000.00 USD | 1,230.00 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,560,000.00 USD | 2,450.00 USD | 0.00 USD | `+22.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,560,000.00 USD | 1,250.00 USD | 0.00 USD | `+22.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,560,000.00 USD | 143.67 USD | 0.00 USD | `+22.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,560,000.00 USD | 1,700.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,620,000.00 USD | 63,070.00 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,620,000.00 USD | 304.33 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,620,000.00 USD | 241.65 USD | 0.00 USD | `+24.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,620,000.00 USD | 239.97 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,630,000.00 USD | 2,470.00 USD | 0.00 USD | `+24.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,630,000.00 USD | 3,060.00 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,630,000.00 USD | 351.02 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 2,940,000.00 USD | 310,250.00 USD | 0.00 USD | `+25.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 2,940,000.00 USD | 309.53 USD | 0.00 USD | `+25.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 2,940,000.00 USD | 159.09 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 2,940,000.00 USD | 146.21 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,020,000.00 USD | 79,220.00 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,020,000.00 USD | 933.81 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,020,000.00 USD | 658.86 USD | 0.00 USD | `+27.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,240,000.00 USD | 213,390.00 USD | 0.00 USD | `+27.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,240,000.00 USD | 211.10 USD | 0.00 USD | `+28.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,240,000.00 USD | 1,050.00 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,240,000.00 USD | 812.24 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,240,000.00 USD | 509.71 USD | 0.00 USD | `+29.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,240,000.00 USD | 162.15 USD | 0.00 USD | `+29.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,240,000.00 USD | 187.04 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,240,000.00 USD | 542.12 USD | 0.00 USD | `+30.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,260,000.00 USD | 23,740.00 USD | 0.00 USD | `+30.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,260,000.00 USD | 2,010.00 USD | 0.00 USD | `+30.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,260,000.00 USD | 345.91 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,260,000.00 USD | 104.79 USD | 0.00 USD | `+31.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,270,000.00 USD | 6,870.00 USD | 0.00 USD | `+32.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,270,000.00 USD | 265.62 USD | 0.00 USD | `+32.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,270,000.00 USD | 1,480.00 USD | 0.00 USD | `+33.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,270,000.00 USD | 1,010.00 USD | 0.00 USD | `+33.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,270,000.00 USD | 340.38 USD | 0.00 USD | `+34.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,280,000.00 USD | 903.22 USD | 0.00 USD | `+34.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,280,000.00 USD | 424.15 USD | 0.00 USD | `+34.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,320,000.00 USD | 41,160.00 USD | 0.00 USD | `+34.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,330,000.00 USD | 12,840.00 USD | 0.00 USD | `+35.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,340,000.00 USD | 12,890.00 USD | 0.00 USD | `+36.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,350,000.00 USD | 8,820.00 USD | 0.00 USD | `+36.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,350,000.00 USD | 466.95 USD | 0.00 USD | `+36.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,350,000.00 USD | 613.59 USD | 0.00 USD | `+36.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,350,000.00 USD | 1,420.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,370,000.00 USD | 13,000.00 USD | 0.00 USD | `+37.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,370,000.00 USD | 284.42 USD | 0.00 USD | `+37.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,390,000.00 USD | 22,710.00 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,390,000.00 USD | 640.82 USD | 0.00 USD | `+40.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,400,000.00 USD | 13,400.00 USD | 0.00 USD | `+41.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,410,000.00 USD | 1,580.00 USD | 0.00 USD | `+41.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,410,000.00 USD | 1,580.00 USD | 0.00 USD | `+41.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,420,000.00 USD | 13,490.00 USD | 0.00 USD | `+42.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,430,000.00 USD | 11,580.00 USD | 0.00 USD | `+42.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,440,000.00 USD | 3,610.00 USD | 0.00 USD | `+43.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,440,000.00 USD | 1,540.00 USD | 0.00 USD | `+43.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,440,000.00 USD | 1,500.00 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,450,000.00 USD | 15,000.00 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,460,000.00 USD | 9,030.00 USD | 0.00 USD | `+44.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,460,000.00 USD | 569.84 USD | 0.00 USD | `+46.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,480,000.00 USD | 13,890.00 USD | 0.00 USD | `+46.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,480,000.00 USD | 2,710.00 USD | 0.00 USD | `+47.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,500,000.00 USD | 15,500.00 USD | 0.00 USD | `+47.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,510,000.00 USD | 13,100.00 USD | 0.00 USD | `+47.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,540,000.00 USD | 32,860.00 USD | 0.00 USD | `+48.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,550,000.00 USD | 7,090.00 USD | 0.00 USD | `+48.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,550,000.00 USD | 106.64 USD | 0.00 USD | `+49.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,550,000.00 USD | 1,430.00 USD | 0.00 USD | `+49.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,550,000.00 USD | 2,810.00 USD | 0.00 USD | `+49.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,560,000.00 USD | 8,420.00 USD | 0.00 USD | `+49.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 3,560,000.00 USD | 1,410.00 USD | 0.00 USD | `+50.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,560,000.00 USD | 431.38 USD | 0.00 USD | `+51.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,570,000.00 USD | 1,390.00 USD | 0.00 USD | `+51.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,580,000.00 USD | 14,390.00 USD | 0.00 USD | `+51.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,590,000.00 USD | 7,000.00 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,590,000.00 USD | 434.98 USD | 0.00 USD | `+52.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,600,000.00 USD | 14,490.00 USD | 0.00 USD | `+53.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,600,000.00 USD | 1,370.00 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 3,600,000.00 USD | 1,350.00 USD | 0.00 USD | `+54.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,610,000.00 USD | 1,340.00 USD | 0.00 USD | `+54.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,610,000.00 USD | 1,300.00 USD | 0.00 USD | `+55.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,610,000.00 USD | 342.08 USD | 0.00 USD | `+55.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 3,610,000.00 USD | 1,330.00 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,610,000.00 USD | 1,320.00 USD | 0.00 USD | `+57.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,610,000.00 USD | 1,310.00 USD | 0.00 USD | `+57.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,630,000.00 USD | 14,890.00 USD | 0.00 USD | `+57.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,640,000.00 USD | 9,580.00 USD | 0.00 USD | `+57.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,650,000.00 USD | 14,980.00 USD | 0.00 USD | `+58.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,660,000.00 USD | 5,110.00 USD | 0.00 USD | `+58.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,660,000.00 USD | 1,270.00 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,660,000.00 USD | 1,260.00 USD | 0.00 USD | `+60.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 3,660,000.00 USD | 1,980.00 USD | 0.00 USD | `+62.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 3,660,000.00 USD | 574.53 USD | 0.00 USD | `+68.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 3,660,000.00 USD | 391.32 USD | 0.00 USD | `+68.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 3,660,000.00 USD | 1,160.00 USD | 0.00 USD | `+70.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,660,000.00 USD | 1,140.00 USD | 0.00 USD | `+72.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,670,000.00 USD | 1,970.00 USD | 0.00 USD | `+73.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 3,670,000.00 USD | 281.45 USD | 0.00 USD | `+75.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 3,670,000.00 USD | 958.84 USD | 0.00 USD | `+78.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 3,670,000.00 USD | 3,550.00 USD | 0.00 USD | `+79.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 3,670,000.00 USD | 1,070.00 USD | 0.00 USD | `+84.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 3,670,000.00 USD | 1,710.00 USD | 0.00 USD | `+86.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,690,000.00 USD | 13,670.00 USD | 0.00 USD | `+89.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,690,000.00 USD | 295.46 USD | 0.00 USD | `+90.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,690,000.00 USD | 328.97 USD | 0.00 USD | `+92.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,690,000.00 USD | 394.87 USD | 0.00 USD | `+92.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,700,000.00 USD | 10,950.00 USD | 0.00 USD | `+95.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,740,000.00 USD | 41,990.00 USD | 0.00 USD | `+95.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.86` | 3,740,000.00 USD | 149.08 USD | 0.00 USD | `+96.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.87` | 3,760,000.00 USD | 17,290.00 USD | 0.00 USD | `+97.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 3,760,000.00 USD | 2,340.00 USD | 0.00 USD | `+98.54%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8110` | 33,140,000.00 USD | 0.00 USD | 33,140,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD |
| `7D` | `0.8130` | 33,030,000.00 USD | 0.00 USD | 33,030,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD |
| `7D` | `0.8150` | 32,960,000.00 USD | 0.00 USD | 32,960,000.00 USD | 135,770.00 USD | 50,280.00 USD | 124,810.00 USD |
| `7D` | `0.8170` | 32,650,000.00 USD | 0.00 USD | 32,650,000.00 USD | 91,050.00 USD | 23,590.00 USD | 78,040.00 USD |
| `7D` | `0.8190` | 32,460,000.00 USD | 0.00 USD | 32,460,000.00 USD | 195,400.00 USD | 52,010.00 USD | 47,010.00 USD |
| `7D` | `0.8210` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 138,580.00 USD | 47,520.00 USD | 119,250.00 USD |
| `7D` | `0.8230` | 31,860,000.00 USD | 0.00 USD | 31,860,000.00 USD | 37,880.00 USD | 24,290.00 USD | 64,410.00 USD |
| `7D` | `0.8250` | 31,730,000.00 USD | 0.00 USD | 31,730,000.00 USD | 187,510.00 USD | 27,530.00 USD | 126,000.00 USD |
| `7D` | `0.8270` | 31,390,000.00 USD | 0.00 USD | 31,390,000.00 USD | 144,410.00 USD | 51,050.00 USD | 63,610.00 USD |
| `7D` | `0.8290` | 31,130,000.00 USD | 0.00 USD | 31,130,000.00 USD | 89,470.00 USD | 39,850.00 USD | 82,590.00 USD |
| `7D` | `0.8310` | 30,920,000.00 USD | 0.00 USD | 30,920,000.00 USD | 34,030.00 USD | 30,800.00 USD | 22,830.00 USD |
| `7D` | `0.8330` | 30,830,000.00 USD | 0.00 USD | 30,830,000.00 USD | 150,740.00 USD | 85,780.00 USD | 198,210.00 USD |
| `7D` | `0.8350` | 30,390,000.00 USD | 0.00 USD | 30,390,000.00 USD | 74,030.00 USD | 14,320.00 USD | 83,830.00 USD |
| `7D` | `0.8370` | 30,220,000.00 USD | 0.00 USD | 30,220,000.00 USD | 146,890.00 USD | 48,060.00 USD | 102,790.00 USD |
| `7D` | `0.8390` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 24,790.00 USD | 51,510.00 USD | 77,090.00 USD |
| `7D` | `0.8410` | 29,770,000.00 USD | 0.00 USD | 29,770,000.00 USD | 55,190.00 USD | 40,110.00 USD | 27,780.00 USD |
| `7D` | `0.8430` | 29,650,000.00 USD | 0.00 USD | 29,650,000.00 USD | 81,850.00 USD | 49,990.00 USD | 30,430.00 USD |
| `7D` | `0.8450` | 29,490,000.00 USD | 0.00 USD | 29,490,000.00 USD | 43,800.00 USD | 55,690.00 USD | 49,310.00 USD |
| `1D` | `0.8460` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 28,740.00 USD | 30,760.00 USD | 46,180.00 USD |
| `7D` | `0.8470` | 29,340,000.00 USD | 0.00 USD | 29,340,000.00 USD | 23,930.00 USD | 4,350.00 USD | 32,430.00 USD |
| `1D` | `0.8480` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 24,470.00 USD | 17,830.00 USD | 27,320.00 USD |
| `7D` | `0.8490` | 29,280,000.00 USD | 0.00 USD | 29,280,000.00 USD | 45,210.00 USD | 16,670.00 USD | 46,020.00 USD |
| `1D` | `0.8500` | 13,190,000.00 USD | 0.00 USD | 13,190,000.00 USD | 53,880.00 USD | 7,390.00 USD | 15,250.00 USD |
| `7D` | `0.8510` | 29,170,000.00 USD | 0.00 USD | 29,170,000.00 USD | 95,990.00 USD | 42,650.00 USD | 42,410.00 USD |
| `1D` | `0.8520` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 30,310.00 USD | 27,790.00 USD | 16,880.00 USD |
| `7D` | `0.8530` | 28,990,000.00 USD | 0.00 USD | 28,990,000.00 USD | 30,570.00 USD | 50,890.00 USD | 29,460.00 USD |
| `1D` | `0.8540` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 20,080.00 USD | 11,230.00 USD | 42,190.00 USD |
| `7D` | `0.8550` | 28,880,000.00 USD | 0.00 USD | 28,880,000.00 USD | 78,320.00 USD | 26,490.00 USD | 3,080.00 USD |
| `1D` | `0.8560` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 27,930.00 USD | 22,280.00 USD | 25,540.00 USD |
| `7D` | `0.8570` | 28,770,000.00 USD | 0.00 USD | 28,770,000.00 USD | 99,680.00 USD | 45,070.00 USD | 5,400.00 USD |
| `1D` | `0.8580` | 12,890,000.00 USD | 0.00 USD | 12,890,000.00 USD | 56,290.00 USD | 13,830.00 USD | 14,900.00 USD |
| `7D` | `0.8590` | 28,620,000.00 USD | 0.00 USD | 28,620,000.00 USD | 51,400.00 USD | 22,020.00 USD | 18,570.00 USD |
| `1D` | `0.8600` | 12,810,000.00 USD | 0.00 USD | 12,810,000.00 USD | 17,410.00 USD | 6,920.00 USD | 14,890.00 USD |
| `7D` | `0.8610` | 28,530,000.00 USD | 0.00 USD | 28,530,000.00 USD | 36,870.00 USD | 71,110.00 USD | 30,720.00 USD |
| `1D` | `0.8620` | 12,770,000.00 USD | 0.00 USD | 12,770,000.00 USD | 6,110.00 USD | 5,870.00 USD | 673.24 USD |
| `7D` | `0.8630` | 28,390,000.00 USD | 0.00 USD | 28,390,000.00 USD | 30,710.00 USD | 13,800.00 USD | 48,380.00 USD |
| `1D` | `0.8640` | 12,760,000.00 USD | 0.00 USD | 12,760,000.00 USD | 53,230.00 USD | 24,840.00 USD | 60,280.00 USD |
| `7D` | `0.8650` | 28,300,000.00 USD | 0.00 USD | 28,300,000.00 USD | 235,900.00 USD | 43,890.00 USD | 100,880.00 USD |
| `1D` | `0.8660` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 139,410.00 USD | 1,740.00 USD | 13,990.00 USD |
| `7D` | `0.8670` | 27,910,000.00 USD | 0.00 USD | 27,910,000.00 USD | 159,120.00 USD | 71,510.00 USD | 58,910.00 USD |
| `1D` | `0.8680` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 103,830.00 USD | 60,300.00 USD | 33,280.00 USD |
| `7D` | `0.8690` | 27,630,000.00 USD | 0.00 USD | 27,630,000.00 USD | 182,190.00 USD | 79,290.00 USD | 193,930.00 USD |
| `1D` | `0.8700` | 12,270,000.00 USD | 0.00 USD | 12,270,000.00 USD | 110,320.00 USD | 89,890.00 USD | 226,640.00 USD |
| `7D` | `0.8710` | 27,170,000.00 USD | 0.00 USD | 27,170,000.00 USD | 604,760.00 USD | 167,740.00 USD | 362,510.00 USD |
| `1D` | `0.8720` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 211,520.00 USD | 63,380.00 USD | 201,220.00 USD |
| `7D` | `0.8730` | 26,030,000.00 USD | 0.00 USD | 26,030,000.00 USD | 333,320.00 USD | 199,690.00 USD | 215,150.00 USD |
| `1D` | `0.8740` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 43,750.00 USD | 20,450.00 USD | 21,770.00 USD |
| `7D` | `0.8750` | 25,290,000.00 USD | 0.00 USD | 25,290,000.00 USD | 643,630.00 USD | 230,460.00 USD | 324,670.00 USD |
| `1D` | `0.8760` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 77,040.00 USD | 73,640.00 USD | 139,470.00 USD |
| `7D` | `0.8770` | 24,090,000.00 USD | 0.00 USD | 24,090,000.00 USD | 399,330.00 USD | 194,000.00 USD | 420,350.00 USD |
| `1D` | `0.8780` | 10,990,000.00 USD | 0.00 USD | 10,990,000.00 USD | 64,740.00 USD | 48,440.00 USD | 31,980.00 USD |
| `7D` | `0.8790` | 23,070,000.00 USD | 0.00 USD | 23,070,000.00 USD | 312,210.00 USD | 124,520.00 USD | 220,970.00 USD |
| `1D` | `0.8800` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 14,150.00 USD | 11,490.00 USD | 41,550.00 USD |
| `7D` | `0.8810` | 22,420,000.00 USD | 0.00 USD | 22,420,000.00 USD | 641,660.00 USD | 159,780.00 USD | 487,390.00 USD |
| `1D` | `0.8820` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 110,430.00 USD | 63,180.00 USD | 145,990.00 USD |
| `7D` | `0.8830` | 21,130,000.00 USD | 0.00 USD | 21,130,000.00 USD | 783,040.00 USD | 270,900.00 USD | 529,050.00 USD |
| `1D` | `0.8840` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 303,250.00 USD | 69,500.00 USD | 158,020.00 USD |
| `7D` | `0.8850` | 19,540,000.00 USD | 0.00 USD | 19,540,000.00 USD | 519,370.00 USD | 263,660.00 USD | 258,480.00 USD |
| `1D` | `0.8860` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 285,170.00 USD | 128,260.00 USD | 88,690.00 USD |
| `7D` | `0.8870` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 649,180.00 USD | 279,830.00 USD | 511,220.00 USD |
| `1D` | `0.8880` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 332,020.00 USD | 224,400.00 USD | 540,830.00 USD |
| `7D` | `0.8890` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 1,550,000.00 USD | 530,540.00 USD | 1,160,000.00 USD |
| `1D` | `0.8900` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 524,630.00 USD | 174,460.00 USD | 573,620.00 USD |
| `7D` | `0.8910` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 818,970.00 USD | 471,140.00 USD | 681,670.00 USD |
| `1D` | `0.8920` | 7,050,000.00 USD | 0.00 USD | 7,050,000.00 USD | 235,610.00 USD | 49,510.00 USD | 115,390.00 USD |
| `7D` | `0.8930` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 1,790,000.00 USD | 646,070.00 USD | 1,040,000.00 USD |
| `1D` | `0.8940` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 167,880.00 USD | 127,050.00 USD | 266,070.00 USD |
| `7D` | `0.8950` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 771,020.00 USD | 443,450.00 USD | 798,480.00 USD |
| `1D` | `0.8960` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 130,690.00 USD | 139,190.00 USD | 168,760.00 USD |
| `7D` | `0.8970` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 673,010.00 USD | 276,920.00 USD | 492,850.00 USD |
| `1D` | `0.8980` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 114,240.00 USD | 50,830.00 USD | 76,450.00 USD |
| `7D` | `0.8990` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 322,820.00 USD | 147,390.00 USD | 897.80 USD |
| `1D` | `0.9000` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 53,800.00 USD | 24,210.00 USD | 44,070.00 USD |
| `7D` | `0.9010` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 130,380.00 USD | 15,640.00 USD | 6,170.00 USD |
| `1D` | `0.9020` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 49,680.00 USD | 79,010.00 USD | 192,580.00 USD |
| `7D` | `0.9030` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 5,880.00 USD | 50,720.00 USD | 119,280.00 USD |
| `1D` | `0.9040` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 91,760.00 USD | 76,800.00 USD | 73,180.00 USD |
| `7D` | `0.9050` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 70,190.00 USD | 0.00 USD | 46,500.00 USD |
| `1D` | `0.9060` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 195,270.00 USD | 6,440.00 USD | 58,230.00 USD |
| `7D` | `0.9070` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 341,080.00 USD | 19,890.00 USD | 127,760.00 USD |
| `1D` | `0.9080` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 241,380.00 USD | 116,800.00 USD | 207,750.00 USD |
| `7D` | `0.9090` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 53,970.00 USD | 0.00 USD | 128,660.00 USD |
| `1D` | `0.9100` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 174,550.00 USD | 32,520.00 USD | 153,690.00 USD |
| `7D` | `0.9110` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 212,760.00 USD | 106,160.00 USD | 35,810.00 USD |
| `1D` | `0.9120` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 211,640.00 USD | 33,420.00 USD | 172,440.00 USD |
| `7D` | `0.9130` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 80,230.00 USD | 95,530.00 USD | 105,460.00 USD |
| `1D` | `0.9140` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 134,740.00 USD | 70,610.00 USD | 76,700.00 USD |
| `7D` | `0.9150` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 111,690.00 USD | 26,360.00 USD | 38,020.00 USD |
| `1D` | `0.9160` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 19,210.00 USD | 13,400.00 USD | 10,460.00 USD |
| `7D` | `0.9170` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 123,530.00 USD | 0.00 USD | 37,740.00 USD |
| `1D` | `0.9180` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 154,870.00 USD | 9,020.00 USD | 46,150.00 USD |
| `7D` | `0.9190` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 257,890.00 USD | 23,790.00 USD | 0.00 USD |
| `1D` | `0.9200` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD |
| `7D` | `0.9210` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD |
| `1D` | `0.9220` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 39,420.00 USD | 68,320.00 USD |
| `7D` | `0.9230` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 64,540.00 USD | 286,870.00 USD |
| `1D` | `0.9240` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 90,500.00 USD | 40,590.00 USD | 82,110.00 USD |
| `7D` | `0.9250` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 41,710.00 USD | 0.00 USD |
| `1D` | `0.9260` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 111,230.00 USD | 28,360.00 USD | 0.00 USD |
| `7D` | `0.9270` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 209,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9280` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 31,930.00 USD | 80,990.00 USD | 0.00 USD |
| `7D` | `0.9290` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 78,940.00 USD | 0.00 USD |
| `1D` | `0.9300` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 82,700.00 USD | 110,920.00 USD | 166,780.00 USD |
| `7D` | `0.9310` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 177,720.00 USD | 29,170.00 USD | 0.00 USD |
| `1D` | `0.9320` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 189,840.00 USD | 54,470.00 USD | 66,000.00 USD |
| `1D` | `0.9340` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 198,250.00 USD | 74,630.00 USD | 51,380.00 USD |
| `7D` | `0.9350` | 975,070.00 USD | 0.00 USD | 975,070.00 USD | 50,160.00 USD | 52,710.00 USD | 76,050.00 USD |
| `1D` | `0.9360` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 81,170.00 USD | 39,480.00 USD | 113,190.00 USD |
| `7D` | `0.9370` | 796,150.00 USD | 0.00 USD | 796,150.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD |
| `1D` | `0.9380` | 777,990.00 USD | 0.00 USD | 777,990.00 USD | 246,090.00 USD | 118,850.00 USD | 293,510.00 USD |
| `7D` | `0.9390` | 502,440.00 USD | 0.00 USD | 502,440.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD |
| `1D` | `0.9400` | 119,550.00 USD | 0.00 USD | 119,550.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD |
| `1D` | `0.9410` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9410` | 123,000.00 USD | 0.00 USD | 123,000.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9420` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9430` | 62,100.00 USD | 62,100.00 USD | 0.00 USD | 0.00 USD | 62,100.00 USD | 0.00 USD |
| `1D` | `0.9440` | 110,210.00 USD | 110,210.00 USD | 0.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD |
| `7D` | `0.9450` | 396,730.00 USD | 396,730.00 USD | 0.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD |
| `1D` | `0.9460` | 380,390.00 USD | 380,390.00 USD | 0.00 USD | 0.00 USD | 28,980.00 USD | 241,190.00 USD |
| `7D` | `0.9470` | 607,360.00 USD | 607,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `7D` | `0.9490` | 643,170.00 USD | 643,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35,810.00 USD |
| `1D` | `0.9500` | 381,820.00 USD | 381,820.00 USD | 0.00 USD | 1,330.00 USD | 0.00 USD | 107.82 USD |
| `7D` | `0.9510` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 62,510.00 USD | 639,730.00 USD |
| `1D` | `0.9520` | 435,880.00 USD | 435,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,060.00 USD |
| `7D` | `0.9530` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD |
| `1D` | `0.9540` | 473,250.00 USD | 473,250.00 USD | 0.00 USD | 7,240.00 USD | 30,120.00 USD | 0.00 USD |
| `7D` | `0.9550` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 71,910.00 USD | 1,290.00 USD | 288.96 USD |
| `1D` | `0.9560` | 506,920.00 USD | 506,920.00 USD | 0.00 USD | 0.00 USD | 33,360.00 USD | 303.02 USD |
| `7D` | `0.9570` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 463,830.00 USD | 2,240.00 USD | 511.50 USD |
| `1D` | `0.9580` | 550,740.00 USD | 550,740.00 USD | 0.00 USD | 689.00 USD | 43,140.00 USD | 0.00 USD |
| `7D` | `0.9590` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 562,050.00 USD | 1,040.00 USD | 289.76 USD |
| `1D` | `0.9600` | 737,500.00 USD | 737,500.00 USD | 0.00 USD | 77,250.00 USD | 65,470.00 USD | 44,040.00 USD |
| `7D` | `0.9610` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 647,060.00 USD | 176,650.00 USD | 421,920.00 USD |
| `1D` | `0.9620` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 338,260.00 USD | 118,080.00 USD | 277,230.00 USD |
| `7D` | `0.9630` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 552,290.00 USD | 301,610.00 USD | 615,910.00 USD |
| `1D` | `0.9640` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 332,940.00 USD | 127,440.00 USD | 278,810.00 USD |
| `7D` | `0.9650` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 857,470.00 USD | 301,210.00 USD | 412,280.00 USD |
| `1D` | `0.9660` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 273,420.00 USD | 130,360.00 USD | 133,670.00 USD |
| `7D` | `0.9670` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 916,920.00 USD | 487,590.00 USD | 705,590.00 USD |
| `1D` | `0.9680` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 303,010.00 USD | 116,010.00 USD | 350,300.00 USD |
| `7D` | `0.9690` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 596,350.00 USD | 343,680.00 USD | 389,510.00 USD |
| `1D` | `0.9700` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 246,830.00 USD | 142,190.00 USD | 184,780.00 USD |
| `7D` | `0.9710` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 645,500.00 USD | 305,860.00 USD | 144,130.00 USD |
| `1D` | `0.9720` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 320,980.00 USD | 108,180.00 USD | 99,440.00 USD |
| `7D` | `0.9730` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 456,990.00 USD | 160,420.00 USD | 146,260.00 USD |
| `1D` | `0.9740` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 169,060.00 USD | 34,110.00 USD | 53,250.00 USD |
| `7D` | `0.9750` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 201,510.00 USD | 293,590.00 USD | 193,410.00 USD |
| `1D` | `0.9760` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 40,320.00 USD | 41,480.00 USD | 88,080.00 USD |
| `7D` | `0.9770` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 329,170.00 USD | 211,000.00 USD | 499,960.00 USD |
| `1D` | `0.9780` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 110,140.00 USD | 54,830.00 USD | 189,870.00 USD |
| `7D` | `0.9790` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 409,890.00 USD | 83,100.00 USD | 158,290.00 USD |
| `1D` | `0.9800` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 66,270.00 USD | 66,440.00 USD | 90,660.00 USD |
| `7D` | `0.9810` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 212,850.00 USD | 83,040.00 USD | 169,310.00 USD |
| `1D` | `0.9820` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 165,210.00 USD | 28,940.00 USD | 53,530.00 USD |
| `7D` | `0.9830` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 260,850.00 USD | 99,420.00 USD | 199,120.00 USD |
| `1D` | `0.9840` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 74,270.00 USD | 67,350.00 USD | 22,570.00 USD |
| `7D` | `0.9850` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD |
| `1D` | `0.9860` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 131,110.00 USD | 61,330.00 USD | 136,890.00 USD |
| `7D` | `0.9870` | 16,350,000.00 USD | 16,350,000.00 USD | 0.00 USD | 248,980.00 USD | 191,820.00 USD | 58,100.00 USD |
| `1D` | `0.9880` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 85,900.00 USD | 34,510.00 USD | 70,930.00 USD |
| `7D` | `0.9890` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 18,790.00 USD |
| `1D` | `0.9900` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 146,250.00 USD | 50,130.00 USD | 77,350.00 USD |
| `7D` | `0.9910` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD |
| `1D` | `0.9920` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 143,390.00 USD | 45,570.00 USD | 21,440.00 USD |
| `7D` | `0.9930` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 73,350.00 USD |
| `1D` | `0.9940` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 60,490.00 USD | 36,310.00 USD | 61,950.00 USD |
| `7D` | `0.9950` | 17,690,000.00 USD | 17,690,000.00 USD | 0.00 USD | 48,120.00 USD | 137,230.00 USD | 130,850.00 USD |
| `1D` | `0.9960` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 6,800.00 USD | 10,960.00 USD | 22,040.00 USD |
| `7D` | `0.9970` | 18,340,000.00 USD | 18,340,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD |
| `1D` | `0.9980` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 139,760.00 USD | 32,100.00 USD | 142,090.00 USD |
| `7D` | `0.9990` | 18,620,000.00 USD | 18,620,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD |
| `1D` | `1.00` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 19,510.00 USD | 17,530.00 USD | 6,940.00 USD |
| `7D` | `1.00` | 19,070,000.00 USD | 19,070,000.00 USD | 0.00 USD | 202,970.00 USD | 57,170.00 USD | 185,100.00 USD |
| `1D` | `1.00` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 12,840.00 USD | 18,430.00 USD | 18,490.00 USD |
| `7D` | `1.00` | 19,650,000.00 USD | 19,650,000.00 USD | 0.00 USD | 316,600.00 USD | 52,200.00 USD | 216,090.00 USD |
| `1D` | `1.00` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 17,620.00 USD | 13,050.00 USD | 22,470.00 USD |
| `7D` | `1.00` | 19,850,000.00 USD | 19,850,000.00 USD | 0.00 USD | 96,930.00 USD | 29,470.00 USD | 65,240.00 USD |
| `1D` | `1.01` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 9,900.00 USD | 14,020.00 USD | 9,330.00 USD |
| `7D` | `1.01` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 283,350.00 USD | 15,900.00 USD | 212,150.00 USD |
| `1D` | `1.01` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 19,520.00 USD | 9,720.00 USD | 12,370.00 USD |
| `7D` | `1.01` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 247,480.00 USD | 105,290.00 USD | 247,750.00 USD |
| `1D` | `1.01` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 13,140.00 USD | 5,570.00 USD | 11,240.00 USD |
| `7D` | `1.01` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 457,740.00 USD | 174,650.00 USD | 319,400.00 USD |
| `1D` | `1.01` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 21,660.00 USD | 15,860.00 USD | 33,960.00 USD |
| `7D` | `1.01` | 22,900,000.00 USD | 22,900,000.00 USD | 0.00 USD | 342,220.00 USD | 305,010.00 USD | 344,360.00 USD |
| `1D` | `1.01` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 16,320.00 USD | 11,680.00 USD | 27,220.00 USD |
| `7D` | `1.01` | 23,440,000.00 USD | 23,440,000.00 USD | 0.00 USD | 325,510.00 USD | 91,280.00 USD | 124,520.00 USD |
| `1D` | `1.02` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 23,240.00 USD | 15,330.00 USD | 19,840.00 USD |
| `7D` | `1.02` | 24,280,000.00 USD | 24,280,000.00 USD | 0.00 USD | 383,690.00 USD | 97,830.00 USD | 360,110.00 USD |
| `1D` | `1.02` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 26,650.00 USD | 4,040.00 USD | 4,170.00 USD |
| `7D` | `1.02` | 25,150,000.00 USD | 25,150,000.00 USD | 0.00 USD | 303,920.00 USD | 89,280.00 USD | 469,230.00 USD |
| `1D` | `1.02` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 36,470.00 USD | 16,330.00 USD | 65,570.00 USD |
| `7D` | `1.02` | 25,640,000.00 USD | 25,640,000.00 USD | 0.00 USD | 167,390.00 USD | 64,370.00 USD | 260,150.00 USD |
| `1D` | `1.02` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 55,940.00 USD | 4,130.00 USD | 22,580.00 USD |
| `7D` | `1.02` | 26,000,000.00 USD | 26,000,000.00 USD | 0.00 USD | 185,100.00 USD | 50,190.00 USD | 123,500.00 USD |
| `1D` | `1.02` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 29,960.00 USD | 7,480.00 USD | 21,700.00 USD |
| `7D` | `1.02` | 26,260,000.00 USD | 26,260,000.00 USD | 0.00 USD | 112,970.00 USD | 54,210.00 USD | 94,470.00 USD |
| `1D` | `1.03` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 16,450.00 USD | 12,750.00 USD | 15,620.00 USD |
| `7D` | `1.03` | 26,510,000.00 USD | 26,510,000.00 USD | 0.00 USD | 106,360.00 USD | 35,230.00 USD | 110,930.00 USD |
| `1D` | `1.03` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | 4,950.00 USD |
| `7D` | `1.03` | 26,720,000.00 USD | 26,720,000.00 USD | 0.00 USD | 87,950.00 USD | 57,010.00 USD | 67,150.00 USD |
| `1D` | `1.03` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 4,130.00 USD | 10,190.00 USD | 10,170.00 USD |
| `7D` | `1.03` | 27,160,000.00 USD | 27,160,000.00 USD | 0.00 USD | 198,340.00 USD | 79,470.00 USD | 157,430.00 USD |
| `1D` | `1.03` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 21,900.00 USD | 11,130.00 USD | 5,260.00 USD |
| `7D` | `1.03` | 27,610,000.00 USD | 27,610,000.00 USD | 0.00 USD | 136,400.00 USD | 149,600.00 USD | 163,030.00 USD |
| `1D` | `1.03` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 16,600.00 USD | 19,650.00 USD | 46,170.00 USD |
| `7D` | `1.03` | 27,800,000.00 USD | 27,800,000.00 USD | 0.00 USD | 113,490.00 USD | 13,570.00 USD | 63,310.00 USD |
| `1D` | `1.04` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 19,040.00 USD | 16,530.00 USD | 27,320.00 USD |
| `7D` | `1.04` | 28,200,000.00 USD | 28,200,000.00 USD | 0.00 USD | 176,930.00 USD | 41,660.00 USD | 181,120.00 USD |
| `1D` | `1.04` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 51,250.00 USD | 7,020.00 USD | 15,030.00 USD |
| `7D` | `1.04` | 28,510,000.00 USD | 28,510,000.00 USD | 0.00 USD | 114,060.00 USD | 21,690.00 USD | 175,760.00 USD |
| `1D` | `1.04` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 8,210.00 USD | 7,840.00 USD | 8,090.00 USD |
| `7D` | `1.04` | 28,740,000.00 USD | 28,740,000.00 USD | 0.00 USD | 105,050.00 USD | 55,100.00 USD | 72,870.00 USD |
| `1D` | `1.04` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 21,580.00 USD | 18,300.00 USD | 8,780.00 USD |
| `7D` | `1.04` | 28,840,000.00 USD | 28,840,000.00 USD | 0.00 USD | 20,680.00 USD | 49,420.00 USD | 24,820.00 USD |
| `1D` | `1.04` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 19,660.00 USD | 8,720.00 USD | 41,920.00 USD |
| `7D` | `1.04` | 28,930,000.00 USD | 28,930,000.00 USD | 0.00 USD | 69,360.00 USD | 17,730.00 USD | 1,560.00 USD |
| `1D` | `1.05` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 25,330.00 USD | 17,080.00 USD | 25,440.00 USD |
| `7D` | `1.05` | 29,040,000.00 USD | 29,040,000.00 USD | 0.00 USD | 79,950.00 USD | 31,290.00 USD | 294.86 USD |
| `1D` | `1.05` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 53,350.00 USD | 10,090.00 USD | 14,740.00 USD |
| `7D` | `1.05` | 29,110,000.00 USD | 29,110,000.00 USD | 0.00 USD | 38,030.00 USD | 13,720.00 USD | 17,370.00 USD |
| `1D` | `1.05` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 12,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.05` | 29,130,000.00 USD | 29,130,000.00 USD | 0.00 USD | 23,320.00 USD | 0.00 USD | 538.06 USD |
| `1D` | `1.05` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 0.00 USD | 142.30 USD | 14,720.00 USD |
| `7D` | `1.05` | 29,210,000.00 USD | 29,210,000.00 USD | 0.00 USD | 8,370.00 USD | 47,690.00 USD | 28,430.00 USD |
| `1D` | `1.05` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 303.15 USD | 202.65 USD | 0.00 USD |
| `7D` | `1.05` | 29,270,000.00 USD | 29,270,000.00 USD | 0.00 USD | 3,770.00 USD | 5,360.00 USD | 46,120.00 USD |
| `1D` | `1.06` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 11,980.00 USD | 4,220.00 USD | 5,400.00 USD |
| `7D` | `1.06` | 29,280,000.00 USD | 29,280,000.00 USD | 0.00 USD | 6,580.00 USD | 3,950.00 USD | 197.80 USD |
| `7D` | `1.06` | 29,280,000.00 USD | 29,280,000.00 USD | 0.00 USD | 1,110.00 USD | 194.87 USD | 59.76 USD |
| `7D` | `1.06` | 29,320,000.00 USD | 29,320,000.00 USD | 0.00 USD | 17,530.00 USD | 3,870.00 USD | 12,060.00 USD |
| `7D` | `1.06` | 29,330,000.00 USD | 29,330,000.00 USD | 0.00 USD | 10,210.00 USD | 0.00 USD | 388.18 USD |
| `7D` | `1.06` | 29,330,000.00 USD | 29,330,000.00 USD | 0.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `627.18M` | Total OI Tokens: `666,151,583.1 SUI`
  * 1h OI Change: `-1.36%` | 4h OI Change: `-0.08%` | 24h OI Change: `+0.74%`
  * Exchange Breakdown: Binance=`121.50M` | Bybit=`83.73M` | OKX=`34.43M` | Hyperliquid=`32.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `22.81K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `31.12%` | `68.88%` | `0.45` | 6,400,000.00 USD |
| `15M` | `Binance` | `26.36%` | `73.64%` | `0.36` | 2,360,000.00 USD |
| `15M` | `OKX` | `29.02%` | `70.98%` | `0.41` | 255,220.00 USD |
| `15M` | `Bybit` | `28.18%` | `71.82%` | `0.39` | 245,890.00 USD |
| `15M` | `KuCoin` | `51.45%` | `48.55%` | `1.06` | 19,280.00 USD |
| `15M` | `Gate` | `41.35%` | `58.65%` | `0.71` | 117,860.00 USD |
| `15M` | `Bitget` | `15.38%` | `84.62%` | `0.18` | 217,450.00 USD |
| `15M` | `BingX` | `47.63%` | `52.37%` | `0.91` | 998,110.00 USD |
| `15M` | `MEXC` | `72.14%` | `27.86%` | `2.59` | 149,770.00 USD |
| `15M` | `Bitunix` | `22.71%` | `77.29%` | `0.29` | 328,800.00 USD |
| `15M` | `Hyperliquid` | `16.38%` | `83.62%` | `0.20` | 29,650.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `37.66%` | `62.34%` | `0.60` | 1,220,000.00 USD |
| `15M` | `Crypto.com` | `42.27%` | `57.73%` | `0.73` | 23.21 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 423,020.00 USD |
| `15M` | `HTX` | `47.32%` | `52.68%` | `0.90` | 830.87 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `55.84%` | `44.16%` | `1.26` | 19,860.00 USD |
| `15M` | `Aster` | `0.07%` | `99.93%` | `0.00` | 12,170.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `15.27%` | `84.73%` | `0.18` | 2,090.00 USD |
| `15M` | `Whale Positions` | `26.36%` | `73.64%` | `0.36` | 2,360,000.00 USD |
| `15M` | `Global Accounts` | `31.12%` | `68.88%` | `0.45` | 6,400,000.00 USD |
| `1H` | `SUI` | `42.42%` | `57.58%` | `0.74` | 26,850,000.00 USD |
| `1H` | `Binance` | `41.96%` | `58.04%` | `0.72` | 7,980,000.00 USD |
| `1H` | `OKX` | `39.29%` | `60.71%` | `0.65` | 2,210,000.00 USD |
| `1H` | `Bybit` | `41.3%` | `58.7%` | `0.70` | 1,690,000.00 USD |
| `1H` | `KuCoin` | `45.1%` | `54.9%` | `0.82` | 278,910.00 USD |
| `1H` | `Gate` | `49.86%` | `50.14%` | `0.99` | 413,010.00 USD |
| `1H` | `Bitget` | `36.12%` | `63.88%` | `0.57` | 797,360.00 USD |
| `1H` | `BingX` | `38.22%` | `61.78%` | `0.62` | 887,760.00 USD |
| `1H` | `MEXC` | `48.5%` | `51.5%` | `0.94` | 9,500,000.00 USD |
| `1H` | `Bitunix` | `32.55%` | `67.45%` | `0.48` | 811,690.00 USD |
| `1H` | `Hyperliquid` | `43.21%` | `56.79%` | `0.76` | 757,740.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.72%` | `54.28%` | `0.84` | 553,750.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.25%` | `99.75%` | `0.00` | 609,670.00 USD |
| `1H` | `HTX` | `87.87%` | `12.13%` | `7.24` | 20,010.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.79%` | `76.21%` | `0.31` | 163,950.00 USD |
| `1H` | `Aster` | `1.67%` | `98.33%` | `0.02` | 178,160.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `86.71%` | `13.29%` | `6.52` | 9,040.00 USD |
| `1H` | `Whale Positions` | `41.96%` | `58.04%` | `0.72` | 7,980,000.00 USD |
| `1H` | `Global Accounts` | `42.42%` | `57.58%` | `0.74` | 26,850,000.00 USD |
| `4H` | `SUI` | `45.51%` | `54.49%` | `0.84` | 88,550,000.00 USD |
| `4H` | `Binance` | `46.85%` | `53.15%` | `0.88` | 30,760,000.00 USD |
| `4H` | `OKX` | `51.06%` | `48.94%` | `1.04` | 5,350,000.00 USD |
| `4H` | `Bybit` | `47.97%` | `52.03%` | `0.92` | 4,500,000.00 USD |
| `4H` | `KuCoin` | `55.97%` | `44.03%` | `1.27` | 719,750.00 USD |
| `4H` | `Gate` | `45.14%` | `54.86%` | `0.82` | 1,930,000.00 USD |
| `4H` | `Bitget` | `47%` | `53%` | `0.89` | 1,760,000.00 USD |
| `4H` | `BingX` | `46.85%` | `53.15%` | `0.88` | 13,790,000.00 USD |
| `4H` | `MEXC` | `44.3%` | `55.7%` | `0.80` | 5,010,000.00 USD |
| `4H` | `Bitunix` | `55.21%` | `44.79%` | `1.23` | 3,150,000.00 USD |
| `4H` | `Hyperliquid` | `61.33%` | `38.67%` | `1.59` | 1,110,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.57%` | `49.43%` | `1.02` | 14,870,000.00 USD |
| `4H` | `Crypto.com` | `98.84%` | `1.16%` | `85.21` | 9,080.00 USD |
| `4H` | `WhiteBIT` | `0.32%` | `99.68%` | `0.00` | 5,090,000.00 USD |
| `4H` | `HTX` | `26.7%` | `73.3%` | `0.36` | 25,760.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.6%` | `50.4%` | `0.98` | 269,140.00 USD |
| `4H` | `Aster` | `51.23%` | `48.77%` | `1.05` | 70,410.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `54.21%` | `45.79%` | `1.18` | 155,110.00 USD |
| `4H` | `Whale Positions` | `46.85%` | `53.15%` | `0.88` | 30,760,000.00 USD |
| `4H` | `Global Accounts` | `45.51%` | `54.49%` | `0.84` | 88,550,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9422` | `0.9454` | `0.9422` | `0.9510` | `0.9405` | 3,368,024.32 USD | 1,825,270.23 USD | 1,542,754.09 USD | 282,516.14 USD | `+8.39%` | `30B / 7S` |
| `5:00 UTC` | `0.9486` | `0.9483` | `0.9486` | `0.9509` | `0.9456` | 2,264,199.47 USD | 980,139.95 USD | 1,284,059.52 USD | -303,919.57 USD | `-13.42%` | `3B / 12S` |
| `0:00 UTC` | `0.9499` | `0.9497` | `0.9499` | `0.9526` | `0.9459` | 2,916,523.31 USD | 1,485,474.18 USD | 1,431,049.13 USD | 54,425.04 USD | `+1.87%` | `13B / 7S` |
| `5:00 UTC` | `0.9523` | `0.9521` | `0.9523` | `0.9548` | `0.9486` | 2,922,269.66 USD | 1,453,739.73 USD | 1,468,529.93 USD | -14,790.20 USD | `-0.51%` | `10B / 8S` |
| `0:00 UTC` | `0.9600` | `0.9565` | `0.9600` | `0.9617` | `0.9503` | 6,416,225.57 USD | 3,530,243.57 USD | 2,885,982.00 USD | 644,261.57 USD | `+10.04%` | `18B / 17S` |
| `5:00 UTC` | `0.9485` | `0.9509` | `0.9485` | `0.9584` | `0.9476` | 4,295,336.29 USD | 1,504,736.83 USD | 2,790,599.46 USD | -1,285,862.63 USD | `-29.94%` | `4B / 41S` |
| `0:00 UTC` | `0.9476` | `0.9462` | `0.9476` | `0.9495` | `0.9425` | 3,274,884.41 USD | 1,392,018.83 USD | 1,882,865.59 USD | -490,846.76 USD | `-14.99%` | `3B / 22S` |
| `5:00 UTC` | `0.9473` | `0.9468` | `0.9473` | `0.9484` | `0.9444` | 1,455,719.43 USD | 672,614.86 USD | 783,104.57 USD | -110,489.71 USD | `-7.59%` | `4B / 16S` |
| `0:00 UTC` | `0.9443` | `0.9448` | `0.9443` | `0.9482` | `0.9416` | 1,894,016.62 USD | 669,877.01 USD | 1,224,139.61 USD | -554,262.60 USD | `-29.26%` | `2B / 19S` |
| `5:00 UTC` | `0.9422` | `0.9417` | `0.9422` | `0.9429` | `0.9405` | 1,034,275.79 USD | 547,545.94 USD | 486,729.85 USD | 60,816.09 USD | `+5.88%` | `4B / 4S` |

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
| `5m` | 12,370.00 USD | -342,590.00 USD | **`DISTRIBUTION`** |
| `15m` | -63,330.00 USD | -1,180,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 6,670.00 USD | -1,740,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -436,040.00 USD | -5,780,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,350,000.00 USD | -6,120,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 4,050,000.00 USD | -2,910,000.00 USD | **`ACCUMULATION`** |
| `6h` | 4,430,000.00 USD | -3,670,000.00 USD | **`ACCUMULATION`** |
| `8h` | 4,010,000.00 USD | -3,330,000.00 USD | **`ACCUMULATION`** |
| `12h` | 4,710,000.00 USD | -4,240,000.00 USD | **`ACCUMULATION`** |
| `24h` | 6,030,000.00 USD | -12,010,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -14,070,000.00 USD | -62,100,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -141,580,000.00 USD | -456,900,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+12.37K` | 15m=`-63.33K` | 1h=`-436.04K` | 24h=`+6.03M`
* Futures Capital Netflows: 5m=`-342.59K` | 15m=`-1.18M` | 1h=`-5.78M` | 24h=`-12.01M`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
