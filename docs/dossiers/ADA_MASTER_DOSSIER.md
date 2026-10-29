# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:54:56 IST` (`2026-10-29 21:24:56 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1916` | **Live Ask Quote**: `0.1937` | **Mid Price**: `0.1926`
- **Spread Points**: `21.00` | **Spread BPS**: `109.01 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1987` | VWAP Z-Score: `-2.31` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0023` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `16.25` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2110` | Lower -3.00σ Band: `0.1864`
  * Upper +2.51σ Band: `0.2090` | Lower -2.51σ Band: `0.1884`
  * Upper +2.01σ Band: `0.2069` | Lower -2.01σ Band: `0.1904`
  * Upper +2.00σ Band: `0.2069` | Lower -2.00σ Band: `0.1905`
  * Upper +1.28σ Band: `0.2039` | Lower -1.28σ Band: `0.1934`
  * Upper +1.00σ Band: `0.2028` | Lower -1.00σ Band: `0.1946`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1963` | EMA-20=`0.1990` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2001` (Slope: `+0.0000`) | EMA-100=`0.2006`
  * Institutional Anchors: EMA-144=`0.2010` | EMA-200=`0.2015` (Slope: `-0.1816`) | EMA-233=`0.2018`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1862` | Weekly High=`0.2086` | Weekly Low=`0.1862`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1919` (Distance: `+0.32%`)
  * Point of Control (POC) = `0.1913` (Distance: `+0.63%`)
  * Value Area Low (VAL) = `0.1898` (Distance: `+1.44%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2054` | Weekly POC=`0.2031` | Weekly VAL=`0.2005`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1919` | Low=`0.1888`
  * London Session (08:00-16:00 UTC): High=`0.1934` | Low=`0.1919`
  * New York Session (13:00-21:00 UTC): High=`0.1938` | Low=`0.1915`
  * Initial Balance (First Hour): IB High=`0.1932` | IB Low=`0.1921`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1919` - `0.1934`
  * Optimal Trade Entry (OTE 0.705): `0.1930`
  * Structural Invalidation Anchor (0.786): `0.1942`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1902` | `0.1925` | `0.1899` | `0.1925` | `15,110,241` | 2,891,885.04 USD | 162,735.95 USD | `+5.63%` | -8,863,769.10 USD | `+0.52` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1924` | `0.1931` | `0.1918` | `0.1927` | `13,334,934` | 2,568,210.13 USD | -415,116.36 USD | `-16.16%` | -9,278,885.46 USD | `-0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1928` | `0.1930` | `0.1927` | `0.1929` | `250,891` | 48,394.32 USD | 41,525.78 USD | `+85.81%` | -9,237,359.68 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1910` | `0.1935` | `0.1871` | `0.1904` | `138,243,043` | 26,316,880.25 USD | -2,662,790.75 USD | `-10.12%` | -8,676,047.60 USD | `-2.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1903` | `0.1931` | `0.1897` | `0.1927` | `54,041,111` | 10,338,146.03 USD | -355,304.19 USD | `-3.44%` | -9,031,351.79 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1928` | `0.1930` | `0.1926` | `0.1927` | `1,435,097` | 276,676.91 USD | -151,382.25 USD | `-54.71%` | -9,182,734.04 USD | `+0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.2023` | `0.2028` | `0.2015` | `0.2022` | `15,668,827` | 3,167,925.53 USD | 135,664.16 USD | `+4.28%` | -2,066,110.98 USD | `+0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.2022` | `0.2023` | `0.1871` | `0.1904` | `319,583,639` | 61,830,947.38 USD | -6,627,620.80 USD | `-10.72%` | -8,693,731.77 USD | `-3.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1903` | `0.1931` | `0.1897` | `0.1930` | `54,277,808` | 10,383,801.15 USD | -315,562.74 USD | `-3.04%` | -9,009,294.51 USD | `-0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1929` | `373,875,641` | 72,217,487.72 USD | -6,941,399.20 USD | `-9.61%` | -9,367,344.11 USD | `-1.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -5,414,333.03 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -4,633,383.98 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1929` | `373,875,641` | 72,217,487.72 USD | -6,941,399.20 USD | `-9.61%` | -9,367,344.11 USD | `-1.54` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1926`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `534` | `0x77ee...2902` | `SHORT` | 4,129,983.59 USD | `21,412,192.00` | `0.1911` | `0.1941` | `0.5633` | -38,731.85 USD | `-0.94%` | `10X Cross` |
| `1254` | `0x123d...3bff` | `LONG` | 1,815,130.76 USD | `9,393,142.00` | `0.2912` | `0.1941` | `0.000000` | -920,605.18 USD | `-50.72%` | `10X Cross` |
| `1303` | `0x7737...bf66` | `SHORT` | 1,736,197.26 USD | `9,091,466.00` | `0.2190` | `0.1941` | `2.04` | 254,792.54 USD | `+14.68%` | `10X Cross` |
| `1583` | `0x5f94...4b96` | `SHORT` | 1,383,759.84 USD | `7,162,318.00` | `0.2303` | `0.1941` | `0.7260` | 265,715.36 USD | `+19.20%` | `10X Cross` |
| `1818` | `0x4982...59e6` | `SHORT` | 1,140,614.11 USD | `5,998,812.00` | `0.1891` | `0.1941` | `0.4066` | -6,055.75 USD | `-0.53%` | `10X Cross` |
| `1846` | `0xcac1...26b3` | `LONG` | 1,117,041.20 USD | `5,803,927.00` | `0.2000` | `0.1941` | `0.000000` | -43,774.38 USD | `-3.92%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2060` | 6,152.92 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2060 USD [API] | `2026-10-28 07:11:32` |
| `ANNOUNCEMENT` | `INFO` | `0.2060` | 8,326.94 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 8.33K USD at 0.2060 USD [API] | `2026-10-28 07:11:32` |
| `ANNOUNCEMENT` | `INFO` | `0.2060` | 5,005.56 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2060 USD [API] | `2026-10-28 07:11:31` |
| `ANNOUNCEMENT` | `INFO` | `0.2058` | 5,006.61 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2058 USD [API] | `2026-10-28 07:13:21` |
| `ANNOUNCEMENT` | `INFO` | `0.2058` | 6,153.49 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2058 USD [API] | `2026-10-28 07:13:21` |
| `ANNOUNCEMENT` | `INFO` | `0.2066` | 5,410.81 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.41K USD at 0.2066 USD [API] | `2026-10-28 07:58:46` |
| `ANNOUNCEMENT` | `INFO` | `0.2066` | 6,662.55 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.66K USD at 0.2066 USD [API] | `2026-10-28 07:58:46` |
| `ANNOUNCEMENT` | `INFO` | `0.2066` | 30,328.88 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 30.33K USD at 0.2066 USD [API] | `2026-10-28 07:58:46` |
| `ANNOUNCEMENT` | `INFO` | `0.2076` | 6,646.62 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2076 USD [API] | `2026-10-28 08:40:22` |
| `ANNOUNCEMENT` | `INFO` | `0.2072` | 6,644.53 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.64K USD at 0.2072 USD [API] | `2026-10-28 09:20:04` |
| `ANNOUNCEMENT` | `INFO` | `0.2071` | 5,403.71 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.40K USD at 0.2071 USD [API] | `2026-10-28 09:20:43` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2100` (Vol: 230,300.00 USD, Dist: `+5.33%`) | Long MP=`0.1965` (Vol: 250,900.00 USD, Dist: `--1.43%`)
  * 48H Horizon: Short MP=`0.2093` (Vol: 207,000.00 USD, Dist: `+4.96%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--3.36%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 261,100.00 USD, Dist: `+7.17%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--3.36%`)
  * 7D Horizon: Short MP=`0.2124` (Vol: 359,800.00 USD, Dist: `+6.50%`) | Long MP=`0.1926` (Vol: 321,900.00 USD, Dist: `--3.42%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 232.20 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 348.75 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 481.50 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 1,350.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 3,170.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 9,540.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 1,350.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 7,300.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 166,980.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 326.43 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 1,610.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 945.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 331.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 793.42 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 526.77 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 467.30 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 5,380.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,480.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 931.42 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 150.21 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 2,970.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 407.09 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 290.36 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 8,950.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 63,140.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 2,180.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 565.51 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,740.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 1,010.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 16,640.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 1,890.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 882.93 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 163.65 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 138.14 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 144.33 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 37,390.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 981.95 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 43,060.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 4,510.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 504.44 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 10,860.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 5,760.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 929.88 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 634,470.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 5,740.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,180.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,540.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 2,230.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,120.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 1,690.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 1,750.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 1,280.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1700` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 619,120.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,140,000.00 USD | 4,140,000.00 USD | 23,820.00 USD | 700.07 USD | 12,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 516,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 321.20 USD | 18,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 34,840.00 USD | 263,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 4,280.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,430.00 USD | 229,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 226,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 61,110.00 USD | 225,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 4,060,000.00 USD | 4,060,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 5,110.00 USD | 164,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,970,000.00 USD | 3,970,000.00 USD | 53,230.00 USD | 18,310.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 17,370.00 USD | 159,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,820,000.00 USD | 3,820,000.00 USD | 62,120.00 USD | 34,290.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 725.42 USD | 141,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,660,000.00 USD | 3,660,000.00 USD | 73,150.00 USD | 37,690.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 11,150.00 USD | 140,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 3,500,000.00 USD | 3,500,000.00 USD | 75,870.00 USD | 25,350.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 82,920.00 USD | 129,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 3,350,000.00 USD | 3,350,000.00 USD | 38,430.00 USD | 23,350.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 46,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 3,250,000.00 USD | 3,250,000.00 USD | 136,500.00 USD | 9,890.00 USD | 68,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,560.00 USD | 39,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 3,030,000.00 USD | 3,030,000.00 USD | 32,650.00 USD | 21,120.00 USD | 65,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1840` | 2,910,000.00 USD | 2,910,000.00 USD | 77,630.00 USD | 29,420.00 USD | 52,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 9,000.00 USD | 20,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 2,750,000.00 USD | 2,750,000.00 USD | 128,210.00 USD | 59,950.00 USD | 142,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 6,570.00 USD | 11,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 2,420,000.00 USD | 2,420,000.00 USD | 159,010.00 USD | 7,290.00 USD | 72,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 3,850.00 USD | 5,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 2,180,000.00 USD | 2,180,000.00 USD | 102,920.00 USD | 49,970.00 USD | 119,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 451.69 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 1,910,000.00 USD | 1,910,000.00 USD | 223,120.00 USD | 49,550.00 USD | 60,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 1,580,000.00 USD | 1,580,000.00 USD | 162,010.00 USD | 110,140.00 USD | 36,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 802.34 USD | 802.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 114,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1905` | 635.51 USD | 635.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 1,150,000.00 USD | 1,150,000.00 USD | 292,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 861,870.00 USD | 861,870.00 USD | 470,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1930` | 391,530.00 USD | 391,530.00 USD | 361,640.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 214,200.00 USD | 214,200.00 USD | 139,920.00 USD | 0.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 428,400.00 USD | 428,400.00 USD | 139,920.00 USD | 0.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 570,840.00 USD | 570,840.00 USD | 21,890.00 USD | 20,360.00 USD | 100,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 823,190.00 USD | 823,190.00 USD | 6,090.00 USD | 178,720.00 USD | 67,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1970` | 907,090.00 USD | 907,090.00 USD | 0.00 USD | 30,910.00 USD | 52,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 1,000,000.00 USD | 1,000,000.00 USD | 62,420.00 USD | 1,260.00 USD | 32,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1990` | 1,170,000.00 USD | 1,170,000.00 USD | 50,670.00 USD | 37,620.00 USD | 74,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2000` | 1,570,000.00 USD | 1,570,000.00 USD | 188,460.00 USD | 13,490.00 USD | 204,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 169.62 USD | 805.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 2,040,000.00 USD | 2,040,000.00 USD | 101,890.00 USD | 121,910.00 USD | 243,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 461.03 USD | 1,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 2,190,000.00 USD | 2,190,000.00 USD | 32,560.00 USD | 27,550.00 USD | 89,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 5,560.00 USD | 6,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 2,650,000.00 USD | 2,650,000.00 USD | 72,510.00 USD | 83,620.00 USD | 308,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 3,030,000.00 USD | 3,030,000.00 USD | 35,540.00 USD | 211,200.00 USD | 124,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 3,140,000.00 USD | 3,140,000.00 USD | 55,220.00 USD | 25,290.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 3,510,000.00 USD | 3,510,000.00 USD | 242,240.00 USD | 31,090.00 USD | 94,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 4,320,000.00 USD | 4,320,000.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 5,020,000.00 USD | 5,020,000.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 5,990,000.00 USD | 5,990,000.00 USD | 505,530.00 USD | 177,660.00 USD | 289,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 7,440,000.00 USD | 7,440,000.00 USD | 753,960.00 USD | 198,610.00 USD | 493,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 7,810,000.00 USD | 7,810,000.00 USD | 176,210.00 USD | 62,330.00 USD | 132,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 8,230,000.00 USD | 8,230,000.00 USD | 193,160.00 USD | 96,300.00 USD | 138,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 2,580.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 8,580,000.00 USD | 8,580,000.00 USD | 192,160.00 USD | 58,850.00 USD | 90,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 9,080,000.00 USD | 9,080,000.00 USD | 245,390.00 USD | 80,790.00 USD | 180,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 9,180,000.00 USD | 9,180,000.00 USD | 51,890.00 USD | 18,760.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2160` | 9,360,000.00 USD | 9,360,000.00 USD | 99,140.00 USD | 33,680.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 9,520,000.00 USD | 9,520,000.00 USD | 61,590.00 USD | 17,680.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2180` | 9,700,000.00 USD | 9,700,000.00 USD | 78,970.00 USD | 36,240.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2190` | 9,870,000.00 USD | 9,870,000.00 USD | 85,280.00 USD | 39,700.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2195` | 252.21 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2200` | 10,030,000.00 USD | 10,030,000.00 USD | 83,270.00 USD | 24,600.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 10,110,000.00 USD | 10,110,000.00 USD | 36,960.00 USD | 20,190.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 11,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 10,230,000.00 USD | 10,230,000.00 USD | 73,390.00 USD | 8,880.00 USD | 36,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 10,280,000.00 USD | 10,280,000.00 USD | 22,600.00 USD | 8,440.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 11,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2240` | 10,350,000.00 USD | 10,350,000.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 13,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,520.00 USD | 23,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2305` | 14,760.00 USD | 37,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2315` | 439.39 USD | 38,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 38,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 46,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 47,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,370.00 USD | 76,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 76,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 1,400.00 USD | 77,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 298.11 USD | 78,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 78,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 425.73 USD | 79,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 2,590.00 USD | 81,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 83,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 84,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 87,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 87,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 95,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2975` | 43,340.00 USD | 139,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 139,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3035` | 76,470.00 USD | 215,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 216,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 1,090.00 USD | 217,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,310.00 USD | 314,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 758.15 USD | 315,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 4,290.00 USD | 319,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3195` | 188.50 USD | 319,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 2,460.00 USD | 322,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 84,060.00 USD | 406,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 315.88 USD | 406,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3355` | 105.01 USD | 406,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 748.71 USD | 407,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 250.96 USD | 407,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 140.95 USD | 408,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3585` | 911.67 USD | 408,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3605` | 2,450.00 USD | 411,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 162.04 USD | 411,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3635` | 332.60 USD | 411,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 1,560.00 USD | 413,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 422,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3725` | 268,480.00 USD | 691,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3735` | 27,620.00 USD | 718,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 721,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0415` | 2,260,000.00 USD | 0.00 USD | 1,030.00 USD | `-78.19%` | `24,798.00` |
| `Live` | `Long` | `0.0435` | 2,260,000.00 USD | 0.00 USD | 232.20 USD | `-77.14%` | `5,338.00` |
| `Live` | `Long` | `0.0465` | 2,260,000.00 USD | 0.00 USD | 348.75 USD | `-75.56%` | `7,500.00` |
| `Live` | `Long` | `0.0535` | 2,260,000.00 USD | 0.00 USD | 481.50 USD | `-71.88%` | `9,000.00` |
| `Live` | `Long` | `0.0565` | 2,260,000.00 USD | 0.00 USD | 1,350.00 USD | `-70.30%` | `23,814.00` |
| `Live` | `Long` | `0.0655` | 2,260,000.00 USD | 0.00 USD | 3,170.00 USD | `-65.57%` | `48,444.00` |
| `Live` | `Long` | `0.0665` | 2,250,000.00 USD | 0.00 USD | 9,540.00 USD | `-65.05%` | `143,443.00` |
| `Live` | `Long` | `0.0675` | 2,240,000.00 USD | 0.00 USD | 1,350.00 USD | `-64.52%` | `20,000.00` |
| `Live` | `Long` | `0.0695` | 2,240,000.00 USD | 0.00 USD | 7,300.00 USD | `-63.47%` | `105,008.00` |
| `Live` | `Long` | `0.0815` | 2,240,000.00 USD | 0.00 USD | 284.84 USD | `-57.16%` | `3,495.00` |
| `Live` | `Long` | `0.0865` | 2,240,000.00 USD | 0.00 USD | 102.50 USD | `-54.54%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,230,000.00 USD | 0.00 USD | 344.75 USD | `-54.01%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,230,000.00 USD | 0.00 USD | 166,980.00 USD | `-53.48%` | `1,886,753.00` |
| `Live` | `Long` | `0.0925` | 2,070,000.00 USD | 0.00 USD | 326.43 USD | `-51.38%` | `3,529.00` |
| `Live` | `Long` | `0.0935` | 2,070,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.86%` | `17,251.00` |
| `Live` | `Long` | `0.0945` | 2,070,000.00 USD | 0.00 USD | 945.00 USD | `-50.33%` | `10,000.00` |
| `Live` | `Long` | `0.0955` | 2,060,000.00 USD | 0.00 USD | 331.00 USD | `-49.81%` | `3,466.00` |
| `Live` | `Long` | `0.1025` | 2,060,000.00 USD | 0.00 USD | 4,100.00 USD | `-46.13%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,060,000.00 USD | 0.00 USD | 1,050.00 USD | `-45.60%` | `10,149.00` |
| `Live` | `Long` | `0.1065` | 2,060,000.00 USD | 0.00 USD | 793.42 USD | `-44.02%` | `7,450.00` |
| `Live` | `Long` | `0.1085` | 2,060,000.00 USD | 0.00 USD | 526.77 USD | `-42.97%` | `4,855.00` |
| `Live` | `Long` | `0.1095` | 2,060,000.00 USD | 0.00 USD | 1,490.00 USD | `-42.45%` | `13,608.00` |
| `Live` | `Long` | `0.1105` | 2,060,000.00 USD | 0.00 USD | 467.30 USD | `-41.92%` | `4,229.00` |
| `Live` | `Long` | `0.1145` | 2,060,000.00 USD | 0.00 USD | 5,380.00 USD | `-39.82%` | `46,944.00` |
| `Live` | `Long` | `0.1165` | 2,050,000.00 USD | 0.00 USD | 13,480.00 USD | `-38.77%` | `115,721.00` |
| `Live` | `Long` | `0.1175` | 2,040,000.00 USD | 0.00 USD | 931.42 USD | `-38.24%` | `7,927.00` |
| `Live` | `Long` | `0.1195` | 2,040,000.00 USD | 0.00 USD | 150.21 USD | `-37.19%` | `1,257.00` |
| `Live` | `Long` | `0.1205` | 2,040,000.00 USD | 0.00 USD | 826.27 USD | `-36.67%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,040,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.14%` | `8,652.00` |
| `Live` | `Long` | `0.1245` | 2,030,000.00 USD | 0.00 USD | 2,970.00 USD | `-34.56%` | `23,844.00` |
| `Live` | `Long` | `0.1255` | 2,030,000.00 USD | 0.00 USD | 1,980.00 USD | `-34.04%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,030,000.00 USD | 0.00 USD | 314.61 USD | `-33.51%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,030,000.00 USD | 0.00 USD | 1,260.00 USD | `-32.99%` | `9,873.00` |
| `Live` | `Long` | `0.1285` | 2,030,000.00 USD | 0.00 USD | 407.09 USD | `-32.46%` | `3,168.00` |
| `Live` | `Long` | `0.1295` | 2,030,000.00 USD | 0.00 USD | 2,540.00 USD | `-31.94%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,020,000.00 USD | 0.00 USD | 290.36 USD | `-31.41%` | `2,225.00` |
| `Live` | `Long` | `0.1315` | 2,020,000.00 USD | 0.00 USD | 687.35 USD | `-30.88%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,020,000.00 USD | 0.00 USD | 8,950.00 USD | `-30.36%` | `67,553.00` |
| `Live` | `Long` | `0.1335` | 2,010,000.00 USD | 0.00 USD | 3,600.00 USD | `-29.83%` | `26,965.00` |
| `Live` | `Long` | `0.1345` | 2,010,000.00 USD | 0.00 USD | 63,140.00 USD | `-29.31%` | `469,434.00` |
| `Live` | `Long` | `0.1355` | 1,950,000.00 USD | 0.00 USD | 106.64 USD | `-28.78%` | `787.00` |
| `Live` | `Long` | `0.1385` | 1,950,000.00 USD | 0.00 USD | 2,180.00 USD | `-27.20%` | `15,737.00` |
| `Live` | `Long` | `0.1405` | 1,950,000.00 USD | 0.00 USD | 565.51 USD | `-26.15%` | `4,025.00` |
| `Live` | `Long` | `0.1415` | 1,950,000.00 USD | 0.00 USD | 9,740.00 USD | `-25.63%` | `68,863.00` |
| `Live` | `Long` | `0.1425` | 1,940,000.00 USD | 0.00 USD | 1,010.00 USD | `-25.10%` | `7,053.00` |
| `Live` | `Long` | `0.1435` | 1,930,000.00 USD | 0.00 USD | 16,640.00 USD | `-24.58%` | `115,977.00` |
| `Live` | `Long` | `0.1445` | 1,920,000.00 USD | 0.00 USD | 1,890.00 USD | `-24.05%` | `13,058.00` |
| `Live` | `Long` | `0.1455` | 1,920,000.00 USD | 0.00 USD | 3,770.00 USD | `-23.53%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 1,910,000.00 USD | 0.00 USD | 4,580.00 USD | `-23.00%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 1,910,000.00 USD | 0.00 USD | 882.93 USD | `-22.47%` | `5,986.00` |
| `Live` | `Long` | `0.1485` | 1,910,000.00 USD | 0.00 USD | 163.65 USD | `-21.95%` | `1,102.00` |
| `Live` | `Long` | `0.1495` | 1,910,000.00 USD | 0.00 USD | 138.14 USD | `-21.42%` | `924.00` |
| `Live` | `Long` | `0.1505` | 1,910,000.00 USD | 0.00 USD | 144.33 USD | `-20.90%` | `959.00` |
| `Live` | `Long` | `0.1515` | 1,910,000.00 USD | 0.00 USD | 37,390.00 USD | `-20.37%` | `246,812.00` |
| `Live` | `Long` | `0.1525` | 1,870,000.00 USD | 0.00 USD | 981.95 USD | `-19.85%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 1,870,000.00 USD | 0.00 USD | 43,060.00 USD | `-19.32%` | `280,495.00` |
| `Live` | `Long` | `0.1545` | 1,820,000.00 USD | 0.00 USD | 4,510.00 USD | `-18.80%` | `29,174.00` |
| `Live` | `Long` | `0.1555` | 1,820,000.00 USD | 0.00 USD | 504.44 USD | `-18.27%` | `3,244.00` |
| `Live` | `Long` | `0.1565` | 1,820,000.00 USD | 0.00 USD | 10,860.00 USD | `-17.74%` | `69,381.00` |
| `Live` | `Long` | `0.1575` | 1,810,000.00 USD | 0.00 USD | 5,760.00 USD | `-17.22%` | `36,552.00` |
| `Live` | `Long` | `0.1585` | 1,800,000.00 USD | 0.00 USD | 6,000.00 USD | `-16.69%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,800,000.00 USD | 0.00 USD | 929.88 USD | `-16.17%` | `5,830.00` |
| `Live` | `Long` | `0.1605` | 1,800,000.00 USD | 0.00 USD | 634,470.00 USD | `-15.64%` | `3,953,111.00` |
| `Live` | `Long` | `0.1615` | 1,160,000.00 USD | 0.00 USD | 5,740.00 USD | `-15.12%` | `35,537.00` |
| `Live` | `Long` | `0.1625` | 1,160,000.00 USD | 0.00 USD | 2,180.00 USD | `-14.59%` | `13,446.00` |
| `Live` | `Long` | `0.1645` | 1,150,000.00 USD | 0.00 USD | 10,540.00 USD | `-13.54%` | `64,095.00` |
| `Live` | `Long` | `0.1655` | 1,140,000.00 USD | 0.00 USD | 2,230.00 USD | `-13.01%` | `13,493.00` |
| `Live` | `Long` | `0.1665` | 1,140,000.00 USD | 0.00 USD | 1,120.00 USD | `-12.49%` | `6,700.00` |
| `Live` | `Long` | `0.1675` | 1,140,000.00 USD | 0.00 USD | 1,690.00 USD | `-11.96%` | `10,103.00` |
| `Live` | `Long` | `0.1685` | 1,140,000.00 USD | 0.00 USD | 1,750.00 USD | `-11.44%` | `10,397.00` |
| `Live` | `Long` | `0.1695` | 1,140,000.00 USD | 0.00 USD | 1,280.00 USD | `-10.91%` | `7,557.00` |
| `Live` | `Long` | `0.1705` | 1,140,000.00 USD | 0.00 USD | 619,120.00 USD | `-10.39%` | `3,631,197.00` |
| `Live` | `Long` | `0.1715` | 516,150.00 USD | 0.00 USD | 252,270.00 USD | `-9.86%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 263,880.00 USD | 0.00 USD | 34,840.00 USD | `-9.33%` | `201,982.00` |
| `Live` | `Long` | `0.1735` | 229,040.00 USD | 0.00 USD | 2,430.00 USD | `-8.81%` | `14,022.00` |
| `Live` | `Long` | `0.1745` | 226,600.00 USD | 0.00 USD | 1,320.00 USD | `-8.28%` | `7,554.00` |
| `Live` | `Long` | `0.1755` | 225,290.00 USD | 0.00 USD | 61,110.00 USD | `-7.76%` | `348,224.00` |
| `Live` | `Long` | `0.1765` | 164,170.00 USD | 0.00 USD | 5,110.00 USD | `-7.23%` | `28,930.00` |
| `Live` | `Long` | `0.1775` | 159,070.00 USD | 0.00 USD | 17,370.00 USD | `-6.71%` | `97,880.00` |
| `Live` | `Long` | `0.1785` | 141,690.00 USD | 0.00 USD | 725.42 USD | `-6.18%` | `4,064.00` |
| `Live` | `Long` | `0.1795` | 140,970.00 USD | 0.00 USD | 11,150.00 USD | `-5.66%` | `62,104.00` |
| `Live` | `Long` | `0.1805` | 129,820.00 USD | 0.00 USD | 82,920.00 USD | `-5.13%` | `459,366.00` |
| `Live` | `Long` | `0.1815` | 46,900.00 USD | 0.00 USD | 7,670.00 USD | `-4.60%` | `42,240.00` |
| `Live` | `Long` | `0.1825` | 39,240.00 USD | 0.00 USD | 18,560.00 USD | `-4.08%` | `101,700.00` |
| `Live` | `Long` | `0.1845` | 20,680.00 USD | 0.00 USD | 9,000.00 USD | `-3.03%` | `48,772.00` |
| `Live` | `Long` | `0.1855` | 11,680.00 USD | 0.00 USD | 6,570.00 USD | `-2.50%` | `35,424.00` |
| `Live` | `Long` | `0.1865` | 5,110.00 USD | 0.00 USD | 3,850.00 USD | `-1.98%` | `20,661.00` |
| `Live` | `Long` | `0.1875` | 1,250.00 USD | 0.00 USD | 451.69 USD | `-1.45%` | `2,409.00` |
| `Live` | `Long` | `0.1895` | 802.34 USD | 0.00 USD | 802.34 USD | `-0.40%` | `4,234.00` |
| `Live` | `Short` | `0.1905` | 635.51 USD | 635.51 USD | 0.00 USD | `+0.13%` | `3,336.00` |
| `Live` | `Short` | `0.2005` | 805.13 USD | 169.62 USD | 0.00 USD | `+5.38%` | `846.00` |
| `Live` | `Short` | `0.2015` | 1,270.00 USD | 461.03 USD | 0.00 USD | `+5.91%` | `2,288.00` |
| `Live` | `Short` | `0.2025` | 6,830.00 USD | 5,560.00 USD | 0.00 USD | `+6.43%` | `27,473.00` |
| `Live` | `Short` | `0.2125` | 9,410.00 USD | 2,580.00 USD | 0.00 USD | `+11.69%` | `12,141.00` |
| `Live` | `Short` | `0.2195` | 9,660.00 USD | 252.21 USD | 0.00 USD | `+15.37%` | `1,149.00` |
| `Live` | `Short` | `0.2215` | 11,310.00 USD | 1,640.00 USD | 0.00 USD | `+16.42%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 11,510.00 USD | 200.48 USD | 0.00 USD | `+17.47%` | `897.00` |
| `Live` | `Short` | `0.2275` | 13,670.00 USD | 2,160.00 USD | 0.00 USD | `+19.57%` | `9,500.00` |
| `Live` | `Short` | `0.2285` | 23,190.00 USD | 9,520.00 USD | 0.00 USD | `+20.10%` | `41,679.00` |
| `Live` | `Short` | `0.2305` | 37,950.00 USD | 14,760.00 USD | 0.00 USD | `+21.15%` | `64,029.00` |
| `Live` | `Short` | `0.2315` | 38,390.00 USD | 439.39 USD | 0.00 USD | `+21.68%` | `1,898.00` |
| `Live` | `Short` | `0.2325` | 38,670.00 USD | 282.02 USD | 0.00 USD | `+22.20%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 46,310.00 USD | 7,640.00 USD | 0.00 USD | `+22.73%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 47,780.00 USD | 1,470.00 USD | 0.00 USD | `+26.41%` | `6,110.00` |
| `Live` | `Short` | `0.2525` | 76,150.00 USD | 28,370.00 USD | 0.00 USD | `+32.71%` | `112,352.00` |
| `Live` | `Short` | `0.2585` | 76,530.00 USD | 380.25 USD | 0.00 USD | `+35.87%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 77,930.00 USD | 1,400.00 USD | 0.00 USD | `+37.44%` | `5,346.00` |
| `Live` | `Short` | `0.2715` | 78,220.00 USD | 298.11 USD | 0.00 USD | `+42.70%` | `1,098.00` |
| `Live` | `Short` | `0.2775` | 78,600.00 USD | 379.62 USD | 0.00 USD | `+45.85%` | `1,368.00` |
| `Live` | `Short` | `0.2825` | 79,030.00 USD | 425.73 USD | 0.00 USD | `+48.48%` | `1,507.00` |
| `Live` | `Short` | `0.2835` | 81,610.00 USD | 2,590.00 USD | 0.00 USD | `+49.01%` | `9,121.00` |
| `Live` | `Short` | `0.2845` | 83,790.00 USD | 2,170.00 USD | 0.00 USD | `+49.53%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 84,200.00 USD | 411.09 USD | 0.00 USD | `+52.16%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 87,460.00 USD | 3,260.00 USD | 0.00 USD | `+53.21%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 87,980.00 USD | 519.79 USD | 0.00 USD | `+54.26%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 95,970.00 USD | 7,990.00 USD | 0.00 USD | `+55.31%` | `27,027.00` |
| `Live` | `Short` | `0.2975` | 139,310.00 USD | 43,340.00 USD | 0.00 USD | `+56.36%` | `145,687.00` |
| `Live` | `Short` | `0.3005` | 139,460.00 USD | 146.34 USD | 0.00 USD | `+57.94%` | `487.00` |
| `Live` | `Short` | `0.3035` | 215,920.00 USD | 76,470.00 USD | 0.00 USD | `+59.52%` | `251,952.00` |
| `Live` | `Short` | `0.3055` | 216,330.00 USD | 408.15 USD | 0.00 USD | `+60.57%` | `1,336.00` |
| `Live` | `Short` | `0.3105` | 217,420.00 USD | 1,090.00 USD | 0.00 USD | `+63.20%` | `3,500.00` |
| `Live` | `Short` | `0.3115` | 314,730.00 USD | 97,310.00 USD | 0.00 USD | `+63.72%` | `312,388.00` |
| `Live` | `Short` | `0.3155` | 315,490.00 USD | 758.15 USD | 0.00 USD | `+65.83%` | `2,403.00` |
| `Live` | `Short` | `0.3175` | 319,770.00 USD | 4,290.00 USD | 0.00 USD | `+66.88%` | `13,504.00` |
| `Live` | `Short` | `0.3195` | 319,960.00 USD | 188.50 USD | 0.00 USD | `+67.93%` | `590.00` |
| `Live` | `Short` | `0.3275` | 322,420.00 USD | 2,460.00 USD | 0.00 USD | `+72.13%` | `7,515.00` |
| `Live` | `Short` | `0.3295` | 406,490.00 USD | 84,060.00 USD | 0.00 USD | `+73.18%` | `255,121.00` |
| `Live` | `Short` | `0.3325` | 406,800.00 USD | 315.88 USD | 0.00 USD | `+74.76%` | `950.00` |
| `Live` | `Short` | `0.3355` | 406,910.00 USD | 105.01 USD | 0.00 USD | `+76.34%` | `313.00` |
| `Live` | `Short` | `0.3365` | 407,660.00 USD | 748.71 USD | 0.00 USD | `+76.86%` | `2,225.00` |
| `Live` | `Short` | `0.3505` | 407,910.00 USD | 250.96 USD | 0.00 USD | `+84.22%` | `716.00` |
| `Live` | `Short` | `0.3515` | 408,050.00 USD | 140.95 USD | 0.00 USD | `+84.75%` | `401.00` |
| `Live` | `Short` | `0.3585` | 408,960.00 USD | 911.67 USD | 0.00 USD | `+88.43%` | `2,543.00` |
| `Live` | `Short` | `0.3605` | 411,410.00 USD | 2,450.00 USD | 0.00 USD | `+89.48%` | `6,797.00` |
| `Live` | `Short` | `0.3625` | 411,570.00 USD | 162.04 USD | 0.00 USD | `+90.53%` | `447.00` |
| `Live` | `Short` | `0.3635` | 411,900.00 USD | 332.60 USD | 0.00 USD | `+91.05%` | `915.00` |
| `Live` | `Short` | `0.3675` | 413,470.00 USD | 1,560.00 USD | 0.00 USD | `+93.16%` | `4,254.00` |
| `Live` | `Short` | `0.3715` | 422,640.00 USD | 9,170.00 USD | 0.00 USD | `+95.26%` | `24,689.00` |
| `Live` | `Short` | `0.3725` | 691,120.00 USD | 268,480.00 USD | 0.00 USD | `+95.78%` | `720,753.00` |
| `Live` | `Short` | `0.3735` | 718,740.00 USD | 27,620.00 USD | 0.00 USD | `+96.31%` | `73,959.00` |
| `Live` | `Short` | `0.3745` | 721,890.00 USD | 3,140.00 USD | 0.00 USD | `+96.84%` | `8,395.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 833,240.00 USD | 0.00 USD | 415.13 USD | `-68.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 832,830.00 USD | 0.00 USD | 438.99 USD | `-68.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 832,390.00 USD | 0.00 USD | 1,100.00 USD | `-41.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 831,280.00 USD | 0.00 USD | 541.33 USD | `-41.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 830,740.00 USD | 0.00 USD | 602,500.00 USD | `-36.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 228,240.00 USD | 0.00 USD | 4,460.00 USD | `-35.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 223,780.00 USD | 0.00 USD | 1,320.00 USD | `-32.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 222,460.00 USD | 0.00 USD | 13,390.00 USD | `-31.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 209,070.00 USD | 0.00 USD | 728.88 USD | `-30.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 208,340.00 USD | 0.00 USD | 4,910.00 USD | `-29.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 203,430.00 USD | 0.00 USD | 4,730.00 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 198,700.00 USD | 0.00 USD | 1,820.00 USD | `-26.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 196,880.00 USD | 0.00 USD | 1,050.00 USD | `-25.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 195,830.00 USD | 0.00 USD | 2,110.00 USD | `-25.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 193,720.00 USD | 0.00 USD | 1,600.00 USD | `-24.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 192,120.00 USD | 0.00 USD | 4,580.00 USD | `-23.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 187,540.00 USD | 0.00 USD | 303.26 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 187,240.00 USD | 0.00 USD | 1,290.00 USD | `-20.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 185,950.00 USD | 0.00 USD | 279.53 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 185,670.00 USD | 0.00 USD | 324.30 USD | `-18.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 185,350.00 USD | 0.00 USD | 1,480.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 183,870.00 USD | 0.00 USD | 552.21 USD | `-16.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 183,320.00 USD | 0.00 USD | 166.84 USD | `-16.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 183,150.00 USD | 0.00 USD | 2,990.00 USD | `-15.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 180,160.00 USD | 0.00 USD | 562.67 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 179,600.00 USD | 0.00 USD | 24,760.00 USD | `-14.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 154,840.00 USD | 0.00 USD | 6,540.00 USD | `-14.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 148,300.00 USD | 0.00 USD | 2,870.00 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 145,430.00 USD | 0.00 USD | 452.97 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 144,980.00 USD | 0.00 USD | 13,930.00 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 131,050.00 USD | 0.00 USD | 317.92 USD | `-11.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 130,730.00 USD | 0.00 USD | 6,740.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 123,990.00 USD | 0.00 USD | 4,270.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 119,720.00 USD | 0.00 USD | 7,630.00 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 112,090.00 USD | 0.00 USD | 6,860.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 105,230.00 USD | 0.00 USD | 6,900.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 98,330.00 USD | 0.00 USD | 103.58 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 98,220.00 USD | 0.00 USD | 8,060.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 90,160.00 USD | 0.00 USD | 1,760.00 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 88,400.00 USD | 0.00 USD | 623.57 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 87,770.00 USD | 0.00 USD | 4,440.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 83,340.00 USD | 0.00 USD | 12,840.00 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 70,490.00 USD | 0.00 USD | 1,260.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 69,230.00 USD | 0.00 USD | 23,430.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 45,810.00 USD | 0.00 USD | 3,380.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 42,430.00 USD | 0.00 USD | 3,080.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 39,350.00 USD | 0.00 USD | 5,220.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 34,130.00 USD | 0.00 USD | 18,800.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 15,320.00 USD | 0.00 USD | 6,770.00 USD | `-2.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 8,560.00 USD | 0.00 USD | 218.76 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 8,340.00 USD | 0.00 USD | 109.69 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 8,230.00 USD | 0.00 USD | 7,390.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 837.40 USD | 0.00 USD | 837.40 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 6,450.00 USD | 6,450.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 8,480.00 USD | 2,030.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 8,990.00 USD | 513.01 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 11,470.00 USD | 2,480.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 12,230.00 USD | 761.27 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 12,360.00 USD | 125.51 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 15,910.00 USD | 3,550.00 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 16,500.00 USD | 592.30 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 16,870.00 USD | 365.04 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 17,070.00 USD | 199.50 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 80,230,000.00 USD | 80,210,000.00 USD | 0.00 USD | `+5.38%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2015` | 80,240,000.00 USD | 18,790.00 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 80,240,000.00 USD | 101.86 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 80,240,000.00 USD | 752.34 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 80,250,000.00 USD | 1,980.00 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 162,450,000.00 USD | 82,200,000.00 USD | 0.00 USD | `+8.01%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2065` | 162,450,000.00 USD | 1,250.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 162,450,000.00 USD | 312.70 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 162,450,000.00 USD | 3,320.00 USD | 0.00 USD | `+9.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 162,460,000.00 USD | 8,720.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 162,490,000.00 USD | 28,440.00 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 162,500,000.00 USD | 11,750.00 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 162,510,000.00 USD | 5,620.00 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 162,520,000.00 USD | 9,890.00 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 162,520,000.00 USD | 1,800.00 USD | 0.00 USD | `+12.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 162,520,000.00 USD | 1,570.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 162,520,000.00 USD | 219.53 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 162,520,000.00 USD | 109.91 USD | 0.00 USD | `+14.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 162,530,000.00 USD | 6,920.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 162,550,000.00 USD | 18,630.00 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 162,550,000.00 USD | 1,650.00 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 162,550,000.00 USD | 1,690.00 USD | 0.00 USD | `+16.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 162,550,000.00 USD | 501.31 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 162,550,000.00 USD | 114.50 USD | 0.00 USD | `+18.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 162,550,000.00 USD | 202.27 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 162,550,000.00 USD | 109.40 USD | 0.00 USD | `+19.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 162,570,000.00 USD | 21,490.00 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 162,580,000.00 USD | 9,140.00 USD | 0.00 USD | `+20.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 162,590,000.00 USD | 9,180.00 USD | 0.00 USD | `+20.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 162,590,000.00 USD | 662.92 USD | 0.00 USD | `+21.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 162,600,000.00 USD | 9,600.00 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 162,600,000.00 USD | 171.12 USD | 0.00 USD | `+22.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 162,610,000.00 USD | 9,340.00 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 162,610,000.00 USD | 1,010.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 162,620,000.00 USD | 9,420.00 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 162,620,000.00 USD | 315.96 USD | 0.00 USD | `+24.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 162,620,000.00 USD | 650.04 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 162,620,000.00 USD | 192.71 USD | 0.00 USD | `+25.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 162,630,000.00 USD | 10,090.00 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 162,630,000.00 USD | 209.72 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 162,630,000.00 USD | 115.92 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 162,630,000.00 USD | 236.19 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 162,640,000.00 USD | 10,930.00 USD | 0.00 USD | `+28.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 162,640,000.00 USD | 288.22 USD | 0.00 USD | `+29.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 162,640,000.00 USD | 491.03 USD | 0.00 USD | `+29.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 162,640,000.00 USD | 1,320.00 USD | 0.00 USD | `+30.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 162,650,000.00 USD | 9,940.00 USD | 0.00 USD | `+30.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 162,650,000.00 USD | 499.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 162,660,000.00 USD | 1,100.00 USD | 0.00 USD | `+31.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 162,660,000.00 USD | 168.76 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 162,660,000.00 USD | 603.73 USD | 0.00 USD | `+32.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 162,660,000.00 USD | 2,170.00 USD | 0.00 USD | `+33.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 162,660,000.00 USD | 1,570.00 USD | 0.00 USD | `+34.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 162,660,000.00 USD | 1,470.00 USD | 0.00 USD | `+35.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 162,660,000.00 USD | 271.44 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 163,080,000.00 USD | 421,590.00 USD | 0.00 USD | `+36.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 163,080,000.00 USD | 1,180.00 USD | 0.00 USD | `+39.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 163,090,000.00 USD | 945.98 USD | 0.00 USD | `+39.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 163,090,000.00 USD | 8,890.00 USD | 0.00 USD | `+40.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 163,110,000.00 USD | 14,860.00 USD | 0.00 USD | `+41.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 163,110,000.00 USD | 1,340.00 USD | 0.00 USD | `+41.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 163,110,000.00 USD | 2,710.00 USD | 0.00 USD | `+42.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 163,130,000.00 USD | 13,870.00 USD | 0.00 USD | `+43.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 163,130,000.00 USD | 5,220.00 USD | 0.00 USD | `+44.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 163,130,000.00 USD | 944.99 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 163,130,000.00 USD | 161.87 USD | 0.00 USD | `+48.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 163,130,000.00 USD | 113.68 USD | 0.00 USD | `+49.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 163,140,000.00 USD | 1,370.00 USD | 0.00 USD | `+49.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 163,140,000.00 USD | 1,080.00 USD | 0.00 USD | `+51.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 163,150,000.00 USD | 14,980.00 USD | 0.00 USD | `+52.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 163,150,000.00 USD | 1,230.00 USD | 0.00 USD | `+53.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 163,150,000.00 USD | 1,440.00 USD | 0.00 USD | `+56.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 163,150,000.00 USD | 355.21 USD | 0.00 USD | `+57.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 163,160,000.00 USD | 6,650.00 USD | 0.00 USD | `+57.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 163,180,000.00 USD | 18,980.00 USD | 0.00 USD | `+60.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 163,180,000.00 USD | 4,150.00 USD | 0.00 USD | `+62.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 163,190,000.00 USD | 3,250.00 USD | 0.00 USD | `+65.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 163,190,000.00 USD | 5,090.00 USD | 0.00 USD | `+68.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 163,190,000.00 USD | 493.89 USD | 0.00 USD | `+70.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 163,190,000.00 USD | 181.30 USD | 0.00 USD | `+71.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 163,190,000.00 USD | 1,380.00 USD | 0.00 USD | `+73.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 163,210,000.00 USD | 12,290.00 USD | 0.00 USD | `+74.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 163,210,000.00 USD | 111.06 USD | 0.00 USD | `+75.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 163,210,000.00 USD | 220.61 USD | 0.00 USD | `+79.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 163,210,000.00 USD | 3,850.00 USD | 0.00 USD | `+83.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 163,210,000.00 USD | 188.75 USD | 0.00 USD | `+98.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 163,210,000.00 USD | 121.76 USD | 0.00 USD | `+99.99%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1700` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD |
| `1D` | `0.1710` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 23,820.00 USD | 700.07 USD | 12,980.00 USD |
| `1D` | `0.1720` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 0.00 USD | 321.20 USD | 18,400.00 USD |
| `1D` | `0.1730` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 0.00 USD | 4,280.00 USD | 13,510.00 USD |
| `1D` | `0.1740` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `1D` | `0.1760` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD |
| `1D` | `0.1770` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 53,230.00 USD | 18,310.00 USD | 79,670.00 USD |
| `1D` | `0.1780` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 62,120.00 USD | 34,290.00 USD | 67,000.00 USD |
| `1D` | `0.1790` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 73,150.00 USD | 37,690.00 USD | 46,170.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 75,870.00 USD | 25,350.00 USD | 47,570.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 38,430.00 USD | 23,350.00 USD | 44,490.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 136,500.00 USD | 9,890.00 USD | 68,570.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 32,650.00 USD | 21,120.00 USD | 65,060.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 77,630.00 USD | 29,420.00 USD | 52,530.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 128,210.00 USD | 59,950.00 USD | 142,390.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 159,010.00 USD | 7,290.00 USD | 72,660.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 102,920.00 USD | 49,970.00 USD | 119,340.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 223,120.00 USD | 49,550.00 USD | 60,450.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 162,010.00 USD | 110,140.00 USD | 36,600.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 114,440.00 USD | 0.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 292,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `1D` | `0.1920` | 861,870.00 USD | 0.00 USD | 861,870.00 USD | 470,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 391,530.00 USD | 0.00 USD | 391,530.00 USD | 361,640.00 USD | 0.00 USD | 29,890.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 214,200.00 USD | 214,200.00 USD | 0.00 USD | 139,920.00 USD | 0.00 USD | 74,280.00 USD |
| `1D` | `0.1940` | 428,400.00 USD | 428,400.00 USD | 0.00 USD | 139,920.00 USD | 0.00 USD | 74,280.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 570,840.00 USD | 570,840.00 USD | 0.00 USD | 21,890.00 USD | 20,360.00 USD | 100,190.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 823,190.00 USD | 823,190.00 USD | 0.00 USD | 6,090.00 USD | 178,720.00 USD | 67,540.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 907,090.00 USD | 907,090.00 USD | 0.00 USD | 0.00 USD | 30,910.00 USD | 52,980.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 62,420.00 USD | 1,260.00 USD | 32,450.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 50,670.00 USD | 37,620.00 USD | 74,350.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 188,460.00 USD | 13,490.00 USD | 204,800.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 101,890.00 USD | 121,910.00 USD | 243,590.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 32,560.00 USD | 27,550.00 USD | 89,070.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 72,510.00 USD | 83,620.00 USD | 308,470.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 35,540.00 USD | 211,200.00 USD | 124,890.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 55,220.00 USD | 25,290.00 USD | 33,330.00 USD |
| `1D` | `0.2060` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 242,240.00 USD | 31,090.00 USD | 94,760.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 505,530.00 USD | 177,660.00 USD | 289,790.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 753,960.00 USD | 198,610.00 USD | 493,130.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 176,210.00 USD | 62,330.00 USD | 132,480.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 193,160.00 USD | 96,300.00 USD | 138,440.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 192,160.00 USD | 58,850.00 USD | 90,320.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 245,390.00 USD | 80,790.00 USD | 180,130.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 51,890.00 USD | 18,760.00 USD | 31,390.00 USD |
| `7D` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `1D` | `0.2160` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 99,140.00 USD | 33,680.00 USD | 44,240.00 USD |
| `7D` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 61,590.00 USD | 17,680.00 USD | 79,670.00 USD |
| `7D` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 78,970.00 USD | 36,240.00 USD | 67,000.00 USD |
| `7D` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 0.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 85,280.00 USD | 39,700.00 USD | 46,170.00 USD |
| `7D` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `1D` | `0.2200` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 83,270.00 USD | 24,600.00 USD | 47,570.00 USD |
| `7D` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 0.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD |
| `1D` | `0.2210` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 36,960.00 USD | 20,190.00 USD | 28,100.00 USD |
| `7D` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `1D` | `0.2220` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 73,390.00 USD | 8,880.00 USD | 36,120.00 USD |
| `7D` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 0.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD |
| `1D` | `0.2230` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 22,600.00 USD | 8,440.00 USD | 19,060.00 USD |
| `7D` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 0.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD |
| `1D` | `0.2240` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD |
| `7D` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 0.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD |
| `7D` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 0.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD |
| `7D` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 0.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD |
| `7D` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 0.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD |
| `7D` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 0.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD |
| `7D` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 0.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD |
| `7D` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 0.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD |
| `7D` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `420.91M` | Total OI Tokens: `2,160,248,368.8 ADA`
  * 1h OI Change: `-5.22%` | 4h OI Change: `-7.45%` | 24h OI Change: `-9.33%`
  * Exchange Breakdown: Binance=`77.98M` | Bybit=`50.41M` | OKX=`30.03M` | Hyperliquid=`28.40M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.50K` | Last 24h: `14.20K` | Last 3d: `57.34K` | Last 7d: `58.14K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0015%` |
| **USDT Bybit** | `-0.0089%` | **USDT KuCoin** | `0.0068%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0002%` | **USDT Bitget** | `0.0006%` |
| **CoinM Binance** | `0.0035%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `54.32%` | `45.68%` | `1.19` | 62,430,000.00 USD |
| `15M` | `Binance` | `52.88%` | `47.12%` | `1.12` | 29,960,000.00 USD |
| `15M` | `OKX` | `53.78%` | `46.22%` | `1.16` | 11,160,000.00 USD |
| `15M` | `Bybit` | `61.63%` | `38.37%` | `1.61` | 5,000,000.00 USD |
| `15M` | `KuCoin` | `44.37%` | `55.63%` | `0.80` | 897,630.00 USD |
| `15M` | `Gate` | `49.61%` | `50.39%` | `0.98` | 4,410,000.00 USD |
| `15M` | `Bitget` | `54.7%` | `45.3%` | `1.21` | 1,720,000.00 USD |
| `15M` | `BingX` | `74.95%` | `25.05%` | `2.99` | 692,290.00 USD |
| `15M` | `MEXC` | `66.7%` | `33.3%` | `2.00` | 3,960,000.00 USD |
| `15M` | `Bitunix` | `44.42%` | `55.58%` | `0.80` | 1,740,000.00 USD |
| `15M` | `Hyperliquid` | `52.65%` | `47.35%` | `1.11` | 460,100.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.78%` | `48.22%` | `1.07` | 149,320.00 USD |
| `15M` | `Crypto.com` | `50.58%` | `49.42%` | `1.02` | 81,590.00 USD |
| `15M` | `WhiteBIT` | `41.05%` | `58.95%` | `0.70` | 438,250.00 USD |
| `15M` | `HTX` | `65.93%` | `34.07%` | `1.94` | 502,250.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `57.55%` | `42.45%` | `1.36` | 277,370.00 USD |
| `15M` | `Aster` | `50.02%` | `49.98%` | `1.00` | 975,210.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.44%` | `2.56%` | `38.06` | 12,180.00 USD |
| `15M` | `Whale Positions` | `52.88%` | `47.12%` | `1.12` | 29,960,000.00 USD |
| `15M` | `Global Accounts` | `54.32%` | `45.68%` | `1.19` | 62,430,000.00 USD |
| `1H` | `ADA` | `45.44%` | `54.56%` | `0.83` | 392,960,000.00 USD |
| `1H` | `Binance` | `44.96%` | `55.04%` | `0.82` | 176,650,000.00 USD |
| `1H` | `OKX` | `46.58%` | `53.42%` | `0.87` | 88,990,000.00 USD |
| `1H` | `Bybit` | `43.99%` | `56.01%` | `0.79` | 43,170,000.00 USD |
| `1H` | `KuCoin` | `43.66%` | `56.34%` | `0.77` | 3,870,000.00 USD |
| `1H` | `Gate` | `48.98%` | `51.02%` | `0.96` | 19,170,000.00 USD |
| `1H` | `Bitget` | `36.91%` | `63.09%` | `0.59` | 11,450,000.00 USD |
| `1H` | `BingX` | `57.07%` | `42.93%` | `1.33` | 3,150,000.00 USD |
| `1H` | `MEXC` | `52.47%` | `47.53%` | `1.10` | 17,250,000.00 USD |
| `1H` | `Bitunix` | `45.55%` | `54.45%` | `0.84` | 9,580,000.00 USD |
| `1H` | `Hyperliquid` | `48.61%` | `51.39%` | `0.95` | 4,220,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.09%` | `47.91%` | `1.09` | 1,450,000.00 USD |
| `1H` | `Crypto.com` | `49.37%` | `50.63%` | `0.98` | 433,310.00 USD |
| `1H` | `WhiteBIT` | `20.18%` | `79.82%` | `0.25` | 3,460,000.00 USD |
| `1H` | `HTX` | `32.59%` | `67.41%` | `0.48` | 3,120,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.71%` | `56.29%` | `0.78` | 1,610,000.00 USD |
| `1H` | `Aster` | `50.69%` | `49.31%` | `1.03` | 5,230,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `56.15%` | `43.85%` | `1.28` | 176,170.00 USD |
| `1H` | `Whale Positions` | `44.96%` | `55.04%` | `0.82` | 176,650,000.00 USD |
| `1H` | `Global Accounts` | `45.44%` | `54.56%` | `0.83` | 392,960,000.00 USD |
| `4H` | `ADA` | `46.11%` | `53.89%` | `0.86` | 591,760,000.00 USD |
| `4H` | `Binance` | `45.33%` | `54.67%` | `0.83` | 248,520,000.00 USD |
| `4H` | `OKX` | `48.01%` | `51.99%` | `0.92` | 131,930,000.00 USD |
| `4H` | `Bybit` | `44.77%` | `55.23%` | `0.81` | 58,540,000.00 USD |
| `4H` | `KuCoin` | `43.79%` | `56.21%` | `0.78` | 4,850,000.00 USD |
| `4H` | `Gate` | `48.59%` | `51.41%` | `0.95` | 47,050,000.00 USD |
| `4H` | `Bitget` | `37.24%` | `62.76%` | `0.59` | 15,560,000.00 USD |
| `4H` | `BingX` | `50.52%` | `49.48%` | `1.02` | 7,460,000.00 USD |
| `4H` | `MEXC` | `53.16%` | `46.84%` | `1.13` | 28,910,000.00 USD |
| `4H` | `Bitunix` | `44.79%` | `55.21%` | `0.81` | 17,520,000.00 USD |
| `4H` | `Hyperliquid` | `47.5%` | `52.5%` | `0.90` | 5,740,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.66%` | `44.34%` | `1.26` | 2,660,000.00 USD |
| `4H` | `Crypto.com` | `49.97%` | `50.03%` | `1.00` | 804,300.00 USD |
| `4H` | `WhiteBIT` | `27.18%` | `72.82%` | `0.37` | 8,310,000.00 USD |
| `4H` | `HTX` | `37.85%` | `62.15%` | `0.61` | 4,200,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.12%` | `55.88%` | `0.79` | 2,500,000.00 USD |
| `4H` | `Aster` | `46.49%` | `53.51%` | `0.87` | 6,970,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.65%` | `51.35%` | `0.95` | 233,330.00 USD |
| `4H` | `Whale Positions` | `45.33%` | `54.67%` | `0.83` | 248,520,000.00 USD |
| `4H` | `Global Accounts` | `46.11%` | `53.89%` | `0.86` | 591,760,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.2017` | `0.2019` | `0.2017` | `0.2026` | `0.2016` | 936,853.56 USD | 534,839.56 USD | 402,014.00 USD | 132,825.56 USD | `+14.18%` | `1B / 1S` |
| `5:00 UTC` | `0.2021` | `0.2021` | `0.2021` | `0.2026` | `0.2016` | 650,847.81 USD | 328,375.32 USD | 322,472.48 USD | 5,902.84 USD | `+0.91%` | `1B / 0S` |
| `0:00 UTC` | `0.2026` | `0.2026` | `0.2026` | `0.2029` | `0.2021` | 795,394.00 USD | 440,558.18 USD | 354,835.82 USD | 85,722.35 USD | `+10.78%` | `1B / 0S` |
| `5:00 UTC` | `0.2024` | `0.2024` | `0.2024` | `0.2029` | `0.2021` | 784,830.17 USD | 348,021.79 USD | 436,808.38 USD | -88,786.59 USD | `-11.31%` | `0B / 1S` |
| `0:00 UTC` | `0.1996` | `0.1995` | `0.1996` | `0.2024` | `0.1980` | 9,482,489.23 USD | 4,643,460.63 USD | 4,839,028.60 USD | -195,567.97 USD | `-2.06%` | `0B / 8S` |
| `5:00 UTC` | `0.1996` | `0.1997` | `0.1996` | `0.2001` | `0.1991` | 2,005,993.91 USD | 876,806.75 USD | 1,129,187.16 USD | -252,380.41 USD | `-12.58%` | `0B / 0S` |
| `0:00 UTC` | `0.1918` | `0.1942` | `0.1918` | `0.2001` | `0.1905` | 24,025,446.30 USD | 10,254,298.46 USD | 13,771,147.84 USD | -3,516,849.37 USD | `-14.64%` | `1B / 19S` |
| `5:00 UTC` | `0.1906` | `0.1904` | `0.1906` | `0.1935` | `0.1871` | 26,316,880.25 USD | 11,827,044.75 USD | 14,489,835.50 USD | -2,662,790.75 USD | `-10.12%` | `1B / 5S` |
| `0:00 UTC` | `0.1903` | `0.1914` | `0.1903` | `0.1931` | `0.1898` | 10,338,146.03 USD | 4,991,420.92 USD | 5,346,725.11 USD | -355,304.19 USD | `-3.44%` | `0B / 1S` |
| `5:00 UTC` | `0.1928` | `0.1937` | `0.1928` | `0.1951` | `0.1923` | 4,554,774.20 USD | 2,242,873.64 USD | 2,311,900.56 USD | -69,026.92 USD | `-1.52%` | `1B / 1S` |

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
| `5m` | 42,740.00 USD | -257,790.00 USD | **`DISTRIBUTION`** |
| `15m` | 13,330.00 USD | -99,230.00 USD | **`DISTRIBUTION`** |
| `30m` | -408,380.00 USD | -3,750,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,520,000.00 USD | -10,830,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,350,000.00 USD | -11,190,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,080,000.00 USD | -12,540,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,320,000.00 USD | -13,280,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,400,000.00 USD | -9,600,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,150,000.00 USD | -8,570,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,960,000.00 USD | -18,200,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -16,980,000.00 USD | -36,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -75,520,000.00 USD | -198,140,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+42.74K` | 15m=`+13.33K` | 1h=`-2.52M` | 24h=`-7.96M`
* Futures Capital Netflows: 5m=`-257.79K` | 15m=`-99.23K` | 1h=`-10.83M` | 24h=`-18.20M`
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
  * `2026-10-30 02:15:01 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1898` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1839` (Risk Distance: `0.0059` pts)
  * +2.5R Take Profit: `0.2044`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1919` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1978` (Risk Distance: `0.0059` pts)
  * +2.5R Take Profit: `0.1773`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1942`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
