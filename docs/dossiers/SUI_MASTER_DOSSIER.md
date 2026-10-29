# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:39:45 IST` (`2026-10-29 21:09:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8812` | `0.8826` | `0.8719` | `0.8737` | `3,867,282` | 3,391,372.76 USD | 498,079.59 USD | `+14.69%` | -16,379,171.95 USD | `+0.73` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.8736` | `0.8801` | `0.8692` | `0.8733` | `5,761,629` | 5,043,511.82 USD | 10,250.36 USD | `+0.20%` | -16,368,921.59 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.8733` | `0.8744` | `0.8714` | `0.8741` | `360,020` | 314,105.99 USD | -22,615.15 USD | `-7.20%` | -16,391,536.74 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9160` | `0.9191` | `0.8748` | `0.8780` | `28,755,173` | 25,714,743.86 USD | -5,067,169.92 USD | `-19.71%` | -15,637,034.17 USD | `-4.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8779` | `0.8897` | `0.8574` | `0.8737` | `29,477,241` | 25,765,113.89 USD | -841,441.70 USD | `-3.27%` | -16,478,475.87 USD | `-0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.8736` | `0.8801` | `0.8692` | `0.8728` | `6,038,036` | 5,284,569.46 USD | -40,394.97 USD | `-0.76%` | -16,518,870.84 USD | `+0.37` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9311` | `0.9338` | `0.9274` | `0.9295` | `5,959,668` | 5,545,537.10 USD | -24,776.87 USD | `-0.45%` | -9,951,062.67 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9294` | `0.9303` | `0.8574` | `0.8737` | `71,708,417` | 63,836,842.40 USD | -6,009,876.59 USD | `-9.41%` | -15,960,939.26 USD | `-3.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8736` | `0.8801` | `0.8692` | `0.8741` | `6,121,649` | 5,357,617.81 USD | -12,364.79 USD | `-0.23%` | -15,973,304.05 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8728` | `77,746,454` | 69,121,411.85 USD | -6,050,271.57 USD | `-8.75%` | -15,212,835.09 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9043` | `0.9222` | `0.9010` | `0.9063` | `37,205,563` | 33,852,646.16 USD | 118,750.50 USD | `+0.35%` | -8,478,733.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9064` | `0.9286` | `0.9052` | `0.9221` | `31,513,227` | 28,896,267.25 USD | -139,235.07 USD | `-0.48%` | -8,617,968.75 USD | `+0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9221` | `0.9548` | `0.9166` | `0.9539` | `53,988,780` | 50,583,791.87 USD | 2,028,716.92 USD | `+4.01%` | -6,589,251.83 USD | `+0.90` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -9,162,563.53 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8728` | `77,746,454` | 69,121,411.85 USD | -6,050,271.57 USD | `-8.75%` | -15,212,835.09 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `0.8768` | `564.4000` | 494.89 USD | 11,105.37 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8768` | `564.4000` | 494.88 USD | 11,600.25 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8768` | `564.4000` | 494.88 USD | 12,095.13 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8768` | `564.4000` | 494.87 USD | 12,590.00 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8768` | `564.4000` | 494.87 USD | 13,084.86 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8769` | `1065.9000` | 934.73 USD | 5,370.35 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `1065.9000` | 934.72 USD | 6,305.07 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `501.5000` | 439.78 USD | 6,744.84 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `501.5000` | 439.77 USD | 7,184.61 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `668.5000` | 586.21 USD | 7,770.82 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `668.5000` | 586.20 USD | 8,357.02 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `668.5000` | 586.19 USD | 8,943.22 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `668.5000` | 586.19 USD | 9,529.40 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8769` | `668.5000` | 586.18 USD | 10,115.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8769` | `564.4000` | 494.89 USD | 10,610.48 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `0.8770` | `281.0000` | 246.44 USD | 246.44 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.8770` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.88` | `0.00%` | `-` |
| `BID` | `0.8770` | `564.4000` | 494.97 USD | 494.97 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.8770` | `1128.8000` | 989.94 USD | 1,484.91 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.8770` | `1232.9000` | 1,081.22 USD | 2,566.12 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.8770` | `1065.9000` | 934.75 USD | 3,500.88 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `0.8770` | `1065.9000` | 934.74 USD | 4,435.62 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `0.8775` | `5705.0000` | 5,006.25 USD | 5,252.69 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8777` | `9421.1000` | 8,268.43 USD | 13,521.12 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.8778` | `19592.5000` | 17,199.08 USD | 30,720.20 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `0.8779` | `4557.2000` | 4,000.77 USD | 35,357.44 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `0.8779` | `725.0000` | 636.47 USD | 31,356.67 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `0.8780` | `2847.3000` | 2,499.93 USD | 64,127.41 USD | `1 orders` | `+0.11%` | `-` |
| `ASK` | `0.8780` | `29921.0000` | 26,270.04 USD | 61,627.48 USD | `2 orders` | `+0.11%` | `-` |
| `ASK` | `0.8782` | `1118.0000` | 981.78 USD | 65,109.19 USD | `1 orders` | `+0.13%` | `-` |
| `ASK` | `0.8783` | `56.9000` | 49.98 USD | 89,819.07 USD | `1 orders` | `+0.15%` | `-` |
| `ASK` | `0.8783` | `19592.5000` | 17,207.70 USD | 89,769.10 USD | `1 orders` | `+0.15%` | `-` |
| `ASK` | `0.8783` | `8485.1000` | 7,452.21 USD | 72,561.40 USD | `1 orders` | `+0.14%` | `-` |
| `ASK` | `0.8784` | `307.1000` | 269.76 USD | 90,088.83 USD | `2 orders` | `+0.16%` | `-` |
| `ASK` | `0.8785` | `31343.2000` | 27,534.37 USD | 117,794.15 USD | `1 orders` | `+0.17%` | `-` |
| `ASK` | `0.8785` | `194.6000` | 170.95 USD | 90,259.78 USD | `1 orders` | `+0.17%` | `-` |
| `ASK` | `0.8786` | `2730.9000` | 2,399.42 USD | 147,414.39 USD | `1 orders` | `+0.18%` | `-` |
| `ASK` | `0.8786` | `11389.4000` | 10,006.84 USD | 145,014.97 USD | `1 orders` | `+0.18%` | `-` |
| `ASK` | `0.8786` | `19592.5000` | 17,213.97 USD | 135,008.13 USD | `1 orders` | `+0.18%` | `-` |
| `ASK` | `0.8787` | `56994.0000` | 50,082.34 USD | 197,496.73 USD | `2 orders` | `+0.20%` | `-` |
| `ASK` | `0.8788` | `726.2000` | 638.15 USD | 198,134.88 USD | `1 orders` | `+0.20%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `673` | `0xb83d...6e36` | `SHORT` | 3,345,332.94 USD | `3,817,609.40` | `1.11` | `0.8781` | `39.08` | 873,402.38 USD | `+26.11%` | `3X Cross` |
| `1008` | `0xa2ce...3126` | `LONG` | 2,190,434.11 USD | `2,500,010.40` | `0.8597` | `0.8781` | `0.000000` | 41,227.58 USD | `+1.88%` | `10X Cross` |
| `1515` | `0x9946...0852` | `SHORT` | 1,434,021.82 USD | `1,632,538.50` | `1.08` | `0.8781` | `1.83` | 327,727.31 USD | `+22.85%` | `10X Cross` |
| `1797` | `0x9aa5...58af` | `SHORT` | 1,129,659.63 USD | `1,288,168.80` | `1.14` | `0.8781` | `7.84` | 338,033.26 USD | `+29.92%` | `10X Cross` |
| `1889` | `0x9df2...c665` | `SHORT` | 1,051,428.00 USD | `1,200,000.00` | `0.7465` | `0.8781` | `26.48` | -155,575.60 USD | `-14.80%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.13` | 8,037.68 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 8.04K USD at 1.1280 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 1,243.73 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.24K USD at 1.1280 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 932.74 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.93K USD at 1.1280 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 938.10 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.94K USD at 1.1278 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 1,250.84 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.25K USD at 1.1278 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 16,284.30 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 16.28K USD at 1.1278 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 5,005.18 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 5.01K USD at 1.1277 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 935.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.94K USD at 1.1276 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 1,247.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.25K USD at 1.1276 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 4,999.90 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 5.00K USD at 1.1275 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 124.48 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.12K USD at 1.1275 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 2,404.28 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 2.40K USD at 1.1275 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 400.00 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.40K USD at 1.1274 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 128.07 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.13K USD at 1.1274 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 16,278.53 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 16.28K USD at 1.1274 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 937.77 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.94K USD at 1.1274 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 1,250.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.25K USD at 1.1274 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 126.93 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.13K USD at 1.1273 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 4,113.38 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 4.11K USD at 1.1272 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 1,875.21 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.88K USD at 1.1272 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `1.13` | 14,724.10 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 14.72K USD at 1.1271 USD [API] | `2026-10-10 08:30:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9380` | 5,342.21 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9380 USD [API] | `2026-10-28 03:24:35` |
| `ANNOUNCEMENT` | `INFO` | `0.9444` | 153.28 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.15K USD at 0.9444 USD [API] | `2026-10-28 03:32:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9410` | 5,312.32 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.31K USD at 0.9410 USD [API] | `2026-10-28 03:58:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9399` | 5,342.09 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9399 USD [API] | `2026-10-28 04:50:23` |
| `ANNOUNCEMENT` | `INFO` | `0.9375` | 11,149.28 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 11.15K USD at 0.9375 USD [API] | `2026-10-28 05:00:00` |
| `ANNOUNCEMENT` | `INFO` | `0.9341` | 5,846.41 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.85K USD at 0.9341 USD [API] | `2026-10-28 07:10:32` |
| `ANNOUNCEMENT` | `INFO` | `0.9328` | 9,774.38 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 9.77K USD at 0.9328 USD [API] | `2026-10-28 07:13:57` |
| `ANNOUNCEMENT` | `INFO` | `0.9329` | 5,999.88 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.00K USD at 0.9329 USD [API] | `2026-10-28 07:13:57` |
| `ANNOUNCEMENT` | `INFO` | `0.9413` | 5,005.74 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9413 USD [API] | `2026-10-28 08:42:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9404` | 5,341.23 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9404 USD [API] | `2026-10-28 08:57:12` |
| `ANNOUNCEMENT` | `INFO` | `0.9404` | 56,738.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 56.74K USD at 0.9404 USD [API] | `2026-10-28 08:58:22` |
| `ANNOUNCEMENT` | `INFO` | `0.9404` | 12,757.07 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 12.76K USD at 0.9404 USD [API] | `2026-10-28 08:58:21` |
| `ANNOUNCEMENT` | `INFO` | `0.9365` | 4,999.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 5.00K USD at 0.9365 USD [API] | `2026-10-18 19:46:08` |
| `ANNOUNCEMENT` | `INFO` | `0.9393` | 5,344.54 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9393 USD [API] | `2026-10-28 09:05:57` |
| `ANNOUNCEMENT` | `INFO` | `0.9393` | 5,344.17 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9393 USD [API] | `2026-10-28 09:05:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9393` | 16,624.93 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 16.62K USD at 0.9393 USD [API] | `2026-10-28 09:08:01` |
| `ANNOUNCEMENT` | `INFO` | `0.9393` | 5,344.26 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9393 USD [API] | `2026-10-28 09:08:01` |
| `ANNOUNCEMENT` | `INFO` | `0.9404` | 5,342.36 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9404 USD [API] | `2026-10-28 09:10:25` |
| `ANNOUNCEMENT` | `INFO` | `0.9450` | 8,953.12 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 8.95K USD at 0.9450 USD [API] | `2026-10-28 10:01:50` |
| `ANNOUNCEMENT` | `INFO` | `0.9850` | 15,110.76 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 15.11K USD at 0.9850 USD [API] | `2026-10-15 02:23:38` |
| `ANNOUNCEMENT` | `INFO` | `0.9850` | 992.15 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.99K USD at 0.9850 USD [API] | `2026-10-15 02:23:38` |
| `ANNOUNCEMENT` | `INFO` | `0.9850` | 1,832.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.83K USD at 0.9850 USD [API] | `2026-10-15 02:23:38` |
| `ANNOUNCEMENT` | `INFO` | `0.9859` | 1,241.24 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.24K USD at 0.9859 USD [API] | `2026-10-15 02:23:38` |
| `ANNOUNCEMENT` | `INFO` | `0.9859` | 1,241.24 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.24K USD at 0.9859 USD [API] | `2026-10-15 02:23:38` |
| `ANNOUNCEMENT` | `INFO` | `0.9862` | 265.08 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.27K USD at 0.9862 USD [API] | `2026-10-15 02:23:38` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 5,004.24 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 5.00K USD at 1.0271 USD [API] | `2026-10-12 23:34:17` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 1,137.31 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.14K USD at 1.0271 USD [API] | `2026-10-12 23:34:17` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 185.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.19K USD at 1.0271 USD [API] | `2026-10-12 23:34:17` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 10,000.00 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 10.00K USD at 1.0272 USD [API] | `2026-10-12 23:34:17` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 9,999.94 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 10.00K USD at 1.0273 USD [API] | `2026-10-12 23:34:17` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 7,557.76 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 7.56K USD at 1.0274 USD [API] | `2026-10-12 23:34:17` |
| `ANNOUNCEMENT` | `INFO` | `0.9420` | 9,590.05 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 9.59K USD at 0.9420 USD [API] | `2026-10-28 11:34:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9420` | 10,000.03 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.00K USD at 0.9420 USD [API] | `2026-10-28 11:34:33` |
| `ANNOUNCEMENT` | `INFO` | `0.9420` | 10,000.03 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 10.00K USD at 0.9420 USD [API] | `2026-10-28 11:34:32` |


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
| `7D` | `Long Liquidation` | `0.7630` | 8,250,000.00 USD | 8,250,000.00 USD | 36,930.00 USD | 14,770.00 USD | 934.78 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7635` | 2,210.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,060.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7650` | 8,190,000.00 USD | 8,190,000.00 USD | 969.48 USD | 23,090.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7655` | 4,430.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7660` | 3,250,000.00 USD | 3,250,000.00 USD | 224.48 USD | 101.33 USD | 4,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7665` | 2,360.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7670` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 177.87 USD | 18,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7675` | 10,680.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7685` | 2,750.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7690` | 8,140,000.00 USD | 8,140,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7695` | 144,250.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 8,730.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7710` | 8,140,000.00 USD | 8,140,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7715` | 3,190.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 6,810.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 4,570.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 126.41 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 4,630.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 7,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 5,390.00 USD | 36.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 444.63 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7800` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 7,100.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7805` | 24,600.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7810` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 185.50 USD | 5,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,630.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7830` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 950.23 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7850` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7855` | 3,020.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 2,870.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7875` | 5,400.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7880` | 3,220,000.00 USD | 3,220,000.00 USD | 26,800.00 USD | 572.15 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7895` | 8,660.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,670.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 5,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7915` | 1,290.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 731.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 385.87 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7930` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 210.25 USD | 41,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 2,220.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7940` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 4,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 7,640.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 8,040,000.00 USD | 8,040,000.00 USD | 9,530.00 USD | 11,320.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 23,610.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 8,010,000.00 USD | 8,010,000.00 USD | 9,430.00 USD | 0.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 1,170.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 3,170,000.00 USD | 3,170,000.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 643.43 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 7,990,000.00 USD | 7,990,000.00 USD | 911.48 USD | 0.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 2,770.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 322.55 USD | 16,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 43,710.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8010` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 0.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 86,410.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8025` | 421.31 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8035` | 9,920.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8045` | 42,240.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8055` | 1,610.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 3,160,000.00 USD | 3,160,000.00 USD | 11,320.00 USD | 5,490.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 3,120,000.00 USD | 3,120,000.00 USD | 12,970.00 USD | 5,430.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 5,190.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8110` | 7,950,000.00 USD | 7,950,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 146.48 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 3,090,000.00 USD | 3,090,000.00 USD | 27,480.00 USD | 1,350.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 2,480.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8130` | 7,850,000.00 USD | 7,850,000.00 USD | 44,870.00 USD | 16,750.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 11,260.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 3,050,000.00 USD | 3,050,000.00 USD | 44,940.00 USD | 23,740.00 USD | 22,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 7,770,000.00 USD | 7,770,000.00 USD | 137,850.00 USD | 50,280.00 USD | 124,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 8,160.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 2,960,000.00 USD | 2,960,000.00 USD | 111,700.00 USD | 22,860.00 USD | 149,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 571.79 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8170` | 7,460,000.00 USD | 7,460,000.00 USD | 90,990.00 USD | 23,590.00 USD | 78,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 103,660.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 2,680,000.00 USD | 2,680,000.00 USD | 11,610.00 USD | 20,880.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 491.10 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 7,270,000.00 USD | 7,270,000.00 USD | 194,350.00 USD | 52,010.00 USD | 47,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 643.31 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 2,630,000.00 USD | 2,630,000.00 USD | 13,230.00 USD | 16,660.00 USD | 36,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 2,280.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8210` | 6,970,000.00 USD | 6,970,000.00 USD | 137,160.00 USD | 56,860.00 USD | 152,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 5,180.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 2,560,000.00 USD | 2,560,000.00 USD | 12,100.00 USD | 19,830.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 466.85 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 6,630,000.00 USD | 6,630,000.00 USD | 38,600.00 USD | 34,380.00 USD | 64,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 216.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 2,500,000.00 USD | 2,500,000.00 USD | 21,120.00 USD | 16,100.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 3,640.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 6,490,000.00 USD | 6,490,000.00 USD | 188,770.00 USD | 27,530.00 USD | 126,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 317.82 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 2,440,000.00 USD | 2,440,000.00 USD | 16,150.00 USD | 3,800.00 USD | 14,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 6,150,000.00 USD | 6,150,000.00 USD | 141,740.00 USD | 51,050.00 USD | 63,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 11,410.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 2,410,000.00 USD | 2,410,000.00 USD | 19,690.00 USD | 12,830.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 118,200.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8290` | 5,890,000.00 USD | 5,890,000.00 USD | 88,370.00 USD | 40,370.00 USD | 82,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8295` | 32,530.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8300` | 2,340,000.00 USD | 2,340,000.00 USD | 13,880.00 USD | 9,690.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8305` | 1,670.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8310` | 5,680,000.00 USD | 5,680,000.00 USD | 38,140.00 USD | 30,800.00 USD | 22,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 2,290,000.00 USD | 2,290,000.00 USD | 19,130.00 USD | 29,090.00 USD | 62,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8325` | 18,980.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8330` | 5,590,000.00 USD | 5,590,000.00 USD | 149,660.00 USD | 85,780.00 USD | 198,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 2,180,000.00 USD | 2,180,000.00 USD | 49,780.00 USD | 16,200.00 USD | 43,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 5,150,000.00 USD | 5,150,000.00 USD | 76,840.00 USD | 14,320.00 USD | 84,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 18,570.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 2,070,000.00 USD | 2,070,000.00 USD | 68,970.00 USD | 21,090.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 11,000.00 USD | 982,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 4,980,000.00 USD | 4,980,000.00 USD | 143,550.00 USD | 59,030.00 USD | 102,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 137.85 USD | 971,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 1,960,000.00 USD | 1,960,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 79,450.00 USD | 971,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8390` | 4,670,000.00 USD | 4,670,000.00 USD | 26,140.00 USD | 86,060.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 27,150.00 USD | 892,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 1,890,000.00 USD | 1,890,000.00 USD | 80,010.00 USD | 25,720.00 USD | 33,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8405` | 628.27 USD | 865,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8410` | 4,480,000.00 USD | 4,480,000.00 USD | 54,830.00 USD | 40,110.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 9,110.00 USD | 864,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 1,750,000.00 USD | 1,750,000.00 USD | 39,240.00 USD | 21,790.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 8,460.00 USD | 855,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8430` | 4,360,000.00 USD | 4,360,000.00 USD | 77,650.00 USD | 49,990.00 USD | 30,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 6,280.00 USD | 846,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 1,670,000.00 USD | 1,670,000.00 USD | 21,450.00 USD | 12,010.00 USD | 291.54 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 893.23 USD | 840,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8450` | 4,200,000.00 USD | 4,200,000.00 USD | 50,250.00 USD | 55,690.00 USD | 114,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 6,630.00 USD | 839,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 1,630,000.00 USD | 1,630,000.00 USD | 3,860.00 USD | 16,240.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8465` | 15,830.00 USD | 833,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8470` | 3,980,000.00 USD | 3,980,000.00 USD | 22,200.00 USD | 4,350.00 USD | 32,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 29,810.00 USD | 817,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 1,600,000.00 USD | 1,600,000.00 USD | 23,880.00 USD | 28,060.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8485` | 1,890.00 USD | 787,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8490` | 3,920,000.00 USD | 3,920,000.00 USD | 43,620.00 USD | 16,670.00 USD | 46,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 804.99 USD | 785,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 1,500,000.00 USD | 1,500,000.00 USD | 47,850.00 USD | 43,500.00 USD | 155,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 3,820,000.00 USD | 3,820,000.00 USD | 93,500.00 USD | 42,650.00 USD | 42,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 1,220.00 USD | 784,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 1,260,000.00 USD | 1,260,000.00 USD | 44,480.00 USD | 28,260.00 USD | 39,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 17,050.00 USD | 783,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8530` | 3,640,000.00 USD | 3,640,000.00 USD | 35,800.00 USD | 50,890.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 15,640.00 USD | 766,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 1,140,000.00 USD | 1,140,000.00 USD | 56,450.00 USD | 17,420.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8545` | 2,030.00 USD | 750,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8550` | 3,520,000.00 USD | 3,520,000.00 USD | 69,370.00 USD | 26,490.00 USD | 93,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8555` | 139.53 USD | 748,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8560` | 1,000,000.00 USD | 1,000,000.00 USD | 28,740.00 USD | 23,100.00 USD | 17,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8565` | 36,350.00 USD | 748,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8570` | 3,330,000.00 USD | 3,330,000.00 USD | 96,770.00 USD | 114,170.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 935,160.00 USD | 935,160.00 USD | 185,780.00 USD | 17,060.00 USD | 114.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8585` | 24,590.00 USD | 712,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8590` | 3,120,000.00 USD | 3,120,000.00 USD | 57,950.00 USD | 12,270.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 7,610.00 USD | 687,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 732,200.00 USD | 732,200.00 USD | 32,470.00 USD | 6,810.00 USD | 636.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 19,020.00 USD | 680,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8610` | 3,030,000.00 USD | 3,030,000.00 USD | 49,960.00 USD | 25,170.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8615` | 793.18 USD | 661,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8620` | 692,280.00 USD | 692,280.00 USD | 6,610.00 USD | 4,970.00 USD | 666.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 9,140.00 USD | 660,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 2,920,000.00 USD | 2,920,000.00 USD | 25,030.00 USD | 13,800.00 USD | 177,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 4,710.00 USD | 651,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 680,050.00 USD | 680,050.00 USD | 40,460.00 USD | 19,640.00 USD | 725.58 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 2,580.00 USD | 646,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 2,700,000.00 USD | 2,700,000.00 USD | 227,130.00 USD | 16,780.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8655` | 1,230.00 USD | 643,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 619,220.00 USD | 619,220.00 USD | 138,180.00 USD | 2,480.00 USD | 271.63 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,340.00 USD | 642,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 2,360,000.00 USD | 2,360,000.00 USD | 159,830.00 USD | 13,250.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8675` | 11,820.00 USD | 641,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 478,290.00 USD | 478,290.00 USD | 49,450.00 USD | 4,290.00 USD | 58,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8685` | 289.04 USD | 629,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8690` | 2,130,000.00 USD | 2,130,000.00 USD | 175,280.00 USD | 9,930.00 USD | 194,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 6,680.00 USD | 629,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 366,180.00 USD | 366,180.00 USD | 3,120.00 USD | 6,380.00 USD | 898.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 10,230.00 USD | 622,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,750,000.00 USD | 1,750,000.00 USD | 619,190.00 USD | 13,020.00 USD | 396,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 7,540.00 USD | 612,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 355,780.00 USD | 355,780.00 USD | 1,300.00 USD | 0.00 USD | 308,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8725` | 29,520.00 USD | 604,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8730` | 717,320.00 USD | 717,320.00 USD | 318,460.00 USD | 4,170.00 USD | 394,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8735` | 129,080.00 USD | 575,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8740` | 45,570.00 USD | 45,570.00 USD | 0.00 USD | 0.00 USD | 45,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8745` | 13,880.00 USD | 446,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8750` | 988,520.00 USD | 988,520.00 USD | 648,980.00 USD | 14,870.00 USD | 324,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8755` | 1,420.00 USD | 432,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8760` | 182,620.00 USD | 182,620.00 USD | 3,590.00 USD | 0.00 USD | 179,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 33,770.00 USD | 430,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8770` | 1,410,000.00 USD | 1,410,000.00 USD | 405,620.00 USD | 14,470.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8775` | 16,030.00 USD | 397,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8780` | 188,920.00 USD | 188,920.00 USD | 5,990.00 USD | 0.00 USD | 305.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8785` | 56,160.00 USD | 381,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8790` | 1,720,000.00 USD | 1,720,000.00 USD | 293,480.00 USD | 15,310.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 172,470.00 USD | 324,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8800` | 196,970.00 USD | 196,970.00 USD | 7,330.00 USD | 0.00 USD | 722.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8805` | 1,530.00 USD | 152,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8810` | 2,520,000.00 USD | 2,520,000.00 USD | 637,180.00 USD | 159,430.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8815` | 9,320.00 USD | 150,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8820` | 327,290.00 USD | 327,290.00 USD | 130,020.00 USD | 0.00 USD | 305.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8825` | 6,950.00 USD | 141,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8830` | 3,560,000.00 USD | 3,560,000.00 USD | 768,360.00 USD | 265,180.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8835` | 2,330.00 USD | 134,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8840` | 329,120.00 USD | 329,120.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 3,550.00 USD | 132,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8850` | 4,350,000.00 USD | 4,350,000.00 USD | 523,060.00 USD | 256,400.00 USD | 8,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8855` | 2,660.00 USD | 128,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8860` | 332,250.00 USD | 332,250.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8865` | 35,970.00 USD | 126,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8870` | 5,260,000.00 USD | 5,260,000.00 USD | 626,010.00 USD | 279,830.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8875` | 13,890.00 USD | 90,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8885` | 1,310.00 USD | 76,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8890` | 7,340,000.00 USD | 7,340,000.00 USD | 1,550,000.00 USD | 530,540.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8895` | 3,530.00 USD | 74,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8900` | 633,790.00 USD | 633,790.00 USD | 118,020.00 USD | 183,420.00 USD | 95.14 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8905` | 139.90 USD | 71,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8910` | 8,710,000.00 USD | 8,710,000.00 USD | 822,980.00 USD | 539,850.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8915` | 1,100.00 USD | 71,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8920` | 833,140.00 USD | 833,140.00 USD | 186,330.00 USD | 12,760.00 USD | 255.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8925` | 1,040.00 USD | 70,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8930` | 11,200,000.00 USD | 11,200,000.00 USD | 1,800,000.00 USD | 688,070.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8935` | 23,520.00 USD | 69,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8940` | 943,980.00 USD | 943,980.00 USD | 98,350.00 USD | 12,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8945` | 5,750.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8950` | 12,430,000.00 USD | 12,430,000.00 USD | 748,170.00 USD | 483,200.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8955` | 257.01 USD | 39,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8960` | 950,810.00 USD | 950,810.00 USD | 6,020.00 USD | 0.00 USD | 808.94 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8965` | 29,550.00 USD | 39,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8970` | 13,440,000.00 USD | 13,440,000.00 USD | 681,450.00 USD | 327,340.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8975` | 3,540.00 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.8980` | 952,820.00 USD | 952,820.00 USD | 1,810.00 USD | 0.00 USD | 207.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8985` | 320.05 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.8990` | 14,040,000.00 USD | 14,040,000.00 USD | 319,550.00 USD | 147,390.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8995` | 143.92 USD | 6,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9000` | 1,110,000.00 USD | 1,110,000.00 USD | 73,470.00 USD | 53,620.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9010` | 14,200,000.00 USD | 14,200,000.00 USD | 139,730.00 USD | 15,640.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 1,430,000.00 USD | 1,430,000.00 USD | 66,430.00 USD | 65,100.00 USD | 183,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9030` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 50,720.00 USD | 860.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9040` | 1,610,000.00 USD | 1,610,000.00 USD | 46,130.00 USD | 80,350.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9050` | 14,380,000.00 USD | 14,380,000.00 USD | 125,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9055` | 119.44 USD | 6,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9060` | 1,650,000.00 USD | 1,650,000.00 USD | 20,820.00 USD | 17,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9070` | 14,720,000.00 USD | 14,720,000.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.9075` | 5,960.00 USD | 5,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9080` | 1,830,000.00 USD | 1,830,000.00 USD | 92,600.00 USD | 426.90 USD | 81,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9090` | 14,990,000.00 USD | 14,990,000.00 USD | 53,970.00 USD | 34,550.00 USD | 179,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 1,930,000.00 USD | 1,930,000.00 USD | 96,000.00 USD | 6,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9110` | 15,200,000.00 USD | 15,200,000.00 USD | 212,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 1,960,000.00 USD | 1,960,000.00 USD | 25,050.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9130` | 15,280,000.00 USD | 15,280,000.00 USD | 80,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 2,210,000.00 USD | 2,210,000.00 USD | 79,560.00 USD | 25,930.00 USD | 142,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9150` | 15,460,000.00 USD | 15,460,000.00 USD | 111,690.00 USD | 0.00 USD | 64,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9160` | 2,360,000.00 USD | 2,360,000.00 USD | 74,950.00 USD | 27,950.00 USD | 45,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9170` | 15,580,000.00 USD | 15,580,000.00 USD | 123,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 2,390,000.00 USD | 2,390,000.00 USD | 14,990.00 USD | 16,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9190` | 15,840,000.00 USD | 15,840,000.00 USD | 257,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9200` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 1,140.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 16,050,000.00 USD | 16,050,000.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 2,800,000.00 USD | 2,800,000.00 USD | 124,570.00 USD | 39,420.00 USD | 219,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 16,500,000.00 USD | 16,500,000.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9240` | 3,230,000.00 USD | 3,230,000.00 USD | 189,760.00 USD | 59,780.00 USD | 184,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 16,670,000.00 USD | 16,670,000.00 USD | 52,570.00 USD | 41,710.00 USD | 67,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 3,440,000.00 USD | 3,440,000.00 USD | 63,790.00 USD | 53,330.00 USD | 92,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 16,970,000.00 USD | 16,970,000.00 USD | 209,950.00 USD | 0.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 53,570.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 3,710,000.00 USD | 3,710,000.00 USD | 35,710.00 USD | 40,000.00 USD | 79,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 17,360,000.00 USD | 17,360,000.00 USD | 177,720.00 USD | 46,670.00 USD | 166,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 3,910,000.00 USD | 3,910,000.00 USD | 128,960.00 USD | 29,480.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 17,470,000.00 USD | 17,470,000.00 USD | 0.00 USD | 50,420.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 3,910,000.00 USD | 3,910,000.00 USD | 2,150.00 USD | 857.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 17,570,000.00 USD | 17,570,000.00 USD | 50,160.00 USD | 52,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 4,070,000.00 USD | 4,070,000.00 USD | 25,730.00 USD | 33,250.00 USD | 103,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 17,870,000.00 USD | 17,870,000.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 4,750,000.00 USD | 4,750,000.00 USD | 262,840.00 USD | 118,850.00 USD | 293,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 18,250,000.00 USD | 18,250,000.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 4,930,000.00 USD | 4,930,000.00 USD | 114,940.00 USD | 1,710.00 USD | 67,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 18,370,000.00 USD | 18,370,000.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 4,960,000.00 USD | 4,960,000.00 USD | 9,740.00 USD | 0.00 USD | 17,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 62,100.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 5,110,000.00 USD | 5,110,000.00 USD | 2,290.00 USD | 75,230.00 USD | 73,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 5,380,000.00 USD | 5,380,000.00 USD | 56,940.00 USD | 33,530.00 USD | 184,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 5,600,000.00 USD | 5,600,000.00 USD | 89,360.00 USD | 67,670.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 5,720,000.00 USD | 5,720,000.00 USD | 17,970.00 USD | 36,000.00 USD | 69,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 20,060,000.00 USD | 20,060,000.00 USD | 7,120.00 USD | 87,720.00 USD | 732,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 6,000,000.00 USD | 6,000,000.00 USD | 52,120.00 USD | 28,040.00 USD | 196,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 6,210,000.00 USD | 6,210,000.00 USD | 62,990.00 USD | 74,340.00 USD | 78,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 20,190,000.00 USD | 20,190,000.00 USD | 61,410.00 USD | 1,290.00 USD | 60,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 6,280,000.00 USD | 6,280,000.00 USD | 21,240.00 USD | 33,820.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 20,650,000.00 USD | 20,650,000.00 USD | 456,500.00 USD | 2,240.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 6,310,000.00 USD | 6,310,000.00 USD | 689.00 USD | 26,200.00 USD | 159.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 21,220,000.00 USD | 21,220,000.00 USD | 570,590.00 USD | 1,040.00 USD | 289.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 6,570,000.00 USD | 6,570,000.00 USD | 111,160.00 USD | 66,100.00 USD | 82,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 22,570,000.00 USD | 22,570,000.00 USD | 683,980.00 USD | 190,470.00 USD | 476,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 7,260,000.00 USD | 7,260,000.00 USD | 315,960.00 USD | 137,300.00 USD | 239,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 24,080,000.00 USD | 24,080,000.00 USD | 592,010.00 USD | 301,610.00 USD | 616,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 7,910,000.00 USD | 7,910,000.00 USD | 334,070.00 USD | 117,160.00 USD | 197,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 25,640,000.00 USD | 25,640,000.00 USD | 846,210.00 USD | 301,210.00 USD | 412,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 8,410,000.00 USD | 8,410,000.00 USD | 243,570.00 USD | 134,450.00 USD | 120,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 27,780,000.00 USD | 27,780,000.00 USD | 900,420.00 USD | 530,640.00 USD | 705,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9675` | 3,160.00 USD | 3,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9680` | 9,010,000.00 USD | 9,010,000.00 USD | 244,690.00 USD | 78,670.00 USD | 280,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 29,170,000.00 USD | 29,170,000.00 USD | 600,420.00 USD | 343,680.00 USD | 446,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 9,600,000.00 USD | 9,600,000.00 USD | 257,240.00 USD | 134,760.00 USD | 199,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9705` | 65,060.00 USD | 68,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9710` | 30,260,000.00 USD | 30,260,000.00 USD | 641,170.00 USD | 305,860.00 USD | 144,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9715` | 398.41 USD | 68,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9720` | 9,980,000.00 USD | 9,980,000.00 USD | 122,820.00 USD | 117,970.00 USD | 138,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 31,050,000.00 USD | 31,050,000.00 USD | 453,940.00 USD | 160,420.00 USD | 177,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 10,130,000.00 USD | 10,130,000.00 USD | 81,230.00 USD | 31,010.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 31,730,000.00 USD | 31,730,000.00 USD | 193,900.00 USD | 293,590.00 USD | 193,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9755` | 121.55 USD | 68,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 10,270,000.00 USD | 10,270,000.00 USD | 30,550.00 USD | 24,570.00 USD | 76,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9765` | 365.89 USD | 69,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9770` | 32,770,000.00 USD | 32,770,000.00 USD | 329,800.00 USD | 211,000.00 USD | 500,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9775` | 100.88 USD | 69,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9780` | 10,380,000.00 USD | 10,380,000.00 USD | 4,640.00 USD | 14,190.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 33,500,000.00 USD | 33,500,000.00 USD | 424,270.00 USD | 84,800.00 USD | 222,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 10,620,000.00 USD | 10,620,000.00 USD | 65,550.00 USD | 48,270.00 USD | 127,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 15,580.00 USD | 84,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 34,010,000.00 USD | 34,010,000.00 USD | 254,630.00 USD | 83,040.00 USD | 169,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 10,820,000.00 USD | 10,820,000.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 34,570,000.00 USD | 34,570,000.00 USD | 259,110.00 USD | 100,200.00 USD | 199,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 10,960,000.00 USD | 10,960,000.00 USD | 58,950.00 USD | 62,010.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9845` | 10,440.00 USD | 95,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9850` | 34,990,000.00 USD | 34,990,000.00 USD | 241,230.00 USD | 58,210.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 11,210,000.00 USD | 11,210,000.00 USD | 104,500.00 USD | 43,210.00 USD | 100,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 35,480,000.00 USD | 35,480,000.00 USD | 248,640.00 USD | 191,820.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 732.03 USD | 95,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 11,380,000.00 USD | 11,380,000.00 USD | 82,930.00 USD | 26,290.00 USD | 61,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,930.00 USD | 100,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9890` | 35,770,000.00 USD | 35,770,000.00 USD | 191,750.00 USD | 78,280.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 11,570,000.00 USD | 11,570,000.00 USD | 87,940.00 USD | 43,020.00 USD | 51,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 2,670.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9910` | 36,150,000.00 USD | 36,150,000.00 USD | 201,490.00 USD | 89,640.00 USD | 81,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 11,690,000.00 USD | 11,690,000.00 USD | 62,110.00 USD | 41,490.00 USD | 21,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 2,420.00 USD | 105,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 36,520,000.00 USD | 36,520,000.00 USD | 230,590.00 USD | 63,950.00 USD | 74,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 11,860,000.00 USD | 11,860,000.00 USD | 60,860.00 USD | 36,960.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9945` | 6,430.00 USD | 112,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9950` | 36,840,000.00 USD | 36,840,000.00 USD | 53,860.00 USD | 138,500.00 USD | 130,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 11,890,000.00 USD | 11,890,000.00 USD | 6,270.00 USD | 7,010.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9965` | 2,430.00 USD | 114,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9970` | 37,490,000.00 USD | 37,490,000.00 USD | 218,800.00 USD | 81,210.00 USD | 354,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 12,180,000.00 USD | 12,180,000.00 USD | 110,050.00 USD | 21,830.00 USD | 152,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 37,750,000.00 USD | 37,750,000.00 USD | 125,550.00 USD | 35,870.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,230,000.00 USD | 12,230,000.00 USD | 17,400.00 USD | 21,440.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 38,210,000.00 USD | 38,210,000.00 USD | 212,210.00 USD | 57,170.00 USD | 185,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,300,000.00 USD | 12,300,000.00 USD | 15,900.00 USD | 17,420.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 38,710,000.00 USD | 38,710,000.00 USD | 227,430.00 USD | 61,540.00 USD | 208,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 12,370,000.00 USD | 12,370,000.00 USD | 15,370.00 USD | 21,270.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 235.86 USD | 115,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 38,860,000.00 USD | 38,860,000.00 USD | 49,730.00 USD | 39,560.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,400,000.00 USD | 12,400,000.00 USD | 9,400.00 USD | 14,230.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 39,350,000.00 USD | 39,350,000.00 USD | 256,670.00 USD | 15,900.00 USD | 212,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,440,000.00 USD | 12,440,000.00 USD | 18,940.00 USD | 9,170.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 39,950,000.00 USD | 39,950,000.00 USD | 248,390.00 USD | 105,290.00 USD | 247,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,480,000.00 USD | 12,480,000.00 USD | 17,560.00 USD | 5,570.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 40,900,000.00 USD | 40,900,000.00 USD | 457,310.00 USD | 174,650.00 USD | 319,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,550,000.00 USD | 12,550,000.00 USD | 21,660.00 USD | 13,820.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 41,740,000.00 USD | 41,740,000.00 USD | 260,120.00 USD | 234,510.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 12,600,000.00 USD | 12,600,000.00 USD | 13,360.00 USD | 11,780.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 42,180,000.00 USD | 42,180,000.00 USD | 256,090.00 USD | 59,720.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 115,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,640,000.00 USD | 12,640,000.00 USD | 22,200.00 USD | 10,550.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.02` | 8,980.00 USD | 124,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.02` | 42,980,000.00 USD | 42,980,000.00 USD | 344,600.00 USD | 97,830.00 USD | 360,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,660,000.00 USD | 12,660,000.00 USD | 18,720.00 USD | 4,150.00 USD | 133.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 43,820,000.00 USD | 43,820,000.00 USD | 293,320.00 USD | 74,810.00 USD | 469,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,750,000.00 USD | 12,750,000.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 44,250,000.00 USD | 44,250,000.00 USD | 156,090.00 USD | 41,370.00 USD | 235,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,840,000.00 USD | 12,840,000.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 44,560,000.00 USD | 44,560,000.00 USD | 144,260.00 USD | 60,000.00 USD | 103,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 12,910,000.00 USD | 12,910,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 44,790,000.00 USD | 44,790,000.00 USD | 79,090.00 USD | 54,210.00 USD | 94,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,970,000.00 USD | 12,970,000.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 45,040,000.00 USD | 45,040,000.00 USD | 102,860.00 USD | 35,230.00 USD | 110,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 12,990,000.00 USD | 12,990,000.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 45,250,000.00 USD | 45,250,000.00 USD | 86,710.00 USD | 56,310.00 USD | 67,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 13,020,000.00 USD | 13,020,000.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 45,680,000.00 USD | 45,680,000.00 USD | 195,050.00 USD | 78,810.00 USD | 157,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 13,050,000.00 USD | 13,050,000.00 USD | 19,720.00 USD | 7,410.00 USD | 0.35 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 152.91 USD | 124,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.03` | 46,060,000.00 USD | 46,060,000.00 USD | 91,400.00 USD | 132,300.00 USD | 163,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 13,060,000.00 USD | 13,060,000.00 USD | 439.80 USD | 4,130.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 46,250,000.00 USD | 46,250,000.00 USD | 113,380.00 USD | 13,040.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 13,130,000.00 USD | 13,130,000.00 USD | 18,450.00 USD | 7,120.00 USD | 43,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 46,660,000.00 USD | 46,660,000.00 USD | 179,260.00 USD | 41,220.00 USD | 181,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 109.46 USD | 124,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 46,960,000.00 USD | 46,960,000.00 USD | 113,030.00 USD | 19,230.00 USD | 175,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 10,400.00 USD | 134,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 139.22 USD | 135,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 47,190,000.00 USD | 47,190,000.00 USD | 103,260.00 USD | 54,310.00 USD | 72,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 47,290,000.00 USD | 47,290,000.00 USD | 24,360.00 USD | 49,420.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 47,380,000.00 USD | 47,380,000.00 USD | 65,460.00 USD | 17,210.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 47,480,000.00 USD | 47,480,000.00 USD | 73,270.00 USD | 30,790.00 USD | 294.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 47,560,000.00 USD | 47,560,000.00 USD | 39,320.00 USD | 20,630.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 135,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 47,580,000.00 USD | 47,580,000.00 USD | 22,530.00 USD | 0.00 USD | 538.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 138,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,330.00 USD | 139,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 47,660,000.00 USD | 47,660,000.00 USD | 6,060.00 USD | 47,690.00 USD | 28,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 317.52 USD | 139,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 217.44 USD | 139,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 47,720,000.00 USD | 47,720,000.00 USD | 5,800.00 USD | 4,160.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 47,730,000.00 USD | 47,730,000.00 USD | 3,670.00 USD | 3,350.00 USD | 197.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 47,730,000.00 USD | 47,730,000.00 USD | 2,710.00 USD | 194.87 USD | 59.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 47,760,000.00 USD | 47,760,000.00 USD | 16,550.00 USD | 3,870.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 47,770,000.00 USD | 47,770,000.00 USD | 8,610.00 USD | 0.00 USD | 609.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 47,780,000.00 USD | 47,780,000.00 USD | 4,190.00 USD | 1,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 47,780,000.00 USD | 47,780,000.00 USD | 3,910.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 47,810,000.00 USD | 47,810,000.00 USD | 0.00 USD | 5,360.00 USD | 17,950.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.1945` | 4,620,000.00 USD | 0.00 USD | 1,410.00 USD | `-77.74%` | `7,229.50` |
| `Live` | `Long` | `0.1955` | 4,620,000.00 USD | 0.00 USD | 2,410.00 USD | `-77.62%` | `12,310.50` |
| `Live` | `Long` | `0.1995` | 4,610,000.00 USD | 0.00 USD | 256.00 USD | `-77.16%` | `1,283.20` |
| `Live` | `Long` | `0.2045` | 4,610,000.00 USD | 0.00 USD | 204.50 USD | `-76.59%` | `1,000.00` |
| `Live` | `Long` | `0.2135` | 4,610,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.56%` | `18,919.90` |
| `Live` | `Long` | `0.2195` | 4,610,000.00 USD | 0.00 USD | 852.58 USD | `-74.88%` | `3,884.20` |
| `Live` | `Long` | `0.2265` | 4,610,000.00 USD | 0.00 USD | 220.32 USD | `-74.07%` | `972.70` |
| `Live` | `Long` | `0.2355` | 4,610,000.00 USD | 0.00 USD | 1,030.00 USD | `-73.04%` | `4,353.10` |
| `Live` | `Long` | `0.2385` | 4,610,000.00 USD | 0.00 USD | 156.36 USD | `-72.70%` | `655.60` |
| `Live` | `Long` | `0.2505` | 4,610,000.00 USD | 0.00 USD | 2,540.00 USD | `-71.33%` | `10,152.10` |
| `Live` | `Long` | `0.2525` | 4,600,000.00 USD | 0.00 USD | 3,940.00 USD | `-71.10%` | `15,622.00` |
| `Live` | `Long` | `0.2645` | 4,600,000.00 USD | 0.00 USD | 2,610.00 USD | `-69.72%` | `9,865.70` |
| `Live` | `Long` | `0.2685` | 4,600,000.00 USD | 0.00 USD | 106.16 USD | `-69.27%` | `395.40` |
| `Live` | `Long` | `0.2725` | 4,600,000.00 USD | 0.00 USD | 1,910.00 USD | `-68.81%` | `7,000.00` |
| `Live` | `Long` | `0.2735` | 4,590,000.00 USD | 0.00 USD | 248.34 USD | `-68.69%` | `908.00` |
| `Live` | `Long` | `0.2755` | 4,590,000.00 USD | 0.00 USD | 178.91 USD | `-68.47%` | `649.40` |
| `Live` | `Long` | `0.2785` | 4,590,000.00 USD | 0.00 USD | 3,630.00 USD | `-68.12%` | `13,023.80` |
| `Live` | `Long` | `0.2795` | 4,590,000.00 USD | 0.00 USD | 24,070.00 USD | `-68.01%` | `86,117.40` |
| `Live` | `Long` | `0.2885` | 4,570,000.00 USD | 0.00 USD | 29,070.00 USD | `-66.98%` | `100,768.40` |
| `Live` | `Long` | `0.2945` | 4,540,000.00 USD | 0.00 USD | 687.92 USD | `-66.29%` | `2,335.90` |
| `Live` | `Long` | `0.2965` | 4,540,000.00 USD | 0.00 USD | 593.12 USD | `-66.06%` | `2,000.40` |
| `Live` | `Long` | `0.2975` | 4,540,000.00 USD | 0.00 USD | 4,330.00 USD | `-65.95%` | `14,561.30` |
| `Live` | `Long` | `0.3035` | 4,530,000.00 USD | 0.00 USD | 124.25 USD | `-65.26%` | `409.40` |
| `Live` | `Long` | `0.3115` | 4,530,000.00 USD | 0.00 USD | 373.46 USD | `-64.34%` | `1,198.90` |
| `Live` | `Long` | `0.3155` | 4,530,000.00 USD | 0.00 USD | 195.04 USD | `-63.89%` | `618.20` |
| `Live` | `Long` | `0.3245` | 4,530,000.00 USD | 0.00 USD | 202.81 USD | `-62.86%` | `625.00` |
| `Live` | `Long` | `0.3415` | 4,530,000.00 USD | 0.00 USD | 203.91 USD | `-60.91%` | `597.10` |
| `Live` | `Long` | `0.3445` | 4,530,000.00 USD | 0.00 USD | 103.35 USD | `-60.57%` | `300.00` |
| `Live` | `Long` | `0.3455` | 4,530,000.00 USD | 0.00 USD | 338.66 USD | `-60.45%` | `980.20` |
| `Live` | `Long` | `0.3465` | 4,530,000.00 USD | 0.00 USD | 3,470.00 USD | `-60.34%` | `10,000.00` |
| `Live` | `Long` | `0.3505` | 4,530,000.00 USD | 0.00 USD | 1,020.00 USD | `-59.88%` | `2,908.00` |
| `Live` | `Long` | `0.3585` | 4,530,000.00 USD | 0.00 USD | 28,450.00 USD | `-58.97%` | `79,368.10` |
| `Live` | `Long` | `0.3665` | 4,500,000.00 USD | 0.00 USD | 274.88 USD | `-58.05%` | `750.00` |
| `Live` | `Long` | `0.3685` | 4,500,000.00 USD | 0.00 USD | 2,940.00 USD | `-57.82%` | `7,985.90` |
| `Live` | `Long` | `0.3705` | 4,490,000.00 USD | 0.00 USD | 413.14 USD | `-57.59%` | `1,115.10` |
| `Live` | `Long` | `0.3725` | 4,490,000.00 USD | 0.00 USD | 4,260.00 USD | `-57.36%` | `11,446.70` |
| `Live` | `Long` | `0.3785` | 4,490,000.00 USD | 0.00 USD | 861.39 USD | `-56.68%` | `2,275.80` |
| `Live` | `Long` | `0.3795` | 4,490,000.00 USD | 0.00 USD | 278.02 USD | `-56.56%` | `732.60` |
| `Live` | `Long` | `0.3825` | 4,490,000.00 USD | 0.00 USD | 6,500.00 USD | `-56.22%` | `17,000.00` |
| `Live` | `Long` | `0.3845` | 4,480,000.00 USD | 0.00 USD | 1,750.00 USD | `-55.99%` | `4,562.20` |
| `Live` | `Long` | `0.3875` | 4,480,000.00 USD | 0.00 USD | 27,120.00 USD | `-55.65%` | `70,000.00` |
| `Live` | `Long` | `0.3895` | 4,450,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.42%` | `7,661.70` |
| `Live` | `Long` | `0.3905` | 4,450,000.00 USD | 0.00 USD | 191.54 USD | `-55.30%` | `490.50` |
| `Live` | `Long` | `0.3925` | 4,450,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.07%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,440,000.00 USD | 0.00 USD | 754.48 USD | `-54.84%` | `1,912.50` |
| `Live` | `Long` | `0.4035` | 4,440,000.00 USD | 0.00 USD | 935.03 USD | `-53.81%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,440,000.00 USD | 0.00 USD | 5,520.00 USD | `-53.70%` | `13,640.50` |
| `Live` | `Long` | `0.4055` | 4,440,000.00 USD | 0.00 USD | 735.13 USD | `-53.59%` | `1,812.90` |
| `Live` | `Long` | `0.4235` | 4,440,000.00 USD | 0.00 USD | 467.50 USD | `-51.53%` | `1,103.90` |
| `Live` | `Long` | `0.4295` | 4,440,000.00 USD | 0.00 USD | 300.65 USD | `-50.84%` | `700.00` |
| `Live` | `Long` | `0.4345` | 4,440,000.00 USD | 0.00 USD | 765.59 USD | `-50.27%` | `1,762.00` |
| `Live` | `Long` | `0.4385` | 4,440,000.00 USD | 0.00 USD | 122.91 USD | `-49.81%` | `280.30` |
| `Live` | `Long` | `0.4415` | 4,440,000.00 USD | 0.00 USD | 49,780.00 USD | `-49.46%` | `112,757.90` |
| `Live` | `Long` | `0.4435` | 4,390,000.00 USD | 0.00 USD | 10,840.00 USD | `-49.24%` | `24,432.10` |
| `Live` | `Long` | `0.4455` | 4,370,000.00 USD | 0.00 USD | 574.83 USD | `-49.01%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,370,000.00 USD | 0.00 USD | 19,600.00 USD | `-48.89%` | `43,906.00` |
| `Live` | `Long` | `0.4525` | 4,350,000.00 USD | 0.00 USD | 5,660.00 USD | `-48.21%` | `12,500.00` |
| `Live` | `Long` | `0.4535` | 4,350,000.00 USD | 0.00 USD | 702.74 USD | `-48.09%` | `1,549.60` |
| `Live` | `Long` | `0.4595` | 4,350,000.00 USD | 0.00 USD | 295.78 USD | `-47.40%` | `643.70` |
| `Live` | `Long` | `0.4755` | 4,350,000.00 USD | 0.00 USD | 500.27 USD | `-45.57%` | `1,052.10` |
| `Live` | `Long` | `0.4785` | 4,350,000.00 USD | 0.00 USD | 110.10 USD | `-45.23%` | `230.10` |
| `Live` | `Long` | `0.4835` | 4,350,000.00 USD | 0.00 USD | 174.01 USD | `-44.66%` | `359.90` |
| `Live` | `Long` | `0.4865` | 4,350,000.00 USD | 0.00 USD | 201.07 USD | `-44.31%` | `413.30` |
| `Live` | `Long` | `0.4885` | 4,350,000.00 USD | 0.00 USD | 6,570.00 USD | `-44.09%` | `13,442.10` |
| `Live` | `Long` | `0.4895` | 4,340,000.00 USD | 0.00 USD | 646.73 USD | `-43.97%` | `1,321.20` |
| `Live` | `Long` | `0.4915` | 4,340,000.00 USD | 0.00 USD | 3,370.00 USD | `-43.74%` | `6,848.70` |
| `Live` | `Long` | `0.4935` | 4,340,000.00 USD | 0.00 USD | 1,500.00 USD | `-43.51%` | `3,043.40` |
| `Live` | `Long` | `0.4945` | 4,330,000.00 USD | 0.00 USD | 3,820.00 USD | `-43.40%` | `7,724.00` |
| `Live` | `Long` | `0.4955` | 4,330,000.00 USD | 0.00 USD | 211.88 USD | `-43.28%` | `427.60` |
| `Live` | `Long` | `0.4965` | 4,330,000.00 USD | 0.00 USD | 259.97 USD | `-43.17%` | `523.60` |
| `Live` | `Long` | `0.4985` | 4,330,000.00 USD | 0.00 USD | 216.75 USD | `-42.94%` | `434.80` |
| `Live` | `Long` | `0.5015` | 4,330,000.00 USD | 0.00 USD | 212.49 USD | `-42.60%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,330,000.00 USD | 0.00 USD | 1,330.00 USD | `-42.48%` | `2,652.40` |
| `Live` | `Long` | `0.5055` | 4,330,000.00 USD | 0.00 USD | 211.25 USD | `-42.14%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,330,000.00 USD | 0.00 USD | 2,540.00 USD | `-41.80%` | `5,000.00` |
| `Live` | `Long` | `0.5095` | 4,330,000.00 USD | 0.00 USD | 195.75 USD | `-41.68%` | `384.20` |
| `Live` | `Long` | `0.5155` | 4,330,000.00 USD | 0.00 USD | 1,240.00 USD | `-40.99%` | `2,409.50` |
| `Live` | `Long` | `0.5165` | 4,320,000.00 USD | 0.00 USD | 15,330.00 USD | `-40.88%` | `29,690.00` |
| `Live` | `Long` | `0.5175` | 4,310,000.00 USD | 0.00 USD | 213.68 USD | `-40.77%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,310,000.00 USD | 0.00 USD | 121.74 USD | `-40.65%` | `234.80` |
| `Live` | `Long` | `0.5205` | 4,310,000.00 USD | 0.00 USD | 864.13 USD | `-40.42%` | `1,660.20` |
| `Live` | `Long` | `0.5245` | 4,310,000.00 USD | 0.00 USD | 5,280.00 USD | `-39.96%` | `10,075.20` |
| `Live` | `Long` | `0.5255` | 4,300,000.00 USD | 0.00 USD | 31,530.00 USD | `-39.85%` | `60,000.00` |
| `Live` | `Long` | `0.5275` | 4,270,000.00 USD | 0.00 USD | 348.36 USD | `-39.62%` | `660.40` |
| `Live` | `Long` | `0.5285` | 4,270,000.00 USD | 0.00 USD | 2,590.00 USD | `-39.51%` | `4,897.40` |
| `Live` | `Long` | `0.5295` | 4,270,000.00 USD | 0.00 USD | 123,640.00 USD | `-39.39%` | `233,498.70` |
| `Live` | `Long` | `0.5325` | 4,140,000.00 USD | 0.00 USD | 2,680.00 USD | `-39.05%` | `5,038.10` |
| `Live` | `Long` | `0.5345` | 4,140,000.00 USD | 0.00 USD | 417.12 USD | `-38.82%` | `780.40` |
| `Live` | `Long` | `0.5365` | 4,140,000.00 USD | 0.00 USD | 131.55 USD | `-38.59%` | `245.20` |
| `Live` | `Long` | `0.5375` | 4,140,000.00 USD | 0.00 USD | 7,850.00 USD | `-38.48%` | `14,603.90` |
| `Live` | `Long` | `0.5395` | 4,130,000.00 USD | 0.00 USD | 319.98 USD | `-38.25%` | `593.10` |
| `Live` | `Long` | `0.5405` | 4,130,000.00 USD | 0.00 USD | 7,090.00 USD | `-38.13%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,130,000.00 USD | 0.00 USD | 269.13 USD | `-37.90%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,130,000.00 USD | 0.00 USD | 230.32 USD | `-37.68%` | `423.00` |
| `Live` | `Long` | `0.5455` | 4,130,000.00 USD | 0.00 USD | 5,930.00 USD | `-37.56%` | `10,862.70` |
| `Live` | `Long` | `0.5465` | 4,120,000.00 USD | 0.00 USD | 272.87 USD | `-37.45%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,120,000.00 USD | 0.00 USD | 1,240.00 USD | `-37.33%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,120,000.00 USD | 0.00 USD | 28,790.00 USD | `-37.10%` | `52,392.10` |
| `Live` | `Long` | `0.5505` | 4,090,000.00 USD | 0.00 USD | 248.06 USD | `-36.99%` | `450.60` |
| `Live` | `Long` | `0.5515` | 4,090,000.00 USD | 0.00 USD | 160.93 USD | `-36.87%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,090,000.00 USD | 0.00 USD | 582.56 USD | `-36.76%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,090,000.00 USD | 0.00 USD | 271.88 USD | `-36.65%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,090,000.00 USD | 0.00 USD | 531.60 USD | `-36.53%` | `958.70` |
| `Live` | `Long` | `0.5555` | 4,090,000.00 USD | 0.00 USD | 7,950.00 USD | `-36.42%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,080,000.00 USD | 0.00 USD | 141.97 USD | `-36.07%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,080,000.00 USD | 0.00 USD | 304.93 USD | `-35.96%` | `545.00` |
| `Live` | `Long` | `0.5605` | 4,080,000.00 USD | 0.00 USD | 441.84 USD | `-35.84%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,080,000.00 USD | 0.00 USD | 18,470.00 USD | `-35.61%` | `32,832.10` |
| `Live` | `Long` | `0.5635` | 4,060,000.00 USD | 0.00 USD | 195.93 USD | `-35.50%` | `347.70` |
| `Live` | `Long` | `0.5655` | 4,060,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.27%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,050,000.00 USD | 0.00 USD | 570.01 USD | `-35.16%` | `1,006.20` |
| `Live` | `Long` | `0.5675` | 4,050,000.00 USD | 0.00 USD | 1,560.00 USD | `-35.04%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,050,000.00 USD | 0.00 USD | 973.22 USD | `-34.81%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,050,000.00 USD | 0.00 USD | 139.23 USD | `-34.47%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,050,000.00 USD | 0.00 USD | 182.72 USD | `-34.36%` | `318.60` |
| `Live` | `Long` | `0.5745` | 4,050,000.00 USD | 0.00 USD | 144.03 USD | `-34.24%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,050,000.00 USD | 0.00 USD | 1,010.00 USD | `-34.13%` | `1,759.90` |
| `Live` | `Long` | `0.5765` | 4,050,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.01%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,050,000.00 USD | 0.00 USD | 497.75 USD | `-33.90%` | `861.90` |
| `Live` | `Long` | `0.5785` | 4,050,000.00 USD | 0.00 USD | 119.34 USD | `-33.78%` | `206.30` |
| `Live` | `Long` | `0.5795` | 4,050,000.00 USD | 0.00 USD | 212.85 USD | `-33.67%` | `367.30` |
| `Live` | `Long` | `0.5805` | 4,050,000.00 USD | 0.00 USD | 1,410.00 USD | `-33.55%` | `2,422.00` |
| `Live` | `Long` | `0.5825` | 4,040,000.00 USD | 0.00 USD | 6,470.00 USD | `-33.33%` | `11,099.00` |
| `Live` | `Long` | `0.5835` | 4,040,000.00 USD | 0.00 USD | 1,750.00 USD | `-33.21%` | `3,000.00` |
| `Live` | `Long` | `0.5855` | 4,040,000.00 USD | 0.00 USD | 2,640.00 USD | `-32.98%` | `4,508.30` |
| `Live` | `Long` | `0.5865` | 4,030,000.00 USD | 0.00 USD | 466.85 USD | `-32.87%` | `796.00` |
| `Live` | `Long` | `0.5875` | 4,030,000.00 USD | 0.00 USD | 969.32 USD | `-32.75%` | `1,649.90` |
| `Live` | `Long` | `0.5885` | 4,030,000.00 USD | 0.00 USD | 311.14 USD | `-32.64%` | `528.70` |
| `Live` | `Long` | `0.5925` | 4,030,000.00 USD | 0.00 USD | 994.16 USD | `-32.18%` | `1,677.90` |
| `Live` | `Long` | `0.5935` | 4,030,000.00 USD | 0.00 USD | 132.41 USD | `-32.07%` | `223.10` |
| `Live` | `Long` | `0.5945` | 4,030,000.00 USD | 0.00 USD | 8,600.00 USD | `-31.95%` | `14,462.30` |
| `Live` | `Long` | `0.5965` | 4,020,000.00 USD | 0.00 USD | 5,540.00 USD | `-31.72%` | `9,295.80` |
| `Live` | `Long` | `0.5995` | 4,020,000.00 USD | 0.00 USD | 151.97 USD | `-31.38%` | `253.50` |
| `Live` | `Long` | `0.6005` | 4,020,000.00 USD | 0.00 USD | 6,840.00 USD | `-31.27%` | `11,390.00` |
| `Live` | `Long` | `0.6025` | 4,010,000.00 USD | 0.00 USD | 432.35 USD | `-31.04%` | `717.60` |
| `Live` | `Long` | `0.6055` | 4,010,000.00 USD | 0.00 USD | 238.51 USD | `-30.69%` | `393.90` |
| `Live` | `Long` | `0.6075` | 4,010,000.00 USD | 0.00 USD | 851.05 USD | `-30.46%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 4,010,000.00 USD | 0.00 USD | 272.24 USD | `-30.35%` | `447.40` |
| `Live` | `Long` | `0.6105` | 4,010,000.00 USD | 0.00 USD | 2,750.00 USD | `-30.12%` | `4,500.00` |
| `Live` | `Long` | `0.6115` | 4,000,000.00 USD | 0.00 USD | 6,780.00 USD | `-30.01%` | `11,093.80` |
| `Live` | `Long` | `0.6125` | 4,000,000.00 USD | 0.00 USD | 768.01 USD | `-29.89%` | `1,253.90` |
| `Live` | `Long` | `0.6135` | 4,000,000.00 USD | 0.00 USD | 245.40 USD | `-29.78%` | `400.00` |
| `Live` | `Long` | `0.6145` | 4,000,000.00 USD | 0.00 USD | 3,430.00 USD | `-29.66%` | `5,579.50` |
| `Live` | `Long` | `0.6155` | 3,990,000.00 USD | 0.00 USD | 935.13 USD | `-29.55%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 3,990,000.00 USD | 0.00 USD | 29,900.00 USD | `-29.43%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 3,960,000.00 USD | 0.00 USD | 2,600.00 USD | `-29.32%` | `4,205.30` |
| `Live` | `Long` | `0.6185` | 3,960,000.00 USD | 0.00 USD | 4,400.00 USD | `-29.21%` | `7,107.00` |
| `Live` | `Long` | `0.6195` | 3,960,000.00 USD | 0.00 USD | 1,050.00 USD | `-29.09%` | `1,700.60` |
| `Live` | `Long` | `0.6215` | 3,950,000.00 USD | 0.00 USD | 8,420.00 USD | `-28.86%` | `13,552.00` |
| `Live` | `Long` | `0.6245` | 3,950,000.00 USD | 0.00 USD | 619.32 USD | `-28.52%` | `991.70` |
| `Live` | `Long` | `0.6255` | 3,950,000.00 USD | 0.00 USD | 32,070.00 USD | `-28.40%` | `51,265.70` |
| `Live` | `Long` | `0.6285` | 3,910,000.00 USD | 0.00 USD | 102.45 USD | `-28.06%` | `163.00` |
| `Live` | `Long` | `0.6305` | 3,910,000.00 USD | 0.00 USD | 319.35 USD | `-27.83%` | `506.50` |
| `Live` | `Long` | `0.6315` | 3,910,000.00 USD | 0.00 USD | 13,570.00 USD | `-27.72%` | `21,483.80` |
| `Live` | `Long` | `0.6335` | 3,900,000.00 USD | 0.00 USD | 16,340.00 USD | `-27.49%` | `25,791.20` |
| `Live` | `Long` | `0.6345` | 3,880,000.00 USD | 0.00 USD | 450.05 USD | `-27.37%` | `709.30` |
| `Live` | `Long` | `0.6365` | 3,880,000.00 USD | 0.00 USD | 3,060.00 USD | `-27.14%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,880,000.00 USD | 0.00 USD | 130.62 USD | `-27.03%` | `204.90` |
| `Live` | `Long` | `0.6395` | 3,880,000.00 USD | 0.00 USD | 244.03 USD | `-26.80%` | `381.60` |
| `Live` | `Long` | `0.6405` | 3,880,000.00 USD | 0.00 USD | 939.17 USD | `-26.69%` | `1,466.30` |
| `Live` | `Long` | `0.6415` | 3,880,000.00 USD | 0.00 USD | 86,920.00 USD | `-26.57%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,790,000.00 USD | 0.00 USD | 1,260.00 USD | `-26.46%` | `1,956.60` |
| `Live` | `Long` | `0.6435` | 3,790,000.00 USD | 0.00 USD | 657.79 USD | `-26.34%` | `1,022.20` |
| `Live` | `Long` | `0.6445` | 3,790,000.00 USD | 0.00 USD | 65,790.00 USD | `-26.23%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,720,000.00 USD | 0.00 USD | 14,370.00 USD | `-26.11%` | `22,268.90` |
| `Live` | `Long` | `0.6465` | 3,710,000.00 USD | 0.00 USD | 146.76 USD | `-26.00%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,710,000.00 USD | 0.00 USD | 8,240.00 USD | `-25.89%` | `12,723.20` |
| `Live` | `Long` | `0.6485` | 3,700,000.00 USD | 0.00 USD | 668.34 USD | `-25.77%` | `1,030.60` |
| `Live` | `Long` | `0.6495` | 3,700,000.00 USD | 0.00 USD | 325,470.00 USD | `-25.66%` | `501,111.00` |
| `Live` | `Long` | `0.6505` | 3,370,000.00 USD | 0.00 USD | 631.12 USD | `-25.54%` | `970.20` |
| `Live` | `Long` | `0.6515` | 3,370,000.00 USD | 0.00 USD | 403,320.00 USD | `-25.43%` | `619,065.10` |
| `Live` | `Long` | `0.6535` | 2,970,000.00 USD | 0.00 USD | 126,530.00 USD | `-25.20%` | `193,618.10` |
| `Live` | `Long` | `0.6545` | 2,840,000.00 USD | 0.00 USD | 1,150.00 USD | `-25.08%` | `1,761.60` |
| `Live` | `Long` | `0.6555` | 2,840,000.00 USD | 0.00 USD | 1,170.00 USD | `-24.97%` | `1,777.80` |
| `Live` | `Long` | `0.6565` | 2,840,000.00 USD | 0.00 USD | 8,270.00 USD | `-24.86%` | `12,591.20` |
| `Live` | `Long` | `0.6575` | 2,830,000.00 USD | 0.00 USD | 13,280.00 USD | `-24.74%` | `20,198.10` |
| `Live` | `Long` | `0.6585` | 2,820,000.00 USD | 0.00 USD | 2,970.00 USD | `-24.63%` | `4,508.30` |
| `Live` | `Long` | `0.6595` | 2,820,000.00 USD | 0.00 USD | 329.75 USD | `-24.51%` | `500.00` |
| `Live` | `Long` | `0.6615` | 2,820,000.00 USD | 0.00 USD | 126,890.00 USD | `-24.28%` | `191,817.10` |
| `Live` | `Long` | `0.6625` | 2,690,000.00 USD | 0.00 USD | 788.97 USD | `-24.17%` | `1,190.90` |
| `Live` | `Long` | `0.6645` | 2,690,000.00 USD | 0.00 USD | 448.54 USD | `-23.94%` | `675.00` |
| `Live` | `Long` | `0.6675` | 2,690,000.00 USD | 0.00 USD | 5,280.00 USD | `-23.60%` | `7,907.60` |
| `Live` | `Long` | `0.6685` | 2,680,000.00 USD | 0.00 USD | 2,810.00 USD | `-23.48%` | `4,203.00` |
| `Live` | `Long` | `0.6705` | 2,680,000.00 USD | 0.00 USD | 2,290.00 USD | `-23.25%` | `3,411.50` |
| `Live` | `Long` | `0.6715` | 2,680,000.00 USD | 0.00 USD | 8,500.00 USD | `-23.14%` | `12,661.20` |
| `Live` | `Long` | `0.6725` | 2,670,000.00 USD | 0.00 USD | 1,450.00 USD | `-23.02%` | `2,162.40` |
| `Live` | `Long` | `0.6735` | 2,670,000.00 USD | 0.00 USD | 27,680.00 USD | `-22.91%` | `41,094.80` |
| `Live` | `Long` | `0.6745` | 2,640,000.00 USD | 0.00 USD | 6,520.00 USD | `-22.80%` | `9,673.20` |
| `Live` | `Long` | `0.6755` | 2,630,000.00 USD | 0.00 USD | 111.59 USD | `-22.68%` | `165.20` |
| `Live` | `Long` | `0.6765` | 2,630,000.00 USD | 0.00 USD | 1,040.00 USD | `-22.57%` | `1,539.20` |
| `Live` | `Long` | `0.6785` | 2,630,000.00 USD | 0.00 USD | 250.77 USD | `-22.34%` | `369.60` |
| `Live` | `Long` | `0.6795` | 2,630,000.00 USD | 0.00 USD | 5,620.00 USD | `-22.22%` | `8,270.70` |
| `Live` | `Long` | `0.6805` | 2,630,000.00 USD | 0.00 USD | 1,600.00 USD | `-22.11%` | `2,348.00` |
| `Live` | `Long` | `0.6815` | 2,630,000.00 USD | 0.00 USD | 3,380.00 USD | `-21.99%` | `4,954.70` |
| `Live` | `Long` | `0.6825` | 2,620,000.00 USD | 0.00 USD | 15,920.00 USD | `-21.88%` | `23,330.00` |
| `Live` | `Long` | `0.6835` | 2,610,000.00 USD | 0.00 USD | 11,170.00 USD | `-21.77%` | `16,336.60` |
| `Live` | `Long` | `0.6845` | 2,600,000.00 USD | 0.00 USD | 5,790.00 USD | `-21.65%` | `8,455.80` |
| `Live` | `Long` | `0.6875` | 2,590,000.00 USD | 0.00 USD | 2,380.00 USD | `-21.31%` | `3,458.70` |
| `Live` | `Long` | `0.6885` | 2,590,000.00 USD | 0.00 USD | 83,790.00 USD | `-21.19%` | `121,695.30` |
| `Live` | `Long` | `0.6895` | 2,500,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.08%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,500,000.00 USD | 0.00 USD | 3,360.00 USD | `-20.96%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,500,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.85%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 2,490,000.00 USD | 0.00 USD | 2,980.00 USD | `-20.62%` | `4,299.80` |
| `Live` | `Long` | `0.6945` | 2,490,000.00 USD | 0.00 USD | 722.28 USD | `-20.51%` | `1,040.00` |
| `Live` | `Long` | `0.6965` | 2,490,000.00 USD | 0.00 USD | 704.37 USD | `-20.28%` | `1,011.30` |
| `Live` | `Long` | `0.6975` | 2,480,000.00 USD | 0.00 USD | 2,400.00 USD | `-20.16%` | `3,440.40` |
| `Live` | `Long` | `0.6985` | 2,480,000.00 USD | 0.00 USD | 1,930.00 USD | `-20.05%` | `2,759.10` |
| `Live` | `Long` | `0.6995` | 2,480,000.00 USD | 0.00 USD | 879.97 USD | `-19.93%` | `1,258.00` |
| `Live` | `Long` | `0.7015` | 2,480,000.00 USD | 0.00 USD | 383.72 USD | `-19.70%` | `547.00` |
| `Live` | `Long` | `0.7045` | 2,480,000.00 USD | 0.00 USD | 759.59 USD | `-19.36%` | `1,078.20` |
| `Live` | `Long` | `0.7055` | 2,480,000.00 USD | 0.00 USD | 115.00 USD | `-19.25%` | `163.00` |
| `Live` | `Long` | `0.7065` | 2,480,000.00 USD | 0.00 USD | 769.59 USD | `-19.13%` | `1,089.30` |
| `Live` | `Long` | `0.7075` | 2,480,000.00 USD | 0.00 USD | 787.73 USD | `-19.02%` | `1,113.40` |
| `Live` | `Long` | `0.7085` | 2,480,000.00 USD | 0.00 USD | 3,890.00 USD | `-18.90%` | `5,484.60` |
| `Live` | `Long` | `0.7095` | 2,470,000.00 USD | 0.00 USD | 2,720.00 USD | `-18.79%` | `3,833.70` |
| `Live` | `Long` | `0.7105` | 2,470,000.00 USD | 0.00 USD | 3,530.00 USD | `-18.67%` | `4,964.90` |
| `Live` | `Long` | `0.7115` | 2,470,000.00 USD | 0.00 USD | 4,090.00 USD | `-18.56%` | `5,749.90` |
| `Live` | `Long` | `0.7125` | 2,460,000.00 USD | 0.00 USD | 156.39 USD | `-18.45%` | `219.50` |
| `Live` | `Long` | `0.7175` | 2,460,000.00 USD | 0.00 USD | 8,820.00 USD | `-17.87%` | `12,295.90` |
| `Live` | `Long` | `0.7195` | 2,450,000.00 USD | 0.00 USD | 11,720.00 USD | `-17.64%` | `16,293.90` |
| `Live` | `Long` | `0.7205` | 2,440,000.00 USD | 0.00 USD | 120.54 USD | `-17.53%` | `167.30` |
| `Live` | `Long` | `0.7225` | 2,440,000.00 USD | 0.00 USD | 652.13 USD | `-17.30%` | `902.60` |
| `Live` | `Long` | `0.7255` | 2,440,000.00 USD | 0.00 USD | 2,660.00 USD | `-16.96%` | `3,662.80` |
| `Live` | `Long` | `0.7265` | 2,440,000.00 USD | 0.00 USD | 1,060.00 USD | `-16.84%` | `1,453.70` |
| `Live` | `Long` | `0.7275` | 2,440,000.00 USD | 0.00 USD | 762.57 USD | `-16.73%` | `1,048.20` |
| `Live` | `Long` | `0.7285` | 2,440,000.00 USD | 0.00 USD | 214.03 USD | `-16.61%` | `293.80` |
| `Live` | `Long` | `0.7295` | 2,440,000.00 USD | 0.00 USD | 375.98 USD | `-16.50%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,440,000.00 USD | 0.00 USD | 119.88 USD | `-16.39%` | `164.10` |
| `Live` | `Long` | `0.7315` | 2,440,000.00 USD | 0.00 USD | 31,890.00 USD | `-16.27%` | `43,601.40` |
| `Live` | `Long` | `0.7325` | 2,400,000.00 USD | 0.00 USD | 907.93 USD | `-16.16%` | `1,239.50` |
| `Live` | `Long` | `0.7345` | 2,400,000.00 USD | 0.00 USD | 2,340.00 USD | `-15.93%` | `3,185.40` |
| `Live` | `Long` | `0.7355` | 2,400,000.00 USD | 0.00 USD | 51,920.00 USD | `-15.81%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 2,350,000.00 USD | 0.00 USD | 6,900.00 USD | `-15.70%` | `9,366.00` |
| `Live` | `Long` | `0.7375` | 2,340,000.00 USD | 0.00 USD | 203.11 USD | `-15.58%` | `275.40` |
| `Live` | `Long` | `0.7385` | 2,340,000.00 USD | 0.00 USD | 5,940.00 USD | `-15.47%` | `8,037.10` |
| `Live` | `Long` | `0.7405` | 2,340,000.00 USD | 0.00 USD | 3,530.00 USD | `-15.24%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,330,000.00 USD | 0.00 USD | 382.61 USD | `-15.13%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,330,000.00 USD | 0.00 USD | 784,090.00 USD | `-15.01%` | `1,056,015.30` |
| `Live` | `Long` | `0.7445` | 1,550,000.00 USD | 0.00 USD | 105.64 USD | `-14.78%` | `141.90` |
| `Live` | `Long` | `0.7455` | 1,550,000.00 USD | 0.00 USD | 1,990.00 USD | `-14.67%` | `2,666.60` |
| `Live` | `Long` | `0.7475` | 1,550,000.00 USD | 0.00 USD | 103,310.00 USD | `-14.44%` | `138,200.90` |
| `Live` | `Long` | `0.7485` | 1,440,000.00 USD | 0.00 USD | 105.91 USD | `-14.32%` | `141.50` |
| `Live` | `Long` | `0.7495` | 1,440,000.00 USD | 0.00 USD | 599.60 USD | `-14.21%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,440,000.00 USD | 0.00 USD | 1,210.00 USD | `-13.98%` | `1,613.50` |
| `Live` | `Long` | `0.7525` | 1,440,000.00 USD | 0.00 USD | 106.03 USD | `-13.87%` | `140.90` |
| `Live` | `Long` | `0.7535` | 1,440,000.00 USD | 0.00 USD | 2,020.00 USD | `-13.75%` | `2,674.80` |
| `Live` | `Long` | `0.7545` | 1,440,000.00 USD | 0.00 USD | 16,010.00 USD | `-13.64%` | `21,222.10` |
| `Live` | `Long` | `0.7575` | 1,420,000.00 USD | 0.00 USD | 1,900.00 USD | `-13.29%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,420,000.00 USD | 0.00 USD | 36,710.00 USD | `-13.18%` | `48,399.00` |
| `Live` | `Long` | `0.7595` | 1,380,000.00 USD | 0.00 USD | 4,500.00 USD | `-13.07%` | `5,928.80` |
| `Live` | `Long` | `0.7615` | 1,380,000.00 USD | 0.00 USD | 351.43 USD | `-12.84%` | `461.50` |
| `Live` | `Long` | `0.7635` | 1,380,000.00 USD | 0.00 USD | 5,110.00 USD | `-12.61%` | `6,696.30` |
| `Live` | `Long` | `0.7645` | 1,370,000.00 USD | 0.00 USD | 3,510.00 USD | `-12.49%` | `4,596.60` |
| `Live` | `Long` | `0.7655` | 1,370,000.00 USD | 0.00 USD | 320,960.00 USD | `-12.38%` | `419,277.50` |
| `Live` | `Long` | `0.7665` | 1,050,000.00 USD | 0.00 USD | 1,260.00 USD | `-12.26%` | `1,649.10` |
| `Live` | `Long` | `0.7675` | 1,050,000.00 USD | 0.00 USD | 10,510.00 USD | `-12.15%` | `13,688.30` |
| `Live` | `Long` | `0.7685` | 1,040,000.00 USD | 0.00 USD | 499.99 USD | `-12.04%` | `650.60` |
| `Live` | `Long` | `0.7695` | 1,040,000.00 USD | 0.00 USD | 144,250.00 USD | `-11.92%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 892,380.00 USD | 0.00 USD | 13,980.00 USD | `-11.81%` | `18,144.90` |
| `Live` | `Long` | `0.7715` | 878,400.00 USD | 0.00 USD | 338.38 USD | `-11.69%` | `438.60` |
| `Live` | `Long` | `0.7725` | 878,060.00 USD | 0.00 USD | 2,360.00 USD | `-11.58%` | `3,051.60` |
| `Live` | `Long` | `0.7735` | 875,710.00 USD | 0.00 USD | 4,570.00 USD | `-11.46%` | `5,912.10` |
| `Live` | `Long` | `0.7765` | 871,130.00 USD | 0.00 USD | 4,630.00 USD | `-11.12%` | `5,964.40` |
| `Live` | `Long` | `0.7785` | 866,500.00 USD | 0.00 USD | 7,000.00 USD | `-10.89%` | `8,985.30` |
| `Live` | `Long` | `0.7795` | 859,510.00 USD | 0.00 USD | 338.69 USD | `-10.78%` | `434.50` |
| `Live` | `Long` | `0.7815` | 859,170.00 USD | 0.00 USD | 4,160.00 USD | `-10.55%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 855,010.00 USD | 0.00 USD | 1,060.00 USD | `-10.32%` | `1,349.40` |
| `Live` | `Long` | `0.7855` | 853,950.00 USD | 0.00 USD | 3,020.00 USD | `-10.09%` | `3,840.20` |
| `Live` | `Long` | `0.7865` | 850,930.00 USD | 0.00 USD | 2,870.00 USD | `-9.98%` | `3,651.90` |
| `Live` | `Long` | `0.7875` | 848,060.00 USD | 0.00 USD | 15,190.00 USD | `-9.86%` | `19,293.30` |
| `Live` | `Long` | `0.7895` | 832,870.00 USD | 0.00 USD | 44,370.00 USD | `-9.63%` | `56,205.30` |
| `Live` | `Long` | `0.7905` | 788,490.00 USD | 0.00 USD | 3,670.00 USD | `-9.52%` | `4,637.40` |
| `Live` | `Long` | `0.7915` | 784,830.00 USD | 0.00 USD | 1,290.00 USD | `-9.40%` | `1,623.50` |
| `Live` | `Long` | `0.7925` | 783,540.00 USD | 0.00 USD | 385.87 USD | `-9.29%` | `486.90` |
| `Live` | `Long` | `0.7945` | 783,160.00 USD | 0.00 USD | 9,190.00 USD | `-9.06%` | `11,570.20` |
| `Live` | `Long` | `0.7955` | 773,960.00 USD | 0.00 USD | 23,720.00 USD | `-8.95%` | `29,814.10` |
| `Live` | `Long` | `0.7975` | 750,250.00 USD | 0.00 USD | 1,170.00 USD | `-8.72%` | `1,464.30` |
| `Live` | `Long` | `0.7985` | 749,080.00 USD | 0.00 USD | 1,840.00 USD | `-8.60%` | `2,300.00` |
| `Live` | `Long` | `0.7995` | 747,240.00 USD | 0.00 USD | 2,580.00 USD | `-8.49%` | `3,228.10` |
| `Live` | `Long` | `0.8005` | 744,660.00 USD | 0.00 USD | 635.04 USD | `-8.37%` | `793.30` |
| `Live` | `Long` | `0.8015` | 744,030.00 USD | 0.00 USD | 6,810.00 USD | `-8.26%` | `8,499.50` |
| `Live` | `Long` | `0.8035` | 737,210.00 USD | 0.00 USD | 316.42 USD | `-8.03%` | `393.80` |
| `Live` | `Long` | `0.8045` | 736,900.00 USD | 0.00 USD | 41,410.00 USD | `-7.92%` | `51,472.10` |
| `Live` | `Long` | `0.8055` | 695,490.00 USD | 0.00 USD | 1,610.00 USD | `-7.80%` | `2,000.00` |
| `Live` | `Long` | `0.8075` | 693,880.00 USD | 0.00 USD | 1,220.00 USD | `-7.57%` | `1,515.40` |
| `Live` | `Long` | `0.8085` | 692,650.00 USD | 0.00 USD | 22,460.00 USD | `-7.46%` | `27,784.20` |
| `Live` | `Long` | `0.8105` | 670,190.00 USD | 0.00 USD | 2,250.00 USD | `-7.23%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 667,940.00 USD | 0.00 USD | 3,050.00 USD | `-7.11%` | `3,753.20` |
| `Live` | `Long` | `0.8125` | 664,890.00 USD | 0.00 USD | 2,480.00 USD | `-7.00%` | `3,054.20` |
| `Live` | `Long` | `0.8135` | 662,410.00 USD | 0.00 USD | 11,260.00 USD | `-6.88%` | `13,843.50` |
| `Live` | `Long` | `0.8145` | 651,150.00 USD | 0.00 USD | 277.42 USD | `-6.77%` | `340.60` |
| `Live` | `Long` | `0.8155` | 650,870.00 USD | 0.00 USD | 8,160.00 USD | `-6.66%` | `10,000.00` |
| `Live` | `Long` | `0.8165` | 642,720.00 USD | 0.00 USD | 1,440.00 USD | `-6.54%` | `1,758.20` |
| `Live` | `Long` | `0.8175` | 641,280.00 USD | 0.00 USD | 103,450.00 USD | `-6.43%` | `126,546.30` |
| `Live` | `Long` | `0.8185` | 537,830.00 USD | 0.00 USD | 2,070.00 USD | `-6.31%` | `2,529.70` |
| `Live` | `Long` | `0.8195` | 535,760.00 USD | 0.00 USD | 29,980.00 USD | `-6.20%` | `36,587.30` |
| `Live` | `Long` | `0.8205` | 505,770.00 USD | 0.00 USD | 2,280.00 USD | `-6.08%` | `2,781.50` |
| `Live` | `Long` | `0.8215` | 503,490.00 USD | 0.00 USD | 6,900.00 USD | `-5.97%` | `8,399.30` |
| `Live` | `Long` | `0.8225` | 496,590.00 USD | 0.00 USD | 2,570.00 USD | `-5.85%` | `3,128.70` |
| `Live` | `Long` | `0.8235` | 494,020.00 USD | 0.00 USD | 216.00 USD | `-5.74%` | `262.30` |
| `Live` | `Long` | `0.8245` | 493,800.00 USD | 0.00 USD | 1,140.00 USD | `-5.63%` | `1,388.70` |
| `Live` | `Long` | `0.8255` | 492,660.00 USD | 0.00 USD | 4,550.00 USD | `-5.51%` | `5,515.80` |
| `Live` | `Long` | `0.8275` | 488,100.00 USD | 0.00 USD | 11,410.00 USD | `-5.28%` | `13,785.20` |
| `Live` | `Long` | `0.8285` | 476,700.00 USD | 0.00 USD | 126,740.00 USD | `-5.17%` | `152,975.80` |
| `Live` | `Long` | `0.8295` | 349,960.00 USD | 0.00 USD | 32,530.00 USD | `-5.05%` | `39,217.20` |
| `Live` | `Long` | `0.8305` | 317,430.00 USD | 0.00 USD | 1,880.00 USD | `-4.94%` | `2,268.50` |
| `Live` | `Long` | `0.8325` | 315,540.00 USD | 0.00 USD | 20,930.00 USD | `-4.71%` | `25,145.00` |
| `Live` | `Long` | `0.8335` | 294,610.00 USD | 0.00 USD | 234.71 USD | `-4.60%` | `281.60` |
| `Live` | `Long` | `0.8355` | 294,370.00 USD | 0.00 USD | 17,770.00 USD | `-4.37%` | `21,269.40` |
| `Live` | `Long` | `0.8375` | 276,600.00 USD | 0.00 USD | 2,420.00 USD | `-4.14%` | `2,888.90` |
| `Live` | `Long` | `0.8385` | 274,180.00 USD | 0.00 USD | 75,120.00 USD | `-4.02%` | `89,586.40` |
| `Live` | `Long` | `0.8395` | 199,070.00 USD | 0.00 USD | 26,770.00 USD | `-3.91%` | `31,885.00` |
| `Live` | `Long` | `0.8405` | 172,300.00 USD | 0.00 USD | 1,320.00 USD | `-3.79%` | `1,571.70` |
| `Live` | `Long` | `0.8415` | 170,980.00 USD | 0.00 USD | 48,540.00 USD | `-3.68%` | `57,683.50` |
| `Live` | `Long` | `0.8425` | 122,440.00 USD | 0.00 USD | 2,230.00 USD | `-3.57%` | `2,645.50` |
| `Live` | `Long` | `0.8435` | 120,210.00 USD | 0.00 USD | 6,280.00 USD | `-3.45%` | `7,446.40` |
| `Live` | `Long` | `0.8445` | 113,930.00 USD | 0.00 USD | 133.18 USD | `-3.34%` | `157.70` |
| `Live` | `Long` | `0.8455` | 113,790.00 USD | 0.00 USD | 6,340.00 USD | `-3.22%` | `7,494.00` |
| `Live` | `Long` | `0.8465` | 107,460.00 USD | 0.00 USD | 15,830.00 USD | `-3.11%` | `18,696.70` |
| `Live` | `Long` | `0.8475` | 91,630.00 USD | 0.00 USD | 28,990.00 USD | `-2.99%` | `34,202.20` |
| `Live` | `Long` | `0.8485` | 62,640.00 USD | 0.00 USD | 1,890.00 USD | `-2.88%` | `2,222.00` |
| `Live` | `Long` | `0.8495` | 60,760.00 USD | 0.00 USD | 5,290.00 USD | `-2.76%` | `6,230.00` |
| `Live` | `Long` | `0.8505` | 55,470.00 USD | 0.00 USD | 958.26 USD | `-2.65%` | `1,126.70` |
| `Live` | `Long` | `0.8515` | 54,510.00 USD | 0.00 USD | 1,220.00 USD | `-2.54%` | `1,433.90` |
| `Live` | `Long` | `0.8535` | 53,290.00 USD | 0.00 USD | 15,640.00 USD | `-2.31%` | `18,326.40` |
| `Live` | `Long` | `0.8555` | 37,650.00 USD | 0.00 USD | 17,220.00 USD | `-2.08%` | `20,123.80` |
| `Live` | `Long` | `0.8565` | 20,430.00 USD | 0.00 USD | 15,610.00 USD | `-1.96%` | `18,227.90` |
| `Live` | `Long` | `0.8585` | 4,820.00 USD | 0.00 USD | 2,200.00 USD | `-1.73%` | `2,567.10` |
| `Live` | `Long` | `0.8595` | 2,610.00 USD | 0.00 USD | 1,550.00 USD | `-1.62%` | `1,803.60` |
| `Live` | `Long` | `0.8685` | 1,060.00 USD | 0.00 USD | 265.76 USD | `-0.59%` | `306.00` |
| `Live` | `Long` | `0.8695` | 798.46 USD | 0.00 USD | 798.46 USD | `-0.48%` | `918.30` |
| `Live` | `Short` | `0.8935` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | `+2.27%` | `4,019.80` |
| `Live` | `Short` | `0.9025` | 4,410.00 USD | 818.48 USD | 0.00 USD | `+3.30%` | `906.90` |
| `Live` | `Short` | `0.9035` | 13,450.00 USD | 9,040.00 USD | 0.00 USD | `+3.42%` | `10,000.00` |
| `Live` | `Short` | `0.9045` | 13,640.00 USD | 191.39 USD | 0.00 USD | `+3.53%` | `211.60` |
| `Live` | `Short` | `0.9055` | 75,210.00 USD | 61,580.00 USD | 0.00 USD | `+3.65%` | `68,002.30` |
| `Live` | `Short` | `0.9075` | 75,930.00 USD | 717.74 USD | 0.00 USD | `+3.87%` | `790.90` |
| `Live` | `Short` | `0.9155` | 76,080.00 USD | 150.14 USD | 0.00 USD | `+4.79%` | `164.00` |
| `Live` | `Short` | `0.9195` | 112,220.00 USD | 36,140.00 USD | 0.00 USD | `+5.25%` | `39,300.80` |
| `Live` | `Short` | `0.9205` | 125,190.00 USD | 12,970.00 USD | 0.00 USD | `+5.36%` | `14,093.60` |
| `Live` | `Short` | `0.9215` | 127,280.00 USD | 2,090.00 USD | 0.00 USD | `+5.48%` | `2,265.40` |
| `Live` | `Short` | `0.9235` | 127,510.00 USD | 234.48 USD | 0.00 USD | `+5.71%` | `253.90` |
| `Live` | `Short` | `0.9245` | 131,900.00 USD | 4,390.00 USD | 0.00 USD | `+5.82%` | `4,744.30` |
| `Live` | `Short` | `0.9255` | 141,770.00 USD | 9,870.00 USD | 0.00 USD | `+5.93%` | `10,668.20` |
| `Live` | `Short` | `0.9265` | 149,040.00 USD | 7,270.00 USD | 0.00 USD | `+6.05%` | `7,843.80` |
| `Live` | `Short` | `0.9275` | 180,150.00 USD | 31,110.00 USD | 0.00 USD | `+6.16%` | `33,540.90` |
| `Live` | `Short` | `0.9285` | 181,500.00 USD | 1,360.00 USD | 0.00 USD | `+6.28%` | `1,460.00` |
| `Live` | `Short` | `0.9295` | 244,070.00 USD | 62,570.00 USD | 0.00 USD | `+6.39%` | `67,316.00` |
| `Live` | `Short` | `0.9305` | 247,900.00 USD | 3,830.00 USD | 0.00 USD | `+6.51%` | `4,111.50` |
| `Live` | `Short` | `0.9335` | 248,020.00 USD | 116.31 USD | 0.00 USD | `+6.85%` | `124.60` |
| `Live` | `Short` | `0.9345` | 250,120.00 USD | 2,100.00 USD | 0.00 USD | `+6.97%` | `2,252.30` |
| `Live` | `Short` | `0.9365` | 251,870.00 USD | 1,750.00 USD | 0.00 USD | `+7.19%` | `1,866.80` |
| `Live` | `Short` | `0.9675` | 255,030.00 USD | 3,160.00 USD | 0.00 USD | `+10.74%` | `3,266.70` |
| `Live` | `Short` | `0.9705` | 320,090.00 USD | 65,060.00 USD | 0.00 USD | `+11.09%` | `67,040.50` |
| `Live` | `Short` | `0.9765` | 320,310.00 USD | 214.44 USD | 0.00 USD | `+11.77%` | `219.60` |
| `Live` | `Short` | `0.9775` | 320,410.00 USD | 100.88 USD | 0.00 USD | `+11.89%` | `103.20` |
| `Live` | `Short` | `0.9805` | 321,460.00 USD | 1,050.00 USD | 0.00 USD | `+12.23%` | `1,068.70` |
| `Live` | `Short` | `0.9845` | 331,900.00 USD | 10,440.00 USD | 0.00 USD | `+12.69%` | `10,608.60` |
| `Live` | `Short` | `0.9875` | 332,630.00 USD | 732.03 USD | 0.00 USD | `+13.03%` | `741.30` |
| `Live` | `Short` | `0.9885` | 337,560.00 USD | 4,930.00 USD | 0.00 USD | `+13.15%` | `4,982.50` |
| `Live` | `Short` | `0.9905` | 339,130.00 USD | 1,570.00 USD | 0.00 USD | `+13.37%` | `1,586.00` |
| `Live` | `Short` | `0.9925` | 341,540.00 USD | 2,420.00 USD | 0.00 USD | `+13.60%` | `2,434.50` |
| `Live` | `Short` | `0.9965` | 341,670.00 USD | 125.66 USD | 0.00 USD | `+14.06%` | `126.10` |
| `Live` | `Short` | `1.02` | 341,840.00 USD | 170.40 USD | 0.00 USD | `+16.24%` | `167.80` |
| `Live` | `Short` | `1.04` | 342,000.00 USD | 155.92 USD | 0.00 USD | `+18.98%` | `150.00` |
| `Live` | `Short` | `1.04` | 342,140.00 USD | 139.22 USD | 0.00 USD | `+19.10%` | `133.80` |
| `Live` | `Short` | `1.05` | 342,730.00 USD | 597.52 USD | 0.00 USD | `+20.24%` | `568.80` |
| `Live` | `Short` | `1.05` | 345,120.00 USD | 2,390.00 USD | 0.00 USD | `+20.36%` | `2,272.10` |
| `Live` | `Short` | `1.05` | 345,440.00 USD | 317.52 USD | 0.00 USD | `+20.59%` | `301.40` |
| `Live` | `Short` | `1.06` | 345,660.00 USD | 217.64 USD | 0.00 USD | `+20.81%` | `206.20` |
| `Live` | `Short` | `1.08` | 349,350.00 USD | 3,690.00 USD | 0.00 USD | `+23.22%` | `3,432.40` |
| `Live` | `Short` | `1.08` | 355,050.00 USD | 5,700.00 USD | 0.00 USD | `+23.56%` | `5,278.70` |
| `Live` | `Short` | `1.08` | 358,630.00 USD | 3,580.00 USD | 0.00 USD | `+23.68%` | `3,315.70` |
| `Live` | `Short` | `1.08` | 358,800.00 USD | 166.43 USD | 0.00 USD | `+24.02%` | `153.60` |
| `Live` | `Short` | `1.09` | 364,350.00 USD | 5,550.00 USD | 0.00 USD | `+24.71%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 364,680.00 USD | 324.90 USD | 0.00 USD | `+25.85%` | `295.50` |
| `Live` | `Short` | `1.10` | 364,950.00 USD | 277.22 USD | 0.00 USD | `+25.97%` | `251.90` |
| `Live` | `Short` | `1.13` | 388,260.00 USD | 23,310.00 USD | 0.00 USD | `+28.94%` | `20,691.10` |
| `Live` | `Short` | `1.18` | 393,320.00 USD | 5,060.00 USD | 0.00 USD | `+35.47%` | `4,273.60` |
| `Live` | `Short` | `1.20` | 394,770.00 USD | 1,450.00 USD | 0.00 USD | `+37.07%` | `1,213.60` |
| `Live` | `Short` | `1.20` | 395,030.00 USD | 253.69 USD | 0.00 USD | `+37.30%` | `211.50` |
| `Live` | `Short` | `1.21` | 395,170.00 USD | 147.43 USD | 0.00 USD | `+37.98%` | `122.30` |
| `Live` | `Short` | `1.22` | 399,620.00 USD | 4,440.00 USD | 0.00 USD | `+39.47%` | `3,646.70` |
| `Live` | `Short` | `1.23` | 400,000.00 USD | 380.84 USD | 0.00 USD | `+41.30%` | `308.50` |
| `Live` | `Short` | `1.25` | 402,850.00 USD | 2,850.00 USD | 0.00 USD | `+43.25%` | `2,278.20` |
| `Live` | `Short` | `1.26` | 405,520.00 USD | 2,670.00 USD | 0.00 USD | `+44.17%` | `2,118.80` |
| `Live` | `Short` | `1.28` | 407,820.00 USD | 2,300.00 USD | 0.00 USD | `+46.23%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 447,710.00 USD | 39,880.00 USD | 0.00 USD | `+46.80%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 447,930.00 USD | 226.80 USD | 0.00 USD | `+48.17%` | `175.20` |
| `Live` | `Short` | `1.30` | 448,050.00 USD | 114.40 USD | 0.00 USD | `+48.63%` | `88.10` |
| `Live` | `Short` | `1.30` | 449,120.00 USD | 1,070.00 USD | 0.00 USD | `+48.86%` | `826.40` |
| `Live` | `Short` | `1.30` | 449,760.00 USD | 635.85 USD | 0.00 USD | `+49.20%` | `487.80` |
| `Live` | `Short` | `1.31` | 459,700.00 USD | 9,950.00 USD | 0.00 USD | `+49.43%` | `7,618.00` |
| `Live` | `Short` | `1.31` | 460,720.00 USD | 1,020.00 USD | 0.00 USD | `+49.89%` | `777.20` |
| `Live` | `Short` | `1.31` | 492,250.00 USD | 31,530.00 USD | 0.00 USD | `+50.12%` | `24,042.40` |
| `Live` | `Short` | `1.33` | 498,590.00 USD | 6,340.00 USD | 0.00 USD | `+51.72%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 520,560.00 USD | 21,970.00 USD | 0.00 USD | `+52.06%` | `16,535.70` |
| `Live` | `Short` | `1.33` | 520,920.00 USD | 358.30 USD | 0.00 USD | `+52.29%` | `269.30` |
| `Live` | `Short` | `1.33` | 522,440.00 USD | 1,520.00 USD | 0.00 USD | `+52.52%` | `1,143.40` |
| `Live` | `Short` | `1.34` | 524,630.00 USD | 2,190.00 USD | 0.00 USD | `+52.86%` | `1,639.00` |
| `Live` | `Short` | `1.34` | 531,490.00 USD | 6,860.00 USD | 0.00 USD | `+53.32%` | `5,119.30` |
| `Live` | `Short` | `1.34` | 552,890.00 USD | 21,400.00 USD | 0.00 USD | `+53.67%` | `15,941.90` |
| `Live` | `Short` | `1.37` | 911,170.00 USD | 358,280.00 USD | 0.00 USD | `+57.10%` | `261,043.60` |
| `Live` | `Short` | `1.41` | 915,620.00 USD | 4,450.00 USD | 0.00 USD | `+61.91%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 916,020.00 USD | 402.08 USD | 0.00 USD | `+64.43%` | `279.90` |
| `Live` | `Short` | `1.44` | 916,310.00 USD | 288.68 USD | 0.00 USD | `+64.88%` | `200.40` |
| `Live` | `Short` | `1.50` | 926,070.00 USD | 9,760.00 USD | 0.00 USD | `+72.09%` | `6,491.20` |
| `Live` | `Short` | `1.51` | 930,090.00 USD | 4,020.00 USD | 0.00 USD | `+73.35%` | `2,654.10` |
| `Live` | `Short` | `1.54` | 930,230.00 USD | 144.34 USD | 0.00 USD | `+75.76%` | `94.00` |
| `Live` | `Short` | `1.58` | 930,360.00 USD | 133.21 USD | 0.00 USD | `+80.45%` | `84.50` |
| `Live` | `Short` | `1.58` | 948,290.00 USD | 17,930.00 USD | 0.00 USD | `+80.56%` | `11,363.40` |
| `Live` | `Short` | `1.60` | 957,870.00 USD | 9,580.00 USD | 0.00 USD | `+82.74%` | `6,000.00` |
| `Live` | `Short` | `1.65` | 979,200.00 USD | 21,330.00 USD | 0.00 USD | `+88.46%` | `12,957.30` |
| `Live` | `Short` | `1.66` | 1,020,000.00 USD | 36,530.00 USD | 0.00 USD | `+90.18%` | `21,988.10` |
| `Live` | `Short` | `1.66` | 1,050,000.00 USD | 39,140.00 USD | 0.00 USD | `+90.41%` | `23,529.40` |
| `Live` | `Short` | `1.68` | 1,060,000.00 USD | 2,280.00 USD | 0.00 USD | `+92.24%` | `1,360.10` |
| `Live` | `Short` | `1.69` | 1,060,000.00 USD | 440.71 USD | 0.00 USD | `+93.50%` | `260.70` |
| `Live` | `Short` | `1.69` | 1,350,000.00 USD | 292,630.00 USD | 0.00 USD | `+93.61%` | `173,000.00` |
| `Live` | `Short` | `1.70` | 1,350,000.00 USD | 167.09 USD | 0.00 USD | `+94.76%` | `98.20` |
| `Live` | `Short` | `1.71` | 1,350,000.00 USD | 205.67 USD | 0.00 USD | `+96.02%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,360,000.00 USD | 9,700.00 USD | 0.00 USD | `+96.70%` | `5,645.40` |
| `Live` | `Short` | `1.73` | 1,360,000.00 USD | 226.05 USD | 0.00 USD | `+98.42%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,360,000.00 USD | 560.67 USD | 0.00 USD | `+98.99%` | `322.50` |
| `Live` | `Short` | `1.74` | 1,360,000.00 USD | 2,080.00 USD | 0.00 USD | `+99.22%` | `1,197.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,030,000.00 USD | 0.00 USD | 497.31 USD | `-69.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2745` | 1,030,000.00 USD | 0.00 USD | 455.97 USD | `-68.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,030,000.00 USD | 0.00 USD | 102.75 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,030,000.00 USD | 0.00 USD | 256.78 USD | `-59.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,030,000.00 USD | 0.00 USD | 428.87 USD | `-55.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,030,000.00 USD | 0.00 USD | 123.45 USD | `-52.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,030,000.00 USD | 0.00 USD | 818.15 USD | `-51.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4285` | 1,030,000.00 USD | 0.00 USD | 454.04 USD | `-50.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,030,000.00 USD | 0.00 USD | 436.41 USD | `-50.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,030,000.00 USD | 0.00 USD | 876.79 USD | `-50.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,030,000.00 USD | 0.00 USD | 466.72 USD | `-48.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,030,000.00 USD | 0.00 USD | 142.95 USD | `-45.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,030,000.00 USD | 0.00 USD | 781.98 USD | `-42.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,030,000.00 USD | 0.00 USD | 151.74 USD | `-41.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,030,000.00 USD | 0.00 USD | 123.91 USD | `-40.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,030,000.00 USD | 0.00 USD | 219.80 USD | `-37.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,030,000.00 USD | 0.00 USD | 237,400.00 USD | `-36.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 790,990.00 USD | 0.00 USD | 276.75 USD | `-36.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 790,710.00 USD | 0.00 USD | 2,010.00 USD | `-35.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 788,700.00 USD | 0.00 USD | 119.76 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 788,580.00 USD | 0.00 USD | 470.62 USD | `-31.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 788,110.00 USD | 0.00 USD | 108.39 USD | `-31.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 788,000.00 USD | 0.00 USD | 123.28 USD | `-30.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 787,880.00 USD | 0.00 USD | 488.52 USD | `-28.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 787,390.00 USD | 0.00 USD | 4,230.00 USD | `-28.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 783,160.00 USD | 0.00 USD | 242.24 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 782,920.00 USD | 0.00 USD | 193.95 USD | `-26.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6475` | 782,720.00 USD | 0.00 USD | 647.50 USD | `-25.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 782,080.00 USD | 0.00 USD | 834.79 USD | `-25.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 781,240.00 USD | 0.00 USD | 158.54 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 781,080.00 USD | 0.00 USD | 195.47 USD | `-24.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 780,890.00 USD | 0.00 USD | 190.25 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 780,700.00 USD | 0.00 USD | 153.53 USD | `-24.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 780,540.00 USD | 0.00 USD | 52,450.00 USD | `-23.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 728,100.00 USD | 0.00 USD | 536.11 USD | `-22.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 727,560.00 USD | 0.00 USD | 3,600.00 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 723,970.00 USD | 0.00 USD | 340.75 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 723,620.00 USD | 0.00 USD | 9,270.00 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 714,360.00 USD | 0.00 USD | 120.53 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 714,240.00 USD | 0.00 USD | 160.71 USD | `-20.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 714,080.00 USD | 0.00 USD | 738.08 USD | `-20.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 713,340.00 USD | 0.00 USD | 187.61 USD | `-19.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 713,150.00 USD | 0.00 USD | 2,920.00 USD | `-19.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 710,230.00 USD | 0.00 USD | 89,150.00 USD | `-19.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7065` | 621,080.00 USD | 0.00 USD | 189.06 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 620,890.00 USD | 0.00 USD | 5,650.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 615,240.00 USD | 0.00 USD | 100.47 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 615,140.00 USD | 0.00 USD | 152.05 USD | `-18.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 614,990.00 USD | 0.00 USD | 123.41 USD | `-17.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 614,870.00 USD | 0.00 USD | 745.54 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 614,120.00 USD | 0.00 USD | 1,130.00 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 612,990.00 USD | 0.00 USD | 18,770.00 USD | `-16.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 594,220.00 USD | 0.00 USD | 257.26 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 593,960.00 USD | 0.00 USD | 1,590.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 592,370.00 USD | 0.00 USD | 10,160.00 USD | `-14.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 582,210.00 USD | 0.00 USD | 93,810.00 USD | `-14.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 488,400.00 USD | 0.00 USD | 1,230.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 487,170.00 USD | 0.00 USD | 1,840.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 485,340.00 USD | 0.00 USD | 804.61 USD | `-13.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 484,530.00 USD | 0.00 USD | 191.12 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 484,340.00 USD | 0.00 USD | 1,370.00 USD | `-12.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 482,970.00 USD | 0.00 USD | 125.92 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 482,840.00 USD | 0.00 USD | 1,980.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 480,870.00 USD | 0.00 USD | 1,150.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 479,720.00 USD | 0.00 USD | 174.80 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 479,550.00 USD | 0.00 USD | 6,800.00 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 472,750.00 USD | 0.00 USD | 128.47 USD | `-10.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 472,620.00 USD | 0.00 USD | 10,090.00 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 462,530.00 USD | 0.00 USD | 135.11 USD | `-10.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 462,390.00 USD | 0.00 USD | 8,870.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 453,530.00 USD | 0.00 USD | 1,500.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 452,030.00 USD | 0.00 USD | 25,170.00 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7955` | 426,860.00 USD | 0.00 USD | 103.42 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 426,750.00 USD | 0.00 USD | 1,260.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 425,490.00 USD | 0.00 USD | 4,470.00 USD | `-8.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 421,020.00 USD | 0.00 USD | 144.67 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 420,870.00 USD | 0.00 USD | 50,540.00 USD | `-7.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 370,340.00 USD | 0.00 USD | 263.25 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 370,080.00 USD | 0.00 USD | 16,870.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 353,210.00 USD | 0.00 USD | 91,080.00 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 262,130.00 USD | 0.00 USD | 174.63 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 261,960.00 USD | 0.00 USD | 13,470.00 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 248,490.00 USD | 0.00 USD | 125.72 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 248,360.00 USD | 0.00 USD | 4,860.00 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 243,500.00 USD | 0.00 USD | 19,320.00 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 224,180.00 USD | 0.00 USD | 7,160.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 217,030.00 USD | 0.00 USD | 226.71 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 216,800.00 USD | 0.00 USD | 922.29 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 215,880.00 USD | 0.00 USD | 1,120.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 214,760.00 USD | 0.00 USD | 325.56 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 214,430.00 USD | 0.00 USD | 577.25 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 213,860.00 USD | 0.00 USD | 5,760.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 208,100.00 USD | 0.00 USD | 171.46 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 207,930.00 USD | 0.00 USD | 1,270.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 206,650.00 USD | 0.00 USD | 4,170.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 202,480.00 USD | 0.00 USD | 610.23 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 201,870.00 USD | 0.00 USD | 699.65 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 201,170.00 USD | 0.00 USD | 320.31 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 200,850.00 USD | 0.00 USD | 61,340.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 139,510.00 USD | 0.00 USD | 221.25 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 139,280.00 USD | 0.00 USD | 212.81 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 139,070.00 USD | 0.00 USD | 462.49 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 138,610.00 USD | 0.00 USD | 481.80 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 138,130.00 USD | 0.00 USD | 17,180.00 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 120,950.00 USD | 0.00 USD | 901.40 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 120,040.00 USD | 0.00 USD | 345.13 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 119,700.00 USD | 0.00 USD | 20,920.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 98,780.00 USD | 0.00 USD | 3,640.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 95,130.00 USD | 0.00 USD | 108.13 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 95,030.00 USD | 0.00 USD | 7,800.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 87,230.00 USD | 0.00 USD | 8,740.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 78,490.00 USD | 0.00 USD | 202.45 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 78,290.00 USD | 0.00 USD | 921.70 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 77,360.00 USD | 0.00 USD | 1,270.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 76,090.00 USD | 0.00 USD | 741.45 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 75,350.00 USD | 0.00 USD | 168.75 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 75,180.00 USD | 0.00 USD | 2,990.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 72,190.00 USD | 0.00 USD | 12,700.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 59,490.00 USD | 0.00 USD | 712.45 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 58,770.00 USD | 0.00 USD | 58,490.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 281.70 USD | 0.00 USD | 281.70 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8745` | 133.10 USD | 133.10 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8755` | 380.08 USD | 246.98 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8775` | 9,450.00 USD | 9,070.00 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8785` | 9,600.00 USD | 151.10 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8795` | 10,100.00 USD | 507.74 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8805` | 18,470.00 USD | 8,370.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8815` | 22,540.00 USD | 4,070.00 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8825` | 27,560.00 USD | 5,020.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8835` | 37,330.00 USD | 9,770.00 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 40,990.00 USD | 3,660.00 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 54,440.00 USD | 13,450.00 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 58,050.00 USD | 3,620.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 69,410.00 USD | 11,360.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 78,190.00 USD | 8,780.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 88,540.00 USD | 10,340.00 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 89,010.00 USD | 469.91 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 99,620.00 USD | 10,610.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 106,710.00 USD | 7,100.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 109,640.00 USD | 2,920.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 113,530.00 USD | 3,900.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 113,820.00 USD | 289.12 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 132,030.00 USD | 18,210.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 134,750.00 USD | 2,710.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 163,710.00 USD | 28,960.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 167,570.00 USD | 3,860.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 169,630.00 USD | 2,050.00 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 170,550.00 USD | 926.06 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 171,360.00 USD | 805.29 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 172,500.00 USD | 1,140.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 174,490.00 USD | 1,990.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 196,940.00 USD | 22,450.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 197,190.00 USD | 250.83 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 198,290.00 USD | 1,090.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 199,810.00 USD | 1,520.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 200,740.00 USD | 933.08 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 202,950.00 USD | 2,210.00 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 217,720.00 USD | 14,760.00 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 220,740.00 USD | 3,020.00 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 221,060.00 USD | 318.79 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 226,130.00 USD | 5,070.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 231,170.00 USD | 5,040.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 235,070.00 USD | 3,900.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 237,040.00 USD | 1,970.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 237,160.00 USD | 116.59 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 496,270.00 USD | 259,120.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 648,240.00 USD | 151,960.00 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 653,310.00 USD | 5,070.00 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 779,660.00 USD | 126,350.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 781,060.00 USD | 1,400.00 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 785,640.00 USD | 4,580.00 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 788,420.00 USD | 2,780.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 788,700.00 USD | 287.62 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 788,900.00 USD | 195.17 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 789,000.00 USD | 103.17 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 792,200.00 USD | 3,190.00 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 792,350.00 USD | 148.85 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 792,450.00 USD | 100.90 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 793,430.00 USD | 979.71 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 796,130.00 USD | 2,700.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 800,010.00 USD | 3,880.00 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 800,710.00 USD | 701.16 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 802,580.00 USD | 1,880.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 855,640.00 USD | 53,060.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 859,550.00 USD | 3,910.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 868,510.00 USD | 8,960.00 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 868,670.00 USD | 158.55 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 870,560.00 USD | 1,890.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 872,260.00 USD | 1,700.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 873,050.00 USD | 789.04 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 873,170.00 USD | 117.81 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 874,220.00 USD | 1,050.00 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 880,220.00 USD | 6,000.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 880,490.00 USD | 261.97 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 880,750.00 USD | 265.66 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 890,660.00 USD | 9,910.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 893,810.00 USD | 3,150.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 895,240.00 USD | 1,440.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 898,130.00 USD | 2,890.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 905,730.00 USD | 7,600.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 905,850.00 USD | 121.54 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 905,950.00 USD | 100.17 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 906,200.00 USD | 245.02 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 906,360.00 USD | 161.82 USD | 0.00 USD | `+10.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 906,830.00 USD | 469.51 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 906,970.00 USD | 139.23 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 908,310.00 USD | 1,340.00 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 908,510.00 USD | 204.20 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 909,040.00 USD | 531.57 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 912,200.00 USD | 3,160.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 913,200.00 USD | 993.78 USD | 0.00 USD | `+10.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 913,410.00 USD | 212.90 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 925,090.00 USD | 11,680.00 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 925,210.00 USD | 125.61 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 925,650.00 USD | 441.51 USD | 0.00 USD | `+11.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 936,130.00 USD | 10,480.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 936,380.00 USD | 253.14 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 936,630.00 USD | 244.81 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 936,800.00 USD | 176.73 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 937,010.00 USD | 201.77 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 937,300.00 USD | 295.22 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 970,540.00 USD | 33,240.00 USD | 0.00 USD | `+12.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 976,010.00 USD | 5,470.00 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 976,570.00 USD | 558.35 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 977,630.00 USD | 1,060.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 978,870.00 USD | 1,240.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 979,360.00 USD | 490.99 USD | 0.00 USD | `+13.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 980,130.00 USD | 769.72 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 981,120.00 USD | 991.50 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 991,450.00 USD | 10,340.00 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 991,740.00 USD | 284.92 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 992,020.00 USD | 277.64 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 992,370.00 USD | 350.37 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 992,510.00 USD | 144.04 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 992,620.00 USD | 105.44 USD | 0.00 USD | `+14.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 1,000,000.00 USD | 8,760.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,000,000.00 USD | 1,570.00 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 2,180.00 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 1,010,000.00 USD | 363.87 USD | 0.00 USD | `+14.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 589.52 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,010,000.00 USD | 110.62 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 10,090.00 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 5,420.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 1,020,000.00 USD | 1,960.00 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,020,000.00 USD | 248.49 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 33,450.00 USD | 0.00 USD | `+16.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 722.63 USD | 0.00 USD | `+16.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 312.07 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 171.24 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 1,060,000.00 USD | 561.11 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 249.30 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 2,210.00 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 432.18 USD | 0.00 USD | `+17.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 137.88 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 1,060,000.00 USD | 2,470.00 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,060,000.00 USD | 160.60 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,070,000.00 USD | 6,560.00 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,070,000.00 USD | 2,920.00 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 7,680.00 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,080,000.00 USD | 224.56 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 1,090,000.00 USD | 3,570.00 USD | 0.00 USD | `+19.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 1,090,000.00 USD | 5,610.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,810,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 248.20 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 5,390.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 285.32 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,130.00 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 1,240.00 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,820,000.00 USD | 278.06 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 309.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 272.12 USD | 0.00 USD | `+22.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,830,000.00 USD | 117.12 USD | 0.00 USD | `+22.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,970,000.00 USD | 140,120.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,970,000.00 USD | 530.01 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,970,000.00 USD | 128.23 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,070,000.00 USD | 108,190.00 USD | 0.00 USD | `+23.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 3,080,000.00 USD | 550.49 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,080,000.00 USD | 5,810.00 USD | 0.00 USD | `+24.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 5,570.00 USD | 0.00 USD | `+24.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 1,290.00 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 3,090,000.00 USD | 294.81 USD | 0.00 USD | `+25.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 123.13 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 494.98 USD | 0.00 USD | `+25.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,090,000.00 USD | 613.52 USD | 0.00 USD | `+25.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,200,000.00 USD | 115,100.00 USD | 0.00 USD | `+25.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,200,000.00 USD | 409.76 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,200,000.00 USD | 162.77 USD | 0.00 USD | `+26.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 3,210,000.00 USD | 959.70 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,210,000.00 USD | 160.18 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 3,210,000.00 USD | 433.10 USD | 0.00 USD | `+27.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,210,000.00 USD | 293.61 USD | 0.00 USD | `+28.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 3,320,000.00 USD | 112,050.00 USD | 0.00 USD | `+28.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 462.47 USD | 0.00 USD | `+28.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 2,180.00 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 273.34 USD | 0.00 USD | `+29.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,320,000.00 USD | 119.49 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 3,340,000.00 USD | 20,740.00 USD | 0.00 USD | `+29.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 3,340,000.00 USD | 1,430.00 USD | 0.00 USD | `+30.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,340,000.00 USD | 338.50 USD | 0.00 USD | `+31.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,350,000.00 USD | 769.57 USD | 0.00 USD | `+31.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 3,350,000.00 USD | 1,230.00 USD | 0.00 USD | `+31.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 2,450.00 USD | 0.00 USD | `+32.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 1,250.00 USD | 0.00 USD | `+32.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 143.67 USD | 0.00 USD | `+32.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 3,350,000.00 USD | 1,700.00 USD | 0.00 USD | `+33.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,410,000.00 USD | 62,870.00 USD | 0.00 USD | `+33.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 3,420,000.00 USD | 304.33 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 241.65 USD | 0.00 USD | `+34.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 239.97 USD | 0.00 USD | `+34.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 2,470.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 3,060.00 USD | 0.00 USD | `+35.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 3,420,000.00 USD | 351.02 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,730,000.00 USD | 310,250.00 USD | 0.00 USD | `+36.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,730,000.00 USD | 309.53 USD | 0.00 USD | `+36.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,730,000.00 USD | 159.09 USD | 0.00 USD | `+36.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,730,000.00 USD | 146.21 USD | 0.00 USD | `+37.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,810,000.00 USD | 74,910.00 USD | 0.00 USD | `+37.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,810,000.00 USD | 933.81 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,810,000.00 USD | 658.86 USD | 0.00 USD | `+37.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,020,000.00 USD | 213,390.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 4,020,000.00 USD | 211.10 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,020,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,020,000.00 USD | 812.24 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 4,020,000.00 USD | 509.71 USD | 0.00 USD | `+40.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,020,000.00 USD | 162.15 USD | 0.00 USD | `+40.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,030,000.00 USD | 187.04 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,030,000.00 USD | 542.12 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 4,050,000.00 USD | 23,740.00 USD | 0.00 USD | `+41.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,050,000.00 USD | 2,010.00 USD | 0.00 USD | `+41.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 4,050,000.00 USD | 345.91 USD | 0.00 USD | `+41.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,050,000.00 USD | 104.79 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 4,050,000.00 USD | 2,470.00 USD | 0.00 USD | `+43.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,050,000.00 USD | 265.62 USD | 0.00 USD | `+43.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,060,000.00 USD | 1,480.00 USD | 0.00 USD | `+44.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 4,060,000.00 USD | 1,010.00 USD | 0.00 USD | `+44.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,060,000.00 USD | 340.38 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,060,000.00 USD | 903.22 USD | 0.00 USD | `+45.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 4,060,000.00 USD | 475.01 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,100,000.00 USD | 41,160.00 USD | 0.00 USD | `+46.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 4,110,000.00 USD | 12,840.00 USD | 0.00 USD | `+46.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,130,000.00 USD | 12,890.00 USD | 0.00 USD | `+47.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,130,000.00 USD | 8,820.00 USD | 0.00 USD | `+47.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,140,000.00 USD | 466.95 USD | 0.00 USD | `+48.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 4,140,000.00 USD | 613.59 USD | 0.00 USD | `+48.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,140,000.00 USD | 1,420.00 USD | 0.00 USD | `+48.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,150,000.00 USD | 13,000.00 USD | 0.00 USD | `+48.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 4,150,000.00 USD | 284.42 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 4,170,000.00 USD | 22,810.00 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 4,170,000.00 USD | 640.82 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 4,190,000.00 USD | 13,400.00 USD | 0.00 USD | `+53.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,200,000.00 USD | 13,490.00 USD | 0.00 USD | `+54.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 4,210,000.00 USD | 11,580.00 USD | 0.00 USD | `+54.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,220,000.00 USD | 3,610.00 USD | 0.00 USD | `+55.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 4,220,000.00 USD | 1,540.00 USD | 0.00 USD | `+56.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,220,000.00 USD | 1,500.00 USD | 0.00 USD | `+56.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,230,000.00 USD | 15,000.00 USD | 0.00 USD | `+56.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 4,240,000.00 USD | 9,030.00 USD | 0.00 USD | `+56.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,240,000.00 USD | 569.84 USD | 0.00 USD | `+58.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 4,260,000.00 USD | 13,890.00 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,260,000.00 USD | 2,710.00 USD | 0.00 USD | `+59.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,270,000.00 USD | 14,000.00 USD | 0.00 USD | `+60.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 4,290,000.00 USD | 13,100.00 USD | 0.00 USD | `+60.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,320,000.00 USD | 32,860.00 USD | 0.00 USD | `+61.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,330,000.00 USD | 7,090.00 USD | 0.00 USD | `+61.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,330,000.00 USD | 106.64 USD | 0.00 USD | `+61.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 4,330,000.00 USD | 1,430.00 USD | 0.00 USD | `+61.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,330,000.00 USD | 2,810.00 USD | 0.00 USD | `+62.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 4,340,000.00 USD | 8,420.00 USD | 0.00 USD | `+62.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 4,340,000.00 USD | 1,410.00 USD | 0.00 USD | `+63.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,340,000.00 USD | 431.38 USD | 0.00 USD | `+64.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,340,000.00 USD | 1,390.00 USD | 0.00 USD | `+64.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 4,360,000.00 USD | 14,390.00 USD | 0.00 USD | `+64.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,360,000.00 USD | 7,000.00 USD | 0.00 USD | `+65.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,360,000.00 USD | 434.98 USD | 0.00 USD | `+65.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,380,000.00 USD | 14,490.00 USD | 0.00 USD | `+65.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 4,380,000.00 USD | 1,370.00 USD | 0.00 USD | `+66.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 4,380,000.00 USD | 1,350.00 USD | 0.00 USD | `+67.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,380,000.00 USD | 1,340.00 USD | 0.00 USD | `+67.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,380,000.00 USD | 1,300.00 USD | 0.00 USD | `+68.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 4,390,000.00 USD | 342.08 USD | 0.00 USD | `+68.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 4,390,000.00 USD | 1,330.00 USD | 0.00 USD | `+69.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,390,000.00 USD | 1,320.00 USD | 0.00 USD | `+70.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,390,000.00 USD | 1,310.00 USD | 0.00 USD | `+70.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,400,000.00 USD | 14,890.00 USD | 0.00 USD | `+70.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,410,000.00 USD | 9,580.00 USD | 0.00 USD | `+70.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,430,000.00 USD | 14,980.00 USD | 0.00 USD | `+71.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,550,000.00 USD | 121,130.00 USD | 0.00 USD | `+71.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,550,000.00 USD | 1,270.00 USD | 0.00 USD | `+73.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,550,000.00 USD | 1,260.00 USD | 0.00 USD | `+74.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,550,000.00 USD | 1,980.00 USD | 0.00 USD | `+76.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,550,000.00 USD | 574.53 USD | 0.00 USD | `+82.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,560,000.00 USD | 391.32 USD | 0.00 USD | `+83.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,560,000.00 USD | 1,160.00 USD | 0.00 USD | `+85.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,560,000.00 USD | 1,140.00 USD | 0.00 USD | `+87.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,560,000.00 USD | 1,970.00 USD | 0.00 USD | `+87.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,560,000.00 USD | 281.45 USD | 0.00 USD | `+89.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 4,560,000.00 USD | 958.84 USD | 0.00 USD | `+93.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,560,000.00 USD | 3,550.00 USD | 0.00 USD | `+94.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,570,000.00 USD | 1,070.00 USD | 0.00 USD | `+99.91%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7630` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 36,930.00 USD | 14,770.00 USD | 934.78 USD |
| `7D` | `0.7650` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 969.48 USD | 23,090.00 USD | 10,610.00 USD |
| `1D` | `0.7660` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 224.48 USD | 101.33 USD | 4,420.00 USD |
| `7D` | `0.7670` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 0.00 USD | 177.87 USD | 18,920.00 USD |
| `7D` | `0.7690` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 182.28 USD | 161.63 USD | 0.00 USD |
| `7D` | `0.7710` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7790` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 0.00 USD | 5,390.00 USD | 36.15 USD |
| `1D` | `0.7800` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 0.00 USD | 7,100.00 USD | 22,420.00 USD |
| `7D` | `0.7810` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 0.00 USD | 185.50 USD | 5,200.00 USD |
| `7D` | `0.7830` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 5,450.00 USD |
| `7D` | `0.7850` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 13,160.00 USD |
| `7D` | `0.7870` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 0.00 USD | 14,110.00 USD | 0.00 USD |
| `1D` | `0.7880` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 26,800.00 USD | 572.15 USD | 0.00 USD |
| `1D` | `0.7900` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD |
| `7D` | `0.7910` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 0.00 USD | 5,130.00 USD | 0.00 USD |
| `1D` | `0.7920` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 0.00 USD | 731.00 USD | 0.00 USD |
| `7D` | `0.7930` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 0.00 USD | 210.25 USD | 41,170.00 USD |
| `1D` | `0.7940` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 0.00 USD | 4,090.00 USD | 0.00 USD |
| `7D` | `0.7950` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 9,530.00 USD | 11,320.00 USD | 9,870.00 USD |
| `1D` | `0.7960` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 11,240.00 USD |
| `7D` | `0.7970` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 9,430.00 USD | 0.00 USD | 9,790.00 USD |
| `1D` | `0.7980` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7990` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 911.48 USD | 0.00 USD | 8,460.00 USD |
| `1D` | `0.8000` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 0.00 USD | 322.55 USD | 16,320.00 USD |
| `7D` | `0.8010` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 0.00 USD | 0.00 USD | 35,910.00 USD |
| `1D` | `0.8060` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 11,320.00 USD | 5,490.00 USD | 14,150.00 USD |
| `1D` | `0.8100` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 12,970.00 USD | 5,430.00 USD | 19,940.00 USD |
| `7D` | `0.8110` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 57,370.00 USD | 6,420.00 USD | 38,210.00 USD |
| `1D` | `0.8120` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 27,480.00 USD | 1,350.00 USD | 5,320.00 USD |
| `7D` | `0.8130` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 44,870.00 USD | 16,750.00 USD | 12,050.00 USD |
| `1D` | `0.8140` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 44,940.00 USD | 23,740.00 USD | 22,730.00 USD |
| `7D` | `0.8150` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 137,850.00 USD | 50,280.00 USD | 124,810.00 USD |
| `1D` | `0.8160` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 111,700.00 USD | 22,860.00 USD | 149,520.00 USD |
| `7D` | `0.8170` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 90,990.00 USD | 23,590.00 USD | 78,040.00 USD |
| `1D` | `0.8180` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 11,610.00 USD | 20,880.00 USD | 20,350.00 USD |
| `7D` | `0.8190` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 194,350.00 USD | 52,010.00 USD | 47,340.00 USD |
| `1D` | `0.8200` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 13,230.00 USD | 16,660.00 USD | 36,060.00 USD |
| `7D` | `0.8210` | 6,970,000.00 USD | 0.00 USD | 6,970,000.00 USD | 137,160.00 USD | 56,860.00 USD | 152,490.00 USD |
| `1D` | `0.8220` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 12,100.00 USD | 19,830.00 USD | 30,110.00 USD |
| `7D` | `0.8230` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 38,600.00 USD | 34,380.00 USD | 64,410.00 USD |
| `1D` | `0.8240` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 21,120.00 USD | 16,100.00 USD | 20,080.00 USD |
| `7D` | `0.8250` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 188,770.00 USD | 27,530.00 USD | 126,190.00 USD |
| `1D` | `0.8260` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 16,150.00 USD | 3,800.00 USD | 14,020.00 USD |
| `7D` | `0.8270` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 141,740.00 USD | 51,050.00 USD | 63,610.00 USD |
| `1D` | `0.8280` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 19,690.00 USD | 12,830.00 USD | 33,850.00 USD |
| `7D` | `0.8290` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 88,370.00 USD | 40,370.00 USD | 82,590.00 USD |
| `1D` | `0.8300` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 13,880.00 USD | 9,690.00 USD | 25,690.00 USD |
| `7D` | `0.8310` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 38,140.00 USD | 30,800.00 USD | 22,830.00 USD |
| `1D` | `0.8320` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 19,130.00 USD | 29,090.00 USD | 67,320.00 USD |
| `7D` | `0.8330` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 149,660.00 USD | 85,780.00 USD | 198,210.00 USD |
| `1D` | `0.8340` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 49,780.00 USD | 16,200.00 USD | 43,970.00 USD |
| `7D` | `0.8350` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 76,840.00 USD | 14,320.00 USD | 84,180.00 USD |
| `1D` | `0.8360` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 68,970.00 USD | 21,090.00 USD | 20,660.00 USD |
| `7D` | `0.8370` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 143,550.00 USD | 59,030.00 USD | 102,790.00 USD |
| `1D` | `0.8380` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD |
| `7D` | `0.8390` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 26,140.00 USD | 86,060.00 USD | 77,610.00 USD |
| `1D` | `0.8400` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 80,010.00 USD | 25,720.00 USD | 33,570.00 USD |
| `7D` | `0.8410` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 54,830.00 USD | 40,110.00 USD | 27,780.00 USD |
| `1D` | `0.8420` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 39,240.00 USD | 35,080.00 USD | 22,140.00 USD |
| `7D` | `0.8430` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 77,650.00 USD | 49,990.00 USD | 30,430.00 USD |
| `1D` | `0.8440` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 21,450.00 USD | 12,010.00 USD | 291.54 USD |
| `7D` | `0.8450` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 50,250.00 USD | 55,690.00 USD | 114,040.00 USD |
| `1D` | `0.8460` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,860.00 USD | 23,780.00 USD | 40,760.00 USD |
| `7D` | `0.8470` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 22,200.00 USD | 4,350.00 USD | 32,430.00 USD |
| `1D` | `0.8480` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 23,880.00 USD | 28,060.00 USD | 44,480.00 USD |
| `7D` | `0.8490` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 43,620.00 USD | 16,670.00 USD | 46,700.00 USD |
| `1D` | `0.8500` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 47,850.00 USD | 43,500.00 USD | 155,200.00 USD |
| `7D` | `0.8510` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 93,500.00 USD | 42,650.00 USD | 42,410.00 USD |
| `1D` | `0.8520` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 44,480.00 USD | 28,260.00 USD | 39,920.00 USD |
| `7D` | `0.8530` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 35,800.00 USD | 50,890.00 USD | 29,460.00 USD |
| `1D` | `0.8540` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 56,450.00 USD | 17,420.00 USD | 65,400.00 USD |
| `7D` | `0.8550` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 69,370.00 USD | 26,490.00 USD | 93,270.00 USD |
| `1D` | `0.8560` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 28,740.00 USD | 20,540.00 USD | 10,970.00 USD |
| `7D` | `0.8570` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 96,770.00 USD | 114,170.00 USD | 5,400.00 USD |
| `1D` | `0.8580` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 185,780.00 USD | 17,060.00 USD | 114.50 USD |
| `7D` | `0.8590` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 57,950.00 USD | 12,270.00 USD | 18,570.00 USD |
| `1D` | `0.8600` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 32,470.00 USD | 33,380.00 USD | 636.30 USD |
| `7D` | `0.8610` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 49,960.00 USD | 25,170.00 USD | 30,720.00 USD |
| `1D` | `0.8620` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 6,610.00 USD | 4,970.00 USD | 666.95 USD |
| `7D` | `0.8630` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 25,030.00 USD | 13,800.00 USD | 177,840.00 USD |
| `1D` | `0.8640` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 40,460.00 USD | 34,720.00 USD | 53,730.00 USD |
| `7D` | `0.8650` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 227,130.00 USD | 16,780.00 USD | 102,060.00 USD |
| `1D` | `0.8660` | 946,400.00 USD | 0.00 USD | 946,400.00 USD | 138,180.00 USD | 2,480.00 USD | 271.63 USD |
| `7D` | `0.8670` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 159,830.00 USD | 13,250.00 USD | 58,910.00 USD |
| `1D` | `0.8680` | 805,470.00 USD | 0.00 USD | 805,470.00 USD | 49,450.00 USD | 4,290.00 USD | 58,380.00 USD |
| `7D` | `0.8690` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 175,280.00 USD | 9,930.00 USD | 194,860.00 USD |
| `1D` | `0.8700` | 693,360.00 USD | 0.00 USD | 693,360.00 USD | 3,120.00 USD | 6,380.00 USD | 898.09 USD |
| `7D` | `0.8710` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 619,190.00 USD | 13,020.00 USD | 396,740.00 USD |
| `1D` | `0.8720` | 682,960.00 USD | 0.00 USD | 682,960.00 USD | 1,300.00 USD | 0.00 USD | 308,910.00 USD |
| `7D` | `0.8730` | 717,320.00 USD | 0.00 USD | 717,320.00 USD | 318,460.00 USD | 4,170.00 USD | 394,690.00 USD |
| `1D` | `0.8740` | 372,750.00 USD | 0.00 USD | 372,750.00 USD | 0.00 USD | 0.00 USD | 45,570.00 USD |
| `7D` | `0.8740` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8750` | 988,520.00 USD | 988,520.00 USD | 0.00 USD | 648,980.00 USD | 14,870.00 USD | 324,670.00 USD |
| `1D` | `0.8760` | 327,180.00 USD | 0.00 USD | 327,180.00 USD | 3,590.00 USD | 0.00 USD | 178,920.00 USD |
| `7D` | `0.8770` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 405,620.00 USD | 14,470.00 USD | 2,320.00 USD |
| `1D` | `0.8780` | 144,670.00 USD | 0.00 USD | 144,670.00 USD | 5,990.00 USD | 0.00 USD | 305.84 USD |
| `7D` | `0.8790` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 293,480.00 USD | 15,310.00 USD | 2,550.00 USD |
| `1D` | `0.8800` | 138,380.00 USD | 0.00 USD | 138,380.00 USD | 7,330.00 USD | 0.00 USD | 722.37 USD |
| `7D` | `0.8810` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 637,180.00 USD | 159,430.00 USD | 5,730.00 USD |
| `1D` | `0.8820` | 130,320.00 USD | 0.00 USD | 130,320.00 USD | 130,020.00 USD | 0.00 USD | 305.55 USD |
| `1D` | `0.8830` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8830` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 768,360.00 USD | 265,180.00 USD | 6,140.00 USD |
| `1D` | `0.8840` | 1,820.00 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `0.8850` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 523,060.00 USD | 256,400.00 USD | 8,100.00 USD |
| `1D` | `0.8860` | 2,570.00 USD | 2,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 745.79 USD |
| `7D` | `0.8870` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 626,010.00 USD | 279,830.00 USD | 1,200.00 USD |
| `7D` | `0.8890` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 1,550,000.00 USD | 530,540.00 USD | 4,140.00 USD |
| `1D` | `0.8900` | 304,110.00 USD | 304,110.00 USD | 0.00 USD | 118,020.00 USD | 183,420.00 USD | 95.14 USD |
| `7D` | `0.8910` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 822,980.00 USD | 539,850.00 USD | 7,060.00 USD |
| `1D` | `0.8920` | 503,460.00 USD | 503,460.00 USD | 0.00 USD | 186,330.00 USD | 12,760.00 USD | 255.50 USD |
| `7D` | `0.8930` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 1,800,000.00 USD | 688,070.00 USD | 1,440.00 USD |
| `1D` | `0.8940` | 614,310.00 USD | 614,310.00 USD | 0.00 USD | 98,350.00 USD | 12,490.00 USD | 0.00 USD |
| `7D` | `0.8950` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 748,170.00 USD | 483,200.00 USD | 1,880.00 USD |
| `1D` | `0.8960` | 647,700.00 USD | 647,700.00 USD | 0.00 USD | 6,020.00 USD | 26,570.00 USD | 808.94 USD |
| `7D` | `0.8970` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 681,450.00 USD | 327,340.00 USD | 1,760.00 USD |
| `1D` | `0.8980` | 649,720.00 USD | 649,720.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 207.32 USD |
| `7D` | `0.8990` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 319,550.00 USD | 147,390.00 USD | 130,350.00 USD |
| `1D` | `0.9000` | 876,050.00 USD | 876,050.00 USD | 0.00 USD | 73,470.00 USD | 68,700.00 USD | 84,160.00 USD |
| `7D` | `0.9010` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 139,730.00 USD | 15,640.00 USD | 6,170.00 USD |
| `1D` | `0.9020` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 66,430.00 USD | 65,100.00 USD | 183,010.00 USD |
| `7D` | `0.9030` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 50,720.00 USD | 860.58 USD |
| `1D` | `0.9040` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 46,130.00 USD | 80,350.00 USD | 58,160.00 USD |
| `7D` | `0.9050` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 125,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9060` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 20,820.00 USD | 17,480.00 USD | 0.00 USD |
| `7D` | `0.9070` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 341,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9080` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 92,600.00 USD | 426.90 USD | 81,910.00 USD |
| `7D` | `0.9090` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 53,970.00 USD | 34,550.00 USD | 179,540.00 USD |
| `1D` | `0.9100` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 96,000.00 USD | 6,380.00 USD | 0.00 USD |
| `7D` | `0.9110` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 212,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9120` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 25,050.00 USD | 19,530.00 USD | 0.00 USD |
| `7D` | `0.9130` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 80,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9140` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 79,560.00 USD | 25,930.00 USD | 142,470.00 USD |
| `7D` | `0.9150` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 111,690.00 USD | 0.00 USD | 64,730.00 USD |
| `1D` | `0.9160` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 74,950.00 USD | 35,490.00 USD | 71,620.00 USD |
| `7D` | `0.9170` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 123,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9180` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 14,990.00 USD | 16,630.00 USD | 0.00 USD |
| `7D` | `0.9190` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 257,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9200` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | 32,760.00 USD |
| `7D` | `0.9210` | 16,050,000.00 USD | 16,050,000.00 USD | 0.00 USD | 128,930.00 USD | 16,660.00 USD | 63,810.00 USD |
| `1D` | `0.9220` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 124,570.00 USD | 39,420.00 USD | 219,080.00 USD |
| `7D` | `0.9230` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 51,510.00 USD | 64,540.00 USD | 341,030.00 USD |
| `1D` | `0.9240` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 189,760.00 USD | 59,780.00 USD | 184,790.00 USD |
| `7D` | `0.9250` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 52,570.00 USD | 41,710.00 USD | 67,310.00 USD |
| `1D` | `0.9260` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 63,790.00 USD | 53,330.00 USD | 92,700.00 USD |
| `7D` | `0.9270` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 209,950.00 USD | 0.00 USD | 89,770.00 USD |
| `1D` | `0.9280` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 53,570.00 USD | 59,850.00 USD |
| `1D` | `0.9300` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 35,710.00 USD | 40,000.00 USD | 79,160.00 USD |
| `7D` | `0.9310` | 17,360,000.00 USD | 17,360,000.00 USD | 0.00 USD | 177,720.00 USD | 46,670.00 USD | 166,200.00 USD |
| `1D` | `0.9320` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 128,960.00 USD | 29,480.00 USD | 35,380.00 USD |
| `7D` | `0.9330` | 17,470,000.00 USD | 17,470,000.00 USD | 0.00 USD | 0.00 USD | 50,420.00 USD | 63,160.00 USD |
| `1D` | `0.9340` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 2,150.00 USD | 857.80 USD | 0.00 USD |
| `7D` | `0.9350` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 50,160.00 USD | 52,710.00 USD | 0.00 USD |
| `1D` | `0.9360` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 25,730.00 USD | 33,250.00 USD | 107,120.00 USD |
| `7D` | `0.9370` | 17,870,000.00 USD | 17,870,000.00 USD | 0.00 USD | 251,760.00 USD | 0.00 USD | 41,940.00 USD |
| `1D` | `0.9380` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 262,840.00 USD | 118,850.00 USD | 293,510.00 USD |
| `7D` | `0.9390` | 18,250,000.00 USD | 18,250,000.00 USD | 0.00 USD | 82,760.00 USD | 33,320.00 USD | 263,360.00 USD |
| `1D` | `0.9400` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 114,940.00 USD | 1,710.00 USD | 67,280.00 USD |
| `7D` | `0.9410` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 123,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9420` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 9,740.00 USD | 0.00 USD | 17,370.00 USD |
| `7D` | `0.9430` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 62,100.00 USD | 33,660.00 USD |
| `1D` | `0.9440` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 2,290.00 USD | 75,230.00 USD | 73,420.00 USD |
| `7D` | `0.9450` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 244,270.00 USD | 90,360.00 USD |
| `1D` | `0.9460` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 56,940.00 USD | 33,530.00 USD | 184,380.00 USD |
| `7D` | `0.9470` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 210,630.00 USD |
| `1D` | `0.9480` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 89,360.00 USD | 67,670.00 USD | 56,220.00 USD |
| `7D` | `0.9490` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 107,340.00 USD | 118,920.00 USD |
| `1D` | `0.9500` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 17,970.00 USD | 36,000.00 USD | 69,750.00 USD |
| `7D` | `0.9510` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 7,120.00 USD | 87,720.00 USD | 732,510.00 USD |
| `1D` | `0.9520` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 52,120.00 USD | 28,040.00 USD | 196,190.00 USD |
| `7D` | `0.9530` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 1,270.00 USD | 282.82 USD |
| `1D` | `0.9540` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 62,990.00 USD | 74,340.00 USD | 78,100.00 USD |
| `7D` | `0.9550` | 20,190,000.00 USD | 20,190,000.00 USD | 0.00 USD | 61,410.00 USD | 1,290.00 USD | 60,590.00 USD |
| `1D` | `0.9560` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 21,240.00 USD | 33,820.00 USD | 15,050.00 USD |
| `7D` | `0.9570` | 20,650,000.00 USD | 20,650,000.00 USD | 0.00 USD | 456,500.00 USD | 2,240.00 USD | 1,170.00 USD |
| `1D` | `0.9580` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 689.00 USD | 26,200.00 USD | 159.08 USD |
| `7D` | `0.9590` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 570,590.00 USD | 1,040.00 USD | 289.76 USD |
| `1D` | `0.9600` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 111,160.00 USD | 66,100.00 USD | 82,850.00 USD |
| `7D` | `0.9610` | 22,570,000.00 USD | 22,570,000.00 USD | 0.00 USD | 683,980.00 USD | 190,470.00 USD | 476,080.00 USD |
| `1D` | `0.9620` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 315,960.00 USD | 137,300.00 USD | 239,040.00 USD |
| `7D` | `0.9630` | 24,080,000.00 USD | 24,080,000.00 USD | 0.00 USD | 592,010.00 USD | 301,610.00 USD | 616,480.00 USD |
| `1D` | `0.9640` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 334,070.00 USD | 117,160.00 USD | 197,090.00 USD |
| `7D` | `0.9650` | 25,640,000.00 USD | 25,640,000.00 USD | 0.00 USD | 846,210.00 USD | 301,210.00 USD | 412,280.00 USD |
| `1D` | `0.9660` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 243,570.00 USD | 139,760.00 USD | 120,140.00 USD |
| `7D` | `0.9670` | 27,780,000.00 USD | 27,780,000.00 USD | 0.00 USD | 900,420.00 USD | 530,640.00 USD | 705,590.00 USD |
| `1D` | `0.9680` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 199,180.00 USD | 70,260.00 USD | 280,280.00 USD |
| `7D` | `0.9690` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 600,420.00 USD | 343,680.00 USD | 446,000.00 USD |
| `1D` | `0.9700` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 257,240.00 USD | 122,590.00 USD | 174,530.00 USD |
| `7D` | `0.9710` | 30,260,000.00 USD | 30,260,000.00 USD | 0.00 USD | 641,170.00 USD | 305,860.00 USD | 144,620.00 USD |
| `1D` | `0.9720` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 122,820.00 USD | 117,970.00 USD | 138,160.00 USD |
| `7D` | `0.9730` | 31,050,000.00 USD | 31,050,000.00 USD | 0.00 USD | 453,940.00 USD | 160,420.00 USD | 177,120.00 USD |
| `1D` | `0.9740` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 81,230.00 USD | 31,010.00 USD | 39,830.00 USD |
| `7D` | `0.9750` | 31,730,000.00 USD | 31,730,000.00 USD | 0.00 USD | 193,900.00 USD | 293,590.00 USD | 193,410.00 USD |
| `1D` | `0.9760` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 30,550.00 USD | 24,570.00 USD | 76,650.00 USD |
| `7D` | `0.9770` | 32,770,000.00 USD | 32,770,000.00 USD | 0.00 USD | 329,800.00 USD | 211,000.00 USD | 500,390.00 USD |
| `1D` | `0.9780` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 4,640.00 USD | 14,190.00 USD | 91,180.00 USD |
| `7D` | `0.9790` | 33,500,000.00 USD | 33,500,000.00 USD | 0.00 USD | 424,270.00 USD | 84,800.00 USD | 222,510.00 USD |
| `1D` | `0.9800` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 65,550.00 USD | 48,270.00 USD | 127,720.00 USD |
| `7D` | `0.9810` | 34,010,000.00 USD | 34,010,000.00 USD | 0.00 USD | 254,630.00 USD | 83,040.00 USD | 169,310.00 USD |
| `1D` | `0.9820` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 132,760.00 USD | 29,280.00 USD | 44,360.00 USD |
| `7D` | `0.9830` | 34,570,000.00 USD | 34,570,000.00 USD | 0.00 USD | 259,110.00 USD | 100,200.00 USD | 199,120.00 USD |
| `1D` | `0.9840` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 58,950.00 USD | 62,010.00 USD | 18,200.00 USD |
| `7D` | `0.9850` | 34,990,000.00 USD | 34,990,000.00 USD | 0.00 USD | 241,230.00 USD | 58,210.00 USD | 117,140.00 USD |
| `1D` | `0.9860` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 81,740.00 USD | 43,210.00 USD | 100,330.00 USD |
| `7D` | `0.9870` | 35,480,000.00 USD | 35,480,000.00 USD | 0.00 USD | 248,640.00 USD | 191,820.00 USD | 58,100.00 USD |
| `1D` | `0.9880` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 82,930.00 USD | 16,000.00 USD | 49,360.00 USD |
| `7D` | `0.9890` | 35,770,000.00 USD | 35,770,000.00 USD | 0.00 USD | 191,750.00 USD | 78,280.00 USD | 19,900.00 USD |
| `1D` | `0.9900` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 87,940.00 USD | 43,020.00 USD | 51,990.00 USD |
| `7D` | `0.9910` | 36,150,000.00 USD | 36,150,000.00 USD | 0.00 USD | 201,490.00 USD | 89,640.00 USD | 81,790.00 USD |
| `1D` | `0.9920` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 62,110.00 USD | 41,490.00 USD | 21,600.00 USD |
| `7D` | `0.9930` | 36,520,000.00 USD | 36,520,000.00 USD | 0.00 USD | 230,590.00 USD | 63,950.00 USD | 74,270.00 USD |
| `1D` | `0.9940` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 60,860.00 USD | 36,960.00 USD | 70,300.00 USD |
| `7D` | `0.9950` | 36,840,000.00 USD | 36,840,000.00 USD | 0.00 USD | 53,860.00 USD | 138,500.00 USD | 130,850.00 USD |
| `1D` | `0.9960` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 6,270.00 USD | 6,260.00 USD | 20,320.00 USD |
| `7D` | `0.9970` | 37,490,000.00 USD | 37,490,000.00 USD | 0.00 USD | 218,800.00 USD | 81,210.00 USD | 354,810.00 USD |
| `1D` | `0.9980` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 110,050.00 USD | 21,450.00 USD | 149,210.00 USD |
| `7D` | `0.9990` | 37,750,000.00 USD | 37,750,000.00 USD | 0.00 USD | 125,550.00 USD | 35,870.00 USD | 98,990.00 USD |
| `1D` | `1.00` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 17,400.00 USD | 21,440.00 USD | 16,850.00 USD |
| `7D` | `1.00` | 38,210,000.00 USD | 38,210,000.00 USD | 0.00 USD | 212,210.00 USD | 57,170.00 USD | 185,430.00 USD |
| `1D` | `1.00` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 15,900.00 USD | 17,420.00 USD | 36,190.00 USD |
| `7D` | `1.00` | 38,710,000.00 USD | 38,710,000.00 USD | 0.00 USD | 227,430.00 USD | 61,540.00 USD | 208,880.00 USD |
| `1D` | `1.00` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 15,370.00 USD | 21,270.00 USD | 30,450.00 USD |
| `7D` | `1.00` | 38,860,000.00 USD | 38,860,000.00 USD | 0.00 USD | 49,730.00 USD | 39,560.00 USD | 65,670.00 USD |
| `1D` | `1.01` | 12,080,000.00 USD | 12,080,000.00 USD | 0.00 USD | 9,400.00 USD | 14,230.00 USD | 8,760.00 USD |
| `7D` | `1.01` | 39,350,000.00 USD | 39,350,000.00 USD | 0.00 USD | 256,670.00 USD | 15,900.00 USD | 212,150.00 USD |
| `1D` | `1.01` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 18,940.00 USD | 9,170.00 USD | 12,090.00 USD |
| `7D` | `1.01` | 39,950,000.00 USD | 39,950,000.00 USD | 0.00 USD | 248,390.00 USD | 105,290.00 USD | 247,940.00 USD |
| `1D` | `1.01` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 17,560.00 USD | 5,570.00 USD | 14,820.00 USD |
| `7D` | `1.01` | 40,900,000.00 USD | 40,900,000.00 USD | 0.00 USD | 457,310.00 USD | 174,650.00 USD | 319,400.00 USD |
| `1D` | `1.01` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 21,660.00 USD | 13,540.00 USD | 33,850.00 USD |
| `7D` | `1.01` | 41,740,000.00 USD | 41,740,000.00 USD | 0.00 USD | 260,120.00 USD | 234,510.00 USD | 344,360.00 USD |
| `1D` | `1.01` | 12,280,000.00 USD | 12,280,000.00 USD | 0.00 USD | 13,360.00 USD | 11,210.00 USD | 25,990.00 USD |
| `7D` | `1.01` | 42,180,000.00 USD | 42,180,000.00 USD | 0.00 USD | 256,090.00 USD | 59,720.00 USD | 124,520.00 USD |
| `1D` | `1.02` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 22,200.00 USD | 10,550.00 USD | 6,610.00 USD |
| `7D` | `1.02` | 42,980,000.00 USD | 42,980,000.00 USD | 0.00 USD | 344,600.00 USD | 97,830.00 USD | 360,110.00 USD |
| `1D` | `1.02` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 18,720.00 USD | 4,150.00 USD | 133.18 USD |
| `7D` | `1.02` | 43,820,000.00 USD | 43,820,000.00 USD | 0.00 USD | 293,320.00 USD | 74,810.00 USD | 469,230.00 USD |
| `1D` | `1.02` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 31,730.00 USD | 13,020.00 USD | 44,180.00 USD |
| `7D` | `1.02` | 44,250,000.00 USD | 44,250,000.00 USD | 0.00 USD | 156,090.00 USD | 41,370.00 USD | 235,320.00 USD |
| `1D` | `1.02` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 49,170.00 USD | 12,160.00 USD | 20,660.00 USD |
| `7D` | `1.02` | 44,560,000.00 USD | 44,560,000.00 USD | 0.00 USD | 144,260.00 USD | 60,000.00 USD | 103,070.00 USD |
| `1D` | `1.02` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 29,780.00 USD | 12,720.00 USD | 28,260.00 USD |
| `7D` | `1.02` | 44,790,000.00 USD | 44,790,000.00 USD | 0.00 USD | 79,090.00 USD | 54,210.00 USD | 94,770.00 USD |
| `1D` | `1.03` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 17,840.00 USD | 16,400.00 USD | 33,500.00 USD |
| `7D` | `1.03` | 45,040,000.00 USD | 45,040,000.00 USD | 0.00 USD | 102,860.00 USD | 35,230.00 USD | 110,730.00 USD |
| `1D` | `1.03` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 550.85 USD | 116.87 USD | 11,880.00 USD |
| `7D` | `1.03` | 45,250,000.00 USD | 45,250,000.00 USD | 0.00 USD | 86,710.00 USD | 56,310.00 USD | 67,150.00 USD |
| `1D` | `1.03` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 8,830.00 USD | 12,110.00 USD | 10,170.00 USD |
| `7D` | `1.03` | 45,680,000.00 USD | 45,680,000.00 USD | 0.00 USD | 195,050.00 USD | 78,810.00 USD | 157,210.00 USD |
| `1D` | `1.03` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 19,720.00 USD | 7,410.00 USD | 0.35 USD |
| `7D` | `1.03` | 46,060,000.00 USD | 46,060,000.00 USD | 0.00 USD | 91,400.00 USD | 132,300.00 USD | 163,030.00 USD |
| `1D` | `1.03` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 439.80 USD | 4,130.00 USD | 13,930.00 USD |
| `7D` | `1.03` | 46,250,000.00 USD | 46,250,000.00 USD | 0.00 USD | 113,380.00 USD | 13,040.00 USD | 63,310.00 USD |
| `1D` | `1.04` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 18,450.00 USD | 7,120.00 USD | 43,600.00 USD |
| `7D` | `1.04` | 46,660,000.00 USD | 46,660,000.00 USD | 0.00 USD | 179,260.00 USD | 41,220.00 USD | 181,310.00 USD |
| `7D` | `1.04` | 46,960,000.00 USD | 46,960,000.00 USD | 0.00 USD | 113,030.00 USD | 19,230.00 USD | 175,610.00 USD |
| `7D` | `1.04` | 47,190,000.00 USD | 47,190,000.00 USD | 0.00 USD | 103,260.00 USD | 54,310.00 USD | 72,710.00 USD |
| `7D` | `1.04` | 47,290,000.00 USD | 47,290,000.00 USD | 0.00 USD | 24,360.00 USD | 49,420.00 USD | 24,820.00 USD |
| `7D` | `1.04` | 47,380,000.00 USD | 47,380,000.00 USD | 0.00 USD | 65,460.00 USD | 17,210.00 USD | 1,410.00 USD |
| `7D` | `1.05` | 47,480,000.00 USD | 47,480,000.00 USD | 0.00 USD | 73,270.00 USD | 30,790.00 USD | 294.86 USD |
| `7D` | `1.05` | 47,560,000.00 USD | 47,560,000.00 USD | 0.00 USD | 39,320.00 USD | 20,630.00 USD | 17,210.00 USD |
| `7D` | `1.05` | 47,580,000.00 USD | 47,580,000.00 USD | 0.00 USD | 22,530.00 USD | 0.00 USD | 538.06 USD |
| `7D` | `1.05` | 47,660,000.00 USD | 47,660,000.00 USD | 0.00 USD | 6,060.00 USD | 47,690.00 USD | 28,430.00 USD |
| `7D` | `1.05` | 47,720,000.00 USD | 47,720,000.00 USD | 0.00 USD | 5,800.00 USD | 4,160.00 USD | 46,120.00 USD |
| `7D` | `1.06` | 47,730,000.00 USD | 47,730,000.00 USD | 0.00 USD | 3,670.00 USD | 3,350.00 USD | 197.80 USD |
| `7D` | `1.06` | 47,730,000.00 USD | 47,730,000.00 USD | 0.00 USD | 2,710.00 USD | 194.87 USD | 59.76 USD |
| `7D` | `1.06` | 47,760,000.00 USD | 47,760,000.00 USD | 0.00 USD | 16,550.00 USD | 3,870.00 USD | 12,060.00 USD |
| `7D` | `1.06` | 47,770,000.00 USD | 47,770,000.00 USD | 0.00 USD | 8,610.00 USD | 0.00 USD | 609.22 USD |
| `7D` | `1.06` | 47,780,000.00 USD | 47,780,000.00 USD | 0.00 USD | 4,190.00 USD | 1,110.00 USD | 0.00 USD |
| `7D` | `1.07` | 47,780,000.00 USD | 47,780,000.00 USD | 0.00 USD | 3,910.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `1.07` | 47,810,000.00 USD | 47,810,000.00 USD | 0.00 USD | 0.00 USD | 5,360.00 USD | 17,950.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `573.10M` | Total OI Tokens: `650,727,086.4 SUI`
  * 1h OI Change: `-4.84%` | 4h OI Change: `-8.95%` | 24h OI Change: `-10.90%`
  * Exchange Breakdown: Binance=`110.91M` | Bybit=`76.80M` | OKX=`32.30M` | Hyperliquid=`29.26M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.72K` | Last 24h: `23.24K` | Last 3d: `72.27K` | Last 7d: `159.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0053%` | **USDT OKX** | `0.0096%` |
