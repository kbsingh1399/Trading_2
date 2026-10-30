# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 07:36:16 IST` (`2026-10-30 02:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1853` | **Live Ask Quote**: `0.1874` | **Mid Price**: `0.1864`
- **Spread Points**: `21.00` | **Spread BPS**: `112.69 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1854` | VWAP Z-Score: `-1.39` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0026` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `35.52` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2130` | Lower -3.00σ Band: `0.1764`
  * Upper +2.51σ Band: `0.2100` | Lower -2.51σ Band: `0.1794`
  * Upper +2.01σ Band: `0.2069` | Lower -2.01σ Band: `0.1824`
  * Upper +2.00σ Band: `0.2069` | Lower -2.00σ Band: `0.1825`
  * Upper +1.28σ Band: `0.2025` | Lower -1.28σ Band: `0.1869`
  * Upper +1.00σ Band: `0.2008` | Lower -1.00σ Band: `0.1886`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1868` | EMA-20=`0.1894` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1939` (Slope: `+0.0000`) | EMA-100=`0.1968`
  * Institutional Anchors: EMA-144=`0.1981` | EMA-200=`0.1992` (Slope: `-0.7485`) | EMA-233=`0.2001`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1939` (Distance: `-3.85%`)
  * Point of Control (POC) = `0.1907` (Distance: `-2.25%`)
  * Value Area Low (VAL) = `0.1861` (Distance: `+0.15%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2061` | Weekly POC=`0.2031` | Weekly VAL=`0.1996`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1871` | Low=`0.1856`
  * New York Session (13:00-21:00 UTC): High=`0.1875` | Low=`0.1852`
  * Initial Balance (First Hour): IB High=`0.1869` | IB Low=`0.1858`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1856` - `0.1871`
  * Optimal Trade Entry (OTE 0.705): `0.1867`
  * Structural Invalidation Anchor (0.786): `0.1878`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1876` | `0.1876` | `0.1864` | `0.1871` | `3,740,102` | 699,250.45 USD | -40,469.86 USD | `-5.79%` | -4,140,644.67 USD | `+0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1871` | `0.1872` | `0.1862` | `0.1870` | `3,732,192` | 696,488.97 USD | 22,943.04 USD | `+3.29%` | -4,117,701.63 USD | `+0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1869` | `0.1873` | `0.1865` | `0.1868` | `2,045,898` | 382,445.25 USD | 73,123.21 USD | `+19.12%` | -4,044,578.42 USD | `+0.02` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1883` | `0.1884` | `0.1865` | `0.1866` | `13,932,538` | 2,610,344.37 USD | -561,568.27 USD | `-21.51%` | -4,096,301.88 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1867` | `0.1884` | `0.1849` | `0.1875` | `20,631,351` | 3,853,495.92 USD | -3,872.92 USD | `-0.10%` | -4,100,174.81 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1876` | `0.1876` | `0.1862` | `0.1866` | `9,464,791` | 1,768,214.11 USD | 45,625.83 USD | `+2.58%` | -4,054,548.97 USD | `+0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1916` | `0.1925` | `0.1897` | `0.1902` | `69,248,170` | 13,230,792.46 USD | 850,972.63 USD | `+6.43%` | -3,601,662.48 USD | `+0.64` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1903` | `0.1910` | `0.1821` | `0.1870` | `239,530,678` | 44,487,434.47 USD | -1,857,528.25 USD | `-4.18%` | -5,459,190.73 USD | `-0.99` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1871` | `0.1887` | `0.1849` | `0.1868` | `74,429,384` | 13,926,525.02 USD | 1,414,612.31 USD | `+10.16%` | -4,044,578.42 USD | `+0.95` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1910` | `0.1821` | `0.1866` | `313,906,661` | 58,403,988.93 USD | -452,886.50 USD | `-0.78%` | -3,492,423.80 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | 1,321,924.30 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 3,089,831.02 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1910` | `0.1821` | `0.1866` | `313,906,661` | 58,403,988.93 USD | -452,886.50 USD | `-0.78%` | -3,492,423.80 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.1864`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `540` | `0x77ee...2902` | `SHORT` | 3,998,940.98 USD | `21,412,192.00` | `0.1911` | `0.1871` | `0.5718` | 92,310.76 USD | `+2.31%` | `10X Cross` |
