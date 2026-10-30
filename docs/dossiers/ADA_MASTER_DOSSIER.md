# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:12:33 IST` (`2026-10-30 10:42:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1925` | **Live Ask Quote**: `0.1947` | **Mid Price**: `0.1936`
- **Spread Points**: `22.00` | **Spread BPS**: `113.64 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1881` | VWAP Z-Score: `+1.07` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.58` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1977` | Lower -3.00σ Band: `0.1785`
  * Upper +2.51σ Band: `0.1961` | Lower -2.51σ Band: `0.1801`
  * Upper +2.01σ Band: `0.1945` | Lower -2.01σ Band: `0.1817`
  * Upper +2.00σ Band: `0.1945` | Lower -2.00σ Band: `0.1817`
  * Upper +1.28σ Band: `0.1922` | Lower -1.28σ Band: `0.1840`
  * Upper +1.00σ Band: `0.1913` | Lower -1.00σ Band: `0.1849`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1913` | EMA-20=`0.1913` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1919` (Slope: `+0.0000`) | EMA-100=`0.1939`
  * Institutional Anchors: EMA-144=`0.1954` | EMA-200=`0.1971` (Slope: `-0.3863`) | EMA-233=`0.1978`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1938` (Distance: `-0.09%`)
  * Point of Control (POC) = `0.1912` (Distance: `+1.24%`)
  * Value Area Low (VAL) = `0.1875` (Distance: `+3.24%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2065` | Weekly POC=`0.2031` | Weekly VAL=`0.1979`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1940` | Low=`0.1902`
  * New York Session (13:00-21:00 UTC): High=`0.1928` | Low=`0.1912`
  * Initial Balance (First Hour): IB High=`0.1935` | IB Low=`0.1918`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1928` - `0.1944`
  * Optimal Trade Entry (OTE 0.705): `0.1940`
  * Structural Invalidation Anchor (0.786): `0.1951`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1927` | `0.1937` | `0.1926` | `0.1935` | `4,030,099` | 779,182.01 USD | 189,437.42 USD | `+24.31%` | -4,550,134.04 USD | `+1.52` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1934` | `0.1939` | `0.1931` | `0.1939` | `2,949,952` | 571,073.13 USD | 59,930.87 USD | `+10.49%` | -4,490,203.17 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1940` | `0.1941` | `0.1936` | `0.1938` | `1,201,656` | 233,010.68 USD | -80,093.38 USD | `-34.37%` | -4,570,296.55 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1927` | `0.1930` | `0.1924` | `0.1927` | `6,639,699` | 1,279,303.19 USD | 15,250.26 USD | `+1.19%` | -4,854,411.60 USD | `+0.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1926` | `0.1933` | `0.1924` | `0.1927` | `5,722,290` | 1,103,210.95 USD | 114,840.14 USD | `+10.41%` | -4,739,571.46 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1927` | `0.1941` | `0.1926` | `0.1938` | `8,181,707` | 1,583,265.81 USD | 169,274.92 USD | `+10.69%` | -4,570,296.55 USD | `+0.82` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1916` | `0.1924` | `26,112,684` | 5,023,010.35 USD | 493,681.90 USD | `+9.83%` | -4,879,718.95 USD | `+0.44` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1914` | `0.1926` | `25,331,850` | 4,870,682.84 USD | -212,635.97 USD | `-4.37%` | -5,092,354.92 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1927` | `0.1941` | `0.1924` | `0.1938` | `20,543,696` | 3,965,779.95 USD | 299,365.31 USD | `+7.55%` | -4,792,989.60 USD | `+0.37` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1941` | `0.1914` | `0.1937` | `71,988,275` | 13,859,481.86 USD | 580,402.53 USD | `+4.19%` | -4,323,239.17 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,207,439.06 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -4,361,461.60 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1941` | `0.1914` | `0.1937` | `71,988,275` | 13,859,481.86 USD | 580,402.53 USD | `+4.19%` | -4,323,239.17 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.1936`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `537` | `0x77ee...2902` | `SHORT` | 4,135,764.88 USD | `21,412,192.00` | `0.1911` | `0.1937` | `0.5958` | -44,513.14 USD | `-1.08%` | `10X Cross` |
