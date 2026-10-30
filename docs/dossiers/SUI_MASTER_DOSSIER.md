# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SUI
**Canonical Key**: `SUI` | **Broker Instrument**: `SUIUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:56:55 IST` (`2026-10-30 09:26:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.8833` | `0.8835` | `0.8813` | `0.8817` | `355,700` | 313,797.52 USD | -23,951.00 USD | `-7.63%` | -17,715,794.91 USD | `+0.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.8817` | `0.8846` | `0.8815` | `0.8830` | `414,832` | 366,333.21 USD | 152,635.92 USD | `+41.67%` | -17,563,159.00 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.8830` | `0.8833` | `0.8819` | `0.8820` | `131,724` | 116,274.49 USD | -9,696.47 USD | `-8.34%` | -17,572,855.47 USD | `+0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.8820` | `0.8862` | `0.8813` | `0.8830` | `1,245,374` | 1,099,871.32 USD | 63,698.64 USD | `+5.79%` | -15,550,941.03 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.8829` | `0.8849` | `0.8811` | `0.8817` | `3,432,496` | 3,028,718.86 USD | -1,387,671.71 USD | `-45.82%` | -16,938,612.74 USD | `-2.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.8817` | `0.8846` | `0.8815` | `0.8820` | `546,638` | 482,680.47 USD | 143,012.21 USD | `+29.63%` | -16,795,600.53 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.8957` | `0.8970` | `0.8816` | `0.8851` | `11,435,469` | 10,155,670.71 USD | -1,564,974.23 USD | `-15.41%` | -16,662,714.02 USD | `-0.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.8851` | `0.8882` | `0.8802` | `0.8830` | `8,292,750` | 7,329,307.66 USD | 167,351.63 USD | `+2.28%` | -16,495,362.40 USD | `+0.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.8829` | `0.8849` | `0.8811` | `0.8820` | `3,976,285` | 3,508,886.42 USD | -1,247,052.81 USD | `-35.54%` | -17,742,415.21 USD | `-0.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,183,102.89 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8851` | `53,790,878` | 48,001,087.15 USD | -4,396,820.97 USD | `-9.16%` | -16,579,923.86 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8851` | `0.8882` | `0.8802` | `0.8820` | `12,271,811` | 10,840,642.95 USD | -1,077,371.91 USD | `-9.94%` | -17,657,295.77 USD | `+0.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9539` | `0.9617` | `0.9250` | `0.9295` | `47,160,892` | 44,338,664.22 USD | -2,573,311.69 USD | `-5.80%` | -544,594.77 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9294` | `0.9303` | `0.8574` | `0.8693` | `145,957,878` | 129,371,488.06 USD | -7,702,434.84 USD | `-5.95%` | -8,247,029.61 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.8693` | `0.8873` | `0.8264` | `0.8841` | `103,500,549` | 88,462,703.20 USD | -3,936,073.28 USD | `-4.45%` | -12,183,102.89 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8841` | `0.9049` | `0.8777` | `0.8851` | `53,790,878` | 48,001,087.15 USD | -4,396,820.97 USD | `-9.16%` | -16,579,923.86 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.8851` | `0.8882` | `0.8802` | `0.8820` | `12,271,811` | 10,840,642.95 USD | -1,077,371.91 USD | `-9.94%` | -17,657,295.77 USD | `+0.62` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.8812` | `2142.4000` | 1,887.99 USD | 45,783.89 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8812` | `2488.3000` | 2,192.74 USD | 47,976.63 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.8813` | `5704.3000` | 5,027.48 USD | 24,053.78 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8813` | `5681.6000` | 5,007.42 USD | 29,061.20 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.8813` | `1168.7000` | 1,030.01 USD | 30,091.21 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8813` | `253.3000` | 223.24 USD | 30,314.44 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.8813` | `2721.6000` | 2,398.52 USD | 32,712.96 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8813` | `1168.7000` | 1,029.94 USD | 33,742.90 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8813` | `11521.0000` | 10,153.00 USD | 43,895.90 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.8814` | `1612.2000` | 1,420.99 USD | 19,026.29 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.8815` | `1168.8000` | 1,030.33 USD | 3,081.26 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.8815` | `1136.1000` | 1,001.48 USD | 4,082.74 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8815` | `1168.8000` | 1,030.30 USD | 5,113.04 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8815` | `6806.5000` | 5,999.86 USD | 11,112.90 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8815` | `3942.1000` | 3,474.88 USD | 14,587.78 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.8815` | `1154.4000` | 1,017.57 USD | 15,605.35 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8815` | `2268.9000` | 1,999.94 USD | 17,605.30 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.8816` | `443.3000` | 390.82 USD | 1,020.51 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.8816` | `1168.8000` | 1,030.41 USD | 2,050.93 USD | `1 orders` | `-0.02%` | `-` |
| `MID_SPREAD` | `0.8817` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.88` | `0.00%` | `-` |
| `BID` | `0.8817` | `714.2000` | 629.70 USD | 629.70 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `0.8818` | `1135.7000` | 1,001.47 USD | 2,466.75 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8818` | `661.7000` | 583.49 USD | 1,465.28 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8818` | `1000.0000` | 881.79 USD | 881.79 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.8819` | `113.3000` | 99.92 USD | 5,700.28 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8819` | `1168.7000` | 1,030.70 USD | 5,600.36 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8819` | `113.3000` | 99.92 USD | 4,569.66 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8819` | `2271.3000` | 2,002.99 USD | 4,469.74 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.8820` | `2697.1000` | 2,378.95 USD | 12,143.89 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8820` | `1168.7000` | 1,030.81 USD | 9,764.94 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8820` | `1168.8000` | 1,030.87 USD | 8,734.13 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8820` | `2271.0000` | 2,002.98 USD | 7,703.26 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.8821` | `1168.7000` | 1,030.97 USD | 20,952.07 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8821` | `1971.0000` | 1,738.66 USD | 19,921.10 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8821` | `1168.7000` | 1,030.90 USD | 18,182.44 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8821` | `5677.1000` | 5,007.66 USD | 17,151.54 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.8822` | `1168.8000` | 1,031.16 USD | 26,148.44 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.8822` | `2721.4000` | 2,400.85 USD | 25,117.27 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8822` | `2000.0000` | 1,764.36 USD | 22,716.43 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.8823` | `2139.8000` | 1,887.99 USD | 30,231.83 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.8823` | `2488.3000` | 2,195.40 USD | 28,343.84 USD | `1 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:52:21 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `671` | `0xb83d...6e36` | `SHORT` | 3,363,581.11 USD | `3,817,609.40` | `1.11` | `0.8801` | `30.30` | 855,154.20 USD | `+25.42%` | `3X Cross` |
| `1006` | `0xa2ce...3126` | `LONG` | 2,202,584.16 USD | `2,500,010.40` | `0.8597` | `0.8801` | `0.000000` | 53,377.63 USD | `+2.42%` | `10X Cross` |
| `1517` | `0x9946...0852` | `SHORT` | 1,419,936.12 USD | `1,613,032.20` | `1.06` | `0.8801` | `1.85` | 288,741.97 USD | `+20.33%` | `10X Cross` |
| `1908` | `0x9df2...c665` | `SHORT` | 1,057,164.00 USD | `1,200,000.00` | `0.7465` | `0.8801` | `26.34` | -161,311.60 USD | `-15.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.07` | 1,313.92 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.31K USD at 1.0671 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,887.95 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.89K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 399.99 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.40K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 639.25 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.64K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,811.97 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.81K USD at 1.0672 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,655.76 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.66K USD at 1.0673 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 1,999.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.00K USD at 1.0675 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 10.25 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.01K USD at 1.0675 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 5,003.24 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 5.00K USD at 1.0677 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 791.63 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.79K USD at 1.0679 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.07` | 2,836.50 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.84K USD at 1.0680 USD [API] | `2026-10-08 15:15:34` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 2,515.30 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.52K USD at 1.1066 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 9,682.20 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 9.68K USD at 1.1066 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 1,660.05 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.66K USD at 1.1067 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 399.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.40K USD at 1.1067 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `1.11` | 3,348.76 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.35K USD at 1.1067 USD [API] | `2026-09-29 01:36:16` |
| `ANNOUNCEMENT` | `INFO` | `0.9111` | 5,342.96 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.34K USD at 0.9111 USD [API] | `2026-10-29 09:38:03` |
| `ANNOUNCEMENT` | `INFO` | `0.9130` | 5,343.70 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9130 USD [API] | `2026-10-29 09:42:02` |
| `ANNOUNCEMENT` | `INFO` | `0.9240` | 5,089.80 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.09K USD at 0.9240 USD [API] | `2026-10-29 10:48:46` |
| `ANNOUNCEMENT` | `INFO` | `0.9247` | 16,233.60 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 16.23K USD at 0.9247 USD [API] | `2026-10-29 11:01:51` |
| `ANNOUNCEMENT` | `INFO` | `0.9234` | 5,154.59 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.15K USD at 0.9234 USD [API] | `2026-10-29 11:05:05` |
| `ANNOUNCEMENT` | `INFO` | `0.9231` | 17,331.58 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 17.33K USD at 0.9231 USD [API] | `2026-10-29 11:07:33` |
| `ANNOUNCEMENT` | `INFO` | `0.9254` | 5,344.08 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9254 USD [API] | `2026-10-29 11:09:53` |
| `ANNOUNCEMENT` | `INFO` | `0.9222` | 6,029.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.03K USD at 0.9222 USD [API] | `2026-10-29 11:29:21` |
| `ANNOUNCEMENT` | `INFO` | `0.9260` | 12,149.38 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 12.15K USD at 0.9260 USD [API] | `2026-10-29 12:46:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9260` | 5,344.06 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.34K USD at 0.9260 USD [API] | `2026-10-29 12:46:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9278` | 5,999.95 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 6.00K USD at 0.9278 USD [API] | `2026-10-29 13:20:55` |
| `ANNOUNCEMENT` | `INFO` | `0.9244` | 7,325.08 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 7.33K USD at 0.9244 USD [API] | `2026-10-29 13:39:14` |
| `ANNOUNCEMENT` | `INFO` | `0.9277` | 11,844.84 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 11.84K USD at 0.9277 USD [API] | `2026-10-29 13:41:43` |
| `ANNOUNCEMENT` | `INFO` | `0.9315` | 5,006.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9315 USD [API] | `2026-10-29 14:03:28` |
| `ANNOUNCEMENT` | `INFO` | `1.03` | 13.62 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.01K USD at 1.0320 USD [API] | `2026-09-24 20:04:05` |
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 1,601.78 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 1.60K USD at 0.9406 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 661.44 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.66K USD at 0.9406 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9406` | 919.02 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.92K USD at 0.9406 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 415.91 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.42K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 686.09 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.69K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 725.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.73K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9405` | 725.37 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Short: 0.73K USD at 0.9405 USD [API] | `2026-09-21 00:20:20` |
| `ANNOUNCEMENT` | `INFO` | `0.9345` | 16,444.19 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 16.44K USD at 0.9345 USD [API] | `2026-10-29 14:13:52` |
| `ANNOUNCEMENT` | `INFO` | `0.9470` | 5,005.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9470 USD [API] | `2026-10-29 17:00:22` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 182.45 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.18K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 109.34 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.11K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 97.45 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 1,641.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.64K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 2,014.24 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.01K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9508` | 2,014.26 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.01K USD at 0.9508 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9509` | 999.27 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 1.00K USD at 0.9509 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9509` | 5,005.43 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 5.01K USD at 0.9509 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9509` | 97.28 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9509 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9509` | 992.16 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.99K USD at 0.9509 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9509` | 571.22 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.57K USD at 0.9509 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9509` | 3,542.78 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.54K USD at 0.9509 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9509` | 16,527.62 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 16.53K USD at 0.9509 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9510` | 2,014.51 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.01K USD at 0.9510 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9510` | 99.95 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.10K USD at 0.9510 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9510` | 20,908.58 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 20.91K USD at 0.9510 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9511` | 2,014.73 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.01K USD at 0.9511 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9511` | 27.01 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.03K USD at 0.9511 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9511` | 2,366.65 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.37K USD at 0.9511 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9512` | 2,014.94 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.01K USD at 0.9512 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9513` | 2,015.17 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.02K USD at 0.9513 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9514` | 622.58 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.62K USD at 0.9514 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9514` | 2,015.40 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.02K USD at 0.9514 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9514` | 3,399.94 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 3.40K USD at 0.9514 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9514` | 74.97 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 0.07K USD at 0.9514 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9516` | 2,187.85 USD | `-` | `NEWS_INTEL` | `-` | #SUI Liquidated Long: 2.19K USD at 0.9516 USD [API] | `2026-10-23 22:50:40` |
| `ANNOUNCEMENT` | `INFO` | `0.9445` | 5,005.35 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.01K USD at 0.9445 USD [API] | `2026-10-29 17:07:12` |
| `ANNOUNCEMENT` | `INFO` | `0.9419` | 5,267.73 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale SELL: 5.27K USD at 0.9419 USD [API] | `2026-10-29 17:21:34` |
| `ANNOUNCEMENT` | `INFO` | `0.9430` | 5,005.47 USD | `-` | `NEWS_INTEL` | `-` | #SUI Whale BUY: 5.01K USD at 0.9430 USD [API] | `2026-10-29 17:24:14` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9069` (Vol: 414,400.00 USD, Dist: `+2.86%`) | Long MP=`0.8716` (Vol: 414,400.00 USD, Dist: `--1.15%`)
  * 48H Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+2.93%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--1.18%`)
  * 3D Horizon: Short MP=`0.9075` (Vol: 414,400.00 USD, Dist: `+2.93%`) | Long MP=`0.8713` (Vol: 414,400.00 USD, Dist: `--1.18%`)
  * 7D Horizon: Short MP=`0.9731` (Vol: 542,500.00 USD, Dist: `+10.37%`) | Long MP=`0.8715` (Vol: 414,400.00 USD, Dist: `--1.16%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1835` | 1,330.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1865` | 217.89 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 256.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 4,040.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 493.41 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 102.79 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 789.66 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 394.86 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 243.50 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2525` | 2,250.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2545` | 3,630.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 1,720.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 173.82 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 849.48 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 172.42 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 2,830.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 248.34 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 1,030.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 24,590.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 29,070.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 159.57 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2965` | 183.30 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2975` | 4,330.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2985` | 178.23 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 605.12 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3115` | 270.38 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3205` | 131.21 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3215` | 106.38 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3315` | 4,040.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3405` | 3,410.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3465` | 1,230.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3475` | 3,850.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3495` | 37,110.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3505` | 1,020.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 595.72 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3665` | 274.88 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 6,240.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3745` | 6,370.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3795` | 278.02 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3825` | 2,100.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3845` | 1,750.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3855` | 429.87 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3865` | 270.55 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3875` | 4,820.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3895` | 2,980.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3925` | 5,030.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3945` | 754.48 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 935.03 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4045` | 5,520.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4065` | 3,360.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4095` | 28,670.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4215` | 3,930.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4225` | 5,280.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4245` | 468.61 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 8,510.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4345` | 765.59 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 122.91 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4425` | 44,080.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 219.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4455` | 574.83 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4465` | 19,600.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 105.25 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4505` | 816.71 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 1,020.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4545` | 318.15 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4595` | 3,330.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4655` | 394.65 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 221.37 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 9,230.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4765` | 111.36 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4775` | 160.63 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4785` | 110.10 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4825` | 166.70 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 174.01 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4845` | 3,540.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 201.07 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 105.34 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 2,380.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 544.71 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 106.32 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 211.88 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 5,620.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 216.75 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5015` | 212.49 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 1,230.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5055` | 211.25 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 12,570.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5095` | 195.75 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 4,850.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5145` | 1,570.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5155` | 106.04 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5165` | 619.80 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 213.68 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 982.56 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5235` | 124.02 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5245` | 277.57 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5265` | 553.93 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5275` | 348.36 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5285` | 276.72 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5295` | 123,370.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5305` | 264.56 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5315` | 7,760.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,790.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 113.47 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5375` | 1,480.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5395` | 126.46 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 7,090.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5425` | 269.13 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5445` | 230.32 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5465` | 272.87 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,240.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5495` | 1,310.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5505` | 27,770.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5515` | 160.93 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5525` | 582.56 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 271.88 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5545` | 6,550.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5555` | 7,950.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5585` | 141.97 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5595` | 304.93 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5615` | 442.63 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5625` | 468.45 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5635` | 1,480.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 8,190.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5665` | 7,200.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5675` | 1,560.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 973.22 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5725` | 139.23 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5735` | 109,930.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5745` | 144.03 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5755` | 217.37 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5765` | 1,150.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5775` | 841.01 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 212.85 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5805` | 82,680.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5825` | 6,470.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5835` | 6,300.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 584.50 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5855` | 2,280.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5865` | 822.98 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5885` | 311.14 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 225.93 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 273.68 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5935` | 1,130.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5945` | 8,220.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5965` | 1,330.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5975` | 3,420.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5985` | 299.25 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5995` | 4,610.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6005` | 351.11 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6015` | 323.79 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6025` | 432.35 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 851.05 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6085` | 3,620.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6095` | 214.54 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6115` | 6,280.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 438.73 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 2,220.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6155` | 935.13 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 29,900.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 4,980.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6185` | 12,570.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6195` | 2,400.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6225` | 708.53 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6245` | 356.65 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6255` | 33,460.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6285` | 102.45 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 1,100.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6305` | 319.35 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6345` | 947.69 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 14,700.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 3,060.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6375` | 1,100.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6385` | 2,200.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 34,650.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 86,920.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 477.63 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6435` | 3,190.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6445` | 65,790.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6455` | 14,590.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 146.76 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 2,810.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6485` | 1,060.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6495` | 344.82 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6505` | 106.75 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 403,320.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6525` | 2,350.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6535` | 2,840.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6545` | 7,850.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6555` | 676.54 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6565` | 7,400.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 130.91 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6585` | 20,750.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 1,060.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6615` | 4,960.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6625` | 4,050.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6645` | 448.54 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6655` | 1,220.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6665` | 528.73 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6675` | 2,260.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6685` | 5,470.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6705` | 2,830.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 2,240.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 8,140.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6735` | 633.09 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6745` | 33,610.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 111.59 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6765` | 744.15 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 2,650.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6785` | 122.94 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6795` | 39,510.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 4,150.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6825` | 19,300.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 11,170.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6845` | 5,960.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 112.59 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6875` | 6,110.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6885` | 344.25 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 2,110.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6905` | 3,360.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 8,970.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6935` | 3,600.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6945` | 722.28 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 1,700.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 273.03 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6975` | 1,030.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 5,130.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 235.37 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7015` | 1,990.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7025` | 39,470.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7045` | 8,970.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7055` | 141.38 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 143.14 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 1,560.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7085` | 2,020.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7095` | 1,140.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7105` | 4,190.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7115` | 198.58 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7125` | 283.22 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 927.55 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7155` | 11,030.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7165` | 4,620.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7185` | 126.96 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7195` | 420.19 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 8,970.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7225` | 1,420.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 127.05 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7245` | 2,520.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 311.60 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7265` | 7,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7275` | 35,890.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 424.86 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 375.98 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 8,550.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,630.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7345` | 22,160.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7355` | 51,920.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 441,900.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 3,450.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7380` | 10,560,000.00 USD | 10,560,000.00 USD | 56,620.00 USD | 28,770.00 USD | 82,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7385` | 6,020.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 3,380.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7400` | 10,390,000.00 USD | 10,390,000.00 USD | 17,280.00 USD | 13,180.00 USD | 24,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7405` | 3,530.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 382.61 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7420` | 10,340,000.00 USD | 10,340,000.00 USD | 31,920.00 USD | 8,580.00 USD | 37,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7425` | 2,280.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7435` | 783,980.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7440` | 10,260,000.00 USD | 10,260,000.00 USD | 65,280.00 USD | 21,190.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7455` | 2,160.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7460` | 10,130,000.00 USD | 10,130,000.00 USD | 22,100.00 USD | 24,720.00 USD | 42,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7465` | 563.83 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7475` | 107,260.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7480` | 10,050,000.00 USD | 10,050,000.00 USD | 11,220.00 USD | 6,300.00 USD | 375.99 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7495` | 599.60 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7500` | 10,030,000.00 USD | 10,030,000.00 USD | 25,600.00 USD | 12,880.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7515` | 1,210.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7520` | 9,980,000.00 USD | 9,980,000.00 USD | 2,130.00 USD | 10,160.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7525` | 357.14 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 569.50 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7540` | 9,940,000.00 USD | 9,940,000.00 USD | 9,690.00 USD | 4,770.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7545` | 922.07 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 2,070.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7560` | 9,910,000.00 USD | 9,910,000.00 USD | 2,690.00 USD | 17,670.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7575` | 1,900.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7580` | 9,890,000.00 USD | 9,890,000.00 USD | 19,590.00 USD | 20,390.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7585` | 40,520.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 7,810.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7600` | 9,850,000.00 USD | 9,850,000.00 USD | 8,420.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7615` | 351.43 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7620` | 9,830,000.00 USD | 9,830,000.00 USD | 40,420.00 USD | 16,580.00 USD | 630.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7625` | 859.11 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 439.47 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7640` | 9,780,000.00 USD | 9,780,000.00 USD | 556.58 USD | 118.70 USD | 573.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7645` | 1,060.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7655` | 2,740.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7660` | 9,780,000.00 USD | 9,780,000.00 USD | 1,280.00 USD | 23,260.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7665` | 2,950.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7675` | 24,420.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7680` | 9,720,000.00 USD | 9,720,000.00 USD | 182.28 USD | 3,780.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7685` | 6,600.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7695` | 144,250.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7700` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7705` | 5,640.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7715` | 19,250.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7720` | 9,710,000.00 USD | 9,710,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 1,940.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7735` | 5,230.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7755` | 3,430.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 2,930.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7785` | 28,010.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 322,650.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 2,640.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7815` | 4,160.00 USD | 729,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7820` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 1,440.00 USD | 10,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7835` | 4,620.00 USD | 725,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7840` | 9,680,000.00 USD | 9,680,000.00 USD | 6,050.00 USD | 2,680.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7855` | 156.16 USD | 720,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7860` | 9,670,000.00 USD | 9,670,000.00 USD | 1,740.00 USD | 45,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 3,470.00 USD | 720,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7875` | 288.70 USD | 717,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7900` | 9,630,000.00 USD | 9,630,000.00 USD | 6,610.00 USD | 28,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 3,160.00 USD | 716,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7915` | 11,600.00 USD | 713,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7920` | 7,550,000.00 USD | 7,550,000.00 USD | 14,490.00 USD | 21,760.00 USD | 45,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7920` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 23,790.00 USD | 69,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7925` | 3,800.00 USD | 702,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7930` | 7,470,000.00 USD | 7,470,000.00 USD | 1,220.00 USD | 12,720.00 USD | 7,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 809.45 USD | 698,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7940` | 7,450,000.00 USD | 7,450,000.00 USD | 30,150.00 USD | 8,730.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 1,760.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7945` | 736.66 USD | 697,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7950` | 7,390,000.00 USD | 7,390,000.00 USD | 6,200.00 USD | 3,900.00 USD | 24,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7955` | 52,610.00 USD | 696,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7960` | 7,360,000.00 USD | 7,360,000.00 USD | 2,360.00 USD | 2,710.00 USD | 20,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 9,490,000.00 USD | 9,490,000.00 USD | 5,300.00 USD | 19,750.00 USD | 87,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7965` | 12,980.00 USD | 644,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7970` | 7,330,000.00 USD | 7,330,000.00 USD | 19,610.00 USD | 16,290.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7975` | 7,460.00 USD | 631,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7980` | 7,260,000.00 USD | 7,260,000.00 USD | 8,320.00 USD | 0.00 USD | 165.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 9,380,000.00 USD | 9,380,000.00 USD | 33,940.00 USD | 3,570.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 40,230.00 USD | 623,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.7990` | 7,250,000.00 USD | 7,250,000.00 USD | 1,600.00 USD | 20,590.00 USD | 18,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7995` | 4,330.00 USD | 583,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8000` | 7,210,000.00 USD | 7,210,000.00 USD | 30,830.00 USD | 10,990.00 USD | 16,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 9,290,000.00 USD | 9,290,000.00 USD | 41,450.00 USD | 16,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8005` | 6,990.00 USD | 579,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8010` | 7,150,000.00 USD | 7,150,000.00 USD | 1,140.00 USD | 3,860.00 USD | 200.14 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8015` | 6,710.00 USD | 572,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8020` | 7,140,000.00 USD | 7,140,000.00 USD | 796.46 USD | 6,400.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 9,230,000.00 USD | 9,230,000.00 USD | 1,890.00 USD | 29,180.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 1,350.00 USD | 565,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8030` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 1,400.00 USD | 159.97 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8035` | 7,680.00 USD | 564,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8040` | 7,130,000.00 USD | 7,130,000.00 USD | 43,320.00 USD | 22,790.00 USD | 21,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8045` | 15,720.00 USD | 556,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8050` | 7,040,000.00 USD | 7,040,000.00 USD | 19,550.00 USD | 7,230.00 USD | 330.63 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8055` | 361.11 USD | 540,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8060` | 7,010,000.00 USD | 7,010,000.00 USD | 32,080.00 USD | 11,640.00 USD | 73,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 9,150,000.00 USD | 9,150,000.00 USD | 12,280.00 USD | 737.70 USD | 1,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8065` | 6,910.00 USD | 540,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8070` | 6,900,000.00 USD | 6,900,000.00 USD | 8,540.00 USD | 14,620.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8075` | 2,770.00 USD | 533,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8080` | 6,870,000.00 USD | 6,870,000.00 USD | 2,530.00 USD | 4,510.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 9,130,000.00 USD | 9,130,000.00 USD | 5,030.00 USD | 11,280.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8085` | 22,170.00 USD | 530,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8090` | 6,860,000.00 USD | 6,860,000.00 USD | 587.71 USD | 5,580.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8095` | 154,810.00 USD | 508,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8100` | 6,850,000.00 USD | 6,850,000.00 USD | 1,830.00 USD | 5,380.00 USD | 248.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 9,110,000.00 USD | 9,110,000.00 USD | 4,310.00 USD | 9,850.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 2,250.00 USD | 353,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8110` | 6,850,000.00 USD | 6,850,000.00 USD | 1,650.00 USD | 2,090.00 USD | 196.09 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8115` | 2,970.00 USD | 351,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8120` | 6,840,000.00 USD | 6,840,000.00 USD | 13,640.00 USD | 780.21 USD | 23,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 9,090,000.00 USD | 9,090,000.00 USD | 73,000.00 USD | 9,210.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8125` | 7,280.00 USD | 348,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8130` | 6,810,000.00 USD | 6,810,000.00 USD | 683.00 USD | 989.28 USD | 706.99 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 3,800.00 USD | 341,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8140` | 6,800,000.00 USD | 6,800,000.00 USD | 14,810.00 USD | 523.16 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8140` | 8,970,000.00 USD | 8,970,000.00 USD | 55,190.00 USD | 31,920.00 USD | 79,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8145` | 277.42 USD | 337,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8150` | 6,780,000.00 USD | 6,780,000.00 USD | 4,970.00 USD | 1,140.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8155` | 2,810.00 USD | 337,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8160` | 6,760,000.00 USD | 6,760,000.00 USD | 17,910.00 USD | 1,970.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 8,800,000.00 USD | 8,800,000.00 USD | 186,980.00 USD | 49,790.00 USD | 146,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8165` | 104.92 USD | 334,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8170` | 6,720,000.00 USD | 6,720,000.00 USD | 56,460.00 USD | 4,990.00 USD | 30,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8175` | 77,840.00 USD | 334,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8180` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 351.95 USD | 213.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 8,420,000.00 USD | 8,420,000.00 USD | 82,600.00 USD | 41,370.00 USD | 43,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8190` | 6,630,000.00 USD | 6,630,000.00 USD | 24,470.00 USD | 1,600.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8195` | 1,720.00 USD | 256,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8200` | 6,590,000.00 USD | 6,590,000.00 USD | 87,930.00 USD | 3,460.00 USD | 73,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 8,250,000.00 USD | 8,250,000.00 USD | 205,920.00 USD | 48,700.00 USD | 97,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8205` | 1,400.00 USD | 254,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8210` | 6,430,000.00 USD | 6,430,000.00 USD | 15,840.00 USD | 83,090.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 474.01 USD | 253,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 6,280,000.00 USD | 6,280,000.00 USD | 59,890.00 USD | 4,310.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8220` | 7,900,000.00 USD | 7,900,000.00 USD | 110,800.00 USD | 74,480.00 USD | 175,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8225` | 1,490.00 USD | 252,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8230` | 6,190,000.00 USD | 6,190,000.00 USD | 9,670.00 USD | 5,770.00 USD | 105,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 1,870.00 USD | 251,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 6,070,000.00 USD | 6,070,000.00 USD | 9,840.00 USD | 2,400.00 USD | 32,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8240` | 7,540,000.00 USD | 7,540,000.00 USD | 109,730.00 USD | 44,640.00 USD | 87,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8245` | 19,580.00 USD | 249,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8250` | 6,030,000.00 USD | 6,030,000.00 USD | 27,470.00 USD | 1,230.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8255` | 1,580.00 USD | 229,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8260` | 5,990,000.00 USD | 5,990,000.00 USD | 19,170.00 USD | 8,970.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 7,300,000.00 USD | 7,300,000.00 USD | 199,800.00 USD | 32,880.00 USD | 111,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8270` | 5,950,000.00 USD | 5,950,000.00 USD | 39,540.00 USD | 22,100.00 USD | 8,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8275` | 4,690.00 USD | 228,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8280` | 5,880,000.00 USD | 5,880,000.00 USD | 1,490.00 USD | 773.90 USD | 313.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 6,950,000.00 USD | 6,950,000.00 USD | 118,780.00 USD | 44,400.00 USD | 87,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8285` | 120,070.00 USD | 223,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8290` | 5,880,000.00 USD | 5,880,000.00 USD | 24,750.00 USD | 11,650.00 USD | 46,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8300` | 5,790,000.00 USD | 5,790,000.00 USD | 3,410.00 USD | 3,180.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 6,700,000.00 USD | 6,700,000.00 USD | 33,770.00 USD | 45,100.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8310` | 5,780,000.00 USD | 5,780,000.00 USD | 2,590.00 USD | 27,590.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 5,730,000.00 USD | 5,730,000.00 USD | 867.90 USD | 10,780.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 6,570,000.00 USD | 6,570,000.00 USD | 90,830.00 USD | 77,110.00 USD | 150,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 5,690,000.00 USD | 5,690,000.00 USD | 7,940.00 USD | 19,140.00 USD | 74,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 5,590,000.00 USD | 5,590,000.00 USD | 142,540.00 USD | 21,960.00 USD | 30,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 6,260,000.00 USD | 6,260,000.00 USD | 114,580.00 USD | 56,360.00 USD | 180,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8345` | 5,750.00 USD | 103,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8350` | 5,390,000.00 USD | 5,390,000.00 USD | 14,620.00 USD | 13,380.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8355` | 117.64 USD | 97,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8360` | 5,370,000.00 USD | 5,370,000.00 USD | 45,630.00 USD | 1,600.00 USD | 397.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 5,910,000.00 USD | 5,910,000.00 USD | 178,100.00 USD | 28,000.00 USD | 99,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8370` | 5,320,000.00 USD | 5,320,000.00 USD | 20,840.00 USD | 10,110.00 USD | 129,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8375` | 327.21 USD | 97,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 5,160,000.00 USD | 5,160,000.00 USD | 35,040.00 USD | 60,090.00 USD | 16,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 5,600,000.00 USD | 5,600,000.00 USD | 69,220.00 USD | 223,030.00 USD | 223,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8385` | 8,240.00 USD | 97,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8390` | 5,050,000.00 USD | 5,050,000.00 USD | 44,740.00 USD | 792.50 USD | 33,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8395` | 834.13 USD | 89,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8400` | 4,970,000.00 USD | 4,970,000.00 USD | 6,260.00 USD | 9,410.00 USD | 22,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 5,080,000.00 USD | 5,080,000.00 USD | 96,040.00 USD | 56,210.00 USD | 61,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 4,930,000.00 USD | 4,930,000.00 USD | 17,400.00 USD | 16,230.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 750.79 USD | 88,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 4,840,000.00 USD | 4,840,000.00 USD | 71,930.00 USD | 48,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 4,870,000.00 USD | 4,870,000.00 USD | 96,530.00 USD | 66,440.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8425` | 11,390.00 USD | 87,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8430` | 4,720,000.00 USD | 4,720,000.00 USD | 17,820.00 USD | 18,730.00 USD | 21,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 103.24 USD | 76,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 4,660,000.00 USD | 4,660,000.00 USD | 49,800.00 USD | 44,320.00 USD | 166.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 4,700,000.00 USD | 4,700,000.00 USD | 28,900.00 USD | 111,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8445` | 803.20 USD | 75,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8450` | 4,570,000.00 USD | 4,570,000.00 USD | 22,880.00 USD | 30,550.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 10,690.00 USD | 75,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8460` | 4,500,000.00 USD | 4,500,000.00 USD | 623.10 USD | 65,890.00 USD | 26,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 4,560,000.00 USD | 4,560,000.00 USD | 52,800.00 USD | 57,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 4,410,000.00 USD | 4,410,000.00 USD | 81,540.00 USD | 39,470.00 USD | 15,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8475` | 1,270.00 USD | 64,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8480` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 36,960.00 USD | 82,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 4,450,000.00 USD | 4,450,000.00 USD | 73,880.00 USD | 61,480.00 USD | 82,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 4,150,000.00 USD | 4,150,000.00 USD | 61,960.00 USD | 61,840.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 6,910.00 USD | 63,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 3,960,000.00 USD | 3,960,000.00 USD | 42,500.00 USD | 37,570.00 USD | 107,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 4,230,000.00 USD | 4,230,000.00 USD | 85,470.00 USD | 58,490.00 USD | 50,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8505` | 13,600.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8510` | 3,770,000.00 USD | 3,770,000.00 USD | 41,500.00 USD | 106,640.00 USD | 49,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 3,580,000.00 USD | 3,580,000.00 USD | 59,930.00 USD | 95,740.00 USD | 88,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 4,030,000.00 USD | 4,030,000.00 USD | 77,320.00 USD | 53,520.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8525` | 42,610.00 USD | 42,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8530` | 3,330,000.00 USD | 3,330,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 104.30 USD | 104.30 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 13,200.00 USD | 128.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 3,850,000.00 USD | 3,850,000.00 USD | 277,690.00 USD | 50,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 3,120,000.00 USD | 3,120,000.00 USD | 1,920.00 USD | 37,290.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 3,070,000.00 USD | 3,070,000.00 USD | 30,660.00 USD | 17,140.00 USD | 52,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 3,520,000.00 USD | 3,520,000.00 USD | 87,380.00 USD | 91,360.00 USD | 33,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 2,970,000.00 USD | 2,970,000.00 USD | 14,730.00 USD | 12,760.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,940,000.00 USD | 2,940,000.00 USD | 32,900.00 USD | 54,050.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 3,310,000.00 USD | 3,310,000.00 USD | 146,570.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 2,820,000.00 USD | 2,820,000.00 USD | 13,810.00 USD | 6,720.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,760,000.00 USD | 2,760,000.00 USD | 75,640.00 USD | 32,480.00 USD | 200.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 3,150,000.00 USD | 3,150,000.00 USD | 38,890.00 USD | 164,470.00 USD | 20,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 2,660,000.00 USD | 2,660,000.00 USD | 21,600.00 USD | 0.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,630,000.00 USD | 2,630,000.00 USD | 42,920.00 USD | 25,800.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 2,920,000.00 USD | 2,920,000.00 USD | 25,100.00 USD | 145,110.00 USD | 394,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 2,530,000.00 USD | 2,530,000.00 USD | 48,390.00 USD | 103,090.00 USD | 113,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,270,000.00 USD | 2,270,000.00 USD | 88,690.00 USD | 54,960.00 USD | 30,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 2,360,000.00 USD | 2,360,000.00 USD | 83,850.00 USD | 0.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8650` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 35,750.00 USD | 136,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,920,000.00 USD | 1,920,000.00 USD | 135,650.00 USD | 13,430.00 USD | 54,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 2,270,000.00 USD | 2,270,000.00 USD | 294,020.00 USD | 122,950.00 USD | 678,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8670` | 1,720,000.00 USD | 1,720,000.00 USD | 114,240.00 USD | 33,880.00 USD | 142,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,430,000.00 USD | 1,430,000.00 USD | 50,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 1,180,000.00 USD | 1,180,000.00 USD | 213,340.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 97,830.00 USD | 31,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 952,500.00 USD | 952,500.00 USD | 0.00 USD | 34,600.00 USD | 111,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,220,000.00 USD | 1,220,000.00 USD | 152,210.00 USD | 62,100.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 855,600.00 USD | 855,600.00 USD | 30,060.00 USD | 26,400.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 806,620.00 USD | 806,620.00 USD | 207,250.00 USD | 101,630.00 USD | 87,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 778,130.00 USD | 778,130.00 USD | 55,600.00 USD | 39,670.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 652,890.00 USD | 652,890.00 USD | 61,330.00 USD | 20,260.00 USD | 39,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 410,210.00 USD | 410,210.00 USD | 9,520.00 USD | 72,100.00 USD | 71,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 531,870.00 USD | 531,870.00 USD | 29,460.00 USD | 0.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 418,910.00 USD | 418,910.00 USD | 0.00 USD | 0.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 256,990.00 USD | 256,990.00 USD | 16,700.00 USD | 29,060.00 USD | 189,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8770` | 365,840.00 USD | 365,840.00 USD | 27,620.00 USD | 20,280.00 USD | 94,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 223,650.00 USD | 223,650.00 USD | 79,990.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 21,780.00 USD | 21,780.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 126,240.00 USD | 126,240.00 USD | 39,180.00 USD | 0.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 74,130.00 USD | 74,130.00 USD | 4,760.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 20,310.00 USD | 20,310.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 68,360.00 USD | 68,360.00 USD | 37,200.00 USD | 0.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8840` | 1,820.00 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8850` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 214.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8860` | 3,150.00 USD | 3,150.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8870` | 4,560.00 USD | 4,560.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8880` | 127,320.00 USD | 127,320.00 USD | 122,200.00 USD | 0.00 USD | 560.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8880` | 3,860.00 USD | 3,860.00 USD | 0.00 USD | 3,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8900` | 130,170.00 USD | 130,170.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8900` | 12,670.00 USD | 12,670.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8910` | 218,370.00 USD | 218,370.00 USD | 87,950.00 USD | 0.00 USD | 251.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8920` | 220,160.00 USD | 220,160.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8920` | 1,520,000.00 USD | 1,520,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8930` | 238,980.00 USD | 238,980.00 USD | 0.00 USD | 18,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8940` | 260,550.00 USD | 260,550.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8940` | 2,790,000.00 USD | 2,790,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8950` | 338,400.00 USD | 338,400.00 USD | 0.00 USD | 77,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8960` | 3,490,000.00 USD | 3,490,000.00 USD | 593,680.00 USD | 107,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8970` | 339,370.00 USD | 339,370.00 USD | 969.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8980` | 473,200.00 USD | 473,200.00 USD | 73,030.00 USD | 60,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.8980` | 4,570,000.00 USD | 4,570,000.00 USD | 615,200.00 USD | 118,950.00 USD | 339,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.8990` | 669,350.00 USD | 669,350.00 USD | 70,970.00 USD | 125,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9000` | 931,600.00 USD | 931,600.00 USD | 226,850.00 USD | 5,150.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9000` | 4,780,000.00 USD | 4,780,000.00 USD | 198,040.00 USD | 16,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9010` | 1,070,000.00 USD | 1,070,000.00 USD | 3,390.00 USD | 107,900.00 USD | 24,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9020` | 1,150,000.00 USD | 1,150,000.00 USD | 28,630.00 USD | 53,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9020` | 5,560,000.00 USD | 5,560,000.00 USD | 85,610.00 USD | 221,330.00 USD | 476,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9030` | 1,310,000.00 USD | 1,310,000.00 USD | 39,620.00 USD | 108,680.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9040` | 1,630,000.00 USD | 1,630,000.00 USD | 175,130.00 USD | 136,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9040` | 6,010,000.00 USD | 6,010,000.00 USD | 223,750.00 USD | 2,890.00 USD | 218,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9050` | 1,790,000.00 USD | 1,790,000.00 USD | 90,340.00 USD | 26,270.00 USD | 44,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9060` | 2,280,000.00 USD | 2,280,000.00 USD | 168,180.00 USD | 158,360.00 USD | 165,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9060` | 6,430,000.00 USD | 6,430,000.00 USD | 286,790.00 USD | 34,600.00 USD | 104,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9070` | 2,660,000.00 USD | 2,660,000.00 USD | 135,160.00 USD | 128,180.00 USD | 115,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9080` | 2,840,000.00 USD | 2,840,000.00 USD | 113,830.00 USD | 45,320.00 USD | 17,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9080` | 7,340,000.00 USD | 7,340,000.00 USD | 389,350.00 USD | 288,590.00 USD | 227,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9090` | 2,990,000.00 USD | 2,990,000.00 USD | 76,970.00 USD | 49,730.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9100` | 3,170,000.00 USD | 3,170,000.00 USD | 83,550.00 USD | 50,130.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9100` | 7,610,000.00 USD | 7,610,000.00 USD | 123,910.00 USD | 78,920.00 USD | 70,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9110` | 3,310,000.00 USD | 3,310,000.00 USD | 97,650.00 USD | 16,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9120` | 3,500,000.00 USD | 3,500,000.00 USD | 32,690.00 USD | 81,230.00 USD | 69,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9120` | 7,910,000.00 USD | 7,910,000.00 USD | 135,210.00 USD | 163,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9130` | 3,660,000.00 USD | 3,660,000.00 USD | 45,950.00 USD | 25,330.00 USD | 92,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9140` | 4,030,000.00 USD | 4,030,000.00 USD | 162,940.00 USD | 61,860.00 USD | 142,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9140` | 8,140,000.00 USD | 8,140,000.00 USD | 143,540.00 USD | 83,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9145` | 4,060.00 USD | 4,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9150` | 4,390,000.00 USD | 4,390,000.00 USD | 109,360.00 USD | 68,860.00 USD | 184,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9160` | 4,600,000.00 USD | 4,600,000.00 USD | 60,590.00 USD | 102,520.00 USD | 52,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9160` | 8,610,000.00 USD | 8,610,000.00 USD | 212,270.00 USD | 84,510.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9170` | 4,810,000.00 USD | 4,810,000.00 USD | 94,070.00 USD | 28,770.00 USD | 82,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9180` | 4,970,000.00 USD | 4,970,000.00 USD | 26,530.00 USD | 60,340.00 USD | 68,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9180` | 8,900,000.00 USD | 8,900,000.00 USD | 38,590.00 USD | 63,520.00 USD | 187,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9190` | 5,090,000.00 USD | 5,090,000.00 USD | 61,810.00 USD | 16,580.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9195` | 9,200.00 USD | 13,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9200` | 5,280,000.00 USD | 5,280,000.00 USD | 72,440.00 USD | 16,940.00 USD | 100,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9200` | 9,490,000.00 USD | 9,490,000.00 USD | 445,890.00 USD | 32,570.00 USD | 114,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9210` | 5,560,000.00 USD | 5,560,000.00 USD | 85,860.00 USD | 61,240.00 USD | 124,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 5,850,000.00 USD | 5,850,000.00 USD | 129,150.00 USD | 32,770.00 USD | 136,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9220` | 9,880,000.00 USD | 9,880,000.00 USD | 6,470.00 USD | 66,370.00 USD | 318,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9230` | 6,170,000.00 USD | 6,170,000.00 USD | 107,110.00 USD | 55,720.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9235` | 209.36 USD | 13,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9240` | 6,480,000.00 USD | 6,480,000.00 USD | 133,310.00 USD | 59,770.00 USD | 117,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9240` | 10,310,000.00 USD | 10,310,000.00 USD | 111,800.00 USD | 62,860.00 USD | 256,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9250` | 6,730,000.00 USD | 6,730,000.00 USD | 133,720.00 USD | 62,290.00 USD | 55,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 6,860,000.00 USD | 6,860,000.00 USD | 6,140.00 USD | 71,670.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9260` | 10,720,000.00 USD | 10,720,000.00 USD | 213,450.00 USD | 99,090.00 USD | 89,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9270` | 6,960,000.00 USD | 6,960,000.00 USD | 9,360.00 USD | 67,290.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 7,100,000.00 USD | 7,100,000.00 USD | 38,960.00 USD | 30,650.00 USD | 68,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9280` | 10,920,000.00 USD | 10,920,000.00 USD | 128,610.00 USD | 43,320.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9285` | 21,060.00 USD | 34,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9290` | 7,200,000.00 USD | 7,200,000.00 USD | 53,450.00 USD | 2,870.00 USD | 44,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9295` | 2,490.00 USD | 37,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9300` | 7,330,000.00 USD | 7,330,000.00 USD | 5,010.00 USD | 59,350.00 USD | 65,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9300` | 11,390,000.00 USD | 11,390,000.00 USD | 186,110.00 USD | 113,080.00 USD | 168,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9310` | 7,510,000.00 USD | 7,510,000.00 USD | 118,420.00 USD | 16,270.00 USD | 36,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 7,640,000.00 USD | 7,640,000.00 USD | 71,540.00 USD | 28,860.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9320` | 11,510,000.00 USD | 11,510,000.00 USD | 4,410.00 USD | 53,880.00 USD | 63,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9330` | 7,690,000.00 USD | 7,690,000.00 USD | 24,270.00 USD | 19,640.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 7,710,000.00 USD | 7,710,000.00 USD | 1,200.00 USD | 16,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9340` | 11,640,000.00 USD | 11,640,000.00 USD | 50,160.00 USD | 78,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9350` | 7,730,000.00 USD | 7,730,000.00 USD | 964.55 USD | 637.37 USD | 19,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9355` | 340.15 USD | 37,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9360` | 7,860,000.00 USD | 7,860,000.00 USD | 48,380.00 USD | 26,000.00 USD | 55,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9360` | 11,780,000.00 USD | 11,780,000.00 USD | 131,450.00 USD | 3,160.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9365` | 478.55 USD | 37,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9370` | 8,130,000.00 USD | 8,130,000.00 USD | 80,470.00 USD | 54,520.00 USD | 135,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9375` | 454.59 USD | 38,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9380` | 8,270,000.00 USD | 8,270,000.00 USD | 15,820.00 USD | 9,200.00 USD | 110,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9380` | 12,140,000.00 USD | 12,140,000.00 USD | 168,030.00 USD | 5,150.00 USD | 179,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9385` | 43,080.00 USD | 81,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9390` | 8,300,000.00 USD | 8,300,000.00 USD | 2,230.00 USD | 3,000.00 USD | 34,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 8,410,000.00 USD | 8,410,000.00 USD | 46,290.00 USD | 2,190.00 USD | 56,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 12,480,000.00 USD | 12,480,000.00 USD | 173,610.00 USD | 39,110.00 USD | 129,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 8,450,000.00 USD | 8,450,000.00 USD | 20,010.00 USD | 15,520.00 USD | 616.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 8,480,000.00 USD | 8,480,000.00 USD | 6,740.00 USD | 1,340.00 USD | 24,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 12,560,000.00 USD | 12,560,000.00 USD | 12,670.00 USD | 32,360.00 USD | 37,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 8,490,000.00 USD | 8,490,000.00 USD | 4,310.00 USD | 2,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 8,560,000.00 USD | 8,560,000.00 USD | 4,930.00 USD | 23,400.00 USD | 46,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 12,790,000.00 USD | 12,790,000.00 USD | 8,820.00 USD | 217,840.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9445` | 103.90 USD | 81,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9450` | 8,670,000.00 USD | 8,670,000.00 USD | 4,850.00 USD | 793.93 USD | 107,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 8,780,000.00 USD | 8,780,000.00 USD | 56,940.00 USD | 26,210.00 USD | 24,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 8,860,000.00 USD | 8,860,000.00 USD | 36,440.00 USD | 24,720.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 9,000,000.00 USD | 9,000,000.00 USD | 55,350.00 USD | 48,320.00 USD | 35,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 78,160.00 USD | 291,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 9,060,000.00 USD | 9,060,000.00 USD | 18,020.00 USD | 14,650.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 9,130,000.00 USD | 9,130,000.00 USD | 7,440.00 USD | 22,120.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 13,770,000.00 USD | 13,770,000.00 USD | 2,840.00 USD | 30,430.00 USD | 375,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 9,340,000.00 USD | 9,340,000.00 USD | 52,590.00 USD | 28,760.00 USD | 128,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 9,430,000.00 USD | 9,430,000.00 USD | 466.70 USD | 155.85 USD | 83,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 87,720.00 USD | 362,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 9,550,000.00 USD | 9,550,000.00 USD | 29,490.00 USD | 27,080.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 9,630,000.00 USD | 9,630,000.00 USD | 27,570.00 USD | 21,440.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 14,290,000.00 USD | 14,290,000.00 USD | 13,570.00 USD | 3,670.00 USD | 60,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 9,690,000.00 USD | 9,690,000.00 USD | 21,030.00 USD | 13,800.00 USD | 24,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 9,750,000.00 USD | 9,750,000.00 USD | 20,640.00 USD | 11,590.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 14,370,000.00 USD | 14,370,000.00 USD | 74,460.00 USD | 3,500.00 USD | 2,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 9,770,000.00 USD | 9,770,000.00 USD | 16,640.00 USD | 2,570.00 USD | 533.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 9,830,000.00 USD | 9,830,000.00 USD | 10,110.00 USD | 42,520.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 15,220,000.00 USD | 15,220,000.00 USD | 846,080.00 USD | 1,220.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 9,890,000.00 USD | 9,890,000.00 USD | 33,840.00 USD | 27,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 10,060,000.00 USD | 10,060,000.00 USD | 69,660.00 USD | 23,730.00 USD | 78,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 15,830,000.00 USD | 15,830,000.00 USD | 358,610.00 USD | 118,450.00 USD | 131,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 10,420,000.00 USD | 10,420,000.00 USD | 137,750.00 USD | 51,970.00 USD | 166,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 10,570,000.00 USD | 10,570,000.00 USD | 129,590.00 USD | 13,840.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 17,370,000.00 USD | 17,370,000.00 USD | 715,790.00 USD | 231,300.00 USD | 588,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 10,770,000.00 USD | 10,770,000.00 USD | 111,830.00 USD | 28,520.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 10,980,000.00 USD | 10,980,000.00 USD | 125,880.00 USD | 39,890.00 USD | 49,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 18,940,000.00 USD | 18,940,000.00 USD | 693,720.00 USD | 366,520.00 USD | 508,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 11,100,000.00 USD | 11,100,000.00 USD | 18,690.00 USD | 72,860.00 USD | 29,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 11,340,000.00 USD | 11,340,000.00 USD | 135,070.00 USD | 55,850.00 USD | 42,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 20,660,000.00 USD | 20,660,000.00 USD | 962,420.00 USD | 245,250.00 USD | 514,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 11,680,000.00 USD | 11,680,000.00 USD | 93,370.00 USD | 53,730.00 USD | 191,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 11,880,000.00 USD | 11,880,000.00 USD | 80,570.00 USD | 13,020.00 USD | 112,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 22,590,000.00 USD | 22,590,000.00 USD | 818,680.00 USD | 625,850.00 USD | 485,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 12,250,000.00 USD | 12,250,000.00 USD | 162,210.00 USD | 72,620.00 USD | 130,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 12,470,000.00 USD | 12,470,000.00 USD | 120,430.00 USD | 39,280.00 USD | 60,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 23,840,000.00 USD | 23,840,000.00 USD | 657,220.00 USD | 324,760.00 USD | 264,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 12,630,000.00 USD | 12,630,000.00 USD | 64,880.00 USD | 27,540.00 USD | 71,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 12,760,000.00 USD | 12,760,000.00 USD | 38,610.00 USD | 36,660.00 USD | 50,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 24,660,000.00 USD | 24,660,000.00 USD | 403,610.00 USD | 197,100.00 USD | 222,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 12,780,000.00 USD | 12,780,000.00 USD | 24,020.00 USD | 1,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 12,850,000.00 USD | 12,850,000.00 USD | 14,950.00 USD | 5,900.00 USD | 47,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 25,240,000.00 USD | 25,240,000.00 USD | 334,930.00 USD | 116,990.00 USD | 124,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9750` | 12,980,000.00 USD | 12,980,000.00 USD | 20,270.00 USD | 28,720.00 USD | 84,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9755` | 3,590.00 USD | 85,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 12,990,000.00 USD | 12,990,000.00 USD | 423.77 USD | 370.46 USD | 154.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 25,970,000.00 USD | 25,970,000.00 USD | 182,900.00 USD | 286,070.00 USD | 265,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 13,040,000.00 USD | 13,040,000.00 USD | 4,370.00 USD | 20,510.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 13,160,000.00 USD | 13,160,000.00 USD | 28,300.00 USD | 21,450.00 USD | 70,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 27,020,000.00 USD | 27,020,000.00 USD | 323,530.00 USD | 211,120.00 USD | 513,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 13,230,000.00 USD | 13,230,000.00 USD | 18,030.00 USD | 15,220.00 USD | 32,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 13,390,000.00 USD | 13,390,000.00 USD | 43,300.00 USD | 32,650.00 USD | 81,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 27,570,000.00 USD | 27,570,000.00 USD | 247,060.00 USD | 66,910.00 USD | 240,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 1,050.00 USD | 86,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9810` | 13,440,000.00 USD | 13,440,000.00 USD | 44,730.00 USD | 4,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 13,470,000.00 USD | 13,470,000.00 USD | 37,830.00 USD | 836.01 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 27,890,000.00 USD | 27,890,000.00 USD | 108,220.00 USD | 68,030.00 USD | 142,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 13,530,000.00 USD | 13,530,000.00 USD | 31,020.00 USD | 21,700.00 USD | 47.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 13,560,000.00 USD | 13,560,000.00 USD | 2,480.00 USD | 22,240.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 28,590,000.00 USD | 28,590,000.00 USD | 397,850.00 USD | 123,740.00 USD | 177,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 13,610,000.00 USD | 13,610,000.00 USD | 19,260.00 USD | 18,260.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 13,660,000.00 USD | 13,660,000.00 USD | 49,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 28,930,000.00 USD | 28,930,000.00 USD | 108,860.00 USD | 154,250.00 USD | 74,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9865` | 365.70 USD | 86,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9880` | 29,240,000.00 USD | 29,240,000.00 USD | 209,770.00 USD | 75,650.00 USD | 26,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9885` | 4,250.00 USD | 90,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9900` | 29,550,000.00 USD | 29,550,000.00 USD | 201,410.00 USD | 100,430.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9915` | 1,570.00 USD | 92,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9920` | 30,000,000.00 USD | 30,000,000.00 USD | 288,210.00 USD | 79,650.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9935` | 139.59 USD | 92,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9940` | 30,470,000.00 USD | 30,470,000.00 USD | 143,340.00 USD | 183,310.00 USD | 146,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 30,930,000.00 USD | 30,930,000.00 USD | 107,780.00 USD | 55,790.00 USD | 291,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 31,370,000.00 USD | 31,370,000.00 USD | 238,490.00 USD | 42,080.00 USD | 163,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 31,590,000.00 USD | 31,590,000.00 USD | 94,210.00 USD | 53,610.00 USD | 65,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 330.29 USD | 92,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,010,000.00 USD | 32,010,000.00 USD | 250,490.00 USD | 49,140.00 USD | 126,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 32,360,000.00 USD | 32,360,000.00 USD | 148,700.00 USD | 47,010.00 USD | 157,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 5,710.00 USD | 98,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.01` | 705.99 USD | 99,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 170.40 USD | 99,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.03` | 11,040.00 USD | 110,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 1,710.00 USD | 112,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 5,880.00 USD | 117,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 597.52 USD | 118,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.05` | 2,390.00 USD | 120,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.06` | 105.65 USD | 121,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.07` | 1,530.00 USD | 122,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 3,580.00 USD | 126,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 5,550.00 USD | 131,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 324.90 USD | 132,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 277.22 USD | 132,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 8,940.00 USD | 141,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 23,310.00 USD | 164,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.13` | 634.09 USD | 165,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 129.88 USD | 165,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.18` | 381.24 USD | 165,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 177.65 USD | 165,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 4,440.00 USD | 170,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 383.01 USD | 170,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.23` | 380.84 USD | 171,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 1,020.00 USD | 172,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 3,930.00 USD | 176,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 2,670.00 USD | 178,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 4,730.00 USD | 183,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,300.00 USD | 185,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.28` | 39,880.00 USD | 225,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 9,850.00 USD | 235,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.29` | 226.80 USD | 235,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.30` | 114.40 USD | 235,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 1,020.00 USD | 236,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 24,040.00 USD | 260,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 7,490.00 USD | 268,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 6,340.00 USD | 274,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.33` | 21,970.00 USD | 296,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,860.00 USD | 303,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.37` | 358,280.00 USD | 661,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.40` | 137.73 USD | 661,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.41` | 4,450.00 USD | 666,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 402.08 USD | 666,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 288.68 USD | 667,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 16,420.00 USD | 683,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 4,020.00 USD | 687,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 152.75 USD | 687,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 9,930.00 USD | 697,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 144.34 USD | 697,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 268,240.00 USD | 966,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 285.21 USD | 966,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,180.00 USD | 967,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 123.81 USD | 967,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,130.00 USD | 968,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,190.00 USD | 970,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 18,490.00 USD | 989,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 21,330.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 4,080.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 3,620.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 39,070.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 171.37 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 150.02 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 487.21 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 205.67 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 9,720.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 226.05 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 912.54 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,080.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 86,430.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 19,920.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 11,350.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,520.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1835` | 4,680,000.00 USD | 0.00 USD | 1,330.00 USD | `-79.19%` | `7,229.50` |
| `Live` | `Long` | `0.1865` | 4,670,000.00 USD | 0.00 USD | 217.89 USD | `-78.85%` | `1,168.30` |
| `Live` | `Long` | `0.1995` | 4,670,000.00 USD | 0.00 USD | 256.00 USD | `-77.38%` | `1,283.20` |
| `Live` | `Long` | `0.2135` | 4,670,000.00 USD | 0.00 USD | 4,040.00 USD | `-75.79%` | `18,919.90` |
| `Live` | `Long` | `0.2305` | 4,670,000.00 USD | 0.00 USD | 493.41 USD | `-73.86%` | `2,140.60` |
| `Live` | `Long` | `0.2325` | 4,670,000.00 USD | 0.00 USD | 102.79 USD | `-73.64%` | `442.10` |
| `Live` | `Long` | `0.2355` | 4,670,000.00 USD | 0.00 USD | 789.66 USD | `-73.30%` | `3,353.10` |
| `Live` | `Long` | `0.2385` | 4,670,000.00 USD | 0.00 USD | 394.86 USD | `-72.96%` | `1,655.60` |
| `Live` | `Long` | `0.2435` | 4,670,000.00 USD | 0.00 USD | 243.50 USD | `-72.39%` | `1,000.00` |
| `Live` | `Long` | `0.2525` | 4,670,000.00 USD | 0.00 USD | 2,250.00 USD | `-71.37%` | `8,897.00` |
| `Live` | `Long` | `0.2545` | 4,670,000.00 USD | 0.00 USD | 3,630.00 USD | `-71.14%` | `14,245.00` |
| `Live` | `Long` | `0.2555` | 4,660,000.00 USD | 0.00 USD | 1,720.00 USD | `-71.03%` | `6,725.00` |
| `Live` | `Long` | `0.2585` | 4,660,000.00 USD | 0.00 USD | 173.82 USD | `-70.69%` | `672.40` |
| `Live` | `Long` | `0.2625` | 4,660,000.00 USD | 0.00 USD | 849.48 USD | `-70.23%` | `3,236.10` |
| `Live` | `Long` | `0.2655` | 4,660,000.00 USD | 0.00 USD | 172.42 USD | `-69.89%` | `649.40` |
| `Live` | `Long` | `0.2685` | 4,660,000.00 USD | 0.00 USD | 2,830.00 USD | `-69.55%` | `10,547.50` |
| `Live` | `Long` | `0.2735` | 4,660,000.00 USD | 0.00 USD | 248.34 USD | `-68.99%` | `908.00` |
| `Live` | `Long` | `0.2745` | 4,660,000.00 USD | 0.00 USD | 1,030.00 USD | `-68.87%` | `3,748.80` |
| `Live` | `Long` | `0.2855` | 4,660,000.00 USD | 0.00 USD | 24,590.00 USD | `-67.63%` | `86,117.40` |
| `Live` | `Long` | `0.2885` | 4,630,000.00 USD | 0.00 USD | 29,070.00 USD | `-67.29%` | `100,768.40` |
| `Live` | `Long` | `0.2915` | 4,600,000.00 USD | 0.00 USD | 159.57 USD | `-66.95%` | `547.40` |
| `Live` | `Long` | `0.2965` | 4,600,000.00 USD | 0.00 USD | 183.30 USD | `-66.38%` | `618.20` |
| `Live` | `Long` | `0.2975` | 4,600,000.00 USD | 0.00 USD | 4,330.00 USD | `-66.27%` | `14,561.30` |
| `Live` | `Long` | `0.2985` | 4,600,000.00 USD | 0.00 USD | 178.23 USD | `-66.15%` | `597.10` |
| `Live` | `Long` | `0.3025` | 4,600,000.00 USD | 0.00 USD | 605.12 USD | `-65.70%` | `2,000.40` |
| `Live` | `Long` | `0.3115` | 4,600,000.00 USD | 0.00 USD | 270.38 USD | `-64.68%` | `868.00` |
| `Live` | `Long` | `0.3205` | 4,600,000.00 USD | 0.00 USD | 131.21 USD | `-63.66%` | `409.40` |
| `Live` | `Long` | `0.3215` | 4,600,000.00 USD | 0.00 USD | 106.38 USD | `-63.54%` | `330.90` |
| `Live` | `Long` | `0.3315` | 4,600,000.00 USD | 0.00 USD | 4,040.00 USD | `-62.41%` | `12,176.00` |
| `Live` | `Long` | `0.3405` | 4,590,000.00 USD | 0.00 USD | 3,410.00 USD | `-61.39%` | `10,000.00` |
| `Live` | `Long` | `0.3465` | 4,590,000.00 USD | 0.00 USD | 1,230.00 USD | `-60.71%` | `3,555.40` |
| `Live` | `Long` | `0.3475` | 4,590,000.00 USD | 0.00 USD | 3,850.00 USD | `-60.60%` | `11,077.80` |
| `Live` | `Long` | `0.3495` | 4,580,000.00 USD | 0.00 USD | 37,110.00 USD | `-60.37%` | `106,186.60` |
| `Live` | `Long` | `0.3505` | 4,550,000.00 USD | 0.00 USD | 1,020.00 USD | `-60.26%` | `2,908.00` |
| `Live` | `Long` | `0.3585` | 4,540,000.00 USD | 0.00 USD | 595.72 USD | `-59.35%` | `1,661.70` |
| `Live` | `Long` | `0.3665` | 4,540,000.00 USD | 0.00 USD | 274.88 USD | `-58.44%` | `750.00` |
| `Live` | `Long` | `0.3675` | 4,540,000.00 USD | 0.00 USD | 6,240.00 USD | `-58.33%` | `16,991.10` |
| `Live` | `Long` | `0.3745` | 4,540,000.00 USD | 0.00 USD | 6,370.00 USD | `-57.53%` | `17,000.00` |
| `Live` | `Long` | `0.3795` | 4,530,000.00 USD | 0.00 USD | 278.02 USD | `-56.97%` | `732.60` |
| `Live` | `Long` | `0.3825` | 4,530,000.00 USD | 0.00 USD | 2,100.00 USD | `-56.63%` | `5,481.20` |
| `Live` | `Long` | `0.3845` | 4,530,000.00 USD | 0.00 USD | 1,750.00 USD | `-56.40%` | `4,562.20` |
| `Live` | `Long` | `0.3855` | 4,530,000.00 USD | 0.00 USD | 429.87 USD | `-56.29%` | `1,115.10` |
| `Live` | `Long` | `0.3865` | 4,530,000.00 USD | 0.00 USD | 270.55 USD | `-56.17%` | `700.00` |
| `Live` | `Long` | `0.3875` | 4,530,000.00 USD | 0.00 USD | 4,820.00 USD | `-56.06%` | `12,426.00` |
| `Live` | `Long` | `0.3895` | 4,520,000.00 USD | 0.00 USD | 2,980.00 USD | `-55.83%` | `7,661.70` |
| `Live` | `Long` | `0.3925` | 4,520,000.00 USD | 0.00 USD | 5,030.00 USD | `-55.49%` | `12,808.60` |
| `Live` | `Long` | `0.3945` | 4,510,000.00 USD | 0.00 USD | 754.48 USD | `-55.27%` | `1,912.50` |
| `Live` | `Long` | `0.4035` | 4,510,000.00 USD | 0.00 USD | 935.03 USD | `-54.25%` | `2,317.30` |
| `Live` | `Long` | `0.4045` | 4,510,000.00 USD | 0.00 USD | 5,520.00 USD | `-54.13%` | `13,640.50` |
| `Live` | `Long` | `0.4065` | 4,510,000.00 USD | 0.00 USD | 3,360.00 USD | `-53.91%` | `8,275.50` |
| `Live` | `Long` | `0.4095` | 4,500,000.00 USD | 0.00 USD | 28,670.00 USD | `-53.57%` | `70,000.00` |
| `Live` | `Long` | `0.4215` | 4,470,000.00 USD | 0.00 USD | 3,930.00 USD | `-52.20%` | `9,320.00` |
| `Live` | `Long` | `0.4225` | 4,470,000.00 USD | 0.00 USD | 5,280.00 USD | `-52.09%` | `12,500.00` |
| `Live` | `Long` | `0.4245` | 4,470,000.00 USD | 0.00 USD | 468.61 USD | `-51.86%` | `1,103.90` |
| `Live` | `Long` | `0.4255` | 4,460,000.00 USD | 0.00 USD | 8,510.00 USD | `-51.75%` | `20,000.00` |
| `Live` | `Long` | `0.4345` | 4,460,000.00 USD | 0.00 USD | 765.59 USD | `-50.73%` | `1,762.00` |
| `Live` | `Long` | `0.4385` | 4,460,000.00 USD | 0.00 USD | 122.91 USD | `-50.28%` | `280.30` |
| `Live` | `Long` | `0.4425` | 4,460,000.00 USD | 0.00 USD | 44,080.00 USD | `-49.82%` | `99,611.70` |
| `Live` | `Long` | `0.4435` | 4,410,000.00 USD | 0.00 USD | 219.00 USD | `-49.71%` | `493.80` |
| `Live` | `Long` | `0.4455` | 4,410,000.00 USD | 0.00 USD | 574.83 USD | `-49.48%` | `1,290.30` |
| `Live` | `Long` | `0.4465` | 4,410,000.00 USD | 0.00 USD | 19,600.00 USD | `-49.37%` | `43,906.00` |
| `Live` | `Long` | `0.4475` | 4,390,000.00 USD | 0.00 USD | 105.25 USD | `-49.26%` | `235.20` |
| `Live` | `Long` | `0.4505` | 4,390,000.00 USD | 0.00 USD | 816.71 USD | `-48.92%` | `1,812.90` |
| `Live` | `Long` | `0.4535` | 4,390,000.00 USD | 0.00 USD | 1,020.00 USD | `-48.58%` | `2,246.80` |
| `Live` | `Long` | `0.4545` | 4,390,000.00 USD | 0.00 USD | 318.15 USD | `-48.46%` | `700.00` |
| `Live` | `Long` | `0.4595` | 4,390,000.00 USD | 0.00 USD | 3,330.00 USD | `-47.90%` | `7,245.50` |
| `Live` | `Long` | `0.4655` | 4,390,000.00 USD | 0.00 USD | 394.65 USD | `-47.22%` | `847.80` |
| `Live` | `Long` | `0.4695` | 4,390,000.00 USD | 0.00 USD | 221.37 USD | `-46.76%` | `471.50` |
| `Live` | `Long` | `0.4705` | 4,380,000.00 USD | 0.00 USD | 9,230.00 USD | `-46.65%` | `19,627.90` |
| `Live` | `Long` | `0.4765` | 4,380,000.00 USD | 0.00 USD | 111.36 USD | `-45.97%` | `233.70` |
| `Live` | `Long` | `0.4775` | 4,380,000.00 USD | 0.00 USD | 160.63 USD | `-45.85%` | `336.40` |
| `Live` | `Long` | `0.4785` | 4,380,000.00 USD | 0.00 USD | 110.10 USD | `-45.74%` | `230.10` |
| `Live` | `Long` | `0.4825` | 4,380,000.00 USD | 0.00 USD | 166.70 USD | `-45.29%` | `345.50` |
| `Live` | `Long` | `0.4835` | 4,380,000.00 USD | 0.00 USD | 174.01 USD | `-45.17%` | `359.90` |
| `Live` | `Long` | `0.4845` | 4,370,000.00 USD | 0.00 USD | 3,540.00 USD | `-45.06%` | `7,307.20` |
| `Live` | `Long` | `0.4865` | 4,370,000.00 USD | 0.00 USD | 201.07 USD | `-44.83%` | `413.30` |
| `Live` | `Long` | `0.4895` | 4,370,000.00 USD | 0.00 USD | 105.34 USD | `-44.49%` | `215.20` |
| `Live` | `Long` | `0.4915` | 4,370,000.00 USD | 0.00 USD | 2,380.00 USD | `-44.27%` | `4,848.70` |
| `Live` | `Long` | `0.4925` | 4,370,000.00 USD | 0.00 USD | 544.71 USD | `-44.15%` | `1,106.00` |
| `Live` | `Long` | `0.4945` | 4,370,000.00 USD | 0.00 USD | 106.32 USD | `-43.93%` | `215.00` |
| `Live` | `Long` | `0.4955` | 4,370,000.00 USD | 0.00 USD | 211.88 USD | `-43.81%` | `427.60` |
| `Live` | `Long` | `0.4975` | 4,370,000.00 USD | 0.00 USD | 5,620.00 USD | `-43.59%` | `11,290.30` |
| `Live` | `Long` | `0.4985` | 4,360,000.00 USD | 0.00 USD | 216.75 USD | `-43.47%` | `434.80` |
| `Live` | `Long` | `0.5015` | 4,360,000.00 USD | 0.00 USD | 212.49 USD | `-43.13%` | `423.70` |
| `Live` | `Long` | `0.5025` | 4,360,000.00 USD | 0.00 USD | 1,230.00 USD | `-43.02%` | `2,451.10` |
| `Live` | `Long` | `0.5055` | 4,360,000.00 USD | 0.00 USD | 211.25 USD | `-42.68%` | `417.90` |
| `Live` | `Long` | `0.5085` | 4,360,000.00 USD | 0.00 USD | 12,570.00 USD | `-42.34%` | `24,715.80` |
| `Live` | `Long` | `0.5095` | 4,350,000.00 USD | 0.00 USD | 195.75 USD | `-42.23%` | `384.20` |
| `Live` | `Long` | `0.5105` | 4,350,000.00 USD | 0.00 USD | 4,850.00 USD | `-42.11%` | `9,500.00` |
| `Live` | `Long` | `0.5145` | 4,340,000.00 USD | 0.00 USD | 1,570.00 USD | `-41.66%` | `3,043.40` |
| `Live` | `Long` | `0.5155` | 4,340,000.00 USD | 0.00 USD | 106.04 USD | `-41.55%` | `205.70` |
| `Live` | `Long` | `0.5165` | 4,340,000.00 USD | 0.00 USD | 619.80 USD | `-41.43%` | `1,200.00` |
| `Live` | `Long` | `0.5175` | 4,340,000.00 USD | 0.00 USD | 213.68 USD | `-41.32%` | `412.90` |
| `Live` | `Long` | `0.5185` | 4,340,000.00 USD | 0.00 USD | 982.56 USD | `-41.21%` | `1,895.00` |
| `Live` | `Long` | `0.5235` | 4,340,000.00 USD | 0.00 USD | 124.02 USD | `-40.64%` | `236.90` |
| `Live` | `Long` | `0.5245` | 4,340,000.00 USD | 0.00 USD | 277.57 USD | `-40.52%` | `529.20` |
| `Live` | `Long` | `0.5265` | 4,340,000.00 USD | 0.00 USD | 553.93 USD | `-40.30%` | `1,052.10` |
| `Live` | `Long` | `0.5275` | 4,340,000.00 USD | 0.00 USD | 348.36 USD | `-40.18%` | `660.40` |
| `Live` | `Long` | `0.5285` | 4,340,000.00 USD | 0.00 USD | 276.72 USD | `-40.07%` | `523.60` |
| `Live` | `Long` | `0.5295` | 4,340,000.00 USD | 0.00 USD | 123,370.00 USD | `-39.96%` | `233,000.00` |
| `Live` | `Long` | `0.5305` | 4,210,000.00 USD | 0.00 USD | 264.56 USD | `-39.84%` | `498.70` |
| `Live` | `Long` | `0.5315` | 4,210,000.00 USD | 0.00 USD | 7,760.00 USD | `-39.73%` | `14,603.90` |
| `Live` | `Long` | `0.5325` | 4,210,000.00 USD | 0.00 USD | 2,790.00 USD | `-39.62%` | `5,239.40` |
| `Live` | `Long` | `0.5355` | 4,200,000.00 USD | 0.00 USD | 113.47 USD | `-39.28%` | `211.90` |
| `Live` | `Long` | `0.5375` | 4,200,000.00 USD | 0.00 USD | 1,480.00 USD | `-39.05%` | `2,751.80` |
| `Live` | `Long` | `0.5395` | 4,200,000.00 USD | 0.00 USD | 126.46 USD | `-38.82%` | `234.40` |
| `Live` | `Long` | `0.5405` | 4,200,000.00 USD | 0.00 USD | 7,090.00 USD | `-38.71%` | `13,118.90` |
| `Live` | `Long` | `0.5425` | 4,190,000.00 USD | 0.00 USD | 269.13 USD | `-38.48%` | `496.10` |
| `Live` | `Long` | `0.5445` | 4,190,000.00 USD | 0.00 USD | 230.32 USD | `-38.26%` | `423.00` |
| `Live` | `Long` | `0.5465` | 4,190,000.00 USD | 0.00 USD | 272.87 USD | `-38.03%` | `499.30` |
| `Live` | `Long` | `0.5475` | 4,190,000.00 USD | 0.00 USD | 1,240.00 USD | `-37.92%` | `2,257.90` |
| `Live` | `Long` | `0.5495` | 4,190,000.00 USD | 0.00 USD | 1,310.00 USD | `-37.69%` | `2,392.10` |
| `Live` | `Long` | `0.5505` | 4,190,000.00 USD | 0.00 USD | 27,770.00 USD | `-37.58%` | `50,450.60` |
| `Live` | `Long` | `0.5515` | 4,160,000.00 USD | 0.00 USD | 160.93 USD | `-37.46%` | `291.80` |
| `Live` | `Long` | `0.5525` | 4,160,000.00 USD | 0.00 USD | 582.56 USD | `-37.35%` | `1,054.40` |
| `Live` | `Long` | `0.5535` | 4,160,000.00 USD | 0.00 USD | 271.88 USD | `-37.24%` | `491.20` |
| `Live` | `Long` | `0.5545` | 4,160,000.00 USD | 0.00 USD | 6,550.00 USD | `-37.12%` | `11,821.40` |
| `Live` | `Long` | `0.5555` | 4,160,000.00 USD | 0.00 USD | 7,950.00 USD | `-37.01%` | `14,310.10` |
| `Live` | `Long` | `0.5585` | 4,150,000.00 USD | 0.00 USD | 141.97 USD | `-36.67%` | `254.20` |
| `Live` | `Long` | `0.5595` | 4,150,000.00 USD | 0.00 USD | 304.93 USD | `-36.56%` | `545.00` |
| `Live` | `Long` | `0.5615` | 4,150,000.00 USD | 0.00 USD | 442.63 USD | `-36.33%` | `788.30` |
| `Live` | `Long` | `0.5625` | 4,150,000.00 USD | 0.00 USD | 468.45 USD | `-36.22%` | `832.80` |
| `Live` | `Long` | `0.5635` | 4,150,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.10%` | `2,623.90` |
| `Live` | `Long` | `0.5655` | 4,150,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.88%` | `14,484.70` |
| `Live` | `Long` | `0.5665` | 4,140,000.00 USD | 0.00 USD | 7,200.00 USD | `-35.76%` | `12,714.00` |
| `Live` | `Long` | `0.5675` | 4,130,000.00 USD | 0.00 USD | 1,560.00 USD | `-35.65%` | `2,747.00` |
| `Live` | `Long` | `0.5695` | 4,130,000.00 USD | 0.00 USD | 973.22 USD | `-35.42%` | `1,708.90` |
| `Live` | `Long` | `0.5725` | 4,130,000.00 USD | 0.00 USD | 139.23 USD | `-35.08%` | `243.20` |
| `Live` | `Long` | `0.5735` | 4,130,000.00 USD | 0.00 USD | 109,930.00 USD | `-34.97%` | `191,690.40` |
| `Live` | `Long` | `0.5745` | 4,020,000.00 USD | 0.00 USD | 144.03 USD | `-34.86%` | `250.70` |
| `Live` | `Long` | `0.5755` | 4,020,000.00 USD | 0.00 USD | 217.37 USD | `-34.74%` | `377.70` |
| `Live` | `Long` | `0.5765` | 4,020,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.63%` | `1,994.20` |
| `Live` | `Long` | `0.5775` | 4,020,000.00 USD | 0.00 USD | 841.01 USD | `-34.51%` | `1,456.30` |
| `Live` | `Long` | `0.5795` | 4,010,000.00 USD | 0.00 USD | 212.85 USD | `-34.29%` | `367.30` |
| `Live` | `Long` | `0.5805` | 4,010,000.00 USD | 0.00 USD | 82,680.00 USD | `-34.17%` | `142,422.00` |
| `Live` | `Long` | `0.5825` | 3,930,000.00 USD | 0.00 USD | 6,470.00 USD | `-33.95%` | `11,099.00` |
| `Live` | `Long` | `0.5835` | 3,930,000.00 USD | 0.00 USD | 6,300.00 USD | `-33.83%` | `10,805.30` |
| `Live` | `Long` | `0.5845` | 3,920,000.00 USD | 0.00 USD | 584.50 USD | `-33.72%` | `1,000.00` |
| `Live` | `Long` | `0.5855` | 3,920,000.00 USD | 0.00 USD | 2,280.00 USD | `-33.61%` | `3,901.10` |
| `Live` | `Long` | `0.5865` | 3,920,000.00 USD | 0.00 USD | 822.98 USD | `-33.49%` | `1,403.20` |
| `Live` | `Long` | `0.5885` | 3,920,000.00 USD | 0.00 USD | 311.14 USD | `-33.27%` | `528.70` |
| `Live` | `Long` | `0.5905` | 3,920,000.00 USD | 0.00 USD | 225.93 USD | `-33.04%` | `382.60` |
| `Live` | `Long` | `0.5925` | 3,910,000.00 USD | 0.00 USD | 273.68 USD | `-32.81%` | `461.90` |
| `Live` | `Long` | `0.5935` | 3,910,000.00 USD | 0.00 USD | 1,130.00 USD | `-32.70%` | `1,901.00` |
| `Live` | `Long` | `0.5945` | 3,910,000.00 USD | 0.00 USD | 8,220.00 USD | `-32.59%` | `13,833.50` |
| `Live` | `Long` | `0.5965` | 3,910,000.00 USD | 0.00 USD | 1,330.00 USD | `-32.36%` | `2,225.40` |
| `Live` | `Long` | `0.5975` | 3,900,000.00 USD | 0.00 USD | 3,420.00 USD | `-32.25%` | `5,729.40` |
| `Live` | `Long` | `0.5985` | 3,900,000.00 USD | 0.00 USD | 299.25 USD | `-32.13%` | `500.00` |
| `Live` | `Long` | `0.5995` | 3,900,000.00 USD | 0.00 USD | 4,610.00 USD | `-32.02%` | `7,683.30` |
| `Live` | `Long` | `0.6005` | 3,900,000.00 USD | 0.00 USD | 351.11 USD | `-31.91%` | `584.70` |
| `Live` | `Long` | `0.6015` | 3,900,000.00 USD | 0.00 USD | 323.79 USD | `-31.79%` | `538.30` |
| `Live` | `Long` | `0.6025` | 3,890,000.00 USD | 0.00 USD | 432.35 USD | `-31.68%` | `717.60` |
| `Live` | `Long` | `0.6075` | 3,890,000.00 USD | 0.00 USD | 851.05 USD | `-31.11%` | `1,400.90` |
| `Live` | `Long` | `0.6085` | 3,890,000.00 USD | 0.00 USD | 3,620.00 USD | `-31.00%` | `5,956.20` |
| `Live` | `Long` | `0.6095` | 3,890,000.00 USD | 0.00 USD | 214.54 USD | `-30.89%` | `352.00` |
| `Live` | `Long` | `0.6115` | 3,890,000.00 USD | 0.00 USD | 6,280.00 USD | `-30.66%` | `10,277.40` |
| `Live` | `Long` | `0.6125` | 3,880,000.00 USD | 0.00 USD | 438.73 USD | `-30.55%` | `716.30` |
| `Live` | `Long` | `0.6145` | 3,880,000.00 USD | 0.00 USD | 2,220.00 USD | `-30.32%` | `3,618.10` |
| `Live` | `Long` | `0.6155` | 3,880,000.00 USD | 0.00 USD | 935.13 USD | `-30.21%` | `1,519.30` |
| `Live` | `Long` | `0.6165` | 3,880,000.00 USD | 0.00 USD | 29,900.00 USD | `-30.09%` | `48,503.10` |
| `Live` | `Long` | `0.6175` | 3,850,000.00 USD | 0.00 USD | 4,980.00 USD | `-29.98%` | `8,064.80` |
| `Live` | `Long` | `0.6185` | 3,850,000.00 USD | 0.00 USD | 12,570.00 USD | `-29.87%` | `20,327.90` |
| `Live` | `Long` | `0.6195` | 3,830,000.00 USD | 0.00 USD | 2,400.00 USD | `-29.75%` | `3,868.00` |
| `Live` | `Long` | `0.6225` | 3,830,000.00 USD | 0.00 USD | 708.53 USD | `-29.41%` | `1,138.20` |
| `Live` | `Long` | `0.6245` | 3,830,000.00 USD | 0.00 USD | 356.65 USD | `-29.19%` | `571.10` |
| `Live` | `Long` | `0.6255` | 3,830,000.00 USD | 0.00 USD | 33,460.00 USD | `-29.07%` | `53,492.10` |
| `Live` | `Long` | `0.6285` | 3,800,000.00 USD | 0.00 USD | 102.45 USD | `-28.73%` | `163.00` |
| `Live` | `Long` | `0.6295` | 3,800,000.00 USD | 0.00 USD | 1,100.00 USD | `-28.62%` | `1,739.60` |
| `Live` | `Long` | `0.6305` | 3,790,000.00 USD | 0.00 USD | 319.35 USD | `-28.51%` | `506.50` |
| `Live` | `Long` | `0.6345` | 3,790,000.00 USD | 0.00 USD | 947.69 USD | `-28.05%` | `1,493.60` |
| `Live` | `Long` | `0.6355` | 3,790,000.00 USD | 0.00 USD | 14,700.00 USD | `-27.94%` | `23,124.30` |
| `Live` | `Long` | `0.6365` | 3,780,000.00 USD | 0.00 USD | 3,060.00 USD | `-27.82%` | `4,804.70` |
| `Live` | `Long` | `0.6375` | 3,780,000.00 USD | 0.00 USD | 1,100.00 USD | `-27.71%` | `1,726.70` |
| `Live` | `Long` | `0.6385` | 3,770,000.00 USD | 0.00 USD | 2,200.00 USD | `-27.60%` | `3,440.40` |
| `Live` | `Long` | `0.6405` | 3,770,000.00 USD | 0.00 USD | 34,650.00 USD | `-27.37%` | `54,099.10` |
| `Live` | `Long` | `0.6415` | 3,740,000.00 USD | 0.00 USD | 86,920.00 USD | `-27.26%` | `135,497.00` |
| `Live` | `Long` | `0.6425` | 3,650,000.00 USD | 0.00 USD | 477.63 USD | `-27.14%` | `743.40` |
| `Live` | `Long` | `0.6435` | 3,650,000.00 USD | 0.00 USD | 3,190.00 USD | `-27.03%` | `4,951.30` |
| `Live` | `Long` | `0.6445` | 3,650,000.00 USD | 0.00 USD | 65,790.00 USD | `-26.92%` | `102,072.40` |
| `Live` | `Long` | `0.6455` | 3,580,000.00 USD | 0.00 USD | 14,590.00 USD | `-26.80%` | `22,595.00` |
| `Live` | `Long` | `0.6465` | 3,570,000.00 USD | 0.00 USD | 146.76 USD | `-26.69%` | `227.00` |
| `Live` | `Long` | `0.6475` | 3,570,000.00 USD | 0.00 USD | 2,810.00 USD | `-26.58%` | `4,340.10` |
| `Live` | `Long` | `0.6485` | 3,560,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.46%` | `1,635.60` |
| `Live` | `Long` | `0.6495` | 3,560,000.00 USD | 0.00 USD | 344.82 USD | `-26.35%` | `530.90` |
| `Live` | `Long` | `0.6505` | 3,560,000.00 USD | 0.00 USD | 106.75 USD | `-26.24%` | `164.10` |
| `Live` | `Long` | `0.6515` | 3,560,000.00 USD | 0.00 USD | 403,320.00 USD | `-26.12%` | `619,065.10` |
| `Live` | `Long` | `0.6525` | 3,160,000.00 USD | 0.00 USD | 2,350.00 USD | `-26.01%` | `3,599.00` |
| `Live` | `Long` | `0.6535` | 3,160,000.00 USD | 0.00 USD | 2,840.00 USD | `-25.90%` | `4,345.80` |
| `Live` | `Long` | `0.6545` | 3,150,000.00 USD | 0.00 USD | 7,850.00 USD | `-25.78%` | `11,993.00` |
| `Live` | `Long` | `0.6555` | 3,150,000.00 USD | 0.00 USD | 676.54 USD | `-25.67%` | `1,032.10` |
| `Live` | `Long` | `0.6565` | 3,140,000.00 USD | 0.00 USD | 7,400.00 USD | `-25.56%` | `11,267.10` |
| `Live` | `Long` | `0.6575` | 3,140,000.00 USD | 0.00 USD | 130.91 USD | `-25.44%` | `199.10` |
| `Live` | `Long` | `0.6585` | 3,140,000.00 USD | 0.00 USD | 20,750.00 USD | `-25.33%` | `31,515.10` |
| `Live` | `Long` | `0.6595` | 3,120,000.00 USD | 0.00 USD | 1,060.00 USD | `-25.22%` | `1,611.70` |
| `Live` | `Long` | `0.6615` | 3,120,000.00 USD | 0.00 USD | 4,960.00 USD | `-24.99%` | `7,503.30` |
| `Live` | `Long` | `0.6625` | 3,110,000.00 USD | 0.00 USD | 4,050.00 USD | `-24.88%` | `6,115.90` |
| `Live` | `Long` | `0.6645` | 3,110,000.00 USD | 0.00 USD | 448.54 USD | `-24.65%` | `675.00` |
| `Live` | `Long` | `0.6655` | 3,110,000.00 USD | 0.00 USD | 1,220.00 USD | `-24.54%` | `1,827.00` |
| `Live` | `Long` | `0.6665` | 3,100,000.00 USD | 0.00 USD | 528.73 USD | `-24.42%` | `793.30` |
| `Live` | `Long` | `0.6675` | 3,100,000.00 USD | 0.00 USD | 2,260.00 USD | `-24.31%` | `3,386.00` |
| `Live` | `Long` | `0.6685` | 3,100,000.00 USD | 0.00 USD | 5,470.00 USD | `-24.20%` | `8,188.90` |
| `Live` | `Long` | `0.6705` | 3,100,000.00 USD | 0.00 USD | 2,830.00 USD | `-23.97%` | `4,215.40` |
| `Live` | `Long` | `0.6715` | 3,090,000.00 USD | 0.00 USD | 2,240.00 USD | `-23.86%` | `3,341.20` |
| `Live` | `Long` | `0.6725` | 3,090,000.00 USD | 0.00 USD | 8,140.00 USD | `-23.74%` | `12,106.60` |
| `Live` | `Long` | `0.6735` | 3,080,000.00 USD | 0.00 USD | 633.09 USD | `-23.63%` | `940.00` |
| `Live` | `Long` | `0.6745` | 3,080,000.00 USD | 0.00 USD | 33,610.00 USD | `-23.52%` | `49,828.00` |
| `Live` | `Long` | `0.6755` | 3,050,000.00 USD | 0.00 USD | 111.59 USD | `-23.40%` | `165.20` |
| `Live` | `Long` | `0.6765` | 3,050,000.00 USD | 0.00 USD | 744.15 USD | `-23.29%` | `1,100.00` |
| `Live` | `Long` | `0.6775` | 3,050,000.00 USD | 0.00 USD | 2,650.00 USD | `-23.18%` | `3,908.00` |
| `Live` | `Long` | `0.6785` | 3,050,000.00 USD | 0.00 USD | 122.94 USD | `-23.06%` | `181.20` |
| `Live` | `Long` | `0.6795` | 3,050,000.00 USD | 0.00 USD | 39,510.00 USD | `-22.95%` | `58,139.50` |
| `Live` | `Long` | `0.6805` | 3,010,000.00 USD | 0.00 USD | 4,150.00 USD | `-22.84%` | `6,099.00` |
| `Live` | `Long` | `0.6825` | 3,000,000.00 USD | 0.00 USD | 19,300.00 USD | `-22.61%` | `28,284.70` |
| `Live` | `Long` | `0.6835` | 2,980,000.00 USD | 0.00 USD | 11,170.00 USD | `-22.50%` | `16,336.60` |
| `Live` | `Long` | `0.6845` | 2,970,000.00 USD | 0.00 USD | 5,960.00 USD | `-22.38%` | `8,711.60` |
| `Live` | `Long` | `0.6865` | 2,970,000.00 USD | 0.00 USD | 112.59 USD | `-22.15%` | `164.00` |
| `Live` | `Long` | `0.6875` | 2,970,000.00 USD | 0.00 USD | 6,110.00 USD | `-22.04%` | `8,883.90` |
| `Live` | `Long` | `0.6885` | 2,960,000.00 USD | 0.00 USD | 344.25 USD | `-21.93%` | `500.00` |
| `Live` | `Long` | `0.6895` | 2,960,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.81%` | `3,065.00` |
| `Live` | `Long` | `0.6905` | 2,960,000.00 USD | 0.00 USD | 3,360.00 USD | `-21.70%` | `4,864.60` |
| `Live` | `Long` | `0.6915` | 2,950,000.00 USD | 0.00 USD | 8,970.00 USD | `-21.59%` | `12,967.20` |
| `Live` | `Long` | `0.6935` | 2,940,000.00 USD | 0.00 USD | 3,600.00 USD | `-21.36%` | `5,196.70` |
| `Live` | `Long` | `0.6945` | 2,940,000.00 USD | 0.00 USD | 722.28 USD | `-21.25%` | `1,040.00` |
| `Live` | `Long` | `0.6955` | 2,940,000.00 USD | 0.00 USD | 1,700.00 USD | `-21.13%` | `2,448.00` |
| `Live` | `Long` | `0.6965` | 2,940,000.00 USD | 0.00 USD | 273.03 USD | `-21.02%` | `392.00` |
| `Live` | `Long` | `0.6975` | 2,940,000.00 USD | 0.00 USD | 1,030.00 USD | `-20.91%` | `1,482.80` |
| `Live` | `Long` | `0.6985` | 2,940,000.00 USD | 0.00 USD | 5,130.00 USD | `-20.79%` | `7,342.20` |
| `Live` | `Long` | `0.7005` | 2,930,000.00 USD | 0.00 USD | 235.37 USD | `-20.57%` | `336.00` |
| `Live` | `Long` | `0.7015` | 2,930,000.00 USD | 0.00 USD | 1,990.00 USD | `-20.45%` | `2,841.50` |
| `Live` | `Long` | `0.7025` | 2,930,000.00 USD | 0.00 USD | 39,470.00 USD | `-20.34%` | `56,186.20` |
| `Live` | `Long` | `0.7045` | 2,890,000.00 USD | 0.00 USD | 8,970.00 USD | `-20.11%` | `12,729.60` |
| `Live` | `Long` | `0.7055` | 2,880,000.00 USD | 0.00 USD | 141.38 USD | `-20.00%` | `200.40` |
| `Live` | `Long` | `0.7065` | 2,880,000.00 USD | 0.00 USD | 143.14 USD | `-19.89%` | `202.60` |
| `Live` | `Long` | `0.7075` | 2,880,000.00 USD | 0.00 USD | 1,560.00 USD | `-19.77%` | `2,202.70` |
| `Live` | `Long` | `0.7085` | 2,880,000.00 USD | 0.00 USD | 2,020.00 USD | `-19.66%` | `2,848.30` |
| `Live` | `Long` | `0.7095` | 2,880,000.00 USD | 0.00 USD | 1,140.00 USD | `-19.55%` | `1,603.50` |
| `Live` | `Long` | `0.7105` | 2,880,000.00 USD | 0.00 USD | 4,190.00 USD | `-19.43%` | `5,890.40` |
| `Live` | `Long` | `0.7115` | 2,870,000.00 USD | 0.00 USD | 198.58 USD | `-19.32%` | `279.10` |
| `Live` | `Long` | `0.7125` | 2,870,000.00 USD | 0.00 USD | 283.22 USD | `-19.21%` | `397.50` |
| `Live` | `Long` | `0.7135` | 2,870,000.00 USD | 0.00 USD | 927.55 USD | `-19.09%` | `1,300.00` |
| `Live` | `Long` | `0.7155` | 2,870,000.00 USD | 0.00 USD | 11,030.00 USD | `-18.87%` | `15,416.10` |
| `Live` | `Long` | `0.7165` | 2,860,000.00 USD | 0.00 USD | 4,620.00 USD | `-18.75%` | `6,444.00` |
| `Live` | `Long` | `0.7185` | 2,860,000.00 USD | 0.00 USD | 126.96 USD | `-18.53%` | `176.70` |
| `Live` | `Long` | `0.7195` | 2,850,000.00 USD | 0.00 USD | 420.19 USD | `-18.41%` | `584.00` |
| `Live` | `Long` | `0.7215` | 2,850,000.00 USD | 0.00 USD | 8,970.00 USD | `-18.19%` | `12,429.90` |
| `Live` | `Long` | `0.7225` | 2,850,000.00 USD | 0.00 USD | 1,420.00 USD | `-18.07%` | `1,965.70` |
| `Live` | `Long` | `0.7235` | 2,840,000.00 USD | 0.00 USD | 127.05 USD | `-17.96%` | `175.60` |
| `Live` | `Long` | `0.7245` | 2,840,000.00 USD | 0.00 USD | 2,520.00 USD | `-17.85%` | `3,475.80` |
| `Live` | `Long` | `0.7255` | 2,840,000.00 USD | 0.00 USD | 311.60 USD | `-17.73%` | `429.50` |
| `Live` | `Long` | `0.7265` | 2,840,000.00 USD | 0.00 USD | 7,000.00 USD | `-17.62%` | `9,636.90` |
| `Live` | `Long` | `0.7275` | 2,830,000.00 USD | 0.00 USD | 35,890.00 USD | `-17.51%` | `49,332.50` |
| `Live` | `Long` | `0.7285` | 2,800,000.00 USD | 0.00 USD | 424.86 USD | `-17.39%` | `583.20` |
| `Live` | `Long` | `0.7295` | 2,800,000.00 USD | 0.00 USD | 375.98 USD | `-17.28%` | `515.40` |
| `Live` | `Long` | `0.7305` | 2,800,000.00 USD | 0.00 USD | 8,550.00 USD | `-17.17%` | `11,710.00` |
| `Live` | `Long` | `0.7335` | 2,790,000.00 USD | 0.00 USD | 1,630.00 USD | `-16.83%` | `2,226.70` |
| `Live` | `Long` | `0.7345` | 2,790,000.00 USD | 0.00 USD | 22,160.00 USD | `-16.71%` | `30,170.10` |
| `Live` | `Long` | `0.7355` | 2,770,000.00 USD | 0.00 USD | 51,920.00 USD | `-16.60%` | `70,595.50` |
| `Live` | `Long` | `0.7365` | 2,710,000.00 USD | 0.00 USD | 441,900.00 USD | `-16.49%` | `600,000.00` |
| `Live` | `Long` | `0.7375` | 2,270,000.00 USD | 0.00 USD | 3,450.00 USD | `-16.37%` | `4,683.00` |
| `Live` | `Long` | `0.7385` | 2,270,000.00 USD | 0.00 USD | 6,020.00 USD | `-16.26%` | `8,146.50` |
| `Live` | `Long` | `0.7395` | 2,260,000.00 USD | 0.00 USD | 3,380.00 USD | `-16.15%` | `4,569.20` |
| `Live` | `Long` | `0.7405` | 2,260,000.00 USD | 0.00 USD | 3,530.00 USD | `-16.03%` | `4,766.70` |
| `Live` | `Long` | `0.7415` | 2,250,000.00 USD | 0.00 USD | 382.61 USD | `-15.92%` | `516.00` |
| `Live` | `Long` | `0.7425` | 2,250,000.00 USD | 0.00 USD | 2,280.00 USD | `-15.80%` | `3,074.90` |
| `Live` | `Long` | `0.7435` | 2,250,000.00 USD | 0.00 USD | 783,980.00 USD | `-15.69%` | `1,054,441.80` |
| `Live` | `Long` | `0.7455` | 1,470,000.00 USD | 0.00 USD | 2,160.00 USD | `-15.46%` | `2,892.60` |
| `Live` | `Long` | `0.7465` | 1,470,000.00 USD | 0.00 USD | 563.83 USD | `-15.35%` | `755.30` |
| `Live` | `Long` | `0.7475` | 1,470,000.00 USD | 0.00 USD | 107,260.00 USD | `-15.24%` | `143,489.20` |
| `Live` | `Long` | `0.7495` | 1,360,000.00 USD | 0.00 USD | 599.60 USD | `-15.01%` | `800.00` |
| `Live` | `Long` | `0.7515` | 1,360,000.00 USD | 0.00 USD | 1,210.00 USD | `-14.78%` | `1,613.50` |
| `Live` | `Long` | `0.7525` | 1,360,000.00 USD | 0.00 USD | 357.14 USD | `-14.67%` | `474.60` |
| `Live` | `Long` | `0.7535` | 1,360,000.00 USD | 0.00 USD | 569.50 USD | `-14.56%` | `755.80` |
| `Live` | `Long` | `0.7545` | 1,360,000.00 USD | 0.00 USD | 922.07 USD | `-14.44%` | `1,222.10` |
| `Live` | `Long` | `0.7555` | 1,350,000.00 USD | 0.00 USD | 2,070.00 USD | `-14.33%` | `2,744.00` |
| `Live` | `Long` | `0.7575` | 1,350,000.00 USD | 0.00 USD | 1,900.00 USD | `-14.10%` | `2,514.80` |
| `Live` | `Long` | `0.7585` | 1,350,000.00 USD | 0.00 USD | 40,520.00 USD | `-13.99%` | `53,414.90` |
| `Live` | `Long` | `0.7595` | 1,310,000.00 USD | 0.00 USD | 7,810.00 USD | `-13.88%` | `10,288.50` |
| `Live` | `Long` | `0.7615` | 1,300,000.00 USD | 0.00 USD | 351.43 USD | `-13.65%` | `461.50` |
| `Live` | `Long` | `0.7625` | 1,300,000.00 USD | 0.00 USD | 859.11 USD | `-13.54%` | `1,126.70` |
| `Live` | `Long` | `0.7635` | 1,300,000.00 USD | 0.00 USD | 439.47 USD | `-13.42%` | `575.60` |
| `Live` | `Long` | `0.7645` | 1,300,000.00 USD | 0.00 USD | 1,060.00 USD | `-13.31%` | `1,384.30` |
| `Live` | `Long` | `0.7655` | 1,300,000.00 USD | 0.00 USD | 2,740.00 USD | `-13.20%` | `3,585.10` |
| `Live` | `Long` | `0.7665` | 1,300,000.00 USD | 0.00 USD | 2,950.00 USD | `-13.08%` | `3,852.60` |
| `Live` | `Long` | `0.7675` | 1,290,000.00 USD | 0.00 USD | 24,420.00 USD | `-12.97%` | `31,823.60` |
| `Live` | `Long` | `0.7685` | 1,270,000.00 USD | 0.00 USD | 6,600.00 USD | `-12.86%` | `8,589.60` |
| `Live` | `Long` | `0.7695` | 1,260,000.00 USD | 0.00 USD | 144,250.00 USD | `-12.74%` | `187,459.50` |
| `Live` | `Long` | `0.7705` | 1,120,000.00 USD | 0.00 USD | 5,640.00 USD | `-12.63%` | `7,324.10` |
| `Live` | `Long` | `0.7715` | 1,110,000.00 USD | 0.00 USD | 19,250.00 USD | `-12.52%` | `24,952.50` |
| `Live` | `Long` | `0.7725` | 1,090,000.00 USD | 0.00 USD | 1,940.00 USD | `-12.40%` | `2,515.50` |
| `Live` | `Long` | `0.7735` | 1,090,000.00 USD | 0.00 USD | 5,230.00 USD | `-12.29%` | `6,756.40` |
| `Live` | `Long` | `0.7755` | 1,090,000.00 USD | 0.00 USD | 3,430.00 USD | `-12.06%` | `4,424.80` |
| `Live` | `Long` | `0.7765` | 1,080,000.00 USD | 0.00 USD | 2,930.00 USD | `-11.95%` | `3,768.50` |
| `Live` | `Long` | `0.7785` | 1,080,000.00 USD | 0.00 USD | 28,010.00 USD | `-11.72%` | `35,979.30` |
| `Live` | `Long` | `0.7795` | 1,050,000.00 USD | 0.00 USD | 322,650.00 USD | `-11.61%` | `413,923.40` |
| `Live` | `Long` | `0.7815` | 729,620.00 USD | 0.00 USD | 4,160.00 USD | `-11.38%` | `5,325.20` |
| `Live` | `Long` | `0.7835` | 725,460.00 USD | 0.00 USD | 4,620.00 USD | `-11.16%` | `5,900.70` |
| `Live` | `Long` | `0.7855` | 720,830.00 USD | 0.00 USD | 156.16 USD | `-10.93%` | `198.80` |
| `Live` | `Long` | `0.7865` | 720,680.00 USD | 0.00 USD | 3,470.00 USD | `-10.82%` | `4,417.70` |
| `Live` | `Long` | `0.7875` | 717,200.00 USD | 0.00 USD | 288.70 USD | `-10.70%` | `366.60` |
| `Live` | `Long` | `0.7905` | 716,910.00 USD | 0.00 USD | 3,160.00 USD | `-10.36%` | `4,000.00` |
| `Live` | `Long` | `0.7915` | 713,750.00 USD | 0.00 USD | 11,600.00 USD | `-10.25%` | `14,657.80` |
| `Live` | `Long` | `0.7925` | 702,150.00 USD | 0.00 USD | 3,800.00 USD | `-10.14%` | `4,789.00` |
| `Live` | `Long` | `0.7935` | 698,360.00 USD | 0.00 USD | 809.45 USD | `-10.02%` | `1,020.10` |
| `Live` | `Long` | `0.7945` | 697,550.00 USD | 0.00 USD | 736.66 USD | `-9.91%` | `927.20` |
| `Live` | `Long` | `0.7955` | 696,810.00 USD | 0.00 USD | 52,610.00 USD | `-9.79%` | `66,134.90` |
| `Live` | `Long` | `0.7965` | 644,200.00 USD | 0.00 USD | 12,980.00 USD | `-9.68%` | `16,300.50` |
| `Live` | `Long` | `0.7975` | 631,220.00 USD | 0.00 USD | 7,460.00 USD | `-9.57%` | `9,359.90` |
| `Live` | `Long` | `0.7985` | 623,750.00 USD | 0.00 USD | 40,230.00 USD | `-9.45%` | `50,386.80` |
| `Live` | `Long` | `0.7995` | 583,520.00 USD | 0.00 USD | 4,330.00 USD | `-9.34%` | `5,415.00` |
| `Live` | `Long` | `0.8005` | 579,190.00 USD | 0.00 USD | 6,990.00 USD | `-9.23%` | `8,736.00` |
| `Live` | `Long` | `0.8015` | 572,200.00 USD | 0.00 USD | 6,710.00 USD | `-9.11%` | `8,367.40` |
| `Live` | `Long` | `0.8025` | 565,490.00 USD | 0.00 USD | 1,350.00 USD | `-9.00%` | `1,686.70` |
| `Live` | `Long` | `0.8035` | 564,140.00 USD | 0.00 USD | 7,680.00 USD | `-8.89%` | `9,559.90` |
| `Live` | `Long` | `0.8045` | 556,450.00 USD | 0.00 USD | 15,720.00 USD | `-8.77%` | `19,542.50` |
| `Live` | `Long` | `0.8055` | 540,730.00 USD | 0.00 USD | 361.11 USD | `-8.66%` | `448.30` |
| `Live` | `Long` | `0.8065` | 540,370.00 USD | 0.00 USD | 6,910.00 USD | `-8.55%` | `8,571.00` |
| `Live` | `Long` | `0.8075` | 533,460.00 USD | 0.00 USD | 2,770.00 USD | `-8.43%` | `3,424.80` |
| `Live` | `Long` | `0.8085` | 530,690.00 USD | 0.00 USD | 22,170.00 USD | `-8.32%` | `27,427.20` |
| `Live` | `Long` | `0.8095` | 508,520.00 USD | 0.00 USD | 154,810.00 USD | `-8.21%` | `191,238.50` |
| `Live` | `Long` | `0.8105` | 353,710.00 USD | 0.00 USD | 2,250.00 USD | `-8.09%` | `2,779.70` |
| `Live` | `Long` | `0.8115` | 351,460.00 USD | 0.00 USD | 2,970.00 USD | `-7.98%` | `3,654.30` |
| `Live` | `Long` | `0.8125` | 348,490.00 USD | 0.00 USD | 7,280.00 USD | `-7.87%` | `8,966.00` |
| `Live` | `Long` | `0.8135` | 341,210.00 USD | 0.00 USD | 3,800.00 USD | `-7.75%` | `4,677.00` |
| `Live` | `Long` | `0.8145` | 337,400.00 USD | 0.00 USD | 277.42 USD | `-7.64%` | `340.60` |
| `Live` | `Long` | `0.8155` | 337,120.00 USD | 0.00 USD | 2,810.00 USD | `-7.53%` | `3,447.40` |
| `Live` | `Long` | `0.8165` | 334,310.00 USD | 0.00 USD | 104.92 USD | `-7.41%` | `128.50` |
| `Live` | `Long` | `0.8175` | 334,210.00 USD | 0.00 USD | 77,840.00 USD | `-7.30%` | `95,214.30` |
| `Live` | `Long` | `0.8195` | 256,370.00 USD | 0.00 USD | 1,720.00 USD | `-7.07%` | `2,098.80` |
| `Live` | `Long` | `0.8205` | 254,650.00 USD | 0.00 USD | 1,400.00 USD | `-6.96%` | `1,706.20` |
| `Live` | `Long` | `0.8215` | 253,250.00 USD | 0.00 USD | 474.01 USD | `-6.85%` | `577.00` |
| `Live` | `Long` | `0.8225` | 252,780.00 USD | 0.00 USD | 1,490.00 USD | `-6.73%` | `1,805.60` |
| `Live` | `Long` | `0.8235` | 251,290.00 USD | 0.00 USD | 1,870.00 USD | `-6.62%` | `2,274.90` |
| `Live` | `Long` | `0.8245` | 249,420.00 USD | 0.00 USD | 19,580.00 USD | `-6.51%` | `23,750.90` |
| `Live` | `Long` | `0.8255` | 229,840.00 USD | 0.00 USD | 1,580.00 USD | `-6.39%` | `1,911.90` |
| `Live` | `Long` | `0.8275` | 228,260.00 USD | 0.00 USD | 4,690.00 USD | `-6.17%` | `5,664.10` |
| `Live` | `Long` | `0.8285` | 223,570.00 USD | 0.00 USD | 120,070.00 USD | `-6.05%` | `144,926.90` |
| `Live` | `Long` | `0.8345` | 103,500.00 USD | 0.00 USD | 5,750.00 USD | `-5.37%` | `6,885.20` |
| `Live` | `Long` | `0.8355` | 97,750.00 USD | 0.00 USD | 117.64 USD | `-5.26%` | `140.80` |
| `Live` | `Long` | `0.8375` | 97,640.00 USD | 0.00 USD | 327.21 USD | `-5.03%` | `390.70` |
| `Live` | `Long` | `0.8385` | 97,310.00 USD | 0.00 USD | 8,240.00 USD | `-4.92%` | `9,832.00` |
| `Live` | `Long` | `0.8395` | 89,060.00 USD | 0.00 USD | 834.13 USD | `-4.81%` | `993.60` |
| `Live` | `Long` | `0.8415` | 88,230.00 USD | 0.00 USD | 750.79 USD | `-4.58%` | `892.20` |
| `Live` | `Long` | `0.8425` | 87,480.00 USD | 0.00 USD | 11,390.00 USD | `-4.47%` | `13,521.40` |
| `Live` | `Long` | `0.8435` | 76,090.00 USD | 0.00 USD | 103.24 USD | `-4.35%` | `122.40` |
| `Live` | `Long` | `0.8445` | 75,980.00 USD | 0.00 USD | 803.20 USD | `-4.24%` | `951.10` |
| `Live` | `Long` | `0.8455` | 75,180.00 USD | 0.00 USD | 10,690.00 USD | `-4.13%` | `12,645.90` |
| `Live` | `Long` | `0.8475` | 64,490.00 USD | 0.00 USD | 1,270.00 USD | `-3.90%` | `1,493.20` |
| `Live` | `Long` | `0.8495` | 63,220.00 USD | 0.00 USD | 6,910.00 USD | `-3.67%` | `8,134.60` |
| `Live` | `Long` | `0.8505` | 56,310.00 USD | 0.00 USD | 13,600.00 USD | `-3.56%` | `15,990.30` |
| `Live` | `Long` | `0.8525` | 42,710.00 USD | 0.00 USD | 42,610.00 USD | `-3.33%` | `49,980.80` |
| `Live` | `Long` | `0.8535` | 104.30 USD | 0.00 USD | 104.30 USD | `-3.22%` | `122.20` |
| `Live` | `Short` | `0.9145` | 4,060.00 USD | 4,060.00 USD | 0.00 USD | `+3.70%` | `4,444.10` |
| `Live` | `Short` | `0.9195` | 13,260.00 USD | 9,200.00 USD | 0.00 USD | `+4.27%` | `10,000.00` |
| `Live` | `Short` | `0.9235` | 13,470.00 USD | 209.36 USD | 0.00 USD | `+4.72%` | `226.70` |
| `Live` | `Short` | `0.9285` | 34,530.00 USD | 21,060.00 USD | 0.00 USD | `+5.29%` | `22,682.60` |
| `Live` | `Short` | `0.9295` | 37,010.00 USD | 2,490.00 USD | 0.00 USD | `+5.40%` | `2,674.10` |
| `Live` | `Short` | `0.9355` | 37,360.00 USD | 340.15 USD | 0.00 USD | `+6.08%` | `363.60` |
| `Live` | `Short` | `0.9365` | 37,830.00 USD | 478.55 USD | 0.00 USD | `+6.19%` | `511.00` |
| `Live` | `Short` | `0.9375` | 38,290.00 USD | 454.59 USD | 0.00 USD | `+6.31%` | `484.90` |
| `Live` | `Short` | `0.9385` | 81,370.00 USD | 43,080.00 USD | 0.00 USD | `+6.42%` | `45,903.60` |
| `Live` | `Short` | `0.9445` | 81,470.00 USD | 103.90 USD | 0.00 USD | `+7.10%` | `110.00` |
| `Live` | `Short` | `0.9755` | 85,060.00 USD | 3,590.00 USD | 0.00 USD | `+10.62%` | `3,680.60` |
| `Live` | `Short` | `0.9805` | 86,110.00 USD | 1,050.00 USD | 0.00 USD | `+11.18%` | `1,068.70` |
| `Live` | `Short` | `0.9865` | 86,480.00 USD | 365.70 USD | 0.00 USD | `+11.86%` | `370.70` |
| `Live` | `Short` | `0.9885` | 90,730.00 USD | 4,250.00 USD | 0.00 USD | `+12.09%` | `4,304.30` |
| `Live` | `Short` | `0.9915` | 92,300.00 USD | 1,570.00 USD | 0.00 USD | `+12.43%` | `1,586.00` |
| `Live` | `Short` | `0.9935` | 92,440.00 USD | 139.59 USD | 0.00 USD | `+12.66%` | `140.50` |
| `Live` | `Short` | `1.00` | 92,770.00 USD | 330.29 USD | 0.00 USD | `+13.56%` | `329.80` |
| `Live` | `Short` | `1.01` | 98,480.00 USD | 5,710.00 USD | 0.00 USD | `+14.92%` | `5,629.50` |
| `Live` | `Short` | `1.01` | 99,190.00 USD | 705.99 USD | 0.00 USD | `+15.04%` | `695.90` |
| `Live` | `Short` | `1.02` | 99,360.00 USD | 170.40 USD | 0.00 USD | `+15.15%` | `167.80` |
| `Live` | `Short` | `1.03` | 110,400.00 USD | 11,040.00 USD | 0.00 USD | `+16.74%` | `10,723.80` |
| `Live` | `Short` | `1.04` | 112,100.00 USD | 1,710.00 USD | 0.00 USD | `+18.10%` | `1,639.00` |
| `Live` | `Short` | `1.05` | 117,980.00 USD | 5,880.00 USD | 0.00 USD | `+18.78%` | `5,609.70` |
| `Live` | `Short` | `1.05` | 118,580.00 USD | 597.52 USD | 0.00 USD | `+19.12%` | `568.80` |
| `Live` | `Short` | `1.05` | 120,970.00 USD | 2,390.00 USD | 0.00 USD | `+19.23%` | `2,272.10` |
| `Live` | `Short` | `1.06` | 121,070.00 USD | 105.65 USD | 0.00 USD | `+19.80%` | `100.00` |
| `Live` | `Short` | `1.07` | 122,600.00 USD | 1,530.00 USD | 0.00 USD | `+21.39%` | `1,429.60` |
| `Live` | `Short` | `1.08` | 126,180.00 USD | 3,580.00 USD | 0.00 USD | `+22.52%` | `3,315.70` |
| `Live` | `Short` | `1.09` | 131,740.00 USD | 5,550.00 USD | 0.00 USD | `+23.54%` | `5,095.60` |
| `Live` | `Short` | `1.10` | 132,060.00 USD | 324.90 USD | 0.00 USD | `+24.68%` | `295.50` |
| `Live` | `Short` | `1.10` | 132,340.00 USD | 277.22 USD | 0.00 USD | `+24.79%` | `251.90` |
| `Live` | `Short` | `1.11` | 141,280.00 USD | 8,940.00 USD | 0.00 USD | `+25.92%` | `8,047.90` |
| `Live` | `Short` | `1.13` | 164,580.00 USD | 23,310.00 USD | 0.00 USD | `+27.74%` | `20,691.10` |
| `Live` | `Short` | `1.13` | 165,220.00 USD | 634.09 USD | 0.00 USD | `+28.42%` | `559.90` |
| `Live` | `Short` | `1.15` | 165,350.00 USD | 129.88 USD | 0.00 USD | `+30.80%` | `112.60` |
| `Live` | `Short` | `1.18` | 165,730.00 USD | 381.24 USD | 0.00 USD | `+34.09%` | `322.40` |
| `Live` | `Short` | `1.20` | 165,910.00 USD | 177.65 USD | 0.00 USD | `+36.02%` | `148.10` |
| `Live` | `Short` | `1.22` | 170,350.00 USD | 4,440.00 USD | 0.00 USD | `+38.17%` | `3,646.70` |
| `Live` | `Short` | `1.22` | 170,730.00 USD | 383.01 USD | 0.00 USD | `+38.62%` | `313.30` |
| `Live` | `Short` | `1.23` | 171,110.00 USD | 380.84 USD | 0.00 USD | `+39.99%` | `308.50` |
| `Live` | `Short` | `1.24` | 172,140.00 USD | 1,020.00 USD | 0.00 USD | `+40.21%` | `826.40` |
| `Live` | `Short` | `1.24` | 176,060.00 USD | 3,930.00 USD | 0.00 USD | `+40.55%` | `3,169.40` |
| `Live` | `Short` | `1.26` | 178,730.00 USD | 2,670.00 USD | 0.00 USD | `+42.82%` | `2,118.80` |
| `Live` | `Short` | `1.26` | 183,460.00 USD | 4,730.00 USD | 0.00 USD | `+43.16%` | `3,742.60` |
| `Live` | `Short` | `1.28` | 185,760.00 USD | 2,300.00 USD | 0.00 USD | `+44.86%` | `1,804.00` |
| `Live` | `Short` | `1.28` | 225,650.00 USD | 39,880.00 USD | 0.00 USD | `+45.43%` | `31,097.50` |
| `Live` | `Short` | `1.29` | 235,490.00 USD | 9,850.00 USD | 0.00 USD | `+46.56%` | `7,618.00` |
| `Live` | `Short` | `1.29` | 235,720.00 USD | 226.80 USD | 0.00 USD | `+46.79%` | `175.20` |
| `Live` | `Short` | `1.30` | 235,830.00 USD | 114.40 USD | 0.00 USD | `+47.24%` | `88.10` |
| `Live` | `Short` | `1.31` | 236,850.00 USD | 1,020.00 USD | 0.00 USD | `+48.49%` | `777.20` |
| `Live` | `Short` | `1.31` | 260,890.00 USD | 24,040.00 USD | 0.00 USD | `+48.72%` | `18,332.80` |
| `Live` | `Short` | `1.31` | 268,390.00 USD | 7,490.00 USD | 0.00 USD | `+48.83%` | `5,709.60` |
| `Live` | `Short` | `1.33` | 274,730.00 USD | 6,340.00 USD | 0.00 USD | `+50.30%` | `4,781.30` |
| `Live` | `Short` | `1.33` | 296,690.00 USD | 21,970.00 USD | 0.00 USD | `+50.64%` | `16,535.70` |
| `Live` | `Short` | `1.34` | 303,550.00 USD | 6,860.00 USD | 0.00 USD | `+51.89%` | `5,119.30` |
| `Live` | `Short` | `1.37` | 661,830.00 USD | 358,280.00 USD | 0.00 USD | `+55.63%` | `261,043.60` |
| `Live` | `Short` | `1.40` | 661,970.00 USD | 137.73 USD | 0.00 USD | `+59.04%` | `98.20` |
| `Live` | `Short` | `1.41` | 666,420.00 USD | 4,450.00 USD | 0.00 USD | `+60.40%` | `3,142.60` |
| `Live` | `Short` | `1.44` | 666,820.00 USD | 402.08 USD | 0.00 USD | `+62.89%` | `279.90` |
| `Live` | `Short` | `1.44` | 667,110.00 USD | 288.68 USD | 0.00 USD | `+63.34%` | `200.40` |
| `Live` | `Short` | `1.47` | 683,530.00 USD | 16,420.00 USD | 0.00 USD | `+66.52%` | `11,182.60` |
| `Live` | `Short` | `1.51` | 687,550.00 USD | 4,020.00 USD | 0.00 USD | `+71.74%` | `2,654.10` |
| `Live` | `Short` | `1.53` | 687,700.00 USD | 152.75 USD | 0.00 USD | `+73.21%` | `100.00` |
| `Live` | `Short` | `1.53` | 697,630.00 USD | 9,930.00 USD | 0.00 USD | `+73.44%` | `6,491.20` |
| `Live` | `Short` | `1.54` | 697,770.00 USD | 144.34 USD | 0.00 USD | `+74.12%` | `94.00` |
| `Live` | `Short` | `1.55` | 966,010.00 USD | 268,240.00 USD | 0.00 USD | `+75.82%` | `173,000.00` |
| `Live` | `Short` | `1.58` | 966,290.00 USD | 285.21 USD | 0.00 USD | `+78.88%` | `180.80` |
| `Live` | `Short` | `1.59` | 967,480.00 USD | 1,180.00 USD | 0.00 USD | `+80.69%` | `743.20` |
| `Live` | `Short` | `1.60` | 967,600.00 USD | 123.81 USD | 0.00 USD | `+81.15%` | `77.50` |
| `Live` | `Short` | `1.60` | 968,730.00 USD | 1,130.00 USD | 0.00 USD | `+81.71%` | `704.60` |
| `Live` | `Short` | `1.61` | 970,920.00 USD | 2,190.00 USD | 0.00 USD | `+82.28%` | `1,360.10` |
| `Live` | `Short` | `1.62` | 989,400.00 USD | 18,490.00 USD | 0.00 USD | `+83.87%` | `11,400.30` |
| `Live` | `Short` | `1.65` | 1,010,000.00 USD | 21,330.00 USD | 0.00 USD | `+86.70%` | `12,957.30` |
| `Live` | `Short` | `1.65` | 1,010,000.00 USD | 4,080.00 USD | 0.00 USD | `+87.50%` | `2,466.00` |
| `Live` | `Short` | `1.66` | 1,020,000.00 USD | 3,620.00 USD | 0.00 USD | `+88.18%` | `2,184.10` |
| `Live` | `Short` | `1.66` | 1,060,000.00 USD | 39,070.00 USD | 0.00 USD | `+88.29%` | `23,529.40` |
| `Live` | `Short` | `1.68` | 1,060,000.00 USD | 171.37 USD | 0.00 USD | `+90.33%` | `102.10` |
| `Live` | `Short` | `1.69` | 1,060,000.00 USD | 150.02 USD | 0.00 USD | `+91.35%` | `88.90` |
| `Live` | `Short` | `1.71` | 1,060,000.00 USD | 487.21 USD | 0.00 USD | `+93.51%` | `285.50` |
| `Live` | `Short` | `1.71` | 1,060,000.00 USD | 205.67 USD | 0.00 USD | `+94.19%` | `120.10` |
| `Live` | `Short` | `1.72` | 1,070,000.00 USD | 9,720.00 USD | 0.00 USD | `+95.21%` | `5,645.40` |
| `Live` | `Short` | `1.73` | 1,070,000.00 USD | 226.05 USD | 0.00 USD | `+96.57%` | `130.40` |
| `Live` | `Short` | `1.74` | 1,070,000.00 USD | 912.54 USD | 0.00 USD | `+97.25%` | `524.60` |
| `Live` | `Short` | `1.74` | 1,070,000.00 USD | 2,080.00 USD | 0.00 USD | `+97.48%` | `1,197.00` |
| `Live` | `Short` | `1.74` | 1,160,000.00 USD | 86,430.00 USD | 0.00 USD | `+97.82%` | `49,543.90` |
| `Live` | `Short` | `1.75` | 1,180,000.00 USD | 19,920.00 USD | 0.00 USD | `+98.61%` | `11,370.30` |
| `Live` | `Short` | `1.75` | 1,190,000.00 USD | 11,350.00 USD | 0.00 USD | `+98.84%` | `6,474.70` |
| `Live` | `Short` | `1.75` | 1,190,000.00 USD | 1,520.00 USD | 0.00 USD | `+98.95%` | `868.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2625` | 1,150,000.00 USD | 0.00 USD | 497.31 USD | `-70.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 1,150,000.00 USD | 0.00 USD | 102.75 USD | `-61.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 1,150,000.00 USD | 0.00 USD | 256.78 USD | `-60.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3885` | 1,150,000.00 USD | 0.00 USD | 428.87 USD | `-55.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4115` | 1,150,000.00 USD | 0.00 USD | 123.45 USD | `-53.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4195` | 1,150,000.00 USD | 0.00 USD | 818.15 USD | `-52.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4345` | 1,150,000.00 USD | 0.00 USD | 436.41 USD | `-50.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4355` | 1,150,000.00 USD | 0.00 USD | 876.79 USD | `-50.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4505` | 1,150,000.00 USD | 0.00 USD | 466.72 USD | `-48.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4765` | 1,150,000.00 USD | 0.00 USD | 142.95 USD | `-45.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 1,150,000.00 USD | 0.00 USD | 3,010.00 USD | `-43.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5135` | 1,140,000.00 USD | 0.00 USD | 151.74 USD | `-41.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 1,140,000.00 USD | 0.00 USD | 123.91 USD | `-41.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5495` | 1,140,000.00 USD | 0.00 USD | 219.80 USD | `-37.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 1,140,000.00 USD | 0.00 USD | 237,400.00 USD | `-37.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5535` | 906,690.00 USD | 0.00 USD | 276.75 USD | `-37.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 906,410.00 USD | 0.00 USD | 1,680.00 USD | `-36.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 904,730.00 USD | 0.00 USD | 853.41 USD | `-35.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5805` | 903,880.00 USD | 0.00 USD | 119.76 USD | `-34.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 903,760.00 USD | 0.00 USD | 3,520.00 USD | `-33.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5955` | 900,230.00 USD | 0.00 USD | 470.62 USD | `-32.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 899,760.00 USD | 0.00 USD | 108.39 USD | `-31.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 899,660.00 USD | 0.00 USD | 123.28 USD | `-31.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6205` | 899,530.00 USD | 0.00 USD | 488.52 USD | `-29.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6255` | 899,040.00 USD | 0.00 USD | 4,070.00 USD | `-29.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6305` | 894,980.00 USD | 0.00 USD | 242.24 USD | `-28.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6465` | 894,730.00 USD | 0.00 USD | 193.95 USD | `-26.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6505` | 894,540.00 USD | 0.00 USD | 149.22 USD | `-26.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6555` | 894,390.00 USD | 0.00 USD | 195.47 USD | `-25.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6595` | 894,200.00 USD | 0.00 USD | 112.91 USD | `-25.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6605` | 894,080.00 USD | 0.00 USD | 181.31 USD | `-25.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6615` | 893,900.00 USD | 0.00 USD | 190.25 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6635` | 893,710.00 USD | 0.00 USD | 153.53 USD | `-24.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6705` | 893,560.00 USD | 0.00 USD | 52,450.00 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6735` | 841,110.00 USD | 0.00 USD | 536.11 USD | `-23.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6805` | 840,570.00 USD | 0.00 USD | 918.68 USD | `-22.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6815` | 839,650.00 USD | 0.00 USD | 340.75 USD | `-22.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6905` | 839,310.00 USD | 0.00 USD | 9,270.00 USD | `-21.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6915` | 830,050.00 USD | 0.00 USD | 120.53 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6945` | 829,930.00 USD | 0.00 USD | 160.71 USD | `-21.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6965` | 829,770.00 USD | 0.00 USD | 738.08 USD | `-21.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6995` | 829,030.00 USD | 0.00 USD | 187.61 USD | `-20.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 828,840.00 USD | 0.00 USD | 8,500.00 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7015` | 820,350.00 USD | 0.00 USD | 89,150.00 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7075` | 731,190.00 USD | 0.00 USD | 5,650.00 USD | `-19.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7085` | 725,540.00 USD | 0.00 USD | 371.68 USD | `-19.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 725,170.00 USD | 0.00 USD | 152.05 USD | `-19.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7175` | 725,020.00 USD | 0.00 USD | 123.41 USD | `-18.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7275` | 724,900.00 USD | 0.00 USD | 745.54 USD | `-17.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 724,150.00 USD | 0.00 USD | 1,130.00 USD | `-17.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7315` | 723,020.00 USD | 0.00 USD | 18,770.00 USD | `-17.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7335` | 704,250.00 USD | 0.00 USD | 7,970.00 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7365` | 696,280.00 USD | 0.00 USD | 257.26 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7425` | 696,020.00 USD | 0.00 USD | 161.72 USD | `-15.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7435` | 695,860.00 USD | 0.00 USD | 1,590.00 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7455` | 694,270.00 USD | 0.00 USD | 10,160.00 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7505` | 684,110.00 USD | 0.00 USD | 94,190.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7545` | 589,920.00 USD | 0.00 USD | 1,230.00 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7585` | 588,690.00 USD | 0.00 USD | 1,840.00 USD | `-13.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7595` | 586,850.00 USD | 0.00 USD | 804.61 USD | `-13.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7605` | 586,050.00 USD | 0.00 USD | 590.68 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7625` | 585,460.00 USD | 0.00 USD | 635.62 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7645` | 584,820.00 USD | 0.00 USD | 191.12 USD | `-13.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7675` | 584,630.00 USD | 0.00 USD | 273.92 USD | `-12.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7725` | 584,360.00 USD | 0.00 USD | 125.92 USD | `-12.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7735` | 584,230.00 USD | 0.00 USD | 1,980.00 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7745` | 582,250.00 USD | 0.00 USD | 1,150.00 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7755` | 581,110.00 USD | 0.00 USD | 1,500.00 USD | `-12.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7795` | 579,610.00 USD | 0.00 USD | 1,860.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 577,750.00 USD | 0.00 USD | 128.47 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7815` | 577,620.00 USD | 0.00 USD | 7,820.00 USD | `-11.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7835` | 569,810.00 USD | 0.00 USD | 6,960.00 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 562,850.00 USD | 0.00 USD | 135.11 USD | `-10.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7865` | 562,710.00 USD | 0.00 USD | 7,870.00 USD | `-10.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7885` | 554,850.00 USD | 0.00 USD | 1,090.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7905` | 553,760.00 USD | 0.00 USD | 1,500.00 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7935` | 552,260.00 USD | 0.00 USD | 1,290.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7945` | 550,970.00 USD | 0.00 USD | 24,240.00 USD | `-9.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 526,730.00 USD | 0.00 USD | 1,260.00 USD | `-9.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7985` | 525,480.00 USD | 0.00 USD | 319.40 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7995` | 525,160.00 USD | 0.00 USD | 4,740.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 520,420.00 USD | 0.00 USD | 1,800.00 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8015` | 518,620.00 USD | 0.00 USD | 144.67 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8045` | 518,480.00 USD | 0.00 USD | 1,510.00 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8055` | 516,960.00 USD | 0.00 USD | 390.59 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8075` | 516,570.00 USD | 0.00 USD | 263.25 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8085` | 516,310.00 USD | 0.00 USD | 1,250.00 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8095` | 515,060.00 USD | 0.00 USD | 218.32 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 514,840.00 USD | 0.00 USD | 182,590.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 332,250.00 USD | 0.00 USD | 174.63 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8125` | 332,080.00 USD | 0.00 USD | 1,420.00 USD | `-7.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8135` | 330,660.00 USD | 0.00 USD | 123,350.00 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8145` | 207,310.00 USD | 0.00 USD | 1,160.00 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8165` | 206,150.00 USD | 0.00 USD | 216.70 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8185` | 205,930.00 USD | 0.00 USD | 125.72 USD | `-7.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8195` | 205,810.00 USD | 0.00 USD | 375.49 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8205` | 205,430.00 USD | 0.00 USD | 14,050.00 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8225` | 191,380.00 USD | 0.00 USD | 7,160.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8235` | 184,230.00 USD | 0.00 USD | 226.71 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8245` | 184,000.00 USD | 0.00 USD | 3,780.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8255` | 180,220.00 USD | 0.00 USD | 6,050.00 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8265` | 174,170.00 USD | 0.00 USD | 325.56 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8275` | 173,840.00 USD | 0.00 USD | 666.55 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8295` | 173,180.00 USD | 0.00 USD | 11,080.00 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8305` | 162,090.00 USD | 0.00 USD | 3,950.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8315` | 158,140.00 USD | 0.00 USD | 171.46 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8325` | 157,970.00 USD | 0.00 USD | 7,920.00 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8335` | 150,050.00 USD | 0.00 USD | 690.30 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8345` | 149,360.00 USD | 0.00 USD | 161.89 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8355` | 149,200.00 USD | 0.00 USD | 263.43 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 148,930.00 USD | 0.00 USD | 610.23 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8375` | 148,320.00 USD | 0.00 USD | 699.65 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8385` | 147,620.00 USD | 0.00 USD | 320.31 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8395` | 147,300.00 USD | 0.00 USD | 240.52 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8405` | 147,060.00 USD | 0.00 USD | 9,760.00 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 137,310.00 USD | 0.00 USD | 1,020.00 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8435` | 136,290.00 USD | 0.00 USD | 510.57 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8445` | 135,780.00 USD | 0.00 USD | 212.81 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8455` | 135,570.00 USD | 0.00 USD | 1,940.00 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8465` | 133,620.00 USD | 0.00 USD | 12,850.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8475` | 120,770.00 USD | 0.00 USD | 481.80 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8485` | 120,280.00 USD | 0.00 USD | 1,330.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 118,960.00 USD | 0.00 USD | 1,430.00 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8515` | 117,530.00 USD | 0.00 USD | 2,930.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8525` | 114,600.00 USD | 0.00 USD | 1,070.00 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8545` | 113,520.00 USD | 0.00 USD | 5,150.00 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 108,370.00 USD | 0.00 USD | 11,960.00 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 96,400.00 USD | 0.00 USD | 5,020.00 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8575` | 91,380.00 USD | 0.00 USD | 134.80 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 91,250.00 USD | 0.00 USD | 8,900.00 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8595` | 82,340.00 USD | 0.00 USD | 1,740.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 80,600.00 USD | 0.00 USD | 1,450.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8615` | 79,150.00 USD | 0.00 USD | 6,160.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8625` | 72,990.00 USD | 0.00 USD | 1,960.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8635` | 71,030.00 USD | 0.00 USD | 611.88 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8645` | 70,420.00 USD | 0.00 USD | 26,840.00 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8655` | 43,580.00 USD | 0.00 USD | 5,080.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 38,500.00 USD | 0.00 USD | 734.45 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 37,770.00 USD | 0.00 USD | 541.15 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8685` | 37,230.00 USD | 0.00 USD | 279.83 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8695` | 36,950.00 USD | 0.00 USD | 666.30 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 36,280.00 USD | 0.00 USD | 106.11 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 36,170.00 USD | 0.00 USD | 3,710.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 32,460.00 USD | 0.00 USD | 1,500.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8735` | 30,960.00 USD | 0.00 USD | 3,450.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8745` | 27,510.00 USD | 0.00 USD | 866.37 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8755` | 26,640.00 USD | 0.00 USD | 1,540.00 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8765` | 25,110.00 USD | 0.00 USD | 14,670.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8775` | 10,440.00 USD | 0.00 USD | 123.55 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8785` | 10,320.00 USD | 0.00 USD | 1,380.00 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8795` | 8,930.00 USD | 0.00 USD | 281.09 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8805` | 8,650.00 USD | 0.00 USD | 4,580.00 USD | `-0.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8815` | 4,070.00 USD | 0.00 USD | 4,070.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8825` | 563.65 USD | 563.65 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8835` | 989.59 USD | 425.94 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8845` | 3,200.00 USD | 2,210.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8855` | 7,420.00 USD | 4,210.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8865` | 11,010.00 USD | 3,600.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8875` | 11,250.00 USD | 235.54 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8885` | 22,610.00 USD | 11,360.00 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8895` | 31,390.00 USD | 8,780.00 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8905` | 32,620.00 USD | 1,230.00 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8915` | 33,090.00 USD | 469.91 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8925` | 43,700.00 USD | 10,610.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8935` | 43,980.00 USD | 277.07 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8945` | 44,080.00 USD | 100.09 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8955` | 47,470.00 USD | 3,390.00 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8965` | 48,750.00 USD | 1,280.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8975` | 66,960.00 USD | 18,210.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8985` | 67,850.00 USD | 889.43 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8995` | 96,810.00 USD | 28,960.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 97,450.00 USD | 638.09 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9015` | 99,500.00 USD | 2,050.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9025` | 100,430.00 USD | 926.06 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 100,620.00 USD | 188.92 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 103,570.00 USD | 2,950.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9055` | 115,750.00 USD | 12,180.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 116,190.00 USD | 444.19 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 116,440.00 USD | 250.83 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 117,540.00 USD | 1,090.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 119,060.00 USD | 1,520.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9105` | 120,440.00 USD | 1,370.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 120,700.00 USD | 260.23 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9125` | 123,590.00 USD | 2,890.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 126,610.00 USD | 3,020.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9145` | 129,790.00 USD | 3,180.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 130,360.00 USD | 570.08 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 130,650.00 USD | 295.30 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 134,550.00 USD | 3,900.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 136,530.00 USD | 1,970.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 136,640.00 USD | 116.59 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 139,810.00 USD | 3,160.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 291,770.00 USD | 151,960.00 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 291,910.00 USD | 145.02 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9235` | 292,410.00 USD | 495.00 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 293,810.00 USD | 1,400.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 298,830.00 USD | 5,030.00 USD | 0.00 USD | `+4.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 301,040.00 USD | 2,200.00 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 301,320.00 USD | 287.62 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 301,520.00 USD | 199.16 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 302,610.00 USD | 1,090.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 303,060.00 USD | 448.69 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 303,180.00 USD | 120.16 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 306,610.00 USD | 3,430.00 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 307,180.00 USD | 568.87 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9345` | 307,480.00 USD | 292.78 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 308,420.00 USD | 944.76 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 309,440.00 USD | 1,020.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9375` | 309,540.00 USD | 104.53 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9385` | 362,600.00 USD | 53,060.00 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 366,510.00 USD | 3,910.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 375,470.00 USD | 8,960.00 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 376,000.00 USD | 529.50 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 376,670.00 USD | 667.86 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 378,370.00 USD | 1,700.00 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 379,160.00 USD | 789.04 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 387,720.00 USD | 8,560.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 388,780.00 USD | 1,050.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 389,620.00 USD | 848.20 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 408,740.00 USD | 19,120.00 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9495` | 409,910.00 USD | 1,160.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 415,720.00 USD | 5,820.00 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9515` | 417,870.00 USD | 2,150.00 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 427,780.00 USD | 9,910.00 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9545` | 430,930.00 USD | 3,150.00 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 432,370.00 USD | 1,440.00 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 435,250.00 USD | 2,890.00 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 436,380.00 USD | 1,130.00 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9585` | 436,510.00 USD | 121.54 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9595` | 437,580.00 USD | 1,070.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 442,970.00 USD | 5,390.00 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9615` | 461,840.00 USD | 18,870.00 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 481,240.00 USD | 19,400.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 481,500.00 USD | 259.86 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 482,840.00 USD | 1,340.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 483,310.00 USD | 476.57 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 483,700.00 USD | 386.60 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 486,860.00 USD | 3,160.00 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9685` | 487,850.00 USD | 993.78 USD | 0.00 USD | `+9.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 488,070.00 USD | 212.90 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 488,230.00 USD | 165.86 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 488,360.00 USD | 125.61 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 488,800.00 USD | 441.51 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 498,990.00 USD | 10,190.00 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 502,580.00 USD | 3,590.00 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 506,780.00 USD | 4,200.00 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 506,960.00 USD | 176.73 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9785` | 507,470.00 USD | 513.32 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9795` | 542,830.00 USD | 35,360.00 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 574,790.00 USD | 31,960.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 579,780.00 USD | 4,990.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 580,340.00 USD | 558.35 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 581,400.00 USD | 1,060.00 USD | 0.00 USD | `+11.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 582,580.00 USD | 1,180.00 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 583,070.00 USD | 490.99 USD | 0.00 USD | `+11.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9905` | 583,470.00 USD | 395.21 USD | 0.00 USD | `+12.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 584,460.00 USD | 991.50 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 594,790.00 USD | 10,340.00 USD | 0.00 USD | `+12.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 595,200.00 USD | 409.52 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9945` | 595,490.00 USD | 284.92 USD | 0.00 USD | `+12.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9965` | 595,840.00 USD | 350.37 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9995` | 595,960.00 USD | 124.04 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 597,520.00 USD | 1,560.00 USD | 0.00 USD | `+13.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 599,690.00 USD | 2,180.00 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 600,470.00 USD | 778.64 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 600,840.00 USD | 363.87 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 601,100.00 USD | 267.20 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 601,690.00 USD | 589.52 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 601,800.00 USD | 110.62 USD | 0.00 USD | `+14.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 611,890.00 USD | 10,090.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 617,310.00 USD | 5,420.00 USD | 0.00 USD | `+14.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 619,840.00 USD | 2,520.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 620,090.00 USD | 248.49 USD | 0.00 USD | `+15.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 629,230.00 USD | 9,150.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 629,960.00 USD | 722.63 USD | 0.00 USD | `+15.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 630,270.00 USD | 312.07 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 630,440.00 USD | 171.24 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 631,000.00 USD | 561.11 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 631,250.00 USD | 249.30 USD | 0.00 USD | `+16.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 632,720.00 USD | 1,470.00 USD | 0.00 USD | `+16.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 633,150.00 USD | 432.18 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 633,290.00 USD | 137.88 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 635,630.00 USD | 2,340.00 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 636,330.00 USD | 694.72 USD | 0.00 USD | `+17.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 636,490.00 USD | 160.60 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 643,040.00 USD | 6,560.00 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 645,960.00 USD | 2,920.00 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 646,180.00 USD | 224.56 USD | 0.00 USD | `+18.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 649,760.00 USD | 3,570.00 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 650,190.00 USD | 432.19 USD | 0.00 USD | `+18.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 652,040.00 USD | 1,850.00 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,350,000.00 USD | 1,700,000.00 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 5,390.00 USD | 0.00 USD | `+20.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 285.32 USD | 0.00 USD | `+20.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 1,130.00 USD | 0.00 USD | `+20.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 1,240.00 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 2,360,000.00 USD | 278.06 USD | 0.00 USD | `+20.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 309.00 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 228.98 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 272.12 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,360,000.00 USD | 117.12 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 2,500,000.00 USD | 140,120.00 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,500,000.00 USD | 530.01 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,500,000.00 USD | 128.23 USD | 0.00 USD | `+22.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,610,000.00 USD | 108,190.00 USD | 0.00 USD | `+22.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,620,000.00 USD | 3,430.00 USD | 0.00 USD | `+22.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 2,620,000.00 USD | 550.49 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,620,000.00 USD | 5,810.00 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,620,000.00 USD | 1,520.00 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 5,570.00 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 1,290.00 USD | 0.00 USD | `+23.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 294.81 USD | 0.00 USD | `+24.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 2,630,000.00 USD | 183.11 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,630,000.00 USD | 123.13 USD | 0.00 USD | `+24.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,630,000.00 USD | 494.98 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,630,000.00 USD | 613.52 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,750,000.00 USD | 115,100.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,750,000.00 USD | 409.76 USD | 0.00 USD | `+24.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,750,000.00 USD | 162.77 USD | 0.00 USD | `+25.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 2,750,000.00 USD | 959.70 USD | 0.00 USD | `+25.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,750,000.00 USD | 160.18 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 2,750,000.00 USD | 669.85 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,750,000.00 USD | 293.61 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 2,860,000.00 USD | 112,050.00 USD | 0.00 USD | `+27.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,860,000.00 USD | 462.47 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,870,000.00 USD | 2,180.00 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,870,000.00 USD | 273.34 USD | 0.00 USD | `+28.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,870,000.00 USD | 119.49 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 2,890,000.00 USD | 20,740.00 USD | 0.00 USD | `+28.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,890,000.00 USD | 468.47 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 2,890,000.00 USD | 1,430.00 USD | 0.00 USD | `+29.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,890,000.00 USD | 338.50 USD | 0.00 USD | `+29.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,890,000.00 USD | 2,640.00 USD | 0.00 USD | `+30.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 2,890,000.00 USD | 1,230.00 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,890,000.00 USD | 2,450.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,900,000.00 USD | 1,250.00 USD | 0.00 USD | `+31.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.16` | 2,900,000.00 USD | 143.67 USD | 0.00 USD | `+31.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,900,000.00 USD | 989.81 USD | 0.00 USD | `+32.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,900,000.00 USD | 304.33 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 2,900,000.00 USD | 255.14 USD | 0.00 USD | `+32.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,900,000.00 USD | 241.65 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,900,000.00 USD | 239.97 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,900,000.00 USD | 2,470.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.18` | 2,900,000.00 USD | 3,060.00 USD | 0.00 USD | `+33.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,210,000.00 USD | 310,250.00 USD | 0.00 USD | `+34.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,210,000.00 USD | 309.53 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 3,210,000.00 USD | 159.09 USD | 0.00 USD | `+35.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,210,000.00 USD | 146.21 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,230,000.00 USD | 18,560.00 USD | 0.00 USD | `+36.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,230,000.00 USD | 933.81 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 3,230,000.00 USD | 658.86 USD | 0.00 USD | `+36.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,450,000.00 USD | 213,390.00 USD | 0.00 USD | `+37.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.21` | 3,450,000.00 USD | 560.05 USD | 0.00 USD | `+37.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,450,000.00 USD | 1,050.00 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,450,000.00 USD | 108.05 USD | 0.00 USD | `+38.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.22` | 3,450,000.00 USD | 509.71 USD | 0.00 USD | `+38.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,450,000.00 USD | 162.15 USD | 0.00 USD | `+39.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,450,000.00 USD | 187.04 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,450,000.00 USD | 542.12 USD | 0.00 USD | `+39.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 3,480,000.00 USD | 23,740.00 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,480,000.00 USD | 2,010.00 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 3,480,000.00 USD | 345.91 USD | 0.00 USD | `+40.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,480,000.00 USD | 104.79 USD | 0.00 USD | `+41.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,480,000.00 USD | 100.04 USD | 0.00 USD | `+41.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,480,000.00 USD | 517.52 USD | 0.00 USD | `+42.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,480,000.00 USD | 152.29 USD | 0.00 USD | `+42.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,480,000.00 USD | 1,480.00 USD | 0.00 USD | `+42.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 3,480,000.00 USD | 1,010.00 USD | 0.00 USD | `+43.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,480,000.00 USD | 2,780.00 USD | 0.00 USD | `+43.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,480,000.00 USD | 340.38 USD | 0.00 USD | `+44.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,480,000.00 USD | 903.22 USD | 0.00 USD | `+44.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 3,490,000.00 USD | 475.01 USD | 0.00 USD | `+44.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,530,000.00 USD | 41,160.00 USD | 0.00 USD | `+44.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,540,000.00 USD | 12,840.00 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,730,000.00 USD | 194,770.00 USD | 0.00 USD | `+45.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,750,000.00 USD | 12,890.00 USD | 0.00 USD | `+46.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,760,000.00 USD | 8,820.00 USD | 0.00 USD | `+46.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,760,000.00 USD | 466.95 USD | 0.00 USD | `+46.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 3,760,000.00 USD | 613.59 USD | 0.00 USD | `+46.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,760,000.00 USD | 1,420.00 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,770,000.00 USD | 13,000.00 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 3,770,000.00 USD | 284.42 USD | 0.00 USD | `+47.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 3,790,000.00 USD | 22,810.00 USD | 0.00 USD | `+49.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,790,000.00 USD | 640.82 USD | 0.00 USD | `+50.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 3,800,000.00 USD | 134.75 USD | 0.00 USD | `+50.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,810,000.00 USD | 13,400.00 USD | 0.00 USD | `+51.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 3,810,000.00 USD | 541.96 USD | 0.00 USD | `+52.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,820,000.00 USD | 13,490.00 USD | 0.00 USD | `+53.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 3,830,000.00 USD | 11,580.00 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 3,840,000.00 USD | 3,610.00 USD | 0.00 USD | `+53.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,840,000.00 USD | 1,500.00 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,850,000.00 USD | 15,000.00 USD | 0.00 USD | `+54.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.37` | 3,860,000.00 USD | 9,030.00 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,860,000.00 USD | 405.86 USD | 0.00 USD | `+57.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 3,880,000.00 USD | 13,890.00 USD | 0.00 USD | `+57.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,890,000.00 USD | 14,000.00 USD | 0.00 USD | `+58.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 3,900,000.00 USD | 12,560.00 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,940,000.00 USD | 32,860.00 USD | 0.00 USD | `+59.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,940,000.00 USD | 102.40 USD | 0.00 USD | `+59.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 3,940,000.00 USD | 106.64 USD | 0.00 USD | `+60.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,940,000.00 USD | 2,810.00 USD | 0.00 USD | `+60.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 3,950,000.00 USD | 8,420.00 USD | 0.00 USD | `+61.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 3,950,000.00 USD | 1,410.00 USD | 0.00 USD | `+61.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,950,000.00 USD | 145.37 USD | 0.00 USD | `+62.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,950,000.00 USD | 1,390.00 USD | 0.00 USD | `+63.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 3,970,000.00 USD | 14,390.00 USD | 0.00 USD | `+63.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,970,000.00 USD | 7,000.00 USD | 0.00 USD | `+64.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 3,990,000.00 USD | 14,490.00 USD | 0.00 USD | `+64.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,990,000.00 USD | 1,340.00 USD | 0.00 USD | `+66.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 3,990,000.00 USD | 342.08 USD | 0.00 USD | `+67.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,000,000.00 USD | 14,890.00 USD | 0.00 USD | `+68.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 4,010,000.00 USD | 9,580.00 USD | 0.00 USD | `+69.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,030,000.00 USD | 14,980.00 USD | 0.00 USD | `+69.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,030,000.00 USD | 5,110.00 USD | 0.00 USD | `+70.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 4,030,000.00 USD | 1,180.00 USD | 0.00 USD | `+70.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 4,040,000.00 USD | 1,260.00 USD | 0.00 USD | `+72.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 4,040,000.00 USD | 2,150.00 USD | 0.00 USD | `+74.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,040,000.00 USD | 158.76 USD | 0.00 USD | `+76.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 4,070,000.00 USD | 30,710.00 USD | 0.00 USD | `+77.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 4,070,000.00 USD | 574.53 USD | 0.00 USD | `+80.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 4,070,000.00 USD | 391.32 USD | 0.00 USD | `+81.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 4,070,000.00 USD | 1,160.00 USD | 0.00 USD | `+83.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,070,000.00 USD | 1,140.00 USD | 0.00 USD | `+85.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 4,070,000.00 USD | 1,970.00 USD | 0.00 USD | `+86.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,070,000.00 USD | 281.45 USD | 0.00 USD | `+88.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 4,080,000.00 USD | 2,070.00 USD | 0.00 USD | `+88.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 4,090,000.00 USD | 13,060.00 USD | 0.00 USD | `+92.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 4,090,000.00 USD | 1,390.00 USD | 0.00 USD | `+97.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,090,000.00 USD | 1,070.00 USD | 0.00 USD | `+98.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 4,090,000.00 USD | 320.52 USD | 0.00 USD | `+98.50%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7380` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 56,620.00 USD | 28,770.00 USD | 82,570.00 USD |
| `7D` | `0.7400` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 17,280.00 USD | 13,180.00 USD | 24,540.00 USD |
| `7D` | `0.7420` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 31,920.00 USD | 8,580.00 USD | 37,420.00 USD |
| `7D` | `0.7440` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 65,280.00 USD | 21,190.00 USD | 41,020.00 USD |
| `7D` | `0.7460` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 22,100.00 USD | 24,720.00 USD | 42,470.00 USD |
| `7D` | `0.7480` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 11,220.00 USD | 6,300.00 USD | 375.99 USD |
| `7D` | `0.7500` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 25,600.00 USD | 12,880.00 USD | 11,450.00 USD |
| `7D` | `0.7520` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 2,130.00 USD | 10,160.00 USD | 22,250.00 USD |
| `7D` | `0.7540` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 9,690.00 USD | 4,770.00 USD | 13,530.00 USD |
| `7D` | `0.7560` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 2,690.00 USD | 17,670.00 USD | 5,490.00 USD |
| `7D` | `0.7580` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 19,590.00 USD | 20,390.00 USD | 1,090.00 USD |
| `7D` | `0.7600` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 8,420.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `0.7620` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 40,420.00 USD | 16,580.00 USD | 630.66 USD |
| `7D` | `0.7640` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 556.58 USD | 118.70 USD | 573.15 USD |
| `7D` | `0.7660` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 1,280.00 USD | 23,260.00 USD | 32,410.00 USD |
| `7D` | `0.7680` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 182.28 USD | 3,780.00 USD | 1,880.00 USD |
| `7D` | `0.7700` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD |
| `7D` | `0.7720` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 7,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.7780` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD |
| `7D` | `0.7800` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 0.00 USD | 2,640.00 USD | 1,330.00 USD |
| `7D` | `0.7820` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 0.00 USD | 1,440.00 USD | 10,610.00 USD |
| `7D` | `0.7840` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 6,050.00 USD | 2,680.00 USD | 1,320.00 USD |
| `7D` | `0.7860` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 1,740.00 USD | 45,250.00 USD | 0.00 USD |
| `7D` | `0.7900` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 6,610.00 USD | 28,080.00 USD | 0.00 USD |
| `1D` | `0.7910` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 13,200.00 USD | 12,510.00 USD | 9,350.00 USD |
| `1D` | `0.7920` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 8,610.00 USD | 9,490.00 USD | 36,790.00 USD |
| `7D` | `0.7920` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 0.00 USD | 23,790.00 USD | 69,490.00 USD |
| `1D` | `0.7930` | 7,490,000.00 USD | 0.00 USD | 7,490,000.00 USD | 1,220.00 USD | 12,720.00 USD | 7,560.00 USD |
| `1D` | `0.7940` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 30,150.00 USD | 8,730.00 USD | 18,890.00 USD |
| `7D` | `0.7940` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 0.00 USD | 1,760.00 USD | 4,720.00 USD |
| `1D` | `0.7950` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 8,910.00 USD | 3,900.00 USD | 24,940.00 USD |
| `1D` | `0.7960` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 2,360.00 USD | 2,710.00 USD | 20,810.00 USD |
| `7D` | `0.7960` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 5,300.00 USD | 19,750.00 USD | 87,940.00 USD |
| `1D` | `0.7970` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 19,610.00 USD | 16,290.00 USD | 40,370.00 USD |
| `1D` | `0.7980` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 8,320.00 USD | 0.00 USD | 165.92 USD |
| `7D` | `0.7980` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 33,940.00 USD | 3,570.00 USD | 49,630.00 USD |
| `1D` | `0.7990` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 1,600.00 USD | 20,590.00 USD | 18,860.00 USD |
| `1D` | `0.8000` | 7,220,000.00 USD | 0.00 USD | 7,220,000.00 USD | 30,830.00 USD | 10,990.00 USD | 16,320.00 USD |
| `7D` | `0.8000` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 41,450.00 USD | 16,710.00 USD | 0.00 USD |
| `1D` | `0.8010` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 1,140.00 USD | 3,860.00 USD | 200.14 USD |
| `1D` | `0.8020` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 796.46 USD | 6,400.00 USD | 6,570.00 USD |
| `7D` | `0.8020` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 1,890.00 USD | 29,180.00 USD | 35,910.00 USD |
| `1D` | `0.8030` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 0.00 USD | 1,400.00 USD | 159.97 USD |
| `1D` | `0.8040` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 43,320.00 USD | 22,790.00 USD | 21,430.00 USD |
| `7D` | `0.8040` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD |
| `1D` | `0.8050` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 19,550.00 USD | 7,230.00 USD | 330.63 USD |
| `1D` | `0.8060` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 32,080.00 USD | 11,640.00 USD | 73,980.00 USD |
| `7D` | `0.8060` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 12,280.00 USD | 737.70 USD | 1,170.00 USD |
| `1D` | `0.8070` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 8,540.00 USD | 14,620.00 USD | 1,120.00 USD |
| `1D` | `0.8080` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 2,530.00 USD | 4,510.00 USD | 1,630.00 USD |
| `7D` | `0.8080` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 5,030.00 USD | 11,280.00 USD | 8,230.00 USD |
| `1D` | `0.8090` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 587.71 USD | 5,580.00 USD | 1,870.00 USD |
| `1D` | `0.8100` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 1,830.00 USD | 5,380.00 USD | 248.40 USD |
| `7D` | `0.8100` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 4,310.00 USD | 9,850.00 USD | 5,630.00 USD |
| `1D` | `0.8110` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 1,650.00 USD | 2,090.00 USD | 196.09 USD |
| `1D` | `0.8120` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 13,640.00 USD | 780.21 USD | 23,580.00 USD |
| `7D` | `0.8120` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 73,000.00 USD | 9,210.00 USD | 38,210.00 USD |
| `1D` | `0.8130` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 683.00 USD | 989.28 USD | 706.99 USD |
| `1D` | `0.8140` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 14,810.00 USD | 523.16 USD | 11,360.00 USD |
| `7D` | `0.8140` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 55,190.00 USD | 31,920.00 USD | 79,240.00 USD |
| `1D` | `0.8150` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 4,970.00 USD | 1,140.00 USD | 7,080.00 USD |
| `1D` | `0.8160` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 17,910.00 USD | 1,970.00 USD | 23,350.00 USD |
| `7D` | `0.8160` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 186,980.00 USD | 49,790.00 USD | 146,720.00 USD |
| `1D` | `0.8170` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 56,460.00 USD | 4,990.00 USD | 30,300.00 USD |
| `1D` | `0.8180` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 0.00 USD | 351.95 USD | 213.40 USD |
| `7D` | `0.8180` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 82,600.00 USD | 41,370.00 USD | 43,240.00 USD |
| `1D` | `0.8190` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 24,470.00 USD | 1,600.00 USD | 10,410.00 USD |
| `1D` | `0.8200` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 87,930.00 USD | 3,460.00 USD | 73,220.00 USD |
| `7D` | `0.8200` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 205,920.00 USD | 48,700.00 USD | 97,610.00 USD |
| `1D` | `0.8210` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 16,280.00 USD | 83,240.00 USD | 50,570.00 USD |
| `1D` | `0.8220` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 59,890.00 USD | 4,450.00 USD | 18,880.00 USD |
| `7D` | `0.8220` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 110,800.00 USD | 74,480.00 USD | 175,590.00 USD |
| `1D` | `0.8230` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 9,670.00 USD | 5,770.00 USD | 105,860.00 USD |
| `1D` | `0.8240` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 9,760.00 USD | 2,400.00 USD | 32,680.00 USD |
| `7D` | `0.8240` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 109,730.00 USD | 44,640.00 USD | 87,630.00 USD |
| `1D` | `0.8250` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 27,470.00 USD | 1,230.00 USD | 4,950.00 USD |
| `1D` | `0.8260` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 19,170.00 USD | 8,970.00 USD | 17,260.00 USD |
| `7D` | `0.8260` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 199,800.00 USD | 32,880.00 USD | 111,970.00 USD |
| `1D` | `0.8270` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 39,540.00 USD | 22,100.00 USD | 8,150.00 USD |
| `1D` | `0.8280` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 1,490.00 USD | 773.90 USD | 313.76 USD |
| `7D` | `0.8280` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 118,780.00 USD | 44,400.00 USD | 87,990.00 USD |
| `1D` | `0.8290` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 24,750.00 USD | 11,650.00 USD | 46,490.00 USD |
| `1D` | `0.8300` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 3,410.00 USD | 3,180.00 USD | 7,300.00 USD |
| `7D` | `0.8300` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 33,770.00 USD | 45,100.00 USD | 48,290.00 USD |
| `1D` | `0.8310` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 2,590.00 USD | 27,590.00 USD | 23,300.00 USD |
| `1D` | `0.8320` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 867.90 USD | 10,780.00 USD | 22,900.00 USD |
| `7D` | `0.8320` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 90,830.00 USD | 77,110.00 USD | 150,430.00 USD |
| `1D` | `0.8330` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 7,940.00 USD | 19,140.00 USD | 74,670.00 USD |
| `1D` | `0.8340` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 142,540.00 USD | 21,960.00 USD | 30,560.00 USD |
| `7D` | `0.8340` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 114,580.00 USD | 56,360.00 USD | 180,080.00 USD |
| `1D` | `0.8350` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 14,620.00 USD | 13,380.00 USD | 1,070.00 USD |
| `1D` | `0.8360` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 46,210.00 USD | 1,800.00 USD | 397.88 USD |
| `7D` | `0.8360` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 178,100.00 USD | 28,000.00 USD | 99,550.00 USD |
| `1D` | `0.8370` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 20,840.00 USD | 10,300.00 USD | 129,040.00 USD |
| `1D` | `0.8380` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 35,040.00 USD | 60,090.00 USD | 16,830.00 USD |
| `7D` | `0.8380` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 69,220.00 USD | 223,030.00 USD | 223,070.00 USD |
| `1D` | `0.8390` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 44,740.00 USD | 792.50 USD | 33,000.00 USD |
| `1D` | `0.8400` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 6,260.00 USD | 9,410.00 USD | 22,280.00 USD |
| `7D` | `0.8400` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 96,040.00 USD | 56,210.00 USD | 61,950.00 USD |
| `1D` | `0.8410` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 17,400.00 USD | 16,230.00 USD | 55,700.00 USD |
| `1D` | `0.8420` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 71,930.00 USD | 48,120.00 USD | 0.00 USD |
| `7D` | `0.8420` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 96,530.00 USD | 66,440.00 USD | 9,570.00 USD |
| `1D` | `0.8430` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 17,820.00 USD | 18,730.00 USD | 21,880.00 USD |
| `1D` | `0.8440` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 49,800.00 USD | 44,320.00 USD | 166.34 USD |
| `7D` | `0.8440` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 28,900.00 USD | 111,080.00 USD | 0.00 USD |
| `1D` | `0.8450` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 22,880.00 USD | 30,550.00 USD | 12,980.00 USD |
| `1D` | `0.8460` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 623.10 USD | 65,890.00 USD | 26,100.00 USD |
| `7D` | `0.8460` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 52,800.00 USD | 57,770.00 USD | 0.00 USD |
| `1D` | `0.8470` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 81,540.00 USD | 39,470.00 USD | 15,130.00 USD |
| `1D` | `0.8480` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 6,790.00 USD | 36,960.00 USD | 82,740.00 USD |
| `7D` | `0.8480` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 73,880.00 USD | 61,480.00 USD | 82,870.00 USD |
| `1D` | `0.8490` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 61,960.00 USD | 61,840.00 USD | 67,980.00 USD |
| `1D` | `0.8500` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 42,500.00 USD | 37,570.00 USD | 107,590.00 USD |
| `7D` | `0.8500` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 85,470.00 USD | 58,490.00 USD | 50,360.00 USD |
| `1D` | `0.8510` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 41,500.00 USD | 106,640.00 USD | 49,410.00 USD |
| `1D` | `0.8520` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 59,930.00 USD | 95,740.00 USD | 88,510.00 USD |
| `7D` | `0.8520` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 77,320.00 USD | 53,520.00 USD | 54,650.00 USD |
| `1D` | `0.8530` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 93,910.00 USD | 90,610.00 USD | 12,030.00 USD |
| `1D` | `0.8540` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 0.00 USD | 13,200.00 USD | 128.06 USD |
| `7D` | `0.8540` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 277,690.00 USD | 50,820.00 USD | 0.00 USD |
| `1D` | `0.8550` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 1,920.00 USD | 37,290.00 USD | 15,370.00 USD |
| `1D` | `0.8560` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 30,660.00 USD | 17,140.00 USD | 52,090.00 USD |
| `7D` | `0.8560` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 87,380.00 USD | 91,360.00 USD | 33,190.00 USD |
| `1D` | `0.8570` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 14,730.00 USD | 12,760.00 USD | 3,770.00 USD |
| `1D` | `0.8580` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 32,900.00 USD | 54,050.00 USD | 26,530.00 USD |
| `7D` | `0.8580` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 146,570.00 USD | 14,530.00 USD | 0.00 USD |
| `1D` | `0.8590` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 13,810.00 USD | 6,720.00 USD | 36,530.00 USD |
| `1D` | `0.8600` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 75,640.00 USD | 32,480.00 USD | 200.12 USD |
| `7D` | `0.8600` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 38,890.00 USD | 164,470.00 USD | 20,680.00 USD |
| `1D` | `0.8610` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 21,600.00 USD | 0.00 USD | 6,800.00 USD |
| `1D` | `0.8620` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 42,920.00 USD | 25,800.00 USD | 25,970.00 USD |
| `7D` | `0.8620` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 25,100.00 USD | 145,110.00 USD | 394,640.00 USD |
| `1D` | `0.8630` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 48,390.00 USD | 103,090.00 USD | 113,770.00 USD |
| `1D` | `0.8640` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 88,690.00 USD | 54,960.00 USD | 30,280.00 USD |
| `7D` | `0.8640` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 83,850.00 USD | 0.00 USD | 2,680.00 USD |
| `1D` | `0.8650` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 13,580.00 USD | 35,750.00 USD | 136,870.00 USD |
| `1D` | `0.8660` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 135,650.00 USD | 13,430.00 USD | 54,950.00 USD |
| `7D` | `0.8660` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 294,020.00 USD | 122,950.00 USD | 678,840.00 USD |
| `1D` | `0.8670` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 114,240.00 USD | 33,880.00 USD | 142,270.00 USD |
| `1D` | `0.8680` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 50,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8680` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 213,340.00 USD | 0.00 USD | 10,240.00 USD |
| `1D` | `0.8690` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 25,820.00 USD |
| `1D` | `0.8700` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 97,830.00 USD | 31,630.00 USD |
| `7D` | `0.8700` | 952,500.00 USD | 0.00 USD | 952,500.00 USD | 0.00 USD | 34,600.00 USD | 111,270.00 USD |
| `1D` | `0.8710` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 152,210.00 USD | 62,100.00 USD | 151,880.00 USD |
| `1D` | `0.8720` | 850,840.00 USD | 0.00 USD | 850,840.00 USD | 30,060.00 USD | 26,400.00 USD | 21,020.00 USD |
| `7D` | `0.8720` | 806,620.00 USD | 0.00 USD | 806,620.00 USD | 207,250.00 USD | 101,630.00 USD | 87,530.00 USD |
| `1D` | `0.8730` | 773,360.00 USD | 0.00 USD | 773,360.00 USD | 55,600.00 USD | 39,670.00 USD | 29,960.00 USD |
| `1D` | `0.8740` | 648,130.00 USD | 0.00 USD | 648,130.00 USD | 61,330.00 USD | 20,260.00 USD | 39,440.00 USD |
| `7D` | `0.8740` | 410,210.00 USD | 0.00 USD | 410,210.00 USD | 9,520.00 USD | 72,100.00 USD | 71,600.00 USD |
| `1D` | `0.8750` | 527,110.00 USD | 0.00 USD | 527,110.00 USD | 29,460.00 USD | 0.00 USD | 83,500.00 USD |
| `1D` | `0.8760` | 414,140.00 USD | 0.00 USD | 414,140.00 USD | 0.00 USD | 0.00 USD | 53,070.00 USD |
| `7D` | `0.8760` | 256,990.00 USD | 0.00 USD | 256,990.00 USD | 16,700.00 USD | 29,060.00 USD | 189,440.00 USD |
| `1D` | `0.8770` | 361,080.00 USD | 0.00 USD | 361,080.00 USD | 27,620.00 USD | 20,280.00 USD | 94,280.00 USD |
| `1D` | `0.8780` | 218,890.00 USD | 0.00 USD | 218,890.00 USD | 79,990.00 USD | 17,410.00 USD | 0.00 USD |
| `7D` | `0.8780` | 21,780.00 USD | 0.00 USD | 21,780.00 USD | 0.00 USD | 0.00 USD | 1,480.00 USD |
| `1D` | `0.8790` | 121,480.00 USD | 0.00 USD | 121,480.00 USD | 39,180.00 USD | 0.00 USD | 12,930.00 USD |
| `1D` | `0.8800` | 69,370.00 USD | 0.00 USD | 69,370.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `0.8800` | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 20,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8810` | 68,360.00 USD | 0.00 USD | 68,360.00 USD | 37,200.00 USD | 0.00 USD | 31,170.00 USD |
| `7D` | `0.8810` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8820` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8840` | 1,820.00 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `1D` | `0.8850` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 214.94 USD |
| `1D` | `0.8860` | 3,150.00 USD | 3,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `1D` | `0.8870` | 4,560.00 USD | 4,560.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD | 0.00 USD |
| `1D` | `0.8880` | 127,320.00 USD | 127,320.00 USD | 0.00 USD | 122,200.00 USD | 0.00 USD | 560.38 USD |
| `7D` | `0.8880` | 3,860.00 USD | 3,860.00 USD | 0.00 USD | 0.00 USD | 3,860.00 USD | 0.00 USD |
| `1D` | `0.8900` | 130,170.00 USD | 130,170.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8900` | 12,670.00 USD | 12,670.00 USD | 0.00 USD | 8,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8910` | 218,370.00 USD | 218,370.00 USD | 0.00 USD | 87,950.00 USD | 0.00 USD | 251.48 USD |
| `1D` | `0.8920` | 220,160.00 USD | 220,160.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8920` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8930` | 238,980.00 USD | 238,980.00 USD | 0.00 USD | 0.00 USD | 18,820.00 USD | 0.00 USD |
| `1D` | `0.8940` | 260,550.00 USD | 260,550.00 USD | 0.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `7D` | `0.8940` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8950` | 338,400.00 USD | 338,400.00 USD | 0.00 USD | 0.00 USD | 77,850.00 USD | 0.00 USD |
| `7D` | `0.8960` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 593,680.00 USD | 107,280.00 USD | 0.00 USD |
| `1D` | `0.8970` | 339,370.00 USD | 339,370.00 USD | 0.00 USD | 969.20 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.8980` | 473,200.00 USD | 473,200.00 USD | 0.00 USD | 73,030.00 USD | 60,810.00 USD | 0.00 USD |
| `7D` | `0.8980` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 615,200.00 USD | 118,950.00 USD | 339,780.00 USD |
| `1D` | `0.8990` | 669,350.00 USD | 669,350.00 USD | 0.00 USD | 70,970.00 USD | 125,180.00 USD | 0.00 USD |
| `1D` | `0.9000` | 931,600.00 USD | 931,600.00 USD | 0.00 USD | 226,850.00 USD | 5,150.00 USD | 30,250.00 USD |
| `7D` | `0.9000` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 198,040.00 USD | 16,730.00 USD | 0.00 USD |
| `1D` | `0.9010` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 16,960.00 USD | 107,900.00 USD | 24,790.00 USD |
| `1D` | `0.9020` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 28,630.00 USD | 53,510.00 USD | 0.00 USD |
| `7D` | `0.9020` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 85,610.00 USD | 221,330.00 USD | 476,390.00 USD |
| `1D` | `0.9030` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 39,620.00 USD | 108,680.00 USD | 16,750.00 USD |
| `1D` | `0.9040` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 175,130.00 USD | 136,350.00 USD | 0.00 USD |
| `7D` | `0.9040` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 223,750.00 USD | 2,890.00 USD | 218,670.00 USD |
| `1D` | `0.9050` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 90,340.00 USD | 26,270.00 USD | 44,370.00 USD |
| `1D` | `0.9060` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 168,180.00 USD | 158,360.00 USD | 165,470.00 USD |
| `7D` | `0.9060` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 286,790.00 USD | 34,600.00 USD | 104,620.00 USD |
| `1D` | `0.9070` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 135,160.00 USD | 128,180.00 USD | 115,990.00 USD |
| `1D` | `0.9080` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 113,830.00 USD | 45,320.00 USD | 17,240.00 USD |
| `7D` | `0.9080` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 389,350.00 USD | 288,590.00 USD | 227,140.00 USD |
| `1D` | `0.9090` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 76,970.00 USD | 49,730.00 USD | 33,090.00 USD |
| `1D` | `0.9100` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 83,550.00 USD | 50,130.00 USD | 40,220.00 USD |
| `7D` | `0.9100` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 123,910.00 USD | 78,920.00 USD | 70,600.00 USD |
| `1D` | `0.9110` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 97,650.00 USD | 16,590.00 USD | 29,110.00 USD |
| `1D` | `0.9120` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 32,690.00 USD | 81,230.00 USD | 69,240.00 USD |
| `7D` | `0.9120` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 135,210.00 USD | 163,810.00 USD | 0.00 USD |
| `1D` | `0.9130` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 45,950.00 USD | 25,330.00 USD | 92,690.00 USD |
| `1D` | `0.9140` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 162,940.00 USD | 61,860.00 USD | 142,770.00 USD |
| `7D` | `0.9140` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 143,540.00 USD | 83,230.00 USD | 0.00 USD |
| `1D` | `0.9150` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 109,360.00 USD | 68,860.00 USD | 184,390.00 USD |
| `1D` | `0.9160` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 60,590.00 USD | 102,520.00 USD | 52,430.00 USD |
| `7D` | `0.9160` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 212,270.00 USD | 84,510.00 USD | 172,440.00 USD |
| `1D` | `0.9170` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 94,070.00 USD | 28,770.00 USD | 82,700.00 USD |
| `1D` | `0.9180` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 33,320.00 USD | 60,340.00 USD | 68,440.00 USD |
| `7D` | `0.9180` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 38,590.00 USD | 63,520.00 USD | 187,840.00 USD |
| `1D` | `0.9190` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 61,810.00 USD | 16,580.00 USD | 49,670.00 USD |
| `1D` | `0.9200` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 72,440.00 USD | 16,940.00 USD | 100,020.00 USD |
| `7D` | `0.9200` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 445,890.00 USD | 32,570.00 USD | 114,170.00 USD |
| `1D` | `0.9210` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 85,860.00 USD | 61,240.00 USD | 124,600.00 USD |
| `1D` | `0.9220` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 129,150.00 USD | 32,770.00 USD | 136,590.00 USD |
| `7D` | `0.9220` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 6,470.00 USD | 66,370.00 USD | 318,200.00 USD |
| `1D` | `0.9230` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 107,110.00 USD | 55,720.00 USD | 151,880.00 USD |
| `1D` | `0.9240` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 133,900.00 USD | 59,970.00 USD | 117,430.00 USD |
| `7D` | `0.9240` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 111,800.00 USD | 62,860.00 USD | 256,790.00 USD |
| `1D` | `0.9250` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 133,720.00 USD | 62,480.00 USD | 55,080.00 USD |
| `1D` | `0.9260` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 6,140.00 USD | 71,670.00 USD | 52,810.00 USD |
| `7D` | `0.9260` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 213,450.00 USD | 99,090.00 USD | 89,770.00 USD |
| `1D` | `0.9270` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 9,360.00 USD | 67,290.00 USD | 27,410.00 USD |
| `1D` | `0.9280` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 38,960.00 USD | 30,650.00 USD | 68,280.00 USD |
| `7D` | `0.9280` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 128,610.00 USD | 43,320.00 USD | 36,720.00 USD |
| `1D` | `0.9290` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 53,450.00 USD | 2,870.00 USD | 44,980.00 USD |
| `1D` | `0.9300` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 5,010.00 USD | 59,350.00 USD | 65,490.00 USD |
| `7D` | `0.9300` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 186,110.00 USD | 113,080.00 USD | 168,120.00 USD |
| `1D` | `0.9310` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 118,420.00 USD | 16,270.00 USD | 36,900.00 USD |
| `1D` | `0.9320` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 71,540.00 USD | 28,860.00 USD | 35,540.00 USD |
| `7D` | `0.9320` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 4,410.00 USD | 53,880.00 USD | 63,160.00 USD |
| `1D` | `0.9330` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 24,270.00 USD | 19,640.00 USD | 6,470.00 USD |
| `1D` | `0.9340` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 1,200.00 USD | 16,430.00 USD | 0.00 USD |
| `7D` | `0.9340` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 50,160.00 USD | 78,870.00 USD | 0.00 USD |
| `1D` | `0.9350` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 964.55 USD | 637.37 USD | 19,260.00 USD |
| `1D` | `0.9360` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 48,380.00 USD | 26,000.00 USD | 55,350.00 USD |
| `7D` | `0.9360` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 131,450.00 USD | 3,160.00 USD | 8,180.00 USD |
| `1D` | `0.9370` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 80,470.00 USD | 54,520.00 USD | 135,700.00 USD |
| `1D` | `0.9380` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 15,820.00 USD | 9,200.00 USD | 110,030.00 USD |
| `7D` | `0.9380` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 168,030.00 USD | 5,150.00 USD | 179,560.00 USD |
| `1D` | `0.9390` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 2,680.00 USD | 3,150.00 USD | 34,210.00 USD |
| `1D` | `0.9400` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 46,290.00 USD | 2,330.00 USD | 56,200.00 USD |
| `7D` | `0.9400` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 173,610.00 USD | 39,110.00 USD | 129,920.00 USD |
| `1D` | `0.9410` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 20,010.00 USD | 15,520.00 USD | 616.58 USD |
| `1D` | `0.9420` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 6,740.00 USD | 1,340.00 USD | 24,870.00 USD |
| `7D` | `0.9420` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 12,670.00 USD | 32,360.00 USD | 37,360.00 USD |
| `1D` | `0.9430` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 4,310.00 USD | 2,340.00 USD | 0.00 USD |
| `1D` | `0.9440` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 4,930.00 USD | 23,400.00 USD | 46,190.00 USD |
| `7D` | `0.9440` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 8,820.00 USD | 217,840.00 USD | 1,280.00 USD |
| `1D` | `0.9450` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 4,850.00 USD | 793.93 USD | 107,000.00 USD |
| `1D` | `0.9460` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 56,940.00 USD | 26,210.00 USD | 24,340.00 USD |
| `7D` | `0.9460` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 0.00 USD | 69,070.00 USD | 127,910.00 USD |
| `1D` | `0.9470` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 36,440.00 USD | 24,720.00 USD | 20,480.00 USD |
| `1D` | `0.9480` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 55,350.00 USD | 48,320.00 USD | 35,870.00 USD |
| `7D` | `0.9480` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 78,160.00 USD | 291,990.00 USD |
| `1D` | `0.9490` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 18,020.00 USD | 14,650.00 USD | 22,780.00 USD |
| `1D` | `0.9500` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 7,440.00 USD | 22,120.00 USD | 47,610.00 USD |
| `7D` | `0.9500` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 2,840.00 USD | 30,430.00 USD | 375,100.00 USD |
| `1D` | `0.9510` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 52,590.00 USD | 28,760.00 USD | 128,260.00 USD |
| `1D` | `0.9520` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 466.70 USD | 155.85 USD | 83,920.00 USD |
| `7D` | `0.9520` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 87,720.00 USD | 362,480.00 USD |
| `1D` | `0.9530` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 29,490.00 USD | 27,080.00 USD | 70,380.00 USD |
| `1D` | `0.9540` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 27,570.00 USD | 21,440.00 USD | 27,680.00 USD |
| `7D` | `0.9540` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 13,570.00 USD | 3,670.00 USD | 60,880.00 USD |
| `1D` | `0.9550` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 21,030.00 USD | 13,800.00 USD | 24,930.00 USD |
| `1D` | `0.9560` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 20,640.00 USD | 11,590.00 USD | 23,330.00 USD |
| `7D` | `0.9560` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 74,460.00 USD | 3,500.00 USD | 2,410.00 USD |
| `1D` | `0.9570` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 16,640.00 USD | 2,570.00 USD | 533.76 USD |
| `1D` | `0.9580` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 10,110.00 USD | 42,520.00 USD | 12,560.00 USD |
| `7D` | `0.9580` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 846,080.00 USD | 1,220.00 USD | 1,790.00 USD |
| `1D` | `0.9590` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 33,840.00 USD | 27,020.00 USD | 0.00 USD |
| `1D` | `0.9600` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 69,660.00 USD | 23,730.00 USD | 78,070.00 USD |
| `7D` | `0.9600` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 358,610.00 USD | 118,450.00 USD | 131,760.00 USD |
| `1D` | `0.9610` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 137,510.00 USD | 51,860.00 USD | 166,430.00 USD |
| `1D` | `0.9620` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 129,590.00 USD | 13,840.00 USD | 10,290.00 USD |
| `7D` | `0.9620` | 17,370,000.00 USD | 17,370,000.00 USD | 0.00 USD | 715,790.00 USD | 231,300.00 USD | 588,980.00 USD |
| `1D` | `0.9630` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 111,830.00 USD | 28,520.00 USD | 53,290.00 USD |
| `1D` | `0.9640` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 125,880.00 USD | 39,890.00 USD | 49,130.00 USD |
| `7D` | `0.9640` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 693,720.00 USD | 366,520.00 USD | 508,260.00 USD |
| `1D` | `0.9650` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 18,690.00 USD | 72,860.00 USD | 29,960.00 USD |
| `1D` | `0.9660` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 135,070.00 USD | 55,850.00 USD | 42,300.00 USD |
| `7D` | `0.9660` | 20,660,000.00 USD | 20,660,000.00 USD | 0.00 USD | 962,420.00 USD | 245,250.00 USD | 514,790.00 USD |
| `1D` | `0.9670` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 93,370.00 USD | 53,730.00 USD | 191,400.00 USD |
| `1D` | `0.9680` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 80,770.00 USD | 13,020.00 USD | 112,310.00 USD |
| `7D` | `0.9680` | 22,550,000.00 USD | 22,550,000.00 USD | 0.00 USD | 780,090.00 USD | 625,850.00 USD | 485,330.00 USD |
| `1D` | `0.9690` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 162,210.00 USD | 72,620.00 USD | 130,100.00 USD |
| `1D` | `0.9700` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 120,430.00 USD | 39,280.00 USD | 60,840.00 USD |
| `7D` | `0.9700` | 23,800,000.00 USD | 23,800,000.00 USD | 0.00 USD | 657,220.00 USD | 324,760.00 USD | 264,680.00 USD |
| `1D` | `0.9710` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 67,590.00 USD | 27,540.00 USD | 71,860.00 USD |
| `1D` | `0.9720` | 12,780,000.00 USD | 12,780,000.00 USD | 0.00 USD | 38,610.00 USD | 36,660.00 USD | 50,950.00 USD |
| `7D` | `0.9720` | 24,620,000.00 USD | 24,620,000.00 USD | 0.00 USD | 403,610.00 USD | 197,100.00 USD | 222,870.00 USD |
| `1D` | `0.9730` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 24,020.00 USD | 1,020.00 USD | 0.00 USD |
| `1D` | `0.9740` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 14,950.00 USD | 5,900.00 USD | 47,290.00 USD |
| `7D` | `0.9740` | 25,200,000.00 USD | 25,200,000.00 USD | 0.00 USD | 334,930.00 USD | 116,990.00 USD | 124,030.00 USD |
| `1D` | `0.9750` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 20,270.00 USD | 28,720.00 USD | 84,460.00 USD |
| `1D` | `0.9760` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 244.53 USD | 290.18 USD | 154.26 USD |
| `7D` | `0.9760` | 25,930,000.00 USD | 25,930,000.00 USD | 0.00 USD | 182,900.00 USD | 286,070.00 USD | 265,750.00 USD |
| `1D` | `0.9770` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 4,370.00 USD | 20,510.00 USD | 32,110.00 USD |
| `1D` | `0.9780` | 13,190,000.00 USD | 13,190,000.00 USD | 0.00 USD | 28,300.00 USD | 21,450.00 USD | 70,630.00 USD |
| `7D` | `0.9780` | 26,980,000.00 USD | 26,980,000.00 USD | 0.00 USD | 323,530.00 USD | 211,120.00 USD | 513,910.00 USD |
| `1D` | `0.9790` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 18,030.00 USD | 15,220.00 USD | 32,800.00 USD |
| `1D` | `0.9800` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 43,300.00 USD | 32,650.00 USD | 81,360.00 USD |
| `7D` | `0.9800` | 27,530,000.00 USD | 27,530,000.00 USD | 0.00 USD | 247,060.00 USD | 66,910.00 USD | 240,420.00 USD |
| `1D` | `0.9810` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 44,730.00 USD | 4,820.00 USD | 0.00 USD |
| `1D` | `0.9820` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 37,830.00 USD | 836.01 USD | 0.00 USD |
| `7D` | `0.9820` | 27,850,000.00 USD | 27,850,000.00 USD | 0.00 USD | 108,220.00 USD | 68,030.00 USD | 142,510.00 USD |
| `1D` | `0.9830` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 31,020.00 USD | 21,700.00 USD | 47.72 USD |
| `1D` | `0.9840` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 2,480.00 USD | 22,540.00 USD | 5,900.00 USD |
| `7D` | `0.9840` | 28,550,000.00 USD | 28,550,000.00 USD | 0.00 USD | 397,850.00 USD | 123,740.00 USD | 177,280.00 USD |
| `1D` | `0.9850` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 19,260.00 USD | 18,260.00 USD | 14,480.00 USD |
| `1D` | `0.9860` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 49,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9860` | 28,890,000.00 USD | 28,890,000.00 USD | 0.00 USD | 108,860.00 USD | 154,250.00 USD | 74,460.00 USD |
| `7D` | `0.9880` | 29,200,000.00 USD | 29,200,000.00 USD | 0.00 USD | 209,770.00 USD | 75,650.00 USD | 26,750.00 USD |
| `7D` | `0.9900` | 29,510,000.00 USD | 29,510,000.00 USD | 0.00 USD | 201,410.00 USD | 100,430.00 USD | 6,630.00 USD |
| `7D` | `0.9920` | 29,960,000.00 USD | 29,960,000.00 USD | 0.00 USD | 288,210.00 USD | 79,650.00 USD | 81,440.00 USD |
| `7D` | `0.9940` | 30,430,000.00 USD | 30,430,000.00 USD | 0.00 USD | 143,340.00 USD | 183,310.00 USD | 146,940.00 USD |
| `7D` | `0.9960` | 30,890,000.00 USD | 30,890,000.00 USD | 0.00 USD | 107,780.00 USD | 55,790.00 USD | 291,980.00 USD |
| `7D` | `0.9980` | 31,330,000.00 USD | 31,330,000.00 USD | 0.00 USD | 238,490.00 USD | 42,080.00 USD | 163,410.00 USD |
| `7D` | `1.00` | 31,550,000.00 USD | 31,550,000.00 USD | 0.00 USD | 94,210.00 USD | 53,610.00 USD | 65,960.00 USD |
| `7D` | `1.00` | 31,970,000.00 USD | 31,970,000.00 USD | 0.00 USD | 250,490.00 USD | 49,140.00 USD | 126,410.00 USD |
| `7D` | `1.00` | 32,330,000.00 USD | 32,330,000.00 USD | 0.00 USD | 148,700.00 USD | 47,010.00 USD | 157,970.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `555.53M` | Total OI Tokens: `631,581,808.7 SUI`
  * 1h OI Change: `-0.73%` | 4h OI Change: `-4.66%` | 24h OI Change: `-10.74%`
  * Exchange Breakdown: Binance=`98.99M` | Bybit=`74.38M` | OKX=`32.50M` | Hyperliquid=`29.40M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.22K` | Last 24h: `2.87K` | Last 3d: `42.29K` | Last 7d: `152.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0071%` | **USDT OKX** | `-0.0010%` |
| **USDT Bybit** | `-0.0051%` | **USDT KuCoin** | `0.0097%` |
| **USDT MEXC** | `0.0071%` | **USDT BingX** | `0.0070%` |
| **USDT Gate** | `0.0026%` | **USDT Bitget** | `-0.0097%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SUI` | `48.26%` | `51.74%` | `0.93` | 3,050,000.00 USD |
| `15M` | `Binance` | `48.28%` | `51.72%` | `0.93` | 692,180.00 USD |
| `15M` | `OKX` | `50.18%` | `49.82%` | `1.01` | 106,540.00 USD |
| `15M` | `Bybit` | `44.4%` | `55.6%` | `0.80` | 100,730.00 USD |
| `15M` | `KuCoin` | `34.19%` | `65.81%` | `0.52` | 13,430.00 USD |
| `15M` | `Gate` | `37.41%` | `62.59%` | `0.60` | 44,810.00 USD |
| `15M` | `Bitget` | `30.57%` | `69.43%` | `0.44` | 17,020.00 USD |
| `15M` | `BingX` | `42.05%` | `57.95%` | `0.73` | 1,040,000.00 USD |
| `15M` | `MEXC` | `35.59%` | `64.41%` | `0.55` | 292,720.00 USD |
| `15M` | `Bitunix` | `54.26%` | `45.74%` | `1.19` | 41,200.00 USD |
| `15M` | `Hyperliquid` | `19.79%` | `80.21%` | `0.25` | 28,390.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `26.9%` | `73.1%` | `0.37` | 294,330.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 13.53 USD |
| `15M` | `WhiteBIT` | `99.6%` | `0.4%` | `249.00` | 343,780.00 USD |
| `15M` | `HTX` | `97.21%` | `2.79%` | `34.84` | 897.15 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `48.96%` | `51.04%` | `0.96` | 27,370.00 USD |
| `15M` | `Aster` | `5.57%` | `94.43%` | `0.06` | 618.09 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `2.05%` | `97.95%` | `0.02` | 8,750.00 USD |
| `15M` | `Whale Positions` | `48.28%` | `51.72%` | `0.93` | 692,180.00 USD |
| `15M` | `Global Accounts` | `48.26%` | `51.74%` | `0.93` | 3,050,000.00 USD |
| `1H` | `SUI` | `45.21%` | `54.79%` | `0.83` | 22,770,000.00 USD |
| `1H` | `Binance` | `43.94%` | `56.06%` | `0.78` | 8,560,000.00 USD |
| `1H` | `OKX` | `47.18%` | `52.82%` | `0.89` | 2,450,000.00 USD |
| `1H` | `Bybit` | `46.84%` | `53.16%` | `0.88` | 1,670,000.00 USD |
| `1H` | `KuCoin` | `55.29%` | `44.71%` | `1.24` | 359,270.00 USD |
| `1H` | `Gate` | `49.61%` | `50.39%` | `0.98` | 865,710.00 USD |
| `1H` | `Bitget` | `46.03%` | `53.97%` | `0.85` | 959,240.00 USD |
| `1H` | `BingX` | `10.29%` | `89.71%` | `0.11` | 2,320,000.00 USD |
| `1H` | `MEXC` | `50.04%` | `49.96%` | `1.00` | 2,950,000.00 USD |
| `1H` | `Bitunix` | `54.07%` | `45.93%` | `1.18` | 958,270.00 USD |
| `1H` | `Hyperliquid` | `36.46%` | `63.54%` | `0.57` | 173,330.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `38.17%` | `61.83%` | `0.62` | 236,640.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.48%` | `0.52%` | `191.31` | 1,090,000.00 USD |
| `1H` | `HTX` | `49.61%` | `50.39%` | `0.98` | 45,920.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `29.06%` | `70.94%` | `0.41` | 111,060.00 USD |
| `1H` | `Aster` | `9.5%` | `90.5%` | `0.10` | 16,100.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `29.97%` | `70.03%` | `0.43` | 4,770.00 USD |
| `1H` | `Whale Positions` | `43.94%` | `56.06%` | `0.78` | 8,560,000.00 USD |
| `1H` | `Global Accounts` | `45.21%` | `54.79%` | `0.83` | 22,770,000.00 USD |
| `4H` | `SUI` | `46.20%` | `53.80%` | `0.86` | 104,940,000.00 USD |
| `4H` | `Binance` | `44.58%` | `55.42%` | `0.80` | 40,830,000.00 USD |
| `4H` | `OKX` | `41.89%` | `58.11%` | `0.72` | 13,270,000.00 USD |
| `4H` | `Bybit` | `48.42%` | `51.58%` | `0.94` | 9,400,000.00 USD |
| `4H` | `KuCoin` | `47.13%` | `52.87%` | `0.89` | 1,390,000.00 USD |
| `4H` | `Gate` | `57.43%` | `42.57%` | `1.35` | 2,980,000.00 USD |
| `4H` | `Bitget` | `46.07%` | `53.93%` | `0.85` | 5,040,000.00 USD |
| `4H` | `BingX` | `23.64%` | `76.36%` | `0.31` | 5,110,000.00 USD |
| `4H` | `MEXC` | `45.22%` | `54.78%` | `0.83` | 15,590,000.00 USD |
| `4H` | `Bitunix` | `48.96%` | `51.04%` | `0.96` | 3,370,000.00 USD |
| `4H` | `Hyperliquid` | `41.63%` | `58.37%` | `0.71` | 1,500,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.18%` | `42.82%` | `1.34` | 2,200,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.85%` | `3.15%` | `30.75` | 3,410,000.00 USD |
| `4H` | `HTX` | `43.97%` | `56.03%` | `0.78` | 271,400.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.7%` | `56.3%` | `0.78` | 196,320.00 USD |
| `4H` | `Aster` | `44.84%` | `55.16%` | `0.81` | 237,770.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.29%` | `43.71%` | `1.29` | 123,360.00 USD |
| `4H` | `Whale Positions` | `44.58%` | `55.42%` | `0.80` | 40,830,000.00 USD |
| `4H` | `Global Accounts` | `46.20%` | `53.80%` | `0.86` | 104,940,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.8931` | `0.8934` | `0.8931` | `0.8971` | `0.8900` | 1,974,065.79 USD | 794,673.98 USD | 1,179,391.81 USD | -384,717.84 USD | `-19.49%` | `2B / 21S` |
| `5:00 UTC` | `0.8911` | `0.8910` | `0.8911` | `0.8931` | `0.8898` | 1,611,113.83 USD | 837,255.00 USD | 773,858.84 USD | 63,396.16 USD | `+3.93%` | `8B / 3S` |
| `0:00 UTC` | `0.8831` | `0.8870` | `0.8831` | `0.8949` | `0.8817` | 3,990,178.39 USD | 1,362,331.47 USD | 2,627,846.92 USD | -1,265,515.46 USD | `-31.72%` | `5B / 47S` |
| `5:00 UTC` | `0.8842` | `0.8841` | `0.8842` | `0.8867` | `0.8819` | 2,580,312.70 USD | 1,301,087.80 USD | 1,279,224.90 USD | 21,862.90 USD | `+0.85%` | `8B / 6S` |
| `0:00 UTC` | `0.8841` | `0.8838` | `0.8841` | `0.8874` | `0.8802` | 2,392,175.76 USD | 1,120,822.52 USD | 1,271,353.25 USD | -150,530.73 USD | `-6.29%` | `11B / 13S` |
| `5:00 UTC` | `0.8845` | `0.8853` | `0.8845` | `0.8882` | `0.8831` | 1,835,307.01 USD | 895,840.06 USD | 939,466.95 USD | -43,626.90 USD | `-2.38%` | `5B / 13S` |
| `0:00 UTC` | `0.8830` | `0.8831` | `0.8830` | `0.8848` | `0.8809` | 2,001,953.56 USD | 1,149,882.09 USD | 852,071.47 USD | 297,810.61 USD | `+14.88%` | `5B / 4S` |
| `5:00 UTC` | `0.8816` | `0.8832` | `0.8816` | `0.8862` | `0.8813` | 1,099,871.32 USD | 581,784.98 USD | 518,086.34 USD | 63,698.64 USD | `+5.79%` | `12B / 6S` |
| `0:00 UTC` | `0.8824` | `0.8824` | `0.8824` | `0.8850` | `0.8811` | 3,028,718.86 USD | 820,523.57 USD | 2,208,195.28 USD | -1,387,671.71 USD | `-45.82%` | `5B / 8S` |
| `5:00 UTC` | `0.8824` | `0.8831` | `0.8824` | `0.8847` | `0.8816` | 341,678.35 USD | 241,549.50 USD | 100,128.85 USD | 141,420.65 USD | `+41.39%` | `12B / 4S` |

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
| `5m` | -73,540.00 USD | 205,080.00 USD | **`ACCUMULATION`** |
| `15m` | -84,840.00 USD | 9,560.00 USD | **`DISTRIBUTION`** |
| `30m` | -158,270.00 USD | -1,160,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -238,080.00 USD | -960,520.00 USD | **`DISTRIBUTION`** |
| `2h` | -21,930.00 USD | -3,760,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -735,200.00 USD | -6,700,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 2,060,000.00 USD | -5,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 2,420,000.00 USD | -14,160,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,010,000.00 USD | -17,380,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,870,000.00 USD | -33,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -26,610,000.00 USD | -90,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -153,260,000.00 USD | -491,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-73.54K` | 15m=`-84.84K` | 1h=`-238.08K` | 24h=`-8.87M`
* Futures Capital Netflows: 5m=`+205.08K` | 15m=`+9.56K` | 1h=`-960.52K` | 24h=`-33.37M`
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
  * `2026-10-30 14:41:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:10:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
