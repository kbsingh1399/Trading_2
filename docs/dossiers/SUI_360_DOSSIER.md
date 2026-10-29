# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:06:25 IST` (`2026-10-29 20:36:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.9189` | `0.9204` | `0.9154` | `0.9164` | `1,078,285` | 989,855.12 USD | 160,978.73 USD | `+16.26%` | -10,084,790.91 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9163` | `0.9184` | `0.9146` | `0.9160` | `1,105,149` | 1,012,579.68 USD | -87,555.38 USD | `-8.65%` | -10,172,346.29 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.9160` | `0.9191` | `0.9072` | `0.9077` | `3,024,482` | 2,755,129.98 USD | -245,077.13 USD | `-8.90%` | -10,417,423.42 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9294` | `0.9303` | `0.9098` | `0.9181` | `10,264,492` | 9,410,634.53 USD | -158,737.52 USD | `-1.69%` | -10,335,869.63 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9182` | `0.9204` | `0.9146` | `0.9160` | `3,211,511` | 2,946,350.12 USD | 57,472.55 USD | `+1.95%` | -10,278,397.08 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9160` | `0.9191` | `0.9072` | `0.9077` | `3,024,482` | 2,755,129.98 USD | -245,077.13 USD | `-8.90%` | -10,523,474.21 USD | `-0.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9362` | `0.9377` | `0.9250` | `0.9312` | `11,914,670` | 11,092,555.41 USD | -218,628.60 USD | `-1.97%` | -10,248,722.58 USD | `+0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9311` | `0.9338` | `0.9274` | `0.9295` | `5,959,668` | 5,545,537.10 USD | -24,776.87 USD | `-0.45%` | -10,273,499.45 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9294` | `0.9303` | `0.9064` | `0.9073` | `16,847,793` | 15,427,247.26 USD | -359,948.82 USD | `-2.33%` | -10,633,448.27 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.9064` | `0.9073` | `16,847,793` | 15,427,247.26 USD | -359,948.82 USD | `-2.33%` | -9,522,512.34 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -8,478,733.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -8,617,968.75 USD | `+0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.9064` | `0.9073` | `16,847,793` | 15,427,247.26 USD | -359,948.82 USD | `-2.33%` | -9,522,512.34 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `BID` | `0.9061` | `1329.8000` | 1,204.95 USD | 22,909.15 USD | `2 orders` | `-0.11%` | `-` |
| `BID` | `0.9062` | `1662.9000` | 1,506.87 USD | 20,343.80 USD | `1 orders` | `-0.11%` | `-` |
| `BID` | `0.9062` | `340.5000` | 308.55 USD | 20,652.35 USD | `2 orders` | `-0.11%` | `-` |
| `BID` | `0.9062` | `1160.8000` | 1,051.86 USD | 21,704.21 USD | `1 orders` | `-0.11%` | `-` |
| `BID` | `0.9063` | `1660.3000` | 1,504.81 USD | 17,332.27 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `0.9063` | `1660.3000` | 1,504.66 USD | 18,836.93 USD | `1 orders` | `-0.10%` | `-` |
| `BID` | `0.9064` | `1660.3000` | 1,504.96 USD | 15,767.99 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.9064` | `65.6000` | 59.46 USD | 15,827.45 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.9065` | `1660.3000` | 1,505.11 USD | 13,431.41 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.9065` | `917.4000` | 831.62 USD | 14,263.03 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.9066` | `13.3000` | 12.06 USD | 8,913.42 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9066` | `3323.2000` | 3,012.88 USD | 11,926.30 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.9068` | `400.0000` | 362.71 USD | 8,901.36 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9069` | `1660.1000` | 1,505.53 USD | 8,175.89 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9069` | `400.0000` | 362.75 USD | 8,538.65 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `0.9071` | `3320.6000` | 3,012.25 USD | 3,012.25 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.9071` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.91` | `0.00%` | `-` |
| `BID` | `0.9071` | `1337.0000` | 1,212.82 USD | 1,212.82 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.9071` | `2005.5000` | 1,819.21 USD | 3,032.03 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `0.9071` | `1337.0000` | 1,212.79 USD | 4,244.82 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.9071` | `1337.0000` | 1,212.78 USD | 5,457.60 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.9071` | `1337.0000` | 1,212.77 USD | 6,670.37 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `0.9072` | `3325.8000` | 3,017.20 USD | 6,029.45 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.9073` | `668.5000` | 606.54 USD | 11,177.32 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9073` | `2331.4000` | 2,115.28 USD | 10,570.78 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.9073` | `668.5000` | 606.52 USD | 8,455.50 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9073` | `668.5000` | 606.52 USD | 7,848.98 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9073` | `668.5000` | 606.51 USD | 7,242.46 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9073` | `668.5000` | 606.50 USD | 6,635.95 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9074` | `82.6000` | 74.96 USD | 19,266.41 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9074` | `6952.6000` | 6,309.07 USD | 19,191.45 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `0.9074` | `1662.9000` | 1,508.90 USD | 12,882.39 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9074` | `216.2000` | 196.17 USD | 11,373.49 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9075` | `17644.2000` | 16,012.82 USD | 40,188.23 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9075` | `1662.8000` | 1,509.02 USD | 24,175.41 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9075` | `3746.7000` | 3,399.98 USD | 22,666.39 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9076` | `2488.3000` | 2,258.51 USD | 56,714.47 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.9076` | `10819.4000` | 9,819.80 USD | 54,455.97 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9076` | `2146.3000` | 1,947.98 USD | 44,636.17 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.9076` | `2754.5000` | 2,499.96 USD | 42,688.19 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9077` | `4837.7000` | 4,391.08 USD | 61,105.56 USD | `3 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:04:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `657` | `0xb83d...6e36` | `SHORT` | 3,492,425.43 USD | `3,817,609.40` | `1.11` | `0.9052` | `35.45` | 726,309.89 USD | `+20.80%` | `3X Cross` |
| `996` | `0xa2ce...3126` | `LONG` | 2,265,784.43 USD | `2,500,010.40` | `0.8597` | `0.9052` | `0.000000` | 116,577.90 USD | `+5.15%` | `10X Cross` |
| `1494` | `0x9946...0852` | `SHORT` | 1,515,227.97 USD | `1,664,573.50` | `1.08` | `0.9052` | `1.67` | 281,091.64 USD | `+18.55%` | `10X Cross` |
| `1792` | `0x9aa5...58af` | `SHORT` | 1,180,928.75 USD | `1,288,168.80` | `1.14` | `0.9052` | `6.96` | 286,764.14 USD | `+24.28%` | `10X Cross` |
| `1900` | `0x9df2...c665` | `SHORT` | 1,085,388.00 USD | `1,200,000.00` | `0.7465` | `0.9052` | `25.82` | -189,535.60 USD | `-17.46%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9292` | 10,211.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.21K USD at 0.9292 USD [API] | `2026-10-27 21:53:25` |
| `ANNOUNCEMENT` | `INFO` | `0.9292` | 10,211.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.21K USD at 0.9292 USD [API] | `2026-10-27 21:53:25` |
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 5,807.03 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.81K USD at 0.9297 USD [API] | `2026-10-27 22:04:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9297` | 10,217.29 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 10.22K USD at 0.9297 USD [API] | `2026-10-27 22:04:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9275` | 9,715.98 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 9.72K USD at 0.9275 USD [API] | `2026-10-27 22:12:18` |
| `ANNOUNCEMENT` | `INFO` | `0.9276` | 6,289.06 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.29K USD at 0.9276 USD [API] | `2026-10-27 22:27:01` |
| `ANNOUNCEMENT` | `INFO` | `0.9138` | 7,972.82 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 7.97K USD at 0.9138 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9302` | 5,006.54 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9302 USD [API] | `2026-10-27 23:06:13` |
| `ANNOUNCEMENT` | `INFO` | `0.9750` | 2,410.86 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.41K USD at 0.9750 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9751` | 97.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9751 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9752` | 99.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9752 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9753` | 2,175.21 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.18K USD at 0.9753 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9753` | 278.36 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.28K USD at 0.9753 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9754` | 17,626.27 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 17.63K USD at 0.9754 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9755` | 199.98 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.20K USD at 0.9755 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9755` | 16,276.90 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 16.28K USD at 0.9755 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9756` | 2,134.03 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.13K USD at 0.9756 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9759` | 279.49 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.28K USD at 0.9759 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9759` | 994.72 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.99K USD at 0.9759 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9760` | 127.95 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.13K USD at 0.9760 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9760` | 49.97 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.05K USD at 0.9760 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9761` | 946.26 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.95K USD at 0.9761 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9762` | 6,372.47 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 6.37K USD at 0.9762 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9762` | 70.68 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.07K USD at 0.9762 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9762` | 80.05 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.08K USD at 0.9762 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9763` | 3,399.92 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.40K USD at 0.9763 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9764` | 5,340.17 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 5.34K USD at 0.9764 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `0.9294` | 15,568.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 15.57K USD at 0.9294 USD [API] | `2026-10-27 23:34:38` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9709` (Vol: 378,700.00 USD, Dist: `+5.85%`) | Long MP=`0.8890` (Vol: 711,300.00 USD, Dist: `--3.07%`)
  * 48H Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+5.82%`) | Long MP=`0.8887` (Vol: 546,500.00 USD, Dist: `--3.11%`)
  * 3D Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+5.82%`) | Long MP=`0.8887` (Vol: 859,700.00 USD, Dist: `--3.11%`)
  * 7D Horizon: Short MP=`0.9685` (Vol: 565,100.00 USD, Dist: `+5.59%`) | Long MP=`0.8890` (Vol: 1,100,000.00 USD, Dist: `--3.08%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1915` | 16,490.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1965` | 2,190.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 147.74 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 7,370.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,020.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 218.31 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 20,550.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 280.38 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 1,930.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 2,770.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 687.92 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3055` | 3,060.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3145` | 7,530.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3205` | 693.98 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3395` | 378.58 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3415` | 167.51 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3535` | 622.87 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3595` | 9,270.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3635` | 227.19 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3755` | 26,290.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3775` | 6,420.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4005` | 280.35 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 6,220.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4115` | 699.55 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4145` | 1,260.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 102.62 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 467.50 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4325` | 391.46 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4355` | 481.66 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4375` | 43,580.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4415` | 5,800.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 219.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4445` | 573.54 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4495` | 78,660.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 702.74 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 1,480.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4635` | 6,280.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4725` | 5,330.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4795` | 33,560.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4805` | 514.42 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 299.66 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4875` | 12,080.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 1,050.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,120.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 5,360.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 3,330.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 258.21 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 2,540.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 847.53 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 1,620.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 276.39 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 1,240.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 2,450.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5205` | 422.33 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5225` | 244.90 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 5,280.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 125,730.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 264.06 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5335` | 1,040.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 417.12 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 1,190.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 5,850.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 319.98 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 1,670.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 16,060.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 441.84 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 195.93 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 570.01 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 182.72 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 1,010.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 227.41 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 104.60 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 18,120.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 292,250.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5875` | 969.32 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 5,540.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 151.97 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6035` | 48,180.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 10,680.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 272.24 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,780.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 213.64 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 245.40 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 141,660.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 2,060.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 1,540.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 4,400.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,070.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6265` | 546.18 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 3,510.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6335` | 3,130.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 450.05 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 207.17 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 2,850.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 2,240.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6395` | 1,690.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 939.17 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 94,330.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 477.63 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 8,530.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 471.21 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 3,910.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 4,390.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 721.59 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 631.12 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 408,650.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 126,530.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 1,730.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 7,700.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 13,150.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 788.97 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 5,280.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 2,810.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 161.22 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 8,500.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,500.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 35,930.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 1,040.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 10,350.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 5,620.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 3,380.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 15,920.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 6,350.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,790.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 480.49 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 83,790.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 3,670.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 669.50 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 8,940.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 1,930.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7035` | 1,390.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 759.59 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 769.59 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 787.73 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 3,890.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 2,550.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 3,530.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 569.20 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 156.39 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 22,830.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 1,470.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 11,720.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 129.26 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 2,660.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 1,060.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 762.57 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 214.03 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 907.93 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 311,430.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 5,810.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 578.07 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 510.15 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 784,090.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 43,970.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 1,640.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 103,910.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7485` | 105.91 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 811.78 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,340.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 106.03 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,200.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 922.07 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 36,710.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,390.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 1,910.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 2,210.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,060.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 2,360.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7675` | 10,680.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 2,750.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7695` | 144,250.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 8,730.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7715` | 3,190.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 6,810.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 4,570.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 126.41 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 4,630.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 7,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 444.63 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7805` | 24,600.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,630.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7835` | 950.23 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7855` | 3,020.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 2,870.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7875` | 5,400.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7895` | 8,660.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7915` | 1,290.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 385.87 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7935` | 2,220.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7945` | 7,640.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7955` | 23,610.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7975` | 1,170.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7985` | 643.43 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7995` | 2,770.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8005` | 43,710.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8015` | 86,410.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 421.31 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 9,920.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 42,240.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 1,610.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8105` | 5,190.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8115` | 146.48 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8125` | 2,480.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8135` | 11,260.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8155` | 8,160.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8160` | 30,270,000.00 USD | 30,270,000.00 USD | 210,530.00 USD | 64,440.00 USD | 167,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 571.79 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8175` | 103,660.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 11,110,000.00 USD | 11,110,000.00 USD | 78,400.00 USD | 26,400.00 USD | 71,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 29,830,000.00 USD | 29,830,000.00 USD | 77,750.00 USD | 39,880.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 491.10 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8195` | 643.31 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 10,930,000.00 USD | 10,930,000.00 USD | 13,230.00 USD | 16,660.00 USD | 26,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 29,670,000.00 USD | 29,670,000.00 USD | 205,920.00 USD | 47,330.00 USD | 97,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8215` | 5,180.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 10,870,000.00 USD | 10,870,000.00 USD | 12,100.00 USD | 18,530.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8220` | 29,320,000.00 USD | 29,320,000.00 USD | 104,090.00 USD | 39,210.00 USD | 93,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 466.85 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8235` | 216.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 10,810,000.00 USD | 10,810,000.00 USD | 21,120.00 USD | 16,100.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8240` | 29,080,000.00 USD | 29,080,000.00 USD | 97,060.00 USD | 36,240.00 USD | 86,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 3,640.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8255` | 317.82 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 10,750,000.00 USD | 10,750,000.00 USD | 13,860.00 USD | 3,800.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 28,860,000.00 USD | 28,860,000.00 USD | 185,230.00 USD | 28,970.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 11,410.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 10,720,000.00 USD | 10,720,000.00 USD | 19,690.00 USD | 12,830.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 28,540,000.00 USD | 28,540,000.00 USD | 113,570.00 USD | 44,400.00 USD | 87,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 118,200.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8295` | 32,530.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8300` | 10,660,000.00 USD | 10,660,000.00 USD | 11,010.00 USD | 9,200.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 28,290,000.00 USD | 28,290,000.00 USD | 30,930.00 USD | 41,810.00 USD | 44,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8305` | 1,670.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8320` | 10,610,000.00 USD | 10,610,000.00 USD | 19,130.00 USD | 10,200.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 28,170,000.00 USD | 28,170,000.00 USD | 90,830.00 USD | 57,170.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8325` | 18,980.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8340` | 10,570,000.00 USD | 10,570,000.00 USD | 49,780.00 USD | 16,200.00 USD | 43,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 27,970,000.00 USD | 27,970,000.00 USD | 105,040.00 USD | 53,420.00 USD | 180,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 18,570.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 10,460,000.00 USD | 10,460,000.00 USD | 48,150.00 USD | 11,860.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 27,630,000.00 USD | 27,630,000.00 USD | 138,260.00 USD | 28,750.00 USD | 94,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 11,000.00 USD | 982,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8375` | 137.85 USD | 971,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 10,380,000.00 USD | 10,380,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 27,370,000.00 USD | 27,370,000.00 USD | 69,590.00 USD | 59,380.00 USD | 95,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 79,450.00 USD | 971,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8395` | 27,150.00 USD | 892,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 10,310,000.00 USD | 10,310,000.00 USD | 19,020.00 USD | 19,340.00 USD | 33,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 27,140,000.00 USD | 27,140,000.00 USD | 76,470.00 USD | 55,720.00 USD | 58,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 628.27 USD | 865,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8415` | 9,110.00 USD | 864,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 10,240,000.00 USD | 10,240,000.00 USD | 11,140.00 USD | 15,160.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 26,950,000.00 USD | 26,950,000.00 USD | 70,700.00 USD | 48,060.00 USD | 11,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 8,460.00 USD | 855,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8435` | 6,280.00 USD | 846,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 10,190,000.00 USD | 10,190,000.00 USD | 21,450.00 USD | 11,360.00 USD | 81.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 26,820,000.00 USD | 26,820,000.00 USD | 34,250.00 USD | 40,470.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 893.23 USD | 840,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8455` | 6,630.00 USD | 839,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 10,160,000.00 USD | 10,160,000.00 USD | 3,270.00 USD | 9,410.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 26,720,000.00 USD | 26,720,000.00 USD | 31,090.00 USD | 33,020.00 USD | 72,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 15,830.00 USD | 833,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8475` | 29,810.00 USD | 817,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 10,120,000.00 USD | 10,120,000.00 USD | 24,190.00 USD | 20,130.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 26,580,000.00 USD | 26,580,000.00 USD | 52,580.00 USD | 6,260.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,890.00 USD | 787,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8495` | 804.99 USD | 785,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 10,030,000.00 USD | 10,030,000.00 USD | 47,850.00 USD | 7,390.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 26,490,000.00 USD | 26,490,000.00 USD | 32,630.00 USD | 15,300.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 784,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 9,960,000.00 USD | 9,960,000.00 USD | 21,900.00 USD | 27,950.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 26,420,000.00 USD | 26,420,000.00 USD | 77,320.00 USD | 45,980.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 17,050.00 USD | 783,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8535` | 15,640.00 USD | 766,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 9,900,000.00 USD | 9,900,000.00 USD | 14,330.00 USD | 2,800.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 26,250,000.00 USD | 26,250,000.00 USD | 92,380.00 USD | 64,630.00 USD | 15,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8545` | 2,030.00 USD | 750,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8555` | 139.53 USD | 748,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 9,860,000.00 USD | 9,860,000.00 USD | 28,740.00 USD | 23,100.00 USD | 17,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 26,070,000.00 USD | 26,070,000.00 USD | 87,380.00 USD | 45,770.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 36,350.00 USD | 748,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 9,790,000.00 USD | 9,790,000.00 USD | 13,710.00 USD | 13,380.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 25,930,000.00 USD | 25,930,000.00 USD | 65,360.00 USD | 21,960.00 USD | 19,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 24,590.00 USD | 712,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8595` | 7,610.00 USD | 687,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 9,750,000.00 USD | 9,750,000.00 USD | 4,180.00 USD | 6,810.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 25,830,000.00 USD | 25,830,000.00 USD | 38,890.00 USD | 65,420.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 19,020.00 USD | 680,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8615` | 793.18 USD | 661,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 9,720,000.00 USD | 9,720,000.00 USD | 5,810.00 USD | 4,970.00 USD | 396.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 25,700,000.00 USD | 25,700,000.00 USD | 25,100.00 USD | 21,240.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 9,140.00 USD | 660,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8635` | 4,710.00 USD | 651,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 9,710,000.00 USD | 9,710,000.00 USD | 40,460.00 USD | 21,260.00 USD | 60,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 25,600,000.00 USD | 25,600,000.00 USD | 38,670.00 USD | 27,710.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 2,580.00 USD | 646,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8655` | 1,230.00 USD | 643,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 9,590,000.00 USD | 9,590,000.00 USD | 138,180.00 USD | 2,480.00 USD | 13,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 25,530,000.00 USD | 25,530,000.00 USD | 261,430.00 USD | 35,900.00 USD | 117,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,340.00 USD | 642,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8675` | 11,820.00 USD | 641,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 9,430,000.00 USD | 9,430,000.00 USD | 103,400.00 USD | 61,870.00 USD | 33,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 25,110,000.00 USD | 25,110,000.00 USD | 208,910.00 USD | 100,620.00 USD | 113,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8685` | 289.04 USD | 629,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8695` | 6,680.00 USD | 629,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 9,240,000.00 USD | 9,240,000.00 USD | 109,900.00 USD | 92,460.00 USD | 227,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 24,690,000.00 USD | 24,690,000.00 USD | 377,870.00 USD | 141,350.00 USD | 324,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 10,230.00 USD | 622,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8715` | 7,540.00 USD | 612,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 8,810,000.00 USD | 8,810,000.00 USD | 211,680.00 USD | 63,650.00 USD | 201,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 23,850,000.00 USD | 23,850,000.00 USD | 440,480.00 USD | 149,650.00 USD | 311,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8725` | 29,520.00 USD | 604,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8735` | 129,080.00 USD | 575,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8740` | 8,330,000.00 USD | 8,330,000.00 USD | 43,030.00 USD | 19,920.00 USD | 21,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 22,940,000.00 USD | 22,940,000.00 USD | 566,110.00 USD | 236,710.00 USD | 199,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8745` | 13,880.00 USD | 446,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8755` | 1,420.00 USD | 432,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8760` | 8,250,000.00 USD | 8,250,000.00 USD | 89,270.00 USD | 97,710.00 USD | 179,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 21,940,000.00 USD | 21,940,000.00 USD | 594,350.00 USD | 249,690.00 USD | 486,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 33,770.00 USD | 430,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8775` | 16,030.00 USD | 397,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 7,880,000.00 USD | 7,880,000.00 USD | 63,800.00 USD | 50,410.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 20,610,000.00 USD | 20,610,000.00 USD | 261,940.00 USD | 131,240.00 USD | 233,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8785` | 56,160.00 USD | 381,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8795` | 172,470.00 USD | 324,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 7,730,000.00 USD | 7,730,000.00 USD | 13,090.00 USD | 12,550.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 19,990,000.00 USD | 19,990,000.00 USD | 427,340.00 USD | 120,050.00 USD | 424,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8805` | 1,530.00 USD | 152,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8815` | 9,320.00 USD | 150,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8820` | 7,670,000.00 USD | 7,670,000.00 USD | 130,020.00 USD | 63,620.00 USD | 160,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 19,010,000.00 USD | 19,010,000.00 USD | 561,150.00 USD | 242,470.00 USD | 320,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8825` | 6,950.00 USD | 141,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8835` | 2,330.00 USD | 134,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8840` | 7,310,000.00 USD | 7,310,000.00 USD | 301,690.00 USD | 66,580.00 USD | 152,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 17,890,000.00 USD | 17,890,000.00 USD | 772,020.00 USD | 222,890.00 USD | 525,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 3,550.00 USD | 132,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8855` | 2,660.00 USD | 128,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8860` | 6,790,000.00 USD | 6,790,000.00 USD | 272,520.00 USD | 127,540.00 USD | 90,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 16,370,000.00 USD | 16,370,000.00 USD | 520,190.00 USD | 257,680.00 USD | 263,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8865` | 35,970.00 USD | 126,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8875` | 13,890.00 USD | 90,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8880` | 6,300,000.00 USD | 6,300,000.00 USD | 297,140.00 USD | 211,060.00 USD | 485,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 15,330,000.00 USD | 15,330,000.00 USD | 1,050,000.00 USD | 404,050.00 USD | 992,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8885` | 1,310.00 USD | 76,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8895` | 3,530.00 USD | 74,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8900` | 5,310,000.00 USD | 5,310,000.00 USD | 515,380.00 USD | 158,940.00 USD | 512,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 12,880,000.00 USD | 12,880,000.00 USD | 1,180,000.00 USD | 483,970.00 USD | 997,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8905` | 139.90 USD | 71,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8915` | 1,100.00 USD | 71,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8920` | 4,120,000.00 USD | 4,120,000.00 USD | 242,700.00 USD | 69,180.00 USD | 108,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 10,220,000.00 USD | 10,220,000.00 USD | 1,550,000.00 USD | 594,410.00 USD | 705,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 1,040.00 USD | 70,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8935` | 23,520.00 USD | 69,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8940` | 3,700,000.00 USD | 3,700,000.00 USD | 207,140.00 USD | 182,590.00 USD | 376,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 7,370,000.00 USD | 7,370,000.00 USD | 1,220,000.00 USD | 617,220.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8945` | 5,750.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8955` | 257.01 USD | 39,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8960` | 2,930,000.00 USD | 2,930,000.00 USD | 140,660.00 USD | 160,980.00 USD | 230,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 4,480,000.00 USD | 4,480,000.00 USD | 657,470.00 USD | 365,250.00 USD | 767,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8965` | 29,550.00 USD | 39,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8975` | 3,540.00 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8980` | 2,400,000.00 USD | 2,400,000.00 USD | 128,530.00 USD | 68,440.00 USD | 103,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 2,690,000.00 USD | 2,690,000.00 USD | 656,780.00 USD | 284,000.00 USD | 172,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 320.05 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8995` | 143.92 USD | 6,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 2,100,000.00 USD | 2,100,000.00 USD | 79,530.00 USD | 24,210.00 USD | 70,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 1,570,000.00 USD | 1,570,000.00 USD | 127,760.00 USD | 33,800.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 1,930,000.00 USD | 1,930,000.00 USD | 66,430.00 USD | 56,290.00 USD | 190,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 1,410,000.00 USD | 1,410,000.00 USD | 8,440.00 USD | 52,590.00 USD | 118,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 1,610,000.00 USD | 1,610,000.00 USD | 128,110.00 USD | 81,940.00 USD | 142,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 1,230,000.00 USD | 1,230,000.00 USD | 98,990.00 USD | 0.00 USD | 72,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 119.44 USD | 6,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 1,260,000.00 USD | 1,260,000.00 USD | 215,300.00 USD | 10,170.00 USD | 58,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 1,050,000.00 USD | 1,050,000.00 USD | 245,950.00 USD | 0.00 USD | 940.28 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9075` | 5,960.00 USD | 5,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9080` | 977,130.00 USD | 977,130.00 USD | 305,430.00 USD | 116,800.00 USD | 213,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 807,480.00 USD | 807,480.00 USD | 175,380.00 USD | 19,890.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 340,920.00 USD | 340,920.00 USD | 35,010.00 USD | 37,530.00 USD | 35,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9100` | 447,410.00 USD | 447,410.00 USD | 123,910.00 USD | 0.00 USD | 91,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9120` | 232,390.00 USD | 232,390.00 USD | 88,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 232,490.00 USD | 232,490.00 USD | 22,970.00 USD | 0.00 USD | 71,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 143,540.00 USD | 143,540.00 USD | 143,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 137,810.00 USD | 137,810.00 USD | 74,950.00 USD | 17,730.00 USD | 45,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9160` | 171,920.00 USD | 171,920.00 USD | 171,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 21,140.00 USD | 21,140.00 USD | 12,120.00 USD | 9,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9180` | 195,710.00 USD | 195,710.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9200` | 663,000.00 USD | 663,000.00 USD | 386,820.00 USD | 16,660.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 226,920.00 USD | 226,920.00 USD | 32,990.00 USD | 39,420.00 USD | 133,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9220` | 884,090.00 USD | 884,090.00 USD | 0.00 USD | 64,540.00 USD | 156,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9240` | 605,570.00 USD | 605,570.00 USD | 170,280.00 USD | 58,320.00 USD | 150,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9240` | 1,210,000.00 USD | 1,210,000.00 USD | 104,080.00 USD | 41,710.00 USD | 184,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 697,730.00 USD | 697,730.00 USD | 63,790.00 USD | 28,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9260` | 1,320,000.00 USD | 1,320,000.00 USD | 102,010.00 USD | 0.00 USD | 233.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 754,010.00 USD | 754,010.00 USD | 0.00 USD | 44,480.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9280` | 1,420,000.00 USD | 1,420,000.00 USD | 107,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 905,820.00 USD | 905,820.00 USD | 32,650.00 USD | 40,000.00 USD | 79,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9300` | 1,600,000.00 USD | 1,600,000.00 USD | 177,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 1,020,000.00 USD | 1,020,000.00 USD | 100,660.00 USD | 15,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9320` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 50,420.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9340` | 1,820,000.00 USD | 1,820,000.00 USD | 50,160.00 USD | 52,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 1,180,000.00 USD | 1,180,000.00 USD | 25,730.00 USD | 33,250.00 USD | 103,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9360` | 1,940,000.00 USD | 1,940,000.00 USD | 122,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 1,860,000.00 USD | 1,860,000.00 USD | 262,840.00 USD | 118,850.00 USD | 293,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9380` | 2,290,000.00 USD | 2,290,000.00 USD | 168,030.00 USD | 0.00 USD | 177,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 1,980,000.00 USD | 1,980,000.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 2,610,000.00 USD | 2,610,000.00 USD | 166,670.00 USD | 33,320.00 USD | 127,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 20,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 216,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 2,340,000.00 USD | 2,340,000.00 USD | 56,940.00 USD | 28,980.00 USD | 160,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 2,550,000.00 USD | 2,550,000.00 USD | 89,360.00 USD | 66,670.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 54,830.00 USD | 208,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 2,670,000.00 USD | 2,670,000.00 USD | 17,970.00 USD | 36,000.00 USD | 69,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 29,180.00 USD | 371,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 2,950,000.00 USD | 2,950,000.00 USD | 51,320.00 USD | 28,040.00 USD | 195,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 87,720.00 USD | 360,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 3,130,000.00 USD | 3,130,000.00 USD | 62,990.00 USD | 66,810.00 USD | 55,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 4,240,000.00 USD | 4,240,000.00 USD | 10,500.00 USD | 2,560.00 USD | 60,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 3,200,000.00 USD | 3,200,000.00 USD | 21,240.00 USD | 33,360.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 4,310,000.00 USD | 4,310,000.00 USD | 72,330.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 3,250,000.00 USD | 3,250,000.00 USD | 689.00 USD | 43,140.00 USD | 159.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 5,160,000.00 USD | 5,160,000.00 USD | 846,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 3,510,000.00 USD | 3,510,000.00 USD | 110,540.00 USD | 65,690.00 USD | 82,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 5,720,000.00 USD | 5,720,000.00 USD | 356,870.00 USD | 73,200.00 USD | 131,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 4,210,000.00 USD | 4,210,000.00 USD | 299,180.00 USD | 137,300.00 USD | 272,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 7,250,000.00 USD | 7,250,000.00 USD | 715,790.00 USD | 231,300.00 USD | 588,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 4,850,000.00 USD | 4,850,000.00 USD | 324,050.00 USD | 116,210.00 USD | 197,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 8,820,000.00 USD | 8,820,000.00 USD | 693,720.00 USD | 366,520.00 USD | 508,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 5,360,000.00 USD | 5,360,000.00 USD | 243,570.00 USD | 143,870.00 USD | 119,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 10,590,000.00 USD | 10,590,000.00 USD | 995,070.00 USD | 220,060.00 USD | 554,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9680` | 5,960,000.00 USD | 5,960,000.00 USD | 244,090.00 USD | 77,940.00 USD | 280,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 12,760,000.00 USD | 12,760,000.00 USD | 911,470.00 USD | 645,640.00 USD | 613,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 6,550,000.00 USD | 6,550,000.00 USD | 257,240.00 USD | 130,350.00 USD | 199,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 14,180,000.00 USD | 14,180,000.00 USD | 694,250.00 USD | 344,900.00 USD | 380,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 68,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9715` | 398.41 USD | 68,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9720` | 6,920,000.00 USD | 6,920,000.00 USD | 122,820.00 USD | 117,970.00 USD | 126,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 14,900,000.00 USD | 14,900,000.00 USD | 398,310.00 USD | 184,170.00 USD | 139,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 7,070,000.00 USD | 7,070,000.00 USD | 79,700.00 USD | 30,700.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 15,450,000.00 USD | 15,450,000.00 USD | 309,060.00 USD | 116,990.00 USD | 120,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9755` | 121.55 USD | 68,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 7,200,000.00 USD | 7,200,000.00 USD | 30,090.00 USD | 24,570.00 USD | 76,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 16,140,000.00 USD | 16,140,000.00 USD | 182,900.00 USD | 286,070.00 USD | 218,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9765` | 365.89 USD | 69,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9775` | 100.88 USD | 69,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9780` | 7,340,000.00 USD | 7,340,000.00 USD | 4,640.00 USD | 22,340.00 USD | 118,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 17,290,000.00 USD | 17,290,000.00 USD | 441,770.00 USD | 196,630.00 USD | 509,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 7,600,000.00 USD | 7,600,000.00 USD | 65,550.00 USD | 48,270.00 USD | 144,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 17,920,000.00 USD | 17,920,000.00 USD | 341,810.00 USD | 87,560.00 USD | 204,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 15,580.00 USD | 84,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9820` | 7,810,000.00 USD | 7,810,000.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 18,230,000.00 USD | 18,230,000.00 USD | 108,220.00 USD | 52,950.00 USD | 147,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 7,950,000.00 USD | 7,950,000.00 USD | 58,950.00 USD | 66,720.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 18,920,000.00 USD | 18,920,000.00 USD | 395,810.00 USD | 123,000.00 USD | 176,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9845` | 10,440.00 USD | 95,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9860` | 8,170,000.00 USD | 8,170,000.00 USD | 93,180.00 USD | 38,470.00 USD | 86,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 19,260,000.00 USD | 19,260,000.00 USD | 107,440.00 USD | 154,250.00 USD | 72,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 732.03 USD | 95,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 8,340,000.00 USD | 8,340,000.00 USD | 83,850.00 USD | 26,290.00 USD | 61,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 19,560,000.00 USD | 19,560,000.00 USD | 209,770.00 USD | 64,380.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,930.00 USD | 100,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9900` | 8,520,000.00 USD | 8,520,000.00 USD | 87,940.00 USD | 43,020.00 USD | 51,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 19,870,000.00 USD | 19,870,000.00 USD | 201,410.00 USD | 100,430.00 USD | 6,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 2,670.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9920` | 8,650,000.00 USD | 8,650,000.00 USD | 62,110.00 USD | 41,490.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 20,320,000.00 USD | 20,320,000.00 USD | 288,210.00 USD | 79,650.00 USD | 84,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,420.00 USD | 105,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9940` | 8,790,000.00 USD | 8,790,000.00 USD | 48,130.00 USD | 36,960.00 USD | 58,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 20,800,000.00 USD | 20,800,000.00 USD | 143,340.00 USD | 183,310.00 USD | 149,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9945` | 6,430.00 USD | 112,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9960` | 8,830,000.00 USD | 8,830,000.00 USD | 6,270.00 USD | 7,010.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 21,250,000.00 USD | 21,250,000.00 USD | 107,780.00 USD | 55,790.00 USD | 287,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9965` | 2,430.00 USD | 114,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9980` | 9,100,000.00 USD | 9,100,000.00 USD | 109,650.00 USD | 21,830.00 USD | 145,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 21,690,000.00 USD | 21,690,000.00 USD | 238,490.00 USD | 42,080.00 USD | 165,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,140,000.00 USD | 9,140,000.00 USD | 17,400.00 USD | 16,450.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 21,910,000.00 USD | 21,910,000.00 USD | 94,210.00 USD | 53,610.00 USD | 64,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,200,000.00 USD | 9,200,000.00 USD | 15,900.00 USD | 17,990.00 USD | 26,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 22,460,000.00 USD | 22,460,000.00 USD | 250,490.00 USD | 51,850.00 USD | 254,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,270,000.00 USD | 9,270,000.00 USD | 16,070.00 USD | 21,070.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 22,790,000.00 USD | 22,790,000.00 USD | 155,110.00 USD | 45,420.00 USD | 124,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 235.86 USD | 115,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,300,000.00 USD | 9,300,000.00 USD | 9,400.00 USD | 14,230.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 22,990,000.00 USD | 22,990,000.00 USD | 109,230.00 USD | 24,230.00 USD | 69,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,350,000.00 USD | 9,350,000.00 USD | 18,940.00 USD | 9,170.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 23,590,000.00 USD | 23,590,000.00 USD | 274,240.00 USD | 66,150.00 USD | 255,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,380,000.00 USD | 9,380,000.00 USD | 18,290.00 USD | 5,570.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 24,250,000.00 USD | 24,250,000.00 USD | 311,680.00 USD | 74,250.00 USD | 271,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,450,000.00 USD | 9,450,000.00 USD | 21,660.00 USD | 13,820.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 25,300,000.00 USD | 25,300,000.00 USD | 385,660.00 USD | 249,310.00 USD | 418,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,510,000.00 USD | 9,510,000.00 USD | 13,360.00 USD | 11,780.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 26,030,000.00 USD | 26,030,000.00 USD | 341,120.00 USD | 208,060.00 USD | 179,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 115,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,550,000.00 USD | 9,550,000.00 USD | 22,200.00 USD | 10,550.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 26,930,000.00 USD | 26,930,000.00 USD | 390,660.00 USD | 101,810.00 USD | 413,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 8,980.00 USD | 124,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,570,000.00 USD | 9,570,000.00 USD | 18,720.00 USD | 4,150.00 USD | 133.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 27,580,000.00 USD | 27,580,000.00 USD | 268,340.00 USD | 28,880.00 USD | 345,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,660,000.00 USD | 9,660,000.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 28,230,000.00 USD | 28,230,000.00 USD | 201,610.00 USD | 96,960.00 USD | 352,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,740,000.00 USD | 9,740,000.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 28,520,000.00 USD | 28,520,000.00 USD | 163,000.00 USD | 31,420.00 USD | 95,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,810,000.00 USD | 9,810,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 28,750,000.00 USD | 28,750,000.00 USD | 75,030.00 USD | 60,830.00 USD | 95,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,880,000.00 USD | 9,880,000.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 29,140,000.00 USD | 29,140,000.00 USD | 173,720.00 USD | 56,910.00 USD | 158,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,890,000.00 USD | 9,890,000.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 29,230,000.00 USD | 29,230,000.00 USD | 40,590.00 USD | 31,490.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,920,000.00 USD | 9,920,000.00 USD | 8,830.00 USD | 11,740.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 29,480,000.00 USD | 29,480,000.00 USD | 117,500.00 USD | 46,890.00 USD | 89,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 29,950,000.00 USD | 29,950,000.00 USD | 145,150.00 USD | 125,610.00 USD | 192,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 152.91 USD | 124,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.03` | 30,330,000.00 USD | 30,330,000.00 USD | 166,040.00 USD | 102,410.00 USD | 118,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 30,720,000.00 USD | 30,720,000.00 USD | 184,730.00 USD | 21,870.00 USD | 183,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 109.46 USD | 124,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 31,070,000.00 USD | 31,070,000.00 USD | 146,060.00 USD | 27,060.00 USD | 172,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 10,400.00 USD | 134,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 31,290,000.00 USD | 31,290,000.00 USD | 74,160.00 USD | 57,530.00 USD | 88,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 135,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 31,380,000.00 USD | 31,380,000.00 USD | 53,240.00 USD | 12,870.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 31,540,000.00 USD | 31,540,000.00 USD | 77,760.00 USD | 65,330.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 31,640,000.00 USD | 31,640,000.00 USD | 72,850.00 USD | 29,490.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 31,720,000.00 USD | 31,720,000.00 USD | 49,580.00 USD | 12,030.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 31,730,000.00 USD | 31,730,000.00 USD | 0.00 USD | 3,180.00 USD | 96.48 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 135,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 138,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 31,820,000.00 USD | 31,820,000.00 USD | 24,160.00 USD | 46,330.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,330.00 USD | 139,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 139,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 31,880,000.00 USD | 31,880,000.00 USD | 8,480.00 USD | 2,340.00 USD | 53,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 217.44 USD | 139,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.06` | 31,890,000.00 USD | 31,890,000.00 USD | 5,910.00 USD | 5,170.00 USD | 154.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 31,900,000.00 USD | 31,900,000.00 USD | 3,120.00 USD | 3,350.00 USD | 173.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 31,930,000.00 USD | 31,930,000.00 USD | 15,370.00 USD | 3,080.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 31,940,000.00 USD | 31,940,000.00 USD | 4,660.00 USD | 786.13 USD | 85.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 31,940,000.00 USD | 31,940,000.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 114.44 USD | 139,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 1,150.00 USD | 141,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 5,700.00 USD | 146,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 150,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,130.00 USD | 153,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 166.43 USD | 153,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 159,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 159,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 159,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 183,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 1,450.00 USD | 184,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 253.69 USD | 184,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 29,760.00 USD | 214,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 147.43 USD | 214,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 219,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 5,250.00 USD | 224,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 9,370.00 USD | 233,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 234,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 137.21 USD | 234,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 214,000.00 USD | 448,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 451,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 490,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 2,110.00 USD | 493,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 493,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 493,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 494,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 525,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 532,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 554,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 358.30 USD | 554,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,520.00 USD | 556,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 562,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 921,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 925,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 926,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 926,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 1,200.00 USD | 927,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 9,530.00 USD | 937,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 4,830.00 USD | 941,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 146.37 USD | 942,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 1,360.00 USD | 943,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 947,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 1,120.00 USD | 948,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 24,290.00 USD | 972,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 973,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 17,550.00 USD | 990,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.39 USD | 990,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 2,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 122.73 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 9,720.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 39,240.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 9,450.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 296,610.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 85,590.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 148.68 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 2,400.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 781.77 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 952.52 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 14,230.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 203.88 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 943.75 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 190.35 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1915` | 5,470,000.00 USD | 0.00 USD | 16,490.00 USD | `-79.40%` | `86,117.40` |
