# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8846` | `0.8872` | `0.8803` | `0.8823` | `1,244,093` | 1,100,554.57 USD | -132,021.49 USD | `-12.00%` | -15,406,477.18 USD | `+0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.8824` | `0.8842` | `0.8759` | `0.8765` | `3,022,633` | 2,660,263.37 USD | -348,859.49 USD | `-13.11%` | -15,755,336.67 USD | `-0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.8764` | `0.8769` | `0.8760` | `0.8769` | `98,828` | 86,609.51 USD | 44,539.70 USD | `+51.43%` | -15,710,796.97 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.8929` | `0.9001` | `0.8853` | `0.8855` | `5,668,322` | 5,070,824.21 USD | 293,261.50 USD | `+5.78%` | -14,820,965.94 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.8854` | `0.8885` | `0.8799` | `0.8823` | `5,833,582` | 5,162,774.90 USD | -452,551.62 USD | `-8.77%` | -15,273,517.57 USD | `-0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.8824` | `0.8842` | `0.8759` | `0.8776` | `3,161,974` | 2,782,414.67 USD | -288,805.46 USD | `-10.38%` | -15,562,323.03 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9294` | `0.9303` | `0.8574` | `0.8737` | `71,708,417` | 63,836,842.40 USD | -6,009,876.59 USD | `-9.41%` | -15,181,110.62 USD | `-3.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8736` | `0.9001` | `0.8692` | `0.8823` | `37,030,182` | 32,817,210.50 USD | 141,157.12 USD | `+0.43%` | -15,039,953.50 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.8824` | `0.8842` | `0.8759` | `0.8766` | `3,115,313` | 2,741,484.16 USD | -303,097.82 USD | `-11.06%` | -15,343,051.32 USD | `+0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8766` | `111,852,878` | 99,394,629.58 USD | -6,171,397.77 USD | `-6.21%` | -15,333,961.30 USD | `-0.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -8,478,733.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -8,617,968.75 USD | `+0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8766` | `111,852,878` | 99,394,629.58 USD | -6,171,397.77 USD | `-6.21%` | -15,333,961.30 USD | `-0.97` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.8781` | `2405.0000` | 2,111.93 USD | 20,840.05 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.8781` | `139.7000` | 122.67 USD | 20,962.72 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8781` | `1699.3000` | 1,492.09 USD | 22,454.81 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.8782` | `5814.7000` | 5,106.76 USD | 14,611.03 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.8782` | `2265.5000` | 1,989.65 USD | 16,600.68 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8782` | `157.1000` | 137.97 USD | 16,738.65 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8782` | `2265.5000` | 1,989.47 USD | 18,728.12 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.96 USD | 8,604.71 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.96 USD | 8,704.67 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 8,804.62 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 8,904.58 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 9,004.53 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 9,104.48 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 9,204.43 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 9,304.38 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 9,404.32 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8783` | `113.8000` | 99.95 USD | 9,504.27 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8784` | `5700.3000` | 5,007.20 USD | 6,008.61 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8784` | `2841.7000` | 2,496.15 USD | 8,504.76 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `0.8787` | `2266.1000` | 1,991.22 USD | 1,991.22 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.8787` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.88` | `0.00%` | `-` |
| `BID` | `0.8787` | `1139.7000` | 1,001.41 USD | 1,001.41 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `0.8788` | `22.8000` | 20.04 USD | 6,113.38 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8788` | `2266.1000` | 1,991.40 USD | 6,093.34 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8788` | `2401.9000` | 2,110.72 USD | 4,101.94 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `0.8789` | `3911.5000` | 3,437.82 USD | 11,542.78 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `0.8789` | `2266.1000` | 1,991.58 USD | 8,104.96 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8790` | `2266.3000` | 1,992.19 USD | 18,408.91 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8790` | `1000.0000` | 879.04 USD | 16,416.72 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8790` | `2266.3000` | 1,992.01 USD | 15,537.68 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8790` | `2278.7000` | 2,002.89 USD | 13,545.67 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8791` | `21346.9000` | 18,767.13 USD | 47,549.85 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.8791` | `8514.6000` | 7,485.44 USD | 28,782.73 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.8791` | `2285.6000` | 2,009.32 USD | 21,297.29 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.8791` | `1000.0000` | 879.06 USD | 19,287.97 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8792` | `2266.3000` | 1,992.60 USD | 57,555.88 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8792` | `5695.1000` | 5,007.19 USD | 55,563.28 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8792` | `2266.3000` | 1,992.53 USD | 50,556.09 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8792` | `1153.0000` | 1,013.71 USD | 48,563.56 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8793` | `285.4000` | 250.95 USD | 60,306.76 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.8793` | `2843.2000` | 2,499.94 USD | 60,055.82 USD | `1 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `682` | `0xb83d...6e36` | `SHORT` | 3,372,514.32 USD | `3,817,609.40` | `1.11` | `0.8847` | `38.31` | 846,221.00 USD | `+25.09%` | `3X Cross` |
| `1024` | `0xa2ce...3126` | `LONG` | 2,206,634.18 USD | `2,500,010.40` | `0.8597` | `0.8847` | `0.000000` | 57,427.65 USD | `+2.60%` | `10X Cross` |
| `1546` | `0x9946...0852` | `SHORT` | 1,442,151.86 USD | `1,632,538.50` | `1.08` | `0.8847` | `1.78` | 319,597.27 USD | `+22.16%` | `10X Cross` |
| `1832` | `0x9aa5...58af` | `SHORT` | 1,136,177.76 USD | `1,288,168.80` | `1.14` | `0.8847` | `7.71` | 331,515.12 USD | `+29.18%` | `10X Cross` |
| `1918` | `0x9df2...c665` | `SHORT` | 1,060,092.00 USD | `1,200,000.00` | `0.7465` | `0.8847` | `26.51` | -164,239.60 USD | `-15.49%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9816` | 154.30 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.15K USD at 0.9816 USD [API] | `2026-09-21 08:38:19` |
| `ANNOUNCEMENT` | `INFO` | `0.9230` | 5,007.28 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9230 USD [API] | `2026-10-28 13:20:03` |
| `ANNOUNCEMENT` | `INFO` | `0.9224` | 5,007.13 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9224 USD [API] | `2026-10-28 13:30:10` |
| `ANNOUNCEMENT` | `INFO` | `0.9190` | 5,958.72 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.96K USD at 0.9190 USD [API] | `2026-10-28 13:52:39` |
| `ANNOUNCEMENT` | `INFO` | `0.9208` | 5,007.16 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9208 USD [API] | `2026-10-28 14:42:33` |
| `ANNOUNCEMENT` | `INFO` | `0.9254` | 7,207.83 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 7.21K USD at 0.9254 USD [API] | `2026-10-28 16:15:35` |
| `ANNOUNCEMENT` | `INFO` | `0.9231` | 5,006.10 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9231 USD [API] | `2026-10-28 16:22:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9261` | 34,626.23 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 34.63K USD at 0.9261 USD [API] | `2026-10-28 18:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 15.36 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.02K USD at 1.0593 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 399.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.40K USD at 1.0593 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 81.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.08K USD at 1.0591 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 81.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.08K USD at 1.0591 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `1.06` | 1,539.89 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.54K USD at 1.0590 USD [API] | `2026-09-25 01:02:00` |
| `ANNOUNCEMENT` | `INFO` | `0.9363` | 5,774.85 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.77K USD at 0.9363 USD [API] | `2026-10-28 18:40:34` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9682` (Vol: 265,800.00 USD, Dist: `+9.12%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.9707` (Vol: 232,500.00 USD, Dist: `+9.40%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.9707` (Vol: 232,500.00 USD, Dist: `+9.40%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.9713` (Vol: 513,800.00 USD, Dist: `+9.46%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1945` | 1,410.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 2,410.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 204.50 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 852.58 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 220.32 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 1,030.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 156.36 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 2,540.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 3,940.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,610.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 106.16 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 1,910.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 178.91 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 3,630.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 24,070.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 687.92 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 593.12 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 124.25 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 373.46 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3155` | 195.04 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3245` | 202.81 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3415` | 203.91 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3445` | 103.35 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3455` | 338.66 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 3,470.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 28,450.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3685` | 2,940.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3705` | 413.14 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3725` | 4,260.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3785` | 861.39 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3825` | 6,500.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3875` | 27,120.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 191.54 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4055` | 735.13 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 467.50 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4295` | 300.65 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4345` | 765.59 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4415` | 49,780.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 10,840.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 5,660.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 702.74 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 295.78 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4755` | 500.27 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4885` | 6,570.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 646.73 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 3,370.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,500.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 3,820.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 259.97 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,330.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 2,540.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 1,240.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 15,330.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 121.74 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5205` | 864.13 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 5,280.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5255` | 31,530.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 2,590.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 123,640.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,680.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5345` | 417.12 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5365` | 131.55 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 7,850.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 319.98 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5455` | 5,930.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 28,790.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 248.06 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 531.60 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5605` | 441.84 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 18,470.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 195.93 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 570.01 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 182.72 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 1,010.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 497.75 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 119.34 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 1,410.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 1,750.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,640.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 466.85 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5875` | 969.32 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 994.16 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 132.41 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,600.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 5,540.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 151.97 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 6,840.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 238.51 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 272.24 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6105` | 2,750.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,780.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 768.01 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6135` | 245.40 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 3,430.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 2,600.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 4,400.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 1,050.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6215` | 8,420.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 619.32 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 32,070.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 13,570.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6335` | 16,340.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 450.05 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 130.62 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6395` | 244.03 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 939.17 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 1,260.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 657.79 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,370.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 8,240.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 668.34 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 325,470.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 631.12 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 126,530.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 1,150.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 1,170.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 8,270.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 13,280.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 2,970.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 329.75 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 126,890.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 788.97 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 5,280.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 2,810.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,290.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 8,500.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 1,450.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 27,680.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 6,520.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 1,040.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 250.77 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 5,620.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 1,600.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6815` | 3,380.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 15,920.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 11,170.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,790.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 2,380.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 83,790.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 2,980.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 722.28 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 704.37 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 2,400.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 1,930.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6995` | 879.97 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 383.72 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 759.59 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 115.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 769.59 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 787.73 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 3,890.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 2,720.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 3,530.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 4,090.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 156.39 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7175` | 8,820.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 11,720.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7205` | 120.54 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 652.13 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 2,660.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 1,060.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 762.57 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 214.03 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 119.88 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7315` | 31,890.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7325` | 907.93 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 2,340.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 6,900.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 203.11 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7385` | 5,940.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7425` | 784,090.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 105.64 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7455` | 1,990.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 103,310.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7485` | 105.91 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 106.03 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 2,020.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 16,010.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7585` | 36,710.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 4,500.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7630` | 11,610,000.00 USD | 11,610,000.00 USD | 36,930.00 USD | 14,770.00 USD | 327.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 5,110.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 3,510.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 11,560,000.00 USD | 11,560,000.00 USD | 969.48 USD | 23,090.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 320,960.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7660` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 101.33 USD | 4,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7665` | 1,260.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 11,520,000.00 USD | 11,520,000.00 USD | 0.00 USD | 177.87 USD | 19,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 10,510.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 499.99 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 11,500,000.00 USD | 11,500,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 144,250.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 13,980.00 USD | 892,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 11,500,000.00 USD | 11,500,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 338.38 USD | 878,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 2,360.00 USD | 878,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 4,570.00 USD | 875,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 4,630.00 USD | 871,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 7,000.00 USD | 866,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 338.69 USD | 859,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7800` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 7,100.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7810` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 185.50 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 859,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 1,060.00 USD | 855,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7850` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7855` | 3,020.00 USD | 853,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 2,870.00 USD | 850,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 15,190.00 USD | 848,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7880` | 4,510,000.00 USD | 4,510,000.00 USD | 26,800.00 USD | 572.15 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 190.39 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 44,370.00 USD | 832,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7900` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 788,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 18,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 1,290.00 USD | 784,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 731.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 385.87 USD | 783,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7930` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 35,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.7940` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 4,350.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 9,190.00 USD | 783,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 11,400,000.00 USD | 11,400,000.00 USD | 9,530.00 USD | 6,180.00 USD | 51,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 23,720.00 USD | 773,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 428.05 USD | 11,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 11,330,000.00 USD | 11,330,000.00 USD | 9,430.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 1,170.00 USD | 750,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 4,450,000.00 USD | 4,450,000.00 USD | 2,830.00 USD | 8,900.00 USD | 10,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 1,840.00 USD | 749,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 11,310,000.00 USD | 11,310,000.00 USD | 911.48 USD | 0.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 2,580.00 USD | 747,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 11,260.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 635.04 USD | 744,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8010` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 14,760.00 USD | 35,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 6,810.00 USD | 744,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8030` | 11,250,000.00 USD | 11,250,000.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8035` | 316.42 USD | 737,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 41,410.00 USD | 736,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8050` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 15,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 1,610.00 USD | 695,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 4,400,000.00 USD | 4,400,000.00 USD | 12,740.00 USD | 13,670.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 11,230,000.00 USD | 11,230,000.00 USD | 2,040.00 USD | 11,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 1,220.00 USD | 693,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8080` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 8,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,460.00 USD | 692,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 4,350,000.00 USD | 4,350,000.00 USD | 12,970.00 USD | 5,430.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 670,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8110` | 11,220,000.00 USD | 11,220,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 3,050.00 USD | 667,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 4,310,000.00 USD | 4,310,000.00 USD | 27,480.00 USD | 1,350.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 2,480.00 USD | 664,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8130` | 11,120,000.00 USD | 11,120,000.00 USD | 44,870.00 USD | 16,750.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 11,260.00 USD | 662,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 4,280,000.00 USD | 4,280,000.00 USD | 44,940.00 USD | 23,740.00 USD | 22,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 651,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 11,040,000.00 USD | 11,040,000.00 USD | 137,850.00 USD | 50,280.00 USD | 125,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 8,160.00 USD | 650,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 4,190,000.00 USD | 4,190,000.00 USD | 111,700.00 USD | 22,860.00 USD | 149,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 1,440.00 USD | 642,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8170` | 10,730,000.00 USD | 10,730,000.00 USD | 90,990.00 USD | 23,590.00 USD | 78,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 103,450.00 USD | 641,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 3,900,000.00 USD | 3,900,000.00 USD | 11,610.00 USD | 20,880.00 USD | 20,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 2,070.00 USD | 537,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 10,540,000.00 USD | 10,540,000.00 USD | 194,350.00 USD | 52,010.00 USD | 47,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 29,980.00 USD | 535,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 3,850,000.00 USD | 3,850,000.00 USD | 13,230.00 USD | 16,660.00 USD | 36,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 505,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 10,240,000.00 USD | 10,240,000.00 USD | 137,160.00 USD | 56,860.00 USD | 152,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 6,900.00 USD | 503,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 3,780,000.00 USD | 3,780,000.00 USD | 12,100.00 USD | 19,830.00 USD | 30,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 2,570.00 USD | 496,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 9,900,000.00 USD | 9,900,000.00 USD | 38,600.00 USD | 35,700.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 216.00 USD | 494,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 3,720,000.00 USD | 3,720,000.00 USD | 21,120.00 USD | 16,700.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 1,140.00 USD | 493,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 9,760,000.00 USD | 9,760,000.00 USD | 188,770.00 USD | 27,530.00 USD | 126,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 4,550.00 USD | 492,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 3,660,000.00 USD | 3,660,000.00 USD | 17,700.00 USD | 4,440.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 9,420,000.00 USD | 9,420,000.00 USD | 141,740.00 USD | 51,050.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 11,410.00 USD | 488,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 3,630,000.00 USD | 3,630,000.00 USD | 22,620.00 USD | 12,830.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 126,740.00 USD | 476,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8290` | 9,160,000.00 USD | 9,160,000.00 USD | 88,370.00 USD | 40,370.00 USD | 82,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 32,530.00 USD | 349,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8300` | 3,560,000.00 USD | 3,560,000.00 USD | 13,880.00 USD | 9,690.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8305` | 1,880.00 USD | 317,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8310` | 8,950,000.00 USD | 8,950,000.00 USD | 38,140.00 USD | 32,050.00 USD | 24,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 3,510,000.00 USD | 3,510,000.00 USD | 19,130.00 USD | 29,090.00 USD | 67,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8325` | 20,930.00 USD | 315,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8330` | 8,850,000.00 USD | 8,850,000.00 USD | 152,500.00 USD | 85,780.00 USD | 200,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8335` | 234.71 USD | 294,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8340` | 3,390,000.00 USD | 3,390,000.00 USD | 49,780.00 USD | 16,200.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 8,420,000.00 USD | 8,420,000.00 USD | 76,840.00 USD | 15,430.00 USD | 83,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 17,770.00 USD | 294,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 3,280,000.00 USD | 3,280,000.00 USD | 75,630.00 USD | 23,510.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8370` | 8,240,000.00 USD | 8,240,000.00 USD | 146,620.00 USD | 60,250.00 USD | 101,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 2,420.00 USD | 276,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 3,160,000.00 USD | 3,160,000.00 USD | 29,780.00 USD | 14,800.00 USD | 28,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 75,120.00 USD | 274,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8390` | 7,930,000.00 USD | 7,930,000.00 USD | 26,140.00 USD | 87,820.00 USD | 78,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 26,770.00 USD | 199,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 3,090,000.00 USD | 3,090,000.00 USD | 80,010.00 USD | 26,570.00 USD | 33,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 1,320.00 USD | 172,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8410` | 7,740,000.00 USD | 7,740,000.00 USD | 54,830.00 USD | 40,110.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 48,540.00 USD | 170,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 2,950,000.00 USD | 2,950,000.00 USD | 45,210.00 USD | 35,080.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 2,230.00 USD | 122,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8430` | 7,620,000.00 USD | 7,620,000.00 USD | 77,650.00 USD | 84,470.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 6,280.00 USD | 120,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 2,840,000.00 USD | 2,840,000.00 USD | 21,450.00 USD | 12,010.00 USD | 291.54 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 133.18 USD | 113,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8450` | 7,420,000.00 USD | 7,420,000.00 USD | 50,250.00 USD | 55,690.00 USD | 114,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 6,340.00 USD | 113,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 2,810,000.00 USD | 2,810,000.00 USD | 3,860.00 USD | 23,780.00 USD | 40,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 15,830.00 USD | 107,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8470` | 7,200,000.00 USD | 7,200,000.00 USD | 25,980.00 USD | 6,020.00 USD | 34,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 28,990.00 USD | 91,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 2,740,000.00 USD | 2,740,000.00 USD | 46,950.00 USD | 35,940.00 USD | 85,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,890.00 USD | 62,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8490` | 7,140,000.00 USD | 7,140,000.00 USD | 43,620.00 USD | 32,060.00 USD | 152,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 5,290.00 USD | 60,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 2,570,000.00 USD | 2,570,000.00 USD | 56,320.00 USD | 51,020.00 USD | 155,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8505` | 958.26 USD | 55,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8510` | 6,910,000.00 USD | 6,910,000.00 USD | 93,500.00 USD | 42,650.00 USD | 78,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 54,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 2,310,000.00 USD | 2,310,000.00 USD | 96,680.00 USD | 61,140.00 USD | 66,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 6,690,000.00 USD | 6,690,000.00 USD | 39,890.00 USD | 52,520.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 15,640.00 USD | 53,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 2,090,000.00 USD | 2,090,000.00 USD | 56,450.00 USD | 46,460.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 6,580,000.00 USD | 6,580,000.00 USD | 69,370.00 USD | 63,400.00 USD | 93,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8555` | 17,220.00 USD | 37,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 1,920,000.00 USD | 1,920,000.00 USD | 28,740.00 USD | 27,040.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 15,610.00 USD | 20,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8570` | 6,350,000.00 USD | 6,350,000.00 USD | 96,770.00 USD | 166,050.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 1,850,000.00 USD | 1,850,000.00 USD | 180,840.00 USD | 34,130.00 USD | 114.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 2,200.00 USD | 4,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8590` | 6,080,000.00 USD | 6,080,000.00 USD | 57,950.00 USD | 12,270.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 1,550.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 1,640,000.00 USD | 1,640,000.00 USD | 32,470.00 USD | 33,380.00 USD | 636.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 6,000,000.00 USD | 6,000,000.00 USD | 49,960.00 USD | 120,290.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 1,570,000.00 USD | 1,570,000.00 USD | 6,610.00 USD | 35,120.00 USD | 666.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 5,790,000.00 USD | 5,790,000.00 USD | 25,030.00 USD | 13,800.00 USD | 181,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8640` | 1,530,000.00 USD | 1,530,000.00 USD | 40,460.00 USD | 34,720.00 USD | 126,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8650` | 5,570,000.00 USD | 5,570,000.00 USD | 227,130.00 USD | 16,780.00 USD | 308,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,330,000.00 USD | 1,330,000.00 USD | 184,320.00 USD | 33,670.00 USD | 271.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8670` | 5,020,000.00 USD | 5,020,000.00 USD | 159,830.00 USD | 41,080.00 USD | 52,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,110,000.00 USD | 1,110,000.00 USD | 98,550.00 USD | 70,170.00 USD | 112,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8685` | 265.76 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8690` | 4,760,000.00 USD | 4,760,000.00 USD | 175,280.00 USD | 9,930.00 USD | 267,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 798.46 USD | 798.46 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 826,270.00 USD | 826,270.00 USD | 59,260.00 USD | 6,380.00 USD | 898.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 4,310,000.00 USD | 4,310,000.00 USD | 619,190.00 USD | 13,020.00 USD | 390,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 759,730.00 USD | 759,730.00 USD | 1,300.00 USD | 54,700.00 USD | 308,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 3,290,000.00 USD | 3,290,000.00 USD | 318,460.00 USD | 78,000.00 USD | 387,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 394,830.00 USD | 394,830.00 USD | 0.00 USD | 19,580.00 USD | 45,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 2,510,000.00 USD | 2,510,000.00 USD | 648,980.00 USD | 118,620.00 USD | 318,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 329,670.00 USD | 329,670.00 USD | 3,590.00 USD | 34,150.00 USD | 178,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,420,000.00 USD | 1,420,000.00 USD | 405,620.00 USD | 14,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 113,020.00 USD | 113,020.00 USD | 5,990.00 USD | 0.00 USD | 305.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 999,150.00 USD | 999,150.00 USD | 293,480.00 USD | 67,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 106,720.00 USD | 106,720.00 USD | 7,330.00 USD | 60,300.00 USD | 722.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 638,050.00 USD | 638,050.00 USD | 637,180.00 USD | 0.00 USD | 869.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 38,360.00 USD | 38,360.00 USD | 36,230.00 USD | 0.00 USD | 305.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8830` | 773,660.00 USD | 773,660.00 USD | 768,360.00 USD | 0.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,820.00 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8850` | 1,300,000.00 USD | 1,300,000.00 USD | 523,060.00 USD | 0.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8860` | 745.79 USD | 745.79 USD | 0.00 USD | 0.00 USD | 745.79 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8870` | 1,930,000.00 USD | 1,930,000.00 USD | 626,010.00 USD | 0.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8890` | 3,470,000.00 USD | 3,470,000.00 USD | 1,530,000.00 USD | 0.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8900` | 3,090.00 USD | 3,090.00 USD | 2,250.00 USD | 0.00 USD | 95.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8910` | 4,280,000.00 USD | 4,280,000.00 USD | 806,690.00 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 189,680.00 USD | 189,680.00 USD | 186,330.00 USD | 0.00 USD | 252.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8930` | 6,060,000.00 USD | 6,060,000.00 USD | 1,770,000.00 USD | 0.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8935` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8940` | 282,640.00 USD | 282,640.00 USD | 92,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8950` | 6,800,000.00 USD | 6,800,000.00 USD | 744,640.00 USD | 0.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8970` | 7,480,000.00 USD | 7,480,000.00 USD | 674,170.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8980` | 282,850.00 USD | 282,850.00 USD | 0.00 USD | 0.00 USD | 207.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8990` | 7,920,000.00 USD | 7,920,000.00 USD | 305,920.00 USD | 0.00 USD | 129,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9000` | 581,210.00 USD | 581,210.00 USD | 73,470.00 USD | 68,200.00 USD | 156,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 8,290,000.00 USD | 8,290,000.00 USD | 139,730.00 USD | 15,640.00 USD | 211,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 973,080.00 USD | 973,080.00 USD | 112,580.00 USD | 96,290.00 USD | 183,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9025` | 818.48 USD | 4,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9030` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 78,550.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9035` | 9,040.00 USD | 13,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9040` | 1,330,000.00 USD | 1,330,000.00 USD | 95,230.00 USD | 146,230.00 USD | 112,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9045` | 191.39 USD | 13,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9050` | 8,570,000.00 USD | 8,570,000.00 USD | 125,280.00 USD | 0.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9055` | 61,580.00 USD | 75,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9060` | 1,420,000.00 USD | 1,420,000.00 USD | 76,970.00 USD | 17,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 8,910,000.00 USD | 8,910,000.00 USD | 341,080.00 USD | 0.00 USD | 920.04 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9075` | 717.74 USD | 75,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9080` | 1,650,000.00 USD | 1,650,000.00 USD | 92,600.00 USD | 55,120.00 USD | 81,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 9,250,000.00 USD | 9,250,000.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 1,770,000.00 USD | 1,770,000.00 USD | 96,000.00 USD | 25,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 9,570,000.00 USD | 9,570,000.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 1,850,000.00 USD | 1,850,000.00 USD | 25,050.00 USD | 53,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 9,680,000.00 USD | 9,680,000.00 USD | 80,230.00 USD | 34,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 2,100,000.00 USD | 2,100,000.00 USD | 79,560.00 USD | 25,930.00 USD | 142,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 9,910,000.00 USD | 9,910,000.00 USD | 111,690.00 USD | 52,310.00 USD | 64,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9155` | 150.14 USD | 76,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9160` | 2,340,000.00 USD | 2,340,000.00 USD | 74,950.00 USD | 95,790.00 USD | 71,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 10,030,000.00 USD | 10,030,000.00 USD | 123,530.00 USD | 0.00 USD | 653.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 2,440,000.00 USD | 2,440,000.00 USD | 38,060.00 USD | 24,510.00 USD | 36,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 10,410,000.00 USD | 10,410,000.00 USD | 257,890.00 USD | 13,920.00 USD | 104,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9195` | 36,140.00 USD | 112,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 8,860.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9205` | 12,970.00 USD | 125,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9210` | 10,660,000.00 USD | 10,660,000.00 USD | 128,930.00 USD | 16,660.00 USD | 102,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9215` | 2,090.00 USD | 127,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9220` | 2,950,000.00 USD | 2,950,000.00 USD | 149,120.00 USD | 72,360.00 USD | 246,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 11,120,000.00 USD | 11,120,000.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9235` | 234.48 USD | 127,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9240` | 3,410,000.00 USD | 3,410,000.00 USD | 217,830.00 USD | 59,780.00 USD | 184,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9245` | 4,390.00 USD | 131,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9250` | 11,280,000.00 USD | 11,280,000.00 USD | 52,570.00 USD | 41,710.00 USD | 67,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9255` | 9,870.00 USD | 141,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9260` | 3,650,000.00 USD | 3,650,000.00 USD | 63,790.00 USD | 81,480.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9265` | 7,270.00 USD | 149,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9270` | 11,620,000.00 USD | 11,620,000.00 USD | 209,950.00 USD | 38,670.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9275` | 31,110.00 USD | 180,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9280` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 64,220.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9285` | 1,360.00 USD | 181,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9290` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 51,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9295` | 62,570.00 USD | 244,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9300` | 3,950,000.00 USD | 3,950,000.00 USD | 41,680.00 USD | 57,070.00 USD | 79,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9305` | 3,830.00 USD | 247,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9310` | 12,060,000.00 USD | 12,060,000.00 USD | 177,720.00 USD | 46,670.00 USD | 166,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 4,150,000.00 USD | 4,150,000.00 USD | 128,960.00 USD | 29,480.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 76,570.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9335` | 116.31 USD | 248,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9340` | 4,180,000.00 USD | 4,180,000.00 USD | 2,150.00 USD | 31,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9345` | 2,100.00 USD | 250,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9350` | 12,300,000.00 USD | 12,300,000.00 USD | 50,160.00 USD | 54,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 4,350,000.00 USD | 4,350,000.00 USD | 25,730.00 USD | 33,250.00 USD | 107,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9365` | 1,750.00 USD | 251,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9370` | 12,600,000.00 USD | 12,600,000.00 USD | 255,550.00 USD | 0.00 USD | 42,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 5,030,000.00 USD | 5,030,000.00 USD | 262,840.00 USD | 118,850.00 USD | 298,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 12,980,000.00 USD | 12,980,000.00 USD | 82,760.00 USD | 34,800.00 USD | 263,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 5,220,000.00 USD | 5,220,000.00 USD | 123,820.00 USD | 1,710.00 USD | 67,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 13,110,000.00 USD | 13,110,000.00 USD | 123,000.00 USD | 1,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 5,250,000.00 USD | 5,250,000.00 USD | 9,740.00 USD | 3,830.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 13,210,000.00 USD | 13,210,000.00 USD | 4,090.00 USD | 63,720.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 5,400,000.00 USD | 5,400,000.00 USD | 3,840.00 USD | 77,580.00 USD | 73,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 244,270.00 USD | 90,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 5,680,000.00 USD | 5,680,000.00 USD | 59,870.00 USD | 33,530.00 USD | 184,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 211,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 5,900,000.00 USD | 5,900,000.00 USD | 89,360.00 USD | 67,670.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 107,340.00 USD | 119,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 6,020,000.00 USD | 6,020,000.00 USD | 17,970.00 USD | 36,000.00 USD | 69,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 14,810,000.00 USD | 14,810,000.00 USD | 7,120.00 USD | 88,970.00 USD | 733,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 6,300,000.00 USD | 6,300,000.00 USD | 52,120.00 USD | 28,040.00 USD | 196,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 14,810,000.00 USD | 14,810,000.00 USD | 2,840.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 6,520,000.00 USD | 6,520,000.00 USD | 62,990.00 USD | 74,340.00 USD | 81,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 14,940,000.00 USD | 14,940,000.00 USD | 61,410.00 USD | 2,400.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 6,590,000.00 USD | 6,590,000.00 USD | 27,900.00 USD | 36,240.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 15,400,000.00 USD | 15,400,000.00 USD | 459,560.00 USD | 3,460.00 USD | 578.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 6,620,000.00 USD | 6,620,000.00 USD | 689.00 USD | 27,470.00 USD | 159.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 15,970,000.00 USD | 15,970,000.00 USD | 570,590.00 USD | 1,040.00 USD | 899.71 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 6,880,000.00 USD | 6,880,000.00 USD | 111,160.00 USD | 66,100.00 USD | 82,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 17,330,000.00 USD | 17,330,000.00 USD | 683,980.00 USD | 190,470.00 USD | 476,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 7,580,000.00 USD | 7,580,000.00 USD | 315,960.00 USD | 137,300.00 USD | 239,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 18,840,000.00 USD | 18,840,000.00 USD | 592,010.00 USD | 301,610.00 USD | 616,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 8,210,000.00 USD | 8,210,000.00 USD | 334,070.00 USD | 100,680.00 USD | 197,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 20,390,000.00 USD | 20,390,000.00 USD | 846,210.00 USD | 301,210.00 USD | 411,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 8,690,000.00 USD | 8,690,000.00 USD | 226,860.00 USD | 139,760.00 USD | 120,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 22,540,000.00 USD | 22,540,000.00 USD | 900,420.00 USD | 544,430.00 USD | 703,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 255,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9680` | 9,240,000.00 USD | 9,240,000.00 USD | 199,180.00 USD | 70,260.00 USD | 280,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 23,940,000.00 USD | 23,940,000.00 USD | 600,420.00 USD | 343,680.00 USD | 453,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 9,800,000.00 USD | 9,800,000.00 USD | 257,240.00 USD | 106,950.00 USD | 189,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 320,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9710` | 25,020,000.00 USD | 25,020,000.00 USD | 641,170.00 USD | 306,450.00 USD | 129,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 10,080,000.00 USD | 10,080,000.00 USD | 100,350.00 USD | 77,980.00 USD | 110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 25,800,000.00 USD | 25,800,000.00 USD | 453,940.00 USD | 160,420.00 USD | 173,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 10,240,000.00 USD | 10,240,000.00 USD | 81,230.00 USD | 31,010.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 26,480,000.00 USD | 26,480,000.00 USD | 193,900.00 USD | 293,590.00 USD | 189,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 10,390,000.00 USD | 10,390,000.00 USD | 31,860.00 USD | 33,470.00 USD | 87,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9765` | 214.44 USD | 320,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9770` | 27,520,000.00 USD | 27,520,000.00 USD | 329,800.00 USD | 211,000.00 USD | 499,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9775` | 100.88 USD | 320,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9780` | 10,510,000.00 USD | 10,510,000.00 USD | 4,640.00 USD | 25,130.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 28,270,000.00 USD | 28,270,000.00 USD | 424,270.00 USD | 99,560.00 USD | 225,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 10,750,000.00 USD | 10,750,000.00 USD | 65,550.00 USD | 48,270.00 USD | 127,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 321,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 28,780,000.00 USD | 28,780,000.00 USD | 256,520.00 USD | 83,040.00 USD | 168,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 10,960,000.00 USD | 10,960,000.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 29,350,000.00 USD | 29,350,000.00 USD | 259,110.00 USD | 116,030.00 USD | 199,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 11,100,000.00 USD | 11,100,000.00 USD | 58,950.00 USD | 60,590.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9845` | 10,440.00 USD | 331,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9850` | 29,770,000.00 USD | 29,770,000.00 USD | 241,230.00 USD | 58,210.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 11,320,000.00 USD | 11,320,000.00 USD | 74,810.00 USD | 44,550.00 USD | 100,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 30,290,000.00 USD | 30,290,000.00 USD | 250,680.00 USD | 203,100.00 USD | 63,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 732.03 USD | 332,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 11,470,000.00 USD | 11,470,000.00 USD | 82,930.00 USD | 24,280.00 USD | 49,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,930.00 USD | 337,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9890` | 30,580,000.00 USD | 30,580,000.00 USD | 191,750.00 USD | 78,280.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 11,640,000.00 USD | 11,640,000.00 USD | 87,940.00 USD | 34,700.00 USD | 42,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 1,570.00 USD | 339,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9910` | 30,950,000.00 USD | 30,950,000.00 USD | 201,490.00 USD | 89,640.00 USD | 85,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 11,720,000.00 USD | 11,720,000.00 USD | 49,210.00 USD | 20,540.00 USD | 16,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,420.00 USD | 341,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 31,320,000.00 USD | 31,320,000.00 USD | 230,590.00 USD | 63,950.00 USD | 74,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 11,890,000.00 USD | 11,890,000.00 USD | 60,860.00 USD | 36,590.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 31,640,000.00 USD | 31,640,000.00 USD | 53,860.00 USD | 138,500.00 USD | 126,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 11,920,000.00 USD | 11,920,000.00 USD | 6,270.00 USD | 5,900.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9965` | 125.66 USD | 341,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9970` | 32,300,000.00 USD | 32,300,000.00 USD | 218,800.00 USD | 81,210.00 USD | 354,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 12,200,000.00 USD | 12,200,000.00 USD | 110,050.00 USD | 20,740.00 USD | 149,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 32,560,000.00 USD | 32,560,000.00 USD | 125,550.00 USD | 35,870.00 USD | 101,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,260,000.00 USD | 12,260,000.00 USD | 16,340.00 USD | 21,440.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 33,010,000.00 USD | 33,010,000.00 USD | 212,210.00 USD | 57,170.00 USD | 181,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,330,000.00 USD | 12,330,000.00 USD | 15,000.00 USD | 17,420.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 33,510,000.00 USD | 33,510,000.00 USD | 227,430.00 USD | 61,540.00 USD | 209,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,400,000.00 USD | 12,400,000.00 USD | 15,370.00 USD | 21,270.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 33,660,000.00 USD | 33,660,000.00 USD | 49,730.00 USD | 39,560.00 USD | 65,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,430,000.00 USD | 12,430,000.00 USD | 9,400.00 USD | 13,960.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,150,000.00 USD | 34,150,000.00 USD | 256,670.00 USD | 15,900.00 USD | 215,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,470,000.00 USD | 12,470,000.00 USD | 17,690.00 USD | 8,610.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 34,750,000.00 USD | 34,750,000.00 USD | 248,390.00 USD | 105,290.00 USD | 247,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,500,000.00 USD | 12,500,000.00 USD | 17,560.00 USD | 5,290.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 35,640,000.00 USD | 35,640,000.00 USD | 457,310.00 USD | 174,650.00 USD | 258,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,570,000.00 USD | 12,570,000.00 USD | 21,660.00 USD | 13,540.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 36,350,000.00 USD | 36,350,000.00 USD | 191,660.00 USD | 177,300.00 USD | 340,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,620,000.00 USD | 12,620,000.00 USD | 13,360.00 USD | 10,400.00 USD | 25,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 36,790,000.00 USD | 36,790,000.00 USD | 256,090.00 USD | 59,720.00 USD | 126,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 341,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,660,000.00 USD | 12,660,000.00 USD | 21,410.00 USD | 10,550.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 37,600,000.00 USD | 37,600,000.00 USD | 344,600.00 USD | 97,830.00 USD | 360,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,680,000.00 USD | 12,680,000.00 USD | 18,050.00 USD | 4,150.00 USD | 133.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 38,430,000.00 USD | 38,430,000.00 USD | 293,320.00 USD | 74,810.00 USD | 468,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,770,000.00 USD | 12,770,000.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 38,870,000.00 USD | 38,870,000.00 USD | 156,090.00 USD | 41,370.00 USD | 235,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,850,000.00 USD | 12,850,000.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 39,170,000.00 USD | 39,170,000.00 USD | 144,260.00 USD | 60,000.00 USD | 101,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,920,000.00 USD | 12,920,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 39,400,000.00 USD | 39,400,000.00 USD | 79,090.00 USD | 54,210.00 USD | 95,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,990,000.00 USD | 12,990,000.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 39,650,000.00 USD | 39,650,000.00 USD | 102,860.00 USD | 35,230.00 USD | 111,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 13,010,000.00 USD | 13,010,000.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 39,860,000.00 USD | 39,860,000.00 USD | 86,710.00 USD | 56,310.00 USD | 66,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 13,040,000.00 USD | 13,040,000.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 13,060,000.00 USD | 13,060,000.00 USD | 14,310.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 40,260,000.00 USD | 40,260,000.00 USD | 195,050.00 USD | 78,810.00 USD | 127,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 40,590,000.00 USD | 40,590,000.00 USD | 57,170.00 USD | 103,690.00 USD | 163,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 40,780,000.00 USD | 40,780,000.00 USD | 113,380.00 USD | 13,040.00 USD | 64,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 41,180,000.00 USD | 41,180,000.00 USD | 179,260.00 USD | 40,110.00 USD | 182,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 41,480,000.00 USD | 41,480,000.00 USD | 111,300.00 USD | 18,150.00 USD | 175,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 155.92 USD | 342,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 342,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 41,710,000.00 USD | 41,710,000.00 USD | 103,260.00 USD | 52,580.00 USD | 72,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 41,810,000.00 USD | 41,810,000.00 USD | 22,800.00 USD | 49,420.00 USD | 23,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 41,890,000.00 USD | 41,890,000.00 USD | 65,460.00 USD | 17,210.00 USD | 738.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 42,000,000.00 USD | 42,000,000.00 USD | 73,270.00 USD | 30,790.00 USD | 725.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 42,070,000.00 USD | 42,070,000.00 USD | 39,320.00 USD | 20,630.00 USD | 16,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 342,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 42,090,000.00 USD | 42,090,000.00 USD | 22,530.00 USD | 0.00 USD | 195.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 345,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 42,180,000.00 USD | 42,180,000.00 USD | 6,060.00 USD | 47,690.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 345,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 42,240,000.00 USD | 42,240,000.00 USD | 4,500.00 USD | 9,420.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.06` | 217.64 USD | 345,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.06` | 42,240,000.00 USD | 42,240,000.00 USD | 3,670.00 USD | 2,060.00 USD | 72.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 42,240,000.00 USD | 42,240,000.00 USD | 1,550.00 USD | 194.87 USD | 99.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 42,300,000.00 USD | 42,300,000.00 USD | 16,550.00 USD | 3,870.00 USD | 32,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 42,310,000.00 USD | 42,310,000.00 USD | 8,610.00 USD | 0.00 USD | 378.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 42,310,000.00 USD | 42,310,000.00 USD | 4,190.00 USD | 1,110.00 USD | 216.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 42,320,000.00 USD | 42,320,000.00 USD | 3,910.00 USD | 1,120.00 USD | 146.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 42,350,000.00 USD | 42,350,000.00 USD | 0.00 USD | 12,740.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,690.00 USD | 349,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 5,700.00 USD | 355,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 358,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 166.43 USD | 358,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 364,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 364,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 364,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 388,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 5,060.00 USD | 393,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 1,450.00 USD | 394,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 253.69 USD | 395,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.21` | 147.43 USD | 395,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 399,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.25` | 2,850.00 USD | 402,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 405,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 407,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 447,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 447,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 448,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,070.00 USD | 449,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 635.85 USD | 449,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 9,950.00 USD | 459,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 460,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 31,530.00 USD | 492,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 498,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 520,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 358.30 USD | 520,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,520.00 USD | 522,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 2,190.00 USD | 524,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 531,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 21,400.00 USD | 552,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 911,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 915,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 916,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 916,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 9,760.00 USD | 926,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 930,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 930,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 133.21 USD | 930,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 17,930.00 USD | 948,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 9,580.00 USD | 957,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 979,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 36,530.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,140.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 2,280.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 440.71 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 292,630.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 167.09 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 9,700.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 560.67 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1905` | 4,890,000.00 USD | 0.00 USD | 190.50 USD | `-78.41%` | `1,000.00` |
| `Live` | `Long` | `0.1985` | 4,890,000.00 USD | 0.00 USD | 193.08 USD | `-77.50%` | `972.70` |
| `Live` | `Long` | `0.1995` | 4,890,000.00 USD | 0.00 USD | 256.00 USD | `-77.39%` | `1,283.20` |
| `Live` | `Long` | `0.2055` | 4,890,000.00 USD | 0.00 USD | 439.89 USD | `-76.71%` | `2,140.60` |
| `Live` | `Long` | `0.2335` | 4,890,000.00 USD | 0.00 USD | 4,420.00 USD | `-73.54%` | `18,919.90` |
| `Live` | `Long` | `0.2355` | 4,880,000.00 USD | 0.00 USD | 789.66 USD | `-73.31%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,880,000.00 USD | 0.00 USD | 156.36 USD | `-72.97%` | `655.60` |
| `Live` | `Long` | `0.2405` | 4,880,000.00 USD | 0.00 USD | 1,620.00 USD | `-72.74%` | `6,725.00` |
| `Live` | `Long` | `0.2425` | 4,880,000.00 USD | 0.00 USD | 2,460.00 USD | `-72.52%` | `10,152.10` |
| `Live` | `Long` | `0.2525` | 4,880,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.38%` | `8,897.00` |
| `Live` | `Long` | `0.2605` | 4,880,000.00 USD | 0.00 USD | 169.17 USD | `-70.48%` | `649.40` |
| `Live` | `Long` | `0.2685` | 4,880,000.00 USD | 0.00 USD | 272.15 USD | `-69.57%` | `1,013.60` |
| `Live` | `Long` | `0.2705` | 4,880,000.00 USD | 0.00 USD | 161.52 USD | `-69.34%` | `597.10` |
| `Live` | `Long` | `0.2715` | 4,880,000.00 USD | 0.00 USD | 3,310.00 USD | `-69.23%` | `12,176.00` |
| `Live` | `Long` | `0.2735` | 4,870,000.00 USD | 0.00 USD | 248.34 USD | `-69.00%` | `908.00` |
| `Live` | `Long` | `0.2855` | 4,870,000.00 USD | 0.00 USD | 116.88 USD | `-67.64%` | `409.40` |
| `Live` | `Long` | `0.2875` | 4,870,000.00 USD | 0.00 USD | 24,760.00 USD | `-67.42%` | `86,117.40` |
| `Live` | `Long` | `0.2885` | 4,850,000.00 USD | 0.00 USD | 29,070.00 USD | `-67.30%` | `100,768.40` |
| `Live` | `Long` | `0.2945` | 4,820,000.00 USD | 0.00 USD | 687.92 USD | `-66.62%` | `2,335.90` |
| `Live` | `Long` | `0.2975` | 4,820,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.28%` | `14,561.30` |
| `Live` | `Long` | `0.3015` | 4,810,000.00 USD | 0.00 USD | 603.12 USD | `-65.83%` | `2,000.40` |
| `Live` | `Long` | `0.3085` | 4,810,000.00 USD | 0.00 USD | 102.08 USD | `-65.03%` | `330.90` |
| `Live` | `Long` | `0.3115` | 4,810,000.00 USD | 0.00 USD | 270.38 USD | `-64.69%` | `868.00` |
| `Live` | `Long` | `0.3205` | 4,810,000.00 USD | 0.00 USD | 581.03 USD | `-63.67%` | `1,812.90` |
| `Live` | `Long` | `0.3255` | 4,810,000.00 USD | 0.00 USD | 203.44 USD | `-63.11%` | `625.00` |
| `Live` | `Long` | `0.3385` | 4,810,000.00 USD | 0.00 USD | 3,390.00 USD | `-61.63%` | `10,000.00` |
| `Live` | `Long` | `0.3395` | 4,810,000.00 USD | 0.00 USD | 101.85 USD | `-61.52%` | `300.00` |
| `Live` | `Long` | `0.3505` | 4,810,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.27%` | `2,908.00` |
| `Live` | `Long` | `0.3585` | 4,810,000.00 USD | 0.00 USD | 595.72 USD | `-59.37%` | `1,661.70` |
| `Live` | `Long` | `0.3615` | 4,810,000.00 USD | 0.00 USD | 28,090.00 USD | `-59.03%` | `77,706.40` |
| `Live` | `Long` | `0.3655` | 4,780,000.00 USD | 0.00 USD | 407.57 USD | `-58.57%` | `1,115.10` |
| `Live` | `Long` | `0.3665` | 4,780,000.00 USD | 0.00 USD | 274.88 USD | `-58.46%` | `750.00` |
| `Live` | `Long` | `0.3675` | 4,780,000.00 USD | 0.00 USD | 4,070.00 USD | `-58.35%` | `11,077.80` |
| `Live` | `Long` | `0.3795` | 4,770,000.00 USD | 0.00 USD | 278.02 USD | `-56.99%` | `732.60` |
| `Live` | `Long` | `0.3815` | 4,770,000.00 USD | 0.00 USD | 6,490.00 USD | `-56.76%` | `17,000.00` |
| `Live` | `Long` | `0.3845` | 4,770,000.00 USD | 0.00 USD | 1,750.00 USD | `-56.42%` | `4,562.20` |
| `Live` | `Long` | `0.3895` | 4,770,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.85%` | `7,661.70` |
| `Live` | `Long` | `0.3905` | 4,760,000.00 USD | 0.00 USD | 27,340.00 USD | `-55.74%` | `70,000.00` |
| `Live` | `Long` | `0.3925` | 4,740,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.51%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,730,000.00 USD | 0.00 USD | 754.48 USD | `-55.29%` | `1,912.50` |
| `Live` | `Long` | `0.4035` | 4,730,000.00 USD | 0.00 USD | 935.03 USD | `-54.27%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,730,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.15%` | `13,640.50` |
| `Live` | `Long` | `0.4185` | 4,720,000.00 USD | 0.00 USD | 952.42 USD | `-52.57%` | `2,275.80` |
| `Live` | `Long` | `0.4235` | 4,720,000.00 USD | 0.00 USD | 10,610.00 USD | `-52.00%` | `25,042.20` |
| `Live` | `Long` | `0.4255` | 4,710,000.00 USD | 0.00 USD | 749.73 USD | `-51.77%` | `1,762.00` |
| `Live` | `Long` | `0.4285` | 4,710,000.00 USD | 0.00 USD | 299.95 USD | `-51.43%` | `700.00` |
| `Live` | `Long` | `0.4315` | 4,710,000.00 USD | 0.00 USD | 226.28 USD | `-51.09%` | `524.40` |
| `Live` | `Long` | `0.4385` | 4,710,000.00 USD | 0.00 USD | 5,600.00 USD | `-50.30%` | `12,780.30` |
| `Live` | `Long` | `0.4405` | 4,710,000.00 USD | 0.00 USD | 47,620.00 USD | `-50.07%` | `108,111.70` |
| `Live` | `Long` | `0.4415` | 4,660,000.00 USD | 0.00 USD | 5,800.00 USD | `-49.96%` | `13,146.20` |
| `Live` | `Long` | `0.4425` | 4,650,000.00 USD | 0.00 USD | 375.15 USD | `-49.85%` | `847.80` |
| `Live` | `Long` | `0.4435` | 4,650,000.00 USD | 0.00 USD | 26,830.00 USD | `-49.73%` | `60,493.80` |
| `Live` | `Long` | `0.4455` | 4,620,000.00 USD | 0.00 USD | 574.83 USD | `-49.51%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,620,000.00 USD | 0.00 USD | 19,600.00 USD | `-49.39%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,600,000.00 USD | 0.00 USD | 14,430.00 USD | `-49.28%` | `32,244.50` |
| `Live` | `Long` | `0.4535` | 4,590,000.00 USD | 0.00 USD | 702.74 USD | `-48.60%` | `1,549.60` |
| `Live` | `Long` | `0.4595` | 4,590,000.00 USD | 0.00 USD | 295.78 USD | `-47.92%` | `643.70` |
| `Live` | `Long` | `0.4645` | 4,590,000.00 USD | 0.00 USD | 2,110.00 USD | `-47.35%` | `4,538.10` |
| `Live` | `Long` | `0.4695` | 4,590,000.00 USD | 0.00 USD | 3,890.00 USD | `-46.79%` | `8,275.50` |
| `Live` | `Long` | `0.4715` | 4,580,000.00 USD | 0.00 USD | 1,720.00 USD | `-46.56%` | `3,650.40` |
| `Live` | `Long` | `0.4765` | 4,580,000.00 USD | 0.00 USD | 2,880.00 USD | `-45.99%` | `6,043.40` |
| `Live` | `Long` | `0.4785` | 4,580,000.00 USD | 0.00 USD | 110.10 USD | `-45.77%` | `230.10` |
| `Live` | `Long` | `0.4825` | 4,580,000.00 USD | 0.00 USD | 507.64 USD | `-45.31%` | `1,052.10` |
| `Live` | `Long` | `0.4835` | 4,580,000.00 USD | 0.00 USD | 174.01 USD | `-45.20%` | `359.90` |
| `Live` | `Long` | `0.4845` | 4,580,000.00 USD | 0.00 USD | 535.86 USD | `-45.09%` | `1,106.00` |
| `Live` | `Long` | `0.4865` | 4,580,000.00 USD | 0.00 USD | 5,690.00 USD | `-44.86%` | `11,703.60` |
| `Live` | `Long` | `0.4885` | 4,570,000.00 USD | 0.00 USD | 1,050.00 USD | `-44.63%` | `2,151.80` |
| `Live` | `Long` | `0.4895` | 4,570,000.00 USD | 0.00 USD | 105.34 USD | `-44.52%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,570,000.00 USD | 0.00 USD | 2,380.00 USD | `-44.29%` | `4,848.70` |
| `Live` | `Long` | `0.4925` | 4,570,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.18%` | `7,307.20` |
| `Live` | `Long` | `0.4945` | 4,560,000.00 USD | 0.00 USD | 365.24 USD | `-43.95%` | `738.60` |
| `Live` | `Long` | `0.4955` | 4,560,000.00 USD | 0.00 USD | 211.88 USD | `-43.84%` | `427.60` |
| `Live` | `Long` | `0.4985` | 4,560,000.00 USD | 0.00 USD | 216.75 USD | `-43.50%` | `434.80` |
| `Live` | `Long` | `0.5005` | 4,560,000.00 USD | 0.00 USD | 100.75 USD | `-43.27%` | `201.30` |
| `Live` | `Long` | `0.5015` | 4,560,000.00 USD | 0.00 USD | 212.49 USD | `-43.16%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,560,000.00 USD | 0.00 USD | 1,230.00 USD | `-43.05%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 4,560,000.00 USD | 0.00 USD | 716.75 USD | `-42.71%` | `1,417.90` |
| `Live` | `Long` | `0.5085` | 4,560,000.00 USD | 0.00 USD | 2,030.00 USD | `-42.37%` | `4,000.00` |
| `Live` | `Long` | `0.5095` | 4,560,000.00 USD | 0.00 USD | 195.75 USD | `-42.25%` | `384.20` |
| `Live` | `Long` | `0.5155` | 4,560,000.00 USD | 0.00 USD | 1,560.00 USD | `-41.57%` | `3,017.10` |
| `Live` | `Long` | `0.5165` | 4,560,000.00 USD | 0.00 USD | 619.80 USD | `-41.46%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,560,000.00 USD | 0.00 USD | 1,070.00 USD | `-41.35%` | `2,073.10` |
| `Live` | `Long` | `0.5185` | 4,560,000.00 USD | 0.00 USD | 121.74 USD | `-41.23%` | `234.80` |
| `Live` | `Long` | `0.5235` | 4,560,000.00 USD | 0.00 USD | 14,910.00 USD | `-40.67%` | `28,490.00` |
| `Live` | `Long` | `0.5245` | 4,540,000.00 USD | 0.00 USD | 5,280.00 USD | `-40.55%` | `10,075.20` |
| `Live` | `Long` | `0.5255` | 4,540,000.00 USD | 0.00 USD | 128.85 USD | `-40.44%` | `245.20` |
| `Live` | `Long` | `0.5275` | 4,540,000.00 USD | 0.00 USD | 348.36 USD | `-40.21%` | `660.40` |
| `Live` | `Long` | `0.5285` | 4,530,000.00 USD | 0.00 USD | 125,730.00 USD | `-40.10%` | `237,897.40` |
| `Live` | `Long` | `0.5295` | 4,410,000.00 USD | 0.00 USD | 264.06 USD | `-39.99%` | `498.70` |
| `Live` | `Long` | `0.5325` | 4,410,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.65%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,410,000.00 USD | 0.00 USD | 417.12 USD | `-39.42%` | `780.40` |
| `Live` | `Long` | `0.5395` | 4,410,000.00 USD | 0.00 USD | 8,200.00 USD | `-38.85%` | `15,197.00` |
| `Live` | `Long` | `0.5405` | 4,400,000.00 USD | 0.00 USD | 9,620.00 USD | `-38.74%` | `17,801.90` |
| `Live` | `Long` | `0.5425` | 4,390,000.00 USD | 0.00 USD | 269.13 USD | `-38.51%` | `496.10` |
| `Live` | `Long` | `0.5435` | 4,390,000.00 USD | 0.00 USD | 5,900.00 USD | `-38.40%` | `10,862.70` |
| `Live` | `Long` | `0.5445` | 4,380,000.00 USD | 0.00 USD | 230.32 USD | `-38.29%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,380,000.00 USD | 0.00 USD | 272.87 USD | `-38.06%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,380,000.00 USD | 0.00 USD | 1,780.00 USD | `-37.95%` | `3,257.90` |
| `Live` | `Long` | `0.5495` | 4,380,000.00 USD | 0.00 USD | 28,790.00 USD | `-37.72%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,350,000.00 USD | 0.00 USD | 413.21 USD | `-37.61%` | `750.60` |
| `Live` | `Long` | `0.5515` | 4,350,000.00 USD | 0.00 USD | 160.93 USD | `-37.49%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,350,000.00 USD | 0.00 USD | 582.56 USD | `-37.38%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,350,000.00 USD | 0.00 USD | 271.88 USD | `-37.27%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,350,000.00 USD | 0.00 USD | 531.60 USD | `-37.15%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,350,000.00 USD | 0.00 USD | 7,950.00 USD | `-37.04%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,340,000.00 USD | 0.00 USD | 141.97 USD | `-36.70%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,340,000.00 USD | 0.00 USD | 304.93 USD | `-36.59%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,340,000.00 USD | 0.00 USD | 441.84 USD | `-36.47%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,340,000.00 USD | 0.00 USD | 330.53 USD | `-36.25%` | `587.60` |
| `Live` | `Long` | `0.5635` | 4,340,000.00 USD | 0.00 USD | 195.93 USD | `-36.13%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,340,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.91%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,330,000.00 USD | 0.00 USD | 570.01 USD | `-35.79%` | `1,006.20` |
| `Live` | `Long` | `0.5675` | 4,330,000.00 USD | 0.00 USD | 18,580.00 USD | `-35.68%` | `32,747.00` |
| `Live` | `Long` | `0.5685` | 4,310,000.00 USD | 0.00 USD | 4,540.00 USD | `-35.57%` | `7,985.90` |
| `Live` | `Long` | `0.5695` | 4,310,000.00 USD | 0.00 USD | 973.22 USD | `-35.45%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,310,000.00 USD | 0.00 USD | 139.23 USD | `-35.11%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,310,000.00 USD | 0.00 USD | 182.72 USD | `-35.00%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,310,000.00 USD | 0.00 USD | 144.03 USD | `-34.89%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,310,000.00 USD | 0.00 USD | 1,010.00 USD | `-34.77%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,310,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.66%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,300,000.00 USD | 0.00 USD | 497.75 USD | `-34.55%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,300,000.00 USD | 0.00 USD | 119.34 USD | `-34.43%` | `206.30` |
| `Live` | `Long` | `0.5795` | 4,300,000.00 USD | 0.00 USD | 212.85 USD | `-34.32%` | `367.30` |
| `Live` | `Long` | `0.5805` | 4,300,000.00 USD | 0.00 USD | 1,760.00 USD | `-34.21%` | `3,027.80` |
| `Live` | `Long` | `0.5825` | 4,300,000.00 USD | 0.00 USD | 6,470.00 USD | `-33.98%` | `11,099.00` |
| `Live` | `Long` | `0.5855` | 4,290,000.00 USD | 0.00 USD | 2,640.00 USD | `-33.64%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,290,000.00 USD | 0.00 USD | 466.85 USD | `-33.53%` | `796.00` |
| `Live` | `Long` | `0.5875` | 4,290,000.00 USD | 0.00 USD | 969.32 USD | `-33.41%` | `1,649.90` |
| `Live` | `Long` | `0.5885` | 4,290,000.00 USD | 0.00 USD | 311.14 USD | `-33.30%` | `528.70` |
| `Live` | `Long` | `0.5925` | 4,290,000.00 USD | 0.00 USD | 994.16 USD | `-32.85%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,290,000.00 USD | 0.00 USD | 132.41 USD | `-32.73%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,290,000.00 USD | 0.00 USD | 8,220.00 USD | `-32.62%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 4,280,000.00 USD | 0.00 USD | 608.61 USD | `-32.39%` | `1,020.30` |
| `Live` | `Long` | `0.5995` | 4,280,000.00 USD | 0.00 USD | 694.58 USD | `-32.05%` | `1,158.60` |
| `Live` | `Long` | `0.6005` | 4,280,000.00 USD | 0.00 USD | 19,000.00 USD | `-31.94%` | `31,633.50` |
| `Live` | `Long` | `0.6015` | 4,260,000.00 USD | 0.00 USD | 323.79 USD | `-31.83%` | `538.30` |
| `Live` | `Long` | `0.6025` | 4,260,000.00 USD | 0.00 USD | 432.35 USD | `-31.71%` | `717.60` |
| `Live` | `Long` | `0.6075` | 4,260,000.00 USD | 0.00 USD | 851.05 USD | `-31.15%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,260,000.00 USD | 0.00 USD | 272.24 USD | `-31.03%` | `447.40` |
| `Live` | `Long` | `0.6105` | 4,260,000.00 USD | 0.00 USD | 663.43 USD | `-30.81%` | `1,086.70` |
| `Live` | `Long` | `0.6115` | 4,260,000.00 USD | 0.00 USD | 16,020.00 USD | `-30.69%` | `26,196.40` |
| `Live` | `Long` | `0.6125` | 4,240,000.00 USD | 0.00 USD | 213.64 USD | `-30.58%` | `348.80` |
| `Live` | `Long` | `0.6135` | 4,240,000.00 USD | 0.00 USD | 357.73 USD | `-30.47%` | `583.10` |
| `Live` | `Long` | `0.6145` | 4,240,000.00 USD | 0.00 USD | 3,600.00 USD | `-30.35%` | `5,859.40` |
| `Live` | `Long` | `0.6155` | 4,240,000.00 USD | 0.00 USD | 18,790.00 USD | `-30.24%` | `30,534.50` |
| `Live` | `Long` | `0.6165` | 4,220,000.00 USD | 0.00 USD | 29,900.00 USD | `-30.13%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 4,190,000.00 USD | 0.00 USD | 4,170.00 USD | `-30.01%` | `6,760.50` |
| `Live` | `Long` | `0.6185` | 4,190,000.00 USD | 0.00 USD | 13,910.00 USD | `-29.90%` | `22,495.30` |
| `Live` | `Long` | `0.6195` | 4,170,000.00 USD | 0.00 USD | 1,050.00 USD | `-29.79%` | `1,700.60` |
| `Live` | `Long` | `0.6215` | 4,170,000.00 USD | 0.00 USD | 19,270.00 USD | `-29.56%` | `31,006.80` |
| `Live` | `Long` | `0.6245` | 4,150,000.00 USD | 0.00 USD | 619.32 USD | `-29.22%` | `991.70` |
| `Live` | `Long` | `0.6255` | 4,150,000.00 USD | 0.00 USD | 32,070.00 USD | `-29.11%` | `51,265.70` |
| `Live` | `Long` | `0.6285` | 4,120,000.00 USD | 0.00 USD | 102.45 USD | `-28.77%` | `163.00` |
| `Live` | `Long` | `0.6305` | 4,120,000.00 USD | 0.00 USD | 319.35 USD | `-28.54%` | `506.50` |
| `Live` | `Long` | `0.6315` | 4,120,000.00 USD | 0.00 USD | 3,510.00 USD | `-28.43%` | `5,564.80` |
| `Live` | `Long` | `0.6345` | 4,110,000.00 USD | 0.00 USD | 843.00 USD | `-28.09%` | `1,328.60` |
| `Live` | `Long` | `0.6365` | 4,110,000.00 USD | 0.00 USD | 3,060.00 USD | `-27.86%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 4,110,000.00 USD | 0.00 USD | 130.62 USD | `-27.75%` | `204.90` |
| `Live` | `Long` | `0.6385` | 4,110,000.00 USD | 0.00 USD | 309.35 USD | `-27.63%` | `484.50` |
| `Live` | `Long` | `0.6395` | 4,110,000.00 USD | 0.00 USD | 321,670.00 USD | `-27.52%` | `503,000.00` |
| `Live` | `Long` | `0.6405` | 3,790,000.00 USD | 0.00 USD | 939.17 USD | `-27.41%` | `1,466.30` |
| `Live` | `Long` | `0.6415` | 3,790,000.00 USD | 0.00 USD | 86,920.00 USD | `-27.29%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,700,000.00 USD | 0.00 USD | 1,260.00 USD | `-27.18%` | `1,956.60` |
| `Live` | `Long` | `0.6435` | 3,700,000.00 USD | 0.00 USD | 657.79 USD | `-27.07%` | `1,022.20` |
| `Live` | `Long` | `0.6445` | 3,700,000.00 USD | 0.00 USD | 65,790.00 USD | `-26.95%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,630,000.00 USD | 0.00 USD | 14,590.00 USD | `-26.84%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,620,000.00 USD | 0.00 USD | 146.76 USD | `-26.73%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,620,000.00 USD | 0.00 USD | 3,910.00 USD | `-26.61%` | `6,031.70` |
| `Live` | `Long` | `0.6485` | 3,610,000.00 USD | 0.00 USD | 668.34 USD | `-26.50%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,610,000.00 USD | 0.00 USD | 721.59 USD | `-26.39%` | `1,111.00` |
| `Live` | `Long` | `0.6505` | 3,610,000.00 USD | 0.00 USD | 1,820.00 USD | `-26.27%` | `2,797.20` |
| `Live` | `Long` | `0.6515` | 3,610,000.00 USD | 0.00 USD | 403,320.00 USD | `-26.16%` | `619,065.10` |
| `Live` | `Long` | `0.6535` | 3,210,000.00 USD | 0.00 USD | 126,530.00 USD | `-25.93%` | `193,618.10` |
| `Live` | `Long` | `0.6545` | 3,080,000.00 USD | 0.00 USD | 509.46 USD | `-25.82%` | `778.40` |
| `Live` | `Long` | `0.6555` | 3,080,000.00 USD | 0.00 USD | 676.54 USD | `-25.71%` | `1,032.10` |
| `Live` | `Long` | `0.6565` | 3,080,000.00 USD | 0.00 USD | 8,220.00 USD | `-25.59%` | `12,525.80` |
| `Live` | `Long` | `0.6575` | 3,070,000.00 USD | 0.00 USD | 13,280.00 USD | `-25.48%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 3,060,000.00 USD | 0.00 USD | 2,970.00 USD | `-25.37%` | `4,508.30` |
| `Live` | `Long` | `0.6615` | 3,060,000.00 USD | 0.00 USD | 10,820.00 USD | `-25.03%` | `16,357.90` |
| `Live` | `Long` | `0.6625` | 3,040,000.00 USD | 0.00 USD | 788.97 USD | `-24.91%` | `1,190.90` |
| `Live` | `Long` | `0.6635` | 3,040,000.00 USD | 0.00 USD | 2,160.00 USD | `-24.80%` | `3,259.80` |
| `Live` | `Long` | `0.6645` | 3,040,000.00 USD | 0.00 USD | 448.54 USD | `-24.69%` | `675.00` |
| `Live` | `Long` | `0.6665` | 3,040,000.00 USD | 0.00 USD | 186.02 USD | `-24.46%` | `279.10` |
| `Live` | `Long` | `0.6675` | 3,040,000.00 USD | 0.00 USD | 6,810.00 USD | `-24.35%` | `10,207.60` |
| `Live` | `Long` | `0.6685` | 3,030,000.00 USD | 0.00 USD | 2,810.00 USD | `-24.23%` | `4,203.00` |
| `Live` | `Long` | `0.6705` | 3,030,000.00 USD | 0.00 USD | 2,290.00 USD | `-24.01%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 3,030,000.00 USD | 0.00 USD | 8,500.00 USD | `-23.89%` | `12,661.20` |
| `Live` | `Long` | `0.6725` | 3,020,000.00 USD | 0.00 USD | 29,400.00 USD | `-23.78%` | `43,720.20` |
| `Live` | `Long` | `0.6735` | 2,990,000.00 USD | 0.00 USD | 633.09 USD | `-23.67%` | `940.00` |
| `Live` | `Long` | `0.6745` | 2,990,000.00 USD | 0.00 USD | 6,520.00 USD | `-23.55%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 2,980,000.00 USD | 0.00 USD | 111.59 USD | `-23.44%` | `165.20` |
| `Live` | `Long` | `0.6775` | 2,980,000.00 USD | 0.00 USD | 6,780.00 USD | `-23.21%` | `10,000.00` |
| `Live` | `Long` | `0.6785` | 2,980,000.00 USD | 0.00 USD | 250.77 USD | `-23.10%` | `369.60` |
| `Live` | `Long` | `0.6795` | 2,980,000.00 USD | 0.00 USD | 45,130.00 USD | `-22.99%` | `66,410.20` |
| `Live` | `Long` | `0.6805` | 2,930,000.00 USD | 0.00 USD | 1,600.00 USD | `-22.87%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 2,930,000.00 USD | 0.00 USD | 3,550.00 USD | `-22.76%` | `5,210.50` |
| `Live` | `Long` | `0.6825` | 2,930,000.00 USD | 0.00 USD | 135,750.00 USD | `-22.65%` | `198,898.80` |
| `Live` | `Long` | `0.6835` | 2,790,000.00 USD | 0.00 USD | 11,170.00 USD | `-22.53%` | `16,336.60` |
| `Live` | `Long` | `0.6845` | 2,780,000.00 USD | 0.00 USD | 5,790.00 USD | `-22.42%` | `8,455.80` |
| `Live` | `Long` | `0.6865` | 2,770,000.00 USD | 0.00 USD | 112.59 USD | `-22.19%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,770,000.00 USD | 0.00 USD | 480.49 USD | `-22.08%` | `698.90` |
| `Live` | `Long` | `0.6885` | 2,770,000.00 USD | 0.00 USD | 83,790.00 USD | `-21.97%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 2,690,000.00 USD | 0.00 USD | 2,230.00 USD | `-21.85%` | `3,232.30` |
| `Live` | `Long` | `0.6905` | 2,690,000.00 USD | 0.00 USD | 3,360.00 USD | `-21.74%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,680,000.00 USD | 0.00 USD | 8,970.00 USD | `-21.63%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 2,680,000.00 USD | 0.00 USD | 2,980.00 USD | `-21.40%` | `4,299.80` |
| `Live` | `Long` | `0.6945` | 2,670,000.00 USD | 0.00 USD | 722.28 USD | `-21.29%` | `1,040.00` |
| `Live` | `Long` | `0.6965` | 2,670,000.00 USD | 0.00 USD | 1,150.00 USD | `-21.06%` | `1,650.00` |
| `Live` | `Long` | `0.6975` | 2,670,000.00 USD | 0.00 USD | 2,400.00 USD | `-20.95%` | `3,440.40` |
| `Live` | `Long` | `0.6985` | 2,670,000.00 USD | 0.00 USD | 1,930.00 USD | `-20.83%` | `2,759.10` |
| `Live` | `Long` | `0.7015` | 2,670,000.00 USD | 0.00 USD | 1,990.00 USD | `-20.49%` | `2,841.50` |
| `Live` | `Long` | `0.7045` | 2,660,000.00 USD | 0.00 USD | 759.59 USD | `-20.15%` | `1,078.20` |
| `Live` | `Long` | `0.7065` | 2,660,000.00 USD | 0.00 USD | 769.59 USD | `-19.93%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 2,660,000.00 USD | 0.00 USD | 787.73 USD | `-19.81%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 2,660,000.00 USD | 0.00 USD | 2,020.00 USD | `-19.70%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,660,000.00 USD | 0.00 USD | 2,720.00 USD | `-19.59%` | `3,833.70` |
| `Live` | `Long` | `0.7105` | 2,660,000.00 USD | 0.00 USD | 3,530.00 USD | `-19.47%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 2,650,000.00 USD | 0.00 USD | 569.20 USD | `-19.36%` | `800.00` |
| `Live` | `Long` | `0.7125` | 2,650,000.00 USD | 0.00 USD | 272.53 USD | `-19.25%` | `382.50` |
| `Live` | `Long` | `0.7135` | 2,650,000.00 USD | 0.00 USD | 3,530.00 USD | `-19.13%` | `4,949.90` |
| `Live` | `Long` | `0.7175` | 2,650,000.00 USD | 0.00 USD | 9,190.00 USD | `-18.68%` | `12,805.60` |
| `Live` | `Long` | `0.7195` | 2,640,000.00 USD | 0.00 USD | 11,250.00 USD | `-18.45%` | `15,634.40` |
| `Live` | `Long` | `0.7225` | 2,630,000.00 USD | 0.00 USD | 129.26 USD | `-18.11%` | `178.90` |
| `Live` | `Long` | `0.7255` | 2,630,000.00 USD | 0.00 USD | 2,660.00 USD | `-17.77%` | `3,662.80` |
| `Live` | `Long` | `0.7265` | 2,630,000.00 USD | 0.00 USD | 1,180.00 USD | `-17.66%` | `1,619.70` |
| `Live` | `Long` | `0.7275` | 2,620,000.00 USD | 0.00 USD | 762.57 USD | `-17.55%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 2,620,000.00 USD | 0.00 USD | 214.03 USD | `-17.43%` | `293.80` |
| `Live` | `Long` | `0.7295` | 2,620,000.00 USD | 0.00 USD | 26,490.00 USD | `-17.32%` | `36,317.70` |
| `Live` | `Long` | `0.7305` | 2,600,000.00 USD | 0.00 USD | 119.88 USD | `-17.21%` | `164.10` |
| `Live` | `Long` | `0.7325` | 2,600,000.00 USD | 0.00 USD | 1,030.00 USD | `-16.98%` | `1,409.90` |
| `Live` | `Long` | `0.7335` | 2,600,000.00 USD | 0.00 USD | 724.11 USD | `-16.87%` | `987.20` |
| `Live` | `Long` | `0.7345` | 2,600,000.00 USD | 0.00 USD | 2,340.00 USD | `-16.75%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,590,000.00 USD | 0.00 USD | 51,920.00 USD | `-16.64%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 2,540,000.00 USD | 0.00 USD | 533.01 USD | `-16.53%` | `723.70` |
| `Live` | `Long` | `0.7375` | 2,540,000.00 USD | 0.00 USD | 14,950.00 USD | `-16.41%` | `20,275.40` |
| `Live` | `Long` | `0.7385` | 2,530,000.00 USD | 0.00 USD | 5,810.00 USD | `-16.30%` | `7,871.10` |
| `Live` | `Long` | `0.7395` | 2,520,000.00 USD | 0.00 USD | 1,260.00 USD | `-16.19%` | `1,705.90` |
| `Live` | `Long` | `0.7405` | 2,520,000.00 USD | 0.00 USD | 6,330.00 USD | `-16.07%` | `8,542.50` |
| `Live` | `Long` | `0.7415` | 2,510,000.00 USD | 0.00 USD | 382.61 USD | `-15.96%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,510,000.00 USD | 0.00 USD | 784,090.00 USD | `-15.85%` | `1,056,015.30` |
| `Live` | `Long` | `0.7435` | 1,730,000.00 USD | 0.00 USD | 421.12 USD | `-15.73%` | `566.40` |
| `Live` | `Long` | `0.7445` | 1,730,000.00 USD | 0.00 USD | 105.64 USD | `-15.62%` | `141.90` |
| `Live` | `Long` | `0.7455` | 1,730,000.00 USD | 0.00 USD | 2,160.00 USD | `-15.51%` | `2,892.60` |
| `Live` | `Long` | `0.7475` | 1,720,000.00 USD | 0.00 USD | 103,410.00 USD | `-15.28%` | `138,338.20` |
| `Live` | `Long` | `0.7485` | 1,620,000.00 USD | 0.00 USD | 105.91 USD | `-15.17%` | `141.50` |
| `Live` | `Long` | `0.7495` | 1,620,000.00 USD | 0.00 USD | 599.60 USD | `-15.05%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,620,000.00 USD | 0.00 USD | 1,210.00 USD | `-14.83%` | `1,613.50` |
| `Live` | `Long` | `0.7525` | 1,620,000.00 USD | 0.00 USD | 106.03 USD | `-14.71%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,620,000.00 USD | 0.00 USD | 264.86 USD | `-14.60%` | `351.50` |
| `Live` | `Long` | `0.7545` | 1,620,000.00 USD | 0.00 USD | 2,190.00 USD | `-14.49%` | `2,897.60` |
| `Live` | `Long` | `0.7555` | 1,620,000.00 USD | 0.00 USD | 440.08 USD | `-14.37%` | `582.50` |
| `Live` | `Long` | `0.7565` | 1,620,000.00 USD | 0.00 USD | 438.54 USD | `-14.26%` | `579.70` |
| `Live` | `Long` | `0.7575` | 1,620,000.00 USD | 0.00 USD | 1,900.00 USD | `-14.15%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,610,000.00 USD | 0.00 USD | 36,710.00 USD | `-14.03%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,580,000.00 USD | 0.00 USD | 4,390.00 USD | `-13.92%` | `5,776.10` |
| `Live` | `Long` | `0.7615` | 1,570,000.00 USD | 0.00 USD | 351.43 USD | `-13.69%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,570,000.00 USD | 0.00 USD | 859.11 USD | `-13.58%` | `1,126.70` |
| `Live` | `Long` | `0.7635` | 1,570,000.00 USD | 0.00 USD | 320,810.00 USD | `-13.47%` | `420,185.20` |
| `Live` | `Long` | `0.7645` | 1,250,000.00 USD | 0.00 USD | 3,510.00 USD | `-13.35%` | `4,596.60` |
| `Live` | `Long` | `0.7655` | 1,250,000.00 USD | 0.00 USD | 4,430.00 USD | `-13.24%` | `5,788.60` |
| `Live` | `Long` | `0.7665` | 1,240,000.00 USD | 0.00 USD | 1,420.00 USD | `-13.13%` | `1,847.90` |
| `Live` | `Long` | `0.7675` | 1,240,000.00 USD | 0.00 USD | 10,200.00 USD | `-13.01%` | `13,292.20` |
| `Live` | `Long` | `0.7685` | 1,230,000.00 USD | 0.00 USD | 499.99 USD | `-12.90%` | `650.60` |
| `Live` | `Long` | `0.7695` | 1,230,000.00 USD | 0.00 USD | 153,870.00 USD | `-12.79%` | `199,959.50` |
| `Live` | `Long` | `0.7705` | 1,080,000.00 USD | 0.00 USD | 4,350.00 USD | `-12.67%` | `5,644.90` |
| `Live` | `Long` | `0.7715` | 1,070,000.00 USD | 0.00 USD | 338.38 USD | `-12.56%` | `438.60` |
| `Live` | `Long` | `0.7725` | 1,070,000.00 USD | 0.00 USD | 2,950.00 USD | `-12.45%` | `3,816.80` |
| `Live` | `Long` | `0.7735` | 1,070,000.00 USD | 0.00 USD | 4,570.00 USD | `-12.33%` | `5,912.10` |
| `Live` | `Long` | `0.7755` | 1,060,000.00 USD | 0.00 USD | 4,130.00 USD | `-12.11%` | `5,321.70` |
| `Live` | `Long` | `0.7765` | 1,060,000.00 USD | 0.00 USD | 21,370.00 USD | `-11.99%` | `27,514.60` |
| `Live` | `Long` | `0.7785` | 1,040,000.00 USD | 0.00 USD | 6,450.00 USD | `-11.77%` | `8,285.30` |
| `Live` | `Long` | `0.7795` | 1,030,000.00 USD | 0.00 USD | 28,280.00 USD | `-11.65%` | `36,277.00` |
| `Live` | `Long` | `0.7815` | 1,000,000.00 USD | 0.00 USD | 13,880.00 USD | `-11.43%` | `17,766.50` |
| `Live` | `Long` | `0.7825` | 990,880.00 USD | 0.00 USD | 15,670.00 USD | `-11.31%` | `20,031.40` |
| `Live` | `Long` | `0.7835` | 975,210.00 USD | 0.00 USD | 1,720.00 USD | `-11.20%` | `2,199.80` |
| `Live` | `Long` | `0.7855` | 973,490.00 USD | 0.00 USD | 3,020.00 USD | `-10.97%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 970,470.00 USD | 0.00 USD | 2,870.00 USD | `-10.86%` | `3,651.90` |
| `Live` | `Long` | `0.7875` | 967,600.00 USD | 0.00 USD | 5,970.00 USD | `-10.75%` | `7,581.70` |
| `Live` | `Long` | `0.7895` | 961,630.00 USD | 0.00 USD | 2,530.00 USD | `-10.52%` | `3,204.80` |
| `Live` | `Long` | `0.7905` | 959,100.00 USD | 0.00 USD | 3,870.00 USD | `-10.41%` | `4,891.30` |
| `Live` | `Long` | `0.7915` | 955,230.00 USD | 0.00 USD | 5,470.00 USD | `-10.29%` | `6,905.90` |
| `Live` | `Long` | `0.7925` | 949,760.00 USD | 0.00 USD | 3,930.00 USD | `-10.18%` | `4,953.00` |
| `Live` | `Long` | `0.7945` | 945,840.00 USD | 0.00 USD | 7,640.00 USD | `-9.95%` | `9,619.00` |
| `Live` | `Long` | `0.7955` | 938,200.00 USD | 0.00 USD | 23,610.00 USD | `-9.84%` | `29,676.80` |
| `Live` | `Long` | `0.7975` | 914,590.00 USD | 0.00 USD | 1,170.00 USD | `-9.61%` | `1,464.30` |
| `Live` | `Long` | `0.7995` | 913,420.00 USD | 0.00 USD | 2,580.00 USD | `-9.39%` | `3,228.10` |
| `Live` | `Long` | `0.8005` | 910,840.00 USD | 0.00 USD | 635.04 USD | `-9.27%` | `793.30` |
| `Live` | `Long` | `0.8015` | 910,210.00 USD | 0.00 USD | 7,130.00 USD | `-9.16%` | `8,893.40` |
| `Live` | `Long` | `0.8035` | 903,080.00 USD | 0.00 USD | 79,510.00 USD | `-8.93%` | `98,951.90` |
| `Live` | `Long` | `0.8045` | 823,570.00 USD | 0.00 USD | 34,400.00 USD | `-8.82%` | `42,764.80` |
| `Live` | `Long` | `0.8055` | 789,170.00 USD | 0.00 USD | 266.62 USD | `-8.71%` | `331.00` |
| `Live` | `Long` | `0.8075` | 788,900.00 USD | 0.00 USD | 2,760.00 USD | `-8.48%` | `3,414.30` |
| `Live` | `Long` | `0.8085` | 786,140.00 USD | 0.00 USD | 22,170.00 USD | `-8.37%` | `27,427.20` |
| `Live` | `Long` | `0.8095` | 763,970.00 USD | 0.00 USD | 2,210.00 USD | `-8.25%` | `2,728.60` |
| `Live` | `Long` | `0.8105` | 761,760.00 USD | 0.00 USD | 2,250.00 USD | `-8.14%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 759,510.00 USD | 0.00 USD | 1,390.00 USD | `-8.03%` | `1,716.00` |
| `Live` | `Long` | `0.8125` | 758,110.00 USD | 0.00 USD | 54,950.00 USD | `-7.91%` | `67,633.70` |
| `Live` | `Long` | `0.8135` | 703,160.00 USD | 0.00 USD | 8,130.00 USD | `-7.80%` | `9,989.60` |
| `Live` | `Long` | `0.8145` | 695,030.00 USD | 0.00 USD | 2,200.00 USD | `-7.69%` | `2,702.90` |
| `Live` | `Long` | `0.8155` | 692,830.00 USD | 0.00 USD | 24,220.00 USD | `-7.57%` | `29,705.40` |
| `Live` | `Long` | `0.8165` | 668,610.00 USD | 0.00 USD | 104.92 USD | `-7.46%` | `128.50` |
| `Live` | `Long` | `0.8175` | 668,500.00 USD | 0.00 USD | 103,450.00 USD | `-7.35%` | `126,546.30` |
| `Live` | `Long` | `0.8185` | 565,050.00 USD | 0.00 USD | 2,230.00 USD | `-7.23%` | `2,719.90` |
| `Live` | `Long` | `0.8195` | 562,820.00 USD | 0.00 USD | 2,830.00 USD | `-7.12%` | `3,459.10` |
| `Live` | `Long` | `0.8205` | 559,990.00 USD | 0.00 USD | 2,280.00 USD | `-7.01%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 557,710.00 USD | 0.00 USD | 6,650.00 USD | `-6.89%` | `8,091.40` |
| `Live` | `Long` | `0.8225` | 551,060.00 USD | 0.00 USD | 466.85 USD | `-6.78%` | `567.60` |
| `Live` | `Long` | `0.8235` | 550,590.00 USD | 0.00 USD | 45,230.00 USD | `-6.67%` | `54,928.20` |
| `Live` | `Long` | `0.8245` | 505,360.00 USD | 0.00 USD | 17,700.00 USD | `-6.55%` | `21,461.90` |
| `Live` | `Long` | `0.8255` | 487,660.00 USD | 0.00 USD | 5,300.00 USD | `-6.44%` | `6,425.70` |
| `Live` | `Long` | `0.8275` | 482,360.00 USD | 0.00 USD | 16,090.00 USD | `-6.21%` | `19,449.30` |
| `Live` | `Long` | `0.8285` | 466,270.00 USD | 0.00 USD | 137,340.00 USD | `-6.10%` | `165,769.50` |
| `Live` | `Long` | `0.8295` | 328,930.00 USD | 0.00 USD | 24,330.00 USD | `-5.99%` | `29,330.40` |
| `Live` | `Long` | `0.8305` | 304,600.00 USD | 0.00 USD | 2,460.00 USD | `-5.87%` | `2,959.90` |
| `Live` | `Long` | `0.8315` | 302,140.00 USD | 0.00 USD | 3,340.00 USD | `-5.76%` | `4,013.70` |
| `Live` | `Long` | `0.8325` | 298,800.00 USD | 0.00 USD | 12,370.00 USD | `-5.65%` | `14,857.80` |
| `Live` | `Long` | `0.8335` | 286,430.00 USD | 0.00 USD | 5,100.00 USD | `-5.53%` | `6,122.50` |
| `Live` | `Long` | `0.8345` | 281,330.00 USD | 0.00 USD | 11,360.00 USD | `-5.42%` | `13,614.50` |
| `Live` | `Long` | `0.8355` | 269,970.00 USD | 0.00 USD | 2,890.00 USD | `-5.31%` | `3,459.70` |
| `Live` | `Long` | `0.8365` | 267,080.00 USD | 0.00 USD | 57,620.00 USD | `-5.19%` | `68,888.00` |
| `Live` | `Long` | `0.8375` | 209,450.00 USD | 0.00 USD | 2,190.00 USD | `-5.08%` | `2,620.20` |
| `Live` | `Long` | `0.8385` | 207,260.00 USD | 0.00 USD | 77,770.00 USD | `-4.97%` | `92,754.10` |
| `Live` | `Long` | `0.8395` | 129,480.00 USD | 0.00 USD | 26,310.00 USD | `-4.85%` | `31,342.50` |
| `Live` | `Long` | `0.8405` | 103,170.00 USD | 0.00 USD | 692.74 USD | `-4.74%` | `824.20` |
| `Live` | `Long` | `0.8415` | 102,480.00 USD | 0.00 USD | 4,730.00 USD | `-4.63%` | `5,616.80` |
| `Live` | `Long` | `0.8425` | 97,750.00 USD | 0.00 USD | 2,340.00 USD | `-4.51%` | `2,780.00` |
| `Live` | `Long` | `0.8435` | 95,410.00 USD | 0.00 USD | 3,340.00 USD | `-4.40%` | `3,954.20` |
| `Live` | `Long` | `0.8445` | 92,070.00 USD | 0.00 USD | 598.67 USD | `-4.29%` | `708.90` |
| `Live` | `Long` | `0.8455` | 91,480.00 USD | 0.00 USD | 15,800.00 USD | `-4.17%` | `18,690.40` |
| `Live` | `Long` | `0.8465` | 75,670.00 USD | 0.00 USD | 15,120.00 USD | `-4.06%` | `17,865.30` |
| `Live` | `Long` | `0.8475` | 60,550.00 USD | 0.00 USD | 10,800.00 USD | `-3.95%` | `12,740.30` |
| `Live` | `Long` | `0.8485` | 49,750.00 USD | 0.00 USD | 1,380.00 USD | `-3.83%` | `1,631.60` |
| `Live` | `Long` | `0.8495` | 48,370.00 USD | 0.00 USD | 804.99 USD | `-3.72%` | `947.60` |
| `Live` | `Long` | `0.8505` | 47,560.00 USD | 0.00 USD | 9,470.00 USD | `-3.61%` | `11,139.20` |
| `Live` | `Long` | `0.8515` | 38,090.00 USD | 0.00 USD | 1,220.00 USD | `-3.49%` | `1,433.90` |
| `Live` | `Long` | `0.8525` | 36,870.00 USD | 0.00 USD | 1,260.00 USD | `-3.38%` | `1,476.60` |
| `Live` | `Long` | `0.8535` | 35,610.00 USD | 0.00 USD | 15,640.00 USD | `-3.27%` | `18,326.40` |
| `Live` | `Long` | `0.8545` | 19,970.00 USD | 0.00 USD | 784.69 USD | `-3.15%` | `918.30` |
| `Live` | `Long` | `0.8555` | 19,180.00 USD | 0.00 USD | 17,220.00 USD | `-3.04%` | `20,123.80` |
| `Live` | `Long` | `0.8585` | 1,970.00 USD | 0.00 USD | 1,170.00 USD | `-2.70%` | `1,367.50` |
| `Live` | `Long` | `0.8595` | 793.58 USD | 0.00 USD | 793.58 USD | `-2.59%` | `923.30` |
| `Live` | `Short` | `0.9175` | 3,550.00 USD | 3,550.00 USD | 0.00 USD | `+3.99%` | `3,866.20` |
| `Live` | `Short` | `0.9255` | 9,410.00 USD | 5,860.00 USD | 0.00 USD | `+4.90%` | `6,333.20` |
| `Live` | `Short` | `0.9305` | 11,250.00 USD | 1,840.00 USD | 0.00 USD | `+5.46%` | `1,980.30` |
| `Live` | `Short` | `0.9315` | 11,650.00 USD | 397.84 USD | 0.00 USD | `+5.58%` | `427.10` |
| `Live` | `Short` | `0.9325` | 12,550.00 USD | 900.70 USD | 0.00 USD | `+5.69%` | `965.90` |
| `Live` | `Short` | `0.9335` | 13,570.00 USD | 1,020.00 USD | 0.00 USD | `+5.80%` | `1,093.90` |
| `Live` | `Short` | `0.9345` | 13,690.00 USD | 115.04 USD | 0.00 USD | `+5.92%` | `123.10` |
| `Live` | `Short` | `0.9385` | 17,350.00 USD | 3,670.00 USD | 0.00 USD | `+6.37%` | `3,906.50` |
| `Live` | `Short` | `0.9395` | 20,910.00 USD | 3,560.00 USD | 0.00 USD | `+6.48%` | `3,784.30` |
| `Live` | `Short` | `0.9675` | 24,070.00 USD | 3,160.00 USD | 0.00 USD | `+9.66%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 89,130.00 USD | 65,060.00 USD | 0.00 USD | `+10.00%` | `67,040.50` |
| `Live` | `Short` | `0.9745` | 93,090.00 USD | 3,950.00 USD | 0.00 USD | `+10.45%` | `4,057.90` |
| `Live` | `Short` | `0.9775` | 93,190.00 USD | 100.88 USD | 0.00 USD | `+10.79%` | `103.20` |
| `Live` | `Short` | `0.9805` | 94,230.00 USD | 1,050.00 USD | 0.00 USD | `+11.13%` | `1,068.70` |
| `Live` | `Short` | `0.9885` | 99,160.00 USD | 4,930.00 USD | 0.00 USD | `+12.04%` | `4,982.50` |
| `Live` | `Short` | `0.9905` | 100,730.00 USD | 1,570.00 USD | 0.00 USD | `+12.26%` | `1,586.00` |
| `Live` | `Short` | `0.9925` | 103,150.00 USD | 2,420.00 USD | 0.00 USD | `+12.49%` | `2,434.50` |
| `Live` | `Short` | `1.00` | 103,480.00 USD | 330.29 USD | 0.00 USD | `+13.51%` | `329.80` |
| `Live` | `Short` | `1.02` | 103,650.00 USD | 170.40 USD | 0.00 USD | `+15.10%` | `167.80` |
| `Live` | `Short` | `1.04` | 103,800.00 USD | 155.92 USD | 0.00 USD | `+17.82%` | `150.00` |
| `Live` | `Short` | `1.04` | 103,940.00 USD | 139.22 USD | 0.00 USD | `+17.93%` | `133.80` |
| `Live` | `Short` | `1.05` | 104,540.00 USD | 597.52 USD | 0.00 USD | `+19.06%` | `568.80` |
| `Live` | `Short` | `1.05` | 106,930.00 USD | 2,390.00 USD | 0.00 USD | `+19.18%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 107,250.00 USD | 317.52 USD | 0.00 USD | `+19.40%` | `301.40` |
| `Live` | `Short` | `1.06` | 107,460.00 USD | 217.64 USD | 0.00 USD | `+19.63%` | `206.20` |
| `Live` | `Short` | `1.08` | 111,050.00 USD | 3,580.00 USD | 0.00 USD | `+22.46%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 111,210.00 USD | 166.43 USD | 0.00 USD | `+22.80%` | `153.60` |
| `Live` | `Short` | `1.09` | 116,760.00 USD | 5,550.00 USD | 0.00 USD | `+23.48%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 117,090.00 USD | 324.90 USD | 0.00 USD | `+24.62%` | `295.50` |
| `Live` | `Short` | `1.10` | 117,370.00 USD | 277.22 USD | 0.00 USD | `+24.73%` | `251.90` |
| `Live` | `Short` | `1.13` | 140,680.00 USD | 23,310.00 USD | 0.00 USD | `+27.68%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 141,090.00 USD | 418.33 USD | 0.00 USD | `+27.90%` | `370.70` |
| `Live` | `Short` | `1.13` | 142,460.00 USD | 1,370.00 USD | 0.00 USD | `+28.24%` | `1,207.00` |
| `Live` | `Short` | `1.13` | 143,090.00 USD | 634.09 USD | 0.00 USD | `+28.36%` | `559.90` |
| `Live` | `Short` | `1.20` | 144,550.00 USD | 1,450.00 USD | 0.00 USD | `+35.72%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 149,670.00 USD | 5,120.00 USD | 0.00 USD | `+35.84%` | `4,273.60` |
| `Live` | `Short` | `1.20` | 149,920.00 USD | 253.69 USD | 0.00 USD | `+35.95%` | `211.50` |
| `Live` | `Short` | `1.21` | 150,070.00 USD | 147.43 USD | 0.00 USD | `+36.63%` | `122.30` |
| `Live` | `Short` | `1.22` | 154,510.00 USD | 4,440.00 USD | 0.00 USD | `+38.10%` | `3,646.70` |
| `Live` | `Short` | `1.23` | 154,890.00 USD | 380.84 USD | 0.00 USD | `+39.92%` | `308.50` |
| `Live` | `Short` | `1.26` | 157,560.00 USD | 2,670.00 USD | 0.00 USD | `+42.75%` | `2,118.80` |
| `Live` | `Short` | `1.26` | 162,400.00 USD | 4,840.00 USD | 0.00 USD | `+43.20%` | `3,829.60` |
| `Live` | `Short` | `1.27` | 164,490.00 USD | 2,090.00 USD | 0.00 USD | `+44.22%` | `1,639.00` |
| `Live` | `Short` | `1.28` | 166,790.00 USD | 2,300.00 USD | 0.00 USD | `+44.79%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 206,670.00 USD | 39,880.00 USD | 0.00 USD | `+45.36%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 206,900.00 USD | 226.80 USD | 0.00 USD | `+46.72%` | `175.20` |
| `Live` | `Short` | `1.30` | 207,020.00 USD | 114.40 USD | 0.00 USD | `+47.17%` | `88.10` |
| `Live` | `Short` | `1.30` | 207,650.00 USD | 635.85 USD | 0.00 USD | `+47.74%` | `487.80` |
| `Live` | `Short` | `1.31` | 208,670.00 USD | 1,020.00 USD | 0.00 USD | `+48.42%` | `777.20` |
| `Live` | `Short` | `1.31` | 240,200.00 USD | 31,530.00 USD | 0.00 USD | `+48.64%` | `24,042.40` |
| `Live` | `Short` | `1.32` | 250,260.00 USD | 10,060.00 USD | 0.00 USD | `+49.66%` | `7,618.00` |
| `Live` | `Short` | `1.33` | 256,600.00 USD | 6,340.00 USD | 0.00 USD | `+50.23%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 278,570.00 USD | 21,970.00 USD | 0.00 USD | `+50.57%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 278,920.00 USD | 358.30 USD | 0.00 USD | `+50.80%` | `269.30` |
| `Live` | `Short` | `1.33` | 280,450.00 USD | 1,520.00 USD | 0.00 USD | `+51.02%` | `1,143.40` |
| `Live` | `Short` | `1.34` | 287,300.00 USD | 6,860.00 USD | 0.00 USD | `+51.82%` | `5,119.30` |
| `Live` | `Short` | `1.34` | 288,420.00 USD | 1,110.00 USD | 0.00 USD | `+52.38%` | `826.40` |
| `Live` | `Short` | `1.37` | 310,260.00 USD | 21,850.00 USD | 0.00 USD | `+55.33%` | `15,941.90` |
| `Live` | `Short` | `1.37` | 668,550.00 USD | 358,280.00 USD | 0.00 USD | `+55.56%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 672,990.00 USD | 4,450.00 USD | 0.00 USD | `+60.32%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 673,390.00 USD | 402.08 USD | 0.00 USD | `+62.81%` | `279.90` |
| `Live` | `Short` | `1.44` | 673,680.00 USD | 288.68 USD | 0.00 USD | `+63.26%` | `200.40` |
| `Live` | `Short` | `1.48` | 674,180.00 USD | 498.36 USD | 0.00 USD | `+67.46%` | `337.30` |
| `Live` | `Short` | `1.49` | 683,880.00 USD | 9,700.00 USD | 0.00 USD | `+69.38%` | `6,491.20` |
| `Live` | `Short` | `1.51` | 687,900.00 USD | 4,020.00 USD | 0.00 USD | `+71.65%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 688,340.00 USD | 440.55 USD | 0.00 USD | `+73.01%` | `288.60` |
| `Live` | `Short` | `1.53` | 705,470.00 USD | 17,130.00 USD | 0.00 USD | `+73.58%` | `11,182.60` |
| `Live` | `Short` | `1.54` | 705,610.00 USD | 144.34 USD | 0.00 USD | `+74.03%` | `94.00` |
| `Live` | `Short` | `1.56` | 705,740.00 USD | 132.03 USD | 0.00 USD | `+77.09%` | `84.50` |
| `Live` | `Short` | `1.58` | 706,030.00 USD | 285.21 USD | 0.00 USD | `+78.79%` | `180.80` |
| `Live` | `Short` | `1.65` | 727,360.00 USD | 21,330.00 USD | 0.00 USD | `+86.61%` | `12,957.30` |
| `Live` | `Short` | `1.66` | 735,040.00 USD | 7,680.00 USD | 0.00 USD | `+87.75%` | `4,636.10` |
| `Live` | `Short` | `1.66` | 774,140.00 USD | 39,090.00 USD | 0.00 USD | `+88.31%` | `23,529.40` |
| `Live` | `Short` | `1.69` | 774,300.00 USD | 165.81 USD | 0.00 USD | `+91.37%` | `98.20` |
| `Live` | `Short` | `1.69` | 1,070,000.00 USD | 292,630.00 USD | 0.00 USD | `+91.71%` | `173,000.00` |
| `Live` | `Short` | `1.69` | 1,070,000.00 USD | 951.86 USD | 0.00 USD | `+91.83%` | `562.40` |
| `Live` | `Short` | `1.70` | 1,070,000.00 USD | 2,310.00 USD | 0.00 USD | `+92.39%` | `1,360.10` |
| `Live` | `Short` | `1.70` | 1,080,000.00 USD | 9,620.00 USD | 0.00 USD | `+93.19%` | `5,645.40` |
| `Live` | `Short` | `1.71` | 1,080,000.00 USD | 205.67 USD | 0.00 USD | `+94.09%` | `120.10` |
| `Live` | `Short` | `1.73` | 1,080,000.00 USD | 226.05 USD | 0.00 USD | `+96.47%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,080,000.00 USD | 2,080.00 USD | 0.00 USD | `+97.27%` | `1,197.00` |
| `Live` | `Short` | `1.75` | 1,080,000.00 USD | 455.05 USD | 0.00 USD | `+97.83%` | `260.70` |
| `Live` | `Short` | `1.75` | 1,090,000.00 USD | 6,990.00 USD | 0.00 USD | `+98.17%` | `4,000.00` |
| `Live` | `Short` | `1.75` | 1,110,000.00 USD | 19,920.00 USD | 0.00 USD | `+98.51%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 1,120,000.00 USD | 11,350.00 USD | 0.00 USD | `+98.63%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,120,000.00 USD | 1,520.00 USD | 0.00 USD | `+98.85%` | `868.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,100,000.00 USD | 0.00 USD | 497.31 USD | `-70.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2745` | 1,100,000.00 USD | 0.00 USD | 455.97 USD | `-68.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,100,000.00 USD | 0.00 USD | 102.75 USD | `-61.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,100,000.00 USD | 0.00 USD | 256.78 USD | `-60.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,100,000.00 USD | 0.00 USD | 428.87 USD | `-55.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,100,000.00 USD | 0.00 USD | 123.45 USD | `-53.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,100,000.00 USD | 0.00 USD | 818.15 USD | `-52.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 1,100,000.00 USD | 0.00 USD | 454.04 USD | `-51.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,100,000.00 USD | 0.00 USD | 436.41 USD | `-50.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,100,000.00 USD | 0.00 USD | 876.79 USD | `-50.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,100,000.00 USD | 0.00 USD | 466.72 USD | `-48.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,100,000.00 USD | 0.00 USD | 142.95 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,100,000.00 USD | 0.00 USD | 781.98 USD | `-43.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,090,000.00 USD | 0.00 USD | 151.74 USD | `-41.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,090,000.00 USD | 0.00 USD | 123.91 USD | `-41.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,090,000.00 USD | 0.00 USD | 219.80 USD | `-37.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,090,000.00 USD | 0.00 USD | 237,400.00 USD | `-37.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 856,620.00 USD | 0.00 USD | 276.75 USD | `-37.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 856,340.00 USD | 0.00 USD | 2,010.00 USD | `-36.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 854,330.00 USD | 0.00 USD | 119.76 USD | `-34.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 854,210.00 USD | 0.00 USD | 470.62 USD | `-32.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 853,740.00 USD | 0.00 USD | 108.39 USD | `-31.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 853,630.00 USD | 0.00 USD | 123.28 USD | `-31.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 853,510.00 USD | 0.00 USD | 488.52 USD | `-29.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 853,020.00 USD | 0.00 USD | 4,230.00 USD | `-29.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 848,790.00 USD | 0.00 USD | 242.24 USD | `-28.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 848,550.00 USD | 0.00 USD | 193.95 USD | `-26.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 848,360.00 USD | 0.00 USD | 647.50 USD | `-26.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 847,710.00 USD | 0.00 USD | 834.79 USD | `-26.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 846,870.00 USD | 0.00 USD | 158.54 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 846,710.00 USD | 0.00 USD | 195.47 USD | `-25.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 846,520.00 USD | 0.00 USD | 190.25 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 846,330.00 USD | 0.00 USD | 153.53 USD | `-24.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 846,180.00 USD | 0.00 USD | 52,450.00 USD | `-24.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 793,730.00 USD | 0.00 USD | 536.11 USD | `-23.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 793,190.00 USD | 0.00 USD | 918.68 USD | `-22.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 792,270.00 USD | 0.00 USD | 340.75 USD | `-22.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 791,930.00 USD | 0.00 USD | 9,270.00 USD | `-21.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 782,670.00 USD | 0.00 USD | 120.53 USD | `-21.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 782,550.00 USD | 0.00 USD | 160.71 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 782,390.00 USD | 0.00 USD | 738.08 USD | `-21.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 781,650.00 USD | 0.00 USD | 187.61 USD | `-20.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 781,460.00 USD | 0.00 USD | 2,920.00 USD | `-20.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 778,540.00 USD | 0.00 USD | 89,150.00 USD | `-20.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 689,390.00 USD | 0.00 USD | 189.06 USD | `-19.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 689,200.00 USD | 0.00 USD | 5,650.00 USD | `-19.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 683,550.00 USD | 0.00 USD | 100.47 USD | `-19.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 683,450.00 USD | 0.00 USD | 152.05 USD | `-19.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 683,300.00 USD | 0.00 USD | 123.41 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 683,170.00 USD | 0.00 USD | 745.54 USD | `-17.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 682,430.00 USD | 0.00 USD | 1,130.00 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 681,300.00 USD | 0.00 USD | 18,770.00 USD | `-17.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 662,530.00 USD | 0.00 USD | 257.26 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 662,270.00 USD | 0.00 USD | 1,590.00 USD | `-15.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 660,670.00 USD | 0.00 USD | 10,160.00 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 650,520.00 USD | 0.00 USD | 93,810.00 USD | `-14.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 556,710.00 USD | 0.00 USD | 1,230.00 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 555,480.00 USD | 0.00 USD | 1,840.00 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 553,640.00 USD | 0.00 USD | 804.61 USD | `-13.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 552,840.00 USD | 0.00 USD | 191.12 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 552,650.00 USD | 0.00 USD | 273.92 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 552,370.00 USD | 0.00 USD | 125.92 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 552,250.00 USD | 0.00 USD | 1,980.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 550,270.00 USD | 0.00 USD | 1,150.00 USD | `-12.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 549,120.00 USD | 0.00 USD | 1,500.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 547,630.00 USD | 0.00 USD | 6,800.00 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 540,830.00 USD | 0.00 USD | 128.47 USD | `-11.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 540,700.00 USD | 0.00 USD | 10,090.00 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 530,610.00 USD | 0.00 USD | 135.11 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 530,480.00 USD | 0.00 USD | 8,870.00 USD | `-10.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 521,610.00 USD | 0.00 USD | 1,500.00 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 520,110.00 USD | 0.00 USD | 25,170.00 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 494,940.00 USD | 0.00 USD | 103.42 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 494,830.00 USD | 0.00 USD | 1,260.00 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 493,570.00 USD | 0.00 USD | 319.40 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 493,260.00 USD | 0.00 USD | 4,470.00 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 488,780.00 USD | 0.00 USD | 144.67 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 488,640.00 USD | 0.00 USD | 50,540.00 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 438,100.00 USD | 0.00 USD | 263.25 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 437,840.00 USD | 0.00 USD | 16,870.00 USD | `-8.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 420,970.00 USD | 0.00 USD | 91,080.00 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 329,890.00 USD | 0.00 USD | 174.63 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 329,720.00 USD | 0.00 USD | 13,470.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 316,250.00 USD | 0.00 USD | 125.72 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 316,120.00 USD | 0.00 USD | 4,860.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 311,270.00 USD | 0.00 USD | 19,320.00 USD | `-7.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 291,950.00 USD | 0.00 USD | 7,160.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 284,790.00 USD | 0.00 USD | 226.71 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 284,560.00 USD | 0.00 USD | 922.29 USD | `-6.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 283,640.00 USD | 0.00 USD | 1,120.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 282,520.00 USD | 0.00 USD | 325.56 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 282,190.00 USD | 0.00 USD | 577.25 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 281,620.00 USD | 0.00 USD | 5,760.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 275,860.00 USD | 0.00 USD | 171.46 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 275,690.00 USD | 0.00 USD | 1,270.00 USD | `-5.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 274,410.00 USD | 0.00 USD | 4,170.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 270,240.00 USD | 0.00 USD | 610.23 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 269,630.00 USD | 0.00 USD | 699.65 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 268,930.00 USD | 0.00 USD | 320.31 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 268,610.00 USD | 0.00 USD | 107,290.00 USD | `-4.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 161,320.00 USD | 0.00 USD | 710.23 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 160,610.00 USD | 0.00 USD | 212.81 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 160,400.00 USD | 0.00 USD | 6,370.00 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 154,030.00 USD | 0.00 USD | 481.80 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 153,550.00 USD | 0.00 USD | 12,330.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 141,220.00 USD | 0.00 USD | 901.40 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 140,320.00 USD | 0.00 USD | 345.13 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 139,970.00 USD | 0.00 USD | 16,140.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 123,830.00 USD | 0.00 USD | 3,640.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 120,190.00 USD | 0.00 USD | 980.47 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 119,210.00 USD | 0.00 USD | 325.20 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 118,880.00 USD | 0.00 USD | 7,800.00 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 111,080.00 USD | 0.00 USD | 726.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 110,360.00 USD | 0.00 USD | 247.60 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 110,110.00 USD | 0.00 USD | 1,260.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 108,850.00 USD | 0.00 USD | 921.70 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 107,930.00 USD | 0.00 USD | 2,220.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 105,700.00 USD | 0.00 USD | 1,270.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 104,430.00 USD | 0.00 USD | 741.45 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 103,690.00 USD | 0.00 USD | 826.73 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 102,870.00 USD | 0.00 USD | 5,340.00 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 97,520.00 USD | 0.00 USD | 11,850.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 85,670.00 USD | 0.00 USD | 712.45 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 84,960.00 USD | 0.00 USD | 58,490.00 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 26,470.00 USD | 0.00 USD | 2,420.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 24,050.00 USD | 0.00 USD | 133.10 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 23,920.00 USD | 0.00 USD | 257.92 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 23,660.00 USD | 0.00 USD | 9,070.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 14,590.00 USD | 0.00 USD | 151.10 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 14,440.00 USD | 0.00 USD | 2,000.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 12,440.00 USD | 0.00 USD | 8,370.00 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 4,070.00 USD | 0.00 USD | 4,070.00 USD | `-0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8825` | 5,020.00 USD | 5,020.00 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8835` | 14,780.00 USD | 9,770.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 18,440.00 USD | 3,660.00 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 22,040.00 USD | 3,600.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 25,660.00 USD | 3,620.00 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 37,010.00 USD | 11,360.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 45,800.00 USD | 8,780.00 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 56,140.00 USD | 10,340.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 56,610.00 USD | 469.91 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 67,220.00 USD | 10,610.00 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 74,320.00 USD | 7,100.00 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 77,240.00 USD | 2,920.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 81,140.00 USD | 3,900.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 81,430.00 USD | 289.12 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 99,630.00 USD | 18,210.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 102,350.00 USD | 2,710.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 131,310.00 USD | 28,960.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 140,310.00 USD | 8,990.00 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 142,360.00 USD | 2,050.00 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 143,290.00 USD | 926.06 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 144,090.00 USD | 805.29 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 147,310.00 USD | 3,220.00 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 149,300.00 USD | 1,990.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 171,750.00 USD | 22,450.00 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 172,000.00 USD | 250.83 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 173,100.00 USD | 1,090.00 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 174,620.00 USD | 1,520.00 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 177,510.00 USD | 2,880.00 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 179,720.00 USD | 2,210.00 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 180,750.00 USD | 1,030.00 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 183,770.00 USD | 3,020.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 184,090.00 USD | 318.79 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 184,340.00 USD | 252.49 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 184,650.00 USD | 309.14 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 188,550.00 USD | 3,900.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 190,520.00 USD | 1,970.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 190,640.00 USD | 116.59 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 449,760.00 USD | 259,120.00 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 601,720.00 USD | 151,960.00 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 606,790.00 USD | 5,070.00 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 733,140.00 USD | 126,350.00 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 734,540.00 USD | 1,400.00 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 739,120.00 USD | 4,580.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 741,900.00 USD | 2,780.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 742,190.00 USD | 287.62 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 742,450.00 USD | 266.85 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 742,560.00 USD | 103.17 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 742,920.00 USD | 366.52 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 743,070.00 USD | 148.85 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 743,170.00 USD | 100.90 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 743,740.00 USD | 568.87 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 746,440.00 USD | 2,700.00 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 746,970.00 USD | 523.79 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 747,670.00 USD | 701.16 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 749,540.00 USD | 1,880.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 802,600.00 USD | 53,060.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 806,510.00 USD | 3,910.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 815,470.00 USD | 8,960.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 816,000.00 USD | 529.50 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 816,580.00 USD | 579.45 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 822,290.00 USD | 5,710.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 823,080.00 USD | 789.04 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 823,200.00 USD | 117.81 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 824,250.00 USD | 1,050.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 830,260.00 USD | 6,000.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 830,520.00 USD | 261.97 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 830,790.00 USD | 265.66 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 830,940.00 USD | 159.19 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 840,850.00 USD | 9,910.00 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 844,000.00 USD | 3,150.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 845,440.00 USD | 1,440.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 848,320.00 USD | 2,890.00 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 855,930.00 USD | 7,600.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 856,050.00 USD | 121.54 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 856,150.00 USD | 100.17 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 908,650.00 USD | 52,510.00 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 908,820.00 USD | 161.82 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 909,290.00 USD | 469.51 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 909,430.00 USD | 139.23 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 910,760.00 USD | 1,340.00 USD | 0.00 USD | `+9.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 910,970.00 USD | 204.20 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 911,500.00 USD | 531.57 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 914,660.00 USD | 3,160.00 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 915,650.00 USD | 993.78 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 915,870.00 USD | 212.90 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 927,540.00 USD | 11,680.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 927,670.00 USD | 125.61 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 928,110.00 USD | 441.51 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 938,410.00 USD | 10,300.00 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 938,660.00 USD | 253.14 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 938,910.00 USD | 244.81 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 939,080.00 USD | 176.73 USD | 0.00 USD | `+10.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 939,280.00 USD | 201.77 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 939,580.00 USD | 295.22 USD | 0.00 USD | `+11.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 972,820.00 USD | 33,240.00 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 978,290.00 USD | 5,470.00 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 978,840.00 USD | 558.35 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 979,910.00 USD | 1,060.00 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 981,140.00 USD | 1,240.00 USD | 0.00 USD | `+11.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 981,630.00 USD | 490.99 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 982,280.00 USD | 644.82 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 983,270.00 USD | 991.50 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 993,610.00 USD | 10,340.00 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 994,020.00 USD | 409.52 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 994,300.00 USD | 284.92 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 994,580.00 USD | 277.64 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 994,930.00 USD | 350.37 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 995,070.00 USD | 144.04 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 995,180.00 USD | 105.44 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 1,000,000.00 USD | 8,760.00 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 1,570.00 USD | 0.00 USD | `+13.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 2,180.00 USD | 0.00 USD | `+13.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 363.87 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 589.52 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 110.62 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 10,090.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 5,420.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,030,000.00 USD | 2,080.00 USD | 0.00 USD | `+14.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,030,000.00 USD | 248.49 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 33,450.00 USD | 0.00 USD | `+15.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 722.63 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 312.07 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 171.24 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 561.11 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 249.30 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 2,210.00 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 432.18 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 137.88 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,070,000.00 USD | 2,470.00 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,070,000.00 USD | 160.60 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,070,000.00 USD | 6,560.00 USD | 0.00 USD | `+17.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 2,920.00 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 7,680.00 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 224.56 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,090,000.00 USD | 3,570.00 USD | 0.00 USD | `+18.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,090,000.00 USD | 432.19 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,090,000.00 USD | 5,890.00 USD | 0.00 USD | `+19.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,810.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 248.20 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 5,390.00 USD | 0.00 USD | `+19.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 285.32 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 1,130.00 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 1,240.00 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,830,000.00 USD | 278.06 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 309.00 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 272.12 USD | 0.00 USD | `+21.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 117.12 USD | 0.00 USD | `+21.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,970,000.00 USD | 140,120.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,970,000.00 USD | 530.01 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,970,000.00 USD | 128.23 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,080,000.00 USD | 108,190.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,080,000.00 USD | 550.49 USD | 0.00 USD | `+22.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,080,000.00 USD | 5,810.00 USD | 0.00 USD | `+23.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 5,570.00 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 1,290.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 294.81 USD | 0.00 USD | `+23.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 183.11 USD | 0.00 USD | `+24.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 123.13 USD | 0.00 USD | `+24.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 494.98 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 613.52 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,210,000.00 USD | 115,100.00 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,210,000.00 USD | 409.76 USD | 0.00 USD | `+24.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,210,000.00 USD | 162.77 USD | 0.00 USD | `+25.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,210,000.00 USD | 959.70 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,210,000.00 USD | 160.18 USD | 0.00 USD | `+25.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,210,000.00 USD | 433.10 USD | 0.00 USD | `+25.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,210,000.00 USD | 293.61 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,320,000.00 USD | 112,050.00 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 462.47 USD | 0.00 USD | `+27.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,330,000.00 USD | 2,180.00 USD | 0.00 USD | `+27.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,330,000.00 USD | 273.34 USD | 0.00 USD | `+28.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,330,000.00 USD | 119.49 USD | 0.00 USD | `+28.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,350,000.00 USD | 20,740.00 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,350,000.00 USD | 468.47 USD | 0.00 USD | `+28.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,350,000.00 USD | 1,430.00 USD | 0.00 USD | `+29.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,350,000.00 USD | 338.50 USD | 0.00 USD | `+29.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,350,000.00 USD | 769.57 USD | 0.00 USD | `+30.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,350,000.00 USD | 1,230.00 USD | 0.00 USD | `+30.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 2,450.00 USD | 0.00 USD | `+31.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 1,250.00 USD | 0.00 USD | `+31.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 143.67 USD | 0.00 USD | `+31.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,360,000.00 USD | 1,700.00 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,430,000.00 USD | 76,220.00 USD | 0.00 USD | `+32.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,430,000.00 USD | 304.33 USD | 0.00 USD | `+32.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,430,000.00 USD | 241.65 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,430,000.00 USD | 239.97 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,440,000.00 USD | 2,470.00 USD | 0.00 USD | `+33.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,440,000.00 USD | 3,060.00 USD | 0.00 USD | `+33.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,440,000.00 USD | 351.02 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,750,000.00 USD | 310,250.00 USD | 0.00 USD | `+34.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,750,000.00 USD | 309.53 USD | 0.00 USD | `+34.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,750,000.00 USD | 159.09 USD | 0.00 USD | `+35.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,750,000.00 USD | 146.21 USD | 0.00 USD | `+35.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,830,000.00 USD | 78,160.00 USD | 0.00 USD | `+36.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,830,000.00 USD | 933.81 USD | 0.00 USD | `+36.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,830,000.00 USD | 658.86 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,040,000.00 USD | 213,390.00 USD | 0.00 USD | `+37.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,040,000.00 USD | 211.10 USD | 0.00 USD | `+37.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,040,000.00 USD | 1,050.00 USD | 0.00 USD | `+37.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,040,000.00 USD | 509.71 USD | 0.00 USD | `+38.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,040,000.00 USD | 162.15 USD | 0.00 USD | `+39.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,040,000.00 USD | 187.04 USD | 0.00 USD | `+39.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,050,000.00 USD | 542.12 USD | 0.00 USD | `+39.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,070,000.00 USD | 23,740.00 USD | 0.00 USD | `+39.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,070,000.00 USD | 2,010.00 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,070,000.00 USD | 345.91 USD | 0.00 USD | `+40.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,070,000.00 USD | 104.79 USD | 0.00 USD | `+41.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,080,000.00 USD | 7,040.00 USD | 0.00 USD | `+41.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,080,000.00 USD | 517.52 USD | 0.00 USD | `+42.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,080,000.00 USD | 265.62 USD | 0.00 USD | `+42.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,080,000.00 USD | 1,480.00 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,080,000.00 USD | 1,010.00 USD | 0.00 USD | `+42.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,080,000.00 USD | 340.38 USD | 0.00 USD | `+44.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,080,000.00 USD | 903.22 USD | 0.00 USD | `+44.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,080,000.00 USD | 475.01 USD | 0.00 USD | `+44.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,120,000.00 USD | 41,160.00 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,140,000.00 USD | 12,840.00 USD | 0.00 USD | `+45.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,150,000.00 USD | 12,890.00 USD | 0.00 USD | `+46.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,160,000.00 USD | 8,820.00 USD | 0.00 USD | `+46.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,160,000.00 USD | 466.95 USD | 0.00 USD | `+46.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,160,000.00 USD | 613.59 USD | 0.00 USD | `+46.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,160,000.00 USD | 1,420.00 USD | 0.00 USD | `+46.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,170,000.00 USD | 13,000.00 USD | 0.00 USD | `+47.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,180,000.00 USD | 1,040.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 4,200,000.00 USD | 22,810.00 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,200,000.00 USD | 640.82 USD | 0.00 USD | `+50.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 4,210,000.00 USD | 13,400.00 USD | 0.00 USD | `+51.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,230,000.00 USD | 13,490.00 USD | 0.00 USD | `+52.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,240,000.00 USD | 11,580.00 USD | 0.00 USD | `+53.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,240,000.00 USD | 3,610.00 USD | 0.00 USD | `+53.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,240,000.00 USD | 1,540.00 USD | 0.00 USD | `+54.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,240,000.00 USD | 1,500.00 USD | 0.00 USD | `+54.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,260,000.00 USD | 15,000.00 USD | 0.00 USD | `+54.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,270,000.00 USD | 9,030.00 USD | 0.00 USD | `+55.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,270,000.00 USD | 569.84 USD | 0.00 USD | `+57.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,280,000.00 USD | 13,890.00 USD | 0.00 USD | `+57.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,290,000.00 USD | 2,710.00 USD | 0.00 USD | `+58.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,300,000.00 USD | 14,000.00 USD | 0.00 USD | `+58.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,310,000.00 USD | 13,100.00 USD | 0.00 USD | `+58.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,350,000.00 USD | 32,860.00 USD | 0.00 USD | `+59.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,350,000.00 USD | 7,090.00 USD | 0.00 USD | `+59.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,350,000.00 USD | 106.64 USD | 0.00 USD | `+60.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,350,000.00 USD | 1,430.00 USD | 0.00 USD | `+60.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,360,000.00 USD | 2,810.00 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,370,000.00 USD | 8,420.00 USD | 0.00 USD | `+61.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,370,000.00 USD | 1,410.00 USD | 0.00 USD | `+61.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,370,000.00 USD | 431.38 USD | 0.00 USD | `+62.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,370,000.00 USD | 1,390.00 USD | 0.00 USD | `+63.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,380,000.00 USD | 14,390.00 USD | 0.00 USD | `+63.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,390,000.00 USD | 7,000.00 USD | 0.00 USD | `+63.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,390,000.00 USD | 434.98 USD | 0.00 USD | `+64.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,410,000.00 USD | 14,490.00 USD | 0.00 USD | `+64.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,410,000.00 USD | 1,370.00 USD | 0.00 USD | `+64.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,410,000.00 USD | 1,350.00 USD | 0.00 USD | `+65.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,410,000.00 USD | 1,340.00 USD | 0.00 USD | `+66.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,410,000.00 USD | 1,300.00 USD | 0.00 USD | `+66.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,410,000.00 USD | 342.08 USD | 0.00 USD | `+67.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,410,000.00 USD | 1,330.00 USD | 0.00 USD | `+67.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,410,000.00 USD | 1,320.00 USD | 0.00 USD | `+68.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,410,000.00 USD | 1,310.00 USD | 0.00 USD | `+68.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,430,000.00 USD | 14,890.00 USD | 0.00 USD | `+68.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,440,000.00 USD | 9,580.00 USD | 0.00 USD | `+68.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,450,000.00 USD | 14,980.00 USD | 0.00 USD | `+69.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,580,000.00 USD | 121,130.00 USD | 0.00 USD | `+70.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,580,000.00 USD | 1,270.00 USD | 0.00 USD | `+72.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,580,000.00 USD | 1,260.00 USD | 0.00 USD | `+72.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,580,000.00 USD | 1,980.00 USD | 0.00 USD | `+74.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,580,000.00 USD | 574.53 USD | 0.00 USD | `+80.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,580,000.00 USD | 391.32 USD | 0.00 USD | `+81.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,580,000.00 USD | 1,160.00 USD | 0.00 USD | `+83.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,580,000.00 USD | 1,140.00 USD | 0.00 USD | `+85.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,590,000.00 USD | 1,970.00 USD | 0.00 USD | `+85.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,590,000.00 USD | 281.45 USD | 0.00 USD | `+88.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 4,590,000.00 USD | 958.84 USD | 0.00 USD | `+91.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,590,000.00 USD | 3,550.00 USD | 0.00 USD | `+92.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,590,000.00 USD | 1,070.00 USD | 0.00 USD | `+97.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,590,000.00 USD | 320.52 USD | 0.00 USD | `+98.40%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7630` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 36,930.00 USD | 14,770.00 USD | 327.66 USD |
| `7D` | `0.7650` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 969.48 USD | 23,090.00 USD | 10,340.00 USD |
| `1D` | `0.7660` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 101.33 USD | 4,420.00 USD |
| `7D` | `0.7670` | 11,520,000.00 USD | 0.00 USD | 11,520,000.00 USD | 0.00 USD | 177.87 USD | 19,060.00 USD |
| `7D` | `0.7690` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD |
| `7D` | `0.7710` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7790` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD |
| `1D` | `0.7800` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 0.00 USD | 7,100.00 USD | 22,420.00 USD |
| `7D` | `0.7810` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 0.00 USD | 185.50 USD | 5,300.00 USD |
| `7D` | `0.7830` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 5,390.00 USD |
| `7D` | `0.7850` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 13,480.00 USD |
| `7D` | `0.7870` | 11,470,000.00 USD | 0.00 USD | 11,470,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD |
| `1D` | `0.7880` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 26,800.00 USD | 572.15 USD | 0.00 USD |
| `7D` | `0.7890` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 190.39 USD |
| `1D` | `0.7900` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD |
| `7D` | `0.7910` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 0.00 USD | 18,650.00 USD | 0.00 USD |
| `1D` | `0.7920` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 0.00 USD | 731.00 USD | 0.00 USD |
| `7D` | `0.7930` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 35,140.00 USD |
| `1D` | `0.7940` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 0.00 USD | 4,350.00 USD | 14,510.00 USD |
| `7D` | `0.7950` | 11,400,000.00 USD | 0.00 USD | 11,400,000.00 USD | 9,530.00 USD | 6,180.00 USD | 51,800.00 USD |
| `1D` | `0.7960` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 428.05 USD | 11,240.00 USD |
| `7D` | `0.7970` | 11,330,000.00 USD | 0.00 USD | 11,330,000.00 USD | 9,430.00 USD | 0.00 USD | 9,700.00 USD |
| `1D` | `0.7980` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 2,830.00 USD | 8,900.00 USD | 10,830.00 USD |
| `7D` | `0.7990` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 911.48 USD | 0.00 USD | 8,530.00 USD |
| `1D` | `0.8000` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 0.00 USD | 11,260.00 USD | 16,320.00 USD |
| `7D` | `0.8010` | 11,300,000.00 USD | 0.00 USD | 11,300,000.00 USD | 0.00 USD | 14,760.00 USD | 35,960.00 USD |
| `7D` | `0.8030` | 11,250,000.00 USD | 0.00 USD | 11,250,000.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8050` | 11,250,000.00 USD | 0.00 USD | 11,250,000.00 USD | 0.00 USD | 15,820.00 USD | 0.00 USD |
| `1D` | `0.8060` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 12,740.00 USD | 13,670.00 USD | 14,150.00 USD |
| `7D` | `0.8070` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 2,040.00 USD | 11,280.00 USD | 0.00 USD |
| `1D` | `0.8080` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 0.00 USD | 8,280.00 USD | 0.00 USD |
| `1D` | `0.8100` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 12,970.00 USD | 5,430.00 USD | 19,940.00 USD |
| `7D` | `0.8110` | 11,220,000.00 USD | 0.00 USD | 11,220,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,470.00 USD |
| `1D` | `0.8120` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 27,480.00 USD | 1,350.00 USD | 5,320.00 USD |
| `7D` | `0.8130` | 11,120,000.00 USD | 0.00 USD | 11,120,000.00 USD | 44,870.00 USD | 16,750.00 USD | 12,160.00 USD |
| `1D` | `0.8140` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 44,940.00 USD | 23,740.00 USD | 22,730.00 USD |
| `7D` | `0.8150` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 137,850.00 USD | 50,280.00 USD | 125,310.00 USD |
| `1D` | `0.8160` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 111,700.00 USD | 22,860.00 USD | 149,520.00 USD |
| `7D` | `0.8170` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 90,990.00 USD | 23,590.00 USD | 78,630.00 USD |
| `1D` | `0.8180` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 11,610.00 USD | 20,880.00 USD | 20,350.00 USD |
| `7D` | `0.8190` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 194,350.00 USD | 52,010.00 USD | 47,110.00 USD |
| `1D` | `0.8200` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 13,230.00 USD | 16,660.00 USD | 36,060.00 USD |
| `7D` | `0.8210` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 137,160.00 USD | 56,860.00 USD | 152,120.00 USD |
| `1D` | `0.8220` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 12,100.00 USD | 19,830.00 USD | 30,520.00 USD |
| `7D` | `0.8230` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 38,600.00 USD | 35,700.00 USD | 63,710.00 USD |
| `1D` | `0.8240` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 21,120.00 USD | 16,700.00 USD | 20,080.00 USD |
| `7D` | `0.8250` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 188,770.00 USD | 27,530.00 USD | 126,580.00 USD |
| `1D` | `0.8260` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 17,700.00 USD | 4,440.00 USD | 14,020.00 USD |
| `7D` | `0.8270` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 141,740.00 USD | 51,050.00 USD | 62,500.00 USD |
| `1D` | `0.8280` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 22,620.00 USD | 12,830.00 USD | 33,850.00 USD |
| `7D` | `0.8290` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 88,370.00 USD | 40,370.00 USD | 82,690.00 USD |
| `1D` | `0.8300` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 13,880.00 USD | 9,690.00 USD | 25,690.00 USD |
| `7D` | `0.8310` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 38,140.00 USD | 32,050.00 USD | 24,250.00 USD |
| `1D` | `0.8320` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 19,130.00 USD | 29,090.00 USD | 67,320.00 USD |
| `7D` | `0.8330` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 152,500.00 USD | 85,780.00 USD | 200,500.00 USD |
| `1D` | `0.8340` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 49,780.00 USD | 16,200.00 USD | 47,570.00 USD |
| `7D` | `0.8350` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 76,840.00 USD | 15,430.00 USD | 83,530.00 USD |
| `1D` | `0.8360` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 75,630.00 USD | 23,510.00 USD | 20,660.00 USD |
| `7D` | `0.8370` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 146,620.00 USD | 60,250.00 USD | 101,350.00 USD |
| `1D` | `0.8380` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 29,780.00 USD | 14,800.00 USD | 28,800.00 USD |
| `7D` | `0.8390` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 26,140.00 USD | 87,820.00 USD | 78,050.00 USD |
| `1D` | `0.8400` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 80,010.00 USD | 26,570.00 USD | 33,570.00 USD |
| `7D` | `0.8410` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 54,830.00 USD | 40,110.00 USD | 28,680.00 USD |
| `1D` | `0.8420` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 45,210.00 USD | 35,080.00 USD | 22,140.00 USD |
| `7D` | `0.8430` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 77,650.00 USD | 84,470.00 USD | 30,600.00 USD |
| `1D` | `0.8440` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 21,450.00 USD | 12,010.00 USD | 291.54 USD |
| `7D` | `0.8450` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 50,250.00 USD | 55,690.00 USD | 114,430.00 USD |
| `1D` | `0.8460` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 3,860.00 USD | 23,780.00 USD | 40,760.00 USD |
| `7D` | `0.8470` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 25,980.00 USD | 6,020.00 USD | 34,390.00 USD |
| `1D` | `0.8480` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 46,950.00 USD | 35,940.00 USD | 85,540.00 USD |
| `7D` | `0.8490` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 43,620.00 USD | 32,060.00 USD | 152,140.00 USD |
| `1D` | `0.8500` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 56,320.00 USD | 51,020.00 USD | 155,200.00 USD |
| `7D` | `0.8510` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 93,500.00 USD | 42,650.00 USD | 78,920.00 USD |
| `1D` | `0.8520` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 96,680.00 USD | 61,140.00 USD | 66,990.00 USD |
| `7D` | `0.8530` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 39,890.00 USD | 52,520.00 USD | 24,370.00 USD |
| `1D` | `0.8540` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 56,450.00 USD | 46,460.00 USD | 65,400.00 USD |
| `7D` | `0.8550` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 69,370.00 USD | 63,400.00 USD | 93,230.00 USD |
| `1D` | `0.8560` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 28,740.00 USD | 27,040.00 USD | 10,970.00 USD |
| `7D` | `0.8570` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 96,770.00 USD | 166,050.00 USD | 5,380.00 USD |
| `1D` | `0.8580` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 180,840.00 USD | 34,130.00 USD | 114.50 USD |
| `7D` | `0.8590` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 57,950.00 USD | 12,270.00 USD | 16,510.00 USD |
| `1D` | `0.8600` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 32,470.00 USD | 33,380.00 USD | 636.30 USD |
| `7D` | `0.8610` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 49,960.00 USD | 120,290.00 USD | 34,680.00 USD |
| `1D` | `0.8620` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 6,610.00 USD | 35,120.00 USD | 666.95 USD |
| `7D` | `0.8630` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 25,030.00 USD | 13,800.00 USD | 181,640.00 USD |
| `1D` | `0.8640` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 40,460.00 USD | 34,720.00 USD | 126,260.00 USD |
| `7D` | `0.8650` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 227,130.00 USD | 16,780.00 USD | 308,640.00 USD |
| `1D` | `0.8660` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 184,320.00 USD | 33,670.00 USD | 271.63 USD |
| `7D` | `0.8670` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 159,830.00 USD | 41,080.00 USD | 52,740.00 USD |
| `1D` | `0.8680` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 98,550.00 USD | 70,170.00 USD | 112,520.00 USD |
| `7D` | `0.8690` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 175,280.00 USD | 9,930.00 USD | 267,390.00 USD |
| `1D` | `0.8700` | 826,270.00 USD | 0.00 USD | 826,270.00 USD | 59,260.00 USD | 6,380.00 USD | 898.09 USD |
| `7D` | `0.8710` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 619,190.00 USD | 13,020.00 USD | 390,380.00 USD |
| `1D` | `0.8720` | 759,730.00 USD | 0.00 USD | 759,730.00 USD | 1,300.00 USD | 54,700.00 USD | 308,910.00 USD |
| `7D` | `0.8730` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 318,460.00 USD | 78,000.00 USD | 387,540.00 USD |
| `1D` | `0.8740` | 394,830.00 USD | 0.00 USD | 394,830.00 USD | 0.00 USD | 19,580.00 USD | 45,570.00 USD |
| `7D` | `0.8750` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 648,980.00 USD | 118,620.00 USD | 318,630.00 USD |
| `1D` | `0.8760` | 329,670.00 USD | 0.00 USD | 329,670.00 USD | 3,590.00 USD | 34,150.00 USD | 178,920.00 USD |
| `7D` | `0.8770` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 405,620.00 USD | 14,470.00 USD | 0.00 USD |
| `1D` | `0.8780` | 113,020.00 USD | 0.00 USD | 113,020.00 USD | 5,990.00 USD | 0.00 USD | 305.84 USD |
| `7D` | `0.8790` | 999,150.00 USD | 0.00 USD | 999,150.00 USD | 293,480.00 USD | 67,620.00 USD | 0.00 USD |
| `1D` | `0.8800` | 106,720.00 USD | 0.00 USD | 106,720.00 USD | 7,330.00 USD | 60,300.00 USD | 722.37 USD |
| `7D` | `0.8810` | 638,050.00 USD | 0.00 USD | 638,050.00 USD | 637,180.00 USD | 0.00 USD | 869.19 USD |
| `1D` | `0.8820` | 38,360.00 USD | 0.00 USD | 38,360.00 USD | 36,230.00 USD | 0.00 USD | 305.55 USD |
| `7D` | `0.8820` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8830` | 773,660.00 USD | 773,660.00 USD | 0.00 USD | 768,360.00 USD | 0.00 USD | 5,300.00 USD |
| `1D` | `0.8840` | 1,820.00 USD | 0.00 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `1D` | `0.8850` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8850` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 523,060.00 USD | 0.00 USD | 6,050.00 USD |
| `1D` | `0.8860` | 745.79 USD | 745.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | 745.79 USD |
| `7D` | `0.8870` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 626,010.00 USD | 0.00 USD | 2,200.00 USD |
| `7D` | `0.8890` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 4,300.00 USD |
| `1D` | `0.8900` | 3,090.00 USD | 3,090.00 USD | 0.00 USD | 2,250.00 USD | 0.00 USD | 95.14 USD |
| `7D` | `0.8910` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 806,690.00 USD | 0.00 USD | 3,830.00 USD |
| `1D` | `0.8920` | 189,680.00 USD | 189,680.00 USD | 0.00 USD | 186,330.00 USD | 0.00 USD | 252.18 USD |
| `7D` | `0.8930` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 4,710.00 USD |
| `1D` | `0.8940` | 282,640.00 USD | 282,640.00 USD | 0.00 USD | 92,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8950` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 744,640.00 USD | 0.00 USD | 1,700.00 USD |
| `7D` | `0.8970` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 674,170.00 USD | 0.00 USD | 5,440.00 USD |
| `1D` | `0.8980` | 282,850.00 USD | 282,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 207.32 USD |
| `7D` | `0.8990` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 305,920.00 USD | 0.00 USD | 129,600.00 USD |
| `1D` | `0.9000` | 581,210.00 USD | 581,210.00 USD | 0.00 USD | 73,470.00 USD | 68,200.00 USD | 156,690.00 USD |
| `7D` | `0.9010` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 139,730.00 USD | 15,640.00 USD | 211,020.00 USD |
| `1D` | `0.9020` | 973,080.00 USD | 973,080.00 USD | 0.00 USD | 112,580.00 USD | 96,290.00 USD | 183,010.00 USD |
| `7D` | `0.9030` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 78,550.00 USD | 1,200.00 USD |
| `1D` | `0.9040` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 95,230.00 USD | 146,230.00 USD | 112,300.00 USD |
| `7D` | `0.9050` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 125,280.00 USD | 0.00 USD | 75,590.00 USD |
| `1D` | `0.9060` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 76,970.00 USD | 17,480.00 USD | 0.00 USD |
| `7D` | `0.9070` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 341,080.00 USD | 0.00 USD | 920.04 USD |
| `1D` | `0.9080` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 92,600.00 USD | 55,120.00 USD | 81,910.00 USD |
| `7D` | `0.9090` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 53,970.00 USD | 108,380.00 USD | 179,540.00 USD |
| `1D` | `0.9100` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 96,000.00 USD | 25,960.00 USD | 0.00 USD |
| `7D` | `0.9110` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 212,760.00 USD | 103,750.00 USD | 0.00 USD |
| `1D` | `0.9120` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 25,050.00 USD | 53,680.00 USD | 0.00 USD |
| `7D` | `0.9130` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 80,230.00 USD | 34,480.00 USD | 0.00 USD |
| `1D` | `0.9140` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 79,560.00 USD | 25,930.00 USD | 142,470.00 USD |
| `7D` | `0.9150` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 111,690.00 USD | 52,310.00 USD | 64,730.00 USD |
| `1D` | `0.9160` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 74,950.00 USD | 95,790.00 USD | 71,620.00 USD |
| `7D` | `0.9170` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 123,530.00 USD | 0.00 USD | 653.94 USD |
| `1D` | `0.9180` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 38,060.00 USD | 24,510.00 USD | 36,260.00 USD |
| `7D` | `0.9190` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 257,890.00 USD | 13,920.00 USD | 104,820.00 USD |
| `1D` | `0.9200` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 8,860.00 USD | 32,760.00 USD |
| `7D` | `0.9210` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 128,930.00 USD | 16,660.00 USD | 102,100.00 USD |
| `1D` | `0.9220` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 149,120.00 USD | 72,360.00 USD | 246,150.00 USD |
| `7D` | `0.9230` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD |
| `1D` | `0.9240` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 217,830.00 USD | 59,780.00 USD | 184,790.00 USD |
| `7D` | `0.9250` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 52,570.00 USD | 41,710.00 USD | 67,310.00 USD |
| `1D` | `0.9260` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 63,790.00 USD | 81,480.00 USD | 93,240.00 USD |
| `7D` | `0.9270` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 209,950.00 USD | 38,670.00 USD | 89,770.00 USD |
| `1D` | `0.9280` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 64,220.00 USD | 59,850.00 USD |
| `7D` | `0.9290` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 51,870.00 USD | 0.00 USD |
| `1D` | `0.9300` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 41,680.00 USD | 57,070.00 USD | 79,160.00 USD |
| `7D` | `0.9310` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 177,720.00 USD | 46,670.00 USD | 166,690.00 USD |
| `1D` | `0.9320` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 128,960.00 USD | 29,480.00 USD | 35,380.00 USD |
| `7D` | `0.9330` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 76,570.00 USD | 63,160.00 USD |
| `1D` | `0.9340` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 2,150.00 USD | 31,010.00 USD | 0.00 USD |
| `7D` | `0.9350` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 50,160.00 USD | 54,380.00 USD | 0.00 USD |
| `1D` | `0.9360` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 25,730.00 USD | 33,250.00 USD | 107,120.00 USD |
| `7D` | `0.9370` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 255,550.00 USD | 0.00 USD | 42,370.00 USD |
| `1D` | `0.9380` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 262,840.00 USD | 118,850.00 USD | 298,310.00 USD |
| `7D` | `0.9390` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 82,760.00 USD | 34,800.00 USD | 263,360.00 USD |
| `1D` | `0.9400` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 123,820.00 USD | 1,710.00 USD | 67,680.00 USD |
| `7D` | `0.9410` | 13,110,000.00 USD | 13,110,000.00 USD | 0.00 USD | 123,000.00 USD | 1,320.00 USD | 0.00 USD |
| `1D` | `0.9420` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 9,740.00 USD | 3,830.00 USD | 17,370.00 USD |
| `7D` | `0.9430` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 4,090.00 USD | 63,720.00 USD | 33,660.00 USD |
| `1D` | `0.9440` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 3,840.00 USD | 77,580.00 USD | 73,420.00 USD |
| `7D` | `0.9450` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 244,270.00 USD | 90,710.00 USD |
| `1D` | `0.9460` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 59,870.00 USD | 33,530.00 USD | 184,380.00 USD |
| `7D` | `0.9470` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 211,290.00 USD |
| `1D` | `0.9480` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 89,360.00 USD | 67,670.00 USD | 56,220.00 USD |
| `7D` | `0.9490` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 107,340.00 USD | 119,410.00 USD |
| `1D` | `0.9500` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 17,970.00 USD | 36,000.00 USD | 69,750.00 USD |
| `7D` | `0.9510` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 7,120.00 USD | 88,970.00 USD | 733,010.00 USD |
| `1D` | `0.9520` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 52,120.00 USD | 28,040.00 USD | 196,190.00 USD |
| `7D` | `0.9530` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 2,840.00 USD | 1,270.00 USD | 0.00 USD |
| `1D` | `0.9540` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 62,990.00 USD | 74,340.00 USD | 81,700.00 USD |
| `7D` | `0.9550` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 61,410.00 USD | 2,400.00 USD | 60,300.00 USD |
| `1D` | `0.9560` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 27,900.00 USD | 36,240.00 USD | 15,050.00 USD |
| `7D` | `0.9570` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 459,560.00 USD | 3,460.00 USD | 578.72 USD |
| `1D` | `0.9580` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 689.00 USD | 27,470.00 USD | 159.08 USD |
| `7D` | `0.9590` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 570,590.00 USD | 1,040.00 USD | 899.71 USD |
| `1D` | `0.9600` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 111,160.00 USD | 66,100.00 USD | 82,850.00 USD |
| `7D` | `0.9610` | 17,330,000.00 USD | 17,330,000.00 USD | 0.00 USD | 683,980.00 USD | 190,470.00 USD | 476,740.00 USD |
| `1D` | `0.9620` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 315,960.00 USD | 137,300.00 USD | 239,040.00 USD |
| `7D` | `0.9630` | 18,840,000.00 USD | 18,840,000.00 USD | 0.00 USD | 592,010.00 USD | 301,610.00 USD | 616,470.00 USD |
| `1D` | `0.9640` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 334,070.00 USD | 100,680.00 USD | 197,090.00 USD |
| `7D` | `0.9650` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 846,210.00 USD | 301,210.00 USD | 411,230.00 USD |
| `1D` | `0.9660` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 226,860.00 USD | 139,760.00 USD | 120,140.00 USD |
| `7D` | `0.9670` | 22,540,000.00 USD | 22,540,000.00 USD | 0.00 USD | 900,420.00 USD | 544,430.00 USD | 703,670.00 USD |
| `1D` | `0.9680` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 199,180.00 USD | 70,260.00 USD | 280,280.00 USD |
| `7D` | `0.9690` | 23,940,000.00 USD | 23,940,000.00 USD | 0.00 USD | 600,420.00 USD | 343,680.00 USD | 453,030.00 USD |
| `1D` | `0.9700` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 257,240.00 USD | 106,950.00 USD | 189,040.00 USD |
| `7D` | `0.9710` | 25,020,000.00 USD | 25,020,000.00 USD | 0.00 USD | 641,170.00 USD | 306,450.00 USD | 129,290.00 USD |
| `1D` | `0.9720` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 100,350.00 USD | 77,980.00 USD | 110,000.00 USD |
| `7D` | `0.9730` | 25,800,000.00 USD | 25,800,000.00 USD | 0.00 USD | 453,940.00 USD | 160,420.00 USD | 173,110.00 USD |
| `1D` | `0.9740` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 81,230.00 USD | 31,010.00 USD | 39,830.00 USD |
| `7D` | `0.9750` | 26,480,000.00 USD | 26,480,000.00 USD | 0.00 USD | 193,900.00 USD | 293,590.00 USD | 189,830.00 USD |
| `1D` | `0.9760` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 31,860.00 USD | 33,470.00 USD | 87,480.00 USD |
| `7D` | `0.9770` | 27,520,000.00 USD | 27,520,000.00 USD | 0.00 USD | 329,800.00 USD | 211,000.00 USD | 499,750.00 USD |
| `1D` | `0.9780` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 4,640.00 USD | 25,130.00 USD | 91,180.00 USD |
| `7D` | `0.9790` | 28,270,000.00 USD | 28,270,000.00 USD | 0.00 USD | 424,270.00 USD | 99,560.00 USD | 225,180.00 USD |
| `1D` | `0.9800` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 65,550.00 USD | 48,270.00 USD | 127,720.00 USD |
| `7D` | `0.9810` | 28,780,000.00 USD | 28,780,000.00 USD | 0.00 USD | 256,520.00 USD | 83,040.00 USD | 168,680.00 USD |
| `1D` | `0.9820` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD |
| `7D` | `0.9830` | 29,350,000.00 USD | 29,350,000.00 USD | 0.00 USD | 259,110.00 USD | 116,030.00 USD | 199,450.00 USD |
| `1D` | `0.9840` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 58,950.00 USD | 60,590.00 USD | 18,200.00 USD |
| `7D` | `0.9850` | 29,770,000.00 USD | 29,770,000.00 USD | 0.00 USD | 241,230.00 USD | 58,210.00 USD | 119,480.00 USD |
| `1D` | `0.9860` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 74,810.00 USD | 44,550.00 USD | 100,330.00 USD |
| `7D` | `0.9870` | 30,290,000.00 USD | 30,290,000.00 USD | 0.00 USD | 250,680.00 USD | 203,100.00 USD | 63,450.00 USD |
| `1D` | `0.9880` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 82,930.00 USD | 24,280.00 USD | 49,360.00 USD |
| `7D` | `0.9890` | 30,580,000.00 USD | 30,580,000.00 USD | 0.00 USD | 191,750.00 USD | 78,280.00 USD | 16,750.00 USD |
| `1D` | `0.9900` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 87,940.00 USD | 34,700.00 USD | 42,950.00 USD |
| `7D` | `0.9910` | 30,950,000.00 USD | 30,950,000.00 USD | 0.00 USD | 201,490.00 USD | 89,640.00 USD | 85,760.00 USD |
| `1D` | `0.9920` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 49,210.00 USD | 20,540.00 USD | 16,560.00 USD |
| `7D` | `0.9930` | 31,320,000.00 USD | 31,320,000.00 USD | 0.00 USD | 230,590.00 USD | 63,950.00 USD | 74,350.00 USD |
| `1D` | `0.9940` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 60,860.00 USD | 36,590.00 USD | 70,300.00 USD |
| `7D` | `0.9950` | 31,640,000.00 USD | 31,640,000.00 USD | 0.00 USD | 53,860.00 USD | 138,500.00 USD | 126,580.00 USD |
| `1D` | `0.9960` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 6,270.00 USD | 5,900.00 USD | 20,320.00 USD |
| `7D` | `0.9970` | 32,300,000.00 USD | 32,300,000.00 USD | 0.00 USD | 218,800.00 USD | 81,210.00 USD | 354,990.00 USD |
| `1D` | `0.9980` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 110,050.00 USD | 20,740.00 USD | 149,210.00 USD |
| `7D` | `0.9990` | 32,560,000.00 USD | 32,560,000.00 USD | 0.00 USD | 125,550.00 USD | 35,870.00 USD | 101,230.00 USD |
| `1D` | `1.00` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 16,340.00 USD | 21,440.00 USD | 16,850.00 USD |
| `7D` | `1.00` | 33,010,000.00 USD | 33,010,000.00 USD | 0.00 USD | 212,210.00 USD | 57,170.00 USD | 181,360.00 USD |
| `1D` | `1.00` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 15,000.00 USD | 17,420.00 USD | 36,190.00 USD |
| `7D` | `1.00` | 33,510,000.00 USD | 33,510,000.00 USD | 0.00 USD | 227,430.00 USD | 61,540.00 USD | 209,300.00 USD |
| `1D` | `1.00` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 15,370.00 USD | 21,270.00 USD | 30,450.00 USD |
| `7D` | `1.00` | 33,660,000.00 USD | 33,660,000.00 USD | 0.00 USD | 49,730.00 USD | 39,560.00 USD | 65,210.00 USD |
| `1D` | `1.01` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 9,400.00 USD | 13,960.00 USD | 8,760.00 USD |
| `7D` | `1.01` | 34,150,000.00 USD | 34,150,000.00 USD | 0.00 USD | 256,670.00 USD | 15,900.00 USD | 215,550.00 USD |
| `1D` | `1.01` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 17,690.00 USD | 8,610.00 USD | 12,090.00 USD |
| `7D` | `1.01` | 34,750,000.00 USD | 34,750,000.00 USD | 0.00 USD | 248,390.00 USD | 105,290.00 USD | 247,530.00 USD |
| `1D` | `1.01` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 17,560.00 USD | 5,290.00 USD | 14,820.00 USD |
| `7D` | `1.01` | 35,640,000.00 USD | 35,640,000.00 USD | 0.00 USD | 457,310.00 USD | 174,650.00 USD | 258,240.00 USD |
| `1D` | `1.01` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 21,660.00 USD | 13,540.00 USD | 33,850.00 USD |
| `7D` | `1.01` | 36,350,000.00 USD | 36,350,000.00 USD | 0.00 USD | 191,660.00 USD | 177,300.00 USD | 340,450.00 USD |
| `1D` | `1.01` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 13,360.00 USD | 10,400.00 USD | 25,990.00 USD |
| `7D` | `1.01` | 36,790,000.00 USD | 36,790,000.00 USD | 0.00 USD | 256,090.00 USD | 59,720.00 USD | 126,280.00 USD |
| `1D` | `1.02` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 21,410.00 USD | 10,550.00 USD | 6,610.00 USD |
| `7D` | `1.02` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 344,600.00 USD | 97,830.00 USD | 360,610.00 USD |
| `1D` | `1.02` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 18,050.00 USD | 4,150.00 USD | 133.18 USD |
| `7D` | `1.02` | 38,430,000.00 USD | 38,430,000.00 USD | 0.00 USD | 293,320.00 USD | 74,810.00 USD | 468,160.00 USD |
| `1D` | `1.02` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD |
| `7D` | `1.02` | 38,870,000.00 USD | 38,870,000.00 USD | 0.00 USD | 156,090.00 USD | 41,370.00 USD | 235,230.00 USD |
| `1D` | `1.02` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD |
| `7D` | `1.02` | 39,170,000.00 USD | 39,170,000.00 USD | 0.00 USD | 144,260.00 USD | 60,000.00 USD | 101,770.00 USD |
| `1D` | `1.02` | 12,920,000.00 USD | 12,920,000.00 USD | 0.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD |
| `7D` | `1.02` | 39,400,000.00 USD | 39,400,000.00 USD | 0.00 USD | 79,090.00 USD | 54,210.00 USD | 95,470.00 USD |
| `1D` | `1.03` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD |
| `7D` | `1.03` | 39,650,000.00 USD | 39,650,000.00 USD | 0.00 USD | 102,860.00 USD | 35,230.00 USD | 111,000.00 USD |
| `1D` | `1.03` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD |
| `7D` | `1.03` | 39,860,000.00 USD | 39,860,000.00 USD | 0.00 USD | 86,710.00 USD | 56,310.00 USD | 66,760.00 USD |
| `1D` | `1.03` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD |
| `1D` | `1.03` | 13,060,000.00 USD | 13,060,000.00 USD | 0.00 USD | 14,310.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `1.03` | 40,260,000.00 USD | 40,260,000.00 USD | 0.00 USD | 195,050.00 USD | 78,810.00 USD | 127,580.00 USD |
| `7D` | `1.03` | 40,590,000.00 USD | 40,590,000.00 USD | 0.00 USD | 57,170.00 USD | 103,690.00 USD | 163,650.00 USD |
| `7D` | `1.03` | 40,780,000.00 USD | 40,780,000.00 USD | 0.00 USD | 113,380.00 USD | 13,040.00 USD | 64,680.00 USD |
| `7D` | `1.04` | 41,180,000.00 USD | 41,180,000.00 USD | 0.00 USD | 179,260.00 USD | 40,110.00 USD | 182,150.00 USD |
| `7D` | `1.04` | 41,480,000.00 USD | 41,480,000.00 USD | 0.00 USD | 111,300.00 USD | 18,150.00 USD | 175,680.00 USD |
| `7D` | `1.04` | 41,710,000.00 USD | 41,710,000.00 USD | 0.00 USD | 103,260.00 USD | 52,580.00 USD | 72,310.00 USD |
| `7D` | `1.04` | 41,810,000.00 USD | 41,810,000.00 USD | 0.00 USD | 22,800.00 USD | 49,420.00 USD | 23,360.00 USD |
| `7D` | `1.04` | 41,890,000.00 USD | 41,890,000.00 USD | 0.00 USD | 65,460.00 USD | 17,210.00 USD | 738.90 USD |
| `7D` | `1.05` | 42,000,000.00 USD | 42,000,000.00 USD | 0.00 USD | 73,270.00 USD | 30,790.00 USD | 725.36 USD |
| `7D` | `1.05` | 42,070,000.00 USD | 42,070,000.00 USD | 0.00 USD | 39,320.00 USD | 20,630.00 USD | 16,100.00 USD |
| `7D` | `1.05` | 42,090,000.00 USD | 42,090,000.00 USD | 0.00 USD | 22,530.00 USD | 0.00 USD | 195.44 USD |
| `7D` | `1.05` | 42,180,000.00 USD | 42,180,000.00 USD | 0.00 USD | 6,060.00 USD | 47,690.00 USD | 28,720.00 USD |
| `7D` | `1.05` | 42,240,000.00 USD | 42,240,000.00 USD | 0.00 USD | 4,500.00 USD | 9,420.00 USD | 46,110.00 USD |
| `7D` | `1.06` | 42,240,000.00 USD | 42,240,000.00 USD | 0.00 USD | 3,670.00 USD | 2,060.00 USD | 72.32 USD |
| `7D` | `1.06` | 42,240,000.00 USD | 42,240,000.00 USD | 0.00 USD | 1,550.00 USD | 194.87 USD | 99.67 USD |
| `7D` | `1.06` | 42,300,000.00 USD | 42,300,000.00 USD | 0.00 USD | 16,550.00 USD | 3,870.00 USD | 32,890.00 USD |
| `7D` | `1.06` | 42,310,000.00 USD | 42,310,000.00 USD | 0.00 USD | 8,610.00 USD | 0.00 USD | 378.27 USD |
| `7D` | `1.06` | 42,310,000.00 USD | 42,310,000.00 USD | 0.00 USD | 4,190.00 USD | 1,110.00 USD | 216.19 USD |
| `7D` | `1.07` | 42,320,000.00 USD | 42,320,000.00 USD | 0.00 USD | 3,910.00 USD | 1,120.00 USD | 146.51 USD |
| `7D` | `1.07` | 42,350,000.00 USD | 42,350,000.00 USD | 0.00 USD | 0.00 USD | 12,740.00 USD | 17,950.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `583.50M` | Total OI Tokens: `658,433,164.8 SUI`
  * 1h OI Change: `+2.30%` | 4h OI Change: `-6.27%` | 24h OI Change: `-9.23%`
  * Exchange Breakdown: Binance=`107.97M` | Bybit=`77.87M` | OKX=`33.27M` | Hyperliquid=`28.98M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.15K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0021%` | **USDT OKX** | `0.0015%` |
