# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:37:20 IST` (`2026-10-30 04:07:20 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1901` | **Live Ask Quote**: `0.1922` | **Mid Price**: `0.1911`
- **Spread Points**: `21.00` | **Spread BPS**: `109.86 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1860` | VWAP Z-Score: `+2.60` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0019` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `54.33` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1917` | Lower -3.00σ Band: `0.1804`
  * Upper +2.51σ Band: `0.1907` | Lower -2.51σ Band: `0.1813`
  * Upper +2.01σ Band: `0.1898` | Lower -2.01σ Band: `0.1822`
  * Upper +2.00σ Band: `0.1898` | Lower -2.00σ Band: `0.1822`
  * Upper +1.28σ Band: `0.1884` | Lower -1.28σ Band: `0.1836`
  * Upper +1.00σ Band: `0.1879` | Lower -1.00σ Band: `0.1841`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1889` | EMA-20=`0.1890` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1922` (Slope: `+0.0000`) | EMA-100=`0.1954`
  * Institutional Anchors: EMA-144=`0.1970` | EMA-200=`0.1984` (Slope: `-0.6699`) | EMA-233=`0.1992`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1925` (Distance: `-0.73%`)
  * Point of Control (POC) = `0.1907` (Distance: `+0.24%`)
  * Value Area Low (VAL) = `0.1859` (Distance: `+2.85%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2065` | Weekly POC=`0.2031` | Weekly VAL=`0.1994`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1919` | Low=`0.1904`
  * New York Session (13:00-21:00 UTC): High=`0.1923` | Low=`0.1900`
  * Initial Balance (First Hour): IB High=`0.1917` | IB Low=`0.1906`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1904` - `0.1919`
  * Optimal Trade Entry (OTE 0.705): `0.1915`
  * Structural Invalidation Anchor (0.786): `0.1927`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1910` | `0.1917` | `0.1908` | `0.1914` | `3,615,895` | 691,846.32 USD | 152,186.74 USD | `+22.00%` | -2,948,247.59 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1914` | `0.1921` | `0.1914` | `0.1920` | `3,631,177` | 696,265.45 USD | -39,646.13 USD | `-5.69%` | -2,987,893.72 USD | `-0.43` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1920` | `0.1925` | `0.1918` | `0.1924` | `3,339,017` | 641,524.10 USD | 43,418.57 USD | `+6.77%` | -2,944,475.14 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1896` | `0.1909` | `0.1894` | `0.1906` | `8,420,854` | 1,602,763.76 USD | 17,600.26 USD | `+1.10%` | -3,250,682.67 USD | `-0.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1906` | `0.1921` | `0.1902` | `0.1920` | `10,286,014` | 1,967,841.08 USD | 175,567.18 USD | `+8.92%` | -3,075,115.49 USD | `+0.19` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1920` | `0.1925` | `0.1918` | `0.1924` | `3,339,017` | 641,524.10 USD | 43,418.57 USD | `+6.77%` | -3,031,696.92 USD | `+0.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1871` | `0.1887` | `0.1849` | `0.1872` | `76,835,251` | 14,376,224.92 USD | 1,578,173.19 USD | `+10.98%` | -3,318,892.36 USD | `+1.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1871` | `0.1899` | `0.1858` | `0.1890` | `34,457,559` | 6,492,300.86 USD | -34,935.20 USD | `-0.54%` | -3,353,827.56 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1891` | `0.1925` | `0.1890` | `0.1924` | `33,866,377` | 6,454,936.09 USD | 322,130.64 USD | `+4.99%` | -3,031,696.92 USD | `+0.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1924` | `384,689,865` | 71,810,896.33 USD | 7,840.38 USD | `+0.01%` | -3,031,696.92 USD | `+0.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | 1,321,924.30 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 3,089,831.02 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1924` | `384,689,865` | 71,810,896.33 USD | 7,840.38 USD | `+0.01%` | -3,031,696.92 USD | `+0.19` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.1911`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `542` | `0x77ee...2902` | `SHORT` | 4,098,507.67 USD | `21,412,192.00` | `0.1911` | `0.1914` | `0.5709` | -7,255.93 USD | `-0.18%` | `10X Cross` |
