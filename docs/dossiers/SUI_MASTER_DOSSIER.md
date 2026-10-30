# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:44:30 IST` (`2026-10-30 06:14:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8904` | `0.8910` | `0.8872` | `0.8890` | `1,625,476` | 1,445,142.30 USD | -283,437.84 USD | `-19.61%` | -14,095,595.93 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.8891` | `0.8916` | `0.8884` | `0.8915` | `1,106,545` | 985,152.57 USD | 31,546.14 USD | `+3.20%` | -14,064,049.80 USD | `+0.99` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.8915` | `0.8943` | `0.8911` | `0.8942` | `992,851` | 885,985.52 USD | 155,980.21 USD | `+17.61%` | -13,908,069.58 USD | `+1.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9007` | `0.9020` | `0.8972` | `0.8989` | `2,708,403` | 2,436,057.12 USD | -463,648.94 USD | `-19.03%` | -12,861,622.64 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8988` | `0.8992` | `0.8901` | `0.8903` | `2,598,346` | 2,324,299.92 USD | -950,535.45 USD | `-40.90%` | -13,812,158.09 USD | `-2.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8904` | `0.8943` | `0.8872` | `0.8942` | `3,724,872` | 3,316,280.39 USD | -95,911.49 USD | `-2.89%` | -13,908,069.58 USD | `-0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8841` | `0.8966` | `0.8777` | `0.8946` | `15,840,652` | 14,060,418.53 USD | -340,237.43 USD | `-2.42%` | -12,409,833.65 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8945` | `0.9049` | `0.8901` | `0.8903` | `16,000,354` | 14,388,014.90 USD | -1,985,403.03 USD | `-13.80%` | -14,395,236.68 USD | `-0.61` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8904` | `0.8943` | `0.8872` | `0.8942` | `3,724,118` | 3,315,606.52 USD | -95,237.62 USD | `-2.87%` | -14,490,474.30 USD | `+0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8942` | `35,565,124` | 31,764,039.95 USD | -2,420,878.08 USD | `-7.62%` | -14,743,216.04 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | 1,889,481.85 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -683,829.84 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,386,264.68 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,322,337.96 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8942` | `35,565,124` | 31,764,039.95 USD | -2,420,878.08 USD | `-7.62%` | -14,743,216.04 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `0.8936` | `1636.1000` | 1,462.07 USD | 41,587.17 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8937` | `728.4000` | 651.00 USD | 14,590.47 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8937` | `1636.1000` | 1,462.22 USD | 16,052.69 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8937` | `5594.6000` | 4,999.95 USD | 21,052.64 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8937` | `6392.2000` | 5,712.71 USD | 26,765.34 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8937` | `4475.7000` | 3,999.84 USD | 30,765.19 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8937` | `8837.5000` | 7,897.81 USD | 38,663.00 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.8937` | `1636.1000` | 1,462.10 USD | 40,125.10 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8938` | `132.0000` | 117.99 USD | 12,284.17 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8938` | `132.0000` | 117.99 USD | 12,402.15 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8938` | `1720.0000` | 1,537.32 USD | 13,939.47 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8939` | `443.0000` | 396.01 USD | 4,466.32 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `0.8939` | `1455.4000` | 1,301.01 USD | 5,767.33 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `0.8939` | `1768.1000` | 1,580.50 USD | 7,347.83 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.8939` | `1768.1000` | 1,580.45 USD | 8,928.28 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8939` | `1252.9000` | 1,119.92 USD | 10,048.20 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8939` | `2369.5000` | 2,117.98 USD | 12,166.18 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8940` | `2499.7000` | 2,234.83 USD | 3,605.44 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8940` | `520.0000` | 464.86 USD | 4,070.31 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `0.8941` | `1120.6000` | 1,001.95 USD | 1,001.95 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.8941` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.89` | `0.00%` | `-` |
| `BID` | `0.8941` | `1533.0000` | 1,370.61 USD | 1,370.61 USD | `2 orders` | `-0.00%` | `-` |
| `ASK` | `0.8942` | `400.0000` | 357.70 USD | 3,363.62 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8942` | `2241.1000` | 2,003.97 USD | 3,005.92 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8943` | `5602.2000` | 5,009.94 USD | 8,373.55 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8944` | `2236.0000` | 1,999.97 USD | 12,038.17 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8944` | `1636.1000` | 1,463.33 USD | 10,038.21 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8944` | `225.1000` | 201.33 USD | 8,574.88 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8945` | `5600.0000` | 5,009.48 USD | 20,515.28 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8945` | `1514.4000` | 1,354.69 USD | 15,505.80 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8945` | `111.7000` | 99.92 USD | 14,151.11 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8945` | `614.4000` | 549.57 USD | 14,051.19 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8945` | `1636.1000` | 1,463.44 USD | 13,501.62 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8946` | `1227.0000` | 1,097.74 USD | 27,563.13 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8946` | `1857.2000` | 1,661.47 USD | 26,465.40 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.8946` | `3157.9000` | 2,825.06 USD | 24,803.93 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.8946` | `1636.1000` | 1,463.59 USD | 21,978.87 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8947` | `2000.0000` | 1,789.38 USD | 49,557.12 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.8947` | `11371.2000` | 10,173.59 USD | 47,767.74 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `0.8947` | `12.5000` | 11.18 USD | 37,594.15 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8947` | `11199.6000` | 10,019.83 USD | 37,582.97 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `663` | `0xb83d...6e36` | `SHORT` | 3,392,900.35 USD | `3,817,609.40` | `1.11` | `0.8891` | `34.25` | 825,834.96 USD | `+24.34%` | `3X Cross` |
| `994` | `0xa2ce...3126` | `LONG` | 2,221,009.24 USD | `2,500,010.40` | `0.8597` | `0.8891` | `0.000000` | 71,802.71 USD | `+3.23%` | `10X Cross` |
| `1551` | `0x9946...0852` | `SHORT` | 1,382,943.96 USD | `1,557,106.30` | `1.07` | `0.8891` | `1.86` | 275,733.84 USD | `+19.94%` | `10X Cross` |
| `1887` | `0x9df2...c665` | `SHORT` | 1,066,500.00 USD | `1,200,000.00` | `0.7465` | `0.8891` | `26.02` | -170,647.60 USD | `-16.00%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9048` | 5,070.15 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.07K USD at 0.9048 USD [API] | `2026-10-29 03:18:13` |
| `ANNOUNCEMENT` | `INFO` | `0.9038` | 5,341.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9038 USD [API] | `2026-10-29 04:14:26` |
| `ANNOUNCEMENT` | `INFO` | `0.9014` | 853.20 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.85K USD at 0.9014 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `0.9013` | 1,980.18 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.98K USD at 0.9013 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `0.9014` | 1,001.32 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.00K USD at 0.9014 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `0.9024` | 1,001.35 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.00K USD at 0.9024 USD [API] | `2026-10-29 07:17:06` |
| `ANNOUNCEMENT` | `INFO` | `0.9072` | 9,788.55 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 9.79K USD at 0.9072 USD [API] | `2026-10-29 07:47:48` |
| `ANNOUNCEMENT` | `INFO` | `0.9072` | 9,788.55 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 9.79K USD at 0.9072 USD [API] | `2026-10-29 07:47:48` |
| `ANNOUNCEMENT` | `INFO` | `0.9014` | 3,561.16 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 3.56K USD at 0.9014 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `0.9025` | 3,556.60 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 3.56K USD at 0.9025 USD [API] | `2026-10-29 07:17:06` |
| `ANNOUNCEMENT` | `INFO` | `0.9070` | 5,006.08 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9070 USD [API] | `2026-10-29 08:09:57` |


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
| `Live` | `Long Liquidation` | `0.1955` | 1,820.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2125` | 212.50 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2155` | 1,450.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 2,490.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 313.73 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 3,250.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 849.48 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 24,160.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 154.64 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 3,450.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 1,430.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,190.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 593.12 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3145` | 104.07 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3205` | 3,210.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3215` | 9,160.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3325` | 602.79 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3415` | 4,270.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 5,070.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3495` | 27,160.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3635` | 405.34 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3655` | 406.18 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 6,730.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3815` | 267.05 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 9,010.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 31,820.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4165` | 733.87 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4245` | 468.61 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4375` | 514.24 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 429.86 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 373.46 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 44,080.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 219.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 105.25 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 1,020.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 3,330.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4725` | 1,720.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 1,570.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4795` | 504.48 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 166.70 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 3,540.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 536.96 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 4,640.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 5,630.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 5,680.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 102.76 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 854.17 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 106.04 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5215` | 123.54 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5265` | 7,140.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 162.83 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 123,640.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5305` | 130.08 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 278.29 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 113.47 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 7,850.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 1,480.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 126.46 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 6,150.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 334.82 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5565` | 556.50 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5615` | 442.63 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 1,300.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 7,200.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 109,930.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 217.37 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,490.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 6,470.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 225.93 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 608.61 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5975` | 3,420.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 14,140.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 4,760.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 323.79 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6035` | 1,220.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 886.10 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6095` | 214.54 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,280.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 438.73 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 112.33 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 4,880.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,980.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 12,570.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 2,400.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 708.53 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6235` | 187.05 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 1,100.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 843.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 7,600.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6385` | 34,150.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 33,040.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 4,980.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,190.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 2,370.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 3,200.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 668.34 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 91,460.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 1,300.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6525` | 2,350.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 2,840.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 6,700.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 1,830.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 7,070.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 325.46 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 4,840.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 528.73 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 2,260.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 5,470.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 337.36 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 29,210.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 2,240.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,620.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 835.14 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 868.02 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 933.37 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 9,150.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 122.94 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 43,650.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 2,110.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 17,190.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 15,130.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,960.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 6,110.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 3,170.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6925` | 282.54 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 3,600.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 722.28 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,700.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,030.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 4,830.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 235.37 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 8,970.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 143.14 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 3,620.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,020.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 8,760.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 25,350.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 283.22 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 927.55 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 428,700.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 11,030.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 4,620.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7185` | 126.96 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 420.19 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 8,450.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,920.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 127.05 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7245` | 2,520.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 311.60 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 3,410.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 35,890.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 424.86 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 13,500.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 8,260.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 6,240.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7360` | 10,380,000.00 USD | 10,380,000.00 USD | 79,750.00 USD | 28,310.00 USD | 71,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7375` | 7,100.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7380` | 10,200,000.00 USD | 10,200,000.00 USD | 23,980.00 USD | 22,880.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,020.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7400` | 10,140,000.00 USD | 10,140,000.00 USD | 17,280.00 USD | 13,180.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7420` | 10,090,000.00 USD | 10,090,000.00 USD | 31,920.00 USD | 8,580.00 USD | 38,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7425` | 2,430.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 783,980.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7440` | 10,010,000.00 USD | 10,010,000.00 USD | 65,280.00 USD | 21,190.00 USD | 40,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7455` | 4,020.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7460` | 9,880,000.00 USD | 9,880,000.00 USD | 22,100.00 USD | 24,720.00 USD | 42,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7465` | 359.96 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7480` | 9,790,000.00 USD | 9,790,000.00 USD | 11,220.00 USD | 6,300.00 USD | 738.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7495` | 4,820.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7500` | 9,770,000.00 USD | 9,770,000.00 USD | 25,600.00 USD | 12,880.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7520` | 9,720,000.00 USD | 9,720,000.00 USD | 2,130.00 USD | 10,160.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7535` | 569.50 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7540` | 9,690,000.00 USD | 9,690,000.00 USD | 9,690.00 USD | 4,770.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7545` | 1,250.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 1,750.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7560` | 9,660,000.00 USD | 9,660,000.00 USD | 2,690.00 USD | 17,670.00 USD | 7,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7580` | 9,630,000.00 USD | 9,630,000.00 USD | 19,590.00 USD | 20,390.00 USD | 358.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,900.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7600` | 9,590,000.00 USD | 9,590,000.00 USD | 8,420.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7605` | 2,920.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7620` | 9,580,000.00 USD | 9,580,000.00 USD | 40,420.00 USD | 16,580.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7625` | 859.11 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 439.47 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7640` | 9,520,000.00 USD | 9,520,000.00 USD | 556.58 USD | 118.70 USD | 97.65 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,060.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7660` | 9,520,000.00 USD | 9,520,000.00 USD | 1,280.00 USD | 23,260.00 USD | 32,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,260.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7675` | 25,580.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7680` | 9,460,000.00 USD | 9,460,000.00 USD | 182.28 USD | 3,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7685` | 207.19 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7695` | 468,690.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7700` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 876,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 871,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7720` | 9,460,000.00 USD | 9,460,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,940.00 USD | 852,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 5,230.00 USD | 850,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 3,430.00 USD | 844,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 3,510.00 USD | 841,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 837,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 809,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 2,640.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 809,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7820` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 1,440.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 24,380.00 USD | 805,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7840` | 9,430,000.00 USD | 9,430,000.00 USD | 6,050.00 USD | 2,680.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7860` | 9,420,000.00 USD | 9,420,000.00 USD | 1,740.00 USD | 45,550.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 781,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 777,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7900` | 7,320,000.00 USD | 7,320,000.00 USD | 37,240.00 USD | 29,720.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7900` | 9,360,000.00 USD | 9,360,000.00 USD | 6,610.00 USD | 28,080.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 777,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7915` | 11,400.00 USD | 773,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 7,240,000.00 USD | 7,240,000.00 USD | 10,370.00 USD | 16,170.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7920` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 23,790.00 USD | 67,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 10,810.00 USD | 762,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 751,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7940` | 7,170,000.00 USD | 7,170,000.00 USD | 21,090.00 USD | 20,690.00 USD | 21,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 886.60 USD | 4,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 736.66 USD | 750,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7955` | 52,610.00 USD | 749,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 7,110,000.00 USD | 7,110,000.00 USD | 4,910.00 USD | 6,390.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 9,220,000.00 USD | 9,220,000.00 USD | 2,210.00 USD | 19,210.00 USD | 82,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 12,980.00 USD | 697,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,460.00 USD | 684,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 7,060,000.00 USD | 7,060,000.00 USD | 25,120.00 USD | 11,770.00 USD | 37,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 9,120,000.00 USD | 9,120,000.00 USD | 35,260.00 USD | 3,570.00 USD | 66,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 40,230.00 USD | 676,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7995` | 7,590.00 USD | 636,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 6,980,000.00 USD | 6,980,000.00 USD | 32,430.00 USD | 31,530.00 USD | 35,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 9,010,000.00 USD | 9,010,000.00 USD | 41,450.00 USD | 16,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 3,740.00 USD | 629,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8015` | 7,500.00 USD | 625,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8020` | 6,880,000.00 USD | 6,880,000.00 USD | 1,730.00 USD | 251.75 USD | 724.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 8,950,000.00 USD | 8,950,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 3,830.00 USD | 617,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,680.00 USD | 613,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8040` | 6,880,000.00 USD | 6,880,000.00 USD | 37,430.00 USD | 24,190.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8045` | 16,660.00 USD | 606,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 361.11 USD | 589,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 6,800,000.00 USD | 6,800,000.00 USD | 50,970.00 USD | 15,300.00 USD | 69,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 8,880,000.00 USD | 8,880,000.00 USD | 10,860.00 USD | 737.70 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 589,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 582,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8080` | 6,660,000.00 USD | 6,660,000.00 USD | 3,230.00 USD | 19,130.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 8,870,000.00 USD | 8,870,000.00 USD | 5,030.00 USD | 11,280.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,620.00 USD | 579,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8095` | 130,110.00 USD | 556,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 6,640,000.00 USD | 6,640,000.00 USD | 2,420.00 USD | 11,070.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 8,850,000.00 USD | 8,850,000.00 USD | 4,310.00 USD | 9,850.00 USD | 104.33 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 426,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,970.00 USD | 424,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 6,620,000.00 USD | 6,620,000.00 USD | 15,380.00 USD | 3,270.00 USD | 23,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 8,830,000.00 USD | 8,830,000.00 USD | 73,000.00 USD | 9,210.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 1,160.00 USD | 421,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 420,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 6,580,000.00 USD | 6,580,000.00 USD | 29,630.00 USD | 9,710.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8140` | 8,710,000.00 USD | 8,710,000.00 USD | 55,190.00 USD | 31,920.00 USD | 78,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 416,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8155` | 38,250.00 USD | 416,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 6,520,000.00 USD | 6,520,000.00 USD | 116,280.00 USD | 24,170.00 USD | 172,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 8,550,000.00 USD | 8,550,000.00 USD | 186,980.00 USD | 49,790.00 USD | 146,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 104.92 USD | 378,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8175` | 77,840.00 USD | 378,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 6,200,000.00 USD | 6,200,000.00 USD | 66,880.00 USD | 10,440.00 USD | 36,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 8,160,000.00 USD | 8,160,000.00 USD | 82,600.00 USD | 41,370.00 USD | 42,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 24,620.00 USD | 300,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,230.00 USD | 275,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 6,090,000.00 USD | 6,090,000.00 USD | 112,400.00 USD | 8,800.00 USD | 83,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 8,000,000.00 USD | 8,000,000.00 USD | 205,920.00 USD | 48,700.00 USD | 103,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 5,360.00 USD | 274,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8215` | 474.01 USD | 268,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 5,880,000.00 USD | 5,880,000.00 USD | 86,610.00 USD | 89,600.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8220` | 7,640,000.00 USD | 7,640,000.00 USD | 110,800.00 USD | 73,170.00 USD | 169,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 2,890.00 USD | 268,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8235` | 463.63 USD | 265,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 5,620,000.00 USD | 5,620,000.00 USD | 10,570.00 USD | 5,990.00 USD | 143,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8240` | 7,290,000.00 USD | 7,290,000.00 USD | 102,030.00 USD | 42,270.00 USD | 90,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 18,980.00 USD | 265,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8255` | 1,580.00 USD | 246,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 5,460,000.00 USD | 5,460,000.00 USD | 43,870.00 USD | 11,180.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 7,050,000.00 USD | 7,050,000.00 USD | 194,340.00 USD | 32,880.00 USD | 111,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 244,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 5,380,000.00 USD | 5,380,000.00 USD | 41,020.00 USD | 22,610.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 6,710,000.00 USD | 6,710,000.00 USD | 118,780.00 USD | 44,400.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 239,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8295` | 46,590.00 USD | 119,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8300` | 5,310,000.00 USD | 5,310,000.00 USD | 27,690.00 USD | 14,510.00 USD | 53,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 6,460,000.00 USD | 6,460,000.00 USD | 33,770.00 USD | 45,100.00 USD | 44,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 5,210,000.00 USD | 5,210,000.00 USD | 3,000.00 USD | 37,880.00 USD | 46,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 6,340,000.00 USD | 6,340,000.00 USD | 90,830.00 USD | 77,110.00 USD | 150,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 5,130,000.00 USD | 5,130,000.00 USD | 149,940.00 USD | 40,900.00 USD | 105,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 6,020,000.00 USD | 6,020,000.00 USD | 114,580.00 USD | 56,360.00 USD | 180,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8345` | 5,750.00 USD | 73,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 4,830,000.00 USD | 4,830,000.00 USD | 58,860.00 USD | 13,740.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 5,670,000.00 USD | 5,670,000.00 USD | 175,960.00 USD | 28,000.00 USD | 92,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 327.21 USD | 67,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 4,760,000.00 USD | 4,760,000.00 USD | 51,030.00 USD | 66,750.00 USD | 144,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 5,370,000.00 USD | 5,370,000.00 USD | 65,710.00 USD | 219,730.00 USD | 223,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 7,300.00 USD | 67,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 4,500,000.00 USD | 4,500,000.00 USD | 38,430.00 USD | 9,770.00 USD | 55,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 4,860,000.00 USD | 4,860,000.00 USD | 82,000.00 USD | 54,600.00 USD | 58,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 862.10 USD | 59,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8415` | 134.47 USD | 59,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 4,390,000.00 USD | 4,390,000.00 USD | 89,320.00 USD | 63,630.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 4,670,000.00 USD | 4,670,000.00 USD | 96,530.00 USD | 66,440.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 11,390.00 USD | 58,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 4,180,000.00 USD | 4,180,000.00 USD | 67,620.00 USD | 63,050.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 4,490,000.00 USD | 4,490,000.00 USD | 28,900.00 USD | 111,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 745.82 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 4,030,000.00 USD | 4,030,000.00 USD | 22,250.00 USD | 93,240.00 USD | 38,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 4,350,000.00 USD | 4,350,000.00 USD | 52,800.00 USD | 57,770.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 317.98 USD | 46,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 3,880,000.00 USD | 3,880,000.00 USD | 51,620.00 USD | 62,920.00 USD | 70,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 4,240,000.00 USD | 4,240,000.00 USD | 73,880.00 USD | 46,880.00 USD | 84,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 202.28 USD | 46,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 3,690,000.00 USD | 3,690,000.00 USD | 72,370.00 USD | 88,390.00 USD | 167,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 4,030,000.00 USD | 4,030,000.00 USD | 82,620.00 USD | 58,490.00 USD | 53,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 3,360,000.00 USD | 3,360,000.00 USD | 89,760.00 USD | 198,220.00 USD | 133,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 3,840,000.00 USD | 3,840,000.00 USD | 77,320.00 USD | 53,520.00 USD | 52,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 42,610.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 2,940,000.00 USD | 2,940,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 3,660,000.00 USD | 3,660,000.00 USD | 277,690.00 USD | 36,220.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8545` | 3,630.00 USD | 3,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,740,000.00 USD | 2,740,000.00 USD | 1,920.00 USD | 24,460.00 USD | 46,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 3,340,000.00 USD | 3,340,000.00 USD | 87,380.00 USD | 55,310.00 USD | 36,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,670,000.00 USD | 2,670,000.00 USD | 32,900.00 USD | 66,810.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 3,160,000.00 USD | 3,160,000.00 USD | 146,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,550,000.00 USD | 2,550,000.00 USD | 89,450.00 USD | 30,490.00 USD | 23,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 3,010,000.00 USD | 3,010,000.00 USD | 38,890.00 USD | 164,470.00 USD | 20,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,400,000.00 USD | 2,400,000.00 USD | 46,800.00 USD | 25,800.00 USD | 26,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 2,790,000.00 USD | 2,790,000.00 USD | 25,100.00 USD | 145,110.00 USD | 393,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,300,000.00 USD | 2,300,000.00 USD | 77,240.00 USD | 149,990.00 USD | 107,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 2,230,000.00 USD | 2,230,000.00 USD | 83,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,970,000.00 USD | 1,970,000.00 USD | 133,260.00 USD | 27,450.00 USD | 167,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 2,140,000.00 USD | 2,140,000.00 USD | 294,020.00 USD | 93,770.00 USD | 678,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,640,000.00 USD | 1,640,000.00 USD | 106,760.00 USD | 11,860.00 USD | 125,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 1,080,000.00 USD | 1,080,000.00 USD | 213,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 90,040.00 USD | 50,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 863,580.00 USD | 863,580.00 USD | 0.00 USD | 34,600.00 USD | 104,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,260,000.00 USD | 1,260,000.00 USD | 182,270.00 USD | 62,100.00 USD | 172,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 724,360.00 USD | 724,360.00 USD | 207,250.00 USD | 72,450.00 USD | 87,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 838,640.00 USD | 838,640.00 USD | 55,600.00 USD | 0.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 357,130.00 USD | 357,130.00 USD | 9,520.00 USD | 0.00 USD | 66,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 755,530.00 USD | 755,530.00 USD | 0.00 USD | 0.00 USD | 142,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 281,230.00 USD | 281,230.00 USD | 16,700.00 USD | 0.00 USD | 186,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 612,950.00 USD | 612,950.00 USD | 107,610.00 USD | 20,280.00 USD | 67,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 417,130.00 USD | 417,130.00 USD | 4,760.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 78,080.00 USD | 78,080.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 411,360.00 USD | 411,360.00 USD | 37,200.00 USD | 24,670.00 USD | 113,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 57,770.00 USD | 57,770.00 USD | 0.00 USD | 3,570.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 235,970.00 USD | 235,970.00 USD | 30,450.00 USD | 2,260.00 USD | 26,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 48,570.00 USD | 48,570.00 USD | 0.00 USD | 35,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 177,210.00 USD | 177,210.00 USD | 0.00 USD | 0.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 175,880.00 USD | 175,880.00 USD | 122,200.00 USD | 1,400.00 USD | 560.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 12,670.00 USD | 12,670.00 USD | 0.00 USD | 3,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 51,720.00 USD | 51,720.00 USD | 2,860.00 USD | 0.00 USD | 48,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 8,820.00 USD | 8,820.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 149,100.00 USD | 149,100.00 USD | 137,750.00 USD | 0.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8920` | 1,510,000.00 USD | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8940` | 390,250.00 USD | 390,250.00 USD | 200,000.00 USD | 40,390.00 USD | 754.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8940` | 2,780,000.00 USD | 2,780,000.00 USD | 1,270,000.00 USD | 0.00 USD | 6,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8960` | 496,860.00 USD | 496,860.00 USD | 2,890.00 USD | 101,620.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8960` | 3,510,000.00 USD | 3,510,000.00 USD | 610,810.00 USD | 107,280.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8965` | 852.66 USD | 852.66 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8980` | 917,790.00 USD | 917,790.00 USD | 74,000.00 USD | 95,760.00 USD | 251,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8980` | 4,590,000.00 USD | 4,590,000.00 USD | 626,180.00 USD | 118,950.00 USD | 339,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9000` | 1,280,000.00 USD | 1,280,000.00 USD | 237,980.00 USD | 121,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9000` | 4,810,000.00 USD | 4,810,000.00 USD | 198,040.00 USD | 16,730.00 USD | 514.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 1,420,000.00 USD | 1,420,000.00 USD | 7,290.00 USD | 138,990.00 USD | 189.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9020` | 5,560,000.00 USD | 5,560,000.00 USD | 85,610.00 USD | 192,140.00 USD | 477,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9040` | 1,810,000.00 USD | 1,810,000.00 USD | 157,060.00 USD | 223,010.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9040` | 6,010,000.00 USD | 6,010,000.00 USD | 223,750.00 USD | 2,890.00 USD | 223,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9060` | 2,440,000.00 USD | 2,440,000.00 USD | 258,520.00 USD | 176,840.00 USD | 202,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9060` | 6,440,000.00 USD | 6,440,000.00 USD | 286,790.00 USD | 34,600.00 USD | 104,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9080` | 2,970,000.00 USD | 2,970,000.00 USD | 249,000.00 USD | 147,110.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9080` | 7,310,000.00 USD | 7,310,000.00 USD | 389,350.00 USD | 259,410.00 USD | 224,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 3,140,000.00 USD | 3,140,000.00 USD | 99,190.00 USD | 39,940.00 USD | 31,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9100` | 7,510,000.00 USD | 7,510,000.00 USD | 123,910.00 USD | 6,820.00 USD | 68,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 3,430,000.00 USD | 3,430,000.00 USD | 100,870.00 USD | 97,820.00 USD | 90,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9120` | 7,780,000.00 USD | 7,780,000.00 USD | 135,210.00 USD | 134,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 3,920,000.00 USD | 3,920,000.00 USD | 208,890.00 USD | 69,780.00 USD | 209,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9140` | 8,010,000.00 USD | 8,010,000.00 USD | 143,540.00 USD | 83,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 4,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9160` | 4,440,000.00 USD | 4,440,000.00 USD | 130,780.00 USD | 169,050.00 USD | 223,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9160` | 8,470,000.00 USD | 8,470,000.00 USD | 212,270.00 USD | 84,510.00 USD | 170,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 4,720,000.00 USD | 4,720,000.00 USD | 90,690.00 USD | 76,080.00 USD | 110,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9180` | 8,750,000.00 USD | 8,750,000.00 USD | 38,590.00 USD | 48,930.00 USD | 187,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9195` | 9,200.00 USD | 14,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 4,990,000.00 USD | 4,990,000.00 USD | 104,190.00 USD | 22,510.00 USD | 141,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9200` | 9,340,000.00 USD | 9,340,000.00 USD | 445,890.00 USD | 32,570.00 USD | 114,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 5,550,000.00 USD | 5,550,000.00 USD | 203,870.00 USD | 94,010.00 USD | 261,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9220` | 9,740,000.00 USD | 9,740,000.00 USD | 6,470.00 USD | 66,370.00 USD | 320,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9235` | 209.36 USD | 14,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9240` | 6,170,000.00 USD | 6,170,000.00 USD | 240,420.00 USD | 110,560.00 USD | 265,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9240` | 10,170,000.00 USD | 10,170,000.00 USD | 111,800.00 USD | 62,860.00 USD | 260,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 6,520,000.00 USD | 6,520,000.00 USD | 135,010.00 USD | 117,320.00 USD | 106,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9260` | 10,550,000.00 USD | 10,550,000.00 USD | 209,940.00 USD | 81,200.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 6,670,000.00 USD | 6,670,000.00 USD | 5,090.00 USD | 67,540.00 USD | 74,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9280` | 10,710,000.00 USD | 10,710,000.00 USD | 114,570.00 USD | 5,660.00 USD | 33,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 6,880,000.00 USD | 6,880,000.00 USD | 43,730.00 USD | 61,500.00 USD | 106,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9300` | 11,160,000.00 USD | 11,160,000.00 USD | 186,110.00 USD | 98,550.00 USD | 169,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 7,170,000.00 USD | 7,170,000.00 USD | 189,960.00 USD | 36,420.00 USD | 59,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9320` | 11,280,000.00 USD | 11,280,000.00 USD | 4,410.00 USD | 53,880.00 USD | 63,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 7,210,000.00 USD | 7,210,000.00 USD | 5,250.00 USD | 35,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9340` | 11,410,000.00 USD | 11,410,000.00 USD | 50,160.00 USD | 78,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 7,360,000.00 USD | 7,360,000.00 USD | 48,720.00 USD | 29,540.00 USD | 67,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9360` | 11,550,000.00 USD | 11,550,000.00 USD | 131,450.00 USD | 3,160.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 7,780,000.00 USD | 7,780,000.00 USD | 118,620.00 USD | 63,250.00 USD | 245,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9380` | 11,910,000.00 USD | 11,910,000.00 USD | 168,030.00 USD | 5,150.00 USD | 183,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 39,850.00 USD | 54,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9400` | 7,940,000.00 USD | 7,940,000.00 USD | 59,870.00 USD | 3,680.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 12,240,000.00 USD | 12,240,000.00 USD | 170,760.00 USD | 37,790.00 USD | 127,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 7,990,000.00 USD | 7,990,000.00 USD | 17,290.00 USD | 14,410.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 12,310,000.00 USD | 12,310,000.00 USD | 4,970.00 USD | 29,990.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9425` | 2,050.00 USD | 56,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9440` | 8,100,000.00 USD | 8,100,000.00 USD | 6,330.00 USD | 38,560.00 USD | 58,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 12,530,000.00 USD | 12,530,000.00 USD | 3,360.00 USD | 217,840.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9445` | 103.90 USD | 56,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9460` | 8,340,000.00 USD | 8,340,000.00 USD | 61,800.00 USD | 32,120.00 USD | 152,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 69,070.00 USD | 128,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 8,560,000.00 USD | 8,560,000.00 USD | 91,790.00 USD | 73,040.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 78,160.00 USD | 291,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 8,700,000.00 USD | 8,700,000.00 USD | 26,310.00 USD | 36,450.00 USD | 70,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 13,510,000.00 USD | 13,510,000.00 USD | 2,840.00 USD | 30,430.00 USD | 371,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 8,990,000.00 USD | 8,990,000.00 USD | 52,590.00 USD | 28,420.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 87,720.00 USD | 360,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 9,200,000.00 USD | 9,200,000.00 USD | 59,860.00 USD | 51,440.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 14,030,000.00 USD | 14,030,000.00 USD | 13,570.00 USD | 3,670.00 USD | 61,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 9,320,000.00 USD | 9,320,000.00 USD | 40,290.00 USD | 27,000.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 14,110,000.00 USD | 14,110,000.00 USD | 72,330.00 USD | 3,500.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 9,400,000.00 USD | 9,400,000.00 USD | 27,440.00 USD | 45,440.00 USD | 12,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 14,960,000.00 USD | 14,960,000.00 USD | 846,080.00 USD | 1,220.00 USD | 896.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 9,630,000.00 USD | 9,630,000.00 USD | 103,500.00 USD | 50,930.00 USD | 78,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 15,570,000.00 USD | 15,570,000.00 USD | 358,610.00 USD | 118,450.00 USD | 132,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 10,140,000.00 USD | 10,140,000.00 USD | 267,480.00 USD | 66,570.00 USD | 176,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 17,110,000.00 USD | 17,110,000.00 USD | 715,790.00 USD | 231,300.00 USD | 594,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 10,550,000.00 USD | 10,550,000.00 USD | 238,280.00 USD | 68,410.00 USD | 102,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 18,680,000.00 USD | 18,680,000.00 USD | 693,720.00 USD | 366,520.00 USD | 508,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 10,910,000.00 USD | 10,910,000.00 USD | 155,090.00 USD | 129,450.00 USD | 72,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 20,410,000.00 USD | 20,410,000.00 USD | 962,420.00 USD | 245,250.00 USD | 520,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 11,460,000.00 USD | 11,460,000.00 USD | 175,350.00 USD | 67,790.00 USD | 303,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 22,480,000.00 USD | 22,480,000.00 USD | 856,440.00 USD | 625,850.00 USD | 592,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 12,030,000.00 USD | 12,030,000.00 USD | 274,850.00 USD | 111,340.00 USD | 186,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 23,790,000.00 USD | 23,790,000.00 USD | 694,250.00 USD | 345,780.00 USD | 263,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 12,310,000.00 USD | 12,310,000.00 USD | 99,840.00 USD | 64,240.00 USD | 117,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 24,610,000.00 USD | 24,610,000.00 USD | 400,520.00 USD | 196,560.00 USD | 225,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 12,400,000.00 USD | 12,400,000.00 USD | 36,690.00 USD | 2,780.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 25,180,000.00 USD | 25,180,000.00 USD | 334,930.00 USD | 116,990.00 USD | 116,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 12,530,000.00 USD | 12,530,000.00 USD | 20,700.00 USD | 28,970.00 USD | 84,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 25,910,000.00 USD | 25,910,000.00 USD | 182,900.00 USD | 286,070.00 USD | 264,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 12,710,000.00 USD | 12,710,000.00 USD | 32,890.00 USD | 42,000.00 USD | 102,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 27,050,000.00 USD | 27,050,000.00 USD | 410,980.00 USD | 211,120.00 USD | 517,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 12,910,000.00 USD | 12,910,000.00 USD | 61,120.00 USD | 37,860.00 USD | 108,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 27,590,000.00 USD | 27,590,000.00 USD | 247,060.00 USD | 52,490.00 USD | 238,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 57,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9820` | 13,000,000.00 USD | 13,000,000.00 USD | 76,660.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 27,910,000.00 USD | 27,910,000.00 USD | 108,220.00 USD | 68,030.00 USD | 148,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 13,080,000.00 USD | 13,080,000.00 USD | 33,500.00 USD | 44,230.00 USD | 5,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 28,610,000.00 USD | 28,610,000.00 USD | 397,850.00 USD | 123,740.00 USD | 176,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 13,280,000.00 USD | 13,280,000.00 USD | 70,580.00 USD | 40,960.00 USD | 90,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 28,950,000.00 USD | 28,950,000.00 USD | 107,440.00 USD | 154,250.00 USD | 71,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 57,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 13,420,000.00 USD | 13,420,000.00 USD | 75,940.00 USD | 22,710.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 29,260,000.00 USD | 29,260,000.00 USD | 209,770.00 USD | 75,650.00 USD | 30,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 61,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9900` | 13,550,000.00 USD | 13,550,000.00 USD | 74,860.00 USD | 32,660.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 29,570,000.00 USD | 29,570,000.00 USD | 201,410.00 USD | 100,430.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9915` | 1,570.00 USD | 63,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9920` | 13,610,000.00 USD | 13,610,000.00 USD | 21,690.00 USD | 17,780.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 30,020,000.00 USD | 30,020,000.00 USD | 288,210.00 USD | 79,650.00 USD | 81,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 63,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9940` | 13,740,000.00 USD | 13,740,000.00 USD | 43,770.00 USD | 20,800.00 USD | 70,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 30,490,000.00 USD | 30,490,000.00 USD | 143,340.00 USD | 183,310.00 USD | 145,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 13,770,000.00 USD | 13,770,000.00 USD | 6,270.00 USD | 3,140.00 USD | 20,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 30,940,000.00 USD | 30,940,000.00 USD | 107,780.00 USD | 55,790.00 USD | 287,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 14,030,000.00 USD | 14,030,000.00 USD | 92,080.00 USD | 17,560.00 USD | 148,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 31,390,000.00 USD | 31,390,000.00 USD | 238,490.00 USD | 42,080.00 USD | 165,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,610,000.00 USD | 31,610,000.00 USD | 94,210.00 USD | 53,610.00 USD | 69,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 64,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,160,000.00 USD | 32,160,000.00 USD | 250,490.00 USD | 51,850.00 USD | 254,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,530,000.00 USD | 32,530,000.00 USD | 155,110.00 USD | 54,750.00 USD | 157,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 32,670,000.00 USD | 32,670,000.00 USD | 76,570.00 USD | 24,230.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 33,070,000.00 USD | 33,070,000.00 USD | 219,210.00 USD | 23,470.00 USD | 164,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 33,610,000.00 USD | 33,610,000.00 USD | 311,680.00 USD | 74,250.00 USD | 151,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,000,000.00 USD | 34,000,000.00 USD | 196,720.00 USD | 102,780.00 USD | 87,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,350,000.00 USD | 34,350,000.00 USD | 91,940.00 USD | 116,240.00 USD | 141,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 705.99 USD | 64,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 64,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 35,040,000.00 USD | 35,040,000.00 USD | 306,830.00 USD | 87,000.00 USD | 295,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 35,290,000.00 USD | 35,290,000.00 USD | 89,190.00 USD | 9,800.00 USD | 151,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 35,640,000.00 USD | 35,640,000.00 USD | 104,970.00 USD | 47,120.00 USD | 202,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 35,930,000.00 USD | 35,930,000.00 USD | 163,000.00 USD | 30,810.00 USD | 94,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 36,080,000.00 USD | 36,080,000.00 USD | 65,710.00 USD | 37,380.00 USD | 49,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 11,040.00 USD | 75,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 103.85 USD | 76,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 76,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,840.00 USD | 79,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.06` | 1,740.00 USD | 81,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 84,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 90,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 90,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 90,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 8,940.00 USD | 99,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 123,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 123,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 639.88 USD | 124,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 129.88 USD | 124,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 177.65 USD | 124,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 129,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 383.01 USD | 129,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 129,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 3,930.00 USD | 133,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 136,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 138,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 9,740.00 USD | 148,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 188,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 188,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 188,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 189,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 221,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 1,090.00 USD | 222,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 228,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 250,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 257,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.35` | 132.52 USD | 257,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 616,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 620,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 620,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 621,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.46` | 21,110.00 USD | 642,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 16,420.00 USD | 658,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 149.75 USD | 658,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 662,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 9,930.00 USD | 672,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 673,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 673,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,180.00 USD | 674,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 123.81 USD | 674,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,130.00 USD | 675,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 282,600.00 USD | 958,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 979,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 3,940.00 USD | 983,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 3,620.00 USD | 987,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,090.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 2,260.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 141.16 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 150.02 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 9,650.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 900.48 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 494.34 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 85,830.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 20,050.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 7,100.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1955` | 4,720,000.00 USD | 0.00 USD | 1,820.00 USD | `-78.08%` | `9,320.00` |
| `Live` | `Long` | `0.1995` | 4,720,000.00 USD | 0.00 USD | 256.00 USD | `-77.63%` | `1,283.20` |
| `Live` | `Long` | `0.2125` | 4,720,000.00 USD | 0.00 USD | 212.50 USD | `-76.17%` | `1,000.00` |
| `Live` | `Long` | `0.2135` | 4,720,000.00 USD | 0.00 USD | 4,040.00 USD | `-76.06%` | `18,919.90` |
| `Live` | `Long` | `0.2155` | 4,710,000.00 USD | 0.00 USD | 1,450.00 USD | `-75.83%` | `6,725.00` |
| `Live` | `Long` | `0.2355` | 4,710,000.00 USD | 0.00 USD | 789.66 USD | `-73.59%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,710,000.00 USD | 0.00 USD | 156.36 USD | `-73.25%` | `655.60` |
| `Live` | `Long` | `0.2455` | 4,710,000.00 USD | 0.00 USD | 2,490.00 USD | `-72.47%` | `10,152.10` |
| `Live` | `Long` | `0.2475` | 4,710,000.00 USD | 0.00 USD | 313.73 USD | `-72.24%` | `1,267.60` |
| `Live` | `Long` | `0.2525` | 4,710,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.68%` | `8,897.00` |
| `Live` | `Long` | `0.2615` | 4,710,000.00 USD | 0.00 USD | 3,250.00 USD | `-70.67%` | `12,426.00` |
| `Live` | `Long` | `0.2625` | 4,700,000.00 USD | 0.00 USD | 849.48 USD | `-70.56%` | `3,236.10` |
| `Live` | `Long` | `0.2685` | 4,700,000.00 USD | 0.00 USD | 106.16 USD | `-69.89%` | `395.40` |
| `Live` | `Long` | `0.2735` | 4,700,000.00 USD | 0.00 USD | 248.34 USD | `-69.33%` | `908.00` |
| `Live` | `Long` | `0.2805` | 4,700,000.00 USD | 0.00 USD | 24,160.00 USD | `-68.54%` | `86,117.40` |
| `Live` | `Long` | `0.2825` | 4,680,000.00 USD | 0.00 USD | 154.64 USD | `-68.32%` | `547.40` |
| `Live` | `Long` | `0.2835` | 4,680,000.00 USD | 0.00 USD | 3,450.00 USD | `-68.21%` | `12,176.00` |
| `Live` | `Long` | `0.2855` | 4,670,000.00 USD | 0.00 USD | 1,430.00 USD | `-67.98%` | `5,000.00` |
| `Live` | `Long` | `0.2885` | 4,670,000.00 USD | 0.00 USD | 29,190.00 USD | `-67.65%` | `101,177.80` |
| `Live` | `Long` | `0.2965` | 4,640,000.00 USD | 0.00 USD | 593.12 USD | `-66.75%` | `2,000.40` |
| `Live` | `Long` | `0.2975` | 4,640,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.64%` | `14,561.30` |
| `Live` | `Long` | `0.3115` | 4,640,000.00 USD | 0.00 USD | 270.38 USD | `-65.07%` | `868.00` |
| `Live` | `Long` | `0.3145` | 4,640,000.00 USD | 0.00 USD | 104.07 USD | `-64.73%` | `330.90` |
| `Live` | `Long` | `0.3205` | 4,640,000.00 USD | 0.00 USD | 3,210.00 USD | `-64.06%` | `10,000.00` |
| `Live` | `Long` | `0.3215` | 4,630,000.00 USD | 0.00 USD | 9,160.00 USD | `-63.94%` | `28,480.20` |
| `Live` | `Long` | `0.3325` | 4,630,000.00 USD | 0.00 USD | 602.79 USD | `-62.71%` | `1,812.90` |
| `Live` | `Long` | `0.3415` | 4,620,000.00 USD | 0.00 USD | 4,270.00 USD | `-61.70%` | `12,500.00` |
| `Live` | `Long` | `0.3465` | 4,620,000.00 USD | 0.00 USD | 5,070.00 USD | `-61.14%` | `14,633.20` |
| `Live` | `Long` | `0.3495` | 4,620,000.00 USD | 0.00 USD | 27,160.00 USD | `-60.80%` | `77,706.40` |
| `Live` | `Long` | `0.3505` | 4,590,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.69%` | `2,908.00` |
| `Live` | `Long` | `0.3585` | 4,590,000.00 USD | 0.00 USD | 595.72 USD | `-59.80%` | `1,661.70` |
| `Live` | `Long` | `0.3635` | 4,590,000.00 USD | 0.00 USD | 405.34 USD | `-59.23%` | `1,115.10` |
| `Live` | `Long` | `0.3655` | 4,590,000.00 USD | 0.00 USD | 406.18 USD | `-59.01%` | `1,111.30` |
| `Live` | `Long` | `0.3665` | 4,590,000.00 USD | 0.00 USD | 274.88 USD | `-58.90%` | `750.00` |
| `Live` | `Long` | `0.3795` | 4,590,000.00 USD | 0.00 USD | 6,730.00 USD | `-57.44%` | `17,732.60` |
| `Live` | `Long` | `0.3815` | 4,580,000.00 USD | 0.00 USD | 267.05 USD | `-57.22%` | `700.00` |
| `Live` | `Long` | `0.3845` | 4,580,000.00 USD | 0.00 USD | 1,750.00 USD | `-56.88%` | `4,562.20` |
| `Live` | `Long` | `0.3895` | 4,580,000.00 USD | 0.00 USD | 2,980.00 USD | `-56.32%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 4,570,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.98%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,570,000.00 USD | 0.00 USD | 754.48 USD | `-55.76%` | `1,912.50` |
| `Live` | `Long` | `0.4035` | 4,570,000.00 USD | 0.00 USD | 9,010.00 USD | `-54.75%` | `22,317.30` |
| `Live` | `Long` | `0.4045` | 4,560,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.64%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,550,000.00 USD | 0.00 USD | 31,820.00 USD | `-54.41%` | `78,275.50` |
| `Live` | `Long` | `0.4165` | 4,520,000.00 USD | 0.00 USD | 733.87 USD | `-53.29%` | `1,762.00` |
| `Live` | `Long` | `0.4245` | 4,520,000.00 USD | 0.00 USD | 468.61 USD | `-52.39%` | `1,103.90` |
| `Live` | `Long` | `0.4375` | 4,520,000.00 USD | 0.00 USD | 514.24 USD | `-50.94%` | `1,175.40` |
| `Live` | `Long` | `0.4385` | 4,520,000.00 USD | 0.00 USD | 429.86 USD | `-50.82%` | `980.30` |
| `Live` | `Long` | `0.4405` | 4,520,000.00 USD | 0.00 USD | 373.46 USD | `-50.60%` | `847.80` |
| `Live` | `Long` | `0.4425` | 4,520,000.00 USD | 0.00 USD | 44,080.00 USD | `-50.38%` | `99,611.70` |
| `Live` | `Long` | `0.4435` | 4,470,000.00 USD | 0.00 USD | 219.00 USD | `-50.26%` | `493.80` |
| `Live` | `Long` | `0.4455` | 4,470,000.00 USD | 0.00 USD | 574.83 USD | `-50.04%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,470,000.00 USD | 0.00 USD | 19,600.00 USD | `-49.93%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,450,000.00 USD | 0.00 USD | 105.25 USD | `-49.81%` | `235.20` |
| `Live` | `Long` | `0.4535` | 4,450,000.00 USD | 0.00 USD | 1,020.00 USD | `-49.14%` | `2,246.80` |
| `Live` | `Long` | `0.4595` | 4,450,000.00 USD | 0.00 USD | 3,330.00 USD | `-48.47%` | `7,245.50` |
| `Live` | `Long` | `0.4725` | 4,450,000.00 USD | 0.00 USD | 1,720.00 USD | `-47.01%` | `3,650.40` |
| `Live` | `Long` | `0.4785` | 4,450,000.00 USD | 0.00 USD | 1,570.00 USD | `-46.34%` | `3,273.50` |
| `Live` | `Long` | `0.4795` | 4,450,000.00 USD | 0.00 USD | 504.48 USD | `-46.23%` | `1,052.10` |
| `Live` | `Long` | `0.4825` | 4,450,000.00 USD | 0.00 USD | 166.70 USD | `-45.89%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,450,000.00 USD | 0.00 USD | 174.01 USD | `-45.78%` | `359.90` |
| `Live` | `Long` | `0.4845` | 4,450,000.00 USD | 0.00 USD | 3,540.00 USD | `-45.66%` | `7,307.20` |
| `Live` | `Long` | `0.4855` | 4,440,000.00 USD | 0.00 USD | 536.96 USD | `-45.55%` | `1,106.00` |
| `Live` | `Long` | `0.4865` | 4,440,000.00 USD | 0.00 USD | 201.07 USD | `-45.44%` | `413.30` |
| `Live` | `Long` | `0.4885` | 4,440,000.00 USD | 0.00 USD | 4,640.00 USD | `-45.22%` | `9,500.00` |
| `Live` | `Long` | `0.4895` | 4,440,000.00 USD | 0.00 USD | 5,630.00 USD | `-45.10%` | `11,505.50` |
| `Live` | `Long` | `0.4915` | 4,430,000.00 USD | 0.00 USD | 2,380.00 USD | `-44.88%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 4,430,000.00 USD | 0.00 USD | 106.32 USD | `-44.54%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,430,000.00 USD | 0.00 USD | 211.88 USD | `-44.43%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,430,000.00 USD | 0.00 USD | 216.75 USD | `-44.09%` | `434.80` |
| `Live` | `Long` | `0.5015` | 4,430,000.00 USD | 0.00 USD | 212.49 USD | `-43.76%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,430,000.00 USD | 0.00 USD | 1,230.00 USD | `-43.65%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 4,430,000.00 USD | 0.00 USD | 211.25 USD | `-43.31%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,430,000.00 USD | 0.00 USD | 5,680.00 USD | `-42.97%` | `11,163.80` |
| `Live` | `Long` | `0.5095` | 4,420,000.00 USD | 0.00 USD | 195.75 USD | `-42.86%` | `384.20` |
| `Live` | `Long` | `0.5105` | 4,420,000.00 USD | 0.00 USD | 102.76 USD | `-42.75%` | `201.30` |
| `Live` | `Long` | `0.5145` | 4,420,000.00 USD | 0.00 USD | 854.17 USD | `-42.30%` | `1,660.20` |
| `Live` | `Long` | `0.5155` | 4,420,000.00 USD | 0.00 USD | 106.04 USD | `-42.19%` | `205.70` |
| `Live` | `Long` | `0.5165` | 4,420,000.00 USD | 0.00 USD | 619.80 USD | `-42.08%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,420,000.00 USD | 0.00 USD | 213.68 USD | `-41.96%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,420,000.00 USD | 0.00 USD | 121.74 USD | `-41.85%` | `234.80` |
| `Live` | `Long` | `0.5215` | 4,420,000.00 USD | 0.00 USD | 123.54 USD | `-41.52%` | `236.90` |
| `Live` | `Long` | `0.5265` | 4,420,000.00 USD | 0.00 USD | 7,140.00 USD | `-40.95%` | `13,552.00` |
| `Live` | `Long` | `0.5275` | 4,410,000.00 USD | 0.00 USD | 348.36 USD | `-40.84%` | `660.40` |
| `Live` | `Long` | `0.5285` | 4,410,000.00 USD | 0.00 USD | 162.83 USD | `-40.73%` | `308.10` |
| `Live` | `Long` | `0.5295` | 4,410,000.00 USD | 0.00 USD | 123,640.00 USD | `-40.62%` | `233,498.70` |
| `Live` | `Long` | `0.5305` | 4,290,000.00 USD | 0.00 USD | 130.08 USD | `-40.51%` | `245.20` |
| `Live` | `Long` | `0.5315` | 4,290,000.00 USD | 0.00 USD | 278.29 USD | `-40.39%` | `523.60` |
| `Live` | `Long` | `0.5325` | 4,290,000.00 USD | 0.00 USD | 2,680.00 USD | `-40.28%` | `5,038.10` |
| `Live` | `Long` | `0.5355` | 4,280,000.00 USD | 0.00 USD | 113.47 USD | `-39.95%` | `211.90` |
| `Live` | `Long` | `0.5375` | 4,280,000.00 USD | 0.00 USD | 7,850.00 USD | `-39.72%` | `14,603.90` |
| `Live` | `Long` | `0.5385` | 4,280,000.00 USD | 0.00 USD | 1,480.00 USD | `-39.61%` | `2,751.80` |
| `Live` | `Long` | `0.5395` | 4,270,000.00 USD | 0.00 USD | 126.46 USD | `-39.50%` | `234.40` |
| `Live` | `Long` | `0.5405` | 4,270,000.00 USD | 0.00 USD | 7,090.00 USD | `-39.38%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,270,000.00 USD | 0.00 USD | 269.13 USD | `-39.16%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,270,000.00 USD | 0.00 USD | 6,150.00 USD | `-38.94%` | `11,285.70` |
| `Live` | `Long` | `0.5465` | 4,260,000.00 USD | 0.00 USD | 272.87 USD | `-38.71%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,260,000.00 USD | 0.00 USD | 1,240.00 USD | `-38.60%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,260,000.00 USD | 0.00 USD | 28,790.00 USD | `-38.38%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,230,000.00 USD | 0.00 USD | 248.06 USD | `-38.26%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,230,000.00 USD | 0.00 USD | 334.82 USD | `-38.15%` | `607.10` |
| `Live` | `Long` | `0.5525` | 4,230,000.00 USD | 0.00 USD | 582.56 USD | `-38.04%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,230,000.00 USD | 0.00 USD | 271.88 USD | `-37.93%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,230,000.00 USD | 0.00 USD | 531.60 USD | `-37.81%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,230,000.00 USD | 0.00 USD | 7,950.00 USD | `-37.70%` | `14,310.10` |
| `Live` | `Long` | `0.5565` | 4,220,000.00 USD | 0.00 USD | 556.50 USD | `-37.59%` | `1,000.00` |
| `Live` | `Long` | `0.5585` | 4,220,000.00 USD | 0.00 USD | 141.97 USD | `-37.37%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,220,000.00 USD | 0.00 USD | 304.93 USD | `-37.25%` | `545.00` |
| `Live` | `Long` | `0.5615` | 4,220,000.00 USD | 0.00 USD | 442.63 USD | `-37.03%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,220,000.00 USD | 0.00 USD | 330.53 USD | `-36.92%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,220,000.00 USD | 0.00 USD | 1,300.00 USD | `-36.81%` | `2,314.70` |
| `Live` | `Long` | `0.5655` | 4,220,000.00 USD | 0.00 USD | 8,190.00 USD | `-36.58%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,210,000.00 USD | 0.00 USD | 7,200.00 USD | `-36.47%` | `12,714.00` |
| `Live` | `Long` | `0.5675` | 4,200,000.00 USD | 0.00 USD | 1,560.00 USD | `-36.36%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,200,000.00 USD | 0.00 USD | 973.22 USD | `-36.13%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,200,000.00 USD | 0.00 USD | 139.23 USD | `-35.80%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,200,000.00 USD | 0.00 USD | 109,930.00 USD | `-35.68%` | `191,690.40` |
| `Live` | `Long` | `0.5745` | 4,090,000.00 USD | 0.00 USD | 144.03 USD | `-35.57%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,090,000.00 USD | 0.00 USD | 217.37 USD | `-35.46%` | `377.70` |
| `Live` | `Long` | `0.5765` | 4,090,000.00 USD | 0.00 USD | 1,490.00 USD | `-35.35%` | `2,588.60` |
| `Live` | `Long` | `0.5775` | 4,090,000.00 USD | 0.00 USD | 497.75 USD | `-35.24%` | `861.90` |
| `Live` | `Long` | `0.5795` | 4,090,000.00 USD | 0.00 USD | 6,470.00 USD | `-35.01%` | `11,172.60` |
| `Live` | `Long` | `0.5805` | 4,080,000.00 USD | 0.00 USD | 1,410.00 USD | `-34.90%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,080,000.00 USD | 0.00 USD | 6,470.00 USD | `-34.67%` | `11,099.00` |
| `Live` | `Long` | `0.5855` | 4,070,000.00 USD | 0.00 USD | 2,640.00 USD | `-34.34%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,070,000.00 USD | 0.00 USD | 466.85 USD | `-34.23%` | `796.00` |
| `Live` | `Long` | `0.5885` | 4,070,000.00 USD | 0.00 USD | 311.14 USD | `-34.00%` | `528.70` |
| `Live` | `Long` | `0.5905` | 4,070,000.00 USD | 0.00 USD | 225.93 USD | `-33.78%` | `382.60` |
| `Live` | `Long` | `0.5925` | 4,070,000.00 USD | 0.00 USD | 994.16 USD | `-33.55%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,070,000.00 USD | 0.00 USD | 132.41 USD | `-33.44%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,070,000.00 USD | 0.00 USD | 8,220.00 USD | `-33.33%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,060,000.00 USD | 0.00 USD | 608.61 USD | `-33.10%` | `1,020.30` |
| `Live` | `Long` | `0.5975` | 4,060,000.00 USD | 0.00 USD | 3,420.00 USD | `-32.99%` | `5,729.40` |
| `Live` | `Long` | `0.5985` | 4,060,000.00 USD | 0.00 USD | 14,140.00 USD | `-32.88%` | `23,624.30` |
| `Live` | `Long` | `0.5995` | 4,040,000.00 USD | 0.00 USD | 4,760.00 USD | `-32.77%` | `7,936.80` |
| `Live` | `Long` | `0.6005` | 4,040,000.00 USD | 0.00 USD | 351.11 USD | `-32.66%` | `584.70` |
| `Live` | `Long` | `0.6015` | 4,040,000.00 USD | 0.00 USD | 323.79 USD | `-32.54%` | `538.30` |
| `Live` | `Long` | `0.6025` | 4,040,000.00 USD | 0.00 USD | 432.35 USD | `-32.43%` | `717.60` |
| `Live` | `Long` | `0.6035` | 4,040,000.00 USD | 0.00 USD | 1,220.00 USD | `-32.32%` | `2,023.70` |
| `Live` | `Long` | `0.6075` | 4,040,000.00 USD | 0.00 USD | 851.05 USD | `-31.87%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,030,000.00 USD | 0.00 USD | 886.10 USD | `-31.76%` | `1,456.20` |
| `Live` | `Long` | `0.6095` | 4,030,000.00 USD | 0.00 USD | 214.54 USD | `-31.65%` | `352.00` |
| `Live` | `Long` | `0.6115` | 4,030,000.00 USD | 0.00 USD | 6,280.00 USD | `-31.42%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 4,030,000.00 USD | 0.00 USD | 438.73 USD | `-31.31%` | `716.30` |
| `Live` | `Long` | `0.6135` | 4,030,000.00 USD | 0.00 USD | 112.33 USD | `-31.20%` | `183.10` |
| `Live` | `Long` | `0.6145` | 4,030,000.00 USD | 0.00 USD | 4,880.00 USD | `-31.09%` | `7,935.00` |
| `Live` | `Long` | `0.6155` | 4,020,000.00 USD | 0.00 USD | 935.13 USD | `-30.97%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 4,020,000.00 USD | 0.00 USD | 29,900.00 USD | `-30.86%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 3,990,000.00 USD | 0.00 USD | 4,980.00 USD | `-30.75%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 3,990,000.00 USD | 0.00 USD | 12,570.00 USD | `-30.64%` | `20,327.90` |
| `Live` | `Long` | `0.6195` | 3,970,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.53%` | `3,868.00` |
| `Live` | `Long` | `0.6225` | 3,970,000.00 USD | 0.00 USD | 708.53 USD | `-30.19%` | `1,138.20` |
| `Live` | `Long` | `0.6235` | 3,970,000.00 USD | 0.00 USD | 187.05 USD | `-30.08%` | `300.00` |
| `Live` | `Long` | `0.6245` | 3,970,000.00 USD | 0.00 USD | 356.65 USD | `-29.96%` | `571.10` |
| `Live` | `Long` | `0.6285` | 3,970,000.00 USD | 0.00 USD | 102.45 USD | `-29.52%` | `163.00` |
| `Live` | `Long` | `0.6295` | 3,970,000.00 USD | 0.00 USD | 1,100.00 USD | `-29.40%` | `1,739.60` |
| `Live` | `Long` | `0.6305` | 3,970,000.00 USD | 0.00 USD | 319.35 USD | `-29.29%` | `506.50` |
| `Live` | `Long` | `0.6345` | 3,970,000.00 USD | 0.00 USD | 843.00 USD | `-28.84%` | `1,328.60` |
| `Live` | `Long` | `0.6365` | 3,970,000.00 USD | 0.00 USD | 3,060.00 USD | `-28.62%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,960,000.00 USD | 0.00 USD | 7,600.00 USD | `-28.51%` | `11,926.70` |
| `Live` | `Long` | `0.6385` | 3,960,000.00 USD | 0.00 USD | 34,150.00 USD | `-28.39%` | `53,492.10` |
| `Live` | `Long` | `0.6405` | 3,920,000.00 USD | 0.00 USD | 33,040.00 USD | `-28.17%` | `51,581.80` |
| `Live` | `Long` | `0.6415` | 3,890,000.00 USD | 0.00 USD | 86,920.00 USD | `-28.06%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,800,000.00 USD | 0.00 USD | 4,980.00 USD | `-27.95%` | `7,754.70` |
| `Live` | `Long` | `0.6435` | 3,800,000.00 USD | 0.00 USD | 3,190.00 USD | `-27.83%` | `4,951.30` |
| `Live` | `Long` | `0.6445` | 3,790,000.00 USD | 0.00 USD | 65,790.00 USD | `-27.72%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,730,000.00 USD | 0.00 USD | 14,590.00 USD | `-27.61%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,710,000.00 USD | 0.00 USD | 2,370.00 USD | `-27.50%` | `3,667.40` |
| `Live` | `Long` | `0.6475` | 3,710,000.00 USD | 0.00 USD | 3,200.00 USD | `-27.39%` | `4,945.10` |
| `Live` | `Long` | `0.6485` | 3,710,000.00 USD | 0.00 USD | 668.34 USD | `-27.27%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,710,000.00 USD | 0.00 USD | 91,460.00 USD | `-27.16%` | `140,810.00` |
| `Live` | `Long` | `0.6505` | 3,620,000.00 USD | 0.00 USD | 1,300.00 USD | `-27.05%` | `1,991.10` |
| `Live` | `Long` | `0.6515` | 3,610,000.00 USD | 0.00 USD | 403,320.00 USD | `-26.94%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,210,000.00 USD | 0.00 USD | 2,350.00 USD | `-26.82%` | `3,599.00` |
| `Live` | `Long` | `0.6535` | 3,210,000.00 USD | 0.00 USD | 2,840.00 USD | `-26.71%` | `4,345.80` |
| `Live` | `Long` | `0.6545` | 3,210,000.00 USD | 0.00 USD | 6,700.00 USD | `-26.60%` | `10,231.40` |
| `Live` | `Long` | `0.6555` | 3,200,000.00 USD | 0.00 USD | 1,830.00 USD | `-26.49%` | `2,793.70` |
| `Live` | `Long` | `0.6565` | 3,200,000.00 USD | 0.00 USD | 7,070.00 USD | `-26.38%` | `10,764.20` |
| `Live` | `Long` | `0.6575` | 3,190,000.00 USD | 0.00 USD | 13,280.00 USD | `-26.26%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,180,000.00 USD | 0.00 USD | 2,970.00 USD | `-26.15%` | `4,508.30` |
| `Live` | `Long` | `0.6615` | 3,170,000.00 USD | 0.00 USD | 325.46 USD | `-25.82%` | `492.00` |
| `Live` | `Long` | `0.6625` | 3,170,000.00 USD | 0.00 USD | 4,840.00 USD | `-25.70%` | `7,306.80` |
| `Live` | `Long` | `0.6645` | 3,170,000.00 USD | 0.00 USD | 448.54 USD | `-25.48%` | `675.00` |
| `Live` | `Long` | `0.6665` | 3,170,000.00 USD | 0.00 USD | 528.73 USD | `-25.25%` | `793.30` |
| `Live` | `Long` | `0.6675` | 3,170,000.00 USD | 0.00 USD | 2,260.00 USD | `-25.14%` | `3,386.00` |
| `Live` | `Long` | `0.6685` | 3,170,000.00 USD | 0.00 USD | 5,470.00 USD | `-25.03%` | `8,188.90` |
| `Live` | `Long` | `0.6695` | 3,160,000.00 USD | 0.00 USD | 337.36 USD | `-24.92%` | `503.90` |
| `Live` | `Long` | `0.6705` | 3,160,000.00 USD | 0.00 USD | 29,210.00 USD | `-24.81%` | `43,566.30` |
| `Live` | `Long` | `0.6715` | 3,130,000.00 USD | 0.00 USD | 2,240.00 USD | `-24.69%` | `3,341.20` |
| `Live` | `Long` | `0.6725` | 3,130,000.00 USD | 0.00 USD | 1,620.00 USD | `-24.58%` | `2,406.60` |
| `Live` | `Long` | `0.6735` | 3,130,000.00 USD | 0.00 USD | 835.14 USD | `-24.47%` | `1,240.00` |
| `Live` | `Long` | `0.6745` | 3,130,000.00 USD | 0.00 USD | 6,520.00 USD | `-24.36%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 3,120,000.00 USD | 0.00 USD | 868.02 USD | `-24.24%` | `1,285.00` |
| `Live` | `Long` | `0.6765` | 3,120,000.00 USD | 0.00 USD | 933.37 USD | `-24.13%` | `1,379.70` |
| `Live` | `Long` | `0.6775` | 3,120,000.00 USD | 0.00 USD | 9,150.00 USD | `-24.02%` | `13,500.00` |
| `Live` | `Long` | `0.6785` | 3,110,000.00 USD | 0.00 USD | 122.94 USD | `-23.91%` | `181.20` |
| `Live` | `Long` | `0.6795` | 3,110,000.00 USD | 0.00 USD | 43,650.00 USD | `-23.80%` | `64,238.50` |
| `Live` | `Long` | `0.6805` | 3,060,000.00 USD | 0.00 USD | 1,600.00 USD | `-23.68%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 3,060,000.00 USD | 0.00 USD | 2,110.00 USD | `-23.57%` | `3,092.70` |
| `Live` | `Long` | `0.6825` | 3,060,000.00 USD | 0.00 USD | 17,190.00 USD | `-23.46%` | `25,192.00` |
| `Live` | `Long` | `0.6835` | 3,040,000.00 USD | 0.00 USD | 15,130.00 USD | `-23.35%` | `22,136.50` |
| `Live` | `Long` | `0.6845` | 3,030,000.00 USD | 0.00 USD | 5,960.00 USD | `-23.24%` | `8,711.60` |
| `Live` | `Long` | `0.6865` | 3,020,000.00 USD | 0.00 USD | 112.59 USD | `-23.01%` | `164.00` |
| `Live` | `Long` | `0.6875` | 3,020,000.00 USD | 0.00 USD | 6,110.00 USD | `-22.90%` | `8,883.90` |
| `Live` | `Long` | `0.6895` | 3,020,000.00 USD | 0.00 USD | 3,170.00 USD | `-22.67%` | `4,601.40` |
| `Live` | `Long` | `0.6905` | 3,010,000.00 USD | 0.00 USD | 3,360.00 USD | `-22.56%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 3,010,000.00 USD | 0.00 USD | 8,970.00 USD | `-22.45%` | `12,967.20` |
| `Live` | `Long` | `0.6925` | 3,000,000.00 USD | 0.00 USD | 282.54 USD | `-22.34%` | `408.00` |
| `Live` | `Long` | `0.6935` | 3,000,000.00 USD | 0.00 USD | 3,600.00 USD | `-22.23%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 3,000,000.00 USD | 0.00 USD | 722.28 USD | `-22.11%` | `1,040.00` |
| `Live` | `Long` | `0.6955` | 3,000,000.00 USD | 0.00 USD | 1,700.00 USD | `-22.00%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,990,000.00 USD | 0.00 USD | 273.03 USD | `-21.89%` | `392.00` |
| `Live` | `Long` | `0.6975` | 2,990,000.00 USD | 0.00 USD | 1,030.00 USD | `-21.78%` | `1,482.80` |
| `Live` | `Long` | `0.6985` | 2,990,000.00 USD | 0.00 USD | 4,830.00 USD | `-21.67%` | `6,919.90` |
| `Live` | `Long` | `0.7005` | 2,990,000.00 USD | 0.00 USD | 235.37 USD | `-21.44%` | `336.00` |
| `Live` | `Long` | `0.7015` | 2,990,000.00 USD | 0.00 USD | 1,990.00 USD | `-21.33%` | `2,841.50` |
| `Live` | `Long` | `0.7045` | 2,990,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.99%` | `12,729.60` |
| `Live` | `Long` | `0.7065` | 2,980,000.00 USD | 0.00 USD | 143.14 USD | `-20.77%` | `202.60` |
| `Live` | `Long` | `0.7075` | 2,980,000.00 USD | 0.00 USD | 3,620.00 USD | `-20.66%` | `5,122.60` |
| `Live` | `Long` | `0.7085` | 2,970,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.54%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,970,000.00 USD | 0.00 USD | 8,760.00 USD | `-20.43%` | `12,349.40` |
| `Live` | `Long` | `0.7105` | 2,960,000.00 USD | 0.00 USD | 25,350.00 USD | `-20.32%` | `35,683.00` |
| `Live` | `Long` | `0.7125` | 2,940,000.00 USD | 0.00 USD | 283.22 USD | `-20.10%` | `397.50` |
| `Live` | `Long` | `0.7135` | 2,940,000.00 USD | 0.00 USD | 927.55 USD | `-19.98%` | `1,300.00` |
| `Live` | `Long` | `0.7145` | 2,940,000.00 USD | 0.00 USD | 428,700.00 USD | `-19.87%` | `600,000.00` |
| `Live` | `Long` | `0.7155` | 2,510,000.00 USD | 0.00 USD | 11,030.00 USD | `-19.76%` | `15,416.10` |
| `Live` | `Long` | `0.7165` | 2,500,000.00 USD | 0.00 USD | 4,620.00 USD | `-19.65%` | `6,444.00` |
| `Live` | `Long` | `0.7185` | 2,490,000.00 USD | 0.00 USD | 126.96 USD | `-19.42%` | `176.70` |
| `Live` | `Long` | `0.7195` | 2,490,000.00 USD | 0.00 USD | 420.19 USD | `-19.31%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,490,000.00 USD | 0.00 USD | 8,450.00 USD | `-19.09%` | `11,706.20` |
| `Live` | `Long` | `0.7225` | 2,480,000.00 USD | 0.00 USD | 1,920.00 USD | `-18.97%` | `2,659.50` |
| `Live` | `Long` | `0.7235` | 2,480,000.00 USD | 0.00 USD | 127.05 USD | `-18.86%` | `175.60` |
| `Live` | `Long` | `0.7245` | 2,480,000.00 USD | 0.00 USD | 2,520.00 USD | `-18.75%` | `3,475.80` |
| `Live` | `Long` | `0.7255` | 2,480,000.00 USD | 0.00 USD | 311.60 USD | `-18.64%` | `429.50` |
| `Live` | `Long` | `0.7265` | 2,480,000.00 USD | 0.00 USD | 3,410.00 USD | `-18.53%` | `4,687.00` |
| `Live` | `Long` | `0.7275` | 2,470,000.00 USD | 0.00 USD | 35,890.00 USD | `-18.41%` | `49,332.50` |
| `Live` | `Long` | `0.7285` | 2,440,000.00 USD | 0.00 USD | 424.86 USD | `-18.30%` | `583.20` |
| `Live` | `Long` | `0.7295` | 2,440,000.00 USD | 0.00 USD | 375.98 USD | `-18.19%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,440,000.00 USD | 0.00 USD | 119.88 USD | `-18.08%` | `164.10` |
| `Live` | `Long` | `0.7325` | 2,440,000.00 USD | 0.00 USD | 13,500.00 USD | `-17.85%` | `18,432.50` |
| `Live` | `Long` | `0.7335` | 2,420,000.00 USD | 0.00 USD | 8,260.00 USD | `-17.74%` | `11,261.30` |
| `Live` | `Long` | `0.7345` | 2,420,000.00 USD | 0.00 USD | 6,240.00 USD | `-17.63%` | `8,498.00` |
| `Live` | `Long` | `0.7355` | 2,410,000.00 USD | 0.00 USD | 51,920.00 USD | `-17.52%` | `70,595.50` |
| `Live` | `Long` | `0.7375` | 2,360,000.00 USD | 0.00 USD | 7,100.00 USD | `-17.29%` | `9,632.90` |
| `Live` | `Long` | `0.7385` | 2,350,000.00 USD | 0.00 USD | 6,020.00 USD | `-17.18%` | `8,146.50` |
| `Live` | `Long` | `0.7395` | 2,350,000.00 USD | 0.00 USD | 3,380.00 USD | `-17.07%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,340,000.00 USD | 0.00 USD | 3,530.00 USD | `-16.96%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,340,000.00 USD | 0.00 USD | 382.61 USD | `-16.84%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,340,000.00 USD | 0.00 USD | 2,430.00 USD | `-16.73%` | `3,275.30` |
| `Live` | `Long` | `0.7435` | 2,340,000.00 USD | 0.00 USD | 783,980.00 USD | `-16.62%` | `1,054,441.80` |
| `Live` | `Long` | `0.7455` | 1,550,000.00 USD | 0.00 USD | 4,020.00 USD | `-16.39%` | `5,393.10` |
| `Live` | `Long` | `0.7465` | 1,550,000.00 USD | 0.00 USD | 359.96 USD | `-16.28%` | `482.20` |
| `Live` | `Long` | `0.7475` | 1,550,000.00 USD | 0.00 USD | 107,260.00 USD | `-16.17%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,440,000.00 USD | 0.00 USD | 4,820.00 USD | `-15.95%` | `6,426.70` |
| `Live` | `Long` | `0.7515` | 1,430,000.00 USD | 0.00 USD | 1,210.00 USD | `-15.72%` | `1,613.50` |
| `Live` | `Long` | `0.7535` | 1,430,000.00 USD | 0.00 USD | 569.50 USD | `-15.50%` | `755.80` |
| `Live` | `Long` | `0.7545` | 1,430,000.00 USD | 0.00 USD | 1,250.00 USD | `-15.39%` | `1,650.60` |
| `Live` | `Long` | `0.7555` | 1,430,000.00 USD | 0.00 USD | 1,750.00 USD | `-15.27%` | `2,315.50` |
| `Live` | `Long` | `0.7575` | 1,430,000.00 USD | 0.00 USD | 1,900.00 USD | `-15.05%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,430,000.00 USD | 0.00 USD | 40,520.00 USD | `-14.94%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,390,000.00 USD | 0.00 USD | 4,900.00 USD | `-14.82%` | `6,448.30` |
| `Live` | `Long` | `0.7605` | 1,380,000.00 USD | 0.00 USD | 2,920.00 USD | `-14.71%` | `3,840.20` |
| `Live` | `Long` | `0.7615` | 1,380,000.00 USD | 0.00 USD | 351.43 USD | `-14.60%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,380,000.00 USD | 0.00 USD | 859.11 USD | `-14.49%` | `1,126.70` |
| `Live` | `Long` | `0.7635` | 1,380,000.00 USD | 0.00 USD | 439.47 USD | `-14.38%` | `575.60` |
| `Live` | `Long` | `0.7645` | 1,380,000.00 USD | 0.00 USD | 1,060.00 USD | `-14.26%` | `1,384.30` |
| `Live` | `Long` | `0.7655` | 1,380,000.00 USD | 0.00 USD | 4,430.00 USD | `-14.15%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,370,000.00 USD | 0.00 USD | 1,260.00 USD | `-14.04%` | `1,649.10` |
| `Live` | `Long` | `0.7675` | 1,370,000.00 USD | 0.00 USD | 25,580.00 USD | `-13.93%` | `33,323.60` |
| `Live` | `Long` | `0.7685` | 1,350,000.00 USD | 0.00 USD | 207.19 USD | `-13.82%` | `269.60` |
| `Live` | `Long` | `0.7695` | 1,350,000.00 USD | 0.00 USD | 468,690.00 USD | `-13.70%` | `609,082.40` |
| `Live` | `Long` | `0.7705` | 876,990.00 USD | 0.00 USD | 5,640.00 USD | `-13.59%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 871,350.00 USD | 0.00 USD | 19,250.00 USD | `-13.48%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 852,100.00 USD | 0.00 USD | 1,940.00 USD | `-13.37%` | `2,515.50` |
| `Live` | `Long` | `0.7735` | 850,150.00 USD | 0.00 USD | 5,230.00 USD | `-13.25%` | `6,756.40` |
| `Live` | `Long` | `0.7755` | 844,930.00 USD | 0.00 USD | 3,430.00 USD | `-13.03%` | `4,424.80` |
| `Live` | `Long` | `0.7765` | 841,500.00 USD | 0.00 USD | 3,510.00 USD | `-12.92%` | `4,518.50` |
| `Live` | `Long` | `0.7785` | 837,990.00 USD | 0.00 USD | 28,010.00 USD | `-12.69%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 809,980.00 USD | 0.00 USD | 338.69 USD | `-12.58%` | `434.50` |
| `Live` | `Long` | `0.7815` | 809,640.00 USD | 0.00 USD | 4,160.00 USD | `-12.36%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 805,480.00 USD | 0.00 USD | 24,380.00 USD | `-12.13%` | `31,116.60` |
| `Live` | `Long` | `0.7865` | 781,100.00 USD | 0.00 USD | 3,470.00 USD | `-11.80%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 777,620.00 USD | 0.00 USD | 288.70 USD | `-11.68%` | `366.60` |
| `Live` | `Long` | `0.7905` | 777,330.00 USD | 0.00 USD | 3,670.00 USD | `-11.35%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 773,670.00 USD | 0.00 USD | 11,400.00 USD | `-11.24%` | `14,400.60` |
| `Live` | `Long` | `0.7925` | 762,270.00 USD | 0.00 USD | 10,810.00 USD | `-11.12%` | `13,636.90` |
| `Live` | `Long` | `0.7935` | 751,460.00 USD | 0.00 USD | 809.45 USD | `-11.01%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 750,650.00 USD | 0.00 USD | 736.66 USD | `-10.90%` | `927.20` |
| `Live` | `Long` | `0.7955` | 749,920.00 USD | 0.00 USD | 52,610.00 USD | `-10.79%` | `66,134.90` |
| `Live` | `Long` | `0.7965` | 697,310.00 USD | 0.00 USD | 12,980.00 USD | `-10.68%` | `16,300.50` |
| `Live` | `Long` | `0.7975` | 684,320.00 USD | 0.00 USD | 7,460.00 USD | `-10.56%` | `9,359.90` |
| `Live` | `Long` | `0.7985` | 676,860.00 USD | 0.00 USD | 40,230.00 USD | `-10.45%` | `50,386.80` |
| `Live` | `Long` | `0.7995` | 636,620.00 USD | 0.00 USD | 7,590.00 USD | `-10.34%` | `9,489.80` |
| `Live` | `Long` | `0.8005` | 629,040.00 USD | 0.00 USD | 3,740.00 USD | `-10.23%` | `4,666.20` |
| `Live` | `Long` | `0.8015` | 625,300.00 USD | 0.00 USD | 7,500.00 USD | `-10.11%` | `9,361.90` |
| `Live` | `Long` | `0.8025` | 617,800.00 USD | 0.00 USD | 3,830.00 USD | `-10.00%` | `4,767.30` |
| `Live` | `Long` | `0.8035` | 613,970.00 USD | 0.00 USD | 7,680.00 USD | `-9.89%` | `9,559.90` |
| `Live` | `Long` | `0.8045` | 606,290.00 USD | 0.00 USD | 16,660.00 USD | `-9.78%` | `20,710.00` |
| `Live` | `Long` | `0.8055` | 589,630.00 USD | 0.00 USD | 361.11 USD | `-9.67%` | `448.30` |
| `Live` | `Long` | `0.8065` | 589,270.00 USD | 0.00 USD | 6,910.00 USD | `-9.55%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 582,360.00 USD | 0.00 USD | 2,770.00 USD | `-9.44%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 579,590.00 USD | 0.00 USD | 22,620.00 USD | `-9.33%` | `27,983.60` |
| `Live` | `Long` | `0.8095` | 556,970.00 USD | 0.00 USD | 130,110.00 USD | `-9.22%` | `160,732.40` |
| `Live` | `Long` | `0.8105` | 426,850.00 USD | 0.00 USD | 2,250.00 USD | `-9.11%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 424,600.00 USD | 0.00 USD | 2,970.00 USD | `-8.99%` | `3,654.30` |
| `Live` | `Long` | `0.8125` | 421,630.00 USD | 0.00 USD | 1,160.00 USD | `-8.88%` | `1,421.60` |
| `Live` | `Long` | `0.8135` | 420,480.00 USD | 0.00 USD | 3,800.00 USD | `-8.77%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 416,670.00 USD | 0.00 USD | 277.42 USD | `-8.66%` | `340.60` |
| `Live` | `Long` | `0.8155` | 416,400.00 USD | 0.00 USD | 38,250.00 USD | `-8.54%` | `46,908.50` |
| `Live` | `Long` | `0.8165` | 378,140.00 USD | 0.00 USD | 104.92 USD | `-8.43%` | `128.50` |
| `Live` | `Long` | `0.8175` | 378,040.00 USD | 0.00 USD | 77,840.00 USD | `-8.32%` | `95,214.30` |
| `Live` | `Long` | `0.8185` | 300,200.00 USD | 0.00 USD | 24,620.00 USD | `-8.21%` | `30,080.00` |
| `Live` | `Long` | `0.8195` | 275,580.00 USD | 0.00 USD | 1,230.00 USD | `-8.10%` | `1,498.80` |
| `Live` | `Long` | `0.8205` | 274,350.00 USD | 0.00 USD | 5,360.00 USD | `-7.98%` | `6,531.20` |
| `Live` | `Long` | `0.8215` | 268,990.00 USD | 0.00 USD | 474.01 USD | `-7.87%` | `577.00` |
| `Live` | `Long` | `0.8225` | 268,520.00 USD | 0.00 USD | 2,890.00 USD | `-7.76%` | `3,517.50` |
| `Live` | `Long` | `0.8235` | 265,630.00 USD | 0.00 USD | 463.63 USD | `-7.65%` | `563.00` |
| `Live` | `Long` | `0.8245` | 265,160.00 USD | 0.00 USD | 18,980.00 USD | `-7.54%` | `23,022.60` |
| `Live` | `Long` | `0.8255` | 246,180.00 USD | 0.00 USD | 1,580.00 USD | `-7.42%` | `1,911.90` |
| `Live` | `Long` | `0.8275` | 244,600.00 USD | 0.00 USD | 4,690.00 USD | `-7.20%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 239,920.00 USD | 0.00 USD | 120,070.00 USD | `-7.09%` | `144,926.90` |
| `Live` | `Long` | `0.8295` | 119,840.00 USD | 0.00 USD | 46,590.00 USD | `-6.97%` | `56,161.30` |
| `Live` | `Long` | `0.8345` | 73,260.00 USD | 0.00 USD | 5,750.00 USD | `-6.41%` | `6,885.20` |
| `Live` | `Long` | `0.8375` | 67,510.00 USD | 0.00 USD | 327.21 USD | `-6.08%` | `390.70` |
| `Live` | `Long` | `0.8385` | 67,180.00 USD | 0.00 USD | 7,300.00 USD | `-5.97%` | `8,701.00` |
| `Live` | `Long` | `0.8405` | 59,890.00 USD | 0.00 USD | 862.10 USD | `-5.74%` | `1,025.70` |
| `Live` | `Long` | `0.8415` | 59,030.00 USD | 0.00 USD | 134.47 USD | `-5.63%` | `159.80` |
| `Live` | `Long` | `0.8425` | 58,890.00 USD | 0.00 USD | 11,390.00 USD | `-5.52%` | `13,521.40` |
| `Live` | `Long` | `0.8455` | 47,500.00 USD | 0.00 USD | 745.82 USD | `-5.18%` | `882.10` |
| `Live` | `Long` | `0.8475` | 46,750.00 USD | 0.00 USD | 317.98 USD | `-4.96%` | `375.20` |
| `Live` | `Long` | `0.8485` | 46,440.00 USD | 0.00 USD | 202.28 USD | `-4.84%` | `238.40` |
| `Live` | `Long` | `0.8525` | 46,230.00 USD | 0.00 USD | 42,610.00 USD | `-4.40%` | `49,980.80` |
| `Live` | `Long` | `0.8545` | 3,630.00 USD | 0.00 USD | 3,630.00 USD | `-4.17%` | `4,242.90` |
| `Live` | `Short` | `0.8965` | 852.66 USD | 852.66 USD | 0.00 USD | `+0.54%` | `951.10` |
| `Live` | `Short` | `0.9145` | 4,920.00 USD | 4,060.00 USD | 0.00 USD | `+2.56%` | `4,444.10` |
| `Live` | `Short` | `0.9195` | 14,110.00 USD | 9,200.00 USD | 0.00 USD | `+3.12%` | `10,000.00` |
| `Live` | `Short` | `0.9235` | 14,320.00 USD | 209.36 USD | 0.00 USD | `+3.57%` | `226.70` |
| `Live` | `Short` | `0.9385` | 54,170.00 USD | 39,850.00 USD | 0.00 USD | `+5.25%` | `42,456.90` |
| `Live` | `Short` | `0.9425` | 56,220.00 USD | 2,050.00 USD | 0.00 USD | `+5.70%` | `2,174.10` |
| `Live` | `Short` | `0.9445` | 56,320.00 USD | 103.90 USD | 0.00 USD | `+5.92%` | `110.00` |
| `Live` | `Short` | `0.9805` | 57,370.00 USD | 1,050.00 USD | 0.00 USD | `+9.96%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 57,730.00 USD | 365.70 USD | 0.00 USD | `+10.63%` | `370.70` |
| `Live` | `Short` | `0.9885` | 61,990.00 USD | 4,250.00 USD | 0.00 USD | `+10.86%` | `4,304.30` |
| `Live` | `Short` | `0.9915` | 63,560.00 USD | 1,570.00 USD | 0.00 USD | `+11.19%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 63,700.00 USD | 139.59 USD | 0.00 USD | `+11.42%` | `140.50` |
| `Live` | `Short` | `1.00` | 64,030.00 USD | 330.29 USD | 0.00 USD | `+12.31%` | `329.80` |
| `Live` | `Short` | `1.01` | 64,740.00 USD | 705.99 USD | 0.00 USD | `+13.77%` | `695.90` |
| `Live` | `Short` | `1.02` | 64,910.00 USD | 170.40 USD | 0.00 USD | `+13.88%` | `167.80` |
| `Live` | `Short` | `1.03` | 75,950.00 USD | 11,040.00 USD | 0.00 USD | `+15.45%` | `10,723.80` |
| `Live` | `Short` | `1.04` | 76,050.00 USD | 103.85 USD | 0.00 USD | `+16.46%` | `100.00` |
| `Live` | `Short` | `1.05` | 76,650.00 USD | 597.52 USD | 0.00 USD | `+17.81%` | `568.80` |
| `Live` | `Short` | `1.05` | 79,490.00 USD | 2,840.00 USD | 0.00 USD | `+17.92%` | `2,697.50` |
| `Live` | `Short` | `1.06` | 81,220.00 USD | 1,740.00 USD | 0.00 USD | `+18.82%` | `1,639.00` |
| `Live` | `Short` | `1.08` | 84,800.00 USD | 3,580.00 USD | 0.00 USD | `+21.17%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 90,360.00 USD | 5,550.00 USD | 0.00 USD | `+22.18%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 90,680.00 USD | 324.90 USD | 0.00 USD | `+23.31%` | `295.50` |
| `Live` | `Short` | `1.10` | 90,960.00 USD | 277.22 USD | 0.00 USD | `+23.42%` | `251.90` |
| `Live` | `Short` | `1.11` | 99,900.00 USD | 8,940.00 USD | 0.00 USD | `+24.54%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 123,200.00 USD | 23,310.00 USD | 0.00 USD | `+26.33%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 123,840.00 USD | 634.09 USD | 0.00 USD | `+27.01%` | `559.90` |
| `Live` | `Short` | `1.15` | 124,480.00 USD | 639.88 USD | 0.00 USD | `+28.46%` | `558.60` |
| `Live` | `Short` | `1.15` | 124,610.00 USD | 129.88 USD | 0.00 USD | `+29.36%` | `112.60` |
| `Live` | `Short` | `1.20` | 124,790.00 USD | 177.65 USD | 0.00 USD | `+34.52%` | `148.10` |
| `Live` | `Short` | `1.22` | 129,230.00 USD | 4,440.00 USD | 0.00 USD | `+36.65%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 129,610.00 USD | 383.01 USD | 0.00 USD | `+37.10%` | `313.30` |
| `Live` | `Short` | `1.23` | 129,990.00 USD | 380.84 USD | 0.00 USD | `+38.44%` | `308.50` |
| `Live` | `Short` | `1.24` | 133,920.00 USD | 3,930.00 USD | 0.00 USD | `+39.01%` | `3,169.40` |
| `Live` | `Short` | `1.26` | 136,590.00 USD | 2,670.00 USD | 0.00 USD | `+41.25%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 138,890.00 USD | 2,300.00 USD | 0.00 USD | `+43.27%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 148,630.00 USD | 9,740.00 USD | 0.00 USD | `+43.38%` | `7,618.00` |
| `Live` | `Short` | `1.28` | 188,520.00 USD | 39,880.00 USD | 0.00 USD | `+43.83%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 188,740.00 USD | 226.80 USD | 0.00 USD | `+45.17%` | `175.20` |
| `Live` | `Short` | `1.30` | 188,860.00 USD | 114.40 USD | 0.00 USD | `+45.62%` | `88.10` |
| `Live` | `Short` | `1.31` | 189,880.00 USD | 1,020.00 USD | 0.00 USD | `+46.86%` | `777.20` |
| `Live` | `Short` | `1.31` | 221,410.00 USD | 31,530.00 USD | 0.00 USD | `+47.08%` | `24,042.40` |
| `Live` | `Short` | `1.32` | 222,500.00 USD | 1,090.00 USD | 0.00 USD | `+48.43%` | `826.40` |
| `Live` | `Short` | `1.33` | 228,840.00 USD | 6,340.00 USD | 0.00 USD | `+48.65%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 250,810.00 USD | 21,970.00 USD | 0.00 USD | `+48.99%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 257,660.00 USD | 6,860.00 USD | 0.00 USD | `+50.22%` | `5,119.30` |
| `Live` | `Short` | `1.35` | 257,800.00 USD | 132.52 USD | 0.00 USD | `+51.34%` | `98.20` |
| `Live` | `Short` | `1.37` | 616,080.00 USD | 358,280.00 USD | 0.00 USD | `+53.92%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 620,520.00 USD | 4,450.00 USD | 0.00 USD | `+58.63%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 620,930.00 USD | 402.08 USD | 0.00 USD | `+61.10%` | `279.90` |
| `Live` | `Short` | `1.44` | 621,210.00 USD | 288.68 USD | 0.00 USD | `+61.55%` | `200.40` |
| `Live` | `Short` | `1.46` | 642,330.00 USD | 21,110.00 USD | 0.00 USD | `+64.01%` | `14,437.60` |
| `Live` | `Short` | `1.47` | 658,750.00 USD | 16,420.00 USD | 0.00 USD | `+64.69%` | `11,182.60` |
| `Live` | `Short` | `1.50` | 658,900.00 USD | 149.75 USD | 0.00 USD | `+67.94%` | `100.00` |
| `Live` | `Short` | `1.51` | 662,920.00 USD | 4,020.00 USD | 0.00 USD | `+69.85%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 672,850.00 USD | 9,930.00 USD | 0.00 USD | `+71.64%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 673,000.00 USD | 144.34 USD | 0.00 USD | `+72.20%` | `94.00` |
| `Live` | `Short` | `1.58` | 673,280.00 USD | 285.21 USD | 0.00 USD | `+76.91%` | `180.80` |
| `Live` | `Short` | `1.59` | 674,470.00 USD | 1,180.00 USD | 0.00 USD | `+78.71%` | `743.20` |
| `Live` | `Short` | `1.60` | 674,590.00 USD | 123.81 USD | 0.00 USD | `+79.15%` | `77.50` |
| `Live` | `Short` | `1.60` | 675,720.00 USD | 1,130.00 USD | 0.00 USD | `+79.71%` | `704.60` |
| `Live` | `Short` | `1.63` | 958,320.00 USD | 282,600.00 USD | 0.00 USD | `+83.19%` | `173,000.00` |
| `Live` | `Short` | `1.65` | 979,650.00 USD | 21,330.00 USD | 0.00 USD | `+84.65%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 983,590.00 USD | 3,940.00 USD | 0.00 USD | `+85.43%` | `2,381.50` |
| `Live` | `Short` | `1.66` | 987,210.00 USD | 3,620.00 USD | 0.00 USD | `+86.11%` | `2,184.10` |
| `Live` | `Short` | `1.66` | 1,030,000.00 USD | 39,090.00 USD | 0.00 USD | `+86.33%` | `23,529.40` |
| `Live` | `Short` | `1.66` | 1,030,000.00 USD | 2,260.00 USD | 0.00 USD | `+86.67%` | `1,360.10` |
| `Live` | `Short` | `1.67` | 1,030,000.00 USD | 141.16 USD | 0.00 USD | `+87.34%` | `84.50` |
| `Live` | `Short` | `1.69` | 1,030,000.00 USD | 150.02 USD | 0.00 USD | `+89.25%` | `88.90` |
| `Live` | `Short` | `1.71` | 1,040,000.00 USD | 9,650.00 USD | 0.00 USD | `+91.60%` | `5,645.40` |
| `Live` | `Short` | `1.71` | 1,040,000.00 USD | 205.67 USD | 0.00 USD | `+92.05%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,040,000.00 USD | 900.48 USD | 0.00 USD | `+92.50%` | `524.60` |
| `Live` | `Short` | `1.73` | 1,040,000.00 USD | 494.34 USD | 0.00 USD | `+94.18%` | `285.50` |
| `Live` | `Short` | `1.73` | 1,130,000.00 USD | 85,830.00 USD | 0.00 USD | `+94.29%` | `49,543.90` |
| `Live` | `Short` | `1.73` | 1,130,000.00 USD | 226.05 USD | 0.00 USD | `+94.41%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,130,000.00 USD | 2,080.00 USD | 0.00 USD | `+95.30%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 1,150,000.00 USD | 20,050.00 USD | 0.00 USD | `+96.42%` | `11,445.40` |
| `Live` | `Short` | `1.75` | 1,160,000.00 USD | 11,350.00 USD | 0.00 USD | `+96.65%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,160,000.00 USD | 1,520.00 USD | 0.00 USD | `+96.76%` | `868.90` |
| `Live` | `Short` | `1.78` | 1,170,000.00 USD | 7,100.00 USD | 0.00 USD | `+99.12%` | `4,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,210,000.00 USD | 0.00 USD | 497.31 USD | `-70.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,210,000.00 USD | 0.00 USD | 102.75 USD | `-61.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,210,000.00 USD | 0.00 USD | 256.78 USD | `-60.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,200,000.00 USD | 0.00 USD | 428.87 USD | `-56.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,200,000.00 USD | 0.00 USD | 123.45 USD | `-53.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,200,000.00 USD | 0.00 USD | 818.15 USD | `-52.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,200,000.00 USD | 0.00 USD | 436.41 USD | `-51.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,200,000.00 USD | 0.00 USD | 876.79 USD | `-51.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,200,000.00 USD | 0.00 USD | 466.72 USD | `-49.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,200,000.00 USD | 0.00 USD | 142.95 USD | `-46.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,200,000.00 USD | 0.00 USD | 3,010.00 USD | `-43.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,200,000.00 USD | 0.00 USD | 151.74 USD | `-42.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,200,000.00 USD | 0.00 USD | 123.91 USD | `-42.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,200,000.00 USD | 0.00 USD | 219.80 USD | `-38.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,200,000.00 USD | 0.00 USD | 237,400.00 USD | `-38.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 960,790.00 USD | 0.00 USD | 276.75 USD | `-37.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 960,510.00 USD | 0.00 USD | 1,680.00 USD | `-37.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 958,830.00 USD | 0.00 USD | 853.41 USD | `-36.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 957,970.00 USD | 0.00 USD | 119.76 USD | `-34.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 957,860.00 USD | 0.00 USD | 3,520.00 USD | `-34.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 954,330.00 USD | 0.00 USD | 470.62 USD | `-33.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 953,860.00 USD | 0.00 USD | 108.39 USD | `-32.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 953,750.00 USD | 0.00 USD | 123.28 USD | `-32.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 953,630.00 USD | 0.00 USD | 488.52 USD | `-30.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 953,140.00 USD | 0.00 USD | 4,230.00 USD | `-29.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 948,910.00 USD | 0.00 USD | 242.24 USD | `-29.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 948,670.00 USD | 0.00 USD | 193.95 USD | `-27.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 948,480.00 USD | 0.00 USD | 149.22 USD | `-27.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 948,330.00 USD | 0.00 USD | 195.47 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 948,130.00 USD | 0.00 USD | 112.91 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 948,020.00 USD | 0.00 USD | 181.31 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 947,840.00 USD | 0.00 USD | 190.25 USD | `-25.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 947,650.00 USD | 0.00 USD | 153.53 USD | `-25.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 947,490.00 USD | 0.00 USD | 52,450.00 USD | `-24.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 895,050.00 USD | 0.00 USD | 536.11 USD | `-24.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 894,510.00 USD | 0.00 USD | 918.68 USD | `-23.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 893,590.00 USD | 0.00 USD | 340.75 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 893,250.00 USD | 0.00 USD | 9,270.00 USD | `-22.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 883,990.00 USD | 0.00 USD | 120.53 USD | `-22.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 883,870.00 USD | 0.00 USD | 160.71 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 883,700.00 USD | 0.00 USD | 738.08 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 882,970.00 USD | 0.00 USD | 187.61 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 882,780.00 USD | 0.00 USD | 8,500.00 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 874,280.00 USD | 0.00 USD | 89,150.00 USD | `-21.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 785,130.00 USD | 0.00 USD | 189.06 USD | `-20.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 784,940.00 USD | 0.00 USD | 5,650.00 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 779,290.00 USD | 0.00 USD | 371.68 USD | `-20.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 778,920.00 USD | 0.00 USD | 152.05 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 778,770.00 USD | 0.00 USD | 123.41 USD | `-19.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 778,640.00 USD | 0.00 USD | 745.54 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 777,900.00 USD | 0.00 USD | 1,130.00 USD | `-18.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 776,770.00 USD | 0.00 USD | 18,770.00 USD | `-17.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 758,000.00 USD | 0.00 USD | 7,970.00 USD | `-17.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 750,030.00 USD | 0.00 USD | 257.26 USD | `-17.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 749,770.00 USD | 0.00 USD | 161.72 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 749,610.00 USD | 0.00 USD | 1,590.00 USD | `-16.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 748,020.00 USD | 0.00 USD | 10,160.00 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 737,860.00 USD | 0.00 USD | 94,190.00 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 643,670.00 USD | 0.00 USD | 1,230.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 642,440.00 USD | 0.00 USD | 1,840.00 USD | `-14.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 640,600.00 USD | 0.00 USD | 804.61 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 639,800.00 USD | 0.00 USD | 590.68 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 639,210.00 USD | 0.00 USD | 635.62 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 638,570.00 USD | 0.00 USD | 191.12 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 638,380.00 USD | 0.00 USD | 273.92 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 638,100.00 USD | 0.00 USD | 125.92 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 637,980.00 USD | 0.00 USD | 1,980.00 USD | `-13.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 636,000.00 USD | 0.00 USD | 1,150.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 634,850.00 USD | 0.00 USD | 1,500.00 USD | `-13.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 633,360.00 USD | 0.00 USD | 1,860.00 USD | `-12.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 631,500.00 USD | 0.00 USD | 128.47 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 631,370.00 USD | 0.00 USD | 6,960.00 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 624,410.00 USD | 0.00 USD | 135.11 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 624,280.00 USD | 0.00 USD | 7,870.00 USD | `-11.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7885` | 616,410.00 USD | 0.00 USD | 1,090.00 USD | `-11.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 615,320.00 USD | 0.00 USD | 1,500.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7935` | 613,820.00 USD | 0.00 USD | 1,290.00 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 612,530.00 USD | 0.00 USD | 23,420.00 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 589,110.00 USD | 0.00 USD | 1,260.00 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 587,850.00 USD | 0.00 USD | 319.40 USD | `-10.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 587,530.00 USD | 0.00 USD | 4,740.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 582,800.00 USD | 0.00 USD | 1,800.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 581,000.00 USD | 0.00 USD | 144.67 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 580,850.00 USD | 0.00 USD | 1,510.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 579,340.00 USD | 0.00 USD | 50,540.00 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 528,810.00 USD | 0.00 USD | 263.25 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 528,540.00 USD | 0.00 USD | 1,250.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8095` | 527,290.00 USD | 0.00 USD | 218.32 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 527,080.00 USD | 0.00 USD | 190,180.00 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 336,890.00 USD | 0.00 USD | 174.63 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 336,720.00 USD | 0.00 USD | 1,010.00 USD | `-8.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 335,710.00 USD | 0.00 USD | 123,350.00 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 212,350.00 USD | 0.00 USD | 1,160.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 211,200.00 USD | 0.00 USD | 216.70 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 210,980.00 USD | 0.00 USD | 125.72 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 210,850.00 USD | 0.00 USD | 375.49 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 210,480.00 USD | 0.00 USD | 13,910.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 196,570.00 USD | 0.00 USD | 7,160.00 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 189,420.00 USD | 0.00 USD | 226.71 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 189,190.00 USD | 0.00 USD | 3,780.00 USD | `-7.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 185,410.00 USD | 0.00 USD | 1,420.00 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 183,990.00 USD | 0.00 USD | 325.56 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 183,660.00 USD | 0.00 USD | 666.55 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 182,990.00 USD | 0.00 USD | 577.25 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 182,420.00 USD | 0.00 USD | 3,950.00 USD | `-6.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 178,460.00 USD | 0.00 USD | 171.46 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 178,290.00 USD | 0.00 USD | 7,920.00 USD | `-6.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 170,370.00 USD | 0.00 USD | 690.30 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 169,680.00 USD | 0.00 USD | 144.54 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 169,540.00 USD | 0.00 USD | 263.43 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 169,270.00 USD | 0.00 USD | 610.23 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 168,660.00 USD | 0.00 USD | 699.65 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 167,960.00 USD | 0.00 USD | 320.31 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 167,640.00 USD | 0.00 USD | 240.52 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 167,400.00 USD | 0.00 USD | 728.04 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 166,670.00 USD | 0.00 USD | 1,020.00 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 165,660.00 USD | 0.00 USD | 510.57 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 165,150.00 USD | 0.00 USD | 212.81 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 164,930.00 USD | 0.00 USD | 1,940.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 162,990.00 USD | 0.00 USD | 12,850.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 150,130.00 USD | 0.00 USD | 481.80 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 149,650.00 USD | 0.00 USD | 1,330.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 148,330.00 USD | 0.00 USD | 25,830.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8525` | 122,500.00 USD | 0.00 USD | 7,700.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 114,800.00 USD | 0.00 USD | 470.06 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 114,330.00 USD | 0.00 USD | 6,960.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 107,370.00 USD | 0.00 USD | 5,020.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 102,340.00 USD | 0.00 USD | 105.30 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 102,240.00 USD | 0.00 USD | 8,900.00 USD | `-3.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 93,340.00 USD | 0.00 USD | 1,740.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 91,600.00 USD | 0.00 USD | 1,230.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 90,370.00 USD | 0.00 USD | 6,160.00 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 84,210.00 USD | 0.00 USD | 1,960.00 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 82,250.00 USD | 0.00 USD | 611.88 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 81,640.00 USD | 0.00 USD | 2,420.00 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 79,230.00 USD | 0.00 USD | 3,310.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 75,910.00 USD | 0.00 USD | 734.45 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 75,180.00 USD | 0.00 USD | 3,020.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 72,170.00 USD | 0.00 USD | 410.11 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 71,760.00 USD | 0.00 USD | 5,340.00 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 66,410.00 USD | 0.00 USD | 124.74 USD | `-2.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 66,290.00 USD | 0.00 USD | 5,160.00 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 61,130.00 USD | 0.00 USD | 1,500.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 59,630.00 USD | 0.00 USD | 3,450.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 56,180.00 USD | 0.00 USD | 866.37 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 55,310.00 USD | 0.00 USD | 1,360.00 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 53,950.00 USD | 0.00 USD | 3,050.00 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 50,900.00 USD | 0.00 USD | 9,070.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 41,840.00 USD | 0.00 USD | 1,380.00 USD | `-1.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 40,450.00 USD | 0.00 USD | 2,000.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 38,450.00 USD | 0.00 USD | 4,580.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 33,870.00 USD | 0.00 USD | 4,070.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 29,800.00 USD | 0.00 USD | 563.65 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 29,240.00 USD | 0.00 USD | 425.94 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8855` | 28,810.00 USD | 0.00 USD | 4,210.00 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 24,590.00 USD | 0.00 USD | 3,600.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 21,000.00 USD | 0.00 USD | 235.54 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8885` | 20,760.00 USD | 0.00 USD | 11,360.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 9,400.00 USD | 0.00 USD | 8,780.00 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8905` | 622.27 USD | 0.00 USD | 152.36 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 469.91 USD | 0.00 USD | 469.91 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 10,610.00 USD | 10,610.00 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 10,890.00 USD | 277.07 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 10,990.00 USD | 100.09 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 14,380.00 USD | 3,390.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 14,670.00 USD | 289.12 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 32,880.00 USD | 18,210.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 33,770.00 USD | 889.43 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 62,730.00 USD | 28,960.00 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 66,290.00 USD | 3,560.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 68,340.00 USD | 2,050.00 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 69,270.00 USD | 926.06 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 69,460.00 USD | 188.92 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 72,410.00 USD | 2,950.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 74,410.00 USD | 1,990.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 74,690.00 USD | 283.01 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 74,940.00 USD | 250.83 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 76,030.00 USD | 1,090.00 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 77,560.00 USD | 1,520.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 78,490.00 USD | 933.08 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 78,750.00 USD | 260.23 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 81,640.00 USD | 2,890.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 84,660.00 USD | 3,020.00 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 87,840.00 USD | 3,180.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 97,560.00 USD | 9,730.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 97,870.00 USD | 309.14 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 101,770.00 USD | 3,900.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 103,750.00 USD | 1,970.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 103,860.00 USD | 116.59 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 104,050.00 USD | 184.10 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 256,010.00 USD | 151,960.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 261,080.00 USD | 5,070.00 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 261,580.00 USD | 495.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 262,980.00 USD | 1,400.00 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 268,000.00 USD | 5,030.00 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 270,210.00 USD | 2,200.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 270,500.00 USD | 287.62 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 270,690.00 USD | 199.16 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 271,780.00 USD | 1,090.00 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 272,230.00 USD | 448.69 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 272,350.00 USD | 120.16 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 275,780.00 USD | 3,430.00 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 276,350.00 USD | 568.87 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 276,650.00 USD | 292.78 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 277,170.00 USD | 523.79 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 277,870.00 USD | 701.16 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 277,980.00 USD | 104.53 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 331,040.00 USD | 53,060.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 334,940.00 USD | 3,910.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 343,900.00 USD | 8,960.00 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 344,430.00 USD | 529.50 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 345,100.00 USD | 667.86 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 346,800.00 USD | 1,700.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 347,590.00 USD | 789.04 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 356,160.00 USD | 8,560.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 357,210.00 USD | 1,050.00 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 358,060.00 USD | 848.20 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 377,180.00 USD | 19,120.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 378,340.00 USD | 1,160.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 382,560.00 USD | 4,220.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 382,720.00 USD | 159.19 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 392,630.00 USD | 9,910.00 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 395,780.00 USD | 3,150.00 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 397,220.00 USD | 1,440.00 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 400,100.00 USD | 2,890.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 401,230.00 USD | 1,130.00 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 401,360.00 USD | 121.54 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 402,580.00 USD | 1,230.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 455,090.00 USD | 52,510.00 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 455,250.00 USD | 161.82 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 474,650.00 USD | 19,400.00 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 474,910.00 USD | 259.86 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 476,250.00 USD | 1,340.00 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 476,730.00 USD | 476.57 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 477,110.00 USD | 386.60 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 480,270.00 USD | 3,160.00 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 481,270.00 USD | 993.78 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 481,480.00 USD | 212.90 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 481,650.00 USD | 165.86 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 481,770.00 USD | 125.61 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 482,210.00 USD | 441.51 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 492,400.00 USD | 10,190.00 USD | 0.00 USD | `+9.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 492,650.00 USD | 253.14 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 496,860.00 USD | 4,200.00 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 497,030.00 USD | 176.73 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 497,550.00 USD | 513.32 USD | 0.00 USD | `+9.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 532,910.00 USD | 35,360.00 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 564,870.00 USD | 31,960.00 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 569,660.00 USD | 4,800.00 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 570,220.00 USD | 558.35 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 571,290.00 USD | 1,060.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 572,470.00 USD | 1,180.00 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 572,960.00 USD | 490.99 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 573,350.00 USD | 395.21 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 574,340.00 USD | 991.50 USD | 0.00 USD | `+11.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 584,680.00 USD | 10,340.00 USD | 0.00 USD | `+11.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 585,090.00 USD | 409.52 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 585,370.00 USD | 284.92 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 585,720.00 USD | 350.37 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 585,850.00 USD | 124.04 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 587,400.00 USD | 1,560.00 USD | 0.00 USD | `+12.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 589,580.00 USD | 2,180.00 USD | 0.00 USD | `+12.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 590,360.00 USD | 778.64 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 590,720.00 USD | 363.87 USD | 0.00 USD | `+12.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 591,310.00 USD | 589.52 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 591,420.00 USD | 110.62 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 601,510.00 USD | 10,090.00 USD | 0.00 USD | `+13.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 606,930.00 USD | 5,420.00 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 609,460.00 USD | 2,520.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 609,700.00 USD | 248.49 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 618,850.00 USD | 9,150.00 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 619,580.00 USD | 722.63 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 619,890.00 USD | 312.07 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 620,060.00 USD | 171.24 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 620,620.00 USD | 561.11 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 620,870.00 USD | 249.30 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 622,340.00 USD | 1,470.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 622,770.00 USD | 432.18 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 622,910.00 USD | 137.88 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 625,250.00 USD | 2,340.00 USD | 0.00 USD | `+15.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 625,940.00 USD | 694.72 USD | 0.00 USD | `+15.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 626,100.00 USD | 160.60 USD | 0.00 USD | `+16.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 632,660.00 USD | 6,560.00 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 635,580.00 USD | 2,920.00 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 635,800.00 USD | 224.56 USD | 0.00 USD | `+17.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 639,380.00 USD | 3,570.00 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 639,810.00 USD | 432.19 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 641,660.00 USD | 1,850.00 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,290,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+18.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,290,000.00 USD | 5,390.00 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,290,000.00 USD | 285.32 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,290,000.00 USD | 1,130.00 USD | 0.00 USD | `+18.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,290,000.00 USD | 1,240.00 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,290,000.00 USD | 278.06 USD | 0.00 USD | `+19.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,290,000.00 USD | 309.00 USD | 0.00 USD | `+19.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,290,000.00 USD | 228.98 USD | 0.00 USD | `+19.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,290,000.00 USD | 272.12 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,290,000.00 USD | 117.12 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,430,000.00 USD | 140,120.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,440,000.00 USD | 530.01 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,440,000.00 USD | 128.23 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,540,000.00 USD | 108,190.00 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,550,000.00 USD | 3,430.00 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,550,000.00 USD | 550.49 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,550,000.00 USD | 5,810.00 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,550,000.00 USD | 1,520.00 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,560,000.00 USD | 5,570.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,560,000.00 USD | 1,290.00 USD | 0.00 USD | `+22.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,560,000.00 USD | 294.81 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,560,000.00 USD | 183.11 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,560,000.00 USD | 123.13 USD | 0.00 USD | `+22.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,560,000.00 USD | 494.98 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,560,000.00 USD | 613.52 USD | 0.00 USD | `+23.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,680,000.00 USD | 115,100.00 USD | 0.00 USD | `+23.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,680,000.00 USD | 409.76 USD | 0.00 USD | `+23.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,680,000.00 USD | 162.77 USD | 0.00 USD | `+23.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,680,000.00 USD | 959.70 USD | 0.00 USD | `+23.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,680,000.00 USD | 160.18 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,680,000.00 USD | 669.85 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,680,000.00 USD | 293.61 USD | 0.00 USD | `+25.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,790,000.00 USD | 112,050.00 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,790,000.00 USD | 462.47 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,800,000.00 USD | 2,180.00 USD | 0.00 USD | `+26.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,800,000.00 USD | 273.34 USD | 0.00 USD | `+26.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,800,000.00 USD | 119.49 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,820,000.00 USD | 20,740.00 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,820,000.00 USD | 468.47 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,820,000.00 USD | 1,430.00 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,820,000.00 USD | 338.50 USD | 0.00 USD | `+28.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,820,000.00 USD | 2,640.00 USD | 0.00 USD | `+29.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,820,000.00 USD | 1,230.00 USD | 0.00 USD | `+29.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,830,000.00 USD | 2,450.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,830,000.00 USD | 1,250.00 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,830,000.00 USD | 143.67 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,830,000.00 USD | 989.81 USD | 0.00 USD | `+30.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,830,000.00 USD | 304.33 USD | 0.00 USD | `+31.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,830,000.00 USD | 255.14 USD | 0.00 USD | `+31.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,830,000.00 USD | 241.65 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,830,000.00 USD | 239.97 USD | 0.00 USD | `+32.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,830,000.00 USD | 2,470.00 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,830,000.00 USD | 3,060.00 USD | 0.00 USD | `+32.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,140,000.00 USD | 310,250.00 USD | 0.00 USD | `+33.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,140,000.00 USD | 309.53 USD | 0.00 USD | `+33.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,150,000.00 USD | 159.09 USD | 0.00 USD | `+33.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,150,000.00 USD | 146.21 USD | 0.00 USD | `+34.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,160,000.00 USD | 18,560.00 USD | 0.00 USD | `+34.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,160,000.00 USD | 933.81 USD | 0.00 USD | `+34.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,170,000.00 USD | 658.86 USD | 0.00 USD | `+35.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,380,000.00 USD | 213,390.00 USD | 0.00 USD | `+35.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,380,000.00 USD | 560.05 USD | 0.00 USD | `+35.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,380,000.00 USD | 1,050.00 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,380,000.00 USD | 509.71 USD | 0.00 USD | `+37.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,380,000.00 USD | 162.15 USD | 0.00 USD | `+37.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,380,000.00 USD | 187.04 USD | 0.00 USD | `+38.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,380,000.00 USD | 542.12 USD | 0.00 USD | `+38.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,410,000.00 USD | 23,740.00 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,410,000.00 USD | 2,010.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,410,000.00 USD | 345.91 USD | 0.00 USD | `+38.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,410,000.00 USD | 104.79 USD | 0.00 USD | `+39.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,410,000.00 USD | 100.04 USD | 0.00 USD | `+40.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,410,000.00 USD | 517.52 USD | 0.00 USD | `+40.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,410,000.00 USD | 152.29 USD | 0.00 USD | `+40.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,410,000.00 USD | 1,480.00 USD | 0.00 USD | `+41.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,410,000.00 USD | 1,010.00 USD | 0.00 USD | `+41.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,410,000.00 USD | 2,780.00 USD | 0.00 USD | `+42.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,410,000.00 USD | 340.38 USD | 0.00 USD | `+42.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,420,000.00 USD | 903.22 USD | 0.00 USD | `+42.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,420,000.00 USD | 475.01 USD | 0.00 USD | `+42.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,460,000.00 USD | 41,160.00 USD | 0.00 USD | `+43.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,470,000.00 USD | 12,840.00 USD | 0.00 USD | `+43.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,660,000.00 USD | 194,770.00 USD | 0.00 USD | `+44.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,680,000.00 USD | 12,890.00 USD | 0.00 USD | `+44.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,690,000.00 USD | 8,820.00 USD | 0.00 USD | `+44.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,690,000.00 USD | 466.95 USD | 0.00 USD | `+45.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,690,000.00 USD | 613.59 USD | 0.00 USD | `+45.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,690,000.00 USD | 1,420.00 USD | 0.00 USD | `+45.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,700,000.00 USD | 13,000.00 USD | 0.00 USD | `+45.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,700,000.00 USD | 284.42 USD | 0.00 USD | `+45.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,720,000.00 USD | 22,810.00 USD | 0.00 USD | `+48.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,730,000.00 USD | 640.82 USD | 0.00 USD | `+49.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,730,000.00 USD | 134.75 USD | 0.00 USD | `+49.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,740,000.00 USD | 13,400.00 USD | 0.00 USD | `+50.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,740,000.00 USD | 541.96 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,750,000.00 USD | 13,490.00 USD | 0.00 USD | `+51.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,760,000.00 USD | 11,580.00 USD | 0.00 USD | `+51.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,770,000.00 USD | 3,610.00 USD | 0.00 USD | `+52.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,770,000.00 USD | 1,500.00 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,780,000.00 USD | 15,000.00 USD | 0.00 USD | `+53.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,790,000.00 USD | 9,030.00 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,790,000.00 USD | 405.86 USD | 0.00 USD | `+55.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,810,000.00 USD | 13,890.00 USD | 0.00 USD | `+55.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,820,000.00 USD | 14,000.00 USD | 0.00 USD | `+56.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,830,000.00 USD | 12,560.00 USD | 0.00 USD | `+57.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,870,000.00 USD | 32,860.00 USD | 0.00 USD | `+57.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,870,000.00 USD | 102.40 USD | 0.00 USD | `+58.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,870,000.00 USD | 106.64 USD | 0.00 USD | `+58.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,870,000.00 USD | 1,430.00 USD | 0.00 USD | `+58.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,870,000.00 USD | 2,810.00 USD | 0.00 USD | `+58.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,880,000.00 USD | 8,420.00 USD | 0.00 USD | `+59.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 3,880,000.00 USD | 1,410.00 USD | 0.00 USD | `+59.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,880,000.00 USD | 145.37 USD | 0.00 USD | `+61.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,880,000.00 USD | 1,390.00 USD | 0.00 USD | `+61.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,900,000.00 USD | 14,390.00 USD | 0.00 USD | `+61.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,900,000.00 USD | 7,000.00 USD | 0.00 USD | `+62.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,920,000.00 USD | 14,490.00 USD | 0.00 USD | `+62.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,920,000.00 USD | 1,370.00 USD | 0.00 USD | `+62.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,920,000.00 USD | 1,340.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,920,000.00 USD | 342.08 USD | 0.00 USD | `+65.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 3,920,000.00 USD | 1,330.00 USD | 0.00 USD | `+65.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,940,000.00 USD | 14,890.00 USD | 0.00 USD | `+67.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,950,000.00 USD | 9,580.00 USD | 0.00 USD | `+67.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,960,000.00 USD | 14,980.00 USD | 0.00 USD | `+68.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,980,000.00 USD | 20,120.00 USD | 0.00 USD | `+68.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,980,000.00 USD | 1,180.00 USD | 0.00 USD | `+68.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,990,000.00 USD | 1,260.00 USD | 0.00 USD | `+70.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 3,990,000.00 USD | 2,150.00 USD | 0.00 USD | `+72.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 3,990,000.00 USD | 158.76 USD | 0.00 USD | `+74.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 3,990,000.00 USD | 574.53 USD | 0.00 USD | `+78.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 3,990,000.00 USD | 391.32 USD | 0.00 USD | `+79.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 3,990,000.00 USD | 1,160.00 USD | 0.00 USD | `+81.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,990,000.00 USD | 1,140.00 USD | 0.00 USD | `+83.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,990,000.00 USD | 1,970.00 USD | 0.00 USD | `+83.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 3,990,000.00 USD | 281.45 USD | 0.00 USD | `+86.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,000,000.00 USD | 2,070.00 USD | 0.00 USD | `+86.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,010,000.00 USD | 13,060.00 USD | 0.00 USD | `+90.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 4,010,000.00 USD | 1,390.00 USD | 0.00 USD | `+95.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,010,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,010,000.00 USD | 320.52 USD | 0.00 USD | `+96.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 4,010,000.00 USD | 1,710.00 USD | 0.00 USD | `+98.11%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7360` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 79,750.00 USD | 28,310.00 USD | 71,200.00 USD |
| `7D` | `0.7380` | 10,200,000.00 USD | 0.00 USD | 10,200,000.00 USD | 23,980.00 USD | 22,880.00 USD | 17,840.00 USD |
| `7D` | `0.7400` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 17,280.00 USD | 13,180.00 USD | 24,590.00 USD |
| `7D` | `0.7420` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 31,920.00 USD | 8,580.00 USD | 38,040.00 USD |
| `7D` | `0.7440` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 65,280.00 USD | 21,190.00 USD | 40,240.00 USD |
| `7D` | `0.7460` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 22,100.00 USD | 24,720.00 USD | 42,210.00 USD |
| `7D` | `0.7480` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 11,220.00 USD | 6,300.00 USD | 738.49 USD |
| `7D` | `0.7500` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 25,600.00 USD | 12,880.00 USD | 11,320.00 USD |
| `7D` | `0.7520` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,130.00 USD | 10,160.00 USD | 22,100.00 USD |
| `7D` | `0.7540` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 9,690.00 USD | 4,770.00 USD | 14,120.00 USD |
| `7D` | `0.7560` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 2,690.00 USD | 17,670.00 USD | 7,530.00 USD |
| `7D` | `0.7580` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 19,590.00 USD | 20,390.00 USD | 358.66 USD |
| `7D` | `0.7600` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 8,420.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `0.7620` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 40,420.00 USD | 16,580.00 USD | 1,090.00 USD |
| `7D` | `0.7640` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 556.58 USD | 118.70 USD | 97.65 USD |
| `7D` | `0.7660` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 1,280.00 USD | 23,260.00 USD | 32,550.00 USD |
| `7D` | `0.7680` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 182.28 USD | 3,780.00 USD | 0.00 USD |
| `7D` | `0.7700` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD |
| `7D` | `0.7720` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7780` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD |
| `7D` | `0.7800` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 0.00 USD | 2,640.00 USD | 1,290.00 USD |
| `7D` | `0.7820` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 0.00 USD | 1,440.00 USD | 10,680.00 USD |
| `7D` | `0.7840` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 6,050.00 USD | 2,680.00 USD | 4,540.00 USD |
| `7D` | `0.7860` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 1,740.00 USD | 45,550.00 USD | 13,160.00 USD |
| `1D` | `0.7900` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 37,240.00 USD | 29,720.00 USD | 17,590.00 USD |
| `7D` | `0.7900` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 6,610.00 USD | 28,080.00 USD | 1,280.00 USD |
| `1D` | `0.7920` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 10,370.00 USD | 16,170.00 USD | 37,070.00 USD |
| `7D` | `0.7920` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 0.00 USD | 23,790.00 USD | 67,960.00 USD |
| `1D` | `0.7940` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 21,090.00 USD | 20,690.00 USD | 21,700.00 USD |
| `7D` | `0.7940` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 0.00 USD | 886.60 USD | 4,720.00 USD |
| `1D` | `0.7960` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 4,910.00 USD | 6,390.00 USD | 40,790.00 USD |
| `7D` | `0.7960` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 2,210.00 USD | 19,210.00 USD | 82,920.00 USD |
| `1D` | `0.7980` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 25,120.00 USD | 11,770.00 USD | 37,160.00 USD |
| `7D` | `0.7980` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 35,260.00 USD | 3,570.00 USD | 66,610.00 USD |
| `1D` | `0.8000` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 32,430.00 USD | 31,530.00 USD | 35,100.00 USD |
| `7D` | `0.8000` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 41,450.00 USD | 16,710.00 USD | 0.00 USD |
| `1D` | `0.8020` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 1,730.00 USD | 251.75 USD | 724.11 USD |
| `7D` | `0.8020` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,910.00 USD |
| `1D` | `0.8040` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 37,430.00 USD | 24,190.00 USD | 21,590.00 USD |
| `7D` | `0.8040` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD |
| `1D` | `0.8060` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 50,970.00 USD | 15,300.00 USD | 69,040.00 USD |
| `7D` | `0.8060` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 10,860.00 USD | 737.70 USD | 0.00 USD |
| `1D` | `0.8080` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 3,230.00 USD | 19,130.00 USD | 2,460.00 USD |
| `7D` | `0.8080` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 5,030.00 USD | 11,280.00 USD | 8,230.00 USD |
| `1D` | `0.8100` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 2,420.00 USD | 11,070.00 USD | 2,110.00 USD |
| `7D` | `0.8100` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 4,310.00 USD | 9,850.00 USD | 104.33 USD |
| `1D` | `0.8120` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 15,380.00 USD | 3,270.00 USD | 23,770.00 USD |
| `7D` | `0.8120` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 73,000.00 USD | 9,210.00 USD | 38,210.00 USD |
| `1D` | `0.8140` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 29,630.00 USD | 9,710.00 USD | 23,410.00 USD |
| `7D` | `0.8140` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 55,190.00 USD | 31,920.00 USD | 78,170.00 USD |
| `1D` | `0.8160` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 116,280.00 USD | 24,170.00 USD | 172,870.00 USD |
| `7D` | `0.8160` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 186,980.00 USD | 49,790.00 USD | 146,640.00 USD |
| `1D` | `0.8180` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 66,880.00 USD | 10,440.00 USD | 36,760.00 USD |
| `7D` | `0.8180` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 82,600.00 USD | 41,370.00 USD | 42,780.00 USD |
| `1D` | `0.8200` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 112,400.00 USD | 8,800.00 USD | 83,680.00 USD |
| `7D` | `0.8200` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 205,920.00 USD | 48,700.00 USD | 103,530.00 USD |
| `1D` | `0.8220` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 86,610.00 USD | 89,600.00 USD | 85,640.00 USD |
| `7D` | `0.8220` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 110,800.00 USD | 73,170.00 USD | 169,050.00 USD |
| `1D` | `0.8240` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 10,570.00 USD | 5,990.00 USD | 143,620.00 USD |
| `7D` | `0.8240` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 102,030.00 USD | 42,270.00 USD | 90,060.00 USD |
| `1D` | `0.8260` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 43,870.00 USD | 11,180.00 USD | 25,460.00 USD |
| `7D` | `0.8260` | 7,050,000.00 USD | 0.00 USD | 7,050,000.00 USD | 194,340.00 USD | 32,880.00 USD | 111,300.00 USD |
| `1D` | `0.8280` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 41,020.00 USD | 22,610.00 USD | 8,410.00 USD |
| `7D` | `0.8280` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 118,780.00 USD | 44,400.00 USD | 88,410.00 USD |
| `1D` | `0.8300` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 27,690.00 USD | 14,510.00 USD | 53,530.00 USD |
| `7D` | `0.8300` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 33,770.00 USD | 45,100.00 USD | 44,750.00 USD |
| `1D` | `0.8320` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 3,000.00 USD | 37,880.00 USD | 46,200.00 USD |
| `7D` | `0.8320` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 90,830.00 USD | 77,110.00 USD | 150,260.00 USD |
| `1D` | `0.8340` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 149,940.00 USD | 40,900.00 USD | 105,220.00 USD |
| `7D` | `0.8340` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 114,580.00 USD | 56,360.00 USD | 180,740.00 USD |
| `1D` | `0.8360` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 58,860.00 USD | 13,740.00 USD | 1,470.00 USD |
| `7D` | `0.8360` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 175,960.00 USD | 28,000.00 USD | 92,530.00 USD |
| `1D` | `0.8380` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 51,030.00 USD | 66,750.00 USD | 144,000.00 USD |
| `7D` | `0.8380` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 65,710.00 USD | 219,730.00 USD | 223,070.00 USD |
| `1D` | `0.8400` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 38,430.00 USD | 9,770.00 USD | 55,270.00 USD |
| `7D` | `0.8400` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 82,000.00 USD | 54,600.00 USD | 58,420.00 USD |
| `1D` | `0.8420` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 89,320.00 USD | 63,630.00 USD | 55,700.00 USD |
| `7D` | `0.8420` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 96,530.00 USD | 66,440.00 USD | 12,640.00 USD |
| `1D` | `0.8440` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 67,620.00 USD | 63,050.00 USD | 21,810.00 USD |
| `7D` | `0.8440` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 28,900.00 USD | 111,080.00 USD | 0.00 USD |
| `1D` | `0.8460` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 22,250.00 USD | 93,240.00 USD | 38,910.00 USD |
| `7D` | `0.8460` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 52,800.00 USD | 57,770.00 USD | 1,790.00 USD |
| `1D` | `0.8480` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 51,620.00 USD | 62,920.00 USD | 70,340.00 USD |
| `7D` | `0.8480` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 73,880.00 USD | 46,880.00 USD | 84,570.00 USD |
| `1D` | `0.8500` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 72,370.00 USD | 88,390.00 USD | 167,200.00 USD |
| `7D` | `0.8500` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 82,620.00 USD | 58,490.00 USD | 53,090.00 USD |
| `1D` | `0.8520` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 89,760.00 USD | 198,220.00 USD | 133,900.00 USD |
| `7D` | `0.8520` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 77,320.00 USD | 53,520.00 USD | 52,310.00 USD |
| `1D` | `0.8540` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,150.00 USD |
| `7D` | `0.8540` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 277,690.00 USD | 36,220.00 USD | 3,040.00 USD |
| `1D` | `0.8560` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 1,920.00 USD | 24,460.00 USD | 46,520.00 USD |
| `7D` | `0.8560` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 87,380.00 USD | 55,310.00 USD | 36,270.00 USD |
| `1D` | `0.8580` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 32,900.00 USD | 66,810.00 USD | 26,530.00 USD |
| `7D` | `0.8580` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 146,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8600` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 89,450.00 USD | 30,490.00 USD | 23,650.00 USD |
| `7D` | `0.8600` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 38,890.00 USD | 164,470.00 USD | 20,680.00 USD |
| `1D` | `0.8620` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 46,800.00 USD | 25,800.00 USD | 26,450.00 USD |
| `7D` | `0.8620` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 25,100.00 USD | 145,110.00 USD | 393,070.00 USD |
| `1D` | `0.8640` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 77,240.00 USD | 149,990.00 USD | 107,300.00 USD |
| `7D` | `0.8640` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 83,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8660` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 133,260.00 USD | 27,450.00 USD | 167,030.00 USD |
| `7D` | `0.8660` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 294,020.00 USD | 93,770.00 USD | 678,840.00 USD |
| `1D` | `0.8680` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 106,760.00 USD | 11,860.00 USD | 125,530.00 USD |
| `7D` | `0.8680` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 213,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8700` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 90,040.00 USD | 50,550.00 USD |
| `7D` | `0.8700` | 863,580.00 USD | 0.00 USD | 863,580.00 USD | 0.00 USD | 34,600.00 USD | 104,620.00 USD |
| `1D` | `0.8720` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 182,270.00 USD | 62,100.00 USD | 172,900.00 USD |
| `7D` | `0.8720` | 724,360.00 USD | 0.00 USD | 724,360.00 USD | 207,250.00 USD | 72,450.00 USD | 87,530.00 USD |
| `1D` | `0.8740` | 838,640.00 USD | 0.00 USD | 838,640.00 USD | 55,600.00 USD | 0.00 USD | 27,510.00 USD |
| `7D` | `0.8740` | 357,130.00 USD | 0.00 USD | 357,130.00 USD | 9,520.00 USD | 0.00 USD | 66,380.00 USD |
| `1D` | `0.8760` | 755,530.00 USD | 0.00 USD | 755,530.00 USD | 0.00 USD | 0.00 USD | 142,570.00 USD |
| `7D` | `0.8760` | 281,230.00 USD | 0.00 USD | 281,230.00 USD | 16,700.00 USD | 0.00 USD | 186,450.00 USD |
| `1D` | `0.8780` | 612,950.00 USD | 0.00 USD | 612,950.00 USD | 107,610.00 USD | 20,280.00 USD | 67,920.00 USD |
| `1D` | `0.8800` | 417,130.00 USD | 0.00 USD | 417,130.00 USD | 4,760.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `0.8800` | 78,080.00 USD | 0.00 USD | 78,080.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8820` | 411,360.00 USD | 0.00 USD | 411,360.00 USD | 37,200.00 USD | 24,670.00 USD | 113,540.00 USD |
| `7D` | `0.8820` | 57,770.00 USD | 0.00 USD | 57,770.00 USD | 0.00 USD | 3,570.00 USD | 5,630.00 USD |
| `1D` | `0.8840` | 235,970.00 USD | 0.00 USD | 235,970.00 USD | 30,450.00 USD | 2,260.00 USD | 26,040.00 USD |
| `7D` | `0.8840` | 48,570.00 USD | 0.00 USD | 48,570.00 USD | 0.00 USD | 35,900.00 USD | 0.00 USD |
| `1D` | `0.8860` | 177,210.00 USD | 0.00 USD | 177,210.00 USD | 0.00 USD | 0.00 USD | 1,330.00 USD |
| `1D` | `0.8880` | 175,880.00 USD | 0.00 USD | 175,880.00 USD | 122,200.00 USD | 1,400.00 USD | 560.38 USD |
| `7D` | `0.8880` | 12,670.00 USD | 0.00 USD | 12,670.00 USD | 0.00 USD | 3,860.00 USD | 0.00 USD |
| `1D` | `0.8900` | 51,720.00 USD | 0.00 USD | 51,720.00 USD | 2,860.00 USD | 0.00 USD | 48,860.00 USD |
| `7D` | `0.8900` | 8,820.00 USD | 0.00 USD | 8,820.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8910` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8910` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8920` | 149,100.00 USD | 149,100.00 USD | 0.00 USD | 137,750.00 USD | 0.00 USD | 11,360.00 USD |
| `7D` | `0.8920` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8940` | 390,250.00 USD | 390,250.00 USD | 0.00 USD | 200,000.00 USD | 40,390.00 USD | 754.18 USD |
| `7D` | `0.8940` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 6,300.00 USD |
| `1D` | `0.8960` | 496,860.00 USD | 496,860.00 USD | 0.00 USD | 2,890.00 USD | 101,620.00 USD | 2,090.00 USD |
| `7D` | `0.8960` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 610,810.00 USD | 107,280.00 USD | 4,220.00 USD |
| `1D` | `0.8980` | 917,790.00 USD | 917,790.00 USD | 0.00 USD | 74,000.00 USD | 95,760.00 USD | 251,170.00 USD |
| `7D` | `0.8980` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 626,180.00 USD | 118,950.00 USD | 339,780.00 USD |
| `1D` | `0.9000` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 237,980.00 USD | 121,990.00 USD | 0.00 USD |
| `7D` | `0.9000` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 198,040.00 USD | 16,730.00 USD | 514.60 USD |
| `1D` | `0.9020` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 7,290.00 USD | 138,990.00 USD | 189.28 USD |
| `7D` | `0.9020` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 85,610.00 USD | 192,140.00 USD | 477,260.00 USD |
| `1D` | `0.9040` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 157,060.00 USD | 223,010.00 USD | 1,030.00 USD |
| `7D` | `0.9040` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 223,750.00 USD | 2,890.00 USD | 223,490.00 USD |
| `1D` | `0.9060` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 258,520.00 USD | 176,840.00 USD | 202,950.00 USD |
| `7D` | `0.9060` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 286,790.00 USD | 34,600.00 USD | 104,620.00 USD |
| `1D` | `0.9080` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 249,000.00 USD | 147,110.00 USD | 133,230.00 USD |
| `7D` | `0.9080` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 389,350.00 USD | 259,410.00 USD | 224,560.00 USD |
| `1D` | `0.9100` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 99,190.00 USD | 39,940.00 USD | 31,420.00 USD |
| `7D` | `0.9100` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 123,910.00 USD | 6,820.00 USD | 68,960.00 USD |
| `1D` | `0.9120` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 100,870.00 USD | 97,820.00 USD | 90,810.00 USD |
| `7D` | `0.9120` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 135,210.00 USD | 134,750.00 USD | 0.00 USD |
| `1D` | `0.9140` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 208,890.00 USD | 69,780.00 USD | 209,100.00 USD |
| `7D` | `0.9140` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 143,540.00 USD | 83,230.00 USD | 0.00 USD |
| `1D` | `0.9160` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 130,780.00 USD | 169,050.00 USD | 223,880.00 USD |
| `7D` | `0.9160` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 212,270.00 USD | 84,510.00 USD | 170,540.00 USD |
| `1D` | `0.9180` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 90,690.00 USD | 76,080.00 USD | 110,630.00 USD |
| `7D` | `0.9180` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 38,590.00 USD | 48,930.00 USD | 187,840.00 USD |
| `1D` | `0.9200` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 104,190.00 USD | 22,510.00 USD | 141,320.00 USD |
| `7D` | `0.9200` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 445,890.00 USD | 32,570.00 USD | 114,170.00 USD |
| `1D` | `0.9220` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 203,870.00 USD | 94,010.00 USD | 261,190.00 USD |
| `7D` | `0.9220` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 6,470.00 USD | 66,370.00 USD | 320,750.00 USD |
| `1D` | `0.9240` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 240,420.00 USD | 110,560.00 USD | 265,860.00 USD |
| `7D` | `0.9240` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 111,800.00 USD | 62,860.00 USD | 260,630.00 USD |
| `1D` | `0.9260` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 135,010.00 USD | 117,320.00 USD | 106,460.00 USD |
| `7D` | `0.9260` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 209,940.00 USD | 81,200.00 USD | 89,770.00 USD |
| `1D` | `0.9280` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 5,090.00 USD | 67,540.00 USD | 74,750.00 USD |
| `7D` | `0.9280` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 114,570.00 USD | 5,660.00 USD | 33,190.00 USD |
| `1D` | `0.9300` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 43,730.00 USD | 61,500.00 USD | 106,700.00 USD |
| `7D` | `0.9300` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 186,110.00 USD | 98,550.00 USD | 169,910.00 USD |
| `1D` | `0.9320` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 189,960.00 USD | 36,420.00 USD | 59,010.00 USD |
| `7D` | `0.9320` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 4,410.00 USD | 53,880.00 USD | 63,730.00 USD |
| `1D` | `0.9340` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 5,250.00 USD | 35,920.00 USD | 0.00 USD |
| `7D` | `0.9340` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 50,160.00 USD | 78,870.00 USD | 0.00 USD |
| `1D` | `0.9360` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 48,720.00 USD | 29,540.00 USD | 67,940.00 USD |
| `7D` | `0.9360` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 131,450.00 USD | 3,160.00 USD | 3,340.00 USD |
| `1D` | `0.9380` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 118,620.00 USD | 63,250.00 USD | 245,730.00 USD |
| `7D` | `0.9380` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 168,030.00 USD | 5,150.00 USD | 183,370.00 USD |
| `1D` | `0.9400` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 59,870.00 USD | 3,680.00 USD | 89,860.00 USD |
| `7D` | `0.9400` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 170,760.00 USD | 37,790.00 USD | 127,800.00 USD |
| `1D` | `0.9420` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 17,290.00 USD | 14,410.00 USD | 24,380.00 USD |
| `7D` | `0.9420` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 4,970.00 USD | 29,990.00 USD | 33,660.00 USD |
| `1D` | `0.9440` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 6,330.00 USD | 38,560.00 USD | 58,010.00 USD |
| `7D` | `0.9440` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 3,360.00 USD | 217,840.00 USD | 2,300.00 USD |
| `1D` | `0.9460` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 61,800.00 USD | 32,120.00 USD | 152,830.00 USD |
| `7D` | `0.9460` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 69,070.00 USD | 128,340.00 USD |
| `1D` | `0.9480` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 91,790.00 USD | 73,040.00 USD | 56,220.00 USD |
| `7D` | `0.9480` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 0.00 USD | 78,160.00 USD | 291,990.00 USD |
| `1D` | `0.9500` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 26,310.00 USD | 36,450.00 USD | 70,360.00 USD |
| `7D` | `0.9500` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 2,840.00 USD | 30,430.00 USD | 371,330.00 USD |
| `1D` | `0.9520` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 52,590.00 USD | 28,420.00 USD | 212,340.00 USD |
| `7D` | `0.9520` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 87,720.00 USD | 360,980.00 USD |
| `1D` | `0.9540` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 59,860.00 USD | 51,440.00 USD | 98,250.00 USD |
| `7D` | `0.9540` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 13,570.00 USD | 3,670.00 USD | 61,600.00 USD |
| `1D` | `0.9560` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 40,290.00 USD | 27,000.00 USD | 48,260.00 USD |
| `7D` | `0.9560` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 72,330.00 USD | 3,500.00 USD | 1,880.00 USD |
| `1D` | `0.9580` | 9,400,000.00 USD | 9,400,000.00 USD | 0.00 USD | 27,440.00 USD | 45,440.00 USD | 12,820.00 USD |
| `7D` | `0.9580` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 846,080.00 USD | 1,220.00 USD | 896.09 USD |
| `1D` | `0.9600` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 103,500.00 USD | 50,930.00 USD | 78,080.00 USD |
| `7D` | `0.9600` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 358,610.00 USD | 118,450.00 USD | 132,780.00 USD |
| `1D` | `0.9620` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 267,480.00 USD | 66,570.00 USD | 176,710.00 USD |
| `7D` | `0.9620` | 17,110,000.00 USD | 17,110,000.00 USD | 0.00 USD | 715,790.00 USD | 231,300.00 USD | 594,960.00 USD |
| `1D` | `0.9640` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 238,280.00 USD | 68,410.00 USD | 102,420.00 USD |
| `7D` | `0.9640` | 18,680,000.00 USD | 18,680,000.00 USD | 0.00 USD | 693,720.00 USD | 366,520.00 USD | 508,630.00 USD |
| `1D` | `0.9660` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 155,090.00 USD | 129,450.00 USD | 72,340.00 USD |
| `7D` | `0.9660` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 962,420.00 USD | 245,250.00 USD | 520,080.00 USD |
| `1D` | `0.9680` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 175,350.00 USD | 67,790.00 USD | 303,820.00 USD |
| `7D` | `0.9680` | 22,480,000.00 USD | 22,480,000.00 USD | 0.00 USD | 856,440.00 USD | 625,850.00 USD | 592,880.00 USD |
| `1D` | `0.9700` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 274,850.00 USD | 111,340.00 USD | 186,340.00 USD |
| `7D` | `0.9700` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 694,250.00 USD | 345,780.00 USD | 263,800.00 USD |
| `1D` | `0.9720` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 99,840.00 USD | 64,240.00 USD | 117,970.00 USD |
| `7D` | `0.9720` | 24,610,000.00 USD | 24,610,000.00 USD | 0.00 USD | 400,520.00 USD | 196,560.00 USD | 225,520.00 USD |
| `1D` | `0.9740` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 36,690.00 USD | 2,780.00 USD | 43,950.00 USD |
| `7D` | `0.9740` | 25,180,000.00 USD | 25,180,000.00 USD | 0.00 USD | 334,930.00 USD | 116,990.00 USD | 116,670.00 USD |
| `1D` | `0.9760` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 20,700.00 USD | 28,970.00 USD | 84,590.00 USD |
| `7D` | `0.9760` | 25,910,000.00 USD | 25,910,000.00 USD | 0.00 USD | 182,900.00 USD | 286,070.00 USD | 264,600.00 USD |
| `1D` | `0.9780` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 32,890.00 USD | 42,000.00 USD | 102,660.00 USD |
| `7D` | `0.9780` | 27,050,000.00 USD | 27,050,000.00 USD | 0.00 USD | 410,980.00 USD | 211,120.00 USD | 517,290.00 USD |
| `1D` | `0.9800` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 61,120.00 USD | 37,860.00 USD | 108,110.00 USD |
| `7D` | `0.9800` | 27,590,000.00 USD | 27,590,000.00 USD | 0.00 USD | 247,060.00 USD | 52,490.00 USD | 238,830.00 USD |
| `1D` | `0.9820` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 76,660.00 USD | 5,650.00 USD | 0.00 USD |
| `7D` | `0.9820` | 27,910,000.00 USD | 27,910,000.00 USD | 0.00 USD | 108,220.00 USD | 68,030.00 USD | 148,410.00 USD |
| `1D` | `0.9840` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 33,500.00 USD | 44,230.00 USD | 5,980.00 USD |
| `7D` | `0.9840` | 28,610,000.00 USD | 28,610,000.00 USD | 0.00 USD | 397,850.00 USD | 123,740.00 USD | 176,370.00 USD |
| `1D` | `0.9860` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 70,580.00 USD | 40,960.00 USD | 90,440.00 USD |
| `7D` | `0.9860` | 28,950,000.00 USD | 28,950,000.00 USD | 0.00 USD | 107,440.00 USD | 154,250.00 USD | 71,320.00 USD |
| `1D` | `0.9880` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 75,940.00 USD | 22,710.00 USD | 42,600.00 USD |
| `7D` | `0.9880` | 29,260,000.00 USD | 29,260,000.00 USD | 0.00 USD | 209,770.00 USD | 75,650.00 USD | 30,070.00 USD |
| `1D` | `0.9900` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 74,860.00 USD | 32,660.00 USD | 23,060.00 USD |
| `7D` | `0.9900` | 29,570,000.00 USD | 29,570,000.00 USD | 0.00 USD | 201,410.00 USD | 100,430.00 USD | 5,820.00 USD |
| `1D` | `0.9920` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 21,690.00 USD | 17,780.00 USD | 11,230.00 USD |
| `7D` | `0.9920` | 30,020,000.00 USD | 30,020,000.00 USD | 0.00 USD | 288,210.00 USD | 79,650.00 USD | 81,980.00 USD |
| `1D` | `0.9940` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 43,770.00 USD | 20,800.00 USD | 70,270.00 USD |
| `7D` | `0.9940` | 30,490,000.00 USD | 30,490,000.00 USD | 0.00 USD | 143,340.00 USD | 183,310.00 USD | 145,950.00 USD |
| `1D` | `0.9960` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 6,270.00 USD | 3,140.00 USD | 20,090.00 USD |
| `7D` | `0.9960` | 30,940,000.00 USD | 30,940,000.00 USD | 0.00 USD | 107,780.00 USD | 55,790.00 USD | 287,750.00 USD |
| `1D` | `0.9980` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 92,080.00 USD | 17,560.00 USD | 148,620.00 USD |
| `7D` | `0.9980` | 31,390,000.00 USD | 31,390,000.00 USD | 0.00 USD | 238,490.00 USD | 42,080.00 USD | 165,400.00 USD |
| `7D` | `1.00` | 31,610,000.00 USD | 31,610,000.00 USD | 0.00 USD | 94,210.00 USD | 53,610.00 USD | 69,200.00 USD |
| `7D` | `1.00` | 32,160,000.00 USD | 32,160,000.00 USD | 0.00 USD | 250,490.00 USD | 51,850.00 USD | 254,030.00 USD |
| `7D` | `1.00` | 32,530,000.00 USD | 32,530,000.00 USD | 0.00 USD | 155,110.00 USD | 54,750.00 USD | 157,280.00 USD |
| `7D` | `1.01` | 32,670,000.00 USD | 32,670,000.00 USD | 0.00 USD | 76,570.00 USD | 24,230.00 USD | 35,750.00 USD |
| `7D` | `1.01` | 33,070,000.00 USD | 33,070,000.00 USD | 0.00 USD | 219,210.00 USD | 23,470.00 USD | 164,880.00 USD |
| `7D` | `1.01` | 33,610,000.00 USD | 33,610,000.00 USD | 0.00 USD | 311,680.00 USD | 74,250.00 USD | 151,960.00 USD |
| `7D` | `1.01` | 34,000,000.00 USD | 34,000,000.00 USD | 0.00 USD | 196,720.00 USD | 102,780.00 USD | 87,330.00 USD |
| `7D` | `1.01` | 34,350,000.00 USD | 34,350,000.00 USD | 0.00 USD | 91,940.00 USD | 116,240.00 USD | 141,090.00 USD |
| `7D` | `1.02` | 35,040,000.00 USD | 35,040,000.00 USD | 0.00 USD | 306,830.00 USD | 87,000.00 USD | 295,030.00 USD |
| `7D` | `1.02` | 35,290,000.00 USD | 35,290,000.00 USD | 0.00 USD | 89,190.00 USD | 9,800.00 USD | 151,730.00 USD |
| `7D` | `1.02` | 35,640,000.00 USD | 35,640,000.00 USD | 0.00 USD | 104,970.00 USD | 47,120.00 USD | 202,070.00 USD |
| `7D` | `1.02` | 35,930,000.00 USD | 35,930,000.00 USD | 0.00 USD | 163,000.00 USD | 30,810.00 USD | 94,190.00 USD |
| `7D` | `1.02` | 36,080,000.00 USD | 36,080,000.00 USD | 0.00 USD | 65,710.00 USD | 37,380.00 USD | 49,650.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `569.83M` | Total OI Tokens: `641,362,489.9 SUI`
  * 1h OI Change: `-1.70%` | 4h OI Change: `+3.26%` | 24h OI Change: `-7.12%`
  * Exchange Breakdown: Binance=`102.24M` | Bybit=`76.41M` | OKX=`33.00M` | Hyperliquid=`29.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-15.44K` | Last 24h: `-2.19K` | Last 3d: `56.09K` | Last 7d: `151.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0027%` | **USDT OKX** | `-0.0029%` |
| **USDT Bybit** | `-0.0171%` | **USDT KuCoin** | `0.0021%` |
| **USDT MEXC** | `-0.0029%` | **USDT BingX** | `-0.0026%` |
| **USDT Gate** | `-0.0058%` | **USDT Bitget** | `-0.0143%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `40.04%` | `59.96%` | `0.67` | 5,550,000.00 USD |
| `15M` | `Binance` | `29.71%` | `70.29%` | `0.42` | 2,150,000.00 USD |
| `15M` | `OKX` | `37.72%` | `62.28%` | `0.61` | 273,890.00 USD |
| `15M` | `Bybit` | `32.88%` | `67.12%` | `0.49` | 588,000.00 USD |
| `15M` | `KuCoin` | `41.35%` | `58.65%` | `0.71` | 34,900.00 USD |
| `15M` | `Gate` | `55.73%` | `44.27%` | `1.26` | 211,380.00 USD |
| `15M` | `Bitget` | `37.19%` | `62.81%` | `0.59` | 126,580.00 USD |
| `15M` | `BingX` | `47.2%` | `52.8%` | `0.89` | 652,490.00 USD |
| `15M` | `MEXC` | `20.21%` | `79.79%` | `0.25` | 209,460.00 USD |
| `15M` | `Bitunix` | `28.79%` | `71.21%` | `0.40` | 93,680.00 USD |
| `15M` | `Hyperliquid` | `19.49%` | `80.51%` | `0.24` | 19,070.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `62.25%` | `37.75%` | `1.65` | 1,130,000.00 USD |
| `15M` | `Crypto.com` | `2.43%` | `97.57%` | `0.02` | 667.59 USD |
| `15M` | `WhiteBIT` | `47.94%` | `52.06%` | `0.92` | 44,200.00 USD |
| `15M` | `HTX` | `34.7%` | `65.3%` | `0.53` | 1,680.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0.37%` | `99.63%` | `0.00` | 9,280.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.64%` | `53.36%` | `0.87` | 10,250.00 USD |
| `15M` | `Whale Positions` | `29.71%` | `70.29%` | `0.42` | 2,150,000.00 USD |
| `15M` | `Global Accounts` | `40.04%` | `59.96%` | `0.67` | 5,550,000.00 USD |
| `1H` | `SUI` | `44.03%` | `55.97%` | `0.79` | 21,530,000.00 USD |
| `1H` | `Binance` | `50.38%` | `49.62%` | `1.02` | 7,370,000.00 USD |
| `1H` | `OKX` | `44.7%` | `55.3%` | `0.81` | 1,640,000.00 USD |
| `1H` | `Bybit` | `32.75%` | `67.25%` | `0.49` | 2,510,000.00 USD |
| `1H` | `KuCoin` | `34.74%` | `65.26%` | `0.53` | 105,460.00 USD |
| `1H` | `Gate` | `30.94%` | `69.06%` | `0.45` | 317,720.00 USD |
| `1H` | `Bitget` | `35.79%` | `64.21%` | `0.56` | 638,780.00 USD |
| `1H` | `BingX` | `31.51%` | `68.49%` | `0.46` | 486,050.00 USD |
| `1H` | `MEXC` | `44.92%` | `55.08%` | `0.82` | 5,920,000.00 USD |
| `1H` | `Bitunix` | `20.38%` | `79.62%` | `0.26` | 1,320,000.00 USD |
| `1H` | `Hyperliquid` | `49.1%` | `50.9%` | `0.96` | 443,220.00 USD |
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
| `1H` | `Whale Positions` | `50.38%` | `49.62%` | `1.02` | 7,370,000.00 USD |
| `1H` | `Global Accounts` | `44.03%` | `55.97%` | `0.79` | 21,530,000.00 USD |
| `4H` | `SUI` | `48.10%` | `51.90%` | `0.93` | 68,640,000.00 USD |
| `4H` | `Binance` | `53.42%` | `46.58%` | `1.15` | 23,660,000.00 USD |
| `4H` | `OKX` | `47.99%` | `52.01%` | `0.92` | 3,900,000.00 USD |
| `4H` | `Bybit` | `48.16%` | `51.84%` | `0.93` | 5,730,000.00 USD |
| `4H` | `KuCoin` | `55.58%` | `44.42%` | `1.25` | 510,220.00 USD |
| `4H` | `Gate` | `46.86%` | `53.14%` | `0.88` | 1,830,000.00 USD |
| `4H` | `Bitget` | `54.54%` | `45.46%` | `1.20` | 1,200,000.00 USD |
| `4H` | `BingX` | `39.97%` | `60.03%` | `0.67` | 14,040,000.00 USD |
| `4H` | `MEXC` | `48.44%` | `51.56%` | `0.94` | 2,750,000.00 USD |
| `4H` | `Bitunix` | `49.35%` | `50.65%` | `0.97` | 1,390,000.00 USD |
| `4H` | `Hyperliquid` | `36.63%` | `63.37%` | `0.58` | 1,280,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.84%` | `52.16%` | `0.92` | 11,520,000.00 USD |
| `4H` | `Crypto.com` | `45.71%` | `54.29%` | `0.84` | 1,830.00 USD |
| `4H` | `WhiteBIT` | `32.95%` | `67.05%` | `0.49` | 471,330.00 USD |
| `4H` | `HTX` | `58.64%` | `41.36%` | `1.42` | 27,950.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `60.39%` | `39.61%` | `1.52` | 48,090.00 USD |
| `4H` | `Aster` | `79.52%` | `20.48%` | `3.88` | 74,650.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `38.79%` | `61.21%` | `0.63` | 213,600.00 USD |
| `4H` | `Whale Positions` | `53.42%` | `46.58%` | `1.15` | 23,660,000.00 USD |
| `4H` | `Global Accounts` | `48.10%` | `51.90%` | `0.93` | 68,640,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.8851` | `0.8843` | `0.8851` | `0.8873` | `0.8813` | 3,303,378.86 USD | 1,747,933.70 USD | 1,555,445.16 USD | 192,488.53 USD | `+5.83%` | `6B / 8S` |
| `0:00 UTC` | `0.8790` | `0.8806` | `0.8790` | `0.8870` | `0.8778` | 3,823,669.01 USD | 1,840,836.89 USD | 1,982,832.12 USD | -141,995.24 USD | `-3.71%` | `23B / 14S` |
| `5:00 UTC` | `0.8903` | `0.8884` | `0.8903` | `0.8908` | `0.8844` | 3,559,512.45 USD | 1,938,272.96 USD | 1,621,239.49 USD | 317,033.48 USD | `+8.91%` | `9B / 6S` |
| `0:00 UTC` | `0.8865` | `0.8876` | `0.8865` | `0.8905` | `0.8850` | 2,686,854.06 USD | 1,226,021.69 USD | 1,460,832.37 USD | -234,810.69 USD | `-8.74%` | `3B / 8S` |
| `5:00 UTC` | `0.8950` | `0.8939` | `0.8950` | `0.8966` | `0.8897` | 3,990,383.01 USD | 1,854,959.02 USD | 2,135,424.00 USD | -280,464.98 USD | `-7.03%` | `14B / 6S` |
| `0:00 UTC` | `0.9031` | `0.9000` | `0.9031` | `0.9050` | `0.8941` | 7,284,926.68 USD | 3,459,713.58 USD | 3,825,213.10 USD | -365,499.52 USD | `-5.02%` | `21B / 11S` |
| `5:00 UTC` | `0.9010` | `0.9015` | `0.9010` | `0.9032` | `0.9001` | 2,342,731.18 USD | 1,068,506.03 USD | 1,274,225.14 USD | -205,719.11 USD | `-8.78%` | `0B / 2S` |
| `0:00 UTC` | `0.9001` | `0.8995` | `0.9001` | `0.9021` | `0.8972` | 2,436,057.12 USD | 986,204.09 USD | 1,449,853.03 USD | -463,648.94 USD | `-19.03%` | `0B / 8S` |
| `5:00 UTC` | `0.8952` | `0.8946` | `0.8952` | `0.8992` | `0.8901` | 2,324,299.92 USD | 686,882.24 USD | 1,637,417.69 USD | -950,535.45 USD | `-40.90%` | `1B / 42S` |
| `0:00 UTC` | `0.8912` | `0.8896` | `0.8912` | `0.8917` | `0.8872` | 2,421,294.66 USD | 1,082,312.13 USD | 1,338,982.53 USD | -256,670.41 USD | `-10.60%` | `2B / 8S` |

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
| `5m` | 22,100.00 USD | -80,370.00 USD | **`DISTRIBUTION`** |
| `15m` | -9,470.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -123,600.00 USD | -1,690,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -603,920.00 USD | -2,860,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,320,000.00 USD | -2,540,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 3,430,000.00 USD | 1,730,000.00 USD | **`ACCUMULATION`** |
| `6h` | -2,470,000.00 USD | -9,750,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -3,730,000.00 USD | -12,330,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -12,930,000.00 USD | -22,830,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,900,000.00 USD | -26,800,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -26,070,000.00 USD | -89,950,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -154,760,000.00 USD | -487,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+22.10K` | 15m=`-9.47K` | 1h=`-603.92K` | 24h=`-7.90M`
* Futures Capital Netflows: 5m=`-80.37K` | 15m=`-1.36M` | 1h=`-2.86M` | 24h=`-26.80M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
