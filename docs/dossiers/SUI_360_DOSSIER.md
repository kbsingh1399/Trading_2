# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:01:31 IST` (`2026-10-30 04:31:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8897` | `0.8907` | `0.8865` | `0.8877` | `1,437,320` | 1,278,002.55 USD | -173,318.99 USD | `-13.56%` | -12,453,007.40 USD | `-0.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.8877` | `0.8895` | `0.8859` | `0.8890` | `506,634` | 449,852.93 USD | 100,232.87 USD | `+22.28%` | -12,352,774.53 USD | `-0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.8891` | `0.8893` | `0.8884` | `0.8892` | `185,027` | 164,470.53 USD | -52,861.01 USD | `-32.14%` | -12,405,635.53 USD | `-0.54` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.8841` | `0.8869` | `0.8777` | `0.8867` | `4,342,170` | 3,823,669.01 USD | -141,995.24 USD | `-3.71%` | -12,783,530.40 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.8867` | `0.8907` | `0.8844` | `0.8890` | `4,006,842` | 3,559,512.45 USD | 317,033.48 USD | `+8.91%` | -12,466,496.92 USD | `+0.35` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8891` | `0.8893` | `0.8884` | `0.8892` | `185,027` | 164,470.53 USD | -52,861.01 USD | `-32.14%` | -12,519,357.93 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8556` | `0.8707` | `0.8482` | `0.8661` | `11,338,098` | 9,773,400.88 USD | 845,261.99 USD | `+8.65%` | -14,666,181.90 USD | `+0.79` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.8661` | `0.8873` | `0.8656` | `0.8841` | `13,301,873` | 11,663,934.28 USD | 1,975,651.91 USD | `+16.94%` | -12,690,530.00 USD | `+1.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.8841` | `0.8907` | `0.8777` | `0.8892` | `8,534,039` | 7,547,651.99 USD | 122,177.23 USD | `+1.62%` | -12,568,352.77 USD | `+0.35` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.8907` | `0.8777` | `0.8893` | `8,446,617` | 7,469,936.96 USD | 198,192.19 USD | `+2.65%` | -12,124,145.78 USD | `+0.70` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | 1,889,481.85 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -683,829.84 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.8907` | `0.8777` | `0.8893` | `8,446,617` | 7,469,936.96 USD | 198,192.19 USD | `+2.65%` | -12,124,145.78 USD | `+0.70` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `BID` | `0.8885` | `1139.8000` | 1,012.77 USD | 23,886.40 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8885` | `139.8000` | 124.22 USD | 24,010.62 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8885` | `139.8000` | 124.22 USD | 24,134.83 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8885` | `16875.3000` | 14,994.04 USD | 39,128.88 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8885` | `4457.6000` | 3,960.58 USD | 43,089.45 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8885` | `2000.0000` | 1,776.96 USD | 44,866.41 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8885` | `4337.4000` | 3,853.61 USD | 48,720.02 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8886` | `2108.5000` | 1,873.70 USD | 11,737.72 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `139.8000` | 124.23 USD | 11,861.95 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `5779.0000` | 5,135.33 USD | 16,997.28 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `139.8000` | 124.23 USD | 17,121.51 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `139.8000` | 124.23 USD | 17,245.74 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `139.8000` | 124.22 USD | 17,369.96 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `4437.3000` | 3,942.90 USD | 21,312.86 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `1616.7000` | 1,436.55 USD | 22,749.41 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8886` | `139.8000` | 124.22 USD | 22,873.63 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8887` | `3249.5000` | 2,887.96 USD | 4,729.67 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8887` | `5777.7000` | 5,134.35 USD | 9,864.02 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.8888` | `400.0000` | 355.53 USD | 355.53 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8888` | `1672.1000` | 1,486.18 USD | 1,841.71 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `0.8889` | `1571.8000` | 1,397.20 USD | 1,397.20 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `0.8889` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.89` | `0.00%` | `-` |
| `ASK` | `0.8890` | `1476.6000` | 1,312.73 USD | 6,341.23 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8890` | `4084.7000` | 3,631.30 USD | 5,028.50 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8891` | `1476.5000` | 1,312.82 USD | 9,766.76 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8891` | `407.6000` | 362.40 USD | 8,453.94 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8891` | `1968.7000` | 1,750.31 USD | 8,091.54 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8892` | `1968.7000` | 1,750.59 USD | 15,076.27 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8892` | `1753.3000` | 1,559.00 USD | 13,325.68 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8892` | `2249.2000` | 1,999.92 USD | 11,766.68 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8893` | `1969.3000` | 1,751.40 USD | 29,489.86 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8893` | `1000.0000` | 889.34 USD | 27,738.47 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8893` | `5634.8000` | 5,011.14 USD | 26,849.13 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8893` | `5634.1000` | 5,010.46 USD | 21,837.99 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8893` | `1969.3000` | 1,751.26 USD | 16,827.53 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8894` | `1124.8000` | 1,000.44 USD | 36,182.62 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8894` | `1000.0000` | 889.43 USD | 35,182.18 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8894` | `1476.9000` | 1,313.58 USD | 34,292.75 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8894` | `1000.0000` | 889.41 USD | 32,979.17 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8894` | `2810.8000` | 2,499.93 USD | 32,089.76 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8894` | `112.4000` | 99.97 USD | 29,589.83 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `662` | `0xb83d...6e36` | `SHORT` | 3,391,869.60 USD | `3,817,609.40` | `1.11` | `0.8899` | `34.24` | 826,865.72 USD | `+24.38%` | `3X Cross` |
| `1001` | `0xa2ce...3126` | `LONG` | 2,212,134.20 USD | `2,500,010.40` | `0.8597` | `0.8899` | `0.000000` | 62,927.67 USD | `+2.84%` | `10X Cross` |
| `1647` | `0x9946...0852` | `SHORT` | 1,284,937.42 USD | `1,444,269.20` | `1.08` | `0.8899` | `1.94` | 273,641.44 USD | `+21.30%` | `10X Cross` |
| `1900` | `0x9df2...c665` | `SHORT` | 1,067,616.00 USD | `1,200,000.00` | `0.7465` | `0.8899` | `26.00` | -171,763.60 USD | `-16.09%` | `10X Cross` |
| `1981` | `0x9aa5...58af` | `SHORT` | 1,019,124.79 USD | `1,145,495.90` | `1.14` | `0.8899` | `8.66` | 286,011.76 USD | `+28.06%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 5,343.53 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9406 USD [API] | `2026-10-29 00:52:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9335` | 9,058.69 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 9.06K USD at 0.9335 USD [API] | `2026-10-29 01:31:02` |
| `ANNOUNCEMENT` | `INFO` | `0.9071` | 418.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.42K USD at 0.9071 USD [API] | `2026-10-29 02:00:14` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9685` (Vol: 265,800.00 USD, Dist: `+9.59%`) | Long MP=`0.8636` (Vol: 140,500.00 USD, Dist: `--2.28%`)
  * 48H Horizon: Short MP=`0.9684` (Vol: 265,800.00 USD, Dist: `+9.58%`) | Long MP=`0.8642` (Vol: 140,500.00 USD, Dist: `--2.20%`)
  * 3D Horizon: Short MP=`0.9684` (Vol: 237,100.00 USD, Dist: `+9.58%`) | Long MP=`0.8642` (Vol: 140,500.00 USD, Dist: `--2.20%`)
  * 7D Horizon: Short MP=`0.9682` (Vol: 687,400.00 USD, Dist: `+9.56%`) | Long MP=`0.8631` (Vol: 140,500.00 USD, Dist: `--2.33%`)
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
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 3,450.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,020.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 2,280.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 784,400.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 2,160.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7465` | 359.96 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 264.86 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 1,250.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 1,750.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,900.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7625` | 3,790.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 11,990,000.00 USD | 11,990,000.00 USD | 37,590.00 USD | 14,770.00 USD | 934.78 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 5,550.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 3,510.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 11,940,000.00 USD | 11,940,000.00 USD | 556.58 USD | 23,090.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,260.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 11,900,000.00 USD | 11,900,000.00 USD | 1,280.00 USD | 177.87 USD | 18,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 25,580.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 207.19 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 11,880,000.00 USD | 11,880,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 150,510.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 11,880,000.00 USD | 11,880,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,940.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 5,230.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 3,430.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 3,510.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 321,490.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 767,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 5,390.00 USD | 36.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 739,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7810` | 11,870,000.00 USD | 11,870,000.00 USD | 0.00 USD | 185.50 USD | 5,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 739,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 21,600.00 USD | 735,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7845` | 155.96 USD | 713,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7850` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 587.33 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7850` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 713,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7870` | 5,550,000.00 USD | 5,550,000.00 USD | 16,780.00 USD | 318.35 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7870` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 710,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7890` | 5,530,000.00 USD | 5,530,000.00 USD | 10,020.00 USD | 12,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 11,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 709,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7910` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 4,750.00 USD | 285.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 29,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 7,620.00 USD | 706,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 10,810.00 USD | 698,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7930` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 12,600.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 12,880.00 USD | 77,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 687,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7945` | 736.66 USD | 686,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7950` | 5,460,000.00 USD | 5,460,000.00 USD | 13,930.00 USD | 266.53 USD | 14,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 18,870.00 USD | 51,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 53,850.00 USD | 686,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7965` | 12,980.00 USD | 632,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 5,430,000.00 USD | 5,430,000.00 USD | 3,300.00 USD | 9,330.00 USD | 22,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 11,630,000.00 USD | 11,630,000.00 USD | 12,100.00 USD | 0.00 USD | 38,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,580.00 USD | 619,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7985` | 40,230.00 USD | 611,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7990` | 5,390,000.00 USD | 5,390,000.00 USD | 505.25 USD | 322.55 USD | 18,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 11,580,000.00 USD | 11,580,000.00 USD | 488.55 USD | 0.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 10,050.00 USD | 571,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8005` | 3,850.00 USD | 561,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8010` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 10,940.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 11,570,000.00 USD | 11,570,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 7,610.00 USD | 557,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 1,350.00 USD | 550,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,680.00 USD | 548,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 16,660.00 USD | 540,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8050` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 6,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 11,520,000.00 USD | 11,520,000.00 USD | 2,040.00 USD | 15,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 361.11 USD | 524,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 523,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 5,340,000.00 USD | 5,340,000.00 USD | 12,740.00 USD | 14,260.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 517,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,510.00 USD | 514,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8090` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 130,110.00 USD | 491,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,430.00 USD | 361,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8110` | 5,300,000.00 USD | 5,300,000.00 USD | 40,190.00 USD | 6,030.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 11,490,000.00 USD | 11,490,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,970.00 USD | 359,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8125` | 1,160.00 USD | 356,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8130` | 5,230,000.00 USD | 5,230,000.00 USD | 23,290.00 USD | 13,030.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 11,390,000.00 USD | 11,390,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 355,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 351,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 5,180,000.00 USD | 5,180,000.00 USD | 66,820.00 USD | 25,820.00 USD | 100,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 11,310,000.00 USD | 11,310,000.00 USD | 135,770.00 USD | 51,810.00 USD | 124,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 38,250.00 USD | 351,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8165` | 492.27 USD | 312,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8170` | 4,990,000.00 USD | 4,990,000.00 USD | 68,580.00 USD | 28,480.00 USD | 79,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 11,000,000.00 USD | 11,000,000.00 USD | 91,050.00 USD | 25,080.00 USD | 78,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 77,840.00 USD | 312,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8185` | 28,030.00 USD | 234,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8190` | 4,810,000.00 USD | 4,810,000.00 USD | 12,140.00 USD | 6,480.00 USD | 15,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 10,810,000.00 USD | 10,810,000.00 USD | 195,400.00 USD | 53,380.00 USD | 47,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,110.00 USD | 206,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8205` | 9,370.00 USD | 205,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8210` | 4,780,000.00 USD | 4,780,000.00 USD | 16,970.00 USD | 30,830.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 10,510,000.00 USD | 10,510,000.00 USD | 138,580.00 USD | 58,400.00 USD | 152,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 474.01 USD | 195,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8225` | 3,080.00 USD | 195,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 4,690,000.00 USD | 4,690,000.00 USD | 11,730.00 USD | 18,140.00 USD | 20,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 10,160,000.00 USD | 10,160,000.00 USD | 37,880.00 USD | 37,160.00 USD | 64,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 463.63 USD | 192,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8245` | 18,980.00 USD | 191,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 4,640,000.00 USD | 4,640,000.00 USD | 18,440.00 USD | 8,600.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 10,020,000.00 USD | 10,020,000.00 USD | 187,510.00 USD | 30,370.00 USD | 126,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 1,580.00 USD | 172,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8270` | 4,590,000.00 USD | 4,590,000.00 USD | 29,570.00 USD | 10,040.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 9,680,000.00 USD | 9,680,000.00 USD | 147,770.00 USD | 51,050.00 USD | 63,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 171,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 166,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8290` | 4,540,000.00 USD | 4,540,000.00 USD | 12,280.00 USD | 15,940.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 9,410,000.00 USD | 9,410,000.00 USD | 89,470.00 USD | 42,420.00 USD | 82,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 46,590.00 USD | 46,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.8395` | 190.31 USD | 190.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.8885` | 322.61 USD | 512.93 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8890` | 957,850.00 USD | 957,850.00 USD | 884,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8910` | 220,290.00 USD | 220,290.00 USD | 186,060.00 USD | 10,900.00 USD | 347.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8910` | 1,760,000.00 USD | 1,760,000.00 USD | 806,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8925` | 807.44 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8930` | 264,950.00 USD | 264,950.00 USD | 44,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8930` | 3,530,000.00 USD | 3,530,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8935` | 2,520.00 USD | 3,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8950` | 444,180.00 USD | 444,180.00 USD | 98,920.00 USD | 48,760.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 4,300,000.00 USD | 4,300,000.00 USD | 719,730.00 USD | 56,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8965` | 187.46 USD | 4,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8970` | 466,400.00 USD | 466,400.00 USD | 0.00 USD | 22,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8970` | 5,020,000.00 USD | 5,020,000.00 USD | 659,500.00 USD | 54,550.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8990` | 948,300.00 USD | 948,300.00 USD | 51,680.00 USD | 152,190.00 USD | 278,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8990` | 5,730,000.00 USD | 5,730,000.00 USD | 308,910.00 USD | 64,400.00 USD | 340,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9010` | 1,530,000.00 USD | 1,530,000.00 USD | 249,240.00 USD | 99,300.00 USD | 230,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 6,270,000.00 USD | 6,270,000.00 USD | 207,550.00 USD | 109,410.00 USD | 216,090.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 8,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9150` | 3,270,000.00 USD | 3,270,000.00 USD | 119,590.00 USD | 92,390.00 USD | 299,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 8,230,000.00 USD | 8,230,000.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9170` | 3,550,000.00 USD | 3,550,000.00 USD | 106,060.00 USD | 107,790.00 USD | 62,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 8,350,000.00 USD | 8,350,000.00 USD | 123,530.00 USD | 2,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9175` | 2,910.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.9305` | 4,210.00 USD | 15,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9310` | 5,330,000.00 USD | 5,330,000.00 USD | 104,570.00 USD | 67,630.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 10,550,000.00 USD | 10,550,000.00 USD | 177,720.00 USD | 48,210.00 USD | 166,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9325` | 523.13 USD | 15,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9330` | 5,440,000.00 USD | 5,440,000.00 USD | 32,530.00 USD | 39,200.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 76,570.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 5,460,000.00 USD | 5,460,000.00 USD | 1,360.00 USD | 13,120.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 10,810,000.00 USD | 10,810,000.00 USD | 53,950.00 USD | 55,880.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 6,000,000.00 USD | 6,000,000.00 USD | 198,110.00 USD | 85,110.00 USD | 261,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 11,100,000.00 USD | 11,100,000.00 USD | 251,760.00 USD | 1,370.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 39,850.00 USD | 55,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `0.9790` | 11,670,000.00 USD | 11,670,000.00 USD | 19,400.00 USD | 33,280.00 USD | 105,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 26,910,000.00 USD | 26,910,000.00 USD | 411,780.00 USD | 99,560.00 USD | 222,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 56,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 11,910,000.00 USD | 11,910,000.00 USD | 100,630.00 USD | 45,360.00 USD | 103,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 27,420,000.00 USD | 27,420,000.00 USD | 264,890.00 USD | 83,040.00 USD | 169,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 12,060,000.00 USD | 12,060,000.00 USD | 91,650.00 USD | 38,020.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 28,000,000.00 USD | 28,000,000.00 USD | 262,900.00 USD | 116,030.00 USD | 199,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 12,140,000.00 USD | 12,140,000.00 USD | 22,370.00 USD | 48,410.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 28,410,000.00 USD | 28,410,000.00 USD | 234,160.00 USD | 58,210.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 56,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9870` | 12,330,000.00 USD | 12,330,000.00 USD | 56,760.00 USD | 31,400.00 USD | 97,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 28,920,000.00 USD | 28,920,000.00 USD | 248,980.00 USD | 203,100.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 61,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9890` | 12,490,000.00 USD | 12,490,000.00 USD | 100,670.00 USD | 32,930.00 USD | 33,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 29,210,000.00 USD | 29,210,000.00 USD | 194,850.00 USD | 78,280.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 1,570.00 USD | 62,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9910` | 12,660,000.00 USD | 12,660,000.00 USD | 80,380.00 USD | 30,860.00 USD | 50,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 29,580,000.00 USD | 29,580,000.00 USD | 198,890.00 USD | 89,640.00 USD | 81,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 12,720,000.00 USD | 12,720,000.00 USD | 33,580.00 USD | 16,590.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 29,950,000.00 USD | 29,950,000.00 USD | 228,340.00 USD | 63,950.00 USD | 74,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 62,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9950` | 30,270,000.00 USD | 30,270,000.00 USD | 48,120.00 USD | 138,500.00 USD | 130,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 30,920,000.00 USD | 30,920,000.00 USD | 215,040.00 USD | 81,210.00 USD | 354,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 31,200,000.00 USD | 31,200,000.00 USD | 145,170.00 USD | 35,870.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,640,000.00 USD | 31,640,000.00 USD | 202,970.00 USD | 57,170.00 USD | 185,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 63,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,140,000.00 USD | 32,140,000.00 USD | 226,340.00 USD | 61,540.00 USD | 208,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,300,000.00 USD | 32,300,000.00 USD | 51,930.00 USD | 39,560.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 100.65 USD | 63,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 32,780,000.00 USD | 32,780,000.00 USD | 256,020.00 USD | 15,900.00 USD | 212,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 33,380,000.00 USD | 33,380,000.00 USD | 247,480.00 USD | 105,290.00 USD | 247,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,180,000.00 USD | 34,180,000.00 USD | 398,890.00 USD | 134,240.00 USD | 259,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,890,000.00 USD | 34,890,000.00 USD | 188,370.00 USD | 177,300.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 705.99 USD | 64,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 35,240,000.00 USD | 35,240,000.00 USD | 168,660.00 USD | 59,720.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 64,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 36,000,000.00 USD | 36,000,000.00 USD | 300,680.00 USD | 97,830.00 USD | 360,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 1,670.00 USD | 65,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.04` | 155.92 USD | 66,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,880,000.00 USD | 39,880,000.00 USD | 102,550.00 USD | 52,580.00 USD | 72,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,970,000.00 USD | 39,970,000.00 USD | 18,340.00 USD | 48,310.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 40,060,000.00 USD | 40,060,000.00 USD | 65,240.00 USD | 17,210.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,160,000.00 USD | 40,160,000.00 USD | 76,550.00 USD | 30,790.00 USD | 294.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,240,000.00 USD | 40,240,000.00 USD | 35,930.00 USD | 20,630.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 66,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,260,000.00 USD | 40,260,000.00 USD | 22,610.00 USD | 0.00 USD | 538.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 69,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,340,000.00 USD | 40,340,000.00 USD | 8,370.00 USD | 46,830.00 USD | 28,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,400,000.00 USD | 40,400,000.00 USD | 1,650.00 USD | 9,420.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,430,000.00 USD | 40,430,000.00 USD | 5,290.00 USD | 2,060.00 USD | 21,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,430,000.00 USD | 40,430,000.00 USD | 0.00 USD | 638.17 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,480,000.00 USD | 40,480,000.00 USD | 16,370.00 USD | 3,040.00 USD | 33,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,490,000.00 USD | 40,490,000.00 USD | 9,950.00 USD | 0.00 USD | 609.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,500,000.00 USD | 40,500,000.00 USD | 5,370.00 USD | 1,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 40,500,000.00 USD | 40,500,000.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 40,530,000.00 USD | 40,530,000.00 USD | 2,410.00 USD | 12,740.00 USD | 17,950.00 USD | `Tier 1 CEX` |
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
  * Total Open Interest: `579.26M` | Total OI Tokens: `651,580,466.8 SUI`
  * 1h OI Change: `+2.68%` | 4h OI Change: `+3.89%` | 24h OI Change: `-6.21%`
  * Exchange Breakdown: Binance=`104.69M` | Bybit=`77.90M` | OKX=`33.50M` | Hyperliquid=`29.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-33.17K` | Last 24h: `-2.19K` | Last 3d: `56.09K` | Last 7d: `151.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0124%` | **USDT OKX** | `-0.0128%` |
| **USDT Bybit** | `-0.0247%` | **USDT KuCoin** | `-0.0084%` |
| **USDT MEXC** | `-0.0124%` | **USDT BingX** | `-0.0103%` |
| **USDT Gate** | `-0.0107%` | **USDT Bitget** | `-0.0137%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `60.99%` | `39.01%` | `1.56` | 5,490,000.00 USD |
| `15M` | `Binance` | `60.61%` | `39.39%` | `1.54` | 2,080,000.00 USD |
| `15M` | `OKX` | `62.16%` | `37.84%` | `1.64` | 272,090.00 USD |
| `15M` | `Bybit` | `59.15%` | `40.85%` | `1.45` | 384,550.00 USD |
| `15M` | `KuCoin` | `31.89%` | `68.11%` | `0.47` | 19,200.00 USD |
| `15M` | `Gate` | `41.01%` | `58.99%` | `0.70` | 240,290.00 USD |
| `15M` | `Bitget` | `43.35%` | `56.65%` | `0.77` | 78,810.00 USD |
| `15M` | `BingX` | `70.36%` | `29.64%` | `2.37` | 779,230.00 USD |
| `15M` | `MEXC` | `65.82%` | `34.18%` | `1.93` | 368,670.00 USD |
| `15M` | `Bitunix` | `42.43%` | `57.57%` | `0.74` | 77,940.00 USD |
| `15M` | `Hyperliquid` | `58.1%` | `41.9%` | `1.39` | 41,160.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `94.08%` | `5.92%` | `15.89` | 1,090,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 662.54 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 28,030.00 USD |
| `15M` | `HTX` | `44.96%` | `55.04%` | `0.82` | 1,410.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `20.25%` | `79.75%` | `0.25` | 15,100.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `47.21%` | `52.79%` | `0.89` | 12,990.00 USD |
| `15M` | `Whale Positions` | `60.61%` | `39.39%` | `1.54` | 2,080,000.00 USD |
| `15M` | `Global Accounts` | `60.99%` | `39.01%` | `1.56` | 5,490,000.00 USD |
| `1H` | `SUI` | `53.11%` | `46.89%` | `1.13` | 29,090,000.00 USD |
| `1H` | `Binance` | `52.74%` | `47.26%` | `1.12` | 10,710,000.00 USD |
| `1H` | `OKX` | `50.17%` | `49.83%` | `1.01` | 4,200,000.00 USD |
| `1H` | `Bybit` | `52.38%` | `47.62%` | `1.10` | 2,380,000.00 USD |
| `1H` | `KuCoin` | `63.5%` | `36.5%` | `1.74` | 219,000.00 USD |
| `1H` | `Gate` | `42.69%` | `57.31%` | `0.74` | 512,250.00 USD |
| `1H` | `Bitget` | `54.91%` | `45.09%` | `1.22` | 1,130,000.00 USD |
| `1H` | `BingX` | `51.55%` | `48.45%` | `1.06` | 657,070.00 USD |
| `1H` | `MEXC` | `48.07%` | `51.93%` | `0.93` | 5,280,000.00 USD |
| `1H` | `Bitunix` | `50.04%` | `49.96%` | `1.00` | 839,490.00 USD |
| `1H` | `Hyperliquid` | `74.71%` | `25.29%` | `2.95` | 2,300,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49%` | `51%` | `0.96` | 521,510.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `71.94%` | `28.06%` | `2.56` | 131,340.00 USD |
| `1H` | `HTX` | `32.45%` | `67.55%` | `0.48` | 7,160.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `1.35%` | `98.65%` | `0.01` | 9,960.00 USD |
| `1H` | `Aster` | `50.06%` | `49.94%` | `1.00` | 173,240.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `70.56%` | `29.44%` | `2.40` | 24,910.00 USD |
| `1H` | `Whale Positions` | `52.74%` | `47.26%` | `1.12` | 10,710,000.00 USD |
| `1H` | `Global Accounts` | `53.11%` | `46.89%` | `1.13` | 29,090,000.00 USD |
| `4H` | `SUI` | `49.46%` | `50.54%` | `0.98` | 107,240,000.00 USD |
| `4H` | `Binance` | `52.81%` | `47.19%` | `1.12` | 40,410,000.00 USD |
| `4H` | `OKX` | `51.1%` | `48.9%` | `1.04` | 6,750,000.00 USD |
| `4H` | `Bybit` | `49.75%` | `50.25%` | `0.99` | 9,230,000.00 USD |
| `4H` | `KuCoin` | `46.7%` | `53.3%` | `0.88` | 1,630,000.00 USD |
| `4H` | `Gate` | `44.93%` | `55.07%` | `0.82` | 3,070,000.00 USD |
| `4H` | `Bitget` | `45.42%` | `54.58%` | `0.83` | 3,410,000.00 USD |
| `4H` | `BingX` | `43.19%` | `56.81%` | `0.76` | 14,610,000.00 USD |
| `4H` | `MEXC` | `48.43%` | `51.57%` | `0.94` | 3,740,000.00 USD |
| `4H` | `Bitunix` | `51.59%` | `48.41%` | `1.07` | 2,930,000.00 USD |
| `4H` | `Hyperliquid` | `48.38%` | `51.62%` | `0.94` | 2,860,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.93%` | `51.07%` | `0.96` | 16,710,000.00 USD |
| `4H` | `Crypto.com` | `35.43%` | `64.57%` | `0.55` | 20,030.00 USD |
| `4H` | `WhiteBIT` | `29.67%` | `70.33%` | `0.42` | 808,960.00 USD |
| `4H` | `HTX` | `58.87%` | `41.13%` | `1.43` | 60,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.93%` | `47.07%` | `1.12` | 434,460.00 USD |
| `4H` | `Aster` | `55.61%` | `44.39%` | `1.25` | 222,660.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.64%` | `59.36%` | `0.68` | 340,120.00 USD |
| `4H` | `Whale Positions` | `52.81%` | `47.19%` | `1.12` | 40,410,000.00 USD |
| `4H` | `Global Accounts` | `49.46%` | `50.54%` | `0.98` | 107,240,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.8503` | `0.8533` | `0.8503` | `0.8596` | `0.8482` | 2,970,160.51 USD | 1,607,321.44 USD | 1,362,839.07 USD | 244,482.37 USD | `+8.23%` | `19B / 6S` |
| `5:00 UTC` | `0.8605` | `0.8638` | `0.8605` | `0.8693` | `0.8592` | 3,068,721.14 USD | 1,724,308.92 USD | 1,344,412.22 USD | 379,896.70 USD | `+12.38%` | `24B / 7S` |
| `0:00 UTC` | `0.8697` | `0.8685` | `0.8697` | `0.8708` | `0.8651` | 2,460,446.55 USD | 1,349,113.11 USD | 1,111,333.44 USD | 237,779.67 USD | `+9.66%` | `7B / 9S` |
| `5:00 UTC` | `0.8680` | `0.8663` | `0.8680` | `0.8697` | `0.8640` | 1,274,072.68 USD | 628,587.96 USD | 645,484.72 USD | -16,896.75 USD | `-1.33%` | `6B / 9S` |
| `0:00 UTC` | `0.8698` | `0.8685` | `0.8698` | `0.8706` | `0.8657` | 2,093,919.35 USD | 1,157,864.07 USD | 936,055.29 USD | 221,808.78 USD | `+10.59%` | `11B / 2S` |
| `5:00 UTC` | `0.8700` | `0.8715` | `0.8700` | `0.8748` | `0.8669` | 2,353,506.52 USD | 1,517,666.93 USD | 835,839.59 USD | 681,827.34 USD | `+28.97%` | `29B / 5S` |
| `0:00 UTC` | `0.8800` | `0.8785` | `0.8800` | `0.8828` | `0.8730` | 3,913,129.55 USD | 2,396,328.40 USD | 1,516,801.15 USD | 879,527.25 USD | `+22.48%` | `20B / 6S` |
| `5:00 UTC` | `0.8851` | `0.8843` | `0.8851` | `0.8873` | `0.8813` | 3,303,378.86 USD | 1,747,933.70 USD | 1,555,445.16 USD | 192,488.53 USD | `+5.83%` | `6B / 8S` |
| `0:00 UTC` | `0.8790` | `0.8806` | `0.8790` | `0.8870` | `0.8778` | 3,823,669.01 USD | 1,840,836.89 USD | 1,982,832.12 USD | -141,995.24 USD | `-3.71%` | `23B / 14S` |
| `5:00 UTC` | `0.8903` | `0.8884` | `0.8903` | `0.8908` | `0.8844` | 3,288,119.94 USD | 1,762,888.00 USD | 1,525,231.94 USD | 237,656.05 USD | `+7.23%` | `10B / 7S` |

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
| `5m` | -16,450.00 USD | 973,270.00 USD | **`ACCUMULATION`** |
| `15m` | 695,970.00 USD | 586,630.00 USD | **`ACCUMULATION`** |
| `30m` | 556,890.00 USD | 878,500.00 USD | **`ACCUMULATION`** |
| `1h` | 720,330.00 USD | 2,810,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,150,000.00 USD | 5,010,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,220,000.00 USD | -5,030,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,390,000.00 USD | -9,410,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -11,830,000.00 USD | -19,340,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -13,950,000.00 USD | -26,700,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,940,000.00 USD | -24,960,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -26,980,000.00 USD | -86,090,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -157,230,000.00 USD | -484,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-16.45K` | 15m=`+695.97K` | 1h=`+720.33K` | 24h=`-8.94M`
* Futures Capital Netflows: 5m=`+973.27K` | 15m=`+586.63K` | 1h=`+2.81M` | 24h=`-24.96M`
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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
