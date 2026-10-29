# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:41:04 IST` (`2026-10-29 23:11:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8804` | `0.8824` | `0.8791` | `0.8813` | `731,741` | 644,347.63 USD | 91,670.69 USD | `+14.23%` | -14,871,243.04 USD | `+0.47` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.8813` | `0.8822` | `0.8726` | `0.8736` | `1,481,482` | 1,299,129.81 USD | -320,653.64 USD | `-24.68%` | -15,191,896.68 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.8736` | `0.8739` | `0.8720` | `0.8726` | `372,987` | 325,616.11 USD | -62,269.17 USD | `-19.12%` | -15,254,165.85 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8832` | `0.8897` | `0.8814` | `0.8842` | `3,338,989` | 2,957,541.44 USD | 26,581.69 USD | `+0.90%` | -14,504,165.92 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.8842` | `0.8846` | `0.8776` | `0.8813` | `4,194,194` | 3,693,620.20 USD | -415,979.42 USD | `-11.26%` | -14,920,145.34 USD | `-0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.8813` | `0.8822` | `0.8720` | `0.8731` | `1,859,086` | 1,628,775.87 USD | -378,892.86 USD | `-23.26%` | -15,299,038.20 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.8736` | `0.9001` | `0.8692` | `0.8823` | `37,030,182` | 32,817,210.50 USD | 141,157.12 USD | `+0.43%` | -15,031,283.00 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.8824` | `0.8897` | `0.8719` | `0.8813` | `20,466,724` | 18,053,055.46 USD | -77,228.34 USD | `-0.43%` | -15,108,511.33 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.8813` | `0.8822` | `0.8720` | `0.8726` | `1,854,469` | 1,624,745.92 USD | -382,922.81 USD | `-23.57%` | -15,491,434.14 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8735` | `131,076,764` | 116,346,670.62 USD | -6,318,807.08 USD | `-5.43%` | -15,481,370.60 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -8,478,733.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -8,617,968.75 USD | `+0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8735` | `131,076,764` | 116,346,670.62 USD | -6,318,807.08 USD | `-5.43%` | -15,481,370.60 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.8717` | `20682.4000` | 18,029.68 USD | 60,389.65 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `0.8717` | `4588.5000` | 3,999.89 USD | 64,389.54 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.8717` | `4655.2000` | 4,057.98 USD | 68,447.52 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `0.8718` | `19245.3000` | 16,778.24 USD | 41,861.42 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.8718` | `285.4000` | 248.80 USD | 42,110.22 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.8718` | `286.5000` | 249.76 USD | 42,359.98 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.8719` | `120.0000` | 104.63 USD | 23,330.69 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8719` | `2010.0000` | 1,752.48 USD | 25,083.17 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8720` | `126.0000` | 109.88 USD | 14,077.43 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.8720` | `5743.1000` | 5,008.21 USD | 19,085.64 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8720` | `2124.5000` | 1,852.63 USD | 20,938.27 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.8720` | `114.6000` | 99.93 USD | 21,038.21 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8720` | `500.3000` | 436.27 USD | 21,474.47 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `0.8720` | `2008.8000` | 1,751.59 USD | 23,226.07 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8721` | `6463.1000` | 5,636.66 USD | 12,215.11 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8721` | `2009.5000` | 1,752.44 USD | 13,967.55 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8722` | `400.0000` | 348.88 USD | 4,825.47 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8722` | `2009.9000` | 1,752.97 USD | 6,578.45 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8723` | `1148.3000` | 1,001.71 USD | 1,001.71 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8723` | `3983.5000` | 3,474.89 USD | 4,476.59 USD | `2 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `0.8724` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.87` | `0.00%` | `-` |
| `ASK` | `0.8726` | `1147.9000` | 1,001.67 USD | 3,553.44 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8726` | `415.4000` | 362.47 USD | 2,551.77 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8726` | `2009.0000` | 1,753.01 USD | 2,189.29 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8726` | `500.0000` | 436.28 USD | 436.28 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8727` | `2009.0000` | 1,753.25 USD | 30,569.41 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8727` | `19033.9000` | 16,610.69 USD | 28,816.16 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8727` | `742.7000` | 648.14 USD | 12,205.46 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8727` | `2295.8000` | 2,003.48 USD | 11,557.32 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8727` | `6876.0000` | 6,000.41 USD | 9,553.85 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8728` | `129.4000` | 112.94 USD | 44,127.69 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8728` | `2138.4000` | 1,866.44 USD | 44,014.74 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.8728` | `2177.9000` | 1,900.89 USD | 42,148.31 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8728` | `7663.9000` | 6,689.05 USD | 40,247.41 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.8728` | `1000.0000` | 872.77 USD | 33,558.36 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8728` | `2424.7000` | 2,116.18 USD | 32,685.59 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.8729` | `19033.9000` | 16,615.45 USD | 62,496.76 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8729` | `2009.0000` | 1,753.62 USD | 45,881.30 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8730` | `2009.0000` | 1,753.90 USD | 67,311.93 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.8730` | `2000.0000` | 1,746.00 USD | 65,558.03 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8730` | `1506.7000` | 1,315.27 USD | 63,812.03 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `675` | `0xb83d...6e36` | `SHORT` | 3,334,223.70 USD | `3,817,609.40` | `1.11` | `0.8743` | `39.88` | 884,511.62 USD | `+26.53%` | `3X Cross` |
| `1021` | `0xa2ce...3126` | `LONG` | 2,188,634.10 USD | `2,500,010.40` | `0.8597` | `0.8743` | `0.000000` | 39,427.57 USD | `+1.80%` | `10X Cross` |
| `1522` | `0x9946...0852` | `SHORT` | 1,426,250.94 USD | `1,632,538.50` | `1.08` | `0.8743` | `1.83` | 335,498.19 USD | `+23.52%` | `10X Cross` |
| `1865` | `0x9aa5...58af` | `SHORT` | 1,101,324.59 USD | `1,258,009.70` | `1.14` | `0.8743` | `8.16` | 332,006.11 USD | `+30.15%` | `10X Cross` |
| `1928` | `0x9df2...c665` | `SHORT` | 1,048,200.00 USD | `1,200,000.00` | `0.7465` | `0.8743` | `27.35` | -152,347.60 USD | `-14.53%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9261` | 34,626.23 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 34.63K USD at 0.9261 USD [API] | `2026-10-28 18:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 15.36 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.02K USD at 1.0593 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 399.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.40K USD at 1.0593 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 81.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.08K USD at 1.0591 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 81.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.08K USD at 1.0591 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 1,539.89 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.54K USD at 1.0590 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `0.9363` | 5,774.85 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.77K USD at 0.9363 USD [API] | `2026-10-28 18:40:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9376` | 5,004.60 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.00K USD at 0.9376 USD [API] | `2026-10-28 18:53:09` |
| `ANNOUNCEMENT` | `INFO` | `0.9388` | 8,271.02 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 8.27K USD at 0.9388 USD [API] | `2026-10-28 19:11:03` |
| `ANNOUNCEMENT` | `INFO` | `0.9393` | 5,075.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.08K USD at 0.9393 USD [API] | `2026-10-28 19:28:24` |
| `ANNOUNCEMENT` | `INFO` | `0.9393` | 5,340.76 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9393 USD [API] | `2026-10-28 19:28:23` |
| `ANNOUNCEMENT` | `INFO` | `0.9431` | 7,544.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 7.54K USD at 0.9431 USD [API] | `2026-10-28 19:35:13` |
| `ANNOUNCEMENT` | `INFO` | `0.9546` | 9,991.15 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 9.99K USD at 0.9546 USD [API] | `2026-10-28 20:05:10` |
| `ANNOUNCEMENT` | `INFO` | `0.9548` | 30,059.22 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 30.06K USD at 0.9548 USD [API] | `2026-10-28 20:05:10` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9682` (Vol: 265,800.00 USD, Dist: `+9.98%`) | Long MP=`0.8652` (Vol: 230,900.00 USD, Dist: `--1.72%`)
  * 48H Horizon: Short MP=`0.9707` (Vol: 232,500.00 USD, Dist: `+10.26%`) | Long MP=`0.8657` (Vol: 154,300.00 USD, Dist: `--1.67%`)
  * 3D Horizon: Short MP=`0.9707` (Vol: 232,500.00 USD, Dist: `+10.26%`) | Long MP=`0.8657` (Vol: 154,300.00 USD, Dist: `--1.67%`)
  * 7D Horizon: Short MP=`0.9713` (Vol: 513,800.00 USD, Dist: `+10.32%`) | Long MP=`0.8660` (Vol: 154,300.00 USD, Dist: `--1.64%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1905` | 190.50 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 193.08 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 439.89 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 4,420.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 1,620.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 2,460.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 169.17 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 272.15 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 161.52 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2715` | 3,310.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 116.88 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 24,760.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 687.92 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 603.12 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3085` | 102.08 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3205` | 581.03 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3255` | 203.44 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3385` | 3,390.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3395` | 101.85 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3615` | 28,090.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3655` | 407.57 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 4,070.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3815` | 6,490.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 27,340.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 952.42 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 10,610.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 749.73 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4285` | 299.95 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4315` | 226.28 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 5,600.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4405` | 47,620.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4415` | 5,800.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 375.15 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 26,830.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 14,430.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 702.74 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 295.78 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 2,110.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 3,890.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 1,720.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4765` | 2,880.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 507.64 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 535.86 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 5,690.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 1,050.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 3,600.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 365.24 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5005` | 100.75 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 716.75 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 2,030.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 1,560.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 1,070.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5235` | 14,910.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 5,280.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5255` | 128.85 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 125,730.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 264.06 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 417.12 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 8,200.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 9,620.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5435` | 5,900.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,780.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 413.21 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 441.84 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 330.53 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 195.93 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 570.01 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 18,580.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5685` | 4,540.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 182.72 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 1,010.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 119.34 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,760.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5875` | 969.32 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 608.61 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 694.58 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 19,000.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 323.79 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 272.24 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6105` | 663.43 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 16,020.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 213.64 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 357.73 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 3,600.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 18,790.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,170.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 13,910.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 1,050.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6215` | 19,270.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 619.32 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,070.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 3,510.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 843.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 130.62 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6385` | 309.35 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6395` | 321,670.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 939.17 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 1,260.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 657.79 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 3,910.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 668.34 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 721.59 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 1,820.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 126,530.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 509.46 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 676.54 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 8,220.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 10,820.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 788.97 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6635` | 2,160.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 186.02 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 6,810.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 2,810.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 8,500.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 29,400.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 6,780.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 250.77 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 45,130.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 3,550.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 135,750.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 11,170.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,790.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 480.49 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 83,790.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,230.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 2,980.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 722.28 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 1,150.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 2,400.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 1,930.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 759.59 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 769.59 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 787.73 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,020.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 2,720.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 3,530.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 569.20 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 272.53 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 3,530.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 9,190.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 11,250.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 129.26 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 2,660.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 1,180.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 762.57 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 214.03 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 26,490.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 1,030.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 724.11 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 533.01 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 14,950.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 5,810.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 1,260.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 6,330.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 784,090.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 421.12 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 105.64 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 2,160.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 103,410.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7485` | 105.91 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 106.03 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 264.86 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 2,190.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 440.08 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7565` | 438.54 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 36,710.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,390.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7625` | 859.11 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 11,980,000.00 USD | 11,980,000.00 USD | 37,590.00 USD | 14,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 320,810.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 3,510.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 11,930,000.00 USD | 11,930,000.00 USD | 556.58 USD | 23,090.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,420.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 11,890,000.00 USD | 11,890,000.00 USD | 1,280.00 USD | 177.87 USD | 19,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 10,200.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 499.99 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 11,870,000.00 USD | 11,870,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 153,870.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 4,350.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 11,870,000.00 USD | 11,870,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 338.38 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 2,950.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 4,570.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 4,130.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 21,370.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 6,450.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 11,870,000.00 USD | 11,870,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 28,280.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7810` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 185.50 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 13,880.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7825` | 15,670.00 USD | 990,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 0.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 1,720.00 USD | 975,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7850` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7855` | 3,020.00 USD | 973,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 2,870.00 USD | 970,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7870` | 5,540,000.00 USD | 5,540,000.00 USD | 16,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7870` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 5,970.00 USD | 967,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7890` | 5,520,000.00 USD | 5,520,000.00 USD | 10,020.00 USD | 12,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 11,400.00 USD | 326.97 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 2,530.00 USD | 961,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,870.00 USD | 959,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7910` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 4,440.00 USD | 285.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 29,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 5,470.00 USD | 955,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7925` | 3,930.00 USD | 949,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7930` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 9,580.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 12,880.00 USD | 77,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 7,640.00 USD | 945,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7950` | 5,460,000.00 USD | 5,460,000.00 USD | 13,930.00 USD | 266.53 USD | 14,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 18,870.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 23,610.00 USD | 938,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 5,430,000.00 USD | 5,430,000.00 USD | 3,300.00 USD | 9,330.00 USD | 22,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 11,620,000.00 USD | 11,620,000.00 USD | 12,100.00 USD | 0.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 1,170.00 USD | 914,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7990` | 5,390,000.00 USD | 5,390,000.00 USD | 505.25 USD | 322.55 USD | 18,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 11,570,000.00 USD | 11,570,000.00 USD | 488.55 USD | 0.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 2,580.00 USD | 913,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8005` | 635.04 USD | 910,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8010` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 10,940.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 11,560,000.00 USD | 11,560,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 7,130.00 USD | 910,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 79,510.00 USD | 903,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 34,400.00 USD | 823,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8050` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 6,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 11,510,000.00 USD | 11,510,000.00 USD | 2,040.00 USD | 15,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 266.62 USD | 789,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 5,340,000.00 USD | 5,340,000.00 USD | 12,740.00 USD | 14,260.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,760.00 USD | 788,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 786,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8090` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 2,210.00 USD | 763,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 761,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8110` | 5,300,000.00 USD | 5,300,000.00 USD | 40,190.00 USD | 6,030.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 11,480,000.00 USD | 11,480,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 1,390.00 USD | 759,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8125` | 54,950.00 USD | 758,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8130` | 5,220,000.00 USD | 5,220,000.00 USD | 23,290.00 USD | 12,500.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 11,380,000.00 USD | 11,380,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 8,130.00 USD | 703,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8145` | 2,200.00 USD | 695,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 5,180,000.00 USD | 5,180,000.00 USD | 66,820.00 USD | 24,820.00 USD | 100,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8150` | 11,300,000.00 USD | 11,300,000.00 USD | 135,770.00 USD | 50,280.00 USD | 125,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 24,220.00 USD | 692,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8165` | 104.92 USD | 668,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8170` | 4,990,000.00 USD | 4,990,000.00 USD | 67,220.00 USD | 28,480.00 USD | 79,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 10,990,000.00 USD | 10,990,000.00 USD | 91,050.00 USD | 23,590.00 USD | 82,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 103,450.00 USD | 668,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8185` | 2,230.00 USD | 565,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8190` | 4,820,000.00 USD | 4,820,000.00 USD | 12,140.00 USD | 6,030.00 USD | 15,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 10,790,000.00 USD | 10,790,000.00 USD | 195,400.00 USD | 53,380.00 USD | 47,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 2,830.00 USD | 562,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 559,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8210` | 4,780,000.00 USD | 4,780,000.00 USD | 16,970.00 USD | 30,390.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 10,500,000.00 USD | 10,500,000.00 USD | 138,580.00 USD | 56,860.00 USD | 152,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 6,650.00 USD | 557,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8225` | 466.85 USD | 551,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 4,690,000.00 USD | 4,690,000.00 USD | 11,730.00 USD | 18,140.00 USD | 20,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 10,150,000.00 USD | 10,150,000.00 USD | 37,880.00 USD | 37,160.00 USD | 63,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 45,230.00 USD | 550,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8245` | 17,700.00 USD | 505,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 4,640,000.00 USD | 4,640,000.00 USD | 18,440.00 USD | 8,600.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 10,010,000.00 USD | 10,010,000.00 USD | 187,510.00 USD | 30,370.00 USD | 126,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 5,300.00 USD | 487,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8270` | 4,590,000.00 USD | 4,590,000.00 USD | 29,570.00 USD | 9,330.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 9,670,000.00 USD | 9,670,000.00 USD | 147,770.00 USD | 51,050.00 USD | 62,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 16,090.00 USD | 482,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8285` | 137,340.00 USD | 466,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8290` | 4,540,000.00 USD | 4,540,000.00 USD | 12,280.00 USD | 15,250.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 9,410,000.00 USD | 9,410,000.00 USD | 89,470.00 USD | 40,370.00 USD | 82,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 24,330.00 USD | 328,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8305` | 2,460.00 USD | 304,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8310` | 4,460,000.00 USD | 4,460,000.00 USD | 24,960.00 USD | 21,850.00 USD | 59,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 9,190,000.00 USD | 9,190,000.00 USD | 36,870.00 USD | 32,050.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8315` | 3,340.00 USD | 302,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8325` | 12,370.00 USD | 298,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8330` | 4,360,000.00 USD | 4,360,000.00 USD | 42,250.00 USD | 23,450.00 USD | 42,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 9,100,000.00 USD | 9,100,000.00 USD | 150,740.00 USD | 85,780.00 USD | 207,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8335` | 5,100.00 USD | 286,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8345` | 11,360.00 USD | 281,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8350` | 4,250,000.00 USD | 4,250,000.00 USD | 23,790.00 USD | 18,810.00 USD | 22,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 8,660,000.00 USD | 8,660,000.00 USD | 77,100.00 USD | 17,250.00 USD | 82,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 2,890.00 USD | 269,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8365` | 57,620.00 USD | 267,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 4,180,000.00 USD | 4,180,000.00 USD | 85,240.00 USD | 18,990.00 USD | 30,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 8,480,000.00 USD | 8,480,000.00 USD | 146,890.00 USD | 62,180.00 USD | 103,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 2,190.00 USD | 209,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8385` | 77,770.00 USD | 207,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8390` | 4,050,000.00 USD | 4,050,000.00 USD | 70,320.00 USD | 30,700.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 8,170,000.00 USD | 8,170,000.00 USD | 24,790.00 USD | 89,740.00 USD | 77,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 26,310.00 USD | 129,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8405` | 692.74 USD | 103,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8410` | 3,910,000.00 USD | 3,910,000.00 USD | 79,140.00 USD | 23,550.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 7,980,000.00 USD | 7,980,000.00 USD | 59,670.00 USD | 41,980.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 4,730.00 USD | 102,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8425` | 2,340.00 USD | 97,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 3,780,000.00 USD | 3,780,000.00 USD | 29,850.00 USD | 50,900.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 7,850,000.00 USD | 7,850,000.00 USD | 81,850.00 USD | 112,960.00 USD | 31,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 3,340.00 USD | 95,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8445` | 598.67 USD | 92,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8450` | 3,680,000.00 USD | 3,680,000.00 USD | 11,600.00 USD | 34,120.00 USD | 115,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 7,620,000.00 USD | 7,620,000.00 USD | 43,800.00 USD | 115,170.00 USD | 220,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 15,800.00 USD | 91,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8465` | 15,120.00 USD | 75,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8470` | 3,510,000.00 USD | 3,510,000.00 USD | 62,880.00 USD | 66,780.00 USD | 87,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 7,240,000.00 USD | 7,240,000.00 USD | 27,720.00 USD | 6,020.00 USD | 33,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 10,800.00 USD | 60,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,380.00 USD | 49,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8490` | 3,300,000.00 USD | 3,300,000.00 USD | 69,150.00 USD | 70,780.00 USD | 180,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 7,170,000.00 USD | 7,170,000.00 USD | 87,880.00 USD | 78,940.00 USD | 150,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 804.99 USD | 48,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8505` | 9,470.00 USD | 47,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 2,980,000.00 USD | 2,980,000.00 USD | 84,100.00 USD | 61,520.00 USD | 65,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 6,860,000.00 USD | 6,860,000.00 USD | 95,990.00 USD | 42,650.00 USD | 149,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 38,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8525` | 1,260.00 USD | 36,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8530` | 2,770,000.00 USD | 2,770,000.00 USD | 83,020.00 USD | 52,480.00 USD | 103,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 6,570,000.00 USD | 6,570,000.00 USD | 30,570.00 USD | 52,520.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 15,640.00 USD | 35,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8545` | 784.69 USD | 19,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8550` | 2,530,000.00 USD | 2,530,000.00 USD | 58,930.00 USD | 11,700.00 USD | 17,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 6,460,000.00 USD | 6,460,000.00 USD | 78,320.00 USD | 63,400.00 USD | 93,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8555` | 17,220.00 USD | 19,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,440,000.00 USD | 2,440,000.00 USD | 106,410.00 USD | 33,070.00 USD | 124.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 6,220,000.00 USD | 6,220,000.00 USD | 99,680.00 USD | 166,050.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 1,170.00 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,300,000.00 USD | 2,300,000.00 USD | 144,580.00 USD | 97,280.00 USD | 31,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 5,950,000.00 USD | 5,950,000.00 USD | 51,400.00 USD | 69,250.00 USD | 19,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 793.58 USD | 793.58 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,030,000.00 USD | 2,030,000.00 USD | 37,090.00 USD | 47,640.00 USD | 641.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 5,810,000.00 USD | 5,810,000.00 USD | 36,870.00 USD | 174,840.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 1,940,000.00 USD | 1,940,000.00 USD | 53,710.00 USD | 122,930.00 USD | 278,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 5,570,000.00 USD | 5,570,000.00 USD | 30,710.00 USD | 78,200.00 USD | 394,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8650` | 1,480,000.00 USD | 1,480,000.00 USD | 248,690.00 USD | 34,470.00 USD | 72,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 5,070,000.00 USD | 5,070,000.00 USD | 313,070.00 USD | 110,550.00 USD | 308,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8670` | 1,130,000.00 USD | 1,130,000.00 USD | 41,460.00 USD | 20,170.00 USD | 125.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 4,330,000.00 USD | 4,330,000.00 USD | 159,120.00 USD | 41,080.00 USD | 50,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,070,000.00 USD | 1,070,000.00 USD | 148,850.00 USD | 87,020.00 USD | 112,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 4,080,000.00 USD | 4,080,000.00 USD | 182,190.00 USD | 9,930.00 USD | 417,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 718,120.00 USD | 718,120.00 USD | 93,860.00 USD | 58,480.00 USD | 349,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 3,480,000.00 USD | 3,480,000.00 USD | 604,760.00 USD | 13,020.00 USD | 393,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 215,780.00 USD | 215,780.00 USD | 0.00 USD | 0.00 USD | 74,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 2,460,000.00 USD | 2,460,000.00 USD | 333,320.00 USD | 78,000.00 USD | 387,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 140,900.00 USD | 140,900.00 USD | 0.00 USD | 19,580.00 USD | 103,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,670,000.00 USD | 1,670,000.00 USD | 643,280.00 USD | 7,500.00 USD | 318,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 17,760.00 USD | 17,760.00 USD | 5,200.00 USD | 0.00 USD | 83.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 695,720.00 USD | 695,720.00 USD | 398,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 12,470.00 USD | 12,470.00 USD | 6,560.00 USD | 0.00 USD | 222.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 296,940.00 USD | 296,940.00 USD | 296,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 5,690.00 USD | 5,690.00 USD | 5,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8810` | 26,040.00 USD | 26,040.00 USD | 26,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8810` | 52,090.00 USD | 52,090.00 USD | 26,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8830` | 1,230.00 USD | 1,230.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8830` | 79,970.00 USD | 79,970.00 USD | 27,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8850` | 3,270.00 USD | 3,270.00 USD | 0.00 USD | 0.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8870` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | 530.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8890` | 969,280.00 USD | 969,280.00 USD | 884,290.00 USD | 0.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8910` | 190,200.00 USD | 190,200.00 USD | 186,060.00 USD | 0.00 USD | 347.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8910` | 1,780,000.00 USD | 1,780,000.00 USD | 806,690.00 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8930` | 234,860.00 USD | 234,860.00 USD | 44,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8930` | 3,550,000.00 USD | 3,550,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8950` | 414,090.00 USD | 414,090.00 USD | 98,920.00 USD | 48,760.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 4,320,000.00 USD | 4,320,000.00 USD | 719,730.00 USD | 56,980.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8970` | 436,310.00 USD | 436,310.00 USD | 0.00 USD | 22,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8970` | 5,040,000.00 USD | 5,040,000.00 USD | 659,500.00 USD | 54,550.00 USD | 470.27 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8990` | 893,680.00 USD | 893,680.00 USD | 51,680.00 USD | 127,660.00 USD | 278,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8990` | 5,750,000.00 USD | 5,750,000.00 USD | 308,910.00 USD | 64,400.00 USD | 341,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9010` | 1,470,000.00 USD | 1,470,000.00 USD | 249,240.00 USD | 99,300.00 USD | 230,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 6,280,000.00 USD | 6,280,000.00 USD | 207,550.00 USD | 109,410.00 USD | 215,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9030` | 1,610,000.00 USD | 1,610,000.00 USD | 3,140.00 USD | 76,840.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9030` | 6,370,000.00 USD | 6,370,000.00 USD | 5,880.00 USD | 78,550.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9050` | 2,000,000.00 USD | 2,000,000.00 USD | 144,360.00 USD | 134,060.00 USD | 111,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9050` | 6,710,000.00 USD | 6,710,000.00 USD | 122,230.00 USD | 0.00 USD | 219,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9070` | 2,340,000.00 USD | 2,340,000.00 USD | 111,680.00 USD | 55,120.00 USD | 175,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 7,050,000.00 USD | 7,050,000.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9090` | 2,520,000.00 USD | 2,520,000.00 USD | 167,160.00 USD | 6,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 7,400,000.00 USD | 7,400,000.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9110` | 2,620,000.00 USD | 2,620,000.00 USD | 70,890.00 USD | 34,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 7,710,000.00 USD | 7,710,000.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9130` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 62,740.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 7,860,000.00 USD | 7,860,000.00 USD | 80,230.00 USD | 62,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9150` | 3,210,000.00 USD | 3,210,000.00 USD | 119,590.00 USD | 91,680.00 USD | 299,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 8,250,000.00 USD | 8,250,000.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9170` | 3,470,000.00 USD | 3,470,000.00 USD | 106,060.00 USD | 94,830.00 USD | 62,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 8,370,000.00 USD | 8,370,000.00 USD | 123,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9175` | 3,550.00 USD | 3,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9190` | 3,560,000.00 USD | 3,560,000.00 USD | 25,950.00 USD | 26,670.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 8,830,000.00 USD | 8,830,000.00 USD | 296,480.00 USD | 60,800.00 USD | 104,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9210` | 3,790,000.00 USD | 3,790,000.00 USD | 47,610.00 USD | 60,370.00 USD | 128,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 9,160,000.00 USD | 9,160,000.00 USD | 128,930.00 USD | 16,660.00 USD | 178,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9230` | 4,370,000.00 USD | 4,370,000.00 USD | 230,840.00 USD | 75,900.00 USD | 272,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 9,620,000.00 USD | 9,620,000.00 USD | 51,510.00 USD | 66,370.00 USD | 341,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9250` | 4,730,000.00 USD | 4,730,000.00 USD | 195,300.00 USD | 37,890.00 USD | 123,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 9,780,000.00 USD | 9,780,000.00 USD | 52,570.00 USD | 43,650.00 USD | 67,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9255` | 5,860.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9270` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 99,610.00 USD | 64,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 10,120,000.00 USD | 10,120,000.00 USD | 209,950.00 USD | 40,600.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9290` | 5,040,000.00 USD | 5,040,000.00 USD | 38,710.00 USD | 20,700.00 USD | 88,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 10,180,000.00 USD | 10,180,000.00 USD | 4,480.00 USD | 53,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9305` | 1,840.00 USD | 11,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9310` | 5,250,000.00 USD | 5,250,000.00 USD | 104,570.00 USD | 67,100.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 10,570,000.00 USD | 10,570,000.00 USD | 177,720.00 USD | 46,670.00 USD | 166,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9315` | 397.84 USD | 11,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9325` | 900.70 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9330` | 5,360,000.00 USD | 5,360,000.00 USD | 32,530.00 USD | 38,720.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 76,570.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9335` | 1,020.00 USD | 13,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9345` | 115.04 USD | 13,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9350` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 13,120.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 10,820,000.00 USD | 10,820,000.00 USD | 53,950.00 USD | 54,380.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9370` | 5,920,000.00 USD | 5,920,000.00 USD | 198,110.00 USD | 84,650.00 USD | 261,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 11,120,000.00 USD | 11,120,000.00 USD | 251,760.00 USD | 1,370.00 USD | 42,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 3,670.00 USD | 17,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9390` | 6,320,000.00 USD | 6,320,000.00 USD | 171,940.00 USD | 72,440.00 USD | 153,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 11,500,000.00 USD | 11,500,000.00 USD | 86,850.00 USD | 34,800.00 USD | 263,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9395` | 3,560.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9410` | 6,430,000.00 USD | 6,430,000.00 USD | 52,890.00 USD | 4,990.00 USD | 55,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 11,630,000.00 USD | 11,630,000.00 USD | 123,000.00 USD | 2,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 6,450,000.00 USD | 6,450,000.00 USD | 702.40 USD | 3,090.00 USD | 17,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 66,560.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9450` | 6,770,000.00 USD | 6,770,000.00 USD | 6,770.00 USD | 76,490.00 USD | 234,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 12,070,000.00 USD | 12,070,000.00 USD | 3,360.00 USD | 244,270.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 6,960,000.00 USD | 6,960,000.00 USD | 92,510.00 USD | 52,870.00 USD | 44,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 12,280,000.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 7,150,000.00 USD | 7,150,000.00 USD | 71,990.00 USD | 62,590.00 USD | 58,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 107,340.00 USD | 119,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 7,430,000.00 USD | 7,430,000.00 USD | 53,450.00 USD | 49,760.00 USD | 175,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 13,330,000.00 USD | 13,330,000.00 USD | 2,840.00 USD | 88,970.00 USD | 733,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 7,620,000.00 USD | 7,620,000.00 USD | 32,500.00 USD | 26,060.00 USD | 129,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 1,270.00 USD | 2,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 7,790,000.00 USD | 7,790,000.00 USD | 50,010.00 USD | 82,110.00 USD | 35,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 13,470,000.00 USD | 13,470,000.00 USD | 74,980.00 USD | 2,400.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 7,800,000.00 USD | 7,800,000.00 USD | 8,380.00 USD | 2,420.00 USD | 159.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 13,940,000.00 USD | 13,940,000.00 USD | 463,830.00 USD | 3,460.00 USD | 951.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 7,880,000.00 USD | 7,880,000.00 USD | 33,930.00 USD | 53,240.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 14,500,000.00 USD | 14,500,000.00 USD | 562,050.00 USD | 1,040.00 USD | 344.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 8,510,000.00 USD | 8,510,000.00 USD | 216,120.00 USD | 122,820.00 USD | 290,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 15,870,000.00 USD | 15,870,000.00 USD | 698,570.00 USD | 190,470.00 USD | 479,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 9,110,000.00 USD | 9,110,000.00 USD | 352,690.00 USD | 93,850.00 USD | 147,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 17,370,000.00 USD | 17,370,000.00 USD | 579,300.00 USD | 301,610.00 USD | 619,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 9,500,000.00 USD | 9,500,000.00 USD | 168,910.00 USD | 139,810.00 USD | 82,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 18,950,000.00 USD | 18,950,000.00 USD | 857,470.00 USD | 312,610.00 USD | 411,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 10,120,000.00 USD | 10,120,000.00 USD | 264,730.00 USD | 113,900.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 21,110,000.00 USD | 21,110,000.00 USD | 889,580.00 USD | 555,340.00 USD | 708,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 24,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9690` | 10,680,000.00 USD | 10,680,000.00 USD | 235,940.00 USD | 92,380.00 USD | 239,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 22,550,000.00 USD | 22,550,000.00 USD | 596,350.00 USD | 356,560.00 USD | 489,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 89,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9710` | 11,040,000.00 USD | 11,040,000.00 USD | 170,370.00 USD | 69,530.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 23,650,000.00 USD | 23,650,000.00 USD | 645,500.00 USD | 319,140.00 USD | 133,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 11,260,000.00 USD | 11,260,000.00 USD | 80,510.00 USD | 64,370.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 24,440,000.00 USD | 24,440,000.00 USD | 456,990.00 USD | 160,420.00 USD | 172,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9745` | 3,950.00 USD | 93,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9750` | 11,460,000.00 USD | 11,460,000.00 USD | 58,820.00 USD | 45,650.00 USD | 103,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 25,150,000.00 USD | 25,150,000.00 USD | 203,760.00 USD | 293,590.00 USD | 216,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 11,530,000.00 USD | 11,530,000.00 USD | 15,370.00 USD | 8,230.00 USD | 42,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 26,200,000.00 USD | 26,200,000.00 USD | 329,170.00 USD | 211,000.00 USD | 503,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9775` | 100.88 USD | 93,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9790` | 11,700,000.00 USD | 11,700,000.00 USD | 23,820.00 USD | 40,710.00 USD | 105,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 26,930,000.00 USD | 26,930,000.00 USD | 411,780.00 USD | 99,560.00 USD | 221,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 94,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 11,970,000.00 USD | 11,970,000.00 USD | 112,160.00 USD | 50,080.00 USD | 103,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 27,440,000.00 USD | 27,440,000.00 USD | 264,890.00 USD | 83,040.00 USD | 168,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 12,140,000.00 USD | 12,140,000.00 USD | 106,220.00 USD | 40,920.00 USD | 29,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 28,030,000.00 USD | 28,030,000.00 USD | 262,900.00 USD | 116,030.00 USD | 203,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 12,220,000.00 USD | 12,220,000.00 USD | 22,370.00 USD | 48,410.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 28,430,000.00 USD | 28,430,000.00 USD | 234,160.00 USD | 58,210.00 USD | 114,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 12,410,000.00 USD | 12,410,000.00 USD | 56,760.00 USD | 31,630.00 USD | 97,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 28,950,000.00 USD | 28,950,000.00 USD | 248,980.00 USD | 203,100.00 USD | 65,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,930.00 USD | 99,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9890` | 12,570,000.00 USD | 12,570,000.00 USD | 100,670.00 USD | 33,650.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 29,240,000.00 USD | 29,240,000.00 USD | 194,850.00 USD | 78,280.00 USD | 16,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 1,570.00 USD | 100,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9910` | 12,740,000.00 USD | 12,740,000.00 USD | 80,470.00 USD | 30,860.00 USD | 51,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 29,610,000.00 USD | 29,610,000.00 USD | 198,890.00 USD | 89,640.00 USD | 78,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,420.00 USD | 103,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9930` | 12,800,000.00 USD | 12,800,000.00 USD | 33,580.00 USD | 16,590.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 29,980,000.00 USD | 29,980,000.00 USD | 228,340.00 USD | 63,950.00 USD | 76,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 30,300,000.00 USD | 30,300,000.00 USD | 48,120.00 USD | 138,500.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 30,950,000.00 USD | 30,950,000.00 USD | 215,040.00 USD | 81,210.00 USD | 356,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 31,230,000.00 USD | 31,230,000.00 USD | 145,170.00 USD | 35,870.00 USD | 101,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,670,000.00 USD | 31,670,000.00 USD | 202,970.00 USD | 57,170.00 USD | 181,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 103,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,170,000.00 USD | 32,170,000.00 USD | 226,340.00 USD | 61,540.00 USD | 207,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,320,000.00 USD | 32,320,000.00 USD | 51,930.00 USD | 39,560.00 USD | 64,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 32,810,000.00 USD | 32,810,000.00 USD | 256,020.00 USD | 15,900.00 USD | 211,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 33,410,000.00 USD | 33,410,000.00 USD | 247,480.00 USD | 105,290.00 USD | 248,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,200,000.00 USD | 34,200,000.00 USD | 398,890.00 USD | 134,240.00 USD | 260,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,910,000.00 USD | 34,910,000.00 USD | 188,370.00 USD | 177,300.00 USD | 341,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 35,260,000.00 USD | 35,260,000.00 USD | 168,660.00 USD | 59,720.00 USD | 124,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 103,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 36,020,000.00 USD | 36,020,000.00 USD | 300,680.00 USD | 97,830.00 USD | 359,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 36,860,000.00 USD | 36,860,000.00 USD | 291,360.00 USD | 74,810.00 USD | 471,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 37,290,000.00 USD | 37,290,000.00 USD | 153,580.00 USD | 41,370.00 USD | 234,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 37,600,000.00 USD | 37,600,000.00 USD | 151,650.00 USD | 60,000.00 USD | 103,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 37,830,000.00 USD | 37,830,000.00 USD | 75,770.00 USD | 54,210.00 USD | 94,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 38,080,000.00 USD | 38,080,000.00 USD | 104,260.00 USD | 35,230.00 USD | 111,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 38,290,000.00 USD | 38,290,000.00 USD | 85,920.00 USD | 56,310.00 USD | 66,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 38,640,000.00 USD | 38,640,000.00 USD | 168,010.00 USD | 58,600.00 USD | 128,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 38,970,000.00 USD | 38,970,000.00 USD | 57,570.00 USD | 103,690.00 USD | 164,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 39,110,000.00 USD | 39,110,000.00 USD | 64,880.00 USD | 13,040.00 USD | 63,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,480,000.00 USD | 39,480,000.00 USD | 156,670.00 USD | 38,980.00 USD | 180,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 39,790,000.00 USD | 39,790,000.00 USD | 110,420.00 USD | 18,150.00 USD | 175,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 155.92 USD | 103,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 103,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 40,020,000.00 USD | 40,020,000.00 USD | 102,550.00 USD | 52,580.00 USD | 72,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 40,110,000.00 USD | 40,110,000.00 USD | 18,340.00 USD | 48,310.00 USD | 25,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 40,190,000.00 USD | 40,190,000.00 USD | 67,080.00 USD | 17,210.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,300,000.00 USD | 40,300,000.00 USD | 76,550.00 USD | 30,790.00 USD | 327.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,370,000.00 USD | 40,370,000.00 USD | 35,930.00 USD | 20,630.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 104,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,400,000.00 USD | 40,400,000.00 USD | 22,610.00 USD | 0.00 USD | 390.75 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 106,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,480,000.00 USD | 40,480,000.00 USD | 8,370.00 USD | 46,830.00 USD | 28,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 107,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 40,540,000.00 USD | 40,540,000.00 USD | 1,650.00 USD | 9,420.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 217.64 USD | 107,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,570,000.00 USD | 40,570,000.00 USD | 5,290.00 USD | 2,060.00 USD | 21,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,570,000.00 USD | 40,570,000.00 USD | 0.00 USD | 638.17 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,620,000.00 USD | 40,620,000.00 USD | 16,370.00 USD | 3,040.00 USD | 32,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,630,000.00 USD | 40,630,000.00 USD | 11,330.00 USD | 0.00 USD | 204.99 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 40,640,000.00 USD | 40,640,000.00 USD | 5,370.00 USD | 1,110.00 USD | 461.79 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 40,640,000.00 USD | 40,640,000.00 USD | 0.00 USD | 1,120.00 USD | 146.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 40,670,000.00 USD | 40,670,000.00 USD | 2,410.00 USD | 12,740.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 111,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 166.43 USD | 111,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 116,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 117,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 117,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 140,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 418.33 USD | 141,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 1,370.00 USD | 142,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 143,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 1,450.00 USD | 144,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 5,120.00 USD | 149,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 253.69 USD | 149,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 147.43 USD | 150,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 154,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 154,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 157,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 4,840.00 USD | 162,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.27` | 2,090.00 USD | 164,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 166,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 206,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 206,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 207,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 635.85 USD | 207,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 208,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 240,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 10,060.00 USD | 250,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 256,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 278,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 358.30 USD | 278,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,520.00 USD | 280,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 287,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 1,110.00 USD | 288,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 21,850.00 USD | 310,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 668,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 672,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 673,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 673,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 498.36 USD | 674,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 9,700.00 USD | 683,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 687,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 440.55 USD | 688,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 17,130.00 USD | 705,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 705,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 132.03 USD | 705,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 706,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 727,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 7,680.00 USD | 735,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,090.00 USD | 774,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 165.81 USD | 774,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 292,630.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 951.86 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 2,310.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 9,620.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 455.05 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 6,990.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1925` | 4,850,000.00 USD | 0.00 USD | 959.59 USD | `-78.14%` | `4,984.90` |
