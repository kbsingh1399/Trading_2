# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 17:10:08 IST` (`2026-10-30 11:40:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8948` | `0.8966` | `0.8910` | `0.8914` | `916,293` | 818,713.29 USD | -53,946.30 USD | `-6.59%` | -17,362,835.53 USD | `-0.78` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.8915` | `0.8938` | `0.8912` | `0.8928` | `581,110` | 518,770.92 USD | 967.05 USD | `+0.19%` | -17,361,868.47 USD | `-0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.8929` | `0.8938` | `0.8916` | `0.8919` | `154,639` | 138,025.80 USD | -59,839.61 USD | `-43.35%` | -17,421,708.09 USD | `-0.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8840` | `0.8911` | `0.8835` | `0.8903` | `4,116,047` | 3,655,137.08 USD | 226,605.40 USD | `+6.20%` | -17,390,979.34 USD | `+0.86` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8903` | `0.8951` | `0.8881` | `0.8948` | `1,786,012` | 1,592,683.02 USD | 82,090.10 USD | `+5.15%` | -17,308,889.23 USD | `+0.48` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8948` | `0.8966` | `0.8910` | `0.8918` | `1,651,136` | 1,474,702.48 USD | -112,023.46 USD | `-7.60%` | -17,420,912.69 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8829` | `0.8863` | `0.8791` | `0.8856` | `8,378,902` | 7,391,506.92 USD | -907,807.76 USD | `-12.28%` | -17,320,379.99 USD | `+0.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8857` | `0.8951` | `0.8813` | `0.8948` | `9,128,532` | 8,101,156.58 USD | 180,308.15 USD | `+2.23%` | -17,140,071.84 USD | `+0.58` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.8948` | `0.8966` | `0.8910` | `0.8918` | `1,651,136` | 1,474,702.48 USD | -112,023.46 USD | `-7.60%` | -17,252,095.30 USD | `+0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,183,102.89 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8851` | `53,790,878` | 48,001,087.15 USD | -4,396,820.97 USD | `-9.16%` | -16,579,923.86 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8851` | `0.8966` | `0.8791` | `0.8919` | `27,452,740` | 24,297,940.29 USD | -672,886.36 USD | `-2.77%` | -17,252,810.22 USD | `+0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -544,594.77 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,247,029.61 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,183,102.89 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8851` | `53,790,878` | 48,001,087.15 USD | -4,396,820.97 USD | `-9.16%` | -16,579,923.86 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8851` | `0.8966` | `0.8791` | `0.8919` | `27,452,740` | 24,297,940.29 USD | -672,886.36 USD | `-2.77%` | -17,252,810.22 USD | `+0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID` | `0.8889` | `1303.9000` | 1,159.09 USD | 46,810.63 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8890` | `2123.6000` | 1,887.92 USD | 24,499.77 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8890` | `3996.2000` | 3,552.62 USD | 28,052.39 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8890` | `10476.9000` | 9,313.75 USD | 37,366.15 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8890` | `977.9000` | 869.32 USD | 38,235.47 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8890` | `12.5000` | 11.11 USD | 38,246.59 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8890` | `8330.0000` | 7,404.95 USD | 45,651.54 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.8891` | `1303.9000` | 1,159.35 USD | 16,818.26 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8891` | `1304.0000` | 1,159.41 USD | 17,977.68 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8891` | `5212.5000` | 4,634.17 USD | 22,611.85 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `0.8892` | `56.2000` | 49.98 USD | 5,683.78 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8892` | `5630.9000` | 5,007.17 USD | 10,690.95 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8892` | `3976.8000` | 3,536.25 USD | 14,227.20 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8892` | `1610.1000` | 1,431.72 USD | 15,658.91 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.8893` | `978.2000` | 869.96 USD | 4,474.28 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8893` | `1303.9000` | 1,159.53 USD | 5,633.81 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8894` | `112.3000` | 99.88 USD | 1,747.68 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8894` | `2087.6000` | 1,856.63 USD | 3,604.31 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8895` | `726.7000` | 646.43 USD | 646.43 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.8895` | `1125.8000` | 1,001.38 USD | 1,647.81 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `0.8896` | `693.6000` | 617.05 USD | 1,195.29 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8896` | `650.0000` | 578.24 USD | 578.24 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.8896` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.89` | `0.00%` | `-` |
| `ASK` | `0.8897` | `1125.5000` | 1,001.39 USD | 4,516.45 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8897` | `1303.7000` | 1,159.93 USD | 3,515.06 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8897` | `1303.7000` | 1,159.84 USD | 2,355.13 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8898` | `6931.6000` | 6,168.01 USD | 11,844.73 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.8898` | `1304.0000` | 1,160.26 USD | 5,676.71 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8899` | `1303.7000` | 1,160.18 USD | 17,007.91 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8899` | `2250.7000` | 2,002.90 USD | 15,847.74 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8899` | `2247.7000` | 2,000.12 USD | 13,844.84 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8900` | `349.1000` | 310.71 USD | 23,393.98 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8900` | `1303.9000` | 1,160.51 USD | 23,083.27 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8900` | `798.8000` | 710.95 USD | 21,922.76 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8900` | `3244.9000` | 2,887.96 USD | 21,211.81 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8900` | `1303.9000` | 1,160.46 USD | 18,323.85 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8900` | `174.7000` | 155.48 USD | 17,163.39 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8901` | `2696.2000` | 2,399.91 USD | 50,919.55 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8901` | `22939.4000` | 20,418.36 USD | 48,519.63 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `0.8901` | `1303.9000` | 1,160.59 USD | 28,101.27 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8901` | `3984.7000` | 3,546.70 USD | 26,940.68 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `666` | `0xb83d...6e36` | `SHORT` | 3,395,114.57 USD | `3,817,609.40` | `1.11` | `0.8891` | `27.44` | 823,620.75 USD | `+24.26%` | `3X Cross` |
| `993` | `0xa2ce...3126` | `LONG` | 2,223,259.25 USD | `2,500,010.40` | `0.8597` | `0.8891` | `0.000000` | 74,052.72 USD | `+3.33%` | `10X Cross` |
| `1504` | `0x9946...0852` | `SHORT` | 1,434,308.23 USD | `1,613,032.20` | `1.06` | `0.8891` | `1.85` | 274,369.85 USD | `+19.13%` | `10X Cross` |
| `1898` | `0x9df2...c665` | `SHORT` | 1,067,088.00 USD | `1,200,000.00` | `0.7465` | `0.8891` | `18.50` | -171,235.60 USD | `-16.05%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9473` | 1,287.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.29K USD at 0.9473 USD [API] | `2026-10-29 14:36:31` |
| `ANNOUNCEMENT` | `INFO` | `0.9311` | 11,583.57 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 11.58K USD at 0.9311 USD [API] | `2026-10-29 19:23:03` |
| `ANNOUNCEMENT` | `INFO` | `0.9311` | 15,011.45 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 15.01K USD at 0.9311 USD [API] | `2026-10-29 19:23:03` |
| `ANNOUNCEMENT` | `INFO` | `0.9304` | 16,416.34 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 16.42K USD at 0.9304 USD [API] | `2026-10-29 19:48:48` |
| `ANNOUNCEMENT` | `INFO` | `0.9400` | 239.98 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.24K USD at 0.9400 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9400` | 305.31 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.31K USD at 0.9400 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9400` | 2,350.00 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.35K USD at 0.9400 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9400` | 19.93 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.02K USD at 0.9400 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9402` | 1,145.74 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.15K USD at 0.9402 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9402` | 49.93 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.05K USD at 0.9402 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9402` | 5,005.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 5.01K USD at 0.9402 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9403` | 104.94 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9403 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9403` | 102.59 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9403 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9403` | 1,309.88 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.31K USD at 0.9403 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9403` | 1,309.88 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.31K USD at 0.9403 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9403` | 1,309.88 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.31K USD at 0.9403 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9403` | 1,309.88 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.31K USD at 0.9403 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9404` | 1,897.63 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.90K USD at 0.9404 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9404` | 74.95 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.07K USD at 0.9404 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9404` | 3,399.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.40K USD at 0.9404 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 50.04 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.05K USD at 0.9406 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9408` | 49.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.05K USD at 0.9408 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9408` | 3,290.73 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.29K USD at 0.9408 USD [API] | `2026-10-23 22:55:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9358` | 154.13 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.15K USD at 0.9358 USD [API] | `2026-10-24 14:14:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9358` | 7,836.81 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 7.84K USD at 0.9358 USD [API] | `2026-10-24 14:14:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9358` | 0.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.00K USD at 0.9358 USD [API] | `2026-10-24 14:14:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9359` | 9,868.46 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 9.87K USD at 0.9359 USD [API] | `2026-10-24 14:14:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9685` | 2,241.79 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.24K USD at 0.9685 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9685` | 3,999.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 4.00K USD at 0.9685 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9686` | 400.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.40K USD at 0.9686 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9686` | 48.43 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.05K USD at 0.9686 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9687` | 49.98 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.05K USD at 0.9687 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9687` | 1,675.04 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.68K USD at 0.9687 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9687` | 199.94 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.20K USD at 0.9687 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9688` | 12.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.01K USD at 0.9688 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9689` | 2,233.85 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.23K USD at 0.9689 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9689` | 2,233.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.23K USD at 0.9689 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9689` | 495.13 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.50K USD at 0.9689 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9690` | 277.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.28K USD at 0.9690 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9690` | 226.65 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.23K USD at 0.9690 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9691` | 558.61 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.56K USD at 0.9691 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9691` | 5,247.85 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 5.25K USD at 0.9691 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9691` | 1,035.92 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.04K USD at 0.9691 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9273` | 3,905.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.91K USD at 0.9273 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `0.9273` | 763.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.76K USD at 0.9273 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `0.9273` | 572.54 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.57K USD at 0.9273 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `0.9274` | 1,901.38 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.90K USD at 0.9274 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `0.9274` | 763.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.76K USD at 0.9274 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `0.9274` | 100.07 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9274 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `0.9274` | 1,026.28 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.03K USD at 0.9274 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `0.9029` | 16,002.73 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 16.00K USD at 0.9029 USD [API] | `2026-10-29 20:38:24` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9069` (Vol: 461,900.00 USD, Dist: `+1.94%`) | Long MP=`0.8716` (Vol: 461,900.00 USD, Dist: `--2.03%`)
  * 48H Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+2.02%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--2.06%`)
  * 3D Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+2.02%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--2.06%`)
  * 7D Horizon: Short MP=`0.9731` (Vol: 542,500.00 USD, Dist: `+9.39%`) | Long MP=`0.8715` (Vol: 414,400.00 USD, Dist: `--2.03%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1885` | 188.50 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 2,710.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 414.21 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 132.80 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 1,500.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 4,630.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 2,670.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2535` | 2,260.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 160.42 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 849.48 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 171.12 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 278.50 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 3,480.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 53,920.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,860.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 282.73 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3125` | 110.53 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3165` | 104.73 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3295` | 25,600.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3375` | 9,610.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3425` | 3,430.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 5,070.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3635` | 405.34 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3685` | 4,610.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3735` | 6,350.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 3,860.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 3,260.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 3,360.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4085` | 740.57 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4155` | 732.11 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4205` | 29,430.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4215` | 3,930.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4245` | 8,960.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4335` | 367.52 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 44,080.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 219.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 105.25 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4505` | 6,110.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 316.75 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 1,020.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 3,330.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 9,230.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4775` | 252.69 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 166.70 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 3,540.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 536.96 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 5,520.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5005` | 5,280.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 475.07 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5035` | 1,390.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 76,870.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 228.38 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 106.04 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 1,110.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 123,140.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,610.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5305` | 264.56 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 10,460.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 113.47 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 126.46 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5435` | 5,900.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 1,310.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 27,770.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5615` | 950.84 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 1,480.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 7,200.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 6,330.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 109,930.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 485.51 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 217.37 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 269.98 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,280.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 822.98 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5875` | 176.25 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 225.93 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 1,130.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 608.61 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5975` | 3,420.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 299.25 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 4,610.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 3,030.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 113,380.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 699.84 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 1,040.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6095` | 214.54 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,280.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 438.73 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 2,110.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 44,470.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,980.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 12,570.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 2,400.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 708.53 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 34,160.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 1,100.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 949.85 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 2,130.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 1,690.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 1,100.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 34,650.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 588.32 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 86,950.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,190.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 2,810.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 1,060.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 344.82 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 106.75 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6525` | 2,350.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 3,990.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 6,700.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 676.54 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 7,070.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 130.91 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 16,140.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 1,060.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6605` | 184.35 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 15,600.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 1,400.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6655` | 2,290.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 728.68 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 2,260.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 5,470.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 273.16 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,630.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 29,210.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,280.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 744.15 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 2,370.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 122.94 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 39,510.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 4,150.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 19,300.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 11,170.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 2,430.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6855` | 4,290.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 6,110.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 7,690.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 722.28 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,700.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 16,070.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,820.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 5,130.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7025` | 39,470.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 8,970.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 141.38 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 143.14 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 770.68 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,810.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 1,140.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 4,190.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 283.22 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 927.55 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 11,030.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 4,620.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7185` | 126.96 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 420.19 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 8,970.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,420.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 127.05 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7245` | 11,950.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 435,610.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 3,410.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 35,890.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 3,280.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 246.12 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,630.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 22,160.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 3,450.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,020.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 1,170.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 796,610.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 6,350.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7465` | 563.83 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 357.14 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 569.50 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 922.07 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,070.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7570` | 11,050,000.00 USD | 11,050,000.00 USD | 22,280.00 USD | 18,340.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7590` | 11,000,000.00 USD | 11,000,000.00 USD | 6,840.00 USD | 25,130.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7595` | 1,650.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 6,170.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7610` | 10,970,000.00 USD | 10,970,000.00 USD | 21,310.00 USD | 16,580.00 USD | 630.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7625` | 859.11 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 10,930,000.00 USD | 10,930,000.00 USD | 20,690.00 USD | 118.70 USD | 573.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 439.47 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,060.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 10,910,000.00 USD | 10,910,000.00 USD | 556.58 USD | 23,090.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 2,740.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 2,950.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 10,870,000.00 USD | 10,870,000.00 USD | 1,280.00 USD | 3,960.00 USD | 18,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 24,420.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 6,600.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 10,850,000.00 USD | 10,850,000.00 USD | 182.28 USD | 161.63 USD | 3,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 10,850,000.00 USD | 10,850,000.00 USD | 7,690.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,220.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 5,230.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 3,430.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 2,930.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 5,390.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7810` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 185.50 USD | 5,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7825` | 323,560.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 3,930.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 1,880.00 USD | 743,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7850` | 10,820,000.00 USD | 10,820,000.00 USD | 7,790.00 USD | 20,370.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 741,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 24,880.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 738,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 14,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 1,980.00 USD | 737,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7900` | 9,110,000.00 USD | 9,110,000.00 USD | 20,640.00 USD | 25,340.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 5,190.00 USD | 735,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7910` | 9,050,000.00 USD | 9,050,000.00 USD | 1,950.00 USD | 6,990.00 USD | 285.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 10,740,000.00 USD | 10,740,000.00 USD | 6,610.00 USD | 24,700.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 11,600.00 USD | 730,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 9,040,000.00 USD | 9,040,000.00 USD | 13,250.00 USD | 9,540.00 USD | 36,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 3,800.00 USD | 719,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7930` | 8,980,000.00 USD | 8,980,000.00 USD | 6,520.00 USD | 12,800.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 13,760.00 USD | 67,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 715,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7940` | 8,960,000.00 USD | 8,960,000.00 USD | 30,290.00 USD | 8,810.00 USD | 23,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 595.40 USD | 714,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7950` | 8,890,000.00 USD | 8,890,000.00 USD | 9,270.00 USD | 4,100.00 USD | 25,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 10,630,000.00 USD | 10,630,000.00 USD | 3,420.00 USD | 20,630.00 USD | 75,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 52,610.00 USD | 713,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 8,860,000.00 USD | 8,860,000.00 USD | 10,800.00 USD | 2,830.00 USD | 25,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 13,090.00 USD | 661,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 8,820,000.00 USD | 8,820,000.00 USD | 24,100.00 USD | 20,190.00 USD | 47,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 10,530,000.00 USD | 10,530,000.00 USD | 27,750.00 USD | 4,320.00 USD | 53,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,460.00 USD | 648,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 8,730,000.00 USD | 8,730,000.00 USD | 15,810.00 USD | 0.00 USD | 333.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 40,070.00 USD | 640,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7990` | 8,710,000.00 USD | 8,710,000.00 USD | 1,600.00 USD | 22,720.00 USD | 18,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 10,440,000.00 USD | 10,440,000.00 USD | 8,070.00 USD | 10,040.00 USD | 27,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 4,380.00 USD | 600,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 8,670,000.00 USD | 8,670,000.00 USD | 41,250.00 USD | 14,850.00 USD | 20,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 6,510.00 USD | 596,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8010` | 8,590,000.00 USD | 8,590,000.00 USD | 13,800.00 USD | 8,500.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 10,400,000.00 USD | 10,400,000.00 USD | 60,350.00 USD | 29,250.00 USD | 56,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 6,820.00 USD | 589,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8020` | 8,560,000.00 USD | 8,560,000.00 USD | 1,270.00 USD | 6,400.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 1,350.00 USD | 582,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8030` | 8,550,000.00 USD | 8,550,000.00 USD | 11,920.00 USD | 11,150.00 USD | 159.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8030` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 26,250.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,680.00 USD | 581,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8040` | 8,520,000.00 USD | 8,520,000.00 USD | 43,320.00 USD | 36,370.00 USD | 26,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8045` | 15,720.00 USD | 573,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8050` | 8,420,000.00 USD | 8,420,000.00 USD | 19,790.00 USD | 7,230.00 USD | 330.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 10,220,000.00 USD | 10,220,000.00 USD | 10,860.00 USD | 32,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 361.11 USD | 558,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 8,390,000.00 USD | 8,390,000.00 USD | 36,670.00 USD | 11,640.00 USD | 73,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 557,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 8,270,000.00 USD | 8,270,000.00 USD | 8,540.00 USD | 14,620.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 10,170,000.00 USD | 10,170,000.00 USD | 6,450.00 USD | 11,280.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 550,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8080` | 8,250,000.00 USD | 8,250,000.00 USD | 2,530.00 USD | 4,510.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 21,200.00 USD | 548,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8090` | 8,240,000.00 USD | 8,240,000.00 USD | 587.71 USD | 5,580.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 154,810.00 USD | 526,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 8,230,000.00 USD | 8,230,000.00 USD | 1,830.00 USD | 5,380.00 USD | 248.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 372,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8110` | 8,220,000.00 USD | 8,220,000.00 USD | 1,650.00 USD | 2,090.00 USD | 196.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 10,140,000.00 USD | 10,140,000.00 USD | 61,670.00 USD | 8,310.00 USD | 44,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 1,720.00 USD | 369,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 8,220,000.00 USD | 8,220,000.00 USD | 13,640.00 USD | 780.21 USD | 23,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 1,160.00 USD | 368,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8130` | 8,180,000.00 USD | 8,180,000.00 USD | 683.00 USD | 989.28 USD | 706.99 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 10,030,000.00 USD | 10,030,000.00 USD | 45,800.00 USD | 19,710.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 366,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 8,180,000.00 USD | 8,180,000.00 USD | 14,810.00 USD | 523.16 USD | 11,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 363,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 8,150,000.00 USD | 8,150,000.00 USD | 4,970.00 USD | 1,140.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 9,950,000.00 USD | 9,950,000.00 USD | 139,680.00 USD | 51,810.00 USD | 172,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 2,810.00 USD | 362,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 8,140,000.00 USD | 8,140,000.00 USD | 17,910.00 USD | 1,970.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 729.13 USD | 360,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8170` | 8,090,000.00 USD | 8,090,000.00 USD | 56,460.00 USD | 4,990.00 USD | 30,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 9,590,000.00 USD | 9,590,000.00 USD | 91,050.00 USD | 25,080.00 USD | 77,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 77,840.00 USD | 359,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 351.95 USD | 213.40 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8190` | 8,000,000.00 USD | 8,000,000.00 USD | 24,470.00 USD | 1,520.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 9,390,000.00 USD | 9,390,000.00 USD | 200,250.00 USD | 53,380.00 USD | 49,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,140.00 USD | 281,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 7,960,000.00 USD | 7,960,000.00 USD | 82,040.00 USD | 3,460.00 USD | 73,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8210` | 7,810,000.00 USD | 7,810,000.00 USD | 16,280.00 USD | 83,250.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 9,090,000.00 USD | 9,090,000.00 USD | 138,580.00 USD | 80,040.00 USD | 199,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,770.00 USD | 280,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 7,660,000.00 USD | 7,660,000.00 USD | 60,840.00 USD | 2,360.00 USD | 18,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 1,020.00 USD | 278,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 7,570,000.00 USD | 7,570,000.00 USD | 6,660.00 USD | 3,770.00 USD | 103,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 8,670,000.00 USD | 8,670,000.00 USD | 47,220.00 USD | 42,890.00 USD | 66,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 1,870.00 USD | 277,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 7,460,000.00 USD | 7,460,000.00 USD | 7,980.00 USD | 2,930.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 18,280.00 USD | 275,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 7,420,000.00 USD | 7,420,000.00 USD | 28,540.00 USD | 1,410.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 8,520,000.00 USD | 8,520,000.00 USD | 208,750.00 USD | 32,700.00 USD | 124,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 1,580.00 USD | 257,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 7,390,000.00 USD | 7,390,000.00 USD | 19,380.00 USD | 9,260.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8270` | 7,340,000.00 USD | 7,340,000.00 USD | 39,420.00 USD | 16,780.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 8,150,000.00 USD | 8,150,000.00 USD | 147,770.00 USD | 53,560.00 USD | 60,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 255,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 7,280,000.00 USD | 7,280,000.00 USD | 1,470.00 USD | 697.90 USD | 564.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 251,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8290` | 7,280,000.00 USD | 7,280,000.00 USD | 25,790.00 USD | 5,230.00 USD | 46,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 7,890,000.00 USD | 7,890,000.00 USD | 97,180.00 USD | 43,350.00 USD | 86,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8300` | 7,200,000.00 USD | 7,200,000.00 USD | 4,230.00 USD | 3,350.00 USD | 7,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8310` | 7,190,000.00 USD | 7,190,000.00 USD | 3,130.00 USD | 27,660.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 7,660,000.00 USD | 7,660,000.00 USD | 36,870.00 USD | 32,050.00 USD | 111,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 7,130,000.00 USD | 7,130,000.00 USD | 867.90 USD | 10,650.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 7,100,000.00 USD | 7,100,000.00 USD | 7,940.00 USD | 19,110.00 USD | 74,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 7,480,000.00 USD | 7,480,000.00 USD | 157,210.00 USD | 105,720.00 USD | 197,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 7,000,000.00 USD | 7,000,000.00 USD | 142,890.00 USD | 21,960.00 USD | 30,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8345` | 5,750.00 USD | 131,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8350` | 6,800,000.00 USD | 6,800,000.00 USD | 14,620.00 USD | 13,380.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 7,020,000.00 USD | 7,020,000.00 USD | 120,070.00 USD | 16,770.00 USD | 87,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 6,770,000.00 USD | 6,770,000.00 USD | 46,210.00 USD | 1,970.00 USD | 397.88 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 28,050.00 USD | 125,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 6,720,000.00 USD | 6,720,000.00 USD | 22,120.00 USD | 10,740.00 USD | 129,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 6,800,000.00 USD | 6,800,000.00 USD | 140,480.00 USD | 111,450.00 USD | 140,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 6,560,000.00 USD | 6,560,000.00 USD | 35,600.00 USD | 60,420.00 USD | 16,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 948.34 USD | 97,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8390` | 6,450,000.00 USD | 6,450,000.00 USD | 45,660.00 USD | 1,500.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 6,400,000.00 USD | 6,400,000.00 USD | 41,090.00 USD | 164,090.00 USD | 167,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 8,460.00 USD | 96,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 6,370,000.00 USD | 6,370,000.00 USD | 7,690.00 USD | 9,650.00 USD | 22,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 6,330,000.00 USD | 6,330,000.00 USD | 17,680.00 USD | 16,720.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 6,030,000.00 USD | 6,030,000.00 USD | 99,070.00 USD | 35,890.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 750.79 USD | 87,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 6,240,000.00 USD | 6,240,000.00 USD | 71,930.00 USD | 48,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 11,790.00 USD | 87,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 6,120,000.00 USD | 6,120,000.00 USD | 17,820.00 USD | 18,730.00 USD | 22,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 5,870,000.00 USD | 5,870,000.00 USD | 67,920.00 USD | 123,520.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 103.24 USD | 75,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 6,060,000.00 USD | 6,060,000.00 USD | 49,800.00 USD | 44,550.00 USD | 166.34 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 803.20 USD | 75,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8450` | 5,960,000.00 USD | 5,960,000.00 USD | 35,860.00 USD | 31,570.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 5,670,000.00 USD | 5,670,000.00 USD | 37,890.00 USD | 103,700.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 10,690.00 USD | 74,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 5,880,000.00 USD | 5,880,000.00 USD | 24,060.00 USD | 68,600.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 157.20 USD | 63,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8470` | 5,760,000.00 USD | 5,760,000.00 USD | 91,300.00 USD | 39,700.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 5,520,000.00 USD | 5,520,000.00 USD | 44,110.00 USD | 0.00 USD | 29,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 317.98 USD | 63,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 5,600,000.00 USD | 5,600,000.00 USD | 11,990.00 USD | 37,210.00 USD | 85,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 5,470,000.00 USD | 5,470,000.00 USD | 95,010.00 USD | 64,020.00 USD | 80,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 5,450,000.00 USD | 5,450,000.00 USD | 64,910.00 USD | 84,070.00 USD | 135,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 6,910.00 USD | 63,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 5,230,000.00 USD | 5,230,000.00 USD | 46,610.00 USD | 37,570.00 USD | 113,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8505` | 13,600.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 5,030,000.00 USD | 5,030,000.00 USD | 52,490.00 USD | 115,520.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 5,160,000.00 USD | 5,160,000.00 USD | 157,910.00 USD | 72,120.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 4,800,000.00 USD | 4,800,000.00 USD | 78,650.00 USD | 101,060.00 USD | 88,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 42,610.00 USD | 42,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8530` | 4,530,000.00 USD | 4,530,000.00 USD | 126,550.00 USD | 99,460.00 USD | 27,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 4,910,000.00 USD | 4,910,000.00 USD | 239,650.00 USD | 73,080.00 USD | 95,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 104.30 USD | 104.30 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 4,280,000.00 USD | 4,280,000.00 USD | 36,780.00 USD | 36,580.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 4,180,000.00 USD | 4,180,000.00 USD | 9,680.00 USD | 45,100.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 4,510,000.00 USD | 4,510,000.00 USD | 118,050.00 USD | 50,640.00 USD | 34,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 4,100,000.00 USD | 4,100,000.00 USD | 67,310.00 USD | 41,200.00 USD | 52,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 3,940,000.00 USD | 3,940,000.00 USD | 14,730.00 USD | 46,510.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 4,300,000.00 USD | 4,300,000.00 USD | 140,780.00 USD | 111,600.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 3,860,000.00 USD | 3,860,000.00 USD | 32,900.00 USD | 54,050.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 3,740,000.00 USD | 3,740,000.00 USD | 25,280.00 USD | 6,720.00 USD | 41,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 3,990,000.00 USD | 3,990,000.00 USD | 132,610.00 USD | 87,830.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 3,670,000.00 USD | 3,670,000.00 USD | 75,640.00 USD | 32,480.00 USD | 167.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 3,560,000.00 USD | 3,560,000.00 USD | 21,120.00 USD | 0.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 3,770,000.00 USD | 3,770,000.00 USD | 36,870.00 USD | 188,190.00 USD | 32,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 3,530,000.00 USD | 3,530,000.00 USD | 66,110.00 USD | 25,800.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 3,410,000.00 USD | 3,410,000.00 USD | 90,570.00 USD | 107,100.00 USD | 121,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 3,510,000.00 USD | 3,510,000.00 USD | 100,980.00 USD | 64,400.00 USD | 387,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8640` | 3,100,000.00 USD | 3,100,000.00 USD | 108,200.00 USD | 54,960.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,880,000.00 USD | 2,880,000.00 USD | 23,980.00 USD | 35,600.00 USD | 142,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 2,960,000.00 USD | 2,960,000.00 USD | 254,940.00 USD | 122,950.00 USD | 622,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,680,000.00 USD | 2,680,000.00 USD | 200,780.00 USD | 17,340.00 USD | 79,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8670` | 2,380,000.00 USD | 2,380,000.00 USD | 122,450.00 USD | 33,880.00 USD | 154,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,950,000.00 USD | 1,950,000.00 USD | 252,430.00 USD | 0.00 USD | 158,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 2,070,000.00 USD | 2,070,000.00 USD | 72,190.00 USD | 17,760.00 USD | 33,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,940,000.00 USD | 1,940,000.00 USD | 37,450.00 USD | 0.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 109,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 108,470.00 USD | 31,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,740,000.00 USD | 1,740,000.00 USD | 217,480.00 USD | 79,810.00 USD | 182,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,430,000.00 USD | 1,430,000.00 USD | 254,800.00 USD | 146,150.00 USD | 92,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,260,000.00 USD | 1,260,000.00 USD | 103,610.00 USD | 73,160.00 USD | 64,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,020,000.00 USD | 1,020,000.00 USD | 71,110.00 USD | 55,280.00 USD | 52,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 940,870.00 USD | 940,870.00 USD | 79,470.00 USD | 101,280.00 USD | 137,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 840,500.00 USD | 840,500.00 USD | 134,620.00 USD | 68,390.00 USD | 39,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 598,050.00 USD | 598,050.00 USD | 29,460.00 USD | 67,500.00 USD | 117,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 622,250.00 USD | 622,250.00 USD | 108,430.00 USD | 112,580.00 USD | 306,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 383,380.00 USD | 383,380.00 USD | 0.00 USD | 0.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 330,320.00 USD | 330,320.00 USD | 50,560.00 USD | 20,280.00 USD | 104,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 94,460.00 USD | 94,460.00 USD | 0.00 USD | 61,690.00 USD | 3,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 154,780.00 USD | 154,780.00 USD | 79,990.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 57,370.00 USD | 57,370.00 USD | 39,180.00 USD | 0.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 29,340.00 USD | 29,340.00 USD | 0.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 5,260.00 USD | 5,260.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 26,030.00 USD | 26,030.00 USD | 20,310.00 USD | 0.00 USD | 196.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 4,260.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 2,430.00 USD | 2,430.00 USD | 0.00 USD | 0.00 USD | 214.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 2,220.00 USD | 2,220.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 5,530.00 USD | 5,530.00 USD | 0.00 USD | 0.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 811.86 USD | 811.86 USD | 0.00 USD | 0.00 USD | 560.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8905` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8910` | 251.48 USD | 251.48 USD | 0.00 USD | 0.00 USD | 251.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8910` | 528,160.00 USD | 528,160.00 USD | 523,470.00 USD | 0.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8910` | 1,060,000.00 USD | 1,060,000.00 USD | 523,470.00 USD | 0.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 1,790.00 USD | 1,790.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 3,570.00 USD | 3,570.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8930` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 728.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8940` | 25,140.00 USD | 25,140.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8950` | 102,990.00 USD | 102,990.00 USD | 0.00 USD | 77,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 1,930,000.00 USD | 1,930,000.00 USD | 800,940.00 USD | 68,760.00 USD | 325.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8970` | 103,960.00 USD | 103,960.00 USD | 969.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8970` | 2,650,000.00 USD | 2,650,000.00 USD | 617,630.00 USD | 93,070.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8980` | 260,980.00 USD | 260,980.00 USD | 96,220.00 USD | 60,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8990` | 511,410.00 USD | 511,410.00 USD | 113,150.00 USD | 129,660.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8990` | 3,420,000.00 USD | 3,420,000.00 USD | 368,200.00 USD | 67,360.00 USD | 340,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9000` | 816,950.00 USD | 816,950.00 USD | 246,360.00 USD | 5,150.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9010` | 955,070.00 USD | 955,070.00 USD | 27,370.00 USD | 80,270.00 USD | 30,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 4,210,000.00 USD | 4,210,000.00 USD | 207,550.00 USD | 138,590.00 USD | 435,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 1,130,000.00 USD | 1,130,000.00 USD | 93,760.00 USD | 57,880.00 USD | 24,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9030` | 1,280,000.00 USD | 1,280,000.00 USD | 47,830.00 USD | 71,900.00 USD | 28,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9030` | 4,570,000.00 USD | 4,570,000.00 USD | 124,030.00 USD | 99,390.00 USD | 136,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9040` | 1,660,000.00 USD | 1,660,000.00 USD | 197,110.00 USD | 154,100.00 USD | 33,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9050` | 1,860,000.00 USD | 1,860,000.00 USD | 127,800.00 USD | 26,270.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9050` | 5,060,000.00 USD | 5,060,000.00 USD | 169,680.00 USD | 0.00 USD | 323,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9060` | 2,370,000.00 USD | 2,370,000.00 USD | 168,180.00 USD | 169,000.00 USD | 165,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9070` | 2,860,000.00 USD | 2,860,000.00 USD | 200,430.00 USD | 145,890.00 USD | 147,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 5,980,000.00 USD | 5,980,000.00 USD | 595,880.00 USD | 197,080.00 USD | 123,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9080` | 3,160,000.00 USD | 3,160,000.00 USD | 151,730.00 USD | 92,080.00 USD | 60,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9090` | 3,380,000.00 USD | 3,380,000.00 USD | 92,480.00 USD | 65,350.00 USD | 56,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 6,590,000.00 USD | 6,590,000.00 USD | 140,150.00 USD | 244,140.00 USD | 229,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 3,670,000.00 USD | 3,670,000.00 USD | 156,840.00 USD | 98,270.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9110` | 3,920,000.00 USD | 3,920,000.00 USD | 97,650.00 USD | 84,090.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 7,270,000.00 USD | 7,270,000.00 USD | 341,320.00 USD | 216,330.00 USD | 120,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 4,100,000.00 USD | 4,100,000.00 USD | 32,690.00 USD | 81,230.00 USD | 69,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9130` | 4,300,000.00 USD | 4,300,000.00 USD | 68,900.00 USD | 25,330.00 USD | 103,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 7,500,000.00 USD | 7,500,000.00 USD | 80,230.00 USD | 148,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 4,670,000.00 USD | 4,670,000.00 USD | 162,940.00 USD | 61,860.00 USD | 142,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 6,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9150` | 5,040,000.00 USD | 5,040,000.00 USD | 120,960.00 USD | 68,860.00 USD | 184,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 7,890,000.00 USD | 7,890,000.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9160` | 5,280,000.00 USD | 5,280,000.00 USD | 81,680.00 USD | 104,770.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9170` | 5,510,000.00 USD | 5,510,000.00 USD | 103,830.00 USD | 28,770.00 USD | 94,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 8,090,000.00 USD | 8,090,000.00 USD | 163,880.00 USD | 2,050.00 USD | 31,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 5,680,000.00 USD | 5,680,000.00 USD | 38,530.00 USD | 60,340.00 USD | 71,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9190` | 5,860,000.00 USD | 5,860,000.00 USD | 94,380.00 USD | 18,760.00 USD | 61,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 8,700,000.00 USD | 8,700,000.00 USD | 296,480.00 USD | 75,390.00 USD | 238,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9195` | 4,600.00 USD | 11,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 6,050,000.00 USD | 6,050,000.00 USD | 76,540.00 USD | 16,940.00 USD | 105,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9210` | 6,360,000.00 USD | 6,360,000.00 USD | 96,850.00 USD | 70,120.00 USD | 141,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 9,100,000.00 USD | 9,100,000.00 USD | 194,470.00 USD | 18,660.00 USD | 187,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 6,680,000.00 USD | 6,680,000.00 USD | 147,880.00 USD | 32,770.00 USD | 136,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9230` | 6,990,000.00 USD | 6,990,000.00 USD | 107,110.00 USD | 55,720.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 9,620,000.00 USD | 9,620,000.00 USD | 56,540.00 USD | 68,150.00 USD | 398,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9235` | 209.36 USD | 11,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9240` | 7,310,000.00 USD | 7,310,000.00 USD | 133,900.00 USD | 65,460.00 USD | 117,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9250` | 7,620,000.00 USD | 7,620,000.00 USD | 167,630.00 USD | 71,780.00 USD | 70,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 10,030,000.00 USD | 10,030,000.00 USD | 182,660.00 USD | 120,540.00 USD | 109,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 7,840,000.00 USD | 7,840,000.00 USD | 43,480.00 USD | 95,380.00 USD | 74,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9270` | 7,970,000.00 USD | 7,970,000.00 USD | 18,040.00 USD | 75,810.00 USD | 39,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 10,520,000.00 USD | 10,520,000.00 USD | 270,890.00 USD | 100,630.00 USD | 118,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 8,170,000.00 USD | 8,170,000.00 USD | 77,040.00 USD | 54,950.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9285` | 1,100.00 USD | 12,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9290` | 8,320,000.00 USD | 8,320,000.00 USD | 53,740.00 USD | 37,110.00 USD | 62,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 10,750,000.00 USD | 10,750,000.00 USD | 52,860.00 USD | 111,530.00 USD | 62,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 8,450,000.00 USD | 8,450,000.00 USD | 5,010.00 USD | 59,630.00 USD | 65,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9310` | 8,640,000.00 USD | 8,640,000.00 USD | 129,900.00 USD | 16,270.00 USD | 42,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 11,180,000.00 USD | 11,180,000.00 USD | 181,630.00 USD | 80,980.00 USD | 168,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 8,780,000.00 USD | 8,780,000.00 USD | 71,540.00 USD | 29,090.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9325` | 2,420.00 USD | 15,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9330` | 8,830,000.00 USD | 8,830,000.00 USD | 25,650.00 USD | 20,660.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 11,330,000.00 USD | 11,330,000.00 USD | 7,740.00 USD | 77,810.00 USD | 65,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 8,850,000.00 USD | 8,850,000.00 USD | 1,200.00 USD | 16,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 8,870,000.00 USD | 8,870,000.00 USD | 2,160.00 USD | 867.77 USD | 19,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 11,440,000.00 USD | 11,440,000.00 USD | 53,950.00 USD | 55,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9355` | 237.34 USD | 15,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9360` | 9,000,000.00 USD | 9,000,000.00 USD | 49,530.00 USD | 26,230.00 USD | 55,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9365` | 374.23 USD | 15,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9370` | 9,200,000.00 USD | 9,200,000.00 USD | 80,470.00 USD | 27,130.00 USD | 93,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 11,750,000.00 USD | 11,750,000.00 USD | 256,610.00 USD | 5,150.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9375` | 454.59 USD | 16,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9380` | 9,270,000.00 USD | 9,270,000.00 USD | 15,820.00 USD | 9,440.00 USD | 43,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 43,080.00 USD | 59,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9390` | 9,310,000.00 USD | 9,310,000.00 USD | 3,150.00 USD | 3,270.00 USD | 34,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 12,140,000.00 USD | 12,140,000.00 USD | 86,850.00 USD | 36,340.00 USD | 266,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 9,420,000.00 USD | 9,420,000.00 USD | 47,250.00 USD | 2,660.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9405` | 6,380.00 USD | 65,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9410` | 9,450,000.00 USD | 9,450,000.00 USD | 20,430.00 USD | 15,760.00 USD | 616.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 12,280,000.00 USD | 12,280,000.00 USD | 128,480.00 USD | 8,510.00 USD | 4,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 9,490,000.00 USD | 9,490,000.00 USD | 7,430.00 USD | 1,870.00 USD | 24,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 9,500,000.00 USD | 9,500,000.00 USD | 5,380.00 USD | 2,520.00 USD | 26.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 12,400,000.00 USD | 12,400,000.00 USD | 15,490.00 USD | 70,360.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 9,570,000.00 USD | 9,570,000.00 USD | 5,140.00 USD | 23,770.00 USD | 46,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9445` | 511.64 USD | 66,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9450` | 9,620,000.00 USD | 9,620,000.00 USD | 4,850.00 USD | 1,000.00 USD | 47,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 12,740,000.00 USD | 12,740,000.00 USD | 3,360.00 USD | 244,270.00 USD | 94,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 9,730,000.00 USD | 9,730,000.00 USD | 56,940.00 USD | 26,210.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 9,810,000.00 USD | 9,810,000.00 USD | 36,440.00 USD | 24,890.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 212,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9475` | 1,720.00 USD | 67,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9480` | 9,950,000.00 USD | 9,950,000.00 USD | 55,350.00 USD | 48,320.00 USD | 35,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 10,010,000.00 USD | 10,010,000.00 USD | 19,060.00 USD | 15,420.00 USD | 22,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 13,180,000.00 USD | 13,180,000.00 USD | 2,500.00 USD | 108,270.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 10,090,000.00 USD | 10,090,000.00 USD | 8,330.00 USD | 22,290.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 10,300,000.00 USD | 10,300,000.00 USD | 53,450.00 USD | 28,930.00 USD | 128,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 14,010,000.00 USD | 14,010,000.00 USD | 2,840.00 USD | 88,970.00 USD | 734,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 10,370,000.00 USD | 10,370,000.00 USD | 466.70 USD | 332.24 USD | 72,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 10,500,000.00 USD | 10,500,000.00 USD | 29,490.00 USD | 27,260.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 10,580,000.00 USD | 10,580,000.00 USD | 27,930.00 USD | 21,440.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 10,640,000.00 USD | 10,640,000.00 USD | 21,030.00 USD | 13,800.00 USD | 24,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 14,150,000.00 USD | 14,150,000.00 USD | 77,110.00 USD | 2,400.00 USD | 62,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 10,690,000.00 USD | 10,690,000.00 USD | 20,640.00 USD | 11,590.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 10,710,000.00 USD | 10,710,000.00 USD | 16,640.00 USD | 2,570.00 USD | 533.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 14,620,000.00 USD | 14,620,000.00 USD | 463,830.00 USD | 4,720.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 10,760,000.00 USD | 10,760,000.00 USD | 10,110.00 USD | 23,670.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 10,820,000.00 USD | 10,820,000.00 USD | 33,840.00 USD | 26,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 15,210,000.00 USD | 15,210,000.00 USD | 563,790.00 USD | 21,410.00 USD | 3,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 10,980,000.00 USD | 10,980,000.00 USD | 55,860.00 USD | 23,730.00 USD | 78,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 11,300,000.00 USD | 11,300,000.00 USD | 108,340.00 USD | 51,860.00 USD | 166,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 16,590,000.00 USD | 16,590,000.00 USD | 698,570.00 USD | 201,530.00 USD | 480,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 11,430,000.00 USD | 11,430,000.00 USD | 107,150.00 USD | 13,840.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 11,560,000.00 USD | 11,560,000.00 USD | 85,660.00 USD | 15,720.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 18,100,000.00 USD | 18,100,000.00 USD | 579,300.00 USD | 301,610.00 USD | 624,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 11,730,000.00 USD | 11,730,000.00 USD | 108,050.00 USD | 39,580.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9645` | 1,580.00 USD | 69,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9650` | 11,850,000.00 USD | 11,850,000.00 USD | 18,450.00 USD | 72,700.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 19,680,000.00 USD | 19,680,000.00 USD | 857,470.00 USD | 312,610.00 USD | 408,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 12,080,000.00 USD | 12,080,000.00 USD | 135,020.00 USD | 55,700.00 USD | 42,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 12,420,000.00 USD | 12,420,000.00 USD | 93,370.00 USD | 53,420.00 USD | 191,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 21,510,000.00 USD | 21,510,000.00 USD | 763,290.00 USD | 555,340.00 USD | 508,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 12,630,000.00 USD | 12,630,000.00 USD | 85,180.00 USD | 13,070.00 USD | 112,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 13,000,000.00 USD | 13,000,000.00 USD | 166,870.00 USD | 72,380.00 USD | 130,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 22,750,000.00 USD | 22,750,000.00 USD | 558,600.00 USD | 291,960.00 USD | 398,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 13,220,000.00 USD | 13,220,000.00 USD | 120,570.00 USD | 38,730.00 USD | 65,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 13,390,000.00 USD | 13,390,000.00 USD | 66,850.00 USD | 27,000.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 23,810,000.00 USD | 23,810,000.00 USD | 573,060.00 USD | 319,680.00 USD | 159,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 13,530,000.00 USD | 13,530,000.00 USD | 45,860.00 USD | 36,780.00 USD | 55,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 13,550,000.00 USD | 13,550,000.00 USD | 24,020.00 USD | 679.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 24,620,000.00 USD | 24,620,000.00 USD | 458,870.00 USD | 161,170.00 USD | 192,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 13,620,000.00 USD | 13,620,000.00 USD | 15,050.00 USD | 6,020.00 USD | 47,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 13,770,000.00 USD | 13,770,000.00 USD | 24,670.00 USD | 32,410.00 USD | 91,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 25,360,000.00 USD | 25,360,000.00 USD | 227,380.00 USD | 293,590.00 USD | 223,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9755` | 3,590.00 USD | 72,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 13,780,000.00 USD | 13,780,000.00 USD | 7,490.00 USD | 290.18 USD | 296.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 13,830,000.00 USD | 13,830,000.00 USD | 4,370.00 USD | 22,640.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 26,440,000.00 USD | 26,440,000.00 USD | 329,170.00 USD | 218,820.00 USD | 525,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 13,970,000.00 USD | 13,970,000.00 USD | 38,720.00 USD | 25,310.00 USD | 75,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 14,060,000.00 USD | 14,060,000.00 USD | 30,700.00 USD | 19,870.00 USD | 37,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 27,040,000.00 USD | 27,040,000.00 USD | 271,900.00 USD | 86,630.00 USD | 244,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 14,220,000.00 USD | 14,220,000.00 USD | 43,770.00 USD | 32,410.00 USD | 81,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 74,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 14,290,000.00 USD | 14,290,000.00 USD | 56,460.00 USD | 14,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 27,510,000.00 USD | 27,510,000.00 USD | 206,910.00 USD | 86,870.00 USD | 176,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 14,350,000.00 USD | 14,350,000.00 USD | 37,790.00 USD | 14,300.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 14,400,000.00 USD | 14,400,000.00 USD | 31,260.00 USD | 21,460.00 USD | 47.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 28,100,000.00 USD | 28,100,000.00 USD | 262,900.00 USD | 128,370.00 USD | 200,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 14,430,000.00 USD | 14,430,000.00 USD | 2,310.00 USD | 22,540.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 14,490,000.00 USD | 14,490,000.00 USD | 23,370.00 USD | 19,710.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 28,510,000.00 USD | 28,510,000.00 USD | 235,580.00 USD | 58,210.00 USD | 118,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 14,650,000.00 USD | 14,650,000.00 USD | 51,980.00 USD | 24,120.00 USD | 81,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 74,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9870` | 14,700,000.00 USD | 14,700,000.00 USD | 27,800.00 USD | 7,430.00 USD | 16,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 29,020,000.00 USD | 29,020,000.00 USD | 248,980.00 USD | 203,100.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 14,790,000.00 USD | 14,790,000.00 USD | 50,330.00 USD | 11,470.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 78,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9890` | 29,320,000.00 USD | 29,320,000.00 USD | 194,850.00 USD | 78,280.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 29,690,000.00 USD | 29,690,000.00 USD | 198,890.00 USD | 89,640.00 USD | 84,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9915` | 1,570.00 USD | 80,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 30,050,000.00 USD | 30,050,000.00 USD | 228,340.00 USD | 63,950.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 80,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9950` | 30,370,000.00 USD | 30,370,000.00 USD | 48,120.00 USD | 138,500.00 USD | 125,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 31,020,000.00 USD | 31,020,000.00 USD | 215,040.00 USD | 81,210.00 USD | 360,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 31,310,000.00 USD | 31,310,000.00 USD | 145,170.00 USD | 35,870.00 USD | 101,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,600,000.00 USD | 31,600,000.00 USD | 196,410.00 USD | 50,130.00 USD | 52,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 80,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,710,000.00 USD | 31,710,000.00 USD | 101,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 705.99 USD | 81,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 81,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.03` | 11,040.00 USD | 92,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 278.90 USD | 92,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 93,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 95,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 105.25 USD | 95,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 99,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 105,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 105,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 105,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 8,940.00 USD | 114,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 137,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 138,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 129.88 USD | 138,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 215.17 USD | 138,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 177.65 USD | 139,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 143,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 383.01 USD | 143,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 144,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 3,930.00 USD | 148,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 4,830.00 USD | 153,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 155,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.27` | 9,700.00 USD | 165,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 1,050.00 USD | 166,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 168,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 208,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 126.24 USD | 208,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 209,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 209,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 210,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 24,040.00 USD | 234,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 7,490.00 USD | 241,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 248,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 270,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 276,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 635,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 639,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 640,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 640,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 16,390.00 USD | 656,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 258,720.00 USD | 915,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 151.25 USD | 915,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 919,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 9,920.00 USD | 929,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 929,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 76,120.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 116.82 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 17,870.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,180.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 123.81 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,130.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 2,250.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 3,940.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,020.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 3,620.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 150.02 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 485.78 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 174.03 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 9,630.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 903.10 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,860.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 12,410.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 782.21 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1885` | 4,670,000.00 USD | 0.00 USD | 188.50 USD | `-78.93%` | `1,000.00` |
| `Live` | `Long` | `0.1905` | 4,670,000.00 USD | 0.00 USD | 2,710.00 USD | `-78.71%` | `14,245.00` |
| `Live` | `Long` | `0.1935` | 4,660,000.00 USD | 0.00 USD | 414.21 USD | `-78.37%` | `2,140.60` |
| `Live` | `Long` | `0.1975` | 4,660,000.00 USD | 0.00 USD | 132.80 USD | `-77.92%` | `672.40` |
| `Live` | `Long` | `0.1995` | 4,660,000.00 USD | 0.00 USD | 256.00 USD | `-77.70%` | `1,283.20` |
| `Live` | `Long` | `0.2225` | 4,660,000.00 USD | 0.00 USD | 1,500.00 USD | `-75.13%` | `6,725.00` |
| `Live` | `Long` | `0.2355` | 4,660,000.00 USD | 0.00 USD | 789.66 USD | `-73.68%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,660,000.00 USD | 0.00 USD | 156.36 USD | `-73.34%` | `655.60` |
| `Live` | `Long` | `0.2445` | 4,660,000.00 USD | 0.00 USD | 4,630.00 USD | `-72.67%` | `18,919.90` |
| `Live` | `Long` | `0.2485` | 4,660,000.00 USD | 0.00 USD | 2,670.00 USD | `-72.22%` | `10,749.20` |
| `Live` | `Long` | `0.2535` | 4,650,000.00 USD | 0.00 USD | 2,260.00 USD | `-71.66%` | `8,897.00` |
| `Live` | `Long` | `0.2595` | 4,650,000.00 USD | 0.00 USD | 160.42 USD | `-70.99%` | `618.20` |
| `Live` | `Long` | `0.2625` | 4,650,000.00 USD | 0.00 USD | 849.48 USD | `-70.66%` | `3,236.10` |
| `Live` | `Long` | `0.2635` | 4,650,000.00 USD | 0.00 USD | 171.12 USD | `-70.55%` | `649.40` |
| `Live` | `Long` | `0.2685` | 4,650,000.00 USD | 0.00 USD | 106.16 USD | `-69.99%` | `395.40` |
| `Live` | `Long` | `0.2735` | 4,650,000.00 USD | 0.00 USD | 248.34 USD | `-69.43%` | `908.00` |
| `Live` | `Long` | `0.2785` | 4,650,000.00 USD | 0.00 USD | 278.50 USD | `-68.87%` | `1,000.00` |
| `Live` | `Long` | `0.2855` | 4,650,000.00 USD | 0.00 USD | 3,480.00 USD | `-68.09%` | `12,176.00` |
| `Live` | `Long` | `0.2885` | 4,650,000.00 USD | 0.00 USD | 53,920.00 USD | `-67.75%` | `186,885.80` |
| `Live` | `Long` | `0.2945` | 4,590,000.00 USD | 0.00 USD | 3,860.00 USD | `-67.08%` | `13,104.40` |
| `Live` | `Long` | `0.2955` | 4,590,000.00 USD | 0.00 USD | 282.73 USD | `-66.97%` | `956.80` |
| `Live` | `Long` | `0.2975` | 4,590,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.75%` | `14,561.30` |
| `Live` | `Long` | `0.3115` | 4,580,000.00 USD | 0.00 USD | 270.38 USD | `-65.18%` | `868.00` |
| `Live` | `Long` | `0.3125` | 4,580,000.00 USD | 0.00 USD | 110.53 USD | `-65.07%` | `353.70` |
| `Live` | `Long` | `0.3165` | 4,580,000.00 USD | 0.00 USD | 104.73 USD | `-64.62%` | `330.90` |
| `Live` | `Long` | `0.3295` | 4,580,000.00 USD | 0.00 USD | 25,600.00 USD | `-63.17%` | `77,706.40` |
| `Live` | `Long` | `0.3375` | 4,560,000.00 USD | 0.00 USD | 9,610.00 USD | `-62.28%` | `28,480.20` |
| `Live` | `Long` | `0.3425` | 4,550,000.00 USD | 0.00 USD | 3,430.00 USD | `-61.72%` | `10,000.00` |
| `Live` | `Long` | `0.3465` | 4,540,000.00 USD | 0.00 USD | 5,070.00 USD | `-61.27%` | `14,633.20` |
| `Live` | `Long` | `0.3505` | 4,540,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.82%` | `2,908.00` |
| `Live` | `Long` | `0.3585` | 4,540,000.00 USD | 0.00 USD | 595.72 USD | `-59.93%` | `1,661.70` |
| `Live` | `Long` | `0.3635` | 4,540,000.00 USD | 0.00 USD | 405.34 USD | `-59.37%` | `1,115.10` |
| `Live` | `Long` | `0.3665` | 4,540,000.00 USD | 0.00 USD | 274.88 USD | `-59.03%` | `750.00` |
| `Live` | `Long` | `0.3685` | 4,540,000.00 USD | 0.00 USD | 4,610.00 USD | `-58.81%` | `12,500.00` |
| `Live` | `Long` | `0.3735` | 4,530,000.00 USD | 0.00 USD | 6,350.00 USD | `-58.25%` | `17,000.00` |
| `Live` | `Long` | `0.3795` | 4,530,000.00 USD | 0.00 USD | 278.02 USD | `-57.58%` | `732.60` |
| `Live` | `Long` | `0.3845` | 4,530,000.00 USD | 0.00 USD | 3,860.00 USD | `-57.02%` | `10,043.40` |
| `Live` | `Long` | `0.3895` | 4,520,000.00 USD | 0.00 USD | 3,260.00 USD | `-56.46%` | `8,361.70` |
| `Live` | `Long` | `0.3925` | 4,520,000.00 USD | 0.00 USD | 5,030.00 USD | `-56.13%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,510,000.00 USD | 0.00 USD | 754.48 USD | `-55.90%` | `1,912.50` |
| `Live` | `Long` | `0.4035` | 4,510,000.00 USD | 0.00 USD | 935.03 USD | `-54.90%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,510,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.79%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,510,000.00 USD | 0.00 USD | 3,360.00 USD | `-54.56%` | `8,275.50` |
| `Live` | `Long` | `0.4085` | 4,500,000.00 USD | 0.00 USD | 740.57 USD | `-54.34%` | `1,812.90` |
| `Live` | `Long` | `0.4155` | 4,500,000.00 USD | 0.00 USD | 732.11 USD | `-53.56%` | `1,762.00` |
| `Live` | `Long` | `0.4205` | 4,500,000.00 USD | 0.00 USD | 29,430.00 USD | `-53.00%` | `70,000.00` |
| `Live` | `Long` | `0.4215` | 4,470,000.00 USD | 0.00 USD | 3,930.00 USD | `-52.89%` | `9,320.00` |
| `Live` | `Long` | `0.4245` | 4,470,000.00 USD | 0.00 USD | 8,960.00 USD | `-52.55%` | `21,103.90` |
| `Live` | `Long` | `0.4335` | 4,460,000.00 USD | 0.00 USD | 367.52 USD | `-51.54%` | `847.80` |
| `Live` | `Long` | `0.4385` | 4,460,000.00 USD | 0.00 USD | 122.91 USD | `-50.99%` | `280.30` |
| `Live` | `Long` | `0.4425` | 4,460,000.00 USD | 0.00 USD | 44,080.00 USD | `-50.54%` | `99,611.70` |
| `Live` | `Long` | `0.4435` | 4,410,000.00 USD | 0.00 USD | 219.00 USD | `-50.43%` | `493.80` |
| `Live` | `Long` | `0.4455` | 4,410,000.00 USD | 0.00 USD | 574.83 USD | `-50.20%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,410,000.00 USD | 0.00 USD | 19,600.00 USD | `-50.09%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,390,000.00 USD | 0.00 USD | 105.25 USD | `-49.98%` | `235.20` |
| `Live` | `Long` | `0.4505` | 4,390,000.00 USD | 0.00 USD | 6,110.00 USD | `-49.64%` | `13,552.00` |
| `Live` | `Long` | `0.4525` | 4,390,000.00 USD | 0.00 USD | 316.75 USD | `-49.42%` | `700.00` |
| `Live` | `Long` | `0.4535` | 4,390,000.00 USD | 0.00 USD | 1,020.00 USD | `-49.31%` | `2,246.80` |
| `Live` | `Long` | `0.4595` | 4,390,000.00 USD | 0.00 USD | 3,330.00 USD | `-48.64%` | `7,245.50` |
| `Live` | `Long` | `0.4705` | 4,380,000.00 USD | 0.00 USD | 9,230.00 USD | `-47.41%` | `19,627.90` |
| `Live` | `Long` | `0.4775` | 4,370,000.00 USD | 0.00 USD | 252.69 USD | `-46.63%` | `529.20` |
| `Live` | `Long` | `0.4785` | 4,370,000.00 USD | 0.00 USD | 110.10 USD | `-46.51%` | `230.10` |
| `Live` | `Long` | `0.4825` | 4,370,000.00 USD | 0.00 USD | 166.70 USD | `-46.07%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,370,000.00 USD | 0.00 USD | 174.01 USD | `-45.96%` | `359.90` |
| `Live` | `Long` | `0.4845` | 4,370,000.00 USD | 0.00 USD | 3,540.00 USD | `-45.84%` | `7,307.20` |
| `Live` | `Long` | `0.4855` | 4,370,000.00 USD | 0.00 USD | 536.96 USD | `-45.73%` | `1,106.00` |
| `Live` | `Long` | `0.4865` | 4,370,000.00 USD | 0.00 USD | 201.07 USD | `-45.62%` | `413.30` |
| `Live` | `Long` | `0.4885` | 4,370,000.00 USD | 0.00 USD | 5,520.00 USD | `-45.40%` | `11,290.30` |
| `Live` | `Long` | `0.4895` | 4,360,000.00 USD | 0.00 USD | 105.34 USD | `-45.29%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,360,000.00 USD | 0.00 USD | 2,380.00 USD | `-45.06%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 4,360,000.00 USD | 0.00 USD | 106.32 USD | `-44.73%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,360,000.00 USD | 0.00 USD | 211.88 USD | `-44.61%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,360,000.00 USD | 0.00 USD | 216.75 USD | `-44.28%` | `434.80` |
| `Live` | `Long` | `0.5005` | 4,360,000.00 USD | 0.00 USD | 5,280.00 USD | `-44.06%` | `10,552.10` |
| `Live` | `Long` | `0.5015` | 4,350,000.00 USD | 0.00 USD | 475.07 USD | `-43.94%` | `947.30` |
| `Live` | `Long` | `0.5025` | 4,350,000.00 USD | 0.00 USD | 1,230.00 USD | `-43.83%` | `2,451.10` |
| `Live` | `Long` | `0.5035` | 4,350,000.00 USD | 0.00 USD | 1,390.00 USD | `-43.72%` | `2,751.80` |
| `Live` | `Long` | `0.5055` | 4,350,000.00 USD | 0.00 USD | 211.25 USD | `-43.50%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,350,000.00 USD | 0.00 USD | 76,870.00 USD | `-43.16%` | `151,163.80` |
| `Live` | `Long` | `0.5095` | 4,270,000.00 USD | 0.00 USD | 195.75 USD | `-43.05%` | `384.20` |
| `Live` | `Long` | `0.5115` | 4,270,000.00 USD | 0.00 USD | 228.38 USD | `-42.83%` | `446.50` |
| `Live` | `Long` | `0.5155` | 4,270,000.00 USD | 0.00 USD | 106.04 USD | `-42.38%` | `205.70` |
| `Live` | `Long` | `0.5165` | 4,270,000.00 USD | 0.00 USD | 619.80 USD | `-42.27%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,270,000.00 USD | 0.00 USD | 213.68 USD | `-42.16%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,270,000.00 USD | 0.00 USD | 1,110.00 USD | `-42.04%` | `2,131.90` |
| `Live` | `Long` | `0.5275` | 4,270,000.00 USD | 0.00 USD | 348.36 USD | `-41.04%` | `660.40` |
| `Live` | `Long` | `0.5285` | 4,270,000.00 USD | 0.00 USD | 123,140.00 USD | `-40.93%` | `233,000.00` |
| `Live` | `Long` | `0.5295` | 4,150,000.00 USD | 0.00 USD | 1,610.00 USD | `-40.81%` | `3,043.40` |
| `Live` | `Long` | `0.5305` | 4,150,000.00 USD | 0.00 USD | 264.56 USD | `-40.70%` | `498.70` |
| `Live` | `Long` | `0.5325` | 4,150,000.00 USD | 0.00 USD | 10,460.00 USD | `-40.48%` | `19,642.00` |
| `Live` | `Long` | `0.5355` | 4,140,000.00 USD | 0.00 USD | 113.47 USD | `-40.14%` | `211.90` |
| `Live` | `Long` | `0.5395` | 4,140,000.00 USD | 0.00 USD | 126.46 USD | `-39.70%` | `234.40` |
| `Live` | `Long` | `0.5405` | 4,140,000.00 USD | 0.00 USD | 7,090.00 USD | `-39.58%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,130,000.00 USD | 0.00 USD | 269.13 USD | `-39.36%` | `496.10` |
| `Live` | `Long` | `0.5435` | 4,130,000.00 USD | 0.00 USD | 5,900.00 USD | `-39.25%` | `10,862.70` |
| `Live` | `Long` | `0.5445` | 4,120,000.00 USD | 0.00 USD | 230.32 USD | `-39.14%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,120,000.00 USD | 0.00 USD | 272.87 USD | `-38.91%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,120,000.00 USD | 0.00 USD | 1,240.00 USD | `-38.80%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,120,000.00 USD | 0.00 USD | 1,310.00 USD | `-38.58%` | `2,392.10` |
| `Live` | `Long` | `0.5505` | 4,120,000.00 USD | 0.00 USD | 27,770.00 USD | `-38.47%` | `50,450.60` |
| `Live` | `Long` | `0.5515` | 4,090,000.00 USD | 0.00 USD | 160.93 USD | `-38.36%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,090,000.00 USD | 0.00 USD | 582.56 USD | `-38.24%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,090,000.00 USD | 0.00 USD | 271.88 USD | `-38.13%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,090,000.00 USD | 0.00 USD | 531.60 USD | `-38.02%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,090,000.00 USD | 0.00 USD | 7,950.00 USD | `-37.91%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,080,000.00 USD | 0.00 USD | 141.97 USD | `-37.57%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,080,000.00 USD | 0.00 USD | 304.93 USD | `-37.46%` | `545.00` |
| `Live` | `Long` | `0.5615` | 4,080,000.00 USD | 0.00 USD | 950.84 USD | `-37.24%` | `1,693.40` |
| `Live` | `Long` | `0.5625` | 4,080,000.00 USD | 0.00 USD | 330.53 USD | `-37.13%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,080,000.00 USD | 0.00 USD | 1,480.00 USD | `-37.01%` | `2,623.90` |
| `Live` | `Long` | `0.5655` | 4,080,000.00 USD | 0.00 USD | 8,190.00 USD | `-36.79%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,070,000.00 USD | 0.00 USD | 7,200.00 USD | `-36.68%` | `12,714.00` |
| `Live` | `Long` | `0.5675` | 4,060,000.00 USD | 0.00 USD | 1,560.00 USD | `-36.57%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,060,000.00 USD | 0.00 USD | 973.22 USD | `-36.34%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,060,000.00 USD | 0.00 USD | 6,330.00 USD | `-36.01%` | `11,048.50` |
| `Live` | `Long` | `0.5735` | 4,050,000.00 USD | 0.00 USD | 109,930.00 USD | `-35.90%` | `191,690.40` |
| `Live` | `Long` | `0.5745` | 3,950,000.00 USD | 0.00 USD | 485.51 USD | `-35.78%` | `845.10` |
| `Live` | `Long` | `0.5755` | 3,940,000.00 USD | 0.00 USD | 217.37 USD | `-35.67%` | `377.70` |
| `Live` | `Long` | `0.5765` | 3,940,000.00 USD | 0.00 USD | 1,150.00 USD | `-35.56%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 3,940,000.00 USD | 0.00 USD | 497.75 USD | `-35.45%` | `861.90` |
| `Live` | `Long` | `0.5795` | 3,940,000.00 USD | 0.00 USD | 212.85 USD | `-35.23%` | `367.30` |
| `Live` | `Long` | `0.5805` | 3,940,000.00 USD | 0.00 USD | 1,410.00 USD | `-35.11%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 3,940,000.00 USD | 0.00 USD | 6,470.00 USD | `-34.89%` | `11,099.00` |
| `Live` | `Long` | `0.5845` | 3,930,000.00 USD | 0.00 USD | 269.98 USD | `-34.67%` | `461.90` |
| `Live` | `Long` | `0.5855` | 3,930,000.00 USD | 0.00 USD | 2,280.00 USD | `-34.55%` | `3,901.10` |
| `Live` | `Long` | `0.5865` | 3,930,000.00 USD | 0.00 USD | 822.98 USD | `-34.44%` | `1,403.20` |
| `Live` | `Long` | `0.5875` | 3,930,000.00 USD | 0.00 USD | 176.25 USD | `-34.33%` | `300.00` |
| `Live` | `Long` | `0.5885` | 3,930,000.00 USD | 0.00 USD | 311.14 USD | `-34.22%` | `528.70` |
| `Live` | `Long` | `0.5905` | 3,930,000.00 USD | 0.00 USD | 225.93 USD | `-34.00%` | `382.60` |
| `Live` | `Long` | `0.5935` | 3,930,000.00 USD | 0.00 USD | 1,130.00 USD | `-33.66%` | `1,901.00` |
| `Live` | `Long` | `0.5945` | 3,930,000.00 USD | 0.00 USD | 8,220.00 USD | `-33.55%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 3,920,000.00 USD | 0.00 USD | 608.61 USD | `-33.33%` | `1,020.30` |
| `Live` | `Long` | `0.5975` | 3,920,000.00 USD | 0.00 USD | 3,420.00 USD | `-33.21%` | `5,729.40` |
| `Live` | `Long` | `0.5985` | 3,920,000.00 USD | 0.00 USD | 299.25 USD | `-33.10%` | `500.00` |
| `Live` | `Long` | `0.5995` | 3,920,000.00 USD | 0.00 USD | 4,610.00 USD | `-32.99%` | `7,683.30` |
| `Live` | `Long` | `0.6005` | 3,910,000.00 USD | 0.00 USD | 351.11 USD | `-32.88%` | `584.70` |
| `Live` | `Long` | `0.6015` | 3,910,000.00 USD | 0.00 USD | 3,030.00 USD | `-32.77%` | `5,038.30` |
| `Live` | `Long` | `0.6025` | 3,910,000.00 USD | 0.00 USD | 113,380.00 USD | `-32.65%` | `188,177.10` |
| `Live` | `Long` | `0.6075` | 3,800,000.00 USD | 0.00 USD | 699.84 USD | `-32.10%` | `1,152.00` |
| `Live` | `Long` | `0.6085` | 3,790,000.00 USD | 0.00 USD | 1,040.00 USD | `-31.98%` | `1,705.10` |
| `Live` | `Long` | `0.6095` | 3,790,000.00 USD | 0.00 USD | 214.54 USD | `-31.87%` | `352.00` |
| `Live` | `Long` | `0.6115` | 3,790,000.00 USD | 0.00 USD | 6,280.00 USD | `-31.65%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 3,790,000.00 USD | 0.00 USD | 438.73 USD | `-31.54%` | `716.30` |
| `Live` | `Long` | `0.6145` | 3,790,000.00 USD | 0.00 USD | 2,110.00 USD | `-31.31%` | `3,435.00` |
| `Live` | `Long` | `0.6155` | 3,780,000.00 USD | 0.00 USD | 935.13 USD | `-31.20%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 3,780,000.00 USD | 0.00 USD | 44,470.00 USD | `-31.09%` | `72,130.30` |
| `Live` | `Long` | `0.6175` | 3,740,000.00 USD | 0.00 USD | 4,980.00 USD | `-30.98%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 3,730,000.00 USD | 0.00 USD | 12,570.00 USD | `-30.87%` | `20,327.90` |
| `Live` | `Long` | `0.6195` | 3,720,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.75%` | `3,868.00` |
| `Live` | `Long` | `0.6225` | 3,720,000.00 USD | 0.00 USD | 708.53 USD | `-30.42%` | `1,138.20` |
| `Live` | `Long` | `0.6245` | 3,720,000.00 USD | 0.00 USD | 356.65 USD | `-30.20%` | `571.10` |
| `Live` | `Long` | `0.6255` | 3,720,000.00 USD | 0.00 USD | 34,160.00 USD | `-30.08%` | `54,611.90` |
| `Live` | `Long` | `0.6285` | 3,680,000.00 USD | 0.00 USD | 102.45 USD | `-29.75%` | `163.00` |
| `Live` | `Long` | `0.6295` | 3,680,000.00 USD | 0.00 USD | 1,100.00 USD | `-29.64%` | `1,739.60` |
| `Live` | `Long` | `0.6305` | 3,680,000.00 USD | 0.00 USD | 949.85 USD | `-29.52%` | `1,506.50` |
| `Live` | `Long` | `0.6315` | 3,680,000.00 USD | 0.00 USD | 2,130.00 USD | `-29.41%` | `3,368.50` |
| `Live` | `Long` | `0.6345` | 3,680,000.00 USD | 0.00 USD | 1,690.00 USD | `-29.08%` | `2,658.10` |
| `Live` | `Long` | `0.6365` | 3,680,000.00 USD | 0.00 USD | 3,060.00 USD | `-28.85%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,680,000.00 USD | 0.00 USD | 1,100.00 USD | `-28.74%` | `1,726.70` |
| `Live` | `Long` | `0.6405` | 3,670,000.00 USD | 0.00 USD | 34,650.00 USD | `-28.41%` | `54,099.10` |
| `Live` | `Long` | `0.6415` | 3,640,000.00 USD | 0.00 USD | 588.32 USD | `-28.30%` | `917.10` |
| `Live` | `Long` | `0.6425` | 3,640,000.00 USD | 0.00 USD | 86,950.00 USD | `-28.18%` | `135,323.30` |
| `Live` | `Long` | `0.6435` | 3,550,000.00 USD | 0.00 USD | 3,190.00 USD | `-28.07%` | `4,951.30` |
| `Live` | `Long` | `0.6445` | 3,550,000.00 USD | 0.00 USD | 65,790.00 USD | `-27.96%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,480,000.00 USD | 0.00 USD | 14,590.00 USD | `-27.85%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,470,000.00 USD | 0.00 USD | 146.76 USD | `-27.74%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,470,000.00 USD | 0.00 USD | 2,810.00 USD | `-27.62%` | `4,340.10` |
| `Live` | `Long` | `0.6485` | 3,470,000.00 USD | 0.00 USD | 1,060.00 USD | `-27.51%` | `1,635.60` |
| `Live` | `Long` | `0.6495` | 3,460,000.00 USD | 0.00 USD | 344.82 USD | `-27.40%` | `530.90` |
| `Live` | `Long` | `0.6505` | 3,460,000.00 USD | 0.00 USD | 106.75 USD | `-27.29%` | `164.10` |
| `Live` | `Long` | `0.6515` | 3,460,000.00 USD | 0.00 USD | 403,320.00 USD | `-27.18%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,060,000.00 USD | 0.00 USD | 2,350.00 USD | `-27.07%` | `3,599.00` |
| `Live` | `Long` | `0.6535` | 3,060,000.00 USD | 0.00 USD | 3,990.00 USD | `-26.95%` | `6,107.40` |
| `Live` | `Long` | `0.6545` | 3,050,000.00 USD | 0.00 USD | 6,700.00 USD | `-26.84%` | `10,231.40` |
| `Live` | `Long` | `0.6555` | 3,050,000.00 USD | 0.00 USD | 676.54 USD | `-26.73%` | `1,032.10` |
| `Live` | `Long` | `0.6565` | 3,050,000.00 USD | 0.00 USD | 7,070.00 USD | `-26.62%` | `10,764.20` |
| `Live` | `Long` | `0.6575` | 3,040,000.00 USD | 0.00 USD | 130.91 USD | `-26.51%` | `199.10` |
| `Live` | `Long` | `0.6585` | 3,040,000.00 USD | 0.00 USD | 16,140.00 USD | `-26.39%` | `24,507.30` |
| `Live` | `Long` | `0.6595` | 3,020,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.28%` | `1,611.70` |
| `Live` | `Long` | `0.6605` | 3,020,000.00 USD | 0.00 USD | 184.35 USD | `-26.17%` | `279.10` |
| `Live` | `Long` | `0.6615` | 3,020,000.00 USD | 0.00 USD | 15,600.00 USD | `-26.06%` | `23,580.30` |
| `Live` | `Long` | `0.6625` | 3,010,000.00 USD | 0.00 USD | 1,400.00 USD | `-25.95%` | `2,106.70` |
| `Live` | `Long` | `0.6645` | 3,010,000.00 USD | 0.00 USD | 448.54 USD | `-25.72%` | `675.00` |
| `Live` | `Long` | `0.6655` | 3,000,000.00 USD | 0.00 USD | 2,290.00 USD | `-25.61%` | `3,440.40` |
| `Live` | `Long` | `0.6665` | 3,000,000.00 USD | 0.00 USD | 728.68 USD | `-25.50%` | `1,093.30` |
| `Live` | `Long` | `0.6675` | 3,000,000.00 USD | 0.00 USD | 2,260.00 USD | `-25.39%` | `3,386.00` |
| `Live` | `Long` | `0.6685` | 3,000,000.00 USD | 0.00 USD | 5,470.00 USD | `-25.28%` | `8,188.90` |
| `Live` | `Long` | `0.6695` | 2,990,000.00 USD | 0.00 USD | 273.16 USD | `-25.17%` | `408.00` |
| `Live` | `Long` | `0.6705` | 2,990,000.00 USD | 0.00 USD | 2,630.00 USD | `-25.05%` | `3,915.40` |
| `Live` | `Long` | `0.6715` | 2,990,000.00 USD | 0.00 USD | 29,210.00 USD | `-24.94%` | `43,496.00` |
| `Live` | `Long` | `0.6725` | 2,960,000.00 USD | 0.00 USD | 1,280.00 USD | `-24.83%` | `1,906.60` |
| `Live` | `Long` | `0.6735` | 2,960,000.00 USD | 0.00 USD | 633.09 USD | `-24.72%` | `940.00` |
| `Live` | `Long` | `0.6745` | 2,960,000.00 USD | 0.00 USD | 6,520.00 USD | `-24.61%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 2,950,000.00 USD | 0.00 USD | 111.59 USD | `-24.49%` | `165.20` |
| `Live` | `Long` | `0.6765` | 2,950,000.00 USD | 0.00 USD | 744.15 USD | `-24.38%` | `1,100.00` |
| `Live` | `Long` | `0.6775` | 2,950,000.00 USD | 0.00 USD | 2,370.00 USD | `-24.27%` | `3,500.00` |
| `Live` | `Long` | `0.6785` | 2,950,000.00 USD | 0.00 USD | 122.94 USD | `-24.16%` | `181.20` |
| `Live` | `Long` | `0.6795` | 2,950,000.00 USD | 0.00 USD | 39,510.00 USD | `-24.05%` | `58,139.50` |
| `Live` | `Long` | `0.6805` | 2,910,000.00 USD | 0.00 USD | 4,150.00 USD | `-23.94%` | `6,099.00` |
| `Live` | `Long` | `0.6825` | 2,910,000.00 USD | 0.00 USD | 19,300.00 USD | `-23.71%` | `28,284.70` |
| `Live` | `Long` | `0.6835` | 2,890,000.00 USD | 0.00 USD | 11,170.00 USD | `-23.60%` | `16,336.60` |
| `Live` | `Long` | `0.6845` | 2,880,000.00 USD | 0.00 USD | 2,430.00 USD | `-23.49%` | `3,554.60` |
| `Live` | `Long` | `0.6855` | 2,870,000.00 USD | 0.00 USD | 4,290.00 USD | `-23.38%` | `6,259.00` |
| `Live` | `Long` | `0.6865` | 2,870,000.00 USD | 0.00 USD | 112.59 USD | `-23.27%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,870,000.00 USD | 0.00 USD | 6,110.00 USD | `-23.15%` | `8,883.90` |
| `Live` | `Long` | `0.6895` | 2,860,000.00 USD | 0.00 USD | 2,110.00 USD | `-22.93%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,860,000.00 USD | 0.00 USD | 3,360.00 USD | `-22.82%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,860,000.00 USD | 0.00 USD | 8,970.00 USD | `-22.71%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 2,850,000.00 USD | 0.00 USD | 7,690.00 USD | `-22.48%` | `11,084.70` |
| `Live` | `Long` | `0.6945` | 2,840,000.00 USD | 0.00 USD | 722.28 USD | `-22.37%` | `1,040.00` |
| `Live` | `Long` | `0.6955` | 2,840,000.00 USD | 0.00 USD | 1,700.00 USD | `-22.26%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,840,000.00 USD | 0.00 USD | 16,070.00 USD | `-22.15%` | `23,074.60` |
| `Live` | `Long` | `0.6975` | 2,820,000.00 USD | 0.00 USD | 1,820.00 USD | `-22.04%` | `2,608.70` |
| `Live` | `Long` | `0.6985` | 2,820,000.00 USD | 0.00 USD | 5,130.00 USD | `-21.92%` | `7,342.20` |
| `Live` | `Long` | `0.7015` | 2,820,000.00 USD | 0.00 USD | 1,990.00 USD | `-21.59%` | `2,841.50` |
| `Live` | `Long` | `0.7025` | 2,810,000.00 USD | 0.00 USD | 39,470.00 USD | `-21.48%` | `56,186.20` |
| `Live` | `Long` | `0.7045` | 2,770,000.00 USD | 0.00 USD | 8,970.00 USD | `-21.25%` | `12,729.60` |
| `Live` | `Long` | `0.7055` | 2,770,000.00 USD | 0.00 USD | 141.38 USD | `-21.14%` | `200.40` |
| `Live` | `Long` | `0.7065` | 2,760,000.00 USD | 0.00 USD | 143.14 USD | `-21.03%` | `202.60` |
| `Live` | `Long` | `0.7075` | 2,760,000.00 USD | 0.00 USD | 770.68 USD | `-20.92%` | `1,089.30` |
| `Live` | `Long` | `0.7085` | 2,760,000.00 USD | 0.00 USD | 2,810.00 USD | `-20.81%` | `3,961.70` |
| `Live` | `Long` | `0.7095` | 2,760,000.00 USD | 0.00 USD | 1,140.00 USD | `-20.69%` | `1,603.50` |
| `Live` | `Long` | `0.7105` | 2,760,000.00 USD | 0.00 USD | 4,190.00 USD | `-20.58%` | `5,890.40` |
| `Live` | `Long` | `0.7125` | 2,760,000.00 USD | 0.00 USD | 283.22 USD | `-20.36%` | `397.50` |
| `Live` | `Long` | `0.7135` | 2,760,000.00 USD | 0.00 USD | 927.55 USD | `-20.25%` | `1,300.00` |
| `Live` | `Long` | `0.7155` | 2,750,000.00 USD | 0.00 USD | 11,030.00 USD | `-20.02%` | `15,416.10` |
| `Live` | `Long` | `0.7165` | 2,740,000.00 USD | 0.00 USD | 4,620.00 USD | `-19.91%` | `6,444.00` |
| `Live` | `Long` | `0.7185` | 2,740,000.00 USD | 0.00 USD | 126.96 USD | `-19.69%` | `176.70` |
| `Live` | `Long` | `0.7195` | 2,740,000.00 USD | 0.00 USD | 420.19 USD | `-19.58%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,740,000.00 USD | 0.00 USD | 8,970.00 USD | `-19.35%` | `12,429.90` |
| `Live` | `Long` | `0.7225` | 2,730,000.00 USD | 0.00 USD | 1,420.00 USD | `-19.24%` | `1,965.70` |
| `Live` | `Long` | `0.7235` | 2,730,000.00 USD | 0.00 USD | 127.05 USD | `-19.13%` | `175.60` |
| `Live` | `Long` | `0.7245` | 2,730,000.00 USD | 0.00 USD | 11,950.00 USD | `-19.02%` | `16,495.80` |
| `Live` | `Long` | `0.7255` | 2,720,000.00 USD | 0.00 USD | 435,610.00 USD | `-18.91%` | `600,429.50` |
| `Live` | `Long` | `0.7265` | 2,280,000.00 USD | 0.00 USD | 3,410.00 USD | `-18.79%` | `4,687.00` |
| `Live` | `Long` | `0.7275` | 2,280,000.00 USD | 0.00 USD | 35,890.00 USD | `-18.68%` | `49,332.50` |
| `Live` | `Long` | `0.7285` | 2,240,000.00 USD | 0.00 USD | 3,280.00 USD | `-18.57%` | `4,501.50` |
| `Live` | `Long` | `0.7295` | 2,240,000.00 USD | 0.00 USD | 375.98 USD | `-18.46%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,240,000.00 USD | 0.00 USD | 119.88 USD | `-18.35%` | `164.10` |
| `Live` | `Long` | `0.7325` | 2,240,000.00 USD | 0.00 USD | 246.12 USD | `-18.12%` | `336.00` |
| `Live` | `Long` | `0.7335` | 2,240,000.00 USD | 0.00 USD | 1,630.00 USD | `-18.01%` | `2,226.70` |
| `Live` | `Long` | `0.7345` | 2,240,000.00 USD | 0.00 USD | 22,160.00 USD | `-17.90%` | `30,170.10` |
| `Live` | `Long` | `0.7355` | 2,210,000.00 USD | 0.00 USD | 51,920.00 USD | `-17.79%` | `70,595.50` |
| `Live` | `Long` | `0.7375` | 2,160,000.00 USD | 0.00 USD | 3,450.00 USD | `-17.56%` | `4,683.00` |
| `Live` | `Long` | `0.7385` | 2,160,000.00 USD | 0.00 USD | 6,020.00 USD | `-17.45%` | `8,146.50` |
| `Live` | `Long` | `0.7395` | 2,150,000.00 USD | 0.00 USD | 3,380.00 USD | `-17.34%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,150,000.00 USD | 0.00 USD | 3,530.00 USD | `-17.23%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,140,000.00 USD | 0.00 USD | 382.61 USD | `-17.12%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,140,000.00 USD | 0.00 USD | 1,170.00 USD | `-17.01%` | `1,573.50` |
| `Live` | `Long` | `0.7435` | 2,140,000.00 USD | 0.00 USD | 796,610.00 USD | `-16.89%` | `1,071,432.90` |
| `Live` | `Long` | `0.7455` | 1,350,000.00 USD | 0.00 USD | 6,350.00 USD | `-16.67%` | `8,522.10` |
| `Live` | `Long` | `0.7465` | 1,340,000.00 USD | 0.00 USD | 563.83 USD | `-16.56%` | `755.30` |
| `Live` | `Long` | `0.7475` | 1,340,000.00 USD | 0.00 USD | 107,260.00 USD | `-16.45%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,230,000.00 USD | 0.00 USD | 599.60 USD | `-16.22%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,230,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.00%` | `1,613.50` |
| `Live` | `Long` | `0.7525` | 1,230,000.00 USD | 0.00 USD | 357.14 USD | `-15.89%` | `474.60` |
| `Live` | `Long` | `0.7535` | 1,230,000.00 USD | 0.00 USD | 569.50 USD | `-15.78%` | `755.80` |
| `Live` | `Long` | `0.7545` | 1,230,000.00 USD | 0.00 USD | 922.07 USD | `-15.66%` | `1,222.10` |
| `Live` | `Long` | `0.7555` | 1,230,000.00 USD | 0.00 USD | 2,070.00 USD | `-15.55%` | `2,744.00` |
| `Live` | `Long` | `0.7575` | 1,230,000.00 USD | 0.00 USD | 1,900.00 USD | `-15.33%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,220,000.00 USD | 0.00 USD | 40,520.00 USD | `-15.22%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,180,000.00 USD | 0.00 USD | 1,650.00 USD | `-15.11%` | `2,169.80` |
| `Live` | `Long` | `0.7605` | 1,180,000.00 USD | 0.00 USD | 6,170.00 USD | `-14.99%` | `8,118.70` |
| `Live` | `Long` | `0.7615` | 1,180,000.00 USD | 0.00 USD | 351.43 USD | `-14.88%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,180,000.00 USD | 0.00 USD | 859.11 USD | `-14.77%` | `1,126.70` |
| `Live` | `Long` | `0.7635` | 1,180,000.00 USD | 0.00 USD | 439.47 USD | `-14.66%` | `575.60` |
| `Live` | `Long` | `0.7645` | 1,170,000.00 USD | 0.00 USD | 1,060.00 USD | `-14.55%` | `1,384.30` |
| `Live` | `Long` | `0.7655` | 1,170,000.00 USD | 0.00 USD | 2,740.00 USD | `-14.43%` | `3,585.10` |
| `Live` | `Long` | `0.7665` | 1,170,000.00 USD | 0.00 USD | 2,950.00 USD | `-14.32%` | `3,852.60` |
| `Live` | `Long` | `0.7675` | 1,170,000.00 USD | 0.00 USD | 24,420.00 USD | `-14.21%` | `31,823.60` |
| `Live` | `Long` | `0.7685` | 1,140,000.00 USD | 0.00 USD | 6,600.00 USD | `-14.10%` | `8,589.60` |
| `Live` | `Long` | `0.7705` | 1,140,000.00 USD | 0.00 USD | 5,640.00 USD | `-13.88%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 1,130,000.00 USD | 0.00 USD | 19,250.00 USD | `-13.76%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 1,110,000.00 USD | 0.00 USD | 1,220.00 USD | `-13.65%` | `1,585.20` |
| `Live` | `Long` | `0.7735` | 1,110,000.00 USD | 0.00 USD | 5,230.00 USD | `-13.54%` | `6,756.40` |
| `Live` | `Long` | `0.7755` | 1,110,000.00 USD | 0.00 USD | 3,430.00 USD | `-13.32%` | `4,424.80` |
| `Live` | `Long` | `0.7765` | 1,100,000.00 USD | 0.00 USD | 2,930.00 USD | `-13.21%` | `3,768.50` |
| `Live` | `Long` | `0.7785` | 1,100,000.00 USD | 0.00 USD | 28,010.00 USD | `-12.98%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 1,070,000.00 USD | 0.00 USD | 338.69 USD | `-12.87%` | `434.50` |
| `Live` | `Long` | `0.7815` | 1,070,000.00 USD | 0.00 USD | 4,160.00 USD | `-12.65%` | `5,325.20` |
| `Live` | `Long` | `0.7825` | 1,070,000.00 USD | 0.00 USD | 323,560.00 USD | `-12.53%` | `413,488.90` |
| `Live` | `Long` | `0.7835` | 743,430.00 USD | 0.00 USD | 1,880.00 USD | `-12.42%` | `2,398.60` |
| `Live` | `Long` | `0.7865` | 741,550.00 USD | 0.00 USD | 3,470.00 USD | `-12.09%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 738,070.00 USD | 0.00 USD | 288.70 USD | `-11.98%` | `366.60` |
| `Live` | `Long` | `0.7895` | 737,780.00 USD | 0.00 USD | 1,980.00 USD | `-11.75%` | `2,513.00` |
| `Live` | `Long` | `0.7905` | 735,800.00 USD | 0.00 USD | 5,190.00 USD | `-11.64%` | `6,563.70` |
| `Live` | `Long` | `0.7915` | 730,610.00 USD | 0.00 USD | 11,600.00 USD | `-11.53%` | `14,657.80` |
| `Live` | `Long` | `0.7925` | 719,010.00 USD | 0.00 USD | 3,800.00 USD | `-11.42%` | `4,789.00` |
| `Live` | `Long` | `0.7935` | 715,210.00 USD | 0.00 USD | 809.45 USD | `-11.31%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 714,400.00 USD | 0.00 USD | 595.40 USD | `-11.19%` | `749.40` |
| `Live` | `Long` | `0.7955` | 713,810.00 USD | 0.00 USD | 52,610.00 USD | `-11.08%` | `66,134.90` |
| `Live` | `Long` | `0.7965` | 661,200.00 USD | 0.00 USD | 13,090.00 USD | `-10.97%` | `16,438.80` |
| `Live` | `Long` | `0.7975` | 648,110.00 USD | 0.00 USD | 7,460.00 USD | `-10.86%` | `9,359.90` |
| `Live` | `Long` | `0.7985` | 640,640.00 USD | 0.00 USD | 40,070.00 USD | `-10.75%` | `50,180.50` |
| `Live` | `Long` | `0.7995` | 600,570.00 USD | 0.00 USD | 4,380.00 USD | `-10.63%` | `5,483.00` |
| `Live` | `Long` | `0.8005` | 596,190.00 USD | 0.00 USD | 6,510.00 USD | `-10.52%` | `8,130.70` |
| `Live` | `Long` | `0.8015` | 589,680.00 USD | 0.00 USD | 6,820.00 USD | `-10.41%` | `8,506.20` |
| `Live` | `Long` | `0.8025` | 582,860.00 USD | 0.00 USD | 1,350.00 USD | `-10.30%` | `1,686.70` |
| `Live` | `Long` | `0.8035` | 581,510.00 USD | 0.00 USD | 7,680.00 USD | `-10.19%` | `9,559.90` |
| `Live` | `Long` | `0.8045` | 573,830.00 USD | 0.00 USD | 15,720.00 USD | `-10.08%` | `19,542.50` |
| `Live` | `Long` | `0.8055` | 558,100.00 USD | 0.00 USD | 361.11 USD | `-9.96%` | `448.30` |
| `Live` | `Long` | `0.8065` | 557,740.00 USD | 0.00 USD | 6,910.00 USD | `-9.85%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 550,830.00 USD | 0.00 USD | 2,770.00 USD | `-9.74%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 548,070.00 USD | 0.00 USD | 21,200.00 USD | `-9.63%` | `26,219.00` |
| `Live` | `Long` | `0.8095` | 526,870.00 USD | 0.00 USD | 154,810.00 USD | `-9.52%` | `191,238.50` |
| `Live` | `Long` | `0.8105` | 372,060.00 USD | 0.00 USD | 2,250.00 USD | `-9.40%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 369,810.00 USD | 0.00 USD | 1,720.00 USD | `-9.29%` | `2,118.80` |
| `Live` | `Long` | `0.8125` | 368,090.00 USD | 0.00 USD | 1,160.00 USD | `-9.18%` | `1,421.60` |
| `Live` | `Long` | `0.8135` | 366,930.00 USD | 0.00 USD | 3,800.00 USD | `-9.07%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 363,130.00 USD | 0.00 USD | 277.42 USD | `-8.96%` | `340.60` |
| `Live` | `Long` | `0.8155` | 362,850.00 USD | 0.00 USD | 2,810.00 USD | `-8.85%` | `3,447.40` |
| `Live` | `Long` | `0.8165` | 360,040.00 USD | 0.00 USD | 729.13 USD | `-8.73%` | `893.00` |
| `Live` | `Long` | `0.8175` | 359,310.00 USD | 0.00 USD | 77,840.00 USD | `-8.62%` | `95,214.30` |
| `Live` | `Long` | `0.8195` | 281,470.00 USD | 0.00 USD | 1,140.00 USD | `-8.40%` | `1,385.00` |
| `Live` | `Long` | `0.8215` | 280,340.00 USD | 0.00 USD | 1,770.00 USD | `-8.18%` | `2,157.30` |
| `Live` | `Long` | `0.8225` | 278,560.00 USD | 0.00 USD | 1,020.00 USD | `-8.06%` | `1,238.00` |
| `Live` | `Long` | `0.8235` | 277,550.00 USD | 0.00 USD | 1,870.00 USD | `-7.95%` | `2,274.90` |
| `Live` | `Long` | `0.8245` | 275,670.00 USD | 0.00 USD | 18,280.00 USD | `-7.84%` | `22,175.00` |
| `Live` | `Long` | `0.8255` | 257,390.00 USD | 0.00 USD | 1,580.00 USD | `-7.73%` | `1,911.90` |
| `Live` | `Long` | `0.8275` | 255,810.00 USD | 0.00 USD | 4,690.00 USD | `-7.50%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 251,120.00 USD | 0.00 USD | 120,070.00 USD | `-7.39%` | `144,926.90` |
| `Live` | `Long` | `0.8345` | 131,050.00 USD | 0.00 USD | 5,750.00 USD | `-6.72%` | `6,885.20` |
| `Live` | `Long` | `0.8365` | 125,310.00 USD | 0.00 USD | 28,050.00 USD | `-6.50%` | `33,537.60` |
| `Live` | `Long` | `0.8385` | 97,250.00 USD | 0.00 USD | 948.34 USD | `-6.28%` | `1,131.00` |
| `Live` | `Long` | `0.8395` | 96,300.00 USD | 0.00 USD | 8,460.00 USD | `-6.16%` | `10,080.70` |
| `Live` | `Long` | `0.8415` | 87,840.00 USD | 0.00 USD | 750.79 USD | `-5.94%` | `892.20` |
| `Live` | `Long` | `0.8425` | 87,090.00 USD | 0.00 USD | 11,790.00 USD | `-5.83%` | `13,998.90` |
| `Live` | `Long` | `0.8435` | 75,300.00 USD | 0.00 USD | 103.24 USD | `-5.72%` | `122.40` |
| `Live` | `Long` | `0.8445` | 75,190.00 USD | 0.00 USD | 803.20 USD | `-5.60%` | `951.10` |
| `Live` | `Long` | `0.8455` | 74,390.00 USD | 0.00 USD | 10,690.00 USD | `-5.49%` | `12,645.90` |
| `Live` | `Long` | `0.8465` | 63,700.00 USD | 0.00 USD | 157.20 USD | `-5.38%` | `185.70` |
| `Live` | `Long` | `0.8475` | 63,540.00 USD | 0.00 USD | 317.98 USD | `-5.27%` | `375.20` |
| `Live` | `Long` | `0.8495` | 63,220.00 USD | 0.00 USD | 6,910.00 USD | `-5.05%` | `8,134.60` |
| `Live` | `Long` | `0.8505` | 56,310.00 USD | 0.00 USD | 13,600.00 USD | `-4.93%` | `15,990.30` |
| `Live` | `Long` | `0.8525` | 42,710.00 USD | 0.00 USD | 42,610.00 USD | `-4.71%` | `49,980.80` |
| `Live` | `Long` | `0.8535` | 104.30 USD | 0.00 USD | 104.30 USD | `-4.60%` | `122.20` |
| `Live` | `Short` | `0.8905` | 2,670.00 USD | 2,670.00 USD | 0.00 USD | `-0.46%` | `2,995.40` |
| `Live` | `Short` | `0.9145` | 6,730.00 USD | 4,060.00 USD | 0.00 USD | `+2.22%` | `4,444.10` |
| `Live` | `Short` | `0.9195` | 11,330.00 USD | 4,600.00 USD | 0.00 USD | `+2.78%` | `5,000.00` |
| `Live` | `Short` | `0.9235` | 11,540.00 USD | 209.36 USD | 0.00 USD | `+3.23%` | `226.70` |
| `Live` | `Short` | `0.9285` | 12,640.00 USD | 1,100.00 USD | 0.00 USD | `+3.78%` | `1,183.50` |
| `Live` | `Short` | `0.9325` | 15,060.00 USD | 2,420.00 USD | 0.00 USD | `+4.23%` | `2,595.00` |
| `Live` | `Short` | `0.9355` | 15,290.00 USD | 237.34 USD | 0.00 USD | `+4.57%` | `253.70` |
| `Live` | `Short` | `0.9365` | 15,670.00 USD | 374.23 USD | 0.00 USD | `+4.68%` | `399.60` |
| `Live` | `Short` | `0.9375` | 16,120.00 USD | 454.59 USD | 0.00 USD | `+4.79%` | `484.90` |
| `Live` | `Short` | `0.9385` | 59,200.00 USD | 43,080.00 USD | 0.00 USD | `+4.90%` | `45,903.60` |
| `Live` | `Short` | `0.9405` | 65,580.00 USD | 6,380.00 USD | 0.00 USD | `+5.13%` | `6,783.70` |
| `Live` | `Short` | `0.9445` | 66,100.00 USD | 511.64 USD | 0.00 USD | `+5.57%` | `541.70` |
| `Live` | `Short` | `0.9475` | 67,810.00 USD | 1,720.00 USD | 0.00 USD | `+5.91%` | `1,812.00` |
| `Live` | `Short` | `0.9645` | 69,390.00 USD | 1,580.00 USD | 0.00 USD | `+7.81%` | `1,639.00` |
| `Live` | `Short` | `0.9755` | 72,980.00 USD | 3,590.00 USD | 0.00 USD | `+9.04%` | `3,680.60` |
| `Live` | `Short` | `0.9805` | 74,030.00 USD | 1,050.00 USD | 0.00 USD | `+9.60%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 74,400.00 USD | 365.70 USD | 0.00 USD | `+10.27%` | `370.70` |
| `Live` | `Short` | `0.9885` | 78,650.00 USD | 4,250.00 USD | 0.00 USD | `+10.49%` | `4,304.30` |
| `Live` | `Short` | `0.9915` | 80,220.00 USD | 1,570.00 USD | 0.00 USD | `+10.83%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 80,360.00 USD | 139.59 USD | 0.00 USD | `+11.05%` | `140.50` |
| `Live` | `Short` | `1.00` | 80,690.00 USD | 330.29 USD | 0.00 USD | `+11.94%` | `329.80` |
| `Live` | `Short` | `1.01` | 81,400.00 USD | 705.99 USD | 0.00 USD | `+13.40%` | `695.90` |
| `Live` | `Short` | `1.02` | 81,570.00 USD | 170.40 USD | 0.00 USD | `+13.51%` | `167.80` |
| `Live` | `Short` | `1.03` | 92,610.00 USD | 11,040.00 USD | 0.00 USD | `+15.07%` | `10,723.80` |
| `Live` | `Short` | `1.05` | 92,890.00 USD | 278.90 USD | 0.00 USD | `+17.20%` | `266.00` |
| `Live` | `Short` | `1.05` | 93,490.00 USD | 597.52 USD | 0.00 USD | `+17.42%` | `568.80` |
| `Live` | `Short` | `1.05` | 95,880.00 USD | 2,390.00 USD | 0.00 USD | `+17.53%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 95,980.00 USD | 105.25 USD | 0.00 USD | `+17.65%` | `100.00` |
| `Live` | `Short` | `1.08` | 99,560.00 USD | 3,580.00 USD | 0.00 USD | `+20.77%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 105,120.00 USD | 5,550.00 USD | 0.00 USD | `+21.78%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 105,440.00 USD | 324.90 USD | 0.00 USD | `+22.90%` | `295.50` |
| `Live` | `Short` | `1.10` | 105,720.00 USD | 277.22 USD | 0.00 USD | `+23.01%` | `251.90` |
| `Live` | `Short` | `1.11` | 114,660.00 USD | 8,940.00 USD | 0.00 USD | `+24.13%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 137,960.00 USD | 23,310.00 USD | 0.00 USD | `+25.92%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 138,600.00 USD | 634.09 USD | 0.00 USD | `+26.59%` | `559.90` |
| `Live` | `Short` | `1.15` | 138,730.00 USD | 129.88 USD | 0.00 USD | `+28.93%` | `112.60` |
| `Live` | `Short` | `1.19` | 138,940.00 USD | 215.17 USD | 0.00 USD | `+32.73%` | `181.20` |
| `Live` | `Short` | `1.20` | 139,120.00 USD | 177.65 USD | 0.00 USD | `+34.08%` | `148.10` |
| `Live` | `Short` | `1.22` | 143,560.00 USD | 4,440.00 USD | 0.00 USD | `+36.20%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 143,950.00 USD | 383.01 USD | 0.00 USD | `+36.65%` | `313.30` |
| `Live` | `Short` | `1.23` | 144,330.00 USD | 380.84 USD | 0.00 USD | `+37.99%` | `308.50` |
| `Live` | `Short` | `1.24` | 148,260.00 USD | 3,930.00 USD | 0.00 USD | `+38.55%` | `3,169.40` |
| `Live` | `Short` | `1.26` | 153,090.00 USD | 4,830.00 USD | 0.00 USD | `+40.34%` | `3,850.80` |
| `Live` | `Short` | `1.26` | 155,760.00 USD | 2,670.00 USD | 0.00 USD | `+40.78%` | `2,118.80` |
| `Live` | `Short` | `1.27` | 165,460.00 USD | 9,700.00 USD | 0.00 USD | `+42.35%` | `7,618.00` |
| `Live` | `Short` | `1.28` | 166,520.00 USD | 1,050.00 USD | 0.00 USD | `+42.57%` | `826.40` |
| `Live` | `Short` | `1.28` | 168,820.00 USD | 2,300.00 USD | 0.00 USD | `+42.79%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 208,700.00 USD | 39,880.00 USD | 0.00 USD | `+43.35%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 208,830.00 USD | 126.24 USD | 0.00 USD | `+43.69%` | `98.20` |
| `Live` | `Short` | `1.29` | 209,060.00 USD | 226.80 USD | 0.00 USD | `+44.70%` | `175.20` |
| `Live` | `Short` | `1.30` | 209,170.00 USD | 114.40 USD | 0.00 USD | `+45.14%` | `88.10` |
| `Live` | `Short` | `1.31` | 210,190.00 USD | 1,020.00 USD | 0.00 USD | `+46.37%` | `777.20` |
| `Live` | `Short` | `1.31` | 234,230.00 USD | 24,040.00 USD | 0.00 USD | `+46.60%` | `18,332.80` |
| `Live` | `Short` | `1.31` | 241,720.00 USD | 7,490.00 USD | 0.00 USD | `+46.71%` | `5,709.60` |
| `Live` | `Short` | `1.33` | 248,060.00 USD | 6,340.00 USD | 0.00 USD | `+48.16%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 270,030.00 USD | 21,970.00 USD | 0.00 USD | `+48.50%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 276,890.00 USD | 6,860.00 USD | 0.00 USD | `+49.73%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 635,170.00 USD | 358,280.00 USD | 0.00 USD | `+53.41%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 639,620.00 USD | 4,450.00 USD | 0.00 USD | `+58.11%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 640,020.00 USD | 402.08 USD | 0.00 USD | `+60.57%` | `279.90` |
| `Live` | `Short` | `1.44` | 640,310.00 USD | 288.68 USD | 0.00 USD | `+61.01%` | `200.40` |
| `Live` | `Short` | `1.47` | 656,690.00 USD | 16,390.00 USD | 0.00 USD | `+63.81%` | `11,182.60` |
| `Live` | `Short` | `1.50` | 915,420.00 USD | 258,720.00 USD | 0.00 USD | `+67.16%` | `173,000.00` |
| `Live` | `Short` | `1.51` | 915,570.00 USD | 151.25 USD | 0.00 USD | `+69.06%` | `100.00` |
| `Live` | `Short` | `1.51` | 919,590.00 USD | 4,020.00 USD | 0.00 USD | `+69.29%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 929,500.00 USD | 9,920.00 USD | 0.00 USD | `+70.74%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 929,650.00 USD | 144.34 USD | 0.00 USD | `+71.63%` | `94.00` |
| `Live` | `Short` | `1.54` | 1,010,000.00 USD | 76,120.00 USD | 0.00 USD | `+71.75%` | `49,543.90` |
| `Live` | `Short` | `1.56` | 1,010,000.00 USD | 116.82 USD | 0.00 USD | `+73.87%` | `75.10` |
| `Live` | `Short` | `1.57` | 1,020,000.00 USD | 17,870.00 USD | 0.00 USD | `+75.21%` | `11,400.30` |
| `Live` | `Short` | `1.58` | 1,020,000.00 USD | 285.21 USD | 0.00 USD | `+76.33%` | `180.80` |
| `Live` | `Short` | `1.59` | 1,030,000.00 USD | 1,180.00 USD | 0.00 USD | `+78.12%` | `743.20` |
| `Live` | `Short` | `1.60` | 1,030,000.00 USD | 123.81 USD | 0.00 USD | `+78.56%` | `77.50` |
| `Live` | `Short` | `1.60` | 1,030,000.00 USD | 1,130.00 USD | 0.00 USD | `+79.23%` | `704.60` |
| `Live` | `Short` | `1.65` | 1,050,000.00 USD | 21,330.00 USD | 0.00 USD | `+84.04%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 1,050,000.00 USD | 2,250.00 USD | 0.00 USD | `+84.60%` | `1,360.10` |
| `Live` | `Short` | `1.65` | 1,050,000.00 USD | 3,940.00 USD | 0.00 USD | `+84.82%` | `2,381.50` |
| `Live` | `Short` | `1.66` | 1,090,000.00 USD | 39,020.00 USD | 0.00 USD | `+85.38%` | `23,529.40` |
| `Live` | `Short` | `1.66` | 1,100,000.00 USD | 3,620.00 USD | 0.00 USD | `+85.49%` | `2,184.10` |
| `Live` | `Short` | `1.69` | 1,100,000.00 USD | 150.02 USD | 0.00 USD | `+88.62%` | `88.90` |
| `Live` | `Short` | `1.70` | 1,100,000.00 USD | 485.78 USD | 0.00 USD | `+90.19%` | `285.50` |
| `Live` | `Short` | `1.70` | 1,100,000.00 USD | 174.03 USD | 0.00 USD | `+90.52%` | `102.10` |
| `Live` | `Short` | `1.71` | 1,110,000.00 USD | 9,630.00 USD | 0.00 USD | `+90.75%` | `5,645.40` |
| `Live` | `Short` | `1.71` | 1,110,000.00 USD | 205.67 USD | 0.00 USD | `+91.42%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,110,000.00 USD | 903.10 USD | 0.00 USD | `+92.42%` | `524.60` |
| `Live` | `Short` | `1.73` | 1,110,000.00 USD | 226.05 USD | 0.00 USD | `+93.77%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,110,000.00 USD | 2,080.00 USD | 0.00 USD | `+94.66%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 1,110,000.00 USD | 1,860.00 USD | 0.00 USD | `+95.22%` | `1,065.00` |
| `Live` | `Short` | `1.75` | 1,130,000.00 USD | 19,920.00 USD | 0.00 USD | `+95.78%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 1,140,000.00 USD | 11,350.00 USD | 0.00 USD | `+96.00%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,150,000.00 USD | 1,520.00 USD | 0.00 USD | `+96.11%` | `868.90` |
| `Live` | `Short` | `1.77` | 1,160,000.00 USD | 12,410.00 USD | 0.00 USD | `+98.12%` | `7,000.00` |
| `Live` | `Short` | `1.79` | 1,160,000.00 USD | 782.21 USD | 0.00 USD | `+99.80%` | `437.60` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,180,000.00 USD | 0.00 USD | 497.31 USD | `-70.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,180,000.00 USD | 0.00 USD | 102.75 USD | `-61.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,180,000.00 USD | 0.00 USD | 256.78 USD | `-60.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,180,000.00 USD | 0.00 USD | 428.87 USD | `-56.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,180,000.00 USD | 0.00 USD | 123.45 USD | `-54.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,180,000.00 USD | 0.00 USD | 818.15 USD | `-53.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,170,000.00 USD | 0.00 USD | 436.41 USD | `-51.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,170,000.00 USD | 0.00 USD | 876.79 USD | `-51.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,170,000.00 USD | 0.00 USD | 466.72 USD | `-49.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,170,000.00 USD | 0.00 USD | 142.95 USD | `-46.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,170,000.00 USD | 0.00 USD | 3,010.00 USD | `-44.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,170,000.00 USD | 0.00 USD | 151.74 USD | `-42.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,170,000.00 USD | 0.00 USD | 123.91 USD | `-42.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,170,000.00 USD | 0.00 USD | 219.80 USD | `-38.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,170,000.00 USD | 0.00 USD | 237,400.00 USD | `-38.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 932,110.00 USD | 0.00 USD | 276.75 USD | `-38.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 931,830.00 USD | 0.00 USD | 1,680.00 USD | `-37.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 930,150.00 USD | 0.00 USD | 853.41 USD | `-36.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 929,300.00 USD | 0.00 USD | 119.76 USD | `-35.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 929,180.00 USD | 0.00 USD | 3,520.00 USD | `-34.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 925,650.00 USD | 0.00 USD | 470.62 USD | `-33.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 925,180.00 USD | 0.00 USD | 108.39 USD | `-32.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 925,070.00 USD | 0.00 USD | 123.28 USD | `-32.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 924,950.00 USD | 0.00 USD | 488.52 USD | `-30.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 924,460.00 USD | 0.00 USD | 4,420.00 USD | `-30.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 920,040.00 USD | 0.00 USD | 242.24 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 919,800.00 USD | 0.00 USD | 193.95 USD | `-27.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 919,600.00 USD | 0.00 USD | 149.22 USD | `-27.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 919,460.00 USD | 0.00 USD | 195.47 USD | `-26.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 919,260.00 USD | 0.00 USD | 112.91 USD | `-26.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 919,150.00 USD | 0.00 USD | 181.31 USD | `-26.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 918,970.00 USD | 0.00 USD | 190.25 USD | `-26.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 918,780.00 USD | 0.00 USD | 153.53 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 918,620.00 USD | 0.00 USD | 52,450.00 USD | `-25.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 866,170.00 USD | 0.00 USD | 536.11 USD | `-24.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 865,640.00 USD | 0.00 USD | 918.68 USD | `-23.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 864,720.00 USD | 0.00 USD | 340.75 USD | `-23.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 864,380.00 USD | 0.00 USD | 9,270.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 855,110.00 USD | 0.00 USD | 120.53 USD | `-22.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 854,990.00 USD | 0.00 USD | 160.71 USD | `-22.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 854,830.00 USD | 0.00 USD | 738.08 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 854,090.00 USD | 0.00 USD | 187.61 USD | `-21.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 853,910.00 USD | 0.00 USD | 8,500.00 USD | `-21.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 845,410.00 USD | 0.00 USD | 89,150.00 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 756,260.00 USD | 0.00 USD | 5,650.00 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 750,610.00 USD | 0.00 USD | 371.68 USD | `-20.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 750,240.00 USD | 0.00 USD | 152.05 USD | `-20.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 750,090.00 USD | 0.00 USD | 123.41 USD | `-19.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 749,960.00 USD | 0.00 USD | 745.54 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 749,220.00 USD | 0.00 USD | 1,130.00 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 748,080.00 USD | 0.00 USD | 18,770.00 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 729,310.00 USD | 0.00 USD | 7,970.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 721,350.00 USD | 0.00 USD | 257.26 USD | `-17.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 721,090.00 USD | 0.00 USD | 161.72 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 720,930.00 USD | 0.00 USD | 1,590.00 USD | `-16.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 719,330.00 USD | 0.00 USD | 10,160.00 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 709,180.00 USD | 0.00 USD | 93,810.00 USD | `-16.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 615,370.00 USD | 0.00 USD | 1,230.00 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 614,140.00 USD | 0.00 USD | 1,840.00 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 612,300.00 USD | 0.00 USD | 804.61 USD | `-15.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 611,500.00 USD | 0.00 USD | 590.68 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 610,910.00 USD | 0.00 USD | 635.62 USD | `-14.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 610,270.00 USD | 0.00 USD | 191.12 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 610,080.00 USD | 0.00 USD | 273.92 USD | `-14.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 609,810.00 USD | 0.00 USD | 125.92 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 609,680.00 USD | 0.00 USD | 1,980.00 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 607,700.00 USD | 0.00 USD | 1,150.00 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 606,560.00 USD | 0.00 USD | 1,500.00 USD | `-13.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 605,060.00 USD | 0.00 USD | 1,860.00 USD | `-12.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 603,200.00 USD | 0.00 USD | 128.47 USD | `-12.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7815` | 603,070.00 USD | 0.00 USD | 7,820.00 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 595,260.00 USD | 0.00 USD | 6,960.00 USD | `-12.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 588,300.00 USD | 0.00 USD | 135.11 USD | `-12.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 588,160.00 USD | 0.00 USD | 7,870.00 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7885` | 580,300.00 USD | 0.00 USD | 1,090.00 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 579,210.00 USD | 0.00 USD | 1,500.00 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7935` | 577,710.00 USD | 0.00 USD | 1,290.00 USD | `-11.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 576,420.00 USD | 0.00 USD | 24,240.00 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 552,180.00 USD | 0.00 USD | 1,260.00 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 550,930.00 USD | 0.00 USD | 319.40 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 550,610.00 USD | 0.00 USD | 4,740.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 545,870.00 USD | 0.00 USD | 1,800.00 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 544,070.00 USD | 0.00 USD | 144.67 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 543,920.00 USD | 0.00 USD | 1,510.00 USD | `-10.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 542,410.00 USD | 0.00 USD | 390.59 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 542,020.00 USD | 0.00 USD | 263.25 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 541,760.00 USD | 0.00 USD | 1,250.00 USD | `-9.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8095` | 540,510.00 USD | 0.00 USD | 330.68 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 540,180.00 USD | 0.00 USD | 182,770.00 USD | `-9.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 357,410.00 USD | 0.00 USD | 174.63 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 357,230.00 USD | 0.00 USD | 1,420.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 355,810.00 USD | 0.00 USD | 123,350.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 232,460.00 USD | 0.00 USD | 1,160.00 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 231,300.00 USD | 0.00 USD | 216.70 USD | `-8.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 231,090.00 USD | 0.00 USD | 125.72 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 230,960.00 USD | 0.00 USD | 375.49 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 230,590.00 USD | 0.00 USD | 13,640.00 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 216,940.00 USD | 0.00 USD | 7,160.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 209,790.00 USD | 0.00 USD | 226.71 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 209,560.00 USD | 0.00 USD | 3,780.00 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 205,780.00 USD | 0.00 USD | 1,420.00 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 204,360.00 USD | 0.00 USD | 325.56 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 204,030.00 USD | 0.00 USD | 1,600.00 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 202,430.00 USD | 0.00 USD | 11,080.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 191,350.00 USD | 0.00 USD | 3,950.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 187,400.00 USD | 0.00 USD | 171.46 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 187,220.00 USD | 0.00 USD | 7,920.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 179,300.00 USD | 0.00 USD | 690.30 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 178,610.00 USD | 0.00 USD | 161.89 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 178,450.00 USD | 0.00 USD | 263.43 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 178,190.00 USD | 0.00 USD | 610.23 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 177,580.00 USD | 0.00 USD | 699.65 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 176,880.00 USD | 0.00 USD | 320.31 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 176,560.00 USD | 0.00 USD | 240.52 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 176,320.00 USD | 0.00 USD | 9,760.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 166,560.00 USD | 0.00 USD | 1,020.00 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 165,550.00 USD | 0.00 USD | 510.57 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 165,030.00 USD | 0.00 USD | 212.81 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 164,820.00 USD | 0.00 USD | 1,940.00 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 162,880.00 USD | 0.00 USD | 12,850.00 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 150,020.00 USD | 0.00 USD | 481.80 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 149,540.00 USD | 0.00 USD | 1,340.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 148,200.00 USD | 0.00 USD | 477.13 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 147,720.00 USD | 0.00 USD | 2,930.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8525` | 144,790.00 USD | 0.00 USD | 1,070.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 143,710.00 USD | 0.00 USD | 5,150.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 138,560.00 USD | 0.00 USD | 11,960.00 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 126,590.00 USD | 0.00 USD | 4,280.00 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 122,310.00 USD | 0.00 USD | 1,800.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 120,510.00 USD | 0.00 USD | 8,900.00 USD | `-4.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 111,610.00 USD | 0.00 USD | 1,740.00 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 109,870.00 USD | 0.00 USD | 1,450.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 108,420.00 USD | 0.00 USD | 6,160.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 102,260.00 USD | 0.00 USD | 1,960.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 100,300.00 USD | 0.00 USD | 611.88 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 99,690.00 USD | 0.00 USD | 26,840.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 72,850.00 USD | 0.00 USD | 5,080.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 67,770.00 USD | 0.00 USD | 734.45 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 67,040.00 USD | 0.00 USD | 541.15 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 66,490.00 USD | 0.00 USD | 279.83 USD | `-2.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 66,210.00 USD | 0.00 USD | 5,770.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 60,450.00 USD | 0.00 USD | 106.11 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 60,340.00 USD | 0.00 USD | 3,710.00 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 56,630.00 USD | 0.00 USD | 1,500.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 55,130.00 USD | 0.00 USD | 3,450.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 51,680.00 USD | 0.00 USD | 866.37 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 50,810.00 USD | 0.00 USD | 5,220.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 45,590.00 USD | 0.00 USD | 9,520.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 36,070.00 USD | 0.00 USD | 236.66 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 35,830.00 USD | 0.00 USD | 1,020.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 34,810.00 USD | 0.00 USD | 1,990.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 32,820.00 USD | 0.00 USD | 4,580.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 28,240.00 USD | 0.00 USD | 4,070.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 24,170.00 USD | 0.00 USD | 563.65 USD | `-1.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 23,610.00 USD | 0.00 USD | 425.94 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 23,180.00 USD | 0.00 USD | 858.76 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8855` | 22,320.00 USD | 0.00 USD | 3,070.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 19,250.00 USD | 0.00 USD | 3,600.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 15,650.00 USD | 0.00 USD | 235.54 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8885` | 15,420.00 USD | 0.00 USD | 2,030.00 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 13,390.00 USD | 0.00 USD | 1,050.00 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8905` | 12,330.00 USD | 0.00 USD | 1,230.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 11,100.00 USD | 0.00 USD | 114.91 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 10,990.00 USD | 0.00 USD | 10,610.00 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 377.17 USD | 0.00 USD | 277.07 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8945` | 100.09 USD | 0.00 USD | 100.09 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 3,390.00 USD | 3,390.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 4,670.00 USD | 1,280.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 22,880.00 USD | 18,210.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 23,770.00 USD | 889.43 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 52,740.00 USD | 28,960.00 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 53,370.00 USD | 638.09 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 53,600.00 USD | 226.46 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 54,530.00 USD | 926.06 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 54,710.00 USD | 188.92 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 57,670.00 USD | 2,950.00 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 62,200.00 USD | 4,530.00 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 62,500.00 USD | 299.87 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 65,220.00 USD | 2,720.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 66,310.00 USD | 1,090.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 66,820.00 USD | 509.23 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 68,360.00 USD | 1,540.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 68,620.00 USD | 260.23 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 71,510.00 USD | 2,890.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 74,530.00 USD | 3,020.00 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 77,710.00 USD | 3,180.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 78,280.00 USD | 570.08 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 78,580.00 USD | 295.30 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 82,480.00 USD | 3,900.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 84,450.00 USD | 1,970.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 84,570.00 USD | 116.59 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 87,730.00 USD | 3,160.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 239,690.00 USD | 151,960.00 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 239,840.00 USD | 145.02 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 240,330.00 USD | 495.00 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 240,630.00 USD | 296.02 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 245,360.00 USD | 4,730.00 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 247,560.00 USD | 2,200.00 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 247,850.00 USD | 287.62 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 248,050.00 USD | 199.16 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 248,180.00 USD | 130.59 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 251,860.00 USD | 3,680.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 251,980.00 USD | 120.16 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 255,410.00 USD | 3,430.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 255,980.00 USD | 568.87 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 256,270.00 USD | 292.78 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 256,690.00 USD | 420.98 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 257,710.00 USD | 1,020.00 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 257,810.00 USD | 104.53 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 310,870.00 USD | 53,060.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 314,780.00 USD | 3,910.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 323,740.00 USD | 8,960.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 324,270.00 USD | 529.50 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 324,940.00 USD | 667.86 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 326,640.00 USD | 1,700.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 327,430.00 USD | 789.04 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 335,990.00 USD | 8,560.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 337,050.00 USD | 1,050.00 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 337,900.00 USD | 848.20 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 357,010.00 USD | 19,120.00 USD | 0.00 USD | `+6.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 358,180.00 USD | 1,160.00 USD | 0.00 USD | `+6.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 362,400.00 USD | 4,220.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 364,550.00 USD | 2,150.00 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 374,460.00 USD | 9,910.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 377,610.00 USD | 3,150.00 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 379,040.00 USD | 1,440.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 381,930.00 USD | 2,890.00 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 383,060.00 USD | 1,130.00 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 383,180.00 USD | 121.54 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 384,260.00 USD | 1,070.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 389,640.00 USD | 5,390.00 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 408,520.00 USD | 18,870.00 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 427,920.00 USD | 19,400.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 428,180.00 USD | 259.86 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 429,510.00 USD | 1,340.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 429,990.00 USD | 476.57 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 430,380.00 USD | 386.60 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 433,540.00 USD | 3,160.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 434,530.00 USD | 993.78 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 434,750.00 USD | 212.90 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 434,910.00 USD | 165.86 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 435,040.00 USD | 125.61 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 435,480.00 USD | 441.51 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 445,670.00 USD | 10,190.00 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 449,260.00 USD | 3,590.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 453,460.00 USD | 4,200.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 453,640.00 USD | 176.73 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 454,150.00 USD | 513.32 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 489,510.00 USD | 35,360.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 521,470.00 USD | 31,960.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 526,460.00 USD | 4,990.00 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 527,010.00 USD | 558.35 USD | 0.00 USD | `+9.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 528,080.00 USD | 1,060.00 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 529,260.00 USD | 1,180.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 529,750.00 USD | 490.99 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 530,150.00 USD | 395.21 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 531,140.00 USD | 991.50 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 541,470.00 USD | 10,340.00 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 541,880.00 USD | 409.52 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 542,170.00 USD | 284.92 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 542,520.00 USD | 350.37 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 542,640.00 USD | 124.04 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 544,200.00 USD | 1,560.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 546,370.00 USD | 2,180.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 547,150.00 USD | 778.64 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 547,520.00 USD | 363.87 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 547,780.00 USD | 267.20 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 548,370.00 USD | 589.52 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 548,480.00 USD | 110.62 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 558,570.00 USD | 10,090.00 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 563,990.00 USD | 5,420.00 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 566,520.00 USD | 2,520.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 566,760.00 USD | 248.49 USD | 0.00 USD | `+13.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 575,910.00 USD | 9,150.00 USD | 0.00 USD | `+13.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 576,640.00 USD | 722.63 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 576,950.00 USD | 312.07 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 577,120.00 USD | 171.24 USD | 0.00 USD | `+14.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 577,680.00 USD | 561.11 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 577,930.00 USD | 249.30 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 579,400.00 USD | 1,470.00 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 579,830.00 USD | 432.18 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 579,970.00 USD | 137.88 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 582,310.00 USD | 2,340.00 USD | 0.00 USD | `+15.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 583,000.00 USD | 694.72 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 583,160.00 USD | 160.60 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 589,720.00 USD | 6,560.00 USD | 0.00 USD | `+16.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 592,640.00 USD | 2,920.00 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 592,860.00 USD | 224.56 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 596,440.00 USD | 3,570.00 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 596,870.00 USD | 432.19 USD | 0.00 USD | `+17.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 598,720.00 USD | 1,850.00 USD | 0.00 USD | `+17.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,300,000.00 USD | 1,700,000.00 USD | 0.00 USD | `+17.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,310,000.00 USD | 5,390.00 USD | 0.00 USD | `+18.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,310,000.00 USD | 285.32 USD | 0.00 USD | `+18.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,310,000.00 USD | 1,130.00 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,310,000.00 USD | 1,240.00 USD | 0.00 USD | `+18.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,310,000.00 USD | 278.06 USD | 0.00 USD | `+18.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,310,000.00 USD | 309.00 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,310,000.00 USD | 228.98 USD | 0.00 USD | `+19.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,310,000.00 USD | 272.12 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,310,000.00 USD | 117.12 USD | 0.00 USD | `+19.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,450,000.00 USD | 140,120.00 USD | 0.00 USD | `+19.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,450,000.00 USD | 530.01 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,450,000.00 USD | 128.23 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,560,000.00 USD | 108,190.00 USD | 0.00 USD | `+20.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,560,000.00 USD | 3,430.00 USD | 0.00 USD | `+21.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,560,000.00 USD | 550.49 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,570,000.00 USD | 5,810.00 USD | 0.00 USD | `+21.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,570,000.00 USD | 1,520.00 USD | 0.00 USD | `+21.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,580,000.00 USD | 5,570.00 USD | 0.00 USD | `+21.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,580,000.00 USD | 1,290.00 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,580,000.00 USD | 294.81 USD | 0.00 USD | `+22.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,580,000.00 USD | 183.11 USD | 0.00 USD | `+22.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,580,000.00 USD | 123.13 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,580,000.00 USD | 494.98 USD | 0.00 USD | `+22.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,580,000.00 USD | 613.52 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,690,000.00 USD | 115,100.00 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,690,000.00 USD | 409.76 USD | 0.00 USD | `+23.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,700,000.00 USD | 162.77 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,700,000.00 USD | 959.70 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,700,000.00 USD | 160.18 USD | 0.00 USD | `+23.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,700,000.00 USD | 669.85 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,700,000.00 USD | 293.61 USD | 0.00 USD | `+25.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,810,000.00 USD | 112,050.00 USD | 0.00 USD | `+25.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,810,000.00 USD | 462.47 USD | 0.00 USD | `+25.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,810,000.00 USD | 2,180.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,810,000.00 USD | 273.34 USD | 0.00 USD | `+26.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,810,000.00 USD | 119.49 USD | 0.00 USD | `+26.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,830,000.00 USD | 20,740.00 USD | 0.00 USD | `+26.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,830,000.00 USD | 468.47 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,830,000.00 USD | 1,430.00 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,840,000.00 USD | 338.50 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,840,000.00 USD | 2,640.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,840,000.00 USD | 1,230.00 USD | 0.00 USD | `+28.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,840,000.00 USD | 2,450.00 USD | 0.00 USD | `+29.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,840,000.00 USD | 1,250.00 USD | 0.00 USD | `+29.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,840,000.00 USD | 143.67 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,840,000.00 USD | 989.81 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,840,000.00 USD | 304.33 USD | 0.00 USD | `+30.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,840,000.00 USD | 255.14 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,840,000.00 USD | 241.65 USD | 0.00 USD | `+31.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,840,000.00 USD | 239.97 USD | 0.00 USD | `+31.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,850,000.00 USD | 2,470.00 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,850,000.00 USD | 3,060.00 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,160,000.00 USD | 310,250.00 USD | 0.00 USD | `+32.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,160,000.00 USD | 309.53 USD | 0.00 USD | `+33.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,160,000.00 USD | 159.09 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,160,000.00 USD | 146.21 USD | 0.00 USD | `+33.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,180,000.00 USD | 18,560.00 USD | 0.00 USD | `+34.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,180,000.00 USD | 933.81 USD | 0.00 USD | `+34.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,180,000.00 USD | 658.86 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,390,000.00 USD | 213,390.00 USD | 0.00 USD | `+35.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,400,000.00 USD | 560.05 USD | 0.00 USD | `+35.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,400,000.00 USD | 1,050.00 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,400,000.00 USD | 108.05 USD | 0.00 USD | `+36.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,400,000.00 USD | 509.71 USD | 0.00 USD | `+36.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,400,000.00 USD | 162.15 USD | 0.00 USD | `+37.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,400,000.00 USD | 187.04 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,400,000.00 USD | 542.12 USD | 0.00 USD | `+37.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,420,000.00 USD | 23,740.00 USD | 0.00 USD | `+37.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,420,000.00 USD | 2,010.00 USD | 0.00 USD | `+38.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,420,000.00 USD | 345.91 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,420,000.00 USD | 104.79 USD | 0.00 USD | `+39.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,420,000.00 USD | 100.04 USD | 0.00 USD | `+39.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,420,000.00 USD | 517.52 USD | 0.00 USD | `+40.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,420,000.00 USD | 152.29 USD | 0.00 USD | `+40.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,430,000.00 USD | 1,480.00 USD | 0.00 USD | `+40.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,430,000.00 USD | 1,010.00 USD | 0.00 USD | `+41.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,430,000.00 USD | 2,780.00 USD | 0.00 USD | `+41.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,430,000.00 USD | 340.38 USD | 0.00 USD | `+42.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,430,000.00 USD | 903.22 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,430,000.00 USD | 475.01 USD | 0.00 USD | `+42.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,470,000.00 USD | 41,160.00 USD | 0.00 USD | `+42.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,490,000.00 USD | 12,840.00 USD | 0.00 USD | `+43.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,680,000.00 USD | 194,770.00 USD | 0.00 USD | `+43.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,690,000.00 USD | 12,890.00 USD | 0.00 USD | `+44.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,700,000.00 USD | 8,820.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,700,000.00 USD | 466.95 USD | 0.00 USD | `+44.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,700,000.00 USD | 613.59 USD | 0.00 USD | `+44.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,700,000.00 USD | 1,420.00 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,720,000.00 USD | 13,000.00 USD | 0.00 USD | `+45.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,720,000.00 USD | 284.42 USD | 0.00 USD | `+45.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,740,000.00 USD | 22,810.00 USD | 0.00 USD | `+47.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,740,000.00 USD | 640.82 USD | 0.00 USD | `+48.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,740,000.00 USD | 134.75 USD | 0.00 USD | `+48.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,760,000.00 USD | 13,400.00 USD | 0.00 USD | `+49.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,760,000.00 USD | 541.96 USD | 0.00 USD | `+49.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,770,000.00 USD | 13,490.00 USD | 0.00 USD | `+50.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,780,000.00 USD | 11,580.00 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,780,000.00 USD | 3,610.00 USD | 0.00 USD | `+51.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,790,000.00 USD | 1,500.00 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,800,000.00 USD | 15,000.00 USD | 0.00 USD | `+52.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,810,000.00 USD | 9,030.00 USD | 0.00 USD | `+53.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,810,000.00 USD | 405.86 USD | 0.00 USD | `+55.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,820,000.00 USD | 13,890.00 USD | 0.00 USD | `+55.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,840,000.00 USD | 14,000.00 USD | 0.00 USD | `+56.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,850,000.00 USD | 12,560.00 USD | 0.00 USD | `+56.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,880,000.00 USD | 32,860.00 USD | 0.00 USD | `+57.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,880,000.00 USD | 102.40 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,880,000.00 USD | 106.64 USD | 0.00 USD | `+57.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,890,000.00 USD | 2,810.00 USD | 0.00 USD | `+58.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,900,000.00 USD | 8,420.00 USD | 0.00 USD | `+58.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,900,000.00 USD | 145.37 USD | 0.00 USD | `+60.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,900,000.00 USD | 1,390.00 USD | 0.00 USD | `+60.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,910,000.00 USD | 14,390.00 USD | 0.00 USD | `+60.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,920,000.00 USD | 7,000.00 USD | 0.00 USD | `+61.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,930,000.00 USD | 14,490.00 USD | 0.00 USD | `+62.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,930,000.00 USD | 1,340.00 USD | 0.00 USD | `+63.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,930,000.00 USD | 342.08 USD | 0.00 USD | `+64.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,940,000.00 USD | 1,200.00 USD | 0.00 USD | `+66.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,950,000.00 USD | 14,890.00 USD | 0.00 USD | `+66.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,960,000.00 USD | 9,580.00 USD | 0.00 USD | `+66.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,970,000.00 USD | 14,980.00 USD | 0.00 USD | `+67.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,980,000.00 USD | 5,110.00 USD | 0.00 USD | `+67.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,980,000.00 USD | 1,180.00 USD | 0.00 USD | `+67.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,980,000.00 USD | 1,260.00 USD | 0.00 USD | `+70.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 3,980,000.00 USD | 2,150.00 USD | 0.00 USD | `+72.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 3,980,000.00 USD | 158.76 USD | 0.00 USD | `+74.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,020,000.00 USD | 30,710.00 USD | 0.00 USD | `+74.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,020,000.00 USD | 574.53 USD | 0.00 USD | `+77.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,020,000.00 USD | 391.32 USD | 0.00 USD | `+78.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,020,000.00 USD | 1,160.00 USD | 0.00 USD | `+81.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,020,000.00 USD | 1,140.00 USD | 0.00 USD | `+83.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,020,000.00 USD | 1,970.00 USD | 0.00 USD | `+83.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,020,000.00 USD | 281.45 USD | 0.00 USD | `+85.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,020,000.00 USD | 2,070.00 USD | 0.00 USD | `+85.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,040,000.00 USD | 13,060.00 USD | 0.00 USD | `+90.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 4,040,000.00 USD | 1,390.00 USD | 0.00 USD | `+94.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,040,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,040,000.00 USD | 320.52 USD | 0.00 USD | `+95.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 4,040,000.00 USD | 1,710.00 USD | 0.00 USD | `+97.45%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7570` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 22,280.00 USD | 18,340.00 USD | 7,630.00 USD |
| `7D` | `0.7590` | 11,000,000.00 USD | 0.00 USD | 11,000,000.00 USD | 6,840.00 USD | 25,130.00 USD | 1,190.00 USD |
| `7D` | `0.7610` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 21,310.00 USD | 16,580.00 USD | 630.66 USD |
| `7D` | `0.7630` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 20,690.00 USD | 118.70 USD | 573.15 USD |
| `7D` | `0.7650` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 556.58 USD | 23,090.00 USD | 10,340.00 USD |
| `7D` | `0.7670` | 10,870,000.00 USD | 0.00 USD | 10,870,000.00 USD | 1,280.00 USD | 3,960.00 USD | 18,920.00 USD |
| `7D` | `0.7690` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 182.28 USD | 161.63 USD | 3,150.00 USD |
| `7D` | `0.7710` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 7,690.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.7790` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 0.00 USD | 5,390.00 USD | 1,290.00 USD |
| `7D` | `0.7810` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 0.00 USD | 185.50 USD | 5,230.00 USD |
| `7D` | `0.7830` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 0.00 USD | 3,930.00 USD | 5,450.00 USD |
| `7D` | `0.7850` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 7,790.00 USD | 20,370.00 USD | 4,220.00 USD |
| `7D` | `0.7870` | 10,780,000.00 USD | 0.00 USD | 10,780,000.00 USD | 0.00 USD | 24,880.00 USD | 1,280.00 USD |
| `7D` | `0.7890` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 0.00 USD | 14,290.00 USD | 0.00 USD |
| `1D` | `0.7900` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 20,640.00 USD | 25,340.00 USD | 9,070.00 USD |
| `1D` | `0.7910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 1,950.00 USD | 6,990.00 USD | 285.55 USD |
| `7D` | `0.7910` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 6,610.00 USD | 24,700.00 USD | 1,530.00 USD |
| `1D` | `0.7920` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 13,250.00 USD | 9,540.00 USD | 36,790.00 USD |
| `1D` | `0.7930` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 6,520.00 USD | 12,800.00 USD | 7,590.00 USD |
| `7D` | `0.7930` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 0.00 USD | 13,760.00 USD | 67,960.00 USD |
| `1D` | `0.7940` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 30,290.00 USD | 8,810.00 USD | 23,640.00 USD |
| `1D` | `0.7950` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 9,270.00 USD | 4,100.00 USD | 25,000.00 USD |
| `7D` | `0.7950` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 3,420.00 USD | 20,630.00 USD | 75,300.00 USD |
| `1D` | `0.7960` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 10,800.00 USD | 2,830.00 USD | 25,750.00 USD |
| `1D` | `0.7970` | 8,820,000.00 USD | 0.00 USD | 8,820,000.00 USD | 24,100.00 USD | 20,190.00 USD | 47,050.00 USD |
| `7D` | `0.7970` | 10,530,000.00 USD | 0.00 USD | 10,530,000.00 USD | 27,750.00 USD | 4,320.00 USD | 53,570.00 USD |
| `1D` | `0.7980` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 15,810.00 USD | 0.00 USD | 333.04 USD |
| `1D` | `0.7990` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 1,600.00 USD | 22,720.00 USD | 18,860.00 USD |
| `7D` | `0.7990` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 8,070.00 USD | 10,040.00 USD | 27,590.00 USD |
| `1D` | `0.8000` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 41,250.00 USD | 14,850.00 USD | 20,840.00 USD |
| `1D` | `0.8010` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 13,800.00 USD | 8,500.00 USD | 4,660.00 USD |
| `7D` | `0.8010` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 60,350.00 USD | 29,250.00 USD | 56,280.00 USD |
| `1D` | `0.8020` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 1,270.00 USD | 6,400.00 USD | 6,570.00 USD |
| `1D` | `0.8030` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 11,920.00 USD | 11,150.00 USD | 159.97 USD |
| `7D` | `0.8030` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 0.00 USD | 26,250.00 USD | 9,800.00 USD |
| `1D` | `0.8040` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 43,320.00 USD | 36,370.00 USD | 26,020.00 USD |
| `1D` | `0.8050` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 19,790.00 USD | 7,230.00 USD | 330.63 USD |
| `7D` | `0.8050` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 10,860.00 USD | 32,020.00 USD | 0.00 USD |
| `1D` | `0.8060` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 36,670.00 USD | 11,640.00 USD | 73,980.00 USD |
| `1D` | `0.8070` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 8,540.00 USD | 14,620.00 USD | 1,120.00 USD |
| `7D` | `0.8070` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 6,450.00 USD | 11,280.00 USD | 3,110.00 USD |
| `1D` | `0.8080` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 2,530.00 USD | 4,510.00 USD | 1,630.00 USD |
| `1D` | `0.8090` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 587.71 USD | 5,580.00 USD | 1,870.00 USD |
| `7D` | `0.8090` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 0.00 USD | 9,100.00 USD | 0.00 USD |
| `1D` | `0.8100` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 1,830.00 USD | 5,380.00 USD | 248.40 USD |
| `1D` | `0.8110` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 1,650.00 USD | 2,090.00 USD | 196.09 USD |
| `7D` | `0.8110` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 61,670.00 USD | 8,310.00 USD | 44,510.00 USD |
| `1D` | `0.8120` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 13,640.00 USD | 780.21 USD | 23,580.00 USD |
| `1D` | `0.8130` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 683.00 USD | 989.28 USD | 706.99 USD |
| `7D` | `0.8130` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 45,800.00 USD | 19,710.00 USD | 12,050.00 USD |
| `1D` | `0.8140` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 14,810.00 USD | 523.16 USD | 11,360.00 USD |
| `1D` | `0.8150` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 4,970.00 USD | 1,140.00 USD | 7,080.00 USD |
| `7D` | `0.8150` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 139,680.00 USD | 51,810.00 USD | 172,260.00 USD |
| `1D` | `0.8160` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 17,910.00 USD | 1,970.00 USD | 23,350.00 USD |
| `1D` | `0.8170` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 56,460.00 USD | 4,990.00 USD | 30,300.00 USD |
| `7D` | `0.8170` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 91,050.00 USD | 25,080.00 USD | 77,680.00 USD |
| `1D` | `0.8180` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 0.00 USD | 351.95 USD | 213.40 USD |
| `1D` | `0.8190` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 24,470.00 USD | 1,520.00 USD | 10,410.00 USD |
| `7D` | `0.8190` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 200,250.00 USD | 53,380.00 USD | 49,120.00 USD |
| `1D` | `0.8200` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 82,040.00 USD | 3,460.00 USD | 73,220.00 USD |
| `1D` | `0.8210` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 16,280.00 USD | 83,250.00 USD | 50,570.00 USD |
| `7D` | `0.8210` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 138,580.00 USD | 80,040.00 USD | 199,020.00 USD |
| `1D` | `0.8220` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 60,840.00 USD | 2,360.00 USD | 18,920.00 USD |
| `1D` | `0.8230` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 6,660.00 USD | 3,770.00 USD | 103,320.00 USD |
| `7D` | `0.8230` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 47,220.00 USD | 42,890.00 USD | 66,580.00 USD |
| `1D` | `0.8240` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 7,980.00 USD | 2,930.00 USD | 29,210.00 USD |
| `1D` | `0.8250` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 28,540.00 USD | 1,410.00 USD | 4,980.00 USD |
| `7D` | `0.8250` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 208,750.00 USD | 32,700.00 USD | 124,360.00 USD |
| `1D` | `0.8260` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 19,380.00 USD | 9,260.00 USD | 17,260.00 USD |
| `1D` | `0.8270` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 39,420.00 USD | 16,780.00 USD | 1,470.00 USD |
| `7D` | `0.8270` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 147,770.00 USD | 53,560.00 USD | 60,860.00 USD |
| `1D` | `0.8280` | 7,280,000.00 USD | 0.00 USD | 7,280,000.00 USD | 1,470.00 USD | 697.90 USD | 564.31 USD |
| `1D` | `0.8290` | 7,280,000.00 USD | 0.00 USD | 7,280,000.00 USD | 25,790.00 USD | 5,230.00 USD | 46,670.00 USD |
| `7D` | `0.8290` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 97,180.00 USD | 43,350.00 USD | 86,320.00 USD |
| `1D` | `0.8300` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 4,230.00 USD | 3,350.00 USD | 7,280.00 USD |
| `1D` | `0.8310` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 3,130.00 USD | 27,660.00 USD | 23,300.00 USD |
| `7D` | `0.8310` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 36,870.00 USD | 32,050.00 USD | 111,870.00 USD |
| `1D` | `0.8320` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 867.90 USD | 10,650.00 USD | 22,900.00 USD |
| `1D` | `0.8330` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 7,940.00 USD | 19,110.00 USD | 74,650.00 USD |
| `7D` | `0.8330` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 157,210.00 USD | 105,720.00 USD | 197,890.00 USD |
| `1D` | `0.8340` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 142,890.00 USD | 21,960.00 USD | 30,560.00 USD |
| `1D` | `0.8350` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 14,620.00 USD | 13,380.00 USD | 1,070.00 USD |
| `7D` | `0.8350` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 120,070.00 USD | 16,770.00 USD | 87,130.00 USD |
| `1D` | `0.8360` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 46,210.00 USD | 1,970.00 USD | 397.88 USD |
| `1D` | `0.8370` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 22,120.00 USD | 10,740.00 USD | 129,100.00 USD |
| `7D` | `0.8370` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 140,480.00 USD | 111,450.00 USD | 140,920.00 USD |
| `1D` | `0.8380` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 35,600.00 USD | 60,420.00 USD | 16,830.00 USD |
| `1D` | `0.8390` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 45,660.00 USD | 1,500.00 USD | 33,130.00 USD |
| `7D` | `0.8390` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 41,090.00 USD | 164,090.00 USD | 167,550.00 USD |
| `1D` | `0.8400` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 7,690.00 USD | 9,650.00 USD | 22,310.00 USD |
| `1D` | `0.8410` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 17,680.00 USD | 16,720.00 USD | 55,700.00 USD |
| `7D` | `0.8410` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 99,070.00 USD | 35,890.00 USD | 27,510.00 USD |
| `1D` | `0.8420` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 71,930.00 USD | 48,400.00 USD | 0.00 USD |
| `1D` | `0.8430` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 17,820.00 USD | 18,730.00 USD | 22,220.00 USD |
| `7D` | `0.8430` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 67,920.00 USD | 123,520.00 USD | 9,570.00 USD |
| `1D` | `0.8440` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 49,800.00 USD | 44,550.00 USD | 166.34 USD |
| `1D` | `0.8450` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 35,860.00 USD | 31,570.00 USD | 13,220.00 USD |
| `7D` | `0.8450` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 37,890.00 USD | 103,700.00 USD | 2,500.00 USD |
| `1D` | `0.8460` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 24,060.00 USD | 68,600.00 USD | 29,910.00 USD |
| `1D` | `0.8470` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 91,300.00 USD | 39,700.00 USD | 27,010.00 USD |
| `7D` | `0.8470` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 44,110.00 USD | 0.00 USD | 29,290.00 USD |
| `1D` | `0.8480` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 11,990.00 USD | 37,210.00 USD | 85,590.00 USD |
| `1D` | `0.8490` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 95,010.00 USD | 64,020.00 USD | 80,290.00 USD |
| `7D` | `0.8490` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 64,910.00 USD | 84,070.00 USD | 135,690.00 USD |
| `1D` | `0.8500` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 46,610.00 USD | 37,570.00 USD | 113,490.00 USD |
| `1D` | `0.8510` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 52,490.00 USD | 115,520.00 USD | 66,110.00 USD |
| `7D` | `0.8510` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 157,910.00 USD | 72,120.00 USD | 19,510.00 USD |
| `1D` | `0.8520` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 78,650.00 USD | 101,060.00 USD | 88,510.00 USD |
| `1D` | `0.8530` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 126,550.00 USD | 99,460.00 USD | 27,540.00 USD |
| `7D` | `0.8530` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 239,650.00 USD | 73,080.00 USD | 95,060.00 USD |
| `1D` | `0.8540` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 36,780.00 USD | 36,580.00 USD | 21,980.00 USD |
| `1D` | `0.8550` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 9,680.00 USD | 45,100.00 USD | 26,840.00 USD |
| `7D` | `0.8550` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 118,050.00 USD | 50,640.00 USD | 34,360.00 USD |
| `1D` | `0.8560` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 67,310.00 USD | 41,200.00 USD | 52,090.00 USD |
| `1D` | `0.8570` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 14,730.00 USD | 46,510.00 USD | 20,870.00 USD |
| `7D` | `0.8570` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 140,780.00 USD | 111,600.00 USD | 63,950.00 USD |
| `1D` | `0.8580` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 32,900.00 USD | 54,050.00 USD | 26,530.00 USD |
| `1D` | `0.8590` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 25,280.00 USD | 6,720.00 USD | 41,750.00 USD |
| `7D` | `0.8590` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 132,610.00 USD | 87,830.00 USD | 2,210.00 USD |
| `1D` | `0.8600` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 75,640.00 USD | 32,480.00 USD | 167.74 USD |
| `1D` | `0.8610` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 21,120.00 USD | 0.00 USD | 6,770.00 USD |
| `7D` | `0.8610` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 36,870.00 USD | 188,190.00 USD | 32,650.00 USD |
| `1D` | `0.8620` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 66,110.00 USD | 25,800.00 USD | 25,970.00 USD |
| `1D` | `0.8630` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 90,570.00 USD | 107,100.00 USD | 121,380.00 USD |
| `7D` | `0.8630` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 100,980.00 USD | 64,400.00 USD | 387,000.00 USD |
| `1D` | `0.8640` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 108,200.00 USD | 54,960.00 USD | 54,030.00 USD |
| `1D` | `0.8650` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 23,980.00 USD | 35,600.00 USD | 142,570.00 USD |
| `7D` | `0.8650` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 254,940.00 USD | 122,950.00 USD | 622,600.00 USD |
| `1D` | `0.8660` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 200,780.00 USD | 17,340.00 USD | 79,580.00 USD |
| `1D` | `0.8670` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 122,450.00 USD | 33,880.00 USD | 154,060.00 USD |
| `7D` | `0.8670` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 252,430.00 USD | 0.00 USD | 158,450.00 USD |
| `1D` | `0.8680` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 72,190.00 USD | 17,760.00 USD | 33,400.00 USD |
| `1D` | `0.8690` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 37,450.00 USD | 0.00 USD | 25,780.00 USD |
| `7D` | `0.8690` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 109,170.00 USD |
| `1D` | `0.8700` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 108,470.00 USD | 31,630.00 USD |
| `1D` | `0.8710` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 217,480.00 USD | 79,810.00 USD | 182,950.00 USD |
| `7D` | `0.8710` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 254,800.00 USD | 146,150.00 USD | 92,670.00 USD |
| `1D` | `0.8720` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 103,610.00 USD | 73,160.00 USD | 64,770.00 USD |
| `1D` | `0.8730` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 71,110.00 USD | 55,280.00 USD | 52,890.00 USD |
| `7D` | `0.8730` | 940,870.00 USD | 0.00 USD | 940,870.00 USD | 79,470.00 USD | 101,280.00 USD | 137,870.00 USD |
| `1D` | `0.8740` | 840,500.00 USD | 0.00 USD | 840,500.00 USD | 134,620.00 USD | 68,390.00 USD | 39,440.00 USD |
| `1D` | `0.8750` | 598,050.00 USD | 0.00 USD | 598,050.00 USD | 29,460.00 USD | 67,500.00 USD | 117,700.00 USD |
| `7D` | `0.8750` | 622,250.00 USD | 0.00 USD | 622,250.00 USD | 108,430.00 USD | 112,580.00 USD | 306,770.00 USD |
| `1D` | `0.8760` | 383,380.00 USD | 0.00 USD | 383,380.00 USD | 0.00 USD | 0.00 USD | 53,070.00 USD |
| `1D` | `0.8770` | 330,320.00 USD | 0.00 USD | 330,320.00 USD | 50,560.00 USD | 20,280.00 USD | 104,690.00 USD |
| `7D` | `0.8770` | 94,460.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 61,690.00 USD | 3,440.00 USD |
| `1D` | `0.8780` | 154,780.00 USD | 0.00 USD | 154,780.00 USD | 79,990.00 USD | 17,410.00 USD | 0.00 USD |
| `1D` | `0.8790` | 57,370.00 USD | 0.00 USD | 57,370.00 USD | 39,180.00 USD | 0.00 USD | 12,930.00 USD |
| `7D` | `0.8790` | 29,340.00 USD | 0.00 USD | 29,340.00 USD | 0.00 USD | 0.00 USD | 3,300.00 USD |
| `1D` | `0.8800` | 5,260.00 USD | 0.00 USD | 5,260.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `0.8810` | 26,030.00 USD | 0.00 USD | 26,030.00 USD | 20,310.00 USD | 0.00 USD | 196.63 USD |
| `1D` | `0.8840` | 4,260.00 USD | 0.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `1D` | `0.8850` | 2,430.00 USD | 0.00 USD | 2,430.00 USD | 0.00 USD | 0.00 USD | 214.94 USD |
| `1D` | `0.8870` | 2,220.00 USD | 0.00 USD | 2,220.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD |
| `7D` | `0.8870` | 5,530.00 USD | 0.00 USD | 5,530.00 USD | 0.00 USD | 0.00 USD | 2,550.00 USD |
| `1D` | `0.8880` | 811.86 USD | 0.00 USD | 811.86 USD | 0.00 USD | 0.00 USD | 560.38 USD |
| `7D` | `0.8890` | 2,970.00 USD | 0.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | 2,970.00 USD |
| `1D` | `0.8910` | 251.48 USD | 0.00 USD | 251.48 USD | 0.00 USD | 0.00 USD | 251.48 USD |
| `7D` | `0.8910` | 528,160.00 USD | 528,160.00 USD | 0.00 USD | 523,470.00 USD | 0.00 USD | 4,680.00 USD |
| `7D` | `0.8910` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 523,470.00 USD | 0.00 USD | 4,680.00 USD |
| `1D` | `0.8920` | 1,790.00 USD | 1,790.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8920` | 3,570.00 USD | 3,570.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8930` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 728.40 USD |
| `1D` | `0.8940` | 25,140.00 USD | 25,140.00 USD | 0.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `1D` | `0.8950` | 102,990.00 USD | 102,990.00 USD | 0.00 USD | 0.00 USD | 77,850.00 USD | 0.00 USD |
| `7D` | `0.8950` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 800,940.00 USD | 68,760.00 USD | 325.98 USD |
| `1D` | `0.8970` | 103,960.00 USD | 103,960.00 USD | 0.00 USD | 969.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8970` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 617,630.00 USD | 93,070.00 USD | 11,020.00 USD |
| `1D` | `0.8980` | 260,980.00 USD | 260,980.00 USD | 0.00 USD | 96,220.00 USD | 60,810.00 USD | 0.00 USD |
| `1D` | `0.8990` | 511,410.00 USD | 511,410.00 USD | 0.00 USD | 113,150.00 USD | 129,660.00 USD | 7,610.00 USD |
| `7D` | `0.8990` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 368,200.00 USD | 67,360.00 USD | 340,220.00 USD |
| `1D` | `0.9000` | 816,950.00 USD | 816,950.00 USD | 0.00 USD | 246,360.00 USD | 5,150.00 USD | 54,030.00 USD |
| `1D` | `0.9010` | 955,070.00 USD | 955,070.00 USD | 0.00 USD | 27,370.00 USD | 80,270.00 USD | 30,490.00 USD |
| `7D` | `0.9010` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 207,550.00 USD | 138,590.00 USD | 435,070.00 USD |
| `1D` | `0.9020` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 93,760.00 USD | 57,880.00 USD | 24,630.00 USD |
| `1D` | `0.9030` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 47,830.00 USD | 71,900.00 USD | 28,540.00 USD |
| `7D` | `0.9030` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 124,030.00 USD | 99,390.00 USD | 136,060.00 USD |
| `1D` | `0.9040` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 197,110.00 USD | 154,100.00 USD | 33,400.00 USD |
| `1D` | `0.9050` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 127,800.00 USD | 26,270.00 USD | 44,370.00 USD |
| `7D` | `0.9050` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 169,680.00 USD | 0.00 USD | 323,290.00 USD |
| `1D` | `0.9060` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 168,180.00 USD | 169,000.00 USD | 165,470.00 USD |
| `1D` | `0.9070` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 200,430.00 USD | 145,890.00 USD | 147,060.00 USD |
| `7D` | `0.9070` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 595,880.00 USD | 197,080.00 USD | 123,890.00 USD |
| `1D` | `0.9080` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 151,730.00 USD | 92,080.00 USD | 60,980.00 USD |
| `1D` | `0.9090` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 92,480.00 USD | 65,350.00 USD | 56,020.00 USD |
| `7D` | `0.9090` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 140,150.00 USD | 244,140.00 USD | 229,880.00 USD |
| `1D` | `0.9100` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 156,840.00 USD | 98,270.00 USD | 40,220.00 USD |
| `1D` | `0.9110` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 97,650.00 USD | 84,090.00 USD | 63,310.00 USD |
| `7D` | `0.9110` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 341,320.00 USD | 216,330.00 USD | 120,090.00 USD |
| `1D` | `0.9120` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 32,690.00 USD | 81,230.00 USD | 69,240.00 USD |
| `1D` | `0.9130` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 68,900.00 USD | 25,330.00 USD | 103,130.00 USD |
| `7D` | `0.9130` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 80,230.00 USD | 148,650.00 USD | 0.00 USD |
| `1D` | `0.9140` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 162,940.00 USD | 61,860.00 USD | 142,770.00 USD |
| `1D` | `0.9150` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 120,960.00 USD | 68,860.00 USD | 184,390.00 USD |
| `7D` | `0.9150` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD |
| `1D` | `0.9160` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 81,680.00 USD | 104,770.00 USD | 56,240.00 USD |
| `1D` | `0.9170` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 103,830.00 USD | 28,770.00 USD | 94,580.00 USD |
| `7D` | `0.9170` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 163,880.00 USD | 2,050.00 USD | 31,840.00 USD |
| `1D` | `0.9180` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 38,530.00 USD | 60,340.00 USD | 71,280.00 USD |
| `1D` | `0.9190` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 94,380.00 USD | 18,760.00 USD | 61,990.00 USD |
| `7D` | `0.9190` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 296,480.00 USD | 75,390.00 USD | 238,200.00 USD |
| `1D` | `0.9200` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 76,540.00 USD | 16,940.00 USD | 105,910.00 USD |
| `1D` | `0.9210` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 96,850.00 USD | 70,120.00 USD | 141,300.00 USD |
| `7D` | `0.9210` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 194,470.00 USD | 18,660.00 USD | 187,940.00 USD |
| `1D` | `0.9220` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 147,880.00 USD | 32,770.00 USD | 136,590.00 USD |
| `1D` | `0.9230` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 107,110.00 USD | 55,720.00 USD | 151,880.00 USD |
| `7D` | `0.9230` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 56,540.00 USD | 68,150.00 USD | 398,340.00 USD |
| `1D` | `0.9240` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 133,900.00 USD | 65,460.00 USD | 117,430.00 USD |
| `1D` | `0.9250` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 167,630.00 USD | 71,780.00 USD | 70,680.00 USD |
| `7D` | `0.9250` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 182,660.00 USD | 120,540.00 USD | 109,690.00 USD |
| `1D` | `0.9260` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 43,480.00 USD | 95,380.00 USD | 74,680.00 USD |
| `1D` | `0.9270` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 18,040.00 USD | 75,810.00 USD | 39,000.00 USD |
| `7D` | `0.9270` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 270,890.00 USD | 100,630.00 USD | 118,470.00 USD |
| `1D` | `0.9280` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 77,040.00 USD | 54,950.00 USD | 68,320.00 USD |
| `1D` | `0.9290` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 53,740.00 USD | 37,110.00 USD | 62,080.00 USD |
| `7D` | `0.9290` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 52,860.00 USD | 111,530.00 USD | 62,710.00 USD |
| `1D` | `0.9300` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 5,010.00 USD | 59,630.00 USD | 65,490.00 USD |
| `1D` | `0.9310` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 129,900.00 USD | 16,270.00 USD | 42,450.00 USD |
| `7D` | `0.9310` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 181,630.00 USD | 80,980.00 USD | 168,120.00 USD |
| `1D` | `0.9320` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 71,540.00 USD | 29,090.00 USD | 35,540.00 USD |
| `1D` | `0.9330` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 25,650.00 USD | 20,660.00 USD | 6,700.00 USD |
| `7D` | `0.9330` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 7,740.00 USD | 77,810.00 USD | 65,660.00 USD |
| `1D` | `0.9340` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 1,200.00 USD | 16,430.00 USD | 0.00 USD |
| `1D` | `0.9350` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 2,160.00 USD | 867.77 USD | 19,260.00 USD |
| `7D` | `0.9350` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 53,950.00 USD | 55,880.00 USD | 0.00 USD |
| `1D` | `0.9360` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 49,530.00 USD | 26,230.00 USD | 55,350.00 USD |
| `1D` | `0.9370` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 80,470.00 USD | 27,130.00 USD | 93,690.00 USD |
| `7D` | `0.9370` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 256,610.00 USD | 5,150.00 USD | 44,240.00 USD |
| `1D` | `0.9380` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 15,820.00 USD | 9,440.00 USD | 43,070.00 USD |
| `1D` | `0.9390` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 3,150.00 USD | 3,270.00 USD | 34,210.00 USD |
| `7D` | `0.9390` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 86,850.00 USD | 36,340.00 USD | 266,510.00 USD |
| `1D` | `0.9400` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 47,250.00 USD | 2,660.00 USD | 56,240.00 USD |
| `1D` | `0.9410` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 20,430.00 USD | 15,760.00 USD | 616.58 USD |
| `7D` | `0.9410` | 12,280,000.00 USD | 12,280,000.00 USD | 0.00 USD | 128,480.00 USD | 8,510.00 USD | 4,990.00 USD |
| `1D` | `0.9420` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 7,430.00 USD | 1,870.00 USD | 24,960.00 USD |
| `1D` | `0.9430` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 5,380.00 USD | 2,520.00 USD | 26.67 USD |
| `7D` | `0.9430` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 15,490.00 USD | 70,360.00 USD | 33,660.00 USD |
| `1D` | `0.9440` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 5,140.00 USD | 23,770.00 USD | 46,190.00 USD |
| `1D` | `0.9450` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 4,850.00 USD | 1,000.00 USD | 47,330.00 USD |
| `7D` | `0.9450` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 3,360.00 USD | 244,270.00 USD | 94,130.00 USD |
| `1D` | `0.9460` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 56,940.00 USD | 26,210.00 USD | 24,590.00 USD |
| `1D` | `0.9470` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 36,440.00 USD | 24,890.00 USD | 20,480.00 USD |
| `7D` | `0.9470` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 212,500.00 USD |
| `1D` | `0.9480` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 55,350.00 USD | 48,320.00 USD | 35,870.00 USD |
| `1D` | `0.9490` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 19,060.00 USD | 15,420.00 USD | 22,960.00 USD |
| `7D` | `0.9490` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 2,500.00 USD | 108,270.00 USD | 118,920.00 USD |
| `1D` | `0.9500` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 8,330.00 USD | 22,290.00 USD | 47,610.00 USD |
| `1D` | `0.9510` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 53,450.00 USD | 28,930.00 USD | 128,260.00 USD |
| `7D` | `0.9510` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 2,840.00 USD | 88,970.00 USD | 734,250.00 USD |
| `1D` | `0.9520` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 466.70 USD | 332.24 USD | 72,640.00 USD |
| `1D` | `0.9530` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 29,490.00 USD | 27,260.00 USD | 70,380.00 USD |
| `7D` | `0.9530` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD |
| `1D` | `0.9540` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 27,930.00 USD | 21,440.00 USD | 27,680.00 USD |
| `1D` | `0.9550` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 21,030.00 USD | 13,800.00 USD | 24,930.00 USD |
| `7D` | `0.9550` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 77,110.00 USD | 2,400.00 USD | 62,060.00 USD |
| `1D` | `0.9560` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 20,640.00 USD | 11,590.00 USD | 23,330.00 USD |
| `1D` | `0.9570` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 16,640.00 USD | 2,570.00 USD | 533.76 USD |
| `7D` | `0.9570` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 463,830.00 USD | 4,720.00 USD | 2,940.00 USD |
| `1D` | `0.9580` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 10,110.00 USD | 23,670.00 USD | 12,560.00 USD |
| `1D` | `0.9590` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 33,840.00 USD | 26,900.00 USD | 0.00 USD |
| `7D` | `0.9590` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 563,790.00 USD | 21,410.00 USD | 3,520.00 USD |
| `1D` | `0.9600` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 55,860.00 USD | 23,730.00 USD | 78,040.00 USD |
| `1D` | `0.9610` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 108,340.00 USD | 51,860.00 USD | 166,400.00 USD |
| `7D` | `0.9610` | 16,590,000.00 USD | 16,590,000.00 USD | 0.00 USD | 698,570.00 USD | 201,530.00 USD | 480,590.00 USD |
| `1D` | `0.9620` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 107,150.00 USD | 13,840.00 USD | 10,290.00 USD |
| `1D` | `0.9630` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 85,660.00 USD | 15,720.00 USD | 23,460.00 USD |
| `7D` | `0.9630` | 18,100,000.00 USD | 18,100,000.00 USD | 0.00 USD | 579,300.00 USD | 301,610.00 USD | 624,890.00 USD |
| `1D` | `0.9640` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 108,050.00 USD | 39,580.00 USD | 18,220.00 USD |
| `1D` | `0.9650` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 18,450.00 USD | 72,700.00 USD | 29,960.00 USD |
| `7D` | `0.9650` | 19,680,000.00 USD | 19,680,000.00 USD | 0.00 USD | 857,470.00 USD | 312,610.00 USD | 408,950.00 USD |
| `1D` | `0.9660` | 12,080,000.00 USD | 12,080,000.00 USD | 0.00 USD | 135,020.00 USD | 55,700.00 USD | 42,300.00 USD |
| `1D` | `0.9670` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 93,370.00 USD | 53,420.00 USD | 191,400.00 USD |
| `7D` | `0.9670` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 763,290.00 USD | 555,340.00 USD | 508,410.00 USD |
| `1D` | `0.9680` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 85,180.00 USD | 13,070.00 USD | 112,260.00 USD |
| `1D` | `0.9690` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 166,870.00 USD | 72,380.00 USD | 130,080.00 USD |
| `7D` | `0.9690` | 22,750,000.00 USD | 22,750,000.00 USD | 0.00 USD | 558,600.00 USD | 291,960.00 USD | 398,260.00 USD |
| `1D` | `0.9700` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 120,570.00 USD | 38,730.00 USD | 65,600.00 USD |
| `1D` | `0.9710` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 66,850.00 USD | 27,000.00 USD | 71,880.00 USD |
| `7D` | `0.9710` | 23,810,000.00 USD | 23,810,000.00 USD | 0.00 USD | 573,060.00 USD | 319,680.00 USD | 159,190.00 USD |
| `1D` | `0.9720` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 45,860.00 USD | 36,780.00 USD | 55,850.00 USD |
| `1D` | `0.9730` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 24,020.00 USD | 679.60 USD | 0.00 USD |
| `7D` | `0.9730` | 24,620,000.00 USD | 24,620,000.00 USD | 0.00 USD | 458,870.00 USD | 161,170.00 USD | 192,990.00 USD |
| `1D` | `0.9740` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 15,050.00 USD | 6,020.00 USD | 47,290.00 USD |
| `1D` | `0.9750` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 24,670.00 USD | 32,410.00 USD | 91,120.00 USD |
| `7D` | `0.9750` | 25,360,000.00 USD | 25,360,000.00 USD | 0.00 USD | 227,380.00 USD | 293,590.00 USD | 223,590.00 USD |
| `1D` | `0.9760` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 7,490.00 USD | 290.18 USD | 296.90 USD |
| `1D` | `0.9770` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 4,370.00 USD | 22,640.00 USD | 32,110.00 USD |
| `7D` | `0.9770` | 26,440,000.00 USD | 26,440,000.00 USD | 0.00 USD | 329,170.00 USD | 218,820.00 USD | 525,360.00 USD |
| `1D` | `0.9780` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 38,720.00 USD | 25,310.00 USD | 75,160.00 USD |
| `1D` | `0.9790` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 30,700.00 USD | 19,870.00 USD | 37,260.00 USD |
| `7D` | `0.9790` | 27,040,000.00 USD | 27,040,000.00 USD | 0.00 USD | 271,900.00 USD | 86,630.00 USD | 244,270.00 USD |
| `1D` | `0.9800` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 43,770.00 USD | 32,410.00 USD | 81,360.00 USD |
| `1D` | `0.9810` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 56,460.00 USD | 14,450.00 USD | 0.00 USD |
| `7D` | `0.9810` | 27,510,000.00 USD | 27,510,000.00 USD | 0.00 USD | 206,910.00 USD | 86,870.00 USD | 176,660.00 USD |
| `1D` | `0.9820` | 14,350,000.00 USD | 14,350,000.00 USD | 0.00 USD | 37,790.00 USD | 14,300.00 USD | 4,590.00 USD |
| `1D` | `0.9830` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 31,260.00 USD | 21,460.00 USD | 47.72 USD |
| `7D` | `0.9830` | 28,100,000.00 USD | 28,100,000.00 USD | 0.00 USD | 262,900.00 USD | 128,370.00 USD | 200,330.00 USD |
| `1D` | `0.9840` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 2,310.00 USD | 22,540.00 USD | 5,900.00 USD |
| `1D` | `0.9850` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 23,370.00 USD | 19,710.00 USD | 14,510.00 USD |
| `7D` | `0.9850` | 28,510,000.00 USD | 28,510,000.00 USD | 0.00 USD | 235,580.00 USD | 58,210.00 USD | 118,560.00 USD |
| `1D` | `0.9860` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 51,980.00 USD | 24,120.00 USD | 81,170.00 USD |
| `1D` | `0.9870` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 27,800.00 USD | 7,430.00 USD | 16,370.00 USD |
| `7D` | `0.9870` | 29,020,000.00 USD | 29,020,000.00 USD | 0.00 USD | 248,980.00 USD | 203,100.00 USD | 57,080.00 USD |
| `1D` | `0.9880` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 50,330.00 USD | 11,470.00 USD | 26,140.00 USD |
| `7D` | `0.9890` | 29,320,000.00 USD | 29,320,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 18,200.00 USD |
| `7D` | `0.9910` | 29,690,000.00 USD | 29,690,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 84,050.00 USD |
| `7D` | `0.9930` | 30,050,000.00 USD | 30,050,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 72,830.00 USD |
| `7D` | `0.9950` | 30,370,000.00 USD | 30,370,000.00 USD | 0.00 USD | 48,120.00 USD | 138,500.00 USD | 125,920.00 USD |
| `7D` | `0.9970` | 31,020,000.00 USD | 31,020,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 360,870.00 USD |
| `7D` | `0.9990` | 31,310,000.00 USD | 31,310,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 101,850.00 USD |
| `7D` | `1.00` | 31,600,000.00 USD | 31,600,000.00 USD | 0.00 USD | 196,410.00 USD | 50,130.00 USD | 52,400.00 USD |
| `7D` | `1.00` | 31,710,000.00 USD | 31,710,000.00 USD | 0.00 USD | 101,260.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `566.68M` | Total OI Tokens: `637,578,811.3 SUI`
  * 1h OI Change: `+1.05%` | 4h OI Change: `-0.62%` | 24h OI Change: `-9.13%`
  * Exchange Breakdown: Binance=`100.85M` | Bybit=`75.52M` | OKX=`33.08M` | Hyperliquid=`29.12M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.23K` | Last 24h: `2.87K` | Last 3d: `42.29K` | Last 7d: `152.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0066%` |
| **USDT Bybit** | `-0.0058%` | **USDT KuCoin** | `0.0029%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0004%` | **USDT Bitget** | `-0.0049%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `32.55%` | `67.45%` | `0.48` | 3,350,000.00 USD |
| `15M` | `Binance` | `47.62%` | `52.38%` | `0.91` | 949,670.00 USD |
| `15M` | `OKX` | `62%` | `38%` | `1.63` | 402,910.00 USD |
| `15M` | `Bybit` | `34.44%` | `65.56%` | `0.53` | 217,360.00 USD |
| `15M` | `KuCoin` | `28.99%` | `71.01%` | `0.41` | 16,110.00 USD |
| `15M` | `Gate` | `33.92%` | `66.08%` | `0.51` | 35,680.00 USD |
| `15M` | `Bitget` | `26.6%` | `73.4%` | `0.36` | 68,280.00 USD |
| `15M` | `BingX` | `26.42%` | `73.58%` | `0.36` | 120,940.00 USD |
| `15M` | `MEXC` | `30.44%` | `69.56%` | `0.44` | 1,150,000.00 USD |
| `15M` | `Bitunix` | `54.25%` | `45.75%` | `1.19` | 94,040.00 USD |
| `15M` | `Hyperliquid` | `64.04%` | `35.96%` | `1.78` | 31,710.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `41%` | `59%` | `0.69` | 231,180.00 USD |
| `15M` | `Crypto.com` | `97.58%` | `2.42%` | `40.32` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 9,230.00 USD |
| `15M` | `HTX` | `39.59%` | `60.41%` | `0.66` | 6,680.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `68.71%` | `31.29%` | `2.20` | 14,980.00 USD |
| `15M` | `Aster` | `8.22%` | `91.78%` | `0.09` | 31.87 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.03%` | `43.97%` | `1.27` | 974.27 USD |
| `15M` | `Whale Positions` | `47.62%` | `52.38%` | `0.91` | 949,670.00 USD |
| `15M` | `Global Accounts` | `32.55%` | `67.45%` | `0.48` | 3,350,000.00 USD |
| `1H` | `SUI` | `45.41%` | `54.59%` | `0.83` | 15,280,000.00 USD |
| `1H` | `Binance` | `57.54%` | `42.46%` | `1.36` | 4,290,000.00 USD |
| `1H` | `OKX` | `60.5%` | `39.5%` | `1.53` | 822,420.00 USD |
| `1H` | `Bybit` | `55.41%` | `44.59%` | `1.24` | 820,170.00 USD |
| `1H` | `KuCoin` | `39.22%` | `60.78%` | `0.65` | 18,080.00 USD |
| `1H` | `Gate` | `39.74%` | `60.26%` | `0.66` | 150,300.00 USD |
| `1H` | `Bitget` | `46.66%` | `53.34%` | `0.87` | 144,530.00 USD |
| `1H` | `BingX` | `33.63%` | `66.37%` | `0.51` | 4,140,000.00 USD |
| `1H` | `MEXC` | `49.94%` | `50.06%` | `1.00` | 843,380.00 USD |
| `1H` | `Bitunix` | `81.83%` | `18.17%` | `4.50` | 554,570.00 USD |
| `1H` | `Hyperliquid` | `79.86%` | `20.14%` | `3.97` | 118,360.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.21%` | `50.79%` | `0.97` | 1,950,000.00 USD |
| `1H` | `Crypto.com` | `96.72%` | `3.28%` | `29.49` | 1,950.00 USD |
| `1H` | `WhiteBIT` | `0.25%` | `99.75%` | `0.00` | 1,210,000.00 USD |
| `1H` | `HTX` | `34.17%` | `65.83%` | `0.52` | 26,630.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `17.78%` | `82.22%` | `0.22` | 139,660.00 USD |
| `1H` | `Aster` | `55.79%` | `44.21%` | `1.26` | 19,980.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.97%` | `57.03%` | `0.75` | 34,440.00 USD |
| `1H` | `Whale Positions` | `57.54%` | `42.46%` | `1.36` | 4,290,000.00 USD |
| `1H` | `Global Accounts` | `45.41%` | `54.59%` | `0.83` | 15,280,000.00 USD |
| `4H` | `SUI` | `46.60%` | `53.40%` | `0.87` | 81,650,000.00 USD |
| `4H` | `Binance` | `49.4%` | `50.6%` | `0.98` | 27,590,000.00 USD |
| `4H` | `OKX` | `45.67%` | `54.33%` | `0.84` | 6,550,000.00 USD |
| `4H` | `Bybit` | `49.8%` | `50.2%` | `0.99` | 4,960,000.00 USD |
| `4H` | `KuCoin` | `48.64%` | `51.36%` | `0.95` | 449,380.00 USD |
| `4H` | `Gate` | `45.43%` | `54.57%` | `0.83` | 2,250,000.00 USD |
| `4H` | `Bitget` | `48.18%` | `51.82%` | `0.93` | 2,470,000.00 USD |
| `4H` | `BingX` | `26.01%` | `73.99%` | `0.35` | 4,990,000.00 USD |
| `4H` | `MEXC` | `49.52%` | `50.48%` | `0.98` | 19,290,000.00 USD |
| `4H` | `Bitunix` | `48.62%` | `51.38%` | `0.95` | 4,150,000.00 USD |
| `4H` | `Hyperliquid` | `42.43%` | `57.57%` | `0.74` | 1,150,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.92%` | `51.08%` | `0.96` | 4,100,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.68%` | `87.32%` | `0.15` | 2,080,000.00 USD |
| `4H` | `HTX` | `50.53%` | `49.47%` | `1.02` | 80,680.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.11%` | `47.89%` | `1.09` | 1,230,000.00 USD |
| `4H` | `Aster` | `81.99%` | `18.01%` | `4.55` | 184,200.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `59.81%` | `40.19%` | `1.49` | 118,300.00 USD |
| `4H` | `Whale Positions` | `49.4%` | `50.6%` | `0.98` | 27,590,000.00 USD |
| `4H` | `Global Accounts` | `46.60%` | `53.40%` | `0.87` | 81,650,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.8824` | `0.8824` | `0.8824` | `0.8850` | `0.8811` | 3,028,718.86 USD | 820,523.57 USD | 2,208,195.28 USD | -1,387,671.71 USD | `-45.82%` | `5B / 8S` |
| `5:00 UTC` | `0.8809` | `0.8813` | `0.8809` | `0.8847` | `0.8794` | 1,587,197.83 USD | 802,914.12 USD | 784,283.71 USD | 18,630.42 USD | `+1.17%` | `13B / 10S` |
| `0:00 UTC` | `0.8818` | `0.8816` | `0.8818` | `0.8844` | `0.8791` | 1,551,250.08 USD | 906,932.96 USD | 644,317.13 USD | 262,615.83 USD | `+16.93%` | `10B / 5S` |
| `5:00 UTC` | `0.8844` | `0.8837` | `0.8844` | `0.8863` | `0.8807` | 1,224,340.15 USD | 711,478.93 USD | 512,861.22 USD | 198,617.70 USD | `+16.22%` | `12B / 4S` |
| `0:00 UTC` | `0.8851` | `0.8844` | `0.8851` | `0.8860` | `0.8827` | 1,368,441.85 USD | 678,385.46 USD | 690,056.39 USD | -11,670.93 USD | `-0.85%` | `3B / 1S` |
| `5:00 UTC` | `0.8838` | `0.8844` | `0.8838` | `0.8877` | `0.8813` | 1,484,894.62 USD | 684,089.10 USD | 800,805.52 USD | -116,716.42 USD | `-7.86%` | `5B / 13S` |
| `0:00 UTC` | `0.8871` | `0.8881` | `0.8871` | `0.8911` | `0.8836` | 3,655,137.08 USD | 1,940,871.24 USD | 1,714,265.84 USD | 226,605.40 USD | `+6.20%` | `14B / 3S` |
| `5:00 UTC` | `0.8911` | `0.8918` | `0.8911` | `0.8952` | `0.8881` | 1,592,683.02 USD | 837,386.56 USD | 755,296.46 USD | 82,090.10 USD | `+5.15%` | `18B / 8S` |
| `0:00 UTC` | `0.8924` | `0.8930` | `0.8924` | `0.8966` | `0.8911` | 1,758,454.28 USD | 800,627.30 USD | 957,826.98 USD | -157,199.68 USD | `-8.94%` | `8B / 11S` |
| `5:00 UTC` | `0.8899` | `0.8899` | `0.8899` | `0.8921` | `0.8889` | 459,902.43 USD | 185,986.21 USD | 273,916.22 USD | -87,930.00 USD | `-19.12%` | `1B / 9S` |

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
| `5m` | -295.94 USD | -481,690.00 USD | **`DISTRIBUTION`** |
| `15m` | -180,950.00 USD | -623,260.00 USD | **`DISTRIBUTION`** |
| `30m` | -175,780.00 USD | -583,660.00 USD | **`DISTRIBUTION`** |
| `1h` | -287,730.00 USD | 275,770.00 USD | **`DISTRIBUTION`** |
| `2h` | -609,780.00 USD | 555,240.00 USD | **`DISTRIBUTION`** |
| `4h` | -706,860.00 USD | -3,260,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,540,000.00 USD | -6,270,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 1,220,000.00 USD | -2,350,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,750,000.00 USD | -15,550,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,400,000.00 USD | -32,610,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -26,930,000.00 USD | -87,850,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -151,740,000.00 USD | -492,200,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-295.94` | 15m=`-180.95K` | 1h=`-287.73K` | 24h=`-9.40M`
* Futures Capital Netflows: 5m=`-481.69K` | 15m=`-623.26K` | 1h=`+275.77K` | 24h=`-32.61M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
