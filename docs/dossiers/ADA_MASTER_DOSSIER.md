# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:51:57 IST` (`2026-10-30 11:21:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1931` | **Live Ask Quote**: `0.1952` | **Mid Price**: `0.1941`
- **Spread Points**: `21.00` | **Spread BPS**: `108.16 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1882` | VWAP Z-Score: `+1.74` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.13` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1980` | Lower -3.00σ Band: `0.1785`
  * Upper +2.51σ Band: `0.1964` | Lower -2.51σ Band: `0.1801`
  * Upper +2.01σ Band: `0.1948` | Lower -2.01σ Band: `0.1817`
  * Upper +2.00σ Band: `0.1947` | Lower -2.00σ Band: `0.1818`
  * Upper +1.28σ Band: `0.1924` | Lower -1.28σ Band: `0.1841`
  * Upper +1.00σ Band: `0.1915` | Lower -1.00σ Band: `0.1850`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1921` | EMA-20=`0.1917` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1920` (Slope: `+0.0000`) | EMA-100=`0.1939`
  * Institutional Anchors: EMA-144=`0.1954` | EMA-200=`0.1970` (Slope: `-0.3559`) | EMA-233=`0.1977`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1939` (Distance: `+0.16%`)
  * Point of Control (POC) = `0.1912` (Distance: `+1.57%`)
  * Value Area Low (VAL) = `0.1877` (Distance: `+3.45%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2065` | Weekly POC=`0.2031` | Weekly VAL=`0.1979`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1942` | Low=`0.1902`
  * New York Session (13:00-21:00 UTC): High=`0.1942` | Low=`0.1912`
  * Initial Balance (First Hour): IB High=`0.1935` | IB Low=`0.1918`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1934` - `0.1949`
  * Optimal Trade Entry (OTE 0.705): `0.1945`
  * Structural Invalidation Anchor (0.786): `0.1957`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1950` | `0.1954` | `0.1945` | `0.1947` | `3,668,718` | 715,468.69 USD | -143,821.83 USD | `-20.10%` | -4,345,807.36 USD | `-1.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1946` | `0.1948` | `0.1943` | `0.1945` | `1,400,796` | 272,552.57 USD | -54,268.99 USD | `-19.91%` | -4,400,076.35 USD | `-0.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1945` | `0.1946` | `0.1943` | `0.1944` | `351,119` | 68,288.71 USD | 6,176.56 USD | `+9.04%` | -4,393,899.78 USD | `-0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1927` | `0.1941` | `0.1926` | `0.1938` | `8,976,737` | 1,737,432.33 USD | 227,430.57 USD | `+13.09%` | -4,598,517.88 USD | `+1.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1938` | `0.1951` | `0.1935` | `0.1950` | `8,429,944` | 1,638,885.40 USD | 396,532.35 USD | `+24.20%` | -4,201,985.53 USD | `+1.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1950` | `0.1954` | `0.1943` | `0.1944` | `5,420,537` | 1,056,291.31 USD | -191,922.42 USD | `-18.17%` | -4,393,907.95 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1924` | `0.1930` | `0.1914` | `0.1926` | `25,331,850` | 4,870,682.84 USD | -212,635.97 USD | `-4.37%` | -4,622,595.77 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1927` | `0.1951` | `0.1924` | `0.1950` | `29,768,670` | 5,758,831.86 USD | 754,053.32 USD | `+13.09%` | -3,868,542.45 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1950` | `0.1954` | `0.1943` | `0.1944` | `5,420,633` | 1,056,309.97 USD | -191,914.25 USD | `-18.17%` | -4,060,456.70 USD | `+0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1954` | `0.1914` | `0.1944` | `86,633,837` | 16,708,835.03 USD | 843,185.00 USD | `+5.05%` | -4,060,456.70 USD | `+0.56` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,207,439.06 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -4,361,461.60 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1954` | `0.1914` | `0.1944` | `86,633,837` | 16,708,835.03 USD | 843,185.00 USD | `+5.05%` | -4,060,456.70 USD | `+0.56` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1941`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `533` | `0x77ee...2902` | `SHORT` | 4,164,671.34 USD | `21,412,192.00` | `0.1911` | `0.1943` | `0.5965` | -73,419.60 USD | `-1.76%` | `10X Cross` |
| `1208` | `0x123d...3bff` | `LONG` | 1,826,725.36 USD | `9,392,870.00` | `0.2912` | `0.1943` | `0.000000` | -908,931.36 USD | `-49.76%` | `10X Cross` |
| `1246` | `0x7737...bf66` | `SHORT` | 1,768,108.31 USD | `9,091,466.00` | `0.2190` | `0.1943` | `2.14` | 222,881.49 USD | `+12.61%` | `10X Cross` |
| `1547` | `0x5f94...4b96` | `SHORT` | 1,392,927.60 USD | `7,162,318.00` | `0.2303` | `0.1943` | `0.7115` | 256,547.59 USD | `+18.42%` | `10X Cross` |
| `1774` | `0x4982...59e6` | `SHORT` | 1,166,768.93 USD | `5,998,812.00` | `0.1891` | `0.1943` | `0.4114` | -32,210.57 USD | `-2.76%` | `10X Cross` |
| `1834` | `0xcac1...26b3` | `LONG` | 1,128,399.49 USD | `5,803,927.00` | `0.2000` | `0.1943` | `0.000000` | -32,416.10 USD | `-2.87%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2044` | 6,153.80 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.15K USD at 0.2044 USD [API] | `2026-10-29 17:38:44` |
| `ANNOUNCEMENT` | `INFO` | `0.2033` | 5,005.57 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.01K USD at 0.2033 USD [API] | `2026-10-29 18:14:46` |
| `ANNOUNCEMENT` | `INFO` | `0.2036` | 5,516.20 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.52K USD at 0.2036 USD [API] | `2026-10-29 18:15:11` |
| `ANNOUNCEMENT` | `INFO` | `0.4935` | 596.18 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.60K USD at 0.4935 USD [API] | `2025-10-10 21:18:23` |
| `ANNOUNCEMENT` | `INFO` | `0.4952` | 7,820.83 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 7.82K USD at 0.4952 USD [API] | `2025-10-10 21:18:23` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2099` (Vol: 189,000.00 USD, Dist: `+8.37%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.50%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+8.03%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.52%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 325,500.00 USD, Dist: `+10.35%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.52%`)
  * 7D Horizon: Short MP=`0.2131` (Vol: 448,200.00 USD, Dist: `+10.03%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--5.44%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0415` | 823.53 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 237.54 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 2,520.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 180.76 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 1,270.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 589.50 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 7,400.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 2,860.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,150.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 209.42 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 150,830.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 935.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 2,220.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 13,370.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 87,280.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 182.25 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 150.44 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 25,200.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 532.08 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 317.55 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 574.60 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 7,090.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,150.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 3,110.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 375.41 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,420.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 529.68 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 10,210.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 5,700.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 403.77 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 731.83 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 2,020.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,540.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 958.46 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,220.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,870.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 4,110.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 1,360.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,720.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,830.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 2,890.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 43,350.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,400.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 539,530.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 157.50 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 166,980.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 3,450.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,580.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 16,800.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,180.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,840.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 18,480.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1660` | 9,390,000.00 USD | 9,390,000.00 USD | 146,290.00 USD | 50,280.00 USD | 147,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1665` | 34,190.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1670` | 9,050,000.00 USD | 9,050,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 1,690.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1680` | 8,940,000.00 USD | 8,940,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1685` | 281.23 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1690` | 8,860,000.00 USD | 8,860,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1695` | 79,290.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1700` | 8,760,000.00 USD | 8,760,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1710` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 396,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1720` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 2,920.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 143,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 9,930,000.00 USD | 9,930,000.00 USD | 115,290.00 USD | 33,150.00 USD | 132,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1730` | 8,610,000.00 USD | 8,610,000.00 USD | 32,310.00 USD | 6,910.00 USD | 82,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 658.61 USD | 110,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 9,640,000.00 USD | 9,640,000.00 USD | 56,600.00 USD | 30,930.00 USD | 33,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1740` | 8,490,000.00 USD | 8,490,000.00 USD | 10,400.00 USD | 29,910.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1750` | 9,520,000.00 USD | 9,520,000.00 USD | 50,990.00 USD | 20,400.00 USD | 46,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1750` | 8,400,000.00 USD | 8,400,000.00 USD | 7,610.00 USD | 6,730.00 USD | 39,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 17,080.00 USD | 109,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 9,410,000.00 USD | 9,410,000.00 USD | 45,460.00 USD | 8,400.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1760` | 8,350,000.00 USD | 8,350,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 47,010.00 USD | 92,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 9,330,000.00 USD | 9,330,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1770` | 8,330,000.00 USD | 8,330,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 45,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 9,020,000.00 USD | 9,020,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1780` | 8,080,000.00 USD | 8,080,000.00 USD | 140,230.00 USD | 13,120.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 44,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 8,890,000.00 USD | 8,890,000.00 USD | 114,060.00 USD | 42,720.00 USD | 86,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 7,870,000.00 USD | 7,870,000.00 USD | 12,380.00 USD | 28,450.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 39,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 8,650,000.00 USD | 8,650,000.00 USD | 724,590.00 USD | 95,980.00 USD | 184,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 7,710,000.00 USD | 7,710,000.00 USD | 469,140.00 USD | 95,830.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 3,050.00 USD | 35,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 7,640,000.00 USD | 7,640,000.00 USD | 151,460.00 USD | 56,740.00 USD | 160,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 7,000,000.00 USD | 7,000,000.00 USD | 356,840.00 USD | 46,600.00 USD | 179,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 20,100.00 USD | 32,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 7,270,000.00 USD | 7,270,000.00 USD | 435,080.00 USD | 95,510.00 USD | 318,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 6,420,000.00 USD | 6,420,000.00 USD | 126,700.00 USD | 63,070.00 USD | 444,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 9,020.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 6,420,000.00 USD | 6,420,000.00 USD | 439,340.00 USD | 45,220.00 USD | 65,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 5,790,000.00 USD | 5,790,000.00 USD | 441,880.00 USD | 47,220.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 1,370.00 USD | 3,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 5,870,000.00 USD | 5,870,000.00 USD | 445,620.00 USD | 111,410.00 USD | 203,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 5,270,000.00 USD | 5,270,000.00 USD | 373,060.00 USD | 64,640.00 USD | 192,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,300.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 5,110,000.00 USD | 5,110,000.00 USD | 154,260.00 USD | 112,070.00 USD | 185,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 4,640,000.00 USD | 4,640,000.00 USD | 76,160.00 USD | 72,320.00 USD | 267,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 4,660,000.00 USD | 4,660,000.00 USD | 171,980.00 USD | 62,190.00 USD | 521,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 4,220,000.00 USD | 4,220,000.00 USD | 70,810.00 USD | 15,200.00 USD | 39,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 3,910,000.00 USD | 3,910,000.00 USD | 85,470.00 USD | 38,000.00 USD | 510,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 4,090,000.00 USD | 4,090,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 3,270,000.00 USD | 3,270,000.00 USD | 359,770.00 USD | 232,260.00 USD | 231,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 3,600,000.00 USD | 3,600,000.00 USD | 325,960.00 USD | 148,540.00 USD | 670,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 2,450,000.00 USD | 2,450,000.00 USD | 410,160.00 USD | 182,950.00 USD | 231,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 2,460,000.00 USD | 2,460,000.00 USD | 562,390.00 USD | 144,640.00 USD | 111,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,620,000.00 USD | 1,620,000.00 USD | 103,950.00 USD | 163,310.00 USD | 481,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 1,640,000.00 USD | 1,640,000.00 USD | 255,740.00 USD | 30,390.00 USD | 284,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 873,930.00 USD | 873,930.00 USD | 688,750.00 USD | 62,290.00 USD | 97,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 1,070,000.00 USD | 1,070,000.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 25,220.00 USD | 25,220.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 516,300.00 USD | 516,300.00 USD | 168,540.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1930` | 14,160.00 USD | 14,160.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 331,360.00 USD | 331,360.00 USD | 0.00 USD | 0.00 USD | 331,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 24,450.00 USD | 24,450.00 USD | 0.00 USD | 356.90 USD | 24,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 48,890.00 USD | 48,890.00 USD | 0.00 USD | 356.90 USD | 24,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 342,910.00 USD | 342,910.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 685,810.00 USD | 685,810.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 463,230.00 USD | 463,230.00 USD | 0.00 USD | 1,890.00 USD | 412,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1950` | 1,570,000.00 USD | 1,570,000.00 USD | 681,420.00 USD | 1,990.00 USD | 203,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,870,000.00 USD | 1,870,000.00 USD | 596,440.00 USD | 255,590.00 USD | 559,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 3,400,000.00 USD | 3,400,000.00 USD | 430,170.00 USD | 158,320.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 104.93 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 2,850,000.00 USD | 2,850,000.00 USD | 288,590.00 USD | 260,510.00 USD | 428,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1970` | 3,990,000.00 USD | 3,990,000.00 USD | 65,930.00 USD | 164,750.00 USD | 354,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 3,980,000.00 USD | 3,980,000.00 USD | 420,330.00 USD | 145,540.00 USD | 560,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1980` | 4,730,000.00 USD | 4,730,000.00 USD | 312,350.00 USD | 44,250.00 USD | 383,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 443.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 4,670,000.00 USD | 4,670,000.00 USD | 251,680.00 USD | 74,740.00 USD | 365,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1990` | 5,040,000.00 USD | 5,040,000.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 696.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 5,610,000.00 USD | 5,610,000.00 USD | 426,270.00 USD | 100,110.00 USD | 417,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2000` | 5,620,000.00 USD | 5,620,000.00 USD | 153,280.00 USD | 61,070.00 USD | 371,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 3,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 6,500,000.00 USD | 6,500,000.00 USD | 255,670.00 USD | 235,120.00 USD | 395,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 6,470,000.00 USD | 6,470,000.00 USD | 361,660.00 USD | 91,810.00 USD | 399,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 3,860.00 USD | 7,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 7,100,000.00 USD | 7,100,000.00 USD | 230,470.00 USD | 94,350.00 USD | 270,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 7,150,000.00 USD | 7,150,000.00 USD | 91,080.00 USD | 52,660.00 USD | 529,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 2,640.00 USD | 9,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 7,490,000.00 USD | 7,490,000.00 USD | 150,500.00 USD | 97,440.00 USD | 149,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 7,420,000.00 USD | 7,420,000.00 USD | 22,590.00 USD | 94,230.00 USD | 153,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 7,780,000.00 USD | 7,780,000.00 USD | 83,570.00 USD | 73,360.00 USD | 132,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 7,560,000.00 USD | 7,560,000.00 USD | 62,650.00 USD | 76,780.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 7,960,000.00 USD | 7,960,000.00 USD | 90,000.00 USD | 32,500.00 USD | 52,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 7,660,000.00 USD | 7,660,000.00 USD | 39,740.00 USD | 1,630.00 USD | 57,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2055` | 617.73 USD | 10,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2060` | 8,400,000.00 USD | 8,400,000.00 USD | 314,030.00 USD | 32,110.00 USD | 92,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 7,850,000.00 USD | 7,850,000.00 USD | 154,800.00 USD | 18,480.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2065` | 214.55 USD | 10,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2070` | 8,860,000.00 USD | 8,860,000.00 USD | 196,560.00 USD | 81,580.00 USD | 181,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 8,470,000.00 USD | 8,470,000.00 USD | 441,660.00 USD | 141,790.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 9,190,000.00 USD | 9,190,000.00 USD | 218,960.00 USD | 70,470.00 USD | 42,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 9,150,000.00 USD | 9,150,000.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 10,060,000.00 USD | 10,060,000.00 USD | 456,020.00 USD | 147,490.00 USD | 273,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 12,100,000.00 USD | 12,100,000.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 10,810,000.00 USD | 10,810,000.00 USD | 448,900.00 USD | 92,790.00 USD | 206,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 16,180,000.00 USD | 16,180,000.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2105` | 218.71 USD | 10,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2110` | 11,140,000.00 USD | 11,140,000.00 USD | 152,340.00 USD | 48,060.00 USD | 129,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 19,400,000.00 USD | 19,400,000.00 USD | 1,090,000.00 USD | 518,310.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 11,560,000.00 USD | 11,560,000.00 USD | 163,120.00 USD | 100,480.00 USD | 158,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 22,450,000.00 USD | 22,450,000.00 USD | 1,170,000.00 USD | 492,740.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 153.21 USD | 10,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 11,960,000.00 USD | 11,960,000.00 USD | 207,060.00 USD | 63,250.00 USD | 120,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 25,290,000.00 USD | 25,290,000.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 12,140,000.00 USD | 12,140,000.00 USD | 125,780.00 USD | 31,360.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 27,390,000.00 USD | 27,390,000.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 12,210,000.00 USD | 12,210,000.00 USD | 45,180.00 USD | 8,240.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 29,650,000.00 USD | 29,650,000.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 467.20 USD | 11,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2160` | 30,630,000.00 USD | 30,630,000.00 USD | 467,380.00 USD | 144,820.00 USD | 370,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2165` | 224.94 USD | 11,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 15,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2185` | 4,300.00 USD | 19,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2205` | 229.10 USD | 20,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2215` | 942.26 USD | 21,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2225` | 462.36 USD | 21,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 21,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 23,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 33,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2315` | 604.45 USD | 33,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 34,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 41,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,670.00 USD | 43,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 680.06 USD | 44,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 45,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 379.11 USD | 45,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 45,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2665` | 411.48 USD | 46,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 1,970.00 USD | 48,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 48,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 1,010.00 USD | 49,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 49,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 51,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 52,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 55,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 221.71 USD | 55,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 56,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 64,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 64,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 131.85 USD | 64,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 65,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 4,170.00 USD | 69,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 98,280.00 USD | 167,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 70,390.00 USD | 237,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3135` | 297.82 USD | 238,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3235` | 782.87 USD | 238,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3245` | 36,810.00 USD | 275,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3255` | 3,730.00 USD | 279,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 281,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 245.23 USD | 282,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 331.22 USD | 282,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,440.00 USD | 283,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 205,850.00 USD | 489,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3585` | 258,390.00 USD | 748,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 2,940.00 USD | 751,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 143.91 USD | 751,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3665` | 490.74 USD | 751,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 37,030.00 USD | 788,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 791,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3785` | 169.19 USD | 792,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3805` | 475.62 USD | 792,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3855` | 980.33 USD | 793,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0415` | 2,460,000.00 USD | 0.00 USD | 823.53 USD | `-78.73%` | `19,844.00` |
| `Live` | `Long` | `0.0445` | 2,450,000.00 USD | 0.00 USD | 237.54 USD | `-77.19%` | `5,338.00` |
| `Live` | `Long` | `0.0495` | 2,450,000.00 USD | 0.00 USD | 2,520.00 USD | `-74.63%` | `50,839.00` |
| `Live` | `Long` | `0.0525` | 2,450,000.00 USD | 0.00 USD | 180.76 USD | `-73.09%` | `3,443.00` |
| `Live` | `Long` | `0.0535` | 2,450,000.00 USD | 0.00 USD | 1,270.00 USD | `-72.58%` | `23,814.00` |
| `Live` | `Long` | `0.0655` | 2,450,000.00 USD | 0.00 USD | 589.50 USD | `-66.43%` | `9,000.00` |
| `Live` | `Long` | `0.0705` | 2,450,000.00 USD | 0.00 USD | 7,400.00 USD | `-63.86%` | `105,008.00` |
| `Live` | `Long` | `0.0725` | 2,440,000.00 USD | 0.00 USD | 2,860.00 USD | `-62.84%` | `39,410.00` |
| `Live` | `Long` | `0.0735` | 2,440,000.00 USD | 0.00 USD | 1,150.00 USD | `-62.33%` | `15,628.00` |
| `Live` | `Long` | `0.0745` | 2,440,000.00 USD | 0.00 USD | 209.42 USD | `-61.81%` | `2,811.00` |
| `Live` | `Long` | `0.0805` | 2,440,000.00 USD | 0.00 USD | 150,830.00 USD | `-58.74%` | `1,873,703.00` |
| `Live` | `Long` | `0.0815` | 2,290,000.00 USD | 0.00 USD | 284.84 USD | `-58.22%` | `3,495.00` |
| `Live` | `Long` | `0.0865` | 2,290,000.00 USD | 0.00 USD | 102.50 USD | `-55.66%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,290,000.00 USD | 0.00 USD | 344.75 USD | `-55.15%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,290,000.00 USD | 0.00 USD | 1,150.00 USD | `-54.64%` | `13,050.00` |
| `Live` | `Long` | `0.0925` | 2,290,000.00 USD | 0.00 USD | 165.11 USD | `-52.59%` | `1,785.00` |
| `Live` | `Long` | `0.0935` | 2,290,000.00 USD | 0.00 USD | 935.00 USD | `-52.07%` | `10,000.00` |
| `Live` | `Long` | `0.0945` | 2,280,000.00 USD | 0.00 USD | 2,220.00 USD | `-51.56%` | `23,466.00` |
| `Live` | `Long` | `0.0955` | 2,280,000.00 USD | 0.00 USD | 13,370.00 USD | `-51.05%` | `140,000.00` |
| `Live` | `Long` | `0.0985` | 2,270,000.00 USD | 0.00 USD | 87,280.00 USD | `-49.51%` | `886,128.00` |
| `Live` | `Long` | `0.1025` | 2,180,000.00 USD | 0.00 USD | 4,100.00 USD | `-47.46%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,180,000.00 USD | 0.00 USD | 1,050.00 USD | `-46.95%` | `10,149.00` |
| `Live` | `Long` | `0.1045` | 2,180,000.00 USD | 0.00 USD | 182.25 USD | `-46.43%` | `1,744.00` |
| `Live` | `Long` | `0.1055` | 2,180,000.00 USD | 0.00 USD | 150.44 USD | `-45.92%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,180,000.00 USD | 0.00 USD | 653.70 USD | `-45.41%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,180,000.00 USD | 0.00 USD | 25,200.00 USD | `-44.90%` | `234,396.00` |
| `Live` | `Long` | `0.1085` | 2,150,000.00 USD | 0.00 USD | 532.08 USD | `-44.38%` | `4,904.00` |
| `Live` | `Long` | `0.1095` | 2,150,000.00 USD | 0.00 USD | 317.55 USD | `-43.87%` | `2,900.00` |
| `Live` | `Long` | `0.1105` | 2,150,000.00 USD | 0.00 USD | 574.60 USD | `-43.36%` | `5,200.00` |
| `Live` | `Long` | `0.1135` | 2,150,000.00 USD | 0.00 USD | 7,090.00 USD | `-41.82%` | `62,484.00` |
| `Live` | `Long` | `0.1145` | 2,140,000.00 USD | 0.00 USD | 862.64 USD | `-41.31%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,140,000.00 USD | 0.00 USD | 13,150.00 USD | `-40.28%` | `112,888.00` |
| `Live` | `Long` | `0.1175` | 2,130,000.00 USD | 0.00 USD | 3,110.00 USD | `-39.77%` | `26,446.00` |
| `Live` | `Long` | `0.1185` | 2,120,000.00 USD | 0.00 USD | 375.41 USD | `-39.26%` | `3,168.00` |
| `Live` | `Long` | `0.1205` | 2,120,000.00 USD | 0.00 USD | 826.27 USD | `-38.23%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,120,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.72%` | `8,652.00` |
| `Live` | `Long` | `0.1245` | 2,120,000.00 USD | 0.00 USD | 404.62 USD | `-36.18%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,120,000.00 USD | 0.00 USD | 2,420.00 USD | `-35.67%` | `19,273.00` |
| `Live` | `Long` | `0.1265` | 2,120,000.00 USD | 0.00 USD | 314.61 USD | `-35.16%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,120,000.00 USD | 0.00 USD | 1,260.00 USD | `-34.65%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,120,000.00 USD | 0.00 USD | 2,540.00 USD | `-33.62%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,120,000.00 USD | 0.00 USD | 13,060.00 USD | `-33.11%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,100,000.00 USD | 0.00 USD | 529.68 USD | `-32.60%` | `4,028.00` |
| `Live` | `Long` | `0.1325` | 2,100,000.00 USD | 0.00 USD | 10,210.00 USD | `-32.08%` | `77,060.00` |
| `Live` | `Long` | `0.1335` | 2,090,000.00 USD | 0.00 USD | 5,700.00 USD | `-31.57%` | `42,702.00` |
| `Live` | `Long` | `0.1355` | 2,090,000.00 USD | 0.00 USD | 106.64 USD | `-30.54%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,090,000.00 USD | 0.00 USD | 403.77 USD | `-30.03%` | `2,958.00` |
| `Live` | `Long` | `0.1385` | 2,090,000.00 USD | 0.00 USD | 731.83 USD | `-29.01%` | `5,284.00` |
| `Live` | `Long` | `0.1405` | 2,080,000.00 USD | 0.00 USD | 2,020.00 USD | `-27.98%` | `14,357.00` |
| `Live` | `Long` | `0.1415` | 2,080,000.00 USD | 0.00 USD | 9,540.00 USD | `-27.47%` | `67,399.00` |
| `Live` | `Long` | `0.1425` | 2,070,000.00 USD | 0.00 USD | 958.46 USD | `-26.96%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,070,000.00 USD | 0.00 USD | 15,780.00 USD | `-26.44%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,060,000.00 USD | 0.00 USD | 2,220.00 USD | `-25.93%` | `15,394.00` |
| `Live` | `Long` | `0.1455` | 2,050,000.00 USD | 0.00 USD | 3,870.00 USD | `-25.42%` | `26,603.00` |
| `Live` | `Long` | `0.1465` | 2,050,000.00 USD | 0.00 USD | 4,580.00 USD | `-24.91%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,050,000.00 USD | 0.00 USD | 4,110.00 USD | `-24.39%` | `27,852.00` |
| `Live` | `Long` | `0.1485` | 2,040,000.00 USD | 0.00 USD | 1,360.00 USD | `-23.88%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 2,040,000.00 USD | 0.00 USD | 427.12 USD | `-23.37%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 2,040,000.00 USD | 0.00 USD | 1,720.00 USD | `-22.86%` | `11,458.00` |
| `Live` | `Long` | `0.1515` | 2,040,000.00 USD | 0.00 USD | 35,830.00 USD | `-22.34%` | `236,501.00` |
| `Live` | `Long` | `0.1525` | 2,000,000.00 USD | 0.00 USD | 2,890.00 USD | `-21.83%` | `18,919.00` |
| `Live` | `Long` | `0.1535` | 2,000,000.00 USD | 0.00 USD | 43,350.00 USD | `-21.32%` | `282,402.00` |
| `Live` | `Long` | `0.1545` | 1,960,000.00 USD | 0.00 USD | 721.05 USD | `-20.81%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,960,000.00 USD | 0.00 USD | 1,400.00 USD | `-20.29%` | `9,004.00` |
| `Live` | `Long` | `0.1565` | 1,950,000.00 USD | 0.00 USD | 539,530.00 USD | `-19.78%` | `3,447,463.00` |
| `Live` | `Long` | `0.1575` | 1,410,000.00 USD | 0.00 USD | 157.50 USD | `-19.27%` | `1,000.00` |
| `Live` | `Long` | `0.1585` | 1,410,000.00 USD | 0.00 USD | 166,980.00 USD | `-18.76%` | `1,053,495.00` |
| `Live` | `Long` | `0.1595` | 1,250,000.00 USD | 0.00 USD | 3,450.00 USD | `-18.24%` | `21,609.00` |
| `Live` | `Long` | `0.1605` | 1,240,000.00 USD | 0.00 USD | 57,580.00 USD | `-17.73%` | `358,740.00` |
| `Live` | `Long` | `0.1615` | 1,190,000.00 USD | 0.00 USD | 16,800.00 USD | `-17.22%` | `104,026.00` |
| `Live` | `Long` | `0.1625` | 1,170,000.00 USD | 0.00 USD | 2,180.00 USD | `-16.71%` | `13,446.00` |
| `Live` | `Long` | `0.1645` | 1,170,000.00 USD | 0.00 USD | 10,840.00 USD | `-15.68%` | `65,896.00` |
| `Live` | `Long` | `0.1655` | 1,160,000.00 USD | 0.00 USD | 18,480.00 USD | `-15.17%` | `111,650.00` |
| `Live` | `Long` | `0.1665` | 1,140,000.00 USD | 0.00 USD | 34,190.00 USD | `-14.65%` | `205,345.00` |
| `Live` | `Long` | `0.1675` | 1,100,000.00 USD | 0.00 USD | 1,690.00 USD | `-14.14%` | `10,103.00` |
| `Live` | `Long` | `0.1685` | 1,100,000.00 USD | 0.00 USD | 281.23 USD | `-13.63%` | `1,669.00` |
| `Live` | `Long` | `0.1695` | 1,100,000.00 USD | 0.00 USD | 79,290.00 USD | `-13.12%` | `467,760.00` |
| `Live` | `Long` | `0.1705` | 1,020,000.00 USD | 0.00 USD | 626,600.00 USD | `-12.60%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 396,140.00 USD | 0.00 USD | 252,270.00 USD | `-12.09%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 143,870.00 USD | 0.00 USD | 33,550.00 USD | `-11.58%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 110,320.00 USD | 0.00 USD | 658.61 USD | `-11.07%` | `3,796.00` |
| `Live` | `Long` | `0.1755` | 109,660.00 USD | 0.00 USD | 17,080.00 USD | `-10.04%` | `97,301.00` |
| `Live` | `Long` | `0.1765` | 92,580.00 USD | 0.00 USD | 47,010.00 USD | `-9.53%` | `266,352.00` |
| `Live` | `Long` | `0.1775` | 45,570.00 USD | 0.00 USD | 1,360.00 USD | `-9.02%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 44,210.00 USD | 0.00 USD | 4,530.00 USD | `-8.50%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 39,690.00 USD | 0.00 USD | 3,840.00 USD | `-7.99%` | `21,396.00` |
| `Live` | `Long` | `0.1805` | 35,850.00 USD | 0.00 USD | 3,050.00 USD | `-7.48%` | `16,904.00` |
| `Live` | `Long` | `0.1815` | 32,790.00 USD | 0.00 USD | 20,100.00 USD | `-6.97%` | `110,749.00` |
| `Live` | `Long` | `0.1825` | 12,690.00 USD | 0.00 USD | 9,020.00 USD | `-6.45%` | `49,427.00` |
| `Live` | `Long` | `0.1835` | 3,670.00 USD | 0.00 USD | 1,370.00 USD | `-5.94%` | `7,489.00` |
| `Live` | `Long` | `0.1845` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | `-5.43%` | `12,457.00` |
| `Live` | `Short` | `0.1965` | 104.93 USD | 104.93 USD | 0.00 USD | `+0.72%` | `534.00` |
| `Live` | `Short` | `0.1985` | 443.57 USD | 338.64 USD | 0.00 USD | `+1.75%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 696.54 USD | 252.97 USD | 0.00 USD | `+2.26%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 3,270.00 USD | 2,570.00 USD | 0.00 USD | `+2.77%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 7,130.00 USD | 3,860.00 USD | 0.00 USD | `+3.29%` | `19,136.00` |
| `Live` | `Short` | `0.2025` | 9,770.00 USD | 2,640.00 USD | 0.00 USD | `+3.80%` | `13,040.00` |
| `Live` | `Short` | `0.2055` | 10,380.00 USD | 617.73 USD | 0.00 USD | `+5.34%` | `3,006.00` |
| `Live` | `Short` | `0.2065` | 10,600.00 USD | 214.55 USD | 0.00 USD | `+5.85%` | `1,039.00` |
| `Live` | `Short` | `0.2105` | 10,820.00 USD | 218.71 USD | 0.00 USD | `+7.90%` | `1,039.00` |
| `Live` | `Short` | `0.2125` | 10,970.00 USD | 153.21 USD | 0.00 USD | `+8.92%` | `721.00` |
| `Live` | `Short` | `0.2155` | 11,440.00 USD | 467.20 USD | 0.00 USD | `+10.46%` | `2,168.00` |
| `Live` | `Short` | `0.2165` | 11,660.00 USD | 224.94 USD | 0.00 USD | `+10.97%` | `1,039.00` |
| `Live` | `Short` | `0.2175` | 15,590.00 USD | 3,930.00 USD | 0.00 USD | `+11.49%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 19,890.00 USD | 4,300.00 USD | 0.00 USD | `+12.00%` | `19,678.00` |
| `Live` | `Short` | `0.2205` | 20,120.00 USD | 229.10 USD | 0.00 USD | `+13.02%` | `1,039.00` |
| `Live` | `Short` | `0.2215` | 21,060.00 USD | 942.26 USD | 0.00 USD | `+13.54%` | `4,254.00` |
| `Live` | `Short` | `0.2225` | 21,530.00 USD | 462.36 USD | 0.00 USD | `+14.05%` | `2,078.00` |
| `Live` | `Short` | `0.2235` | 21,730.00 USD | 200.48 USD | 0.00 USD | `+14.56%` | `897.00` |
| `Live` | `Short` | `0.2265` | 23,960.00 USD | 2,230.00 USD | 0.00 USD | `+16.10%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 33,200.00 USD | 9,240.00 USD | 0.00 USD | `+17.13%` | `40,428.00` |
| `Live` | `Short` | `0.2315` | 33,800.00 USD | 604.45 USD | 0.00 USD | `+18.66%` | `2,611.00` |
| `Live` | `Short` | `0.2325` | 34,080.00 USD | 282.02 USD | 0.00 USD | `+19.18%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 41,720.00 USD | 7,640.00 USD | 0.00 USD | `+19.69%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 43,390.00 USD | 1,670.00 USD | 0.00 USD | `+23.28%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 44,070.00 USD | 680.06 USD | 0.00 USD | `+23.79%` | `2,816.00` |
| `Live` | `Short` | `0.2425` | 45,150.00 USD | 1,080.00 USD | 0.00 USD | `+24.30%` | `4,435.00` |
| `Live` | `Short` | `0.2565` | 45,530.00 USD | 379.11 USD | 0.00 USD | `+31.48%` | `1,478.00` |
| `Live` | `Short` | `0.2585` | 45,910.00 USD | 380.25 USD | 0.00 USD | `+32.50%` | `1,471.00` |
| `Live` | `Short` | `0.2665` | 46,320.00 USD | 411.48 USD | 0.00 USD | `+36.60%` | `1,544.00` |
| `Live` | `Short` | `0.2675` | 48,290.00 USD | 1,970.00 USD | 0.00 USD | `+37.12%` | `7,372.00` |
| `Live` | `Short` | `0.2715` | 48,410.00 USD | 120.00 USD | 0.00 USD | `+39.17%` | `442.00` |
| `Live` | `Short` | `0.2725` | 49,420.00 USD | 1,010.00 USD | 0.00 USD | `+39.68%` | `3,713.00` |
| `Live` | `Short` | `0.2775` | 49,800.00 USD | 379.62 USD | 0.00 USD | `+42.24%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 51,980.00 USD | 2,170.00 USD | 0.00 USD | `+45.83%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 52,390.00 USD | 411.09 USD | 0.00 USD | `+48.39%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 55,650.00 USD | 3,260.00 USD | 0.00 USD | `+49.42%` | `11,194.00` |
| `Live` | `Short` | `0.2925` | 55,870.00 USD | 221.71 USD | 0.00 USD | `+49.93%` | `758.00` |
| `Live` | `Short` | `0.2935` | 56,390.00 USD | 519.79 USD | 0.00 USD | `+50.44%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 64,380.00 USD | 7,990.00 USD | 0.00 USD | `+51.47%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 64,520.00 USD | 146.34 USD | 0.00 USD | `+54.03%` | `487.00` |
| `Live` | `Short` | `0.3045` | 64,660.00 USD | 131.85 USD | 0.00 USD | `+56.08%` | `433.00` |
| `Live` | `Short` | `0.3055` | 65,060.00 USD | 408.15 USD | 0.00 USD | `+56.59%` | `1,336.00` |
| `Live` | `Short` | `0.3085` | 69,230.00 USD | 4,170.00 USD | 0.00 USD | `+58.13%` | `13,504.00` |
| `Live` | `Short` | `0.3115` | 167,520.00 USD | 98,280.00 USD | 0.00 USD | `+59.67%` | `315,521.00` |
| `Live` | `Short` | `0.3125` | 237,900.00 USD | 70,390.00 USD | 0.00 USD | `+60.18%` | `225,244.00` |
| `Live` | `Short` | `0.3135` | 238,200.00 USD | 297.82 USD | 0.00 USD | `+60.70%` | `950.00` |
| `Live` | `Short` | `0.3235` | 238,990.00 USD | 782.87 USD | 0.00 USD | `+65.82%` | `2,420.00` |
| `Live` | `Short` | `0.3245` | 275,790.00 USD | 36,810.00 USD | 0.00 USD | `+66.33%` | `113,421.00` |
| `Live` | `Short` | `0.3255` | 279,520.00 USD | 3,730.00 USD | 0.00 USD | `+66.85%` | `11,458.00` |
| `Live` | `Short` | `0.3295` | 281,900.00 USD | 2,380.00 USD | 0.00 USD | `+68.90%` | `7,219.00` |
| `Live` | `Short` | `0.3425` | 282,140.00 USD | 245.23 USD | 0.00 USD | `+75.56%` | `716.00` |
| `Live` | `Short` | `0.3505` | 282,470.00 USD | 331.22 USD | 0.00 USD | `+79.66%` | `945.00` |
| `Live` | `Short` | `0.3515` | 283,920.00 USD | 1,440.00 USD | 0.00 USD | `+80.17%` | `4,102.00` |
| `Live` | `Short` | `0.3575` | 489,770.00 USD | 205,850.00 USD | 0.00 USD | `+83.25%` | `575,809.00` |
| `Live` | `Short` | `0.3585` | 748,160.00 USD | 258,390.00 USD | 0.00 USD | `+83.76%` | `720,753.00` |
| `Live` | `Short` | `0.3615` | 751,100.00 USD | 2,940.00 USD | 0.00 USD | `+85.30%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 751,240.00 USD | 143.91 USD | 0.00 USD | `+85.81%` | `397.00` |
| `Live` | `Short` | `0.3665` | 751,730.00 USD | 490.74 USD | 0.00 USD | `+87.86%` | `1,339.00` |
| `Live` | `Short` | `0.3715` | 788,770.00 USD | 37,030.00 USD | 0.00 USD | `+90.42%` | `99,689.00` |
| `Live` | `Short` | `0.3745` | 791,910.00 USD | 3,140.00 USD | 0.00 USD | `+91.96%` | `8,395.00` |
| `Live` | `Short` | `0.3785` | 792,080.00 USD | 169.19 USD | 0.00 USD | `+94.01%` | `447.00` |
| `Live` | `Short` | `0.3805` | 792,560.00 USD | 475.62 USD | 0.00 USD | `+95.04%` | `1,250.00` |
| `Live` | `Short` | `0.3855` | 793,540.00 USD | 980.33 USD | 0.00 USD | `+97.60%` | `2,543.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 110,720,000.00 USD | 0.00 USD | 415.13 USD | `-69.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 110,720,000.00 USD | 0.00 USD | 438.99 USD | `-68.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 110,720,000.00 USD | 0.00 USD | 1,100.00 USD | `-43.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 110,720,000.00 USD | 0.00 USD | 541.33 USD | `-42.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 110,720,000.00 USD | 0.00 USD | 429.20 USD | `-40.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 110,720,000.00 USD | 0.00 USD | 602,500.00 USD | `-38.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 110,120,000.00 USD | 0.00 USD | 4,460.00 USD | `-36.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 110,110,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 110,110,000.00 USD | 0.00 USD | 13,390.00 USD | `-33.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 110,100,000.00 USD | 0.00 USD | 728.88 USD | `-32.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 110,100,000.00 USD | 0.00 USD | 4,350.00 USD | `-31.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 110,090,000.00 USD | 0.00 USD | 4,730.00 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 110,090,000.00 USD | 0.00 USD | 1,820.00 USD | `-28.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 110,080,000.00 USD | 0.00 USD | 1,050.00 USD | `-27.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 110,080,000.00 USD | 0.00 USD | 351.26 USD | `-26.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 110,080,000.00 USD | 0.00 USD | 1,600.00 USD | `-26.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 110,080,000.00 USD | 0.00 USD | 10,400.00 USD | `-25.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 110,070,000.00 USD | 0.00 USD | 5,980.00 USD | `-23.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 110,060,000.00 USD | 0.00 USD | 303.26 USD | `-22.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 110,060,000.00 USD | 0.00 USD | 3,230.00 USD | `-22.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 110,060,000.00 USD | 0.00 USD | 6,380.00 USD | `-21.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 110,050,000.00 USD | 0.00 USD | 126.54 USD | `-20.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 110,050,000.00 USD | 0.00 USD | 1,790.00 USD | `-20.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 110,050,000.00 USD | 0.00 USD | 6,260.00 USD | `-19.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 110,050,000.00 USD | 0.00 USD | 552.21 USD | `-18.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 110,050,000.00 USD | 0.00 USD | 166.84 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 110,050,000.00 USD | 0.00 USD | 7,690.00 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 110,040,000.00 USD | 0.00 USD | 769.39 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 110,040,000.00 USD | 0.00 USD | 24,760.00 USD | `-16.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 110,010,000.00 USD | 0.00 USD | 6,540.00 USD | `-16.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 110,010,000.00 USD | 0.00 USD | 1,550.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 110,000,000.00 USD | 0.00 USD | 452.97 USD | `-15.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 110,000,000.00 USD | 0.00 USD | 12,640.00 USD | `-14.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 109,990,000.00 USD | 0.00 USD | 317.92 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 109,990,000.00 USD | 0.00 USD | 4,270.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 109,990,000.00 USD | 0.00 USD | 813.97 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 109,990,000.00 USD | 0.00 USD | 1,220.00 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 109,990,000.00 USD | 0.00 USD | 640.67 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 109,980,000.00 USD | 0.00 USD | 595.80 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 109,980,000.00 USD | 0.00 USD | 349.00 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 109,980,000.00 USD | 0.00 USD | 1,760.00 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 109,980,000.00 USD | 0.00 USD | 847.38 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 109,980,000.00 USD | 0.00 USD | 5,090.00 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 109,980,000.00 USD | 0.00 USD | 18,790.00 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 109,960,000.00 USD | 0.00 USD | 14,810.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 109,940,000.00 USD | 0.00 USD | 1,570.00 USD | `-7.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 109,940,000.00 USD | 0.00 USD | 2,720.00 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 109,940,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-6.45%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 73,440,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-5.94%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 36,720.00 USD | 0.00 USD | 2,610.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 34,110.00 USD | 0.00 USD | 519.21 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 33,600.00 USD | 0.00 USD | 1,420.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 32,180.00 USD | 0.00 USD | 389.62 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 31,790.00 USD | 0.00 USD | 3,100.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 28,690.00 USD | 0.00 USD | 19,340.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 9,350.00 USD | 0.00 USD | 1,450.00 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 7,900.00 USD | 0.00 USD | 4,700.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 3,200.00 USD | 0.00 USD | 224.07 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 2,980.00 USD | 0.00 USD | 2,810.00 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 171.55 USD | 0.00 USD | 171.55 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 247.89 USD | 247.89 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 3,900.00 USD | 3,660.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 6,020.00 USD | 2,110.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 6,980.00 USD | 968.08 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 10,200.00 USD | 3,220.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 27,060.00 USD | 16,860.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 73,400.00 USD | 46,340.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 75,240.00 USD | 1,840.00 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 86,510.00 USD | 11,280.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 89,610.00 USD | 3,100.00 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 91,770.00 USD | 2,160.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 107,260.00 USD | 15,490.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 107,570.00 USD | 312.70 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 115,910.00 USD | 8,340.00 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 123,900.00 USD | 7,990.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 145,970.00 USD | 22,070.00 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 165,800.00 USD | 19,820.00 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 172,500.00 USD | 6,700.00 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 176,690.00 USD | 4,190.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 177,660.00 USD | 965.25 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 187,960.00 USD | 10,300.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 188,570.00 USD | 609.66 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 188,680.00 USD | 109.91 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 204,140.00 USD | 15,460.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 207,010.00 USD | 2,870.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 208,660.00 USD | 1,650.00 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 217,840.00 USD | 9,180.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 221,590.00 USD | 3,750.00 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 221,700.00 USD | 114.50 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 222,040.00 USD | 339.60 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 222,150.00 USD | 109.40 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 222,300.00 USD | 151.06 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 231,440.00 USD | 9,140.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 232,100.00 USD | 662.92 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 232,440.00 USD | 337.06 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 232,610.00 USD | 171.12 USD | 0.00 USD | `+19.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 232,710.00 USD | 101.11 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 233,820.00 USD | 1,110.00 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 243,240.00 USD | 9,420.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 243,690.00 USD | 443.91 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 244,470.00 USD | 778.76 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 244,660.00 USD | 192.71 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 245,170.00 USD | 514.45 USD | 0.00 USD | `+22.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 245,380.00 USD | 209.72 USD | 0.00 USD | `+23.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 245,500.00 USD | 115.92 USD | 0.00 USD | `+23.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 245,740.00 USD | 236.19 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 246,880.00 USD | 1,150.00 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 247,170.00 USD | 288.22 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 247,660.00 USD | 491.03 USD | 0.00 USD | `+26.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 248,990.00 USD | 1,320.00 USD | 0.00 USD | `+26.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 258,930.00 USD | 9,940.00 USD | 0.00 USD | `+27.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 259,420.00 USD | 499.00 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 260,520.00 USD | 1,100.00 USD | 0.00 USD | `+28.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 260,690.00 USD | 168.76 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 262,870.00 USD | 2,170.00 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 264,560.00 USD | 1,700.00 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 264,830.00 USD | 271.44 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 685,590.00 USD | 420,750.00 USD | 0.00 USD | `+33.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 686,770.00 USD | 1,180.00 USD | 0.00 USD | `+35.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 695,660.00 USD | 8,890.00 USD | 0.00 USD | `+37.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 710,530.00 USD | 14,860.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 711,870.00 USD | 1,340.00 USD | 0.00 USD | `+38.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 714,580.00 USD | 2,710.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 728,440.00 USD | 13,870.00 USD | 0.00 USD | `+40.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 733,660.00 USD | 5,220.00 USD | 0.00 USD | `+40.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 734,830.00 USD | 1,170.00 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 738,990.00 USD | 4,150.00 USD | 0.00 USD | `+42.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 739,930.00 USD | 944.99 USD | 0.00 USD | `+43.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 740,130.00 USD | 198.73 USD | 0.00 USD | `+45.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 741,500.00 USD | 1,370.00 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 742,580.00 USD | 1,080.00 USD | 0.00 USD | `+47.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 757,560.00 USD | 14,980.00 USD | 0.00 USD | `+48.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 758,800.00 USD | 1,230.00 USD | 0.00 USD | `+49.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 760,240.00 USD | 1,440.00 USD | 0.00 USD | `+52.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 760,600.00 USD | 355.21 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 767,250.00 USD | 6,650.00 USD | 0.00 USD | `+54.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 786,230.00 USD | 18,980.00 USD | 0.00 USD | `+56.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 790,380.00 USD | 4,150.00 USD | 0.00 USD | `+58.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 793,620.00 USD | 3,250.00 USD | 0.00 USD | `+61.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 794,120.00 USD | 493.89 USD | 0.00 USD | `+66.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 794,300.00 USD | 181.30 USD | 0.00 USD | `+66.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 795,680.00 USD | 1,380.00 USD | 0.00 USD | `+68.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 807,970.00 USD | 12,290.00 USD | 0.00 USD | `+70.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 808,080.00 USD | 111.06 USD | 0.00 USD | `+70.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 808,300.00 USD | 220.61 USD | 0.00 USD | `+75.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 811,640.00 USD | 3,340.00 USD | 0.00 USD | `+79.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 811,830.00 USD | 188.75 USD | 0.00 USD | `+93.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 812,740.00 USD | 909.54 USD | 0.00 USD | `+94.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 812,860.00 USD | 121.76 USD | 0.00 USD | `+95.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 813,000.00 USD | 141.78 USD | 0.00 USD | `+99.65%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1660` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 146,290.00 USD | 50,280.00 USD | 147,910.00 USD |
| `7D` | `0.1670` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD |
| `7D` | `0.1680` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD |
| `7D` | `0.1690` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD |
| `7D` | `0.1700` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD |
| `7D` | `0.1710` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD |
| `7D` | `0.1720` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 0.00 USD | 2,920.00 USD | 41,020.00 USD |
| `1D` | `0.1730` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 115,290.00 USD | 33,150.00 USD | 132,970.00 USD |
| `7D` | `0.1730` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 32,310.00 USD | 6,910.00 USD | 82,340.00 USD |
| `1D` | `0.1740` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 56,600.00 USD | 30,930.00 USD | 33,020.00 USD |
| `7D` | `0.1740` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 10,400.00 USD | 29,910.00 USD | 48,080.00 USD |
| `1D` | `0.1750` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 50,990.00 USD | 20,400.00 USD | 46,850.00 USD |
| `7D` | `0.1750` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 7,610.00 USD | 6,730.00 USD | 39,280.00 USD |
| `1D` | `0.1760` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 45,460.00 USD | 8,400.00 USD | 25,060.00 USD |
| `7D` | `0.1760` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD |
| `1D` | `0.1770` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD |
| `7D` | `0.1770` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD |
| `1D` | `0.1780` | 9,020,000.00 USD | 0.00 USD | 9,020,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD |
| `7D` | `0.1780` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 140,230.00 USD | 13,120.00 USD | 56,120.00 USD |
| `1D` | `0.1790` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 114,060.00 USD | 42,720.00 USD | 86,800.00 USD |
| `7D` | `0.1790` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 12,380.00 USD | 28,450.00 USD | 116,120.00 USD |
| `1D` | `0.1800` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 724,590.00 USD | 95,980.00 USD | 184,640.00 USD |
| `7D` | `0.1800` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 469,140.00 USD | 95,830.00 USD | 141,980.00 USD |
| `1D` | `0.1810` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 151,460.00 USD | 56,740.00 USD | 160,440.00 USD |
| `7D` | `0.1810` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 356,840.00 USD | 46,600.00 USD | 179,050.00 USD |
| `1D` | `0.1820` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 435,080.00 USD | 95,510.00 USD | 318,680.00 USD |
| `7D` | `0.1820` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 126,700.00 USD | 63,070.00 USD | 444,200.00 USD |
| `1D` | `0.1830` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 439,340.00 USD | 45,220.00 USD | 65,230.00 USD |
| `7D` | `0.1830` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 441,880.00 USD | 47,220.00 USD | 32,460.00 USD |
| `1D` | `0.1840` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 445,620.00 USD | 111,410.00 USD | 203,410.00 USD |
| `7D` | `0.1840` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 373,060.00 USD | 64,640.00 USD | 192,770.00 USD |
| `1D` | `0.1850` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 154,260.00 USD | 112,070.00 USD | 185,290.00 USD |
| `7D` | `0.1850` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 76,160.00 USD | 72,320.00 USD | 267,580.00 USD |
| `1D` | `0.1860` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 171,980.00 USD | 62,190.00 USD | 521,890.00 USD |
| `7D` | `0.1860` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 70,810.00 USD | 15,200.00 USD | 39,200.00 USD |
| `1D` | `0.1870` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 85,470.00 USD | 38,000.00 USD | 510,020.00 USD |
| `7D` | `0.1870` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD |
| `1D` | `0.1880` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 359,770.00 USD | 232,260.00 USD | 231,940.00 USD |
| `7D` | `0.1880` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 325,960.00 USD | 148,540.00 USD | 670,720.00 USD |
| `1D` | `0.1890` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 410,160.00 USD | 182,950.00 USD | 231,740.00 USD |
| `7D` | `0.1890` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 562,390.00 USD | 144,640.00 USD | 111,430.00 USD |
| `1D` | `0.1900` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 103,950.00 USD | 163,310.00 USD | 481,550.00 USD |
| `7D` | `0.1900` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 255,740.00 USD | 30,390.00 USD | 284,570.00 USD |
| `1D` | `0.1910` | 873,930.00 USD | 0.00 USD | 873,930.00 USD | 688,750.00 USD | 62,290.00 USD | 97,670.00 USD |
| `7D` | `0.1910` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD |
| `1D` | `0.1920` | 25,220.00 USD | 0.00 USD | 25,220.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD |
| `7D` | `0.1920` | 516,300.00 USD | 0.00 USD | 516,300.00 USD | 168,540.00 USD | 0.00 USD | 16,400.00 USD |
| `1D` | `0.1930` | 14,160.00 USD | 0.00 USD | 14,160.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD |
| `7D` | `0.1930` | 331,360.00 USD | 0.00 USD | 331,360.00 USD | 0.00 USD | 0.00 USD | 331,360.00 USD |
| `1D` | `0.1940` | 24,450.00 USD | 24,450.00 USD | 0.00 USD | 0.00 USD | 356.90 USD | 24,090.00 USD |
| `1D` | `0.1940` | 48,890.00 USD | 48,890.00 USD | 0.00 USD | 0.00 USD | 356.90 USD | 24,090.00 USD |
| `7D` | `0.1940` | 342,910.00 USD | 342,910.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `7D` | `0.1940` | 685,810.00 USD | 685,810.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `1D` | `0.1950` | 463,230.00 USD | 463,230.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD | 412,450.00 USD |
| `7D` | `0.1950` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 681,420.00 USD | 1,990.00 USD | 203,120.00 USD |
| `1D` | `0.1960` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 596,440.00 USD | 255,590.00 USD | 559,330.00 USD |
| `7D` | `0.1960` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 430,170.00 USD | 158,320.00 USD | 1,240,000.00 USD |
| `1D` | `0.1970` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 288,590.00 USD | 260,510.00 USD | 428,920.00 USD |
| `7D` | `0.1970` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 65,930.00 USD | 164,750.00 USD | 354,550.00 USD |
| `1D` | `0.1980` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 420,330.00 USD | 145,540.00 USD | 560,340.00 USD |
| `7D` | `0.1980` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 312,350.00 USD | 44,250.00 USD | 383,190.00 USD |
| `1D` | `0.1990` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 251,680.00 USD | 74,740.00 USD | 365,160.00 USD |
| `7D` | `0.1990` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD |
| `1D` | `0.2000` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 426,270.00 USD | 100,110.00 USD | 417,810.00 USD |
| `7D` | `0.2000` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 153,280.00 USD | 61,070.00 USD | 371,130.00 USD |
| `1D` | `0.2010` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 255,670.00 USD | 235,120.00 USD | 395,170.00 USD |
| `7D` | `0.2010` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 361,660.00 USD | 91,810.00 USD | 399,110.00 USD |
| `1D` | `0.2020` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 230,470.00 USD | 94,350.00 USD | 270,300.00 USD |
| `7D` | `0.2020` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 91,080.00 USD | 52,660.00 USD | 529,150.00 USD |
| `1D` | `0.2030` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 150,500.00 USD | 97,440.00 USD | 149,790.00 USD |
| `7D` | `0.2030` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 22,590.00 USD | 94,230.00 USD | 153,910.00 USD |
| `1D` | `0.2040` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 83,570.00 USD | 73,360.00 USD | 132,510.00 USD |
| `7D` | `0.2040` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 62,650.00 USD | 76,780.00 USD | 6,560.00 USD |
| `1D` | `0.2050` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 90,000.00 USD | 32,500.00 USD | 52,620.00 USD |
| `7D` | `0.2050` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 39,740.00 USD | 1,630.00 USD | 57,550.00 USD |
| `1D` | `0.2060` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 314,030.00 USD | 32,110.00 USD | 92,000.00 USD |
| `7D` | `0.2060` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 154,800.00 USD | 18,480.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 196,560.00 USD | 81,580.00 USD | 181,570.00 USD |
| `7D` | `0.2070` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 441,660.00 USD | 141,790.00 USD | 35,600.00 USD |
| `1D` | `0.2080` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 218,960.00 USD | 70,470.00 USD | 42,310.00 USD |
| `7D` | `0.2080` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD |
| `1D` | `0.2090` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 456,020.00 USD | 147,490.00 USD | 273,580.00 USD |
| `7D` | `0.2090` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD |
| `1D` | `0.2100` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 448,900.00 USD | 92,790.00 USD | 206,550.00 USD |
| `7D` | `0.2100` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD |
| `1D` | `0.2110` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 152,340.00 USD | 48,060.00 USD | 129,000.00 USD |
| `7D` | `0.2110` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 1,090,000.00 USD | 518,310.00 USD | 1,620,000.00 USD |
| `1D` | `0.2120` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 163,120.00 USD | 100,480.00 USD | 158,760.00 USD |
| `7D` | `0.2120` | 22,450,000.00 USD | 22,450,000.00 USD | 0.00 USD | 1,170,000.00 USD | 492,740.00 USD | 1,390,000.00 USD |
| `1D` | `0.2130` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 207,060.00 USD | 63,250.00 USD | 120,370.00 USD |
| `7D` | `0.2130` | 25,290,000.00 USD | 25,290,000.00 USD | 0.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,260,000.00 USD |
| `1D` | `0.2140` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 125,780.00 USD | 31,360.00 USD | 26,470.00 USD |
| `7D` | `0.2140` | 27,390,000.00 USD | 27,390,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD |
| `1D` | `0.2150` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 45,180.00 USD | 8,240.00 USD | 17,830.00 USD |
| `7D` | `0.2150` | 29,650,000.00 USD | 29,650,000.00 USD | 0.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD |
| `7D` | `0.2160` | 30,630,000.00 USD | 30,630,000.00 USD | 0.00 USD | 467,380.00 USD | 144,820.00 USD | 370,160.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `416.13M` | Total OI Tokens: `2,134,747,969.5 ADA`
  * 1h OI Change: `+1.08%` | 4h OI Change: `+0.93%` | 24h OI Change: `-7.25%`
  * Exchange Breakdown: Binance=`75.52M` | Bybit=`50.63M` | OKX=`29.53M` | Hyperliquid=`28.29M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.84K` | Last 24h: `30.56K` | Last 3d: `64.45K` | Last 7d: `83.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0065%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `39.24%` | `60.76%` | `0.65` | 15,950,000.00 USD |
| `15M` | `Binance` | `36.45%` | `63.55%` | `0.57` | 9,060,000.00 USD |
| `15M` | `OKX` | `32.03%` | `67.97%` | `0.47` | 1,540,000.00 USD |
| `15M` | `Bybit` | `45.28%` | `54.72%` | `0.83` | 1,790,000.00 USD |
| `15M` | `KuCoin` | `56.06%` | `43.94%` | `1.28` | 47,410.00 USD |
| `15M` | `Gate` | `58.38%` | `41.62%` | `1.40` | 711,020.00 USD |
| `15M` | `Bitget` | `38.18%` | `61.82%` | `0.62` | 239,470.00 USD |
| `15M` | `BingX` | `52.04%` | `47.96%` | `1.09` | 240,220.00 USD |
| `15M` | `MEXC` | `69.99%` | `30.01%` | `2.33` | 282,400.00 USD |
| `15M` | `Bitunix` | `26.4%` | `73.6%` | `0.36` | 599,130.00 USD |
| `15M` | `Hyperliquid` | `29.43%` | `70.57%` | `0.42` | 656,180.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.46%` | `45.54%` | `1.20` | 218,470.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `73.85%` | `26.15%` | `2.82` | 58,990.00 USD |
| `15M` | `HTX` | `47.87%` | `52.13%` | `0.92` | 122,450.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `6.25%` | `93.75%` | `0.07` | 31,420.00 USD |
| `15M` | `Aster` | `63.66%` | `36.34%` | `1.75` | 325,220.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `58.14%` | `41.86%` | `1.39` | 28,680.00 USD |
| `15M` | `Whale Positions` | `36.45%` | `63.55%` | `0.57` | 9,060,000.00 USD |
| `15M` | `Global Accounts` | `39.24%` | `60.76%` | `0.65` | 15,950,000.00 USD |
| `1H` | `ADA` | `45.32%` | `54.68%` | `0.83` | 58,070,000.00 USD |
| `1H` | `Binance` | `41.79%` | `58.21%` | `0.72` | 33,910,000.00 USD |
| `1H` | `OKX` | `52%` | `48%` | `1.08` | 6,280,000.00 USD |
| `1H` | `Bybit` | `47.55%` | `52.45%` | `0.91` | 5,470,000.00 USD |
| `1H` | `KuCoin` | `51.37%` | `48.63%` | `1.06` | 528,120.00 USD |
| `1H` | `Gate` | `54.2%` | `45.8%` | `1.18` | 2,840,000.00 USD |
| `1H` | `Bitget` | `53.38%` | `46.62%` | `1.15` | 849,910.00 USD |
| `1H` | `BingX` | `58.19%` | `41.81%` | `1.39` | 1,070,000.00 USD |
| `1H` | `MEXC` | `65.92%` | `34.08%` | `1.93` | 791,070.00 USD |
| `1H` | `Bitunix` | `49.26%` | `50.74%` | `0.97` | 1,780,000.00 USD |
| `1H` | `Hyperliquid` | `40.6%` | `59.4%` | `0.68` | 1,850,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.81%` | `49.19%` | `1.03` | 621,830.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `25.91%` | `74.09%` | `0.35` | 411,770.00 USD |
| `1H` | `HTX` | `40.66%` | `59.34%` | `0.69` | 444,490.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.59%` | `51.41%` | `0.95` | 62,430.00 USD |
| `1H` | `Aster` | `52.63%` | `47.37%` | `1.11` | 852,700.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.92%` | `47.08%` | `1.12` | 315,110.00 USD |
| `1H` | `Whale Positions` | `41.79%` | `58.21%` | `0.72` | 33,910,000.00 USD |
| `1H` | `Global Accounts` | `45.32%` | `54.68%` | `0.83` | 58,070,000.00 USD |
| `4H` | `ADA` | `46.66%` | `53.34%` | `0.87` | 10,830,000,000.00 USD |
| `4H` | `Binance` | `44.74%` | `55.26%` | `0.81` | 3,180,000,000.00 USD |
| `4H` | `OKX` | `49.3%` | `50.7%` | `0.97` | 1,520,000,000.00 USD |
| `4H` | `Bybit` | `45.9%` | `54.1%` | `0.85` | 963,310,000.00 USD |
| `4H` | `KuCoin` | `51.45%` | `48.55%` | `1.06` | 29,190,000.00 USD |
| `4H` | `Gate` | `50.72%` | `49.28%` | `1.03` | 1,090,000,000.00 USD |
| `4H` | `Bitget` | `43.9%` | `56.1%` | `0.78` | 486,630,000.00 USD |
| `4H` | `BingX` | `49.35%` | `50.65%` | `0.97` | 204,830,000.00 USD |
| `4H` | `MEXC` | `47.17%` | `52.83%` | `0.89` | 521,780,000.00 USD |
| `4H` | `Bitunix` | `48.26%` | `51.74%` | `0.93` | 441,020,000.00 USD |
| `4H` | `Hyperliquid` | `43.49%` | `56.51%` | `0.77` | 618,480,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.45%` | `49.55%` | `1.02` | 692,800,000.00 USD |
| `4H` | `Crypto.com` | `46.68%` | `53.32%` | `0.88` | 37,040,000.00 USD |
| `4H` | `WhiteBIT` | `16.56%` | `83.44%` | `0.20` | 192,110,000.00 USD |
| `4H` | `HTX` | `45.06%` | `54.94%` | `0.82` | 37,440,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `52.2%` | `47.8%` | `1.09` | 517,040,000.00 USD |
| `4H` | `Bitfinex` | `50.36%` | `49.64%` | `1.01` | 8,090,000.00 USD |
| `4H` | `Kraken` | `47.75%` | `52.25%` | `0.91` | 68,380,000.00 USD |
| `4H` | `Aster` | `45.13%` | `54.87%` | `0.82` | 117,290,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.84%` | `49.16%` | `1.03` | 104,150,000.00 USD |
| `4H` | `Whale Positions` | `44.74%` | `55.26%` | `0.81` | 3,180,000,000.00 USD |
| `4H` | `Global Accounts` | `46.66%` | `53.34%` | `0.87` | 10,830,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1925` | `0.1926` | `0.1925` | `0.1930` | `0.1921` | 1,372,988.82 USD | 626,720.98 USD | 746,267.84 USD | -119,546.86 USD | `-8.71%` | `0B / 1S` |
| `5:00 UTC` | `0.1918` | `0.1920` | `0.1918` | `0.1925` | `0.1916` | 742,501.25 USD | 301,932.71 USD | 440,568.55 USD | -138,635.84 USD | `-18.67%` | `1B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1930` | `0.1915` | 1,936,754.49 USD | 922,725.13 USD | 1,014,029.36 USD | -91,304.23 USD | `-4.71%` | `1B / 3S` |
| `5:00 UTC` | `0.1925` | `0.1925` | `0.1925` | `0.1928` | `0.1920` | 818,438.28 USD | 477,644.62 USD | 340,793.66 USD | 136,850.96 USD | `+16.72%` | `0B / 0S` |
| `0:00 UTC` | `0.1928` | `0.1927` | `0.1928` | `0.1930` | `0.1925` | 1,279,303.19 USD | 647,276.72 USD | 632,026.47 USD | 15,250.26 USD | `+1.19%` | `0B / 0S` |
| `5:00 UTC` | `0.1926` | `0.1928` | `0.1926` | `0.1933` | `0.1925` | 1,103,210.95 USD | 609,025.54 USD | 494,185.40 USD | 114,840.14 USD | `+10.41%` | `1B / 0S` |
| `0:00 UTC` | `0.1935` | `0.1936` | `0.1935` | `0.1941` | `0.1926` | 1,737,432.33 USD | 982,431.45 USD | 755,000.88 USD | 227,430.57 USD | `+13.09%` | `2B / 0S` |
| `5:00 UTC` | `0.1951` | `0.1945` | `0.1951` | `0.1951` | `0.1935` | 1,638,885.40 USD | 1,017,708.87 USD | 621,176.53 USD | 396,532.35 USD | `+24.20%` | `5B / 0S` |
| `0:00 UTC` | `0.1946` | `0.1949` | `0.1946` | `0.1955` | `0.1943` | 1,220,578.14 USD | 507,791.59 USD | 712,786.55 USD | -204,994.95 USD | `-16.79%` | `0B / 2S` |
| `5:00 UTC` | `0.1933` | `0.1937` | `0.1933` | `0.1945` | `0.1933` | 1,049,733.04 USD | 369,489.48 USD | 680,243.56 USD | -310,754.08 USD | `-29.60%` | `0B / 7S` |

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
| `5m` | -16,610.00 USD | -49,820.00 USD | **`DISTRIBUTION`** |
| `15m` | 132,100.00 USD | 514,510.00 USD | **`ACCUMULATION`** |
| `30m` | 452,030.00 USD | 1,060,000.00 USD | **`ACCUMULATION`** |
| `1h` | 740,570.00 USD | 1,960,000.00 USD | **`ACCUMULATION`** |
| `2h` | 717,190.00 USD | 1,830,000.00 USD | **`ACCUMULATION`** |
| `4h` | 394,200.00 USD | 1,930,000.00 USD | **`ACCUMULATION`** |
| `6h` | 553,800.00 USD | 2,000,000.00 USD | **`ACCUMULATION`** |
| `8h` | 320,720.00 USD | 3,640,000.00 USD | **`ACCUMULATION`** |
| `12h` | -2,300,000.00 USD | 2,090,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,040,000.00 USD | -7,440,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,920,000.00 USD | -38,180,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,430,000.00 USD | -195,250,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-16.61K` | 15m=`+132.10K` | 1h=`+740.57K` | 24h=`-8.04M`
* Futures Capital Netflows: 5m=`-49.82K` | 15m=`+514.51K` | 1h=`+1.96M` | 24h=`-7.44M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1877` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1832` (Risk Distance: `0.0045` pts)
  * +2.5R Take Profit: `0.1989`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1939` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1984` (Risk Distance: `0.0045` pts)
  * +2.5R Take Profit: `0.1827`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1957`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
