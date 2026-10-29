# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1898` | **Live Ask Quote**: `0.1919` | **Mid Price**: `0.1908`
- **Spread Points**: `21.00` | **Spread BPS**: `110.03 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1981` | VWAP Z-Score: `-1.64` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0023` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `29.03` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2112` | Lower -3.00σ Band: `0.1849`
  * Upper +2.51σ Band: `0.2091` | Lower -2.51σ Band: `0.1871`
  * Upper +2.01σ Band: `0.2069` | Lower -2.01σ Band: `0.1893`
  * Upper +2.00σ Band: `0.2068` | Lower -2.00σ Band: `0.1893`
  * Upper +1.28σ Band: `0.2037` | Lower -1.28σ Band: `0.1925`
  * Upper +1.00σ Band: `0.2024` | Lower -1.00σ Band: `0.1937`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1936` | EMA-20=`0.1966` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1988` (Slope: `+0.0000`) | EMA-100=`0.1999`
  * Institutional Anchors: EMA-144=`0.2005` | EMA-200=`0.2011` (Slope: `-0.3620`) | EMA-233=`0.2015`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1862` | Weekly High=`0.2086` | Weekly Low=`0.1862`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1935` (Distance: `-1.36%`)
  * Point of Control (POC) = `0.1912` (Distance: `-0.16%`)
  * Value Area Low (VAL) = `0.1907` (Distance: `+0.11%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2055` | Weekly POC=`0.2031` | Weekly VAL=`0.2005`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1888`
  * London Session (08:00-16:00 UTC): High=`0.1916` | Low=`0.1901`
  * New York Session (13:00-21:00 UTC): High=`0.1920` | Low=`0.1897`
  * Initial Balance (First Hour): IB High=`0.1914` | IB Low=`0.1903`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1901` - `0.1916`
  * Optimal Trade Entry (OTE 0.705): `0.1912`
  * Structural Invalidation Anchor (0.786): `0.1924`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1928` | `0.1932` | `0.1919` | `0.1921` | `5,510,966` | 1,061,118.34 USD | -184,983.60 USD | `-17.43%` | -9,425,986.25 USD | `+0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1922` | `0.1925` | `0.1909` | `0.1911` | `8,969,348` | 1,720,054.75 USD | -266,024.48 USD | `-15.47%` | -9,692,010.72 USD | `+0.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1910` | `0.1910` | `0.1908` | `0.1908` | `163,226` | 31,164.80 USD | -27,420.21 USD | `-87.98%` | -9,719,430.94 USD | `+0.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1940` | `0.1953` | `0.1928` | `0.1928` | `17,469,247` | 3,396,141.31 USD | 88,943.37 USD | `+2.62%` | -9,407,295.81 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1928` | `0.1937` | `0.1919` | `0.1921` | `13,384,532` | 2,581,325.54 USD | -47,676.44 USD | `-1.85%` | -9,454,972.25 USD | `+0.37` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1922` | `0.1925` | `0.1908` | `0.1908` | `9,132,574` | 1,751,219.55 USD | -293,444.69 USD | `-16.76%` | -9,748,416.94 USD | `+0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.2022` | `0.2023` | `0.1871` | `0.1904` | `319,583,639` | 61,830,947.38 USD | -6,627,620.80 USD | `-10.72%` | -8,794,465.17 USD | `-3.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1903` | `0.1953` | `0.1897` | `0.1921` | `118,898,936` | 22,899,002.06 USD | -718,669.23 USD | `-3.14%` | -9,513,134.40 USD | `-0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1922` | `0.1925` | `0.1908` | `0.1908` | `9,127,131` | 1,750,181.02 USD | -292,406.17 USD | `-16.71%` | -9,805,540.57 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1908` | `447,614,398` | 86,481,025.69 USD | -7,639,591.43 USD | `-8.83%` | -10,065,536.34 USD | `-1.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -5,414,333.03 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -4,633,383.98 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1908` | `447,614,398` | 86,481,025.69 USD | -7,639,591.43 USD | `-8.83%` | -10,065,536.34 USD | `-1.62` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1908`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `537` | `0x77ee...2902` | `SHORT` | 4,131,268.32 USD | `21,412,192.00` | `0.1911` | `0.1927` | `0.5625` | -40,016.58 USD | `-0.97%` | `10X Cross` |
| `1258` | `0x123d...3bff` | `LONG` | 1,815,036.83 USD | `9,393,142.00` | `0.2912` | `0.1927` | `0.000000` | -920,699.11 USD | `-50.73%` | `10X Cross` |
| `1295` | `0x7737...bf66` | `SHORT` | 1,754,107.45 USD | `9,091,466.00` | `0.2190` | `0.1927` | `2.04` | 236,882.35 USD | `+13.50%` | `10X Cross` |
| `1604` | `0x5f94...4b96` | `SHORT` | 1,378,531.35 USD | `7,162,318.00` | `0.2303` | `0.1927` | `0.7262` | 270,943.85 USD | `+19.65%` | `10X Cross` |
| `1805` | `0x4982...59e6` | `SHORT` | 1,157,410.79 USD | `5,998,812.00` | `0.1891` | `0.1927` | `0.4046` | -22,852.42 USD | `-1.97%` | `10X Cross` |
| `1855` | `0xcac1...26b3` | `LONG` | 1,117,023.79 USD | `5,803,927.00` | `0.2000` | `0.1927` | `0.000000` | -43,791.79 USD | `-3.92%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2024` | 5,493.95 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.49K USD at 0.2024 USD [API] | `2026-10-28 13:16:55` |
| `ANNOUNCEMENT` | `INFO` | `0.2024` | 6,153.87 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2024 USD [API] | `2026-10-28 13:18:59` |
| `ANNOUNCEMENT` | `INFO` | `0.2028` | 5,091.34 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.09K USD at 0.2028 USD [API] | `2026-10-28 13:23:39` |
| `ANNOUNCEMENT` | `INFO` | `0.2028` | 12,084.83 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 12.08K USD at 0.2028 USD [API] | `2026-10-28 13:23:39` |
| `ANNOUNCEMENT` | `INFO` | `0.2028` | 6,153.56 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2028 USD [API] | `2026-10-28 13:26:24` |
| `ANNOUNCEMENT` | `INFO` | `0.2028` | 6,126.09 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.13K USD at 0.2028 USD [API] | `2026-10-28 14:03:48` |
| `ANNOUNCEMENT` | `INFO` | `0.2028` | 5,194.45 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.19K USD at 0.2028 USD [API] | `2026-10-28 14:03:48` |
| `ANNOUNCEMENT` | `INFO` | `0.2028` | 6,172.72 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.17K USD at 0.2028 USD [API] | `2026-10-28 14:03:48` |
| `ANNOUNCEMENT` | `INFO` | `0.2028` | 12,838.74 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 12.84K USD at 0.2028 USD [API] | `2026-10-28 14:03:48` |
| `ANNOUNCEMENT` | `INFO` | `0.2019` | 5,006.61 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2019 USD [API] | `2026-10-28 14:19:13` |
| `ANNOUNCEMENT` | `INFO` | `0.2019` | 6,646.53 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2019 USD [API] | `2026-10-28 14:19:13` |
| `ANNOUNCEMENT` | `INFO` | `0.2029` | 6,649.35 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2029 USD [API] | `2026-10-28 15:06:37` |
| `ANNOUNCEMENT` | `INFO` | `0.2025` | 6,647.39 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2025 USD [API] | `2026-10-28 15:08:31` |
| `ANNOUNCEMENT` | `INFO` | `0.2034` | 5,082.94 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.08K USD at 0.2034 USD [API] | `2026-10-28 15:27:39` |
| `ANNOUNCEMENT` | `INFO` | `0.2011` | 5,393.43 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.39K USD at 0.2011 USD [API] | `2026-10-28 16:50:22` |
| `ANNOUNCEMENT` | `INFO` | `0.2026` | 6,648.22 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2026 USD [API] | `2026-10-28 17:46:02` |
| `ANNOUNCEMENT` | `INFO` | `0.2025` | 6,231.35 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.23K USD at 0.2025 USD [API] | `2026-10-28 17:45:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2100` (Vol: 191,800.00 USD, Dist: `+8.57%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.2109` (Vol: 224,500.00 USD, Dist: `+9.02%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.2138` (Vol: 289,900.00 USD, Dist: `+10.57%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.2130` (Vol: 459,300.00 USD, Dist: `+10.16%`) | Long MP=`0.1904` (Vol: 143,100.00 USD, Dist: `--1.54%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0385` | 197.12 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Long Liquidation` | `0.1700` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 619,120.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,170,000.00 USD | 4,170,000.00 USD | 23,820.00 USD | 700.07 USD | 12,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 516,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 321.20 USD | 18,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 34,840.00 USD | 263,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 4,280.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,430.00 USD | 229,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 6,690.00 USD | 567.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 226,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1750` | 4,090,000.00 USD | 4,090,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 61,110.00 USD | 225,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 4,070,000.00 USD | 4,070,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 5,110.00 USD | 164,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,980,000.00 USD | 3,980,000.00 USD | 53,230.00 USD | 18,310.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 17,370.00 USD | 159,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,820,000.00 USD | 3,820,000.00 USD | 62,120.00 USD | 34,290.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 725.42 USD | 141,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,660,000.00 USD | 3,660,000.00 USD | 75,310.00 USD | 38,160.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 11,150.00 USD | 140,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 3,500,000.00 USD | 3,500,000.00 USD | 75,870.00 USD | 26,100.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 82,920.00 USD | 129,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 3,350,000.00 USD | 3,350,000.00 USD | 38,430.00 USD | 23,350.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 46,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 3,250,000.00 USD | 3,250,000.00 USD | 139,390.00 USD | 10,510.00 USD | 68,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,560.00 USD | 39,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 3,030,000.00 USD | 3,030,000.00 USD | 32,650.00 USD | 22,130.00 USD | 65,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1840` | 2,910,000.00 USD | 2,910,000.00 USD | 77,630.00 USD | 29,420.00 USD | 52,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 9,000.00 USD | 20,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 2,750,000.00 USD | 2,750,000.00 USD | 127,560.00 USD | 58,700.00 USD | 180,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 6,570.00 USD | 11,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 2,380,000.00 USD | 2,380,000.00 USD | 202,510.00 USD | 3,510.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 3,850.00 USD | 5,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 2,090,000.00 USD | 2,090,000.00 USD | 102,920.00 USD | 49,970.00 USD | 140,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 451.69 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 1,800,000.00 USD | 1,800,000.00 USD | 223,120.00 USD | 49,550.00 USD | 60,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 1,460,000.00 USD | 1,460,000.00 USD | 162,010.00 USD | 110,140.00 USD | 122,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 802.34 USD | 802.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,070,000.00 USD | 1,070,000.00 USD | 104,350.00 USD | 114,440.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1905` | 635.51 USD | 635.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 805,950.00 USD | 805,950.00 USD | 292,920.00 USD | 0.00 USD | 42,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 470,340.00 USD | 470,340.00 USD | 470,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 723,270.00 USD | 723,270.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 937,470.00 USD | 937,470.00 USD | 139,920.00 USD | 0.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 1,080,000.00 USD | 1,080,000.00 USD | 21,890.00 USD | 20,360.00 USD | 100,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,330,000.00 USD | 1,330,000.00 USD | 6,090.00 USD | 178,720.00 USD | 67,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 30,910.00 USD | 138,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 1,750,000.00 USD | 1,750,000.00 USD | 166,770.00 USD | 1,260.00 USD | 75,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1990` | 1,950,000.00 USD | 1,950,000.00 USD | 50,670.00 USD | 37,620.00 USD | 117,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2000` | 2,360,000.00 USD | 2,360,000.00 USD | 188,460.00 USD | 13,490.00 USD | 204,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 169.62 USD | 805.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 2,870,000.00 USD | 2,870,000.00 USD | 101,890.00 USD | 121,910.00 USD | 286,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 461.03 USD | 1,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 3,090,000.00 USD | 3,090,000.00 USD | 87,620.00 USD | 28,170.00 USD | 107,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 5,560.00 USD | 6,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 3,530,000.00 USD | 3,530,000.00 USD | 72,510.00 USD | 84,620.00 USD | 281,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 3,900,000.00 USD | 3,900,000.00 USD | 35,540.00 USD | 211,200.00 USD | 124,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 4,020,000.00 USD | 4,020,000.00 USD | 57,390.00 USD | 25,750.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 4,390,000.00 USD | 4,390,000.00 USD | 242,240.00 USD | 31,850.00 USD | 94,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 5,200,000.00 USD | 5,200,000.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 5,900,000.00 USD | 5,900,000.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 6,860,000.00 USD | 6,860,000.00 USD | 505,530.00 USD | 177,660.00 USD | 284,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 8,260,000.00 USD | 8,260,000.00 USD | 753,960.00 USD | 187,890.00 USD | 457,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 8,520,000.00 USD | 8,520,000.00 USD | 136,470.00 USD | 43,460.00 USD | 81,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 8,950,000.00 USD | 8,950,000.00 USD | 193,160.00 USD | 96,800.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 2,580.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,310,000.00 USD | 9,310,000.00 USD | 213,030.00 USD | 58,850.00 USD | 87,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 9,790,000.00 USD | 9,790,000.00 USD | 245,390.00 USD | 75,430.00 USD | 162,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 9,840,000.00 USD | 9,840,000.00 USD | 32,020.00 USD | 9,330.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2160` | 10,020,000.00 USD | 10,020,000.00 USD | 97,520.00 USD | 33,680.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 10,170,000.00 USD | 10,170,000.00 USD | 60,130.00 USD | 17,300.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2180` | 10,360,000.00 USD | 10,360,000.00 USD | 78,970.00 USD | 36,240.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2190` | 10,530,000.00 USD | 10,530,000.00 USD | 85,280.00 USD | 39,700.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2195` | 252.21 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2200` | 10,680,000.00 USD | 10,680,000.00 USD | 82,050.00 USD | 24,600.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 10,770,000.00 USD | 10,770,000.00 USD | 35,870.00 USD | 19,900.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 11,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 10,880,000.00 USD | 10,880,000.00 USD | 73,390.00 USD | 8,880.00 USD | 36,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 10,930,000.00 USD | 10,930,000.00 USD | 22,600.00 USD | 8,440.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 11,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2240` | 11,000,000.00 USD | 11,000,000.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0405` | 2,270,000.00 USD | 0.00 USD | 1,020.00 USD | `-78.92%` | `25,182.00` |
| `Live` | `Long` | `0.0515` | 2,270,000.00 USD | 0.00 USD | 463.50 USD | `-73.20%` | `9,000.00` |
| `Live` | `Long` | `0.0545` | 2,270,000.00 USD | 0.00 USD | 1,300.00 USD | `-71.64%` | `23,814.00` |
| `Live` | `Long` | `0.0565` | 2,270,000.00 USD | 0.00 USD | 423.75 USD | `-70.60%` | `7,500.00` |
| `Live` | `Long` | `0.0585` | 2,270,000.00 USD | 0.00 USD | 1,170.00 USD | `-69.56%` | `20,000.00` |
| `Live` | `Long` | `0.0605` | 2,270,000.00 USD | 0.00 USD | 208.30 USD | `-68.51%` | `3,443.00` |
| `Live` | `Long` | `0.0655` | 2,270,000.00 USD | 0.00 USD | 9,170.00 USD | `-65.91%` | `140,000.00` |
| `Live` | `Long` | `0.0685` | 2,260,000.00 USD | 0.00 USD | 3,320.00 USD | `-64.35%` | `48,444.00` |
| `Live` | `Long` | `0.0695` | 2,250,000.00 USD | 0.00 USD | 7,300.00 USD | `-63.83%` | `105,008.00` |
| `Live` | `Long` | `0.0815` | 2,250,000.00 USD | 0.00 USD | 284.84 USD | `-57.59%` | `3,495.00` |
| `Live` | `Long` | `0.0835` | 2,250,000.00 USD | 0.00 USD | 156,450.00 USD | `-56.54%` | `1,873,703.00` |
| `Live` | `Long` | `0.0865` | 2,090,000.00 USD | 0.00 USD | 102.50 USD | `-54.98%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,090,000.00 USD | 0.00 USD | 1,710.00 USD | `-54.46%` | `19,568.00` |
| `Live` | `Long` | `0.0885` | 2,090,000.00 USD | 0.00 USD | 1,150.00 USD | `-53.94%` | `13,050.00` |
| `Live` | `Long` | `0.0905` | 2,090,000.00 USD | 0.00 USD | 157.83 USD | `-52.90%` | `1,744.00` |
| `Live` | `Long` | `0.0925` | 2,090,000.00 USD | 0.00 USD | 1,090.00 USD | `-51.86%` | `11,785.00` |
| `Live` | `Long` | `0.0955` | 2,090,000.00 USD | 0.00 USD | 331.00 USD | `-50.30%` | `3,466.00` |
| `Live` | `Long` | `0.1005` | 2,090,000.00 USD | 0.00 USD | 2,780.00 USD | `-47.70%` | `27,674.00` |
| `Live` | `Long` | `0.1025` | 2,080,000.00 USD | 0.00 USD | 5,800.00 USD | `-46.66%` | `56,584.00` |
| `Live` | `Long` | `0.1035` | 2,080,000.00 USD | 0.00 USD | 1,050.00 USD | `-46.14%` | `10,149.00` |
| `Live` | `Long` | `0.1045` | 2,080,000.00 USD | 0.00 USD | 107.74 USD | `-45.62%` | `1,031.00` |
| `Live` | `Long` | `0.1065` | 2,080,000.00 USD | 0.00 USD | 793.42 USD | `-44.57%` | `7,450.00` |
| `Live` | `Long` | `0.1075` | 2,070,000.00 USD | 0.00 USD | 454.62 USD | `-44.05%` | `4,229.00` |
| `Live` | `Long` | `0.1085` | 2,070,000.00 USD | 0.00 USD | 526.77 USD | `-43.53%` | `4,855.00` |
| `Live` | `Long` | `0.1095` | 2,070,000.00 USD | 0.00 USD | 1,490.00 USD | `-43.01%` | `13,608.00` |
| `Live` | `Long` | `0.1105` | 2,070,000.00 USD | 0.00 USD | 25,410.00 USD | `-42.49%` | `229,972.00` |
| `Live` | `Long` | `0.1115` | 2,050,000.00 USD | 0.00 USD | 1,670.00 USD | `-41.97%` | `15,000.00` |
| `Live` | `Long` | `0.1145` | 2,050,000.00 USD | 0.00 USD | 5,380.00 USD | `-40.41%` | `46,944.00` |
| `Live` | `Long` | `0.1165` | 2,040,000.00 USD | 0.00 USD | 13,360.00 USD | `-39.37%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,030,000.00 USD | 0.00 USD | 931.42 USD | `-38.85%` | `7,927.00` |
| `Live` | `Long` | `0.1205` | 2,030,000.00 USD | 0.00 USD | 826.27 USD | `-37.29%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,020,000.00 USD | 0.00 USD | 1,200.00 USD | `-36.77%` | `9,909.00` |
| `Live` | `Long` | `0.1225` | 2,020,000.00 USD | 0.00 USD | 388.08 USD | `-36.25%` | `3,168.00` |
| `Live` | `Long` | `0.1245` | 2,020,000.00 USD | 0.00 USD | 404.62 USD | `-35.21%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,020,000.00 USD | 0.00 USD | 1,980.00 USD | `-34.69%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,020,000.00 USD | 0.00 USD | 314.61 USD | `-34.17%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,020,000.00 USD | 0.00 USD | 2,570.00 USD | `-33.65%` | `20,182.00` |
| `Live` | `Long` | `0.1295` | 2,020,000.00 USD | 0.00 USD | 2,540.00 USD | `-32.60%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,020,000.00 USD | 0.00 USD | 290.36 USD | `-32.08%` | `2,225.00` |
| `Live` | `Long` | `0.1315` | 2,020,000.00 USD | 0.00 USD | 687.35 USD | `-31.56%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,010,000.00 USD | 0.00 USD | 6,960.00 USD | `-31.04%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,010,000.00 USD | 0.00 USD | 3,600.00 USD | `-30.52%` | `26,965.00` |
| `Live` | `Long` | `0.1345` | 2,000,000.00 USD | 0.00 USD | 2,120.00 USD | `-30.00%` | `15,737.00` |
| `Live` | `Long` | `0.1355` | 2,000,000.00 USD | 0.00 USD | 58,000.00 USD | `-29.48%` | `428,047.00` |
| `Live` | `Long` | `0.1385` | 1,940,000.00 USD | 0.00 USD | 1,410.00 USD | `-27.92%` | `10,199.00` |
| `Live` | `Long` | `0.1405` | 1,940,000.00 USD | 0.00 USD | 565.51 USD | `-26.88%` | `4,025.00` |
| `Live` | `Long` | `0.1415` | 1,940,000.00 USD | 0.00 USD | 9,740.00 USD | `-26.36%` | `68,863.00` |
| `Live` | `Long` | `0.1425` | 1,930,000.00 USD | 0.00 USD | 902.88 USD | `-25.84%` | `6,336.00` |
| `Live` | `Long` | `0.1435` | 1,930,000.00 USD | 0.00 USD | 16,640.00 USD | `-25.32%` | `115,977.00` |
| `Live` | `Long` | `0.1445` | 1,910,000.00 USD | 0.00 USD | 1,890.00 USD | `-24.80%` | `13,058.00` |
| `Live` | `Long` | `0.1455` | 1,910,000.00 USD | 0.00 USD | 3,770.00 USD | `-24.28%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 1,910,000.00 USD | 0.00 USD | 4,580.00 USD | `-23.76%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 1,900,000.00 USD | 0.00 USD | 882.93 USD | `-23.24%` | `5,986.00` |
| `Live` | `Long` | `0.1485` | 1,900,000.00 USD | 0.00 USD | 7,640.00 USD | `-22.72%` | `51,475.00` |
| `Live` | `Long` | `0.1495` | 1,900,000.00 USD | 0.00 USD | 138.14 USD | `-22.20%` | `924.00` |
| `Live` | `Long` | `0.1505` | 1,900,000.00 USD | 0.00 USD | 2,640.00 USD | `-21.68%` | `17,551.00` |
| `Live` | `Long` | `0.1515` | 1,890,000.00 USD | 0.00 USD | 33,400.00 USD | `-21.16%` | `220,430.00` |
| `Live` | `Long` | `0.1525` | 1,860,000.00 USD | 0.00 USD | 981.95 USD | `-20.63%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 1,860,000.00 USD | 0.00 USD | 74,520.00 USD | `-20.11%` | `485,495.00` |
| `Live` | `Long` | `0.1545` | 1,780,000.00 USD | 0.00 USD | 721.05 USD | `-19.59%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,780,000.00 USD | 0.00 USD | 1,940.00 USD | `-19.07%` | `12,464.00` |
| `Live` | `Long` | `0.1565` | 1,780,000.00 USD | 0.00 USD | 12,820.00 USD | `-18.55%` | `81,894.00` |
| `Live` | `Long` | `0.1575` | 1,770,000.00 USD | 0.00 USD | 216.56 USD | `-18.03%` | `1,375.00` |
| `Live` | `Long` | `0.1585` | 1,770,000.00 USD | 0.00 USD | 6,000.00 USD | `-17.51%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,760,000.00 USD | 0.00 USD | 538,940.00 USD | `-16.99%` | `3,378,951.00` |
| `Live` | `Long` | `0.1605` | 1,220,000.00 USD | 0.00 USD | 60,230.00 USD | `-16.47%` | `375,279.00` |
| `Live` | `Long` | `0.1615` | 1,160,000.00 USD | 0.00 USD | 5,740.00 USD | `-15.95%` | `35,537.00` |
| `Live` | `Long` | `0.1625` | 1,160,000.00 USD | 0.00 USD | 2,350.00 USD | `-15.43%` | `14,453.00` |
| `Live` | `Long` | `0.1645` | 1,160,000.00 USD | 0.00 USD | 10,540.00 USD | `-14.39%` | `64,095.00` |
| `Live` | `Long` | `0.1655` | 1,140,000.00 USD | 0.00 USD | 241.46 USD | `-13.87%` | `1,459.00` |
| `Live` | `Long` | `0.1665` | 1,140,000.00 USD | 0.00 USD | 1,120.00 USD | `-13.35%` | `6,700.00` |
| `Live` | `Long` | `0.1675` | 1,140,000.00 USD | 0.00 USD | 1,690.00 USD | `-12.83%` | `10,103.00` |
| `Live` | `Long` | `0.1685` | 1,140,000.00 USD | 0.00 USD | 13,630.00 USD | `-12.31%` | `80,880.00` |
| `Live` | `Long` | `0.1695` | 1,130,000.00 USD | 0.00 USD | 1,280.00 USD | `-11.79%` | `7,557.00` |
| `Live` | `Long` | `0.1705` | 1,130,000.00 USD | 0.00 USD | 625,360.00 USD | `-11.27%` | `3,667,828.00` |
| `Live` | `Long` | `0.1715` | 501,180.00 USD | 0.00 USD | 252,270.00 USD | `-10.75%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 248,910.00 USD | 0.00 USD | 36,420.00 USD | `-10.23%` | `211,108.00` |
| `Live` | `Long` | `0.1735` | 212,500.00 USD | 0.00 USD | 2,430.00 USD | `-9.71%` | `14,022.00` |
| `Live` | `Long` | `0.1745` | 210,060.00 USD | 0.00 USD | 1,440.00 USD | `-9.19%` | `8,224.00` |
| `Live` | `Long` | `0.1755` | 208,630.00 USD | 0.00 USD | 61,110.00 USD | `-8.67%` | `348,224.00` |
| `Live` | `Long` | `0.1765` | 147,510.00 USD | 0.00 USD | 4,990.00 USD | `-8.14%` | `28,260.00` |
| `Live` | `Long` | `0.1775` | 142,530.00 USD | 0.00 USD | 15,900.00 USD | `-7.62%` | `89,588.00` |
| `Live` | `Long` | `0.1785` | 126,620.00 USD | 0.00 USD | 2,480.00 USD | `-7.10%` | `13,921.00` |
| `Live` | `Long` | `0.1795` | 124,140.00 USD | 0.00 USD | 873.09 USD | `-6.58%` | `4,864.00` |
| `Live` | `Long` | `0.1805` | 123,270.00 USD | 0.00 USD | 55,280.00 USD | `-6.06%` | `306,255.00` |
| `Live` | `Long` | `0.1815` | 67,990.00 USD | 0.00 USD | 12,340.00 USD | `-5.54%` | `68,003.00` |
| `Live` | `Long` | `0.1825` | 55,640.00 USD | 0.00 USD | 47,090.00 USD | `-5.02%` | `258,047.00` |
| `Live` | `Long` | `0.1835` | 8,550.00 USD | 0.00 USD | 1,630.00 USD | `-4.50%` | `8,867.00` |
| `Live` | `Long` | `0.1845` | 6,920.00 USD | 0.00 USD | 2,740.00 USD | `-3.98%` | `14,832.00` |
| `Live` | `Long` | `0.1865` | 4,190.00 USD | 0.00 USD | 3,740.00 USD | `-2.94%` | `20,031.00` |
| `Live` | `Long` | `0.1875` | 451.69 USD | 0.00 USD | 451.69 USD | `-2.42%` | `2,409.00` |
| `Live` | `Short` | `0.2005` | 254.23 USD | 254.23 USD | 0.00 USD | `+4.35%` | `1,268.00` |
| `Live` | `Short` | `0.2025` | 7,780.00 USD | 7,530.00 USD | 0.00 USD | `+5.39%` | `37,172.00` |
| `Live` | `Short` | `0.2035` | 8,250.00 USD | 465.40 USD | 0.00 USD | `+5.91%` | `2,287.00` |
| `Live` | `Short` | `0.2125` | 10,830.00 USD | 2,580.00 USD | 0.00 USD | `+10.59%` | `12,141.00` |
| `Live` | `Short` | `0.2175` | 14,760.00 USD | 3,930.00 USD | 0.00 USD | `+13.19%` | `18,067.00` |
| `Live` | `Short` | `0.2215` | 16,400.00 USD | 1,640.00 USD | 0.00 USD | `+15.27%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 16,600.00 USD | 200.48 USD | 0.00 USD | `+16.32%` | `897.00` |
| `Live` | `Short` | `0.2275` | 18,760.00 USD | 2,160.00 USD | 0.00 USD | `+18.40%` | `9,500.00` |
| `Live` | `Short` | `0.2285` | 28,000.00 USD | 9,240.00 USD | 0.00 USD | `+18.92%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 28,280.00 USD | 282.02 USD | 0.00 USD | `+21.00%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 35,920.00 USD | 7,640.00 USD | 0.00 USD | `+21.52%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 37,390.00 USD | 1,470.00 USD | 0.00 USD | `+25.16%` | `6,110.00` |
| `Live` | `Short` | `0.2525` | 65,760.00 USD | 28,370.00 USD | 0.00 USD | `+31.41%` | `112,352.00` |
| `Live` | `Short` | `0.2585` | 66,140.00 USD | 380.25 USD | 0.00 USD | `+34.53%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 67,540.00 USD | 1,400.00 USD | 0.00 USD | `+36.09%` | `5,346.00` |
| `Live` | `Short` | `0.2715` | 67,830.00 USD | 298.11 USD | 0.00 USD | `+41.30%` | `1,098.00` |
| `Live` | `Short` | `0.2775` | 68,210.00 USD | 379.62 USD | 0.00 USD | `+44.42%` | `1,368.00` |
| `Live` | `Short` | `0.2825` | 68,640.00 USD | 425.73 USD | 0.00 USD | `+47.02%` | `1,507.00` |
| `Live` | `Short` | `0.2835` | 71,230.00 USD | 2,590.00 USD | 0.00 USD | `+47.54%` | `9,121.00` |
| `Live` | `Short` | `0.2845` | 73,400.00 USD | 2,170.00 USD | 0.00 USD | `+48.06%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 73,810.00 USD | 411.09 USD | 0.00 USD | `+50.66%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 77,070.00 USD | 3,260.00 USD | 0.00 USD | `+51.70%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 77,590.00 USD | 519.79 USD | 0.00 USD | `+52.75%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 85,580.00 USD | 7,990.00 USD | 0.00 USD | `+53.79%` | `27,027.00` |
| `Live` | `Short` | `0.2965` | 128,330.00 USD | 42,750.00 USD | 0.00 USD | `+54.31%` | `144,174.00` |
| `Live` | `Short` | `0.3005` | 128,470.00 USD | 146.34 USD | 0.00 USD | `+56.39%` | `487.00` |
| `Live` | `Short` | `0.3015` | 204,440.00 USD | 75,960.00 USD | 0.00 USD | `+56.91%` | `251,952.00` |
| `Live` | `Short` | `0.3035` | 204,640.00 USD | 204.56 USD | 0.00 USD | `+57.95%` | `674.00` |
| `Live` | `Short` | `0.3055` | 205,050.00 USD | 408.15 USD | 0.00 USD | `+58.99%` | `1,336.00` |
| `Live` | `Short` | `0.3115` | 302,360.00 USD | 97,310.00 USD | 0.00 USD | `+62.11%` | `312,388.00` |
| `Live` | `Short` | `0.3175` | 377,430.00 USD | 75,070.00 USD | 0.00 USD | `+65.24%` | `236,444.00` |
| `Live` | `Short` | `0.3185` | 381,730.00 USD | 4,300.00 USD | 0.00 USD | `+65.76%` | `13,504.00` |
| `Live` | `Short` | `0.3245` | 382,870.00 USD | 1,140.00 USD | 0.00 USD | `+68.88%` | `3,500.00` |
| `Live` | `Short` | `0.3275` | 386,620.00 USD | 3,750.00 USD | 0.00 USD | `+70.44%` | `11,458.00` |
| `Live` | `Short` | `0.3295` | 389,000.00 USD | 2,380.00 USD | 0.00 USD | `+71.48%` | `7,219.00` |
| `Live` | `Short` | `0.3325` | 389,310.00 USD | 315.88 USD | 0.00 USD | `+73.04%` | `950.00` |
| `Live` | `Short` | `0.3385` | 390,310.00 USD | 995.53 USD | 0.00 USD | `+76.16%` | `2,941.00` |
| `Live` | `Short` | `0.3425` | 391,770.00 USD | 1,460.00 USD | 0.00 USD | `+78.25%` | `4,254.00` |
| `Live` | `Short` | `0.3525` | 392,090.00 USD | 322.54 USD | 0.00 USD | `+83.45%` | `915.00` |
| `Live` | `Short` | `0.3555` | 392,230.00 USD | 142.56 USD | 0.00 USD | `+85.01%` | `401.00` |
| `Live` | `Short` | `0.3565` | 392,340.00 USD | 111.58 USD | 0.00 USD | `+85.53%` | `313.00` |
| `Live` | `Short` | `0.3585` | 394,780.00 USD | 2,440.00 USD | 0.00 USD | `+86.57%` | `6,797.00` |
| `Live` | `Short` | `0.3615` | 397,810.00 USD | 3,030.00 USD | 0.00 USD | `+88.13%` | `8,392.00` |
| `Live` | `Short` | `0.3665` | 400,570.00 USD | 2,750.00 USD | 0.00 USD | `+90.74%` | `7,515.00` |
| `Live` | `Short` | `0.3715` | 409,740.00 USD | 9,170.00 USD | 0.00 USD | `+93.34%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 898,300.00 USD | 488,560.00 USD | 0.00 USD | `+94.90%` | `1,304,556.00` |
| `Live` | `Short` | `0.3815` | 898,440.00 USD | 140.39 USD | 0.00 USD | `+98.54%` | `368.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 856,990.00 USD | 0.00 USD | 415.13 USD | `-69.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 856,570.00 USD | 0.00 USD | 438.99 USD | `-68.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 856,140.00 USD | 0.00 USD | 1,100.00 USD | `-42.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 855,030.00 USD | 0.00 USD | 541.33 USD | `-41.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 854,490.00 USD | 0.00 USD | 602,500.00 USD | `-37.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 251,990.00 USD | 0.00 USD | 4,460.00 USD | `-35.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 247,530.00 USD | 0.00 USD | 1,320.00 USD | `-33.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 246,210.00 USD | 0.00 USD | 13,390.00 USD | `-32.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 232,820.00 USD | 0.00 USD | 728.88 USD | `-31.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 232,090.00 USD | 0.00 USD | 4,350.00 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 227,740.00 USD | 0.00 USD | 4,730.00 USD | `-28.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 223,010.00 USD | 0.00 USD | 1,820.00 USD | `-27.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 221,190.00 USD | 0.00 USD | 1,050.00 USD | `-26.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 220,140.00 USD | 0.00 USD | 1,600.00 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 218,530.00 USD | 0.00 USD | 4,580.00 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 213,950.00 USD | 0.00 USD | 303.26 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 213,650.00 USD | 0.00 USD | 1,290.00 USD | `-21.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 212,360.00 USD | 0.00 USD | 279.53 USD | `-20.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 212,080.00 USD | 0.00 USD | 324.30 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 211,760.00 USD | 0.00 USD | 1,480.00 USD | `-19.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 210,280.00 USD | 0.00 USD | 552.21 USD | `-17.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 209,730.00 USD | 0.00 USD | 166.84 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 209,560.00 USD | 0.00 USD | 2,990.00 USD | `-16.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 206,570.00 USD | 0.00 USD | 562.67 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 206,010.00 USD | 0.00 USD | 24,760.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 181,250.00 USD | 0.00 USD | 6,540.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 174,710.00 USD | 0.00 USD | 2,870.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 171,840.00 USD | 0.00 USD | 452.97 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 171,390.00 USD | 0.00 USD | 14,050.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 157,350.00 USD | 0.00 USD | 317.92 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 157,030.00 USD | 0.00 USD | 6,740.00 USD | `-12.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 150,290.00 USD | 0.00 USD | 4,270.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 146,020.00 USD | 0.00 USD | 7,630.00 USD | `-11.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 138,390.00 USD | 0.00 USD | 6,860.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 131,530.00 USD | 0.00 USD | 6,900.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 124,630.00 USD | 0.00 USD | 103.58 USD | `-9.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 124,520.00 USD | 0.00 USD | 7,710.00 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 116,810.00 USD | 0.00 USD | 1,760.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 115,040.00 USD | 0.00 USD | 847.38 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 114,200.00 USD | 0.00 USD | 4,440.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 109,760.00 USD | 0.00 USD | 12,840.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 96,920.00 USD | 0.00 USD | 4,850.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 92,060.00 USD | 0.00 USD | 2,110.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 89,960.00 USD | 0.00 USD | 3,200.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 86,760.00 USD | 0.00 USD | 3,080.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 83,670.00 USD | 0.00 USD | 5,630.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 78,050.00 USD | 0.00 USD | 18,800.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 59,240.00 USD | 0.00 USD | 5,850.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 53,400.00 USD | 0.00 USD | 264.64 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 53,130.00 USD | 0.00 USD | 109.69 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 53,020.00 USD | 0.00 USD | 1,120.00 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 51,900.00 USD | 0.00 USD | 6,240.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 45,660.00 USD | 0.00 USD | 381.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 45,280.00 USD | 0.00 USD | 45,280.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 513.01 USD | 513.01 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 2,990.00 USD | 2,480.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 3,750.00 USD | 761.27 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 4,250.00 USD | 498.33 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 7,800.00 USD | 3,550.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 8,810.00 USD | 1,000.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 9,450.00 USD | 646.71 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 9,650.00 USD | 199.50 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 80,220,000.00 USD | 80,210,000.00 USD | 0.00 USD | `+4.35%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2015` | 80,260,000.00 USD | 46,340.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 80,260,000.00 USD | 101.86 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 80,260,000.00 USD | 752.34 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 80,270,000.00 USD | 2,170.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 162,470,000.00 USD | 82,200,000.00 USD | 0.00 USD | `+6.95%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2065` | 162,470,000.00 USD | 207.74 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 162,470,000.00 USD | 312.70 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 162,470,000.00 USD | 3,320.00 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 162,480,000.00 USD | 8,720.00 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 162,500,000.00 USD | 24,600.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 162,520,000.00 USD | 11,750.00 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 162,520,000.00 USD | 472.39 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 162,520,000.00 USD | 3,400.00 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 162,520,000.00 USD | 965.25 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 162,520,000.00 USD | 1,570.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 162,520,000.00 USD | 219.53 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 162,520,000.00 USD | 109.91 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 162,530,000.00 USD | 6,920.00 USD | 0.00 USD | `+14.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 162,530,000.00 USD | 4,510.00 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 162,540,000.00 USD | 1,650.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 162,540,000.00 USD | 1,690.00 USD | 0.00 USD | `+15.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 162,540,000.00 USD | 501.31 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 162,540,000.00 USD | 114.50 USD | 0.00 USD | `+16.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 162,540,000.00 USD | 339.60 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 162,540,000.00 USD | 109.40 USD | 0.00 USD | `+17.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 162,560,000.00 USD | 21,490.00 USD | 0.00 USD | `+18.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 162,570,000.00 USD | 9,140.00 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 162,580,000.00 USD | 9,180.00 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 162,580,000.00 USD | 662.92 USD | 0.00 USD | `+19.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 162,590,000.00 USD | 9,600.00 USD | 0.00 USD | `+20.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 162,590,000.00 USD | 171.12 USD | 0.00 USD | `+21.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 162,600,000.00 USD | 9,340.00 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 162,600,000.00 USD | 1,010.00 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 162,610,000.00 USD | 9,420.00 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 162,610,000.00 USD | 315.96 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 162,610,000.00 USD | 650.04 USD | 0.00 USD | `+23.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 162,610,000.00 USD | 192.71 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 162,620,000.00 USD | 10,090.00 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 162,620,000.00 USD | 209.72 USD | 0.00 USD | `+25.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 162,620,000.00 USD | 115.92 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 162,620,000.00 USD | 236.19 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 162,630,000.00 USD | 10,930.00 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 162,630,000.00 USD | 288.22 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 162,630,000.00 USD | 491.03 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 162,630,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 162,640,000.00 USD | 9,940.00 USD | 0.00 USD | `+29.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 162,640,000.00 USD | 499.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 162,640,000.00 USD | 1,100.00 USD | 0.00 USD | `+30.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 162,650,000.00 USD | 168.76 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 162,650,000.00 USD | 603.73 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 162,650,000.00 USD | 2,170.00 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 162,650,000.00 USD | 1,570.00 USD | 0.00 USD | `+33.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 162,650,000.00 USD | 1,470.00 USD | 0.00 USD | `+34.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 162,650,000.00 USD | 271.44 USD | 0.00 USD | `+35.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 163,070,000.00 USD | 421,590.00 USD | 0.00 USD | `+35.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 163,070,000.00 USD | 1,180.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 163,070,000.00 USD | 945.98 USD | 0.00 USD | `+38.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 163,080,000.00 USD | 8,890.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 163,100,000.00 USD | 14,860.00 USD | 0.00 USD | `+39.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 163,100,000.00 USD | 1,340.00 USD | 0.00 USD | `+40.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 163,100,000.00 USD | 2,710.00 USD | 0.00 USD | `+41.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 163,120,000.00 USD | 13,870.00 USD | 0.00 USD | `+42.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 163,120,000.00 USD | 5,220.00 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 163,120,000.00 USD | 1,170.00 USD | 0.00 USD | `+44.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 163,120,000.00 USD | 944.99 USD | 0.00 USD | `+45.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 163,120,000.00 USD | 161.87 USD | 0.00 USD | `+47.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 163,120,000.00 USD | 113.68 USD | 0.00 USD | `+47.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 163,130,000.00 USD | 1,370.00 USD | 0.00 USD | `+48.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 163,130,000.00 USD | 1,080.00 USD | 0.00 USD | `+49.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 163,140,000.00 USD | 14,980.00 USD | 0.00 USD | `+51.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 163,140,000.00 USD | 1,230.00 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 163,140,000.00 USD | 1,440.00 USD | 0.00 USD | `+54.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 163,140,000.00 USD | 355.21 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 163,150,000.00 USD | 6,650.00 USD | 0.00 USD | `+56.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 163,170,000.00 USD | 18,980.00 USD | 0.00 USD | `+58.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 163,170,000.00 USD | 4,150.00 USD | 0.00 USD | `+60.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 163,180,000.00 USD | 3,250.00 USD | 0.00 USD | `+63.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 163,180,000.00 USD | 5,090.00 USD | 0.00 USD | `+66.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 163,180,000.00 USD | 493.89 USD | 0.00 USD | `+68.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 163,180,000.00 USD | 181.30 USD | 0.00 USD | `+69.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 163,180,000.00 USD | 1,380.00 USD | 0.00 USD | `+71.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 163,200,000.00 USD | 12,290.00 USD | 0.00 USD | `+73.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 163,200,000.00 USD | 111.06 USD | 0.00 USD | `+73.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 163,200,000.00 USD | 220.61 USD | 0.00 USD | `+77.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 163,200,000.00 USD | 3,850.00 USD | 0.00 USD | `+81.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 163,200,000.00 USD | 188.75 USD | 0.00 USD | `+96.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 163,200,000.00 USD | 909.54 USD | 0.00 USD | `+96.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 163,200,000.00 USD | 121.76 USD | 0.00 USD | `+98.02%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1700` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD |
| `1D` | `0.1710` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 23,820.00 USD | 700.07 USD | 12,980.00 USD |
| `1D` | `0.1720` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 0.00 USD | 321.20 USD | 18,400.00 USD |
| `1D` | `0.1730` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 0.00 USD | 4,280.00 USD | 13,510.00 USD |
| `1D` | `0.1740` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 0.00 USD | 6,690.00 USD | 567.36 USD |
| `1D` | `0.1750` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1760` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD |
| `1D` | `0.1770` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 53,230.00 USD | 18,310.00 USD | 79,670.00 USD |
| `1D` | `0.1780` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 62,120.00 USD | 34,290.00 USD | 67,000.00 USD |
| `1D` | `0.1790` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 75,310.00 USD | 38,160.00 USD | 46,170.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 75,870.00 USD | 26,100.00 USD | 47,570.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 38,430.00 USD | 23,350.00 USD | 44,490.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 139,390.00 USD | 10,510.00 USD | 68,570.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 32,650.00 USD | 22,130.00 USD | 65,060.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 77,630.00 USD | 29,420.00 USD | 52,530.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 127,560.00 USD | 58,700.00 USD | 180,540.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 202,510.00 USD | 3,510.00 USD | 86,740.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 102,920.00 USD | 49,970.00 USD | 140,680.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 223,120.00 USD | 49,550.00 USD | 60,450.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 162,010.00 USD | 110,140.00 USD | 122,090.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 104,350.00 USD | 114,440.00 USD | 42,920.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 805,950.00 USD | 0.00 USD | 805,950.00 USD | 292,920.00 USD | 0.00 USD | 42,690.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `1D` | `0.1920` | 470,340.00 USD | 0.00 USD | 470,340.00 USD | 470,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1930` | 723,270.00 USD | 723,270.00 USD | 0.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 937,470.00 USD | 937,470.00 USD | 0.00 USD | 139,920.00 USD | 0.00 USD | 74,280.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 21,890.00 USD | 20,360.00 USD | 100,190.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 6,090.00 USD | 178,720.00 USD | 67,540.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 30,910.00 USD | 138,480.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 166,770.00 USD | 1,260.00 USD | 75,360.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 50,670.00 USD | 37,620.00 USD | 117,040.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 188,460.00 USD | 13,490.00 USD | 204,800.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 101,890.00 USD | 121,910.00 USD | 286,340.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 87,620.00 USD | 28,170.00 USD | 107,030.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 72,510.00 USD | 84,620.00 USD | 281,720.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 35,540.00 USD | 211,200.00 USD | 124,890.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 57,390.00 USD | 25,750.00 USD | 33,330.00 USD |
| `1D` | `0.2060` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 242,240.00 USD | 31,850.00 USD | 94,760.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 505,530.00 USD | 177,660.00 USD | 284,330.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 753,960.00 USD | 187,890.00 USD | 457,420.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 136,470.00 USD | 43,460.00 USD | 81,370.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 193,160.00 USD | 96,800.00 USD | 139,010.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 213,030.00 USD | 58,850.00 USD | 87,590.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 245,390.00 USD | 75,430.00 USD | 162,270.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 32,020.00 USD | 9,330.00 USD | 5,840.00 USD |
| `7D` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `1D` | `0.2160` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 97,520.00 USD | 33,680.00 USD | 44,240.00 USD |
| `7D` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 60,130.00 USD | 17,300.00 USD | 79,670.00 USD |
| `7D` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 78,970.00 USD | 36,240.00 USD | 67,000.00 USD |
| `7D` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 0.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 85,280.00 USD | 39,700.00 USD | 46,170.00 USD |
| `7D` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `1D` | `0.2200` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 82,050.00 USD | 24,600.00 USD | 47,570.00 USD |
| `7D` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 0.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD |
| `1D` | `0.2210` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 35,870.00 USD | 19,900.00 USD | 28,100.00 USD |
| `7D` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `1D` | `0.2220` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 73,390.00 USD | 8,880.00 USD | 36,120.00 USD |
| `7D` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 0.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD |
| `1D` | `0.2230` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 22,600.00 USD | 8,440.00 USD | 19,060.00 USD |
| `7D` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 0.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD |
| `1D` | `0.2240` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD |
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
  * Total Open Interest: `417.40M` | Total OI Tokens: `2,154,730,815.7 ADA`
  * 1h OI Change: `-0.09%` | 4h OI Change: `-7.55%` | 24h OI Change: `-10.06%`
  * Exchange Breakdown: Binance=`76.88M` | Bybit=`50.53M` | OKX=`29.69M` | Hyperliquid=`28.23M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-398.09` | Last 24h: `14.20K` | Last 3d: `57.34K` | Last 7d: `58.14K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0075%` | **USDT OKX** | `-0.0042%` |
| **USDT Bybit** | `-0.0091%` | **USDT KuCoin** | `0.0024%` |
| **USDT MEXC** | `0.0075%` | **USDT BingX** | `0.0084%` |
| **USDT Gate** | `-0.0045%` | **USDT Bitget** | `0.0012%` |
| **CoinM Binance** | `-0.0022%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `47.25%` | `52.75%` | `0.90` | 81,570,000.00 USD |
| `15M` | `Binance` | `50.94%` | `49.06%` | `1.04` | 41,580,000.00 USD |
| `15M` | `OKX` | `48.12%` | `51.88%` | `0.93` | 5,560,000.00 USD |
| `15M` | `Bybit` | `42.95%` | `57.05%` | `0.75` | 14,570,000.00 USD |
| `15M` | `KuCoin` | `45.37%` | `54.63%` | `0.83` | 269,420.00 USD |
| `15M` | `Gate` | `51.36%` | `48.64%` | `1.06` | 1,920,000.00 USD |
| `15M` | `Bitget` | `45.02%` | `54.98%` | `0.82` | 1,220,000.00 USD |
| `15M` | `BingX` | `50.47%` | `49.53%` | `1.02` | 926,930.00 USD |
| `15M` | `MEXC` | `26.68%` | `73.32%` | `0.36` | 1,910,000.00 USD |
| `15M` | `Bitunix` | `49.72%` | `50.28%` | `0.99` | 1,520,000.00 USD |
| `15M` | `Hyperliquid` | `37.87%` | `62.13%` | `0.61` | 9,140,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.12%` | `46.88%` | `1.13` | 198,890.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `3.74%` | `96.26%` | `0.04` | 103,120.00 USD |
| `15M` | `HTX` | `51.59%` | `48.41%` | `1.07` | 37,560.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `78.64%` | `21.36%` | `3.68` | 1,040,000.00 USD |
| `15M` | `Aster` | `39.76%` | `60.24%` | `0.66` | 1,230,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `40.08%` | `59.92%` | `0.67` | 337,580.00 USD |
| `15M` | `Whale Positions` | `50.94%` | `49.06%` | `1.04` | 41,580,000.00 USD |
| `15M` | `Global Accounts` | `47.25%` | `52.75%` | `0.90` | 81,570,000.00 USD |
| `1H` | `ADA` | `51.24%` | `48.76%` | `1.05` | 745,280,000.00 USD |
| `1H` | `Binance` | `51.1%` | `48.9%` | `1.04` | 395,430,000.00 USD |
| `1H` | `OKX` | `56.44%` | `43.56%` | `1.30` | 43,340,000.00 USD |
| `1H` | `Bybit` | `48.49%` | `51.51%` | `0.94` | 97,560,000.00 USD |
| `1H` | `KuCoin` | `46.52%` | `53.48%` | `0.87` | 2,920,000.00 USD |
| `1H` | `Gate` | `49.57%` | `50.43%` | `0.98` | 19,690,000.00 USD |
| `1H` | `Bitget` | `51.79%` | `48.21%` | `1.07` | 16,430,000.00 USD |
| `1H` | `BingX` | `55.87%` | `44.13%` | `1.27` | 6,730,000.00 USD |
| `1H` | `MEXC` | `47.11%` | `52.89%` | `0.89` | 10,320,000.00 USD |
| `1H` | `Bitunix` | `48.2%` | `51.8%` | `0.93` | 16,690,000.00 USD |
| `1H` | `Hyperliquid` | `53.35%` | `46.65%` | `1.14` | 101,070,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.43%` | `50.57%` | `0.98` | 4,110,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `11.95%` | `88.05%` | `0.14` | 884,020.00 USD |
| `1H` | `HTX` | `34.4%` | `65.6%` | `0.52` | 1,020,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `57.59%` | `42.41%` | `1.36` | 4,670,000.00 USD |
| `1H` | `Aster` | `54.07%` | `45.93%` | `1.18` | 17,090,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.61%` | `53.39%` | `0.87` | 7,360,000.00 USD |
| `1H` | `Whale Positions` | `51.1%` | `48.9%` | `1.04` | 395,430,000.00 USD |
| `1H` | `Global Accounts` | `51.24%` | `48.76%` | `1.05` | 745,280,000.00 USD |
| `4H` | `ADA` | `46.43%` | `53.57%` | `0.87` | 612,940,000.00 USD |
| `4H` | `Binance` | `45.69%` | `54.31%` | `0.84` | 260,910,000.00 USD |
| `4H` | `OKX` | `47.85%` | `52.15%` | `0.92` | 133,990,000.00 USD |
| `4H` | `Bybit` | `44.83%` | `55.17%` | `0.81` | 60,070,000.00 USD |
| `4H` | `KuCoin` | `43.8%` | `56.2%` | `0.78` | 5,070,000.00 USD |
| `4H` | `Gate` | `48.84%` | `51.16%` | `0.95` | 47,880,000.00 USD |
| `4H` | `Bitget` | `37.78%` | `62.22%` | `0.61` | 16,990,000.00 USD |
| `4H` | `BingX` | `52.11%` | `47.89%` | `1.09` | 7,160,000.00 USD |
| `4H` | `MEXC` | `53.81%` | `46.19%` | `1.16` | 29,880,000.00 USD |
| `4H` | `Bitunix` | `44.78%` | `55.22%` | `0.81` | 18,110,000.00 USD |
| `4H` | `Hyperliquid` | `49.32%` | `50.68%` | `0.97` | 6,160,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.64%` | `44.36%` | `1.25` | 2,600,000.00 USD |
| `4H` | `Crypto.com` | `50.47%` | `49.53%` | `1.02` | 826,070.00 USD |
| `4H` | `WhiteBIT` | `31.04%` | `68.96%` | `0.45` | 7,640,000.00 USD |
| `4H` | `HTX` | `44.42%` | `55.58%` | `0.80` | 5,050,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.52%` | `54.48%` | `0.84` | 2,720,000.00 USD |
| `4H` | `Aster` | `45.72%` | `54.28%` | `0.84` | 7,640,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51%` | `49%` | `1.04` | 251,380.00 USD |
| `4H` | `Whale Positions` | `45.69%` | `54.31%` | `0.84` | 260,910,000.00 USD |
| `4H` | `Global Accounts` | `46.43%` | `53.57%` | `0.87` | 612,940,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.2024` | `0.2024` | `0.2024` | `0.2029` | `0.2021` | 784,830.17 USD | 348,021.79 USD | 436,808.38 USD | -88,786.59 USD | `-11.31%` | `0B / 1S` |
| `0:00 UTC` | `0.1996` | `0.1995` | `0.1996` | `0.2024` | `0.1980` | 9,482,489.23 USD | 4,643,460.63 USD | 4,839,028.60 USD | -195,567.97 USD | `-2.06%` | `0B / 8S` |
| `5:00 UTC` | `0.1996` | `0.1997` | `0.1996` | `0.2001` | `0.1991` | 2,005,993.91 USD | 876,806.75 USD | 1,129,187.16 USD | -252,380.41 USD | `-12.58%` | `0B / 0S` |
| `0:00 UTC` | `0.1918` | `0.1942` | `0.1918` | `0.2001` | `0.1905` | 24,025,446.30 USD | 10,254,298.46 USD | 13,771,147.84 USD | -3,516,849.37 USD | `-14.64%` | `1B / 19S` |
| `5:00 UTC` | `0.1906` | `0.1904` | `0.1906` | `0.1935` | `0.1871` | 26,316,880.25 USD | 11,827,044.75 USD | 14,489,835.50 USD | -2,662,790.75 USD | `-10.12%` | `1B / 5S` |
| `0:00 UTC` | `0.1903` | `0.1914` | `0.1903` | `0.1931` | `0.1898` | 10,338,146.03 USD | 4,991,420.92 USD | 5,346,725.11 USD | -355,304.19 USD | `-3.44%` | `0B / 1S` |
| `5:00 UTC` | `0.1928` | `0.1937` | `0.1928` | `0.1951` | `0.1923` | 6,583,389.18 USD | 3,089,378.61 USD | 3,494,010.58 USD | -404,631.97 USD | `-6.15%` | `0B / 3S` |
| `0:00 UTC` | `0.1946` | `0.1945` | `0.1946` | `0.1953` | `0.1928` | 3,396,141.31 USD | 1,742,542.34 USD | 1,653,598.97 USD | 88,943.37 USD | `+2.62%` | `1B / 4S` |
| `5:00 UTC` | `0.1928` | `0.1929` | `0.1928` | `0.1938` | `0.1920` | 2,581,325.54 USD | 1,266,824.55 USD | 1,314,500.99 USD | -47,676.44 USD | `-1.85%` | `1B / 2S` |
| `0:00 UTC` | `0.1920` | `0.1919` | `0.1920` | `0.1925` | `0.1915` | 805,530.96 USD | 257,468.99 USD | 548,061.97 USD | -290,592.98 USD | `-36.07%` | `0B / 1S` |

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
| `5m` | -160,110.00 USD | 31,600.00 USD | **`DISTRIBUTION`** |
| `15m` | -394,420.00 USD | -99,340.00 USD | **`DISTRIBUTION`** |
| `30m` | -426,090.00 USD | 2,480.00 USD | **`DISTRIBUTION`** |
| `1h` | -274,780.00 USD | -16,810.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,380,000.00 USD | -9,470,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,020,000.00 USD | -10,370,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,290,000.00 USD | -12,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,800,000.00 USD | -8,990,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,610,000.00 USD | -8,840,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,260,000.00 USD | -17,340,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -17,450,000.00 USD | -35,590,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -75,660,000.00 USD | -198,020,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-160.11K` | 15m=`-394.42K` | 1h=`-274.78K` | 24h=`-8.26M`
* Futures Capital Netflows: 5m=`+31.60K` | 15m=`-99.34K` | 1h=`-16.81K` | 24h=`-17.34M`
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
  * Execution Entry: `0.1907` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1848` (Risk Distance: `0.0059` pts)
  * +2.5R Take Profit: `0.2055`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1935` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1994` (Risk Distance: `0.0059` pts)
  * +2.5R Take Profit: `0.1787`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1924`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