| **USDT Bybit** | `-0.0001%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0055%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0034%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `53.24%` | `46.76%` | `1.14` | 23,200,000.00 USD |
| `15M` | `Binance` | `49.06%` | `50.94%` | `0.96` | 9,240,000.00 USD |
| `15M` | `OKX` | `61.09%` | `38.91%` | `1.57` | 1,920,000.00 USD |
| `15M` | `Bybit` | `49.61%` | `50.39%` | `0.98` | 1,750,000.00 USD |
| `15M` | `KuCoin` | `57.09%` | `42.91%` | `1.33` | 160,420.00 USD |
| `15M` | `Gate` | `56.37%` | `43.63%` | `1.29` | 648,790.00 USD |
| `15M` | `Bitget` | `37.09%` | `62.91%` | `0.59` | 899,010.00 USD |
| `15M` | `BingX` | `79.58%` | `20.42%` | `3.90` | 1,950,000.00 USD |
| `15M` | `MEXC` | `72.77%` | `27.23%` | `2.67` | 1,610,000.00 USD |
| `15M` | `Bitunix` | `49.51%` | `50.49%` | `0.98` | 738,510.00 USD |
| `15M` | `Hyperliquid` | `36.84%` | `63.16%` | `0.58` | 470,470.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.51%` | `54.49%` | `0.84` | 3,490,000.00 USD |
| `15M` | `Crypto.com` | `52.52%` | `47.48%` | `1.11` | 5,730.00 USD |
| `15M` | `WhiteBIT` | `26.96%` | `73.04%` | `0.37` | 162,870.00 USD |
| `15M` | `HTX` | `53.97%` | `46.03%` | `1.17` | 2,230.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `59.45%` | `40.55%` | `1.47` | 39,120.00 USD |
| `15M` | `Aster` | `50.01%` | `49.99%` | `1.00` | 91,920.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `81.51%` | `18.49%` | `4.41` | 31,240.00 USD |
| `15M` | `Whale Positions` | `49.06%` | `50.94%` | `0.96` | 9,240,000.00 USD |
| `15M` | `Global Accounts` | `53.24%` | `46.76%` | `1.14` | 23,200,000.00 USD |
| `1H` | `SUI` | `45.27%` | `54.73%` | `0.83` | 90,770,000.00 USD |
| `1H` | `Binance` | `42.49%` | `57.51%` | `0.74` | 40,010,000.00 USD |
| `1H` | `OKX` | `51.59%` | `48.41%` | `1.07` | 7,100,000.00 USD |
| `1H` | `Bybit` | `45.9%` | `54.1%` | `0.85` | 7,760,000.00 USD |
| `1H` | `KuCoin` | `46.84%` | `53.16%` | `0.88` | 894,060.00 USD |
| `1H` | `Gate` | `47.92%` | `52.08%` | `0.92` | 1,860,000.00 USD |
| `1H` | `Bitget` | `42.76%` | `57.24%` | `0.75` | 2,970,000.00 USD |
| `1H` | `BingX` | `58.2%` | `41.8%` | `1.39` | 4,450,000.00 USD |
| `1H` | `MEXC` | `48.08%` | `51.92%` | `0.93` | 5,600,000.00 USD |
| `1H` | `Bitunix` | `40.41%` | `59.59%` | `0.68` | 2,690,000.00 USD |
| `1H` | `Hyperliquid` | `43.85%` | `56.15%` | `0.78` | 2,310,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.45%` | `50.55%` | `0.98` | 13,020,000.00 USD |
| `1H` | `Crypto.com` | `45.63%` | `54.37%` | `0.84` | 29,210.00 USD |
| `1H` | `WhiteBIT` | `6.55%` | `93.45%` | `0.07` | 1,260,000.00 USD |
| `1H` | `HTX` | `53.09%` | `46.91%` | `1.13` | 54,770.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.03%` | `53.97%` | `0.85` | 358,710.00 USD |
| `1H` | `Aster` | `29.69%` | `70.31%` | `0.42` | 230,230.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `63.28%` | `36.72%` | `1.72` | 154,290.00 USD |
| `1H` | `Whale Positions` | `42.49%` | `57.51%` | `0.74` | 40,010,000.00 USD |
| `1H` | `Global Accounts` | `45.27%` | `54.73%` | `0.83` | 90,770,000.00 USD |
| `4H` | `SUI` | `44.12%` | `55.88%` | `0.79` | 149,110,000.00 USD |
| `4H` | `Binance` | `43.1%` | `56.9%` | `0.76` | 57,730,000.00 USD |
| `4H` | `OKX` | `48.33%` | `51.67%` | `0.94` | 11,200,000.00 USD |
| `4H` | `Bybit` | `45.59%` | `54.41%` | `0.84` | 11,470,000.00 USD |
| `4H` | `KuCoin` | `46.35%` | `53.65%` | `0.86` | 1,270,000.00 USD |
| `4H` | `Gate` | `48.21%` | `51.79%` | `0.93` | 2,970,000.00 USD |
| `4H` | `Bitget` | `41.82%` | `58.18%` | `0.72` | 4,090,000.00 USD |
| `4H` | `BingX` | `47.88%` | `52.12%` | `0.92` | 15,820,000.00 USD |
| `4H` | `MEXC` | `49.13%` | `50.87%` | `0.97` | 9,350,000.00 USD |
| `4H` | `Bitunix` | `43.97%` | `56.03%` | `0.78` | 4,680,000.00 USD |
| `4H` | `Hyperliquid` | `41.36%` | `58.64%` | `0.71` | 2,690,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.17%` | `50.83%` | `0.97` | 21,390,000.00 USD |
| `4H` | `Crypto.com` | `56.19%` | `43.81%` | `1.28` | 42,710.00 USD |
| `4H` | `WhiteBIT` | `1.67%` | `98.33%` | `0.02` | 5,160,000.00 USD |
| `4H` | `HTX` | `53.92%` | `46.08%` | `1.17` | 69,720.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.12%` | `51.88%` | `0.93` | 571,190.00 USD |
| `4H` | `Aster` | `36.67%` | `63.33%` | `0.58` | 362,750.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.79%` | `50.21%` | `0.99` | 253,750.00 USD |
| `4H` | `Whale Positions` | `43.1%` | `56.9%` | `0.76` | 57,730,000.00 USD |
| `4H` | `Global Accounts` | `44.12%` | `55.88%` | `0.79` | 149,110,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9324` | `0.9295` | `0.9324` | `0.9329` | `0.9253` | 3,699,722.99 USD | 2,179,603.27 USD | 1,520,119.72 USD | 659,483.55 USD | `+17.83%` | `23B / 6S` |
| `0:00 UTC` | `0.9297` | `0.9291` | `0.9297` | `0.9317` | `0.9275` | 1,239,749.35 USD | 593,055.04 USD | 646,694.30 USD | -53,639.26 USD | `-4.33%` | `5B / 5S` |
| `5:00 UTC` | `0.9315` | `0.9301` | `0.9315` | `0.9321` | `0.9274` | 1,221,799.97 USD | 672,184.00 USD | 549,615.97 USD | 122,568.03 USD | `+10.03%` | `9B / 6S` |
| `0:00 UTC` | `0.9318` | `0.9320` | `0.9318` | `0.9338` | `0.9294` | 1,810,474.94 USD | 929,976.91 USD | 880,498.03 USD | 49,478.88 USD | `+2.73%` | `7B / 6S` |
| `5:00 UTC` | `0.9302` | `0.9304` | `0.9302` | `0.9331` | `0.9288` | 1,273,512.84 USD | 565,164.16 USD | 708,348.68 USD | -143,184.52 USD | `-11.24%` | `4B / 11S` |
| `0:00 UTC` | `0.9115` | `0.9168` | `0.9115` | `0.9303` | `0.9099` | 9,410,634.53 USD | 4,625,948.50 USD | 4,784,686.02 USD | -158,737.52 USD | `-1.69%` | `3B / 20S` |
| `5:00 UTC` | `0.9172` | `0.9175` | `0.9172` | `0.9204` | `0.9146` | 2,946,350.12 USD | 1,501,911.34 USD | 1,444,438.78 USD | 57,472.55 USD | `+1.95%` | `10B / 6S` |
| `0:00 UTC` | `0.8942` | `0.8944` | `0.8942` | `0.9194` | `0.8750` | 25,714,743.86 USD | 10,323,786.97 USD | 15,390,956.89 USD | -5,067,169.92 USD | `-19.71%` | `3B / 22S` |
| `5:00 UTC` | `0.8801` | `0.8742` | `0.8801` | `0.8897` | `0.8575` | 25,765,113.89 USD | 12,461,836.10 USD | 13,303,277.79 USD | -841,441.70 USD | `-3.27%` | `7B / 12S` |
| `0:00 UTC` | `0.8735` | `0.8751` | `0.8735` | `0.8792` | `0.8692` | 3,451,372.00 USD | 1,617,050.98 USD | 1,834,321.02 USD | -217,270.04 USD | `-6.30%` | `11B / 11S` |

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
| `5m` | 372,230.00 USD | 860,440.00 USD | **`ACCUMULATION`** |
| `15m` | 600,530.00 USD | -224,610.00 USD | **`ACCUMULATION`** |
| `30m` | -3,760,000.00 USD | -13,280,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -6,500,000.00 USD | -12,470,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -8,020,000.00 USD | -12,450,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -8,490,000.00 USD | -15,150,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,640,000.00 USD | -19,990,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,410,000.00 USD | -17,160,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,130,000.00 USD | -17,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,970,000.00 USD | -30,640,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -22,220,000.00 USD | -79,230,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -150,980,000.00 USD | -477,610,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+372.23K` | 15m=`+600.53K` | 1h=`-6.50M` | 24h=`-8.97M`
* Futures Capital Netflows: 5m=`+860.44K` | 15m=`-224.61K` | 1h=`-12.47M` | 24h=`-30.64M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
