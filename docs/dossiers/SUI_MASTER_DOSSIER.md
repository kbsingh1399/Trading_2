# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:35:21 IST` (`2026-10-29 19:05:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.9277` | `0.9308` | `0.9277` | `0.9302` | `1,272,325` | 1,182,484.27 USD | 179,187.88 USD | `+15.15%` | -9,933,306.14 USD | `+1.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9303` | `0.9329` | `0.9301` | `0.9312` | `1,444,264` | 1,345,787.01 USD | 379,268.21 USD | `+28.18%` | -9,554,037.93 USD | `+1.99` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9311` | `0.9317` | `0.9276` | `0.9292` | `594,771` | 552,626.44 USD | -80,965.80 USD | `-14.65%` | -9,635,003.72 USD | `-0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9314` | `0.9322` | `0.9250` | `0.9271` | `2,998,756` | 2,780,290.59 USD | -289,752.58 USD | `-10.42%` | -10,175,729.11 USD | `-0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9271` | `0.9329` | `0.9252` | `0.9312` | `3,980,448` | 3,699,722.99 USD | 659,483.55 USD | `+17.83%` | -9,516,245.56 USD | `+1.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9311` | `0.9317` | `0.9276` | `0.9289` | `604,983` | 562,113.04 USD | -90,380.12 USD | `-16.08%` | -9,606,625.69 USD | `-0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9475` | `0.9481` | `0.9282` | `0.9361` | `13,061,944` | 12,258,406.01 USD | -1,086,968.70 USD | `-8.87%` | -10,586,025.92 USD | `-0.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9362` | `0.9377` | `0.9250` | `0.9312` | `11,914,670` | 11,092,555.41 USD | -218,628.60 USD | `-1.97%` | -10,804,654.52 USD | `+0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9311` | `0.9317` | `0.9276` | `0.9289` | `604,983` | 562,113.04 USD | -90,380.12 USD | `-16.08%` | -10,895,034.64 USD | `+0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -10,284,836.62 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -8,256,119.70 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9289` | `41,806,207` | 39,355,240.16 USD | -2,638,914.94 USD | `-6.71%` | -10,895,034.64 USD | `-0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9429` | `0.9465` | `0.8981` | `0.9043` | `62,278,068` | 57,050,963.40 USD | -8,597,484.18 USD | `-15.07%` | -10,264,352.04 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -10,145,601.55 USD | `+0.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -10,284,836.62 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -8,256,119.70 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9289` | `41,806,207` | 39,355,240.16 USD | -2,638,914.94 USD | `-6.71%` | -10,895,034.64 USD | `-0.24` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.9286` | `2337.0000` | 2,170.26 USD | 72,893.17 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.9287` | `2337.3000` | 2,170.72 USD | 39,207.14 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9287` | `17684.3000` | 16,423.59 USD | 55,630.72 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9287` | `16251.4000` | 15,092.19 USD | 70,722.91 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.9288` | `2726.6000` | 2,532.60 USD | 27,516.38 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9288` | `2337.3000` | 2,170.95 USD | 29,687.33 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9288` | `2523.1000` | 2,343.48 USD | 32,030.81 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.9288` | `5389.5000` | 5,005.61 USD | 37,036.42 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.9289` | `6959.0000` | 6,464.28 USD | 21,869.48 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.9289` | `908.2000` | 843.63 USD | 22,713.10 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `0.9289` | `2336.9000` | 2,170.72 USD | 24,883.83 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9289` | `107.6000` | 99.95 USD | 24,983.77 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.9290` | `2155.2000` | 2,002.22 USD | 6,600.60 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.9290` | `2336.6000` | 2,170.65 USD | 8,771.25 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9290` | `5388.6000` | 5,005.85 USD | 13,777.10 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9290` | `1752.6000` | 1,628.10 USD | 15,405.19 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.9291` | `701.5000` | 651.79 USD | 3,185.27 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.9291` | `1077.4000` | 1,001.04 USD | 4,186.31 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.9291` | `443.5000` | 412.06 USD | 4,598.37 USD | `1 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `0.9292` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.93` | `0.00%` | `-` |
| `BID` | `0.9292` | `2726.6000` | 2,533.47 USD | 2,533.47 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `0.9293` | `1752.8000` | 1,628.91 USD | 3,726.11 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9293` | `1077.3000` | 1,001.12 USD | 2,097.19 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9293` | `400.0000` | 371.71 USD | 1,096.07 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.9293` | `779.5000` | 724.36 USD | 724.36 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `0.9294` | `2337.1000` | 2,172.19 USD | 9,071.48 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9294` | `2337.1000` | 2,172.08 USD | 6,899.29 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9294` | `1077.2000` | 1,001.11 USD | 4,727.21 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.9295` | `2351.3000` | 2,185.60 USD | 17,371.05 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9295` | `113.7000` | 105.69 USD | 15,185.44 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9295` | `1059.1000` | 984.44 USD | 15,079.76 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9295` | `2113.7000` | 1,964.68 USD | 14,095.31 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9295` | `113.7000` | 105.68 USD | 12,130.63 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9295` | `113.7000` | 105.68 USD | 12,024.95 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.9295` | `613.7000` | 570.42 USD | 11,919.26 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9295` | `2450.2000` | 2,277.36 USD | 11,348.85 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.9296` | `2336.8000` | 2,172.38 USD | 31,971.06 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.9296` | `5492.1000` | 5,105.62 USD | 29,798.68 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.9296` | `1335.3000` | 1,241.31 USD | 24,693.06 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.9296` | `4337.1000` | 4,031.77 USD | 23,451.75 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.9296` | `2204.2000` | 2,048.94 USD | 19,419.98 USD | `2 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `657` | `0xb83d...6e36` | `SHORT` | 3,558,737.31 USD | `3,817,609.40` | `1.11` | `0.9327` | `33.74` | 659,998.01 USD | `+18.55%` | `3X Cross` |
| `989` | `0xa2ce...3126` | `LONG` | 2,326,984.68 USD | `2,500,010.40` | `0.8597` | `0.9327` | `0.000000` | 177,778.15 USD | `+7.64%` | `10X Cross` |
| `1465` | `0x9946...0852` | `SHORT` | 1,550,849.84 USD | `1,664,573.50` | `1.08` | `0.9327` | `1.56` | 245,469.77 USD | `+15.83%` | `10X Cross` |
| `1776` | `0x9aa5...58af` | `SHORT` | 1,198,924.47 USD | `1,288,168.80` | `1.14` | `0.9327` | `6.68` | 268,768.42 USD | `+22.42%` | `10X Cross` |
| `1861` | `0x9df2...c665` | `SHORT` | 1,118,628.00 USD | `1,200,000.00` | `0.7465` | `0.9327` | `24.39` | -222,775.60 USD | `-19.92%` | `10X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `0.9302` | 5,006.54 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9302 USD [API] | `2026-10-27 23:06:13` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9706` (Vol: 378,700.00 USD, Dist: `+4.19%`) | Long MP=`0.8887` (Vol: 676,100.00 USD, Dist: `--4.60%`)
  * 48H Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+4.19%`) | Long MP=`0.8887` (Vol: 546,500.00 USD, Dist: `--4.60%`)
  * 3D Horizon: Short MP=`0.9706` (Vol: 230,000.00 USD, Dist: `+4.19%`) | Long MP=`0.8887` (Vol: 859,700.00 USD, Dist: `--4.60%`)
  * 7D Horizon: Short MP=`0.9685` (Vol: 565,100.00 USD, Dist: `+3.96%`) | Long MP=`0.8890` (Vol: 1,100,000.00 USD, Dist: `--4.58%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1865` | 6,010.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 1,970.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 138.65 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 307.45 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 264.60 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 21,870.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 557.56 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 1,910.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 238.66 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 5,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2895` | 7,470.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 687.92 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 7,100.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 7,310.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3185` | 3,140.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3205` | 157.21 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3395` | 378.58 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3485` | 2,000.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,640.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3645` | 227.81 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3765` | 6,630.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3825` | 26,770.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 357.06 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 69,910.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4015` | 281.05 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 102.86 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 467.50 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4245` | 1,290.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4295` | 475.03 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4315` | 1,120.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4365` | 43,480.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 6,070.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4415` | 5,800.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 219.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4445` | 573.54 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 16,360.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 3,210.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 702.74 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 295.78 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 899.31 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 5,320.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4725` | 472.50 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 33,280.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4815` | 252.11 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 6,330.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 373.10 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,120.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 258.21 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5075` | 842.55 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 2,030.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 2,490.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 5,330.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 1,240.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5205` | 422.33 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5225` | 244.90 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 5,280.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5265` | 347.70 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 125,730.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 264.06 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 417.12 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 1,190.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5385` | 5,850.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 319.98 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5415` | 1,390.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5435` | 1,620.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 16,060.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 441.84 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 195.93 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 570.01 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 182.72 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 1,010.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 1,240.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 278.45 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 11,670.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 135,670.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5875` | 58,220.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 297,240.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 5,540.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 151.97 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6095` | 1,390.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,780.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 213.64 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 245.40 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 2,670.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 4,400.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 39,890.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6265` | 546.18 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 3,510.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 450.05 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 207.17 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 2,850.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 2,240.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6385` | 1,120.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6395` | 2,270.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 939.17 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 7,900.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 489.83 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 471.21 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 8,080.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 210.50 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 721.59 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 631.12 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 408,650.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 126,530.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 1,580.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 7,070.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 10,930.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 2,820.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 602.30 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 5,280.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 2,810.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6695` | 161.22 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 37,780.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,500.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 5,100.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 2,950.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 5,620.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 9,020.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 3,380.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 15,920.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 7,040.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,790.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 480.49 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 83,790.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6925` | 17,150.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 2,980.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 102.25 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 11,290.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,390.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 759.59 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 769.59 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 787.73 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 3,890.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 2,550.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 3,530.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 569.20 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 156.39 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 22,830.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 150.40 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 1,470.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 11,720.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 5,110.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 5,150.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 1,280.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 762.57 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 214.03 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 907.93 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 311,430.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 46,940.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 147.01 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 1,110.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 784,090.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 1,630.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 103,310.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7485` | 105.91 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 811.78 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7505` | 437.47 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,340.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 106.03 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,200.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 922.07 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,210.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7565` | 1,900.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,590.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 36,710.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,390.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 604.16 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,060.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 6,290.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 4,860.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7675` | 10,680.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 499.99 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7695` | 144,250.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 4,350.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7715` | 3,190.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,490.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 4,570.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7745` | 24,410.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 126.41 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 4,630.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 544.25 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 6,450.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 444.63 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,630.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7835` | 950.23 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7855` | 3,020.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 4,460.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7875` | 6,210.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7895` | 8,660.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,850.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7915` | 1,290.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 8,090.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7935` | 2,220.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7945` | 9,230.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7955` | 23,610.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7965` | 42,350.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7975` | 1,170.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7985` | 643.43 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7995` | 2,580.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8005` | 1,150.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8015` | 86,410.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 421.31 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 26,280.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 15,590.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8105` | 5,190.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,620.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8135` | 11,260.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8155` | 8,360.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8160` | 32,370,000.00 USD | 32,370,000.00 USD | 210,530.00 USD | 62,790.00 USD | 167,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 362.12 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8175` | 103,660.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8180` | 31,930,000.00 USD | 31,930,000.00 USD | 77,750.00 USD | 39,880.00 USD | 43,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 491.10 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8195` | 999.13 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8200` | 31,770,000.00 USD | 31,770,000.00 USD | 205,920.00 USD | 47,330.00 USD | 97,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8215` | 5,180.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 31,420,000.00 USD | 31,420,000.00 USD | 104,090.00 USD | 39,210.00 USD | 93,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 466.85 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8235` | 11,490.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8240` | 31,180,000.00 USD | 31,180,000.00 USD | 97,060.00 USD | 26,160.00 USD | 86,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 3,190.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8255` | 317.82 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8260` | 30,970,000.00 USD | 30,970,000.00 USD | 185,230.00 USD | 28,970.00 USD | 110,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 11,410.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8280` | 30,650,000.00 USD | 30,650,000.00 USD | 113,570.00 USD | 43,870.00 USD | 85,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 118,200.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8295` | 32,530.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8300` | 30,400,000.00 USD | 30,400,000.00 USD | 30,930.00 USD | 41,810.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8305` | 1,670.00 USD | 974,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8320` | 12,540,000.00 USD | 12,540,000.00 USD | 30,010.00 USD | 11,950.00 USD | 9,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 30,290,000.00 USD | 30,290,000.00 USD | 90,830.00 USD | 57,170.00 USD | 60,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8325` | 18,980.00 USD | 972,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8340` | 12,490,000.00 USD | 12,490,000.00 USD | 49,780.00 USD | 16,150.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 30,080,000.00 USD | 30,080,000.00 USD | 105,040.00 USD | 53,420.00 USD | 180,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8345` | 687.79 USD | 953,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8355` | 17,890.00 USD | 952,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 12,380,000.00 USD | 12,380,000.00 USD | 43,570.00 USD | 7,470.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 29,740,000.00 USD | 29,740,000.00 USD | 138,260.00 USD | 17,780.00 USD | 94,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 137.85 USD | 935,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 12,310,000.00 USD | 12,310,000.00 USD | 29,520.00 USD | 7,740.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 29,490,000.00 USD | 29,490,000.00 USD | 69,590.00 USD | 59,380.00 USD | 96,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 79,450.00 USD | 934,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8395` | 27,150.00 USD | 855,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 12,240,000.00 USD | 12,240,000.00 USD | 19,020.00 USD | 19,340.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 29,260,000.00 USD | 29,260,000.00 USD | 76,470.00 USD | 55,720.00 USD | 58,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 1,380.00 USD | 828,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8415` | 2,200.00 USD | 826,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 12,190,000.00 USD | 12,190,000.00 USD | 11,140.00 USD | 15,160.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 29,070,000.00 USD | 29,070,000.00 USD | 70,700.00 USD | 48,060.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 25,310.00 USD | 824,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8435` | 6,280.00 USD | 799,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 12,140,000.00 USD | 12,140,000.00 USD | 22,070.00 USD | 15,080.00 USD | 81.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 28,940,000.00 USD | 28,940,000.00 USD | 34,250.00 USD | 40,470.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 133.18 USD | 793,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8455` | 6,630.00 USD | 792,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 12,100,000.00 USD | 12,100,000.00 USD | 10,030.00 USD | 13,860.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 28,840,000.00 USD | 28,840,000.00 USD | 31,090.00 USD | 33,020.00 USD | 73,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 15,830.00 USD | 786,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8475` | 29,810.00 USD | 770,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 12,050,000.00 USD | 12,050,000.00 USD | 32,420.00 USD | 20,130.00 USD | 49,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 28,700,000.00 USD | 28,700,000.00 USD | 52,580.00 USD | 6,260.00 USD | 34,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,890.00 USD | 740,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8495` | 804.99 USD | 738,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 11,950,000.00 USD | 11,950,000.00 USD | 61,890.00 USD | 7,390.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 28,610,000.00 USD | 28,610,000.00 USD | 32,630.00 USD | 15,300.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 738,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 11,860,000.00 USD | 11,860,000.00 USD | 30,310.00 USD | 27,790.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 28,540,000.00 USD | 28,540,000.00 USD | 77,320.00 USD | 45,980.00 USD | 45,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 4,220.00 USD | 736,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8535` | 11,410.00 USD | 732,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 11,790,000.00 USD | 11,790,000.00 USD | 20,080.00 USD | 11,230.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 28,370,000.00 USD | 28,370,000.00 USD | 92,380.00 USD | 64,630.00 USD | 15,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8545` | 2,030.00 USD | 721,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8555` | 139.53 USD | 719,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 11,720,000.00 USD | 11,720,000.00 USD | 27,930.00 USD | 22,280.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 28,200,000.00 USD | 28,200,000.00 USD | 87,380.00 USD | 45,770.00 USD | 7,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 36,350.00 USD | 718,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 11,640,000.00 USD | 11,640,000.00 USD | 56,290.00 USD | 13,730.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 28,060,000.00 USD | 28,060,000.00 USD | 65,360.00 USD | 21,180.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 14,660.00 USD | 682,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8595` | 7,610.00 USD | 667,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 11,560,000.00 USD | 11,560,000.00 USD | 16,950.00 USD | 6,660.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 27,950,000.00 USD | 27,950,000.00 USD | 38,890.00 USD | 65,420.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 19,020.00 USD | 660,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8615` | 1,090.00 USD | 641,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 11,520,000.00 USD | 11,520,000.00 USD | 6,110.00 USD | 4,970.00 USD | 396.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 27,820,000.00 USD | 27,820,000.00 USD | 25,100.00 USD | 21,240.00 USD | 56,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 9,140.00 USD | 640,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8635` | 5,160.00 USD | 631,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 11,510,000.00 USD | 11,510,000.00 USD | 52,440.00 USD | 25,350.00 USD | 61,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 27,720,000.00 USD | 27,720,000.00 USD | 38,670.00 USD | 27,710.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 2,580.00 USD | 625,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8655` | 1,230.00 USD | 623,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 11,370,000.00 USD | 11,370,000.00 USD | 137,930.00 USD | 1,970.00 USD | 13,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 27,650,000.00 USD | 27,650,000.00 USD | 261,430.00 USD | 35,900.00 USD | 119,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,040.00 USD | 622,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8675` | 13,120.00 USD | 621,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 11,210,000.00 USD | 11,210,000.00 USD | 102,620.00 USD | 60,770.00 USD | 33,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 27,240,000.00 USD | 27,240,000.00 USD | 208,910.00 USD | 100,620.00 USD | 114,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8685` | 289.04 USD | 607,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8695` | 4,920.00 USD | 607,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 11,020,000.00 USD | 11,020,000.00 USD | 109,230.00 USD | 90,980.00 USD | 226,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 26,810,000.00 USD | 26,810,000.00 USD | 377,870.00 USD | 141,350.00 USD | 326,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 14,520.00 USD | 602,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8715` | 2,870.00 USD | 588,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 10,590,000.00 USD | 10,590,000.00 USD | 210,640.00 USD | 63,650.00 USD | 201,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 25,970,000.00 USD | 25,970,000.00 USD | 440,480.00 USD | 149,650.00 USD | 310,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8725` | 29,520.00 USD | 585,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8735` | 129,080.00 USD | 555,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8740` | 10,110,000.00 USD | 10,110,000.00 USD | 43,030.00 USD | 19,920.00 USD | 21,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 25,070,000.00 USD | 25,070,000.00 USD | 566,110.00 USD | 235,670.00 USD | 196,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8745` | 13,880.00 USD | 426,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8755` | 1,420.00 USD | 412,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8760` | 10,030,000.00 USD | 10,030,000.00 USD | 74,790.00 USD | 73,290.00 USD | 139,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 24,070,000.00 USD | 24,070,000.00 USD | 594,350.00 USD | 249,690.00 USD | 486,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 33,510.00 USD | 411,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8775` | 16,030.00 USD | 377,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 9,740,000.00 USD | 9,740,000.00 USD | 64,740.00 USD | 47,450.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 22,740,000.00 USD | 22,740,000.00 USD | 261,940.00 USD | 106,230.00 USD | 202,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8785` | 56,160.00 USD | 361,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8795` | 172,470.00 USD | 305,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 9,600,000.00 USD | 9,600,000.00 USD | 13,090.00 USD | 12,370.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 22,170,000.00 USD | 22,170,000.00 USD | 439,660.00 USD | 120,050.00 USD | 423,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8805` | 1,530.00 USD | 133,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8815` | 8,730.00 USD | 131,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8820` | 9,530,000.00 USD | 9,530,000.00 USD | 108,450.00 USD | 63,480.00 USD | 145,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 21,180,000.00 USD | 21,180,000.00 USD | 562,000.00 USD | 248,320.00 USD | 318,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8825` | 5,300.00 USD | 123,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8835` | 7,220.00 USD | 117,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8840` | 9,210,000.00 USD | 9,210,000.00 USD | 300,890.00 USD | 65,390.00 USD | 152,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 20,050,000.00 USD | 20,050,000.00 USD | 772,470.00 USD | 232,070.00 USD | 537,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 3,550.00 USD | 110,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8855` | 2,660.00 USD | 106,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8860` | 8,690,000.00 USD | 8,690,000.00 USD | 272,520.00 USD | 127,540.00 USD | 90,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 18,510,000.00 USD | 18,510,000.00 USD | 533,450.00 USD | 257,680.00 USD | 262,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8865` | 19,190.00 USD | 104,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8875` | 12,780.00 USD | 85,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8880` | 8,200,000.00 USD | 8,200,000.00 USD | 298,190.00 USD | 211,570.00 USD | 486,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 17,460,000.00 USD | 17,460,000.00 USD | 1,060,000.00 USD | 404,050.00 USD | 990,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8885` | 697.38 USD | 72,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8895` | 3,530.00 USD | 71,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8900` | 7,210,000.00 USD | 7,210,000.00 USD | 515,380.00 USD | 158,940.00 USD | 513,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 15,010,000.00 USD | 15,010,000.00 USD | 1,180,000.00 USD | 483,970.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8905` | 892.28 USD | 892.28 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8915` | 1,100.00 USD | 68,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8920` | 6,020,000.00 USD | 6,020,000.00 USD | 234,530.00 USD | 59,650.00 USD | 100,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 12,340,000.00 USD | 12,340,000.00 USD | 1,550,000.00 USD | 567,000.00 USD | 706,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 1,040.00 USD | 67,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8935` | 20,360.00 USD | 66,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8940` | 5,630,000.00 USD | 5,630,000.00 USD | 176,200.00 USD | 130,550.00 USD | 278,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 9,510,000.00 USD | 9,510,000.00 USD | 1,220,000.00 USD | 602,640.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8945` | 5,750.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8955` | 257.01 USD | 39,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8960` | 5,040,000.00 USD | 5,040,000.00 USD | 134,160.00 USD | 141,360.00 USD | 176,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 6,640,000.00 USD | 6,640,000.00 USD | 657,470.00 USD | 314,840.00 USD | 704,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8965` | 29,550.00 USD | 39,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8975` | 3,540.00 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8980` | 4,590,000.00 USD | 4,590,000.00 USD | 128,530.00 USD | 69,170.00 USD | 103,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 4,960,000.00 USD | 4,960,000.00 USD | 656,780.00 USD | 284,000.00 USD | 169,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 320.05 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8995` | 143.92 USD | 6,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9000` | 4,290,000.00 USD | 4,290,000.00 USD | 53,800.00 USD | 24,210.00 USD | 40,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 3,850,000.00 USD | 3,850,000.00 USD | 127,760.00 USD | 33,800.00 USD | 1,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 4,170,000.00 USD | 4,170,000.00 USD | 49,680.00 USD | 67,410.00 USD | 190,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 3,690,000.00 USD | 3,690,000.00 USD | 8,440.00 USD | 52,590.00 USD | 123,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 3,860,000.00 USD | 3,860,000.00 USD | 128,110.00 USD | 81,940.00 USD | 142,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 3,500,000.00 USD | 3,500,000.00 USD | 98,990.00 USD | 0.00 USD | 71,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 119.44 USD | 6,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9060` | 3,510,000.00 USD | 3,510,000.00 USD | 215,300.00 USD | 10,170.00 USD | 60,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9060` | 3,330,000.00 USD | 3,330,000.00 USD | 245,950.00 USD | 0.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9075` | 5,960.00 USD | 5,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.9080` | 3,220,000.00 USD | 3,220,000.00 USD | 305,430.00 USD | 116,800.00 USD | 213,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9080` | 3,080,000.00 USD | 3,080,000.00 USD | 175,380.00 USD | 19,890.00 USD | 165,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 2,590,000.00 USD | 2,590,000.00 USD | 225,400.00 USD | 58,970.00 USD | 153,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9100` | 2,720,000.00 USD | 2,720,000.00 USD | 123,910.00 USD | 91,580.00 USD | 126,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 2,150,000.00 USD | 2,150,000.00 USD | 228,280.00 USD | 39,820.00 USD | 204,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9120` | 2,380,000.00 USD | 2,380,000.00 USD | 88,860.00 USD | 51,920.00 USD | 105,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 1,680,000.00 USD | 1,680,000.00 USD | 172,190.00 USD | 87,890.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 2,140,000.00 USD | 2,140,000.00 USD | 143,540.00 USD | 58,200.00 USD | 61,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 1,310,000.00 USD | 1,310,000.00 USD | 74,950.00 USD | 50,090.00 USD | 65,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9160` | 1,870,000.00 USD | 1,870,000.00 USD | 171,920.00 USD | 26,360.00 USD | 136,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 1,120,000.00 USD | 1,120,000.00 USD | 154,870.00 USD | 9,020.00 USD | 46,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9180` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 905,830.00 USD | 905,830.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 1,510,000.00 USD | 1,510,000.00 USD | 386,820.00 USD | 16,660.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 899,650.00 USD | 899,650.00 USD | 32,990.00 USD | 39,420.00 USD | 133,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 64,540.00 USD | 156,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 693,870.00 USD | 693,870.00 USD | 170,280.00 USD | 58,320.00 USD | 150,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 826,040.00 USD | 826,040.00 USD | 104,080.00 USD | 41,710.00 USD | 184,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 315,220.00 USD | 315,220.00 USD | 63,790.00 USD | 28,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 495,770.00 USD | 495,770.00 USD | 102,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 223,060.00 USD | 223,060.00 USD | 0.00 USD | 44,480.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 393,760.00 USD | 393,760.00 USD | 107,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 166,780.00 USD | 166,780.00 USD | 0.00 USD | 0.00 USD | 166,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9300` | 285,830.00 USD | 285,830.00 USD | 177,720.00 USD | 108,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 114,380.00 USD | 114,380.00 USD | 100,660.00 USD | 0.00 USD | 13,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 144,850.00 USD | 144,850.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9340` | 102,880.00 USD | 102,880.00 USD | 50,160.00 USD | 52,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 251,630.00 USD | 251,630.00 USD | 0.00 USD | 33,250.00 USD | 73,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9360` | 225,690.00 USD | 225,690.00 USD | 122,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 910,080.00 USD | 910,080.00 USD | 246,090.00 USD | 118,850.00 USD | 293,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9380` | 571,410.00 USD | 571,410.00 USD | 168,030.00 USD | 0.00 USD | 177,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 1,030,000.00 USD | 1,030,000.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 899,020.00 USD | 899,020.00 USD | 166,670.00 USD | 33,320.00 USD | 127,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 919,880.00 USD | 919,880.00 USD | 0.00 USD | 20,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 216,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 1,390,000.00 USD | 1,390,000.00 USD | 56,940.00 USD | 28,980.00 USD | 160,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 1,460,000.00 USD | 1,460,000.00 USD | 50,850.00 USD | 26,450.00 USD | 99.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 208,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 1,520,000.00 USD | 1,520,000.00 USD | 17,970.00 USD | 6,400.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 371,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 1,660,000.00 USD | 1,660,000.00 USD | 37,450.00 USD | 17,280.00 USD | 86,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 62,510.00 USD | 329,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 1,850,000.00 USD | 1,850,000.00 USD | 62,990.00 USD | 66,810.00 USD | 55,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 2,380,000.00 USD | 2,380,000.00 USD | 10,500.00 USD | 2,560.00 USD | 60,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 33,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 2,450,000.00 USD | 2,450,000.00 USD | 72,330.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 1,920,000.00 USD | 1,920,000.00 USD | 689.00 USD | 43,140.00 USD | 159.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 3,300,000.00 USD | 3,300,000.00 USD | 846,080.00 USD | 0.00 USD | 511.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 2,210,000.00 USD | 2,210,000.00 USD | 110,240.00 USD | 65,470.00 USD | 108,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 3,860,000.00 USD | 3,860,000.00 USD | 356,870.00 USD | 73,200.00 USD | 131,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 3,020,000.00 USD | 3,020,000.00 USD | 385,380.00 USD | 135,810.00 USD | 290,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 5,420,000.00 USD | 5,420,000.00 USD | 741,340.00 USD | 231,300.00 USD | 588,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 3,690,000.00 USD | 3,690,000.00 USD | 338,870.00 USD | 116,210.00 USD | 217,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 6,990,000.00 USD | 6,990,000.00 USD | 693,720.00 USD | 366,520.00 USD | 508,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 4,240,000.00 USD | 4,240,000.00 USD | 274,510.00 USD | 140,370.00 USD | 130,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 8,750,000.00 USD | 8,750,000.00 USD | 1,020,000.00 USD | 191,600.00 USD | 548,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 4,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9680` | 5,030,000.00 USD | 5,030,000.00 USD | 310,700.00 USD | 118,860.00 USD | 362,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 10,910,000.00 USD | 10,910,000.00 USD | 911,470.00 USD | 631,050.00 USD | 614,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 5,620,000.00 USD | 5,620,000.00 USD | 250,300.00 USD | 142,870.00 USD | 193,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 12,330,000.00 USD | 12,330,000.00 USD | 694,250.00 USD | 344,900.00 USD | 381,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 69,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9720` | 6,200,000.00 USD | 6,200,000.00 USD | 334,210.00 USD | 127,200.00 USD | 126,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 13,050,000.00 USD | 13,050,000.00 USD | 398,310.00 USD | 184,170.00 USD | 138,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 6,440,000.00 USD | 6,440,000.00 USD | 167,080.00 USD | 29,860.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 13,600,000.00 USD | 13,600,000.00 USD | 309,060.00 USD | 116,990.00 USD | 124,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 6,600,000.00 USD | 6,600,000.00 USD | 29,860.00 USD | 41,140.00 USD | 87,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 14,290,000.00 USD | 14,290,000.00 USD | 182,900.00 USD | 286,070.00 USD | 216,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9765` | 214.44 USD | 69,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9780` | 6,850,000.00 USD | 6,850,000.00 USD | 85,910.00 USD | 32,630.00 USD | 129,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 15,440,000.00 USD | 15,440,000.00 USD | 441,770.00 USD | 196,630.00 USD | 512,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 7,180,000.00 USD | 7,180,000.00 USD | 101,910.00 USD | 72,820.00 USD | 157,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 16,070,000.00 USD | 16,070,000.00 USD | 341,810.00 USD | 87,560.00 USD | 204,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 15,580.00 USD | 84,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9820` | 7,450,000.00 USD | 7,450,000.00 USD | 184,070.00 USD | 32,930.00 USD | 53,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 16,380,000.00 USD | 16,380,000.00 USD | 108,220.00 USD | 52,160.00 USD | 142,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 7,620,000.00 USD | 7,620,000.00 USD | 79,960.00 USD | 66,570.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 17,070,000.00 USD | 17,070,000.00 USD | 395,810.00 USD | 123,000.00 USD | 177,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9845` | 6,080.00 USD | 90,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9860` | 7,950,000.00 USD | 7,950,000.00 USD | 128,950.00 USD | 60,420.00 USD | 136,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 17,410,000.00 USD | 17,410,000.00 USD | 107,440.00 USD | 154,250.00 USD | 73,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 731.29 USD | 91,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9875` | 54,600.00 USD | 146,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 8,140,000.00 USD | 8,140,000.00 USD | 85,110.00 USD | 35,320.00 USD | 70,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 17,710,000.00 USD | 17,710,000.00 USD | 209,770.00 USD | 64,380.00 USD | 26,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,930.00 USD | 151,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9895` | 5,760.00 USD | 157,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9900` | 8,410,000.00 USD | 8,410,000.00 USD | 144,770.00 USD | 50,640.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 18,020,000.00 USD | 18,020,000.00 USD | 201,410.00 USD | 100,430.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 20,050.00 USD | 177,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9920` | 8,620,000.00 USD | 8,620,000.00 USD | 142,180.00 USD | 46,030.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 18,470,000.00 USD | 18,470,000.00 USD | 288,210.00 USD | 79,650.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,420.00 USD | 179,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9940` | 8,780,000.00 USD | 8,780,000.00 USD | 59,940.00 USD | 36,960.00 USD | 59,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 18,940,000.00 USD | 18,940,000.00 USD | 143,340.00 USD | 183,310.00 USD | 146,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9945` | 6,430.00 USD | 185,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9960` | 8,820,000.00 USD | 8,820,000.00 USD | 6,270.00 USD | 11,390.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 19,400,000.00 USD | 19,400,000.00 USD | 107,780.00 USD | 55,790.00 USD | 291,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9965` | 4,780.00 USD | 190,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9980` | 9,140,000.00 USD | 9,140,000.00 USD | 138,880.00 USD | 32,380.00 USD | 145,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 19,840,000.00 USD | 19,840,000.00 USD | 238,490.00 USD | 42,080.00 USD | 163,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,180,000.00 USD | 9,180,000.00 USD | 18,790.00 USD | 17,140.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 20,050,000.00 USD | 20,050,000.00 USD | 94,210.00 USD | 53,610.00 USD | 65,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,230,000.00 USD | 9,230,000.00 USD | 11,220.00 USD | 18,430.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 20,640,000.00 USD | 20,640,000.00 USD | 276,050.00 USD | 51,850.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 9,280,000.00 USD | 9,280,000.00 USD | 17,620.00 USD | 13,280.00 USD | 22,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 21,070,000.00 USD | 21,070,000.00 USD | 219,820.00 USD | 45,420.00 USD | 165,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 449.11 USD | 191,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,310,000.00 USD | 9,310,000.00 USD | 9,900.00 USD | 14,230.00 USD | 9,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 21,330,000.00 USD | 21,330,000.00 USD | 181,560.00 USD | 14,150.00 USD | 68,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,360,000.00 USD | 9,360,000.00 USD | 19,520.00 USD | 9,720.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 21,930,000.00 USD | 21,930,000.00 USD | 274,240.00 USD | 66,150.00 USD | 253,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,380,000.00 USD | 9,380,000.00 USD | 13,150.00 USD | 5,570.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 22,580,000.00 USD | 22,580,000.00 USD | 311,680.00 USD | 74,250.00 USD | 271,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,450,000.00 USD | 9,450,000.00 USD | 21,660.00 USD | 13,820.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 23,640,000.00 USD | 23,640,000.00 USD | 385,660.00 USD | 248,790.00 USD | 419,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 9,510,000.00 USD | 9,510,000.00 USD | 13,360.00 USD | 11,680.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 24,370,000.00 USD | 24,370,000.00 USD | 341,120.00 USD | 208,060.00 USD | 178,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 191,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,550,000.00 USD | 9,550,000.00 USD | 23,240.00 USD | 11,060.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 25,280,000.00 USD | 25,280,000.00 USD | 402,200.00 USD | 101,810.00 USD | 413,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,570,000.00 USD | 9,570,000.00 USD | 18,720.00 USD | 4,090.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 25,960,000.00 USD | 25,960,000.00 USD | 297,940.00 USD | 28,880.00 USD | 346,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,660,000.00 USD | 9,660,000.00 USD | 32,190.00 USD | 13,020.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 26,640,000.00 USD | 26,640,000.00 USD | 214,170.00 USD | 110,730.00 USD | 353,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,730,000.00 USD | 9,730,000.00 USD | 45,050.00 USD | 7,770.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 27,030,000.00 USD | 27,030,000.00 USD | 208,130.00 USD | 42,850.00 USD | 140,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 9,800,000.00 USD | 9,800,000.00 USD | 29,960.00 USD | 7,740.00 USD | 28,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 27,280,000.00 USD | 27,280,000.00 USD | 97,520.00 USD | 61,990.00 USD | 96,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,850,000.00 USD | 9,850,000.00 USD | 17,840.00 USD | 16,400.00 USD | 18,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 27,690,000.00 USD | 27,690,000.00 USD | 187,390.00 USD | 56,910.00 USD | 158,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,870,000.00 USD | 9,870,000.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 27,780,000.00 USD | 27,780,000.00 USD | 41,560.00 USD | 32,180.00 USD | 17,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 463,280.00 USD | 654,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,900,000.00 USD | 9,900,000.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 28,030,000.00 USD | 28,030,000.00 USD | 119,530.00 USD | 47,560.00 USD | 90,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 3,190.00 USD | 657,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,930,000.00 USD | 9,930,000.00 USD | 20,340.00 USD | 11,130.00 USD | 0.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 28,500,000.00 USD | 28,500,000.00 USD | 147,960.00 USD | 125,610.00 USD | 193,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 9,970,000.00 USD | 9,970,000.00 USD | 7,200.00 USD | 11,970.00 USD | 24,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 28,890,000.00 USD | 28,890,000.00 USD | 166,990.00 USD | 102,410.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,070,000.00 USD | 10,070,000.00 USD | 26,990.00 USD | 18,830.00 USD | 49,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,280,000.00 USD | 29,280,000.00 USD | 184,730.00 USD | 21,870.00 USD | 182,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,150,000.00 USD | 10,150,000.00 USD | 59,260.00 USD | 7,020.00 USD | 15,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,630,000.00 USD | 29,630,000.00 USD | 147,100.00 USD | 27,060.00 USD | 173,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 10,400.00 USD | 668,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,170,000.00 USD | 10,170,000.00 USD | 8,210.00 USD | 7,840.00 USD | 8,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,840,000.00 USD | 29,840,000.00 USD | 74,160.00 USD | 58,400.00 USD | 87,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 668,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,220,000.00 USD | 10,220,000.00 USD | 21,580.00 USD | 18,300.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 29,940,000.00 USD | 29,940,000.00 USD | 53,240.00 USD | 12,870.00 USD | 29,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,290,000.00 USD | 10,290,000.00 USD | 19,660.00 USD | 8,720.00 USD | 41,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 30,100,000.00 USD | 30,100,000.00 USD | 78,480.00 USD | 65,330.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 10,320,000.00 USD | 10,320,000.00 USD | 6,590.00 USD | 7,020.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,200,000.00 USD | 30,200,000.00 USD | 74,370.00 USD | 30,010.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,280,000.00 USD | 30,280,000.00 USD | 50,260.00 USD | 12,520.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,290,000.00 USD | 30,290,000.00 USD | 1,420.00 USD | 3,180.00 USD | 608.24 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 668,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 671,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,380,000.00 USD | 30,380,000.00 USD | 24,860.00 USD | 46,330.00 USD | 21,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,330.00 USD | 672,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 672,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 30,450,000.00 USD | 30,450,000.00 USD | 8,480.00 USD | 2,340.00 USD | 53,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 328.69 USD | 673,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,460,000.00 USD | 30,460,000.00 USD | 6,690.00 USD | 5,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,470,000.00 USD | 30,470,000.00 USD | 3,120.00 USD | 3,350.00 USD | 257.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,500,000.00 USD | 30,500,000.00 USD | 15,370.00 USD | 3,080.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,500,000.00 USD | 30,500,000.00 USD | 4,660.00 USD | 786.13 USD | 265.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 30,510,000.00 USD | 30,510,000.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.07` | 116.04 USD | 673,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 1,150.00 USD | 674,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 5,700.00 USD | 680,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 683,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,120.00 USD | 686,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 166.43 USD | 687,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 1,110.00 USD | 688,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 693,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 694,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 694,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 717,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 1,450.00 USD | 719,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 253.69 USD | 719,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 29,760.00 USD | 749,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 147.43 USD | 749,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 2,880.00 USD | 752,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 756,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 9,290.00 USD | 765,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 5,270.00 USD | 771,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 771,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 137.21 USD | 771,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 213,830.00 USD | 985,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 988,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.27` | 2,090.00 USD | 990,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 358.30 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,520.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 260.65 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 1,200.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.46` | 9,490.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 143.91 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 4,820.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 1,090.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 1,360.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 24,350.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 2,580,000.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 17,720.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 287.38 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 122.73 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 9,710.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 9,400.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 39,240.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 291,760.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 84,990.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 781.77 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 952.52 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 2,470.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 14,230.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 203.88 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 943.75 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 190.35 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1895` | 5,350,000.00 USD | 0.00 USD | 189.50 USD | `-79.66%` | `1,000.00` |
| `Live` | `Long` | `0.1945` | 5,350,000.00 USD | 0.00 USD | 16,750.00 USD | `-79.12%` | `86,117.40` |
| `Live` | `Long` | `0.1995` | 5,340,000.00 USD | 0.00 USD | 2,280.00 USD | `-78.59%` | `11,435.30` |
| `Live` | `Long` | `0.2195` | 5,330,000.00 USD | 0.00 USD | 7,080.00 USD | `-76.44%` | `32,244.50` |
| `Live` | `Long` | `0.2215` | 5,330,000.00 USD | 0.00 USD | 143.84 USD | `-76.22%` | `649.40` |
| `Live` | `Long` | `0.2355` | 5,330,000.00 USD | 0.00 USD | 789.66 USD | `-74.72%` | `3,353.10` |
| `Live` | `Long` | `0.2365` | 5,330,000.00 USD | 0.00 USD | 307.45 USD | `-74.61%` | `1,300.00` |
| `Live` | `Long` | `0.2385` | 5,330,000.00 USD | 0.00 USD | 156.36 USD | `-74.40%` | `655.60` |
| `Live` | `Long` | `0.2525` | 5,330,000.00 USD | 0.00 USD | 2,250.00 USD | `-72.90%` | `8,897.00` |
| `Live` | `Long` | `0.2585` | 5,320,000.00 USD | 0.00 USD | 2,270.00 USD | `-72.25%` | `8,782.90` |
| `Live` | `Long` | `0.2605` | 5,320,000.00 USD | 0.00 USD | 220.85 USD | `-72.04%` | `847.80` |
| `Live` | `Long` | `0.2655` | 5,320,000.00 USD | 0.00 USD | 20,630.00 USD | `-71.50%` | `77,706.40` |
| `Live` | `Long` | `0.2685` | 5,300,000.00 USD | 0.00 USD | 106.16 USD | `-71.18%` | `395.40` |
| `Live` | `Long` | `0.2735` | 5,300,000.00 USD | 0.00 USD | 248.34 USD | `-70.64%` | `908.00` |
| `Live` | `Long` | `0.2745` | 5,300,000.00 USD | 0.00 USD | 1,920.00 USD | `-70.53%` | `7,000.00` |
| `Live` | `Long` | `0.2835` | 5,300,000.00 USD | 0.00 USD | 2,800.00 USD | `-69.57%` | `9,865.70` |
| `Live` | `Long` | `0.2845` | 5,300,000.00 USD | 0.00 USD | 299.32 USD | `-69.46%` | `1,052.10` |
| `Live` | `Long` | `0.2885` | 5,300,000.00 USD | 0.00 USD | 29,070.00 USD | `-69.03%` | `100,768.40` |
| `Live` | `Long` | `0.2945` | 5,270,000.00 USD | 0.00 USD | 687.92 USD | `-68.39%` | `2,335.90` |
| `Live` | `Long` | `0.2975` | 5,270,000.00 USD | 0.00 USD | 4,330.00 USD | `-68.07%` | `14,561.30` |
| `Live` | `Long` | `0.3025` | 5,260,000.00 USD | 0.00 USD | 3,020.00 USD | `-67.53%` | `10,000.00` |
| `Live` | `Long` | `0.3115` | 5,260,000.00 USD | 0.00 USD | 7,730.00 USD | `-66.56%` | `24,806.30` |
| `Live` | `Long` | `0.3275` | 5,250,000.00 USD | 0.00 USD | 8,450.00 USD | `-64.85%` | `25,791.20` |
| `Live` | `Long` | `0.3325` | 5,240,000.00 USD | 0.00 USD | 370.77 USD | `-64.31%` | `1,115.10` |
| `Live` | `Long` | `0.3335` | 5,240,000.00 USD | 0.00 USD | 163.58 USD | `-64.20%` | `490.50` |
| `Live` | `Long` | `0.3415` | 5,240,000.00 USD | 0.00 USD | 666.92 USD | `-63.34%` | `1,952.90` |
| `Live` | `Long` | `0.3505` | 5,240,000.00 USD | 0.00 USD | 1,780.00 USD | `-62.38%` | `5,073.30` |
| `Live` | `Long` | `0.3585` | 5,240,000.00 USD | 0.00 USD | 1,230.00 USD | `-61.52%` | `3,423.70` |
| `Live` | `Long` | `0.3605` | 5,240,000.00 USD | 0.00 USD | 225.31 USD | `-61.30%` | `625.00` |
| `Live` | `Long` | `0.3665` | 5,240,000.00 USD | 0.00 USD | 274.88 USD | `-60.66%` | `750.00` |
| `Live` | `Long` | `0.3775` | 5,240,000.00 USD | 0.00 USD | 6,420.00 USD | `-59.48%` | `17,000.00` |
| `Live` | `Long` | `0.3795` | 5,230,000.00 USD | 0.00 USD | 278.02 USD | `-59.26%` | `732.60` |
| `Live` | `Long` | `0.3835` | 5,230,000.00 USD | 0.00 USD | 26,840.00 USD | `-58.83%` | `70,000.00` |
| `Live` | `Long` | `0.3845` | 5,200,000.00 USD | 0.00 USD | 1,750.00 USD | `-58.73%` | `4,562.20` |
| `Live` | `Long` | `0.3895` | 5,200,000.00 USD | 0.00 USD | 2,980.00 USD | `-58.19%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 5,200,000.00 USD | 0.00 USD | 5,030.00 USD | `-57.87%` | `12,808.60` |
| `Live` | `Long` | `0.4035` | 5,190,000.00 USD | 0.00 USD | 935.03 USD | `-56.69%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 5,190,000.00 USD | 0.00 USD | 5,800.00 USD | `-56.58%` | `14,340.50` |
| `Live` | `Long` | `0.4205` | 5,190,000.00 USD | 0.00 USD | 260.08 USD | `-54.86%` | `618.50` |
| `Live` | `Long` | `0.4235` | 5,190,000.00 USD | 0.00 USD | 467.50 USD | `-54.54%` | `1,103.90` |
| `Live` | `Long` | `0.4365` | 5,190,000.00 USD | 0.00 USD | 502.11 USD | `-53.15%` | `1,150.30` |
| `Live` | `Long` | `0.4375` | 5,190,000.00 USD | 0.00 USD | 43,580.00 USD | `-53.04%` | `99,611.70` |
| `Live` | `Long` | `0.4385` | 5,140,000.00 USD | 0.00 USD | 122.91 USD | `-52.93%` | `280.30` |
| `Live` | `Long` | `0.4405` | 5,140,000.00 USD | 0.00 USD | 1,830.00 USD | `-52.72%` | `4,149.40` |
| `Live` | `Long` | `0.4415` | 5,140,000.00 USD | 0.00 USD | 5,800.00 USD | `-52.61%` | `13,146.20` |
| `Live` | `Long` | `0.4435` | 5,130,000.00 USD | 0.00 USD | 219.00 USD | `-52.39%` | `493.80` |
| `Live` | `Long` | `0.4445` | 5,130,000.00 USD | 0.00 USD | 573.54 USD | `-52.29%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 5,130,000.00 USD | 0.00 USD | 19,600.00 USD | `-52.07%` | `43,906.00` |
| `Live` | `Long` | `0.4535` | 5,110,000.00 USD | 0.00 USD | 702.74 USD | `-51.32%` | `1,549.60` |
| `Live` | `Long` | `0.4595` | 5,110,000.00 USD | 0.00 USD | 295.78 USD | `-50.68%` | `643.70` |
| `Live` | `Long` | `0.4605` | 5,110,000.00 USD | 0.00 USD | 80,590.00 USD | `-50.57%` | `175,000.00` |
| `Live` | `Long` | `0.4655` | 5,030,000.00 USD | 0.00 USD | 811.65 USD | `-50.03%` | `1,743.60` |
| `Live` | `Long` | `0.4685` | 5,030,000.00 USD | 0.00 USD | 6,350.00 USD | `-49.71%` | `13,552.00` |
| `Live` | `Long` | `0.4705` | 5,030,000.00 USD | 0.00 USD | 5,310.00 USD | `-49.50%` | `11,290.30` |
| `Live` | `Long` | `0.4715` | 5,020,000.00 USD | 0.00 USD | 246.88 USD | `-49.39%` | `523.60` |
| `Live` | `Long` | `0.4735` | 5,020,000.00 USD | 0.00 USD | 1,220.00 USD | `-49.17%` | `2,584.80` |
| `Live` | `Long` | `0.4785` | 5,020,000.00 USD | 0.00 USD | 110.10 USD | `-48.64%` | `230.10` |
| `Live` | `Long` | `0.4835` | 5,020,000.00 USD | 0.00 USD | 174.01 USD | `-48.10%` | `359.90` |
| `Live` | `Long` | `0.4865` | 5,020,000.00 USD | 0.00 USD | 201.07 USD | `-47.78%` | `413.30` |
| `Live` | `Long` | `0.4875` | 5,020,000.00 USD | 0.00 USD | 12,080.00 USD | `-47.67%` | `24,770.70` |
| `Live` | `Long` | `0.4885` | 5,010,000.00 USD | 0.00 USD | 1,190.00 USD | `-47.56%` | `2,426.10` |
| `Live` | `Long` | `0.4895` | 5,010,000.00 USD | 0.00 USD | 105.34 USD | `-47.46%` | `215.20` |
| `Live` | `Long` | `0.4915` | 5,010,000.00 USD | 0.00 USD | 2,380.00 USD | `-47.24%` | `4,848.70` |
| `Live` | `Long` | `0.4945` | 5,000,000.00 USD | 0.00 USD | 106.32 USD | `-46.92%` | `215.00` |
| `Live` | `Long` | `0.4955` | 5,000,000.00 USD | 0.00 USD | 3,120.00 USD | `-46.81%` | `6,305.00` |
| `Live` | `Long` | `0.4965` | 5,000,000.00 USD | 0.00 USD | 496.50 USD | `-46.71%` | `1,000.00` |
| `Live` | `Long` | `0.4975` | 5,000,000.00 USD | 0.00 USD | 3,330.00 USD | `-46.60%` | `6,701.80` |
| `Live` | `Long` | `0.4985` | 5,000,000.00 USD | 0.00 USD | 216.75 USD | `-46.49%` | `434.80` |
| `Live` | `Long` | `0.5005` | 5,000,000.00 USD | 0.00 USD | 5,410.00 USD | `-46.28%` | `10,805.30` |
| `Live` | `Long` | `0.5015` | 4,990,000.00 USD | 0.00 USD | 212.49 USD | `-46.17%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,990,000.00 USD | 0.00 USD | 1,230.00 USD | `-46.06%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 4,990,000.00 USD | 0.00 USD | 487.76 USD | `-45.74%` | `964.90` |
| `Live` | `Long` | `0.5065` | 4,990,000.00 USD | 0.00 USD | 258.21 USD | `-45.63%` | `509.80` |
| `Live` | `Long` | `0.5085` | 4,990,000.00 USD | 0.00 USD | 2,030.00 USD | `-45.42%` | `4,000.00` |
| `Live` | `Long` | `0.5095` | 4,990,000.00 USD | 0.00 USD | 1,040.00 USD | `-45.31%` | `2,044.40` |
| `Live` | `Long` | `0.5105` | 4,980,000.00 USD | 0.00 USD | 35,730.00 USD | `-45.20%` | `70,000.00` |
| `Live` | `Long` | `0.5125` | 4,950,000.00 USD | 0.00 USD | 1,620.00 USD | `-44.99%` | `3,166.20` |
| `Live` | `Long` | `0.5145` | 4,950,000.00 USD | 0.00 USD | 276.39 USD | `-44.77%` | `537.20` |
| `Live` | `Long` | `0.5155` | 4,950,000.00 USD | 0.00 USD | 1,240.00 USD | `-44.67%` | `2,409.50` |
| `Live` | `Long` | `0.5165` | 4,950,000.00 USD | 0.00 USD | 619.80 USD | `-44.56%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,950,000.00 USD | 0.00 USD | 213.68 USD | `-44.45%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,950,000.00 USD | 0.00 USD | 121.74 USD | `-44.34%` | `234.80` |
| `Live` | `Long` | `0.5195` | 4,940,000.00 USD | 0.00 USD | 2,340.00 USD | `-44.24%` | `4,500.00` |
| `Live` | `Long` | `0.5205` | 4,940,000.00 USD | 0.00 USD | 422.33 USD | `-44.13%` | `811.40` |
| `Live` | `Long` | `0.5225` | 4,940,000.00 USD | 0.00 USD | 244.90 USD | `-43.91%` | `468.70` |
| `Live` | `Long` | `0.5245` | 4,940,000.00 USD | 0.00 USD | 5,280.00 USD | `-43.70%` | `10,075.20` |
| `Live` | `Long` | `0.5275` | 4,940,000.00 USD | 0.00 USD | 348.36 USD | `-43.38%` | `660.40` |
| `Live` | `Long` | `0.5285` | 4,940,000.00 USD | 0.00 USD | 125,730.00 USD | `-43.27%` | `237,897.40` |
| `Live` | `Long` | `0.5295` | 4,810,000.00 USD | 0.00 USD | 264.06 USD | `-43.16%` | `498.70` |
| `Live` | `Long` | `0.5325` | 4,810,000.00 USD | 0.00 USD | 2,680.00 USD | `-42.84%` | `5,038.10` |
| `Live` | `Long` | `0.5335` | 4,810,000.00 USD | 0.00 USD | 5,800.00 USD | `-42.73%` | `10,862.70` |
| `Live` | `Long` | `0.5345` | 4,800,000.00 USD | 0.00 USD | 417.12 USD | `-42.63%` | `780.40` |
| `Live` | `Long` | `0.5375` | 4,800,000.00 USD | 0.00 USD | 1,190.00 USD | `-42.30%` | `2,206.50` |
| `Live` | `Long` | `0.5395` | 4,800,000.00 USD | 0.00 USD | 319.98 USD | `-42.09%` | `593.10` |
| `Live` | `Long` | `0.5405` | 4,800,000.00 USD | 0.00 USD | 7,090.00 USD | `-41.98%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,790,000.00 USD | 0.00 USD | 269.13 USD | `-41.77%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,790,000.00 USD | 0.00 USD | 230.32 USD | `-41.55%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,790,000.00 USD | 0.00 USD | 272.87 USD | `-41.34%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,790,000.00 USD | 0.00 USD | 1,240.00 USD | `-41.23%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,790,000.00 USD | 0.00 USD | 28,790.00 USD | `-41.02%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,760,000.00 USD | 0.00 USD | 248.06 USD | `-40.91%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,760,000.00 USD | 0.00 USD | 1,570.00 USD | `-40.80%` | `2,851.60` |
| `Live` | `Long` | `0.5525` | 4,760,000.00 USD | 0.00 USD | 8,650.00 USD | `-40.69%` | `15,658.30` |
| `Live` | `Long` | `0.5535` | 4,750,000.00 USD | 0.00 USD | 271.88 USD | `-40.59%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,750,000.00 USD | 0.00 USD | 531.60 USD | `-40.48%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,750,000.00 USD | 0.00 USD | 7,950.00 USD | `-40.37%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,740,000.00 USD | 0.00 USD | 141.97 USD | `-40.05%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,740,000.00 USD | 0.00 USD | 304.93 USD | `-39.94%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,740,000.00 USD | 0.00 USD | 441.84 USD | `-39.84%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,740,000.00 USD | 0.00 USD | 330.53 USD | `-39.62%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,740,000.00 USD | 0.00 USD | 195.93 USD | `-39.51%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,740,000.00 USD | 0.00 USD | 8,190.00 USD | `-39.30%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,730,000.00 USD | 0.00 USD | 570.01 USD | `-39.19%` | `1,006.20` |
| `Live` | `Long` | `0.5675` | 4,730,000.00 USD | 0.00 USD | 1,560.00 USD | `-39.08%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,730,000.00 USD | 0.00 USD | 973.22 USD | `-38.87%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,730,000.00 USD | 0.00 USD | 139.23 USD | `-38.55%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,730,000.00 USD | 0.00 USD | 182.72 USD | `-38.44%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,730,000.00 USD | 0.00 USD | 144.03 USD | `-38.33%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,730,000.00 USD | 0.00 USD | 1,010.00 USD | `-38.23%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,730,000.00 USD | 0.00 USD | 1,150.00 USD | `-38.12%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,730,000.00 USD | 0.00 USD | 497.75 USD | `-38.01%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,730,000.00 USD | 0.00 USD | 227.41 USD | `-37.90%` | `393.10` |
| `Live` | `Long` | `0.5795` | 4,730,000.00 USD | 0.00 USD | 104.60 USD | `-37.80%` | `180.50` |
| `Live` | `Long` | `0.5805` | 4,730,000.00 USD | 0.00 USD | 1,410.00 USD | `-37.69%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,730,000.00 USD | 0.00 USD | 6,470.00 USD | `-37.47%` | `11,099.00` |
| `Live` | `Long` | `0.5855` | 4,720,000.00 USD | 0.00 USD | 2,640.00 USD | `-37.15%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,720,000.00 USD | 0.00 USD | 466.85 USD | `-37.04%` | `796.00` |
| `Live` | `Long` | `0.5875` | 4,720,000.00 USD | 0.00 USD | 969.32 USD | `-36.94%` | `1,649.90` |
| `Live` | `Long` | `0.5885` | 4,710,000.00 USD | 0.00 USD | 311.14 USD | `-36.83%` | `528.70` |
| `Live` | `Long` | `0.5925` | 4,710,000.00 USD | 0.00 USD | 297,240.00 USD | `-36.40%` | `501,677.90` |
| `Live` | `Long` | `0.5935` | 4,420,000.00 USD | 0.00 USD | 132.41 USD | `-36.29%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,420,000.00 USD | 0.00 USD | 8,220.00 USD | `-36.19%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,410,000.00 USD | 0.00 USD | 5,540.00 USD | `-35.97%` | `9,295.80` |
| `Live` | `Long` | `0.5995` | 4,400,000.00 USD | 0.00 USD | 151.97 USD | `-35.65%` | `253.50` |
| `Live` | `Long` | `0.6005` | 4,400,000.00 USD | 0.00 USD | 351.11 USD | `-35.54%` | `584.70` |
| `Live` | `Long` | `0.6015` | 4,400,000.00 USD | 0.00 USD | 12,030.00 USD | `-35.43%` | `20,000.00` |
| `Live` | `Long` | `0.6025` | 4,390,000.00 USD | 0.00 USD | 432.35 USD | `-35.33%` | `717.60` |
| `Live` | `Long` | `0.6035` | 4,390,000.00 USD | 0.00 USD | 181.05 USD | `-35.22%` | `300.00` |
| `Live` | `Long` | `0.6075` | 4,390,000.00 USD | 0.00 USD | 851.05 USD | `-34.79%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,390,000.00 USD | 0.00 USD | 272.24 USD | `-34.68%` | `447.40` |
| `Live` | `Long` | `0.6115` | 4,390,000.00 USD | 0.00 USD | 55,600.00 USD | `-34.36%` | `90,926.50` |
| `Live` | `Long` | `0.6125` | 4,330,000.00 USD | 0.00 USD | 213.64 USD | `-34.25%` | `348.80` |
| `Live` | `Long` | `0.6135` | 4,330,000.00 USD | 0.00 USD | 245.40 USD | `-34.15%` | `400.00` |
| `Live` | `Long` | `0.6155` | 4,330,000.00 USD | 0.00 USD | 935.13 USD | `-33.93%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 4,330,000.00 USD | 0.00 USD | 40,760.00 USD | `-33.82%` | `66,114.40` |
| `Live` | `Long` | `0.6175` | 4,290,000.00 USD | 0.00 USD | 1,540.00 USD | `-33.72%` | `2,500.00` |
| `Live` | `Long` | `0.6185` | 4,290,000.00 USD | 0.00 USD | 4,400.00 USD | `-33.61%` | `7,107.00` |
| `Live` | `Long` | `0.6235` | 4,290,000.00 USD | 0.00 USD | 1,140.00 USD | `-33.07%` | `1,827.00` |
| `Live` | `Long` | `0.6245` | 4,280,000.00 USD | 0.00 USD | 356.65 USD | `-32.97%` | `571.10` |
| `Live` | `Long` | `0.6255` | 4,280,000.00 USD | 0.00 USD | 32,070.00 USD | `-32.86%` | `51,265.70` |
| `Live` | `Long` | `0.6265` | 4,250,000.00 USD | 0.00 USD | 546.18 USD | `-32.75%` | `871.80` |
| `Live` | `Long` | `0.6285` | 4,250,000.00 USD | 0.00 USD | 102.45 USD | `-32.54%` | `163.00` |
| `Live` | `Long` | `0.6305` | 4,250,000.00 USD | 0.00 USD | 319.35 USD | `-32.32%` | `506.50` |
| `Live` | `Long` | `0.6315` | 4,250,000.00 USD | 0.00 USD | 3,510.00 USD | `-32.21%` | `5,564.80` |
| `Live` | `Long` | `0.6345` | 4,250,000.00 USD | 0.00 USD | 450.05 USD | `-31.89%` | `709.30` |
| `Live` | `Long` | `0.6355` | 4,250,000.00 USD | 0.00 USD | 207.17 USD | `-31.78%` | `326.00` |
| `Live` | `Long` | `0.6365` | 4,250,000.00 USD | 0.00 USD | 2,850.00 USD | `-31.68%` | `4,478.70` |
| `Live` | `Long` | `0.6375` | 4,240,000.00 USD | 0.00 USD | 2,240.00 USD | `-31.57%` | `3,513.60` |
| `Live` | `Long` | `0.6395` | 4,240,000.00 USD | 0.00 USD | 559.75 USD | `-31.36%` | `875.30` |
| `Live` | `Long` | `0.6405` | 4,240,000.00 USD | 0.00 USD | 2,070.00 USD | `-31.25%` | `3,227.90` |
| `Live` | `Long` | `0.6415` | 4,240,000.00 USD | 0.00 USD | 86,920.00 USD | `-31.14%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 4,150,000.00 USD | 0.00 USD | 477.63 USD | `-31.03%` | `743.40` |
| `Live` | `Long` | `0.6435` | 4,150,000.00 USD | 0.00 USD | 489.83 USD | `-30.93%` | `761.20` |
| `Live` | `Long` | `0.6445` | 4,150,000.00 USD | 0.00 USD | 65,790.00 USD | `-30.82%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 4,090,000.00 USD | 0.00 USD | 471.21 USD | `-30.71%` | `730.00` |
| `Live` | `Long` | `0.6475` | 4,080,000.00 USD | 0.00 USD | 3,910.00 USD | `-30.50%` | `6,031.70` |
| `Live` | `Long` | `0.6485` | 4,080,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.39%` | `6,766.10` |
| `Live` | `Long` | `0.6495` | 4,080,000.00 USD | 0.00 USD | 721.59 USD | `-30.28%` | `1,111.00` |
| `Live` | `Long` | `0.6505` | 4,080,000.00 USD | 0.00 USD | 631.12 USD | `-30.17%` | `970.20` |
| `Live` | `Long` | `0.6515` | 4,080,000.00 USD | 0.00 USD | 416,790.00 USD | `-30.07%` | `639,745.30` |
| `Live` | `Long` | `0.6535` | 3,660,000.00 USD | 0.00 USD | 134,070.00 USD | `-29.85%` | `205,164.00` |
| `Live` | `Long` | `0.6545` | 3,520,000.00 USD | 0.00 USD | 1,750.00 USD | `-29.75%` | `2,666.60` |
| `Live` | `Long` | `0.6555` | 3,520,000.00 USD | 0.00 USD | 1,730.00 USD | `-29.64%` | `2,634.80` |
| `Live` | `Long` | `0.6565` | 3,520,000.00 USD | 0.00 USD | 9,190.00 USD | `-29.53%` | `14,002.00` |
| `Live` | `Long` | `0.6575` | 3,510,000.00 USD | 0.00 USD | 13,280.00 USD | `-29.42%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,500,000.00 USD | 0.00 USD | 2,970.00 USD | `-29.32%` | `4,508.30` |
| `Live` | `Long` | `0.6615` | 3,500,000.00 USD | 0.00 USD | 10,930.00 USD | `-28.99%` | `16,517.10` |
| `Live` | `Long` | `0.6625` | 3,480,000.00 USD | 0.00 USD | 788.97 USD | `-28.89%` | `1,190.90` |
| `Live` | `Long` | `0.6645` | 3,480,000.00 USD | 0.00 USD | 448.54 USD | `-28.67%` | `675.00` |
| `Live` | `Long` | `0.6675` | 3,480,000.00 USD | 0.00 USD | 7,330.00 USD | `-28.35%` | `10,975.90` |
| `Live` | `Long` | `0.6685` | 3,480,000.00 USD | 0.00 USD | 2,810.00 USD | `-28.24%` | `4,203.00` |
| `Live` | `Long` | `0.6695` | 3,470,000.00 USD | 0.00 USD | 161.22 USD | `-28.14%` | `240.80` |
| `Live` | `Long` | `0.6705` | 3,470,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.03%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,470,000.00 USD | 0.00 USD | 8,500.00 USD | `-27.92%` | `12,661.20` |
| `Live` | `Long` | `0.6725` | 3,460,000.00 USD | 0.00 USD | 1,500.00 USD | `-27.81%` | `2,227.70` |
| `Live` | `Long` | `0.6735` | 3,460,000.00 USD | 0.00 USD | 633.09 USD | `-27.71%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,460,000.00 USD | 0.00 USD | 6,520.00 USD | `-27.60%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 3,450,000.00 USD | 0.00 USD | 111.59 USD | `-27.49%` | `165.20` |
| `Live` | `Long` | `0.6765` | 3,450,000.00 USD | 0.00 USD | 1,040.00 USD | `-27.38%` | `1,539.20` |
| `Live` | `Long` | `0.6785` | 3,450,000.00 USD | 0.00 USD | 10,350.00 USD | `-27.17%` | `15,251.40` |
| `Live` | `Long` | `0.6795` | 3,440,000.00 USD | 0.00 USD | 35,250.00 USD | `-27.06%` | `51,872.10` |
| `Live` | `Long` | `0.6805` | 3,410,000.00 USD | 0.00 USD | 1,600.00 USD | `-26.95%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 3,410,000.00 USD | 0.00 USD | 3,380.00 USD | `-26.85%` | `4,954.70` |
| `Live` | `Long` | `0.6825` | 3,400,000.00 USD | 0.00 USD | 15,920.00 USD | `-26.74%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 3,390,000.00 USD | 0.00 USD | 6,350.00 USD | `-26.63%` | `9,292.50` |
| `Live` | `Long` | `0.6845` | 3,380,000.00 USD | 0.00 USD | 5,790.00 USD | `-26.53%` | `8,455.80` |
| `Live` | `Long` | `0.6875` | 3,370,000.00 USD | 0.00 USD | 480.49 USD | `-26.20%` | `698.90` |
| `Live` | `Long` | `0.6885` | 3,370,000.00 USD | 0.00 USD | 83,790.00 USD | `-26.10%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 3,290,000.00 USD | 0.00 USD | 2,110.00 USD | `-25.99%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 3,290,000.00 USD | 0.00 USD | 3,360.00 USD | `-25.88%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 3,280,000.00 USD | 0.00 USD | 8,970.00 USD | `-25.77%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 3,270,000.00 USD | 0.00 USD | 3,670.00 USD | `-25.56%` | `5,287.80` |
| `Live` | `Long` | `0.6965` | 3,270,000.00 USD | 0.00 USD | 273.03 USD | `-25.24%` | `392.00` |
| `Live` | `Long` | `0.6985` | 3,270,000.00 USD | 0.00 USD | 2,600.00 USD | `-25.02%` | `3,723.10` |
| `Live` | `Long` | `0.6995` | 3,270,000.00 USD | 0.00 USD | 8,700.00 USD | `-24.91%` | `12,441.30` |
| `Live` | `Long` | `0.7045` | 3,260,000.00 USD | 0.00 USD | 759.59 USD | `-24.38%` | `1,078.20` |
| `Live` | `Long` | `0.7065` | 3,260,000.00 USD | 0.00 USD | 769.59 USD | `-24.16%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 3,260,000.00 USD | 0.00 USD | 787.73 USD | `-24.06%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 3,260,000.00 USD | 0.00 USD | 3,890.00 USD | `-23.95%` | `5,484.60` |
| `Live` | `Long` | `0.7095` | 3,250,000.00 USD | 0.00 USD | 3,950.00 USD | `-23.84%` | `5,566.60` |
| `Live` | `Long` | `0.7105` | 3,250,000.00 USD | 0.00 USD | 3,530.00 USD | `-23.73%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 3,250,000.00 USD | 0.00 USD | 569.20 USD | `-23.63%` | `800.00` |
| `Live` | `Long` | `0.7125` | 3,250,000.00 USD | 0.00 USD | 156.39 USD | `-23.52%` | `219.50` |
| `Live` | `Long` | `0.7145` | 3,250,000.00 USD | 0.00 USD | 22,830.00 USD | `-23.30%` | `31,949.70` |
| `Live` | `Long` | `0.7175` | 3,220,000.00 USD | 0.00 USD | 1,470.00 USD | `-22.98%` | `2,050.00` |
| `Live` | `Long` | `0.7195` | 3,220,000.00 USD | 0.00 USD | 11,720.00 USD | `-22.77%` | `16,293.90` |
| `Live` | `Long` | `0.7215` | 3,210,000.00 USD | 0.00 USD | 2,480.00 USD | `-22.55%` | `3,440.40` |
| `Live` | `Long` | `0.7225` | 3,210,000.00 USD | 0.00 USD | 129.26 USD | `-22.45%` | `178.90` |
| `Live` | `Long` | `0.7255` | 3,210,000.00 USD | 0.00 USD | 2,660.00 USD | `-22.12%` | `3,662.80` |
| `Live` | `Long` | `0.7265` | 3,200,000.00 USD | 0.00 USD | 1,060.00 USD | `-22.02%` | `1,453.70` |
| `Live` | `Long` | `0.7275` | 3,200,000.00 USD | 0.00 USD | 762.57 USD | `-21.91%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 3,200,000.00 USD | 0.00 USD | 214.03 USD | `-21.80%` | `293.80` |
| `Live` | `Long` | `0.7295` | 3,200,000.00 USD | 0.00 USD | 375.98 USD | `-21.69%` | `515.40` |
| `Live` | `Long` | `0.7305` | 3,200,000.00 USD | 0.00 USD | 119.88 USD | `-21.59%` | `164.10` |
| `Live` | `Long` | `0.7325` | 3,200,000.00 USD | 0.00 USD | 907.93 USD | `-21.37%` | `1,239.50` |
| `Live` | `Long` | `0.7345` | 3,200,000.00 USD | 0.00 USD | 2,340.00 USD | `-21.16%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 3,200,000.00 USD | 0.00 USD | 51,920.00 USD | `-21.05%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 3,150,000.00 USD | 0.00 USD | 6,900.00 USD | `-20.94%` | `9,366.00` |
| `Live` | `Long` | `0.7385` | 3,140,000.00 USD | 0.00 USD | 5,810.00 USD | `-20.73%` | `7,871.10` |
| `Live` | `Long` | `0.7395` | 3,130,000.00 USD | 0.00 USD | 306,210.00 USD | `-20.62%` | `414,071.80` |
| `Live` | `Long` | `0.7405` | 2,830,000.00 USD | 0.00 USD | 3,530.00 USD | `-20.51%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,820,000.00 USD | 0.00 USD | 510.15 USD | `-20.41%` | `688.00` |
| `Live` | `Long` | `0.7425` | 2,820,000.00 USD | 0.00 USD | 784,090.00 USD | `-20.30%` | `1,056,015.30` |
| `Live` | `Long` | `0.7435` | 2,040,000.00 USD | 0.00 USD | 147.81 USD | `-20.19%` | `198.80` |
| `Live` | `Long` | `0.7445` | 2,040,000.00 USD | 0.00 USD | 105.64 USD | `-20.08%` | `141.90` |
| `Live` | `Long` | `0.7475` | 2,040,000.00 USD | 0.00 USD | 103,310.00 USD | `-19.76%` | `138,200.90` |
| `Live` | `Long` | `0.7485` | 1,940,000.00 USD | 0.00 USD | 709.28 USD | `-19.66%` | `947.60` |
| `Live` | `Long` | `0.7495` | 1,930,000.00 USD | 0.00 USD | 811.78 USD | `-19.55%` | `1,083.10` |
| `Live` | `Long` | `0.7515` | 1,930,000.00 USD | 0.00 USD | 43,190.00 USD | `-19.33%` | `57,472.40` |
| `Live` | `Long` | `0.7525` | 1,890,000.00 USD | 0.00 USD | 106.03 USD | `-19.23%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,890,000.00 USD | 0.00 USD | 1,200.00 USD | `-19.12%` | `1,588.10` |
| `Live` | `Long` | `0.7545` | 1,890,000.00 USD | 0.00 USD | 922.07 USD | `-19.01%` | `1,222.10` |
| `Live` | `Long` | `0.7575` | 1,890,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.69%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,890,000.00 USD | 0.00 USD | 36,710.00 USD | `-18.58%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,850,000.00 USD | 0.00 USD | 4,390.00 USD | `-18.47%` | `5,776.10` |
| `Live` | `Long` | `0.7615` | 1,850,000.00 USD | 0.00 USD | 351.43 USD | `-18.26%` | `461.50` |
| `Live` | `Long` | `0.7635` | 1,850,000.00 USD | 0.00 USD | 604.16 USD | `-18.05%` | `791.30` |
| `Live` | `Long` | `0.7645` | 1,840,000.00 USD | 0.00 USD | 2,660.00 USD | `-17.94%` | `3,483.10` |
| `Live` | `Long` | `0.7655` | 1,840,000.00 USD | 0.00 USD | 6,290.00 USD | `-17.83%` | `8,212.10` |
| `Live` | `Long` | `0.7665` | 1,840,000.00 USD | 0.00 USD | 1,950.00 USD | `-17.72%` | `2,550.10` |
| `Live` | `Long` | `0.7675` | 1,830,000.00 USD | 0.00 USD | 10,680.00 USD | `-17.62%` | `13,912.80` |
| `Live` | `Long` | `0.7685` | 1,820,000.00 USD | 0.00 USD | 499.99 USD | `-17.51%` | `650.60` |
| `Live` | `Long` | `0.7695` | 1,820,000.00 USD | 0.00 USD | 144,250.00 USD | `-17.40%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 1,680,000.00 USD | 0.00 USD | 4,350.00 USD | `-17.29%` | `5,644.90` |
| `Live` | `Long` | `0.7715` | 1,670,000.00 USD | 0.00 USD | 3,190.00 USD | `-17.19%` | `4,137.70` |
| `Live` | `Long` | `0.7725` | 1,670,000.00 USD | 0.00 USD | 3,060.00 USD | `-17.08%` | `3,964.90` |
| `Live` | `Long` | `0.7735` | 1,670,000.00 USD | 0.00 USD | 5,370.00 USD | `-16.97%` | `6,941.20` |
| `Live` | `Long` | `0.7755` | 1,660,000.00 USD | 0.00 USD | 126.41 USD | `-16.76%` | `163.00` |
| `Live` | `Long` | `0.7765` | 1,660,000.00 USD | 0.00 USD | 9,050.00 USD | `-16.65%` | `11,650.60` |
| `Live` | `Long` | `0.7775` | 1,650,000.00 USD | 0.00 USD | 544.25 USD | `-16.54%` | `700.00` |
| `Live` | `Long` | `0.7785` | 1,650,000.00 USD | 0.00 USD | 6,450.00 USD | `-16.43%` | `8,285.30` |
| `Live` | `Long` | `0.7795` | 1,650,000.00 USD | 0.00 USD | 444.63 USD | `-16.33%` | `570.40` |
| `Live` | `Long` | `0.7815` | 1,650,000.00 USD | 0.00 USD | 4,630.00 USD | `-16.11%` | `5,918.40` |
| `Live` | `Long` | `0.7835` | 1,640,000.00 USD | 0.00 USD | 950.23 USD | `-15.90%` | `1,212.80` |
| `Live` | `Long` | `0.7845` | 1,640,000.00 USD | 0.00 USD | 24,720.00 USD | `-15.79%` | `31,516.40` |
| `Live` | `Long` | `0.7855` | 1,620,000.00 USD | 0.00 USD | 3,020.00 USD | `-15.68%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 1,610,000.00 USD | 0.00 USD | 2,870.00 USD | `-15.58%` | `3,651.90` |
| `Live` | `Long` | `0.7875` | 1,610,000.00 USD | 0.00 USD | 5,400.00 USD | `-15.47%` | `6,852.00` |
| `Live` | `Long` | `0.7895` | 1,600,000.00 USD | 0.00 USD | 8,660.00 USD | `-15.25%` | `10,969.90` |
| `Live` | `Long` | `0.7905` | 1,600,000.00 USD | 0.00 USD | 3,670.00 USD | `-15.15%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 1,590,000.00 USD | 0.00 USD | 1,290.00 USD | `-15.04%` | `1,623.50` |
| `Live` | `Long` | `0.7925` | 1,590,000.00 USD | 0.00 USD | 385.87 USD | `-14.93%` | `486.90` |
| `Live` | `Long` | `0.7935` | 1,590,000.00 USD | 0.00 USD | 2,220.00 USD | `-14.82%` | `2,799.50` |
| `Live` | `Long` | `0.7945` | 1,590,000.00 USD | 0.00 USD | 7,640.00 USD | `-14.72%` | `9,619.00` |
| `Live` | `Long` | `0.7955` | 1,580,000.00 USD | 0.00 USD | 23,610.00 USD | `-14.61%` | `29,676.80` |
| `Live` | `Long` | `0.7975` | 1,560,000.00 USD | 0.00 USD | 1,170.00 USD | `-14.40%` | `1,464.30` |
| `Live` | `Long` | `0.7985` | 1,560,000.00 USD | 0.00 USD | 643.43 USD | `-14.29%` | `805.80` |
| `Live` | `Long` | `0.7995` | 1,560,000.00 USD | 0.00 USD | 2,580.00 USD | `-14.18%` | `3,228.10` |
| `Live` | `Long` | `0.8005` | 1,550,000.00 USD | 0.00 USD | 1,340.00 USD | `-14.07%` | `1,671.20` |
| `Live` | `Long` | `0.8015` | 1,550,000.00 USD | 0.00 USD | 94,200.00 USD | `-13.97%` | `117,535.80` |
| `Live` | `Long` | `0.8025` | 1,460,000.00 USD | 0.00 USD | 43,090.00 USD | `-13.86%` | `53,695.80` |
| `Live` | `Long` | `0.8035` | 1,410,000.00 USD | 0.00 USD | 27,890.00 USD | `-13.75%` | `34,715.80` |
| `Live` | `Long` | `0.8045` | 1,390,000.00 USD | 0.00 USD | 15,590.00 USD | `-13.64%` | `19,380.70` |
| `Live` | `Long` | `0.8055` | 1,370,000.00 USD | 0.00 USD | 2,450.00 USD | `-13.54%` | `3,036.00` |
| `Live` | `Long` | `0.8085` | 1,370,000.00 USD | 0.00 USD | 22,170.00 USD | `-13.21%` | `27,427.20` |
| `Live` | `Long` | `0.8105` | 1,350,000.00 USD | 0.00 USD | 5,190.00 USD | `-13.00%` | `6,403.40` |
| `Live` | `Long` | `0.8115` | 1,340,000.00 USD | 0.00 USD | 146.48 USD | `-12.89%` | `180.50` |
| `Live` | `Long` | `0.8125` | 1,340,000.00 USD | 0.00 USD | 2,480.00 USD | `-12.79%` | `3,054.20` |
| `Live` | `Long` | `0.8135` | 1,340,000.00 USD | 0.00 USD | 11,260.00 USD | `-12.68%` | `13,843.50` |
| `Live` | `Long` | `0.8145` | 1,330,000.00 USD | 0.00 USD | 5,890.00 USD | `-12.57%` | `7,228.60` |
| `Live` | `Long` | `0.8155` | 1,320,000.00 USD | 0.00 USD | 8,160.00 USD | `-12.46%` | `10,000.00` |
| `Live` | `Long` | `0.8165` | 1,310,000.00 USD | 0.00 USD | 362.12 USD | `-12.36%` | `443.50` |
| `Live` | `Long` | `0.8175` | 1,310,000.00 USD | 0.00 USD | 103,870.00 USD | `-12.25%` | `127,056.90` |
| `Live` | `Long` | `0.8185` | 1,210,000.00 USD | 0.00 USD | 491.10 USD | `-12.14%` | `600.00` |
| `Live` | `Long` | `0.8195` | 1,210,000.00 USD | 0.00 USD | 643.31 USD | `-12.03%` | `785.00` |
| `Live` | `Long` | `0.8205` | 1,210,000.00 USD | 0.00 USD | 2,280.00 USD | `-11.93%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 1,200,000.00 USD | 0.00 USD | 5,180.00 USD | `-11.82%` | `6,300.50` |
| `Live` | `Long` | `0.8225` | 1,200,000.00 USD | 0.00 USD | 466.85 USD | `-11.71%` | `567.60` |
| `Live` | `Long` | `0.8235` | 1,200,000.00 USD | 0.00 USD | 659.29 USD | `-11.60%` | `800.60` |
| `Live` | `Long` | `0.8245` | 1,200,000.00 USD | 0.00 USD | 3,190.00 USD | `-11.50%` | `3,871.50` |
| `Live` | `Long` | `0.8255` | 1,200,000.00 USD | 0.00 USD | 317.82 USD | `-11.39%` | `385.00` |
| `Live` | `Long` | `0.8275` | 1,200,000.00 USD | 0.00 USD | 11,410.00 USD | `-11.18%` | `13,785.20` |
| `Live` | `Long` | `0.8285` | 1,180,000.00 USD | 0.00 USD | 118,200.00 USD | `-11.07%` | `142,661.50` |
| `Live` | `Long` | `0.8295` | 1,070,000.00 USD | 0.00 USD | 32,530.00 USD | `-10.96%` | `39,217.20` |
| `Live` | `Long` | `0.8305` | 1,030,000.00 USD | 0.00 USD | 1,670.00 USD | `-10.85%` | `2,011.70` |
| `Live` | `Long` | `0.8325` | 1,030,000.00 USD | 0.00 USD | 18,980.00 USD | `-10.64%` | `22,795.90` |
| `Live` | `Long` | `0.8335` | 1,010,000.00 USD | 0.00 USD | 115.27 USD | `-10.53%` | `138.30` |
| `Live` | `Long` | `0.8355` | 1,010,000.00 USD | 0.00 USD | 17,770.00 USD | `-10.32%` | `21,269.40` |
| `Live` | `Long` | `0.8365` | 994,430.00 USD | 0.00 USD | 689.44 USD | `-10.21%` | `824.20` |
| `Live` | `Long` | `0.8375` | 993,740.00 USD | 0.00 USD | 137.85 USD | `-10.10%` | `164.60` |
| `Live` | `Long` | `0.8385` | 993,600.00 USD | 0.00 USD | 79,450.00 USD | `-9.99%` | `94,750.80` |
| `Live` | `Long` | `0.8395` | 914,150.00 USD | 0.00 USD | 38,940.00 USD | `-9.89%` | `46,389.50` |
| `Live` | `Long` | `0.8405` | 875,210.00 USD | 0.00 USD | 628.27 USD | `-9.78%` | `747.50` |
| `Live` | `Long` | `0.8415` | 874,580.00 USD | 0.00 USD | 9,110.00 USD | `-9.67%` | `10,825.10` |
| `Live` | `Long` | `0.8425` | 865,470.00 USD | 0.00 USD | 8,460.00 USD | `-9.57%` | `10,043.20` |
| `Live` | `Long` | `0.8435` | 857,010.00 USD | 0.00 USD | 6,280.00 USD | `-9.46%` | `7,446.40` |
| `Live` | `Long` | `0.8445` | 850,730.00 USD | 0.00 USD | 133.18 USD | `-9.35%` | `157.70` |
| `Live` | `Long` | `0.8455` | 850,600.00 USD | 0.00 USD | 6,630.00 USD | `-9.24%` | `7,840.60` |
| `Live` | `Long` | `0.8465` | 843,970.00 USD | 0.00 USD | 15,830.00 USD | `-9.14%` | `18,696.70` |
| `Live` | `Long` | `0.8475` | 828,140.00 USD | 0.00 USD | 29,810.00 USD | `-9.03%` | `35,169.30` |
| `Live` | `Long` | `0.8485` | 798,340.00 USD | 0.00 USD | 1,890.00 USD | `-8.92%` | `2,222.00` |
| `Live` | `Long` | `0.8495` | 796,450.00 USD | 0.00 USD | 17,790.00 USD | `-8.81%` | `20,947.60` |
| `Live` | `Long` | `0.8515` | 778,650.00 USD | 0.00 USD | 1,220.00 USD | `-8.60%` | `1,433.90` |
| `Live` | `Long` | `0.8535` | 777,430.00 USD | 0.00 USD | 15,640.00 USD | `-8.38%` | `18,326.40` |
| `Live` | `Long` | `0.8545` | 761,790.00 USD | 0.00 USD | 2,030.00 USD | `-8.28%` | `2,375.90` |
| `Live` | `Long` | `0.8555` | 759,760.00 USD | 0.00 USD | 139.53 USD | `-8.17%` | `163.10` |
| `Live` | `Long` | `0.8565` | 759,620.00 USD | 0.00 USD | 36,350.00 USD | `-8.06%` | `42,440.00` |
| `Live` | `Long` | `0.8585` | 723,270.00 USD | 0.00 USD | 14,660.00 USD | `-7.85%` | `17,077.30` |
| `Live` | `Long` | `0.8595` | 708,610.00 USD | 0.00 USD | 7,610.00 USD | `-7.74%` | `8,848.50` |
| `Live` | `Long` | `0.8605` | 701,010.00 USD | 0.00 USD | 19,020.00 USD | `-7.63%` | `22,098.50` |
| `Live` | `Long` | `0.8615` | 681,990.00 USD | 0.00 USD | 793.18 USD | `-7.53%` | `920.70` |
| `Live` | `Long` | `0.8625` | 681,200.00 USD | 0.00 USD | 26,310.00 USD | `-7.42%` | `30,507.00` |
| `Live` | `Long` | `0.8635` | 654,890.00 USD | 0.00 USD | 4,710.00 USD | `-7.31%` | `5,449.60` |
| `Live` | `Long` | `0.8645` | 650,180.00 USD | 0.00 USD | 2,580.00 USD | `-7.20%` | `2,988.60` |
| `Live` | `Long` | `0.8655` | 647,600.00 USD | 0.00 USD | 1,230.00 USD | `-7.10%` | `1,426.30` |
| `Live` | `Long` | `0.8665` | 646,360.00 USD | 0.00 USD | 1,040.00 USD | `-6.99%` | `1,205.70` |
| `Live` | `Long` | `0.8675` | 645,320.00 USD | 0.00 USD | 11,820.00 USD | `-6.88%` | `13,628.20` |
| `Live` | `Long` | `0.8685` | 633,490.00 USD | 0.00 USD | 588.84 USD | `-6.77%` | `678.00` |
| `Live` | `Long` | `0.8695` | 632,910.00 USD | 0.00 USD | 4,920.00 USD | `-6.67%` | `5,663.60` |
| `Live` | `Long` | `0.8705` | 627,980.00 USD | 0.00 USD | 11,990.00 USD | `-6.56%` | `13,768.60` |
| `Live` | `Long` | `0.8715` | 616,000.00 USD | 0.00 USD | 7,540.00 USD | `-6.45%` | `8,654.90` |
| `Live` | `Long` | `0.8725` | 608,450.00 USD | 0.00 USD | 29,520.00 USD | `-6.34%` | `33,829.20` |
| `Live` | `Long` | `0.8735` | 578,940.00 USD | 0.00 USD | 129,080.00 USD | `-6.24%` | `147,768.00` |
| `Live` | `Long` | `0.8745` | 449,860.00 USD | 0.00 USD | 13,880.00 USD | `-6.13%` | `15,872.80` |
| `Live` | `Long` | `0.8755` | 435,980.00 USD | 0.00 USD | 1,420.00 USD | `-6.02%` | `1,624.00` |
| `Live` | `Long` | `0.8765` | 434,560.00 USD | 0.00 USD | 33,510.00 USD | `-5.92%` | `38,226.70` |
| `Live` | `Long` | `0.8775` | 401,050.00 USD | 0.00 USD | 16,030.00 USD | `-5.81%` | `18,270.50` |
| `Live` | `Long` | `0.8785` | 385,020.00 USD | 0.00 USD | 56,160.00 USD | `-5.70%` | `63,924.50` |
| `Live` | `Long` | `0.8795` | 328,860.00 USD | 0.00 USD | 172,470.00 USD | `-5.59%` | `196,099.30` |
| `Live` | `Long` | `0.8805` | 156,390.00 USD | 0.00 USD | 1,530.00 USD | `-5.49%` | `1,737.40` |
| `Live` | `Long` | `0.8815` | 154,860.00 USD | 0.00 USD | 8,730.00 USD | `-5.38%` | `9,904.10` |
| `Live` | `Long` | `0.8825` | 146,130.00 USD | 0.00 USD | 7,190.00 USD | `-5.27%` | `8,151.30` |
| `Live` | `Long` | `0.8835` | 138,940.00 USD | 0.00 USD | 7,220.00 USD | `-5.16%` | `8,171.40` |
| `Live` | `Long` | `0.8845` | 131,720.00 USD | 0.00 USD | 3,550.00 USD | `-5.06%` | `4,018.00` |
| `Live` | `Long` | `0.8855` | 128,170.00 USD | 0.00 USD | 2,660.00 USD | `-4.95%` | `2,998.60` |
| `Live` | `Long` | `0.8865` | 125,510.00 USD | 0.00 USD | 35,970.00 USD | `-4.84%` | `40,570.10` |
| `Live` | `Long` | `0.8875` | 89,550.00 USD | 0.00 USD | 13,890.00 USD | `-4.73%` | `15,652.60` |
| `Live` | `Long` | `0.8885` | 75,650.00 USD | 0.00 USD | 697.38 USD | `-4.63%` | `784.90` |
| `Live` | `Long` | `0.8895` | 74,960.00 USD | 0.00 USD | 3,530.00 USD | `-4.52%` | `3,972.10` |
| `Live` | `Long` | `0.8905` | 71,420.00 USD | 0.00 USD | 139.90 USD | `-4.41%` | `157.10` |
| `Live` | `Long` | `0.8915` | 71,280.00 USD | 0.00 USD | 1,100.00 USD | `-4.31%` | `1,229.80` |
| `Live` | `Long` | `0.8925` | 70,190.00 USD | 0.00 USD | 1,040.00 USD | `-4.20%` | `1,162.90` |
| `Live` | `Long` | `0.8935` | 69,150.00 USD | 0.00 USD | 23,520.00 USD | `-4.09%` | `26,319.40` |
| `Live` | `Long` | `0.8945` | 45,630.00 USD | 0.00 USD | 5,750.00 USD | `-3.98%` | `6,428.20` |
| `Live` | `Long` | `0.8955` | 39,880.00 USD | 0.00 USD | 257.01 USD | `-3.88%` | `287.00` |
| `Live` | `Long` | `0.8965` | 39,630.00 USD | 0.00 USD | 29,550.00 USD | `-3.77%` | `32,958.10` |
| `Live` | `Long` | `0.8975` | 10,080.00 USD | 0.00 USD | 3,540.00 USD | `-3.66%` | `3,941.60` |
| `Live` | `Long` | `0.8985` | 6,540.00 USD | 0.00 USD | 320.05 USD | `-3.55%` | `356.20` |
| `Live` | `Long` | `0.8995` | 6,220.00 USD | 0.00 USD | 143.92 USD | `-3.45%` | `160.00` |
| `Live` | `Long` | `0.9055` | 6,080.00 USD | 0.00 USD | 119.44 USD | `-2.80%` | `131.90` |
| `Live` | `Long` | `0.9075` | 5,960.00 USD | 0.00 USD | 5,960.00 USD | `-2.59%` | `6,565.50` |
| `Live` | `Short` | `0.9675` | 3,160.00 USD | 3,160.00 USD | 0.00 USD | `+3.85%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 68,220.00 USD | 65,060.00 USD | 0.00 USD | `+4.17%` | `67,040.50` |
| `Live` | `Short` | `0.9755` | 68,400.00 USD | 176.86 USD | 0.00 USD | `+4.71%` | `181.30` |
| `Live` | `Short` | `0.9765` | 68,610.00 USD | 214.44 USD | 0.00 USD | `+4.82%` | `219.60` |
| `Live` | `Short` | `0.9775` | 68,720.00 USD | 100.88 USD | 0.00 USD | `+4.93%` | `103.20` |
| `Live` | `Short` | `0.9805` | 84,290.00 USD | 15,580.00 USD | 0.00 USD | `+5.25%` | `15,886.90` |
| `Live` | `Short` | `0.9845` | 94,740.00 USD | 10,440.00 USD | 0.00 USD | `+5.68%` | `10,608.60` |
| `Live` | `Short` | `0.9855` | 95,520.00 USD | 786.72 USD | 0.00 USD | `+5.78%` | `798.30` |
| `Live` | `Short` | `0.9865` | 96,940.00 USD | 1,410.00 USD | 0.00 USD | `+5.89%` | `1,433.30` |
| `Live` | `Short` | `0.9875` | 151,540.00 USD | 54,600.00 USD | 0.00 USD | `+6.00%` | `55,292.50` |
| `Live` | `Short` | `0.9885` | 156,460.00 USD | 4,930.00 USD | 0.00 USD | `+6.11%` | `4,982.50` |
| `Live` | `Short` | `0.9895` | 162,230.00 USD | 5,760.00 USD | 0.00 USD | `+6.21%` | `5,824.20` |
| `Live` | `Short` | `0.9905` | 182,280.00 USD | 20,050.00 USD | 0.00 USD | `+6.32%` | `20,246.30` |
| `Live` | `Short` | `0.9925` | 184,700.00 USD | 2,420.00 USD | 0.00 USD | `+6.54%` | `2,434.50` |
| `Live` | `Short` | `0.9945` | 191,120.00 USD | 6,430.00 USD | 0.00 USD | `+6.75%` | `6,462.70` |
| `Live` | `Short` | `0.9965` | 191,250.00 USD | 125.66 USD | 0.00 USD | `+6.97%` | `126.10` |
| `Live` | `Short` | `0.9975` | 195,430.00 USD | 4,180.00 USD | 0.00 USD | `+7.07%` | `4,189.30` |
| `Live` | `Short` | `1.00` | 195,740.00 USD | 314.41 USD | 0.00 USD | `+7.82%` | `313.00` |
| `Live` | `Short` | `1.02` | 195,910.00 USD | 170.40 USD | 0.00 USD | `+9.00%` | `167.80` |
| `Live` | `Short` | `1.02` | 204,890.00 USD | 8,980.00 USD | 0.00 USD | `+9.11%` | `8,832.40` |
| `Live` | `Short` | `1.04` | 215,290.00 USD | 10,400.00 USD | 0.00 USD | `+11.58%` | `10,007.60` |
| `Live` | `Short` | `1.04` | 215,430.00 USD | 139.22 USD | 0.00 USD | `+11.69%` | `133.80` |
| `Live` | `Short` | `1.05` | 216,030.00 USD | 597.52 USD | 0.00 USD | `+12.76%` | `568.80` |
| `Live` | `Short` | `1.05` | 218,420.00 USD | 2,390.00 USD | 0.00 USD | `+12.87%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 219,750.00 USD | 1,330.00 USD | 0.00 USD | `+12.98%` | `1,260.50` |
| `Live` | `Short` | `1.05` | 220,060.00 USD | 317.52 USD | 0.00 USD | `+13.08%` | `301.40` |
| `Live` | `Short` | `1.05` | 220,390.00 USD | 328.69 USD | 0.00 USD | `+13.19%` | `311.70` |
| `Live` | `Short` | `1.07` | 220,510.00 USD | 114.44 USD | 0.00 USD | `+14.80%` | `107.00` |
| `Live` | `Short` | `1.08` | 221,660.00 USD | 1,150.00 USD | 0.00 USD | `+15.66%` | `1,066.30` |
| `Live` | `Short` | `1.08` | 227,360.00 USD | 5,700.00 USD | 0.00 USD | `+15.87%` | `5,278.70` |
| `Live` | `Short` | `1.08` | 230,940.00 USD | 3,580.00 USD | 0.00 USD | `+15.98%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 234,070.00 USD | 3,130.00 USD | 0.00 USD | `+16.20%` | `2,889.30` |
| `Live` | `Short` | `1.08` | 234,230.00 USD | 166.43 USD | 0.00 USD | `+16.30%` | `153.60` |
| `Live` | `Short` | `1.08` | 235,340.00 USD | 1,110.00 USD | 0.00 USD | `+16.41%` | `1,026.10` |
| `Live` | `Short` | `1.09` | 240,900.00 USD | 5,550.00 USD | 0.00 USD | `+16.95%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 241,220.00 USD | 324.90 USD | 0.00 USD | `+18.02%` | `295.50` |
| `Live` | `Short` | `1.10` | 241,500.00 USD | 277.22 USD | 0.00 USD | `+18.13%` | `251.90` |
| `Live` | `Short` | `1.13` | 264,810.00 USD | 23,310.00 USD | 0.00 USD | `+20.92%` | `20,691.10` |
| `Live` | `Short` | `1.20` | 266,260.00 USD | 1,450.00 USD | 0.00 USD | `+28.54%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 266,510.00 USD | 253.69 USD | 0.00 USD | `+28.76%` | `211.50` |
| `Live` | `Short` | `1.20` | 296,280.00 USD | 29,760.00 USD | 0.00 USD | `+29.08%` | `24,749.90` |
| `Live` | `Short` | `1.21` | 296,420.00 USD | 147.43 USD | 0.00 USD | `+29.40%` | `122.30` |
| `Live` | `Short` | `1.22` | 300,870.00 USD | 4,440.00 USD | 0.00 USD | `+30.80%` | `3,646.70` |
| `Live` | `Short` | `1.23` | 315,510.00 USD | 14,640.00 USD | 0.00 USD | `+32.19%` | `11,891.60` |
| `Live` | `Short` | `1.23` | 315,890.00 USD | 380.84 USD | 0.00 USD | `+32.51%` | `308.50` |
| `Live` | `Short` | `1.26` | 316,030.00 USD | 137.21 USD | 0.00 USD | `+34.87%` | `109.20` |
| `Live` | `Short` | `1.26` | 530,030.00 USD | 214,000.00 USD | 0.00 USD | `+35.09%` | `170,042.00` |
| `Live` | `Short` | `1.26` | 532,700.00 USD | 2,670.00 USD | 0.00 USD | `+35.20%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 572,580.00 USD | 39,880.00 USD | 0.00 USD | `+37.66%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 574,700.00 USD | 2,120.00 USD | 0.00 USD | `+38.74%` | `1,639.00` |
| `Live` | `Short` | `1.29` | 574,920.00 USD | 226.80 USD | 0.00 USD | `+38.95%` | `175.20` |
| `Live` | `Short` | `1.30` | 575,040.00 USD | 114.40 USD | 0.00 USD | `+39.38%` | `88.10` |
| `Live` | `Short` | `1.31` | 576,050.00 USD | 1,020.00 USD | 0.00 USD | `+40.46%` | `777.20` |
| `Live` | `Short` | `1.31` | 607,590.00 USD | 31,530.00 USD | 0.00 USD | `+40.78%` | `24,042.40` |
| `Live` | `Short` | `1.33` | 613,920.00 USD | 6,340.00 USD | 0.00 USD | `+42.28%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 635,890.00 USD | 21,970.00 USD | 0.00 USD | `+42.60%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 636,250.00 USD | 358.30 USD | 0.00 USD | `+42.82%` | `269.30` |
| `Live` | `Short` | `1.33` | 637,770.00 USD | 1,520.00 USD | 0.00 USD | `+43.03%` | `1,143.40` |
| `Live` | `Short` | `1.34` | 644,630.00 USD | 6,860.00 USD | 0.00 USD | `+43.78%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 1,000,000.00 USD | 358,280.00 USD | 0.00 USD | `+47.33%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 1,010,000.00 USD | 4,450.00 USD | 0.00 USD | `+51.83%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 1,010,000.00 USD | 402.08 USD | 0.00 USD | `+54.20%` | `279.90` |
| `Live` | `Short` | `1.44` | 1,010,000.00 USD | 288.68 USD | 0.00 USD | `+54.62%` | `200.40` |
| `Live` | `Short` | `1.44` | 1,010,000.00 USD | 1,190.00 USD | 0.00 USD | `+54.84%` | `826.40` |
| `Live` | `Short` | `1.45` | 1,010,000.00 USD | 4,740.00 USD | 0.00 USD | `+55.16%` | `3,279.70` |
| `Live` | `Short` | `1.47` | 1,020,000.00 USD | 9,520.00 USD | 0.00 USD | `+57.42%` | `6,491.20` |
| `Live` | `Short` | `1.49` | 1,020,000.00 USD | 146.47 USD | 0.00 USD | `+60.10%` | `98.20` |
| `Live` | `Short` | `1.49` | 1,030,000.00 USD | 1,360.00 USD | 0.00 USD | `+60.21%` | `910.40` |
| `Live` | `Short` | `1.51` | 1,030,000.00 USD | 4,020.00 USD | 0.00 USD | `+62.57%` | `2,654.10` |
| `Live` | `Short` | `1.52` | 1,050,000.00 USD | 24,220.00 USD | 0.00 USD | `+63.10%` | `15,941.90` |
| `Live` | `Short` | `1.54` | 1,050,000.00 USD | 144.34 USD | 0.00 USD | `+64.82%` | `94.00` |
| `Live` | `Short` | `1.58` | 1,070,000.00 USD | 17,930.00 USD | 0.00 USD | `+69.33%` | `11,363.40` |
| `Live` | `Short` | `1.59` | 3,720,000.00 USD | 2,650,000.00 USD | 0.00 USD | `+70.62%` | `1,664,573.50` |
| `Live` | `Short` | `1.60` | 3,720,000.00 USD | 1,080.00 USD | 0.00 USD | `+71.58%` | `676.70` |
| `Live` | `Short` | `1.61` | 3,720,000.00 USD | 122.73 USD | 0.00 USD | `+72.66%` | `76.30` |
| `Live` | `Short` | `1.62` | 3,730,000.00 USD | 9,710.00 USD | 0.00 USD | `+73.62%` | `6,000.00` |
| `Live` | `Short` | `1.65` | 3,750,000.00 USD | 21,330.00 USD | 0.00 USD | `+76.74%` | `12,957.30` |
| `Live` | `Short` | `1.67` | 3,790,000.00 USD | 39,210.00 USD | 0.00 USD | `+78.88%` | `23,529.40` |
| `Live` | `Short` | `1.67` | 3,800,000.00 USD | 9,450.00 USD | 0.00 USD | `+79.64%` | `5,645.40` |
| `Live` | `Short` | `1.70` | 4,090,000.00 USD | 294,360.00 USD | 0.00 USD | `+82.64%` | `173,000.00` |
| `Live` | `Short` | `1.71` | 4,090,000.00 USD | 205.67 USD | 0.00 USD | `+83.82%` | `120.10` |
| `Live` | `Short` | `1.73` | 4,180,000.00 USD | 86,110.00 USD | 0.00 USD | `+86.08%` | `49,674.30` |
| `Live` | `Short` | `1.74` | 4,180,000.00 USD | 146.65 USD | 0.00 USD | `+86.29%` | `84.50` |
| `Live` | `Short` | `1.74` | 4,180,000.00 USD | 2,080.00 USD | 0.00 USD | `+86.83%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 4,200,000.00 USD | 19,920.00 USD | 0.00 USD | `+88.01%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 4,210,000.00 USD | 11,350.00 USD | 0.00 USD | `+88.12%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 4,210,000.00 USD | 1,520.00 USD | 0.00 USD | `+88.33%` | `868.90` |
| `Live` | `Short` | `1.78` | 4,220,000.00 USD | 2,420.00 USD | 0.00 USD | `+91.12%` | `1,360.10` |
| `Live` | `Short` | `1.79` | 4,220,000.00 USD | 781.77 USD | 0.00 USD | `+91.76%` | `437.60` |
| `Live` | `Short` | `1.79` | 4,220,000.00 USD | 952.52 USD | 0.00 USD | `+92.62%` | `530.80` |
| `Live` | `Short` | `1.83` | 4,230,000.00 USD | 14,230.00 USD | 0.00 USD | `+96.06%` | `7,789.30` |
| `Live` | `Short` | `1.83` | 4,230,000.00 USD | 203.88 USD | 0.00 USD | `+96.27%` | `111.50` |
| `Live` | `Short` | `1.85` | 4,230,000.00 USD | 943.75 USD | 0.00 USD | `+98.63%` | `510.00` |
| `Live` | `Short` | `1.85` | 4,230,000.00 USD | 190.35 USD | 0.00 USD | `+98.96%` | `102.70` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2745` | 1,790,000.00 USD | 0.00 USD | 455.97 USD | `-70.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,790,000.00 USD | 0.00 USD | 102.75 USD | `-63.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,790,000.00 USD | 0.00 USD | 256.78 USD | `-62.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,790,000.00 USD | 0.00 USD | 428.87 USD | `-58.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,790,000.00 USD | 0.00 USD | 123.45 USD | `-55.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,790,000.00 USD | 0.00 USD | 818.15 USD | `-54.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 1,790,000.00 USD | 0.00 USD | 454.04 USD | `-54.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,790,000.00 USD | 0.00 USD | 436.41 USD | `-53.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,780,000.00 USD | 0.00 USD | 876.79 USD | `-53.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,780,000.00 USD | 0.00 USD | 466.72 USD | `-51.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,780,000.00 USD | 0.00 USD | 142.95 USD | `-48.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,780,000.00 USD | 0.00 USD | 5,650.00 USD | `-46.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,780,000.00 USD | 0.00 USD | 151.74 USD | `-44.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,780,000.00 USD | 0.00 USD | 123.91 USD | `-44.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,780,000.00 USD | 0.00 USD | 219.80 USD | `-41.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,780,000.00 USD | 0.00 USD | 237,400.00 USD | `-40.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 1,540,000.00 USD | 0.00 USD | 276.75 USD | `-40.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 1,540,000.00 USD | 0.00 USD | 2,010.00 USD | `-39.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 1,540,000.00 USD | 0.00 USD | 119.76 USD | `-37.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 1,540,000.00 USD | 0.00 USD | 108.39 USD | `-35.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 1,540,000.00 USD | 0.00 USD | 123.28 USD | `-35.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 1,540,000.00 USD | 0.00 USD | 488.52 USD | `-33.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 1,540,000.00 USD | 0.00 USD | 5,940.00 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 1,530,000.00 USD | 0.00 USD | 242.24 USD | `-32.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 1,530,000.00 USD | 0.00 USD | 193.95 USD | `-30.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 1,530,000.00 USD | 0.00 USD | 647.50 USD | `-30.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 1,530,000.00 USD | 0.00 USD | 834.79 USD | `-30.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 1,530,000.00 USD | 0.00 USD | 158.54 USD | `-29.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 1,530,000.00 USD | 0.00 USD | 195.47 USD | `-29.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 1,530,000.00 USD | 0.00 USD | 190.25 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 1,530,000.00 USD | 0.00 USD | 52,450.00 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 1,480,000.00 USD | 0.00 USD | 536.11 USD | `-27.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 1,480,000.00 USD | 0.00 USD | 5,490.00 USD | `-26.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 1,470,000.00 USD | 0.00 USD | 340.75 USD | `-26.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 1,470,000.00 USD | 0.00 USD | 9,270.00 USD | `-25.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 1,460,000.00 USD | 0.00 USD | 120.53 USD | `-25.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 1,460,000.00 USD | 0.00 USD | 160.71 USD | `-25.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 1,460,000.00 USD | 0.00 USD | 187.61 USD | `-24.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 1,460,000.00 USD | 0.00 USD | 2,920.00 USD | `-24.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 1,460,000.00 USD | 0.00 USD | 89,150.00 USD | `-24.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 1,370,000.00 USD | 0.00 USD | 189.06 USD | `-24.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 1,370,000.00 USD | 0.00 USD | 5,650.00 USD | `-24.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 1,360,000.00 USD | 0.00 USD | 100.47 USD | `-23.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 1,360,000.00 USD | 0.00 USD | 152.05 USD | `-23.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 1,360,000.00 USD | 0.00 USD | 123.41 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 1,360,000.00 USD | 0.00 USD | 1,130.00 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 1,360,000.00 USD | 0.00 USD | 18,770.00 USD | `-21.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 1,340,000.00 USD | 0.00 USD | 257.26 USD | `-20.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 1,340,000.00 USD | 0.00 USD | 10,160.00 USD | `-19.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 1,330,000.00 USD | 0.00 USD | 93,810.00 USD | `-19.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 1,240,000.00 USD | 0.00 USD | 1,230.00 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 1,240,000.00 USD | 0.00 USD | 924.99 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 1,240,000.00 USD | 0.00 USD | 804.61 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 1,230,000.00 USD | 0.00 USD | 191.12 USD | `-17.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 1,230,000.00 USD | 0.00 USD | 1,370.00 USD | `-17.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 1,230,000.00 USD | 0.00 USD | 125.92 USD | `-17.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 1,230,000.00 USD | 0.00 USD | 1,150.00 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 1,230,000.00 USD | 0.00 USD | 200.39 USD | `-16.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 1,230,000.00 USD | 0.00 USD | 1,860.00 USD | `-16.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 1,230,000.00 USD | 0.00 USD | 128.47 USD | `-16.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 1,230,000.00 USD | 0.00 USD | 3,130.00 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 1,230,000.00 USD | 0.00 USD | 135.11 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 1,230,000.00 USD | 0.00 USD | 1,500.00 USD | `-15.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 1,220,000.00 USD | 0.00 USD | 25,170.00 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 1,200,000.00 USD | 0.00 USD | 103.42 USD | `-14.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 1,200,000.00 USD | 0.00 USD | 1,260.00 USD | `-14.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 1,200,000.00 USD | 0.00 USD | 5,660.00 USD | `-14.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 1,190,000.00 USD | 0.00 USD | 144.67 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 1,190,000.00 USD | 0.00 USD | 50,540.00 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 1,140,000.00 USD | 0.00 USD | 263.25 USD | `-13.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 1,140,000.00 USD | 0.00 USD | 16,870.00 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 1,120,000.00 USD | 0.00 USD | 91,080.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 1,030,000.00 USD | 0.00 USD | 174.63 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 1,030,000.00 USD | 0.00 USD | 125.72 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 1,030,000.00 USD | 0.00 USD | 340.83 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 1,030,000.00 USD | 0.00 USD | 11,040.00 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 1,020,000.00 USD | 0.00 USD | 922.29 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 1,020,000.00 USD | 0.00 USD | 1,120.00 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 1,020,000.00 USD | 0.00 USD | 124.43 USD | `-10.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 1,020,000.00 USD | 0.00 USD | 4,380.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 1,020,000.00 USD | 0.00 USD | 171.46 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 1,020,000.00 USD | 0.00 USD | 1,270.00 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 1,010,000.00 USD | 0.00 USD | 4,170.00 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 1,010,000.00 USD | 0.00 USD | 610.23 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 1,010,000.00 USD | 0.00 USD | 475.87 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 1,010,000.00 USD | 0.00 USD | 320.31 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 1,010,000.00 USD | 0.00 USD | 1,010.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 1,010,000.00 USD | 0.00 USD | 221.25 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 1,010,000.00 USD | 0.00 USD | 212.81 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 1,010,000.00 USD | 0.00 USD | 462.49 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 1,010,000.00 USD | 0.00 USD | 481.80 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 1,010,000.00 USD | 0.00 USD | 12,210.00 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 993,670.00 USD | 0.00 USD | 901.40 USD | `-8.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 992,770.00 USD | 0.00 USD | 242.93 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 992,530.00 USD | 0.00 USD | 6,200.00 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 986,330.00 USD | 0.00 USD | 108.13 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 986,220.00 USD | 0.00 USD | 1,640.00 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 984,580.00 USD | 0.00 USD | 4,300.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 980,280.00 USD | 0.00 USD | 202.45 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 980,070.00 USD | 0.00 USD | 921.70 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 979,150.00 USD | 0.00 USD | 161.49 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 978,990.00 USD | 0.00 USD | 1,270.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 977,720.00 USD | 0.00 USD | 741.45 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 976,980.00 USD | 0.00 USD | 168.75 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 976,810.00 USD | 0.00 USD | 2,110.00 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 974,700.00 USD | 0.00 USD | 3,350.00 USD | `-6.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 971,350.00 USD | 0.00 USD | 712.45 USD | `-6.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 970,640.00 USD | 0.00 USD | 58,490.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 912,150.00 USD | 0.00 USD | 281.70 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 911,870.00 USD | 0.00 USD | 133.10 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 911,730.00 USD | 0.00 USD | 246.98 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 911,490.00 USD | 0.00 USD | 9,070.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 902,420.00 USD | 0.00 USD | 151.10 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 902,270.00 USD | 0.00 USD | 507.74 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 901,760.00 USD | 0.00 USD | 8,100.00 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 893,660.00 USD | 0.00 USD | 157,870.00 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 735,800.00 USD | 0.00 USD | 5,020.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8835` | 730,780.00 USD | 0.00 USD | 11,690.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8855` | 719,090.00 USD | 0.00 USD | 3,660.00 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 715,430.00 USD | 0.00 USD | 11,560.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 703,880.00 USD | 0.00 USD | 886.79 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8885` | 702,990.00 USD | 0.00 USD | 11,360.00 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 691,630.00 USD | 0.00 USD | 7,820.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8905` | 683,820.00 USD | 0.00 USD | 10,130.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 673,690.00 USD | 0.00 USD | 469.91 USD | `-4.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 673,220.00 USD | 0.00 USD | 10,610.00 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 662,610.00 USD | 0.00 USD | 7,100.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8945` | 655,510.00 USD | 0.00 USD | 2,920.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8955` | 652,590.00 USD | 0.00 USD | 3,900.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 648,690.00 USD | 0.00 USD | 7,930.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8975` | 640,770.00 USD | 0.00 USD | 18,210.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 622,560.00 USD | 0.00 USD | 2,460.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8995` | 620,100.00 USD | 0.00 USD | 28,960.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 591,130.00 USD | 0.00 USD | 4,300.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9015` | 586,830.00 USD | 0.00 USD | 1,230.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 585,610.00 USD | 0.00 USD | 926.06 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 584,680.00 USD | 0.00 USD | 561.16 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 584,120.00 USD | 0.00 USD | 1,140.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9055` | 582,980.00 USD | 0.00 USD | 1,990.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 580,990.00 USD | 0.00 USD | 30,120.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 550,870.00 USD | 0.00 USD | 4,680.00 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 546,190.00 USD | 0.00 USD | 1,440.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 544,750.00 USD | 0.00 USD | 1,520.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9105` | 543,220.00 USD | 0.00 USD | 637.90 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 542,590.00 USD | 0.00 USD | 6,170.00 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9125` | 536,420.00 USD | 0.00 USD | 14,760.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 521,660.00 USD | 0.00 USD | 465.70 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 521,190.00 USD | 0.00 USD | 337.72 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 520,850.00 USD | 0.00 USD | 5,070.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 515,790.00 USD | 0.00 USD | 5,040.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 510,750.00 USD | 0.00 USD | 1,470.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 509,270.00 USD | 0.00 USD | 302.74 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 508,970.00 USD | 0.00 USD | 1,380.00 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 507,590.00 USD | 0.00 USD | 16,090.00 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 491,500.00 USD | 0.00 USD | 7,650.00 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 483,850.00 USD | 0.00 USD | 84,100.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 399,750.00 USD | 0.00 USD | 3,230.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 396,520.00 USD | 0.00 USD | 498.77 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 396,030.00 USD | 0.00 USD | 235,060.00 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 160,960.00 USD | 0.00 USD | 160,180.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 779.75 USD | 0.00 USD | 146.27 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 633.49 USD | 0.00 USD | 195.17 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 438.31 USD | 0.00 USD | 103.17 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 335.14 USD | 0.00 USD | 186.29 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 148.85 USD | 0.00 USD | 148.85 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 5,600.00 USD | 5,600.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 6,570.00 USD | 979.71 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 52,260.00 USD | 45,680.00 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 53,730.00 USD | 1,470.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 53,830.00 USD | 103.95 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 54,010.00 USD | 175.88 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 107,070.00 USD | 53,060.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 110,980.00 USD | 3,910.00 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 119,940.00 USD | 8,960.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 120,100.00 USD | 158.55 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 120,230.00 USD | 132.80 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 120,350.00 USD | 121.15 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 124,700.00 USD | 4,340.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 125,720.00 USD | 1,030.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 126,780.00 USD | 1,050.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 132,780.00 USD | 6,000.00 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 133,040.00 USD | 261.97 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 133,310.00 USD | 265.66 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 134,310.00 USD | 999.27 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 136,870.00 USD | 2,560.00 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 140,010.00 USD | 3,150.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 141,450.00 USD | 1,440.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 144,340.00 USD | 2,890.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 151,940.00 USD | 7,600.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 159,800.00 USD | 7,860.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 159,900.00 USD | 100.17 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 200,740.00 USD | 40,840.00 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 200,900.00 USD | 161.82 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 201,100.00 USD | 197.79 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 202,000.00 USD | 900.10 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 203,340.00 USD | 1,340.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 203,540.00 USD | 204.20 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 205,400.00 USD | 1,860.00 USD | 0.00 USD | `+3.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 209,000.00 USD | 3,590.00 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 210,140.00 USD | 1,150.00 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 210,660.00 USD | 513.54 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 215,960.00 USD | 5,310.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 216,170.00 USD | 210.33 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 217,300.00 USD | 1,130.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 227,880.00 USD | 10,580.00 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 228,130.00 USD | 253.14 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 228,380.00 USD | 244.81 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 228,660.00 USD | 285.72 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 228,870.00 USD | 201.77 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 229,290.00 USD | 421.87 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 265,740.00 USD | 36,450.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 271,210.00 USD | 5,470.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 271,920.00 USD | 714.28 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 272,990.00 USD | 1,060.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 273,260.00 USD | 271.90 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 273,750.00 USD | 490.99 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 274,520.00 USD | 769.72 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 275,510.00 USD | 991.50 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 285,850.00 USD | 10,340.00 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 286,130.00 USD | 284.92 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 286,410.00 USD | 277.64 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 286,760.00 USD | 350.37 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 286,900.00 USD | 144.04 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 287,010.00 USD | 105.44 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 295,770.00 USD | 8,760.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 297,350.00 USD | 1,570.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 299,520.00 USD | 2,180.00 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 299,890.00 USD | 363.87 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 300,480.00 USD | 589.52 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 301,140.00 USD | 660.52 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 311,220.00 USD | 10,090.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 316,650.00 USD | 5,420.00 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 319,420.00 USD | 2,770.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 352,870.00 USD | 33,450.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 353,590.00 USD | 722.63 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 353,910.00 USD | 312.07 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 354,080.00 USD | 171.24 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 354,640.00 USD | 561.11 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 356,250.00 USD | 1,610.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 358,460.00 USD | 2,210.00 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 358,900.00 USD | 432.18 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 359,030.00 USD | 137.88 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 363,200.00 USD | 4,170.00 USD | 0.00 USD | `+10.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 363,360.00 USD | 160.60 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 370,030.00 USD | 6,670.00 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 377,700.00 USD | 7,680.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 377,930.00 USD | 224.56 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 381,500.00 USD | 3,570.00 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 387,690.00 USD | 6,190.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,140,000.00 USD | 1,760,000.00 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,150,000.00 USD | 1,810.00 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,150,000.00 USD | 248.20 USD | 0.00 USD | `+13.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,150,000.00 USD | 5,390.00 USD | 0.00 USD | `+13.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,150,000.00 USD | 285.32 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,150,000.00 USD | 2,570.00 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,160,000.00 USD | 1,240.00 USD | 0.00 USD | `+13.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,160,000.00 USD | 278.06 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,160,000.00 USD | 309.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,160,000.00 USD | 272.12 USD | 0.00 USD | `+14.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,160,000.00 USD | 117.12 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,300,000.00 USD | 140,120.00 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,300,000.00 USD | 530.01 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,300,000.00 USD | 128.23 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,410,000.00 USD | 108,190.00 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,410,000.00 USD | 550.49 USD | 0.00 USD | `+16.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,410,000.00 USD | 5,810.00 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,420,000.00 USD | 5,570.00 USD | 0.00 USD | `+16.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,420,000.00 USD | 1,290.00 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,420,000.00 USD | 294.81 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,420,000.00 USD | 123.13 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,420,000.00 USD | 494.98 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,420,000.00 USD | 613.52 USD | 0.00 USD | `+18.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,540,000.00 USD | 117,450.00 USD | 0.00 USD | `+18.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,540,000.00 USD | 409.76 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,540,000.00 USD | 162.77 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,540,000.00 USD | 959.70 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,540,000.00 USD | 160.18 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,540,000.00 USD | 433.10 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,540,000.00 USD | 293.61 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,650,000.00 USD | 112,050.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,650,000.00 USD | 462.47 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,660,000.00 USD | 2,180.00 USD | 0.00 USD | `+21.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,660,000.00 USD | 273.34 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,660,000.00 USD | 141.31 USD | 0.00 USD | `+21.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,680,000.00 USD | 20,740.00 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,680,000.00 USD | 1,430.00 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,680,000.00 USD | 338.50 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,680,000.00 USD | 769.57 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,680,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,680,000.00 USD | 2,450.00 USD | 0.00 USD | `+24.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,680,000.00 USD | 1,250.00 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,680,000.00 USD | 143.67 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,690,000.00 USD | 1,700.00 USD | 0.00 USD | `+24.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,750,000.00 USD | 63,070.00 USD | 0.00 USD | `+25.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,750,000.00 USD | 304.33 USD | 0.00 USD | `+25.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,750,000.00 USD | 241.65 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,750,000.00 USD | 239.97 USD | 0.00 USD | `+26.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,750,000.00 USD | 2,470.00 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,760,000.00 USD | 3,060.00 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,760,000.00 USD | 351.02 USD | 0.00 USD | `+26.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,070,000.00 USD | 310,250.00 USD | 0.00 USD | `+27.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,070,000.00 USD | 309.53 USD | 0.00 USD | `+27.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,070,000.00 USD | 159.09 USD | 0.00 USD | `+28.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,070,000.00 USD | 146.21 USD | 0.00 USD | `+28.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,150,000.00 USD | 79,220.00 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,150,000.00 USD | 933.81 USD | 0.00 USD | `+28.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,150,000.00 USD | 658.86 USD | 0.00 USD | `+29.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,360,000.00 USD | 213,390.00 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,360,000.00 USD | 211.10 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,360,000.00 USD | 1,050.00 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,360,000.00 USD | 812.24 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,360,000.00 USD | 509.71 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,360,000.00 USD | 162.15 USD | 0.00 USD | `+31.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,360,000.00 USD | 187.04 USD | 0.00 USD | `+32.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,360,000.00 USD | 542.12 USD | 0.00 USD | `+32.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,390,000.00 USD | 23,740.00 USD | 0.00 USD | `+32.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,390,000.00 USD | 2,010.00 USD | 0.00 USD | `+32.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,390,000.00 USD | 345.91 USD | 0.00 USD | `+32.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,390,000.00 USD | 104.79 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,400,000.00 USD | 6,870.00 USD | 0.00 USD | `+34.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,400,000.00 USD | 265.62 USD | 0.00 USD | `+34.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,400,000.00 USD | 1,480.00 USD | 0.00 USD | `+35.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,400,000.00 USD | 1,010.00 USD | 0.00 USD | `+35.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,400,000.00 USD | 340.38 USD | 0.00 USD | `+36.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,400,000.00 USD | 903.22 USD | 0.00 USD | `+36.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,400,000.00 USD | 424.15 USD | 0.00 USD | `+36.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,440,000.00 USD | 41,160.00 USD | 0.00 USD | `+37.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,460,000.00 USD | 12,840.00 USD | 0.00 USD | `+37.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,470,000.00 USD | 12,890.00 USD | 0.00 USD | `+38.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,480,000.00 USD | 8,820.00 USD | 0.00 USD | `+38.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,480,000.00 USD | 466.95 USD | 0.00 USD | `+38.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,480,000.00 USD | 613.59 USD | 0.00 USD | `+38.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,480,000.00 USD | 1,420.00 USD | 0.00 USD | `+39.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,490,000.00 USD | 13,000.00 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,490,000.00 USD | 284.42 USD | 0.00 USD | `+39.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,520,000.00 USD | 22,710.00 USD | 0.00 USD | `+41.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,520,000.00 USD | 640.82 USD | 0.00 USD | `+42.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,530,000.00 USD | 13,400.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,530,000.00 USD | 1,580.00 USD | 0.00 USD | `+44.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,530,000.00 USD | 1,580.00 USD | 0.00 USD | `+44.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,550,000.00 USD | 13,490.00 USD | 0.00 USD | `+44.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,560,000.00 USD | 11,580.00 USD | 0.00 USD | `+44.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,560,000.00 USD | 3,610.00 USD | 0.00 USD | `+45.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,560,000.00 USD | 1,540.00 USD | 0.00 USD | `+46.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,560,000.00 USD | 1,500.00 USD | 0.00 USD | `+46.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,580,000.00 USD | 15,000.00 USD | 0.00 USD | `+46.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,590,000.00 USD | 9,030.00 USD | 0.00 USD | `+47.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,590,000.00 USD | 569.84 USD | 0.00 USD | `+49.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,600,000.00 USD | 13,890.00 USD | 0.00 USD | `+49.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,610,000.00 USD | 2,710.00 USD | 0.00 USD | `+50.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,620,000.00 USD | 15,500.00 USD | 0.00 USD | `+50.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,630,000.00 USD | 13,100.00 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,670,000.00 USD | 32,860.00 USD | 0.00 USD | `+51.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,670,000.00 USD | 7,090.00 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,670,000.00 USD | 106.64 USD | 0.00 USD | `+51.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,680,000.00 USD | 1,430.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,680,000.00 USD | 2,810.00 USD | 0.00 USD | `+51.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,690,000.00 USD | 8,420.00 USD | 0.00 USD | `+52.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 3,690,000.00 USD | 1,410.00 USD | 0.00 USD | `+53.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,690,000.00 USD | 431.38 USD | 0.00 USD | `+54.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,690,000.00 USD | 1,390.00 USD | 0.00 USD | `+54.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,700,000.00 USD | 14,390.00 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,710,000.00 USD | 7,000.00 USD | 0.00 USD | `+55.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,710,000.00 USD | 434.98 USD | 0.00 USD | `+55.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,730,000.00 USD | 14,490.00 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,730,000.00 USD | 1,370.00 USD | 0.00 USD | `+55.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 3,730,000.00 USD | 1,350.00 USD | 0.00 USD | `+56.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,730,000.00 USD | 1,340.00 USD | 0.00 USD | `+57.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,730,000.00 USD | 1,300.00 USD | 0.00 USD | `+58.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,730,000.00 USD | 342.08 USD | 0.00 USD | `+58.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 3,730,000.00 USD | 1,330.00 USD | 0.00 USD | `+58.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,740,000.00 USD | 1,320.00 USD | 0.00 USD | `+59.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,740,000.00 USD | 1,310.00 USD | 0.00 USD | `+59.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,750,000.00 USD | 14,890.00 USD | 0.00 USD | `+59.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 3,760,000.00 USD | 9,580.00 USD | 0.00 USD | `+59.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,780,000.00 USD | 14,980.00 USD | 0.00 USD | `+60.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 3,780,000.00 USD | 5,110.00 USD | 0.00 USD | `+61.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,780,000.00 USD | 1,270.00 USD | 0.00 USD | `+63.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 3,780,000.00 USD | 1,260.00 USD | 0.00 USD | `+63.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 3,790,000.00 USD | 1,980.00 USD | 0.00 USD | `+65.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 3,790,000.00 USD | 574.53 USD | 0.00 USD | `+70.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 3,790,000.00 USD | 391.32 USD | 0.00 USD | `+71.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 3,790,000.00 USD | 1,160.00 USD | 0.00 USD | `+73.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,790,000.00 USD | 1,140.00 USD | 0.00 USD | `+75.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 3,790,000.00 USD | 1,970.00 USD | 0.00 USD | `+76.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 3,790,000.00 USD | 281.45 USD | 0.00 USD | `+78.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 3,790,000.00 USD | 958.84 USD | 0.00 USD | `+81.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 3,800,000.00 USD | 3,550.00 USD | 0.00 USD | `+82.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 3,800,000.00 USD | 1,070.00 USD | 0.00 USD | `+87.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 3,800,000.00 USD | 1,710.00 USD | 0.00 USD | `+89.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,810,000.00 USD | 13,670.00 USD | 0.00 USD | `+93.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 3,810,000.00 USD | 295.46 USD | 0.00 USD | `+93.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,810,000.00 USD | 328.97 USD | 0.00 USD | `+95.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 3,810,000.00 USD | 394.87 USD | 0.00 USD | `+95.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,820,000.00 USD | 10,950.00 USD | 0.00 USD | `+98.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 3,870,000.00 USD | 41,990.00 USD | 0.00 USD | `+98.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.86` | 3,870,000.00 USD | 149.08 USD | 0.00 USD | `+100.03%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.8160` | 32,370,000.00 USD | 0.00 USD | 32,370,000.00 USD | 210,530.00 USD | 62,790.00 USD | 167,200.00 USD |
| `7D` | `0.8180` | 31,930,000.00 USD | 0.00 USD | 31,930,000.00 USD | 77,750.00 USD | 39,880.00 USD | 43,240.00 USD |
| `7D` | `0.8200` | 31,770,000.00 USD | 0.00 USD | 31,770,000.00 USD | 205,920.00 USD | 47,330.00 USD | 97,290.00 USD |
| `7D` | `0.8220` | 31,420,000.00 USD | 0.00 USD | 31,420,000.00 USD | 104,090.00 USD | 39,210.00 USD | 93,700.00 USD |
| `7D` | `0.8240` | 31,180,000.00 USD | 0.00 USD | 31,180,000.00 USD | 97,060.00 USD | 26,160.00 USD | 86,080.00 USD |
| `7D` | `0.8260` | 30,970,000.00 USD | 0.00 USD | 30,970,000.00 USD | 185,230.00 USD | 28,970.00 USD | 110,690.00 USD |
| `7D` | `0.8280` | 30,650,000.00 USD | 0.00 USD | 30,650,000.00 USD | 113,570.00 USD | 43,870.00 USD | 85,440.00 USD |
| `7D` | `0.8300` | 30,400,000.00 USD | 0.00 USD | 30,400,000.00 USD | 30,930.00 USD | 41,810.00 USD | 44,520.00 USD |
| `1D` | `0.8320` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 30,010.00 USD | 11,950.00 USD | 9,850.00 USD |
| `7D` | `0.8320` | 30,290,000.00 USD | 0.00 USD | 30,290,000.00 USD | 90,830.00 USD | 57,170.00 USD | 60,840.00 USD |
| `1D` | `0.8340` | 12,490,000.00 USD | 0.00 USD | 12,490,000.00 USD | 49,780.00 USD | 16,150.00 USD | 43,950.00 USD |
| `7D` | `0.8340` | 30,080,000.00 USD | 0.00 USD | 30,080,000.00 USD | 105,040.00 USD | 53,420.00 USD | 180,080.00 USD |
| `1D` | `0.8360` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 43,570.00 USD | 7,470.00 USD | 20,660.00 USD |
| `7D` | `0.8360` | 29,740,000.00 USD | 0.00 USD | 29,740,000.00 USD | 138,260.00 USD | 17,780.00 USD | 94,730.00 USD |
| `1D` | `0.8380` | 12,310,000.00 USD | 0.00 USD | 12,310,000.00 USD | 29,520.00 USD | 7,740.00 USD | 28,240.00 USD |
| `7D` | `0.8380` | 29,490,000.00 USD | 0.00 USD | 29,490,000.00 USD | 69,590.00 USD | 59,380.00 USD | 96,450.00 USD |
| `1D` | `0.8400` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 19,020.00 USD | 19,340.00 USD | 18,940.00 USD |
| `7D` | `0.8400` | 29,260,000.00 USD | 0.00 USD | 29,260,000.00 USD | 76,470.00 USD | 55,720.00 USD | 58,540.00 USD |
| `1D` | `0.8420` | 12,190,000.00 USD | 0.00 USD | 12,190,000.00 USD | 11,140.00 USD | 15,160.00 USD | 22,140.00 USD |
| `7D` | `0.8420` | 29,070,000.00 USD | 0.00 USD | 29,070,000.00 USD | 70,700.00 USD | 48,060.00 USD | 10,700.00 USD |
| `1D` | `0.8440` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 22,070.00 USD | 15,080.00 USD | 81.17 USD |
| `7D` | `0.8440` | 28,940,000.00 USD | 0.00 USD | 28,940,000.00 USD | 34,250.00 USD | 40,470.00 USD | 28,000.00 USD |
| `1D` | `0.8460` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 10,030.00 USD | 13,860.00 USD | 25,070.00 USD |
| `7D` | `0.8460` | 28,840,000.00 USD | 0.00 USD | 28,840,000.00 USD | 31,090.00 USD | 33,020.00 USD | 73,030.00 USD |
| `1D` | `0.8480` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 32,420.00 USD | 20,130.00 USD | 49,710.00 USD |
| `7D` | `0.8480` | 28,700,000.00 USD | 0.00 USD | 28,700,000.00 USD | 52,580.00 USD | 6,260.00 USD | 34,250.00 USD |
| `1D` | `0.8500` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 61,890.00 USD | 7,390.00 USD | 15,330.00 USD |
| `7D` | `0.8500` | 28,610,000.00 USD | 0.00 USD | 28,610,000.00 USD | 32,630.00 USD | 15,300.00 USD | 23,760.00 USD |
| `1D` | `0.8520` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 30,310.00 USD | 27,790.00 USD | 15,250.00 USD |
| `7D` | `0.8520` | 28,540,000.00 USD | 0.00 USD | 28,540,000.00 USD | 77,320.00 USD | 45,980.00 USD | 45,410.00 USD |
| `1D` | `0.8540` | 11,790,000.00 USD | 0.00 USD | 11,790,000.00 USD | 20,080.00 USD | 11,230.00 USD | 41,090.00 USD |
| `7D` | `0.8540` | 28,370,000.00 USD | 0.00 USD | 28,370,000.00 USD | 92,380.00 USD | 64,630.00 USD | 15,550.00 USD |
| `1D` | `0.8560` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 27,930.00 USD | 22,280.00 USD | 26,990.00 USD |
| `7D` | `0.8560` | 28,200,000.00 USD | 0.00 USD | 28,200,000.00 USD | 87,380.00 USD | 45,770.00 USD | 7,640.00 USD |
| `1D` | `0.8580` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 56,290.00 USD | 13,730.00 USD | 14,850.00 USD |
| `7D` | `0.8580` | 28,060,000.00 USD | 0.00 USD | 28,060,000.00 USD | 65,360.00 USD | 21,180.00 USD | 17,560.00 USD |
| `1D` | `0.8600` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 16,950.00 USD | 6,660.00 USD | 15,960.00 USD |
| `7D` | `0.8600` | 27,950,000.00 USD | 0.00 USD | 27,950,000.00 USD | 38,890.00 USD | 65,420.00 USD | 23,210.00 USD |
| `1D` | `0.8620` | 11,520,000.00 USD | 0.00 USD | 11,520,000.00 USD | 6,110.00 USD | 4,970.00 USD | 396.37 USD |
| `7D` | `0.8620` | 27,820,000.00 USD | 0.00 USD | 27,820,000.00 USD | 25,100.00 USD | 21,240.00 USD | 56,160.00 USD |
| `1D` | `0.8640` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 52,440.00 USD | 25,350.00 USD | 61,080.00 USD |
| `7D` | `0.8640` | 27,720,000.00 USD | 0.00 USD | 27,720,000.00 USD | 38,670.00 USD | 27,710.00 USD | 2,680.00 USD |
| `1D` | `0.8660` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 137,930.00 USD | 1,970.00 USD | 13,560.00 USD |
| `7D` | `0.8660` | 27,650,000.00 USD | 0.00 USD | 27,650,000.00 USD | 261,430.00 USD | 35,900.00 USD | 119,830.00 USD |
| `1D` | `0.8680` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 102,620.00 USD | 60,770.00 USD | 33,690.00 USD |
| `7D` | `0.8680` | 27,240,000.00 USD | 0.00 USD | 27,240,000.00 USD | 208,910.00 USD | 100,620.00 USD | 114,220.00 USD |
| `1D` | `0.8700` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 109,230.00 USD | 90,980.00 USD | 226,980.00 USD |
| `7D` | `0.8700` | 26,810,000.00 USD | 0.00 USD | 26,810,000.00 USD | 377,870.00 USD | 141,350.00 USD | 326,470.00 USD |
| `1D` | `0.8720` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 210,640.00 USD | 63,650.00 USD | 201,220.00 USD |
| `7D` | `0.8720` | 25,970,000.00 USD | 0.00 USD | 25,970,000.00 USD | 440,480.00 USD | 149,650.00 USD | 310,450.00 USD |
| `1D` | `0.8740` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 43,030.00 USD | 19,920.00 USD | 21,550.00 USD |
| `7D` | `0.8740` | 25,070,000.00 USD | 0.00 USD | 25,070,000.00 USD | 566,110.00 USD | 235,670.00 USD | 196,080.00 USD |
| `1D` | `0.8760` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 74,790.00 USD | 73,290.00 USD | 139,450.00 USD |
| `7D` | `0.8760` | 24,070,000.00 USD | 0.00 USD | 24,070,000.00 USD | 594,350.00 USD | 249,690.00 USD | 486,650.00 USD |
| `1D` | `0.8780` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 64,740.00 USD | 47,450.00 USD | 31,970.00 USD |
| `7D` | `0.8780` | 22,740,000.00 USD | 0.00 USD | 22,740,000.00 USD | 261,940.00 USD | 106,230.00 USD | 202,400.00 USD |
| `1D` | `0.8800` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 13,090.00 USD | 12,370.00 USD | 41,460.00 USD |
| `7D` | `0.8800` | 22,170,000.00 USD | 0.00 USD | 22,170,000.00 USD | 439,660.00 USD | 120,050.00 USD | 423,230.00 USD |
| `1D` | `0.8820` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 108,450.00 USD | 63,480.00 USD | 145,380.00 USD |
| `7D` | `0.8820` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 562,000.00 USD | 248,320.00 USD | 318,820.00 USD |
| `1D` | `0.8840` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 300,890.00 USD | 65,390.00 USD | 152,430.00 USD |
| `7D` | `0.8840` | 20,050,000.00 USD | 0.00 USD | 20,050,000.00 USD | 772,470.00 USD | 232,070.00 USD | 537,600.00 USD |
| `1D` | `0.8860` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 272,520.00 USD | 127,540.00 USD | 90,270.00 USD |
| `7D` | `0.8860` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 533,450.00 USD | 257,680.00 USD | 262,580.00 USD |
| `1D` | `0.8880` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 298,190.00 USD | 211,570.00 USD | 486,020.00 USD |
| `7D` | `0.8880` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 1,060,000.00 USD | 404,050.00 USD | 990,720.00 USD |
| `1D` | `0.8900` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 515,380.00 USD | 158,940.00 USD | 513,690.00 USD |
| `7D` | `0.8900` | 15,010,000.00 USD | 0.00 USD | 15,010,000.00 USD | 1,180,000.00 USD | 483,970.00 USD | 1,000,000.00 USD |
| `1D` | `0.8920` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 234,530.00 USD | 59,650.00 USD | 100,400.00 USD |
| `7D` | `0.8920` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 1,550,000.00 USD | 567,000.00 USD | 706,510.00 USD |
| `1D` | `0.8940` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 176,200.00 USD | 130,550.00 USD | 278,110.00 USD |
| `7D` | `0.8940` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 1,220,000.00 USD | 602,640.00 USD | 1,050,000.00 USD |
| `1D` | `0.8960` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 134,160.00 USD | 141,360.00 USD | 176,490.00 USD |
| `7D` | `0.8960` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 657,470.00 USD | 314,840.00 USD | 704,690.00 USD |
| `1D` | `0.8980` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 128,530.00 USD | 69,170.00 USD | 103,680.00 USD |
| `7D` | `0.8980` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 656,780.00 USD | 284,000.00 USD | 169,540.00 USD |
| `1D` | `0.9000` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 53,800.00 USD | 24,210.00 USD | 40,900.00 USD |
| `7D` | `0.9000` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 127,760.00 USD | 33,800.00 USD | 1,800.00 USD |
| `1D` | `0.9020` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 49,680.00 USD | 67,410.00 USD | 190,680.00 USD |
| `7D` | `0.9020` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 8,440.00 USD | 52,590.00 USD | 123,230.00 USD |
| `1D` | `0.9040` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 128,110.00 USD | 81,940.00 USD | 142,620.00 USD |
| `7D` | `0.9040` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 98,990.00 USD | 0.00 USD | 71,470.00 USD |
| `1D` | `0.9060` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 215,300.00 USD | 10,170.00 USD | 60,130.00 USD |
| `7D` | `0.9060` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 245,950.00 USD | 0.00 USD | 2,520.00 USD |
| `1D` | `0.9080` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 305,430.00 USD | 116,800.00 USD | 213,980.00 USD |
| `7D` | `0.9080` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 175,380.00 USD | 19,890.00 USD | 165,310.00 USD |
| `1D` | `0.9100` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 225,400.00 USD | 58,970.00 USD | 153,690.00 USD |
| `7D` | `0.9100` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 123,910.00 USD | 91,580.00 USD | 126,930.00 USD |
| `1D` | `0.9120` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 228,280.00 USD | 39,820.00 USD | 204,060.00 USD |
| `7D` | `0.9120` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 88,860.00 USD | 51,920.00 USD | 105,460.00 USD |
| `1D` | `0.9140` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 172,190.00 USD | 87,890.00 USD | 109,160.00 USD |
| `7D` | `0.9140` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 143,540.00 USD | 58,200.00 USD | 61,200.00 USD |
| `1D` | `0.9160` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 74,950.00 USD | 50,090.00 USD | 65,510.00 USD |
| `7D` | `0.9160` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 171,920.00 USD | 26,360.00 USD | 136,070.00 USD |
| `1D` | `0.9180` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 154,870.00 USD | 9,020.00 USD | 46,150.00 USD |
| `7D` | `0.9180` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD |
| `1D` | `0.9200` | 905,830.00 USD | 0.00 USD | 905,830.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD |
| `7D` | `0.9200` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 386,820.00 USD | 16,660.00 USD | 63,810.00 USD |
| `1D` | `0.9220` | 899,650.00 USD | 0.00 USD | 899,650.00 USD | 32,990.00 USD | 39,420.00 USD | 133,380.00 USD |
| `7D` | `0.9220` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 64,540.00 USD | 156,550.00 USD |
| `1D` | `0.9240` | 693,870.00 USD | 0.00 USD | 693,870.00 USD | 170,280.00 USD | 58,320.00 USD | 150,050.00 USD |
| `7D` | `0.9240` | 826,040.00 USD | 0.00 USD | 826,040.00 USD | 104,080.00 USD | 41,710.00 USD | 184,480.00 USD |
| `1D` | `0.9260` | 315,220.00 USD | 0.00 USD | 315,220.00 USD | 63,790.00 USD | 28,360.00 USD | 0.00 USD |
| `7D` | `0.9260` | 495,770.00 USD | 0.00 USD | 495,770.00 USD | 102,010.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9280` | 223,060.00 USD | 0.00 USD | 223,060.00 USD | 0.00 USD | 44,480.00 USD | 11,800.00 USD |
| `7D` | `0.9280` | 393,760.00 USD | 0.00 USD | 393,760.00 USD | 107,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9300` | 166,780.00 USD | 0.00 USD | 166,780.00 USD | 0.00 USD | 0.00 USD | 166,780.00 USD |
| `7D` | `0.9300` | 285,830.00 USD | 0.00 USD | 285,830.00 USD | 177,720.00 USD | 108,110.00 USD | 0.00 USD |
| `1D` | `0.9310` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9320` | 114,380.00 USD | 114,380.00 USD | 0.00 USD | 100,660.00 USD | 0.00 USD | 13,720.00 USD |
| `7D` | `0.9320` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9340` | 144,850.00 USD | 144,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `7D` | `0.9340` | 102,880.00 USD | 102,880.00 USD | 0.00 USD | 50,160.00 USD | 52,710.00 USD | 0.00 USD |
| `1D` | `0.9360` | 251,630.00 USD | 251,630.00 USD | 0.00 USD | 0.00 USD | 33,250.00 USD | 73,530.00 USD |
| `7D` | `0.9360` | 225,690.00 USD | 225,690.00 USD | 0.00 USD | 122,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9380` | 910,080.00 USD | 910,080.00 USD | 0.00 USD | 246,090.00 USD | 118,850.00 USD | 293,510.00 USD |
| `7D` | `0.9380` | 571,410.00 USD | 571,410.00 USD | 0.00 USD | 168,030.00 USD | 0.00 USD | 177,680.00 USD |
| `1D` | `0.9400` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 80,680.00 USD | 0.00 USD | 38,870.00 USD |
| `7D` | `0.9400` | 899,020.00 USD | 899,020.00 USD | 0.00 USD | 166,670.00 USD | 33,320.00 USD | 127,620.00 USD |
| `7D` | `0.9420` | 919,880.00 USD | 919,880.00 USD | 0.00 USD | 0.00 USD | 20,860.00 USD | 0.00 USD |
| `1D` | `0.9440` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 62,750.00 USD | 47,460.00 USD |
| `7D` | `0.9440` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 216,440.00 USD | 0.00 USD |
| `1D` | `0.9460` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 56,940.00 USD | 28,980.00 USD | 160,360.00 USD |
| `7D` | `0.9460` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD |
| `1D` | `0.9480` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 50,850.00 USD | 26,450.00 USD | 99.96 USD |
| `7D` | `0.9480` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 208,890.00 USD |
| `1D` | `0.9500` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 17,970.00 USD | 6,400.00 USD | 31,450.00 USD |
| `7D` | `0.9500` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 371,330.00 USD |
| `1D` | `0.9520` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 37,450.00 USD | 17,280.00 USD | 86,190.00 USD |
| `7D` | `0.9520` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 62,510.00 USD | 329,600.00 USD |
| `1D` | `0.9540` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 62,990.00 USD | 66,810.00 USD | 55,690.00 USD |
| `7D` | `0.9540` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 10,500.00 USD | 2,560.00 USD | 60,880.00 USD |
| `1D` | `0.9560` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 33,360.00 USD | 0.00 USD |
| `7D` | `0.9560` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 72,330.00 USD | 2,240.00 USD | 0.00 USD |
| `1D` | `0.9580` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 689.00 USD | 43,140.00 USD | 159.08 USD |
| `7D` | `0.9580` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 846,080.00 USD | 0.00 USD | 511.50 USD |
| `1D` | `0.9600` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 110,240.00 USD | 65,470.00 USD | 108,980.00 USD |
| `7D` | `0.9600` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 356,870.00 USD | 73,200.00 USD | 131,760.00 USD |
| `1D` | `0.9620` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 385,380.00 USD | 135,810.00 USD | 290,610.00 USD |
| `7D` | `0.9620` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 741,340.00 USD | 231,300.00 USD | 588,410.00 USD |
| `1D` | `0.9640` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 338,870.00 USD | 116,210.00 USD | 217,530.00 USD |
| `7D` | `0.9640` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 693,720.00 USD | 366,520.00 USD | 508,260.00 USD |
| `1D` | `0.9660` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 274,510.00 USD | 140,370.00 USD | 130,080.00 USD |
| `7D` | `0.9660` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 1,020,000.00 USD | 191,600.00 USD | 548,840.00 USD |
| `1D` | `0.9680` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 310,700.00 USD | 118,860.00 USD | 362,240.00 USD |
| `7D` | `0.9680` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 911,470.00 USD | 631,050.00 USD | 614,230.00 USD |
| `1D` | `0.9700` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 250,300.00 USD | 142,870.00 USD | 193,000.00 USD |
| `7D` | `0.9700` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 694,250.00 USD | 344,900.00 USD | 381,970.00 USD |
| `1D` | `0.9720` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 334,210.00 USD | 127,200.00 USD | 126,890.00 USD |
| `7D` | `0.9720` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 398,310.00 USD | 184,170.00 USD | 138,660.00 USD |
| `1D` | `0.9740` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 167,080.00 USD | 29,860.00 USD | 39,830.00 USD |
| `7D` | `0.9740` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 309,060.00 USD | 116,990.00 USD | 124,030.00 USD |
| `1D` | `0.9760` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 29,860.00 USD | 41,140.00 USD | 87,910.00 USD |
| `7D` | `0.9760` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 182,900.00 USD | 286,070.00 USD | 216,120.00 USD |
| `1D` | `0.9780` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 85,910.00 USD | 32,630.00 USD | 129,550.00 USD |
| `7D` | `0.9780` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 441,770.00 USD | 196,630.00 USD | 512,910.00 USD |
| `1D` | `0.9800` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 101,910.00 USD | 72,820.00 USD | 157,610.00 USD |
| `7D` | `0.9800` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 341,810.00 USD | 87,560.00 USD | 204,510.00 USD |
| `1D` | `0.9820` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 184,070.00 USD | 32,930.00 USD | 53,370.00 USD |
| `7D` | `0.9820` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 108,220.00 USD | 52,160.00 USD | 142,510.00 USD |
| `1D` | `0.9840` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 79,960.00 USD | 66,570.00 USD | 28,500.00 USD |
| `7D` | `0.9840` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 395,810.00 USD | 123,000.00 USD | 177,280.00 USD |
| `1D` | `0.9860` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 128,950.00 USD | 60,420.00 USD | 136,860.00 USD |
| `7D` | `0.9860` | 17,410,000.00 USD | 17,410,000.00 USD | 0.00 USD | 107,440.00 USD | 154,250.00 USD | 73,290.00 USD |
| `1D` | `0.9880` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 85,110.00 USD | 35,320.00 USD | 70,840.00 USD |
| `7D` | `0.9880` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 209,770.00 USD | 64,380.00 USD | 26,750.00 USD |
| `1D` | `0.9900` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 144,770.00 USD | 50,640.00 USD | 76,870.00 USD |
| `7D` | `0.9900` | 18,020,000.00 USD | 18,020,000.00 USD | 0.00 USD | 201,410.00 USD | 100,430.00 USD | 6,630.00 USD |
| `1D` | `0.9920` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 142,180.00 USD | 46,030.00 USD | 21,600.00 USD |
| `7D` | `0.9920` | 18,470,000.00 USD | 18,470,000.00 USD | 0.00 USD | 288,210.00 USD | 79,650.00 USD | 81,440.00 USD |
| `1D` | `0.9940` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 59,940.00 USD | 36,960.00 USD | 59,090.00 USD |
| `7D` | `0.9940` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 143,340.00 USD | 183,310.00 USD | 146,510.00 USD |
| `1D` | `0.9960` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 6,270.00 USD | 11,390.00 USD | 20,320.00 USD |
| `7D` | `0.9960` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 107,780.00 USD | 55,790.00 USD | 291,980.00 USD |
| `1D` | `0.9980` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 138,880.00 USD | 32,380.00 USD | 145,310.00 USD |
| `7D` | `0.9980` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 238,490.00 USD | 42,080.00 USD | 163,410.00 USD |
| `1D` | `1.00` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 18,790.00 USD | 17,140.00 USD | 6,790.00 USD |
| `7D` | `1.00` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 94,210.00 USD | 53,610.00 USD | 65,960.00 USD |
| `1D` | `1.00` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 11,220.00 USD | 18,430.00 USD | 20,250.00 USD |
| `7D` | `1.00` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 276,050.00 USD | 51,850.00 USD | 257,650.00 USD |
| `1D` | `1.00` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 17,620.00 USD | 13,280.00 USD | 22,720.00 USD |
| `7D` | `1.00` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 219,820.00 USD | 45,420.00 USD | 165,190.00 USD |
| `1D` | `1.01` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 9,900.00 USD | 14,230.00 USD | 9,200.00 USD |
| `7D` | `1.01` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 181,560.00 USD | 14,150.00 USD | 68,220.00 USD |
| `1D` | `1.01` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 19,520.00 USD | 9,720.00 USD | 12,400.00 USD |
| `7D` | `1.01` | 21,930,000.00 USD | 21,930,000.00 USD | 0.00 USD | 274,240.00 USD | 66,150.00 USD | 253,510.00 USD |
| `1D` | `1.01` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 13,150.00 USD | 5,570.00 USD | 8,860.00 USD |
| `7D` | `1.01` | 22,580,000.00 USD | 22,580,000.00 USD | 0.00 USD | 311,680.00 USD | 74,250.00 USD | 271,210.00 USD |
| `1D` | `1.01` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 21,660.00 USD | 13,820.00 USD | 33,850.00 USD |
| `7D` | `1.01` | 23,640,000.00 USD | 23,640,000.00 USD | 0.00 USD | 385,660.00 USD | 248,790.00 USD | 419,250.00 USD |
| `1D` | `1.01` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 13,360.00 USD | 11,680.00 USD | 28,370.00 USD |
| `7D` | `1.01` | 24,370,000.00 USD | 24,370,000.00 USD | 0.00 USD | 341,120.00 USD | 208,060.00 USD | 178,380.00 USD |
| `1D` | `1.02` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 23,240.00 USD | 11,060.00 USD | 6,860.00 USD |
| `7D` | `1.02` | 25,280,000.00 USD | 25,280,000.00 USD | 0.00 USD | 402,200.00 USD | 101,810.00 USD | 413,760.00 USD |
| `1D` | `1.02` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 18,720.00 USD | 4,090.00 USD | 1,440.00 USD |
| `7D` | `1.02` | 25,960,000.00 USD | 25,960,000.00 USD | 0.00 USD | 297,940.00 USD | 28,880.00 USD | 346,840.00 USD |
| `1D` | `1.02` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 32,190.00 USD | 13,020.00 USD | 44,180.00 USD |
| `7D` | `1.02` | 26,640,000.00 USD | 26,640,000.00 USD | 0.00 USD | 214,170.00 USD | 110,730.00 USD | 353,160.00 USD |
| `1D` | `1.02` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 45,050.00 USD | 7,770.00 USD | 20,660.00 USD |
| `7D` | `1.02` | 27,030,000.00 USD | 27,030,000.00 USD | 0.00 USD | 208,130.00 USD | 42,850.00 USD | 140,340.00 USD |
| `1D` | `1.02` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 29,960.00 USD | 7,740.00 USD | 28,590.00 USD |
| `7D` | `1.02` | 27,280,000.00 USD | 27,280,000.00 USD | 0.00 USD | 97,520.00 USD | 61,990.00 USD | 96,860.00 USD |
| `1D` | `1.03` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 17,840.00 USD | 16,400.00 USD | 18,870.00 USD |
| `7D` | `1.03` | 27,690,000.00 USD | 27,690,000.00 USD | 0.00 USD | 187,390.00 USD | 56,910.00 USD | 158,140.00 USD |
| `1D` | `1.03` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD |
| `7D` | `1.03` | 27,780,000.00 USD | 27,780,000.00 USD | 0.00 USD | 41,560.00 USD | 32,180.00 USD | 17,510.00 USD |
| `1D` | `1.03` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD |
| `7D` | `1.03` | 28,030,000.00 USD | 28,030,000.00 USD | 0.00 USD | 119,530.00 USD | 47,560.00 USD | 90,140.00 USD |
| `1D` | `1.03` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 20,340.00 USD | 11,130.00 USD | 0.35 USD |
| `7D` | `1.03` | 28,500,000.00 USD | 28,500,000.00 USD | 0.00 USD | 147,960.00 USD | 125,610.00 USD | 193,500.00 USD |
| `1D` | `1.03` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 7,200.00 USD | 11,970.00 USD | 24,940.00 USD |
| `7D` | `1.03` | 28,890,000.00 USD | 28,890,000.00 USD | 0.00 USD | 166,990.00 USD | 102,410.00 USD | 118,210.00 USD |
| `1D` | `1.04` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 26,990.00 USD | 18,830.00 USD | 49,230.00 USD |
| `7D` | `1.04` | 29,280,000.00 USD | 29,280,000.00 USD | 0.00 USD | 184,730.00 USD | 21,870.00 USD | 182,870.00 USD |
| `1D` | `1.04` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 59,260.00 USD | 7,020.00 USD | 15,210.00 USD |
| `7D` | `1.04` | 29,630,000.00 USD | 29,630,000.00 USD | 0.00 USD | 147,100.00 USD | 27,060.00 USD | 173,080.00 USD |
| `1D` | `1.04` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 8,210.00 USD | 7,840.00 USD | 8,140.00 USD |
| `7D` | `1.04` | 29,840,000.00 USD | 29,840,000.00 USD | 0.00 USD | 74,160.00 USD | 58,400.00 USD | 87,090.00 USD |
| `1D` | `1.04` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 21,580.00 USD | 18,300.00 USD | 7,110.00 USD |
| `7D` | `1.04` | 29,940,000.00 USD | 29,940,000.00 USD | 0.00 USD | 53,240.00 USD | 12,870.00 USD | 29,270.00 USD |
| `1D` | `1.04` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 19,660.00 USD | 8,720.00 USD | 41,040.00 USD |
| `7D` | `1.04` | 30,100,000.00 USD | 30,100,000.00 USD | 0.00 USD | 78,480.00 USD | 65,330.00 USD | 15,360.00 USD |
| `1D` | `1.04` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 6,590.00 USD | 7,020.00 USD | 15,410.00 USD |
| `7D` | `1.05` | 30,200,000.00 USD | 30,200,000.00 USD | 0.00 USD | 74,370.00 USD | 30,010.00 USD | 1,070.00 USD |
| `7D` | `1.05` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 50,260.00 USD | 12,520.00 USD | 16,760.00 USD |
| `7D` | `1.05` | 30,290,000.00 USD | 30,290,000.00 USD | 0.00 USD | 1,420.00 USD | 3,180.00 USD | 608.24 USD |
| `7D` | `1.05` | 30,380,000.00 USD | 30,380,000.00 USD | 0.00 USD | 24,860.00 USD | 46,330.00 USD | 21,220.00 USD |
| `7D` | `1.05` | 30,450,000.00 USD | 30,450,000.00 USD | 0.00 USD | 8,480.00 USD | 2,340.00 USD | 53,860.00 USD |
| `7D` | `1.06` | 30,460,000.00 USD | 30,460,000.00 USD | 0.00 USD | 6,690.00 USD | 5,170.00 USD | 0.00 USD |
| `7D` | `1.06` | 30,470,000.00 USD | 30,470,000.00 USD | 0.00 USD | 3,120.00 USD | 3,350.00 USD | 257.56 USD |
| `7D` | `1.06` | 30,500,000.00 USD | 30,500,000.00 USD | 0.00 USD | 15,370.00 USD | 3,080.00 USD | 11,800.00 USD |
| `7D` | `1.06` | 30,500,000.00 USD | 30,500,000.00 USD | 0.00 USD | 4,660.00 USD | 786.13 USD | 265.87 USD |
| `7D` | `1.06` | 30,510,000.00 USD | 30,510,000.00 USD | 0.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `616.88M` | Total OI Tokens: `661,800,261.2 SUI`
  * 1h OI Change: `-0.89%` | 4h OI Change: `-2.71%` | 24h OI Change: `-2.35%`
  * Exchange Breakdown: Binance=`119.82M` | Bybit=`80.88M` | OKX=`33.78M` | Hyperliquid=`31.81M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `20.49K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0076%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0083%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `57.40%` | `42.60%` | `1.35` | 5,350,000.00 USD |
| `15M` | `Binance` | `70.12%` | `29.88%` | `2.35` | 1,570,000.00 USD |
| `15M` | `OKX` | `59.72%` | `40.28%` | `1.48` | 373,580.00 USD |
| `15M` | `Bybit` | `45.8%` | `54.2%` | `0.85` | 304,300.00 USD |
| `15M` | `KuCoin` | `56.57%` | `43.43%` | `1.30` | 20,150.00 USD |
| `15M` | `Gate` | `64.42%` | `35.58%` | `1.81` | 27,820.00 USD |
| `15M` | `Bitget` | `52.3%` | `47.7%` | `1.10` | 98,740.00 USD |
| `15M` | `BingX` | `33.28%` | `66.72%` | `0.50` | 160,910.00 USD |
| `15M` | `MEXC` | `51%` | `49%` | `1.04` | 2,190,000.00 USD |
| `15M` | `Bitunix` | `85.25%` | `14.75%` | `5.78` | 200,780.00 USD |
| `15M` | `Hyperliquid` | `36.36%` | `63.64%` | `0.57` | 27,280.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `58.01%` | `41.99%` | `1.38` | 85,850.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `41.92%` | `58.08%` | `0.72` | 286,080.00 USD |
| `15M` | `HTX` | `52.75%` | `47.25%` | `1.12` | 167.95 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `75.64%` | `24.36%` | `3.11` | 6,770.00 USD |
| `15M` | `Aster` | `95.71%` | `4.29%` | `22.31` | 1,250.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `83.87%` | `16.13%` | `5.20` | 3,580.00 USD |
| `15M` | `Whale Positions` | `70.12%` | `29.88%` | `2.35` | 1,570,000.00 USD |
| `15M` | `Global Accounts` | `57.40%` | `42.60%` | `1.35` | 5,350,000.00 USD |
| `1H` | `SUI` | `47.32%` | `52.68%` | `0.90` | 20,480,000.00 USD |
| `1H` | `Binance` | `50.91%` | `49.09%` | `1.04` | 5,460,000.00 USD |
| `1H` | `OKX` | `52.7%` | `47.3%` | `1.11` | 1,500,000.00 USD |
| `1H` | `Bybit` | `43.23%` | `56.77%` | `0.76` | 1,660,000.00 USD |
| `1H` | `KuCoin` | `44.4%` | `55.6%` | `0.80` | 173,680.00 USD |
| `1H` | `Gate` | `38.98%` | `61.02%` | `0.64` | 147,330.00 USD |
| `1H` | `Bitget` | `46.97%` | `53.03%` | `0.89` | 487,140.00 USD |
| `1H` | `BingX` | `49.57%` | `50.43%` | `0.98` | 513,470.00 USD |
| `1H` | `MEXC` | `49.5%` | `50.5%` | `0.98` | 7,940,000.00 USD |
| `1H` | `Bitunix` | `50.33%` | `49.67%` | `1.01` | 601,980.00 USD |
| `1H` | `Hyperliquid` | `18.81%` | `81.19%` | `0.23` | 543,150.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.38%` | `47.62%` | `1.10` | 578,420.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `14.71%` | `85.29%` | `0.17` | 673,770.00 USD |
| `1H` | `HTX` | `27.23%` | `72.77%` | `0.37` | 3,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `21.15%` | `78.85%` | `0.27` | 174,410.00 USD |
| `1H` | `Aster` | `45.14%` | `54.86%` | `0.82` | 2,910.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.4%` | `55.6%` | `0.80` | 21,390.00 USD |
| `1H` | `Whale Positions` | `50.91%` | `49.09%` | `1.04` | 5,460,000.00 USD |
| `1H` | `Global Accounts` | `47.32%` | `52.68%` | `0.90` | 20,480,000.00 USD |
| `4H` | `SUI` | `43.92%` | `56.08%` | `0.78` | 80,690,000.00 USD |
| `4H` | `Binance` | `45.14%` | `54.86%` | `0.82` | 26,230,000.00 USD |
| `4H` | `OKX` | `41.84%` | `58.16%` | `0.72` | 5,450,000.00 USD |
| `4H` | `Bybit` | `48.07%` | `51.93%` | `0.93` | 4,290,000.00 USD |
| `4H` | `KuCoin` | `50.78%` | `49.22%` | `1.03` | 713,410.00 USD |
| `4H` | `Gate` | `46.55%` | `53.45%` | `0.87` | 1,790,000.00 USD |
| `4H` | `Bitget` | `43.09%` | `56.91%` | `0.76` | 1,590,000.00 USD |
| `4H` | `BingX` | `46.32%` | `53.68%` | `0.86` | 13,490,000.00 USD |
| `4H` | `MEXC` | `48.98%` | `51.02%` | `0.96` | 4,860,000.00 USD |
| `4H` | `Bitunix` | `51.8%` | `48.2%` | `1.07` | 3,090,000.00 USD |
| `4H` | `Hyperliquid` | `61.43%` | `38.57%` | `1.59` | 811,850.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.74%` | `49.26%` | `1.03` | 12,560,000.00 USD |
| `4H` | `Crypto.com` | `83.92%` | `16.08%` | `5.22` | 14,100.00 USD |
| `4H` | `WhiteBIT` | `0.06%` | `99.94%` | `0.00` | 5,260,000.00 USD |
| `4H` | `HTX` | `27.85%` | `72.15%` | `0.39` | 25,280.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.33%` | `56.67%` | `0.76` | 265,930.00 USD |
| `4H` | `Aster` | `48.42%` | `51.58%` | `0.94` | 118,770.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `64.09%` | `35.91%` | `1.78` | 123,300.00 USD |
| `4H` | `Whale Positions` | `45.14%` | `54.86%` | `0.82` | 26,230,000.00 USD |
| `4H` | `Global Accounts` | `43.92%` | `56.08%` | `0.78` | 80,690,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9473` | `0.9468` | `0.9473` | `0.9484` | `0.9444` | 1,455,719.43 USD | 672,614.86 USD | 783,104.57 USD | -110,489.71 USD | `-7.59%` | `4B / 16S` |
| `0:00 UTC` | `0.9443` | `0.9448` | `0.9443` | `0.9482` | `0.9416` | 1,894,016.62 USD | 669,877.01 USD | 1,224,139.61 USD | -554,262.60 USD | `-29.26%` | `2B / 19S` |
| `5:00 UTC` | `0.9422` | `0.9426` | `0.9422` | `0.9456` | `0.9405` | 2,904,363.37 USD | 1,710,904.86 USD | 1,193,458.51 USD | 517,446.35 USD | `+17.82%` | `9B / 3S` |
| `0:00 UTC` | `0.9365` | `0.9385` | `0.9365` | `0.9465` | `0.9328` | 3,456,784.57 USD | 1,287,230.60 USD | 2,169,553.97 USD | -882,323.36 USD | `-25.52%` | `11B / 45S` |
| `5:00 UTC` | `0.9311` | `0.9327` | `0.9311` | `0.9364` | `0.9283` | 4,003,241.44 USD | 1,917,706.18 USD | 2,085,535.26 USD | -167,829.08 USD | `-4.19%` | `12B / 10S` |
| `0:00 UTC` | `0.9355` | `0.9352` | `0.9355` | `0.9377` | `0.9317` | 2,368,816.93 USD | 1,005,010.81 USD | 1,363,806.11 USD | -358,795.30 USD | `-15.15%` | `6B / 13S` |
| `5:00 UTC` | `0.9329` | `0.9340` | `0.9329` | `0.9372` | `0.9308` | 2,243,724.91 USD | 1,007,080.32 USD | 1,236,644.58 USD | -229,564.26 USD | `-10.23%` | `7B / 14S` |
| `0:00 UTC` | `0.9264` | `0.9272` | `0.9264` | `0.9323` | `0.9251` | 2,780,290.59 USD | 1,245,269.00 USD | 1,535,021.59 USD | -289,752.58 USD | `-10.42%` | `8B / 17S` |
| `5:00 UTC` | `0.9324` | `0.9295` | `0.9324` | `0.9329` | `0.9253` | 3,699,722.99 USD | 2,179,603.27 USD | 1,520,119.72 USD | 659,483.55 USD | `+17.83%` | `23B / 6S` |
| `0:00 UTC` | `0.9293` | `0.9297` | `0.9293` | `0.9317` | `0.9284` | 302,595.05 USD | 106,340.36 USD | 196,254.70 USD | -89,914.34 USD | `-29.71%` | `2B / 11S` |

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
| `5m` | -87,820.00 USD | -144,730.00 USD | **`DISTRIBUTION`** |
| `15m` | -58,230.00 USD | 1,080,000.00 USD | **`ACCUMULATION`** |
| `30m` | -154,110.00 USD | 1,460,000.00 USD | **`ACCUMULATION`** |
| `1h` | -472,220.00 USD | 533,680.00 USD | **`ACCUMULATION`** |
| `2h` | -353,130.00 USD | -2,700,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 2,280,000.00 USD | -7,330,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 3,670,000.00 USD | -4,090,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 4,060,000.00 USD | -5,460,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 4,400,000.00 USD | -3,980,000.00 USD | **`ACCUMULATION`** |
| `24h` | 3,190,000.00 USD | -16,710,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -14,550,000.00 USD | -65,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -142,520,000.00 USD | -467,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-87.82K` | 15m=`-58.23K` | 1h=`-472.22K` | 24h=`+3.19M`
* Futures Capital Netflows: 5m=`-144.73K` | 15m=`+1.08M` | 1h=`+533.68K` | 24h=`-16.71M`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