| `Live` | `Long` | `0.1995` | 4,850,000.00 USD | 0.00 USD | 256.00 USD | `-77.35%` | `1,283.20` |
| `Live` | `Long` | `0.2065` | 4,850,000.00 USD | 0.00 USD | 293.13 USD | `-76.55%` | `1,419.50` |
| `Live` | `Long` | `0.2095` | 4,850,000.00 USD | 0.00 USD | 2,790.00 USD | `-76.21%` | `13,310.50` |
| `Live` | `Long` | `0.2135` | 4,840,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.76%` | `18,919.90` |
| `Live` | `Long` | `0.2355` | 4,840,000.00 USD | 0.00 USD | 789.66 USD | `-73.26%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,840,000.00 USD | 0.00 USD | 429.28 USD | `-72.92%` | `1,799.90` |
| `Live` | `Long` | `0.2415` | 4,840,000.00 USD | 0.00 USD | 516.95 USD | `-72.58%` | `2,140.60` |
| `Live` | `Long` | `0.2495` | 4,840,000.00 USD | 0.00 USD | 242.69 USD | `-71.67%` | `972.70` |
| `Live` | `Long` | `0.2525` | 4,840,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.33%` | `8,897.00` |
| `Live` | `Long` | `0.2575` | 4,830,000.00 USD | 0.00 USD | 2,610.00 USD | `-70.76%` | `10,152.10` |
| `Live` | `Long` | `0.2635` | 4,830,000.00 USD | 0.00 USD | 496.17 USD | `-70.08%` | `1,883.00` |
| `Live` | `Long` | `0.2665` | 4,830,000.00 USD | 0.00 USD | 173.07 USD | `-69.74%` | `649.40` |
| `Live` | `Long` | `0.2685` | 4,830,000.00 USD | 0.00 USD | 106.16 USD | `-69.51%` | `395.40` |
| `Live` | `Long` | `0.2735` | 4,830,000.00 USD | 0.00 USD | 248.34 USD | `-68.94%` | `908.00` |
| `Live` | `Long` | `0.2875` | 4,830,000.00 USD | 0.00 USD | 163.65 USD | `-67.35%` | `569.20` |
| `Live` | `Long` | `0.2885` | 4,830,000.00 USD | 0.00 USD | 29,070.00 USD | `-67.24%` | `100,768.40` |
| `Live` | `Long` | `0.2905` | 4,800,000.00 USD | 0.00 USD | 118.93 USD | `-67.01%` | `409.40` |
| `Live` | `Long` | `0.2945` | 4,800,000.00 USD | 0.00 USD | 687.92 USD | `-66.56%` | `2,335.90` |
| `Live` | `Long` | `0.2975` | 4,800,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.22%` | `14,561.30` |
| `Live` | `Long` | `0.3045` | 4,800,000.00 USD | 0.00 USD | 28,270.00 USD | `-65.42%` | `92,842.40` |
| `Live` | `Long` | `0.3105` | 4,770,000.00 USD | 0.00 USD | 102.74 USD | `-64.74%` | `330.90` |
| `Live` | `Long` | `0.3115` | 4,770,000.00 USD | 0.00 USD | 270.38 USD | `-64.63%` | `868.00` |
| `Live` | `Long` | `0.3165` | 4,770,000.00 USD | 0.00 USD | 195.66 USD | `-64.06%` | `618.20` |
| `Live` | `Long` | `0.3175` | 4,770,000.00 USD | 0.00 USD | 635.13 USD | `-63.95%` | `2,000.40` |
| `Live` | `Long` | `0.3185` | 4,770,000.00 USD | 0.00 USD | 190.18 USD | `-63.83%` | `597.10` |
| `Live` | `Long` | `0.3255` | 4,770,000.00 USD | 0.00 USD | 203.44 USD | `-63.04%` | `625.00` |
| `Live` | `Long` | `0.3405` | 4,770,000.00 USD | 0.00 USD | 4,150.00 USD | `-61.34%` | `12,176.00` |
| `Live` | `Long` | `0.3425` | 4,760,000.00 USD | 0.00 USD | 3,430.00 USD | `-61.11%` | `10,000.00` |
| `Live` | `Long` | `0.3475` | 4,760,000.00 USD | 0.00 USD | 125.62 USD | `-60.54%` | `361.50` |
| `Live` | `Long` | `0.3505` | 4,760,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.20%` | `2,908.00` |
| `Live` | `Long` | `0.3585` | 4,760,000.00 USD | 0.00 USD | 4,570.00 USD | `-59.29%` | `12,739.50` |
| `Live` | `Long` | `0.3605` | 4,750,000.00 USD | 0.00 USD | 653.55 USD | `-59.07%` | `1,812.90` |
| `Live` | `Long` | `0.3665` | 4,750,000.00 USD | 0.00 USD | 274.88 USD | `-58.38%` | `750.00` |
| `Live` | `Long` | `0.3795` | 4,750,000.00 USD | 0.00 USD | 278.02 USD | `-56.91%` | `732.60` |
| `Live` | `Long` | `0.3815` | 4,750,000.00 USD | 0.00 USD | 6,490.00 USD | `-56.68%` | `17,000.00` |
| `Live` | `Long` | `0.3825` | 4,750,000.00 USD | 0.00 USD | 426.53 USD | `-56.57%` | `1,115.10` |
| `Live` | `Long` | `0.3845` | 4,750,000.00 USD | 0.00 USD | 1,750.00 USD | `-56.34%` | `4,562.20` |
| `Live` | `Long` | `0.3895` | 4,740,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.77%` | `7,661.70` |
| `Live` | `Long` | `0.3905` | 4,740,000.00 USD | 0.00 USD | 30,340.00 USD | `-55.66%` | `77,706.40` |
| `Live` | `Long` | `0.3925` | 4,710,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.43%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,710,000.00 USD | 0.00 USD | 754.48 USD | `-55.20%` | `1,912.50` |
| `Live` | `Long` | `0.4025` | 4,700,000.00 USD | 0.00 USD | 28,180.00 USD | `-54.30%` | `70,000.00` |
| `Live` | `Long` | `0.4035` | 4,680,000.00 USD | 0.00 USD | 935.03 USD | `-54.18%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,680,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.07%` | `13,640.50` |
| `Live` | `Long` | `0.4175` | 4,670,000.00 USD | 0.00 USD | 218.94 USD | `-52.59%` | `524.40` |
| `Live` | `Long` | `0.4235` | 4,670,000.00 USD | 0.00 USD | 467.50 USD | `-51.91%` | `1,103.90` |
| `Live` | `Long` | `0.4275` | 4,670,000.00 USD | 0.00 USD | 2,000.00 USD | `-51.46%` | `4,670.70` |
| `Live` | `Long` | `0.4285` | 4,670,000.00 USD | 0.00 USD | 299.95 USD | `-51.34%` | `700.00` |
| `Live` | `Long` | `0.4385` | 4,670,000.00 USD | 0.00 USD | 122.91 USD | `-50.21%` | `280.30` |
| `Live` | `Long` | `0.4405` | 4,670,000.00 USD | 0.00 USD | 54,420.00 USD | `-49.98%` | `123,550.00` |
| `Live` | `Long` | `0.4415` | 4,610,000.00 USD | 0.00 USD | 5,800.00 USD | `-49.87%` | `13,146.20` |
| `Live` | `Long` | `0.4425` | 4,610,000.00 USD | 0.00 USD | 779.69 USD | `-49.75%` | `1,762.00` |
| `Live` | `Long` | `0.4435` | 4,610,000.00 USD | 0.00 USD | 219.00 USD | `-49.64%` | `493.80` |
| `Live` | `Long` | `0.4445` | 4,610,000.00 USD | 0.00 USD | 573.54 USD | `-49.53%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,600,000.00 USD | 0.00 USD | 19,600.00 USD | `-49.30%` | `43,906.00` |
| `Live` | `Long` | `0.4485` | 4,590,000.00 USD | 0.00 USD | 3,810.00 USD | `-49.07%` | `8,500.00` |
| `Live` | `Long` | `0.4535` | 4,580,000.00 USD | 0.00 USD | 702.74 USD | `-48.51%` | `1,549.60` |
| `Live` | `Long` | `0.4565` | 4,580,000.00 USD | 0.00 USD | 387.02 USD | `-48.16%` | `847.80` |
| `Live` | `Long` | `0.4595` | 4,580,000.00 USD | 0.00 USD | 295.78 USD | `-47.82%` | `643.70` |
| `Live` | `Long` | `0.4645` | 4,580,000.00 USD | 0.00 USD | 2,110.00 USD | `-47.26%` | `4,538.10` |
| `Live` | `Long` | `0.4695` | 4,580,000.00 USD | 0.00 USD | 3,890.00 USD | `-46.69%` | `8,275.50` |
| `Live` | `Long` | `0.4715` | 4,570,000.00 USD | 0.00 USD | 1,720.00 USD | `-46.46%` | `3,650.40` |
| `Live` | `Long` | `0.4785` | 4,570,000.00 USD | 0.00 USD | 6,090.00 USD | `-45.67%` | `12,730.10` |
| `Live` | `Long` | `0.4825` | 4,570,000.00 USD | 0.00 USD | 1,470.00 USD | `-45.21%` | `3,043.40` |
| `Live` | `Long` | `0.4835` | 4,560,000.00 USD | 0.00 USD | 174.01 USD | `-45.10%` | `359.90` |
| `Live` | `Long` | `0.4845` | 4,560,000.00 USD | 0.00 USD | 9,690.00 USD | `-44.99%` | `20,000.00` |
| `Live` | `Long` | `0.4865` | 4,550,000.00 USD | 0.00 USD | 201.07 USD | `-44.76%` | `413.30` |
| `Live` | `Long` | `0.4885` | 4,550,000.00 USD | 0.00 USD | 1,050.00 USD | `-44.53%` | `2,151.80` |
| `Live` | `Long` | `0.4895` | 4,550,000.00 USD | 0.00 USD | 105.34 USD | `-44.42%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,550,000.00 USD | 0.00 USD | 6,070.00 USD | `-44.19%` | `12,357.70` |
| `Live` | `Long` | `0.4925` | 4,550,000.00 USD | 0.00 USD | 5,560.00 USD | `-44.08%` | `11,290.30` |
| `Live` | `Long` | `0.4945` | 4,540,000.00 USD | 0.00 USD | 106.32 USD | `-43.85%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,540,000.00 USD | 0.00 USD | 211.88 USD | `-43.74%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,540,000.00 USD | 0.00 USD | 216.75 USD | `-43.40%` | `434.80` |
| `Live` | `Long` | `0.4995` | 4,540,000.00 USD | 0.00 USD | 552.45 USD | `-43.28%` | `1,106.00` |
| `Live` | `Long` | `0.5015` | 4,540,000.00 USD | 0.00 USD | 1,720.00 USD | `-43.05%` | `3,423.70` |
| `Live` | `Long` | `0.5025` | 4,540,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.94%` | `2,451.10` |
| `Live` | `Long` | `0.5035` | 4,540,000.00 USD | 0.00 USD | 503.50 USD | `-42.83%` | `1,000.00` |
| `Live` | `Long` | `0.5055` | 4,540,000.00 USD | 0.00 USD | 211.25 USD | `-42.60%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,540,000.00 USD | 0.00 USD | 5,680.00 USD | `-42.26%` | `11,163.80` |
| `Live` | `Long` | `0.5095` | 4,530,000.00 USD | 0.00 USD | 195.75 USD | `-42.15%` | `384.20` |
| `Live` | `Long` | `0.5125` | 4,530,000.00 USD | 0.00 USD | 268.34 USD | `-41.81%` | `523.60` |
| `Live` | `Long` | `0.5155` | 4,530,000.00 USD | 0.00 USD | 1,240.00 USD | `-41.47%` | `2,409.50` |
| `Live` | `Long` | `0.5165` | 4,530,000.00 USD | 0.00 USD | 619.80 USD | `-41.35%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,530,000.00 USD | 0.00 USD | 213.68 USD | `-41.24%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,530,000.00 USD | 0.00 USD | 982.56 USD | `-41.12%` | `1,895.00` |
| `Live` | `Long` | `0.5245` | 4,530,000.00 USD | 0.00 USD | 22,750.00 USD | `-40.44%` | `43,371.80` |
| `Live` | `Long` | `0.5275` | 4,510,000.00 USD | 0.00 USD | 348.36 USD | `-40.10%` | `660.40` |
| `Live` | `Long` | `0.5295` | 4,500,000.00 USD | 0.00 USD | 123,640.00 USD | `-39.88%` | `233,498.70` |
| `Live` | `Long` | `0.5325` | 4,380,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.53%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,380,000.00 USD | 0.00 USD | 417.12 USD | `-39.31%` | `780.40` |
| `Live` | `Long` | `0.5375` | 4,380,000.00 USD | 0.00 USD | 7,850.00 USD | `-38.97%` | `14,603.90` |
| `Live` | `Long` | `0.5405` | 4,370,000.00 USD | 0.00 USD | 7,090.00 USD | `-38.63%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,360,000.00 USD | 0.00 USD | 269.13 USD | `-38.40%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,360,000.00 USD | 0.00 USD | 230.32 USD | `-38.17%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,360,000.00 USD | 0.00 USD | 272.87 USD | `-37.94%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,360,000.00 USD | 0.00 USD | 1,570.00 USD | `-37.83%` | `2,865.50` |
| `Live` | `Long` | `0.5495` | 4,360,000.00 USD | 0.00 USD | 28,790.00 USD | `-37.60%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,330,000.00 USD | 0.00 USD | 33,280.00 USD | `-37.49%` | `60,450.60` |
| `Live` | `Long` | `0.5515` | 4,300,000.00 USD | 0.00 USD | 160.93 USD | `-37.38%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,300,000.00 USD | 0.00 USD | 582.56 USD | `-37.26%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,300,000.00 USD | 0.00 USD | 407.60 USD | `-37.15%` | `736.40` |
| `Live` | `Long` | `0.5545` | 4,300,000.00 USD | 0.00 USD | 6,670.00 USD | `-37.04%` | `12,022.70` |
| `Live` | `Long` | `0.5555` | 4,290,000.00 USD | 0.00 USD | 7,950.00 USD | `-36.92%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,280,000.00 USD | 0.00 USD | 141.97 USD | `-36.58%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,280,000.00 USD | 0.00 USD | 304.93 USD | `-36.47%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,280,000.00 USD | 0.00 USD | 441.84 USD | `-36.36%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,280,000.00 USD | 0.00 USD | 330.53 USD | `-36.13%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,280,000.00 USD | 0.00 USD | 195.93 USD | `-36.01%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,280,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.79%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,270,000.00 USD | 0.00 USD | 570.01 USD | `-35.67%` | `1,006.20` |
| `Live` | `Long` | `0.5675` | 4,270,000.00 USD | 0.00 USD | 1,560.00 USD | `-35.56%` | `2,747.00` |
| `Live` | `Long` | `0.5685` | 4,270,000.00 USD | 0.00 USD | 4,540.00 USD | `-35.45%` | `7,985.90` |
| `Live` | `Long` | `0.5695` | 4,270,000.00 USD | 0.00 USD | 973.22 USD | `-35.33%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,270,000.00 USD | 0.00 USD | 139.23 USD | `-34.99%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,270,000.00 USD | 0.00 USD | 182.72 USD | `-34.88%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,270,000.00 USD | 0.00 USD | 144.03 USD | `-34.77%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,270,000.00 USD | 0.00 USD | 1,010.00 USD | `-34.65%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,260,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.54%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,260,000.00 USD | 0.00 USD | 497.75 USD | `-34.42%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,260,000.00 USD | 0.00 USD | 227.41 USD | `-34.31%` | `393.10` |
| `Live` | `Long` | `0.5795` | 4,260,000.00 USD | 0.00 USD | 684.10 USD | `-34.20%` | `1,180.50` |
| `Live` | `Long` | `0.5805` | 4,260,000.00 USD | 0.00 USD | 1,760.00 USD | `-34.08%` | `3,027.80` |
| `Live` | `Long` | `0.5815` | 4,260,000.00 USD | 0.00 USD | 174.45 USD | `-33.97%` | `300.00` |
| `Live` | `Long` | `0.5825` | 4,260,000.00 USD | 0.00 USD | 6,470.00 USD | `-33.86%` | `11,099.00` |
| `Live` | `Long` | `0.5855` | 4,250,000.00 USD | 0.00 USD | 2,640.00 USD | `-33.52%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,250,000.00 USD | 0.00 USD | 466.85 USD | `-33.40%` | `796.00` |
| `Live` | `Long` | `0.5875` | 4,250,000.00 USD | 0.00 USD | 969.32 USD | `-33.29%` | `1,649.90` |
| `Live` | `Long` | `0.5885` | 4,250,000.00 USD | 0.00 USD | 311.14 USD | `-33.18%` | `528.70` |
| `Live` | `Long` | `0.5925` | 4,250,000.00 USD | 0.00 USD | 994.16 USD | `-32.72%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,250,000.00 USD | 0.00 USD | 132.41 USD | `-32.61%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,250,000.00 USD | 0.00 USD | 8,220.00 USD | `-32.49%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,240,000.00 USD | 0.00 USD | 17,930.00 USD | `-32.27%` | `30,057.30` |
| `Live` | `Long` | `0.5995` | 4,220,000.00 USD | 0.00 USD | 151.97 USD | `-31.93%` | `253.50` |
| `Live` | `Long` | `0.6005` | 4,220,000.00 USD | 0.00 USD | 4,370.00 USD | `-31.81%` | `7,276.20` |
| `Live` | `Long` | `0.6015` | 4,220,000.00 USD | 0.00 USD | 323.79 USD | `-31.70%` | `538.30` |
| `Live` | `Long` | `0.6025` | 4,220,000.00 USD | 0.00 USD | 432.35 USD | `-31.59%` | `717.60` |
| `Live` | `Long` | `0.6075` | 4,220,000.00 USD | 0.00 USD | 851.05 USD | `-31.02%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,220,000.00 USD | 0.00 USD | 272.24 USD | `-30.90%` | `447.40` |
| `Live` | `Long` | `0.6095` | 4,220,000.00 USD | 0.00 USD | 9,700.00 USD | `-30.79%` | `15,919.00` |
| `Live` | `Long` | `0.6105` | 4,210,000.00 USD | 0.00 USD | 663.43 USD | `-30.68%` | `1,086.70` |
| `Live` | `Long` | `0.6115` | 4,200,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.56%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 4,200,000.00 USD | 0.00 USD | 213.64 USD | `-30.45%` | `348.80` |
| `Live` | `Long` | `0.6135` | 4,200,000.00 USD | 0.00 USD | 357.73 USD | `-30.34%` | `583.10` |
| `Live` | `Long` | `0.6145` | 4,200,000.00 USD | 0.00 USD | 3,430.00 USD | `-30.22%` | `5,579.50` |
| `Live` | `Long` | `0.6155` | 4,190,000.00 USD | 0.00 USD | 18,790.00 USD | `-30.11%` | `30,534.50` |
| `Live` | `Long` | `0.6165` | 4,180,000.00 USD | 0.00 USD | 29,900.00 USD | `-30.00%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 4,150,000.00 USD | 0.00 USD | 4,170.00 USD | `-29.88%` | `6,760.50` |
| `Live` | `Long` | `0.6185` | 4,140,000.00 USD | 0.00 USD | 13,910.00 USD | `-29.77%` | `22,495.30` |
| `Live` | `Long` | `0.6195` | 4,130,000.00 USD | 0.00 USD | 1,610.00 USD | `-29.66%` | `2,605.70` |
| `Live` | `Long` | `0.6215` | 4,130,000.00 USD | 0.00 USD | 444.75 USD | `-29.43%` | `715.60` |
| `Live` | `Long` | `0.6225` | 4,130,000.00 USD | 0.00 USD | 263.07 USD | `-29.32%` | `422.60` |
| `Live` | `Long` | `0.6245` | 4,130,000.00 USD | 0.00 USD | 619.32 USD | `-29.09%` | `991.70` |
| `Live` | `Long` | `0.6255` | 4,120,000.00 USD | 0.00 USD | 32,070.00 USD | `-28.97%` | `51,265.70` |
| `Live` | `Long` | `0.6285` | 4,090,000.00 USD | 0.00 USD | 102.45 USD | `-28.63%` | `163.00` |
| `Live` | `Long` | `0.6305` | 4,090,000.00 USD | 0.00 USD | 319.35 USD | `-28.41%` | `506.50` |
| `Live` | `Long` | `0.6315` | 4,090,000.00 USD | 0.00 USD | 3,510.00 USD | `-28.29%` | `5,564.80` |
| `Live` | `Long` | `0.6345` | 4,090,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.95%` | `1,813.10` |
| `Live` | `Long` | `0.6355` | 4,090,000.00 USD | 0.00 USD | 207.17 USD | `-27.84%` | `326.00` |
| `Live` | `Long` | `0.6365` | 4,090,000.00 USD | 0.00 USD | 3,340.00 USD | `-27.73%` | `5,244.00` |
| `Live` | `Long` | `0.6375` | 4,080,000.00 USD | 0.00 USD | 318,880.00 USD | `-27.61%` | `500,204.90` |
| `Live` | `Long` | `0.6395` | 3,770,000.00 USD | 0.00 USD | 8,830.00 USD | `-27.38%` | `13,805.30` |
| `Live` | `Long` | `0.6405` | 3,760,000.00 USD | 0.00 USD | 939.17 USD | `-27.27%` | `1,466.30` |
| `Live` | `Long` | `0.6415` | 3,760,000.00 USD | 0.00 USD | 87,100.00 USD | `-27.16%` | `135,776.90` |
| `Live` | `Long` | `0.6425` | 3,670,000.00 USD | 0.00 USD | 1,260.00 USD | `-27.04%` | `1,956.60` |
| `Live` | `Long` | `0.6435` | 3,670,000.00 USD | 0.00 USD | 657.79 USD | `-26.93%` | `1,022.20` |
| `Live` | `Long` | `0.6445` | 3,670,000.00 USD | 0.00 USD | 65,790.00 USD | `-26.82%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,600,000.00 USD | 0.00 USD | 14,590.00 USD | `-26.70%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,590,000.00 USD | 0.00 USD | 146.76 USD | `-26.59%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,590,000.00 USD | 0.00 USD | 3,910.00 USD | `-26.48%` | `6,031.70` |
| `Live` | `Long` | `0.6485` | 3,580,000.00 USD | 0.00 USD | 668.34 USD | `-26.36%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,580,000.00 USD | 0.00 USD | 17,260.00 USD | `-26.25%` | `26,574.10` |
| `Live` | `Long` | `0.6505` | 3,560,000.00 USD | 0.00 USD | 10,740.00 USD | `-26.14%` | `16,513.30` |
| `Live` | `Long` | `0.6515` | 3,550,000.00 USD | 0.00 USD | 403,320.00 USD | `-26.02%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,150,000.00 USD | 0.00 USD | 371.14 USD | `-25.91%` | `568.80` |
| `Live` | `Long` | `0.6535` | 3,150,000.00 USD | 0.00 USD | 126,530.00 USD | `-25.80%` | `193,618.10` |
| `Live` | `Long` | `0.6545` | 3,020,000.00 USD | 0.00 USD | 151.45 USD | `-25.68%` | `231.40` |
| `Live` | `Long` | `0.6555` | 3,020,000.00 USD | 0.00 USD | 676.54 USD | `-25.57%` | `1,032.10` |
| `Live` | `Long` | `0.6565` | 3,020,000.00 USD | 0.00 USD | 7,070.00 USD | `-25.45%` | `10,764.20` |
| `Live` | `Long` | `0.6575` | 3,020,000.00 USD | 0.00 USD | 13,280.00 USD | `-25.34%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,000,000.00 USD | 0.00 USD | 2,970.00 USD | `-25.23%` | `4,508.30` |
| `Live` | `Long` | `0.6615` | 3,000,000.00 USD | 0.00 USD | 13,800.00 USD | `-24.89%` | `20,857.90` |
| `Live` | `Long` | `0.6625` | 2,990,000.00 USD | 0.00 USD | 788.97 USD | `-24.77%` | `1,190.90` |
| `Live` | `Long` | `0.6635` | 2,980,000.00 USD | 0.00 USD | 1,170.00 USD | `-24.66%` | `1,761.60` |
| `Live` | `Long` | `0.6645` | 2,980,000.00 USD | 0.00 USD | 448.54 USD | `-24.55%` | `675.00` |
| `Live` | `Long` | `0.6665` | 2,980,000.00 USD | 0.00 USD | 528.73 USD | `-24.32%` | `793.30` |
| `Live` | `Long` | `0.6675` | 2,980,000.00 USD | 0.00 USD | 6,810.00 USD | `-24.21%` | `10,207.60` |
| `Live` | `Long` | `0.6685` | 2,980,000.00 USD | 0.00 USD | 2,810.00 USD | `-24.09%` | `4,203.00` |
| `Live` | `Long` | `0.6705` | 2,970,000.00 USD | 0.00 USD | 2,290.00 USD | `-23.86%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 2,970,000.00 USD | 0.00 USD | 8,500.00 USD | `-23.75%` | `12,661.20` |
| `Live` | `Long` | `0.6725` | 2,960,000.00 USD | 0.00 USD | 29,400.00 USD | `-23.64%` | `43,720.20` |
| `Live` | `Long` | `0.6735` | 2,930,000.00 USD | 0.00 USD | 633.09 USD | `-23.52%` | `940.00` |
| `Live` | `Long` | `0.6745` | 2,930,000.00 USD | 0.00 USD | 6,520.00 USD | `-23.41%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 2,930,000.00 USD | 0.00 USD | 111.59 USD | `-23.30%` | `165.20` |
| `Live` | `Long` | `0.6775` | 2,930,000.00 USD | 0.00 USD | 6,780.00 USD | `-23.07%` | `10,000.00` |
| `Live` | `Long` | `0.6795` | 2,920,000.00 USD | 0.00 USD | 45,130.00 USD | `-22.84%` | `66,410.20` |
| `Live` | `Long` | `0.6805` | 2,870,000.00 USD | 0.00 USD | 1,600.00 USD | `-22.73%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 2,870,000.00 USD | 0.00 USD | 3,550.00 USD | `-22.62%` | `5,210.50` |
| `Live` | `Long` | `0.6825` | 2,870,000.00 USD | 0.00 USD | 15,920.00 USD | `-22.50%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 2,850,000.00 USD | 0.00 USD | 11,510.00 USD | `-22.39%` | `16,836.60` |
| `Live` | `Long` | `0.6845` | 2,840,000.00 USD | 0.00 USD | 5,790.00 USD | `-22.28%` | `8,455.80` |
| `Live` | `Long` | `0.6865` | 2,840,000.00 USD | 0.00 USD | 112.59 USD | `-22.05%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,830,000.00 USD | 0.00 USD | 480.49 USD | `-21.93%` | `698.90` |
| `Live` | `Long` | `0.6885` | 2,830,000.00 USD | 0.00 USD | 83,790.00 USD | `-21.82%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 2,750,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.71%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,750,000.00 USD | 0.00 USD | 3,470.00 USD | `-21.59%` | `5,031.90` |
| `Live` | `Long` | `0.6915` | 2,750,000.00 USD | 0.00 USD | 8,970.00 USD | `-21.48%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 2,740,000.00 USD | 0.00 USD | 3,600.00 USD | `-21.25%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 2,730,000.00 USD | 0.00 USD | 2,640.00 USD | `-21.14%` | `3,799.80` |
| `Live` | `Long` | `0.6965` | 2,730,000.00 USD | 0.00 USD | 1,150.00 USD | `-20.91%` | `1,650.00` |
| `Live` | `Long` | `0.6985` | 2,730,000.00 USD | 0.00 USD | 1,930.00 USD | `-20.69%` | `2,759.10` |
| `Live` | `Long` | `0.7015` | 2,730,000.00 USD | 0.00 USD | 1,990.00 USD | `-20.34%` | `2,841.50` |
| `Live` | `Long` | `0.7045` | 2,720,000.00 USD | 0.00 USD | 759.59 USD | `-20.00%` | `1,078.20` |
| `Live` | `Long` | `0.7065` | 2,720,000.00 USD | 0.00 USD | 769.59 USD | `-19.78%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 2,720,000.00 USD | 0.00 USD | 3,420.00 USD | `-19.66%` | `4,832.90` |
| `Live` | `Long` | `0.7085` | 2,720,000.00 USD | 0.00 USD | 2,020.00 USD | `-19.55%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,720,000.00 USD | 0.00 USD | 2,720.00 USD | `-19.44%` | `3,833.70` |
| `Live` | `Long` | `0.7105` | 2,720,000.00 USD | 0.00 USD | 3,530.00 USD | `-19.32%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 2,710,000.00 USD | 0.00 USD | 569.20 USD | `-19.21%` | `800.00` |
| `Live` | `Long` | `0.7125` | 2,710,000.00 USD | 0.00 USD | 156.39 USD | `-19.10%` | `219.50` |
| `Live` | `Long` | `0.7175` | 2,710,000.00 USD | 0.00 USD | 126,470.00 USD | `-18.53%` | `176,259.70` |
| `Live` | `Long` | `0.7195` | 2,580,000.00 USD | 0.00 USD | 14,810.00 USD | `-18.30%` | `20,584.30` |
| `Live` | `Long` | `0.7225` | 2,570,000.00 USD | 0.00 USD | 129.26 USD | `-17.96%` | `178.90` |
| `Live` | `Long` | `0.7255` | 2,570,000.00 USD | 0.00 USD | 3,180.00 USD | `-17.62%` | `4,386.50` |
| `Live` | `Long` | `0.7265` | 2,570,000.00 USD | 0.00 USD | 1,060.00 USD | `-17.51%` | `1,453.70` |
| `Live` | `Long` | `0.7275` | 2,570,000.00 USD | 0.00 USD | 762.57 USD | `-17.39%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 2,560,000.00 USD | 0.00 USD | 214.03 USD | `-17.28%` | `293.80` |
| `Live` | `Long` | `0.7295` | 2,560,000.00 USD | 0.00 USD | 26,490.00 USD | `-17.17%` | `36,317.70` |
| `Live` | `Long` | `0.7305` | 2,540,000.00 USD | 0.00 USD | 241.14 USD | `-17.05%` | `330.10` |
| `Live` | `Long` | `0.7325` | 2,540,000.00 USD | 0.00 USD | 907.93 USD | `-16.82%` | `1,239.50` |
| `Live` | `Long` | `0.7335` | 2,540,000.00 USD | 0.00 USD | 837.00 USD | `-16.71%` | `1,141.10` |
| `Live` | `Long` | `0.7345` | 2,540,000.00 USD | 0.00 USD | 2,340.00 USD | `-16.60%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,530,000.00 USD | 0.00 USD | 51,920.00 USD | `-16.48%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 2,480,000.00 USD | 0.00 USD | 3,450.00 USD | `-16.37%` | `4,683.00` |
| `Live` | `Long` | `0.7375` | 2,480,000.00 USD | 0.00 USD | 203.11 USD | `-16.26%` | `275.40` |
| `Live` | `Long` | `0.7385` | 2,480,000.00 USD | 0.00 USD | 5,810.00 USD | `-16.14%` | `7,871.10` |
| `Live` | `Long` | `0.7395` | 2,470,000.00 USD | 0.00 USD | 1,260.00 USD | `-16.03%` | `1,705.90` |
| `Live` | `Long` | `0.7405` | 2,470,000.00 USD | 0.00 USD | 5,210.00 USD | `-15.92%` | `7,038.80` |
| `Live` | `Long` | `0.7415` | 2,470,000.00 USD | 0.00 USD | 382.61 USD | `-15.80%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,470,000.00 USD | 0.00 USD | 785,210.00 USD | `-15.69%` | `1,057,516.70` |
| `Live` | `Long` | `0.7435` | 1,680,000.00 USD | 0.00 USD | 421.12 USD | `-15.58%` | `566.40` |
| `Live` | `Long` | `0.7445` | 1,680,000.00 USD | 0.00 USD | 105.64 USD | `-15.46%` | `141.90` |
| `Live` | `Long` | `0.7455` | 1,680,000.00 USD | 0.00 USD | 2,160.00 USD | `-15.35%` | `2,892.60` |
| `Live` | `Long` | `0.7465` | 1,680,000.00 USD | 0.00 USD | 15,290.00 USD | `-15.23%` | `20,482.20` |
| `Live` | `Long` | `0.7475` | 1,660,000.00 USD | 0.00 USD | 107,260.00 USD | `-15.12%` | `143,489.20` |
| `Live` | `Long` | `0.7485` | 1,550,000.00 USD | 0.00 USD | 105.91 USD | `-15.01%` | `141.50` |
| `Live` | `Long` | `0.7495` | 1,550,000.00 USD | 0.00 USD | 9,250.00 USD | `-14.89%` | `12,345.90` |
| `Live` | `Long` | `0.7515` | 1,550,000.00 USD | 0.00 USD | 1,210.00 USD | `-14.67%` | `1,613.50` |
| `Live` | `Long` | `0.7525` | 1,540,000.00 USD | 0.00 USD | 106.03 USD | `-14.55%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,540,000.00 USD | 0.00 USD | 766.69 USD | `-14.44%` | `1,017.50` |
| `Live` | `Long` | `0.7545` | 1,540,000.00 USD | 0.00 USD | 922.07 USD | `-14.33%` | `1,222.10` |
| `Live` | `Long` | `0.7565` | 1,540,000.00 USD | 0.00 USD | 438.54 USD | `-14.10%` | `579.70` |
| `Live` | `Long` | `0.7575` | 1,540,000.00 USD | 0.00 USD | 1,900.00 USD | `-13.99%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,540,000.00 USD | 0.00 USD | 36,710.00 USD | `-13.87%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,500,000.00 USD | 0.00 USD | 4,390.00 USD | `-13.76%` | `5,776.10` |
| `Live` | `Long` | `0.7615` | 1,500,000.00 USD | 0.00 USD | 351.43 USD | `-13.53%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,500,000.00 USD | 0.00 USD | 859.11 USD | `-13.42%` | `1,126.70` |
| `Live` | `Long` | `0.7635` | 1,500,000.00 USD | 0.00 USD | 5,110.00 USD | `-13.30%` | `6,696.30` |
| `Live` | `Long` | `0.7645` | 1,490,000.00 USD | 0.00 USD | 319,630.00 USD | `-13.19%` | `418,085.50` |
| `Live` | `Long` | `0.7655` | 1,170,000.00 USD | 0.00 USD | 4,430.00 USD | `-13.08%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,170,000.00 USD | 0.00 USD | 1,420.00 USD | `-12.96%` | `1,847.90` |
| `Live` | `Long` | `0.7675` | 1,170,000.00 USD | 0.00 USD | 10,200.00 USD | `-12.85%` | `13,292.20` |
| `Live` | `Long` | `0.7685` | 1,160,000.00 USD | 0.00 USD | 807.39 USD | `-12.74%` | `1,050.60` |
| `Live` | `Long` | `0.7695` | 1,160,000.00 USD | 0.00 USD | 144,250.00 USD | `-12.62%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 1,010,000.00 USD | 0.00 USD | 4,350.00 USD | `-12.51%` | `5,644.90` |
| `Live` | `Long` | `0.7715` | 1,010,000.00 USD | 0.00 USD | 9,980.00 USD | `-12.40%` | `12,938.60` |
| `Live` | `Long` | `0.7725` | 997,570.00 USD | 0.00 USD | 2,200.00 USD | `-12.28%` | `2,852.80` |
| `Live` | `Long` | `0.7735` | 995,370.00 USD | 0.00 USD | 4,570.00 USD | `-12.17%` | `5,912.10` |
| `Live` | `Long` | `0.7745` | 990,790.00 USD | 0.00 USD | 746.62 USD | `-12.06%` | `964.00` |
| `Live` | `Long` | `0.7755` | 990,050.00 USD | 0.00 USD | 3,430.00 USD | `-11.94%` | `4,424.80` |
| `Live` | `Long` | `0.7765` | 986,620.00 USD | 0.00 USD | 21,370.00 USD | `-11.83%` | `27,514.60` |
| `Live` | `Long` | `0.7785` | 965,250.00 USD | 0.00 USD | 35,490.00 USD | `-11.60%` | `45,588.50` |
| `Live` | `Long` | `0.7795` | 929,760.00 USD | 0.00 USD | 338.69 USD | `-11.49%` | `434.50` |
| `Live` | `Long` | `0.7815` | 929,420.00 USD | 0.00 USD | 4,160.00 USD | `-11.26%` | `5,325.20` |
| `Live` | `Long` | `0.7825` | 925,260.00 USD | 0.00 USD | 15,670.00 USD | `-11.15%` | `20,031.40` |
| `Live` | `Long` | `0.7835` | 909,580.00 USD | 0.00 USD | 1,720.00 USD | `-11.03%` | `2,199.80` |
| `Live` | `Long` | `0.7855` | 907,860.00 USD | 0.00 USD | 3,020.00 USD | `-10.81%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 904,840.00 USD | 0.00 USD | 2,870.00 USD | `-10.69%` | `3,651.90` |
| `Live` | `Long` | `0.7875` | 901,970.00 USD | 0.00 USD | 684.97 USD | `-10.58%` | `869.80` |
| `Live` | `Long` | `0.7895` | 901,290.00 USD | 0.00 USD | 2,530.00 USD | `-10.35%` | `3,204.80` |
| `Live` | `Long` | `0.7905` | 898,760.00 USD | 0.00 USD | 3,870.00 USD | `-10.24%` | `4,891.30` |
| `Live` | `Long` | `0.7915` | 894,890.00 USD | 0.00 USD | 5,470.00 USD | `-10.13%` | `6,905.90` |
| `Live` | `Long` | `0.7925` | 889,420.00 USD | 0.00 USD | 12,850.00 USD | `-10.01%` | `16,218.30` |
| `Live` | `Long` | `0.7935` | 876,570.00 USD | 0.00 USD | 4,070.00 USD | `-9.90%` | `5,130.80` |
| `Live` | `Long` | `0.7945` | 872,500.00 USD | 0.00 USD | 10,070.00 USD | `-9.78%` | `12,673.20` |
| `Live` | `Long` | `0.7955` | 862,430.00 USD | 0.00 USD | 33,500.00 USD | `-9.67%` | `42,118.10` |
| `Live` | `Long` | `0.7965` | 828,930.00 USD | 0.00 USD | 7,960.00 USD | `-9.56%` | `10,000.00` |
| `Live` | `Long` | `0.7975` | 820,960.00 USD | 0.00 USD | 1,170.00 USD | `-9.44%` | `1,464.30` |
| `Live` | `Long` | `0.7995` | 819,790.00 USD | 0.00 USD | 18,340.00 USD | `-9.22%` | `22,933.50` |
| `Live` | `Long` | `0.8015` | 801,460.00 USD | 0.00 USD | 7,130.00 USD | `-8.99%` | `8,893.40` |
| `Live` | `Long` | `0.8035` | 794,330.00 USD | 0.00 USD | 316.42 USD | `-8.76%` | `393.80` |
| `Live` | `Long` | `0.8045` | 794,010.00 USD | 0.00 USD | 34,400.00 USD | `-8.65%` | `42,764.80` |
| `Live` | `Long` | `0.8065` | 759,610.00 USD | 0.00 USD | 1,540.00 USD | `-8.42%` | `1,908.10` |
| `Live` | `Long` | `0.8075` | 758,070.00 USD | 0.00 USD | 1,220.00 USD | `-8.31%` | `1,515.40` |
| `Live` | `Long` | `0.8085` | 756,850.00 USD | 0.00 USD | 22,170.00 USD | `-8.19%` | `27,427.20` |
| `Live` | `Long` | `0.8095` | 734,670.00 USD | 0.00 USD | 3,890.00 USD | `-8.08%` | `4,805.10` |
| `Live` | `Long` | `0.8105` | 730,780.00 USD | 0.00 USD | 2,390.00 USD | `-7.97%` | `2,942.70` |
| `Live` | `Long` | `0.8115` | 728,400.00 USD | 0.00 USD | 1,390.00 USD | `-7.85%` | `1,716.00` |
| `Live` | `Long` | `0.8125` | 727,000.00 USD | 0.00 USD | 112.37 USD | `-7.74%` | `138.30` |
| `Live` | `Long` | `0.8135` | 726,890.00 USD | 0.00 USD | 8,130.00 USD | `-7.63%` | `9,989.60` |
| `Live` | `Long` | `0.8145` | 718,770.00 USD | 0.00 USD | 2,200.00 USD | `-7.51%` | `2,702.90` |
| `Live` | `Long` | `0.8155` | 716,560.00 USD | 0.00 USD | 8,160.00 USD | `-7.40%` | `10,000.00` |
| `Live` | `Long` | `0.8165` | 708,410.00 USD | 0.00 USD | 104.92 USD | `-7.29%` | `128.50` |
| `Live` | `Long` | `0.8175` | 708,300.00 USD | 0.00 USD | 103,490.00 USD | `-7.17%` | `126,593.20` |
| `Live` | `Long` | `0.8185` | 604,810.00 USD | 0.00 USD | 491.10 USD | `-7.06%` | `600.00` |
| `Live` | `Long` | `0.8195` | 604,320.00 USD | 0.00 USD | 1,110.00 USD | `-6.95%` | `1,360.00` |
| `Live` | `Long` | `0.8205` | 603,210.00 USD | 0.00 USD | 2,280.00 USD | `-6.83%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 600,930.00 USD | 0.00 USD | 6,650.00 USD | `-6.72%` | `8,091.40` |
| `Live` | `Long` | `0.8225` | 594,280.00 USD | 0.00 USD | 1,870.00 USD | `-6.61%` | `2,279.50` |
| `Live` | `Long` | `0.8235` | 592,400.00 USD | 0.00 USD | 216.00 USD | `-6.49%` | `262.30` |
| `Live` | `Long` | `0.8245` | 592,190.00 USD | 0.00 USD | 70,830.00 USD | `-6.38%` | `85,903.10` |
| `Live` | `Long` | `0.8255` | 521,360.00 USD | 0.00 USD | 1,070.00 USD | `-6.26%` | `1,294.90` |
| `Live` | `Long` | `0.8275` | 520,290.00 USD | 0.00 USD | 16,090.00 USD | `-6.04%` | `19,449.30` |
| `Live` | `Long` | `0.8285` | 504,200.00 USD | 0.00 USD | 135,600.00 USD | `-5.92%` | `163,670.70` |
| `Live` | `Long` | `0.8295` | 368,600.00 USD | 0.00 USD | 24,330.00 USD | `-5.81%` | `29,330.40` |
| `Live` | `Long` | `0.8305` | 344,270.00 USD | 0.00 USD | 3,360.00 USD | `-5.70%` | `4,047.10` |
| `Live` | `Long` | `0.8315` | 340,910.00 USD | 0.00 USD | 3,340.00 USD | `-5.58%` | `4,013.70` |
| `Live` | `Long` | `0.8325` | 337,570.00 USD | 0.00 USD | 28,510.00 USD | `-5.47%` | `34,246.60` |
| `Live` | `Long` | `0.8335` | 309,060.00 USD | 0.00 USD | 5,100.00 USD | `-5.36%` | `6,122.50` |
| `Live` | `Long` | `0.8345` | 303,960.00 USD | 0.00 USD | 469.82 USD | `-5.24%` | `563.00` |
| `Live` | `Long` | `0.8355` | 303,490.00 USD | 0.00 USD | 6,740.00 USD | `-5.13%` | `8,068.90` |
| `Live` | `Long` | `0.8365` | 296,740.00 USD | 0.00 USD | 67,100.00 USD | `-5.02%` | `80,216.60` |
| `Live` | `Long` | `0.8375` | 229,640.00 USD | 0.00 USD | 21,870.00 USD | `-4.90%` | `26,113.90` |
| `Live` | `Long` | `0.8385` | 207,770.00 USD | 0.00 USD | 77,770.00 USD | `-4.79%` | `92,754.10` |
| `Live` | `Long` | `0.8395` | 130,000.00 USD | 0.00 USD | 30,330.00 USD | `-4.67%` | `36,133.40` |
| `Live` | `Long` | `0.8405` | 99,660.00 USD | 0.00 USD | 3,620.00 USD | `-4.56%` | `4,310.00` |
| `Live` | `Long` | `0.8415` | 96,040.00 USD | 0.00 USD | 3,250.00 USD | `-4.45%` | `3,858.40` |
| `Live` | `Long` | `0.8425` | 92,800.00 USD | 0.00 USD | 3,420.00 USD | `-4.33%` | `4,055.10` |
| `Live` | `Long` | `0.8435` | 89,380.00 USD | 0.00 USD | 4,290.00 USD | `-4.22%` | `5,082.70` |
| `Live` | `Long` | `0.8445` | 85,090.00 USD | 0.00 USD | 598.67 USD | `-4.11%` | `708.90` |
| `Live` | `Long` | `0.8455` | 84,490.00 USD | 0.00 USD | 15,800.00 USD | `-3.99%` | `18,690.40` |
| `Live` | `Long` | `0.8465` | 68,690.00 USD | 0.00 USD | 15,830.00 USD | `-3.88%` | `18,696.70` |
| `Live` | `Long` | `0.8475` | 52,860.00 USD | 0.00 USD | 10,800.00 USD | `-3.77%` | `12,740.30` |
| `Live` | `Long` | `0.8485` | 42,070.00 USD | 0.00 USD | 1,380.00 USD | `-3.65%` | `1,631.60` |
| `Live` | `Long` | `0.8495` | 40,680.00 USD | 0.00 USD | 804.99 USD | `-3.54%` | `947.60` |
| `Live` | `Long` | `0.8515` | 39,880.00 USD | 0.00 USD | 1,220.00 USD | `-3.31%` | `1,433.90` |
| `Live` | `Long` | `0.8525` | 38,660.00 USD | 0.00 USD | 3,050.00 USD | `-3.20%` | `3,575.40` |
| `Live` | `Long` | `0.8535` | 35,610.00 USD | 0.00 USD | 15,640.00 USD | `-3.09%` | `18,326.40` |
| `Live` | `Long` | `0.8545` | 19,970.00 USD | 0.00 USD | 2,810.00 USD | `-2.97%` | `3,294.20` |
| `Live` | `Long` | `0.8555` | 17,150.00 USD | 0.00 USD | 15,180.00 USD | `-2.86%` | `17,747.90` |
| `Live` | `Long` | `0.8585` | 1,970.00 USD | 0.00 USD | 1,170.00 USD | `-2.52%` | `1,367.50` |
| `Live` | `Long` | `0.8595` | 793.58 USD | 0.00 USD | 793.58 USD | `-2.40%` | `923.30` |
| `Live` | `Short` | `0.8795` | 841.24 USD | 841.24 USD | 0.00 USD | `-0.13%` | `956.50` |
| `Live` | `Short` | `0.9175` | 4,390.00 USD | 3,550.00 USD | 0.00 USD | `+4.18%` | `3,866.20` |
| `Live` | `Short` | `0.9265` | 23,860.00 USD | 19,470.00 USD | 0.00 USD | `+5.20%` | `21,018.40` |
| `Live` | `Short` | `0.9275` | 115,780.00 USD | 91,920.00 USD | 0.00 USD | `+5.32%` | `99,101.30` |
| `Live` | `Short` | `0.9385` | 119,440.00 USD | 3,670.00 USD | 0.00 USD | `+6.57%` | `3,906.50` |
| `Live` | `Short` | `0.9675` | 122,610.00 USD | 3,160.00 USD | 0.00 USD | `+9.86%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 187,670.00 USD | 65,060.00 USD | 0.00 USD | `+10.20%` | `67,040.50` |
| `Live` | `Short` | `0.9775` | 187,770.00 USD | 100.88 USD | 0.00 USD | `+11.00%` | `103.20` |
| `Live` | `Short` | `0.9805` | 188,820.00 USD | 1,050.00 USD | 0.00 USD | `+11.34%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 189,180.00 USD | 365.70 USD | 0.00 USD | `+12.02%` | `370.70` |
| `Live` | `Short` | `0.9885` | 194,110.00 USD | 4,930.00 USD | 0.00 USD | `+12.24%` | `4,982.50` |
| `Live` | `Short` | `0.9905` | 195,680.00 USD | 1,570.00 USD | 0.00 USD | `+12.47%` | `1,586.00` |
| `Live` | `Short` | `0.9925` | 198,090.00 USD | 2,420.00 USD | 0.00 USD | `+12.70%` | `2,434.50` |
| `Live` | `Short` | `1.00` | 198,430.00 USD | 330.29 USD | 0.00 USD | `+13.72%` | `329.80` |
| `Live` | `Short` | `1.02` | 198,600.00 USD | 170.40 USD | 0.00 USD | `+15.31%` | `167.80` |
| `Live` | `Short` | `1.04` | 198,750.00 USD | 155.92 USD | 0.00 USD | `+18.04%` | `150.00` |
| `Live` | `Short` | `1.04` | 198,890.00 USD | 139.22 USD | 0.00 USD | `+18.15%` | `133.80` |
| `Live` | `Short` | `1.05` | 199,490.00 USD | 597.52 USD | 0.00 USD | `+19.28%` | `568.80` |
| `Live` | `Short` | `1.05` | 201,880.00 USD | 2,390.00 USD | 0.00 USD | `+19.40%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 202,190.00 USD | 317.52 USD | 0.00 USD | `+19.62%` | `301.40` |
| `Live` | `Short` | `1.05` | 202,410.00 USD | 217.44 USD | 0.00 USD | `+19.74%` | `206.20` |
| `Live` | `Short` | `1.08` | 205,990.00 USD | 3,580.00 USD | 0.00 USD | `+22.69%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 206,160.00 USD | 166.43 USD | 0.00 USD | `+23.03%` | `153.60` |
| `Live` | `Short` | `1.09` | 211,710.00 USD | 5,550.00 USD | 0.00 USD | `+23.71%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 212,040.00 USD | 324.90 USD | 0.00 USD | `+24.85%` | `295.50` |
| `Live` | `Short` | `1.10` | 212,320.00 USD | 277.22 USD | 0.00 USD | `+24.96%` | `251.90` |
| `Live` | `Short` | `1.12` | 212,420.00 USD | 106.17 USD | 0.00 USD | `+27.57%` | `94.50` |
| `Live` | `Short` | `1.13` | 235,730.00 USD | 23,310.00 USD | 0.00 USD | `+27.91%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 236,360.00 USD | 634.09 USD | 0.00 USD | `+28.60%` | `559.90` |
| `Live` | `Short` | `1.20` | 237,820.00 USD | 1,450.00 USD | 0.00 USD | `+35.98%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 238,070.00 USD | 253.69 USD | 0.00 USD | `+36.20%` | `211.50` |
| `Live` | `Short` | `1.20` | 243,210.00 USD | 5,130.00 USD | 0.00 USD | `+36.43%` | `4,273.60` |
| `Live` | `Short` | `1.21` | 243,350.00 USD | 147.43 USD | 0.00 USD | `+36.88%` | `122.30` |
| `Live` | `Short` | `1.22` | 247,800.00 USD | 4,440.00 USD | 0.00 USD | `+38.36%` | `3,646.70` |
| `Live` | `Short` | `1.23` | 249,810.00 USD | 2,020.00 USD | 0.00 USD | `+39.61%` | `1,639.00` |
| `Live` | `Short` | `1.23` | 250,190.00 USD | 380.84 USD | 0.00 USD | `+40.18%` | `308.50` |
| `Live` | `Short` | `1.26` | 252,860.00 USD | 2,670.00 USD | 0.00 USD | `+43.02%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 256,220.00 USD | 3,360.00 USD | 0.00 USD | `+45.06%` | `2,630.40` |
| `Live` | `Short` | `1.28` | 296,100.00 USD | 39,880.00 USD | 0.00 USD | `+45.63%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 296,330.00 USD | 226.80 USD | 0.00 USD | `+46.99%` | `175.20` |
| `Live` | `Short` | `1.30` | 296,450.00 USD | 114.40 USD | 0.00 USD | `+47.44%` | `88.10` |
| `Live` | `Short` | `1.30` | 297,080.00 USD | 635.85 USD | 0.00 USD | `+48.01%` | `487.80` |
| `Live` | `Short` | `1.31` | 298,100.00 USD | 1,020.00 USD | 0.00 USD | `+48.69%` | `777.20` |
| `Live` | `Short` | `1.31` | 329,630.00 USD | 31,530.00 USD | 0.00 USD | `+48.92%` | `24,042.40` |
| `Live` | `Short` | `1.33` | 335,970.00 USD | 6,340.00 USD | 0.00 USD | `+50.51%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 357,940.00 USD | 21,970.00 USD | 0.00 USD | `+50.85%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 358,290.00 USD | 358.30 USD | 0.00 USD | `+51.08%` | `269.30` |
| `Live` | `Short` | `1.33` | 369,970.00 USD | 11,670.00 USD | 0.00 USD | `+51.31%` | `8,761.40` |
| `Live` | `Short` | `1.34` | 376,830.00 USD | 6,860.00 USD | 0.00 USD | `+52.10%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 398,630.00 USD | 21,800.00 USD | 0.00 USD | `+55.28%` | `15,941.90` |
| `Live` | `Short` | `1.37` | 756,910.00 USD | 358,280.00 USD | 0.00 USD | `+55.85%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 761,350.00 USD | 4,450.00 USD | 0.00 USD | `+60.62%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 761,760.00 USD | 402.08 USD | 0.00 USD | `+63.11%` | `279.90` |
| `Live` | `Short` | `1.44` | 762,040.00 USD | 288.68 USD | 0.00 USD | `+63.57%` | `200.40` |
| `Live` | `Short` | `1.48` | 762,470.00 USD | 428.43 USD | 0.00 USD | `+68.56%` | `288.60` |
| `Live` | `Short` | `1.50` | 772,190.00 USD | 9,710.00 USD | 0.00 USD | `+69.93%` | `6,491.20` |
| `Live` | `Short` | `1.51` | 776,210.00 USD | 4,020.00 USD | 0.00 USD | `+71.97%` | `2,654.10` |
| `Live` | `Short` | `1.52` | 776,340.00 USD | 128.48 USD | 0.00 USD | `+72.65%` | `84.50` |
| `Live` | `Short` | `1.53` | 776,850.00 USD | 517.25 USD | 0.00 USD | `+74.13%` | `337.30` |
| `Live` | `Short` | `1.54` | 777,000.00 USD | 144.34 USD | 0.00 USD | `+74.36%` | `94.00` |
| `Live` | `Short` | `1.54` | 794,200.00 USD | 17,200.00 USD | 0.00 USD | `+74.70%` | `11,182.60` |
| `Live` | `Short` | `1.58` | 794,490.00 USD | 285.21 USD | 0.00 USD | `+79.12%` | `180.80` |
| `Live` | `Short` | `1.63` | 796,700.00 USD | 2,210.00 USD | 0.00 USD | `+84.69%` | `1,360.10` |
| `Live` | `Short` | `1.65` | 825,670.00 USD | 28,970.00 USD | 0.00 USD | `+86.96%` | `17,593.40` |
| `Live` | `Short` | `1.66` | 864,740.00 USD | 39,070.00 USD | 0.00 USD | `+88.55%` | `23,529.40` |
| `Live` | `Short` | `1.67` | 1,150,000.00 USD | 288,480.00 USD | 0.00 USD | `+89.34%` | `173,000.00` |
| `Live` | `Short` | `1.68` | 1,150,000.00 USD | 437.85 USD | 0.00 USD | `+90.71%` | `260.70` |
| `Live` | `Short` | `1.69` | 1,150,000.00 USD | 165.81 USD | 0.00 USD | `+91.73%` | `98.20` |
| `Live` | `Short` | `1.71` | 1,160,000.00 USD | 9,630.00 USD | 0.00 USD | `+93.77%` | `5,645.40` |
| `Live` | `Short` | `1.71` | 1,160,000.00 USD | 205.67 USD | 0.00 USD | `+94.45%` | `120.10` |
| `Live` | `Short` | `1.73` | 1,160,000.00 USD | 226.05 USD | 0.00 USD | `+96.84%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,170,000.00 USD | 2,080.00 USD | 0.00 USD | `+97.63%` | `1,197.00` |
| `Live` | `Short` | `1.74` | 1,170,000.00 USD | 6,980.00 USD | 0.00 USD | `+98.09%` | `4,000.00` |
| `Live` | `Short` | `1.75` | 1,190,000.00 USD | 19,920.00 USD | 0.00 USD | `+98.88%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 1,200,000.00 USD | 11,350.00 USD | 0.00 USD | `+99.00%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,210,000.00 USD | 1,520.00 USD | 0.00 USD | `+99.22%` | `868.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,070,000.00 USD | 0.00 USD | 497.31 USD | `-70.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2745` | 1,070,000.00 USD | 0.00 USD | 455.97 USD | `-68.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,060,000.00 USD | 0.00 USD | 102.75 USD | `-61.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,060,000.00 USD | 0.00 USD | 256.78 USD | `-60.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,060,000.00 USD | 0.00 USD | 428.87 USD | `-55.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,060,000.00 USD | 0.00 USD | 123.45 USD | `-53.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,060,000.00 USD | 0.00 USD | 818.15 USD | `-52.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 1,060,000.00 USD | 0.00 USD | 454.04 USD | `-51.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,060,000.00 USD | 0.00 USD | 436.41 USD | `-50.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,060,000.00 USD | 0.00 USD | 876.79 USD | `-50.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,060,000.00 USD | 0.00 USD | 466.72 USD | `-48.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,060,000.00 USD | 0.00 USD | 142.95 USD | `-45.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,060,000.00 USD | 0.00 USD | 781.98 USD | `-43.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,060,000.00 USD | 0.00 USD | 151.74 USD | `-41.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,060,000.00 USD | 0.00 USD | 123.91 USD | `-41.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,060,000.00 USD | 0.00 USD | 219.80 USD | `-37.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,060,000.00 USD | 0.00 USD | 237,400.00 USD | `-37.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 821,940.00 USD | 0.00 USD | 276.75 USD | `-37.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 821,660.00 USD | 0.00 USD | 1,680.00 USD | `-36.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 819,980.00 USD | 0.00 USD | 119.76 USD | `-34.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 819,860.00 USD | 0.00 USD | 470.62 USD | `-32.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 819,390.00 USD | 0.00 USD | 108.39 USD | `-31.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 819,280.00 USD | 0.00 USD | 123.28 USD | `-31.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 819,160.00 USD | 0.00 USD | 488.52 USD | `-29.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 818,670.00 USD | 0.00 USD | 4,230.00 USD | `-28.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 814,450.00 USD | 0.00 USD | 242.24 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 814,200.00 USD | 0.00 USD | 193.95 USD | `-26.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 814,010.00 USD | 0.00 USD | 647.50 USD | `-26.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 813,360.00 USD | 0.00 USD | 834.79 USD | `-26.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 812,530.00 USD | 0.00 USD | 158.54 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 812,370.00 USD | 0.00 USD | 195.47 USD | `-25.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 812,170.00 USD | 0.00 USD | 190.25 USD | `-24.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 811,980.00 USD | 0.00 USD | 153.53 USD | `-24.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 811,830.00 USD | 0.00 USD | 52,450.00 USD | `-23.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 759,380.00 USD | 0.00 USD | 536.11 USD | `-23.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 758,850.00 USD | 0.00 USD | 918.68 USD | `-22.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 757,930.00 USD | 0.00 USD | 340.75 USD | `-22.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 757,590.00 USD | 0.00 USD | 9,270.00 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 748,320.00 USD | 0.00 USD | 120.53 USD | `-21.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 748,200.00 USD | 0.00 USD | 160.71 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 748,040.00 USD | 0.00 USD | 738.08 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 747,300.00 USD | 0.00 USD | 187.61 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 747,110.00 USD | 0.00 USD | 2,920.00 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 744,190.00 USD | 0.00 USD | 89,150.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 655,040.00 USD | 0.00 USD | 189.06 USD | `-19.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 654,850.00 USD | 0.00 USD | 5,650.00 USD | `-19.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 649,200.00 USD | 0.00 USD | 100.47 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 649,100.00 USD | 0.00 USD | 152.05 USD | `-19.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 648,950.00 USD | 0.00 USD | 123.41 USD | `-18.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 648,830.00 USD | 0.00 USD | 745.54 USD | `-17.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 648,080.00 USD | 0.00 USD | 1,130.00 USD | `-17.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 646,950.00 USD | 0.00 USD | 18,770.00 USD | `-16.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 628,180.00 USD | 0.00 USD | 257.26 USD | `-16.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 627,920.00 USD | 0.00 USD | 1,590.00 USD | `-15.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 626,330.00 USD | 0.00 USD | 10,160.00 USD | `-15.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 616,170.00 USD | 0.00 USD | 94,190.00 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 521,980.00 USD | 0.00 USD | 1,230.00 USD | `-14.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 520,750.00 USD | 0.00 USD | 1,840.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 518,910.00 USD | 0.00 USD | 804.61 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 518,110.00 USD | 0.00 USD | 191.12 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 517,920.00 USD | 0.00 USD | 273.92 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 517,640.00 USD | 0.00 USD | 125.92 USD | `-12.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 517,520.00 USD | 0.00 USD | 1,980.00 USD | `-12.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 515,540.00 USD | 0.00 USD | 1,150.00 USD | `-12.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 514,390.00 USD | 0.00 USD | 1,500.00 USD | `-11.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 512,900.00 USD | 0.00 USD | 1,860.00 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 511,040.00 USD | 0.00 USD | 128.47 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 510,910.00 USD | 0.00 USD | 10,090.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 500,820.00 USD | 0.00 USD | 135.11 USD | `-10.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 500,680.00 USD | 0.00 USD | 8,870.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 491,810.00 USD | 0.00 USD | 1,500.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 490,310.00 USD | 0.00 USD | 25,170.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 465,140.00 USD | 0.00 USD | 103.42 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 465,040.00 USD | 0.00 USD | 1,260.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 463,780.00 USD | 0.00 USD | 319.40 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 463,460.00 USD | 0.00 USD | 4,740.00 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 458,720.00 USD | 0.00 USD | 4,470.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 454,250.00 USD | 0.00 USD | 144.67 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 454,100.00 USD | 0.00 USD | 50,540.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 403,570.00 USD | 0.00 USD | 263.25 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 403,300.00 USD | 0.00 USD | 16,870.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 386,430.00 USD | 0.00 USD | 91,080.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 295,360.00 USD | 0.00 USD | 174.63 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 295,180.00 USD | 0.00 USD | 13,470.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 281,720.00 USD | 0.00 USD | 125.72 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 281,590.00 USD | 0.00 USD | 4,860.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 276,730.00 USD | 0.00 USD | 18,750.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 257,980.00 USD | 0.00 USD | 7,160.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 250,820.00 USD | 0.00 USD | 226.71 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 250,600.00 USD | 0.00 USD | 922.29 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 249,680.00 USD | 0.00 USD | 1,120.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 248,550.00 USD | 0.00 USD | 325.56 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 248,230.00 USD | 0.00 USD | 577.25 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 247,650.00 USD | 0.00 USD | 5,760.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 241,890.00 USD | 0.00 USD | 171.46 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 241,720.00 USD | 0.00 USD | 1,740.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 239,980.00 USD | 0.00 USD | 4,170.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 235,810.00 USD | 0.00 USD | 610.23 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 235,200.00 USD | 0.00 USD | 699.65 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 234,500.00 USD | 0.00 USD | 320.31 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 234,180.00 USD | 0.00 USD | 2,000.00 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 232,180.00 USD | 0.00 USD | 59,480.00 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 172,700.00 USD | 0.00 USD | 710.23 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 171,990.00 USD | 0.00 USD | 212.81 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 171,780.00 USD | 0.00 USD | 6,370.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 165,410.00 USD | 0.00 USD | 481.80 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 164,930.00 USD | 0.00 USD | 12,890.00 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 152,030.00 USD | 0.00 USD | 345.13 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 151,690.00 USD | 0.00 USD | 16,140.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 135,540.00 USD | 0.00 USD | 3,640.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 131,900.00 USD | 0.00 USD | 4,010.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 127,900.00 USD | 0.00 USD | 992.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 126,910.00 USD | 0.00 USD | 7,800.00 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 119,110.00 USD | 0.00 USD | 461.66 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 118,650.00 USD | 0.00 USD | 1,510.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 117,140.00 USD | 0.00 USD | 2,080.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 115,060.00 USD | 0.00 USD | 987.33 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 114,070.00 USD | 0.00 USD | 2,350.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 111,720.00 USD | 0.00 USD | 1,880.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 109,840.00 USD | 0.00 USD | 5,950.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 103,890.00 USD | 0.00 USD | 741.45 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 103,150.00 USD | 0.00 USD | 826.73 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 102,330.00 USD | 0.00 USD | 5,340.00 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 96,980.00 USD | 0.00 USD | 11,960.00 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 85,030.00 USD | 0.00 USD | 712.45 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 84,310.00 USD | 0.00 USD | 58,490.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 25,820.00 USD | 0.00 USD | 2,420.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 23,400.00 USD | 0.00 USD | 133.10 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 23,270.00 USD | 0.00 USD | 257.92 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 23,010.00 USD | 0.00 USD | 3,420.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 19,590.00 USD | 0.00 USD | 9,070.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 10,520.00 USD | 0.00 USD | 151.10 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 10,370.00 USD | 0.00 USD | 2,000.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 8,370.00 USD | 0.00 USD | 8,370.00 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8815` | 4,070.00 USD | 4,070.00 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8825` | 9,090.00 USD | 5,020.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8835` | 18,850.00 USD | 9,770.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 22,510.00 USD | 3,660.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 26,110.00 USD | 3,600.00 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 29,730.00 USD | 3,620.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 41,080.00 USD | 11,360.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 49,870.00 USD | 8,780.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 53,350.00 USD | 3,480.00 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 53,820.00 USD | 469.91 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 64,420.00 USD | 10,610.00 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 71,520.00 USD | 7,100.00 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 71,620.00 USD | 100.09 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 71,880.00 USD | 258.44 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 72,170.00 USD | 289.12 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 90,380.00 USD | 18,210.00 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 93,090.00 USD | 2,710.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 122,060.00 USD | 28,960.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 126,350.00 USD | 4,290.00 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 128,410.00 USD | 2,050.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 129,330.00 USD | 926.06 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 130,140.00 USD | 805.29 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 133,090.00 USD | 2,950.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 135,080.00 USD | 1,990.00 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 157,540.00 USD | 22,450.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 157,790.00 USD | 250.83 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 158,880.00 USD | 1,090.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 160,410.00 USD | 1,520.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 163,290.00 USD | 2,880.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 165,500.00 USD | 2,210.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 166,530.00 USD | 1,030.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 169,550.00 USD | 3,020.00 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 169,870.00 USD | 318.79 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 170,120.00 USD | 252.49 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 170,430.00 USD | 309.14 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 174,330.00 USD | 3,900.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 176,310.00 USD | 1,970.00 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 176,420.00 USD | 116.59 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 435,540.00 USD | 259,120.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 587,500.00 USD | 151,960.00 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 592,580.00 USD | 5,070.00 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 718,920.00 USD | 126,350.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 720,320.00 USD | 1,400.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 724,900.00 USD | 4,580.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 727,110.00 USD | 2,200.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 727,400.00 USD | 287.62 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 727,660.00 USD | 266.85 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 727,770.00 USD | 103.17 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 728,820.00 USD | 1,050.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 728,970.00 USD | 148.85 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 729,070.00 USD | 100.90 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 729,640.00 USD | 568.87 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 732,340.00 USD | 2,700.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 732,860.00 USD | 523.79 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 733,560.00 USD | 701.16 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 735,440.00 USD | 1,880.00 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 788,500.00 USD | 53,060.00 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 792,400.00 USD | 3,910.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 801,370.00 USD | 8,960.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 801,890.00 USD | 529.50 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 802,200.00 USD | 301.79 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 807,910.00 USD | 5,710.00 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 808,700.00 USD | 789.04 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 808,820.00 USD | 117.81 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 809,870.00 USD | 1,050.00 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 815,870.00 USD | 6,000.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 816,140.00 USD | 261.97 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 816,400.00 USD | 265.66 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 816,560.00 USD | 159.19 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 826,470.00 USD | 9,910.00 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 829,620.00 USD | 3,150.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 831,050.00 USD | 1,440.00 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 833,940.00 USD | 2,890.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 841,540.00 USD | 7,600.00 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 841,670.00 USD | 121.54 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 841,770.00 USD | 100.17 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 894,270.00 USD | 52,510.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 894,430.00 USD | 161.82 USD | 0.00 USD | `+9.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 914,300.00 USD | 19,870.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 914,440.00 USD | 139.23 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 915,780.00 USD | 1,340.00 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 915,980.00 USD | 204.20 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 916,520.00 USD | 531.57 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 919,680.00 USD | 3,160.00 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 920,670.00 USD | 993.78 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 920,880.00 USD | 212.90 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 932,560.00 USD | 11,680.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 932,690.00 USD | 125.61 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 933,130.00 USD | 441.51 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 943,430.00 USD | 10,300.00 USD | 0.00 USD | `+10.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 943,680.00 USD | 253.14 USD | 0.00 USD | `+10.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 947,880.00 USD | 4,200.00 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 948,060.00 USD | 176.73 USD | 0.00 USD | `+11.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 948,260.00 USD | 201.77 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 948,550.00 USD | 295.22 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 981,790.00 USD | 33,240.00 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 987,260.00 USD | 5,470.00 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 987,820.00 USD | 558.35 USD | 0.00 USD | `+11.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 988,880.00 USD | 1,060.00 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 990,120.00 USD | 1,240.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 990,610.00 USD | 490.99 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 991,250.00 USD | 644.82 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 992,250.00 USD | 991.50 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 1,000,000.00 USD | 10,340.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 1,000,000.00 USD | 409.52 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 1,000,000.00 USD | 284.92 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 1,000,000.00 USD | 277.64 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 1,000,000.00 USD | 350.37 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 1,000,000.00 USD | 144.04 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 1,000,000.00 USD | 105.44 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 1,010,000.00 USD | 8,760.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 1,570.00 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,020,000.00 USD | 2,180.00 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,020,000.00 USD | 363.87 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 589.52 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 110.62 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,030,000.00 USD | 10,090.00 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,030,000.00 USD | 5,420.00 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,040,000.00 USD | 2,080.00 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,040,000.00 USD | 248.49 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,070,000.00 USD | 33,450.00 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,070,000.00 USD | 722.63 USD | 0.00 USD | `+15.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,070,000.00 USD | 312.07 USD | 0.00 USD | `+15.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,070,000.00 USD | 171.24 USD | 0.00 USD | `+15.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,070,000.00 USD | 561.11 USD | 0.00 USD | `+15.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,070,000.00 USD | 249.30 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,070,000.00 USD | 2,210.00 USD | 0.00 USD | `+16.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,070,000.00 USD | 432.18 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,070,000.00 USD | 137.88 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,080,000.00 USD | 2,470.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,080,000.00 USD | 694.72 USD | 0.00 USD | `+17.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 160.60 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 6,560.00 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,090,000.00 USD | 2,920.00 USD | 0.00 USD | `+18.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,090,000.00 USD | 7,680.00 USD | 0.00 USD | `+18.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,090,000.00 USD | 224.56 USD | 0.00 USD | `+18.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,100,000.00 USD | 3,570.00 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,100,000.00 USD | 432.19 USD | 0.00 USD | `+19.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,100,000.00 USD | 5,890.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+19.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 1,810.00 USD | 0.00 USD | `+19.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 248.20 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,840,000.00 USD | 5,390.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,840,000.00 USD | 285.32 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,840,000.00 USD | 1,130.00 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,840,000.00 USD | 1,240.00 USD | 0.00 USD | `+20.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,840,000.00 USD | 278.06 USD | 0.00 USD | `+20.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,840,000.00 USD | 309.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,840,000.00 USD | 272.12 USD | 0.00 USD | `+21.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,840,000.00 USD | 117.12 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,980,000.00 USD | 140,120.00 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,980,000.00 USD | 530.01 USD | 0.00 USD | `+22.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,980,000.00 USD | 128.23 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,090,000.00 USD | 108,190.00 USD | 0.00 USD | `+22.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,090,000.00 USD | 550.49 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 5,810.00 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,100,000.00 USD | 5,570.00 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,100,000.00 USD | 1,290.00 USD | 0.00 USD | `+23.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,100,000.00 USD | 294.81 USD | 0.00 USD | `+24.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,100,000.00 USD | 183.11 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,100,000.00 USD | 123.13 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,100,000.00 USD | 494.98 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,100,000.00 USD | 613.52 USD | 0.00 USD | `+24.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,220,000.00 USD | 115,290.00 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,220,000.00 USD | 409.76 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,220,000.00 USD | 162.77 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,220,000.00 USD | 959.70 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,220,000.00 USD | 160.18 USD | 0.00 USD | `+25.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,220,000.00 USD | 669.85 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,220,000.00 USD | 293.61 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,330,000.00 USD | 112,050.00 USD | 0.00 USD | `+27.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,330,000.00 USD | 462.47 USD | 0.00 USD | `+27.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,340,000.00 USD | 2,180.00 USD | 0.00 USD | `+28.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,340,000.00 USD | 273.34 USD | 0.00 USD | `+28.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,340,000.00 USD | 119.49 USD | 0.00 USD | `+28.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,360,000.00 USD | 20,740.00 USD | 0.00 USD | `+28.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,360,000.00 USD | 468.47 USD | 0.00 USD | `+29.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,360,000.00 USD | 1,430.00 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,360,000.00 USD | 338.50 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,360,000.00 USD | 769.57 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,360,000.00 USD | 1,230.00 USD | 0.00 USD | `+30.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,360,000.00 USD | 2,450.00 USD | 0.00 USD | `+31.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,360,000.00 USD | 1,250.00 USD | 0.00 USD | `+31.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,360,000.00 USD | 143.67 USD | 0.00 USD | `+31.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,440,000.00 USD | 76,220.00 USD | 0.00 USD | `+32.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,440,000.00 USD | 304.33 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,440,000.00 USD | 241.65 USD | 0.00 USD | `+33.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,440,000.00 USD | 239.97 USD | 0.00 USD | `+33.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,440,000.00 USD | 2,470.00 USD | 0.00 USD | `+33.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,450,000.00 USD | 3,060.00 USD | 0.00 USD | `+34.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,760,000.00 USD | 310,250.00 USD | 0.00 USD | `+34.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,760,000.00 USD | 309.53 USD | 0.00 USD | `+35.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,760,000.00 USD | 159.09 USD | 0.00 USD | `+35.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,760,000.00 USD | 146.21 USD | 0.00 USD | `+35.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,840,000.00 USD | 78,160.00 USD | 0.00 USD | `+36.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,840,000.00 USD | 933.81 USD | 0.00 USD | `+36.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,840,000.00 USD | 658.86 USD | 0.00 USD | `+36.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,050,000.00 USD | 213,390.00 USD | 0.00 USD | `+37.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,050,000.00 USD | 211.10 USD | 0.00 USD | `+37.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,050,000.00 USD | 1,050.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,050,000.00 USD | 509.71 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,050,000.00 USD | 162.15 USD | 0.00 USD | `+39.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,050,000.00 USD | 187.04 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,050,000.00 USD | 542.12 USD | 0.00 USD | `+40.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,080,000.00 USD | 23,740.00 USD | 0.00 USD | `+40.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,080,000.00 USD | 2,010.00 USD | 0.00 USD | `+40.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,080,000.00 USD | 345.91 USD | 0.00 USD | `+40.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,080,000.00 USD | 104.79 USD | 0.00 USD | `+41.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,090,000.00 USD | 7,040.00 USD | 0.00 USD | `+41.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,090,000.00 USD | 517.52 USD | 0.00 USD | `+42.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,090,000.00 USD | 265.62 USD | 0.00 USD | `+42.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,090,000.00 USD | 1,480.00 USD | 0.00 USD | `+43.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,090,000.00 USD | 1,010.00 USD | 0.00 USD | `+43.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,090,000.00 USD | 340.38 USD | 0.00 USD | `+44.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,090,000.00 USD | 903.22 USD | 0.00 USD | `+44.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,090,000.00 USD | 475.01 USD | 0.00 USD | `+44.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,130,000.00 USD | 41,160.00 USD | 0.00 USD | `+44.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,150,000.00 USD | 12,840.00 USD | 0.00 USD | `+45.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,160,000.00 USD | 12,890.00 USD | 0.00 USD | `+46.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,170,000.00 USD | 8,820.00 USD | 0.00 USD | `+46.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,170,000.00 USD | 466.95 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,170,000.00 USD | 613.59 USD | 0.00 USD | `+46.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,170,000.00 USD | 1,420.00 USD | 0.00 USD | `+47.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,180,000.00 USD | 13,000.00 USD | 0.00 USD | `+47.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,180,000.00 USD | 1,150.00 USD | 0.00 USD | `+47.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 4,210,000.00 USD | 22,810.00 USD | 0.00 USD | `+49.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,210,000.00 USD | 640.82 USD | 0.00 USD | `+50.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 4,220,000.00 USD | 13,400.00 USD | 0.00 USD | `+52.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,230,000.00 USD | 13,490.00 USD | 0.00 USD | `+53.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,250,000.00 USD | 11,580.00 USD | 0.00 USD | `+53.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,250,000.00 USD | 3,610.00 USD | 0.00 USD | `+53.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,250,000.00 USD | 1,540.00 USD | 0.00 USD | `+54.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,250,000.00 USD | 1,500.00 USD | 0.00 USD | `+55.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,270,000.00 USD | 15,000.00 USD | 0.00 USD | `+55.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,280,000.00 USD | 9,030.00 USD | 0.00 USD | `+55.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,280,000.00 USD | 569.84 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,290,000.00 USD | 13,890.00 USD | 0.00 USD | `+57.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,290,000.00 USD | 2,710.00 USD | 0.00 USD | `+58.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,310,000.00 USD | 14,000.00 USD | 0.00 USD | `+58.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,320,000.00 USD | 13,100.00 USD | 0.00 USD | `+59.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,350,000.00 USD | 32,860.00 USD | 0.00 USD | `+59.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,360,000.00 USD | 7,090.00 USD | 0.00 USD | `+60.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,360,000.00 USD | 106.64 USD | 0.00 USD | `+60.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,360,000.00 USD | 1,430.00 USD | 0.00 USD | `+60.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,370,000.00 USD | 2,810.00 USD | 0.00 USD | `+60.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,370,000.00 USD | 8,420.00 USD | 0.00 USD | `+61.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,380,000.00 USD | 1,410.00 USD | 0.00 USD | `+61.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,380,000.00 USD | 431.38 USD | 0.00 USD | `+63.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,380,000.00 USD | 1,390.00 USD | 0.00 USD | `+63.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,390,000.00 USD | 14,390.00 USD | 0.00 USD | `+63.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,400,000.00 USD | 7,000.00 USD | 0.00 USD | `+64.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,400,000.00 USD | 434.98 USD | 0.00 USD | `+64.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,410,000.00 USD | 14,490.00 USD | 0.00 USD | `+64.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,410,000.00 USD | 1,370.00 USD | 0.00 USD | `+64.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,420,000.00 USD | 1,350.00 USD | 0.00 USD | `+66.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,420,000.00 USD | 1,340.00 USD | 0.00 USD | `+66.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,420,000.00 USD | 1,300.00 USD | 0.00 USD | `+67.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,420,000.00 USD | 342.08 USD | 0.00 USD | `+67.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,420,000.00 USD | 1,330.00 USD | 0.00 USD | `+67.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,420,000.00 USD | 1,320.00 USD | 0.00 USD | `+68.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,420,000.00 USD | 1,310.00 USD | 0.00 USD | `+69.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,440,000.00 USD | 14,890.00 USD | 0.00 USD | `+69.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,450,000.00 USD | 9,580.00 USD | 0.00 USD | `+69.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,460,000.00 USD | 14,980.00 USD | 0.00 USD | `+70.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,580,000.00 USD | 121,130.00 USD | 0.00 USD | `+70.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,580,000.00 USD | 1,270.00 USD | 0.00 USD | `+72.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,590,000.00 USD | 1,260.00 USD | 0.00 USD | `+73.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,590,000.00 USD | 1,980.00 USD | 0.00 USD | `+75.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,590,000.00 USD | 574.53 USD | 0.00 USD | `+80.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,590,000.00 USD | 391.32 USD | 0.00 USD | `+81.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,590,000.00 USD | 1,160.00 USD | 0.00 USD | `+83.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,590,000.00 USD | 1,140.00 USD | 0.00 USD | `+86.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,590,000.00 USD | 1,970.00 USD | 0.00 USD | `+86.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,590,000.00 USD | 281.45 USD | 0.00 USD | `+88.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 4,590,000.00 USD | 958.84 USD | 0.00 USD | `+91.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,600,000.00 USD | 3,550.00 USD | 0.00 USD | `+93.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,600,000.00 USD | 1,070.00 USD | 0.00 USD | `+98.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,600,000.00 USD | 320.52 USD | 0.00 USD | `+98.77%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7630` | 11,980,000.00 USD | 0.00 USD | 11,980,000.00 USD | 37,590.00 USD | 14,770.00 USD | 0.00 USD |
| `7D` | `0.7650` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 556.58 USD | 23,090.00 USD | 10,440.00 USD |
| `7D` | `0.7670` | 11,890,000.00 USD | 0.00 USD | 11,890,000.00 USD | 1,280.00 USD | 177.87 USD | 19,060.00 USD |
| `7D` | `0.7690` | 11,870,000.00 USD | 0.00 USD | 11,870,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD |
| `7D` | `0.7710` | 11,870,000.00 USD | 0.00 USD | 11,870,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7790` | 11,870,000.00 USD | 0.00 USD | 11,870,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD |
| `7D` | `0.7810` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 0.00 USD | 185.50 USD | 5,300.00 USD |
| `7D` | `0.7830` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 0.00 USD | 0.00 USD | 5,390.00 USD |
| `1D` | `0.7850` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 0.00 USD | 587.33 USD | 0.00 USD |
| `7D` | `0.7850` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD |
| `1D` | `0.7870` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 16,780.00 USD | 318.35 USD | 181.14 USD |
| `7D` | `0.7870` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD |
| `1D` | `0.7890` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 10,020.00 USD | 12,010.00 USD | 0.00 USD |
| `7D` | `0.7890` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 0.00 USD | 11,400.00 USD | 326.97 USD |
| `1D` | `0.7910` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 0.00 USD | 4,440.00 USD | 104.41 USD |
| `7D` | `0.7910` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 0.00 USD | 29,560.00 USD | 0.00 USD |
| `1D` | `0.7930` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 0.00 USD | 9,580.00 USD | 31,460.00 USD |
| `7D` | `0.7930` | 11,780,000.00 USD | 0.00 USD | 11,780,000.00 USD | 0.00 USD | 12,880.00 USD | 77,400.00 USD |
| `1D` | `0.7950` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 13,930.00 USD | 266.53 USD | 14,640.00 USD |
| `7D` | `0.7950` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 0.00 USD | 18,870.00 USD | 51,860.00 USD |
| `1D` | `0.7970` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 3,300.00 USD | 9,330.00 USD | 22,280.00 USD |
| `7D` | `0.7970` | 11,620,000.00 USD | 0.00 USD | 11,620,000.00 USD | 12,100.00 USD | 0.00 USD | 38,410.00 USD |
| `1D` | `0.7990` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 505.25 USD | 322.55 USD | 18,780.00 USD |
| `7D` | `0.7990` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 488.55 USD | 0.00 USD | 8,530.00 USD |
| `1D` | `0.8010` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 0.00 USD | 10,940.00 USD | 16,320.00 USD |
| `7D` | `0.8010` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 1,890.00 USD | 14,760.00 USD | 35,960.00 USD |
| `1D` | `0.8050` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 0.00 USD | 6,830.00 USD | 0.00 USD |
| `7D` | `0.8050` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 2,040.00 USD | 15,820.00 USD | 0.00 USD |
| `1D` | `0.8070` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 12,740.00 USD | 14,260.00 USD | 14,150.00 USD |
| `7D` | `0.8070` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD |
| `1D` | `0.8090` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `1D` | `0.8110` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 40,190.00 USD | 6,030.00 USD | 25,290.00 USD |
| `7D` | `0.8110` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,320.00 USD |
| `1D` | `0.8130` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 23,290.00 USD | 13,030.00 USD | 6,060.00 USD |
| `7D` | `0.8130` | 11,380,000.00 USD | 0.00 USD | 11,380,000.00 USD | 45,800.00 USD | 16,750.00 USD | 12,050.00 USD |
| `1D` | `0.8150` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 66,820.00 USD | 25,820.00 USD | 101,340.00 USD |
| `7D` | `0.8150` | 11,300,000.00 USD | 0.00 USD | 11,300,000.00 USD | 135,770.00 USD | 50,280.00 USD | 125,210.00 USD |
| `1D` | `0.8170` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 67,980.00 USD | 28,480.00 USD | 75,830.00 USD |
| `7D` | `0.8170` | 10,990,000.00 USD | 0.00 USD | 10,990,000.00 USD | 91,050.00 USD | 23,590.00 USD | 82,270.00 USD |
| `1D` | `0.8190` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 12,140.00 USD | 6,030.00 USD | 15,880.00 USD |
| `7D` | `0.8190` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 195,400.00 USD | 53,380.00 USD | 47,330.00 USD |
| `1D` | `0.8210` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 16,970.00 USD | 30,390.00 USD | 46,470.00 USD |
| `7D` | `0.8210` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 138,580.00 USD | 56,860.00 USD | 152,190.00 USD |
| `1D` | `0.8230` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 11,730.00 USD | 18,140.00 USD | 19,530.00 USD |
| `7D` | `0.8230` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 37,880.00 USD | 37,160.00 USD | 63,720.00 USD |
| `1D` | `0.8250` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 18,440.00 USD | 8,600.00 USD | 20,390.00 USD |
| `7D` | `0.8250` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 187,510.00 USD | 30,370.00 USD | 126,480.00 USD |
| `1D` | `0.8270` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 29,570.00 USD | 10,040.00 USD | 20,150.00 USD |
| `7D` | `0.8270` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 147,770.00 USD | 51,050.00 USD | 62,290.00 USD |
| `1D` | `0.8290` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 12,280.00 USD | 15,940.00 USD | 50,400.00 USD |
| `7D` | `0.8290` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 89,470.00 USD | 40,370.00 USD | 82,490.00 USD |
| `1D` | `0.8310` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 25,970.00 USD | 22,490.00 USD | 59,310.00 USD |
| `7D` | `0.8310` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 36,870.00 USD | 32,050.00 USD | 22,700.00 USD |
| `1D` | `0.8330` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 42,250.00 USD | 23,450.00 USD | 34,410.00 USD |
| `7D` | `0.8330` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 150,740.00 USD | 85,780.00 USD | 207,590.00 USD |
| `1D` | `0.8350` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 23,790.00 USD | 18,810.00 USD | 22,310.00 USD |
| `7D` | `0.8350` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 77,100.00 USD | 17,250.00 USD | 82,430.00 USD |
| `1D` | `0.8370` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 85,240.00 USD | 18,990.00 USD | 29,760.00 USD |
| `7D` | `0.8370` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 146,890.00 USD | 62,180.00 USD | 103,670.00 USD |
| `1D` | `0.8390` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 70,320.00 USD | 36,150.00 USD | 39,190.00 USD |
| `7D` | `0.8390` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 24,790.00 USD | 89,740.00 USD | 77,010.00 USD |
| `1D` | `0.8410` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 79,140.00 USD | 23,550.00 USD | 21,420.00 USD |
| `7D` | `0.8410` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 59,670.00 USD | 41,980.00 USD | 28,510.00 USD |
| `1D` | `0.8430` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 29,850.00 USD | 50,900.00 USD | 35,880.00 USD |
| `7D` | `0.8430` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 81,850.00 USD | 112,960.00 USD | 31,020.00 USD |
| `1D` | `0.8450` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 11,600.00 USD | 34,120.00 USD | 115,970.00 USD |
| `7D` | `0.8450` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 43,800.00 USD | 115,170.00 USD | 220,610.00 USD |
| `1D` | `0.8470` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 62,880.00 USD | 63,740.00 USD | 86,950.00 USD |
| `7D` | `0.8470` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 27,720.00 USD | 6,020.00 USD | 33,290.00 USD |
| `1D` | `0.8490` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 64,540.00 USD | 68,810.00 USD | 175,630.00 USD |
| `7D` | `0.8490` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 87,880.00 USD | 78,940.00 USD | 150,260.00 USD |
| `1D` | `0.8510` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 84,100.00 USD | 61,520.00 USD | 62,210.00 USD |
| `7D` | `0.8510` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 95,990.00 USD | 42,650.00 USD | 149,990.00 USD |
| `1D` | `0.8530` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 83,020.00 USD | 52,480.00 USD | 103,650.00 USD |
| `7D` | `0.8530` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 30,570.00 USD | 52,520.00 USD | 26,590.00 USD |
| `1D` | `0.8550` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 58,930.00 USD | 11,700.00 USD | 17,510.00 USD |
| `7D` | `0.8550` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 78,320.00 USD | 63,400.00 USD | 93,230.00 USD |
| `1D` | `0.8570` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 106,410.00 USD | 43,970.00 USD | 187.47 USD |
| `7D` | `0.8570` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 99,680.00 USD | 166,050.00 USD | 4,580.00 USD |
| `1D` | `0.8590` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 144,580.00 USD | 97,280.00 USD | 31,840.00 USD |
| `7D` | `0.8590` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 51,400.00 USD | 69,250.00 USD | 19,270.00 USD |
| `1D` | `0.8610` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 37,090.00 USD | 47,640.00 USD | 841.07 USD |
| `7D` | `0.8610` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 36,870.00 USD | 174,840.00 USD | 30,950.00 USD |
| `1D` | `0.8630` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 53,710.00 USD | 122,930.00 USD | 278,100.00 USD |
| `7D` | `0.8630` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 30,710.00 USD | 78,200.00 USD | 394,640.00 USD |
| `1D` | `0.8650` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 248,690.00 USD | 34,470.00 USD | 72,830.00 USD |
| `7D` | `0.8650` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 313,070.00 USD | 110,550.00 USD | 308,290.00 USD |
| `1D` | `0.8670` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 41,460.00 USD | 20,170.00 USD | 0.00 USD |
| `7D` | `0.8670` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 159,120.00 USD | 41,080.00 USD | 50,030.00 USD |
| `1D` | `0.8690` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 148,850.00 USD | 87,020.00 USD | 111,910.00 USD |
| `7D` | `0.8690` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 182,190.00 USD | 9,930.00 USD | 417,050.00 USD |
| `1D` | `0.8710` | 676,320.00 USD | 0.00 USD | 676,320.00 USD | 93,860.00 USD | 54,700.00 USD | 349,470.00 USD |
| `7D` | `0.8710` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 604,760.00 USD | 13,020.00 USD | 393,750.00 USD |
| `1D` | `0.8730` | 178,290.00 USD | 0.00 USD | 178,290.00 USD | 0.00 USD | 0.00 USD | 74,740.00 USD |
| `7D` | `0.8730` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 333,320.00 USD | 78,000.00 USD | 387,540.00 USD |
| `1D` | `0.8750` | 103,560.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | 103,560.00 USD |
| `7D` | `0.8750` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 643,280.00 USD | 7,500.00 USD | 318,630.00 USD |
| `1D` | `0.8760` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8770` | 695,720.00 USD | 0.00 USD | 695,720.00 USD | 398,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8790` | 6,560.00 USD | 6,560.00 USD | 0.00 USD | 6,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8790` | 296,940.00 USD | 0.00 USD | 296,940.00 USD | 296,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8810` | 12,250.00 USD | 12,250.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8810` | 26,040.00 USD | 26,040.00 USD | 0.00 USD | 26,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8810` | 52,090.00 USD | 52,090.00 USD | 0.00 USD | 26,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8830` | 13,480.00 USD | 13,480.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8830` | 79,970.00 USD | 79,970.00 USD | 0.00 USD | 27,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8870` | 13,820.00 USD | 13,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 340.71 USD |
| `1D` | `0.8890` | 13,820.00 USD | 13,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.70 USD |
| `7D` | `0.8890` | 969,280.00 USD | 969,280.00 USD | 0.00 USD | 884,290.00 USD | 0.00 USD | 5,020.00 USD |
| `1D` | `0.8910` | 210,780.00 USD | 210,780.00 USD | 0.00 USD | 186,060.00 USD | 10,900.00 USD | 0.66 USD |
| `7D` | `0.8910` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 806,690.00 USD | 0.00 USD | 3,460.00 USD |
| `1D` | `0.8930` | 255,870.00 USD | 255,870.00 USD | 0.00 USD | 44,660.00 USD | 0.00 USD | 431.84 USD |
| `7D` | `0.8930` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 1,760,000.00 USD | 0.00 USD | 3,630.00 USD |
| `1D` | `0.8950` | 436,050.00 USD | 436,050.00 USD | 0.00 USD | 98,920.00 USD | 48,760.00 USD | 32,510.00 USD |
| `7D` | `0.8950` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 719,730.00 USD | 56,980.00 USD | 1,620.00 USD |
| `1D` | `0.8970` | 458,270.00 USD | 458,270.00 USD | 0.00 USD | 0.00 USD | 22,220.00 USD | 0.00 USD |
| `7D` | `0.8970` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 659,500.00 USD | 54,550.00 USD | 470.27 USD |
| `1D` | `0.8990` | 915,710.00 USD | 915,710.00 USD | 0.00 USD | 51,680.00 USD | 127,660.00 USD | 278,090.00 USD |
| `7D` | `0.8990` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 308,910.00 USD | 64,400.00 USD | 341,380.00 USD |
| `1D` | `0.9010` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 249,240.00 USD | 99,300.00 USD | 230,990.00 USD |
| `7D` | `0.9010` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 207,550.00 USD | 109,410.00 USD | 215,220.00 USD |
| `1D` | `0.9030` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 3,140.00 USD | 76,840.00 USD | 56,510.00 USD |
| `7D` | `0.9030` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 5,880.00 USD | 78,550.00 USD | 1,730.00 USD |
| `1D` | `0.9050` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 144,360.00 USD | 134,060.00 USD | 111,910.00 USD |
| `7D` | `0.9050` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 122,230.00 USD | 0.00 USD | 219,130.00 USD |
| `1D` | `0.9070` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 111,680.00 USD | 55,120.00 USD | 175,480.00 USD |
| `7D` | `0.9070` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9090` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 167,160.00 USD | 11,830.00 USD | 0.00 USD |
| `7D` | `0.9090` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD |
| `1D` | `0.9110` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 70,890.00 USD | 34,900.00 USD | 0.00 USD |
| `7D` | `0.9110` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD |
| `1D` | `0.9130` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 62,740.00 USD | 15,770.00 USD |
| `7D` | `0.9130` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 80,230.00 USD | 62,970.00 USD | 0.00 USD |
| `1D` | `0.9150` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 119,590.00 USD | 92,390.00 USD | 300,270.00 USD |
| `7D` | `0.9150` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 111,690.00 USD | 111,780.00 USD | 169,890.00 USD |
| `1D` | `0.9170` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 106,060.00 USD | 95,530.00 USD | 63,130.00 USD |
| `7D` | `0.9170` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 123,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9190` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 26,960.00 USD | 27,310.00 USD | 28,090.00 USD |
| `7D` | `0.9190` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 296,480.00 USD | 60,800.00 USD | 104,960.00 USD |
| `1D` | `0.9210` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 47,610.00 USD | 60,370.00 USD | 124,270.00 USD |
| `7D` | `0.9210` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 128,930.00 USD | 16,660.00 USD | 178,830.00 USD |
| `1D` | `0.9230` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 230,840.00 USD | 75,900.00 USD | 273,100.00 USD |
| `7D` | `0.9230` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 51,510.00 USD | 66,370.00 USD | 341,030.00 USD |
| `1D` | `0.9250` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 195,300.00 USD | 37,890.00 USD | 122,770.00 USD |
| `7D` | `0.9250` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 52,570.00 USD | 43,650.00 USD | 67,880.00 USD |
| `1D` | `0.9270` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 99,610.00 USD | 63,980.00 USD |
| `7D` | `0.9270` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 209,950.00 USD | 40,600.00 USD | 89,770.00 USD |
| `1D` | `0.9290` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 38,710.00 USD | 21,240.00 USD | 89,530.00 USD |
| `7D` | `0.9290` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 4,480.00 USD | 53,740.00 USD | 0.00 USD |
| `1D` | `0.9310` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 104,570.00 USD | 67,630.00 USD | 48,820.00 USD |
| `7D` | `0.9310` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 177,720.00 USD | 46,670.00 USD | 166,200.00 USD |
| `1D` | `0.9330` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 32,530.00 USD | 39,200.00 USD | 35,380.00 USD |
| `7D` | `0.9330` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 76,570.00 USD | 63,160.00 USD |
| `1D` | `0.9350` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 757.65 USD | 13,120.00 USD | 0.00 USD |
| `7D` | `0.9350` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 53,950.00 USD | 54,380.00 USD | 3,770.00 USD |
| `1D` | `0.9370` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 198,110.00 USD | 84,650.00 USD | 261,310.00 USD |
| `7D` | `0.9370` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 251,760.00 USD | 1,370.00 USD | 42,430.00 USD |
| `1D` | `0.9390` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 171,940.00 USD | 72,440.00 USD | 149,290.00 USD |
| `7D` | `0.9390` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 86,850.00 USD | 34,800.00 USD | 263,790.00 USD |
| `1D` | `0.9410` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 52,890.00 USD | 4,990.00 USD | 55,120.00 USD |
| `7D` | `0.9410` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 123,000.00 USD | 2,780.00 USD | 0.00 USD |
| `1D` | `0.9430` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 702.40 USD | 3,090.00 USD | 17,940.00 USD |
| `7D` | `0.9430` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 66,560.00 USD | 33,660.00 USD |
| `1D` | `0.9450` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 6,770.00 USD | 76,490.00 USD | 240,780.00 USD |
| `7D` | `0.9450` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 3,360.00 USD | 244,270.00 USD | 90,360.00 USD |
| `1D` | `0.9470` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 92,510.00 USD | 52,870.00 USD | 44,590.00 USD |
| `7D` | `0.9470` | 12,280,000.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `1D` | `0.9490` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 71,990.00 USD | 62,590.00 USD | 58,150.00 USD |
| `7D` | `0.9490` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 107,340.00 USD | 119,200.00 USD |
| `1D` | `0.9510` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 53,450.00 USD | 49,760.00 USD | 175,780.00 USD |
| `7D` | `0.9510` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 2,840.00 USD | 88,970.00 USD | 733,450.00 USD |
| `1D` | `0.9530` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 32,500.00 USD | 26,060.00 USD | 124,860.00 USD |
| `7D` | `0.9530` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 2,190.00 USD |
| `1D` | `0.9550` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 50,010.00 USD | 82,110.00 USD | 35,430.00 USD |
| `7D` | `0.9550` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 74,980.00 USD | 2,400.00 USD | 61,370.00 USD |
| `1D` | `0.9570` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 8,380.00 USD | 2,420.00 USD | 303.02 USD |
| `7D` | `0.9570` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 463,830.00 USD | 3,460.00 USD | 951.74 USD |
| `1D` | `0.9590` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 33,930.00 USD | 53,830.00 USD | 12.64 USD |
| `7D` | `0.9590` | 14,500,000.00 USD | 14,500,000.00 USD | 0.00 USD | 562,050.00 USD | 1,040.00 USD | 344.34 USD |
| `1D` | `0.9610` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 207,270.00 USD | 108,280.00 USD | 290,770.00 USD |
| `7D` | `0.9610` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 698,570.00 USD | 190,470.00 USD | 479,490.00 USD |
| `1D` | `0.9630` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 329,630.00 USD | 84,410.00 USD | 128,960.00 USD |
| `7D` | `0.9630` | 17,370,000.00 USD | 17,370,000.00 USD | 0.00 USD | 579,300.00 USD | 301,610.00 USD | 619,200.00 USD |
| `1D` | `0.9650` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 168,910.00 USD | 139,810.00 USD | 82,410.00 USD |
| `7D` | `0.9650` | 18,950,000.00 USD | 18,950,000.00 USD | 0.00 USD | 857,470.00 USD | 312,610.00 USD | 411,000.00 USD |
| `1D` | `0.9670` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 264,730.00 USD | 113,900.00 USD | 239,150.00 USD |
| `7D` | `0.9670` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 889,580.00 USD | 555,340.00 USD | 708,670.00 USD |
| `1D` | `0.9690` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 235,940.00 USD | 92,380.00 USD | 238,910.00 USD |
| `7D` | `0.9690` | 22,550,000.00 USD | 22,550,000.00 USD | 0.00 USD | 596,350.00 USD | 356,560.00 USD | 489,060.00 USD |
| `1D` | `0.9710` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 170,370.00 USD | 69,530.00 USD | 117,350.00 USD |
| `7D` | `0.9710` | 23,650,000.00 USD | 23,650,000.00 USD | 0.00 USD | 645,500.00 USD | 319,140.00 USD | 133,390.00 USD |
| `1D` | `0.9730` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 80,510.00 USD | 64,370.00 USD | 70,810.00 USD |
| `7D` | `0.9730` | 24,440,000.00 USD | 24,440,000.00 USD | 0.00 USD | 456,990.00 USD | 160,420.00 USD | 172,340.00 USD |
| `1D` | `0.9750` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 58,820.00 USD | 45,650.00 USD | 103,200.00 USD |
| `7D` | `0.9750` | 25,150,000.00 USD | 25,150,000.00 USD | 0.00 USD | 203,760.00 USD | 293,590.00 USD | 216,550.00 USD |
| `1D` | `0.9770` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 15,370.00 USD | 8,230.00 USD | 41,600.00 USD |
| `7D` | `0.9770` | 26,200,000.00 USD | 26,200,000.00 USD | 0.00 USD | 329,170.00 USD | 211,000.00 USD | 503,880.00 USD |
| `1D` | `0.9790` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 19,400.00 USD | 33,280.00 USD | 105,520.00 USD |
| `7D` | `0.9790` | 26,930,000.00 USD | 26,930,000.00 USD | 0.00 USD | 411,780.00 USD | 99,560.00 USD | 221,890.00 USD |
| `1D` | `0.9810` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 100,630.00 USD | 45,360.00 USD | 103,390.00 USD |
| `7D` | `0.9810` | 27,440,000.00 USD | 27,440,000.00 USD | 0.00 USD | 264,890.00 USD | 83,040.00 USD | 168,620.00 USD |
| `1D` | `0.9830` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 106,220.00 USD | 40,920.00 USD | 20,340.00 USD |
| `7D` | `0.9830` | 28,030,000.00 USD | 28,030,000.00 USD | 0.00 USD | 262,900.00 USD | 116,030.00 USD | 203,790.00 USD |
| `1D` | `0.9850` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 22,370.00 USD | 48,410.00 USD | 6,030.00 USD |
| `7D` | `0.9850` | 28,430,000.00 USD | 28,430,000.00 USD | 0.00 USD | 234,160.00 USD | 58,210.00 USD | 114,800.00 USD |
| `1D` | `0.9870` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 56,760.00 USD | 31,400.00 USD | 98,240.00 USD |
| `7D` | `0.9870` | 28,950,000.00 USD | 28,950,000.00 USD | 0.00 USD | 248,980.00 USD | 203,100.00 USD | 65,410.00 USD |
| `1D` | `0.9890` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 100,670.00 USD | 33,420.00 USD | 33,960.00 USD |
| `7D` | `0.9890` | 29,240,000.00 USD | 29,240,000.00 USD | 0.00 USD | 194,850.00 USD | 78,280.00 USD | 16,890.00 USD |
| `1D` | `0.9910` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 80,470.00 USD | 30,860.00 USD | 50,980.00 USD |
| `7D` | `0.9910` | 29,610,000.00 USD | 29,610,000.00 USD | 0.00 USD | 198,890.00 USD | 89,640.00 USD | 78,900.00 USD |
| `1D` | `0.9930` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 33,580.00 USD | 16,590.00 USD | 15,190.00 USD |
| `7D` | `0.9930` | 29,980,000.00 USD | 29,980,000.00 USD | 0.00 USD | 228,340.00 USD | 63,950.00 USD | 76,400.00 USD |
| `7D` | `0.9950` | 30,300,000.00 USD | 30,300,000.00 USD | 0.00 USD | 48,120.00 USD | 138,500.00 USD | 130,770.00 USD |
| `7D` | `0.9970` | 30,950,000.00 USD | 30,950,000.00 USD | 0.00 USD | 215,040.00 USD | 81,210.00 USD | 356,400.00 USD |
| `7D` | `0.9990` | 31,230,000.00 USD | 31,230,000.00 USD | 0.00 USD | 145,170.00 USD | 35,870.00 USD | 101,390.00 USD |
| `7D` | `1.00` | 31,670,000.00 USD | 31,670,000.00 USD | 0.00 USD | 202,970.00 USD | 57,170.00 USD | 181,050.00 USD |
| `7D` | `1.00` | 32,170,000.00 USD | 32,170,000.00 USD | 0.00 USD | 226,340.00 USD | 61,540.00 USD | 207,930.00 USD |
| `7D` | `1.00` | 32,320,000.00 USD | 32,320,000.00 USD | 0.00 USD | 51,930.00 USD | 39,560.00 USD | 64,970.00 USD |
| `7D` | `1.01` | 32,810,000.00 USD | 32,810,000.00 USD | 0.00 USD | 256,020.00 USD | 15,900.00 USD | 211,810.00 USD |
| `7D` | `1.01` | 33,410,000.00 USD | 33,410,000.00 USD | 0.00 USD | 247,480.00 USD | 105,290.00 USD | 248,530.00 USD |
| `7D` | `1.01` | 34,200,000.00 USD | 34,200,000.00 USD | 0.00 USD | 398,890.00 USD | 134,240.00 USD | 260,960.00 USD |
| `7D` | `1.01` | 34,910,000.00 USD | 34,910,000.00 USD | 0.00 USD | 188,370.00 USD | 177,300.00 USD | 341,620.00 USD |
| `7D` | `1.01` | 35,260,000.00 USD | 35,260,000.00 USD | 0.00 USD | 168,660.00 USD | 59,720.00 USD | 124,410.00 USD |
| `7D` | `1.02` | 36,020,000.00 USD | 36,020,000.00 USD | 0.00 USD | 300,680.00 USD | 97,830.00 USD | 359,050.00 USD |
| `7D` | `1.02` | 36,860,000.00 USD | 36,860,000.00 USD | 0.00 USD | 291,360.00 USD | 74,810.00 USD | 471,150.00 USD |
| `7D` | `1.02` | 37,290,000.00 USD | 37,290,000.00 USD | 0.00 USD | 153,580.00 USD | 41,370.00 USD | 234,000.00 USD |
| `7D` | `1.02` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 151,650.00 USD | 60,000.00 USD | 103,520.00 USD |
| `7D` | `1.02` | 37,830,000.00 USD | 37,830,000.00 USD | 0.00 USD | 75,770.00 USD | 54,210.00 USD | 94,430.00 USD |
| `7D` | `1.03` | 38,080,000.00 USD | 38,080,000.00 USD | 0.00 USD | 104,260.00 USD | 35,230.00 USD | 111,210.00 USD |
| `7D` | `1.03` | 38,290,000.00 USD | 38,290,000.00 USD | 0.00 USD | 85,920.00 USD | 56,310.00 USD | 66,380.00 USD |
| `7D` | `1.03` | 38,640,000.00 USD | 38,640,000.00 USD | 0.00 USD | 168,010.00 USD | 58,600.00 USD | 128,070.00 USD |
| `7D` | `1.03` | 38,970,000.00 USD | 38,970,000.00 USD | 0.00 USD | 57,570.00 USD | 103,690.00 USD | 164,370.00 USD |
| `7D` | `1.03` | 39,110,000.00 USD | 39,110,000.00 USD | 0.00 USD | 64,880.00 USD | 13,040.00 USD | 63,490.00 USD |
| `7D` | `1.04` | 39,480,000.00 USD | 39,480,000.00 USD | 0.00 USD | 156,670.00 USD | 38,980.00 USD | 180,260.00 USD |
| `7D` | `1.04` | 39,790,000.00 USD | 39,790,000.00 USD | 0.00 USD | 110,420.00 USD | 18,150.00 USD | 175,610.00 USD |
| `7D` | `1.04` | 40,020,000.00 USD | 40,020,000.00 USD | 0.00 USD | 102,550.00 USD | 52,580.00 USD | 72,740.00 USD |
| `7D` | `1.04` | 40,110,000.00 USD | 40,110,000.00 USD | 0.00 USD | 18,340.00 USD | 48,310.00 USD | 25,070.00 USD |
| `7D` | `1.04` | 40,190,000.00 USD | 40,190,000.00 USD | 0.00 USD | 67,080.00 USD | 17,210.00 USD | 1,130.00 USD |
| `7D` | `1.05` | 40,300,000.00 USD | 40,300,000.00 USD | 0.00 USD | 76,550.00 USD | 30,790.00 USD | 327.64 USD |
| `7D` | `1.05` | 40,370,000.00 USD | 40,370,000.00 USD | 0.00 USD | 35,930.00 USD | 20,630.00 USD | 15,640.00 USD |
| `7D` | `1.05` | 40,400,000.00 USD | 40,400,000.00 USD | 0.00 USD | 22,610.00 USD | 0.00 USD | 390.75 USD |
| `7D` | `1.05` | 40,480,000.00 USD | 40,480,000.00 USD | 0.00 USD | 8,370.00 USD | 46,830.00 USD | 28,880.00 USD |
| `7D` | `1.05` | 40,540,000.00 USD | 40,540,000.00 USD | 0.00 USD | 1,650.00 USD | 9,420.00 USD | 46,110.00 USD |
| `7D` | `1.06` | 40,570,000.00 USD | 40,570,000.00 USD | 0.00 USD | 5,290.00 USD | 2,060.00 USD | 21,230.00 USD |
| `7D` | `1.06` | 40,570,000.00 USD | 40,570,000.00 USD | 0.00 USD | 0.00 USD | 638.17 USD | 0.00 USD |
| `7D` | `1.06` | 40,620,000.00 USD | 40,620,000.00 USD | 0.00 USD | 16,370.00 USD | 3,040.00 USD | 32,890.00 USD |
| `7D` | `1.06` | 40,630,000.00 USD | 40,630,000.00 USD | 0.00 USD | 11,330.00 USD | 0.00 USD | 204.99 USD |
| `7D` | `1.06` | 40,640,000.00 USD | 40,640,000.00 USD | 0.00 USD | 5,370.00 USD | 1,110.00 USD | 461.79 USD |
| `7D` | `1.07` | 40,640,000.00 USD | 40,640,000.00 USD | 0.00 USD | 0.00 USD | 1,120.00 USD | 146.51 USD |
| `7D` | `1.07` | 40,670,000.00 USD | 40,670,000.00 USD | 0.00 USD | 2,410.00 USD | 12,740.00 USD | 17,950.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `581.42M` | Total OI Tokens: `666,711,827.6 SUI`
  * 1h OI Change: `+1.17%` | 4h OI Change: `-5.32%` | 24h OI Change: `-8.63%`
  * Exchange Breakdown: Binance=`106.22M` | Bybit=`77.02M` | OKX=`33.14M` | Hyperliquid=`28.44M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-14.54K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0087%` | **USDT OKX** | `-0.0045%` |
