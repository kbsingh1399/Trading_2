# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:20:14 IST` (`2026-10-29 18:50:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `0.2020` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2034` | Lower -3.00σ Band: `0.2005`
  * Upper +2.51σ Band: `0.2031` | Lower -2.51σ Band: `0.2008`
  * Upper +2.01σ Band: `0.2028` | Lower -2.01σ Band: `0.2011`
  * Upper +2.00σ Band: `0.2028` | Lower -2.00σ Band: `0.2011`
  * Upper +1.28σ Band: `0.2025` | Lower -1.28σ Band: `0.2014`
  * Upper +1.00σ Band: `0.2024` | Lower -1.00σ Band: `0.2015`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2020` | EMA-20=`0.2020` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2020` (Slope: `+0.0000`) | EMA-100=`0.2020`
  * Institutional Anchors: EMA-144=`0.2020` | EMA-200=`0.2020` (Slope: `+0.0000`) | EMA-233=`0.2020`
- **Range Boundaries**: 24H High=`0.2040` | 24H Low=`0.1999` | Weekly High=`0.2060` | Weekly Low=`0.1979`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2058` (Distance: `-1.87%`)
  * Point of Control (POC) = `0.2047` (Distance: `-1.33%`)
  * Value Area Low (VAL) = `0.1978` (Distance: `+2.09%`)
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
| `5m` | `0.2028` | `0.2030` | `0.2024` | `0.2026` | `1,996,464` | 404,532.70 USD | 67,205.39 USD | `+16.61%` | 546,122.81 USD | `+0.59` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.2026` | `0.2026` | `0.2012` | `0.2019` | `9,668,389` | 1,951,373.18 USD | -44,443.78 USD | `-2.28%` | 501,679.03 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.2020` | `0.2020` | `0.2017` | `0.2018` | `310,086` | 62,577.07 USD | -23,759.53 USD | `-37.97%` | 477,919.50 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.2034` | `0.2037` | `0.2028` | `0.2034` | `5,715,568` | 1,162,027.09 USD | 155,148.22 USD | `+13.35%` | 283,135.60 USD | `+0.22` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.2035` | `0.2037` | `0.2024` | `0.2026` | `5,584,820` | 1,133,902.82 USD | 33,145.97 USD | `+2.92%` | 316,281.57 USD | `-0.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.2026` | `0.2026` | `0.2012` | `0.2018` | `9,959,022` | 2,010,024.63 USD | -72,128.92 USD | `-3.59%` | 244,152.65 USD | `-0.42` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.2064` | `0.2087` | `0.2047` | `0.2054` | `58,420,928` | 12,055,112.15 USD | 949,842.55 USD | `+7.88%` | 1,442,489.40 USD | `+0.81` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.2055` | `0.2055` | `0.2021` | `0.2035` | `51,691,771` | 10,535,643.10 USD | -960,075.10 USD | `-9.11%` | 482,414.30 USD | `-0.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.2034` | `0.2037` | `0.2012` | `0.2018` | `21,259,410` | 4,305,954.54 USD | 116,165.27 USD | `+2.70%` | 598,579.57 USD | `+0.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2018` | `131,372,109` | 26,896,709.79 USD | 105,932.72 USD | `+0.39%` | 146,467.30 USD | `+0.03` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2058` | `0.2065` | `0.1954` | `0.1973` | `282,726,861` | 56,231,891.33 USD | -5,955,308.28 USD | `-10.59%` | -3,049,296.45 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -2,508,321.21 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2021` | `139,196,649` | 28,476,927.53 USD | 83,011.23 USD | `+0.29%` | 123,545.80 USD | `+0.02` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `529` | `0x77ee...2902` | `SHORT` | 4,320,552.10 USD | `21,412,192.00` | `0.1911` | `0.2017` | `0.5562` | -229,300.36 USD | `-5.31%` | `10X Cross` |
| `1206` | `0x123d...3bff` | `LONG` | 1,896,475.37 USD | `9,393,142.00` | `0.2912` | `0.2017` | `0.000000` | -839,260.57 USD | `-44.25%` | `10X Cross` |
| `1250` | `0x7737...bf66` | `SHORT` | 1,834,294.18 USD | `9,091,466.00` | `0.2190` | `0.2017` | `2.13` | 156,695.62 USD | `+8.54%` | `10X Cross` |
| `1538` | `0x5f94...4b96` | `SHORT` | 1,446,143.63 USD | `7,162,318.00` | `0.2303` | `0.2017` | `0.7662` | 203,331.57 USD | `+14.06%` | `10X Cross` |
| `1757` | `0x4982...59e6` | `SHORT` | 1,211,999.98 USD | `5,998,812.00` | `0.1891` | `0.2017` | `0.3874` | -77,441.61 USD | `-6.39%` | `10X Cross` |
| `1804` | `0xcac1...26b3` | `LONG` | 1,171,870.90 USD | `5,803,927.00` | `0.2000` | `0.2017` | `0.000000` | 11,055.32 USD | `+0.94%` | `10X Cross` |
| `1989` | `0x51f6...2b39` | `LONG` | 1,022,846.13 USD | `5,065,350.00` | `0.2294` | `0.2017` | `0.000000` | -139,303.46 USD | `-13.62%` | `10X Cross` |
| `1999` | `0xeadc...9d55` | `LONG` | 1,016,547.58 USD | `5,038,400.00` | `0.2195` | `0.2017` | `0.000000` | -89,165.17 USD | `-8.77%` | `10X Cross` |
| `2012` | `0x0748...d4b2` | `SHORT` | 1,009,650.00 USD | `5,000,000.00` | `0.2036` | `0.2017` | `0.6224` | 8,207.24 USD | `+0.81%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2061` | 6,655.44 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.66K USD at 0.2061 USD [API] | `2026-10-27 21:46:03` |
| `ANNOUNCEMENT` | `INFO` | `0.2057` | 6,350.68 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.35K USD at 0.2057 USD [API] | `2026-10-27 21:53:01` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 6,153.52 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2051 USD [API] | `2026-10-27 22:26:18` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 9,856.01 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 9.86K USD at 0.2051 USD [API] | `2026-10-27 22:26:18` |
| `ANNOUNCEMENT` | `INFO` | `0.2050` | 6,533.03 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.53K USD at 0.2050 USD [API] | `2026-10-27 22:28:45` |
| `ANNOUNCEMENT` | `INFO` | `0.2050` | 6,645.28 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2050 USD [API] | `2026-10-27 22:28:45` |
| `ANNOUNCEMENT` | `INFO` | `0.2052` | 6,153.74 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2052 USD [API] | `2026-10-27 22:32:51` |


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
| `Live` | `Long Liquidation` | `0.0435` | 36,680.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 436.50 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,510.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 139.57 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 992.38 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 2,540.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 132,100.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 763.14 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 143.88 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 11,830.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 967.50 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 1,090.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 108.77 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 1,120.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 942.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 2,550.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 931.42 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 1,560.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 4,030.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,140.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 2,970.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,680.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 290.36 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 710.03 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 692.50 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 2,120.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 565.51 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,740.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 13,970.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,500.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 5,720.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 1,800.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 3,600.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 138.14 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 608.32 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 33,400.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 516,140.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 47,860.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 11,580.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 1,580.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 811.91 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 1,740.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 59,350.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 5,900.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,630.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 2,710.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,540.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 518.51 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 35,280.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 864.13 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 3,310.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 1,280.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 622,890.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,110.00 USD | 891,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 3,000.00 USD | 639,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,830.00 USD | 636,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 634,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,720.00 USD | 632,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,750.00 USD | 628,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,750.00 USD | 623,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1780` | 13,700,000.00 USD | 13,700,000.00 USD | 69,630.00 USD | 11,560.00 USD | 62,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 15,790.00 USD | 607,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,550,000.00 USD | 13,550,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 12,760.00 USD | 591,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 134,610.00 USD | 579,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,500,000.00 USD | 13,500,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 444,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 9,970,000.00 USD | 9,970,000.00 USD | 85,420.00 USD | 26,350.00 USD | 54,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 13,330,000.00 USD | 13,330,000.00 USD | 106,790.00 USD | 51,580.00 USD | 118,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,430.00 USD | 436,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 9,800,000.00 USD | 9,800,000.00 USD | 27,490.00 USD | 9,450.00 USD | 14,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 13,050,000.00 USD | 13,050,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 367.00 USD | 418,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 9,750,000.00 USD | 9,750,000.00 USD | 90,980.00 USD | 24,130.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,870,000.00 USD | 12,870,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 956.45 USD | 418,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 9,610,000.00 USD | 9,610,000.00 USD | 164,360.00 USD | 58,710.00 USD | 98,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 12,380,000.00 USD | 12,380,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 4,100.00 USD | 417,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 9,280,000.00 USD | 9,280,000.00 USD | 35,280.00 USD | 8,700.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 11,370,000.00 USD | 11,370,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 5,180.00 USD | 413,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 9,230,000.00 USD | 9,230,000.00 USD | 78,720.00 USD | 14,920.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,980,000.00 USD | 10,980,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 4,120.00 USD | 407,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 9,120,000.00 USD | 9,120,000.00 USD | 215,690.00 USD | 32,270.00 USD | 34,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,730,000.00 USD | 10,730,000.00 USD | 172,850.00 USD | 43,830.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1885` | 9,670.00 USD | 403,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1890` | 8,830,000.00 USD | 8,830,000.00 USD | 101,390.00 USD | 73,060.00 USD | 183,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,470,000.00 USD | 10,470,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 10,260.00 USD | 394,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 8,480,000.00 USD | 8,480,000.00 USD | 250,420.00 USD | 106,080.00 USD | 202,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 10,030,000.00 USD | 10,030,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1905` | 13,110.00 USD | 383,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 7,920,000.00 USD | 7,920,000.00 USD | 229,000.00 USD | 82,620.00 USD | 90,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,480,000.00 USD | 9,480,000.00 USD | 250,530.00 USD | 90,380.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1915` | 27,820.00 USD | 370,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1920` | 7,520,000.00 USD | 7,520,000.00 USD | 484,130.00 USD | 113,980.00 USD | 185,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 9,130,000.00 USD | 9,130,000.00 USD | 279,260.00 USD | 74,890.00 USD | 77,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1925` | 45,730.00 USD | 342,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1930` | 6,730,000.00 USD | 6,730,000.00 USD | 277,060.00 USD | 195,780.00 USD | 462,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,690,000.00 USD | 8,690,000.00 USD | 747,900.00 USD | 173,570.00 USD | 325,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1935` | 290,650.00 USD | 297,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1940` | 5,800,000.00 USD | 5,800,000.00 USD | 625,100.00 USD | 241,260.00 USD | 494,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,450,000.00 USD | 7,450,000.00 USD | 721,210.00 USD | 271,400.00 USD | 825,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1945` | 4,640.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1950` | 4,440,000.00 USD | 4,440,000.00 USD | 481,290.00 USD | 187,790.00 USD | 237,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,630,000.00 USD | 5,630,000.00 USD | 651,390.00 USD | 297,900.00 USD | 389,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1955` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1960` | 3,530,000.00 USD | 3,530,000.00 USD | 472,120.00 USD | 150,290.00 USD | 324,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 4,290,000.00 USD | 4,290,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1970` | 2,580,000.00 USD | 2,580,000.00 USD | 341,720.00 USD | 152,780.00 USD | 270,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 3,420,000.00 USD | 3,420,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1980` | 1,820,000.00 USD | 1,820,000.00 USD | 355,810.00 USD | 92,080.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,780,000.00 USD | 2,780,000.00 USD | 118,660.00 USD | 47,220.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1990` | 1,210,000.00 USD | 1,210,000.00 USD | 123,760.00 USD | 38,070.00 USD | 112,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,590,000.00 USD | 2,590,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2000` | 939,610.00 USD | 939,610.00 USD | 151,770.00 USD | 74,440.00 USD | 146,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 1,310,000.00 USD | 1,310,000.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2010` | 566,980.00 USD | 566,980.00 USD | 312,990.00 USD | 86,290.00 USD | 167,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 1,120,000.00 USD | 1,120,000.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 130,410.00 USD | 130,410.00 USD | 0.00 USD | 53,220.00 USD | 77,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 260,820.00 USD | 260,820.00 USD | 0.00 USD | 53,220.00 USD | 77,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2020` | 510,450.00 USD | 510,450.00 USD | 94,610.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2030` | 543,420.00 USD | 543,420.00 USD | 0.00 USD | 0.00 USD | 282,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 70,990.00 USD | 70,990.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 141,970.00 USD | 141,970.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 830,870.00 USD | 830,870.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 195,660.00 USD | 195,660.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 922,100.00 USD | 922,100.00 USD | 56,660.00 USD | 1,350.00 USD | 33,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 204,270.00 USD | 204,270.00 USD | 0.00 USD | 1,020.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 1,610,000.00 USD | 1,610,000.00 USD | 343,500.00 USD | 144,440.00 USD | 202,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 691,080.00 USD | 691,080.00 USD | 390,170.00 USD | 96,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 2,280,000.00 USD | 2,280,000.00 USD | 492,770.00 USD | 156,970.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 1,330,000.00 USD | 1,330,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 3,340,000.00 USD | 3,340,000.00 USD | 576,980.00 USD | 197,120.00 USD | 285,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 4,220,000.00 USD | 4,220,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 4,720,000.00 USD | 4,720,000.00 USD | 665,470.00 USD | 235,900.00 USD | 477,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 8,210,000.00 USD | 8,210,000.00 USD | 1,690,000.00 USD | 687,470.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 5,180,000.00 USD | 5,180,000.00 USD | 224,390.00 USD | 69,130.00 USD | 169,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 11,310,000.00 USD | 11,310,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 5,750,000.00 USD | 5,750,000.00 USD | 281,860.00 USD | 108,050.00 USD | 177,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 14,300,000.00 USD | 14,300,000.00 USD | 1,160,000.00 USD | 463,080.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2130` | 6,420,000.00 USD | 6,420,000.00 USD | 344,040.00 USD | 107,690.00 USD | 216,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,090,000.00 USD | 17,090,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2135` | 715.44 USD | 715.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2140` | 7,030,000.00 USD | 7,030,000.00 USD | 317,260.00 USD | 104,000.00 USD | 194,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 19,210,000.00 USD | 19,210,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2145` | 331.83 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2150` | 7,180,000.00 USD | 7,180,000.00 USD | 76,110.00 USD | 19,010.00 USD | 57,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 21,460,000.00 USD | 21,460,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 4,300.00 USD | 5,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2160` | 7,370,000.00 USD | 7,370,000.00 USD | 115,640.00 USD | 35,180.00 USD | 39,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 22,490,000.00 USD | 22,490,000.00 USD | 467,380.00 USD | 164,960.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 7,590,000.00 USD | 7,590,000.00 USD | 75,870.00 USD | 29,290.00 USD | 114,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 23,130,000.00 USD | 23,130,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2180` | 7,780,000.00 USD | 7,780,000.00 USD | 89,140.00 USD | 31,250.00 USD | 62,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 23,660,000.00 USD | 23,660,000.00 USD | 271,760.00 USD | 104,030.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 18,910.00 USD | 24,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2190` | 7,920,000.00 USD | 7,920,000.00 USD | 83,610.00 USD | 28,270.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 24,820,000.00 USD | 24,820,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2200` | 8,080,000.00 USD | 8,080,000.00 USD | 85,310.00 USD | 24,670.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,060,000.00 USD | 26,060,000.00 USD | 521,790.00 USD | 219,450.00 USD | 493,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 8,160,000.00 USD | 8,160,000.00 USD | 40,900.00 USD | 17,550.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,100,000.00 USD | 27,100,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 25,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 8,250,000.00 USD | 8,250,000.00 USD | 58,030.00 USD | 8,770.00 USD | 25,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 27,580,000.00 USD | 27,580,000.00 USD | 198,110.00 USD | 90,610.00 USD | 196,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 8,300,000.00 USD | 8,300,000.00 USD | 24,590.00 USD | 8,880.00 USD | 14,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 27,860,000.00 USD | 27,860,000.00 USD | 139,620.00 USD | 53,210.00 USD | 85,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 26,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2240` | 8,410,000.00 USD | 8,410,000.00 USD | 51,290.00 USD | 20,930.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2240` | 28,600,000.00 USD | 28,600,000.00 USD | 378,190.00 USD | 82,090.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,100,000.00 USD | 29,100,000.00 USD | 186,370.00 USD | 100,930.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2260` | 8,530,000.00 USD | 8,530,000.00 USD | 71,770.00 USD | 27,610.00 USD | 27,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,100,000.00 USD | 30,100,000.00 USD | 441,450.00 USD | 105,500.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2270` | 8,690,000.00 USD | 8,690,000.00 USD | 61,490.00 USD | 29,170.00 USD | 67,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2270` | 30,570,000.00 USD | 30,570,000.00 USD | 230,310.00 USD | 64,760.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 28,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2280` | 30,940,000.00 USD | 30,940,000.00 USD | 105,300.00 USD | 59,020.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 37,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,140,000.00 USD | 31,140,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,250,000.00 USD | 31,250,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,310,000.00 USD | 31,310,000.00 USD | 11,140.00 USD | 13,670.00 USD | 29,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 37,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 45,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2345` | 259.83 USD | 45,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2395` | 511.57 USD | 46,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 47,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 743.58 USD | 48,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,370.00 USD | 76,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 77,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 2,030.00 USD | 79,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2765` | 13,830.00 USD | 93,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 93,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 95,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 95,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 99,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 99,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 107,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2965` | 199.54 USD | 107,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 108,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 108,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 155.90 USD | 108,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 97,380.00 USD | 206,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 114.32 USD | 206,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 208,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3315` | 4,480.00 USD | 212,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 1,420.00 USD | 214,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3355` | 87,600.00 USD | 302,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 753.16 USD | 302,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3395` | 2,870.00 USD | 305,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3405` | 243.80 USD | 305,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3455` | 316.13 USD | 306,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 2,370.00 USD | 308,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 26,810.00 USD | 335,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3685` | 147.77 USD | 335,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 344,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 347,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3875` | 2,320,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 788.87 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3925` | 26,120.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3935` | 280.17 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3985` | 287,220.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3995` | 534.53 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4015` | 1,020.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4025` | 6,790.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0435` | 2,550,000.00 USD | 0.00 USD | 36,680.00 USD | `-78.62%` | `843,282.00` |
| `Live` | `Long` | `0.0485` | 2,510,000.00 USD | 0.00 USD | 436.50 USD | `-76.17%` | `9,000.00` |
| `Live` | `Long` | `0.0525` | 2,510,000.00 USD | 0.00 USD | 5,510.00 USD | `-74.20%` | `105,008.00` |
| `Live` | `Long` | `0.0545` | 2,510,000.00 USD | 0.00 USD | 139.57 USD | `-73.22%` | `2,561.00` |
| `Live` | `Long` | `0.0635` | 2,510,000.00 USD | 0.00 USD | 992.38 USD | `-68.80%` | `15,628.00` |
| `Live` | `Long` | `0.0645` | 2,510,000.00 USD | 0.00 USD | 2,540.00 USD | `-68.30%` | `39,410.00` |
| `Live` | `Long` | `0.0705` | 2,500,000.00 USD | 0.00 USD | 132,100.00 USD | `-65.36%` | `1,873,703.00` |
| `Live` | `Long` | `0.0725` | 2,370,000.00 USD | 0.00 USD | 763.14 USD | `-64.37%` | `10,526.00` |
| `Live` | `Long` | `0.0815` | 2,370,000.00 USD | 0.00 USD | 284.84 USD | `-59.95%` | `3,495.00` |
| `Live` | `Long` | `0.0825` | 2,370,000.00 USD | 0.00 USD | 143.88 USD | `-59.46%` | `1,744.00` |
| `Live` | `Long` | `0.0845` | 2,370,000.00 USD | 0.00 USD | 11,830.00 USD | `-58.48%` | `140,000.00` |
| `Live` | `Long` | `0.0865` | 2,360,000.00 USD | 0.00 USD | 967.50 USD | `-57.49%` | `11,185.00` |
| `Live` | `Long` | `0.0875` | 2,360,000.00 USD | 0.00 USD | 1,090.00 USD | `-57.00%` | `12,456.00` |
| `Live` | `Long` | `0.0885` | 2,360,000.00 USD | 0.00 USD | 1,150.00 USD | `-56.51%` | `13,050.00` |
| `Live` | `Long` | `0.0925` | 2,360,000.00 USD | 0.00 USD | 165.11 USD | `-54.55%` | `1,785.00` |
| `Live` | `Long` | `0.0945` | 2,360,000.00 USD | 0.00 USD | 327.54 USD | `-53.56%` | `3,466.00` |
| `Live` | `Long` | `0.1025` | 2,360,000.00 USD | 0.00 USD | 4,100.00 USD | `-49.63%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,350,000.00 USD | 0.00 USD | 1,050.00 USD | `-49.14%` | `10,149.00` |
| `Live` | `Long` | `0.1055` | 2,350,000.00 USD | 0.00 USD | 108.77 USD | `-48.16%` | `1,031.00` |
| `Live` | `Long` | `0.1065` | 2,350,000.00 USD | 0.00 USD | 1,120.00 USD | `-47.67%` | `10,503.00` |
| `Live` | `Long` | `0.1085` | 2,350,000.00 USD | 0.00 USD | 942.00 USD | `-46.68%` | `8,682.00` |
| `Live` | `Long` | `0.1095` | 2,350,000.00 USD | 0.00 USD | 2,550.00 USD | `-46.19%` | `23,247.00` |
| `Live` | `Long` | `0.1145` | 2,350,000.00 USD | 0.00 USD | 862.64 USD | `-43.73%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,340,000.00 USD | 0.00 USD | 13,360.00 USD | `-42.75%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,330,000.00 USD | 0.00 USD | 931.42 USD | `-42.26%` | `7,927.00` |
| `Live` | `Long` | `0.1205` | 2,330,000.00 USD | 0.00 USD | 1,560.00 USD | `-40.79%` | `12,950.00` |
| `Live` | `Long` | `0.1215` | 2,330,000.00 USD | 0.00 USD | 4,030.00 USD | `-40.29%` | `33,159.00` |
| `Live` | `Long` | `0.1245` | 2,320,000.00 USD | 0.00 USD | 404.62 USD | `-38.82%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,320,000.00 USD | 0.00 USD | 2,140.00 USD | `-38.33%` | `17,030.00` |
| `Live` | `Long` | `0.1265` | 2,320,000.00 USD | 0.00 USD | 314.61 USD | `-37.84%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,320,000.00 USD | 0.00 USD | 1,260.00 USD | `-37.35%` | `9,873.00` |
| `Live` | `Long` | `0.1285` | 2,320,000.00 USD | 0.00 USD | 2,970.00 USD | `-36.86%` | `23,117.00` |
| `Live` | `Long` | `0.1295` | 2,320,000.00 USD | 0.00 USD | 2,680.00 USD | `-36.36%` | `20,694.00` |
| `Live` | `Long` | `0.1305` | 2,310,000.00 USD | 0.00 USD | 290.36 USD | `-35.87%` | `2,225.00` |
| `Live` | `Long` | `0.1315` | 2,310,000.00 USD | 0.00 USD | 687.35 USD | `-35.38%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,310,000.00 USD | 0.00 USD | 6,960.00 USD | `-34.89%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,310,000.00 USD | 0.00 USD | 3,600.00 USD | `-34.40%` | `26,965.00` |
| `Live` | `Long` | `0.1345` | 2,300,000.00 USD | 0.00 USD | 710.03 USD | `-33.91%` | `5,279.00` |
| `Live` | `Long` | `0.1355` | 2,300,000.00 USD | 0.00 USD | 106.64 USD | `-33.42%` | `787.00` |
| `Live` | `Long` | `0.1385` | 2,300,000.00 USD | 0.00 USD | 692.50 USD | `-31.94%` | `5,000.00` |
| `Live` | `Long` | `0.1395` | 2,300,000.00 USD | 0.00 USD | 2,120.00 USD | `-31.45%` | `15,162.00` |
| `Live` | `Long` | `0.1405` | 2,300,000.00 USD | 0.00 USD | 565.51 USD | `-30.96%` | `4,025.00` |
| `Live` | `Long` | `0.1415` | 2,300,000.00 USD | 0.00 USD | 9,740.00 USD | `-30.47%` | `68,863.00` |
| `Live` | `Long` | `0.1435` | 2,290,000.00 USD | 0.00 USD | 13,970.00 USD | `-29.48%` | `97,369.00` |
| `Live` | `Long` | `0.1445` | 2,280,000.00 USD | 0.00 USD | 2,500.00 USD | `-28.99%` | `17,302.00` |
| `Live` | `Long` | `0.1455` | 2,270,000.00 USD | 0.00 USD | 5,720.00 USD | `-28.50%` | `39,318.00` |
| `Live` | `Long` | `0.1465` | 2,270,000.00 USD | 0.00 USD | 4,580.00 USD | `-28.01%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,260,000.00 USD | 0.00 USD | 1,800.00 USD | `-27.52%` | `12,201.00` |
| `Live` | `Long` | `0.1485` | 2,260,000.00 USD | 0.00 USD | 3,600.00 USD | `-27.03%` | `24,225.00` |
| `Live` | `Long` | `0.1495` | 2,260,000.00 USD | 0.00 USD | 138.14 USD | `-26.54%` | `924.00` |
| `Live` | `Long` | `0.1505` | 2,260,000.00 USD | 0.00 USD | 608.32 USD | `-26.04%` | `4,042.00` |
| `Live` | `Long` | `0.1515` | 2,260,000.00 USD | 0.00 USD | 33,400.00 USD | `-25.55%` | `220,430.00` |
| `Live` | `Long` | `0.1525` | 2,220,000.00 USD | 0.00 USD | 516,140.00 USD | `-25.06%` | `3,384,521.00` |
| `Live` | `Long` | `0.1535` | 1,710,000.00 USD | 0.00 USD | 47,860.00 USD | `-24.57%` | `311,804.00` |
| `Live` | `Long` | `0.1545` | 1,660,000.00 USD | 0.00 USD | 721.05 USD | `-24.08%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,660,000.00 USD | 0.00 USD | 11,580.00 USD | `-23.59%` | `74,487.00` |
| `Live` | `Long` | `0.1565` | 1,650,000.00 USD | 0.00 USD | 1,580.00 USD | `-23.10%` | `10,116.00` |
| `Live` | `Long` | `0.1575` | 1,650,000.00 USD | 0.00 USD | 811.91 USD | `-22.60%` | `5,155.00` |
| `Live` | `Long` | `0.1585` | 1,640,000.00 USD | 0.00 USD | 6,000.00 USD | `-22.11%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,640,000.00 USD | 0.00 USD | 1,740.00 USD | `-21.62%` | `10,929.00` |
| `Live` | `Long` | `0.1605` | 1,640,000.00 USD | 0.00 USD | 59,350.00 USD | `-21.13%` | `369,768.00` |
| `Live` | `Long` | `0.1615` | 1,580,000.00 USD | 0.00 USD | 5,900.00 USD | `-20.64%` | `36,515.00` |
| `Live` | `Long` | `0.1625` | 1,570,000.00 USD | 0.00 USD | 2,630.00 USD | `-20.15%` | `16,160.00` |
| `Live` | `Long` | `0.1635` | 1,570,000.00 USD | 0.00 USD | 2,710.00 USD | `-19.66%` | `16,600.00` |
| `Live` | `Long` | `0.1645` | 1,570,000.00 USD | 0.00 USD | 10,540.00 USD | `-19.16%` | `64,095.00` |
| `Live` | `Long` | `0.1655` | 1,560,000.00 USD | 0.00 USD | 518.51 USD | `-18.67%` | `3,133.00` |
| `Live` | `Long` | `0.1665` | 1,550,000.00 USD | 0.00 USD | 35,280.00 USD | `-18.18%` | `211,889.00` |
| `Live` | `Long` | `0.1675` | 1,520,000.00 USD | 0.00 USD | 864.13 USD | `-17.69%` | `5,159.00` |
| `Live` | `Long` | `0.1685` | 1,520,000.00 USD | 0.00 USD | 3,310.00 USD | `-17.20%` | `19,635.00` |
| `Live` | `Long` | `0.1695` | 1,520,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.71%` | `7,557.00` |
| `Live` | `Long` | `0.1705` | 1,510,000.00 USD | 0.00 USD | 622,890.00 USD | `-16.22%` | `3,653,343.00` |
| `Live` | `Long` | `0.1715` | 891,200.00 USD | 0.00 USD | 252,110.00 USD | `-15.72%` | `1,470,005.00` |
| `Live` | `Long` | `0.1725` | 639,100.00 USD | 0.00 USD | 3,000.00 USD | `-15.23%` | `17,371.00` |
| `Live` | `Long` | `0.1735` | 636,100.00 USD | 0.00 USD | 1,830.00 USD | `-14.74%` | `10,522.00` |
| `Live` | `Long` | `0.1745` | 634,280.00 USD | 0.00 USD | 1,320.00 USD | `-14.25%` | `7,554.00` |
| `Live` | `Long` | `0.1755` | 632,960.00 USD | 0.00 USD | 4,720.00 USD | `-13.76%` | `26,871.00` |
| `Live` | `Long` | `0.1765` | 628,240.00 USD | 0.00 USD | 4,750.00 USD | `-13.27%` | `26,931.00` |
| `Live` | `Long` | `0.1775` | 623,490.00 USD | 0.00 USD | 15,750.00 USD | `-12.78%` | `88,754.00` |
| `Live` | `Long` | `0.1785` | 607,740.00 USD | 0.00 USD | 15,790.00 USD | `-12.29%` | `88,484.00` |
| `Live` | `Long` | `0.1795` | 591,940.00 USD | 0.00 USD | 12,760.00 USD | `-11.79%` | `71,107.00` |
| `Live` | `Long` | `0.1805` | 579,180.00 USD | 0.00 USD | 134,610.00 USD | `-11.30%` | `745,776.00` |
| `Live` | `Long` | `0.1815` | 444,560.00 USD | 0.00 USD | 7,670.00 USD | `-10.81%` | `42,240.00` |
| `Live` | `Long` | `0.1825` | 436,900.00 USD | 0.00 USD | 18,430.00 USD | `-10.32%` | `100,978.00` |
| `Live` | `Long` | `0.1835` | 418,470.00 USD | 0.00 USD | 367.00 USD | `-9.83%` | `2,000.00` |
| `Live` | `Long` | `0.1845` | 418,100.00 USD | 0.00 USD | 956.45 USD | `-9.34%` | `5,184.00` |
| `Live` | `Long` | `0.1855` | 417,150.00 USD | 0.00 USD | 4,100.00 USD | `-8.85%` | `22,111.00` |
| `Live` | `Long` | `0.1865` | 413,040.00 USD | 0.00 USD | 5,180.00 USD | `-8.35%` | `27,798.00` |
| `Live` | `Long` | `0.1875` | 407,860.00 USD | 0.00 USD | 4,120.00 USD | `-7.86%` | `21,979.00` |
| `Live` | `Long` | `0.1885` | 403,740.00 USD | 0.00 USD | 9,670.00 USD | `-7.37%` | `51,278.00` |
| `Live` | `Long` | `0.1895` | 394,070.00 USD | 0.00 USD | 10,260.00 USD | `-6.88%` | `54,132.00` |
| `Live` | `Long` | `0.1905` | 383,820.00 USD | 0.00 USD | 13,110.00 USD | `-6.39%` | `68,819.00` |
| `Live` | `Long` | `0.1915` | 370,710.00 USD | 0.00 USD | 27,820.00 USD | `-5.90%` | `145,262.00` |
| `Live` | `Long` | `0.1925` | 342,890.00 USD | 0.00 USD | 45,730.00 USD | `-5.41%` | `237,574.00` |
| `Live` | `Long` | `0.1935` | 297,150.00 USD | 0.00 USD | 290,650.00 USD | `-4.91%` | `1,502,046.00` |
| `Live` | `Long` | `0.1945` | 6,510.00 USD | 0.00 USD | 4,640.00 USD | `-4.42%` | `23,844.00` |
| `Live` | `Long` | `0.1955` | 1,870.00 USD | 0.00 USD | 1,870.00 USD | `-3.93%` | `9,570.00` |
| `Live` | `Short` | `0.2135` | 715.44 USD | 715.44 USD | 0.00 USD | `+4.91%` | `3,351.00` |
| `Live` | `Short` | `0.2145` | 1,050.00 USD | 331.83 USD | 0.00 USD | `+5.41%` | `1,547.00` |
| `Live` | `Short` | `0.2155` | 5,340.00 USD | 4,300.00 USD | 0.00 USD | `+5.90%` | `19,938.00` |
| `Live` | `Short` | `0.2185` | 24,250.00 USD | 18,910.00 USD | 0.00 USD | `+7.37%` | `86,525.00` |
| `Live` | `Short` | `0.2215` | 25,890.00 USD | 1,640.00 USD | 0.00 USD | `+8.85%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 26,090.00 USD | 200.48 USD | 0.00 USD | `+9.83%` | `897.00` |
| `Live` | `Short` | `0.2275` | 28,260.00 USD | 2,160.00 USD | 0.00 USD | `+11.79%` | `9,500.00` |
| `Live` | `Short` | `0.2285` | 37,490.00 USD | 9,240.00 USD | 0.00 USD | `+12.29%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 37,780.00 USD | 282.02 USD | 0.00 USD | `+14.25%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 45,410.00 USD | 7,640.00 USD | 0.00 USD | `+14.74%` | `32,708.00` |
| `Live` | `Short` | `0.2345` | 45,670.00 USD | 259.83 USD | 0.00 USD | `+15.23%` | `1,108.00` |
| `Live` | `Short` | `0.2395` | 46,180.00 USD | 511.57 USD | 0.00 USD | `+17.69%` | `2,136.00` |
| `Live` | `Short` | `0.2405` | 47,650.00 USD | 1,470.00 USD | 0.00 USD | `+18.18%` | `6,110.00` |
| `Live` | `Short` | `0.2415` | 48,400.00 USD | 743.58 USD | 0.00 USD | `+18.67%` | `3,079.00` |
| `Live` | `Short` | `0.2525` | 76,770.00 USD | 28,370.00 USD | 0.00 USD | `+24.08%` | `112,352.00` |
| `Live` | `Short` | `0.2585` | 77,150.00 USD | 380.25 USD | 0.00 USD | `+27.03%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 79,180.00 USD | 2,030.00 USD | 0.00 USD | `+28.50%` | `7,759.00` |
| `Live` | `Short` | `0.2765` | 93,000.00 USD | 13,830.00 USD | 0.00 USD | `+35.87%` | `50,000.00` |
| `Live` | `Short` | `0.2775` | 93,380.00 USD | 379.62 USD | 0.00 USD | `+36.36%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 95,550.00 USD | 2,170.00 USD | 0.00 USD | `+39.80%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 95,960.00 USD | 411.09 USD | 0.00 USD | `+42.26%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 99,230.00 USD | 3,260.00 USD | 0.00 USD | `+43.24%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 99,750.00 USD | 519.79 USD | 0.00 USD | `+44.23%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 107,730.00 USD | 7,990.00 USD | 0.00 USD | `+45.21%` | `27,027.00` |
| `Live` | `Short` | `0.2965` | 107,930.00 USD | 199.54 USD | 0.00 USD | `+45.70%` | `673.00` |
| `Live` | `Short` | `0.3005` | 108,080.00 USD | 146.34 USD | 0.00 USD | `+47.67%` | `487.00` |
| `Live` | `Short` | `0.3055` | 108,490.00 USD | 408.15 USD | 0.00 USD | `+50.12%` | `1,336.00` |
| `Live` | `Short` | `0.3075` | 108,640.00 USD | 155.90 USD | 0.00 USD | `+51.11%` | `507.00` |
| `Live` | `Short` | `0.3105` | 206,020.00 USD | 97,380.00 USD | 0.00 USD | `+52.58%` | `313,625.00` |
| `Live` | `Short` | `0.3115` | 206,140.00 USD | 114.32 USD | 0.00 USD | `+53.07%` | `367.00` |
| `Live` | `Short` | `0.3295` | 208,520.00 USD | 2,380.00 USD | 0.00 USD | `+61.92%` | `7,219.00` |
| `Live` | `Short` | `0.3315` | 212,990.00 USD | 4,480.00 USD | 0.00 USD | `+62.90%` | `13,504.00` |
| `Live` | `Short` | `0.3335` | 214,410.00 USD | 1,420.00 USD | 0.00 USD | `+63.88%` | `4,254.00` |
| `Live` | `Short` | `0.3355` | 302,010.00 USD | 87,600.00 USD | 0.00 USD | `+64.86%` | `261,099.00` |
| `Live` | `Short` | `0.3385` | 302,760.00 USD | 753.16 USD | 0.00 USD | `+66.34%` | `2,225.00` |
| `Live` | `Short` | `0.3395` | 305,640.00 USD | 2,870.00 USD | 0.00 USD | `+66.83%` | `8,465.00` |
| `Live` | `Short` | `0.3405` | 305,880.00 USD | 243.80 USD | 0.00 USD | `+67.32%` | `716.00` |
| `Live` | `Short` | `0.3455` | 306,200.00 USD | 316.13 USD | 0.00 USD | `+69.78%` | `915.00` |
| `Live` | `Short` | `0.3485` | 308,570.00 USD | 2,370.00 USD | 0.00 USD | `+71.25%` | `6,797.00` |
| `Live` | `Short` | `0.3625` | 335,380.00 USD | 26,810.00 USD | 0.00 USD | `+78.13%` | `73,959.00` |
| `Live` | `Short` | `0.3685` | 335,530.00 USD | 147.77 USD | 0.00 USD | `+81.08%` | `401.00` |
| `Live` | `Short` | `0.3715` | 344,700.00 USD | 9,170.00 USD | 0.00 USD | `+82.56%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 347,840.00 USD | 3,140.00 USD | 0.00 USD | `+84.03%` | `8,395.00` |
| `Live` | `Short` | `0.3875` | 2,670,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+90.42%` | `5,998,812.00` |
| `Live` | `Short` | `0.3915` | 2,670,000.00 USD | 788.87 USD | 0.00 USD | `+92.38%` | `2,015.00` |
| `Live` | `Short` | `0.3925` | 2,700,000.00 USD | 26,120.00 USD | 0.00 USD | `+92.87%` | `66,555.00` |
| `Live` | `Short` | `0.3935` | 2,700,000.00 USD | 280.17 USD | 0.00 USD | `+93.37%` | `712.00` |
| `Live` | `Short` | `0.3985` | 2,990,000.00 USD | 287,220.00 USD | 0.00 USD | `+95.82%` | `720,753.00` |
| `Live` | `Short` | `0.3995` | 2,990,000.00 USD | 534.53 USD | 0.00 USD | `+96.31%` | `1,338.00` |
| `Live` | `Short` | `0.4015` | 2,990,000.00 USD | 1,020.00 USD | 0.00 USD | `+97.30%` | `2,543.00` |
| `Live` | `Short` | `0.4025` | 3,000,000.00 USD | 6,790.00 USD | 0.00 USD | `+97.79%` | `16,862.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 598,980,000.00 USD | 0.00 USD | 415.13 USD | `-70.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 598,980,000.00 USD | 0.00 USD | 1,100.00 USD | `-45.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 598,980,000.00 USD | 0.00 USD | 541.33 USD | `-45.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 598,980,000.00 USD | 0.00 USD | 602,500.00 USD | `-40.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 598,370,000.00 USD | 0.00 USD | 1,320.00 USD | `-37.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 598,370,000.00 USD | 0.00 USD | 13,390.00 USD | `-35.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 598,360,000.00 USD | 0.00 USD | 728.88 USD | `-34.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 598,360,000.00 USD | 0.00 USD | 4,350.00 USD | `-33.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 598,350,000.00 USD | 0.00 USD | 542.99 USD | `-32.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 598,350,000.00 USD | 0.00 USD | 1,820.00 USD | `-31.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 598,350,000.00 USD | 0.00 USD | 1,050.00 USD | `-30.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 598,350,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 598,350,000.00 USD | 0.00 USD | 1,600.00 USD | `-29.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 598,350,000.00 USD | 0.00 USD | 4,580.00 USD | `-28.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 598,340,000.00 USD | 0.00 USD | 303.26 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 598,340,000.00 USD | 0.00 USD | 1,290.00 USD | `-25.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 598,340,000.00 USD | 0.00 USD | 279.53 USD | `-25.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 598,340,000.00 USD | 0.00 USD | 324.30 USD | `-24.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 598,340,000.00 USD | 0.00 USD | 1,480.00 USD | `-23.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 598,340,000.00 USD | 0.00 USD | 552.21 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 598,340,000.00 USD | 0.00 USD | 166.84 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 598,340,000.00 USD | 0.00 USD | 2,990.00 USD | `-21.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 598,330,000.00 USD | 0.00 USD | 562.67 USD | `-20.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 598,330,000.00 USD | 0.00 USD | 24,760.00 USD | `-20.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 598,310,000.00 USD | 0.00 USD | 6,540.00 USD | `-19.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 598,300,000.00 USD | 0.00 USD | 2,870.00 USD | `-19.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 598,300,000.00 USD | 0.00 USD | 452.97 USD | `-18.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 598,300,000.00 USD | 0.00 USD | 13,930.00 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 598,290,000.00 USD | 0.00 USD | 317.92 USD | `-17.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 598,290,000.00 USD | 0.00 USD | 6,740.00 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 598,280,000.00 USD | 0.00 USD | 4,270.00 USD | `-16.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 598,270,000.00 USD | 0.00 USD | 7,630.00 USD | `-16.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 598,270,000.00 USD | 0.00 USD | 6,860.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 598,260,000.00 USD | 0.00 USD | 6,900.00 USD | `-15.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 598,250,000.00 USD | 0.00 USD | 103.58 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 598,250,000.00 USD | 0.00 USD | 8,220.00 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 598,240,000.00 USD | 0.00 USD | 1,760.00 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 598,240,000.00 USD | 0.00 USD | 623.57 USD | `-13.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 598,240,000.00 USD | 0.00 USD | 4,440.00 USD | `-12.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 598,240,000.00 USD | 0.00 USD | 12,390.00 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 598,230,000.00 USD | 0.00 USD | 5,760.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 598,220,000.00 USD | 0.00 USD | 26,470.00 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 598,190,000.00 USD | 0.00 USD | 2,400.00 USD | `-10.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 598,190,000.00 USD | 0.00 USD | 2,190.00 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 598,190,000.00 USD | 0.00 USD | 3,160.00 USD | `-9.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 598,190,000.00 USD | 0.00 USD | 18,650.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 598,170,000.00 USD | 0.00 USD | 282.33 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 598,170,000.00 USD | 0.00 USD | 218.76 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 598,170,000.00 USD | 0.00 USD | 109.69 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 598,170,000.00 USD | 0.00 USD | 7,390.00 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 598,160,000.00 USD | 0.00 USD | 837.40 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 598,160,000.00 USD | 0.00 USD | 16,100.00 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 598,140,000.00 USD | 0.00 USD | 123.71 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 598,140,000.00 USD | 0.00 USD | 211.37 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 598,140,000.00 USD | 0.00 USD | 2,480.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 598,140,000.00 USD | 0.00 USD | 2,620.00 USD | `-4.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1955` | 598,140,000.00 USD | 0.00 USD | 2,050.00 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1965` | 598,130,000.00 USD | 0.00 USD | 2,380.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1975` | 598,130,000.00 USD | 0.00 USD | 79,010,000.00 USD | `-2.95%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1985` | 519,130,000.00 USD | 0.00 USD | 79,400,000.00 USD | `-2.46%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1995` | 439,720,000.00 USD | 0.00 USD | 319,210,000.00 USD | `-1.97%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2005` | 120,510,000.00 USD | 0.00 USD | 80,200,000.00 USD | `-1.47%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2015` | 40,310,000.00 USD | 0.00 USD | 40,300,000.00 USD | `-0.98%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2025` | 10,120.00 USD | 0.00 USD | 10,120.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 40,700,000.00 USD | 40,700,000.00 USD | 0.00 USD | `+0.00%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2045` | 163,400,000.00 USD | 122,700,000.00 USD | 0.00 USD | `+0.49%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2055` | 245,600,000.00 USD | 82,200,000.00 USD | 0.00 USD | `+0.98%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2065` | 245,610,000.00 USD | 1,260.00 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 245,610,000.00 USD | 8,020.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 245,620,000.00 USD | 2,120.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 245,630,000.00 USD | 8,720.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 245,660,000.00 USD | 34,460.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 245,670,000.00 USD | 12,990.00 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 245,670,000.00 USD | 1,700.00 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 245,680,000.00 USD | 10,740.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 245,690,000.00 USD | 2,460.00 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 245,690,000.00 USD | 2,720.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 245,690,000.00 USD | 109.77 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 245,690,000.00 USD | 109.91 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 245,690,000.00 USD | 584.97 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 245,820,000.00 USD | 125,830.00 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 245,820,000.00 USD | 1,650.00 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 245,820,000.00 USD | 1,690.00 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 245,820,000.00 USD | 501.31 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 245,830,000.00 USD | 6,860.00 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 245,830,000.00 USD | 341.18 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 245,830,000.00 USD | 109.40 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 245,850,000.00 USD | 21,490.00 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 245,860,000.00 USD | 9,140.00 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 245,870,000.00 USD | 9,180.00 USD | 0.00 USD | `+12.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 245,870,000.00 USD | 662.92 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 245,880,000.00 USD | 9,600.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 245,880,000.00 USD | 171.12 USD | 0.00 USD | `+14.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 245,890,000.00 USD | 9,340.00 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 245,890,000.00 USD | 1,010.00 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 245,900,000.00 USD | 9,420.00 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 245,900,000.00 USD | 315.96 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 245,900,000.00 USD | 650.04 USD | 0.00 USD | `+16.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 245,900,000.00 USD | 192.71 USD | 0.00 USD | `+17.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 245,910,000.00 USD | 12,620.00 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 245,910,000.00 USD | 209.72 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 245,910,000.00 USD | 115.92 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 245,920,000.00 USD | 10,930.00 USD | 0.00 USD | `+20.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 245,920,000.00 USD | 288.22 USD | 0.00 USD | `+20.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 245,920,000.00 USD | 491.03 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 245,930,000.00 USD | 1,320.00 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 245,940,000.00 USD | 10,630.00 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 245,940,000.00 USD | 499.00 USD | 0.00 USD | `+22.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 245,940,000.00 USD | 1,100.00 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 245,940,000.00 USD | 168.76 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 245,940,000.00 USD | 603.73 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 245,940,000.00 USD | 2,170.00 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 245,940,000.00 USD | 1,570.00 USD | 0.00 USD | `+26.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 245,940,000.00 USD | 1,470.00 USD | 0.00 USD | `+26.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 245,940,000.00 USD | 271.44 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 246,370,000.00 USD | 421,430.00 USD | 0.00 USD | `+28.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 246,370,000.00 USD | 945.98 USD | 0.00 USD | `+30.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 246,370,000.00 USD | 8,890.00 USD | 0.00 USD | `+31.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 246,390,000.00 USD | 14,860.00 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 246,390,000.00 USD | 3,920.00 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 246,390,000.00 USD | 1,310.00 USD | 0.00 USD | `+33.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 246,410,000.00 USD | 13,870.00 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 246,410,000.00 USD | 4,960.00 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 246,410,000.00 USD | 944.99 USD | 0.00 USD | `+37.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 246,410,000.00 USD | 161.87 USD | 0.00 USD | `+38.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 246,420,000.00 USD | 542.34 USD | 0.00 USD | `+39.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 246,420,000.00 USD | 1,370.00 USD | 0.00 USD | `+39.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 246,420,000.00 USD | 1,080.00 USD | 0.00 USD | `+41.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 246,430,000.00 USD | 15,160.00 USD | 0.00 USD | `+42.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 246,430,000.00 USD | 796.09 USD | 0.00 USD | `+43.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 246,440,000.00 USD | 1,440.00 USD | 0.00 USD | `+46.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 246,440,000.00 USD | 355.21 USD | 0.00 USD | `+47.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 246,440,000.00 USD | 6,950.00 USD | 0.00 USD | `+47.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 246,460,000.00 USD | 18,980.00 USD | 0.00 USD | `+50.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 246,470,000.00 USD | 4,150.00 USD | 0.00 USD | `+51.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 246,470,000.00 USD | 3,250.00 USD | 0.00 USD | `+54.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 246,470,000.00 USD | 5,090.00 USD | 0.00 USD | `+57.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 246,480,000.00 USD | 1,450.00 USD | 0.00 USD | `+59.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 246,480,000.00 USD | 181.30 USD | 0.00 USD | `+59.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 246,480,000.00 USD | 1,380.00 USD | 0.00 USD | `+61.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 246,490,000.00 USD | 12,290.00 USD | 0.00 USD | `+63.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 246,490,000.00 USD | 111.06 USD | 0.00 USD | `+63.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 246,490,000.00 USD | 220.61 USD | 0.00 USD | `+67.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 246,490,000.00 USD | 3,850.00 USD | 0.00 USD | `+71.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 246,490,000.00 USD | 188.75 USD | 0.00 USD | `+85.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 246,490,000.00 USD | 121.76 USD | 0.00 USD | `+86.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 246,490,000.00 USD | 141.78 USD | 0.00 USD | `+91.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3935` | 246,490,000.00 USD | 393.50 USD | 0.00 USD | `+93.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 246,500,000.00 USD | 1,260.00 USD | 0.00 USD | `+93.86%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1780` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 69,630.00 USD | 11,560.00 USD | 62,840.00 USD |
| `7D` | `0.1790` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD |
| `7D` | `0.1800` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `7D` | `0.1810` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 85,420.00 USD | 26,420.00 USD | 61,350.00 USD |
| `7D` | `0.1820` | 13,330,000.00 USD | 0.00 USD | 13,330,000.00 USD | 106,790.00 USD | 51,580.00 USD | 118,390.00 USD |
| `1D` | `0.1830` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 27,490.00 USD | 9,450.00 USD | 14,940.00 USD |
| `7D` | `0.1830` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 82,640.00 USD | 22,630.00 USD | 30,850.00 USD |
| `7D` | `0.1840` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 164,360.00 USD | 58,710.00 USD | 98,820.00 USD |
| `7D` | `0.1850` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 35,280.00 USD | 8,700.00 USD | 14,030.00 USD |
| `7D` | `0.1860` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 78,720.00 USD | 14,920.00 USD | 15,170.00 USD |
| `7D` | `0.1870` | 10,980,000.00 USD | 0.00 USD | 10,980,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 215,690.00 USD | 32,590.00 USD | 34,840.00 USD |
| `7D` | `0.1880` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 172,850.00 USD | 43,830.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 101,390.00 USD | 73,060.00 USD | 183,110.00 USD |
| `7D` | `0.1890` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 248,750.00 USD | 106,080.00 USD | 202,770.00 USD |
| `7D` | `0.1900` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 229,000.00 USD | 83,050.00 USD | 90,970.00 USD |
| `7D` | `0.1910` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 250,530.00 USD | 90,380.00 USD | 16,510.00 USD |
| `1D` | `0.1920` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 484,130.00 USD | 113,980.00 USD | 185,370.00 USD |
| `7D` | `0.1920` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 279,260.00 USD | 74,890.00 USD | 77,590.00 USD |
| `1D` | `0.1930` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 277,060.00 USD | 195,780.00 USD | 462,380.00 USD |
| `7D` | `0.1930` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 747,900.00 USD | 173,570.00 USD | 325,790.00 USD |
| `1D` | `0.1940` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 631,230.00 USD | 241,260.00 USD | 512,850.00 USD |
| `7D` | `0.1940` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 721,210.00 USD | 271,400.00 USD | 825,170.00 USD |
| `1D` | `0.1950` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 481,290.00 USD | 187,790.00 USD | 237,550.00 USD |
| `7D` | `0.1950` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 651,390.00 USD | 297,900.00 USD | 389,660.00 USD |
| `1D` | `0.1960` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 472,120.00 USD | 150,290.00 USD | 324,410.00 USD |
| `7D` | `0.1960` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 341,720.00 USD | 152,780.00 USD | 270,770.00 USD |
| `7D` | `0.1970` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 372,530.00 USD | 92,080.00 USD | 192,410.00 USD |
| `7D` | `0.1980` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 118,660.00 USD | 47,220.00 USD | 23,890.00 USD |
| `1D` | `0.1990` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 123,760.00 USD | 38,070.00 USD | 112,190.00 USD |
| `7D` | `0.1990` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 939,610.00 USD | 0.00 USD | 939,610.00 USD | 151,770.00 USD | 74,440.00 USD | 146,420.00 USD |
| `7D` | `0.2000` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 566,980.00 USD | 0.00 USD | 566,980.00 USD | 312,990.00 USD | 86,290.00 USD | 167,700.00 USD |
| `7D` | `0.2010` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 130,410.00 USD | 130,410.00 USD | 0.00 USD | 0.00 USD | 53,220.00 USD | 77,190.00 USD |
| `1D` | `0.2020` | 260,820.00 USD | 260,820.00 USD | 0.00 USD | 0.00 USD | 53,220.00 USD | 77,190.00 USD |
| `7D` | `0.2020` | 510,450.00 USD | 0.00 USD | 510,450.00 USD | 94,610.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 543,420.00 USD | 543,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 282,600.00 USD |
| `7D` | `0.2030` | 70,990.00 USD | 70,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD |
| `7D` | `0.2030` | 141,970.00 USD | 141,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,990.00 USD |
| `1D` | `0.2040` | 830,870.00 USD | 830,870.00 USD | 0.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD |
| `7D` | `0.2040` | 195,660.00 USD | 195,660.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2060` | 975,620.00 USD | 975,620.00 USD | 0.00 USD | 73,380.00 USD | 1,350.00 USD | 70,020.00 USD |
| `7D` | `0.2060` | 204,270.00 USD | 204,270.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 7,590.00 USD |
| `1D` | `0.2070` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 343,500.00 USD | 144,440.00 USD | 202,190.00 USD |
| `7D` | `0.2070` | 691,080.00 USD | 691,080.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 0.00 USD |
| `1D` | `0.2080` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 492,770.00 USD | 156,970.00 USD | 16,220.00 USD |
| `7D` | `0.2080` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 576,980.00 USD | 197,120.00 USD | 285,880.00 USD |
| `7D` | `0.2090` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 673,830.00 USD | 235,900.00 USD | 496,000.00 USD |
| `7D` | `0.2100` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 1,690,000.00 USD | 687,470.00 USD | 1,610,000.00 USD |
| `1D` | `0.2110` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 224,390.00 USD | 69,550.00 USD | 169,900.00 USD |
| `7D` | `0.2110` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 261,010.00 USD | 104,310.00 USD | 168,670.00 USD |
| `7D` | `0.2120` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 1,160,000.00 USD | 463,080.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 335,320.00 USD | 107,690.00 USD | 208,050.00 USD |
| `7D` | `0.2130` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 315,030.00 USD | 104,320.00 USD | 194,350.00 USD |
| `7D` | `0.2140` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 76,110.00 USD | 19,010.00 USD | 57,150.00 USD |
| `7D` | `0.2150` | 21,460,000.00 USD | 21,460,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `1D` | `0.2160` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 115,640.00 USD | 35,180.00 USD | 39,560.00 USD |
| `7D` | `0.2160` | 22,490,000.00 USD | 22,490,000.00 USD | 0.00 USD | 467,380.00 USD | 164,960.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 75,870.00 USD | 29,290.00 USD | 114,780.00 USD |
| `7D` | `0.2170` | 23,130,000.00 USD | 23,130,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 87,470.00 USD | 31,250.00 USD | 62,940.00 USD |
| `7D` | `0.2180` | 23,660,000.00 USD | 23,660,000.00 USD | 0.00 USD | 271,760.00 USD | 104,030.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 83,610.00 USD | 28,270.00 USD | 33,670.00 USD |
| `7D` | `0.2190` | 24,820,000.00 USD | 24,820,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `1D` | `0.2200` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 85,310.00 USD | 24,670.00 USD | 41,810.00 USD |
| `7D` | `0.2200` | 26,060,000.00 USD | 26,060,000.00 USD | 0.00 USD | 521,790.00 USD | 219,450.00 USD | 493,190.00 USD |
| `1D` | `0.2210` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 40,900.00 USD | 17,620.00 USD | 28,100.00 USD |
| `7D` | `0.2210` | 27,100,000.00 USD | 27,100,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `1D` | `0.2220` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 58,030.00 USD | 8,770.00 USD | 33,250.00 USD |
| `7D` | `0.2220` | 27,580,000.00 USD | 27,580,000.00 USD | 0.00 USD | 198,110.00 USD | 90,610.00 USD | 196,280.00 USD |
| `1D` | `0.2230` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 24,590.00 USD | 8,880.00 USD | 14,940.00 USD |
| `7D` | `0.2230` | 27,860,000.00 USD | 27,860,000.00 USD | 0.00 USD | 139,620.00 USD | 53,210.00 USD | 85,630.00 USD |
| `1D` | `0.2240` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 42,950.00 USD | 19,440.00 USD | 30,850.00 USD |
| `7D` | `0.2240` | 28,600,000.00 USD | 28,600,000.00 USD | 0.00 USD | 378,190.00 USD | 82,090.00 USD | 277,380.00 USD |
| `7D` | `0.2250` | 29,100,000.00 USD | 29,100,000.00 USD | 0.00 USD | 186,370.00 USD | 100,930.00 USD | 212,920.00 USD |
| `1D` | `0.2260` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 71,770.00 USD | 27,610.00 USD | 27,970.00 USD |
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
  * Total Open Interest: `448.42M` | Total OI Tokens: `2,220,733,551.1 ADA`
  * 1h OI Change: `-0.69%` | 4h OI Change: `-2.34%` | 24h OI Change: `-3.68%`
  * Exchange Breakdown: Binance=`84.11M` | Bybit=`53.50M` | OKX=`31.42M` | Hyperliquid=`29.77M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.11K` | Last 24h: `14.21K` | Last 3d: `57.26K` | Last 7d: `58.11K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0043%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0042%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `46.34%` | `53.66%` | `0.86` | 18,220,000.00 USD |
