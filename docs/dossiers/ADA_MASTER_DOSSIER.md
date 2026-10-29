# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:33:41 IST` (`2026-10-29 21:03:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1908` | **Live Ask Quote**: `0.1930` | **Mid Price**: `0.1919`
- **Spread Points**: `22.00` | **Spread BPS**: `114.64 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1994` | VWAP Z-Score: `-2.94` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0020` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `16.65` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2093` | Lower -3.00σ Band: `0.1894`
  * Upper +2.51σ Band: `0.2077` | Lower -2.51σ Band: `0.1910`
  * Upper +2.01σ Band: `0.2060` | Lower -2.01σ Band: `0.1927`
  * Upper +2.00σ Band: `0.2060` | Lower -2.00σ Band: `0.1927`
  * Upper +1.28σ Band: `0.2036` | Lower -1.28σ Band: `0.1951`
  * Upper +1.00σ Band: `0.2027` | Lower -1.00σ Band: `0.1960`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1981` | EMA-20=`0.2000` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2005` (Slope: `+0.0000`) | EMA-100=`0.2008`
  * Institutional Anchors: EMA-144=`0.2011` | EMA-200=`0.2016` (Slope: `-0.1186`) | EMA-233=`0.2019`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1895` | Weekly High=`0.2086` | Weekly Low=`0.1895`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2037` (Distance: `-5.70%`)
  * Point of Control (POC) = `0.2010` (Distance: `-4.44%`)
  * Value Area Low (VAL) = `0.1953` (Distance: `-1.67%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2067` | POC=`0.2054` | VAL=`0.2018`
  * Prior Day Extremes: PDH=`0.2086` | PDL=`0.1994` | PDC=`0.2054`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2054` | Weekly POC=`0.2031` | Weekly VAL=`0.2005`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.2065` | Low=`0.1944`
  * London Session (08:00-16:00 UTC): High=`0.2009` | Low=`0.1957`
  * New York Session (13:00-21:00 UTC): High=`0.2074` | Low=`0.1979`
  * Initial Balance (First Hour): IB High=`0.2000` | IB Low=`0.1977`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1911` - `0.1927`
  * Optimal Trade Entry (OTE 0.705): `0.1923`
  * Structural Invalidation Anchor (0.786): `0.1934`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1910` | `0.1918` | `0.1871` | `0.1902` | `96,782,125` | 18,358,695.77 USD | -2,953,683.00 USD | `-16.09%` | -9,097,763.06 USD | `-2.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1902` | `0.1935` | `0.1901` | `0.1920` | `29,791,006` | 5,726,707.12 USD | 403,324.54 USD | `+7.04%` | -8,694,438.52 USD | `+0.78` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1919` | `0.1922` | `0.1915` | `0.1920` | `1,931,764` | 370,714.77 USD | 50,481.16 USD | `+13.62%` | -8,643,957.36 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1995` | `0.2001` | `0.1991` | `0.1993` | `10,049,322` | 2,005,993.91 USD | -252,380.41 USD | `-12.58%` | -2,627,230.68 USD | `-0.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1994` | `0.2000` | `0.1905` | `0.1909` | `123,755,659` | 24,025,446.30 USD | -3,516,849.37 USD | `-14.64%` | -6,144,080.06 USD | `-4.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1910` | `0.1935` | `0.1871` | `0.1920` | `128,504,895` | 24,456,117.66 USD | -2,499,877.30 USD | `-10.22%` | -8,643,957.36 USD | `-2.31` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.2034` | `0.2037` | `0.2012` | `0.2024` | `32,838,114` | 6,645,891.06 USD | 314,100.73 USD | `+4.73%` | -2,314,914.17 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.2023` | `0.2028` | `0.2015` | `0.2022` | `15,668,827` | 3,167,925.53 USD | 135,664.16 USD | `+4.28%` | -2,179,250.01 USD | `+0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.2022` | `0.2023` | `0.1871` | `0.1920` | `309,845,491` | 59,970,184.79 USD | -6,464,707.35 USD | `-10.78%` | -8,643,957.36 USD | `-3.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1920` | `309,772,779` | 59,956,220.39 USD | -6,475,062.88 USD | `-10.80%` | -8,901,007.79 USD | `-1.48` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -5,414,333.03 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -4,633,383.98 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1920` | `309,772,779` | 59,956,220.39 USD | -6,475,062.88 USD | `-10.80%` | -8,901,007.79 USD | `-1.48` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1919`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `515` | `0x77ee...2902` | `SHORT` | 4,268,306.35 USD | `21,412,192.00` | `0.1911` | `0.1911` | `0.5569` | -177,054.61 USD | `-4.15%` | `10X Cross` |
| `1248` | `0x7737...bf66` | `SHORT` | 1,814,202.04 USD | `9,091,466.00` | `0.2190` | `0.1911` | `2.11` | 176,787.76 USD | `+9.74%` | `10X Cross` |
| `1252` | `0x123d...3bff` | `LONG` | 1,811,467.43 USD | `9,393,142.00` | `0.2912` | `0.1911` | `0.000000` | -924,268.50 USD | `-51.02%` | `10X Cross` |
| `1561` | `0x5f94...4b96` | `SHORT` | 1,408,899.57 USD | `7,162,318.00` | `0.2303` | `0.1911` | `0.7282` | 240,575.62 USD | `+17.08%` | `10X Cross` |
| `1752` | `0x4982...59e6` | `SHORT` | 1,195,803.18 USD | `5,998,812.00` | `0.1891` | `0.1911` | `0.3984` | -61,244.82 USD | `-5.12%` | `10X Cross` |
| `1843` | `0xcac1...26b3` | `LONG` | 1,112,903.00 USD | `5,803,927.00` | `0.2000` | `0.1911` | `0.000000` | -47,912.58 USD | `-4.31%` | `10X Cross` |
| `1984` | `0xeadc...9d55` | `LONG` | 1,002,994.29 USD | `5,038,400.00` | `0.2195` | `0.1911` | `0.000000` | -102,718.46 USD | `-10.24%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2066` | 7,440.55 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 7.44K USD at 0.2066 USD [API] | `2026-10-28 03:17:56` |
| `ANNOUNCEMENT` | `INFO` | `0.2065` | 6,153.97 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.15K USD at 0.2065 USD [API] | `2026-10-28 03:17:56` |
| `ANNOUNCEMENT` | `INFO` | `0.2069` | 11,330.81 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 11.33K USD at 0.2069 USD [API] | `2026-10-28 04:10:38` |
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
| `Live` | `Long Liquidation` | `0.0385` | 763.99 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 560.71 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,510.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 1,010.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 835.91 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 135,840.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 784.19 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 3,010.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 426.98 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 13,080.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 331.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 830.31 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 890.98 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 1,290.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 2,550.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 931.42 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 3,030.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,160.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,140.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 431.96 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 3,730.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 710.03 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 2,120.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 1,270.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,740.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 146.92 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 13,970.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,500.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 5,720.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 3,630.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 163.65 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 138.14 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 608.32 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 36,900.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 516,140.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 47,940.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 10,980.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 1,580.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 2,250.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 59,470.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 6,010.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,630.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 2,670.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,540.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 2,030.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,980.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 34,360.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 1,920.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 26,580.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1700` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 621,230.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 2,900,000.00 USD | 2,900,000.00 USD | 23,820.00 USD | 353.70 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 896,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 321.20 USD | 1,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 2,720.00 USD | 644,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 4,280.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,830.00 USD | 641,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 639,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,720.00 USD | 638,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 2,840,000.00 USD | 2,840,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,750.00 USD | 633,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 2,750,000.00 USD | 2,750,000.00 USD | 53,230.00 USD | 16,740.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,750.00 USD | 628,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 2,600,000.00 USD | 2,600,000.00 USD | 62,120.00 USD | 34,290.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 20,740.00 USD | 612,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 2,440,000.00 USD | 2,440,000.00 USD | 73,150.00 USD | 37,010.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 11,150.00 USD | 592,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 2,280,000.00 USD | 2,280,000.00 USD | 72,000.00 USD | 24,650.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 136,240.00 USD | 581,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 2,140,000.00 USD | 2,140,000.00 USD | 38,430.00 USD | 21,250.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 444,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 2,040,000.00 USD | 2,040,000.00 USD | 136,500.00 USD | 8,980.00 USD | 41,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,430.00 USD | 437,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 1,850,000.00 USD | 1,850,000.00 USD | 27,490.00 USD | 20,190.00 USD | 23,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 367.00 USD | 418,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 1,780,000.00 USD | 1,780,000.00 USD | 77,630.00 USD | 29,420.00 USD | 52,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 956.45 USD | 418,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 1,620,000.00 USD | 1,620,000.00 USD | 128,210.00 USD | 60,170.00 USD | 124,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 4,100.00 USD | 417,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 1,300,000.00 USD | 1,300,000.00 USD | 159,010.00 USD | 7,290.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 5,180.00 USD | 413,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 1,120,000.00 USD | 1,120,000.00 USD | 102,920.00 USD | 49,970.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 4,120.00 USD | 408,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 929,740.00 USD | 929,740.00 USD | 223,120.00 USD | 49,550.00 USD | 60,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1885` | 108.95 USD | 404,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1890` | 596,610.00 USD | 596,610.00 USD | 162,010.00 USD | 110,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 6,260.00 USD | 403,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 324,460.00 USD | 324,460.00 USD | 0.00 USD | 114,440.00 USD | 210,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1905` | 17,750.00 USD | 397,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1910` | 292,920.00 USD | 292,920.00 USD | 292,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1910` | 585,840.00 USD | 585,840.00 USD | 292,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1915` | 32,410.00 USD | 379,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1920` | 1,060,000.00 USD | 1,060,000.00 USD | 470,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1925` | 50,320.00 USD | 347,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1930` | 1,460,000.00 USD | 1,460,000.00 USD | 375,010.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1935` | 290,650.00 USD | 297,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1940` | 1,620,000.00 USD | 1,620,000.00 USD | 139,920.00 USD | 0.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1945` | 4,640.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1950` | 1,680,000.00 USD | 1,680,000.00 USD | 21,890.00 USD | 20,360.00 USD | 17,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1955` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,930,000.00 USD | 1,930,000.00 USD | 6,090.00 USD | 178,720.00 USD | 67,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 30,910.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 2,050,000.00 USD | 2,050,000.00 USD | 62,420.00 USD | 1,260.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1990` | 2,170,000.00 USD | 2,170,000.00 USD | 50,670.00 USD | 37,620.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2000` | 2,580,000.00 USD | 2,580,000.00 USD | 188,460.00 USD | 11,400.00 USD | 204,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2010` | 3,030,000.00 USD | 3,030,000.00 USD | 101,890.00 USD | 121,910.00 USD | 225,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 3,170,000.00 USD | 3,170,000.00 USD | 32,560.00 USD | 26,640.00 USD | 89,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2030` | 3,660,000.00 USD | 3,660,000.00 USD | 67,350.00 USD | 81,120.00 USD | 338,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 4,030,000.00 USD | 4,030,000.00 USD | 35,540.00 USD | 211,200.00 USD | 124,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 4,150,000.00 USD | 4,150,000.00 USD | 55,220.00 USD | 24,610.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 4,510,000.00 USD | 4,510,000.00 USD | 238,370.00 USD | 30,390.00 USD | 94,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 5,320,000.00 USD | 5,320,000.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 6,020,000.00 USD | 6,020,000.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 6,980,000.00 USD | 6,980,000.00 USD | 505,530.00 USD | 177,310.00 USD | 279,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 8,410,000.00 USD | 8,410,000.00 USD | 753,960.00 USD | 203,010.00 USD | 476,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 8,850,000.00 USD | 8,850,000.00 USD | 209,440.00 USD | 62,330.00 USD | 162,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 9,280,000.00 USD | 9,280,000.00 USD | 193,160.00 USD | 96,300.00 USD | 138,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 3,570.00 USD | 3,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,620,000.00 USD | 9,620,000.00 USD | 192,160.00 USD | 58,850.00 USD | 90,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2135` | 715.44 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2140` | 10,130,000.00 USD | 10,130,000.00 USD | 245,390.00 USD | 82,990.00 USD | 180,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 10,260,000.00 USD | 10,260,000.00 USD | 68,510.00 USD | 18,760.00 USD | 46,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 3,970.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2160` | 10,440,000.00 USD | 10,440,000.00 USD | 99,140.00 USD | 34,110.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 10,600,000.00 USD | 10,600,000.00 USD | 61,590.00 USD | 17,680.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2180` | 10,780,000.00 USD | 10,780,000.00 USD | 78,970.00 USD | 36,240.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 18,910.00 USD | 27,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2190` | 10,950,000.00 USD | 10,950,000.00 USD | 85,280.00 USD | 39,700.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2195` | 252.21 USD | 27,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2200` | 11,100,000.00 USD | 11,100,000.00 USD | 83,270.00 USD | 24,920.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 11,190,000.00 USD | 11,190,000.00 USD | 36,960.00 USD | 20,190.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 11,310,000.00 USD | 11,310,000.00 USD | 73,390.00 USD | 8,880.00 USD | 36,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 11,360,000.00 USD | 11,360,000.00 USD | 22,600.00 USD | 8,440.00 USD | 19,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 29,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2240` | 11,430,000.00 USD | 11,430,000.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 31,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 40,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2315` | 113.90 USD | 40,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 41,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 48,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2395` | 511.57 USD | 49,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 50,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 743.58 USD | 51,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,370.00 USD | 79,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2535` | 611.70 USD | 80,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 80,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 1,400.00 USD | 82,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 298.11 USD | 82,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 82,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2815` | 451.53 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 85,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2885` | 464.77 USD | 85,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 86,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 89,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 90,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 98,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 98,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 98,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 206.95 USD | 98,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 96,880.00 USD | 195,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 114.32 USD | 195,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3145` | 159.45 USD | 196,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 299.73 USD | 196,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 198,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3315` | 83,520.00 USD | 282,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3355` | 4,530.00 USD | 286,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 240.93 USD | 287,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 753.16 USD | 287,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3405` | 5,350.00 USD | 293,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3415` | 2,570.00 USD | 295,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3435` | 314.30 USD | 296,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 2,370.00 USD | 298,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3655` | 146.57 USD | 298,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3665` | 27,110.00 USD | 325,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 334,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 337,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 987.96 USD | 338,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 788.87 USD | 339,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3925` | 26,120.00 USD | 365,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3935` | 2,360,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3945` | 986.25 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3985` | 287,220.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3995` | 534.53 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 6,790.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4045` | 505.63 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 2,550,000.00 USD | 0.00 USD | 763.99 USD | `-80.96%` | `19,844.00` |
| `Live` | `Long` | `0.0485` | 2,550,000.00 USD | 0.00 USD | 560.71 USD | `-76.01%` | `11,561.00` |
| `Live` | `Long` | `0.0525` | 2,550,000.00 USD | 0.00 USD | 5,510.00 USD | `-74.04%` | `105,008.00` |
| `Live` | `Long` | `0.0645` | 2,540,000.00 USD | 0.00 USD | 1,010.00 USD | `-68.10%` | `15,628.00` |
| `Live` | `Long` | `0.0655` | 2,540,000.00 USD | 0.00 USD | 835.91 USD | `-67.61%` | `12,762.00` |
| `Live` | `Long` | `0.0725` | 2,540,000.00 USD | 0.00 USD | 135,840.00 USD | `-64.14%` | `1,873,703.00` |
| `Live` | `Long` | `0.0745` | 2,410,000.00 USD | 0.00 USD | 784.19 USD | `-63.16%` | `10,526.00` |
| `Live` | `Long` | `0.0765` | 2,410,000.00 USD | 0.00 USD | 3,010.00 USD | `-62.17%` | `39,410.00` |
| `Live` | `Long` | `0.0815` | 2,400,000.00 USD | 0.00 USD | 426.98 USD | `-59.69%` | `5,239.00` |
| `Live` | `Long` | `0.0865` | 2,400,000.00 USD | 0.00 USD | 13,080.00 USD | `-57.22%` | `151,185.00` |
| `Live` | `Long` | `0.0875` | 2,390,000.00 USD | 0.00 USD | 344.75 USD | `-56.73%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,390,000.00 USD | 0.00 USD | 1,150.00 USD | `-56.23%` | `13,050.00` |
| `Live` | `Long` | `0.0925` | 2,390,000.00 USD | 0.00 USD | 165.11 USD | `-54.25%` | `1,785.00` |
| `Live` | `Long` | `0.0955` | 2,390,000.00 USD | 0.00 USD | 331.00 USD | `-52.77%` | `3,466.00` |
| `Live` | `Long` | `0.0975` | 2,390,000.00 USD | 0.00 USD | 830.31 USD | `-51.78%` | `8,516.00` |
| `Live` | `Long` | `0.1025` | 2,390,000.00 USD | 0.00 USD | 4,100.00 USD | `-49.31%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,380,000.00 USD | 0.00 USD | 1,050.00 USD | `-48.81%` | `10,149.00` |
| `Live` | `Long` | `0.1065` | 2,380,000.00 USD | 0.00 USD | 890.98 USD | `-47.33%` | `8,366.00` |
| `Live` | `Long` | `0.1085` | 2,380,000.00 USD | 0.00 USD | 1,290.00 USD | `-46.34%` | `11,850.00` |
| `Live` | `Long` | `0.1095` | 2,380,000.00 USD | 0.00 USD | 2,550.00 USD | `-45.85%` | `23,247.00` |
| `Live` | `Long` | `0.1145` | 2,380,000.00 USD | 0.00 USD | 862.64 USD | `-43.37%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,370,000.00 USD | 0.00 USD | 13,360.00 USD | `-42.38%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,360,000.00 USD | 0.00 USD | 931.42 USD | `-41.89%` | `7,927.00` |
| `Live` | `Long` | `0.1205` | 2,360,000.00 USD | 0.00 USD | 826.27 USD | `-40.41%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,360,000.00 USD | 0.00 USD | 1,050.00 USD | `-39.91%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,360,000.00 USD | 0.00 USD | 3,030.00 USD | `-38.92%` | `24,507.00` |
| `Live` | `Long` | `0.1245` | 2,360,000.00 USD | 0.00 USD | 1,160.00 USD | `-38.43%` | `9,343.00` |
| `Live` | `Long` | `0.1255` | 2,350,000.00 USD | 0.00 USD | 2,140.00 USD | `-37.93%` | `17,030.00` |
| `Live` | `Long` | `0.1265` | 2,350,000.00 USD | 0.00 USD | 314.61 USD | `-37.44%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,350,000.00 USD | 0.00 USD | 1,260.00 USD | `-36.94%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,350,000.00 USD | 0.00 USD | 2,540.00 USD | `-35.95%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,350,000.00 USD | 0.00 USD | 431.96 USD | `-35.46%` | `3,310.00` |
| `Live` | `Long` | `0.1315` | 2,350,000.00 USD | 0.00 USD | 3,730.00 USD | `-34.97%` | `28,344.00` |
| `Live` | `Long` | `0.1325` | 2,340,000.00 USD | 0.00 USD | 6,960.00 USD | `-34.47%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,340,000.00 USD | 0.00 USD | 3,600.00 USD | `-33.98%` | `26,965.00` |
| `Live` | `Long` | `0.1345` | 2,330,000.00 USD | 0.00 USD | 710.03 USD | `-33.48%` | `5,279.00` |
| `Live` | `Long` | `0.1355` | 2,330,000.00 USD | 0.00 USD | 106.64 USD | `-32.99%` | `787.00` |
| `Live` | `Long` | `0.1395` | 2,330,000.00 USD | 0.00 USD | 2,120.00 USD | `-31.01%` | `15,162.00` |
| `Live` | `Long` | `0.1405` | 2,330,000.00 USD | 0.00 USD | 1,270.00 USD | `-30.51%` | `9,025.00` |
| `Live` | `Long` | `0.1415` | 2,330,000.00 USD | 0.00 USD | 9,740.00 USD | `-30.02%` | `68,863.00` |
| `Live` | `Long` | `0.1425` | 2,320,000.00 USD | 0.00 USD | 146.92 USD | `-29.53%` | `1,031.00` |
| `Live` | `Long` | `0.1435` | 2,320,000.00 USD | 0.00 USD | 13,970.00 USD | `-29.03%` | `97,369.00` |
| `Live` | `Long` | `0.1445` | 2,310,000.00 USD | 0.00 USD | 2,500.00 USD | `-28.54%` | `17,302.00` |
| `Live` | `Long` | `0.1455` | 2,300,000.00 USD | 0.00 USD | 5,720.00 USD | `-28.04%` | `39,318.00` |
| `Live` | `Long` | `0.1465` | 2,300,000.00 USD | 0.00 USD | 4,580.00 USD | `-27.55%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,290,000.00 USD | 0.00 USD | 3,630.00 USD | `-27.05%` | `24,600.00` |
| `Live` | `Long` | `0.1485` | 2,290,000.00 USD | 0.00 USD | 163.65 USD | `-26.56%` | `1,102.00` |
| `Live` | `Long` | `0.1495` | 2,290,000.00 USD | 0.00 USD | 138.14 USD | `-26.06%` | `924.00` |
| `Live` | `Long` | `0.1505` | 2,290,000.00 USD | 0.00 USD | 608.32 USD | `-25.57%` | `4,042.00` |
| `Live` | `Long` | `0.1515` | 2,290,000.00 USD | 0.00 USD | 36,900.00 USD | `-25.07%` | `243,553.00` |
| `Live` | `Long` | `0.1525` | 2,250,000.00 USD | 0.00 USD | 516,140.00 USD | `-24.58%` | `3,384,521.00` |
| `Live` | `Long` | `0.1535` | 1,740,000.00 USD | 0.00 USD | 47,940.00 USD | `-24.09%` | `312,296.00` |
| `Live` | `Long` | `0.1545` | 1,690,000.00 USD | 0.00 USD | 721.05 USD | `-23.59%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,690,000.00 USD | 0.00 USD | 10,980.00 USD | `-23.10%` | `70,625.00` |
| `Live` | `Long` | `0.1565` | 1,680,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.60%` | `10,116.00` |
| `Live` | `Long` | `0.1585` | 1,670,000.00 USD | 0.00 USD | 6,000.00 USD | `-21.61%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,670,000.00 USD | 0.00 USD | 2,250.00 USD | `-21.12%` | `14,121.00` |
| `Live` | `Long` | `0.1605` | 1,670,000.00 USD | 0.00 USD | 59,470.00 USD | `-20.62%` | `370,528.00` |
| `Live` | `Long` | `0.1615` | 1,610,000.00 USD | 0.00 USD | 6,010.00 USD | `-20.13%` | `37,185.00` |
| `Live` | `Long` | `0.1625` | 1,600,000.00 USD | 0.00 USD | 2,630.00 USD | `-19.63%` | `16,160.00` |
| `Live` | `Long` | `0.1635` | 1,600,000.00 USD | 0.00 USD | 2,670.00 USD | `-19.14%` | `16,314.00` |
| `Live` | `Long` | `0.1645` | 1,590,000.00 USD | 0.00 USD | 10,540.00 USD | `-18.64%` | `64,095.00` |
| `Live` | `Long` | `0.1655` | 1,580,000.00 USD | 0.00 USD | 2,030.00 USD | `-18.15%` | `12,259.00` |
| `Live` | `Long` | `0.1665` | 1,580,000.00 USD | 0.00 USD | 1,980.00 USD | `-17.66%` | `11,889.00` |
| `Live` | `Long` | `0.1675` | 1,580,000.00 USD | 0.00 USD | 34,360.00 USD | `-17.16%` | `205,159.00` |
| `Live` | `Long` | `0.1685` | 1,550,000.00 USD | 0.00 USD | 1,920.00 USD | `-16.67%` | `11,375.00` |
| `Live` | `Long` | `0.1695` | 1,540,000.00 USD | 0.00 USD | 26,580.00 USD | `-16.17%` | `156,825.00` |
| `Live` | `Long` | `0.1705` | 1,520,000.00 USD | 0.00 USD | 621,230.00 USD | `-15.68%` | `3,643,607.00` |
| `Live` | `Long` | `0.1715` | 896,310.00 USD | 0.00 USD | 252,270.00 USD | `-15.18%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 644,040.00 USD | 0.00 USD | 2,720.00 USD | `-14.69%` | `15,753.00` |
| `Live` | `Long` | `0.1735` | 641,320.00 USD | 0.00 USD | 1,830.00 USD | `-14.19%` | `10,522.00` |
| `Live` | `Long` | `0.1745` | 639,490.00 USD | 0.00 USD | 1,320.00 USD | `-13.70%` | `7,554.00` |
| `Live` | `Long` | `0.1755` | 638,170.00 USD | 0.00 USD | 4,720.00 USD | `-13.20%` | `26,871.00` |
| `Live` | `Long` | `0.1765` | 633,460.00 USD | 0.00 USD | 4,750.00 USD | `-12.71%` | `26,931.00` |
| `Live` | `Long` | `0.1775` | 628,710.00 USD | 0.00 USD | 15,750.00 USD | `-12.22%` | `88,754.00` |
| `Live` | `Long` | `0.1785` | 612,950.00 USD | 0.00 USD | 20,740.00 USD | `-11.72%` | `116,210.00` |
| `Live` | `Long` | `0.1795` | 592,210.00 USD | 0.00 USD | 11,150.00 USD | `-11.23%` | `62,104.00` |
| `Live` | `Long` | `0.1805` | 581,060.00 USD | 0.00 USD | 136,240.00 USD | `-10.73%` | `754,779.00` |
| `Live` | `Long` | `0.1815` | 444,820.00 USD | 0.00 USD | 7,670.00 USD | `-10.24%` | `42,240.00` |
| `Live` | `Long` | `0.1825` | 437,160.00 USD | 0.00 USD | 18,430.00 USD | `-9.74%` | `100,978.00` |
| `Live` | `Long` | `0.1835` | 418,730.00 USD | 0.00 USD | 367.00 USD | `-9.25%` | `2,000.00` |
| `Live` | `Long` | `0.1845` | 418,360.00 USD | 0.00 USD | 956.45 USD | `-8.75%` | `5,184.00` |
| `Live` | `Long` | `0.1855` | 417,400.00 USD | 0.00 USD | 4,100.00 USD | `-8.26%` | `22,111.00` |
| `Live` | `Long` | `0.1865` | 413,300.00 USD | 0.00 USD | 5,180.00 USD | `-7.76%` | `27,798.00` |
| `Live` | `Long` | `0.1875` | 408,120.00 USD | 0.00 USD | 4,120.00 USD | `-7.27%` | `21,979.00` |
| `Live` | `Long` | `0.1885` | 404,000.00 USD | 0.00 USD | 108.95 USD | `-6.78%` | `578.00` |
| `Live` | `Long` | `0.1895` | 403,890.00 USD | 0.00 USD | 6,260.00 USD | `-6.28%` | `33,010.00` |
| `Live` | `Long` | `0.1905` | 397,630.00 USD | 0.00 USD | 17,750.00 USD | `-5.79%` | `93,172.00` |
| `Live` | `Long` | `0.1915` | 379,880.00 USD | 0.00 USD | 32,410.00 USD | `-5.29%` | `169,227.00` |
| `Live` | `Long` | `0.1925` | 347,480.00 USD | 0.00 USD | 50,320.00 USD | `-4.80%` | `261,413.00` |
| `Live` | `Long` | `0.1935` | 297,150.00 USD | 0.00 USD | 290,650.00 USD | `-4.30%` | `1,502,046.00` |
| `Live` | `Long` | `0.1945` | 6,510.00 USD | 0.00 USD | 4,640.00 USD | `-3.81%` | `23,844.00` |
| `Live` | `Long` | `0.1955` | 1,870.00 USD | 0.00 USD | 1,870.00 USD | `-3.31%` | `9,570.00` |
| `Live` | `Short` | `0.2125` | 3,570.00 USD | 3,570.00 USD | 0.00 USD | `+5.09%` | `16,787.00` |
| `Live` | `Short` | `0.2135` | 4,280.00 USD | 715.44 USD | 0.00 USD | `+5.59%` | `3,351.00` |
| `Live` | `Short` | `0.2155` | 8,260.00 USD | 3,970.00 USD | 0.00 USD | `+6.58%` | `18,440.00` |
| `Live` | `Short` | `0.2185` | 27,160.00 USD | 18,910.00 USD | 0.00 USD | `+8.06%` | `86,525.00` |
| `Live` | `Short` | `0.2195` | 27,410.00 USD | 252.21 USD | 0.00 USD | `+8.56%` | `1,149.00` |
| `Live` | `Short` | `0.2215` | 29,060.00 USD | 1,640.00 USD | 0.00 USD | `+9.55%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 29,260.00 USD | 200.48 USD | 0.00 USD | `+10.53%` | `897.00` |
| `Live` | `Short` | `0.2275` | 31,420.00 USD | 2,160.00 USD | 0.00 USD | `+12.51%` | `9,500.00` |
| `Live` | `Short` | `0.2285` | 40,660.00 USD | 9,240.00 USD | 0.00 USD | `+13.01%` | `40,428.00` |
| `Live` | `Short` | `0.2315` | 40,770.00 USD | 113.90 USD | 0.00 USD | `+14.49%` | `492.00` |
| `Live` | `Short` | `0.2325` | 41,050.00 USD | 282.02 USD | 0.00 USD | `+14.99%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 48,690.00 USD | 7,640.00 USD | 0.00 USD | `+15.48%` | `32,708.00` |
| `Live` | `Short` | `0.2395` | 49,200.00 USD | 511.57 USD | 0.00 USD | `+18.45%` | `2,136.00` |
| `Live` | `Short` | `0.2405` | 50,670.00 USD | 1,470.00 USD | 0.00 USD | `+18.94%` | `6,110.00` |
| `Live` | `Short` | `0.2415` | 51,420.00 USD | 743.58 USD | 0.00 USD | `+19.44%` | `3,079.00` |
| `Live` | `Short` | `0.2525` | 79,790.00 USD | 28,370.00 USD | 0.00 USD | `+24.88%` | `112,352.00` |
| `Live` | `Short` | `0.2535` | 80,400.00 USD | 611.70 USD | 0.00 USD | `+25.37%` | `2,413.00` |
| `Live` | `Short` | `0.2585` | 80,780.00 USD | 380.25 USD | 0.00 USD | `+27.84%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 82,180.00 USD | 1,400.00 USD | 0.00 USD | `+29.33%` | `5,346.00` |
| `Live` | `Short` | `0.2715` | 82,470.00 USD | 298.11 USD | 0.00 USD | `+34.27%` | `1,098.00` |
| `Live` | `Short` | `0.2775` | 82,850.00 USD | 379.62 USD | 0.00 USD | `+37.24%` | `1,368.00` |
| `Live` | `Short` | `0.2815` | 83,300.00 USD | 451.53 USD | 0.00 USD | `+39.22%` | `1,604.00` |
| `Live` | `Short` | `0.2845` | 85,480.00 USD | 2,170.00 USD | 0.00 USD | `+40.70%` | `7,640.00` |
| `Live` | `Short` | `0.2885` | 85,940.00 USD | 464.77 USD | 0.00 USD | `+42.68%` | `1,611.00` |
| `Live` | `Short` | `0.2895` | 86,350.00 USD | 411.09 USD | 0.00 USD | `+43.18%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 89,620.00 USD | 3,260.00 USD | 0.00 USD | `+44.16%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 90,140.00 USD | 519.79 USD | 0.00 USD | `+45.15%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 98,120.00 USD | 7,990.00 USD | 0.00 USD | `+46.14%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 98,270.00 USD | 146.34 USD | 0.00 USD | `+48.62%` | `487.00` |
| `Live` | `Short` | `0.3055` | 98,680.00 USD | 408.15 USD | 0.00 USD | `+51.09%` | `1,336.00` |
| `Live` | `Short` | `0.3075` | 98,880.00 USD | 206.95 USD | 0.00 USD | `+52.08%` | `673.00` |
| `Live` | `Short` | `0.3105` | 195,770.00 USD | 96,880.00 USD | 0.00 USD | `+53.56%` | `312,021.00` |
| `Live` | `Short` | `0.3115` | 195,880.00 USD | 114.32 USD | 0.00 USD | `+54.06%` | `367.00` |
| `Live` | `Short` | `0.3145` | 196,040.00 USD | 159.45 USD | 0.00 USD | `+55.54%` | `507.00` |
| `Live` | `Short` | `0.3155` | 196,340.00 USD | 299.73 USD | 0.00 USD | `+56.03%` | `950.00` |
| `Live` | `Short` | `0.3295` | 198,720.00 USD | 2,380.00 USD | 0.00 USD | `+62.96%` | `7,219.00` |
| `Live` | `Short` | `0.3315` | 282,240.00 USD | 83,520.00 USD | 0.00 USD | `+63.95%` | `251,952.00` |
| `Live` | `Short` | `0.3355` | 286,770.00 USD | 4,530.00 USD | 0.00 USD | `+65.92%` | `13,504.00` |
| `Live` | `Short` | `0.3365` | 287,010.00 USD | 240.93 USD | 0.00 USD | `+66.42%` | `716.00` |
| `Live` | `Short` | `0.3385` | 287,770.00 USD | 753.16 USD | 0.00 USD | `+67.41%` | `2,225.00` |
| `Live` | `Short` | `0.3405` | 293,120.00 USD | 5,350.00 USD | 0.00 USD | `+68.40%` | `15,712.00` |
| `Live` | `Short` | `0.3415` | 295,680.00 USD | 2,570.00 USD | 0.00 USD | `+68.89%` | `7,515.00` |
| `Live` | `Short` | `0.3435` | 296,000.00 USD | 314.30 USD | 0.00 USD | `+69.88%` | `915.00` |
| `Live` | `Short` | `0.3485` | 298,370.00 USD | 2,370.00 USD | 0.00 USD | `+72.35%` | `6,797.00` |
| `Live` | `Short` | `0.3655` | 298,510.00 USD | 146.57 USD | 0.00 USD | `+80.76%` | `401.00` |
| `Live` | `Short` | `0.3665` | 325,620.00 USD | 27,110.00 USD | 0.00 USD | `+81.26%` | `73,959.00` |
| `Live` | `Short` | `0.3715` | 334,790.00 USD | 9,170.00 USD | 0.00 USD | `+83.73%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 337,930.00 USD | 3,140.00 USD | 0.00 USD | `+85.21%` | `8,395.00` |
| `Live` | `Short` | `0.3885` | 338,920.00 USD | 987.96 USD | 0.00 USD | `+92.14%` | `2,543.00` |
| `Live` | `Short` | `0.3915` | 339,710.00 USD | 788.87 USD | 0.00 USD | `+93.62%` | `2,015.00` |
| `Live` | `Short` | `0.3925` | 365,830.00 USD | 26,120.00 USD | 0.00 USD | `+94.11%` | `66,555.00` |
| `Live` | `Short` | `0.3935` | 2,730,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+94.61%` | `5,999,524.00` |
| `Live` | `Short` | `0.3945` | 2,730,000.00 USD | 986.25 USD | 0.00 USD | `+95.10%` | `2,500.00` |
| `Live` | `Short` | `0.3985` | 3,010,000.00 USD | 287,220.00 USD | 0.00 USD | `+97.08%` | `720,753.00` |
| `Live` | `Short` | `0.3995` | 3,020,000.00 USD | 534.53 USD | 0.00 USD | `+97.58%` | `1,338.00` |
| `Live` | `Short` | `0.4025` | 3,020,000.00 USD | 6,790.00 USD | 0.00 USD | `+99.06%` | `16,862.00` |
| `Live` | `Short` | `0.4045` | 3,020,000.00 USD | 505.63 USD | 0.00 USD | `+100.05%` | `1,250.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 558,690,000.00 USD | 0.00 USD | 415.13 USD | `-70.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 558,690,000.00 USD | 0.00 USD | 438.99 USD | `-70.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 558,690,000.00 USD | 0.00 USD | 1,100.00 USD | `-45.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 558,690,000.00 USD | 0.00 USD | 541.33 USD | `-44.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 558,690,000.00 USD | 0.00 USD | 602,500.00 USD | `-40.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 558,090,000.00 USD | 0.00 USD | 1,320.00 USD | `-36.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 558,090,000.00 USD | 0.00 USD | 13,390.00 USD | `-35.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 558,080,000.00 USD | 0.00 USD | 728.88 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 558,070,000.00 USD | 0.00 USD | 4,350.00 USD | `-33.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 558,070,000.00 USD | 0.00 USD | 542.99 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 558,070,000.00 USD | 0.00 USD | 1,820.00 USD | `-31.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 558,070,000.00 USD | 0.00 USD | 1,050.00 USD | `-30.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 558,070,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 558,060,000.00 USD | 0.00 USD | 1,600.00 USD | `-29.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 558,060,000.00 USD | 0.00 USD | 4,580.00 USD | `-28.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 558,060,000.00 USD | 0.00 USD | 303.26 USD | `-25.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 558,060,000.00 USD | 0.00 USD | 1,290.00 USD | `-25.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 558,060,000.00 USD | 0.00 USD | 279.53 USD | `-24.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 558,060,000.00 USD | 0.00 USD | 324.30 USD | `-23.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 558,060,000.00 USD | 0.00 USD | 1,480.00 USD | `-23.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 558,050,000.00 USD | 0.00 USD | 552.21 USD | `-21.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 558,050,000.00 USD | 0.00 USD | 166.84 USD | `-21.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 558,050,000.00 USD | 0.00 USD | 2,990.00 USD | `-20.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 558,050,000.00 USD | 0.00 USD | 562.67 USD | `-20.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 558,050,000.00 USD | 0.00 USD | 24,760.00 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 558,030,000.00 USD | 0.00 USD | 6,540.00 USD | `-19.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 558,020,000.00 USD | 0.00 USD | 2,870.00 USD | `-18.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 558,020,000.00 USD | 0.00 USD | 452.97 USD | `-18.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 558,020,000.00 USD | 0.00 USD | 13,930.00 USD | `-17.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 558,000,000.00 USD | 0.00 USD | 317.92 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 558,000,000.00 USD | 0.00 USD | 6,740.00 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 557,990,000.00 USD | 0.00 USD | 4,270.00 USD | `-16.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 557,990,000.00 USD | 0.00 USD | 7,630.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 557,980,000.00 USD | 0.00 USD | 6,860.00 USD | `-15.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 557,980,000.00 USD | 0.00 USD | 6,900.00 USD | `-14.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 557,970,000.00 USD | 0.00 USD | 103.58 USD | `-14.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 557,970,000.00 USD | 0.00 USD | 8,220.00 USD | `-13.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 557,960,000.00 USD | 0.00 USD | 1,760.00 USD | `-13.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 557,960,000.00 USD | 0.00 USD | 623.57 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 557,960,000.00 USD | 0.00 USD | 4,440.00 USD | `-12.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 557,950,000.00 USD | 0.00 USD | 12,390.00 USD | `-11.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 557,940,000.00 USD | 0.00 USD | 5,760.00 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 557,940,000.00 USD | 0.00 USD | 26,470.00 USD | `-10.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 557,910,000.00 USD | 0.00 USD | 2,890.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 557,910,000.00 USD | 0.00 USD | 3,080.00 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 557,900,000.00 USD | 0.00 USD | 3,160.00 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 557,900,000.00 USD | 0.00 USD | 18,650.00 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 557,880,000.00 USD | 0.00 USD | 282.33 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 557,880,000.00 USD | 0.00 USD | 218.76 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 557,880,000.00 USD | 0.00 USD | 109.69 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 557,880,000.00 USD | 0.00 USD | 7,390.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 557,870,000.00 USD | 0.00 USD | 837.40 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 557,870,000.00 USD | 0.00 USD | 6,450.00 USD | `-5.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 557,870,000.00 USD | 0.00 USD | 2,030.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 557,860,000.00 USD | 0.00 USD | 513.01 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 557,860,000.00 USD | 0.00 USD | 2,480.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 557,860,000.00 USD | 0.00 USD | 2,620.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1955` | 557,860,000.00 USD | 0.00 USD | 125.51 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1965` | 557,860,000.00 USD | 0.00 USD | 2,380.00 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1975` | 557,860,000.00 USD | 0.00 USD | 79,010,000.00 USD | `-2.32%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1985` | 478,850,000.00 USD | 0.00 USD | 79,400,000.00 USD | `-1.83%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1995` | 399,450,000.00 USD | 0.00 USD | 319,220,000.00 USD | `-1.34%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2005` | 80,230,000.00 USD | 0.00 USD | 80,210,000.00 USD | `-0.84%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2015` | 18,790.00 USD | 0.00 USD | 18,790.00 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 10,120.00 USD | 10,120.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 10,230.00 USD | 101.75 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 10,790.00 USD | 558.90 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 82,210,000.00 USD | 82,200,000.00 USD | 0.00 USD | `+1.63%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2065` | 82,210,000.00 USD | 1,260.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 82,210,000.00 USD | 102.09 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 82,210,000.00 USD | 2,120.00 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 82,220,000.00 USD | 9,130.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 82,260,000.00 USD | 34,800.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 82,270,000.00 USD | 12,690.00 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 82,280,000.00 USD | 5,620.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 82,290,000.00 USD | 10,740.00 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 82,290,000.00 USD | 2,460.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 82,290,000.00 USD | 2,600.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 82,290,000.00 USD | 219.53 USD | 0.00 USD | `+7.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 82,290,000.00 USD | 109.91 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 82,290,000.00 USD | 584.97 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 82,420,000.00 USD | 125,830.00 USD | 0.00 USD | `+9.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 82,420,000.00 USD | 1,650.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 82,420,000.00 USD | 1,690.00 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 82,450,000.00 USD | 24,570.00 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 82,450,000.00 USD | 6,860.00 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 82,450,000.00 USD | 341.18 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 82,450,000.00 USD | 109.40 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 82,480,000.00 USD | 21,490.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 82,480,000.00 USD | 9,140.00 USD | 0.00 USD | `+13.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 82,490,000.00 USD | 9,180.00 USD | 0.00 USD | `+13.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 82,490,000.00 USD | 662.92 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 82,500,000.00 USD | 9,600.00 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 82,500,000.00 USD | 171.12 USD | 0.00 USD | `+14.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 82,510,000.00 USD | 9,340.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 82,510,000.00 USD | 1,010.00 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 82,520,000.00 USD | 9,420.00 USD | 0.00 USD | `+16.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 82,520,000.00 USD | 315.96 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 82,530,000.00 USD | 650.04 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 82,530,000.00 USD | 192.71 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 82,540,000.00 USD | 12,620.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 82,540,000.00 USD | 209.72 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 82,540,000.00 USD | 115.92 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 82,540,000.00 USD | 236.19 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 82,550,000.00 USD | 10,930.00 USD | 0.00 USD | `+20.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 82,550,000.00 USD | 288.22 USD | 0.00 USD | `+21.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 82,550,000.00 USD | 491.03 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 82,550,000.00 USD | 1,320.00 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 82,560,000.00 USD | 9,940.00 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 82,560,000.00 USD | 499.00 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 82,560,000.00 USD | 1,100.00 USD | 0.00 USD | `+23.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 82,560,000.00 USD | 168.76 USD | 0.00 USD | `+24.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 82,560,000.00 USD | 603.73 USD | 0.00 USD | `+24.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 82,570,000.00 USD | 2,170.00 USD | 0.00 USD | `+25.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 82,570,000.00 USD | 1,570.00 USD | 0.00 USD | `+26.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 82,570,000.00 USD | 3,390.00 USD | 0.00 USD | `+27.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 82,570,000.00 USD | 271.44 USD | 0.00 USD | `+28.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 82,990,000.00 USD | 421,430.00 USD | 0.00 USD | `+28.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 82,990,000.00 USD | 945.98 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 83,000,000.00 USD | 8,890.00 USD | 0.00 USD | `+32.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 83,020,000.00 USD | 14,860.00 USD | 0.00 USD | `+32.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 83,020,000.00 USD | 3,920.00 USD | 0.00 USD | `+33.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 83,020,000.00 USD | 2,710.00 USD | 0.00 USD | `+34.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 83,040,000.00 USD | 13,870.00 USD | 0.00 USD | `+35.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 83,040,000.00 USD | 4,960.00 USD | 0.00 USD | `+35.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 83,040,000.00 USD | 944.99 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 83,040,000.00 USD | 161.87 USD | 0.00 USD | `+39.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 83,040,000.00 USD | 542.34 USD | 0.00 USD | `+40.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 83,050,000.00 USD | 1,370.00 USD | 0.00 USD | `+40.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 83,050,000.00 USD | 1,080.00 USD | 0.00 USD | `+42.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 83,060,000.00 USD | 15,160.00 USD | 0.00 USD | `+43.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 83,060,000.00 USD | 796.09 USD | 0.00 USD | `+44.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 83,060,000.00 USD | 1,440.00 USD | 0.00 USD | `+47.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 83,060,000.00 USD | 355.21 USD | 0.00 USD | `+48.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 83,070,000.00 USD | 6,950.00 USD | 0.00 USD | `+48.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 83,090,000.00 USD | 18,980.00 USD | 0.00 USD | `+51.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 83,090,000.00 USD | 4,150.00 USD | 0.00 USD | `+52.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 83,100,000.00 USD | 3,250.00 USD | 0.00 USD | `+55.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 83,100,000.00 USD | 5,090.00 USD | 0.00 USD | `+58.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 83,100,000.00 USD | 1,450.00 USD | 0.00 USD | `+60.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 83,100,000.00 USD | 181.30 USD | 0.00 USD | `+60.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 83,110,000.00 USD | 1,380.00 USD | 0.00 USD | `+62.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 83,120,000.00 USD | 12,290.00 USD | 0.00 USD | `+64.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 83,120,000.00 USD | 111.06 USD | 0.00 USD | `+64.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 83,120,000.00 USD | 220.61 USD | 0.00 USD | `+68.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 83,120,000.00 USD | 3,850.00 USD | 0.00 USD | `+72.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 83,120,000.00 USD | 188.75 USD | 0.00 USD | `+86.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 83,120,000.00 USD | 121.76 USD | 0.00 USD | `+88.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 83,120,000.00 USD | 141.78 USD | 0.00 USD | `+92.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3935` | 83,120,000.00 USD | 393.50 USD | 0.00 USD | `+94.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 83,120,000.00 USD | 1,260.00 USD | 0.00 USD | `+95.10%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1700` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD |
| `1D` | `0.1710` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 23,820.00 USD | 353.70 USD | 2,350.00 USD |
| `1D` | `0.1720` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 0.00 USD | 321.20 USD | 1,770.00 USD |
| `1D` | `0.1730` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 0.00 USD | 4,280.00 USD | 13,510.00 USD |
| `1D` | `0.1740` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `1D` | `0.1760` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD |
| `1D` | `0.1770` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 53,230.00 USD | 16,740.00 USD | 79,670.00 USD |
| `1D` | `0.1780` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 62,120.00 USD | 34,290.00 USD | 67,000.00 USD |
| `1D` | `0.1790` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 73,150.00 USD | 37,010.00 USD | 46,170.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 72,000.00 USD | 24,650.00 USD | 47,570.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 38,430.00 USD | 21,250.00 USD | 44,490.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 136,500.00 USD | 8,980.00 USD | 41,990.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 27,490.00 USD | 20,190.00 USD | 23,490.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 77,630.00 USD | 29,420.00 USD | 52,530.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 128,210.00 USD | 60,170.00 USD | 124,090.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 159,010.00 USD | 7,290.00 USD | 19,510.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 102,920.00 USD | 49,970.00 USD | 36,200.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 929,740.00 USD | 0.00 USD | 929,740.00 USD | 223,120.00 USD | 49,550.00 USD | 60,450.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 596,610.00 USD | 0.00 USD | 596,610.00 USD | 162,010.00 USD | 110,140.00 USD | 0.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 324,460.00 USD | 0.00 USD | 324,460.00 USD | 0.00 USD | 114,440.00 USD | 210,020.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 292,920.00 USD | 292,920.00 USD | 0.00 USD | 292,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1910` | 585,840.00 USD | 585,840.00 USD | 0.00 USD | 292,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `1D` | `0.1920` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 470,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 375,010.00 USD | 0.00 USD | 29,890.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 139,920.00 USD | 0.00 USD | 21,130.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 21,890.00 USD | 20,360.00 USD | 17,050.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 6,090.00 USD | 178,720.00 USD | 67,540.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 30,910.00 USD | 16,390.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 62,420.00 USD | 1,260.00 USD | 5,870.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 50,670.00 USD | 37,620.00 USD | 32,790.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 188,460.00 USD | 11,400.00 USD | 204,800.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 101,890.00 USD | 121,910.00 USD | 225,290.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 32,560.00 USD | 26,640.00 USD | 89,070.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 67,350.00 USD | 81,120.00 USD | 338,420.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 35,540.00 USD | 211,200.00 USD | 124,890.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 55,220.00 USD | 24,610.00 USD | 33,330.00 USD |
| `1D` | `0.2060` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 238,370.00 USD | 30,390.00 USD | 94,760.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 505,530.00 USD | 177,310.00 USD | 279,160.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 753,960.00 USD | 203,010.00 USD | 476,510.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 209,440.00 USD | 62,330.00 USD | 162,430.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 193,160.00 USD | 96,300.00 USD | 138,440.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 192,160.00 USD | 58,850.00 USD | 90,320.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 245,390.00 USD | 82,990.00 USD | 180,130.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 68,510.00 USD | 18,760.00 USD | 46,370.00 USD |
| `7D` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `1D` | `0.2160` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 99,140.00 USD | 34,110.00 USD | 44,240.00 USD |
| `7D` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 61,590.00 USD | 17,680.00 USD | 79,670.00 USD |
| `7D` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 78,970.00 USD | 36,240.00 USD | 67,000.00 USD |
| `7D` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 0.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 85,280.00 USD | 39,700.00 USD | 46,170.00 USD |
| `7D` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `1D` | `0.2200` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 83,270.00 USD | 24,920.00 USD | 47,570.00 USD |
| `7D` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 0.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD |
| `1D` | `0.2210` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 36,960.00 USD | 20,190.00 USD | 28,100.00 USD |
| `7D` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `1D` | `0.2220` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 73,390.00 USD | 8,880.00 USD | 36,120.00 USD |
| `7D` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 0.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD |
| `1D` | `0.2230` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 22,600.00 USD | 8,440.00 USD | 19,060.00 USD |
| `7D` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 0.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD |
| `1D` | `0.2240` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD |
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
  * Total Open Interest: `416.63M` | Total OI Tokens: `2,172,121,767.2 ADA`
  * 1h OI Change: `-7.45%` | 4h OI Change: `-8.85%` | 24h OI Change: `-10.18%`
  * Exchange Breakdown: Binance=`77.36M` | Bybit=`50.22M` | OKX=`29.69M` | Hyperliquid=`27.96M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.93K` | Last 24h: `14.20K` | Last 3d: `57.34K` | Last 7d: `58.14K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0026%` |
| **USDT Bybit** | `-0.0074%` | **USDT KuCoin** | `0.0068%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0007%` | **USDT Bitget** | `0.0012%` |
| **CoinM Binance** | `0.0068%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `44.11%` | `55.89%` | `0.79` | 213,000,000.00 USD |
| `15M` | `Binance` | `43.7%` | `56.3%` | `0.78` | 97,400,000.00 USD |
| `15M` | `OKX` | `47.31%` | `52.69%` | `0.90` | 51,800,000.00 USD |
| `15M` | `Bybit` | `41.79%` | `58.21%` | `0.72` | 27,020,000.00 USD |
| `15M` | `KuCoin` | `41.38%` | `58.62%` | `0.71` | 1,930,000.00 USD |
| `15M` | `Gate` | `49.6%` | `50.4%` | `0.98` | 3,770,000.00 USD |
| `15M` | `Bitget` | `37.46%` | `62.54%` | `0.60` | 5,530,000.00 USD |
| `15M` | `BingX` | `55.23%` | `44.77%` | `1.23` | 1,270,000.00 USD |
| `15M` | `MEXC` | `45.61%` | `54.39%` | `0.84` | 7,960,000.00 USD |
| `15M` | `Bitunix` | `46.43%` | `53.57%` | `0.87` | 4,740,000.00 USD |
| `15M` | `Hyperliquid` | `46.95%` | `53.05%` | `0.89` | 2,450,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `71.08%` | `28.92%` | `2.46` | 642,370.00 USD |
| `15M` | `Crypto.com` | `48.14%` | `51.86%` | `0.93` | 172,530.00 USD |
| `15M` | `WhiteBIT` | `9.09%` | `90.91%` | `0.10` | 2,360,000.00 USD |
| `15M` | `HTX` | `25.46%` | `74.54%` | `0.34` | 2,000,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `43.34%` | `56.66%` | `0.76` | 636,360.00 USD |
| `15M` | `Aster` | `48.77%` | `51.23%` | `0.95` | 3,140,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `59.91%` | `40.09%` | `1.49` | 129,170.00 USD |
| `15M` | `Whale Positions` | `43.7%` | `56.3%` | `0.78` | 97,400,000.00 USD |
| `15M` | `Global Accounts` | `44.11%` | `55.89%` | `0.79` | 213,000,000.00 USD |
| `1H` | `ADA` | `46.27%` | `53.73%` | `0.86` | 206,730,000.00 USD |
| `1H` | `Binance` | `44.62%` | `55.38%` | `0.81` | 70,230,000.00 USD |
| `1H` | `OKX` | `46.49%` | `53.51%` | `0.87` | 26,280,000.00 USD |
| `1H` | `Bybit` | `45.65%` | `54.35%` | `0.84` | 22,250,000.00 USD |
| `1H` | `KuCoin` | `53.31%` | `46.69%` | `1.14` | 1,850,000.00 USD |
| `1H` | `Gate` | `47.7%` | `52.3%` | `0.91` | 9,850,000.00 USD |
| `1H` | `Bitget` | `45.43%` | `54.57%` | `0.83` | 18,910,000.00 USD |
| `1H` | `BingX` | `43.13%` | `56.87%` | `0.76` | 4,410,000.00 USD |
| `1H` | `MEXC` | `41.66%` | `58.34%` | `0.71` | 12,100,000.00 USD |
| `1H` | `Bitunix` | `45.97%` | `54.03%` | `0.85` | 5,200,000.00 USD |
| `1H` | `Hyperliquid` | `42.62%` | `57.38%` | `0.74` | 3,330,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.86%` | `46.14%` | `1.17` | 30,210,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `5.26%` | `94.74%` | `0.06` | 732,740.00 USD |
| `1H` | `HTX` | `45.08%` | `54.92%` | `0.82` | 297,740.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.05%` | `54.95%` | `0.82` | 767,150.00 USD |
| `1H` | `Aster` | `34.59%` | `65.41%` | `0.53` | 210,560.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.64%` | `56.36%` | `0.77` | 87,240.00 USD |
| `1H` | `Whale Positions` | `44.62%` | `55.38%` | `0.81` | 70,230,000.00 USD |
| `1H` | `Global Accounts` | `46.27%` | `53.73%` | `0.86` | 206,730,000.00 USD |
| `4H` | `ADA` | `46.70%` | `53.30%` | `0.88` | 272,700,000.00 USD |
| `4H` | `Binance` | `45.49%` | `54.51%` | `0.83` | 93,620,000.00 USD |
| `4H` | `OKX` | `46.59%` | `53.41%` | `0.87` | 31,440,000.00 USD |
| `4H` | `Bybit` | `46.1%` | `53.9%` | `0.86` | 27,310,000.00 USD |
| `4H` | `KuCoin` | `50.63%` | `49.37%` | `1.03` | 2,300,000.00 USD |
| `4H` | `Gate` | `50.65%` | `49.35%` | `1.03` | 12,970,000.00 USD |
| `4H` | `Bitget` | `45.61%` | `54.39%` | `0.84` | 22,050,000.00 USD |
| `4H` | `BingX` | `46.32%` | `53.68%` | `0.86` | 8,140,000.00 USD |
| `4H` | `MEXC` | `44.31%` | `55.69%` | `0.80` | 18,640,000.00 USD |
| `4H` | `Bitunix` | `48.3%` | `51.7%` | `0.93` | 6,750,000.00 USD |
| `4H` | `Hyperliquid` | `40.94%` | `59.06%` | `0.69` | 3,930,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.76%` | `47.24%` | `1.12` | 41,280,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.9%` | `95.1%` | `0.05` | 2,240,000.00 USD |
| `4H` | `HTX` | `45.92%` | `54.08%` | `0.85` | 539,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.12%` | `51.88%` | `0.93` | 1,190,000.00 USD |
| `4H` | `Aster` | `35.15%` | `64.85%` | `0.54` | 217,820.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.28%` | `57.72%` | `0.73` | 95,450.00 USD |
| `4H` | `Whale Positions` | `45.49%` | `54.51%` | `0.83` | 93,620,000.00 USD |
| `4H` | `Global Accounts` | `46.70%` | `53.30%` | `0.88` | 272,700,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.2026` | `0.2024` | `0.2026` | `0.2030` | `0.2016` | 791,895.15 USD | 515,308.00 USD | 276,587.15 USD | 238,720.85 USD | `+30.15%` | `4B / 0S` |
| `0:00 UTC` | `0.2017` | `0.2019` | `0.2017` | `0.2026` | `0.2016` | 936,853.56 USD | 534,839.56 USD | 402,014.00 USD | 132,825.56 USD | `+14.18%` | `1B / 1S` |
| `5:00 UTC` | `0.2021` | `0.2021` | `0.2021` | `0.2026` | `0.2016` | 650,847.81 USD | 328,375.32 USD | 322,472.48 USD | 5,902.84 USD | `+0.91%` | `1B / 0S` |
| `0:00 UTC` | `0.2026` | `0.2026` | `0.2026` | `0.2029` | `0.2021` | 795,394.00 USD | 440,558.18 USD | 354,835.82 USD | 85,722.35 USD | `+10.78%` | `1B / 0S` |
| `5:00 UTC` | `0.2024` | `0.2024` | `0.2024` | `0.2029` | `0.2021` | 784,830.17 USD | 348,021.79 USD | 436,808.38 USD | -88,786.59 USD | `-11.31%` | `0B / 1S` |
| `0:00 UTC` | `0.1996` | `0.1995` | `0.1996` | `0.2024` | `0.1980` | 9,482,489.23 USD | 4,643,460.63 USD | 4,839,028.60 USD | -195,567.97 USD | `-2.06%` | `0B / 8S` |
| `5:00 UTC` | `0.1996` | `0.1997` | `0.1996` | `0.2001` | `0.1991` | 2,005,993.91 USD | 876,806.75 USD | 1,129,187.16 USD | -252,380.41 USD | `-12.58%` | `0B / 0S` |
| `0:00 UTC` | `0.1918` | `0.1942` | `0.1918` | `0.2001` | `0.1905` | 24,025,446.30 USD | 10,254,298.46 USD | 13,771,147.84 USD | -3,516,849.37 USD | `-14.64%` | `1B / 19S` |
| `5:00 UTC` | `0.1906` | `0.1904` | `0.1906` | `0.1935` | `0.1871` | 26,316,880.25 USD | 11,827,044.75 USD | 14,489,835.50 USD | -2,662,790.75 USD | `-10.12%` | `1B / 5S` |
| `0:00 UTC` | `0.1905` | `0.1906` | `0.1905` | `0.1915` | `0.1898` | 3,131,664.41 USD | 1,521,954.19 USD | 1,609,710.22 USD | -87,756.03 USD | `-2.80%` | `0B / 1S` |

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
| `5m` | 77,000.00 USD | 2,280,000.00 USD | **`ACCUMULATION`** |
| `15m` | -1,640,000.00 USD | -8,830,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,350,000.00 USD | -9,970,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,180,000.00 USD | -10,800,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,580,000.00 USD | -10,180,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,540,000.00 USD | -12,230,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,430,000.00 USD | -11,940,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,270,000.00 USD | -8,640,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -3,770,000.00 USD | -7,510,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,810,000.00 USD | -17,110,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -16,760,000.00 USD | -35,190,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -75,110,000.00 USD | -196,680,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+77.00K` | 15m=`-1.64M` | 1h=`-3.18M` | 24h=`-7.81M`
* Futures Capital Netflows: 5m=`+2.28M` | 15m=`-8.83M` | 1h=`-10.80M` | 24h=`-17.11M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1953` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1896` (Risk Distance: `0.0057` pts)
  * +2.5R Take Profit: `0.2095`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2037` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.2094` (Risk Distance: `0.0057` pts)
  * +2.5R Take Profit: `0.1895`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1934`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
