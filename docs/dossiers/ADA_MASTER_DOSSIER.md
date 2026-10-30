# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:24:07 IST` (`2026-10-30 09:54:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1911` | **Live Ask Quote**: `0.1932` | **Mid Price**: `0.1921`
- **Spread Points**: `21.00` | **Spread BPS**: `109.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1879` | VWAP Z-Score: `+1.06` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.24` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1974` | Lower -3.00σ Band: `0.1784`
  * Upper +2.51σ Band: `0.1959` | Lower -2.51σ Band: `0.1800`
  * Upper +2.01σ Band: `0.1943` | Lower -2.01σ Band: `0.1815`
  * Upper +2.00σ Band: `0.1943` | Lower -2.00σ Band: `0.1816`
  * Upper +1.28σ Band: `0.1920` | Lower -1.28σ Band: `0.1839`
  * Upper +1.00σ Band: `0.1911` | Lower -1.00σ Band: `0.1847`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1912` | EMA-20=`0.1913` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1919` (Slope: `+0.0000`) | EMA-100=`0.1941`
  * Institutional Anchors: EMA-144=`0.1956` | EMA-200=`0.1972` (Slope: `-0.3795`) | EMA-233=`0.1979`
- **Range Boundaries**: 24H High=`0.2074` | 24H Low=`0.1808` | Weekly High=`0.2086` | Weekly Low=`0.1808`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1938` (Distance: `-0.79%`)
  * Point of Control (POC) = `0.1912` (Distance: `+0.53%`)
  * Value Area Low (VAL) = `0.1872` (Distance: `+2.71%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2065` | Weekly POC=`0.2031` | Weekly VAL=`0.1983`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1940` | Low=`0.1902`
  * New York Session (13:00-21:00 UTC): High=`0.1933` | Low=`0.1910`
  * Initial Balance (First Hour): IB High=`0.1935` | IB Low=`0.1918`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1914` - `0.1929`
  * Optimal Trade Entry (OTE 0.705): `0.1925`
  * Structural Invalidation Anchor (0.786): `0.1937`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1927` | `0.1929` | `0.1922` | `0.1926` | `1,461,580` | 281,436.09 USD | -32,787.05 USD | `-11.65%` | -5,096,286.33 USD | `-0.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1925` | `0.1925` | `0.1919` | `0.1923` | `1,204,013` | 231,454.28 USD | -37,236.74 USD | `-16.09%` | -5,133,523.08 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1923` | `0.1924` | `0.1923` | `0.1923` | `12,305` | 2,366.34 USD | -2,042.72 USD | `-86.32%` | -5,135,565.80 USD | `-0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.1922` | `0.1924` | `0.1916` | `0.1918` | `3,868,318` | 742,501.25 USD | -138,635.84 USD | `-18.67%` | -5,027,075.67 USD | `-0.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1919` | `0.1929` | `0.1914` | `0.1926` | `10,078,974` | 1,936,754.49 USD | -91,304.23 USD | `-4.71%` | -5,118,379.90 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1925` | `0.1925` | `0.1919` | `0.1923` | `1,216,318` | 233,820.61 USD | -39,279.46 USD | `-16.80%` | -5,157,659.36 USD | `-0.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1943` | `0.1944` | `0.1919` | `0.1924` | `27,579,785` | 5,322,908.18 USD | -465,649.66 USD | `-8.75%` | -5,262,574.87 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1916` | `0.1924` | `26,112,684` | 5,023,010.35 USD | 493,681.90 USD | `+9.83%` | -4,768,892.97 USD | `+0.44` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1914` | `0.1923` | `22,349,956` | 4,296,582.43 USD | -381,541.66 USD | `-8.88%` | -5,150,434.63 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1930` | `0.1914` | `0.1923` | `48,421,750` | 9,311,729.64 USD | 104,277.09 USD | `+1.12%` | -4,799,364.61 USD | `+0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,207,439.06 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -4,361,461.60 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1930` | `0.1914` | `0.1923` | `48,421,750` | 9,311,729.64 USD | 104,277.09 USD | `+1.12%` | -4,799,364.61 USD | `+0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.1921`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `535` | `0x77ee...2902` | `SHORT` | 4,116,493.91 USD | `21,412,192.00` | `0.1911` | `0.1923` | `0.6009` | -25,242.17 USD | `-0.61%` | `10X Cross` |
| `1220` | `0x123d...3bff` | `LONG` | 1,806,624.62 USD | `9,392,870.00` | `0.2912` | `0.1923` | `0.000000` | -929,032.10 USD | `-51.42%` | `10X Cross` |
| `1253` | `0x7737...bf66` | `SHORT` | 1,748,470.74 USD | `9,091,466.00` | `0.2190` | `0.1923` | `2.15` | 242,519.06 USD | `+13.87%` | `10X Cross` |
| `1549` | `0x5f94...4b96` | `SHORT` | 1,377,528.62 USD | `7,162,318.00` | `0.2303` | `0.1923` | `0.7015` | 271,946.58 USD | `+19.74%` | `10X Cross` |
| `1789` | `0x4982...59e6` | `SHORT` | 1,153,151.63 USD | `5,998,812.00` | `0.1891` | `0.1923` | `0.4137` | -18,593.27 USD | `-1.61%` | `10X Cross` |
| `1836` | `0xcac1...26b3` | `LONG` | 1,115,746.93 USD | `5,803,927.00` | `0.2000` | `0.1923` | `0.000000` | -45,068.66 USD | `-4.04%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1999` | 5,011.50 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.01K USD at 0.1999 USD [API] | `2026-10-29 09:25:32` |
| `ANNOUNCEMENT` | `INFO` | `0.1999` | 5,009.99 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 5.01K USD at 0.1999 USD [API] | `2026-10-29 09:25:14` |
| `ANNOUNCEMENT` | `INFO` | `0.1994` | 6,650.46 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.1994 USD [API] | `2026-10-29 09:34:07` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2099` (Vol: 189,000.00 USD, Dist: `+9.11%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.86%`)
  * 48H Horizon: Short MP=`0.2092` (Vol: 207,000.00 USD, Dist: `+8.76%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.89%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 325,500.00 USD, Dist: `+11.10%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.89%`)
  * 7D Horizon: Short MP=`0.2131` (Vol: 448,200.00 USD, Dist: `+10.77%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--4.80%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0395` | 210.42 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 823.53 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 242.88 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 103.16 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 2,690.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 137.71 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 555.91 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 2,020.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 181.31 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 228.96 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 7,510.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 1,160.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 581.25 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 154,580.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 3,570.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 13,120.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,270.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 87,280.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,280.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 2,090.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 150.44 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 2,200.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 420.22 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 430.44 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 25,870.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 365.90 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,150.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,640.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 7,570.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 1,180.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 2,420.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 529.68 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 8,970.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 26,900.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 403.77 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 314.44 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,540.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 958.46 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,990.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 3,770.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 4,210.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 1,360.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,720.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,830.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 2,350.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 42,630.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,250.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 11,530.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 819.16 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 703,200.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 2,780.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,580.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 4,200.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,180.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,040.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1640` | 8,340,000.00 USD | 8,340,000.00 USD | 166,770.00 USD | 55,610.00 USD | 217,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,840.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1650` | 7,900,000.00 USD | 7,900,000.00 USD | 57,340.00 USD | 18,500.00 USD | 42,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 6,810.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1660` | 7,780,000.00 USD | 7,780,000.00 USD | 88,950.00 USD | 31,770.00 USD | 105,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1665` | 889.94 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1670` | 7,550,000.00 USD | 7,550,000.00 USD | 50,670.00 USD | 2,500.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1680` | 7,450,000.00 USD | 7,450,000.00 USD | 66,390.00 USD | 2,720.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1685` | 12,160.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1690` | 7,370,000.00 USD | 7,370,000.00 USD | 70,950.00 USD | 17,160.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1695` | 79,290.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1700` | 7,270,000.00 USD | 7,270,000.00 USD | 3,140.00 USD | 5,040.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1710` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 2,350.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 394,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1720` | 7,170,000.00 USD | 7,170,000.00 USD | 9,500.00 USD | 2,920.00 USD | 41,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 142,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 8,810,000.00 USD | 8,810,000.00 USD | 110,770.00 USD | 33,130.00 USD | 132,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1730` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 332.90 USD | 82,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 658.61 USD | 108,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 8,540,000.00 USD | 8,540,000.00 USD | 33,860.00 USD | 15,040.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1740` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 3,560.00 USD | 32,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1750` | 8,460,000.00 USD | 8,460,000.00 USD | 50,710.00 USD | 15,820.00 USD | 14,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1750` | 7,000,000.00 USD | 7,000,000.00 USD | 7,610.00 USD | 6,730.00 USD | 25,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 17,290.00 USD | 107,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 8,380,000.00 USD | 8,380,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1760` | 6,960,000.00 USD | 6,960,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 50,680.00 USD | 90,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 8,320,000.00 USD | 8,320,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1770` | 6,940,000.00 USD | 6,940,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 8,010,000.00 USD | 8,010,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1780` | 6,680,000.00 USD | 6,680,000.00 USD | 140,230.00 USD | 12,660.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 38,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 7,880,000.00 USD | 7,880,000.00 USD | 114,490.00 USD | 48,320.00 USD | 90,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 6,470,000.00 USD | 6,470,000.00 USD | 9,850.00 USD | 27,990.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 34,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 7,630,000.00 USD | 7,630,000.00 USD | 746,750.00 USD | 99,750.00 USD | 184,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 6,320,000.00 USD | 6,320,000.00 USD | 464,090.00 USD | 95,830.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 3,050.00 USD | 30,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 6,600,000.00 USD | 6,600,000.00 USD | 160,390.00 USD | 59,240.00 USD | 169,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 5,620,000.00 USD | 5,620,000.00 USD | 354,390.00 USD | 45,990.00 USD | 179,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 4,070.00 USD | 27,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 6,210,000.00 USD | 6,210,000.00 USD | 433,390.00 USD | 96,490.00 USD | 318,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 5,040,000.00 USD | 5,040,000.00 USD | 123,330.00 USD | 62,450.00 USD | 444,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 20,830.00 USD | 23,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 5,360,000.00 USD | 5,360,000.00 USD | 436,700.00 USD | 44,980.00 USD | 65,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 4,410,000.00 USD | 4,410,000.00 USD | 435,140.00 USD | 47,220.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1835` | 170.10 USD | 170.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 4,820,000.00 USD | 4,820,000.00 USD | 434,390.00 USD | 111,320.00 USD | 199,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 3,890,000.00 USD | 3,890,000.00 USD | 273,040.00 USD | 41,950.00 USD | 192,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,300.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 4,070,000.00 USD | 4,070,000.00 USD | 85,970.00 USD | 46,150.00 USD | 159,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 3,380,000.00 USD | 3,380,000.00 USD | 50,160.00 USD | 6,440.00 USD | 228,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 3,780,000.00 USD | 3,780,000.00 USD | 168,220.00 USD | 44,670.00 USD | 430,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 3,100,000.00 USD | 3,100,000.00 USD | 70,810.00 USD | 15,200.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 3,130,000.00 USD | 3,130,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 3,010,000.00 USD | 3,010,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 2,560,000.00 USD | 2,560,000.00 USD | 344,090.00 USD | 232,420.00 USD | 224,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 2,520,000.00 USD | 2,520,000.00 USD | 132,450.00 USD | 103,170.00 USD | 670,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 1,760,000.00 USD | 1,760,000.00 USD | 277,850.00 USD | 51,110.00 USD | 179,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 1,610,000.00 USD | 1,610,000.00 USD | 510,390.00 USD | 12,880.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1895` | 280.27 USD | 450.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,250,000.00 USD | 1,250,000.00 USD | 93,550.00 USD | 128,280.00 USD | 299,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 1,060,000.00 USD | 1,060,000.00 USD | 255,740.00 USD | 30,390.00 USD | 216,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 733,850.00 USD | 733,850.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 553,650.00 USD | 553,650.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 11,060.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 600,250.00 USD | 600,250.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 1,200,000.00 USD | 1,200,000.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 457,320.00 USD | 457,320.00 USD | 284,520.00 USD | 2,420.00 USD | 170,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 914,650.00 USD | 914,650.00 USD | 284,520.00 USD | 2,420.00 USD | 170,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1930` | 2,180,000.00 USD | 2,180,000.00 USD | 653,060.00 USD | 0.00 USD | 331,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 1,290,000.00 USD | 1,290,000.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 2,530,000.00 USD | 2,530,000.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 288.05 USD | 738.43 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1950` | 1,800,000.00 USD | 1,800,000.00 USD | 25,540.00 USD | 73,330.00 USD | 412,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1950` | 3,430,000.00 USD | 3,430,000.00 USD | 693,070.00 USD | 1,990.00 USD | 203,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 3,210,000.00 USD | 3,210,000.00 USD | 575,620.00 USD | 280,100.00 USD | 552,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 5,020,000.00 USD | 5,020,000.00 USD | 236,660.00 USD | 112,940.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 843.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 3,870,000.00 USD | 3,870,000.00 USD | 156,270.00 USD | 128,680.00 USD | 376,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1970` | 5,340,000.00 USD | 5,340,000.00 USD | 13,930.00 USD | 32,990.00 USD | 275,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 4,770,000.00 USD | 4,770,000.00 USD | 409,930.00 USD | 110,510.00 USD | 378,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1980` | 6,010,000.00 USD | 6,010,000.00 USD | 312,350.00 USD | 44,250.00 USD | 315,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 1,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 5,330,000.00 USD | 5,330,000.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1990` | 6,320,000.00 USD | 6,320,000.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 1,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 6,260,000.00 USD | 6,260,000.00 USD | 415,860.00 USD | 100,110.00 USD | 414,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2000` | 6,790,000.00 USD | 6,790,000.00 USD | 56,530.00 USD | 38,390.00 USD | 371,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 4,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 6,990,000.00 USD | 6,990,000.00 USD | 189,510.00 USD | 169,210.00 USD | 368,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 7,510,000.00 USD | 7,510,000.00 USD | 335,650.00 USD | 25,310.00 USD | 359,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 2,100.00 USD | 6,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 7,470,000.00 USD | 7,470,000.00 USD | 224,560.00 USD | 76,110.00 USD | 179,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 8,140,000.00 USD | 8,140,000.00 USD | 87,710.00 USD | 52,030.00 USD | 495,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 20,050.00 USD | 26,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 7,820,000.00 USD | 7,820,000.00 USD | 125,200.00 USD | 93,750.00 USD | 132,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 8,410,000.00 USD | 8,410,000.00 USD | 15,840.00 USD | 94,230.00 USD | 153,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2035` | 137.57 USD | 26,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2040` | 8,140,000.00 USD | 8,140,000.00 USD | 82,750.00 USD | 97,770.00 USD | 133,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 8,550,000.00 USD | 8,550,000.00 USD | 59,380.00 USD | 76,320.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 8,310,000.00 USD | 8,310,000.00 USD | 87,350.00 USD | 31,950.00 USD | 52,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 8,640,000.00 USD | 8,640,000.00 USD | 37,210.00 USD | 1,160.00 USD | 57,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 8,740,000.00 USD | 8,740,000.00 USD | 312,050.00 USD | 31,930.00 USD | 92,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 8,820,000.00 USD | 8,820,000.00 USD | 149,740.00 USD | 18,480.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 9,240,000.00 USD | 9,240,000.00 USD | 200,720.00 USD | 104,040.00 USD | 191,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 9,440,000.00 USD | 9,440,000.00 USD | 439,210.00 USD | 141,790.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2075` | 2,220.00 USD | 28,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2080` | 9,660,000.00 USD | 9,660,000.00 USD | 295,330.00 USD | 82,730.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 10,130,000.00 USD | 10,130,000.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 10,600,000.00 USD | 10,600,000.00 USD | 486,620.00 USD | 154,050.00 USD | 300,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 13,070,000.00 USD | 13,070,000.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 11,380,000.00 USD | 11,380,000.00 USD | 461,920.00 USD | 102,570.00 USD | 210,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 17,150,000.00 USD | 17,150,000.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 11,710,000.00 USD | 11,710,000.00 USD | 153,450.00 USD | 48,240.00 USD | 129,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 20,340,000.00 USD | 20,340,000.00 USD | 1,060,000.00 USD | 511,730.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 12,090,000.00 USD | 12,090,000.00 USD | 143,040.00 USD | 84,890.00 USD | 149,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 23,340,000.00 USD | 23,340,000.00 USD | 1,160,000.00 USD | 466,390.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 26,160,000.00 USD | 26,160,000.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 28,260,000.00 USD | 28,260,000.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 30,520,000.00 USD | 30,520,000.00 USD | 924,080.00 USD | 324,670.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 467.20 USD | 28,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2160` | 31,550,000.00 USD | 31,550,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 32,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2185` | 2,650.00 USD | 35,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2215` | 996.75 USD | 36,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 36,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 38,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 48,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 48,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 56,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2345` | 612.28 USD | 56,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,670.00 USD | 58,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 680.06 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 60,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 4,050.00 USD | 64,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2535` | 1,080.00 USD | 65,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 65,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2665` | 411.48 USD | 66,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 1,970.00 USD | 68,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 68,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 68,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 70,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 71,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 74,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 74,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 11,980.00 USD | 86,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 118,290.00 USD | 205,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3025` | 73,140.00 USD | 278,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 131.85 USD | 278,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 278,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3065` | 206.58 USD | 279,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 1,150.00 USD | 280,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 98,280.00 USD | 378,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3145` | 3,600.00 USD | 382,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3265` | 37,030.00 USD | 419,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 792.55 USD | 419,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3285` | 312.07 USD | 420,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 422,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 240.93 USD | 422,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3475` | 317.96 USD | 423,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 200,530.00 USD | 623,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 331.22 USD | 624,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,120.00 USD | 625,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3555` | 142.56 USD | 625,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 256,950.00 USD | 882,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3585` | 5,070.00 USD | 887,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3595` | 160.70 USD | 887,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 2,940.00 USD | 890,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 143.91 USD | 890,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3665` | 366.50 USD | 890,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3705` | 27,790.00 USD | 918,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 927,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3725` | 947.27 USD | 928,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 932,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3795` | 24,090.00 USD | 956,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3845` | 28,440.00 USD | 984,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0395` | 2,450,000.00 USD | 0.00 USD | 210.42 USD | `-79.45%` | `5,327.00` |
| `Live` | `Long` | `0.0415` | 2,450,000.00 USD | 0.00 USD | 823.53 USD | `-78.41%` | `19,844.00` |
| `Live` | `Long` | `0.0455` | 2,450,000.00 USD | 0.00 USD | 242.88 USD | `-76.33%` | `5,338.00` |
| `Live` | `Long` | `0.0485` | 2,450,000.00 USD | 0.00 USD | 103.16 USD | `-74.77%` | `2,127.00` |
| `Live` | `Long` | `0.0555` | 2,450,000.00 USD | 0.00 USD | 2,690.00 USD | `-71.13%` | `48,444.00` |
| `Live` | `Long` | `0.0575` | 2,450,000.00 USD | 0.00 USD | 137.71 USD | `-70.09%` | `2,395.00` |
| `Live` | `Long` | `0.0595` | 2,450,000.00 USD | 0.00 USD | 555.91 USD | `-69.05%` | `9,343.00` |
| `Live` | `Long` | `0.0615` | 2,440,000.00 USD | 0.00 USD | 2,020.00 USD | `-68.01%` | `32,814.00` |
| `Live` | `Long` | `0.0645` | 2,440,000.00 USD | 0.00 USD | 181.31 USD | `-66.45%` | `2,811.00` |
| `Live` | `Long` | `0.0665` | 2,440,000.00 USD | 0.00 USD | 228.96 USD | `-65.41%` | `3,443.00` |
| `Live` | `Long` | `0.0715` | 2,440,000.00 USD | 0.00 USD | 7,510.00 USD | `-62.81%` | `105,008.00` |
| `Live` | `Long` | `0.0745` | 2,430,000.00 USD | 0.00 USD | 1,160.00 USD | `-61.25%` | `15,628.00` |
| `Live` | `Long` | `0.0775` | 2,430,000.00 USD | 0.00 USD | 581.25 USD | `-59.69%` | `7,500.00` |
| `Live` | `Long` | `0.0815` | 2,430,000.00 USD | 0.00 USD | 284.84 USD | `-57.61%` | `3,495.00` |
| `Live` | `Long` | `0.0825` | 2,430,000.00 USD | 0.00 USD | 154,580.00 USD | `-57.09%` | `1,873,703.00` |
| `Live` | `Long` | `0.0865` | 2,280,000.00 USD | 0.00 USD | 102.50 USD | `-55.01%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,280,000.00 USD | 0.00 USD | 344.75 USD | `-54.49%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,280,000.00 USD | 0.00 USD | 1,150.00 USD | `-53.97%` | `13,050.00` |
| `Live` | `Long` | `0.0905` | 2,280,000.00 USD | 0.00 USD | 3,570.00 USD | `-52.93%` | `39,410.00` |
| `Live` | `Long` | `0.0925` | 2,270,000.00 USD | 0.00 USD | 13,120.00 USD | `-51.89%` | `141,785.00` |
| `Live` | `Long` | `0.0945` | 2,260,000.00 USD | 0.00 USD | 1,270.00 USD | `-50.85%` | `13,466.00` |
| `Live` | `Long` | `0.0985` | 2,260,000.00 USD | 0.00 USD | 87,280.00 USD | `-48.76%` | `886,128.00` |
| `Live` | `Long` | `0.1025` | 2,170,000.00 USD | 0.00 USD | 4,280.00 USD | `-46.68%` | `41,744.00` |
| `Live` | `Long` | `0.1035` | 2,170,000.00 USD | 0.00 USD | 1,050.00 USD | `-46.16%` | `10,149.00` |
| `Live` | `Long` | `0.1045` | 2,170,000.00 USD | 0.00 USD | 2,090.00 USD | `-45.64%` | `20,000.00` |
| `Live` | `Long` | `0.1055` | 2,160,000.00 USD | 0.00 USD | 150.44 USD | `-45.12%` | `1,426.00` |
| `Live` | `Long` | `0.1065` | 2,160,000.00 USD | 0.00 USD | 653.70 USD | `-44.60%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,160,000.00 USD | 0.00 USD | 2,200.00 USD | `-44.08%` | `20,486.00` |
| `Live` | `Long` | `0.1085` | 2,160,000.00 USD | 0.00 USD | 420.22 USD | `-43.56%` | `3,873.00` |
| `Live` | `Long` | `0.1095` | 2,160,000.00 USD | 0.00 USD | 430.44 USD | `-43.04%` | `3,931.00` |
| `Live` | `Long` | `0.1125` | 2,160,000.00 USD | 0.00 USD | 25,870.00 USD | `-41.48%` | `229,972.00` |
| `Live` | `Long` | `0.1145` | 2,130,000.00 USD | 0.00 USD | 862.64 USD | `-40.44%` | `7,534.00` |
| `Live` | `Long` | `0.1155` | 2,130,000.00 USD | 0.00 USD | 365.90 USD | `-39.92%` | `3,168.00` |
| `Live` | `Long` | `0.1165` | 2,130,000.00 USD | 0.00 USD | 13,150.00 USD | `-39.40%` | `112,888.00` |
| `Live` | `Long` | `0.1175` | 2,120,000.00 USD | 0.00 USD | 1,640.00 USD | `-38.88%` | `13,927.00` |
| `Live` | `Long` | `0.1185` | 2,120,000.00 USD | 0.00 USD | 7,570.00 USD | `-38.36%` | `63,913.00` |
| `Live` | `Long` | `0.1205` | 2,110,000.00 USD | 0.00 USD | 826.27 USD | `-37.32%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,110,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.80%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,110,000.00 USD | 0.00 USD | 1,180.00 USD | `-35.76%` | `9,522.00` |
| `Live` | `Long` | `0.1245` | 2,110,000.00 USD | 0.00 USD | 404.62 USD | `-35.24%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,110,000.00 USD | 0.00 USD | 2,420.00 USD | `-34.72%` | `19,273.00` |
| `Live` | `Long` | `0.1265` | 2,100,000.00 USD | 0.00 USD | 314.61 USD | `-34.20%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,100,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.68%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,100,000.00 USD | 0.00 USD | 2,540.00 USD | `-32.64%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,100,000.00 USD | 0.00 USD | 13,060.00 USD | `-32.12%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,090,000.00 USD | 0.00 USD | 529.68 USD | `-31.60%` | `4,028.00` |
| `Live` | `Long` | `0.1325` | 2,090,000.00 USD | 0.00 USD | 6,960.00 USD | `-31.08%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,080,000.00 USD | 0.00 USD | 8,970.00 USD | `-30.56%` | `67,209.00` |
| `Live` | `Long` | `0.1345` | 2,070,000.00 USD | 0.00 USD | 26,900.00 USD | `-30.04%` | `200,000.00` |
| `Live` | `Long` | `0.1355` | 2,040,000.00 USD | 0.00 USD | 106.64 USD | `-29.52%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,040,000.00 USD | 0.00 USD | 403.77 USD | `-29.00%` | `2,958.00` |
| `Live` | `Long` | `0.1405` | 2,040,000.00 USD | 0.00 USD | 314.44 USD | `-26.92%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,040,000.00 USD | 0.00 USD | 9,540.00 USD | `-26.40%` | `67,399.00` |
| `Live` | `Long` | `0.1425` | 2,030,000.00 USD | 0.00 USD | 958.46 USD | `-25.88%` | `6,726.00` |
| `Live` | `Long` | `0.1435` | 2,030,000.00 USD | 0.00 USD | 15,780.00 USD | `-25.36%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,020,000.00 USD | 0.00 USD | 2,990.00 USD | `-24.84%` | `20,678.00` |
| `Live` | `Long` | `0.1455` | 2,010,000.00 USD | 0.00 USD | 3,770.00 USD | `-24.32%` | `25,886.00` |
| `Live` | `Long` | `0.1465` | 2,010,000.00 USD | 0.00 USD | 4,580.00 USD | `-23.80%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,010,000.00 USD | 0.00 USD | 4,210.00 USD | `-23.28%` | `28,569.00` |
| `Live` | `Long` | `0.1485` | 2,000,000.00 USD | 0.00 USD | 1,360.00 USD | `-22.76%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 2,000,000.00 USD | 0.00 USD | 427.12 USD | `-22.24%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 2,000,000.00 USD | 0.00 USD | 1,720.00 USD | `-21.72%` | `11,458.00` |
| `Live` | `Long` | `0.1515` | 2,000,000.00 USD | 0.00 USD | 35,830.00 USD | `-21.20%` | `236,501.00` |
| `Live` | `Long` | `0.1525` | 1,960,000.00 USD | 0.00 USD | 2,350.00 USD | `-20.68%` | `15,391.00` |
| `Live` | `Long` | `0.1535` | 1,960,000.00 USD | 0.00 USD | 42,630.00 USD | `-20.16%` | `277,705.00` |
| `Live` | `Long` | `0.1545` | 1,920,000.00 USD | 0.00 USD | 721.05 USD | `-19.64%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,920,000.00 USD | 0.00 USD | 1,250.00 USD | `-19.12%` | `8,067.00` |
| `Live` | `Long` | `0.1565` | 1,910,000.00 USD | 0.00 USD | 11,530.00 USD | `-18.60%` | `73,669.00` |
| `Live` | `Long` | `0.1575` | 1,900,000.00 USD | 0.00 USD | 819.16 USD | `-18.08%` | `5,201.00` |
| `Live` | `Long` | `0.1585` | 1,900,000.00 USD | 0.00 USD | 703,200.00 USD | `-17.56%` | `4,436,577.00` |
| `Live` | `Long` | `0.1595` | 1,200,000.00 USD | 0.00 USD | 2,780.00 USD | `-17.04%` | `17,408.00` |
| `Live` | `Long` | `0.1605` | 1,200,000.00 USD | 0.00 USD | 57,580.00 USD | `-16.51%` | `358,740.00` |
| `Live` | `Long` | `0.1615` | 1,140,000.00 USD | 0.00 USD | 4,200.00 USD | `-15.99%` | `26,015.00` |
| `Live` | `Long` | `0.1625` | 1,130,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.47%` | `13,446.00` |
| `Live` | `Long` | `0.1635` | 1,130,000.00 USD | 0.00 USD | 1,040.00 USD | `-14.95%` | `6,337.00` |
| `Live` | `Long` | `0.1645` | 1,130,000.00 USD | 0.00 USD | 10,840.00 USD | `-14.43%` | `65,896.00` |
| `Live` | `Long` | `0.1655` | 1,120,000.00 USD | 0.00 USD | 6,810.00 USD | `-13.91%` | `41,167.00` |
| `Live` | `Long` | `0.1665` | 1,110,000.00 USD | 0.00 USD | 889.94 USD | `-13.39%` | `5,345.00` |
| `Live` | `Long` | `0.1675` | 1,110,000.00 USD | 0.00 USD | 630.81 USD | `-12.87%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,110,000.00 USD | 0.00 USD | 12,160.00 USD | `-12.35%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,100,000.00 USD | 0.00 USD | 79,290.00 USD | `-11.83%` | `467,760.00` |
| `Live` | `Long` | `0.1705` | 1,020,000.00 USD | 0.00 USD | 626,600.00 USD | `-11.31%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 394,430.00 USD | 0.00 USD | 252,270.00 USD | `-10.79%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 142,160.00 USD | 0.00 USD | 33,550.00 USD | `-10.27%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 108,610.00 USD | 0.00 USD | 658.61 USD | `-9.75%` | `3,796.00` |
| `Live` | `Long` | `0.1755` | 107,950.00 USD | 0.00 USD | 17,290.00 USD | `-8.71%` | `98,507.00` |
| `Live` | `Long` | `0.1765` | 90,660.00 USD | 0.00 USD | 50,680.00 USD | `-8.19%` | `287,146.00` |
| `Live` | `Long` | `0.1775` | 39,980.00 USD | 0.00 USD | 1,360.00 USD | `-7.67%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 38,620.00 USD | 0.00 USD | 4,530.00 USD | `-7.15%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 34,090.00 USD | 0.00 USD | 3,840.00 USD | `-6.63%` | `21,396.00` |
| `Live` | `Long` | `0.1805` | 30,250.00 USD | 0.00 USD | 3,050.00 USD | `-6.11%` | `16,904.00` |
| `Live` | `Long` | `0.1815` | 27,200.00 USD | 0.00 USD | 4,070.00 USD | `-5.59%` | `22,444.00` |
| `Live` | `Long` | `0.1825` | 23,130.00 USD | 0.00 USD | 20,830.00 USD | `-5.07%` | `114,125.00` |
| `Live` | `Short` | `0.1835` | 170.10 USD | 170.10 USD | 0.00 USD | `-4.55%` | `927.00` |
| `Live` | `Long` | `0.1845` | 2,300.00 USD | 0.00 USD | 2,300.00 USD | `-4.03%` | `12,457.00` |
| `Live` | `Short` | `0.1895` | 450.38 USD | 280.27 USD | 0.00 USD | `-1.43%` | `1,479.00` |
| `Live` | `Short` | `0.1945` | 738.43 USD | 288.05 USD | 0.00 USD | `+1.17%` | `1,481.00` |
| `Live` | `Short` | `0.1965` | 843.36 USD | 104.93 USD | 0.00 USD | `+2.21%` | `534.00` |
| `Live` | `Short` | `0.1985` | 1,180.00 USD | 338.64 USD | 0.00 USD | `+3.25%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 1,430.00 USD | 252.97 USD | 0.00 USD | `+3.77%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 4,010.00 USD | 2,570.00 USD | 0.00 USD | `+4.29%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 6,110.00 USD | 2,100.00 USD | 0.00 USD | `+4.81%` | `10,418.00` |
| `Live` | `Short` | `0.2025` | 26,160.00 USD | 20,050.00 USD | 0.00 USD | `+5.33%` | `99,030.00` |
| `Live` | `Short` | `0.2035` | 26,300.00 USD | 137.57 USD | 0.00 USD | `+5.85%` | `676.00` |
| `Live` | `Short` | `0.2075` | 28,520.00 USD | 2,220.00 USD | 0.00 USD | `+7.93%` | `10,683.00` |
| `Live` | `Short` | `0.2155` | 28,980.00 USD | 467.20 USD | 0.00 USD | `+12.09%` | `2,168.00` |
| `Live` | `Short` | `0.2175` | 32,910.00 USD | 3,930.00 USD | 0.00 USD | `+13.13%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 35,560.00 USD | 2,650.00 USD | 0.00 USD | `+13.65%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 36,560.00 USD | 996.75 USD | 0.00 USD | `+15.21%` | `4,500.00` |
| `Live` | `Short` | `0.2235` | 36,760.00 USD | 200.48 USD | 0.00 USD | `+16.25%` | `897.00` |
| `Live` | `Short` | `0.2265` | 38,990.00 USD | 2,230.00 USD | 0.00 USD | `+17.82%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 48,230.00 USD | 9,240.00 USD | 0.00 USD | `+18.86%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 48,510.00 USD | 282.02 USD | 0.00 USD | `+20.94%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 56,150.00 USD | 7,640.00 USD | 0.00 USD | `+21.46%` | `32,708.00` |
| `Live` | `Short` | `0.2345` | 56,760.00 USD | 612.28 USD | 0.00 USD | `+21.98%` | `2,611.00` |
| `Live` | `Short` | `0.2405` | 58,440.00 USD | 1,670.00 USD | 0.00 USD | `+25.10%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 59,120.00 USD | 680.06 USD | 0.00 USD | `+25.62%` | `2,816.00` |
| `Live` | `Short` | `0.2425` | 60,190.00 USD | 1,080.00 USD | 0.00 USD | `+26.14%` | `4,435.00` |
| `Live` | `Short` | `0.2445` | 64,240.00 USD | 4,050.00 USD | 0.00 USD | `+27.18%` | `16,564.00` |
| `Live` | `Short` | `0.2535` | 65,320.00 USD | 1,080.00 USD | 0.00 USD | `+31.86%` | `4,254.00` |
| `Live` | `Short` | `0.2585` | 65,700.00 USD | 380.25 USD | 0.00 USD | `+34.46%` | `1,471.00` |
| `Live` | `Short` | `0.2665` | 66,110.00 USD | 411.48 USD | 0.00 USD | `+38.62%` | `1,544.00` |
| `Live` | `Short` | `0.2675` | 68,080.00 USD | 1,970.00 USD | 0.00 USD | `+39.14%` | `7,372.00` |
| `Live` | `Short` | `0.2715` | 68,200.00 USD | 120.00 USD | 0.00 USD | `+41.22%` | `442.00` |
| `Live` | `Short` | `0.2775` | 68,580.00 USD | 379.62 USD | 0.00 USD | `+44.34%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 70,760.00 USD | 2,170.00 USD | 0.00 USD | `+47.98%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 71,170.00 USD | 411.09 USD | 0.00 USD | `+50.59%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 74,430.00 USD | 3,260.00 USD | 0.00 USD | `+51.63%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 74,950.00 USD | 519.79 USD | 0.00 USD | `+52.67%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 86,930.00 USD | 11,980.00 USD | 0.00 USD | `+53.71%` | `40,531.00` |
| `Live` | `Short` | `0.3005` | 205,220.00 USD | 118,290.00 USD | 0.00 USD | `+56.31%` | `393,656.00` |
| `Live` | `Short` | `0.3025` | 278,360.00 USD | 73,140.00 USD | 0.00 USD | `+57.35%` | `241,775.00` |
| `Live` | `Short` | `0.3045` | 278,490.00 USD | 131.85 USD | 0.00 USD | `+58.39%` | `433.00` |
| `Live` | `Short` | `0.3055` | 278,900.00 USD | 408.15 USD | 0.00 USD | `+58.91%` | `1,336.00` |
| `Live` | `Short` | `0.3065` | 279,100.00 USD | 206.58 USD | 0.00 USD | `+59.43%` | `674.00` |
| `Live` | `Short` | `0.3105` | 280,260.00 USD | 1,150.00 USD | 0.00 USD | `+61.51%` | `3,713.00` |
| `Live` | `Short` | `0.3115` | 378,540.00 USD | 98,280.00 USD | 0.00 USD | `+62.03%` | `315,521.00` |
| `Live` | `Short` | `0.3145` | 382,150.00 USD | 3,600.00 USD | 0.00 USD | `+63.59%` | `11,458.00` |
| `Live` | `Short` | `0.3265` | 419,180.00 USD | 37,030.00 USD | 0.00 USD | `+69.83%` | `113,421.00` |
| `Live` | `Short` | `0.3275` | 419,970.00 USD | 792.55 USD | 0.00 USD | `+70.35%` | `2,420.00` |
| `Live` | `Short` | `0.3285` | 420,280.00 USD | 312.07 USD | 0.00 USD | `+70.87%` | `950.00` |
| `Live` | `Short` | `0.3295` | 422,660.00 USD | 2,380.00 USD | 0.00 USD | `+71.39%` | `7,219.00` |
| `Live` | `Short` | `0.3365` | 422,900.00 USD | 240.93 USD | 0.00 USD | `+75.03%` | `716.00` |
| `Live` | `Short` | `0.3475` | 423,220.00 USD | 317.96 USD | 0.00 USD | `+80.75%` | `915.00` |
| `Live` | `Short` | `0.3485` | 623,750.00 USD | 200,530.00 USD | 0.00 USD | `+81.27%` | `575,408.00` |
| `Live` | `Short` | `0.3505` | 624,080.00 USD | 331.22 USD | 0.00 USD | `+82.31%` | `945.00` |
| `Live` | `Short` | `0.3515` | 625,200.00 USD | 1,120.00 USD | 0.00 USD | `+82.83%` | `3,187.00` |
| `Live` | `Short` | `0.3555` | 625,340.00 USD | 142.56 USD | 0.00 USD | `+84.92%` | `401.00` |
| `Live` | `Short` | `0.3565` | 882,290.00 USD | 256,950.00 USD | 0.00 USD | `+85.44%` | `720,753.00` |
| `Live` | `Short` | `0.3585` | 887,360.00 USD | 5,070.00 USD | 0.00 USD | `+86.48%` | `14,148.00` |
| `Live` | `Short` | `0.3595` | 887,520.00 USD | 160.70 USD | 0.00 USD | `+87.00%` | `447.00` |
| `Live` | `Short` | `0.3615` | 890,470.00 USD | 2,940.00 USD | 0.00 USD | `+88.04%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 890,610.00 USD | 143.91 USD | 0.00 USD | `+88.56%` | `397.00` |
| `Live` | `Short` | `0.3665` | 890,980.00 USD | 366.50 USD | 0.00 USD | `+90.64%` | `1,000.00` |
| `Live` | `Short` | `0.3705` | 918,760.00 USD | 27,790.00 USD | 0.00 USD | `+92.72%` | `75,000.00` |
| `Live` | `Short` | `0.3715` | 927,940.00 USD | 9,170.00 USD | 0.00 USD | `+93.24%` | `24,689.00` |
| `Live` | `Short` | `0.3725` | 928,880.00 USD | 947.27 USD | 0.00 USD | `+93.76%` | `2,543.00` |
| `Live` | `Short` | `0.3745` | 932,030.00 USD | 3,140.00 USD | 0.00 USD | `+94.80%` | `8,395.00` |
| `Live` | `Short` | `0.3795` | 956,120.00 USD | 24,090.00 USD | 0.00 USD | `+97.40%` | `63,484.00` |
| `Live` | `Short` | `0.3845` | 984,560.00 USD | 28,440.00 USD | 0.00 USD | `+100.00%` | `73,959.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 110,720,000.00 USD | 0.00 USD | 415.13 USD | `-69.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 110,720,000.00 USD | 0.00 USD | 438.99 USD | `-68.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 110,720,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 110,720,000.00 USD | 0.00 USD | 541.33 USD | `-42.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 110,720,000.00 USD | 0.00 USD | 429.20 USD | `-39.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 110,720,000.00 USD | 0.00 USD | 602,500.00 USD | `-37.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 110,120,000.00 USD | 0.00 USD | 4,460.00 USD | `-35.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 110,110,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 110,110,000.00 USD | 0.00 USD | 13,390.00 USD | `-32.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 110,100,000.00 USD | 0.00 USD | 728.88 USD | `-31.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 110,100,000.00 USD | 0.00 USD | 4,350.00 USD | `-30.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 110,090,000.00 USD | 0.00 USD | 4,730.00 USD | `-28.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 110,090,000.00 USD | 0.00 USD | 1,820.00 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 110,080,000.00 USD | 0.00 USD | 1,050.00 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 110,080,000.00 USD | 0.00 USD | 351.26 USD | `-25.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 110,080,000.00 USD | 0.00 USD | 1,600.00 USD | `-25.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 110,080,000.00 USD | 0.00 USD | 10,400.00 USD | `-24.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 110,070,000.00 USD | 0.00 USD | 5,980.00 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 110,070,000.00 USD | 0.00 USD | 303.26 USD | `-21.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 110,060,000.00 USD | 0.00 USD | 3,230.00 USD | `-21.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 110,060,000.00 USD | 0.00 USD | 6,380.00 USD | `-20.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 110,060,000.00 USD | 0.00 USD | 126.54 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 110,060,000.00 USD | 0.00 USD | 1,790.00 USD | `-19.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 110,050,000.00 USD | 0.00 USD | 6,260.00 USD | `-18.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 110,050,000.00 USD | 0.00 USD | 552.21 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 110,050,000.00 USD | 0.00 USD | 166.84 USD | `-17.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 110,050,000.00 USD | 0.00 USD | 10,270.00 USD | `-16.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 110,040,000.00 USD | 0.00 USD | 769.39 USD | `-15.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 110,040,000.00 USD | 0.00 USD | 24,760.00 USD | `-15.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 110,010,000.00 USD | 0.00 USD | 6,540.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 110,000,000.00 USD | 0.00 USD | 1,550.00 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 110,000,000.00 USD | 0.00 USD | 452.97 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 110,000,000.00 USD | 0.00 USD | 12,640.00 USD | `-13.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 109,990,000.00 USD | 0.00 USD | 317.92 USD | `-12.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 109,990,000.00 USD | 0.00 USD | 6,930.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 109,980,000.00 USD | 0.00 USD | 813.97 USD | `-11.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 109,980,000.00 USD | 0.00 USD | 1,220.00 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 109,980,000.00 USD | 0.00 USD | 640.67 USD | `-10.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 109,980,000.00 USD | 0.00 USD | 595.80 USD | `-9.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 109,980,000.00 USD | 0.00 USD | 349.00 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 109,980,000.00 USD | 0.00 USD | 1,760.00 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 109,980,000.00 USD | 0.00 USD | 847.38 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 109,980,000.00 USD | 0.00 USD | 5,090.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 109,970,000.00 USD | 0.00 USD | 18,790.00 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 109,950,000.00 USD | 0.00 USD | 14,810.00 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 109,940,000.00 USD | 0.00 USD | 1,570.00 USD | `-6.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 109,940,000.00 USD | 0.00 USD | 2,720.00 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 109,930,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-5.07%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 73,430,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-4.55%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 31,780.00 USD | 0.00 USD | 2,030.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 29,750.00 USD | 0.00 USD | 286.41 USD | `-3.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 29,460.00 USD | 0.00 USD | 1,420.00 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 28,040.00 USD | 0.00 USD | 3,580.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 24,460.00 USD | 0.00 USD | 3,100.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 21,360.00 USD | 0.00 USD | 19,340.00 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 2,020.00 USD | 0.00 USD | 1,450.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 570.29 USD | 0.00 USD | 570.29 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 224.07 USD | 224.07 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 3,520.00 USD | 3,300.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 3,800.00 USD | 276.77 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 4,350.00 USD | 549.75 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 8,010.00 USD | 3,660.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 8,300.00 USD | 292.10 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 8,950.00 USD | 646.71 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 9,860.00 USD | 912.11 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 26,720.00 USD | 16,860.00 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 73,060.00 USD | 46,340.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 74,890.00 USD | 1,840.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 86,170.00 USD | 11,280.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 88,860.00 USD | 2,690.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 91,010.00 USD | 2,160.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 106,500.00 USD | 15,490.00 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 106,810.00 USD | 312.70 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 115,150.00 USD | 8,340.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 123,150.00 USD | 7,990.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 145,220.00 USD | 22,070.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 165,040.00 USD | 19,820.00 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 171,750.00 USD | 6,700.00 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 175,940.00 USD | 4,190.00 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 176,910.00 USD | 965.25 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 187,210.00 USD | 10,300.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 187,820.00 USD | 609.66 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 187,930.00 USD | 109.91 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 203,390.00 USD | 15,460.00 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 206,150.00 USD | 2,760.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 207,800.00 USD | 1,650.00 USD | 0.00 USD | `+15.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 216,980.00 USD | 9,180.00 USD | 0.00 USD | `+15.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 220,730.00 USD | 3,750.00 USD | 0.00 USD | `+16.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 220,850.00 USD | 114.50 USD | 0.00 USD | `+16.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 221,190.00 USD | 339.60 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 221,290.00 USD | 109.40 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 221,450.00 USD | 151.06 USD | 0.00 USD | `+18.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 230,590.00 USD | 9,140.00 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 231,250.00 USD | 662.92 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 231,590.00 USD | 337.06 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 231,760.00 USD | 171.12 USD | 0.00 USD | `+20.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 231,860.00 USD | 101.11 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 232,970.00 USD | 1,110.00 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 242,390.00 USD | 9,420.00 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 242,830.00 USD | 443.91 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 243,610.00 USD | 778.76 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 243,800.00 USD | 192.71 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 244,320.00 USD | 514.45 USD | 0.00 USD | `+24.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 244,530.00 USD | 209.72 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 244,640.00 USD | 115.92 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 244,880.00 USD | 236.19 USD | 0.00 USD | `+26.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 246,030.00 USD | 1,150.00 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 246,310.00 USD | 288.22 USD | 0.00 USD | `+27.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 246,810.00 USD | 491.03 USD | 0.00 USD | `+28.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 248,130.00 USD | 1,320.00 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 258,070.00 USD | 9,940.00 USD | 0.00 USD | `+29.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 258,570.00 USD | 499.00 USD | 0.00 USD | `+29.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 259,670.00 USD | 1,100.00 USD | 0.00 USD | `+30.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 259,840.00 USD | 168.76 USD | 0.00 USD | `+30.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 262,010.00 USD | 2,170.00 USD | 0.00 USD | `+31.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 263,710.00 USD | 1,700.00 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 263,980.00 USD | 271.44 USD | 0.00 USD | `+34.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 684,730.00 USD | 420,750.00 USD | 0.00 USD | `+35.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 685,910.00 USD | 1,180.00 USD | 0.00 USD | `+37.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 694,810.00 USD | 8,890.00 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 709,670.00 USD | 14,860.00 USD | 0.00 USD | `+39.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 711,010.00 USD | 1,340.00 USD | 0.00 USD | `+40.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 713,720.00 USD | 2,710.00 USD | 0.00 USD | `+41.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 727,590.00 USD | 13,870.00 USD | 0.00 USD | `+42.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 732,800.00 USD | 5,220.00 USD | 0.00 USD | `+42.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 733,980.00 USD | 1,170.00 USD | 0.00 USD | `+44.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 738,130.00 USD | 4,150.00 USD | 0.00 USD | `+44.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 739,070.00 USD | 944.99 USD | 0.00 USD | `+45.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 739,270.00 USD | 198.73 USD | 0.00 USD | `+47.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 740,640.00 USD | 1,370.00 USD | 0.00 USD | `+47.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 741,720.00 USD | 1,080.00 USD | 0.00 USD | `+49.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 756,710.00 USD | 14,980.00 USD | 0.00 USD | `+51.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 757,940.00 USD | 1,230.00 USD | 0.00 USD | `+51.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 759,380.00 USD | 1,440.00 USD | 0.00 USD | `+54.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 759,740.00 USD | 355.21 USD | 0.00 USD | `+55.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 766,390.00 USD | 6,650.00 USD | 0.00 USD | `+56.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 785,370.00 USD | 18,980.00 USD | 0.00 USD | `+58.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 789,520.00 USD | 4,150.00 USD | 0.00 USD | `+60.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 792,770.00 USD | 3,250.00 USD | 0.00 USD | `+63.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 793,260.00 USD | 493.89 USD | 0.00 USD | `+68.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 793,440.00 USD | 181.30 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 794,830.00 USD | 1,380.00 USD | 0.00 USD | `+71.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 807,110.00 USD | 12,290.00 USD | 0.00 USD | `+72.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 807,220.00 USD | 111.06 USD | 0.00 USD | `+73.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 807,450.00 USD | 220.61 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 810,780.00 USD | 3,340.00 USD | 0.00 USD | `+81.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 810,970.00 USD | 188.75 USD | 0.00 USD | `+96.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 811,880.00 USD | 909.54 USD | 0.00 USD | `+96.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 812,000.00 USD | 121.76 USD | 0.00 USD | `+97.92%` | `TACTICAL (Retail Cluster)` |

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
| `1D` | `0.1730` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 110,770.00 USD | 33,130.00 USD | 132,970.00 USD |
| `7D` | `0.1730` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 0.00 USD | 332.90 USD | 82,340.00 USD |
| `1D` | `0.1740` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 33,860.00 USD | 15,040.00 USD | 23,970.00 USD |
| `7D` | `0.1740` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 0.00 USD | 3,560.00 USD | 32,360.00 USD |
| `1D` | `0.1750` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 50,710.00 USD | 15,820.00 USD | 14,890.00 USD |
| `7D` | `0.1750` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 7,610.00 USD | 6,730.00 USD | 25,660.00 USD |
| `1D` | `0.1760` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 39,610.00 USD | 8,400.00 USD | 13,070.00 USD |
| `7D` | `0.1760` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD |
| `1D` | `0.1770` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 208,040.00 USD | 35,120.00 USD | 68,890.00 USD |
| `7D` | `0.1770` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD |
| `1D` | `0.1780` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 70,380.00 USD | 13,120.00 USD | 42,010.00 USD |
| `7D` | `0.1780` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 140,230.00 USD | 12,660.00 USD | 56,120.00 USD |
| `1D` | `0.1790` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 114,490.00 USD | 48,320.00 USD | 90,750.00 USD |
| `7D` | `0.1790` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 9,850.00 USD | 27,990.00 USD | 116,120.00 USD |
| `1D` | `0.1800` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 746,750.00 USD | 99,750.00 USD | 184,760.00 USD |
| `7D` | `0.1800` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 464,090.00 USD | 95,830.00 USD | 141,980.00 USD |
| `1D` | `0.1810` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 160,390.00 USD | 59,240.00 USD | 169,600.00 USD |
| `7D` | `0.1810` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 354,390.00 USD | 45,990.00 USD | 179,050.00 USD |
| `1D` | `0.1820` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 433,390.00 USD | 96,490.00 USD | 318,680.00 USD |
| `7D` | `0.1820` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 123,330.00 USD | 62,450.00 USD | 444,200.00 USD |
| `1D` | `0.1830` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 436,700.00 USD | 44,980.00 USD | 65,230.00 USD |
| `7D` | `0.1830` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 435,140.00 USD | 47,220.00 USD | 32,460.00 USD |
| `1D` | `0.1840` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 434,390.00 USD | 111,320.00 USD | 199,870.00 USD |
| `7D` | `0.1840` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 273,040.00 USD | 41,950.00 USD | 192,770.00 USD |
| `1D` | `0.1850` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 85,970.00 USD | 46,150.00 USD | 159,010.00 USD |
| `7D` | `0.1850` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 50,160.00 USD | 6,440.00 USD | 228,270.00 USD |
| `1D` | `0.1860` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 168,220.00 USD | 44,670.00 USD | 430,730.00 USD |
| `7D` | `0.1860` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 70,810.00 USD | 15,200.00 USD | 5,140.00 USD |
| `1D` | `0.1870` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 62,810.00 USD | 34,550.00 USD | 473,170.00 USD |
| `7D` | `0.1870` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD |
| `1D` | `0.1880` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 344,090.00 USD | 232,420.00 USD | 224,860.00 USD |
| `7D` | `0.1880` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 132,450.00 USD | 103,170.00 USD | 670,720.00 USD |
| `1D` | `0.1890` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 277,850.00 USD | 51,110.00 USD | 179,190.00 USD |
| `7D` | `0.1890` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 510,390.00 USD | 12,880.00 USD | 32,810.00 USD |
| `1D` | `0.1900` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 93,550.00 USD | 128,280.00 USD | 299,230.00 USD |
| `7D` | `0.1900` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 255,740.00 USD | 30,390.00 USD | 216,460.00 USD |
| `1D` | `0.1910` | 733,850.00 USD | 0.00 USD | 733,850.00 USD | 643,430.00 USD | 55,400.00 USD | 23,970.00 USD |
| `7D` | `0.1910` | 553,650.00 USD | 0.00 USD | 553,650.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD |
| `1D` | `0.1920` | 11,060.00 USD | 0.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | 11,060.00 USD |
| `7D` | `0.1920` | 600,250.00 USD | 600,250.00 USD | 0.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD |
| `7D` | `0.1920` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 583,840.00 USD | 0.00 USD | 16,400.00 USD |
| `1D` | `0.1930` | 457,320.00 USD | 457,320.00 USD | 0.00 USD | 284,520.00 USD | 2,420.00 USD | 170,380.00 USD |
| `1D` | `0.1930` | 914,650.00 USD | 914,650.00 USD | 0.00 USD | 284,520.00 USD | 2,420.00 USD | 170,380.00 USD |
| `7D` | `0.1930` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 653,060.00 USD | 0.00 USD | 331,360.00 USD |
| `1D` | `0.1940` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 21,310.00 USD | 356.90 USD | 352,350.00 USD |
| `7D` | `0.1940` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `1D` | `0.1950` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 25,540.00 USD | 73,330.00 USD | 412,450.00 USD |
| `7D` | `0.1950` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 693,070.00 USD | 1,990.00 USD | 203,120.00 USD |
| `1D` | `0.1960` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 575,620.00 USD | 280,100.00 USD | 552,250.00 USD |
| `7D` | `0.1960` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 236,660.00 USD | 112,940.00 USD | 1,240,000.00 USD |
| `1D` | `0.1970` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 156,270.00 USD | 128,680.00 USD | 376,370.00 USD |
| `7D` | `0.1970` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 13,930.00 USD | 32,990.00 USD | 275,930.00 USD |
| `1D` | `0.1980` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 409,930.00 USD | 110,510.00 USD | 378,020.00 USD |
| `7D` | `0.1980` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 312,350.00 USD | 44,250.00 USD | 315,080.00 USD |
| `1D` | `0.1990` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 206,360.00 USD | 67,850.00 USD | 291,470.00 USD |
| `7D` | `0.1990` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD |
| `1D` | `0.2000` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 415,860.00 USD | 100,110.00 USD | 414,270.00 USD |
| `7D` | `0.2000` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 56,530.00 USD | 38,390.00 USD | 371,130.00 USD |
| `1D` | `0.2010` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 189,510.00 USD | 169,210.00 USD | 368,890.00 USD |
| `7D` | `0.2010` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 335,650.00 USD | 25,310.00 USD | 359,800.00 USD |
| `1D` | `0.2020` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 224,560.00 USD | 76,110.00 USD | 179,140.00 USD |
| `7D` | `0.2020` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 87,710.00 USD | 52,030.00 USD | 495,090.00 USD |
| `1D` | `0.2030` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 125,200.00 USD | 93,750.00 USD | 132,660.00 USD |
| `7D` | `0.2030` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 15,840.00 USD | 94,230.00 USD | 153,910.00 USD |
| `1D` | `0.2040` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 82,750.00 USD | 97,770.00 USD | 133,090.00 USD |
| `7D` | `0.2040` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 59,380.00 USD | 76,320.00 USD | 6,560.00 USD |
| `1D` | `0.2050` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 87,350.00 USD | 31,950.00 USD | 52,620.00 USD |
| `7D` | `0.2050` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 37,210.00 USD | 1,160.00 USD | 57,550.00 USD |
| `1D` | `0.2060` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 312,050.00 USD | 31,930.00 USD | 92,350.00 USD |
| `7D` | `0.2060` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 149,740.00 USD | 18,480.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 200,720.00 USD | 104,040.00 USD | 191,430.00 USD |
| `7D` | `0.2070` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 439,210.00 USD | 141,790.00 USD | 35,600.00 USD |
| `1D` | `0.2080` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 295,330.00 USD | 82,730.00 USD | 42,600.00 USD |
| `7D` | `0.2080` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD |
| `1D` | `0.2090` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 486,620.00 USD | 154,050.00 USD | 300,210.00 USD |
| `7D` | `0.2090` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD |
| `1D` | `0.2100` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 461,920.00 USD | 102,570.00 USD | 210,050.00 USD |
| `7D` | `0.2100` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD |
| `1D` | `0.2110` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 153,450.00 USD | 48,240.00 USD | 129,000.00 USD |
| `7D` | `0.2110` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 1,060,000.00 USD | 511,730.00 USD | 1,620,000.00 USD |
| `1D` | `0.2120` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 143,040.00 USD | 84,890.00 USD | 149,700.00 USD |
| `7D` | `0.2120` | 23,340,000.00 USD | 23,340,000.00 USD | 0.00 USD | 1,160,000.00 USD | 466,390.00 USD | 1,380,000.00 USD |
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
  * Total Open Interest: `410.23M` | Total OI Tokens: `2,124,587,511.1 ADA`
  * 1h OI Change: `+0.26%` | 4h OI Change: `-0.80%` | 24h OI Change: `-7.95%`
  * Exchange Breakdown: Binance=`74.79M` | Bybit=`50.16M` | OKX=`29.06M` | Hyperliquid=`28.43M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.64K` | Last 24h: `30.56K` | Last 3d: `64.45K` | Last 7d: `83.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0038%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0067%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `51.10%` | `48.90%` | `1.04` | 9,370,000.00 USD |
| `15M` | `Binance` | `51.66%` | `48.34%` | `1.07` | 2,790,000.00 USD |
| `15M` | `OKX` | `61.89%` | `38.11%` | `1.62` | 1,310,000.00 USD |
| `15M` | `Bybit` | `59.32%` | `40.68%` | `1.46` | 496,020.00 USD |
| `15M` | `KuCoin` | `57.45%` | `42.55%` | `1.35` | 84,560.00 USD |
| `15M` | `Gate` | `48.23%` | `51.77%` | `0.93` | 2,010,000.00 USD |
| `15M` | `Bitget` | `67.02%` | `32.98%` | `2.03` | 108,900.00 USD |
| `15M` | `BingX` | `21.87%` | `78.13%` | `0.28` | 374,360.00 USD |
| `15M` | `MEXC` | `87.4%` | `12.6%` | `6.94` | 542,910.00 USD |
| `15M` | `Bitunix` | `52.58%` | `47.42%` | `1.11` | 187,380.00 USD |
| `15M` | `Hyperliquid` | `91.33%` | `8.67%` | `10.53` | 144,890.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.57%` | `46.43%` | `1.15` | 50,640.00 USD |
| `15M` | `Crypto.com` | `77.32%` | `22.68%` | `3.41` | 6,070.00 USD |
| `15M` | `WhiteBIT` | `19.64%` | `80.36%` | `0.24` | 1,050,000.00 USD |
| `15M` | `HTX` | `77.31%` | `22.69%` | `3.41` | 92,360.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `45.72%` | `54.28%` | `0.84` | 102,420.00 USD |
| `15M` | `Aster` | `49.36%` | `50.64%` | `0.97` | 19,040.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `36.58%` | `63.42%` | `0.58` | 14,630.00 USD |
| `15M` | `Whale Positions` | `51.66%` | `48.34%` | `1.07` | 2,790,000.00 USD |
| `15M` | `Global Accounts` | `51.10%` | `48.90%` | `1.04` | 9,370,000.00 USD |
| `1H` | `ADA` | `46.57%` | `53.43%` | `0.87` | 17,310,000.00 USD |
| `1H` | `Binance` | `47.62%` | `52.38%` | `0.91` | 5,630,000.00 USD |
| `1H` | `OKX` | `46.69%` | `53.31%` | `0.88` | 1,180,000.00 USD |
| `1H` | `Bybit` | `52.55%` | `47.45%` | `1.11` | 1,180,000.00 USD |
| `1H` | `KuCoin` | `43.45%` | `56.55%` | `0.77` | 148,390.00 USD |
| `1H` | `Gate` | `53.53%` | `46.47%` | `1.15` | 948,020.00 USD |
| `1H` | `Bitget` | `62.48%` | `37.52%` | `1.67` | 338,200.00 USD |
| `1H` | `BingX` | `52.71%` | `47.29%` | `1.11` | 1,510,000.00 USD |
| `1H` | `MEXC` | `39.1%` | `60.9%` | `0.64` | 1,550,000.00 USD |
| `1H` | `Bitunix` | `48.49%` | `51.51%` | `0.94` | 250,280.00 USD |
| `1H` | `Hyperliquid` | `36.07%` | `63.93%` | `0.56` | 250,320.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.28%` | `48.72%` | `1.05` | 2,860,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.92%` | `91.08%` | `0.10` | 1,090,000.00 USD |
| `1H` | `HTX` | `54.9%` | `45.1%` | `1.22` | 52,670.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `64.85%` | `35.15%` | `1.84` | 259,110.00 USD |
| `1H` | `Aster` | `84.47%` | `15.53%` | `5.44` | 1,370.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `86.04%` | `13.96%` | `6.16` | 52,740.00 USD |
| `1H` | `Whale Positions` | `47.62%` | `52.38%` | `0.91` | 5,630,000.00 USD |
| `1H` | `Global Accounts` | `46.57%` | `53.43%` | `0.87` | 17,310,000.00 USD |
| `4H` | `ADA` | `46.28%` | `53.72%` | `0.86` | 161,180,000.00 USD |
| `4H` | `Binance` | `50.48%` | `49.52%` | `1.02` | 59,180,000.00 USD |
| `4H` | `OKX` | `50.71%` | `49.29%` | `1.03` | 33,360,000.00 USD |
| `4H` | `Bybit` | `50.69%` | `49.31%` | `1.03` | 10,540,000.00 USD |
| `4H` | `KuCoin` | `46.58%` | `53.42%` | `0.87` | 1,100,000.00 USD |
| `4H` | `Gate` | `52.34%` | `47.66%` | `1.10` | 27,300,000.00 USD |
| `4H` | `Bitget` | `44.07%` | `55.93%` | `0.79` | 3,000,000.00 USD |
| `4H` | `BingX` | `36.39%` | `63.61%` | `0.57` | 3,160,000.00 USD |
| `4H` | `MEXC` | `45.91%` | `54.09%` | `0.85` | 9,850,000.00 USD |
| `4H` | `Bitunix` | `48.21%` | `51.79%` | `0.93` | 3,860,000.00 USD |
| `4H` | `Hyperliquid` | `35.53%` | `64.47%` | `0.55` | 1,390,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.83%` | `49.17%` | `1.03` | 1,120,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 191,440.00 USD |
| `4H` | `WhiteBIT` | `4.94%` | `95.06%` | `0.05` | 4,850,000.00 USD |
| `4H` | `HTX` | `57.02%` | `42.98%` | `1.33` | 779,280.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `57.58%` | `42.42%` | `1.36` | 558,730.00 USD |
| `4H` | `Aster` | `28.25%` | `71.75%` | `0.39` | 897,440.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `76.72%` | `23.28%` | `3.30` | 50,100.00 USD |
| `4H` | `Whale Positions` | `50.48%` | `49.52%` | `1.02` | 59,180,000.00 USD |
| `4H` | `Global Accounts` | `46.28%` | `53.72%` | `0.86` | 161,180,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1921` | `0.1928` | `0.1921` | `0.1941` | `0.1920` | 1,954,616.49 USD | 896,711.52 USD | 1,057,904.97 USD | -161,193.45 USD | `-8.25%` | `0B / 4S` |
| `5:00 UTC` | `0.1925` | `0.1924` | `0.1925` | `0.1930` | `0.1920` | 1,539,119.78 USD | 772,101.15 USD | 767,018.63 USD | 5,082.52 USD | `+0.33%` | `2B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1924` | `0.1925` | `0.1930` | `0.1918` | 1,135,407.39 USD | 588,660.08 USD | 546,747.31 USD | 41,912.77 USD | `+3.69%` | `2B / 1S` |
| `5:00 UTC` | `0.1928` | `0.1927` | `0.1928` | `0.1930` | `0.1923` | 1,200,311.82 USD | 545,374.62 USD | 654,937.20 USD | -109,562.58 USD | `-9.13%` | `0B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1925` | `0.1918` | 999,923.94 USD | 501,446.14 USD | 498,477.80 USD | 2,968.35 USD | `+0.30%` | `1B / 2S` |
| `5:00 UTC` | `0.1920` | `0.1923` | `0.1920` | `0.1930` | `0.1916` | 1,687,367.20 USD | 1,122,865.28 USD | 564,501.92 USD | 558,363.36 USD | `+33.09%` | `5B / 0S` |
| `0:00 UTC` | `0.1925` | `0.1926` | `0.1925` | `0.1930` | `0.1921` | 1,372,988.82 USD | 626,720.98 USD | 746,267.84 USD | -119,546.86 USD | `-8.71%` | `0B / 1S` |
| `5:00 UTC` | `0.1918` | `0.1920` | `0.1918` | `0.1925` | `0.1916` | 742,501.25 USD | 301,932.71 USD | 440,568.55 USD | -138,635.84 USD | `-18.67%` | `1B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1930` | `0.1915` | 1,936,754.49 USD | 922,725.13 USD | 1,014,029.36 USD | -91,304.23 USD | `-4.71%` | `1B / 3S` |
| `5:00 UTC` | `0.1925` | `0.1923` | `0.1925` | `0.1925` | `0.1920` | 139,996.62 USD | 49,421.62 USD | 90,575.00 USD | -41,153.38 USD | `-29.40%` | `1B / 2S` |

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
| `5m` | -9,160.00 USD | 73,610.00 USD | **`ACCUMULATION`** |
| `15m` | -42,960.00 USD | 137,300.00 USD | **`ACCUMULATION`** |
| `30m` | -45,950.00 USD | 4,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -16,380.00 USD | -62,950.00 USD | **`DISTRIBUTION`** |
| `2h` | -180,770.00 USD | 473,000.00 USD | **`ACCUMULATION`** |
| `4h` | -562,490.00 USD | 442,830.00 USD | **`DISTRIBUTION`** |
| `6h` | -387,250.00 USD | -48,800.00 USD | **`DISTRIBUTION`** |
| `8h` | -21,690.00 USD | 4,240,000.00 USD | **`ACCUMULATION`** |
| `12h` | -4,390,000.00 USD | -440,710.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,620,000.00 USD | -8,970,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,910,000.00 USD | -40,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,800,000.00 USD | -197,150,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-9.16K` | 15m=`-42.96K` | 1h=`-16.38K` | 24h=`-8.62M`
* Futures Capital Netflows: 5m=`+73.61K` | 15m=`+137.30K` | 1h=`-62.95K` | 24h=`-8.97M`
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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1872` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1827` (Risk Distance: `0.0045` pts)
  * +2.5R Take Profit: `0.1985`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1938` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.1983` (Risk Distance: `0.0045` pts)
  * +2.5R Take Profit: `0.1825`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1937`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
