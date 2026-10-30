# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:46:25 IST` (`2026-10-30 04:16:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8792` | `0.8827` | `0.8785` | `0.8821` | `2,008,476` | 1,768,216.02 USD | 702,919.97 USD | `+39.75%` | -12,209,630.70 USD | `+3.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.8821` | `0.8873` | `0.8813` | `0.8864` | `1,682,568` | 1,488,064.29 USD | 658,086.38 USD | `+44.22%` | -11,551,544.32 USD | `+2.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.8865` | `0.8866` | `0.8863` | `0.8864` | `24,498` | 21,714.91 USD | -12,857.53 USD | `-59.21%` | -11,564,401.85 USD | `-0.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8681` | `0.8747` | `0.8668` | `0.8742` | `2,700,609` | 2,353,506.52 USD | 681,827.34 USD | `+28.97%` | -13,275,603.25 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.8741` | `0.8827` | `0.8729` | `0.8821` | `4,454,501` | 3,913,129.55 USD | 879,527.25 USD | `+22.48%` | -12,396,076.00 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.8821` | `0.8873` | `0.8813` | `0.8864` | `1,707,067` | 1,509,779.19 USD | 645,228.85 USD | `+42.74%` | -11,750,847.15 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.8549` | `0.8637` | `0.8453` | `0.8555` | `17,720,786` | 15,162,870.44 USD | -425,226.29 USD | `-2.80%` | -15,024,501.36 USD | `+0.15` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8556` | `0.8707` | `0.8482` | `0.8661` | `11,338,098` | 9,773,400.88 USD | 845,261.99 USD | `+8.65%` | -14,179,239.37 USD | `+0.79` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.8661` | `0.8873` | `0.8656` | `0.8864` | `11,244,598` | 9,844,888.96 USD | 2,437,534.08 USD | `+24.76%` | -11,741,705.30 USD | `+1.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -565,079.35 USD | `-1.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,267,514.18 USD | `-1.80` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8864` | `101,471,981` | 86,669,103.53 USD | -3,483,332.97 USD | `-4.02%` | -11,750,847.15 USD | `-0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -20,484.57 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | 2,008,232.35 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -565,079.35 USD | `-1.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,267,514.18 USD | `-1.80` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8864` | `101,471,981` | 86,669,103.53 USD | -3,483,332.97 USD | `-4.02%` | -11,750,847.15 USD | `-0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `0.8796` | `145.8000` | 128.25 USD | 26,122.54 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8796` | `145.8000` | 128.25 USD | 26,250.79 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8796` | `145.8000` | 128.25 USD | 26,379.04 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8796` | `145.8000` | 128.25 USD | 26,507.28 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8796` | `4430.8000` | 3,897.33 USD | 30,404.61 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8796` | `215.7000` | 189.73 USD | 30,594.34 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8796` | `1971.3000` | 1,733.92 USD | 32,328.26 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8797` | `5841.5000` | 5,138.94 USD | 19,166.86 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8797` | `2117.1000` | 1,862.39 USD | 21,029.25 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8797` | `1000.0000` | 879.67 USD | 21,908.92 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8797` | `372.8000` | 327.94 USD | 22,236.86 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8797` | `4271.5000` | 3,757.42 USD | 25,994.29 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `0.8798` | `3521.7000` | 3,098.53 USD | 7,042.97 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8798` | `1971.3000` | 1,734.41 USD | 8,777.37 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8798` | `1971.3000` | 1,734.27 USD | 10,511.65 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8798` | `3996.9000` | 3,516.27 USD | 14,027.92 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8799` | `557.8000` | 490.79 USD | 3,497.11 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8799` | `508.4000` | 447.32 USD | 3,944.43 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `0.8800` | `898.5000` | 790.72 USD | 790.72 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.8800` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.88` | `0.00%` | `-` |
| `BID` | `0.8800` | `1138.7000` | 1,002.10 USD | 1,002.10 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.8800` | `2277.6000` | 2,004.22 USD | 3,006.32 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `0.8801` | `67.8000` | 59.67 USD | 1,202.44 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8801` | `400.0000` | 352.04 USD | 1,142.77 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8802` | `2840.2000` | 2,499.97 USD | 6,439.62 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8802` | `1971.3000` | 1,735.12 USD | 3,939.65 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8802` | `1138.5000` | 1,002.08 USD | 2,204.53 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8803` | `2271.8000` | 1,999.98 USD | 21,540.86 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8803` | `5691.3000` | 5,010.28 USD | 19,540.89 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8803` | `1971.5000` | 1,735.57 USD | 14,530.61 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8803` | `1000.0000` | 880.32 USD | 12,795.04 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8803` | `1971.5000` | 1,735.53 USD | 11,914.72 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8803` | `2276.9000` | 2,004.31 USD | 10,179.18 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8803` | `1971.3000` | 1,735.26 USD | 8,174.87 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8804` | `1971.5000` | 1,735.81 USD | 50,317.97 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8804` | `5804.7000` | 5,110.69 USD | 48,582.17 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.8804` | `22939.4000` | 20,195.16 USD | 43,471.48 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.8804` | `1971.3000` | 1,735.45 USD | 23,276.32 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8805` | `1971.3000` | 1,735.77 USD | 53,264.09 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8805` | `1136.6000` | 1,000.79 USD | 51,528.32 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8805` | `238.0000` | 209.56 USD | 50,527.53 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `659` | `0xb83d...6e36` | `SHORT` | 3,359,687.15 USD | `3,817,609.40` | `1.11` | `0.8792` | `35.17` | 859,048.16 USD | `+25.57%` | `3X Cross` |
| `999` | `0xa2ce...3126` | `LONG` | 2,197,559.14 USD | `2,500,010.40` | `0.8597` | `0.8792` | `0.000000` | 48,352.61 USD | `+2.20%` | `10X Cross` |
| `1653` | `0x9946...0852` | `SHORT` | 1,270,278.09 USD | `1,444,269.20` | `1.08` | `0.8792` | `2.00` | 288,300.78 USD | `+22.70%` | `10X Cross` |
| `1900` | `0x9df2...c665` | `SHORT` | 1,055,436.00 USD | `1,200,000.00` | `0.7465` | `0.8792` | `26.40` | -159,583.60 USD | `-15.12%` | `10X Cross` |
| `1985` | `0x9aa5...58af` | `SHORT` | 1,011,240.67 USD | `1,150,012.70` | `1.14` | `0.8792` | `8.78` | 299,042.16 USD | `+29.57%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 5,343.53 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9406 USD [API] | `2026-10-29 00:52:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9335` | 9,058.69 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 9.06K USD at 0.9335 USD [API] | `2026-10-29 01:31:02` |


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
| `Live` | `Short Liquidation` | `1.77` | 927.76 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1955` | 4,690,000.00 USD | 0.00 USD | 1,820.00 USD | `-77.89%` | `9,320.00` |
| `Live` | `Long` | `0.1965` | 4,690,000.00 USD | 0.00 USD | 736.64 USD | `-77.77%` | `3,748.80` |
| `Live` | `Long` | `0.1995` | 4,690,000.00 USD | 0.00 USD | 256.00 USD | `-77.43%` | `1,283.20` |
| `Live` | `Long` | `0.2075` | 4,690,000.00 USD | 0.00 USD | 207.50 USD | `-76.53%` | `1,000.00` |
| `Live` | `Long` | `0.2135` | 4,690,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.85%` | `18,919.90` |
| `Live` | `Long` | `0.2215` | 4,690,000.00 USD | 0.00 USD | 258.78 USD | `-74.94%` | `1,168.30` |
| `Live` | `Long` | `0.2225` | 4,690,000.00 USD | 0.00 USD | 476.28 USD | `-74.83%` | `2,140.60` |
| `Live` | `Long` | `0.2345` | 4,680,000.00 USD | 0.00 USD | 228.10 USD | `-73.47%` | `972.70` |
| `Live` | `Long` | `0.2355` | 4,680,000.00 USD | 0.00 USD | 789.66 USD | `-73.36%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,680,000.00 USD | 0.00 USD | 156.36 USD | `-73.02%` | `655.60` |
| `Live` | `Long` | `0.2505` | 4,680,000.00 USD | 0.00 USD | 250.50 USD | `-71.66%` | `1,000.00` |
| `Live` | `Long` | `0.2525` | 4,680,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.44%` | `8,897.00` |
| `Live` | `Long` | `0.2535` | 4,680,000.00 USD | 0.00 USD | 112.07 USD | `-71.32%` | `442.10` |
| `Live` | `Long` | `0.2575` | 4,680,000.00 USD | 0.00 USD | 4,350.00 USD | `-70.87%` | `16,877.10` |
| `Live` | `Long` | `0.2645` | 4,680,000.00 USD | 0.00 USD | 171.77 USD | `-70.08%` | `649.40` |
| `Live` | `Long` | `0.2685` | 4,680,000.00 USD | 0.00 USD | 106.16 USD | `-69.63%` | `395.40` |
| `Live` | `Long` | `0.2695` | 4,680,000.00 USD | 0.00 USD | 160.92 USD | `-69.51%` | `597.10` |
| `Live` | `Long` | `0.2725` | 4,680,000.00 USD | 0.00 USD | 168.46 USD | `-69.17%` | `618.20` |
| `Live` | `Long` | `0.2735` | 4,680,000.00 USD | 0.00 USD | 248.34 USD | `-69.06%` | `908.00` |
| `Live` | `Long` | `0.2785` | 4,680,000.00 USD | 0.00 USD | 3,970.00 USD | `-68.50%` | `14,245.00` |
| `Live` | `Long` | `0.2885` | 4,670,000.00 USD | 0.00 USD | 29,070.00 USD | `-67.36%` | `100,768.40` |
| `Live` | `Long` | `0.2905` | 4,640,000.00 USD | 0.00 USD | 3,540.00 USD | `-67.14%` | `12,176.00` |
| `Live` | `Long` | `0.2975` | 4,640,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.35%` | `14,561.30` |
| `Live` | `Long` | `0.2985` | 4,640,000.00 USD | 0.00 USD | 25,710.00 USD | `-66.23%` | `86,117.40` |
| `Live` | `Long` | `0.3075` | 4,610,000.00 USD | 0.00 USD | 125.89 USD | `-65.22%` | `409.40` |
| `Live` | `Long` | `0.3115` | 4,610,000.00 USD | 0.00 USD | 270.38 USD | `-64.76%` | `868.00` |
| `Live` | `Long` | `0.3175` | 4,610,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.08%` | `4,218.90` |
| `Live` | `Long` | `0.3355` | 4,610,000.00 USD | 0.00 USD | 4,170.00 USD | `-62.05%` | `12,426.00` |
| `Live` | `Long` | `0.3365` | 4,600,000.00 USD | 0.00 USD | 673.13 USD | `-61.94%` | `2,000.40` |
| `Live` | `Long` | `0.3465` | 4,600,000.00 USD | 0.00 USD | 1,230.00 USD | `-60.80%` | `3,555.40` |
| `Live` | `Long` | `0.3475` | 4,600,000.00 USD | 0.00 USD | 3,850.00 USD | `-60.69%` | `11,077.80` |
| `Live` | `Long` | `0.3505` | 4,600,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.35%` | `2,908.00` |
| `Live` | `Long` | `0.3545` | 4,600,000.00 USD | 0.00 USD | 10,100.00 USD | `-59.90%` | `28,480.20` |
| `Live` | `Long` | `0.3585` | 4,590,000.00 USD | 0.00 USD | 595.72 USD | `-59.45%` | `1,661.70` |
| `Live` | `Long` | `0.3665` | 4,590,000.00 USD | 0.00 USD | 274.88 USD | `-58.54%` | `750.00` |
| `Live` | `Long` | `0.3685` | 4,590,000.00 USD | 0.00 USD | 29,050.00 USD | `-58.32%` | `78,821.50` |
| `Live` | `Long` | `0.3785` | 4,560,000.00 USD | 0.00 USD | 3,790.00 USD | `-57.18%` | `10,000.00` |
| `Live` | `Long` | `0.3795` | 4,550,000.00 USD | 0.00 USD | 278.02 USD | `-57.07%` | `732.60` |
| `Live` | `Long` | `0.3815` | 4,550,000.00 USD | 0.00 USD | 6,490.00 USD | `-56.84%` | `17,000.00` |
| `Live` | `Long` | `0.3845` | 4,550,000.00 USD | 0.00 USD | 1,750.00 USD | `-56.51%` | `4,562.20` |
| `Live` | `Long` | `0.3855` | 4,540,000.00 USD | 0.00 USD | 269.85 USD | `-56.39%` | `700.00` |
| `Live` | `Long` | `0.3895` | 4,540,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.94%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 4,540,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.60%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,540,000.00 USD | 0.00 USD | 28,370.00 USD | `-55.37%` | `71,912.50` |
| `Live` | `Long` | `0.3995` | 4,510,000.00 USD | 0.00 USD | 724.25 USD | `-54.81%` | `1,812.90` |
| `Live` | `Long` | `0.4035` | 4,510,000.00 USD | 0.00 USD | 935.03 USD | `-54.36%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,510,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.24%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,500,000.00 USD | 0.00 USD | 3,360.00 USD | `-54.02%` | `8,275.50` |
| `Live` | `Long` | `0.4105` | 4,500,000.00 USD | 0.00 USD | 5,130.00 USD | `-53.56%` | `12,500.00` |
| `Live` | `Long` | `0.4235` | 4,490,000.00 USD | 0.00 USD | 467.50 USD | `-52.09%` | `1,103.90` |
| `Live` | `Long` | `0.4315` | 4,490,000.00 USD | 0.00 USD | 236.20 USD | `-51.19%` | `547.40` |
| `Live` | `Long` | `0.4335` | 4,490,000.00 USD | 0.00 USD | 763.83 USD | `-50.96%` | `1,762.00` |
| `Live` | `Long` | `0.4385` | 4,490,000.00 USD | 0.00 USD | 122.91 USD | `-50.40%` | `280.30` |
| `Live` | `Long` | `0.4405` | 4,490,000.00 USD | 0.00 USD | 43,880.00 USD | `-50.17%` | `99,611.70` |
| `Live` | `Long` | `0.4425` | 4,450,000.00 USD | 0.00 USD | 8,850.00 USD | `-49.94%` | `20,000.00` |
| `Live` | `Long` | `0.4435` | 4,440,000.00 USD | 0.00 USD | 219.00 USD | `-49.83%` | `493.80` |
| `Live` | `Long` | `0.4455` | 4,440,000.00 USD | 0.00 USD | 574.83 USD | `-49.61%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,440,000.00 USD | 0.00 USD | 19,600.00 USD | `-49.49%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,420,000.00 USD | 0.00 USD | 105.25 USD | `-49.38%` | `235.20` |
| `Live` | `Long` | `0.4495` | 4,420,000.00 USD | 0.00 USD | 314.65 USD | `-49.15%` | `700.00` |
| `Live` | `Long` | `0.4535` | 4,420,000.00 USD | 0.00 USD | 1,400.00 USD | `-48.70%` | `3,094.60` |
| `Live` | `Long` | `0.4595` | 4,420,000.00 USD | 0.00 USD | 3,330.00 USD | `-48.02%` | `7,245.50` |
| `Live` | `Long` | `0.4715` | 4,410,000.00 USD | 0.00 USD | 1,720.00 USD | `-46.66%` | `3,650.40` |
| `Live` | `Long` | `0.4735` | 4,410,000.00 USD | 0.00 USD | 603.48 USD | `-46.44%` | `1,274.50` |
| `Live` | `Long` | `0.4785` | 4,410,000.00 USD | 0.00 USD | 110.10 USD | `-45.87%` | `230.10` |
| `Live` | `Long` | `0.4825` | 4,410,000.00 USD | 0.00 USD | 166.70 USD | `-45.42%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,410,000.00 USD | 0.00 USD | 4,040.00 USD | `-45.31%` | `8,345.80` |
| `Live` | `Long` | `0.4855` | 4,410,000.00 USD | 0.00 USD | 3,650.00 USD | `-45.08%` | `7,509.00` |
| `Live` | `Long` | `0.4865` | 4,400,000.00 USD | 0.00 USD | 201.07 USD | `-44.97%` | `413.30` |
| `Live` | `Long` | `0.4895` | 4,400,000.00 USD | 0.00 USD | 105.34 USD | `-44.63%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,400,000.00 USD | 0.00 USD | 2,380.00 USD | `-44.40%` | `4,848.70` |
| `Live` | `Long` | `0.4935` | 4,400,000.00 USD | 0.00 USD | 5,570.00 USD | `-44.18%` | `11,290.30` |
| `Live` | `Long` | `0.4945` | 4,390,000.00 USD | 0.00 USD | 106.32 USD | `-44.06%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,390,000.00 USD | 0.00 USD | 211.88 USD | `-43.95%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,390,000.00 USD | 0.00 USD | 768.09 USD | `-43.61%` | `1,540.80` |
| `Live` | `Long` | `0.4995` | 4,390,000.00 USD | 0.00 USD | 1,520.00 USD | `-43.50%` | `3,043.40` |
| `Live` | `Long` | `0.5015` | 4,390,000.00 USD | 0.00 USD | 212.49 USD | `-43.27%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,390,000.00 USD | 0.00 USD | 1,230.00 USD | `-43.16%` | `2,451.10` |
| `Live` | `Long` | `0.5045` | 4,390,000.00 USD | 0.00 USD | 4,790.00 USD | `-42.93%` | `9,500.00` |
| `Live` | `Long` | `0.5055` | 4,380,000.00 USD | 0.00 USD | 211.25 USD | `-42.82%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,380,000.00 USD | 0.00 USD | 5,680.00 USD | `-42.48%` | `11,163.80` |
| `Live` | `Long` | `0.5095` | 4,380,000.00 USD | 0.00 USD | 195.75 USD | `-42.37%` | `384.20` |
| `Live` | `Long` | `0.5105` | 4,380,000.00 USD | 0.00 USD | 1,400.00 USD | `-42.25%` | `2,751.80` |
| `Live` | `Long` | `0.5115` | 4,380,000.00 USD | 0.00 USD | 4,120.00 USD | `-42.14%` | `8,054.90` |
| `Live` | `Long` | `0.5125` | 4,370,000.00 USD | 0.00 USD | 539.20 USD | `-42.03%` | `1,052.10` |
| `Live` | `Long` | `0.5155` | 4,370,000.00 USD | 0.00 USD | 106.04 USD | `-41.69%` | `205.70` |
| `Live` | `Long` | `0.5165` | 4,370,000.00 USD | 0.00 USD | 619.80 USD | `-41.57%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,370,000.00 USD | 0.00 USD | 213.68 USD | `-41.46%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,370,000.00 USD | 0.00 USD | 982.56 USD | `-41.35%` | `1,895.00` |
| `Live` | `Long` | `0.5205` | 4,370,000.00 USD | 0.00 USD | 439.41 USD | `-41.12%` | `844.20` |
| `Live` | `Long` | `0.5255` | 4,370,000.00 USD | 0.00 USD | 380.93 USD | `-40.56%` | `724.90` |
| `Live` | `Long` | `0.5265` | 4,370,000.00 USD | 0.00 USD | 124.73 USD | `-40.44%` | `236.90` |
| `Live` | `Long` | `0.5275` | 4,370,000.00 USD | 0.00 USD | 348.36 USD | `-40.33%` | `660.40` |
| `Live` | `Long` | `0.5295` | 4,370,000.00 USD | 0.00 USD | 123,640.00 USD | `-40.10%` | `233,498.70` |
| `Live` | `Long` | `0.5325` | 4,250,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.76%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,240,000.00 USD | 0.00 USD | 7,810.00 USD | `-39.54%` | `14,603.90` |
| `Live` | `Long` | `0.5355` | 4,240,000.00 USD | 0.00 USD | 113.47 USD | `-39.42%` | `211.90` |
| `Live` | `Long` | `0.5405` | 4,240,000.00 USD | 0.00 USD | 7,090.00 USD | `-38.86%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,230,000.00 USD | 0.00 USD | 269.13 USD | `-38.63%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,230,000.00 USD | 0.00 USD | 230.32 USD | `-38.41%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,230,000.00 USD | 0.00 USD | 6,210.00 USD | `-38.18%` | `11,362.00` |
| `Live` | `Long` | `0.5475` | 4,220,000.00 USD | 0.00 USD | 1,240.00 USD | `-38.07%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,220,000.00 USD | 0.00 USD | 29,340.00 USD | `-37.84%` | `53,392.10` |
| `Live` | `Long` | `0.5505` | 4,190,000.00 USD | 0.00 USD | 248.06 USD | `-37.73%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,190,000.00 USD | 0.00 USD | 160.93 USD | `-37.61%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,190,000.00 USD | 0.00 USD | 582.56 USD | `-37.50%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,190,000.00 USD | 0.00 USD | 271.88 USD | `-37.39%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,190,000.00 USD | 0.00 USD | 531.60 USD | `-37.28%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,190,000.00 USD | 0.00 USD | 7,950.00 USD | `-37.16%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,180,000.00 USD | 0.00 USD | 141.97 USD | `-36.82%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,180,000.00 USD | 0.00 USD | 304.93 USD | `-36.71%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,180,000.00 USD | 0.00 USD | 441.84 USD | `-36.60%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,180,000.00 USD | 0.00 USD | 330.53 USD | `-36.37%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,180,000.00 USD | 0.00 USD | 534.03 USD | `-36.26%` | `947.70` |
| `Live` | `Long` | `0.5655` | 4,180,000.00 USD | 0.00 USD | 8,190.00 USD | `-36.03%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,170,000.00 USD | 0.00 USD | 7,200.00 USD | `-35.92%` | `12,714.00` |
| `Live` | `Long` | `0.5675` | 4,160,000.00 USD | 0.00 USD | 1,560.00 USD | `-35.80%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,160,000.00 USD | 0.00 USD | 973.22 USD | `-35.58%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,160,000.00 USD | 0.00 USD | 139.23 USD | `-35.24%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,160,000.00 USD | 0.00 USD | 182.72 USD | `-35.13%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,160,000.00 USD | 0.00 USD | 144.03 USD | `-35.01%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,160,000.00 USD | 0.00 USD | 217.37 USD | `-34.90%` | `377.70` |
| `Live` | `Long` | `0.5765` | 4,160,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.79%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,160,000.00 USD | 0.00 USD | 497.75 USD | `-34.67%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,160,000.00 USD | 0.00 USD | 141.85 USD | `-34.56%` | `245.20` |
| `Live` | `Long` | `0.5795` | 4,160,000.00 USD | 0.00 USD | 212.85 USD | `-34.45%` | `367.30` |
| `Live` | `Long` | `0.5805` | 4,160,000.00 USD | 0.00 USD | 1,410.00 USD | `-34.33%` | `2,422.00` |
| `Live` | `Long` | `0.5815` | 4,160,000.00 USD | 0.00 USD | 268.59 USD | `-34.22%` | `461.90` |
| `Live` | `Long` | `0.5825` | 4,160,000.00 USD | 0.00 USD | 6,470.00 USD | `-34.11%` | `11,099.00` |
| `Live` | `Long` | `0.5835` | 4,150,000.00 USD | 0.00 USD | 353.48 USD | `-33.99%` | `605.80` |
| `Live` | `Long` | `0.5855` | 4,150,000.00 USD | 0.00 USD | 2,640.00 USD | `-33.77%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,150,000.00 USD | 0.00 USD | 466.85 USD | `-33.66%` | `796.00` |
| `Live` | `Long` | `0.5885` | 4,150,000.00 USD | 0.00 USD | 311.14 USD | `-33.43%` | `528.70` |
| `Live` | `Long` | `0.5905` | 4,150,000.00 USD | 0.00 USD | 412.11 USD | `-33.20%` | `697.90` |
| `Live` | `Long` | `0.5925` | 4,150,000.00 USD | 0.00 USD | 994.16 USD | `-32.98%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,150,000.00 USD | 0.00 USD | 132.41 USD | `-32.86%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,150,000.00 USD | 0.00 USD | 8,220.00 USD | `-32.75%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,140,000.00 USD | 0.00 USD | 7,050.00 USD | `-32.52%` | `11,825.60` |
| `Live` | `Long` | `0.5975` | 4,130,000.00 USD | 0.00 USD | 4,360.00 USD | `-32.41%` | `7,291.60` |
| `Live` | `Long` | `0.5985` | 4,130,000.00 USD | 0.00 USD | 299.25 USD | `-32.30%` | `500.00` |
| `Live` | `Long` | `0.5995` | 4,130,000.00 USD | 0.00 USD | 4,760.00 USD | `-32.18%` | `7,936.80` |
| `Live` | `Long` | `0.6005` | 4,120,000.00 USD | 0.00 USD | 351.11 USD | `-32.07%` | `584.70` |
| `Live` | `Long` | `0.6015` | 4,120,000.00 USD | 0.00 USD | 323.79 USD | `-31.96%` | `538.30` |
| `Live` | `Long` | `0.6025` | 4,120,000.00 USD | 0.00 USD | 432.35 USD | `-31.85%` | `717.60` |
| `Live` | `Long` | `0.6035` | 4,120,000.00 USD | 0.00 USD | 1,220.00 USD | `-31.73%` | `2,023.70` |
| `Live` | `Long` | `0.6075` | 4,120,000.00 USD | 0.00 USD | 851.05 USD | `-31.28%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,120,000.00 USD | 0.00 USD | 886.10 USD | `-31.17%` | `1,456.20` |
| `Live` | `Long` | `0.6095` | 4,120,000.00 USD | 0.00 USD | 214.54 USD | `-31.05%` | `352.00` |
| `Live` | `Long` | `0.6115` | 4,120,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.83%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 4,110,000.00 USD | 0.00 USD | 438.73 USD | `-30.71%` | `716.30` |
| `Live` | `Long` | `0.6135` | 4,110,000.00 USD | 0.00 USD | 112.33 USD | `-30.60%` | `183.10` |
| `Live` | `Long` | `0.6145` | 4,110,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.49%` | `3,435.00` |
| `Live` | `Long` | `0.6155` | 4,110,000.00 USD | 0.00 USD | 935.13 USD | `-30.37%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 4,110,000.00 USD | 0.00 USD | 29,900.00 USD | `-30.26%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 4,080,000.00 USD | 0.00 USD | 4,980.00 USD | `-30.15%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 4,070,000.00 USD | 0.00 USD | 12,570.00 USD | `-30.04%` | `20,327.90` |
| `Live` | `Long` | `0.6195` | 4,060,000.00 USD | 0.00 USD | 2,400.00 USD | `-29.92%` | `3,868.00` |
| `Live` | `Long` | `0.6215` | 4,060,000.00 USD | 0.00 USD | 14,820.00 USD | `-29.70%` | `23,839.90` |
| `Live` | `Long` | `0.6225` | 4,040,000.00 USD | 0.00 USD | 90,210.00 USD | `-29.58%` | `144,922.60` |
| `Live` | `Long` | `0.6245` | 3,950,000.00 USD | 0.00 USD | 356.65 USD | `-29.36%` | `571.10` |
| `Live` | `Long` | `0.6255` | 3,950,000.00 USD | 0.00 USD | 32,630.00 USD | `-29.24%` | `52,170.80` |
| `Live` | `Long` | `0.6285` | 3,920,000.00 USD | 0.00 USD | 102.45 USD | `-28.90%` | `163.00` |
| `Live` | `Long` | `0.6295` | 3,920,000.00 USD | 0.00 USD | 1,100.00 USD | `-28.79%` | `1,739.60` |
| `Live` | `Long` | `0.6305` | 3,920,000.00 USD | 0.00 USD | 319.35 USD | `-28.68%` | `506.50` |
| `Live` | `Long` | `0.6345` | 3,920,000.00 USD | 0.00 USD | 843.00 USD | `-28.23%` | `1,328.60` |
| `Live` | `Long` | `0.6365` | 3,920,000.00 USD | 0.00 USD | 3,060.00 USD | `-28.00%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,910,000.00 USD | 0.00 USD | 1,100.00 USD | `-27.89%` | `1,726.70` |
| `Live` | `Long` | `0.6395` | 3,910,000.00 USD | 0.00 USD | 319.75 USD | `-27.66%` | `500.00` |
| `Live` | `Long` | `0.6405` | 3,910,000.00 USD | 0.00 USD | 33,040.00 USD | `-27.55%` | `51,581.80` |
| `Live` | `Long` | `0.6415` | 3,880,000.00 USD | 0.00 USD | 86,920.00 USD | `-27.43%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,790,000.00 USD | 0.00 USD | 4,980.00 USD | `-27.32%` | `7,754.70` |
| `Live` | `Long` | `0.6435` | 3,790,000.00 USD | 0.00 USD | 3,190.00 USD | `-27.21%` | `4,951.30` |
| `Live` | `Long` | `0.6445` | 3,780,000.00 USD | 0.00 USD | 65,790.00 USD | `-27.09%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,720,000.00 USD | 0.00 USD | 14,590.00 USD | `-26.98%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,700,000.00 USD | 0.00 USD | 146.76 USD | `-26.87%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,700,000.00 USD | 0.00 USD | 3,200.00 USD | `-26.76%` | `4,945.10` |
| `Live` | `Long` | `0.6485` | 3,700,000.00 USD | 0.00 USD | 668.34 USD | `-26.64%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,700,000.00 USD | 0.00 USD | 539.67 USD | `-26.53%` | `830.90` |
| `Live` | `Long` | `0.6505` | 3,700,000.00 USD | 0.00 USD | 2,340.00 USD | `-26.42%` | `3,604.50` |
| `Live` | `Long` | `0.6515` | 3,700,000.00 USD | 0.00 USD | 403,320.00 USD | `-26.30%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,290,000.00 USD | 0.00 USD | 2,350.00 USD | `-26.19%` | `3,599.00` |
| `Live` | `Long` | `0.6535` | 3,290,000.00 USD | 0.00 USD | 127,900.00 USD | `-26.08%` | `195,717.60` |
| `Live` | `Long` | `0.6545` | 3,160,000.00 USD | 0.00 USD | 6,700.00 USD | `-25.96%` | `10,231.40` |
| `Live` | `Long` | `0.6555` | 3,160,000.00 USD | 0.00 USD | 10,760.00 USD | `-25.85%` | `16,411.10` |
| `Live` | `Long` | `0.6565` | 3,150,000.00 USD | 0.00 USD | 8,220.00 USD | `-25.74%` | `12,525.80` |
| `Live` | `Long` | `0.6575` | 3,140,000.00 USD | 0.00 USD | 13,280.00 USD | `-25.62%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,120,000.00 USD | 0.00 USD | 2,970.00 USD | `-25.51%` | `4,508.30` |
| `Live` | `Long` | `0.6605` | 3,120,000.00 USD | 0.00 USD | 6,740.00 USD | `-25.28%` | `10,200.00` |
| `Live` | `Long` | `0.6615` | 3,110,000.00 USD | 0.00 USD | 325.46 USD | `-25.17%` | `492.00` |
| `Live` | `Long` | `0.6625` | 3,110,000.00 USD | 0.00 USD | 4,840.00 USD | `-25.06%` | `7,306.80` |
| `Live` | `Long` | `0.6645` | 3,110,000.00 USD | 0.00 USD | 634.00 USD | `-24.83%` | `954.10` |
| `Live` | `Long` | `0.6665` | 3,110,000.00 USD | 0.00 USD | 528.73 USD | `-24.61%` | `793.30` |
| `Live` | `Long` | `0.6675` | 3,110,000.00 USD | 0.00 USD | 3,050.00 USD | `-24.49%` | `4,574.20` |
| `Live` | `Long` | `0.6685` | 3,100,000.00 USD | 0.00 USD | 135.71 USD | `-24.38%` | `203.00` |
| `Live` | `Long` | `0.6695` | 3,100,000.00 USD | 0.00 USD | 337.36 USD | `-24.27%` | `503.90` |
| `Live` | `Long` | `0.6705` | 3,100,000.00 USD | 0.00 USD | 2,290.00 USD | `-24.15%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,100,000.00 USD | 0.00 USD | 2,240.00 USD | `-24.04%` | `3,341.20` |
| `Live` | `Long` | `0.6725` | 3,100,000.00 USD | 0.00 USD | 1,280.00 USD | `-23.93%` | `1,906.60` |
| `Live` | `Long` | `0.6735` | 3,100,000.00 USD | 0.00 USD | 633.09 USD | `-23.81%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,100,000.00 USD | 0.00 USD | 33,610.00 USD | `-23.70%` | `49,828.00` |
| `Live` | `Long` | `0.6755` | 3,060,000.00 USD | 0.00 USD | 854.64 USD | `-23.59%` | `1,265.20` |
| `Live` | `Long` | `0.6765` | 3,060,000.00 USD | 0.00 USD | 189.22 USD | `-23.47%` | `279.70` |
| `Live` | `Long` | `0.6775` | 3,060,000.00 USD | 0.00 USD | 9,350.00 USD | `-23.36%` | `13,800.00` |
| `Live` | `Long` | `0.6785` | 3,050,000.00 USD | 0.00 USD | 122.94 USD | `-23.25%` | `181.20` |
| `Live` | `Long` | `0.6795` | 3,050,000.00 USD | 0.00 USD | 43,650.00 USD | `-23.14%` | `64,238.50` |
| `Live` | `Long` | `0.6805` | 3,010,000.00 USD | 0.00 USD | 1,600.00 USD | `-23.02%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 3,010,000.00 USD | 0.00 USD | 2,110.00 USD | `-22.91%` | `3,092.70` |
| `Live` | `Long` | `0.6825` | 3,010,000.00 USD | 0.00 USD | 17,190.00 USD | `-22.80%` | `25,192.00` |
| `Live` | `Long` | `0.6835` | 2,990,000.00 USD | 0.00 USD | 15,130.00 USD | `-22.68%` | `22,136.50` |
| `Live` | `Long` | `0.6845` | 2,970,000.00 USD | 0.00 USD | 5,960.00 USD | `-22.57%` | `8,711.60` |
| `Live` | `Long` | `0.6865` | 2,970,000.00 USD | 0.00 USD | 112.59 USD | `-22.34%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,970,000.00 USD | 0.00 USD | 6,110.00 USD | `-22.23%` | `8,883.90` |
| `Live` | `Long` | `0.6885` | 2,960,000.00 USD | 0.00 USD | 1,060.00 USD | `-22.12%` | `1,536.40` |
| `Live` | `Long` | `0.6895` | 2,960,000.00 USD | 0.00 USD | 2,110.00 USD | `-22.00%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,960,000.00 USD | 0.00 USD | 3,360.00 USD | `-21.89%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,960,000.00 USD | 0.00 USD | 10,590.00 USD | `-21.78%` | `15,317.60` |
| `Live` | `Long` | `0.6935` | 2,940,000.00 USD | 0.00 USD | 3,600.00 USD | `-21.55%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 2,940,000.00 USD | 0.00 USD | 7,670.00 USD | `-21.44%` | `11,040.00` |
| `Live` | `Long` | `0.6955` | 2,930,000.00 USD | 0.00 USD | 1,700.00 USD | `-21.33%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,930,000.00 USD | 0.00 USD | 273.03 USD | `-21.21%` | `392.00` |
| `Live` | `Long` | `0.6975` | 2,930,000.00 USD | 0.00 USD | 1,030.00 USD | `-21.10%` | `1,482.80` |
| `Live` | `Long` | `0.6985` | 2,930,000.00 USD | 0.00 USD | 1,670.00 USD | `-20.99%` | `2,396.30` |
| `Live` | `Long` | `0.7015` | 2,930,000.00 USD | 0.00 USD | 1,990.00 USD | `-20.65%` | `2,841.50` |
| `Live` | `Long` | `0.7045` | 2,930,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.31%` | `12,729.60` |
| `Live` | `Long` | `0.7065` | 2,920,000.00 USD | 0.00 USD | 143.14 USD | `-20.08%` | `202.60` |
| `Live` | `Long` | `0.7075` | 2,920,000.00 USD | 0.00 USD | 3,620.00 USD | `-19.97%` | `5,122.60` |
| `Live` | `Long` | `0.7085` | 2,910,000.00 USD | 0.00 USD | 2,020.00 USD | `-19.85%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,910,000.00 USD | 0.00 USD | 1,110.00 USD | `-19.74%` | `1,568.50` |
| `Live` | `Long` | `0.7105` | 2,910,000.00 USD | 0.00 USD | 25,230.00 USD | `-19.63%` | `35,512.10` |
| `Live` | `Long` | `0.7125` | 2,890,000.00 USD | 0.00 USD | 283.22 USD | `-19.40%` | `397.50` |
| `Live` | `Long` | `0.7135` | 2,890,000.00 USD | 0.00 USD | 1,440.00 USD | `-19.29%` | `2,023.70` |
| `Live` | `Long` | `0.7145` | 2,880,000.00 USD | 0.00 USD | 297.23 USD | `-19.18%` | `416.00` |
| `Live` | `Long` | `0.7155` | 2,880,000.00 USD | 0.00 USD | 12,470.00 USD | `-19.06%` | `17,421.50` |
| `Live` | `Long` | `0.7165` | 2,870,000.00 USD | 0.00 USD | 4,620.00 USD | `-18.95%` | `6,444.00` |
| `Live` | `Long` | `0.7185` | 2,870,000.00 USD | 0.00 USD | 431,230.00 USD | `-18.72%` | `600,176.70` |
| `Live` | `Long` | `0.7195` | 2,440,000.00 USD | 0.00 USD | 420.19 USD | `-18.61%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,430,000.00 USD | 0.00 USD | 8,450.00 USD | `-18.38%` | `11,706.20` |
| `Live` | `Long` | `0.7225` | 2,430,000.00 USD | 0.00 USD | 1,420.00 USD | `-18.27%` | `1,965.70` |
| `Live` | `Long` | `0.7235` | 2,420,000.00 USD | 0.00 USD | 127.05 USD | `-18.16%` | `175.60` |
| `Live` | `Long` | `0.7245` | 2,420,000.00 USD | 0.00 USD | 2,520.00 USD | `-18.04%` | `3,475.80` |
| `Live` | `Long` | `0.7255` | 2,420,000.00 USD | 0.00 USD | 311.60 USD | `-17.93%` | `429.50` |
| `Live` | `Long` | `0.7265` | 2,420,000.00 USD | 0.00 USD | 3,410.00 USD | `-17.82%` | `4,687.00` |
| `Live` | `Long` | `0.7275` | 2,420,000.00 USD | 0.00 USD | 36,540.00 USD | `-17.71%` | `50,227.70` |
| `Live` | `Long` | `0.7285` | 2,380,000.00 USD | 0.00 USD | 8,840.00 USD | `-17.59%` | `12,129.10` |
| `Live` | `Long` | `0.7295` | 2,370,000.00 USD | 0.00 USD | 3,990.00 USD | `-17.48%` | `5,465.30` |
| `Live` | `Long` | `0.7305` | 2,370,000.00 USD | 0.00 USD | 119.88 USD | `-17.37%` | `164.10` |
| `Live` | `Long` | `0.7325` | 2,370,000.00 USD | 0.00 USD | 13,500.00 USD | `-17.14%` | `18,432.50` |
| `Live` | `Long` | `0.7335` | 2,360,000.00 USD | 0.00 USD | 12,160.00 USD | `-17.03%` | `16,573.90` |
| `Live` | `Long` | `0.7345` | 2,340,000.00 USD | 0.00 USD | 2,340.00 USD | `-16.91%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,340,000.00 USD | 0.00 USD | 51,920.00 USD | `-16.80%` | `70,595.50` |
| `Live` | `Long` | `0.7375` | 2,290,000.00 USD | 0.00 USD | 3,450.00 USD | `-16.57%` | `4,683.00` |
| `Live` | `Long` | `0.7385` | 2,290,000.00 USD | 0.00 USD | 6,020.00 USD | `-16.46%` | `8,146.50` |
| `Live` | `Long` | `0.7395` | 2,280,000.00 USD | 0.00 USD | 3,380.00 USD | `-16.35%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,280,000.00 USD | 0.00 USD | 3,530.00 USD | `-16.23%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,270,000.00 USD | 0.00 USD | 382.61 USD | `-16.12%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,270,000.00 USD | 0.00 USD | 2,280.00 USD | `-16.01%` | `3,074.90` |
| `Live` | `Long` | `0.7435` | 2,270,000.00 USD | 0.00 USD | 784,400.00 USD | `-15.90%` | `1,055,008.20` |
| `Live` | `Long` | `0.7455` | 1,490,000.00 USD | 0.00 USD | 2,160.00 USD | `-15.67%` | `2,892.60` |
| `Live` | `Long` | `0.7465` | 1,480,000.00 USD | 0.00 USD | 359.96 USD | `-15.56%` | `482.20` |
| `Live` | `Long` | `0.7475` | 1,480,000.00 USD | 0.00 USD | 107,260.00 USD | `-15.44%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,380,000.00 USD | 0.00 USD | 599.60 USD | `-15.22%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,380,000.00 USD | 0.00 USD | 1,210.00 USD | `-14.99%` | `1,613.50` |
| `Live` | `Long` | `0.7535` | 1,370,000.00 USD | 0.00 USD | 264.86 USD | `-14.76%` | `351.50` |
| `Live` | `Long` | `0.7545` | 1,370,000.00 USD | 0.00 USD | 1,250.00 USD | `-14.65%` | `1,650.60` |
| `Live` | `Long` | `0.7555` | 1,370,000.00 USD | 0.00 USD | 1,750.00 USD | `-14.54%` | `2,315.50` |
| `Live` | `Long` | `0.7575` | 1,370,000.00 USD | 0.00 USD | 1,900.00 USD | `-14.31%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,370,000.00 USD | 0.00 USD | 40,520.00 USD | `-14.20%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,330,000.00 USD | 0.00 USD | 4,900.00 USD | `-14.09%` | `6,448.30` |
| `Live` | `Long` | `0.7615` | 1,320,000.00 USD | 0.00 USD | 351.43 USD | `-13.86%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,320,000.00 USD | 0.00 USD | 3,790.00 USD | `-13.75%` | `4,966.90` |
| `Live` | `Long` | `0.7635` | 1,320,000.00 USD | 0.00 USD | 5,550.00 USD | `-13.63%` | `7,271.90` |
| `Live` | `Long` | `0.7645` | 1,310,000.00 USD | 0.00 USD | 3,510.00 USD | `-13.52%` | `4,596.60` |
| `Live` | `Long` | `0.7655` | 1,310,000.00 USD | 0.00 USD | 4,430.00 USD | `-13.41%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,310,000.00 USD | 0.00 USD | 1,260.00 USD | `-13.29%` | `1,649.10` |
| `Live` | `Long` | `0.7675` | 1,300,000.00 USD | 0.00 USD | 25,580.00 USD | `-13.18%` | `33,323.60` |
| `Live` | `Long` | `0.7685` | 1,280,000.00 USD | 0.00 USD | 207.19 USD | `-13.07%` | `269.60` |
| `Live` | `Long` | `0.7695` | 1,280,000.00 USD | 0.00 USD | 150,510.00 USD | `-12.95%` | `195,593.50` |
| `Live` | `Long` | `0.7705` | 1,130,000.00 USD | 0.00 USD | 5,640.00 USD | `-12.84%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 1,120,000.00 USD | 0.00 USD | 19,250.00 USD | `-12.73%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 1,100,000.00 USD | 0.00 USD | 1,940.00 USD | `-12.62%` | `2,515.50` |
| `Live` | `Long` | `0.7735` | 1,100,000.00 USD | 0.00 USD | 5,230.00 USD | `-12.50%` | `6,756.40` |
| `Live` | `Long` | `0.7755` | 1,100,000.00 USD | 0.00 USD | 3,430.00 USD | `-12.28%` | `4,424.80` |
| `Live` | `Long` | `0.7765` | 1,090,000.00 USD | 0.00 USD | 3,510.00 USD | `-12.16%` | `4,518.50` |
| `Live` | `Long` | `0.7775` | 1,090,000.00 USD | 0.00 USD | 321,490.00 USD | `-12.05%` | `413,488.90` |
| `Live` | `Long` | `0.7785` | 767,850.00 USD | 0.00 USD | 28,010.00 USD | `-11.94%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 739,840.00 USD | 0.00 USD | 338.69 USD | `-11.82%` | `434.50` |
| `Live` | `Long` | `0.7815` | 739,500.00 USD | 0.00 USD | 4,160.00 USD | `-11.60%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 735,340.00 USD | 0.00 USD | 21,600.00 USD | `-11.37%` | `27,572.80` |
| `Live` | `Long` | `0.7845` | 713,740.00 USD | 0.00 USD | 155.96 USD | `-11.26%` | `198.80` |
| `Live` | `Long` | `0.7865` | 713,580.00 USD | 0.00 USD | 3,470.00 USD | `-11.03%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 710,110.00 USD | 0.00 USD | 288.70 USD | `-10.92%` | `366.60` |
| `Live` | `Long` | `0.7905` | 709,820.00 USD | 0.00 USD | 3,670.00 USD | `-10.58%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 706,150.00 USD | 0.00 USD | 7,620.00 USD | `-10.47%` | `9,623.00` |
| `Live` | `Long` | `0.7925` | 698,540.00 USD | 0.00 USD | 10,810.00 USD | `-10.35%` | `13,636.90` |
| `Live` | `Long` | `0.7935` | 687,730.00 USD | 0.00 USD | 809.45 USD | `-10.24%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 686,920.00 USD | 0.00 USD | 736.66 USD | `-10.13%` | `927.20` |
| `Live` | `Long` | `0.7955` | 686,180.00 USD | 0.00 USD | 53,850.00 USD | `-10.01%` | `67,697.90` |
| `Live` | `Long` | `0.7965` | 632,330.00 USD | 0.00 USD | 12,980.00 USD | `-9.90%` | `16,300.50` |
| `Live` | `Long` | `0.7975` | 619,350.00 USD | 0.00 USD | 7,580.00 USD | `-9.79%` | `9,508.60` |
| `Live` | `Long` | `0.7985` | 611,760.00 USD | 0.00 USD | 40,230.00 USD | `-9.67%` | `50,386.80` |
| `Live` | `Long` | `0.7995` | 571,530.00 USD | 0.00 USD | 10,050.00 USD | `-9.56%` | `12,576.50` |
| `Live` | `Long` | `0.8005` | 561,470.00 USD | 0.00 USD | 3,850.00 USD | `-9.45%` | `4,809.40` |
| `Live` | `Long` | `0.8015` | 557,620.00 USD | 0.00 USD | 7,610.00 USD | `-9.33%` | `9,500.20` |
| `Live` | `Long` | `0.8025` | 550,010.00 USD | 0.00 USD | 1,350.00 USD | `-9.22%` | `1,686.70` |
| `Live` | `Long` | `0.8035` | 548,660.00 USD | 0.00 USD | 7,680.00 USD | `-9.11%` | `9,559.90` |
| `Live` | `Long` | `0.8045` | 540,980.00 USD | 0.00 USD | 16,660.00 USD | `-9.00%` | `20,710.00` |
| `Live` | `Long` | `0.8055` | 524,310.00 USD | 0.00 USD | 361.11 USD | `-8.88%` | `448.30` |
| `Live` | `Long` | `0.8065` | 523,950.00 USD | 0.00 USD | 6,910.00 USD | `-8.77%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 517,040.00 USD | 0.00 USD | 2,770.00 USD | `-8.66%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 514,270.00 USD | 0.00 USD | 22,510.00 USD | `-8.54%` | `27,845.30` |
| `Live` | `Long` | `0.8095` | 491,760.00 USD | 0.00 USD | 130,110.00 USD | `-8.43%` | `160,732.40` |
| `Live` | `Long` | `0.8105` | 361,650.00 USD | 0.00 USD | 2,430.00 USD | `-8.32%` | `3,000.50` |
| `Live` | `Long` | `0.8115` | 359,220.00 USD | 0.00 USD | 2,970.00 USD | `-8.20%` | `3,654.30` |
| `Live` | `Long` | `0.8125` | 356,250.00 USD | 0.00 USD | 1,160.00 USD | `-8.09%` | `1,421.60` |
| `Live` | `Long` | `0.8135` | 355,100.00 USD | 0.00 USD | 3,800.00 USD | `-7.98%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 351,290.00 USD | 0.00 USD | 277.42 USD | `-7.86%` | `340.60` |
| `Live` | `Long` | `0.8155` | 351,010.00 USD | 0.00 USD | 38,250.00 USD | `-7.75%` | `46,908.50` |
| `Live` | `Long` | `0.8165` | 312,760.00 USD | 0.00 USD | 492.27 USD | `-7.64%` | `602.90` |
| `Live` | `Long` | `0.8175` | 312,270.00 USD | 0.00 USD | 77,840.00 USD | `-7.52%` | `95,214.30` |
| `Live` | `Long` | `0.8185` | 234,430.00 USD | 0.00 USD | 28,030.00 USD | `-7.41%` | `34,240.00` |
| `Live` | `Long` | `0.8195` | 206,410.00 USD | 0.00 USD | 1,110.00 USD | `-7.30%` | `1,360.00` |
| `Live` | `Long` | `0.8205` | 205,290.00 USD | 0.00 USD | 9,370.00 USD | `-7.19%` | `11,414.00` |
| `Live` | `Long` | `0.8215` | 195,930.00 USD | 0.00 USD | 474.01 USD | `-7.07%` | `577.00` |
| `Live` | `Long` | `0.8225` | 195,450.00 USD | 0.00 USD | 3,080.00 USD | `-6.96%` | `3,747.80` |
| `Live` | `Long` | `0.8235` | 192,370.00 USD | 0.00 USD | 463.63 USD | `-6.85%` | `563.00` |
| `Live` | `Long` | `0.8245` | 191,910.00 USD | 0.00 USD | 18,980.00 USD | `-6.73%` | `23,022.60` |
| `Live` | `Long` | `0.8255` | 172,920.00 USD | 0.00 USD | 1,580.00 USD | `-6.62%` | `1,911.90` |
| `Live` | `Long` | `0.8275` | 171,340.00 USD | 0.00 USD | 4,690.00 USD | `-6.39%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 166,660.00 USD | 0.00 USD | 120,070.00 USD | `-6.28%` | `144,926.90` |
| `Live` | `Long` | `0.8295` | 46,590.00 USD | 0.00 USD | 46,590.00 USD | `-6.17%` | `56,161.30` |
| `Live` | `Short` | `0.8395` | 190.31 USD | 190.31 USD | 0.00 USD | `-5.04%` | `226.70` |
| `Live` | `Short` | `0.8885` | 512.93 USD | 322.61 USD | 0.00 USD | `+0.51%` | `363.10` |
| `Live` | `Short` | `0.8925` | 1,320.00 USD | 807.44 USD | 0.00 USD | `+0.96%` | `904.70` |
| `Live` | `Short` | `0.8935` | 3,840.00 USD | 2,520.00 USD | 0.00 USD | `+1.07%` | `2,815.00` |
| `Live` | `Short` | `0.8965` | 4,020.00 USD | 187.46 USD | 0.00 USD | `+1.41%` | `209.10` |
| `Live` | `Short` | `0.9145` | 8,090.00 USD | 4,060.00 USD | 0.00 USD | `+3.45%` | `4,444.10` |
| `Live` | `Short` | `0.9175` | 11,000.00 USD | 2,910.00 USD | 0.00 USD | `+3.79%` | `3,170.30` |
| `Live` | `Short` | `0.9305` | 15,210.00 USD | 4,210.00 USD | 0.00 USD | `+5.26%` | `4,523.60` |
| `Live` | `Short` | `0.9325` | 15,730.00 USD | 523.13 USD | 0.00 USD | `+5.48%` | `561.00` |
| `Live` | `Short` | `0.9385` | 55,570.00 USD | 39,850.00 USD | 0.00 USD | `+6.16%` | `42,456.90` |
| `Live` | `Short` | `0.9805` | 56,620.00 USD | 1,050.00 USD | 0.00 USD | `+10.91%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 56,990.00 USD | 365.70 USD | 0.00 USD | `+11.59%` | `370.70` |
| `Live` | `Short` | `0.9885` | 61,240.00 USD | 4,250.00 USD | 0.00 USD | `+11.82%` | `4,304.30` |
| `Live` | `Short` | `0.9905` | 62,810.00 USD | 1,570.00 USD | 0.00 USD | `+12.04%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 62,950.00 USD | 139.59 USD | 0.00 USD | `+12.38%` | `140.50` |
| `Live` | `Short` | `1.00` | 63,280.00 USD | 330.29 USD | 0.00 USD | `+13.29%` | `329.80` |
| `Live` | `Short` | `1.01` | 63,380.00 USD | 100.65 USD | 0.00 USD | `+13.85%` | `100.00` |
| `Live` | `Short` | `1.01` | 64,090.00 USD | 705.99 USD | 0.00 USD | `+14.76%` | `695.90` |
| `Live` | `Short` | `1.02` | 64,260.00 USD | 170.40 USD | 0.00 USD | `+14.87%` | `167.80` |
| `Live` | `Short` | `1.02` | 65,930.00 USD | 1,670.00 USD | 0.00 USD | `+15.21%` | `1,639.00` |
| `Live` | `Short` | `1.04` | 66,090.00 USD | 155.92 USD | 0.00 USD | `+17.59%` | `150.00` |
| `Live` | `Short` | `1.05` | 66,680.00 USD | 597.52 USD | 0.00 USD | `+18.83%` | `568.80` |
| `Live` | `Short` | `1.05` | 69,070.00 USD | 2,390.00 USD | 0.00 USD | `+18.95%` | `2,272.10` |
| `Live` | `Short` | `1.08` | 72,650.00 USD | 3,580.00 USD | 0.00 USD | `+22.23%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 78,210.00 USD | 5,550.00 USD | 0.00 USD | `+23.24%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 78,530.00 USD | 324.90 USD | 0.00 USD | `+24.38%` | `295.50` |
| `Live` | `Short` | `1.10` | 78,810.00 USD | 277.22 USD | 0.00 USD | `+24.49%` | `251.90` |
| `Live` | `Short` | `1.10` | 80,110.00 USD | 1,310.00 USD | 0.00 USD | `+24.94%` | `1,182.10` |
| `Live` | `Short` | `1.11` | 89,050.00 USD | 8,940.00 USD | 0.00 USD | `+25.62%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 112,360.00 USD | 23,310.00 USD | 0.00 USD | `+27.43%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 112,990.00 USD | 634.09 USD | 0.00 USD | `+28.11%` | `559.90` |
| `Live` | `Short` | `1.20` | 113,170.00 USD | 177.65 USD | 0.00 USD | `+35.69%` | `148.10` |
| `Live` | `Short` | `1.22` | 117,620.00 USD | 4,440.00 USD | 0.00 USD | `+37.84%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 118,000.00 USD | 383.01 USD | 0.00 USD | `+38.29%` | `313.30` |
| `Live` | `Short` | `1.23` | 118,380.00 USD | 380.84 USD | 0.00 USD | `+39.65%` | `308.50` |
| `Live` | `Short` | `1.24` | 122,300.00 USD | 3,930.00 USD | 0.00 USD | `+40.10%` | `3,169.40` |
| `Live` | `Short` | `1.24` | 123,530.00 USD | 1,230.00 USD | 0.00 USD | `+40.32%` | `989.90` |
| `Live` | `Short` | `1.26` | 126,200.00 USD | 2,670.00 USD | 0.00 USD | `+42.47%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 128,510.00 USD | 2,300.00 USD | 0.00 USD | `+44.51%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 168,390.00 USD | 39,880.00 USD | 0.00 USD | `+45.08%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 178,200.00 USD | 9,820.00 USD | 0.00 USD | `+45.75%` | `7,618.00` |
| `Live` | `Short` | `1.29` | 178,430.00 USD | 226.80 USD | 0.00 USD | `+46.43%` | `175.20` |
| `Live` | `Short` | `1.30` | 178,550.00 USD | 114.40 USD | 0.00 USD | `+46.89%` | `88.10` |
| `Live` | `Short` | `1.31` | 179,560.00 USD | 1,020.00 USD | 0.00 USD | `+48.13%` | `777.20` |
| `Live` | `Short` | `1.31` | 211,090.00 USD | 31,530.00 USD | 0.00 USD | `+48.36%` | `24,042.40` |
| `Live` | `Short` | `1.32` | 211,320.00 USD | 229.23 USD | 0.00 USD | `+49.71%` | `173.20` |
| `Live` | `Short` | `1.33` | 217,660.00 USD | 6,340.00 USD | 0.00 USD | `+49.94%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 239,630.00 USD | 21,970.00 USD | 0.00 USD | `+50.28%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 246,490.00 USD | 6,860.00 USD | 0.00 USD | `+51.52%` | `5,119.30` |
| `Live` | `Short` | `1.34` | 247,590.00 USD | 1,110.00 USD | 0.00 USD | `+51.75%` | `826.40` |
| `Live` | `Short` | `1.35` | 270,360.00 USD | 22,760.00 USD | 0.00 USD | `+53.11%` | `16,816.80` |
| `Live` | `Short` | `1.37` | 628,640.00 USD | 358,280.00 USD | 0.00 USD | `+55.26%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 633,080.00 USD | 4,450.00 USD | 0.00 USD | `+60.01%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 633,490.00 USD | 402.08 USD | 0.00 USD | `+62.50%` | `279.90` |
| `Live` | `Short` | `1.44` | 633,770.00 USD | 288.68 USD | 0.00 USD | `+62.95%` | `200.40` |
| `Live` | `Short` | `1.45` | 633,920.00 USD | 142.05 USD | 0.00 USD | `+63.63%` | `98.20` |
| `Live` | `Short` | `1.50` | 650,700.00 USD | 16,780.00 USD | 0.00 USD | `+69.74%` | `11,182.60` |
| `Live` | `Short` | `1.51` | 654,720.00 USD | 4,020.00 USD | 0.00 USD | `+71.32%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 654,870.00 USD | 152.85 USD | 0.00 USD | `+72.90%` | `100.00` |
| `Live` | `Short` | `1.53` | 664,800.00 USD | 9,930.00 USD | 0.00 USD | `+73.13%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 664,950.00 USD | 144.34 USD | 0.00 USD | `+73.70%` | `94.00` |
| `Live` | `Short` | `1.58` | 665,230.00 USD | 285.21 USD | 0.00 USD | `+78.45%` | `180.80` |
| `Live` | `Short` | `1.59` | 666,420.00 USD | 1,180.00 USD | 0.00 USD | `+80.26%` | `743.20` |
| `Live` | `Short` | `1.60` | 666,540.00 USD | 123.81 USD | 0.00 USD | `+80.71%` | `77.50` |
| `Live` | `Short` | `1.60` | 666,680.00 USD | 135.24 USD | 0.00 USD | `+81.05%` | `84.50` |
| `Live` | `Short` | `1.60` | 667,810.00 USD | 1,130.00 USD | 0.00 USD | `+81.27%` | `704.60` |
| `Live` | `Short` | `1.65` | 689,140.00 USD | 21,330.00 USD | 0.00 USD | `+86.25%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 693,080.00 USD | 3,940.00 USD | 0.00 USD | `+87.04%` | `2,381.50` |
| `Live` | `Short` | `1.66` | 696,700.00 USD | 3,620.00 USD | 0.00 USD | `+87.72%` | `2,184.10` |
| `Live` | `Short` | `1.66` | 735,800.00 USD | 39,090.00 USD | 0.00 USD | `+87.95%` | `23,529.40` |
| `Live` | `Short` | `1.66` | 1,030,000.00 USD | 290,220.00 USD | 0.00 USD | `+88.29%` | `174,360.10` |
| `Live` | `Short` | `1.69` | 1,030,000.00 USD | 150.02 USD | 0.00 USD | `+90.89%` | `88.90` |
| `Live` | `Short` | `1.71` | 1,030,000.00 USD | 205.67 USD | 0.00 USD | `+93.72%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,040,000.00 USD | 9,700.00 USD | 0.00 USD | `+94.28%` | `5,645.40` |
| `Live` | `Short` | `1.72` | 1,040,000.00 USD | 492.06 USD | 0.00 USD | `+94.96%` | `285.50` |
| `Live` | `Short` | `1.73` | 1,040,000.00 USD | 226.05 USD | 0.00 USD | `+96.09%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,040,000.00 USD | 2,080.00 USD | 0.00 USD | `+97.00%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 1,040,000.00 USD | 983.07 USD | 0.00 USD | `+97.45%` | `563.20` |
| `Live` | `Short` | `1.75` | 1,050,000.00 USD | 7,000.00 USD | 0.00 USD | `+98.02%` | `4,000.00` |
| `Live` | `Short` | `1.75` | 1,070,000.00 USD | 19,920.00 USD | 0.00 USD | `+98.13%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 1,080,000.00 USD | 11,350.00 USD | 0.00 USD | `+98.36%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,080,000.00 USD | 1,520.00 USD | 0.00 USD | `+98.47%` | `868.90` |
| `Live` | `Short` | `1.77` | 1,080,000.00 USD | 927.76 USD | 0.00 USD | `+100.05%` | `524.60` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,230,000.00 USD | 0.00 USD | 497.31 USD | `-70.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2745` | 1,230,000.00 USD | 0.00 USD | 455.97 USD | `-68.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,230,000.00 USD | 0.00 USD | 102.75 USD | `-61.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,230,000.00 USD | 0.00 USD | 256.78 USD | `-60.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,230,000.00 USD | 0.00 USD | 428.87 USD | `-56.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,230,000.00 USD | 0.00 USD | 123.45 USD | `-53.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,230,000.00 USD | 0.00 USD | 818.15 USD | `-52.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,230,000.00 USD | 0.00 USD | 436.41 USD | `-50.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,230,000.00 USD | 0.00 USD | 876.79 USD | `-50.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,220,000.00 USD | 0.00 USD | 466.72 USD | `-49.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,220,000.00 USD | 0.00 USD | 142.95 USD | `-46.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,220,000.00 USD | 0.00 USD | 3,010.00 USD | `-43.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,220,000.00 USD | 0.00 USD | 151.74 USD | `-41.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,220,000.00 USD | 0.00 USD | 123.91 USD | `-41.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,220,000.00 USD | 0.00 USD | 219.80 USD | `-37.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,220,000.00 USD | 0.00 USD | 237,400.00 USD | `-37.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 983,370.00 USD | 0.00 USD | 276.75 USD | `-37.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 983,090.00 USD | 0.00 USD | 1,680.00 USD | `-36.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 981,410.00 USD | 0.00 USD | 853.41 USD | `-35.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 980,560.00 USD | 0.00 USD | 119.76 USD | `-34.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 980,440.00 USD | 0.00 USD | 3,520.00 USD | `-33.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 976,910.00 USD | 0.00 USD | 470.62 USD | `-32.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 976,440.00 USD | 0.00 USD | 108.39 USD | `-32.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 976,330.00 USD | 0.00 USD | 123.28 USD | `-31.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 976,210.00 USD | 0.00 USD | 488.52 USD | `-29.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 975,720.00 USD | 0.00 USD | 4,230.00 USD | `-29.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 971,500.00 USD | 0.00 USD | 242.24 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 971,250.00 USD | 0.00 USD | 193.95 USD | `-26.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 971,060.00 USD | 0.00 USD | 149.22 USD | `-26.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 970,910.00 USD | 0.00 USD | 158.54 USD | `-26.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 970,750.00 USD | 0.00 USD | 195.47 USD | `-25.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 970,560.00 USD | 0.00 USD | 112.91 USD | `-25.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 970,440.00 USD | 0.00 USD | 181.31 USD | `-25.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 970,260.00 USD | 0.00 USD | 190.25 USD | `-25.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 970,070.00 USD | 0.00 USD | 153.53 USD | `-24.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 969,920.00 USD | 0.00 USD | 52,450.00 USD | `-24.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 917,470.00 USD | 0.00 USD | 536.11 USD | `-23.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 916,930.00 USD | 0.00 USD | 918.68 USD | `-23.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 916,020.00 USD | 0.00 USD | 340.75 USD | `-22.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 915,680.00 USD | 0.00 USD | 9,270.00 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 906,410.00 USD | 0.00 USD | 120.53 USD | `-21.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 906,290.00 USD | 0.00 USD | 160.71 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 906,130.00 USD | 0.00 USD | 738.08 USD | `-21.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 905,390.00 USD | 0.00 USD | 187.61 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 905,200.00 USD | 0.00 USD | 8,500.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 896,710.00 USD | 0.00 USD | 89,150.00 USD | `-20.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 807,560.00 USD | 0.00 USD | 189.06 USD | `-20.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 807,370.00 USD | 0.00 USD | 5,650.00 USD | `-19.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 801,720.00 USD | 0.00 USD | 371.68 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 801,340.00 USD | 0.00 USD | 152.05 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 801,190.00 USD | 0.00 USD | 123.41 USD | `-18.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 801,070.00 USD | 0.00 USD | 745.54 USD | `-17.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 800,320.00 USD | 0.00 USD | 1,130.00 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 799,190.00 USD | 0.00 USD | 18,770.00 USD | `-17.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 780,420.00 USD | 0.00 USD | 7,970.00 USD | `-17.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 772,450.00 USD | 0.00 USD | 257.26 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 772,200.00 USD | 0.00 USD | 161.72 USD | `-16.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 772,030.00 USD | 0.00 USD | 1,590.00 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 770,440.00 USD | 0.00 USD | 10,160.00 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 760,280.00 USD | 0.00 USD | 94,190.00 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 666,090.00 USD | 0.00 USD | 1,230.00 USD | `-14.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 664,860.00 USD | 0.00 USD | 1,840.00 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 663,020.00 USD | 0.00 USD | 804.61 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 662,220.00 USD | 0.00 USD | 590.68 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 661,630.00 USD | 0.00 USD | 635.62 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 660,990.00 USD | 0.00 USD | 191.12 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 660,800.00 USD | 0.00 USD | 273.92 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 660,530.00 USD | 0.00 USD | 125.92 USD | `-12.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 660,400.00 USD | 0.00 USD | 1,980.00 USD | `-12.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 658,430.00 USD | 0.00 USD | 1,150.00 USD | `-12.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 657,280.00 USD | 0.00 USD | 1,500.00 USD | `-12.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 655,780.00 USD | 0.00 USD | 1,860.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 653,920.00 USD | 0.00 USD | 128.47 USD | `-11.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 653,790.00 USD | 0.00 USD | 6,960.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 646,840.00 USD | 0.00 USD | 135.11 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 646,700.00 USD | 0.00 USD | 8,870.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 637,830.00 USD | 0.00 USD | 1,500.00 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7935` | 636,330.00 USD | 0.00 USD | 1,290.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 635,050.00 USD | 0.00 USD | 23,420.00 USD | `-10.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 611,620.00 USD | 0.00 USD | 103.42 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 611,520.00 USD | 0.00 USD | 1,260.00 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 610,260.00 USD | 0.00 USD | 319.40 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 609,940.00 USD | 0.00 USD | 4,740.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 605,200.00 USD | 0.00 USD | 2,590.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 602,610.00 USD | 0.00 USD | 144.67 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 602,470.00 USD | 0.00 USD | 1,510.00 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 600,960.00 USD | 0.00 USD | 50,540.00 USD | `-8.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 550,420.00 USD | 0.00 USD | 263.25 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 550,160.00 USD | 0.00 USD | 1,250.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 548,910.00 USD | 0.00 USD | 181,850.00 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 367,060.00 USD | 0.00 USD | 353.81 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 366,700.00 USD | 0.00 USD | 1,010.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 365,690.00 USD | 0.00 USD | 123,350.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 242,340.00 USD | 0.00 USD | 1,160.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 241,180.00 USD | 0.00 USD | 216.70 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 240,960.00 USD | 0.00 USD | 125.72 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 240,840.00 USD | 0.00 USD | 375.49 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 240,460.00 USD | 0.00 USD | 21,270.00 USD | `-7.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 219,190.00 USD | 0.00 USD | 7,160.00 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 212,040.00 USD | 0.00 USD | 226.71 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 211,810.00 USD | 0.00 USD | 3,780.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 208,030.00 USD | 0.00 USD | 1,320.00 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 206,710.00 USD | 0.00 USD | 325.56 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 206,380.00 USD | 0.00 USD | 666.55 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 205,720.00 USD | 0.00 USD | 577.25 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 205,140.00 USD | 0.00 USD | 3,950.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 201,190.00 USD | 0.00 USD | 171.46 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 201,020.00 USD | 0.00 USD | 13,500.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 187,520.00 USD | 0.00 USD | 690.30 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 186,830.00 USD | 0.00 USD | 144.54 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 186,680.00 USD | 0.00 USD | 263.43 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 186,420.00 USD | 0.00 USD | 610.23 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 185,810.00 USD | 0.00 USD | 699.65 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 185,110.00 USD | 0.00 USD | 320.31 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 184,790.00 USD | 0.00 USD | 240.52 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 184,550.00 USD | 0.00 USD | 388.23 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 184,160.00 USD | 0.00 USD | 510.57 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 183,650.00 USD | 0.00 USD | 212.81 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 183,440.00 USD | 0.00 USD | 2,950.00 USD | `-4.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 180,490.00 USD | 0.00 USD | 12,850.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 167,630.00 USD | 0.00 USD | 481.80 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 167,150.00 USD | 0.00 USD | 451.83 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 166,700.00 USD | 0.00 USD | 25,350.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8525` | 141,350.00 USD | 0.00 USD | 6,990.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 134,360.00 USD | 0.00 USD | 345.13 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 134,020.00 USD | 0.00 USD | 16,630.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 117,390.00 USD | 0.00 USD | 1,470.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 115,920.00 USD | 0.00 USD | 4,010.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 111,910.00 USD | 0.00 USD | 8,900.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 103,010.00 USD | 0.00 USD | 1,740.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 101,270.00 USD | 0.00 USD | 3,880.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 97,390.00 USD | 0.00 USD | 6,160.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 91,230.00 USD | 0.00 USD | 4,190.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 87,040.00 USD | 0.00 USD | 987.33 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 86,060.00 USD | 0.00 USD | 2,420.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 83,640.00 USD | 0.00 USD | 3,310.00 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 80,330.00 USD | 0.00 USD | 6,910.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 73,420.00 USD | 0.00 USD | 741.45 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 72,680.00 USD | 0.00 USD | 410.11 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 72,270.00 USD | 0.00 USD | 5,340.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 66,930.00 USD | 0.00 USD | 11,960.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 54,970.00 USD | 0.00 USD | 712.45 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 54,260.00 USD | 0.00 USD | 116.74 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 54,140.00 USD | 0.00 USD | 314.55 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 53,830.00 USD | 0.00 USD | 866.37 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 52,960.00 USD | 0.00 USD | 35,020.00 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 17,940.00 USD | 0.00 USD | 635.29 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 17,310.00 USD | 0.00 USD | 9,070.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 8,240.00 USD | 0.00 USD | 151.10 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 8,090.00 USD | 0.00 USD | 2,000.00 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 6,090.00 USD | 0.00 USD | 1,030.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 5,060.00 USD | 0.00 USD | 4,070.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 989.59 USD | 0.00 USD | 563.65 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 425.94 USD | 0.00 USD | 425.94 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 4,210.00 USD | 4,210.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 7,810.00 USD | 3,600.00 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 8,050.00 USD | 235.54 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 19,410.00 USD | 11,360.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 28,190.00 USD | 8,780.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 29,210.00 USD | 1,020.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 29,680.00 USD | 469.91 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 40,280.00 USD | 10,610.00 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 40,560.00 USD | 277.07 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 40,660.00 USD | 100.09 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 40,820.00 USD | 155.10 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 41,110.00 USD | 289.12 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 59,310.00 USD | 18,210.00 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 60,200.00 USD | 889.43 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 89,170.00 USD | 28,960.00 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 91,180.00 USD | 2,020.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 93,240.00 USD | 2,050.00 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 94,160.00 USD | 926.06 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 94,350.00 USD | 188.92 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 97,310.00 USD | 2,950.00 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 99,300.00 USD | 1,990.00 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 99,440.00 USD | 138.69 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 99,690.00 USD | 250.83 USD | 0.00 USD | `+2.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 100,780.00 USD | 1,090.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 102,300.00 USD | 1,520.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 103,240.00 USD | 933.08 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 103,500.00 USD | 260.23 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 106,390.00 USD | 2,890.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 109,410.00 USD | 3,020.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 112,480.00 USD | 3,070.00 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 113,050.00 USD | 570.08 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 113,360.00 USD | 309.14 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 117,260.00 USD | 3,900.00 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 119,240.00 USD | 1,970.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 119,350.00 USD | 116.59 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 378,470.00 USD | 259,120.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 530,430.00 USD | 151,960.00 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 535,510.00 USD | 5,070.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 536,000.00 USD | 495.00 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 537,400.00 USD | 1,400.00 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 542,280.00 USD | 4,880.00 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 544,480.00 USD | 2,200.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 544,770.00 USD | 287.62 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 544,970.00 USD | 199.16 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 545,100.00 USD | 130.59 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 545,550.00 USD | 448.69 USD | 0.00 USD | `+5.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 545,670.00 USD | 120.16 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 546,700.00 USD | 1,030.00 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 547,270.00 USD | 568.87 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 547,560.00 USD | 292.78 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 548,090.00 USD | 523.79 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 548,790.00 USD | 701.16 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 548,890.00 USD | 104.53 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 601,950.00 USD | 53,060.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 605,860.00 USD | 3,910.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 614,820.00 USD | 8,960.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 615,350.00 USD | 529.50 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 615,650.00 USD | 301.79 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 617,350.00 USD | 1,700.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 618,140.00 USD | 789.04 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 618,260.00 USD | 117.81 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 619,310.00 USD | 1,050.00 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 625,320.00 USD | 6,000.00 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 644,440.00 USD | 19,120.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 644,700.00 USD | 261.97 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 648,920.00 USD | 4,220.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 649,080.00 USD | 159.19 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 658,990.00 USD | 9,910.00 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 662,140.00 USD | 3,150.00 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 663,580.00 USD | 1,440.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 666,460.00 USD | 2,890.00 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 667,590.00 USD | 1,130.00 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 667,720.00 USD | 121.54 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 667,870.00 USD | 155.06 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 720,380.00 USD | 52,510.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 720,540.00 USD | 161.82 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 739,940.00 USD | 19,400.00 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 740,080.00 USD | 139.23 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 741,420.00 USD | 1,340.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 741,950.00 USD | 537.78 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 742,490.00 USD | 531.57 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 745,650.00 USD | 3,160.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 746,640.00 USD | 993.78 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 746,850.00 USD | 212.90 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 758,530.00 USD | 11,680.00 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 758,660.00 USD | 125.61 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 759,100.00 USD | 441.51 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 769,290.00 USD | 10,190.00 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 769,540.00 USD | 253.14 USD | 0.00 USD | `+10.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 773,740.00 USD | 4,200.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 773,920.00 USD | 176.73 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 774,430.00 USD | 513.32 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 809,790.00 USD | 35,360.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 841,640.00 USD | 31,850.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 846,440.00 USD | 4,800.00 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 847,000.00 USD | 558.35 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 848,060.00 USD | 1,060.00 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 849,240.00 USD | 1,180.00 USD | 0.00 USD | `+11.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 849,730.00 USD | 490.99 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 850,130.00 USD | 395.21 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 851,120.00 USD | 991.50 USD | 0.00 USD | `+12.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 861,450.00 USD | 10,340.00 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 861,860.00 USD | 409.52 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 862,150.00 USD | 284.92 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 862,500.00 USD | 350.37 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 862,620.00 USD | 124.04 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 862,740.00 USD | 117.26 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 864,920.00 USD | 2,180.00 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 865,700.00 USD | 778.64 USD | 0.00 USD | `+13.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 866,060.00 USD | 363.87 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 866,650.00 USD | 589.52 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 866,760.00 USD | 110.62 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 876,840.00 USD | 10,090.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 882,270.00 USD | 5,420.00 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 884,790.00 USD | 2,520.00 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 885,040.00 USD | 248.49 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 894,190.00 USD | 9,150.00 USD | 0.00 USD | `+14.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 894,910.00 USD | 722.63 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 895,220.00 USD | 312.07 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 895,400.00 USD | 171.24 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 895,960.00 USD | 561.11 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 896,210.00 USD | 249.30 USD | 0.00 USD | `+16.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 897,670.00 USD | 1,470.00 USD | 0.00 USD | `+16.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 898,100.00 USD | 432.18 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 898,240.00 USD | 137.88 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 900,590.00 USD | 2,340.00 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 901,280.00 USD | 694.72 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 901,440.00 USD | 160.60 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 908,000.00 USD | 6,560.00 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 910,910.00 USD | 2,920.00 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 911,140.00 USD | 224.56 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 914,710.00 USD | 3,570.00 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 915,140.00 USD | 432.19 USD | 0.00 USD | `+18.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 916,850.00 USD | 1,700.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,610,000.00 USD | 1,690,000.00 USD | 0.00 USD | `+19.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,620,000.00 USD | 5,390.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,620,000.00 USD | 285.32 USD | 0.00 USD | `+19.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,620,000.00 USD | 1,130.00 USD | 0.00 USD | `+19.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,620,000.00 USD | 1,240.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,620,000.00 USD | 278.06 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,620,000.00 USD | 309.00 USD | 0.00 USD | `+20.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,620,000.00 USD | 228.98 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,620,000.00 USD | 272.12 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,620,000.00 USD | 117.12 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,760,000.00 USD | 140,120.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,760,000.00 USD | 530.01 USD | 0.00 USD | `+21.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,760,000.00 USD | 128.23 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,870,000.00 USD | 108,190.00 USD | 0.00 USD | `+22.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,870,000.00 USD | 3,430.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,870,000.00 USD | 550.49 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,880,000.00 USD | 5,810.00 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,880,000.00 USD | 1,520.00 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,890,000.00 USD | 5,570.00 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,890,000.00 USD | 1,290.00 USD | 0.00 USD | `+23.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,890,000.00 USD | 294.81 USD | 0.00 USD | `+23.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,890,000.00 USD | 183.11 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,890,000.00 USD | 123.13 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,890,000.00 USD | 494.98 USD | 0.00 USD | `+24.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,890,000.00 USD | 613.52 USD | 0.00 USD | `+24.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,000,000.00 USD | 115,100.00 USD | 0.00 USD | `+24.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,000,000.00 USD | 409.76 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,000,000.00 USD | 162.77 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,010,000.00 USD | 959.70 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,010,000.00 USD | 160.18 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,010,000.00 USD | 669.85 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,010,000.00 USD | 293.61 USD | 0.00 USD | `+26.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,120,000.00 USD | 112,050.00 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,120,000.00 USD | 462.47 USD | 0.00 USD | `+27.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,120,000.00 USD | 2,180.00 USD | 0.00 USD | `+27.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,120,000.00 USD | 273.34 USD | 0.00 USD | `+27.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,120,000.00 USD | 119.49 USD | 0.00 USD | `+27.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,140,000.00 USD | 20,740.00 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,140,000.00 USD | 468.47 USD | 0.00 USD | `+28.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,140,000.00 USD | 1,430.00 USD | 0.00 USD | `+29.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,140,000.00 USD | 338.50 USD | 0.00 USD | `+29.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,150,000.00 USD | 2,640.00 USD | 0.00 USD | `+30.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,150,000.00 USD | 1,230.00 USD | 0.00 USD | `+30.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,150,000.00 USD | 2,450.00 USD | 0.00 USD | `+30.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,150,000.00 USD | 1,250.00 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,150,000.00 USD | 143.67 USD | 0.00 USD | `+31.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,150,000.00 USD | 989.81 USD | 0.00 USD | `+32.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,150,000.00 USD | 304.33 USD | 0.00 USD | `+32.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,150,000.00 USD | 255.14 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,150,000.00 USD | 241.65 USD | 0.00 USD | `+33.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,150,000.00 USD | 239.97 USD | 0.00 USD | `+33.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,160,000.00 USD | 2,470.00 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,160,000.00 USD | 3,060.00 USD | 0.00 USD | `+33.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,470,000.00 USD | 310,250.00 USD | 0.00 USD | `+34.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,470,000.00 USD | 309.53 USD | 0.00 USD | `+34.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,470,000.00 USD | 159.09 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,470,000.00 USD | 146.21 USD | 0.00 USD | `+35.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,490,000.00 USD | 18,420.00 USD | 0.00 USD | `+35.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,490,000.00 USD | 933.81 USD | 0.00 USD | `+35.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,490,000.00 USD | 658.86 USD | 0.00 USD | `+36.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,700,000.00 USD | 213,390.00 USD | 0.00 USD | `+36.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,700,000.00 USD | 560.05 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,710,000.00 USD | 1,050.00 USD | 0.00 USD | `+37.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,710,000.00 USD | 509.71 USD | 0.00 USD | `+38.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,710,000.00 USD | 162.15 USD | 0.00 USD | `+38.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,710,000.00 USD | 187.04 USD | 0.00 USD | `+39.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,710,000.00 USD | 542.12 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,730,000.00 USD | 23,740.00 USD | 0.00 USD | `+39.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,730,000.00 USD | 2,010.00 USD | 0.00 USD | `+39.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,730,000.00 USD | 345.91 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,730,000.00 USD | 104.79 USD | 0.00 USD | `+41.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,730,000.00 USD | 100.04 USD | 0.00 USD | `+41.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,730,000.00 USD | 517.52 USD | 0.00 USD | `+42.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,730,000.00 USD | 152.29 USD | 0.00 USD | `+42.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,740,000.00 USD | 1,480.00 USD | 0.00 USD | `+42.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,740,000.00 USD | 1,010.00 USD | 0.00 USD | `+42.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,740,000.00 USD | 2,780.00 USD | 0.00 USD | `+43.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,740,000.00 USD | 340.38 USD | 0.00 USD | `+43.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,740,000.00 USD | 903.22 USD | 0.00 USD | `+43.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,740,000.00 USD | 475.01 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,780,000.00 USD | 41,160.00 USD | 0.00 USD | `+44.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,800,000.00 USD | 12,840.00 USD | 0.00 USD | `+45.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,990,000.00 USD | 194,770.00 USD | 0.00 USD | `+45.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,000,000.00 USD | 12,890.00 USD | 0.00 USD | `+45.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,010,000.00 USD | 8,820.00 USD | 0.00 USD | `+45.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,010,000.00 USD | 466.95 USD | 0.00 USD | `+46.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,010,000.00 USD | 613.59 USD | 0.00 USD | `+46.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,010,000.00 USD | 1,420.00 USD | 0.00 USD | `+46.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,030,000.00 USD | 13,000.00 USD | 0.00 USD | `+47.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,030,000.00 USD | 284.42 USD | 0.00 USD | `+47.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 4,050,000.00 USD | 22,810.00 USD | 0.00 USD | `+49.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,050,000.00 USD | 640.82 USD | 0.00 USD | `+50.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,050,000.00 USD | 134.75 USD | 0.00 USD | `+50.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 4,060,000.00 USD | 13,400.00 USD | 0.00 USD | `+51.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,080,000.00 USD | 13,490.00 USD | 0.00 USD | `+52.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,090,000.00 USD | 11,580.00 USD | 0.00 USD | `+52.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,090,000.00 USD | 3,610.00 USD | 0.00 USD | `+53.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,090,000.00 USD | 1,500.00 USD | 0.00 USD | `+54.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,110,000.00 USD | 15,000.00 USD | 0.00 USD | `+54.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,120,000.00 USD | 9,030.00 USD | 0.00 USD | `+55.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,120,000.00 USD | 405.86 USD | 0.00 USD | `+57.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,130,000.00 USD | 13,890.00 USD | 0.00 USD | `+57.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,150,000.00 USD | 14,000.00 USD | 0.00 USD | `+58.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,160,000.00 USD | 12,560.00 USD | 0.00 USD | `+58.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,190,000.00 USD | 32,860.00 USD | 0.00 USD | `+59.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,190,000.00 USD | 102.40 USD | 0.00 USD | `+59.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,190,000.00 USD | 106.64 USD | 0.00 USD | `+59.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,190,000.00 USD | 1,430.00 USD | 0.00 USD | `+60.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,200,000.00 USD | 2,810.00 USD | 0.00 USD | `+60.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,210,000.00 USD | 8,420.00 USD | 0.00 USD | `+60.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,210,000.00 USD | 1,410.00 USD | 0.00 USD | `+61.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,210,000.00 USD | 145.37 USD | 0.00 USD | `+62.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,210,000.00 USD | 1,390.00 USD | 0.00 USD | `+62.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,220,000.00 USD | 14,390.00 USD | 0.00 USD | `+62.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,230,000.00 USD | 7,000.00 USD | 0.00 USD | `+63.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,240,000.00 USD | 14,490.00 USD | 0.00 USD | `+63.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,250,000.00 USD | 1,370.00 USD | 0.00 USD | `+64.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,250,000.00 USD | 1,350.00 USD | 0.00 USD | `+65.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,250,000.00 USD | 1,340.00 USD | 0.00 USD | `+65.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,250,000.00 USD | 342.08 USD | 0.00 USD | `+66.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,250,000.00 USD | 1,330.00 USD | 0.00 USD | `+67.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,250,000.00 USD | 1,310.00 USD | 0.00 USD | `+68.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,270,000.00 USD | 14,890.00 USD | 0.00 USD | `+68.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,280,000.00 USD | 9,580.00 USD | 0.00 USD | `+68.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,290,000.00 USD | 14,980.00 USD | 0.00 USD | `+69.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,310,000.00 USD | 20,120.00 USD | 0.00 USD | `+69.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,310,000.00 USD | 1,180.00 USD | 0.00 USD | `+69.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,310,000.00 USD | 1,260.00 USD | 0.00 USD | `+72.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,320,000.00 USD | 2,150.00 USD | 0.00 USD | `+74.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,320,000.00 USD | 158.76 USD | 0.00 USD | `+76.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,320,000.00 USD | 574.53 USD | 0.00 USD | `+80.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,320,000.00 USD | 391.32 USD | 0.00 USD | `+81.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,320,000.00 USD | 1,160.00 USD | 0.00 USD | `+83.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,320,000.00 USD | 1,140.00 USD | 0.00 USD | `+85.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,320,000.00 USD | 1,970.00 USD | 0.00 USD | `+85.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,320,000.00 USD | 281.45 USD | 0.00 USD | `+87.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,320,000.00 USD | 2,070.00 USD | 0.00 USD | `+87.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,340,000.00 USD | 13,060.00 USD | 0.00 USD | `+92.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,340,000.00 USD | 1,070.00 USD | 0.00 USD | `+97.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,340,000.00 USD | 320.52 USD | 0.00 USD | `+98.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 4,340,000.00 USD | 1,710.00 USD | 0.00 USD | `+99.83%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `568.64M` | Total OI Tokens: `647,623,865.8 SUI`
  * 1h OI Change: `+0.96%` | 4h OI Change: `-2.40%` | 24h OI Change: `-7.51%`
  * Exchange Breakdown: Binance=`103.49M` | Bybit=`76.62M` | OKX=`33.13M` | Hyperliquid=`29.35M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-32.73K` | Last 24h: `-2.19K` | Last 3d: `56.09K` | Last 7d: `151.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0142%` | **USDT OKX** | `-0.0128%` |
