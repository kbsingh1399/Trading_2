# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 08:39:50 IST` (`2026-10-30 03:09:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1886` | **Live Ask Quote**: `0.1908` | **Mid Price**: `0.1897`
- **Spread Points**: `22.00` | **Spread BPS**: `115.97 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1897` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1910` | Lower -3.00σ Band: `0.1884`
  * Upper +2.51σ Band: `0.1907` | Lower -2.51σ Band: `0.1887`
  * Upper +2.01σ Band: `0.1905` | Lower -2.01σ Band: `0.1889`
  * Upper +2.00σ Band: `0.1905` | Lower -2.00σ Band: `0.1889`
  * Upper +1.28σ Band: `0.1902` | Lower -1.28σ Band: `0.1892`
  * Upper +1.00σ Band: `0.1901` | Lower -1.00σ Band: `0.1893`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1897` | EMA-20=`0.1897` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1897` (Slope: `+0.0000`) | EMA-100=`0.1897`
  * Institutional Anchors: EMA-144=`0.1897` | EMA-200=`0.1897` (Slope: `+0.0000`) | EMA-233=`0.1897`
- **Range Boundaries**: 24H High=`0.1916` | 24H Low=`0.1878` | Weekly High=`0.1935` | Weekly Low=`0.1859`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1925` (Distance: `-1.97%`)
  * Point of Control (POC) = `0.1907` (Distance: `-1.02%`)
  * Value Area Low (VAL) = `0.1857` (Distance: `+1.65%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2063` | Weekly POC=`0.2031` | Weekly VAL=`0.1994`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1905` | Low=`0.1889`
  * New York Session (13:00-21:00 UTC): High=`0.1908` | Low=`0.1886`
  * Initial Balance (First Hour): IB High=`0.1903` | IB Low=`0.1891`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1889` - `0.1905`
  * Optimal Trade Entry (OTE 0.705): `0.1901`
  * Structural Invalidation Anchor (0.786): `0.1912`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1891` | `0.1892` | `0.1887` | `0.1890` | `1,374,710` | 259,771.34 USD | 34,396.80 USD | `+13.24%` | -3,898,548.89 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1891` | `0.1901` | `0.1890` | `0.1895` | `3,103,182` | 588,771.73 USD | 184,343.33 USD | `+31.31%` | -3,714,205.55 USD | `+1.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1895` | `0.1901` | `0.1894` | `0.1901` | `2,787,756` | 528,998.66 USD | 129,642.57 USD | `+24.51%` | -3,584,562.98 USD | `+0.91` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1894` | `0.1899` | `0.1889` | `0.1896` | `7,384,391` | 1,399,205.02 USD | -159,421.60 USD | `-11.39%` | -3,725,102.88 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1897` | `0.1897` | `0.1884` | `0.1890` | `5,803,993` | 1,096,660.36 USD | -125,777.71 USD | `-11.47%` | -3,850,880.59 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1891` | `0.1901` | `0.1890` | `0.1900` | `5,890,477` | 1,117,682.76 USD | 313,924.50 USD | `+28.09%` | -3,536,956.09 USD | `+0.36` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1871` | `0.1887` | `0.1849` | `0.1872` | `76,835,251` | 14,376,224.92 USD | 1,578,173.19 USD | `+10.98%` | -3,318,892.36 USD | `+1.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1871` | `0.1899` | `0.1858` | `0.1890` | `34,457,559` | 6,492,300.86 USD | -34,935.20 USD | `-0.54%` | -3,353,827.56 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1891` | `0.1901` | `0.1890` | `0.1901` | `5,890,938` | 1,117,770.39 USD | 313,985.91 USD | `+28.09%` | -3,039,841.65 USD | `+0.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1910` | `0.1821` | `0.1900` | `356,713,965` | 66,473,643.00 USD | -365.76 USD | `-0.00%` | -3,039,903.06 USD | `+0.18` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | 1,321,924.30 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 3,089,831.02 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1910` | `0.1821` | `0.1900` | `356,713,965` | 66,473,643.00 USD | -365.76 USD | `-0.00%` | -3,039,903.06 USD | `+0.18` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.1897`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:26:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `543` | `0x77ee...2902` | `SHORT` | 4,043,906.58 USD | `21,412,192.00` | `0.1911` | `0.1888` | `0.5706` | 47,345.16 USD | `+1.17%` | `10X Cross` |
| `1229` | `0x123d...3bff` | `LONG` | 1,773,279.93 USD | `9,392,870.00` | `0.2912` | `0.1888` | `0.000000` | -962,376.79 USD | `-54.27%` | `10X Cross` |
| `1260` | `0x7737...bf66` | `SHORT` | 1,718,105.24 USD | `9,091,466.00` | `0.2190` | `0.1888` | `2.00` | 272,884.55 USD | `+15.88%` | `10X Cross` |
| `1560` | `0x5f94...4b96` | `SHORT` | 1,353,391.61 USD | `7,162,318.00` | `0.2303` | `0.1888` | `0.6911` | 296,083.59 USD | `+21.88%` | `10X Cross` |
| `1792` | `0x4982...59e6` | `SHORT` | 1,132,515.72 USD | `5,998,812.00` | `0.1891` | `0.1888` | `0.4186` | 2,042.64 USD | `+0.18%` | `10X Cross` |
| `1842` | `0xcac1...26b3` | `LONG` | 1,095,723.38 USD | `5,803,927.00` | `0.2000` | `0.1888` | `0.000000` | -65,092.21 USD | `-5.94%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2065` | 6,647.05 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2065 USD [API] | `2026-10-28 22:02:11` |
| `ANNOUNCEMENT` | `INFO` | `0.2061` | 11,281.91 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 11.28K USD at 0.2061 USD [API] | `2026-10-28 22:44:33` |
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
  * 24H Horizon: Short MP=`0.2100` (Vol: 191,800.00 USD, Dist: `+9.59%`) | Long MP=`0.1867` (Vol: 71,500.00 USD, Dist: `--2.58%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+9.21%`) | Long MP=`0.1867` (Vol: 71,500.00 USD, Dist: `--2.56%`)
  * 3D Horizon: Short MP=`0.2138` (Vol: 289,900.00 USD, Dist: `+11.61%`) | Long MP=`0.1867` (Vol: 71,500.00 USD, Dist: `--2.56%`)
  * 7D Horizon: Short MP=`0.2130` (Vol: 459,300.00 USD, Dist: `+11.19%`) | Long MP=`0.1868` (Vol: 71,500.00 USD, Dist: `--2.52%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0385` | 323.05 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 883.06 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 294.40 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 544.50 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 338.96 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 1,720.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 1,330.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,720.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 10,710.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 896.09 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 413.16 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 2,040.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 4,340.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 180,430.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 975.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,230.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 150.44 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 475.58 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 380.45 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 5,380.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,640.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 122.17 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 1,180.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,690.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 10,030.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 5,700.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 491.46 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 314.44 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,540.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 958.46 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,220.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 33,880.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 292.94 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 1,360.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 3,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,710.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 5,170.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 186,740.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 1,180.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,320.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 15,260.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,130.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 3,340.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 58,740.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 4,200.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,870.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 552,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,840.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,020.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 12,160.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 78,180.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 627,450.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,180,000.00 USD | 4,180,000.00 USD | 29,110.00 USD | 2,020.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 376,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 4,140,000.00 USD | 4,140,000.00 USD | 10,810.00 USD | 837.36 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 124,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 4,080,000.00 USD | 4,080,000.00 USD | 5,710.00 USD | 7,590.00 USD | 28,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,270.00 USD | 91,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 4,040,000.00 USD | 4,040,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 234.18 USD | 89,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1750` | 4,030,000.00 USD | 4,030,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 19,070.00 USD | 89,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 4,010,000.00 USD | 4,010,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 42,760.00 USD | 70,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,920,000.00 USD | 3,920,000.00 USD | 54,620.00 USD | 20,340.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,230.00 USD | 27,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,760,000.00 USD | 3,760,000.00 USD | 69,710.00 USD | 35,540.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 26,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,590,000.00 USD | 3,590,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 1,120.00 USD | 22,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `0.1950` | 973,990.00 USD | 973,990.00 USD | 96,260.00 USD | 25,730.00 USD | 236,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 425.60 USD | 425.60 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,530,000.00 USD | 1,530,000.00 USD | 77,200.00 USD | 221,440.00 USD | 253,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 530.53 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 2,020,000.00 USD | 2,020,000.00 USD | 179,990.00 USD | 3,990.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 869.18 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 2,330,000.00 USD | 2,330,000.00 USD | 88,240.00 USD | 40,300.00 USD | 185,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 1,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 2,890,000.00 USD | 2,890,000.00 USD | 225,870.00 USD | 37,570.00 USD | 297,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 3,440,000.00 USD | 3,440,000.00 USD | 112,020.00 USD | 136,420.00 USD | 302,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 2,100.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.2075` | 2,220.00 USD | 8,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.2125` | 2,580.00 USD | 10,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,740,000.00 USD | 9,740,000.00 USD | 210,380.00 USD | 58,850.00 USD | 87,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 10,110,000.00 USD | 10,110,000.00 USD | 196,360.00 USD | 58,130.00 USD | 110,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2145` | 6,020.00 USD | 16,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2150` | 10,150,000.00 USD | 10,150,000.00 USD | 31,260.00 USD | 8,690.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 20,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 2,650.00 USD | 23,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 24,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 25,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 27,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 36,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 36,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 44,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 45,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 543.62 USD | 46,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 47,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2485` | 648.83 USD | 48,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 1,480.00 USD | 49,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 1,970.00 USD | 51,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 51,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 52,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 54,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 4,320.00 USD | 58,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 61,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 65,270.00 USD | 127,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 135,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 135,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3035` | 3,480.00 USD | 138,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 131.85 USD | 138,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 139,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 97,510.00 USD | 236,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3145` | 140.58 USD | 236,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3255` | 1,140.00 USD | 238,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3285` | 794.97 USD | 238,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 39,750.00 USD | 278,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 242,530.00 USD | 521,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3375` | 2,960.00 USD | 524,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 382.57 USD | 524,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 201,110.00 USD | 725,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 331.22 USD | 725,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,120.00 USD | 727,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 324.37 USD | 727,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 106.95 USD | 727,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3595` | 914.21 USD | 728,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 2,940.00 USD | 731,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 143.91 USD | 731,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 740,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0435` | 2,410,000.00 USD | 0.00 USD | 863.21 USD | `-76.99%` | `19,844.00` |
| `Live` | `Long` | `0.0485` | 2,410,000.00 USD | 0.00 USD | 136.33 USD | `-74.34%` | `2,811.00` |
| `Live` | `Long` | `0.0495` | 2,410,000.00 USD | 0.00 USD | 253.44 USD | `-73.81%` | `5,120.00` |
| `Live` | `Long` | `0.0505` | 2,410,000.00 USD | 0.00 USD | 107.41 USD | `-73.28%` | `2,127.00` |
| `Live` | `Long` | `0.0515` | 2,410,000.00 USD | 0.00 USD | 1,370.00 USD | `-72.75%` | `26,617.00` |
| `Live` | `Long` | `0.0575` | 2,410,000.00 USD | 0.00 USD | 306.94 USD | `-69.58%` | `5,338.00` |
| `Live` | `Long` | `0.0585` | 2,410,000.00 USD | 0.00 USD | 526.50 USD | `-69.05%` | `9,000.00` |
| `Live` | `Long` | `0.0675` | 2,410,000.00 USD | 0.00 USD | 630.65 USD | `-64.29%` | `9,343.00` |
| `Live` | `Long` | `0.0735` | 2,410,000.00 USD | 0.00 USD | 7,720.00 USD | `-61.12%` | `105,008.00` |
| `Live` | `Long` | `0.0765` | 2,400,000.00 USD | 0.00 USD | 1,820.00 USD | `-59.53%` | `23,814.00` |
| `Live` | `Long` | `0.0775` | 2,400,000.00 USD | 0.00 USD | 412.84 USD | `-59.00%` | `5,327.00` |
| `Live` | `Long` | `0.0815` | 2,400,000.00 USD | 0.00 USD | 4,230.00 USD | `-56.88%` | `51,939.00` |
| `Live` | `Long` | `0.0835` | 2,390,000.00 USD | 0.00 USD | 11,690.00 USD | `-55.82%` | `140,000.00` |
| `Live` | `Long` | `0.0865` | 2,380,000.00 USD | 0.00 USD | 102.50 USD | `-54.24%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,380,000.00 USD | 0.00 USD | 344.75 USD | `-53.71%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,380,000.00 USD | 0.00 USD | 1,820.00 USD | `-53.18%` | `20,550.00` |
| `Live` | `Long` | `0.0895` | 2,380,000.00 USD | 0.00 USD | 1,400.00 USD | `-52.65%` | `15,628.00` |
| `Live` | `Long` | `0.0915` | 2,380,000.00 USD | 0.00 USD | 171,440.00 USD | `-51.59%` | `1,873,703.00` |
| `Live` | `Long` | `0.0925` | 2,210,000.00 USD | 0.00 USD | 165.11 USD | `-51.06%` | `1,785.00` |
| `Live` | `Long` | `0.0945` | 2,210,000.00 USD | 0.00 USD | 327.54 USD | `-50.01%` | `3,466.00` |
| `Live` | `Long` | `0.0955` | 2,210,000.00 USD | 0.00 USD | 955.00 USD | `-49.48%` | `10,000.00` |
| `Live` | `Long` | `0.0965` | 2,200,000.00 USD | 0.00 USD | 332.25 USD | `-48.95%` | `3,443.00` |
| `Live` | `Long` | `0.0985` | 2,200,000.00 USD | 0.00 USD | 87,280.00 USD | `-47.89%` | `886,128.00` |
| `Live` | `Long` | `0.1015` | 2,120,000.00 USD | 0.00 USD | 177.02 USD | `-46.30%` | `1,744.00` |
| `Live` | `Long` | `0.1025` | 2,120,000.00 USD | 0.00 USD | 4,100.00 USD | `-45.77%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,110,000.00 USD | 0.00 USD | 1,050.00 USD | `-45.24%` | `10,149.00` |
| `Live` | `Long` | `0.1055` | 2,110,000.00 USD | 0.00 USD | 150.44 USD | `-44.19%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,110,000.00 USD | 0.00 USD | 653.70 USD | `-43.66%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,110,000.00 USD | 0.00 USD | 475.58 USD | `-43.13%` | `4,424.00` |
| `Live` | `Long` | `0.1085` | 2,110,000.00 USD | 0.00 USD | 579.61 USD | `-42.60%` | `5,342.00` |
| `Live` | `Long` | `0.1095` | 2,110,000.00 USD | 0.00 USD | 1,490.00 USD | `-42.07%` | `13,608.00` |
| `Live` | `Long` | `0.1105` | 2,110,000.00 USD | 0.00 USD | 4,350.00 USD | `-41.54%` | `39,410.00` |
| `Live` | `Long` | `0.1145` | 2,100,000.00 USD | 0.00 USD | 862.64 USD | `-39.42%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,100,000.00 USD | 0.00 USD | 13,360.00 USD | `-38.37%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,090,000.00 USD | 0.00 USD | 2,160.00 USD | `-37.84%` | `18,343.00` |
| `Live` | `Long` | `0.1185` | 2,090,000.00 USD | 0.00 USD | 169.34 USD | `-37.31%` | `1,429.00` |
| `Live` | `Long` | `0.1205` | 2,090,000.00 USD | 0.00 USD | 826.27 USD | `-36.25%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,090,000.00 USD | 0.00 USD | 1,050.00 USD | `-35.72%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,090,000.00 USD | 0.00 USD | 3,650.00 USD | `-34.66%` | `29,522.00` |
| `Live` | `Long` | `0.1245` | 2,080,000.00 USD | 0.00 USD | 404.62 USD | `-34.13%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,080,000.00 USD | 0.00 USD | 2,380.00 USD | `-33.60%` | `18,941.00` |
| `Live` | `Long` | `0.1265` | 2,080,000.00 USD | 0.00 USD | 314.61 USD | `-33.08%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,080,000.00 USD | 0.00 USD | 1,260.00 USD | `-32.55%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,080,000.00 USD | 0.00 USD | 2,540.00 USD | `-31.49%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,080,000.00 USD | 0.00 USD | 13,060.00 USD | `-30.96%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,060,000.00 USD | 0.00 USD | 687.35 USD | `-30.43%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,060,000.00 USD | 0.00 USD | 6,960.00 USD | `-29.90%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,050,000.00 USD | 0.00 USD | 5,910.00 USD | `-29.37%` | `44,280.00` |
| `Live` | `Long` | `0.1345` | 2,050,000.00 USD | 0.00 USD | 7,630.00 USD | `-28.84%` | `56,723.00` |
| `Live` | `Long` | `0.1355` | 2,040,000.00 USD | 0.00 USD | 106.64 USD | `-28.31%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,040,000.00 USD | 0.00 USD | 403.77 USD | `-27.79%` | `2,958.00` |
| `Live` | `Long` | `0.1405` | 2,040,000.00 USD | 0.00 USD | 314.44 USD | `-25.67%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,040,000.00 USD | 0.00 USD | 42,080.00 USD | `-25.14%` | `297,371.00` |
| `Live` | `Long` | `0.1425` | 2,000,000.00 USD | 0.00 USD | 958.46 USD | `-24.61%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,000,000.00 USD | 0.00 USD | 15,780.00 USD | `-24.08%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 1,980,000.00 USD | 0.00 USD | 2,220.00 USD | `-23.55%` | `15,394.00` |
| `Live` | `Long` | `0.1455` | 1,980,000.00 USD | 0.00 USD | 3,770.00 USD | `-23.02%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 1,980,000.00 USD | 0.00 USD | 33,880.00 USD | `-22.49%` | `231,277.00` |
| `Live` | `Long` | `0.1475` | 1,940,000.00 USD | 0.00 USD | 292.94 USD | `-21.97%` | `1,986.00` |
| `Live` | `Long` | `0.1485` | 1,940,000.00 USD | 0.00 USD | 1,360.00 USD | `-21.44%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 1,940,000.00 USD | 0.00 USD | 427.12 USD | `-20.91%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 1,940,000.00 USD | 0.00 USD | 10,580.00 USD | `-20.38%` | `70,285.00` |
| `Live` | `Long` | `0.1515` | 1,930,000.00 USD | 0.00 USD | 35,710.00 USD | `-19.85%` | `235,729.00` |
| `Live` | `Long` | `0.1525` | 1,890,000.00 USD | 0.00 USD | 110,250.00 USD | `-19.32%` | `722,928.00` |
| `Live` | `Long` | `0.1535` | 1,780,000.00 USD | 0.00 USD | 41,820.00 USD | `-18.79%` | `272,427.00` |
| `Live` | `Long` | `0.1545` | 1,740,000.00 USD | 0.00 USD | 721.05 USD | `-18.26%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,740,000.00 USD | 0.00 USD | 1,320.00 USD | `-17.73%` | `8,490.00` |
| `Live` | `Long` | `0.1565` | 1,740,000.00 USD | 0.00 USD | 10,860.00 USD | `-17.20%` | `69,381.00` |
| `Live` | `Long` | `0.1575` | 1,730,000.00 USD | 0.00 USD | 713.16 USD | `-16.68%` | `4,528.00` |
| `Live` | `Long` | `0.1585` | 1,730,000.00 USD | 0.00 USD | 6,000.00 USD | `-16.15%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,720,000.00 USD | 0.00 USD | 3,450.00 USD | `-15.62%` | `21,609.00` |
| `Live` | `Long` | `0.1605` | 1,720,000.00 USD | 0.00 USD | 57,720.00 USD | `-15.09%` | `359,655.00` |
| `Live` | `Long` | `0.1615` | 1,660,000.00 USD | 0.00 USD | 549,760.00 USD | `-14.56%` | `3,404,097.00` |
| `Live` | `Long` | `0.1625` | 1,110,000.00 USD | 0.00 USD | 3,210.00 USD | `-14.03%` | `19,783.00` |
| `Live` | `Long` | `0.1635` | 1,110,000.00 USD | 0.00 USD | 124.26 USD | `-13.50%` | `760.00` |
| `Live` | `Long` | `0.1645` | 1,110,000.00 USD | 0.00 USD | 10,840.00 USD | `-12.97%` | `65,896.00` |
| `Live` | `Long` | `0.1665` | 1,100,000.00 USD | 0.00 USD | 1,720.00 USD | `-11.91%` | `10,345.00` |
| `Live` | `Long` | `0.1675` | 1,090,000.00 USD | 0.00 USD | 630.81 USD | `-11.39%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,090,000.00 USD | 0.00 USD | 12,160.00 USD | `-10.86%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,080,000.00 USD | 0.00 USD | 78,180.00 USD | `-10.33%` | `461,249.00` |
| `Live` | `Long` | `0.1705` | 1,000,000.00 USD | 0.00 USD | 626,600.00 USD | `-9.80%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 377,020.00 USD | 0.00 USD | 252,270.00 USD | `-9.27%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 124,750.00 USD | 0.00 USD | 33,550.00 USD | `-8.74%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 91,200.00 USD | 0.00 USD | 1,270.00 USD | `-8.21%` | `7,296.00` |
| `Live` | `Long` | `0.1745` | 89,940.00 USD | 0.00 USD | 234.18 USD | `-7.68%` | `1,342.00` |
| `Live` | `Long` | `0.1755` | 89,700.00 USD | 0.00 USD | 18,670.00 USD | `-7.15%` | `106,401.00` |
| `Live` | `Long` | `0.1765` | 71,030.00 USD | 0.00 USD | 42,760.00 USD | `-6.62%` | `242,276.00` |
| `Live` | `Long` | `0.1775` | 28,270.00 USD | 0.00 USD | 1,360.00 USD | `-6.09%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 26,910.00 USD | 0.00 USD | 4,530.00 USD | `-5.57%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 22,380.00 USD | 0.00 USD | 1,470.00 USD | `-5.04%` | `8,184.00` |
| `Live` | `Long` | `0.1805` | 20,910.00 USD | 0.00 USD | 3,050.00 USD | `-4.51%` | `16,904.00` |
| `Live` | `Long` | `0.1815` | 17,860.00 USD | 0.00 USD | 11,080.00 USD | `-3.98%` | `61,030.00` |
| `Live` | `Long` | `0.1825` | 6,780.00 USD | 0.00 USD | 6,780.00 USD | `-3.45%` | `37,172.00` |
| `Live` | `Short` | `0.1945` | 2,570.00 USD | 2,570.00 USD | 0.00 USD | `+2.90%` | `13,212.00` |
| `Live` | `Short` | `0.1955` | 3,320.00 USD | 755.22 USD | 0.00 USD | `+3.43%` | `3,863.00` |
| `Live` | `Short` | `0.1965` | 3,430.00 USD | 104.93 USD | 0.00 USD | `+3.96%` | `534.00` |
| `Live` | `Short` | `0.1975` | 3,620.00 USD | 187.03 USD | 0.00 USD | `+4.49%` | `947.00` |
| `Live` | `Short` | `0.1985` | 3,960.00 USD | 338.64 USD | 0.00 USD | `+5.02%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 4,060.00 USD | 107.13 USD | 0.00 USD | `+5.54%` | `537.00` |
| `Live` | `Short` | `0.2005` | 6,640.00 USD | 2,570.00 USD | 0.00 USD | `+6.07%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 8,740.00 USD | 2,100.00 USD | 0.00 USD | `+6.60%` | `10,418.00` |
| `Live` | `Short` | `0.2075` | 10,950.00 USD | 2,220.00 USD | 0.00 USD | `+9.78%` | `10,683.00` |
| `Live` | `Short` | `0.2125` | 13,530.00 USD | 2,580.00 USD | 0.00 USD | `+12.42%` | `12,141.00` |
| `Live` | `Short` | `0.2145` | 19,550.00 USD | 6,020.00 USD | 0.00 USD | `+13.48%` | `28,067.00` |
| `Live` | `Short` | `0.2175` | 23,480.00 USD | 3,930.00 USD | 0.00 USD | `+15.07%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 26,130.00 USD | 2,650.00 USD | 0.00 USD | `+15.60%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 27,780.00 USD | 1,640.00 USD | 0.00 USD | `+17.18%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 27,980.00 USD | 200.48 USD | 0.00 USD | `+18.24%` | `897.00` |
| `Live` | `Short` | `0.2265` | 30,210.00 USD | 2,230.00 USD | 0.00 USD | `+19.83%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 39,450.00 USD | 9,240.00 USD | 0.00 USD | `+20.89%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 39,730.00 USD | 282.02 USD | 0.00 USD | `+23.00%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 47,370.00 USD | 7,640.00 USD | 0.00 USD | `+23.53%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 49,040.00 USD | 1,670.00 USD | 0.00 USD | `+27.24%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 49,580.00 USD | 543.62 USD | 0.00 USD | `+27.76%` | `2,251.00` |
| `Live` | `Short` | `0.2425` | 50,660.00 USD | 1,080.00 USD | 0.00 USD | `+28.29%` | `4,435.00` |
| `Live` | `Short` | `0.2455` | 51,300.00 USD | 641.00 USD | 0.00 USD | `+29.88%` | `2,611.00` |
| `Live` | `Short` | `0.2485` | 52,360.00 USD | 1,060.00 USD | 0.00 USD | `+31.47%` | `4,254.00` |
| `Live` | `Short` | `0.2585` | 52,740.00 USD | 380.25 USD | 0.00 USD | `+36.76%` | `1,471.00` |
| `Live` | `Short` | `0.2675` | 54,710.00 USD | 1,970.00 USD | 0.00 USD | `+41.52%` | `7,372.00` |
| `Live` | `Short` | `0.2715` | 54,830.00 USD | 120.00 USD | 0.00 USD | `+43.64%` | `442.00` |
| `Live` | `Short` | `0.2775` | 55,210.00 USD | 379.62 USD | 0.00 USD | `+46.81%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 57,380.00 USD | 2,170.00 USD | 0.00 USD | `+50.51%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 57,790.00 USD | 411.09 USD | 0.00 USD | `+53.16%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 61,060.00 USD | 3,260.00 USD | 0.00 USD | `+54.22%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 61,580.00 USD | 519.79 USD | 0.00 USD | `+55.27%` | `1,771.00` |
| `Live` | `Short` | `0.2945` | 65,550.00 USD | 3,980.00 USD | 0.00 USD | `+55.80%` | `13,504.00` |
| `Live` | `Short` | `0.2955` | 73,540.00 USD | 7,990.00 USD | 0.00 USD | `+56.33%` | `27,027.00` |
| `Live` | `Short` | `0.2965` | 138,960.00 USD | 65,420.00 USD | 0.00 USD | `+56.86%` | `220,630.00` |
| `Live` | `Short` | `0.3005` | 139,100.00 USD | 146.34 USD | 0.00 USD | `+58.98%` | `487.00` |
| `Live` | `Short` | `0.3045` | 139,240.00 USD | 131.85 USD | 0.00 USD | `+61.09%` | `433.00` |
| `Live` | `Short` | `0.3055` | 139,640.00 USD | 408.15 USD | 0.00 USD | `+61.62%` | `1,336.00` |
| `Live` | `Short` | `0.3075` | 143,170.00 USD | 3,520.00 USD | 0.00 USD | `+62.68%` | `11,458.00` |
| `Live` | `Short` | `0.3125` | 240,670.00 USD | 97,510.00 USD | 0.00 USD | `+65.33%` | `312,021.00` |
| `Live` | `Short` | `0.3265` | 277,710.00 USD | 37,030.00 USD | 0.00 USD | `+72.73%` | `113,421.00` |
| `Live` | `Short` | `0.3295` | 280,880.00 USD | 3,180.00 USD | 0.00 USD | `+74.32%` | `9,639.00` |
| `Live` | `Short` | `0.3335` | 281,030.00 USD | 149.07 USD | 0.00 USD | `+76.44%` | `447.00` |
| `Live` | `Short` | `0.3355` | 282,210.00 USD | 1,170.00 USD | 0.00 USD | `+77.49%` | `3,500.00` |
| `Live` | `Short` | `0.3385` | 359,460.00 USD | 77,250.00 USD | 0.00 USD | `+79.08%` | `228,215.00` |
| `Live` | `Short` | `0.3415` | 362,460.00 USD | 3,000.00 USD | 0.00 USD | `+80.67%` | `8,785.00` |
| `Live` | `Short` | `0.3425` | 362,700.00 USD | 245.23 USD | 0.00 USD | `+81.20%` | `716.00` |
| `Live` | `Short` | `0.3455` | 611,720.00 USD | 249,020.00 USD | 0.00 USD | `+82.78%` | `720,753.00` |
| `Live` | `Short` | `0.3465` | 611,860.00 USD | 138.95 USD | 0.00 USD | `+83.31%` | `401.00` |
| `Live` | `Short` | `0.3485` | 812,390.00 USD | 200,530.00 USD | 0.00 USD | `+84.37%` | `575,408.00` |
| `Live` | `Short` | `0.3495` | 813,690.00 USD | 1,300.00 USD | 0.00 USD | `+84.90%` | `3,713.00` |
| `Live` | `Short` | `0.3505` | 814,020.00 USD | 331.22 USD | 0.00 USD | `+85.43%` | `945.00` |
| `Live` | `Short` | `0.3515` | 815,140.00 USD | 1,120.00 USD | 0.00 USD | `+85.96%` | `3,187.00` |
| `Live` | `Short` | `0.3555` | 815,460.00 USD | 325.28 USD | 0.00 USD | `+88.08%` | `915.00` |
| `Live` | `Short` | `0.3565` | 815,570.00 USD | 106.95 USD | 0.00 USD | `+88.60%` | `300.00` |
| `Live` | `Short` | `0.3615` | 819,770.00 USD | 4,200.00 USD | 0.00 USD | `+91.25%` | `11,627.00` |
| `Live` | `Short` | `0.3625` | 819,920.00 USD | 143.91 USD | 0.00 USD | `+91.78%` | `397.00` |
| `Live` | `Short` | `0.3715` | 829,090.00 USD | 9,170.00 USD | 0.00 USD | `+96.54%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 856,010.00 USD | 26,920.00 USD | 0.00 USD | `+98.13%` | `71,879.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 148,010,000.00 USD | 0.00 USD | 415.13 USD | `-68.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 148,010,000.00 USD | 0.00 USD | 438.99 USD | `-67.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 148,010,000.00 USD | 0.00 USD | 1,100.00 USD | `-41.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 148,000,000.00 USD | 0.00 USD | 541.33 USD | `-41.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 148,000,000.00 USD | 0.00 USD | 429.20 USD | `-38.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 148,000,000.00 USD | 0.00 USD | 602,500.00 USD | `-36.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 147,400,000.00 USD | 0.00 USD | 4,460.00 USD | `-34.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 147,400,000.00 USD | 0.00 USD | 1,320.00 USD | `-32.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 147,400,000.00 USD | 0.00 USD | 13,390.00 USD | `-30.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 147,380,000.00 USD | 0.00 USD | 728.88 USD | `-29.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 147,380,000.00 USD | 0.00 USD | 4,350.00 USD | `-28.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 147,380,000.00 USD | 0.00 USD | 4,730.00 USD | `-27.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 147,370,000.00 USD | 0.00 USD | 1,820.00 USD | `-26.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 147,370,000.00 USD | 0.00 USD | 1,050.00 USD | `-25.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 147,370,000.00 USD | 0.00 USD | 351.26 USD | `-24.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 147,370,000.00 USD | 0.00 USD | 1,600.00 USD | `-24.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 147,370,000.00 USD | 0.00 USD | 10,400.00 USD | `-23.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 147,360,000.00 USD | 0.00 USD | 5,980.00 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 147,350,000.00 USD | 0.00 USD | 303.26 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 147,350,000.00 USD | 0.00 USD | 3,230.00 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 147,350,000.00 USD | 0.00 USD | 6,380.00 USD | `-19.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 147,340,000.00 USD | 0.00 USD | 126.54 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 147,340,000.00 USD | 0.00 USD | 1,790.00 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 147,340,000.00 USD | 0.00 USD | 6,260.00 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 147,330,000.00 USD | 0.00 USD | 552.21 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 147,330,000.00 USD | 0.00 USD | 166.84 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 147,330,000.00 USD | 0.00 USD | 9,410.00 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 147,320,000.00 USD | 0.00 USD | 769.39 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 147,320,000.00 USD | 0.00 USD | 24,760.00 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 147,300,000.00 USD | 0.00 USD | 6,540.00 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 147,290,000.00 USD | 0.00 USD | 1,750.00 USD | `-12.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 147,290,000.00 USD | 0.00 USD | 5,670.00 USD | `-12.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 147,280,000.00 USD | 0.00 USD | 7,390.00 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 147,280,000.00 USD | 0.00 USD | 317.92 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 147,280,000.00 USD | 0.00 USD | 4,270.00 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 147,270,000.00 USD | 0.00 USD | 1,300.00 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 147,270,000.00 USD | 0.00 USD | 1,280.00 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 147,270,000.00 USD | 0.00 USD | 640.67 USD | `-8.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 147,270,000.00 USD | 0.00 USD | 103.58 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 147,270,000.00 USD | 0.00 USD | 349.00 USD | `-7.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 147,270,000.00 USD | 0.00 USD | 1,760.00 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 147,270,000.00 USD | 0.00 USD | 847.38 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 147,260,000.00 USD | 0.00 USD | 4,910.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 147,260,000.00 USD | 0.00 USD | 5,400.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 147,250,000.00 USD | 0.00 USD | 18,500.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 147,240,000.00 USD | 0.00 USD | 1,570.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 147,230,000.00 USD | 0.00 USD | 2,720.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 147,230,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-3.45%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 110,730,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-2.92%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 37,330,000.00 USD | 0.00 USD | 18,800.00 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 37,310,000.00 USD | 0.00 USD | 3,970.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 37,310,000.00 USD | 0.00 USD | 37,300,000.00 USD | `-1.33%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1875` | 6,680.00 USD | 0.00 USD | 3,580.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 2,320.00 USD | 2,320.00 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 7,820.00 USD | 5,500.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 9,910.00 USD | 2,090.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 10,270.00 USD | 362.29 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 10,630.00 USD | 366.49 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 11,020.00 USD | 389.00 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 11,840.00 USD | 819.54 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 15,500.00 USD | 3,660.00 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 16,500.00 USD | 1,000.00 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 17,150.00 USD | 646.71 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 17,550.00 USD | 399.00 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 28,080.00 USD | 10,540.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 74,420.00 USD | 46,340.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 75,020.00 USD | 594.34 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 82,220.00 USD | 7,210.00 USD | 0.00 USD | `+7.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 84,910.00 USD | 2,690.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 87,070.00 USD | 2,160.00 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 87,270.00 USD | 207.74 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 87,590.00 USD | 312.70 USD | 0.00 USD | `+9.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 95,930.00 USD | 8,340.00 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 103,850.00 USD | 7,920.00 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 125,920.00 USD | 22,070.00 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 145,900.00 USD | 19,980.00 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 152,600.00 USD | 6,700.00 USD | 0.00 USD | `+12.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 156,790.00 USD | 4,190.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 157,760.00 USD | 965.25 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 168,060.00 USD | 10,300.00 USD | 0.00 USD | `+14.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 168,550.00 USD | 487.34 USD | 0.00 USD | `+14.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 168,660.00 USD | 109.91 USD | 0.00 USD | `+15.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 184,120.00 USD | 15,460.00 USD | 0.00 USD | `+16.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 186,880.00 USD | 2,760.00 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 188,530.00 USD | 1,650.00 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 197,540.00 USD | 9,010.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 201,290.00 USD | 3,750.00 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 201,400.00 USD | 114.50 USD | 0.00 USD | `+18.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 201,740.00 USD | 339.60 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 201,850.00 USD | 109.40 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 210,950.00 USD | 9,100.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 220,090.00 USD | 9,140.00 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 220,760.00 USD | 662.92 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 221,090.00 USD | 337.06 USD | 0.00 USD | `+22.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 221,260.00 USD | 171.12 USD | 0.00 USD | `+23.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 221,360.00 USD | 101.11 USD | 0.00 USD | `+23.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 222,470.00 USD | 1,110.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 231,890.00 USD | 9,420.00 USD | 0.00 USD | `+24.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 232,210.00 USD | 315.96 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 232,990.00 USD | 778.76 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 233,180.00 USD | 192.71 USD | 0.00 USD | `+26.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 233,700.00 USD | 514.45 USD | 0.00 USD | `+26.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 233,910.00 USD | 209.72 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 234,020.00 USD | 115.92 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 234,260.00 USD | 236.19 USD | 0.00 USD | `+28.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 235,410.00 USD | 1,150.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 235,690.00 USD | 288.22 USD | 0.00 USD | `+29.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 236,180.00 USD | 491.03 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 237,510.00 USD | 1,320.00 USD | 0.00 USD | `+30.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 247,450.00 USD | 9,940.00 USD | 0.00 USD | `+31.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 247,950.00 USD | 499.00 USD | 0.00 USD | `+32.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 249,050.00 USD | 1,100.00 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 249,220.00 USD | 168.76 USD | 0.00 USD | `+33.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 249,820.00 USD | 603.73 USD | 0.00 USD | `+33.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 251,990.00 USD | 2,170.00 USD | 0.00 USD | `+34.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 253,460.00 USD | 1,470.00 USD | 0.00 USD | `+36.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 253,730.00 USD | 271.44 USD | 0.00 USD | `+37.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 674,640.00 USD | 420,910.00 USD | 0.00 USD | `+37.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 675,820.00 USD | 1,180.00 USD | 0.00 USD | `+39.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 684,710.00 USD | 8,890.00 USD | 0.00 USD | `+41.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 699,580.00 USD | 14,860.00 USD | 0.00 USD | `+42.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 700,920.00 USD | 1,340.00 USD | 0.00 USD | `+42.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 703,630.00 USD | 2,710.00 USD | 0.00 USD | `+43.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 717,490.00 USD | 13,870.00 USD | 0.00 USD | `+44.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 722,710.00 USD | 5,220.00 USD | 0.00 USD | `+45.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 723,880.00 USD | 1,170.00 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 728,040.00 USD | 4,150.00 USD | 0.00 USD | `+47.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 728,980.00 USD | 944.99 USD | 0.00 USD | `+47.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 729,180.00 USD | 198.73 USD | 0.00 USD | `+49.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 730,550.00 USD | 1,370.00 USD | 0.00 USD | `+50.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 731,630.00 USD | 1,080.00 USD | 0.00 USD | `+52.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 746,610.00 USD | 14,980.00 USD | 0.00 USD | `+53.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 747,850.00 USD | 1,230.00 USD | 0.00 USD | `+54.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 749,290.00 USD | 1,440.00 USD | 0.00 USD | `+57.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 749,650.00 USD | 355.21 USD | 0.00 USD | `+58.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 756,300.00 USD | 6,650.00 USD | 0.00 USD | `+58.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 775,280.00 USD | 18,980.00 USD | 0.00 USD | `+61.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 779,430.00 USD | 4,150.00 USD | 0.00 USD | `+63.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 782,670.00 USD | 3,250.00 USD | 0.00 USD | `+66.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 783,170.00 USD | 493.89 USD | 0.00 USD | `+71.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 783,350.00 USD | 181.30 USD | 0.00 USD | `+72.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 784,730.00 USD | 1,380.00 USD | 0.00 USD | `+74.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 797,020.00 USD | 12,290.00 USD | 0.00 USD | `+75.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 797,130.00 USD | 111.06 USD | 0.00 USD | `+76.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 797,350.00 USD | 220.61 USD | 0.00 USD | `+80.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 800,690.00 USD | 3,340.00 USD | 0.00 USD | `+84.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 800,880.00 USD | 188.75 USD | 0.00 USD | `+99.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 801,790.00 USD | 909.54 USD | 0.00 USD | `+100.24%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `406.22M` | Total OI Tokens: `2,141,143,316.9 ADA`
  * 1h OI Change: `+1.16%` | 4h OI Change: `-2.71%` | 24h OI Change: `-7.83%`
  * Exchange Breakdown: Binance=`75.47M` | Bybit=`49.91M` | OKX=`28.61M` | Hyperliquid=`27.83M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `188.82` | Last 24h: `10.44K` | Last 3d: `50.88K` | Last 7d: `82.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0064%` |
| **USDT Bybit** | `-0.0168%` | **USDT KuCoin** | `0.0016%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0004%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `45.75%` | `54.25%` | `0.84` | 3,760,000.00 USD |
| `15M` | `Binance` | `43.12%` | `56.88%` | `0.76` | 1,310,000.00 USD |
| `15M` | `OKX` | `45.64%` | `54.36%` | `0.84` | 336,150.00 USD |
| `15M` | `Bybit` | `54.88%` | `45.12%` | `1.22` | 601,750.00 USD |
| `15M` | `KuCoin` | `69.14%` | `30.86%` | `2.24` | 64,580.00 USD |
| `15M` | `Gate` | `55.53%` | `44.47%` | `1.25` | 46,220.00 USD |
| `15M` | `Bitget` | `22.38%` | `77.62%` | `0.29` | 257,190.00 USD |
| `15M` | `BingX` | `58.89%` | `41.11%` | `1.43` | 132,050.00 USD |
| `15M` | `MEXC` | `13.36%` | `86.64%` | `0.15` | 153,120.00 USD |
| `15M` | `Bitunix` | `32.86%` | `67.14%` | `0.49` | 67,980.00 USD |
| `15M` | `Hyperliquid` | `38.37%` | `61.63%` | `0.62` | 22,020.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `57.84%` | `42.16%` | `1.37` | 690,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `5.16%` | `94.84%` | `0.05` | 58,110.00 USD |
| `15M` | `HTX` | `69.51%` | `30.49%` | `2.28` | 18,360.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `3.2%` | `96.8%` | `0.03` | 2,730.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 17.04 USD |
| `15M` | `Whale Positions` | `43.12%` | `56.88%` | `0.76` | 1,310,000.00 USD |
| `15M` | `Global Accounts` | `45.75%` | `54.25%` | `0.84` | 3,760,000.00 USD |
| `1H` | `ADA` | `50.66%` | `49.34%` | `1.03` | 67,110,000.00 USD |
| `1H` | `Binance` | `50.39%` | `49.61%` | `1.02` | 27,290,000.00 USD |
| `1H` | `OKX` | `48.91%` | `51.09%` | `0.96` | 14,450,000.00 USD |
| `1H` | `Bybit` | `56.2%` | `43.8%` | `1.28` | 5,350,000.00 USD |
| `1H` | `KuCoin` | `53.84%` | `46.16%` | `1.17` | 317,560.00 USD |
| `1H` | `Gate` | `58.64%` | `41.36%` | `1.42` | 8,700,000.00 USD |
| `1H` | `Bitget` | `41.86%` | `58.14%` | `0.72` | 1,390,000.00 USD |
| `1H` | `BingX` | `54.81%` | `45.19%` | `1.21` | 745,940.00 USD |
| `1H` | `MEXC` | `49.26%` | `50.74%` | `0.97` | 2,360,000.00 USD |
| `1H` | `Bitunix` | `35.58%` | `64.42%` | `0.55` | 2,510,000.00 USD |
| `1H` | `Hyperliquid` | `54.99%` | `45.01%` | `1.22` | 1,150,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.37%` | `48.63%` | `1.06` | 254,250.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 40,810.00 USD |
| `1H` | `WhiteBIT` | `14.85%` | `85.15%` | `0.17` | 556,350.00 USD |
| `1H` | `HTX` | `46.57%` | `53.43%` | `0.87` | 1,430,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `55.56%` | `44.44%` | `1.25` | 148,630.00 USD |
| `1H` | `Aster` | `70.14%` | `29.86%` | `2.35` | 394,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `18.71%` | `81.29%` | `0.23` | 30,620.00 USD |
| `1H` | `Whale Positions` | `50.39%` | `49.61%` | `1.02` | 27,290,000.00 USD |
| `1H` | `Global Accounts` | `50.66%` | `49.34%` | `1.03` | 67,110,000.00 USD |
| `4H` | `ADA` | `49.82%` | `50.18%` | `0.99` | 510,140,000.00 USD |
| `4H` | `Binance` | `50.05%` | `49.95%` | `1.00` | 189,580,000.00 USD |
| `4H` | `OKX` | `49.69%` | `50.31%` | `0.99` | 116,140,000.00 USD |
| `4H` | `Bybit` | `47.85%` | `52.15%` | `0.92` | 49,160,000.00 USD |
| `4H` | `KuCoin` | `48.52%` | `51.48%` | `0.94` | 4,680,000.00 USD |
| `4H` | `Gate` | `57.42%` | `42.58%` | `1.35` | 44,970,000.00 USD |
| `4H` | `Bitget` | `47.15%` | `52.85%` | `0.89` | 17,240,000.00 USD |
| `4H` | `BingX` | `46%` | `54%` | `0.85` | 7,480,000.00 USD |
| `4H` | `MEXC` | `49.94%` | `50.06%` | `1.00` | 30,850,000.00 USD |
| `4H` | `Bitunix` | `43.94%` | `56.06%` | `0.78` | 18,570,000.00 USD |
| `4H` | `Hyperliquid` | `48.38%` | `51.62%` | `0.94` | 5,840,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.17%` | `48.83%` | `1.05` | 1,690,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 573,200.00 USD |
| `4H` | `WhiteBIT` | `57.79%` | `42.21%` | `1.37` | 4,020,000.00 USD |
| `4H` | `HTX` | `52.9%` | `47.1%` | `1.12` | 12,580,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `54.36%` | `45.64%` | `1.19` | 1,500,000.00 USD |
| `4H` | `Aster` | `46.9%` | `53.1%` | `0.88` | 5,030,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `23.34%` | `76.66%` | `0.30` | 226,190.00 USD |
| `4H` | `Whale Positions` | `50.05%` | `49.95%` | `1.00` | 189,580,000.00 USD |
| `4H` | `Global Accounts` | `49.82%` | `50.18%` | `0.99` | 510,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1874` | `0.1869` | `0.1874` | `0.1878` | `0.1855` | 4,653,756.20 USD | 2,488,864.82 USD | 2,164,891.37 USD | 323,973.45 USD | `+6.96%` | `1B / 3S` |
| `0:00 UTC` | `0.1872` | `0.1874` | `0.1872` | `0.1888` | `0.1860` | 5,684,500.06 USD | 3,804,478.59 USD | 1,880,021.47 USD | 1,924,457.12 USD | `+33.85%` | `8B / 1S` |
| `5:00 UTC` | `0.1874` | `0.1874` | `0.1874` | `0.1885` | `0.1865` | 2,610,344.37 USD | 1,024,388.05 USD | 1,585,956.32 USD | -561,568.27 USD | `-21.51%` | `1B / 5S` |
| `0:00 UTC` | `0.1880` | `0.1868` | `0.1880` | `0.1885` | `0.1850` | 3,853,495.92 USD | 1,924,811.50 USD | 1,928,684.42 USD | -3,872.92 USD | `-0.10%` | `4B / 5S` |
| `5:00 UTC` | `0.1866` | `0.1869` | `0.1866` | `0.1876` | `0.1862` | 2,227,884.56 USD | 1,223,520.92 USD | 1,004,363.65 USD | 219,157.27 USD | `+9.84%` | `1B / 1S` |
| `0:00 UTC` | `0.1874` | `0.1870` | `0.1874` | `0.1881` | `0.1859` | 2,036,163.82 USD | 1,133,163.53 USD | 903,000.29 USD | 230,163.23 USD | `+11.30%` | `3B / 0S` |
| `5:00 UTC` | `0.1888` | `0.1889` | `0.1888` | `0.1898` | `0.1880` | 1,960,271.66 USD | 990,186.27 USD | 970,085.39 USD | 20,100.88 USD | `+1.03%` | `3B / 0S` |
| `0:00 UTC` | `0.1899` | `0.1895` | `0.1899` | `0.1900` | `0.1890` | 1,399,205.02 USD | 619,891.71 USD | 779,313.31 USD | -159,421.60 USD | `-11.39%` | `1B / 1S` |
| `5:00 UTC` | `0.1890` | `0.1890` | `0.1890` | `0.1898` | `0.1885` | 1,096,660.36 USD | 485,441.32 USD | 611,219.04 USD | -125,777.71 USD | `-11.47%` | `0B / 2S` |
| `0:00 UTC` | `0.1900` | `0.1898` | `0.1900` | `0.1901` | `0.1890` | 757,750.13 USD | 491,864.45 USD | 265,885.69 USD | 225,978.76 USD | `+29.82%` | `3B / 1S` |

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
| `5m` | 39,940.00 USD | 132,740.00 USD | **`ACCUMULATION`** |
| `15m` | 162,440.00 USD | -172,270.00 USD | **`DISTRIBUTION`** |
| `30m` | 139,520.00 USD | -187,720.00 USD | **`DISTRIBUTION`** |
| `1h` | 201,190.00 USD | 422,100.00 USD | **`ACCUMULATION`** |
| `2h` | -161,390.00 USD | 1,890,000.00 USD | **`ACCUMULATION`** |
| `4h` | -3,170,000.00 USD | -1,230,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,300,000.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,630,000.00 USD | -13,290,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,410,000.00 USD | -13,690,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,720,000.00 USD | -9,250,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,900,000.00 USD | -41,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,180,000.00 USD | -199,460,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+39.94K` | 15m=`+162.44K` | 1h=`+201.19K` | 24h=`-8.72M`
* Futures Capital Netflows: 5m=`+132.74K` | 15m=`-172.27K` | 1h=`+422.10K` | 24h=`-9.25M`
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
  * `2026-10-30 08:34:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:38 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:35:38 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:36:38 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:36:38 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1857` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.02` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.19`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1925` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.40` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.82`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1912`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