| `1226` | `0x123d...3bff` | `LONG` | 1,797,231.75 USD | `9,392,870.00` | `0.2912` | `0.1914` | `0.000000` | -938,424.97 USD | `-52.22%` | `10X Cross` |
| `1265` | `0x7737...bf66` | `SHORT` | 1,739,924.76 USD | `9,091,466.00` | `0.2190` | `0.1914` | `2.03` | 251,065.04 USD | `+14.43%` | `10X Cross` |
| `1563` | `0x5f94...4b96` | `SHORT` | 1,371,225.78 USD | `7,162,318.00` | `0.2303` | `0.1914` | `0.7012` | 278,249.42 USD | `+20.29%` | `10X Cross` |
| `1794` | `0x4982...59e6` | `SHORT` | 1,147,932.66 USD | `5,998,812.00` | `0.1891` | `0.1914` | `0.4104` | -13,374.30 USD | `-1.17%` | `10X Cross` |
| `1847` | `0xcac1...26b3` | `LONG` | 1,111,161.82 USD | `5,803,927.00` | `0.2000` | `0.1914` | `0.000000` | -49,653.76 USD | `-4.47%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2049` | 6,649.01 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2049 USD [API] | `2026-10-29 01:00:11` |
| `ANNOUNCEMENT` | `INFO` | `0.2154` | 112.87 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.11K USD at 0.2154 USD [API] | `2026-09-03 14:48:53` |
| `ANNOUNCEMENT` | `INFO` | `0.2154` | 196.66 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.20K USD at 0.2154 USD [API] | `2026-09-03 14:48:53` |
| `ANNOUNCEMENT` | `INFO` | `0.1961` | 493.51 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.49K USD at 0.1961 USD [API] | `2026-08-20 14:01:11` |
| `ANNOUNCEMENT` | `INFO` | `0.2049` | 6,648.65 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2049 USD [API] | `2026-10-29 01:17:48` |
| `ANNOUNCEMENT` | `INFO` | `0.2041` | 8,718.07 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 8.72K USD at 0.2041 USD [API] | `2026-10-29 01:25:22` |
| `ANNOUNCEMENT` | `INFO` | `0.2029` | 8,300.25 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 8.30K USD at 0.2029 USD [API] | `2026-10-29 01:33:52` |
| `ANNOUNCEMENT` | `INFO` | `0.2029` | 6,153.65 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2029 USD [API] | `2026-10-29 01:33:52` |
| `ANNOUNCEMENT` | `INFO` | `0.2030` | 5,005.40 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2030 USD [API] | `2026-10-29 01:33:52` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.67%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.69%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.69%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--4.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0435` | 863.21 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 136.33 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 253.44 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 107.41 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 1,370.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 306.94 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 526.50 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 630.65 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,720.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 1,820.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 412.84 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 4,230.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 11,690.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,820.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 1,400.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 171,440.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 955.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 332.25 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 87,280.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 177.02 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 150.44 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 475.58 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 579.61 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 4,350.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 2,160.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 169.34 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 3,650.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,380.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 5,910.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 7,630.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 403.77 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 314.44 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 42,080.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 958.46 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,220.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 33,880.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 292.94 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 1,360.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 10,580.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,710.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 110,250.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 41,820.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,320.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 10,860.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 713.16 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 3,450.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,720.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 549,760.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 3,210.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 124.26 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,840.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,720.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 12,160.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 78,180.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,180,000.00 USD | 4,180,000.00 USD | 29,110.00 USD | 2,020.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 377,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 4,140,000.00 USD | 4,140,000.00 USD | 10,810.00 USD | 837.36 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 124,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 4,080,000.00 USD | 4,080,000.00 USD | 5,710.00 USD | 7,590.00 USD | 28,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,270.00 USD | 91,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 4,040,000.00 USD | 4,040,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 234.18 USD | 89,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1750` | 4,030,000.00 USD | 4,030,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 18,670.00 USD | 89,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 4,010,000.00 USD | 4,010,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 42,760.00 USD | 71,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,920,000.00 USD | 3,920,000.00 USD | 54,620.00 USD | 20,340.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 28,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,760,000.00 USD | 3,760,000.00 USD | 69,710.00 USD | 35,540.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 26,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,590,000.00 USD | 3,590,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 1,470.00 USD | 22,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 3,420,000.00 USD | 3,420,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 3,050.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 3,270,000.00 USD | 3,270,000.00 USD | 50,420.00 USD | 27,730.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 11,080.00 USD | 17,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 3,150,000.00 USD | 3,150,000.00 USD | 159,050.00 USD | 14,270.00 USD | 72,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 6,780.00 USD | 6,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 2,910,000.00 USD | 2,910,000.00 USD | 72,410.00 USD | 24,810.00 USD | 133,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1840` | 2,670,000.00 USD | 2,670,000.00 USD | 113,190.00 USD | 50,780.00 USD | 145,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1850` | 2,370,000.00 USD | 2,370,000.00 USD | 110,780.00 USD | 66,490.00 USD | 179,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 2,010,000.00 USD | 2,010,000.00 USD | 228,970.00 USD | 8,970.00 USD | 94,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 1,680,000.00 USD | 1,680,000.00 USD | 178,050.00 USD | 55,340.00 USD | 277,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 1,170,000.00 USD | 1,170,000.00 USD | 294,230.00 USD | 92,270.00 USD | 246,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 532,270.00 USD | 532,270.00 USD | 162,010.00 USD | 135,840.00 USD | 154,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 80,250.00 USD | 80,250.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 37,340.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 615,120.00 USD | 615,120.00 USD | 166,380.00 USD | 5,450.00 USD | 81,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 2,570.00 USD | 2,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1950` | 973,990.00 USD | 973,990.00 USD | 96,260.00 USD | 25,730.00 USD | 236,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 755.22 USD | 3,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,530,000.00 USD | 1,530,000.00 USD | 77,200.00 USD | 221,440.00 USD | 253,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 3,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 187.03 USD | 3,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1980` | 2,020,000.00 USD | 2,020,000.00 USD | 179,990.00 USD | 3,990.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 3,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 2,330,000.00 USD | 2,330,000.00 USD | 88,240.00 USD | 40,300.00 USD | 185,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 107.13 USD | 4,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 2,890,000.00 USD | 2,890,000.00 USD | 225,870.00 USD | 37,570.00 USD | 297,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 6,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 3,440,000.00 USD | 3,440,000.00 USD | 112,020.00 USD | 136,420.00 USD | 302,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 2,100.00 USD | 8,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 3,670,000.00 USD | 3,670,000.00 USD | 94,050.00 USD | 29,200.00 USD | 103,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2030` | 4,110,000.00 USD | 4,110,000.00 USD | 76,100.00 USD | 86,660.00 USD | 281,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 4,490,000.00 USD | 4,490,000.00 USD | 43,130.00 USD | 212,450.00 USD | 124,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 4,620,000.00 USD | 4,620,000.00 USD | 62,210.00 USD | 26,520.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 4,990,000.00 USD | 4,990,000.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 5,800,000.00 USD | 5,800,000.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2075` | 2,220.00 USD | 10,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2080` | 6,500,000.00 USD | 6,500,000.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 7,470,000.00 USD | 7,470,000.00 USD | 505,530.00 USD | 178,540.00 USD | 285,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 8,670,000.00 USD | 8,670,000.00 USD | 666,700.00 USD | 153,810.00 USD | 381,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 8,950,000.00 USD | 8,950,000.00 USD | 142,180.00 USD | 46,780.00 USD | 96,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 9,380,000.00 USD | 9,380,000.00 USD | 194,250.00 USD | 98,370.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 2,580.00 USD | 13,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,740,000.00 USD | 9,740,000.00 USD | 210,380.00 USD | 58,850.00 USD | 87,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 10,110,000.00 USD | 10,110,000.00 USD | 196,360.00 USD | 58,130.00 USD | 110,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2145` | 6,020.00 USD | 19,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2150` | 10,150,000.00 USD | 10,150,000.00 USD | 31,260.00 USD | 8,690.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 23,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 2,650.00 USD | 26,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 27,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 27,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 30,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 39,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 47,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,670.00 USD | 49,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 543.62 USD | 49,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 50,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 641.00 USD | 51,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2485` | 1,060.00 USD | 52,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 52,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 1,970.00 USD | 54,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 54,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 55,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 57,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 57,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 61,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 61,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2945` | 3,980.00 USD | 65,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 73,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2965` | 65,420.00 USD | 138,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 139,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 131.85 USD | 139,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 139,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 3,520.00 USD | 143,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 97,510.00 USD | 240,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 37,030.00 USD | 277,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 3,180.00 USD | 280,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 149.07 USD | 281,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3355` | 1,170.00 USD | 282,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 77,250.00 USD | 359,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3415` | 3,000.00 USD | 362,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 245.23 USD | 362,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3455` | 249,020.00 USD | 611,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3465` | 138.95 USD | 611,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 200,530.00 USD | 812,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 1,300.00 USD | 813,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 331.22 USD | 814,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,120.00 USD | 815,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3555` | 325.28 USD | 815,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 106.95 USD | 815,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 4,200.00 USD | 819,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 143.91 USD | 819,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 829,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 26,920.00 USD | 856,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0415` | 2,440,000.00 USD | 0.00 USD | 823.53 USD | `-78.40%` | `19,844.00` |
| `Live` | `Long` | `0.0455` | 2,440,000.00 USD | 0.00 USD | 242.88 USD | `-76.32%` | `5,338.00` |
| `Live` | `Long` | `0.0465` | 2,440,000.00 USD | 0.00 USD | 247.71 USD | `-75.80%` | `5,327.00` |
| `Live` | `Long` | `0.0495` | 2,440,000.00 USD | 0.00 USD | 105.29 USD | `-74.24%` | `2,127.00` |
| `Live` | `Long` | `0.0535` | 2,440,000.00 USD | 0.00 USD | 401.25 USD | `-72.16%` | `7,500.00` |
| `Live` | `Long` | `0.0565` | 2,440,000.00 USD | 0.00 USD | 508.50 USD | `-70.60%` | `9,000.00` |
| `Live` | `Long` | `0.0595` | 2,440,000.00 USD | 0.00 USD | 167.25 USD | `-69.04%` | `2,811.00` |
| `Live` | `Long` | `0.0645` | 2,440,000.00 USD | 0.00 USD | 1,540.00 USD | `-66.43%` | `23,814.00` |
| `Live` | `Long` | `0.0685` | 2,440,000.00 USD | 0.00 USD | 640.00 USD | `-64.35%` | `9,343.00` |
| `Live` | `Long` | `0.0695` | 2,440,000.00 USD | 0.00 USD | 3,370.00 USD | `-63.83%` | `48,444.00` |
| `Live` | `Long` | `0.0715` | 2,430,000.00 USD | 0.00 USD | 7,510.00 USD | `-62.79%` | `105,008.00` |
| `Live` | `Long` | `0.0755` | 2,430,000.00 USD | 0.00 USD | 259.95 USD | `-60.71%` | `3,443.00` |
| `Live` | `Long` | `0.0815` | 2,430,000.00 USD | 0.00 USD | 284.84 USD | `-57.59%` | `3,495.00` |
| `Live` | `Long` | `0.0845` | 2,430,000.00 USD | 0.00 USD | 159,650.00 USD | `-56.03%` | `1,889,331.00` |
| `Live` | `Long` | `0.0865` | 2,270,000.00 USD | 0.00 USD | 102.50 USD | `-54.99%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,270,000.00 USD | 0.00 USD | 344.75 USD | `-54.47%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,270,000.00 USD | 0.00 USD | 1,150.00 USD | `-53.94%` | `13,050.00` |
| `Live` | `Long` | `0.0915` | 2,260,000.00 USD | 0.00 USD | 12,810.00 USD | `-52.38%` | `140,000.00` |
| `Live` | `Long` | `0.0925` | 2,250,000.00 USD | 0.00 USD | 165.11 USD | `-51.86%` | `1,785.00` |
| `Live` | `Long` | `0.0935` | 2,250,000.00 USD | 0.00 USD | 935.00 USD | `-51.34%` | `10,000.00` |
| `Live` | `Long` | `0.0945` | 2,250,000.00 USD | 0.00 USD | 327.54 USD | `-50.82%` | `3,466.00` |
| `Live` | `Long` | `0.0975` | 2,250,000.00 USD | 0.00 USD | 170.04 USD | `-49.26%` | `1,744.00` |
| `Live` | `Long` | `0.0985` | 2,250,000.00 USD | 0.00 USD | 87,280.00 USD | `-48.74%` | `886,128.00` |
| `Live` | `Long` | `0.1015` | 2,160,000.00 USD | 0.00 USD | 343.58 USD | `-47.18%` | `3,385.00` |
| `Live` | `Long` | `0.1025` | 2,160,000.00 USD | 0.00 USD | 4,100.00 USD | `-46.66%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,160,000.00 USD | 0.00 USD | 1,050.00 USD | `-46.14%` | `10,149.00` |
| `Live` | `Long` | `0.1055` | 2,160,000.00 USD | 0.00 USD | 4,310.00 USD | `-45.10%` | `40,836.00` |
| `Live` | `Long` | `0.1065` | 2,150,000.00 USD | 0.00 USD | 653.70 USD | `-44.58%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,150,000.00 USD | 0.00 USD | 2,630.00 USD | `-44.06%` | `24,424.00` |
| `Live` | `Long` | `0.1095` | 2,150,000.00 USD | 0.00 USD | 1,490.00 USD | `-43.02%` | `13,608.00` |
| `Live` | `Long` | `0.1115` | 2,150,000.00 USD | 0.00 USD | 114.96 USD | `-41.98%` | `1,031.00` |
| `Live` | `Long` | `0.1145` | 2,150,000.00 USD | 0.00 USD | 1,230.00 USD | `-40.41%` | `10,702.00` |
| `Live` | `Long` | `0.1165` | 2,150,000.00 USD | 0.00 USD | 40,150.00 USD | `-39.37%` | `344,662.00` |
| `Live` | `Long` | `0.1175` | 2,110,000.00 USD | 0.00 USD | 8,820.00 USD | `-38.85%` | `75,083.00` |
| `Live` | `Long` | `0.1185` | 2,100,000.00 USD | 0.00 USD | 169.34 USD | `-38.33%` | `1,429.00` |
| `Live` | `Long` | `0.1205` | 2,100,000.00 USD | 0.00 USD | 826.27 USD | `-37.29%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,100,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.77%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,100,000.00 USD | 0.00 USD | 1,180.00 USD | `-35.73%` | `9,522.00` |
| `Live` | `Long` | `0.1245` | 2,100,000.00 USD | 0.00 USD | 404.62 USD | `-35.21%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,090,000.00 USD | 0.00 USD | 1,980.00 USD | `-34.69%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-34.17%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,090,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.65%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,090,000.00 USD | 0.00 USD | 2,540.00 USD | `-32.61%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,090,000.00 USD | 0.00 USD | 13,060.00 USD | `-32.09%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,080,000.00 USD | 0.00 USD | 687.35 USD | `-31.57%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,070,000.00 USD | 0.00 USD | 6,960.00 USD | `-31.05%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,070,000.00 USD | 0.00 USD | 5,910.00 USD | `-30.53%` | `44,280.00` |
| `Live` | `Long` | `0.1345` | 2,060,000.00 USD | 0.00 USD | 491.46 USD | `-30.01%` | `3,654.00` |
| `Live` | `Long` | `0.1355` | 2,060,000.00 USD | 0.00 USD | 106.64 USD | `-29.49%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,060,000.00 USD | 0.00 USD | 403.77 USD | `-28.97%` | `2,958.00` |
| `Live` | `Long` | `0.1405` | 2,060,000.00 USD | 0.00 USD | 314.44 USD | `-26.88%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,060,000.00 USD | 0.00 USD | 9,540.00 USD | `-26.36%` | `67,399.00` |
| `Live` | `Long` | `0.1425` | 2,050,000.00 USD | 0.00 USD | 1,060.00 USD | `-25.84%` | `7,443.00` |
| `Live` | `Long` | `0.1435` | 2,050,000.00 USD | 0.00 USD | 15,780.00 USD | `-25.32%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,030,000.00 USD | 0.00 USD | 2,220.00 USD | `-24.80%` | `15,394.00` |
| `Live` | `Long` | `0.1455` | 2,030,000.00 USD | 0.00 USD | 7,330.00 USD | `-24.28%` | `50,393.00` |
| `Live` | `Long` | `0.1465` | 2,020,000.00 USD | 0.00 USD | 37,670.00 USD | `-23.76%` | `257,143.00` |
| `Live` | `Long` | `0.1475` | 1,990,000.00 USD | 0.00 USD | 292.94 USD | `-23.24%` | `1,986.00` |
| `Live` | `Long` | `0.1485` | 1,990,000.00 USD | 0.00 USD | 1,360.00 USD | `-22.72%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 1,990,000.00 USD | 0.00 USD | 427.12 USD | `-22.20%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 1,990,000.00 USD | 0.00 USD | 3,000.00 USD | `-21.68%` | `19,912.00` |
| `Live` | `Long` | `0.1515` | 1,980,000.00 USD | 0.00 USD | 35,710.00 USD | `-21.16%` | `235,729.00` |
| `Live` | `Long` | `0.1525` | 1,950,000.00 USD | 0.00 USD | 981.95 USD | `-20.64%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 1,950,000.00 USD | 0.00 USD | 42,360.00 USD | `-20.12%` | `275,955.00` |
| `Live` | `Long` | `0.1545` | 1,900,000.00 USD | 0.00 USD | 721.05 USD | `-19.60%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,900,000.00 USD | 0.00 USD | 1,940.00 USD | `-19.08%` | `12,478.00` |
| `Live` | `Long` | `0.1565` | 1,900,000.00 USD | 0.00 USD | 10,860.00 USD | `-18.56%` | `69,381.00` |
| `Live` | `Long` | `0.1575` | 1,890,000.00 USD | 0.00 USD | 157.50 USD | `-18.04%` | `1,000.00` |
| `Live` | `Long` | `0.1585` | 1,890,000.00 USD | 0.00 USD | 703,320.00 USD | `-17.52%` | `4,437,337.00` |
| `Live` | `Long` | `0.1595` | 1,190,000.00 USD | 0.00 USD | 2,780.00 USD | `-17.00%` | `17,408.00` |
| `Live` | `Long` | `0.1605` | 1,180,000.00 USD | 0.00 USD | 57,720.00 USD | `-16.48%` | `359,655.00` |
| `Live` | `Long` | `0.1615` | 1,130,000.00 USD | 0.00 USD | 4,200.00 USD | `-15.96%` | `26,015.00` |
| `Live` | `Long` | `0.1625` | 1,120,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.44%` | `13,446.00` |
| `Live` | `Long` | `0.1645` | 1,120,000.00 USD | 0.00 USD | 10,840.00 USD | `-14.39%` | `65,896.00` |
| `Live` | `Long` | `0.1665` | 1,110,000.00 USD | 0.00 USD | 1,950.00 USD | `-13.35%` | `11,682.00` |
| `Live` | `Long` | `0.1675` | 1,110,000.00 USD | 0.00 USD | 630.81 USD | `-12.83%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,110,000.00 USD | 0.00 USD | 12,160.00 USD | `-12.31%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,090,000.00 USD | 0.00 USD | 78,180.00 USD | `-11.79%` | `461,249.00` |
| `Live` | `Long` | `0.1705` | 1,020,000.00 USD | 0.00 USD | 626,600.00 USD | `-11.27%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 388,790.00 USD | 0.00 USD | 252,270.00 USD | `-10.75%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 136,510.00 USD | 0.00 USD | 33,550.00 USD | `-10.23%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 102,970.00 USD | 0.00 USD | 1,270.00 USD | `-9.71%` | `7,296.00` |
| `Live` | `Long` | `0.1745` | 101,700.00 USD | 0.00 USD | 234.18 USD | `-9.19%` | `1,342.00` |
| `Live` | `Long` | `0.1755` | 101,460.00 USD | 0.00 USD | 18,510.00 USD | `-8.67%` | `105,458.00` |
| `Live` | `Long` | `0.1765` | 82,960.00 USD | 0.00 USD | 42,760.00 USD | `-8.15%` | `242,276.00` |
| `Live` | `Long` | `0.1775` | 40,200.00 USD | 0.00 USD | 1,360.00 USD | `-7.63%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 38,840.00 USD | 0.00 USD | 4,530.00 USD | `-7.11%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 34,310.00 USD | 0.00 USD | 3,840.00 USD | `-6.59%` | `21,396.00` |
| `Live` | `Long` | `0.1805` | 30,470.00 USD | 0.00 USD | 12,610.00 USD | `-6.07%` | `69,840.00` |
| `Live` | `Long` | `0.1815` | 17,860.00 USD | 0.00 USD | 11,080.00 USD | `-5.55%` | `61,030.00` |
| `Live` | `Long` | `0.1825` | 6,780.00 USD | 0.00 USD | 6,780.00 USD | `-5.03%` | `37,172.00` |
| `Live` | `Short` | `0.1955` | 755.22 USD | 755.22 USD | 0.00 USD | `+1.74%` | `3,863.00` |
| `Live` | `Short` | `0.1965` | 860.15 USD | 104.93 USD | 0.00 USD | `+2.26%` | `534.00` |
| `Live` | `Short` | `0.1975` | 1,050.00 USD | 187.03 USD | 0.00 USD | `+2.78%` | `947.00` |
| `Live` | `Short` | `0.1985` | 1,390.00 USD | 338.64 USD | 0.00 USD | `+3.30%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 1,640.00 USD | 252.97 USD | 0.00 USD | `+3.82%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 4,210.00 USD | 2,570.00 USD | 0.00 USD | `+4.34%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 6,310.00 USD | 2,100.00 USD | 0.00 USD | `+4.86%` | `10,418.00` |
| `Live` | `Short` | `0.2025` | 6,420.00 USD | 105.50 USD | 0.00 USD | `+5.38%` | `521.00` |
| `Live` | `Short` | `0.2075` | 8,630.00 USD | 2,220.00 USD | 0.00 USD | `+7.98%` | `10,683.00` |
| `Live` | `Short` | `0.2145` | 9,060.00 USD | 426.21 USD | 0.00 USD | `+11.63%` | `1,987.00` |
| `Live` | `Short` | `0.2175` | 12,990.00 USD | 3,930.00 USD | 0.00 USD | `+13.19%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 15,640.00 USD | 2,650.00 USD | 0.00 USD | `+13.71%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 16,640.00 USD | 996.75 USD | 0.00 USD | `+15.27%` | `4,500.00` |
| `Live` | `Short` | `0.2235` | 16,840.00 USD | 200.48 USD | 0.00 USD | `+16.31%` | `897.00` |
| `Live` | `Short` | `0.2265` | 19,070.00 USD | 2,230.00 USD | 0.00 USD | `+17.87%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 28,310.00 USD | 9,240.00 USD | 0.00 USD | `+18.91%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 28,590.00 USD | 282.02 USD | 0.00 USD | `+20.99%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 36,230.00 USD | 7,640.00 USD | 0.00 USD | `+21.51%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 37,900.00 USD | 1,670.00 USD | 0.00 USD | `+25.16%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 39,210.00 USD | 1,310.00 USD | 0.00 USD | `+25.68%` | `5,427.00` |
| `Live` | `Short` | `0.2425` | 40,290.00 USD | 1,080.00 USD | 0.00 USD | `+26.20%` | `4,435.00` |
| `Live` | `Short` | `0.2435` | 41,320.00 USD | 1,040.00 USD | 0.00 USD | `+26.72%` | `4,254.00` |
| `Live` | `Short` | `0.2585` | 41,700.00 USD | 380.25 USD | 0.00 USD | `+34.52%` | `1,471.00` |
| `Live` | `Short` | `0.2635` | 43,100.00 USD | 1,390.00 USD | 0.00 USD | `+37.13%` | `5,287.00` |
| `Live` | `Short` | `0.2675` | 45,070.00 USD | 1,970.00 USD | 0.00 USD | `+39.21%` | `7,372.00` |
| `Live` | `Short` | `0.2715` | 45,190.00 USD | 120.00 USD | 0.00 USD | `+41.29%` | `442.00` |
| `Live` | `Short` | `0.2775` | 45,570.00 USD | 379.62 USD | 0.00 USD | `+44.41%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 47,740.00 USD | 2,170.00 USD | 0.00 USD | `+48.05%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 48,150.00 USD | 411.09 USD | 0.00 USD | `+50.66%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 51,420.00 USD | 3,260.00 USD | 0.00 USD | `+51.70%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 51,940.00 USD | 519.79 USD | 0.00 USD | `+52.74%` | `1,771.00` |
| `Live` | `Short` | `0.2945` | 54,500.00 USD | 2,560.00 USD | 0.00 USD | `+53.26%` | `8,697.00` |
| `Live` | `Short` | `0.2955` | 62,480.00 USD | 7,990.00 USD | 0.00 USD | `+53.78%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 63,750.00 USD | 1,260.00 USD | 0.00 USD | `+56.38%` | `4,200.00` |
| `Live` | `Short` | `0.3045` | 67,990.00 USD | 4,240.00 USD | 0.00 USD | `+58.46%` | `13,937.00` |
| `Live` | `Short` | `0.3055` | 68,400.00 USD | 408.15 USD | 0.00 USD | `+58.98%` | `1,336.00` |
| `Live` | `Short` | `0.3075` | 136,240.00 USD | 67,840.00 USD | 0.00 USD | `+60.02%` | `220,630.00` |
| `Live` | `Short` | `0.3115` | 233,440.00 USD | 97,190.00 USD | 0.00 USD | `+62.10%` | `312,021.00` |
| `Live` | `Short` | `0.3145` | 237,040.00 USD | 3,600.00 USD | 0.00 USD | `+63.67%` | `11,458.00` |
| `Live` | `Short` | `0.3225` | 238,170.00 USD | 1,130.00 USD | 0.00 USD | `+67.83%` | `3,500.00` |
| `Live` | `Short` | `0.3235` | 275,050.00 USD | 36,880.00 USD | 0.00 USD | `+68.35%` | `114,011.00` |
| `Live` | `Short` | `0.3275` | 275,360.00 USD | 311.12 USD | 0.00 USD | `+70.43%` | `950.00` |
| `Live` | `Short` | `0.3295` | 277,740.00 USD | 2,380.00 USD | 0.00 USD | `+71.47%` | `7,219.00` |
| `Live` | `Short` | `0.3305` | 278,540.00 USD | 799.81 USD | 0.00 USD | `+71.99%` | `2,420.00` |
| `Live` | `Short` | `0.3335` | 281,470.00 USD | 2,930.00 USD | 0.00 USD | `+73.55%` | `8,785.00` |
| `Live` | `Short` | `0.3425` | 359,630.00 USD | 78,160.00 USD | 0.00 USD | `+78.24%` | `228,215.00` |
| `Live` | `Short` | `0.3455` | 558,440.00 USD | 198,800.00 USD | 0.00 USD | `+79.80%` | `575,408.00` |
| `Live` | `Short` | `0.3465` | 558,680.00 USD | 248.09 USD | 0.00 USD | `+80.32%` | `716.00` |
| `Live` | `Short` | `0.3505` | 559,020.00 USD | 331.22 USD | 0.00 USD | `+82.40%` | `945.00` |
| `Live` | `Short` | `0.3515` | 560,140.00 USD | 1,120.00 USD | 0.00 USD | `+82.92%` | `3,187.00` |
| `Live` | `Short` | `0.3525` | 560,290.00 USD | 157.57 USD | 0.00 USD | `+83.44%` | `447.00` |
| `Live` | `Short` | `0.3545` | 560,440.00 USD | 142.15 USD | 0.00 USD | `+84.48%` | `401.00` |
| `Live` | `Short` | `0.3565` | 560,540.00 USD | 106.95 USD | 0.00 USD | `+85.52%` | `300.00` |
| `Live` | `Short` | `0.3585` | 560,870.00 USD | 328.03 USD | 0.00 USD | `+86.56%` | `915.00` |
| `Live` | `Short` | `0.3615` | 563,810.00 USD | 2,940.00 USD | 0.00 USD | `+88.12%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 825,230.00 USD | 261,420.00 USD | 0.00 USD | `+88.64%` | `721,150.00` |
| `Live` | `Short` | `0.3705` | 826,170.00 USD | 942.18 USD | 0.00 USD | `+92.81%` | `2,543.00` |
| `Live` | `Short` | `0.3715` | 835,340.00 USD | 9,170.00 USD | 0.00 USD | `+93.33%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 838,490.00 USD | 3,140.00 USD | 0.00 USD | `+94.89%` | `8,395.00` |
| `Live` | `Short` | `0.3795` | 862,580.00 USD | 24,090.00 USD | 0.00 USD | `+97.49%` | `63,484.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 148,020,000.00 USD | 0.00 USD | 415.13 USD | `-69.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 148,020,000.00 USD | 0.00 USD | 438.99 USD | `-68.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 148,020,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 148,010,000.00 USD | 0.00 USD | 541.33 USD | `-41.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 148,010,000.00 USD | 0.00 USD | 429.20 USD | `-39.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 148,010,000.00 USD | 0.00 USD | 602,500.00 USD | `-37.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 147,410,000.00 USD | 0.00 USD | 4,460.00 USD | `-35.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 147,410,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 147,410,000.00 USD | 0.00 USD | 13,390.00 USD | `-32.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 147,390,000.00 USD | 0.00 USD | 728.88 USD | `-31.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 147,390,000.00 USD | 0.00 USD | 4,350.00 USD | `-30.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 147,390,000.00 USD | 0.00 USD | 4,730.00 USD | `-28.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 147,380,000.00 USD | 0.00 USD | 1,820.00 USD | `-27.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 147,380,000.00 USD | 0.00 USD | 1,050.00 USD | `-26.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 147,380,000.00 USD | 0.00 USD | 351.26 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 147,380,000.00 USD | 0.00 USD | 1,600.00 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 147,380,000.00 USD | 0.00 USD | 10,400.00 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 147,370,000.00 USD | 0.00 USD | 5,980.00 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 147,360,000.00 USD | 0.00 USD | 303.26 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 147,360,000.00 USD | 0.00 USD | 3,230.00 USD | `-21.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 147,360,000.00 USD | 0.00 USD | 6,380.00 USD | `-20.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 147,350,000.00 USD | 0.00 USD | 126.54 USD | `-19.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 147,350,000.00 USD | 0.00 USD | 1,790.00 USD | `-19.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 147,350,000.00 USD | 0.00 USD | 6,260.00 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 147,340,000.00 USD | 0.00 USD | 552.21 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 147,340,000.00 USD | 0.00 USD | 166.84 USD | `-17.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 147,340,000.00 USD | 0.00 USD | 9,410.00 USD | `-16.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 147,330,000.00 USD | 0.00 USD | 769.39 USD | `-15.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 147,330,000.00 USD | 0.00 USD | 24,760.00 USD | `-15.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 147,310,000.00 USD | 0.00 USD | 6,540.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 147,300,000.00 USD | 0.00 USD | 1,750.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 147,300,000.00 USD | 0.00 USD | 5,670.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 147,290,000.00 USD | 0.00 USD | 7,390.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 147,290,000.00 USD | 0.00 USD | 317.92 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 147,290,000.00 USD | 0.00 USD | 4,270.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 147,280,000.00 USD | 0.00 USD | 1,300.00 USD | `-11.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 147,280,000.00 USD | 0.00 USD | 1,280.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 147,280,000.00 USD | 0.00 USD | 640.67 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 147,280,000.00 USD | 0.00 USD | 349.00 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 147,280,000.00 USD | 0.00 USD | 1,760.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 147,280,000.00 USD | 0.00 USD | 847.38 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 147,270,000.00 USD | 0.00 USD | 4,910.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 147,270,000.00 USD | 0.00 USD | 5,400.00 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 147,260,000.00 USD | 0.00 USD | 18,500.00 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 147,250,000.00 USD | 0.00 USD | 1,570.00 USD | `-6.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 147,240,000.00 USD | 0.00 USD | 2,720.00 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 147,240,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-5.03%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 110,740,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-4.51%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 37,340,000.00 USD | 0.00 USD | 18,800.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 37,320,000.00 USD | 0.00 USD | 3,970.00 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 37,320,000.00 USD | 0.00 USD | 37,300,000.00 USD | `-2.95%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1875` | 16,590.00 USD | 0.00 USD | 3,580.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 13,010.00 USD | 0.00 USD | 3,100.00 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 9,910.00 USD | 0.00 USD | 2,320.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 7,590.00 USD | 0.00 USD | 5,500.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 2,090.00 USD | 0.00 USD | 2,090.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 362.29 USD | 362.29 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 728.77 USD | 366.49 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 1,120.00 USD | 389.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 1,940.00 USD | 819.54 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 5,590.00 USD | 3,660.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 6,600.00 USD | 1,000.00 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 7,240.00 USD | 646.71 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 7,640.00 USD | 399.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 18,180.00 USD | 10,540.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 64,520.00 USD | 46,340.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 65,110.00 USD | 594.34 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 72,320.00 USD | 7,210.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 75,010.00 USD | 2,690.00 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 77,160.00 USD | 2,160.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 77,370.00 USD | 207.74 USD | 0.00 USD | `+7.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 77,680.00 USD | 312.70 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 86,020.00 USD | 8,340.00 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 93,940.00 USD | 7,920.00 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 116,010.00 USD | 22,070.00 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 135,990.00 USD | 19,980.00 USD | 0.00 USD | `+10.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 142,690.00 USD | 6,700.00 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 146,890.00 USD | 4,190.00 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 147,850.00 USD | 965.25 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 158,150.00 USD | 10,300.00 USD | 0.00 USD | `+12.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 158,640.00 USD | 487.34 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 158,750.00 USD | 109.91 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 174,210.00 USD | 15,460.00 USD | 0.00 USD | `+14.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 176,980.00 USD | 2,760.00 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 178,620.00 USD | 1,650.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 187,630.00 USD | 9,010.00 USD | 0.00 USD | `+15.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 191,380.00 USD | 3,750.00 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 191,500.00 USD | 114.50 USD | 0.00 USD | `+16.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 191,840.00 USD | 339.60 USD | 0.00 USD | `+17.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 191,950.00 USD | 109.40 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 201,050.00 USD | 9,100.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 210,190.00 USD | 9,140.00 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 210,850.00 USD | 662.92 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 211,190.00 USD | 337.06 USD | 0.00 USD | `+20.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 211,360.00 USD | 171.12 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 211,460.00 USD | 101.11 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 212,570.00 USD | 1,110.00 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 221,990.00 USD | 9,420.00 USD | 0.00 USD | `+22.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 222,310.00 USD | 315.96 USD | 0.00 USD | `+23.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 223,080.00 USD | 778.76 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 223,280.00 USD | 192.71 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 223,790.00 USD | 514.45 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 224,000.00 USD | 209.72 USD | 0.00 USD | `+25.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 224,120.00 USD | 115.92 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 224,350.00 USD | 236.19 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 225,500.00 USD | 1,150.00 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 225,790.00 USD | 288.22 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 226,280.00 USD | 491.03 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 227,600.00 USD | 1,320.00 USD | 0.00 USD | `+28.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 237,540.00 USD | 9,940.00 USD | 0.00 USD | `+29.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 238,040.00 USD | 499.00 USD | 0.00 USD | `+29.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 239,140.00 USD | 1,100.00 USD | 0.00 USD | `+30.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 239,310.00 USD | 168.76 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 239,910.00 USD | 603.73 USD | 0.00 USD | `+31.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 242,090.00 USD | 2,170.00 USD | 0.00 USD | `+31.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 243,560.00 USD | 1,470.00 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 243,830.00 USD | 271.44 USD | 0.00 USD | `+35.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 664,730.00 USD | 420,910.00 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 665,910.00 USD | 1,180.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 674,810.00 USD | 8,890.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 689,670.00 USD | 14,860.00 USD | 0.00 USD | `+39.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 691,010.00 USD | 1,340.00 USD | 0.00 USD | `+40.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 693,720.00 USD | 2,710.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 707,590.00 USD | 13,870.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 712,800.00 USD | 5,220.00 USD | 0.00 USD | `+42.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 713,980.00 USD | 1,170.00 USD | 0.00 USD | `+44.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 718,130.00 USD | 4,150.00 USD | 0.00 USD | `+44.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 719,080.00 USD | 944.99 USD | 0.00 USD | `+45.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 719,270.00 USD | 198.73 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 720,650.00 USD | 1,370.00 USD | 0.00 USD | `+48.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 721,730.00 USD | 1,080.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 736,710.00 USD | 14,980.00 USD | 0.00 USD | `+51.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 737,940.00 USD | 1,230.00 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 739,390.00 USD | 1,440.00 USD | 0.00 USD | `+54.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 739,740.00 USD | 355.21 USD | 0.00 USD | `+55.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 746,390.00 USD | 6,650.00 USD | 0.00 USD | `+56.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 765,370.00 USD | 18,980.00 USD | 0.00 USD | `+58.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 769,520.00 USD | 4,150.00 USD | 0.00 USD | `+60.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 772,770.00 USD | 3,250.00 USD | 0.00 USD | `+63.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 773,260.00 USD | 493.89 USD | 0.00 USD | `+68.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 773,440.00 USD | 181.30 USD | 0.00 USD | `+69.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 774,830.00 USD | 1,380.00 USD | 0.00 USD | `+71.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 787,120.00 USD | 12,290.00 USD | 0.00 USD | `+73.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 787,230.00 USD | 111.06 USD | 0.00 USD | `+73.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 787,450.00 USD | 220.61 USD | 0.00 USD | `+77.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 790,790.00 USD | 3,340.00 USD | 0.00 USD | `+81.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 790,970.00 USD | 188.75 USD | 0.00 USD | `+96.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 791,880.00 USD | 909.54 USD | 0.00 USD | `+96.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 792,010.00 USD | 121.76 USD | 0.00 USD | `+98.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1710` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 29,110.00 USD | 2,020.00 USD | 16,860.00 USD |
| `1D` | `0.1720` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 10,810.00 USD | 837.36 USD | 45,740.00 USD |
| `1D` | `0.1730` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 5,710.00 USD | 7,590.00 USD | 28,880.00 USD |
| `1D` | `0.1740` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD |
| `1D` | `0.1750` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1760` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD |
| `1D` | `0.1770` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 54,620.00 USD | 20,340.00 USD | 79,670.00 USD |
| `1D` | `0.1780` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 69,710.00 USD | 35,540.00 USD | 67,000.00 USD |
| `1D` | `0.1790` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 50,420.00 USD | 27,730.00 USD | 44,490.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 159,050.00 USD | 14,270.00 USD | 72,260.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 72,410.00 USD | 24,810.00 USD | 133,410.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 113,190.00 USD | 50,780.00 USD | 145,530.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 110,780.00 USD | 66,490.00 USD | 179,880.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 228,970.00 USD | 8,970.00 USD | 94,110.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 178,050.00 USD | 55,340.00 USD | 277,370.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 294,230.00 USD | 92,270.00 USD | 246,440.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 532,270.00 USD | 0.00 USD | 532,270.00 USD | 162,010.00 USD | 135,840.00 USD | 154,170.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 80,250.00 USD | 0.00 USD | 80,250.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 37,340.00 USD | 0.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `1D` | `0.1920` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 615,120.00 USD | 615,120.00 USD | 0.00 USD | 166,380.00 USD | 5,450.00 USD | 81,660.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 973,990.00 USD | 973,990.00 USD | 0.00 USD | 96,260.00 USD | 25,730.00 USD | 236,880.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 77,200.00 USD | 221,440.00 USD | 253,530.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 179,990.00 USD | 3,990.00 USD | 79,050.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 88,240.00 USD | 40,300.00 USD | 185,390.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 225,870.00 USD | 37,570.00 USD | 297,800.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 112,020.00 USD | 136,420.00 USD | 302,380.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 94,050.00 USD | 29,200.00 USD | 103,450.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 76,100.00 USD | 86,660.00 USD | 281,720.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 43,130.00 USD | 212,450.00 USD | 124,890.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 62,210.00 USD | 26,520.00 USD | 33,330.00 USD |
| `1D` | `0.2060` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 505,530.00 USD | 178,540.00 USD | 285,710.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 666,700.00 USD | 153,810.00 USD | 381,110.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 142,180.00 USD | 46,780.00 USD | 96,740.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 194,250.00 USD | 98,370.00 USD | 139,010.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 210,380.00 USD | 58,850.00 USD | 87,590.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 196,360.00 USD | 58,130.00 USD | 110,450.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 31,260.00 USD | 8,690.00 USD | 5,840.00 USD |
| `7D` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `7D` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |
| `7D` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `7D` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 0.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD |
| `7D` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `7D` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 0.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD |
| `7D` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `7D` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 0.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD |
| `7D` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 0.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD |
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
  * Total Open Interest: `410.85M` | Total OI Tokens: `2,137,815,630.4 ADA`
  * 1h OI Change: `+0.74%` | 4h OI Change: `-0.91%` | 24h OI Change: `-6.54%`
  * Exchange Breakdown: Binance=`76.24M` | Bybit=`50.91M` | OKX=`28.98M` | Hyperliquid=`28.18M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.26K` | Last 24h: `10.54K` | Last 3d: `50.95K` | Last 7d: `82.09K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0074%` |
