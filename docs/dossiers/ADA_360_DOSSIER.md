# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:35:24 IST` (`2026-10-30 06:05:24 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1919` | **Live Ask Quote**: `0.1941` | **Mid Price**: `0.1930`
- **Spread Points**: `22.00` | **Spread BPS**: `113.99 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1868` | VWAP Z-Score: `+1.86` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0015` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1950` | Lower -3.00σ Band: `0.1787`
  * Upper +2.51σ Band: `0.1937` | Lower -2.51σ Band: `0.1800`
  * Upper +2.01σ Band: `0.1923` | Lower -2.01σ Band: `0.1814`
  * Upper +2.00σ Band: `0.1923` | Lower -2.00σ Band: `0.1814`
  * Upper +1.28σ Band: `0.1903` | Lower -1.28σ Band: `0.1833`
  * Upper +1.00σ Band: `0.1896` | Lower -1.00σ Band: `0.1841`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1918` | EMA-20=`0.1908` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1922` (Slope: `+0.0000`) | EMA-100=`0.1949`
  * Institutional Anchors: EMA-144=`0.1965` | EMA-200=`0.1980` (Slope: `-0.4249`) | EMA-233=`0.1988`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1925` (Distance: `+0.23%`)
  * Point of Control (POC) = `0.1907` (Distance: `+1.21%`)
  * Value Area Low (VAL) = `0.1858` (Distance: `+3.89%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2065` | Weekly POC=`0.2031` | Weekly VAL=`0.1991`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1935` | Low=`0.1916`
  * New York Session (13:00-21:00 UTC): High=`0.1942` | Low=`0.1918`
  * Initial Balance (First Hour): IB High=`0.1935` | IB Low=`0.1918`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1922` - `0.1938`
  * Optimal Trade Entry (OTE 0.705): `0.1934`
  * Structural Invalidation Anchor (0.786): `0.1945`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1945` | `0.1947` | `0.1942` | `0.1942` | `2,399,480` | 466,536.39 USD | 13,666.57 USD | `+2.93%` | -2,977,265.72 USD | `+0.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1942` | `0.1945` | `0.1941` | `0.1942` | `1,289,841` | 250,677.35 USD | -65,445.48 USD | `-26.11%` | -3,042,711.20 USD | `-0.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1942` | `0.1948` | `0.1940` | `0.1947` | `1,215,329` | 236,269.29 USD | -28,498.08 USD | `-12.06%` | -3,071,209.27 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1931` | `0.1949` | `0.1931` | `0.1942` | `10,319,381` | 2,004,577.31 USD | 69,803.69 USD | `+3.48%` | -3,132,445.16 USD | `+0.10` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1943` | `0.1947` | `0.1941` | `0.1944` | `4,045,009` | 786,211.02 USD | 141,512.88 USD | `+18.00%` | -2,990,932.28 USD | `+0.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1945` | `0.1948` | `0.1940` | `0.1946` | `4,875,954` | 947,898.66 USD | -75,240.10 USD | `-7.94%` | -3,066,172.39 USD | `-0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1891` | `0.1925` | `0.1890` | `0.1922` | `38,552,834` | 7,355,562.18 USD | 283,539.33 USD | `+3.85%` | -2,631,458.62 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1921` | `0.1935` | `0.1912` | `0.1931` | `29,083,424` | 5,598,838.76 USD | -95,129.92 USD | `-1.70%` | -2,726,588.54 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1931` | `0.1949` | `0.1931` | `0.1947` | `19,269,040` | 3,744,271.37 USD | 131,039.58 USD | `+3.50%` | -2,595,548.96 USD | `+0.22` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,580,512.54 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -3,611,263.47 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1949` | `0.1912` | `0.1946` | `48,325,108` | 9,337,786.62 USD | 41,133.48 USD | `+0.44%` | -3,570,129.99 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 2,548,855.78 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,988,388.12 USD | `-0.99` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,580,512.54 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -3,611,263.47 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1949` | `0.1912` | `0.1937` | `51,245,116` | 9,904,955.02 USD | -151,177.13 USD | `-1.53%` | -3,762,440.60 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.1930`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `534` | `0x77ee...2902` | `SHORT` | 4,147,327.47 USD | `21,412,192.00` | `0.1911` | `0.1934` | `0.5746` | -56,075.73 USD | `-1.35%` | `10X Cross` |
| `1214` | `0x123d...3bff` | `LONG` | 1,816,862.84 USD | `9,392,870.00` | `0.2912` | `0.1934` | `0.000000` | -918,793.87 USD | `-50.57%` | `10X Cross` |
| `1257` | `0x7737...bf66` | `SHORT` | 1,760,926.05 USD | `9,091,466.00` | `0.2190` | `0.1934` | `2.06` | 230,063.75 USD | `+13.06%` | `10X Cross` |
| `1555` | `0x5f94...4b96` | `SHORT` | 1,385,407.17 USD | `7,162,318.00` | `0.2303` | `0.1934` | `0.7084` | 264,068.03 USD | `+19.06%` | `10X Cross` |
| `1779` | `0x4982...59e6` | `SHORT` | 1,161,909.90 USD | `5,998,812.00` | `0.1891` | `0.1934` | `0.4058` | -27,351.53 USD | `-2.35%` | `10X Cross` |
| `1831` | `0xcac1...26b3` | `LONG` | 1,122,653.60 USD | `5,803,927.00` | `0.2000` | `0.1934` | `0.000000` | -38,161.99 USD | `-3.40%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1955` | 1,759.77 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Short: 1.76K USD at 0.1955 USD [API] | `2026-10-29 02:31:16` |
| `ANNOUNCEMENT` | `INFO` | `0.1955` | 260.05 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Short: 0.26K USD at 0.1955 USD [API] | `2026-10-29 02:31:16` |
| `ANNOUNCEMENT` | `INFO` | `0.1961` | 5,077.28 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Short: 5.08K USD at 0.1961 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `0.1961` | 6,153.42 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Short: 6.15K USD at 0.1961 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `0.1974` | 6,224.14 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.22K USD at 0.1974 USD [API] | `2026-10-29 03:20:32` |
| `ANNOUNCEMENT` | `INFO` | `0.1978` | 5,527.45 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.53K USD at 0.1978 USD [API] | `2026-10-29 04:20:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1978` | 8,717.68 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 8.72K USD at 0.1978 USD [API] | `2026-10-29 04:20:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1986` | 5,039.04 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.04K USD at 0.1986 USD [API] | `2026-10-29 04:34:55` |
| `ANNOUNCEMENT` | `INFO` | `0.1985` | 5,854.17 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.85K USD at 0.1985 USD [API] | `2026-10-29 04:37:14` |
| `ANNOUNCEMENT` | `INFO` | `0.2130` | 2,032.75 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Short: 2.03K USD at 0.2130 USD [API] | `2026-10-18 19:33:08` |
| `ANNOUNCEMENT` | `INFO` | `0.2007` | 5,006.16 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2007 USD [API] | `2026-10-29 05:24:03` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1953` (Vol: 203,100.00 USD, Dist: `+0.45%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.84%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+7.64%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.86%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 325,500.00 USD, Dist: `+9.95%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.86%`)
  * 7D Horizon: Short MP=`0.2131` (Vol: 448,200.00 USD, Dist: `+9.63%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--5.78%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0405` | 803.68 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 226.87 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 113.79 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 508.50 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 3,030.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 2,110.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 184.12 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 228.96 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 7,400.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 551.25 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,180.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 152,990.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 2,920.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 1,400.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 13,090.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 170.04 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 91,170.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 150.44 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 475.58 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 420.22 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 25,410.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 359.57 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,140.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,150.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,640.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 169.34 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 1,180.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 5,910.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 3,790.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 403.77 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 415.18 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,540.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 958.46 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,220.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 8,370.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 292.94 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 1,360.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 3,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,710.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 981.95 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 73,060.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,910.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 11,760.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 692,170.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 2,780.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,580.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 4,200.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,180.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,840.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 1,050.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 889.94 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 12,160.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 78,180.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 389,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 137,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 7,610,000.00 USD | 7,610,000.00 USD | 80,220.00 USD | 20,820.00 USD | 109,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,270.00 USD | 104,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 7,400,000.00 USD | 7,400,000.00 USD | 14,680.00 USD | 10,530.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1750` | 7,370,000.00 USD | 7,370,000.00 USD | 33,680.00 USD | 4,880.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 18,150.00 USD | 102,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 7,330,000.00 USD | 7,330,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 42,760.00 USD | 84,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 7,270,000.00 USD | 7,270,000.00 USD | 221,260.00 USD | 38,980.00 USD | 111,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 41,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 6,900,000.00 USD | 6,900,000.00 USD | 108,330.00 USD | 25,390.00 USD | 92,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 40,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 6,670,000.00 USD | 6,670,000.00 USD | 150,750.00 USD | 56,560.00 USD | 109,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 36,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 6,350,000.00 USD | 6,350,000.00 USD | 758,290.00 USD | 102,260.00 USD | 195,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 12,610.00 USD | 32,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 5,300,000.00 USD | 5,300,000.00 USD | 150,090.00 USD | 58,550.00 USD | 169,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 11,550.00 USD | 19,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 4,920,000.00 USD | 4,920,000.00 USD | 430,200.00 USD | 95,460.00 USD | 318,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 8,070.00 USD | 8,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 4,080,000.00 USD | 4,080,000.00 USD | 432,250.00 USD | 43,660.00 USD | 65,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1840` | 3,530,000.00 USD | 3,530,000.00 USD | 326,870.00 USD | 61,300.00 USD | 125,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1850` | 3,020,000.00 USD | 3,020,000.00 USD | 19,720.00 USD | 25,410.00 USD | 92,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 2,880,000.00 USD | 2,880,000.00 USD | 134,830.00 USD | 13,940.00 USD | 394,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 2,340,000.00 USD | 2,340,000.00 USD | 51,230.00 USD | 32,210.00 USD | 473,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 1,780,000.00 USD | 1,780,000.00 USD | 176,700.00 USD | 134,410.00 USD | 75,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 1,400,000.00 USD | 1,400,000.00 USD | 199,620.00 USD | 9,630.00 USD | 46,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,140,000.00 USD | 1,140,000.00 USD | 17,850.00 USD | 66,810.00 USD | 226,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 829,570.00 USD | 829,570.00 USD | 620,270.00 USD | 50,700.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 134,620.00 USD | 134,620.00 USD | 0.00 USD | 0.00 USD | 134,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 559,090.00 USD | 559,090.00 USD | 386,280.00 USD | 2,420.00 USD | 170,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 1,120,000.00 USD | 1,120,000.00 USD | 386,280.00 USD | 2,420.00 USD | 170,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 2,160,000.00 USD | 2,160,000.00 USD | 608,960.00 USD | 74,250.00 USD | 356,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 2,840,000.00 USD | 2,840,000.00 USD | 198,740.00 USD | 73,330.00 USD | 414,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 555.61 USD | 555.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1960` | 3,840,000.00 USD | 3,840,000.00 USD | 387,530.00 USD | 204,390.00 USD | 403,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 660.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 4,200,000.00 USD | 4,200,000.00 USD | 27,170.00 USD | 87,190.00 USD | 243,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 187.03 USD | 847.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1980` | 4,890,000.00 USD | 4,890,000.00 USD | 334,230.00 USD | 49,040.00 USD | 304,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 1,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 5,420,000.00 USD | 5,420,000.00 USD | 183,200.00 USD | 63,150.00 USD | 291,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 1,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 6,140,000.00 USD | 6,140,000.00 USD | 321,810.00 USD | 50,750.00 USD | 339,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 4,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 6,710,000.00 USD | 6,710,000.00 USD | 124,750.00 USD | 148,270.00 USD | 303,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 2,100.00 USD | 6,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 7,090,000.00 USD | 7,090,000.00 USD | 184,800.00 USD | 44,340.00 USD | 146,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2030` | 7,520,000.00 USD | 7,520,000.00 USD | 109,180.00 USD | 90,080.00 USD | 231,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 7,840,000.00 USD | 7,840,000.00 USD | 69,130.00 USD | 119,990.00 USD | 133,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 8,010,000.00 USD | 8,010,000.00 USD | 84,210.00 USD | 31,180.00 USD | 52,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 8,440,000.00 USD | 8,440,000.00 USD | 308,720.00 USD | 30,930.00 USD | 94,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 9,120,000.00 USD | 9,120,000.00 USD | 305,180.00 USD | 129,660.00 USD | 241,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2075` | 2,220.00 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2080` | 9,620,000.00 USD | 9,620,000.00 USD | 363,130.00 USD | 94,950.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 10,570,000.00 USD | 10,570,000.00 USD | 492,560.00 USD | 155,040.00 USD | 300,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 11,350,000.00 USD | 11,350,000.00 USD | 468,900.00 USD | 103,900.00 USD | 210,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 11,630,000.00 USD | 11,630,000.00 USD | 136,950.00 USD | 33,760.00 USD | 105,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 11,970,000.00 USD | 11,970,000.00 USD | 128,320.00 USD | 81,120.00 USD | 130,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 460.70 USD | 8,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 12,290,000.00 USD | 12,290,000.00 USD | 195,470.00 USD | 48,090.00 USD | 80,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 12,480,000.00 USD | 12,480,000.00 USD | 130,000.00 USD | 31,520.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 12,510,000.00 USD | 12,510,000.00 USD | 19,320.00 USD | 5,490.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 12,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 2,650.00 USD | 15,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2195` | 2,300.00 USD | 17,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 996.75 USD | 18,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 18,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 21,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 30,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 30,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 38,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 620.11 USD | 38,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,670.00 USD | 40,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 680.06 USD | 41,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 3,160.00 USD | 44,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 1,070.00 USD | 45,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 45,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 1,970.00 USD | 47,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 47,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 48,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 50,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 50,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 54,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 54,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 62,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2965` | 1,100.00 USD | 63,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 63,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 4,240.00 USD | 68,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 69,670.00 USD | 137,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,190.00 USD | 235,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3165` | 3,630.00 USD | 238,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 1,110.00 USD | 239,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3185` | 302.57 USD | 240,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3225` | 36,580.00 USD | 276,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 2,870.00 USD | 279,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 3,180.00 USD | 282,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3415` | 196,500.00 USD | 479,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3435` | 245.95 USD | 479,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 331.22 USD | 479,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,120.00 USD | 480,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3555` | 325.28 USD | 481,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 249.91 USD | 481,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 2,940.00 USD | 484,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 143.91 USD | 484,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3635` | 261,990.00 USD | 746,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3665` | 163.83 USD | 746,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 755,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3735` | 949.81 USD | 756,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 759,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3765` | 23,900.00 USD | 783,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0395` | 2,420,000.00 USD | 0.00 USD | 783.84 USD | `-79.56%` | `19,844.00` |
| `Live` | `Long` | `0.0525` | 2,420,000.00 USD | 0.00 USD | 490.51 USD | `-72.84%` | `9,343.00` |
| `Live` | `Long` | `0.0545` | 2,420,000.00 USD | 0.00 USD | 115.92 USD | `-71.80%` | `2,127.00` |
| `Live` | `Long` | `0.0555` | 2,420,000.00 USD | 0.00 USD | 2,690.00 USD | `-71.29%` | `48,444.00` |
| `Live` | `Long` | `0.0575` | 2,420,000.00 USD | 0.00 USD | 197.97 USD | `-70.25%` | `3,443.00` |
| `Live` | `Long` | `0.0585` | 2,420,000.00 USD | 0.00 USD | 1,920.00 USD | `-69.73%` | `32,814.00` |
| `Live` | `Long` | `0.0645` | 2,420,000.00 USD | 0.00 USD | 483.75 USD | `-66.63%` | `7,500.00` |
| `Live` | `Long` | `0.0685` | 2,420,000.00 USD | 0.00 USD | 192.55 USD | `-64.56%` | `2,811.00` |
| `Live` | `Long` | `0.0695` | 2,420,000.00 USD | 0.00 USD | 1,090.00 USD | `-64.04%` | `15,628.00` |
| `Live` | `Long` | `0.0705` | 2,420,000.00 USD | 0.00 USD | 7,400.00 USD | `-63.53%` | `105,008.00` |
| `Live` | `Long` | `0.0785` | 2,410,000.00 USD | 0.00 USD | 147,090.00 USD | `-59.39%` | `1,873,703.00` |
| `Live` | `Long` | `0.0815` | 2,260,000.00 USD | 0.00 USD | 284.84 USD | `-57.84%` | `3,495.00` |
| `Live` | `Long` | `0.0855` | 2,260,000.00 USD | 0.00 USD | 1,710.00 USD | `-55.77%` | `20,000.00` |
| `Live` | `Long` | `0.0865` | 2,260,000.00 USD | 0.00 USD | 102.50 USD | `-55.25%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,260,000.00 USD | 0.00 USD | 344.75 USD | `-54.73%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,260,000.00 USD | 0.00 USD | 1,150.00 USD | `-54.21%` | `13,050.00` |
| `Live` | `Long` | `0.0925` | 2,260,000.00 USD | 0.00 USD | 1,090.00 USD | `-52.14%` | `11,785.00` |
| `Live` | `Long` | `0.0945` | 2,260,000.00 USD | 0.00 USD | 327.54 USD | `-51.11%` | `3,466.00` |
| `Live` | `Long` | `0.0965` | 2,260,000.00 USD | 0.00 USD | 168.30 USD | `-50.08%` | `1,744.00` |
| `Live` | `Long` | `0.0985` | 2,260,000.00 USD | 0.00 USD | 91,170.00 USD | `-49.04%` | `925,538.00` |
| `Live` | `Long` | `0.0995` | 2,170,000.00 USD | 0.00 USD | 117.61 USD | `-48.52%` | `1,182.00` |
| `Live` | `Long` | `0.1005` | 2,170,000.00 USD | 0.00 USD | 14,170.00 USD | `-48.01%` | `141,031.00` |
| `Live` | `Long` | `0.1025` | 2,150,000.00 USD | 0.00 USD | 34,080.00 USD | `-46.97%` | `332,456.00` |
| `Live` | `Long` | `0.1035` | 2,120,000.00 USD | 0.00 USD | 1,050.00 USD | `-46.45%` | `10,149.00` |
| `Live` | `Long` | `0.1055` | 2,120,000.00 USD | 0.00 USD | 150.44 USD | `-45.42%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,120,000.00 USD | 0.00 USD | 653.70 USD | `-44.90%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,120,000.00 USD | 0.00 USD | 475.58 USD | `-44.38%` | `4,424.00` |
| `Live` | `Long` | `0.1085` | 2,110,000.00 USD | 0.00 USD | 420.22 USD | `-43.87%` | `3,873.00` |
| `Live` | `Long` | `0.1095` | 2,110,000.00 USD | 0.00 USD | 1,840.00 USD | `-43.35%` | `16,776.00` |
| `Live` | `Long` | `0.1145` | 2,110,000.00 USD | 0.00 USD | 862.64 USD | `-40.76%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,110,000.00 USD | 0.00 USD | 13,150.00 USD | `-39.73%` | `112,888.00` |
| `Live` | `Long` | `0.1175` | 2,100,000.00 USD | 0.00 USD | 1,640.00 USD | `-39.21%` | `13,927.00` |
| `Live` | `Long` | `0.1185` | 2,100,000.00 USD | 0.00 USD | 169.34 USD | `-38.69%` | `1,429.00` |
| `Live` | `Long` | `0.1205` | 2,100,000.00 USD | 0.00 USD | 826.27 USD | `-37.66%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,100,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.14%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,090,000.00 USD | 0.00 USD | 1,180.00 USD | `-36.11%` | `9,522.00` |
| `Live` | `Long` | `0.1245` | 2,090,000.00 USD | 0.00 USD | 404.62 USD | `-35.59%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,090,000.00 USD | 0.00 USD | 1,980.00 USD | `-35.07%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-34.55%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,090,000.00 USD | 0.00 USD | 1,260.00 USD | `-34.04%` | `9,873.00` |
| `Live` | `Long` | `0.1285` | 2,090,000.00 USD | 0.00 USD | 3,150.00 USD | `-33.52%` | `24,507.00` |
| `Live` | `Long` | `0.1295` | 2,090,000.00 USD | 0.00 USD | 2,540.00 USD | `-33.00%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,080,000.00 USD | 0.00 USD | 13,060.00 USD | `-32.48%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,070,000.00 USD | 0.00 USD | 687.35 USD | `-31.97%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,070,000.00 USD | 0.00 USD | 6,960.00 USD | `-31.45%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,060,000.00 USD | 0.00 USD | 5,910.00 USD | `-30.93%` | `44,280.00` |
| `Live` | `Long` | `0.1355` | 2,060,000.00 USD | 0.00 USD | 106.64 USD | `-29.90%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,060,000.00 USD | 0.00 USD | 403.77 USD | `-29.38%` | `2,958.00` |
| `Live` | `Long` | `0.1405` | 2,060,000.00 USD | 0.00 USD | 314.44 USD | `-27.31%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,060,000.00 USD | 0.00 USD | 9,540.00 USD | `-26.79%` | `67,399.00` |
| `Live` | `Long` | `0.1425` | 2,050,000.00 USD | 0.00 USD | 958.46 USD | `-26.28%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,050,000.00 USD | 0.00 USD | 15,780.00 USD | `-25.76%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,030,000.00 USD | 0.00 USD | 2,220.00 USD | `-25.24%` | `15,394.00` |
| `Live` | `Long` | `0.1455` | 2,030,000.00 USD | 0.00 USD | 7,530.00 USD | `-24.72%` | `51,752.00` |
| `Live` | `Long` | `0.1465` | 2,020,000.00 USD | 0.00 USD | 4,580.00 USD | `-24.21%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,020,000.00 USD | 0.00 USD | 1,070.00 USD | `-23.69%` | `7,270.00` |
| `Live` | `Long` | `0.1485` | 2,010,000.00 USD | 0.00 USD | 1,360.00 USD | `-23.17%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 2,010,000.00 USD | 0.00 USD | 427.12 USD | `-22.66%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 2,010,000.00 USD | 0.00 USD | 3,000.00 USD | `-22.14%` | `19,912.00` |
| `Live` | `Long` | `0.1515` | 2,010,000.00 USD | 0.00 USD | 35,830.00 USD | `-21.62%` | `236,501.00` |
| `Live` | `Long` | `0.1525` | 1,970,000.00 USD | 0.00 USD | 981.95 USD | `-21.10%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 1,970,000.00 USD | 0.00 USD | 73,980.00 USD | `-20.59%` | `481,961.00` |
| `Live` | `Long` | `0.1545` | 1,900,000.00 USD | 0.00 USD | 2,030.00 USD | `-20.07%` | `13,156.00` |
| `Live` | `Long` | `0.1555` | 1,900,000.00 USD | 0.00 USD | 1,250.00 USD | `-19.55%` | `8,067.00` |
| `Live` | `Long` | `0.1565` | 1,900,000.00 USD | 0.00 USD | 539,530.00 USD | `-19.03%` | `3,447,463.00` |
| `Live` | `Long` | `0.1575` | 1,360,000.00 USD | 0.00 USD | 160,120.00 USD | `-18.52%` | `1,016,653.00` |
| `Live` | `Long` | `0.1585` | 1,200,000.00 USD | 0.00 USD | 6,000.00 USD | `-18.00%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,190,000.00 USD | 0.00 USD | 2,780.00 USD | `-17.48%` | `17,408.00` |
| `Live` | `Long` | `0.1605` | 1,190,000.00 USD | 0.00 USD | 57,580.00 USD | `-16.96%` | `358,740.00` |
| `Live` | `Long` | `0.1615` | 1,130,000.00 USD | 0.00 USD | 4,200.00 USD | `-16.45%` | `26,015.00` |
| `Live` | `Long` | `0.1625` | 1,130,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.93%` | `13,446.00` |
| `Live` | `Long` | `0.1645` | 1,120,000.00 USD | 0.00 USD | 10,840.00 USD | `-14.89%` | `65,896.00` |
| `Live` | `Long` | `0.1665` | 1,110,000.00 USD | 0.00 USD | 889.94 USD | `-13.86%` | `5,345.00` |
| `Live` | `Long` | `0.1675` | 1,110,000.00 USD | 0.00 USD | 1,690.00 USD | `-13.34%` | `10,103.00` |
| `Live` | `Long` | `0.1685` | 1,110,000.00 USD | 0.00 USD | 12,160.00 USD | `-12.83%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,100,000.00 USD | 0.00 USD | 79,290.00 USD | `-12.31%` | `467,760.00` |
| `Live` | `Long` | `0.1705` | 1,020,000.00 USD | 0.00 USD | 626,600.00 USD | `-11.79%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 392,240.00 USD | 0.00 USD | 252,270.00 USD | `-11.27%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 139,970.00 USD | 0.00 USD | 33,550.00 USD | `-10.76%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 106,420.00 USD | 0.00 USD | 1,270.00 USD | `-10.24%` | `7,296.00` |
| `Live` | `Long` | `0.1755` | 105,160.00 USD | 0.00 USD | 18,150.00 USD | `-9.20%` | `103,409.00` |
| `Live` | `Long` | `0.1765` | 87,010.00 USD | 0.00 USD | 42,760.00 USD | `-8.69%` | `242,276.00` |
| `Live` | `Long` | `0.1775` | 44,250.00 USD | 0.00 USD | 1,360.00 USD | `-8.17%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 42,890.00 USD | 0.00 USD | 4,530.00 USD | `-7.65%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 38,360.00 USD | 0.00 USD | 3,840.00 USD | `-7.13%` | `21,396.00` |
| `Live` | `Long` | `0.1805` | 34,520.00 USD | 0.00 USD | 12,610.00 USD | `-6.62%` | `69,840.00` |
| `Live` | `Long` | `0.1815` | 21,910.00 USD | 0.00 USD | 11,550.00 USD | `-6.10%` | `63,611.00` |
| `Live` | `Long` | `0.1825` | 10,370.00 USD | 0.00 USD | 8,070.00 USD | `-5.58%` | `44,212.00` |
| `Live` | `Long` | `0.1845` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | `-4.55%` | `12,457.00` |
| `Live` | `Short` | `0.1955` | 555.61 USD | 555.61 USD | 0.00 USD | `+1.14%` | `2,842.00` |
| `Live` | `Short` | `0.1965` | 660.54 USD | 104.93 USD | 0.00 USD | `+1.66%` | `534.00` |
| `Live` | `Short` | `0.1975` | 847.57 USD | 187.03 USD | 0.00 USD | `+2.18%` | `947.00` |
| `Live` | `Short` | `0.1985` | 1,190.00 USD | 338.64 USD | 0.00 USD | `+2.70%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 1,440.00 USD | 252.97 USD | 0.00 USD | `+3.21%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 4,010.00 USD | 2,570.00 USD | 0.00 USD | `+3.73%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 6,110.00 USD | 2,100.00 USD | 0.00 USD | `+4.25%` | `10,418.00` |
| `Live` | `Short` | `0.2075` | 8,330.00 USD | 2,220.00 USD | 0.00 USD | `+7.35%` | `10,683.00` |
| `Live` | `Short` | `0.2155` | 8,800.00 USD | 467.20 USD | 0.00 USD | `+11.49%` | `2,168.00` |
| `Live` | `Short` | `0.2175` | 12,730.00 USD | 3,930.00 USD | 0.00 USD | `+12.53%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 15,380.00 USD | 2,650.00 USD | 0.00 USD | `+13.04%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 16,370.00 USD | 996.75 USD | 0.00 USD | `+14.59%` | `4,500.00` |
| `Live` | `Short` | `0.2235` | 16,570.00 USD | 200.48 USD | 0.00 USD | `+15.63%` | `897.00` |
| `Live` | `Short` | `0.2265` | 18,810.00 USD | 2,230.00 USD | 0.00 USD | `+17.18%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 28,040.00 USD | 9,240.00 USD | 0.00 USD | `+18.22%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 28,330.00 USD | 282.02 USD | 0.00 USD | `+20.29%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 35,960.00 USD | 7,640.00 USD | 0.00 USD | `+20.80%` | `32,708.00` |
| `Live` | `Short` | `0.2375` | 36,580.00 USD | 620.11 USD | 0.00 USD | `+22.87%` | `2,611.00` |
| `Live` | `Short` | `0.2405` | 38,260.00 USD | 1,670.00 USD | 0.00 USD | `+24.42%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 38,940.00 USD | 680.06 USD | 0.00 USD | `+24.94%` | `2,816.00` |
| `Live` | `Short` | `0.2425` | 42,090.00 USD | 3,160.00 USD | 0.00 USD | `+25.46%` | `13,019.00` |
| `Live` | `Short` | `0.2565` | 43,190.00 USD | 1,090.00 USD | 0.00 USD | `+32.70%` | `4,254.00` |
| `Live` | `Short` | `0.2585` | 43,570.00 USD | 380.25 USD | 0.00 USD | `+33.74%` | `1,471.00` |
| `Live` | `Short` | `0.2675` | 45,540.00 USD | 1,970.00 USD | 0.00 USD | `+38.39%` | `7,372.00` |
| `Live` | `Short` | `0.2695` | 45,950.00 USD | 416.11 USD | 0.00 USD | `+39.43%` | `1,544.00` |
| `Live` | `Short` | `0.2715` | 46,070.00 USD | 120.00 USD | 0.00 USD | `+40.46%` | `442.00` |
| `Live` | `Short` | `0.2755` | 47,100.00 USD | 1,020.00 USD | 0.00 USD | `+42.53%` | `3,713.00` |
| `Live` | `Short` | `0.2775` | 47,480.00 USD | 379.62 USD | 0.00 USD | `+43.57%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 49,650.00 USD | 2,170.00 USD | 0.00 USD | `+47.19%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 50,060.00 USD | 411.09 USD | 0.00 USD | `+49.77%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 53,320.00 USD | 3,260.00 USD | 0.00 USD | `+50.81%` | `11,194.00` |
| `Live` | `Short` | `0.2925` | 53,550.00 USD | 221.71 USD | 0.00 USD | `+51.33%` | `758.00` |
| `Live` | `Short` | `0.2935` | 54,070.00 USD | 519.79 USD | 0.00 USD | `+51.84%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 62,050.00 USD | 7,990.00 USD | 0.00 USD | `+52.88%` | `27,027.00` |
| `Live` | `Short` | `0.2995` | 62,340.00 USD | 284.52 USD | 0.00 USD | `+54.95%` | `950.00` |
| `Live` | `Short` | `0.3005` | 62,480.00 USD | 146.34 USD | 0.00 USD | `+55.47%` | `487.00` |
| `Live` | `Short` | `0.3045` | 62,610.00 USD | 131.85 USD | 0.00 USD | `+57.54%` | `433.00` |
| `Live` | `Short` | `0.3055` | 67,150.00 USD | 4,530.00 USD | 0.00 USD | `+58.05%` | `14,840.00` |
| `Live` | `Short` | `0.3065` | 68,220.00 USD | 1,070.00 USD | 0.00 USD | `+58.57%` | `3,500.00` |
| `Live` | `Short` | `0.3075` | 137,730.00 USD | 69,510.00 USD | 0.00 USD | `+59.09%` | `226,047.00` |
| `Live` | `Short` | `0.3115` | 234,920.00 USD | 97,190.00 USD | 0.00 USD | `+61.16%` | `312,021.00` |
| `Live` | `Short` | `0.3155` | 237,700.00 USD | 2,770.00 USD | 0.00 USD | `+63.23%` | `8,785.00` |
| `Live` | `Short` | `0.3215` | 241,380.00 USD | 3,680.00 USD | 0.00 USD | `+66.33%` | `11,458.00` |
| `Live` | `Short` | `0.3225` | 277,960.00 USD | 36,580.00 USD | 0.00 USD | `+66.85%` | `113,421.00` |
| `Live` | `Short` | `0.3275` | 278,750.00 USD | 792.55 USD | 0.00 USD | `+69.43%` | `2,420.00` |
| `Live` | `Short` | `0.3295` | 281,130.00 USD | 2,380.00 USD | 0.00 USD | `+70.47%` | `7,219.00` |
| `Live` | `Short` | `0.3375` | 281,370.00 USD | 241.65 USD | 0.00 USD | `+74.61%` | `716.00` |
| `Live` | `Short` | `0.3475` | 281,690.00 USD | 317.96 USD | 0.00 USD | `+79.78%` | `915.00` |
| `Live` | `Short` | `0.3505` | 282,020.00 USD | 331.22 USD | 0.00 USD | `+81.33%` | `945.00` |
| `Live` | `Short` | `0.3515` | 485,400.00 USD | 203,380.00 USD | 0.00 USD | `+81.85%` | `578,595.00` |
| `Live` | `Short` | `0.3595` | 485,540.00 USD | 144.16 USD | 0.00 USD | `+85.99%` | `401.00` |
| `Live` | `Short` | `0.3615` | 488,480.00 USD | 2,940.00 USD | 0.00 USD | `+87.02%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 488,630.00 USD | 143.91 USD | 0.00 USD | `+87.54%` | `397.00` |
| `Live` | `Short` | `0.3665` | 488,990.00 USD | 366.50 USD | 0.00 USD | `+89.61%` | `1,000.00` |
| `Live` | `Short` | `0.3705` | 512,510.00 USD | 23,520.00 USD | 0.00 USD | `+91.68%` | `63,484.00` |
| `Live` | `Short` | `0.3715` | 789,440.00 USD | 276,930.00 USD | 0.00 USD | `+92.20%` | `745,442.00` |
| `Live` | `Short` | `0.3725` | 789,610.00 USD | 166.51 USD | 0.00 USD | `+92.72%` | `447.00` |
| `Live` | `Short` | `0.3745` | 792,750.00 USD | 3,140.00 USD | 0.00 USD | `+93.75%` | `8,395.00` |
| `Live` | `Short` | `0.3765` | 793,710.00 USD | 957.44 USD | 0.00 USD | `+94.79%` | `2,543.00` |
| `Live` | `Short` | `0.3805` | 794,190.00 USD | 475.62 USD | 0.00 USD | `+96.85%` | `1,250.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 110,710,000.00 USD | 0.00 USD | 415.13 USD | `-69.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 110,710,000.00 USD | 0.00 USD | 438.99 USD | `-68.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 110,710,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 110,710,000.00 USD | 0.00 USD | 541.33 USD | `-42.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 110,710,000.00 USD | 0.00 USD | 429.20 USD | `-40.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 110,710,000.00 USD | 0.00 USD | 602,500.00 USD | `-37.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 110,100,000.00 USD | 0.00 USD | 4,460.00 USD | `-36.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 110,100,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 110,100,000.00 USD | 0.00 USD | 13,390.00 USD | `-32.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 110,080,000.00 USD | 0.00 USD | 728.88 USD | `-31.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 110,080,000.00 USD | 0.00 USD | 4,350.00 USD | `-30.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 110,080,000.00 USD | 0.00 USD | 4,730.00 USD | `-28.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 110,070,000.00 USD | 0.00 USD | 1,820.00 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 110,070,000.00 USD | 0.00 USD | 1,050.00 USD | `-26.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 110,070,000.00 USD | 0.00 USD | 351.26 USD | `-26.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 110,070,000.00 USD | 0.00 USD | 1,600.00 USD | `-25.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 110,070,000.00 USD | 0.00 USD | 10,400.00 USD | `-24.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 110,060,000.00 USD | 0.00 USD | 5,980.00 USD | `-22.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 110,050,000.00 USD | 0.00 USD | 303.26 USD | `-22.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 110,050,000.00 USD | 0.00 USD | 3,230.00 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 110,050,000.00 USD | 0.00 USD | 6,380.00 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 110,040,000.00 USD | 0.00 USD | 126.54 USD | `-20.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 110,040,000.00 USD | 0.00 USD | 1,790.00 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 110,040,000.00 USD | 0.00 USD | 6,260.00 USD | `-19.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 110,030,000.00 USD | 0.00 USD | 552.21 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 110,030,000.00 USD | 0.00 USD | 166.84 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 110,030,000.00 USD | 0.00 USD | 9,410.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 110,020,000.00 USD | 0.00 USD | 769.39 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 110,020,000.00 USD | 0.00 USD | 24,760.00 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 110,000,000.00 USD | 0.00 USD | 6,540.00 USD | `-15.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 109,990,000.00 USD | 0.00 USD | 1,750.00 USD | `-14.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 109,990,000.00 USD | 0.00 USD | 452.97 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 109,990,000.00 USD | 0.00 USD | 12,640.00 USD | `-13.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 109,980,000.00 USD | 0.00 USD | 317.92 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 109,980,000.00 USD | 0.00 USD | 4,270.00 USD | `-12.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 109,970,000.00 USD | 0.00 USD | 1,300.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 109,970,000.00 USD | 0.00 USD | 1,220.00 USD | `-11.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 109,970,000.00 USD | 0.00 USD | 640.67 USD | `-10.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 109,970,000.00 USD | 0.00 USD | 595.80 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 109,970,000.00 USD | 0.00 USD | 885.06 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 109,970,000.00 USD | 0.00 USD | 1,760.00 USD | `-9.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 109,970,000.00 USD | 0.00 USD | 847.38 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 109,970,000.00 USD | 0.00 USD | 5,090.00 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 109,960,000.00 USD | 0.00 USD | 5,400.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 109,960,000.00 USD | 0.00 USD | 15,050.00 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 109,940,000.00 USD | 0.00 USD | 1,570.00 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 109,940,000.00 USD | 0.00 USD | 2,720.00 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 109,940,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-5.58%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 73,440,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-5.06%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 35,770.00 USD | 0.00 USD | 18,800.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 16,970.00 USD | 0.00 USD | 3,970.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 13,000.00 USD | 0.00 USD | 1,420.00 USD | `-3.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 11,580.00 USD | 0.00 USD | 3,580.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 8,000.00 USD | 0.00 USD | 3,100.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 4,900.00 USD | 0.00 USD | 2,320.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 2,580.00 USD | 0.00 USD | 126.49 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 2,450.00 USD | 0.00 USD | 2,090.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 362.29 USD | 0.00 USD | 362.29 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 1,780.00 USD | 389.00 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 2,030.00 USD | 247.89 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 5,680.00 USD | 3,660.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 6,680.00 USD | 1,000.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 7,330.00 USD | 646.71 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 7,730.00 USD | 399.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 24,590.00 USD | 16,860.00 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 70,930.00 USD | 46,340.00 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 71,520.00 USD | 594.34 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 78,730.00 USD | 7,210.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 81,420.00 USD | 2,690.00 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 83,570.00 USD | 2,160.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 83,780.00 USD | 207.74 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 84,090.00 USD | 312.70 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 92,430.00 USD | 8,340.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 100,580.00 USD | 8,150.00 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 122,660.00 USD | 22,070.00 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 142,480.00 USD | 19,820.00 USD | 0.00 USD | `+9.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 149,180.00 USD | 6,700.00 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 153,380.00 USD | 4,190.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 154,340.00 USD | 965.25 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 164,640.00 USD | 10,300.00 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 165,250.00 USD | 609.66 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 165,360.00 USD | 109.91 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 180,830.00 USD | 15,460.00 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 183,590.00 USD | 2,760.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 185,240.00 USD | 1,650.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 194,420.00 USD | 9,180.00 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 198,170.00 USD | 3,750.00 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 198,280.00 USD | 114.50 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 198,620.00 USD | 339.60 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 198,730.00 USD | 109.40 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 198,880.00 USD | 151.06 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 208,020.00 USD | 9,140.00 USD | 0.00 USD | `+18.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 208,690.00 USD | 662.92 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 209,020.00 USD | 337.06 USD | 0.00 USD | `+19.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 209,190.00 USD | 171.12 USD | 0.00 USD | `+20.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 209,290.00 USD | 101.11 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 210,400.00 USD | 1,110.00 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 219,820.00 USD | 9,420.00 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 220,270.00 USD | 443.91 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 221,050.00 USD | 778.76 USD | 0.00 USD | `+22.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 221,240.00 USD | 192.71 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 221,750.00 USD | 514.45 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 221,960.00 USD | 209.72 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 222,080.00 USD | 115.92 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 222,320.00 USD | 236.19 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 223,460.00 USD | 1,150.00 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 223,750.00 USD | 288.22 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 224,240.00 USD | 491.03 USD | 0.00 USD | `+27.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 225,570.00 USD | 1,320.00 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 235,510.00 USD | 9,940.00 USD | 0.00 USD | `+28.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 236,010.00 USD | 499.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 237,110.00 USD | 1,100.00 USD | 0.00 USD | `+29.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 237,270.00 USD | 168.76 USD | 0.00 USD | `+30.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 237,880.00 USD | 603.73 USD | 0.00 USD | `+30.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 240,050.00 USD | 2,170.00 USD | 0.00 USD | `+31.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 241,750.00 USD | 1,700.00 USD | 0.00 USD | `+33.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 242,020.00 USD | 271.44 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 662,770.00 USD | 420,750.00 USD | 0.00 USD | `+34.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 663,950.00 USD | 1,180.00 USD | 0.00 USD | `+36.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 672,850.00 USD | 8,890.00 USD | 0.00 USD | `+38.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 687,710.00 USD | 14,860.00 USD | 0.00 USD | `+38.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 689,050.00 USD | 1,340.00 USD | 0.00 USD | `+39.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 691,760.00 USD | 2,710.00 USD | 0.00 USD | `+40.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 705,630.00 USD | 13,870.00 USD | 0.00 USD | `+41.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 710,840.00 USD | 5,220.00 USD | 0.00 USD | `+42.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 712,020.00 USD | 1,170.00 USD | 0.00 USD | `+43.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 716,170.00 USD | 4,150.00 USD | 0.00 USD | `+44.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 717,110.00 USD | 944.99 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 717,310.00 USD | 198.73 USD | 0.00 USD | `+46.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 718,690.00 USD | 1,370.00 USD | 0.00 USD | `+47.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 719,760.00 USD | 1,080.00 USD | 0.00 USD | `+48.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 734,750.00 USD | 14,980.00 USD | 0.00 USD | `+50.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 735,980.00 USD | 1,230.00 USD | 0.00 USD | `+50.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 737,430.00 USD | 1,440.00 USD | 0.00 USD | `+53.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 737,780.00 USD | 355.21 USD | 0.00 USD | `+54.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 744,430.00 USD | 6,650.00 USD | 0.00 USD | `+55.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 763,410.00 USD | 18,980.00 USD | 0.00 USD | `+58.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 767,560.00 USD | 4,150.00 USD | 0.00 USD | `+59.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 770,810.00 USD | 3,250.00 USD | 0.00 USD | `+62.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 771,300.00 USD | 493.89 USD | 0.00 USD | `+67.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 771,480.00 USD | 181.30 USD | 0.00 USD | `+68.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 772,870.00 USD | 1,380.00 USD | 0.00 USD | `+70.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 785,150.00 USD | 12,290.00 USD | 0.00 USD | `+72.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 785,270.00 USD | 111.06 USD | 0.00 USD | `+72.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 785,490.00 USD | 220.61 USD | 0.00 USD | `+76.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 788,820.00 USD | 3,340.00 USD | 0.00 USD | `+80.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 789,010.00 USD | 188.75 USD | 0.00 USD | `+95.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 789,920.00 USD | 909.54 USD | 0.00 USD | `+95.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 790,040.00 USD | 121.76 USD | 0.00 USD | `+96.85%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1730` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 80,220.00 USD | 20,820.00 USD | 109,210.00 USD |
| `1D` | `0.1740` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 14,680.00 USD | 10,530.00 USD | 4,890.00 USD |
| `1D` | `0.1750` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 33,680.00 USD | 4,880.00 USD | 7,240.00 USD |
| `1D` | `0.1760` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD |
| `1D` | `0.1770` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 221,260.00 USD | 38,980.00 USD | 111,280.00 USD |
| `1D` | `0.1780` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 108,330.00 USD | 25,390.00 USD | 92,140.00 USD |
| `1D` | `0.1790` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 150,750.00 USD | 56,560.00 USD | 109,390.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 758,290.00 USD | 102,260.00 USD | 195,040.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 150,090.00 USD | 58,550.00 USD | 169,600.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 430,200.00 USD | 95,460.00 USD | 318,680.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 432,250.00 USD | 43,660.00 USD | 65,230.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 326,870.00 USD | 61,300.00 USD | 125,350.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 19,720.00 USD | 25,410.00 USD | 92,700.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 134,830.00 USD | 13,940.00 USD | 394,170.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 51,230.00 USD | 32,210.00 USD | 473,170.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 176,700.00 USD | 134,410.00 USD | 75,830.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 199,620.00 USD | 9,630.00 USD | 46,570.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 17,850.00 USD | 66,810.00 USD | 226,120.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 829,570.00 USD | 0.00 USD | 829,570.00 USD | 620,270.00 USD | 50,700.00 USD | 23,970.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `1D` | `0.1920` | 134,620.00 USD | 0.00 USD | 134,620.00 USD | 0.00 USD | 0.00 USD | 134,620.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 559,090.00 USD | 559,090.00 USD | 0.00 USD | 386,280.00 USD | 2,420.00 USD | 170,380.00 USD |
| `1D` | `0.1930` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 386,280.00 USD | 2,420.00 USD | 170,380.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 608,960.00 USD | 74,250.00 USD | 356,250.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 198,740.00 USD | 73,330.00 USD | 414,570.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 387,530.00 USD | 204,390.00 USD | 403,220.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 27,170.00 USD | 87,190.00 USD | 243,740.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 334,230.00 USD | 49,040.00 USD | 304,900.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 183,200.00 USD | 63,150.00 USD | 291,470.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 321,810.00 USD | 50,750.00 USD | 339,750.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 124,750.00 USD | 148,270.00 USD | 303,610.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 184,800.00 USD | 44,340.00 USD | 146,480.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 109,180.00 USD | 90,080.00 USD | 231,660.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 69,130.00 USD | 119,990.00 USD | 133,090.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 84,210.00 USD | 31,180.00 USD | 52,620.00 USD |
| `1D` | `0.2060` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 308,720.00 USD | 30,930.00 USD | 94,300.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 305,180.00 USD | 129,660.00 USD | 241,990.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 363,130.00 USD | 94,950.00 USD | 42,600.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 492,560.00 USD | 155,040.00 USD | 300,210.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 468,900.00 USD | 103,900.00 USD | 210,050.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 136,950.00 USD | 33,760.00 USD | 105,240.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 128,320.00 USD | 81,120.00 USD | 130,630.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 195,470.00 USD | 48,090.00 USD | 80,750.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 130,000.00 USD | 31,520.00 USD | 26,470.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 19,320.00 USD | 5,490.00 USD | 4,870.00 USD |
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
  * Total Open Interest: `412.34M` | Total OI Tokens: `2,123,993,513.7 ADA`
  * 1h OI Change: `-0.25%` | 4h OI Change: `+2.62%` | 24h OI Change: `-6.81%`
  * Exchange Breakdown: Binance=`76.12M` | Bybit=`50.14M` | OKX=`29.08M` | Hyperliquid=`28.38M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.73K` | Last 24h: `10.54K` | Last 3d: `50.95K` | Last 7d: `82.09K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0002%` | **USDT KuCoin** | `0.0073%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0086%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `28.17%` | `71.83%` | `0.39` | 19,940,000.00 USD |
| `15M` | `Binance` | `30.73%` | `69.27%` | `0.44` | 11,260,000.00 USD |
| `15M` | `OKX` | `56.58%` | `43.42%` | `1.30` | 1,160,000.00 USD |
| `15M` | `Bybit` | `39.42%` | `60.58%` | `0.65` | 964,560.00 USD |
| `15M` | `KuCoin` | `44.47%` | `55.53%` | `0.80` | 164,520.00 USD |
| `15M` | `Gate` | `39.3%` | `60.7%` | `0.65` | 927,620.00 USD |
| `15M` | `Bitget` | `7.17%` | `92.83%` | `0.08` | 1,340,000.00 USD |
| `15M` | `BingX` | `5.26%` | `94.74%` | `0.06` | 2,870,000.00 USD |
| `15M` | `MEXC` | `9.6%` | `90.4%` | `0.11` | 174,990.00 USD |
| `15M` | `Bitunix` | `45.39%` | `54.61%` | `0.83` | 386,080.00 USD |
| `15M` | `Hyperliquid` | `29.91%` | `70.09%` | `0.43` | 230,390.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.82%` | `52.18%` | `0.92` | 187,410.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `3.03%` | `96.97%` | `0.03` | 15,820.00 USD |
| `15M` | `HTX` | `30.89%` | `69.11%` | `0.45` | 93,180.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `37.37%` | `62.63%` | `0.60` | 120,050.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `22.88%` | `77.12%` | `0.30` | 54,720.00 USD |
| `15M` | `Whale Positions` | `30.73%` | `69.27%` | `0.44` | 11,260,000.00 USD |
| `15M` | `Global Accounts` | `28.17%` | `71.83%` | `0.39` | 19,940,000.00 USD |
| `1H` | `ADA` | `41.43%` | `58.57%` | `0.71` | 63,920,000.00 USD |
| `1H` | `Binance` | `42.31%` | `57.69%` | `0.73` | 36,880,000.00 USD |
| `1H` | `OKX` | `55.13%` | `44.87%` | `1.23` | 4,080,000.00 USD |
| `1H` | `Bybit` | `61.31%` | `38.69%` | `1.58` | 5,270,000.00 USD |
| `1H` | `KuCoin` | `59.13%` | `40.87%` | `1.45` | 832,960.00 USD |
| `1H` | `Gate` | `41.63%` | `58.37%` | `0.71` | 2,930,000.00 USD |
| `1H` | `Bitget` | `19.99%` | `80.01%` | `0.25` | 2,360,000.00 USD |
| `1H` | `BingX` | `13.05%` | `86.95%` | `0.15` | 4,850,000.00 USD |
| `1H` | `MEXC` | `24.9%` | `75.1%` | `0.33` | 767,850.00 USD |
| `1H` | `Bitunix` | `48.62%` | `51.38%` | `0.95` | 1,270,000.00 USD |
| `1H` | `Hyperliquid` | `41.98%` | `58.02%` | `0.72` | 1,880,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.84%` | `54.16%` | `0.85` | 478,830.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `6.17%` | `93.83%` | `0.07` | 51,140.00 USD |
| `1H` | `HTX` | `11.64%` | `88.36%` | `0.13` | 1,190,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `54.7%` | `45.3%` | `1.21` | 796,110.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `65.25%` | `34.75%` | `1.88` | 290,650.00 USD |
| `1H` | `Whale Positions` | `42.31%` | `57.69%` | `0.73` | 36,880,000.00 USD |
| `1H` | `Global Accounts` | `41.43%` | `58.57%` | `0.71` | 63,920,000.00 USD |
| `4H` | `ADA` | `49.57%` | `50.43%` | `0.98` | 206,600,000.00 USD |
| `4H` | `Binance` | `51.58%` | `48.42%` | `1.07` | 83,640,000.00 USD |
| `4H` | `OKX` | `47.43%` | `52.57%` | `0.90` | 43,220,000.00 USD |
| `4H` | `Bybit` | `52.75%` | `47.25%` | `1.12` | 16,130,000.00 USD |
| `4H` | `KuCoin` | `54.15%` | `45.85%` | `1.18` | 1,360,000.00 USD |
| `4H` | `Gate` | `54.29%` | `45.71%` | `1.19` | 29,460,000.00 USD |
| `4H` | `Bitget` | `43.89%` | `56.11%` | `0.78` | 4,070,000.00 USD |
| `4H` | `BingX` | `47.56%` | `52.44%` | `0.91` | 3,050,000.00 USD |
| `4H` | `MEXC` | `47.24%` | `52.76%` | `0.90` | 8,660,000.00 USD |
| `4H` | `Bitunix` | `40.38%` | `59.62%` | `0.68` | 6,840,000.00 USD |
| `4H` | `Hyperliquid` | `61.38%` | `38.62%` | `1.59` | 2,560,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.54%` | `49.46%` | `1.02` | 1,050,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 241,710.00 USD |
| `4H` | `WhiteBIT` | `11.36%` | `88.64%` | `0.13` | 1,910,000.00 USD |
| `4H` | `HTX` | `45%` | `55%` | `0.82` | 2,880,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.89%` | `64.11%` | `0.56` | 159,530.00 USD |
| `4H` | `Aster` | `12.59%` | `87.41%` | `0.14` | 1,300,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.23%` | `75.77%` | `0.32` | 74,180.00 USD |
| `4H` | `Whale Positions` | `51.58%` | `48.42%` | `1.07` | 83,640,000.00 USD |
| `4H` | `Global Accounts` | `49.57%` | `50.43%` | `0.98` | 206,600,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1923` | `0.1922` | `0.1923` | `0.1925` | `0.1918` | 1,542,150.19 USD | 773,488.73 USD | 768,661.46 USD | 4,827.26 USD | `+0.31%` | `0B / 0S` |
| `0:00 UTC` | `0.1915` | `0.1918` | `0.1915` | `0.1925` | `0.1913` | 1,592,969.86 USD | 824,734.22 USD | 768,235.64 USD | 56,498.59 USD | `+3.55%` | `2B / 0S` |
| `5:00 UTC` | `0.1925` | `0.1925` | `0.1925` | `0.1928` | `0.1920` | 1,263,727.12 USD | 669,438.04 USD | 594,289.08 USD | 75,148.96 USD | `+5.95%` | `1B / 1S` |
| `0:00 UTC` | `0.1928` | `0.1928` | `0.1928` | `0.1931` | `0.1925` | 1,020,820.14 USD | 499,851.61 USD | 520,968.53 USD | -21,116.92 USD | `-2.07%` | `0B / 0S` |
| `5:00 UTC` | `0.1933` | `0.1931` | `0.1933` | `0.1935` | `0.1926` | 1,721,321.63 USD | 757,830.55 USD | 963,491.09 USD | -205,660.54 USD | `-11.95%` | `0B / 1S` |
| `0:00 UTC` | `0.1946` | `0.1943` | `0.1946` | `0.1950` | `0.1931` | 2,004,577.31 USD | 1,037,190.50 USD | 967,386.81 USD | 69,803.69 USD | `+3.48%` | `6B / 1S` |
| `5:00 UTC` | `0.1943` | `0.1944` | `0.1943` | `0.1948` | `0.1941` | 786,211.02 USD | 463,861.95 USD | 322,349.07 USD | 141,512.88 USD | `+18.00%` | `0B / 0S` |
| `0:00 UTC` | `0.1945` | `0.1945` | `0.1945` | `0.1948` | `0.1941` | 981,634.02 USD | 452,264.75 USD | 529,369.27 USD | -77,104.52 USD | `-7.85%` | `0B / 1S` |
| `5:00 UTC` | `0.1935` | `0.1937` | `0.1935` | `0.1948` | `0.1931` | 1,469,717.37 USD | 597,212.27 USD | 872,505.10 USD | -275,292.83 USD | `-18.73%` | `0B / 7S` |
| `0:00 UTC` | `0.1933` | `0.1934` | `0.1933` | `0.1935` | `0.1933` | 12,109.64 USD | 11,814.00 USD | 295.64 USD | 11,518.35 USD | `+95.12%` | `2B / 0S` |

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
| `5m` | -12,620.00 USD | 92,580.00 USD | **`ACCUMULATION`** |
| `15m` | -157,170.00 USD | -586,430.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,300.00 USD | -963,240.00 USD | **`DISTRIBUTION`** |
| `1h` | 110,030.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 124,330.00 USD | -188,410.00 USD | **`DISTRIBUTION`** |
| `4h` | 329,580.00 USD | 471,950.00 USD | **`ACCUMULATION`** |
| `6h` | -1,590,000.00 USD | -2,670,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -3,800,000.00 USD | -4,680,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,750,000.00 USD | -11,650,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,300,000.00 USD | -7,400,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,800,000.00 USD | -43,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,550,000.00 USD | -197,420,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.62K` | 15m=`-157.17K` | 1h=`+110.03K` | 24h=`-8.30M`
* Futures Capital Netflows: 5m=`+92.58K` | 15m=`-586.43K` | 1h=`-1.36M` | 24h=`-7.40M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1858` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1807` (Risk Distance: `0.0051` pts)
  * +2.5R Take Profit: `0.1986`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1925` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1976` (Risk Distance: `0.0051` pts)
  * +2.5R Take Profit: `0.1797`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1945`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
