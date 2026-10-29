# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:02:37 IST` (`2026-10-29 19:32:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2009` | **Live Ask Quote**: `0.2030` | **Mid Price**: `0.2020`
- **Spread Points**: `21.00` | **Spread BPS**: `103.99 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1999` | VWAP Z-Score: `+0.19` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0013` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.24` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2089` | Lower -3.00σ Band: `0.1910`
  * Upper +2.51σ Band: `0.2074` | Lower -2.51σ Band: `0.1924`
  * Upper +2.01σ Band: `0.2059` | Lower -2.01σ Band: `0.1939`
  * Upper +2.00σ Band: `0.2059` | Lower -2.00σ Band: `0.1939`
  * Upper +1.28σ Band: `0.2037` | Lower -1.28σ Band: `0.1961`
  * Upper +1.00σ Band: `0.2029` | Lower -1.00σ Band: `0.1969`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2017` | EMA-20=`0.2020` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2012` (Slope: `+0.0000`) | EMA-100=`0.2012`
  * Institutional Anchors: EMA-144=`0.2014` | EMA-200=`0.2018` (Slope: `+0.0391`) | EMA-233=`0.2020`
- **Range Boundaries**: 24H High=`0.2086` | 24H Low=`0.1944` | Weekly High=`0.2086` | Weekly Low=`0.1944`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2058` (Distance: `-1.87%`)
  * Point of Control (POC) = `0.2047` (Distance: `-1.33%`)
  * Value Area Low (VAL) = `0.1979` (Distance: `+2.04%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2067` | POC=`0.2054` | VAL=`0.2018`
  * Prior Day Extremes: PDH=`0.2086` | PDL=`0.1994` | PDC=`0.2054`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2057` | Weekly POC=`0.2031` | Weekly VAL=`0.2011`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.2065` | Low=`0.1944`
  * London Session (08:00-16:00 UTC): High=`0.2009` | Low=`0.1957`
  * New York Session (13:00-21:00 UTC): High=`0.2074` | Low=`0.1979`
  * Initial Balance (First Hour): IB High=`0.2000` | IB Low=`0.1977`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2011` - `0.2028`
  * Optimal Trade Entry (OTE 0.705): `0.2024`
  * Structural Invalidation Anchor (0.786): `0.2036`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.2016` | `0.2021` | `0.2015` | `0.2017` | `1,173,990` | 236,918.98 USD | 108,845.94 USD | `+45.94%` | 929,563.66 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.2017` | `0.2019` | `0.2015` | `0.2018` | `1,015,131` | 204,777.05 USD | 18,348.63 USD | `+8.96%` | 947,912.29 USD | `+0.18` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.2018` | `0.2022` | `0.2016` | `0.2020` | `426,037` | 86,037.39 USD | 22,098.19 USD | `+25.68%` | 970,010.48 USD | `+0.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.2019` | `0.2029` | `0.2016` | `0.2024` | `3,913,467` | 791,895.15 USD | 238,720.85 USD | `+30.15%` | 892,973.02 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.2023` | `0.2025` | `0.2015` | `0.2017` | `4,641,919` | 936,853.56 USD | 132,825.56 USD | `+14.18%` | 1,025,798.58 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.2017` | `0.2022` | `0.2015` | `0.2020` | `1,441,168` | 290,814.44 USD | 40,446.82 USD | `+13.91%` | 1,066,245.40 USD | `-0.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.2055` | `0.2055` | `0.2021` | `0.2035` | `51,691,771` | 10,535,643.10 USD | -960,075.10 USD | `-9.11%` | 30,302.02 USD | `-0.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.2034` | `0.2037` | `0.2012` | `0.2024` | `32,838,114` | 6,645,891.06 USD | 314,100.73 USD | `+4.73%` | 344,402.75 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.2023` | `0.2025` | `0.2015` | `0.2020` | `6,083,087` | 1,227,668.00 USD | 173,272.38 USD | `+14.11%` | 517,675.13 USD | `+0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2021` | `149,033,935` | 30,464,321.38 USD | 477,147.63 USD | `+1.57%` | 517,682.20 USD | `+0.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2058` | `0.2065` | `0.1954` | `0.1973` | `282,726,861` | 56,231,891.33 USD | -5,955,308.28 USD | `-10.59%` | -3,049,296.45 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -2,508,321.21 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2021` | `149,033,935` | 30,464,321.38 USD | 477,147.63 USD | `+1.57%` | 517,682.20 USD | `+0.14` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.2020`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `525` | `0x77ee...2902` | `SHORT` | 4,332,542.93 USD | `21,412,192.00` | `0.1911` | `0.2024` | `0.5553` | -241,291.19 USD | `-5.57%` | `10X Cross` |
| `1205` | `0x123d...3bff` | `LONG` | 1,900,608.35 USD | `9,393,142.00` | `0.2912` | `0.2024` | `0.000000` | -835,127.59 USD | `-43.94%` | `10X Cross` |
| `1258` | `0x7737...bf66` | `SHORT` | 1,837,112.53 USD | `9,091,466.00` | `0.2190` | `0.2024` | `2.13` | 153,877.26 USD | `+8.38%` | `10X Cross` |
| `1541` | `0x5f94...4b96` | `SHORT` | 1,449,223.42 USD | `7,162,318.00` | `0.2303` | `0.2024` | `0.7588` | 200,251.77 USD | `+13.82%` | `10X Cross` |
| `1758` | `0x4982...59e6` | `SHORT` | 1,214,339.51 USD | `5,998,812.00` | `0.1891` | `0.2024` | `0.3921` | -79,781.15 USD | `-6.57%` | `10X Cross` |
| `1807` | `0xcac1...26b3` | `LONG` | 1,174,076.39 USD | `5,803,927.00` | `0.2000` | `0.2024` | `0.000000` | 13,260.81 USD | `+1.13%` | `10X Cross` |
| `1988` | `0x51f6...2b39` | `LONG` | 1,024,922.92 USD | `5,065,350.00` | `0.2294` | `0.2024` | `0.000000` | -137,226.67 USD | `-13.39%` | `10X Cross` |
| `1996` | `0xeadc...9d55` | `LONG` | 1,018,462.18 USD | `5,038,400.00` | `0.2195` | `0.2024` | `0.000000` | -87,250.57 USD | `-8.57%` | `10X Cross` |
| `2011` | `0x0748...d4b2` | `SHORT` | 1,011,450.00 USD | `5,000,000.00` | `0.2036` | `0.2024` | `0.6235` | 6,407.24 USD | `+0.63%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2057` | 6,350.68 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.35K USD at 0.2057 USD [API] | `2026-10-27 21:53:01` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 6,153.52 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2051 USD [API] | `2026-10-27 22:26:18` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 9,856.01 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 9.86K USD at 0.2051 USD [API] | `2026-10-27 22:26:18` |
| `ANNOUNCEMENT` | `INFO` | `0.2050` | 6,533.03 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.53K USD at 0.2050 USD [API] | `2026-10-27 22:28:45` |
| `ANNOUNCEMENT` | `INFO` | `0.2050` | 6,645.28 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2050 USD [API] | `2026-10-27 22:28:45` |
| `ANNOUNCEMENT` | `INFO` | `0.2052` | 6,153.74 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2052 USD [API] | `2026-10-27 22:32:51` |
| `ANNOUNCEMENT` | `INFO` | `0.2054` | 6,646.97 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2054 USD [API] | `2026-10-27 23:16:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2093` (Vol: 207,000.00 USD, Dist: `+3.41%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--4.79%`)
  * 48H Horizon: Short MP=`0.2093` (Vol: 207,000.00 USD, Dist: `+3.41%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--4.79%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 261,100.00 USD, Dist: `+5.58%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--4.79%`)
  * 7D Horizon: Short MP=`0.2124` (Vol: 359,800.00 USD, Dist: `+4.93%`) | Long MP=`0.1926` (Vol: 321,900.00 USD, Dist: `--4.85%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0465` | 119.09 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 445.50 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,510.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 1,010.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 835.91 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 137,720.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,940.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 815.76 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 11,550.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 145.62 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 1,220.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,970.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 781.18 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 1,050.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 2,890.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 931.42 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 3,030.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,740.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 473.62 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 3,450.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 710.03 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 2,120.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 565.51 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 10,450.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 146.92 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 13,970.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,500.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 5,720.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 1,180.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 787.50 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 1,990.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 3,620.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 33,860.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 981.95 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 561,180.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 1,400.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 16,340.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 1,580.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 1,640.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 59,350.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 6,640.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,730.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 2,670.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 12,040.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 518.51 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,980.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 34,130.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 2,150.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 26,580.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 619,830.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,110.00 USD | 896,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 4,140.00 USD | 644,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,830.00 USD | 640,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 638,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,720.00 USD | 637,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,750.00 USD | 632,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,750.00 USD | 627,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1780` | 13,700,000.00 USD | 13,700,000.00 USD | 69,630.00 USD | 11,560.00 USD | 62,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 15,790.00 USD | 612,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,550,000.00 USD | 13,550,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 11,150.00 USD | 596,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 134,610.00 USD | 585,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,500,000.00 USD | 13,500,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 450,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 10,160,000.00 USD | 10,160,000.00 USD | 92,290.00 USD | 27,030.00 USD | 64,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 13,330,000.00 USD | 13,330,000.00 USD | 106,790.00 USD | 51,580.00 USD | 118,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 24,230.00 USD | 442,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 9,970,000.00 USD | 9,970,000.00 USD | 27,490.00 USD | 9,450.00 USD | 14,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 13,050,000.00 USD | 13,050,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 367.00 USD | 418,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 9,920,000.00 USD | 9,920,000.00 USD | 73,290.00 USD | 18,120.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,870,000.00 USD | 12,870,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 956.45 USD | 418,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 9,810,000.00 USD | 9,810,000.00 USD | 153,920.00 USD | 58,710.00 USD | 98,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 12,380,000.00 USD | 12,380,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 4,100.00 USD | 417,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 9,500,000.00 USD | 9,500,000.00 USD | 35,280.00 USD | 8,700.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 11,370,000.00 USD | 11,370,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 3,090.00 USD | 413,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 9,440,000.00 USD | 9,440,000.00 USD | 78,720.00 USD | 14,920.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,980,000.00 USD | 10,980,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 6,230.00 USD | 410,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 9,330,000.00 USD | 9,330,000.00 USD | 216,520.00 USD | 32,820.00 USD | 34,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,730,000.00 USD | 10,730,000.00 USD | 172,850.00 USD | 43,830.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1885` | 108.95 USD | 403,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1890` | 9,050,000.00 USD | 9,050,000.00 USD | 101,390.00 USD | 73,060.00 USD | 183,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,470,000.00 USD | 10,470,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 6,260.00 USD | 403,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 8,690,000.00 USD | 8,690,000.00 USD | 239,320.00 USD | 105,770.00 USD | 202,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 10,030,000.00 USD | 10,030,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1905` | 17,750.00 USD | 397,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 8,140,000.00 USD | 8,140,000.00 USD | 226,960.00 USD | 83,050.00 USD | 90,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,480,000.00 USD | 9,480,000.00 USD | 250,530.00 USD | 90,380.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1915` | 32,240.00 USD | 379,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1920` | 7,740,000.00 USD | 7,740,000.00 USD | 485,240.00 USD | 114,280.00 USD | 185,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 9,130,000.00 USD | 9,130,000.00 USD | 279,260.00 USD | 74,890.00 USD | 77,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1925` | 50,330.00 USD | 347,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1930` | 6,960,000.00 USD | 6,960,000.00 USD | 277,060.00 USD | 199,440.00 USD | 462,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,690,000.00 USD | 8,690,000.00 USD | 747,900.00 USD | 173,570.00 USD | 325,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1935` | 290,650.00 USD | 297,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1940` | 6,020,000.00 USD | 6,020,000.00 USD | 657,420.00 USD | 247,350.00 USD | 520,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,450,000.00 USD | 7,450,000.00 USD | 721,210.00 USD | 271,400.00 USD | 825,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1945` | 4,640.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1950` | 4,590,000.00 USD | 4,590,000.00 USD | 478,570.00 USD | 187,790.00 USD | 237,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,630,000.00 USD | 5,630,000.00 USD | 651,390.00 USD | 297,900.00 USD | 389,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1955` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1960` | 3,690,000.00 USD | 3,690,000.00 USD | 472,120.00 USD | 150,290.00 USD | 324,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 4,290,000.00 USD | 4,290,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1970` | 2,740,000.00 USD | 2,740,000.00 USD | 341,720.00 USD | 160,090.00 USD | 269,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 3,420,000.00 USD | 3,420,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1980` | 1,970,000.00 USD | 1,970,000.00 USD | 450,090.00 USD | 105,090.00 USD | 206,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,780,000.00 USD | 2,780,000.00 USD | 118,660.00 USD | 47,220.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1990` | 1,210,000.00 USD | 1,210,000.00 USD | 123,760.00 USD | 38,070.00 USD | 112,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,590,000.00 USD | 2,590,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2000` | 936,840.00 USD | 936,840.00 USD | 151,770.00 USD | 74,440.00 USD | 146,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 1,310,000.00 USD | 1,310,000.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2010` | 564,210.00 USD | 564,210.00 USD | 312,990.00 USD | 86,290.00 USD | 164,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 1,120,000.00 USD | 1,120,000.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 77,190.00 USD | 77,190.00 USD | 0.00 USD | 0.00 USD | 77,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 154,380.00 USD | 154,380.00 USD | 0.00 USD | 0.00 USD | 77,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2020` | 510,450.00 USD | 510,450.00 USD | 94,610.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2030` | 436,990.00 USD | 436,990.00 USD | 0.00 USD | 0.00 USD | 282,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 70,990.00 USD | 70,990.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 141,970.00 USD | 141,970.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 724,430.00 USD | 724,430.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 195,660.00 USD | 195,660.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 731,740.00 USD | 731,740.00 USD | 0.00 USD | 7,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 981,400.00 USD | 981,400.00 USD | 150,940.00 USD | 14,360.00 USD | 84,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 204,270.00 USD | 204,270.00 USD | 0.00 USD | 1,020.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 1,670,000.00 USD | 1,670,000.00 USD | 343,500.00 USD | 144,440.00 USD | 202,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 691,080.00 USD | 691,080.00 USD | 390,170.00 USD | 96,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 2,340,000.00 USD | 2,340,000.00 USD | 492,770.00 USD | 156,970.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 1,330,000.00 USD | 1,330,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 3,400,000.00 USD | 3,400,000.00 USD | 576,980.00 USD | 200,770.00 USD | 283,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 4,220,000.00 USD | 4,220,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 4,850,000.00 USD | 4,850,000.00 USD | 712,610.00 USD | 242,410.00 USD | 503,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 8,210,000.00 USD | 8,210,000.00 USD | 1,690,000.00 USD | 687,470.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 5,320,000.00 USD | 5,320,000.00 USD | 224,390.00 USD | 69,550.00 USD | 169,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 11,310,000.00 USD | 11,310,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2115` | 2,610.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2120` | 5,770,000.00 USD | 5,770,000.00 USD | 218,390.00 USD | 91,450.00 USD | 138,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 14,300,000.00 USD | 14,300,000.00 USD | 1,160,000.00 USD | 463,080.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 4,260.00 USD | 6,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 6,370,000.00 USD | 6,370,000.00 USD | 303,450.00 USD | 107,690.00 USD | 195,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,090,000.00 USD | 17,090,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2135` | 715.44 USD | 7,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2140` | 6,970,000.00 USD | 6,970,000.00 USD | 302,450.00 USD | 103,900.00 USD | 194,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 19,210,000.00 USD | 19,210,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 7,120,000.00 USD | 7,120,000.00 USD | 73,380.00 USD | 19,010.00 USD | 57,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 21,460,000.00 USD | 21,460,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 4,300.00 USD | 11,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2160` | 7,310,000.00 USD | 7,310,000.00 USD | 116,460.00 USD | 35,400.00 USD | 39,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 22,490,000.00 USD | 22,490,000.00 USD | 467,380.00 USD | 164,960.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 7,530,000.00 USD | 7,530,000.00 USD | 75,870.00 USD | 29,290.00 USD | 114,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 23,130,000.00 USD | 23,130,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2180` | 7,710,000.00 USD | 7,710,000.00 USD | 78,030.00 USD | 30,940.00 USD | 62,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 23,660,000.00 USD | 23,660,000.00 USD | 271,760.00 USD | 104,030.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 18,910.00 USD | 30,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2190` | 7,850,000.00 USD | 7,850,000.00 USD | 81,570.00 USD | 28,270.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 24,820,000.00 USD | 24,820,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2200` | 8,000,000.00 USD | 8,000,000.00 USD | 85,310.00 USD | 24,670.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,060,000.00 USD | 26,060,000.00 USD | 521,790.00 USD | 219,450.00 USD | 493,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 8,090,000.00 USD | 8,090,000.00 USD | 40,900.00 USD | 19,080.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,100,000.00 USD | 27,100,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 32,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 8,200,000.00 USD | 8,200,000.00 USD | 64,900.00 USD | 8,820.00 USD | 36,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 27,580,000.00 USD | 27,580,000.00 USD | 198,110.00 USD | 90,610.00 USD | 196,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 8,250,000.00 USD | 8,250,000.00 USD | 24,590.00 USD | 8,880.00 USD | 14,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 27,860,000.00 USD | 27,860,000.00 USD | 139,620.00 USD | 53,210.00 USD | 85,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 32,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2240` | 8,320,000.00 USD | 8,320,000.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2240` | 28,600,000.00 USD | 28,600,000.00 USD | 378,190.00 USD | 82,090.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,100,000.00 USD | 29,100,000.00 USD | 186,370.00 USD | 100,930.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2260` | 8,430,000.00 USD | 8,430,000.00 USD | 61,330.00 USD | 26,650.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,100,000.00 USD | 30,100,000.00 USD | 441,450.00 USD | 105,500.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2270` | 30,570,000.00 USD | 30,570,000.00 USD | 230,310.00 USD | 64,760.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 34,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2280` | 30,940,000.00 USD | 30,940,000.00 USD | 105,300.00 USD | 59,020.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 44,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,140,000.00 USD | 31,140,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,250,000.00 USD | 31,250,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,310,000.00 USD | 31,310,000.00 USD | 11,140.00 USD | 13,670.00 USD | 29,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2315` | 113.90 USD | 44,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 44,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 52,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2395` | 511.57 USD | 52,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 54,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 743.58 USD | 54,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,370.00 USD | 83,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2535` | 611.70 USD | 83,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 84,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 1,400.00 USD | 85,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 298.11 USD | 85,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 824.73 USD | 86,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 88,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 89,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 92,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 93,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 101,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 101,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 101,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 206.95 USD | 101,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,310.00 USD | 199,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 299.73 USD | 199,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3245` | 164.52 USD | 199,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 82,510.00 USD | 282,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 284,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3345` | 4,520.00 USD | 288,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 3,880.00 USD | 292,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3405` | 3,560.00 USD | 296,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3435` | 1,460.00 USD | 297,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3465` | 317.05 USD | 298,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 2,380.00 USD | 300,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3655` | 27,180.00 USD | 327,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 336,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 340,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3885` | 2,330,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 788.87 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3925` | 27,120.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3935` | 280.17 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3995` | 288,480.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4045` | 6,820.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0465` | 2,550,000.00 USD | 0.00 USD | 119.09 USD | `-77.02%` | `2,561.00` |
| `Live` | `Long` | `0.0495` | 2,550,000.00 USD | 0.00 USD | 445.50 USD | `-75.54%` | `9,000.00` |
| `Live` | `Long` | `0.0525` | 2,550,000.00 USD | 0.00 USD | 5,510.00 USD | `-74.05%` | `105,008.00` |
| `Live` | `Long` | `0.0645` | 2,550,000.00 USD | 0.00 USD | 1,010.00 USD | `-68.12%` | `15,628.00` |
| `Live` | `Long` | `0.0655` | 2,550,000.00 USD | 0.00 USD | 835.91 USD | `-67.63%` | `12,762.00` |
| `Live` | `Long` | `0.0735` | 2,550,000.00 USD | 0.00 USD | 137,720.00 USD | `-63.68%` | `1,873,703.00` |
| `Live` | `Long` | `0.0745` | 2,410,000.00 USD | 0.00 USD | 2,940.00 USD | `-63.18%` | `39,410.00` |
| `Live` | `Long` | `0.0775` | 2,410,000.00 USD | 0.00 USD | 815.76 USD | `-61.70%` | `10,526.00` |
| `Live` | `Long` | `0.0815` | 2,400,000.00 USD | 0.00 USD | 284.84 USD | `-59.72%` | `3,495.00` |
| `Live` | `Long` | `0.0825` | 2,400,000.00 USD | 0.00 USD | 11,550.00 USD | `-59.23%` | `140,000.00` |
| `Live` | `Long` | `0.0835` | 2,390,000.00 USD | 0.00 USD | 145.62 USD | `-58.73%` | `1,744.00` |
| `Live` | `Long` | `0.0865` | 2,390,000.00 USD | 0.00 USD | 102.50 USD | `-57.25%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,390,000.00 USD | 0.00 USD | 1,220.00 USD | `-56.76%` | `13,940.00` |
| `Live` | `Long` | `0.0885` | 2,390,000.00 USD | 0.00 USD | 1,150.00 USD | `-56.26%` | `13,050.00` |
| `Live` | `Long` | `0.0925` | 2,390,000.00 USD | 0.00 USD | 165.11 USD | `-54.29%` | `1,785.00` |
| `Live` | `Long` | `0.0945` | 2,390,000.00 USD | 0.00 USD | 327.54 USD | `-53.30%` | `3,466.00` |
| `Live` | `Long` | `0.1025` | 2,390,000.00 USD | 0.00 USD | 4,970.00 USD | `-49.35%` | `48,516.00` |
| `Live` | `Long` | `0.1035` | 2,380,000.00 USD | 0.00 USD | 1,050.00 USD | `-48.85%` | `10,149.00` |
| `Live` | `Long` | `0.1065` | 2,380,000.00 USD | 0.00 USD | 781.18 USD | `-47.37%` | `7,335.00` |
| `Live` | `Long` | `0.1085` | 2,380,000.00 USD | 0.00 USD | 1,050.00 USD | `-46.38%` | `9,713.00` |
| `Live` | `Long` | `0.1095` | 2,380,000.00 USD | 0.00 USD | 2,890.00 USD | `-45.89%` | `26,415.00` |
| `Live` | `Long` | `0.1145` | 2,380,000.00 USD | 0.00 USD | 862.64 USD | `-43.41%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,380,000.00 USD | 0.00 USD | 13,360.00 USD | `-42.43%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,360,000.00 USD | 0.00 USD | 931.42 USD | `-41.93%` | `7,927.00` |
| `Live` | `Long` | `0.1205` | 2,360,000.00 USD | 0.00 USD | 826.27 USD | `-40.45%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,360,000.00 USD | 0.00 USD | 1,050.00 USD | `-39.96%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,360,000.00 USD | 0.00 USD | 3,030.00 USD | `-38.97%` | `24,507.00` |
| `Live` | `Long` | `0.1245` | 2,360,000.00 USD | 0.00 USD | 404.62 USD | `-38.47%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,360,000.00 USD | 0.00 USD | 2,740.00 USD | `-37.98%` | `21,866.00` |
| `Live` | `Long` | `0.1265` | 2,360,000.00 USD | 0.00 USD | 473.62 USD | `-37.48%` | `3,744.00` |
| `Live` | `Long` | `0.1275` | 2,360,000.00 USD | 0.00 USD | 1,260.00 USD | `-36.99%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,350,000.00 USD | 0.00 USD | 2,540.00 USD | `-36.00%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,350,000.00 USD | 0.00 USD | 3,450.00 USD | `-35.51%` | `26,427.00` |
| `Live` | `Long` | `0.1315` | 2,350,000.00 USD | 0.00 USD | 687.35 USD | `-35.01%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,350,000.00 USD | 0.00 USD | 6,960.00 USD | `-34.52%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,340,000.00 USD | 0.00 USD | 3,600.00 USD | `-34.03%` | `26,965.00` |
| `Live` | `Long` | `0.1345` | 2,340,000.00 USD | 0.00 USD | 710.03 USD | `-33.53%` | `5,279.00` |
| `Live` | `Long` | `0.1355` | 2,340,000.00 USD | 0.00 USD | 106.64 USD | `-33.04%` | `787.00` |
| `Live` | `Long` | `0.1395` | 2,340,000.00 USD | 0.00 USD | 2,120.00 USD | `-31.06%` | `15,162.00` |
| `Live` | `Long` | `0.1405` | 2,330,000.00 USD | 0.00 USD | 565.51 USD | `-30.57%` | `4,025.00` |
| `Live` | `Long` | `0.1415` | 2,330,000.00 USD | 0.00 USD | 10,450.00 USD | `-30.07%` | `73,863.00` |
| `Live` | `Long` | `0.1425` | 2,320,000.00 USD | 0.00 USD | 146.92 USD | `-29.58%` | `1,031.00` |
| `Live` | `Long` | `0.1435` | 2,320,000.00 USD | 0.00 USD | 13,970.00 USD | `-29.08%` | `97,369.00` |
| `Live` | `Long` | `0.1445` | 2,310,000.00 USD | 0.00 USD | 2,500.00 USD | `-28.59%` | `17,302.00` |
| `Live` | `Long` | `0.1455` | 2,310,000.00 USD | 0.00 USD | 5,720.00 USD | `-28.09%` | `39,318.00` |
| `Live` | `Long` | `0.1465` | 2,300,000.00 USD | 0.00 USD | 4,580.00 USD | `-27.60%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,300,000.00 USD | 0.00 USD | 1,180.00 USD | `-27.11%` | `8,000.00` |
| `Live` | `Long` | `0.1485` | 2,290,000.00 USD | 0.00 USD | 787.50 USD | `-26.61%` | `5,303.00` |
| `Live` | `Long` | `0.1495` | 2,290,000.00 USD | 0.00 USD | 1,990.00 USD | `-26.12%` | `13,323.00` |
| `Live` | `Long` | `0.1505` | 2,290,000.00 USD | 0.00 USD | 3,620.00 USD | `-25.62%` | `24,082.00` |
| `Live` | `Long` | `0.1515` | 2,290,000.00 USD | 0.00 USD | 33,860.00 USD | `-25.13%` | `223,513.00` |
| `Live` | `Long` | `0.1525` | 2,250,000.00 USD | 0.00 USD | 981.95 USD | `-24.64%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 2,250,000.00 USD | 0.00 USD | 561,180.00 USD | `-24.14%` | `3,655,893.00` |
| `Live` | `Long` | `0.1545` | 1,690,000.00 USD | 0.00 USD | 1,400.00 USD | `-23.65%` | `9,062.00` |
| `Live` | `Long` | `0.1555` | 1,690,000.00 USD | 0.00 USD | 16,340.00 USD | `-23.15%` | `105,110.00` |
| `Live` | `Long` | `0.1565` | 1,670,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.66%` | `10,116.00` |
| `Live` | `Long` | `0.1585` | 1,670,000.00 USD | 0.00 USD | 6,000.00 USD | `-21.67%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,670,000.00 USD | 0.00 USD | 1,640.00 USD | `-21.18%` | `10,259.00` |
| `Live` | `Long` | `0.1605` | 1,670,000.00 USD | 0.00 USD | 59,350.00 USD | `-20.68%` | `369,768.00` |
| `Live` | `Long` | `0.1615` | 1,610,000.00 USD | 0.00 USD | 6,640.00 USD | `-20.19%` | `41,137.00` |
| `Live` | `Long` | `0.1625` | 1,600,000.00 USD | 0.00 USD | 2,730.00 USD | `-19.69%` | `16,830.00` |
| `Live` | `Long` | `0.1635` | 1,600,000.00 USD | 0.00 USD | 2,670.00 USD | `-19.20%` | `16,314.00` |
| `Live` | `Long` | `0.1645` | 1,590,000.00 USD | 0.00 USD | 12,040.00 USD | `-18.71%` | `73,221.00` |
| `Live` | `Long` | `0.1655` | 1,580,000.00 USD | 0.00 USD | 518.51 USD | `-18.21%` | `3,133.00` |
| `Live` | `Long` | `0.1665` | 1,580,000.00 USD | 0.00 USD | 1,980.00 USD | `-17.72%` | `11,889.00` |
| `Live` | `Long` | `0.1675` | 1,580,000.00 USD | 0.00 USD | 34,130.00 USD | `-17.22%` | `203,766.00` |
| `Live` | `Long` | `0.1685` | 1,550,000.00 USD | 0.00 USD | 2,150.00 USD | `-16.73%` | `12,768.00` |
| `Live` | `Long` | `0.1695` | 1,540,000.00 USD | 0.00 USD | 26,580.00 USD | `-16.23%` | `156,825.00` |
| `Live` | `Long` | `0.1705` | 1,520,000.00 USD | 0.00 USD | 619,830.00 USD | `-15.74%` | `3,635,347.00` |
| `Live` | `Long` | `0.1715` | 896,640.00 USD | 0.00 USD | 252,110.00 USD | `-15.25%` | `1,470,005.00` |
| `Live` | `Long` | `0.1725` | 644,540.00 USD | 0.00 USD | 4,140.00 USD | `-14.75%` | `24,013.00` |
| `Live` | `Long` | `0.1735` | 640,400.00 USD | 0.00 USD | 1,830.00 USD | `-14.26%` | `10,522.00` |
| `Live` | `Long` | `0.1745` | 638,570.00 USD | 0.00 USD | 1,320.00 USD | `-13.76%` | `7,554.00` |
| `Live` | `Long` | `0.1755` | 637,250.00 USD | 0.00 USD | 4,720.00 USD | `-13.27%` | `26,871.00` |
| `Live` | `Long` | `0.1765` | 632,540.00 USD | 0.00 USD | 4,750.00 USD | `-12.77%` | `26,931.00` |
| `Live` | `Long` | `0.1775` | 627,780.00 USD | 0.00 USD | 15,750.00 USD | `-12.28%` | `88,754.00` |
| `Live` | `Long` | `0.1785` | 612,030.00 USD | 0.00 USD | 15,790.00 USD | `-11.79%` | `88,484.00` |
| `Live` | `Long` | `0.1795` | 596,230.00 USD | 0.00 USD | 11,150.00 USD | `-11.29%` | `62,104.00` |
| `Live` | `Long` | `0.1805` | 585,090.00 USD | 0.00 USD | 134,610.00 USD | `-10.80%` | `745,776.00` |
| `Live` | `Long` | `0.1815` | 450,470.00 USD | 0.00 USD | 7,670.00 USD | `-10.30%` | `42,240.00` |
| `Live` | `Long` | `0.1825` | 442,810.00 USD | 0.00 USD | 24,230.00 USD | `-9.81%` | `132,755.00` |
| `Live` | `Long` | `0.1835` | 418,580.00 USD | 0.00 USD | 367.00 USD | `-9.32%` | `2,000.00` |
| `Live` | `Long` | `0.1845` | 418,210.00 USD | 0.00 USD | 956.45 USD | `-8.82%` | `5,184.00` |
| `Live` | `Long` | `0.1855` | 417,260.00 USD | 0.00 USD | 4,100.00 USD | `-8.33%` | `22,111.00` |
| `Live` | `Long` | `0.1865` | 413,150.00 USD | 0.00 USD | 3,090.00 USD | `-7.83%` | `16,543.00` |
| `Live` | `Long` | `0.1875` | 410,070.00 USD | 0.00 USD | 6,230.00 USD | `-7.34%` | `33,234.00` |
| `Live` | `Long` | `0.1885` | 403,840.00 USD | 0.00 USD | 108.95 USD | `-6.84%` | `578.00` |
| `Live` | `Long` | `0.1895` | 403,730.00 USD | 0.00 USD | 6,260.00 USD | `-6.35%` | `33,010.00` |
| `Live` | `Long` | `0.1905` | 397,470.00 USD | 0.00 USD | 17,750.00 USD | `-5.86%` | `93,172.00` |
| `Live` | `Long` | `0.1915` | 379,720.00 USD | 0.00 USD | 32,240.00 USD | `-5.36%` | `168,337.00` |
| `Live` | `Long` | `0.1925` | 347,490.00 USD | 0.00 USD | 50,330.00 USD | `-4.87%` | `261,472.00` |
| `Live` | `Long` | `0.1935` | 297,150.00 USD | 0.00 USD | 290,650.00 USD | `-4.37%` | `1,502,046.00` |
| `Live` | `Long` | `0.1945` | 6,510.00 USD | 0.00 USD | 4,640.00 USD | `-3.88%` | `23,844.00` |
| `Live` | `Long` | `0.1955` | 1,870.00 USD | 0.00 USD | 1,870.00 USD | `-3.39%` | `9,570.00` |
| `Live` | `Short` | `0.2115` | 2,610.00 USD | 2,610.00 USD | 0.00 USD | `+4.52%` | `12,331.00` |
| `Live` | `Short` | `0.2125` | 6,870.00 USD | 4,260.00 USD | 0.00 USD | `+5.02%` | `20,047.00` |
| `Live` | `Short` | `0.2135` | 7,580.00 USD | 715.44 USD | 0.00 USD | `+5.51%` | `3,351.00` |
| `Live` | `Short` | `0.2155` | 11,880.00 USD | 4,300.00 USD | 0.00 USD | `+6.50%` | `19,938.00` |
| `Live` | `Short` | `0.2185` | 30,790.00 USD | 18,910.00 USD | 0.00 USD | `+7.98%` | `86,525.00` |
| `Live` | `Short` | `0.2215` | 32,430.00 USD | 1,640.00 USD | 0.00 USD | `+9.46%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 32,630.00 USD | 200.48 USD | 0.00 USD | `+10.45%` | `897.00` |
| `Live` | `Short` | `0.2275` | 34,790.00 USD | 2,160.00 USD | 0.00 USD | `+12.43%` | `9,500.00` |
| `Live` | `Short` | `0.2285` | 44,030.00 USD | 9,240.00 USD | 0.00 USD | `+12.92%` | `40,428.00` |
| `Live` | `Short` | `0.2315` | 44,140.00 USD | 113.90 USD | 0.00 USD | `+14.41%` | `492.00` |
| `Live` | `Short` | `0.2325` | 44,430.00 USD | 282.02 USD | 0.00 USD | `+14.90%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 52,060.00 USD | 7,640.00 USD | 0.00 USD | `+15.39%` | `32,708.00` |
| `Live` | `Short` | `0.2395` | 52,570.00 USD | 511.57 USD | 0.00 USD | `+18.36%` | `2,136.00` |
| `Live` | `Short` | `0.2405` | 54,040.00 USD | 1,470.00 USD | 0.00 USD | `+18.85%` | `6,110.00` |
| `Live` | `Short` | `0.2415` | 54,790.00 USD | 743.58 USD | 0.00 USD | `+19.35%` | `3,079.00` |
| `Live` | `Short` | `0.2525` | 83,160.00 USD | 28,370.00 USD | 0.00 USD | `+24.78%` | `112,352.00` |
| `Live` | `Short` | `0.2535` | 83,770.00 USD | 611.70 USD | 0.00 USD | `+25.28%` | `2,413.00` |
| `Live` | `Short` | `0.2585` | 84,150.00 USD | 380.25 USD | 0.00 USD | `+27.75%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 85,550.00 USD | 1,400.00 USD | 0.00 USD | `+29.23%` | `5,346.00` |
| `Live` | `Short` | `0.2715` | 85,840.00 USD | 298.11 USD | 0.00 USD | `+34.17%` | `1,098.00` |
| `Live` | `Short` | `0.2775` | 86,670.00 USD | 824.73 USD | 0.00 USD | `+37.14%` | `2,972.00` |
| `Live` | `Short` | `0.2845` | 88,840.00 USD | 2,170.00 USD | 0.00 USD | `+40.60%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 89,250.00 USD | 411.09 USD | 0.00 USD | `+43.07%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 92,520.00 USD | 3,260.00 USD | 0.00 USD | `+44.06%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 93,040.00 USD | 519.79 USD | 0.00 USD | `+45.05%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 101,020.00 USD | 7,990.00 USD | 0.00 USD | `+46.03%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 101,170.00 USD | 146.34 USD | 0.00 USD | `+48.51%` | `487.00` |
| `Live` | `Short` | `0.3055` | 101,580.00 USD | 408.15 USD | 0.00 USD | `+50.98%` | `1,336.00` |
| `Live` | `Short` | `0.3075` | 101,780.00 USD | 206.95 USD | 0.00 USD | `+51.96%` | `673.00` |
| `Live` | `Short` | `0.3115` | 199,090.00 USD | 97,310.00 USD | 0.00 USD | `+53.94%` | `312,388.00` |
| `Live` | `Short` | `0.3155` | 199,390.00 USD | 299.73 USD | 0.00 USD | `+55.92%` | `950.00` |
| `Live` | `Short` | `0.3245` | 199,560.00 USD | 164.52 USD | 0.00 USD | `+60.37%` | `507.00` |
| `Live` | `Short` | `0.3275` | 282,070.00 USD | 82,510.00 USD | 0.00 USD | `+61.85%` | `251,952.00` |
| `Live` | `Short` | `0.3295` | 284,450.00 USD | 2,380.00 USD | 0.00 USD | `+62.84%` | `7,219.00` |
| `Live` | `Short` | `0.3345` | 288,970.00 USD | 4,520.00 USD | 0.00 USD | `+65.31%` | `13,504.00` |
| `Live` | `Short` | `0.3385` | 292,850.00 USD | 3,880.00 USD | 0.00 USD | `+67.28%` | `11,458.00` |
| `Live` | `Short` | `0.3405` | 296,410.00 USD | 3,560.00 USD | 0.00 USD | `+68.27%` | `10,456.00` |
| `Live` | `Short` | `0.3435` | 297,870.00 USD | 1,460.00 USD | 0.00 USD | `+69.76%` | `4,254.00` |
| `Live` | `Short` | `0.3465` | 298,180.00 USD | 317.05 USD | 0.00 USD | `+71.24%` | `915.00` |
| `Live` | `Short` | `0.3495` | 300,560.00 USD | 2,380.00 USD | 0.00 USD | `+72.72%` | `6,797.00` |
| `Live` | `Short` | `0.3655` | 327,740.00 USD | 27,180.00 USD | 0.00 USD | `+80.63%` | `74,360.00` |
| `Live` | `Short` | `0.3715` | 336,910.00 USD | 9,170.00 USD | 0.00 USD | `+83.59%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 340,050.00 USD | 3,140.00 USD | 0.00 USD | `+85.08%` | `8,395.00` |
| `Live` | `Short` | `0.3885` | 2,670,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+91.99%` | `5,998,812.00` |
| `Live` | `Short` | `0.3915` | 2,670,000.00 USD | 788.87 USD | 0.00 USD | `+93.48%` | `2,015.00` |
| `Live` | `Short` | `0.3925` | 2,700,000.00 USD | 27,120.00 USD | 0.00 USD | `+93.97%` | `69,098.00` |
| `Live` | `Short` | `0.3935` | 2,700,000.00 USD | 280.17 USD | 0.00 USD | `+94.47%` | `712.00` |
| `Live` | `Short` | `0.3995` | 2,990,000.00 USD | 288,480.00 USD | 0.00 USD | `+97.43%` | `722,091.00` |
| `Live` | `Short` | `0.4045` | 2,990,000.00 USD | 6,820.00 USD | 0.00 USD | `+99.90%` | `16,862.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 558,720,000.00 USD | 0.00 USD | 415.13 USD | `-70.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 558,720,000.00 USD | 0.00 USD | 438.99 USD | `-70.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 558,720,000.00 USD | 0.00 USD | 1,100.00 USD | `-45.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 558,720,000.00 USD | 0.00 USD | 541.33 USD | `-44.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 558,720,000.00 USD | 0.00 USD | 602,500.00 USD | `-40.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 558,110,000.00 USD | 0.00 USD | 1,320.00 USD | `-36.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 558,110,000.00 USD | 0.00 USD | 13,390.00 USD | `-35.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 558,100,000.00 USD | 0.00 USD | 728.88 USD | `-34.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 558,100,000.00 USD | 0.00 USD | 4,350.00 USD | `-33.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 558,100,000.00 USD | 0.00 USD | 542.99 USD | `-32.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 558,090,000.00 USD | 0.00 USD | 1,820.00 USD | `-31.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 558,090,000.00 USD | 0.00 USD | 1,050.00 USD | `-30.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 558,090,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 558,090,000.00 USD | 0.00 USD | 1,600.00 USD | `-29.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 558,090,000.00 USD | 0.00 USD | 4,580.00 USD | `-28.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 558,080,000.00 USD | 0.00 USD | 303.26 USD | `-25.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 558,080,000.00 USD | 0.00 USD | 1,290.00 USD | `-25.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 558,080,000.00 USD | 0.00 USD | 279.53 USD | `-24.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 558,080,000.00 USD | 0.00 USD | 324.30 USD | `-23.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 558,080,000.00 USD | 0.00 USD | 1,480.00 USD | `-23.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 558,080,000.00 USD | 0.00 USD | 552.21 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 558,080,000.00 USD | 0.00 USD | 166.84 USD | `-21.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 558,080,000.00 USD | 0.00 USD | 2,990.00 USD | `-20.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 558,080,000.00 USD | 0.00 USD | 562.67 USD | `-20.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 558,080,000.00 USD | 0.00 USD | 24,760.00 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 558,050,000.00 USD | 0.00 USD | 6,540.00 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 558,040,000.00 USD | 0.00 USD | 2,870.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 558,040,000.00 USD | 0.00 USD | 452.97 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 558,040,000.00 USD | 0.00 USD | 13,930.00 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 558,030,000.00 USD | 0.00 USD | 317.92 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 558,030,000.00 USD | 0.00 USD | 6,740.00 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 558,020,000.00 USD | 0.00 USD | 4,270.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 558,020,000.00 USD | 0.00 USD | 7,630.00 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 558,010,000.00 USD | 0.00 USD | 6,860.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 558,000,000.00 USD | 0.00 USD | 6,900.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 557,990,000.00 USD | 0.00 USD | 103.58 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 557,990,000.00 USD | 0.00 USD | 8,220.00 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 557,990,000.00 USD | 0.00 USD | 1,760.00 USD | `-13.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 557,980,000.00 USD | 0.00 USD | 623.57 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 557,980,000.00 USD | 0.00 USD | 4,440.00 USD | `-12.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 557,980,000.00 USD | 0.00 USD | 12,390.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 557,970,000.00 USD | 0.00 USD | 5,760.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 557,960,000.00 USD | 0.00 USD | 26,470.00 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 557,930,000.00 USD | 0.00 USD | 2,890.00 USD | `-10.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 557,930,000.00 USD | 0.00 USD | 3,080.00 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 557,930,000.00 USD | 0.00 USD | 3,160.00 USD | `-9.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 557,930,000.00 USD | 0.00 USD | 18,650.00 USD | `-8.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 557,910,000.00 USD | 0.00 USD | 282.33 USD | `-8.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 557,910,000.00 USD | 0.00 USD | 218.76 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 557,910,000.00 USD | 0.00 USD | 109.69 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 557,910,000.00 USD | 0.00 USD | 7,390.00 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 557,900,000.00 USD | 0.00 USD | 837.40 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 557,900,000.00 USD | 0.00 USD | 6,450.00 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 557,890,000.00 USD | 0.00 USD | 2,030.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 557,890,000.00 USD | 0.00 USD | 513.01 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 557,890,000.00 USD | 0.00 USD | 2,480.00 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 557,890,000.00 USD | 0.00 USD | 2,620.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1955` | 557,880,000.00 USD | 0.00 USD | 2,050.00 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1965` | 557,880,000.00 USD | 0.00 USD | 2,380.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1975` | 557,880,000.00 USD | 0.00 USD | 79,010,000.00 USD | `-2.40%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1985` | 478,870,000.00 USD | 0.00 USD | 79,400,000.00 USD | `-1.90%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1995` | 399,470,000.00 USD | 0.00 USD | 319,240,000.00 USD | `-1.41%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2005` | 80,230,000.00 USD | 0.00 USD | 80,210,000.00 USD | `-0.91%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2015` | 18,790.00 USD | 0.00 USD | 18,790.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 10,120.00 USD | 10,120.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 10,230.00 USD | 101.75 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 10,790.00 USD | 558.90 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 82,210,000.00 USD | 82,200,000.00 USD | 0.00 USD | `+1.56%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2065` | 82,210,000.00 USD | 1,260.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 82,210,000.00 USD | 102.09 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 82,230,000.00 USD | 21,560.00 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 82,240,000.00 USD | 9,130.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 82,280,000.00 USD | 34,800.00 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 82,290,000.00 USD | 12,690.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 82,300,000.00 USD | 5,620.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 82,310,000.00 USD | 10,740.00 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 82,310,000.00 USD | 2,460.00 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 82,310,000.00 USD | 2,600.00 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 82,310,000.00 USD | 219.53 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 82,310,000.00 USD | 109.91 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 82,310,000.00 USD | 584.97 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 82,440,000.00 USD | 125,830.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 82,440,000.00 USD | 1,650.00 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 82,440,000.00 USD | 1,690.00 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 82,440,000.00 USD | 501.31 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 82,450,000.00 USD | 6,860.00 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 82,450,000.00 USD | 341.18 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 82,450,000.00 USD | 109.40 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 82,470,000.00 USD | 21,490.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 82,480,000.00 USD | 9,140.00 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 82,490,000.00 USD | 9,180.00 USD | 0.00 USD | `+13.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 82,490,000.00 USD | 662.92 USD | 0.00 USD | `+13.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 82,500,000.00 USD | 9,600.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 82,500,000.00 USD | 171.12 USD | 0.00 USD | `+14.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 82,510,000.00 USD | 9,340.00 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 82,510,000.00 USD | 1,010.00 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 82,520,000.00 USD | 9,420.00 USD | 0.00 USD | `+16.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 82,520,000.00 USD | 315.96 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 82,520,000.00 USD | 650.04 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 82,520,000.00 USD | 192.71 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 82,530,000.00 USD | 12,620.00 USD | 0.00 USD | `+18.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 82,530,000.00 USD | 209.72 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 82,530,000.00 USD | 115.92 USD | 0.00 USD | `+19.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 82,530,000.00 USD | 236.19 USD | 0.00 USD | `+20.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 82,540,000.00 USD | 10,930.00 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 82,550,000.00 USD | 288.22 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 82,550,000.00 USD | 491.03 USD | 0.00 USD | `+21.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 82,550,000.00 USD | 1,320.00 USD | 0.00 USD | `+22.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 82,560,000.00 USD | 9,940.00 USD | 0.00 USD | `+22.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 82,560,000.00 USD | 499.00 USD | 0.00 USD | `+23.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 82,560,000.00 USD | 1,100.00 USD | 0.00 USD | `+23.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 82,560,000.00 USD | 168.76 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 82,560,000.00 USD | 603.73 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 82,560,000.00 USD | 2,170.00 USD | 0.00 USD | `+25.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 82,560,000.00 USD | 1,570.00 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 82,570,000.00 USD | 3,390.00 USD | 0.00 USD | `+27.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 82,570,000.00 USD | 271.44 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 82,990,000.00 USD | 421,430.00 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 82,990,000.00 USD | 945.98 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 83,000,000.00 USD | 8,890.00 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 83,010,000.00 USD | 14,860.00 USD | 0.00 USD | `+32.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 83,020,000.00 USD | 3,920.00 USD | 0.00 USD | `+33.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 83,020,000.00 USD | 2,710.00 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 83,030,000.00 USD | 13,870.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 83,040,000.00 USD | 4,960.00 USD | 0.00 USD | `+35.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 83,040,000.00 USD | 944.99 USD | 0.00 USD | `+38.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 83,040,000.00 USD | 161.87 USD | 0.00 USD | `+39.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 83,040,000.00 USD | 542.34 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 83,040,000.00 USD | 1,370.00 USD | 0.00 USD | `+40.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 83,040,000.00 USD | 1,080.00 USD | 0.00 USD | `+42.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 83,060,000.00 USD | 15,160.00 USD | 0.00 USD | `+43.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 83,060,000.00 USD | 796.09 USD | 0.00 USD | `+44.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 83,060,000.00 USD | 1,440.00 USD | 0.00 USD | `+47.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 83,060,000.00 USD | 355.21 USD | 0.00 USD | `+48.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 83,070,000.00 USD | 6,950.00 USD | 0.00 USD | `+48.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 83,090,000.00 USD | 18,980.00 USD | 0.00 USD | `+50.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 83,090,000.00 USD | 4,150.00 USD | 0.00 USD | `+52.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 83,090,000.00 USD | 3,250.00 USD | 0.00 USD | `+55.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 83,100,000.00 USD | 5,090.00 USD | 0.00 USD | `+58.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 83,100,000.00 USD | 1,450.00 USD | 0.00 USD | `+60.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 83,100,000.00 USD | 181.30 USD | 0.00 USD | `+60.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 83,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+62.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 83,110,000.00 USD | 12,290.00 USD | 0.00 USD | `+64.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 83,110,000.00 USD | 111.06 USD | 0.00 USD | `+64.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 83,110,000.00 USD | 220.61 USD | 0.00 USD | `+68.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 83,120,000.00 USD | 3,850.00 USD | 0.00 USD | `+72.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 83,120,000.00 USD | 188.75 USD | 0.00 USD | `+86.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 83,120,000.00 USD | 121.76 USD | 0.00 USD | `+88.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 83,120,000.00 USD | 141.78 USD | 0.00 USD | `+92.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3935` | 83,120,000.00 USD | 393.50 USD | 0.00 USD | `+94.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 83,120,000.00 USD | 1,260.00 USD | 0.00 USD | `+94.96%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1780` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 69,630.00 USD | 11,560.00 USD | 62,840.00 USD |
| `7D` | `0.1790` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD |
| `7D` | `0.1800` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `7D` | `0.1810` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 92,290.00 USD | 27,030.00 USD | 64,220.00 USD |
| `7D` | `0.1820` | 13,330,000.00 USD | 0.00 USD | 13,330,000.00 USD | 106,790.00 USD | 51,580.00 USD | 118,390.00 USD |
| `1D` | `0.1830` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 27,490.00 USD | 9,450.00 USD | 14,940.00 USD |
| `7D` | `0.1830` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 73,290.00 USD | 18,120.00 USD | 18,760.00 USD |
| `7D` | `0.1840` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 153,920.00 USD | 58,710.00 USD | 98,260.00 USD |
| `7D` | `0.1850` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 35,280.00 USD | 8,700.00 USD | 14,030.00 USD |
| `7D` | `0.1860` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 78,720.00 USD | 14,920.00 USD | 15,170.00 USD |
| `7D` | `0.1870` | 10,980,000.00 USD | 0.00 USD | 10,980,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 216,520.00 USD | 32,820.00 USD | 34,840.00 USD |
| `7D` | `0.1880` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 172,850.00 USD | 43,830.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 101,390.00 USD | 73,060.00 USD | 183,110.00 USD |
| `7D` | `0.1890` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 239,320.00 USD | 105,770.00 USD | 202,770.00 USD |
| `7D` | `0.1900` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 226,960.00 USD | 83,050.00 USD | 90,970.00 USD |
| `7D` | `0.1910` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 250,530.00 USD | 90,380.00 USD | 16,510.00 USD |
| `1D` | `0.1920` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 485,240.00 USD | 114,280.00 USD | 185,370.00 USD |
| `7D` | `0.1920` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 279,260.00 USD | 74,890.00 USD | 77,590.00 USD |
| `1D` | `0.1930` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 277,060.00 USD | 199,440.00 USD | 462,380.00 USD |
| `7D` | `0.1930` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 747,900.00 USD | 173,570.00 USD | 325,790.00 USD |
| `1D` | `0.1940` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 657,420.00 USD | 247,350.00 USD | 520,020.00 USD |
| `7D` | `0.1940` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 721,210.00 USD | 271,400.00 USD | 825,170.00 USD |
| `1D` | `0.1950` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 478,570.00 USD | 187,790.00 USD | 237,550.00 USD |
| `7D` | `0.1950` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 651,390.00 USD | 297,900.00 USD | 389,660.00 USD |
| `1D` | `0.1960` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 472,120.00 USD | 150,290.00 USD | 324,410.00 USD |
| `7D` | `0.1960` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 341,720.00 USD | 160,090.00 USD | 269,390.00 USD |
| `7D` | `0.1970` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 450,090.00 USD | 105,090.00 USD | 206,760.00 USD |
| `7D` | `0.1980` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 118,660.00 USD | 47,220.00 USD | 23,890.00 USD |
| `1D` | `0.1990` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 123,760.00 USD | 38,070.00 USD | 112,190.00 USD |
| `7D` | `0.1990` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 936,840.00 USD | 0.00 USD | 936,840.00 USD | 151,770.00 USD | 74,440.00 USD | 146,420.00 USD |
| `7D` | `0.2000` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 564,210.00 USD | 0.00 USD | 564,210.00 USD | 312,990.00 USD | 86,290.00 USD | 164,930.00 USD |
| `7D` | `0.2010` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 77,190.00 USD | 77,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77,190.00 USD |
| `1D` | `0.2020` | 154,380.00 USD | 154,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77,190.00 USD |
| `7D` | `0.2020` | 510,450.00 USD | 0.00 USD | 510,450.00 USD | 94,610.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 436,990.00 USD | 436,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 282,600.00 USD |
| `7D` | `0.2030` | 70,990.00 USD | 70,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD |
| `7D` | `0.2030` | 141,970.00 USD | 141,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD |
| `1D` | `0.2040` | 724,430.00 USD | 724,430.00 USD | 0.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD |
| `7D` | `0.2040` | 195,660.00 USD | 195,660.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 731,740.00 USD | 731,740.00 USD | 0.00 USD | 0.00 USD | 7,310.00 USD | 0.00 USD |
| `1D` | `0.2060` | 981,400.00 USD | 981,400.00 USD | 0.00 USD | 150,940.00 USD | 14,360.00 USD | 84,360.00 USD |
| `7D` | `0.2060` | 204,270.00 USD | 204,270.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 7,590.00 USD |
| `1D` | `0.2070` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 343,500.00 USD | 144,440.00 USD | 202,190.00 USD |
| `7D` | `0.2070` | 691,080.00 USD | 691,080.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 0.00 USD |
| `1D` | `0.2080` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 492,770.00 USD | 156,970.00 USD | 13,790.00 USD |
| `7D` | `0.2080` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 576,980.00 USD | 200,770.00 USD | 283,100.00 USD |
| `7D` | `0.2090` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 712,610.00 USD | 242,410.00 USD | 503,180.00 USD |
| `7D` | `0.2100` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 1,690,000.00 USD | 687,470.00 USD | 1,610,000.00 USD |
| `1D` | `0.2110` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 224,390.00 USD | 69,550.00 USD | 169,900.00 USD |
| `7D` | `0.2110` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 218,390.00 USD | 91,450.00 USD | 138,440.00 USD |
| `7D` | `0.2120` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 1,160,000.00 USD | 463,080.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 303,450.00 USD | 107,690.00 USD | 195,630.00 USD |
| `7D` | `0.2130` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 302,450.00 USD | 103,900.00 USD | 194,350.00 USD |
| `7D` | `0.2140` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 73,380.00 USD | 19,010.00 USD | 57,150.00 USD |
| `7D` | `0.2150` | 21,460,000.00 USD | 21,460,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `1D` | `0.2160` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 116,460.00 USD | 35,400.00 USD | 39,560.00 USD |
| `7D` | `0.2160` | 22,490,000.00 USD | 22,490,000.00 USD | 0.00 USD | 467,380.00 USD | 164,960.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 75,870.00 USD | 29,290.00 USD | 114,780.00 USD |
| `7D` | `0.2170` | 23,130,000.00 USD | 23,130,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 78,030.00 USD | 30,940.00 USD | 62,940.00 USD |
| `7D` | `0.2180` | 23,660,000.00 USD | 23,660,000.00 USD | 0.00 USD | 271,760.00 USD | 104,030.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 81,570.00 USD | 28,270.00 USD | 33,670.00 USD |
| `7D` | `0.2190` | 24,820,000.00 USD | 24,820,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `1D` | `0.2200` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 85,310.00 USD | 24,670.00 USD | 41,810.00 USD |
| `7D` | `0.2200` | 26,060,000.00 USD | 26,060,000.00 USD | 0.00 USD | 521,790.00 USD | 219,450.00 USD | 493,190.00 USD |
| `1D` | `0.2210` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 40,900.00 USD | 19,080.00 USD | 28,100.00 USD |
| `7D` | `0.2210` | 27,100,000.00 USD | 27,100,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `1D` | `0.2220` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 64,900.00 USD | 8,820.00 USD | 36,120.00 USD |
| `7D` | `0.2220` | 27,580,000.00 USD | 27,580,000.00 USD | 0.00 USD | 198,110.00 USD | 90,610.00 USD | 196,280.00 USD |
| `1D` | `0.2230` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 24,590.00 USD | 8,880.00 USD | 14,940.00 USD |
| `7D` | `0.2230` | 27,860,000.00 USD | 27,860,000.00 USD | 0.00 USD | 139,620.00 USD | 53,210.00 USD | 85,630.00 USD |
| `1D` | `0.2240` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 33,610.00 USD | 14,920.00 USD | 18,760.00 USD |
| `7D` | `0.2240` | 28,600,000.00 USD | 28,600,000.00 USD | 0.00 USD | 378,190.00 USD | 82,090.00 USD | 277,380.00 USD |
| `7D` | `0.2250` | 29,100,000.00 USD | 29,100,000.00 USD | 0.00 USD | 186,370.00 USD | 100,930.00 USD | 212,920.00 USD |
| `1D` | `0.2260` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 61,330.00 USD | 26,650.00 USD | 27,410.00 USD |
| `7D` | `0.2260` | 30,100,000.00 USD | 30,100,000.00 USD | 0.00 USD | 441,450.00 USD | 105,500.00 USD | 452,530.00 USD |
| `7D` | `0.2270` | 30,570,000.00 USD | 30,570,000.00 USD | 0.00 USD | 230,310.00 USD | 64,760.00 USD | 175,420.00 USD |
| `7D` | `0.2280` | 30,940,000.00 USD | 30,940,000.00 USD | 0.00 USD | 105,300.00 USD | 59,020.00 USD | 208,320.00 USD |
| `7D` | `0.2290` | 31,140,000.00 USD | 31,140,000.00 USD | 0.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD |
| `7D` | `0.2300` | 31,250,000.00 USD | 31,250,000.00 USD | 0.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD |
| `7D` | `0.2310` | 31,310,000.00 USD | 31,310,000.00 USD | 0.00 USD | 11,140.00 USD | 13,670.00 USD | 29,340.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `450.39M` | Total OI Tokens: `2,223,279,112.9 ADA`
  * 1h OI Change: `-0.30%` | 4h OI Change: `-2.12%` | 24h OI Change: `-3.54%`
  * Exchange Breakdown: Binance=`84.51M` | Bybit=`53.62M` | OKX=`31.48M` | Hyperliquid=`29.87M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.63K` | Last 24h: `14.21K` | Last 3d: `57.26K` | Last 7d: `58.11K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0030%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0040%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `47.73%` | `52.27%` | `0.91` | 6,740,000.00 USD |
| `15M` | `Binance` | `45.16%` | `54.84%` | `0.82` | 2,060,000.00 USD |
| `15M` | `OKX` | `36.13%` | `63.87%` | `0.57` | 1,450,000.00 USD |
| `15M` | `Bybit` | `43.69%` | `56.31%` | `0.78` | 492,400.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `52.77%` | `47.23%` | `1.12` | 1,200,000.00 USD |
| `15M` | `Bitget` | `47.67%` | `52.33%` | `0.91` | 92,120.00 USD |
| `15M` | `BingX` | `43.04%` | `56.96%` | `0.76` | 188,340.00 USD |
| `15M` | `MEXC` | `78.64%` | `21.36%` | `3.68` | 405,950.00 USD |
| `15M` | `Bitunix` | `45.02%` | `54.98%` | `0.82` | 357,830.00 USD |
| `15M` | `Hyperliquid` | `79.35%` | `20.65%` | `3.84` | 63,710.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.93%` | `50.07%` | `1.00` | 47,410.00 USD |
| `15M` | `Crypto.com` | `57.54%` | `42.46%` | `1.36` | 22,730.00 USD |
| `15M` | `WhiteBIT` | `64.2%` | `35.8%` | `1.79` | 266,450.00 USD |
| `15M` | `HTX` | `72.01%` | `27.99%` | `2.57` | 31,290.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `50.28%` | `49.72%` | `1.01` | 32,910.00 USD |
| `15M` | `Aster` | `43.09%` | `56.91%` | `0.76` | 37,870.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `87.5%` | `12.5%` | `7.00` | 11.39 USD |
| `15M` | `Whale Positions` | `45.16%` | `54.84%` | `0.82` | 2,060,000.00 USD |
| `15M` | `Global Accounts` | `47.73%` | `52.27%` | `0.91` | 6,740,000.00 USD |
| `1H` | `ADA` | `50.42%` | `49.58%` | `1.02` | 44,330,000.00 USD |
| `1H` | `Binance` | `50.04%` | `49.96%` | `1.00` | 14,820,000.00 USD |
| `1H` | `OKX` | `48.28%` | `51.72%` | `0.93` | 7,970,000.00 USD |
| `1H` | `Bybit` | `42.84%` | `57.16%` | `0.75` | 3,950,000.00 USD |
| `1H` | `KuCoin` | `37.99%` | `62.01%` | `0.61` | 278,360.00 USD |
| `1H` | `Gate` | `49.54%` | `50.46%` | `0.98` | 7,490,000.00 USD |
| `1H` | `Bitget` | `50.73%` | `49.27%` | `1.03` | 754,100.00 USD |
| `1H` | `BingX` | `56.65%` | `43.35%` | `1.31` | 1,200,000.00 USD |
| `1H` | `MEXC` | `70.29%` | `29.71%` | `2.37` | 2,820,000.00 USD |
| `1H` | `Bitunix` | `57.8%` | `42.2%` | `1.37` | 2,120,000.00 USD |
| `1H` | `Hyperliquid` | `39.9%` | `60.1%` | `0.66` | 256,150.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.25%` | `48.75%` | `1.05` | 285,100.00 USD |
| `1H` | `Crypto.com` | `56.15%` | `43.85%` | `1.28` | 103,740.00 USD |
| `1H` | `WhiteBIT` | `50.93%` | `49.07%` | `1.04` | 1,410,000.00 USD |
| `1H` | `HTX` | `44.85%` | `55.15%` | `0.81` | 223,750.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.64%` | `55.36%` | `0.81` | 218,460.00 USD |
| `1H` | `Aster` | `19.39%` | `80.61%` | `0.24` | 418,390.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.69%` | `45.31%` | `1.21` | 14,720.00 USD |
| `1H` | `Whale Positions` | `50.04%` | `49.96%` | `1.00` | 14,820,000.00 USD |
| `1H` | `Global Accounts` | `50.42%` | `49.58%` | `1.02` | 44,330,000.00 USD |
| `4H` | `ADA` | `48.83%` | `51.17%` | `0.95` | 155,180,000.00 USD |
| `4H` | `Binance` | `48.9%` | `51.1%` | `0.96` | 100,130,000.00 USD |
| `4H` | `OKX` | `50.04%` | `49.96%` | `1.00` | 9,430,000.00 USD |
| `4H` | `Bybit` | `50.27%` | `49.73%` | `1.01` | 4,660,000.00 USD |
| `4H` | `KuCoin` | `52.21%` | `47.79%` | `1.09` | 805,990.00 USD |
| `4H` | `Gate` | `50.38%` | `49.62%` | `1.02` | 12,970,000.00 USD |
| `4H` | `Bitget` | `44.32%` | `55.68%` | `0.80` | 3,790,000.00 USD |
| `4H` | `BingX` | `36.12%` | `63.88%` | `0.57` | 8,100,000.00 USD |
| `4H` | `MEXC` | `49.9%` | `50.1%` | `1.00` | 2,230,000.00 USD |
| `4H` | `Bitunix` | `46.65%` | `53.35%` | `0.87` | 4,260,000.00 USD |
| `4H` | `Hyperliquid` | `50.33%` | `49.67%` | `1.01` | 1,100,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.65%` | `47.35%` | `1.11` | 3,090,000.00 USD |
| `4H` | `Crypto.com` | `51.09%` | `48.91%` | `1.04` | 0.00 USD |
| `4H` | `WhiteBIT` | `43.75%` | `56.25%` | `0.78` | 841,680.00 USD |
| `4H` | `HTX` | `50.6%` | `49.4%` | `1.02` | 813,500.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.91%` | `56.09%` | `0.78` | 162,150.00 USD |
| `4H` | `Aster` | `41.79%` | `58.21%` | `0.72` | 1,340,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.15%` | `75.85%` | `0.32` | 1,460,000.00 USD |
| `4H` | `Whale Positions` | `48.9%` | `51.1%` | `0.96` | 100,130,000.00 USD |
| `4H` | `Global Accounts` | `48.83%` | `51.17%` | `0.95` | 155,180,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.2047` | `0.2049` | `0.2047` | `0.2056` | `0.2042` | 2,508,493.59 USD | 1,331,643.13 USD | 1,176,850.47 USD | 154,792.66 USD | `+6.17%` | `1B / 1S` |
| `5:00 UTC` | `0.2044` | `0.2044` | `0.2044` | `0.2047` | `0.2041` | 1,406,635.22 USD | 616,800.46 USD | 789,834.77 USD | -173,034.31 USD | `-12.30%` | `0B / 0S` |
| `0:00 UTC` | `0.2049` | `0.2041` | `0.2049` | `0.2051` | `0.2030` | 2,865,852.90 USD | 1,183,037.36 USD | 1,682,815.54 USD | -499,778.19 USD | `-17.44%` | `0B / 2S` |
| `5:00 UTC` | `0.2029` | `0.2028` | `0.2029` | `0.2036` | `0.2021` | 3,754,661.38 USD | 1,656,303.06 USD | 2,098,358.32 USD | -442,055.26 USD | `-11.77%` | `2B / 1S` |
| `0:00 UTC` | `0.2032` | `0.2034` | `0.2032` | `0.2037` | `0.2029` | 1,162,027.09 USD | 658,587.65 USD | 503,439.43 USD | 155,148.22 USD | `+13.35%` | `1B / 0S` |
| `5:00 UTC` | `0.2032` | `0.2031` | `0.2032` | `0.2037` | `0.2025` | 1,133,902.82 USD | 583,524.40 USD | 550,378.43 USD | 33,145.97 USD | `+2.92%` | `0B / 1S` |
| `0:00 UTC` | `0.2022` | `0.2019` | `0.2022` | `0.2026` | `0.2012` | 3,558,066.00 USD | 1,722,575.84 USD | 1,835,490.16 USD | -112,914.31 USD | `-3.17%` | `2B / 3S` |
| `5:00 UTC` | `0.2026` | `0.2024` | `0.2026` | `0.2030` | `0.2016` | 791,895.15 USD | 515,308.00 USD | 276,587.15 USD | 238,720.85 USD | `+30.15%` | `4B / 0S` |
| `0:00 UTC` | `0.2017` | `0.2019` | `0.2017` | `0.2026` | `0.2016` | 936,853.56 USD | 534,839.56 USD | 402,014.00 USD | 132,825.56 USD | `+14.18%` | `1B / 1S` |
| `5:00 UTC` | `0.2021` | `0.2021` | `0.2021` | `0.2026` | `0.2016` | 650,839.93 USD | 328,367.44 USD | 322,472.48 USD | 5,894.96 USD | `+0.91%` | `1B / 0S` |

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
| `5m` | 27,020.00 USD | 23,960.00 USD | **`ACCUMULATION`** |
| `15m` | -91,650.00 USD | 140,370.00 USD | **`ACCUMULATION`** |
| `30m` | 24,680.00 USD | 328,410.00 USD | **`ACCUMULATION`** |
| `1h` | -178,280.00 USD | 207,950.00 USD | **`ACCUMULATION`** |
| `2h` | -599,430.00 USD | -1,330,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -907,970.00 USD | -1,840,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -819,570.00 USD | 1,360,000.00 USD | **`ACCUMULATION`** |
| `8h` | -917,800.00 USD | 1,870,000.00 USD | **`ACCUMULATION`** |
| `12h` | -324,100.00 USD | 4,130,000.00 USD | **`ACCUMULATION`** |
| `24h` | -3,910,000.00 USD | -2,580,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -13,720,000.00 USD | -26,410,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -72,470,000.00 USD | -186,110,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+27.02K` | 15m=`-91.65K` | 1h=`-178.28K` | 24h=`-3.91M`
* Futures Capital Netflows: 5m=`+23.96K` | 15m=`+140.37K` | 1h=`+207.95K` | 24h=`-2.58M`
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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1979` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1932` (Risk Distance: `0.0047` pts)
  * +2.5R Take Profit: `0.2097`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2058` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.2105` (Risk Distance: `0.0047` pts)
  * +2.5R Take Profit: `0.1940`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2036`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
