# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:13:48 IST` (`2026-10-29 22:43:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1917` | **Live Ask Quote**: `0.1939` | **Mid Price**: `0.1928`
- **Spread Points**: `22.00` | **Spread BPS**: `114.11 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1976` | VWAP Z-Score: `-1.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0024` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `31.62` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2115` | Lower -3.00σ Band: `0.1838`
  * Upper +2.51σ Band: `0.2092` | Lower -2.51σ Band: `0.1861`
  * Upper +2.01σ Band: `0.2069` | Lower -2.01σ Band: `0.1884`
  * Upper +2.00σ Band: `0.2069` | Lower -2.00σ Band: `0.1884`
  * Upper +1.28σ Band: `0.2035` | Lower -1.28σ Band: `0.1918`
  * Upper +1.00σ Band: `0.2023` | Lower -1.00σ Band: `0.1930`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1925` | EMA-20=`0.1955` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1982` (Slope: `+0.0000`) | EMA-100=`0.1995`
  * Institutional Anchors: EMA-144=`0.2002` | EMA-200=`0.2009` (Slope: `-0.4539`) | EMA-233=`0.2013`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1862` | Weekly High=`0.2086` | Weekly Low=`0.1862`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1922` (Distance: `+0.41%`)
  * Point of Control (POC) = `0.1912` (Distance: `+0.94%`)
  * Value Area Low (VAL) = `0.1894` (Distance: `+1.90%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2057` | Weekly POC=`0.2031` | Weekly VAL=`0.2005`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1886`
  * London Session (08:00-16:00 UTC): High=`0.1936` | Low=`0.1920`
  * New York Session (13:00-21:00 UTC): High=`0.1940` | Low=`0.1916`
  * Initial Balance (First Hour): IB High=`0.1934` | IB Low=`0.1922`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1920` - `0.1936`
  * Optimal Trade Entry (OTE 0.705): `0.1932`
  * Structural Invalidation Anchor (0.786): `0.1943`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1922` | `0.1932` | `0.1919` | `0.1929` | `6,071,272` | 1,168,998.70 USD | 174,033.25 USD | `+14.89%` | -9,320,012.43 USD | `+0.48` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1930` | `0.1933` | `0.1921` | `0.1921` | `4,857,103` | 936,638.68 USD | -43,955.92 USD | `-4.69%` | -9,363,968.35 USD | `-0.12` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1921` | `0.1932` | `0.1919` | `0.1932` | `4,242,492` | 817,422.55 USD | -78,647.36 USD | `-9.62%` | -9,442,615.70 USD | `-0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1922` | `0.1925` | `0.1894` | `0.1914` | `27,789,540` | 5,311,481.42 USD | -69,875.36 USD | `-1.32%` | -9,539,073.00 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1913` | `0.1933` | `0.1906` | `0.1921` | `19,092,680` | 3,670,150.10 USD | 244,309.98 USD | `+6.66%` | -9,294,763.02 USD | `+0.67` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1921` | `0.1932` | `0.1919` | `0.1932` | `4,293,180` | 827,215.47 USD | -68,870.27 USD | `-8.33%` | -9,363,633.30 USD | `+0.31` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.2022` | `0.2023` | `0.1871` | `0.1904` | `319,583,639` | 61,830,947.38 USD | -6,627,620.80 USD | `-10.72%` | -8,794,465.17 USD | `-3.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1903` | `0.1953` | `0.1897` | `0.1921` | `118,898,936` | 22,899,002.06 USD | -718,669.23 USD | `-3.14%` | -9,513,134.40 USD | `-0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1922` | `0.1933` | `0.1894` | `0.1932` | `51,124,712` | 9,799,054.07 USD | 95,787.26 USD | `+0.98%` | -9,417,347.14 USD | `+0.21` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1933` | `489,658,004` | 94,538,802.03 USD | -7,240,720.08 USD | `-7.66%` | -9,666,664.99 USD | `-1.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -5,414,333.03 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -4,633,383.98 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | -2,865,477.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | -2,425,944.91 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1933` | `489,658,004` | 94,538,802.03 USD | -7,240,720.08 USD | `-7.66%` | -9,666,664.99 USD | `-1.58` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1928`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:05:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `533` | `0x77ee...2902` | `SHORT` | 4,132,553.06 USD | `21,412,192.00` | `0.1911` | `0.1931` | `0.5628` | -41,301.32 USD | `-1.00%` | `10X Cross` |
| `1241` | `0x123d...3bff` | `LONG` | 1,809,588.81 USD | `9,393,142.00` | `0.2912` | `0.1931` | `0.000000` | -926,147.13 USD | `-51.18%` | `10X Cross` |
| `1275` | `0x7737...bf66` | `SHORT` | 1,755,107.51 USD | `9,091,466.00` | `0.2190` | `0.1931` | `2.02` | 235,882.29 USD | `+13.44%` | `10X Cross` |
| `1582` | `0x5f94...4b96` | `SHORT` | 1,380,107.06 USD | `7,162,318.00` | `0.2303` | `0.1931` | `0.7077` | 269,368.14 USD | `+19.52%` | `10X Cross` |
| `1796` | `0x4982...59e6` | `SHORT` | 1,157,170.83 USD | `5,998,812.00` | `0.1891` | `0.1931` | `0.4074` | -22,612.47 USD | `-1.95%` | `10X Cross` |
| `1839` | `0xcac1...26b3` | `LONG` | 1,117,952.42 USD | `5,803,927.00` | `0.2000` | `0.1931` | `0.000000` | -42,863.17 USD | `-3.83%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`0.2100` (Vol: 191,800.00 USD, Dist: `+9.25%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+8.87%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.2138` (Vol: 289,900.00 USD, Dist: `+11.26%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.2130` (Vol: 459,300.00 USD, Dist: `+10.84%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
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
| `1D` | `Long Liquidation` | `0.1700` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 625,360.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,020,000.00 USD | 4,020,000.00 USD | 23,820.00 USD | 962.92 USD | 13,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 501,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 3,980,000.00 USD | 3,980,000.00 USD | 9,810.00 USD | 321.20 USD | 45,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 36,420.00 USD | 248,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 6,070.00 USD | 28,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,430.00 USD | 212,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 3,890,000.00 USD | 3,890,000.00 USD | 1,100.00 USD | 6,690.00 USD | 567.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,440.00 USD | 210,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1750` | 3,880,000.00 USD | 3,880,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 61,110.00 USD | 208,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 3,860,000.00 USD | 3,860,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,990.00 USD | 147,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,770,000.00 USD | 3,770,000.00 USD | 53,230.00 USD | 18,700.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,900.00 USD | 142,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,620,000.00 USD | 3,620,000.00 USD | 63,860.00 USD | 34,290.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 2,480.00 USD | 126,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,460,000.00 USD | 3,460,000.00 USD | 78,700.00 USD | 38,930.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 873.09 USD | 124,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 3,290,000.00 USD | 3,290,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 55,280.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 3,140,000.00 USD | 3,140,000.00 USD | 40,760.00 USD | 23,880.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 12,340.00 USD | 67,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 3,030,000.00 USD | 3,030,000.00 USD | 143,910.00 USD | 14,270.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 47,090.00 USD | 55,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 2,810,000.00 USD | 2,810,000.00 USD | 72,410.00 USD | 24,810.00 USD | 132,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 1,630.00 USD | 8,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 2,580,000.00 USD | 2,580,000.00 USD | 90,620.00 USD | 40,900.00 USD | 122,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,740.00 USD | 6,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 2,320,000.00 USD | 2,320,000.00 USD | 120,260.00 USD | 64,080.00 USD | 182,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 1,960,000.00 USD | 1,960,000.00 USD | 202,510.00 USD | 8,970.00 USD | 88,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 3,740.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 1,660,000.00 USD | 1,660,000.00 USD | 178,050.00 USD | 55,340.00 USD | 276,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 451.69 USD | 451.69 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 1,150,000.00 USD | 1,150,000.00 USD | 249,090.00 USD | 72,510.00 USD | 200,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 624,160.00 USD | 624,160.00 USD | 162,010.00 USD | 123,380.00 USD | 154,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 184,600.00 USD | 184,600.00 USD | 104,350.00 USD | 0.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 37,340.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 723,270.00 USD | 723,270.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 944,540.00 USD | 944,540.00 USD | 139,920.00 USD | 5,450.00 USD | 75,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 1,300,000.00 USD | 1,300,000.00 USD | 96,260.00 USD | 25,730.00 USD | 235,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,740,000.00 USD | 1,740,000.00 USD | 32,060.00 USD | 201,680.00 USD | 207,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 44,160.00 USD | 170,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 2,210,000.00 USD | 2,210,000.00 USD | 166,770.00 USD | 3,990.00 USD | 76,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1990` | 2,520,000.00 USD | 2,520,000.00 USD | 88,240.00 USD | 40,300.00 USD | 184,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2000` | 3,020,000.00 USD | 3,020,000.00 USD | 201,440.00 USD | 25,490.00 USD | 274,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 254.23 USD | 254.23 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 3,560,000.00 USD | 3,560,000.00 USD | 104,220.00 USD | 128,530.00 USD | 302,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 3,780,000.00 USD | 3,780,000.00 USD | 92,140.00 USD | 29,200.00 USD | 107,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 7,530.00 USD | 7,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 4,220,000.00 USD | 4,220,000.00 USD | 74,710.00 USD | 85,020.00 USD | 281,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2035` | 465.40 USD | 8,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2040` | 4,600,000.00 USD | 4,600,000.00 USD | 37,280.00 USD | 211,200.00 USD | 124,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 4,720,000.00 USD | 4,720,000.00 USD | 60,770.00 USD | 26,520.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 5,090,000.00 USD | 5,090,000.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 5,900,000.00 USD | 5,900,000.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 6,600,000.00 USD | 6,600,000.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 7,570,000.00 USD | 7,570,000.00 USD | 505,530.00 USD | 177,920.00 USD | 284,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 8,880,000.00 USD | 8,880,000.00 USD | 730,580.00 USD | 176,050.00 USD | 403,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 9,160,000.00 USD | 9,160,000.00 USD | 136,470.00 USD | 45,260.00 USD | 96,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 9,590,000.00 USD | 9,590,000.00 USD | 194,250.00 USD | 96,800.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 2,580.00 USD | 10,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,950,000.00 USD | 9,950,000.00 USD | 213,030.00 USD | 58,850.00 USD | 87,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 10,370,000.00 USD | 10,370,000.00 USD | 228,800.00 USD | 69,510.00 USD | 121,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 10,410,000.00 USD | 10,410,000.00 USD | 31,260.00 USD | 8,960.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2160` | 10,580,000.00 USD | 10,580,000.00 USD | 91,970.00 USD | 33,400.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 10,740,000.00 USD | 10,740,000.00 USD | 60,130.00 USD | 17,300.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 14,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2180` | 10,860,000.00 USD | 10,860,000.00 USD | 51,680.00 USD | 0.00 USD | 65,900.00 USD | `Tier 1 CEX` |
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
| `1D` | `0.1700` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 0.00 USD | 433.10 USD | 2,510.00 USD |
| `1D` | `0.1710` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 23,820.00 USD | 962.92 USD | 13,300.00 USD |
| `1D` | `0.1720` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 9,810.00 USD | 321.20 USD | 45,510.00 USD |
| `1D` | `0.1730` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 6,070.00 USD | 28,880.00 USD |
| `1D` | `0.1740` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 1,100.00 USD | 6,690.00 USD | 567.36 USD |
| `1D` | `0.1750` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1760` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD |
| `1D` | `0.1770` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 53,230.00 USD | 18,700.00 USD | 79,670.00 USD |
| `1D` | `0.1780` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 63,860.00 USD | 34,290.00 USD | 67,000.00 USD |
| `1D` | `0.1790` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 78,700.00 USD | 38,930.00 USD | 46,170.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 40,760.00 USD | 23,880.00 USD | 44,490.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 143,910.00 USD | 14,270.00 USD | 69,380.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 72,410.00 USD | 24,810.00 USD | 132,830.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 90,620.00 USD | 40,900.00 USD | 122,470.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 120,260.00 USD | 64,080.00 USD | 182,080.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 202,510.00 USD | 8,970.00 USD | 88,350.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 178,050.00 USD | 55,340.00 USD | 276,220.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 249,090.00 USD | 72,510.00 USD | 200,330.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 624,160.00 USD | 0.00 USD | 624,160.00 USD | 162,010.00 USD | 123,380.00 USD | 154,170.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 184,600.00 USD | 0.00 USD | 184,600.00 USD | 104,350.00 USD | 0.00 USD | 42,920.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 37,340.00 USD | 0.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1930` | 723,270.00 USD | 723,270.00 USD | 0.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 944,540.00 USD | 944,540.00 USD | 0.00 USD | 139,920.00 USD | 5,450.00 USD | 75,890.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 96,260.00 USD | 25,730.00 USD | 235,720.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 32,060.00 USD | 201,680.00 USD | 207,420.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 44,160.00 USD | 170,560.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 166,770.00 USD | 3,990.00 USD | 76,170.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 88,240.00 USD | 40,300.00 USD | 184,810.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 201,440.00 USD | 25,490.00 USD | 274,740.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 104,220.00 USD | 128,530.00 USD | 302,380.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 92,140.00 USD | 29,200.00 USD | 107,030.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 74,710.00 USD | 85,020.00 USD | 281,720.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 37,280.00 USD | 211,200.00 USD | 124,890.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 60,770.00 USD | 26,520.00 USD | 33,330.00 USD |
| `1D` | `0.2060` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 505,530.00 USD | 177,920.00 USD | 284,650.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 730,580.00 USD | 176,050.00 USD | 403,620.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 136,470.00 USD | 45,260.00 USD | 96,740.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 194,250.00 USD | 96,800.00 USD | 139,010.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 213,030.00 USD | 58,850.00 USD | 87,590.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 228,800.00 USD | 69,510.00 USD | 121,820.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 31,260.00 USD | 8,960.00 USD | 5,840.00 USD |
| `7D` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `1D` | `0.2160` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 91,970.00 USD | 33,400.00 USD | 44,240.00 USD |
| `7D` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 60,130.00 USD | 17,300.00 USD | 79,670.00 USD |
| `7D` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 10,860,000.00 USD | 10,860,000.00 USD | 0.00 USD | 51,680.00 USD | 0.00 USD | 65,900.00 USD |
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
  * Total Open Interest: `420.26M` | Total OI Tokens: `2,168,418,604.6 ADA`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-6.08%` | 24h OI Change: `-9.20%`
  * Exchange Breakdown: Binance=`76.33M` | Bybit=`51.56M` | OKX=`29.75M` | Hyperliquid=`28.15M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.75K` | Last 24h: `14.20K` | Last 3d: `57.34K` | Last 7d: `58.14K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0055%` | **USDT OKX** | `-0.0057%` |
| **USDT Bybit** | `-0.0012%` | **USDT KuCoin** | `0.0004%` |
| **USDT MEXC** | `0.0056%` | **USDT BingX** | `0.0060%` |
| **USDT Gate** | `-0.0039%` | **USDT Bitget** | `0.0028%` |
| **CoinM Binance** | `-0.0034%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `53.70%` | `46.30%` | `1.16` | 25,810,000.00 USD |
| `15M` | `Binance` | `47.7%` | `52.3%` | `0.91` | 9,600,000.00 USD |
| `15M` | `OKX` | `64.1%` | `35.9%` | `1.79` | 5,270,000.00 USD |
| `15M` | `Bybit` | `50.59%` | `49.41%` | `1.02` | 2,070,000.00 USD |
| `15M` | `KuCoin` | `56.64%` | `43.36%` | `1.31` | 395,690.00 USD |
| `15M` | `Gate` | `48.76%` | `51.24%` | `0.95` | 3,670,000.00 USD |
| `15M` | `Bitget` | `47.48%` | `52.52%` | `0.90` | 610,660.00 USD |
| `15M` | `BingX` | `51.78%` | `48.22%` | `1.07` | 116,100.00 USD |
| `15M` | `MEXC` | `65.14%` | `34.86%` | `1.87` | 2,360,000.00 USD |
| `15M` | `Bitunix` | `52.47%` | `47.53%` | `1.10` | 556,460.00 USD |
| `15M` | `Hyperliquid` | `45.32%` | `54.68%` | `0.83` | 128,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `67.53%` | `32.47%` | `2.08` | 91,300.00 USD |
| `15M` | `Crypto.com` | `44.7%` | `55.3%` | `0.81` | 15,550.00 USD |
| `15M` | `WhiteBIT` | `34.52%` | `65.48%` | `0.53` | 379,780.00 USD |
| `15M` | `HTX` | `83.8%` | `16.2%` | `5.17` | 155,940.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `42.12%` | `57.88%` | `0.73` | 147,180.00 USD |
| `15M` | `Aster` | `91.2%` | `8.8%` | `10.36` | 216,430.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `33.18%` | `66.82%` | `0.50` | 4,290.00 USD |
| `15M` | `Whale Positions` | `47.7%` | `52.3%` | `0.91` | 9,600,000.00 USD |
| `15M` | `Global Accounts` | `53.70%` | `46.30%` | `1.16` | 25,810,000.00 USD |
| `1H` | `ADA` | `54.26%` | `45.74%` | `1.19` | 110,190,000.00 USD |
| `1H` | `Binance` | `56.71%` | `43.29%` | `1.31` | 44,860,000.00 USD |
| `1H` | `OKX` | `55.25%` | `44.75%` | `1.23` | 23,350,000.00 USD |
| `1H` | `Bybit` | `49.46%` | `50.54%` | `0.98` | 7,180,000.00 USD |
| `1H` | `KuCoin` | `43.36%` | `56.64%` | `0.77` | 847,300.00 USD |
| `1H` | `Gate` | `48.9%` | `51.1%` | `0.96` | 13,680,000.00 USD |
| `1H` | `Bitget` | `51.6%` | `48.4%` | `1.07` | 2,970,000.00 USD |
| `1H` | `BingX` | `40.43%` | `59.57%` | `0.68` | 1,330,000.00 USD |
| `1H` | `MEXC` | `57.52%` | `42.48%` | `1.35` | 9,030,000.00 USD |
| `1H` | `Bitunix` | `47.56%` | `52.44%` | `0.91` | 2,790,000.00 USD |
| `1H` | `Hyperliquid` | `37.09%` | `62.91%` | `0.59` | 531,940.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.82%` | `41.18%` | `1.43` | 359,610.00 USD |
| `1H` | `Crypto.com` | `49.88%` | `50.12%` | `1.00` | 79,980.00 USD |
| `1H` | `WhiteBIT` | `58.93%` | `41.07%` | `1.43` | 783,000.00 USD |
| `1H` | `HTX` | `57.7%` | `42.3%` | `1.36` | 791,660.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.62%` | `58.38%` | `0.71` | 428,270.00 USD |
| `1H` | `Aster` | `60.75%` | `39.25%` | `1.55` | 1,130,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `38.85%` | `61.15%` | `0.64` | 45,150.00 USD |
| `1H` | `Whale Positions` | `56.71%` | `43.29%` | `1.31` | 44,860,000.00 USD |
| `1H` | `Global Accounts` | `54.26%` | `45.74%` | `1.19` | 110,190,000.00 USD |
| `4H` | `ADA` | `47.61%` | `52.39%` | `0.91` | 662,930,000.00 USD |
| `4H` | `Binance` | `47.34%` | `52.66%` | `0.90` | 284,140,000.00 USD |
| `4H` | `OKX` | `48.76%` | `51.24%` | `0.95` | 144,740,000.00 USD |
| `4H` | `Bybit` | `45.52%` | `54.48%` | `0.84` | 62,870,000.00 USD |
| `4H` | `KuCoin` | `43.54%` | `56.46%` | `0.77` | 5,440,000.00 USD |
| `4H` | `Gate` | `48.77%` | `51.23%` | `0.95` | 52,330,000.00 USD |
| `4H` | `Bitget` | `39.63%` | `60.37%` | `0.66` | 18,940,000.00 USD |
| `4H` | `BingX` | `50.45%` | `49.55%` | `1.02` | 6,740,000.00 USD |
| `4H` | `MEXC` | `54.71%` | `45.29%` | `1.21` | 34,880,000.00 USD |
| `4H` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 18,300,000.00 USD |
| `4H` | `Hyperliquid` | `48.6%` | `51.4%` | `0.95` | 6,440,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `56.77%` | `43.23%` | `1.31` | 2,630,000.00 USD |
| `4H` | `Crypto.com` | `50.79%` | `49.21%` | `1.03` | 820,230.00 USD |
| `4H` | `WhiteBIT` | `32.51%` | `67.49%` | `0.48` | 7,380,000.00 USD |
| `4H` | `HTX` | `45.9%` | `54.1%` | `0.85` | 5,540,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.18%` | `54.82%` | `0.82` | 2,920,000.00 USD |
| `4H` | `Aster` | `48.37%` | `51.63%` | `0.94` | 8,560,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.22%` | `48.78%` | `1.05` | 256,480.00 USD |
| `4H` | `Whale Positions` | `47.34%` | `52.66%` | `0.90` | 284,140,000.00 USD |
| `4H` | `Global Accounts` | `47.61%` | `52.39%` | `0.91` | 662,930,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1996` | `0.1997` | `0.1996` | `0.2001` | `0.1991` | 2,005,993.91 USD | 876,806.75 USD | 1,129,187.16 USD | -252,380.41 USD | `-12.58%` | `0B / 0S` |
| `0:00 UTC` | `0.1918` | `0.1942` | `0.1918` | `0.2001` | `0.1905` | 24,025,446.30 USD | 10,254,298.46 USD | 13,771,147.84 USD | -3,516,849.37 USD | `-14.64%` | `1B / 19S` |
| `5:00 UTC` | `0.1906` | `0.1904` | `0.1906` | `0.1935` | `0.1871` | 26,316,880.25 USD | 11,827,044.75 USD | 14,489,835.50 USD | -2,662,790.75 USD | `-10.12%` | `1B / 5S` |
| `0:00 UTC` | `0.1903` | `0.1914` | `0.1903` | `0.1931` | `0.1898` | 10,338,146.03 USD | 4,991,420.92 USD | 5,346,725.11 USD | -355,304.19 USD | `-3.44%` | `0B / 1S` |
| `5:00 UTC` | `0.1928` | `0.1937` | `0.1928` | `0.1951` | `0.1923` | 6,583,389.18 USD | 3,089,378.61 USD | 3,494,010.58 USD | -404,631.97 USD | `-6.15%` | `0B / 3S` |
| `0:00 UTC` | `0.1946` | `0.1945` | `0.1946` | `0.1953` | `0.1928` | 3,396,141.31 USD | 1,742,542.34 USD | 1,653,598.97 USD | 88,943.37 USD | `+2.62%` | `1B / 4S` |
| `5:00 UTC` | `0.1928` | `0.1929` | `0.1928` | `0.1938` | `0.1920` | 2,581,325.54 USD | 1,266,824.55 USD | 1,314,500.99 USD | -47,676.44 USD | `-1.85%` | `1B / 2S` |
| `0:00 UTC` | `0.1910` | `0.1912` | `0.1910` | `0.1925` | `0.1895` | 5,311,481.42 USD | 2,620,803.03 USD | 2,690,678.39 USD | -69,875.36 USD | `-1.32%` | `2B / 0S` |
| `5:00 UTC` | `0.1923` | `0.1923` | `0.1923` | `0.1933` | `0.1906` | 3,670,150.10 USD | 1,957,230.04 USD | 1,712,920.06 USD | 244,309.98 USD | `+6.66%` | `3B / 2S` |
| `0:00 UTC` | `0.1930` | `0.1930` | `0.1930` | `0.1938` | `0.1920` | 2,338,324.70 USD | 1,102,542.69 USD | 1,235,782.00 USD | -133,239.31 USD | `-5.70%` | `2B / 1S` |

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
| `5m` | -9,340.00 USD | -36,530.00 USD | **`DISTRIBUTION`** |
| `15m` | -50,700.00 USD | 197,220.00 USD | **`ACCUMULATION`** |
| `30m` | -440,170.00 USD | 467,800.00 USD | **`ACCUMULATION`** |
| `1h` | -813,700.00 USD | 507,070.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,000,000.00 USD | -9,830,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,300,000.00 USD | -10,070,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,360,000.00 USD | -11,980,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,320,000.00 USD | -8,810,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,990,000.00 USD | -8,590,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,680,000.00 USD | -17,260,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -17,730,000.00 USD | -35,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -76,080,000.00 USD | -197,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-9.34K` | 15m=`-50.70K` | 1h=`-813.70K` | 24h=`-8.68M`
* Futures Capital Netflows: 5m=`-36.53K` | 15m=`+197.22K` | 1h=`+507.07K` | 24h=`-17.26M`
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
  * `2026-10-30 03:30:16 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:10:16 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1894` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1833` (Risk Distance: `0.0061` pts)
  * +2.5R Take Profit: `0.2047`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1922` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1983` (Risk Distance: `0.0061` pts)
  * +2.5R Take Profit: `0.1769`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1943`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