| **USDT Bybit** | `-0.0231%` | **USDT KuCoin** | `-0.0093%` |
| **USDT MEXC** | `-0.0139%` | **USDT BingX** | `-0.0101%` |
| **USDT Gate** | `-0.0109%` | **USDT Bitget** | `-0.0133%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `35.56%` | `64.44%` | `0.55` | 5,530,000.00 USD |
| `15M` | `Binance` | `29.36%` | `70.64%` | `0.42` | 2,120,000.00 USD |
| `15M` | `OKX` | `37.8%` | `62.2%` | `0.61` | 231,570.00 USD |
| `15M` | `Bybit` | `40.73%` | `59.27%` | `0.69` | 647,210.00 USD |
| `15M` | `KuCoin` | `42.6%` | `57.4%` | `0.74` | 40,140.00 USD |
| `15M` | `Gate` | `29.06%` | `70.94%` | `0.41` | 126,140.00 USD |
| `15M` | `Bitget` | `44.52%` | `55.48%` | `0.80` | 80,740.00 USD |
| `15M` | `BingX` | `45.77%` | `54.23%` | `0.84` | 781,600.00 USD |
| `15M` | `MEXC` | `25.93%` | `74.07%` | `0.35` | 152,800.00 USD |
| `15M` | `Bitunix` | `57.08%` | `42.92%` | `1.33` | 83,440.00 USD |
| `15M` | `Hyperliquid` | `25.55%` | `74.45%` | `0.34` | 105,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `37.58%` | `62.42%` | `0.60` | 1,120,000.00 USD |
| `15M` | `Crypto.com` | `3.07%` | `96.93%` | `0.03` | 164.34 USD |
| `15M` | `WhiteBIT` | `19.45%` | `80.55%` | `0.24` | 25,150.00 USD |
| `15M` | `HTX` | `54.87%` | `45.13%` | `1.22` | 692.20 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 25.27 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `36.42%` | `63.58%` | `0.57` | 16,080.00 USD |
| `15M` | `Whale Positions` | `29.36%` | `70.64%` | `0.42` | 2,120,000.00 USD |
| `15M` | `Global Accounts` | `35.56%` | `64.44%` | `0.55` | 5,530,000.00 USD |
| `1H` | `SUI` | `47.91%` | `52.09%` | `0.92` | 41,230,000.00 USD |
| `1H` | `Binance` | `48.82%` | `51.18%` | `0.95` | 16,900,000.00 USD |
| `1H` | `OKX` | `50.45%` | `49.55%` | `1.02` | 4,600,000.00 USD |
| `1H` | `Bybit` | `54.07%` | `45.93%` | `1.18` | 8,060,000.00 USD |
| `1H` | `KuCoin` | `49.78%` | `50.22%` | `0.99` | 700,300.00 USD |
| `1H` | `Gate` | `33.33%` | `66.67%` | `0.50` | 4,820,000.00 USD |
| `1H` | `Bitget` | `45.21%` | `54.79%` | `0.83` | 2,780,000.00 USD |
| `1H` | `BingX` | `27.27%` | `72.73%` | `0.37` | 344,150.00 USD |
| `1H` | `MEXC` | `47.7%` | `52.3%` | `0.91` | 615,980.00 USD |
| `1H` | `Bitunix` | `47.69%` | `52.31%` | `0.91` | 492,850.00 USD |
| `1H` | `Hyperliquid` | `67.18%` | `32.82%` | `2.05` | 688,110.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.95%` | `58.05%` | `0.72` | 553,200.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `37.23%` | `62.77%` | `0.59` | 142,680.00 USD |
| `1H` | `HTX` | `42.52%` | `57.48%` | `0.74` | 189,970.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `54.8%` | `45.2%` | `1.21` | 1,880.00 USD |
| `1H` | `Aster` | `39.13%` | `60.87%` | `0.64` | 45,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.51%` | `52.49%` | `0.91` | 304,280.00 USD |
| `1H` | `Whale Positions` | `48.82%` | `51.18%` | `0.95` | 16,900,000.00 USD |
| `1H` | `Global Accounts` | `47.91%` | `52.09%` | `0.92` | 41,230,000.00 USD |
| `4H` | `SUI` | `49.76%` | `50.24%` | `0.99` | 224,510,000.00 USD |
| `4H` | `Binance` | `50.9%` | `49.1%` | `1.04` | 87,240,000.00 USD |
| `4H` | `OKX` | `51.46%` | `48.54%` | `1.06` | 21,060,000.00 USD |
| `4H` | `Bybit` | `45.04%` | `54.96%` | `0.82` | 23,690,000.00 USD |
| `4H` | `KuCoin` | `46.25%` | `53.75%` | `0.86` | 1,620,000.00 USD |
| `4H` | `Gate` | `49.48%` | `50.52%` | `0.98` | 4,620,000.00 USD |
| `4H` | `Bitget` | `56.23%` | `43.77%` | `1.28` | 10,400,000.00 USD |
| `4H` | `BingX` | `35.75%` | `64.25%` | `0.56` | 5,590,000.00 USD |
| `4H` | `MEXC` | `50.09%` | `49.91%` | `1.00` | 47,310,000.00 USD |
| `4H` | `Bitunix` | `40.29%` | `59.71%` | `0.67` | 7,720,000.00 USD |
| `4H` | `Hyperliquid` | `52.97%` | `47.03%` | `1.13` | 7,110,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.35%` | `51.65%` | `0.94` | 3,490,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `55.67%` | `44.33%` | `1.26` | 1,020,000.00 USD |
| `4H` | `HTX` | `45.55%` | `54.45%` | `0.84` | 128,530.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `63.78%` | `36.22%` | `1.76` | 2,540,000.00 USD |
| `4H` | `Aster` | `53.73%` | `46.27%` | `1.16` | 506,390.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `30.13%` | `69.87%` | `0.43` | 469,340.00 USD |
| `4H` | `Whale Positions` | `50.9%` | `49.1%` | `1.04` | 87,240,000.00 USD |
| `4H` | `Global Accounts` | `49.76%` | `50.24%` | `0.99` | 224,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.8554` | `0.8547` | `0.8554` | `0.8589` | `0.8518` | 3,213,767.92 USD | 1,386,293.70 USD | 1,827,474.23 USD | -441,180.53 USD | `-13.73%` | `5B / 12S` |
| `0:00 UTC` | `0.8503` | `0.8533` | `0.8503` | `0.8596` | `0.8482` | 2,970,160.51 USD | 1,607,321.44 USD | 1,362,839.07 USD | 244,482.37 USD | `+8.23%` | `19B / 6S` |
| `5:00 UTC` | `0.8605` | `0.8638` | `0.8605` | `0.8693` | `0.8592` | 3,068,721.14 USD | 1,724,308.92 USD | 1,344,412.22 USD | 379,896.70 USD | `+12.38%` | `24B / 7S` |
| `0:00 UTC` | `0.8697` | `0.8685` | `0.8697` | `0.8708` | `0.8651` | 2,460,446.55 USD | 1,349,113.11 USD | 1,111,333.44 USD | 237,779.67 USD | `+9.66%` | `7B / 9S` |
| `5:00 UTC` | `0.8680` | `0.8663` | `0.8680` | `0.8697` | `0.8640` | 1,274,072.68 USD | 628,587.96 USD | 645,484.72 USD | -16,896.75 USD | `-1.33%` | `6B / 9S` |
| `0:00 UTC` | `0.8698` | `0.8685` | `0.8698` | `0.8706` | `0.8657` | 2,093,919.35 USD | 1,157,864.07 USD | 936,055.29 USD | 221,808.78 USD | `+10.59%` | `11B / 2S` |
| `5:00 UTC` | `0.8700` | `0.8715` | `0.8700` | `0.8748` | `0.8669` | 2,353,506.52 USD | 1,517,666.93 USD | 835,839.59 USD | 681,827.34 USD | `+28.97%` | `29B / 5S` |
| `0:00 UTC` | `0.8800` | `0.8785` | `0.8800` | `0.8828` | `0.8730` | 3,913,129.55 USD | 2,396,328.40 USD | 1,516,801.15 USD | 879,527.25 USD | `+22.48%` | `20B / 6S` |
| `5:00 UTC` | `0.8851` | `0.8843` | `0.8851` | `0.8873` | `0.8813` | 3,303,378.86 USD | 1,747,933.70 USD | 1,555,445.16 USD | 192,488.53 USD | `+5.83%` | `6B / 8S` |
| `0:00 UTC` | `0.8790` | `0.8803` | `0.8790` | `0.8849` | `0.8778` | 3,548,538.23 USD | 1,629,121.26 USD | 1,919,416.97 USD | -290,295.70 USD | `-8.18%` | `12B / 13S` |

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
| `5m` | -295,990.00 USD | 396,090.00 USD | **`ACCUMULATION`** |
| `15m` | -192,880.00 USD | 393,910.00 USD | **`ACCUMULATION`** |
| `30m` | -229,190.00 USD | 1,670,000.00 USD | **`ACCUMULATION`** |
| `1h` | 206,070.00 USD | 3,150,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,800,000.00 USD | 4,770,000.00 USD | **`ACCUMULATION`** |
| `4h` | -5,310,000.00 USD | -6,120,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -6,220,000.00 USD | -9,220,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -13,630,000.00 USD | -18,550,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -14,110,000.00 USD | -26,600,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,790,000.00 USD | -25,240,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -28,190,000.00 USD | -86,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -157,430,000.00 USD | -484,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-295.99K` | 15m=`-192.88K` | 1h=`+206.07K` | 24h=`-9.79M`
* Futures Capital Netflows: 5m=`+396.09K` | 15m=`+393.91K` | 1h=`+3.15M` | 24h=`-25.24M`
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
  * `2026-10-30 09:09:49 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:41:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:43:49 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
