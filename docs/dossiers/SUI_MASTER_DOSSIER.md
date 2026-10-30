# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:31:46 IST` (`2026-10-30 05:01:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8891` | `0.8905` | `0.8878` | `0.8882` | `714,565` | 635,288.04 USD | 49,483.33 USD | `+7.79%` | -12,417,013.59 USD | `-0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.8881` | `0.8890` | `0.8849` | `0.8872` | `1,714,194` | 1,519,777.02 USD | -338,415.42 USD | `-22.27%` | -12,755,429.01 USD | `-1.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.8872` | `0.8888` | `0.8872` | `0.8887` | `478,928` | 425,336.48 USD | 66,673.77 USD | `+15.68%` | -12,688,755.24 USD | `-0.08` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.8867` | `0.8907` | `0.8844` | `0.8890` | `4,006,842` | 3,559,512.45 USD | 317,033.48 USD | `+8.91%` | -12,515,491.76 USD | `+0.35` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8891` | `0.8905` | `0.8849` | `0.8899` | `3,027,442` | 2,686,854.06 USD | -234,810.69 USD | `-8.74%` | -12,750,302.45 USD | `+0.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.8900` | `0.8952` | `0.8896` | `0.8948` | `2,456,503` | 2,193,092.40 USD | -228,944.70 USD | `-10.44%` | -12,979,247.15 USD | `-0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8556` | `0.8707` | `0.8482` | `0.8661` | `11,338,098` | 9,773,400.88 USD | 845,261.99 USD | `+8.65%` | -14,666,181.90 USD | `+0.79` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.8661` | `0.8873` | `0.8656` | `0.8841` | `13,301,873` | 11,663,934.28 USD | 1,975,651.91 USD | `+16.94%` | -12,690,530.00 USD | `+1.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.8841` | `0.8952` | `0.8777` | `0.8948` | `13,832,957` | 12,263,127.92 USD | -288,717.15 USD | `-2.35%` | -12,979,247.15 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.8907` | `0.8777` | `0.8886` | `11,256,748` | 9,963,626.02 USD | -47,263.10 USD | `-0.47%` | -12,369,601.06 USD | `+0.64` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | 1,889,481.85 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -683,829.84 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.8952` | `0.8777` | `0.8948` | `13,832,957` | 12,263,127.92 USD | -288,717.15 USD | `-2.35%` | -12,611,055.12 USD | `+0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `0.8939` | `5604.8000` | 5,010.30 USD | 28,268.25 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8939` | `4443.9000` | 3,972.49 USD | 32,240.74 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.8940` | `4120.3000` | 3,683.59 USD | 19,721.23 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8940` | `3956.2000` | 3,536.72 USD | 23,257.95 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8941` | `138.7000` | 124.02 USD | 6,098.46 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8941` | `1605.7000` | 1,435.70 USD | 7,534.16 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.8941` | `138.7000` | 124.01 USD | 7,658.18 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8941` | `138.7000` | 124.01 USD | 7,782.19 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8941` | `138.7000` | 124.01 USD | 7,906.20 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8941` | `138.7000` | 124.01 USD | 8,030.21 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8941` | `138.7000` | 124.01 USD | 8,154.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8941` | `2094.3000` | 1,872.45 USD | 10,026.67 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8941` | `138.7000` | 124.01 USD | 10,150.68 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8941` | `6584.6000` | 5,886.96 USD | 16,037.64 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `0.8942` | `704.5000` | 630.00 USD | 1,632.32 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8942` | `520.0000` | 465.00 USD | 2,097.32 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8942` | `2241.7000` | 2,004.57 USD | 4,101.89 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8942` | `1955.5000` | 1,748.53 USD | 5,850.42 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8942` | `138.7000` | 124.02 USD | 5,974.44 USD | `1 orders` | `-0.02%` | `-` |
| `MID_SPREAD` | `0.8943` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.89` | `0.00%` | `-` |
| `BID` | `0.8943` | `1120.8000` | 1,002.32 USD | 1,002.32 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `0.8944` | `713.8000` | 638.40 USD | 638.40 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `0.8945` | `30.4000` | 27.19 USD | 6,169.71 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8945` | `1956.1000` | 1,749.81 USD | 6,142.51 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8945` | `1120.5000` | 1,002.30 USD | 4,392.70 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8945` | `1956.1000` | 1,749.67 USD | 3,390.41 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8945` | `1120.6000` | 1,002.33 USD | 1,640.73 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8946` | `1955.5000` | 1,749.49 USD | 16,281.76 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8946` | `1000.0000` | 894.64 USD | 14,532.27 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8946` | `2235.6000` | 2,000.01 USD | 13,637.63 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8946` | `2240.8000` | 2,004.64 USD | 11,637.62 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8946` | `1000.0000` | 894.60 USD | 9,632.98 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8946` | `2871.4000` | 2,568.67 USD | 8,738.38 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `0.8947` | `2794.2000` | 2,499.97 USD | 27,379.92 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8947` | `5600.3000` | 5,010.53 USD | 24,879.95 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8947` | `3010.0000` | 2,692.99 USD | 19,869.42 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.8947` | `1000.0000` | 894.67 USD | 17,176.43 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8948` | `1557.3000` | 1,393.53 USD | 31,244.90 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.8948` | `694.9000` | 621.82 USD | 29,851.36 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8948` | `2067.2000` | 1,849.63 USD | 29,229.55 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.8949` | `1117.7000` | 1,000.17 USD | 32,245.07 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `660` | `0xb83d...6e36` | `SHORT` | 3,409,659.66 USD | `3,817,609.40` | `1.11` | `0.8946` | `34.35` | 809,075.66 USD | `+23.73%` | `3X Cross` |
| `998` | `0xa2ce...3126` | `LONG` | 2,236,984.31 USD | `2,500,010.40` | `0.8597` | `0.8946` | `0.000000` | 87,777.78 USD | `+3.92%` | `10X Cross` |
| `1545` | `0x9946...0852` | `SHORT` | 1,393,174.15 USD | `1,557,106.30` | `1.07` | `0.8946` | `1.87` | 265,503.65 USD | `+19.06%` | `10X Cross` |
| `1904` | `0x9df2...c665` | `SHORT` | 1,071,768.00 USD | `1,200,000.00` | `0.7465` | `0.8946` | `25.87` | -175,915.60 USD | `-16.41%` | `10X Cross` |
| `2007` | `0x9aa5...58af` | `SHORT` | 1,010,096.06 USD | `1,129,280.30` | `1.14` | `0.8946` | `8.80` | 276,565.03 USD | `+27.38%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9071` | 418.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.42K USD at 0.9071 USD [API] | `2026-10-29 02:00:14` |
| `ANNOUNCEMENT` | `INFO` | `0.9026` | 47.30 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.05K USD at 0.9026 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `0.9026` | 11.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.01K USD at 0.9026 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `0.9026` | 227.27 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.23K USD at 0.9026 USD [API] | `2026-10-29 02:30:54` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9069` (Vol: 414,400.00 USD, Dist: `+1.34%`) | Long MP=`0.8716` (Vol: 414,400.00 USD, Dist: `--2.61%`)
  * 48H Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+1.41%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--2.64%`)
  * 3D Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+1.41%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--2.64%`)
  * 7D Horizon: Short MP=`0.9682` (Vol: 687,400.00 USD, Dist: `+8.19%`) | Long MP=`0.8711` (Vol: 414,400.00 USD, Dist: `--2.66%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1955` | 1,820.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1965` | 736.64 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 207.50 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 258.78 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 476.28 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 228.10 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 250.50 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 112.07 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 4,350.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 171.77 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 160.92 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 168.46 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 3,970.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 3,540.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2985` | 25,710.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3075` | 125.89 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,340.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3355` | 4,170.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3365` | 673.13 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 1,230.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3475` | 3,850.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 10,100.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3685` | 29,050.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3785` | 3,790.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3815` | 6,490.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3855` | 269.85 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 28,370.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 724.25 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 3,360.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4105` | 5,130.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 467.50 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4315` | 236.20 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4335` | 763.83 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 43,880.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 8,850.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 219.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 105.25 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4495` | 314.65 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 1,400.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 3,330.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 1,720.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4735` | 603.48 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 166.70 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 4,040.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 3,650.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 5,570.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 768.09 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4995` | 1,520.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5045` | 4,790.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 5,680.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 1,400.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 4,120.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 539.20 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 106.04 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 982.56 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5205` | 439.41 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5255` | 380.93 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5265` | 124.73 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 123,640.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 7,810.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 113.47 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 6,210.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 29,340.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 7,200.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 182.72 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 217.37 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 141.85 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5815` | 268.59 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 353.48 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 412.11 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 7,050.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5975` | 4,360.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 299.25 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 4,760.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 323.79 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6035` | 1,220.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 886.10 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6095` | 214.54 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,280.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 438.73 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 112.33 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 2,110.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,980.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 12,570.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 2,400.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6215` | 14,820.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 90,210.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,630.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 1,100.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 843.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 1,100.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6395` | 319.75 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 33,040.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 4,980.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,190.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 3,200.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 668.34 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 539.67 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 2,340.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6525` | 2,350.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 127,900.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 6,700.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 10,760.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 8,220.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6605` | 6,740.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 325.46 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 4,840.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 634.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 528.73 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 3,050.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 135.71 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 337.36 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 2,240.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,280.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 33,610.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 854.64 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 189.22 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 9,350.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 122.94 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 43,650.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 2,110.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 17,190.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 15,130.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,960.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 6,110.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 1,060.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 10,590.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 3,600.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 7,670.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,700.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,030.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 1,670.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 8,970.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 143.14 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 3,620.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,020.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 1,110.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 25,230.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 283.22 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 1,440.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 297.23 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 12,470.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 4,620.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7185` | 431,230.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 420.19 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 8,450.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,420.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 127.05 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7245` | 2,520.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 311.60 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 3,410.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 36,540.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 8,840.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 3,990.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 13,500.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 12,160.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7350` | 12,820,000.00 USD | 12,820,000.00 USD | 69,900.00 USD | 27,680.00 USD | 97,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7370` | 12,620,000.00 USD | 12,620,000.00 USD | 38,700.00 USD | 17,190.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7375` | 3,450.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,020.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7390` | 12,530,000.00 USD | 12,530,000.00 USD | 27,490.00 USD | 24,560.00 USD | 26,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7410` | 12,450,000.00 USD | 12,450,000.00 USD | 18,820.00 USD | 8,780.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 2,280.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7430` | 12,400,000.00 USD | 12,400,000.00 USD | 44,520.00 USD | 5,210.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7435` | 784,400.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7450` | 12,310,000.00 USD | 12,310,000.00 USD | 34,130.00 USD | 21,270.00 USD | 43,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7455` | 2,160.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7465` | 359.96 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7470` | 12,210,000.00 USD | 12,210,000.00 USD | 23,010.00 USD | 19,630.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7490` | 12,150,000.00 USD | 12,150,000.00 USD | 26,370.00 USD | 12,290.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7510` | 12,100,000.00 USD | 12,100,000.00 USD | 10,970.00 USD | 16,630.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7530` | 12,050,000.00 USD | 12,050,000.00 USD | 1,690.00 USD | 654.10 USD | 6,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7535` | 264.86 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 1,250.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7550` | 12,040,000.00 USD | 12,040,000.00 USD | 8,700.00 USD | 6,530.00 USD | 18,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7555` | 1,750.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7570` | 12,010,000.00 USD | 12,010,000.00 USD | 22,280.00 USD | 16,160.00 USD | 182.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7590` | 11,970,000.00 USD | 11,970,000.00 USD | 6,840.00 USD | 25,130.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,900.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7610` | 11,940,000.00 USD | 11,940,000.00 USD | 21,310.00 USD | 16,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7625` | 3,790.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 11,900,000.00 USD | 11,900,000.00 USD | 20,690.00 USD | 118.70 USD | 934.78 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 5,550.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 3,510.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 11,880,000.00 USD | 11,880,000.00 USD | 556.58 USD | 23,090.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,260.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 11,840,000.00 USD | 11,840,000.00 USD | 1,280.00 USD | 3,960.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 25,580.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 207.19 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 11,820,000.00 USD | 11,820,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 150,510.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 11,820,000.00 USD | 11,820,000.00 USD | 7,690.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,940.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 5,230.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 3,430.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 3,510.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 321,490.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7780` | 7,660,000.00 USD | 7,660,000.00 USD | 7,440.00 USD | 5,830.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 767,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 5,390.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 739,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7800` | 7,650,000.00 USD | 7,650,000.00 USD | 466.70 USD | 10,380.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7810` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 185.50 USD | 5,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 739,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7820` | 7,580,000.00 USD | 7,580,000.00 USD | 15,370.00 USD | 17,460.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7830` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 3,930.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 21,600.00 USD | 735,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7840` | 7,520,000.00 USD | 7,520,000.00 USD | 29,640.00 USD | 26,410.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7845` | 155.96 USD | 713,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7850` | 11,780,000.00 USD | 11,780,000.00 USD | 7,790.00 USD | 20,370.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7860` | 7,450,000.00 USD | 7,450,000.00 USD | 3,670.00 USD | 5,420.00 USD | 453.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 713,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 25,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 710,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7880` | 7,440,000.00 USD | 7,440,000.00 USD | 33,380.00 USD | 6,000.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 14,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7900` | 7,390,000.00 USD | 7,390,000.00 USD | 20,640.00 USD | 23,720.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 709,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 11,700,000.00 USD | 11,700,000.00 USD | 6,610.00 USD | 24,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 7,620.00 USD | 706,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 7,340,000.00 USD | 7,340,000.00 USD | 10,370.00 USD | 16,170.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 10,810.00 USD | 698,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7930` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 12,880.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 687,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7940` | 7,270,000.00 USD | 7,270,000.00 USD | 21,090.00 USD | 20,690.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 736.66 USD | 686,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 11,580,000.00 USD | 11,580,000.00 USD | 2,210.00 USD | 25,690.00 USD | 81,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 53,850.00 USD | 686,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 7,210,000.00 USD | 7,210,000.00 USD | 4,910.00 USD | 6,390.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 12,980.00 USD | 632,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7970` | 11,470,000.00 USD | 11,470,000.00 USD | 26,700.00 USD | 3,570.00 USD | 58,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,580.00 USD | 619,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 7,160,000.00 USD | 7,160,000.00 USD | 25,120.00 USD | 11,770.00 USD | 36,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 40,230.00 USD | 611,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 11,380,000.00 USD | 11,380,000.00 USD | 8,560.00 USD | 2,220.00 USD | 20,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 10,050.00 USD | 571,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 7,080,000.00 USD | 7,080,000.00 USD | 32,430.00 USD | 21,300.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 3,850.00 USD | 561,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8010` | 11,350,000.00 USD | 11,350,000.00 USD | 43,340.00 USD | 14,760.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 7,610.00 USD | 557,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8020` | 6,990,000.00 USD | 6,990,000.00 USD | 1,730.00 USD | 251.75 USD | 1,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 1,350.00 USD | 550,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,680.00 USD | 548,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8040` | 6,990,000.00 USD | 6,990,000.00 USD | 37,430.00 USD | 23,740.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8045` | 16,660.00 USD | 540,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8050` | 11,260,000.00 USD | 11,260,000.00 USD | 10,860.00 USD | 19,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 361.11 USD | 524,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 6,910,000.00 USD | 6,910,000.00 USD | 50,970.00 USD | 15,130.00 USD | 70,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 523,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8070` | 11,230,000.00 USD | 11,230,000.00 USD | 5,030.00 USD | 11,280.00 USD | 1,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 517,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8080` | 6,770,000.00 USD | 6,770,000.00 USD | 3,230.00 USD | 19,130.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,510.00 USD | 514,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8090` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 9,100.00 USD | 11,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 130,110.00 USD | 491,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 6,750,000.00 USD | 6,750,000.00 USD | 1,750.00 USD | 6,140.00 USD | 1,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,430.00 USD | 361,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8110` | 11,190,000.00 USD | 11,190,000.00 USD | 61,670.00 USD | 8,310.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,970.00 USD | 359,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 6,740,000.00 USD | 6,740,000.00 USD | 15,380.00 USD | 3,270.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 1,160.00 USD | 356,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8130` | 11,080,000.00 USD | 11,080,000.00 USD | 45,800.00 USD | 19,710.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 355,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 6,700,000.00 USD | 6,700,000.00 USD | 29,630.00 USD | 9,710.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 351,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 11,000,000.00 USD | 11,000,000.00 USD | 139,680.00 USD | 51,810.00 USD | 169,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 38,250.00 USD | 351,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 6,630,000.00 USD | 6,630,000.00 USD | 116,280.00 USD | 24,170.00 USD | 173,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 492.27 USD | 312,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8170` | 10,640,000.00 USD | 10,640,000.00 USD | 91,050.00 USD | 25,080.00 USD | 78,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 77,840.00 USD | 312,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 6,320,000.00 USD | 6,320,000.00 USD | 66,880.00 USD | 10,440.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 28,030.00 USD | 234,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 10,440,000.00 USD | 10,440,000.00 USD | 200,250.00 USD | 53,380.00 USD | 47,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,110.00 USD | 206,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 6,210,000.00 USD | 6,210,000.00 USD | 112,400.00 USD | 8,800.00 USD | 88,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 9,370.00 USD | 205,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 10,140,000.00 USD | 10,140,000.00 USD | 138,580.00 USD | 80,040.00 USD | 198,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 474.01 USD | 195,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 6,000,000.00 USD | 6,000,000.00 USD | 86,610.00 USD | 89,600.00 USD | 85,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 3,080.00 USD | 195,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 9,720,000.00 USD | 9,720,000.00 USD | 44,590.00 USD | 40,420.00 USD | 66,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 463.63 USD | 192,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 5,740,000.00 USD | 5,740,000.00 USD | 10,570.00 USD | 6,410.00 USD | 149,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 18,980.00 USD | 191,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 9,570,000.00 USD | 9,570,000.00 USD | 198,230.00 USD | 30,370.00 USD | 126,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 1,580.00 USD | 172,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 5,570,000.00 USD | 5,570,000.00 USD | 43,870.00 USD | 11,180.00 USD | 24,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 9,220,000.00 USD | 9,220,000.00 USD | 147,770.00 USD | 53,560.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 171,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 5,490,000.00 USD | 5,490,000.00 USD | 41,470.00 USD | 22,760.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 166,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8290` | 8,950,000.00 USD | 8,950,000.00 USD | 94,690.00 USD | 42,420.00 USD | 82,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 46,590.00 USD | 46,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8300` | 5,420,000.00 USD | 5,420,000.00 USD | 27,690.00 USD | 14,510.00 USD | 54,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 8,730,000.00 USD | 8,730,000.00 USD | 36,870.00 USD | 32,050.00 USD | 116,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 5,320,000.00 USD | 5,320,000.00 USD | 3,000.00 USD | 37,880.00 USD | 41,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 8,550,000.00 USD | 8,550,000.00 USD | 157,210.00 USD | 105,720.00 USD | 198,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 5,240,000.00 USD | 5,240,000.00 USD | 149,160.00 USD | 40,080.00 USD | 100,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 8,080,000.00 USD | 8,080,000.00 USD | 117,940.00 USD | 16,770.00 USD | 84,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 4,950,000.00 USD | 4,950,000.00 USD | 58,860.00 USD | 13,380.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 7,870,000.00 USD | 7,870,000.00 USD | 140,480.00 USD | 109,700.00 USD | 145,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 4,880,000.00 USD | 4,880,000.00 USD | 51,030.00 USD | 66,750.00 USD | 144,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 7,470,000.00 USD | 7,470,000.00 USD | 30,810.00 USD | 160,930.00 USD | 164,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8395` | 190.31 USD | 190.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 4,610,000.00 USD | 4,610,000.00 USD | 36,990.00 USD | 9,770.00 USD | 55,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 7,110,000.00 USD | 7,110,000.00 USD | 91,790.00 USD | 34,400.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8420` | 4,510,000.00 USD | 4,510,000.00 USD | 89,320.00 USD | 63,630.00 USD | 65,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 6,960,000.00 USD | 6,960,000.00 USD | 67,920.00 USD | 123,520.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 4,290,000.00 USD | 4,290,000.00 USD | 67,620.00 USD | 63,050.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 6,760,000.00 USD | 6,760,000.00 USD | 34,560.00 USD | 102,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 4,140,000.00 USD | 4,140,000.00 USD | 22,250.00 USD | 93,240.00 USD | 39,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 6,620,000.00 USD | 6,620,000.00 USD | 44,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 3,990,000.00 USD | 3,990,000.00 USD | 51,620.00 USD | 61,820.00 USD | 70,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 6,580,000.00 USD | 6,580,000.00 USD | 64,910.00 USD | 69,480.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8500` | 3,800,000.00 USD | 3,800,000.00 USD | 71,330.00 USD | 88,390.00 USD | 167,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 6,310,000.00 USD | 6,310,000.00 USD | 155,060.00 USD | 72,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 3,480,000.00 USD | 3,480,000.00 USD | 89,760.00 USD | 172,130.00 USD | 134,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 6,080,000.00 USD | 6,080,000.00 USD | 215,880.00 USD | 17,300.00 USD | 52,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 3,080,000.00 USD | 3,080,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 5,800,000.00 USD | 5,800,000.00 USD | 78,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 24,460.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 5,720,000.00 USD | 5,720,000.00 USD | 99,680.00 USD | 55,310.00 USD | 33,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,810,000.00 USD | 2,810,000.00 USD | 32,900.00 USD | 66,810.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 5,530,000.00 USD | 5,530,000.00 USD | 132,610.00 USD | 56,980.00 USD | 33,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,690,000.00 USD | 2,690,000.00 USD | 75,640.00 USD | 23,780.00 USD | 23,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 5,310,000.00 USD | 5,310,000.00 USD | 36,870.00 USD | 188,190.00 USD | 28,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,560,000.00 USD | 2,560,000.00 USD | 46,800.00 USD | 25,800.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 5,060,000.00 USD | 5,060,000.00 USD | 100,980.00 USD | 64,400.00 USD | 388,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,460,000.00 USD | 2,460,000.00 USD | 77,240.00 USD | 137,660.00 USD | 98,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 4,500,000.00 USD | 4,500,000.00 USD | 254,940.00 USD | 93,770.00 USD | 562,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,150,000.00 USD | 2,150,000.00 USD | 118,030.00 USD | 27,450.00 USD | 154,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 3,590,000.00 USD | 3,590,000.00 USD | 252,430.00 USD | 0.00 USD | 126,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,850,000.00 USD | 1,850,000.00 USD | 106,760.00 USD | 11,860.00 USD | 125,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 108,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 38,850.00 USD | 50,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 3,100,000.00 USD | 3,100,000.00 USD | 207,250.00 USD | 34,600.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,520,000.00 USD | 1,520,000.00 USD | 182,270.00 USD | 62,100.00 USD | 172,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 88,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,100,000.00 USD | 1,100,000.00 USD | 55,600.00 USD | 0.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 2,770,000.00 USD | 2,770,000.00 USD | 26,230.00 USD | 0.00 USD | 258,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 150,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 866,800.00 USD | 866,800.00 USD | 79,990.00 USD | 6,840.00 USD | 67,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 712,120.00 USD | 712,120.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 2,410,000.00 USD | 2,410,000.00 USD | 20,310.00 USD | 3,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 707,360.00 USD | 707,360.00 USD | 37,200.00 USD | 0.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 575,310.00 USD | 575,310.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 35,900.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 573,040.00 USD | 573,040.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 571,960.00 USD | 571,960.00 USD | 122,200.00 USD | 1,400.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8885` | 322.61 USD | 512.93 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8890` | 2,340,000.00 USD | 2,340,000.00 USD | 8,820.00 USD | 3,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 447,010.00 USD | 447,010.00 USD | 2,860.00 USD | 0.00 USD | 49,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 2,330,000.00 USD | 2,330,000.00 USD | 523,470.00 USD | 55,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 395,140.00 USD | 395,140.00 USD | 137,750.00 USD | 0.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8925` | 807.44 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,750,000.00 USD | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8935` | 2,520.00 USD | 3,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8940` | 246,060.00 USD | 246,060.00 USD | 200,000.00 USD | 45,760.00 USD | 298.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 881,620.00 USD | 881,620.00 USD | 800,940.00 USD | 68,760.00 USD | 11,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 1,760,000.00 USD | 1,760,000.00 USD | 800,940.00 USD | 68,760.00 USD | 11,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8960` | 113,450.00 USD | 113,450.00 USD | 2,890.00 USD | 107,980.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8965` | 187.46 USD | 4,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8970` | 2,490,000.00 USD | 2,490,000.00 USD | 634,760.00 USD | 93,070.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8980` | 536,750.00 USD | 536,750.00 USD | 74,000.00 USD | 98,360.00 USD | 250,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8990` | 3,280,000.00 USD | 3,280,000.00 USD | 379,180.00 USD | 67,360.00 USD | 340,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9000` | 1,230,000.00 USD | 1,230,000.00 USD | 239,630.00 USD | 191,290.00 USD | 257,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 3,980,000.00 USD | 3,980,000.00 USD | 207,550.00 USD | 109,410.00 USD | 381,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 1,950,000.00 USD | 1,950,000.00 USD | 209,800.00 USD | 138,990.00 USD | 379,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9030` | 4,300,000.00 USD | 4,300,000.00 USD | 124,030.00 USD | 99,390.00 USD | 101,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9040` | 2,720,000.00 USD | 2,720,000.00 USD | 211,950.00 USD | 223,010.00 USD | 330,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9050` | 4,800,000.00 USD | 4,800,000.00 USD | 169,680.00 USD | 0.00 USD | 323,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9060` | 3,310,000.00 USD | 3,310,000.00 USD | 258,520.00 USD | 125,650.00 USD | 203,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 5,470,000.00 USD | 5,470,000.00 USD | 548,330.00 USD | 85,530.00 USD | 40,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9080` | 3,840,000.00 USD | 3,840,000.00 USD | 249,000.00 USD | 147,110.00 USD | 133,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 5,870,000.00 USD | 5,870,000.00 USD | 60,680.00 USD | 142,850.00 USD | 191,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 4,010,000.00 USD | 4,010,000.00 USD | 99,190.00 USD | 39,940.00 USD | 29,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 6,290,000.00 USD | 6,290,000.00 USD | 259,120.00 USD | 103,750.00 USD | 66,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 4,290,000.00 USD | 4,290,000.00 USD | 100,870.00 USD | 97,820.00 USD | 90,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 6,530,000.00 USD | 6,530,000.00 USD | 80,230.00 USD | 86,960.00 USD | 66,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 4,740,000.00 USD | 4,740,000.00 USD | 181,270.00 USD | 56,340.00 USD | 209,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 8,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9150` | 6,920,000.00 USD | 6,920,000.00 USD | 111,690.00 USD | 111,780.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9160` | 5,270,000.00 USD | 5,270,000.00 USD | 130,780.00 USD | 169,050.00 USD | 223,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 7,090,000.00 USD | 7,090,000.00 USD | 163,880.00 USD | 2,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9175` | 2,910.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9180` | 5,500,000.00 USD | 5,500,000.00 USD | 90,690.00 USD | 51,410.00 USD | 93,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 7,690,000.00 USD | 7,690,000.00 USD | 296,480.00 USD | 60,800.00 USD | 238,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9200` | 5,710,000.00 USD | 5,710,000.00 USD | 73,730.00 USD | 22,510.00 USD | 112,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 8,070,000.00 USD | 8,070,000.00 USD | 194,470.00 USD | 18,660.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 6,270,000.00 USD | 6,270,000.00 USD | 203,870.00 USD | 94,010.00 USD | 260,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 8,590,000.00 USD | 8,590,000.00 USD | 56,540.00 USD | 68,150.00 USD | 395,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9240` | 6,860,000.00 USD | 6,860,000.00 USD | 240,420.00 USD | 84,970.00 USD | 266,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 8,880,000.00 USD | 8,880,000.00 USD | 158,890.00 USD | 63,010.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 7,220,000.00 USD | 7,220,000.00 USD | 135,010.00 USD | 117,320.00 USD | 105,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 9,240,000.00 USD | 9,240,000.00 USD | 220,880.00 USD | 46,830.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 7,370,000.00 USD | 7,370,000.00 USD | 5,090.00 USD | 67,540.00 USD | 74,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 9,330,000.00 USD | 9,330,000.00 USD | 4,480.00 USD | 53,740.00 USD | 35,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 7,590,000.00 USD | 7,590,000.00 USD | 43,730.00 USD | 61,500.00 USD | 115,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9305` | 4,210.00 USD | 15,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9310` | 9,770,000.00 USD | 9,770,000.00 USD | 181,630.00 USD | 50,140.00 USD | 199,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 7,850,000.00 USD | 7,850,000.00 USD | 176,150.00 USD | 29,700.00 USD | 59,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9325` | 523.13 USD | 15,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9330` | 9,910,000.00 USD | 9,910,000.00 USD | 4,410.00 USD | 76,570.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 7,890,000.00 USD | 7,890,000.00 USD | 5,250.00 USD | 35,920.00 USD | 706.99 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 10,020,000.00 USD | 10,020,000.00 USD | 53,950.00 USD | 55,880.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 8,020,000.00 USD | 8,020,000.00 USD | 48,720.00 USD | 17,210.00 USD | 55,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 10,330,000.00 USD | 10,330,000.00 USD | 256,610.00 USD | 5,150.00 USD | 46,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 8,470,000.00 USD | 8,470,000.00 USD | 155,050.00 USD | 62,150.00 USD | 239,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 39,850.00 USD | 55,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9390` | 10,720,000.00 USD | 10,720,000.00 USD | 86,850.00 USD | 36,340.00 USD | 265,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 8,620,000.00 USD | 8,620,000.00 USD | 58,840.00 USD | 3,680.00 USD | 89,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 10,850,000.00 USD | 10,850,000.00 USD | 123,000.00 USD | 6,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 8,680,000.00 USD | 8,680,000.00 USD | 17,290.00 USD | 13,920.00 USD | 24,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 10,960,000.00 USD | 10,960,000.00 USD | 4,970.00 USD | 68,030.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 8,780,000.00 USD | 8,780,000.00 USD | 6,330.00 USD | 38,560.00 USD | 58,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 11,300,000.00 USD | 11,300,000.00 USD | 3,360.00 USD | 244,270.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 9,030,000.00 USD | 9,030,000.00 USD | 59,870.00 USD | 32,120.00 USD | 159,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 9,260,000.00 USD | 9,260,000.00 USD | 91,790.00 USD | 73,040.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 9,390,000.00 USD | 9,390,000.00 USD | 26,310.00 USD | 36,450.00 USD | 70,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 12,560,000.00 USD | 12,560,000.00 USD | 2,840.00 USD | 88,970.00 USD | 736,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 9,680,000.00 USD | 9,680,000.00 USD | 52,590.00 USD | 28,420.00 USD | 211,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 1,270.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 9,890,000.00 USD | 9,890,000.00 USD | 59,080.00 USD | 50,610.00 USD | 94,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 12,700,000.00 USD | 12,700,000.00 USD | 74,980.00 USD | 2,400.00 USD | 60,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 10,000,000.00 USD | 10,000,000.00 USD | 40,290.00 USD | 26,630.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 13,170,000.00 USD | 13,170,000.00 USD | 463,830.00 USD | 4,720.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 10,090,000.00 USD | 10,090,000.00 USD | 27,440.00 USD | 45,440.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 13,760,000.00 USD | 13,760,000.00 USD | 563,790.00 USD | 21,410.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 10,320,000.00 USD | 10,320,000.00 USD | 102,060.00 USD | 50,930.00 USD | 78,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 15,130,000.00 USD | 15,130,000.00 USD | 698,570.00 USD | 201,530.00 USD | 476,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 10,830,000.00 USD | 10,830,000.00 USD | 267,480.00 USD | 67,570.00 USD | 177,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 16,630,000.00 USD | 16,630,000.00 USD | 579,300.00 USD | 301,610.00 USD | 616,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 11,240,000.00 USD | 11,240,000.00 USD | 238,280.00 USD | 68,650.00 USD | 102,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 18,210,000.00 USD | 18,210,000.00 USD | 857,470.00 USD | 312,610.00 USD | 412,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 11,600,000.00 USD | 11,600,000.00 USD | 156,170.00 USD | 130,010.00 USD | 71,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 20,190,000.00 USD | 20,190,000.00 USD | 801,890.00 USD | 555,340.00 USD | 614,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 12,140,000.00 USD | 12,140,000.00 USD | 175,350.00 USD | 67,790.00 USD | 303,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 21,550,000.00 USD | 21,550,000.00 USD | 596,350.00 USD | 312,990.00 USD | 456,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 12,720,000.00 USD | 12,720,000.00 USD | 274,850.00 USD | 111,340.00 USD | 186,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 22,670,000.00 USD | 22,670,000.00 USD | 647,710.00 USD | 319,140.00 USD | 147,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 13,000,000.00 USD | 13,000,000.00 USD | 99,840.00 USD | 64,240.00 USD | 118,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 23,480,000.00 USD | 23,480,000.00 USD | 456,990.00 USD | 160,420.00 USD | 197,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 13,080,000.00 USD | 13,080,000.00 USD | 36,690.00 USD | 2,780.00 USD | 43,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 24,220,000.00 USD | 24,220,000.00 USD | 227,380.00 USD | 293,590.00 USD | 222,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 13,220,000.00 USD | 13,220,000.00 USD | 20,700.00 USD | 29,360.00 USD | 84,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 25,290,000.00 USD | 25,290,000.00 USD | 329,170.00 USD | 211,000.00 USD | 521,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 13,380,000.00 USD | 13,380,000.00 USD | 32,890.00 USD | 32,300.00 USD | 101,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 25,920,000.00 USD | 25,920,000.00 USD | 342,340.00 USD | 72,140.00 USD | 222,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 13,590,000.00 USD | 13,590,000.00 USD | 61,120.00 USD | 37,860.00 USD | 107,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 56,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 26,360,000.00 USD | 26,360,000.00 USD | 206,910.00 USD | 60,620.00 USD | 169,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 13,670,000.00 USD | 13,670,000.00 USD | 77,470.00 USD | 5,610.00 USD | 225.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 26,940,000.00 USD | 26,940,000.00 USD | 262,900.00 USD | 116,030.00 USD | 199,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 13,760,000.00 USD | 13,760,000.00 USD | 33,500.00 USD | 44,230.00 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 27,350,000.00 USD | 27,350,000.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 13,960,000.00 USD | 13,960,000.00 USD | 70,580.00 USD | 40,790.00 USD | 90,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 56,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9870` | 27,860,000.00 USD | 27,860,000.00 USD | 248,980.00 USD | 203,100.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 14,100,000.00 USD | 14,100,000.00 USD | 75,940.00 USD | 21,120.00 USD | 42,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 61,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9890` | 28,150,000.00 USD | 28,150,000.00 USD | 194,850.00 USD | 78,280.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 14,200,000.00 USD | 14,200,000.00 USD | 74,180.00 USD | 15,760.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 1,570.00 USD | 62,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9910` | 28,520,000.00 USD | 28,520,000.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 28,890,000.00 USD | 28,890,000.00 USD | 228,340.00 USD | 63,950.00 USD | 74,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 62,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9950` | 29,200,000.00 USD | 29,200,000.00 USD | 48,120.00 USD | 138,500.00 USD | 130,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 29,860,000.00 USD | 29,860,000.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 30,140,000.00 USD | 30,140,000.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 30,580,000.00 USD | 30,580,000.00 USD | 202,970.00 USD | 57,170.00 USD | 185,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 63,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,080,000.00 USD | 31,080,000.00 USD | 226,340.00 USD | 61,540.00 USD | 208,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,230,000.00 USD | 31,230,000.00 USD | 51,930.00 USD | 39,560.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 100.65 USD | 63,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 31,540,000.00 USD | 31,540,000.00 USD | 168,320.00 USD | 16,800.00 USD | 121,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 32,070,000.00 USD | 32,070,000.00 USD | 247,480.00 USD | 61,720.00 USD | 214,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 32,640,000.00 USD | 32,640,000.00 USD | 334,550.00 USD | 84,080.00 USD | 157,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 33,350,000.00 USD | 33,350,000.00 USD | 188,370.00 USD | 177,300.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 705.99 USD | 64,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 33,710,000.00 USD | 33,710,000.00 USD | 168,660.00 USD | 60,680.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 64,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 34,180,000.00 USD | 34,180,000.00 USD | 148,890.00 USD | 62,970.00 USD | 266,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 1,670.00 USD | 65,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 34,660,000.00 USD | 34,660,000.00 USD | 180,470.00 USD | 47,380.00 USD | 245,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 34,920,000.00 USD | 34,920,000.00 USD | 95,590.00 USD | 18,960.00 USD | 151,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 35,240,000.00 USD | 35,240,000.00 USD | 151,650.00 USD | 61,120.00 USD | 103,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 35,430,000.00 USD | 35,430,000.00 USD | 59,440.00 USD | 54,210.00 USD | 77,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 35,630,000.00 USD | 35,630,000.00 USD | 76,740.00 USD | 35,970.00 USD | 82,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 35,800,000.00 USD | 35,800,000.00 USD | 85,920.00 USD | 34,530.00 USD | 50,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 36,040,000.00 USD | 36,040,000.00 USD | 135,830.00 USD | 33,520.00 USD | 76,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 36,370,000.00 USD | 36,370,000.00 USD | 57,570.00 USD | 103,690.00 USD | 163,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 36,510,000.00 USD | 36,510,000.00 USD | 64,880.00 USD | 13,040.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 36,740,000.00 USD | 36,740,000.00 USD | 79,670.00 USD | 21,540.00 USD | 133,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 36,860,000.00 USD | 36,860,000.00 USD | 53,800.00 USD | 806.65 USD | 63,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 155.92 USD | 66,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 66,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 69,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 72,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 78,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 78,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 78,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 1,310.00 USD | 80,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 8,940.00 USD | 89,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 112,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 112,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 177.65 USD | 113,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 117,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 383.01 USD | 118,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 118,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 3,930.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 1,230.00 USD | 123,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 126,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 128,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 168,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 9,820.00 USD | 178,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 178,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 178,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 179,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 211,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 229.23 USD | 211,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 217,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 239,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 246,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 1,110.00 USD | 247,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.35` | 22,760.00 USD | 270,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 628,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 633,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 633,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 633,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 142.05 USD | 633,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 16,780.00 USD | 650,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 654,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 152.85 USD | 654,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 9,930.00 USD | 664,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 664,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 665,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,180.00 USD | 666,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 123.81 USD | 666,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 135.24 USD | 666,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,130.00 USD | 667,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 689,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 3,940.00 USD | 693,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 3,620.00 USD | 696,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,090.00 USD | 735,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 290,220.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 150.02 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 9,700.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 492.06 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 983.07 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 7,000.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1955` | 4,690,000.00 USD | 0.00 USD | 1,820.00 USD | `-77.79%` | `9,320.00` |
| `Live` | `Long` | `0.1965` | 4,690,000.00 USD | 0.00 USD | 736.64 USD | `-77.68%` | `3,748.80` |
| `Live` | `Long` | `0.1995` | 4,690,000.00 USD | 0.00 USD | 256.00 USD | `-77.34%` | `1,283.20` |
| `Live` | `Long` | `0.2075` | 4,690,000.00 USD | 0.00 USD | 207.50 USD | `-76.43%` | `1,000.00` |
| `Live` | `Long` | `0.2135` | 4,690,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.75%` | `18,919.90` |
| `Live` | `Long` | `0.2215` | 4,690,000.00 USD | 0.00 USD | 258.78 USD | `-74.84%` | `1,168.30` |
| `Live` | `Long` | `0.2225` | 4,690,000.00 USD | 0.00 USD | 476.28 USD | `-74.73%` | `2,140.60` |
| `Live` | `Long` | `0.2345` | 4,680,000.00 USD | 0.00 USD | 228.10 USD | `-73.36%` | `972.70` |
| `Live` | `Long` | `0.2355` | 4,680,000.00 USD | 0.00 USD | 789.66 USD | `-73.25%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,680,000.00 USD | 0.00 USD | 156.36 USD | `-72.91%` | `655.60` |
| `Live` | `Long` | `0.2505` | 4,680,000.00 USD | 0.00 USD | 250.50 USD | `-71.54%` | `1,000.00` |
| `Live` | `Long` | `0.2525` | 4,680,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.32%` | `8,897.00` |
| `Live` | `Long` | `0.2535` | 4,680,000.00 USD | 0.00 USD | 112.07 USD | `-71.20%` | `442.10` |
| `Live` | `Long` | `0.2575` | 4,680,000.00 USD | 0.00 USD | 4,350.00 USD | `-70.75%` | `16,877.10` |
| `Live` | `Long` | `0.2645` | 4,680,000.00 USD | 0.00 USD | 171.77 USD | `-69.95%` | `649.40` |
| `Live` | `Long` | `0.2685` | 4,680,000.00 USD | 0.00 USD | 106.16 USD | `-69.50%` | `395.40` |
| `Live` | `Long` | `0.2695` | 4,680,000.00 USD | 0.00 USD | 160.92 USD | `-69.39%` | `597.10` |
| `Live` | `Long` | `0.2725` | 4,680,000.00 USD | 0.00 USD | 168.46 USD | `-69.05%` | `618.20` |
| `Live` | `Long` | `0.2735` | 4,680,000.00 USD | 0.00 USD | 248.34 USD | `-68.93%` | `908.00` |
| `Live` | `Long` | `0.2785` | 4,680,000.00 USD | 0.00 USD | 3,970.00 USD | `-68.36%` | `14,245.00` |
| `Live` | `Long` | `0.2885` | 4,670,000.00 USD | 0.00 USD | 29,070.00 USD | `-67.23%` | `100,768.40` |
| `Live` | `Long` | `0.2905` | 4,640,000.00 USD | 0.00 USD | 3,540.00 USD | `-67.00%` | `12,176.00` |
| `Live` | `Long` | `0.2975` | 4,640,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.21%` | `14,561.30` |
| `Live` | `Long` | `0.2985` | 4,640,000.00 USD | 0.00 USD | 25,710.00 USD | `-66.09%` | `86,117.40` |
| `Live` | `Long` | `0.3075` | 4,610,000.00 USD | 0.00 USD | 125.89 USD | `-65.07%` | `409.40` |
| `Live` | `Long` | `0.3115` | 4,610,000.00 USD | 0.00 USD | 270.38 USD | `-64.62%` | `868.00` |
| `Live` | `Long` | `0.3175` | 4,610,000.00 USD | 0.00 USD | 1,340.00 USD | `-63.93%` | `4,218.90` |
| `Live` | `Long` | `0.3355` | 4,610,000.00 USD | 0.00 USD | 4,170.00 USD | `-61.89%` | `12,426.00` |
| `Live` | `Long` | `0.3365` | 4,600,000.00 USD | 0.00 USD | 673.13 USD | `-61.78%` | `2,000.40` |
| `Live` | `Long` | `0.3465` | 4,600,000.00 USD | 0.00 USD | 1,230.00 USD | `-60.64%` | `3,555.40` |
| `Live` | `Long` | `0.3475` | 4,600,000.00 USD | 0.00 USD | 3,850.00 USD | `-60.53%` | `11,077.80` |
| `Live` | `Long` | `0.3505` | 4,600,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.19%` | `2,908.00` |
| `Live` | `Long` | `0.3545` | 4,600,000.00 USD | 0.00 USD | 10,100.00 USD | `-59.73%` | `28,480.20` |
| `Live` | `Long` | `0.3585` | 4,590,000.00 USD | 0.00 USD | 595.72 USD | `-59.28%` | `1,661.70` |
| `Live` | `Long` | `0.3665` | 4,590,000.00 USD | 0.00 USD | 274.88 USD | `-58.37%` | `750.00` |
| `Live` | `Long` | `0.3685` | 4,590,000.00 USD | 0.00 USD | 29,050.00 USD | `-58.14%` | `78,821.50` |
| `Live` | `Long` | `0.3785` | 4,560,000.00 USD | 0.00 USD | 3,790.00 USD | `-57.00%` | `10,000.00` |
| `Live` | `Long` | `0.3795` | 4,550,000.00 USD | 0.00 USD | 278.02 USD | `-56.89%` | `732.60` |
| `Live` | `Long` | `0.3815` | 4,550,000.00 USD | 0.00 USD | 6,490.00 USD | `-56.66%` | `17,000.00` |
| `Live` | `Long` | `0.3845` | 4,550,000.00 USD | 0.00 USD | 1,750.00 USD | `-56.32%` | `4,562.20` |
| `Live` | `Long` | `0.3855` | 4,540,000.00 USD | 0.00 USD | 269.85 USD | `-56.21%` | `700.00` |
| `Live` | `Long` | `0.3895` | 4,540,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.76%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 4,540,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.41%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,540,000.00 USD | 0.00 USD | 28,370.00 USD | `-55.19%` | `71,912.50` |
| `Live` | `Long` | `0.3995` | 4,510,000.00 USD | 0.00 USD | 724.25 USD | `-54.62%` | `1,812.90` |
| `Live` | `Long` | `0.4035` | 4,510,000.00 USD | 0.00 USD | 935.03 USD | `-54.16%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,510,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.05%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,500,000.00 USD | 0.00 USD | 3,360.00 USD | `-53.82%` | `8,275.50` |
| `Live` | `Long` | `0.4105` | 4,500,000.00 USD | 0.00 USD | 5,130.00 USD | `-53.37%` | `12,500.00` |
| `Live` | `Long` | `0.4235` | 4,490,000.00 USD | 0.00 USD | 467.50 USD | `-51.89%` | `1,103.90` |
| `Live` | `Long` | `0.4315` | 4,490,000.00 USD | 0.00 USD | 236.20 USD | `-50.98%` | `547.40` |
| `Live` | `Long` | `0.4335` | 4,490,000.00 USD | 0.00 USD | 763.83 USD | `-50.76%` | `1,762.00` |
| `Live` | `Long` | `0.4385` | 4,490,000.00 USD | 0.00 USD | 122.91 USD | `-50.19%` | `280.30` |
| `Live` | `Long` | `0.4405` | 4,490,000.00 USD | 0.00 USD | 43,880.00 USD | `-49.96%` | `99,611.70` |
| `Live` | `Long` | `0.4425` | 4,450,000.00 USD | 0.00 USD | 8,850.00 USD | `-49.73%` | `20,000.00` |
| `Live` | `Long` | `0.4435` | 4,440,000.00 USD | 0.00 USD | 219.00 USD | `-49.62%` | `493.80` |
| `Live` | `Long` | `0.4455` | 4,440,000.00 USD | 0.00 USD | 574.83 USD | `-49.39%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,440,000.00 USD | 0.00 USD | 19,600.00 USD | `-49.28%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,420,000.00 USD | 0.00 USD | 105.25 USD | `-49.17%` | `235.20` |
| `Live` | `Long` | `0.4495` | 4,420,000.00 USD | 0.00 USD | 314.65 USD | `-48.94%` | `700.00` |
| `Live` | `Long` | `0.4535` | 4,420,000.00 USD | 0.00 USD | 1,400.00 USD | `-48.49%` | `3,094.60` |
| `Live` | `Long` | `0.4595` | 4,420,000.00 USD | 0.00 USD | 3,330.00 USD | `-47.80%` | `7,245.50` |
| `Live` | `Long` | `0.4715` | 4,410,000.00 USD | 0.00 USD | 1,720.00 USD | `-46.44%` | `3,650.40` |
| `Live` | `Long` | `0.4735` | 4,410,000.00 USD | 0.00 USD | 603.48 USD | `-46.21%` | `1,274.50` |
| `Live` | `Long` | `0.4785` | 4,410,000.00 USD | 0.00 USD | 110.10 USD | `-45.65%` | `230.10` |
| `Live` | `Long` | `0.4825` | 4,410,000.00 USD | 0.00 USD | 166.70 USD | `-45.19%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,410,000.00 USD | 0.00 USD | 4,040.00 USD | `-45.08%` | `8,345.80` |
| `Live` | `Long` | `0.4855` | 4,410,000.00 USD | 0.00 USD | 3,650.00 USD | `-44.85%` | `7,509.00` |
| `Live` | `Long` | `0.4865` | 4,400,000.00 USD | 0.00 USD | 201.07 USD | `-44.74%` | `413.30` |
| `Live` | `Long` | `0.4895` | 4,400,000.00 USD | 0.00 USD | 105.34 USD | `-44.40%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,400,000.00 USD | 0.00 USD | 2,380.00 USD | `-44.17%` | `4,848.70` |
| `Live` | `Long` | `0.4935` | 4,400,000.00 USD | 0.00 USD | 5,570.00 USD | `-43.94%` | `11,290.30` |
| `Live` | `Long` | `0.4945` | 4,390,000.00 USD | 0.00 USD | 106.32 USD | `-43.83%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,390,000.00 USD | 0.00 USD | 211.88 USD | `-43.71%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,390,000.00 USD | 0.00 USD | 768.09 USD | `-43.37%` | `1,540.80` |
| `Live` | `Long` | `0.4995` | 4,390,000.00 USD | 0.00 USD | 1,520.00 USD | `-43.26%` | `3,043.40` |
| `Live` | `Long` | `0.5015` | 4,390,000.00 USD | 0.00 USD | 212.49 USD | `-43.03%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,390,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.92%` | `2,451.10` |
| `Live` | `Long` | `0.5045` | 4,390,000.00 USD | 0.00 USD | 4,790.00 USD | `-42.69%` | `9,500.00` |
| `Live` | `Long` | `0.5055` | 4,380,000.00 USD | 0.00 USD | 211.25 USD | `-42.58%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,380,000.00 USD | 0.00 USD | 5,680.00 USD | `-42.24%` | `11,163.80` |
| `Live` | `Long` | `0.5095` | 4,380,000.00 USD | 0.00 USD | 195.75 USD | `-42.12%` | `384.20` |
| `Live` | `Long` | `0.5105` | 4,380,000.00 USD | 0.00 USD | 1,400.00 USD | `-42.01%` | `2,751.80` |
| `Live` | `Long` | `0.5115` | 4,380,000.00 USD | 0.00 USD | 4,120.00 USD | `-41.90%` | `8,054.90` |
| `Live` | `Long` | `0.5125` | 4,370,000.00 USD | 0.00 USD | 539.20 USD | `-41.78%` | `1,052.10` |
| `Live` | `Long` | `0.5155` | 4,370,000.00 USD | 0.00 USD | 106.04 USD | `-41.44%` | `205.70` |
| `Live` | `Long` | `0.5165` | 4,370,000.00 USD | 0.00 USD | 619.80 USD | `-41.33%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,370,000.00 USD | 0.00 USD | 213.68 USD | `-41.22%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,370,000.00 USD | 0.00 USD | 982.56 USD | `-41.10%` | `1,895.00` |
| `Live` | `Long` | `0.5205` | 4,370,000.00 USD | 0.00 USD | 439.41 USD | `-40.87%` | `844.20` |
| `Live` | `Long` | `0.5255` | 4,370,000.00 USD | 0.00 USD | 380.93 USD | `-40.31%` | `724.90` |
| `Live` | `Long` | `0.5265` | 4,370,000.00 USD | 0.00 USD | 124.73 USD | `-40.19%` | `236.90` |
| `Live` | `Long` | `0.5275` | 4,370,000.00 USD | 0.00 USD | 348.36 USD | `-40.08%` | `660.40` |
| `Live` | `Long` | `0.5295` | 4,370,000.00 USD | 0.00 USD | 123,640.00 USD | `-39.85%` | `233,498.70` |
| `Live` | `Long` | `0.5325` | 4,250,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.51%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,240,000.00 USD | 0.00 USD | 7,810.00 USD | `-39.28%` | `14,603.90` |
| `Live` | `Long` | `0.5355` | 4,240,000.00 USD | 0.00 USD | 113.47 USD | `-39.17%` | `211.90` |
| `Live` | `Long` | `0.5405` | 4,240,000.00 USD | 0.00 USD | 7,090.00 USD | `-38.60%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,230,000.00 USD | 0.00 USD | 269.13 USD | `-38.38%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,230,000.00 USD | 0.00 USD | 230.32 USD | `-38.15%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,230,000.00 USD | 0.00 USD | 6,210.00 USD | `-37.92%` | `11,362.00` |
| `Live` | `Long` | `0.5475` | 4,220,000.00 USD | 0.00 USD | 1,240.00 USD | `-37.81%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,220,000.00 USD | 0.00 USD | 29,340.00 USD | `-37.58%` | `53,392.10` |
| `Live` | `Long` | `0.5505` | 4,190,000.00 USD | 0.00 USD | 248.06 USD | `-37.47%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,190,000.00 USD | 0.00 USD | 160.93 USD | `-37.35%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,190,000.00 USD | 0.00 USD | 582.56 USD | `-37.24%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,190,000.00 USD | 0.00 USD | 271.88 USD | `-37.13%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,190,000.00 USD | 0.00 USD | 531.60 USD | `-37.01%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,190,000.00 USD | 0.00 USD | 7,950.00 USD | `-36.90%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,180,000.00 USD | 0.00 USD | 141.97 USD | `-36.56%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,180,000.00 USD | 0.00 USD | 304.93 USD | `-36.44%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,180,000.00 USD | 0.00 USD | 441.84 USD | `-36.33%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,180,000.00 USD | 0.00 USD | 330.53 USD | `-36.10%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,180,000.00 USD | 0.00 USD | 534.03 USD | `-35.99%` | `947.70` |
| `Live` | `Long` | `0.5655` | 4,180,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.76%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,170,000.00 USD | 0.00 USD | 7,200.00 USD | `-35.65%` | `12,714.00` |
| `Live` | `Long` | `0.5675` | 4,160,000.00 USD | 0.00 USD | 1,560.00 USD | `-35.54%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,160,000.00 USD | 0.00 USD | 973.22 USD | `-35.31%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,160,000.00 USD | 0.00 USD | 139.23 USD | `-34.97%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,160,000.00 USD | 0.00 USD | 182.72 USD | `-34.85%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,160,000.00 USD | 0.00 USD | 144.03 USD | `-34.74%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,160,000.00 USD | 0.00 USD | 217.37 USD | `-34.63%` | `377.70` |
| `Live` | `Long` | `0.5765` | 4,160,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.51%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,160,000.00 USD | 0.00 USD | 497.75 USD | `-34.40%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,160,000.00 USD | 0.00 USD | 141.85 USD | `-34.29%` | `245.20` |
| `Live` | `Long` | `0.5795` | 4,160,000.00 USD | 0.00 USD | 212.85 USD | `-34.17%` | `367.30` |
| `Live` | `Long` | `0.5805` | 4,160,000.00 USD | 0.00 USD | 1,410.00 USD | `-34.06%` | `2,422.00` |
| `Live` | `Long` | `0.5815` | 4,160,000.00 USD | 0.00 USD | 268.59 USD | `-33.95%` | `461.90` |
| `Live` | `Long` | `0.5825` | 4,160,000.00 USD | 0.00 USD | 6,470.00 USD | `-33.83%` | `11,099.00` |
| `Live` | `Long` | `0.5835` | 4,150,000.00 USD | 0.00 USD | 353.48 USD | `-33.72%` | `605.80` |
| `Live` | `Long` | `0.5855` | 4,150,000.00 USD | 0.00 USD | 2,640.00 USD | `-33.49%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,150,000.00 USD | 0.00 USD | 466.85 USD | `-33.38%` | `796.00` |
| `Live` | `Long` | `0.5885` | 4,150,000.00 USD | 0.00 USD | 311.14 USD | `-33.15%` | `528.70` |
| `Live` | `Long` | `0.5905` | 4,150,000.00 USD | 0.00 USD | 412.11 USD | `-32.92%` | `697.90` |
| `Live` | `Long` | `0.5925` | 4,150,000.00 USD | 0.00 USD | 994.16 USD | `-32.70%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,150,000.00 USD | 0.00 USD | 132.41 USD | `-32.58%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,150,000.00 USD | 0.00 USD | 8,220.00 USD | `-32.47%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,140,000.00 USD | 0.00 USD | 7,050.00 USD | `-32.24%` | `11,825.60` |
| `Live` | `Long` | `0.5975` | 4,130,000.00 USD | 0.00 USD | 4,360.00 USD | `-32.13%` | `7,291.60` |
| `Live` | `Long` | `0.5985` | 4,130,000.00 USD | 0.00 USD | 299.25 USD | `-32.01%` | `500.00` |
| `Live` | `Long` | `0.5995` | 4,130,000.00 USD | 0.00 USD | 4,760.00 USD | `-31.90%` | `7,936.80` |
| `Live` | `Long` | `0.6005` | 4,120,000.00 USD | 0.00 USD | 351.11 USD | `-31.79%` | `584.70` |
| `Live` | `Long` | `0.6015` | 4,120,000.00 USD | 0.00 USD | 323.79 USD | `-31.67%` | `538.30` |
| `Live` | `Long` | `0.6025` | 4,120,000.00 USD | 0.00 USD | 432.35 USD | `-31.56%` | `717.60` |
| `Live` | `Long` | `0.6035` | 4,120,000.00 USD | 0.00 USD | 1,220.00 USD | `-31.45%` | `2,023.70` |
| `Live` | `Long` | `0.6075` | 4,120,000.00 USD | 0.00 USD | 851.05 USD | `-30.99%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,120,000.00 USD | 0.00 USD | 886.10 USD | `-30.88%` | `1,456.20` |
| `Live` | `Long` | `0.6095` | 4,120,000.00 USD | 0.00 USD | 214.54 USD | `-30.76%` | `352.00` |
| `Live` | `Long` | `0.6115` | 4,120,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.54%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 4,110,000.00 USD | 0.00 USD | 438.73 USD | `-30.42%` | `716.30` |
| `Live` | `Long` | `0.6135` | 4,110,000.00 USD | 0.00 USD | 112.33 USD | `-30.31%` | `183.10` |
| `Live` | `Long` | `0.6145` | 4,110,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.20%` | `3,435.00` |
| `Live` | `Long` | `0.6155` | 4,110,000.00 USD | 0.00 USD | 935.13 USD | `-30.08%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 4,110,000.00 USD | 0.00 USD | 29,900.00 USD | `-29.97%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 4,080,000.00 USD | 0.00 USD | 4,980.00 USD | `-29.86%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 4,070,000.00 USD | 0.00 USD | 12,570.00 USD | `-29.74%` | `20,327.90` |
| `Live` | `Long` | `0.6195` | 4,060,000.00 USD | 0.00 USD | 2,400.00 USD | `-29.63%` | `3,868.00` |
| `Live` | `Long` | `0.6215` | 4,060,000.00 USD | 0.00 USD | 14,820.00 USD | `-29.40%` | `23,839.90` |
| `Live` | `Long` | `0.6225` | 4,040,000.00 USD | 0.00 USD | 90,210.00 USD | `-29.29%` | `144,922.60` |
| `Live` | `Long` | `0.6245` | 3,950,000.00 USD | 0.00 USD | 356.65 USD | `-29.06%` | `571.10` |
| `Live` | `Long` | `0.6255` | 3,950,000.00 USD | 0.00 USD | 32,630.00 USD | `-28.95%` | `52,170.80` |
| `Live` | `Long` | `0.6285` | 3,920,000.00 USD | 0.00 USD | 102.45 USD | `-28.61%` | `163.00` |
| `Live` | `Long` | `0.6295` | 3,920,000.00 USD | 0.00 USD | 1,100.00 USD | `-28.49%` | `1,739.60` |
| `Live` | `Long` | `0.6305` | 3,920,000.00 USD | 0.00 USD | 319.35 USD | `-28.38%` | `506.50` |
| `Live` | `Long` | `0.6345` | 3,920,000.00 USD | 0.00 USD | 843.00 USD | `-27.92%` | `1,328.60` |
| `Live` | `Long` | `0.6365` | 3,920,000.00 USD | 0.00 USD | 3,060.00 USD | `-27.70%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,910,000.00 USD | 0.00 USD | 1,100.00 USD | `-27.58%` | `1,726.70` |
| `Live` | `Long` | `0.6395` | 3,910,000.00 USD | 0.00 USD | 319.75 USD | `-27.36%` | `500.00` |
| `Live` | `Long` | `0.6405` | 3,910,000.00 USD | 0.00 USD | 33,040.00 USD | `-27.24%` | `51,581.80` |
| `Live` | `Long` | `0.6415` | 3,880,000.00 USD | 0.00 USD | 86,920.00 USD | `-27.13%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,790,000.00 USD | 0.00 USD | 4,980.00 USD | `-27.02%` | `7,754.70` |
| `Live` | `Long` | `0.6435` | 3,790,000.00 USD | 0.00 USD | 3,190.00 USD | `-26.90%` | `4,951.30` |
| `Live` | `Long` | `0.6445` | 3,780,000.00 USD | 0.00 USD | 65,790.00 USD | `-26.79%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,720,000.00 USD | 0.00 USD | 14,590.00 USD | `-26.68%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,700,000.00 USD | 0.00 USD | 146.76 USD | `-26.56%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,700,000.00 USD | 0.00 USD | 3,200.00 USD | `-26.45%` | `4,945.10` |
| `Live` | `Long` | `0.6485` | 3,700,000.00 USD | 0.00 USD | 668.34 USD | `-26.33%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,700,000.00 USD | 0.00 USD | 539.67 USD | `-26.22%` | `830.90` |
| `Live` | `Long` | `0.6505` | 3,700,000.00 USD | 0.00 USD | 2,340.00 USD | `-26.11%` | `3,604.50` |
| `Live` | `Long` | `0.6515` | 3,700,000.00 USD | 0.00 USD | 403,320.00 USD | `-25.99%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,290,000.00 USD | 0.00 USD | 2,350.00 USD | `-25.88%` | `3,599.00` |
| `Live` | `Long` | `0.6535` | 3,290,000.00 USD | 0.00 USD | 127,900.00 USD | `-25.77%` | `195,717.60` |
| `Live` | `Long` | `0.6545` | 3,160,000.00 USD | 0.00 USD | 6,700.00 USD | `-25.65%` | `10,231.40` |
| `Live` | `Long` | `0.6555` | 3,160,000.00 USD | 0.00 USD | 10,760.00 USD | `-25.54%` | `16,411.10` |
| `Live` | `Long` | `0.6565` | 3,150,000.00 USD | 0.00 USD | 8,220.00 USD | `-25.43%` | `12,525.80` |
| `Live` | `Long` | `0.6575` | 3,140,000.00 USD | 0.00 USD | 13,280.00 USD | `-25.31%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,120,000.00 USD | 0.00 USD | 2,970.00 USD | `-25.20%` | `4,508.30` |
| `Live` | `Long` | `0.6605` | 3,120,000.00 USD | 0.00 USD | 6,740.00 USD | `-24.97%` | `10,200.00` |
| `Live` | `Long` | `0.6615` | 3,110,000.00 USD | 0.00 USD | 325.46 USD | `-24.86%` | `492.00` |
| `Live` | `Long` | `0.6625` | 3,110,000.00 USD | 0.00 USD | 4,840.00 USD | `-24.74%` | `7,306.80` |
| `Live` | `Long` | `0.6645` | 3,110,000.00 USD | 0.00 USD | 634.00 USD | `-24.52%` | `954.10` |
| `Live` | `Long` | `0.6665` | 3,110,000.00 USD | 0.00 USD | 528.73 USD | `-24.29%` | `793.30` |
| `Live` | `Long` | `0.6675` | 3,110,000.00 USD | 0.00 USD | 3,050.00 USD | `-24.18%` | `4,574.20` |
| `Live` | `Long` | `0.6685` | 3,100,000.00 USD | 0.00 USD | 135.71 USD | `-24.06%` | `203.00` |
| `Live` | `Long` | `0.6695` | 3,100,000.00 USD | 0.00 USD | 337.36 USD | `-23.95%` | `503.90` |
| `Live` | `Long` | `0.6705` | 3,100,000.00 USD | 0.00 USD | 2,290.00 USD | `-23.84%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,100,000.00 USD | 0.00 USD | 2,240.00 USD | `-23.72%` | `3,341.20` |
| `Live` | `Long` | `0.6725` | 3,100,000.00 USD | 0.00 USD | 1,280.00 USD | `-23.61%` | `1,906.60` |
| `Live` | `Long` | `0.6735` | 3,100,000.00 USD | 0.00 USD | 633.09 USD | `-23.49%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,100,000.00 USD | 0.00 USD | 33,610.00 USD | `-23.38%` | `49,828.00` |
| `Live` | `Long` | `0.6755` | 3,060,000.00 USD | 0.00 USD | 854.64 USD | `-23.27%` | `1,265.20` |
| `Live` | `Long` | `0.6765` | 3,060,000.00 USD | 0.00 USD | 189.22 USD | `-23.15%` | `279.70` |
| `Live` | `Long` | `0.6775` | 3,060,000.00 USD | 0.00 USD | 9,350.00 USD | `-23.04%` | `13,800.00` |
| `Live` | `Long` | `0.6785` | 3,050,000.00 USD | 0.00 USD | 122.94 USD | `-22.93%` | `181.20` |
| `Live` | `Long` | `0.6795` | 3,050,000.00 USD | 0.00 USD | 43,650.00 USD | `-22.81%` | `64,238.50` |
| `Live` | `Long` | `0.6805` | 3,010,000.00 USD | 0.00 USD | 1,600.00 USD | `-22.70%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 3,010,000.00 USD | 0.00 USD | 2,110.00 USD | `-22.59%` | `3,092.70` |
| `Live` | `Long` | `0.6825` | 3,010,000.00 USD | 0.00 USD | 17,190.00 USD | `-22.47%` | `25,192.00` |
| `Live` | `Long` | `0.6835` | 2,990,000.00 USD | 0.00 USD | 15,130.00 USD | `-22.36%` | `22,136.50` |
| `Live` | `Long` | `0.6845` | 2,970,000.00 USD | 0.00 USD | 5,960.00 USD | `-22.25%` | `8,711.60` |
| `Live` | `Long` | `0.6865` | 2,970,000.00 USD | 0.00 USD | 112.59 USD | `-22.02%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,970,000.00 USD | 0.00 USD | 6,110.00 USD | `-21.90%` | `8,883.90` |
| `Live` | `Long` | `0.6885` | 2,960,000.00 USD | 0.00 USD | 1,060.00 USD | `-21.79%` | `1,536.40` |
| `Live` | `Long` | `0.6895` | 2,960,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.68%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,960,000.00 USD | 0.00 USD | 3,360.00 USD | `-21.56%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,960,000.00 USD | 0.00 USD | 10,590.00 USD | `-21.45%` | `15,317.60` |
| `Live` | `Long` | `0.6935` | 2,940,000.00 USD | 0.00 USD | 3,600.00 USD | `-21.22%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 2,940,000.00 USD | 0.00 USD | 7,670.00 USD | `-21.11%` | `11,040.00` |
| `Live` | `Long` | `0.6955` | 2,930,000.00 USD | 0.00 USD | 1,700.00 USD | `-21.00%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,930,000.00 USD | 0.00 USD | 273.03 USD | `-20.88%` | `392.00` |
| `Live` | `Long` | `0.6975` | 2,930,000.00 USD | 0.00 USD | 1,030.00 USD | `-20.77%` | `1,482.80` |
| `Live` | `Long` | `0.6985` | 2,930,000.00 USD | 0.00 USD | 1,670.00 USD | `-20.65%` | `2,396.30` |
| `Live` | `Long` | `0.7015` | 2,930,000.00 USD | 0.00 USD | 1,990.00 USD | `-20.31%` | `2,841.50` |
| `Live` | `Long` | `0.7045` | 2,930,000.00 USD | 0.00 USD | 8,970.00 USD | `-19.97%` | `12,729.60` |
| `Live` | `Long` | `0.7065` | 2,920,000.00 USD | 0.00 USD | 143.14 USD | `-19.75%` | `202.60` |
| `Live` | `Long` | `0.7075` | 2,920,000.00 USD | 0.00 USD | 3,620.00 USD | `-19.63%` | `5,122.60` |
| `Live` | `Long` | `0.7085` | 2,910,000.00 USD | 0.00 USD | 2,020.00 USD | `-19.52%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,910,000.00 USD | 0.00 USD | 1,110.00 USD | `-19.41%` | `1,568.50` |
| `Live` | `Long` | `0.7105` | 2,910,000.00 USD | 0.00 USD | 25,230.00 USD | `-19.29%` | `35,512.10` |
| `Live` | `Long` | `0.7125` | 2,890,000.00 USD | 0.00 USD | 283.22 USD | `-19.06%` | `397.50` |
| `Live` | `Long` | `0.7135` | 2,890,000.00 USD | 0.00 USD | 1,440.00 USD | `-18.95%` | `2,023.70` |
| `Live` | `Long` | `0.7145` | 2,880,000.00 USD | 0.00 USD | 297.23 USD | `-18.84%` | `416.00` |
| `Live` | `Long` | `0.7155` | 2,880,000.00 USD | 0.00 USD | 12,470.00 USD | `-18.72%` | `17,421.50` |
| `Live` | `Long` | `0.7165` | 2,870,000.00 USD | 0.00 USD | 4,620.00 USD | `-18.61%` | `6,444.00` |
| `Live` | `Long` | `0.7185` | 2,870,000.00 USD | 0.00 USD | 431,230.00 USD | `-18.38%` | `600,176.70` |
| `Live` | `Long` | `0.7195` | 2,440,000.00 USD | 0.00 USD | 420.19 USD | `-18.27%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,430,000.00 USD | 0.00 USD | 8,450.00 USD | `-18.04%` | `11,706.20` |
| `Live` | `Long` | `0.7225` | 2,430,000.00 USD | 0.00 USD | 1,420.00 USD | `-17.93%` | `1,965.70` |
| `Live` | `Long` | `0.7235` | 2,420,000.00 USD | 0.00 USD | 127.05 USD | `-17.81%` | `175.60` |
| `Live` | `Long` | `0.7245` | 2,420,000.00 USD | 0.00 USD | 2,520.00 USD | `-17.70%` | `3,475.80` |
| `Live` | `Long` | `0.7255` | 2,420,000.00 USD | 0.00 USD | 311.60 USD | `-17.59%` | `429.50` |
| `Live` | `Long` | `0.7265` | 2,420,000.00 USD | 0.00 USD | 3,410.00 USD | `-17.47%` | `4,687.00` |
| `Live` | `Long` | `0.7275` | 2,420,000.00 USD | 0.00 USD | 36,540.00 USD | `-17.36%` | `50,227.70` |
| `Live` | `Long` | `0.7285` | 2,380,000.00 USD | 0.00 USD | 8,840.00 USD | `-17.25%` | `12,129.10` |
| `Live` | `Long` | `0.7295` | 2,370,000.00 USD | 0.00 USD | 3,990.00 USD | `-17.13%` | `5,465.30` |
| `Live` | `Long` | `0.7305` | 2,370,000.00 USD | 0.00 USD | 119.88 USD | `-17.02%` | `164.10` |
| `Live` | `Long` | `0.7325` | 2,370,000.00 USD | 0.00 USD | 13,500.00 USD | `-16.79%` | `18,432.50` |
| `Live` | `Long` | `0.7335` | 2,360,000.00 USD | 0.00 USD | 12,160.00 USD | `-16.68%` | `16,573.90` |
| `Live` | `Long` | `0.7345` | 2,340,000.00 USD | 0.00 USD | 2,340.00 USD | `-16.57%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,340,000.00 USD | 0.00 USD | 51,920.00 USD | `-16.45%` | `70,595.50` |
| `Live` | `Long` | `0.7375` | 2,290,000.00 USD | 0.00 USD | 3,450.00 USD | `-16.22%` | `4,683.00` |
| `Live` | `Long` | `0.7385` | 2,290,000.00 USD | 0.00 USD | 6,020.00 USD | `-16.11%` | `8,146.50` |
| `Live` | `Long` | `0.7395` | 2,280,000.00 USD | 0.00 USD | 3,380.00 USD | `-16.00%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,280,000.00 USD | 0.00 USD | 3,530.00 USD | `-15.88%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,270,000.00 USD | 0.00 USD | 382.61 USD | `-15.77%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,270,000.00 USD | 0.00 USD | 2,280.00 USD | `-15.66%` | `3,074.90` |
| `Live` | `Long` | `0.7435` | 2,270,000.00 USD | 0.00 USD | 784,400.00 USD | `-15.54%` | `1,055,008.20` |
| `Live` | `Long` | `0.7455` | 1,490,000.00 USD | 0.00 USD | 2,160.00 USD | `-15.32%` | `2,892.60` |
| `Live` | `Long` | `0.7465` | 1,480,000.00 USD | 0.00 USD | 359.96 USD | `-15.20%` | `482.20` |
| `Live` | `Long` | `0.7475` | 1,480,000.00 USD | 0.00 USD | 107,260.00 USD | `-15.09%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,380,000.00 USD | 0.00 USD | 599.60 USD | `-14.86%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,380,000.00 USD | 0.00 USD | 1,210.00 USD | `-14.63%` | `1,613.50` |
| `Live` | `Long` | `0.7535` | 1,370,000.00 USD | 0.00 USD | 264.86 USD | `-14.41%` | `351.50` |
| `Live` | `Long` | `0.7545` | 1,370,000.00 USD | 0.00 USD | 1,250.00 USD | `-14.29%` | `1,650.60` |
| `Live` | `Long` | `0.7555` | 1,370,000.00 USD | 0.00 USD | 1,750.00 USD | `-14.18%` | `2,315.50` |
| `Live` | `Long` | `0.7575` | 1,370,000.00 USD | 0.00 USD | 1,900.00 USD | `-13.95%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,370,000.00 USD | 0.00 USD | 40,520.00 USD | `-13.84%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,330,000.00 USD | 0.00 USD | 4,900.00 USD | `-13.73%` | `6,448.30` |
| `Live` | `Long` | `0.7615` | 1,320,000.00 USD | 0.00 USD | 351.43 USD | `-13.50%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,320,000.00 USD | 0.00 USD | 3,790.00 USD | `-13.38%` | `4,966.90` |
| `Live` | `Long` | `0.7635` | 1,320,000.00 USD | 0.00 USD | 5,550.00 USD | `-13.27%` | `7,271.90` |
| `Live` | `Long` | `0.7645` | 1,310,000.00 USD | 0.00 USD | 3,510.00 USD | `-13.16%` | `4,596.60` |
| `Live` | `Long` | `0.7655` | 1,310,000.00 USD | 0.00 USD | 4,430.00 USD | `-13.04%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,310,000.00 USD | 0.00 USD | 1,260.00 USD | `-12.93%` | `1,649.10` |
| `Live` | `Long` | `0.7675` | 1,300,000.00 USD | 0.00 USD | 25,580.00 USD | `-12.82%` | `33,323.60` |
| `Live` | `Long` | `0.7685` | 1,280,000.00 USD | 0.00 USD | 207.19 USD | `-12.70%` | `269.60` |
| `Live` | `Long` | `0.7695` | 1,280,000.00 USD | 0.00 USD | 150,510.00 USD | `-12.59%` | `195,593.50` |
| `Live` | `Long` | `0.7705` | 1,130,000.00 USD | 0.00 USD | 5,640.00 USD | `-12.48%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 1,120,000.00 USD | 0.00 USD | 19,250.00 USD | `-12.36%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 1,100,000.00 USD | 0.00 USD | 1,940.00 USD | `-12.25%` | `2,515.50` |
| `Live` | `Long` | `0.7735` | 1,100,000.00 USD | 0.00 USD | 5,230.00 USD | `-12.14%` | `6,756.40` |
| `Live` | `Long` | `0.7755` | 1,100,000.00 USD | 0.00 USD | 3,430.00 USD | `-11.91%` | `4,424.80` |
| `Live` | `Long` | `0.7765` | 1,090,000.00 USD | 0.00 USD | 3,510.00 USD | `-11.79%` | `4,518.50` |
| `Live` | `Long` | `0.7775` | 1,090,000.00 USD | 0.00 USD | 321,490.00 USD | `-11.68%` | `413,488.90` |
| `Live` | `Long` | `0.7785` | 767,850.00 USD | 0.00 USD | 28,010.00 USD | `-11.57%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 739,840.00 USD | 0.00 USD | 338.69 USD | `-11.45%` | `434.50` |
| `Live` | `Long` | `0.7815` | 739,500.00 USD | 0.00 USD | 4,160.00 USD | `-11.23%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 735,340.00 USD | 0.00 USD | 21,600.00 USD | `-11.00%` | `27,572.80` |
| `Live` | `Long` | `0.7845` | 713,740.00 USD | 0.00 USD | 155.96 USD | `-10.89%` | `198.80` |
| `Live` | `Long` | `0.7865` | 713,580.00 USD | 0.00 USD | 3,470.00 USD | `-10.66%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 710,110.00 USD | 0.00 USD | 288.70 USD | `-10.54%` | `366.60` |
| `Live` | `Long` | `0.7905` | 709,820.00 USD | 0.00 USD | 3,670.00 USD | `-10.20%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 706,150.00 USD | 0.00 USD | 7,620.00 USD | `-10.09%` | `9,623.00` |
| `Live` | `Long` | `0.7925` | 698,540.00 USD | 0.00 USD | 10,810.00 USD | `-9.98%` | `13,636.90` |
| `Live` | `Long` | `0.7935` | 687,730.00 USD | 0.00 USD | 809.45 USD | `-9.86%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 686,920.00 USD | 0.00 USD | 736.66 USD | `-9.75%` | `927.20` |
| `Live` | `Long` | `0.7955` | 686,180.00 USD | 0.00 USD | 53,850.00 USD | `-9.64%` | `67,697.90` |
| `Live` | `Long` | `0.7965` | 632,330.00 USD | 0.00 USD | 12,980.00 USD | `-9.52%` | `16,300.50` |
| `Live` | `Long` | `0.7975` | 619,350.00 USD | 0.00 USD | 7,580.00 USD | `-9.41%` | `9,508.60` |
| `Live` | `Long` | `0.7985` | 611,760.00 USD | 0.00 USD | 40,230.00 USD | `-9.30%` | `50,386.80` |
| `Live` | `Long` | `0.7995` | 571,530.00 USD | 0.00 USD | 10,050.00 USD | `-9.18%` | `12,576.50` |
| `Live` | `Long` | `0.8005` | 561,470.00 USD | 0.00 USD | 3,850.00 USD | `-9.07%` | `4,809.40` |
| `Live` | `Long` | `0.8015` | 557,620.00 USD | 0.00 USD | 7,610.00 USD | `-8.95%` | `9,500.20` |
| `Live` | `Long` | `0.8025` | 550,010.00 USD | 0.00 USD | 1,350.00 USD | `-8.84%` | `1,686.70` |
| `Live` | `Long` | `0.8035` | 548,660.00 USD | 0.00 USD | 7,680.00 USD | `-8.73%` | `9,559.90` |
| `Live` | `Long` | `0.8045` | 540,980.00 USD | 0.00 USD | 16,660.00 USD | `-8.61%` | `20,710.00` |
| `Live` | `Long` | `0.8055` | 524,310.00 USD | 0.00 USD | 361.11 USD | `-8.50%` | `448.30` |
| `Live` | `Long` | `0.8065` | 523,950.00 USD | 0.00 USD | 6,910.00 USD | `-8.39%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 517,040.00 USD | 0.00 USD | 2,770.00 USD | `-8.27%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 514,270.00 USD | 0.00 USD | 22,510.00 USD | `-8.16%` | `27,845.30` |
| `Live` | `Long` | `0.8095` | 491,760.00 USD | 0.00 USD | 130,110.00 USD | `-8.05%` | `160,732.40` |
| `Live` | `Long` | `0.8105` | 361,650.00 USD | 0.00 USD | 2,430.00 USD | `-7.93%` | `3,000.50` |
| `Live` | `Long` | `0.8115` | 359,220.00 USD | 0.00 USD | 2,970.00 USD | `-7.82%` | `3,654.30` |
| `Live` | `Long` | `0.8125` | 356,250.00 USD | 0.00 USD | 1,160.00 USD | `-7.71%` | `1,421.60` |
| `Live` | `Long` | `0.8135` | 355,100.00 USD | 0.00 USD | 3,800.00 USD | `-7.59%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 351,290.00 USD | 0.00 USD | 277.42 USD | `-7.48%` | `340.60` |
| `Live` | `Long` | `0.8155` | 351,010.00 USD | 0.00 USD | 38,250.00 USD | `-7.36%` | `46,908.50` |
| `Live` | `Long` | `0.8165` | 312,760.00 USD | 0.00 USD | 492.27 USD | `-7.25%` | `602.90` |
| `Live` | `Long` | `0.8175` | 312,270.00 USD | 0.00 USD | 77,840.00 USD | `-7.14%` | `95,214.30` |
| `Live` | `Long` | `0.8185` | 234,430.00 USD | 0.00 USD | 28,030.00 USD | `-7.02%` | `34,240.00` |
| `Live` | `Long` | `0.8195` | 206,410.00 USD | 0.00 USD | 1,110.00 USD | `-6.91%` | `1,360.00` |
| `Live` | `Long` | `0.8205` | 205,290.00 USD | 0.00 USD | 9,370.00 USD | `-6.80%` | `11,414.00` |
| `Live` | `Long` | `0.8215` | 195,930.00 USD | 0.00 USD | 474.01 USD | `-6.68%` | `577.00` |
| `Live` | `Long` | `0.8225` | 195,450.00 USD | 0.00 USD | 3,080.00 USD | `-6.57%` | `3,747.80` |
| `Live` | `Long` | `0.8235` | 192,370.00 USD | 0.00 USD | 463.63 USD | `-6.46%` | `563.00` |
| `Live` | `Long` | `0.8245` | 191,910.00 USD | 0.00 USD | 18,980.00 USD | `-6.34%` | `23,022.60` |
| `Live` | `Long` | `0.8255` | 172,920.00 USD | 0.00 USD | 1,580.00 USD | `-6.23%` | `1,911.90` |
| `Live` | `Long` | `0.8275` | 171,340.00 USD | 0.00 USD | 4,690.00 USD | `-6.00%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 166,660.00 USD | 0.00 USD | 120,070.00 USD | `-5.89%` | `144,926.90` |
| `Live` | `Long` | `0.8295` | 46,590.00 USD | 0.00 USD | 46,590.00 USD | `-5.77%` | `56,161.30` |
| `Live` | `Short` | `0.8395` | 190.31 USD | 190.31 USD | 0.00 USD | `-4.64%` | `226.70` |
| `Live` | `Short` | `0.8885` | 512.93 USD | 322.61 USD | 0.00 USD | `+0.93%` | `363.10` |
| `Live` | `Short` | `0.8925` | 1,320.00 USD | 807.44 USD | 0.00 USD | `+1.38%` | `904.70` |
| `Live` | `Short` | `0.8935` | 3,840.00 USD | 2,520.00 USD | 0.00 USD | `+1.50%` | `2,815.00` |
| `Live` | `Short` | `0.8965` | 4,020.00 USD | 187.46 USD | 0.00 USD | `+1.84%` | `209.10` |
| `Live` | `Short` | `0.9145` | 8,090.00 USD | 4,060.00 USD | 0.00 USD | `+3.88%` | `4,444.10` |
| `Live` | `Short` | `0.9175` | 11,000.00 USD | 2,910.00 USD | 0.00 USD | `+4.22%` | `3,170.30` |
| `Live` | `Short` | `0.9305` | 15,210.00 USD | 4,210.00 USD | 0.00 USD | `+5.70%` | `4,523.60` |
| `Live` | `Short` | `0.9325` | 15,730.00 USD | 523.13 USD | 0.00 USD | `+5.93%` | `561.00` |
| `Live` | `Short` | `0.9385` | 55,570.00 USD | 39,850.00 USD | 0.00 USD | `+6.61%` | `42,456.90` |
| `Live` | `Short` | `0.9805` | 56,620.00 USD | 1,050.00 USD | 0.00 USD | `+11.38%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 56,990.00 USD | 365.70 USD | 0.00 USD | `+12.06%` | `370.70` |
| `Live` | `Short` | `0.9885` | 61,240.00 USD | 4,250.00 USD | 0.00 USD | `+12.29%` | `4,304.30` |
| `Live` | `Short` | `0.9905` | 62,810.00 USD | 1,570.00 USD | 0.00 USD | `+12.51%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 62,950.00 USD | 139.59 USD | 0.00 USD | `+12.86%` | `140.50` |
| `Live` | `Short` | `1.00` | 63,280.00 USD | 330.29 USD | 0.00 USD | `+13.76%` | `329.80` |
| `Live` | `Short` | `1.01` | 63,380.00 USD | 100.65 USD | 0.00 USD | `+14.33%` | `100.00` |
| `Live` | `Short` | `1.01` | 64,090.00 USD | 705.99 USD | 0.00 USD | `+15.24%` | `695.90` |
| `Live` | `Short` | `1.02` | 64,260.00 USD | 170.40 USD | 0.00 USD | `+15.35%` | `167.80` |
| `Live` | `Short` | `1.02` | 65,930.00 USD | 1,670.00 USD | 0.00 USD | `+15.70%` | `1,639.00` |
| `Live` | `Short` | `1.04` | 66,090.00 USD | 155.92 USD | 0.00 USD | `+18.08%` | `150.00` |
| `Live` | `Short` | `1.05` | 66,680.00 USD | 597.52 USD | 0.00 USD | `+19.33%` | `568.80` |
| `Live` | `Short` | `1.05` | 69,070.00 USD | 2,390.00 USD | 0.00 USD | `+19.44%` | `2,272.10` |
| `Live` | `Short` | `1.08` | 72,650.00 USD | 3,580.00 USD | 0.00 USD | `+22.74%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 78,210.00 USD | 5,550.00 USD | 0.00 USD | `+23.76%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 78,530.00 USD | 324.90 USD | 0.00 USD | `+24.90%` | `295.50` |
| `Live` | `Short` | `1.10` | 78,810.00 USD | 277.22 USD | 0.00 USD | `+25.01%` | `251.90` |
| `Live` | `Short` | `1.10` | 80,110.00 USD | 1,310.00 USD | 0.00 USD | `+25.46%` | `1,182.10` |
| `Live` | `Short` | `1.11` | 89,050.00 USD | 8,940.00 USD | 0.00 USD | `+26.15%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 112,360.00 USD | 23,310.00 USD | 0.00 USD | `+27.96%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 112,990.00 USD | 634.09 USD | 0.00 USD | `+28.64%` | `559.90` |
| `Live` | `Short` | `1.20` | 113,170.00 USD | 177.65 USD | 0.00 USD | `+36.26%` | `148.10` |
| `Live` | `Short` | `1.22` | 117,620.00 USD | 4,440.00 USD | 0.00 USD | `+38.41%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 118,000.00 USD | 383.01 USD | 0.00 USD | `+38.87%` | `313.30` |
| `Live` | `Short` | `1.23` | 118,380.00 USD | 380.84 USD | 0.00 USD | `+40.23%` | `308.50` |
| `Live` | `Short` | `1.24` | 122,300.00 USD | 3,930.00 USD | 0.00 USD | `+40.69%` | `3,169.40` |
| `Live` | `Short` | `1.24` | 123,530.00 USD | 1,230.00 USD | 0.00 USD | `+40.91%` | `989.90` |
| `Live` | `Short` | `1.26` | 126,200.00 USD | 2,670.00 USD | 0.00 USD | `+43.07%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 128,510.00 USD | 2,300.00 USD | 0.00 USD | `+45.12%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 168,390.00 USD | 39,880.00 USD | 0.00 USD | `+45.68%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 178,200.00 USD | 9,820.00 USD | 0.00 USD | `+46.37%` | `7,618.00` |
| `Live` | `Short` | `1.29` | 178,430.00 USD | 226.80 USD | 0.00 USD | `+47.05%` | `175.20` |
| `Live` | `Short` | `1.30` | 178,550.00 USD | 114.40 USD | 0.00 USD | `+47.50%` | `88.10` |
| `Live` | `Short` | `1.31` | 179,560.00 USD | 1,020.00 USD | 0.00 USD | `+48.75%` | `777.20` |
| `Live` | `Short` | `1.31` | 211,090.00 USD | 31,530.00 USD | 0.00 USD | `+48.98%` | `24,042.40` |
| `Live` | `Short` | `1.32` | 211,320.00 USD | 229.23 USD | 0.00 USD | `+50.34%` | `173.20` |
| `Live` | `Short` | `1.33` | 217,660.00 USD | 6,340.00 USD | 0.00 USD | `+50.57%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 239,630.00 USD | 21,970.00 USD | 0.00 USD | `+50.91%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 246,490.00 USD | 6,860.00 USD | 0.00 USD | `+52.16%` | `5,119.30` |
| `Live` | `Short` | `1.34` | 247,590.00 USD | 1,110.00 USD | 0.00 USD | `+52.39%` | `826.40` |
| `Live` | `Short` | `1.35` | 270,360.00 USD | 22,760.00 USD | 0.00 USD | `+53.75%` | `16,816.80` |
| `Live` | `Short` | `1.37` | 628,640.00 USD | 358,280.00 USD | 0.00 USD | `+55.91%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 633,080.00 USD | 4,450.00 USD | 0.00 USD | `+60.68%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 633,490.00 USD | 402.08 USD | 0.00 USD | `+63.18%` | `279.90` |
| `Live` | `Short` | `1.44` | 633,770.00 USD | 288.68 USD | 0.00 USD | `+63.63%` | `200.40` |
| `Live` | `Short` | `1.45` | 633,920.00 USD | 142.05 USD | 0.00 USD | `+64.31%` | `98.20` |
| `Live` | `Short` | `1.50` | 650,700.00 USD | 16,780.00 USD | 0.00 USD | `+70.45%` | `11,182.60` |
| `Live` | `Short` | `1.51` | 654,720.00 USD | 4,020.00 USD | 0.00 USD | `+72.04%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 654,870.00 USD | 152.85 USD | 0.00 USD | `+73.63%` | `100.00` |
| `Live` | `Short` | `1.53` | 664,800.00 USD | 9,930.00 USD | 0.00 USD | `+73.86%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 664,950.00 USD | 144.34 USD | 0.00 USD | `+74.42%` | `94.00` |
| `Live` | `Short` | `1.58` | 665,230.00 USD | 285.21 USD | 0.00 USD | `+79.19%` | `180.80` |
| `Live` | `Short` | `1.59` | 666,420.00 USD | 1,180.00 USD | 0.00 USD | `+81.01%` | `743.20` |
| `Live` | `Short` | `1.60` | 666,540.00 USD | 123.81 USD | 0.00 USD | `+81.47%` | `77.50` |
| `Live` | `Short` | `1.60` | 666,680.00 USD | 135.24 USD | 0.00 USD | `+81.81%` | `84.50` |
| `Live` | `Short` | `1.60` | 667,810.00 USD | 1,130.00 USD | 0.00 USD | `+82.03%` | `704.60` |
| `Live` | `Short` | `1.65` | 689,140.00 USD | 21,330.00 USD | 0.00 USD | `+87.03%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 693,080.00 USD | 3,940.00 USD | 0.00 USD | `+87.83%` | `2,381.50` |
| `Live` | `Short` | `1.66` | 696,700.00 USD | 3,620.00 USD | 0.00 USD | `+88.51%` | `2,184.10` |
| `Live` | `Short` | `1.66` | 735,800.00 USD | 39,090.00 USD | 0.00 USD | `+88.74%` | `23,529.40` |
| `Live` | `Short` | `1.66` | 1,030,000.00 USD | 290,220.00 USD | 0.00 USD | `+89.08%` | `174,360.10` |
| `Live` | `Short` | `1.69` | 1,030,000.00 USD | 150.02 USD | 0.00 USD | `+91.69%` | `88.90` |
| `Live` | `Short` | `1.71` | 1,030,000.00 USD | 205.67 USD | 0.00 USD | `+94.53%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,040,000.00 USD | 9,700.00 USD | 0.00 USD | `+95.10%` | `5,645.40` |
| `Live` | `Short` | `1.72` | 1,040,000.00 USD | 492.06 USD | 0.00 USD | `+95.78%` | `285.50` |
| `Live` | `Short` | `1.73` | 1,040,000.00 USD | 226.05 USD | 0.00 USD | `+96.91%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,040,000.00 USD | 2,080.00 USD | 0.00 USD | `+97.82%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 1,040,000.00 USD | 983.07 USD | 0.00 USD | `+98.28%` | `563.20` |
| `Live` | `Short` | `1.75` | 1,050,000.00 USD | 7,000.00 USD | 0.00 USD | `+98.85%` | `4,000.00` |
| `Live` | `Short` | `1.75` | 1,070,000.00 USD | 19,920.00 USD | 0.00 USD | `+98.96%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 1,080,000.00 USD | 11,350.00 USD | 0.00 USD | `+99.19%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,080,000.00 USD | 1,520.00 USD | 0.00 USD | `+99.30%` | `868.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,200,000.00 USD | 0.00 USD | 497.31 USD | `-70.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2745` | 1,200,000.00 USD | 0.00 USD | 455.97 USD | `-68.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,200,000.00 USD | 0.00 USD | 102.75 USD | `-61.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,200,000.00 USD | 0.00 USD | 256.78 USD | `-60.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,200,000.00 USD | 0.00 USD | 428.87 USD | `-55.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,200,000.00 USD | 0.00 USD | 123.45 USD | `-53.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,200,000.00 USD | 0.00 USD | 818.15 USD | `-52.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,190,000.00 USD | 0.00 USD | 436.41 USD | `-50.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,190,000.00 USD | 0.00 USD | 876.79 USD | `-50.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,190,000.00 USD | 0.00 USD | 466.72 USD | `-48.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,190,000.00 USD | 0.00 USD | 142.95 USD | `-45.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,190,000.00 USD | 0.00 USD | 3,010.00 USD | `-43.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,190,000.00 USD | 0.00 USD | 151.74 USD | `-41.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,190,000.00 USD | 0.00 USD | 123.91 USD | `-41.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,190,000.00 USD | 0.00 USD | 219.80 USD | `-37.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,190,000.00 USD | 0.00 USD | 237,400.00 USD | `-37.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 951,780.00 USD | 0.00 USD | 276.75 USD | `-37.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 951,510.00 USD | 0.00 USD | 1,680.00 USD | `-36.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 949,820.00 USD | 0.00 USD | 853.41 USD | `-35.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 948,970.00 USD | 0.00 USD | 119.76 USD | `-34.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 948,850.00 USD | 0.00 USD | 3,520.00 USD | `-33.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 945,330.00 USD | 0.00 USD | 470.62 USD | `-32.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 944,860.00 USD | 0.00 USD | 108.39 USD | `-31.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 944,750.00 USD | 0.00 USD | 123.28 USD | `-31.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 944,620.00 USD | 0.00 USD | 488.52 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 944,140.00 USD | 0.00 USD | 4,230.00 USD | `-28.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 939,910.00 USD | 0.00 USD | 242.24 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 939,670.00 USD | 0.00 USD | 193.95 USD | `-26.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 939,470.00 USD | 0.00 USD | 149.22 USD | `-26.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 939,320.00 USD | 0.00 USD | 158.54 USD | `-25.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 939,170.00 USD | 0.00 USD | 195.47 USD | `-25.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 938,970.00 USD | 0.00 USD | 112.91 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 938,860.00 USD | 0.00 USD | 181.31 USD | `-24.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 938,680.00 USD | 0.00 USD | 190.25 USD | `-24.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 938,490.00 USD | 0.00 USD | 153.53 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 938,330.00 USD | 0.00 USD | 52,450.00 USD | `-23.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 885,880.00 USD | 0.00 USD | 536.11 USD | `-23.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 885,350.00 USD | 0.00 USD | 918.68 USD | `-22.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 884,430.00 USD | 0.00 USD | 340.75 USD | `-22.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 884,090.00 USD | 0.00 USD | 9,270.00 USD | `-21.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 874,820.00 USD | 0.00 USD | 120.53 USD | `-21.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 874,700.00 USD | 0.00 USD | 160.71 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 874,540.00 USD | 0.00 USD | 738.08 USD | `-20.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 873,800.00 USD | 0.00 USD | 187.61 USD | `-20.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 873,620.00 USD | 0.00 USD | 8,500.00 USD | `-20.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 865,120.00 USD | 0.00 USD | 89,150.00 USD | `-20.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 775,970.00 USD | 0.00 USD | 189.06 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 775,780.00 USD | 0.00 USD | 5,650.00 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 770,130.00 USD | 0.00 USD | 371.68 USD | `-19.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 769,760.00 USD | 0.00 USD | 152.05 USD | `-19.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 769,610.00 USD | 0.00 USD | 123.41 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 769,480.00 USD | 0.00 USD | 745.54 USD | `-17.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 768,740.00 USD | 0.00 USD | 1,130.00 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 767,600.00 USD | 0.00 USD | 18,770.00 USD | `-16.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 748,830.00 USD | 0.00 USD | 7,970.00 USD | `-16.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 740,870.00 USD | 0.00 USD | 257.26 USD | `-16.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 740,610.00 USD | 0.00 USD | 161.72 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 740,450.00 USD | 0.00 USD | 1,590.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 738,850.00 USD | 0.00 USD | 10,160.00 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 728,700.00 USD | 0.00 USD | 94,190.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 634,500.00 USD | 0.00 USD | 1,230.00 USD | `-14.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 633,280.00 USD | 0.00 USD | 1,840.00 USD | `-13.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 631,440.00 USD | 0.00 USD | 804.61 USD | `-13.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 630,630.00 USD | 0.00 USD | 590.68 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 630,040.00 USD | 0.00 USD | 635.62 USD | `-13.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 629,410.00 USD | 0.00 USD | 191.12 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 629,220.00 USD | 0.00 USD | 273.92 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 628,940.00 USD | 0.00 USD | 125.92 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 628,820.00 USD | 0.00 USD | 1,980.00 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 626,840.00 USD | 0.00 USD | 1,150.00 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 625,690.00 USD | 0.00 USD | 1,500.00 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 624,190.00 USD | 0.00 USD | 1,860.00 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 622,340.00 USD | 0.00 USD | 128.47 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 622,210.00 USD | 0.00 USD | 6,960.00 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 615,250.00 USD | 0.00 USD | 135.11 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 615,110.00 USD | 0.00 USD | 8,870.00 USD | `-10.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 606,250.00 USD | 0.00 USD | 1,500.00 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7935` | 604,750.00 USD | 0.00 USD | 1,290.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 603,460.00 USD | 0.00 USD | 23,420.00 USD | `-9.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 580,040.00 USD | 0.00 USD | 103.42 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 579,930.00 USD | 0.00 USD | 1,260.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 578,680.00 USD | 0.00 USD | 319.40 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 578,360.00 USD | 0.00 USD | 4,740.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 573,620.00 USD | 0.00 USD | 1,800.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 571,820.00 USD | 0.00 USD | 144.67 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 571,680.00 USD | 0.00 USD | 1,510.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 570,160.00 USD | 0.00 USD | 50,540.00 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 519,630.00 USD | 0.00 USD | 263.25 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 519,370.00 USD | 0.00 USD | 1,250.00 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8095` | 518,120.00 USD | 0.00 USD | 218.32 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 517,900.00 USD | 0.00 USD | 181,850.00 USD | `-7.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 336,050.00 USD | 0.00 USD | 353.81 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 335,690.00 USD | 0.00 USD | 1,010.00 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 334,680.00 USD | 0.00 USD | 123,350.00 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 211,330.00 USD | 0.00 USD | 1,160.00 USD | `-7.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 210,170.00 USD | 0.00 USD | 216.70 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 209,950.00 USD | 0.00 USD | 125.72 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 209,830.00 USD | 0.00 USD | 375.49 USD | `-6.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 209,450.00 USD | 0.00 USD | 13,790.00 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 195,660.00 USD | 0.00 USD | 7,160.00 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 188,500.00 USD | 0.00 USD | 226.71 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 188,280.00 USD | 0.00 USD | 3,780.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 184,500.00 USD | 0.00 USD | 1,320.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 183,180.00 USD | 0.00 USD | 325.56 USD | `-6.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 182,850.00 USD | 0.00 USD | 666.55 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 182,180.00 USD | 0.00 USD | 577.25 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 181,610.00 USD | 0.00 USD | 3,950.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 177,650.00 USD | 0.00 USD | 171.46 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 177,480.00 USD | 0.00 USD | 7,920.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 169,560.00 USD | 0.00 USD | 690.30 USD | `-5.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 168,870.00 USD | 0.00 USD | 144.54 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 168,730.00 USD | 0.00 USD | 263.43 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 168,460.00 USD | 0.00 USD | 610.23 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 167,850.00 USD | 0.00 USD | 699.65 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 167,150.00 USD | 0.00 USD | 320.31 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 166,830.00 USD | 0.00 USD | 240.52 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 166,590.00 USD | 0.00 USD | 388.23 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 166,210.00 USD | 0.00 USD | 3,040.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 163,160.00 USD | 0.00 USD | 510.57 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 162,650.00 USD | 0.00 USD | 212.81 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 162,440.00 USD | 0.00 USD | 2,530.00 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 159,910.00 USD | 0.00 USD | 12,850.00 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 147,050.00 USD | 0.00 USD | 481.80 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 146,570.00 USD | 0.00 USD | 1,330.00 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 145,250.00 USD | 0.00 USD | 25,350.00 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8525` | 119,900.00 USD | 0.00 USD | 7,700.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 112,200.00 USD | 0.00 USD | 345.13 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 111,850.00 USD | 0.00 USD | 1,420.00 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 110,430.00 USD | 0.00 USD | 1,470.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 108,960.00 USD | 0.00 USD | 105.30 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 108,860.00 USD | 0.00 USD | 8,900.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 99,950.00 USD | 0.00 USD | 1,740.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 98,210.00 USD | 0.00 USD | 3,880.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 94,330.00 USD | 0.00 USD | 6,160.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 88,170.00 USD | 0.00 USD | 1,960.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 86,210.00 USD | 0.00 USD | 2,590.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 83,620.00 USD | 0.00 USD | 2,420.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 81,210.00 USD | 0.00 USD | 3,310.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 77,890.00 USD | 0.00 USD | 6,910.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 70,990.00 USD | 0.00 USD | 3,020.00 USD | `-1.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 67,970.00 USD | 0.00 USD | 410.11 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 67,560.00 USD | 0.00 USD | 5,340.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 62,220.00 USD | 0.00 USD | 11,960.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 50,260.00 USD | 0.00 USD | 712.45 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 49,550.00 USD | 0.00 USD | 1,500.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 48,050.00 USD | 0.00 USD | 314.55 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 47,740.00 USD | 0.00 USD | 866.37 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 46,870.00 USD | 0.00 USD | 35,020.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 11,850.00 USD | 0.00 USD | 635.29 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 11,220.00 USD | 0.00 USD | 9,070.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 2,150.00 USD | 0.00 USD | 151.10 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 2,000.00 USD | 0.00 USD | 2,000.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8805` | 1,030.00 USD | 1,030.00 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8815` | 5,100.00 USD | 4,070.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8825` | 5,660.00 USD | 563.65 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8835` | 6,090.00 USD | 425.94 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 10,300.00 USD | 4,210.00 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 13,900.00 USD | 3,600.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 14,140.00 USD | 235.54 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 25,500.00 USD | 11,360.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 34,280.00 USD | 8,780.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 34,430.00 USD | 152.36 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 34,900.00 USD | 469.91 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 45,510.00 USD | 10,610.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 45,790.00 USD | 277.07 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 45,890.00 USD | 100.09 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 49,280.00 USD | 3,390.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 49,570.00 USD | 289.12 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 67,780.00 USD | 18,210.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 68,660.00 USD | 889.43 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 97,630.00 USD | 28,960.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 99,250.00 USD | 1,620.00 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 101,300.00 USD | 2,050.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 102,230.00 USD | 926.06 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 102,420.00 USD | 188.92 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 105,370.00 USD | 2,950.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 107,360.00 USD | 1,990.00 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 107,500.00 USD | 138.69 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 107,750.00 USD | 250.83 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 108,850.00 USD | 1,090.00 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 110,370.00 USD | 1,520.00 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 111,300.00 USD | 933.08 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 111,560.00 USD | 260.23 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 114,450.00 USD | 2,890.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 117,480.00 USD | 3,020.00 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 120,550.00 USD | 3,070.00 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 121,120.00 USD | 570.08 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 121,430.00 USD | 309.14 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 125,330.00 USD | 3,900.00 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 127,300.00 USD | 1,970.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 127,420.00 USD | 116.59 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 386,540.00 USD | 259,120.00 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 538,500.00 USD | 151,960.00 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 543,570.00 USD | 5,070.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 544,070.00 USD | 495.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 545,470.00 USD | 1,400.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 550,350.00 USD | 4,880.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 552,550.00 USD | 2,200.00 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 552,840.00 USD | 287.62 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 553,040.00 USD | 199.16 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 553,170.00 USD | 130.59 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 553,620.00 USD | 448.69 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 553,740.00 USD | 120.16 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 554,770.00 USD | 1,030.00 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 555,340.00 USD | 568.87 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 555,630.00 USD | 292.78 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 556,150.00 USD | 523.79 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 556,850.00 USD | 701.16 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 556,960.00 USD | 104.53 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 610,020.00 USD | 53,060.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 613,930.00 USD | 3,910.00 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 622,890.00 USD | 8,960.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 623,420.00 USD | 529.50 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 623,720.00 USD | 301.79 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 625,420.00 USD | 1,700.00 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 626,210.00 USD | 789.04 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 634,770.00 USD | 8,560.00 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 635,830.00 USD | 1,050.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 636,670.00 USD | 848.20 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 655,790.00 USD | 19,120.00 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 656,060.00 USD | 261.97 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 660,280.00 USD | 4,220.00 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 660,440.00 USD | 159.19 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 670,350.00 USD | 9,910.00 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 673,490.00 USD | 3,150.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 674,930.00 USD | 1,440.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 677,820.00 USD | 2,890.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 678,950.00 USD | 1,130.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 679,070.00 USD | 121.54 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 679,230.00 USD | 155.06 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 731,730.00 USD | 52,510.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 731,890.00 USD | 161.82 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 751,300.00 USD | 19,400.00 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 751,560.00 USD | 259.86 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 752,890.00 USD | 1,340.00 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 753,370.00 USD | 476.57 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 753,900.00 USD | 531.57 USD | 0.00 USD | `+9.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 757,060.00 USD | 3,160.00 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 758,060.00 USD | 993.78 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 758,270.00 USD | 212.90 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 769,950.00 USD | 11,680.00 USD | 0.00 USD | `+10.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 770,070.00 USD | 125.61 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 770,510.00 USD | 441.51 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 780,700.00 USD | 10,190.00 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 780,950.00 USD | 253.14 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 785,160.00 USD | 4,200.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 785,330.00 USD | 176.73 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 785,850.00 USD | 513.32 USD | 0.00 USD | `+11.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 821,210.00 USD | 35,360.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 853,060.00 USD | 31,850.00 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 857,850.00 USD | 4,800.00 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 858,410.00 USD | 558.35 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 859,480.00 USD | 1,060.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 860,660.00 USD | 1,180.00 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 861,150.00 USD | 490.99 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 861,540.00 USD | 395.21 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 862,530.00 USD | 991.50 USD | 0.00 USD | `+12.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 872,870.00 USD | 10,340.00 USD | 0.00 USD | `+12.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 873,280.00 USD | 409.52 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 873,560.00 USD | 284.92 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 873,910.00 USD | 350.37 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 874,040.00 USD | 124.04 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 874,160.00 USD | 117.26 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 876,330.00 USD | 2,180.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 877,110.00 USD | 778.64 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 877,480.00 USD | 363.87 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 878,060.00 USD | 589.52 USD | 0.00 USD | `+14.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 878,180.00 USD | 110.62 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 888,260.00 USD | 10,090.00 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 893,680.00 USD | 5,420.00 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 896,210.00 USD | 2,520.00 USD | 0.00 USD | `+14.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 896,460.00 USD | 248.49 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 905,610.00 USD | 9,150.00 USD | 0.00 USD | `+15.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 906,330.00 USD | 722.63 USD | 0.00 USD | `+15.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 906,640.00 USD | 312.07 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 906,810.00 USD | 171.24 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 907,370.00 USD | 561.11 USD | 0.00 USD | `+16.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 907,620.00 USD | 249.30 USD | 0.00 USD | `+16.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 909,090.00 USD | 1,470.00 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 909,520.00 USD | 432.18 USD | 0.00 USD | `+16.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 909,660.00 USD | 137.88 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 912,000.00 USD | 2,340.00 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 912,700.00 USD | 694.72 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 912,860.00 USD | 160.60 USD | 0.00 USD | `+18.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 919,410.00 USD | 6,560.00 USD | 0.00 USD | `+18.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 922,330.00 USD | 2,920.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 922,560.00 USD | 224.56 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 926,130.00 USD | 3,570.00 USD | 0.00 USD | `+18.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 926,560.00 USD | 432.19 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 928,260.00 USD | 1,700.00 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,450,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,460,000.00 USD | 5,390.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,460,000.00 USD | 285.32 USD | 0.00 USD | `+20.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,460,000.00 USD | 1,130.00 USD | 0.00 USD | `+20.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,460,000.00 USD | 1,240.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,460,000.00 USD | 278.06 USD | 0.00 USD | `+20.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,460,000.00 USD | 309.00 USD | 0.00 USD | `+21.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,460,000.00 USD | 228.98 USD | 0.00 USD | `+21.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,460,000.00 USD | 272.12 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,460,000.00 USD | 117.12 USD | 0.00 USD | `+21.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,600,000.00 USD | 140,120.00 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,600,000.00 USD | 530.01 USD | 0.00 USD | `+22.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,600,000.00 USD | 128.23 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,710,000.00 USD | 108,190.00 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,710,000.00 USD | 3,430.00 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,710,000.00 USD | 550.49 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,720,000.00 USD | 5,810.00 USD | 0.00 USD | `+23.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,720,000.00 USD | 1,520.00 USD | 0.00 USD | `+23.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,730,000.00 USD | 5,570.00 USD | 0.00 USD | `+23.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,730,000.00 USD | 1,290.00 USD | 0.00 USD | `+23.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,730,000.00 USD | 294.81 USD | 0.00 USD | `+24.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,730,000.00 USD | 183.11 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,730,000.00 USD | 123.13 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,730,000.00 USD | 494.98 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,730,000.00 USD | 613.52 USD | 0.00 USD | `+24.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,850,000.00 USD | 115,100.00 USD | 0.00 USD | `+25.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,850,000.00 USD | 409.76 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,850,000.00 USD | 162.77 USD | 0.00 USD | `+25.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,850,000.00 USD | 959.70 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,850,000.00 USD | 160.18 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,850,000.00 USD | 669.85 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,850,000.00 USD | 293.61 USD | 0.00 USD | `+27.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,960,000.00 USD | 112,050.00 USD | 0.00 USD | `+27.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,960,000.00 USD | 462.47 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,960,000.00 USD | 2,180.00 USD | 0.00 USD | `+28.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,960,000.00 USD | 273.34 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,960,000.00 USD | 119.49 USD | 0.00 USD | `+28.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,980,000.00 USD | 20,740.00 USD | 0.00 USD | `+28.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,980,000.00 USD | 468.47 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,990,000.00 USD | 1,430.00 USD | 0.00 USD | `+29.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,990,000.00 USD | 338.50 USD | 0.00 USD | `+30.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,990,000.00 USD | 2,640.00 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,990,000.00 USD | 1,230.00 USD | 0.00 USD | `+30.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,990,000.00 USD | 2,450.00 USD | 0.00 USD | `+31.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,990,000.00 USD | 1,250.00 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,990,000.00 USD | 143.67 USD | 0.00 USD | `+31.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,000,000.00 USD | 989.81 USD | 0.00 USD | `+32.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,000,000.00 USD | 304.33 USD | 0.00 USD | `+32.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,000,000.00 USD | 255.14 USD | 0.00 USD | `+33.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,000,000.00 USD | 241.65 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,000,000.00 USD | 239.97 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,000,000.00 USD | 2,470.00 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,000,000.00 USD | 3,060.00 USD | 0.00 USD | `+34.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,310,000.00 USD | 310,250.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,310,000.00 USD | 309.53 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,310,000.00 USD | 159.09 USD | 0.00 USD | `+35.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,310,000.00 USD | 146.21 USD | 0.00 USD | `+36.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,330,000.00 USD | 18,420.00 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,330,000.00 USD | 933.81 USD | 0.00 USD | `+36.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,330,000.00 USD | 658.86 USD | 0.00 USD | `+36.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,550,000.00 USD | 213,390.00 USD | 0.00 USD | `+37.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,550,000.00 USD | 560.05 USD | 0.00 USD | `+37.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,550,000.00 USD | 1,050.00 USD | 0.00 USD | `+38.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,550,000.00 USD | 509.71 USD | 0.00 USD | `+38.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,550,000.00 USD | 162.15 USD | 0.00 USD | `+39.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,550,000.00 USD | 187.04 USD | 0.00 USD | `+39.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,550,000.00 USD | 542.12 USD | 0.00 USD | `+40.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,570,000.00 USD | 23,740.00 USD | 0.00 USD | `+40.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,570,000.00 USD | 2,010.00 USD | 0.00 USD | `+40.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,580,000.00 USD | 345.91 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,580,000.00 USD | 104.79 USD | 0.00 USD | `+41.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,580,000.00 USD | 100.04 USD | 0.00 USD | `+42.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,580,000.00 USD | 517.52 USD | 0.00 USD | `+42.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,580,000.00 USD | 152.29 USD | 0.00 USD | `+42.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,580,000.00 USD | 1,480.00 USD | 0.00 USD | `+43.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,580,000.00 USD | 1,010.00 USD | 0.00 USD | `+43.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,580,000.00 USD | 2,780.00 USD | 0.00 USD | `+44.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,580,000.00 USD | 340.38 USD | 0.00 USD | `+44.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,580,000.00 USD | 903.22 USD | 0.00 USD | `+44.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,580,000.00 USD | 475.01 USD | 0.00 USD | `+44.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,620,000.00 USD | 41,160.00 USD | 0.00 USD | `+45.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,640,000.00 USD | 12,840.00 USD | 0.00 USD | `+45.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,830,000.00 USD | 194,770.00 USD | 0.00 USD | `+45.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,840,000.00 USD | 12,890.00 USD | 0.00 USD | `+46.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,850,000.00 USD | 8,820.00 USD | 0.00 USD | `+46.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,850,000.00 USD | 466.95 USD | 0.00 USD | `+46.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,850,000.00 USD | 613.59 USD | 0.00 USD | `+47.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,860,000.00 USD | 1,420.00 USD | 0.00 USD | `+47.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,870,000.00 USD | 13,000.00 USD | 0.00 USD | `+47.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,870,000.00 USD | 284.42 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,890,000.00 USD | 22,810.00 USD | 0.00 USD | `+50.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,890,000.00 USD | 640.82 USD | 0.00 USD | `+51.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,890,000.00 USD | 134.75 USD | 0.00 USD | `+51.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,910,000.00 USD | 13,400.00 USD | 0.00 USD | `+52.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,920,000.00 USD | 13,490.00 USD | 0.00 USD | `+53.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,930,000.00 USD | 11,580.00 USD | 0.00 USD | `+53.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,940,000.00 USD | 3,610.00 USD | 0.00 USD | `+53.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,940,000.00 USD | 1,500.00 USD | 0.00 USD | `+55.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,950,000.00 USD | 15,000.00 USD | 0.00 USD | `+55.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,960,000.00 USD | 9,030.00 USD | 0.00 USD | `+55.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,960,000.00 USD | 405.86 USD | 0.00 USD | `+57.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,970,000.00 USD | 13,890.00 USD | 0.00 USD | `+57.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,990,000.00 USD | 14,000.00 USD | 0.00 USD | `+58.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,000,000.00 USD | 12,560.00 USD | 0.00 USD | `+59.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,030,000.00 USD | 32,860.00 USD | 0.00 USD | `+60.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,030,000.00 USD | 102.40 USD | 0.00 USD | `+60.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,030,000.00 USD | 106.64 USD | 0.00 USD | `+60.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,040,000.00 USD | 1,430.00 USD | 0.00 USD | `+60.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,040,000.00 USD | 2,810.00 USD | 0.00 USD | `+60.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,050,000.00 USD | 8,420.00 USD | 0.00 USD | `+61.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,050,000.00 USD | 1,410.00 USD | 0.00 USD | `+62.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,050,000.00 USD | 145.37 USD | 0.00 USD | `+63.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,050,000.00 USD | 1,390.00 USD | 0.00 USD | `+63.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,060,000.00 USD | 14,390.00 USD | 0.00 USD | `+63.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,070,000.00 USD | 7,000.00 USD | 0.00 USD | `+64.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,090,000.00 USD | 14,490.00 USD | 0.00 USD | `+64.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,090,000.00 USD | 1,370.00 USD | 0.00 USD | `+64.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,090,000.00 USD | 1,350.00 USD | 0.00 USD | `+66.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,090,000.00 USD | 1,340.00 USD | 0.00 USD | `+66.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,090,000.00 USD | 342.08 USD | 0.00 USD | `+67.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,090,000.00 USD | 1,330.00 USD | 0.00 USD | `+67.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,090,000.00 USD | 1,310.00 USD | 0.00 USD | `+69.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,110,000.00 USD | 14,890.00 USD | 0.00 USD | `+69.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,120,000.00 USD | 9,580.00 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,130,000.00 USD | 14,980.00 USD | 0.00 USD | `+70.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,150,000.00 USD | 20,120.00 USD | 0.00 USD | `+70.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,150,000.00 USD | 1,180.00 USD | 0.00 USD | `+70.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,160,000.00 USD | 1,260.00 USD | 0.00 USD | `+73.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,160,000.00 USD | 2,150.00 USD | 0.00 USD | `+75.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,160,000.00 USD | 158.76 USD | 0.00 USD | `+77.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,160,000.00 USD | 574.53 USD | 0.00 USD | `+80.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,160,000.00 USD | 391.32 USD | 0.00 USD | `+81.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,160,000.00 USD | 1,160.00 USD | 0.00 USD | `+83.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,160,000.00 USD | 1,140.00 USD | 0.00 USD | `+86.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,160,000.00 USD | 1,970.00 USD | 0.00 USD | `+86.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,160,000.00 USD | 281.45 USD | 0.00 USD | `+88.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,160,000.00 USD | 2,070.00 USD | 0.00 USD | `+88.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,180,000.00 USD | 13,060.00 USD | 0.00 USD | `+93.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,180,000.00 USD | 1,070.00 USD | 0.00 USD | `+98.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,180,000.00 USD | 320.52 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7350` | 12,820,000.00 USD | 0.00 USD | 12,820,000.00 USD | 69,900.00 USD | 27,680.00 USD | 97,970.00 USD |
| `7D` | `0.7370` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 38,700.00 USD | 17,190.00 USD | 32,690.00 USD |
| `7D` | `0.7390` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 27,490.00 USD | 24,560.00 USD | 26,600.00 USD |
| `7D` | `0.7410` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 18,820.00 USD | 8,780.00 USD | 29,580.00 USD |
| `7D` | `0.7430` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 44,520.00 USD | 5,210.00 USD | 33,180.00 USD |
| `7D` | `0.7450` | 12,310,000.00 USD | 0.00 USD | 12,310,000.00 USD | 34,130.00 USD | 21,270.00 USD | 43,570.00 USD |
| `7D` | `0.7470` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 23,010.00 USD | 19,630.00 USD | 23,940.00 USD |
| `7D` | `0.7490` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 26,370.00 USD | 12,290.00 USD | 5,240.00 USD |
| `7D` | `0.7510` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 10,970.00 USD | 16,630.00 USD | 21,970.00 USD |
| `7D` | `0.7530` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 1,690.00 USD | 654.10 USD | 6,800.00 USD |
| `7D` | `0.7550` | 12,040,000.00 USD | 0.00 USD | 12,040,000.00 USD | 8,700.00 USD | 6,530.00 USD | 18,850.00 USD |
| `7D` | `0.7570` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 22,280.00 USD | 16,160.00 USD | 182.91 USD |
| `7D` | `0.7590` | 11,970,000.00 USD | 0.00 USD | 11,970,000.00 USD | 6,840.00 USD | 25,130.00 USD | 1,090.00 USD |
| `7D` | `0.7610` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 21,310.00 USD | 16,580.00 USD | 0.00 USD |
| `7D` | `0.7630` | 11,900,000.00 USD | 0.00 USD | 11,900,000.00 USD | 20,690.00 USD | 118.70 USD | 934.78 USD |
| `7D` | `0.7650` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 556.58 USD | 23,090.00 USD | 10,610.00 USD |
| `7D` | `0.7670` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 1,280.00 USD | 3,960.00 USD | 23,950.00 USD |
| `7D` | `0.7690` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD |
| `7D` | `0.7710` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 7,690.00 USD | 1,480.00 USD | 0.00 USD |
| `1D` | `0.7780` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 7,440.00 USD | 5,830.00 USD | 1,330.00 USD |
| `7D` | `0.7790` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 0.00 USD | 5,390.00 USD | 1,330.00 USD |
| `1D` | `0.7800` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 466.70 USD | 10,380.00 USD | 55,250.00 USD |
| `7D` | `0.7810` | 11,800,000.00 USD | 0.00 USD | 11,800,000.00 USD | 0.00 USD | 185.50 USD | 5,200.00 USD |
| `1D` | `0.7820` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 15,370.00 USD | 17,460.00 USD | 33,180.00 USD |
| `7D` | `0.7830` | 11,790,000.00 USD | 0.00 USD | 11,790,000.00 USD | 0.00 USD | 3,930.00 USD | 5,450.00 USD |
| `1D` | `0.7840` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 29,640.00 USD | 26,410.00 USD | 12,520.00 USD |
| `7D` | `0.7850` | 11,780,000.00 USD | 0.00 USD | 11,780,000.00 USD | 7,790.00 USD | 20,370.00 USD | 14,430.00 USD |
| `1D` | `0.7860` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 3,670.00 USD | 5,420.00 USD | 453.01 USD |
| `7D` | `0.7870` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 0.00 USD | 25,170.00 USD | 0.00 USD |
| `1D` | `0.7880` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 33,380.00 USD | 6,000.00 USD | 9,800.00 USD |
| `7D` | `0.7890` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 0.00 USD | 14,290.00 USD | 0.00 USD |
| `1D` | `0.7900` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 20,640.00 USD | 23,720.00 USD | 8,870.00 USD |
| `7D` | `0.7910` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 6,610.00 USD | 24,700.00 USD | 0.00 USD |
| `1D` | `0.7920` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 10,370.00 USD | 16,170.00 USD | 37,760.00 USD |
| `7D` | `0.7930` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 0.00 USD | 12,880.00 USD | 78,780.00 USD |
| `1D` | `0.7940` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 21,090.00 USD | 20,690.00 USD | 21,830.00 USD |
| `7D` | `0.7950` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 2,210.00 USD | 25,690.00 USD | 81,480.00 USD |
| `1D` | `0.7960` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 4,910.00 USD | 6,390.00 USD | 39,790.00 USD |
| `7D` | `0.7970` | 11,470,000.00 USD | 0.00 USD | 11,470,000.00 USD | 26,700.00 USD | 3,570.00 USD | 58,520.00 USD |
| `1D` | `0.7980` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 25,120.00 USD | 11,770.00 USD | 36,510.00 USD |
| `7D` | `0.7990` | 11,380,000.00 USD | 0.00 USD | 11,380,000.00 USD | 8,560.00 USD | 2,220.00 USD | 20,920.00 USD |
| `1D` | `0.8000` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 32,430.00 USD | 21,300.00 USD | 35,520.00 USD |
| `7D` | `0.8010` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 43,340.00 USD | 14,760.00 USD | 35,910.00 USD |
| `1D` | `0.8020` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 1,730.00 USD | 251.75 USD | 1,230.00 USD |
| `1D` | `0.8040` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 37,430.00 USD | 23,740.00 USD | 21,880.00 USD |
| `7D` | `0.8050` | 11,260,000.00 USD | 0.00 USD | 11,260,000.00 USD | 10,860.00 USD | 19,680.00 USD | 0.00 USD |
| `1D` | `0.8060` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 50,970.00 USD | 15,130.00 USD | 70,190.00 USD |
| `7D` | `0.8070` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 5,030.00 USD | 11,280.00 USD | 1,940.00 USD |
| `1D` | `0.8080` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 3,230.00 USD | 19,130.00 USD | 1,570.00 USD |
| `7D` | `0.8090` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 0.00 USD | 9,100.00 USD | 11,920.00 USD |
| `1D` | `0.8100` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 1,750.00 USD | 6,140.00 USD | 1,660.00 USD |
| `7D` | `0.8110` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 61,670.00 USD | 8,310.00 USD | 38,210.00 USD |
| `1D` | `0.8120` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 15,380.00 USD | 3,270.00 USD | 23,380.00 USD |
| `7D` | `0.8130` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 45,800.00 USD | 19,710.00 USD | 13,970.00 USD |
| `1D` | `0.8140` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 29,630.00 USD | 9,710.00 USD | 23,900.00 USD |
| `7D` | `0.8150` | 11,000,000.00 USD | 0.00 USD | 11,000,000.00 USD | 139,680.00 USD | 51,810.00 USD | 169,600.00 USD |
| `1D` | `0.8160` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 116,280.00 USD | 24,170.00 USD | 173,740.00 USD |
| `7D` | `0.8170` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 91,050.00 USD | 25,080.00 USD | 78,040.00 USD |
| `1D` | `0.8180` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 66,880.00 USD | 10,440.00 USD | 32,950.00 USD |
| `7D` | `0.8190` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 200,250.00 USD | 53,380.00 USD | 47,340.00 USD |
| `1D` | `0.8200` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 112,400.00 USD | 8,800.00 USD | 88,010.00 USD |
| `7D` | `0.8210` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 138,580.00 USD | 80,040.00 USD | 198,560.00 USD |
| `1D` | `0.8220` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 86,610.00 USD | 89,600.00 USD | 85,570.00 USD |
| `7D` | `0.8230` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 44,590.00 USD | 40,420.00 USD | 66,990.00 USD |
| `1D` | `0.8240` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 10,570.00 USD | 6,410.00 USD | 149,870.00 USD |
| `7D` | `0.8250` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 198,230.00 USD | 30,370.00 USD | 126,190.00 USD |
| `1D` | `0.8260` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 43,870.00 USD | 11,180.00 USD | 24,850.00 USD |
| `7D` | `0.8270` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 147,770.00 USD | 53,560.00 USD | 66,160.00 USD |
| `1D` | `0.8280` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 41,470.00 USD | 22,760.00 USD | 7,500.00 USD |
| `7D` | `0.8290` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 94,690.00 USD | 42,420.00 USD | 82,590.00 USD |
| `1D` | `0.8300` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 27,690.00 USD | 14,510.00 USD | 54,420.00 USD |
| `7D` | `0.8310` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 36,870.00 USD | 32,050.00 USD | 116,190.00 USD |
| `1D` | `0.8320` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 3,000.00 USD | 37,880.00 USD | 41,510.00 USD |
| `7D` | `0.8330` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 157,210.00 USD | 105,720.00 USD | 198,210.00 USD |
| `1D` | `0.8340` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 149,160.00 USD | 40,080.00 USD | 100,520.00 USD |
| `7D` | `0.8350` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 117,940.00 USD | 16,770.00 USD | 84,180.00 USD |
| `1D` | `0.8360` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 58,860.00 USD | 13,380.00 USD | 1,460.00 USD |
| `7D` | `0.8370` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 140,480.00 USD | 109,700.00 USD | 145,880.00 USD |
| `1D` | `0.8380` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 51,030.00 USD | 66,750.00 USD | 144,000.00 USD |
| `7D` | `0.8390` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 30,810.00 USD | 160,930.00 USD | 164,020.00 USD |
| `1D` | `0.8400` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 36,990.00 USD | 9,770.00 USD | 55,200.00 USD |
| `7D` | `0.8410` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 91,790.00 USD | 34,400.00 USD | 27,510.00 USD |
| `1D` | `0.8420` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 89,320.00 USD | 63,630.00 USD | 65,170.00 USD |
| `7D` | `0.8430` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 67,920.00 USD | 123,520.00 USD | 9,570.00 USD |
| `1D` | `0.8440` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 67,620.00 USD | 63,050.00 USD | 22,350.00 USD |
| `7D` | `0.8450` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 34,560.00 USD | 102,460.00 USD | 0.00 USD |
| `1D` | `0.8460` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 22,250.00 USD | 93,240.00 USD | 39,150.00 USD |
| `7D` | `0.8470` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 44,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8480` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 51,620.00 USD | 61,820.00 USD | 70,740.00 USD |
| `7D` | `0.8490` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 64,910.00 USD | 69,480.00 USD | 133,230.00 USD |
| `1D` | `0.8500` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 71,330.00 USD | 88,390.00 USD | 167,420.00 USD |
| `7D` | `0.8510` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 155,060.00 USD | 72,120.00 USD | 0.00 USD |
| `1D` | `0.8520` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 89,760.00 USD | 172,130.00 USD | 134,230.00 USD |
| `7D` | `0.8530` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 215,880.00 USD | 17,300.00 USD | 52,310.00 USD |
| `1D` | `0.8540` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,240.00 USD |
| `7D` | `0.8550` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 78,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8560` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 0.00 USD | 24,460.00 USD | 46,280.00 USD |
| `7D` | `0.8570` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 99,680.00 USD | 55,310.00 USD | 33,190.00 USD |
| `1D` | `0.8580` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 32,900.00 USD | 66,810.00 USD | 26,540.00 USD |
| `7D` | `0.8590` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 132,610.00 USD | 56,980.00 USD | 33,020.00 USD |
| `1D` | `0.8600` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 75,640.00 USD | 23,780.00 USD | 23,250.00 USD |
| `7D` | `0.8610` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 36,870.00 USD | 188,190.00 USD | 28,430.00 USD |
| `1D` | `0.8620` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 46,800.00 USD | 25,800.00 USD | 26,260.00 USD |
| `7D` | `0.8630` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 100,980.00 USD | 64,400.00 USD | 388,160.00 USD |
| `1D` | `0.8640` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 77,240.00 USD | 137,660.00 USD | 98,430.00 USD |
| `7D` | `0.8650` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 254,940.00 USD | 93,770.00 USD | 562,220.00 USD |
| `1D` | `0.8660` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 118,030.00 USD | 27,450.00 USD | 154,920.00 USD |
| `7D` | `0.8670` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 252,430.00 USD | 0.00 USD | 126,970.00 USD |
| `1D` | `0.8680` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 106,760.00 USD | 11,860.00 USD | 125,520.00 USD |
| `7D` | `0.8690` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 108,230.00 USD |
| `1D` | `0.8700` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 38,850.00 USD | 50,170.00 USD |
| `7D` | `0.8710` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 207,250.00 USD | 34,600.00 USD | 4,350.00 USD |
| `1D` | `0.8720` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 182,270.00 USD | 62,100.00 USD | 172,760.00 USD |
| `7D` | `0.8730` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 88,860.00 USD |
| `1D` | `0.8740` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 55,600.00 USD | 0.00 USD | 27,510.00 USD |
| `7D` | `0.8750` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 26,230.00 USD | 0.00 USD | 258,860.00 USD |
| `1D` | `0.8760` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 150,570.00 USD |
| `7D` | `0.8770` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 68,370.00 USD |
| `1D` | `0.8780` | 866,800.00 USD | 0.00 USD | 866,800.00 USD | 79,990.00 USD | 6,840.00 USD | 67,840.00 USD |
| `1D` | `0.8800` | 712,120.00 USD | 0.00 USD | 712,120.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8810` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 20,310.00 USD | 3,570.00 USD | 0.00 USD |
| `1D` | `0.8820` | 707,360.00 USD | 0.00 USD | 707,360.00 USD | 37,200.00 USD | 0.00 USD | 94,850.00 USD |
| `7D` | `0.8830` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 6,140.00 USD |
| `1D` | `0.8840` | 575,310.00 USD | 0.00 USD | 575,310.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD |
| `7D` | `0.8850` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 35,900.00 USD | 7,760.00 USD |
| `1D` | `0.8860` | 573,040.00 USD | 0.00 USD | 573,040.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `1D` | `0.8880` | 571,960.00 USD | 0.00 USD | 571,960.00 USD | 122,200.00 USD | 1,400.00 USD | 1,350.00 USD |
| `7D` | `0.8890` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 8,820.00 USD | 3,860.00 USD | 0.00 USD |
| `1D` | `0.8900` | 447,010.00 USD | 0.00 USD | 447,010.00 USD | 2,860.00 USD | 0.00 USD | 49,010.00 USD |
| `7D` | `0.8910` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 523,470.00 USD | 55,310.00 USD | 0.00 USD |
| `1D` | `0.8920` | 395,140.00 USD | 0.00 USD | 395,140.00 USD | 137,750.00 USD | 0.00 USD | 11,330.00 USD |
| `7D` | `0.8930` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8940` | 246,060.00 USD | 0.00 USD | 246,060.00 USD | 200,000.00 USD | 45,760.00 USD | 298.98 USD |
| `1D` | `0.8950` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8950` | 881,620.00 USD | 881,620.00 USD | 0.00 USD | 800,940.00 USD | 68,760.00 USD | 11,920.00 USD |
| `7D` | `0.8950` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 800,940.00 USD | 68,760.00 USD | 11,920.00 USD |
| `1D` | `0.8960` | 113,450.00 USD | 113,450.00 USD | 0.00 USD | 2,890.00 USD | 107,980.00 USD | 2,580.00 USD |
| `7D` | `0.8970` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 634,760.00 USD | 93,070.00 USD | 1,520.00 USD |
| `1D` | `0.8980` | 536,750.00 USD | 536,750.00 USD | 0.00 USD | 74,000.00 USD | 98,360.00 USD | 250,940.00 USD |
| `7D` | `0.8990` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 379,180.00 USD | 67,360.00 USD | 340,680.00 USD |
| `1D` | `0.9000` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 239,630.00 USD | 191,290.00 USD | 257,660.00 USD |
| `7D` | `0.9010` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 207,550.00 USD | 109,410.00 USD | 381,840.00 USD |
| `1D` | `0.9020` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 209,800.00 USD | 138,990.00 USD | 379,620.00 USD |
| `7D` | `0.9030` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 124,030.00 USD | 99,390.00 USD | 101,580.00 USD |
| `1D` | `0.9040` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 211,950.00 USD | 223,010.00 USD | 330,710.00 USD |
| `7D` | `0.9050` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 169,680.00 USD | 0.00 USD | 323,290.00 USD |
| `1D` | `0.9060` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 258,520.00 USD | 125,650.00 USD | 203,700.00 USD |
| `7D` | `0.9070` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 548,330.00 USD | 85,530.00 USD | 40,300.00 USD |
| `1D` | `0.9080` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 249,000.00 USD | 147,110.00 USD | 133,610.00 USD |
| `7D` | `0.9090` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 60,680.00 USD | 142,850.00 USD | 191,060.00 USD |
| `1D` | `0.9100` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 99,190.00 USD | 39,940.00 USD | 29,720.00 USD |
| `7D` | `0.9110` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 259,120.00 USD | 103,750.00 USD | 66,380.00 USD |
| `1D` | `0.9120` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 100,870.00 USD | 97,820.00 USD | 90,440.00 USD |
| `7D` | `0.9130` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 80,230.00 USD | 86,960.00 USD | 66,050.00 USD |
| `1D` | `0.9140` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 181,270.00 USD | 56,340.00 USD | 209,490.00 USD |
| `7D` | `0.9150` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 111,690.00 USD | 111,780.00 USD | 172,440.00 USD |
| `1D` | `0.9160` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 130,780.00 USD | 169,050.00 USD | 223,760.00 USD |
| `7D` | `0.9170` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 163,880.00 USD | 2,050.00 USD | 0.00 USD |
| `1D` | `0.9180` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 90,690.00 USD | 51,410.00 USD | 93,750.00 USD |
| `7D` | `0.9190` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 296,480.00 USD | 60,800.00 USD | 238,200.00 USD |
| `1D` | `0.9200` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 73,730.00 USD | 22,510.00 USD | 112,270.00 USD |
| `7D` | `0.9210` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 194,470.00 USD | 18,660.00 USD | 173,150.00 USD |
| `1D` | `0.9220` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 203,870.00 USD | 94,010.00 USD | 260,940.00 USD |
| `7D` | `0.9230` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 56,540.00 USD | 68,150.00 USD | 395,270.00 USD |
| `1D` | `0.9240` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 240,420.00 USD | 84,970.00 USD | 266,810.00 USD |
| `7D` | `0.9250` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 158,890.00 USD | 63,010.00 USD | 70,380.00 USD |
| `1D` | `0.9260` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 135,010.00 USD | 117,320.00 USD | 105,360.00 USD |
| `7D` | `0.9270` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 220,880.00 USD | 46,830.00 USD | 89,770.00 USD |
| `1D` | `0.9280` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 5,090.00 USD | 67,540.00 USD | 74,580.00 USD |
| `7D` | `0.9290` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 4,480.00 USD | 53,740.00 USD | 35,100.00 USD |
| `1D` | `0.9300` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 43,730.00 USD | 61,500.00 USD | 115,770.00 USD |
| `7D` | `0.9310` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 181,630.00 USD | 50,140.00 USD | 199,230.00 USD |
| `1D` | `0.9320` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 176,150.00 USD | 29,700.00 USD | 59,420.00 USD |
| `7D` | `0.9330` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 4,410.00 USD | 76,570.00 USD | 63,160.00 USD |
| `1D` | `0.9340` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 5,250.00 USD | 35,920.00 USD | 706.99 USD |
| `7D` | `0.9350` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 53,950.00 USD | 55,880.00 USD | 5,030.00 USD |
| `1D` | `0.9360` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 48,720.00 USD | 17,210.00 USD | 55,350.00 USD |
| `7D` | `0.9370` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 256,610.00 USD | 5,150.00 USD | 46,960.00 USD |
| `1D` | `0.9380` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 155,050.00 USD | 62,150.00 USD | 239,380.00 USD |
| `7D` | `0.9390` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 86,850.00 USD | 36,340.00 USD | 265,660.00 USD |
| `1D` | `0.9400` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 58,840.00 USD | 3,680.00 USD | 89,060.00 USD |
| `7D` | `0.9410` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 123,000.00 USD | 6,050.00 USD | 0.00 USD |
| `1D` | `0.9420` | 8,680,000.00 USD | 8,680,000.00 USD | 0.00 USD | 17,290.00 USD | 13,920.00 USD | 24,450.00 USD |
| `7D` | `0.9430` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 4,970.00 USD | 68,030.00 USD | 33,660.00 USD |
| `1D` | `0.9440` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 6,330.00 USD | 38,560.00 USD | 58,580.00 USD |
| `7D` | `0.9450` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 3,360.00 USD | 244,270.00 USD | 90,360.00 USD |
| `1D` | `0.9460` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 59,870.00 USD | 32,120.00 USD | 159,670.00 USD |
| `7D` | `0.9470` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `1D` | `0.9480` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 91,790.00 USD | 73,040.00 USD | 56,120.00 USD |
| `7D` | `0.9490` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD |
| `1D` | `0.9500` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 26,310.00 USD | 36,450.00 USD | 70,450.00 USD |
| `7D` | `0.9510` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 2,840.00 USD | 88,970.00 USD | 736,280.00 USD |
| `1D` | `0.9520` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 52,590.00 USD | 28,420.00 USD | 211,920.00 USD |
| `7D` | `0.9530` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 1,580.00 USD |
| `1D` | `0.9540` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 59,080.00 USD | 50,610.00 USD | 94,310.00 USD |
| `7D` | `0.9550` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 74,980.00 USD | 2,400.00 USD | 60,590.00 USD |
| `1D` | `0.9560` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 40,290.00 USD | 26,630.00 USD | 48,530.00 USD |
| `7D` | `0.9570` | 13,170,000.00 USD | 13,170,000.00 USD | 0.00 USD | 463,830.00 USD | 4,720.00 USD | 1,170.00 USD |
| `1D` | `0.9580` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 27,440.00 USD | 45,440.00 USD | 12,090.00 USD |
| `7D` | `0.9590` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 563,790.00 USD | 21,410.00 USD | 1,570.00 USD |
| `1D` | `0.9600` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 102,060.00 USD | 50,930.00 USD | 78,530.00 USD |
| `7D` | `0.9610` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 698,570.00 USD | 201,530.00 USD | 476,080.00 USD |
| `1D` | `0.9620` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 267,480.00 USD | 67,570.00 USD | 177,160.00 USD |
| `7D` | `0.9630` | 16,630,000.00 USD | 16,630,000.00 USD | 0.00 USD | 579,300.00 USD | 301,610.00 USD | 616,480.00 USD |
| `1D` | `0.9640` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 238,280.00 USD | 68,650.00 USD | 102,410.00 USD |
| `7D` | `0.9650` | 18,210,000.00 USD | 18,210,000.00 USD | 0.00 USD | 857,470.00 USD | 312,610.00 USD | 412,280.00 USD |
| `1D` | `0.9660` | 11,600,000.00 USD | 11,600,000.00 USD | 0.00 USD | 156,170.00 USD | 130,010.00 USD | 71,650.00 USD |
| `7D` | `0.9670` | 20,190,000.00 USD | 20,190,000.00 USD | 0.00 USD | 801,890.00 USD | 555,340.00 USD | 614,720.00 USD |
| `1D` | `0.9680` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 175,350.00 USD | 67,790.00 USD | 303,980.00 USD |
| `7D` | `0.9690` | 21,550,000.00 USD | 21,550,000.00 USD | 0.00 USD | 596,350.00 USD | 312,990.00 USD | 456,350.00 USD |
| `1D` | `0.9700` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 274,850.00 USD | 111,340.00 USD | 186,410.00 USD |
| `7D` | `0.9710` | 22,670,000.00 USD | 22,670,000.00 USD | 0.00 USD | 647,710.00 USD | 319,140.00 USD | 147,630.00 USD |
| `1D` | `0.9720` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 99,840.00 USD | 64,240.00 USD | 118,280.00 USD |
| `7D` | `0.9730` | 23,480,000.00 USD | 23,480,000.00 USD | 0.00 USD | 456,990.00 USD | 160,420.00 USD | 197,270.00 USD |
| `1D` | `0.9740` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 36,690.00 USD | 2,780.00 USD | 43,800.00 USD |
| `7D` | `0.9750` | 24,220,000.00 USD | 24,220,000.00 USD | 0.00 USD | 227,380.00 USD | 293,590.00 USD | 222,120.00 USD |
| `1D` | `0.9760` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 20,700.00 USD | 29,360.00 USD | 84,740.00 USD |
| `7D` | `0.9770` | 25,290,000.00 USD | 25,290,000.00 USD | 0.00 USD | 329,170.00 USD | 211,000.00 USD | 521,320.00 USD |
| `1D` | `0.9780` | 13,380,000.00 USD | 13,380,000.00 USD | 0.00 USD | 32,890.00 USD | 32,300.00 USD | 101,790.00 USD |
| `7D` | `0.9790` | 25,920,000.00 USD | 25,920,000.00 USD | 0.00 USD | 342,340.00 USD | 72,140.00 USD | 222,510.00 USD |
| `1D` | `0.9800` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 61,120.00 USD | 37,860.00 USD | 107,850.00 USD |
| `7D` | `0.9810` | 26,360,000.00 USD | 26,360,000.00 USD | 0.00 USD | 206,910.00 USD | 60,620.00 USD | 169,310.00 USD |
| `1D` | `0.9820` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 77,470.00 USD | 5,610.00 USD | 225.42 USD |
| `7D` | `0.9830` | 26,940,000.00 USD | 26,940,000.00 USD | 0.00 USD | 262,900.00 USD | 116,030.00 USD | 199,120.00 USD |
| `1D` | `0.9840` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 33,500.00 USD | 44,230.00 USD | 5,980.00 USD |
| `7D` | `0.9850` | 27,350,000.00 USD | 27,350,000.00 USD | 0.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD |
| `1D` | `0.9860` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 70,580.00 USD | 40,790.00 USD | 90,730.00 USD |
| `7D` | `0.9870` | 27,860,000.00 USD | 27,860,000.00 USD | 0.00 USD | 248,980.00 USD | 203,100.00 USD | 58,100.00 USD |
| `1D` | `0.9880` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 75,940.00 USD | 21,120.00 USD | 42,510.00 USD |
| `7D` | `0.9890` | 28,150,000.00 USD | 28,150,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 19,900.00 USD |
| `1D` | `0.9900` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 74,180.00 USD | 15,760.00 USD | 6,860.00 USD |
| `7D` | `0.9910` | 28,520,000.00 USD | 28,520,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD |
| `7D` | `0.9930` | 28,890,000.00 USD | 28,890,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 74,270.00 USD |
| `7D` | `0.9950` | 29,200,000.00 USD | 29,200,000.00 USD | 0.00 USD | 48,120.00 USD | 138,500.00 USD | 130,850.00 USD |
| `7D` | `0.9970` | 29,860,000.00 USD | 29,860,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD |
| `7D` | `0.9990` | 30,140,000.00 USD | 30,140,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD |
| `7D` | `1.00` | 30,580,000.00 USD | 30,580,000.00 USD | 0.00 USD | 202,970.00 USD | 57,170.00 USD | 185,430.00 USD |
| `7D` | `1.00` | 31,080,000.00 USD | 31,080,000.00 USD | 0.00 USD | 226,340.00 USD | 61,540.00 USD | 208,880.00 USD |
| `7D` | `1.00` | 31,230,000.00 USD | 31,230,000.00 USD | 0.00 USD | 51,930.00 USD | 39,560.00 USD | 65,670.00 USD |
| `7D` | `1.01` | 31,540,000.00 USD | 31,540,000.00 USD | 0.00 USD | 168,320.00 USD | 16,800.00 USD | 121,280.00 USD |
| `7D` | `1.01` | 32,070,000.00 USD | 32,070,000.00 USD | 0.00 USD | 247,480.00 USD | 61,720.00 USD | 214,680.00 USD |
| `7D` | `1.01` | 32,640,000.00 USD | 32,640,000.00 USD | 0.00 USD | 334,550.00 USD | 84,080.00 USD | 157,480.00 USD |
| `7D` | `1.01` | 33,350,000.00 USD | 33,350,000.00 USD | 0.00 USD | 188,370.00 USD | 177,300.00 USD | 344,360.00 USD |
| `7D` | `1.01` | 33,710,000.00 USD | 33,710,000.00 USD | 0.00 USD | 168,660.00 USD | 60,680.00 USD | 124,520.00 USD |
| `7D` | `1.02` | 34,180,000.00 USD | 34,180,000.00 USD | 0.00 USD | 148,890.00 USD | 62,970.00 USD | 266,840.00 USD |
| `7D` | `1.02` | 34,660,000.00 USD | 34,660,000.00 USD | 0.00 USD | 180,470.00 USD | 47,380.00 USD | 245,240.00 USD |
| `7D` | `1.02` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 95,590.00 USD | 18,960.00 USD | 151,670.00 USD |
| `7D` | `1.02` | 35,240,000.00 USD | 35,240,000.00 USD | 0.00 USD | 151,650.00 USD | 61,120.00 USD | 103,070.00 USD |
| `7D` | `1.02` | 35,430,000.00 USD | 35,430,000.00 USD | 0.00 USD | 59,440.00 USD | 54,210.00 USD | 77,750.00 USD |
| `7D` | `1.03` | 35,630,000.00 USD | 35,630,000.00 USD | 0.00 USD | 76,740.00 USD | 35,970.00 USD | 82,320.00 USD |
| `7D` | `1.03` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 85,920.00 USD | 34,530.00 USD | 50,520.00 USD |
| `7D` | `1.03` | 36,040,000.00 USD | 36,040,000.00 USD | 0.00 USD | 135,830.00 USD | 33,520.00 USD | 76,260.00 USD |
| `7D` | `1.03` | 36,370,000.00 USD | 36,370,000.00 USD | 0.00 USD | 57,570.00 USD | 103,690.00 USD | 163,030.00 USD |
| `7D` | `1.03` | 36,510,000.00 USD | 36,510,000.00 USD | 0.00 USD | 64,880.00 USD | 13,040.00 USD | 63,310.00 USD |
| `7D` | `1.04` | 36,740,000.00 USD | 36,740,000.00 USD | 0.00 USD | 79,670.00 USD | 21,540.00 USD | 133,450.00 USD |
| `7D` | `1.04` | 36,860,000.00 USD | 36,860,000.00 USD | 0.00 USD | 53,800.00 USD | 806.65 USD | 63,320.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `581.10M` | Total OI Tokens: `648,833,396.0 SUI`
  * 1h OI Change: `+1.42%` | 4h OI Change: `+5.24%` | 24h OI Change: `-5.96%`
  * Exchange Breakdown: Binance=`105.16M` | Bybit=`78.22M` | OKX=`33.54M` | Hyperliquid=`30.04M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-30.60K` | Last 24h: `-2.19K` | Last 3d: `56.09K` | Last 7d: `151.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0094%` | **USDT OKX** | `-0.0108%` |
| **USDT Bybit** | `-0.0251%` | **USDT KuCoin** | `-0.0050%` |
| **USDT MEXC** | `-0.0096%` | **USDT BingX** | `-0.0081%` |
| **USDT Gate** | `-0.0083%` | **USDT Bitget** | `-0.0158%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `48.99%` | `51.01%` | `0.96` | 5,430,000.00 USD |
| `15M` | `Binance` | `46.9%` | `53.1%` | `0.88` | 2,150,000.00 USD |
| `15M` | `OKX` | `39.14%` | `60.86%` | `0.64` | 342,460.00 USD |
| `15M` | `Bybit` | `47.49%` | `52.51%` | `0.90` | 386,210.00 USD |
| `15M` | `KuCoin` | `48.43%` | `51.57%` | `0.94` | 14,950.00 USD |
| `15M` | `Gate` | `49.81%` | `50.19%` | `0.99` | 131,700.00 USD |
| `15M` | `Bitget` | `35.13%` | `64.87%` | `0.54` | 79,400.00 USD |
| `15M` | `BingX` | `48.88%` | `51.12%` | `0.96` | 768,910.00 USD |
| `15M` | `MEXC` | `59.85%` | `40.15%` | `1.49` | 313,490.00 USD |
| `15M` | `Bitunix` | `57.04%` | `42.96%` | `1.33` | 101,850.00 USD |
| `15M` | `Hyperliquid` | `59.02%` | `40.98%` | `1.44` | 20,720.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.73%` | `48.27%` | `1.07` | 1,070,000.00 USD |
| `15M` | `Crypto.com` | `41.16%` | `58.84%` | `0.70` | 14.46 USD |
| `15M` | `WhiteBIT` | `88.95%` | `11.05%` | `8.05` | 15,280.00 USD |
| `15M` | `HTX` | `46.52%` | `53.48%` | `0.87` | 2,820.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `95.4%` | `4.6%` | `20.74` | 30,230.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `66.64%` | `33.36%` | `2.00` | 10,340.00 USD |
| `15M` | `Whale Positions` | `46.9%` | `53.1%` | `0.88` | 2,150,000.00 USD |
| `15M` | `Global Accounts` | `48.99%` | `51.01%` | `0.96` | 5,430,000.00 USD |
| `1H` | `SUI` | `51.16%` | `48.84%` | `1.05` | 17,160,000.00 USD |
| `1H` | `Binance` | `56.98%` | `43.02%` | `1.32` | 6,090,000.00 USD |
| `1H` | `OKX` | `42.13%` | `57.87%` | `0.73` | 851,560.00 USD |
| `1H` | `Bybit` | `44.86%` | `55.14%` | `0.81` | 1,350,000.00 USD |
| `1H` | `KuCoin` | `42.21%` | `57.79%` | `0.73` | 62,490.00 USD |
| `1H` | `Gate` | `42.98%` | `57.02%` | `0.75` | 626,960.00 USD |
| `1H` | `Bitget` | `40.96%` | `59.04%` | `0.69` | 232,440.00 USD |
| `1H` | `BingX` | `45.32%` | `54.68%` | `0.83` | 3,300,000.00 USD |
| `1H` | `MEXC` | `57.06%` | `42.94%` | `1.33` | 857,070.00 USD |
| `1H` | `Bitunix` | `54.15%` | `45.85%` | `1.18` | 266,540.00 USD |
| `1H` | `Hyperliquid` | `34.27%` | `65.73%` | `0.52` | 293,670.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.83%` | `47.17%` | `1.12` | 3,030,000.00 USD |
| `1H` | `Crypto.com` | `93.25%` | `6.75%` | `13.81` | 727.76 USD |
| `1H` | `WhiteBIT` | `46.74%` | `53.26%` | `0.88` | 74,300.00 USD |
| `1H` | `HTX` | `46.18%` | `53.82%` | `0.86` | 5,650.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `93.22%` | `6.78%` | `13.75` | 58,050.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.43%` | `50.57%` | `0.98` | 45,330.00 USD |
| `1H` | `Whale Positions` | `56.98%` | `43.02%` | `1.32` | 6,090,000.00 USD |
| `1H` | `Global Accounts` | `51.16%` | `48.84%` | `1.05` | 17,160,000.00 USD |
| `4H` | `SUI` | `51.18%` | `48.82%` | `1.05` | 157,410,000.00 USD |
| `4H` | `Binance` | `51.96%` | `48.04%` | `1.08` | 60,330,000.00 USD |
| `4H` | `OKX` | `49.66%` | `50.34%` | `0.99` | 16,780,000.00 USD |
| `4H` | `Bybit` | `46.62%` | `53.38%` | `0.87` | 16,260,000.00 USD |
| `4H` | `KuCoin` | `49.3%` | `50.7%` | `0.97` | 977,380.00 USD |
| `4H` | `Gate` | `45.76%` | `54.24%` | `0.84` | 3,140,000.00 USD |
| `4H` | `Bitget` | `59.89%` | `40.11%` | `1.49` | 6,560,000.00 USD |
| `4H` | `BingX` | `33.71%` | `66.29%` | `0.51` | 4,070,000.00 USD |
| `4H` | `MEXC` | `51.25%` | `48.75%` | `1.05` | 34,570,000.00 USD |
| `4H` | `Bitunix` | `46.23%` | `53.77%` | `0.86` | 4,540,000.00 USD |
| `4H` | `Hyperliquid` | `65.94%` | `34.06%` | `1.94` | 4,670,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.14%` | `50.86%` | `0.97` | 2,630,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `70.62%` | `29.38%` | `2.40` | 619,240.00 USD |
| `4H` | `HTX` | `41.07%` | `58.93%` | `0.70` | 68,800.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `80.61%` | `19.39%` | `4.16` | 1,240,000.00 USD |
| `4H` | `Aster` | `56.63%` | `43.37%` | `1.31` | 563,870.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `30.01%` | `69.99%` | `0.43` | 390,250.00 USD |
| `4H` | `Whale Positions` | `51.96%` | `48.04%` | `1.08` | 60,330,000.00 USD |
| `4H` | `Global Accounts` | `51.18%` | `48.82%` | `1.05` | 157,410,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.8680` | `0.8663` | `0.8680` | `0.8697` | `0.8640` | 1,274,072.68 USD | 628,587.96 USD | 645,484.72 USD | -16,896.75 USD | `-1.33%` | `6B / 9S` |
| `0:00 UTC` | `0.8698` | `0.8685` | `0.8698` | `0.8706` | `0.8657` | 2,093,919.35 USD | 1,157,864.07 USD | 936,055.29 USD | 221,808.78 USD | `+10.59%` | `11B / 2S` |
| `5:00 UTC` | `0.8700` | `0.8715` | `0.8700` | `0.8748` | `0.8669` | 2,353,506.52 USD | 1,517,666.93 USD | 835,839.59 USD | 681,827.34 USD | `+28.97%` | `29B / 5S` |
| `0:00 UTC` | `0.8800` | `0.8785` | `0.8800` | `0.8828` | `0.8730` | 3,913,129.55 USD | 2,396,328.40 USD | 1,516,801.15 USD | 879,527.25 USD | `+22.48%` | `20B / 6S` |
| `5:00 UTC` | `0.8851` | `0.8843` | `0.8851` | `0.8873` | `0.8813` | 3,303,378.86 USD | 1,747,933.70 USD | 1,555,445.16 USD | 192,488.53 USD | `+5.83%` | `6B / 8S` |
| `0:00 UTC` | `0.8790` | `0.8806` | `0.8790` | `0.8870` | `0.8778` | 3,823,669.01 USD | 1,840,836.89 USD | 1,982,832.12 USD | -141,995.24 USD | `-3.71%` | `23B / 14S` |
| `5:00 UTC` | `0.8903` | `0.8884` | `0.8903` | `0.8908` | `0.8844` | 3,559,512.45 USD | 1,938,272.96 USD | 1,621,239.49 USD | 317,033.48 USD | `+8.91%` | `9B / 6S` |
| `0:00 UTC` | `0.8865` | `0.8876` | `0.8865` | `0.8905` | `0.8850` | 2,686,854.06 USD | 1,226,021.69 USD | 1,460,832.37 USD | -234,810.69 USD | `-8.74%` | `3B / 8S` |
| `5:00 UTC` | `0.8950` | `0.8939` | `0.8950` | `0.8966` | `0.8897` | 3,990,383.01 USD | 1,854,959.02 USD | 2,135,424.00 USD | -280,464.98 USD | `-7.03%` | `14B / 6S` |
| `0:00 UTC` | `0.8952` | `0.8948` | `0.8952` | `0.8955` | `0.8941` | 319,197.61 USD | 176,108.70 USD | 143,088.92 USD | 33,019.78 USD | `+10.34%` | `2B / 1S` |

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
| `5m` | 102,070.00 USD | -342,190.00 USD | **`DISTRIBUTION`** |
| `15m` | 1,020,000.00 USD | -362,440.00 USD | **`ACCUMULATION`** |
| `30m` | 970,010.00 USD | -336,830.00 USD | **`ACCUMULATION`** |
| `1h` | 1,480,000.00 USD | 336,540.00 USD | **`ACCUMULATION`** |
| `2h` | 2,030,000.00 USD | 3,490,000.00 USD | **`ACCUMULATION`** |
| `4h` | 2,360,000.00 USD | 5,540,000.00 USD | **`ACCUMULATION`** |
| `6h` | -4,500,000.00 USD | -9,020,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,370,000.00 USD | -20,960,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -13,260,000.00 USD | -23,170,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,980,000.00 USD | -25,490,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -26,120,000.00 USD | -85,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -156,530,000.00 USD | -484,210,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+102.07K` | 15m=`+1.02M` | 1h=`+1.48M` | 24h=`-7.98M`
* Futures Capital Netflows: 5m=`-342.19K` | 15m=`-362.44K` | 1h=`+336.54K` | 24h=`-25.49M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