| `1236` | `0x123d...3bff` | `LONG` | 1,755,151.69 USD | `9,392,870.00` | `0.2912` | `0.1871` | `0.000000` | -980,505.03 USD | `-55.86%` | `10X Cross` |
| `1260` | `0x7737...bf66` | `SHORT` | 1,698,740.42 USD | `9,091,466.00` | `0.2190` | `0.1871` | `1.98` | 292,249.38 USD | `+17.20%` | `10X Cross` |
| `1563` | `0x5f94...4b96` | `SHORT` | 1,338,422.36 USD | `7,162,318.00` | `0.2303` | `0.1871` | `0.6810` | 311,052.83 USD | `+23.24%` | `10X Cross` |
| `1788` | `0x4982...59e6` | `SHORT` | 1,120,218.15 USD | `5,998,812.00` | `0.1891` | `0.1871` | `0.4249` | 14,340.21 USD | `+1.28%` | `10X Cross` |
| `1826` | `0xcac1...26b3` | `LONG` | 1,083,825.33 USD | `5,803,927.00` | `0.2000` | `0.1871` | `0.000000` | -76,990.26 USD | `-7.10%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2065` | 5,880.22 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.88K USD at 0.2065 USD [API] | `2026-10-28 19:46:53` |
| `ANNOUNCEMENT` | `INFO` | `0.2065` | 6,647.05 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2065 USD [API] | `2026-10-28 22:02:11` |
| `ANNOUNCEMENT` | `INFO` | `0.2061` | 11,281.91 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 11.28K USD at 0.2061 USD [API] | `2026-10-28 22:44:33` |


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
| `Live` | `Long Liquidation` | `0.0405` | 207.36 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,050.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 1,240.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 103.16 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 6,930.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 481.50 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,610.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 155.12 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 7,300.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 3,760.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 111.86 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 160,200.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 1,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 157.83 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 1,610.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 935.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 6,940.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 793.42 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 454.62 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 111.86 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,730.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 28,660.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 150.21 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 2,080.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 5,300.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 290.36 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 2,120.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 12,990.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 100.02 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 565.51 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 11,090.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 902.88 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 105,520.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 1,890.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 882.93 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 4,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 2,050.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,720.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 33,400.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 981.95 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 77,210.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 1,970.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 3,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 12,520.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 216.56 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,120.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 138.61 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 602,410.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 4,200.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 65,290.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,040.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,540.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 241.46 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,120.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 13,630.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 78,180.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 625,360.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,180,000.00 USD | 4,180,000.00 USD | 29,110.00 USD | 2,020.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 423,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 4,140,000.00 USD | 4,140,000.00 USD | 10,810.00 USD | 837.36 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 35,220.00 USD | 170,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 4,080,000.00 USD | 4,080,000.00 USD | 5,710.00 USD | 7,590.00 USD | 28,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 4,020.00 USD | 135,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 4,040,000.00 USD | 4,040,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 131,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1750` | 4,030,000.00 USD | 4,030,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1760` | 4,010,000.00 USD | 4,010,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,990.00 USD | 130,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,920,000.00 USD | 3,920,000.00 USD | 54,620.00 USD | 20,340.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 16,020.00 USD | 125,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,760,000.00 USD | 3,760,000.00 USD | 69,710.00 USD | 35,540.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 2,480.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,590,000.00 USD | 3,590,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 873.09 USD | 106,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 3,420,000.00 USD | 3,420,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 55,280.00 USD | 105,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 3,270,000.00 USD | 3,270,000.00 USD | 50,420.00 USD | 27,730.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 15,750.00 USD | 50,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 3,150,000.00 USD | 3,150,000.00 USD | 159,050.00 USD | 14,270.00 USD | 72,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 27,520.00 USD | 34,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 2,910,000.00 USD | 2,910,000.00 USD | 72,410.00 USD | 24,810.00 USD | 133,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 827.59 USD | 7,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 2,670,000.00 USD | 2,670,000.00 USD | 113,190.00 USD | 50,780.00 USD | 145,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,240.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 2,370,000.00 USD | 2,370,000.00 USD | 110,780.00 USD | 66,490.00 USD | 179,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 2,010,000.00 USD | 2,010,000.00 USD | 228,970.00 USD | 8,970.00 USD | 94,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 3,740.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 1,680,000.00 USD | 1,680,000.00 USD | 178,050.00 USD | 55,340.00 USD | 277,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 451.69 USD | 451.69 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `0.1960` | 1,530,000.00 USD | 1,530,000.00 USD | 77,200.00 USD | 221,440.00 USD | 253,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 2,020,000.00 USD | 2,020,000.00 USD | 179,990.00 USD | 3,990.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1990` | 2,330,000.00 USD | 2,330,000.00 USD | 88,240.00 USD | 40,300.00 USD | 185,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 252.97 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 2,890,000.00 USD | 2,890,000.00 USD | 225,870.00 USD | 37,570.00 USD | 297,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2010` | 3,440,000.00 USD | 3,440,000.00 USD | 112,020.00 USD | 136,420.00 USD | 302,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 104.78 USD | 357.75 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.2125` | 2,580.00 USD | 2,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,740,000.00 USD | 9,740,000.00 USD | 210,380.00 USD | 58,850.00 USD | 87,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 10,110,000.00 USD | 10,110,000.00 USD | 196,360.00 USD | 58,130.00 USD | 110,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 10,150,000.00 USD | 10,150,000.00 USD | 31,260.00 USD | 8,690.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 6,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 8,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 8,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 10,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 20,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 20,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 28,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 29,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 30,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2435` | 635.78 USD | 31,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,370.00 USD | 59,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 59,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 1,400.00 USD | 61,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 298.11 USD | 61,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 62,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 425.73 USD | 62,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 2,590.00 USD | 65,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 67,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 67,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 70,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 71,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 79,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2965` | 72,390.00 USD | 151,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 151,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 152,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,310.00 USD | 249,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 4,220.00 USD | 253,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 40,020.00 USD | 293,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3195` | 1,120.00 USD | 295,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3205` | 3,860.00 USD | 298,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 1,390.00 USD | 300,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 346,230.00 USD | 646,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3315` | 237.35 USD | 646,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 748.71 USD | 647,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3435` | 326.33 USD | 647,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3455` | 154.44 USD | 647,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3465` | 317.05 USD | 648,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3525` | 141.35 USD | 648,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3595` | 914.21 USD | 649,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3605` | 2,450.00 USD | 651,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 1,950.00 USD | 653,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3645` | 209,740.00 USD | 863,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3705` | 267,040.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3725` | 116.59 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0415` | 2,330,000.00 USD | 0.00 USD | 116.66 USD | `-77.81%` | `2,811.00` |
| `Live` | `Long` | `0.0435` | 2,330,000.00 USD | 0.00 USD | 863.21 USD | `-76.74%` | `19,844.00` |
| `Live` | `Long` | `0.0565` | 2,330,000.00 USD | 0.00 USD | 289.28 USD | `-69.79%` | `5,120.00` |
| `Live` | `Long` | `0.0575` | 2,320,000.00 USD | 0.00 USD | 306.94 USD | `-69.25%` | `5,338.00` |
| `Live` | `Long` | `0.0585` | 2,320,000.00 USD | 0.00 USD | 526.50 USD | `-68.72%` | `9,000.00` |
| `Live` | `Long` | `0.0645` | 2,320,000.00 USD | 0.00 USD | 1,720.00 USD | `-65.51%` | `26,617.00` |
| `Live` | `Long` | `0.0725` | 2,320,000.00 USD | 0.00 USD | 363.08 USD | `-61.23%` | `5,008.00` |
| `Live` | `Long` | `0.0745` | 2,320,000.00 USD | 0.00 USD | 18,250.00 USD | `-60.16%` | `245,008.00` |
| `Live` | `Long` | `0.0785` | 2,300,000.00 USD | 0.00 USD | 1,870.00 USD | `-58.02%` | `23,814.00` |
| `Live` | `Long` | `0.0815` | 2,300,000.00 USD | 0.00 USD | 284.84 USD | `-56.42%` | `3,495.00` |
| `Live` | `Long` | `0.0865` | 2,300,000.00 USD | 0.00 USD | 4,290.00 USD | `-53.75%` | `49,629.00` |
| `Live` | `Long` | `0.0875` | 2,300,000.00 USD | 0.00 USD | 344.75 USD | `-53.21%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,300,000.00 USD | 0.00 USD | 1,150.00 USD | `-52.68%` | `13,050.00` |
| `Live` | `Long` | `0.0915` | 2,300,000.00 USD | 0.00 USD | 1,430.00 USD | `-51.07%` | `15,628.00` |
| `Live` | `Long` | `0.0925` | 2,290,000.00 USD | 0.00 USD | 173,480.00 USD | `-50.54%` | `1,875,488.00` |
| `Live` | `Long` | `0.0945` | 2,120,000.00 USD | 0.00 USD | 327.54 USD | `-49.47%` | `3,466.00` |
| `Live` | `Long` | `0.0965` | 2,120,000.00 USD | 0.00 USD | 965.00 USD | `-48.40%` | `10,000.00` |
| `Live` | `Long` | `0.0995` | 2,120,000.00 USD | 0.00 USD | 342.58 USD | `-46.79%` | `3,443.00` |
| `Live` | `Long` | `0.1025` | 2,120,000.00 USD | 0.00 USD | 4,100.00 USD | `-45.19%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,120,000.00 USD | 0.00 USD | 1,230.00 USD | `-44.66%` | `11,893.00` |
| `Live` | `Long` | `0.1045` | 2,110,000.00 USD | 0.00 USD | 2,090.00 USD | `-44.12%` | `20,000.00` |
| `Live` | `Long` | `0.1055` | 2,110,000.00 USD | 0.00 USD | 150.44 USD | `-43.59%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,110,000.00 USD | 0.00 USD | 653.70 USD | `-43.05%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,110,000.00 USD | 0.00 USD | 475.58 USD | `-42.52%` | `4,424.00` |
| `Live` | `Long` | `0.1095` | 2,110,000.00 USD | 0.00 USD | 1,490.00 USD | `-41.45%` | `13,608.00` |
| `Live` | `Long` | `0.1135` | 2,110,000.00 USD | 0.00 USD | 117.02 USD | `-39.31%` | `1,031.00` |
| `Live` | `Long` | `0.1145` | 2,110,000.00 USD | 0.00 USD | 862.64 USD | `-38.77%` | `7,534.00` |
| `Live` | `Long` | `0.1155` | 2,110,000.00 USD | 0.00 USD | 102.10 USD | `-38.24%` | `884.00` |
| `Live` | `Long` | `0.1165` | 2,110,000.00 USD | 0.00 USD | 13,510.00 USD | `-37.70%` | `115,947.00` |
| `Live` | `Long` | `0.1175` | 2,090,000.00 USD | 0.00 USD | 6,270.00 USD | `-37.17%` | `53,337.00` |
| `Live` | `Long` | `0.1205` | 2,090,000.00 USD | 0.00 USD | 826.27 USD | `-35.56%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,090,000.00 USD | 0.00 USD | 1,050.00 USD | `-35.03%` | `8,652.00` |
| `Live` | `Long` | `0.1245` | 2,090,000.00 USD | 0.00 USD | 404.62 USD | `-33.43%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,090,000.00 USD | 0.00 USD | 1,980.00 USD | `-32.89%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,080,000.00 USD | 0.00 USD | 314.61 USD | `-32.36%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,080,000.00 USD | 0.00 USD | 1,260.00 USD | `-31.82%` | `9,873.00` |
| `Live` | `Long` | `0.1285` | 2,080,000.00 USD | 0.00 USD | 407.09 USD | `-31.29%` | `3,168.00` |
| `Live` | `Long` | `0.1295` | 2,080,000.00 USD | 0.00 USD | 2,640.00 USD | `-30.75%` | `20,424.00` |
| `Live` | `Long` | `0.1305` | 2,080,000.00 USD | 0.00 USD | 12,700.00 USD | `-30.22%` | `97,328.00` |
| `Live` | `Long` | `0.1315` | 2,070,000.00 USD | 0.00 USD | 687.35 USD | `-29.68%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,070,000.00 USD | 0.00 USD | 6,960.00 USD | `-29.15%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,060,000.00 USD | 0.00 USD | 5,700.00 USD | `-28.61%` | `42,702.00` |
| `Live` | `Long` | `0.1355` | 2,050,000.00 USD | 0.00 USD | 740.91 USD | `-27.54%` | `5,468.00` |
| `Live` | `Long` | `0.1375` | 2,050,000.00 USD | 0.00 USD | 31,620.00 USD | `-26.47%` | `229,972.00` |
| `Live` | `Long` | `0.1405` | 2,020,000.00 USD | 0.00 USD | 314.44 USD | `-24.87%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,020,000.00 USD | 0.00 USD | 10,880.00 USD | `-24.34%` | `76,921.00` |
| `Live` | `Long` | `0.1425` | 2,010,000.00 USD | 0.00 USD | 958.46 USD | `-23.80%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,010,000.00 USD | 0.00 USD | 15,780.00 USD | `-23.27%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 1,990,000.00 USD | 0.00 USD | 1,890.00 USD | `-22.73%` | `13,058.00` |
| `Live` | `Long` | `0.1455` | 1,990,000.00 USD | 0.00 USD | 3,770.00 USD | `-22.20%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 1,990,000.00 USD | 0.00 USD | 31,680.00 USD | `-21.66%` | `216,277.00` |
| `Live` | `Long` | `0.1475` | 1,960,000.00 USD | 0.00 USD | 292.94 USD | `-21.13%` | `1,986.00` |
| `Live` | `Long` | `0.1485` | 1,960,000.00 USD | 0.00 USD | 1,360.00 USD | `-20.59%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 1,950,000.00 USD | 0.00 USD | 138.14 USD | `-20.06%` | `924.00` |
| `Live` | `Long` | `0.1505` | 1,950,000.00 USD | 0.00 USD | 3,100.00 USD | `-19.52%` | `20,629.00` |
| `Live` | `Long` | `0.1515` | 1,950,000.00 USD | 0.00 USD | 35,710.00 USD | `-18.99%` | `235,729.00` |
| `Live` | `Long` | `0.1525` | 1,920,000.00 USD | 0.00 USD | 8,660.00 USD | `-18.45%` | `56,812.00` |
| `Live` | `Long` | `0.1535` | 1,910,000.00 USD | 0.00 USD | 152,600.00 USD | `-17.92%` | `994,165.00` |
| `Live` | `Long` | `0.1545` | 1,750,000.00 USD | 0.00 USD | 1,180.00 USD | `-17.38%` | `7,625.00` |
| `Live` | `Long` | `0.1555` | 1,750,000.00 USD | 0.00 USD | 1,020.00 USD | `-16.85%` | `6,587.00` |
| `Live` | `Long` | `0.1565` | 1,750,000.00 USD | 0.00 USD | 10,860.00 USD | `-16.31%` | `69,381.00` |
| `Live` | `Long` | `0.1575` | 1,740,000.00 USD | 0.00 USD | 4,650.00 USD | `-15.78%` | `29,511.00` |
| `Live` | `Long` | `0.1585` | 1,740,000.00 USD | 0.00 USD | 9,170.00 USD | `-15.25%` | `57,842.00` |
| `Live` | `Long` | `0.1595` | 1,730,000.00 USD | 0.00 USD | 138.61 USD | `-14.71%` | `869.00` |
| `Live` | `Long` | `0.1605` | 1,730,000.00 USD | 0.00 USD | 60,380.00 USD | `-14.18%` | `376,194.00` |
| `Live` | `Long` | `0.1615` | 1,670,000.00 USD | 0.00 USD | 4,880.00 USD | `-13.64%` | `30,216.00` |
| `Live` | `Long` | `0.1625` | 1,660,000.00 USD | 0.00 USD | 551,250.00 USD | `-13.11%` | `3,392,288.00` |
| `Live` | `Long` | `0.1645` | 1,110,000.00 USD | 0.00 USD | 12,700.00 USD | `-12.04%` | `77,233.00` |
| `Live` | `Long` | `0.1665` | 1,100,000.00 USD | 0.00 USD | 889.94 USD | `-10.97%` | `5,345.00` |
| `Live` | `Long` | `0.1675` | 1,100,000.00 USD | 0.00 USD | 1,650.00 USD | `-10.43%` | `9,874.00` |
| `Live` | `Long` | `0.1685` | 1,090,000.00 USD | 0.00 USD | 12,160.00 USD | `-9.90%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,080,000.00 USD | 0.00 USD | 78,180.00 USD | `-9.36%` | `461,249.00` |
| `Live` | `Long` | `0.1705` | 1,000,000.00 USD | 0.00 USD | 626,600.00 USD | `-8.83%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 378,050.00 USD | 0.00 USD | 252,270.00 USD | `-8.29%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 125,780.00 USD | 0.00 USD | 33,550.00 USD | `-7.76%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 92,230.00 USD | 0.00 USD | 1,270.00 USD | `-7.22%` | `7,296.00` |
| `Live` | `Long` | `0.1745` | 90,960.00 USD | 0.00 USD | 234.18 USD | `-6.69%` | `1,342.00` |
| `Live` | `Long` | `0.1755` | 90,730.00 USD | 0.00 USD | 17,080.00 USD | `-6.15%` | `97,295.00` |
| `Live` | `Long` | `0.1765` | 73,650.00 USD | 0.00 USD | 43,700.00 USD | `-5.62%` | `247,592.00` |
| `Live` | `Long` | `0.1775` | 29,950.00 USD | 0.00 USD | 1,230.00 USD | `-5.09%` | `6,907.00` |
| `Live` | `Long` | `0.1785` | 28,730.00 USD | 0.00 USD | 4,530.00 USD | `-4.55%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 24,200.00 USD | 0.00 USD | 1,120.00 USD | `-4.02%` | `6,234.00` |
| `Live` | `Long` | `0.1805` | 23,080.00 USD | 0.00 USD | 5,220.00 USD | `-3.48%` | `28,904.00` |
| `Live` | `Long` | `0.1815` | 17,860.00 USD | 0.00 USD | 11,080.00 USD | `-2.95%` | `61,030.00` |
| `Live` | `Long` | `0.1825` | 6,780.00 USD | 0.00 USD | 6,780.00 USD | `-2.41%` | `37,172.00` |
| `Live` | `Short` | `0.1955` | 152.49 USD | 152.49 USD | 0.00 USD | `+4.54%` | `780.00` |
| `Live` | `Short` | `0.1975` | 349.99 USD | 197.50 USD | 0.00 USD | `+5.61%` | `1,000.00` |
| `Live` | `Short` | `0.1985` | 688.63 USD | 338.64 USD | 0.00 USD | `+6.14%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 941.60 USD | 252.97 USD | 0.00 USD | `+6.68%` | `1,268.00` |
| `Live` | `Short` | `0.2015` | 3,040.00 USD | 2,100.00 USD | 0.00 USD | `+7.75%` | `10,418.00` |
| `Live` | `Short` | `0.2125` | 5,620.00 USD | 2,580.00 USD | 0.00 USD | `+13.63%` | `12,141.00` |
| `Live` | `Short` | `0.2145` | 6,020.00 USD | 398.11 USD | 0.00 USD | `+14.70%` | `1,856.00` |
| `Live` | `Short` | `0.2175` | 9,950.00 USD | 3,930.00 USD | 0.00 USD | `+16.30%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 12,600.00 USD | 2,650.00 USD | 0.00 USD | `+16.84%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 14,240.00 USD | 1,640.00 USD | 0.00 USD | `+18.44%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 14,450.00 USD | 200.48 USD | 0.00 USD | `+19.51%` | `897.00` |
| `Live` | `Short` | `0.2265` | 16,680.00 USD | 2,230.00 USD | 0.00 USD | `+21.12%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 25,910.00 USD | 9,240.00 USD | 0.00 USD | `+22.19%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 26,200.00 USD | 282.02 USD | 0.00 USD | `+24.32%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 33,830.00 USD | 7,640.00 USD | 0.00 USD | `+24.86%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 35,300.00 USD | 1,470.00 USD | 0.00 USD | `+28.60%` | `6,110.00` |
| `Live` | `Short` | `0.2415` | 35,850.00 USD | 543.62 USD | 0.00 USD | `+29.14%` | `2,251.00` |
| `Live` | `Short` | `0.2425` | 36,920.00 USD | 1,080.00 USD | 0.00 USD | `+29.67%` | `4,435.00` |
| `Live` | `Short` | `0.2475` | 37,570.00 USD | 646.22 USD | 0.00 USD | `+32.35%` | `2,611.00` |
| `Live` | `Short` | `0.2585` | 37,950.00 USD | 380.25 USD | 0.00 USD | `+38.23%` | `1,471.00` |
| `Live` | `Short` | `0.2715` | 38,370.00 USD | 418.11 USD | 0.00 USD | `+45.18%` | `1,540.00` |
| `Live` | `Short` | `0.2775` | 38,750.00 USD | 379.62 USD | 0.00 USD | `+48.39%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 40,920.00 USD | 2,170.00 USD | 0.00 USD | `+52.13%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 41,330.00 USD | 411.09 USD | 0.00 USD | `+54.80%` | `1,420.00` |
| `Live` | `Short` | `0.2905` | 42,570.00 USD | 1,240.00 USD | 0.00 USD | `+55.34%` | `4,254.00` |
| `Live` | `Short` | `0.2915` | 110,140.00 USD | 67,580.00 USD | 0.00 USD | `+55.87%` | `231,824.00` |
| `Live` | `Short` | `0.2935` | 110,660.00 USD | 519.79 USD | 0.00 USD | `+56.94%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 118,650.00 USD | 7,990.00 USD | 0.00 USD | `+58.01%` | `27,027.00` |
| `Live` | `Short` | `0.2975` | 118,840.00 USD | 189.21 USD | 0.00 USD | `+59.08%` | `636.00` |
| `Live` | `Short` | `0.3005` | 118,990.00 USD | 146.34 USD | 0.00 USD | `+60.69%` | `487.00` |
| `Live` | `Short` | `0.3025` | 123,070.00 USD | 4,080.00 USD | 0.00 USD | `+61.76%` | `13,504.00` |
| `Live` | `Short` | `0.3045` | 129,020.00 USD | 5,950.00 USD | 0.00 USD | `+62.83%` | `19,542.00` |
| `Live` | `Short` | `0.3055` | 129,430.00 USD | 408.15 USD | 0.00 USD | `+63.36%` | `1,336.00` |
| `Live` | `Short` | `0.3125` | 226,940.00 USD | 97,510.00 USD | 0.00 USD | `+67.10%` | `312,021.00` |
| `Live` | `Short` | `0.3155` | 230,550.00 USD | 3,610.00 USD | 0.00 USD | `+68.71%` | `11,458.00` |
| `Live` | `Short` | `0.3185` | 230,750.00 USD | 200.34 USD | 0.00 USD | `+70.31%` | `629.00` |
| `Live` | `Short` | `0.3195` | 230,890.00 USD | 142.82 USD | 0.00 USD | `+70.85%` | `447.00` |
| `Live` | `Short` | `0.3235` | 231,070.00 USD | 172.43 USD | 0.00 USD | `+72.99%` | `533.00` |
| `Live` | `Short` | `0.3295` | 234,240.00 USD | 3,180.00 USD | 0.00 USD | `+76.19%` | `9,639.00` |
| `Live` | `Short` | `0.3305` | 272,880.00 USD | 38,640.00 USD | 0.00 USD | `+76.73%` | `116,921.00` |
| `Live` | `Short` | `0.3315` | 275,800.00 USD | 2,910.00 USD | 0.00 USD | `+77.26%` | `8,785.00` |
| `Live` | `Short` | `0.3425` | 276,040.00 USD | 245.23 USD | 0.00 USD | `+83.15%` | `716.00` |
| `Live` | `Short` | `0.3445` | 524,340.00 USD | 248,300.00 USD | 0.00 USD | `+84.21%` | `720,753.00` |
| `Live` | `Short` | `0.3465` | 524,480.00 USD | 138.95 USD | 0.00 USD | `+85.28%` | `401.00` |
| `Live` | `Short` | `0.3485` | 524,700.00 USD | 221.65 USD | 0.00 USD | `+86.35%` | `636.00` |
| `Live` | `Short` | `0.3505` | 726,380.00 USD | 201,680.00 USD | 0.00 USD | `+87.42%` | `575,408.00` |
| `Live` | `Short` | `0.3515` | 727,840.00 USD | 1,450.00 USD | 0.00 USD | `+87.96%` | `4,132.00` |
| `Live` | `Short` | `0.3585` | 728,160.00 USD | 328.03 USD | 0.00 USD | `+91.70%` | `915.00` |
| `Live` | `Short` | `0.3595` | 729,080.00 USD | 914.21 USD | 0.00 USD | `+92.24%` | `2,543.00` |
| `Live` | `Short` | `0.3615` | 732,020.00 USD | 2,940.00 USD | 0.00 USD | `+93.31%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 732,160.00 USD | 143.91 USD | 0.00 USD | `+93.84%` | `397.00` |
| `Live` | `Short` | `0.3635` | 734,860.00 USD | 2,700.00 USD | 0.00 USD | `+94.37%` | `7,433.00` |
| `Live` | `Short` | `0.3655` | 735,210.00 USD | 347.22 USD | 0.00 USD | `+95.44%` | `950.00` |
| `Live` | `Short` | `0.3715` | 744,380.00 USD | 9,170.00 USD | 0.00 USD | `+98.65%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 747,530.00 USD | 3,140.00 USD | 0.00 USD | `+100.26%` | `8,395.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 185,360,000.00 USD | 0.00 USD | 415.13 USD | `-68.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 185,360,000.00 USD | 0.00 USD | 438.99 USD | `-67.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 185,360,000.00 USD | 0.00 USD | 1,100.00 USD | `-40.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 185,360,000.00 USD | 0.00 USD | 541.33 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 185,360,000.00 USD | 0.00 USD | 429.20 USD | `-38.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 185,360,000.00 USD | 0.00 USD | 602,500.00 USD | `-35.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 184,760,000.00 USD | 0.00 USD | 4,460.00 USD | `-33.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 184,750,000.00 USD | 0.00 USD | 1,320.00 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 184,750,000.00 USD | 0.00 USD | 13,390.00 USD | `-30.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 184,740,000.00 USD | 0.00 USD | 728.88 USD | `-29.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 184,740,000.00 USD | 0.00 USD | 4,350.00 USD | `-28.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 184,730,000.00 USD | 0.00 USD | 4,730.00 USD | `-26.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 184,730,000.00 USD | 0.00 USD | 1,820.00 USD | `-25.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 184,720,000.00 USD | 0.00 USD | 1,050.00 USD | `-24.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 184,720,000.00 USD | 0.00 USD | 351.26 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 184,720,000.00 USD | 0.00 USD | 1,600.00 USD | `-23.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 184,720,000.00 USD | 0.00 USD | 10,400.00 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 184,710,000.00 USD | 0.00 USD | 5,980.00 USD | `-20.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 184,710,000.00 USD | 0.00 USD | 303.26 USD | `-19.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 184,700,000.00 USD | 0.00 USD | 1,290.00 USD | `-18.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 184,700,000.00 USD | 0.00 USD | 6,380.00 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 184,700,000.00 USD | 0.00 USD | 126.54 USD | `-17.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 184,700,000.00 USD | 0.00 USD | 1,790.00 USD | `-16.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 184,700,000.00 USD | 0.00 USD | 6,260.00 USD | `-16.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 184,690,000.00 USD | 0.00 USD | 552.21 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 184,690,000.00 USD | 0.00 USD | 166.84 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 184,690,000.00 USD | 0.00 USD | 9,410.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 184,680,000.00 USD | 0.00 USD | 769.39 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 184,680,000.00 USD | 0.00 USD | 24,760.00 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 184,650,000.00 USD | 0.00 USD | 6,540.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 184,650,000.00 USD | 0.00 USD | 2,870.00 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 184,640,000.00 USD | 0.00 USD | 5,670.00 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 184,640,000.00 USD | 0.00 USD | 8,020.00 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 184,630,000.00 USD | 0.00 USD | 951.90 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 184,630,000.00 USD | 0.00 USD | 4,960.00 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 184,620,000.00 USD | 0.00 USD | 1,930.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 184,620,000.00 USD | 0.00 USD | 582.93 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 184,620,000.00 USD | 0.00 USD | 103.58 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 184,620,000.00 USD | 0.00 USD | 74,710.00 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 184,550,000.00 USD | 0.00 USD | 1,760.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 184,550,000.00 USD | 0.00 USD | 847.38 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 184,540,000.00 USD | 0.00 USD | 4,910.00 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 184,540,000.00 USD | 0.00 USD | 5,400.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 184,530,000.00 USD | 0.00 USD | 4,270.00 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 184,530,000.00 USD | 0.00 USD | 1,570.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 184,530,000.00 USD | 0.00 USD | 2,720.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 184,530,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-2.41%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 148,020,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-1.88%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 74,620,000.00 USD | 0.00 USD | 18,800.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 74,610,000.00 USD | 0.00 USD | 5,850.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 74,600,000.00 USD | 0.00 USD | 74,600,000.00 USD | `-0.27%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.1875` | 3,580.00 USD | 3,580.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 6,680.00 USD | 3,100.00 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 9,000.00 USD | 2,320.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 9,510.00 USD | 503.49 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 12,900.00 USD | 3,390.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 13,260.00 USD | 362.29 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 13,520.00 USD | 263.55 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 13,910.00 USD | 389.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 14,160.00 USD | 247.89 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 17,820.00 USD | 3,660.00 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 18,820.00 USD | 1,000.00 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 19,470.00 USD | 646.71 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 19,860.00 USD | 399.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 30,400.00 USD | 10,540.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 76,740.00 USD | 46,340.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 77,330.00 USD | 594.34 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 79,590.00 USD | 2,250.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 82,280.00 USD | 2,690.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 84,430.00 USD | 2,160.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 84,640.00 USD | 207.74 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 84,950.00 USD | 312.70 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 93,290.00 USD | 8,340.00 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 101,210.00 USD | 7,920.00 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 123,280.00 USD | 22,070.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 143,260.00 USD | 19,980.00 USD | 0.00 USD | `+13.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 149,960.00 USD | 6,700.00 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 154,160.00 USD | 4,190.00 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 155,120.00 USD | 965.25 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 165,430.00 USD | 10,300.00 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 165,910.00 USD | 487.34 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 166,020.00 USD | 109.91 USD | 0.00 USD | `+16.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 181,480.00 USD | 15,460.00 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 184,250.00 USD | 2,760.00 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 185,890.00 USD | 1,650.00 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 194,900.00 USD | 9,010.00 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 198,650.00 USD | 3,750.00 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 198,770.00 USD | 114.50 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 199,110.00 USD | 339.60 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 199,220.00 USD | 109.40 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 208,320.00 USD | 9,100.00 USD | 0.00 USD | `+21.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 217,460.00 USD | 9,140.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 218,120.00 USD | 662.92 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 218,460.00 USD | 337.06 USD | 0.00 USD | `+23.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 218,630.00 USD | 171.12 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 218,730.00 USD | 101.11 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 219,800.00 USD | 1,070.00 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 229,220.00 USD | 9,420.00 USD | 0.00 USD | `+25.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 229,530.00 USD | 315.96 USD | 0.00 USD | `+26.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 230,310.00 USD | 778.76 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 230,500.00 USD | 192.71 USD | 0.00 USD | `+27.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 231,020.00 USD | 514.45 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 231,230.00 USD | 209.72 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 231,340.00 USD | 115.92 USD | 0.00 USD | `+29.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 231,580.00 USD | 236.19 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 232,730.00 USD | 1,150.00 USD | 0.00 USD | `+30.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 233,020.00 USD | 288.22 USD | 0.00 USD | `+31.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 233,510.00 USD | 491.03 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 234,830.00 USD | 1,320.00 USD | 0.00 USD | `+32.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 244,770.00 USD | 9,940.00 USD | 0.00 USD | `+32.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 245,270.00 USD | 499.00 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 246,370.00 USD | 1,100.00 USD | 0.00 USD | `+33.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 246,540.00 USD | 168.76 USD | 0.00 USD | `+34.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 247,140.00 USD | 603.73 USD | 0.00 USD | `+35.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 249,320.00 USD | 2,170.00 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 250,880.00 USD | 1,570.00 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 252,350.00 USD | 1,470.00 USD | 0.00 USD | `+37.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 252,620.00 USD | 271.44 USD | 0.00 USD | `+38.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 673,530.00 USD | 420,910.00 USD | 0.00 USD | `+39.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 674,710.00 USD | 1,180.00 USD | 0.00 USD | `+41.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 683,610.00 USD | 8,890.00 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 698,470.00 USD | 14,860.00 USD | 0.00 USD | `+43.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 699,810.00 USD | 1,340.00 USD | 0.00 USD | `+44.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 702,520.00 USD | 2,710.00 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 716,390.00 USD | 13,870.00 USD | 0.00 USD | `+46.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 721,600.00 USD | 5,220.00 USD | 0.00 USD | `+46.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 722,780.00 USD | 1,170.00 USD | 0.00 USD | `+48.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 726,930.00 USD | 4,150.00 USD | 0.00 USD | `+48.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 727,870.00 USD | 944.99 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 728,030.00 USD | 161.87 USD | 0.00 USD | `+51.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 728,150.00 USD | 113.68 USD | 0.00 USD | `+51.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 729,520.00 USD | 1,370.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 730,600.00 USD | 1,080.00 USD | 0.00 USD | `+53.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 745,580.00 USD | 14,980.00 USD | 0.00 USD | `+55.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 746,820.00 USD | 1,230.00 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 748,260.00 USD | 1,440.00 USD | 0.00 USD | `+59.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 748,620.00 USD | 355.21 USD | 0.00 USD | `+60.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 755,270.00 USD | 6,650.00 USD | 0.00 USD | `+60.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 774,250.00 USD | 18,980.00 USD | 0.00 USD | `+63.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 778,400.00 USD | 4,150.00 USD | 0.00 USD | `+64.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 781,640.00 USD | 3,250.00 USD | 0.00 USD | `+68.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 782,140.00 USD | 493.89 USD | 0.00 USD | `+73.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 782,320.00 USD | 181.30 USD | 0.00 USD | `+74.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 783,700.00 USD | 1,380.00 USD | 0.00 USD | `+76.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 795,990.00 USD | 12,290.00 USD | 0.00 USD | `+77.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 796,100.00 USD | 111.06 USD | 0.00 USD | `+78.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 796,320.00 USD | 220.61 USD | 0.00 USD | `+82.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 799,660.00 USD | 3,340.00 USD | 0.00 USD | `+86.89%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `402.16M` | Total OI Tokens: `2,137,744,372.1 ADA`
  * 1h OI Change: `+0.21%` | 4h OI Change: `-3.38%` | 24h OI Change: `-8.47%`
  * Exchange Breakdown: Binance=`75.07M` | Bybit=`49.32M` | OKX=`28.49M` | Hyperliquid=`27.62M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.29K` | Last 24h: `10.44K` | Last 3d: `50.88K` | Last 7d: `82.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0078%` | **USDT OKX** | `0.0030%` |
| **USDT Bybit** | `-0.0144%` | **USDT KuCoin** | `-0.0011%` |
| **USDT MEXC** | `0.0074%` | **USDT BingX** | `0.0090%` |
| **USDT Gate** | `-0.0067%` | **USDT Bitget** | `0.0094%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `42.82%` | `57.18%` | `0.75` | 55,210,000.00 USD |
| `15M` | `Binance` | `46.5%` | `53.5%` | `0.87` | 19,140,000.00 USD |
| `15M` | `OKX` | `41.93%` | `58.07%` | `0.72` | 4,990,000.00 USD |
| `15M` | `Bybit` | `39.96%` | `60.04%` | `0.67` | 9,200,000.00 USD |
| `15M` | `KuCoin` | `35.87%` | `64.13%` | `0.56` | 850,680.00 USD |
| `15M` | `Gate` | `60.4%` | `39.6%` | `1.53` | 1,120,000.00 USD |
| `15M` | `Bitget` | `58.73%` | `41.27%` | `1.42` | 3,820,000.00 USD |
| `15M` | `BingX` | `57.44%` | `42.56%` | `1.35` | 324,360.00 USD |
| `15M` | `MEXC` | `43.9%` | `56.1%` | `0.78` | 5,390,000.00 USD |
| `15M` | `Bitunix` | `45.17%` | `54.83%` | `0.82` | 1,970,000.00 USD |
| `15M` | `Hyperliquid` | `15.92%` | `84.08%` | `0.19` | 6,750,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `64.14%` | `35.86%` | `1.79` | 203,990.00 USD |
| `15M` | `Crypto.com` | `45.92%` | `54.08%` | `0.85` | 85,970.00 USD |
| `15M` | `WhiteBIT` | `96.98%` | `3.02%` | `32.11` | 704,760.00 USD |
| `15M` | `HTX` | `71.77%` | `28.23%` | `2.54` | 126,050.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.25%` | `53.75%` | `0.86` | 108,770.00 USD |
| `15M` | `Aster` | `39.28%` | `60.72%` | `0.65` | 253,200.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `78.93%` | `21.07%` | `3.75` | 172,160.00 USD |
| `15M` | `Whale Positions` | `46.5%` | `53.5%` | `0.87` | 19,140,000.00 USD |
| `15M` | `Global Accounts` | `42.82%` | `57.18%` | `0.75` | 55,210,000.00 USD |
| `1H` | `ADA` | `44.46%` | `55.54%` | `0.80` | 5,070,000,000.00 USD |
| `1H` | `Binance` | `44.46%` | `55.54%` | `0.80` | 1,660,000,000.00 USD |
| `1H` | `OKX` | `43.63%` | `56.37%` | `0.77` | 1,020,000,000.00 USD |
| `1H` | `Bybit` | `45.94%` | `54.06%` | `0.85` | 340,250,000.00 USD |
| `1H` | `KuCoin` | `56.65%` | `43.35%` | `1.31` | 66,930,000.00 USD |
| `1H` | `Gate` | `48.12%` | `51.88%` | `0.93` | 564,090,000.00 USD |
| `1H` | `Bitget` | `50.43%` | `49.57%` | `1.02` | 201,680,000.00 USD |
| `1H` | `BingX` | `49.09%` | `50.91%` | `0.96` | 43,990,000.00 USD |
| `1H` | `MEXC` | `43.3%` | `56.7%` | `0.76` | 170,510,000.00 USD |
| `1H` | `Bitunix` | `46.22%` | `53.78%` | `0.86` | 178,740,000.00 USD |
| `1H` | `Hyperliquid` | `54.07%` | `45.93%` | `1.18` | 245,330,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.32%` | `58.68%` | `0.70` | 12,460,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `28.39%` | `71.61%` | `0.40` | 353,810,000.00 USD |
| `1H` | `HTX` | `42.49%` | `57.51%` | `0.74` | 44,480,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.92%` | `50.08%` | `1.00` | 22,850,000.00 USD |
| `1H` | `Bitfinex` | `25.51%` | `74.49%` | `0.34` | 6,170,000.00 USD |
| `1H` | `Kraken` | `32.85%` | `67.15%` | `0.49` | 15,960,000.00 USD |
| `1H` | `Aster` | `44.69%` | `55.31%` | `0.81` | 55,170,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.41%` | `62.59%` | `0.60` | 64,100,000.00 USD |
| `1H` | `Whale Positions` | `44.46%` | `55.54%` | `0.80` | 1,660,000,000.00 USD |
| `1H` | `Global Accounts` | `44.46%` | `55.54%` | `0.80` | 5,070,000,000.00 USD |
| `4H` | `ADA` | `49.99%` | `50.01%` | `1.00` | 20,350,000,000.00 USD |
| `4H` | `Binance` | `45.72%` | `54.28%` | `0.84` | 5,950,000,000.00 USD |
| `4H` | `OKX` | `46.86%` | `53.14%` | `0.88` | 3,500,000,000.00 USD |
| `4H` | `Bybit` | `48.83%` | `51.17%` | `0.95` | 1,360,000,000.00 USD |
| `4H` | `KuCoin` | `56.41%` | `43.59%` | `1.29` | 205,320,000.00 USD |
| `4H` | `Gate` | `47.14%` | `52.86%` | `0.89` | 1,950,000,000.00 USD |
| `4H` | `Bitget` | `49.99%` | `50.01%` | `1.00` | 746,060,000.00 USD |
| `4H` | `BingX` | `48.48%` | `51.52%` | `0.94` | 173,530,000.00 USD |
| `4H` | `MEXC` | `47.68%` | `52.32%` | `0.91` | 678,940,000.00 USD |
| `4H` | `Bitunix` | `49.34%` | `50.66%` | `0.97` | 658,160,000.00 USD |
| `4H` | `Hyperliquid` | `47.27%` | `52.73%` | `0.90` | 979,570,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.72%` | `46.28%` | `1.16` | 52,510,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `65.48%` | `34.52%` | `1.90` | 3,310,000,000.00 USD |
| `4H` | `HTX` | `40.36%` | `59.64%` | `0.68` | 187,290,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `52.6%` | `47.4%` | `1.11` | 129,590,000.00 USD |
| `4H` | `Bitfinex` | `27.95%` | `72.05%` | `0.39` | 13,890,000.00 USD |
| `4H` | `Kraken` | `40.89%` | `59.11%` | `0.69` | 72,530,000.00 USD |
| `4H` | `Aster` | `45.77%` | `54.23%` | `0.84` | 172,820,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.39%` | `56.61%` | `0.77` | 196,290,000.00 USD |
| `4H` | `Whale Positions` | `45.72%` | `54.28%` | `0.84` | 5,950,000,000.00 USD |
| `4H` | `Global Accounts` | `49.99%` | `50.01%` | `1.00` | 20,350,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

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
| `5m` | 18,760.00 USD | -16,060.00 USD | **`ACCUMULATION`** |
| `15m` | 70,450.00 USD | 202,200.00 USD | **`ACCUMULATION`** |
| `30m` | -222,080.00 USD | 8,800.00 USD | **`DISTRIBUTION`** |
| `1h` | -428,180.00 USD | 1,440,000.00 USD | **`ACCUMULATION`** |
| `2h` | -2,070,000.00 USD | -3,400,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,200,000.00 USD | -1,800,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,810,000.00 USD | -12,850,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -8,050,000.00 USD | -13,820,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,520,000.00 USD | -11,450,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,390,000.00 USD | -11,420,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,640,000.00 USD | -40,300,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,300,000.00 USD | -199,630,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+18.76K` | 15m=`+70.45K` | 1h=`-428.18K` | 24h=`-9.39M`
* Futures Capital Netflows: 5m=`-16.06K` | 15m=`+202.20K` | 1h=`+1.44M` | 24h=`-11.42M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1861` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1799` (Risk Distance: `0.0062` pts)
  * +2.5R Take Profit: `0.2016`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1939` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.2001` (Risk Distance: `0.0062` pts)
  * +2.5R Take Profit: `0.1784`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1878`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
