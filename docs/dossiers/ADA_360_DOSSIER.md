# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:26:38 IST` (`2026-10-30 08:56:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1907` | **Live Ask Quote**: `0.1928` | **Mid Price**: `0.1918`
- **Spread Points**: `21.00` | **Spread BPS**: `109.52 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `0.1878` | VWAP Z-Score: `+0.90` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0012` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.66` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1973` | Lower -3.00σ Band: `0.1782`
  * Upper +2.51σ Band: `0.1957` | Lower -2.51σ Band: `0.1798`
  * Upper +2.01σ Band: `0.1941` | Lower -2.01σ Band: `0.1814`
  * Upper +2.00σ Band: `0.1941` | Lower -2.00σ Band: `0.1814`
  * Upper +1.28σ Band: `0.1918` | Lower -1.28σ Band: `0.1837`
  * Upper +1.00σ Band: `0.1909` | Lower -1.00σ Band: `0.1846`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1914` | EMA-20=`0.1914` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1921` (Slope: `+0.0000`) | EMA-100=`0.1943`
  * Institutional Anchors: EMA-144=`0.1959` | EMA-200=`0.1974` (Slope: `-0.3560`) | EMA-233=`0.1982`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1938` (Distance: `-1.02%`)
  * Point of Control (POC) = `0.1912` (Distance: `+0.30%`)
  * Value Area Low (VAL) = `0.1870` (Distance: `+2.56%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2065` | Weekly POC=`0.2031` | Weekly VAL=`0.1985`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1940` | Low=`0.1904`
  * New York Session (13:00-21:00 UTC): High=`0.1929` | Low=`0.1906`
  * Initial Balance (First Hour): IB High=`0.1935` | IB Low=`0.1918`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1910` - `0.1925`
  * Optimal Trade Entry (OTE 0.705): `0.1921`
  * Structural Invalidation Anchor (0.786): `0.1933`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1922` | `0.1925` | `0.1921` | `0.1922` | `1,405,071` | 270,178.84 USD | -10,474.34 USD | `-3.88%` | -4,539,398.06 USD | `+0.27` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1922` | `0.1925` | `0.1919` | `0.1922` | `2,308,179` | 443,758.37 USD | 108,549.33 USD | `+24.46%` | -4,430,848.72 USD | `+1.79` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1922` | `0.1922` | `0.1919` | `0.1919` | `221,246` | 42,486.96 USD | -35,648.95 USD | `-83.91%` | -4,466,497.67 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1924` | `0.1929` | `0.1918` | `0.1927` | `5,902,833` | 1,135,407.39 USD | 41,912.77 USD | `+3.69%` | -4,419,361.14 USD | `+0.34` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1927` | `0.1930` | `0.1922` | `0.1923` | `6,230,832` | 1,200,311.82 USD | -109,562.58 USD | `-9.13%` | -4,528,923.72 USD | `-0.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1922` | `0.1925` | `0.1919` | `0.1919` | `3,866,860` | 743,444.82 USD | 75,246.12 USD | `+10.12%` | -4,453,677.60 USD | `+0.64` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1932` | `0.1954` | `0.1929` | `0.1942` | `27,116,099` | 5,265,334.78 USD | 190,431.19 USD | `+3.62%` | -4,168,963.57 USD | `+0.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1943` | `0.1944` | `0.1919` | `0.1924` | `27,579,785` | 5,322,908.18 USD | -465,649.66 USD | `-8.75%` | -4,634,613.23 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1918` | `0.1919` | `16,068,161` | 3,092,143.39 USD | -5,223.76 USD | `-0.17%` | -4,639,836.99 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1930` | `0.1918` | `0.1921` | `16,414,569` | 3,158,656.56 USD | 45,379.14 USD | `+1.44%` | -4,858,262.56 USD | `+0.32` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,207,439.06 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -4,361,461.60 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1930` | `0.1918` | `0.1921` | `16,414,569` | 3,158,656.56 USD | 45,379.14 USD | `+1.44%` | -4,858,262.56 USD | `+0.32` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.1918`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `546` | `0x77ee...2902` | `SHORT` | 4,115,894.37 USD | `21,412,192.00` | `0.1911` | `0.1927` | `0.5942` | -24,642.63 USD | `-0.60%` | `10X Cross` |
| `1237` | `0x123d...3bff` | `LONG` | 1,804,276.40 USD | `9,392,870.00` | `0.2912` | `0.1927` | `0.000000` | -931,380.32 USD | `-51.62%` | `10X Cross` |
| `1272` | `0x7737...bf66` | `SHORT` | 1,747,107.02 USD | `9,091,466.00` | `0.2190` | `0.1927` | `2.13` | 243,882.78 USD | `+13.96%` | `10X Cross` |
| `1577` | `0x5f94...4b96` | `SHORT` | 1,375,308.30 USD | `7,162,318.00` | `0.2303` | `0.1927` | `0.7070` | 274,166.89 USD | `+19.93%` | `10X Cross` |
| `1810` | `0x4982...59e6` | `SHORT` | 1,151,351.99 USD | `5,998,812.00` | `0.1891` | `0.1927` | `0.4125` | -16,793.62 USD | `-1.46%` | `10X Cross` |
| `1848` | `0xcac1...26b3` | `LONG` | 1,115,572.81 USD | `5,803,927.00` | `0.2000` | `0.1927` | `0.000000` | -45,242.78 USD | `-4.06%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1988` | 5,254.95 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.25K USD at 0.1988 USD [API] | `2026-10-29 08:20:17` |
| `ANNOUNCEMENT` | `INFO` | `0.1987` | 6,648.05 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.1987 USD [API] | `2026-10-29 08:20:17` |
| `ANNOUNCEMENT` | `INFO` | `0.1999` | 5,011.50 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.01K USD at 0.1999 USD [API] | `2026-10-29 09:25:32` |
| `ANNOUNCEMENT` | `INFO` | `0.1999` | 5,009.99 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.01K USD at 0.1999 USD [API] | `2026-10-29 09:25:14` |
| `ANNOUNCEMENT` | `INFO` | `0.1994` | 6,650.46 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.1994 USD [API] | `2026-10-29 09:34:07` |
| `ANNOUNCEMENT` | `INFO` | `0.2143` | 1,259.11 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 1.26K USD at 0.2143 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `0.2242` | 4,031.56 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 4.03K USD at 0.2242 USD [API] | `2026-10-08 17:25:15` |
| `ANNOUNCEMENT` | `INFO` | `0.2242` | 389.90 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.39K USD at 0.2242 USD [API] | `2026-10-08 17:25:15` |
| `ANNOUNCEMENT` | `INFO` | `0.2003` | 6,637.14 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.64K USD at 0.2003 USD [API] | `2026-10-29 12:02:00` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 2.82 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.00K USD at 0.2016 USD [API] | `2026-10-29 13:10:03` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 9,363.57 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 9.36K USD at 0.2016 USD [API] | `2026-10-29 13:27:51` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 9,285.95 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 9.29K USD at 0.2016 USD [API] | `2026-10-29 13:27:51` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 9,970.42 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 9.97K USD at 0.2016 USD [API] | `2026-10-29 13:27:51` |
| `ANNOUNCEMENT` | `INFO` | `0.2009` | 5,006.19 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2009 USD [API] | `2026-10-29 13:44:17` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 269.55 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.27K USD at 0.2051 USD [API] | `2026-08-26 14:48:31` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 291.91 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.29K USD at 0.2051 USD [API] | `2026-08-26 14:48:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2099` (Vol: 189,000.00 USD, Dist: `+9.50%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.52%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+9.15%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.54%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 325,500.00 USD, Dist: `+11.50%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.54%`)
  * 7D Horizon: Short MP=`0.2131` (Vol: 448,200.00 USD, Dist: `+11.17%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--4.45%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0405` | 803.68 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 232.20 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 103.16 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 509.19 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 2,790.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 553.50 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 175.69 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,510.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 225.52 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 7,510.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 1,130.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 603.75 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 152,990.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 935.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 17,130.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 170.04 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 89,250.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 150.44 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 2,200.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 420.22 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 317.55 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 25,640.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 359.57 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 119.08 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 20,430.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,640.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 169.34 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 1,180.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,420.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 3,910.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 5,700.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 26,900.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 403.77 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 357.96 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 314.44 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,540.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 958.46 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,330.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 9,150.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 292.94 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 1,360.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,720.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,830.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 2,350.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 42,630.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,050.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 12,420.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 532,970.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 166,980.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 2,780.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,580.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 4,200.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,180.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1640` | 8,340,000.00 USD | 8,340,000.00 USD | 166,770.00 USD | 55,610.00 USD | 217,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,840.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1650` | 7,900,000.00 USD | 7,900,000.00 USD | 57,340.00 USD | 18,500.00 USD | 42,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 7,860.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1660` | 7,780,000.00 USD | 7,780,000.00 USD | 88,950.00 USD | 31,770.00 USD | 105,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1665` | 889.94 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1670` | 7,550,000.00 USD | 7,550,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1680` | 7,450,000.00 USD | 7,450,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1685` | 12,160.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1690` | 7,370,000.00 USD | 7,370,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1695` | 79,290.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1700` | 7,270,000.00 USD | 7,270,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1710` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 386,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1720` | 7,170,000.00 USD | 7,170,000.00 USD | 9,500.00 USD | 2,920.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 134,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 8,230,000.00 USD | 8,230,000.00 USD | 87,640.00 USD | 24,080.00 USD | 128,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1730` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 332.90 USD | 82,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 658.61 USD | 100,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 7,990,000.00 USD | 7,990,000.00 USD | 23,910.00 USD | 15,040.00 USD | 9,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1740` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 3,560.00 USD | 32,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1750` | 7,940,000.00 USD | 7,940,000.00 USD | 50,710.00 USD | 15,820.00 USD | 14,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1750` | 7,000,000.00 USD | 7,000,000.00 USD | 7,610.00 USD | 6,730.00 USD | 25,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 17,080.00 USD | 100,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 7,860,000.00 USD | 7,860,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1760` | 6,960,000.00 USD | 6,960,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 42,760.00 USD | 83,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 7,790,000.00 USD | 7,790,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1770` | 6,940,000.00 USD | 6,940,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 40,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 7,480,000.00 USD | 7,480,000.00 USD | 77,450.00 USD | 15,460.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1780` | 6,680,000.00 USD | 6,680,000.00 USD | 140,230.00 USD | 12,660.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 39,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 7,340,000.00 USD | 7,340,000.00 USD | 130,180.00 USD | 52,650.00 USD | 95,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 6,470,000.00 USD | 6,470,000.00 USD | 9,850.00 USD | 27,990.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 34,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 7,060,000.00 USD | 7,060,000.00 USD | 756,150.00 USD | 103,250.00 USD | 195,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 6,320,000.00 USD | 6,320,000.00 USD | 464,090.00 USD | 95,830.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 16,340.00 USD | 30,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 6,000,000.00 USD | 6,000,000.00 USD | 160,190.00 USD | 59,050.00 USD | 169,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 5,620,000.00 USD | 5,620,000.00 USD | 354,390.00 USD | 45,990.00 USD | 179,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 4,070.00 USD | 14,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 5,610,000.00 USD | 5,610,000.00 USD | 432,620.00 USD | 95,990.00 USD | 318,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 5,040,000.00 USD | 5,040,000.00 USD | 123,330.00 USD | 62,450.00 USD | 444,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 7,950.00 USD | 10,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 4,770,000.00 USD | 4,770,000.00 USD | 436,420.00 USD | 44,980.00 USD | 65,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 4,410,000.00 USD | 4,410,000.00 USD | 435,140.00 USD | 47,220.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 870.52 USD | 870.52 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 4,220,000.00 USD | 4,220,000.00 USD | 361,330.00 USD | 81,330.00 USD | 185,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 3,890,000.00 USD | 3,890,000.00 USD | 273,040.00 USD | 41,950.00 USD | 192,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,300.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 3,590,000.00 USD | 3,590,000.00 USD | 56,030.00 USD | 39,720.00 USD | 116,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 3,380,000.00 USD | 3,380,000.00 USD | 50,160.00 USD | 6,440.00 USD | 228,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 3,380,000.00 USD | 3,380,000.00 USD | 171,630.00 USD | 44,670.00 USD | 430,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 3,100,000.00 USD | 3,100,000.00 USD | 70,810.00 USD | 15,200.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 2,730,000.00 USD | 2,730,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 3,010,000.00 USD | 3,010,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 2,160,000.00 USD | 2,160,000.00 USD | 199,290.00 USD | 172,440.00 USD | 196,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 2,520,000.00 USD | 2,520,000.00 USD | 132,450.00 USD | 103,170.00 USD | 670,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 1,590,000.00 USD | 1,590,000.00 USD | 217,970.00 USD | 38,240.00 USD | 93,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 1,610,000.00 USD | 1,610,000.00 USD | 510,390.00 USD | 12,880.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,240,000.00 USD | 1,240,000.00 USD | 93,550.00 USD | 128,280.00 USD | 299,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 1,060,000.00 USD | 1,060,000.00 USD | 255,740.00 USD | 30,390.00 USD | 216,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 722,800.00 USD | 722,800.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 553,650.00 USD | 553,650.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1920` | 11,060.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1920` | 22,110.00 USD | 22,110.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 600,250.00 USD | 600,250.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 1,200,000.00 USD | 1,200,000.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 479,440.00 USD | 479,440.00 USD | 284,520.00 USD | 2,420.00 USD | 170,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1930` | 2,180,000.00 USD | 2,180,000.00 USD | 653,060.00 USD | 0.00 USD | 331,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 853,680.00 USD | 853,680.00 USD | 21,310.00 USD | 356.90 USD | 352,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 2,530,000.00 USD | 2,530,000.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 1,370,000.00 USD | 1,370,000.00 USD | 25,540.00 USD | 73,330.00 USD | 413,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1950` | 3,430,000.00 USD | 3,430,000.00 USD | 693,070.00 USD | 1,990.00 USD | 203,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 2,560,000.00 USD | 2,560,000.00 USD | 429,500.00 USD | 243,130.00 USD | 524,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 5,020,000.00 USD | 5,020,000.00 USD | 236,660.00 USD | 112,940.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 975.46 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 3,070,000.00 USD | 3,070,000.00 USD | 96,390.00 USD | 115,800.00 USD | 290,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1970` | 5,340,000.00 USD | 5,340,000.00 USD | 13,930.00 USD | 32,990.00 USD | 275,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 3,960,000.00 USD | 3,960,000.00 USD | 409,930.00 USD | 110,510.00 USD | 378,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1980` | 6,010,000.00 USD | 6,010,000.00 USD | 312,350.00 USD | 44,250.00 USD | 315,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 1,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 4,530,000.00 USD | 4,530,000.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1990` | 6,320,000.00 USD | 6,320,000.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 1,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 5,340,000.00 USD | 5,340,000.00 USD | 342,800.00 USD | 70,120.00 USD | 400,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2000` | 6,790,000.00 USD | 6,790,000.00 USD | 56,530.00 USD | 38,390.00 USD | 371,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 5,990,000.00 USD | 5,990,000.00 USD | 159,370.00 USD | 162,580.00 USD | 326,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 7,510,000.00 USD | 7,510,000.00 USD | 335,650.00 USD | 25,310.00 USD | 359,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 2,100.00 USD | 6,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 6,470,000.00 USD | 6,470,000.00 USD | 223,790.00 USD | 75,610.00 USD | 179,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 8,140,000.00 USD | 8,140,000.00 USD | 87,710.00 USD | 52,030.00 USD | 495,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 1,050.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 6,840,000.00 USD | 6,840,000.00 USD | 124,930.00 USD | 93,750.00 USD | 154,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 8,410,000.00 USD | 8,410,000.00 USD | 15,840.00 USD | 94,230.00 USD | 153,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2035` | 137.57 USD | 7,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2040` | 7,180,000.00 USD | 7,180,000.00 USD | 82,600.00 USD | 120,640.00 USD | 133,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 8,550,000.00 USD | 8,550,000.00 USD | 59,380.00 USD | 76,320.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 7,350,000.00 USD | 7,350,000.00 USD | 86,770.00 USD | 31,580.00 USD | 52,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 8,640,000.00 USD | 8,640,000.00 USD | 37,210.00 USD | 1,160.00 USD | 57,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 7,790,000.00 USD | 7,790,000.00 USD | 311,840.00 USD | 31,930.00 USD | 92,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 8,820,000.00 USD | 8,820,000.00 USD | 149,740.00 USD | 18,480.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 8,360,000.00 USD | 8,360,000.00 USD | 255,320.00 USD | 118,740.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 9,440,000.00 USD | 9,440,000.00 USD | 439,210.00 USD | 141,790.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2075` | 2,220.00 USD | 9,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2080` | 8,830,000.00 USD | 8,830,000.00 USD | 331,850.00 USD | 94,230.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 10,130,000.00 USD | 10,130,000.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 9,780,000.00 USD | 9,780,000.00 USD | 491,160.00 USD | 154,050.00 USD | 300,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 13,070,000.00 USD | 13,070,000.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 10,560,000.00 USD | 10,560,000.00 USD | 463,870.00 USD | 102,770.00 USD | 210,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 17,150,000.00 USD | 17,150,000.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 10,850,000.00 USD | 10,850,000.00 USD | 131,380.00 USD | 39,260.00 USD | 124,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 20,340,000.00 USD | 20,340,000.00 USD | 1,060,000.00 USD | 511,730.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 11,210,000.00 USD | 11,210,000.00 USD | 136,500.00 USD | 84,890.00 USD | 135,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 23,340,000.00 USD | 23,340,000.00 USD | 1,160,000.00 USD | 466,390.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2130` | 11,570,000.00 USD | 11,570,000.00 USD | 212,500.00 USD | 59,020.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 26,160,000.00 USD | 26,160,000.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 11,750,000.00 USD | 11,750,000.00 USD | 130,000.00 USD | 31,520.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 28,260,000.00 USD | 28,260,000.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 30,520,000.00 USD | 30,520,000.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 467.20 USD | 10,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2160` | 31,550,000.00 USD | 31,550,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 14,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2185` | 2,650.00 USD | 16,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2215` | 996.75 USD | 17,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 17,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 20,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 29,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2315` | 226.87 USD | 29,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 29,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 37,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 620.11 USD | 38,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,670.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 680.06 USD | 40,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 41,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 3,830.00 USD | 45,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 45,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2625` | 1,120.00 USD | 46,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2655` | 409.93 USD | 47,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 1,970.00 USD | 49,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 49,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 49,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 51,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 52,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 55,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 56,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 9,510.00 USD | 65,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2995` | 4,040.00 USD | 69,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 69,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 1,120.00 USD | 70,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 68,960.00 USD | 139,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 140,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3065` | 206.58 USD | 140,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 2,710.00 USD | 143,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,190.00 USD | 240,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3135` | 297.82 USD | 240,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 1,100.00 USD | 241,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 3,640.00 USD | 245,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 37,820.00 USD | 283,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 285,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 238.07 USD | 285,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3435` | 314.30 USD | 286,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 202,010.00 USD | 488,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,120.00 USD | 489,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 142.96 USD | 489,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3605` | 5,100.00 USD | 494,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 2,940.00 USD | 497,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 143.91 USD | 497,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3635` | 261,990.00 USD | 759,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3655` | 163.38 USD | 759,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3665` | 366.50 USD | 760,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 769,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3725` | 947.27 USD | 770,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3735` | 28,010.00 USD | 798,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 801,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3795` | 24,090.00 USD | 825,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0405` | 2,440,000.00 USD | 0.00 USD | 803.68 USD | `-78.95%` | `19,844.00` |
| `Live` | `Long` | `0.0435` | 2,440,000.00 USD | 0.00 USD | 232.20 USD | `-77.39%` | `5,338.00` |
| `Live` | `Long` | `0.0485` | 2,440,000.00 USD | 0.00 USD | 103.16 USD | `-74.79%` | `2,127.00` |
| `Live` | `Long` | `0.0545` | 2,440,000.00 USD | 0.00 USD | 509.19 USD | `-71.67%` | `9,343.00` |
| `Live` | `Long` | `0.0575` | 2,430,000.00 USD | 0.00 USD | 2,790.00 USD | `-70.11%` | `48,444.00` |
| `Live` | `Long` | `0.0615` | 2,430,000.00 USD | 0.00 USD | 553.50 USD | `-68.04%` | `9,000.00` |
| `Live` | `Long` | `0.0625` | 2,430,000.00 USD | 0.00 USD | 175.69 USD | `-67.52%` | `2,811.00` |
| `Live` | `Long` | `0.0635` | 2,430,000.00 USD | 0.00 USD | 1,510.00 USD | `-67.00%` | `23,814.00` |
| `Live` | `Long` | `0.0655` | 2,430,000.00 USD | 0.00 USD | 225.52 USD | `-65.96%` | `3,443.00` |
| `Live` | `Long` | `0.0715` | 2,430,000.00 USD | 0.00 USD | 7,510.00 USD | `-62.84%` | `105,008.00` |
| `Live` | `Long` | `0.0725` | 2,420,000.00 USD | 0.00 USD | 1,130.00 USD | `-62.32%` | `15,628.00` |
| `Live` | `Long` | `0.0805` | 2,420,000.00 USD | 0.00 USD | 603.75 USD | `-58.16%` | `7,500.00` |
| `Live` | `Long` | `0.0815` | 2,420,000.00 USD | 0.00 USD | 152,990.00 USD | `-57.64%` | `1,877,198.00` |
| `Live` | `Long` | `0.0865` | 2,270,000.00 USD | 0.00 USD | 102.50 USD | `-55.04%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,270,000.00 USD | 0.00 USD | 344.75 USD | `-54.52%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,270,000.00 USD | 0.00 USD | 1,150.00 USD | `-54.00%` | `13,050.00` |
| `Live` | `Long` | `0.0925` | 2,270,000.00 USD | 0.00 USD | 165.11 USD | `-51.92%` | `1,785.00` |
| `Live` | `Long` | `0.0935` | 2,270,000.00 USD | 0.00 USD | 935.00 USD | `-51.40%` | `10,000.00` |
| `Live` | `Long` | `0.0945` | 2,260,000.00 USD | 0.00 USD | 327.54 USD | `-50.88%` | `3,466.00` |
| `Live` | `Long` | `0.0955` | 2,260,000.00 USD | 0.00 USD | 17,130.00 USD | `-50.36%` | `179,410.00` |
| `Live` | `Long` | `0.0975` | 2,250,000.00 USD | 0.00 USD | 170.04 USD | `-49.32%` | `1,744.00` |
| `Live` | `Long` | `0.0985` | 2,250,000.00 USD | 0.00 USD | 89,250.00 USD | `-48.80%` | `906,128.00` |
| `Live` | `Long` | `0.1025` | 2,160,000.00 USD | 0.00 USD | 4,100.00 USD | `-46.73%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,150,000.00 USD | 0.00 USD | 1,050.00 USD | `-46.21%` | `10,149.00` |
| `Live` | `Long` | `0.1055` | 2,150,000.00 USD | 0.00 USD | 150.44 USD | `-45.17%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,150,000.00 USD | 0.00 USD | 653.70 USD | `-44.65%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,150,000.00 USD | 0.00 USD | 2,200.00 USD | `-44.13%` | `20,486.00` |
| `Live` | `Long` | `0.1085` | 2,150,000.00 USD | 0.00 USD | 420.22 USD | `-43.61%` | `3,873.00` |
| `Live` | `Long` | `0.1095` | 2,150,000.00 USD | 0.00 USD | 317.55 USD | `-43.09%` | `2,900.00` |
| `Live` | `Long` | `0.1115` | 2,150,000.00 USD | 0.00 USD | 25,640.00 USD | `-42.05%` | `229,972.00` |
| `Live` | `Long` | `0.1135` | 2,120,000.00 USD | 0.00 USD | 359.57 USD | `-41.01%` | `3,168.00` |
| `Live` | `Long` | `0.1145` | 2,120,000.00 USD | 0.00 USD | 862.64 USD | `-40.49%` | `7,534.00` |
| `Live` | `Long` | `0.1155` | 2,120,000.00 USD | 0.00 USD | 119.08 USD | `-39.97%` | `1,031.00` |
| `Live` | `Long` | `0.1165` | 2,120,000.00 USD | 0.00 USD | 20,430.00 USD | `-39.45%` | `175,372.00` |
| `Live` | `Long` | `0.1175` | 2,100,000.00 USD | 0.00 USD | 1,640.00 USD | `-38.93%` | `13,927.00` |
| `Live` | `Long` | `0.1185` | 2,100,000.00 USD | 0.00 USD | 169.34 USD | `-38.41%` | `1,429.00` |
| `Live` | `Long` | `0.1205` | 2,100,000.00 USD | 0.00 USD | 826.27 USD | `-37.37%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,100,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.85%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,100,000.00 USD | 0.00 USD | 1,180.00 USD | `-35.81%` | `9,522.00` |
| `Live` | `Long` | `0.1245` | 2,100,000.00 USD | 0.00 USD | 404.62 USD | `-35.29%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,100,000.00 USD | 0.00 USD | 2,420.00 USD | `-34.77%` | `19,273.00` |
| `Live` | `Long` | `0.1265` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-34.25%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,090,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.73%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,090,000.00 USD | 0.00 USD | 2,540.00 USD | `-32.69%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,090,000.00 USD | 0.00 USD | 13,060.00 USD | `-32.17%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,080,000.00 USD | 0.00 USD | 3,910.00 USD | `-31.65%` | `29,734.00` |
| `Live` | `Long` | `0.1325` | 2,070,000.00 USD | 0.00 USD | 6,960.00 USD | `-31.13%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,070,000.00 USD | 0.00 USD | 5,700.00 USD | `-30.61%` | `42,702.00` |
| `Live` | `Long` | `0.1345` | 2,060,000.00 USD | 0.00 USD | 26,900.00 USD | `-30.09%` | `200,000.00` |
| `Live` | `Long` | `0.1355` | 2,030,000.00 USD | 0.00 USD | 106.64 USD | `-29.57%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,030,000.00 USD | 0.00 USD | 403.77 USD | `-29.05%` | `2,958.00` |
| `Live` | `Long` | `0.1395` | 2,030,000.00 USD | 0.00 USD | 357.96 USD | `-27.49%` | `2,566.00` |
| `Live` | `Long` | `0.1405` | 2,030,000.00 USD | 0.00 USD | 314.44 USD | `-26.98%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,030,000.00 USD | 0.00 USD | 9,540.00 USD | `-26.46%` | `67,399.00` |
| `Live` | `Long` | `0.1425` | 2,020,000.00 USD | 0.00 USD | 958.46 USD | `-25.94%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,020,000.00 USD | 0.00 USD | 15,780.00 USD | `-25.42%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,010,000.00 USD | 0.00 USD | 2,330.00 USD | `-24.90%` | `16,111.00` |
| `Live` | `Long` | `0.1455` | 2,000,000.00 USD | 0.00 USD | 3,770.00 USD | `-24.38%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 2,000,000.00 USD | 0.00 USD | 9,150.00 USD | `-23.86%` | `62,427.00` |
| `Live` | `Long` | `0.1475` | 1,990,000.00 USD | 0.00 USD | 292.94 USD | `-23.34%` | `1,986.00` |
| `Live` | `Long` | `0.1485` | 1,990,000.00 USD | 0.00 USD | 1,360.00 USD | `-22.82%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 1,990,000.00 USD | 0.00 USD | 427.12 USD | `-22.30%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 1,990,000.00 USD | 0.00 USD | 1,720.00 USD | `-21.78%` | `11,458.00` |
| `Live` | `Long` | `0.1515` | 1,990,000.00 USD | 0.00 USD | 35,830.00 USD | `-21.26%` | `236,501.00` |
| `Live` | `Long` | `0.1525` | 1,950,000.00 USD | 0.00 USD | 2,350.00 USD | `-20.74%` | `15,391.00` |
| `Live` | `Long` | `0.1535` | 1,950,000.00 USD | 0.00 USD | 42,630.00 USD | `-20.22%` | `277,705.00` |
| `Live` | `Long` | `0.1545` | 1,910,000.00 USD | 0.00 USD | 721.05 USD | `-19.70%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,910,000.00 USD | 0.00 USD | 1,050.00 USD | `-19.18%` | `6,772.00` |
| `Live` | `Long` | `0.1565` | 1,900,000.00 USD | 0.00 USD | 12,420.00 USD | `-18.66%` | `79,342.00` |
| `Live` | `Long` | `0.1575` | 1,890,000.00 USD | 0.00 USD | 532,970.00 USD | `-18.14%` | `3,383,905.00` |
| `Live` | `Long` | `0.1585` | 1,360,000.00 USD | 0.00 USD | 166,980.00 USD | `-17.62%` | `1,053,495.00` |
| `Live` | `Long` | `0.1595` | 1,190,000.00 USD | 0.00 USD | 2,780.00 USD | `-17.10%` | `17,408.00` |
| `Live` | `Long` | `0.1605` | 1,190,000.00 USD | 0.00 USD | 57,580.00 USD | `-16.58%` | `358,740.00` |
| `Live` | `Long` | `0.1615` | 1,130,000.00 USD | 0.00 USD | 4,200.00 USD | `-16.06%` | `26,015.00` |
| `Live` | `Long` | `0.1625` | 1,130,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.54%` | `13,446.00` |
| `Live` | `Long` | `0.1645` | 1,120,000.00 USD | 0.00 USD | 10,840.00 USD | `-14.50%` | `65,896.00` |
| `Live` | `Long` | `0.1655` | 1,110,000.00 USD | 0.00 USD | 7,860.00 USD | `-13.98%` | `47,504.00` |
| `Live` | `Long` | `0.1665` | 1,110,000.00 USD | 0.00 USD | 889.94 USD | `-13.46%` | `5,345.00` |
| `Live` | `Long` | `0.1675` | 1,110,000.00 USD | 0.00 USD | 630.81 USD | `-12.94%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,100,000.00 USD | 0.00 USD | 12,160.00 USD | `-12.42%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,090,000.00 USD | 0.00 USD | 79,290.00 USD | `-11.90%` | `467,760.00` |
| `Live` | `Long` | `0.1705` | 1,010,000.00 USD | 0.00 USD | 626,600.00 USD | `-11.38%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 386,710.00 USD | 0.00 USD | 252,270.00 USD | `-10.86%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 134,440.00 USD | 0.00 USD | 33,550.00 USD | `-10.34%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 100,890.00 USD | 0.00 USD | 658.61 USD | `-9.82%` | `3,796.00` |
| `Live` | `Long` | `0.1755` | 100,230.00 USD | 0.00 USD | 17,080.00 USD | `-8.78%` | `97,301.00` |
| `Live` | `Long` | `0.1765` | 83,150.00 USD | 0.00 USD | 42,760.00 USD | `-8.26%` | `242,276.00` |
| `Live` | `Long` | `0.1775` | 40,390.00 USD | 0.00 USD | 1,360.00 USD | `-7.74%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 39,030.00 USD | 0.00 USD | 4,530.00 USD | `-7.22%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 34,500.00 USD | 0.00 USD | 3,840.00 USD | `-6.70%` | `21,396.00` |
| `Live` | `Long` | `0.1805` | 30,660.00 USD | 0.00 USD | 16,340.00 USD | `-6.19%` | `90,542.00` |
| `Live` | `Long` | `0.1815` | 14,320.00 USD | 0.00 USD | 4,070.00 USD | `-5.67%` | `22,444.00` |
| `Live` | `Long` | `0.1825` | 10,250.00 USD | 0.00 USD | 7,950.00 USD | `-5.15%` | `43,548.00` |
| `Live` | `Short` | `0.1835` | 870.52 USD | 870.52 USD | 0.00 USD | `-4.63%` | `4,744.00` |
| `Live` | `Long` | `0.1845` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | `-4.11%` | `12,457.00` |
| `Live` | `Short` | `0.1965` | 975.46 USD | 104.93 USD | 0.00 USD | `+2.13%` | `534.00` |
| `Live` | `Short` | `0.1985` | 1,310.00 USD | 338.64 USD | 0.00 USD | `+3.17%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 1,570.00 USD | 252.97 USD | 0.00 USD | `+3.69%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 4,140.00 USD | 2,570.00 USD | 0.00 USD | `+4.21%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 6,240.00 USD | 2,100.00 USD | 0.00 USD | `+4.73%` | `10,418.00` |
| `Live` | `Short` | `0.2025` | 7,290.00 USD | 1,050.00 USD | 0.00 USD | `+5.25%` | `5,169.00` |
| `Live` | `Short` | `0.2035` | 7,420.00 USD | 137.57 USD | 0.00 USD | `+5.77%` | `676.00` |
| `Live` | `Short` | `0.2075` | 9,640.00 USD | 2,220.00 USD | 0.00 USD | `+7.85%` | `10,683.00` |
| `Live` | `Short` | `0.2155` | 10,110.00 USD | 467.20 USD | 0.00 USD | `+12.01%` | `2,168.00` |
| `Live` | `Short` | `0.2175` | 14,040.00 USD | 3,930.00 USD | 0.00 USD | `+13.05%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 16,690.00 USD | 2,650.00 USD | 0.00 USD | `+13.57%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 17,690.00 USD | 996.75 USD | 0.00 USD | `+15.12%` | `4,500.00` |
| `Live` | `Short` | `0.2235` | 17,890.00 USD | 200.48 USD | 0.00 USD | `+16.16%` | `897.00` |
| `Live` | `Short` | `0.2265` | 20,120.00 USD | 2,230.00 USD | 0.00 USD | `+17.72%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 29,360.00 USD | 9,240.00 USD | 0.00 USD | `+18.76%` | `40,428.00` |
| `Live` | `Short` | `0.2315` | 29,580.00 USD | 226.87 USD | 0.00 USD | `+20.32%` | `980.00` |
| `Live` | `Short` | `0.2325` | 29,870.00 USD | 282.02 USD | 0.00 USD | `+20.84%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 37,500.00 USD | 7,640.00 USD | 0.00 USD | `+21.36%` | `32,708.00` |
| `Live` | `Short` | `0.2375` | 38,120.00 USD | 620.11 USD | 0.00 USD | `+23.44%` | `2,611.00` |
| `Live` | `Short` | `0.2405` | 39,800.00 USD | 1,670.00 USD | 0.00 USD | `+25.00%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 40,480.00 USD | 680.06 USD | 0.00 USD | `+25.52%` | `2,816.00` |
| `Live` | `Short` | `0.2425` | 41,550.00 USD | 1,080.00 USD | 0.00 USD | `+26.04%` | `4,435.00` |
| `Live` | `Short` | `0.2445` | 45,390.00 USD | 3,830.00 USD | 0.00 USD | `+27.08%` | `15,682.00` |
| `Live` | `Short` | `0.2585` | 45,770.00 USD | 380.25 USD | 0.00 USD | `+34.36%` | `1,471.00` |
| `Live` | `Short` | `0.2625` | 46,880.00 USD | 1,120.00 USD | 0.00 USD | `+36.43%` | `4,254.00` |
| `Live` | `Short` | `0.2655` | 47,290.00 USD | 409.93 USD | 0.00 USD | `+37.99%` | `1,544.00` |
| `Live` | `Short` | `0.2675` | 49,260.00 USD | 1,970.00 USD | 0.00 USD | `+39.03%` | `7,372.00` |
| `Live` | `Short` | `0.2715` | 49,380.00 USD | 120.00 USD | 0.00 USD | `+41.11%` | `442.00` |
| `Live` | `Short` | `0.2775` | 49,760.00 USD | 379.62 USD | 0.00 USD | `+44.23%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 51,940.00 USD | 2,170.00 USD | 0.00 USD | `+47.87%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 52,350.00 USD | 411.09 USD | 0.00 USD | `+50.47%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 55,610.00 USD | 3,260.00 USD | 0.00 USD | `+51.51%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 56,130.00 USD | 519.79 USD | 0.00 USD | `+52.55%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 65,640.00 USD | 9,510.00 USD | 0.00 USD | `+53.59%` | `32,186.00` |
| `Live` | `Short` | `0.2995` | 69,690.00 USD | 4,040.00 USD | 0.00 USD | `+55.67%` | `13,504.00` |
| `Live` | `Short` | `0.3005` | 69,830.00 USD | 146.34 USD | 0.00 USD | `+56.19%` | `487.00` |
| `Live` | `Short` | `0.3015` | 70,950.00 USD | 1,120.00 USD | 0.00 USD | `+56.70%` | `3,713.00` |
| `Live` | `Short` | `0.3045` | 139,920.00 USD | 68,960.00 USD | 0.00 USD | `+58.26%` | `226,480.00` |
| `Live` | `Short` | `0.3055` | 140,320.00 USD | 408.15 USD | 0.00 USD | `+58.78%` | `1,336.00` |
| `Live` | `Short` | `0.3065` | 140,530.00 USD | 206.58 USD | 0.00 USD | `+59.30%` | `674.00` |
| `Live` | `Short` | `0.3085` | 143,240.00 USD | 2,710.00 USD | 0.00 USD | `+60.34%` | `8,785.00` |
| `Live` | `Short` | `0.3115` | 240,440.00 USD | 97,190.00 USD | 0.00 USD | `+61.90%` | `312,021.00` |
| `Live` | `Short` | `0.3135` | 240,730.00 USD | 297.82 USD | 0.00 USD | `+62.94%` | `950.00` |
| `Live` | `Short` | `0.3155` | 241,840.00 USD | 1,100.00 USD | 0.00 USD | `+63.98%` | `3,500.00` |
| `Live` | `Short` | `0.3175` | 245,480.00 USD | 3,640.00 USD | 0.00 USD | `+65.02%` | `11,458.00` |
| `Live` | `Short` | `0.3265` | 283,300.00 USD | 37,820.00 USD | 0.00 USD | `+69.70%` | `115,841.00` |
| `Live` | `Short` | `0.3295` | 285,680.00 USD | 2,380.00 USD | 0.00 USD | `+71.26%` | `7,219.00` |
| `Live` | `Short` | `0.3325` | 285,910.00 USD | 238.07 USD | 0.00 USD | `+72.82%` | `716.00` |
| `Live` | `Short` | `0.3435` | 286,230.00 USD | 314.30 USD | 0.00 USD | `+78.53%` | `915.00` |
| `Live` | `Short` | `0.3505` | 488,240.00 USD | 202,010.00 USD | 0.00 USD | `+82.17%` | `576,353.00` |
| `Live` | `Short` | `0.3515` | 489,360.00 USD | 1,120.00 USD | 0.00 USD | `+82.69%` | `3,187.00` |
| `Live` | `Short` | `0.3565` | 489,500.00 USD | 142.96 USD | 0.00 USD | `+85.29%` | `401.00` |
| `Live` | `Short` | `0.3605` | 494,600.00 USD | 5,100.00 USD | 0.00 USD | `+87.37%` | `14,148.00` |
| `Live` | `Short` | `0.3615` | 497,540.00 USD | 2,940.00 USD | 0.00 USD | `+87.89%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 497,690.00 USD | 143.91 USD | 0.00 USD | `+88.41%` | `397.00` |
| `Live` | `Short` | `0.3635` | 759,680.00 USD | 261,990.00 USD | 0.00 USD | `+88.93%` | `720,753.00` |
| `Live` | `Short` | `0.3655` | 759,850.00 USD | 163.38 USD | 0.00 USD | `+89.97%` | `447.00` |
| `Live` | `Short` | `0.3665` | 760,210.00 USD | 366.50 USD | 0.00 USD | `+90.49%` | `1,000.00` |
| `Live` | `Short` | `0.3715` | 769,380.00 USD | 9,170.00 USD | 0.00 USD | `+93.09%` | `24,689.00` |
| `Live` | `Short` | `0.3725` | 770,330.00 USD | 947.27 USD | 0.00 USD | `+93.61%` | `2,543.00` |
| `Live` | `Short` | `0.3735` | 798,340.00 USD | 28,010.00 USD | 0.00 USD | `+94.13%` | `75,000.00` |
| `Live` | `Short` | `0.3745` | 801,490.00 USD | 3,140.00 USD | 0.00 USD | `+94.65%` | `8,395.00` |
| `Live` | `Short` | `0.3795` | 825,580.00 USD | 24,090.00 USD | 0.00 USD | `+97.25%` | `63,484.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 110,720,000.00 USD | 0.00 USD | 415.13 USD | `-69.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 110,720,000.00 USD | 0.00 USD | 438.99 USD | `-68.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 110,720,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 110,720,000.00 USD | 0.00 USD | 541.33 USD | `-42.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 110,720,000.00 USD | 0.00 USD | 429.20 USD | `-39.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 110,720,000.00 USD | 0.00 USD | 602,500.00 USD | `-37.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 110,120,000.00 USD | 0.00 USD | 4,460.00 USD | `-35.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 110,110,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 110,110,000.00 USD | 0.00 USD | 13,390.00 USD | `-32.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 110,100,000.00 USD | 0.00 USD | 728.88 USD | `-31.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 110,100,000.00 USD | 0.00 USD | 4,350.00 USD | `-30.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 110,090,000.00 USD | 0.00 USD | 4,730.00 USD | `-28.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 110,090,000.00 USD | 0.00 USD | 1,820.00 USD | `-27.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 110,090,000.00 USD | 0.00 USD | 1,050.00 USD | `-26.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 110,080,000.00 USD | 0.00 USD | 351.26 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 110,080,000.00 USD | 0.00 USD | 1,600.00 USD | `-25.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 110,080,000.00 USD | 0.00 USD | 10,400.00 USD | `-24.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 110,070,000.00 USD | 0.00 USD | 5,980.00 USD | `-22.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 110,070,000.00 USD | 0.00 USD | 303.26 USD | `-21.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 110,070,000.00 USD | 0.00 USD | 3,230.00 USD | `-21.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 110,060,000.00 USD | 0.00 USD | 6,380.00 USD | `-20.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 110,060,000.00 USD | 0.00 USD | 126.54 USD | `-19.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 110,060,000.00 USD | 0.00 USD | 1,790.00 USD | `-19.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 110,050,000.00 USD | 0.00 USD | 6,260.00 USD | `-18.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 110,050,000.00 USD | 0.00 USD | 552.21 USD | `-17.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 110,050,000.00 USD | 0.00 USD | 166.84 USD | `-17.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 110,050,000.00 USD | 0.00 USD | 10,270.00 USD | `-16.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 110,040,000.00 USD | 0.00 USD | 769.39 USD | `-16.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 110,040,000.00 USD | 0.00 USD | 24,760.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 110,010,000.00 USD | 0.00 USD | 6,540.00 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 110,010,000.00 USD | 0.00 USD | 1,550.00 USD | `-14.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 110,000,000.00 USD | 0.00 USD | 452.97 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 110,000,000.00 USD | 0.00 USD | 12,640.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 109,990,000.00 USD | 0.00 USD | 317.92 USD | `-12.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 109,990,000.00 USD | 0.00 USD | 6,930.00 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 109,980,000.00 USD | 0.00 USD | 813.97 USD | `-11.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 109,980,000.00 USD | 0.00 USD | 1,220.00 USD | `-10.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 109,980,000.00 USD | 0.00 USD | 640.67 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 109,980,000.00 USD | 0.00 USD | 595.80 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 109,980,000.00 USD | 0.00 USD | 349.00 USD | `-9.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 109,980,000.00 USD | 0.00 USD | 1,760.00 USD | `-8.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 109,980,000.00 USD | 0.00 USD | 847.38 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 109,980,000.00 USD | 0.00 USD | 5,090.00 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 109,970,000.00 USD | 0.00 USD | 18,790.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 109,950,000.00 USD | 0.00 USD | 14,810.00 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 109,940,000.00 USD | 0.00 USD | 1,570.00 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 109,940,000.00 USD | 0.00 USD | 2,720.00 USD | `-5.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 109,930,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-5.15%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 73,430,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-4.63%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 33,150.00 USD | 0.00 USD | 1,880.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 31,270.00 USD | 0.00 USD | 286.41 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 30,980.00 USD | 0.00 USD | 1,420.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 29,560.00 USD | 0.00 USD | 3,580.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 25,980.00 USD | 0.00 USD | 3,100.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 22,880.00 USD | 0.00 USD | 19,340.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 3,540.00 USD | 0.00 USD | 1,450.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 2,090.00 USD | 0.00 USD | 2,090.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 224.07 USD | 224.07 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 2,960.00 USD | 2,740.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 3,280.00 USD | 322.09 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 3,830.00 USD | 549.75 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 7,490.00 USD | 3,660.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 8,490.00 USD | 1,000.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 9,140.00 USD | 646.71 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 10,050.00 USD | 912.11 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 26,910.00 USD | 16,860.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 73,250.00 USD | 46,340.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 75,090.00 USD | 1,840.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 86,360.00 USD | 11,280.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 89,050.00 USD | 2,690.00 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 91,210.00 USD | 2,160.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 106,690.00 USD | 15,490.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 107,010.00 USD | 312.70 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 115,350.00 USD | 8,340.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 123,340.00 USD | 7,990.00 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 145,410.00 USD | 22,070.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 165,240.00 USD | 19,820.00 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 171,940.00 USD | 6,700.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 176,130.00 USD | 4,190.00 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 177,100.00 USD | 965.25 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 187,400.00 USD | 10,300.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 188,010.00 USD | 609.66 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 188,120.00 USD | 109.91 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 203,580.00 USD | 15,460.00 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 206,350.00 USD | 2,760.00 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 207,990.00 USD | 1,650.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 217,170.00 USD | 9,180.00 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 220,920.00 USD | 3,750.00 USD | 0.00 USD | `+16.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 221,040.00 USD | 114.50 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 221,380.00 USD | 339.60 USD | 0.00 USD | `+17.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 221,490.00 USD | 109.40 USD | 0.00 USD | `+17.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 221,640.00 USD | 151.06 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 230,780.00 USD | 9,140.00 USD | 0.00 USD | `+18.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 231,440.00 USD | 662.92 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 231,780.00 USD | 337.06 USD | 0.00 USD | `+20.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 231,950.00 USD | 171.12 USD | 0.00 USD | `+20.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 232,050.00 USD | 101.11 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 233,160.00 USD | 1,110.00 USD | 0.00 USD | `+21.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 242,580.00 USD | 9,420.00 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 243,030.00 USD | 443.91 USD | 0.00 USD | `+22.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 243,800.00 USD | 778.76 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 244,000.00 USD | 192.71 USD | 0.00 USD | `+23.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 244,510.00 USD | 514.45 USD | 0.00 USD | `+24.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 244,720.00 USD | 209.72 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 244,840.00 USD | 115.92 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 245,070.00 USD | 236.19 USD | 0.00 USD | `+26.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 246,220.00 USD | 1,150.00 USD | 0.00 USD | `+27.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 246,510.00 USD | 288.22 USD | 0.00 USD | `+27.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 247,000.00 USD | 491.03 USD | 0.00 USD | `+28.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 248,320.00 USD | 1,320.00 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 258,260.00 USD | 9,940.00 USD | 0.00 USD | `+29.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 258,760.00 USD | 499.00 USD | 0.00 USD | `+29.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 259,860.00 USD | 1,100.00 USD | 0.00 USD | `+30.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 260,030.00 USD | 168.76 USD | 0.00 USD | `+30.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 260,630.00 USD | 603.73 USD | 0.00 USD | `+31.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 262,810.00 USD | 2,170.00 USD | 0.00 USD | `+31.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 264,500.00 USD | 1,700.00 USD | 0.00 USD | `+33.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 264,770.00 USD | 271.44 USD | 0.00 USD | `+34.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 685,530.00 USD | 420,750.00 USD | 0.00 USD | `+35.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 686,710.00 USD | 1,180.00 USD | 0.00 USD | `+37.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 695,600.00 USD | 8,890.00 USD | 0.00 USD | `+39.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 710,470.00 USD | 14,860.00 USD | 0.00 USD | `+39.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 711,810.00 USD | 1,340.00 USD | 0.00 USD | `+40.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 714,520.00 USD | 2,710.00 USD | 0.00 USD | `+41.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 728,380.00 USD | 13,870.00 USD | 0.00 USD | `+42.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 733,600.00 USD | 5,220.00 USD | 0.00 USD | `+42.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 734,770.00 USD | 1,170.00 USD | 0.00 USD | `+44.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 738,930.00 USD | 4,150.00 USD | 0.00 USD | `+44.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 739,870.00 USD | 944.99 USD | 0.00 USD | `+45.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 740,070.00 USD | 198.73 USD | 0.00 USD | `+47.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 741,440.00 USD | 1,370.00 USD | 0.00 USD | `+47.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 742,520.00 USD | 1,080.00 USD | 0.00 USD | `+49.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 757,500.00 USD | 14,980.00 USD | 0.00 USD | `+50.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 758,740.00 USD | 1,230.00 USD | 0.00 USD | `+51.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 760,180.00 USD | 1,440.00 USD | 0.00 USD | `+54.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 760,540.00 USD | 355.21 USD | 0.00 USD | `+55.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 767,190.00 USD | 6,650.00 USD | 0.00 USD | `+56.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 786,170.00 USD | 18,980.00 USD | 0.00 USD | `+58.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 790,320.00 USD | 4,150.00 USD | 0.00 USD | `+60.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 793,560.00 USD | 3,250.00 USD | 0.00 USD | `+63.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 794,060.00 USD | 493.89 USD | 0.00 USD | `+68.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 794,240.00 USD | 181.30 USD | 0.00 USD | `+69.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 795,620.00 USD | 1,380.00 USD | 0.00 USD | `+71.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 807,910.00 USD | 12,290.00 USD | 0.00 USD | `+72.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 808,020.00 USD | 111.06 USD | 0.00 USD | `+73.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 808,240.00 USD | 220.61 USD | 0.00 USD | `+77.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 811,580.00 USD | 3,340.00 USD | 0.00 USD | `+81.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 811,770.00 USD | 188.75 USD | 0.00 USD | `+96.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 812,680.00 USD | 909.54 USD | 0.00 USD | `+96.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 812,800.00 USD | 121.76 USD | 0.00 USD | `+97.77%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1640` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 166,770.00 USD | 55,610.00 USD | 217,430.00 USD |
| `7D` | `0.1650` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 57,340.00 USD | 18,500.00 USD | 42,730.00 USD |
| `7D` | `0.1660` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 88,950.00 USD | 31,770.00 USD | 105,170.00 USD |
| `7D` | `0.1670` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD |
| `7D` | `0.1680` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD |
| `7D` | `0.1690` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD |
| `7D` | `0.1700` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD |
| `7D` | `0.1710` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD |
| `7D` | `0.1720` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 9,500.00 USD | 2,920.00 USD | 41,020.00 USD |
| `1D` | `0.1730` | 8,290,000.00 USD | 0.00 USD | 8,290,000.00 USD | 93,280.00 USD | 25,590.00 USD | 128,710.00 USD |
| `7D` | `0.1730` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 0.00 USD | 332.90 USD | 82,340.00 USD |
| `1D` | `0.1740` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 23,910.00 USD | 15,040.00 USD | 9,440.00 USD |
| `7D` | `0.1740` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 0.00 USD | 3,560.00 USD | 32,360.00 USD |
| `1D` | `0.1750` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 50,710.00 USD | 15,820.00 USD | 14,890.00 USD |
| `7D` | `0.1750` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 7,610.00 USD | 6,730.00 USD | 25,660.00 USD |
| `1D` | `0.1760` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD |
| `7D` | `0.1760` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD |
| `1D` | `0.1770` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD |
| `7D` | `0.1770` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD |
| `1D` | `0.1780` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 70,220.00 USD | 12,970.00 USD | 42,010.00 USD |
| `7D` | `0.1780` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 140,230.00 USD | 12,660.00 USD | 56,120.00 USD |
| `1D` | `0.1790` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 130,180.00 USD | 52,650.00 USD | 95,320.00 USD |
| `7D` | `0.1790` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 9,850.00 USD | 27,990.00 USD | 116,120.00 USD |
| `1D` | `0.1800` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 756,150.00 USD | 103,250.00 USD | 195,040.00 USD |
| `7D` | `0.1800` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 464,090.00 USD | 95,830.00 USD | 141,980.00 USD |
| `1D` | `0.1810` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 160,190.00 USD | 59,050.00 USD | 169,600.00 USD |
| `7D` | `0.1810` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 354,390.00 USD | 45,990.00 USD | 179,050.00 USD |
| `1D` | `0.1820` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 432,620.00 USD | 95,990.00 USD | 318,680.00 USD |
| `7D` | `0.1820` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 123,330.00 USD | 62,450.00 USD | 444,200.00 USD |
| `1D` | `0.1830` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 436,420.00 USD | 44,980.00 USD | 65,230.00 USD |
| `7D` | `0.1830` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 435,140.00 USD | 47,220.00 USD | 32,460.00 USD |
| `1D` | `0.1840` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 380,190.00 USD | 85,110.00 USD | 185,890.00 USD |
| `7D` | `0.1840` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 273,040.00 USD | 41,950.00 USD | 192,770.00 USD |
| `1D` | `0.1850` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 56,030.00 USD | 39,720.00 USD | 116,200.00 USD |
| `7D` | `0.1850` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 50,160.00 USD | 6,440.00 USD | 228,270.00 USD |
| `1D` | `0.1860` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 171,630.00 USD | 44,670.00 USD | 430,730.00 USD |
| `7D` | `0.1860` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 70,810.00 USD | 15,200.00 USD | 5,140.00 USD |
| `1D` | `0.1870` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD |
| `7D` | `0.1870` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD |
| `1D` | `0.1880` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 235,680.00 USD | 180,000.00 USD | 196,900.00 USD |
| `7D` | `0.1880` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 132,450.00 USD | 103,170.00 USD | 670,720.00 USD |
| `1D` | `0.1890` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 217,970.00 USD | 38,240.00 USD | 93,570.00 USD |
| `7D` | `0.1890` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 510,390.00 USD | 12,880.00 USD | 32,810.00 USD |
| `1D` | `0.1900` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 93,550.00 USD | 128,280.00 USD | 299,230.00 USD |
| `7D` | `0.1900` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 255,740.00 USD | 30,390.00 USD | 216,460.00 USD |
| `1D` | `0.1910` | 733,850.00 USD | 0.00 USD | 733,850.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD |
| `7D` | `0.1910` | 553,650.00 USD | 0.00 USD | 553,650.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD |
| `1D` | `0.1920` | 11,060.00 USD | 0.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD |
| `7D` | `0.1920` | 600,250.00 USD | 600,250.00 USD | 0.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD |
| `7D` | `0.1920` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD |
| `1D` | `0.1930` | 457,320.00 USD | 457,320.00 USD | 0.00 USD | 284,520.00 USD | 2,420.00 USD | 170,380.00 USD |
| `1D` | `0.1930` | 914,650.00 USD | 914,650.00 USD | 0.00 USD | 284,520.00 USD | 2,420.00 USD | 170,380.00 USD |
| `7D` | `0.1930` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 653,060.00 USD | 0.00 USD | 331,360.00 USD |
| `1D` | `0.1940` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD |
| `7D` | `0.1940` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `1D` | `0.1950` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 25,540.00 USD | 73,330.00 USD | 413,790.00 USD |
| `7D` | `0.1950` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 693,070.00 USD | 1,990.00 USD | 203,120.00 USD |
| `1D` | `0.1960` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 467,210.00 USD | 250,690.00 USD | 524,290.00 USD |
| `7D` | `0.1960` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 236,660.00 USD | 112,940.00 USD | 1,240,000.00 USD |
| `1D` | `0.1970` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 96,390.00 USD | 115,800.00 USD | 290,740.00 USD |
| `7D` | `0.1970` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 13,930.00 USD | 32,990.00 USD | 275,930.00 USD |
| `1D` | `0.1980` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 409,930.00 USD | 110,510.00 USD | 378,020.00 USD |
| `7D` | `0.1980` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 312,350.00 USD | 44,250.00 USD | 315,080.00 USD |
| `1D` | `0.1990` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD |
| `7D` | `0.1990` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD |
| `1D` | `0.2000` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 361,650.00 USD | 73,900.00 USD | 400,290.00 USD |
| `7D` | `0.2000` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 56,530.00 USD | 38,390.00 USD | 371,130.00 USD |
| `1D` | `0.2010` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 159,370.00 USD | 162,580.00 USD | 326,080.00 USD |
| `7D` | `0.2010` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 335,650.00 USD | 25,310.00 USD | 359,800.00 USD |
| `1D` | `0.2020` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 223,790.00 USD | 75,610.00 USD | 179,140.00 USD |
| `7D` | `0.2020` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 87,710.00 USD | 52,030.00 USD | 495,090.00 USD |
| `1D` | `0.2030` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 124,930.00 USD | 93,750.00 USD | 154,570.00 USD |
| `7D` | `0.2030` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 15,840.00 USD | 94,230.00 USD | 153,910.00 USD |
| `1D` | `0.2040` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 82,600.00 USD | 120,640.00 USD | 133,090.00 USD |
| `7D` | `0.2040` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 59,380.00 USD | 76,320.00 USD | 6,560.00 USD |
| `1D` | `0.2050` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 86,770.00 USD | 31,580.00 USD | 52,620.00 USD |
| `7D` | `0.2050` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 37,210.00 USD | 1,160.00 USD | 57,550.00 USD |
| `1D` | `0.2060` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 311,840.00 USD | 31,930.00 USD | 92,350.00 USD |
| `7D` | `0.2060` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 149,740.00 USD | 18,480.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 255,320.00 USD | 118,570.00 USD | 203,060.00 USD |
| `7D` | `0.2070` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 439,210.00 USD | 141,790.00 USD | 35,600.00 USD |
| `1D` | `0.2080` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 330,520.00 USD | 94,230.00 USD | 42,600.00 USD |
| `7D` | `0.2080` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD |
| `1D` | `0.2090` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 491,160.00 USD | 154,050.00 USD | 300,210.00 USD |
| `7D` | `0.2090` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD |
| `1D` | `0.2100` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 463,870.00 USD | 102,650.00 USD | 210,050.00 USD |
| `7D` | `0.2100` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD |
| `1D` | `0.2110` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 136,020.00 USD | 40,770.00 USD | 124,740.00 USD |
| `7D` | `0.2110` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 1,060,000.00 USD | 511,730.00 USD | 1,620,000.00 USD |
| `1D` | `0.2120` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 136,500.00 USD | 84,890.00 USD | 135,170.00 USD |
| `7D` | `0.2120` | 23,340,000.00 USD | 23,340,000.00 USD | 0.00 USD | 1,160,000.00 USD | 466,390.00 USD | 1,380,000.00 USD |
| `1D` | `0.2130` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 212,500.00 USD | 59,020.00 USD | 88,410.00 USD |
| `7D` | `0.2130` | 26,160,000.00 USD | 26,160,000.00 USD | 0.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,250,000.00 USD |
| `1D` | `0.2140` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 130,000.00 USD | 31,520.00 USD | 26,470.00 USD |
| `7D` | `0.2140` | 28,260,000.00 USD | 28,260,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD |
| `7D` | `0.2150` | 30,520,000.00 USD | 30,520,000.00 USD | 0.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD |
| `7D` | `0.2160` | 31,550,000.00 USD | 31,550,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `410.54M` | Total OI Tokens: `2,121,507,347.2 ADA`
  * 1h OI Change: `+0.40%` | 4h OI Change: `-0.67%` | 24h OI Change: `-7.53%`
  * Exchange Breakdown: Binance=`74.69M` | Bybit=`50.10M` | OKX=`29.03M` | Hyperliquid=`28.53M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.59K` | Last 24h: `30.56K` | Last 3d: `64.45K` | Last 7d: `83.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0041%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0071%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `54.69%` | `45.31%` | `1.21` | 3,680,000.00 USD |
| `15M` | `Binance` | `66.27%` | `33.73%` | `1.96` | 1,300,000.00 USD |
| `15M` | `OKX` | `47.09%` | `52.91%` | `0.89` | 245,730.00 USD |
| `15M` | `Bybit` | `67.48%` | `32.52%` | `2.08` | 300,050.00 USD |
| `15M` | `KuCoin` | `55.28%` | `44.72%` | `1.24` | 70,050.00 USD |
| `15M` | `Gate` | `53.77%` | `46.23%` | `1.16` | 99,300.00 USD |
| `15M` | `Bitget` | `51.54%` | `48.46%` | `1.06` | 118,930.00 USD |
| `15M` | `BingX` | `45.94%` | `54.06%` | `0.85` | 87,780.00 USD |
| `15M` | `MEXC` | `52.93%` | `47.07%` | `1.12` | 345,750.00 USD |
| `15M` | `Bitunix` | `43.96%` | `56.04%` | `0.78` | 55,750.00 USD |
| `15M` | `Hyperliquid` | `16.47%` | `83.53%` | `0.20` | 39,480.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.52%` | `45.48%` | `1.20` | 651,610.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 270,420.00 USD |
| `15M` | `HTX` | `29.02%` | `70.98%` | `0.41` | 11,610.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `80.14%` | `19.86%` | `4.04` | 78,550.00 USD |
| `15M` | `Aster` | `74.47%` | `25.53%` | `2.92` | 43.60 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `61.24%` | `38.76%` | `1.58` | 6,550.00 USD |
| `15M` | `Whale Positions` | `66.27%` | `33.73%` | `1.96` | 1,300,000.00 USD |
| `15M` | `Global Accounts` | `54.69%` | `45.31%` | `1.21` | 3,680,000.00 USD |
| `1H` | `ADA` | `42.01%` | `57.99%` | `0.72` | 45,350,000.00 USD |
| `1H` | `Binance` | `41.76%` | `58.24%` | `0.72` | 16,880,000.00 USD |
| `1H` | `OKX` | `41.25%` | `58.75%` | `0.70` | 8,390,000.00 USD |
| `1H` | `Bybit` | `36.26%` | `63.74%` | `0.57` | 4,100,000.00 USD |
| `1H` | `KuCoin` | `44.08%` | `55.92%` | `0.79` | 395,280.00 USD |
| `1H` | `Gate` | `46.89%` | `53.11%` | `0.88` | 8,210,000.00 USD |
| `1H` | `Bitget` | `44.15%` | `55.85%` | `0.79` | 782,120.00 USD |
| `1H` | `BingX` | `30.13%` | `69.87%` | `0.43` | 682,720.00 USD |
| `1H` | `MEXC` | `46.48%` | `53.52%` | `0.87` | 1,950,000.00 USD |
| `1H` | `Bitunix` | `38.35%` | `61.65%` | `0.62` | 1,030,000.00 USD |
| `1H` | `Hyperliquid` | `69.24%` | `30.76%` | `2.25` | 601,770.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.75%` | `43.25%` | `1.31` | 331,900.00 USD |
| `1H` | `Crypto.com` | `24.67%` | `75.33%` | `0.33` | 60,620.00 USD |
| `1H` | `WhiteBIT` | `22.22%` | `77.78%` | `0.29` | 1,310,000.00 USD |
| `1H` | `HTX` | `51.78%` | `48.22%` | `1.07` | 162,340.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.64%` | `58.36%` | `0.71` | 205,150.00 USD |
| `1H` | `Aster` | `37.65%` | `62.35%` | `0.60` | 247,220.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `89.85%` | `10.15%` | `8.85` | 4,530.00 USD |
| `1H` | `Whale Positions` | `41.76%` | `58.24%` | `0.72` | 16,880,000.00 USD |
| `1H` | `Global Accounts` | `42.01%` | `57.99%` | `0.72` | 45,350,000.00 USD |
| `4H` | `ADA` | `45.43%` | `54.57%` | `0.83` | 74,290,000.00 USD |
| `4H` | `Binance` | `51.32%` | `48.68%` | `1.05` | 24,240,000.00 USD |
| `4H` | `OKX` | `49.29%` | `50.71%` | `0.97` | 6,010,000.00 USD |
| `4H` | `Bybit` | `47.37%` | `52.63%` | `0.90` | 6,520,000.00 USD |
| `4H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 1,070,000.00 USD |
| `4H` | `Gate` | `49.25%` | `50.75%` | `0.97` | 1,750,000.00 USD |
| `4H` | `Bitget` | `41.47%` | `58.53%` | `0.71` | 2,490,000.00 USD |
| `4H` | `BingX` | `28.82%` | `71.18%` | `0.40` | 10,580,000.00 USD |
| `4H` | `MEXC` | `47.41%` | `52.59%` | `0.90` | 5,590,000.00 USD |
| `4H` | `Bitunix` | `46.73%` | `53.27%` | `0.88` | 1,830,000.00 USD |
| `4H` | `Hyperliquid` | `35.17%` | `64.83%` | `0.54` | 647,960.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.03%` | `48.97%` | `1.04` | 11,150,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `2.88%` | `97.12%` | `0.03` | 1,840,000.00 USD |
| `4H` | `HTX` | `57.53%` | `42.47%` | `1.35` | 339,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.14%` | `47.86%` | `1.09` | 173,100.00 USD |
| `4H` | `Aster` | `24.85%` | `75.15%` | `0.33` | 33,130.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `54.9%` | `45.1%` | `1.22` | 29,180.00 USD |
| `4H` | `Whale Positions` | `51.32%` | `48.68%` | `1.05` | 24,240,000.00 USD |
| `4H` | `Global Accounts` | `45.43%` | `54.57%` | `0.83` | 74,290,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1945` | `0.1947` | `0.1945` | `0.1955` | `0.1943` | 1,082,696.69 USD | 522,652.08 USD | 560,044.61 USD | -37,392.53 USD | `-3.45%` | `1B / 1S` |
| `5:00 UTC` | `0.1938` | `0.1941` | `0.1938` | `0.1946` | `0.1936` | 788,689.45 USD | 257,084.28 USD | 531,605.17 USD | -274,520.88 USD | `-34.81%` | `0B / 1S` |
| `0:00 UTC` | `0.1940` | `0.1940` | `0.1940` | `0.1945` | `0.1935` | 1,131,280.96 USD | 497,533.88 USD | 633,747.08 USD | -136,213.20 USD | `-12.04%` | `0B / 3S` |
| `5:00 UTC` | `0.1936` | `0.1936` | `0.1936` | `0.1940` | `0.1933` | 697,890.94 USD | 262,282.71 USD | 435,608.23 USD | -173,325.53 USD | `-24.84%` | `0B / 1S` |
| `0:00 UTC` | `0.1921` | `0.1928` | `0.1921` | `0.1941` | `0.1920` | 1,954,616.49 USD | 896,711.52 USD | 1,057,904.97 USD | -161,193.45 USD | `-8.25%` | `0B / 4S` |
| `5:00 UTC` | `0.1925` | `0.1924` | `0.1925` | `0.1930` | `0.1920` | 1,539,119.78 USD | 772,101.15 USD | 767,018.63 USD | 5,082.52 USD | `+0.33%` | `2B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1924` | `0.1925` | `0.1930` | `0.1918` | 1,135,407.39 USD | 588,660.08 USD | 546,747.31 USD | 41,912.77 USD | `+3.69%` | `2B / 1S` |
| `5:00 UTC` | `0.1928` | `0.1927` | `0.1928` | `0.1930` | `0.1923` | 1,200,311.82 USD | 545,374.62 USD | 654,937.20 USD | -109,562.58 USD | `-9.13%` | `0B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1925` | `0.1918` | 999,923.94 USD | 501,446.14 USD | 498,477.80 USD | 2,968.35 USD | `+0.30%` | `1B / 2S` |
| `5:00 UTC` | `0.1918` | `0.1918` | `0.1918` | `0.1920` | `0.1916` | 327,714.90 USD | 244,679.98 USD | 83,034.93 USD | 161,645.05 USD | `+49.32%` | `2B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:57` | `Range 0.001` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.2010` | 3,900,000.00 USD | 0.00 USD |
| `10-28 17:44` | `Volume 20M ADA` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.2042` | 0.00 USD | 0.00 USD |
| `10-28 17:43` | `Range 0.001` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.2042` | 0.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.001` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.2058` | 1,300,000.00 USD | 0.00 USD |
| `10-28 16:11` | `Range 0.001` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.2077` | 1,600,000.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.001` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.2066` | 0.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.001` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.2055` | 0.00 USD | 0.00 USD |
| `10-28 09:01` | `Range 0.001` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.2075` | 0.00 USD | 0.00 USD |
| `10-28 09:01` | `Range 0.001` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.2085` | 0.00 USD | 0.00 USD |
| `10-28 08:39` | `Volume 20M ADA` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.2085` | 4,700,000.00 USD | 0.00 USD |
| `10-28 07:53` | `Range 0.001` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.2063` | 3,600,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -15,620.00 USD | 351,930.00 USD | **`ACCUMULATION`** |
| `15m` | -64,090.00 USD | 514,390.00 USD | **`ACCUMULATION`** |
| `30m` | -219,660.00 USD | 404,410.00 USD | **`ACCUMULATION`** |
| `1h` | -56,320.00 USD | 644,840.00 USD | **`ACCUMULATION`** |
| `2h` | -406,660.00 USD | -175,450.00 USD | **`DISTRIBUTION`** |
| `4h` | -129,090.00 USD | -131,280.00 USD | **`DISTRIBUTION`** |
| `6h` | -213,890.00 USD | 1,110,000.00 USD | **`ACCUMULATION`** |
| `8h` | -343,230.00 USD | -1,560,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,660,000.00 USD | -509,310.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,380,000.00 USD | -8,060,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -22,010,000.00 USD | -40,320,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,120,000.00 USD | -196,590,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-15.62K` | 15m=`-64.09K` | 1h=`-56.32K` | 24h=`-8.38M`
* Futures Capital Netflows: 5m=`+351.93K` | 15m=`+514.39K` | 1h=`+644.84K` | 24h=`-8.06M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1870` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1824` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1984`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1938` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1984` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1824`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1933`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
