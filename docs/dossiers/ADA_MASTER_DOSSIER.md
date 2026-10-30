# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1926` | **Live Ask Quote**: `0.1948` | **Mid Price**: `0.1937`
- **Spread Points**: `22.00` | **Spread BPS**: `113.58 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1882` | VWAP Z-Score: `+1.41` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.21` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1978` | Lower -3.00σ Band: `0.1785`
  * Upper +2.51σ Band: `0.1962` | Lower -2.51σ Band: `0.1801`
  * Upper +2.01σ Band: `0.1946` | Lower -2.01σ Band: `0.1817`
  * Upper +2.00σ Band: `0.1946` | Lower -2.00σ Band: `0.1818`
  * Upper +1.28σ Band: `0.1923` | Lower -1.28σ Band: `0.1841`
  * Upper +1.00σ Band: `0.1914` | Lower -1.00σ Band: `0.1850`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1916` | EMA-20=`0.1914` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1919` (Slope: `+0.0000`) | EMA-100=`0.1939`
  * Institutional Anchors: EMA-144=`0.1954` | EMA-200=`0.1971` (Slope: `-0.3731`) | EMA-233=`0.1977`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1938` (Distance: `-0.02%`)
  * Point of Control (POC) = `0.1912` (Distance: `+1.32%`)
  * Value Area Low (VAL) = `0.1876` (Distance: `+3.27%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `0.1929` - `0.1945`
  * Optimal Trade Entry (OTE 0.705): `0.1941`
  * Structural Invalidation Anchor (0.786): `0.1952`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1940` | `0.1941` | `0.1936` | `0.1938` | `1,996,686` | 387,177.19 USD | -21,937.72 USD | `-5.67%` | -4,807,455.69 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1938` | `0.1940` | `0.1935` | `0.1938` | `1,487,668` | 288,269.45 USD | 51,761.11 USD | `+17.96%` | -4,755,694.58 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1938` | `0.1940` | `0.1936` | `0.1939` | `911,335` | 176,588.81 USD | -9,040.61 USD | `-5.12%` | -4,764,735.20 USD | `-0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1926` | `0.1933` | `0.1924` | `0.1927` | `5,722,290` | 1,103,210.95 USD | 114,840.14 USD | `+10.41%` | -4,962,264.52 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1927` | `0.1941` | `0.1926` | `0.1938` | `8,976,737` | 1,737,432.33 USD | 227,430.57 USD | `+13.09%` | -4,734,833.95 USD | `+1.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1938` | `0.1940` | `0.1935` | `0.1939` | `2,399,003` | 464,858.26 USD | 42,720.50 USD | `+9.19%` | -4,692,113.45 USD | `+0.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1916` | `0.1924` | `26,112,684` | 5,023,010.35 USD | 493,681.90 USD | `+9.83%` | -4,879,718.95 USD | `+0.44` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1914` | `0.1926` | `25,331,850` | 4,870,682.84 USD | -212,635.97 USD | `-4.37%` | -5,092,354.92 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1927` | `0.1941` | `0.1924` | `0.1939` | `23,739,830` | 4,585,212.11 USD | 400,648.85 USD | `+8.74%` | -4,691,706.07 USD | `+0.42` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1941` | `0.1914` | `0.1939` | `75,207,279` | 14,483,348.52 USD | 686,138.00 USD | `+4.74%` | -4,217,503.70 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,207,439.06 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -4,361,461.60 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1941` | `0.1914` | `0.1939` | `75,207,279` | 14,483,348.52 USD | 686,138.00 USD | `+4.74%` | -4,217,503.70 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.1937`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `533` | `0x77ee...2902` | `SHORT` | 4,150,111.05 USD | `21,412,192.00` | `0.1911` | `0.1939` | `0.5941` | -58,859.31 USD | `-1.42%` | `10X Cross` |
| `1209` | `0x123d...3bff` | `LONG` | 1,822,404.64 USD | `9,392,870.00` | `0.2912` | `0.1939` | `0.000000` | -913,252.08 USD | `-50.11%` | `10X Cross` |
| `1249` | `0x7737...bf66` | `SHORT` | 1,762,107.94 USD | `9,091,466.00` | `0.2190` | `0.1939` | `2.13` | 228,881.86 USD | `+12.99%` | `10X Cross` |
| `1544` | `0x5f94...4b96` | `SHORT` | 1,389,704.56 USD | `7,162,318.00` | `0.2303` | `0.1939` | `0.7126` | 259,770.64 USD | `+18.69%` | `10X Cross` |
| `1777` | `0x4982...59e6` | `SHORT` | 1,162,929.69 USD | `5,998,812.00` | `0.1891` | `0.1939` | `0.4113` | -28,371.33 USD | `-2.44%` | `10X Cross` |
| `1827` | `0xcac1...26b3` | `LONG` | 1,125,555.56 USD | `5,803,927.00` | `0.2000` | `0.1939` | `0.000000` | -35,260.02 USD | `-3.13%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`0.2099` (Vol: 189,000.00 USD, Dist: `+8.37%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.50%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+8.03%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.52%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 325,500.00 USD, Dist: `+10.35%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--5.52%`)
  * 7D Horizon: Short MP=`0.2131` (Vol: 448,200.00 USD, Dist: `+10.03%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--5.44%`)
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
| `Live` | `Long Liquidation` | `0.1645` | 43,740.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 18,480.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1660` | 9,390,000.00 USD | 9,390,000.00 USD | 146,290.00 USD | 50,280.00 USD | 147,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1665` | 889.94 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1670` | 9,050,000.00 USD | 9,050,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1680` | 8,940,000.00 USD | 8,940,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1685` | 281.23 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1690` | 8,860,000.00 USD | 8,860,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1695` | 79,290.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1700` | 8,760,000.00 USD | 8,760,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1710` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 398,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1720` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 2,920.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 145,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 9,480,000.00 USD | 9,480,000.00 USD | 115,290.00 USD | 33,150.00 USD | 132,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1730` | 8,610,000.00 USD | 8,610,000.00 USD | 32,310.00 USD | 6,910.00 USD | 82,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 658.61 USD | 112,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 9,200,000.00 USD | 9,200,000.00 USD | 56,600.00 USD | 30,930.00 USD | 33,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1740` | 8,490,000.00 USD | 8,490,000.00 USD | 10,400.00 USD | 29,910.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1750` | 9,070,000.00 USD | 9,070,000.00 USD | 50,710.00 USD | 15,850.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1750` | 8,400,000.00 USD | 8,400,000.00 USD | 7,610.00 USD | 6,730.00 USD | 39,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 17,290.00 USD | 111,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 8,980,000.00 USD | 8,980,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1760` | 8,350,000.00 USD | 8,350,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 49,610.00 USD | 94,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 8,920,000.00 USD | 8,920,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1770` | 8,330,000.00 USD | 8,330,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 44,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 8,610,000.00 USD | 8,610,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1780` | 8,080,000.00 USD | 8,080,000.00 USD | 140,230.00 USD | 13,120.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 43,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 8,480,000.00 USD | 8,480,000.00 USD | 114,060.00 USD | 42,720.00 USD | 86,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 7,870,000.00 USD | 7,870,000.00 USD | 12,380.00 USD | 28,450.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 38,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 8,240,000.00 USD | 8,240,000.00 USD | 724,590.00 USD | 95,920.00 USD | 184,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 7,710,000.00 USD | 7,710,000.00 USD | 469,140.00 USD | 95,830.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 3,050.00 USD | 35,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 7,230,000.00 USD | 7,230,000.00 USD | 160,390.00 USD | 56,840.00 USD | 162,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 7,000,000.00 USD | 7,000,000.00 USD | 356,840.00 USD | 46,600.00 USD | 179,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 20,760.00 USD | 32,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 6,850,000.00 USD | 6,850,000.00 USD | 434,090.00 USD | 97,220.00 USD | 318,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 6,420,000.00 USD | 6,420,000.00 USD | 126,700.00 USD | 63,070.00 USD | 444,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 9,020.00 USD | 11,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 6,000,000.00 USD | 6,000,000.00 USD | 439,340.00 USD | 45,140.00 USD | 65,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 5,790,000.00 USD | 5,790,000.00 USD | 441,880.00 USD | 47,220.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1840` | 5,450,000.00 USD | 5,450,000.00 USD | 444,800.00 USD | 111,410.00 USD | 203,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 5,270,000.00 USD | 5,270,000.00 USD | 373,060.00 USD | 64,640.00 USD | 192,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,300.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 4,690,000.00 USD | 4,690,000.00 USD | 152,130.00 USD | 112,070.00 USD | 185,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 4,640,000.00 USD | 4,640,000.00 USD | 76,160.00 USD | 72,320.00 USD | 267,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 4,240,000.00 USD | 4,240,000.00 USD | 166,780.00 USD | 47,730.00 USD | 463,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 4,220,000.00 USD | 4,220,000.00 USD | 70,810.00 USD | 15,200.00 USD | 39,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 3,570,000.00 USD | 3,570,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 4,090,000.00 USD | 4,090,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 3,000,000.00 USD | 3,000,000.00 USD | 364,910.00 USD | 232,420.00 USD | 231,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 3,600,000.00 USD | 3,600,000.00 USD | 325,960.00 USD | 148,540.00 USD | 670,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 2,170,000.00 USD | 2,170,000.00 USD | 410,160.00 USD | 182,950.00 USD | 231,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 2,460,000.00 USD | 2,460,000.00 USD | 562,390.00 USD | 144,640.00 USD | 111,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,340,000.00 USD | 1,340,000.00 USD | 93,550.00 USD | 134,400.00 USD | 365,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 1,640,000.00 USD | 1,640,000.00 USD | 255,740.00 USD | 30,390.00 USD | 284,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 748,020.00 USD | 748,020.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 1,070,000.00 USD | 1,070,000.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 25,220.00 USD | 25,220.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 516,300.00 USD | 516,300.00 USD | 168,540.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1930` | 14,160.00 USD | 14,160.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 331,360.00 USD | 331,360.00 USD | 0.00 USD | 0.00 USD | 331,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 374,020.00 USD | 374,020.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 748,040.00 USD | 748,040.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 342,910.00 USD | 342,910.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 685,810.00 USD | 685,810.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 1,260,000.00 USD | 1,260,000.00 USD | 25,540.00 USD | 73,330.00 USD | 412,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1950` | 1,570,000.00 USD | 1,570,000.00 USD | 681,420.00 USD | 1,990.00 USD | 203,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 2,670,000.00 USD | 2,670,000.00 USD | 596,440.00 USD | 255,590.00 USD | 559,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 3,400,000.00 USD | 3,400,000.00 USD | 430,170.00 USD | 158,320.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 104.93 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 3,650,000.00 USD | 3,650,000.00 USD | 288,590.00 USD | 260,510.00 USD | 428,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1970` | 3,990,000.00 USD | 3,990,000.00 USD | 65,930.00 USD | 164,750.00 USD | 354,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 4,620,000.00 USD | 4,620,000.00 USD | 409,930.00 USD | 116,630.00 USD | 443,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1980` | 4,730,000.00 USD | 4,730,000.00 USD | 312,350.00 USD | 44,250.00 USD | 383,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 443.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 5,180,000.00 USD | 5,180,000.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1990` | 5,040,000.00 USD | 5,040,000.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 696.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 6,130,000.00 USD | 6,130,000.00 USD | 426,270.00 USD | 100,110.00 USD | 417,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2000` | 5,620,000.00 USD | 5,620,000.00 USD | 153,280.00 USD | 61,070.00 USD | 371,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 3,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 7,010,000.00 USD | 7,010,000.00 USD | 255,670.00 USD | 235,120.00 USD | 395,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 6,470,000.00 USD | 6,470,000.00 USD | 361,660.00 USD | 91,810.00 USD | 399,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 3,870.00 USD | 7,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 7,530,000.00 USD | 7,530,000.00 USD | 225,270.00 USD | 79,900.00 USD | 212,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 7,150,000.00 USD | 7,150,000.00 USD | 91,080.00 USD | 52,660.00 USD | 529,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 3,690.00 USD | 10,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 7,870,000.00 USD | 7,870,000.00 USD | 127,840.00 USD | 93,910.00 USD | 112,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 7,420,000.00 USD | 7,420,000.00 USD | 22,590.00 USD | 94,230.00 USD | 153,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2035` | 137.57 USD | 10,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2040` | 8,160,000.00 USD | 8,160,000.00 USD | 82,750.00 USD | 73,360.00 USD | 132,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 7,560,000.00 USD | 7,560,000.00 USD | 62,650.00 USD | 76,780.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 8,330,000.00 USD | 8,330,000.00 USD | 87,880.00 USD | 32,500.00 USD | 52,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 7,660,000.00 USD | 7,660,000.00 USD | 39,740.00 USD | 1,630.00 USD | 57,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 8,770,000.00 USD | 8,770,000.00 USD | 314,030.00 USD | 32,050.00 USD | 92,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 7,850,000.00 USD | 7,850,000.00 USD | 154,800.00 USD | 18,480.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2065` | 214.55 USD | 11,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2070` | 9,230,000.00 USD | 9,230,000.00 USD | 195,950.00 USD | 81,580.00 USD | 181,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 8,470,000.00 USD | 8,470,000.00 USD | 441,660.00 USD | 141,790.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 9,560,000.00 USD | 9,560,000.00 USD | 217,370.00 USD | 70,470.00 USD | 42,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 9,150,000.00 USD | 9,150,000.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 10,470,000.00 USD | 10,470,000.00 USD | 484,690.00 USD | 147,490.00 USD | 283,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 12,100,000.00 USD | 12,100,000.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 11,240,000.00 USD | 11,240,000.00 USD | 456,330.00 USD | 102,230.00 USD | 210,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 16,180,000.00 USD | 16,180,000.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2105` | 218.71 USD | 11,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2110` | 11,580,000.00 USD | 11,580,000.00 USD | 157,970.00 USD | 48,270.00 USD | 129,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 19,400,000.00 USD | 19,400,000.00 USD | 1,090,000.00 USD | 518,310.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 12,000,000.00 USD | 12,000,000.00 USD | 164,340.00 USD | 100,480.00 USD | 158,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 22,450,000.00 USD | 22,450,000.00 USD | 1,170,000.00 USD | 492,740.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 153.21 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 12,370,000.00 USD | 12,370,000.00 USD | 206,790.00 USD | 58,700.00 USD | 101,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 25,290,000.00 USD | 25,290,000.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 12,550,000.00 USD | 12,550,000.00 USD | 130,000.00 USD | 26,610.00 USD | 25,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 27,390,000.00 USD | 27,390,000.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 29,650,000.00 USD | 29,650,000.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 467.20 USD | 12,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2160` | 30,630,000.00 USD | 30,630,000.00 USD | 467,380.00 USD | 144,820.00 USD | 370,160.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.1660` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 146,290.00 USD | 50,280.00 USD | 147,910.00 USD |
| `7D` | `0.1670` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD |
| `7D` | `0.1680` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD |
| `7D` | `0.1690` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD |
| `7D` | `0.1700` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD |
| `7D` | `0.1710` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD |
| `7D` | `0.1720` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 0.00 USD | 2,920.00 USD | 41,020.00 USD |
| `1D` | `0.1730` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 115,290.00 USD | 33,150.00 USD | 132,970.00 USD |
| `7D` | `0.1730` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 32,310.00 USD | 6,910.00 USD | 82,340.00 USD |
| `1D` | `0.1740` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 56,600.00 USD | 30,930.00 USD | 33,020.00 USD |
| `7D` | `0.1740` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 10,400.00 USD | 29,910.00 USD | 48,080.00 USD |
| `1D` | `0.1750` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 50,710.00 USD | 15,850.00 USD | 28,060.00 USD |
| `7D` | `0.1750` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 7,610.00 USD | 6,730.00 USD | 39,280.00 USD |
| `1D` | `0.1760` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD |
| `7D` | `0.1760` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD |
| `1D` | `0.1770` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD |
| `7D` | `0.1770` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD |
| `1D` | `0.1780` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD |
| `7D` | `0.1780` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 140,230.00 USD | 13,120.00 USD | 56,120.00 USD |
| `1D` | `0.1790` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 114,060.00 USD | 42,720.00 USD | 86,800.00 USD |
| `7D` | `0.1790` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 12,380.00 USD | 28,450.00 USD | 116,120.00 USD |
| `1D` | `0.1800` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 724,590.00 USD | 95,920.00 USD | 184,640.00 USD |
| `7D` | `0.1800` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 469,140.00 USD | 95,830.00 USD | 141,980.00 USD |
| `1D` | `0.1810` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 160,390.00 USD | 56,840.00 USD | 162,920.00 USD |
| `7D` | `0.1810` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 356,840.00 USD | 46,600.00 USD | 179,050.00 USD |
| `1D` | `0.1820` | 6,850,000.00 USD | 0.00 USD | 6,850,000.00 USD | 434,090.00 USD | 97,220.00 USD | 318,680.00 USD |
| `7D` | `0.1820` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 126,700.00 USD | 63,070.00 USD | 444,200.00 USD |
| `1D` | `0.1830` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 439,340.00 USD | 45,140.00 USD | 65,230.00 USD |
| `7D` | `0.1830` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 441,880.00 USD | 47,220.00 USD | 32,460.00 USD |
| `1D` | `0.1840` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 444,800.00 USD | 111,410.00 USD | 203,410.00 USD |
| `7D` | `0.1840` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 373,060.00 USD | 64,640.00 USD | 192,770.00 USD |
| `1D` | `0.1850` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 152,130.00 USD | 112,070.00 USD | 185,290.00 USD |
| `7D` | `0.1850` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 76,160.00 USD | 72,320.00 USD | 267,580.00 USD |
| `1D` | `0.1860` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 166,780.00 USD | 47,730.00 USD | 463,660.00 USD |
| `7D` | `0.1860` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 70,810.00 USD | 15,200.00 USD | 39,200.00 USD |
| `1D` | `0.1870` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD |
| `7D` | `0.1870` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD |
| `1D` | `0.1880` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 364,910.00 USD | 232,420.00 USD | 231,940.00 USD |
| `7D` | `0.1880` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 325,960.00 USD | 148,540.00 USD | 670,720.00 USD |
| `1D` | `0.1890` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 410,160.00 USD | 182,950.00 USD | 231,740.00 USD |
| `7D` | `0.1890` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 562,390.00 USD | 144,640.00 USD | 111,430.00 USD |
| `1D` | `0.1900` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 93,550.00 USD | 134,400.00 USD | 365,080.00 USD |
| `7D` | `0.1900` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 255,740.00 USD | 30,390.00 USD | 284,570.00 USD |
| `1D` | `0.1910` | 748,020.00 USD | 0.00 USD | 748,020.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD |
| `7D` | `0.1910` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD |
| `1D` | `0.1920` | 25,220.00 USD | 0.00 USD | 25,220.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD |
| `7D` | `0.1920` | 516,300.00 USD | 0.00 USD | 516,300.00 USD | 168,540.00 USD | 0.00 USD | 16,400.00 USD |
| `1D` | `0.1930` | 14,160.00 USD | 0.00 USD | 14,160.00 USD | 0.00 USD | 2,420.00 USD | 11,740.00 USD |
| `7D` | `0.1930` | 331,360.00 USD | 0.00 USD | 331,360.00 USD | 0.00 USD | 0.00 USD | 331,360.00 USD |
| `1D` | `0.1940` | 374,020.00 USD | 374,020.00 USD | 0.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD |
| `1D` | `0.1940` | 748,040.00 USD | 748,040.00 USD | 0.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD |
| `7D` | `0.1940` | 342,910.00 USD | 342,910.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `7D` | `0.1940` | 685,810.00 USD | 685,810.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `1D` | `0.1950` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 25,540.00 USD | 73,330.00 USD | 412,450.00 USD |
| `7D` | `0.1950` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 681,420.00 USD | 1,990.00 USD | 203,120.00 USD |
| `1D` | `0.1960` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 596,440.00 USD | 255,590.00 USD | 559,330.00 USD |
| `7D` | `0.1960` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 430,170.00 USD | 158,320.00 USD | 1,240,000.00 USD |
| `1D` | `0.1970` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 288,590.00 USD | 260,510.00 USD | 428,920.00 USD |
| `7D` | `0.1970` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 65,930.00 USD | 164,750.00 USD | 354,550.00 USD |
| `1D` | `0.1980` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 409,930.00 USD | 116,630.00 USD | 443,860.00 USD |
| `7D` | `0.1980` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 312,350.00 USD | 44,250.00 USD | 383,190.00 USD |
| `1D` | `0.1990` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD |
| `7D` | `0.1990` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD |
| `1D` | `0.2000` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 426,270.00 USD | 100,110.00 USD | 417,810.00 USD |
| `7D` | `0.2000` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 153,280.00 USD | 61,070.00 USD | 371,130.00 USD |
| `1D` | `0.2010` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 255,670.00 USD | 235,120.00 USD | 395,170.00 USD |
| `7D` | `0.2010` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 361,660.00 USD | 91,810.00 USD | 399,110.00 USD |
| `1D` | `0.2020` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 225,270.00 USD | 79,900.00 USD | 212,060.00 USD |
| `7D` | `0.2020` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 91,080.00 USD | 52,660.00 USD | 529,150.00 USD |
| `1D` | `0.2030` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 127,840.00 USD | 93,910.00 USD | 112,940.00 USD |
| `7D` | `0.2030` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 22,590.00 USD | 94,230.00 USD | 153,910.00 USD |
| `1D` | `0.2040` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 82,750.00 USD | 73,360.00 USD | 132,510.00 USD |
| `7D` | `0.2040` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 62,650.00 USD | 76,780.00 USD | 6,560.00 USD |
| `1D` | `0.2050` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 87,880.00 USD | 32,500.00 USD | 52,620.00 USD |
| `7D` | `0.2050` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 39,740.00 USD | 1,630.00 USD | 57,550.00 USD |
| `1D` | `0.2060` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 314,030.00 USD | 32,050.00 USD | 92,350.00 USD |
| `7D` | `0.2060` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 154,800.00 USD | 18,480.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 195,950.00 USD | 81,580.00 USD | 181,570.00 USD |
| `7D` | `0.2070` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 441,660.00 USD | 141,790.00 USD | 35,600.00 USD |
| `1D` | `0.2080` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 217,370.00 USD | 70,470.00 USD | 42,310.00 USD |
| `7D` | `0.2080` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD |
| `1D` | `0.2090` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 484,690.00 USD | 147,490.00 USD | 283,500.00 USD |
| `7D` | `0.2090` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD |
| `1D` | `0.2100` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 456,330.00 USD | 102,230.00 USD | 210,050.00 USD |
| `7D` | `0.2100` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD |
| `1D` | `0.2110` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 157,970.00 USD | 48,270.00 USD | 129,000.00 USD |
| `7D` | `0.2110` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 1,090,000.00 USD | 518,310.00 USD | 1,620,000.00 USD |
| `1D` | `0.2120` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 164,340.00 USD | 100,480.00 USD | 158,760.00 USD |
| `7D` | `0.2120` | 22,450,000.00 USD | 22,450,000.00 USD | 0.00 USD | 1,170,000.00 USD | 492,740.00 USD | 1,390,000.00 USD |
| `1D` | `0.2130` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 206,790.00 USD | 58,700.00 USD | 101,580.00 USD |
| `7D` | `0.2130` | 25,290,000.00 USD | 25,290,000.00 USD | 0.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,260,000.00 USD |
| `1D` | `0.2140` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 130,000.00 USD | 26,610.00 USD | 25,900.00 USD |
| `7D` | `0.2140` | 27,390,000.00 USD | 27,390,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD |
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
  * Total Open Interest: `414.61M` | Total OI Tokens: `2,131,028,461.5 ADA`
  * 1h OI Change: `+0.89%` | 4h OI Change: `+0.38%` | 24h OI Change: `-7.52%`
  * Exchange Breakdown: Binance=`75.40M` | Bybit=`50.32M` | OKX=`29.63M` | Hyperliquid=`28.29M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.77K` | Last 24h: `30.56K` | Last 3d: `64.45K` | Last 7d: `83.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0053%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0089%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `47.25%` | `52.75%` | `0.90` | 10,370,000.00 USD |
| `15M` | `Binance` | `45.92%` | `54.08%` | `0.85` | 3,620,000.00 USD |
| `15M` | `OKX` | `57.55%` | `42.45%` | `1.36` | 2,070,000.00 USD |
| `15M` | `Bybit` | `51.28%` | `48.72%` | `1.05` | 768,980.00 USD |
| `15M` | `KuCoin` | `47.92%` | `52.08%` | `0.92` | 26,900.00 USD |
| `15M` | `Gate` | `45.29%` | `54.71%` | `0.83` | 1,840,000.00 USD |
| `15M` | `Bitget` | `59.24%` | `40.76%` | `1.45` | 108,800.00 USD |
| `15M` | `BingX` | `53.89%` | `46.11%` | `1.17` | 177,310.00 USD |
| `15M` | `MEXC` | `54.19%` | `45.81%` | `1.18` | 264,160.00 USD |
| `15M` | `Bitunix` | `44.39%` | `55.61%` | `0.80` | 261,780.00 USD |
| `15M` | `Hyperliquid` | `84.1%` | `15.9%` | `5.29` | 294,740.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `59.7%` | `40.3%` | `1.48` | 58,090.00 USD |
| `15M` | `Crypto.com` | `54%` | `46%` | `1.17` | 20,340.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 698,250.00 USD |
| `15M` | `HTX` | `55.53%` | `44.47%` | `1.25` | 91,220.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `54.91%` | `45.09%` | `1.22` | 36,870.00 USD |
| `15M` | `Aster` | `64.13%` | `35.87%` | `1.79` | 40,600.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.61%` | `46.39%` | `1.16` | 1,270.00 USD |
| `15M` | `Whale Positions` | `45.92%` | `54.08%` | `0.85` | 3,620,000.00 USD |
| `15M` | `Global Accounts` | `47.25%` | `52.75%` | `0.90` | 10,370,000.00 USD |
| `1H` | `ADA` | `45.77%` | `54.23%` | `0.84` | 57,280,000.00 USD |
| `1H` | `Binance` | `42.74%` | `57.26%` | `0.75` | 33,270,000.00 USD |
| `1H` | `OKX` | `57.38%` | `42.62%` | `1.35` | 6,010,000.00 USD |
| `1H` | `Bybit` | `44.65%` | `55.35%` | `0.81` | 4,790,000.00 USD |
| `1H` | `KuCoin` | `50.96%` | `49.04%` | `1.04` | 687,290.00 USD |
| `1H` | `Gate` | `53.01%` | `46.99%` | `1.13` | 2,770,000.00 USD |
| `1H` | `Bitget` | `55.83%` | `44.17%` | `1.26` | 816,010.00 USD |
| `1H` | `BingX` | `57.94%` | `42.06%` | `1.38` | 1,230,000.00 USD |
| `1H` | `MEXC` | `58.75%` | `41.25%` | `1.42` | 769,860.00 USD |
| `1H` | `Bitunix` | `35.7%` | `64.3%` | `0.56` | 2,100,000.00 USD |
| `1H` | `Hyperliquid` | `56.99%` | `43.01%` | `1.33` | 2,090,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.34%` | `50.66%` | `0.97` | 446,480.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `9.38%` | `90.62%` | `0.10` | 650,700.00 USD |
| `1H` | `HTX` | `34.81%` | `65.19%` | `0.53` | 405,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `65.3%` | `34.7%` | `1.88` | 140,220.00 USD |
| `1H` | `Aster` | `45.22%` | `54.78%` | `0.83` | 775,390.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.99%` | `49.01%` | `1.04` | 337,200.00 USD |
| `1H` | `Whale Positions` | `42.74%` | `57.26%` | `0.75` | 33,270,000.00 USD |
| `1H` | `Global Accounts` | `45.77%` | `54.23%` | `0.84` | 57,280,000.00 USD |
| `4H` | `ADA` | `44.31%` | `55.69%` | `0.80` | 167,170,000.00 USD |
| `4H` | `Binance` | `44.76%` | `55.24%` | `0.81` | 59,410,000.00 USD |
| `4H` | `OKX` | `47.75%` | `52.25%` | `0.91` | 34,080,000.00 USD |
| `4H` | `Bybit` | `42.24%` | `57.76%` | `0.73` | 11,670,000.00 USD |
| `4H` | `KuCoin` | `45.01%` | `54.99%` | `0.82` | 1,180,000.00 USD |
| `4H` | `Gate` | `46.06%` | `53.94%` | `0.85` | 28,770,000.00 USD |
| `4H` | `Bitget` | `45.43%` | `54.57%` | `0.83` | 2,420,000.00 USD |
| `4H` | `BingX` | `32.95%` | `67.05%` | `0.49` | 3,270,000.00 USD |
| `4H` | `MEXC` | `47.27%` | `52.73%` | `0.90` | 8,500,000.00 USD |
| `4H` | `Bitunix` | `46.46%` | `53.54%` | `0.87` | 4,050,000.00 USD |
| `4H` | `Hyperliquid` | `70.8%` | `29.2%` | `2.42` | 2,070,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.11%` | `48.89%` | `1.05` | 1,130,000.00 USD |
| `4H` | `Crypto.com` | `39.98%` | `60.02%` | `0.67` | 233,950.00 USD |
| `4H` | `WhiteBIT` | `11.56%` | `88.44%` | `0.13` | 7,460,000.00 USD |
| `4H` | `HTX` | `50.18%` | `49.82%` | `1.01` | 970,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `56.13%` | `43.87%` | `1.28` | 1,000,000.00 USD |
| `4H` | `Aster` | `37.64%` | `62.36%` | `0.60` | 870,870.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `62.02%` | `37.98%` | `1.63` | 92,380.00 USD |
| `4H` | `Whale Positions` | `44.76%` | `55.24%` | `0.81` | 59,410,000.00 USD |
| `4H` | `Global Accounts` | `44.31%` | `55.69%` | `0.80` | 167,170,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1925` | `0.1918` | 999,923.94 USD | 501,446.14 USD | 498,477.80 USD | 2,968.35 USD | `+0.30%` | `1B / 2S` |
| `5:00 UTC` | `0.1920` | `0.1923` | `0.1920` | `0.1930` | `0.1916` | 1,687,367.20 USD | 1,122,865.28 USD | 564,501.92 USD | 558,363.36 USD | `+33.09%` | `5B / 0S` |
| `0:00 UTC` | `0.1925` | `0.1926` | `0.1925` | `0.1930` | `0.1921` | 1,372,988.82 USD | 626,720.98 USD | 746,267.84 USD | -119,546.86 USD | `-8.71%` | `0B / 1S` |
| `5:00 UTC` | `0.1918` | `0.1920` | `0.1918` | `0.1925` | `0.1916` | 742,501.25 USD | 301,932.71 USD | 440,568.55 USD | -138,635.84 USD | `-18.67%` | `1B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1930` | `0.1915` | 1,936,754.49 USD | 922,725.13 USD | 1,014,029.36 USD | -91,304.23 USD | `-4.71%` | `1B / 3S` |
| `5:00 UTC` | `0.1925` | `0.1925` | `0.1925` | `0.1928` | `0.1920` | 818,438.28 USD | 477,644.62 USD | 340,793.66 USD | 136,850.96 USD | `+16.72%` | `0B / 0S` |
| `0:00 UTC` | `0.1928` | `0.1927` | `0.1928` | `0.1930` | `0.1925` | 1,279,303.19 USD | 647,276.72 USD | 632,026.47 USD | 15,250.26 USD | `+1.19%` | `0B / 0S` |
| `5:00 UTC` | `0.1926` | `0.1928` | `0.1926` | `0.1933` | `0.1925` | 1,103,210.95 USD | 609,025.54 USD | 494,185.40 USD | 114,840.14 USD | `+10.41%` | `1B / 0S` |
| `0:00 UTC` | `0.1935` | `0.1936` | `0.1935` | `0.1941` | `0.1926` | 1,737,432.33 USD | 982,431.45 USD | 755,000.88 USD | 227,430.57 USD | `+13.09%` | `2B / 0S` |
| `5:00 UTC` | `0.1938` | `0.1938` | `0.1938` | `0.1941` | `0.1935` | 269,608.32 USD | 169,248.01 USD | 100,360.31 USD | 68,887.70 USD | `+25.55%` | `1B / 0S` |

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
| `5m` | 123,530.00 USD | 198,780.00 USD | **`ACCUMULATION`** |
| `15m` | 231,830.00 USD | 470,080.00 USD | **`ACCUMULATION`** |
| `30m` | 450,170.00 USD | 1,020,000.00 USD | **`ACCUMULATION`** |
| `1h` | 522,080.00 USD | 1,290,000.00 USD | **`ACCUMULATION`** |
| `2h` | 478,410.00 USD | 1,480,000.00 USD | **`ACCUMULATION`** |
| `4h` | 70,330.00 USD | 1,080,000.00 USD | **`ACCUMULATION`** |
| `6h` | 348,810.00 USD | 1,130,000.00 USD | **`ACCUMULATION`** |
| `8h` | 264,070.00 USD | 3,290,000.00 USD | **`ACCUMULATION`** |
| `12h` | -2,980,000.00 USD | 837,170.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,260,000.00 USD | -9,060,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,340,000.00 USD | -38,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,920,000.00 USD | -196,390,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+123.53K` | 15m=`+231.83K` | 1h=`+522.08K` | 24h=`-8.26M`
* Futures Capital Netflows: 5m=`+198.78K` | 15m=`+470.08K` | 1h=`+1.29M` | 24h=`-9.06M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1876` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1830` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1991`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1938` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1984` (Risk Distance: `0.0046` pts)
  * +2.5R Take Profit: `0.1823`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1952`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