| **USDT Bybit** | `-0.0066%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0087%` | **USDT BingX** | `0.0088%` |
| **USDT Gate** | `-0.0052%` | **USDT Bitget** | `0.0089%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `46.14%` | `53.86%` | `0.86` | 13,650,000.00 USD |
| `15M` | `Binance` | `53.11%` | `46.89%` | `1.13` | 5,590,000.00 USD |
| `15M` | `OKX` | `36.7%` | `63.3%` | `0.58` | 502,160.00 USD |
| `15M` | `Bybit` | `32.13%` | `67.87%` | `0.47` | 2,460,000.00 USD |
| `15M` | `KuCoin` | `62.62%` | `37.38%` | `1.68` | 44,170.00 USD |
| `15M` | `Gate` | `39.59%` | `60.41%` | `0.66` | 364,300.00 USD |
| `15M` | `Bitget` | `40.6%` | `59.4%` | `0.68` | 161,130.00 USD |
| `15M` | `BingX` | `38.46%` | `61.54%` | `0.62` | 882,290.00 USD |
| `15M` | `MEXC` | `39.37%` | `60.63%` | `0.65` | 292,960.00 USD |
| `15M` | `Bitunix` | `34.9%` | `65.1%` | `0.54` | 389,940.00 USD |
| `15M` | `Hyperliquid` | `25.85%` | `74.15%` | `0.35` | 348,640.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.38%` | `47.62%` | `1.10` | 2,360,000.00 USD |
| `15M` | `Crypto.com` | `48.74%` | `51.26%` | `0.95` | 32.44 USD |
| `15M` | `WhiteBIT` | `90.88%` | `9.12%` | `9.96` | 205,160.00 USD |
| `15M` | `HTX` | `10.45%` | `89.55%` | `0.12` | 2,870.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `28.83%` | `71.17%` | `0.41` | 4,430.00 USD |
| `15M` | `Aster` | `45.29%` | `54.71%` | `0.83` | 8,310.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `26.89%` | `73.11%` | `0.37` | 34,430.00 USD |
| `15M` | `Whale Positions` | `53.11%` | `46.89%` | `1.13` | 5,590,000.00 USD |
| `15M` | `Global Accounts` | `46.14%` | `53.86%` | `0.86` | 13,650,000.00 USD |
| `1H` | `SUI` | `49.39%` | `50.61%` | `0.98` | 47,480,000.00 USD |
| `1H` | `Binance` | `54.27%` | `45.73%` | `1.19` | 19,230,000.00 USD |
| `1H` | `OKX` | `46.69%` | `53.31%` | `0.88` | 2,680,000.00 USD |
| `1H` | `Bybit` | `34.73%` | `65.27%` | `0.53` | 5,760,000.00 USD |
| `1H` | `KuCoin` | `59.91%` | `40.09%` | `1.49` | 138,500.00 USD |
| `1H` | `Gate` | `44.1%` | `55.9%` | `0.79` | 1,200,000.00 USD |
| `1H` | `Bitget` | `48.34%` | `51.66%` | `0.94` | 877,970.00 USD |
| `1H` | `BingX` | `44.64%` | `55.36%` | `0.81` | 2,800,000.00 USD |
| `1H` | `MEXC` | `48.73%` | `51.27%` | `0.95` | 2,650,000.00 USD |
| `1H` | `Bitunix` | `44.21%` | `55.79%` | `0.79` | 1,130,000.00 USD |
| `1H` | `Hyperliquid` | `33.52%` | `66.48%` | `0.50` | 902,440.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.71%` | `50.29%` | `0.99` | 8,810,000.00 USD |
| `1H` | `Crypto.com` | `57.91%` | `42.09%` | `1.38` | 4,730.00 USD |
| `1H` | `WhiteBIT` | `87.5%` | `12.5%` | `7.00` | 1,010,000.00 USD |
| `1H` | `HTX` | `36.78%` | `63.22%` | `0.58` | 6,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.89%` | `47.11%` | `1.12` | 126,770.00 USD |
| `1H` | `Aster` | `66.03%` | `33.97%` | `1.94` | 25,990.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `24.64%` | `75.36%` | `0.33` | 132,100.00 USD |
| `1H` | `Whale Positions` | `54.27%` | `45.73%` | `1.19` | 19,230,000.00 USD |
| `1H` | `Global Accounts` | `49.39%` | `50.61%` | `0.98` | 47,480,000.00 USD |
| `4H` | `SUI` | `47.28%` | `52.72%` | `0.90` | 203,310,000.00 USD |
| `4H` | `Binance` | `47.78%` | `52.22%` | `0.91` | 82,740,000.00 USD |
| `4H` | `OKX` | `49.86%` | `50.14%` | `0.99` | 13,660,000.00 USD |
| `4H` | `Bybit` | `43.36%` | `56.64%` | `0.77` | 18,130,000.00 USD |
| `4H` | `KuCoin` | `48.47%` | `51.53%` | `0.94` | 1,350,000.00 USD |
| `4H` | `Gate` | `47.18%` | `52.82%` | `0.89` | 4,800,000.00 USD |
| `4H` | `Bitget` | `44.9%` | `55.1%` | `0.81` | 5,720,000.00 USD |
| `4H` | `BingX` | `48.79%` | `51.21%` | `0.95` | 14,260,000.00 USD |
| `4H` | `MEXC` | `48.11%` | `51.89%` | `0.93` | 13,070,000.00 USD |
| `4H` | `Bitunix` | `43.22%` | `56.78%` | `0.76` | 5,550,000.00 USD |
| `4H` | `Hyperliquid` | `42.09%` | `57.91%` | `0.73` | 4,970,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.24%` | `50.76%` | `0.97` | 32,690,000.00 USD |
| `4H` | `Crypto.com` | `56.74%` | `43.26%` | `1.31` | 43,330.00 USD |
| `4H` | `WhiteBIT` | `40.48%` | `59.52%` | `0.68` | 4,560,000.00 USD |
| `4H` | `HTX` | `51.96%` | `48.04%` | `1.08` | 76,720.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.35%` | `53.65%` | `0.86` | 705,210.00 USD |
| `4H` | `Aster` | `33.19%` | `66.81%` | `0.50` | 513,530.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.41%` | `57.59%` | `0.74` | 473,890.00 USD |
| `4H` | `Whale Positions` | `47.78%` | `52.22%` | `0.91` | 82,740,000.00 USD |
| `4H` | `Global Accounts` | `47.28%` | `52.72%` | `0.90` | 203,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.8801` | `0.8742` | `0.8801` | `0.8897` | `0.8575` | 25,765,113.89 USD | 12,461,836.10 USD | 13,303,277.79 USD | -841,441.70 USD | `-3.27%` | `7B / 12S` |
| `0:00 UTC` | `0.8841` | `0.8789` | `0.8841` | `0.8854` | `0.8692` | 12,554,511.67 USD | 6,312,205.57 USD | 6,242,306.10 USD | 69,899.48 USD | `+0.56%` | `13B / 6S` |
| `5:00 UTC` | `0.8962` | `0.8922` | `0.8962` | `0.8998` | `0.8850` | 10,029,099.72 USD | 5,129,823.74 USD | 4,899,275.97 USD | 230,547.77 USD | `+2.30%` | `13B / 7S` |
| `0:00 UTC` | `0.8977` | `0.8947` | `0.8977` | `0.9002` | `0.8853` | 5,070,824.21 USD | 2,682,042.86 USD | 2,388,781.36 USD | 293,261.50 USD | `+5.78%` | `18B / 23S` |
| `5:00 UTC` | `0.8865` | `0.8851` | `0.8865` | `0.8885` | `0.8800` | 5,162,774.90 USD | 2,355,111.64 USD | 2,807,663.26 USD | -452,551.62 USD | `-8.77%` | `10B / 8S` |
| `0:00 UTC` | `0.8800` | `0.8800` | `0.8800` | `0.8888` | `0.8720` | 7,652,579.47 USD | 3,792,343.47 USD | 3,860,236.00 USD | -67,892.53 USD | `-0.89%` | `30B / 17S` |
| `5:00 UTC` | `0.8861` | `0.8851` | `0.8861` | `0.8898` | `0.8777` | 3,749,314.34 USD | 2,064,688.13 USD | 1,684,626.21 USD | 380,061.92 USD | `+10.14%` | `11B / 8S` |
| `0:00 UTC` | `0.8863` | `0.8858` | `0.8863` | `0.8898` | `0.8814` | 2,957,541.44 USD | 1,492,061.57 USD | 1,465,479.88 USD | 26,581.69 USD | `+0.90%` | `10B / 13S` |
| `5:00 UTC` | `0.8800` | `0.8807` | `0.8800` | `0.8847` | `0.8777` | 3,693,620.20 USD | 1,638,820.39 USD | 2,054,799.81 USD | -415,979.42 USD | `-11.26%` | `7B / 10S` |
| `0:00 UTC` | `0.8776` | `0.8789` | `0.8776` | `0.8822` | `0.8761` | 687,636.63 USD | 203,033.83 USD | 484,602.80 USD | -281,568.97 USD | `-40.95%` | `6B / 27S` |

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
| `5m` | 224,630.00 USD | -647,800.00 USD | **`DISTRIBUTION`** |
| `15m` | 420,020.00 USD | -1,230,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 213,160.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 391,720.00 USD | -402,970.00 USD | **`DISTRIBUTION`** |
| `2h` | -286,790.00 USD | 377,020.00 USD | **`ACCUMULATION`** |
| `4h` | -8,120,000.00 USD | -11,770,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,300,000.00 USD | -14,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,770,000.00 USD | -16,300,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -3,980,000.00 USD | -16,970,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,670,000.00 USD | -27,610,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,930,000.00 USD | -77,120,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -150,620,000.00 USD | -475,970,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+224.63K` | 15m=`+420.02K` | 1h=`+391.72K` | 24h=`-8.67M`
* Futures Capital Netflows: 5m=`-647.80K` | 15m=`-1.23M` | 1h=`-402.97K` | 24h=`-27.61M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