| **USDT Bybit** | `-0.0208%` | **USDT KuCoin** | `0.0043%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0019%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `45.54%` | `54.46%` | `0.84` | 102,810,000.00 USD |
| `15M` | `Binance` | `52.26%` | `47.74%` | `1.09` | 35,040,000.00 USD |
| `15M` | `OKX` | `50.55%` | `49.45%` | `1.02` | 18,220,000.00 USD |
| `15M` | `Bybit` | `54.57%` | `45.43%` | `1.20` | 6,650,000.00 USD |
| `15M` | `KuCoin` | `37.36%` | `62.64%` | `0.60` | 493,720.00 USD |
| `15M` | `Gate` | `46.79%` | `53.21%` | `0.88` | 5,510,000.00 USD |
| `15M` | `Bitget` | `40.77%` | `59.23%` | `0.69` | 3,700,000.00 USD |
| `15M` | `BingX` | `38.51%` | `61.49%` | `0.63` | 5,010,000.00 USD |
| `15M` | `MEXC` | `26.86%` | `73.14%` | `0.37` | 12,930,000.00 USD |
| `15M` | `Bitunix` | `33.25%` | `66.75%` | `0.50` | 5,270,000.00 USD |
| `15M` | `Hyperliquid` | `25.92%` | `74.08%` | `0.35` | 5,170,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.56%` | `53.44%` | `0.87` | 907,110.00 USD |
| `15M` | `Crypto.com` | `48.33%` | `51.67%` | `0.94` | 134,480.00 USD |
| `15M` | `WhiteBIT` | `99.99%` | `0.01%` | `9999.00` | 1,050,000.00 USD |
| `15M` | `HTX` | `22.78%` | `77.22%` | `0.30` | 313,710.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `59.56%` | `40.44%` | `1.47` | 1,540,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `43.65%` | `56.35%` | `0.77` | 871,020.00 USD |
| `15M` | `Whale Positions` | `52.26%` | `47.74%` | `1.09` | 35,040,000.00 USD |
| `15M` | `Global Accounts` | `45.54%` | `54.46%` | `0.84` | 102,810,000.00 USD |
| `1H` | `ADA` | `50.33%` | `49.67%` | `1.01` | 113,910,000.00 USD |
| `1H` | `Binance` | `49.88%` | `50.12%` | `1.00` | 69,800,000.00 USD |
| `1H` | `OKX` | `51.48%` | `48.52%` | `1.06` | 12,430,000.00 USD |
| `1H` | `Bybit` | `49.43%` | `50.57%` | `0.98` | 10,200,000.00 USD |
| `1H` | `KuCoin` | `52.13%` | `47.87%` | `1.09` | 672,050.00 USD |
| `1H` | `Gate` | `51.2%` | `48.8%` | `1.05` | 3,120,000.00 USD |
| `1H` | `Bitget` | `41.04%` | `58.96%` | `0.70` | 2,440,000.00 USD |
| `1H` | `BingX` | `42.35%` | `57.65%` | `0.73` | 2,030,000.00 USD |
| `1H` | `MEXC` | `53.47%` | `46.53%` | `1.15` | 1,150,000.00 USD |
| `1H` | `Bitunix` | `52.22%` | `47.78%` | `1.09` | 2,970,000.00 USD |
| `1H` | `Hyperliquid` | `64.06%` | `35.94%` | `1.78` | 4,810,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.83%` | `52.17%` | `0.92` | 444,310.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `22.17%` | `77.83%` | `0.28` | 67,640.00 USD |
| `1H` | `HTX` | `25.9%` | `74.1%` | `0.35` | 650,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `100%` | `0.00` | 3,750.00 USD |
| `1H` | `Aster` | `50.52%` | `49.48%` | `1.02` | 2,180,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.66%` | `45.34%` | `1.21` | 952,470.00 USD |
| `1H` | `Whale Positions` | `49.88%` | `50.12%` | `1.00` | 69,800,000.00 USD |
| `1H` | `Global Accounts` | `50.33%` | `49.67%` | `1.01` | 113,910,000.00 USD |
| `4H` | `ADA` | `47.69%` | `52.31%` | `0.91` | 2,470,000,000.00 USD |
| `4H` | `Binance` | `47.6%` | `52.4%` | `0.91` | 871,100,000.00 USD |
| `4H` | `OKX` | `50.83%` | `49.17%` | `1.03` | 460,070,000.00 USD |
| `4H` | `Bybit` | `49.11%` | `50.89%` | `0.97` | 225,850,000.00 USD |
| `4H` | `KuCoin` | `50.53%` | `49.47%` | `1.02` | 38,660,000.00 USD |
| `4H` | `Gate` | `43.2%` | `56.8%` | `0.76` | 125,850,000.00 USD |
| `4H` | `Bitget` | `48.86%` | `51.14%` | `0.96` | 102,520,000.00 USD |
| `4H` | `BingX` | `40.21%` | `59.79%` | `0.67` | 111,450,000.00 USD |
| `4H` | `MEXC` | `46.61%` | `53.39%` | `0.87` | 197,190,000.00 USD |
| `4H` | `Bitunix` | `46.87%` | `53.13%` | `0.88` | 106,750,000.00 USD |
| `4H` | `Hyperliquid` | `44.22%` | `55.78%` | `0.79` | 123,220,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.37%` | `42.63%` | `1.35` | 26,620,000.00 USD |
| `4H` | `Crypto.com` | `51.66%` | `48.34%` | `1.07` | 5,660,000.00 USD |
| `4H` | `WhiteBIT` | `50.43%` | `49.57%` | `1.02` | 15,640,000.00 USD |
| `4H` | `HTX` | `51.26%` | `48.74%` | `1.05` | 5,110,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `50.85%` | `49.15%` | `1.03` | 10,010,000.00 USD |
| `4H` | `Aster` | `50.32%` | `49.68%` | `1.01` | 19,700,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.79%` | `60.21%` | `0.66` | 25,830,000.00 USD |
| `4H` | `Whale Positions` | `47.6%` | `52.4%` | `0.91` | 871,100,000.00 USD |
| `4H` | `Global Accounts` | `47.69%` | `52.31%` | `0.91` | 2,470,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1866` | `0.1869` | `0.1866` | `0.1876` | `0.1862` | 2,227,884.56 USD | 1,223,520.92 USD | 1,004,363.65 USD | 219,157.27 USD | `+9.84%` | `1B / 1S` |
| `0:00 UTC` | `0.1874` | `0.1870` | `0.1874` | `0.1881` | `0.1859` | 2,036,163.82 USD | 1,133,163.53 USD | 903,000.29 USD | 230,163.23 USD | `+11.30%` | `3B / 0S` |
| `5:00 UTC` | `0.1888` | `0.1889` | `0.1888` | `0.1898` | `0.1880` | 1,960,271.66 USD | 990,186.27 USD | 970,085.39 USD | 20,100.88 USD | `+1.03%` | `3B / 0S` |
| `0:00 UTC` | `0.1899` | `0.1895` | `0.1899` | `0.1900` | `0.1890` | 1,399,205.02 USD | 619,891.71 USD | 779,313.31 USD | -159,421.60 USD | `-11.39%` | `1B / 1S` |
| `5:00 UTC` | `0.1890` | `0.1890` | `0.1890` | `0.1898` | `0.1885` | 1,096,660.36 USD | 485,441.32 USD | 611,219.04 USD | -125,777.71 USD | `-11.47%` | `0B / 2S` |
| `0:00 UTC` | `0.1900` | `0.1898` | `0.1900` | `0.1901` | `0.1890` | 2,242,807.14 USD | 1,164,175.89 USD | 1,078,631.26 USD | 85,544.63 USD | `+3.81%` | `1B / 2S` |
| `5:00 UTC` | `0.1906` | `0.1904` | `0.1906` | `0.1910` | `0.1895` | 1,602,763.76 USD | 810,182.01 USD | 792,581.75 USD | 17,600.26 USD | `+1.10%` | `0B / 0S` |
| `0:00 UTC` | `0.1918` | `0.1914` | `0.1918` | `0.1921` | `0.1903` | 1,967,841.08 USD | 1,071,704.13 USD | 896,136.95 USD | 175,567.18 USD | `+8.92%` | `5B / 1S` |
| `5:00 UTC` | `0.1923` | `0.1922` | `0.1923` | `0.1925` | `0.1918` | 1,542,150.19 USD | 773,488.73 USD | 768,661.46 USD | 4,827.26 USD | `+0.31%` | `0B / 0S` |
| `0:00 UTC` | `0.1923` | `0.1922` | `0.1923` | `0.1923` | `0.1921` | 16,893.06 USD | 8,450.84 USD | 8,442.22 USD | 8.62 USD | `+0.05%` | `0B / 0S` |

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
| `5m` | -117,890.00 USD | -3,470.00 USD | **`DISTRIBUTION`** |
| `15m` | -218,830.00 USD | 156,660.00 USD | **`DISTRIBUTION`** |
| `30m` | -162,520.00 USD | 195,940.00 USD | **`ACCUMULATION`** |
| `1h` | -215,160.00 USD | 1,030,000.00 USD | **`ACCUMULATION`** |
| `2h` | 205,200.00 USD | 1,390,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,720,000.00 USD | -1,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,920,000.00 USD | -17,090.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,200,000.00 USD | -10,320,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,360,000.00 USD | -13,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,170,000.00 USD | -6,830,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,840,000.00 USD | -40,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,270,000.00 USD | -198,310,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-117.89K` | 15m=`-218.83K` | 1h=`-215.16K` | 24h=`-8.17M`
* Futures Capital Netflows: 5m=`-3.47K` | 15m=`+156.66K` | 1h=`+1.03M` | 24h=`-6.83M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1859` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1804` (Risk Distance: `0.0055` pts)
  * +2.5R Take Profit: `0.1996`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1925` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1980` (Risk Distance: `0.0055` pts)
  * +2.5R Take Profit: `0.1788`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1927`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