| **USDT Bybit** | `-0.0050%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0021%` | **USDT BingX** | `0.0093%` |
| **USDT Gate** | `-0.0089%` | **USDT Bitget** | `0.0090%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `49.58%` | `50.42%` | `0.98` | 10,570,000.00 USD |
| `15M` | `Binance` | `54.24%` | `45.76%` | `1.19` | 4,080,000.00 USD |
| `15M` | `OKX` | `31.39%` | `68.61%` | `0.46` | 658,740.00 USD |
| `15M` | `Bybit` | `42.42%` | `57.58%` | `0.74` | 560,450.00 USD |
| `15M` | `KuCoin` | `47.9%` | `52.1%` | `0.92` | 32,290.00 USD |
| `15M` | `Gate` | `46.99%` | `53.01%` | `0.89` | 339,140.00 USD |
| `15M` | `Bitget` | `36.08%` | `63.92%` | `0.56` | 370,140.00 USD |
| `15M` | `BingX` | `47.59%` | `52.41%` | `0.91` | 718,960.00 USD |
| `15M` | `MEXC` | `49.59%` | `50.41%` | `0.98` | 916,110.00 USD |
| `15M` | `Bitunix` | `50.75%` | `49.25%` | `1.03` | 351,140.00 USD |
| `15M` | `Hyperliquid` | `27.32%` | `72.68%` | `0.38` | 167,420.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.88%` | `53.12%` | `0.88` | 1,860,000.00 USD |
| `15M` | `Crypto.com` | `89.16%` | `10.84%` | `8.23` | 760.26 USD |
| `15M` | `WhiteBIT` | `91.39%` | `8.61%` | `10.61` | 321,040.00 USD |
| `15M` | `HTX` | `22.65%` | `77.35%` | `0.29` | 1,410.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `63.55%` | `36.45%` | `1.74` | 14,820.00 USD |
| `15M` | `Aster` | `34.14%` | `65.86%` | `0.52` | 131,180.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `74.28%` | `25.72%` | `2.89` | 43,010.00 USD |
| `15M` | `Whale Positions` | `54.24%` | `45.76%` | `1.19` | 4,080,000.00 USD |
| `15M` | `Global Accounts` | `49.58%` | `50.42%` | `0.98` | 10,570,000.00 USD |
| `1H` | `SUI` | `51.80%` | `48.20%` | `1.07` | 42,510,000.00 USD |
| `1H` | `Binance` | `53.52%` | `46.48%` | `1.15` | 16,520,000.00 USD |
| `1H` | `OKX` | `50.03%` | `49.97%` | `1.00` | 2,510,000.00 USD |
| `1H` | `Bybit` | `55.72%` | `44.28%` | `1.26` | 2,820,000.00 USD |
| `1H` | `KuCoin` | `50.83%` | `49.17%` | `1.03` | 227,820.00 USD |
| `1H` | `Gate` | `49.02%` | `50.98%` | `0.96` | 1,220,000.00 USD |
| `1H` | `Bitget` | `45.28%` | `54.72%` | `0.83` | 1,440,000.00 USD |
| `1H` | `BingX` | `50.27%` | `49.73%` | `1.01` | 2,590,000.00 USD |
| `1H` | `MEXC` | `47.65%` | `52.35%` | `0.91` | 3,540,000.00 USD |
| `1H` | `Bitunix` | `51.28%` | `48.72%` | `1.05` | 1,080,000.00 USD |
| `1H` | `Hyperliquid` | `46.41%` | `53.59%` | `0.87` | 1,550,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.15%` | `50.85%` | `0.97` | 7,570,000.00 USD |
| `1H` | `Crypto.com` | `91.11%` | `8.89%` | `10.25` | 2,430.00 USD |
| `1H` | `WhiteBIT` | `84.79%` | `15.21%` | `5.57` | 990,310.00 USD |
| `1H` | `HTX` | `40.21%` | `59.79%` | `0.67` | 6,970.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `37.57%` | `62.43%` | `0.60` | 147,070.00 USD |
| `1H` | `Aster` | `29.58%` | `70.42%` | `0.42` | 208,700.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.13%` | `51.87%` | `0.93` | 109,480.00 USD |
| `1H` | `Whale Positions` | `53.52%` | `46.48%` | `1.15` | 16,520,000.00 USD |
| `1H` | `Global Accounts` | `51.80%` | `48.20%` | `1.07` | 42,510,000.00 USD |
| `4H` | `SUI` | `46.68%` | `53.32%` | `0.88` | 303,040,000.00 USD |
| `4H` | `Binance` | `47.26%` | `52.74%` | `0.90` | 124,180,000.00 USD |
| `4H` | `OKX` | `49.93%` | `50.07%` | `1.00` | 41,060,000.00 USD |
| `4H` | `Bybit` | `46.53%` | `53.47%` | `0.87` | 41,680,000.00 USD |
| `4H` | `KuCoin` | `45.31%` | `54.69%` | `0.83` | 3,510,000.00 USD |
| `4H` | `Gate` | `48.19%` | `51.81%` | `0.93` | 6,210,000.00 USD |
| `4H` | `Bitget` | `45.57%` | `54.43%` | `0.84` | 16,300,000.00 USD |
| `4H` | `BingX` | `44.39%` | `55.61%` | `0.80` | 9,640,000.00 USD |
| `4H` | `MEXC` | `43.67%` | `56.33%` | `0.78` | 25,930,000.00 USD |
| `4H` | `Bitunix` | `45.78%` | `54.22%` | `0.84` | 12,820,000.00 USD |
| `4H` | `Hyperliquid` | `42.79%` | `57.21%` | `0.75` | 10,470,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `45.25%` | `54.75%` | `0.83` | 2,010,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `42.64%` | `57.36%` | `0.74` | 4,880,000.00 USD |
| `4H` | `HTX` | `50.23%` | `49.77%` | `1.01` | 654,110.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.45%` | `55.55%` | `0.80` | 1,910,000.00 USD |
| `4H` | `Aster` | `40.72%` | `59.28%` | `0.69` | 1,400,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.97%` | `52.03%` | `0.92` | 373,870.00 USD |
| `4H` | `Whale Positions` | `47.26%` | `52.74%` | `0.90` | 124,180,000.00 USD |
| `4H` | `Global Accounts` | `46.68%` | `53.32%` | `0.88` | 303,040,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9302` | `0.9304` | `0.9302` | `0.9331` | `0.9288` | 1,273,512.84 USD | 565,164.16 USD | 708,348.68 USD | -143,184.52 USD | `-11.24%` | `4B / 11S` |
| `0:00 UTC` | `0.9115` | `0.9168` | `0.9115` | `0.9303` | `0.9099` | 9,410,634.53 USD | 4,625,948.50 USD | 4,784,686.02 USD | -158,737.52 USD | `-1.69%` | `3B / 20S` |
| `5:00 UTC` | `0.9172` | `0.9175` | `0.9172` | `0.9204` | `0.9146` | 2,946,350.12 USD | 1,501,911.34 USD | 1,444,438.78 USD | 57,472.55 USD | `+1.95%` | `10B / 6S` |
| `0:00 UTC` | `0.8942` | `0.8944` | `0.8942` | `0.9194` | `0.8750` | 25,714,743.86 USD | 10,323,786.97 USD | 15,390,956.89 USD | -5,067,169.92 USD | `-19.71%` | `3B / 22S` |
| `5:00 UTC` | `0.8801` | `0.8742` | `0.8801` | `0.8897` | `0.8575` | 25,765,113.89 USD | 12,461,836.10 USD | 13,303,277.79 USD | -841,441.70 USD | `-3.27%` | `7B / 12S` |
| `0:00 UTC` | `0.8841` | `0.8789` | `0.8841` | `0.8854` | `0.8692` | 12,554,511.67 USD | 6,312,205.57 USD | 6,242,306.10 USD | 69,899.48 USD | `+0.56%` | `13B / 6S` |
| `5:00 UTC` | `0.8962` | `0.8922` | `0.8962` | `0.8998` | `0.8850` | 10,029,099.72 USD | 5,129,823.74 USD | 4,899,275.97 USD | 230,547.77 USD | `+2.30%` | `13B / 7S` |
| `0:00 UTC` | `0.8977` | `0.8947` | `0.8977` | `0.9002` | `0.8853` | 5,070,824.21 USD | 2,682,042.86 USD | 2,388,781.36 USD | 293,261.50 USD | `+5.78%` | `18B / 23S` |
| `5:00 UTC` | `0.8865` | `0.8851` | `0.8865` | `0.8885` | `0.8800` | 5,162,774.90 USD | 2,355,111.64 USD | 2,807,663.26 USD | -452,551.62 USD | `-8.77%` | `10B / 8S` |
| `0:00 UTC` | `0.8800` | `0.8812` | `0.8800` | `0.8841` | `0.8793` | 1,246,375.57 USD | 589,300.79 USD | 657,074.78 USD | -67,773.99 USD | `-5.44%` | `14B / 5S` |

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
| `5m` | -223,420.00 USD | -580,250.00 USD | **`DISTRIBUTION`** |
| `15m` | -315,260.00 USD | -1,160,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -152,480.00 USD | -1,220,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -287,170.00 USD | 1,030,000.00 USD | **`ACCUMULATION`** |
| `2h` | -7,750,000.00 USD | -9,620,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -8,940,000.00 USD | -10,610,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,000,000.00 USD | -17,450,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,430,000.00 USD | -14,970,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,560,000.00 USD | -16,560,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,340,000.00 USD | -28,440,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -23,120,000.00 USD | -77,270,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -151,180,000.00 USD | -475,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-223.42K` | 15m=`-315.26K` | 1h=`-287.17K` | 24h=`-9.34M`
* Futures Capital Netflows: 5m=`-580.25K` | 15m=`-1.16M` | 1h=`+1.03M` | 24h=`-28.44M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