| `Live` | `Long` | `0.1965` | 5,460,000.00 USD | 0.00 USD | 2,190.00 USD | `-78.86%` | `11,152.10` |
| `Live` | `Long` | `0.1995` | 5,460,000.00 USD | 0.00 USD | 256.00 USD | `-78.54%` | `1,283.20` |
| `Live` | `Long` | `0.2275` | 5,460,000.00 USD | 0.00 USD | 147.74 USD | `-75.53%` | `649.40` |
| `Live` | `Long` | `0.2285` | 5,460,000.00 USD | 0.00 USD | 7,370.00 USD | `-75.42%` | `32,244.50` |
| `Live` | `Long` | `0.2295` | 5,450,000.00 USD | 0.00 USD | 2,020.00 USD | `-75.31%` | `8,782.90` |
| `Live` | `Long` | `0.2355` | 5,450,000.00 USD | 0.00 USD | 789.66 USD | `-74.67%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 5,450,000.00 USD | 0.00 USD | 156.36 USD | `-74.35%` | `655.60` |
| `Live` | `Long` | `0.2525` | 5,450,000.00 USD | 0.00 USD | 2,250.00 USD | `-72.84%` | `8,897.00` |
| `Live` | `Long` | `0.2575` | 5,440,000.00 USD | 0.00 USD | 218.31 USD | `-72.30%` | `847.80` |
| `Live` | `Long` | `0.2645` | 5,440,000.00 USD | 0.00 USD | 20,550.00 USD | `-71.55%` | `77,706.40` |
| `Live` | `Long` | `0.2665` | 5,420,000.00 USD | 0.00 USD | 280.38 USD | `-71.33%` | `1,052.10` |
| `Live` | `Long` | `0.2685` | 5,420,000.00 USD | 0.00 USD | 106.16 USD | `-71.12%` | `395.40` |
| `Live` | `Long` | `0.2735` | 5,420,000.00 USD | 0.00 USD | 248.34 USD | `-70.58%` | `908.00` |
| `Live` | `Long` | `0.2755` | 5,420,000.00 USD | 0.00 USD | 1,930.00 USD | `-70.37%` | `7,000.00` |
| `Live` | `Long` | `0.2805` | 5,420,000.00 USD | 0.00 USD | 2,770.00 USD | `-69.83%` | `9,865.70` |
| `Live` | `Long` | `0.2885` | 5,420,000.00 USD | 0.00 USD | 29,070.00 USD | `-68.97%` | `100,768.40` |
| `Live` | `Long` | `0.2945` | 5,390,000.00 USD | 0.00 USD | 687.92 USD | `-68.32%` | `2,335.90` |
| `Live` | `Long` | `0.2975` | 5,390,000.00 USD | 0.00 USD | 4,330.00 USD | `-68.00%` | `14,561.30` |
| `Live` | `Long` | `0.3055` | 5,380,000.00 USD | 0.00 USD | 3,060.00 USD | `-67.14%` | `10,000.00` |
| `Live` | `Long` | `0.3115` | 5,380,000.00 USD | 0.00 USD | 270.38 USD | `-66.49%` | `868.00` |
| `Live` | `Long` | `0.3145` | 5,380,000.00 USD | 0.00 USD | 7,530.00 USD | `-66.17%` | `23,938.30` |
| `Live` | `Long` | `0.3205` | 5,370,000.00 USD | 0.00 USD | 693.98 USD | `-65.52%` | `2,165.30` |
| `Live` | `Long` | `0.3395` | 5,370,000.00 USD | 0.00 USD | 378.58 USD | `-63.48%` | `1,115.10` |
| `Live` | `Long` | `0.3415` | 5,370,000.00 USD | 0.00 USD | 167.51 USD | `-63.27%` | `490.50` |
| `Live` | `Long` | `0.3505` | 5,370,000.00 USD | 0.00 USD | 1,020.00 USD | `-62.30%` | `2,908.00` |
| `Live` | `Long` | `0.3535` | 5,370,000.00 USD | 0.00 USD | 622.87 USD | `-61.97%` | `1,762.00` |
| `Live` | `Long` | `0.3585` | 5,370,000.00 USD | 0.00 USD | 595.72 USD | `-61.44%` | `1,661.70` |
| `Live` | `Long` | `0.3595` | 5,370,000.00 USD | 0.00 USD | 9,270.00 USD | `-61.33%` | `25,791.20` |
| `Live` | `Long` | `0.3635` | 5,360,000.00 USD | 0.00 USD | 227.19 USD | `-60.90%` | `625.00` |
| `Live` | `Long` | `0.3665` | 5,360,000.00 USD | 0.00 USD | 274.88 USD | `-60.58%` | `750.00` |
| `Live` | `Long` | `0.3755` | 5,360,000.00 USD | 0.00 USD | 26,290.00 USD | `-59.61%` | `70,000.00` |
| `Live` | `Long` | `0.3775` | 5,330,000.00 USD | 0.00 USD | 6,420.00 USD | `-59.39%` | `17,000.00` |
| `Live` | `Long` | `0.3795` | 5,330,000.00 USD | 0.00 USD | 278.02 USD | `-59.18%` | `732.60` |
| `Live` | `Long` | `0.3845` | 5,330,000.00 USD | 0.00 USD | 1,750.00 USD | `-58.64%` | `4,562.20` |
| `Live` | `Long` | `0.3895` | 5,320,000.00 USD | 0.00 USD | 2,980.00 USD | `-58.10%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 5,320,000.00 USD | 0.00 USD | 5,030.00 USD | `-57.78%` | `12,808.60` |
| `Live` | `Long` | `0.4005` | 5,320,000.00 USD | 0.00 USD | 280.35 USD | `-56.92%` | `700.00` |
| `Live` | `Long` | `0.4035` | 5,320,000.00 USD | 0.00 USD | 935.03 USD | `-56.60%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 5,310,000.00 USD | 0.00 USD | 6,220.00 USD | `-56.49%` | `15,384.10` |
| `Live` | `Long` | `0.4115` | 5,310,000.00 USD | 0.00 USD | 699.55 USD | `-55.74%` | `1,700.00` |
| `Live` | `Long` | `0.4145` | 5,310,000.00 USD | 0.00 USD | 1,260.00 USD | `-55.41%` | `3,043.40` |
| `Live` | `Long` | `0.4185` | 5,310,000.00 USD | 0.00 USD | 102.62 USD | `-54.98%` | `245.20` |
| `Live` | `Long` | `0.4235` | 5,310,000.00 USD | 0.00 USD | 467.50 USD | `-54.45%` | `1,103.90` |
| `Live` | `Long` | `0.4325` | 5,310,000.00 USD | 0.00 USD | 391.46 USD | `-53.48%` | `905.10` |
| `Live` | `Long` | `0.4355` | 5,310,000.00 USD | 0.00 USD | 481.66 USD | `-53.15%` | `1,106.00` |
| `Live` | `Long` | `0.4375` | 5,310,000.00 USD | 0.00 USD | 43,580.00 USD | `-52.94%` | `99,611.70` |
| `Live` | `Long` | `0.4385` | 5,260,000.00 USD | 0.00 USD | 122.91 USD | `-52.83%` | `280.30` |
| `Live` | `Long` | `0.4415` | 5,260,000.00 USD | 0.00 USD | 5,800.00 USD | `-52.51%` | `13,146.20` |
| `Live` | `Long` | `0.4435` | 5,260,000.00 USD | 0.00 USD | 219.00 USD | `-52.29%` | `493.80` |
| `Live` | `Long` | `0.4445` | 5,260,000.00 USD | 0.00 USD | 573.54 USD | `-52.19%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 5,250,000.00 USD | 0.00 USD | 19,600.00 USD | `-51.97%` | `43,906.00` |
| `Live` | `Long` | `0.4495` | 5,240,000.00 USD | 0.00 USD | 78,660.00 USD | `-51.65%` | `175,000.00` |
| `Live` | `Long` | `0.4535` | 5,160,000.00 USD | 0.00 USD | 702.74 USD | `-51.22%` | `1,549.60` |
| `Live` | `Long` | `0.4595` | 5,160,000.00 USD | 0.00 USD | 1,480.00 USD | `-50.57%` | `3,228.50` |
| `Live` | `Long` | `0.4635` | 5,150,000.00 USD | 0.00 USD | 6,280.00 USD | `-50.14%` | `13,552.00` |
| `Live` | `Long` | `0.4725` | 5,150,000.00 USD | 0.00 USD | 5,330.00 USD | `-49.17%` | `11,290.30` |
| `Live` | `Long` | `0.4785` | 5,140,000.00 USD | 0.00 USD | 110.10 USD | `-48.53%` | `230.10` |
| `Live` | `Long` | `0.4795` | 5,140,000.00 USD | 0.00 USD | 33,560.00 USD | `-48.42%` | `70,000.00` |
| `Live` | `Long` | `0.4805` | 5,110,000.00 USD | 0.00 USD | 514.42 USD | `-48.31%` | `1,070.60` |
| `Live` | `Long` | `0.4835` | 5,110,000.00 USD | 0.00 USD | 174.01 USD | `-47.99%` | `359.90` |
| `Live` | `Long` | `0.4845` | 5,110,000.00 USD | 0.00 USD | 299.66 USD | `-47.88%` | `618.50` |
| `Live` | `Long` | `0.4865` | 5,110,000.00 USD | 0.00 USD | 201.07 USD | `-47.67%` | `413.30` |
| `Live` | `Long` | `0.4875` | 5,110,000.00 USD | 0.00 USD | 12,080.00 USD | `-47.56%` | `24,770.70` |
| `Live` | `Long` | `0.4885` | 5,100,000.00 USD | 0.00 USD | 1,050.00 USD | `-47.45%` | `2,151.80` |
| `Live` | `Long` | `0.4895` | 5,090,000.00 USD | 0.00 USD | 105.34 USD | `-47.35%` | `215.20` |
| `Live` | `Long` | `0.4915` | 5,090,000.00 USD | 0.00 USD | 2,380.00 USD | `-47.13%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 5,090,000.00 USD | 0.00 USD | 106.32 USD | `-46.81%` | `215.00` |
| `Live` | `Long` | `0.4955` | 5,090,000.00 USD | 0.00 USD | 3,120.00 USD | `-46.70%` | `6,305.00` |
| `Live` | `Long` | `0.4965` | 5,090,000.00 USD | 0.00 USD | 5,360.00 USD | `-46.59%` | `10,805.30` |
| `Live` | `Long` | `0.4975` | 5,080,000.00 USD | 0.00 USD | 3,330.00 USD | `-46.49%` | `6,701.80` |
| `Live` | `Long` | `0.4985` | 5,080,000.00 USD | 0.00 USD | 216.75 USD | `-46.38%` | `434.80` |
| `Live` | `Long` | `0.5015` | 5,080,000.00 USD | 0.00 USD | 212.49 USD | `-46.05%` | `423.70` |
| `Live` | `Long` | `0.5025` | 5,080,000.00 USD | 0.00 USD | 1,230.00 USD | `-45.95%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 5,080,000.00 USD | 0.00 USD | 211.25 USD | `-45.62%` | `417.90` |
| `Live` | `Long` | `0.5065` | 5,080,000.00 USD | 0.00 USD | 258.21 USD | `-45.52%` | `509.80` |
| `Live` | `Long` | `0.5085` | 5,080,000.00 USD | 0.00 USD | 2,540.00 USD | `-45.30%` | `5,000.00` |
| `Live` | `Long` | `0.5095` | 5,080,000.00 USD | 0.00 USD | 195.75 USD | `-45.19%` | `384.20` |
| `Live` | `Long` | `0.5105` | 5,080,000.00 USD | 0.00 USD | 847.53 USD | `-45.09%` | `1,660.20` |
| `Live` | `Long` | `0.5125` | 5,070,000.00 USD | 0.00 USD | 1,620.00 USD | `-44.87%` | `3,166.20` |
| `Live` | `Long` | `0.5145` | 5,070,000.00 USD | 0.00 USD | 276.39 USD | `-44.66%` | `537.20` |
| `Live` | `Long` | `0.5155` | 5,070,000.00 USD | 0.00 USD | 1,240.00 USD | `-44.55%` | `2,409.50` |
| `Live` | `Long` | `0.5165` | 5,070,000.00 USD | 0.00 USD | 619.80 USD | `-44.44%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 5,070,000.00 USD | 0.00 USD | 213.68 USD | `-44.33%` | `412.90` |
| `Live` | `Long` | `0.5185` | 5,070,000.00 USD | 0.00 USD | 2,450.00 USD | `-44.23%` | `4,734.80` |
| `Live` | `Long` | `0.5205` | 5,070,000.00 USD | 0.00 USD | 422.33 USD | `-44.01%` | `811.40` |
| `Live` | `Long` | `0.5225` | 5,070,000.00 USD | 0.00 USD | 244.90 USD | `-43.80%` | `468.70` |
| `Live` | `Long` | `0.5245` | 5,070,000.00 USD | 0.00 USD | 5,280.00 USD | `-43.58%` | `10,075.20` |
| `Live` | `Long` | `0.5275` | 5,060,000.00 USD | 0.00 USD | 348.36 USD | `-43.26%` | `660.40` |
| `Live` | `Long` | `0.5285` | 5,060,000.00 USD | 0.00 USD | 125,730.00 USD | `-43.15%` | `237,897.40` |
| `Live` | `Long` | `0.5295` | 4,940,000.00 USD | 0.00 USD | 264.06 USD | `-43.04%` | `498.70` |
| `Live` | `Long` | `0.5325` | 4,940,000.00 USD | 0.00 USD | 2,680.00 USD | `-42.72%` | `5,038.10` |
| `Live` | `Long` | `0.5335` | 4,930,000.00 USD | 0.00 USD | 1,040.00 USD | `-42.61%` | `1,952.90` |
| `Live` | `Long` | `0.5345` | 4,930,000.00 USD | 0.00 USD | 417.12 USD | `-42.51%` | `780.40` |
| `Live` | `Long` | `0.5375` | 4,930,000.00 USD | 0.00 USD | 1,190.00 USD | `-42.18%` | `2,206.50` |
| `Live` | `Long` | `0.5385` | 4,930,000.00 USD | 0.00 USD | 5,850.00 USD | `-42.07%` | `10,862.70` |
| `Live` | `Long` | `0.5395` | 4,920,000.00 USD | 0.00 USD | 319.98 USD | `-41.97%` | `593.10` |
| `Live` | `Long` | `0.5405` | 4,920,000.00 USD | 0.00 USD | 7,090.00 USD | `-41.86%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,920,000.00 USD | 0.00 USD | 269.13 USD | `-41.64%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,920,000.00 USD | 0.00 USD | 230.32 USD | `-41.43%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,920,000.00 USD | 0.00 USD | 1,670.00 USD | `-41.21%` | `3,059.10` |
| `Live` | `Long` | `0.5475` | 4,920,000.00 USD | 0.00 USD | 1,240.00 USD | `-41.11%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,910,000.00 USD | 0.00 USD | 28,790.00 USD | `-40.89%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,890,000.00 USD | 0.00 USD | 248.06 USD | `-40.78%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,880,000.00 USD | 0.00 USD | 160.93 USD | `-40.68%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,880,000.00 USD | 0.00 USD | 582.56 USD | `-40.57%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,880,000.00 USD | 0.00 USD | 271.88 USD | `-40.46%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,880,000.00 USD | 0.00 USD | 531.60 USD | `-40.35%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,880,000.00 USD | 0.00 USD | 16,060.00 USD | `-40.25%` | `28,914.00` |
| `Live` | `Long` | `0.5585` | 4,870,000.00 USD | 0.00 USD | 141.97 USD | `-39.92%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,870,000.00 USD | 0.00 USD | 304.93 USD | `-39.82%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,870,000.00 USD | 0.00 USD | 441.84 USD | `-39.71%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,870,000.00 USD | 0.00 USD | 330.53 USD | `-39.49%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,870,000.00 USD | 0.00 USD | 195.93 USD | `-39.39%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,870,000.00 USD | 0.00 USD | 8,190.00 USD | `-39.17%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,860,000.00 USD | 0.00 USD | 570.01 USD | `-39.06%` | `1,006.20` |
| `Live` | `Long` | `0.5675` | 4,860,000.00 USD | 0.00 USD | 1,560.00 USD | `-38.96%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,860,000.00 USD | 0.00 USD | 973.22 USD | `-38.74%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,850,000.00 USD | 0.00 USD | 139.23 USD | `-38.42%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,850,000.00 USD | 0.00 USD | 182.72 USD | `-38.31%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,850,000.00 USD | 0.00 USD | 144.03 USD | `-38.20%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,850,000.00 USD | 0.00 USD | 1,010.00 USD | `-38.09%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,850,000.00 USD | 0.00 USD | 1,150.00 USD | `-37.99%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,850,000.00 USD | 0.00 USD | 497.75 USD | `-37.88%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,850,000.00 USD | 0.00 USD | 227.41 USD | `-37.77%` | `393.10` |
| `Live` | `Long` | `0.5795` | 4,850,000.00 USD | 0.00 USD | 104.60 USD | `-37.66%` | `180.50` |
| `Live` | `Long` | `0.5805` | 4,850,000.00 USD | 0.00 USD | 1,410.00 USD | `-37.56%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,850,000.00 USD | 0.00 USD | 18,120.00 USD | `-37.34%` | `31,099.00` |
| `Live` | `Long` | `0.5845` | 4,830,000.00 USD | 0.00 USD | 292,250.00 USD | `-37.13%` | `500,000.00` |
| `Live` | `Long` | `0.5855` | 4,540,000.00 USD | 0.00 USD | 2,640.00 USD | `-37.02%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,540,000.00 USD | 0.00 USD | 466.85 USD | `-36.91%` | `796.00` |
| `Live` | `Long` | `0.5875` | 4,540,000.00 USD | 0.00 USD | 969.32 USD | `-36.80%` | `1,649.90` |
| `Live` | `Long` | `0.5885` | 4,540,000.00 USD | 0.00 USD | 311.14 USD | `-36.70%` | `528.70` |
| `Live` | `Long` | `0.5925` | 4,530,000.00 USD | 0.00 USD | 994.16 USD | `-36.27%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,530,000.00 USD | 0.00 USD | 132.41 USD | `-36.16%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,530,000.00 USD | 0.00 USD | 8,220.00 USD | `-36.05%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,530,000.00 USD | 0.00 USD | 5,540.00 USD | `-35.84%` | `9,295.80` |
| `Live` | `Long` | `0.5995` | 4,520,000.00 USD | 0.00 USD | 151.97 USD | `-35.51%` | `253.50` |
| `Live` | `Long` | `0.6005` | 4,520,000.00 USD | 0.00 USD | 351.11 USD | `-35.41%` | `584.70` |
| `Live` | `Long` | `0.6025` | 4,520,000.00 USD | 0.00 USD | 432.35 USD | `-35.19%` | `717.60` |
| `Live` | `Long` | `0.6035` | 4,520,000.00 USD | 0.00 USD | 48,180.00 USD | `-35.08%` | `79,832.70` |
| `Live` | `Long` | `0.6065` | 4,470,000.00 USD | 0.00 USD | 10,680.00 USD | `-34.76%` | `17,611.30` |
| `Live` | `Long` | `0.6075` | 4,460,000.00 USD | 0.00 USD | 851.05 USD | `-34.65%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,460,000.00 USD | 0.00 USD | 272.24 USD | `-34.55%` | `447.40` |
| `Live` | `Long` | `0.6115` | 4,460,000.00 USD | 0.00 USD | 6,780.00 USD | `-34.22%` | `11,093.80` |
| `Live` | `Long` | `0.6125` | 4,450,000.00 USD | 0.00 USD | 213.64 USD | `-34.11%` | `348.80` |
| `Live` | `Long` | `0.6135` | 4,450,000.00 USD | 0.00 USD | 245.40 USD | `-34.01%` | `400.00` |
| `Live` | `Long` | `0.6145` | 4,450,000.00 USD | 0.00 USD | 141,660.00 USD | `-33.90%` | `230,521.60` |
| `Live` | `Long` | `0.6155` | 4,310,000.00 USD | 0.00 USD | 2,060.00 USD | `-33.79%` | `3,346.30` |
| `Live` | `Long` | `0.6165` | 4,310,000.00 USD | 0.00 USD | 29,900.00 USD | `-33.68%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 4,280,000.00 USD | 0.00 USD | 1,540.00 USD | `-33.58%` | `2,500.00` |
| `Live` | `Long` | `0.6185` | 4,280,000.00 USD | 0.00 USD | 4,400.00 USD | `-33.47%` | `7,107.00` |
| `Live` | `Long` | `0.6245` | 4,270,000.00 USD | 0.00 USD | 356.65 USD | `-32.82%` | `571.10` |
| `Live` | `Long` | `0.6255` | 4,270,000.00 USD | 0.00 USD | 32,070.00 USD | `-32.72%` | `51,265.70` |
| `Live` | `Long` | `0.6265` | 4,240,000.00 USD | 0.00 USD | 546.18 USD | `-32.61%` | `871.80` |
| `Live` | `Long` | `0.6285` | 4,240,000.00 USD | 0.00 USD | 102.45 USD | `-32.39%` | `163.00` |
| `Live` | `Long` | `0.6305` | 4,240,000.00 USD | 0.00 USD | 319.35 USD | `-32.18%` | `506.50` |
| `Live` | `Long` | `0.6315` | 4,240,000.00 USD | 0.00 USD | 3,510.00 USD | `-32.07%` | `5,564.80` |
| `Live` | `Long` | `0.6335` | 4,240,000.00 USD | 0.00 USD | 3,130.00 USD | `-31.86%` | `4,946.60` |
| `Live` | `Long` | `0.6345` | 4,230,000.00 USD | 0.00 USD | 450.05 USD | `-31.75%` | `709.30` |
| `Live` | `Long` | `0.6355` | 4,230,000.00 USD | 0.00 USD | 207.17 USD | `-31.64%` | `326.00` |
| `Live` | `Long` | `0.6365` | 4,230,000.00 USD | 0.00 USD | 2,850.00 USD | `-31.53%` | `4,478.70` |
| `Live` | `Long` | `0.6375` | 4,230,000.00 USD | 0.00 USD | 2,240.00 USD | `-31.43%` | `3,513.60` |
| `Live` | `Long` | `0.6395` | 4,230,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.21%` | `2,636.90` |
| `Live` | `Long` | `0.6405` | 4,220,000.00 USD | 0.00 USD | 939.17 USD | `-31.10%` | `1,466.30` |
| `Live` | `Long` | `0.6415` | 4,220,000.00 USD | 0.00 USD | 94,330.00 USD | `-31.00%` | `147,042.90` |
| `Live` | `Long` | `0.6425` | 4,130,000.00 USD | 0.00 USD | 477.63 USD | `-30.89%` | `743.40` |
| `Live` | `Long` | `0.6435` | 4,130,000.00 USD | 0.00 USD | 8,530.00 USD | `-30.78%` | `13,261.20` |
| `Live` | `Long` | `0.6445` | 4,120,000.00 USD | 0.00 USD | 65,790.00 USD | `-30.67%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 4,050,000.00 USD | 0.00 USD | 471.21 USD | `-30.57%` | `730.00` |
| `Live` | `Long` | `0.6475` | 4,050,000.00 USD | 0.00 USD | 3,910.00 USD | `-30.35%` | `6,031.70` |
| `Live` | `Long` | `0.6485` | 4,050,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.24%` | `6,766.10` |
| `Live` | `Long` | `0.6495` | 4,050,000.00 USD | 0.00 USD | 721.59 USD | `-30.13%` | `1,111.00` |
| `Live` | `Long` | `0.6505` | 4,050,000.00 USD | 0.00 USD | 631.12 USD | `-30.03%` | `970.20` |
| `Live` | `Long` | `0.6515` | 4,040,000.00 USD | 0.00 USD | 408,650.00 USD | `-29.92%` | `627,245.30` |
| `Live` | `Long` | `0.6535` | 3,640,000.00 USD | 0.00 USD | 126,530.00 USD | `-29.70%` | `193,618.10` |
| `Live` | `Long` | `0.6555` | 3,510,000.00 USD | 0.00 USD | 1,730.00 USD | `-29.49%` | `2,634.80` |
| `Live` | `Long` | `0.6565` | 3,510,000.00 USD | 0.00 USD | 7,700.00 USD | `-29.38%` | `11,722.00` |
| `Live` | `Long` | `0.6575` | 3,500,000.00 USD | 0.00 USD | 13,280.00 USD | `-29.27%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,490,000.00 USD | 0.00 USD | 2,970.00 USD | `-29.17%` | `4,508.30` |
| `Live` | `Long` | `0.6615` | 3,480,000.00 USD | 0.00 USD | 13,150.00 USD | `-28.84%` | `19,885.40` |
| `Live` | `Long` | `0.6625` | 3,470,000.00 USD | 0.00 USD | 788.97 USD | `-28.74%` | `1,190.90` |
| `Live` | `Long` | `0.6645` | 3,470,000.00 USD | 0.00 USD | 448.54 USD | `-28.52%` | `675.00` |
| `Live` | `Long` | `0.6675` | 3,470,000.00 USD | 0.00 USD | 5,280.00 USD | `-28.20%` | `7,907.60` |
| `Live` | `Long` | `0.6685` | 3,460,000.00 USD | 0.00 USD | 2,810.00 USD | `-28.09%` | `4,203.00` |
| `Live` | `Long` | `0.6695` | 3,460,000.00 USD | 0.00 USD | 161.22 USD | `-27.98%` | `240.80` |
| `Live` | `Long` | `0.6705` | 3,460,000.00 USD | 0.00 USD | 2,290.00 USD | `-27.88%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,460,000.00 USD | 0.00 USD | 8,500.00 USD | `-27.77%` | `12,661.20` |
| `Live` | `Long` | `0.6725` | 3,450,000.00 USD | 0.00 USD | 1,500.00 USD | `-27.66%` | `2,227.70` |
| `Live` | `Long` | `0.6735` | 3,450,000.00 USD | 0.00 USD | 633.09 USD | `-27.55%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,450,000.00 USD | 0.00 USD | 35,930.00 USD | `-27.45%` | `53,274.60` |
| `Live` | `Long` | `0.6755` | 3,410,000.00 USD | 0.00 USD | 111.59 USD | `-27.34%` | `165.20` |
| `Live` | `Long` | `0.6765` | 3,410,000.00 USD | 0.00 USD | 1,040.00 USD | `-27.23%` | `1,539.20` |
| `Live` | `Long` | `0.6785` | 3,410,000.00 USD | 0.00 USD | 10,350.00 USD | `-27.02%` | `15,251.40` |
| `Live` | `Long` | `0.6795` | 3,400,000.00 USD | 0.00 USD | 5,620.00 USD | `-26.91%` | `8,270.70` |
| `Live` | `Long` | `0.6805` | 3,400,000.00 USD | 0.00 USD | 1,600.00 USD | `-26.80%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 3,390,000.00 USD | 0.00 USD | 3,380.00 USD | `-26.69%` | `4,954.70` |
| `Live` | `Long` | `0.6825` | 3,390,000.00 USD | 0.00 USD | 15,920.00 USD | `-26.59%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 3,370,000.00 USD | 0.00 USD | 6,350.00 USD | `-26.48%` | `9,292.50` |
| `Live` | `Long` | `0.6845` | 3,370,000.00 USD | 0.00 USD | 5,790.00 USD | `-26.37%` | `8,455.80` |
| `Live` | `Long` | `0.6875` | 3,360,000.00 USD | 0.00 USD | 480.49 USD | `-26.05%` | `698.90` |
| `Live` | `Long` | `0.6885` | 3,360,000.00 USD | 0.00 USD | 83,790.00 USD | `-25.94%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 3,280,000.00 USD | 0.00 USD | 2,110.00 USD | `-25.83%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 3,280,000.00 USD | 0.00 USD | 3,360.00 USD | `-25.72%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 3,270,000.00 USD | 0.00 USD | 8,970.00 USD | `-25.62%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 3,260,000.00 USD | 0.00 USD | 3,670.00 USD | `-25.40%` | `5,287.80` |
| `Live` | `Long` | `0.6945` | 3,260,000.00 USD | 0.00 USD | 669.50 USD | `-25.29%` | `964.00` |
| `Live` | `Long` | `0.6965` | 3,260,000.00 USD | 0.00 USD | 8,940.00 USD | `-25.08%` | `12,833.30` |
| `Live` | `Long` | `0.6985` | 3,250,000.00 USD | 0.00 USD | 1,930.00 USD | `-24.86%` | `2,759.10` |
| `Live` | `Long` | `0.7035` | 3,250,000.00 USD | 0.00 USD | 1,390.00 USD | `-24.33%` | `1,977.40` |
| `Live` | `Long` | `0.7045` | 3,250,000.00 USD | 0.00 USD | 759.59 USD | `-24.22%` | `1,078.20` |
| `Live` | `Long` | `0.7065` | 3,250,000.00 USD | 0.00 USD | 769.59 USD | `-24.00%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 3,250,000.00 USD | 0.00 USD | 787.73 USD | `-23.90%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 3,240,000.00 USD | 0.00 USD | 3,890.00 USD | `-23.79%` | `5,484.60` |
| `Live` | `Long` | `0.7095` | 3,240,000.00 USD | 0.00 USD | 2,550.00 USD | `-23.68%` | `3,589.20` |
| `Live` | `Long` | `0.7105` | 3,240,000.00 USD | 0.00 USD | 3,530.00 USD | `-23.57%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 3,230,000.00 USD | 0.00 USD | 569.20 USD | `-23.47%` | `800.00` |
| `Live` | `Long` | `0.7125` | 3,230,000.00 USD | 0.00 USD | 156.39 USD | `-23.36%` | `219.50` |
| `Live` | `Long` | `0.7145` | 3,230,000.00 USD | 0.00 USD | 22,830.00 USD | `-23.14%` | `31,949.70` |
| `Live` | `Long` | `0.7175` | 3,210,000.00 USD | 0.00 USD | 1,470.00 USD | `-22.82%` | `2,050.00` |
| `Live` | `Long` | `0.7195` | 3,210,000.00 USD | 0.00 USD | 11,720.00 USD | `-22.61%` | `16,293.90` |
| `Live` | `Long` | `0.7225` | 3,200,000.00 USD | 0.00 USD | 129.26 USD | `-22.28%` | `178.90` |
| `Live` | `Long` | `0.7255` | 3,200,000.00 USD | 0.00 USD | 2,660.00 USD | `-21.96%` | `3,662.80` |
| `Live` | `Long` | `0.7265` | 3,190,000.00 USD | 0.00 USD | 1,060.00 USD | `-21.85%` | `1,453.70` |
| `Live` | `Long` | `0.7275` | 3,190,000.00 USD | 0.00 USD | 762.57 USD | `-21.74%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 3,190,000.00 USD | 0.00 USD | 214.03 USD | `-21.64%` | `293.80` |
| `Live` | `Long` | `0.7295` | 3,190,000.00 USD | 0.00 USD | 375.98 USD | `-21.53%` | `515.40` |
| `Live` | `Long` | `0.7305` | 3,190,000.00 USD | 0.00 USD | 119.88 USD | `-21.42%` | `164.10` |
| `Live` | `Long` | `0.7325` | 3,190,000.00 USD | 0.00 USD | 907.93 USD | `-21.21%` | `1,239.50` |
| `Live` | `Long` | `0.7345` | 3,190,000.00 USD | 0.00 USD | 2,340.00 USD | `-20.99%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 3,190,000.00 USD | 0.00 USD | 51,920.00 USD | `-20.88%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 3,140,000.00 USD | 0.00 USD | 311,430.00 USD | `-20.78%` | `422,854.90` |
| `Live` | `Long` | `0.7385` | 2,830,000.00 USD | 0.00 USD | 5,810.00 USD | `-20.56%` | `7,871.10` |
| `Live` | `Long` | `0.7395` | 2,820,000.00 USD | 0.00 USD | 578.07 USD | `-20.45%` | `781.70` |
| `Live` | `Long` | `0.7405` | 2,820,000.00 USD | 0.00 USD | 3,530.00 USD | `-20.35%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,820,000.00 USD | 0.00 USD | 510.15 USD | `-20.24%` | `688.00` |
| `Live` | `Long` | `0.7425` | 2,820,000.00 USD | 0.00 USD | 784,090.00 USD | `-20.13%` | `1,056,015.30` |
| `Live` | `Long` | `0.7435` | 2,030,000.00 USD | 0.00 USD | 43,970.00 USD | `-20.02%` | `59,132.90` |
| `Live` | `Long` | `0.7445` | 1,990,000.00 USD | 0.00 USD | 1,640.00 USD | `-19.92%` | `2,207.10` |
| `Live` | `Long` | `0.7475` | 1,990,000.00 USD | 0.00 USD | 103,910.00 USD | `-19.59%` | `139,007.00` |
| `Live` | `Long` | `0.7485` | 1,880,000.00 USD | 0.00 USD | 105.91 USD | `-19.49%` | `141.50` |
| `Live` | `Long` | `0.7495` | 1,880,000.00 USD | 0.00 USD | 811.78 USD | `-19.38%` | `1,083.10` |
| `Live` | `Long` | `0.7515` | 1,880,000.00 USD | 0.00 USD | 1,340.00 USD | `-19.16%` | `1,779.90` |
| `Live` | `Long` | `0.7525` | 1,880,000.00 USD | 0.00 USD | 106.03 USD | `-19.06%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,880,000.00 USD | 0.00 USD | 1,200.00 USD | `-18.95%` | `1,588.10` |
| `Live` | `Long` | `0.7545` | 1,880,000.00 USD | 0.00 USD | 922.07 USD | `-18.84%` | `1,222.10` |
| `Live` | `Long` | `0.7575` | 1,880,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.52%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,880,000.00 USD | 0.00 USD | 36,710.00 USD | `-18.41%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,840,000.00 USD | 0.00 USD | 4,390.00 USD | `-18.30%` | `5,776.10` |
| `Live` | `Long` | `0.7615` | 1,830,000.00 USD | 0.00 USD | 1,910.00 USD | `-18.09%` | `2,503.90` |
| `Live` | `Long` | `0.7635` | 1,830,000.00 USD | 0.00 USD | 2,210.00 USD | `-17.87%` | `2,890.10` |
| `Live` | `Long` | `0.7645` | 1,830,000.00 USD | 0.00 USD | 1,060.00 USD | `-17.76%` | `1,384.30` |
| `Live` | `Long` | `0.7655` | 1,830,000.00 USD | 0.00 USD | 4,430.00 USD | `-17.66%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,820,000.00 USD | 0.00 USD | 2,360.00 USD | `-17.55%` | `3,074.70` |
| `Live` | `Long` | `0.7675` | 1,820,000.00 USD | 0.00 USD | 10,680.00 USD | `-17.44%` | `13,912.80` |
| `Live` | `Long` | `0.7685` | 1,810,000.00 USD | 0.00 USD | 2,750.00 USD | `-17.33%` | `3,578.60` |
| `Live` | `Long` | `0.7695` | 1,810,000.00 USD | 0.00 USD | 144,250.00 USD | `-17.23%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 1,660,000.00 USD | 0.00 USD | 8,730.00 USD | `-17.12%` | `11,331.10` |
| `Live` | `Long` | `0.7715` | 1,660,000.00 USD | 0.00 USD | 3,190.00 USD | `-17.01%` | `4,137.70` |
| `Live` | `Long` | `0.7725` | 1,650,000.00 USD | 0.00 USD | 6,810.00 USD | `-16.90%` | `8,810.50` |
| `Live` | `Long` | `0.7735` | 1,650,000.00 USD | 0.00 USD | 4,570.00 USD | `-16.80%` | `5,912.10` |
| `Live` | `Long` | `0.7755` | 1,640,000.00 USD | 0.00 USD | 126.41 USD | `-16.58%` | `163.00` |
| `Live` | `Long` | `0.7765` | 1,640,000.00 USD | 0.00 USD | 4,630.00 USD | `-16.47%` | `5,964.40` |
| `Live` | `Long` | `0.7785` | 1,640,000.00 USD | 0.00 USD | 7,000.00 USD | `-16.26%` | `8,985.30` |
| `Live` | `Long` | `0.7795` | 1,630,000.00 USD | 0.00 USD | 444.63 USD | `-16.15%` | `570.40` |
| `Live` | `Long` | `0.7805` | 1,630,000.00 USD | 0.00 USD | 24,600.00 USD | `-16.04%` | `31,516.40` |
| `Live` | `Long` | `0.7815` | 1,600,000.00 USD | 0.00 USD | 4,630.00 USD | `-15.94%` | `5,918.40` |
| `Live` | `Long` | `0.7835` | 1,600,000.00 USD | 0.00 USD | 950.23 USD | `-15.72%` | `1,212.80` |
| `Live` | `Long` | `0.7855` | 1,600,000.00 USD | 0.00 USD | 3,020.00 USD | `-15.51%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 1,600,000.00 USD | 0.00 USD | 2,870.00 USD | `-15.40%` | `3,651.90` |
| `Live` | `Long` | `0.7875` | 1,590,000.00 USD | 0.00 USD | 5,400.00 USD | `-15.29%` | `6,852.00` |
| `Live` | `Long` | `0.7895` | 1,590,000.00 USD | 0.00 USD | 8,660.00 USD | `-15.08%` | `10,969.90` |
| `Live` | `Long` | `0.7905` | 1,580,000.00 USD | 0.00 USD | 3,670.00 USD | `-14.97%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 1,580,000.00 USD | 0.00 USD | 1,290.00 USD | `-14.86%` | `1,623.50` |
| `Live` | `Long` | `0.7925` | 1,570,000.00 USD | 0.00 USD | 385.87 USD | `-14.75%` | `486.90` |
| `Live` | `Long` | `0.7935` | 1,570,000.00 USD | 0.00 USD | 2,220.00 USD | `-14.65%` | `2,799.50` |
| `Live` | `Long` | `0.7945` | 1,570,000.00 USD | 0.00 USD | 7,640.00 USD | `-14.54%` | `9,619.00` |
| `Live` | `Long` | `0.7955` | 1,560,000.00 USD | 0.00 USD | 23,610.00 USD | `-14.43%` | `29,676.80` |
| `Live` | `Long` | `0.7975` | 1,540,000.00 USD | 0.00 USD | 1,170.00 USD | `-14.22%` | `1,464.30` |
| `Live` | `Long` | `0.7985` | 1,540,000.00 USD | 0.00 USD | 643.43 USD | `-14.11%` | `805.80` |
| `Live` | `Long` | `0.7995` | 1,540,000.00 USD | 0.00 USD | 2,770.00 USD | `-14.00%` | `3,466.90` |
| `Live` | `Long` | `0.8005` | 1,540,000.00 USD | 0.00 USD | 43,710.00 USD | `-13.89%` | `54,603.20` |
| `Live` | `Long` | `0.8015` | 1,490,000.00 USD | 0.00 USD | 86,410.00 USD | `-13.78%` | `107,816.10` |
| `Live` | `Long` | `0.8025` | 1,410,000.00 USD | 0.00 USD | 421.31 USD | `-13.68%` | `525.00` |
| `Live` | `Long` | `0.8035` | 1,410,000.00 USD | 0.00 USD | 9,920.00 USD | `-13.57%` | `12,344.10` |
| `Live` | `Long` | `0.8045` | 1,400,000.00 USD | 0.00 USD | 42,240.00 USD | `-13.46%` | `52,508.10` |
| `Live` | `Long` | `0.8055` | 1,350,000.00 USD | 0.00 USD | 1,610.00 USD | `-13.35%` | `2,000.00` |
| `Live` | `Long` | `0.8085` | 1,350,000.00 USD | 0.00 USD | 22,170.00 USD | `-13.03%` | `27,427.20` |
| `Live` | `Long` | `0.8105` | 1,330,000.00 USD | 0.00 USD | 5,190.00 USD | `-12.82%` | `6,403.40` |
| `Live` | `Long` | `0.8115` | 1,320,000.00 USD | 0.00 USD | 146.48 USD | `-12.71%` | `180.50` |
| `Live` | `Long` | `0.8125` | 1,320,000.00 USD | 0.00 USD | 2,480.00 USD | `-12.60%` | `3,054.20` |
| `Live` | `Long` | `0.8135` | 1,320,000.00 USD | 0.00 USD | 11,260.00 USD | `-12.49%` | `13,843.50` |
| `Live` | `Long` | `0.8145` | 1,310,000.00 USD | 0.00 USD | 277.42 USD | `-12.39%` | `340.60` |
| `Live` | `Long` | `0.8155` | 1,310,000.00 USD | 0.00 USD | 8,160.00 USD | `-12.28%` | `10,000.00` |
| `Live` | `Long` | `0.8165` | 1,300,000.00 USD | 0.00 USD | 571.79 USD | `-12.17%` | `700.30` |
| `Live` | `Long` | `0.8175` | 1,300,000.00 USD | 0.00 USD | 103,660.00 USD | `-12.06%` | `126,800.10` |
| `Live` | `Long` | `0.8185` | 1,200,000.00 USD | 0.00 USD | 491.10 USD | `-11.96%` | `600.00` |
| `Live` | `Long` | `0.8195` | 1,200,000.00 USD | 0.00 USD | 643.31 USD | `-11.85%` | `785.00` |
| `Live` | `Long` | `0.8205` | 1,200,000.00 USD | 0.00 USD | 2,280.00 USD | `-11.74%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 1,190,000.00 USD | 0.00 USD | 5,180.00 USD | `-11.63%` | `6,300.50` |
| `Live` | `Long` | `0.8225` | 1,190,000.00 USD | 0.00 USD | 466.85 USD | `-11.53%` | `567.60` |
| `Live` | `Long` | `0.8235` | 1,190,000.00 USD | 0.00 USD | 216.00 USD | `-11.42%` | `262.30` |
| `Live` | `Long` | `0.8245` | 1,190,000.00 USD | 0.00 USD | 3,640.00 USD | `-11.31%` | `4,409.80` |
| `Live` | `Long` | `0.8255` | 1,180,000.00 USD | 0.00 USD | 317.82 USD | `-11.20%` | `385.00` |
| `Live` | `Long` | `0.8275` | 1,180,000.00 USD | 0.00 USD | 11,410.00 USD | `-10.99%` | `13,785.20` |
| `Live` | `Long` | `0.8285` | 1,170,000.00 USD | 0.00 USD | 118,200.00 USD | `-10.88%` | `142,661.50` |
| `Live` | `Long` | `0.8295` | 1,050,000.00 USD | 0.00 USD | 32,530.00 USD | `-10.77%` | `39,217.20` |
| `Live` | `Long` | `0.8305` | 1,020,000.00 USD | 0.00 USD | 1,670.00 USD | `-10.67%` | `2,011.70` |
| `Live` | `Long` | `0.8325` | 1,020,000.00 USD | 0.00 USD | 18,980.00 USD | `-10.45%` | `22,795.90` |
| `Live` | `Long` | `0.8355` | 1,000,000.00 USD | 0.00 USD | 18,570.00 USD | `-10.13%` | `22,231.90` |
| `Live` | `Long` | `0.8365` | 982,870.00 USD | 0.00 USD | 11,000.00 USD | `-10.02%` | `13,149.30` |
| `Live` | `Long` | `0.8375` | 971,870.00 USD | 0.00 USD | 137.85 USD | `-9.91%` | `164.60` |
| `Live` | `Long` | `0.8385` | 971,730.00 USD | 0.00 USD | 79,450.00 USD | `-9.80%` | `94,750.80` |
| `Live` | `Long` | `0.8395` | 892,280.00 USD | 0.00 USD | 27,150.00 USD | `-9.70%` | `32,340.20` |
| `Live` | `Long` | `0.8405` | 865,130.00 USD | 0.00 USD | 628.27 USD | `-9.59%` | `747.50` |
| `Live` | `Long` | `0.8415` | 864,500.00 USD | 0.00 USD | 9,110.00 USD | `-9.48%` | `10,825.10` |
| `Live` | `Long` | `0.8425` | 855,390.00 USD | 0.00 USD | 8,460.00 USD | `-9.37%` | `10,043.20` |
| `Live` | `Long` | `0.8435` | 846,930.00 USD | 0.00 USD | 6,280.00 USD | `-9.27%` | `7,446.40` |
| `Live` | `Long` | `0.8445` | 840,650.00 USD | 0.00 USD | 893.23 USD | `-9.16%` | `1,057.70` |
| `Live` | `Long` | `0.8455` | 839,760.00 USD | 0.00 USD | 6,630.00 USD | `-9.05%` | `7,840.60` |
| `Live` | `Long` | `0.8465` | 833,130.00 USD | 0.00 USD | 15,830.00 USD | `-8.94%` | `18,696.70` |
| `Live` | `Long` | `0.8475` | 817,300.00 USD | 0.00 USD | 29,810.00 USD | `-8.84%` | `35,169.30` |
| `Live` | `Long` | `0.8485` | 787,500.00 USD | 0.00 USD | 1,890.00 USD | `-8.73%` | `2,222.00` |
| `Live` | `Long` | `0.8495` | 785,610.00 USD | 0.00 USD | 804.99 USD | `-8.62%` | `947.60` |
| `Live` | `Long` | `0.8515` | 784,810.00 USD | 0.00 USD | 1,220.00 USD | `-8.41%` | `1,433.90` |
| `Live` | `Long` | `0.8525` | 783,580.00 USD | 0.00 USD | 17,050.00 USD | `-8.30%` | `20,000.00` |
| `Live` | `Long` | `0.8535` | 766,530.00 USD | 0.00 USD | 15,640.00 USD | `-8.19%` | `18,326.40` |
| `Live` | `Long` | `0.8545` | 750,890.00 USD | 0.00 USD | 2,030.00 USD | `-8.08%` | `2,375.90` |
| `Live` | `Long` | `0.8555` | 748,860.00 USD | 0.00 USD | 139.53 USD | `-7.98%` | `163.10` |
| `Live` | `Long` | `0.8565` | 748,720.00 USD | 0.00 USD | 36,350.00 USD | `-7.87%` | `42,440.00` |
| `Live` | `Long` | `0.8585` | 712,370.00 USD | 0.00 USD | 24,590.00 USD | `-7.65%` | `28,644.90` |
| `Live` | `Long` | `0.8595` | 687,780.00 USD | 0.00 USD | 7,610.00 USD | `-7.55%` | `8,848.50` |
| `Live` | `Long` | `0.8605` | 680,180.00 USD | 0.00 USD | 19,020.00 USD | `-7.44%` | `22,098.50` |
| `Live` | `Long` | `0.8615` | 661,160.00 USD | 0.00 USD | 793.18 USD | `-7.33%` | `920.70` |
| `Live` | `Long` | `0.8625` | 660,370.00 USD | 0.00 USD | 9,140.00 USD | `-7.22%` | `10,602.70` |
| `Live` | `Long` | `0.8635` | 651,220.00 USD | 0.00 USD | 4,710.00 USD | `-7.12%` | `5,449.60` |
| `Live` | `Long` | `0.8645` | 646,520.00 USD | 0.00 USD | 2,580.00 USD | `-7.01%` | `2,988.60` |
| `Live` | `Long` | `0.8655` | 643,930.00 USD | 0.00 USD | 1,230.00 USD | `-6.90%` | `1,426.30` |
| `Live` | `Long` | `0.8665` | 642,700.00 USD | 0.00 USD | 1,340.00 USD | `-6.79%` | `1,550.90` |
| `Live` | `Long` | `0.8675` | 641,360.00 USD | 0.00 USD | 11,820.00 USD | `-6.69%` | `13,628.20` |
| `Live` | `Long` | `0.8685` | 629,530.00 USD | 0.00 USD | 289.04 USD | `-6.58%` | `332.80` |
| `Live` | `Long` | `0.8695` | 629,240.00 USD | 0.00 USD | 6,680.00 USD | `-6.47%` | `7,680.60` |
| `Live` | `Long` | `0.8705` | 622,570.00 USD | 0.00 USD | 10,230.00 USD | `-6.36%` | `11,751.60` |
| `Live` | `Long` | `0.8715` | 612,340.00 USD | 0.00 USD | 7,540.00 USD | `-6.26%` | `8,654.90` |
| `Live` | `Long` | `0.8725` | 604,790.00 USD | 0.00 USD | 29,520.00 USD | `-6.15%` | `33,829.20` |
| `Live` | `Long` | `0.8735` | 575,280.00 USD | 0.00 USD | 129,080.00 USD | `-6.04%` | `147,768.00` |
| `Live` | `Long` | `0.8745` | 446,200.00 USD | 0.00 USD | 13,880.00 USD | `-5.93%` | `15,872.80` |
| `Live` | `Long` | `0.8755` | 432,320.00 USD | 0.00 USD | 1,420.00 USD | `-5.82%` | `1,624.00` |
| `Live` | `Long` | `0.8765` | 430,900.00 USD | 0.00 USD | 33,770.00 USD | `-5.72%` | `38,532.60` |
| `Live` | `Long` | `0.8775` | 397,130.00 USD | 0.00 USD | 16,030.00 USD | `-5.61%` | `18,270.50` |
| `Live` | `Long` | `0.8785` | 381,090.00 USD | 0.00 USD | 56,160.00 USD | `-5.50%` | `63,924.50` |
| `Live` | `Long` | `0.8795` | 324,940.00 USD | 0.00 USD | 172,470.00 USD | `-5.39%` | `196,099.30` |
| `Live` | `Long` | `0.8805` | 152,470.00 USD | 0.00 USD | 1,530.00 USD | `-5.29%` | `1,737.40` |
| `Live` | `Long` | `0.8815` | 150,940.00 USD | 0.00 USD | 9,320.00 USD | `-5.18%` | `10,573.20` |
| `Live` | `Long` | `0.8825` | 141,620.00 USD | 0.00 USD | 6,950.00 USD | `-5.07%` | `7,879.60` |
| `Live` | `Long` | `0.8835` | 134,660.00 USD | 0.00 USD | 2,330.00 USD | `-4.96%` | `2,634.40` |
| `Live` | `Long` | `0.8845` | 132,330.00 USD | 0.00 USD | 3,550.00 USD | `-4.86%` | `4,018.00` |
| `Live` | `Long` | `0.8855` | 128,780.00 USD | 0.00 USD | 2,660.00 USD | `-4.75%` | `2,998.60` |
| `Live` | `Long` | `0.8865` | 126,130.00 USD | 0.00 USD | 35,970.00 USD | `-4.64%` | `40,570.10` |
| `Live` | `Long` | `0.8875` | 90,160.00 USD | 0.00 USD | 13,890.00 USD | `-4.53%` | `15,652.60` |
| `Live` | `Long` | `0.8885` | 76,270.00 USD | 0.00 USD | 1,310.00 USD | `-4.43%` | `1,476.10` |
| `Live` | `Long` | `0.8895` | 74,960.00 USD | 0.00 USD | 3,530.00 USD | `-4.32%` | `3,972.10` |
| `Live` | `Long` | `0.8905` | 71,420.00 USD | 0.00 USD | 139.90 USD | `-4.21%` | `157.10` |
| `Live` | `Long` | `0.8915` | 71,280.00 USD | 0.00 USD | 1,100.00 USD | `-4.10%` | `1,229.80` |
| `Live` | `Long` | `0.8925` | 70,190.00 USD | 0.00 USD | 1,040.00 USD | `-4.00%` | `1,162.90` |
| `Live` | `Long` | `0.8935` | 69,150.00 USD | 0.00 USD | 23,520.00 USD | `-3.89%` | `26,319.40` |
| `Live` | `Long` | `0.8945` | 45,630.00 USD | 0.00 USD | 5,750.00 USD | `-3.78%` | `6,428.20` |
| `Live` | `Long` | `0.8955` | 39,880.00 USD | 0.00 USD | 257.01 USD | `-3.67%` | `287.00` |
| `Live` | `Long` | `0.8965` | 39,630.00 USD | 0.00 USD | 29,550.00 USD | `-3.57%` | `32,958.10` |
| `Live` | `Long` | `0.8975` | 10,080.00 USD | 0.00 USD | 3,540.00 USD | `-3.46%` | `3,941.60` |
| `Live` | `Long` | `0.8985` | 6,540.00 USD | 0.00 USD | 320.05 USD | `-3.35%` | `356.20` |
| `Live` | `Long` | `0.8995` | 6,220.00 USD | 0.00 USD | 143.92 USD | `-3.24%` | `160.00` |
| `Live` | `Long` | `0.9055` | 6,080.00 USD | 0.00 USD | 119.44 USD | `-2.60%` | `131.90` |
| `Live` | `Long` | `0.9075` | 5,960.00 USD | 0.00 USD | 5,960.00 USD | `-2.38%` | `6,565.50` |
| `Live` | `Short` | `0.9675` | 3,160.00 USD | 3,160.00 USD | 0.00 USD | `+4.07%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 68,220.00 USD | 65,060.00 USD | 0.00 USD | `+4.39%` | `67,040.50` |
| `Live` | `Short` | `0.9715` | 68,620.00 USD | 398.41 USD | 0.00 USD | `+4.50%` | `410.10` |
| `Live` | `Short` | `0.9755` | 68,740.00 USD | 121.55 USD | 0.00 USD | `+4.93%` | `124.60` |
| `Live` | `Short` | `0.9765` | 69,110.00 USD | 365.89 USD | 0.00 USD | `+5.04%` | `374.70` |
| `Live` | `Short` | `0.9775` | 69,210.00 USD | 100.88 USD | 0.00 USD | `+5.15%` | `103.20` |
| `Live` | `Short` | `0.9805` | 84,790.00 USD | 15,580.00 USD | 0.00 USD | `+5.47%` | `15,886.90` |
| `Live` | `Short` | `0.9845` | 95,230.00 USD | 10,440.00 USD | 0.00 USD | `+5.90%` | `10,608.60` |
| `Live` | `Short` | `0.9875` | 95,960.00 USD | 732.03 USD | 0.00 USD | `+6.22%` | `741.30` |
| `Live` | `Short` | `0.9885` | 100,890.00 USD | 4,930.00 USD | 0.00 USD | `+6.33%` | `4,982.50` |
| `Live` | `Short` | `0.9905` | 103,560.00 USD | 2,670.00 USD | 0.00 USD | `+6.55%` | `2,692.10` |
| `Live` | `Short` | `0.9925` | 105,970.00 USD | 2,420.00 USD | 0.00 USD | `+6.76%` | `2,434.50` |
| `Live` | `Short` | `0.9945` | 112,400.00 USD | 6,430.00 USD | 0.00 USD | `+6.98%` | `6,462.70` |
| `Live` | `Short` | `0.9965` | 114,830.00 USD | 2,430.00 USD | 0.00 USD | `+7.19%` | `2,435.90` |
| `Live` | `Short` | `1.00` | 115,060.00 USD | 235.86 USD | 0.00 USD | `+8.05%` | `234.80` |
| `Live` | `Short` | `1.02` | 115,230.00 USD | 170.40 USD | 0.00 USD | `+9.23%` | `167.80` |
| `Live` | `Short` | `1.02` | 124,210.00 USD | 8,980.00 USD | 0.00 USD | `+9.34%` | `8,832.40` |
| `Live` | `Short` | `1.03` | 124,360.00 USD | 152.91 USD | 0.00 USD | `+11.06%` | `148.10` |
| `Live` | `Short` | `1.04` | 124,470.00 USD | 109.46 USD | 0.00 USD | `+11.60%` | `105.50` |
| `Live` | `Short` | `1.04` | 134,880.00 USD | 10,400.00 USD | 0.00 USD | `+11.82%` | `10,007.60` |
| `Live` | `Short` | `1.04` | 135,010.00 USD | 139.22 USD | 0.00 USD | `+11.92%` | `133.80` |
| `Live` | `Short` | `1.05` | 135,610.00 USD | 597.52 USD | 0.00 USD | `+13.00%` | `568.80` |
| `Live` | `Short` | `1.05` | 138,000.00 USD | 2,390.00 USD | 0.00 USD | `+13.11%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 139,330.00 USD | 1,330.00 USD | 0.00 USD | `+13.21%` | `1,260.50` |
| `Live` | `Short` | `1.05` | 139,650.00 USD | 317.52 USD | 0.00 USD | `+13.32%` | `301.40` |
| `Live` | `Short` | `1.05` | 139,860.00 USD | 217.44 USD | 0.00 USD | `+13.43%` | `206.20` |
| `Live` | `Short` | `1.07` | 139,980.00 USD | 114.44 USD | 0.00 USD | `+15.04%` | `107.00` |
| `Live` | `Short` | `1.08` | 141,130.00 USD | 1,150.00 USD | 0.00 USD | `+15.90%` | `1,066.30` |
| `Live` | `Short` | `1.08` | 146,820.00 USD | 5,700.00 USD | 0.00 USD | `+16.12%` | `5,278.70` |
| `Live` | `Short` | `1.08` | 150,410.00 USD | 3,580.00 USD | 0.00 USD | `+16.23%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 153,540.00 USD | 3,130.00 USD | 0.00 USD | `+16.44%` | `2,889.30` |
| `Live` | `Short` | `1.08` | 153,700.00 USD | 166.43 USD | 0.00 USD | `+16.55%` | `153.60` |
| `Live` | `Short` | `1.09` | 159,250.00 USD | 5,550.00 USD | 0.00 USD | `+17.19%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 159,580.00 USD | 324.90 USD | 0.00 USD | `+18.27%` | `295.50` |
| `Live` | `Short` | `1.10` | 159,860.00 USD | 277.22 USD | 0.00 USD | `+18.38%` | `251.90` |
| `Live` | `Short` | `1.13` | 183,160.00 USD | 23,310.00 USD | 0.00 USD | `+21.17%` | `20,691.10` |
| `Live` | `Short` | `1.20` | 184,620.00 USD | 1,450.00 USD | 0.00 USD | `+28.81%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 184,870.00 USD | 253.69 USD | 0.00 USD | `+29.03%` | `211.50` |
| `Live` | `Short` | `1.20` | 214,630.00 USD | 29,760.00 USD | 0.00 USD | `+29.35%` | `24,749.90` |
| `Live` | `Short` | `1.21` | 214,780.00 USD | 147.43 USD | 0.00 USD | `+29.67%` | `122.30` |
| `Live` | `Short` | `1.22` | 219,220.00 USD | 4,440.00 USD | 0.00 USD | `+31.07%` | `3,646.70` |
| `Live` | `Short` | `1.23` | 224,470.00 USD | 5,250.00 USD | 0.00 USD | `+32.15%` | `4,273.60` |
| `Live` | `Short` | `1.23` | 233,840.00 USD | 9,370.00 USD | 0.00 USD | `+32.25%` | `7,618.00` |
| `Live` | `Short` | `1.23` | 234,220.00 USD | 380.84 USD | 0.00 USD | `+32.79%` | `308.50` |
| `Live` | `Short` | `1.26` | 234,360.00 USD | 137.21 USD | 0.00 USD | `+35.16%` | `109.20` |
| `Live` | `Short` | `1.26` | 448,360.00 USD | 214,000.00 USD | 0.00 USD | `+35.37%` | `170,042.00` |
| `Live` | `Short` | `1.26` | 451,020.00 USD | 2,670.00 USD | 0.00 USD | `+35.48%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 490,910.00 USD | 39,880.00 USD | 0.00 USD | `+37.96%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 493,020.00 USD | 2,110.00 USD | 0.00 USD | `+38.49%` | `1,639.00` |
| `Live` | `Short` | `1.29` | 493,240.00 USD | 226.80 USD | 0.00 USD | `+39.25%` | `175.20` |
| `Live` | `Short` | `1.30` | 493,360.00 USD | 114.40 USD | 0.00 USD | `+39.68%` | `88.10` |
| `Live` | `Short` | `1.31` | 494,380.00 USD | 1,020.00 USD | 0.00 USD | `+40.75%` | `777.20` |
| `Live` | `Short` | `1.31` | 525,910.00 USD | 31,530.00 USD | 0.00 USD | `+41.07%` | `24,042.40` |
| `Live` | `Short` | `1.33` | 532,240.00 USD | 6,340.00 USD | 0.00 USD | `+42.58%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 554,210.00 USD | 21,970.00 USD | 0.00 USD | `+42.90%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 554,570.00 USD | 358.30 USD | 0.00 USD | `+43.12%` | `269.30` |
| `Live` | `Short` | `1.33` | 556,090.00 USD | 1,520.00 USD | 0.00 USD | `+43.33%` | `1,143.40` |
| `Live` | `Short` | `1.34` | 562,950.00 USD | 6,860.00 USD | 0.00 USD | `+44.09%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 921,230.00 USD | 358,280.00 USD | 0.00 USD | `+47.64%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 925,680.00 USD | 4,450.00 USD | 0.00 USD | `+52.15%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 926,080.00 USD | 402.08 USD | 0.00 USD | `+54.52%` | `279.90` |
| `Live` | `Short` | `1.44` | 926,370.00 USD | 288.68 USD | 0.00 USD | `+54.95%` | `200.40` |
| `Live` | `Short` | `1.45` | 927,570.00 USD | 1,200.00 USD | 0.00 USD | `+56.03%` | `826.40` |
| `Live` | `Short` | `1.47` | 937,100.00 USD | 9,530.00 USD | 0.00 USD | `+57.96%` | `6,491.20` |
| `Live` | `Short` | `1.47` | 941,930.00 USD | 4,830.00 USD | 0.00 USD | `+58.39%` | `3,279.70` |
| `Live` | `Short` | `1.49` | 942,080.00 USD | 146.37 USD | 0.00 USD | `+60.33%` | `98.20` |
| `Live` | `Short` | `1.49` | 943,440.00 USD | 1,360.00 USD | 0.00 USD | `+60.54%` | `910.40` |
| `Live` | `Short` | `1.51` | 947,450.00 USD | 4,020.00 USD | 0.00 USD | `+62.91%` | `2,654.10` |
| `Live` | `Short` | `1.52` | 948,570.00 USD | 1,120.00 USD | 0.00 USD | `+63.02%` | `736.20` |
| `Live` | `Short` | `1.52` | 972,860.00 USD | 24,290.00 USD | 0.00 USD | `+63.88%` | `15,941.90` |
| `Live` | `Short` | `1.54` | 973,000.00 USD | 144.34 USD | 0.00 USD | `+65.17%` | `94.00` |
| `Live` | `Short` | `1.57` | 990,550.00 USD | 17,550.00 USD | 0.00 USD | `+68.83%` | `11,182.60` |
| `Live` | `Short` | `1.58` | 990,840.00 USD | 285.39 USD | 0.00 USD | `+69.80%` | `180.80` |
| `Live` | `Short` | `1.59` | 3,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | `+71.52%` | `1,664,573.50` |
| `Live` | `Short` | `1.61` | 3,650,000.00 USD | 122.73 USD | 0.00 USD | `+73.02%` | `76.30` |
| `Live` | `Short` | `1.62` | 3,650,000.00 USD | 9,720.00 USD | 0.00 USD | `+74.21%` | `6,000.00` |
| `Live` | `Short` | `1.65` | 3,680,000.00 USD | 21,330.00 USD | 0.00 USD | `+77.11%` | `12,957.30` |
| `Live` | `Short` | `1.67` | 3,720,000.00 USD | 39,240.00 USD | 0.00 USD | `+79.37%` | `23,529.40` |
| `Live` | `Short` | `1.67` | 3,720,000.00 USD | 9,450.00 USD | 0.00 USD | `+80.01%` | `5,645.40` |
| `Live` | `Short` | `1.71` | 3,730,000.00 USD | 205.67 USD | 0.00 USD | `+84.21%` | `120.10` |
| `Live` | `Short` | `1.71` | 4,020,000.00 USD | 296,610.00 USD | 0.00 USD | `+84.42%` | `173,000.00` |
| `Live` | `Short` | `1.73` | 4,110,000.00 USD | 85,590.00 USD | 0.00 USD | `+85.82%` | `49,543.90` |
| `Live` | `Short` | `1.73` | 4,110,000.00 USD | 226.05 USD | 0.00 USD | `+86.47%` | `130.40` |
| `Live` | `Short` | `1.74` | 4,110,000.00 USD | 2,080.00 USD | 0.00 USD | `+87.22%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 4,130,000.00 USD | 19,920.00 USD | 0.00 USD | `+88.40%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 4,140,000.00 USD | 11,350.00 USD | 0.00 USD | `+88.51%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 4,140,000.00 USD | 1,520.00 USD | 0.00 USD | `+88.73%` | `868.90` |
| `Live` | `Short` | `1.76` | 4,140,000.00 USD | 148.68 USD | 0.00 USD | `+89.26%` | `84.50` |
| `Live` | `Short` | `1.76` | 4,140,000.00 USD | 2,400.00 USD | 0.00 USD | `+89.80%` | `1,360.10` |
| `Live` | `Short` | `1.79` | 4,150,000.00 USD | 781.77 USD | 0.00 USD | `+92.17%` | `437.60` |
| `Live` | `Short` | `1.79` | 4,150,000.00 USD | 952.52 USD | 0.00 USD | `+93.03%` | `530.80` |
| `Live` | `Short` | `1.83` | 4,160,000.00 USD | 14,230.00 USD | 0.00 USD | `+96.47%` | `7,789.30` |
| `Live` | `Short` | `1.83` | 4,160,000.00 USD | 203.88 USD | 0.00 USD | `+96.69%` | `111.50` |
| `Live` | `Short` | `1.85` | 4,160,000.00 USD | 943.75 USD | 0.00 USD | `+99.05%` | `510.00` |
| `Live` | `Short` | `1.85` | 4,160,000.00 USD | 190.35 USD | 0.00 USD | `+99.38%` | `102.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2745` | 2,230,000.00 USD | 0.00 USD | 455.97 USD | `-70.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 2,230,000.00 USD | 0.00 USD | 102.75 USD | `-63.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 2,230,000.00 USD | 0.00 USD | 256.78 USD | `-62.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 2,230,000.00 USD | 0.00 USD | 428.87 USD | `-58.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 2,220,000.00 USD | 0.00 USD | 123.45 USD | `-55.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 2,220,000.00 USD | 0.00 USD | 818.15 USD | `-54.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 2,220,000.00 USD | 0.00 USD | 454.04 USD | `-53.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 2,220,000.00 USD | 0.00 USD | 436.41 USD | `-53.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 2,220,000.00 USD | 0.00 USD | 876.79 USD | `-53.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 2,220,000.00 USD | 0.00 USD | 466.72 USD | `-51.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 2,220,000.00 USD | 0.00 USD | 142.95 USD | `-48.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 2,220,000.00 USD | 0.00 USD | 5,650.00 USD | `-46.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 2,220,000.00 USD | 0.00 USD | 151.74 USD | `-44.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 2,220,000.00 USD | 0.00 USD | 123.91 USD | `-44.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 2,220,000.00 USD | 0.00 USD | 219.80 USD | `-40.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 2,220,000.00 USD | 0.00 USD | 237,400.00 USD | `-40.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 1,980,000.00 USD | 0.00 USD | 276.75 USD | `-40.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 1,980,000.00 USD | 0.00 USD | 2,010.00 USD | `-39.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 1,980,000.00 USD | 0.00 USD | 119.76 USD | `-37.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 1,980,000.00 USD | 0.00 USD | 108.39 USD | `-35.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 1,980,000.00 USD | 0.00 USD | 123.28 USD | `-34.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 1,980,000.00 USD | 0.00 USD | 488.52 USD | `-33.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 1,970,000.00 USD | 0.00 USD | 5,940.00 USD | `-32.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 1,970,000.00 USD | 0.00 USD | 242.24 USD | `-32.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 1,970,000.00 USD | 0.00 USD | 193.95 USD | `-30.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 1,970,000.00 USD | 0.00 USD | 647.50 USD | `-30.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 1,970,000.00 USD | 0.00 USD | 834.79 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 1,970,000.00 USD | 0.00 USD | 158.54 USD | `-29.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 1,970,000.00 USD | 0.00 USD | 195.47 USD | `-29.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 1,970,000.00 USD | 0.00 USD | 190.25 USD | `-28.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 1,970,000.00 USD | 0.00 USD | 52,450.00 USD | `-27.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 1,910,000.00 USD | 0.00 USD | 536.11 USD | `-27.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 1,910,000.00 USD | 0.00 USD | 5,490.00 USD | `-26.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 1,910,000.00 USD | 0.00 USD | 340.75 USD | `-26.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 1,910,000.00 USD | 0.00 USD | 9,270.00 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 1,900,000.00 USD | 0.00 USD | 120.53 USD | `-25.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 1,900,000.00 USD | 0.00 USD | 160.71 USD | `-25.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 1,900,000.00 USD | 0.00 USD | 187.61 USD | `-24.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 1,900,000.00 USD | 0.00 USD | 2,920.00 USD | `-24.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 1,890,000.00 USD | 0.00 USD | 89,150.00 USD | `-24.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 1,810,000.00 USD | 0.00 USD | 189.06 USD | `-24.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 1,810,000.00 USD | 0.00 USD | 5,650.00 USD | `-23.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 1,800,000.00 USD | 0.00 USD | 100.47 USD | `-23.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 1,800,000.00 USD | 0.00 USD | 152.05 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 1,800,000.00 USD | 0.00 USD | 123.41 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 1,800,000.00 USD | 0.00 USD | 1,130.00 USD | `-21.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 1,800,000.00 USD | 0.00 USD | 18,770.00 USD | `-21.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 1,780,000.00 USD | 0.00 USD | 257.26 USD | `-20.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 1,780,000.00 USD | 0.00 USD | 10,160.00 USD | `-19.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 1,770,000.00 USD | 0.00 USD | 93,810.00 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 1,680,000.00 USD | 0.00 USD | 1,230.00 USD | `-18.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 1,670,000.00 USD | 0.00 USD | 924.99 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 1,670,000.00 USD | 0.00 USD | 804.61 USD | `-18.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 1,670,000.00 USD | 0.00 USD | 191.12 USD | `-17.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 1,670,000.00 USD | 0.00 USD | 1,370.00 USD | `-17.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 1,670,000.00 USD | 0.00 USD | 125.92 USD | `-16.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 1,670,000.00 USD | 0.00 USD | 1,150.00 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 1,670,000.00 USD | 0.00 USD | 200.39 USD | `-16.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 1,670,000.00 USD | 0.00 USD | 1,860.00 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 1,670,000.00 USD | 0.00 USD | 128.47 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 1,670,000.00 USD | 0.00 USD | 3,130.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 1,660,000.00 USD | 0.00 USD | 135.11 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 1,660,000.00 USD | 0.00 USD | 1,500.00 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 1,660,000.00 USD | 0.00 USD | 25,170.00 USD | `-14.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 1,640,000.00 USD | 0.00 USD | 103.42 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 1,640,000.00 USD | 0.00 USD | 1,260.00 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 1,640,000.00 USD | 0.00 USD | 7,670.00 USD | `-13.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 1,630,000.00 USD | 0.00 USD | 144.67 USD | `-13.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 1,630,000.00 USD | 0.00 USD | 50,540.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 1,580,000.00 USD | 0.00 USD | 263.25 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 1,580,000.00 USD | 0.00 USD | 16,870.00 USD | `-13.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 1,560,000.00 USD | 0.00 USD | 91,080.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 1,470,000.00 USD | 0.00 USD | 174.63 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 1,470,000.00 USD | 0.00 USD | 125.72 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 1,470,000.00 USD | 0.00 USD | 4,860.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 1,460,000.00 USD | 0.00 USD | 11,040.00 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 1,450,000.00 USD | 0.00 USD | 922.29 USD | `-11.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 1,450,000.00 USD | 0.00 USD | 1,120.00 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 1,450,000.00 USD | 0.00 USD | 124.43 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 1,450,000.00 USD | 0.00 USD | 4,380.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 1,450,000.00 USD | 0.00 USD | 171.46 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 1,450,000.00 USD | 0.00 USD | 1,270.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 1,450,000.00 USD | 0.00 USD | 4,170.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 1,440,000.00 USD | 0.00 USD | 610.23 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 1,440,000.00 USD | 0.00 USD | 699.65 USD | `-9.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 1,440,000.00 USD | 0.00 USD | 320.31 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 1,440,000.00 USD | 0.00 USD | 1,010.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 1,440,000.00 USD | 0.00 USD | 221.25 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 1,440,000.00 USD | 0.00 USD | 212.81 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 1,440,000.00 USD | 0.00 USD | 462.49 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 1,440,000.00 USD | 0.00 USD | 481.80 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 1,440,000.00 USD | 0.00 USD | 13,120.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 1,420,000.00 USD | 0.00 USD | 901.40 USD | `-8.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 1,420,000.00 USD | 0.00 USD | 242.93 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 1,420,000.00 USD | 0.00 USD | 6,200.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 1,420,000.00 USD | 0.00 USD | 108.13 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 1,420,000.00 USD | 0.00 USD | 1,640.00 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 1,420,000.00 USD | 0.00 USD | 8,740.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 1,410,000.00 USD | 0.00 USD | 202.45 USD | `-7.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 1,410,000.00 USD | 0.00 USD | 921.70 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 1,410,000.00 USD | 0.00 USD | 161.49 USD | `-7.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 1,410,000.00 USD | 0.00 USD | 1,270.00 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 1,400,000.00 USD | 0.00 USD | 741.45 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 1,400,000.00 USD | 0.00 USD | 168.75 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 1,400,000.00 USD | 0.00 USD | 2,990.00 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 1,400,000.00 USD | 0.00 USD | 3,630.00 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 1,400,000.00 USD | 0.00 USD | 712.45 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 1,400,000.00 USD | 0.00 USD | 58,490.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 1,340,000.00 USD | 0.00 USD | 281.70 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 1,340,000.00 USD | 0.00 USD | 133.10 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 1,340,000.00 USD | 0.00 USD | 246.98 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 1,340,000.00 USD | 0.00 USD | 9,070.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 1,330,000.00 USD | 0.00 USD | 151.10 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 1,330,000.00 USD | 0.00 USD | 507.74 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 1,330,000.00 USD | 0.00 USD | 8,370.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 1,320,000.00 USD | 0.00 USD | 157,870.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 1,160,000.00 USD | 0.00 USD | 5,020.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 1,160,000.00 USD | 0.00 USD | 9,770.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8855` | 1,150,000.00 USD | 0.00 USD | 3,660.00 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 1,140,000.00 USD | 0.00 USD | 13,450.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 1,130,000.00 USD | 0.00 USD | 3,620.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8885` | 1,120,000.00 USD | 0.00 USD | 11,360.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 1,110,000.00 USD | 0.00 USD | 8,780.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8905` | 1,100,000.00 USD | 0.00 USD | 10,340.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 1,090,000.00 USD | 0.00 USD | 469.91 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 1,090,000.00 USD | 0.00 USD | 10,610.00 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 1,080,000.00 USD | 0.00 USD | 7,100.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8945` | 1,080,000.00 USD | 0.00 USD | 2,920.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8955` | 1,070,000.00 USD | 0.00 USD | 3,900.00 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 1,070,000.00 USD | 0.00 USD | 7,930.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8975` | 1,060,000.00 USD | 0.00 USD | 18,210.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 1,040,000.00 USD | 0.00 USD | 2,710.00 USD | `-3.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8995` | 1,040,000.00 USD | 0.00 USD | 28,960.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 1,010,000.00 USD | 0.00 USD | 3,860.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9015` | 1,010,000.00 USD | 0.00 USD | 1,230.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 1,010,000.00 USD | 0.00 USD | 926.06 USD | `-2.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 1,010,000.00 USD | 0.00 USD | 805.29 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 1,000,000.00 USD | 0.00 USD | 1,140.00 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9055` | 1,000,000.00 USD | 0.00 USD | 1,990.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 1,000,000.00 USD | 0.00 USD | 22,450.00 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 979,160.00 USD | 0.00 USD | 250.83 USD | `-2.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 978,910.00 USD | 0.00 USD | 1,440.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 977,470.00 USD | 0.00 USD | 1,520.00 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9105` | 975,950.00 USD | 0.00 USD | 637.90 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 975,310.00 USD | 0.00 USD | 2,210.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9125` | 973,100.00 USD | 0.00 USD | 14,760.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 958,340.00 USD | 0.00 USD | 3,020.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 955,310.00 USD | 0.00 USD | 318.79 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 955,000.00 USD | 0.00 USD | 5,070.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 949,930.00 USD | 0.00 USD | 5,040.00 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 944,890.00 USD | 0.00 USD | 3,210.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 941,680.00 USD | 0.00 USD | 1,970.00 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 939,710.00 USD | 0.00 USD | 116.59 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 939,590.00 USD | 0.00 USD | 259,120.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 680,470.00 USD | 0.00 USD | 151,960.00 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 528,510.00 USD | 0.00 USD | 5,070.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 523,440.00 USD | 0.00 USD | 126,350.00 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 397,090.00 USD | 0.00 USD | 1,400.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 395,690.00 USD | 0.00 USD | 235,060.00 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 160,630.00 USD | 0.00 USD | 160,180.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 444.61 USD | 0.00 USD | 146.27 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 298.35 USD | 0.00 USD | 195.17 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 103.17 USD | 0.00 USD | 103.17 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 186.29 USD | 186.29 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 335.14 USD | 148.85 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 436.04 USD | 100.90 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 1,420.00 USD | 979.71 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 4,120.00 USD | 2,700.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 8,000.00 USD | 3,880.00 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 17,510.00 USD | 9,510.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 19,380.00 USD | 1,880.00 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 72,440.00 USD | 53,060.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 76,350.00 USD | 3,910.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 85,310.00 USD | 8,960.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 85,470.00 USD | 158.55 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 87,360.00 USD | 1,890.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 87,480.00 USD | 121.15 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 88,270.00 USD | 789.04 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 88,380.00 USD | 117.81 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 89,440.00 USD | 1,050.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 95,440.00 USD | 6,000.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 95,700.00 USD | 261.97 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 95,970.00 USD | 265.66 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 96,970.00 USD | 999.27 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 106,880.00 USD | 9,910.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 110,020.00 USD | 3,150.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 111,460.00 USD | 1,440.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 114,350.00 USD | 2,890.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 121,950.00 USD | 7,600.00 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 122,070.00 USD | 121.54 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 122,170.00 USD | 100.17 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 122,420.00 USD | 245.02 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 122,580.00 USD | 161.82 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 122,780.00 USD | 197.79 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 123,680.00 USD | 900.10 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 125,010.00 USD | 1,340.00 USD | 0.00 USD | `+3.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 125,220.00 USD | 204.20 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 125,860.00 USD | 643.88 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 129,020.00 USD | 3,160.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 130,020.00 USD | 993.78 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 131,410.00 USD | 1,400.00 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 143,090.00 USD | 11,680.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 143,300.00 USD | 210.33 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 144,430.00 USD | 1,130.00 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 155,060.00 USD | 10,640.00 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 155,320.00 USD | 253.14 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 155,560.00 USD | 244.81 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 155,850.00 USD | 285.72 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 156,050.00 USD | 201.77 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 156,640.00 USD | 592.60 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 193,100.00 USD | 36,450.00 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 198,570.00 USD | 5,470.00 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 199,120.00 USD | 558.35 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 200,190.00 USD | 1,060.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 201,420.00 USD | 1,240.00 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 201,910.00 USD | 490.99 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 202,680.00 USD | 769.72 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 203,680.00 USD | 991.50 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 214,010.00 USD | 10,340.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 214,300.00 USD | 284.92 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 214,570.00 USD | 277.64 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 214,920.00 USD | 350.37 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 215,070.00 USD | 144.04 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 215,170.00 USD | 105.44 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 223,940.00 USD | 8,760.00 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 225,510.00 USD | 1,570.00 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 227,690.00 USD | 2,180.00 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 228,050.00 USD | 363.87 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 228,640.00 USD | 589.52 USD | 0.00 USD | `+8.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 229,300.00 USD | 660.52 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 239,390.00 USD | 10,090.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 244,810.00 USD | 5,420.00 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 247,580.00 USD | 2,770.00 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 247,830.00 USD | 248.49 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 281,280.00 USD | 33,450.00 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 282,010.00 USD | 722.63 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 282,320.00 USD | 312.07 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 282,490.00 USD | 171.24 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 283,050.00 USD | 561.11 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 283,300.00 USD | 249.30 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 285,510.00 USD | 2,210.00 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 285,950.00 USD | 432.18 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 286,080.00 USD | 137.88 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 290,250.00 USD | 4,170.00 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 290,410.00 USD | 160.60 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 296,970.00 USD | 6,560.00 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 299,880.00 USD | 2,920.00 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 307,560.00 USD | 7,680.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 307,790.00 USD | 224.56 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 311,360.00 USD | 3,570.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 318,810.00 USD | 7,450.00 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,080,000.00 USD | 1,760,000.00 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,080,000.00 USD | 1,810.00 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,080,000.00 USD | 248.20 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,080,000.00 USD | 5,390.00 USD | 0.00 USD | `+13.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,080,000.00 USD | 285.32 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,090,000.00 USD | 2,570.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,090,000.00 USD | 1,240.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,090,000.00 USD | 278.06 USD | 0.00 USD | `+14.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,090,000.00 USD | 309.00 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,090,000.00 USD | 272.12 USD | 0.00 USD | `+15.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,090,000.00 USD | 117.12 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,230,000.00 USD | 140,120.00 USD | 0.00 USD | `+15.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,230,000.00 USD | 530.01 USD | 0.00 USD | `+15.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,230,000.00 USD | 128.23 USD | 0.00 USD | `+16.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,340,000.00 USD | 108,190.00 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,340,000.00 USD | 550.49 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,340,000.00 USD | 5,810.00 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,350,000.00 USD | 5,570.00 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,350,000.00 USD | 1,290.00 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,350,000.00 USD | 294.81 USD | 0.00 USD | `+17.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,350,000.00 USD | 123.13 USD | 0.00 USD | `+17.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,350,000.00 USD | 494.98 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,350,000.00 USD | 613.52 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,480,000.00 USD | 124,320.00 USD | 0.00 USD | `+18.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,480,000.00 USD | 409.76 USD | 0.00 USD | `+18.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,480,000.00 USD | 162.77 USD | 0.00 USD | `+18.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,480,000.00 USD | 959.70 USD | 0.00 USD | `+18.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,480,000.00 USD | 160.18 USD | 0.00 USD | `+19.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,480,000.00 USD | 433.10 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,480,000.00 USD | 293.61 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,590,000.00 USD | 112,050.00 USD | 0.00 USD | `+20.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,590,000.00 USD | 462.47 USD | 0.00 USD | `+21.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,590,000.00 USD | 2,180.00 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,590,000.00 USD | 273.34 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,590,000.00 USD | 260.81 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,610,000.00 USD | 20,740.00 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,620,000.00 USD | 1,430.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,620,000.00 USD | 338.50 USD | 0.00 USD | `+23.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,620,000.00 USD | 769.57 USD | 0.00 USD | `+23.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,620,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,620,000.00 USD | 2,450.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,620,000.00 USD | 1,250.00 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,620,000.00 USD | 143.67 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,620,000.00 USD | 1,700.00 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,690,000.00 USD | 63,070.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,690,000.00 USD | 304.33 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,690,000.00 USD | 241.65 USD | 0.00 USD | `+26.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,690,000.00 USD | 239.97 USD | 0.00 USD | `+26.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,690,000.00 USD | 2,470.00 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,690,000.00 USD | 3,060.00 USD | 0.00 USD | `+26.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,690,000.00 USD | 351.02 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,000,000.00 USD | 310,250.00 USD | 0.00 USD | `+27.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,000,000.00 USD | 309.53 USD | 0.00 USD | `+28.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,000,000.00 USD | 159.09 USD | 0.00 USD | `+28.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,000,000.00 USD | 146.21 USD | 0.00 USD | `+28.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,080,000.00 USD | 79,820.00 USD | 0.00 USD | `+29.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,090,000.00 USD | 933.81 USD | 0.00 USD | `+29.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,090,000.00 USD | 658.86 USD | 0.00 USD | `+29.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,300,000.00 USD | 213,390.00 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,300,000.00 USD | 211.10 USD | 0.00 USD | `+30.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,300,000.00 USD | 1,050.00 USD | 0.00 USD | `+30.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,300,000.00 USD | 812.24 USD | 0.00 USD | `+31.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,300,000.00 USD | 509.71 USD | 0.00 USD | `+31.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,300,000.00 USD | 162.15 USD | 0.00 USD | `+32.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,300,000.00 USD | 187.04 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,300,000.00 USD | 542.12 USD | 0.00 USD | `+32.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,330,000.00 USD | 23,740.00 USD | 0.00 USD | `+32.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,330,000.00 USD | 2,010.00 USD | 0.00 USD | `+32.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,330,000.00 USD | 345.91 USD | 0.00 USD | `+33.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,330,000.00 USD | 104.79 USD | 0.00 USD | `+34.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,340,000.00 USD | 9,540.00 USD | 0.00 USD | `+34.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,340,000.00 USD | 265.62 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,340,000.00 USD | 1,480.00 USD | 0.00 USD | `+35.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,340,000.00 USD | 1,010.00 USD | 0.00 USD | `+35.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,340,000.00 USD | 340.38 USD | 0.00 USD | `+36.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,340,000.00 USD | 903.22 USD | 0.00 USD | `+36.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,340,000.00 USD | 424.15 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,380,000.00 USD | 41,160.00 USD | 0.00 USD | `+37.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,400,000.00 USD | 12,840.00 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,410,000.00 USD | 12,890.00 USD | 0.00 USD | `+38.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,420,000.00 USD | 8,820.00 USD | 0.00 USD | `+38.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,420,000.00 USD | 466.95 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,420,000.00 USD | 613.59 USD | 0.00 USD | `+39.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,420,000.00 USD | 1,420.00 USD | 0.00 USD | `+39.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,430,000.00 USD | 13,000.00 USD | 0.00 USD | `+39.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,430,000.00 USD | 284.42 USD | 0.00 USD | `+39.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,460,000.00 USD | 22,710.00 USD | 0.00 USD | `+42.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,460,000.00 USD | 640.82 USD | 0.00 USD | `+43.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,470,000.00 USD | 13,400.00 USD | 0.00 USD | `+44.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,470,000.00 USD | 1,580.00 USD | 0.00 USD | `+44.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,490,000.00 USD | 13,490.00 USD | 0.00 USD | `+45.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,500,000.00 USD | 11,580.00 USD | 0.00 USD | `+45.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,500,000.00 USD | 3,610.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,500,000.00 USD | 1,540.00 USD | 0.00 USD | `+46.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,500,000.00 USD | 1,500.00 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,520,000.00 USD | 15,000.00 USD | 0.00 USD | `+46.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,530,000.00 USD | 9,030.00 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,530,000.00 USD | 569.84 USD | 0.00 USD | `+49.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,540,000.00 USD | 13,890.00 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,550,000.00 USD | 2,710.00 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,560,000.00 USD | 15,500.00 USD | 0.00 USD | `+50.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,570,000.00 USD | 13,100.00 USD | 0.00 USD | `+50.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,610,000.00 USD | 32,860.00 USD | 0.00 USD | `+51.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,610,000.00 USD | 7,090.00 USD | 0.00 USD | `+51.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,610,000.00 USD | 106.64 USD | 0.00 USD | `+51.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,620,000.00 USD | 1,430.00 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,620,000.00 USD | 2,810.00 USD | 0.00 USD | `+52.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,630,000.00 USD | 8,420.00 USD | 0.00 USD | `+52.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 3,630,000.00 USD | 1,410.00 USD | 0.00 USD | `+53.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,630,000.00 USD | 431.38 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,630,000.00 USD | 1,390.00 USD | 0.00 USD | `+54.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,640,000.00 USD | 14,390.00 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,650,000.00 USD | 7,000.00 USD | 0.00 USD | `+55.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,650,000.00 USD | 434.98 USD | 0.00 USD | `+55.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,670,000.00 USD | 14,490.00 USD | 0.00 USD | `+55.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,670,000.00 USD | 1,370.00 USD | 0.00 USD | `+56.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 3,670,000.00 USD | 1,350.00 USD | 0.00 USD | `+57.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,670,000.00 USD | 1,340.00 USD | 0.00 USD | `+57.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,670,000.00 USD | 1,300.00 USD | 0.00 USD | `+58.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,670,000.00 USD | 342.08 USD | 0.00 USD | `+58.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 3,670,000.00 USD | 1,330.00 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,670,000.00 USD | 1,320.00 USD | 0.00 USD | `+60.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,680,000.00 USD | 1,310.00 USD | 0.00 USD | `+60.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,690,000.00 USD | 14,890.00 USD | 0.00 USD | `+60.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,700,000.00 USD | 9,580.00 USD | 0.00 USD | `+60.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,720,000.00 USD | 14,980.00 USD | 0.00 USD | `+61.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,720,000.00 USD | 5,110.00 USD | 0.00 USD | `+61.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,720,000.00 USD | 1,270.00 USD | 0.00 USD | `+63.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,720,000.00 USD | 1,260.00 USD | 0.00 USD | `+63.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 3,730,000.00 USD | 1,980.00 USD | 0.00 USD | `+65.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 3,730,000.00 USD | 574.53 USD | 0.00 USD | `+71.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 3,730,000.00 USD | 391.32 USD | 0.00 USD | `+72.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 3,730,000.00 USD | 1,160.00 USD | 0.00 USD | `+74.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,730,000.00 USD | 1,140.00 USD | 0.00 USD | `+76.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,730,000.00 USD | 1,970.00 USD | 0.00 USD | `+76.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 3,730,000.00 USD | 281.45 USD | 0.00 USD | `+78.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 3,730,000.00 USD | 958.84 USD | 0.00 USD | `+81.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 3,740,000.00 USD | 3,550.00 USD | 0.00 USD | `+82.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 3,740,000.00 USD | 1,070.00 USD | 0.00 USD | `+87.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 3,740,000.00 USD | 1,710.00 USD | 0.00 USD | `+90.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,750,000.00 USD | 13,670.00 USD | 0.00 USD | `+93.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,750,000.00 USD | 295.46 USD | 0.00 USD | `+93.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 3,750,000.00 USD | 1,030.00 USD | 0.00 USD | `+94.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,750,000.00 USD | 328.97 USD | 0.00 USD | `+95.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,750,000.00 USD | 394.87 USD | 0.00 USD | `+95.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,750,000.00 USD | 1,010.00 USD | 0.00 USD | `+98.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,770,000.00 USD | 10,950.00 USD | 0.00 USD | `+98.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,810,000.00 USD | 41,990.00 USD | 0.00 USD | `+99.05%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8160` | 30,270,000.00 USD | 0.00 USD | 30,270,000.00 USD | 210,530.00 USD | 64,440.00 USD | 167,460.00 USD |
| `1D` | `0.8180` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 78,400.00 USD | 26,400.00 USD | 71,970.00 USD |
| `7D` | `0.8180` | 29,830,000.00 USD | 0.00 USD | 29,830,000.00 USD | 77,750.00 USD | 39,880.00 USD | 42,650.00 USD |
| `1D` | `0.8200` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 13,230.00 USD | 16,660.00 USD | 26,450.00 USD |
| `7D` | `0.8200` | 29,670,000.00 USD | 0.00 USD | 29,670,000.00 USD | 205,920.00 USD | 47,330.00 USD | 97,140.00 USD |
| `1D` | `0.8220` | 10,870,000.00 USD | 0.00 USD | 10,870,000.00 USD | 12,100.00 USD | 18,530.00 USD | 30,110.00 USD |
| `7D` | `0.8220` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 104,090.00 USD | 39,210.00 USD | 93,690.00 USD |
| `1D` | `0.8240` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 21,120.00 USD | 16,100.00 USD | 20,080.00 USD |
| `7D` | `0.8240` | 29,080,000.00 USD | 0.00 USD | 29,080,000.00 USD | 97,060.00 USD | 36,240.00 USD | 86,870.00 USD |
| `1D` | `0.8260` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 13,860.00 USD | 3,800.00 USD | 14,020.00 USD |
| `7D` | `0.8260` | 28,860,000.00 USD | 0.00 USD | 28,860,000.00 USD | 185,230.00 USD | 28,970.00 USD | 108,640.00 USD |
| `1D` | `0.8280` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 19,690.00 USD | 12,830.00 USD | 33,850.00 USD |
| `7D` | `0.8280` | 28,540,000.00 USD | 0.00 USD | 28,540,000.00 USD | 113,570.00 USD | 44,400.00 USD | 87,770.00 USD |
| `1D` | `0.8300` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 11,010.00 USD | 9,200.00 USD | 25,690.00 USD |
| `7D` | `0.8300` | 28,290,000.00 USD | 0.00 USD | 28,290,000.00 USD | 30,930.00 USD | 41,810.00 USD | 44,360.00 USD |
| `1D` | `0.8320` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 19,130.00 USD | 10,200.00 USD | 6,610.00 USD |
| `7D` | `0.8320` | 28,170,000.00 USD | 0.00 USD | 28,170,000.00 USD | 90,830.00 USD | 57,170.00 USD | 60,670.00 USD |
| `1D` | `0.8340` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 49,780.00 USD | 16,200.00 USD | 43,970.00 USD |
| `7D` | `0.8340` | 27,970,000.00 USD | 0.00 USD | 27,970,000.00 USD | 105,040.00 USD | 53,420.00 USD | 180,540.00 USD |
| `1D` | `0.8360` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 48,150.00 USD | 11,860.00 USD | 20,660.00 USD |
| `7D` | `0.8360` | 27,630,000.00 USD | 0.00 USD | 27,630,000.00 USD | 138,260.00 USD | 28,750.00 USD | 94,660.00 USD |
| `1D` | `0.8380` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD |
| `7D` | `0.8380` | 27,370,000.00 USD | 0.00 USD | 27,370,000.00 USD | 69,590.00 USD | 59,380.00 USD | 95,430.00 USD |
| `1D` | `0.8400` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 19,020.00 USD | 19,340.00 USD | 33,570.00 USD |
| `7D` | `0.8400` | 27,140,000.00 USD | 0.00 USD | 27,140,000.00 USD | 76,470.00 USD | 55,720.00 USD | 58,740.00 USD |
| `1D` | `0.8420` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 11,140.00 USD | 15,160.00 USD | 22,140.00 USD |
| `7D` | `0.8420` | 26,950,000.00 USD | 0.00 USD | 26,950,000.00 USD | 70,700.00 USD | 48,060.00 USD | 11,430.00 USD |
| `1D` | `0.8440` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 21,450.00 USD | 11,360.00 USD | 81.17 USD |
| `7D` | `0.8440` | 26,820,000.00 USD | 0.00 USD | 26,820,000.00 USD | 34,250.00 USD | 40,470.00 USD | 28,820.00 USD |
| `1D` | `0.8460` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 3,270.00 USD | 9,410.00 USD | 25,070.00 USD |
| `7D` | `0.8460` | 26,720,000.00 USD | 0.00 USD | 26,720,000.00 USD | 31,090.00 USD | 33,020.00 USD | 72,030.00 USD |
| `1D` | `0.8480` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 24,190.00 USD | 20,130.00 USD | 44,480.00 USD |
| `7D` | `0.8480` | 26,580,000.00 USD | 0.00 USD | 26,580,000.00 USD | 52,580.00 USD | 6,260.00 USD | 34,190.00 USD |
| `1D` | `0.8500` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 47,850.00 USD | 7,390.00 USD | 15,030.00 USD |
| `7D` | `0.8500` | 26,490,000.00 USD | 0.00 USD | 26,490,000.00 USD | 32,630.00 USD | 15,300.00 USD | 23,180.00 USD |
| `1D` | `0.8520` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 21,900.00 USD | 27,950.00 USD | 11,040.00 USD |
| `7D` | `0.8520` | 26,420,000.00 USD | 0.00 USD | 26,420,000.00 USD | 77,320.00 USD | 45,980.00 USD | 46,030.00 USD |
| `1D` | `0.8540` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 14,330.00 USD | 2,800.00 USD | 24,610.00 USD |
| `7D` | `0.8540` | 26,250,000.00 USD | 0.00 USD | 26,250,000.00 USD | 92,380.00 USD | 64,630.00 USD | 15,520.00 USD |
| `1D` | `0.8560` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 28,740.00 USD | 23,100.00 USD | 17,510.00 USD |
| `7D` | `0.8560` | 26,070,000.00 USD | 0.00 USD | 26,070,000.00 USD | 87,380.00 USD | 45,770.00 USD | 6,930.00 USD |
| `1D` | `0.8580` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 13,710.00 USD | 13,380.00 USD | 14,690.00 USD |
| `7D` | `0.8580` | 25,930,000.00 USD | 0.00 USD | 25,930,000.00 USD | 65,360.00 USD | 21,960.00 USD | 19,570.00 USD |
| `1D` | `0.8600` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 4,180.00 USD | 6,810.00 USD | 15,080.00 USD |
| `7D` | `0.8600` | 25,830,000.00 USD | 0.00 USD | 25,830,000.00 USD | 38,890.00 USD | 65,420.00 USD | 23,940.00 USD |
| `1D` | `0.8620` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 5,810.00 USD | 4,970.00 USD | 396.37 USD |
| `7D` | `0.8620` | 25,700,000.00 USD | 0.00 USD | 25,700,000.00 USD | 25,100.00 USD | 21,240.00 USD | 54,850.00 USD |
| `1D` | `0.8640` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 40,460.00 USD | 21,260.00 USD | 60,870.00 USD |
| `7D` | `0.8640` | 25,600,000.00 USD | 0.00 USD | 25,600,000.00 USD | 38,670.00 USD | 27,710.00 USD | 3,090.00 USD |
| `1D` | `0.8660` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 138,180.00 USD | 2,480.00 USD | 13,560.00 USD |
| `7D` | `0.8660` | 25,530,000.00 USD | 0.00 USD | 25,530,000.00 USD | 261,430.00 USD | 35,900.00 USD | 117,940.00 USD |
| `1D` | `0.8680` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 103,400.00 USD | 61,870.00 USD | 33,690.00 USD |
| `7D` | `0.8680` | 25,110,000.00 USD | 0.00 USD | 25,110,000.00 USD | 208,910.00 USD | 100,620.00 USD | 113,000.00 USD |
| `1D` | `0.8700` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 109,900.00 USD | 92,460.00 USD | 227,330.00 USD |
| `7D` | `0.8700` | 24,690,000.00 USD | 0.00 USD | 24,690,000.00 USD | 377,870.00 USD | 141,350.00 USD | 324,980.00 USD |
| `1D` | `0.8720` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 211,680.00 USD | 63,650.00 USD | 201,370.00 USD |
| `7D` | `0.8720` | 23,850,000.00 USD | 0.00 USD | 23,850,000.00 USD | 440,480.00 USD | 149,650.00 USD | 311,410.00 USD |
| `1D` | `0.8740` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 43,030.00 USD | 19,920.00 USD | 21,550.00 USD |
| `7D` | `0.8740` | 22,940,000.00 USD | 0.00 USD | 22,940,000.00 USD | 566,110.00 USD | 236,710.00 USD | 199,810.00 USD |
| `1D` | `0.8760` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 89,270.00 USD | 97,710.00 USD | 179,030.00 USD |
| `7D` | `0.8760` | 21,940,000.00 USD | 0.00 USD | 21,940,000.00 USD | 594,350.00 USD | 249,690.00 USD | 486,640.00 USD |
| `1D` | `0.8780` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 63,800.00 USD | 50,410.00 USD | 31,970.00 USD |
| `7D` | `0.8780` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 261,940.00 USD | 131,240.00 USD | 233,250.00 USD |
| `1D` | `0.8800` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 13,090.00 USD | 12,550.00 USD | 41,060.00 USD |
| `7D` | `0.8800` | 19,990,000.00 USD | 0.00 USD | 19,990,000.00 USD | 427,340.00 USD | 120,050.00 USD | 424,530.00 USD |
| `1D` | `0.8820` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 130,020.00 USD | 63,620.00 USD | 160,430.00 USD |
| `7D` | `0.8820` | 19,010,000.00 USD | 0.00 USD | 19,010,000.00 USD | 561,150.00 USD | 242,470.00 USD | 320,530.00 USD |
| `1D` | `0.8840` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 301,690.00 USD | 66,580.00 USD | 152,330.00 USD |
| `7D` | `0.8840` | 17,890,000.00 USD | 0.00 USD | 17,890,000.00 USD | 772,020.00 USD | 222,890.00 USD | 525,230.00 USD |
| `1D` | `0.8860` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 272,520.00 USD | 127,540.00 USD | 90,270.00 USD |
| `7D` | `0.8860` | 16,370,000.00 USD | 0.00 USD | 16,370,000.00 USD | 520,190.00 USD | 257,680.00 USD | 263,750.00 USD |
| `1D` | `0.8880` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 297,140.00 USD | 211,060.00 USD | 485,780.00 USD |
| `7D` | `0.8880` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 1,050,000.00 USD | 404,050.00 USD | 992,340.00 USD |
| `1D` | `0.8900` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 515,380.00 USD | 158,940.00 USD | 512,370.00 USD |
| `7D` | `0.8900` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 1,180,000.00 USD | 483,970.00 USD | 997,510.00 USD |
| `1D` | `0.8920` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 242,700.00 USD | 69,180.00 USD | 108,670.00 USD |
| `7D` | `0.8920` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 1,550,000.00 USD | 594,410.00 USD | 705,690.00 USD |
| `1D` | `0.8940` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 207,140.00 USD | 182,590.00 USD | 376,280.00 USD |
| `7D` | `0.8940` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 1,220,000.00 USD | 617,220.00 USD | 1,050,000.00 USD |
| `1D` | `0.8960` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 140,660.00 USD | 160,980.00 USD | 230,410.00 USD |
| `7D` | `0.8960` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 657,470.00 USD | 365,250.00 USD | 767,600.00 USD |
| `1D` | `0.8980` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 128,530.00 USD | 68,440.00 USD | 103,680.00 USD |
| `7D` | `0.8980` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 656,780.00 USD | 284,000.00 USD | 172,720.00 USD |
| `1D` | `0.9000` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 79,530.00 USD | 24,210.00 USD | 70,810.00 USD |
| `7D` | `0.9000` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 127,760.00 USD | 33,800.00 USD | 5,330.00 USD |
| `1D` | `0.9020` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 66,430.00 USD | 56,290.00 USD | 190,680.00 USD |
| `7D` | `0.9020` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 8,440.00 USD | 52,590.00 USD | 118,850.00 USD |
| `1D` | `0.9040` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 128,110.00 USD | 81,940.00 USD | 142,290.00 USD |
| `7D` | `0.9040` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 98,990.00 USD | 0.00 USD | 72,670.00 USD |
| `1D` | `0.9060` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 215,300.00 USD | 10,170.00 USD | 58,360.00 USD |
| `7D` | `0.9060` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 245,950.00 USD | 0.00 USD | 940.28 USD |
| `1D` | `0.9080` | 977,130.00 USD | 0.00 USD | 977,130.00 USD | 305,430.00 USD | 116,800.00 USD | 213,980.00 USD |
| `7D` | `0.9080` | 807,480.00 USD | 0.00 USD | 807,480.00 USD | 175,380.00 USD | 19,890.00 USD | 164,800.00 USD |
| `1D` | `0.9100` | 340,920.00 USD | 0.00 USD | 340,920.00 USD | 35,010.00 USD | 37,530.00 USD | 35,900.00 USD |
| `7D` | `0.9100` | 447,410.00 USD | 0.00 USD | 447,410.00 USD | 123,910.00 USD | 0.00 USD | 91,110.00 USD |
| `7D` | `0.9120` | 232,390.00 USD | 0.00 USD | 232,390.00 USD | 88,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9140` | 232,490.00 USD | 0.00 USD | 232,490.00 USD | 22,970.00 USD | 0.00 USD | 71,710.00 USD |
| `7D` | `0.9140` | 143,540.00 USD | 0.00 USD | 143,540.00 USD | 143,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9150` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9160` | 137,810.00 USD | 0.00 USD | 137,810.00 USD | 74,950.00 USD | 17,730.00 USD | 45,120.00 USD |
| `7D` | `0.9160` | 171,920.00 USD | 171,920.00 USD | 0.00 USD | 171,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9170` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9180` | 21,140.00 USD | 21,140.00 USD | 0.00 USD | 12,120.00 USD | 9,020.00 USD | 0.00 USD |
| `7D` | `0.9180` | 195,710.00 USD | 195,710.00 USD | 0.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD |
| `7D` | `0.9200` | 663,000.00 USD | 663,000.00 USD | 0.00 USD | 386,820.00 USD | 16,660.00 USD | 63,810.00 USD |
| `1D` | `0.9220` | 226,920.00 USD | 226,920.00 USD | 0.00 USD | 32,990.00 USD | 39,420.00 USD | 133,380.00 USD |
| `7D` | `0.9220` | 884,090.00 USD | 884,090.00 USD | 0.00 USD | 0.00 USD | 64,540.00 USD | 156,550.00 USD |
| `1D` | `0.9240` | 605,570.00 USD | 605,570.00 USD | 0.00 USD | 170,280.00 USD | 58,320.00 USD | 150,050.00 USD |
| `7D` | `0.9240` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 104,080.00 USD | 41,710.00 USD | 184,480.00 USD |
| `1D` | `0.9260` | 697,730.00 USD | 697,730.00 USD | 0.00 USD | 63,790.00 USD | 28,360.00 USD | 0.00 USD |
| `7D` | `0.9260` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 102,010.00 USD | 0.00 USD | 233.04 USD |
| `1D` | `0.9280` | 754,010.00 USD | 754,010.00 USD | 0.00 USD | 0.00 USD | 44,480.00 USD | 11,800.00 USD |
| `7D` | `0.9280` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 107,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9300` | 905,820.00 USD | 905,820.00 USD | 0.00 USD | 32,650.00 USD | 40,000.00 USD | 79,160.00 USD |
| `7D` | `0.9300` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 177,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9320` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 100,660.00 USD | 15,870.00 USD | 0.00 USD |
| `7D` | `0.9320` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 50,420.00 USD | 63,160.00 USD |
| `7D` | `0.9340` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 50,160.00 USD | 52,710.00 USD | 0.00 USD |
| `1D` | `0.9360` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 25,730.00 USD | 33,250.00 USD | 103,620.00 USD |
| `7D` | `0.9360` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 122,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9380` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 262,840.00 USD | 118,850.00 USD | 293,510.00 USD |
| `7D` | `0.9380` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 168,030.00 USD | 0.00 USD | 177,680.00 USD |
| `1D` | `0.9400` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD |
| `7D` | `0.9400` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 166,670.00 USD | 33,320.00 USD | 127,620.00 USD |
| `7D` | `0.9420` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 20,860.00 USD | 0.00 USD |
| `1D` | `0.9440` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD |
| `7D` | `0.9440` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 216,440.00 USD | 0.00 USD |
| `1D` | `0.9460` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 56,940.00 USD | 28,980.00 USD | 160,360.00 USD |
| `7D` | `0.9460` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD |
| `1D` | `0.9480` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 89,360.00 USD | 66,670.00 USD | 56,220.00 USD |
| `7D` | `0.9480` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 54,830.00 USD | 208,890.00 USD |
| `1D` | `0.9500` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 17,970.00 USD | 36,000.00 USD | 69,470.00 USD |
| `7D` | `0.9500` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 29,180.00 USD | 371,330.00 USD |
| `1D` | `0.9520` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 51,320.00 USD | 28,040.00 USD | 195,920.00 USD |
| `7D` | `0.9520` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 87,720.00 USD | 360,980.00 USD |
| `1D` | `0.9540` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 62,990.00 USD | 66,810.00 USD | 55,690.00 USD |
| `7D` | `0.9540` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 10,500.00 USD | 2,560.00 USD | 60,590.00 USD |
| `1D` | `0.9560` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 21,240.00 USD | 33,360.00 USD | 15,050.00 USD |
| `7D` | `0.9560` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 72,330.00 USD | 2,240.00 USD | 0.00 USD |
| `1D` | `0.9580` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 689.00 USD | 43,140.00 USD | 159.08 USD |
| `7D` | `0.9580` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 846,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9600` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 110,540.00 USD | 65,690.00 USD | 82,850.00 USD |
| `7D` | `0.9600` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 356,870.00 USD | 73,200.00 USD | 131,760.00 USD |
| `1D` | `0.9620` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 299,180.00 USD | 137,300.00 USD | 272,910.00 USD |
| `7D` | `0.9620` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 715,790.00 USD | 231,300.00 USD | 588,700.00 USD |
| `1D` | `0.9640` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 324,050.00 USD | 116,210.00 USD | 197,090.00 USD |
| `7D` | `0.9640` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 693,720.00 USD | 366,520.00 USD | 508,130.00 USD |
| `1D` | `0.9660` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 243,570.00 USD | 143,870.00 USD | 119,930.00 USD |
| `7D` | `0.9660` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 995,070.00 USD | 220,060.00 USD | 554,270.00 USD |
| `1D` | `0.9680` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 244,090.00 USD | 77,940.00 USD | 280,080.00 USD |
| `7D` | `0.9680` | 12,760,000.00 USD | 12,760,000.00 USD | 0.00 USD | 911,470.00 USD | 645,640.00 USD | 613,760.00 USD |
| `1D` | `0.9700` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 257,240.00 USD | 130,350.00 USD | 199,290.00 USD |
| `7D` | `0.9700` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 694,250.00 USD | 344,900.00 USD | 380,820.00 USD |
| `1D` | `0.9720` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 122,820.00 USD | 117,970.00 USD | 126,930.00 USD |
| `7D` | `0.9720` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 398,310.00 USD | 184,170.00 USD | 139,530.00 USD |
| `1D` | `0.9740` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 79,700.00 USD | 30,700.00 USD | 39,830.00 USD |
| `7D` | `0.9740` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 309,060.00 USD | 116,990.00 USD | 120,700.00 USD |
| `1D` | `0.9760` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 30,090.00 USD | 24,570.00 USD | 76,650.00 USD |
| `7D` | `0.9760` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 182,900.00 USD | 286,070.00 USD | 218,590.00 USD |
| `1D` | `0.9780` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 4,640.00 USD | 22,340.00 USD | 118,360.00 USD |
| `7D` | `0.9780` | 17,290,000.00 USD | 17,290,000.00 USD | 0.00 USD | 441,770.00 USD | 196,630.00 USD | 509,920.00 USD |
| `1D` | `0.9800` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 65,550.00 USD | 48,270.00 USD | 144,660.00 USD |
| `7D` | `0.9800` | 17,920,000.00 USD | 17,920,000.00 USD | 0.00 USD | 341,810.00 USD | 87,560.00 USD | 204,470.00 USD |
| `1D` | `0.9820` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD |
| `7D` | `0.9820` | 18,230,000.00 USD | 18,230,000.00 USD | 0.00 USD | 108,220.00 USD | 52,950.00 USD | 147,230.00 USD |
| `1D` | `0.9840` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 58,950.00 USD | 66,720.00 USD | 18,200.00 USD |
| `7D` | `0.9840` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 395,810.00 USD | 123,000.00 USD | 176,600.00 USD |
| `1D` | `0.9860` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 93,180.00 USD | 38,470.00 USD | 86,180.00 USD |
| `7D` | `0.9860` | 19,260,000.00 USD | 19,260,000.00 USD | 0.00 USD | 107,440.00 USD | 154,250.00 USD | 72,460.00 USD |
| `1D` | `0.9880` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 83,850.00 USD | 26,290.00 USD | 61,740.00 USD |
| `7D` | `0.9880` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 209,770.00 USD | 64,380.00 USD | 27,710.00 USD |
| `1D` | `0.9900` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 87,940.00 USD | 43,020.00 USD | 51,990.00 USD |
| `7D` | `0.9900` | 19,870,000.00 USD | 19,870,000.00 USD | 0.00 USD | 201,410.00 USD | 100,430.00 USD | 6,090.00 USD |
| `1D` | `0.9920` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 62,110.00 USD | 41,490.00 USD | 21,600.00 USD |
| `7D` | `0.9920` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 288,210.00 USD | 79,650.00 USD | 84,340.00 USD |
| `1D` | `0.9940` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 48,130.00 USD | 36,960.00 USD | 58,940.00 USD |
| `7D` | `0.9940` | 20,800,000.00 USD | 20,800,000.00 USD | 0.00 USD | 143,340.00 USD | 183,310.00 USD | 149,950.00 USD |
| `1D` | `0.9960` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 6,270.00 USD | 7,010.00 USD | 20,320.00 USD |
| `7D` | `0.9960` | 21,250,000.00 USD | 21,250,000.00 USD | 0.00 USD | 107,780.00 USD | 55,790.00 USD | 287,580.00 USD |
| `1D` | `0.9980` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 109,650.00 USD | 21,830.00 USD | 145,310.00 USD |
| `7D` | `0.9980` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 238,490.00 USD | 42,080.00 USD | 165,240.00 USD |
| `1D` | `1.00` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 17,400.00 USD | 16,450.00 USD | 6,470.00 USD |
| `7D` | `1.00` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 94,210.00 USD | 53,610.00 USD | 64,730.00 USD |
| `1D` | `1.00` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 15,900.00 USD | 17,990.00 USD | 26,580.00 USD |
| `7D` | `1.00` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 250,490.00 USD | 51,850.00 USD | 254,480.00 USD |
| `1D` | `1.00` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 16,070.00 USD | 21,070.00 USD | 30,450.00 USD |
| `7D` | `1.00` | 22,790,000.00 USD | 22,790,000.00 USD | 0.00 USD | 155,110.00 USD | 45,420.00 USD | 124,180.00 USD |
| `1D` | `1.01` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 9,400.00 USD | 14,230.00 USD | 8,760.00 USD |
| `7D` | `1.01` | 22,990,000.00 USD | 22,990,000.00 USD | 0.00 USD | 109,230.00 USD | 24,230.00 USD | 69,300.00 USD |
| `1D` | `1.01` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 18,940.00 USD | 9,170.00 USD | 12,090.00 USD |
| `7D` | `1.01` | 23,590,000.00 USD | 23,590,000.00 USD | 0.00 USD | 274,240.00 USD | 66,150.00 USD | 255,820.00 USD |
| `1D` | `1.01` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 18,290.00 USD | 5,570.00 USD | 14,820.00 USD |
| `7D` | `1.01` | 24,250,000.00 USD | 24,250,000.00 USD | 0.00 USD | 311,680.00 USD | 74,250.00 USD | 271,810.00 USD |
| `1D` | `1.01` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 21,660.00 USD | 13,820.00 USD | 33,850.00 USD |
| `7D` | `1.01` | 25,300,000.00 USD | 25,300,000.00 USD | 0.00 USD | 385,660.00 USD | 249,310.00 USD | 418,320.00 USD |
| `1D` | `1.01` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 13,360.00 USD | 11,780.00 USD | 28,370.00 USD |
| `7D` | `1.01` | 26,030,000.00 USD | 26,030,000.00 USD | 0.00 USD | 341,120.00 USD | 208,060.00 USD | 179,100.00 USD |
| `1D` | `1.02` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 22,200.00 USD | 10,550.00 USD | 6,610.00 USD |
| `7D` | `1.02` | 26,930,000.00 USD | 26,930,000.00 USD | 0.00 USD | 390,660.00 USD | 101,810.00 USD | 413,590.00 USD |
| `1D` | `1.02` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 18,720.00 USD | 4,150.00 USD | 133.18 USD |
| `7D` | `1.02` | 27,580,000.00 USD | 27,580,000.00 USD | 0.00 USD | 268,340.00 USD | 28,880.00 USD | 345,140.00 USD |
| `1D` | `1.02` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD |
| `7D` | `1.02` | 28,230,000.00 USD | 28,230,000.00 USD | 0.00 USD | 201,610.00 USD | 96,960.00 USD | 352,960.00 USD |
| `1D` | `1.02` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD |
| `7D` | `1.02` | 28,520,000.00 USD | 28,520,000.00 USD | 0.00 USD | 163,000.00 USD | 31,420.00 USD | 95,100.00 USD |
| `1D` | `1.02` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD |
| `7D` | `1.02` | 28,750,000.00 USD | 28,750,000.00 USD | 0.00 USD | 75,030.00 USD | 60,830.00 USD | 95,430.00 USD |
| `1D` | `1.03` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD |
| `7D` | `1.03` | 29,140,000.00 USD | 29,140,000.00 USD | 0.00 USD | 173,720.00 USD | 56,910.00 USD | 158,480.00 USD |
| `1D` | `1.03` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD |
| `7D` | `1.03` | 29,230,000.00 USD | 29,230,000.00 USD | 0.00 USD | 40,590.00 USD | 31,490.00 USD | 18,640.00 USD |
| `1D` | `1.03` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 8,830.00 USD | 11,740.00 USD | 10,170.00 USD |
| `7D` | `1.03` | 29,480,000.00 USD | 29,480,000.00 USD | 0.00 USD | 117,500.00 USD | 46,890.00 USD | 89,540.00 USD |
| `7D` | `1.03` | 29,950,000.00 USD | 29,950,000.00 USD | 0.00 USD | 145,150.00 USD | 125,610.00 USD | 192,860.00 USD |
| `7D` | `1.03` | 30,330,000.00 USD | 30,330,000.00 USD | 0.00 USD | 166,040.00 USD | 102,410.00 USD | 118,090.00 USD |
| `7D` | `1.04` | 30,720,000.00 USD | 30,720,000.00 USD | 0.00 USD | 184,730.00 USD | 21,870.00 USD | 183,710.00 USD |
| `7D` | `1.04` | 31,070,000.00 USD | 31,070,000.00 USD | 0.00 USD | 146,060.00 USD | 27,060.00 USD | 172,430.00 USD |
| `7D` | `1.04` | 31,290,000.00 USD | 31,290,000.00 USD | 0.00 USD | 74,160.00 USD | 57,530.00 USD | 88,010.00 USD |
| `7D` | `1.04` | 31,380,000.00 USD | 31,380,000.00 USD | 0.00 USD | 53,240.00 USD | 12,870.00 USD | 31,560.00 USD |
| `7D` | `1.04` | 31,540,000.00 USD | 31,540,000.00 USD | 0.00 USD | 77,760.00 USD | 65,330.00 USD | 12,990.00 USD |
| `7D` | `1.05` | 31,640,000.00 USD | 31,640,000.00 USD | 0.00 USD | 72,850.00 USD | 29,490.00 USD | 1,500.00 USD |
| `7D` | `1.05` | 31,720,000.00 USD | 31,720,000.00 USD | 0.00 USD | 49,580.00 USD | 12,030.00 USD | 15,500.00 USD |
| `7D` | `1.05` | 31,730,000.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 3,180.00 USD | 96.48 USD |
| `7D` | `1.05` | 31,820,000.00 USD | 31,820,000.00 USD | 0.00 USD | 24,160.00 USD | 46,330.00 USD | 21,360.00 USD |
| `7D` | `1.05` | 31,880,000.00 USD | 31,880,000.00 USD | 0.00 USD | 8,480.00 USD | 2,340.00 USD | 53,570.00 USD |
| `7D` | `1.06` | 31,890,000.00 USD | 31,890,000.00 USD | 0.00 USD | 5,910.00 USD | 5,170.00 USD | 154.98 USD |
| `7D` | `1.06` | 31,900,000.00 USD | 31,900,000.00 USD | 0.00 USD | 3,120.00 USD | 3,350.00 USD | 173.28 USD |
| `7D` | `1.06` | 31,930,000.00 USD | 31,930,000.00 USD | 0.00 USD | 15,370.00 USD | 3,080.00 USD | 11,860.00 USD |
| `7D` | `1.06` | 31,940,000.00 USD | 31,940,000.00 USD | 0.00 USD | 4,660.00 USD | 786.13 USD | 85.40 USD |
| `7D` | `1.06` | 31,940,000.00 USD | 31,940,000.00 USD | 0.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `603.11M` | Total OI Tokens: `657,337,786.6 SUI`
  * 1h OI Change: `-2.02%` | 4h OI Change: `-4.79%` | 24h OI Change: `-5.02%`
  * Exchange Breakdown: Binance=`116.96M` | Bybit=`79.20M` | OKX=`33.34M` | Hyperliquid=`30.82M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `19.75K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0078%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0049%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `46.90%` | `53.10%` | `0.88` | 16,800,000.00 USD |
| `15M` | `Binance` | `48.8%` | `51.2%` | `0.95` | 7,700,000.00 USD |
| `15M` | `OKX` | `48.5%` | `51.5%` | `0.94` | 1,940,000.00 USD |
| `15M` | `Bybit` | `46.17%` | `53.83%` | `0.86` | 2,390,000.00 USD |
| `15M` | `KuCoin` | `42.31%` | `57.69%` | `0.73` | 188,790.00 USD |
| `15M` | `Gate` | `51.26%` | `48.74%` | `1.05` | 347,700.00 USD |
| `15M` | `Bitget` | `38.72%` | `61.28%` | `0.63` | 961,800.00 USD |
| `15M` | `BingX` | `58.75%` | `41.25%` | `1.42` | 540,950.00 USD |
| `15M` | `MEXC` | `43.72%` | `56.28%` | `0.78` | 1,240,000.00 USD |
| `15M` | `Bitunix` | `37.15%` | `62.85%` | `0.59` | 655,590.00 USD |
| `15M` | `Hyperliquid` | `33.13%` | `66.87%` | `0.50` | 434,800.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.8%` | `45.2%` | `1.21` | 49,210.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `52.34%` | `47.66%` | `1.10` | 162,540.00 USD |
| `15M` | `HTX` | `72.04%` | `27.96%` | `2.58` | 25,690.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `47.63%` | `52.37%` | `0.91` | 115,340.00 USD |
| `15M` | `Aster` | `30.03%` | `69.97%` | `0.43` | 45,590.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `31.35%` | `68.65%` | `0.46` | 5,330.00 USD |
| `15M` | `Whale Positions` | `48.8%` | `51.2%` | `0.95` | 7,700,000.00 USD |
| `15M` | `Global Accounts` | `46.90%` | `53.10%` | `0.88` | 16,800,000.00 USD |
| `1H` | `SUI` | `44.58%` | `55.42%` | `0.80` | 30,240,000.00 USD |
| `1H` | `Binance` | `48.67%` | `51.33%` | `0.95` | 11,070,000.00 USD |
| `1H` | `OKX` | `56.77%` | `43.23%` | `1.31` | 2,150,000.00 USD |
| `1H` | `Bybit` | `43.56%` | `56.44%` | `0.77` | 2,340,000.00 USD |
| `1H` | `KuCoin` | `43.14%` | `56.86%` | `0.76` | 177,550.00 USD |
| `1H` | `Gate` | `41.43%` | `58.57%` | `0.71` | 823,130.00 USD |
| `1H` | `Bitget` | `45.62%` | `54.38%` | `0.84` | 556,040.00 USD |
| `1H` | `BingX` | `41.63%` | `58.37%` | `0.71` | 3,680,000.00 USD |
| `1H` | `MEXC` | `43.69%` | `56.31%` | `0.78` | 1,600,000.00 USD |
| `1H` | `Bitunix` | `40.1%` | `59.9%` | `0.67` | 884,130.00 USD |
| `1H` | `Hyperliquid` | `42.75%` | `57.25%` | `0.75` | 470,930.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.35%` | `54.65%` | `0.83` | 4,940,000.00 USD |
| `1H` | `Crypto.com` | `76.17%` | `23.83%` | `3.20` | 4,580.00 USD |
| `1H` | `WhiteBIT` | `0.78%` | `99.22%` | `0.01` | 1,270,000.00 USD |
| `1H` | `HTX` | `68.42%` | `31.58%` | `2.17` | 11,940.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `68.38%` | `31.62%` | `2.16` | 159,870.00 USD |
| `1H` | `Aster` | `35.58%` | `64.42%` | `0.55` | 36,770.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `25.64%` | `74.36%` | `0.34` | 78,440.00 USD |
| `1H` | `Whale Positions` | `48.67%` | `51.33%` | `0.95` | 11,070,000.00 USD |
| `1H` | `Global Accounts` | `44.58%` | `55.42%` | `0.80` | 30,240,000.00 USD |
| `4H` | `SUI` | `44.03%` | `55.97%` | `0.79` | 80,660,000.00 USD |
| `4H` | `Binance` | `46.61%` | `53.39%` | `0.87` | 25,380,000.00 USD |
| `4H` | `OKX` | `47.79%` | `52.21%` | `0.92` | 5,630,000.00 USD |
| `4H` | `Bybit` | `47.8%` | `52.2%` | `0.92` | 5,020,000.00 USD |
| `4H` | `KuCoin` | `46.67%` | `53.33%` | `0.88` | 544,540.00 USD |
| `4H` | `Gate` | `48.34%` | `51.66%` | `0.94` | 1,700,000.00 USD |
| `4H` | `Bitget` | `40.92%` | `59.08%` | `0.69` | 1,440,000.00 USD |
| `4H` | `BingX` | `45.14%` | `54.86%` | `0.82` | 14,670,000.00 USD |
| `4H` | `MEXC` | `53.52%` | `46.48%` | `1.15` | 4,890,000.00 USD |
| `4H` | `Bitunix` | `45.81%` | `54.19%` | `0.85` | 2,580,000.00 USD |
| `4H` | `Hyperliquid` | `38.87%` | `61.13%` | `0.64` | 715,570.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.94%` | `52.06%` | `0.92` | 12,310,000.00 USD |
| `4H` | `Crypto.com` | `80.79%` | `19.21%` | `4.21` | 17,240.00 USD |
| `4H` | `WhiteBIT` | `0.2%` | `99.8%` | `0.00` | 5,150,000.00 USD |
| `4H` | `HTX` | `58.67%` | `41.33%` | `1.42` | 21,600.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `60.08%` | `39.92%` | `1.51` | 320,850.00 USD |
| `4H` | `Aster` | `43.95%` | `56.05%` | `0.78` | 147,470.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.56%` | `72.44%` | `0.38` | 134,730.00 USD |
| `4H` | `Whale Positions` | `46.61%` | `53.39%` | `0.87` | 25,380,000.00 USD |
| `4H` | `Global Accounts` | `44.03%` | `55.97%` | `0.79` | 80,660,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9329` | `0.9340` | `0.9329` | `0.9372` | `0.9308` | 2,243,724.91 USD | 1,007,080.32 USD | 1,236,644.58 USD | -229,564.26 USD | `-10.23%` | `7B / 14S` |
| `0:00 UTC` | `0.9264` | `0.9272` | `0.9264` | `0.9323` | `0.9251` | 2,780,290.59 USD | 1,245,269.00 USD | 1,535,021.59 USD | -289,752.58 USD | `-10.42%` | `8B / 17S` |
| `5:00 UTC` | `0.9324` | `0.9295` | `0.9324` | `0.9329` | `0.9253` | 3,699,722.99 USD | 2,179,603.27 USD | 1,520,119.72 USD | 659,483.55 USD | `+17.83%` | `23B / 6S` |
| `0:00 UTC` | `0.9297` | `0.9291` | `0.9297` | `0.9317` | `0.9275` | 1,239,749.35 USD | 593,055.04 USD | 646,694.30 USD | -53,639.26 USD | `-4.33%` | `5B / 5S` |
| `5:00 UTC` | `0.9315` | `0.9301` | `0.9315` | `0.9321` | `0.9274` | 1,221,799.97 USD | 672,184.00 USD | 549,615.97 USD | 122,568.03 USD | `+10.03%` | `9B / 6S` |
| `0:00 UTC` | `0.9318` | `0.9320` | `0.9318` | `0.9338` | `0.9294` | 1,810,474.94 USD | 929,976.91 USD | 880,498.03 USD | 49,478.88 USD | `+2.73%` | `7B / 6S` |
| `5:00 UTC` | `0.9302` | `0.9304` | `0.9302` | `0.9331` | `0.9288` | 1,273,512.84 USD | 565,164.16 USD | 708,348.68 USD | -143,184.52 USD | `-11.24%` | `4B / 11S` |
| `0:00 UTC` | `0.9115` | `0.9168` | `0.9115` | `0.9303` | `0.9099` | 9,410,634.53 USD | 4,625,948.50 USD | 4,784,686.02 USD | -158,737.52 USD | `-1.69%` | `3B / 20S` |
| `5:00 UTC` | `0.9172` | `0.9175` | `0.9172` | `0.9204` | `0.9146` | 2,946,350.12 USD | 1,501,911.34 USD | 1,444,438.78 USD | 57,472.55 USD | `+1.95%` | `10B / 6S` |
| `0:00 UTC` | `0.9166` | `0.9167` | `0.9166` | `0.9176` | `0.9160` | 146,370.38 USD | 104,560.02 USD | 41,810.36 USD | 62,749.65 USD | `+42.87%` | `9B / 1S` |

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
| `5m` | -931,930.00 USD | 17,620.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,010,000.00 USD | 371,390.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,860,000.00 USD | 798,590.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,900,000.00 USD | -88,870.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,070,000.00 USD | 2,200,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -3,010,000.00 USD | -3,270,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 855,210.00 USD | -5,590,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 1,230,000.00 USD | -4,600,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 927,440.00 USD | -4,480,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -3,550,000.00 USD | -16,130,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -17,280,000.00 USD | -64,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -146,040,000.00 USD | -466,370,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-931.93K` | 15m=`-1.01M` | 1h=`-2.90M` | 24h=`-3.55M`
* Futures Capital Netflows: 5m=`+17.62K` | 15m=`+371.39K` | 1h=`-88.87K` | 24h=`-16.13M`
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
  * `2026-10-30 01:35:49 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:00:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