| `15M` | `Binance` | `50.99%` | `49.01%` | `1.04` | 6,530,000.00 USD |
| `15M` | `OKX` | `47.36%` | `52.64%` | `0.90` | 2,740,000.00 USD |
| `15M` | `Bybit` | `41.89%` | `58.11%` | `0.72` | 1,950,000.00 USD |
| `15M` | `KuCoin` | `34.09%` | `65.91%` | `0.52` | 261,340.00 USD |
| `15M` | `Gate` | `59.63%` | `40.37%` | `1.48` | 2,760,000.00 USD |
| `15M` | `Bitget` | `54.55%` | `45.45%` | `1.20` | 364,860.00 USD |
| `15M` | `BingX` | `53.64%` | `46.36%` | `1.16` | 688,010.00 USD |
| `15M` | `MEXC` | `34.83%` | `65.17%` | `0.53` | 1,090,000.00 USD |
| `15M` | `Bitunix` | `48.84%` | `51.16%` | `0.95` | 848,350.00 USD |
| `15M` | `Hyperliquid` | `23.86%` | `76.14%` | `0.31` | 131,280.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `41.87%` | `58.13%` | `0.72` | 142,850.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 33,060.00 USD |
| `15M` | `WhiteBIT` | `10.05%` | `89.95%` | `0.11` | 397,230.00 USD |
| `15M` | `HTX` | `61.51%` | `38.49%` | `1.60` | 30,430.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `42.81%` | `57.19%` | `0.75` | 96,080.00 USD |
| `15M` | `Aster` | `44.04%` | `55.96%` | `0.79` | 135,950.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 12,580.00 USD |
| `15M` | `Whale Positions` | `50.99%` | `49.01%` | `1.04` | 6,530,000.00 USD |
| `15M` | `Global Accounts` | `46.34%` | `53.66%` | `0.86` | 18,220,000.00 USD |
| `1H` | `ADA` | `47.61%` | `52.39%` | `0.91` | 60,880,000.00 USD |
| `1H` | `Binance` | `49.48%` | `50.52%` | `0.98` | 21,800,000.00 USD |
| `1H` | `OKX` | `48.61%` | `51.39%` | `0.95` | 12,430,000.00 USD |
| `1H` | `Bybit` | `42.31%` | `57.69%` | `0.73` | 5,220,000.00 USD |
| `1H` | `KuCoin` | `38.81%` | `61.19%` | `0.63` | 398,120.00 USD |
| `1H` | `Gate` | `60%` | `40%` | `1.50` | 9,410,000.00 USD |
| `1H` | `Bitget` | `55.28%` | `44.72%` | `1.24` | 992,610.00 USD |
| `1H` | `BingX` | `45.39%` | `54.61%` | `0.83` | 1,760,000.00 USD |
| `1H` | `MEXC` | `43.21%` | `56.79%` | `0.76` | 3,370,000.00 USD |
| `1H` | `Bitunix` | `59.99%` | `40.01%` | `1.50` | 2,670,000.00 USD |
| `1H` | `Hyperliquid` | `30.87%` | `69.13%` | `0.45` | 277,660.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.68%` | `55.32%` | `0.81` | 341,540.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 101,930.00 USD |
| `1H` | `WhiteBIT` | `7.11%` | `92.89%` | `0.08` | 1,390,000.00 USD |
| `1H` | `HTX` | `61.72%` | `38.28%` | `1.61` | 121,630.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `62.86%` | `37.14%` | `1.69` | 237,360.00 USD |
| `1H` | `Aster` | `76.51%` | `23.49%` | `3.26` | 327,270.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.74%` | `53.26%` | `0.88` | 27,400.00 USD |
| `1H` | `Whale Positions` | `49.48%` | `50.52%` | `0.98` | 21,800,000.00 USD |
| `1H` | `Global Accounts` | `47.61%` | `52.39%` | `0.91` | 60,880,000.00 USD |
| `4H` | `ADA` | `48.78%` | `51.22%` | `0.95` | 323,390,000.00 USD |
| `4H` | `Binance` | `49.24%` | `50.76%` | `0.97` | 117,330,000.00 USD |
| `4H` | `OKX` | `49.37%` | `50.63%` | `0.98` | 68,380,000.00 USD |
| `4H` | `Bybit` | `49.81%` | `50.19%` | `0.99` | 24,300,000.00 USD |
| `4H` | `KuCoin` | `50.96%` | `49.04%` | `1.04` | 1,840,000.00 USD |
| `4H` | `Gate` | `50.27%` | `49.73%` | `1.01` | 44,470,000.00 USD |
| `4H` | `Bitget` | `43.39%` | `56.61%` | `0.77` | 7,320,000.00 USD |
| `4H` | `BingX` | `37.76%` | `62.24%` | `0.61` | 9,220,000.00 USD |
| `4H` | `MEXC` | `50.23%` | `49.77%` | `1.01` | 23,970,000.00 USD |
| `4H` | `Bitunix` | `44.84%` | `55.16%` | `0.81` | 10,480,000.00 USD |
| `4H` | `Hyperliquid` | `51.89%` | `48.11%` | `1.08` | 3,120,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.91%` | `48.09%` | `1.08` | 1,400,000.00 USD |
| `4H` | `Crypto.com` | `50.56%` | `49.44%` | `1.02` | 392,780.00 USD |
| `4H` | `WhiteBIT` | `41.15%` | `58.85%` | `0.70` | 5,740,000.00 USD |
| `4H` | `HTX` | `50.67%` | `49.33%` | `1.03` | 1,300,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.11%` | `55.89%` | `0.79` | 1,410,000.00 USD |
| `4H` | `Aster` | `46.23%` | `53.77%` | `0.86` | 2,580,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.85%` | `75.15%` | `0.33` | 125,670.00 USD |
| `4H` | `Whale Positions` | `49.24%` | `50.76%` | `0.97` | 117,330,000.00 USD |
| `4H` | `Global Accounts` | `48.78%` | `51.22%` | `0.95` | 323,390,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.2061` | `0.2060` | `0.2061` | `0.2072` | `0.2054` | 2,545,595.94 USD | 1,190,541.20 USD | 1,355,054.75 USD | -164,513.55 USD | `-6.46%` | `0B / 1S` |
| `0:00 UTC` | `0.2052` | `0.2054` | `0.2052` | `0.2061` | `0.2047` | 2,681,797.52 USD | 1,504,963.17 USD | 1,176,834.35 USD | 328,128.82 USD | `+12.24%` | `2B / 1S` |
| `5:00 UTC` | `0.2054` | `0.2054` | `0.2054` | `0.2059` | `0.2051` | 1,103,361.90 USD | 582,275.03 USD | 521,086.87 USD | 61,188.16 USD | `+5.55%` | `1B / 1S` |
| `0:00 UTC` | `0.2047` | `0.2049` | `0.2047` | `0.2056` | `0.2042` | 2,508,493.59 USD | 1,331,643.13 USD | 1,176,850.47 USD | 154,792.66 USD | `+6.17%` | `1B / 1S` |
| `5:00 UTC` | `0.2044` | `0.2044` | `0.2044` | `0.2047` | `0.2041` | 1,406,635.22 USD | 616,800.46 USD | 789,834.77 USD | -173,034.31 USD | `-12.30%` | `0B / 0S` |
| `0:00 UTC` | `0.2049` | `0.2041` | `0.2049` | `0.2051` | `0.2030` | 2,865,852.90 USD | 1,183,037.36 USD | 1,682,815.54 USD | -499,778.19 USD | `-17.44%` | `0B / 2S` |
| `5:00 UTC` | `0.2029` | `0.2028` | `0.2029` | `0.2036` | `0.2021` | 3,754,661.38 USD | 1,656,303.06 USD | 2,098,358.32 USD | -442,055.26 USD | `-11.77%` | `2B / 1S` |
| `0:00 UTC` | `0.2032` | `0.2034` | `0.2032` | `0.2037` | `0.2029` | 1,162,027.09 USD | 658,587.65 USD | 503,439.43 USD | 155,148.22 USD | `+13.35%` | `1B / 0S` |
| `5:00 UTC` | `0.2032` | `0.2031` | `0.2032` | `0.2037` | `0.2025` | 1,133,902.82 USD | 583,524.40 USD | 550,378.43 USD | 33,145.97 USD | `+2.92%` | `0B / 1S` |
| `0:00 UTC` | `0.2022` | `0.2019` | `0.2022` | `0.2026` | `0.2012` | 3,489,507.06 USD | 1,678,404.42 USD | 1,811,102.64 USD | -132,698.21 USD | `-3.80%` | `2B / 4S` |

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
| `5m` | -53,650.00 USD | -170,310.00 USD | **`DISTRIBUTION`** |
| `15m` | -123,580.00 USD | -409,400.00 USD | **`DISTRIBUTION`** |
| `30m` | -197,070.00 USD | -260,070.00 USD | **`DISTRIBUTION`** |
| `1h` | -484,440.00 USD | -1,220,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -915,680.00 USD | -2,210,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,100,000.00 USD | -2,010,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -937,250.00 USD | 1,140,000.00 USD | **`ACCUMULATION`** |
| `8h` | -749,260.00 USD | 1,620,000.00 USD | **`ACCUMULATION`** |
| `12h` | -439,180.00 USD | 4,190,000.00 USD | **`ACCUMULATION`** |
| `24h` | -3,880,000.00 USD | -3,280,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -13,880,000.00 USD | -26,650,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -72,470,000.00 USD | -188,670,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-53.65K` | 15m=`-123.58K` | 1h=`-484.44K` | 24h=`-3.88M`
* Futures Capital Netflows: 5m=`-170.31K` | 15m=`-409.40K` | 1h=`-1.22M` | 24h=`-3.28M`
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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1978` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.01` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.21`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2058` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.41` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.80`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2036`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
