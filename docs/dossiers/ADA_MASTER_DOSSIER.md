# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:39:48 IST` (`2026-10-30 11:09:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1937` | **Live Ask Quote**: `0.1958` | **Mid Price**: `0.1948`
- **Spread Points**: `21.00` | **Spread BPS**: `107.83 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1948` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1961` | Lower -3.00σ Band: `0.1934`
  * Upper +2.51σ Band: `0.1958` | Lower -2.51σ Band: `0.1937`
  * Upper +2.01σ Band: `0.1956` | Lower -2.01σ Band: `0.1939`
  * Upper +2.00σ Band: `0.1955` | Lower -2.00σ Band: `0.1940`
  * Upper +1.28σ Band: `0.1953` | Lower -1.28σ Band: `0.1942`
  * Upper +1.00σ Band: `0.1951` | Lower -1.00σ Band: `0.1944`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1948` | EMA-20=`0.1948` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1948` (Slope: `+0.0000`) | EMA-100=`0.1948`
  * Institutional Anchors: EMA-144=`0.1948` | EMA-200=`0.1948` (Slope: `+0.0000`) | EMA-233=`0.1948`
- **Range Boundaries**: 24H High=`0.1967` | 24H Low=`0.1928` | Weekly High=`0.1986` | Weekly Low=`0.1909`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1939` (Distance: `+0.44%`)
  * Point of Control (POC) = `0.1912` (Distance: `+1.85%`)
  * Value Area Low (VAL) = `0.1876` (Distance: `+3.79%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `0.1940` - `0.1955`
  * Optimal Trade Entry (OTE 0.705): `0.1951`
  * Structural Invalidation Anchor (0.786): `0.1963`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1940` | `0.1941` | `0.1936` | `0.1938` | `1,996,686` | 387,177.19 USD | -21,937.72 USD | `-5.67%` | -4,807,455.69 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1938` | `0.1940` | `0.1935` | `0.1938` | `1,487,668` | 288,269.45 USD | 51,761.11 USD | `+17.96%` | -4,755,694.58 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1938` | `0.1940` | `0.1936` | `0.1939` | `911,335` | 176,588.81 USD | -9,040.61 USD | `-5.12%` | -4,764,735.20 USD | `-0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1927` | `0.1941` | `0.1926` | `0.1938` | `8,976,737` | 1,737,432.33 USD | 227,430.57 USD | `+13.09%` | -4,598,517.88 USD | `+1.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1938` | `0.1951` | `0.1935` | `0.1950` | `8,429,944` | 1,638,885.40 USD | 396,532.35 USD | `+24.20%` | -4,201,985.53 USD | `+1.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1950` | `0.1954` | `0.1949` | `0.1950` | `2,542,222` | 496,136.28 USD | -105,463.27 USD | `-21.26%` | -4,307,448.80 USD | `-0.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1924` | `0.1930` | `0.1914` | `0.1926` | `25,331,850` | 4,870,682.84 USD | -212,635.97 USD | `-4.37%` | -4,622,595.77 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1927` | `0.1951` | `0.1924` | `0.1950` | `29,768,670` | 5,758,831.86 USD | 754,053.32 USD | `+13.09%` | -3,868,542.45 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1950` | `0.1954` | `0.1949` | `0.1949` | `2,542,365` | 496,164.15 USD | -105,491.14 USD | `-21.26%` | -3,974,033.59 USD | `+0.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1941` | `0.1914` | `0.1939` | `75,207,279` | 14,483,348.52 USD | 686,138.00 USD | `+4.74%` | -4,217,503.70 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,207,439.06 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -4,361,461.60 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -4,392,212.53 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1954` | `0.1912` | `0.1924` | `110,780,894` | 21,429,221.43 USD | -511,429.17 USD | `-2.39%` | -4,903,641.70 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1924` | `0.1954` | `0.1914` | `0.1950` | `83,755,426` | 16,148,661.34 USD | 929,635.98 USD | `+5.76%` | -3,974,005.72 USD | `+0.58` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1948`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `532` | `0x77ee...2902` | `SHORT` | 4,179,445.76 USD | `21,412,192.00` | `0.1911` | `0.1947` | `0.5957` | -88,194.02 USD | `-2.11%` | `10X Cross` |
| `1205` | `0x123d...3bff` | `LONG` | 1,828,885.72 USD | `9,392,870.00` | `0.2912` | `0.1947` | `0.000000` | -906,771.00 USD | `-49.58%` | `10X Cross` |
| `1242` | `0x7737...bf66` | `SHORT` | 1,771,017.58 USD | `9,091,466.00` | `0.2190` | `0.1947` | `2.14` | 219,972.22 USD | `+12.42%` | `10X Cross` |
| `1553` | `0x5f94...4b96` | `SHORT` | 1,394,933.05 USD | `7,162,318.00` | `0.2303` | `0.1947` | `0.7150` | 254,542.14 USD | `+18.25%` | `10X Cross` |
| `1767` | `0x4982...59e6` | `SHORT` | 1,172,467.81 USD | `5,998,812.00` | `0.1891` | `0.1947` | `0.4099` | -37,909.44 USD | `-3.23%` | `10X Cross` |
| `1829` | `0xcac1...26b3` | `LONG` | 1,129,885.29 USD | `5,803,927.00` | `0.2000` | `0.1947` | `0.000000` | -30,930.29 USD | `-2.74%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `1D` | `Long Liquidation` | `0.1730` | 10,240,000.00 USD | 10,240,000.00 USD | 115,290.00 USD | 33,150.00 USD | 137,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1730` | 8,610,000.00 USD | 8,610,000.00 USD | 32,310.00 USD | 6,910.00 USD | 82,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 658.61 USD | 110,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 9,950,000.00 USD | 9,950,000.00 USD | 56,600.00 USD | 30,930.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1740` | 8,490,000.00 USD | 8,490,000.00 USD | 10,400.00 USD | 29,910.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1750` | 9,830,000.00 USD | 9,830,000.00 USD | 50,710.00 USD | 17,820.00 USD | 39,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1750` | 8,400,000.00 USD | 8,400,000.00 USD | 7,610.00 USD | 6,730.00 USD | 39,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 17,080.00 USD | 109,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 9,730,000.00 USD | 9,730,000.00 USD | 45,460.00 USD | 8,400.00 USD | 25,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1760` | 8,350,000.00 USD | 8,350,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 47,010.00 USD | 92,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 9,650,000.00 USD | 9,650,000.00 USD | 208,040.00 USD | 35,120.00 USD | 63,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1770` | 8,330,000.00 USD | 8,330,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 45,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 9,340,000.00 USD | 9,340,000.00 USD | 70,380.00 USD | 13,120.00 USD | 38,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1780` | 8,080,000.00 USD | 8,080,000.00 USD | 140,230.00 USD | 13,120.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 44,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 9,220,000.00 USD | 9,220,000.00 USD | 114,060.00 USD | 42,720.00 USD | 92,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 7,870,000.00 USD | 7,870,000.00 USD | 12,380.00 USD | 28,450.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 39,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 8,970,000.00 USD | 8,970,000.00 USD | 724,590.00 USD | 95,980.00 USD | 178,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 7,710,000.00 USD | 7,710,000.00 USD | 469,140.00 USD | 95,830.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 3,050.00 USD | 35,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 7,970,000.00 USD | 7,970,000.00 USD | 150,850.00 USD | 56,840.00 USD | 146,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 7,000,000.00 USD | 7,000,000.00 USD | 356,840.00 USD | 46,600.00 USD | 179,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 20,100.00 USD | 32,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 7,620,000.00 USD | 7,620,000.00 USD | 435,080.00 USD | 95,510.00 USD | 340,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 6,420,000.00 USD | 6,420,000.00 USD | 126,700.00 USD | 63,070.00 USD | 444,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 9,020.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 6,740,000.00 USD | 6,740,000.00 USD | 439,340.00 USD | 45,220.00 USD | 70,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 5,790,000.00 USD | 5,790,000.00 USD | 441,880.00 USD | 47,220.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 1,370.00 USD | 3,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 6,190,000.00 USD | 6,190,000.00 USD | 444,800.00 USD | 111,410.00 USD | 204,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 5,270,000.00 USD | 5,270,000.00 USD | 373,060.00 USD | 64,640.00 USD | 192,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 2,300.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 5,430,000.00 USD | 5,430,000.00 USD | 154,260.00 USD | 112,070.00 USD | 186,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 4,640,000.00 USD | 4,640,000.00 USD | 76,160.00 USD | 72,320.00 USD | 267,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 4,980,000.00 USD | 4,980,000.00 USD | 171,980.00 USD | 55,740.00 USD | 513,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 4,220,000.00 USD | 4,220,000.00 USD | 70,810.00 USD | 15,200.00 USD | 39,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 4,230,000.00 USD | 4,230,000.00 USD | 80,170.00 USD | 38,000.00 USD | 502,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 4,090,000.00 USD | 4,090,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 3,610,000.00 USD | 3,610,000.00 USD | 360,930.00 USD | 232,420.00 USD | 260,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 3,600,000.00 USD | 3,600,000.00 USD | 325,960.00 USD | 148,540.00 USD | 670,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 2,760,000.00 USD | 2,760,000.00 USD | 410,160.00 USD | 182,950.00 USD | 225,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 2,460,000.00 USD | 2,460,000.00 USD | 562,390.00 USD | 144,640.00 USD | 111,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 1,940,000.00 USD | 1,940,000.00 USD | 103,950.00 USD | 150,420.00 USD | 454,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 1,640,000.00 USD | 1,640,000.00 USD | 255,740.00 USD | 30,390.00 USD | 284,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 1,230,000.00 USD | 1,230,000.00 USD | 678,150.00 USD | 62,290.00 USD | 98,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 1,070,000.00 USD | 1,070,000.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1920` | 393,190.00 USD | 393,190.00 USD | 0.00 USD | 0.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 516,300.00 USD | 516,300.00 USD | 168,540.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1930` | 384,440.00 USD | 384,440.00 USD | 0.00 USD | 2,420.00 USD | 18,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 331,360.00 USD | 331,360.00 USD | 0.00 USD | 0.00 USD | 331,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1940` | 363,490.00 USD | 363,490.00 USD | 21,310.00 USD | 356.90 USD | 341,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 342,910.00 USD | 342,910.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1940` | 685,810.00 USD | 685,810.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 403,280.00 USD | 403,280.00 USD | 0.00 USD | 1,890.00 USD | 401,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 806,550.00 USD | 806,550.00 USD | 0.00 USD | 1,890.00 USD | 401,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1950` | 1,570,000.00 USD | 1,570,000.00 USD | 681,420.00 USD | 1,990.00 USD | 203,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1960` | 2,250,000.00 USD | 2,250,000.00 USD | 596,440.00 USD | 255,590.00 USD | 595,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 3,400,000.00 USD | 3,400,000.00 USD | 430,170.00 USD | 158,320.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 104.93 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 3,230,000.00 USD | 3,230,000.00 USD | 288,590.00 USD | 260,510.00 USD | 431,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1970` | 3,990,000.00 USD | 3,990,000.00 USD | 65,930.00 USD | 164,750.00 USD | 354,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1980` | 4,310,000.00 USD | 4,310,000.00 USD | 420,330.00 USD | 132,650.00 USD | 522,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1980` | 4,730,000.00 USD | 4,730,000.00 USD | 312,350.00 USD | 44,250.00 USD | 383,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 443.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 4,990,000.00 USD | 4,990,000.00 USD | 241,080.00 USD | 74,740.00 USD | 364,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1990` | 5,040,000.00 USD | 5,040,000.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 696.54 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 5,950,000.00 USD | 5,950,000.00 USD | 426,270.00 USD | 100,110.00 USD | 431,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2000` | 5,620,000.00 USD | 5,620,000.00 USD | 153,280.00 USD | 61,070.00 USD | 371,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 3,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 6,830,000.00 USD | 6,830,000.00 USD | 255,670.00 USD | 235,120.00 USD | 391,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 6,470,000.00 USD | 6,470,000.00 USD | 361,660.00 USD | 91,810.00 USD | 399,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 3,860.00 USD | 7,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 7,400,000.00 USD | 7,400,000.00 USD | 230,470.00 USD | 87,910.00 USD | 245,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 7,150,000.00 USD | 7,150,000.00 USD | 91,080.00 USD | 52,660.00 USD | 529,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 2,640.00 USD | 9,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 7,790,000.00 USD | 7,790,000.00 USD | 145,200.00 USD | 97,440.00 USD | 154,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 7,420,000.00 USD | 7,420,000.00 USD | 22,590.00 USD | 94,230.00 USD | 153,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 8,080,000.00 USD | 8,080,000.00 USD | 82,750.00 USD | 73,360.00 USD | 129,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 7,560,000.00 USD | 7,560,000.00 USD | 62,650.00 USD | 76,780.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 8,260,000.00 USD | 8,260,000.00 USD | 90,000.00 USD | 32,500.00 USD | 58,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 7,660,000.00 USD | 7,660,000.00 USD | 39,740.00 USD | 1,630.00 USD | 57,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2055` | 617.73 USD | 10,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2060` | 8,700,000.00 USD | 8,700,000.00 USD | 314,030.00 USD | 32,110.00 USD | 91,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 7,850,000.00 USD | 7,850,000.00 USD | 154,800.00 USD | 18,480.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2065` | 214.55 USD | 10,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2070` | 9,160,000.00 USD | 9,160,000.00 USD | 195,950.00 USD | 81,580.00 USD | 183,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 8,470,000.00 USD | 8,470,000.00 USD | 441,660.00 USD | 141,790.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 9,490,000.00 USD | 9,490,000.00 USD | 218,960.00 USD | 70,470.00 USD | 39,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 9,150,000.00 USD | 9,150,000.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 10,360,000.00 USD | 10,360,000.00 USD | 456,020.00 USD | 147,490.00 USD | 272,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 12,100,000.00 USD | 12,100,000.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 11,110,000.00 USD | 11,110,000.00 USD | 448,900.00 USD | 92,790.00 USD | 203,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 16,180,000.00 USD | 16,180,000.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2105` | 218.71 USD | 10,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2110` | 11,450,000.00 USD | 11,450,000.00 USD | 153,880.00 USD | 48,270.00 USD | 135,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 19,400,000.00 USD | 19,400,000.00 USD | 1,090,000.00 USD | 518,310.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 11,870,000.00 USD | 11,870,000.00 USD | 163,120.00 USD | 100,480.00 USD | 158,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 22,450,000.00 USD | 22,450,000.00 USD | 1,170,000.00 USD | 492,740.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2125` | 153.21 USD | 10,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2130` | 12,250,000.00 USD | 12,250,000.00 USD | 206,790.00 USD | 60,670.00 USD | 112,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 25,290,000.00 USD | 25,290,000.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 12,430,000.00 USD | 12,430,000.00 USD | 126,930.00 USD | 31,520.00 USD | 25,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 27,390,000.00 USD | 27,390,000.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 12,500,000.00 USD | 12,500,000.00 USD | 45,180.00 USD | 8,240.00 USD | 18,400.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `0.1415` | 110,090,000.00 USD | 0.00 USD | 1,050.00 USD | `-27.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 110,090,000.00 USD | 0.00 USD | 351.26 USD | `-26.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 110,090,000.00 USD | 0.00 USD | 1,600.00 USD | `-26.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 110,080,000.00 USD | 0.00 USD | 10,400.00 USD | `-25.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 110,070,000.00 USD | 0.00 USD | 5,980.00 USD | `-23.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 110,070,000.00 USD | 0.00 USD | 303.26 USD | `-22.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 110,070,000.00 USD | 0.00 USD | 3,230.00 USD | `-22.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 110,060,000.00 USD | 0.00 USD | 6,380.00 USD | `-21.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 110,060,000.00 USD | 0.00 USD | 126.54 USD | `-20.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 110,060,000.00 USD | 0.00 USD | 1,790.00 USD | `-20.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 110,060,000.00 USD | 0.00 USD | 6,260.00 USD | `-19.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 110,050,000.00 USD | 0.00 USD | 552.21 USD | `-18.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 110,050,000.00 USD | 0.00 USD | 166.84 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 110,050,000.00 USD | 0.00 USD | 10,270.00 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 110,040,000.00 USD | 0.00 USD | 769.39 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 110,040,000.00 USD | 0.00 USD | 24,760.00 USD | `-16.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 110,010,000.00 USD | 0.00 USD | 6,540.00 USD | `-16.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 110,010,000.00 USD | 0.00 USD | 1,550.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 110,010,000.00 USD | 0.00 USD | 452.97 USD | `-15.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 110,000,000.00 USD | 0.00 USD | 12,640.00 USD | `-14.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 109,990,000.00 USD | 0.00 USD | 317.92 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 109,990,000.00 USD | 0.00 USD | 4,270.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 109,990,000.00 USD | 0.00 USD | 813.97 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 109,990,000.00 USD | 0.00 USD | 1,220.00 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 109,990,000.00 USD | 0.00 USD | 640.67 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 109,990,000.00 USD | 0.00 USD | 595.80 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
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
| `Sell Stop` | `0.1845` | 37,350.00 USD | 0.00 USD | 2,610.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 34,740.00 USD | 0.00 USD | 805.63 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 33,940.00 USD | 0.00 USD | 1,420.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 32,520.00 USD | 0.00 USD | 528.38 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 31,990.00 USD | 0.00 USD | 3,100.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 28,890.00 USD | 0.00 USD | 19,340.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 9,550.00 USD | 0.00 USD | 1,450.00 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 8,100.00 USD | 0.00 USD | 4,700.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 3,410.00 USD | 0.00 USD | 224.07 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 3,180.00 USD | 0.00 USD | 3,010.00 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 171.55 USD | 0.00 USD | 171.55 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 549.75 USD | 549.75 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 4,200.00 USD | 3,660.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 6,320.00 USD | 2,110.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 7,290.00 USD | 968.08 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 8,410.00 USD | 1,120.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 25,270.00 USD | 16,860.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 71,610.00 USD | 46,340.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 73,440.00 USD | 1,840.00 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 84,720.00 USD | 11,280.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 87,630.00 USD | 2,910.00 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 89,790.00 USD | 2,160.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 105,270.00 USD | 15,490.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 105,590.00 USD | 312.70 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 113,930.00 USD | 8,340.00 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 121,920.00 USD | 7,990.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 143,990.00 USD | 22,070.00 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 163,820.00 USD | 19,820.00 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 170,520.00 USD | 6,700.00 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 174,710.00 USD | 4,190.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 175,680.00 USD | 965.25 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 185,980.00 USD | 10,300.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 186,590.00 USD | 609.66 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 186,700.00 USD | 109.91 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 202,160.00 USD | 15,460.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 204,930.00 USD | 2,760.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 206,570.00 USD | 1,650.00 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 215,750.00 USD | 9,180.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 219,500.00 USD | 3,750.00 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 219,620.00 USD | 114.50 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 219,960.00 USD | 339.60 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 220,070.00 USD | 109.40 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 220,220.00 USD | 151.06 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 229,360.00 USD | 9,140.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 230,020.00 USD | 662.92 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 230,360.00 USD | 337.06 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 230,530.00 USD | 171.12 USD | 0.00 USD | `+19.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 230,630.00 USD | 101.11 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 231,740.00 USD | 1,110.00 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 241,160.00 USD | 9,420.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 241,610.00 USD | 443.91 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 242,380.00 USD | 778.76 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 242,580.00 USD | 192.71 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 243,090.00 USD | 514.45 USD | 0.00 USD | `+22.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 243,300.00 USD | 209.72 USD | 0.00 USD | `+23.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 243,420.00 USD | 115.92 USD | 0.00 USD | `+23.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 243,650.00 USD | 236.19 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 244,800.00 USD | 1,150.00 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 245,090.00 USD | 288.22 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 245,580.00 USD | 491.03 USD | 0.00 USD | `+26.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 246,900.00 USD | 1,320.00 USD | 0.00 USD | `+26.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 256,840.00 USD | 9,940.00 USD | 0.00 USD | `+27.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 257,340.00 USD | 499.00 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 258,440.00 USD | 1,100.00 USD | 0.00 USD | `+28.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 258,610.00 USD | 168.76 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 260,780.00 USD | 2,170.00 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 262,480.00 USD | 1,700.00 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 262,750.00 USD | 271.44 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 683,510.00 USD | 420,750.00 USD | 0.00 USD | `+33.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 684,690.00 USD | 1,180.00 USD | 0.00 USD | `+35.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 693,580.00 USD | 8,890.00 USD | 0.00 USD | `+37.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 708,440.00 USD | 14,860.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 709,780.00 USD | 1,340.00 USD | 0.00 USD | `+38.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 712,490.00 USD | 2,710.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 726,360.00 USD | 13,870.00 USD | 0.00 USD | `+40.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 731,580.00 USD | 5,220.00 USD | 0.00 USD | `+40.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 732,750.00 USD | 1,170.00 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 736,900.00 USD | 4,150.00 USD | 0.00 USD | `+42.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 737,850.00 USD | 944.99 USD | 0.00 USD | `+43.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 738,050.00 USD | 198.73 USD | 0.00 USD | `+45.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 739,420.00 USD | 1,370.00 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 740,500.00 USD | 1,080.00 USD | 0.00 USD | `+47.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 755,480.00 USD | 14,980.00 USD | 0.00 USD | `+48.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 756,710.00 USD | 1,230.00 USD | 0.00 USD | `+49.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 758,160.00 USD | 1,440.00 USD | 0.00 USD | `+52.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 758,510.00 USD | 355.21 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 765,170.00 USD | 6,650.00 USD | 0.00 USD | `+54.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 784,140.00 USD | 18,980.00 USD | 0.00 USD | `+56.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 788,290.00 USD | 4,150.00 USD | 0.00 USD | `+58.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 791,540.00 USD | 3,250.00 USD | 0.00 USD | `+61.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 792,030.00 USD | 493.89 USD | 0.00 USD | `+66.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 792,210.00 USD | 181.30 USD | 0.00 USD | `+66.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 793,600.00 USD | 1,380.00 USD | 0.00 USD | `+68.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 805,890.00 USD | 12,290.00 USD | 0.00 USD | `+70.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 806,000.00 USD | 111.06 USD | 0.00 USD | `+70.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 806,220.00 USD | 220.61 USD | 0.00 USD | `+75.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 809,560.00 USD | 3,340.00 USD | 0.00 USD | `+79.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 809,750.00 USD | 188.75 USD | 0.00 USD | `+93.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 810,660.00 USD | 909.54 USD | 0.00 USD | `+94.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 810,780.00 USD | 121.76 USD | 0.00 USD | `+95.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 810,920.00 USD | 141.78 USD | 0.00 USD | `+99.65%` | `TACTICAL (Retail Cluster)` |

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
| `1D` | `0.1730` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 115,290.00 USD | 33,150.00 USD | 137,700.00 USD |
| `7D` | `0.1730` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 32,310.00 USD | 6,910.00 USD | 82,340.00 USD |
| `1D` | `0.1740` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 56,600.00 USD | 30,930.00 USD | 33,240.00 USD |
| `7D` | `0.1740` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 10,400.00 USD | 29,910.00 USD | 48,080.00 USD |
| `1D` | `0.1750` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 50,710.00 USD | 17,820.00 USD | 39,090.00 USD |
| `7D` | `0.1750` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 7,610.00 USD | 6,730.00 USD | 39,280.00 USD |
| `1D` | `0.1760` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 45,460.00 USD | 8,400.00 USD | 25,200.00 USD |
| `7D` | `0.1760` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 3,480.00 USD | 13,510.00 USD | 1,140.00 USD |
| `1D` | `0.1770` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 208,040.00 USD | 35,120.00 USD | 63,080.00 USD |
| `7D` | `0.1770` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 140,320.00 USD | 34,230.00 USD | 81,310.00 USD |
| `1D` | `0.1780` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 70,380.00 USD | 13,120.00 USD | 38,130.00 USD |
| `7D` | `0.1780` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 140,230.00 USD | 13,120.00 USD | 56,120.00 USD |
| `1D` | `0.1790` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 114,060.00 USD | 42,720.00 USD | 92,380.00 USD |
| `7D` | `0.1790` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 12,380.00 USD | 28,450.00 USD | 116,120.00 USD |
| `1D` | `0.1800` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 724,590.00 USD | 95,980.00 USD | 178,290.00 USD |
| `7D` | `0.1800` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 469,140.00 USD | 95,830.00 USD | 141,980.00 USD |
| `1D` | `0.1810` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 150,850.00 USD | 56,840.00 USD | 146,210.00 USD |
| `7D` | `0.1810` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 356,840.00 USD | 46,600.00 USD | 179,050.00 USD |
| `1D` | `0.1820` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 435,080.00 USD | 95,510.00 USD | 340,800.00 USD |
| `7D` | `0.1820` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 126,700.00 USD | 63,070.00 USD | 444,200.00 USD |
| `1D` | `0.1830` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 439,340.00 USD | 45,220.00 USD | 70,670.00 USD |
| `7D` | `0.1830` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 441,880.00 USD | 47,220.00 USD | 32,460.00 USD |
| `1D` | `0.1840` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 444,800.00 USD | 111,410.00 USD | 204,780.00 USD |
| `7D` | `0.1840` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 373,060.00 USD | 64,640.00 USD | 192,770.00 USD |
| `1D` | `0.1850` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 154,260.00 USD | 112,070.00 USD | 186,670.00 USD |
| `7D` | `0.1850` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 76,160.00 USD | 72,320.00 USD | 267,580.00 USD |
| `1D` | `0.1860` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 171,980.00 USD | 55,740.00 USD | 513,310.00 USD |
| `7D` | `0.1860` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 70,810.00 USD | 15,200.00 USD | 39,200.00 USD |
| `1D` | `0.1870` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 80,170.00 USD | 38,000.00 USD | 502,330.00 USD |
| `7D` | `0.1870` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 69,260.00 USD | 36,800.00 USD | 383,690.00 USD |
| `1D` | `0.1880` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 360,930.00 USD | 232,420.00 USD | 260,760.00 USD |
| `7D` | `0.1880` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 325,960.00 USD | 148,540.00 USD | 670,720.00 USD |
| `1D` | `0.1890` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 410,160.00 USD | 182,950.00 USD | 225,970.00 USD |
| `7D` | `0.1890` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 562,390.00 USD | 144,640.00 USD | 111,430.00 USD |
| `1D` | `0.1900` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 103,950.00 USD | 150,420.00 USD | 454,770.00 USD |
| `7D` | `0.1900` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 255,740.00 USD | 30,390.00 USD | 284,570.00 USD |
| `1D` | `0.1910` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 678,150.00 USD | 62,290.00 USD | 98,270.00 USD |
| `7D` | `0.1910` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 464,200.00 USD | 31,510.00 USD | 57,950.00 USD |
| `1D` | `0.1920` | 393,190.00 USD | 0.00 USD | 393,190.00 USD | 0.00 USD | 0.00 USD | 8,750.00 USD |
| `7D` | `0.1920` | 516,300.00 USD | 0.00 USD | 516,300.00 USD | 168,540.00 USD | 0.00 USD | 16,400.00 USD |
| `1D` | `0.1930` | 384,440.00 USD | 0.00 USD | 384,440.00 USD | 0.00 USD | 2,420.00 USD | 18,530.00 USD |
| `7D` | `0.1930` | 331,360.00 USD | 0.00 USD | 331,360.00 USD | 0.00 USD | 0.00 USD | 331,360.00 USD |
| `1D` | `0.1940` | 363,490.00 USD | 0.00 USD | 363,490.00 USD | 21,310.00 USD | 356.90 USD | 341,820.00 USD |
| `7D` | `0.1940` | 342,910.00 USD | 342,910.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `7D` | `0.1940` | 685,810.00 USD | 685,810.00 USD | 0.00 USD | 150,130.00 USD | 0.00 USD | 192,780.00 USD |
| `1D` | `0.1950` | 403,280.00 USD | 403,280.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD | 401,380.00 USD |
| `1D` | `0.1950` | 806,550.00 USD | 806,550.00 USD | 0.00 USD | 0.00 USD | 1,890.00 USD | 401,380.00 USD |
| `7D` | `0.1950` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 681,420.00 USD | 1,990.00 USD | 203,120.00 USD |
| `1D` | `0.1960` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 596,440.00 USD | 255,590.00 USD | 595,680.00 USD |
| `7D` | `0.1960` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 430,170.00 USD | 158,320.00 USD | 1,240,000.00 USD |
| `1D` | `0.1970` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 288,590.00 USD | 260,510.00 USD | 431,200.00 USD |
| `7D` | `0.1970` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 65,930.00 USD | 164,750.00 USD | 354,550.00 USD |
| `1D` | `0.1980` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 420,330.00 USD | 132,650.00 USD | 522,530.00 USD |
| `7D` | `0.1980` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 312,350.00 USD | 44,250.00 USD | 383,190.00 USD |
| `1D` | `0.1990` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 241,080.00 USD | 74,740.00 USD | 364,950.00 USD |
| `7D` | `0.1990` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 85,070.00 USD | 42,030.00 USD | 181,030.00 USD |
| `1D` | `0.2000` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 426,270.00 USD | 100,110.00 USD | 431,950.00 USD |
| `7D` | `0.2000` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 153,280.00 USD | 61,070.00 USD | 371,130.00 USD |
| `1D` | `0.2010` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 255,670.00 USD | 235,120.00 USD | 391,010.00 USD |
| `7D` | `0.2010` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 361,660.00 USD | 91,810.00 USD | 399,110.00 USD |
| `1D` | `0.2020` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 230,470.00 USD | 87,910.00 USD | 245,930.00 USD |
| `7D` | `0.2020` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 91,080.00 USD | 52,660.00 USD | 529,150.00 USD |
| `1D` | `0.2030` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 145,200.00 USD | 97,440.00 USD | 154,740.00 USD |
| `7D` | `0.2030` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 22,590.00 USD | 94,230.00 USD | 153,910.00 USD |
| `1D` | `0.2040` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 82,750.00 USD | 73,360.00 USD | 129,280.00 USD |
| `7D` | `0.2040` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 62,650.00 USD | 76,780.00 USD | 6,560.00 USD |
| `1D` | `0.2050` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 90,000.00 USD | 32,500.00 USD | 58,260.00 USD |
| `7D` | `0.2050` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 39,740.00 USD | 1,630.00 USD | 57,550.00 USD |
| `1D` | `0.2060` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 314,030.00 USD | 32,110.00 USD | 91,880.00 USD |
| `7D` | `0.2060` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 154,800.00 USD | 18,480.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 195,950.00 USD | 81,580.00 USD | 183,390.00 USD |
| `7D` | `0.2070` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 441,660.00 USD | 141,790.00 USD | 35,600.00 USD |
| `1D` | `0.2080` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 218,960.00 USD | 70,470.00 USD | 39,190.00 USD |
| `7D` | `0.2080` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 594,380.00 USD | 53,900.00 USD | 36,940.00 USD |
| `1D` | `0.2090` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 456,020.00 USD | 147,490.00 USD | 272,040.00 USD |
| `7D` | `0.2090` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 2,270,000.00 USD | 213,740.00 USD | 459,850.00 USD |
| `1D` | `0.2100` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 448,900.00 USD | 92,790.00 USD | 203,540.00 USD |
| `7D` | `0.2100` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 1,730,000.00 USD | 690,390.00 USD | 1,660,000.00 USD |
| `1D` | `0.2110` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 153,880.00 USD | 48,270.00 USD | 135,890.00 USD |
| `7D` | `0.2110` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 1,090,000.00 USD | 518,310.00 USD | 1,620,000.00 USD |
| `1D` | `0.2120` | 11,870,000.00 USD | 11,870,000.00 USD | 0.00 USD | 163,120.00 USD | 100,480.00 USD | 158,810.00 USD |
| `7D` | `0.2120` | 22,450,000.00 USD | 22,450,000.00 USD | 0.00 USD | 1,170,000.00 USD | 492,740.00 USD | 1,390,000.00 USD |
| `1D` | `0.2130` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 206,790.00 USD | 60,670.00 USD | 112,450.00 USD |
| `7D` | `0.2130` | 25,290,000.00 USD | 25,290,000.00 USD | 0.00 USD | 1,220,000.00 USD | 353,690.00 USD | 1,260,000.00 USD |
| `1D` | `0.2140` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 126,930.00 USD | 31,520.00 USD | 25,900.00 USD |
| `7D` | `0.2140` | 27,390,000.00 USD | 27,390,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 826,790.00 USD |
| `1D` | `0.2150` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 45,180.00 USD | 8,240.00 USD | 18,400.00 USD |
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
  * Total Open Interest: `416.91M` | Total OI Tokens: `2,134,822,146.4 ADA`
  * 1h OI Change: `+1.37%` | 4h OI Change: `+0.85%` | 24h OI Change: `-7.21%`
  * Exchange Breakdown: Binance=`75.63M` | Bybit=`50.71M` | OKX=`29.63M` | Hyperliquid=`28.35M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.83K` | Last 24h: `30.56K` | Last 3d: `64.45K` | Last 7d: `83.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0059%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `56.84%` | `43.16%` | `1.32` | 7,650,000.00 USD |
| `15M` | `Binance` | `54.8%` | `45.2%` | `1.21` | 2,240,000.00 USD |
| `15M` | `OKX` | `70.44%` | `29.56%` | `2.38` | 1,110,000.00 USD |
| `15M` | `Bybit` | `70.02%` | `29.98%` | `2.34` | 775,780.00 USD |
| `15M` | `KuCoin` | `47.1%` | `52.9%` | `0.89` | 277,020.00 USD |
| `15M` | `Gate` | `66.52%` | `33.48%` | `1.99` | 297,750.00 USD |
| `15M` | `Bitget` | `37.32%` | `62.68%` | `0.60` | 190,340.00 USD |
| `15M` | `BingX` | `64.16%` | `35.84%` | `1.79` | 137,110.00 USD |
| `15M` | `MEXC` | `61.53%` | `38.47%` | `1.60` | 976,550.00 USD |
| `15M` | `Bitunix` | `75.8%` | `24.2%` | `3.13` | 185,600.00 USD |
| `15M` | `Hyperliquid` | `46.5%` | `53.5%` | `0.87` | 32,630.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.67%` | `56.33%` | `0.78` | 1,100,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 222,890.00 USD |
| `15M` | `HTX` | `40.14%` | `59.86%` | `0.67` | 24,710.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `74.74%` | `25.26%` | `2.96` | 78,000.00 USD |
| `15M` | `Aster` | `68.96%` | `31.04%` | `2.22` | 2,830.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `94.45%` | `5.55%` | `17.02` | 4,560.00 USD |
| `15M` | `Whale Positions` | `54.8%` | `45.2%` | `1.21` | 2,240,000.00 USD |
| `15M` | `Global Accounts` | `56.84%` | `43.16%` | `1.32` | 7,650,000.00 USD |
| `1H` | `ADA` | `53.42%` | `46.58%` | `1.15` | 22,110,000.00 USD |
| `1H` | `Binance` | `56.54%` | `43.46%` | `1.30` | 6,610,000.00 USD |
| `1H` | `OKX` | `63.19%` | `36.81%` | `1.72` | 2,500,000.00 USD |
| `1H` | `Bybit` | `60.71%` | `39.29%` | `1.55` | 2,530,000.00 USD |
| `1H` | `KuCoin` | `46.46%` | `53.54%` | `0.87` | 540,000.00 USD |
| `1H` | `Gate` | `72.56%` | `27.44%` | `2.64` | 686,230.00 USD |
| `1H` | `Bitget` | `50.59%` | `49.41%` | `1.02` | 728,880.00 USD |
| `1H` | `BingX` | `27.99%` | `72.01%` | `0.39` | 891,940.00 USD |
| `1H` | `MEXC` | `60.63%` | `39.37%` | `1.54` | 2,130,000.00 USD |
| `1H` | `Bitunix` | `68.68%` | `31.32%` | `2.19` | 489,790.00 USD |
| `1H` | `Hyperliquid` | `77.36%` | `22.64%` | `3.42` | 355,210.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.01%` | `53.99%` | `0.85` | 3,160,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,140,000.00 USD |
| `1H` | `HTX` | `49.31%` | `50.69%` | `0.97` | 62,260.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `74.56%` | `25.44%` | `2.93` | 261,900.00 USD |
| `1H` | `Aster` | `22.92%` | `77.08%` | `0.30` | 11,560.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `66.8%` | `33.2%` | `2.01` | 6,510.00 USD |
| `1H` | `Whale Positions` | `56.54%` | `43.46%` | `1.30` | 6,610,000.00 USD |
| `1H` | `Global Accounts` | `53.42%` | `46.58%` | `1.15` | 22,110,000.00 USD |
| `4H` | `ADA` | `48.10%` | `51.90%` | `0.93` | 74,320,000.00 USD |
| `4H` | `Binance` | `51.54%` | `48.46%` | `1.06` | 23,730,000.00 USD |
| `4H` | `OKX` | `53.34%` | `46.66%` | `1.14` | 6,510,000.00 USD |
| `4H` | `Bybit` | `55.43%` | `44.57%` | `1.24` | 6,340,000.00 USD |
| `4H` | `KuCoin` | `49.07%` | `50.93%` | `0.96` | 1,250,000.00 USD |
| `4H` | `Gate` | `60.03%` | `39.97%` | `1.50` | 2,510,000.00 USD |
| `4H` | `Bitget` | `47.28%` | `52.72%` | `0.90` | 1,910,000.00 USD |
| `4H` | `BingX` | `37.6%` | `62.4%` | `0.60` | 5,430,000.00 USD |
| `4H` | `MEXC` | `47.86%` | `52.14%` | `0.92` | 7,640,000.00 USD |
| `4H` | `Bitunix` | `53.39%` | `46.61%` | `1.15` | 1,690,000.00 USD |
| `4H` | `Hyperliquid` | `47.51%` | `52.49%` | `0.91` | 1,140,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.6%` | `51.4%` | `0.95` | 11,460,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `3.3%` | `96.7%` | `0.03` | 3,610,000.00 USD |
| `4H` | `HTX` | `53.82%` | `46.18%` | `1.17` | 308,580.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `64.05%` | `35.95%` | `1.78` | 689,840.00 USD |
| `4H` | `Aster` | `26.4%` | `73.6%` | `0.36` | 33,740.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `82.29%` | `17.71%` | `4.65` | 75,150.00 USD |
| `4H` | `Whale Positions` | `51.54%` | `48.46%` | `1.06` | 23,730,000.00 USD |
| `4H` | `Global Accounts` | `48.10%` | `51.90%` | `0.93` | 74,320,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1920` | `0.1923` | `0.1920` | `0.1930` | `0.1916` | 1,687,367.20 USD | 1,122,865.28 USD | 564,501.92 USD | 558,363.36 USD | `+33.09%` | `5B / 0S` |
| `0:00 UTC` | `0.1925` | `0.1926` | `0.1925` | `0.1930` | `0.1921` | 1,372,988.82 USD | 626,720.98 USD | 746,267.84 USD | -119,546.86 USD | `-8.71%` | `0B / 1S` |
| `5:00 UTC` | `0.1918` | `0.1920` | `0.1918` | `0.1925` | `0.1916` | 742,501.25 USD | 301,932.71 USD | 440,568.55 USD | -138,635.84 USD | `-18.67%` | `1B / 1S` |
| `0:00 UTC` | `0.1925` | `0.1922` | `0.1925` | `0.1930` | `0.1915` | 1,936,754.49 USD | 922,725.13 USD | 1,014,029.36 USD | -91,304.23 USD | `-4.71%` | `1B / 3S` |
| `5:00 UTC` | `0.1925` | `0.1925` | `0.1925` | `0.1928` | `0.1920` | 818,438.28 USD | 477,644.62 USD | 340,793.66 USD | 136,850.96 USD | `+16.72%` | `0B / 0S` |
| `0:00 UTC` | `0.1928` | `0.1927` | `0.1928` | `0.1930` | `0.1925` | 1,279,303.19 USD | 647,276.72 USD | 632,026.47 USD | 15,250.26 USD | `+1.19%` | `0B / 0S` |
| `5:00 UTC` | `0.1926` | `0.1928` | `0.1926` | `0.1933` | `0.1925` | 1,103,210.95 USD | 609,025.54 USD | 494,185.40 USD | 114,840.14 USD | `+10.41%` | `1B / 0S` |
| `0:00 UTC` | `0.1935` | `0.1936` | `0.1935` | `0.1941` | `0.1926` | 1,737,432.33 USD | 982,431.45 USD | 755,000.88 USD | 227,430.57 USD | `+13.09%` | `2B / 0S` |
| `5:00 UTC` | `0.1951` | `0.1945` | `0.1951` | `0.1951` | `0.1935` | 1,638,885.40 USD | 1,017,708.87 USD | 621,176.53 USD | 396,532.35 USD | `+24.20%` | `5B / 0S` |
| `0:00 UTC` | `0.1951` | `0.1950` | `0.1951` | `0.1955` | `0.1945` | 907,328.84 USD | 357,544.27 USD | 549,784.57 USD | -192,240.30 USD | `-21.19%` | `0B / 3S` |

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
| `5m` | 76,380.00 USD | 573,270.00 USD | **`ACCUMULATION`** |
| `15m` | 434,200.00 USD | 1,060,000.00 USD | **`ACCUMULATION`** |
| `30m` | 736,880.00 USD | 1,590,000.00 USD | **`ACCUMULATION`** |
| `1h` | 820,120.00 USD | 2,160,000.00 USD | **`ACCUMULATION`** |
| `2h` | 779,460.00 USD | 2,030,000.00 USD | **`ACCUMULATION`** |
| `4h` | 389,810.00 USD | 2,150,000.00 USD | **`ACCUMULATION`** |
| `6h` | 739,700.00 USD | 2,320,000.00 USD | **`ACCUMULATION`** |
| `8h` | 477,990.00 USD | 3,940,000.00 USD | **`ACCUMULATION`** |
| `12h` | -2,510,000.00 USD | 1,990,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,930,000.00 USD | -7,700,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,890,000.00 USD | -37,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,480,000.00 USD | -195,360,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+76.38K` | 15m=`+434.20K` | 1h=`+820.12K` | 24h=`-7.93M`
* Futures Capital Netflows: 5m=`+573.27K` | 15m=`+1.06M` | 1h=`+2.16M` | 24h=`-7.70M`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `-1.02` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.20`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1939` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.40` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.81`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1963`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