| `1208` | `0x123d...3bff` | `LONG` | 1,816,956.77 USD | `9,392,870.00` | `0.2912` | `0.1937` | `0.000000` | -918,699.95 USD | `-50.56%` | `10X Cross` |
| `1249` | `0x7737...bf66` | `SHORT` | 1,756,925.80 USD | `9,091,466.00` | `0.2190` | `0.1937` | `2.13` | 234,063.99 USD | `+13.32%` | `10X Cross` |
| `1555` | `0x5f94...4b96` | `SHORT` | 1,383,043.61 USD | `7,162,318.00` | `0.2303` | `0.1937` | `0.7152` | 266,431.59 USD | `+19.26%` | `10X Cross` |
| `1772` | `0x4982...59e6` | `SHORT` | 1,158,670.54 USD | `5,998,812.00` | `0.1891` | `0.1937` | `0.4119` | -24,112.18 USD | `-2.08%` | `10X Cross` |
| `1818` | `0xcac1...26b3` | `LONG` | 1,123,117.91 USD | `5,803,927.00` | `0.2000` | `0.1937` | `0.000000` | -37,697.67 USD | `-3.36%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2143` | 1,259.11 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 1.26K USD at 0.2143 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `0.2242` | 4,031.56 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 4.03K USD at 0.2242 USD [API] | `2026-10-08 17:25:15` |
| `ANNOUNCEMENT` | `INFO` | `0.2242` | 389.90 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.39K USD at 0.2242 USD [API] | `2026-10-08 17:25:15` |
| `ANNOUNCEMENT` | `INFO` | `0.2003` | 6,637.14 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.64K USD at 0.2003 USD [API] | `2026-10-29 12:02:00` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 2.82 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.00K USD at 0.2016 USD [API] | `2026-10-29 13:10:03` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 9,363.57 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 9.36K USD at 0.2016 USD [API] | `2026-10-29 13:27:51` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 9,285.95 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 9.29K USD at 0.2016 USD [API] | `2026-10-29 13:27:51` |
| `ANNOUNCEMENT` | `INFO` | `0.2016` | 9,970.42 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 9.97K USD at 0.2016 USD [API] | `2026-10-29 13:27:51` |
| `ANNOUNCEMENT` | `INFO` | `0.2009` | 5,006.19 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2009 USD [API] | `2026-10-29 13:44:17` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 269.55 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.27K USD at 0.2051 USD [API] | `2026-08-26 14:48:31` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 291.91 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.29K USD at 0.2051 USD [API] | `2026-08-26 14:48:31` |
| `ANNOUNCEMENT` | `INFO` | `0.2044` | 6,153.80 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.15K USD at 0.2044 USD [API] | `2026-10-29 17:38:44` |
| `ANNOUNCEMENT` | `INFO` | `0.2033` | 5,005.57 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.01K USD at 0.2033 USD [API] | `2026-10-29 18:14:46` |
| `ANNOUNCEMENT` | `INFO` | `0.2036` | 5,516.20 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.52K USD at 0.2036 USD [API] | `2026-10-29 18:15:11` |
| `ANNOUNCEMENT` | `INFO` | `0.4935` | 596.18 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.60K USD at 0.4935 USD [API] | `2025-10-10 21:18:23` |
| `ANNOUNCEMENT` | `INFO` | `0.4952` | 7,820.83 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 7.82K USD at 0.4952 USD [API] | `2025-10-10 21:18:23` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2099` (Vol: 189,000.00 USD, Dist: `+8.43%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.45%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+8.08%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.48%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 325,500.00 USD, Dist: `+10.41%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.48%`)
  * 7D Horizon: Short MP=`0.2131` (Vol: 448,200.00 USD, Dist: `+10.08%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--5.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0415` | 823.53 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 226.40 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 253.56 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 2,590.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 142.50 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,490.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 773.62 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 235.85 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 7,510.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 1,230.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 896.09 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 156,450.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 3,330.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 12,670.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,270.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 87,280.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,230.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 2,090.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 150.44 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 2,200.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 532.08 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 317.55 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 26,100.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,150.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,640.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 616.20 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 378.58 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 8,360.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 1,180.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,420.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 529.68 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 5,700.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 403.77 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 3,370.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 314.44 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 10,280.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 958.46 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,220.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 292.94 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 5,300.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,720.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,830.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 2,350.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 42,630.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,250.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 11,530.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 157.50 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 703,860.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 2,780.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,580.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 16,800.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,180.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,040.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1640` | 8,340,000.00 USD | 8,340,000.00 USD | 166,770.00 USD | 55,610.00 USD | 217,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 43,740.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1650` | 7,900,000.00 USD | 7,900,000.00 USD | 57,340.00 USD | 18,500.00 USD | 42,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 18,480.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1660` | 7,780,000.00 USD | 7,780,000.00 USD | 88,950.00 USD | 31,770.00 USD | 105,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1665` | 889.94 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1670` | 7,550,000.00 USD | 7,550,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1680` | 7,450,000.00 USD | 7,450,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1685` | 281.23 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1690` | 7,370,000.00 USD | 7,370,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1695` | 79,290.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1700` | 7,270,000.00 USD | 7,270,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1710` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 398,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1720` | 7,170,000.00 USD | 7,170,000.00 USD | 9,500.00 USD | 2,920.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 145,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 9,330,000.00 USD | 9,330,000.00 USD | 115,290.00 USD | 33,150.00 USD | 132,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1730` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 332.90 USD | 82,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 658.61 USD | 112,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 9,050,000.00 USD | 9,050,000.00 USD | 52,460.00 USD | 30,930.00 USD | 33,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1740` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 3,560.00 USD | 32,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1750` | 8,930,000.00 USD | 8,930,000.00 USD | 50,710.00 USD | 15,820.00 USD | 14,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1750` | 7,000,000.00 USD | 7,000,000.00 USD | 7,610.00 USD | 6,730.00 USD | 25,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 17,290.00 USD | 111,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 8,850,000.00 USD | 8,850,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1760` | 6,960,000.00 USD | 6,960,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 49,610.00 USD | 94,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 8,790,000.00 USD | 8,790,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1770` | 6,940,000.00 USD | 6,940,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 44,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 8,480,000.00 USD | 8,480,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1780` | 6,680,000.00 USD | 6,680,000.00 USD | 140,230.00 USD | 12,660.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 43,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 8,350,000.00 USD | 8,350,000.00 USD | 114,060.00 USD | 42,720.00 USD | 86,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 6,470,000.00 USD | 6,470,000.00 USD | 9,850.00 USD | 27,990.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 38,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 8,110,000.00 USD | 8,110,000.00 USD | 736,380.00 USD | 98,670.00 USD | 184,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 6,320,000.00 USD | 6,320,000.00 USD | 464,090.00 USD | 95,830.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 3,050.00 USD | 35,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 7,090,000.00 USD | 7,090,000.00 USD | 160,390.00 USD | 59,240.00 USD | 169,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 5,620,000.00 USD | 5,620,000.00 USD | 354,390.00 USD | 45,990.00 USD | 179,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 20,760.00 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 6,700,000.00 USD | 6,700,000.00 USD | 434,090.00 USD | 97,220.00 USD | 318,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 5,040,000.00 USD | 5,040,000.00 USD | 123,330.00 USD | 62,450.00 USD | 444,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 9,020.00 USD | 11,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 5,850,000.00 USD | 5,850,000.00 USD | 438,560.00 USD | 45,050.00 USD | 65,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 4,410,000.00 USD | 4,410,000.00 USD | 435,140.00 USD | 47,220.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1840` | 5,300,000.00 USD | 5,300,000.00 USD | 444,800.00 USD | 111,320.00 USD | 203,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 3,890,000.00 USD | 3,890,000.00 USD | 273,040.00 USD | 41,950.00 USD | 192,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,300.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 4,540,000.00 USD | 4,540,000.00 USD | 142,760.00 USD | 112,070.00 USD | 185,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 3,380,000.00 USD | 3,380,000.00 USD | 50,160.00 USD | 6,440.00 USD | 228,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 4,100,000.00 USD | 4,100,000.00 USD | 166,780.00 USD | 44,670.00 USD | 430,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 3,100,000.00 USD | 3,100,000.00 USD | 70,810.00 USD | 15,200.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 3,460,000.00 USD | 3,460,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 3,010,000.00 USD | 3,010,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 2,890,000.00 USD | 2,890,000.00 USD | 364,910.00 USD | 232,420.00 USD | 231,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 2,520,000.00 USD | 2,520,000.00 USD | 132,450.00 USD | 103,170.00 USD | 670,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 2,060,000.00 USD | 2,060,000.00 USD | 391,420.00 USD | 182,950.00 USD | 231,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 1,610,000.00 USD | 1,610,000.00 USD | 510,390.00 USD | 12,880.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,250,000.00 USD | 1,250,000.00 USD | 93,550.00 USD | 128,280.00 USD | 299,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 1,060,000.00 USD | 1,060,000.00 USD | 255,740.00 USD | 30,390.00 USD | 216,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 733,850.00 USD | 733,850.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 553,650.00 USD | 553,650.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 11,060.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 600,250.00 USD | 600,250.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 1,200,000.00 USD | 1,200,000.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 14,160.00 USD | 14,160.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 28,330.00 USD | 28,330.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1930` | 2,180,000.00 USD | 2,180,000.00 USD | 653,060.00 USD | 0.00 USD | 331,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 402,350.00 USD | 402,350.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 2,530,000.00 USD | 2,530,000.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 913,670.00 USD | 913,670.00 USD | 25,540.00 USD | 73,330.00 USD | 412,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1950` | 3,430,000.00 USD | 3,430,000.00 USD | 693,070.00 USD | 1,990.00 USD | 203,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 2,340,000.00 USD | 2,340,000.00 USD | 596,440.00 USD | 269,210.00 USD | 559,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 5,020,000.00 USD | 5,020,000.00 USD | 236,660.00 USD | 112,940.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 104.93 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 3,300,000.00 USD | 3,300,000.00 USD | 269,850.00 USD | 260,510.00 USD | 428,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1970` | 5,340,000.00 USD | 5,340,000.00 USD | 13,930.00 USD | 32,990.00 USD | 275,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 4,200,000.00 USD | 4,200,000.00 USD | 409,930.00 USD | 110,510.00 USD | 378,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1980` | 6,010,000.00 USD | 6,010,000.00 USD | 312,350.00 USD | 44,250.00 USD | 315,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 443.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 4,760,000.00 USD | 4,760,000.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1990` | 6,320,000.00 USD | 6,320,000.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 696.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 5,710,000.00 USD | 5,710,000.00 USD | 426,270.00 USD | 100,110.00 USD | 417,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2000` | 6,790,000.00 USD | 6,790,000.00 USD | 56,530.00 USD | 38,390.00 USD | 371,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 3,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 6,580,000.00 USD | 6,580,000.00 USD | 246,300.00 USD | 235,120.00 USD | 395,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 7,510,000.00 USD | 7,510,000.00 USD | 335,650.00 USD | 25,310.00 USD | 359,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 3,870.00 USD | 7,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 7,060,000.00 USD | 7,060,000.00 USD | 225,270.00 USD | 76,840.00 USD | 179,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 8,140,000.00 USD | 8,140,000.00 USD | 87,710.00 USD | 52,030.00 USD | 495,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 3,690.00 USD | 10,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 7,400,000.00 USD | 7,400,000.00 USD | 127,060.00 USD | 93,820.00 USD | 112,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 8,410,000.00 USD | 8,410,000.00 USD | 15,840.00 USD | 94,230.00 USD | 153,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2035` | 137.57 USD | 10,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2040` | 7,700,000.00 USD | 7,700,000.00 USD | 82,750.00 USD | 86,880.00 USD | 132,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 8,550,000.00 USD | 8,550,000.00 USD | 59,380.00 USD | 76,320.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 7,870,000.00 USD | 7,870,000.00 USD | 87,880.00 USD | 32,500.00 USD | 52,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 8,640,000.00 USD | 8,640,000.00 USD | 37,210.00 USD | 1,160.00 USD | 57,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 8,310,000.00 USD | 8,310,000.00 USD | 313,440.00 USD | 31,980.00 USD | 92,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 8,820,000.00 USD | 8,820,000.00 USD | 149,740.00 USD | 18,480.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2065` | 214.55 USD | 11,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2070` | 8,770,000.00 USD | 8,770,000.00 USD | 195,950.00 USD | 81,510.00 USD | 181,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 9,440,000.00 USD | 9,440,000.00 USD | 439,210.00 USD | 141,790.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 9,140,000.00 USD | 9,140,000.00 USD | 250,420.00 USD | 77,280.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 10,130,000.00 USD | 10,130,000.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 10,080,000.00 USD | 10,080,000.00 USD | 484,690.00 USD | 153,650.00 USD | 300,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 13,070,000.00 USD | 13,070,000.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 10,850,000.00 USD | 10,850,000.00 USD | 459,450.00 USD | 102,420.00 USD | 210,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 17,150,000.00 USD | 17,150,000.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2105` | 218.71 USD | 11,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2110` | 11,190,000.00 USD | 11,190,000.00 USD | 157,970.00 USD | 48,270.00 USD | 129,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 20,340,000.00 USD | 20,340,000.00 USD | 1,060,000.00 USD | 511,730.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 11,610,000.00 USD | 11,610,000.00 USD | 160,200.00 USD | 100,480.00 USD | 158,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 23,340,000.00 USD | 23,340,000.00 USD | 1,160,000.00 USD | 466,390.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 153.21 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 11,960,000.00 USD | 11,960,000.00 USD | 209,130.00 USD | 58,810.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 26,160,000.00 USD | 26,160,000.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 28,260,000.00 USD | 28,260,000.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 30,520,000.00 USD | 30,520,000.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 467.20 USD | 12,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2160` | 31,550,000.00 USD | 31,550,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2165` | 224.94 USD | 12,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 16,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2185` | 2,880.00 USD | 19,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 1,230.00 USD | 20,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2205` | 229.10 USD | 20,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2225` | 462.36 USD | 20,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 21,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 23,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 32,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 889.08 USD | 33,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 41,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,670.00 USD | 42,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 680.06 USD | 43,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 44,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 4,050.00 USD | 48,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2485` | 1,060.00 USD | 49,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 50,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 2,390.00 USD | 52,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 52,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 203.13 USD | 52,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 53,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 55,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 55,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 59,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 59,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2945` | 3,980.00 USD | 63,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 71,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 71,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3025` | 124,940.00 USD | 196,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 68,700.00 USD | 265,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 265,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3065` | 206.58 USD | 265,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,190.00 USD | 363,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 1,160.00 USD | 364,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3135` | 3,590.00 USD | 367,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3225` | 1,130.00 USD | 368,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 37,030.00 USD | 406,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 792.55 USD | 406,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 409,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3345` | 239.50 USD | 409,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3355` | 318.73 USD | 409,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3445` | 315.22 USD | 410,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 201,110.00 USD | 611,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 252,960.00 USD | 864,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,120.00 USD | 865,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3555` | 142.56 USD | 865,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 159.36 USD | 865,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3585` | 5,070.00 USD | 870,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 2,940.00 USD | 873,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 143.91 USD | 873,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3665` | 490.74 USD | 874,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3695` | 27,710.00 USD | 901,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 911,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 5,380.00 USD | 916,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3765` | 957.44 USD | 917,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0415` | 2,470,000.00 USD | 0.00 USD | 823.53 USD | `-78.44%` | `19,844.00` |
| `Live` | `Long` | `0.0425` | 2,470,000.00 USD | 0.00 USD | 226.40 USD | `-77.92%` | `5,327.00` |
| `Live` | `Long` | `0.0475` | 2,470,000.00 USD | 0.00 USD | 253.56 USD | `-75.32%` | `5,338.00` |
| `Live` | `Long` | `0.0535` | 2,470,000.00 USD | 0.00 USD | 2,590.00 USD | `-72.20%` | `48,444.00` |
| `Live` | `Long` | `0.0595` | 2,470,000.00 USD | 0.00 USD | 142.50 USD | `-69.08%` | `2,395.00` |
| `Live` | `Long` | `0.0625` | 2,470,000.00 USD | 0.00 USD | 1,490.00 USD | `-67.53%` | `23,814.00` |
| `Live` | `Long` | `0.0655` | 2,470,000.00 USD | 0.00 USD | 773.62 USD | `-65.97%` | `11,811.00` |
| `Live` | `Long` | `0.0685` | 2,470,000.00 USD | 0.00 USD | 235.85 USD | `-64.41%` | `3,443.00` |
| `Live` | `Long` | `0.0715` | 2,470,000.00 USD | 0.00 USD | 7,510.00 USD | `-62.85%` | `105,008.00` |
| `Live` | `Long` | `0.0785` | 2,460,000.00 USD | 0.00 USD | 1,230.00 USD | `-59.21%` | `15,628.00` |
| `Live` | `Long` | `0.0815` | 2,460,000.00 USD | 0.00 USD | 896.09 USD | `-57.65%` | `10,995.00` |
| `Live` | `Long` | `0.0835` | 2,460,000.00 USD | 0.00 USD | 156,450.00 USD | `-56.61%` | `1,873,703.00` |
| `Live` | `Long` | `0.0845` | 2,300,000.00 USD | 0.00 USD | 3,330.00 USD | `-56.09%` | `39,410.00` |
| `Live` | `Long` | `0.0865` | 2,300,000.00 USD | 0.00 USD | 102.50 USD | `-55.06%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,300,000.00 USD | 0.00 USD | 344.75 USD | `-54.54%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,300,000.00 USD | 0.00 USD | 1,150.00 USD | `-54.02%` | `13,050.00` |
| `Live` | `Long` | `0.0905` | 2,300,000.00 USD | 0.00 USD | 12,670.00 USD | `-52.98%` | `140,000.00` |
| `Live` | `Long` | `0.0925` | 2,280,000.00 USD | 0.00 USD | 165.11 USD | `-51.94%` | `1,785.00` |
| `Live` | `Long` | `0.0945` | 2,280,000.00 USD | 0.00 USD | 1,270.00 USD | `-50.90%` | `13,466.00` |
| `Live` | `Long` | `0.0985` | 2,280,000.00 USD | 0.00 USD | 87,280.00 USD | `-48.82%` | `886,128.00` |
| `Live` | `Long` | `0.1025` | 2,190,000.00 USD | 0.00 USD | 4,100.00 USD | `-46.74%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,190,000.00 USD | 0.00 USD | 1,230.00 USD | `-46.22%` | `11,893.00` |
| `Live` | `Long` | `0.1045` | 2,190,000.00 USD | 0.00 USD | 2,090.00 USD | `-45.70%` | `20,000.00` |
| `Live` | `Long` | `0.1055` | 2,190,000.00 USD | 0.00 USD | 150.44 USD | `-45.18%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,190,000.00 USD | 0.00 USD | 653.70 USD | `-44.66%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,190,000.00 USD | 0.00 USD | 2,200.00 USD | `-44.14%` | `20,486.00` |
| `Live` | `Long` | `0.1085` | 2,180,000.00 USD | 0.00 USD | 532.08 USD | `-43.62%` | `4,904.00` |
| `Live` | `Long` | `0.1095` | 2,180,000.00 USD | 0.00 USD | 317.55 USD | `-43.11%` | `2,900.00` |
| `Live` | `Long` | `0.1135` | 2,180,000.00 USD | 0.00 USD | 26,100.00 USD | `-41.03%` | `229,972.00` |
| `Live` | `Long` | `0.1145` | 2,160,000.00 USD | 0.00 USD | 862.64 USD | `-40.51%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,160,000.00 USD | 0.00 USD | 13,150.00 USD | `-39.47%` | `112,888.00` |
| `Live` | `Long` | `0.1175` | 2,140,000.00 USD | 0.00 USD | 1,640.00 USD | `-38.95%` | `13,927.00` |
| `Live` | `Long` | `0.1185` | 2,140,000.00 USD | 0.00 USD | 616.20 USD | `-38.43%` | `5,200.00` |
| `Live` | `Long` | `0.1195` | 2,140,000.00 USD | 0.00 USD | 378.58 USD | `-37.91%` | `3,168.00` |
| `Live` | `Long` | `0.1205` | 2,140,000.00 USD | 0.00 USD | 8,360.00 USD | `-37.39%` | `69,341.00` |
| `Live` | `Long` | `0.1215` | 2,130,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.87%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,130,000.00 USD | 0.00 USD | 1,180.00 USD | `-35.83%` | `9,522.00` |
| `Live` | `Long` | `0.1245` | 2,130,000.00 USD | 0.00 USD | 404.62 USD | `-35.31%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,130,000.00 USD | 0.00 USD | 2,420.00 USD | `-34.79%` | `19,273.00` |
| `Live` | `Long` | `0.1265` | 2,130,000.00 USD | 0.00 USD | 314.61 USD | `-34.27%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,130,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.75%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,130,000.00 USD | 0.00 USD | 2,540.00 USD | `-32.71%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,120,000.00 USD | 0.00 USD | 13,060.00 USD | `-32.19%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,110,000.00 USD | 0.00 USD | 529.68 USD | `-31.67%` | `4,028.00` |
| `Live` | `Long` | `0.1325` | 2,110,000.00 USD | 0.00 USD | 6,960.00 USD | `-31.15%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,100,000.00 USD | 0.00 USD | 5,700.00 USD | `-30.63%` | `42,702.00` |
| `Live` | `Long` | `0.1355` | 2,100,000.00 USD | 0.00 USD | 106.64 USD | `-29.60%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,100,000.00 USD | 0.00 USD | 403.77 USD | `-29.08%` | `2,958.00` |
| `Live` | `Long` | `0.1375` | 2,100,000.00 USD | 0.00 USD | 3,370.00 USD | `-28.56%` | `24,507.00` |
| `Live` | `Long` | `0.1405` | 2,090,000.00 USD | 0.00 USD | 314.44 USD | `-27.00%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,090,000.00 USD | 0.00 USD | 10,280.00 USD | `-26.48%` | `72,683.00` |
| `Live` | `Long` | `0.1425` | 2,080,000.00 USD | 0.00 USD | 958.46 USD | `-25.96%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,080,000.00 USD | 0.00 USD | 15,780.00 USD | `-25.44%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,070,000.00 USD | 0.00 USD | 2,220.00 USD | `-24.92%` | `15,394.00` |
| `Live` | `Long` | `0.1455` | 2,060,000.00 USD | 0.00 USD | 3,770.00 USD | `-24.40%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 2,060,000.00 USD | 0.00 USD | 4,580.00 USD | `-23.88%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,050,000.00 USD | 0.00 USD | 292.94 USD | `-23.36%` | `1,986.00` |
| `Live` | `Long` | `0.1485` | 2,050,000.00 USD | 0.00 USD | 5,300.00 USD | `-22.84%` | `35,723.00` |
| `Live` | `Long` | `0.1495` | 2,050,000.00 USD | 0.00 USD | 427.12 USD | `-22.32%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 2,050,000.00 USD | 0.00 USD | 1,720.00 USD | `-21.80%` | `11,458.00` |
| `Live` | `Long` | `0.1515` | 2,050,000.00 USD | 0.00 USD | 35,830.00 USD | `-21.28%` | `236,501.00` |
| `Live` | `Long` | `0.1525` | 2,010,000.00 USD | 0.00 USD | 2,350.00 USD | `-20.76%` | `15,391.00` |
| `Live` | `Long` | `0.1535` | 2,010,000.00 USD | 0.00 USD | 42,630.00 USD | `-20.24%` | `277,705.00` |
| `Live` | `Long` | `0.1545` | 1,970,000.00 USD | 0.00 USD | 721.05 USD | `-19.72%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,970,000.00 USD | 0.00 USD | 1,250.00 USD | `-19.20%` | `8,067.00` |
| `Live` | `Long` | `0.1565` | 1,960,000.00 USD | 0.00 USD | 11,530.00 USD | `-18.68%` | `73,669.00` |
| `Live` | `Long` | `0.1575` | 1,950,000.00 USD | 0.00 USD | 157.50 USD | `-18.16%` | `1,000.00` |
| `Live` | `Long` | `0.1585` | 1,950,000.00 USD | 0.00 USD | 703,860.00 USD | `-17.65%` | `4,440,778.00` |
| `Live` | `Long` | `0.1595` | 1,250,000.00 USD | 0.00 USD | 2,780.00 USD | `-17.13%` | `17,408.00` |
| `Live` | `Long` | `0.1605` | 1,250,000.00 USD | 0.00 USD | 57,580.00 USD | `-16.61%` | `358,740.00` |
| `Live` | `Long` | `0.1615` | 1,190,000.00 USD | 0.00 USD | 16,800.00 USD | `-16.09%` | `104,026.00` |
| `Live` | `Long` | `0.1625` | 1,170,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.57%` | `13,446.00` |
| `Live` | `Long` | `0.1635` | 1,170,000.00 USD | 0.00 USD | 1,040.00 USD | `-15.05%` | `6,337.00` |
| `Live` | `Long` | `0.1645` | 1,170,000.00 USD | 0.00 USD | 43,740.00 USD | `-14.53%` | `265,896.00` |
| `Live` | `Long` | `0.1655` | 1,120,000.00 USD | 0.00 USD | 18,480.00 USD | `-14.01%` | `111,650.00` |
| `Live` | `Long` | `0.1665` | 1,110,000.00 USD | 0.00 USD | 889.94 USD | `-13.49%` | `5,345.00` |
| `Live` | `Long` | `0.1675` | 1,110,000.00 USD | 0.00 USD | 630.81 USD | `-12.97%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,100,000.00 USD | 0.00 USD | 281.23 USD | `-12.45%` | `1,669.00` |
| `Live` | `Long` | `0.1695` | 1,100,000.00 USD | 0.00 USD | 79,290.00 USD | `-11.93%` | `467,760.00` |
| `Live` | `Long` | `0.1705` | 1,020,000.00 USD | 0.00 USD | 626,600.00 USD | `-11.41%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 398,240.00 USD | 0.00 USD | 252,270.00 USD | `-10.89%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 145,970.00 USD | 0.00 USD | 33,550.00 USD | `-10.37%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 112,420.00 USD | 0.00 USD | 658.61 USD | `-9.85%` | `3,796.00` |
| `Live` | `Long` | `0.1755` | 111,760.00 USD | 0.00 USD | 17,290.00 USD | `-8.81%` | `98,507.00` |
| `Live` | `Long` | `0.1765` | 94,470.00 USD | 0.00 USD | 49,610.00 USD | `-8.29%` | `281,104.00` |
| `Live` | `Long` | `0.1775` | 44,860.00 USD | 0.00 USD | 1,360.00 USD | `-7.77%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 43,500.00 USD | 0.00 USD | 4,530.00 USD | `-7.25%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 38,970.00 USD | 0.00 USD | 3,840.00 USD | `-6.73%` | `21,396.00` |
| `Live` | `Long` | `0.1805` | 35,130.00 USD | 0.00 USD | 3,050.00 USD | `-6.21%` | `16,904.00` |
| `Live` | `Long` | `0.1815` | 32,080.00 USD | 0.00 USD | 20,760.00 USD | `-5.69%` | `114,389.00` |
| `Live` | `Long` | `0.1825` | 11,320.00 USD | 0.00 USD | 9,020.00 USD | `-5.18%` | `49,427.00` |
| `Live` | `Long` | `0.1845` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | `-4.14%` | `12,457.00` |
| `Live` | `Short` | `0.1965` | 104.93 USD | 104.93 USD | 0.00 USD | `+2.10%` | `534.00` |
| `Live` | `Short` | `0.1985` | 443.57 USD | 338.64 USD | 0.00 USD | `+3.14%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 696.54 USD | 252.97 USD | 0.00 USD | `+3.66%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 3,270.00 USD | 2,570.00 USD | 0.00 USD | `+4.18%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 7,140.00 USD | 3,870.00 USD | 0.00 USD | `+4.70%` | `19,225.00` |
| `Live` | `Short` | `0.2025` | 10,830.00 USD | 3,690.00 USD | 0.00 USD | `+5.22%` | `18,209.00` |
| `Live` | `Short` | `0.2035` | 10,970.00 USD | 137.57 USD | 0.00 USD | `+5.74%` | `676.00` |
| `Live` | `Short` | `0.2065` | 11,180.00 USD | 214.55 USD | 0.00 USD | `+7.30%` | `1,039.00` |
| `Live` | `Short` | `0.2105` | 11,400.00 USD | 218.71 USD | 0.00 USD | `+9.37%` | `1,039.00` |
| `Live` | `Short` | `0.2125` | 11,560.00 USD | 153.21 USD | 0.00 USD | `+10.41%` | `721.00` |
| `Live` | `Short` | `0.2155` | 12,020.00 USD | 467.20 USD | 0.00 USD | `+11.97%` | `2,168.00` |
| `Live` | `Short` | `0.2165` | 12,250.00 USD | 224.94 USD | 0.00 USD | `+12.49%` | `1,039.00` |
| `Live` | `Short` | `0.2175` | 16,180.00 USD | 3,930.00 USD | 0.00 USD | `+13.01%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 19,060.00 USD | 2,880.00 USD | 0.00 USD | `+13.53%` | `13,175.00` |
| `Live` | `Short` | `0.2195` | 20,290.00 USD | 1,230.00 USD | 0.00 USD | `+14.05%` | `5,601.00` |
| `Live` | `Short` | `0.2205` | 20,510.00 USD | 229.10 USD | 0.00 USD | `+14.57%` | `1,039.00` |
| `Live` | `Short` | `0.2225` | 20,980.00 USD | 462.36 USD | 0.00 USD | `+15.61%` | `2,078.00` |
| `Live` | `Short` | `0.2235` | 21,180.00 USD | 200.48 USD | 0.00 USD | `+16.13%` | `897.00` |
| `Live` | `Short` | `0.2265` | 23,410.00 USD | 2,230.00 USD | 0.00 USD | `+17.69%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 32,650.00 USD | 9,240.00 USD | 0.00 USD | `+18.73%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 33,540.00 USD | 889.08 USD | 0.00 USD | `+20.80%` | `3,824.00` |
| `Live` | `Short` | `0.2335` | 41,170.00 USD | 7,640.00 USD | 0.00 USD | `+21.32%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 42,850.00 USD | 1,670.00 USD | 0.00 USD | `+24.96%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 43,530.00 USD | 680.06 USD | 0.00 USD | `+25.48%` | `2,816.00` |
| `Live` | `Short` | `0.2425` | 44,600.00 USD | 1,080.00 USD | 0.00 USD | `+26.00%` | `4,435.00` |
| `Live` | `Short` | `0.2445` | 48,650.00 USD | 4,050.00 USD | 0.00 USD | `+27.04%` | `16,564.00` |
| `Live` | `Short` | `0.2485` | 49,710.00 USD | 1,060.00 USD | 0.00 USD | `+29.12%` | `4,254.00` |
| `Live` | `Short` | `0.2585` | 50,090.00 USD | 380.25 USD | 0.00 USD | `+34.31%` | `1,471.00` |
| `Live` | `Short` | `0.2675` | 52,470.00 USD | 2,390.00 USD | 0.00 USD | `+38.99%` | `8,916.00` |
| `Live` | `Short` | `0.2715` | 52,590.00 USD | 120.00 USD | 0.00 USD | `+41.07%` | `442.00` |
| `Live` | `Short` | `0.2745` | 52,800.00 USD | 203.13 USD | 0.00 USD | `+42.63%` | `740.00` |
| `Live` | `Short` | `0.2775` | 53,180.00 USD | 379.62 USD | 0.00 USD | `+44.19%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 55,350.00 USD | 2,170.00 USD | 0.00 USD | `+47.82%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 55,760.00 USD | 411.09 USD | 0.00 USD | `+50.42%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 59,020.00 USD | 3,260.00 USD | 0.00 USD | `+51.46%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 59,540.00 USD | 519.79 USD | 0.00 USD | `+52.50%` | `1,771.00` |
| `Live` | `Short` | `0.2945` | 63,520.00 USD | 3,980.00 USD | 0.00 USD | `+53.02%` | `13,504.00` |
| `Live` | `Short` | `0.2955` | 71,510.00 USD | 7,990.00 USD | 0.00 USD | `+53.54%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 71,650.00 USD | 146.34 USD | 0.00 USD | `+56.14%` | `487.00` |
| `Live` | `Short` | `0.3025` | 196,590.00 USD | 124,940.00 USD | 0.00 USD | `+57.18%` | `413,024.00` |
| `Live` | `Short` | `0.3045` | 265,290.00 USD | 68,700.00 USD | 0.00 USD | `+58.21%` | `225,601.00` |
| `Live` | `Short` | `0.3055` | 265,700.00 USD | 408.15 USD | 0.00 USD | `+58.73%` | `1,336.00` |
| `Live` | `Short` | `0.3065` | 265,900.00 USD | 206.58 USD | 0.00 USD | `+59.25%` | `674.00` |
| `Live` | `Short` | `0.3115` | 363,100.00 USD | 97,190.00 USD | 0.00 USD | `+61.85%` | `312,021.00` |
| `Live` | `Short` | `0.3125` | 364,260.00 USD | 1,160.00 USD | 0.00 USD | `+62.37%` | `3,713.00` |
| `Live` | `Short` | `0.3135` | 367,850.00 USD | 3,590.00 USD | 0.00 USD | `+62.89%` | `11,458.00` |
| `Live` | `Short` | `0.3225` | 368,980.00 USD | 1,130.00 USD | 0.00 USD | `+67.57%` | `3,500.00` |
| `Live` | `Short` | `0.3265` | 406,010.00 USD | 37,030.00 USD | 0.00 USD | `+69.65%` | `113,421.00` |
| `Live` | `Short` | `0.3275` | 406,800.00 USD | 792.55 USD | 0.00 USD | `+70.17%` | `2,420.00` |
| `Live` | `Short` | `0.3295` | 409,180.00 USD | 2,380.00 USD | 0.00 USD | `+71.20%` | `7,219.00` |
| `Live` | `Short` | `0.3345` | 409,420.00 USD | 239.50 USD | 0.00 USD | `+73.80%` | `716.00` |
| `Live` | `Short` | `0.3355` | 409,740.00 USD | 318.73 USD | 0.00 USD | `+74.32%` | `950.00` |
| `Live` | `Short` | `0.3445` | 410,060.00 USD | 315.22 USD | 0.00 USD | `+79.00%` | `915.00` |
| `Live` | `Short` | `0.3495` | 611,160.00 USD | 201,110.00 USD | 0.00 USD | `+81.60%` | `575,408.00` |
| `Live` | `Short` | `0.3505` | 864,120.00 USD | 252,960.00 USD | 0.00 USD | `+82.12%` | `721,698.00` |
| `Live` | `Short` | `0.3515` | 865,240.00 USD | 1,120.00 USD | 0.00 USD | `+82.64%` | `3,187.00` |
| `Live` | `Short` | `0.3555` | 865,380.00 USD | 142.56 USD | 0.00 USD | `+84.71%` | `401.00` |
| `Live` | `Short` | `0.3565` | 865,540.00 USD | 159.36 USD | 0.00 USD | `+85.23%` | `447.00` |
| `Live` | `Short` | `0.3585` | 870,610.00 USD | 5,070.00 USD | 0.00 USD | `+86.27%` | `14,148.00` |
| `Live` | `Short` | `0.3615` | 873,550.00 USD | 2,940.00 USD | 0.00 USD | `+87.83%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 873,700.00 USD | 143.91 USD | 0.00 USD | `+88.35%` | `397.00` |
| `Live` | `Short` | `0.3665` | 874,190.00 USD | 490.74 USD | 0.00 USD | `+90.43%` | `1,339.00` |
| `Live` | `Short` | `0.3695` | 901,900.00 USD | 27,710.00 USD | 0.00 USD | `+91.99%` | `75,000.00` |
| `Live` | `Short` | `0.3715` | 911,070.00 USD | 9,170.00 USD | 0.00 USD | `+93.03%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 916,450.00 USD | 5,380.00 USD | 0.00 USD | `+94.59%` | `14,364.00` |
| `Live` | `Short` | `0.3765` | 917,410.00 USD | 957.44 USD | 0.00 USD | `+95.63%` | `2,543.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 110,720,000.00 USD | 0.00 USD | 415.13 USD | `-69.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 110,720,000.00 USD | 0.00 USD | 438.99 USD | `-68.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 110,720,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 110,720,000.00 USD | 0.00 USD | 541.33 USD | `-42.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 110,720,000.00 USD | 0.00 USD | 429.20 USD | `-39.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 110,720,000.00 USD | 0.00 USD | 602,500.00 USD | `-37.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 110,110,000.00 USD | 0.00 USD | 4,460.00 USD | `-35.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 110,110,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 110,110,000.00 USD | 0.00 USD | 13,390.00 USD | `-32.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 110,100,000.00 USD | 0.00 USD | 728.88 USD | `-31.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 110,090,000.00 USD | 0.00 USD | 4,350.00 USD | `-30.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 110,090,000.00 USD | 0.00 USD | 4,730.00 USD | `-28.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 110,090,000.00 USD | 0.00 USD | 1,820.00 USD | `-27.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 110,080,000.00 USD | 0.00 USD | 1,050.00 USD | `-26.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 110,080,000.00 USD | 0.00 USD | 351.26 USD | `-25.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 110,080,000.00 USD | 0.00 USD | 1,600.00 USD | `-25.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 110,080,000.00 USD | 0.00 USD | 10,400.00 USD | `-24.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 110,070,000.00 USD | 0.00 USD | 5,980.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 110,060,000.00 USD | 0.00 USD | 303.26 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 110,060,000.00 USD | 0.00 USD | 3,230.00 USD | `-21.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 110,060,000.00 USD | 0.00 USD | 6,380.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 110,050,000.00 USD | 0.00 USD | 126.54 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 110,050,000.00 USD | 0.00 USD | 1,790.00 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 110,050,000.00 USD | 0.00 USD | 6,260.00 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 110,050,000.00 USD | 0.00 USD | 552.21 USD | `-17.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 110,050,000.00 USD | 0.00 USD | 166.84 USD | `-17.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 110,050,000.00 USD | 0.00 USD | 10,270.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 110,040,000.00 USD | 0.00 USD | 769.39 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 110,030,000.00 USD | 0.00 USD | 24,760.00 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 110,010,000.00 USD | 0.00 USD | 6,540.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 110,000,000.00 USD | 0.00 USD | 1,550.00 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 110,000,000.00 USD | 0.00 USD | 452.97 USD | `-14.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 110,000,000.00 USD | 0.00 USD | 12,640.00 USD | `-13.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 109,990,000.00 USD | 0.00 USD | 317.92 USD | `-12.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 109,990,000.00 USD | 0.00 USD | 4,270.00 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 109,980,000.00 USD | 0.00 USD | 813.97 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 109,980,000.00 USD | 0.00 USD | 1,220.00 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 109,980,000.00 USD | 0.00 USD | 640.67 USD | `-10.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 109,980,000.00 USD | 0.00 USD | 595.80 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 109,980,000.00 USD | 0.00 USD | 349.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 109,980,000.00 USD | 0.00 USD | 1,760.00 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 109,980,000.00 USD | 0.00 USD | 847.38 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 109,980,000.00 USD | 0.00 USD | 5,090.00 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 109,970,000.00 USD | 0.00 USD | 18,790.00 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 109,950,000.00 USD | 0.00 USD | 14,810.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 109,940,000.00 USD | 0.00 USD | 1,570.00 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 109,940,000.00 USD | 0.00 USD | 2,720.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 109,940,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-5.18%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 73,440,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-4.66%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 33,940.00 USD | 0.00 USD | 2,610.00 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 31,340.00 USD | 0.00 USD | 805.63 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 30,530.00 USD | 0.00 USD | 1,420.00 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 29,110.00 USD | 0.00 USD | 528.38 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 28,590.00 USD | 0.00 USD | 3,100.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 25,480.00 USD | 0.00 USD | 19,340.00 USD | `-1.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 6,140.00 USD | 0.00 USD | 1,450.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 4,700.00 USD | 0.00 USD | 4,700.00 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 224.07 USD | 224.07 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 3,240.00 USD | 3,010.00 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 3,410.00 USD | 171.55 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 3,960.00 USD | 549.75 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 7,610.00 USD | 3,660.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 9,730.00 USD | 2,110.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 10,690.00 USD | 968.08 USD | 0.00 USD | `+3.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 11,810.00 USD | 1,120.00 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 28,670.00 USD | 16,860.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 75,010.00 USD | 46,340.00 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 76,850.00 USD | 1,840.00 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 88,120.00 USD | 11,280.00 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 91,040.00 USD | 2,910.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 93,190.00 USD | 2,160.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 108,680.00 USD | 15,490.00 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 108,990.00 USD | 312.70 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 117,330.00 USD | 8,340.00 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 125,330.00 USD | 7,990.00 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 147,400.00 USD | 22,070.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 167,230.00 USD | 19,820.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 173,930.00 USD | 6,700.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 178,120.00 USD | 4,190.00 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 179,090.00 USD | 965.25 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 189,390.00 USD | 10,300.00 USD | 0.00 USD | `+11.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 190,000.00 USD | 609.66 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 190,110.00 USD | 109.91 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 205,570.00 USD | 15,460.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 208,330.00 USD | 2,760.00 USD | 0.00 USD | `+14.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 209,980.00 USD | 1,650.00 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 219,160.00 USD | 9,180.00 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 222,910.00 USD | 3,750.00 USD | 0.00 USD | `+16.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 223,030.00 USD | 114.50 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 223,370.00 USD | 339.60 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 223,480.00 USD | 109.40 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 223,630.00 USD | 151.06 USD | 0.00 USD | `+18.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 232,770.00 USD | 9,140.00 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 233,430.00 USD | 662.92 USD | 0.00 USD | `+19.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 233,770.00 USD | 337.06 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 233,940.00 USD | 171.12 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 234,040.00 USD | 101.11 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 235,150.00 USD | 1,110.00 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 244,570.00 USD | 9,420.00 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 245,010.00 USD | 443.91 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 245,790.00 USD | 778.76 USD | 0.00 USD | `+23.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 245,980.00 USD | 192.71 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 246,500.00 USD | 514.45 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 246,710.00 USD | 209.72 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 246,820.00 USD | 115.92 USD | 0.00 USD | `+25.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 247,060.00 USD | 236.19 USD | 0.00 USD | `+26.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 248,210.00 USD | 1,150.00 USD | 0.00 USD | `+27.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 248,500.00 USD | 288.22 USD | 0.00 USD | `+27.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 248,990.00 USD | 491.03 USD | 0.00 USD | `+28.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 250,310.00 USD | 1,320.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 260,250.00 USD | 9,940.00 USD | 0.00 USD | `+29.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 260,750.00 USD | 499.00 USD | 0.00 USD | `+29.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 261,850.00 USD | 1,100.00 USD | 0.00 USD | `+30.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 262,020.00 USD | 168.76 USD | 0.00 USD | `+30.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 264,190.00 USD | 2,170.00 USD | 0.00 USD | `+31.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 265,890.00 USD | 1,700.00 USD | 0.00 USD | `+33.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 266,160.00 USD | 271.44 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 686,910.00 USD | 420,750.00 USD | 0.00 USD | `+35.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 688,090.00 USD | 1,180.00 USD | 0.00 USD | `+37.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 696,990.00 USD | 8,890.00 USD | 0.00 USD | `+38.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 711,850.00 USD | 14,860.00 USD | 0.00 USD | `+39.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 713,190.00 USD | 1,340.00 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 715,900.00 USD | 2,710.00 USD | 0.00 USD | `+41.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 729,770.00 USD | 13,870.00 USD | 0.00 USD | `+42.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 734,980.00 USD | 5,220.00 USD | 0.00 USD | `+42.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 736,160.00 USD | 1,170.00 USD | 0.00 USD | `+44.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 740,310.00 USD | 4,150.00 USD | 0.00 USD | `+44.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 741,250.00 USD | 944.99 USD | 0.00 USD | `+45.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 741,450.00 USD | 198.73 USD | 0.00 USD | `+47.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 742,830.00 USD | 1,370.00 USD | 0.00 USD | `+47.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 743,900.00 USD | 1,080.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 758,890.00 USD | 14,980.00 USD | 0.00 USD | `+50.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 760,120.00 USD | 1,230.00 USD | 0.00 USD | `+51.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 761,570.00 USD | 1,440.00 USD | 0.00 USD | `+54.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 761,920.00 USD | 355.21 USD | 0.00 USD | `+55.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 768,570.00 USD | 6,650.00 USD | 0.00 USD | `+56.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 787,550.00 USD | 18,980.00 USD | 0.00 USD | `+58.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 791,700.00 USD | 4,150.00 USD | 0.00 USD | `+60.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 794,950.00 USD | 3,250.00 USD | 0.00 USD | `+63.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 795,440.00 USD | 493.89 USD | 0.00 USD | `+68.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 795,620.00 USD | 181.30 USD | 0.00 USD | `+69.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 797,010.00 USD | 1,380.00 USD | 0.00 USD | `+71.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 809,290.00 USD | 12,290.00 USD | 0.00 USD | `+72.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 809,410.00 USD | 111.06 USD | 0.00 USD | `+73.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 809,630.00 USD | 220.61 USD | 0.00 USD | `+77.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 812,960.00 USD | 3,340.00 USD | 0.00 USD | `+81.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 813,150.00 USD | 188.75 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 814,060.00 USD | 909.54 USD | 0.00 USD | `+96.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 814,180.00 USD | 121.76 USD | 0.00 USD | `+97.70%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1640` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 166,770.00 USD | 55,610.00 USD | 217,430.00 USD |
| `7D` | `0.1650` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 57,340.00 USD | 18,500.00 USD | 42,730.00 USD |
| `7D` | `0.1660` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 88,950.00 USD | 31,770.00 USD | 105,170.00 USD |
| `7D` | `0.1670` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD |
| `7D` | `0.1680` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD |
| `7D` | `0.1690` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD |
| `7D` | `0.1700` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD |
| `7D` | `0.1710` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD |
| `7D` | `0.1720` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 9,500.00 USD | 2,920.00 USD | 41,020.00 USD |
| `1D` | `0.1730` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 115,290.00 USD | 33,150.00 USD | 132,970.00 USD |
| `7D` | `0.1730` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 0.00 USD | 332.90 USD | 82,340.00 USD |
| `1D` | `0.1740` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 52,460.00 USD | 30,930.00 USD | 33,020.00 USD |
| `7D` | `0.1740` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 0.00 USD | 3,560.00 USD | 32,360.00 USD |
| `1D` | `0.1750` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 50,710.00 USD | 15,820.00 USD | 14,890.00 USD |
| `7D` | `0.1750` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 7,610.00 USD | 6,730.00 USD | 25,660.00 USD |
| `1D` | `0.1760` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD |
| `7D` | `0.1760` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD |
| `1D` | `0.1770` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD |
| `7D` | `0.1770` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD |
| `1D` | `0.1780` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD |
| `7D` | `0.1780` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 140,230.00 USD | 12,660.00 USD | 56,120.00 USD |
| `1D` | `0.1790` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 114,060.00 USD | 42,720.00 USD | 86,800.00 USD |
| `7D` | `0.1790` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 9,850.00 USD | 27,990.00 USD | 116,120.00 USD |
| `1D` | `0.1800` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 736,380.00 USD | 98,670.00 USD | 184,730.00 USD |
| `7D` | `0.1800` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 464,090.00 USD | 95,830.00 USD | 141,980.00 USD |
| `1D` | `0.1810` | 7,090,000.00 USD | 0.00 USD | 7,090,000.00 USD | 160,390.00 USD | 59,240.00 USD | 169,600.00 USD |
| `7D` | `0.1810` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 354,390.00 USD | 45,990.00 USD | 179,050.00 USD |
| `1D` | `0.1820` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 434,090.00 USD | 97,220.00 USD | 318,680.00 USD |
| `7D` | `0.1820` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 123,330.00 USD | 62,450.00 USD | 444,200.00 USD |
| `1D` | `0.1830` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 438,560.00 USD | 45,050.00 USD | 65,230.00 USD |
| `7D` | `0.1830` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 435,140.00 USD | 47,220.00 USD | 32,460.00 USD |
| `1D` | `0.1840` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 444,800.00 USD | 111,320.00 USD | 203,410.00 USD |
| `7D` | `0.1840` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 273,040.00 USD | 41,950.00 USD | 192,770.00 USD |
| `1D` | `0.1850` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 142,760.00 USD | 112,070.00 USD | 185,290.00 USD |
| `7D` | `0.1850` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 50,160.00 USD | 6,440.00 USD | 228,270.00 USD |
| `1D` | `0.1860` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 166,780.00 USD | 44,670.00 USD | 430,730.00 USD |
| `7D` | `0.1860` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 70,810.00 USD | 15,200.00 USD | 5,140.00 USD |
| `1D` | `0.1870` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD |
| `7D` | `0.1870` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD |
| `1D` | `0.1880` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 364,910.00 USD | 232,420.00 USD | 231,940.00 USD |
| `7D` | `0.1880` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 132,450.00 USD | 103,170.00 USD | 670,720.00 USD |
| `1D` | `0.1890` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 391,420.00 USD | 182,950.00 USD | 231,740.00 USD |
| `7D` | `0.1890` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 510,390.00 USD | 12,880.00 USD | 32,810.00 USD |
| `1D` | `0.1900` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 93,550.00 USD | 128,280.00 USD | 299,230.00 USD |
| `7D` | `0.1900` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 255,740.00 USD | 30,390.00 USD | 216,460.00 USD |
| `1D` | `0.1910` | 733,850.00 USD | 0.00 USD | 733,850.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD |
| `7D` | `0.1910` | 553,650.00 USD | 0.00 USD | 553,650.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD |
| `1D` | `0.1920` | 11,060.00 USD | 0.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD |
| `7D` | `0.1920` | 600,250.00 USD | 600,250.00 USD | 0.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD |
| `7D` | `0.1920` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD |
| `1D` | `0.1930` | 14,160.00 USD | 14,160.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD |
| `1D` | `0.1930` | 28,330.00 USD | 28,330.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD |
| `7D` | `0.1930` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 653,060.00 USD | 0.00 USD | 331,360.00 USD |
| `1D` | `0.1940` | 402,350.00 USD | 402,350.00 USD | 0.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD |
| `7D` | `0.1940` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `1D` | `0.1950` | 913,670.00 USD | 913,670.00 USD | 0.00 USD | 25,540.00 USD | 73,330.00 USD | 412,450.00 USD |
| `7D` | `0.1950` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 693,070.00 USD | 1,990.00 USD | 203,120.00 USD |
| `1D` | `0.1960` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 596,440.00 USD | 269,210.00 USD | 559,330.00 USD |
| `7D` | `0.1960` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 236,660.00 USD | 112,940.00 USD | 1,240,000.00 USD |
| `1D` | `0.1970` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 269,850.00 USD | 260,510.00 USD | 428,920.00 USD |
| `7D` | `0.1970` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 13,930.00 USD | 32,990.00 USD | 275,930.00 USD |
| `1D` | `0.1980` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 409,930.00 USD | 110,510.00 USD | 378,020.00 USD |
| `7D` | `0.1980` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 312,350.00 USD | 44,250.00 USD | 315,080.00 USD |
| `1D` | `0.1990` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD |
| `7D` | `0.1990` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD |
| `1D` | `0.2000` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 426,270.00 USD | 100,110.00 USD | 417,810.00 USD |
| `7D` | `0.2000` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 56,530.00 USD | 38,390.00 USD | 371,130.00 USD |
| `1D` | `0.2010` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 246,300.00 USD | 235,120.00 USD | 395,170.00 USD |
| `7D` | `0.2010` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 335,650.00 USD | 25,310.00 USD | 359,800.00 USD |
| `1D` | `0.2020` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 225,270.00 USD | 76,840.00 USD | 179,140.00 USD |
| `7D` | `0.2020` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 87,710.00 USD | 52,030.00 USD | 495,090.00 USD |
| `1D` | `0.2030` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 127,060.00 USD | 93,820.00 USD | 112,940.00 USD |
| `7D` | `0.2030` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 15,840.00 USD | 94,230.00 USD | 153,910.00 USD |
| `1D` | `0.2040` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 82,750.00 USD | 86,880.00 USD | 132,960.00 USD |
| `7D` | `0.2040` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 59,380.00 USD | 76,320.00 USD | 6,560.00 USD |
| `1D` | `0.2050` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 87,880.00 USD | 32,500.00 USD | 52,620.00 USD |
| `7D` | `0.2050` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 37,210.00 USD | 1,160.00 USD | 57,550.00 USD |
| `1D` | `0.2060` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 313,440.00 USD | 31,980.00 USD | 92,350.00 USD |
| `7D` | `0.2060` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 149,740.00 USD | 18,480.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 195,950.00 USD | 81,510.00 USD | 181,570.00 USD |
| `7D` | `0.2070` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 439,210.00 USD | 141,790.00 USD | 35,600.00 USD |
| `1D` | `0.2080` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 250,420.00 USD | 77,280.00 USD | 42,540.00 USD |
| `7D` | `0.2080` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD |
| `1D` | `0.2090` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 484,690.00 USD | 153,650.00 USD | 300,210.00 USD |
| `7D` | `0.2090` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD |
| `1D` | `0.2100` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 459,450.00 USD | 102,420.00 USD | 210,050.00 USD |
| `7D` | `0.2100` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD |
| `1D` | `0.2110` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 157,970.00 USD | 48,270.00 USD | 129,000.00 USD |
| `7D` | `0.2110` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 1,060,000.00 USD | 511,730.00 USD | 1,620,000.00 USD |
| `1D` | `0.2120` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 160,200.00 USD | 100,480.00 USD | 158,760.00 USD |
| `7D` | `0.2120` | 23,340,000.00 USD | 23,340,000.00 USD | 0.00 USD | 1,160,000.00 USD | 466,390.00 USD | 1,380,000.00 USD |
| `1D` | `0.2130` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 209,130.00 USD | 58,810.00 USD | 88,410.00 USD |
| `7D` | `0.2130` | 26,160,000.00 USD | 26,160,000.00 USD | 0.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,250,000.00 USD |
| `7D` | `0.2140` | 28,260,000.00 USD | 28,260,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD |
| `7D` | `0.2150` | 30,520,000.00 USD | 30,520,000.00 USD | 0.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD |
| `7D` | `0.2160` | 31,550,000.00 USD | 31,550,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `413.71M` | Total OI Tokens: `2,129,772,790.0 ADA`
  * 1h OI Change: `+1.35%` | 4h OI Change: `+0.11%` | 24h OI Change: `-7.15%`
  * Exchange Breakdown: Binance=`75.30M` | Bybit=`50.14M` | OKX=`29.57M` | Hyperliquid=`28.27M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.75K` | Last 24h: `30.56K` | Last 3d: `64.45K` | Last 7d: `83.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0049%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0078%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `46.01%` | `53.99%` | `0.85` | 16,040,000.00 USD |
| `15M` | `Binance` | `38.36%` | `61.64%` | `0.62` | 9,200,000.00 USD |
| `15M` | `OKX` | `66.04%` | `33.96%` | `1.94` | 2,200,000.00 USD |
| `15M` | `Bybit` | `49.84%` | `50.16%` | `0.99` | 1,340,000.00 USD |
| `15M` | `KuCoin` | `55.95%` | `44.05%` | `1.27` | 198,760.00 USD |
| `15M` | `Gate` | `49.09%` | `50.91%` | `0.96` | 728,960.00 USD |
| `15M` | `Bitget` | `69.95%` | `30.05%` | `2.33` | 252,830.00 USD |
| `15M` | `BingX` | `48.72%` | `51.28%` | `0.95` | 237,790.00 USD |
| `15M` | `MEXC` | `92.3%` | `7.7%` | `11.99` | 242,450.00 USD |
| `15M` | `Bitunix` | `46.29%` | `53.71%` | `0.86` | 409,080.00 USD |
| `15M` | `Hyperliquid` | `49.29%` | `50.71%` | `0.97` | 451,610.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55%` | `45%` | `1.22` | 187,640.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `2.36%` | `97.64%` | `0.02` | 190,990.00 USD |
| `15M` | `HTX` | `41.15%` | `58.85%` | `0.70` | 118,600.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `42.6%` | `57.4%` | `0.74` | 33,640.00 USD |
| `15M` | `Aster` | `68.83%` | `31.17%` | `2.21` | 186,990.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.68%` | `46.32%` | `1.16` | 64,040.00 USD |
| `15M` | `Whale Positions` | `38.36%` | `61.64%` | `0.62` | 9,200,000.00 USD |
| `15M` | `Global Accounts` | `46.01%` | `53.99%` | `0.85` | 16,040,000.00 USD |
| `1H` | `ADA` | `47.33%` | `52.67%` | `0.90` | 39,400,000.00 USD |
| `1H` | `Binance` | `50.83%` | `49.17%` | `1.03` | 12,710,000.00 USD |
| `1H` | `OKX` | `54.6%` | `45.4%` | `1.20` | 6,270,000.00 USD |
| `1H` | `Bybit` | `47.93%` | `52.07%` | `0.92` | 2,500,000.00 USD |
| `1H` | `KuCoin` | `54.09%` | `45.91%` | `1.18` | 246,900.00 USD |
| `1H` | `Gate` | `46.94%` | `53.06%` | `0.88` | 7,160,000.00 USD |
| `1H` | `Bitget` | `47.81%` | `52.19%` | `0.92` | 489,580.00 USD |
| `1H` | `BingX` | `23.61%` | `76.39%` | `0.31` | 1,100,000.00 USD |
| `1H` | `MEXC` | `59.6%` | `40.4%` | `1.48` | 2,180,000.00 USD |
| `1H` | `Bitunix` | `54.73%` | `45.27%` | `1.21` | 1,060,000.00 USD |
| `1H` | `Hyperliquid` | `89.35%` | `10.65%` | `8.39` | 743,490.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.55%` | `45.45%` | `1.20` | 229,490.00 USD |
| `1H` | `Crypto.com` | `54.4%` | `45.6%` | `1.19` | 55,410.00 USD |
| `1H` | `WhiteBIT` | `7.35%` | `92.65%` | `0.08` | 3,590,000.00 USD |
| `1H` | `HTX` | `58.43%` | `41.57%` | `1.41` | 279,020.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `61.4%` | `38.6%` | `1.59` | 548,320.00 USD |
| `1H` | `Aster` | `45.58%` | `54.42%` | `0.84` | 153,560.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.24%` | `39.76%` | `1.52` | 68,760.00 USD |
| `1H` | `Whale Positions` | `50.83%` | `49.17%` | `1.03` | 12,710,000.00 USD |
| `1H` | `Global Accounts` | `47.33%` | `52.67%` | `0.90` | 39,400,000.00 USD |
| `4H` | `ADA` | `41.31%` | `58.69%` | `0.70` | 260,410,000.00 USD |
| `4H` | `Binance` | `39.43%` | `60.57%` | `0.65` | 165,910,000.00 USD |
| `4H` | `OKX` | `46.73%` | `53.27%` | `0.88` | 21,940,000.00 USD |
| `4H` | `Bybit` | `35.73%` | `64.27%` | `0.56` | 18,420,000.00 USD |
| `4H` | `KuCoin` | `48.2%` | `51.8%` | `0.93` | 3,240,000.00 USD |
| `4H` | `Gate` | `48.77%` | `51.23%` | `0.95` | 12,800,000.00 USD |
| `4H` | `Bitget` | `44.94%` | `55.06%` | `0.82` | 5,880,000.00 USD |
| `4H` | `BingX` | `46.54%` | `53.46%` | `0.87` | 5,120,000.00 USD |
| `4H` | `MEXC` | `53.07%` | `46.93%` | `1.13` | 3,050,000.00 USD |
| `4H` | `Bitunix` | `41.79%` | `58.21%` | `0.72` | 6,740,000.00 USD |
| `4H` | `Hyperliquid` | `50.54%` | `49.46%` | `1.02` | 6,260,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.6%` | `49.4%` | `1.02` | 2,190,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `2.85%` | `97.15%` | `0.03` | 2,290,000.00 USD |
| `4H` | `HTX` | `52.79%` | `47.21%` | `1.12` | 1,660,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `69.9%` | `30.1%` | `2.32` | 1,040,000.00 USD |
| `4H` | `Aster` | `47.85%` | `52.15%` | `0.92` | 2,470,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `65.9%` | `34.1%` | `1.93` | 1,420,000.00 USD |
| `4H` | `Whale Positions` | `39.43%` | `60.57%` | `0.65` | 165,910,000.00 USD |
| `4H` | `Global Accounts` | `41.31%` | `58.69%` | `0.70` | 260,410,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1928` | `0.1927` | `0.1928` | `0.1930` | `0.1923` | 1,200,311.82 USD | 545,374.62 USD | 654,937.20 USD | -109,562.58 USD | `-9.13%` | `0B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1925` | `0.1918` | 999,923.94 USD | 501,446.14 USD | 498,477.80 USD | 2,968.35 USD | `+0.30%` | `1B / 2S` |
| `5:00 UTC` | `0.1920` | `0.1923` | `0.1920` | `0.1930` | `0.1916` | 1,687,367.20 USD | 1,122,865.28 USD | 564,501.92 USD | 558,363.36 USD | `+33.09%` | `5B / 0S` |
| `0:00 UTC` | `0.1925` | `0.1926` | `0.1925` | `0.1930` | `0.1921` | 1,372,988.82 USD | 626,720.98 USD | 746,267.84 USD | -119,546.86 USD | `-8.71%` | `0B / 1S` |
| `5:00 UTC` | `0.1918` | `0.1920` | `0.1918` | `0.1925` | `0.1916` | 742,501.25 USD | 301,932.71 USD | 440,568.55 USD | -138,635.84 USD | `-18.67%` | `1B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1930` | `0.1915` | 1,936,754.49 USD | 922,725.13 USD | 1,014,029.36 USD | -91,304.23 USD | `-4.71%` | `1B / 3S` |
| `5:00 UTC` | `0.1925` | `0.1925` | `0.1925` | `0.1928` | `0.1920` | 818,438.28 USD | 477,644.62 USD | 340,793.66 USD | 136,850.96 USD | `+16.72%` | `0B / 0S` |
| `0:00 UTC` | `0.1928` | `0.1927` | `0.1928` | `0.1930` | `0.1925` | 1,279,303.19 USD | 647,276.72 USD | 632,026.47 USD | 15,250.26 USD | `+1.19%` | `0B / 0S` |
| `5:00 UTC` | `0.1926` | `0.1928` | `0.1926` | `0.1933` | `0.1925` | 1,103,210.95 USD | 609,025.54 USD | 494,185.40 USD | 114,840.14 USD | `+10.41%` | `1B / 0S` |
| `0:00 UTC` | `0.1935` | `0.1935` | `0.1935` | `0.1940` | `0.1926` | 1,263,104.63 USD | 757,421.64 USD | 505,682.99 USD | 251,738.65 USD | `+19.93%` | `3B / 0S` |

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
| `5m` | 10,270.00 USD | 209,350.00 USD | **`ACCUMULATION`** |
| `15m` | 55,210.00 USD | 361,890.00 USD | **`ACCUMULATION`** |
| `30m` | 68,200.00 USD | 520,760.00 USD | **`ACCUMULATION`** |
| `1h` | 35,030.00 USD | 740,980.00 USD | **`ACCUMULATION`** |
| `2h` | -117,820.00 USD | 1,080,000.00 USD | **`ACCUMULATION`** |
| `4h` | -418,970.00 USD | 453,210.00 USD | **`ACCUMULATION`** |
| `6h` | -121,240.00 USD | 1,040,000.00 USD | **`ACCUMULATION`** |
| `8h` | -143,730.00 USD | 2,260,000.00 USD | **`ACCUMULATION`** |
| `12h` | -3,570,000.00 USD | 66,970.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,530,000.00 USD | -8,440,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,890,000.00 USD | -39,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,390,000.00 USD | -196,970,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+10.27K` | 15m=`+55.21K` | 1h=`+35.03K` | 24h=`-8.53M`
* Futures Capital Netflows: 5m=`+209.35K` | 15m=`+361.89K` | 1h=`+740.98K` | 24h=`-8.44M`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1875` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1829` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1990`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1938` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1984` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1823`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1951`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
