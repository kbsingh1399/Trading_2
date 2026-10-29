# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:38:02 IST` (`2026-10-29 23:08:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1887` | **Live Ask Quote**: `0.1909` | **Mid Price**: `0.1898`
- **Spread Points**: `22.00` | **Spread BPS**: `115.91 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1974` | VWAP Z-Score: `-1.51` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0023` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.80` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2115` | Lower -3.00σ Band: `0.1833`
  * Upper +2.51σ Band: `0.2092` | Lower -2.51σ Band: `0.1856`
  * Upper +2.01σ Band: `0.2068` | Lower -2.01σ Band: `0.1880`
  * Upper +2.00σ Band: `0.2068` | Lower -2.00σ Band: `0.1880`
  * Upper +1.28σ Band: `0.2034` | Lower -1.28σ Band: `0.1914`
  * Upper +1.00σ Band: `0.2021` | Lower -1.00σ Band: `0.1927`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1919` | EMA-20=`0.1946` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1976` (Slope: `+0.0000`) | EMA-100=`0.1992`
  * Institutional Anchors: EMA-144=`0.1999` | EMA-200=`0.2007` (Slope: `-0.5451`) | EMA-233=`0.2012`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1862` | Weekly High=`0.2086` | Weekly Low=`0.1862`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1925` (Distance: `-1.29%`)
  * Point of Control (POC) = `0.1912` (Distance: `-0.61%`)
  * Value Area Low (VAL) = `0.1899` (Distance: `+0.07%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2057` | Weekly POC=`0.2031` | Weekly VAL=`0.2003`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1886`
  * London Session (08:00-16:00 UTC): High=`0.1906` | Low=`0.1890`
  * New York Session (13:00-21:00 UTC): High=`0.1909` | Low=`0.1887`
  * Initial Balance (First Hour): IB High=`0.1904` | IB Low=`0.1892`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1890` - `0.1906`
  * Optimal Trade Entry (OTE 0.705): `0.1902`
  * Structural Invalidation Anchor (0.786): `0.1913`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1917` | `0.1919` | `0.1911` | `0.1916` | `2,740,294` | 524,783.07 USD | 52,549.98 USD | `+10.01%` | -9,564,377.24 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1916` | `0.1919` | `0.1900` | `0.1903` | `8,298,193` | 1,583,190.44 USD | -188,070.08 USD | `-11.88%` | -9,752,447.32 USD | `-0.99` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1902` | `0.1904` | `0.1900` | `0.1901` | `1,714,127` | 326,072.50 USD | 12,293.36 USD | `+3.77%` | -9,740,153.96 USD | `+0.13` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1921` | `0.1937` | `0.1919` | `0.1924` | `13,638,032` | 2,630,885.00 USD | -106,426.19 USD | `-4.05%` | -9,533,486.99 USD | `+0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1925` | `0.1926` | `0.1911` | `0.1916` | `9,930,436` | 1,904,415.98 USD | -141,591.70 USD | `-7.43%` | -9,675,078.68 USD | `+0.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1916` | `0.1919` | `0.1900` | `0.1901` | `10,012,320` | 1,909,262.94 USD | -175,776.72 USD | `-9.21%` | -9,850,855.40 USD | `+0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1903` | `0.1953` | `0.1897` | `0.1921` | `118,898,936` | 22,899,002.06 USD | -718,669.23 USD | `-3.14%` | -9,772,234.94 USD | `-0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1922` | `0.1937` | `0.1894` | `0.1916` | `70,450,688` | 13,516,932.50 USD | -73,583.27 USD | `-0.54%` | -9,845,818.21 USD | `+0.10` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1916` | `0.1919` | `0.1900` | `0.1900` | `9,915,924` | 1,890,938.06 USD | -190,290.47 USD | `-10.06%` | -10,036,108.68 USD | `+0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1900` | `518,849,187` | 100,137,819.99 USD | -7,610,163.77 USD | `-7.60%` | -10,036,108.68 USD | `-1.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -5,414,333.03 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -4,633,383.98 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1900` | `518,849,187` | 100,137,819.99 USD | -7,610,163.77 USD | `-7.60%` | -10,036,108.68 USD | `-1.62` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1898`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `530` | `0x77ee...2902` | `SHORT` | 4,097,437.06 USD | `21,412,192.00` | `0.1911` | `0.1913` | `0.5574` | -6,185.32 USD | `-0.15%` | `10X Cross` |
| `1243` | `0x123d...3bff` | `LONG` | 1,798,166.75 USD | `9,393,142.00` | `0.2912` | `0.1913` | `0.000000` | -937,569.19 USD | `-52.14%` | `10X Cross` |
| `1273` | `0x7737...bf66` | `SHORT` | 1,739,833.85 USD | `9,091,466.00` | `0.2190` | `0.1913` | `2.01` | 251,155.95 USD | `+14.44%` | `10X Cross` |
| `1585` | `0x5f94...4b96` | `SHORT` | 1,371,369.03 USD | `7,162,318.00` | `0.2303` | `0.1913` | `0.7030` | 278,106.17 USD | `+20.28%` | `10X Cross` |
| `1801` | `0x4982...59e6` | `SHORT` | 1,147,872.68 USD | `5,998,812.00` | `0.1891` | `0.1913` | `0.4115` | -13,314.31 USD | `-1.16%` | `10X Cross` |
| `1844` | `0xcac1...26b3` | `LONG` | 1,112,032.41 USD | `5,803,927.00` | `0.2000` | `0.1913` | `0.000000` | -48,783.17 USD | `-4.39%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2011` | 5,393.43 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.39K USD at 0.2011 USD [API] | `2026-10-28 16:50:22` |
| `ANNOUNCEMENT` | `INFO` | `0.2026` | 6,648.22 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2026 USD [API] | `2026-10-28 17:46:02` |
| `ANNOUNCEMENT` | `INFO` | `0.2025` | 6,231.35 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.23K USD at 0.2025 USD [API] | `2026-10-28 17:45:39` |
| `ANNOUNCEMENT` | `INFO` | `0.2065` | 5,880.22 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.88K USD at 0.2065 USD [API] | `2026-10-28 19:46:53` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2100` (Vol: 191,800.00 USD, Dist: `+9.36%`) | Long MP=`0.1867` (Vol: 71,500.00 USD, Dist: `--2.78%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+8.98%`) | Long MP=`0.1867` (Vol: 71,500.00 USD, Dist: `--2.76%`)
  * 3D Horizon: Short MP=`0.2138` (Vol: 289,900.00 USD, Dist: `+11.38%`) | Long MP=`0.1867` (Vol: 71,500.00 USD, Dist: `--2.76%`)
  * 7D Horizon: Short MP=`0.2130` (Vol: 459,300.00 USD, Dist: `+10.96%`) | Long MP=`0.1907` (Vol: 143,000.00 USD, Dist: `--0.69%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0405` | 1,020.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 463.50 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 1,300.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 423.75 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 1,170.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 208.30 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 9,170.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 3,320.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 7,300.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 156,450.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 1,710.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 157.83 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 1,090.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 331.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 2,780.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 5,800.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 107.74 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 793.42 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 454.62 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 526.77 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 25,410.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 1,670.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 5,380.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 931.42 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,200.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 388.08 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 2,570.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 290.36 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 2,120.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 58,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 1,410.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 565.51 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,740.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 902.88 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 16,640.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 1,890.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 882.93 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 7,640.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 138.14 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 2,640.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 33,400.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 981.95 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 74,520.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,940.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 12,820.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 216.56 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 538,940.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 60,230.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 5,740.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,350.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,540.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 241.46 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,120.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 1,690.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 13,630.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 1,280.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 625,360.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,090,000.00 USD | 4,090,000.00 USD | 23,820.00 USD | 1,400.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 501,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 4,050,000.00 USD | 4,050,000.00 USD | 9,810.00 USD | 495.36 USD | 45,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 36,420.00 USD | 248,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 7,590.00 USD | 28,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,430.00 USD | 212,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 3,960,000.00 USD | 3,960,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,440.00 USD | 210,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1750` | 3,950,000.00 USD | 3,950,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 61,110.00 USD | 208,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 3,920,000.00 USD | 3,920,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,990.00 USD | 147,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,840,000.00 USD | 3,840,000.00 USD | 53,230.00 USD | 18,700.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,900.00 USD | 142,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,680,000.00 USD | 3,680,000.00 USD | 63,860.00 USD | 34,680.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 2,480.00 USD | 126,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,520,000.00 USD | 3,520,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 873.09 USD | 124,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 3,350,000.00 USD | 3,350,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 55,280.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 3,200,000.00 USD | 3,200,000.00 USD | 40,760.00 USD | 24,400.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 12,340.00 USD | 67,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 3,090,000.00 USD | 3,090,000.00 USD | 145,820.00 USD | 14,270.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 47,090.00 USD | 55,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 2,860,000.00 USD | 2,860,000.00 USD | 72,410.00 USD | 24,810.00 USD | 132,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 1,630.00 USD | 8,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 2,630,000.00 USD | 2,630,000.00 USD | 90,620.00 USD | 47,040.00 USD | 131,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,740.00 USD | 6,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 2,360,000.00 USD | 2,360,000.00 USD | 116,980.00 USD | 67,340.00 USD | 181,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 2,000,000.00 USD | 2,000,000.00 USD | 202,510.00 USD | 8,970.00 USD | 88,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 3,740.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 1,700,000.00 USD | 1,700,000.00 USD | 178,050.00 USD | 55,340.00 USD | 276,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 451.69 USD | 451.69 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 1,190,000.00 USD | 1,190,000.00 USD | 249,090.00 USD | 84,790.00 USD | 217,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 636,620.00 USD | 636,620.00 USD | 162,010.00 USD | 135,840.00 USD | 154,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 184,600.00 USD | 184,600.00 USD | 104,350.00 USD | 0.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 37,340.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 582,900.00 USD | 582,900.00 USD | 139,920.00 USD | 5,450.00 USD | 75,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 940,610.00 USD | 940,610.00 USD | 96,260.00 USD | 25,730.00 USD | 235,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,410,000.00 USD | 1,410,000.00 USD | 32,060.00 USD | 213,960.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 1,890,000.00 USD | 1,890,000.00 USD | 166,770.00 USD | 3,990.00 USD | 76,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1990` | 2,200,000.00 USD | 2,200,000.00 USD | 88,240.00 USD | 40,300.00 USD | 184,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2000` | 2,720,000.00 USD | 2,720,000.00 USD | 201,440.00 USD | 31,640.00 USD | 283,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 254.23 USD | 254.23 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 3,260,000.00 USD | 3,260,000.00 USD | 104,220.00 USD | 135,280.00 USD | 302,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 3,490,000.00 USD | 3,490,000.00 USD | 94,050.00 USD | 29,200.00 USD | 105,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 7,530.00 USD | 7,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 3,930,000.00 USD | 3,930,000.00 USD | 74,710.00 USD | 85,020.00 USD | 281,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2035` | 465.40 USD | 8,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2040` | 4,300,000.00 USD | 4,300,000.00 USD | 37,280.00 USD | 211,590.00 USD | 124,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 4,420,000.00 USD | 4,420,000.00 USD | 62,210.00 USD | 26,520.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 4,790,000.00 USD | 4,790,000.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 5,610,000.00 USD | 5,610,000.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 6,300,000.00 USD | 6,300,000.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 7,270,000.00 USD | 7,270,000.00 USD | 505,530.00 USD | 177,920.00 USD | 284,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 8,540,000.00 USD | 8,540,000.00 USD | 708,460.00 USD | 157,510.00 USD | 402,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 8,820,000.00 USD | 8,820,000.00 USD | 136,470.00 USD | 46,780.00 USD | 96,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 9,250,000.00 USD | 9,250,000.00 USD | 194,250.00 USD | 98,370.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 2,580.00 USD | 10,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,610,000.00 USD | 9,610,000.00 USD | 213,030.00 USD | 58,850.00 USD | 87,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 10,010,000.00 USD | 10,010,000.00 USD | 217,740.00 USD | 60,150.00 USD | 121,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 10,060,000.00 USD | 10,060,000.00 USD | 31,260.00 USD | 8,960.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 14,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 16,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 16,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 18,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 28,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 28,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 35,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 37,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,370.00 USD | 65,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 66,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 1,400.00 USD | 67,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 298.11 USD | 67,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 68,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 425.73 USD | 68,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 2,590.00 USD | 71,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 73,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 73,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 77,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 77,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 85,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2965` | 42,750.00 USD | 128,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 128,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 75,960.00 USD | 204,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3035` | 204.56 USD | 204,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 205,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,310.00 USD | 302,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 75,070.00 USD | 377,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3185` | 4,300.00 USD | 381,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3245` | 1,140.00 USD | 382,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 3,750.00 USD | 386,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 389,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 315.88 USD | 389,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 995.53 USD | 390,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 1,460.00 USD | 391,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3525` | 322.54 USD | 392,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3555` | 142.56 USD | 392,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 111.58 USD | 392,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3585` | 2,440.00 USD | 394,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 3,030.00 USD | 397,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3665` | 2,750.00 USD | 400,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 409,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 488,560.00 USD | 898,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3815` | 140.39 USD | 898,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0405` | 2,390,000.00 USD | 0.00 USD | 207.36 USD | `-78.84%` | `5,120.00` |
| `Live` | `Long` | `0.0415` | 2,390,000.00 USD | 0.00 USD | 1,050.00 USD | `-78.32%` | `25,182.00` |
| `Live` | `Long` | `0.0465` | 2,380,000.00 USD | 0.00 USD | 1,240.00 USD | `-75.70%` | `26,617.00` |
| `Live` | `Long` | `0.0485` | 2,380,000.00 USD | 0.00 USD | 103.16 USD | `-74.66%` | `2,127.00` |
| `Live` | `Long` | `0.0495` | 2,380,000.00 USD | 0.00 USD | 6,930.00 USD | `-74.14%` | `140,000.00` |
| `Live` | `Long` | `0.0535` | 2,380,000.00 USD | 0.00 USD | 481.50 USD | `-72.05%` | `9,000.00` |
| `Live` | `Long` | `0.0595` | 2,380,000.00 USD | 0.00 USD | 2,610.00 USD | `-68.91%` | `43,814.00` |
| `Live` | `Long` | `0.0605` | 2,370,000.00 USD | 0.00 USD | 155.12 USD | `-68.39%` | `2,564.00` |
| `Live` | `Long` | `0.0695` | 2,370,000.00 USD | 0.00 USD | 7,300.00 USD | `-63.68%` | `105,008.00` |
| `Live` | `Long` | `0.0725` | 2,370,000.00 USD | 0.00 USD | 3,760.00 USD | `-62.12%` | `51,887.00` |
| `Live` | `Long` | `0.0785` | 2,360,000.00 USD | 0.00 USD | 111.86 USD | `-58.98%` | `1,425.00` |
| `Live` | `Long` | `0.0815` | 2,360,000.00 USD | 0.00 USD | 284.84 USD | `-57.41%` | `3,495.00` |
| `Live` | `Long` | `0.0855` | 2,360,000.00 USD | 0.00 USD | 160,200.00 USD | `-55.32%` | `1,873,703.00` |
| `Live` | `Long` | `0.0865` | 2,200,000.00 USD | 0.00 USD | 102.50 USD | `-54.80%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,200,000.00 USD | 0.00 USD | 1,000.00 USD | `-54.28%` | `11,440.00` |
| `Live` | `Long` | `0.0885` | 2,200,000.00 USD | 0.00 USD | 1,150.00 USD | `-53.76%` | `13,050.00` |
| `Live` | `Long` | `0.0905` | 2,200,000.00 USD | 0.00 USD | 157.83 USD | `-52.71%` | `1,744.00` |
| `Live` | `Long` | `0.0925` | 2,200,000.00 USD | 0.00 USD | 1,610.00 USD | `-51.67%` | `17,413.00` |
| `Live` | `Long` | `0.0935` | 2,200,000.00 USD | 0.00 USD | 935.00 USD | `-51.14%` | `10,000.00` |
| `Live` | `Long` | `0.0945` | 2,200,000.00 USD | 0.00 USD | 327.54 USD | `-50.62%` | `3,466.00` |
| `Live` | `Long` | `0.1025` | 2,200,000.00 USD | 0.00 USD | 6,940.00 USD | `-46.44%` | `67,674.00` |
| `Live` | `Long` | `0.1035` | 2,190,000.00 USD | 0.00 USD | 1,050.00 USD | `-45.92%` | `10,149.00` |
| `Live` | `Long` | `0.1065` | 2,190,000.00 USD | 0.00 USD | 793.42 USD | `-44.35%` | `7,450.00` |
| `Live` | `Long` | `0.1075` | 2,190,000.00 USD | 0.00 USD | 454.62 USD | `-43.83%` | `4,229.00` |
| `Live` | `Long` | `0.1085` | 2,190,000.00 USD | 0.00 USD | 111.86 USD | `-43.31%` | `1,031.00` |
| `Live` | `Long` | `0.1095` | 2,190,000.00 USD | 0.00 USD | 1,490.00 USD | `-42.78%` | `13,608.00` |
| `Live` | `Long` | `0.1145` | 2,180,000.00 USD | 0.00 USD | 862.64 USD | `-40.17%` | `7,534.00` |
| `Live` | `Long` | `0.1155` | 2,180,000.00 USD | 0.00 USD | 1,730.00 USD | `-39.65%` | `15,000.00` |
| `Live` | `Long` | `0.1165` | 2,180,000.00 USD | 0.00 USD | 13,360.00 USD | `-39.13%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,170,000.00 USD | 0.00 USD | 28,660.00 USD | `-38.60%` | `243,899.00` |
| `Live` | `Long` | `0.1195` | 2,140,000.00 USD | 0.00 USD | 150.21 USD | `-37.56%` | `1,257.00` |
| `Live` | `Long` | `0.1205` | 2,140,000.00 USD | 0.00 USD | 826.27 USD | `-37.04%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,140,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.51%` | `8,652.00` |
| `Live` | `Long` | `0.1245` | 2,140,000.00 USD | 0.00 USD | 2,080.00 USD | `-34.95%` | `16,727.00` |
| `Live` | `Long` | `0.1255` | 2,140,000.00 USD | 0.00 USD | 1,980.00 USD | `-34.42%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,130,000.00 USD | 0.00 USD | 5,300.00 USD | `-33.90%` | `41,897.00` |
| `Live` | `Long` | `0.1275` | 2,130,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.38%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,130,000.00 USD | 0.00 USD | 2,540.00 USD | `-32.33%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,120,000.00 USD | 0.00 USD | 290.36 USD | `-31.81%` | `2,225.00` |
| `Live` | `Long` | `0.1315` | 2,120,000.00 USD | 0.00 USD | 687.35 USD | `-31.29%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,120,000.00 USD | 0.00 USD | 6,960.00 USD | `-30.77%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,120,000.00 USD | 0.00 USD | 3,600.00 USD | `-30.24%` | `26,965.00` |
| `Live` | `Long` | `0.1345` | 2,110,000.00 USD | 0.00 USD | 2,120.00 USD | `-29.72%` | `15,737.00` |
| `Live` | `Long` | `0.1355` | 2,110,000.00 USD | 0.00 USD | 12,990.00 USD | `-29.20%` | `95,890.00` |
| `Live` | `Long` | `0.1395` | 2,100,000.00 USD | 0.00 USD | 100.02 USD | `-27.11%` | `717.00` |
| `Live` | `Long` | `0.1405` | 2,100,000.00 USD | 0.00 USD | 565.51 USD | `-26.59%` | `4,025.00` |
| `Live` | `Long` | `0.1415` | 2,100,000.00 USD | 0.00 USD | 11,090.00 USD | `-26.06%` | `78,385.00` |
| `Live` | `Long` | `0.1425` | 2,090,000.00 USD | 0.00 USD | 902.88 USD | `-25.54%` | `6,336.00` |
| `Live` | `Long` | `0.1435` | 2,090,000.00 USD | 0.00 USD | 105,520.00 USD | `-25.02%` | `735,335.00` |
| `Live` | `Long` | `0.1445` | 1,980,000.00 USD | 0.00 USD | 1,890.00 USD | `-24.50%` | `13,058.00` |
| `Live` | `Long` | `0.1455` | 1,980,000.00 USD | 0.00 USD | 3,770.00 USD | `-23.97%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 1,970,000.00 USD | 0.00 USD | 4,580.00 USD | `-23.45%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 1,970,000.00 USD | 0.00 USD | 882.93 USD | `-22.93%` | `5,986.00` |
| `Live` | `Long` | `0.1485` | 1,970,000.00 USD | 0.00 USD | 4,000.00 USD | `-22.41%` | `26,968.00` |
| `Live` | `Long` | `0.1495` | 1,960,000.00 USD | 0.00 USD | 2,050.00 USD | `-21.88%` | `13,697.00` |
| `Live` | `Long` | `0.1505` | 1,960,000.00 USD | 0.00 USD | 1,720.00 USD | `-21.36%` | `11,458.00` |
| `Live` | `Long` | `0.1515` | 1,960,000.00 USD | 0.00 USD | 33,400.00 USD | `-20.84%` | `220,430.00` |
| `Live` | `Long` | `0.1525` | 1,930,000.00 USD | 0.00 USD | 981.95 USD | `-20.32%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 1,930,000.00 USD | 0.00 USD | 77,210.00 USD | `-19.79%` | `503,027.00` |
| `Live` | `Long` | `0.1545` | 1,850,000.00 USD | 0.00 USD | 1,970.00 USD | `-19.27%` | `12,750.00` |
| `Live` | `Long` | `0.1555` | 1,850,000.00 USD | 0.00 USD | 3,000.00 USD | `-18.75%` | `19,304.00` |
| `Live` | `Long` | `0.1565` | 1,840,000.00 USD | 0.00 USD | 12,520.00 USD | `-18.23%` | `80,016.00` |
| `Live` | `Long` | `0.1575` | 1,830,000.00 USD | 0.00 USD | 216.56 USD | `-17.70%` | `1,375.00` |
| `Live` | `Long` | `0.1585` | 1,830,000.00 USD | 0.00 USD | 6,120.00 USD | `-17.18%` | `38,602.00` |
| `Live` | `Long` | `0.1595` | 1,830,000.00 USD | 0.00 USD | 138.61 USD | `-16.66%` | `869.00` |
| `Live` | `Long` | `0.1605` | 1,830,000.00 USD | 0.00 USD | 602,410.00 USD | `-16.14%` | `3,753,361.00` |
| `Live` | `Long` | `0.1615` | 1,220,000.00 USD | 0.00 USD | 4,200.00 USD | `-15.61%` | `26,015.00` |
| `Live` | `Long` | `0.1625` | 1,220,000.00 USD | 0.00 USD | 65,290.00 USD | `-15.09%` | `401,796.00` |
| `Live` | `Long` | `0.1635` | 1,150,000.00 USD | 0.00 USD | 1,040.00 USD | `-14.57%` | `6,337.00` |
| `Live` | `Long` | `0.1645` | 1,150,000.00 USD | 0.00 USD | 10,540.00 USD | `-14.05%` | `64,095.00` |
| `Live` | `Long` | `0.1655` | 1,140,000.00 USD | 0.00 USD | 241.46 USD | `-13.52%` | `1,459.00` |
| `Live` | `Long` | `0.1665` | 1,140,000.00 USD | 0.00 USD | 1,120.00 USD | `-13.00%` | `6,700.00` |
| `Live` | `Long` | `0.1675` | 1,140,000.00 USD | 0.00 USD | 630.81 USD | `-12.48%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,140,000.00 USD | 0.00 USD | 13,630.00 USD | `-11.96%` | `80,880.00` |
| `Live` | `Long` | `0.1695` | 1,130,000.00 USD | 0.00 USD | 78,180.00 USD | `-11.43%` | `461,249.00` |
| `Live` | `Long` | `0.1705` | 1,050,000.00 USD | 0.00 USD | 625,360.00 USD | `-10.91%` | `3,667,828.00` |
| `Live` | `Long` | `0.1715` | 423,000.00 USD | 0.00 USD | 252,270.00 USD | `-10.39%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 170,730.00 USD | 0.00 USD | 35,220.00 USD | `-9.87%` | `204,190.00` |
| `Live` | `Long` | `0.1735` | 135,510.00 USD | 0.00 USD | 4,020.00 USD | `-9.34%` | `23,148.00` |
| `Live` | `Long` | `0.1745` | 131,490.00 USD | 0.00 USD | 1,320.00 USD | `-8.82%` | `7,554.00` |
| `Live` | `Long` | `0.1765` | 130,170.00 USD | 0.00 USD | 4,990.00 USD | `-7.78%` | `28,260.00` |
| `Live` | `Long` | `0.1775` | 125,180.00 USD | 0.00 USD | 16,020.00 USD | `-7.25%` | `90,258.00` |
| `Live` | `Long` | `0.1785` | 109,160.00 USD | 0.00 USD | 2,480.00 USD | `-6.73%` | `13,921.00` |
| `Live` | `Long` | `0.1795` | 106,680.00 USD | 0.00 USD | 873.09 USD | `-6.21%` | `4,864.00` |
| `Live` | `Long` | `0.1805` | 105,810.00 USD | 0.00 USD | 55,280.00 USD | `-5.69%` | `306,255.00` |
| `Live` | `Long` | `0.1815` | 50,530.00 USD | 0.00 USD | 15,750.00 USD | `-5.16%` | `86,764.00` |
| `Live` | `Long` | `0.1825` | 34,780.00 USD | 0.00 USD | 27,520.00 USD | `-4.64%` | `150,814.00` |
| `Live` | `Long` | `0.1835` | 7,260.00 USD | 0.00 USD | 827.59 USD | `-4.12%` | `4,510.00` |
| `Live` | `Long` | `0.1845` | 6,430.00 USD | 0.00 USD | 2,240.00 USD | `-3.59%` | `12,141.00` |
| `Live` | `Long` | `0.1865` | 4,190.00 USD | 0.00 USD | 3,740.00 USD | `-2.55%` | `20,031.00` |
| `Live` | `Long` | `0.1875` | 451.69 USD | 0.00 USD | 451.69 USD | `-2.03%` | `2,409.00` |
| `Live` | `Short` | `0.1995` | 252.97 USD | 252.97 USD | 0.00 USD | `+4.24%` | `1,268.00` |
| `Live` | `Short` | `0.2015` | 357.75 USD | 104.78 USD | 0.00 USD | `+5.29%` | `520.00` |
| `Live` | `Short` | `0.2125` | 2,940.00 USD | 2,580.00 USD | 0.00 USD | `+11.04%` | `12,141.00` |
| `Live` | `Short` | `0.2175` | 6,870.00 USD | 3,930.00 USD | 0.00 USD | `+13.65%` | `18,067.00` |
| `Live` | `Short` | `0.2215` | 8,510.00 USD | 1,640.00 USD | 0.00 USD | `+15.74%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 8,710.00 USD | 200.48 USD | 0.00 USD | `+16.78%` | `897.00` |
| `Live` | `Short` | `0.2275` | 10,870.00 USD | 2,160.00 USD | 0.00 USD | `+18.87%` | `9,500.00` |
| `Live` | `Short` | `0.2285` | 20,110.00 USD | 9,240.00 USD | 0.00 USD | `+19.40%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 20,390.00 USD | 282.02 USD | 0.00 USD | `+21.49%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 28,030.00 USD | 7,640.00 USD | 0.00 USD | `+22.01%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 29,500.00 USD | 1,470.00 USD | 0.00 USD | `+25.67%` | `6,110.00` |
| `Live` | `Short` | `0.2425` | 30,580.00 USD | 1,080.00 USD | 0.00 USD | `+26.71%` | `4,435.00` |
| `Live` | `Short` | `0.2435` | 31,210.00 USD | 635.78 USD | 0.00 USD | `+27.23%` | `2,611.00` |
| `Live` | `Short` | `0.2525` | 59,580.00 USD | 28,370.00 USD | 0.00 USD | `+31.94%` | `112,352.00` |
| `Live` | `Short` | `0.2585` | 59,960.00 USD | 380.25 USD | 0.00 USD | `+35.07%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 61,360.00 USD | 1,400.00 USD | 0.00 USD | `+36.64%` | `5,346.00` |
| `Live` | `Short` | `0.2715` | 61,660.00 USD | 298.11 USD | 0.00 USD | `+41.86%` | `1,098.00` |
| `Live` | `Short` | `0.2775` | 62,040.00 USD | 379.62 USD | 0.00 USD | `+45.00%` | `1,368.00` |
| `Live` | `Short` | `0.2825` | 62,460.00 USD | 425.73 USD | 0.00 USD | `+47.61%` | `1,507.00` |
| `Live` | `Short` | `0.2835` | 65,050.00 USD | 2,590.00 USD | 0.00 USD | `+48.13%` | `9,121.00` |
| `Live` | `Short` | `0.2845` | 67,220.00 USD | 2,170.00 USD | 0.00 USD | `+48.66%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 67,630.00 USD | 411.09 USD | 0.00 USD | `+51.27%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 70,900.00 USD | 3,260.00 USD | 0.00 USD | `+52.31%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 71,420.00 USD | 519.79 USD | 0.00 USD | `+53.36%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 79,400.00 USD | 7,990.00 USD | 0.00 USD | `+54.40%` | `27,027.00` |
| `Live` | `Short` | `0.2965` | 151,790.00 USD | 72,390.00 USD | 0.00 USD | `+54.93%` | `244,139.00` |
| `Live` | `Short` | `0.3005` | 151,940.00 USD | 146.34 USD | 0.00 USD | `+57.02%` | `487.00` |
| `Live` | `Short` | `0.3055` | 152,340.00 USD | 408.15 USD | 0.00 USD | `+59.63%` | `1,336.00` |
| `Live` | `Short` | `0.3115` | 249,650.00 USD | 97,310.00 USD | 0.00 USD | `+62.77%` | `312,388.00` |
| `Live` | `Short` | `0.3125` | 253,870.00 USD | 4,220.00 USD | 0.00 USD | `+63.29%` | `13,504.00` |
| `Live` | `Short` | `0.3155` | 293,890.00 USD | 40,020.00 USD | 0.00 USD | `+64.86%` | `126,832.00` |
| `Live` | `Short` | `0.3195` | 295,010.00 USD | 1,120.00 USD | 0.00 USD | `+66.95%` | `3,500.00` |
| `Live` | `Short` | `0.3205` | 298,870.00 USD | 3,860.00 USD | 0.00 USD | `+67.47%` | `12,048.00` |
| `Live` | `Short` | `0.3265` | 300,260.00 USD | 1,390.00 USD | 0.00 USD | `+70.60%` | `4,254.00` |
| `Live` | `Short` | `0.3295` | 646,490.00 USD | 346,230.00 USD | 0.00 USD | `+72.17%` | `1,050,788.00` |
| `Live` | `Short` | `0.3315` | 646,730.00 USD | 237.35 USD | 0.00 USD | `+73.22%` | `716.00` |
| `Live` | `Short` | `0.3365` | 647,480.00 USD | 748.71 USD | 0.00 USD | `+75.83%` | `2,225.00` |
| `Live` | `Short` | `0.3435` | 647,800.00 USD | 326.33 USD | 0.00 USD | `+79.49%` | `950.00` |
| `Live` | `Short` | `0.3455` | 647,960.00 USD | 154.44 USD | 0.00 USD | `+80.53%` | `447.00` |
| `Live` | `Short` | `0.3465` | 648,270.00 USD | 317.05 USD | 0.00 USD | `+81.05%` | `915.00` |
| `Live` | `Short` | `0.3525` | 648,420.00 USD | 141.35 USD | 0.00 USD | `+84.19%` | `401.00` |
| `Live` | `Short` | `0.3595` | 649,330.00 USD | 914.21 USD | 0.00 USD | `+87.85%` | `2,543.00` |
| `Live` | `Short` | `0.3605` | 651,780.00 USD | 2,450.00 USD | 0.00 USD | `+88.37%` | `6,797.00` |
| `Live` | `Short` | `0.3615` | 653,730.00 USD | 1,950.00 USD | 0.00 USD | `+88.89%` | `5,402.00` |
| `Live` | `Short` | `0.3645` | 863,470.00 USD | 209,740.00 USD | 0.00 USD | `+90.46%` | `575,408.00` |
| `Live` | `Short` | `0.3705` | 1,130,000.00 USD | 267,040.00 USD | 0.00 USD | `+93.59%` | `720,753.00` |
| `Live` | `Short` | `0.3715` | 1,140,000.00 USD | 9,170.00 USD | 0.00 USD | `+94.12%` | `24,689.00` |
| `Live` | `Short` | `0.3725` | 1,140,000.00 USD | 116.59 USD | 0.00 USD | `+94.64%` | `313.00` |
| `Live` | `Short` | `0.3745` | 1,140,000.00 USD | 3,140.00 USD | 0.00 USD | `+95.68%` | `8,395.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 864,760.00 USD | 0.00 USD | 415.13 USD | `-68.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 864,340.00 USD | 0.00 USD | 438.99 USD | `-68.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 863,900.00 USD | 0.00 USD | 1,100.00 USD | `-42.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 862,800.00 USD | 0.00 USD | 541.33 USD | `-41.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 862,260.00 USD | 0.00 USD | 602,500.00 USD | `-37.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 259,760.00 USD | 0.00 USD | 4,460.00 USD | `-35.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 255,300.00 USD | 0.00 USD | 1,320.00 USD | `-33.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 253,980.00 USD | 0.00 USD | 13,390.00 USD | `-31.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 240,590.00 USD | 0.00 USD | 728.88 USD | `-30.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 239,860.00 USD | 0.00 USD | 4,350.00 USD | `-29.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 235,510.00 USD | 0.00 USD | 4,730.00 USD | `-28.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 230,780.00 USD | 0.00 USD | 1,820.00 USD | `-27.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 228,960.00 USD | 0.00 USD | 1,050.00 USD | `-26.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 227,910.00 USD | 0.00 USD | 1,600.00 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 226,300.00 USD | 0.00 USD | 4,580.00 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 221,720.00 USD | 0.00 USD | 303.26 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 221,420.00 USD | 0.00 USD | 1,290.00 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 220,130.00 USD | 0.00 USD | 279.53 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 219,850.00 USD | 0.00 USD | 324.30 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 219,530.00 USD | 0.00 USD | 1,480.00 USD | `-18.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 218,050.00 USD | 0.00 USD | 552.21 USD | `-17.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 217,500.00 USD | 0.00 USD | 166.84 USD | `-16.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 217,330.00 USD | 0.00 USD | 2,990.00 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 214,340.00 USD | 0.00 USD | 562.67 USD | `-15.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 213,780.00 USD | 0.00 USD | 24,760.00 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 189,020.00 USD | 0.00 USD | 6,540.00 USD | `-14.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 182,480.00 USD | 0.00 USD | 2,870.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 179,610.00 USD | 0.00 USD | 452.97 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 179,160.00 USD | 0.00 USD | 14,050.00 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 165,120.00 USD | 0.00 USD | 317.92 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 164,800.00 USD | 0.00 USD | 4,270.00 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 160,530.00 USD | 0.00 USD | 7,630.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 152,900.00 USD | 0.00 USD | 6,860.00 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 146,040.00 USD | 0.00 USD | 103.58 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 145,930.00 USD | 0.00 USD | 75,480.00 USD | `-8.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 70,450.00 USD | 0.00 USD | 1,760.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 68,690.00 USD | 0.00 USD | 847.38 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 67,840.00 USD | 0.00 USD | 4,440.00 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 63,400.00 USD | 0.00 USD | 12,390.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 51,010.00 USD | 0.00 USD | 4,030.00 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 46,990.00 USD | 0.00 USD | 1,570.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 45,420.00 USD | 0.00 USD | 2,720.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 42,700.00 USD | 0.00 USD | 3,080.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 39,620.00 USD | 0.00 USD | 5,630.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 33,990.00 USD | 0.00 USD | 18,800.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 15,190.00 USD | 0.00 USD | 5,850.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 9,340.00 USD | 0.00 USD | 264.64 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 9,080.00 USD | 0.00 USD | 109.69 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 8,970.00 USD | 0.00 USD | 1,840.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 7,130.00 USD | 0.00 USD | 6,730.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 400.43 USD | 0.00 USD | 400.43 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 45,280.00 USD | 45,280.00 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 45,790.00 USD | 513.01 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 48,270.00 USD | 2,480.00 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 48,660.00 USD | 389.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 49,160.00 USD | 498.33 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 52,710.00 USD | 3,550.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 53,710.00 USD | 1,000.00 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 54,360.00 USD | 646.71 USD | 0.00 USD | `+3.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 54,560.00 USD | 199.50 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 80,260,000.00 USD | 80,210,000.00 USD | 0.00 USD | `+4.77%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2015` | 80,310,000.00 USD | 46,440.00 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 80,310,000.00 USD | 101.86 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 80,310,000.00 USD | 752.34 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 80,310,000.00 USD | 2,170.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 80,310,000.00 USD | 130.70 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 80,310,000.00 USD | 207.74 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 80,310,000.00 USD | 312.70 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 80,320,000.00 USD | 3,320.00 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 80,320,000.00 USD | 8,720.00 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 80,350,000.00 USD | 24,600.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 80,360,000.00 USD | 11,750.00 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 80,360,000.00 USD | 472.39 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 80,360,000.00 USD | 3,400.00 USD | 0.00 USD | `+11.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 80,370,000.00 USD | 965.25 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 80,370,000.00 USD | 1,570.00 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 80,370,000.00 USD | 219.53 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 80,370,000.00 USD | 109.91 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 80,370,000.00 USD | 6,920.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 80,380,000.00 USD | 4,510.00 USD | 0.00 USD | `+15.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 80,380,000.00 USD | 1,650.00 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 80,380,000.00 USD | 1,690.00 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 80,380,000.00 USD | 501.31 USD | 0.00 USD | `+16.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 80,380,000.00 USD | 114.50 USD | 0.00 USD | `+17.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 80,380,000.00 USD | 339.60 USD | 0.00 USD | `+17.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 80,380,000.00 USD | 109.40 USD | 0.00 USD | `+18.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 80,410,000.00 USD | 21,490.00 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 80,410,000.00 USD | 9,140.00 USD | 0.00 USD | `+19.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 80,410,000.00 USD | 662.92 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 80,420,000.00 USD | 9,600.00 USD | 0.00 USD | `+20.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 80,420,000.00 USD | 171.12 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 80,430,000.00 USD | 1,010.00 USD | 0.00 USD | `+22.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 80,440,000.00 USD | 9,420.00 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 80,440,000.00 USD | 315.96 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 80,440,000.00 USD | 650.04 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 80,440,000.00 USD | 192.71 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 80,450,000.00 USD | 10,090.00 USD | 0.00 USD | `+25.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 80,450,000.00 USD | 209.72 USD | 0.00 USD | `+25.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 80,450,000.00 USD | 115.92 USD | 0.00 USD | `+26.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 80,450,000.00 USD | 236.19 USD | 0.00 USD | `+27.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 80,460,000.00 USD | 10,930.00 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 80,460,000.00 USD | 288.22 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 80,460,000.00 USD | 491.03 USD | 0.00 USD | `+28.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 80,460,000.00 USD | 1,320.00 USD | 0.00 USD | `+29.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 80,470,000.00 USD | 9,940.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 80,470,000.00 USD | 499.00 USD | 0.00 USD | `+30.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 80,570,000.00 USD | 98,380.00 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 80,570,000.00 USD | 168.76 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 80,570,000.00 USD | 603.73 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 80,570,000.00 USD | 2,170.00 USD | 0.00 USD | `+32.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 80,570,000.00 USD | 1,570.00 USD | 0.00 USD | `+34.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 80,570,000.00 USD | 1,470.00 USD | 0.00 USD | `+34.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 80,580,000.00 USD | 271.44 USD | 0.00 USD | `+35.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 81,000,000.00 USD | 421,590.00 USD | 0.00 USD | `+36.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 81,000,000.00 USD | 1,180.00 USD | 0.00 USD | `+38.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 81,000,000.00 USD | 945.98 USD | 0.00 USD | `+38.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 81,010,000.00 USD | 8,890.00 USD | 0.00 USD | `+39.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 81,020,000.00 USD | 14,860.00 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 81,020,000.00 USD | 1,340.00 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 81,030,000.00 USD | 2,710.00 USD | 0.00 USD | `+41.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 81,040,000.00 USD | 13,870.00 USD | 0.00 USD | `+42.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 81,050,000.00 USD | 5,220.00 USD | 0.00 USD | `+43.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 81,050,000.00 USD | 1,170.00 USD | 0.00 USD | `+45.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 81,050,000.00 USD | 944.99 USD | 0.00 USD | `+46.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 81,050,000.00 USD | 161.87 USD | 0.00 USD | `+47.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 81,050,000.00 USD | 113.68 USD | 0.00 USD | `+48.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 81,050,000.00 USD | 1,370.00 USD | 0.00 USD | `+48.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 81,050,000.00 USD | 1,080.00 USD | 0.00 USD | `+50.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 81,070,000.00 USD | 14,980.00 USD | 0.00 USD | `+51.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 81,070,000.00 USD | 1,230.00 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 81,070,000.00 USD | 1,440.00 USD | 0.00 USD | `+55.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 81,070,000.00 USD | 355.21 USD | 0.00 USD | `+56.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 81,080,000.00 USD | 6,650.00 USD | 0.00 USD | `+57.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 81,090,000.00 USD | 18,980.00 USD | 0.00 USD | `+59.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 81,100,000.00 USD | 4,150.00 USD | 0.00 USD | `+61.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 81,100,000.00 USD | 3,250.00 USD | 0.00 USD | `+64.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 81,110,000.00 USD | 5,090.00 USD | 0.00 USD | `+67.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 81,110,000.00 USD | 493.89 USD | 0.00 USD | `+69.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 81,110,000.00 USD | 181.30 USD | 0.00 USD | `+70.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 81,110,000.00 USD | 1,380.00 USD | 0.00 USD | `+72.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 81,120,000.00 USD | 12,290.00 USD | 0.00 USD | `+73.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 81,120,000.00 USD | 111.06 USD | 0.00 USD | `+74.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 81,120,000.00 USD | 220.61 USD | 0.00 USD | `+78.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 81,130,000.00 USD | 3,850.00 USD | 0.00 USD | `+82.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 81,130,000.00 USD | 188.75 USD | 0.00 USD | `+97.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 81,130,000.00 USD | 909.54 USD | 0.00 USD | `+97.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 81,130,000.00 USD | 121.76 USD | 0.00 USD | `+98.82%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1710` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 23,820.00 USD | 1,400.00 USD | 15,810.00 USD |
| `1D` | `0.1720` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 9,810.00 USD | 495.36 USD | 45,510.00 USD |
| `1D` | `0.1730` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 0.00 USD | 7,590.00 USD | 28,880.00 USD |
| `1D` | `0.1740` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD |
| `1D` | `0.1750` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1760` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD |
| `1D` | `0.1770` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 53,230.00 USD | 18,700.00 USD | 79,670.00 USD |
| `1D` | `0.1780` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 63,860.00 USD | 34,680.00 USD | 67,000.00 USD |
| `1D` | `0.1790` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 40,760.00 USD | 24,400.00 USD | 44,490.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 145,820.00 USD | 14,270.00 USD | 69,380.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 72,410.00 USD | 24,810.00 USD | 132,830.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 90,620.00 USD | 47,040.00 USD | 131,150.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 116,980.00 USD | 67,340.00 USD | 181,910.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 202,510.00 USD | 8,970.00 USD | 88,350.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 178,050.00 USD | 55,340.00 USD | 276,220.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 249,090.00 USD | 84,790.00 USD | 217,680.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 636,620.00 USD | 0.00 USD | 636,620.00 USD | 162,010.00 USD | 135,840.00 USD | 154,170.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 184,600.00 USD | 0.00 USD | 184,600.00 USD | 104,350.00 USD | 0.00 USD | 42,920.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 37,340.00 USD | 0.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `1D` | `0.1920` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 582,900.00 USD | 582,900.00 USD | 0.00 USD | 139,920.00 USD | 5,450.00 USD | 75,890.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 940,610.00 USD | 940,610.00 USD | 0.00 USD | 96,260.00 USD | 25,730.00 USD | 235,720.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 32,060.00 USD | 213,960.00 USD | 224,770.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 166,770.00 USD | 3,990.00 USD | 76,170.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 88,240.00 USD | 40,300.00 USD | 184,810.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 201,440.00 USD | 31,640.00 USD | 283,420.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 104,220.00 USD | 135,280.00 USD | 302,380.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 94,050.00 USD | 29,200.00 USD | 105,810.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 74,710.00 USD | 85,020.00 USD | 281,720.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 37,280.00 USD | 211,590.00 USD | 124,890.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 62,210.00 USD | 26,520.00 USD | 33,330.00 USD |
| `1D` | `0.2060` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 505,530.00 USD | 177,920.00 USD | 284,650.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 708,460.00 USD | 157,510.00 USD | 402,400.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 136,470.00 USD | 46,780.00 USD | 96,740.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 194,250.00 USD | 98,370.00 USD | 139,010.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 213,030.00 USD | 58,850.00 USD | 87,590.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 217,740.00 USD | 60,150.00 USD | 121,210.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 31,260.00 USD | 8,960.00 USD | 5,840.00 USD |
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
  * Total Open Interest: `417.62M` | Total OI Tokens: `2,173,252,195.1 ADA`
  * 1h OI Change: `+0.06%` | 4h OI Change: `-7.25%` | 24h OI Change: `-9.20%`
  * Exchange Breakdown: Binance=`75.51M` | Bybit=`51.03M` | OKX=`29.54M` | Hyperliquid=`28.30M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `144.86` | Last 24h: `14.20K` | Last 3d: `57.34K` | Last 7d: `58.14K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0034%` | **USDT OKX** | `-0.0080%` |
| **USDT Bybit** | `-0.0004%` | **USDT KuCoin** | `-0.0015%` |
| **USDT MEXC** | `0.0035%` | **USDT BingX** | `0.0044%` |
| **USDT Gate** | `-0.0046%` | **USDT Bitget** | `0.0020%` |
| **CoinM Binance** | `-0.0038%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `50.60%` | `49.40%` | `1.02` | 21,070,000.00 USD |
| `15M` | `Binance` | `43.94%` | `56.06%` | `0.78` | 7,420,000.00 USD |
| `15M` | `OKX` | `57.55%` | `42.45%` | `1.36` | 4,200,000.00 USD |
| `15M` | `Bybit` | `56.18%` | `43.82%` | `1.28` | 1,580,000.00 USD |
| `15M` | `KuCoin` | `47.5%` | `52.5%` | `0.90` | 100,990.00 USD |
| `15M` | `Gate` | `48.79%` | `51.21%` | `0.95` | 2,910,000.00 USD |
| `15M` | `Bitget` | `42.59%` | `57.41%` | `0.74` | 340,610.00 USD |
| `15M` | `BingX` | `40.8%` | `59.2%` | `0.69` | 144,830.00 USD |
| `15M` | `MEXC` | `56.47%` | `43.53%` | `1.30` | 3,440,000.00 USD |
| `15M` | `Bitunix` | `42.14%` | `57.86%` | `0.73` | 479,960.00 USD |
| `15M` | `Hyperliquid` | `39.43%` | `60.57%` | `0.65` | 76,390.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `66.08%` | `33.92%` | `1.95` | 123,840.00 USD |
| `15M` | `Crypto.com` | `57.71%` | `42.29%` | `1.36` | 19,460.00 USD |
| `15M` | `WhiteBIT` | `86.37%` | `13.63%` | `6.34` | 90,830.00 USD |
| `15M` | `HTX` | `41.55%` | `58.45%` | `0.71` | 31,500.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `55.38%` | `44.62%` | `1.24` | 55,540.00 USD |
| `15M` | `Aster` | `59.84%` | `40.16%` | `1.49` | 49,970.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `54.35%` | `45.65%` | `1.19` | 8,740.00 USD |
| `15M` | `Whale Positions` | `43.94%` | `56.06%` | `0.78` | 7,420,000.00 USD |
| `15M` | `Global Accounts` | `50.60%` | `49.40%` | `1.02` | 21,070,000.00 USD |
| `1H` | `ADA` | `52.28%` | `47.72%` | `1.10` | 120,880,000.00 USD |
| `1H` | `Binance` | `48.29%` | `51.71%` | `0.93` | 52,390,000.00 USD |
| `1H` | `OKX` | `59.38%` | `40.62%` | `1.46` | 21,100,000.00 USD |
| `1H` | `Bybit` | `50.37%` | `49.63%` | `1.01` | 8,380,000.00 USD |
| `1H` | `KuCoin` | `53.88%` | `46.12%` | `1.17` | 697,710.00 USD |
| `1H` | `Gate` | `48.45%` | `51.55%` | `0.94` | 13,720,000.00 USD |
| `1H` | `Bitget` | `49.35%` | `50.65%` | `0.97` | 2,490,000.00 USD |
| `1H` | `BingX` | `48.3%` | `51.7%` | `0.93` | 959,130.00 USD |
| `1H` | `MEXC` | `55.37%` | `44.63%` | `1.24` | 11,970,000.00 USD |
| `1H` | `Bitunix` | `51.65%` | `48.35%` | `1.07` | 3,150,000.00 USD |
| `1H` | `Hyperliquid` | `36.05%` | `63.95%` | `0.56` | 494,790.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.54%` | `41.46%` | `1.41` | 363,960.00 USD |
| `1H` | `Crypto.com` | `51.7%` | `48.3%` | `1.07` | 94,090.00 USD |
| `1H` | `WhiteBIT` | `58.01%` | `41.99%` | `1.38` | 677,740.00 USD |
| `1H` | `HTX` | `62.99%` | `37.01%` | `1.70` | 550,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.04%` | `54.96%` | `0.82` | 547,630.00 USD |
| `1H` | `Aster` | `83.51%` | `16.49%` | `5.06` | 3,250,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `81.49%` | `18.51%` | `4.40` | 51,990.00 USD |
| `1H` | `Whale Positions` | `48.29%` | `51.71%` | `0.93` | 52,390,000.00 USD |
| `1H` | `Global Accounts` | `52.28%` | `47.72%` | `1.10` | 120,880,000.00 USD |
| `4H` | `ADA` | `48.74%` | `51.26%` | `0.95` | 2,430,000,000.00 USD |
| `4H` | `Binance` | `48.91%` | `51.09%` | `0.96` | 1,400,000,000.00 USD |
| `4H` | `OKX` | `50.54%` | `49.46%` | `1.02` | 157,990,000.00 USD |
| `4H` | `Bybit` | `47.75%` | `52.25%` | `0.91` | 282,630,000.00 USD |
| `4H` | `KuCoin` | `45.68%` | `54.32%` | `0.84` | 13,580,000.00 USD |
| `4H` | `Gate` | `48.71%` | `51.29%` | `0.95` | 54,730,000.00 USD |
| `4H` | `Bitget` | `46.47%` | `53.53%` | `0.87` | 62,360,000.00 USD |
| `4H` | `BingX` | `48.84%` | `51.16%` | `0.95` | 23,790,000.00 USD |
| `4H` | `MEXC` | `48.41%` | `51.59%` | `0.94` | 32,470,000.00 USD |
| `4H` | `Bitunix` | `48.86%` | `51.14%` | `0.96` | 57,790,000.00 USD |
| `4H` | `Hyperliquid` | `48.3%` | `51.7%` | `0.93` | 239,430,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.11%` | `49.89%` | `1.00` | 15,010,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `37.65%` | `62.35%` | `0.60` | 4,230,000.00 USD |
| `4H` | `HTX` | `37.29%` | `62.71%` | `0.59` | 3,250,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.76%` | `50.24%` | `0.99` | 8,660,000.00 USD |
| `4H` | `Aster` | `49.82%` | `50.18%` | `0.99` | 50,400,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.37%` | `49.63%` | `1.01` | 27,320,000.00 USD |
| `4H` | `Whale Positions` | `48.91%` | `51.09%` | `0.96` | 1,400,000,000.00 USD |
| `4H` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 2,430,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1906` | `0.1904` | `0.1906` | `0.1935` | `0.1871` | 26,316,880.25 USD | 11,827,044.75 USD | 14,489,835.50 USD | -2,662,790.75 USD | `-10.12%` | `1B / 5S` |
| `0:00 UTC` | `0.1903` | `0.1914` | `0.1903` | `0.1931` | `0.1898` | 10,338,146.03 USD | 4,991,420.92 USD | 5,346,725.11 USD | -355,304.19 USD | `-3.44%` | `0B / 1S` |
| `5:00 UTC` | `0.1928` | `0.1937` | `0.1928` | `0.1951` | `0.1923` | 6,583,389.18 USD | 3,089,378.61 USD | 3,494,010.58 USD | -404,631.97 USD | `-6.15%` | `0B / 3S` |
| `0:00 UTC` | `0.1946` | `0.1945` | `0.1946` | `0.1953` | `0.1928` | 3,396,141.31 USD | 1,742,542.34 USD | 1,653,598.97 USD | 88,943.37 USD | `+2.62%` | `1B / 4S` |
| `5:00 UTC` | `0.1928` | `0.1929` | `0.1928` | `0.1938` | `0.1920` | 2,581,325.54 USD | 1,266,824.55 USD | 1,314,500.99 USD | -47,676.44 USD | `-1.85%` | `1B / 2S` |
| `0:00 UTC` | `0.1910` | `0.1912` | `0.1910` | `0.1925` | `0.1895` | 5,311,481.42 USD | 2,620,803.03 USD | 2,690,678.39 USD | -69,875.36 USD | `-1.32%` | `2B / 0S` |
| `5:00 UTC` | `0.1923` | `0.1923` | `0.1923` | `0.1933` | `0.1906` | 3,670,150.10 USD | 1,957,230.04 USD | 1,712,920.06 USD | 244,309.98 USD | `+6.66%` | `3B / 2S` |
| `0:00 UTC` | `0.1928` | `0.1930` | `0.1928` | `0.1938` | `0.1920` | 2,630,885.00 USD | 1,262,229.41 USD | 1,368,655.60 USD | -106,426.19 USD | `-4.05%` | `0B / 1S` |
| `5:00 UTC` | `0.1923` | `0.1918` | `0.1923` | `0.1926` | `0.1911` | 1,904,415.98 USD | 881,412.14 USD | 1,023,003.84 USD | -141,591.70 USD | `-7.43%` | `1B / 2S` |
| `0:00 UTC` | `0.1915` | `0.1912` | `0.1915` | `0.1920` | `0.1905` | 758,392.58 USD | 374,122.41 USD | 384,270.16 USD | -10,147.75 USD | `-1.34%` | `2B / 4S` |

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
| `5m` | -216,420.00 USD | -275,730.00 USD | **`DISTRIBUTION`** |
| `15m` | -524,970.00 USD | -359,400.00 USD | **`DISTRIBUTION`** |
| `30m` | -647,090.00 USD | -484,630.00 USD | **`DISTRIBUTION`** |
| `1h` | -753,000.00 USD | 136,890.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,300,000.00 USD | -340,950.00 USD | **`DISTRIBUTION`** |
| `4h` | -5,000,000.00 USD | -10,820,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,790,000.00 USD | -12,730,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,760,000.00 USD | -9,310,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,800,000.00 USD | -9,590,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,340,000.00 USD | -18,040,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -18,250,000.00 USD | -36,230,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -76,580,000.00 USD | -198,370,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-216.42K` | 15m=`-524.97K` | 1h=`-753.00K` | 24h=`-9.34M`
* Futures Capital Netflows: 5m=`-275.73K` | 15m=`-359.40K` | 1h=`+136.89K` | 24h=`-18.04M`
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
  * Execution Entry: `0.1899` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1839` (Risk Distance: `0.0060` pts)
  * +2.5R Take Profit: `0.2049`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1925` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1985` (Risk Distance: `0.0060` pts)
  * +2.5R Take Profit: `0.1775`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1913`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
