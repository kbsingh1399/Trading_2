# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 08:06:32 IST` (`2026-10-30 02:36:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1856` | **Live Ask Quote**: `0.1878` | **Mid Price**: `0.1867`
- **Spread Points**: `22.00` | **Spread BPS**: `117.84 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `0.1854` | VWAP Z-Score: `+0.12` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0025` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `34.23` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1900` | Lower -3.00σ Band: `0.1808`
  * Upper +2.51σ Band: `0.1892` | Lower -2.51σ Band: `0.1816`
  * Upper +2.01σ Band: `0.1885` | Lower -2.01σ Band: `0.1824`
  * Upper +2.00σ Band: `0.1885` | Lower -2.00σ Band: `0.1824`
  * Upper +1.28σ Band: `0.1874` | Lower -1.28σ Band: `0.1835`
  * Upper +1.00σ Band: `0.1869` | Lower -1.00σ Band: `0.1839`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1866` | EMA-20=`0.1890` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1935` (Slope: `+0.0000`) | EMA-100=`0.1966`
  * Institutional Anchors: EMA-144=`0.1979` | EMA-200=`0.1991` (Slope: `-0.7647`) | EMA-233=`0.2000`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1939` (Distance: `-3.34%`)
  * Point of Control (POC) = `0.1907` (Distance: `-1.73%`)
  * Value Area Low (VAL) = `0.1859` (Distance: `+0.78%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2063` | Weekly POC=`0.2031` | Weekly VAL=`0.1996`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1874` | Low=`0.1860`
  * New York Session (13:00-21:00 UTC): High=`0.1878` | Low=`0.1856`
  * Initial Balance (First Hour): IB High=`0.1873` | IB Low=`0.1861`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1860` - `0.1874`
  * Optimal Trade Entry (OTE 0.705): `0.1871`
  * Structural Invalidation Anchor (0.786): `0.1882`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1871` | `0.1874` | `0.1858` | `0.1858` | `3,998,473` | 746,417.83 USD | 4,082.52 USD | `+0.55%` | -3,397,024.04 USD | `-0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1859` | `0.1875` | `0.1859` | `0.1873` | `3,523,965` | 657,760.90 USD | 190,978.80 USD | `+29.03%` | -3,206,045.23 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1872` | `0.1879` | `0.1871` | `0.1876` | `2,097,343` | 393,276.33 USD | -6,377.48 USD | `-1.62%` | -3,212,422.71 USD | `-0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1867` | `0.1884` | `0.1849` | `0.1875` | `20,631,351` | 3,853,495.92 USD | -3,872.92 USD | `-0.10%` | -3,620,263.83 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1876` | `0.1876` | `0.1862` | `0.1872` | `11,924,059` | 2,227,884.56 USD | 219,157.27 USD | `+9.84%` | -3,401,106.56 USD | `+0.30` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1871` | `0.1879` | `0.1858` | `0.1877` | `9,619,696` | 1,797,439.11 USD | 188,687.41 USD | `+10.50%` | -3,212,419.15 USD | `+0.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1903` | `0.1910` | `0.1821` | `0.1870` | `239,530,678` | 44,487,434.47 USD | -1,857,528.25 USD | `-4.18%` | -5,671,107.13 USD | `-0.99` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1871` | `0.1887` | `0.1849` | `0.1872` | `76,835,251` | 14,376,224.92 USD | 1,578,173.19 USD | `+10.98%` | -4,092,933.94 USD | `+1.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1871` | `0.1879` | `0.1858` | `0.1877` | `9,619,696` | 1,797,439.11 USD | 188,687.41 USD | `+10.50%` | -3,904,246.53 USD | `+0.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1910` | `0.1821` | `0.1876` | `325,985,710` | 60,661,114.44 USD | -90,671.22 USD | `-0.15%` | -3,130,208.51 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | 1,321,924.30 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 3,089,831.02 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 3,529,363.36 USD | `-0.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,039,537.30 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1910` | `0.1821` | `0.1876` | `325,985,710` | 60,661,114.44 USD | -90,671.22 USD | `-0.15%` | -3,130,208.51 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.1867`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:57:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `541` | `0x77ee...2902` | `SHORT` | 4,057,610.38 USD | `21,412,192.00` | `0.1911` | `0.1894` | `0.5723` | 33,641.36 USD | `+0.83%` | `10X Cross` |
| `1226` | `0x123d...3bff` | `LONG` | 1,779,197.44 USD | `9,392,870.00` | `0.2912` | `0.1894` | `0.000000` | -956,459.28 USD | `-53.76%` | `10X Cross` |
| `1259` | `0x7737...bf66` | `SHORT` | 1,721,923.66 USD | `9,091,466.00` | `0.2190` | `0.1894` | `2.01` | 269,066.14 USD | `+15.63%` | `10X Cross` |
| `1568` | `0x5f94...4b96` | `SHORT` | 1,356,664.79 USD | `7,162,318.00` | `0.2303` | `0.1894` | `0.6917` | 292,810.41 USD | `+21.58%` | `10X Cross` |
| `1794` | `0x4982...59e6` | `SHORT` | 1,136,894.85 USD | `5,998,812.00` | `0.1891` | `0.1894` | `0.4183` | -2,336.49 USD | `-0.21%` | `10X Cross` |
| `1839` | `0xcac1...26b3` | `LONG` | 1,099,612.01 USD | `5,803,927.00` | `0.2000` | `0.1894` | `0.000000` | -61,203.58 USD | `-5.57%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `Live` | `Long Liquidation` | `0.0375` | 105.41 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long` | `0.0375` | 2,340,000.00 USD | 0.00 USD | 105.41 USD | `-79.95%` | `2,811.00` |
| `Live` | `Long` | `0.0385` | 2,340,000.00 USD | 0.00 USD | 323.05 USD | `-79.41%` | `8,391.00` |
| `Live` | `Long` | `0.0445` | 2,340,000.00 USD | 0.00 USD | 883.06 USD | `-76.20%` | `19,844.00` |
| `Live` | `Long` | `0.0575` | 2,340,000.00 USD | 0.00 USD | 294.40 USD | `-69.25%` | `5,120.00` |
| `Live` | `Long` | `0.0605` | 2,340,000.00 USD | 0.00 USD | 544.50 USD | `-67.65%` | `9,000.00` |
| `Live` | `Long` | `0.0635` | 2,340,000.00 USD | 0.00 USD | 338.96 USD | `-66.04%` | `5,338.00` |
| `Live` | `Long` | `0.0645` | 2,340,000.00 USD | 0.00 USD | 1,720.00 USD | `-65.51%` | `26,617.00` |
| `Live` | `Long` | `0.0715` | 2,340,000.00 USD | 0.00 USD | 1,330.00 USD | `-61.76%` | `18,566.00` |
| `Live` | `Long` | `0.0735` | 2,330,000.00 USD | 0.00 USD | 7,720.00 USD | `-60.70%` | `105,008.00` |
| `Live` | `Long` | `0.0765` | 2,330,000.00 USD | 0.00 USD | 10,710.00 USD | `-59.09%` | `140,000.00` |
| `Live` | `Long` | `0.0815` | 2,320,000.00 USD | 0.00 USD | 896.09 USD | `-56.42%` | `10,995.00` |
| `Live` | `Long` | `0.0825` | 2,320,000.00 USD | 0.00 USD | 413.16 USD | `-55.88%` | `5,008.00` |
| `Live` | `Long` | `0.0855` | 2,310,000.00 USD | 0.00 USD | 2,040.00 USD | `-54.28%` | `23,814.00` |
| `Live` | `Long` | `0.0865` | 2,310,000.00 USD | 0.00 USD | 102.50 USD | `-53.74%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,310,000.00 USD | 0.00 USD | 344.75 USD | `-53.21%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,310,000.00 USD | 0.00 USD | 1,150.00 USD | `-52.67%` | `13,050.00` |
| `Live` | `Long` | `0.0895` | 2,310,000.00 USD | 0.00 USD | 4,340.00 USD | `-52.14%` | `48,444.00` |
| `Live` | `Long` | `0.0925` | 2,310,000.00 USD | 0.00 USD | 165.11 USD | `-50.53%` | `1,785.00` |
| `Live` | `Long` | `0.0945` | 2,310,000.00 USD | 0.00 USD | 327.54 USD | `-49.47%` | `3,466.00` |
| `Live` | `Long` | `0.0955` | 2,310,000.00 USD | 0.00 USD | 180,430.00 USD | `-48.93%` | `1,889,331.00` |
| `Live` | `Long` | `0.0975` | 2,130,000.00 USD | 0.00 USD | 975.00 USD | `-47.86%` | `10,000.00` |
| `Live` | `Long` | `0.1025` | 2,120,000.00 USD | 0.00 USD | 4,100.00 USD | `-45.19%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,120,000.00 USD | 0.00 USD | 1,230.00 USD | `-44.65%` | `11,893.00` |
| `Live` | `Long` | `0.1055` | 2,120,000.00 USD | 0.00 USD | 150.44 USD | `-43.58%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,120,000.00 USD | 0.00 USD | 653.70 USD | `-43.05%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,120,000.00 USD | 0.00 USD | 475.58 USD | `-42.51%` | `4,424.00` |
| `Live` | `Long` | `0.1095` | 2,120,000.00 USD | 0.00 USD | 1,490.00 USD | `-41.44%` | `13,608.00` |
| `Live` | `Long` | `0.1105` | 2,120,000.00 USD | 0.00 USD | 380.45 USD | `-40.91%` | `3,443.00` |
| `Live` | `Long` | `0.1145` | 2,120,000.00 USD | 0.00 USD | 5,380.00 USD | `-38.77%` | `46,944.00` |
| `Live` | `Long` | `0.1165` | 2,110,000.00 USD | 0.00 USD | 13,360.00 USD | `-37.70%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,100,000.00 USD | 0.00 USD | 1,640.00 USD | `-37.17%` | `13,927.00` |
| `Live` | `Long` | `0.1185` | 2,100,000.00 USD | 0.00 USD | 122.17 USD | `-36.63%` | `1,031.00` |
| `Live` | `Long` | `0.1205` | 2,100,000.00 USD | 0.00 USD | 826.27 USD | `-35.56%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,090,000.00 USD | 0.00 USD | 1,050.00 USD | `-35.03%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,090,000.00 USD | 0.00 USD | 1,180.00 USD | `-33.96%` | `9,522.00` |
| `Live` | `Long` | `0.1245` | 2,090,000.00 USD | 0.00 USD | 404.62 USD | `-33.42%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,090,000.00 USD | 0.00 USD | 1,980.00 USD | `-32.89%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-32.35%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,090,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.82%` | `13,258.00` |
| `Live` | `Long` | `0.1295` | 2,090,000.00 USD | 0.00 USD | 2,540.00 USD | `-30.75%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,090,000.00 USD | 0.00 USD | 13,060.00 USD | `-30.21%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,070,000.00 USD | 0.00 USD | 687.35 USD | `-29.68%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,070,000.00 USD | 0.00 USD | 10,030.00 USD | `-29.14%` | `75,721.00` |
| `Live` | `Long` | `0.1335` | 2,060,000.00 USD | 0.00 USD | 5,700.00 USD | `-28.61%` | `42,702.00` |
| `Live` | `Long` | `0.1345` | 2,060,000.00 USD | 0.00 USD | 491.46 USD | `-28.07%` | `3,654.00` |
| `Live` | `Long` | `0.1355` | 2,060,000.00 USD | 0.00 USD | 106.64 USD | `-27.54%` | `787.00` |
| `Live` | `Long` | `0.1405` | 2,060,000.00 USD | 0.00 USD | 314.44 USD | `-24.87%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,060,000.00 USD | 0.00 USD | 9,540.00 USD | `-24.33%` | `67,399.00` |
| `Live` | `Long` | `0.1425` | 2,050,000.00 USD | 0.00 USD | 958.46 USD | `-23.80%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,040,000.00 USD | 0.00 USD | 15,780.00 USD | `-23.26%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,030,000.00 USD | 0.00 USD | 2,220.00 USD | `-22.73%` | `15,394.00` |
| `Live` | `Long` | `0.1455` | 2,030,000.00 USD | 0.00 USD | 3,770.00 USD | `-22.19%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 2,020,000.00 USD | 0.00 USD | 33,880.00 USD | `-21.66%` | `231,277.00` |
| `Live` | `Long` | `0.1475` | 1,990,000.00 USD | 0.00 USD | 292.94 USD | `-21.12%` | `1,986.00` |
| `Live` | `Long` | `0.1485` | 1,990,000.00 USD | 0.00 USD | 1,360.00 USD | `-20.59%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 1,990,000.00 USD | 0.00 USD | 427.12 USD | `-20.05%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 1,990,000.00 USD | 0.00 USD | 3,000.00 USD | `-19.52%` | `19,912.00` |
| `Live` | `Long` | `0.1515` | 1,980,000.00 USD | 0.00 USD | 35,710.00 USD | `-18.98%` | `235,729.00` |
| `Live` | `Long` | `0.1525` | 1,950,000.00 USD | 0.00 USD | 5,170.00 USD | `-18.45%` | `33,921.00` |
| `Live` | `Long` | `0.1535` | 1,940,000.00 USD | 0.00 USD | 186,740.00 USD | `-17.91%` | `1,216,555.00` |
| `Live` | `Long` | `0.1545` | 1,760,000.00 USD | 0.00 USD | 1,180.00 USD | `-17.38%` | `7,625.00` |
| `Live` | `Long` | `0.1555` | 1,760,000.00 USD | 0.00 USD | 1,320.00 USD | `-16.84%` | `8,490.00` |
| `Live` | `Long` | `0.1565` | 1,750,000.00 USD | 0.00 USD | 15,260.00 USD | `-16.31%` | `97,517.00` |
| `Live` | `Long` | `0.1575` | 1,740,000.00 USD | 0.00 USD | 4,130.00 USD | `-15.78%` | `26,224.00` |
| `Live` | `Long` | `0.1585` | 1,730,000.00 USD | 0.00 USD | 6,000.00 USD | `-15.24%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,730,000.00 USD | 0.00 USD | 3,340.00 USD | `-14.71%` | `20,936.00` |
| `Live` | `Long` | `0.1605` | 1,730,000.00 USD | 0.00 USD | 58,740.00 USD | `-14.17%` | `365,992.00` |
| `Live` | `Long` | `0.1615` | 1,670,000.00 USD | 0.00 USD | 4,200.00 USD | `-13.64%` | `26,015.00` |
| `Live` | `Long` | `0.1625` | 1,660,000.00 USD | 0.00 USD | 2,870.00 USD | `-13.10%` | `17,647.00` |
| `Live` | `Long` | `0.1635` | 1,660,000.00 USD | 0.00 USD | 552,320.00 USD | `-12.57%` | `3,378,082.00` |
| `Live` | `Long` | `0.1645` | 1,110,000.00 USD | 0.00 USD | 10,840.00 USD | `-12.03%` | `65,896.00` |
| `Live` | `Long` | `0.1665` | 1,100,000.00 USD | 0.00 USD | 1,020.00 USD | `-10.96%` | `6,105.00` |
| `Live` | `Long` | `0.1675` | 1,100,000.00 USD | 0.00 USD | 630.81 USD | `-10.43%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,090,000.00 USD | 0.00 USD | 12,160.00 USD | `-9.89%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,080,000.00 USD | 0.00 USD | 78,180.00 USD | `-9.36%` | `461,249.00` |
| `Live` | `Long` | `0.1705` | 1,000,000.00 USD | 0.00 USD | 627,450.00 USD | `-8.82%` | `3,680,078.00` |
| `Live` | `Long` | `0.1715` | 376,940.00 USD | 0.00 USD | 252,270.00 USD | `-8.29%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 124,660.00 USD | 0.00 USD | 33,550.00 USD | `-7.75%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 91,110.00 USD | 0.00 USD | 1,270.00 USD | `-7.22%` | `7,296.00` |
| `Live` | `Long` | `0.1745` | 89,850.00 USD | 0.00 USD | 234.18 USD | `-6.68%` | `1,342.00` |
| `Live` | `Long` | `0.1755` | 89,610.00 USD | 0.00 USD | 19,070.00 USD | `-6.15%` | `108,645.00` |
| `Live` | `Long` | `0.1765` | 70,550.00 USD | 0.00 USD | 42,760.00 USD | `-5.61%` | `242,276.00` |
| `Live` | `Long` | `0.1775` | 27,790.00 USD | 0.00 USD | 1,230.00 USD | `-5.08%` | `6,907.00` |
| `Live` | `Long` | `0.1785` | 26,560.00 USD | 0.00 USD | 4,530.00 USD | `-4.55%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 22,030.00 USD | 0.00 USD | 1,120.00 USD | `-4.01%` | `6,234.00` |
| `Live` | `Long` | `0.1805` | 20,910.00 USD | 0.00 USD | 3,050.00 USD | `-3.48%` | `16,904.00` |
| `Live` | `Long` | `0.1815` | 17,860.00 USD | 0.00 USD | 11,080.00 USD | `-2.94%` | `61,030.00` |
| `Live` | `Long` | `0.1825` | 6,780.00 USD | 0.00 USD | 6,780.00 USD | `-2.41%` | `37,172.00` |
| `Live` | `Short` | `0.1955` | 425.60 USD | 425.60 USD | 0.00 USD | `+4.55%` | `2,177.00` |
| `Live` | `Short` | `0.1965` | 530.53 USD | 104.93 USD | 0.00 USD | `+5.08%` | `534.00` |
| `Live` | `Short` | `0.1985` | 869.18 USD | 338.64 USD | 0.00 USD | `+6.15%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 1,120.00 USD | 252.97 USD | 0.00 USD | `+6.68%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 3,700.00 USD | 2,570.00 USD | 0.00 USD | `+7.22%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 5,800.00 USD | 2,100.00 USD | 0.00 USD | `+7.75%` | `10,418.00` |
| `Live` | `Short` | `0.2075` | 8,010.00 USD | 2,220.00 USD | 0.00 USD | `+10.96%` | `10,683.00` |
| `Live` | `Short` | `0.2125` | 10,590.00 USD | 2,580.00 USD | 0.00 USD | `+13.64%` | `12,141.00` |
| `Live` | `Short` | `0.2145` | 16,610.00 USD | 6,020.00 USD | 0.00 USD | `+14.71%` | `28,067.00` |
| `Live` | `Short` | `0.2175` | 20,540.00 USD | 3,930.00 USD | 0.00 USD | `+16.31%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 23,190.00 USD | 2,650.00 USD | 0.00 USD | `+16.84%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 24,840.00 USD | 1,640.00 USD | 0.00 USD | `+18.45%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 25,040.00 USD | 200.48 USD | 0.00 USD | `+19.52%` | `897.00` |
| `Live` | `Short` | `0.2265` | 27,270.00 USD | 2,230.00 USD | 0.00 USD | `+21.12%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 36,510.00 USD | 9,240.00 USD | 0.00 USD | `+22.19%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 36,790.00 USD | 282.02 USD | 0.00 USD | `+24.33%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 44,430.00 USD | 7,640.00 USD | 0.00 USD | `+24.87%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 45,900.00 USD | 1,470.00 USD | 0.00 USD | `+28.61%` | `6,110.00` |
| `Live` | `Short` | `0.2415` | 46,440.00 USD | 543.62 USD | 0.00 USD | `+29.14%` | `2,251.00` |
| `Live` | `Short` | `0.2425` | 47,520.00 USD | 1,080.00 USD | 0.00 USD | `+29.68%` | `4,435.00` |
| `Live` | `Short` | `0.2485` | 48,160.00 USD | 648.83 USD | 0.00 USD | `+32.89%` | `2,611.00` |
| `Live` | `Short` | `0.2585` | 49,640.00 USD | 1,480.00 USD | 0.00 USD | `+38.24%` | `5,725.00` |
| `Live` | `Short` | `0.2675` | 51,620.00 USD | 1,970.00 USD | 0.00 USD | `+43.05%` | `7,372.00` |
| `Live` | `Short` | `0.2715` | 51,740.00 USD | 120.00 USD | 0.00 USD | `+45.19%` | `442.00` |
| `Live` | `Short` | `0.2775` | 52,120.00 USD | 379.62 USD | 0.00 USD | `+48.40%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 54,290.00 USD | 2,170.00 USD | 0.00 USD | `+52.14%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 58,610.00 USD | 4,320.00 USD | 0.00 USD | `+54.81%` | `14,924.00` |
| `Live` | `Short` | `0.2915` | 61,870.00 USD | 3,260.00 USD | 0.00 USD | `+55.88%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 127,150.00 USD | 65,270.00 USD | 0.00 USD | `+56.95%` | `222,401.00` |
| `Live` | `Short` | `0.2955` | 135,130.00 USD | 7,990.00 USD | 0.00 USD | `+58.02%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 135,280.00 USD | 146.34 USD | 0.00 USD | `+60.70%` | `487.00` |
| `Live` | `Short` | `0.3035` | 138,760.00 USD | 3,480.00 USD | 0.00 USD | `+62.30%` | `11,458.00` |
| `Live` | `Short` | `0.3045` | 138,890.00 USD | 131.85 USD | 0.00 USD | `+62.83%` | `433.00` |
| `Live` | `Short` | `0.3055` | 139,300.00 USD | 408.15 USD | 0.00 USD | `+63.37%` | `1,336.00` |
| `Live` | `Short` | `0.3125` | 236,800.00 USD | 97,510.00 USD | 0.00 USD | `+67.11%` | `312,021.00` |
| `Live` | `Short` | `0.3145` | 236,950.00 USD | 140.58 USD | 0.00 USD | `+68.18%` | `447.00` |
| `Live` | `Short` | `0.3255` | 238,080.00 USD | 1,140.00 USD | 0.00 USD | `+74.06%` | `3,500.00` |
| `Live` | `Short` | `0.3285` | 238,880.00 USD | 794.97 USD | 0.00 USD | `+75.67%` | `2,420.00` |
| `Live` | `Short` | `0.3295` | 278,630.00 USD | 39,750.00 USD | 0.00 USD | `+76.20%` | `120,640.00` |
| `Live` | `Short` | `0.3365` | 521,160.00 USD | 242,530.00 USD | 0.00 USD | `+79.95%` | `720,753.00` |
| `Live` | `Short` | `0.3375` | 524,130.00 USD | 2,960.00 USD | 0.00 USD | `+80.48%` | `8,785.00` |
| `Live` | `Short` | `0.3425` | 524,510.00 USD | 382.57 USD | 0.00 USD | `+83.16%` | `1,117.00` |
| `Live` | `Short` | `0.3495` | 725,620.00 USD | 201,110.00 USD | 0.00 USD | `+86.90%` | `575,408.00` |
| `Live` | `Short` | `0.3505` | 725,950.00 USD | 331.22 USD | 0.00 USD | `+87.43%` | `945.00` |
| `Live` | `Short` | `0.3515` | 727,070.00 USD | 1,120.00 USD | 0.00 USD | `+87.97%` | `3,187.00` |
| `Live` | `Short` | `0.3545` | 727,390.00 USD | 324.37 USD | 0.00 USD | `+89.57%` | `915.00` |
| `Live` | `Short` | `0.3565` | 727,500.00 USD | 106.95 USD | 0.00 USD | `+90.64%` | `300.00` |
| `Live` | `Short` | `0.3595` | 728,410.00 USD | 914.21 USD | 0.00 USD | `+92.25%` | `2,543.00` |
| `Live` | `Short` | `0.3615` | 731,350.00 USD | 2,940.00 USD | 0.00 USD | `+93.32%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 731,500.00 USD | 143.91 USD | 0.00 USD | `+93.85%` | `397.00` |
| `Live` | `Short` | `0.3715` | 740,670.00 USD | 9,170.00 USD | 0.00 USD | `+98.66%` | `24,689.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 148,060,000.00 USD | 0.00 USD | 415.13 USD | `-68.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 148,060,000.00 USD | 0.00 USD | 438.99 USD | `-67.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 148,060,000.00 USD | 0.00 USD | 1,100.00 USD | `-40.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 148,060,000.00 USD | 0.00 USD | 541.33 USD | `-40.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 148,060,000.00 USD | 0.00 USD | 429.20 USD | `-38.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 148,060,000.00 USD | 0.00 USD | 602,500.00 USD | `-35.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 147,460,000.00 USD | 0.00 USD | 4,460.00 USD | `-33.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 147,450,000.00 USD | 0.00 USD | 1,320.00 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 147,450,000.00 USD | 0.00 USD | 13,390.00 USD | `-30.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 147,440,000.00 USD | 0.00 USD | 728.88 USD | `-29.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 147,440,000.00 USD | 0.00 USD | 4,350.00 USD | `-28.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 147,430,000.00 USD | 0.00 USD | 4,730.00 USD | `-26.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 147,430,000.00 USD | 0.00 USD | 1,820.00 USD | `-25.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 147,430,000.00 USD | 0.00 USD | 1,050.00 USD | `-24.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 147,430,000.00 USD | 0.00 USD | 351.26 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 147,430,000.00 USD | 0.00 USD | 1,600.00 USD | `-23.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 147,430,000.00 USD | 0.00 USD | 10,400.00 USD | `-22.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 147,410,000.00 USD | 0.00 USD | 5,980.00 USD | `-20.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 147,410,000.00 USD | 0.00 USD | 303.26 USD | `-19.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 147,410,000.00 USD | 0.00 USD | 3,230.00 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 147,410,000.00 USD | 0.00 USD | 6,380.00 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 147,400,000.00 USD | 0.00 USD | 126.54 USD | `-17.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 147,400,000.00 USD | 0.00 USD | 1,790.00 USD | `-16.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 147,400,000.00 USD | 0.00 USD | 6,260.00 USD | `-16.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 147,390,000.00 USD | 0.00 USD | 552.21 USD | `-15.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 147,390,000.00 USD | 0.00 USD | 166.84 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 147,390,000.00 USD | 0.00 USD | 9,410.00 USD | `-14.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 147,380,000.00 USD | 0.00 USD | 769.39 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 147,380,000.00 USD | 0.00 USD | 24,760.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 147,360,000.00 USD | 0.00 USD | 6,540.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 147,350,000.00 USD | 0.00 USD | 1,750.00 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 147,350,000.00 USD | 0.00 USD | 5,670.00 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 147,340,000.00 USD | 0.00 USD | 8,020.00 USD | `-10.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 147,330,000.00 USD | 0.00 USD | 951.90 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 147,330,000.00 USD | 0.00 USD | 4,960.00 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 147,330,000.00 USD | 0.00 USD | 1,930.00 USD | `-8.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 147,330,000.00 USD | 0.00 USD | 582.93 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 147,320,000.00 USD | 0.00 USD | 103.58 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 147,320,000.00 USD | 0.00 USD | 74,710.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 147,250,000.00 USD | 0.00 USD | 1,760.00 USD | `-6.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 147,250,000.00 USD | 0.00 USD | 847.38 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 147,250,000.00 USD | 0.00 USD | 4,910.00 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 147,240,000.00 USD | 0.00 USD | 5,400.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 147,240,000.00 USD | 0.00 USD | 8,980.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 147,230,000.00 USD | 0.00 USD | 1,570.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 147,230,000.00 USD | 0.00 USD | 2,720.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 147,220,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-2.41%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 110,720,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-1.87%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 37,320,000.00 USD | 0.00 USD | 18,800.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 37,300,000.00 USD | 0.00 USD | 3,970.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 37,300,000.00 USD | 0.00 USD | 37,300,000.00 USD | `-0.27%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.1875` | 3,580.00 USD | 3,580.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 6,680.00 USD | 3,100.00 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 9,000.00 USD | 2,320.00 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 14,500.00 USD | 5,500.00 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 16,590.00 USD | 2,090.00 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 16,950.00 USD | 362.29 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 17,320.00 USD | 366.68 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 17,710.00 USD | 389.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 18,530.00 USD | 819.54 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 22,180.00 USD | 3,660.00 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 23,190.00 USD | 1,000.00 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 23,830.00 USD | 646.71 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 24,230.00 USD | 399.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 34,770.00 USD | 10,540.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 81,110.00 USD | 46,340.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 81,700.00 USD | 594.34 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 88,910.00 USD | 7,210.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 91,600.00 USD | 2,690.00 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 93,750.00 USD | 2,160.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 93,960.00 USD | 207.74 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 94,270.00 USD | 312.70 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 102,610.00 USD | 8,340.00 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 110,530.00 USD | 7,920.00 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 132,600.00 USD | 22,070.00 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 152,580.00 USD | 19,980.00 USD | 0.00 USD | `+13.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 159,280.00 USD | 6,700.00 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 163,480.00 USD | 4,190.00 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 164,440.00 USD | 965.25 USD | 0.00 USD | `+14.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 174,740.00 USD | 10,300.00 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 175,230.00 USD | 487.34 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 175,340.00 USD | 109.91 USD | 0.00 USD | `+16.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 190,800.00 USD | 15,460.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 193,570.00 USD | 2,760.00 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 195,210.00 USD | 1,650.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 204,220.00 USD | 9,010.00 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 207,970.00 USD | 3,750.00 USD | 0.00 USD | `+19.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 208,090.00 USD | 114.50 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 208,430.00 USD | 339.60 USD | 0.00 USD | `+20.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 208,540.00 USD | 109.40 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 217,640.00 USD | 9,100.00 USD | 0.00 USD | `+21.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 226,780.00 USD | 9,140.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 227,440.00 USD | 662.92 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 227,780.00 USD | 337.06 USD | 0.00 USD | `+23.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 227,950.00 USD | 171.12 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 228,050.00 USD | 101.11 USD | 0.00 USD | `+24.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 229,160.00 USD | 1,110.00 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 238,580.00 USD | 9,420.00 USD | 0.00 USD | `+25.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 238,900.00 USD | 315.96 USD | 0.00 USD | `+26.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 239,670.00 USD | 778.76 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 239,870.00 USD | 192.71 USD | 0.00 USD | `+27.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 240,380.00 USD | 514.45 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 240,590.00 USD | 209.72 USD | 0.00 USD | `+28.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 240,710.00 USD | 115.92 USD | 0.00 USD | `+29.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 240,940.00 USD | 236.19 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 242,090.00 USD | 1,150.00 USD | 0.00 USD | `+30.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 242,380.00 USD | 288.22 USD | 0.00 USD | `+31.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 242,870.00 USD | 491.03 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 244,190.00 USD | 1,320.00 USD | 0.00 USD | `+32.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 254,130.00 USD | 9,940.00 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 254,630.00 USD | 499.00 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 255,730.00 USD | 1,100.00 USD | 0.00 USD | `+33.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 255,900.00 USD | 168.76 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 256,500.00 USD | 603.73 USD | 0.00 USD | `+35.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 258,680.00 USD | 2,170.00 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 260,250.00 USD | 1,570.00 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 261,720.00 USD | 1,470.00 USD | 0.00 USD | `+37.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 261,990.00 USD | 271.44 USD | 0.00 USD | `+38.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 682,890.00 USD | 420,910.00 USD | 0.00 USD | `+39.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 684,070.00 USD | 1,180.00 USD | 0.00 USD | `+41.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 692,970.00 USD | 8,890.00 USD | 0.00 USD | `+43.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 707,830.00 USD | 14,860.00 USD | 0.00 USD | `+43.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 709,170.00 USD | 1,340.00 USD | 0.00 USD | `+44.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 711,880.00 USD | 2,710.00 USD | 0.00 USD | `+45.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 725,750.00 USD | 13,870.00 USD | 0.00 USD | `+46.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 730,960.00 USD | 5,220.00 USD | 0.00 USD | `+46.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 732,140.00 USD | 1,170.00 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 736,290.00 USD | 4,150.00 USD | 0.00 USD | `+48.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 737,240.00 USD | 944.99 USD | 0.00 USD | `+49.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 737,350.00 USD | 113.68 USD | 0.00 USD | `+51.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 738,720.00 USD | 1,370.00 USD | 0.00 USD | `+52.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 739,800.00 USD | 1,080.00 USD | 0.00 USD | `+53.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 754,780.00 USD | 14,980.00 USD | 0.00 USD | `+55.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 756,020.00 USD | 1,230.00 USD | 0.00 USD | `+55.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 757,460.00 USD | 1,440.00 USD | 0.00 USD | `+59.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 757,820.00 USD | 355.21 USD | 0.00 USD | `+60.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 764,470.00 USD | 6,650.00 USD | 0.00 USD | `+60.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 783,450.00 USD | 18,980.00 USD | 0.00 USD | `+63.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 787,600.00 USD | 4,150.00 USD | 0.00 USD | `+64.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 790,840.00 USD | 3,250.00 USD | 0.00 USD | `+68.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 791,340.00 USD | 493.89 USD | 0.00 USD | `+73.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 791,520.00 USD | 181.30 USD | 0.00 USD | `+74.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 792,900.00 USD | 1,380.00 USD | 0.00 USD | `+76.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 805,190.00 USD | 12,290.00 USD | 0.00 USD | `+77.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 805,300.00 USD | 111.06 USD | 0.00 USD | `+78.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 805,520.00 USD | 220.61 USD | 0.00 USD | `+82.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 808,860.00 USD | 3,340.00 USD | 0.00 USD | `+86.90%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `408.45M` | Total OI Tokens: `2,147,208,818.2 ADA`
  * 1h OI Change: `+2.09%` | 4h OI Change: `-2.20%` | 24h OI Change: `-7.15%`
  * Exchange Breakdown: Binance=`75.87M` | Bybit=`50.19M` | OKX=`28.69M` | Hyperliquid=`27.98M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.35K` | Last 24h: `10.44K` | Last 3d: `50.88K` | Last 7d: `82.10K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0043%` |
| **USDT Bybit** | `-0.0131%` | **USDT KuCoin** | `0.0001%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0006%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `55.55%` | `44.45%` | `1.25` | 20,130,000.00 USD |
| `15M` | `Binance` | `58%` | `42%` | `1.38` | 7,830,000.00 USD |
| `15M` | `OKX` | `51.05%` | `48.95%` | `1.04` | 4,910,000.00 USD |
| `15M` | `Bybit` | `58.15%` | `41.85%` | `1.39` | 1,770,000.00 USD |
| `15M` | `KuCoin` | `65.85%` | `34.15%` | `1.93` | 121,860.00 USD |
| `15M` | `Gate` | `49.84%` | `50.16%` | `0.99` | 2,490,000.00 USD |
| `15M` | `Bitget` | `67.15%` | `32.85%` | `2.04` | 474,340.00 USD |
| `15M` | `BingX` | `50.6%` | `49.4%` | `1.02` | 196,430.00 USD |
| `15M` | `MEXC` | `55.3%` | `44.7%` | `1.24` | 882,610.00 USD |
| `15M` | `Bitunix` | `70.82%` | `29.18%` | `2.43` | 604,390.00 USD |
| `15M` | `Hyperliquid` | `64.46%` | `35.54%` | `1.81` | 167,800.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `60.87%` | `39.13%` | `1.56` | 68,520.00 USD |
| `15M` | `Crypto.com` | `43.29%` | `56.71%` | `0.76` | 4,990.00 USD |
| `15M` | `WhiteBIT` | `12.06%` | `87.94%` | `0.14` | 197,380.00 USD |
| `15M` | `HTX` | `70.69%` | `29.31%` | `2.41` | 164,070.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `30.89%` | `69.11%` | `0.45` | 62,360.00 USD |
| `15M` | `Aster` | `69.62%` | `30.38%` | `2.29` | 175,810.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.22%` | `2.78%` | `34.97` | 23,300.00 USD |
| `15M` | `Whale Positions` | `58%` | `42%` | `1.38` | 7,830,000.00 USD |
| `15M` | `Global Accounts` | `55.55%` | `44.45%` | `1.25` | 20,130,000.00 USD |
| `1H` | `ADA` | `53.35%` | `46.65%` | `1.14` | 32,070,000.00 USD |
| `1H` | `Binance` | `54.02%` | `45.98%` | `1.17` | 10,420,000.00 USD |
| `1H` | `OKX` | `50.15%` | `49.85%` | `1.01` | 3,170,000.00 USD |
| `1H` | `Bybit` | `55.67%` | `44.33%` | `1.26` | 3,930,000.00 USD |
| `1H` | `KuCoin` | `51.91%` | `48.09%` | `1.08` | 300,580.00 USD |
| `1H` | `Gate` | `49.19%` | `50.81%` | `0.97` | 1,090,000.00 USD |
| `1H` | `Bitget` | `50.59%` | `49.41%` | `1.02` | 685,720.00 USD |
| `1H` | `BingX` | `53.13%` | `46.87%` | `1.13` | 3,500,000.00 USD |
| `1H` | `MEXC` | `57.97%` | `42.03%` | `1.38` | 2,260,000.00 USD |
| `1H` | `Bitunix` | `53.61%` | `46.39%` | `1.16` | 956,250.00 USD |
| `1H` | `Hyperliquid` | `49.58%` | `50.42%` | `0.98` | 205,180.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.77%` | `45.23%` | `1.21` | 4,930,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `18.61%` | `81.39%` | `0.23` | 222,500.00 USD |
| `1H` | `HTX` | `24.57%` | `75.43%` | `0.33` | 172,160.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.19%` | `51.81%` | `0.93` | 157,650.00 USD |
| `1H` | `Aster` | `46.64%` | `53.36%` | `0.87` | 19,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `12.14%` | `87.86%` | `0.14` | 41,890.00 USD |
| `1H` | `Whale Positions` | `54.02%` | `45.98%` | `1.17` | 10,420,000.00 USD |
| `1H` | `Global Accounts` | `53.35%` | `46.65%` | `1.14` | 32,070,000.00 USD |
| `4H` | `ADA` | `46.49%` | `53.51%` | `0.87` | 542,580,000.00 USD |
| `4H` | `Binance` | `44.56%` | `55.44%` | `0.80` | 203,050,000.00 USD |
| `4H` | `OKX` | `47.66%` | `52.34%` | `0.91` | 120,370,000.00 USD |
| `4H` | `Bybit` | `48.17%` | `51.83%` | `0.93` | 52,270,000.00 USD |
| `4H` | `KuCoin` | `58.07%` | `41.93%` | `1.38` | 4,930,000.00 USD |
| `4H` | `Gate` | `48.76%` | `51.24%` | `0.95` | 47,410,000.00 USD |
| `4H` | `Bitget` | `41.03%` | `58.97%` | `0.70` | 17,840,000.00 USD |
| `4H` | `BingX` | `28.48%` | `71.52%` | `0.40` | 7,420,000.00 USD |
| `4H` | `MEXC` | `48.16%` | `51.84%` | `0.93` | 35,870,000.00 USD |
| `4H` | `Bitunix` | `45.99%` | `54.01%` | `0.85` | 19,330,000.00 USD |
| `4H` | `Hyperliquid` | `44%` | `56%` | `0.79` | 5,600,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.64%` | `42.36%` | `1.36` | 1,730,000.00 USD |
| `4H` | `Crypto.com` | `46.24%` | `53.76%` | `0.86` | 583,590.00 USD |
| `4H` | `WhiteBIT` | `29.91%` | `70.09%` | `0.43` | 4,120,000.00 USD |
| `4H` | `HTX` | `52.55%` | `47.45%` | `1.11` | 12,580,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.9%` | `51.1%` | `0.96` | 1,770,000.00 USD |
| `4H` | `Aster` | `67.84%` | `32.16%` | `2.11` | 7,460,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `54.4%` | `45.6%` | `1.19` | 257,030.00 USD |
| `4H` | `Whale Positions` | `44.56%` | `55.44%` | `0.80` | 203,050,000.00 USD |
| `4H` | `Global Accounts` | `46.49%` | `53.51%` | `0.87` | 542,580,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1900` | `0.1901` | `0.1900` | `0.1910` | `0.1890` | 5,599,303.36 USD | 2,816,754.41 USD | 2,782,548.95 USD | 34,205.46 USD | `+0.61%` | `2B / 0S` |
| `5:00 UTC` | `0.1846` | `0.1850` | `0.1846` | `0.1901` | `0.1822` | 27,794,530.47 USD | 12,619,418.39 USD | 15,175,112.08 USD | -2,555,693.69 USD | `-9.19%` | `3B / 14S` |
| `0:00 UTC` | `0.1840` | `0.1848` | `0.1840` | `0.1865` | `0.1830` | 6,438,750.41 USD | 3,388,925.82 USD | 3,049,824.59 USD | 339,101.24 USD | `+5.27%` | `3B / 0S` |
| `5:00 UTC` | `0.1874` | `0.1869` | `0.1874` | `0.1878` | `0.1855` | 4,653,756.20 USD | 2,488,864.82 USD | 2,164,891.37 USD | 323,973.45 USD | `+6.96%` | `1B / 3S` |
| `0:00 UTC` | `0.1872` | `0.1874` | `0.1872` | `0.1888` | `0.1860` | 5,684,500.06 USD | 3,804,478.59 USD | 1,880,021.47 USD | 1,924,457.12 USD | `+33.85%` | `8B / 1S` |
| `5:00 UTC` | `0.1874` | `0.1874` | `0.1874` | `0.1885` | `0.1865` | 2,610,344.37 USD | 1,024,388.05 USD | 1,585,956.32 USD | -561,568.27 USD | `-21.51%` | `1B / 5S` |
| `0:00 UTC` | `0.1880` | `0.1868` | `0.1880` | `0.1885` | `0.1850` | 3,853,495.92 USD | 1,924,811.50 USD | 1,928,684.42 USD | -3,872.92 USD | `-0.10%` | `4B / 5S` |
| `5:00 UTC` | `0.1866` | `0.1869` | `0.1866` | `0.1876` | `0.1862` | 2,227,884.56 USD | 1,223,520.92 USD | 1,004,363.65 USD | 219,157.27 USD | `+9.84%` | `1B / 1S` |
| `0:00 UTC` | `0.1874` | `0.1870` | `0.1874` | `0.1881` | `0.1859` | 2,036,163.82 USD | 1,133,163.53 USD | 903,000.29 USD | 230,163.23 USD | `+11.30%` | `3B / 0S` |
| `5:00 UTC` | `0.1888` | `0.1886` | `0.1888` | `0.1893` | `0.1880` | 1,263,938.95 USD | 684,455.44 USD | 579,483.51 USD | 104,971.93 USD | `+8.31%` | `3B / 0S` |

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
| `5m` | 25,620.00 USD | -14,200.00 USD | **`ACCUMULATION`** |
| `15m` | 176,510.00 USD | 228,200.00 USD | **`ACCUMULATION`** |
| `30m` | 166,900.00 USD | 543,920.00 USD | **`ACCUMULATION`** |
| `1h` | -36,890.00 USD | 866,570.00 USD | **`ACCUMULATION`** |
| `2h` | -115,230.00 USD | 3,300,000.00 USD | **`ACCUMULATION`** |
| `4h` | -3,440,000.00 USD | -1,490,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -6,710,000.00 USD | -11,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,840,000.00 USD | -13,460,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,530,000.00 USD | -11,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,960,000.00 USD | -9,190,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,820,000.00 USD | -40,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,550,000.00 USD | -199,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+25.62K` | 15m=`+176.51K` | 1h=`-36.89K` | 24h=`-8.96M`
* Futures Capital Netflows: 5m=`-14.20K` | 15m=`+228.20K` | 1h=`+866.57K` | 24h=`-9.19M`
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
  * `2026-10-30 07:16:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:53:25 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:25 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:53:25 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.1796` (Risk Distance: `0.0063` pts)
  * +2.5R Take Profit: `0.2015`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1939` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.2002` (Risk Distance: `0.0063` pts)
  * +2.5R Take Profit: `0.1783`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1882`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
